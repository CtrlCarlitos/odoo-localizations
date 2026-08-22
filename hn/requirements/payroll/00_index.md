# HN — Payroll requirements index

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | approved (V-HN1 validation wave 2026-08-20; W5 amendment — D. 112 unblock + bono reglamento + Acuerdo 345; see EXTRACTION_PLAN wave log) |
| Authors | Takumi synthesis wave S-HN4 + controller; W5 wave | 
| Updated | 2026-08-20 |

This directory holds the S-HN4 (synthesis wave HN-4) payroll
requirements: the SMM chassis (Ley D. 103 machinery + bienio 2022-2027
dated tables + maquila/zonas-libres track + the DGS promedio sidecar rows),
the complementary-pay family (**13th-month aguinaldo = D. 112-1982 statutory
engine — W5 UNBLOCK R-H74**, 14th month Acuerdo 02-95, bono educativo with
its STSS-154-2000 reglamento), the IHSS cotización matrix
and ceilings with the base-composition config flag, the RIT incapacidad
subsidy engine, the RAP fondo-de-reserva/FOVIIF stack with the D. 40-2026
regularization window, the CT jornada/surcharges/feriados family,
vacaciones, cesantía/preaviso/termination payouts, suspension/maternity
special regimes, and the salario-concepts/records chassis carrying the
85_ mislabel guard. Built from master-index clusters P1-P12 (W4 evidence,
EVID-215..333); S-HN1 retention interfaces (taxation/04), S-HN3 111
columns (fiscal-reporting/02) and S-HN2 comprobante mechanics are consumed
by id, never re-derived. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md) (validation wave — runs next).

**W10 wave (2026-08-21) fold-ins:** file 01 +LB-023 + FR-024/025 rewritten
(THE PROMEDIO FAMILY RESOLVED 5-of-6 years: 2022 L11,278.75 / 2023
L12,377.73 / 2024 L13,156.53 DGS prints + 2025 L13,985.16 SAR-43-2026
anchor — `smm_tables.csv` rows flipped printed/printed_anchor; the FY2022-
FY2025 10×SMM caps unblocked for taxation/04 FR-134; three promedio
resolution semantics separated: FY-cap / emission-time umbral /
hecho-generador-time sanctions); file 03 +LB-020 + FR-126 extended + OQ-011
new (Acuerdo 006-JD-2008 REAP domésticos — health-only separate lane,
JD-delegated rates, optional IVM bridge; segment config gate).

## Files & FR ranges

| File | Scope (clusters) | FR range | FRs | LBs | ACs | OQs |
|------|------------------|----------|-----|-----|-----|-----|
| [01_smm-chassis.md](01_smm-chassis.md) | SMM machinery (D. 103), bienio chains 2022-2027 as dated rows, maquila/zonas-libres track, retro deadlines, salvaguarda chain, **DGS promedio rows (R-H47 — THE feed of taxation/04 FR-134)** (`smm_tables.csv` sidecar); W5: Acuerdo 345 fijación-process metadata + the +15-day effectivity default (FR-041) (P1) | HN-PAYR-FR-001..041 | 41 | 23 | 16 | 14 |
| [02_13th-14th-bono.md](02_13th-14th-bono.md) | **13th month (aguinaldo) STATUTORY ENGINE per D. 112-1982 (W5 UNBLOCK, R-H74; **W6: chain ORIGINAL-pinned `110_`..`113_` — dated beneficiary rows permanents-only→+jubilados from 17-dic-1997, gazette pin PRIMARY, Art. 18 variance ruled R-H80**)**; 14th month (Acuerdo 02-95: 30-jun gate, ordinary-salary average, SMM-average variant, 30-day normalization, exit proration; **W6: D. 135-94 original `114_` — vigencia conflict OQ-012 carried**; **W7 R-H81: interp = D. 74-95 (G 27,655) re-attributed, extension = D. 54-95 (G 27,639) → FR-097 dated row, OQ-002 resolved via `119_`**); bono educativo incl. the STSS-154-2000 reglamento mechanics (W5: FR-094..096) (P2+P3+P4) | HN-PAYR-FR-051..097 | 47 | 25 | 22 | 13 |
| [03_ihss-cotizaciones.md](03_ihss-cotizaciones.md) | IHSS cotización matrix (IVM 3.5/2.5/0.5 + EM 5/2.5/0.5 ⇒ worker 5.0%/employer 8.5%), TWO regime ceilings as dated rows, min(salario, techo) base, base composition RESOLVED to text (Reglamento General 003-JD-2005 Art. 135 — OT/rest-day IN, habitual bonuses IN, occasional OUT, aguinaldo OUT per D.117-2021, 14th = flag; W9), withholding mechanics, enforcement (P5) | HN-PAYR-FR-101..137 | 37 | 20 | 15 | 11 |
| [04_ihss-incapacidad.md](04_ihss-incapacidad.md) | RIT incapacidad: NO cuarentena (days 1-3 employer salary, 4-365 IHSS 66% + complement), 35-day episode key, 182+183=365 structure, refrendo matrix, maternity 42+42 subsidy, entitlement/no-pay matrix (P6) | HN-PAYR-FR-141..170 | 30 | 15 | 18 | 5 |
| [05_rap-fondo.md](05_rap-fondo.md) | RAP-side stack: fondo 4% (techo 3×SMM-nivel-más-alto) + RAP 1.5+1.5 on IVM-excess base, three-bases-never-share rule, termination offset matrix (R-H55), grandfathering (D. 150-2008), D. 40-2026 window + FOVIIF (P7) | HN-PAYR-FR-181..215 | 35 | 15 | 18 | 9 |
| [06_jornada-surcharges.md](06_jornada-surcharges.md) | Jornada types (44 worked/48 paid), night +25%, OT ×1.25/×1.50/×1.75 + caps, séptimo día ÷6 **+ the D. 112 statutory layer (W5: FR-248 ordinary-jornada/OT-excluded/fixed-part/destajo-floor valuation + FR-249 deemed-inclusion classes/forfeiture gate/rest-day stacking)**, 11 feriados (1960-vintage dated config, R-H70) + collision rule, rest-day/holiday ×2 (P8) | HN-PAYR-FR-221..249 | 29 | 16 | 19 | 6 |
| [07_vacaciones.md](07_vacaciones.md) | Vacaciones: 10/12/15/20 días laborables scale, 200-day rule, pay-3-days-before, cash-ban + STSS exceptions, 6-month ordinary average ÷ days worked (NO 360 CT-side), ≤2-year accumulation (P9) | HN-PAYR-FR-261..280 | 20 | 12 | 12 | 2 |
| [08_cesantia-preaviso.md](08_cesantia-preaviso.md) | Preaviso 24h-2m scale + in-lieu, cesantía 10d/20d/1mo-yr + fraction, 25/15-month caps, 35%/75% variants, last-6-month base ÷ days worked, salarios caídos, pregnancy penalties, constancia, NO final-pay deadline (negative) (P10) | HN-PAYR-FR-291..325 | 35 | 14 | 22 | 7 |
| [09_suspension-maternity-special.md](09_suspension-maternity-special.md) | 15 suspension causes, CT sickness half-pay layering vs RIT, CT maternity 4+6w + 180-day base + IHSS reconciliation, minors, domésticos (cash-only base), riesgo profesional residual (P11) | HN-PAYR-FR-331..357 | 27 | 11 | 13 | 5 |
| [10_salario-concepts-records.md](10_salario-concepts-records.md) | Salario taxonomy (habitual+retributive; in-kind ≤30%), pay periods, salario completo indemnity base, mandatory deductions (union/non-union/coop), embargo caps (1959 nominals dated), Libro de Salarios/planillas, contract chassis + retroactive start, **85_ mislabel guard (EVID-333)** (P12) | HN-PAYR-FR-371..398 | 28 | 20 | 16 | 3 |
| **Total** | | HN-PAYR-FR-001..405 | **330** | **172** | **172** | **85** |

Numbering note: FR ranges pre-allocated per file (subagent dispatch
pattern); unused tails/reserved gaps (042-050, 097-100 (087 + 088-096 consumed at V-HN1/W5), 136-140, 171-180,
216-220, 250-260, 281-290, 326-330, 358-370, 399-405) stay reserved for
later additions — no renumbering. File 03 consumed its full allocation
(101..135, no tail). The `smm_tables.csv` sidecar carries the SMM value
rows (general/maquila/zonas-libres/promedio tracks × bienio vintages,
`print_status` discipline: printed / derived_gap / reconstruction_blocked —
never a derived amount in an amount cell); it carries no FRs of its own.

## Wave rulings & carries (controller notes)

- **Consumption discipline (verified):** ISR plantilla/retention engines +
  13th/14th excess-only caps + 111 record shape = HN-TAX-FR-121..153
  (taxation/04 — FR-134 consumes this wave's promedio rows, closing its
  OQ-007 ownership loop); Art. 10 exclusion semantics = HN-TAX-FR-046..078
  (taxation/02); DJIMR-111 export = HN-FREP-FR-054/055 (fiscal-reporting/02);
  chassis/due-days = HN-FREP-FR-001..032 (fiscal-reporting/01);
  comprobante-retención patronos-exempt-unless-requested =
  HN-EINV-FR-139/140 (EV24:EVID-200). Sibling payroll files cite each other
  by file + FR range.
- **Rulings applied (encoded, not re-opened):** R-H43/R-H45/R-H46/R-H47/
  R-H48 (SMM family), R-H49/R-H50/R-H51 (IHSS matrix/ceilings/base),
  R-H52/R-H53/R-H54 (incapacidad), R-H55/R-H56/R-H58 (RAP stack/offset/
  grandfathering), R-H57/R-H59/R-H60/R-H61 (mislabel guard/article map/
  CT negatives/44-48), R-H62/R-H63/R-H64 (bienio practice cadence + print
  defects), R-H65 (87_ edition citation), R-H44 (D. 135-94 = 1994).
- **Evidence-over-brief corrections (subagent findings, controller-kept):**
  (a) file 06: the feriado collision rule is TWO-holidays-on-one-day —
  fixed holidays are paid even on Sunday (brief gloss corrected to
  statute); (b) file 07: Art. 349 ¶2's proportional vacation payout is
  employer-imputable-cause-only (the any-cause cash-out applies to the
  acquired-right leg); (c) file 08: the cesantía fraction rule = Art. 120
  lit. c (brief's "Art. 115" treated as a slip; Art. 115 quoted for
  worker-side liability); (d) file 09: Art. 104 rule 4 (>5y) pays 30 days
  WITHOUT the half-salary qualifier of rules 1-3 — encoded verbatim,
  OQ-003; (e) file 02: Art. 21-A's proportionality sentence ends
  mid-print — pro-rata encoded as the evident rule.
- **Controller verbatim verification:** 5 one-word defects found and fixed
  post-dispatch (LB quotes vs evidence bank: correspondientes / se
  refieren / establecer / recibe / crédritos [sic]); residual checker
  flags adjudicated as artifacts (English translation-column spans,
  OCR-reconstruction-bracket resolutions, «» nested-quote marks, table
  reformatting, mid-quote ellipsis whole-span effects).
- **Config-gapped surfaces (never-guess flags, none silently defaulted):**
  aguinaldo mechanics (P2 — the wave's ONLY yes-blocking OQ, D. 135-94 +
  Acuerdo 201-96 unacquired), IHSS contribution-base composition (LI
  Art. 100 → Reglamento General), riesgos-profesionales rate, fondo techo
  level-set (27_ OQ-2 DECIDE), embargo L100/L200 modern equivalents
  (D. 14-1973 lead), 2022/2024 SMM amounts + 2027 table cells, promedio
  vintages ≠ 2026, Jan-May 2023 maquila, CT final-pay deadline, pre-2024
  IHSS interregnum rows, D. 40-2026 window end-convention.
- **Cross-wave dependencies:** the validation wave (COVERAGE.md +
  adversarial review, per-template Stage 5) is UNBLOCKED by this wave and
  runs next; acquisitions that would convert config gaps into FRs are the
  HANDOVER §6.2 queue (top: D. 135-94 + Acuerdo 201-96; Reglamento General
  IHSS; Ley RAP D.L. 107-2013; DGS promedio prints; STSS-006-2019).

## Open-questions summary

81 OQ rows (S-HN4 73 + W5 amendments; the former yes-blocker D. 135-94 +
Acuerdo 201-96 (aguinaldo P2) is RESOLVED-voided by R-H74/R-H75 — D. 112-1982
acquired and encoded), highest-leverage now: Reglamento General IHSS
(base composition — productive cotización computation on 13th/14th/OT
stays flagged until acquired), Ley RAP D.L. 107-2013 (doubly load-bearing,
Arts. 42/43/61 only via truncated transcription), DGS SMM/promedio prints
2022-2025 + 2027, riesgos-profesionales reglamento/JD cuadro, STSS-006-2019
(maquila base instrument), D. 54-95 (conflicting gazette cites), D. 14-1973
(embargo). Full text per file §7; register mapping to master-index C4
recorded per file.
