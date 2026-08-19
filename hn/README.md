# Honduras (HN)

Odoo localization requirements for Honduras.

- **Tax authority:** Servicio de Administración de Rentas (SAR) — https://www.sar.gob.hn
- **Takumi proof of concept:** not started.
- **Research dossier:** [RESEARCH.md](RESEARCH.md) (source-research pass 2026-08-18/19).

## Scope note (electronic invoicing)

Honduras has no national XML electronic-invoicing regime in force (verified
2026-08-19, see RESEARCH.md §2). The `e-invoicing` topic for HN covers the
**digital administration of the paper fiscal-document regime** (régimen de
facturación: imprentas/autoimpresores, Acuerdo 481-2017; RECAEFUSAR workflow,
validador, compras eventuales). A future SAR electronic-invoicing rollout is a
watch item, not a current scope change.

## Requirements status

| Topic | Directory | Status |
|-------|-----------|--------|
| E-invoicing (paper-regime digital administration) | [requirements/e-invoicing/](requirements/e-invoicing/) | Not started |
| Taxation | [requirements/taxation/](requirements/taxation/) | Not started |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | Not started |
| Payroll | [requirements/payroll/](requirements/payroll/) | Not started |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | Not started |
| Commercial-legal | [requirements/commercial-legal/](requirements/commercial-legal/) | Not started |

Status values: Not started, In progress, In review, Complete.

## Sources

85 registered source files (01-86, gap 85) — see [sources/README.md](sources/README.md).
Core: ISR/ISV/CT consolidations, IPC-indexed ISR table series (FY2023-FY2026),
retenciones/DMR/DMC procedures, facturación reglamento, payroll 2024
architecture (IHSS D. 48-2024, RAP fondo de reserva D. 47-2024), salario
mínimo bienio 2024-2025, Código del Trabajo, and the per-código "Ayuda"/
"Generalidades" form-documentation layer.
