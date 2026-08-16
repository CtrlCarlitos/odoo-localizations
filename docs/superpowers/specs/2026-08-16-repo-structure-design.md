# Odoo Localizations — Repository Structure Design

**Date:** 2026-08-16
**Status:** Approved (approach A) — pending spec review

## Purpose

This repository is a requirements-extraction workspace for building Odoo
localizations for El Salvador (SV), Guatemala (GT), and Honduras (HN). It holds
source documents (laws, decrees, technical specifications, catalogs) from each
country's tax authority, scripts to parse them, and structured markdown
requirements extracted from them.

It is **not** a code repository and not an Odoo module. Extracted requirements
will be consumed in other repositories to build localization modules for Odoo
17.0, 18.0, 19.0, and the upcoming 20.0. Takumi — the in-house AI agent
platform for building, diagnosing, and migrating Odoo modules — will use these
requirements as its input contract to build the localizations as a proof of
concept.

## Scope

| Country | Localization requirements | Electronic invoicing |
|---------|--------------------------|----------------------|
| El Salvador (sv) | Yes | Yes |
| Guatemala (gt) | Yes | Yes |
| Honduras (hn) | Yes | No |

## Directory Structure

```
odoo-localizations/
├── README.md                      # What this repo is, how it's organized
├── shared/
│   ├── scripts/                   # Reusable parsing/extraction scripts
│   │   └── README.md              # Usage per script (PDF, HTML, Excel, XML/JSON)
│   └── docs/                      # Cross-country documentation
│       ├── requirements-template.md   # The Takumi input contract (see below)
│       └── odoo-localization-guide.md # How to build an Odoo localization package
├── sv/
│   ├── README.md                  # El Salvador scope, sources, status, contacts
│   ├── sources/                   # Original government documents (PDF, HTML, XLSX…)
│   │   └── README.md              # Source registry: provenance, date, version
│   ├── scripts/                   # SV-specific parsing/extraction scripts
│   │   └── README.md
│   └── requirements/              # Extracted requirements, per topic
│       ├── README.md              # Topic index and status per topic
│       ├── e-invoicing/
│       ├── taxation/
│       ├── chart-of-accounts/
│       ├── payroll/
│       └── fiscal-reporting/
├── gt/                            # Same layout as sv (includes e-invoicing/)
└── hn/                            # Same layout as sv (no e-invoicing/)
```

Country directories use ISO 3166-1 alpha-2 codes, lowercase (`sv`, `gt`, `hn`).
Each country is self-contained: its sources, scripts, requirements, and README
can be understood without reading the other countries.

## Topic Taxonomy

Requirements within each country are organized by functional topic, mirroring
how Odoo localization modules are built:

- `e-invoicing/` — electronic invoicing mandates, document types, signature/
  stamping, transmission protocols, cancellation, contingency flows
- `taxation/` — VAT/ISR rates, regimes, retention rules, tax reporting
- `chart-of-accounts/` — statutory account charts and mappings
- `payroll/` — payroll taxes, social security, benefits
- `fiscal-reporting/` — periodic filings, declaration formats, books/ledgers

The taxonomy is a starter set. Countries add topics only when a requirement
does not fit (e.g., `customs/`, `municipal-taxes/`), and each country's
`requirements/README.md` indexes the topics that exist there.

## Requirements Document Contract (Takumi Input)

Every requirements file follows the template in
`shared/docs/requirements-template.md`. Fixed sections:

1. **Purpose** — what this requirement covers, in one paragraph
2. **Legal Basis** — citations to source documents (Spanish original + English
   translation), each linking to the file in `sources/`
3. **Functional Requirements** — numbered, testable statements (FR-001…)
4. **Data Model** — entities, fields, catalogs, and code lists
5. **Odoo Mapping** — how requirements map onto Odoo models/fields, with
   version notes where 17/18/19/20 differ
6. **Acceptance Criteria** — Given/When/Then criteria Takumi must satisfy
7. **Open Questions** — unresolved ambiguities, blocking status, owner

Requirements are written in **English**. Spanish legal and technical terms are
kept inline with English translations (e.g., "factura electrónica (electronic
invoice)"). Machine-readable artifacts (extracted catalogs as CSV/JSON) live
next to the markdown that describes them.

## Scripts

- `shared/scripts/` — format-generic parsers used by all countries
  (PDF→text, HTML→text, Excel→CSV, XML/JSON normalization). Source documents
  arrive in all four formats.
- `<country>/scripts/` — country-specific extraction logic that builds on
  shared scripts (e.g., parsing an SV catalog into a normalized CSV).
- Scripts are helpers, not products: no packaging, no CI pipeline. A short
  usage note per script in each scripts README is the documentation bar.

## Git

- Branch: `main` (only branch initially)
- Remote: `git@github.com:CtrlCarlitos/odoo-localizations.git` (origin),
  created manually on GitHub — `gh` CLI is not available in this environment
- Commit message style: short imperative summary lines
- Source PDFs are committed directly; if the repo grows unwieldy, Git LFS can
  be adopted later (deferred decision, documented here)

## Root README Content

- Project description (requirements-extraction workspace, not an Odoo module)
- Country table (scope matrix above)
- Directory layout overview
- Workflow: sources → scripts → requirements → consumed by Takumi and
  downstream module repositories (Odoo 17–20)
- Link to `shared/docs/` guides and the requirements template

## Country README Content

- Country scope (topics covered, e-invoicing or not)
- Tax authority name and key portals (MH El Salvador, SAT Guatemala,
  SAR Honduras)
- Source document registry summary (count by topic, latest additions)
- Requirements status per topic (not started / in progress / under review /
  complete)
- Takumi proof-of-concept status

## Out of Scope

- Any Odoo module code, manifests, or installable artifacts
- CI/CD pipelines
- Multi-language output (English only, Spanish terms inline)
- Cross-country synthesis documents (may be added under `shared/docs/` later
  if a real need emerges)

## Decisions Log

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Structure | Country-first, topics nested | Countries are independent deliverables; matches existing dirs |
| Requirements organization | Per functional topic | Mirrors Odoo module decomposition; best for Takumi |
| Output language | English, Spanish terms inline | Odoo dev convention; sources stay citable |
| Requirements format | Fixed-section template | Machine-consumable consistency across countries |
| Binary sources in git | Plain git, LFS deferred | Simple start; reversible later |
