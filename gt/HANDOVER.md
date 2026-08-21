# gt/HANDOVER — Guatemala Session State & Continuation Guide

**For the next controller session.** Written 2026-08-19 at close of the GT
source-research sessions (W1–W5 + owner DCA batches); updated 2026-08-19
(convergence-audit session: shared-rules D16 reconciliation +
EXTRACTION_PLAN draft); updated 2026-08-19 again (W-GT1 evidence-pass
session: plan approved, FEL stack read, evidence committed); updated
2026-08-19 again (W-GT4 evidence-pass session: fiscal reporting read,
form-identity corrections, evidence committed); updated 2026-08-19 once
more (W-GT5 evidence-pass session: COA + commercial-legal read, OQ14
resolved, evidence committed); updated 2026-08-19 once
more (W-GT6 evidence-pass session: special regimes read, OQ15 resolved + registry
identity correction, ALL SIX EVIDENCE WAVES COMPLETE); updated 2026-08-19
once more (synthesis-prep session: **00_MASTER_INDEX.md built + committed**
— 40 clusters / 81 R rows / 140 GOQs; 3 index-level corrections incl. 2 to
THIS file §5e/§5f); updated 2026-08-20 (**S-GT1 e-invoicing synthesis
COMPLETE — see §5h + §10 S-GT1 addenda**); updated 2026-08-20 again
(**S-GT2 taxation synthesis COMPLETE — see §5i + §10 S-GT2 addenda**);
updated 2026-08-20 once more (**S-GT3 payroll synthesis COMPLETE — see §5j
+ §10 S-GT3 addenda**); updated 2026-08-20 once more (**S-GT4
fiscal-reporting synthesis COMPLETE — see §5k + §10 S-GT4 addenda**). Read
this fully before acting; it is the authoritative cross-session memory.
**Update it at every session boundary.**

Session bootstrap command: `Read gt/HANDOVER.md and continue.`

## 1. What this work is

GT requirements-extraction for the Odoo localization, per
`shared/docs/requirements-extraction-procedure.md` (method spine) and the SV
corpus as precedent. Currently in **Stage 4 (synthesis): S-GT1 (e-invoicing)
COMPLETE 2026-08-20** (8 requirements files + 00_index + COVERAGE committed;
GT-EINV-FR-001..243 + GT-CAT-FR-001..015; 139 LBs / 99 ACs), **S-GT2
(taxation) COMPLETE 2026-08-20** — 7 requirements files + 00_index + 2 CSV
sidecars committed (GT-TAX-FR-001..261; 136 LBs / 93 ACs / 38 OQ rows;
GOQ-53..69 + GOQ-01/06 all consumed; **GOQ-118 + GOQ-68 resolved in-corpus,
R52 dissolved**) and **S-GT3 (payroll) COMPLETE 2026-08-20** — 10 requirements
files + 00_index + 1 CSV sidecar committed (GT-PAY-FR-001..236;
159 LBs / 151 ACs / 29 OQ rows; GOQ-70..91 + GOQ-04/09/10/11 all consumed;
salario_minimo.csv 82 rows; R30-R44 corrections instantiated; ISR consumed
by exact FR id via payroll/09) and **S-GT4 (fiscal-reporting) COMPLETE
2026-08-20** — 6 requirements files + 00_index committed
(GT-FIN-FR-001..185; 111 LBs / 79 ACs / 40 OQ rows; GOQ-92..121 + GOQ-14
all consumed; R46-R59 guards instantiated; taxation consumed by exact FR
id — GT-TAX-FR-105..110 + 025/031..037 + both CSVs; payroll via
GT-PAY-FR-213..222). ALL SIX EVIDENCE WAVES COMPLETE (W-GT1 FEL
stack + W-GT2 taxation + W-GT3 payroll + W-GT4 fiscal reporting + W-GT5 COA
+ commercial-legal + W-GT6 special regimes; 26 evidence files, EVID-001..745);
**synthesis prep DONE — `gt/.extractions/00_MASTER_INDEX.md` is committed
and is THE synthesis gate** (topic clusters, R-ledger, GOQ register,
authority orders). **Next: S-GT5 (COA/commercial-legal) plan doc → synthesis
wave** (C1-C6 + GOQ-122..134 per master index; consumes COA/commercial
clusters; GOQ-124 retention/destruction matrix is an S-GT5 deliverable;
D-19-2016 still blocks S-GT6/S-GT7 special-regimes).
Product architecture context: root `HANDOVER.md` §1 (SaaS thin-client + Odoo;
Takumi consumes requirements).

## 2. Read order for a new session

1. This file
2. `docs/superpowers/specs/2026-08-18-gt-source-research-design.md` —
   decisions D-GT1..D-GT10 (scope, policies, FEL provider model, journal/
   document-type design, dated-instrument regime)
3. `gt/SOURCE_RESEARCH.md` — research record: wave log, candidates, verdicts,
   OQ register (OQ1–OQ17 with statuses), acquisition log
4. `gt/sources/README.md` — the registry (provenance + re-verify flags)
5. `gt/DOWNLOAD_QUEUE.md` — remaining owner-browser items (rev 5; most closed
   by the 2026-08-19 batch)
6. Root `HANDOVER.md` §GT (cross-session) + `shared/docs/` method docs

## 3. Repo/session mechanics

- **Branch `gt-research`, worktree `.worktrees/gt-research`** (same convention
  as HN; `.worktrees/` git-ignored via main commit f6f5415). Main is being
  actively committed by the SV session — never work outside the worktree;
  merge `gt-research` → `main` at milestone by owner decision.
- Commit style: short imperative, no emojis; commit per batch (precedent in
  `git log gt-research`).
- **`.gitattributes` carries `gt/sources/** -text`** — global
  `core.autocrlf=input` must never normalize source bytes (incident fixed
  2026-08-18: 24 blobs were silently CRLF-normalized; re-committed pristine).
  HN worktree should adopt the same line at merge time.
- Python: `~/.venvs/localizations/bin/python` (shared, absolute path — works
  from the worktree). Scripts in `shared/scripts/` (extract_text.py etc.).

## 4. Corpus state (2026-08-19)

**82 registered entries** (`gt/sources/`, numbering 01–83; gap 27 unused):
FEL e-invoicing stack (acuerdos 13-2018/26-2019/15-2020, incorporation
resolutions SAT-DSI 04_–14_, Reglas y validaciones **v1.7.10 Feb-2025**, Doc.
Técnico Servicios, 26 XSDs + 3 JSON catalogs × 2 channels (29_ GitHub pinned
961133c; 30_ cat.desa), manuals, casos-de-prueba 2018, contingencia 2018);
taxation core (IVA 27-92 **pre-FEL vintage — OQ10**, Reglamento IVA AG
5-2013, Código Tributario 6-91, LAT 10-2012 + AG 213-2013, **D-10-2025 IVA
reform — derogates Art. 8-"A"** (added D-31-2024; the "3-'A'" belief was a
myth — W-GT2), D-20-2006 + AG 425-2006 retenciones basis);
payroll (Código de Trabajo D-1441, IGSS set incl. Res. 08-SGF/2026, IRTRA
**D-1528 (1962) — identity corrected W-GT3**, INTECAP **D-17-72**, **bono 14
D-42-92 (40_) + incentivo D-78-89 (41_) — titles corrected W-GT3; December
aguinaldo law D-76-78 = MISSING**, salario
AG 250-2020 + **AG 256-2025 (2026 rates; CE2 maquila = Q3,221.10)** +
Historia 1995-2021); fiscal reporting
(form inventory snapshot 2025-10-06, retenciones Web pages+manuals, LET
manuals ×3, agentes roster 2025-10, criterios 6-2018/2-2019, SAT-2390 set);
COA anchor (Código de Comercio D-2-70, 301pp); special regimes (ZF D-65-89
chain **D-65-89 → D-19-2016 → D-6-2021**, maquila D-29-89 set, ZOLIC AG
65-2022); commercial-legal (AML **D-67-2001 + D-51-2001 + D-15-2026 Ley
Integral (17-jun-2026)**, RM edictos + aranceles).

**Known-stale instruments retained deliberately** (supersession discipline):
23_ (IVA pre-FEL), 68_ (ZF reglamento **inconsistent consolidation — AG
65-2022 reformed it; W-GT6**), 75_ (AML — **supersession
CONFIRMED W-GT5: D-15-2026 art. 126 derogates it effective 17-sep-2026;
current until then**), 17_/19_ (2018 vintage FEL docs), **55_ (pequeño
digest = undated ~2013 body still live at the 2024 capture — W-GT4)**,
**70_ (maquila reglamento: no AG 253-2001 tags; pre-65-2022-era text in
places — W-GT6)**. Reform chains are recorded in SOURCE_RESEARCH.md.

## 5c. W-GT3 facts a synthesis session MUST know (2026-08-19)

- **Bonus-law identity corrections (material)**: 40_ = **BONO 14** (D-42-92:
  paid "primera quincena del mes de julio"; 100% of ordinary salary averaged
  over the year ending June; prorated). 41_ = **old incentivo law** (D-78-89,
  hourly floor Q0.15/Q0.30). **The December AGUINALDO law (Decreto 76-78) is
  NOT in corpus — acquisition candidate; never invent December-bonus
  mechanics.** Current Q250/mes incentivo = D-37-2001 (also missing).
- **IRTRA = flat 1% on total planillas** (D-1528 art. 12 as reformed by
  D-43-92; no brackets — OQ12 disproven). 42_ identity = Decreto 1528
  (29-May-1962). Text layer = substituted-glyph cipher, decoded with audit
  key in the evidence file.
- **IGSS OQ11 still open**: no cuota rates anywhere in corpus (D-295 prints
  only 25/50/25 financing proportions; 08-SGF/2026 defers rates to the JD
  Reglamento de Recaudación — acquisition candidate). NO tope máximo; base
  floor = salario mínimo AG vigente; patrono delivers both shares wholesale
  (laboral + patronal); planilla electrónica lifecycle; single receipt
  IGSS+IRTRA+INTECAP; mora day-after-due + 5% admin; ±1% rounding tolerance.
- **INTECAP = 1% vigente** (law's 0.50/0.75/1.00 ladder; reglamento art. 9:
  "uno por ciento del valor de los salarios mensuales"), base = IGSS
  planillas, **first 20 días of next month** (IGSS collects, retains 2%).
- **CT money rules**: jornada diurna 8/48 (45 effective paid as 48),
  nocturna 6/36, mixta 7/42; **OT ≥ +50%** (12h/day cap; holiday work = OT
  on top, no literal 2×); **vacaciones 15 días hábiles** + 150-day
  qualification + no cash-out while employed + 5-year retro cap;
  **indemnización (despido injusto) = 1 month/year uncapped**, base = 6-month
  average, IGSS offsets; preaviso is WORKER-side (semana/10d/2sem/mes);
  **NO auxilio de cesantía exists** (SV folk model rejected); salarios
  caídos ≤12 months; maternidad 84 días @100% + inamovilidad; lactancia
  2×½h/10 months; menores ≥14; inembargabilidad ladder + 50% alimentos cap;
  **CT contains zero aguinaldo/bono/propina provisions** — those are the
  specific laws' territory exclusively.
- **Salario mínimo structure**: 2 circunscripciones (CE1 = Guatemala dept,
  CE2 = rest) × 3 actividades; 2026 values transcribed [sic]-faithful (see
  registry row 37_ — includes the internal 3,416.90-digits vs
  3,816.90-words defect); history (39_) covers 1995-2021 only — 2022-2025
  AGs missing (minor gap).
- **Planilla IVA-FEL (56_)**: asalariado IVA credit via FEL DTEs + SAT-8560
  DUCA + SAT-2901 FYDUCA + SAT-2311/2799; window 01-Jan → 10th día hábil
  enero; Formulario SAT-1111 + Constancia; re-filing last-wins (priors =
  ANULADAS) + must report to patrono.

## 5d. W-GT4 facts a synthesis session MUST know (2026-08-19)

- **FORM-IDENTITY CORRECTIONS (material — bind S-GT2/S-GT4 synthesis)**:
  ISR anual lucrativas = **SAT-1411**; asalariados anual = **SAT-1431**;
  SAT-1371 = **ISR no-residentes pago directo mensual**; ISR retenciones =
  **SAT-1331** (1321 = ISR capital mensual). The W4-era research note
  ("ISR anual = 1371") was a table misread, corrected row-level against the
  48_ snapshot (2025-10-06). Rejected-myths list + registry + plan updated.
- **48_ channel model**: every tax declaration is Declaraguate-only;
  AsisteLight carries ZERO vigente forms (legacy); 27 admin forms
  paper-only; the 24 Anexo forms are generated inside SAT apps
  (RETENCIONES WEB, RETENISR, EXENIVA, PLANILLA IVA-FEL, AGENCIA VIRTUAL) —
  a fifth filing surface. SAT-1111 dual identity (current PLANILLA IVA-FEL
  app + superseded paper ISR planilla). SAT-2390 ABSENT from 48_: devolución
  CF family = 2124 (general, paper) + 2053/2062/2073 exportadores (ante B
  de Guatemala); electronic dev.CF forms live outside the 4 tables.
- **18 dated-validity strings** captured (e.g. 2237/2046 "Septiembre 2013
  en adelante"; NoVigentes table = valid_to ledger; printed 1-month
  overlap IVA cluster flagged).
- **RetWeb**: SAT-2340 = 15 días hábiles (general+pequeño) but **SAT-2320
  agro = 10 días hábiles**; 51_ p.9 = full ISR retention concept catalog
  (~30 conceptos, rate/base formulas); 52_ = "art. 54 B" D-27-92
  full-accounting agent path (retain only vs Agropecuario sin calificación;
  card payments exit the base); **5% pequeño (ops ≥Q2,500.01)/agro rates =
  OQ18** (additional regimes to reconcile vs W-GT2 matrix in 23_/24_);
  53_ roster as-of 2025-10-01, ~8.4-8.5k agents, columns
  NIT/name/fecha-inicio only; SAT-0261 = voluntary "Otros Agentes"
  inscription (D-20-2006 art. 6).
- **Pequeño/libro (55_/61_)**: 55_ = undated ~2013 body still live at the
  2024-05-13 capture (2043/2047 era; AG 5-2013; pre-FEL) — every number
  as-of; 61_ = ~2018+ LET/SAT-2046 era. Q150,000 threshold attributed by
  55_ fn.1 to **D-4-2012 arts. 12-13 reforming LIVA arts. 45-46** (vigor
  25-Feb-2012, de-oficio migration 1-Apr-2012) — tension vs W-GT2's LAT
  attribution = per-file OQ-3, resolve at synthesis vs law text. Deadline
  = "mes calendario siguiente" (LIVA art. 48; no fixed day/hábiles rule).
  Exit rule LIVA art. 50 (prior-year >Q150k → general). Q2,500 op floor
  and Q50 planilla NOT printed in either doc (live in law text, W-GT2
  xref). FEL content: zero in 55_; auto-load into LET in 61_.
- **LET (57_/58_/82_) + informe (59_)**: PC & especiales = ONE combined
  compras-y-ventas book (in-system SAT-2046 generation); general = TWO
  books per establecimiento generating NO form (resumen = "insumo" for the
  external monthly IVA filing). Feeds: FEL ventas immutable; compras FEL
  by selection; general adds FYDUCA + DUCA + paper path (vehicles ≤2 model
  years); constancias auto-detected. **Only deadline printed anywhere:
  electrónicos 4% if declared within first 10 días hábiles else 5% (82_
  glossary, D27-92 caps.)** 59_ informe = art. 57 "D" D27-92 attestation
  flow; carga masiva hard 100%-success gate. **Record-level field layouts
  are ALL images — never guess fields; OCR/re-capture is an acquisition
  task.** No LET-creating resolution printed anywhere (EVID-474 = hunting
  map). 58_ verified identity (owner-browser download) + print defect:
  glossary defines RTN as the **Honduras** registry [sic] — Guatemala
  uses NIT.
- **SAT-2390 (62_/63_)**: devolución CF régimen general (venders to
  exentas); claim after IVA-declaration due date, **up to 4 years**,
  strictly quarterly/semiannual; SAT cross-validates Libro CSV totals vs
  declared crédito/débito (reject on mismatch — verbatim error captured).
  CSV spec: compras 16 cols (payment block never blank; 17-value tipo-doc
  catalog incl. FESC, FPC-for-no-credit), ventas 11 cols (col K closed
  vocab), files `SAT_<MES><AÑO>_{COMPRAS,VENTAS}.csv` (printed
  "SAT_MESAÑO_…"), rows 1-2 skipped, all cells TEXT except dd/MM/yyyy,
  NC negative/ND positive, comma ban. **Dated row: ventas NIT+ID mandatory
  for ops >Q2,500 a partir de enero 2023.** "FCE" [sic] printed for FACE;
  neither doc prints date/version in text layer.
- **Criterios (64_/65_)**: 2-2019 (applies 1-Jun-2019) dualidad =
  dual-quality agents retain under EACH quality at per-activity statutory
  rates; operational % determined by SAT's Sistema de Retenciones (AG
  425-2006 art. 4); its rate table CONFIRMS the W-GT2 matrix. 6-2018
  (23-Apr-2018): sueldos deductible only if workers in IGSS planilla when
  registration obligatory (≥3 workers; transporte terrestre ≥1);
  related-party sueldos capped at 10% renta bruta; **aguinaldo + bono 14
  each capped at 100% one monthly salary** (excess via pacto colectivo
  homologado only); dietas to pequeños need definitive ISR retention
  (LAT art. 44). 64_ OCR gaps: pages 4/5/8 blank; "20-2008" [sic] for
  20-2006; CT art. 91 (65_) vs 94 num. 7 (64_) numbering divergence.
  Neither prints a third-party-weight formula.



## 5h. S-GT1 facts a synthesis/QA session MUST know (2026-08-20)

- **Deliverables (all committed, branch gt-research)**:
  `gt/requirements/e-invoicing/00_index.md` + 7 topic files
  (01_document-types E1 FR-001..041 · 02_dte-schema E2 FR-042..070 ·
  03_validation-rules E3 FR-071..139 · 04_mandate-onboarding E4
  FR-140..170 · 05_certificador-interface E5+E7 FR-171..203 ·
  06_anulacion-contingencia E6 FR-204..227 · 07_display-representation E8
  FR-228..243) + `gt/requirements/catalogs/01_governance.md`
  (GT-CAT-FR-001..015) with CSV sidecars
  (CAT-FRS 88 / CAT-UGR 43 / CAT-MSG 211 rows, GH-authority) + `_DRIFT.md`
  + `_INDEX.md` + generator `gt/scripts/build_gt_catalogs.py`
  (idempotent). `gt/requirements/COVERAGE.md`: 82 registry rows = 26 cited
  / 56 not-applicable (pending S-GT2..7) / 0 pending-unowned. **24_ is
  cited beyond the expected set** (04 LB-018 = AG 222-2019 layer only) —
  flagged per-row; remainder of 24_ → S-GT2.
- **Wave totals: 243 GT-EINV FRs + 15 GT-CAT FRs; 139 LBs; 99 ACs; 45 OQ
  rows consuming GOQ-15..52 + GOQ-02/03/07/13 (+GOQ-14 kin)**. Master-index
  write-back done (43 rows carry "[S-GT1: cited in …]"; synthesis-order
  line updated). Plan doc:
  `docs/superpowers/plans/2026-08-19-s-gt1-synthesis.md`.
- **Evidence corrections made DURING synthesis (trust-evidence rule held
  twice against controller briefs)**: legacy FACE referencia-origen = **19
  codes (incl. "9" per EVID-141)**, not the plan's 18; complement
  inventory = **18+3** (11 shared + 7 GH-only + Endoso×3 per EVID-030),
  not "~15"; NC/ND cross-certificador liberation = Reglas **3.5.1.6**
  (evidence), not 3.7.1.6 (controller-prompt drift); GOQ-27/33 brief
  descriptions were swapped — register followed.
- **D1 architecture tension (OPEN — surface to product owner)**: GT
  contingencia legally REQUIRES local offline XML generation (Reglas v2.0
  §4.1; FR-220 flags it) vs S0.5 D1 "no local-fallback generation"
  posture (SV-shaped). Needs an explicit architecture ruling before
  implementation waves.
- **Standing citations discipline shipped in-file**: Reglas = "v2.0
  (19/12/2024, vigencia abril 2025)"; rates as dated rows valid_from
  2024-12-19 (GOQ-50); establishment = CodigoEstablecimiento-only (D-GT9
  instantiated in 05 §establishment — the section pre-flagged for product
  owner); NIT check-digit NOT implementable in-corpus (GOQ-49 — no mod-11
  guesses); contingencia footer URL = verificador-integrado (the 2018
  efactura URL is banned-context only).

## 5i. S-GT2 facts a synthesis/QA session MUST know (2026-08-20)

- **Deliverables (all committed, branch gt-research)**:
  `gt/requirements/taxation/00_index.md` + 7 topic files
  (01_iva-core TX1 FR-001..045 · 02_iva-pequeno TX2 FR-046..068 ·
  03_iva-retenciones TX3 FR-069..110 · 04_isr-trabajo TX4 FR-111..146 ·
  05_isr-lucrativas-capital TX5 FR-147..193 · 06_ct-procedures TX6
  FR-194..235 · 07_reform-chain-provenance TX7 FR-236..261) + CSV sidecars
  (`iva_retention_rates.csv` 16 rows = 8 statutory + 8
  secondary-print-pending; `isr_rates.csv` 17 rows incl. 4 transitional
  valid_to). **261 FRs / 136 LBs / 93 ACs / 38 OQ rows**; COVERAGE 42
  cited / 40 N-A / 0 pending. Plan doc:
  `docs/superpowers/plans/2026-08-20-s-gt2-synthesis.md`.
- **Two GOQs RESOLVED in-corpus during synthesis (master index annotated)**:
  **GOQ-118** — AG 425-2006 **art. 4 = Sistema-de-Retenciones procedure AND
  art. 9 = dualidad rule; both citations were correct; R52 tension
  dissolved** (source-verified in 79_ txt; EV02d has no dedicated art.-9
  EVID). **GOQ-68** — RESOLVED-NEGATIVE: **24_ art. 29 ¶6 prints the
  electronic-invoice exception, NOT AG 125-2022 text** (¶4 = 6-month rule
  per AG 222-2019; zero "125-2022" hits in 24_) — AG 125-2022 acquisition
  need stands. GOQ-119 modeling call made: config-driven dualidad (retain
  under EACH quality) + saas Sistema-% resolution + prorrateo.
- **R55 shipped unfrozen**: the EV04b 5% additions (pequeño ≥Q2,500.01, agro
  5% total factura, sector-público 25/5/5) live ONLY as
  secondary-print-pending dated rows (GOQ-06 open until the consolidated
  IVA / art. 54-bis text arrives — rides GOQ-01).
- **GOQ-99 statutory half answered**: LAT art. 72.a + 28_ art. 70 print
  "días hábiles"; LAT arts. 78/80 print plain "días" — transcribed exactly
  per instrument in taxation/04; the RetWeb constancia-delivery half stays
  with F2. SAT-2320 agro 10-día deadline = RetWeb-layer print whose
  instrument is NOT in corpus (GOQ-01-context note; statutory = 15 días
  hábiles uniformly per R26).
- **GOQ-120 recorded unresolved** (CT art. 91 vs 94 num. 7 — both texts
  verbatim, no in-corpus resolution possible; needs a post-2016 CT
  consolidation).
- **Final-review lesson carried forward**: every cross-file "owned there"
  handoff must terminate at a RESOLVING FR id, never a family-range guess
  (the FESP IVA-side cross-lock initially pointed at FR-080..085 — fixed to
  FR-097 + GT-EINV-FR-036 + 05's LB-021 owning the Art. 52/52"A" anchor).
  S-GT3+ briefs should name exact FR ids when pointing at taxation.
- **Consumption surface for later waves**: S-GT3 payroll consumes
  taxation/04's art. 70/72 caps + projection FRs (IGSS shares external per
  GOQ-04); S-GT4 fiscal-reporting consumes FR-105..107 (retention
  deadlines), the two CSV rate catalogs, and the R46 identity rows; F-wave
  mechanics are cross-ref'd but never re-derived.

## 5j. S-GT3 facts a synthesis/QA session MUST know (2026-08-20)

- **Deliverables (all committed, branch gt-research)**:
  `gt/requirements/payroll/00_index.md` + 10 topic files
  (01_ct-salary-model P1 FR-001..025 · 02_working-time-overtime P1
  FR-026..050 · 03_minimum-wage P2 FR-051..075 + `salario_minimo.csv`
  (82 rows) · 04_statutory-bonuses P3 FR-076..100 ·
  05_vacaciones-maternidad P1 FR-101..126 · 06_contracts-termination P1
  FR-127..152 · 07_igss-contributions P4 FR-153..184 · 08_irtra-intecap P5
  FR-185..206 · 09_isr-iva-interfaces P6 FR-207..222 · 10_sso-provenance P7
  FR-223..236). **236 FRs / 159 LBs / 151 ACs / 29 OQ rows**; COVERAGE 58
  cited / 24 N-A / 0 pending (16 payroll rows flipped). Plan doc:
  `docs/superpowers/plans/2026-08-20-s-gt3-synthesis.md`.
- **GOQ-04 discipline shipped**: every IGSS rate/base/tope/cotizable
  component = configurable shared row; 12.67/4.83 priors appear ONLY as
  rejected-prior flags; NO-tope-máximo is itself a negative-FR; mora tasa =
  Acuerdo 1421 external (GOQ-10 half). What 35_ owns: two-share delivery,
  base-floor concept + top-up (amount not printed), planilla electrónica
  lifecycle (GENERAR→TRANSMITIR→VALIDAR→PAGAR; rectificación only estado
  "pagada"), one-planilla-per-patrono + per-obra extras, single receipt
  IGSS+IRTRA+INTECAP, mora shape + 5% cap Q3,000, nota-de-cargo 5/15/15/5,
  RD ≤60m/100% cap, waivers, Q500 + ±1% + Mar-1977/Sep-2022 cutoffs.
- **Salario mínimo CSV = the fidelity surface**: 2026 six cells
  digit-for-digit [sic] with WORDS-GOVERN resolutions (art. 6 digits
  3,416.90 [sic] → 3,816.90; art. 7 = 3,221.10 as printed, NEVER 3,321.10 —
  GOQ-77); 2022-2025 = explicit ABSENT rows that BLOCK consumers (GOQ-11 —
  never interpolated); 2004 CC-suspension = gap segments; monthly formula
  SD × 365/12 noted but printed figures govern (R35/GOQ-82).
- **Bonus laws (R30/R36/R41 instantiated)**: bono 14 = 100% ORDINARY
  month (June-ending average — R36 tension vs art. 93 salario completo
  recorded), 1-15 July window, termination proration from preceding
  1-July, included in indemnización at 6/12 (D-42-92 art. 4); incentivo =
  D-78-89 original (floors [sic]) with today's Q250 = D-37-2001
  quoted-only row + acquisition watcher (GOQ-09); non-contributory unless
  jointly agreed, séptimo-día-only base integration (R42); December
  aguinaldo = ABSENCE-FR with exactly four recordable known-facts.
- **Termination shape (R33/R37)**: indemnización 1 month/year UNCAPPED,
  base = last-6-months salario completo average, bono 14 at 6/12, IGSS
  actuarial offsets + 50% OF THE INDEMNIZACIÓN (art. 82 e — evidence
  reading over an earlier brief's "50%-of-offset"); preaviso worker-side
  money-only-with-consent; salarios caídos ≤12m separate line; NO
  cesantía/doubling anywhere (only 2× = art. 159 domicilio sanction,
  myth-note).
- **IRTRA/INTECAP (R31/R32)**: both flat 1% patronal on IGSS-planilla
  salaries; IRTRA "SOBRE LA TOTALIDAD DE LAS PLANILLAS" no brackets;
  INTECAP ladder dated rows — industrial 0.75% during 1973 → 1.00% ceiling
  1-Jan-1974; agro 1-Jan-1973/1974/1975 (EVID-361; an earlier plan-brief
  reading was wrong — evidence governs); in-force 1% via
  Reglamento-1980 art. 9º only (GOQ-89); 20-day deadline = the only
  printed planilla-window value in the corpus (IGSS's own fecha límite
  external, GOQ-10); art. 16 fee kept ambiguous (GOQ-85).
- **09_isr-iva-interfaces.md = the feed-contract file**: every ISR value
  consumed by EXACT FR id (GT-TAX-FR-112/115/116/117/121/122/124/
  130..133/135..138/141/145/146 + GT-TAX-FR-167..169 — 169 lives in
  taxation/05, not 04); GT-EINV-FR-210 = anulación blocker cross-ref;
  SAT-1111 = PLANILLA IVA-FEL app form (R46); window 01-Jan → 10th día
  hábil 23:59:59; last-wins/ANULADAS re-filing; IGSS-planilla ≠
  SAT-planilla disambiguation FR.
- **Controller-brief errors caught by the trust-evidence rule (4 this
  wave)**: art. 96 less-favorable rule → really art. 103 ¶2; in-kind
  "customary prices" → "a precio de costo o menos"; 50%-of-offset →
  50%-of-indemnización; INTECAP ladder dates. All recorded in
  implementer/reviewer reports; evidence governs everywhere.
- **New gap reports (NOT register GOQs — triage pending)**: OT
  hourly-base divisor (02↔03 interplay); per-locality festividad config;
  art. 152 a)/d)/e) + art. 154 maternity-base re-extraction needs + three
  corpus-silent design defaults in 05 (each marked never-law); día-hábil
  calendar provenance (09). These are candidates for register addition at
  the next master-index maintenance pass.

## 5k. S-GT4 facts a synthesis/QA session MUST know (2026-08-20)

- **Deliverables (all committed, branch gt-research)**:
  `gt/requirements/fiscal-reporting/00_index.md` + 6 topic files
  (01_form-inventory-channels F1 FR-001..026 · 02_retenciones-web F2
  FR-027..074 · 03_pequeno-libro-regime F3 FR-075..102 ·
  04_let-electronic-books F4 FR-103..130 · 05_devolucion-credito-fiscal F5
  FR-131..164 · 06_criterios-interpretive F6 FR-165..185). **185 FRs /
  111 LBs / 79 ACs / 40 OQ rows**; COVERAGE 67 cited / 15 N-A / 0 pending
  (9 rows flipped; 49_/50_ source paths normalized into fin02 LB cells at
  close — HTML snapshots are cited `gt/sources/<nn>_….html (read via txt
  layer)`). Plan doc:
  `docs/superpowers/plans/2026-08-20-s-gt4-synthesis.md`.
- **R46 discipline shipped**: every ISR-form-naming row across the wave
  carries the corrected identity set (anual lucrativas = 1411; asalariados
  anual = 1431; 1371 = no-residentes mensual; retenciones = 1331; 1321 =
  capital mensual). R47 (2320 10-dh = RetWeb print, instrument NOT in
  corpus — statutory 15 dh uniformly via GT-TAX-FR-106) and R53
  (Sep/Oct-2013 both-windows validity ledger; old periods keep predecessor
  codes) instantiated as never-frozen dated rows.
- **Statutory non-re-derivation held everywhere**: 02 renders
  `taxation/iva_retention_rates.csv` + `isr_rates.csv` (R55 5%-additions +
  25/5/5 stay secondary-print-pending, GOQ-06 open); 03 consumes
  taxation/02 (GT-TAX-FR-046..068) under the GOQ-100 as-of-~2013 banner
  (R56 Q.179.00 never copied; R57 no digest paragraph-ordinals); 04's
  glossary prints anchor to taxation ids; 05's statutory layer =
  GT-TAX-FR-025/031..037 (GOQ-111: 62_ prints NO legal basis); 06 is
  confirm-only (dualidad = taxation/03's ONE model; GOQ-116 clause-citation
  ban from 64_'s blank pages; GOQ-121 negative-FR — 65_'s title-only bonus
  citations cannot backfill GOQ-09).
- **GOQ-105 layouts-images negative-FR is the F4 hard blocker**: no LET
  record-level layout may be asserted until re-captured (acquisition
  GOQ-105); the SAT-2390 CSV spec (63_) is the ONE printed layout and is
  column-letter-faithful (group-header spans are images — never
  transcribed). 4%/5%-within-10-días-hábiles = a TARIFF rule (Cap. IX
  D27-92), never a LET deadline (GOQ-107); LET/informe deadlines live
  outside the manuals — the calendario-perpetuo ingestion requirement
  (GOQ-14) is now OWNED by fin01/03/04 (per-NIT-digit windows external,
  JSF transcription candidate).
- **New gap reports (NOT register GOQs — triage pending)**: ISR-constancia
  form code unprinted by 50_ (rides GOQ-98); D27-92 Cap. VIII/IX primary
  texts absent (04's electrónico-tariff rows anchor-pending); informe
  periodicity tension (monthly print vs semestral glossary hint — recorded
  under GOQ-108); 63_ rule-6c ventas col-D omission (flagged-not-corrected,
  kept verbatim). Candidates for register addition at the next
  master-index maintenance pass.
- **Session mechanics**: 6 implementer dispatches + 6 task reviews, ALL
  Approved first-pass (zero fix rounds; one cosmetic minor deferred per
  file at most). Controller grep-verified 2-3 quotes per file (~15
  verbatim quote checks — all passed). No empty-return failures. Two
  wave-close fixes by controller: T1 stale forward-ref filename; GOQ-99
  register-annotation doubled prefix (script artifact).

## 5. GT facts a new session must know

- **FEL model**: SAT owns XML standard + validates; taxpayers integrate via
  **certificadores de DTE** (18 authorized; NOT "instaladores"). **TotalDoc =
  GRUPO CDS S.A., NIT 107902281**, authorized 02/12/2021 → **02/12/2026
  (OQ7 renewal watch)**. Product default provider = TotalDoc (D-GT5/D-GT6);
  public docs only so far; partner-access list in SOURCE_RESEARCH W1-C.
- **No "Anexo técnico" exists** — equivalents: Reglas y validaciones +
  Documento Técnico Servicios + XSDs + JSON catalogs.
- **Schema drift (OQ3, material)**: cat.desa vs GitHub differ in 8/17 shared
  files; GitHub main = "versión 2" actively maintained. Ask TotalDoc/SAT
  which set production validates against.
- **ISR today = LAT D-10-2012** (26-92 superseded). **ISR anual = SAT-1371**
  ("2236" = legacy, rejected). **IVA retenciones = D-20-2006 + AG 425-2006**
  ("resolución 2-2010" = rejected myth).
- **FEL legal chain**: AD 13-2018 → 26-2019 → 15-2020 + SAT-DSI incorporations
  243-2019…400-2023 (04_–14_). Ley IVA Art. 29-"A" is the law-level hook
  (cited by AD 15-2020; **provenance pinned: added by Dto. 4-2019 art. 6**)
  — post-2018 consolidated IVA still missing (OQ10).
- **D-GT8/D-GT9/D-GT10 bind synthesis**: `l10n_latam_invoice_document`
  (one journal, multi document types — now also shared default **D17** in
  `shared/docs/odoo-localization-guide.md`; D-GT8 = its GT instantiation);
  sucursales/warehouses/cash-registers → FEL establishment/dispositivo codes;
  **dated-instrument regime** — D-GT10 instantiates **shared D16**
  (`shared/docs/regulatory-change-management.md`): dated rule rows
  (valid_from/to + provenance; changes add rows), fecha-emisión rule
  selection, no past-dated transmission (certification timestamp;
  historical = non-transmittable accounting class), retro payroll with
  original-period rates, freeze-at-filing, backdating UX. **Naming note
  (2026-08-19 merge session): GT's "shared D13" proposal was renumbered
  D16** (D13/D14 = SV journal/establishment instantiations of D17); D16 was
  reconciled with D15 (as-of doctrine) and amended with HN's D-H2/D-H3
  (hard no-override emission block outside authorization-range vigencia;
  ingestion reconciliation against filed declarations). Cite D15+D16
  together; D18/D19 + `shared/docs/go-live-readiness.md` also bind
  synthesis (GT register already seeded there).

## 5e. W-GT5 facts a synthesis session MUST know (2026-08-19)

- **CCom books anchor (the COA topic's legal base)**: art. 368 (texto
  D-40-99) — partida doble + **PCGA** mandatory; FOUR RM-authorized books:
  Inventarios; De primera entrada o diario; Mayor o centralizador; De
  Estados Financieros — **no copiador de correspondencia** in the current
  text (correspondence = 5-year documents duty, art. 382). Español +
  moneda nacional (369); chronological, no blanks/raspaduras, immediate
  error-salvation (373); balance + P&G signed comerciante+contador ≥1×/year
  (374/377); every entry needs documento fehaciente (381); books kept
  until full liquidation (376), documents ≥5 años (382). **No plan de
  cuentas/catálogo anywhere in CCom — the chart itself is PCGA-governed**
  (no statutory COA exists in GT). No electronic-books provisions (only
  "mecanizados… cualquier otro sistema", art. 368 ¶3). **"Habilitación" is
  SAT/CT vocabulary; CCom says RM "autorización" (art. 372) — parallel
  tracks, both needed per book, never merged.**
- **66_ print facts**: given 28-ene-1970, promulgated 9-abr-1970, vigencia
  **1-ene-1971** (art. XI as modified by D-43-70 — **corrected at
  master-index merge, R45: the 01-07-1970 string is the reform TAG date, not
  the vigencia**); **last
  inline reform = D-11-2006 (DCA 30-05-2006) — consolidation horizon**;
  pp.215-301 = old D-2946 maritime Libro III appendix, still vigente;
  INFILE/TESORERIA stamp, no print date.
- **60_ dual-track habilitación**: CC's 4 books need RM authorization AND
  SAT habilitación (form **SAT-7121**, any tax office / Agencia Virtual);
  tax-law books (IVA/PC) need SAT only. Missing either → cierre temporal
  (CT art. 85); books not up to date / wrong form → Q5,000 per
  fiscalización (CT art. 94.4). **IVA art. 29-"A" (added D-4-2019 art. 6,
  vigencia 30-oct-2019 — third corpus confirmation): REF/FEL taxpayers run
  an electronic system subsuming the 5 book categories**; SAT Agencia
  Virtual "libros electrónicos" tool auto-loads DTEs for FEL emitters
  (LET hook).
- **RM surfaces**: arancel (73_, 1pp scan, **prints NO date** — 2022 label
  is registry-derived, likely superseded, "Ajuste por vigencia de nuevo
  Arancel" rows): books authorization **Q0.20/hoja** (variable); edicto
  Q30 + publicaciones Q200 (sociedades nuevas, capital/fusión/disolución
  mods) / Q100 (dirección-type, clausura/traspaso); disolución Q300;
  escritura modificación Q300; **variable inscripción fee scale NOT
  printed** (market pattern suggests a Q500,000 threshold in the unprinted
  scale — inference only). **83_ edictos: D-18-2017 art. 12 reformed CC
  art. 343 — all CC-mandated publications go via RM's electronic portal**
  (edition 6022, Wed 19-ago-2026; LIBRO ELECTRONICO sociedades ~29 per
  edition; convocatoria entries = text-layer stubs, content not
  extractable).
- **AML chain (OQ14 RESOLVED)**: **D-15-2026 art. 126 derogates D-67-2001
  AND D-58-2005 wholesale** (+ generic clause); art. 125 auto re-points
  old references. **Reglamento mandated (art. 127): SB/IVE elaborates,
  ≤6 months from vigencia ≈ 17-mar-2027 — ALL operational thresholds
  (KYC umbrales, cash/transfer triggers, fine gradation, RTS plazos)
  deferred to it.** **NO quetzal threshold anywhere in the law text —
  the Q2,000 premise fails at law level** (old-regime reglamento tier;
  watch the new reglamento). Only US$10,000 triggers (daily-cash registry
  art. 31, border declaration art. 81, trasiego art. 82); fines
  US$500-300,000 tiers. **VIGENCIA = 17-SEP-2026** (art. 128: publication
  17-jun-2026 + 3 months — **corrects the 17-jun cutover belief**; D-67
  -2001 remains current until then; transitory arts. 116-124/127 run from
  17-sep-2026). PO universe: + cooperatives, empeño, real estate,
  vehicles, art/jewels cash commerce, corporate services, lotteries,
  VASPs, professionals/notaries (light regime: per-client registry +
  monthly aviso ≤15 días hábiles). ML offence narrowed to intentional-only
  (was "obligado a saber"). Retention 5y + 10y digital (financial POs).
  Lineage: D-51-2001 (urgencia, effective 15-nov-2001) → D-67-2001 art.
  47 (after ~32 days; arts. 1-31 survive verbatim) → D-15-2026.
- **Sociedades/comercial (66_, EVID-536..569)**: see evidence file for the
  comerciante calificación (arts. 2/3/6/9), matrícula thresholds/patente
  (334/344/356-358), sociedad types + constitution formalities, títulos
  valores taxonomy (factura mercantil = paper ancestor of FEL — lineage
  noted, never conflated), prescripción specials (513, 626-629, 577, 799,
  916-918, 253).

## 5f. W-GT6 facts a synthesis session MUST know (2026-08-19)

- **ZF exemption schedules (67_ D-65-89, as consolidated)**:
  administradora ISR 100% **15 años** (from the período de imposición
  after operation authorization); usuario (bienes industriales /
  servicios) ISR 100% **10 años** (from notificación of calificación);
  inmuebles **5 años, central-government share only** (municipal share
  untouched); IVA: intra/inter-ZF transfers + local inputs **no
  afectas**; fondo = **US$0.10/m²/month**, due first 5 days of following
  month (72_); ISR declared under LAT Libro I then consigned
  **exonerado** (68_ art. 17). All = D15 dated rows.
- **D-6-2021 delta = narrow** (law arts. 1, 5 Bis, 41 + adds 50 Bis
  defraudación aduanera + grandfathering per pre-D-19-2016 resolutions);
  does NOT touch the 21/22 schedules. **Its vigencia = publication day
  1-jun-2021 (art. 6); the "art. 43 = 90 days" clause belongs to a
  page-mate decree (metadata corrected in evidence).**
- **OQ15 RESOLVED + registry identity correction**: **81_ AG 65-2022 IS
  "REFORMAS AL REGLAMENTO DE LA LEY DE ZONAS FRANCAS, AG 242-90"**
  (MinEconomía 11-mar-2022, DCA 14-mar-2022; arts. 1-24: e-expediente +
  firma electrónica avanzada + tarifario restructure; **e-provisions
  effective 14-sep-2022**). The W5 "ZOLIC-only" verdict was WRONG (the
  body carries ZOLIC tarifario items — source of the mislabel). **68_ =
  inconsistent consolidation**: arts. 3/6/8/13 print pre-65-2022 text
  untagged; tarifario item 9 mislabeled (authentic "Cancelación de
  resolución $500"); art. 18 cites derogated law art. 26.
- **Maquila (69_ D-29-89) post-D-19-2016 shape — never assume "maquila =
  ISR-exempt"**: classic maquiladora/exportadora AT get ONLY a 1-year
  DAI+IVA **suspensión** on inputs (art. 12); the **10-year total ISR
  exoneration lives solely in art. 12 bis d)** — productora AT
  (vestuario/textiles, SA ch. 50-63) + prestadora de servicios
  (TIC/BPO to non-residents) — plus machinery DAI+IVA exoneration, fuel
  exoneration, local inputs/services outside IVA. **Old art. 15 (maquila
  ISR holiday) printed only as "Derogado" — text unrecoverable
  in-corpus** (pre-2016 beneficiaries unmodelable without it / D-19-2016).
  art. 12 bis **ADDED by D-19-2016 art. 7 (corrected at master-index merge,
  R81 — the earlier "born D-38-04" was wrong; D-38-04 touched arts.
  1/3/3bis/12/13/14)**. Intemporal:
  no sunset; 10-year clock **per-beneficiary from calificación
  notification**; conditions: cost accounting + perpetual inventories;
  foreign-branch carve-out where home country credits GT ISR.
- **70_ AG 533-89 consolidation defect**: carries NO AG 253-2001 tags —
  23 bis/ter credited to AG 253-2013 though 71_ proves they were born in
  2001 (23 ter then: 20-days-of-January → first-40-days-of-year + boleta).
  **71_ = AG 253-2001 CONFIRMED** (OCR header garble + D-114-97 legal
  basis + AG 196-96 derogation; likely read 27-jun-2001, flagged).
- **Maquila compliance cadence**: monthly cuenta-corriente DJ **day 20,
  electronic** (+ trailing 3-month IGSS planilla via SEADEX); coeficiente
  report 20th día hábil; annual labor DJ 40 days + nómina 2 months; 100%
  diversion multa; IGSS-driven suspension ladder 2/4/6 months (≥50-worker
  tier), doubling on calendar-year recidivism.
- **D-19-2016 = THE blocking acquisition for special-regimes synthesis**
  (67_ tags: touching 9+ law articles incl. derogating 23/24/26; maquila
  transitional articles absent; whether it changed ISR windows for
  post-2016 ZF users is unresolvable in-corpus). Tag-only leads:
  **AG 3-2017** (maquila reglamento reformer), **D-38-04** (2005 maquila
  reformer — NOT the 12 bis creator; see R81), **DL 21-84** (predecessor).
  Cross-chain: D-65-89 refs at maquila law arts. 4 bis/36 bis + reglamento
  arts. 9 j)/42 bis (CAUCA-documented, IVA-exempt inter-regime flows).

## 5g. Master-index session facts (2026-08-19 — READ BEFORE ANY SYNTHESIS)

- **`gt/.extractions/00_MASTER_INDEX.md` is committed and is THE synthesis
  gate**: 40 topic clusters (E1-E8 / TX1-TX7 / P1-P7 / F1-F6 / C1-C6 /
  SR1-SR6), 81-row R-ledger, **140-GOQ register** (the sole open-questions
  authority — the ~195 per-file OQs live rolled there + struck audit list;
  headline OQ1-OQ18 mapped in its coverage totals), binding authority orders
  per topic, 26-file key table (EV01a..EV06b citation prefixes).
- **Every S-GT wave consumes clusters/R/GOQ ids from the index** — nothing
  outside its GOQ register may be treated as an open question; waves write
  answers back against GOQ ids.
- **Three index-level resolutions:** R20 (Q150,000 = D-4-2012 reforming LIVA
  arts. 45/46 — closes the LAT-attribution confusion), R45 (CCom vigencia
  1971-01-01 — corrected §5e above), R81 (maquila 12 bis added by D-19-2016
  art. 7 — corrected §5f above).
- **Working rulings embedded in the index preamble:** Reglas cited as "v2.0
  (19/12/2024, vigencia abril 2025)" only; GitHub 961133c = working
  authority EXCEPT MediosdePago (cat.desa); 16_ = provider-boundary doc
  only; 23_ IVA never cited alone; retention form numbers cite RetWeb not
  D-20-2006; CT currency qualifier mandatory; "autorización"=RM vs
  "habilitación"=SAT never merged; exemption windows = per-beneficiary D15
  rows keyed by qualification events.
- Rollup scratch (per-wave inputs to the index) lives in
  `gt/.extractions/masterindex_scratch/` (git-ignored).

## 5a. W-GT1 facts a synthesis session MUST know (2026-08-19)

- **Reglas y validaciones = v2.0** (changelog row "2.0 19/12/2024", vigencia
  abril 2025, 146pp; the "v1.7.10 Febrero 2025" cover footer is stale —
  filename encodes it). Chain jumps 1.7.9→2.0. **26 DTE types, 11 families**
  (FACT, FCAM | FPEQ, FCAP | FESP, NABN, RDON, RECI, FEPE | NDEB, NCRE |
  FACA, FCCA | FAPE, FCPE | FAAE, FCAE | FARP, FCRP | FPEC, FCPC | CIVA,
  CAIS | NEV, RANT, FACP); v2.0 added FEPE/FARP/FCRP/FPEC/FCPC (Decreto
  31-2024). Tension vs GitHub XSD (6 types commented out; BIDP XSD-only) =
  evidence OQ.
- **D-GT9 refinement (material for Odoo mapping)**: NO taxpayer
  punto-de-emisión field exists in the schema — establishment =
  `Emisor/@CodigoEstablecimiento` (xs:positiveInteger 1-9999, SAT-assigned)
  + `NombreComercial`; `DatosGenerales/@Dispositivo` (APP/AV/APPVOZ) is
  SAT-apps-exclusive; Serie/Numero are UUID-derived post-certificación.
  Odoo mapping: sucursal/warehouse → CodigoEstablecimiento; dispositivo
  mapping only for SAT-app emission (out of product scope). Runtime teeth:
  mensajes RCP305/306/460/485/497 validate establishment existence/type.
- **Schema drift (OQ3) sharpened**: GitHub = working authority EXCEPT
  MediosdePago (GitHub copy = uncompilable TurismoPasaje overwrite; use
  cat.desa there); catalogoMensajes RCP108/109 bodies swapped between
  channels; unidadesGravables PETROLEO 15/16 differ. Full matrix in
  `gt/.extractions/29_30_FEL_XSDs_catalogs.evidence.md`.
- **Mandate chronology (D-GT10 dated rows)**: 243-2019 proveedores Estado →
  838-2019 serv. profesionales → 639-2020 serv. técnicos (legacy auths void
  31-dic-2020) → 640-2020 ALL FACE emisors (FACE void 31-dic-2020) →
  887-2020 compra directa/baja cuantía (excl. <Q2,500) → 398-2021 →
  1074-2021 salud → 1218-2021 contadores → **1240-2021 régimen general
  (DTE start ≤01-jul-2022; mass mandate; cohort = IVA-registration fact)**
  → 1350-2022 pequeños (≤31-mar-2023) → **400-2023 extends pequeños →
  01-jul-2023**. No sanctions articles — enforcement = authorization lapse.
  Instruments are Resoluciones de Superintendencia (not "Directorio
  Superior"). 07_ carries a 639-2020 duplicate; 11_ carries the full
  1240-2021 text (same DCA page — the portal swap incident explained).
- **IVA Art. 29-"A" provenance PINNED**: added by **Decreto 4-2019 (Ley
  Reactivación Económica del Café) art. 6** — verbatim in 02_ considerando.
  OQ10 consolidated-IVA hunt now has an exact anchor.
- **16_ Doc Técnico = Versión 1.2, undated, XSD refs at -0.1.0** (predates
  the 0.2.1 set). Scope = SAT↔certificador ONLY (getToken 60-min /
  postFactura / postAnulacionDTE / mini-RTU push; no batch/consulta/reversion
  ops). Product integration boundary = certificador (TotalDoc) API, not SAT.
  Anulación = logical annotation, never modifies the certified DTE; Adenda
  must never reach SAT. UUID v4 generated by the certificador. Crypto:
  XAdES-BES, RSA, SHA-256.
- **Anulación window (current authority)**: until the IVA-declaration due
  date of the emission period (supersedes the 2018 5-day rule) + blockers
  (NC/ND/constancia/retención origins, prescription) + cross-certificador
  anulaciones allowed. Fecha emisión: ≤5 días back (CIVA/CAIS exempt),
  same-month future only. CF (consumidor final) cap Q2,500.
- **Rates captured (Reglas v2.0 §)**: IVA 12%/0%; IDP 13 per-unit Q rates;
  ITH 10%; ITP USD30/10; TDP 0.50%; IFB 2%; IDB 6/7.5/8.5%; TAB 100%/75%;
  CEM Q1.50; IBN Q0.18-0.08; TAP USD0.05; FESP ISR 5%; FEPE ICT 1.5%;
  agropecuario 5%/1.5%/2%/10% family; tolerance ±0.01.
- **Certificador roster (31_, as-of 2026-08-18)**: 18 authorized; TotalDoc
  (GRUPO CDS, NIT 107902281) renewal 02/12/2026 = OQ7 watch; 6 more expire
  2026 (AINNOVA/CARI/DIGIFACT/FORCON/INFILE/INFORUM/MEGAPRINT/TEKRA —
  re-check roster at next milestone).

## 5b. W-GT2 facts a synthesis session MUST know (2026-08-19)

- **OQ13 RESOLVED (verbatim, both halves)**: IVA retentions = **% OF THE
  IVA**, not of base (D-20-2006 arts. 1-6): 65% exportadores
  agropecuarios/silvícolas + D.29-89 empresas; 15% otros exportaciones +
  especiales + otros agentes; 25% sector público (municipalidades
  excepted); 15% operadoras de tarjeta (afiliado liable for the 85% not
  retained); **1.5% sobre el VALOR TOTAL** for fuel paid by card (the only
  base-exception). Q2,500 de minimis (art. 10); agent-to-agent abstention;
  declare primeros 15 días hábiles even-if-zero; constancia at retention
  moment. ISR (LAT): asalariados **5% to Q300k annual + Q15,000 + 7%**
  (withholding = annual projection/12); Opcional 5/7% monthly Q30,000;
  capital 10% + dividends 5% definitive; no-residentes 5/3/10/15/25;
  facturas especiales 5% definitive.
- **OQ17 RESOLVED-AS-MYTH**: D-10-2025 derogates IVA Art. **8-"A"** (added
  by **D-31-2024** "Ley Integración Sector Productivo Primario y
  Agropecuario" art. 13 — MINEDUC alimentación-escolar retention), NOT
  Art. 3-"A". "Art. 3-'A'" joins the rejected-myths list. D-31-2024 full
  text = acquisition candidate (also the source of the 5 new DTE types).
- **Consolidation cuts (evidence-verified)**: 23_ IVA through D-10-2012/
  D-4-2012 (no 29-"A", no 8-"A"); 24_ Reglamento IVA tail = **AG 222-2019
  only — 11 FEL arts (new registrants FEL-only from 1-jul-2021; 6-month
  cap on legacy docs)**; 25_ CT through **D-37-2016** + CC annotations to
  03-12-2019 — **no FEL-era reforms; CT Art. 120 IVA-suspension ¶ VOID per
  CC 680-2013** (FEL suspension hook must cite 98"A" not 120); 26_ LAT
  through **D-46-2022** (≤2013 registry risk REFUTED); 28_ with AG 167-2014
  only; 79_ art. 32 reformed AG 125-2022.
- **IVA core values**: tarifa única 12% price-inclusive + 5pp earmarks
  (3.5+1.5); exenciones Art. 7 (15 numerales) vs constancia-based 8/9;
  crédito fiscal prorrateo verbatim (Reg. art. 20-kin ÷1.12 mechanics);
  saldo = traslado, devolución trimestral/semestral; pequeño = **Q150,000
  annual gross threshold (2012 value — dated-row discipline) + 5% pago
  definitivo** + Q2,500 op floor + Q50 planilla; used vehicles/motorcycles
  = FIXED Q fees (Q1,000/500/300/200), not ad-valorem; ISR/LAT deducciones
  caps Q48,000/Q12,000/Q60,000; LAT Utilidades 25%, transitional 31/28/25;
  no NOL carryforward for lucrativas in consolidated text.
- **CT mechanics**: prescription 4 años (8 unregistered) / sanctions 5 años;
  mora 0.0005/day; omisión/retenidos 100% (50% pre-requirement); multa
  scale Q50/day→Q10,000+1%; cierre 10-20d; resarcitorio = Junta Monetaria
  rate (external — OQ); books retention = plazo de prescripción (no fixed
  years); e-documents/signature arts. 125/A/B.

## 6. Access realities & gotchas (verified)

- `portal.sat.gob.gt`/`www.sat.gob.gt` = **Cloudflare 403 to ALL non-browser
  clients** (browser-UA curl too). Acquisition: owner browser downloads
  (ruling OQ2) or Wayback-of-official-URL with provenance + re-verify flags
  (follow-up ruling). Wayback quirks: rate-limits after bursts (sequential +
  sleep); some `id_` captures truncate at exact 1/5 MiB boundaries — try
  alternate captures (65_ fixed via 2022 capture; 66_ via 2024-06-12).
- **SAT label ≠ content**: id 17662 "639-2020" serves a 639-**2011** PDF; id
  57855 "1240-2021" serves a 1218-duplicate post-2023 (real 1240 = digest-
  verified 2022 captures, 12_). wpfd re-ids/re-categories files (manuals
  6524→15747; LAT →78389). **Verify every download by reading it.**
- `legal.dca.gob.gt` search = JS app — owner's browser works well there
  (19 docs found 2026-08-19); CDX `filter=` regex must be lowercase.
- igssgt.org / irtra.org.gt (needs browser UA + referer) / intecap.edu.gt /
  mineco.gob.gt (`mineco.gob.gt`, not mineconomia) fetch directly.
  mintrabajo 403 (use Wayback; site rebuilt ~2024 — check capture mimetypes).
  congreso + registromercantil unusable (empty/maintenance).
- Non-official leads (never registrable): atlas.com.gt calendario
  (back-years; cross-check only), corporacionbi.com calendario,
  diamantecontador forum, capacitacionessat.page Google Sites (SAT-branded,
  non-gov domain — ratify before use).
- OCR: DCA gazette prints need `--psm 6`; **table pages need PSM 4 at
  300–400dpi** (SV D.O. lesson carries over). Several corpus PDFs are scans
  (02/03, 33–35, 38, 64–65, 71, 73, 74, 76–77, 81, 83) — Stage 1 extraction
  must OCR-verify page 1 identity before reading.

## 7. Open questions register (live ones; full list in SOURCE_RESEARCH.md)

**AUTHORITATIVE REGISTER = the 140-GOQ table in
`gt/.extractions/00_MASTER_INDEX.md` §C (OQ1-OQ18 mapped in its coverage
totals). The bullets below are the headline items only.**

- **OQ3** schema drift cat.desa vs GitHub → ask TotalDoc/SAT (drift matrix
  complete; GitHub MediosdePago defect = use cat.desa there meanwhile).
- **OQ10** post-2018 consolidated Ley IVA 27-92 — Art. 29-"A" provenance
  pinned (Dto. 4-2019 art. 6); full text still missing. ~~OQ17~~
  RESOLVED-AS-MYTH (D-10-2025 derogated Art. 8-"A", added D-31-2024;
  "3-'A'" never existed). **D-31-2024 full text = acquisition candidate.**
- **OQ11 (SHARPENED — still open)**: IGSS cuota rates NOT in corpus — live
  in the JD Reglamento de Recaudación (Acuerdo 1118-kin, acquisition
  candidate); no tope máximo; base floor = salario mínimo.
- ~~OQ12~~ **DISPROVEN + RESOLVED W-GT3**: IRTRA = flat 1% on planillas
  (D-1528 as reformed by D-43-92; no brackets; identity corrected to 1962).
- ~~OQ13~~ **RESOLVED W-GT2** (see §5b).
- ~~OQ14~~ **RESOLVED W-GT5** (see §5e): art. 126 derogates D-67-2001 +
  D-58-2005 wholesale; reglamento ≈17-mar-2027 defers all thresholds; **no
  Q threshold in law text (Q2,000 premise fails at law level)**; vigencia
  17-sep-2026.
- ~~OQ15~~ **RESOLVED W-GT6** (see §5f): AG 65-2022 = the AG 242-90 ZF
  reglamento reform (e-provisions 14-sep-2022); W5 "ZOLIC-only" verdict
  was wrong; 68_ = inconsistent consolidation.
- **OQ16** does a numbered Reglamento del Código de Comercio exist?
- **OQ18 (W-GT4)**: 5% IVA-retention rates (pequeño ≥Q2,500.01 / agro on
  total factura, printed by 49_/52_) vs the W-GT2 D-20-2006 matrix —
  reconcile against 23_/24_ law text before synthesis; "54 B"/"54 BIS"
  nomenclature rides the OQ10 consolidated print.
- **Evidence-file OQs (W-GT1..W-GT6)**: ~195 per-file OQ-1.. live in the
  26 evidence files — MOQ-roll into a master index at synthesis prep (SV
  pattern). W-GT4 adds: LET layouts = image-only (re-capture candidate);
  55_/57_/58_/62_/63_ print no dates (currency unverifiable); 64_ OCR
  pages 4/5/8 blank. W-GT5 adds: CCom consolidation horizon 30-05-2006;
  RM autorización vs SAT habilitación = parallel tracks; 73_ arancel
  undated + variable inscripción scale absent. W-GT6 adds: D-19-2016 =
  blocking acquisition (post-2016 ISR windows); AG 3-2017 + D-38-04
  tag-only leads; maquila pre-2016 art. 15 unrecoverable.

## 8. Accountant track (asked 2026-08-19; assume yes, plan B ready)

Asks: (1) current consolidated Ley IVA 27-92 print (≥2018 reforms, ideally
through D-10-2025); (2) calendario perpetuo vencimiento windows per NIT
last-digit (monthly/quarterly/annual); (3) D-15-2026 AML reglamento status +
what happens to AG 75-2006 / Q2,000 cash-documentation rule.

**Plan B (no accountant)**: proceed with corpus-as-is using the SV
gaps discipline — record missing values as OQs with instrument-provenance
notes, never guess (SV precedent: F-14 SS caps shipped as dated data with
instrument-OQs); keep owner-driven DCA browser hunts (they outperformed
every automated route); calendar windows → transcribe from SAT's JSF app in
owner browser with atlas.com.gt as cross-check only; OQ3/dated data →
surface to TotalDoc when partner access opens (W6). Requirements can be
synthesized with these as flagged open questions and back-filled later.

## 9. Next actions (ordered)

1. ~~EXTRACTION_PLAN~~ approved + ~~W-GT1..W-GT6~~ ALL COMPLETE 2026-08-19
   + ~~SYNTHESIS PREP~~ COMPLETE 2026-08-19 (master index committed —
   §5g). ~~S-GT1 (e-invoicing) synthesis~~ **COMPLETE 2026-08-20** (§5h).
   ~~S-GT2 (taxation) synthesis~~ **COMPLETE 2026-08-20** (§5i).
   ~~S-GT3 (payroll) synthesis~~ **COMPLETE 2026-08-20** (§5j).
   ~~S-GT4 (fiscal-reporting) synthesis~~ **COMPLETE 2026-08-20** (§5k).
   **NEXT = S-GT5 (COA/commercial-legal) synthesis wave**: write the S-GT5
   plan doc (S-GT1..S-GT4 pattern: tasks/global constraints from clusters
   C1-C6 + GOQ-122..134; CCom books anchor + dual-track habilitación +
   RM surfaces + sociedades lifecycle + títulos valores/prescripción + AML
   chain; **GOQ-124 retention/destruction matrix is an S-GT5 deliverable**
   (write it in the S-GT5 file); consume fiscal-reporting kin (fin04's
   habilitación bridge; R46 form identities where ISR forms are named);
   AML dated cutover 17-sep-2026 = D15 regime-cutover rows), then subagent
   loop; S-GT6/S-GT7 special-regimes last (D-19-2016 still blocking,
   GOQ-08).
2. Opportunistic gap closure (folds into any synthesis): queue rev-7 items
   (see DOWNLOAD_QUEUE; **D-19-2016 = top-ranked acquisition — blocks
   special-regimes synthesis quality**, GOQ-08); instructivos cat 15812;
   calendario transcription via SAT JSF app; accountant answers fold in
   when they arrive. **Master-index additions: LET field-layout re-capture
   (GOQ-105); 2022-2025 salario AGs (GOQ-11); AG 125-2022 (GOQ-68);
   D-4-2012 full
   text (Q150k attribution); aguinaldo D-76-78 + incentivo D-37-2001
   still missing (W-GT3). W-GT5 addition: D-15-2026 reglamento
   (≈17-mar-2027) — watch legal.dca.gob.gt. W-GT6 additions: AG 3-2017,
   D-38-04, maquila pre-2016 art. 15 text.**
3. ~~All six evidence waves complete~~ — plan reading order fully
   executed.
4. Synthesis prep after each topic's evidence base completes (master index
   + MOQ roll; SV pattern) — **all topics evidence-complete; master index
   is the gate**. Carry the W-GT4 form-identity corrections
   (1411/1431/1371/1331) into every synthesis that names ISR forms; the
   W-GT6 special-regimes corrections (81_ identity, maquila 12 bis d)
   shape S-GT7.
5. Milestone: owner decides `gt-research` → `main` merge (owner owns ALL
   merges; controller verifies branch state only). **OQ7 watch: TotalDoc
   authorization renewal 02/12/2026 — re-check the certificador roster
   (31_) at the next milestone.**
6. W6 partner follow-up when TotalDoc access exists (API manuals, sandbox,
   OQ3 + MediosdePago question).

## 10. Owner notes (2026-08-19, session close; updated same day by the
convergence session; updated again at W-GT1 close)

- ~~Owner will handle the `gt-research` → `main` merge personally~~
  **SUPERSEDED by root HANDOVER §4.6** (standard session-close & merge
  protocol, 2026-08-19): at session close the controller drives the
  rebase-then-merge + §3 merge record. GT waves 1-3 merged to main
  2026-08-20 under §4.6.
- ~~NEXT SESSION PRIORITY: uniform shared rules for all 3 countries~~
  **EXECUTED on main 2026-08-19**; residue closed by the GT convergence
  session (see above). Remaining convergence surface: keep country
  instantiations current at each synthesis close (go-live-readiness
  registers + D15/D16 registers); converge variant texts via root
  HANDOVER.md.
- **W-GT1 session rulings (2026-08-19)**: EXTRACTION_PLAN approved
  as-drafted; **evidence files COMMIT** (gitignore exceptions, SV/HN
  pattern — standing policy for all GT waves); W-GT1 executed
  subagent-driven with controller spot-verification (quote checks against
  the txt sources passed; one agent retry needed — the incorporations
  agent returned empty the first time, watch for that failure mode).
  Reglas v2.0 naming ruling: cite as "Reglas v2.0 (19/12/2024, vigencia
  abril 2025)" — never "v1.7.10" (stale footer). D-GT9 dispositivo
  refinement recorded (§5a) — flag to product owner at S-GT1 synthesis.
- **W-GT2/W-GT3 session addenda (same day, same session)**: the
  subagent-per-reading-unit + controller spot-check pattern held for 3
  waves (14 evidence files, EVID-001..370, no collisions; gaps 077-080,
  326-330). Working conventions: agents get EVID ranges pre-assigned per
  wave (W-GT2: 161-265; W-GT3: 266-370; next wave starts at EVID-371);
  agents read a committed evidence file as the format template (context
  saver); controller verifies 3-5 load-bearing quotes per wave by grep
  before commit. Registry title corrections are batched into the wave
  commit. **Next wave (W-GT4) note: 48_/49_/50_ are HTML snapshots +
  64_/65_ are scans — Stage 1 needs the HTML text dump + OCR; calendario
  JSF transcription still rides any wave (owner browser).**
- **W-GT4 session addenda (2026-08-19, same pattern, 4th wave)**: 6 reader
  agents (EVID-371..500, gaps 418-430/476-480), controller spot-verified
  20+ quotes — all passed. **48_ HTML quirk: the form tables live inside
  an escaped JS payload in the snapshot (visible DOM = chrome only) —
  recovered by unescaping + re-parsing; the dump in `.extractions/`
  documents this.** Material outcome: the W4-research-era form-identity
  note ("ISR anual = SAT-1371") was a **table misread**, corrected
  row-level (1411 anual lucrativas / 1431 asalariados anual / 1371
  no-residentes mensual / 1331 retenciones) — registry + plan myth-list +
  SOURCE_RESEARCH W4 all amended in the wave commit. New cross-file OQ18
  (5% pequeño/agro retention rates vs W-GT2 matrix). Next wave (W-GT5)
  starts at EVID-501.
- **W-GT5 session addenda (2026-08-19, same pattern, 5th wave)**: 4 reader
  agents (EVID-501..645, gaps 523-535/570-585/606-610), controller
  spot-verified 15+ quotes — all passed. **Failure mode repeat+variant: the
  66_-sociedades agent returned an EMPTY final message twice; the retry
  agent DID write the 91KB evidence file — always check the file exists
  before re-dispatching.** Stage-1 lesson: **76_/77_ carry footer-only
  text layers that defeat the scan heuristic (~94/235 chars/page, above
  the 80-char threshold) — force OCR when a political-law PDF extracts
  thin; both recovered at ~9k chars/page.** OQ14 resolved (derogations +
  reglamento deadline + no-Q-threshold + vigencia 17-sep-2026);
  66_/75_/76_/77_ registry rows amended; CCom consolidation tail verified.
  Next wave (W-GT6) starts at EVID-646.
- **W-GT6 session addenda (2026-08-19, final evidence wave)**: 2 reader
  agents (EVID-646..745), controller spot-verified 12+ quotes — all
  passed. **Second registry identity correction of the day: 81_ =
  ZF-reglamento reform AG 65-2022 (header verbatim), NOT ZOLIC-only** —
  OQ15 resolved affirmatively; W5's "retired hypothesis" note was itself
  wrong (recorded in SOURCE_RESEARCH). D-6-2021 vigencia metadata
  corrected (art. 6 = publication day; art. 43 belongs to a page-mate
  decree). Maquila: never assume ISR-exempt — 10-year exoneration only
  via art. 12 bis d (post-D-19-2016). **Session total: 3 waves (W-GT4/5/6),
  12 evidence files, EVID-371..745, 2 registry identity corrections, 2
  OQs resolved (OQ14, OQ15), 1 new OQ (OQ18). Evidence phase COMPLETE —
  master-index/MOQ prep is the next session's work.**
- **Master-index session addenda (2026-08-19, synthesis prep)**: 6 rollup
  agents (one per wave; each read its evidence files end-to-end and wrote a
  scratch rollup), controller assembled `00_MASTER_INDEX.md` (40 clusters /
  81 R rows / 140 GOQs) and spot-verified 8 load-bearing quotes — all passed
  verbatim. **Failure mode repeat: W-GT1 + W-GT5 agents returned EMPTY final
  messages AND wrote no files — always `ls` the scratch dir before
  re-dispatching (both retries clean).** Process lesson: 2 of 6 controller
  briefs carried errors inherited from this HANDOVER (CCom vigencia 1-jul-1970;
  12 bis "born D-38-04") — the agents' evidence-based readings were RIGHT and
  the briefs (and §5e/§5f) were corrected (R45/R81). **Standing rule: where a
  rollup/reader agent contradicts a controller brief on a verbatim matter,
  verify against the evidence file and trust the evidence — session-summary
  notes are secondary.** Index-level resolution R20 closes the Q150,000
  attribution confusion (D-4-2012, never LAT). DOWNLOAD_QUEUE → rev 7.
- **S-GT1 session addenda (2026-08-20, synthesis wave 1 — e-invoicing)**:
  plan doc `docs/superpowers/plans/2026-08-19-s-gt1-synthesis.md` (9
  tasks, SV S1 pattern, committed pre-wave); executed subagent-driven
  (8 implementer dispatches + 8 task reviews + mechanical T9 body), ALL
  reviews Approved first-pass (zero fix rounds). Controller spot-verified
  3-5 quotes per file by grep — all passed. **Failure mode repeated:
  empty final returns on 2 of 9 dispatches (T1 first try wrote NOTHING;
  T2 died post-write pre-commit) — always `ls` + `git log` before
  re-dispatching; the T2 finisher pattern (verify existing artifact →
  commit → report) worked well.** Trust-evidence rule caught THREE
  controller-brief errors (19-code legacy list; 18+3 complements; 3.5.1.6
  vs 3.7.1.6; plus GOQ-27/33 swap) — briefs now cite the register
  directly. Wave totals in §5h; master-index GOQ write-back committed
  (43 annotations + synthesis-order status). Two path typos fixed in
  06-file (19_/20_ .pdf.txt → .pdf). COVERAGE 26 cited / 56 N-A / 0
  pending. **Open architecture item: D1-vs-contingencia tension (§5h) —
  surface at next owner touchpoint.** Next session: S-GT2 plan doc.
- **S-GT2 session addenda (2026-08-20, synthesis wave 2 — taxation)**:
  plan doc `docs/superpowers/plans/2026-08-20-s-gt2-synthesis.md` (8 tasks,
  S-GT1 pattern, committed pre-wave); executed subagent-driven (7 implementer
  dispatches + 7 task reviews + controller T8 index/write-back + final
  whole-branch review + one fix dispatch). **6 of 7 task reviews Approved
  first-pass; T5 needed one fix round (GOQ-58 row-level caveats on
  FR-160/177/178 + OQ enumeration)**. Controller grep-verified 2-3 quotes
  per file in addition to reviewer spot-checks (all passed; ~30 verbatim
  quote checks across the wave). No empty-return failures this wave.
  **Two GOQs resolved in-corpus (GOQ-118 + R52 dissolved; GOQ-68
  resolved-negative) — see §5i; master-index write-back committed
  (23 annotations + R47/R52 + synthesis-order + 5-column GOQ table headers
  register-wide).** Final whole-branch review caught one Important
  cross-file defect (FESP IVA-side cross-lock pointed at FR-080..085
  instead of FR-097/GT-EINV-FR-036/LB-021) + 4 minors — all fixed in one
  commit, scoped re-review PASS. Two source-path typos fixed (26_LAT_ISR →
  26_LAT; 48_FormulariosVigentes → 48_SAT_Lista_Formularios html).
   COVERAGE 42 cited / 40 N-A / 0 pending (16 newly-cited rows; EV04b/c
   manuals + digest/criterios cited ONLY as dated-as-of
   secondary/interpretive anchors). **Evidence-file freeze ruling: W-wave
   evidence files are frozen artifacts — LB backfill suggestions from
   reviewers REJECTED (quotes source-txt-verified instead; owner decision if
   ever wanted).** Next session: S-GT3 payroll plan doc.
- **S-GT3 session addenda (2026-08-20, synthesis wave 3 — payroll)**:
  plan doc `docs/superpowers/plans/2026-08-20-s-gt3-synthesis.md` (11
  tasks, S-GT1/S-GT2 pattern, committed pre-wave); executed
  subagent-driven (10 implementer dispatches + 10 task reviews, ALL
  Approved first-pass — zero fix rounds; controller T11 index/COVERAGE/
  README/master-index write-back). Controller grep-verified 2 quotes per
  file in addition to reviewer spot-checks (~90 verbatim quote checks
  across the wave — all passed). No empty-return failures this wave (the
  `ls` + `git log` pre-dispatch check held as habit). **Trust-evidence
  rule caught FOUR controller-brief errors** (§5j) — every one verified
  independently by the task reviewer before the evidence reading was
  accepted. P1 split four ways (salary/jornada/benefits/termination)
  worked well; the pointer-file pattern (09, SV 08 precedent) kept the
  ISR surface re-derivation-free — 31 external FR ids grep-verified in
  targets. **New-gap discipline**: wave reports flagged 4+ unregistered
  gaps as non-OQ notes (never invented ids) — register triage pending at
  next master-index maintenance. Deferred minors recorded in the SDD
  ledger (`.superpowers/sdd/2026-08-20-s-gt3-synthesis/progress.md` —
  deleted post-wave; load-bearing ones folded into §5j). Forward-pointer
  backfill editorial pass (Tasks 1-4 "FR ids to be assigned" → now
  assignable) deferred to final review triage — NOT executed (files
  consistent as committed). Next session: S-GT4 fiscal-reporting plan
  doc.
- **S-GT4 session addenda (2026-08-20, synthesis wave 4 — fiscal-reporting)**:
  plan doc `docs/superpowers/plans/2026-08-20-s-gt4-synthesis.md` (7 tasks,
  S-GT1..S-GT3 pattern, committed pre-wave); executed subagent-driven (6
  implementer dispatches + 6 task reviews + controller T7 index/COVERAGE/
  README/master-index write-back). **ALL 6 task reviews Approved first-pass
  — zero fix rounds.** Controller grep-verified 2-3 quotes per file (~15
  verbatim checks, all passed) + reviewer spot-checks per file. No
  empty-return failures (the `ls` + `git log` pre-dispatch check held).
  Wave totals in §5k; master-index GOQ write-back committed (31 owned/kin
  annotations: GOQ-92..121 + GOQ-14; resolved kin 118/119/120 annotated as
  kin, never re-opened) + synthesis-order line. **COVERAGE convention
  note: 49_/50_ (HTML snapshots) are cited as `gt/sources/<nn>_….html
  (read via txt layer)` — the extraction-dump path alone does NOT count
  for the citation grep (fixed at close).** Controller wave-close fixes
  (S-GT1/S-GT2 precedent): T1 stale forward-ref filename
  (`03_declaraciones-mensuales` → `03_pequeno-libro-regime`); GOQ-99
  annotation doubled prefix (write-back script artifact). Final
  whole-branch review + fix wave: see §5k/EXTRACTION_PLAN. Next session:
  S-GT5 COA/commercial plan doc.
