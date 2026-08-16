# Repository Scaffolding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the odoo-localizations requirements workspace: root README, shared docs/scripts, and per-country (sv/gt/hn) directory structures, wired to the CtrlCarlitos GitHub remote.

**Architecture:** Country-first layout (ISO 3166-1 alpha-2 codes), topics nested inside each country. `shared/` holds the reusable requirements template (the Takumi input contract), localization guide, and format-generic parsers. Pure documentation/scaffolding — no Odoo code, no CI, no packaging.

**Tech Stack:** Git, Markdown. (Python 3 scripts may be added later; none yet.)

**Spec:** `docs/superpowers/specs/2026-08-16-repo-structure-design.md`

## Global Constraints

- Countries: `sv` (El Salvador), `gt` (Guatemala), `hn` (Honduras) — lowercase ISO codes.
- `sv` and `gt` include the `e-invoicing` topic; `hn` does NOT.
- Topic taxonomy: `e-invoicing`, `taxation`, `chart-of-accounts`, `payroll`, `fiscal-reporting`.
- Requirements language: English, Spanish legal terms inline with translations.
- No Odoo module code, manifests, or installable artifacts anywhere.
- All commits use `git commit --no-gpg-sign` (SSH signing key `id_CtrlCarlitos` is missing on this machine; do not modify global git config).
- Remote: `git@github.com:CtrlCarlitos/odoo-localizations.git` as `origin`. Push is deferred until the SSH key exists — do not attempt `git push`.
- Empty topic directories are kept in git via `.gitkeep` files.

---

### Task 1: Root scaffolding — .gitignore and README.md

**Files:**
- Create: `.gitignore`
- Create: `README.md`

**Interfaces:**
- Consumes: nothing.
- Produces: root `README.md` that links to `sv/README.md`, `gt/README.md`, `hn/README.md`, `shared/docs/requirements-template.md`, `shared/docs/odoo-localization-guide.md` (all created in later tasks — links will resolve once Tasks 2–6 land).

- [ ] **Step 1: Create `.gitignore`**

```gitignore
# OS
.DS_Store
Thumbs.db

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Scratch outputs
*.tmp
```

- [ ] **Step 2: Create root `README.md`**

````markdown
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
````

- [ ] **Step 3: Verify files exist and are non-empty**

Run: `test -s .gitignore && test -s README.md && echo OK`
Expected: `OK`

- [ ] **Step 4: Commit**

```bash
git add .gitignore README.md
git commit --no-gpg-sign -m "Add root README and gitignore"
```

---

### Task 2: shared/docs — requirements template and localization guide

**Files:**
- Create: `shared/docs/requirements-template.md`
- Create: `shared/docs/odoo-localization-guide.md`

**Interfaces:**
- Consumes: nothing.
- Produces: `shared/docs/requirements-template.md` — the fixed 7-section contract (Purpose, Legal Basis, Functional Requirements, Data Model, Odoo Mapping, Acceptance Criteria, Open Questions) referenced by every country's `requirements/README.md` in Tasks 4–6, and by the root README from Task 1. Produces: `shared/docs/odoo-localization-guide.md` — the localization-building reference.

- [ ] **Step 1: Create `shared/docs/requirements-template.md`**

````markdown
# Requirements Template (Takumi Input Contract)

Every requirements file in `<cc>/requirements/<topic>/` follows this template
exactly. Copy it, rename it to match its topic scope, and fill in every
section. If a section genuinely does not apply, write "Not applicable" with
one line explaining why — never delete a section.

Requirements are written in **English**. Spanish legal and technical terms
are kept inline with an English translation on first use, e.g.
*factura electrónica* (electronic invoice).

---

# [Country] — [Topic] — [Specific scope]

| Field   | Value |
|---------|-------|
| Country | sv / gt / hn |
| Topic   | e-invoicing / taxation / chart-of-accounts / payroll / fiscal-reporting |
| Status  | draft / in-review / approved |
| Authors | name(s) |
| Updated | YYYY-MM-DD |

## 1. Purpose

One paragraph: what this requirement covers and what it does not.

## 2. Legal Basis

Every requirement must be traceable to an official source document in
`<cc>/sources/`.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | *Ley ...* | Law ... | `sv/sources/....pdf` | Art. 12 |

## 3. Functional Requirements

Numbered, testable statements. One requirement per line — no compound
requirements.

- **FR-001:** The system shall ...

## 4. Data Model

Entities, fields, catalogs, and code lists. Machine-readable versions
(CSV/JSON) live next to this markdown file.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| | | | | |

## 5. Odoo Mapping

How each functional requirement maps onto Odoo models and fields. Note
version-specific behavior for Odoo 17/18/19/20 wherever they differ.

| FR | Odoo model | Field(s) | Notes / version differences |
|----|------------|----------|------------------------------|
| | | | |

## 6. Acceptance Criteria

Given/When/Then criteria. These are what Takumi must satisfy; each must be
objectively verifiable.

- **AC-001:** Given ..., when ..., then ...

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | | yes / no | | open / resolved |
````

- [ ] **Step 2: Create `shared/docs/odoo-localization-guide.md`**

````markdown
# Building an Odoo Localization Package

Shared reference for turning the requirements in this repository into Odoo
localization modules. Target versions: **17.0, 18.0, 19.0, 20.0**.

## Package anatomy

A complete country localization is typically split into modules:

| Module | Purpose |
|--------|---------|
| `l10n_<cc>` | Fiscal core: chart of accounts, taxes, fiscal positions, tax report |
| `l10n_<cc>_edi` | Electronic invoicing: document generation, signing, transmission |
| `l10n_<cc>_reports` | Periodic fiscal filings and declaration reports |
| `l10n_<cc>_hr` (optional) | Payroll: salary rules, social security contributions |

`<cc>` is the lowercase ISO 3166-1 alpha-2 code (`sv`, `gt`, `hn`), matching
the country directories in this repository.

## Fiscal core (`l10n_<cc>`)

- **Chart of accounts template** — `account.chart.template` records loaded
  from data files; selected by companies during onboarding.
- **Taxes** — tax templates with tax groups, price-inclusion flags, and tax
  grids linked to the tax report.
- **Fiscal positions** — automatic mappings (e.g. exemptions, exports).
- **Tax report** — `account.tax.report` lines and expressions so the
  Tax Report and declarations work out of the box.
- **Country data** — states, address format, and paper formats as needed.

## Electronic invoicing (`l10n_<cc>_edi`)

Built on Odoo's EDI framework (`account.edi.format`):

- Subclass `account.edi.format` to generate the legal document (XML/JSON)
  and attach it to the invoice.
- Implement transmission (HTTP or file-based flows), polling for
  authorization status, error handling, and cancellation/credit-note flows.
- Credentials and environment settings (test/production) belong on the
  company, ideally via a configuration wizard.
- Requirements come from `requirements/e-invoicing/` in the country folder;
  every acceptance criterion there must map to a test in the module.

## Version targeting (17 → 20)

- Develop against the newest stable version first, then port. Most breakage
  concentrates in: chart template APIs, EDI framework signatures, view
  inheritance, and QWeb templates.
- Track upstream `odoo/odoo` for 20.0 API changes; keep the requirements'
  "Odoo Mapping / version differences" column updated as changes are found.
- Prefer one branch per Odoo version (mirroring Odoo's own branching) over
  version-conditional code.

## Testing

- Every acceptance criterion in a requirements file must map to at least one
  Odoo test (`TransactionCase`) in the implementing module.
- Run: `odoo-bin -d test -i l10n_<cc>_edi --test-enable --stop-after-init`
- Include heterogeneous demo data (products with and without taxes, domestic
  and foreign customers) since fiscal behavior differs by partner.

## From requirements to modules

1. Start from `requirements/chart-of-accounts/` — the fiscal core depends on it.
2. Then `taxation/` (tax templates and report), then `fiscal-reporting/`.
3. `e-invoicing/` builds on the fiscal core; `payroll/` is independent.
4. Record any discovered Odoo constraints back into the requirement file's
   "Open Questions" section — this repository is the single source of truth.
````

- [ ] **Step 3: Verify both files exist and contain the fixed section names**

Run: `test -s shared/docs/requirements-template.md && test -s shared/docs/odoo-localization-guide.md && grep -c "^## " shared/docs/requirements-template.md`
Expected: `7`

- [ ] **Step 4: Commit**

```bash
git add shared/docs
git commit --no-gpg-sign -m "Add shared docs: requirements template and localization guide"
```

---

### Task 3: shared/scripts scaffold

**Files:**
- Create: `shared/scripts/README.md`

**Interfaces:**
- Consumes: nothing.
- Produces: `shared/scripts/README.md` — conventions (Python 3, stdlib-first, sources are read-only, outputs go next to requirements) that country `scripts/README.md` files in Tasks 4–6 link to.

- [ ] **Step 1: Create `shared/scripts/README.md`**

```markdown
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
| (none yet) | | |
```

- [ ] **Step 2: Verify file exists**

Run: `test -s shared/scripts/README.md && echo OK`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add shared/scripts
git commit --no-gpg-sign -m "Add shared scripts scaffold"
```

---

### Task 4: El Salvador (sv) scaffold

**Files:**
- Create: `sv/README.md`
- Create: `sv/sources/README.md`
- Create: `sv/scripts/README.md`
- Create: `sv/requirements/README.md`
- Create: `sv/requirements/{e-invoicing,taxation,chart-of-accounts,payroll,fiscal-reporting}/.gitkeep`

**Interfaces:**
- Consumes: `shared/docs/requirements-template.md` (linked from `sv/requirements/README.md`) and `shared/scripts/README.md` conventions (linked from `sv/scripts/README.md`) — both exist after Tasks 2–3.
- Produces: `sv/README.md` linked from the root README; five topic directories under `sv/requirements/`.

- [ ] **Step 1: Create `sv/README.md`**

```markdown
# El Salvador (SV)

Odoo localization requirements for El Salvador, including electronic
invoicing (facturación electrónica).

- **Tax authority:** Ministerio de Hacienda (MH) — https://www.mh.gob.sv
- **Takumi proof of concept:** not started.

## Requirements status

| Topic | Directory | Status |
|-------|-----------|--------|
| Electronic invoicing | [requirements/e-invoicing/](requirements/e-invoicing/) | Not started |
| Taxation | [requirements/taxation/](requirements/taxation/) | Not started |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | Not started |
| Payroll | [requirements/payroll/](requirements/payroll/) | Not started |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | Not started |

Status values: Not started, In progress, In review, Complete.

## Sources

No sources registered yet — see [sources/](sources/).
```

- [ ] **Step 2: Create `sv/sources/README.md`**

```markdown
# Sources — El Salvador

Original, unmodified documents from the Salvadoran tax authority (Ministerio
de Hacienda) and related official bodies. Never edit files here; parsers must
treat them as read-only.

## Registry

| File | Topic | Title | Issued | Retrieved | Provenance (URL) |
|------|-------|-------|--------|-----------|------------------|
| (none yet) | | | | | |

When adding a document: keep its original filename (prefix with `YYYY-MM-DD_`
only if it would collide), place it in this directory, and add a registry row.
```

- [ ] **Step 3: Create `sv/scripts/README.md`**

```markdown
# Scripts — El Salvador

Country-specific parsing and extraction for Salvadoran source documents.
Format-generic helpers live in [shared/scripts](../../shared/scripts/) —
reuse them instead of duplicating here.

| Script | Purpose | Usage |
|--------|---------|-------|
| (none yet) | | |
```

- [ ] **Step 4: Create `sv/requirements/README.md`**

```markdown
# Requirements — El Salvador

Extracted requirements, one directory per topic. Every file follows the
[requirements template](../../shared/docs/requirements-template.md).
Language: English, Spanish legal terms inline with translations.

| Topic | Status | Files |
|-------|--------|-------|
| [e-invoicing](e-invoicing/) | Not started | — |
| [taxation](taxation/) | Not started | — |
| [chart-of-accounts](chart-of-accounts/) | Not started | — |
| [payroll](payroll/) | Not started | — |
| [fiscal-reporting](fiscal-reporting/) | Not started | — |

Status values: Not started, In progress, In review, Complete.
```

- [ ] **Step 5: Create the five topic directories**

```bash
mkdir -p sv/requirements/e-invoicing sv/requirements/taxation \
  sv/requirements/chart-of-accounts sv/requirements/payroll \
  sv/requirements/fiscal-reporting
touch sv/requirements/e-invoicing/.gitkeep sv/requirements/taxation/.gitkeep \
  sv/requirements/chart-of-accounts/.gitkeep sv/requirements/payroll/.gitkeep \
  sv/requirements/fiscal-reporting/.gitkeep
```

- [ ] **Step 6: Verify structure**

Run: `find sv -type f | sort`
Expected:
```
sv/README.md
sv/requirements/README.md
sv/requirements/chart-of-accounts/.gitkeep
sv/requirements/e-invoicing/.gitkeep
sv/requirements/fiscal-reporting/.gitkeep
sv/requirements/payroll/.gitkeep
sv/requirements/taxation/.gitkeep
sv/scripts/README.md
sv/sources/README.md
```

- [ ] **Step 7: Commit**

```bash
git add sv
git commit --no-gpg-sign -m "Add El Salvador directory scaffold"
```

---

### Task 5: Guatemala (gt) scaffold

**Files:**
- Create: `gt/README.md`
- Create: `gt/sources/README.md`
- Create: `gt/scripts/README.md`
- Create: `gt/requirements/README.md`
- Create: `gt/requirements/{e-invoicing,taxation,chart-of-accounts,payroll,fiscal-reporting}/.gitkeep`

**Interfaces:**
- Consumes: `shared/docs/requirements-template.md` (linked from `gt/requirements/README.md`) and `shared/scripts/README.md` conventions (linked from `gt/scripts/README.md`).
- Produces: `gt/README.md` linked from the root README; five topic directories under `gt/requirements/`.

- [ ] **Step 1: Create `gt/README.md`**

```markdown
# Guatemala (GT)

Odoo localization requirements for Guatemala, including electronic invoicing
(facturación electrónica, régimen FEL).

- **Tax authority:** Superintendencia de Administración Tributaria (SAT) — https://www.sat.gob.gt
- **Takumi proof of concept:** not started.

## Requirements status

| Topic | Directory | Status |
|-------|-----------|--------|
| Electronic invoicing | [requirements/e-invoicing/](requirements/e-invoicing/) | Not started |
| Taxation | [requirements/taxation/](requirements/taxation/) | Not started |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | Not started |
| Payroll | [requirements/payroll/](requirements/payroll/) | Not started |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | Not started |

Status values: Not started, In progress, In review, Complete.

## Sources

No sources registered yet — see [sources/](sources/).
```

- [ ] **Step 2: Create `gt/sources/README.md`**

```markdown
# Sources — Guatemala

Original, unmodified documents from the Guatemalan tax authority (SAT) and
related official bodies. Never edit files here; parsers must treat them as
read-only.

## Registry

| File | Topic | Title | Issued | Retrieved | Provenance (URL) |
|------|-------|-------|--------|-----------|------------------|
| (none yet) | | | | | |

When adding a document: keep its original filename (prefix with `YYYY-MM-DD_`
only if it would collide), place it in this directory, and add a registry row.
```

- [ ] **Step 3: Create `gt/scripts/README.md`**

```markdown
# Scripts — Guatemala

Country-specific parsing and extraction for Guatemalan source documents.
Format-generic helpers live in [shared/scripts](../../shared/scripts/) —
reuse them instead of duplicating here.

| Script | Purpose | Usage |
|--------|---------|-------|
| (none yet) | | |
```

- [ ] **Step 4: Create `gt/requirements/README.md`**

```markdown
# Requirements — Guatemala

Extracted requirements, one directory per topic. Every file follows the
[requirements template](../../shared/docs/requirements-template.md).
Language: English, Spanish legal terms inline with translations.

| Topic | Status | Files |
|-------|--------|-------|
| [e-invoicing](e-invoicing/) | Not started | — |
| [taxation](taxation/) | Not started | — |
| [chart-of-accounts](chart-of-accounts/) | Not started | — |
| [payroll](payroll/) | Not started | — |
| [fiscal-reporting](fiscal-reporting/) | Not started | — |

Status values: Not started, In progress, In review, Complete.
```

- [ ] **Step 5: Create the five topic directories**

```bash
mkdir -p gt/requirements/e-invoicing gt/requirements/taxation \
  gt/requirements/chart-of-accounts gt/requirements/payroll \
  gt/requirements/fiscal-reporting
touch gt/requirements/e-invoicing/.gitkeep gt/requirements/taxation/.gitkeep \
  gt/requirements/chart-of-accounts/.gitkeep gt/requirements/payroll/.gitkeep \
  gt/requirements/fiscal-reporting/.gitkeep
```

- [ ] **Step 6: Verify structure**

Run: `find gt -type f | sort`
Expected:
```
gt/README.md
gt/requirements/README.md
gt/requirements/chart-of-accounts/.gitkeep
gt/requirements/e-invoicing/.gitkeep
gt/requirements/fiscal-reporting/.gitkeep
gt/requirements/payroll/.gitkeep
gt/requirements/taxation/.gitkeep
gt/scripts/README.md
gt/sources/README.md
```

- [ ] **Step 7: Commit**

```bash
git add gt
git commit --no-gpg-sign -m "Add Guatemala directory scaffold"
```

---

### Task 6: Honduras (hn) scaffold — no e-invoicing

**Files:**
- Create: `hn/README.md`
- Create: `hn/sources/README.md`
- Create: `hn/scripts/README.md`
- Create: `hn/requirements/README.md`
- Create: `hn/requirements/{taxation,chart-of-accounts,payroll,fiscal-reporting}/.gitkeep`

**Interfaces:**
- Consumes: `shared/docs/requirements-template.md` (linked from `hn/requirements/README.md`) and `shared/scripts/README.md` conventions (linked from `hn/scripts/README.md`).
- Produces: `hn/README.md` linked from the root README; four topic directories under `hn/requirements/` (NO `e-invoicing`).

- [ ] **Step 1: Create `hn/README.md`**

```markdown
# Honduras (HN)

Odoo localization requirements for Honduras. Electronic invoicing is out of
scope for Honduras.

- **Tax authority:** Servicio de Administración de Rentas (SAR) — https://www.sar.gob.hn
- **Takumi proof of concept:** not started.

## Requirements status

| Topic | Directory | Status |
|-------|-----------|--------|
| Taxation | [requirements/taxation/](requirements/taxation/) | Not started |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | Not started |
| Payroll | [requirements/payroll/](requirements/payroll/) | Not started |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | Not started |

Status values: Not started, In progress, In review, Complete.

## Sources

No sources registered yet — see [sources/](sources/).
```

- [ ] **Step 2: Create `hn/sources/README.md`**

```markdown
# Sources — Honduras

Original, unmodified documents from the Honduran tax authority (SAR) and
related official bodies. Never edit files here; parsers must treat them as
read-only.

## Registry

| File | Topic | Title | Issued | Retrieved | Provenance (URL) |
|------|-------|-------|--------|-----------|------------------|
| (none yet) | | | | | |

When adding a document: keep its original filename (prefix with `YYYY-MM-DD_`
only if it would collide), place it in this directory, and add a registry row.
```

- [ ] **Step 3: Create `hn/scripts/README.md`**

```markdown
# Scripts — Honduras

Country-specific parsing and extraction for Honduran source documents.
Format-generic helpers live in [shared/scripts](../../shared/scripts/) —
reuse them instead of duplicating here.

| Script | Purpose | Usage |
|--------|---------|-------|
| (none yet) | | |
```

- [ ] **Step 4: Create `hn/requirements/README.md`**

```markdown
# Requirements — Honduras

Extracted requirements, one directory per topic. Every file follows the
[requirements template](../../shared/docs/requirements-template.md).
Language: English, Spanish legal terms inline with translations.

| Topic | Status | Files |
|-------|--------|-------|
| [taxation](taxation/) | Not started | — |
| [chart-of-accounts](chart-of-accounts/) | Not started | — |
| [payroll](payroll/) | Not started | — |
| [fiscal-reporting](fiscal-reporting/) | Not started | — |

Status values: Not started, In progress, In review, Complete.
```

- [ ] **Step 5: Create the four topic directories (no e-invoicing)**

```bash
mkdir -p hn/requirements/taxation hn/requirements/chart-of-accounts \
  hn/requirements/payroll hn/requirements/fiscal-reporting
touch hn/requirements/taxation/.gitkeep \
  hn/requirements/chart-of-accounts/.gitkeep hn/requirements/payroll/.gitkeep \
  hn/requirements/fiscal-reporting/.gitkeep
```

- [ ] **Step 6: Verify structure and absence of e-invoicing**

Run: `find hn -type f | sort && ! test -e hn/requirements/e-invoicing && echo "no e-invoicing: OK"`
Expected:
```
hn/README.md
hn/requirements/README.md
hn/requirements/chart-of-accounts/.gitkeep
hn/requirements/fiscal-reporting/.gitkeep
hn/requirements/payroll/.gitkeep
hn/requirements/taxation/.gitkeep
hn/scripts/README.md
hn/sources/README.md
no e-invoicing: OK
```

- [ ] **Step 7: Commit**

```bash
git add hn
git commit --no-gpg-sign -m "Add Honduras directory scaffold"
```

---

### Task 7: Wire origin remote and final verification

**Files:**
- Modify: none (git remote configuration only)

**Interfaces:**
- Consumes: completed repo from Tasks 1–6.
- Produces: `origin` remote pointing at `git@github.com:CtrlCarlitos/odoo-localizations.git` (the GitHub repo must be created manually by the user — `gh` CLI is unavailable).

- [ ] **Step 1: Add origin remote**

```bash
git remote add origin git@github.com:CtrlCarlitos/odoo-localizations.git
```

(If it already exists from an earlier attempt, `git remote set-url origin git@github.com:CtrlCarlitos/odoo-localizations.git` instead.)

- [ ] **Step 2: Verify remote**

Run: `git remote -v`
Expected:
```
origin	git@github.com:CtrlCarlitos/odoo-localizations.git (fetch)
origin	git@github.com:CtrlCarlitos/odoo-localizations.git (push)
```

- [ ] **Step 3: Verify final tree matches the spec**

Run: `find . -path ./.git -prune -o -type f -print | sort`
Expected:
```
./.gitignore
./README.md
./docs/superpowers/plans/2026-08-16-repo-scaffolding.md
./docs/superpowers/specs/2026-08-16-repo-structure-design.md
./gt/README.md
./gt/requirements/README.md
./gt/requirements/chart-of-accounts/.gitkeep
./gt/requirements/e-invoicing/.gitkeep
./gt/requirements/fiscal-reporting/.gitkeep
./gt/requirements/payroll/.gitkeep
./gt/requirements/taxation/.gitkeep
./gt/scripts/README.md
./gt/sources/README.md
./hn/README.md
./hn/requirements/README.md
./hn/requirements/chart-of-accounts/.gitkeep
./hn/requirements/fiscal-reporting/.gitkeep
./hn/requirements/payroll/.gitkeep
./hn/requirements/taxation/.gitkeep
./hn/scripts/README.md
./hn/sources/README.md
./shared/docs/odoo-localization-guide.md
./shared/docs/requirements-template.md
./shared/scripts/README.md
./sv/README.md
./sv/requirements/README.md
./sv/requirements/chart-of-accounts/.gitkeep
./sv/requirements/e-invoicing/.gitkeep
./sv/requirements/fiscal-reporting/.gitkeep
./sv/requirements/payroll/.gitkeep
./sv/requirements/taxation/.gitkeep
./sv/scripts/README.md
./sv/sources/README.md
```

- [ ] **Step 4: Verify commit history**

Run: `git log --oneline`
Expected: 7 commits — the spec commit, then one per task above, newest first.

- [ ] **Step 5: Report push deferral**

Do NOT run `git push` — the SSH key `~/.ssh/id_CtrlCarlitos` is missing on this machine. Report to the user: once the key is provisioned and the GitHub repo exists, run `git push -u origin main`.

---

## Plan Self-Review (completed)

- **Spec coverage:** root README (Task 1), shared docs incl. template + guide (Task 2), shared scripts (Task 3), three country scaffolds with topic taxonomy (Tasks 4–6), git remote wiring (Task 7), HN explicitly without e-invoicing (Task 6). LFS deferral is a documented decision in the spec — no task required.
- **Placeholder scan:** no TBD/TODO; "(none yet)" table rows are legitimate initial state, not placeholders.
- **Consistency:** all relative links resolve (`../../shared/...` from `<cc>/requirements/` and `<cc>/scripts/`; `sv/` etc. from root README); commit messages follow short imperative style; `--no-gpg-sign` on every commit.
