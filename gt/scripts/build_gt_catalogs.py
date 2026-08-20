#!/usr/bin/env python3
"""Build the FEL machine-readable catalog sidecars for Guatemala.

Reads BOTH publication channels' JSON catalogs from gt/sources/:
  - 29_FEL_XSD_cat_github_961133c/  (GitHub @ 961133c = working authority,
    per OQ3 ruling / master-index FEL authority preamble)
  - 30_FEL_XSD_cat_catdesa/         (cat.desa.sat.gob.gt)

and emits, into gt/requirements/catalogs/:
  - CAT-FRS_frases.csv            one row per frase        (GH 0.6.0: 12 tipos / 88 frases)
  - CAT-UGR_unidades-gravables.csv one row per unidad      (0.1.4: 12 impuestos / 43 unidades)
  - CAT-MSG_mensajes.csv           one row per mensaje     (0.3.0: 211 codes / 7 families)
  - _INDEX.md                      sidecar map + corrections log
  - _DRIFT.md                      every inter-channel difference, verbatim

Each CSV carries its source version string and "Ultima Actualizacion" header
date as columns (documented in _INDEX.md).

Deterministic and idempotent: re-running against the same sources reproduces
every output byte-identically (the generation date is a constant below, not a
clock read; bump it when regenerating after a source change). Sources are
never modified. Exits non-zero on unreadable or unexpected input.

Usage:
    python gt/scripts/build_gt_catalogs.py
"""

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

GH_DIR = REPO / "gt" / "sources" / "29_FEL_XSD_cat_github_961133c"
CD_DIR = REPO / "gt" / "sources" / "30_FEL_XSD_cat_catdesa"
OUT_DIR = REPO / "gt" / "requirements" / "catalogs"

# Bump this constant when regenerating after a source version change.
GENERATION_DATE = "2026-08-19"

GENERATION_COMMAND = "~/.venvs/localizations/bin/python gt/scripts/build_gt_catalogs.py"

FRASES_GH = "CatalogoFrases-0.6.0.json"
FRASES_CD = "CatalogoFrases-0.1.2.json"
UNIDADES = "catalogoUnidadesGravables-0.1.4.json"
MENSAJES = "catalogoMensajes-0.3.0.json"

# Frase boolean flag keys understood by this builder (schema-governed). An
# unknown flag key in a future source version is a hard error: new flags mean
# a source change that must go through the corrections log, not silence.
FRASE_FLAGS = [
    "retenerISR",
    "esAgenteRetenedor",
    "esPequenoContribuyente",
    "esRegimenElectronico",
    "esAgropecuario",
    "incluyeIVA",
    "contieneResolucion",
    "contieneFechaResolucion",
]

FRASE_FLAG_COLUMNS = {
    "retenerISR": "retener_isr",
    "esAgenteRetenedor": "es_agente_retenedor",
    "esPequenoContribuyente": "es_pequeno_contribuyente",
    "esRegimenElectronico": "es_regimen_electronico",
    "esAgropecuario": "es_agropecuario",
    "incluyeIVA": "incluye_iva",
    "contieneResolucion": "contiene_resolucion",
    "contieneFechaResolucion": "contiene_fecha_resolucion",
}


def fail(msg):
    print(f"build_gt_catalogs.py: ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except OSError as exc:
        fail(f"cannot read {path}: {exc}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")


def md5_of(path):
    try:
        return hashlib.md5(path.read_bytes()).hexdigest()
    except OSError as exc:
        fail(f"cannot hash {path}: {exc}")


def jdump(obj):
    """Deterministic verbatim JSON rendering for the drift record."""
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)


def fmt(value):
    """CSV cell: None/absent -> empty; bool stays python; numbers as parsed."""
    return "" if value is None else value


def bool_cell(value):
    if value is None:
        return ""
    return "true" if value else "false"


# --------------------------------------------------------------------------
# Frases
# --------------------------------------------------------------------------

def frases_rows(doc, version):
    """Flatten a CatalogoFrases document into CSV rows."""
    header = doc.get("cabecera") or {}
    actualizacion = header.get("Ultima Actualizacion", "")
    rows = []
    for tipo in doc["contenido"]["tiposFrases"]:
        for frase in tipo["frases"]:
            unknown = set(frase) - {"codigoEscenario", "escenario", "textoAColocar"} - set(FRASE_FLAGS)
            if unknown:
                fail(
                    f"{FRASES_GH}: unknown frase flag key(s) {sorted(unknown)} at tipo "
                    f"{tipo['codigoTipoFrase']} escenario {frase.get('codigoEscenario')} — "
                    "update FRASE_FLAGS and log the change in _INDEX.md"
                )
            row = {
                "version": version,
                "ultima_actualizacion": actualizacion,
                "tipo_frase": tipo["codigoTipoFrase"],
                "nombre_tipo": tipo["nombre"],
                "codigo_escenario": frase["codigoEscenario"],
                "escenario": frase["escenario"],
            }
            for flag in FRASE_FLAGS:
                row[FRASE_FLAG_COLUMNS[flag]] = bool_cell(frase.get(flag))
            row["texto_a_colocar"] = frase["textoAColocar"]
            rows.append(row)
    return rows, header


def frases_drift(gh_doc, cd_doc):
    """Every inter-channel difference between the two Frases catalogs."""
    out = []
    gh_head, cd_head = gh_doc["cabecera"], cd_doc["cabecera"]
    out.append(
        f"- Header: GH `{jdump(gh_head)}` vs CD `{jdump(cd_head)}` "
        "(same catalog name, different version vintage)."
    )
    gh_tipos = {t["codigoTipoFrase"]: t for t in gh_doc["contenido"]["tiposFrases"]}
    cd_tipos = {t["codigoTipoFrase"]: t for t in cd_doc["contenido"]["tiposFrases"]}
    for code in sorted(set(gh_tipos) | set(cd_tipos)):
        gh_t, cd_t = gh_tipos.get(code), cd_tipos.get(code)
        if gh_t and not cd_t:
            out.append(
                f"- Tipo {code}: GH-only `{gh_t['nombre']}` with {len(gh_t['frases'])} frases "
                "(absent from CD catalog)."
            )
        elif cd_t and not gh_t:
            out.append(
                f"- Tipo {code}: CD-only `{cd_t['nombre']}` with {len(cd_t['frases'])} frases."
            )
        else:
            bits = []
            if gh_t["nombre"] != cd_t["nombre"]:
                bits.append(f"nombre GH `{gh_t['nombre']}` vs CD `{cd_t['nombre']}`")
            if len(gh_t["frases"]) != len(cd_t["frases"]):
                bits.append(
                    f"frase count GH {len(gh_t['frases'])} vs CD {len(cd_t['frases'])}"
                )
            gh_fr = {f["codigoEscenario"]: f for f in gh_t["frases"]}
            cd_fr = {f["codigoEscenario"]: f for f in cd_t["frases"]}
            gh_only = sorted(set(gh_fr) - set(cd_fr))
            cd_only = sorted(set(cd_fr) - set(gh_fr))
            if gh_only:
                bits.append(f"GH-only escenarios {gh_only}")
            if cd_only:
                bits.append(f"CD-only escenarios {cd_only}")
            for esc in sorted(set(gh_fr) & set(cd_fr)):
                g, c = gh_fr[esc], cd_fr[esc]
                if g == c:
                    continue
                g_keys, c_keys = set(g), set(c)
                detail = []
                for key in sorted(g_keys & c_keys):
                    if g[key] != c[key]:
                        detail.append(f"{key}: GH `{jdump(g[key])}` vs CD `{jdump(c[key])}`")
                if g_keys - c_keys:
                    detail.append(f"GH-only keys {sorted(g_keys - c_keys)} = `{ {k: g[k] for k in sorted(g_keys - c_keys)} }`")  # noqa: E501
                if c_keys - g_keys:
                    detail.append(f"CD-only keys {sorted(c_keys - g_keys)}")
                bits.append(
                    f"escenario {esc} row differs ({'; '.join(detail) if detail else 'order/other'})"
                )
            if bits:
                out.append(f"- Tipo {code} (`{gh_t['nombre']}`): " + "; ".join(bits) + ".")
    return out


# --------------------------------------------------------------------------
# Unidades gravables
# --------------------------------------------------------------------------

UNIDAD_FIELDS = ["nombreUnidadGravable", "nombreCorto", "operaSobreCasilla", "factor", "descuento"]


def unidades_rows(doc, version):
    header = doc.get("Cabecera") or {}
    actualizacion = header.get("Ultima Actualizacion", "")
    rows = []
    for grupo in doc["Contenido"]:
        for unidad in grupo["unidadesGravables"]:
            rows.append(
                {
                    "version": version,
                    "ultima_actualizacion": actualizacion,
                    "impuesto": grupo["impuesto"],
                    "codigo_unidad_gravable": fmt(unidad.get("codigoUnidadGravable")),
                    "nombre_unidad_gravable": unidad["nombreUnidadGravable"],
                    "nombre_corto": unidad["nombreCorto"],
                    "opera_sobre_casilla": fmt(unidad.get("operaSobreCasilla")),
                    "factor": fmt(unidad.get("factor")),
                    "descuento": fmt(unidad.get("descuento")),
                }
            )
    return rows, header


def unidades_drift(gh_doc, cd_doc):
    out = []
    gh_head, cd_head = gh_doc["Cabecera"], cd_doc["Cabecera"]
    if gh_head != cd_head:
        out.append(f"- Header: GH `{jdump(gh_head)}` vs CD `{jdump(cd_head)}`.")
    else:
        out.append(f"- Header identical on both channels: `{jdump(gh_head)}`.")

    def index(doc):
        idx = {}
        for grupo in doc["Contenido"]:
            for unidad in grupo["unidadesGravables"]:
                idx[(grupo["impuesto"], unidad["codigoUnidadGravable"])] = unidad
        return idx

    gh_idx, cd_idx = index(gh_doc), index(cd_doc)
    for key in sorted(set(gh_idx) | set(cd_idx), key=lambda k: (str(k[0]), k[1] is None, k[1] or 0)):
        impuesto, codigo = key
        g, c = gh_idx.get(key), cd_idx.get(key)
        if g and not c:
            out.append(
                f"- {impuesto} unidad {codigo}: GH-only `{jdump(g)}`."
            )
        elif c and not g:
            out.append(
                f"- {impuesto} unidad {codigo}: CD-only `{jdump(c)}`."
            )
        else:
            diffs = [f for f in UNIDAD_FIELDS if g.get(f) != c.get(f)]
            if diffs:
                out.append(
                    f"- {impuesto} unidad {codigo} differs — "
                    f"GH `{jdump(g)}` vs CD `{jdump(c)}` (fields: {', '.join(diffs)})."
                )
    return out


# --------------------------------------------------------------------------
# Mensajes
# --------------------------------------------------------------------------

FAMILY_RE = re.compile(r"^(FEL_[A-Z]+)")


def family_of(codigo):
    m = FAMILY_RE.match(codigo)
    return m.group(1) if m else "?"


def mensajes_rows(doc, version):
    header = doc.get("Cabecera") or {}
    actualizacion = header.get("Ultima Actualizacion", "")
    rows = []
    for entry in doc["Contenido"]:
        rows.append(
            {
                "version": version,
                "ultima_actualizacion": actualizacion,
                "codigo": entry["codigo"],
                "familia": family_of(entry["codigo"]),
                "validacion": entry["validacion"],
                "mensaje": entry["mensaje"],
            }
        )
    rows.sort(key=lambda r: r["codigo"])
    return rows, header


def mensajes_drift(gh_doc, cd_doc):
    out = []
    gh_head, cd_head = gh_doc["Cabecera"], cd_doc["Cabecera"]
    if gh_head != cd_head:
        out.append(f"- Header: GH `{jdump(gh_head)}` vs CD `{jdump(cd_head)}`.")
    else:
        out.append(f"- Header identical on both channels: `{jdump(gh_head)}`.")
    gh_idx = {e["codigo"]: e for e in gh_doc["Contenido"]}
    cd_idx = {e["codigo"]: e for e in cd_doc["Contenido"]}
    for codigo in sorted(set(gh_idx) | set(cd_idx)):
        g, c = gh_idx.get(codigo), cd_idx.get(codigo)
        if g and not c:
            out.append(f"- {codigo}: GH-only `{jdump(g)}`.")
        elif c and not g:
            out.append(f"- {codigo}: CD-only `{jdump(c)}`.")
        elif g != c:
            out.append(
                f"- {codigo} bodies differ between channels — GH validacion "
                f"`{g['validacion']}` / mensaje `{g['mensaje']}` vs CD validacion "
                f"`{c['validacion']}` / mensaje `{c['mensaje']}`."
            )
    return out


# --------------------------------------------------------------------------
# Writers
# --------------------------------------------------------------------------

def write_csv(path, fieldnames, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_text(path, text):
    path.write_text(text, encoding="utf-8")


def family_counts(rows):
    counts = {}
    for row in rows:
        counts[row["familia"]] = counts.get(row["familia"], 0) + 1
    return counts


def main():
    for directory in (GH_DIR, CD_DIR):
        if not directory.is_dir():
            fail(f"source directory missing: {directory}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    frases_gh_doc = load_json(GH_DIR / FRASES_GH)
    frases_cd_doc = load_json(CD_DIR / FRASES_CD)
    unidades_gh_doc = load_json(GH_DIR / UNIDADES)
    unidades_cd_doc = load_json(CD_DIR / UNIDADES)
    mensajes_gh_doc = load_json(GH_DIR / MENSAJES)
    mensajes_cd_doc = load_json(CD_DIR / MENSAJES)

    # ---- sidecars (working-authority channel: GitHub 961133c) ----
    frases, frases_header = frases_rows(frases_gh_doc, "0.6.0")
    unidades, unidades_header = unidades_rows(unidades_gh_doc, "0.1.4")
    mensajes, mensajes_header = mensajes_rows(mensajes_gh_doc, "0.3.0")

    write_csv(
        OUT_DIR / "CAT-FRS_frases.csv",
        ["version", "ultima_actualizacion", "tipo_frase", "nombre_tipo",
         "codigo_escenario", "escenario"]
        + [FRASE_FLAG_COLUMNS[f] for f in FRASE_FLAGS]
        + ["texto_a_colocar"],
        frases,
    )
    write_csv(
        OUT_DIR / "CAT-UGR_unidades-gravables.csv",
        ["version", "ultima_actualizacion", "impuesto", "codigo_unidad_gravable",
         "nombre_unidad_gravable", "nombre_corto", "opera_sobre_casilla",
         "factor", "descuento"],
        unidades,
    )
    write_csv(
        OUT_DIR / "CAT-MSG_mensajes.csv",
        ["version", "ultima_actualizacion", "codigo", "familia",
         "validacion", "mensaje"],
        mensajes,
    )

    # ---- drift record (both channels, verbatim) ----
    frases_lines = frases_drift(frases_gh_doc, frases_cd_doc)
    unidades_lines = unidades_drift(unidades_gh_doc, unidades_cd_doc)
    mensajes_lines = mensajes_drift(mensajes_gh_doc, mensajes_cd_doc)

    drift = []
    drift.append("# FEL catalogs — inter-channel drift record (_DRIFT.md)")
    drift.append("")
    drift.append(
        "Generated by `gt/scripts/build_gt_catalogs.py` (generation date "
        f"{GENERATION_DATE}) by diffing BOTH channels' JSON catalogs "
        "programmatically. Channel shorthand: **GH** = "
        "`gt/sources/29_FEL_XSD_cat_github_961133c/` (GitHub @ 961133c, "
        "working authority per the OQ3 ruling / master-index FEL authority "
        "preamble); **CD** = `gt/sources/30_FEL_XSD_cat_catdesa/` "
        "(cat.desa.sat.gob.gt)."
    )
    drift.append("")
    drift.append(
        "Policy (binding, GOQ-02 umbrella): every difference is recorded "
        "verbatim and never silently resolved. The sidecars carry the GH "
        "(working-authority) reading; this file is the only place the CD "
        "reading appears. Material unresolved cases carry their master-index "
        "GOQ id: GOQ-25 (PETROLEO 15/16), GOQ-26 (FEL_RCP108/109). The "
        "GitHub-MediosdePago exception (R2: model from cat.desa) concerns the "
        "XSD set, not these three JSON catalogs — recorded here for "
        "completeness because it is the only per-file authority override."
    )
    drift.append("")
    drift.append(
        "| Catalog | GH version / header date | CD version / header date | "
        "Differences detected | Unresolved (GOQ) |"
    )
    drift.append("|---|---|---|---|---|")
    n_frs = len(frases_lines) - 1  # minus the header line
    n_ugr = sum(1 for l in unidades_lines if l.startswith("- ") and "unidad" in l)
    n_msg = sum(1 for l in mensajes_lines if l.startswith("- FEL_"))
    drift.append(
        f"| CatalogoFrases | 0.6.0 / {frases_gh_doc['cabecera']['Ultima Actualizacion']} "
        f"| 0.1.2 / {frases_cd_doc['cabecera']['Ultima Actualizacion']} "
        f"| {n_frs} drift lines below (scope: 12 tipos/88 frases vs 5 tipos/25 frases) "
        "| GOQ-19 (which set each runtime loads) |"
    )
    drift.append(
        f"| catalogoUnidadesGravables | 0.1.4 / {unidades_gh_doc['Cabecera']['Ultima Actualizacion']} "
        f"| 0.1.4 / {unidades_cd_doc['Cabecera']['Ultima Actualizacion']} "
        f"| {n_ugr} unidad rows differ (PETROLEO 15/16) | GOQ-25 |"
    )
    drift.append(
        f"| catalogoMensajes | 0.3.0 / {mensajes_gh_doc['Cabecera']['Ultima Actualizacion']} "
        f"| 0.3.0 / {mensajes_cd_doc['Cabecera']['Ultima Actualizacion']} "
        f"| {n_msg} codes differ (FEL_RCP108/109 bodies swapped) | GOQ-26 |"
    )
    drift.append("")
    drift.append("## CatalogoFrases (GH 0.6.0 vs CD 0.1.2)")
    drift.append("")
    drift.extend(frases_lines)
    drift.append("")
    drift.append("## catalogoUnidadesGravables (GH 0.1.4 vs CD 0.1.4)")
    drift.append("")
    drift.extend(unidades_lines)
    drift.append("")
    drift.append("## catalogoMensajes (GH 0.3.0 vs CD 0.3.0)")
    drift.append("")
    drift.extend(mensajes_lines)
    drift.append("")
    drift.append("## Source fingerprints (md5, provenance)")
    drift.append("")
    drift.append("| File | Channel | Bytes | md5 |")
    drift.append("|---|---|---|---|")
    for label, channel, path in [
        (FRASES_GH, "GH", GH_DIR / FRASES_GH),
        (FRASES_CD, "CD", CD_DIR / FRASES_CD),
        (UNIDADES, "GH", GH_DIR / UNIDADES),
        (UNIDADES, "CD", CD_DIR / UNIDADES),
        (MENSAJES, "GH", GH_DIR / MENSAJES),
        (MENSAJES, "CD", CD_DIR / MENSAJES),
    ]:
        drift.append(
            f"| `{label}` | {channel} "
            f"| {path.stat().st_size} | `{md5_of(path)}` |"
        )
    drift.append("")
    write_text(OUT_DIR / "_DRIFT.md", "\n".join(drift))

    # ---- index ----
    fam_counts = family_counts(mensajes)
    tipo_counts = {}
    for row in frases:
        tipo_counts[row["tipo_frase"]] = tipo_counts.get(row["tipo_frase"], 0) + 1
    impuesto_counts = {}
    for row in unidades:
        impuesto_counts[row["impuesto"]] = impuesto_counts.get(row["impuesto"], 0) + 1

    index = []
    index.append("# FEL catalogs — machine-readable sidecars")
    index.append("")
    index.append(
        f"Generated by `gt/scripts/build_gt_catalogs.py` on {GENERATION_DATE} "
        f"(`{GENERATION_COMMAND}`). Deterministic and idempotent: re-running "
        "against the same sources reproduces every file byte-identically. "
        "Sources in `gt/sources/` are read-only and never modified. "
        "Inter-channel drift is recorded in [_DRIFT.md](_DRIFT.md) (never "
        "silently resolved — GOQ-02 umbrella)."
    )
    index.append("")
    index.append("## Sidecar map")
    index.append("")
    index.append(
        "| Catalog | File | Source file | Channel | Version | "
        "Ultima Actualizacion | Rows |"
    )
    index.append("|---|---|---|---|---|---|---|")
    index.append(
        f"| CAT-FRS frases | `CAT-FRS_frases.csv` | `gt/sources/29_FEL_XSD_cat_github_961133c/{FRASES_GH}` "
        f"| GitHub 961133c (working authority) | 0.6.0 | "
        f"{frases_header.get('Ultima Actualizacion', '')} | {len(frases)} |"
    )
    index.append(
        f"| CAT-UGR unidades gravables | `CAT-UGR_unidades-gravables.csv` | `gt/sources/29_FEL_XSD_cat_github_961133c/{UNIDADES}` "
        f"| GitHub 961133c (working authority) | 0.1.4 | "
        f"{unidades_header.get('Ultima Actualizacion', '')} | {len(unidades)} |"
    )
    index.append(
        f"| CAT-MSG mensajes | `CAT-MSG_mensajes.csv` | `gt/sources/29_FEL_XSD_cat_github_961133c/{MENSAJES}` "
        f"| GitHub 961133c (working authority) | 0.3.0 | "
        f"{mensajes_header.get('Ultima Actualizacion', '')} | {len(mensajes)} |"
    )
    index.append("")
    index.append(
        "The CD (cat.desa) copies of each source are read by the same script "
        "run for the drift diff only; they never feed the sidecars "
        "(Frases CD = 0.1.2, 5 tipos / 25 frases, header 12/07/2019 08:00:00)."
    )
    index.append("")
    index.append("## Columns")
    index.append("")
    index.append(
        "- Every CSV carries its source `version` string and the catalog "
        "header's `ultima_actualizacion` (\"Ultima Actualizacion\") as the "
        "first two columns — the dated-regime identity per D16/D-GT10."
    )
    index.append(
        "- `CAT-FRS_frases.csv`: `tipo_frase` + `codigo_escenario` = the "
        "(TipoFrase, CodigoEscenario) pair the DTE schema references; "
        "`nombre_tipo` is the tipo label; flag columns "
        "(`retener_isr`, `es_agente_retenedor`, `es_pequeno_contribuyente`, "
        "`es_regimen_electronico`, `es_agropecuario`, `incluye_iva`, "
        "`contiene_resolucion`, `contiene_fecha_resolucion`) carry "
        "`true`/`false` or empty = key absent from the source row; "
        "`texto_a_colocar` is the verbatim legend text to print."
    )
    index.append(
        "- `CAT-UGR_unidades-gravables.csv`: `impuesto` + "
        "`codigo_unidad_gravable` = the join key the schema's "
        "`Impuesto/CodigoUnidadGravable` references; `opera_sobre_casilla` "
        "drives the formula (`MontoGravable` = ad-valorem factor; "
        "`CantidadUnidadesGravables` = per-unit Q/USD factor); empty cells = "
        "source `null` (TASA MUNICIPAL single free-text unidad has null "
        "code/operaSobreCasilla/factor — preserved as-is, never invented)."
    )
    index.append(
        "- `CAT-MSG_mensajes.csv`: `codigo` = the runtime message code; "
        "`familia` derived from the code prefix (FEL_RCP, FEL_AUT, FEL_ASO, "
        "FEL_GEN, FEL_INF, FEL_ANU, FEL_SEC); `validacion` = the validation "
        "rule text; `mensaje` = the message returned to the emitter."
    )
    index.append("")
    index.append("## Composition (generation-time facts)")
    index.append("")
    index.append(
        f"- Frases 0.6.0: {len(tipo_counts)} tipos / {len(frases)} frases — "
        + ", ".join(f"tipo {t}: {c}" for t, c in sorted(tipo_counts.items())) + "."
    )
    index.append(
        f"- Unidades 0.1.4: {len(impuesto_counts)} impuestos / "
        f"{len(unidades)} unidades — "
        + ", ".join(f"{i}: {c}" for i, c in sorted(impuesto_counts.items())) + "."
    )
    index.append(
        f"- Mensajes 0.3.0: {len(mensajes)} codes / {len(fam_counts)} "
        "families — "
        + ", ".join(f"{f}: {c}" for f, c in sorted(fam_counts.items())) + "."
    )
    index.append("")
    index.append("## Corrections log")
    index.append("")
    index.append(
        "Any deviation between a sidecar and its source applied at build "
        "time is logged here (none are applied by the script itself — it is "
        "a verbatim flattening; governance FR: a sidecar contains no "
        "unlogged deviation). Record any manual regeneration decisions here:"
    )
    index.append("")
    index.append(
        f"- {GENERATION_DATE} initial generation: no corrections; verbatim "
        "flatten of the GH JSON (channel authority per OQ3 ruling; the only "
        "per-file override, MediosdePago → cat.desa per R2, concerns the XSD "
        "set, not these catalogs)."
    )
    index.append("")
    write_text(OUT_DIR / "_INDEX.md", "\n".join(index))

    print(
        f"wrote {len(frases)} frases, {len(unidades)} unidades, "
        f"{len(mensajes)} mensajes -> {OUT_DIR}"
    )
    print(
        f"drift: {n_frs} frases lines, {n_ugr} unidad diffs, "
        f"{n_msg} mensaje diffs -> _DRIFT.md"
    )


if __name__ == "__main__":
    main()
