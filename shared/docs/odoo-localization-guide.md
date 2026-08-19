# Building an Odoo Localization Package

Shared reference for turning the requirements in this repository into Odoo
localizations. Target versions: **17.0, 18.0, 19.0, 20.0**.

> **Product architecture caveat:** the module-per-package anatomy below
> describes a conventional self-contained localization. Our current direction
> is a **thin-client Odoo module + proprietary Elixir/Phoenix SaaS core**
> (open-source client, paid service). Where that split lands is pending —
> see [saas-thin-client-architecture.md](saas-thin-client-architecture.md).
> Requirements carry the split via the Odoo Mapping **Layer** column; this
> guide's anatomy applies to whatever portions end up Odoo-side.

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

### Journal & document-type model (D13 — binding, decided 2026-08-18)

**Use `l10n_latam_invoice_document`: ONE journal carries MANY document
types.** The SV package depends on `l10n_latam_invoice_document` and models
document types as `l10n_latam.document.type` records (one per DTE type:
FE, CCF, NR, NC, ND, CR, CL, DCL, FEX, FSE, CD). A sales journal accepts
multiple document types via the journal↔document-type relation; each
`account.move` carries its own `l10n_latam_document_type_id` and
`l10n_latam_document_number`. **One journal per document type is
explicitly rejected** (an 11-journal sales setup is not the design).

Consequences for requirements and modules:

- Odoo Mapping rows reference the move-level document-type field, never a
  per-type journal; sequence/numeroControl machinery keys off
  (journal, document type), not journal alone.
- This is the same pattern as official `l10n_ar/cl/co/ec/mx/pe/uy`
  localizations — deviation from it needs an explicit ruling.
- The l10n_latam dependency is additive for SV: MH-specific validation
  (sello, codigoGeneración, transmission state) lives in the SV EDI layer
  on top; `l10n_latam` supplies only the journal/document-type shape.

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

## Regulatory change management

Spec versions change mid-flight (El Salvador changed its Normativa twice in six
months and re-versioned its catalogs). The version-regime decisions are SETTLED
(D7–D12 in [regulatory-change-management.md](regulatory-change-management.md)):
SaaS-side replace-in-place with switchover dates, immutable catalog releases,
freeze-at-filing reporting with a correction corollary (corrections post as new
entries in the correction period; originals immutable; origin-rate FX reuse),
additive normative packs + wizard Odoo-side. Requirements files must record the
version regime (version fields, effective dates, adaptation windows) wherever
it affects an FR (template §5 note, D12).
