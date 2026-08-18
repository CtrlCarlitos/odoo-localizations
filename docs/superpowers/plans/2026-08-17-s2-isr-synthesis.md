# S2 Synthesis Implementation Plan — sv taxation (ISR) Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W6+W7 ISR evidence base (EVID-088..170, master-index clusters T1–T8) into Takumi-contract requirements files under `sv/requirements/taxation/`, with FR numbering `SV-TAX-FR-nnn`, LB citations to current authority (54_/53_ + reform decrees), dated-data version regimes (Art. 37 vintages, D.E. 10-2025 tables, 969-2024 cutover), layer split, ACs, and coverage tracking.

**Architecture:** Requirements follow the 7-section template; the master index Section S2-A (T1–T8) is the synthesis worklist and its rulings R17–R22 are binding; dated legal data (brackets, retention tables) ships as machine-readable CSV sidecars next to the markdown with valid_from/valid_to columns (D8/D9/D11 discipline — additive dated rows, never in-place edits). This wave is ISR ONLY: IVA-core files (02_Reglamento_IVA et al.) come in a later taxation wave; payroll contributions/labor rules come in the payroll wave.

**Tech Stack:** Markdown; CSV sidecars (hand-built this wave from 53_/55_ evidence); FR IDs `SV-TAX-FR-nnn`.

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` Section S2-A + R17–R22 + SOQ-01..07 (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (D7–D12 version-regime policy).

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + article/page). No trace → OQ, not FR.
- **ISR authority order (binding):** 54_ (current consolidated Ley; reform decrees 55_ Art. 37 / 56_ Art. 3.4+derogations / 57_ Art. 30.1 / 58_ Art. 28 for changed articles) > 03_ (historical, through D.L. 233-2012). Tables: 53_ (D.E. 10-2025, operative) > 10_ (1992, historical). Reglamento: 04_ = D.E. 101-1992 consolidated incl. D.E. 117-2001 repeal map (R17) — cite survivors only.
- **54_-verify rule (from EVID-166):** the W7 delta pass verified only changed + worry-list articles; therefore every implementer MUST re-read the article text in `sv/.extractions/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf.txt` for each article they cite (grep by article number; quote from 54_, not from 03_-era EVID glosses). 03_/10_ EVIDs supply the analysis; 54_/53_ supply the citation.
- **Dead text — never cite as current:** pago mínimo Arts. 76-81 (R21, unconstitutional); EVID-094 foreign-securities/deposit paragraphs + EVID-092 anti-exemption gross-up for foreign rents (R18, D.L. 969-2024); Art. 17 media-tasa as a live method (pending SOQ-01 resolution in Task 3); 10_ tables as operative data (R19).
- **Version regime (D12):** any FR whose amounts/rules changed over time records vintage + effective date in the Odoo Mapping notes: Art. 37 two vintages (957-2011 config ≤2025-05-07; 293-2025 config from 2025-05-08); foreign-exclusion cutover 2024-03-22; aguinaldo vintages (2014-2018 full exemption; 2021 $1,100; 2022-2024 $1,500; 2025+ 2-SMM standing per R22/SOQ-05); retention-table decree chain (D.E. 25-1992 → D.E. 95-2015 → D.E. 10-2025).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification). Default for this wave: computation/bookkeeping/payroll withholding = `odoo`; dated legal data ships as normative packs (D11) = `odoo` data + version notes; SaaS delivery of packs is NOT required by any current decision — do not invent saas Layer rows without an ARCH/D-citation justification.
- English prose, Spanish legal terms inline with translation on first use.
- OQs recorded as rows in-file §7 AND rolled up by the index task; never silently dropped.
- Cross-topic discipline: cite existing FR IDs (SV-EINV/SV-PROT/SV-CAT) by reference; never duplicate their content. Payroll boundary: ISR retention mechanics (rates, tables, bases, recálculo, thresholds) live HERE; ISSS/AFP contributions, labor contracts, SMM figures catalog = payroll wave (16_). IVA retentions/perceptions (1%/13%/2%) already owned by e-invoicing A10 cluster — reference only.
- SOQ handling this wave: SOQ-01 + SOQ-04 are RESOLVED BY Task 3 (verification reads, verdicts recorded in-file + index); SOQ-02/03/05/06/07 are recorded as OQ rows (with working assumptions as stated in the master index).
- Files land in `sv/requirements/taxation/` following the template exactly (7 sections, none deleted).

---

### Task 1: `sv/requirements/taxation/01_isr-framework.md`

**Files:** Create `sv/requirements/taxation/01_isr-framework.md`
**Covers master clusters:** T1 + T2 + T8
**FR numbering:** SV-TAX-FR-001..0NN (opens the prefix)
**Content requirements:**
- T1: renta-obtenida concept & categories (trabajo/empresarial/capital/catch-all incl. condoned debts, excess provisions, unjustified patrimony increment per CT 195); subjects incl. sucesiones/fideicomisos/conjuntos/irregular societies; Art. 6 exclusions + utilidad-pública qualification (12-month auto-renewal per 04_ Art. 7); fiscal year Jan-Dec; cash vs accrual per taxpayer type with irrevocable accrual election for natural persons (Nov-Dec informing); estate/trust period splits; branch consolidation; FX conversion rule (CT Art. 62: hecho-generador-day rate; installment FX deltas into base; payment-date FX difference never in base).
- T2: SV-source classifier (goods/services-used-in-country/IP/securities/government remunerations); Art. 127 partial-territory apportionment worksheet; D.L. 969-2024 foreign-source exclusion (Art. 3.4) + Art. 28 pro-rata carve-out for mixed subjects; dead-track note (R18) recorded in LB notes, not as FRs; domestic 10% tracks survival.
- T8: annual declaration 4-month window; Art. 92 filing-duty catalog incl. IVA-registration-driven duty + salaried exceptions ($9,100/$60,000); conjunto event returns (día hábil siguiente, solidarity); online-only filing (53_ Art. 2, informational); retention remittance 10 días hábiles + December rule (flag: likely CT-superseded — record as OQ, cite CT zone); procedure-routing map (Ley ~70 repealed arts; Reglamento 117-2001 map) as a Legal-Basis note, not FRs.
**Special steps:** verify each cited article against 54_ txt (54_-verify rule); CT Art. 62 quote from `05_Codigo_Tributario.pdf.txt` lines 840-844 (already captured in master index T1 LB row).

### Task 2: `sv/requirements/taxation/02_isr-deductions.md`

**Files:** Create `sv/requirements/taxation/02_isr-deductions.md`
**Covers:** T3
**FR numbering:** continues SV-TAX prefix sequentially from Task 1's last FR.
**Content requirements:**
- Art. 28 necessary-cost gate + gravadas/(gravadas+no gravadas+no renta) pro-rata allocator + 969-2024 carve-out (subjects with foreign-excluded concepts are OUTSIDE the pro-rata); mermas/pérdidas deductibility (D.L. 345-2019: inherent, measurable, real-cost, documented + regulator-recognized; zero-base guard — no deduction when no tax computes).
- Art. 29 numerals as deduction rules: business expenses vs perks blacklist; remunerations conditioned on SS+ISR retentions effected & entered; relatives-payments proof rule; foreign travel + domestic viáticos; leases pro-rata; insurance (50% home-office cap for natural persons); taxes caused & paid (December rule) excluding ISR/IVA/fines; fuel whitelist by vehicle-use; ordinary repairs vs improvement capitalization; interest rules (allocation, non-gravable-asset capitalization, own-capital interest, preferred-share "interest" = dividends, back-to-back cap); inventories/COGS tied to CT 142-143.
- Art. 29-A non-deductible classifier: retention-linked block (incl. December closing rule); interest/commissions non-deductibility conditions (unrelated-lender declaration, active-rate+4pts related/foreign preferential lender, thin-cap 3:1 average equity with financial-entity exemption); IVA-document-defect block; ≥25 SMM cash-payment disallowance (contract alternative); undocumented/unrecorded costs (CPA-certified closing exception); fines/moratory interest; obsolete-inventory losses; accounting provisions; capital losses from ordinary income; goodwill/intangibles amortization.
- Art. 31-32: reserva legal 25% separate liquidation (constitution/deduction/reduction cycle); bad-debt deduction (conditions + 04_ Art. 37 evidence checklist) + recovery-income cycle; donations 20%-of-net cap, qualified-donee validation (ties to T1 Art. 6 qualification), family-benefiticiary block; social-benefit expenses (housing/schools/medical/cultural, sindicato cuotas with CT 115-A/146 refs, ISSS patronal); employer social funds dedicated account + domestic-fund + incorporation proof (04_ Art. 141).
- Reglamento 32: P&L fiscal-adjustment layer (add-back non-deductibles, untaxed income) + gravable/no-gravable ledger segregation + 50/50 common-cost split (explicitly NOT the IVA Art. 66 sales-based proration — different tax, note the distinction).
**Special steps:** 54_-verify rule; the payroll-gate FR cross-references Task 4's withholding FRs by ID (interface below).

### Task 3: `sv/requirements/taxation/03_isr-rates-gains.md`

**Files:** Create `sv/requirements/taxation/03_isr-rates-gains.md`
**Covers:** T4
**FR numbering:** continues SV-TAX prefix.
**Content requirements:**
- Art. 37 progressive computation as dated data: full verbatim tables for BOTH vintages (R20); final-withheld rents excluded from base; non-resident natural persons/sucesiones/fideicomisos 30% flat.
- Art. 41: 30% entities / 25% ≤ $150,000 gravadas (threshold semantics: which year's gravadas, switching behavior); foreign conjuntos 5% gross per event (Art. 40).
- Capital gains: 12-month rule (10% separate liquidation vs ordinary inclusion); per-transaction result = value − costo básico (cost − accumulated admitted depreciation) − conservación improvements − transaction expenses; donated/inherited basis carryover; habituality test (04_ Art. 15 presumptions); holding-period counting (04_ Art. 16); banks/insurers/official-credit extraordinary liquidations = ordinary; capital-loss ledger (offset capital gains only, 5-year carryforward, DGII form declaration, no cross-type offset).
- Securities/deposits 10% separate liquidation (domestic only post-969): weighted-average cost per species; transfer result (price ≥ stock-exchange quote else book value); loss netting same-period + 5y; retention = definitive → no declaration; deposit-interest small-depositor carve-out note (Art. 4.5 < $25k avg balance — harmonized reading, SOQ-07).
- Special computations: >24-month instalment deferral (habitual traders; proportional to pending quotas; capital gains excluded); repossession gain/loss; rent-with-promise-to-sell; POC >1-year contracts (revenue AND costs proportionally — 04_ Art. 27); life annuity algorithm; interest presumption (every credit yields legal interest — rate outside corpus, note); insurer/fianza net-income determination (04_ Art. 33, awareness-level); export income valuation (04_ Art. 34); reserva legal 25% (cross-ref Task 2's FR).
- Losses: NO general NOL carryforward FR (subject to SOQ-04 scan below); zero-base guard cross-ref (345-2019).
**Special steps (SOQ-01, SOQ-04 — resolve, record verdicts in-file §7 and flag for index update):**
- [ ] SOQ-01: read `54_...pdf.txt` Art. 42 region (grep "Artículo 42" / "ganancia neta de capital") + its reform stamps; verdict on whether Reglamento Art. 17 media-tasa survives for any taxpayer class. Expected: Ley Art. 42 governs current periods; Art. 17 = historical (pre-957-2011) method — write the FR on Art. 42 and record Art. 17 as historical LB note; if stamps show otherwise, write both tracks as dated regimes instead.
- [ ] SOQ-04: `rg -n "pérdida" sv/.extractions/05_Codigo_Tributario.pdf.txt` + 04_ txt scan for pérdida-fiscal carryforward; verdict recorded (expected: none — only capital losses; if found, cite and write the NOL FR).

### Task 4: `sv/requirements/taxation/04_isr-withholding.md` + CSV sidecars

**Files:** Create `sv/requirements/taxation/04_isr-withholding.md`, `sv/requirements/taxation/isr_brackets.csv`, `sv/requirements/taxation/withholding_tables.csv`
**Covers:** T5
**FR numbering:** continues SV-TAX prefix.
**Content requirements:**
- Salaried regime: retention = definitive payment; $1,600 fixed deduction (Art. 29.7, no comprobación, embedded in retention per law) + Tramo II non-embedding (53_ e); $800×2 personal deductions (Art. 33: medical incl. parents/spouse/children<25/domestics, education; 6-year record retention); $9,100 no-liquidation threshold; >$60,000 must declare; ISSS/SSF/AFP information exchange note.
- Tables as data: D.E. 10-2025 monthly/quincenal/semanal + June/December recálculo tables transcribed EXACTLY as printed into `withholding_tables.csv` (columns: decree, valid_from, valid_to, frequency, tramo, from_amount, to_amount, rate_pct, over_excess_of, fixed_quota, note) — [sic] anomalies in the note column, never silently corrected (SOQ-03); `isr_brackets.csv` with both Art. 37 vintages (columns: vintage/valid_from/valid_to, tramo, from_amount, to_amount, rate_pct, over_excess_of, fixed_quota, scope) + the 10_/D.E. 25-1992 rows as historical vintages; dated-data loading FR (select by period date — D7/D12).
- Base definition (53_ d): bruto − remuneraciones no gravadas − cotizaciones laborales SS (ISSS) − cotizaciones previsionales (AFP/public pension); employer contributions NOT netted; ordering before table lookup.
- June/December recálculo engine: cumulative gravadas → table → minus Jan-May / Jan-Nov retentions → max(0, diff); exclusions (definitive-retention remunerations; 10% multi-employer amounts); last-employer responsibility; CT 145 constancia within 15 días hábiles; Tramo II $1,600 in recálculo; >$9,100 → Art. 33 deductions instead.
- Special periods: regla-de-tres monthly equivalence; extraordinary remunerations (aguinaldo/vacaciones/bonificaciones) aggregation rules (same-date netting; last-remuneration deduction).
- Multi-employer: table on highest-paying + flat 10% on the rest (excluded from recálculo); aggregate < exemption → none; January/15-días information duty; equal-rents designation; voluntary retention increase via DGII form.
- Aguinaldo: Art. 4.16 standing rule (exempt ≤ 2 SMM comercio y servicios; excess retained with floor DEDUCED — 458-2019 wording); vintage rows 2021-2024 $ caps; 2025+ standing (SOQ-05 note).
- CT non-payroll retention matrix (cite EVID-062/063; FRs to the extent they configure Odoo payment flows): honorarios/independent natural persons 10% (advances included; agricultural harvest labor excluded); leases to natural persons 10%; intangibles 10%/5%; capital yields/dividend advances 10% (keep DISTINCT from Art. 72's 5% — cross-ref Task 5); courts 10% judgment interest; non-residents 20% definitive with reduced rates (5% international transport, 5% reinsurers, 10% qualified foreign financing, 20% related-party financing, 5% film/TV); tax-haven subjects 25% (158-A); financial institutions deposits definitive (159); raffles/prizes (160).
- Part-time/hourly (class-hours, medical-hours) = servicio permanente → tables not 10% (04_ Art. 59; note the subordination qualifier question as OQ — 04_ OQ-5).
**Interfaces:** Task 2's payroll-deductibility gate FR cites this file's base/threshold FRs by ID; Task 5's 5% FRs cross-reference the 156-B 10% distinction.

### Task 5: `sv/requirements/taxation/05_isr-distributions.md`

**Files:** Create `sv/requirements/taxation/05_isr-distributions.md`
**Covers:** T6
**FR numbering:** continues SV-TAX prefix.
**Content requirements:**
- Art. 72: 5% retention on paid/credited utilidades (definitive, domiciled or not); "utilidades" broad definition (gravadas+exentas+no sujetas − costs − ISR of Arts. 37/41); payment/credit events (cash, títulos, in-kind, compensation, loss application, accounting operations); no-declaration when retained; separate declaration + 5% when not.
- Art. 73 permanent establishments → non-domiciliaries; Art. 74 capital reductions (capitalized/reinvested earnings portion, profits-first); Art. 74-A loans to partners/related/preferential-regime/head-office (5%; exceptions: market-or-better interest, regulated/habitual credit institutions, inter-institutional, State borrowers; default >6 installments or term >1y → total consideration = gravable + interest non-deductible); Art. 74-B no-retention cases (prior-taxed profits; capitalization in nominative shares; reinvestment by entes sin personalidad; State/municipal/public/coop-federation recipients; autonomous institutions NOT excepted); Art. 74-C Registro de Control de Utilidades (per-exercise, per-shareholder: determination, paid/credited, capitalization/reinvestment, capital reductions; accounting-consistent; CT 242 b)/c)1) sanction ref); Art. 25 society loans to shareholders/family = dividends; exempt-entity distribution flow-through (04_ Art. 18); CT 158-A carve-out noted as OQ-scope (collect from CT zone).
- Data model: per-shareholder earnings register entity (taxed vs untaxed profit pools) — EDA-style; capitalization/reinvestment events.

### Task 6: `sv/requirements/taxation/06_isr-assets.md`

**Files:** Create `sv/requirements/taxation/06_isr-assets.md`
**Covers:** T7
**FR numbering:** continues SV-TAX prefix.
**Content requirements:**
- Art. 30: category rates 5/20/25/50% (edificaciones/maquinaria/vehículos/otros) as maxima; used-asset base caps 80/60/40/20% by age; ≤12-month assets → full cost in year of greater use; annual quota fixed & constant; part-year pro-rata; construction/production assets → capitalize into built cost (deduct on sale); no revaluation; owner-only depreciation; land never; mixed-use Art. 28 pro-rata; no catch-up of missed quotas; DGII authorization for % changes; IVA-exempt import machinery DGII-value cap.
- Seasonal activities (D.L. 192-2018): FULL annual quota regardless of season length; open-list flag (cafetalero/cañero exemplars) → per-company/asset config, not a hard-coded sector list.
- Art. 30-A software: 25% max, 4-year mirror rules; used-software caps.
- Depreciation register (04_ Art. 84 field list verbatim): specification, depreciable value, in-use start date, useful-life period, improvements, additions, quota, balance, retirement, disposal + nature-demanded extras; block after full redemption; maquinaria definition (04_ Art. 35) for classification.
- Odoo mapping: account.asset templates per category with legal maxima as defaults; seasonal flag; register = asset model fields + history.
**Interfaces:** Task 3's capital-gain FRs cite this file's accumulated-depreciation/basis FRs by ID.

### Task 7: `sv/requirements/taxation/00_index.md` + `sv/requirements/COVERAGE.md` + README updates

**Files:** Create `sv/requirements/taxation/00_index.md`; update `sv/requirements/COVERAGE.md` (ISR rows → cited-as-LB with citing files; rollup counts); update `sv/README.md` + `sv/requirements/README.md` status flips.
**Content requirements:** index file (per-file FR ranges/counts/LBs/ACs/OQs; numbering note: wave-sequential within SV-TAX prefix; OQ rollup with SOQ-01/04 verdicts + still-open SOQ-02/03/05/06/07 mapped to file OQ ids); COVERAGE.md rows for 03_/04_/10_ → cited-as-LB (historical), 53_/54_/55_/56_/57_/58_ → cited-as-LB (current); rollup table updated; README topic status taxation → in review.

## Standing review gates (every task)

1. Fresh implementer subagent per task; reviewer subagent verifies against master index T-clusters + R17-R22 + this plan's Global Constraints (SDD loop).
2. Reviewer checks: every FR has LB citing 54_/53_/reform-decree (current) vs historical mark; no dead-text citations (R18/R19/R21); version-regime notes present where vintages exist; Layer column complete; OQs recorded; template's 7 sections intact; cross-file references by FR ID not content duplication.
3. Fix rounds per SDD; findings ledger kept in the SDD workspace; at wave close, rulings copied to HANDOVER.md BEFORE workspace deletion.
