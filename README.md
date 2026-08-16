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
