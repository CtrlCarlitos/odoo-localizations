# SV — Source coverage matrix

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | all (cross-topic) |
| Status  | draft (S1 + S2 ISR + S3 fiscal-reporting + S4 payroll + S5 commercial-legal + S7 special-regimes + S8 chart-of-accounts waves) |
| Authors | Controller (hand-built; script to regenerate later) |
| Updated | 2026-08-20 (S8) |

Every file in [../sources/](../sources/) mapped against the S1, S2 (ISR),
S3 (fiscal-reporting), S4 (payroll), S5 (commercial-legal), S7
(special-regimes) and S8 (chart-of-accounts) requirements waves. Status values:

- **cited-as-LB** — appears in a Legal Basis row (or as direct schema read) of a requirements file; the citing file(s) named.
- **not-applicable-this-wave** — out of the current wave's scope or superseded-without-content-need; reason noted.
- **pending-S2+** — earmarked for later waves: IVA-core taxation, NIIF.
- **superseded-not-cited** — superseded extraction retained on disk for reference; not a legal-basis citation (the superseding source is the cited LB).

No orphans: every row carries at least one of the four. Sources fully
superseded but cited as historical LB (25_\*, 40_, 41_) still count as
cited-as-LB.

## Matrix (72 source files + schemas/ dir = 73 rows)

| Source | Status | Cited in / note |
|--------|--------|-----------------|
| 01_Ley_IVA.pdf | cited-as-LB | `e-invoicing/01` LB-008/009/010; `e-invoicing/03` LB-012; `fiscal-reporting/02` LB-008 (Ley IVA Art. 57); `chart-of-accounts/06` LB-012 (Arts. 62-63 pointers) |
| 02_Reglamento_IVA.pdf | pending-S2+ | IVA-core taxation wave (01_/02_ still owed to `taxation/`) |
| 03_Ley_ISR.pdf | cited-as-LB | historical — authority-order preambles of `taxation/01..06`; superseded as current authority by 54_ (reform chain D.L. 762-2014/458-2019/969-2024/293-2025); supplies analysis via EVID ids |
| 04_Reglamento_ISR.pdf | cited-as-LB | `taxation/01..06` LB rows (21 rows; D.E. 101-1992 consolidated, survivor articles only per R17) |
| 05_Codigo_Tributario.pdf | cited-as-LB | `e-invoicing/01` LB-007/011/012; `fiscal-reporting/06` LB-008 (CT 154-160); `fiscal-reporting/07` LB-006 (CT 123/124) |
| 06_Guia_Facturacion_Electronica.pdf | not-applicable-this-wave | non-normative guide; S1 rests on 44_/45_/46_/50_/51_/52_ |
| 07_Codigo_Comercio.pdf | cited-as-LB | `commercial-legal/01..09` LB rows (211 — 07_-sourced rows excluding 02's 71_ LB-013 and 04's pointer LB-032; 213 = all 01-09 LB rows; Código de Comercio D.L. 671-1970 current; article text verified vs second official copy 73_ (SOQ-22 resolved-with-residual: both reform lists end at D.L. 641-2008; editorial-artifact residual rides every 07_ LB)) |
| 08_Ley_ISSS.pdf | cited-as-LB | `payroll/01` LB-008; `payroll/05` LB-001..005; `payroll/06` LB-009..011 |
| 09_Ley_Sistema_Pensiones.pdf | cited-as-LB | `payroll/01` LB-009/010; `payroll/04` LB-021; `payroll/05` LB-006..011; `payroll/06` LB-001..008; `payroll/07` LB-021; `payroll/08` LB-001/002 |
| 10_Tablas_Retencion_ISR.pdf | cited-as-LB | historical — `taxation/04` LB-020 (1992 colones-era D.E. 75/25; superseded by the 53_ chain via D.E. 95-2015; dated-data rows in `isr_brackets.csv`) |
| 53_Tablas_Retencion_ISR_DE10_2025.pdf | cited-as-LB | `taxation/04` LB rows (8 — current tables) + `taxation/01` LB-028 (filing/threshold bits) |
| 54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf | cited-as-LB | `taxation/01..06` LB rows (71 rows — current consolidated Ley ISR); `chart-of-accounts/08` LB-005 (pointer row) |
| 55_Reforma_Ley_ISR_DL293_DO_2025-04-30.pdf | cited-as-LB | `taxation/03` (Art. 37 table vintage, effective 2025-05-08) |
| 56_Reforma_Ley_ISR_DL969_DO_2024-03-14.pdf | cited-as-LB | `taxation/01` (Art. 3.4 foreign-source exclusion + derogations) |
| 57_InterpAut_Art30_DL192_DO_2018-12-12.pdf | cited-as-LB | `taxation/06` (Art. 30.1 seasonal depreciation) |
| 58_InterpAut_Art28_DL345_DO_2019-05-31.pdf | cited-as-LB | `taxation/02` (Art. 28 mermas deductibility) |
| 59_F14_v17_form_visual.pdf | cited-as-LB | `fiscal-reporting/06` LB rows (v17 form — Quincena-25 section row 61 casillas 417/418; rows 62-105 renumbered vs v1.6; annex-level representation blocked pending a v17 manual — SOQ-09) |
| 60_DE10_Tablas_Retencion_DO_2025-04-30.pdf | cited-as-LB | `taxation/04` LB-013 (co-cited: D.O. pin + gazette digit verification, EVID-171 — SOQ-03 resolved) |
| 61_F910v9_informe_anual_retenciones.pdf | cited-as-LB | `fiscal-reporting/07` LB rows (F-910 v9 annual ISR retentions inform — CT Art. 123 surface) |
| 62_F915v4_informe_distribucion_utilidades.pdf | cited-as-LB | `fiscal-reporting/07` LB rows (F-915 v4 distributions/shareholder-list inform) |
| 63_F930v3_informe_mensual_retIVA.pdf | cited-as-LB | `fiscal-reporting/04` LB rows (F-930 v3 monthly retIVA inform homed there); `fiscal-reporting/07` (referenced, re-check cadence OQ-004) |
| 64_F935v1_informe_mensual_agentes_extranjeros.pdf | cited-as-LB | `fiscal-reporting/07` LB rows (F-935 v1 monthly foreign-agents inform; SOQ-13 anchor OQ) |
| 65_F11_v18_form_visual.pdf | cited-as-LB | `payroll/08` LB-004..006 (F-11 v18 personal-deduction value feeds — SS rows 713/714/716/721/724, AFP voluntary quota 717, deducción fija 722, total 725; no-gravadas 734; dead pago-mínimo print); `fiscal-reporting/07` OQ-006 coupling counterpart. **Superseded as current print by v19/v20 (per 67_ Anexos 1/8) — not yet acquired (66-70_ OQ-5)** |
| 66_Ley_Quincena25_DL499.pdf | cited-as-LB | law LBs (folded S6 2026-08-18): `payroll/04` LB-025..028 (FR-138..141 benefit mechanics); `payroll/08` LB-012/013 (FR-137 income treatment + FR-142/143 feeds); `taxation/01` LB-032..034 (FR-173/174), `taxation/02` LB-019 (FR-175); also cited in `payroll/01`'s category matrix (FR-004 amendment, Arts. 1/4) |
| 67_Guia_Orientacion_Quincena25.pdf | cited-as-LB | guía LBs (folded S6 2026-08-18): `fiscal-reporting/06` LB-009 (January-only window + 417/418), `fiscal-reporting/07` LB-010 (F-910 code 73), `taxation/01` LB-035 (FR-174 surfaces), `taxation/02` LB-020 (FR-175 documentation), `payroll/08` LB-014 (code 73 + casilla 724 ruling); F-11 v19 (casilla 319) + v20 (Sujetos con Régimen Especial) discovery carried — prints to acquire (≥71) |
| 68_Instrucciones_Carga_Quincena25.pdf | cited-as-LB | upload-flow LBs (folded S6 2026-08-18): `fiscal-reporting/06` LB-010 (January-window gate, Limpiar-to-replace, code-73 auto-assignment — FR-210/211); `fiscal-reporting/07` LB-010 co-cite (68_ p.16, FR-212) |
| 69_Manual_Usuario_Carga_Quincena25.pdf | cited-as-LB | annex-CSV format spec LB (folded S6 2026-08-18): `fiscal-reporting/06` LB-011 (7-column spec §1-3 — FR-209) |
| 70_Plantilla_Quincena25.xls | cited-as-LB | delimiter LB (folded S6 2026-08-18): `fiscal-reporting/06` LB-012 (semicolon header line — the `;` operative-delimiter ruling, FR-209/OQ-009) |
| 71_Ley_LavadoActivos_DL426_2025.pdf | cited-as-LB | `commercial-legal/10` LB rows + `commercial-legal/02` (LB-013, Art. 26 retention) (current AML law D.L. 426, effective 2025-10-17 — wholesale replacement of D. 498; C10 rebased on EVID-241..250; R28: Art. 61 keeps 17_/72_, Art. 25 delegates thresholds) |
| 72_Instructivo_UIF_Acuerdo380_reform2023.pdf | cited-as-LB | `commercial-legal/10` LB rows (kept UIF instructivo per 71_ Art. 61 — operative threshold values Art. 51 ($10k cash/$25k other media) + Art. 52 institutional aggregates, DD/ROS mechanics; EVID-247..249; R28 authority chain) |
| 73_Codigo_Comercio_UIF_indicelegislativo.pdf | cited-as-LB | verification co-cites in `commercial-legal/01..09` §2 preambles (all nine files; + `04` LB-032 pointer row via the 71-73_ evidence gloss) — verification-grade second CC copy (SOQ-22 resolved-with-residual, EVID-250); no independent LB article-text role |
| 74_Ley_Simplificacion_Aduanera_D529.pdf | cited-as-LB | `special-regimes/01` LB-024/025 (declarante roles, consultas); `05` LB-008 (Art. 11-A h) SS-solvencia kin of FR-102); `06` LB rows (9: teledespacho, $18 tasa, presumed valuation, anulación clocks, 5-y caducidad); `07` LB-022 (Art. 13 5-y retention kin) — D. 529-1999 consolidated through D.L. 23-2012, acquired W13 from uif.gob.sv, as printed (SOQ-30) |
| 11_Codigo_Trabajo.pdf | cited-as-LB | `payroll/01` LB-001..007; `payroll/02` LB-001..004, LB-011; `payroll/03` LB-001..020; `payroll/04` LB-001..020, LB-022; `payroll/06` LB-013; `payroll/07` LB-001..010, LB-013..021 |
| 12_Ley_Zonas_Francas.pdf | cited-as-LB | `special-regimes/01` LB rows (11); `02` (14); `04` (6); `05` (4); `07` (12) — D.L. 405-1998 consolidated through D.L. 318-2013, cited as printed (SOQ-30) |
| 13_Ley_Organica_Aduanas.pdf | cited-as-LB | `special-regimes/01` LB rows (2: DGA institutional frame); `06` §2 authority-order preamble; `07` LB row (Art. 19) — D. 903 through D.L. 121-2012, as printed |
| 14_Ley_Servicios_Internacionales.pdf | cited-as-LB | `special-regimes/01` LB rows (10); `02` LB-017 (declaration-duty kin); `03` (11); `04` (8); `05` (3); `07` (5) — D.L. 431 2007 print "Reformas: S/R", as printed |
| 15_Ley_Lavado_Activos.pdf | cited-as-LB | historical — `commercial-legal/10` §2 preamble + authority-order note (derogated wholesale by 71_ D.L. 426 Art. 61, effective 2025-10-17; historical LB for pre-cutover facts only, never current authority — R28; W10 evidence EVID-228..231 historical; no S5 LB row beyond the historical note; R25 title-vs-content: content = D. 498-1998 through reform (6) D.L. 104-2015) |
| 16_Salarios_Minimos_2025.pdf | cited-as-LB | `payroll/02` LB-005..010 (Decreto 11-2025 tariffs → `smm_2025.csv`); `payroll/03` LB-021; `payroll/04` LB-024; `payroll/06` LB-012; `payroll/07` LB-011 (SMM figure also feeds `e-invoicing/01` OQ-007 threshold config) |
| 17_Reglamento_Lavado_Activos.pdf | cited-as-LB | `commercial-legal/10` LB rows (10 co-cites — kept-in-force OPERATIVE reglamento per 71_ Art. 61 + R26 addendum (no post-568-2013 reglamento ever issued): window mechanics, no-tip-off, red-flag catalogs; stale pre-reform thresholds never cited) |
| 17b_Reglamento_Servicios_Internacionales.pdf | cited-as-LB | `special-regimes/03` LB rows (6: Art. 22 caps 50/40/30, dictamen, inventory-register contract); `07` (3) — Reglamento D. 131-2008, as printed |
| 18_Normativa_Cumplimiento_DTE.pdf | cited-as-LB | `e-invoicing/01` LB-014; `02` LB-009; `03` LB-008; `04` LB-009/010; `catalogs/05` LB-003 |
| 19_Manual_Funcional_Transmision.pdf | not-applicable-this-wave | 2025 functional manual; authority-order preamble only (no LB row); content superseded by 45_/46_/47_ |
| 20_Catalogos_Transmision.pdf | not-applicable-this-wave | 2022 catalog PDF; supersession chain 20_ → 25_ → 50_/51_; catalogs wave cites 50_/51_/25_ |
| 22_Manual_Tecnologico_Transmision.pdf | cited-as-LB | `e-invoicing/02` LB-008; `04` LB-007; `06` LB-008 |
| 25_Catalogos_Transmision_v1.2.pdf | not-applicable-this-wave | PDF twin of the cited 25_ XLSX (below) |
| 25_Catalogos_Transmision_v1.2.xlsx | cited-as-LB | `catalogs/05` LB-005 — superseded-historical (v1.2 regime documents) |
| 26_Manual_Consola_Administrativa.pdf | not-applicable-this-wave | MH emitter-console manual; S1 scope is system-to-system (46_); candidate for onboarding (A11) wave |
| 27_Manual_Obtencion_Certificado.pdf | cited-as-LB | `e-invoicing/04` LB-008 |
| 29_Modificacion_Anexos_F07_F14.pdf | not-applicable-this-wave | mislabeled source: the PDF's actual content is the CNR *Registro de Comercio* F-985 regime (extraction `29_F985_CNR_RegComercio`), NOT the F-07/F-14 annex-modification resolutions — the intended resolutions behind v14/v16/v17 remain absent from the corpus (SOQ-12; referenced only as "29_-file OQ-1 kin" in `fiscal-reporting/06` OQ-004 / `07` OQ-001); registry-side F-985 content is out of this wave's scope |
| 30_Calendario_Tributario_2026.pdf | cited-as-LB | `fiscal-reporting/08` LB rows (2026 tax calendar — obligation inventory, due-day visual layer, asueto legend) |
| 31_Guia_FOVIAL_COTRANS.pdf | cited-as-LB | `special-regimes/08` LB rows (6: whole guide, S7 2026-08-19) — provenance chain: guide = secondary authority citing D.L. 208-2000 Art. 26 as reformed D.L. 597-2001; law text absent (SOQ-39; COTRANS instrument absent, MOQ-04 half-open) |
| 32_NIIF_PYMES_2025.pdf | cited-as-LB | `chart-of-accounts/01..08` LB rows (50 — THE operative framework LB of the S8 wave per R29: Secciones 1-35 + Apéndices A/B cited by section/párrafo as printed) + §2 authority-order preambles (all eight files, S8 2026-08-20; EVID-275..298; SOQ-46 instrument gap gates eligibility config) |
| 33_Guia_NIIF_Sostenibilidad_2024-2025.pdf | cited-as-LB | SECONDARY-ONLY LB rows per R29(a) — `chart-of-accounts/01` LB-007 (NIIF 19 framework-flag third value); `03` LB-008; `05` LB-007; `07` LB-007; `08` LB-004 (5 rows total: version/horizon facts — NIIF 18/19 2027-01-01, S1/S2 2024 — + the full-NIIF-vs-PYMES contrast set; never sole LB; EVID-299..303) |
| 34_F07_v14_manual.pdf | cited-as-LB | `fiscal-reporting/01` LB rows (upload-engine §II/§XVI/§XVII); `02` LB rows (§III-§IV sales annexes); `03` (§V/§VII purchase annexes); `04` (§XIX anulados + SOQ-10 defect ruling LB-007); `05` (§XX-§XXIV special annexes); `07` (EVID-182 income-code apéndice transcription) |
| 35_F14_v16_manual.pdf | cited-as-LB | `fiscal-reporting/06` LB rows (F-14 v16 annex row model + export contract); `07` (income-code catalog vintage, Oct-2025) |
| 36_F07_v14_plantilla.xls | cited-as-LB | plantilla anchors: `fiscal-reporting/02` (Anexo 1/2 sheet columns); `03` (Anexo 3/5 sheets); `04` (annexes 4/6-12 sheets; anulados absent from sheets 1-12 — OQ-003) |
| 37_F14_v16_plantilla.xls | cited-as-LB | plantilla anchors: `fiscal-reporting/06` ("Detalle" sheet — annex column template; F-14 export-format OQ-006) |
| 38_F14_v16_form_visual.pdf | cited-as-LB | `fiscal-reporting/06` LB rows (v16 seven-tab form architecture); `07` (v16 row/casilla zones behind the catalog mapping) |
| 39_F07_v14_form_visual.pdf | cited-as-LB | `fiscal-reporting/01` LB rows (v14 77-row casilla graph, USD footer); `03` (purchase credit casilla labels); `04` (retention credit labels); `05` (fuel/price-cap casilla labels) |
| 40_manual_estructuras_catalogo.md | cited-as-LB | `e-invoicing/01` LB-015; `04` LB-011 — superseded-primary, cited as historical LB (MOQ-08 flags) |
| 41_manual_eventos_invalidacion.md | cited-as-LB | `e-invoicing/03` LB-009 — superseded-primary, cited as historical LB |
| 42_Comunicado_Exportaciones_Panama.docx | cited-as-LB | `special-regimes/06` LB row (DUCA-F SV↔Panamá SIECA electronic transmission from 2025-03-03 — dated operational fact) |
| 43_DUCA_Instructivo_COMIECO.pdf | cited-as-LB | `special-regimes/04` LB row (DUCA field 14 regime-expiry + field 56 FAUCA validity, as printed); `06` LB rows (10: 62-field contract, Res. 409-2018 whole) |
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

## Rollup (final through S8; 02_ stays pending for the IVA-core wave)

| Status | Rows |
|--------|------|
| cited-as-LB | 62 |
| superseded-not-cited | 1 (schemas/) |
| not-applicable-this-wave | 9 |
| pending-S2+ | 1 (02_ IVA-core wave) |
| **Total** | **73** |

S8 note: 32_/33_ flipped from the W14 interim (provisional-cited on the
strength of the master-index clusters) to per-file LB citations by the S8
synthesis wave (2026-08-20) — 32_ as the framework LB of all eight
`chart-of-accounts/` files, 33_ as five secondary-only rows in
01/03/05/07/08.
