# GT — Source coverage matrix

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | all (cross-topic) |
| Status  | draft (S-GT1 e-invoicing + catalogs wave complete; S-GT2..S-GT7 pending) |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

As-of date 2026-08-19. Scope of this revision: the S-GT1 e-invoicing +
catalogs wave only. Every file in [../sources/](../sources/) (registry:
[../sources/README.md](../sources/README.md) — 82 entries, numbering
01–83 with gap 27; verification-rejected duplicates are not registry rows)
mapped against the requirements waves. Status values:

- **cited** — a requirements file of this wave cites it via a
  `gt/sources/<nn>_…` path (Legal-Basis row, authority-order preamble, or
  direct schema/catalog read); the citing file(s) named.
- **not-applicable** — non-e-invoicing topic owned by a later S-wave;
  marked "pending S-GTn <topic>".
- **pending** — e-invoicing-adjacent but not yet synthesized by any wave
  (none as of this revision).

Citation check = grep for `gt/sources/<nn>_` across
`gt/requirements/e-invoicing/` + `gt/requirements/catalogs/`. File-number
shorthand (e.g. `04` = `e-invoicing/04_mandate-onboarding.md`,
`cat01` = `catalogs/01_governance.md`).

## Matrix (82 registry rows)

| Source | Status | Cited in / note |
|--------|--------|-----------------|
| 01_AD_13-2018_FEL.pdf | cited | `e-invoicing/01` (taxonomy art. 3), `04` (whole legal chain, LB rows), `05` (certificador arts. 14–20) — consolidated edition; original 2018 wordings not in corpus (GOQ-28) |
| 02_AD_26-2019_FEL_reformas.pdf | cited | `e-invoicing/01` (taxonomy reform), `04` (reform map, art. 29-"A" provenance, LB-003) |
| 03_AD_15-2020_FEL.pdf | cited | `e-invoicing/04` (certificador-eligibility reform, capital tiers) |
| 04_SAT-DSI-243-2019_fel_proveedores_estado.pdf | cited | `e-invoicing/04` (first cohort, 4 modalities) |
| 05_SAT-DSI-838-2019_fel_serv_prof.pdf | cited | `e-invoicing/04` (profesionales individuales cohort) |
| 06_SAT-DSI-639-2020_fel_serv_tecnicos.pdf | cited | `e-invoicing/01` (art. 29-"A" content quote), `04` (servicios técnicos cohort, legacy void 31-dic-2020) |
| 07_SAT-DSI-640-2020_fel_emisores_face.pdf | cited | `e-invoicing/04` (FACE emitters cohort; file also carries the 639-2020 duplicate — noted) |
| 08_SAT-DSI-887-2020_fel_baja_cuantia.pdf | cited | `e-invoicing/04` (compra directa/baja cuantía, Q2,500 exception) |
| 09_SAT-DSI-398-2021_fel_proveedores_estado.pdf | cited | `e-invoicing/04` (art. 43 c–f modalities) |
| 10_SAT-DSI-1074-2021_fel_salud.pdf | cited | `e-invoicing/04` (salud y asistencia social cohort) |
| 11_SAT-DSI-1218-2021_fel_contadores.pdf | cited | `e-invoicing/04` (contadores/auditores cohort; carries the 1240-2021 duplicate text — noted) |
| 12_SAT-DSI-1240-2021_fel_regimen_general.pdf | cited | `e-invoicing/04` (THE mass mandate — Régimen General cohort) |
| 13_SAT-DSI-1350-2022_fel_pequenos.pdf | cited | `e-invoicing/04` (pequeños cohort, LB-016) |
| 14_SAT-DSI-400-2023_fel_pequenos_ampliacion.pdf | cited | `e-invoicing/04` (deadline extension → 01-jul-2023) |
| 15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf | cited | `e-invoicing/01`, `02`, `03`, `05`, `06` + `cat01` — the binding Reglas v2.0 (content; cover footer stale) |
| 16_FEL_DocTecnico_Servicios.pdf | cited | `e-invoicing/02` (schema-version drift evidence), `05` (reception/anulación API, mini-RTU), `06` (anulación transport) — provider-boundary document only |
| 17_FEL_casos_de_prueba.zip | cited | `e-invoicing/01` (type/referencia cases), `05` (certification battery), `07` (display cases) — 2018 vintage, superseded by Reglas v2.0 where they collide |
| 18_FEL_guia_requisitos_minimos.pdf | cited | `e-invoicing/01` (20 display types), `07` (whole display guide) |
| 19_FEL_contingencia.pdf | cited | `e-invoicing/06` (contingencia procedure), `07` (print content) |
| 20_FEL_anulacion_manual.pdf | cited | `e-invoicing/06` (portal anulación flow, supersession record) |
| 21_FEL_firma_electronica_manual.pdf | cited | `e-invoicing/04` (habilitación/acreditación onboarding steps) |
| 22_FEL_autorizacion_certificador.pdf | cited | `e-invoicing/05` (certificador authorization regime, SLAs, security) |
| 23_Ley_IVA_27-92.pdf | not-applicable | pending S-GT2 taxation — corpus copy is pre-FEL (≤~2012, no art. 29-"A"); FEL hooks (arts. 29-30, 29-"A") carried transitively via `04` LB-002/003 (as quoted in 01_/02_/06_); current-edition acquisition = GOQ-01 |
| 24_Reglamento_IVA_AG_5-2013.pdf | cited | `e-invoicing/04` LB-018 only (AG 222-2019 layer: arts. 28 bis, 29 ¶4, 36 bis — FEL-only for first-time registrants, 6-month non-FEL cap, onboarding prerequisites); remainder of the reglamento → pending S-GT2 taxation |
| 25_Codigo_Tributario_6-91.pdf | not-applicable | pending S-GT2 taxation — CT arts. 98.5/98"A".2 statutory hooks restated as law text in `04` §1/§2 (no LB path row; corpus copy path uncited this wave) |
| 26_LAT_10-2012.pdf | not-applicable | pending S-GT2 taxation |
| 28_Reglamento_LAT_AG_213-2013.pdf | not-applicable | pending S-GT2 taxation |
| 29_FEL_XSD_cat_github_961133c/ | cited | `e-invoicing/01`, `02`, `05`, `06` + `cat01` (+ sidecars `_INDEX.md`/`_DRIFT.md`) — working XSD/JSON authority (OQ1 ruling), except MediosdePago (R2) |
| 30_FEL_XSD_cat_catdesa/ | cited | `e-invoicing/01`, `02` + `cat01` (+ `_DRIFT.md`) — MediosdePago authority (R2) + drift counterpart |
| 31_certificadores_dte_snapshot_2026-08-18.html | cited | `e-invoicing/05` (roster: 18 authorized; GRUPO CDS/TotalDoc; renewal cluster = GOQ-03 watch) |
| 32_Codigo_Trabajo_D1441.pdf | not-applicable | pending S-GT3 payroll |
| 33_IGSS_Ley_Organica_D295_D11-2004.pdf | not-applicable | pending S-GT3 payroll |
| 34_IGSS_Reglamento_SSO_AG_229-2014.pdf | not-applicable | pending S-GT3 payroll |
| 35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf | not-applicable | pending S-GT3 payroll |
| 36_IGSS_Guia_Direccion_Recaudacion.pdf | not-applicable | pending S-GT3 payroll |
| 37_Salario_Minimo_AG_256-2025.pdf | not-applicable | pending S-GT3 payroll |
| 38_Salario_Minimo_AG_250-2020.pdf | not-applicable | pending S-GT3 payroll |
| 39_Salario_Minimo_Historia.pdf | not-applicable | pending S-GT3 payroll |
| 40_Aguinaldo_D42-92.pdf | not-applicable | pending S-GT3 payroll |
| 41_Bono14_D78-89.pdf | not-applicable | pending S-GT3 payroll |
| 42_IRTRA_Ley_D15-1928.pdf | not-applicable | pending S-GT3 payroll |
| 43_IRTRA_AG_5-2005.pdf | not-applicable | pending S-GT3 payroll |
| 44_IRTRA_AG_6-2005.pdf | not-applicable | pending S-GT3 payroll |
| 45_INTECAP_Ley_Organica.pdf | not-applicable | pending S-GT3 payroll |
| 46_INTECAP_Reglamento_Tasa_Patronal.pdf | not-applicable | pending S-GT3 payroll |
| 47_SAT_Patronos_Retencion_ISR_2025.pdf | not-applicable | pending S-GT3 payroll (+ S-GT2 taxation kin) |
| 48_SAT_Lista_Formularios_2025-10-06.html | not-applicable | pending S-GT4 fiscal-reporting |
| 49_SAT_RetWebIVA_page.html | not-applicable | pending S-GT4 fiscal-reporting (+ S-GT2 kin) — named indirectly as anulación blocker (Retenciones Web) via Reglas §3.17.2 in `e-invoicing/06`; no path citation this wave |
| 50_SAT_RetWebISR_page.html | not-applicable | pending S-GT4 fiscal-reporting (+ S-GT2 kin) |
| 51_SAT_RetWebISR_Manual_v3.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 52_SAT_RetWebIVA_Manual_2024.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 53_SAT_Agentes_RetIVA_2025-10-01.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 54_SAT-0261_form.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 55_SAT_PequenoContribuyente_guia.pdf | not-applicable | pending S-GT2 taxation (+ S-GT4 kin) |
| 56_SAT_Planilla_IVA_FEL_2024.pdf | not-applicable | pending S-GT3 payroll (+ S-GT4 kin) |
| 57_SAT_LET_Pequeno_Manual.pdf | not-applicable | pending S-GT4 fiscal-reporting — LET blocker named via Reglas §3.17.2 in `e-invoicing/06`; no path citation this wave |
| 58_SAT_LET_IVAGeneral_Manual.pdf | not-applicable | pending S-GT4 fiscal-reporting (same indirect LET-blocker note as 57_) |
| 59_SAT_InformeComprasVentas_Manual.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 60_SAT_Habilitacion_Libros.pdf | not-applicable | pending S-GT5 chart-of-accounts (+ S-GT4 kin) |
| 61_SAT_LibroComprasVentas_Pequeno_Proc.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 62_SAT-2390_guia.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 63_SAT-2390_instrucciones_csv.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 64_SAT_Criterio_2-2019.pdf | not-applicable | pending S-GT2 taxation |
| 65_SAT_Criterio_6-2018.pdf | not-applicable | pending S-GT3 payroll (+ S-GT2 kin) |
| 66_Codigo_Comercio_D2-70.pdf | not-applicable | pending S-GT5 chart-of-accounts (+ S-GT6 commercial-legal kin) |
| 67_ZF_Ley_D65-89.pdf | not-applicable | pending S-GT7 special-regimes |
| 68_ZF_Reglamento_AG_242-90.pdf | not-applicable | pending S-GT7 special-regimes |
| 69_Maquila_Ley_D29-89.pdf | not-applicable | pending S-GT7 special-regimes |
| 70_Maquila_Reglamento_AG_533-89.pdf | not-applicable | pending S-GT7 special-regimes |
| 71_Maquila_ReformasReglamento_AG_253-2001.pdf | not-applicable | pending S-GT7 special-regimes |
| 72_ZF_Fondo_AG_296-94.pdf | not-applicable | pending S-GT7 special-regimes |
| 73_RegistroMercantil_Aranceles_2022.pdf | not-applicable | pending S-GT6 commercial-legal |
| 74_Ley_IVA_EScolar_Reformas_D10-2025.pdf | not-applicable | pending S-GT2 taxation (IVA reform delta) |
| 75_AML_D67-2001.pdf | not-applicable | pending S-GT6 commercial-legal |
| 76_AML_D51-2001.pdf | not-applicable | pending S-GT6 commercial-legal |
| 77_AML_LeyIntegral_D15-2026.pdf | not-applicable | pending S-GT6 commercial-legal |
| 78_Fortalecimiento_D20-2006.pdf | not-applicable | pending S-GT2 taxation (+ S-GT4 kin) |
| 79_Fortalecimiento_Reglamento_AG_425-2006.pdf | not-applicable | pending S-GT2 taxation (+ S-GT4 kin) |
| 80_ZF_Reformas_D6-2021.pdf | not-applicable | pending S-GT7 special-regimes (not an e-invoicing mandate — OQ4 resolved) |
| 81_ZOLIC_Reformas_AG65-2022.pdf | not-applicable | pending S-GT7 special-regimes |
| 82_SAT_LET_RegEspeciales_Manual.pdf | not-applicable | pending S-GT4 fiscal-reporting |
| 83_RM_edictos_2026-08-19.pdf | not-applicable | pending S-GT6 commercial-legal |

Numbering note: registry numbers 01–83 with gap 27 (27 never allocated);
82 rows total.

## Rollup

| Status | Rows |
|--------|------|
| cited | 26 (01–22, 24, 29, 30, 31) |
| not-applicable | 56 |
| pending | 0 |
| **Total** | **82** |

Expected cited set for this wave (01–22, 29, 30, 31) verified by grep —
all present. **24_ is cited beyond the expected set** (`e-invoicing/04`
LB-018, AG 222-2019 FEL layer only); its non-FEL content remains owed to
S-GT2.
