# Odoo Localizations — Requirements Workspace

This repository is the requirements-extraction workspace for the Odoo
localizations of **El Salvador (SV)**, **Guatemala (GT)**, and **Honduras (HN)**.
It collects the official source documents published by each country's tax
authority, the scripts that parse them, and the structured requirements
extracted from them.

## What this repository is — and is not

- A document collection and requirements workspace.
- Home to small helper scripts that parse source documents (PDF, HTML,
  Word/Excel, XML/JSON) into text and machine-readable catalogs.
- **Not** an Odoo module, addon, or installable code. Nothing here ships to
  an Odoo database.

Once requirements are gathered and validated here, they are consumed by
**Takumi** (our in-house AI agent platform for building and maintaining Odoo
modules) as a proof of concept, and used to build the actual localization
modules in separate repositories, targeting Odoo **17.0, 18.0, 19.0, and the
upcoming 20.0**.

## Scope

| Country | Localization | Electronic invoicing | Directory |
|---------|--------------|----------------------|-----------|
| El Salvador | Yes | Yes | [`sv/`](sv/) |
| Guatemala | Yes | Yes | [`gt/`](gt/) |
| Honduras | Yes | No | [`hn/`](hn/) |

## How it is organized

```
odoo-localizations/
├── shared/
│   ├── scripts/     # Reusable parsing scripts shared by all countries
│   └── docs/        # Requirements template + Odoo localization guides
├── sv/              # El Salvador
├── gt/              # Guatemala
└── hn/              # Honduras
```

Each country directory follows the same layout:

```
<cc>/
├── README.md        # Scope, tax authority, source and requirements status
├── sources/         # Original government documents, unmodified
├── scripts/         # Country-specific parsing/extraction scripts
└── requirements/    # Extracted requirements, one directory per topic
```

## Workflow

1. **Collect** — original documents land in `<cc>/sources/` and are recorded
   in that directory's registry.
2. **Parse** — shared (`shared/scripts/`) and country (`<cc>/scripts/`)
   scripts convert documents into text and normalized data.
3. **Extract** — requirements are written following
   [`shared/docs/requirements-template.md`](shared/docs/requirements-template.md),
   in English with Spanish legal terms preserved inline.
4. **Build** — Takumi and downstream module repositories consume the
   requirements to build the localization modules for Odoo 17–20.

## Documentation

- [Requirements template](shared/docs/requirements-template.md) — the fixed
  format every requirements file follows (the Takumi input contract)
- [Building an Odoo localization package](shared/docs/odoo-localization-guide.md)

## Countries

- [El Salvador (sv)](sv/README.md) — Ministerio de Hacienda (MH)
- [Guatemala (gt)](gt/README.md) — Superintendencia de Administración Tributaria (SAT)
- [Honduras (hn)](hn/README.md) — Servicio de Administración de Rentas (SAR)

## Development environment

The helper scripts in [shared/scripts/](shared/scripts/) need a Python 3.10+
environment with a handful of packages, plus system libraries for PDF OCR.

### System packages (sudo)

```bash
sudo apt install tesseract-ocr tesseract-ocr-spa ghostscript qpdf unpaper -y
```

`tesseract-ocr-spa` (Spanish language data) is required — all source
documents are in Spanish.

### Python environment

```bash
python3 -m venv ~/.venvs/localizations
~/.venvs/localizations/bin/pip install pypdf openpyxl ocrmypdf xlrd python-docx
```

Or with `uv`:

```bash
uv venv ~/.venvs/localizations
uv pip install --python ~/.venvs/localizations/bin/python pypdf openpyxl ocrmypdf xlrd python-docx
```

| Package | Used for |
|---------|----------|
| `pypdf` | PDF text extraction with page markers |
| `openpyxl` | `.xlsx` dumps (MH catalogs) |
| `ocrmypdf` | OCR fallback for scanned PDFs (`extract_text.py --ocr`; wraps tesseract) |
| `xlrd` | legacy `.xls` (F-07/F-14 templates) |
| `python-docx` | `.docx` (comunicados) |

Run scripts with the venv interpreter, e.g.:

```bash
~/.venvs/localizations/bin/python shared/scripts/extract_text.py sv --check
```
