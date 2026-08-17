#!/usr/bin/env python3
"""Build machine-readable catalog sidecars for a country's MH catalogs.

Usage:
    build_catalogs.py <country> <catalogs_xlsx> [--pdf <catalogs_pdf_txt>]

Parses the extracted catalogs workbook text (produced by extract_text.py)
into one CSV per catalog: <cc>/requirements/catalogs/CAT-XXX_<slug>.csv
with columns code,value. Overlays corrections parsed from the extracted
catalogs PDF text where the workbook is known-incomplete.

Writes an _INDEX.md documenting source, counts, and applied corrections.
Sources are never modified; re-run anytime the source version changes.
"""

import csv
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# Catalog display names / slugs.
# v1.1 (2026 re-versioning) — matches Catálogos Facturación Electrónica v1.1:
# CAT-002 now includes DTE AND event types (17/18); CAT-008 = Distrito (no longer
# deleted); CAT-023 = Operaciones Especiales (replaces Tipo Doc. Contingencia);
# CAT-024 renamed "Motivo del evento"; new CAT-033 Tipo de Régimen (+ customs
# regimes), and more beyond 033 are emitted generically when present.
CATALOGS = {
    "CAT-001": "ambiente-destino",
    "CAT-002": "tipo-documento-evento",
    "CAT-003": "modelo-facturacion",
    "CAT-004": "tipo-transmision",
    "CAT-005": "tipo-contingencia",
    "CAT-006": "retencion-iva-mh",
    "CAT-007": "tipo-generacion-documento",
    "CAT-008": "distrito",
    "CAT-009": "tipo-establecimiento",
    "CAT-010": "servicio-medico",
    "CAT-011": "tipo-item",
    "CAT-012": "departamento",
    "CAT-013": "municipio",
    "CAT-014": "unidad-medida",
    "CAT-015": "tributos",
    "CAT-016": "condicion-operacion",
    "CAT-017": "forma-pago",
    "CAT-018": "plazo",
    "CAT-019": "actividad-economica",
    "CAT-020": "pais",
    "CAT-021": "documentos-asociados",
    "CAT-022": "tipo-documento-receptor",
    "CAT-023": "operaciones-especiales",
    "CAT-024": "motivo-evento",
    "CAT-025": "titulo-remision-bienes",
    "CAT-026": "tipo-donacion",
    "CAT-027": "recinto-fiscal",
    "CAT-028": "regimen",
    "CAT-029": "tipo-persona",
    "CAT-030": "transporte",
    "CAT-031": "incoterms",
    "CAT-032": "domicilio-fiscal",
    "CAT-033": "tipo-regimen",
}

# Fallback slugs for catalogs present in a source but not in the map (e.g.
# future CAT-034+): derive from the header line text.
def slugify(text: str) -> str:
    import re
    s = re.sub(r"[^a-záéíóúñA-ZÁÉÍÓÚÑ0-9 ]", "", text.lower())
    return "-".join(s.split())[:40]

CAT_RE = re.compile(r"^(CAT-\d{3})\b[^;]*;?\s*$")
CODE_RE = re.compile(r"^([^;]+);(.*)$")
SECTION_RE = re.compile(r"^(\d)-\s+(.*)$")


def parse_workbook(txt: str):
    catalogs = {}
    current = None
    section = ""
    for line in txt.splitlines():
        line = line.strip()
        m = CAT_RE.match(line)
        if m:
            current = m.group(1)
            section = ""
            catalogs.setdefault(current, [])
            continue
        if current is None or line in ("Código;Valores",):
            continue
        sec = SECTION_RE.match(line.rstrip(";"))
        if sec:
            section = sec.group(2).strip()
            continue
        c = CODE_RE.match(line)
        if c:
            code = c.group(1).strip()
            value = unicodedata.normalize("NFC", c.group(2).strip())
            catalogs[current].append((code, value, section))
    return catalogs


def parse_pdf(txt: str):
    """Parse the PDF extraction (markdown table format: | code | value |)."""
    catalogs = {}
    current = None
    for line in txt.splitlines():
        s = line.strip()
        m = re.match(r"^(CAT[- ]\d{3})\b", s.replace("CAT ", "CAT-"))
        if m and ("|" not in s or s.startswith("###") or s.startswith("CAT")):
            key = m.group(1).replace(" ", "-")
            # Only treat as catalog header lines like '### **CAT-001 ...' or 'CAT-001 ...;'
            if s.startswith("###") or s.endswith(";") or "|" not in s:
                current = key
                catalogs.setdefault(current, [])
                continue
        if current is None:
            continue
        row = re.match(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|$", s)
        if row:
            code, value = row.group(1), row.group(2)
            if code in ("Código", ":---", "---", ":---:", ""):
                continue
            catalogs[current].append(
                (code.strip(), unicodedata.normalize("NFC", value.strip()), "")
            )
    return catalogs


def main() -> int:
    args = [a for a in sys.argv[1:]]
    pdf_txt = None
    if "--pdf" in args:
        i = args.index("--pdf")
        pdf_txt = Path(args[i + 1])
        del args[i : i + 2]
    if len(args) != 2:
        print(__doc__)
        return 2
    country, xlsx_txt = args[0], Path(args[1])
    if not xlsx_txt.exists():
        print(f"error: {xlsx_txt} not found", file=sys.stderr)
        return 2
    src = xlsx_txt.with_suffix("").name  # e.g. 25_Catalogos_Transmision_v1.2.xlsx
    out_dir = REPO / country / "requirements" / "catalogs"
    out_dir.mkdir(parents=True, exist_ok=True)

    wb = parse_workbook(xlsx_txt.read_text(encoding="utf-8"))
    pdf = parse_pdf(pdf_txt.read_text(encoding="utf-8")) if pdf_txt else {}

    corrections = []
    rows_written = {}
    # Merge mapped catalogs with any unmapped ones found in the source
    all_cats = dict(CATALOGS)
    for cat in wb:
        if cat not in all_cats:
            header = cat  # derive slug from raw "CAT-0XX Nombre;" line
            name = header.split(None, 1)[1].strip().rstrip(";") if " " in header else cat
            all_cats[cat] = slugify(name)
    for cat, slug in all_cats.items():
        entries = wb.get(cat, [])
        has_sections = any(sec for _, _, sec in entries)
        # Overlay: if workbook misses codes the PDF has, take PDF's full list
        if cat in pdf and {c for c, _, _ in pdf[cat]} - {c for c, _, _ in entries}:
            missing = {c for c, _, _ in pdf[cat]} - {c for c, _, _ in entries}
            corrections.append(
                f"{cat}: workbook missing codes {sorted(missing)}; used PDF list"
            )
            entries = pdf[cat]
        fname = out_dir / f"{cat}_{slug}.csv"
        with fname.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["code", "value"] + (["section"] if has_sections else []))
            for code, value, sec in entries:
                w.writerow([code, value] + ([sec] if has_sections else []))
        rows_written[cat] = len(entries)

    index = out_dir / "_INDEX.md"
    with index.open("w", encoding="utf-8") as f:
        f.write("# MH Catalogs — machine-readable sidecars\n\n")
        f.write(
            f"Generated by `shared/scripts/build_catalogs.py` from "
            f"`{country}/sources/{src}`"
            + (f" (overlay: PDF text)" if pdf_txt else "")
            + ".\nRegenerate after any source version change.\n\n"
        )
        f.write("| Catalog | File | Rows |\n|---|---|---|\n")
        for cat, slug in all_cats.items():
            f.write(f"| {cat} | `{cat}_{slug}.csv` | {rows_written[cat]} |\n")
        if corrections:
            f.write("\n## Corrections applied (workbook vs PDF)\n\n")
            for c in corrections:
                f.write(f"- {c}\n")
    print(f"wrote {len(rows_written)} catalogs to {out_dir}")
    for c in corrections:
        print(f"  CORRECTION: {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
