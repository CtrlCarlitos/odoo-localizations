# SV — Chart of accounts (NIIF para PYMES accounting book) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft (S8, 2026-08-20) |
| Authors | Controller + S8 subagent wave |
| Updated | 2026-08-20 |

This directory holds the S8 (synthesis wave 8) chart-of-accounts
requirements: the ACCOUNTING book under the *Norma de Contabilidad NIIF
para las PYMES* (Accounting Standard for SMEs, 32_, 3rd edition Feb-2025)
— PYME eligibility and the informational *marco contable* (accounting
framework) flag, the ESF/ERI/equity/cash-flow statement architecture,
the financial-instrument/EIR/incurred-loss and FX engines, the
non-financial-asset measurement clusters (inventories, PPE, intangibles,
impairment), the dual-model leases, employee benefits and equity with the
Código de Comercio distribution-capacity overlay, the Sección 23
five-step revenue engine, the consolidation/related-party layer, and the
Sección 29 deferred-tax fiscal bridge with Sección 35 first-time
adoption and edition versioning. Fiscal computations (ISR/IVA/payroll/
special-regimes) are owned by their waves by FR id — this wave never
re-derives fiscal values. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_framework-policies.md](01_framework-policies.md) | PYME eligibility two-prong determination (no public accountability + GPFS; 1.5 compliance bar; separate-FS rule), marco-contable flag as informational config (SOQ-53), complete-FS-set contract (five components; annual + ≥1 comparative; going concern ≥12-month lookahead), disproportionate-cost relief registry, Sección 10 policy governance (full NIIF as non-binding aid; 10.10A prospective revaluation switch; error restatement SV-COA-FR-018 explicitly DISTINCT from e-invoicing fiscal correction — SV-EINV-FR-159 by id), notes architecture (N1) | SV-COA-FR-001..021 | 21 | 7 | 9 | 4 |
| [02_coa-structure.md](02_coa-structure.md) | THE canonical account taxonomy: ESF root classes (a)-(r) with report-line binding (deferred tax ALWAYS non-current), current/non-current split, Sección 4 sub-classifications (PPE classes; related-party AR/AP split; statutory reserves consumed from commercial-legal SV-CML-FR-041/053..056 by id), Sección 5 income-statement architecture (nature vs function; closed OCI list; discontinued single amount), estado de cambios en el patrimonio, CFS per-account classification + 7.19A/B-C supplier-finance surfaces (N2) | SV-COA-FR-022..054 | 33 | 4 | 9 | 3 |
| [03_financial-instruments-fx.md](03_financial-instruments-fx.md) | Part I basic-instrument classification + amortized cost/EIR engine, incurred-loss impairment (NOT ECL), derecognition, Part II FV + narrow hedging (config-gated OFF), fair-value engine, FX translation (functional-currency indicators; prepayment-date rate 30.8A — SV-COA-FR-084) with the CT Art. 62 two-clock fiscal rule consumed as SV-TAX-FR-020 by id (SV-COA-FR-086 — book FX never conflated with tax-base FX) (N3) | SV-COA-FR-055..092 | 38 | 8 | 11 | 4 |
| [04_nonfinancial-assets.md](04_nonfinancial-assets.md) | Inventories (FIFO\|AVG only — LIFO banned 13.19), PPE component model + cost-OR-revaluation per class (10.10A prospective switch; surplus → OCI), intangibles finite-always + ALL internally generated expensed + goodwill ≤10y, Sección 27 impairment engine (CGU allocation, reversal caps), investment property, Sección 34 specialized activities; fiscal Art. 84 register / Art. 30 rates / non-deductibles consumed as SV-TAX-FR-038/052/081/150/165/167/170 by id (dismantling + lease classification route to `05` by filename — see reconciliation notes) (N4) | SV-COA-FR-093..134 | 42 | 7 | 14 | 3 |
| [05_liabilities-equity-benefits.md](05_liabilities-equity-benefits.md) | Provisions Sección 21 (SV-COA-FR-135..143) and the DUAL lease model Sección 20 (SV-COA-FR-144..152 — explicitly NOT IFRS 16), employee benefits Sección 28 (accumulating-absences vacaciones engine consuming SV-PAY-FR-004/044/047/063 by id; statutory ISSS/SIP booked DC-style; DB config-gated OFF), equity Sección 22 + the CC Arts. 37-38 distribution-capacity overlay (SV-CML-FR-053/054 by id; never auto-derived from NIIF equity — SV-COA-FR-177), distributions-at-declaration SV-COA-FR-175, grants (no SV catalog — config), borrowing costs ALL expensed (N5) | SV-COA-FR-135..181 | 47 | 7 | 11 | 4 |
| [06_revenue.md](06_revenue.md) | Sección 23 IFRS-15-aligned five-step engine + Apéndice 23A (modifications, warranties, material rights, principal-vs-agent, returns, licences, royalties), contract balances (asset vs receivable vs liability; whole-contract netting 23.77), contract costs; DTE credit/refund surfaces consumed as SV-EINV-FR-028/101/161 by id (N6) | SV-COA-FR-182..223 | 42 | 12 | 6 | 4 |
| [07_groups-related-parties.md](07_groups-related-parties.md) | Consolidation duty + exemptions, control model (agent/principal), consolidation mechanics + loss of control, NCI transactions as equity, separate/combined FS, business combinations (NCI at proportionate amount; goodwill formula), associates/JCEs, related-party disclosures (KMP remuneration fed from payroll by id), post-period events — including the 32.11 reporting-date no-liability half of the dividends rule (SV-COA-FR-251; declaration half stays `05` FR-175) and the puttable-at-parent case (AC-003 ↔ SV-COA-FR-167) (N7) | SV-COA-FR-224..252 | 29 | 7 | 10 | 3 |
| [08_deferred-tax-adoption.md](08_deferred-tax-adoption.md) | THE fiscal-by-id bridge: Sección 29 current/deferred tax (tax bases sourced from taxation registers BY FR ID — SV-TAX-FR-074/077/082/085/086/087/132/144/156 and SV-SPE-FR-023 exemption-schedule recovery; SV no-NOL ruling — only the capital-loss ledger grounds loss-DTAs), dividend WHT charged to equity (29.33 ↔ taxation/05), Pillar Two config-off, Sección 35 first-time adoption (mandatory exceptions + optional exemptions, adjustments → retained earnings), edition versioning via Tabla A1 (D12 two-vintage rows) (N8) | SV-COA-FR-253..276 | 24 | 5 | 6 | 5 |
| **Total** | | SV-COA-FR-001..276 | **276** | **57** | **76** | **30** |

Numbering note: FR numbering is wave-sequential within the **SV-COA**
prefix (001-276, no gaps, no renumbering); consumers cite by FR id, never
by restatement. The wave's spine is the fiscal-BY-ID discipline: every
book-vs-fiscal difference (FX clocks, depreciation bases, exemption
recovery, loss ledgers, dividend withholding) is recorded once by its
owning wave and consumed here by id — most concentrated in `08`'s
deferred-tax bridge.

## Cross-topic consumer map

**Consumed FROM this wave** (hooks landing here — sibling waves held the
pointers until this wave existed):

- **commercial-legal/03 FR-040** (`sv_cml_valuation_criteria_basis`:
  Consejo de Vigilancia criteria → "NIC" fallback, CC Arts. 443-444) is
  THE NIIF hook — consumed by `01` OQ-2 by id; the shared acquisition
  (Consejo criteria instrument) is tracked as SOQ-46 =
  commercial-legal/03 OQ-002.
- **taxation/06 depreciation interface**: the fiscal Art. 84 register and
  Art. 30/30-A rate rows stay taxation's (SV-TAX-FR-150/167/170 consumed
  by id in `04`); the depreciation ACCOUNTS the lines post to are this
  wave's — the two-track invariant.
- **commercial-legal/02 accounting-books rows** (Art. 439 no-alteration /
  immediate-rectification kin, cited as SV-CML-FR-024 by id in `01`):
  book structure consumed by pointer, never restated.

**Consumed BY this wave** (by id, never restated):

- **SV-TAX-FR-020** — CT Art. 62 two-clock fiscal FX rule (`03` §2 +
  SV-COA-FR-086: hecho-generador-day rate for tax bases; book FX never
  flows into the tax base).
- **SV-TAX-FR-038/052/081/165** — mermas deductibility, gravada/no-gravable
  segregation, costo básico and software-depreciation caps (`04`
  measurement boundaries); **SV-TAX-FR-150/167/170** — fiscal
  depreciation register and accumulated-depreciation exposure (`04`);
  **SV-TAX-FR-156** — leased-goods depreciation capitalization kin (`08`).
- **SV-TAX-FR-074/077/082/085/086/087** — progressive rates, 12-month
  capital-gain rule, capital-loss ledger, NO-general-NOL and securities
  routing (`08`: average-rate measurement, recovery-manner consistency and
  the SOQ-50 loss-DTA ruling); **SV-TAX-FR-132/144** — 5% dividend
  withholding + taxed-earnings register (`05`/`08` 29.33 equity charge);
  **SV-SPE-FR-023** — ZF/DPA dated exemption schedules as deferred-tax
  expected-recovery inputs (`05`/`08`).
- **SV-PAY-FR-004/044/047/063** — canonical salary-category matrix,
  vacaciones accrual (15d + 30%), vacation daily base and ISSS affiliate
  surfaces (`05`'s accumulating-absences and statutory-benefit engines;
  `07`'s KMP remuneration feed design).
- **SV-EINV-FR-159** — account.move transmission-state lock (`01`
  SV-COA-FR-018 distinctness: prior-period error restatement is a NOTES/
  comparative mechanism, never a fiscal-correction substitute);
  **SV-EINV-FR-028/101/161** — NCE/NDE adjustment routing and
  replacement-code rules (`06` contract-balance/DTE interfaces).
- **SV-CML-FR-041/053..056** — Art. 445 balances presentation, Arts. 37-38
  dividend ceiling, Art. 39 reserva legal (legal reserve) config +
  deployment (`02` equity classes; `05` distribution-capacity overlay and
  SV-COA-FR-177); **SV-CML-FR-048/049** — legal-personality and Art. 29
  capital-minimum kin (`05`/`07`).

## Open-questions rollup (in-file OQ-n ↔ master-index SOQ-46..53)

Status legend: all **30 OQs open** (0 resolved; `03` OQ-4 records its
fix-round resolution of the CT Art. 62 by-id citation while keeping the
rate-source and bridge-refresh halves open). Master-index SOQ register:
[§S8 open questions](../../.extractions/00_MASTER_INDEX.md).

| File | OQs | Mapping (in-file OQ → SOQ / kin) |
|------|-----|----------------------------------|
| 01 | 4 | OQ-1 SOQ-46 · OQ-2 SOQ-47 (R29(c) working reading; SV-CML-FR-040 hook) · OQ-3 SOQ-52 · OQ-4 SOQ-53 |
| 02 | 3 | OQ-1 SOQ-46 · OQ-2 balance-sheet/P&L layout gap (implementation design) · OQ-3 CFS/reconciliation layout gap (implementation design) |
| 03 | 4 | OQ-1 hedging applicability config note · OQ-2 loan/aging/prepayment Odoo mapping gaps · OQ-3 SOQ-46 · OQ-4 CT Art. 62 by-id RESOLVED (SV-TAX-FR-020); rate-source + `08` bridge refresh stay open |
| 04 | 3 | OQ-1 SOQ-46 · OQ-2 disproportionate-cost per-usage disclosures (notes design) · OQ-3 component-asset/revaluation/impairment Odoo mapping gaps |
| 05 | 4 | OQ-1 SOQ-49 (CC "utilidades realizadas por balance" bridge) · OQ-2 DB-applicability usage watch · OQ-3 SOQ-46 · OQ-4 SV government cash-grant instruments absent |
| 06 | 4 | OQ-1 deferred-revenue/contract-balance mapping gap · OQ-2 percentage-of-progress mapping gap · OQ-3 loyalty/material-right gap · OQ-4 SOQ-46 |
| 07 | 3 | OQ-1 SOQ-46 + consolidation-applicability kin · OQ-2 fiscal basis divergence watch (Ley ISR Art. 14 vs book carrying; `08` owns the bridge) · OQ-3 KMP remuneration payroll feed design |
| 08 | 5 | OQ-1 SOQ-48 (edition versioning; Tabla A1 artifact) · OQ-2 SOQ-50 (in-file ruling SV-COA-FR-258: no-NOL → capital-loss ledger only) · OQ-3 SOQ-51 (Pillar Two config-off) · OQ-4 SOQ-52 · OQ-5 consolidated-filing base practice (taxation-wave confirm) |

SOQ-46 rides every file as the verification preamble (W18 identity
verdict: authority chain OWNED — 76_/77_/78_ per the §2 notes of 01..08;
the criteria instrument — WHO applies NIIF-PYMES vs full NIIF per CC
Arts. 443-444 — STILL UNFOUND, candidates Res. 175-2023 [derogated] /
Res. 82-2024; the framework ships as a config-gap with NO invented
SV thresholds; external watch shared with commercial-legal/03 OQ-002).
33_ (EY guide) carries the NIIF 19
framework-flag third value (EVID-301) and the full-NIIF-vs-PYMES contrast
set as SECONDARY-ONLY authority.

## Authority note (R29)

Per master-index ruling R29 (W14): **32_** (Norma NIIF para las PYMES,
3rd edition, Feb-2025) is the operative framework LB of every file;
**33_** is SECONDARY-ONLY — never the sole LB of an FR, limited to
version/horizon facts and the documented contrast set (actual LB rows:
`01` LB-007, `03` LB-008, `05` LB-007, `07` LB-007, `08` LB-004). Where
guide and Norma could diverge, the Norma governs without exception.

## Reconciliation notes (carried from task reviews)

- **T4 (`04` FR-102/FR-126 → `05` ownership):** file 04 cites
  `05_liabilities-equity-benefits.md` by FILENAME for Sección 20/21
  surfaces — the owners are **SV-COA-FR-144..152** (Sección 20 leases,
  §3.2) and **SV-COA-FR-135..143** (Sección 21 provisions, §3.1):
  FR-102's PPE dismantling/removal estimate is a Sec 21 provision owned
  by FR-135..143; FR-126's leased-interest investment property routes to
  the lease model owned by FR-144..152. Read those pointers as these id
  ranges — no Sec 20/21 content lives in file 04.
- **T5 (`05` FR-163 payroll pointer + the 32.11 dual encoding):** FR-163
  (termination benefits) keeps the payroll-wave two-track pointer
  (computation stays SV-PAY by id); the 32.11 dividends rule is
  DELIBERATELY split — **`05` FR-175** owns the declaration-event
  boundary (distribution booked against equity when declared, never
  P&L) while **`07` FR-251** owns the reporting-date no-liability rule
  (dividends agreed after period end are not a liability; segregated
  retained-earnings presentation) consuming FR-175 by id. Do not
  double-count: one rule, two halves, cross-cited.
- **T7 (`05` FR-167 ↔ `07` AC-003):** FR-167(d) — a puttable instrument
  classified as equity in a subsidiary's FS is a LIABILITY in the
  controladora's FS — has its reverse pointer at `07` AC-003
  (puttable-at-parent consolidation case), which consumes FR-167 by id
  with the consolidation perimeter from the control model (FR-224),
  never from registry inscription.
- **T8 (`03`/`04`/`05`/`06` → `08` bridge pointers):** the by-filename
  deferred-tax bridges in files 03/04/05/06 land on
  **SV-COA-FR-253..269** (`08_deferred-tax-adoption.md`'s Sección 29
  income-tax engine) — read every `08` (T8) by-filename pointer as that
  id range.

## Wave-prep provenance

Built from W14 evidence (EVID-275..303) via master-index clusters N1-N8
and the SOQ-46..53 register — see
[§S8-A](../../.extractions/00_MASTER_INDEX.md) (chart-of-accounts
authority order, citation rule and per-cluster covers). R29 authority
rulings (33_ secondary-only; 32_ Prólogo P12 applicability gap; the CC
Arts. 443-444 "NIC" working reading) are applied throughout; the
SOQ-46..53 register is carried as in-file OQs (rollup above).
Cross-topic source coverage: [../COVERAGE.md](../COVERAGE.md).
