# SV — Chart of accounts — Deferred tax bridge, first-time adoption & edition versioning

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file closes the wave's two-track spine: it is the fiscal-BY-ID hub where
every book-vs-fiscal difference recorded in files 01-07 lands as a deferred-tax
position under Sección 29 of the *Norma de Contabilidad NIIF para las PYMES*
(Accounting Standard for SMEs, 32_) — current tax (asset/liability measured at
enacted or substantively-enacted rates and legislation at the presentation
date), temporary differences as carrying amount versus tax base (the tax base
sourced from the taxation wave's fiscal registers BY FR ID, never re-derived
here), DTL recognition for all taxable differences with the initial-goodwill
and initial-recognition-neutral exceptions, DTA recognition for deductible
differences and the capital-loss 5-year ledger to the extent future taxable
profit is probable (the SV no-NOL jurisdiction constraint asserted in-file),
average-rate measurement over the taxation wave's progressive bracket feeds,
recovery-manner consistency including the Art. 42 sale-recovery rate and the
special-regimes exemption schedules for expected recovery, investment
differences, no discounting, the two-rate rule with the dividend withholding
charged to equity, the Pillar Two config-off exception, uncertain tax
treatments, presentation (deferred ALWAYS non-current) and the disclosure set;
then the first-time-adoption playbook of Sección 35 (transition-date
recognize/drop/reclassify/re-measure with adjustments to retained earnings,
the 35.9 mandatory exceptions, the 35.10 optional exemptions including the
deemed-cost elections, the transition reconciliations — with the D18
`is_historical` ingestion and D19 sequence-init/cut-over kin cited as shared
canon); and the edition versioning surface (2nd-2015 vs 3rd-2027-01-01 dated
regime rows with early adoption, Tabla A1 as the delta artifact, full-NIIF
horizon watch rows and the S1/S2 boundary note).

It does **not** cover: the fiscal computations themselves (ISR brackets,
capital-loss ledger mechanics, dividend withholding, asset depreciation
registers, exemption schedules — owned by the taxation and special-regimes
waves, consumed here BY FR ID only); the book measurement of the underlying
assets, liabilities, equity and revenue (files 03-07 by id); the ESF/P&L line
architecture and the (a)-(r) report lines (`02_coa-structure.md`); FX book
mechanics (`03_financial-instruments-fx.md`); consolidation and business
combinations (`07_groups-related-parties.md`); sustainability reporting
(out of scope, SOQ-52).

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling
R29): the operative framework LB = **32_** — *Norma de Contabilidad NIIF
para las PYMES, TERCERA EDICIÓN (Febrero 2025)*, IFRS Foundation official
Spanish translation, Sections 1-35 + Apéndice A (fecha de vigencia y
transición) + Apéndice B (glosario, integral part of the Norma); effective
2027-01-01 with early adoption permitted (A1; txt PAGE 315), cited by
section/párrafo as printed. **33_** (EY *Guía Práctica de NIIF y
Sostenibilidad 2024/2025*) is SECONDARY-ONLY authority per R29(a) and
EV33 OQ-1: it can NEVER be the sole LB of an FR; its LB role here is
limited to (a) version/horizon facts (NIIF 18/19 effective 2027-01-01 for
full-NIIF entities — the PYMES Norma is NOT amended by them) and (b)
documented full-NIIF-vs-PYMES contrasts; where 33_ and 32_ could diverge,
32_ governs without exception.

**SOQ-46 instrument-gap note (rides every FR in this file and this
wave):** the Norma itself is jurisdiction-neutral on who applies it —
"Las decisiones sobre qué entidades están requeridas o autorizadas a
utilizar las Normas NIIF de Contabilidad completas o la Norma de
Contabilidad NIIF para las PYMES recaen en las autoridades legislativas y
regulatorias y en los emisores de normas de las distintas jurisdicciones"
(Prólogo P12; txt PAGE 22) — and the SV adopting instrument (Consejo de
Vigilancia criteria per CC Arts. 443-444, or successor legislation) is
NOT in the corpus (commercial-legal/03 OQ-002 tracks the same
acquisition). Eligibility is therefore encoded as a CONFIG-GAP: the
deferred-tax/adoption engine ships against the Norma as printed, NO
quantitative SV thresholds or SV-specific adaptations are invented, and
the per-company framework flag inherited from
`01_framework-policies.md` SV-COA-FR-001 remains informational
configuration.

**Two-track invariant (binding, wave spine):** this file owns the
ACCOUNTING-book deferred-tax bridge ONLY. Every fiscal quantity it
consumes — bracket vintages, average and capital-gain rates, the
capital-loss ledger, the dividend withholding, the per-asset fiscal
register, the exemption schedules — is owned by its wave BY FR ID,
grep-verified in this file's FR lines, and NEVER re-derived, restated or
overridden here. Where book and fiscal treatment differ (depreciation,
provisions deductibility, revenue timing, FX clocks), the difference is
recorded as a temporary difference against the fiscal register's tax base,
not by re-computing the fiscal side.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 29: 29.1 tax includes "impuestos pagados por vía de retención" on distributions. 29.4-29.6: current tax liability/asset recognized for unpaid/recoverable amounts, measured "usando las tasas impositivas y la legislación que haya sido aprobada, o cuyo proceso de aprobación esté prácticamente terminado, en la fecha de presentación"; loss-carryback rights → current asset. 29.7-29.13: temporary differences = carrying amount vs tax base; base per jurisdiction's consolidated-filing practice; worked examples — business-combination FV step-ups, revaluations, goodwill base = cero si no amortizable/deductible-on-disposal, initial-recognition differences, investment carrying-vs-base. 29.14-29.15: DTL for ALL taxable temporary differences EXCEPT initial goodwill and initial-recognition differences of non-business-combination transactions with no P&L/no tax effect. 29.16-29.19A: DTA for deductible differences to the extent future taxable profit is probable (same-authority/same-taxpayer matching; tax-planning opportunities; history-of-losses caution; annual re-assessment of unrecognized DTAs 29.23; write-down/reinstatement). 29.20-29.22: DTA for unused tax losses/credits to the extent probable (sufficient taxable temporary differences; probable profits before expiry; losses from identifiable non-recurring causes; tax planning). 29.24-29.26: investment differences — DTL unless control of reversal timing + reversal not foreseeable; DTA only if reversal probable within foreseeability AND taxable profit available. 29.27-29.31: measurement at rates "que hayan sido aprobadas, o cuyo proceso de aprobación esté prácticamente terminado, en la fecha de presentación"; where different rates apply to different levels of taxable profit, "una entidad medirá los pasivos (activos) por impuestos diferidos utilizando las tasas promedio aprobadas… que se espera que sean aplicables a la ganancia (o pérdida) fiscal" (average rates); recovery-manner consistency (capital-gains rate if recovered by sale); non-depreciable revalued assets/revalued investment property → sale-recovery presumption (refutable for consumptive recovery models); "Una entidad no descontará los activos y pasivos por impuestos corrientes o diferidos" (no discounting — current AND deferred, 29.31). 29.32-29.33: two-rate jurisdictions — undistributed-profits rate until dividend liability recognized, remeasure on recognition; dividend withholding taxes "se cargan al patrimonio como parte de los dividendos". 29.3A: "una entidad no reconocerá los activos y pasivos por impuestos diferidos relacionados con los impuestos a las ganancias del Segundo Pilar, ni revelará la información que de otro modo requerirían los párrafos 29.39 a 29.40"; 29.42-43 disclose the exception + current Pillar Two expense separately. 29.34A-29.34D: uncertain tax treatments — probable-acceptance test; else most-likely amount or expected value (best predictor); changes treated as estimate changes. 29.35-29.37A: presentation — tax expense in the same P&L/OCI/equity component as the underlying; deferred tax assets/liabilities ALWAYS non-current (4.2(o) kin); offset current only with legal right + intent to settle net; offset deferred only same-taxation-authority + intended net settlement. 29.38-29.40: disclosures — expense components; amounts allocated to OCI/equity; rate reconciliation; per-type temporary-difference and unused-loss/credit amounts + movements; unrecognized items with expiry dates; explanation of the dividend tax consequence. | SME Standard Section 29 (income taxes): current tax at enacted or practically-enacted law/rates at the presentation date; temporary differences = carrying vs tax base; DTL all taxable differences except initial goodwill and initial-recognition-neutral items; DTA deductible differences to the extent probable; DTA on unused losses/credits to the extent probable; investment-difference rules; average rates for progressive tables; recovery-manner consistency; sale-recovery presumption for revalued non-depreciables; no discounting; two-rate jurisdictions use the undistributed rate until the dividend liability exists; dividend withholding charged to equity as part of the dividends; NO deferred tax for Pillar Two top-up taxes (with separate current-expense disclosure); uncertain treatments via probable-acceptance then most-likely/expected-value; deferred ALWAYS non-current; offset rules; full disclosure set incl. unrecognized-DTA expiry dates | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 29 whole (txt PAGE 264-276); 29.3A (txt PAGE 265); average-rate + no-discounting body (txt PAGE 272-273); 29.33 (txt PAGE 273); 29.34A-D (txt PAGE 273-274) (EVID-296) |
| LB-002 | Norma NIIF para las PYMES, Sección 35: transition-date procedures — recognize assets/liabilities the Norma requires, drop those it does not, reclassify per its presentation, re-measure per its measurement; adjustments to *ganancias acumuladas* (retained earnings) at the transition date. 35.9 mandatory non-restatements: derecognition (per prior GAAP), derecognition of financial assets/liabilities, hedge accounting, estimates, assets/liabilities of discontinued operations, NCI initial measurement (prospective), government loans (prospective), completed customer contracts. 35.10 optional exemptions: business combinations; share-based payment; fair value as deemed cost; previous-GAAP revaluation as deemed cost; event-driven fair-value measurements (e.g. insurance); cumulative-translation-differences reset to zero; separate financial statements at cost; compound instruments pre-transition; deferred taxes measured prospectively from the transition date; service concessions; full-cost extraction; lease identification at transition; dismantling-liability re-measurement at transition; rate-regulated deemed cost; severe-hyperinflation fair value; revenue-method election retroactive-or-prospective per A27. 35.12-35.15: first-FS disclosures — reconciliation of equity at the transition date AND at the prior-period end under both frameworks, and of the result for the latest prior period. Apéndice A: "Una entidad aplicará esas modificaciones y revisiones a periodos anuales que comiencen a partir del 1 de enero de 2027. Se permite su aplicación anticipada" (A1; disclose early adoption); A3 retrospective application per Sección 10 except A4-A49 (control-model consolidation remeasurement retrospective; Sec 12 prospective; Sec 19 prospective-from-initial-date; Sec 23 retro-or-prospective with completed-contract exemptions; SBC prospective; 28.19 retroactive; 29 deferred-tax-loss transitional retroactive with opening-equity option; 30.5A non-retroactive with spot-rate adjustment mechanics; 30.8A prospective option; bearer-plants deemed-cost option); Tabla A1 — full paragraph delta map (added/modified/deleted) of the 3rd edition vs the 2nd (2015) edition | First-time adoption: transition-date recognize/drop/reclassify/re-measure with adjustments to retained earnings; enumerated 35.9 mandatory exceptions; 35.10 optional exemptions (deemed-cost fair value / prior-GAAP revaluation / event-based; deferred taxes prospective; revenue method per A27; separate-FS cost; cumulative-translation reset; et al.); transition reconciliations of equity (transition date + prior period end) and result. Appendix A: 3rd edition effective 2027-01-01, early adoption permitted (disclosed); retrospective per Section 10 except the A4-A49 exceptions; Tabla A1 = the paragraph-level delta map vs the 2nd edition | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 35 (txt PAGE 307-315); 35.9 (txt PAGE 308); 35.10 (txt PAGE 308-309); Apéndice A A1 (txt PAGE 315); Tabla A1 (txt PAGE 325-329) (EVID-298; 32_ identity block) |
| LB-003 | Norma NIIF para las PYMES, Prólogo P12: "Las decisiones sobre qué entidades están requeridas o autorizadas a utilizar las Normas NIIF de Contabilidad completas o la Norma de Contabilidad NIIF para las PYMES recaen en las autoridades legislativas y regulatorias y en los emisores de normas de las distintas jurisdicciones." Apéndice B (glosario): tax-base and deferred-tax definitions integral to the Norma | Decisions on which entities must or may apply full IFRS or the SME standard rest with each jurisdiction's legislative and regulatory authorities and standard-setters; the glossary is an integral part of the Norma | `sv/sources/32_NIIF_PYMES_2025.pdf` | Prólogo P12 (txt PAGE 22); Apéndice B (txt PAGE 349-350) (EVID-275; 32_ identity block) |
| LB-004 | Guía EY (SECONDARY-ONLY per R29(a); never sole LB): NIIF 18 *Presentation and Disclosure in Financial Statements* and NIIF 19 *Subsidiaries without Public Accountability*, effective 2027-01-01, for FULL-NIIF entities — the NIIF para PYMES is NOT amended by them; the 2024-2026 IFRS amendment set; NIIF S1/S2 sustainability landscape | (Secondary authority, R29(a)): version/horizon facts for the full-NIIF watch rows — PYMES reporters are untouched by NIIF 18/19; S1/S2 documented as a layer distinct from financial statements (SOQ-52 boundary) | `sv/sources/33_Guia_NIIF_Sostenibilidad_2024-2025.pdf` | NIIF 18/19 + amendments chapters (txt PAGE 170-175 zone); S1/S2 chapter (EVID-299/301/302; EV33 OQ-1/OQ-3) |
| LB-005 | Ley ISR (consolidada, D.L. T447 2025-04-30) — **POINTER rows, consumed via the taxation wave BY FR ID, never restated here:** Art. 14 (capital-gain basis = acquisition cost minus depreciations realizadas y admitidas; capital losses); Art. 14-A (10% separate liquidation, domestic securities); Art. 42 (10% tax on capital gains realized after 12 months); Art. 72 (5% retention on distributions/credits of utilidades); Reglamento ISR Arts. 15-17 (capital-loss ledger mechanics) | Income Tax Law pointers: capital gains/losses and their 5-year ledger, the 10% long-horizon capital-gain rate, the 5% dividend withholding — the fiscal feeds this file's deferred-tax engine consumes by id | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 14 pp.9-10 (EVID-093); Art. 14-A pp.10-11 (EVID-094/168); Art. 42 (03-file SOQ-01 verdict, EVID bank); Art. 72 p.45 (EVID-103) — all consumed as `taxation/03_isr-rates-gains.md` LB-006/SV-TAX-FR-082/085/086 and `taxation/05_isr-distributions.md` LB-001/SV-TAX-FR-132 BY ID |

## 3. Functional Requirements

### 3.1 Scope and current tax (Sección 29.1-29.6)

- **SV-COA-FR-253:** The system shall implement the income-tax engine of
  Sección 29 over the ACCOUNTING book — income taxes including taxes paid
  by way of retention (*impuestos pagados por vía de retención*, withholding
  taxes) on distributions — as the wave's fiscal-BY-ID hub: every
  book-vs-fiscal difference recorded in files 01-07 (asset depreciation and
  impairment differences from `04_nonfinancial-assets.md` FR-101..; revenue
  timing from `06_revenue.md` FR-223; provisions and employee-benefit
  accruals from `05_liabilities-equity-benefits.md` FR-135/153; the FX
  two-clock difference between CT Art. 62 [consumed BY ID as SV-TAX-FR-020]
  and Sección 30 book rates from `03_financial-instruments-fx.md`;
  business-combination fair-value step-ups from
  `07_groups-related-parties.md`) lands
  here as a temporary difference against the taxation wave's tax base,
  NEVER by re-deriving the fiscal computation here.
  (LB-001; LB-003; EVID-296)
- **SV-COA-FR-254:** The system shall recognize the current tax liability
  (asset) for current-period unpaid (recoverable) tax and measure it using
  the tax rates and legislation that have been enacted, or whose enactment
  process is practically complete, at the PRESENTATION DATE — resolved as
  DATED regime rows (D15: the rate/legislation vintage resolves as-of the
  fiscal-year presentation date and snapshots on the record; the vintage
  feeds are consumed from `taxation/03_isr-rates-gains.md` SV-TAX-FR-074
  and `sv/requirements/taxation/isr_brackets.csv` BY ID, never
  re-encoded here) — and shall recognize a loss-CARRYBACK right, where the
  jurisdiction grants one, as a current tax asset; for SV the carryback
  surface stays config-off because the corpus Ley ISR grants no carryback
  (operating losses do not carry at all per SV-TAX-FR-086; only the
  capital-loss 5-year ledger carries forward, SV-TAX-FR-085 — consumed
  BY ID under FR-259).
  (LB-001; LB-005; EVID-296)

### 3.2 Temporary differences and recognition gates (Sección 29.7-29.26)

- **SV-COA-FR-255:** The system shall compute a temporary difference for
  each asset and liability as the difference between its CARRYING AMOUNT
  (the accounting book, this wave) and its TAX BASE (*base fiscal*) — the
  amount attributed for tax purposes — sourcing the tax base from the
  taxation wave's per-asset fiscal register BY ID
  (`taxation/06_isr-assets.md` SV-TAX-FR-167 detailed per-asset register,
  SV-TAX-FR-170 accumulated-admitted-depreciation exposure,
  SV-TAX-FR-156 sale-recovery routing), and for investments as carrying
  versus base per 29.13's investment example; where a liability's
  settlement has no tax effect the base equals carrying; goodwill's tax
  base is CERO where not amortizable/not deductible-on-disposal
  (T7 kin, consumed by id); the deferred-tax base is set PER ENTITY
  according to the jurisdiction's consolidated-filing practice (29.13) —
  no SV consolidated deferred-tax base is invented here (taxation/01's
  branch-consolidation surface is the future feed; OQ-5).
  (LB-001; LB-005; EVID-296)
- **SV-COA-FR-256:** The system shall recognize a deferred tax liability
  for ALL taxable temporary differences — including business-combination
  fair-value step-ups, revaluations and every book-over-fiscal
  acceleration recorded in files 01-07 — EXCEPT (a) initial goodwill and
  (b) initial-recognition differences of transactions that are not
  business combinations and affect neither accounting profit nor taxable
  profit (initial-recognition-neutral), which never ground a DTL.
  (LB-001; EVID-296)
- **SV-COA-FR-257:** The system shall recognize a deferred tax asset for
  deductible temporary differences ONLY to the extent it is PROBABLE that
  taxable profit will be available against which the difference can be
  utilized, implementing the Norma's matching conditions: profit expected
  from transactions generating taxable temporary differences with the SAME
  taxation authority and the SAME taxpayer (entity or consolidated group
  where applicable); tax-planning opportunities available to the entity;
  and a CAUTION posture where the entity has a history of recent losses —
  with every unrecognized DTA RE-ASSESSED at each closing date (29.23) and
  written down or reinstated accordingly (estimate-change mechanics per
  `01_framework-policies.md` FR-017, consumed by id).
  (LB-001; EVID-296)
- **SV-COA-FR-258:** The system shall apply the SV NO-NOL jurisdiction
  constraint as an in-file ruling (SOQ-50): unused OPERATING tax losses
  can NEVER ground a DTA in the SV configuration (SV has no general
  net-operating-loss carryforward — `taxation/03_isr-rates-gains.md`
  SV-TAX-FR-086 BY ID); the ONLY loss asset that can ground a DTA is the
  capital-loss 5-year ledger (Ley ISR Art. 14/14-A and Reglamento ISR
  Arts. 15-17 — LB-005 pointers; ledger owned by SV-TAX-FR-085 BY ID),
  recognized to the extent the 29.20-29.22 probable test is met:
  sufficient taxable temporary differences reversing in the window,
  probable taxable profits before the ledger EXPIRES (the 5-year expiry
  dates drive the 29.40 unrecognized-DTA disclosure rows), losses from
  identifiable non-recurring causes, or tax planning.
  (LB-001; LB-005; EVID-296)
- **SV-COA-FR-259:** The system shall treat interests in subsidiaries,
  associates and joint arrangements (carrying amount versus tax base of
  the investment) per 29.24-29.26: a DTL is recognized for the taxable
  temporary difference UNLESS the entity controls the timing of the
  reversal AND the reversal is not expected in the foreseeable future;
  a DTA is recognized only where it is probable the temporary difference
  will reverse in the foreseeable future AND taxable profit will be
  available against which it can be used — the control/foreseeability
  determinations snapshot on the record (D15) and re-assess at each
  closing.
  (LB-001; EVID-296)

### 3.3 Measurement: rates, average rates, recovery manner (Sección 29.27-29.31)

- **SV-COA-FR-260:** The system shall measure deferred tax assets and
  liabilities at the tax rates and legislation enacted, or whose enactment
  is practically complete, at the PRESENTATION DATE — as DATED rate rows
  (D15: fiscal-year-resolution anchor; the enacted/substantively-enacted
  status carries its enactment date on the row), consuming the rate feeds
  BY ID from `taxation/03_isr-rates-gains.md` (SV-TAX-FR-074 bracket
  engine + `isr_brackets.csv` vintages dl_957_2011 / dl_293_2025) and
  never re-deriving the SV rate schedule here.
  (LB-001; LB-005; EVID-296)
- **SV-COA-FR-261:** The system shall apply AVERAGE RATES ("tasas
  promedio… aplicables a la ganancia (o pérdida) fiscal") where the
  jurisdiction taxes through PROGRESSIVE tables — for SV the domiciled
  natural-person Art. 37 progressive brackets — by computing the average
  rate applicable to the estimated fiscal gain (or loss) over the dated
  bracket vintages consumed from SV-TAX-FR-074 BY ID, and the flat-rate
  tracks (juridical-persons 30% per SV-TAX-FR-077 kin; 10% separate
  liquidations per SV-TAX-FR-087/091 kin) directly where progressive
  averaging does not apply.
  (LB-001; LB-005; EVID-296)
- **SV-COA-FR-262:** The system shall implement RECOVERY-MANNER
  consistency: deferred tax on an asset reflects the tax consequences of
  the manner in which the entity expects to recover its carrying amount —
  the CAPITAL-GAINS rate (Ley ISR Art. 42 10% for gains realized after
  12 months, consumed BY ID as SV-TAX-FR-082) where recovery is expected
  by SALE, the ordinary/average rate where by USE over time — sourcing
  each asset's fiscal recovery classification from the taxation register
  BY ID (`taxation/06_isr-assets.md` SV-TAX-FR-156 sale-recovery routing,
  SV-TAX-FR-167 register); a NON-DEPRECIABLE revalued asset or revalued
  investment property presumes recovery by SALE (refutable where the
  recovery model is consumption-based); and where recovery is expected to
  be TAX-FREE (special-regimes exemption schedules —
  `special-regimes/02_zf-exemption-schedules.md` SV-SPE-FR-023..035 BY ID:
  ZF/DPA exemption percentages and per-acuerdo schedules) no taxable
  temporary difference arises on the exempt-recovery portion (29.7:
  recovery without affecting taxable gains), so no DTL is booked on it.
  (LB-001; LB-005; EVID-296)
- **SV-COA-FR-263:** The system shall NEVER discount current or deferred
  tax assets and liabilities ("Una entidad no descontará los activos y
  pasivos por impuestos corrientes o diferidos", 29.31 as printed) and
  shall re-assess unrecognized DTAs at each closing date with write-downs
  and reversals through profit or loss as estimate changes.
  (LB-001; EVID-296)

### 3.4 Two-rate rule, dividend WHT to equity, Pillar Two, uncertain treatments (Sección 29.32-29.34D + 29.3A)

- **SV-COA-FR-264:** The system shall implement the two-rate rule for
  jurisdictions whose tax on distributed profits differs from the
  undistributed rate: deferred tax is measured at the UNDISTRIBUTED-profits
  rate until the entity recognizes a liability to pay the dividend, at
  which point the deferred position is re-measured at the distributed rate
  (SV: the corpus Ley ISR applies one corporate rate with distribution
  taxation via withholding — the rule ships as the engine's general
  behavior with the SV rate tracks consumed BY ID from taxation/03; no
  SV two-tier corporate rate is invented).
  (LB-001; EVID-296)
- **SV-COA-FR-265:** The system shall charge DIVIDEND WITHHOLDING TAX to
  EQUITY, as part of the dividends, at the moment the liability to pay
  the dividend is recognized (29.33 "se cargan al patrimonio como parte
  de los dividendos") — posting the 5% retention computed and effected by
  `taxation/05_isr-distributions.md` SV-TAX-FR-132 BY ID against the
  equity distribution line (never through current P&L), linked to the
  earnings-register rows (SV-TAX-FR-144/145 BY ID) that carry the
  already-taxed pool; the CC Arts. 37-38 statutory distribution-capacity
  ceiling (SOQ-49 kin) is consumed from
  `05_liabilities-equity-benefits.md` BY ID and never re-derived here.
  (LB-001; LB-005; EVID-296)
- **SV-COA-FR-266:** The system shall implement the Pillar Two exception
  as CONFIG-OFF for SV (SOQ-51): NO deferred tax liability or asset is
  recognized for the Pillar Two top-up tax (29.3A), the current Pillar
  Two tax expense is presented separately from other current tax expense,
  and the exception is disclosed (29.42-43) — the config-off default
  stands because NO SV Pillar Two legislation exists in the corpus
  (external watch; OQ-3).
  (LB-001; EVID-296)
- **SV-COA-FR-267:** The system shall implement uncertain tax treatments
  (29.34A-29.34D): a tax treatment used or planned is accepted when it is
  PROBABLE the taxation authority will accept it; where not probable, the
  effect is measured using the MOST-LIKELY amount or the EXPECTED VALUE
  (whichever better predicts the resolution) — with changes in the
  measured effect treated as ESTIMATE changes (10.14A kin, file 01
  FR-017 by id), and the uncertain-treatment surface kept DISTINCT from
  the fiscalización (tax audit) dispute surfaces owned by the taxation
  wave BY ID (linked by id, never merged).
  (LB-001; EVID-296)

### 3.5 Presentation and disclosure (Sección 29.35-29.40)

- **SV-COA-FR-268:** The system shall present income-tax amounts per the
  Section 29 rules: tax expense/income in the SAME component of profit or
  loss, OCI or equity that carries the underlying item; deferred tax
  assets and liabilities ALWAYS NON-CURRENT (4.2(o) — the ESF line
  architecture owned by `02_coa-structure.md` by id); offset of current
  tax assets and liabilities only with a legally enforceable right to set
  off and the intention to settle net; offset of deferred tax assets and
  liabilities only for the SAME taxation authority and intended
  net-settlement or simultaneous realization.
  (LB-001; EVID-296)
- **SV-COA-FR-269:** The system shall emit the Section 29 disclosure
  set: (a) the major components of tax expense/income; (b) amounts
  allocated to OCI and to equity; (c) a rate reconciliation between the
  statutory average rate(s) and the effective rate; (d) per-type
  temporary-difference amounts and movements, and the amounts and expiry
  dates of (for SV) the capital-loss-ledger DTAs; (e) unrecognized DTA
  items WITH their expiry dates (the 5-year capital-loss windows); and
  (f) an explanation of the tax consequence of distributions to
  investors (the dividend-WHT-to-equity charge of FR-265).
  (LB-001; EVID-296)

### 3.6 First-time adoption (Sección 35)

- **SV-COA-FR-270:** The system shall implement the transition-date
  procedures of Sección 35 as a first-adoption workspace: at the
  transition date the entity recognizes the assets and liabilities the
  Norma requires, drops those it does not, reclassifies items per the
  Norma's presentation, and re-measures per its measurement rules — with
  EVERY resulting adjustment posted to *ganancias acumuladas* (retained
  earnings) at the transition date, never through current-period income;
  the workspace rides the D19 cut-over canon as shared reference
  (posting tiers — GL-neutral closed items vs real open items via
  configurable control accounts with XML-ID defaults; trial-balance
  routing dated at cut-over; the straddle-filing checkpoint — cited from
  `shared/docs/regulatory-change-management.md` D19 +
  `shared/docs/go-live-readiness.md` as shared canon, NOT as FRs).
  (LB-002; EVID-298)
- **SV-COA-FR-271:** The system shall ingest the pre-transition legacy
  history per the D18 mid-year go-live canon as shared reference
  (`shared/docs/regulatory-change-management.md` D18: `is_historical`
  records in historical journals with natural journal type,
  suppress/reallow semantics, tiered ingestion — straddle-FY
  transactional detail, prior-FY declaration snapshots, balances,
  carryover ledgers incl. the capital-loss carryover rows, batch-reversal
  or config-gated deletion) — the transition-date re-measurements and
  reconciliations compute on top of ingested values without re-deriving
  what the predecessor system already handled.
  (LB-002; EVID-298)
- **SV-COA-FR-272:** The system shall enforce the 35.9 MANDATORY
  exceptions as non-restatement gates at the transition date — the entity
  shall NOT restate: derecognition recognized or retained under prior
  GAAP; derecognition of financial assets/liabilities under prior GAAP;
  hedge accounting positions taken under prior GAAP; ESTIMATES made
  under prior GAAP (unless they embodied errors or unavailable
  information); assets and liabilities of discontinued operations; the
  initial measurement of non-controlling interests (prospective);
  government loans and related deferred-tax treatment of their benefit
  (prospective); customer contracts completed before the transition
  date.
  (LB-002; EVID-298)
- **SV-COA-FR-273:** The system shall implement the 35.10 OPTIONAL
  exemptions as per-election records that snapshot at the adoption date
  (D15 anchor): FAIR VALUE as deemed cost for any item of PPE (and
  intangibles where FV reliably measurable); PREVIOUS-GAAP REVALUATION as
  deemed cost at the revaluation date; EVENT-DRIVEN fair values (e.g.
  insurance-event FV) as deemed cost; deferred taxes measured
  PROSPECTIVELY from the transition date (not recomputed for pre-transition
  differences); the revenue-method election applied retroactively or
  prospectively per A27; separate financial statements kept at cost; the
  cumulative-translation-difference balance reset to zero for foreign
  operations; plus the further enumerated exemptions (business
  combinations, share-based payment, service concessions, full-cost
  extraction, lease identification at transition, dismantling-liability
  re-measurement, rate-regulated deemed cost, severe-hyperinflation FV,
  compound instruments) — each election dated, evidenced and disclosed.
  (LB-002; EVID-298)
- **SV-COA-FR-274:** The system shall emit the transition
  reconciliations (35.12-35.15) in the first NIIF-PYMES financial
  statements: a reconciliation of EQUITY at the transition date and of
  equity at the end of the latest prior period, and a reconciliation of
  the RESULT for the latest prior period — each reconciling the
  prior-framework figures to this Norma, with the deemed-cost and
  deferred-tax-prospective elections' effects visible as reconciling
  lines.
  (LB-002; EVID-298)

### 3.7 Edition versioning (Apéndice A + Tabla A1)

- **SV-COA-FR-275:** The system shall carry the Norma edition as a DATED
  regime row per company (D12 version-regime discipline): 2nd edition
  (2015) valid for SV books to 2026-12-31 · 3rd edition (Feb-2025)
  MANDATORY for annual periods beginning 2027-01-01 (A1) · EARLY
  ADOPTION of the 3rd edition permitted with disclosure — with the
  Tabla A1 paragraph delta map (added/modified/deleted vs the 2nd
  edition) as the vintage artifact driving edition-sensitive behavior
  differences BY PARAGRAPH (SOQ-48: the 2nd-edition full text is NOT in
  the corpus — no 2nd-edition behavior is invented beyond the Tabla A1
  delta); the edition transition applies the Apéndice A regime —
  retrospective per Sección 10 EXCEPT the A4-A49 exceptions (among
  them: the Section 29 deferred-tax transitional application retroactive
  with an opening-equity option; 30.8A prospective option; Section 19
  prospective-from-initial-date; Section 23 retro-or-prospective with
  completed-contract exemptions), resolved as-of the edition-change
  fiscal year and snapshotted.
  (LB-002; EVID-298; 32_ identity block)
- **SV-COA-FR-276:** The system shall carry full-NIIF horizon facts as
  WATCH ROWS only (R29(a) secondary facts, LB-004 — never sole LB of an
  FR): NIIF 18 (presentation/disclosure) and NIIF 19 (reduced-disclosure
  subsidiaries), both effective 2027-01-01 for FULL-NIIF entities, do NOT
  amend the NIIF para PYMES (the 2024-2026 amendment set likewise watch
  rows) — PYMES-book companies experience no engine change from them;
  and NIIF S1/S2 sustainability reporting is OUT of localization core
  scope (SOQ-52 boundary: no SV adoption instrument in corpus; boundary
  note only, no FRs invented — SAS discipline).
  (LB-002; LB-004 secondary; EVID-299/301/302)

## 4. Data Model

Layer semantics: the deferred-tax/adoption engine is Odoo-native
(account.move posting surfaces + per-asset difference records over the
accounting models + dated config rows consuming the taxation wave's
machine-readable feeds by reference) — all entities live in the client
(wave default `odoo`; see §5). Fiscal quantities are NOT copied into
this wave's models as authority: every rate/base/ledger field stores the
consumed FR-ID reference + the resolved value snapshot (D15), so the
taxation wave's dated rows remain the single source of truth.

**Current/deferred tax computation (l10n_sv_chart.deferred_tax):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.deferred_tax | company_id · fiscal_year_id | m2o | per company/fiscal year; presentation-date resolution | FR-254, FR-260 |
| l10n_sv_chart.deferred_tax | rate_vintage_ref · rate_snapshot | char/m2o + float | consumed BY ID: taxation/03 SV-TAX-FR-074 + isr_brackets.csv vintage (dl_957_2011 / dl_293_2025); enacted/substantively-enacted status + date snapshot | FR-254, FR-260 |
| l10n_sv_chart.deferred_tax | average_rate · rate_basis | float + select | progressive average rate per 29.30-29.31 · flat · capital_gain_10 (SV-TAX-FR-082 by id) | FR-261, FR-262 |
| l10n_sv_chart.deferred_tax | current_tax_asset · current_tax_liability | monetary | 29.4-29.6 presentation-date measurement | FR-254 |
| l10n_sv_chart.deferred_tax | dtl_total · dta_recognized · dta_unrecognized | monetary | 29.14-29.23 gates applied; re-assessed each closing | FR-256, FR-257 |

**Temporary-difference registry (l10n_sv_chart.temp_difference):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.temp_difference | source_ref | m2o/m2m by id | difference source: 04 asset models (FR-101.. kin) · 05 provisions/benefits (FR-135/153 kin) · 06 revenue timing (FR-223) · 03 FX two-clock (CT 62 = SV-TAX-FR-020 vs Sec 30) | FR-253 |
| l10n_sv_chart.temp_difference | carrying_amount · tax_base · tax_base_source | monetary + char | book carrying vs tax base; base consumed BY ID from taxation/06 SV-TAX-FR-167/170/156 register | FR-255 |
| l10n_sv_chart.temp_difference | kind | select | taxable · deductible · investment (29.24-29.26) · initial_recognition_neutral (no DTL) · goodwill_initial (no DTL) · exempt_recovery (no DTL, SV-SPE by id) | FR-256, FR-259, FR-262 |
| l10n_sv_chart.temp_difference | expected_recovery | select + rate | use_over_time · sale (capital-gain rate by id) · tax_free (exemption schedule by id); non-depreciable-revalued presumption flag | FR-262 |
| l10n_sv_chart.temp_difference | dta_probable_basis | select + text | same_authority_same_taxpayer · planning_opportunity · capital_loss_ledger (SV-TAX-FR-085 by id) · history_of_losses_caution; annual re-assessment date | FR-257, FR-258 |

**Capital-loss DTA gate (SV constraint, SOQ-50):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.capital_loss_dta | ledger_ref | char/by id | taxation/03 SV-TAX-FR-085 ledger rows (Ley ISR Art. 14/14-A, Reglamento 15-17 — LB-005 pointers) | FR-258 |
| l10n_sv_chart.capital_loss_dta | expiry_date · probable_test | date + select/text | 5y window; 29.20-29.22 criteria evidence (taxable differences, probable profits before expiry, non-recurring causes, planning); unrecognized rows feed 29.40 expiries | FR-258, FR-269 |

**Uncertain treatments + dividend charge (l10n_sv_chart.uncertain_tax / .dividend_wht_charge):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.uncertain_tax | treatment · acceptance_test | char + select | probable_acceptance · most_likely_amount · expected_value (29.34A-D); estimate-change kin | FR-267 |
| l10n_sv_chart.dividend_wht_charge | retention_ref | m2o/by id | taxation/05 SV-TAX-FR-132 5% retention event; earnings-register link SV-TAX-FR-144/145; CC ceiling kin (05 file by id) | FR-265 |
| l10n_sv_chart.dividend_wht_charge | posting_target | select | equity (as part of the dividends) — never P&L | FR-265 |
| res.company | sv_pillar_two_config | boolean | DEFAULT config-off (SOQ-51; no SV Pillar Two legislation in corpus); when on: 29.3A no-DT + 29.42-43 separate disclosure | FR-266 |

**First-adoption workspace (l10n_sv_chart.adoption_transition):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.adoption_transition | transition_date · adjustment_account | date + m2o | procedures: recognize/drop/reclassify/re-measure; ALL adjustments → ganancias acumuladas; D19 posting-tier + control-account canon (shared docs, cited) | FR-270 |
| l10n_sv_chart.adoption_transition | ingestion_link | char/by id | D18 tiered ingestion (straddle-FY detail / prior-FY snapshots / balances / carryover rows incl. capital-loss ledger) — shared canon | FR-271 |
| l10n_sv_chart.adoption_election | kind | select | 35.9 mandatory gates (read-only enforcement) · 35.10 optional: fv_deemed_cost · prior_pcga_revaluation · event_fv · deferred_tax_prospective · revenue_per_A27 · separate_fs_cost · cumulative_translation_reset · other (business-combination, SBC, concessions, extraction, leases, dismantling, rate-regulated, hyperinflation FV, compound) | FR-272, FR-273 |
| l10n_sv_chart.adoption_election | election_date · evidence · disclosure | date + text | D15 adoption-date anchor; snapshot-on-write | FR-273 |
| l10n_sv_chart.adoption_transition | reconciliation_set | one2many | 35.12-35.15: equity at transition date + prior period end; result for latest prior period | FR-274 |

**Edition regime (l10n_sv_chart.edition_regime):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.edition_regime | edition | select | 2nd_2015 · 3rd_2027 (mandatory, annual periods from 2027-01-01) · 3rd_early (permitted, disclose) | FR-275 |
| l10n_sv_chart.edition_regime | valid_from · valid_to · delta_ref | date + char | D12 dated rows; Tabla A1 (txt PAGE 325-329) as the paragraph delta artifact — SOQ-48 | FR-275 |
| l10n_sv_chart.horizon_watch | topic · facts | char + text | NIIF 18/19 2027 (PYMES NOT amended) · IFRS amendment set · NIIF S1/S2 boundary (SOQ-52) — watch rows only | FR-276 |

## 5. Odoo Mapping

Layer semantics for this wave: the deferred-tax bridge, adoption
workspace and edition rows are Odoo-native (account.move posting
surfaces, per-asset difference records over account.asset/account.move
line models, dated config rows, report disclosures) — every FR maps
`odoo`; no SaaS rows are introduced because none of these FRs touch DTE
generation/transmission (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are
stable across Odoo 17/18/19/20; the fiscal feeds are consumed by
reference to the taxation wave's models/CSVs, never duplicated.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-253 | odoo | l10n_sv_chart.deferred_tax + difference registry | engine scope | hub posture: 03/04/05/06 differences land here by id; fiscal NEVER re-derived |
| FR-254 | odoo | l10n_sv_chart.deferred_tax + account.move | current tax asset/liability + rate_vintage_ref | presentation-date enacted/substantively-enacted resolution (D15); vintage = taxation/03 FR-074 + isr_brackets.csv BY ID; SV carryback config-off (SV-TAX-FR-086 by id) |
| FR-255 | odoo | l10n_sv_chart.temp_difference | carrying vs tax_base (tax_base_source) | base from taxation/06 SV-TAX-FR-167/170/156 BY ID; goodwill base cero; per-entity base 29.13; consolidation doubt = OQ-5 |
| FR-256 | odoo | l10n_sv_chart.temp_difference → account.move | DTL entries | all taxable differences EXCEPT initial goodwill + initial-recognition-neutral (29.14-29.15) |
| FR-257 | odoo | l10n_sv_chart.temp_difference + closing wizard | dta_probable_basis | same-authority/same-taxpayer; planning; history-of-losses caution; 29.23 annual re-assessment; write-down/reinstatement = estimate change (01 FR-017 by id) |
| FR-258 | odoo | l10n_sv_chart.capital_loss_dta | ledger_ref + expiry + probable_test | SOQ-50 in-file ruling: no operating-loss DTAs (SV-TAX-FR-086 by id); only capital-loss 5y ledger (SV-TAX-FR-085; Ley ISR Art. 14/14-A LB-005 pointers) under 29.20-29.22 |
| FR-259 | odoo | l10n_sv_chart.temp_difference (investment kind) | control + foreseeability | 29.24-29.26; DTL unless control + not foreseeable; DTA only if reversal probable + profit available |
| FR-260 | odoo | l10n_sv_chart.deferred_tax | rate_vintage_ref + snapshot | dated enacted-rate rows (29.27-29.29); feeds by id (FR-074 + CSV vintages) |
| FR-261 | odoo | l10n_sv_chart.deferred_tax | average_rate + rate_basis | 29.30-29.31 "tasas promedio" over progressive brackets by id; flat tracks by id |
| FR-262 | odoo | l10n_sv_chart.temp_difference | expected_recovery | sale → capital-gain rate (Art. 42 via SV-TAX-FR-082 by id); register classification by id; non-depreciable-revalued sale presumption; exempt recovery → no DTL (SV-SPE-FR-023..035 by id) |
| FR-263 | odoo | l10n_sv_chart.deferred_tax | no discount flag + re-assessment | 29.31 as printed; write-downs = estimate changes |
| FR-264 | odoo | l10n_sv_chart.deferred_tax | undistributed-rate rule | 29.32: undistributed rate until dividend liability; SV single corporate rate + WHT track by id (no invented SV two-tier) |
| FR-265 | odoo | account.move (equity posting) + l10n_sv_chart.dividend_wht_charge | equity-charge posting | 29.33 WHT to equity as part of dividends; SV-TAX-FR-132 + 144/145 by id; CC ceiling = 05 file by id (SOQ-49 kin) |
| FR-266 | odoo | res.company + report layer | sv_pillar_two_config (default off) | 29.3A no-DT for Pillar Two; 29.42-43 separate current-expense disclosure; SOQ-51 config-off + OQ-3 watch |
| FR-267 | odoo | l10n_sv_chart.uncertain_tax | acceptance_test + method | 29.34A-D probable-acceptance → most-likely/expected-value; changes = estimate changes; fiscalización link by id, never merged |
| FR-268 | odoo | account.move + report layouts | non-current deferred classification + offset gates | deferred ALWAYS non-current (4.2(o); 02 file by id); current offset = legal right + intent; deferred offset = same authority + net-settlement intent |
| FR-269 | odoo | report layer (l10n_sv_chart) | disclosure builder | 29.38-29.40 components incl. rate reconciliation + unrecognized-DTA expiries (5y windows) + dividend consequence |
| FR-270 | odoo | l10n_sv_chart.adoption_transition + account.move | transition workspace + retained-earnings routing | 35.7-35.8 procedures → ganancias acumuladas; D19 canon cited (shared/docs regulatory-change-management.md D19 + go-live-readiness.md) |
| FR-271 | odoo | l10n_sv_chart.adoption_transition | ingestion_link | D18 canon cited (is_historical, historical journals, tiered ingestion, carryover rows incl. capital-loss ledger) |
| FR-272 | odoo | l10n_sv_chart.adoption_election (mandatory gates) | 35.9 enforcement | derecognition/hedging/estimates/discontinued/NCI/government-loans/completed-contracts non-restatement gates |
| FR-273 | odoo | l10n_sv_chart.adoption_election (optional) | 35.10 election records | FV/prior-revaluation/event-FV deemed cost; deferred-tax prospective; revenue per A27; separate-FS cost; translation reset; et al.; D15 adoption-date snapshot |
| FR-274 | odoo | report layer | 35.12-35.15 reconciliations | equity at transition date + prior period end; result for latest prior period |
| FR-275 | odoo | l10n_sv_chart.edition_regime | edition dated rows + Tabla A1 delta ref | 2nd-2015 | 3rd-2027-01-01 + early; Apéndice A A3-A49 regime incl. the Section 29 transitional (retroactive + opening-equity option); SOQ-48 — Tabla A1 as vintage artifact, no invented 2nd-ed. behavior |
| FR-276 | odoo | l10n_sv_chart.horizon_watch | watch rows | NIIF 18/19 2027 (PYMES NOT amended) + amendment set + S1/S2 boundary (SOQ-52) — 33_ secondary facts, never sole LB |

Version-regime notes (D12/D15): the Norma edition is the wave-level
DATED regime row — 3rd edition (Feb-2025) mandatory for annual periods
from 2027-01-01, early adoption permitted (A1; txt PAGE 315); SV
2025-2027 books may run under the 2nd (2015) edition with the Tabla A1
delta map as the only corpus artifact for the difference (SOQ-48 — the
edition flag and rows are owned HERE per file 01's §5 note). Deferred-tax
RATES resolve as-of the fiscal-year presentation date (D15
fiscal-year-resolution anchor) and snapshot on the computation record;
the bracket vintages themselves (dl_957_2011 to 2025-05-07 / dl_293_2025
from 2025-05-08) are owned by taxation/03 SV-TAX-FR-074 BY ID. Adoption
elections resolve as-of the adoption date (D15). Mid-year go-live
(D18): a migrating adopter's pre-transition history ingests as
`is_historical` rows per the shared canon (tiered ingestion; no
re-derivation), and the cut-over posting tiers, control accounts and
`is_sequence_init` sequence-initialization records follow the D19 canon —
both cited as shared documentation, encoded as FR posture here, owned as
mechanics by the go-live surface. No hard gates beyond the Norma's own
recognition gates (D16 no-override: never overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given software capitalized on a 4-year book life while the
  fiscal register admits 25%-straight-line over 4 years (book carrying
  above tax base mid-life), when the closing runs, then a taxable
  temporary difference posts a DTL measured at the ENACTED rate vintage
  applicable — the AVERAGE rate where the taxpayer is on the progressive
  Art. 37 brackets (consumed from SV-TAX-FR-074 by id) — as a dated,
  snapshotted row (FR-255, FR-256, FR-260, FR-261).
- **AC-002:** Given a fiscal year in which part of the capital-loss
  5-year ledger (Ley ISR Art. 14/14-A, SV-TAX-FR-085 by id) expires
  unused, when the DTA gate runs, then a DTA is recognized ONLY to the
  extent probable taxable profit exists before each tranche's expiry
  date — the expiring unrecognized remainder surfaces in the 29.40
  disclosure WITH its expiry dates, and NO DTA is ever grounded on
  operating losses (SOQ-50; FR-258, FR-269).
- **AC-003:** Given a dividend declared and recognized as a liability,
  when the distribution posts, then the 5% withholding (computed by
  taxation/05 SV-TAX-FR-132 by id) is charged against EQUITY as part of
  the dividends — never through current P&L — linked to the
  earnings-register rows (SV-TAX-FR-144/145) and, where the two-rate
  rule is engaged, the deferred position re-measures at the distributed
  rate (FR-264, FR-265).
- **AC-004:** Given an adopter electing fair value as deemed cost for
  its PPE at the transition date, when the first-adoption workspace
  closes, then the election records as a dated 35.10 record, the
  re-measurement posts to ganancias acumuladas (never current income),
  the 35.12-35.15 reconciliations of equity (transition date + prior
  period end) and of the latest prior-period result disclose the
  deemed-cost effect, and the D18-ingested legacy history beneath the
  transition is never re-derived (FR-270, FR-271, FR-273, FR-274).
- **AC-005:** Given the SV default configuration with Pillar Two
  config-off (SOQ-51), when a company computes deferred taxes, then NO
  deferred tax liability or asset arises for any Pillar Two top-up
  amount and the disclosure builder carries the 29.42-43 exception note
  — flipping the config on (a non-SV deployment) adds the separate
  current-expense presentation without ever booking a deferred position
  (FR-266).
- **AC-006:** Given a company whose fiscal year 2026 closes under the
  2nd (2015) edition and whose fiscal year 2027 opens under the 3rd
  edition (mandatory 2027-01-01), when the edition regime resolves, then
  each fiscal year's computations carry their own dated edition row, the
  2027 transition applies the Apéndice A regime (retrospective per
  Sección 10 except A4-A49 — the Section 29 transitional with its
  opening-equity option among them), and any early-2026 adoption of the
  3rd edition is a dated election WITH the early-adoption disclosure —
  Tabla A1 driving which paragraphs changed, no 2nd-edition behavior
  invented beyond it (FR-275).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-48 carried: edition versioning — the corpus carries ONLY the 3rd edition (Feb-2025; effective 2027-01-01; early adoption permitted); SV 2025-2027 books may still run under the 2nd (2015) edition whose full text is ABSENT. The Tabla A1 delta map (txt PAGE 325-329) serves as the vintage artifact (D12 two-vintage rows, FR-275); no 2nd-edition behavior is encoded beyond Tabla A1. Optional acquisition: 2nd-edition full text (2015). | no | Takumi S8 (sources watch) | open |
| OQ-2 | SOQ-50 carried (in-file ruling FR-258): SV has NO general NOL carryforward (taxation/03 SV-TAX-FR-086 by id) — unused OPERATING losses can never ground DTAs; ONLY the capital-loss 5-year ledger (Ley ISR Art. 14/14-A + Reglamento ISR Arts. 15-17 via LB-005 pointers; ledger = SV-TAX-FR-085 by id) can, subject to the 29.20-29.22 probable test. Ruling to re-confirm if a future ISR reform introduces any operating-loss carryforward. | no | Takumi S8 (regulatory watch) | open |
| OQ-3 | SOQ-51 carried: Pillar Two posture — 29.3A exception encoded as config-off (res.company default; FR-266) because NO SV Pillar Two legislation exists in the corpus; the 29.42-43 disclosure pair ships with the config. External watch for SV/global-minimum-tax developments; activation would be a dated config change, never a re-derivation. | no | Takumi S8 (regulatory watch) | open |
| OQ-4 | SOQ-52 carried: sustainability reporting (NIIF S1/S2, ESG, emissions inventories) has NO SV adoption instrument in the corpus and is OUT of Odoo-localization core scope — boundary note only (FR-276 watch row), no FRs invented (SAS discipline); any future SV adoption (or full-NIIF-group demand) = external watch. Kin: 33_ EVID-302 documents the S1/S2 landscape as distinct from the financial-statement layer. | no | Takumi S8 (boundary watch) | open |
| OQ-5 | Consolidated-filing practice for the deferred-tax base (29.13): whether any SV mechanism (branch consolidation, Ley ISR Arts. 22-24 kin — taxation/01 surface) constitutes a consolidated-filing practice that would set a GROUP tax base is NOT settled in the corpus; the engine defaults to PER-ENTITY bases and never invents consolidation. Confirm with the taxation wave before any consolidated deferred-tax surface is enabled. | no | Takumi S8 + taxation wave | open |
