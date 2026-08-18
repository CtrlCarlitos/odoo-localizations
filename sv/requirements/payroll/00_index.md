# SV — Payroll (salary model / SMM / working time / benefits / social security / contracts / ISR interfaces) requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft (S4 wave, in review) |
| Authors | Takumi synthesis wave 4 + controller |
| Updated | 2026-08-18 |

This directory holds the S4 (synthesis wave 4) payroll requirements: the
Código de Trabajo (CT) salary model with the canonical earning-category
matrix, the salario mínimo (SMM) chassis with the Decreto 11-2025 dated
tariffs, the jornada/surcharges/séptimo-día/asueto engine, the vacaciones
and aguinaldo statutory benefits, the ISSS + SIP social-security
contribution engine with its dated caps, the SS declaration/remittance and
sanction cycle, the contracts/termination/indemnización/illness/maternity
layer, and the payroll↔ISR/F-14/F-910/F-11 interface contracts — with the
SMM tariffs and the SS rates/caps as verbatim dated data in two CSV
sidecars. Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_salary-model.md](01_salary-model.md) | CT Art. 119 *salario* with integrantes/exclusions, the Art. 140-143 *salario básico* as the universal derivation base (SB-R1..R7 pay-form rules, weekly-excess hourly base, complete-the-week day), equal-remuneration and privileged-credit metadata, and the CANONICAL earning-category matrix (IBC / ISR gravada / F-14 column flags) consumed wave-wide by FR id | SV-PAY-FR-001..010 | 10 | 12 | 6 | 3 |
| [02_minimum-wage.md](02_minimum-wage.md) | SMM chassis (Arts. 144-148/159: 8-hour reference, 5-8-hour full-SMM window, <5-hour proportional rule, piece-work per-jornada floor, *de pleno derecho* substitution) + the Decreto 11-2025 dated tables (four sectors three-decimal verbatim, Art. 3 caña/café piece rates with rendimiento caps, Art. 6 descanso prestación) as the `smm_2025.csv` sidecar; home-worker routing, Art. 7 benefit-base max rule, SMM-indexed anchor interfaces (2×SMM aguinaldo floor pinned; FE ≥3-SMM, 25-SMM ban and 4×SMM indemnización cap configurable — SOQ-18) | SV-PAY-FR-011..023 | 13 | 11 | 9 | 4 |
| [03_working-time-surcharges.md](03_working-time-surcharges.md) | Jornada classification Arts. 161-167 (8/44 diurna, 7/39 nocturna, mixed >4-nocturnal-hours rule, peligrosas limits), the recargo engine Arts. 168-170 (nocturnal +25%, overtime +100% of hourly básico with file-01's weekly-excess base, fuerza mayor, permanent pacts), the descanso semanal / séptimo-día engine Arts. 171-176 (complete-week accrual, presumed-included decomposition, rest-day work básico + ≥50% + compensatory day) and the asueto chapter Arts. 190-195 (static day set, 2× pay, essential services, coincidence rule) with the SOQ-19 calendar overlay consumed from fiscal-reporting/08 by FR id | SV-PAY-FR-024..043 | 20 | 22 | 10 | 5 |
| [04_statutory-benefits.md](04_statutory-benefits.md) | Vacaciones engine Arts. 177-189 (15 days + 30% surcharge, 200-worked-days gate, scheduling windows, Art. 183 base derivation, +25% lodging/food additions, termination proration, cash-compensation prohibition) + aguinaldo engine Arts. 196-203 (15/19/21-day seniority tiers, proportional payment at 12-December, 12-20 December window, no disciplinary forfeiture, termination proration, countable absences); ISR/IBC/*salario* interfaces strictly by reference | SV-PAY-FR-044..062 | 19 | 24 | 10 | 5 |
| [05_social-security-contributions.md](05_social-security-contributions.md) | ISSS side of D.L. 1263 (mandatory affiliation with reglementary exclusion threshold as dated data, 7.50%/3.00% rates, Art. 99 public-sector regime, Art. 34 base fallbacks, employer-share no-deduction invariant, worker-share cap as F-14-print dated data) + SIP side of D.L. 614 (16% cotización split 7.25/8.75, Art. 14 IBC consuming the file-01 matrix, SMM floor with sector exceptions, multi-job/subsidy/pensioner bases, independent workers, AFP routing, pensioner config per R23) — rates and caps in the `ss_contributions.csv` sidecar (SOQ-11: payroll owns the values; the F-14 side mirrors them) | SV-PAY-FR-063..085 | 23 | 12 | 12 | 8 |
| [06_ss-declaration-remittance.md](06_ss-declaration-remittance.md) | Monthly declare-and-pay within the first ten días hábiles on the shared engine (09_ Art. 21), the electronic planilla única pointer (one flow carrying the AFP previsional + ISSS obrero-patronal declarations), the sanction architecture as distinct regimes (ISSS 1%/month recargo; SIP 5%/10%/15% multa ladders, US$600→1,200 escalation, 20%+2%/month vs 10%+5%/month tracks), the omisión/inconsistencia cure workflow (Art. 22 windows), the 48-hour work-accident report, and the employer record duties | SV-PAY-FR-086..100 | 15 | 13 | 15 | 7 |
| [07_contracts-termination.md](07_contracts-termination.md) | Contract taxonomy Arts. 25-28 (indefinite presumption, obra 7-day notice, interinos, 30-day trial) routing termination outcomes; unjustified-dismissal indemnización Arts. 58-59 (30 days' básico per year, 15-day minimum, 4×SMM countable-salary cap arithmetic — resolving 02 FR-023's forward reference); constancia Art. 60 and despacho de hecho Art. 55; employer illness subsidies Arts. 307-308-B (75% with 60/40/20 tier caps); maternity engine Arts. 309-312 (16 weeks at 75%, void Art. 311 gate per sent. 105-2014, lactancia breaks); sepelio Art. 313; settlement wiring for 04's prorations | SV-PAY-FR-101..120 | 20 | 21 | 16 | 5 |
| [08_isr-interfaces.md](08_isr-interfaces.md) | Payroll↔ISR/reporting interfaces (pointer and value-feed contracts only): the retention-base input contract behind SV-TAX-FR-104 (cotizaciones + remuneraciones no gravadas netting per D.E. 10-2025 Art. 1 d), the Ley ISR Art. 4 cross-check resolving 01's crosscheck_oq cells, the F-14 per-employee value-feed contract (SOQ-11), the F-910 annual feed, the F-11 v18 personal-deduction value feeds (65_ casillas 711-725/734), the SIP Art. 138 voluntary pension-savings regime, and the BLOCKED Quincena-25 pointer (SOQ-09 kin — D.L. 499 not in corpus) | SV-PAY-FR-121..137 | 17 | 11 | 16 | 4 |
| **Total** | | SV-PAY-FR-001..137 | **137** | **126** | **94** | **41** |

Numbering note: FR numbering is wave-sequential within the `SV-PAY`
prefix (001-137, no gaps, no renumbering). The two CSVs are dated-data
sidecars — `smm_2025.csv` (18 rows; the Decreto 11-2025 tariffs of
`02_minimum-wage.md`) and `ss_contributions.csv` (14 rows; the ISSS/SIP
rates and caps of `05_social-security-contributions.md`); they carry no
FRs of their own.

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. 41 OQs total —
39 open / 2 resolved per the per-file status columns. Resolution
note (S4 final review, 2026-08-18): `08` §3.2 (FR-123..125) closed
`01`'s OQ-002/OQ-003 crosscheck family — occasional gratuities
confirmed gravada, indemnización split per Ley ISR Art. 4.3, sepelio
no_gravada, illness/maternity subsidies gravada — recorded as
definitive stamps in 08 and now mirrored in 01 (§4 matrix resolution
note; OQ-002/OQ-003 flipped resolved below).

Master-index SOQ mapping: SOQ-15 = `05` OQ-001 (kin: `05` OQ-005/OQ-007,
`06` OQ-002); SOQ-16 = `05` OQ-002; SOQ-17 = `05` OQ-003 (kin: `06`
OQ-001); SOQ-18 = `02` OQ-002 (+ kin: `07` OQ-002 4×SMM cap sector, `05`
OQ-004 SMM-floor sector association); SOQ-19 = `03` OQ-001; SOQ-20 =
`02` OQ-003 (CSV three-decimal fidelity note); SOQ-21 = `01` OQ-001 and
the CT-vintage LB notes of every 11_-citing file; SOQ-05 kin = `04`
OQ-005 (2025+ standing 2-SMM aguinaldo rule re-verified at encoding);
SOQ-09 kin = `08` OQ-002 (Quincena-25 law absent — blocks the payroll
income-treatment family).

### 01_salary-model.md (3)

- OQ-001 — SOQ-21 carried: CT copy vintage (Índice Legislativo edition, reform stamps (1)-(22), no as-of date); cited articles cross-check consistent — re-verify if a later CT reform lands. open
- OQ-002 — Occasional gratuities ISR treatment: no corpus exclusion from remuneraciones gravadas; matrix marks gravada — confirmed gravada by `08` §3.2 FR-125. resolved (2026-08-18)
- OQ-003 — ISR gravada classification of the non-vacation/aguinaldo prestaciones (indemnización, illness/maternity subsidies, sepelio) via the Ley ISR Art. 4 cross-check — the crosscheck_oq cells (resolved by `08` §3.2 FR-123..125: split / no_gravada / gravada). resolved (2026-08-18)

### 02_minimum-wage.md (4)

- OQ-001 — Prior SMM vintages absent: the repealed 2021 pair (D.E. 9/10-2021) is not in the corpus; pre-2025-06-01 lookups flag, never invent. open
- OQ-002 — SOQ-18 carried: which sector's SMM feeds each UNPINNED SMM-indexed rule (FE receptor ≥3 SMM, 25-SMM cash ban, 4×SMM indemnización cap); configurable selection + MH guidance hunt. open
- OQ-003 — SOQ-20 carried: the three-decimal tariff prints transcribed exact-as-printed with [sic] flags; optional gazette re-verification. open
- OQ-004 — Tarea metric quantification (ton ↔ tarea equivalence) for the Art. 3 rendimiento caps. open

### 03_working-time-surcharges.md (5)

- OQ-001 — SOQ-19 carried: asueto overlay extras (2-Jan, Día del Padre, 5-6-Aug pattern, fin de año) are absent decree instruments; overlay-only days default to no CT pay obligation; exact-date pinning rides fiscal-reporting/08 OQ-003. open
- OQ-002 — Local-festivity day ("la festividad más importante del lugar") left as per-locality configuration. open
- OQ-003 — Art. 193 stay-open sector catalog ships empty pending transcription from the article. open
- OQ-004 — Hourly-básico divisor for sub-8h jornadas (÷8 precedent vs own jornada hours) — needs a file-01-side ruling. open
- OQ-005 — Séptimo día of an employment-incomplete week (termination tail week / mid-week hire): corpus silent; FR-032 ships zero accrual as a disclosed working assumption, proportional proration the live alternative. open

### 04_statutory-benefits.md (5)

- OQ-001 — Vacation day-count convention: 15 días laborables (working assumption) vs calendario. open
- OQ-002 — 200-day gate counting of justifiable absences (Art. 203 is expressly aguinaldo-only). open
- OQ-003 — Aguinaldo tier measurement date (payment-date default vs 12-December). open
- OQ-004 — Aguinaldo proportional denominator (365-day default). open
- OQ-005 — SOQ-05 carried: no 2025/2026 aguinaldo transitory after D.L. 159-2024 → standing 2-SMM rule for 2025+; re-verify at encoding time. open

### 05_social-security-contributions.md (8)

- OQ-001 — SOQ-15 carried: ISSS Reglamento de Aplicación absent (Art. 3 exclusion threshold, cotizable-base cap behind the $30.00 print, Art. 34 variable-base tables, remittance mechanics). open
- OQ-002 — SOQ-16 carried: SIP IBC-ceiling instrument absent; the AFP $472.93 print stands as dated data, no implied ceiling derived. open
- OQ-003 — SOQ-17 carried: D.L. 614 Reglamento + BCR Normas Técnicas + institutos' rate laws absent (planilla-única spec, acreditación windows, INPEP/IPSFA splits). open
- OQ-004 — SMM floor exceptions (aprendices, agrícolas, domésticos): sector association needs the Normativa Técnica. open
- OQ-005 — ISSS remuneración afecta vs SIP IBC divergence: file-01 matrix flags as proxy; fork to the Reglamento's list on acquisition. open
- OQ-006 — Art. 14 final provisions truncated in the evidence extract (pensioner riesgos-profesionales base) — source re-read. open
- OQ-007 — ISSS cap applicability to the employer share (SOQ-15 kin). open
- OQ-008 — Riesgos profesionales rate fold (no separate employer accident rate; watch during Reglamento acquisition). open

### 06_ss-declaration-remittance.md (7)

- OQ-001 — Planilla única spec absent (Art. 27 verbatim truncation; Reglamento/Normas unacquired). open
- OQ-002 — ISSS-side statutory window deferred to the absent Reglamento; unified first-10-hábiles reading operative. open
- OQ-003 — Sanction-procedure details needing a source re-read (ladder day-types, US$1,200 escalation, Art. 22 window composition, Art. 146 mechanics). open
- OQ-004 — Art. 145 non-computed legs (lost-rentabilidad formula; employer-side cotización mechanics). open
- OQ-005 — Art. 33 colon-era fine print ("cien a quinientos colones") never converted/indexed. open
- OQ-006 — Institute accident-report form templates absent (48-hour clock ships without layout). open
- OQ-007 — Retention period for the 16_ Art. 11 records unpinned. open

### 07_contracts-termination.md (5)

- OQ-001 — Indemnización fraction denominator (365-day default; kin of 04 OQ-004). open
- OQ-002 — 4×SMM cap sector (SOQ-18 kin, rides 02 OQ-002): comercio_y_servicios default documented, alternatives pending guidance. open
- OQ-003 — Lactancia breaks child-age span unstated (required config, no invented default). open
- OQ-004 — Prenatal supplementary rest delegated to an absent reglamento. open
- OQ-005 — Illness-tier window cadence (anniversary default) and netting across promotion boundaries. open

### 08_isr-interfaces.md (4)

- OQ-001 — F-14 S/T/U/V stamped values for salaried rows label-inferred only (config + documented default set). open
- OQ-002 — SOQ-09 kin: Ley Especial Quincena Veinticinco (D.L. 499) not in corpus — BLOCKS payroll income-treatment FRs; acquisition queued as source 66. open (blocking: Quincena-25 features only)
- OQ-003 — Non-affiliated voluntary-savings cap input = worker's own prior-year declared renta (worker-supplied provenance to confirm). open
- OQ-004 — F-11 v18 currency watch (footer stamp 27-02-2025; a v19 would renumber casillas 711-725/734 — feed keys re-verify). open
