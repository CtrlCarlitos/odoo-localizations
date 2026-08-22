# HN — Taxation requirements index

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | approved (V-HN1 validation wave 2026-08-20; see EXTRACTION_PLAN wave log) |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-20 |

This directory holds the S-HN1 (synthesis wave HN-1) taxation
requirements: the ISR framework + Código Tributario chassis, renta-neta
deductions, 22-A minimum tax + ganancias de capital + non-resident
withholding, the asalariados plantilla/retention engines with the
FY2022-2026 bracket vintages as a dated CSV sidecar, the D. 17-2010
cédula/selectivo family, the ISV core + liquidation regime, and special
regimes/exonerations. Built from master-index clusters T1-T12 (W1
evidence, EVID-001..071); F/P/E clusters are consumed by id, never
re-derived. Source-to-requirements coverage: [../COVERAGE.md](../COVERAGE.md)
(to be generated at S-wave validation).

**W10 wave (2026-08-21) fold-ins:** file 01 +LB-025 (the CT-131 descargo
executing pair SAR-125-2024/SAR-43-2026 — FR-037's discharge engine statute-
anchored, emission-time umbral semantics demonstrated twice); file 06 +LB-020
(D. 7-2017 original = the OTCD 50%→10%/15% middle instrument — FR-249's
fallback trigger/base now primary-text, regime rows dated 8-mar-2017).

## Files & FR ranges

| File | Scope (clusters) | FR range | FRs | LBs | ACs | OQs |
|------|------------------|----------|-----|-----|-----|-----|
| [01_isr-framework.md](01_isr-framework.md) | Subjects/scope/rates overview, fiscal periods, books, entero, refunds, prescription, sanctions (T1+T11); Art. 206 void dead-text note (R-H5) | HN-TAX-FR-001..045 | 45 | 25 | 24 | 7 |
| [02_isr-deductions.md](02_isr-deductions.md) | Renta-neta chassis, bad-debt cap, non-deductibles, personal/senior stack (65+ chain continuity W9), donations, NOL (T2) | HN-TAX-FR-046..078 | 33 | 18 | 16 | 9 |
| [03_isr-rates-gains-minimum.md](03_isr-rates-gains-minimum.md) | 22-A gross-minimum (regime 0 FY2014-FY2017 extended W9 from the acquired `130_` original text + three dated regimes, R-H32), ganancias de capital 10%, non-resident 13-category table (T4+T5) | HN-TAX-FR-081..104 | 24 | 14 | 20 | 8 |
| [04_isr-withholding.md](04_isr-withholding.md) | Plantilla computation contract, FY2022-2026 scale vintages (`isr_brackets.csv`), 12.5% services + 1% compras engines, entero anchor (T3+T6) | HN-TAX-FR-121..153 | 33 | 15 | 19 | 10 |
| [05_d17-2010-family.md](05_d17-2010-family.md) | Dividends/deemed dividends, cédulas alquiler/enseñanza, revaluación, selectivo vehicles/cigarettes/beverages/slots (T7+T10) | HN-TAX-FR-166..207 | 42 | 16 | 20 | 8 |
| [06_isv.md](06_isv.md) | ISV base/event/rates/exemptions, débito-crérdito liquidation, OTCD cards, simplificado, devolución 8% (T8+T9) | HN-TAX-FR-211..255 | 45 | 20 | 20 | 6 |
| [07_special-regimes-exonerations.md](07_special-regimes-exonerations.md) | Exonerations registry lifecycle, RIT, no-simultaneidad, sacrificio fiscal, state-side gates, Eficiencia closers, turismo family incl. D. 68-2017 current stack (T12; W8) | HN-TAX-FR-256..282 | 27 | 12 | 21 | 8 |
| **Total** | | HN-TAX-FR-001..282 | **249** | **120** | **140** | **56** |

Numbering note: FR ranges pre-allocated per file (subagent dispatch
pattern); unused tail numbers stay reserved (079-080, 105-120, 154-165,
208-210, 282-285) for later additions — no renumbering. V-HN1 changed no
FR ids in this topic (AC/OQ additions only; all adjudications recorded in
the EXTRACTION_PLAN wave log). The
`isr_brackets.csv` sidecar carries the PN annual progressive vintages
(FY2022-2026, 5 × 4 bands, full-precision mechanism per R-H10 — print
2dp is print-only); it carries no FRs of its own.

## Wave rulings & carries (controller notes)

- **Territoriality (origin `03_ OQ-1`) — R-H66 ADOPTED 2026-08-20 by
  product owner:** file 01's FR-004 encodes dated regime rows (worldwide
  pre-2017 / territorial 2017+); OQ-001 resolved (rows remain reversible
  if a contrary instrument lands — flip without code change).
- **Resolved at synthesis (verified by controller):** `01_ OQ-4`
  (10-SMM caps = excess-only, never cliff — proven by the plantilla IF
  semantics, EV07:EVID-055; file 02 OQ-002); `07_ OQ-2` FY2026 leg
  (promedio L14,917.20 → cap L149,172.00 per R-H47/EVID-228; missing
  promedio vintages stay DGS-print leads, P1 owns the rows); `04_ OQ-4`
  (DAR superseded by DJIMR per R-H31 — file 05 OQ-002).
- **Evidence-over-brief corrections (encoded per evidence, not brief):**
  bad-debt cap = 10% of closing client AR (not "prior-year bad debts");
  L30k@60 senior tier attributed to D. 199-2006 per plantilla citation
  (unacquired — row ships activation-blocked, file 02 OQ-008).
- **Cross-wave dependencies:** SMM-promedio rows consumed from
  `../payroll/` (P1, future S-HN4 — R-H47: never recompute); IPC-chain
  current values (98_/99_/100_) ride the selectivo/F9 side of S-HN3;
  OVI/SW declaration chassis = F1 (S-HN3); fiscal-document retention
  surfaces = `../e-invoicing/` (S-HN2, same session).

## Open-questions summary

54 open OQs (wave total), highest-leverage: Reglamento Ley ISR
("Acuerdo N°799" — depreciation/personal-deduction mechanics, cited 5×
across the corpus), D. 199-2006 original (senior-tier anchor), Instructivo
461-2020 (22-A petitions), devolución-8% when-it-applies instruments,
Anexo I canonical source decision. Full text per file §7; register
mapping to master-index C1 recorded per file.
