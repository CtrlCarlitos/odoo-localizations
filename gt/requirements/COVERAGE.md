# GT — Source coverage matrix

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | all (cross-topic) |
| Status  | draft (S-GT1 e-invoicing + catalogs, S-GT2 taxation, S-GT3 payroll, S-GT4 fiscal-reporting and S-GT5 chart-of-accounts/commercial-legal waves complete; S-GT6..S-GT7 pending) |
| Authors | GT synthesis waves S-GT1 + S-GT2 + S-GT3 + S-GT4 + S-GT5 + controller |
| Updated | 2026-08-21 |

As-of date 2026-08-21. Scope of this revision: the S-GT1 e-invoicing +
catalogs wave, the S-GT2 taxation wave, the S-GT3 payroll wave, the S-GT4
fiscal-reporting wave and the S-GT5 chart-of-accounts/commercial-legal wave.
Every file in
[../sources/](../sources/) (registry:
[../sources/README.md](../sources/README.md) — 82 entries, numbering
01–83 with gap 27; verification-rejected duplicates are not registry rows)
mapped against the requirements waves. Status values:

- **cited** — a requirements file of this wave set cites it via a
  `gt/sources/<nn>_…` path (Legal-Basis row, authority-order preamble, or
  direct schema/catalog read); the citing file(s) named.
- **not-applicable** — topic owned by a later S-wave;
  marked "pending S-GTn <topic>".
- **pending** — cited-adjacent but not yet synthesized by any wave
  (none as of this revision).

Citation check = grep for `gt/sources/<nn>_` across
`gt/requirements/e-invoicing/` + `gt/requirements/catalogs/` +
`gt/requirements/taxation/` + `gt/requirements/payroll/` +
`gt/requirements/fiscal-reporting/` + `gt/requirements/chart-of-accounts/` +
`gt/requirements/commercial-legal/`. File-number shorthand (e.g. `04` =
`e-invoicing/04_mandate-onboarding.md`, `tax04` =
`taxation/04_isr-trabajo.md`, `cat01` = `catalogs/01_governance.md`,
`fin01` = `fiscal-reporting/01_form-inventory-channels.md`, `coa01` =
`chart-of-accounts/01_books-anchor.md` (coa01..coa03), `cml01` =
`commercial-legal/01_rm-surfaces.md` (cml01..cml04)).

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
| 23_Ley_IVA_27-92.pdf | cited | `taxation/01` (whole statutory base), `02` (arts. 44-50), `03` (Art. 52/52"A" cross-lock), `05` (factura especial cross-lock), `07` (cutoff register) — historical base ≤ D-10-2012, never cited alone; FEL hooks carried transitively via `e-invoicing/04`; current-edition acquisition = GOQ-01 |
| 24_Reglamento_IVA_AG_5-2013.pdf | cited | `taxation/01` (computation/prorrateo/refund arts.), `02` (Arts. 13/22.5/38/49/55/59), `03` (Chapter IX registry), `07` (AG 222-2019 tail register + GOQ-68 negative finding) + `e-invoicing/04` LB-018 (FEL layer) |
| 25_Codigo_Tributario_6-91.pdf | cited | `taxation/06` (whole procedural backbone: registry, prescription, sanctions, fiscalización), `03` (agent capacity arts. 28/29/41), `07` (authority table) — currency qualifier mandatory on every row (GOQ-53) |
| 26_LAT_10-2012.pdf | cited | `taxation/04` (Libro I arts. 68-82), `05` (arts. 1-107/172-174), `02` (art. 155 guard row), `07` (stamps register through D-46-2022) |
| 28_Reglamento_LAT_AG_213-2013.pdf | cited | `taxation/04` (arts. 67-73 projection rules), `05` (arts. 7-9/19/24-27/74-89), `02` (art. 34 deferral), `07` (AG 167-2014-only tail) |
| 29_FEL_XSD_cat_github_961133c/ | cited | `e-invoicing/01`, `02`, `05`, `06` + `cat01` (+ sidecars `_INDEX.md`/`_DRIFT.md`) — working XSD/JSON authority (OQ1 ruling), except MediosdePago (R2) |
| 30_FEL_XSD_cat_catdesa/ | cited | `e-invoicing/01`, `02` + `cat01` (+ `_DRIFT.md`) — MediosdePago authority (R2) + drift counterpart |
| 31_certificadores_dte_snapshot_2026-08-18.html | cited | `e-invoicing/05` (roster: 18 authorized; GRUPO CDS/TotalDoc; renewal cluster = GOQ-03 watch) |
| 32_Codigo_Trabajo_D1441.pdf | cited | `payroll/01` (salary core, arts. 88-102 kin), `02` (jornada/OT arts. 116-129), `05` (vacaciones/maternidad/menores arts. 130-137, 148-155), `06` (contracts/termination arts. 18-31, 77-87, 259-266), `03` (mechanism arts. 103-115), `10` (edition provenance EVID-266/267/300) — every citation carries the 2024-edition qualifier (R44) |
| 33_IGSS_Ley_Organica_D295_D11-2004.pdf | cited | `payroll/07` (law layer: 25/50/25 structure-only, null-ipso-jure invariant, privileges, inspection; D-11-2004 governance-only R39; GOQ-74) |
| 34_IGSS_Reglamento_SSO_AG_229-2014.pdf | cited | `payroll/10` (SSO duties money-free R40: comité ≥10, plan 3y, exams, suspension; GOQ-76 shuffle flag) |
| 35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf | cited | `payroll/07` (recaudación core: two-share delivery, base floor + NO tope, planilla electrónica lifecycle, single receipt, mora/RD/nota-de-cargo, waivers, ±1% — never a rate, GOQ-04/75) |
| 36_IGSS_Guia_Direccion_Recaudacion.pdf | cited | `payroll/07` (corroboration-only guard row) |
| 37_Salario_Minimo_AG_256-2025.pdf | cited | `payroll/03` (2026 CE1/CE2 × 3 actividades [sic]-faithful six-cell table + CSV rows — GOQ-77/78; incentivo art. 8 e) indivisibility kin in `04`) |
| 38_Salario_Minimo_AG_250-2020.pdf | cited | `payroll/03` (2021 COVID freeze rows + monthly incentivo payment hook; p.3 = AG 243-2020 misattribution R43 in `04`) |
| 39_Salario_Minimo_Historia.pdf | cited | `payroll/03` (1995-2021 series + SD × 365/12 formula, printed figures govern R35/GOQ-82), `04` (p.4 NOTA = the D-37-2001 Q250 quoted-only source — GOQ-09) |
| 40_Aguinaldo_D42-92.pdf | cited | `payroll/04` (BONO 14 engine — filename says Aguinaldo, content = D-42-92: R30 identity correction) |
| 41_Bono14_D78-89.pdf | cited | `payroll/04` (INCENTIVO D-78-89 original law — filename says Bono14, content = incentivo: R30 identity correction; GOQ-83) |
| 42_IRTRA_Ley_D15-1928.pdf | cited | `payroll/08` (D-1528 1962 identity R31 — glyph-decoded layer; art. 12 flat 1% as reformed by D-43-92; GOQ-84/87) |
| 43_IRTRA_AG_5-2005.pdf | cited | `payroll/08` (governance only — Estatutos art. 7 scope; no cuotas; GOQ-86) |
| 44_IRTRA_AG_6-2005.pdf | cited | `payroll/08` (governance only — Junta Reglamento; no cuotas; GOQ-86) |
| 45_INTECAP_Ley_Organica.pdf | cited | `payroll/08` (D-17-72 art. 28 ladder → 1% ceiling, exceptions, rebate, deductibility; GOQ-88) |
| 46_INTECAP_Reglamento_Tasa_Patronal.pdf | cited | `payroll/08` (Reglamento-1980: art. 9º in-force 1%, 20-day deadline, IGSS-planilla base, enforcement ladder; GOQ-89) |
| 47_SAT_Patronos_Retencion_ISR_2025.pdf | cited | `taxation/07` (digest provenance register row) — self-disclaimed digest, never cited as law (26_ > 28_ > 47_); its numeric cross-check (all-match, EVID-243) recorded via EV02c; practice-layer use = GOQ-61 in `taxation/04` (via EV02c, no direct LB) |
| 48_SAT_Lista_Formularios_2025-10-06.html | cited | `taxation/04` (form identities LB-012: 1331/1431/1901/1481/1921/1111 — R46), `05` (1411/1321/1371 — R46) + `fin01` (whole registry: channel model, R46 spine, dated-validity ledger, R53/R58 negatives, GOQ-92..95 — read via the `.extractions` payload dump) |
| 49_SAT_RetWebIVA_page.html | cited | `taxation/03` (secondary-print anchor for the deadline variants, GOQ-01 note) + `fin02` (RetWeb IVA portal: 2340/2320 deadlines, rate-matrix secondary prints, constancia machinery; indirect anulación-blocker name in `e-invoicing/06`) |
| 50_SAT_RetWebISR_page.html | cited | `fin02` (RetWeb ISR portal: 10-dh declare+pay, constancia = factura date, 5-day delivery w/o "hábiles" — R54/GOQ-99; FEL-fed onboarding; SAT-1331 DJ) |
| 51_SAT_RetWebISR_Manual_v3.pdf | cited | `fin02` (ISR manual "noviembre 2024" — GOQ-96: ~30-concepto retention catalog, carga masiva 7/8-col CSV + CTI 03-2023, LAT art. 48/15 anexo fields, state machine) |
| 52_SAT_RetWebIVA_Manual_2024.pdf | cited | `taxation/03` (secondary prints: "art. 54 B" statutory-agent path, card Pago Total/Parcial — GOQ-06/R55/R59) + `fin02` (IVA manual: constancia "Emisión al" dating + consolidation, carga masiva 7-col, line model + Banguat FX, Sector Público 25/5/5) |
| 53_SAT_Agentes_RetIVA_2025-10-01.pdf | cited | `taxation/03` (roster context row — no agent-type column) + `fin02` (roster 8,447 operational surface OF GT-TAX-FR-108: seed-only, OCR-concat verification — GOQ-97) |
| 54_SAT-0261_form.pdf | cited | `taxation/03` (voluntary-inscription anchor, D-20-2006 art. 6) + `fin02` (SAT-0261 field inventory; tri-partite agent provenance) |
| 55_SAT_PequenoContribuyente_guia.pdf | cited | `taxation/02` (secondary prints: fn.1 D-4-2012 attribution [R20 confirmation], art. 48 window, 5% doctrine, Reg. art. 30 legend) + `fin03` (as-of-~2013 dated layer — GOQ-100 banner: obligations, libro spec, 2043/2047/2049 rails, Q.179.00 defect R56) |
| 56_SAT_Planilla_IVA_FEL_2024.pdf | cited | `payroll/09` (Planilla IVA-FEL mechanics: eligibility, January window, four-source feed, last-wins/ANULADAS — procedural manual, never law; GOQ-90/61; statutory values = LAT art. 72 via taxation/04) + `fin01` kin (SAT-1111 app-surface identity R46 — no mechanics re-derivation) |
| 57_SAT_LET_Pequeno_Manual.pdf | cited | `fin04` (LET-PC: combined book, SAT-2046 generation, immutable ventas feed, cierre order, 20-line folios; GOQ-104 provenance) |
| 58_SAT_LET_IVAGeneral_Manual.pdf | cited | `fin04` (LET-General: two books/establecimiento, no form generated, resumen = insumo, FYDUCA/DUCA feeds, vehicle paper rule; R48 RTN-Honduras guard) |
| 59_SAT_InformeComprasVentas_Manual.pdf | cited | `fin04` (informe: art. 57 "D" attestation flow, two FEL-coverage questions, carga masiva 100% gate, PDF constancia, rectificación — GOQ-108) |
| 60_SAT_Habilitacion_Libros.pdf | cited | `coa02` (dual-track model, SAT-7121 habilitación mechanics, art. 29-"A" bridge; undated illustrative orientation ≥30-oct-2019 — GOQ-129 banner) |
| 61_SAT_LibroComprasVentas_Pequeno_Proc.pdf | cited | `fin03` (61_ LET-era layer: both régimens incl. Electrónico, SAT-7121 habilitación → resolución, LET FEL auto-load, SAT-2046 one-click — GOQ-101) |
| 62_SAT-2390_guia.pdf | cited | `fin05` (SAT-2390 flow: CARTERA states, Congelar/RTU gates, claim window, cross-validation gate — GOQ-110/111/112) |
| 63_SAT-2390_instrucciones_csv.pdf | cited | `fin05` (CSV annex spec AUTHORITY: naming, rows 1-2 skipped, compras 16 cols A-P / ventas 11 cols A-K, TEXT cells, NC−/ND+, >Q2,500 NIT+ID from 2023-01 — GOQ-113/114/115; R49 defects verbatim) |
| 64_SAT_Criterio_2-2019.pdf | cited | `taxation/03` (dualidad interpretive layer: EVID-496 + rate-table confirmation) + `fin06` (interpretive confirm-only layer: dualidad holdings, retained-IVA bookkeeping notes, GOQ-116/117 — never the rate source) |
| 65_SAT_Criterio_6-2018.pdf | cited | `taxation/05` (deduction-gating interpretive layer via EV02c/EV04f) + `payroll/04` bono-cap kin consumed indirectly via GT-TAX-FR-169 (no direct path citation) + `fin06` (deducibilidad gates: IGSS-planilla ≥3/≥1, related-party 10%, aguinaldo/bono 100% caps, dietas LAT art. 44; GOQ-121 negative-FR) |
| 66_Codigo_Comercio_D2-70.pdf | cited | `coa01` (arts. 368-384 books/PCGA anchor + dated identity R45), `coa02` (art. 372 autorización; R62 vocabulary), `coa03` (retention LB anchors arts. 376/382-384 + prescription texts), `cml01` (arts. 333-345 RM data model pre-D18-2017 R64), `cml02` (Libros I-II sociedades/lifecycle), `cml03` (Libro III títulos valores + prescription) — consolidated through D-11-2006, GOQ-123 verification banner |
| 67_ZF_Ley_D65-89.pdf | not-applicable | pending S-GT7 special-regimes |
| 68_ZF_Reglamento_AG_242-90.pdf | not-applicable | pending S-GT7 special-regimes |
| 69_Maquila_Ley_D29-89.pdf | not-applicable | pending S-GT7 special-regimes |
| 70_Maquila_Reglamento_AG_533-89.pdf | not-applicable | pending S-GT7 special-regimes |
| 71_Maquila_ReformasReglamento_AG_253-2001.pdf | not-applicable | pending S-GT7 special-regimes |
| 72_ZF_Fondo_AG_296-94.pdf | not-applicable | pending S-GT7 special-regimes |
| 73_RegistroMercantil_Aranceles_2022.pdf | cited | `cml01` (fee catalog dated-2022-label R66) + `coa02` kin (Q0.20/hoja books row) |
| 74_Ley_IVA_EScolar_Reformas_D10-2025.pdf | cited | `taxation/01` (delta register row), `07` (D-10-2025 delta register: deroga 8-"A", LAE ¶, OCR-noise ledger — GOQ-62) |
| 75_AML_D67-2001.pdf | cited | `cml04` (pre-cutover regime rows, operative until 16-sep-2026 — R60) + `coa03` kin (art. 23 5-year retention row in the matrix) |
| 76_AML_D51-2001.pdf | cited | `cml04` (lineage: urgencia window 15-nov→16-dic-2001 only) |
| 77_AML_LeyIntegral_D15-2026.pdf | cited | `cml04` (post-cutover law from 17-sep-2026; cutover spine + thresholds deferred to reglamento GOQ-12) + `cml02` kin (CC-reform art. 113 SMM-fine cutover row) + `coa03` kin (art. 34 ≥5y+10y archive rows) |
| 78_Fortalecimiento_D20-2006.pdf | cited | `taxation/01` (Chapter V reforms — EVID-257), `03` (whole retention matrix, arts. 1-14), `07` (split-vigencia register) + `fin02` kin (RegWeb regime LB via 49_'s own citations — no statutory re-derivation) |
| 79_Fortalecimiento_Reglamento_AG_425-2006.pdf | cited | `taxation/03` (Título II: carné, Sistema art. 4, dualidad art. 9 [GOQ-118 resolved], constancia, lifecycle), `07` (AG 125-2022 stamp register) + `fin02`/`fin06` kin (Sistema-% mechanic + dualidad interpretive layer — consumed via taxation/03 FR ids) |
| 80_ZF_Reformas_D6-2021.pdf | not-applicable | pending S-GT7 special-regimes (not an e-invoicing mandate — OQ4 resolved) |
| 81_ZOLIC_Reformas_AG65-2022.pdf | not-applicable | pending S-GT7 special-regimes |
| 82_SAT_LET_RegEspeciales_Manual.pdf | cited | `fin04` (LET especiales: three regimes' combined book, masked form numbers — GOQ-109, Q3,000,000 agro glossary, THE 4%/5%-within-10-dh tariff rule — GOQ-107) |
| 83_RM_edictos_2026-08-19.pdf | cited | `cml01` (edición 6022 channel anatomy + edicto templates; single-snapshot GOQ-131) |

Numbering note: registry numbers 01–83 with gap 27 (27 never allocated);
82 rows total.

## Rollup

| Status | Rows |
|--------|------|
| cited | 74 (01–26, 28, 29, 30, 31, 32–46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 75, 76, 77, 78, 79, 82, 83) |
| not-applicable | 8 (67, 68, 69, 70, 71, 72, 80, 81 = special-regimes only, pending S-GT7) |
| pending | 0 |
| **Total** | **82** |

Expected cited sets verified by grep. S-GT1: 01–22, 29, 30, 31 (+24_
FEL-layer LB only). S-GT2: 23, 24, 25, 26, 28, 47, 48, 49, 52, 53, 54,
55, 64, 65, 74, 78, 79 (17 rows). S-GT3: 32–46, 56 (16 rows). S-GT4: 48,
49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 61, 62, 63, 64, 65, 82 (17 rows;
+ 78/79 kin via taxation FR ids, no direct new LB). S-GT5: 60, 66, 73, 75,
76, 77, 83 (7 rows). **Secondary-print
discipline:** 49_/52_/
53_/54_/55_ (EV04b/EV04c manuals) and 47_/64_/65_ (digest/criterios) are
cited ONLY as dated-as-of secondary or interpretive anchors — statutory
authority always rests on 23_/24_/25_/26_/28_/78_/79_ (per-file notes
record this; R55 rows stay GOQ-06-open, never frozen). 57_/58_/82_ (LET
manuals) carry GOQ-104 provenance caveats; 62_/63_ carry GOQ-110. S-GT5
additions: 60_ is illustrative orientation only — the force rests in the
cited instruments (CCom/CT/RLIVA/LET, GOQ-129); 73_ fees are
dated-2022-label rows (R66 re-verify); 83_ is a single-édición snapshot
(GOQ-131, never a standing register); 75_/76_/77_ are dated-layer AML —
pre-cutover facts resolve against 75_, never 77_, and vice versa per R60.
