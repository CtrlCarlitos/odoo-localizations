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
| Taxation | [requirements/taxation/](requirements/taxation/) | In review (draft, S2 ISR + S9 IVA + W17 CT-procedures (file 16)) |
| Chart of accounts | [requirements/chart-of-accounts/](requirements/chart-of-accounts/) | In review (draft, S8) |
| Payroll | [requirements/payroll/](requirements/payroll/) | In review (draft, S4) |
| Fiscal reporting | [requirements/fiscal-reporting/](requirements/fiscal-reporting/) | In review (draft, S3) |
| Commercial & legal | [requirements/commercial-legal/](requirements/commercial-legal/) | In review (draft, S5) |
| Special regimes | [requirements/special-regimes/](requirements/special-regimes/) | In review (draft, S7) |

Status values: Not started, In progress, In review, Complete.

## Sources

126 registered source file rows (numbering 01-128 + 17b; gaps 21/23/24/28
unused; the 25_ double vintage pdf+xlsx counts once in the numbering and
twice in the file rows — sources/README is the count of record; 66-70
added by the W11 Quincena-25 package; 71-73 added by W12 — AML regime
replacement D.L. 426 + kept UIF instructivo + CC verification copy; 74 added
by W13 — Ley de Simplificación Aduanera D. 529; 75 added by W16 —
Reglamento de Aplicación del CT, D.E. 117-2001; 76-105 added by W18 —
acquisition follow-ups (CVPCPA NIIF resoluciones + Ley Reguladora,
customs/regime + FYDUCA set, FOVIAL/COTRANS, ISR-tail transitories +
tasa prints, BCR Art. 46-f qualification set); 106 added by W21 — COTRANS
Aug-2025 prorroga D.L. 387-2025; 107-114 added by W22 — the SOQ-41
residuals (D.L. 201-2025 Aeropuerto del Pacífico + D.L. 411-2025 energía
eléctrica) + the post-2008 Código de Comercio reform set incl. THE SAS
statute (D.L. 905-2023); 115-126 added by W25 — the D.O. original prints
of 106_-114_ + the COTRANS chain texts 307/617/1000; 127 added by W27 —
Resolución CVPCPA 82-2024, the NIIF S1/S2 window + PYMES bar; 128 added
by W28 — Resolución CVPCPA 111-2026, the D.L. 426 supervisor-side AML
diagnostic requirement + no-lineamientos statement (SOQ-46 re-probe
by-product); next numbering = 129) — laws
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
