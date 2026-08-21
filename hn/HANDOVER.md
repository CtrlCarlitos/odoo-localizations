# HANDOVER — Honduras Session State & Continuation Guide

**For the next HN controller session.** Written 2026-08-20 after W1 (taxation
core), updated through round-4/D-H2/D-H3 + the merge, W2 fiscal-reporting, W3
facturación, W4 payroll, synthesis prep (master index + OQ registers),
S-HN1..S-HN4 synthesis waves + their merges, the V-HN1 VALIDATION WAVE
(merged to main 2026-08-20, thirteenth §4.6 run at `960df34`, root record
`f2eccbc`), and **V-HN1b (this refresh — in-corpus evidence reads
95_/96_/93_/94_/97_ with FR-067 PINNED + 22-A regime-0 + 97_ history rows;
S-HN5 scoping recorded as DEFERRED; acquisition wave: D. 112 FOUND via
Wayback-of-STSS + 154-2000 bono reglamento + D. 150-2008 + Acuerdo 345
acquired; next = evidence passes for 105_-108_ — the P2 aguinaldo unblock)**.
Read this fully before acting; it is the authoritative HN cross-session
memory (conversation context does not survive). Update it at every session
boundary.

**Bootstrap prompt for a fresh session:** `Read hn/HANDOVER.md and continue.`

---

## 1. Where you are

- **Worktree:** `.worktrees/hn-research`, branch `hn-research`. **Merges to
  date: 2026-08-19 (W1) and 2026-08-20 (W2; W3 at `c1f9fa8`; W4 at `d5a2f4b`;
  synthesis prep at `e106b1f`; S-HN1+S-HN2 at `6d1cfc3` w/ root record
  `b98dae1` — ninth §4.6 run; S-HN3 + R-H66 adoption at `00caef9` w/ root
  record `503ab9c` — tenth §4.6 run, zero conflicts, remote ref delete +
  re-push; **S-HN4 at `d05f2c1` w/ root record `7a40433` — eleventh §4.6
  run, 2 commits rewritten (`087e94f`→`3ee60c0`, `9890bda`→`d05f2c1`),
  zero conflicts, remote ref delete + re-push**). Rebase-then-merge per
  root HANDOVER §4.6, owner-executed; main carries HN evidence through
  EVID-333, the master index, and the S-HN1/S-HN2/S-HN3/**S-HN4**
  requirements incl. adopted R-H66.**
  The cross-country canon D15-D19 was adopted at the W1 merge — HN's
  D-H2/D-H3 are country instantiations of D16/D18 (see
  `shared/docs/regulatory-change-management.md`,
  `shared/docs/go-live-readiness.md`). **Country work model (binding):** every
  country works in its own branch+worktree; `main` = integration; merge at
  milestones by owner decision. NEVER touch `sv/`, `gt/`, or root
  `HANDOVER.md` from this branch; `hn/` + specs are ours.
- **Mission:** bootstrap the Honduras Odoo localization per
  `docs/superpowers/specs/2026-08-18-hn-source-research-design.md`
  (e-invoicing IN scope; acquire+register; evidence waves authorized by the
  phase-extension note in that spec). Procedure:
  `shared/docs/requirements-extraction-procedure.md`.

## 2. Read order for a new session

1. THIS file
2. `hn/EXTRACTION_PLAN.md` — wave log (W1a-W1f taxation + W2a/W2b fiscal
   reporting + W3 facturación + W4 payroll + synthesis prep + **S-HN1/S-HN2/
   S-HN3/S-HN4 synthesis DRAFT-COMPLETE**), reading order, risks,
   **Decisions (D-H1/D-H2/D-H3 binding; D-H2/D-H3 = D16/D18
   instantiations)**
3. **`hn/.extractions/00_MASTER_INDEX.md` — THE synthesis lookup (built
   2026-08-19): authority orders per topic, 18 EV file keys, 43 clusters
   (T1-T12/F1-F11/E1-E8/P1-P12) with Governing EVIDs/LB/crossrefs, R-H1..65
   resolved-contradictions ledger, OQ registers C1-C4 (~227 open), S-wave
   plan. READ BEFORE ANY SYNTHESIS WORK.**
4. **`hn/requirements/taxation/00_index.md` + `hn/requirements/e-invoicing/
    00_index.md` + `hn/requirements/fiscal-reporting/00_index.md` +
    `hn/requirements/payroll/00_index.md` — S-HN1/S-HN2/S-HN3/S-HN4
    deliverable indexes (248 + 155 + 362 + 313 FRs, wave rulings; R-H66
    adopted 2026-08-20). READ BEFORE THE VALIDATION WAVE (COVERAGE.md
    consumes all four; payroll cites taxation/04 plantilla +
    fiscal-reporting/02 código-111 interfaces and owns the SMM-promedio
    rows).**
5. `hn/RESEARCH.md` — research dossier: sites, fetch recipes (§6), hint
   layer w/ corpus verification (§7), open leads (§5, incl. W2+W3+W4
   harvests)
6. `hn/sources/README.md` — registry, 103 files (01-104, 103 reserved-unused),
   full provenance + mislabel-correction notes (**10 incidents to date**)
7. Evidence files in `hn/.extractions/*.evidence.md` (committed): `01_`
   (ISR, EVID-001..015), `02_` (ISV, 016..026), `03_` (CT, 027..038),
   `04-21-22_` (D.17-2010 family, 039..053), `07-12+11_` (tables+plantilla,
   054..056), `05+23+79+80_` (taxation closers, 057..071),
   `13-20_fiscal-procedures.evidence.md` (W2a, 072..090),
   `29+30+46-49+68+74+75_ISR-annual.evidence.md` (091..110),
   `31-42+71_retenciones.evidence.md` (111..129),
   `43-45+69+70+72+73_ISV.evidence.md` (136..150),
   `50-55_selectivo.evidence.md` (151..158),
   `56-62_contribuciones.evidence.md` (163..173),
   `63-67_informativas.evidence.md` (175..185),
   `24-26+76-78_facturacion.evidence.md` (W3, 186..214),
   `82-84+90-92+101+102+104_salario-minimo-13-14.evidence.md` (W4a, 215..240),
   `81+87+88_IHSS.evidence.md` (W4b, 250..274),
   `27+28_RAP-fondo.evidence.md` (W4c, 275..289),
   `85+86_codigo-trabajo.evidence.md` (W4d, 295..333). **EVID numbering is
   corpus-global, next = 362. OQs are per-file/per-doc at evidence-file end
   (~227 open).**

## 3. State: corpus (research phase COMPLETE)

107 registered files, every one page-1 verified (01-108; gap 103
reserved-unused; 105-108 acquired 2026-08-20 post-V-HN1 — **105_ = D. 112
THE aguinaldo law**, recovered via Wayback of the official STSS upload,
correcting the round-5 "routes exhausted" claim; 106_ = D. 43-97 + Acuerdo
STSS-154-2000 bono reglamento; 107_ = D. 150-2008 pact; 108_ = Acuerdo 345
Comisiones SMM; a duplicate D. 103 upload was discarded md5-identical to
104_). Structure:
- **Laws/consolidations:** ISR D.L. 25 (`01_`, hasta SAR-07-2025), ISV
  D.L. 24 (`02_`, hasta D.L. 59-2022), CT D. 170-2016 (`03_`, hasta
  D. 180-2020), D. 17-2010 + Reglamento 1121-2010 + D.28-2019 interp
  (`04_/21_/22_`), Ley Eficiencia D. 113-2011 (`05_`)
- **ISR tables FY2022-2026** (`12/10/09/08/07_`) + **plantilla 2026**
  (`11_` XLSX = the withholding computation contract)
- **Fiscal reporting:** DJIMR SAR-238-2024 (`14_`), DMC chain
  (`15/16/17/20_`), tarjetas mods (`19_`), compras eventuales (`18_`),
  EEFF SAR-619-2024 (`13_`), 42 per-código Ayudas/Generalidades (`29-75_`)
- **Facturación:** Acuerdo 481-2017 consolidado (`24_`) + 189-2014 hist
  (`25_`) + 817-2018 (`26_`) + workflow helps (`76-78_`)
- **Payroll (W4-complete):** IHSS D. 48-2024 (`81_`, rates OCR'd) + Ley
  IHSS (`87_`, OCR'd — native layer junk) + incapacidad (`88_`); RAP fondo
  D. 47-2024 (`27_`) + D. 40-2026 (`28_`); salario mínimo bienios 2023
  (`83/84_`), 2024-2025 (`82_`), **2026-2027 CURRENT (`90_` OCR'd + `91_`
  tabla + `92_` bono + `101_` 2022/2023 vintages + `104_` D.103 machinery +
  `102_` 14th-month reglamento)**; CT D. 189-1959 (`86_`, vintage through
  D.278-2013) + **85_ = D.93-2021 PENAL-side derogations only (9th mislabel
  — NOT CT, no CT gap ever existed)**
- Misc: amnistía D. 7-2026 (`06_`), ISR reforms (`79/80_`), Adulto Mayor
  family (`95/96_`), 22-A chain (`80/93_`), selectivo IPC chain
  (`98/99/100_`), ISR-reglamento ancestor 464-1990 (`94_`), D.194-2002
  original (`97_`). LJT still unapproved (Sep-2025 newest SAR post).

## 4. Key findings (do not re-derive)

- **E-invoicing reality:** NO national XML/DTE regime. Paper regime
  (CAI/rango/vigencia, Arts. 59-61) administered digitally + a statutory
  **Sistema de Emisión Electrónica (SEE) with per-document CAEE** (Arts.
  50-58, gradual mandatory incorporation per SEFIN calendarización) —
  technical docs NOT public (lead 1). D. 17-2010 L-Art 57 = regime's
  statutory birth.
- **Document taxonomy (Arts. 5-8)**: Comprobantes Fiscales (Factura,
  Prevalorada, Ticket, Recibo Honorarios, Boleta Compra, Constancia
  Donación) / Documentos Complementarios (NC, ND, Guías Remisión,
  Comprobantes Retención) / Otros. 16-digit correlativo =
  establecimiento(3, matriz=000)+punto de emisión(3)+tipo doc(2)+consecutive(8,
  wraps 99999999).
- **Withholding:** asalariados = annualize→deduct→table→÷months (plantilla);
  composite L257,493.16 sole-source gate; 12.5% services; 1% compras
  anticipo (retainer >L15M); OTCD cards 10%-of-tax/15% fallback; non-resident
  gross table 25/10 (current = `01_` Art. 5).
- **Rates:** ISR PJ 25%, PN 15/20/25 IPC-indexed annually; 22-A gross-minimum
  (≤L1B excluded, 1%/0.5% sectors); ISV 15%/18%/0; mora 3%/mo cap 36%;
  prescription 4/5/7y; multas = income-range × SMM-promedio fractions +
  ISR-late 5→25%/month escalator.
- **W2 fiscal reporting (do not re-derive):** Form 535 EEFF-prior gate from
  FY2024 (SAR-619-2024); DJIMR = monthly informativa PER retention código
  (25-code catalog), 10 días calendario, rectificativa auto-rectifies the
  determinativa; DMC = form 527, deadline **5 días calendario
  (SAR-237-2024)**; tarjetas 523 (SW informativa) + 215 (OVI determinativa,
  base = 10% of ISV − devolución 8%) file OUTSIDE the DJIMR catalog;
  compras eventuales = doc type 10 buyer-issued (rate unpinned — OQ);
  TP pequeños excluded ≤USD 1M; AS = 5% RNG>L1M (PJ-only), ATN = minimum tax
  over L3M exemption, both D.51-2003 (un-acquired — TOP lead);
  contribuciones: 504 1% / 502 1% / 503 0.5% monthly, 506 3.6% / 509 15%+0.5%
  floor / 511 15% / 107 10% annual; selectivo 203 = separate D.58-1982 tax;
  259 = 4% turística retention.
- **W2 conflicts (open OQs — never resolve silently):** GC non-resident
  retention 2% (46_) vs 4% (05_ Art. 14); ZOLITUR Art. 4 vs Art. 25; DMC
  manuals "8 días" vs gazette 5 (5d = record); 506-vs-509 cooperative
  boundary; 39_ ≡ 37_ (both código 135).
- **W3 facturación (do not re-derive):** D-H1 FR cluster evidence-complete.
  16-digit correlativo grammar + wrap rule; type codes 01/03(Ticket machine
  prefix 09)/04/05/06/07/08/10(Prevalorada)/11/12, **02 unassigned**;
  **code-10 collision: DEI-279-2015 "10 = Compras Eventuales" (introduced
  the 16-digit grammar) vs 481-2017 "10 = Prevalorada" — OQ-2, never
  implement 10 as both**; 189-2014 = 14-digit grammar → dual historical
  parser; CAI ledger contract (Arts. 59-63): per punto × doc type, ONE active
  rango, renewal T-2mo, vigencia ≤1y, consumo starts at Activada; emission
  gate = momento-de-emisión earliest-of (Art. 14) + vigencia/fecha límite;
  two-layer print contract; L50 consolidation (imprenta only); L10,000 ID
  threshold (SEFIN-modifiable, dated row); boleta compra 5%-of-opex +
  per-provider caps, no crédito; NC/ND origin triple; guía 12-motivo + SAR
  copy; retención comprobante at hecho generador (patronos exempt unless
  requested, EVID-200); no-utilizados 12 causes/10 días hábiles; topologies
  centralizado/regional/sucursal; SEE/CAEE = medium of autoimpresor, docs
  unpublished (lead 1); helps' Base-Legal sections defective — cite the
  reglamento.
- **W4 payroll (do not re-derive):** IHSS matrix = **IVM 3.5% employer /
  2.5% worker / 0.5% State (81_ Art. 1) + EM 5%/2.5%/0.5% (87_ Art. 55-A) ⇒
  worker 5.0%, employer 8.5%**; TWO regime ceilings (2024: 11,336.32 IVM /
  11,109.30 EM; 2025: both 11,903.13 — coincidence, not merger); post-2025 =
  JD per actuarial study (dated rows); "porcentajes sobre los techos" =
  drafting ambiguity, coherent reading min(salario, techo) per 55-B;
  **contribution BASE (13th/14th/OT inclusion?) delegated to unacquired
  Reglamento General — config flag, TOP lead**; riesgos profesionales rate
  not in corpus; incapacidad: NO cuarentena — days 1-3 employer salary,
  4-365 IHSS 66% + mandatory employer complement (RIT 71/73). RAP side:
  **STACKED fondo 4% + RAP 1.5% employer (=5.5%) + worker 1.5% retention
  above IVM techo, ≤15 días entero; base "salario ordinario" undefined in
  law (OQ); ceiling 3× top-SMM (instrument unnamed, OQ); fondo coexists-
  with-offset vs CT cesantía (despido injusto: compute, deduct saldo, pay
  excess; other causes: fondo 100% prima + 35%/75% complement floors, CT
  Art. 120 lit. f); vigencia 28-may-2024, no retro**. Ley RAP = doubly
  load-bearing (truncated transcription). SMM: bienio 2026-2027 % 6/6/7/7
  (2026) · 6/6/7/7.5 (2027), full tables pinned; 2027 IPC-escalator
  de-oficio + Jan-Apr-2026 retroactivity; **promedio ONLY in DGS companion
  tables (2026: L14,917.20 → 10×SMM cap L149,172; NOT the table mean — never
  recompute); 2025 (L13,985.16) + 2027 promedios NOT in corpus = OQ +
  DGS-print lead**; 14th month (102_): June, 30-jun year-gate 100%-else-
  proportional, average-of-ordinary-salaries base, small-employer SMM-average
  variant, proportional on exit; bono educativo ≤2×SMM, ≤15-worker
  exemption, non-salary. CT: **NO aguinaldo in the CT — D. 135-94 special
  law (TOP lead; subsumes D. 112)**; vacaciones Arts. 345-356 (10/12/15/20
  días laborables at 1/2/3/4+y; 6-month ordinary average ÷ days worked; no
  360 divisor CT-side); preaviso 24h/1w/2w/1m/2m; cesantía 10d/20d/1mo/yr +
  fraction, cap 25 months (15 for micro ≤10), ≥15y vol-quit 35% / death 75%,
  last-6-month average base; jornada diurna 8h/44h-worked paid-48, nocturna
  6h/36h +25%, OT ×1.25/×1.50/×1.75, ≤12h/day, OT ≤4×/week, planillas book
  OT separately; maternity 4+6w at 180-day average + top-up, nursing
  2×30min, unauthorized firing = 60 days + 10 weeks + 2× rests; **NO general
  final-pay deadline in CT (negative — LB elsewhere)**; extra finds: Art.
  95.12-13+60-A mandatory union/non-union/coop deductions; Art. 104 sickness
  half-pay schedule; 11 paid feriados (8 fixed + 3 Semana Santa, R-H70) ÷6 average + collision rule; Art. 368
  pay-frequency caps; "salario completo" (ord+OT) indemnity base; Libro de
  Salarios (Art. 380). **85_ = 9th mislabel: D.93-2021 derogates PENAL
  (D.130-2017, 31 arts) + CPP + Lavado — ZERO CT articles; penal numbers
  collide with LIVE CT payroll articles — guard table EVID-333.**
- **S-HN1/S-HN2/S-HN3 synthesis (2026-08-20, do not re-derive):** taxation 7
  files (HN-TAX-FR-001..281, 248 FRs/54 OQs) + e-invoicing 4 files
  (HN-EINV-FR-001..175, 155 FRs/26 OQs) + fiscal-reporting 11 files
  (HN-FREP-FR-001..393, 362 FRs/154 LBs/188 ACs/169 OQs +
  `djimr_retention_codes.csv` 25 codes), controller-verified 11/11 + 11/11.
  Rulings made at synthesis: 10-SMM caps = EXCESS-ONLY never cliff (plantilla
  IF semantics, `01_ OQ-4` resolved); FY2026 promedio cap = L149,172.00
  (R-H47 applied); DAR superseded by DJIMR (R-H31 applied); bad-debt cap =
  10%-of-closing-AR (evidence over brief); L30k@60 senior tier attributed to
  D. 199-2006 per plantilla citation — row activation-blocked until acquired.
  **R-H66 (territoriality: worldwide pre-2017 / territorial 2017+,
  dated rows) ADOPTED by product owner 2026-08-20 — encoded in
  taxation/01 FR-004, OQ-001 resolved; rows stay reversible if a contrary
  instrument lands.** S-HN3
  specifics: S-HN1/S-HN2 rates consumed by id throughout; F9 IPC chain
  (98_/99_/100_) = the ONE direct-cite exception (no evidence pass,
  page-1-verified at synthesis, values controller-re-verified vs raw txt —
  cigarettes 539.00/571.34/600.99 chain + per-liter tablas as dated rows);
  only yes-blocking wave OQ = 506-vs-509 boundary (`60_ OQ-1`); open
  conflicts carried (GC 2%-vs-4%, ZOLITUR Art.4-vs-25, 138 duality, 541/542
  drifts, 535 balance-only-vs-+GyP, 509 Mar-30-vs-3-meses, D.117-2021
  identity). New top acquisition LEAD from synthesis: Reglamento Ley ISR
  ("Acuerdo N°799", 5× cited corpus-wide). SEE sub-cluster = config-gapped
  placeholders (e-invoicing/04 FR-166..169), rest of E-wave evidence-complete.
- **S-HN4 payroll synthesis (2026-08-20, do not re-derive):** 10 files +
  `smm_tables.csv` (HN-PAYR-FR-001..398, 313 FRs/146 LBs/163 ACs/73 OQs),
  subagent-dispatched with pre-allocated ranges, controller-verified 10/10
  structural + strict verbatim bank-check (5 one-word LB defects found+fixed:
  correspondientes/se refieren/establecer/recibe/crédritos). P1 OWNS the
  SMM dated rows + DGS promedio rows (R-H47 — the sole feed of taxation/04
  FR-134; print_status discipline: printed/derived_gap/reconstruction_
  blocked, never a derived amount in an amount cell; 2026 promedio
  L14,917.20 + maquila 12,930.07 verified in-CSV). P2 aguinaldo =
  config-gapped placeholders (the wave's ONLY yes-blocking OQ — D. 135-94 +
  Acuerdo 201-96 unacquired). IHSS matrix/ceilings/min-base per R-H49/50/51
  encoded; base composition = config flag (LI Art. 100). RAP stack
  R-H55/56/58 encoded with three-bases-never-share. CT family encoded with
  the R-H57 mislabel guard (EVID-333) in file 10. Evidence-over-brief
  corrections kept: feriado collision = two-holidays-one-day (paid even on
  Sunday); Art. 349 ¶2 proportional leg = employer-imputable-cause only;
  cesantía fraction = Art. 120 lit. c; Art. 104 rule-4 no half-salary
  qualifier; Art. 21-A proportionality sentence ends mid-print.

- **V-HN1b in-corpus reads (2026-08-20, do not re-derive):** `95_`+`96_`
  (EVID-337..348): **FR-067 PINNED + ACTIVATED** — L30k@60 = D. 199-2006
  **Art. 30 num. 14** (own-law "crédito adicional", NOT an ISR amendment),
  valid_from **10-ago-2007**; 96_ (D. 45-2025) does NOT touch deductions;
  carries = taxation/02 OQ-009 (**D. 59-2023 G 14-feb-2024 intermediate
  reform UNACQUIRED = new top lead**; beneficiarios = 60+ OR any-age
  jubilado vs plantilla 60-turn gate; stacking = plantilla-only practice,
  no statutory bridge; créditos-vs-deducción mechanics). `93_` (EVID-350/351):
  **R-H72** — 22-A FR-082 regime 0 (FY2017 = original D. 278-2013 Art. 9
  rules per D. 31-2019 authentic interp: L10M trigger, 1.5%/0.75% floors;
  gazette = G 34,932, catalog "34,934" in error). `97_` (EVID-355/356):
  **R-H73** — original Art. 14 conditioned the 65+/L350k exemption on 5
  consecutive Art. 22-b periods; D. 59-2020 deleted it (FR-068 history
  rows). Coverage after V-HN1b: 107 rows = 101 cited + 6 N/A; LBs 483.
- **Decisions:** **D-H1** (binding, EXTRACTION_PLAN): one journal per company
  via `l10n_latam_invoice_document`; sequence key = (establecimiento→
  `stock.warehouse`, punto de emisión→child emission point, doc type→
  `l10n_latam.document.type`); emission point NOT on journal;
  user↔emission-point matrix = operational FR only. **D-H2** (2026-08-20,
  binding): temporal validity — dated rows resolved by HECHO-GENERADOR/
  period date; payroll key = (payslip period, worker attributes,
  birthday-year rules); HARD BLOCK emission outside CAI vigencia; historical
  = flagged read-only imports; payroll corrections recompute with
  ORIGINAL-period rows; filed periods write-protected; regime cutovers =
  dated config rows. **D-H3** (2026-08-20, binding): go-live ingestion =
  current-FY fiscal-document detail (read-only, original CAI numbers/dates) +
  prior-years aggregates; reconcile vs PREVIOUS system's SAR filings;
  payroll = monthly aggregates per contract (hire-date depth fondo/cesantía/
  vacaciones, FY-start depth ISR/13th/14th); stock/banks = opening balances.

## 5. Gotchas & verified lessons

- **Wrong-domain sites:** congresonacional.gob.hn / stss.gob.hn / upap.gob.hn
  / cpmcp.hn / enag.hn = NXDOMAIN. Real: `congresonacional.hn` (no law
  library), `www.trabajo.gob.hn` (STSS WordPress), **`enag.gob.hn` = Gaceta
  Digital 2015-2026** (recipe: `/index.php/gaceta-digital/<year>/<mes>` →
  `/index.php/gaceta-digital/<id>/download`). TSC biblioteca fully crawled.
- **SAR downloads:** resolve fresh wpdmdl from `/download/<slug>/` page
  (tokens rotate); some slugs dead. **SAR REST search endpoint works
  (wp-json/wp/v2/search) but only indexes posts/pages — validated empty for
  aguinaldo/séptimo día while returning hits for salario; absence of results
  ≠ absence on site (catalog crawl is the real check).**
- **OCR (proven recipes):** scanned gazettes OK at default PSM 6; TABLES
  need `gs -r400 pnggray` + `tesseract --psm 4` (proven on tabla acuerdos +
  91_/92_ rama columns); mojibake text layers (81_ rates, 90_ full, 87_
  font-mangled) re-covered by PSM 6 at 400dpi — sidecar `.OCR.txt` files
  live in hn/.extractions/ and are the AUTHORITATIVE text for those pages.
  102_'s run-on damage is legible as-is.
- `11_` plantilla formulas read fine via openpyxl (not protected).
- IHSS site needs full browser UA. Bing/DDG useless for .hn; navigate
  catalogs directly.
- **Registry glosses and catalog TITLES can mislead — 10 incidents to date**
  (29_/09_/15_ SV; 05_, 94_, 101_-server-filename, 20_, 52_, **85_** HN —
  85_ was believed "CT derogations" for two sessions before W4d read it:
  Penal-only. Title ≠ content; the end-to-end read is the authority. Numeric
  article collisions across codes (Penal vs CT) make "derogates Art. N"
  claims worthless until the code is named in the text.)
- **Manuals can be stale vs gazettes (W2b):** the gazette text is the
  record; flag manual conflicts as OQs. Same class: 101_ p.4 caption
  misprints the 2023 table as "AÑO 2022"; 102_ p.1 prints D. 135-94 "de
  fecha 12 de Octubre de 1991 [sic]" (print error for 1994).

## 6. Next actions (ordered)

1. **V-HN1 validation wave: COMPLETE 2026-08-20 (see EXTRACTION_PLAN wave
   log for the full adjudication).** Deliverables: `hn/requirements/
   COVERAGE.md` (generated by committed `hn/scripts/build_coverage.py`;
   103 rows = 98 cited + 5 N/A; script gates all pass) + four adversarial
   reviewers' findings adjudicated (R-H67..R-H70 in master index; `89_`
   evidence pass EVID-334..336 with the 10th gloss incident — Art. 2
   aguinaldo interp, payroll/02 FR-087 + OQ-007 conflict vs ISR 10.h
   carried; 95_/96_ in-corpus-unread status fix; whole-base/cliff/feriados
   evidence fixes; EINV FR-085/086 + FREP FR-076 + PAYR FR-087 additions).
   All four topic indexes → approved. **NEXT = owner merge decision; then
   S-HN5 thin closes at milestone (Código de Comercio still unacquired)
   and/or the acquisition wave. DONE same session: V-HN1b reads + S-HN5
   scoping (DEFERRED pending Código de Comercio + Ley RAP — see
   EXTRACTION_PLAN) + acquisition wave round 6 (105_-108_ acquired).
   NEXT: evidence passes for 105_-108_ (105_ unblocks the P2 aguinaldo
   sub-cluster — payroll/02 OQ-001), D. 59-2023 fetch (ENAG Feb-2024),
   then D. 135-94/201-96 + Acuerdo 799 + Reglamento General IHSS + Ley RAP
   (§6.2 queue).**
2. **Acquisition queue (W2+W3+W4+S-wave lead harvests, RESEARCH §5 + master-index
   C-registers + synthesis OQs):** TOP = **D. 135-94 + Acuerdo 201-96
   (aguinaldo/compensación social — the 13th-month statutory home; P2 + S-HN4
   blocker)** + **Reglamento Ley ISR "Acuerdo N°799" (NEW top from S-HN1 —
   depreciation/personal-deduction/vinculación mechanics, 5× cited)** +
   **D. 199-2006 original (L30k@60 senior-tier anchor, activation-blocked
   row)** + **Reglamento General IHSS (contribution-base definition)** +
   **Ley RAP D.L. 107-2013 (doubly load-bearing)** + Ley Equidad Tributaria
   D. 51-2003 (AS/ATN + tarjetas Art. 18) + Acuerdo SAR-236-2024 + DGS SMM
   companion prints (2022-2025 + 2027 when exists) + D. 58-1982 + D. 131-98
   + TP family (D. 232-2011 + 027-2015 + DEI-SG-004-2016) + contribuciones
    statutes + D. 54-95 + Código de Comercio + DEI-9382-J-2003 I-VIII + W3
    adds (462-2014, 424-2018, post-2017 compras-eventuales instrument if any)
    + riesgos-profesionales reglamento. S-HN3 sharpened the LSP statutes
    queue: D. 105-2011 + Acuerdo 1775-2011 + D. 31-2018 (LSP portion) +
    D. 53-2015/D. 92-2015 + D. 131-2018 (the 506-vs-509 boundary = the only
    yes-blocking S-HN3 OQ); also Acuerdo 034/99 (542 threshold) and the
    SAR-236-2024 DÉCIMO OCTAVO print. D. 112 = routes exhausted (mirror-only
    at synthesis). Most SAR-catalog fetchable (recipe §6).
   3. **R-H66 territoriality ruling: RESOLVED — adopted by product owner
      2026-08-20 (worldwide pre-2017 / territorial 2017+; taxation/01
      FR-004 dated rows; master-index Section B row 66; rows reversible).
  4. **Merge to main at milestone:** owner decision; rebase-then-merge; never
     force-push (root HANDOVER country model). Branch head after S-HN1/S-HN2
     commit = the synthesis-wave base; future waves branch from here.

Session state at stop (2026-08-20, S-HN4 close + eleventh merge): evidence
COMPLETE through EVID-333 (~227 open OQs); corpus 103 files; W1-W4 +
synthesis prep + all four S-waves committed/merged to main (**S-HN4 at
`d05f2c1`, eleventh §4.6 run, root record `7a40433`; R-H66 adopted**).
S-HN4 payroll = 10 files + `smm_tables.csv`, HN-PAYR-FR-001..398 = 313
FRs/146 LBs/163 ACs/73 OQs, controller-verified 10/10 structural + strict
verbatim bank-check with 5 one-word LB fixes. **Next = validation wave
(`hn/requirements/COVERAGE.md` all four topics + adversarial review,
template Stage 5) + S-HN5 thin-close decision at milestone (or acquisition
wave in parallel — top: D. 135-94 + Acuerdo 201-96).**

## 7. Conventions (mirroring SV)

- Evidence: verbatim Spanish + gloss; candidate CRs + topic tags; doubts →
  OQs, never guesses. Per-file OQ numbering; corpus-global EVID (next=334).
  W2b + W4 + S-HN1/S-HN2 ran subagent-dispatched with pre-allocated EVID/FR
  ranges per family — proven pattern for large batches; controller verifies
  ranges + spot-checks verbatims afterward (done for W4: ranges + 8
  source-level spot-checks incl. all OCR-derived quotes; done for
  S-HN1/S-HN2: 11/11 structural verification + 5/5 verbatim spot-checks —
   script pattern in session log, keep re-using; done for S-HN3: 11/11
   structural (adapted script `/tmp/opencode/verify_hn_s3.py` pattern) +
   5/5 verbatim spot-checks + IPC-chain value re-verification + CSV 25-code
   match vs EVID-077; done for S-HN4: 10/10 structural
   (`/tmp/opencode/hn/s4/verify_hn_s4.py`, same pattern) + STRICT FULL
   verbatim bank-check — every quote-pair-bounded Spanish span ≥40 chars in
   every file vs the evidence bank, split on ellipses, guillemet-edge
   stripping: 372 spans PASS, 5 real one-word LB defects found+fixed, ~45
   residual checker flags adjudicated as artifacts (English spans, OCR-
   bracket resolutions, «» nesting, table reformat). The strict bank-check
   (`/tmp/opencode/hn/s4/spotcheck5.py` pattern) SUPERSEDES 5-sample
   spot-checks for future waves. NOTE: subagent empty-return anomalies now
   TWO shapes —
   (a) empty-return with file-on-disk (W2b/W4, twice), (b) empty-return with
   file ABSENT (S-HN3: 4 of 11 dispatches failed to deliver; simple re-
   dispatch succeeded all 4). S-HN4: 10/10 dispatches delivered (zero
   anomalies). ALWAYS verify disk state, never trust the
   return alone; re-dispatch is the fix for shape (b).
- `.gitignore`: `hn/.extractions/*` ignored EXCEPT `*.evidence.md` +
  `00_MASTER_INDEX.md` (**created 2026-08-19 — committed; update it at every
  wave/milestone that adds EVIDs, rulings, or resolves OQs**).
- Commits: short imperative, no emojis; push after each wave.
- Registry additions continue numbering from `105` (103 reserved-unused);
  page-1 verify everything. **10 mislabel incidents to date** — title-vs-
  content discipline on EVERY acquisition AND every evidence read.
- **Manuals can be stale vs gazettes (W2b):** gazette text is the record.
- **OCR sidecars:** for any file with an `.OCR.txt` in `.extractions/`, the
  OCR sidecar (not the native-layer txt) is authoritative for the damaged
  passages (81_, 87_, 90_, 91_, 92_ as of W4).
