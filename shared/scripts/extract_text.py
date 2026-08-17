#!/usr/bin/env python3
"""Extract text from source documents for requirements evidence passes.

Usage:
    extract_text.py <country> [file ...]

Reads from <country>/sources/, writes to <country>/.extractions/ (scratch,
git-ignored). PDFs get page markers (=== PAGE n ===) so citations can carry
page numbers. XLSX workbooks are dumped sheet-by-sheet as CSV-ish text with
sheet markers. JSON/MD files are copied unchanged.

Options:
    --check    only report extraction quality (pages, chars/page), write nothing

Exit code 1 if any requested file fails. Flags scanned/garbled PDFs with a
warning: those need OCR before evidence work — do not read through them.
"""

import json
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WARN_CHARS = {"\ufffd"}  # replacement chars signal bad decode


def out_name(src: Path) -> Path:
    return src.with_suffix(src.suffix + ".txt" if src.suffix != ".txt" else ".txt")


def extract_pdf(path: Path):
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as e:  # noqa: BLE001 - record, don't die mid-doc
            text = ""
            print(f"  WARN {path.name} p.{i}: extraction error {e}", file=sys.stderr)
        pages.append(f"=== PAGE {i} ===\n{text}")
    return pages, reader


def pdf_quality(pages) -> str:
    """Heuristic: little or no text => likely scanned; many replacement chars => garbled."""
    n = len(pages)
    if n == 0:
        return "EMPTY"
    chars = sum(len(p) for p in pages) / n
    junk = sum(p.count(c) for p in pages for c in WARN_CHARS)
    if chars < 80:
        return f"SCANNED? ({chars:.0f} chars/page — needs OCR)"
    if junk > 20:
        return f"GARBLED? ({junk} replacement chars)"
    return f"ok ({chars:.0f} chars/page)"


def extract_xlsx(path: Path):
    import openpyxl

    wb = openpyxl.load_workbook(str(path), data_only=True, read_only=True)
    blocks = []
    for ws in wb.worksheets:
        lines = [f"=== SHEET {ws.title} ==="]
        for row in ws.iter_rows(values_only=True):
            cells = ["" if c is None else str(c) for c in row]
            if any(c.strip() for c in cells):
                lines.append(";".join(cells))
        blocks.append("\n".join(lines))
    return blocks


def main() -> int:
    args = sys.argv[1:]
    check_only = "--check" in args
    args = [a for a in args if a != "--check"]
    if not args:
        print(__doc__)
        return 2
    country, files = args[0], args[1:]
    src_dir = REPO / country / "sources"
    out_dir = REPO / country / ".extractions"
    if not src_dir.is_dir():
        print(f"error: {src_dir} not found", file=sys.stderr)
        return 2

    targets = [src_dir / f for f in files] or sorted(src_dir.iterdir())
    failures = 0
    out_dir.mkdir(exist_ok=True)

    for src in targets:
        if src.name == "README.md" or src.is_dir():
            continue
        try:
            if src.suffix.lower() == ".pdf":
                pages, _ = extract_pdf(src)
                quality = pdf_quality(pages)
                print(f"{src.name}: {len(pages)} pages, {quality}")
                if quality.startswith(("SCANNED", "GARBLED", "EMPTY")):
                    failures += 1
                    continue
                if not check_only:
                    out_dir.joinpath(src.name + ".txt").write_text(
                        "\n\n".join(pages), encoding="utf-8"
                    )
            elif src.suffix.lower() == ".xlsx":
                if not check_only:
                    blocks = extract_xlsx(src)
                    out_dir.joinpath(src.name + ".txt").write_text(
                        "\n\n".join(blocks), encoding="utf-8"
                    )
                print(f"{src.name}: xlsx dumped")
            elif src.suffix.lower() in {".json", ".md", ".txt"}:
                if not check_only:
                    out_dir.joinpath(src.name).write_text(
                        unicodedata.normalize("NFC", src.read_text(encoding="utf-8")),
                        encoding="utf-8",
                    )
                print(f"{src.name}: copied unchanged")
            else:
                print(f"{src.name}: SKIP (unsupported {src.suffix})")
        except Exception as e:  # noqa: BLE001
            failures += 1
            print(f"{src.name}: FAIL {e}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
