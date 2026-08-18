# SV — Source coverage matrix

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | all (cross-topic) |
| Status  | draft (S1 synthesis wave) |
| Authors | Controller (hand-built; script to regenerate later) |
| Updated | 2026-08-17 |

Every file in [../sources/](../sources/) mapped against the S1 requirements
wave. Status values:

- **cited-as-LB** — appears in a Legal Basis row (or as direct schema read) of a requirements file; the citing file(s) named.
- **not-applicable-this-wave** — out of S1 scope or superseded-without-content-need; reason noted.
- **pending-S2+** — earmarked for later waves: ISR, F-07/F-14, payroll, commercial-legal, special-regimes, NIIF / fiscal-reporting.
- **superseded-not-cited** — superseded extraction retained on disk for reference; not a legal-basis citation (the superseding source is the cited LB).

No orphans: every row carries at least one of the four. Sources fully
superseded but cited as historical LB (25_\*, 40_, 41_) still count as
cited-as-LB.

## Matrix (53 source files + schemas/ dir = 54 rows)

| Source | Status | Cited in / note |
|--------|--------|-----------------|
| 01_Ley_IVA.pdf | cited-as-LB | `e-invoicing/01` LB-008/009/010; `e-invoicing/03` LB-012 |
| 02_Reglamento_IVA.pdf | pending-S2+ | taxation / commercial-legal wave |
| 03_Ley_ISR.pdf | pending-S2+ | ISR wave — **superseded as current authority by 54_** (retained as W6 historical LB; reform chain D.L. 762-2014/458-2019/969-2024/293-2025) |
| 04_Reglamento_ISR.pdf | pending-S2+ | ISR wave |
| 05_Codigo_Tributario.pdf | cited-as-LB | `e-invoicing/01` LB-007/011/012 |
| 06_Guia_Facturacion_Electronica.pdf | not-applicable-this-wave | non-normative guide; S1 rests on 44_/45_/46_/50_/51_/52_ |
| 07_Codigo_Comercio.pdf | pending-S2+ | commercial-legal wave |
| 08_Ley_ISSS.pdf | pending-S2+ | payroll wave |
| 09_Ley_Sistema_Pensiones.pdf | pending-S2+ | payroll wave |
| 10_Tablas_Retencion_ISR.pdf | pending-S2+ | ISR wave — 1992 colones-era (D.E. 75/25); superseded by 53_ (D.E. 10-2025); retained as historical LB |
| 53_Tablas_Retencion_ISR_DE10_2025.pdf | pending-S2+ | ISR wave (current retention tables) |
| 54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf | pending-S2+ | ISR wave (current consolidated Ley ISR; reform history) |
| 55_Reforma_Ley_ISR_DL293_DO_2025-04-30.pdf | pending-S2+ | ISR wave (Art. 37 reform, effective 2025-05-08) |
| 11_Codigo_Trabajo.pdf | pending-S2+ | payroll wave |
| 12_Ley_Zonas_Francas.pdf | pending-S2+ | special-regimes wave |
| 13_Ley_Organica_Aduanas.pdf | pending-S2+ | special-regimes / customs-export wave |
| 14_Ley_Servicios_Internacionales.pdf | pending-S2+ | special-regimes wave |
| 15_Ley_Lavado_Activos.pdf | pending-S2+ | commercial-legal (KYC/AML) wave |
| 16_Salarios_Minimos_2025.pdf | pending-S2+ | payroll wave (SMM figure also feeds `e-invoicing/01` OQ-007 threshold config) |
| 17_Reglamento_Lavado_Activos.pdf | pending-S2+ | commercial-legal (KYC/AML) wave |
| 17b_Reglamento_Servicios_Internacionales.pdf | pending-S2+ | special-regimes wave |
| 18_Normativa_Cumplimiento_DTE.pdf | cited-as-LB | `e-invoicing/01` LB-014; `02` LB-009; `03` LB-008; `04` LB-009/010; `catalogs/05` LB-003 |
| 19_Manual_Funcional_Transmision.pdf | not-applicable-this-wave | 2025 functional manual; authority-order preamble only (no LB row); content superseded by 45_/46_/47_ |
| 20_Catalogos_Transmision.pdf | not-applicable-this-wave | 2022 catalog PDF; supersession chain 20_ → 25_ → 50_/51_; catalogs wave cites 50_/51_/25_ |
| 22_Manual_Tecnologico_Transmision.pdf | cited-as-LB | `e-invoicing/02` LB-008; `04` LB-007; `06` LB-008 |
| 25_Catalogos_Transmision_v1.2.pdf | not-applicable-this-wave | PDF twin of the cited 25_ XLSX (below) |
| 25_Catalogos_Transmision_v1.2.xlsx | cited-as-LB | `catalogs/05` LB-005 — superseded-historical (v1.2 regime documents) |
| 26_Manual_Consola_Administrativa.pdf | not-applicable-this-wave | MH emitter-console manual; S1 scope is system-to-system (46_); candidate for onboarding (A11) wave |
| 27_Manual_Obtencion_Certificado.pdf | cited-as-LB | `e-invoicing/04` LB-008 |
| 29_Modificacion_Anexos_F07_F14.pdf | pending-S2+ | F-07/F-14 wave |
| 30_Calendario_Tributario_2026.pdf | pending-S2+ | fiscal-reporting wave (deadline calendar config) |
| 31_Guia_FOVIAL_COTRANS.pdf | pending-S2+ | special-regimes wave (FOVIAL/COTRANS) |
| 32_NIIF_PYMES_2025.pdf | pending-S2+ | NIIF wave |
| 33_Guia_NIIF_Sostenibilidad_2024-2025.pdf | pending-S2+ | NIIF wave |
| 34_F07_v14_manual.pdf | pending-S2+ | F-07/F-14 wave |
| 35_F14_v16_manual.pdf | pending-S2+ | F-07/F-14 wave |
| 36_F07_v14_plantilla.xls | pending-S2+ | F-07/F-14 wave |
| 37_F14_v16_plantilla.xls | pending-S2+ | F-07/F-14 wave |
| 38_F14_v16_form_visual.pdf | pending-S2+ | F-07/F-14 wave |
| 39_F07_v14_form_visual.pdf | pending-S2+ | F-07/F-14 wave |
| 40_manual_estructuras_catalogo.md | cited-as-LB | `e-invoicing/01` LB-015; `04` LB-011 — superseded-primary, cited as historical LB (MOQ-08 flags) |
| 41_manual_eventos_invalidacion.md | cited-as-LB | `e-invoicing/03` LB-009 — superseded-primary, cited as historical LB |
| 42_Comunicado_Exportaciones_Panama.docx | pending-S2+ | special-regimes / exports wave |
| 43_DUCA_Instructivo_COMIECO.pdf | pending-S2+ | special-regimes / customs (DUCA) wave |
| 44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf | cited-as-LB | `e-invoicing/01` LB-001/002; `02` LB-001/002/003; `03` LB-001..004; `04` LB-001/002; `06` LB-002/003/004/010 |
| 45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf | cited-as-LB | `e-invoicing/01` LB-003/004/005/013; `02` LB-004/005/006; `03` LB-005/006/007; `04` LB-003/004/005; `catalogs/05` LB-004; `06` LB-005/006 |
| 46_Manual_Tecnologico_Integracion_v2.0_2026-05-25.pdf | cited-as-LB | `e-invoicing/02` LB-007; `03` LB-014; `04` LB-006; `06` LB-009 |
| 47_Manual_Funcional_Sistema_Transmision_2026-05-25.pdf | not-applicable-this-wave | v2.0 functional manual; S1 LB rests on 45_ §§ + 46_ (raw-text verified); cite in later waves when entrega/consola UX detail is specified |
| 48_Manual_Estructuras_Catalogos_Modelos_v1.6.pdf | not-applicable-this-wave | pre-v2.0 structures manual; superseded by 45_ Anexo II (+ 40_ historical citations) |
| 49_Manual_Eventos_Invalidacion_Contingencia_v1.1.pdf | not-applicable-this-wave | PDF original of the 2022 events manual; the .md extraction (41_) is the cited LB (`03` LB-009) |
| 50_Catalogos_Facturacion_Electronica_v1.1_2026-07.pdf | cited-as-LB | `catalogs/05` LB-002 (human-reference fallback) |
| 51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx | cited-as-LB | `catalogs/05` LB-001; `e-invoicing/01` LB-016; `02` LB-010; `03` LB-011; `04` LB-012 |
| 52_Json_Schemas_DTE_Eventos_2026-08-11.zip | cited-as-LB | `e-invoicing/01` LB-006; `03` LB-010; `06` LB-007 |
| schemas/ (13 JSON schema files) | superseded-not-cited | superseded 2022-era extraction (fe-ccf-v3, contingencia-v3, anulacion-v2 era; no fe-eret/fe-eop) — NOT the current set; the current 15-schema set lives inside `52_Json_Schemas_DTE_Eventos_2026-08-11.zip`, which is the LB cited directly (`e-invoicing/01` LB-006; `03` LB-010) |

## Rollup

| Status | Rows |
|--------|------|
| cited-as-LB | 14 |
| superseded-not-cited | 1 (schemas/) |
| not-applicable-this-wave | 8 |
| pending-S2+ | 31 |
| **Total** | **54** |
