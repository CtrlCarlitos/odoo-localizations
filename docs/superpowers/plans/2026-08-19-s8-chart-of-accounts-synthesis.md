# S8 Synthesis Implementation Plan — sv chart-of-accounts Takumi files (NIIF PYMES framework)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W14 NIIF evidence base (EVID-275..303, master-index clusters N1–N8 + SOQ-46..53) into Takumi-contract requirements files under `sv/requirements/chart-of-accounts/`, with FR numbering `SV-COA-FR-nnn`, LB citations to 32_ (the framework) under the R29 authority rulings, ACs, and coverage tracking.

**Architecture:** Requirements follow the 7-section template; the master index Section S8-A (N1–N8) is the synthesis worklist and its SOQ-46..53 register is binding. Layering: the framework/policy chassis (N1) admits a company and governs policy changes/errors; the COA structure file (N2) owns the account taxonomy and statement architecture; instruments+FX (N3) and non-financial assets (N4) own the measurement engines; liabilities/equity (N5) owns obligations and the equity model; revenue (N6) owns the recognition engine; groups/related parties (N7) own the multi-entity layer; the deferred-tax bridge + first-adoption + versioning (N8) closes the loop to every fiscal wave. Cross-topic interfaces cite FR IDs of earlier waves BY ID, never re-derived (taxation registers/brackets; special-regimes exemption schedules; payroll statutory engine; e-invoicing doc types; commercial-legal CC hooks).

**Tech Stack:** Markdown; FR IDs `SV-COA-FR-nnn` (new prefix `COA`; wave-sequential across the topic's files, no gaps, no renumbering). CSV sidecars only if a printed data table warrants one (default: none — the NIIF framework is qualitative; dated values live as config-row FRs).

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S8-A + R29 + SOQ-46..53 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12 + D15 as-of doctrine + D16 mechanics canon) + D18/D19 + `go-live-readiness.md` + `sv/HANDOVER.md` (country memory).

**Evidence inputs (read-only for implementers):**
- `sv/.extractions/32_NIIF_PYMES_2025.evidence.md` (EV32, EVID-275..298 — all clusters; THE framework LB)
- `sv/.extractions/33_Guia_NIIF_Sostenibilidad_2024-2025.evidence.md` (EV33, EVID-299..303 — secondary-only: version/horizon facts + contrast set)
- Extraction txt when a verbatim quote is abbreviated in evidence (S3 ruling 25 kin): `32_NIIF_PYMES_2025.pdf.txt` (page-anchored), `33_Guia_NIIF_Sostenibilidad_2024-2025.pdf.txt`.

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + section/párrafo). No trace → OQ, not FR.
- **Authority rule (R29, binding):** 32_ = the operative framework (Norma de Contabilidad NIIF para las PYMES, 3ra edición, feb-2025, effective 2027-01-01, early adoption permitted — cite section/párrafo); 33_ = SECONDARY-ONLY (never sole LB; usable for version/horizon facts and documented contrasts; where they could diverge, 32_ governs). Every file's §2 carries the SOQ-46 instrument-gap note (SV adoption instrument absent; eligibility = config-gap, NO invented SV thresholds).
- **The accounting-vs-fiscal two-track invariant (the wave's spine):** this wave owns the ACCOUNTING book only. Fiscal computations (ISR/IVA/payroll/special-regimes) are owned by their waves BY FR ID — never re-derived here, never overridden here. Where book and fiscal treatment differ (depreciation rates, provisions deductibility, R&D, FX clocks, revenue timing), the file records the difference and routes the bridge through N8's deferred-tax FRs (32_ Sec 29). CT Art. 62 FX (taxation T1) vs Sec 30 (book) = two clocks, never conflated.
- **D15/D12:** accounting policies resolve as-of their domain anchors (transaction date; adoption date for Sec 35 elections; fiscal-year resolution for deferred-tax rates) and snapshot on the record; the NIIF edition is a dated regime row (2nd-2015 vs 3rd-2027 with early adoption — Tabla A1 as the vintage artifact, SOQ-48); version-regime notes per template §5 wherever edition behavior differs.
- **Hard encodings from 32_ (cite as printed):** ESF items (a)-(r) with deferred tax ALWAYS non-current (4.2(o)); current/non-current with liquidity exception; nature-vs-function with function ⇒ separate cost of sales (5.10); OCI closed four-type list; no extraordinary items (5.11); FIFO|AVG only — LIFO banned (13.19); PPE cost-or-revaluation PER CLASS, prospective switch (10.10A); component depreciation; revenue-based depreciation method banned (17.22); intangibles finite-always + 10y cap (18.20) + ALL internally generated incl. R&D expensed (18.15); leases DUAL financiero/operativo (20.4 — NOT IFRS-16); borrowing costs ALL expensed (25.2); grants condition-gated; disproportionate-cost relief registry (2.28-2.30); dividend-WHT-to-equity (29.33); Pillar Two config-off (SOQ-51); prepaid-consideration FX rate (30.8A); hyperinflation config-off guard for SV (Sec 31).
- **Pointer-only / boundary surfaces (zero invented mechanics):** SV adopting instrument (SOQ-46); NIIF 18/19 (2027, full-NIIF entities — watch rows only, PYMES NOT amended); NIIF S1/S2 sustainability (SOQ-52 out-of-scope boundary); 2nd-edition full text (SOQ-48 — Tabla A1 delta map suffices).
- **Cross-topic discipline (cite FR IDs, never duplicate):** taxation/01+03 (rates/brackets/by-id feeds into N8 average-rate + capital-gain-rate rows), taxation/06 (account.asset register = fiscal book), special-regimes/02 (exemption schedules → expected-recovery modeling), taxation/05 (5% + earnings register ↔ 29.33 + CC dividend ceiling SOQ-49), payroll (statutory engine; vacation/termination book accruals here, fiscal there), e-invoicing (§3.11 corrections distinct from book error restatement; doc types), commercial-legal (C2 books/no-alteration kin; C3 FR-040 Consejo hook; C4 reserva legal + equity), D18/D19 (is_historical, deemed-cost elections = Sec 35 kin).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). Chart-of-accounts is Odoo-native (account.account template, account.move engines, res.company config) — default `odoo`.
- English prose, Spanish standard terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; in-file OQ numbering per file (OQ-1..n).
- **FR numbering contract:** wave-sequential `SV-COA-FR-001..` across files in task order; NO gaps, no renumbering; tasks STRICTLY IN ORDER (S4/S5/S7 precedent); index task verifies continuity.
- Files land in `sv/requirements/chart-of-accounts/` following the template exactly (7 sections, none deleted).
- **Process:** execute in `.worktrees/sv` on branch `sv-research`. Commit style: short imperative, no emojis, commit per task. Push at wave close (or at session boundaries if context runs low — resume state recorded in sv/HANDOVER.md first).

---

### Task 1: `sv/requirements/chart-of-accounts/01_framework-policies.md`

**Files:** Create `sv/requirements/chart-of-accounts/01_framework-policies.md`
**Covers:** N1
**FR numbering:** opens SV-COA-FR-001

**Content requirements:**
- §2 preamble: the S8 authority order (32_ operative; 33_ secondary-only per R29(a)); SOQ-46 instrument gap (eligibility = config-gap; framework flag niif_pymes|niif_plenas|+NIIF19 informational, SOQ-53); CC 443-444 "NIC"-covers-PYMES working reading (R29(c)/SOQ-47).
- PYME-eligibility FRs (32_ 1.1-1.7 + Apéndice B): no-public-accountability prong (traded/issuing instruments; fiduciary-as-main-business with the secondary-custody carve-out) + GPFS prong; compliance-declaration bar when ineligible (1.5); separate-FS use in full-NIIF groups (1.7); NO quantitative SV thresholds (config-gap).
- Complete-FS-set FRs (3.17-3.22): the five components; single vs two-statement vs combined retained-earnings variant (3.18/6.4); annual + ≥1 comparative (3.10/3.14); going-concern ≥12-month assessment + disclosure (3.7-3.9); uniformity + comparative reclassification (3.11-3.13); identification disclosures incl. presentation currency + rounding (3.23-3.24); accrual basis (3.17).
- Disproportionate-cost relief registry FR (2.28-2.30): lower PYME threshold, per-use disclosure with reasons.
- Policy-governance FRs (Sec 10): hierarchy 10.4-10.5 (full-NIIF as non-binding aid); change rules (standard-required or more-relevant); 10.10A revaluation-switch prospective; retroactive policy changes with comparative restatement; estimates prospective (10.14A-10.16); prior-period error restatement (10.18-10.23) — explicitly DISTINCT from e-invoicing §3.11/D9 fiscal corrections (by id) and CC 439 rectification (by id).
- Notes-architecture FRs (Sec 8): ordering, material policies, judgments vs estimation-uncertainty disclosures.
**AC examples:** company with fiduciary custody secondary to its main business qualifies; policy change from cost to revaluation model posts prospectively (no comparative restatement); error restatement rewrites comparatives while a fiscal correction posts new-period entries only.
**OQs to carry:** SOQ-46/47/52/53.

### Task 2: `sv/requirements/chart-of-accounts/02_coa-structure.md`

**Files:** Create `sv/requirements/chart-of-accounts/02_coa-structure.md`
**Covers:** N2
**Consumes:** T1 eligibility/config chassis (by id).

**Content requirements:**
- **Root taxonomy FR:** the (a)-(r) ESF item set as parent account classes (32_ 4.2) with report-line mapping; deferred-tax accounts ALWAYS non-current (4.2(o)); current/non-current split with the liquidity-ordering exception (4.4-4.5); operating-cycle/12-month rules (4.6-4.8).
- Sub-classification FRs (4.11): PPE classes; AR/AP related-party segmentation (feeds Sec 33 disclosures); inventory 3-way split; payables split (suppliers/related/deferred income/accruals); provision classes; equity classes incl. statutory reserves (CC kin by id).
- Share-capital + reserve disclosure FRs (4.12-4.13): per-class data, reconciliation of shares in circulation, treasury holdings, option-reserved shares; each reserve described.
- Income-statement architecture FRs (Sec 5): minimum items; nature-vs-function policy (function ⇒ separate cost of sales 5.11); OCI closed four-type list (5.4); no extraordinary items; discontinued single amount; NCI attribution (5.6); equity-statement reconciliation (Sec 6); 6.4 combined variant; proposed-dividend note (6.6).
- CFS FRs (Sec 7): per-account operation/investing/financing classification attribute; indirect/direct methods; FX-flow rate + unrealized-effect line (7.12/7.12A); interest/dividend classification CHOICES (7.14-7.16 — config); non-monetary transactions disclosed not flowed (7.18); financing-liability reconciliation (7.19A); **supplier-finance tagging + disclosure (7.19B-C)**; restricted-cash note (7.21).
- Odoo mapping: account.account template structure + account types; report-line binding (balance sheet/P&L/cash-flow layouts).
**AC examples:** an account flagged deferred-tax never lands in current; interest-paid config flipped between operating and financing reclassifies the CFS line only; a payable enrolled in a supplier-finance program surfaces the 7.19B disclosure block.
**OQs to carry:** SOQ-46 preamble carry; any Odoo-layout gaps as OQs.

### Task 3: `sv/requirements/chart-of-accounts/03_financial-instruments-fx.md`

**Files:** Create `sv/requirements/chart-of-accounts/03_financial-instruments-fx.md`
**Covers:** N3

**Content requirements:**
- Instrument-classification FRs (Sec 11 Part I): the 11.8 basic set + 11.9/11.9ZA debt conditions; no post-initial reclassification (11.11A); account-level classification flags (basic-amortized | FV-P&L | cost−impairment).
- Measurement FRs: initial at transaction price; trade receivables per revenue (11.13A); **financing transactions → PV at market rate (11.13B — partner/shareholder-loan kin, taxation/05 dual-track note)**; amortized cost + EIR engine (11.15-11.20) incl. the worked-example pattern; equities FV-if-measurable else cost−impairment (11.14).
- Incurred-loss impairment FRs (11.21-11.26): objective-evidence triggers; individual vs grouped; PV-at-original-EIR measurement; reversal cap — explicitly NOT ECL (33_ contrast note).
- Derecognition FRs (11.33-11.38): risks-rewards test; retained-asset+liability; substantial modification = extinguish+new.
- Disclosure FRs: category balances; **receivable aging + liability maturity bands (11.43/11.43A)**; pledged; defaults.
- Part II FRs: FV-P&L default (11.54); unquoted-equity cost fallback with last-reliable-FV-becomes-cost; narrow hedging (11.60-11.71: four risk types; swaps/forwards only; conditions 11.64; OCI routing 11.69) — config-gated, likely rare for SV PYMES.
- Fair-value engine FRs (Sec 12): exit price; principal/most-advantageous market; highest-best-use; three approaches; Level 1/2/3 classification (lowest significant input); disclosure set — one reusable FV-measurement record model.
- **FX FRs (Sec 30 + Apéndice 30A):** functional-currency indicators + change-prospective; transaction-date spot (averages if not volatile); **prepaid consideration at prepayment-date rate (30.8A)**; closing-rate monetary vs cost/FV-date non-monetary; P&L routing + net-investment OCI (30.11-30.13); presentation≠functional translation (30.17-30.20, OCI never recycled); convertibility framework; **Sec 31 hyperinflation config-off guard (SV = USD)**.
- Two-clock discipline notes: CT Art. 62 (taxation by id) governs the TAX base only; book differences → T8 deferred tax.
**AC examples:** interest-free 2y partner loan recognized at PV with implicit interest schedule; receivable aging auto-builds the 11.43 disclosure; prepaid USD expense at a foreign supplier keeps the prepayment-date rate; FV measurement with significant unobservable input classifies Level 3.
**OQs to carry:** hedging-applicability config note; any Odoo-loan-mapping gaps.

### Task 4: `sv/requirements/chart-of-accounts/04_nonfinancial-assets.md`

**Files:** Create `sv/requirements/chart-of-accounts/04_nonfinancial-assets.md`
**Covers:** N4
**Consumes:** T3 FV engine (by id).

**Content requirements:**
- Inventory FRs (Sec 13): lower-of-cost/NRV; cost build (non-recoverable duties/taxes net of discounts; financing element → interest; normal-capacity absorption; joint/sub-products; exclusions); techniques (standard/retail/most-recent); **FIFO|AVG only, LIFO banned (13.19), same formula per nature-and-use class**; ag-product harvest-FV-becomes-cost; NRV impairment + reversal (Sec 27.2-27.4) — fiscal castigo/mermas tracks separate (taxation/02+06 by id).
- PPE FRs (Sec 17): recognition + components (replacements/inspections capitalized; replaced component derecognized or substitution-cost proxy); cost build incl. dismantling estimate + NOT-costs list; cash-equivalent price; exchange-of-assets; **cost model OR revaluation model PER CLASS (17.15, class-wide, sufficient regularity, surplus → OCI superávit de revaluación with reversal rules)**; depreciation availability-to-derecognition (idle continues); life/residual/method reviews = estimates; **revenue-based method banned (17.22)**; land not depreciated; disposal → non-revenue P&L; disclosures.
- Intangibles FRs (Sec 18): recognition gate incl. **not-internally-generated (18.4(c))**; **ALL internally generated expensed incl. R&D (18.15-18.16), advances capitalizable, no re-capitalization**; finite-always + 10y cap (18.20) + contractual-life rule; residual-zero presumption; amortization from availability, linear fallback, revenue-based presumption refutable (18.22A); goodwill ≤10y + non-reversible impairment (19.34-19.35 + 27.28).
- Impairment engine FRs (Sec 27): indicator list (external/internal); recoverable = max(FV−costs-to-sell, value-in-use); VIU estimation rules (pre-tax rate; no financing/tax flows; current-state); CGU definition + goodwill-first loss allocation + floors; reversal caps (never goodwill; revaluation-surfaced reversals 17.15C); disclosure classes.
- Investment-property FRs (Sec 16): FV-if-measurable-without-disproportionate-cost else Sec 17 cost; leasehold classification; transfers-on-use-change only; reconciliation disclosure.
- Specialized FRs (Sec 34): bearer plants → PPE (34.2A); biological FV/cost models; harvest products; E&E policy choice + impairment triggers + separate class; concessions financial-asset vs intangible.
- Fiscal two-track notes everywhere: taxation/06 register = the fiscal book (Art. 30/30-A rates, 29-A.19/22 non-deductibles) BY ID; differences → T8 deferred tax; ISR capital-gain basis unaffected by book revaluation.
**AC examples:** LIFO config rejected at validation; revaluation of the building class books surplus to OCI and depreciation on the revalued amount; internally developed customer list expensed; CGU impairment writes goodwill down first with no later reversal; software book 4y vs fiscal 25% → deferred-tax liability via T8 FRs.
**OQs to carry:** any disproportionate-cost usage disclosures; Odoo component-asset mapping gaps.

### Task 5: `sv/requirements/chart-of-accounts/05_liabilities-equity-benefits.md`

**Files:** Create `sv/requirements/chart-of-accounts/05_liabilities-equity-benefits.md`
**Covers:** N5

**Content requirements:**
- Provisions FRs (Sec 21): three-gate recognition; best estimate; PV + pre-tax market rate + risk-in-rate-OR-estimate; only-original-purpose charges; remeasurement + unwinding→finance cost; reimbursement asset; restructuring (detailed plan + valid expectation); onerous contracts; contingencies disclosure rules; group-entity gratuitous guarantees (21.1A/21.18-19).
- Leases FRs (Sec 20 — DUAL model): in-substance-lease identification; classification criteria + indicators, set at inception, reassessed on term change only; lessee finance (lower(FV, PV-minimums) at implicit-or-incremental rate; EIR split; depreciate shorter-of); lessee operating straight-line + inflation-indexed exception; lessor finance net-investment + manufacturer-dealer split; lessor operating; sale-leaseback variants; maturity-band disclosures — NOT IFRS-16 (33_ contrast note).
- Employee-benefit FRs (Sec 28): four categories; short-term undiscounted; **accumulating-absence (vacaciones) accrual engine**; profit-sharing obligation gate; statutory contributions booked DC-style (S4 engine by id — no re-derivation); DB projected-unit-credit or the 28.19 simplified all-terminate-today-undiscounted election; actuarial gains/losses P&L-or-OCI uniform policy; termination-benefit triggers + >12m PV; long-term benefits all-P&L.
- Equity FRs (Sec 22): substance classification (puttable 5 conditions; mandatory-redeem preference = liability; cooperative interests); issuance measurement + contra-equity receivable subject to local-law prohibition (CC Art. 29 kin by id); transaction costs deduct equity; par/excess presentation per local law (CC/estatutos); stock dividends/splits no-total-change; convertible split liability-first (appendix pattern); treasury shares contra-equity no-P&L; distributions + non-cash at FV (carrying fallback); **CC Arts. 37-38 dividend ceiling = legal overlay — separate distribution-capacity ledger field, NEVER auto-derived from NIIF equity (SOQ-49)**.
- Grants FRs (Sec 24): condition-gated income + liability; FV measurement; tax-benefit carve-out note (ZF/LSI/DPA stay fiscal — special-regimes by id).
- **Borrowing-costs FR (25.2): ALL expensed — no capitalization config (33_ contrast).**
**AC examples:** vacaciones balance = undiscounted additional cost of unused rights; convertible issue splits liability at 6% PV with residual to equity; post-year-end declared dividend NOT a liability (32.11, T7 kin) but appears as segregated retained earnings; net-zero commitment alone creates no provision.
**OQs to carry:** SOQ-49; DB-applicability rarity note for SV.

### Task 6: `sv/requirements/chart-of-accounts/06_revenue.md`

**Files:** Create `sv/requirements/chart-of-accounts/06_revenue.md`
**Covers:** N6

**Content requirements:**
- Five-step engine FRs (Sec 23): contract criteria + non-qualifying→liability-until-collected/cancelled (23.9-23.10); combination (23.13); distinct two-criteria + series rule; **transaction price excludes third-party-collected amounts — IVA never revenue (23.23)**; variable consideration expected-value/most-likely + highly-probable restriction + updates; refund liabilities; royalties last-event (23A.37); significant financing → PV + separate interest with ≤1y practical exemption (23.36-23.38); non-cash FV else standalone-price fallback.
- Allocation FRs: relative standalone selling prices (observable else estimate: adjusted-market/cost-plus); discount/variable exceptions incl. series rule.
- Recognition FRs: over-time three criteria (23.54-23.56 with no-alternative-use + right-to-payment detail); point-in-time indicators + acceptance (23.57-23.61); progress methods output/input with wasted-cost exclusion; right-to-invoice (23.67).
- Appendix 23A FRs: modification taxonomy; warranties distinct-if-separately-purchasable else Sec 21; customer options material-right; principal-vs-agent (gross vs net); sales-with-return (refund liability + return asset + NRV-adjusted inventory); licences access-vs-use.
- Contract-balance FRs (23.77-23.81): contract asset vs receivable (unconditional = passage-of-time only) vs contract liability; separate presentation; impairment via Sec 11.
- Cost FRs (23.68-23.76): obtain-costs expensed; fulfill-cost asset (three criteria) + impairment = remaining-consideration − remaining-costs.
- Disclosure FRs (23.82-23.90): disaggregation categories; balances; commitments; methods; judgments.
- **Fiscal two-track notes:** fiscal débito windows + DTE timing (Ley IVA 62-63, e-invoicing by id) anchored on hecho generador — book control-transfer timing NEVER overrides fiscal anchoring (D15); differences → T8 deferred tax.
**AC examples:** 10-pan loyalty scheme recognizes 1.80/pan (guide-verified pattern, 32_ 23A.9-13); 2y interest-free sale splits PV + interest; return-expected sale books refund liability + return asset; over-time construction uses cost-to-cost with waste excluded.
**OQs to carry:** Odoo deferred-revenue/percentage-mapping gaps.

### Task 7: `sv/requirements/chart-of-accounts/07_groups-related-parties.md`

**Files:** Create `sv/requirements/chart-of-accounts/07_groups-related-parties.md`
**Covers:** N7

**Content requirements:**
- Consolidation FRs (Sec 9): duty + controladora-is-subsidiary exemption; held-for-sale subsidiary exclusion + 1y rule + restate; control triad + majority presumption + potential votes + agent/principal; consolidation mechanics (line-by-line, eliminations, NCI separate, uniform date/policies, intragroup losses → impairment check); loss-of-control (derecognize + retained-at-FV + gain/loss; FX-OCI never recycled); NCI transactions = equity transactions; **9.26 separate-FS menu (cost−impairment | FV-P&L | equity method) per category**; 9.25A separate-only; combined FS.
- Business-combination FRs (Sec 19 + 19A): acquisition method; FV identifiables; **NCI proportionate-only (19.14 — no FV option, full-NIIF contrast)**; goodwill formula incl. step-up; step-acquisition revalue→P&L; bargain purchase re-assess→P&L; contingent consideration (FV or most-likely fallback, no fallback remeasurement); 12-month measurement period; acquisition costs expensed; business-vs-asset + optional concentration test + substantive-process tree; associates (20% presumption; policy menu 14.4-14.9); JVs (operations/assets/entities + policy menu 15.9-15.16 + non-controlling-party routing).
- Related-party FRs (Sec 33): definition set + NOT-related list; controladora/ultimate disclosure regardless of transactions; **KMP aggregate remuneration**; transactions/balances/commitments disclosures by category; no arm's-length assertion unless demonstrable; **government-related-entity exemption + substitute disclosures (33.11/33.15)**.
- Post-period-events FRs (Sec 32): adjusting vs non-adjusting; **dividends agreed post-period-end NOT a liability (32.11)**; authorization-date disclosure.
- CC kin notes: legal personality at inscription ≠ reporting-entity boundary (by id).
**AC examples:** step acquisition 15%+85% revalues the prior stake through P&L; NCI at proportionate amount only; parent-entity puttable instrument held by subsidiary = liability at parent; government-controlled entity uses the 33.11 exemption with name/nature/scope disclosures.
**OQs to carry:** consolidation-applicability note (SOQ-46 kin — groups exist regardless of framework).

### Task 8: `sv/requirements/chart-of-accounts/08_deferred-tax-adoption.md`

**Files:** Create `sv/requirements/chart-of-accounts/08_deferred-tax-adoption.md`
**Covers:** N8
**Consumes:** T4 asset models, T6 revenue, T5 equity (by id) as difference sources.

**Content requirements:**
- **Deferred-tax bridge FRs (Sec 29):** current + deferred; enacted/substantively-enacted rates at presentation date (dated rows); temporary differences = carrying vs tax base; DTL all taxable differences except initial-goodwill/initial-recognition-neutral; DTA deductible differences to extent probable (same-authority/same-taxpayer; planning; history-of-losses; annual re-assessment); **SV no-NOL jurisdiction constraint — unused OPERATING losses cannot ground DTAs; only the capital-loss 5y ledger (Ley ISR Art. 14/14-A via taxation by id), subject to 29.21 probable test (SOQ-50 in-file ruling)**; investment differences; **average rates for progressive tables (taxation brackets CSVs by id)**; recovery-manner rates (Art. 42 10% for sale-recovery assets via taxation by id); revalued/deemed-sale presumptions; no discounting; two-rate rule → undistributed until dividend liability; **dividend WHT charged to equity (29.33 ↔ taxation/05 by id)**; **Pillar Two config-off (29.3A — SOQ-51)**; uncertain treatments (29.34A-D); presentation (deferred always non-current; offset rules); disclosure set.
- **First-adoption FRs (Sec 35):** transition-date procedures (recognize/drop/reclassify/re-measure; adjustments → retained earnings); 35.9 mandatory exceptions (enumerated); 35.10 optional exemptions (deemed-cost FV/prior-revaluation/event-FV; deferred taxes prospective; revenue retro-or-prospective per A27; separate-FS cost; cumulative-translation reset; etc.); transition reconciliations — **D18 is_historical ingestion + D19 sequence-init/deemed-cost kin notes by id**.
- **Versioning FRs:** edition dated rows (2nd-2015 vs 3rd-2027-01-01 + early adoption; Tabla A1 as the delta artifact — SOQ-48); full-NIIF horizon watch rows (NIIF 18/19 2027 — PYMES NOT amended; amendments set from 33_ facts); S1/S2 boundary note (SOQ-52).
**AC examples:** book 4y-software vs fiscal 25% → DTL at the enacted average rate; FY with expiring capital-loss ledger recognizes DTA only to extent probable profits; dividend declared → WHT recognized against equity not P&L; adopter elects FV deemed cost for PPE at transition with reconciliation disclosed.
**OQs to carry:** SOQ-48/50/51/52.

### Task 9: index + coverage + registry flips

**Files:**
- Create: `sv/requirements/chart-of-accounts/00_index.md`
- Modify: `sv/requirements/COVERAGE.md` (32_/33_ rows → per-file LB citations; rollup final counts; 02_ stays pending)
- Modify: `sv/README.md` (chart-of-accounts status → draft S8)
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (coverage note: S8 delivered)
- Modify: `sv/EXTRACTION_PLAN.md` (log entry: S8 synthesis COMPLETE)

**Content requirements:** Index: file table (FR ranges), totals, prefix note (SV-COA), cross-topic consumer map, OQ rollup in-file ↔ SOQ-46..53. COVERAGE flips with named citing files; numbering-continuity verification (`grep -o "SV-COA-FR-[0-9]*" ...` → contiguous 001..N); per-FR LB check. Commit + push sv-research.

## Execution protocol

Per-task: fresh implementer subagent (reads this plan's Global Constraints + its task + the evidence files fully) → controller review → reviewer subagent (verifies vs master index + evidence; numbering; LB citations; layer column; cross-refs by id; quote fidelity vs extraction txt) → fix round if findings → commit. Final whole-wave review subagent → ONE fix wave → push. Rulings discovered in-wave recorded in fix commits + summarized for the sv/HANDOVER update BEFORE any workspace deletion. Tasks 1-8 STRICTLY sequential; Task 9 last. Extraction txts are git-ignored here — read from the main checkout read-only if needed (S7 ruling (b) precedent).
