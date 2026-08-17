# El Salvador — Requirements Extraction Plan

Execution plan per [shared/docs/requirements-extraction-procedure.md](../shared/docs/requirements-extraction-procedure.md).
Started 2026-08-16. Status: active.

## Context

- 54 sources registered in [sources/README.md](sources/README.md).
- Hint layer: [tuky-workspace prior project](https://github.com/CtrlCarlitos/tuky-workspace/tree/main/projects/odoo-localization-el-salvador) — 264 AI-generated requirements + design docs. Pointers only; every requirement re-derived from source.
- NotebookLM validator: notebook `c7ca0391-4822-4d3c-8090-b0d8c147ba94` (owner c20260202@gmail.com), partial corpus. Post-synthesis gap probing only, per the usage policy.

## Source inventory and decomposition

| # | Source | Governs | Reading units | Target topics |
|---|--------|---------|---------------|---------------|
| 1 | `20/25_Catalogos_Transmision*` | 32 MH catalogs (types, IDs, codes) | whole, catalog-by-catalog | catalogs (shared), feeds all |
| 2 | `40_manual_estructuras_catalogo.md` | DTE structures, field formats | structure-by-structure | e-invoicing, catalogs |
| 3 | `01_Ley_IVA.pdf` | IVA 13%, débito/crédito, pro-rata | Art. 1–125: tax core → taxation; Art. 54–75 operations → taxation; exemptions → taxation | taxation |
| 4 | `02_Reglamento_IVA.pdf` | IVA regulation | whole (repeal-aware vs Código Tributario) | taxation |
| 5 | `05_Codigo_Tributario.pdf` | Tax procedures, taxpayer registry, document authorization, books, penalties | registry/documents → e-invoicing; books/declarations → fiscal-reporting; penalties → taxation | all |
| 6 | `06_Guia_Facturacion_Electronica.pdf` | DTE system overview | whole | e-invoicing |
| 7 | `18_Normativa_Cumplimiento_DTE.pdf` | DTE compliance normative | whole | e-invoicing |
| 8 | `19_Manual_Funcional_Transmision.pdf` | Transmission functional flow | whole | e-invoicing |
| 9 | `22_Manual_Tecnologico_Transmision.pdf` | Auth, endpoints, payloads | whole | e-invoicing |
| 10 | `26_Manual_Consola_Administrativa.pdf` | MH admin console | whole | e-invoicing |
| 11 | `27_Manual_Obtencion_Certificado.pdf` | Certificate obtainment | whole | e-invoicing |
| 12 | `41_manual_eventos_invalidacion.md` | Invalidation events | whole | e-invoicing |
| 13 | `schemas/*.json` (13) | DTE JSON structures | schema-by-schema | e-invoicing, catalogs |
| 14 | `03_Ley_ISR.pdf` + `04_Reglamento_ISR.pdf` | ISR rates, brackets, withholding | core → taxation; retention tables → taxation | taxation |
| 15 | `10_Tablas_Retencion_ISR.pdf` | Payroll withholding tables | tables as data | taxation, payroll |
| 16 | `07_Codigo_Comercio.pdf` | Commercial registry, accounting books, retention | books → chart-of-accounts, fiscal-reporting; registry → commercial-legal | commercial-legal, chart-of-accounts |
| 17 | `15/17_Lavado_Activos.pdf` | AML obligations | thresholds/KYC → commercial-legal | commercial-legal |
| 18 | `08_Ley_ISSS.pdf`, `09_Ley_Sistema_Pensiones.pdf`, `11_Codigo_Trabajo.pdf`, `16_Salarios_Minimos_2025.pdf` | Social security, pensions, labor law, minimum wage | contributions → payroll; contracts/leave/overtime → payroll | payroll |
| 19 | `29/34/35/36/37/38/39_F07/F14*` | F-07/F-14 forms, annexes, templates | annex-by-annex | fiscal-reporting |
| 20 | `30_Calendario_Tributario_2026.pdf` | Filing calendar | as data | fiscal-reporting |
| 21 | `12_Ley_Zonas_Francas.pdf`, `13_Ley_Organica_Aduanas.pdf`, `14/17b_Servicios_Internacionales.pdf`, `43_DUCA_Instructivo_COMIECO.pdf`, `42_Comunicado_Exportaciones_Panama.docx` | Free zones, customs, international services, DUCA | each law whole | special-regimes |
| 22 | `31_Guia_FOVIAL_COTRANS.pdf` | Fuel contributions | whole | taxation (quantity-based — flag for Odoo Mapping) |
| 23 | `32/33_NIIF*.pdf` | NIIF PYMES, sustainability | accounting treatment → chart-of-accounts | chart-of-accounts |

## Reading order

Dependency-aware; each batch's outputs feed the next.

1. **Foundations**: catalogs (1, 2) + schemas (13) — vocabulary everything cites
2. **IVA core**: Ley IVA (3) → Reglamento IVA (4) — gravada/exenta/no-sujeta, débito/crédito, pro-rata. Everything depends on operation types
3. **Código Tributario** (5) — procedures, documents, books; repeal authority for (4)
4. **DTE stack** (6–12) — transmission, invalidation, contingency, certificates
5. **ISR** (14, 15) — rates, withholding
6. **F-07/F-14** (19, 20) — needs DTE fields + ISR/IVA concepts in place
7. **Payroll** (18) — independent track, can run parallel after (1)
8. **Commercial/legal** (16, 17)
9. **Special regimes** (21) — needs IVA + DTE context
10. **FOVIAL/COTRANS** (22), **NIIF** (23) — closers

## Topic map (source unit → topic)

| Topic | From |
|-------|------|
| `catalogs/` | units 1, 2, 13 (sidecars CSV) |
| `taxation/` | 3, 4, 5(partial), 14, 15, 22 |
| `e-invoicing/` | 5(partial), 6–12, 13(partial) |
| `fiscal-reporting/` | 5(partial), 16(partial), 19, 20 |
| `payroll/` | 15(partial), 18 |
| `commercial-legal/` | 16(partial), 17 |
| `special-regimes/` | 21 |
| `chart-of-accounts/` | 16(partial), 23 |

## Known risks

- **Repeals**: IVA/ISR Reglamento procedural articles repealed by Código Tributario (hint layer flagged many; confirm per article during merge).
- **Wrong-document incident**: file `14_` was previously an unconstitutional version; current file is Decreto 431 (2007) + Reglamento 131 (`17b_`). Verified at import.
- **Scanned PDFs**: F-07/F-14 manuals are form scans; extraction quality must be checked — OCR fallback if needed.
- **Numbering gaps** in sources (21, 23, 24, 28): documents not carried over; if coverage matrix shows gaps, retrieve from MH.
- **FOVIAL/COTRANS**: quantity-based taxes ($/gallon) — no native Odoo tax; Odoo Mapping needs explicit design decision.
- **Sello/estado dual management**: MH state vs Odoo state — likely cross-topic FR cluster; assign home in synthesis.

## Deliverables

1. `requirements/COVERAGE.md` — generated, kept current per synthesis wave
2. Topic files per the Takumi template; FR IDs `SV-<TOPIC>-FR-<nnn>`
3. `requirements/catalogs/` with machine-readable sidecars from catalogs XLSX/structures

## Session protocol

Massive task; executed in waves over multiple sessions. Each session:
extract text for the batch → evidence pass → merge → synthesize → update this
plan and the coverage matrix → commit. Never leave a session with evidence
unmerged; scratch dies with context.
