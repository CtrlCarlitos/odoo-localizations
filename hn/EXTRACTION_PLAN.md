# Honduras — Requirements Extraction Plan

Execution plan per [shared/docs/requirements-extraction-procedure.md](../shared/docs/requirements-extraction-procedure.md).
Started 2026-08-19 (source-research pass complete). Status: active — **evidence
wave W1 COMPLETE 2026-08-20 (W1a-W1f; taxation core EVID-001..071); next W2
(fiscal reporting), preceded by lead-dig round 4**.

## Wave log

- **W1a (2026-08-19, DONE):** Ley ISR `01_` evidence (EVID-001..015, 6 OQs).
  Key: PJ 25% / PN IPC-indexed progressive (FY2026 table = `07_` +4.98%);
  22-A gross-minimum regime; dividends 10% w/ 100-day deemed-anticipo;
  12.5% services retention w/ composite L257,493.16 gate; NOL 3y/50%/sector;
  **13th AND 14th month each exempt ≤10 SMM promedio (Art. 10.h)**.
- **W1b (2026-08-19, DONE):** Ley ISV `02_` evidence (EVID-016..026, 4 OQs).
  Key: 15%/18%/0 rate matrix; ISV-in-price for final consumers; OTCD card
  10%-of-tax retention + 15% no-discrimination fallback; débito/crédito with
  4-month credit window + pro-rata; L250k simplified regime; Anexo I
  SAC-coded canasta; invoice-date-first taxable event.
- **W1c (2026-08-20, DONE):** Código Tributario `03_` (EVID-027..038, 4 OQs).
  Key: renta TERRITORIAL declaration (Art. 1.2 — tension w/ ISR Art. 2 →
  OQ); calendar-year + merger succession; earliest-of retention trigger;
  NIIF books anchor + 30-day posting; 40d/60d start-cese DJs; buzón
  electrónico; cuenta corriente + Feb depuración ≤1 SMM; prescription
  4/5/7y; formal-falta multa table (income-range × SMM fractions) + ISR-late
  5→25% escalator; **mora 3%/month cap 36% (Art. 163)**; RTN suspension;
  Art. 206 VOID.
- **W1d (2026-08-20, DONE):** D.17-2010 family `04_`+`21_` (OCR'd) + `22_`
  (EVID-039..053, 4 OQs). Key: dividend retention mechanics (agreement-date
  trigger, DAR); cédula alquiler 10% >L15k/property (m² proration);
  educación 10%; revaluación 6% + Superávit account; **1% compras anticipo**
  (L15M retainer gate, exemptions, waste-collector interp D.28-2019);
  L-Art 19 minimum-tax vs 22-A supersession OQ; selectivo vehicles 10-60% +
  Ecotasa outside ISV base; cigarettes L350/millar IPC+6%cap; beverages
  2010 per-liter bases; **L-Art 57 = facturación regime statutory birth
  (already contemplated "factura electrónica")**.
- **W1e (2026-08-20, DONE):** tabla series `07_-12_` + plantilla `11_`
  (EVID-054..056, 4 OQs). Key: five FY vintages OCR-recovered (2022-2026);
  **plantilla = computation contract**: annualize → deduct (40k/80k+30k@60+
  350k@65≤350k stack, pension contribs RAP/AFP/public) → annual table →
  ÷months prorate; 10×SMM excess-only caps (13th/14th); vacaciones 360-day
  divisor; DMR/código-111 export contract. New leads: Reglamento Ley ISR
  (Art. 51), STSS-308-2022, D.199-2006, D.194-2002.
- **W1f (2026-08-20, DONE):** taxation-core closers `05_` + `23_` + `79_` +
  `80_` (EVID-057..071, 5 OQs). Key: **05_ registry gloss was WRONG** (content
  ≠ impuesto mínimo/solidario — those = 22-A/51-2003 families; row + plan
  inventory amended): 05_ = devolución 8% ISV tarjetas (status OQ), OTCD
  complement origin (current text in 02_), **Arts. 5/10 VOID (RI-0763-2021)**,
  ganancias de capital 10% mechanics (per-transaction 10 días hábiles, Apr-30
  annual, non-resident real-estate 4% buyer retention, reorg exception),
  exonerations personalísimas/in-kind-only + SEFIN single-document, **RIT
  D.37-84 reformed text (suspension + guarantees + 5-year gate)**, no-simultaneidad,
  sacrificio-fiscal declaration, **general retention entero 10 días calendario
  anchor**; 23_ = Art. 206 CT void detail (5/10/20% litigation guarantee, void
  since 22-feb-2022 rubrica, erga omnes); 79_ = 65+ L80k deduction + ≤L350k
  exemption de pleno derecho (plantilla stack sources); 80_ = 22-A transition
  instrument (L300M/L600M→L1B) + D.105/199-2011 permanent (financial-transactions
  contribution = 05_ Art. 35 exception). **Taxation-core evidence COMPLETE**
  (EVID-001..071); new acquisition leads: D. 31-2019, Instructivo 461-2020,
  D. 199-2006/D. 194-2002 originals.
- **W2 (NEXT):** fiscal-reporting procedures `13-20_` + 42 Ayudas batched by
  family. Before that: lead-dig round 4 (RESEARCH §5).

## Context

- 85 sources registered (01-86, gap 85) in [sources/README.md](sources/README.md);
  every file page-1 verified. Research dossier: [RESEARCH.md](RESEARCH.md).
- No prior-project hint layer exists for HN (unlike SV's tuky-workspace import).
- NotebookLM validator: none yet (corpus young; revisit at first synthesis).
- Fiscal year = calendar year. Currency: lempira (HNL, L).

## Source inventory and decomposition

| # | Source | Governs | Reading units | Target topics |
|---|--------|---------|---------------|---------------|
| 1 | `01_Ley_ISR` (D.L. 25 cons. SAR-07-2025, 50 pp) | ISR: rentas, deducciones, tasas 25/30%, retenciones (Arts. 20-23), 22-A asalariados, ganancias de capital (23-24), renta extranjera | Art. 1-9 concepts → taxation; Art. 10-18 deducciones → taxation; Art. 20-31 retenciones/pagos a cuenta → taxation + payroll; anexos → taxation | taxation, fiscal-reporting |
| 2 | `07/08/09/10/12` (tabla series + plantilla 11) | Asalariados progressive scale vintages FY2022-2026 (IPC-indexed from 2023) | each as data; 11_ formulas = computation semantics | taxation, payroll |
| 3 | `04/21/22/80` (D. 17-2010 + Reglamento + interp + 22-A reform) | Renta de capital 10%, retención 1% anticipo, impuesto neto base | whole each | taxation |
| 4 | `05_Ley_Eficiencia` (D. 113-2011 cons. Jan-2022) | Devolución 8% ISV tarjetas + OTCD complement origin; ganancias de capital 10% mechanics; exonerations discipline; RIT D. 37-84 reformed text; general retention entero anchor (gloss corrected W1f — NOT impuesto mínimo/solidario) | whole | taxation, special-regimes |
| 5 | `02_Ley_ISV` (D.L. 24 cons. D.L. 59-2022) | ISV 15%, base, exenciones Art. 15, débito/crédito, retenciones Art. 8 | Art. 1-8 core → taxation; Art. 15 exemptions → taxation; regimen simplificado → taxation | taxation, fiscal-reporting |
| 6 | `03_Codigo_Tributario` (D. 170-2016 act. 2020) + `23_sentencia` | RTN, obligaciones, declaraciones, prescripción, sanciones, deberes formales; Art. 206 VOID | libros/deberes → all; sanciones → taxation; RTN → all | all |
| 7 | `24/25/26/76/77/78` facturación stack + `18_compras_eventuales` | Régimen de facturación: documentos fiscales, CAI/rangos/vigencia, imprentas, autoimpresores (máquinas registradoras + sistemas computarizados specs), **Sistema de Emisión Electrónica + CAEE (Arts. 50-58)**, authorization procedure (Art. 59-61), compras eventuales | `24_` whole: T. I-II defs + documentos → T. IV medios (imprenta/autoimpresor/SEE) → T. V autorización → T. VI imprentas registro | e-invoicing |
| 8 | `14/15/16/17` (DJIMR, DMC chain) + `19/20` (tarjetas/retenciones mods) | Monthly informativas: retenciones detail + compras detail; ISV card-retention procedure | whole each | fiscal-reporting |
| 9 | `13_SAR-619` + `67_Ayuda_EEFF` | EEFF previo a DJ ISR (FY2024+) | whole | fiscal-reporting, chart-of-accounts |
| 10 | `29-75` Ayuda/Generalidades (42 files) | Per-código declaration mechanics (102/103/106/107/111-138/152/154/201-217/259/502-545) + regime overviews | per-código, batched by family (ISR annual / retenciones / ISV / selectivo / contribuciones / informativas) | fiscal-reporting |
| 11 | `81/27/28` (IHSS aportaciones + RAP fondo reserva + regularización) + `87_Ley_IHSS` + `88_Regl_Incapacidad` | 2024 social-security architecture: IHSS ceilings/rates, RAP-IVM 1.5+1.5, fondo reserva 4%; law-level IHSS text (scanned); sick-leave subsidy mechanics | whole each | payroll |
| 12 | `82/83/84` salario mínimo instruments | Wage floors: sector tables 2023, bienio 2024-2025 | tables as data | payroll |
| 13 | `86_Codigo_Trabajo` (D. 189-1959, 271 pp) | Jornada, salario, aguinaldo (13th), vacaciones, cesantía/preaviso (vs RAP fondo), terminación, mujeres/menores | Books: contrato/jornada/salario → payroll units; prestaciones (T. II) → payroll; SMT (sindicatos) skim | payroll, commercial-legal |
| 14 | `06_D.7-2026`, `75`, `22`, `79/80` misc | Amnistía (ancillary), suspensión PN, interp Art. 19, reforms | light reads | taxation |

## Reading order

Dependency-aware (SV-proven pattern: core law vocabulary first, reporting on
top, payroll parallel, facturación standalone):

1. **Foundations — taxation core**: ISR (1) + tabla series (2) + D.17-2010
   family (3) + Eficiencia (4) → ISV (5) → CT (6). Everything cites these.
2. **Fiscal reporting**: DMR/DJIMR + DMC (8) → Ayuda per-código (10) →
   SAR-619/EEFF (9). Needs ISR/ISV concepts in place.
3. **Facturación** (7): standalone; can run parallel after (1).
4. **Payroll**: tabla/retención consumer side rides (1-2); then IHSS/RAP
   architecture (11) → salario mínimo (12) → Código del Trabajo (13).
5. **Chart of accounts**: thin — Código de Comercio (NOT yet acquired, open
   lead) + EEFF inform (9); decide whether a wave is warranted at synthesis.
6. **Closers**: misc (14), special regimes (later corpus additions).

## Topic map (source unit → topic)

| Topic | From |
|-------|------|
| `taxation/` | 1, 2, 3, 4, 5, 6(partial), 14 |
| `fiscal-reporting/` | 6(partial), 8, 9, 10 |
| `e-invoicing/` | 7, 18_ |
| `payroll/` | 2(partial), 11, 12, 13 |
| `chart-of-accounts/` | 9 + Código de Comercio (open) |
| `commercial-legal/` | 13(partial) + Código de Comercio (open) |

## Known risks

- **Scanned/no-text-layer sources (OCR needed)**: `04_` (D. 17-2010), `21_`
  (Reglamento 1121-2010), `87_` (Ley IHSS). Damaged text layers: `81_`
  (D. 48-2024 rates page), `26_` (partial mojibake). ISR tables in
  `07_/08_/09_/10_/12_` print as images — **OCR feasibility CONFIRMED
  2026-08-19**: gs 400dpi + tesseract PSM 4 recovered the full SAR-01-2026
  FY2026 scale (exentos ≤ L228,324.32 / 15% ≤ L348,154.10 / 20% ≤
  L809,660.75 / 25% beyond; minor spacing noise only). `11_` plantilla
  formulas remain the cross-check.
- **CT consolidation currency (UPDATED 2026-08-19)**: `03_` stops at D. 180-2020;
  the SAR catalog's complete post-2020 CT instrument set = **D. 117-2021
  (interpretación Art. 113.1 — acquired as `89_`)** + the Art. 206 sentencia
  (`23_`, void). Known gap CLOSED at research level; still verify per-article
  at evidence (SV SOQ-22 lesson — catalogs can under-report).
- **Código del Trabajo vintage**: `86_` print's consolidation date unknown —
  pin key articles (aguinaldo 376-family, vacaciones 328-family, cesantía,
  preaviso, jornada) against reform chain; D. 93-2021 derogations are
  repeal-only (numbered articles dead — do not implement; list in `85` gap).
- **IPC-indexed table vintages**: FY2026 table (SAR-01-2026) is operative;
  each annual FR must carry valid_from/valid_to — dated rows, never replace
  (SV CAT-013 lesson). Watch for SAR-xx-2027 (Jan-2027) for FY2027.
- **Salario mínimo 2026-2027**: bienio 2024-2025 still current (Feb-2026
  evidence via SAR-43-2026); successor instrument watch — wage floors are
  dated data.
- **D. 48-2024 rate split**: ceilings captured; the EM/IVM rate articles sit
  in the damaged-text page — OCR before any FR trusts a rate value. The
  Ley Seguro Social itself (D. 140-1959 + D. 80-2001) is only on IHSS's KB
  pages (open lead) — capture if payroll wave needs law-level text.
- **RAP framework**: Ley RAP D.L. 107-2013 full text not acquired — `27_`
  Art. 16 transcription covers the operative payroll articles (42/43/61);
  acquire the full law before any deeper RAP FRs.
- **No retenciones-master reglamento**: HN retenciones live in Ley ISR Arts.
  20-23 + D. 17-2010 + per-código helps + DJIMR — do not expect an SV-anexo
  style single instrument.
- **La Gaceta archive absent**: gazette originals only via SAR republications
  (fine — official copies with gazette numbers); pin publication dates from
  the PDFs themselves.
- **SEE technical documentation absent**: the CAEE algorithm/specs and the
  incorporation calendarización (Acuerdo 481-2017 Arts. 57-58) are not
  publicly posted — SEE FRs can only cite the reglamento's own text until the
  docs are acquired (open lead 1, RESEARCH.md §5). Hint-layer recollection
  (CAI/ranges/expiry/overlap/exhaustion) is corpus-confirmed — see RESEARCH.md
  §7; exhaustion-alert FRs are operational derivations, flag as such.
- **LJT bill**: if passed, taxation core needs a supersession pass before
  synthesis — check status at wave start.

## Process notes

- Waves follow the shared procedure: extract → evidence → synthesis (SDD) →
  coverage. Evidence files land in `hn/.extractions/` (git-ignored except
  committed analysis artifacts — mirror SV's `.gitignore` exceptions when the
  master index is created).
- Registry additions continue numbering from 87 (`sources/README.md` §Numbering).
- Fetch recipes: RESEARCH.md §6.

## Decisions (binding for HN synthesis)

- **D-H1 (2026-08-19, product owner): Odoo journal architecture uses
  `l10n_latam_invoice_document`** — ONE journal per company carrying multiple
  `l10n_latam.document.type` entries, NOT one journal per document type.
  Consequences for synthesis:
  - Odoo Mapping sections model the facturación document taxonomy
    (24_ Arts. 5-8: Comprobantes Fiscales / Documentos Complementarios /
    Otros Comprobantes) as `l10n_latam.document.type` records, not as
    journals.
  - Sequences attach at document-type level (per punto de emisión), aligning
    with the CAI rango-autorizado + 16-digit correlativo regime (Art. 16
    structure: establecimiento/punto de emisión/tipo de documento/talomera +
    secuencia) — the CAI/authorization ledger keys on
    (punto de emisión, document type), never on journal.
  - **Numbering-structure Odoo mapping (design guidance, product-owner
    prior implementation; statutory anchor = 24_ Art. 10 num. 7 + Arts.
    48-49, 61):** the sequence identifier's two location segments map to
    inventory structures — **establecimiento ("sucursal") →
    `stock.warehouse`** (company-level branch code, casa matriz = 000;
    NOT `stock.location`), and **punto de emisión ("caja") → a child
    emission point of the warehouse** (each máquina registradora/dispositivo
    is its own punto de emisión per Art. 61; Art. 49 places puntos fijos
    within establecimientos). Synthesis must reconcile this with
    D-H1's document-type-level sequences: the full sequence key is
    (establecimiento, punto de emisión, document type) = (warehouse,
    emission point, `l10n_latam.document.type`). Note for evidence pass:
    "caja" is implementation vocabulary — the statute says punto de emisión.
  - **Emission point does NOT live on `account.journal`** (prior
    implementation put the terminal on both journal and move — incompatible
    with one-journal D-H1): it belongs on the move / a dedicated emission-
    point entity feeding the sequences. A **user ↔ emission-point
    authorization matrix** (per prior customer practice) is a legitimate
    operational-internal-control FR candidate — label non-statutory
    (24_ has no operator restrictions; hook = 76_ "acreditación de
    responsables"). See RESEARCH.md §7 item 3.
  - Cross-country propagation (GT/SV): NOT decided here — this session owns
    HN only; raise at merge for the product owner to carry into the other
    countries' plans.

- **D-H2 (2026-08-20, product owner; brainstormed in-session): temporal
  validity — dated rows + hecho-generador resolution + hard emission gate.**
  The mechanics Odoo adopts for start/end-dated tax, facturación, and payroll
  regimes. Binding for ALL HN synthesis; inherits repo-wide D9/D11/D12
  (freeze-at-filing, additive dated data, supersession-map discipline):
  1. **Dated rows everywhere.** Every statutory value (ISR PN scale vintages,
     22-A thresholds, deduction stack, selectivo IPC chain, SMM bienios,
     SMM-promedio values, IHSS ceilings, RAP/fondo rates, mora/multa bases)
     ships as data rows with `valid_from`[/`valid_to`], additive-only, never
     replaced in place (SV CAT-013 lesson). **Resolution date = the hecho
     generador / period date of the computation** (move date, payslip period,
     declared period) — never "today". Payroll resolution key = (payslip
     period, worker attributes): the D.59-2020 65+ carve-outs activate in the
     worker's birthday year.
  2. **Emission gate — HARD BLOCK (user decision 2026-08-20; supervisor
     override explicitly rejected).** A fiscal document cannot be posted
     unless its date resolves to a CAI range whose vigencia covers it for
     that (establecimiento, punto de emisión, document type). Backdating
     works only inside a historically-valid range — this is HN's "cannot
     emit in the past" rule; there is no transmission regime to gate.
  3. **Historical reconstruction = flagged read-only imports.** Legacy
     documents never emit, never count against range consumption or filed
     reports.
  4. **Payroll period correctness.** Paid slips frozen; corrections =
     refund-and-reissue computed with the ORIGINAL period's rows; monthly
     withholding uses the current-FY table (plantilla contract:
     annualize → table → ÷ months); the annual declaration uses the declared
     FY's own table. Annual-table availability gap (SAR publishes the FY
     table mid-January) = evidence OQ, never a guessed default.
  5. **Filed-period freeze (D9 kin).** Periods covered by a filed declaration
     are write-protected; corrections flow via rectificativa from the frozen
     snapshot, never silent edits.
  6. **Regime cutovers = dated config rows, not code** (SEE calendarización
     mandate date per company, amnistía D.7-2026 window, transitory
     authorizations e.g. Acuerdo 231-2020). `valid_from` = the instrument's
     vigencia date, which may be retroactive to publication (D. 59-2020 and
     the SETRASS-233-2026 bienio are the live examples — pin vigencia vs
     publication dates at evidence); `valid_to` backfilled only when a
     successor instrument arrives.
  Cross-country note: the SV session is deciding the same question in
  parallel (user relayed the identical prompt 2026-08-20). Mechanics are
  expected identical where surfaces overlap (dated rows, freeze,
  period-parameters); HN-specific = the CAI emission gate + SEE mandate
  rows. Reconcile wording at merge.

- **D-H3 (2026-08-20, product owner): go-live historical ingestion scope.**
  What Odoo ingests as read-only records when a company adopts the
  localization mid-year — no re-emission, no re-numbering, resolved with the
  rules in force at their ORIGINAL dates (D-H2 resolution). Depth decision:
  **current-FY document detail + prior-years aggregates** (prescription
  window 4/5/7y re-exports from legacy on demand):
  1. **Fiscal documents (facturas, CAI-numbered):** current FY imported
     detail-level, read-only, flagged — original CAI numbers, original
     dates, validated against the CAI ranges/dated rows in force at those
     dates; no sequence consumption; excluded from filings Odoo didn't
     make. Prior years: aggregates only.
  2. **Reconciliation method:** imported-document totals reconcile against
     the **monthly declarations the PREVIOUS system filed with SAR** (DMC
     compras / DJIMR retenciones / DJI mensual) — those filings are the
     authoritative aggregates; a go-live reconciliation report flags
     deltas. (HN has no MH-transmission counterpart to validate against —
     SAR's filed declarations ARE the external truth. Optional validator
     hook: Oficina Virtual Verificador de Documentos.)
  3. **Payroll exception (tenure-based prestaciones need history):**
     monthly aggregates per employee-contract, NOT payslips, two depths:
     (a) **from hire date** — contract start/end registry + monthly bases
     feeding fondo de reserva/cesantía-preaviso (CT-Art.-95 pact
     grandfathering)/vacaciones accrual; (b) **from FY start** — monthly
     taxable bases for the ISR annualized true-up + 13th/14th-month
     averages. Payslip-level import NOT required.
  4. **Stock & banks:** opening balances only (ledgers), per product-owner
     decision — no movement-level history.
  HN-specific note: there is no "pre-e-invoicing" medium question — the
  paper CAI regime is current; the depth question is how far back, answered
  above. SV parallel decision recorded in the SV session same day;
  reconcile wording at merge.
