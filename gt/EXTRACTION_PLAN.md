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
| 16 | `40_` bono 14 D-42-92 (**corrected W-GT3; registry title said "aguinaldo"**) · `41_` incentivo D-78-89 (**corrected; old hourly-floor law — Q250/mes lives in D-37-2001, not in corpus**) | Annual statutory bonuses (**December aguinaldo law D-76-78 = acquisition candidate**) | whole each; tail check 40_ | payroll |
| 17 | `42_` IRTRA D-15-1928 · `43_/44_` AG 5/6-2005 · `45_` INTECAP D-17-72 · `46_` INTECAP reglamento tasa patronal | Patronal institute cuotas (**OQ12: IRTRA brackets**) | whole each (all short) | payroll |
| 18 | `56_` planilla IVA-FEL (art. 72 Dto. 10-2012) | Asalariado IVA-deduction planilla | whole; format = fiscal-reporting interface | payroll, fiscal-reporting |
| 19 | `48_` form inventory snapshot 2025-10-06 | Master form registry (SAT-2237 IVA general, **1411 ISR anual lucrativas, 1431 asalariados anual, 1371 ISR no-residentes, 1331 ISR retenciones** — corrected W-GT4, 1361 trimestral, 2046/2241 pequeño, 2340/2320 retenciones IVA, boleta 2000) | as data: form↔regime↔deadline map; per-form validities (e.g. "SAT-2237 válido Sep-2013 en adelante") = dated rows | fiscal-reporting |
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
  - AML: ~~75_ likely superseded by 77_ (D-15-2026) — derogation inventory
    BEFORE synthesis trusts either; 76_ = penal layer.~~ **RESOLVED W-GT5:
    art. 126 derogates D-67-2001 + D-58-2005 wholesale, vigencia
    17-sep-2026; reglamento ≈17-mar-2027 defers all thresholds; no Q
    threshold in law text.**
  - ZF: D-65-89 → D-19-2016 (**missing from corpus — gap; W-GT6 sharpened:
    the blocking acquisition for post-2016 ISR-window modeling**) →
    D-6-2021 (80_); ~~68_ reglamento copy predates any reform (status =
    OQ15)~~ **RESOLVED W-GT6: AG 65-2022 (81_) reformed AG 242-90 (arts.
    1-24, e-provisions 14-sep-2022); 68_ = inconsistent consolidation**.
  - FEL vintage: 17_ casos (2018-05) + 19_ contingencia (2018-05) may lag
    Reglas v1.7.10 / current catalogs (OQ9); read as historical, verify
    each rule against 15_/29_.
  - Salarios: 38_ superseded by 37_ (2026); 39_ = historical series (keep —
    it IS the dated-row source).
- **Consolidation tails unverified (Stage 1 must check)**: ~~25_ CT, 26_ LAT
  (cites only Dto. 14-2013), 32_ CT laboral, 66_ CCom~~ — **W-GT2/W-GT3
  resolved 25_/26_/32_; W-GT5 resolved 66_ (last inline reform D-11-2006;
  old D-2946 Libro III appended, still vigente)**. SV lesson: the tail
  block is the authority list — transcribe it, then hunt gaps.
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
  IVA-retenciones basis (real = D-20-2006 + AG 425-2006); ~~SAT-2236 as ISR
  anual form (real = SAT-1371)~~ **CORRECTED W-GT4 (48_ row-level read):
  ISR anual lucrativas = SAT-1411, asalariados anual = SAT-1431; SAT-1371 =
  ISR no-residentes pago directo mensual; ISR retenciones = SAT-1331 (1321 =
  ISR capital mensual) — the earlier "real = SAT-1371" lineage was itself a
  table misread**; "Decreto 6-2021" as e-invoicing mandate (real = ZF
  reform, 80_); INTECAP "AG 445-86" (real = D-17-72); IRTRA "AG 795" (real
  = D-15-1928); "instaladores" terminology (real = certificadores).
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
   **W-GT6: blocking for post-2016 ZF/maquila ISR-window modeling; also
   tag-only leads AG 3-2017 (maquila reglamento) + D-38-04 (maquila art.
   12 bis creator) + maquila pre-2016 art. 15 text.**
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
  + 5% definitivo;   IVA 12% with 5pp earmarks + fixed-fee used-vehicle
  regime. D-31-2024 added to gap set (new acquisition candidate).
- 2026-08-19 — **W-GT3 COMPLETE** (payroll). Stage 1: 16 PDFs extracted
  (5 via OCR). 4 evidence files committed (EVID-266..370):
  `32_Codigo_Trabajo` (266-300), `33-36_IGSS` (301-325),
  `37-41_Salarios_Bonos` (331-350), `42-46_56_IRTRA_INTECAP_Planilla`
  (351-370). Key outcomes: **registry corrections** — 40_ = **bono 14**
  D-42-92 (July, 100% June-average; title said "aguinaldo"), 41_ = old
  **incentivo** D-78-89 (names were swapped), **December aguinaldo law
  D-76-78 = MISSING (acquisition candidate)**, Q250/mes incentivo =
  D-37-2001 (missing); **42_ IRTRA = Decreto 1528 (1962)**, not "15 de
  1928"; **OQ12 DISPROVEN** (flat 1% on planillas post-D-43-92, no
  brackets); **OQ11 SHARPENED still-open** (no rates in corpus — JD
  Reglamento de Recaudación = acquisition candidate; no tope máximo; base
  floor = salario mínimo); **37_ rate corrections** (CE2 maquila =
  Q3,221.10; CE2 no-agrícola internal [sic] 3,416.90-digits vs
  3,816.90-words); CT: jornada 8/48-45, OT ≥+50%, vacaciones 15 días
  hábiles + 150-day rule, indemnización 1 mes/año uncapped (6-mo base,
  IGSS offsets), **no auxilio de cesantía exists** (SV-folk-model
  rejected), maternity 84d @100%, no aguinaldo/bono in CT; INTECAP 1%
  (law 0.50-1.00 ladder; vigente 1%) first-20-días on IGSS planillas;
  planilla IVA-FEL = Jan 10-días-hábiles, SAT-1111, last-wins, FEL+DUCA
  feed.
- 2026-08-19 — **W-GT4 COMPLETE** (fiscal reporting, units 19-22 +
  64_/65_ criterios). Stage 1: 3 HTML snapshots dumped to text (48_ page
  body + 4 form tables recovered from the snapshot's embedded JS payload —
  FormulariosVigentes/VigentesAnexo/NoVigentes/NoVigentesAnexo), 12 digital
  PDFs extracted, 2 criterios OCR'd (page-1 identities verified: 2-2019,
  6-2018). Stage 2 executed subagent-driven (6 reader agents, controller
  spot-verified 20+ load-bearing quotes by grep — all passed). 6 evidence
  files COMMITTED (EVID-371..500, gaps 418-430/476-480):
  `48_Formularios` (371-385), `49-54_RetWeb_agentes` (386-417),
  `55_61_Pequeno_libro` (431-450), `57-59_82_LET_informe` (451-475),
  `62-63_SAT-2390` (481-490), `64-65_Criterios` (491-500). Key outcomes:
  **FORM-IDENTITY CORRECTIONS (material)** — ISR anual lucrativas =
  **SAT-1411**, asalariados anual = **SAT-1431**, SAT-1371 = ISR
  no-residentes pago directo mensual, ISR retenciones = **SAT-1331**
  (1321 = ISR capital mensual); 18 dated-validity strings + NoVigentes
  table = valid_from/to seed; channel model: all tax declarations
  Declaraguate-only, Anexo forms generated in SAT apps (5th filing
  surface); SAT-2390 ABSENT from 48_ (devolución CF family = 2124 +
  2053/2062/2073; electronic dev.CF forms live outside the tables — OQ).
  **RetWeb**: SAT-2320 agro = 10 días hábiles (vs 2340 15); 51_ p.9 full
  ISR concept catalog (~30 conceptos with rate/base formulas); 52_
  "art. 54 B" D-27-92 full-accounting agent path; **5% pequeño/agro
  retention rates = OQ18** (reconcile vs W-GT2 matrix); 53_ roster as-of
  2025-10-01 ≈ 8.4-8.5k agents (columns NIT/name/fecha inicio only — no
  agent-type column); SAT-0261 = voluntary inscription, D-20-2006 art. 6.
  **Pequeño/libro**: Q150,000 threshold attributed by 55_ to **D-4-2012
  arts. 12-13 (reforming LIVA arts. 45-46, vigor 25-Feb-2012)** — tension
  vs W-GT2's LAT attribution (OQ); 55_ is an undated ~2013 body still live
  at the 2024 capture (2043/2047 forms era; 61_ = 2046/LET era); LIVA
  art. 48 "mes calendario siguiente" deadline; exit rule LIVA art. 50;
  Q2,500 op floor NOT printed in either (lives in law text W-GT2 — xref).
  **LET/informe**: PC+especiales = ONE combined book, general = TWO
  per-establecimiento books (no form generated — "insumo" only); FEL
  ventas immutable feed; general adds FYDUCA/DUCA + vehicle-paper path;
  **only deadline printed anywhere: electrónicos 4% if declared within
  first 10 días hábiles else 5% (82_ glossary)**; 59_ informe = art. 57
  "D" D27-92 attestation flow, carga masiva 100%-success gate;
  **record-level layouts are ALL images (no text layer) — gap, not
  guessed**; no LET-creating resolution printed anywhere (hunting map at
  EVID-474). **SAT-2390**: 4-year claim window, strictly quarterly/
  semiannual; SAT cross-validates Libro CSV totals vs declared crédito/
  débito (rejection on mismatch); full CSV spec captured (compras 16 cols,
  ventas 11 cols, `SAT_MESAÑO_{COMPRAS,VENTAS}.csv` naming, TEXT cells,
  dd/MM/yyyy, NC negative/ND positive); >Q2,500 NIT+ID mandatory from
  enero-2023 (dated row); "FCE" [sic] for FACE; 63_ prints no date in text
  layer. **Criterios**: 2-2019 dualidad = retain under EACH quality at
  statutory rates, % determined by SAT's Sistema de Retenciones (AG
  425-2006 art. 4), rate table CONFIRMS W-GT2 matrix; 6-2018 = sueldos
  deductible only if IGSS planilla when obligatory (≥3 workers; transporte
  ≥1); aguinaldo+bono14 cap = 100% one monthly salary each, excess only
  via pacto colectivo homologado; dietas to pequeños need definitive ISR
  retention; 64_ OCR pages 4/5/8 blank + "20-2008" [sic] for 20-2006;
  CT art. 91 vs 94 numbering divergence between criterios. Registry
  amended (48_ form-identity correction). OQ18 added to SOURCE_RESEARCH;
  ~45 per-file OQs live in the 6 evidence files.
- 2026-08-19 — **W-GT5 COMPLETE** (COA + commercial-legal, units 23-26).
  Stage 1: 2 digital PDFs + OCR batch (73_/75_ auto-detected; **76_/77_
  needed forced OCR** — footer-text layers defeated the scan heuristic,
  recovered at ~9k chars/page each). Stage 2 subagent-driven (4 reader
  agents; **the 66_-sociedades agent returned empty twice — the file WAS
  written on retry**; controller spot-verified 15+ quotes). 4 evidence
  files COMMITTED (EVID-501..645, gaps 523-535/570-585/606-610):
  `66_CCom_libros_contabilidad` (501-522),
  `66_CCom_sociedades_comercial` (536-569), `60_73_83_RM` (586-605),
  `75-77_AML` (611-645). Key outcomes: **CCom books anchor** — partida
  doble + PCGA mandatory (art. 368, texto D-40-99); FOUR RM-authorized
  books (Inventarios; De primera entrada o diario; Mayor o centralizador;
  De Estados Financieros — **no copiador de correspondencia** in the
  current text); español + moneda nacional; no blanks/raspaduras; balance
  signed ≥1×/year; books kept until full liquidation, documents ≥5 años;
  **no plan de cuentas/catálogo anywhere in CCom — the chart itself is
  PCGA-governed**; no electronic-books provisions (only "mecanizados…
  cualquier otro sistema"); "habilitación" is SAT/CT vocabulary — CCom
  says RM "autorización" (art. 372). **Consolidation tail VERIFIED: last
  inline reform = D-11-2006 (DCA 30-05-2006); pp.215-301 = old D-2946
  maritime Libro III appendix, still vigente**. **60_ dual-track
  habilitación**: CC books need RM authorization AND SAT habilitación
  (SAT-7121, any office / Agencia Virtual); tax books SAT-only; IVA art.
  29-"A" (D-4-2019 art. 6, 30-oct-2019 — **third corpus confirmation of
  the provenance**) = REF/FEL electronic system subsuming the 5 book
  categories. **RM surfaces**: arancel Q0.20/hoja books, edicto Q30 +
  Q200/Q100 publicaciones, disolución Q300 — **variable inscripción
  scale NOT printed**; 83_ = D-18-2017 art. 12 displaced print
  publications to RM's electronic portal. **AML chain RESOLVED (OQ14)**:
  D-15-2026 art. 126 derogates D-67-2001 + **D-58-2005 (FT-financing law,
  previously unmapped in the chain)** wholesale; reglamento (art. 127) due
  ≈17-mar-2027 — all operational thresholds deferred to it; **NO quetzal
  threshold in law text (Q2,000 premise fails at law level)**; only
  US$10,000 triggers (arts. 31/81/82); **vigencia = 17-SEP-2026** (art.
  128, publication 17-jun + 3 months — corrects the 17-jun cutover
  belief); PO universe expands (cooperatives, empeño, real estate,
  vehicles, art/jewels, corporate services, lotteries, VASPs,
  professionals/notaries with monthly aviso ≤15 días hábiles); ML offence
  narrowed to intentional-only; retention 5y + 10y digital (financial
  POs). Lineage: D-51-2001 (effective 15-nov-2001) → D-67-2001 art. 47
  derogation after ~32 days (arts. 1-31 survive verbatim). Registry
  amended (66_/75_/76_/77_ rows).
- 2026-08-19 — **SYNTHESIS PREP COMPLETE — MASTER INDEX BUILT**.
  `gt/.extractions/00_MASTER_INDEX.md` COMMITTED (SV pattern; gitignore
  exception pre-existed): 40 topic clusters (E1-E8 e-invoicing / TX1-TX7
  taxation / P1-P7 payroll / F1-F6 fiscal-reporting / C1-C6 COA+commercial /
  SR1-SR6 special-regimes), 81-row resolved-contradictions ledger, 140-GOQ
  register rolled from ALL 250 per-file OQs (struck audit list carries the
  resolved-in-file/cross-wave ~50), binding authority orders per topic +
  26-file key table, coverage totals with the OQ1-OQ18 mapping. Built
  subagent-driven: 6 rollup agents (one per wave, full evidence-file reads;
  W-GT1 and W-GT5 returned EMPTY messages on first dispatch — files confirmed
  absent before re-dispatch; both retries clean), controller verified 8
  load-bearing quotes by grep — all passed verbatim (48_ form identities,
  EVID-175 Q150k, 74_ "artículo 8 'A'", 77_ art. 128 → 17-sep-2026, 81_ ZF
  header, EVID-143 anulación window, EVID-474 LET hunting map, 63_ NIT/ID
  rule). **Three index-level resolutions/corrections:** **R20** Q150,000
  attribution = D-4-2012 arts. 12/13/18 reforming LIVA arts. 45/46 (55_ fn.1
  and W-GT2 EVID-175 agree; the "LAT attribution" was the research-era error —
  closes EV04c OQ-3); **R45** CCom vigencia = **1971-01-01** as modified by
  D-43-70 (the 01-07-1970 string is the reform tag date, NOT the vigencia —
  corrects gt/HANDOVER §5e); **R81** maquila art. 12 bis was **ADDED by
  D-19-2016 art. 7** (tag verbatim; D-38-04 touched arts. 1/3/3bis/12/13/14 —
  corrects gt/HANDOVER §5f "born D-38-04"). DOWNLOAD_QUEUE bumped to rev 7
  (acquisition priorities re-ranked from the GOQ register). **NEXT: S-GT1
  (e-invoicing) plan doc → subagent synthesis wave** (evidence-complete; the
  master index is the gate and it is closed).
- 2026-08-19 — **W-GT6 COMPLETE** (special regimes, unit 27 — THE LAST
  EVIDENCE WAVE). Stage 1: 6 digital PDFs + 2 OCR (71_/81_). Stage 2: 2
  reader agents (ZF chain / maquila chain), controller spot-verified 12+
  quotes. 2 evidence files COMMITTED (EVID-646..745):
  `67-68_72_80_81_ZF` (646-708), `69-71_Maquila` (711-745). Key
  outcomes: **ZF exemption schedules (67_, as consolidated)** —
  administradora ISR 100% **15 años** (from período after operation
  auth.); usuario ISR 100% **10 años** (from calificación notificación);
  inmuebles 5 años (central-government share only); IVA: intra/inter-ZF +
  local inputs no afectas; fondo US$0.10/m²/month (first 5 days);
  ISR declared under LAT Libro I then consigned exonerado (68_ art. 17).
  **D-6-2021 delta = narrow** (law arts. 1, 5 Bis, 41 + adds 50 Bis
  defraudación aduanera + grandfathering per pre-D-19-2016 resolutions;
  does NOT touch the 21/22 schedules); its vigencia = publication day
  1-jun-2021 (art. 6; the "art. 43 = 90 days" clause belongs to a
  page-mate decree — metadata corrected). **OQ15 RESOLVED with registry
  correction: AG 65-2022 (81_) IS the AG 242-90 ZF-reglamento reform**
  (arts. 1-24: e-expediente, firma electrónica avanzada, tarifario;
  e-provisions 14-sep-2022) — the W5 "ZOLIC-only" verdict was wrong (body
  carries ZOLIC tarifario items = mislabel source). **68_ = inconsistent
  consolidation** (untagged pre-65-2022 arts. 3/6/8/13; tarifario item 9
  mislabeled; art. 18 cites derogated law art. 26). **Maquila
  (69-71_)**: post-D-19-2016 shape — classic maquiladora/exportadora AT
  get ONLY 1-year DAI+IVA suspensión on inputs (art. 12); **the 10-year
  total ISR exoneration lives solely in art. 12 bis d)** (productora AT
  vestuario/textiles SA ch. 50-63 + prestadora servicios TIC/BPO
  non-residents) + machinery/fuel exonerations; old art. 15 (maquila ISR
  holiday) printed only as "Derogado" — text unrecoverable in-corpus;
  art. 12 bis born D-38-04 (2005), reformed D-19-2016. Intemporal: no
  sunset; 10-year clock per-beneficiary from calificación notification.
  **70_ consolidation defect: no AG 253-2001 tags (23 bis/ter born 2001
  per 71_, not 2013 as printed)**; 71_ identity CONFIRMED (AG 253-2001,
  D-114-97 basis, derogates AG 196-96). Compliance cadence: monthly
  cuenta-corriente DJ day 20 electronic (+3-month trailing IGSS planilla
  via SEADEX), coeficiente report 20th hábil, annual labor DJ 40 days +
  nómina 2 months; 100% diversion multa; IGSS-driven suspension ladder
  2/4/6 months + recidivism doubling. **D-19-2016 gap map sharpened —
  THE blocking acquisition for post-2016 ISR-window modeling** (67_ tags:
  9+ articles incl. derogating 23/24/26; maquila transitional arts.
  absent); AG 3-2017 + D-38-04 = tag-only leads. Registry amended
  (70_/71_/81_ rows).
- 2026-08-20 — **S-GT1 COMPLETE** (e-invoicing + catalogs synthesis).
   Plan `docs/superpowers/plans/2026-08-19-s-gt1-synthesis.md`; 8 topic
   files + index + COVERAGE committed (GT-EINV-FR-001..243,
   GT-CAT-FR-001..015; 139 LBs / 99 ACs / 45 OQ rows consuming
   GOQ-15..52 + 02/03/07/13/14). Catalog sidecars generated from 29_/30_
   (GH authority; _DRIFT.md records channel diffs verbatim; generator
   gt/scripts/build_gt_catalogs.py idempotent). Master-index GOQ write-back
   done. Evidence corrections: 19-code legacy FACE list; 18+3 complements;
   Reglas 3.5.1.6. D1-contingencia architecture tension flagged (FR-220).
   Next: S-GT2 taxation plan.
- 2026-08-20 — **S-GT2 COMPLETE** (taxation synthesis). Plan
   `docs/superpowers/plans/2026-08-20-s-gt2-synthesis.md`; 7 topic files +
   index + 2 CSV sidecars committed (GT-TAX-FR-001..261; 136 LBs / 93 ACs /
   38 OQ rows consuming GOQ-53..69 + GOQ-01/06 owned + kin
   04/13/14/49/50/99/102/103/118/119/120/124). R20/R55/R46 consumed as
   mandated (R20 = full law-copy footnote mapping 45←12/46←13/50←18;
   R55 rows shipped secondary-print-pending in iva_retention_rates.csv;
   R46 identities throughout). **Two in-corpus GOQ resolutions:**
   GOQ-118 RESOLVED (AG 425-2006 art. 4 = Sistema procedure AND art. 9 =
   dualidad — both citations correct; R52 dissolved, source-verified) and
   GOQ-68 RESOLVED-NEGATIVE (24_ art. 29 ¶6 = electronic-invoice exception,
   NOT AG 125-2022 text; ¶4 = 6-month rule per AG 222-2019; acquisition
   stands). GOQ-119 modeling call made (config-driven dualidad + saas
   Sistema-% resolution). COVERAGE 42 cited / 40 N-A / 0 pending. Final
   whole-branch review: 1 Important (FESP cross-lock mispointed at
   FR-080..085 → repointed to FR-097/GT-EINV-FR-036/LB-021) + minors fixed
   in one commit. Next: S-GT3 payroll plan (GOQ-70..91 + GOQ-04/09/10/11).
- 2026-08-20 — **S-GT3 COMPLETE** (payroll synthesis). Plan
   `docs/superpowers/plans/2026-08-20-s-gt3-synthesis.md`; 10 topic files +
   index + 1 CSV sidecar committed (GT-PAY-FR-001..236; 159 LBs / 151 ACs /
   29 OQ rows consuming GOQ-70..91 + GOQ-04/09/10/11 owned + kin
   58/61/99/121). P1 four-way split (01 salary / 02 jornada / 05 benefits /
   06 termination); salario_minimo.csv 82 rows [sic]-faithful (2026 six
   cells words-govern per GOQ-77/78; 2022-2025 ABSENT rows per GOQ-11,
   never interpolated). R30-R44 corrections instantiated (bonus identities;
   preaviso worker-side; NO cesantía/doubling; no holiday 2×; IRTRA flat 1%
   no brackets; IGSS rates external; CT edition qualifier). ISR side
   consumed by exact FR id via 09_isr-iva-interfaces.md (S-GT2 lesson
   applied; GT-TAX-FR-169 location corrected to taxation/05).
   **Trust-evidence rule caught THREE controller-brief errors** (art. 96
   less-favorable rule → art. 103 ¶2; in-kind "customary prices" →
   "precio de costo o menos"; INTECAP ladder dates — industrial 1.00%
   ceiling 1-Jan-1974 / agro 1-Jan-1975, not the brief's reading) +
   50%-of-indemnización (art. 82 e) over brief's "50%-of-offset").
   COVERAGE 58 cited / 24 N-A / 0 pending. New gap reports flagged for
   register triage: OT hourly-base divisor, per-locality festividad config,
   art. 152 a)/d)/e) + art. 154 re-extraction, día-hábil calendar
   provenance. Next: S-GT4 fiscal-reporting plan (F1-F6 + GOQ-92..121;
   consumes taxation + payroll FR ids).
- 2026-08-20 — **S-GT4 COMPLETE** (fiscal-reporting synthesis). Plan
   `docs/superpowers/plans/2026-08-20-s-gt4-synthesis.md`; 6 topic files +
   index committed (GT-FIN-FR-001..185; 111 LBs / 79 ACs / 40 OQ rows
   consuming GOQ-92..121 + GOQ-14 owned + kin 01/06/09/66/67/94/101/105 and
   resolved kin 118/119/120). F1-F6 map one-to-one: 01 form inventory +
   channel model (R46-corrected ISR identities on every naming row; R53
   both-windows validity ledger; R58 SAT-2390-outside-catalog negative);
   02 RetWeb (operational surface OF GT-TAX-FR-105/106/107 — 2340 15 dh vs
   2320 10 dh never frozen per R47; R54 constancia-date asymmetry; rate
   rendering of both taxation CSVs, secondary-pending rows unfrozen);
   03 pequeño two-document chain (55_ = as-of-~2013 banner GOQ-100; R20
   attribution; R56/R57 guards; LIVA art. 48 whole-month deadline, no day
   invented GOQ-103); 04 LET books (PC+3 especiales one combined book vs
   General two books/resumen-insumo; GOQ-105 layouts-images negative-FR;
   4%/5%-10-dh = tariff rule never a deadline GOQ-107); 05 SAT-2390 (the
   cross-validation gate; CSV spec authoritative from 63_ — 16/11-col
   layouts column-letter-faithful; >Q2,500 NIT+ID from 2023-01 dated row
   GOQ-113); 06 criterios confirm-only layer (GOQ-116 clause-citation ban;
   GOQ-121 negative-FR; dualidad consumes taxation/03's one model).
   Taxation consumed by exact id (GT-TAX-FR-105..110, 025/031..037 + both
   CSVs); payroll via GT-PAY-FR-213..222; GT-EINV-FR-210 outcome-only.
   COVERAGE 67 cited / 15 N-A / 0 pending (9 rows flipped; 49_/50_ source
   paths normalized into fin02 LB cells). Two wave-close fixes: T1 stale
   forward-ref filename; GOQ-99 annotation prefix. New gap reports flagged
   for register triage: ISR-constancia form code (rides GOQ-98), D27-92
   Cap. VIII/IX primary texts (electrónico-tariff anchors), informe
   periodicity tension, 63_ rule-6c ventas col-D omission. Next: S-GT5
   COA/commercial plan (C1-C6 + GOQ-122..134; D-19-2016 still blocks
   S-GT6/S-GT7).
- 2026-08-21 — **S-GT5 COMPLETE** (COA + commercial-legal, clusters C1-C6;
  plan `docs/superpowers/plans/2026-08-21-s-gt5-synthesis.md`). 7 files +
  2 indexes: chart-of-accounts 01_books-anchor (GT-COA-FR-001..033) ·
  02_dual-track-habilitacion (034..060) · 03_retention-destruction-matrix
  (061..074 = **GOQ-124 RESOLVED-DELIVERED**; closes GT-EINV OQ-005/GOQ-41
  kin); commercial-legal 01_rm-surfaces (GT-CML-FR-001..025) ·
  02_sociedades-lifecycle (026..085) · 03_titulos-valores-prescripcion
  (086..125) · 04_aml-compliance (126..163; 17-sep-2026 cutover spine).
  237 FRs / 118 LBs / 78 ACs / 27 OQ rows; GOQ-122..134 + GOQ-05/12 all
  consumed; R45/R60..R71 instantiated; R70 GOQ-133→132 off-by-one fixed.
  Consumption by exact id (GT-TAX-FR-066/214/216/217/230..232/234;
  GT-FIN-FR-020/086..089/104/118; GT-PAY-FR-058/063; GT-EINV-FR-203);
  coa01 FR-021 backfill names GT-CML-FR-001. COVERAGE 74 cited / 8 N-A /
  0 pending (60/66/73/75/76/77/83 flipped; stale S-GT6 labels fixed).
  New gap reports flagged for register triage: art.-604 clock anchor,
  art.-577 debenture anchor, acciones-amortizadas gloss row, impedimento
  owning FR, Código Civil corpus, R71 pre-cutover PO-list risk. Final
  whole-branch review pending (first action of next session). Next: S-GT6/
  S-GT7 special-regimes plan (D-19-2016 still blocking, GOQ-08).
- 2026-08-21 — **S-GT6/S-GT7 COMPLETE (special-regimes; SYNTHESIS PHASE
  ENDS — ALL SEVEN WAVES DELIVERED)**; plan
  `docs/superpowers/plans/2026-08-21-s-gt6-s-gt7-synthesis.md` (one plan,
  one session, both wave ids; prefix GT-SPR). 7 files: special-regimes
  01_zf-exemption-schedules (GT-SPR-FR-001..033) · 02_zf-chain-regime
  (034..060) · 03_maquila-benefit-shape (061..094; R75 negative anchor
  first) · 04_maquila-reglamento-chain (095..133) ·
  05_compliance-cadence-sanctions (134..171; GOQ-99 verbatim-deadline
  discipline) · 06_cross-regime-bridges (172..193; GOQ-08 acquisition
  ledger delivered) + 00_index. 193 FRs / 102 LBs / 79 ACs / 20 OQ rows;
  GOQ-08 + GOQ-135..140 all consumed + kin 01/04/10/99; R72..R81
  instantiated; **4 stale master-index preamble R-cites fixed at
  write-back (R49→R72, R50→R73, R52→R75, R55→R81 — curated ledger
  governs)**. Consumption by exact id (GT-TAX-FR-071..073/147/152/153/
  159..165/214/216/217/232; GT-PAY-FR-018/170/176; GT-FIN-FR-052/054/
  055/065/066/068/069; GT-EINV-FR-178; GT-COA-FR-047..049). **COVERAGE
  82 cited / 0 N-A / 0 pending — CORPUS CLOSED.** All 7 task reviews
  Approved first-pass (zero fix rounds). Methodology: art. 23 quater +
  68_ art.-35-bis renderings quote the txt layers where the frozen
  evidence files truncate (disclosed in LB rows). New gap reports
  flagged for register triage: AG 52-2017 text absent (35 bis adder);
  maquila 12 bis closing-¶ vs 8 bis service-universe asymmetry (folds
  into GOQ-08 on acquisition). **Next: S-GT6/S-GT7 final whole-branch
  review (first action of next session) → §4.6 milestone merge.**
- 2026-08-22 — **ACQUISITION BATCH 2 DELIVERED (owner browser; 12
  instruments registered 84_–95_; queue rev 8 struck; GOQ acquisitions
  annotated in the master index)**: 84_ D-19-2016 (**GOQ-08 blocker IN
  HAND** — art. 7 adds 12 bis verified against primary, R81 confirmed;
  transitorios present; gazette also carries D-20-2016 first page) ·
  85_ D-31-2024 (GOQ-13; image-heavy scan — deeper OCR pass needed) ·
  86_ AG 125-2022 (GOQ-68, reglamento D-7-2019) · 87_ IGSS Acuerdo
  1421-2018 (GOQ-10 mora half) · 88_ D-62-2001 (GOQ-132 instrument —
  pure IVA art.-4-num.-1 reform, NOT AML content) · 89_ D-58-2005 +
  90_ AG 86-2006 (FT law + reglamento, GOQ-134 + bonus) · 91_ AG 4-2005 ·
  92_ Código Civil Dto-Ley 106 (GOQ-147) · 93_ D-76-78 aguinaldo (GOQ-09
  December half — 100%/half-Dec-half-Jan) · 94_ D-38-2004 · 95_ AG 3-2017.
  Duplicates rejected md5-identical: LET IVA-General manual (= 58_),
  certificador procedure (= 22_, v2.1 confirmed current). Registry 94
  entries; COVERAGE 82 cited + 12 pending (evidence passes reopen the
  corpus). Still missing: AG 52-2017 (GOQ-149), consolidated IVA ≥2018
  (GOQ-01/146), D-37-2001 (GOQ-09 half), IGSS Reglamento de Recaudación
  (GOQ-04 cuota rates), AG 75-2006. **NEXT: W-GT7 evidence pass (EVID-746+)
  over 84_–95_ + targeted synthesis backfills (special-regimes GOQ-08
  fences; payroll/04 aguinaldo ABSENCE-FR replacement; payroll/07 mora;
  AML FT-lineage; cml03 fallback clocks; maquila reglamento
  supersession); then §4.6 merge.**
- 2026-08-22 — **W-GT7 COMPLETE (batch-2 evidence pass + targeted
  synthesis backfills — corpus re-closed 94 cited / 0 N-A / 0 pending)**.
  Stage 1: 85_ force-OCR'd (footer layer defeated the 80-char heuristic —
  76_/77_ lesson; 8.8k chars/pp recovered). Stage 2: 5 reader agents
  (maquila/ZF D-19-2016 chain · IVA/FEL instruments · IGSS+aguinaldo · FT
  pair · Código Civil decomposed), controller spot-verified ~20
  load-bearing quotes (all passed, incl. whitespace-normalized re-checks).
  5 evidence files COMMITTED (EVID-746..951): `84_91_94_95_MaquilaZF_
  D19-2016_chain` · `85_86_88_IVA_FEL_D31-2024` · `87_93_IGSS_Aguinaldo` ·
  `89_90_FT` · `92_Codigo_Civil`. Key outcomes: **GOQ-08 RESOLVED**
  (D-19-2016 primary-read: ZF art. 23 keeps 10-años-from-notificación — no
  nominal window change; transitorios 28-30 + untitled art. 18 top-up;
  12-bis-¶/8-bis asymmetry verbatim-real; old art. 15 not reproduced BUT
  94_ recovers the 2005-state trio — AT holiday was art. 12 c); AG 3-2017
  current reglamento reformer, supersession-mapped vs 70_); **GOQ-13
  RESOLVED** (art. 13 IVA 8-"A" verbatim; art. 7 FEL mandate — law names
  NO DTE codes; ICT = Impuesto a la Confianza Tributaria — also resolves
  GOQ-24); **GOQ-68 CLOSED** (AG 125-2022 = reglamento D-7-2019 + AG
  5-2013/425-2006 reforms; 79_ art. 32 pointer = own footnote; arts. 48-49
  reforms); **GOQ-09 half + R82** (D-76-78 = SECTOR PRIVADO ONLY — "…y
  Público" label wrong, public = D-1633 absent; 50%-Dec-quincena +
  50%-Jan-quincena; one-way supletoriedad; payroll/04 FR-095 ABSENCE →
  private engine); **GOQ-10 RESOLVED** (1421 art. 9 fecha límite day-20 +
  art. 38 mora JM-floating cap-100%; FR-161 incobrabilidad fix; cuota
  rates → GOQ-04 refined to PROGRAM reglamentos); **GOQ-132
  RESOLVED-NEGATIVE** (88_ pure IVA, adjacency artifact); **GOQ-134
  RESOLVED** (FT pair primary; art. 18 light tier; AG 118-2002 = AML
  reglamento named at 2-mar-2006 — NOT AG 75-2006); **GOQ-147 RESOLVED**
  (CC art. 1508 5-y fallback closes FR-110; art. 604 = conservation duty;
  acciones-amortizadas = CCom 577 ¶2; horizon ≥ 26-ago-2008 caveat).
  Backfills: 20 requirements files in place, 7 new LB rows, zero FR
  renumbering. Master index: GOQ write-backs + R82 + EV07a..e + totals;
  COVERAGE 94/0/0; DOWNLOAD_QUEUE rev 9 (AG 118-2002 first, D-1633 new,
  IGSS program reglamentos refined). Failure mode hit: BF1 backfill
  dispatch returned EMPTY twice with zero writes (7-file unit too large) —
  split into two, both clean. **Remaining queue: AG 52-2017 (GOQ-149),
  consolidated IVA ≥2018 (GOQ-01/146), D-37-2001 (GOQ-09), D-1633
  (GOQ-09), IGSS program reglamentos (GOQ-04), AG 118-2002/75-2006
  (GOQ-12 lineage). Next: §4.6 merge; no further waves pending.**
- 2026-08-23 — **W-GT8 COMPLETE (batches 3+4 evidence pass + targeted
  backfills)**: 12 registry rows (96_–101_, 103_–108_; gap 102 = SINAS
  re-reject killing the AG 75-2006 AML hypothesis), 6 evidence files
  EV08a..f (EVID-952..1185), 9 backfilled requirements files (10 new LB
  rows, zero FR renumbering), master-index write-backs (GOQ-01
  resolved-composite / 107+146 resolved / 09 in-part / 12 settled / 04
  re-refined→Acuerdo 1124 / 14+145 re-scoped flat), COVERAGE re-closed
  106/0/0, queue rev 11 (calendario JSF item closed — SAT publishes flat
  deadlines only; 1124 + D-1633 art.-11 montos top-ranked; AG 52-2017
  low-priority watch). Material: D-1633 = standing public aguinaldo with
  external art.-11 quantum; 4%/5% electrónico tariff = D-27-92 art. 54
  "E" (D-7-2019) SUNSET 2025-08-09; SEM program reglamento set acquired
  rateless; SAT calendars carry no NIT-digit windows. **Next: §4.6 merge
  of W-GT8 commits; no further waves pending.**
- 2026-08-23 (ii) — **W-GT9 COMPLETE (IGSS JD-library wave)**: 7 rows
  (109_–115_), 4 evidence files (EVID-1186..1305), payroll/07+10
  backfills, GOQ-04 IVS-rate half resolved (3.67+1.83 = 5.50 pair),
  program-family map pinned, corpus re-closed 113/0/0, queue rev 12
  (residue = SEM/accidentes rates via the 410 art.-85 chain). **Next:
  §4.6 merge at session close.**
- 2026-08-23 (iii) — **W-GT10 COMPLETE (JD-library hunt + 1520/1556
  acquisitions)**: hunt verdict NEGATIVE for the SEM/accidentes rate
  instruments (no Acuerdo 475, no rate-setting title among ~500 —
  EVID-1329; DCA-archive owner-browser route only); +2 registry rows
  (116_ Acuerdo 1520/AG 239-2022 = the 1421 arts. 4/5 reform: floor
  formula SMM × 243.3333/30.4167/1.00 + distribution proportions
  corroboration-only; 117_ Acuerdo 1556/AG 17-2026 = standing
  exoneración window ≈25-mar→25-sep-2026); EV10 = EVID-1306..1329
  (controller-written); payroll/07 LB-028/029 + FR-165/169/182/183 +
  payroll/10 LB-011 addendum; GOQ-04 base-floor half formula-anchored
  (rate residue unchanged); corpus re-closed 115/0/0, queue rev 13.
  **Next: §4.6 merge at session close; then idle on owner-side inputs.**
