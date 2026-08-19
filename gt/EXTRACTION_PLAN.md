# Guatemala — Requirements Extraction Plan

Execution plan per
[shared/docs/requirements-extraction-procedure.md](../shared/docs/requirements-extraction-procedure.md)
(Stage 0). Drafted 2026-08-19 from the completed source-research record
(`gt/SOURCE_RESEARCH.md`, waves W1–W5 + owner DCA batches). **Status:
APPROVED 2026-08-19** — owner review passed as-drafted (wave decomposition +
reading order + drift stance); evidence files are COMMITTED work products
(SV-style gitignore exceptions, owner ruling same day).

## Context

- **82 registered entries** in [sources/README.md](sources/README.md)
  (numbering 01–83, gap 27 unused; next numbering = 84). Two are schema
  dirs (`29_` GitHub pinned 961133c, `30_` cat.desa). Registry carries
  provenance + re-verify flags for every Wayback-sourced file.
- **No hint layer** exists for GT (D-GT4) — the community module find
  (aquih/fel_totaldoc) is a hint ONLY, never LB (W1-C P9). No NotebookLM
  notebook yet; the optional Stage-5 gate needs one built first.
- Research decisions D-GT1..D-GT10 in
  `docs/superpowers/specs/2026-08-18-gt-source-research-design.md`.
- **Binding synthesis constraints (shared canon)**: D15 (as-of doctrine +
  anchor table), D16 (date-driven mechanics; D-GT10 = GT instantiation),
  D17 (`l10n_latam_invoice_document` one-journal/many-document-types
  default; D-GT8 = GT instantiation), D18/D19 +
  `shared/docs/go-live-readiness.md` (GT register seeded). D7–D12 apply
  with their country-scope note (SV nouns illustrative).
- **FEL provider model (D-GT5/D-GT6)**: SAT owns XML standard +
  validates; taxpayers integrate via certificadores. TotalDoc = product
  default provider. Provider docs register under `partner-technical`
  provenance (not yet populated — see gap set).

## Source inventory and decomposition

Grouped like the SV plan; registry rows are authoritative for filenames.

| # | Sources | Governs | Reading units | Target topics |
|---|---------|---------|---------------|---------------|
| 1 | `29_/30_` XSDs + JSON catalogs (2 channels) | FEL document schemas; mensajes/unidades gravables/frases catalogs | schema-by-schema; catalog-by-catalog; **drift diff is a first-class reading unit (OQ3)** | catalogs (shared), feeds all |
| 2 | `15_` Reglas y validaciones **v1.7.10 Feb-2025** (146pp) | THE FEL validation normative: per-DTE rules, fields, frases, validations | per-DTE-type chapters; version-string reconcile (prints "VERSIÓN 2.0" — OQ5); capture Reglas version chain 1.5.1→1.7.10 as dated rows | e-invoicing, catalogs |
| 3 | `16_` Documento Técnico Servicios (27pp) | SAT↔certificador web-service spec (DTE reception/certification/anulación API surface) | whole; field/endpoint inventory | e-invoicing (provider interface) |
| 4 | `01_/02_/03_` AD 13-2018 / 26-2019 / 15-2020 | FEL legal chain (creation + reforms; 03_ cites Ley IVA Art. 29-"A") | whole each, repeal-aware (later reform wins) | e-invoicing, taxation (IVA hooks) |
| 5 | `04_–14_` SAT-DSI incorporations (11 resolutions, 243-2019…400-2023) | Mandate cohorts: proveedores Estado, serv. prof./técnicos, FACE emisores, baja cuantía, salud, contadores, **régimen general (12_ = the mass mandate)**, pequeños | whole each; per-resolution incorporation dates + cohort taxonomy = dated rows | e-invoicing |
| 6 | `18_` guía requisitos mínimos, `19_` contingencia (2018 vintage), `20_` anulación manual, `21_` firma/habilitación manual, `22_` autorización certificador, `17_` casos de prueba (2018), `31_` certificador registry snapshot | FEL operational manuals + test cases + certificador roster | whole each; 17_/19_ read as 2018-vintage (supersession check vs Reglas v1.7.10); 31_ = dated roster data (incl. TotalDoc validity 02/12/2021→02/12/2026, OQ7) | e-invoicing |
| 7 | `23_` Ley IVA 27-92 (**pre-FEL consolidation, ≤~2012 — W-GT2 verified: tail ends D-10-2012/D-4-2012**) + `74_` D-10-2025 (IVA reform: **derogates Art. 8-"A"** — added D-31-2024 art. 13; the "3-'A'" belief was a myth) | IVA core: rate, base, exenciones, crédito fiscal, retenciones hooks | 23_ whole (historical base); 74_ as delta (article-by-article derogation/amendment inventory); **OQ10: post-2018 edition with Art. 29-"A" still missing — pair-read, never cite 23_ as current alone** | taxation |
| 8 | `24_` Reglamento IVA AG 5-2013 | IVA regulation | whole; repeal-aware vs CT + later reforms | taxation |
| 9 | `25_` Código Tributario 6-91 (95pp; **reform tail unverified**) | Tax procedures: registry, document authorization, books, declarations, sanctions, fiscalización | decompose: NIT/registry + document rules → e-invoicing; books/declarations/LET anchors → fiscal-reporting; procedures/sanctions/prescription → taxation | all |
| 10 | `26_` LAT 10-2012 (64pp; consolidation ≤2013) + `28_` Reglamento LAT AG 213-2013 | **ISR current regime** (replaces Dto. 26-92): rentas del trabajo/capital/actividades, tariffs, retenciones ISR | 26_ Libro I (ISR) core → taxation; its IVA-reform articles → taxation unit 7 kin; 28_ whole; post-2013 reform check first (Stage 1) | taxation |
| 11 | `78_` D-20-2006 + `79_` AG 425-2006 | **IVA-retenciones legal basis** (agent designation, rates → OQ13) | whole each | taxation, fiscal-reporting |
| 12 | `47_` patronos retención ISR (2025 SAT digest) | Rentas del trabajo withholding obligations (employer view) | whole; cross-check vs 26_/28_ (digest ≠ law — law wins) | payroll, taxation |
| 13 | `32_` Código de Trabajo D-1441 (188pp; tail unverified) | Labor law: jornada, salario, prestaciones, contrato, terminación | payroll books full; contract/commercial books skim-flag | payroll, commercial-legal (fringe) |
| 14 | `33_` IGSS Ley Orgánica D-295 + D-11-2004 · `34_` SSO reglamento AG 229-2014 (+33-2016, 57-2022 noted) · `35_` Res. 08-SGF/2026 recaudación (47pp) · `36_` guía recaudación | IGSS regime: law-level rates, cuota apparatus (**OQ11: split 12.67/4.83 priors to verify**), employer duties | 33_ law rates; 35_ = the cuota/recaudación core; 34_ OSH (light — registrar por presenting); 36_ mechanics | payroll |
| 15 | `37_` AG 256-2025 (salario 2026) · `38_` AG 250-2020 · `39_` Historia salarios | Salario mínimo dated rows (C1/C2 × agrícola/no-agrícola/maquila, eff 2026-01-01) | as data (tables [sic]-faithful); the trio = the D15/D16 wage-row seed | payroll (feeds all SMM-indexed) |
| 16 | `40_` aguinaldo D-42-92 · `41_` bono 14 D-78-89 (Q250/mes) | Annual statutory bonuses | whole each; tail check 40_ | payroll |
| 17 | `42_` IRTRA D-15-1928 · `43_/44_` AG 5/6-2005 · `45_` INTECAP D-17-72 · `46_` INTECAP reglamento tasa patronal | Patronal institute cuotas (**OQ12: IRTRA brackets**) | whole each (all short) | payroll |
| 18 | `56_` planilla IVA-FEL (art. 72 Dto. 10-2012) | Asalariado IVA-deduction planilla | whole; format = fiscal-reporting interface | payroll, fiscal-reporting |
| 19 | `48_` form inventory snapshot 2025-10-06 | Master form registry (SAT-2237 IVA general, **1371 ISR anual**, 1411 asalariados, 1361 trimestral, 2046/2241 pequeño, 1321/2340/2320 retenciones, boleta 2000) | as data: form↔regime↔deadline map; per-form validities (e.g. "SAT-2237 válido Sep-2013 en adelante") = dated rows | fiscal-reporting |
| 20 | `49_/50_` RetWeb IVA/ISR pages · `51_/52_` RetWeb manuals · `53_` agentes roster 2025-10-01 · `54_` SAT-0261 | Retenciones Web regimes (IVA 15 días hábiles / ISR 10+5), agent roster data, inscripción | 49_/50_ = regime ground truth (D-20-2006/AG 425-2006 basis); 51_/52_ = data model; 53_ = dated roster; 54_ = form layout | fiscal-reporting, taxation |
| 21 | `55_` pequeño contribuyente digest · `57_/58_/82_` LET manuals (pequeño/IVA-general/regímenes especiales) · `59_` informe compras/ventas · `61_` libro compras/ventas pequeño proc | LET electronic books + pequeño regime + informe de compras/ventas layouts | manual-by-manual; LET layout = books interface (anchors CT books unit) | fiscal-reporting |
| 22 | `62_/63_` SAT-2390 guía + CSV instrucciones | Devolución crédito fiscal format | whole | fiscal-reporting |
| 23 | `66_` Código de Comercio D-2-70 (301pp; tail unverified) | Merchant registry (matrícula), accounting/books (THE COA anchor), sociedades, títulos valores, prescription | decompose: Arts. libros/contabilidad → chart-of-accounts; sociedades/registro → commercial-legal; títulos valores/prescripción → commercial-legal | chart-of-accounts, commercial-legal |
| 24 | `60_` habilitación de libros | Book legalization mechanics (CC + tax-law view) | whole; cross-check 23_/25_ | chart-of-accounts, fiscal-reporting |
| 25 | `73_` RM aranceles (2022 snapshot) · `83_` RM edictos (2026-08-19 edition) | Registro Mercantil surfaces: fees, edicto publication flow | 73_ as data; 83_ reference snapshot (channel mechanics) | commercial-legal |
| 26 | `75_` AML D-67-2001 · `76_` D-51-2001 (penal) · `77_` **D-15-2026 Ley Integral** | AML regime chain — 77_ likely wholesale-supersedes 75_ (**OQ14: derogation inventory + reglamento status + Q2,000 cash threshold wording**) | 77_ first (current law), then 75_/76_ as historical/delta; capture cutover 17-jun-2026 as D15 regime-cutover rows | commercial-legal |
| 27 | `67_` ZF D-65-89 · `68_` reglamento AG 242-90 (pre-check) · `69_` maquila D-29-89 · `70_` reglamento AG 533-89 · `71_` reformas AG 253-2001 · `72_` fondo AG 296-94 · `80_` D-6-2021 (ZF reform) · `81_` ZOLIC AG 65-2022 | ZF/maquila/ZOLIC special regimes; chain **D-65-89 → D-19-2016 (NOT in corpus — gap) → D-6-2021** | law-then-reglamento pairs; exemption schedules = **canonical D15 consumers** (per-acuerdo dated rows, never global constants); 81_ = ZOLIC-specific (not the ZF reglamento reform — retired hypothesis) | special-regimes |

## Reading order (evidence waves)

Dependency-aware; each wave's outputs feed the next. Within W-GT1 the
internal order is fixed: schemas/catalogs vocabulary first, then Reglas,
then legal chain, then manuals.

1. **W-GT1 — FEL stack** (units 1–6): `15_` Reglas → `29_/30_` → `16_` →
   `01_–03_` → `04_–14_` → manuals/cases/roster. Establishes the DTE
   vocabulary + validation universe everything else cites. OQ3/OQ5/OQ6
   resolve here.
2. **W-GT2 — taxation core** (units 7–11 + 12's taxation half): IVA
   (23_+74_+24_), CT (25_ decomposed), ISR (26_+28_), retenciones
   (78_+79_). OQ13 resolves here; OQ10/OQ17 hunt continues.
3. **W-GT3 — payroll** (units 12–18): CT laboral → IGSS → salarios →
   bonuses → IRTRA/INTECAP → planilla IVA-FEL. OQ11/OQ12 resolve here.
4. **W-GT4 — fiscal reporting** (units 19–22): form family map → retenciones
   web → LET/informe layouts → SAT-2390. Consumes W-GT1 vocabulary +
   W-GT2 retención rates.
5. **W-GT5 — COA + commercial-legal** (units 23–26): CCom decomposed read,
   books legalization, RM surfaces, AML chain.
6. **W-GT6 — special regimes** (unit 27): needs IVA + ISR context from
   W-GT2.
7. Calendario tributario transcription (owner browser; JSF app) rides any
   wave — it is data capture, not document reading.

Synthesis waves (S-GT1…) follow the SV pattern per topic after its
evidence base completes: prep (master index/merge) → plan doc →
subagent-driven wave → reviews → COVERAGE.

## Topic map (source unit → topic)

| Topic | From |
|-------|------|
| `catalogs/` | 1 (JSON catalogs + XSD-embedded enums; CSV sidecars) |
| `e-invoicing/` | 1(partial), 2–6, 9(partial) |
| `taxation/` | 4(partial IVA hooks), 7–11, 12(partial), 20(partial) |
| `payroll/` | 12(partial), 13–18 |
| `fiscal-reporting/` | 9(partial), 11(partial), 18(partial), 19–22, 24(partial) |
| `chart-of-accounts/` | 23(partial), 24 |
| `commercial-legal/` | 23(partial), 25, 26 |
| `special-regimes/` | 27 |

`requirements/` scaffold exists for 5 topics; `catalogs/`,
`commercial-legal/`, `special-regimes/` dirs are added at their synthesis.

## Known risks

- **Supersession chains (repeal-aware reading mandatory)**:
  - IVA: 23_ (≤~2012 consolidation) is NOT current law text alone — AD
    15-2020 cites Art. 29-"A" (not in 23_); D-10-2025 (74_) derogates
    Art. 3-"A" (which decree added it = OQ17 — **RESOLVED-AS-MYTH W-GT2:
    the article was 8-"A", added by D-31-2024; see log**). Post-2018 consolidated
    edition missing (OQ10).
  - AML: 75_ likely superseded by 77_ (D-15-2026) — derogation inventory
    BEFORE synthesis trusts either; 76_ = penal layer.
  - ZF: D-65-89 → D-19-2016 (**missing from corpus**) → D-6-2021 (80_);
    68_ reglamento copy predates any reform (status = OQ15).
  - FEL vintage: 17_ casos (2018-05) + 19_ contingencia (2018-05) may lag
    Reglas v1.7.10 / current catalogs (OQ9); read as historical, verify
    each rule against 15_/29_.
  - Salarios: 38_ superseded by 37_ (2026); 39_ = historical series (keep —
    it IS the dated-row source).
- **Consolidation tails unverified (Stage 1 must check)**: 25_ CT, 26_ LAT
  (cites only Dto. 14-2013), 32_ CT laboral, 66_ CCom. SV lesson: the
  tail block is the authority list — transcribe it, then hunt gaps.
- **Scans needing OCR (verify page-1 identity first — SAT labels lie)**:
  02/03, 33–35, 38, 64–65, 71, 73, 74, 76–77, 81, 83. DCA gazette prints:
  `--psm 6`; **table pages PSM 4 at 300–400dpi**. Several gazette PDFs
  are DCA prints (01_–14_ set) — same rule.
- **Schema drift (OQ3, material)**: 8/17 shared files differ between
  cat.desa (30_) and GitHub (29_); GitHub = "versión 2" actively
  maintained; Frases 0.6.0 GitHub-only vs 0.1.2 cat.desa. Until
  TotalDoc/SAT answer, treat **GitHub 961133c as working authority with
  the drift recorded** — never silently pick one.
- **Version-string reconcile (OQ5)**: 15_ prints both "v1.7.10 Febrero
  2025" and "VERSIÓN 2.0" — resolve in evidence (content-version vs
  document-revision hypothesis to verify).
- **Rejected myths (never implement)**: "resolución 2-2010" as
  IVA-retenciones basis (real = D-20-2006 + AG 425-2006); SAT-2236 as ISR
  anual form (real = SAT-1371); "Decreto 6-2021" as e-invoicing mandate
  (real = ZF reform, 80_); INTECAP "AG 445-86" (real = D-17-72); IRTRA
  "AG 795" (real = D-15-1928); "instaladores" terminology (real =
  certificadores).
- **Dated-instrument discipline (D-GT10/D16 — binding every wave)**: every
  reading unit captures vigencia data (valid_from/valid_to + provenance)
  for: law reforms, salario AGs, FEL Reglas/catalog/XSD versions, form
  validities (48_ prints them), retention-agent rosters (53_), certificador
  authorizations (31_). Extraction sidecars carry these columns from day
  one. No past-dated transmission; historical = non-transmittable class
  (D16 ¶3).
- **Provider-tier citation limits (D-GT6)**: TotalDoc material cites only
  for provider-interface requirements, marked non-government.
- **OQ7 watch**: Grupo CDS/TotalDoc authorization expires **02/12/2026** —
  re-check the certificador registry at the next milestone (product
  default provider continuity).
- **Wayback-sourced files** carry re-verify flags in the registry — if a
  live official route reappears, re-verify before synthesis cites them.

## Gap set (acquisition candidates ≥84, opportunistic)

1. **Post-2018 consolidated Ley IVA 27-92** incl. Arts. 3-"A"/29-"A"
   (OQ10/OQ17) — accountant ask or DCA Edición Legal hunt. **W-GT2 update:
   Art. 29-"A" provenance = Dto. 4-2019 art. 6 (pinned); the "3-'A'"
   sub-item was a myth — real = Art. 8-"A" (D-31-2024 art. 13, derogated
   D-10-2025).**
1a. **D-31-2024 (Ley Integración Sector Productivo Primario y
   Agropecuario)** — added IVA 8-"A" + LAE changes + the 5 new DTE types
   (FEPE/FARP/FCRP/FPEC/FCPC per Reglas v2.0 changelog) — DCA hunt
   (W-GT2 addition).
2. **D-19-2016 Ley Emergente** (ZF chain middle link) — DCA hunt.
3. Instructivos for SAT-2237/1371/1361/2046/1321 (cat 15812, AJAX-gated).
4. Calendario tributario vencimiento windows (JSF transcription, owner).
5. LET creating resolution (normativa listing, AJAX).
6. D-15-2026 AML reglamento status (OQ14) — watch legal.dca.gob.gt.
7. Provider tier population (TotalDoc FAQ + TotalPOS manual — W1-C P2/P3
   verdicts never landed in `gt/sources/providers/`).
8. Accountant asks pending: consolidated IVA print, calendario windows,
   D-15-2026 reglamento status + AG 75-2006/Q2,000 fate.
9. Optional historical LBs: Reglas chain 1.5.1→1.7.9 PDFs; refreshed
   casos-de-prueba (OQ9).

## Deliverables

1. `gt/requirements/<topic>/` Takumi-template files; FR IDs
   `GT-<TOPIC>-FR-<nnn>` (prefixes: GT-EINV, GT-TAX, GT-PAY, GT-FREP,
   GT-CML, GT-SPR, GT-CAT, GT-COA per the SV contract).
2. `gt/requirements/COVERAGE.md` — every registry row → cited/N-A/pending.
3. `gt/requirements/catalogs/` CSV sidecars from 29_/30_ (+ form-family
   data from 48_), with valid_from/valid_to columns (D15/D16 seed rows).

## Session protocol

Same as SV: per-wave — extract text (`shared/scripts/extract_text.py`,
OCR rules above) → evidence pass to `gt/.extractions/` (git-ignored
scratch; commit exceptions only if owner rules so) → plan-log entry here →
commit. Never leave a session with evidence unmerged. Update
`gt/HANDOVER.md` at every session boundary.

## Extraction log

- 2026-08-19 — Stage 0 plan drafted (this file) from the completed
  research record; awaiting owner review of wave decomposition + reading
  order before W-GT1 begins.
- 2026-08-19 — **Plan APPROVED by owner (as-drafted)**; W-GT1 launched.
  Owner ruling: evidence files commit (gitignore exceptions added,
  SV/HN pattern).
- 2026-08-19 — **W-GT1 COMPLETE** (FEL stack, Stage 1 + Stage 2). Stage 1:
  21 PDFs extracted (12 DCA prints via OCR spa) + 25 casos-de-prueba txts
  unzipped. Stage 2 executed subagent-driven (6 reader agents, controller
  spot-verified quotes + structure); 6 evidence files COMMITTED
  (EVID-001..160, gaps 077-080): `29_30_FEL_XSDs_catalogs` (001-030),
  `01-03_AD_FEL_legal_chain` (031-050), `04-14_SAT-DSI_incorporaciones`
  (051-076), `17-22_31_FEL_manuales_casos_roster` (081-110),
  `15_FEL_Reglas` (111-145), `16_FEL_DocTecnico` (146-160). Key outcomes:
  **Reglas content = v2.0** (changelog 2.0 19/12/2024, vigencia abril 2025;
  "1.7.10" = stale cover footer) — OQ5 resolved; **26-DTE-type taxonomy**
  (11 families) — OQ6 resolved; full drift matrix + GitHub MediosdePago
  defect — OQ3 sharpened; **Dto. 4-2019 art. 6 added IVA Art. 29-"A"**
  (verbatim in 02_) — OQ10 provenance pinned; mandate chronology built
  (régimen general ≤01-jul-2022, pequeño ≤01-jul-2023 per 400-2023);
  **D-GT9 refinement: no taxpayer punto-de-emisión field exists —
  establishment = Emisor/@CodigoEstablecimiento (1-9999) only, Dispositivo
  = SAT-apps-exclusive; Serie/Numero UUID-derived post-certificación**;
  Doc Técnico = v1.2 undated, SAT↔certificador surface only (provider-side
  boundary for the product's TotalDoc integration).   Registry amended
  (01_/07_/11_/15_/16_/18_ notes + instrument-type note). OQ3/OQ5/OQ6/OQ9/
  OQ10 statuses updated in SOURCE_RESEARCH.
- 2026-08-19 — **W-GT2 COMPLETE** (taxation core). Stage 1: 9 PDFs
  extracted (74_ via OCR). 4 evidence files committed (EVID-161..265):
  `23_24_74_IVA` (161-190), `25_Codigo_Tributario` (191-215),
  `26_28_47_LAT_ISR` (216-245), `78_79_Retenciones_IVA` (246-265). Key
  outcomes: **OQ13 RESOLVED both halves** (IVA retentions = % of the IVA:
  65/15/25/15/1.5-of-total + Q2,500 de minimis + 15 días hábiles; ISR:
  5%/7% annual Q300k, capital 10%, dividends 5%, no-residentes 5/3/10/15/25,
  facturas especiales 5%); **OQ17 RESOLVED-AS-MYTH** (D-10-2025 derogates
  IVA Art. **8-"A"** — added by D-31-2024 art. 13, NOT "3-'A'"); **LAT
  consolidation-through-D-46-2022** (≤2013 risk refuted); **CT consolidated
  through D-37-2016, no FEL-era reforms; CT Art. 120 suspension ¶ void per
  CC 680-2013**; Reglamento IVA tail = AG 222-2019 (FEL cluster: new
  registrants FEL-only 1-jul-2021); pequeño threshold Q150,000 (2012 value)
  + 5% definitivo; IVA 12% with 5pp earmarks + fixed-fee used-vehicle
  regime. D-31-2024 added to gap set (new acquisition candidate).
