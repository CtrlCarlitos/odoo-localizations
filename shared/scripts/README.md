# Shared Scripts

Reusable parsing and extraction helpers shared by all countries. Country-specific
logic belongs in `<cc>/scripts/`, not here.

## Conventions

- Python 3, standard library first. Add third-party dependencies only when
  clearly worth it (e.g. `pypdf`, `beautifulsoup4`, `openpyxl`) and note them
  in the script's docstring.
- Scripts read from `<cc>/sources/` and write extracted text to stdout, or
  machine-readable sidecars (CSV/JSON) next to the requirements file that uses
  them. Scripts never modify files in `sources/`.
- No packaging, no CI. A script is "done" when its usage note in the table
  below is filled in.

## Scripts

| Script | Formats | Usage |
|--------|---------|-------|
| `extract_text.py` | PDF, XLSX, JSON/MD/TXT | `python extract_text.py <cc> [file ...]` — extracts to `<cc>/.extractions/` with `=== PAGE n ===` markers; `--check` reports quality only. Flags scanned/garbled PDFs (exit 1). Needs `pypdf` + `openpyxl` (venv: `~/.venvs/localizations`). `.xls`/`.docx` not supported yet. |
