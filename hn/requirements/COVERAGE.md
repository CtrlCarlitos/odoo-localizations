# HN — Source coverage matrix

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | all (cross-topic) |
| Status  | validated (V-HN1 gate 1 — S-HN1/S-HN2/S-HN3/S-HN4 waves; W5 acquisition-reads refresh) |
| Authors | script `hn/scripts/build_coverage.py` (regenerate after every wave) |
| Updated | 2026-08-20 |

Every row of [../sources/README.md](../sources/README.md) (147 registered files, gap 103 reserved-unused) mapped against the four synthesis waves + the W5 acquisition-reads wave (taxation 7 files / e-invoicing 4 / fiscal-reporting 11 / payroll 10 = 32 requirement files; 1099 FRs, 523 LB rows, 574 ACs, 327 OQ rows). Script-checked gates (exit 1 on failure): every FR cites ≥1 LB of its own file; every LB token resolves to a registry row that exists on disk; every registry row is LB-cited or carries an explicit not-applicable annotation; per-topic FR totals match the wave records (taxation 249, e-invoicing 157, fiscal-reporting 363, payroll 330).

Status vocabulary (mirrors SV): **cited-as-LB** — appears in a Legal Basis row of a requirements file (citing file(s) + LB ids listed); **not-applicable-this-wave** — explicit annotation with reason (superseded/historical, in-corpus-unread pending evidence pass, or out of scope for the four topics).

## Matrix (147 source files)

| Source | Status | Cited in / note |
|--------|--------|-----------------|
| 01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf | cited-as-LB | `fiscal-reporting/06_eeff-535-gate.md` (LB-007); `fiscal-reporting/07_isr-annual-102-103.md` (LB-014); `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-001); `fiscal-reporting/10_tp-545-informativas.md` (LB-007); `taxation/01_isr-framework.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-019+LB-020+LB-021+LB-022+LB-024); `taxation/02_isr-deductions.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-011); `taxation/03_isr-rates-gains-minimum.md` (LB-001+LB-006+LB-007); `taxation/04_isr-withholding.md` (LB-001+LB-005+LB-006+LB-007+LB-008+LB-009); `taxation/05_d17-2010-family.md` (LB-001) |
| 02_Ley_ISV_DL24_consolidada_DL59-2022.pdf | cited-as-LB | `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-006); `taxation/06_isv.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-008+LB-009+LB-010+LB-011+LB-012+LB-013+LB-014+LB-015) |
| 03_Codigo_Tributario_D170-2016_act_D180-2020.pdf | cited-as-LB | `e-invoicing/02_cai-ledger-emission-gate.md` (LB-020); `fiscal-reporting/06_eeff-535-gate.md` (LB-008); `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-009); `fiscal-reporting/10_tp-545-informativas.md` (LB-011); `taxation/01_isr-framework.md` (LB-007+LB-008+LB-009+LB-010+LB-011+LB-012+LB-013+LB-014+LB-015+LB-016+LB-017+LB-018); `taxation/04_isr-withholding.md` (LB-015) |
| 04_Decreto_17-2010_Ley_Fortalecimiento.pdf | cited-as-LB | `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-005+LB-007); `fiscal-reporting/09_selectivo-declarations.md` (LB-011); `fiscal-reporting/11_contribuciones-sector.md` (LB-010); `taxation/02_isr-deductions.md` (LB-013); `taxation/03_isr-rates-gains-minimum.md` (LB-004+LB-010+LB-011); `taxation/05_d17-2010-family.md` (LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-013); `taxation/06_isv.md` (LB-007); `taxation/07_special-regimes-exonerations.md` (LB-001+LB-002) |
| 05_Ley_Eficiencia_D113-2011_actualizada.pdf | cited-as-LB | `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-003); `taxation/02_isr-deductions.md` (LB-008); `taxation/03_isr-rates-gains-minimum.md` (LB-008+LB-012); `taxation/04_isr-withholding.md` (LB-013+LB-014); `taxation/05_d17-2010-family.md` (LB-015); `taxation/06_isv.md` (LB-016+LB-017+LB-018); `taxation/07_special-regimes-exonerations.md` (LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009) |
| 06_Decreto_7-2026_G37069.pdf | cited-as-LB | `taxation/07_special-regimes-exonerations.md` (LB-010) |
| 23_Sentencia_inconst_Art206_CT_2023.pdf | cited-as-LB | `taxation/01_isr-framework.md` (LB-023) |
| 89_Decreto_117-2021_interp_Art113_CT.pdf | cited-as-LB | `fiscal-reporting/10_tp-545-informativas.md` (LB-012); `payroll/02_13th-14th-bono.md` (LB-012) — V-HN1: evidence pass EVID-334..336 (10th gloss incident — Art. 2 aguinaldo interp); LB rows added to payroll/02 (LB-012 + FR-087, OQ-007 conflict vs ISR 10.h) and fiscal-reporting/10 (LB-013, OQ-004 resolved). |
| 79_Decreto_59-2020_reforma_ISR.pdf | cited-as-LB | `taxation/02_isr-deductions.md` (LB-009); `taxation/04_isr-withholding.md` (LB-010) |
| 80_Decreto_31-2018_reforma_22A.pdf | cited-as-LB | `taxation/03_isr-rates-gains-minimum.md` (LB-002+LB-003); `taxation/05_d17-2010-family.md` (LB-014+LB-015) |
| 21_Acuerdo_1121-2010_Regl_D17-2010.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-010); `taxation/03_isr-rates-gains-minimum.md` (LB-010); `taxation/04_isr-withholding.md` (LB-011); `taxation/05_d17-2010-family.md` (LB-002+LB-003+LB-004+LB-007+LB-010+LB-011+LB-012+LB-013); `taxation/07_special-regimes-exonerations.md` (LB-002) |
| 22_Decreto_28-2019_interp_Art19_D17-2010.pdf | cited-as-LB | `taxation/04_isr-withholding.md` (LB-012); `taxation/05_d17-2010-family.md` (LB-016) |
| 07_Acuerdo_SAR-01-2026_G37051.pdf | cited-as-LB | `taxation/04_isr-withholding.md` (LB-002) |
| 08_Acuerdo_SAR-07-2025_G36735.pdf | cited-as-LB | `taxation/04_isr-withholding.md` (LB-002) |
| 09_Acuerdo_SAR-07-2024_G36458.pdf | cited-as-LB | `taxation/04_isr-withholding.md` (LB-002) |
| 10_Acuerdo_SAR-014-2023_ajuste_IPC.pdf | cited-as-LB | `taxation/04_isr-withholding.md` (LB-002) |
| 12_Acuerdo_SAR-020-2022_tabla_ISR_2022.pdf | cited-as-LB | `taxation/04_isr-withholding.md` (LB-002) |
| 11_Plantilla_Retencion_Fuente_2026.xlsx | cited-as-LB | `taxation/02_isr-deductions.md` (LB-010); `taxation/04_isr-withholding.md` (LB-003+LB-004) |
| 13_Acuerdo_SAR-619-2024_EEFF_previo_ISR.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-012); `fiscal-reporting/06_eeff-535-gate.md` (LB-001+LB-002+LB-003) |
| 14_Acuerdo_SAR-238-2024_DJIMR.pdf | cited-as-LB | `e-invoicing/02_cai-ledger-emission-gate.md` (LB-020); `fiscal-reporting/01_filing-chassis-due-days.md` (LB-004+LB-008+LB-009); `fiscal-reporting/02_djimr-retention-declarations.md` (LB-001+LB-002+LB-003+LB-004+LB-005); `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-012) |
| 15_Acuerdo_DEI-SG-276-2015_DMC.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-010); `fiscal-reporting/03_dmc-527-purchases.md` (LB-001+LB-002) |
| 16_Acuerdo_CPAT-SG-073-2016_DMC_mod.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-010); `fiscal-reporting/03_dmc-527-purchases.md` (LB-003) |
| 17_Acuerdo_SAR-343-2019_DMC_reforma.pdf | cited-as-LB | `fiscal-reporting/03_dmc-527-purchases.md` (LB-004) |
| 18_Acuerdo_DEI-SG-279-2015_compras_eventuales.pdf | cited-as-LB | `e-invoicing/01_document-types-numbering.md` (LB-013); `fiscal-reporting/03_dmc-527-purchases.md` (LB-006) |
| 19_Acuerdo_SAR-240-2024_ISV_tarjetas_mod.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-009); `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-001+LB-002) |
| 20_Acuerdo_SAR-237-2024_retenciones_mod.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-003+LB-010); `fiscal-reporting/03_dmc-527-purchases.md` (LB-005); `fiscal-reporting/05_isv-201-202.md` (LB-011) |
| 29_Ayuda_ISR_PN_codigo102.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-013) |
| 30_Ayuda_ISR_PJ_activo_net_codigo103.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-008+LB-009+LB-010+LB-013) |
| 31_Ayuda_cedular_alquiler.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-006+LB-007+LB-020) |
| 32_Ayuda_retencion_asalariados_111.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-002+LB-016); `fiscal-reporting/02_djimr-retention-declarations.md` (LB-008+LB-009) |
| 33_Ayuda_ret_serv_honorarios_112.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-010) |
| 34_Ayuda_ret_dividendos_113.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-017); `fiscal-reporting/02_djimr-retention-declarations.md` (LB-011+LB-019) |
| 35_Ayuda_ret_intereses_115.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-012) |
| 36_Ayuda_ret_ISV_sector_publico_116.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-013) |
| 37_Ayuda_ret_anticipo_135.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-014) |
| 38_Ayuda_ret_gc_no_residente_138.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-015); `taxation/03_isr-rates-gains-minimum.md` (LB-009) |
| 39_Ayuda_ret_1pct_D17-2010.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-016) |
| 40_Ayuda_ret_ISV_art8_217.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-017+LB-020) |
| 41_Ayuda_ret_ISV_tarjetas_215.pdf | cited-as-LB | `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-003+LB-007+LB-008+LB-010) |
| 42_Ayuda_ATC_523.pdf | cited-as-LB | `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-004+LB-013) |
| 43_Ayuda_ISV_201.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-009+LB-018); `fiscal-reporting/03_dmc-527-purchases.md` (LB-013); `fiscal-reporting/05_isv-201-202.md` (LB-001+LB-003+LB-007+LB-010+LB-014) |
| 44_Ayuda_simplificado_202.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-012); `fiscal-reporting/05_isv-201-202.md` (LB-002+LB-005+LB-015) |
| 45_Ayuda_DMC.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-002+LB-016+LB-019+LB-021); `fiscal-reporting/03_dmc-527-purchases.md` (LB-007+LB-008+LB-009+LB-010+LB-011); `fiscal-reporting/05_isv-201-202.md` (LB-010) |
| 46_Ayuda_ganancias_capital.pdf | cited-as-LB | `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-002+LB-008+LB-010) |
| 47_Ayuda_GC_ZOLITUR_120.pdf | cited-as-LB | `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-004) |
| 48_Ayuda_tradicion_inmuebles_152.pdf | cited-as-LB | `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-006) |
| 49_Ayuda_revaluacion_154.pdf | cited-as-LB | `fiscal-reporting/08_gc-events-119-120-152-154.md` (LB-007) — V-HN1: LB co-cite added to fiscal-reporting/08 LB-007 (was evidence-anchor-only EV29:EVID-108). |
| 50_Ayuda_selectivo_203.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-011+LB-018); `fiscal-reporting/09_selectivo-declarations.md` (LB-001) |
| 51_Ayuda_cigarrillos_211.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-003) |
| 52_Ayuda_gaseosas.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-004) |
| 53_Ayuda_alcoholes_205.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-005) |
| 54_Ayuda_cerveza_204.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-006) |
| 55_Ayuda_turistico_259.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-011); `fiscal-reporting/09_selectivo-declarations.md` (LB-007) |
| 56_Ayuda_casinos_504.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-005+LB-007+LB-018+LB-021); `fiscal-reporting/11_contribuciones-sector.md` (LB-001+LB-008+LB-009+LB-011) |
| 57_Ayuda_telefonia_502.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-015); `fiscal-reporting/11_contribuciones-sector.md` (LB-002) |
| 58_Ayuda_comidas_503.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-003) |
| 59_Ayuda_cooperativo_509.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-004) |
| 60_Ayuda_cooperativo_506.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-005) |
| 61_Ayuda_sector_social_511.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-006) |
| 62_Ayuda_educativas_107.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-015); `fiscal-reporting/11_contribuciones-sector.md` (LB-007+LB-008+LB-009+LB-011) |
| 63_Ayuda_precios_transf_545.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-012+LB-020); `fiscal-reporting/10_tp-545-informativas.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006) |
| 64_Ayuda_socios_utilidades_541.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-013); `fiscal-reporting/10_tp-545-informativas.md` (LB-006+LB-007+LB-008) |
| 65_Ayuda_alquileres_542.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-014); `fiscal-reporting/10_tp-545-informativas.md` (LB-006+LB-009) |
| 66_Ayuda_municipalidades_543.pdf | cited-as-LB | `fiscal-reporting/10_tp-545-informativas.md` (LB-006+LB-010) |
| 67_Ayuda_EEFF_situacion.pdf | cited-as-LB | `fiscal-reporting/06_eeff-535-gate.md` (LB-004+LB-005+LB-006+LB-009) |
| 68_Generalidades_ISR.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-005+LB-011); `taxation/03_isr-rates-gains-minimum.md` (LB-005) |
| 69_Generalidades_ISV.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-006); `fiscal-reporting/03_dmc-527-purchases.md` (LB-014); `fiscal-reporting/05_isv-201-202.md` (LB-002+LB-003+LB-004+LB-012+LB-016) |
| 70_Generalidades_creditos_ISV.pdf | cited-as-LB | `fiscal-reporting/03_dmc-527-purchases.md` (LB-012); `fiscal-reporting/05_isv-201-202.md` (LB-008+LB-009+LB-013+LB-017) |
| 71_Generalidades_DMR.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-006+LB-019); `fiscal-reporting/02_djimr-retention-declarations.md` (LB-013+LB-018+LB-021); `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-002+LB-005+LB-011) |
| 72_Generalidades_DMC.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-019); `fiscal-reporting/03_dmc-527-purchases.md` (LB-008) |
| 73_Generalidades_simplificado.pdf | cited-as-LB | `fiscal-reporting/05_isv-201-202.md` (LB-005+LB-006+LB-018) |
| 74_Generalidades_vence_30abril.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-011) |
| 75_Escrito_suspension_ISR_PN.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-012) |
| 24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf | cited-as-LB | `e-invoicing/01_document-types-numbering.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-011+LB-012); `e-invoicing/02_cai-ledger-emission-gate.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-012+LB-013+LB-014+LB-016+LB-017+LB-018+LB-019); `e-invoicing/03_document-mechanics.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-012+LB-013+LB-014+LB-016+LB-017); `e-invoicing/04_registration-topologies-medios-see.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-012+LB-013+LB-014+LB-015); `taxation/02_isr-deductions.md` (LB-014) |
| 25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf | cited-as-LB | `e-invoicing/01_document-types-numbering.md` (LB-008+LB-009+LB-010+LB-014+LB-015); `e-invoicing/02_cai-ledger-emission-gate.md` (LB-010) |
| 26_Acuerdo_817-2018_tercera_reforma.pdf | cited-as-LB | `e-invoicing/01_document-types-numbering.md` (LB-016); `e-invoicing/03_document-mechanics.md` (LB-015) |
| 76_Ayuda_inscripcion_facturacion.pdf | cited-as-LB | `e-invoicing/04_registration-topologies-medios-see.md` (LB-016) |
| 77_Ayuda_notif_docs_no_usados.pdf | cited-as-LB | `e-invoicing/02_cai-ledger-emission-gate.md` (LB-015) |
| 78_Ayuda_autorizacion_impresion_2026.pdf | cited-as-LB | `e-invoicing/02_cai-ledger-emission-gate.md` (LB-011) |
| 81_Decreto_48-2024_IHSS_aportaciones.pdf | cited-as-LB | `payroll/03_ihss-cotizaciones.md` (LB-001+LB-002+LB-003+LB-004); `payroll/04_ihss-incapacidad.md` (LB-015) |
| 27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf | cited-as-LB | `payroll/05_rap-fondo.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011); `payroll/08_cesantia-preaviso.md` (LB-013); `taxation/02_isr-deductions.md` (LB-012) |
| 28_Decreto_40-2026_reg_RAP.pdf | cited-as-LB | `payroll/05_rap-fondo.md` (LB-012+LB-013+LB-014+LB-015) |
| 82_SETRASS-109-2024_salario_min_2024-2025.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-018+LB-019) |
| 83_SETRASS-014-2023_salario_min_2023.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-020) |
| 84_SETRASS-411-2023_textil_2023.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-021) |
| 86_Codigo_del_Trabajo_TSC.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-011); `payroll/06_jornada-surcharges.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-012); `payroll/07_vacaciones.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011); `payroll/08_cesantia-preaviso.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-012); `payroll/09_suspension-maternity-special.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-011); `payroll/10_salario-concepts-records.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-012+LB-013+LB-014+LB-015+LB-016+LB-017+LB-018) |
| 85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf | cited-as-LB | `payroll/06_jornada-surcharges.md` (LB-013); `payroll/07_vacaciones.md` (LB-012); `payroll/08_cesantia-preaviso.md` (LB-014); `payroll/09_suspension-maternity-special.md` (LB-010); `payroll/10_salario-concepts-records.md` (LB-019+LB-020) |
| 90_Acuerdo_SETRASS-233-2026_salario_min_2026-2027.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-008+LB-009+LB-010+LB-011+LB-012+LB-013) |
| 91_Tabla_Salario_Minimo_2026-2027.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-014) |
| 92_Tabla_Bono_Educativo_2026.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-010) |
| 87_Ley_IHSS_TSC.pdf | cited-as-LB | `payroll/03_ihss-cotizaciones.md` (LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011+LB-012+LB-013+LB-014); `payroll/04_ihss-incapacidad.md` (LB-012+LB-013+LB-014); `taxation/02_isr-deductions.md` (LB-012) |
| 88_Reglamento_Incapacidad_Temporal_IHSS.pdf | cited-as-LB | `payroll/04_ihss-incapacidad.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007+LB-008+LB-009+LB-010+LB-011) |
| 93_Decreto_31-2019_interp_reforma_D31-2018_22A.pdf | cited-as-LB | `taxation/03_isr-rates-gains-minimum.md` (LB-013) |
| 94_Acuerdo_464-1990_Regl_Art50_LeyISR.pdf | not-applicable-this-wave | HISTORICAL reglamento-chain ancestor (1990 retention values: L10k gate, 5% honorarios, 20-day entero — all superseded). V-HN1b: evidenced EVID-351..352-class chain rows in `93+94+97_chain.evidence.md` (values confirmed; no printed derogation clause; every CR tagged HISTORICAL-NEVER-CURRENT). Explicitly NOT the modern Reglamento Ley ISR ('Acuerdo N°799' — W8/R-H83: identity pinned = G 19,972 13-ene-1970; TEXT still unacquired). |
| 95_Decreto_199-2006_Ley_Adulto_Mayor.pdf | cited-as-LB | `taxation/02_isr-deductions.md` (LB-015) |
| 96_Decreto_45-2025_reforma_Adulto_Mayor.pdf | not-applicable-this-wave | V-HN1b: evidenced EVID-342..344 (services-discount side: Art. 31 utilities tiers 25/30%/35/40%, Arts. 31-A/31-B Fiscalía/visible-info) — verified NOT to touch the Art. 30.14 deduction (OQ-008 resolution leg). Out of the four approved topics' scope (special-regimes/commercial-legal territory); cite there when those waves open. |
| 97_Decreto_194-2002_Ley_Equilibrio_Financiero.pdf | cited-as-LB | `taxation/02_isr-deductions.md` (LB-016) |
| 98_Acuerdo_172-2022_selectivo_IPC.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-008) |
| 99_Acuerdo_014-2023_selectivo.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-009) |
| 100_Acuerdo_218-2024_selectivo_IPC.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-010) |
| 101_Acuerdo_STSS-308-2022_G35892.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-015+LB-016+LB-017) |
| 102_Acuerdo_02-95_Regl_14to_mes.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007) |
| 104_Decreto_103_Ley_Salario_Minimo.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-001+LB-002+LB-003+LB-004+LB-005+LB-006+LB-007); `payroll/02_13th-14th-bono.md` (LB-008+LB-009) |
| 105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-013+LB-014+LB-015+LB-016+LB-017); `payroll/06_jornada-surcharges.md` (LB-014+LB-015+LB-016) — W5: evidence pass EVID-362..372 (R-H74 — the 13th-month statutory home); payroll/02 P2 UNBLOCKED (OQ-001 resolved; FR-052..054 rewritten + FR-088..093); séptimo día layer → payroll/06 (LB-014..016, FR-248/249). |
| 106_Gaceta_29320_D43-97_bono_educativo_Ac154-2000_reglamento_bono.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-007); `payroll/02_13th-14th-bono.md` (LB-008+LB-018+LB-019) — W5: evidence pass EVID-373..379 — TWO extracts: D. 43-97 from G 28,271 (29-may-1997, masthead-confirmed — the '29320' title = the reglamento's 6-nov-2000 gazette, number illegible ≈29,32x); bono reglamento OQ-004 RESOLVED (payroll/02 FR-094..096); SMM Arts. 20/35 gazette originals co-cited in payroll/01 LB-007. |
| 107_Gaceta_31753_Decreto_150-2008.pdf | cited-as-LB | `payroll/08_cesantia-preaviso.md` (LB-007+LB-008) — W5: evidence pass EVID-380..382 — CT Art. 120/120-A + the annual-pact Art. 2 as instrument original (≡ 86_ fn.19, no drift); R-H58 anchors upgraded in payroll/08 LB-007/008 + FR-305; new lineage lead D. 247-89. |
| 108_Acuerdo_345_Regl_Comisiones_Salario_Minimo.pdf | cited-as-LB | `payroll/01_smm-chassis.md` (LB-022) — W5: evidence pass EVID-383..384 — commissions procedure + the fijación +15-day vigencia default (payroll/01 LB-022 + FR-041); Acuerdo 345's own vigencia unpinned (G 25,680 date not printed). |
| 109_Gaceta_36460_Decreto_59-2023_Adulto_Mayor.pdf | cited-as-LB | `taxation/02_isr-deductions.md` (LB-017) |
| 110_Gaceta_28441_Decreto_179-97_reforma_Art1_aguinaldo.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-020) |
| 111_Gaceta_25077_Decreto_178-86_interp_aguinaldo.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-021) |
| 112_Gaceta_25155_Decreto_2-87_interp_aguinaldo.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-022) |
| 113_Gaceta_23848_Decreto_112-1982_aguinaldo_original.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-023) |
| 114_Gaceta_1995-01-07_Decreto_135-94_Compensacion_Social.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-024) |
| 115_Gaceta_1982-08-02_Decreto_58_Selectivos_Consumo.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-002) |
| 116_Gaceta_1998-05-20_Decreto_131-98_tasas.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-012) |
| 117_Gaceta_1993-08-14_Decreto_110-93_Ley_Simplificacion_Tributaria.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-022) |
| 118_Gaceta_27941_Decreto_54-96_reformas_tributarias.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-015) |
| 119_Congreso_Inventarios_de_Leyes.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-025) |
| 120_Gaceta_33222_DL107-2013_Ley_RAP.pdf | cited-as-LB | `payroll/05_rap-fondo.md` (LB-016) |
| 121_Gaceta_30059_Decreto_51-2003_Ley_Equidad_Tributaria.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-016) |
| 122_Gaceta_28jun2003_Acuerdo_0948-2003_Regl_Ley_Equidad_Tributaria.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-017) |
| 123_Gaceta_30437_Decreto_52-2004_interp_Art49_51-2003.pdf | cited-as-LB | `fiscal-reporting/07_isr-annual-102-103.md` (LB-017) |
| 124_Gaceta_28847_Decreto_314-98_Ley_Incentivos_Turismo.pdf | cited-as-LB | `taxation/07_special-regimes-exonerations.md` (LB-011) |
| 125_Gaceta_31168_Decreto_135-2006_Adicion_Art5_314-98.pdf | cited-as-LB | `taxation/07_special-regimes-exonerations.md` (LB-011) |
| 126_Gaceta_34419_Decreto_68-2017_Ley_Fomento_Turismo.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-013); `taxation/07_special-regimes-exonerations.md` (LB-011) |
| 127_Acuerdo_005-2017_G34282_Regl_produccion_consumo.pdf | cited-as-LB | `fiscal-reporting/09_selectivo-declarations.md` (LB-014) |
| 128_Gaceta_9jul1993_Decreto_99-93.pdf | cited-as-LB | `fiscal-reporting/02_djimr-retention-declarations.md` (LB-019) |
| 129_Gaceta_27655_May1995_Decreto_74-95_interp_Art34_135-94.pdf | cited-as-LB | `payroll/02_13th-14th-bono.md` (LB-026) |
| 130_Gaceta_33316_Decreto_278-2013_Ley_Ordenamiento_Finanzas_Publicas.pdf | cited-as-LB | `fiscal-reporting/04_otcd-tarjetas-215-523.md` (LB-009); `fiscal-reporting/07_isr-annual-102-103.md` (LB-018); `taxation/03_isr-rates-gains-minimum.md` (LB-019); `taxation/06_isv.md` (LB-019); `taxation/07_special-regimes-exonerations.md` (LB-012) |
| 131_Gaceta_33484_Acuerdo_462-2014_Regl_Ley_Ordenamiento.pdf | cited-as-LB | `taxation/07_special-regimes-exonerations.md` (LB-012) |
| 132_Gaceta_33617_Decreto_74-2014_interp_Art5_278-2013.pdf | cited-as-LB | `taxation/02_isr-deductions.md` (LB-018) |
| 133_Acuerdo_SAR-236-2024_Oficina_Virtual.pdf | cited-as-LB | `fiscal-reporting/01_filing-chassis-due-days.md` (LB-001) |
| 134_Acuerdo_SAR-256-2024_fecha_aplicacion_236-240.pdf | cited-as-LB | `fiscal-reporting/03_dmc-527-purchases.md` (LB-008) |
| 135_Decreto_105-2011_LSP_texto_actualizado.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-012) |
| 136_Gaceta_32730_Acuerdo_1775-2011_Regl_LSP.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-012) |
| 137_Gaceta_34881_Decreto_131-2018_Contribucion_Social_Sector_Social.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-012) |
| 138_Gaceta_33717_Decreto_53-2015_Cooperativas_exoneracion.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-012) |
| 139_Gaceta_35406_Decreto_128-2020_interp_Art3_53-2015.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-012) |
| 140_Gaceta_32691_Decreto_232-2011_Precios_Transferencia.pdf | cited-as-LB | `fiscal-reporting/10_tp-545-informativas.md` (LB-013) |
| 141_Gaceta_33837_Acuerdo_027-2015_Regl_Precios_Transferencia.pdf | cited-as-LB | `fiscal-reporting/10_tp-545-informativas.md` (LB-013) |
| 142_Decreto_62-2019_interp_Art10_232-2011.pdf | cited-as-LB | `fiscal-reporting/10_tp-545-informativas.md` (LB-013) |
| 143_Gaceta_34486_Acuerdo_618-A-2017_Regl_Ley_Fomento_Turismo.pdf | cited-as-LB | `taxation/07_special-regimes-exonerations.md` (LB-012) |
| 144_Acuerdo_SAR-383-2024_codigos_501_524.pdf | cited-as-LB | `fiscal-reporting/11_contribuciones-sector.md` (LB-012) |
| 145_Acuerdo_003-JD-2005_Regl_Gral_Ley_IHSS_ult_version.pdf | cited-as-LB | `payroll/03_ihss-cotizaciones.md` (LB-015+LB-016+LB-017+LB-018) |
| 146_Regl_Aplicacion_Ley_Seguro_Social_Decreto_193-1971.pdf | cited-as-LB | `payroll/03_ihss-cotizaciones.md` (LB-019) |
| 147_Regl_Gral_Ley_IHSS_transparencia_scan.pdf | cited-as-LB | `payroll/03_ihss-cotizaciones.md` (LB-019) |
| 148_Gaceta_33879_10nov2015_IHSS_RAP.pdf | cited-as-LB | `payroll/03_ihss-cotizaciones.md` (LB-019) |

## Rollup

| Status | Rows |
|--------|------|
| cited-as-LB | 145 |
| not-applicable-this-wave | 2 |
| **Total** | **147** |

## V-HN1 gate-1 findings (2026-08-20, fixed in this wave)

1. **`89_` D. 117-2021 had NO evidence pass** despite being in corpus since
   2026-08-18 — the registry gloss sold it as the CT-Art.-113.1 interp only.
   Full read (EVID-334..336) surfaced **Art. 2 = authentic interpretation of
   D. 112-82 Art. 3** (séptimo día + 13th month = salario ONLY for labor
   prestaciones; aguinaldo exempt from ALL taxes/cotizaciones/deductions
   except alimony). Encoded: payroll/02 LB-012 + **HN-PAYR-FR-087**
   (reserved-range addition) + OQ-007 (CONFLICT vs ISR Art. 10.h 10-SMM caps —
   ISR rows stand, immunity row conflict-flagged); IHSS-base statutory lean
   recorded in payroll/03 (flag stays); RAP-base lean in payroll/05 OQ-001;
   TP-scope narrowing in fiscal-reporting/10 LB-013 + FR-326(c) with
   **OQ-004 RESOLVED** (the Ayuda's "Decreto No 117-2021" = `89_`, the
   carrier of CT 113.1's quoted clause). 10th title-vs-content incident
   (registry gloss understated content).
2. **`95_`/`96_` (D. 199-2006 + D. 45-2025, Adulto Mayor) were in corpus
   BEFORE S-HN1** yet taxation/02 claimed the statute "unacquired" —
   corrected to IN-CORP-UNREAD (no evidence pass); FR-067 senior-tier row
   stays activation-blocked pending that read (OQ-008). HANDOVER acquisition
   queue line amended accordingly.
3. **`49_` (Ayuda revaluación 154) was evidence-anchor-cited but LB-uncited**
   — EV29:EVID-108 carried it while LB-007 named only `04_`; co-cite added.
4. `93_`/`94_`/`97_` annotated not-applicable-this-wave (interpretive FY2017
   transition / historical 1990 ancestor / superseded-as-cited original) —
   no FR rests on them; read-on-demand discipline documented above.

Gate 2 (NotebookLM): no notebook exists for HN — optional gate skipped per
procedure ("where a notebook exists"). Gate 3 (adversarial review): dispatched
per topic at this wave; findings adjudicated in EXTRACTION_PLAN wave log.

## W5 refresh (2026-08-20, acquisition-reads wave)

The four V-HN1b acquisitions (105_-108_) given full evidence passes
(EVID-362..384) and flipped from not-applicable to cited-as-LB: **105_ D.
112-1982 = the 13th-month statutory home (R-H74) — payroll/02 P2 UNBLOCKED**
(OQ-001 resolved; the "D. 135-94 Ley del Aguinaldo + Acuerdo 201-96" framing
was a conflation, R-H75); the D. 112 séptimo-día chapter → payroll/06
(FR-248/249 statutory valuation/deemed-inclusion/forfeiture); **106_ = TWO
gazette extracts** (D. 43-97 G 28,271 29-may-1997 + Reglamento STSS-154-2000,
gazette 6-nov-2000) — bono reglamento OQ-004 RESOLVED (FR-094..096); 107_
D. 150-2008 original ≡ 86_ fn.19 (R-H58 anchors upgraded; D. 247-89 lineage
lead); 108_ Acuerdo 345 commissions procedure + fijación +15-day default
(payroll/01 FR-041). Payroll FR total 314 → 326 (+9 payroll/02, +2 payroll/06,
+1 payroll/01).

## W7 refresh (2026-08-21, residual-chain decode wave)

119_ (congreso "Inventarios de Leyes" — official thematic law inventory,
text-native) registered + cited as LB (payroll/02 LB-025). R-H81: the 102_
OQ-2 "conflict" decodes as TWO 1995 decrees — D. 74-95 = the Art.-34 interp
(G 27,655 18-may-1995; the W4 footnote read "54-95" was an OCR misread,
dual-dpi-fixed in EVID-238/LB-002) and D. 54-95 = the jubilados/pensionados
extension (G 27,639 28-abr-1995; the book's "28,639" = digit-swap,
monotonicity-arbitrated) → payroll/02 FR-057 re-attributed + FR-097 dated
beneficiary row + OQ-002 RESOLVED. R-H82: D. 36-90 = G 26,131 11-MAY-1990
(the inventory's "11-abril" = its own slip — payroll/06 LB-014/FR-248 rows)
and D. 247-89 = G 26,028 6-ene-1990 (payroll/08 LB-007 lineage; text remains
the live residual). Payroll FR total 326 → 327 (+FR-097); LBs +1; ACs +1.
