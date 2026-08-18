# SV — Taxation (ISR) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S2 ISR synthesis wave, in review) |
| Authors | Takumi synthesis wave 2 + controller |
| Updated | 2026-08-18 |

This directory holds the S2 (synthesis wave 2) ISR (*Impuesto sobre la
Renta*, income tax) requirements: the subject/period/territoriality/filing
framework, renta neta deductions, rates & special computations, withholding
(payroll tables + CT retention matrix), the 5% distributions regime, and
fixed-asset depreciation/software amortization — with the retention/bracket
tables as verbatim dated data in two CSV sidecars. Source-to-requirements
coverage: [../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_isr-framework.md](01_isr-framework.md) | Subjects, renta obtenida categories, Art. 6 exclusions, periods & cash/accrual methods, territoriality (D.L. 969-2024 exclusion, Art. 127 apportionment), FX, Art. 92 filing duties | SV-TAX-FR-001..033 | 33 | 31 | 17 | 6 |
| [02_isr-deductions.md](02_isr-deductions.md) | Renta neta: Art. 28 pro-rata (+969 carve-out), Art. 29 deductions, Art. 29-A non-deductibles (thin-cap, 25-SMM cash ban), Arts. 31-32 (reserva legal, bad debts, donations), mermas (D.L. 345-2019), Reglamento segregation | SV-TAX-FR-034..073 | 40 | 18 | 22 | 7 |
| [03_isr-rates-gains.md](03_isr-rates-gains.md) | Art. 37 brackets (both dated vintages), Art. 41 entity rates, capital gains (10% separate, 12-month rule, no general NOL), securities/deposits 10%, special computations (instalments, repossession, annuities, export valuation); SOQ-01/04 verdicts in §7 | SV-TAX-FR-074..101 | 28 | 19 | 23 | 9 |
| [04_isr-withholding.md](04_isr-withholding.md) | Salaried retention regime (base, $1,600 fixed deduction, Art. 33 deductions), D.E. 10-2025 periodic + June/December recálculo tables, aguinaldo vintages, multi-employer split, CT 154-160 non-payroll matrix; CSVs `withholding_tables.csv` (20 rows) + `isr_brackets.csv` (23 rows) | SV-TAX-FR-102..131 | 30 | 21 | 18 | 8 |
| [05_isr-distributions.md](05_isr-distributions.md) | Art. 72 5% definitive retention on utilidades, Arts. 73-74-C (permanent establishments, capital reductions, partner-loan deemed distributions, no-retention cases), Registro de Control de Utilidades | SV-TAX-FR-132..149 | 18 | 11 | 18 | 7 |
| [06_isr-assets.md](06_isr-assets.md) | Art. 30 depreciation (rates, used-asset caps, mixed-use pro-rata, seasonal quota), Art. 30-A software 25%, Reglamento Art. 84 per-asset register, Art. 35 maquinaria | SV-TAX-FR-150..172 | 23 | 11 | 20 | 7 |
| **Total** | | SV-TAX-FR-001..172 | **172** | **111** | **118** | **44** |

Numbering note: FR numbering is wave-sequential within the `SV-TAX` prefix
(001-172, no gaps, no renumbering) — unlike S1's per-cluster EINV ranges.
The two CSVs are dated-data sidecars of `04_isr-withholding.md`
(`isr_brackets.csv` additionally carries the historical D.E. 25-1992
colones-era vintage rows); they carry no FRs of their own.

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. 40 open / 4 resolved
(SOQ-01 and SOQ-04 in `03_isr-rates-gains.md` §7; SOQ-03 in `04`
OQ-002 + `01` OQ-005 — D.O. pin + digit-fidelity verification against
the gazette print, source `60_`/EVID-171, 2026-08-18).

Master-index SOQ mapping: 04's OQ-001 = SOQ-02; 04's OQ-002 = SOQ-03;
04's OQ-003 = SOQ-05; SOQ-06 lives in 01's OQ-004 + 06's OQ-001; SOQ-07
in 03's OQ-007 (kin: 02's OQ-006). SOQ-01/SOQ-04 = 03's OQ-001/OQ-002,
resolved.

### 01_isr-framework.md (6)

- OQ-001 — Ley Art. 62 retention-remittance deadline vs CT retention-agent regime (CT re-anchor check). open
- OQ-002 — Art. 92 num. 9 obsolete stamp-tax duty; CT-era restatement of the filing-duty list. open
- OQ-003 — Art. 105-A stale sanction (repealed anchor, colon minimum) disposition. open
- OQ-004 — SOQ-06 carried: D.E. 117-2001 survivors vs later CT Art. 344 ff. repeals. open
- OQ-005 — SOQ-03 (partial): D.E. 10-2025 publishing D.O. issue unpinned (vigencia 2025-05-08 assumed). **resolved** (60_/EVID-171: D.O. 79 T.447 30-abr-2025, effective 2025-05-08)
- OQ-006 — CT Art. 62 FX conversion: operational rate source/feed selection. open

### 02_isr-deductions.md (7)

- OQ-001 — Art. 28 inciso final pro-rata factor vs Reglamento Art. 32 flat 50/50 common-cost split. open
- OQ-002 — SMM parameter source for the 25-SMM cash-payment ban threshold. open
- OQ-003 — BCR active-rate feed for the thin-cap active-rate + 4 points test. open
- OQ-004 — Art. 31.3 bank/insurer reserve regime: deferral to special-regimes wave. open
- OQ-005 — Registry of legally-authorized associations/cooperatives (social funds validation). open
- OQ-006 — Reglamento Art. 29 deposit-interest exclusion stale vs Ley Art. 4.5 (SOQ-07 kin). open
- OQ-007 — Art. 29.6 December window for deductible taxes vs CT deadline rules. open

### 03_isr-rates-gains.md (9)

- OQ-001 — **SOQ-01 verdict (recorded):** Ley Art. 42 flat 10% governs all current periods/classes (54_ pp.39-40, stamp (14) = D.L. 496-2004); Reglamento Art. 17 media-tasa = historical pre-2004 method (LB-010). **resolved**
- OQ-002 — **SOQ-04 verdict (recorded):** NO general NOL carryforward exists (CT/04_ scans negative); only capital losses per Arts. 14/14-A (5-year gains-only ledger). **resolved**
- OQ-003 — Art. 41 US$150,000 threshold: no indexation mechanism in corpus. open
- OQ-004 — "Interés legal" rate feed (life annuities, interest presumption). open
- OQ-005 — Securities price-floor feed (exchange quotation / emitter book values). open
- OQ-006 — DGII calculation-form layouts (capital gain/loss, rentas de capital, capital-loss declaration). open
- OQ-007 — SOQ-07 deposit reading: average-balance computation detail (per-institution vs aggregated). open
- OQ-008 — Insurer/fianza determination + pre-1992 patrimonio-tax basis rows: deferral check. open
- OQ-009 — Art. 37 vintage straddle: single 2025 annual liquidation across the 2025-05-08 cutover (period-close selection rule as working assumption). open

### 04_isr-withholding.md (8)

- OQ-001 — SOQ-02: $1,600 fixed-deduction proration (quincenal/semanal Tramo II) + ordering vs SS/AFP netting. open — working assumption implemented (FR-103/104)
- OQ-002 — SOQ-03: D.E. 10-2025 provenance (publishing D.O. issue) + printed-digit anomalies. **resolved** (60_/EVID-171: effective 2025-05-08 confirmed; all anomaly digits gazette-original)
- OQ-003 — SOQ-05: 2025/2026 aguinaldo transitory (standing 2-SMM rule assumed for 2025+). open
- OQ-004 — Part-time without subordination: retention tables vs 10% honorarios rule. open
- OQ-005 — Retention-decree chain gap D.E. 25-1992 → D.E. 95-2015 (pre-2025-05-08 tables absent). open
- OQ-006 — 10_ 1992 vintage print anomalies (row-3 offsets, quincenal overlap, semanal typo). open
- OQ-007 — MOQ-10 kin: electronic reporting surface for ISR retentions (CT 123/123-A). open (partially answered by S3: F-910/F-915 — see `../fiscal-reporting/07_codes-and-informs.md` §7)
- OQ-008 — Art. 37 straddle kin for WITHHOLDING: wages earned 1-Jan–7-May-2025. open

### 05_isr-distributions.md (7)

- OQ-001 — CT Art. 158-A carve-out scope beyond the 25% tax-haven rate. open
- OQ-002 — Art. 74-C Registro de Control de Utilidades: DGII administrative norms. open (partially answered by S3: F-910/F-915 — see `../fiscal-reporting/07_codes-and-informs.md` §7)
- OQ-003 — Art. 74-A override mechanics (total-consideration reading, mora/quota measurement). open
- OQ-004 — Pool-consumption ordering for ordinary distributions (untaxed-pool default). open
- OQ-005 — Art. 25 inciso 1 vs inciso 2 deemed-loan overlap (exception sets). open
- OQ-006 — Electronic reporting surface for the 5% retention (MOQ-10 kin). open
- OQ-007 — Exemption-proof artifact class for Art. 74-B final inciso. open

### 06_isr-assets.md (7)

- OQ-001 — Reglamento Art. 84 vs CT Arts. 139-143 books/records regime (SOQ-06 carried). open
- OQ-002 — Seasonal-activity qualification list ("actividades estacionales"). open
- OQ-003 — Part-year pro-rata convention: months vs day-count. open
- OQ-004 — Used-asset "AÑOS DE VIDA" measurement + new-price cap evidence classes. open
- OQ-005 — Depreciation-register format norms beyond Art. 84's minimum field list. open
- OQ-006 — Mejoras/adiciones mechanics: own forward quota vs life extension vs restart. open
- OQ-007 — Software schedule span: >25% authorizations and slower-schedule practice. open
