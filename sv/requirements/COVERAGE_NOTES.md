# SV — Coverage curated notes

Curated half of the coverage matrix: `shared/scripts/build_coverage.py`
regenerates the citing-file lists mechanically (LB citation scan) and merges
this file's status overrides and note fragments into `COVERAGE.md`. Status
tokens stay exact; fragments append to the auto-generated list. Citing-file
lists must NOT be duplicated here — they regenerate.

## Status overrides

| Source | Status |
|--------|--------|
| 03_Ley_ISR.pdf | cited-as-LB |
| 06_Guia_Facturacion_Electronica.pdf | not-applicable-this-wave |
| 15_Ley_Lavado_Activos.pdf | cited-as-LB |
| 19_Manual_Funcional_Transmision.pdf | not-applicable-this-wave |
| 20_Catalogos_Transmision.pdf | not-applicable-this-wave |
| 25_Catalogos_Transmision_v1.2.pdf | not-applicable-this-wave |
| 26_Manual_Consola_Administrativa.pdf | not-applicable-this-wave |
| 29_Modificacion_Anexos_F07_F14.pdf | not-applicable-this-wave |
| 47_Manual_Funcional_Sistema_Transmision_2026-05-25.pdf | not-applicable-this-wave |
| 48_Manual_Estructuras_Catalogos_Modelos_v1.6.pdf | not-applicable-this-wave |
| 49_Manual_Eventos_Invalidacion_Contingencia_v1.1.pdf | not-applicable-this-wave |
| 14_Ley_Servicios_Internacionales.pdf | superseded-not-cited |
| 73_Codigo_Comercio_UIF_indicelegislativo.pdf | cited-as-LB |
| schemas/ (dir) | superseded-not-cited |

## Note fragments

| Source | Note |
|--------|------|
| 01_Ley_IVA.pdf | D.L. 296-1992 Asamblea consolidation through reform (14) D.L. 71-2015; SOQ-54 second-official-copy confirmation (2026-08-20) — vintage watch rides every LB |
| 02_Reglamento_IVA.pdf | D.E. 83-1992 consolidated; survivors only per R30(a) (mass repeal = D.E. 117-2001 stamp (3); R17-bis); `taxation/15` §2 records no Rgto. survivor governs the declaration interfaces (no LB row). FLIPPED from pending-S2+ by the S9 wave (2026-08-20) |
| 03_Ley_ISR.pdf | historical — authority-order preambles of `taxation/01..06` (shorthand `03_` cites, no LB rows); superseded as current authority by `54_` (reform chain D.L. 762-2014/458-2019/969-2024/293-2025); supplies analysis via EVID ids |
| 04_Reglamento_ISR.pdf | D.E. 101-1992 consolidated, survivor articles only per R17 (mass repeal = D.E. 117-2001) |
| 05_Codigo_Tributario.pdf | `taxation/13` LB rows = the CT 161/162/162-A/162-B IVA retention matrix (verbatim from the CT txt); `taxation/10` LB-018 re-anchors the stale Rgto. Art. 22/23 Ley anchors onto CT 141/161 |
| 06_Guia_Facturacion_Electronica.pdf | non-normative guide; S1 rests on 44_/45_/46_/50_/51_/52_ |
| 07_Codigo_Comercio.pdf | Código de Comercio D.L. 671-1970 current; article text verified vs second official copy `73_` (SOQ-22 resolved-with-residual: both reform lists end at D.L. 641-2008; editorial-artifact residual rides every 07_ LB); row arithmetic: 211 = 07_-sourced LB rows (excluding `02`'s `71_` LB-013 and `04`'s LB-032 pointer), 213 = all 01-09 LB rows |
| 10_Tablas_Retencion_ISR.pdf | historical LB — 1992 colones-era D.E. 75-1991/25-1992, superseded by the `53_` chain via D.E. 95-2015; dated-data rows live in `taxation/isr_brackets.csv` |
| 12_Ley_Zonas_Francas.pdf | D.L. 405-1998 consolidated through D.L. 318-2013, cited as printed (SOQ-30) |
| 13_Ley_Organica_Aduanas.pdf | D. 903 through D.L. 121-2012, as printed; also §2 authority-order preamble in `special-regimes/06` |
| 14_Ley_Servicios_Internacionales.pdf | D.L. 431 2007 print "Reformas: S/R", as printed; superseded as the LSI LB by the W19 T3 re-key to `80_` (consolidated through D.L. 277-2013 — all 38 spe LB source columns re-keyed, 0 survivors; EV14-cited historical provenance retained). FLIPPED cited-as-LB → superseded-not-cited by the W19 fold-in (2026-08-22) |
| 15_Ley_Lavado_Activos.pdf | historical — `commercial-legal/10` §2 preamble + authority-order note only (shorthand `15_` cites, no LB row); derogated wholesale by `71_` Art. 61 (effective 2025-10-17) — historical LB for pre-cutover facts, never current authority (R28; W10 EVID-228..231; R25 title-vs-content: content = D. 498-1998 through reform (6) D.L. 104-2015) |
| 16_Salarios_Minimos_2025.pdf | Decreto 11-2025 tariffs → `payroll/smm_2025.csv`; SMM figure also feeds `e-invoicing/01` OQ-007 threshold config (prose ref) |
| 17_Reglamento_Lavado_Activos.pdf | kept-in-force OPERATIVE reglamento per `71_` Art. 61 + R26 (no post-568-2013 reglamento ever issued): window mechanics, no-tip-off, red-flag catalogs; stale pre-reform thresholds never cited; further prose co-cites in `commercial-legal/10` beyond the 2 pathed rows |
| 17b_Reglamento_Servicios_Internacionales.pdf | Reglamento D. 131-2008, as printed |
| 19_Manual_Funcional_Transmision.pdf | 2025 functional manual; authority-order preamble only (no LB row); content superseded by 45_/46_/47_ |
| 20_Catalogos_Transmision.pdf | 2022 catalog PDF; supersession chain 20_ → 25_ → 50_/51_; catalogs wave cites 50_/51_/25_ |
| 25_Catalogos_Transmision_v1.2.pdf | PDF twin of the cited 25_ XLSX |
| 25_Catalogos_Transmision_v1.2.xlsx | superseded-historical — retained as LB for documents emitted under the v1.2 regime |
| 26_Manual_Consola_Administrativa.pdf | MH emitter-console manual; S1 scope is system-to-system (46_); candidate for onboarding (A11) wave |
| 29_Modificacion_Anexos_F07_F14.pdf | mislabeled source — actual content is the CNR Registro de Comercio F-985 upload manual (extraction `29_F985_CNR_RegComercio`); the intended F-07/F-14 annex-modification resolutions remain absent (SOQ-12); referenced as 29_-file OQ-1 kin in `fiscal-reporting/06` OQ-004 and `07` OQ-001 |
| 30_Calendario_Tributario_2026.pdf | 2026 tax calendar — obligation inventory, due-day visual layer, asueto legend |
| 31_Guia_FOVIAL_COTRANS.pdf | provenance chain: guide = secondary authority citing D.L. 208-2000 Art. 26 as reformed D.L. 597-2001; law text absent (SOQ-39; COTRANS instrument absent, MOQ-04 half-open) |
| 32_NIIF_PYMES_2025.pdf | THE operative framework LB of the S8 wave per R29 — Secciones 1-35 + Apéndices A/B cited by section/párrafo as printed (EVID-275..298), plus §2 authority-order preambles in all eight files; SOQ-46 instrument gap gates eligibility config. FLIPPED from W14 provisional-cited to per-file LB by S8 (2026-08-20) |
| 33_Guia_NIIF_Sostenibilidad_2024-2025.pdf | SECONDARY-ONLY per R29(a) — never sole LB; version/horizon facts (NIIF 18/19 2027-01-01, S1/S2 2024) + the full-NIIF-vs-PYMES contrast set (EVID-299..303). FLIPPED from W14 provisional-cited by S8 (2026-08-20) |
| 34_F07_v14_manual.pdf | manual §-anchored LBs — upload engine §II/§XVI/§XVII, sales §III-IV, purchase §V/§VII, §XIX anulados + SOQ-10 defect ruling, special §XX-§XXIV, income-code apéndice transcription |
| 35_F14_v16_manual.pdf | F-14 v16 annex row model + export contract; income-code catalog vintage Oct-2025 |
| 36_F07_v14_plantilla.xls | plantilla anchors — Anexo 1/2/3/5 sheet columns, annexes 4/6-12 sheets; anulados absent from sheets 1-12 (OQ-003) |
| 37_F14_v16_plantilla.xls | plantilla anchor — "Detalle" sheet annex column template (F-14 export-format OQ-006) |
| 38_F14_v16_form_visual.pdf | v16 seven-tab form architecture; v16 row/casilla zones behind the catalog mapping |
| 39_F07_v14_form_visual.pdf | v14 77-row casilla graph, USD footer; purchase/retention/fuel casilla labels |
| 40_manual_estructuras_catalogo.md | superseded-primary (official PDF = `48_`), cited as historical LB (MOQ-08 flags) |
| 41_manual_eventos_invalidacion.md | superseded-primary (official PDF = `49_`), cited as historical LB |
| 42_Comunicado_Exportaciones_Panama.docx | DUCA-F SV↔Panamá SIECA electronic transmission from 2025-03-03 — dated operational fact |
| 43_DUCA_Instructivo_COMIECO.pdf | DUCA 62-field contract (Res. 409-2018), as printed |
| 47_Manual_Funcional_Sistema_Transmision_2026-05-25.pdf | v2.0 functional manual; S1 LB rests on 45_ §§ + 46_ (raw-text verified); cite in later waves when entrega/consola UX detail is specified |
| 48_Manual_Estructuras_Catalogos_Modelos_v1.6.pdf | pre-v2.0 structures manual; superseded by 45_ Anexo II (+ 40_ historical citations) |
| 49_Manual_Eventos_Invalidacion_Contingencia_v1.1.pdf | PDF original of the 2022 events manual; the .md extraction (41_) is the cited LB |
| 50_Catalogos_Facturacion_Electronica_v1.1_2026-07.pdf | image-based PDF — human-reference fallback, not a parse source |
| 53_Tablas_Retencion_ISR_DE10_2025.pdf | current retention tables (D.E. 10-2025); `taxation/01` LB-028 carries the filing/threshold bits |
| 54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf | current consolidated Ley ISR; `chart-of-accounts/08` cite is a pointer row |
| 55_Reforma_Ley_ISR_DL293_DO_2025-04-30.pdf | Art. 37 table vintage (Tramos I/II exempt band → $6,600), effective 2025-05-08 |
| 56_Reforma_Ley_ISR_DL969_DO_2024-03-14.pdf | Art. 3.4 foreign-source exclusion + pro-rata carve-out and the derogation map (Arts. 14-A/16/27) |
| 57_InterpAut_Art30_DL192_DO_2018-12-12.pdf | Art. 30.1 seasonal-activity assets (cafetalero/cañero) deduct the full annual depreciation quota |
| 58_InterpAut_Art28_DL345_DO_2019-05-31.pdf | Art. 28 mermas/pérdidas/gastos deductibility (interpretación auténtica) |
| 59_F14_v17_form_visual.pdf | v17 Quincena-25 section row 61 casillas 417/418; rows 62-105 renumbered vs v1.6; annex-level representation blocked pending a v17 manual (SOQ-09) |
| 60_DE10_Tablas_Retencion_DO_2025-04-30.pdf | D.O. original print — co-cited for the publication pin + gazette-digit verification of all 53_ printed-digit anomalies (EVID-171, SOQ-03 resolved); 53_ remains the readable citation of convenience |
| 61_F910v9_informe_anual_retenciones.pdf | F-910 v9 annual ISR retentions inform — the CT Art. 123 surface |
| 62_F915v4_informe_distribucion_utilidades.pdf | F-915 v4 distributions/shareholder-list inform — the reporting format behind `taxation/05`'s Art. 74-C duty |
| 63_F930v3_informe_mensual_retIVA.pdf | F-930 v3 monthly retIVA inform homed in `fiscal-reporting/04`; the `fiscal-reporting/07` cite is reference-only (re-check cadence OQ-004). fiscal-reporting/04 LB-009 writes a truncated source path (`63_F930v3.pdf`) — the scanner's stem rule resolves it |
| 64_F935v1_informe_mensual_agentes_extranjeros.pdf | F-935 v1 monthly foreign-agents inform; SOQ-13 anchor OQ |
| 65_F11_v18_form_visual.pdf | F-11 v18 personal-deduction value feeds (SS rows 713/714/716/721/724, AFP voluntary quota 717, deducción fija 722, total 725; no-gravadas 734; dead pago-mínimo print); `fiscal-reporting/07` OQ-006 coupling counterpart (prose ref). Superseded as current print by v19/v20 (per `67_` Anexos 1/8) — not yet acquired (66-70_ OQ-5) |
| 66_Ley_Quincena25_DL499.pdf | Ley Especial Quincena Veinticinco (D.L. 499), folded S6 2026-08-18; also cited in `payroll/01`'s category matrix (FR-004 amendment, Arts. 1/4 — prose ref) |
| 67_Guia_Orientacion_Quincena25.pdf | guía (folded S6 2026-08-18); F-11 v19 (casilla 319) + v20 (Sujetos con Régimen Especial) discovery carried — prints to acquire (≥71) |
| 68_Instrucciones_Carga_Quincena25.pdf | upload-flow LBs (folded S6 2026-08-18) |
| 69_Manual_Usuario_Carga_Quincena25.pdf | annex-CSV 7-column format spec (folded S6 2026-08-18) |
| 70_Plantilla_Quincena25.xls | delimiter LB — the semicolon header line is the `;` operative-delimiter ruling (FR-209/OQ-009) |
| 71_Ley_LavadoActivos_DL426_2025.pdf | current AML law D.L. 426 (effective 2025-10-17) — wholesale replacement of D. 498; C10 rebased on EVID-241..250; R28: Art. 61 keeps `17_`/`72_`, Art. 25 delegates thresholds |
| 72_Instructivo_UIF_Acuerdo380_reform2023.pdf | kept UIF instructivo per `71_` Art. 61 — operative thresholds Art. 51 ($10k cash/$25k other media) + Art. 52 institutional aggregates; R28 authority chain |
| 73_Codigo_Comercio_UIF_indicelegislativo.pdf | verification-grade second CC copy (SOQ-22 resolved-with-residual, EVID-250); §2-preamble co-cites across `commercial-legal/01..09` (+ `04` LB-032 pointer row via the 71-73_ evidence gloss) — no independent LB article-text role |
| 74_Ley_Simplificacion_Aduanera_D529.pdf | D. 529-1999 consolidated through D.L. 23-2012, acquired W13 from uif.gob.sv, as printed (SOQ-30) |
| 75_Reglamento_Codigo_Tributario_DE117.pdf | D.E. 117-2001 CT-application reglamento, EVID-339..358; `taxation/01` LB-027's 75_ mention is a prose co-cite (source column = `54_`). FLIPPED from pending-S2+ by the W17 fold-in (2026-08-20) |
| 79_Ley_Sancionar_Infracciones_Aduaneras_DL551.pdf | LESIA D.L. 551, INDICE LEGISLATIVO print consolidated through reform (5) D.L. 588-2008 — sanction taxonomy + expiry/recursos anchors (spe/06 FR-176..178, spe/07 FR-179..184; EVID-359..370). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf | LSI consolidated through D.L. 277-2013 — supersedes `14_` as the cited LB (W19 T3 re-key; 277-2013 deltas folded, EVID-380..391). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 82_Reforma_Ley_ZF_DL493_DO_2025-12-23.pdf | ZF tail D.L. 493-2025 (extension economics +10y/2-yr-grace + Art. 7 grave-e) derogation; spe/01 FR-190..194, spe/02 FR-195..198, spe/07 FR-199. FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 86_Ley_Fondo_Conservacion_Vial_consolidada.pdf | FOVIAL consolidated statute (D.L. 208-2000 through D.L. 93-2012) — provenance chain now instrument-anchored (was 31_-guide-only). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 87_Ley_FOVIAL_DL208_DO_2000-12-18_pp6-24.pdf | FOVIAL D.O. original print — original Art. 26 carried NO per-gallon value (Executive traslado clause only). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 88_Reforma_Ley_FOVIAL_DL597_DO_2001-11-09_p3.pdf | D.L. 597-2001 reformed Art. 26 — THE $0.20/galón instrument (spe/08 LB-009). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 89_Ley_COTRANS_DL257_DO_2021-12-23_pp5-19.pdf | COTRANS D.L. 257-2021 — $0.10/galón passenger-tariff contribution (identity corrected from the cargo-transport gloss; spe/08 FR-187..189). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 90_Ley_Transitoria_Pagos_ISR_DL598_DO_2020-03-20_pp4-6.pdf | spent COVID payment-deferral law — spe/01 LB-033 historical note only, no FR (EVID-402, W19 T5). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 91_Disposiciones_Transitorias_Aguinaldo_DL229_DO_2021-12-07_pp4-5.pdf | aguinaldo-cap transitory D.L. 229-2021 ($1,100, single-fiscal-year spent) — payroll/04 vintage-limb re-anchor (W19 T5, EVID-398). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 92_Disposiciones_Transitorias_Aguinaldo_DL596_DO_2022-12-07_pp22-24.pdf | aguinaldo-cap transitory D.L. 596-2022 ($1,500, spent) — payroll/04 re-anchor (W19 T5, EVID-399). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 93_Disposiciones_Transitorias_Aguinaldo_DL900_DO_2023-11-30_pp8-10.pdf | aguinaldo-cap transitory D.L. 900-2023 ($1,500, spent) — payroll/04 re-anchor (W19 T5, EVID-400). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 94_Disposiciones_Transitorias_Aguinaldo_DL159_DO_2024-11-27_pp64-66.pdf | aguinaldo-cap transitory D.L. 159-2024 ($1,500, spent; chain verification EVID-403) — payroll/04 re-anchor (W19 T5, EVID-401). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 95_Disposiciones_Inmobiliarios_Altura_DL95_2024_DGII.pdf | inmobiliarios-en-altura incentive D.L. 95-2024 — horizon TEXT-PINNED 15y (spe/01 FR-200 + spe/02 FR-202 D15-kin rows; W19 T4, EVID-392..393). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30_pp3-18.pdf | Agentes Extranjeros D.L. 308-2025 — spe/01 identity row (FR-201 MIGOB RAEX registration only) + Chapter V 30% levy taxation-owned since W20 (taxation/17, SV-TAX-FR-405..416; spe/01 OQ-6 resolved-by-pointer; W19 T4 EVID-397 → W20 fold-in 2026-08-23). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 97_Disposiciones_Biogas_Acelhuate_DL386_2025_DGII.pdf | biogás Acelhuate D.L. 386-2025 — event-bounded project transitory (spe/02 FR-203 + OQ-8/9 working rulings; W19 T4, EVID-394..396). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 98_DACG_DGA_014_2025_Tasa_InspeccionNoIntrusiva.pdf | DACG DGA-014-2025 — $18.00 current-tasa identity anchor (SOQ-34 resolved: value never changed; spe/06 LB-022; W19 T1, EVID-371/372). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 99_DACG_DGA_008_2015_Tasa_InspeccionNoIntrusiva.pdf | DACG DGA-008-2015 — $18.00-since-2014 chain anchor (SOQ-34; spe/06 LB-022; W19 T1). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| 100_Reforma_Ley_Simplificacion_DL124_DO_2015-10-05_pp9-10.pdf | D.L. 124-2015 — the 74_ Art. 12-B exemption set incl. simplified-declaration <$1,000 (spe/06 FR-176/LB-021; W19 T1). FLIPPED from pending-S2+ by the W19 fold-in (2026-08-22) |
| schemas/ (dir) | superseded 2022-era extraction (fe-ccf-v3, contingencia-v3, anulacion-v2 era; no fe-eret/fe-eop) — NOT the current set; the current 15-schema set lives inside `52_Json_Schemas_DTE_Eventos_2026-08-11.zip`, the LB cited directly (`e-invoicing/01` LB-006; `03` LB-010) |

W19 regen (2026-08-22) pending-set rationale — 12 rows stay `pending-S2+`,
none cited in an LB source column this wave: **76_/77_/78_** (CVPCPA NIIF
adoption resolutions + Ley Reguladora de Contaduría — registry-provenance
use only; no requirements wave has needed an LB article row) · **81_**
(Recopilación de Leyes Aduaneras — SOQ-34-hunt identity/provenance use, its
$18 text superseded by the 98_/99_ dispositions) · **83_/84_/85_** (FYDUCA
format set — SOQ-36 field-level residual, gated on the Portal-internal
Comité Aduanero manuals) · **101_/102_/103_/104_/105_** (BCR qualification
set — consumed as CONFIG provenance by taxation/08 FR-219/OQ-2 prose:
`bcr_calificada` = BCR-list membership with per-institution vigencia; the
46-f exemption LBs rest on 01_/02_ statute text, so no LB source column
cites them). Flip rule held: status follows the LB-citation scan only.
