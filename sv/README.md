# El Salvador (SV)

Odoo localization requirements for El Salvador, including electronic
invoicing (facturación electrónica).

- **Tax authority:** Ministerio de Hacienda (MH) — https://www.mh.gob.sv
- **Takumi proof of concept:** not started.

## Requirements status

| Topic | Directory | Status |
|-------|-----------|--------|
| Electronic invoicing | [requirements/e-invoicing/](requirements/e-invoicing/) | In review (draft, S1) |
| Catalogs | [requirements/catalogs/](requirements/catalogs/) | In review (draft, S1) |
| Taxation | [requirements/taxation/](requirements/taxation/) | In review (draft, S2 ISR) |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | Not started |
| Payroll | [requirements/payroll/](requirements/payroll/) | Not started |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | Not started |
| Commercial & legal | [requirements/commercial-legal/](requirements/commercial-legal/) | Not started |
| Special regimes | [requirements/special-regimes/](requirements/special-regimes/) | Not started |

Status values: Not started, In progress, In review, Complete.

## Sources

56 registered source files (numbering 01-64; gaps 21/23/24/28 unused) — laws
and regulations (tax, commercial, labor), MH electronic-invoicing manuals and
catalogs, F-07/F-14 forms and templates, NIIF — plus the 15 current official
MH JSON schemas inside `52_Json_Schemas_DTE_Eventos_2026-08-11.zip` and a
superseded 2022 `schemas/` directory — see
[sources/README.md](sources/README.md).

## Prior work

Requirements and implementation-design documents for El Salvador were
previously produced in the
[tuky-workspace repository](https://github.com/CtrlCarlitos/tuky-workspace/tree/main/projects/odoo-localization-el-salvador)
(264 extracted requirements across 7 categories, 60+ design documents,
adversarial review rounds). They are kept there as external reference only.
This workspace performs a fresh extraction from the same source documents,
following the [requirements template](../shared/docs/requirements-template.md).
