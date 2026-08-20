# HN — Payroll — Vacaciones: tenure scale, grant mechanics, pay base & termination cash-out (CT Arts. 345-356, 358)

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for Honduras' statutory annual
vacation (*vacaciones*, paid annual leave) under the Código del Trabajo
(D.189-59). It owns the labor-side leave machinery of cluster P9: the
tenure-based entitlement scale (10/12/15/20 días laborables — WORKING days —
at 1/2/3/4+ years of continuous service) as DATED minimum-duration
configuration; the working-day unit and continuity rules (including the
200-day irregular-work substitute); the grant mechanics — 3-month scheduling
window, 10-day advance notice, liquidation and PAYMENT 3 days before leave
starts, the cash-compensation ban with its STSS-exception flow, the
once-only ≤2-year accumulation election for hard-to-replace roles, and the
signed-constancia presumption; the pay base — average ORDINARY remuneration
of the last 6 months (or shorter tenure fraction) plus in-kind valuation,
divided by days ACTUALLY worked, with the ⅓-of-vacation-period cap on paid
unjustified-absence deductions and the mere-liberality exclusion; the
hire-date monthly-aggregate ingestion depth that feeds tenure, the 200-day
test and the base window (D-H3(a)); and the termination cash-out legs
(any-cause acquired-right payout, employer-imputable proportional payout,
unjustified-dismissal additive in-cash payout).

It does **not** own: the ISR-side vacation treatment — the >30-day
*bonificación* exemption and its 360-day daily-rate divisor are the
retention plantilla's and are consumed by id from
`../taxation/04_isr-withholding.md` **HN-TAX-FR-129** (engine family
HN-TAX-FR-121..153); the dismissal/termination-settlement composition
(preaviso, cesantía, salarios caídos, fixed-term Art. 121 indemnity) — file
08 `08_cesantia-preaviso.md` FR-291..325; jornada/working-time calendars and
the weekly-rest law — file 06 `06_jornada-surcharges.md` FR-221..250; suspension and
maternity statuses — file 09 `09_suspension-maternity-special.md` FR-331..360; the
salario/no-salario classification and in-kind valuation semantics and the
Libro de Salarios/planillas record outputs — file 10
`10_salario-concepts-records.md` FR-371..405; SMM/13th/14th-month machinery — files
01 (FR-001..040) and 02 (FR-051..090); IHSS — files 03/04; RAP/fondo —
file 05 (FR-181..215).

## 2. Legal Basis

Authority order (binding, per master evidence index): CT = `86_` (CEDIJ
consolidation print of D.189-59; vintage pinned through D.278-2013 —
fn.36 p.152, `86_ OQ-1` residual). Per **R-H59**, the vacaciones family =
**Arts. 345-356 (+358)** — never a "328-family" (the task-map drift of
`86_ OQ-4` is corrected here). Per **R-H60**, no CT article outside the
evidenced set is cited anywhere in this file. Per **R-H57**, source `85_`
(D.93-2021, G 35,760) contains ZERO Código del Trabajo provisions: its
derogated PENAL article "346" numerically collides with live CT Art. 346
(vacaciones scale) and has **no D.93-2021 effect** on any FR here
(EV85:EVID-333 guard). D-H2 (dated rows, hecho-generador resolution),
D-H3(a) (hire-date monthly-aggregate depth) and the never-guess rule bind
all FRs.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código del Trabajo, Art. 345 | "El trabajador tendrá derecho a vacaciones anuales remuneradas, cuya extensión y oportunidad se regula en el presente Capítulo. En caso de despido injustificado el patrono pagará en efectivo, a más de las indemnizaciones que la ley señale, la parte de vacaciones correspondiente al periodo trabajado." — Annual remunerated vacation right; on unjustified dismissal the employer pays IN CASH, in addition to the statutory indemnities, the vacation part corresponding to the period worked. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 345 (p.101) (EV85:EVID-314) |
| LB-002 | Código del Trabajo, Art. 346 | "El período de vacaciones remuneradas, a que tiene derecho todo trabajador después de cada año de trabajo continuo al servicio del mismo patrono, tendrá como duración mínima la que a continuación se expresa: a) Después de un (1) año de servicios continuos diez (10) días laborables, consecutivos; b) Después de dos (2) años de servicios continuos, doce (12) días laborables, consecutivos; c) Después de tres (3) años de servicios continuos, quince (15) días laborables, consecutivos; y, d) Después de cuatro (4) años de servicios continuos veinte (20) días laborables, consecutivos. No interrumpirán la continuidad del trabajo las licencias sin goce de salario, los descansos otorgados por el presente Código…las enfermedades justificadas, la prórroga o renovación del contrato de trabajo, ni ninguna otra causa análoga que no termine con este." — Minimum duration after each year of CONTINUOUS service with the same employer: 10/12/15/20 consecutive WORKING days at 1/2/3/4+ years; continuity not interrupted by unpaid licenses, Code-granted rests, justified illness, contract prórroga/renewal, or any analogous non-terminating cause. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 346 (p.101) (EV85:EVID-314) |
| LB-003 | Código del Trabajo, Art. 347 | "En las labores en que el trabajo no se efectúe con regularidad todo el año, se considerará cumplida la condición de continuidad en el servicio cuando el interesado haya trabajado durante un mínimo de doscientos (200) días en el año." — Where work is not performed regularly all year, the continuity condition is fulfilled with a minimum of 200 days worked in the year. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 347 (p.101) (EV85:EVID-314) |
| LB-004 | Código del Trabajo, Art. 348 | "La época de las vacaciones debe ser señalada por el patrono, a más tardar dentro de los tres (3) meses siguientes a la fecha en que se tiene derecho a vacaciones…El patrono dará a conocer al trabajador, con diez (10) días de anticipación, la fecha en que le concederá las vacaciones. Las sumas que deba recibir el trabajador por concepto de vacaciones, le serán liquidadas y pagadas con tres (3) días de anticipación respecto de la fecha en que comience a disfrutar de ellas. Es prohibido compensar las vacaciones con dinero, pero la Secretaría de Trabajo y Seguridad Social puede autorizar que se paguen en dinero en casos especiales de perjuicio para la economía nacional o para la industria." — Vacation season set by the employer at the latest within 3 months of entitlement; 10-day advance notice to the worker; vacation sums LIQUIDATED AND PAID 3 days before the leave starts; cash compensation prohibited, STSS may authorize money payment in special national-economy/industry-harm cases. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 348 (pp.101-102) (EV85:EVID-315) |
| LB-005 | Código del Trabajo, Art. 349 | "El trabajador que hubiere adquirido derecho a vacaciones y que antes de disfrutar de éstas cese en su trabajo por cualquier causa, recibirá el importe correspondiente en dinero. Cuando el contrato de trabajo termina antes del tiempo que da derecho a vacaciones, por causa imputable al patrono, el trabajador tendrá derecho a que se le pague la parte proporcional de la cantidad que debía habérsele pagado por vacaciones, en relación al tiempo trabajado." — Worker with acquired right who ceases before enjoying it receives the amount IN CASH whatever the cause; where the contract ends before entitlement time by a cause imputable to the employer, proportional payment in relation to time worked. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 349 (p.102) (EV85:EVID-315) |
| LB-006 | Código del Trabajo, Art. 350 | "Queda prohibido acumular vacaciones, pero podrán serle por una sola vez cuando el trabajador desempeñare labores técnicas, de dirección, de confianza u otras análogas, que dificulten especialmente su reemplazo. En los casos apuntados la acumulación será hasta de dos (2) años." — Accumulation prohibited; allowed ONCE for technical/direction/confidence or analogous hard-to-replace roles; accumulation up to 2 years. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 350 (p.102) (EV85:EVID-315) |
| LB-007 | Código del Trabajo, Art. 352 | "Para calcular el salario que el trabajador debe recibir con motivo de sus vacaciones se tomará como base el promedio de las remuneraciones ordinarias devengadas por él durante los últimos seis (6) meses, o fracción de tiempo menor cuando el contrato no haya durado ese lapso, aumentado con el equivalente de su remuneración en especie, si la hubiere. Para obtener el promedio mencionado en el párrafo anterior se dividirá la suma total de las cantidades que el trabajador hubiere recibido en concepto de salario ordinario, entre el número de días por él trabajados durante el período que sirva de base para hacer el cálculo." — Vacation pay base = average ORDINARY remuneration of the last 6 months (or shorter tenure fraction), increased by in-kind remuneration; the average = total ordinary-salary amounts ÷ number of days WORKED in the base period. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 352 (pp.102-103) (EV85:EVID-316) |
| LB-008 | Código del Trabajo, Art. 353 | "Las faltas injustificadas de asistencia al trabajo no deben descontarse del período de vacaciones, salvo que se haya pagado al trabajador. Si el salario del trabajador se ha estipulado por quincena, o por mes, no debe el patrono descontar las faltas injustificadas que haya pagado a aquél en lo que exceda de un número de días equivalente a la tercera parte del correspondiente período de vacaciones". — Unjustified absences are not deducted from the vacation period itself unless paid; for quincena/monthly salaries, paid unjustified absences are deductible only up to one third of the corresponding vacation period. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 353 (p.103) (EV85:EVID-316) |
| LB-009 | Código del Trabajo, Art. 355 | "De la concesión de vacaciones, así como de las acumulaciones…el patrono dejará constancia escrita firmada por el trabajador…si…no presenta la respectiva constancia…se presumirá que las vacaciones no han sido otorgadas." — Written record of grants and accumulations signed by the worker; without the constancia, vacations are presumed NOT granted. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 355 (p.103) (EV85:EVID-315) |
| LB-010 | Código del Trabajo, Art. 356 | "El trabajador tiene derecho a vacaciones aunque su contrato no le exija trabajar todas las horas de las jornadas ordinarias ni todos los días de la semana." — Vacation right exists even where the contract does not require working all ordinary hours or all days of the week. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 356 (p.103) (EV85:EVID-314) |
| LB-011 | Código del Trabajo, Art. 358 | "No debe contarse en la determinación de la suma que corresponde como remuneración vacacional lo recibido en concepto de gratificación o bonificación, a mero título de liberalidad." — Mere-liberality gratuities/bonuses are not counted in the vacation remuneration. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 358 (p.104) (EV85:EVID-316) |
| LB-012 | D.93-2021 (85_), Art. 1 — MISLABEL GUARD (R-H57) | "Derogar los artículos 102, 103, 104, 105, 106, 176, 182, 225, 263, 275, 309, 317, 337, 346, 368, 397, 403, 411, 417, 430, 434, 437, 444, 469, 511, 569 y 596; todos del Decreto No.130-2017…que contiene el CÓDIGO PENAL…" — the derogated "346" (and 337/368/417…) belongs to the PENAL code D.130-2017, NOT to the CT: zero CT articles are derogated by D.93-2021; CT Art. 346 (vacaciones scale) is LIVE. Guard only — no requirement of this file derives from 85_. | `hn/sources/85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf` | 93-Art. 1 (p.A.2); cross-check table (EV85:EVID-333) |

## 3. Functional Requirements

### 3.1 Entitlement scale, working-day unit, continuity and accrual depth

- **HN-PAYR-FR-261:** The system shall store the statutory vacation
  entitlement as DATED tenure-keyed configuration (D-H2): after each year of
  continuous service with the same employer (*patrono*) — 1 completed year →
  10, 2 years → 12, 3 years → 15, ≥4 years → 20 días laborables (working
  days), consecutive — as one row set with `valid_from` at the CT's
  from-publication inception (G 16,827-16,834, July 1959; Art. 875) and
  open-ended `valid_to`, additive-only, never replaced in place; the scale
  is the statutory MINIMUM duration («duración mínima») and may only be
  exceeded, never reduced (CT Art. 3 ipso-jure nullity of worker waivers).
  (LB-002; EV85:EVID-314)
- **HN-PAYR-FR-262:** The system shall define the entitlement unit as the
  día laborable: consecutive WORKING days of the worker's own schedule,
  EXCLUDING the weekly rest day and other non-working days per the
  working-time calendar owned by file 06 (`06_jornada-surcharges.md`, FR-221..250 —
  consumed by id); calendar spans shall be derived per worker calendar,
  never by a fixed calendar-day equivalence or a 30-day month assumption.
  (LB-002; EV85:EVID-314)
- **HN-PAYR-FR-263:** The system shall compute continuous service per
  employer treating as NOT interrupting continuity: licenses without pay
  (*licencias sin goce de salario*), rests granted by the CT (including
  vacations themselves and the weekly rest), justified illnesses, contract
  prórroga or renewal, and any analogous cause that does not terminate the
  contract; suspension statuses map onto this rule by id from file 09
  (`09_suspension-maternity-special.md`, FR-331..360 — no re-derivation).
  (LB-002; EV85:EVID-314)
- **HN-PAYR-FR-264:** The system shall apply the 200-day irregular-work
  substitute: where the work is not performed regularly all year, the
  continuity condition is considered fulfilled when the worker has worked
  at least 200 days in the year (counted on the FR-266 days-worked
  aggregate); below 200 days the system shall raise an entitlement
  configuration flag and shall derive NO substitute or prorated entitlement
  (never-guess: the CT prints no sub-200 rule).
  (LB-003; EV85:EVID-314)
- **HN-PAYR-FR-265:** The system shall grant the full statutory entitlement
  to workers whose contract does not require working all ordinary hours or
  all days of the week (part-day/part-week/Art. 356 workers), without
  prorating the día-laborable count below the FR-261 scale.
  (LB-010; EV85:EVID-314)
- **HN-PAYR-FR-266:** The system shall ingest MONTHLY AGGREGATES PER
  CONTRACT from the hire date — months of service, days actually worked,
  ordinary-remuneration sums, and continuity-preserving suspension flags —
  as the sole historical depth for vacaciones (D-H3(a): no payslip-level
  import); completed-years tenure (FR-261), the 200-day test (FR-264) and
  the 6-month base window (FR-273) resolve from these aggregates, with
  corrections always recomputed from ORIGINAL-period rows (D-H2: paid slips
  frozen; filed periods write-protected).
  (LB-002; LB-007; EV85:EVID-314; EV85:EVID-316)

### 3.2 Grant mechanics and timing

- **HN-PAYR-FR-267:** The system shall track the grant window: the employer
  sets the vacation season at the latest within the 3 months following the
  entitlement date (each completed-year anniversary); per grant cycle the
  system shall carry `window_due = entitlement_date + 3 months` and raise a
  compliance flag when no leave is scheduled by that date.
  (LB-004; EV85:EVID-315)
- **HN-PAYR-FR-268:** The system shall record, date-stamped, the notice of
  the vacation start date given to the worker at least 10 days in advance
  of the leave start; leave validation shall block starts lacking a notice
  dated ≥10 days earlier. (LB-004; EV85:EVID-315)
- **HN-PAYR-FR-269:** The system shall liquidate and PAY all vacation sums
  at the latest 3 days before the leave starts (hard timing rule): the
  vacation payslip's payment date shall be ≤ `leave_start − 3 days`, and a
  payslip dated later shall be blocked; the payslip's period remains the
  pre-vacation period (resolution date = the hecho generador, never
  "today"; D-H2). (LB-004; EV85:EVID-315)
- **HN-PAYR-FR-270:** The system shall prohibit compensating vacations
  with money for subsisting contracts: no cash-in-lieu payout row shall be
  generatable while the contract is active; the sole exception flow
  requires an STSS (*Secretaría de Trabajo y Seguridad Social*)
  authorization for special cases of harm to the national economy or the
  industry, recorded as a dated, referenced configuration row.
  (LB-004; EV85:EVID-315)
- **HN-PAYR-FR-271:** The system shall prohibit vacation accumulation by
  default and permit it only as a single election per worker (*por una sola
  vez*) for technical, direction, confidence or analogous roles whose
  replacement is especially difficult, with the total accumulation capped
  at 2 entitlement years; the guard shall enforce once-only, the role gate
  and the 2-year ceiling. (LB-006; EV85:EVID-315)
- **HN-PAYR-FR-272:** The system shall keep a written record of each grant
  and each accumulation, signed by the worker, and shall treat the absence
  of the constancia as raising the statutory presumption that the vacation
  was NOT granted (compliance flag on the grant record).
  (LB-009; EV85:EVID-315)

### 3.3 Pay base and CT/ISR regime separation

- **HN-PAYR-FR-273:** The system shall compute the vacation daily base =
  [Σ ordinary remuneration of the last 6 months, or the shorter tenure
  fraction when the contract has lasted less (+) the in-kind remuneration
  valuation, if any] ÷ days ACTUALLY worked in that base period — the
  divisor is days actually worked and NEVER 360 (no 360-day divisor exists
  anywhere in the CT); in-kind valuation and salario classification
  semantics are consumed by id from file 10 (`10_salario-concepts-records.md`,
  FR-371..405); the resolved daily base is snapshotted onto the
  grant/payslip record (D15 snapshot-on-write).
  (LB-007; EV85:EVID-316)
- **HN-PAYR-FR-274:** The system shall keep the CT and ISR vacation
  regimes strictly separate: the vacation >30-day *bonificación* exemption
  with its 360-day daily rate is ISR-side and is consumed by id from
  `../taxation/04_isr-withholding.md` **HN-TAX-FR-129** (engine family
  HN-TAX-FR-121..153); CT-side computations (this file) shall never apply
  the 360-day divisor, and ISR-side computations shall never apply the
  days-actually-worked divisor — no cross-leakage in either direction.
  (LB-007; EV85:EVID-316)
- **HN-PAYR-FR-275:** The system shall carry the base-width as a dated
  configuration flag with default `ordinary_only`: Art. 352's base =
  «remuneraciones ordinarias» (ordinary remuneration); whether overtime
  enters the average is textually arguable (CT Art. 361 counts OT as
  salario while Art. 358 excludes only liberalities) and is unpinned —
  practice commonly uses ordinary-only; the system shall never compute a
  derived or averaged compromise base (never-guess; OQ-002).
  (LB-007; LB-011; EV85:EVID-316; EV85:86_ OQ-6)
- **HN-PAYR-FR-276:** The system shall exclude from the vacation base all
  amounts received as mere liberality (*mera liberalidad* — occasional
  gratuities and bonuses); habitual retributive items are salario and enter
  the ordinary-remuneration sum, with the salario/no-salario classification
  consumed by id from file 10 (FR-371..405). (LB-011; EV85:EVID-316)
- **HN-PAYR-FR-277:** The system shall not deduct unjustified absences
  from the vacation period itself (absences never shorten the leave); for
  workers stipulated by quincena or month, PAID unjustified absences shall
  be deductible only up to one third (⅓) of the number of days of the
  corresponding vacation period — the cap binds the deduction routine, not
  the leave-day count. (LB-008; EV85:EVID-316)

### 3.4 Termination cash-out and interfaces

- **HN-PAYR-FR-278:** The system shall pay in cash, on ANY cessation
  cause, the amount of acquired but unenjoyed vacation (completed-year
  entitlement not yet taken, including banked accumulation under FR-271);
  and where the contract ends before the entitlement time by a cause
  imputable to the employer, the proportional part in relation to the time
  worked; and on unjustified dismissal, the in-cash proportional vacation
  is paid IN ADDITION to the statutory indemnities (Art. 345 ¶2).
  (LB-001; LB-005; EV85:EVID-314; EV85:EVID-315)
- **HN-PAYR-FR-279:** The system shall expose the vacation legs — acquired
  cash-out, employer-imputable proportional payout, unjustified-dismissal
  additive leg, and the FR-273 daily base — by id to the
  termination-settlement engine owned by file 08
  (`08_cesantia-preaviso.md`, FR-291..325), which owns the
  preaviso/cesantía/salarios-caídos composition; no dismissal-side
  mechanics are restated in this file. (LB-001; EV85:EVID-314)
- **HN-PAYR-FR-280:** The system shall emit the vacation record surfaces
  as data shapes consumed by the payroll-records layer of file 10
  (`10_salario-concepts-records.md`, FR-371..405): grant/accumulation constancias
  (FR-272), per-worker vacation balances and accrual state, and the
  pay-3-days-before payslip rows (FR-269) feeding the Libro de
  Salarios/planilla outputs. (LB-009; LB-004; EV85:EVID-315)

## 4. Data Model

Machine-readable sidecar: none allocated for this file — the 4-row
entitlement scale seeds as dated data rows (fixture/data-XML), following the
D-H2 dated-row discipline; all other structures are computed or
configuration surfaces. Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**Entitlement, continuity and ingestion depth:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.vacation.scale (new) | years_from, days_laborables, valid_from, valid_to | int/int/date | rows 1→10, 2→12, 3→15, 4→20 (4 = open-ended ≥4); `valid_from` = 1959-07-15 (first Gaceta installment of the from-publication inception, G 16,827); additive-only, never replaced (D-H2) | FR-261 |
| l10n_hn.vacation.continuity.rule (new) | code, preserves_continuity, note | char/bool | unpaid_license · ct_granted_rest · justified_illness · renewal_prorroga · analogous_non_terminating; suspension statuses joined by id from file 09 | FR-263 |
| l10n_hn.payroll.aggregate (new, shared hire-date ingestion) | contract_id, month, days_worked, ordinary_remuneration, suspension_flags | m2o/date/int/monetary/bool | D-H3(a) hire-date monthly aggregates per contract; shared surface — fondo/cesantía (files 05/08) consume their own legs; NO payslip-level import | FR-266, FR-264, FR-273 |
| hr.contract / hr.employee | hire_date, tenure counters, accumulation_used_once, accumulation_role_gate | date/int/boolean | role gate: technical · direction · confidence · analogous; ≤2 entitlement years ceiling | FR-263, FR-266, FR-271 |

**Grant workflow and pay base:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.vacation.grant (new) | entitlement_date, window_due, notice_date, leave_start, leave_end, working_days, daily_base, amount, pay_date, stss_exception_ref, constancia_signed | date/int/monetary/char/boolean | window_due = entitlement_date + 3 months; notice_date ≤ leave_start − 10 days; pay_date ≤ leave_start − 3 days (hard); daily_base snapshot-on-write (D15); constancia presumption flag | FR-267..FR-273, FR-272 |
| l10n_hn.vacation.parameter (new) | parameter, value, valid_from, valid_to | select/date | base_width: ordinary_only (default) · ot_inclusive — unpinned, OQ-002; absence_deduction_cap_ratio = 1/3 (statutory) | FR-275, FR-277 |
| hr.payslip | vac_days, vac_daily_base, vac_amount, vac_cashout_days, vac_cashout_amount | int/monetary (computed) | vacation pay line + termination cash-out rows; frozen on paid slips; corrections recompute with original-period aggregates (D-H2/D16) | FR-269, FR-273, FR-278 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living
in the LGPL client. No `saas`/`shared` rows are introduced: none of these
FRs touch the thin-client/SaaS architecture split (no DTE-like or
SaaS-channel surface exists for leave/payroll in the corpus). Model names
stable across Odoo 17/18/19/20 (hr.leave / hr.leave.type validation,
hr.payslip, hr.contract, hr.employee; l10n_hn.* are new).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-261, FR-262 | odoo | l10n_hn.vacation.scale + hr.leave allocation compute | dated rows; working-day count | D12: single statutory inception (1959, from-publication), no version regime since; D15/D16: dated rows, snapshot of the resolved row onto the grant; day counting per worker calendar consumed from file 06 |
| FR-263 | odoo | hr.contract tenure counters + l10n_hn.vacation.continuity.rule | continuity flags | Suspension statuses joined by id from file 09; counters per employer (same-patrono continuity) |
| FR-264 | odoo | l10n_hn.payroll.aggregate | 200-day test | ≥200 days → continuity fulfilled; <200 → flag, no derived substitute (never-guess) |
| FR-265 | odoo | hr.contract | part-time gate | No day-count proration below scale (Art. 356) |
| FR-266 | odoo | l10n_hn.payroll.aggregate (ingestion) | hire-date depth | D-H3(a) monthly aggregates; D18 go-live: historical import = aggregate rows only (no journals, no payslips, no straddle-FY detail needed at this depth); retro recompute with original-period rows (D16) |
| FR-267, FR-268 | odoo | hr.leave (dates) + l10n_hn.vacation.grant | window_due, notice_date | Overdue-window compliance flag; notice ≥10 days validation on leave confirmation |
| FR-269 | odoo | hr.payslip payment-date validation | pay_date ≤ start − 3d | Hard block on later-dated payment; payslip period = pre-vacation period (hecho generador, D-H2) |
| FR-270 | odoo | salary-rule guard + STSS exception config | cash-in-lieu ban | No cash-compensation rule generatable for active contracts; exception requires dated STSS authorization reference |
| FR-271 | odoo | hr.employee accumulation fields | once / role / ≤2y | Once-only per worker; role gate; 2-entitlement-year ceiling |
| FR-272 | odoo | l10n_hn.vacation.grant constancia + signature attachment | signed record | Missing constancia → not-granted presumption flag (compliance surface) |
| FR-273..FR-277 | odoo | hr.salary.rule (vacation pay) + l10n_hn.vacation.parameter | base + caps | Base = (6-month ordinary Σ + in-kind) ÷ days worked; daily-base snapshot (D15); base_width default ordinary_only (OQ-002); ⅓ deduction cap; liberality exclusion via file 10 classification; NEVER the 360 divisor (FR-274 guard) |
| FR-278, FR-279 | odoo | hr.payslip cash-out rows + settlement interface | termination legs | Acquired + proportional (employer-imputable) + unjustified-dismissal additive leg; composition engine = file 08 by id |
| FR-280 | odoo | l10n_hn.vacation.grant report surfaces | data shapes | Balances, constancias, pay-3-days-before rows → file 10 Libro/planilla outputs |

Version-regime notes (D12): the entitlement scale carries a single
statutory inception (CT 1959, from-publication effectivity per Art. 875)
with no subsequent instrument in the evidenced corpus — no adaptation
window exists; any future reform enters as a NEW dated row set, never an
in-place edit. D15/D16: resolved scale row, daily base and day counts are
snapshotted onto grant/payslip records; retro corrections recompute with
original-period aggregates; filed periods write-protected. D18: the only
go-live surface is the hire-date aggregate import (FR-266) — tiered as
balance/aggregate rows without journal entries. D19: standard payroll
posting only; no posting-tier or sequence-init surface arises from this
file.

## 6. Acceptance Criteria

- **AC-001:** Given a worker completing 4 continuous years on 2026-01-15,
  the engine selects the ≥4-years row → 20 días laborables; given a
  Monday-Saturday schedule (Sunday weekly rest) and a 10-working-day leave
  starting Mon 2026-01-05, the leave ends Thu 2026-01-15 with Sun 2026-01-11
  excluded from the count (11 calendar days ≠ 10 días laborables)
  (FR-261, FR-262).
- **AC-002:** Given a year of service containing a 2-month unpaid license
  and a 1-month justified illness, both months count toward continuous
  service and the entitlement date is unchanged (FR-263).
- **AC-003:** Given irregular-year work with 210 days worked, the
  continuity condition is fulfilled → 10 días laborables; given 190 days
  worked, no entitlement is generated, no substitute or prorated amount is
  derived, and a configuration flag is raised (FR-264).
- **AC-004:** Given entitlement on 2026-01-15, the grant must be scheduled
  ≤ 2026-04-15; given a leave starting 2026-03-10, the notice must be
  recorded ≤ 2026-02-28; a first grant scheduled 2026-05-01 raises the
  overdue-window flag (FR-267, FR-268).
- **AC-005:** Given a leave starting 2026-03-10, a vacation payslip with
  payment date 2026-03-08 is blocked and one dated 2026-03-07 passes
  (pay_date ≤ leave_start − 3 days) (FR-269).
- **AC-006:** Given Σ ordinary remuneration of the last 6 months =
  L96,000.00, in-kind valuation L6,000.00, and 144 days actually worked,
  the daily base = 102,000 ÷ 144 = L708.33 and a 10-day vacation payment =
  L7,083.33 — with the 360-day divisor absent from every CT-side
  computation (FR-273, FR-274).
- **AC-007:** Given a monthly-salaried worker with a 15-working-day
  vacation period and 8 paid unjustified-absence days in the base window,
  the deductible amount is capped at ⅓ × 15 = 5 days' worth, and the leave
  itself is not shortened (FR-277).
- **AC-008:** Given a mere-liberality Christmas gratuity of L2,000.00 and
  a habitual monthly production bonus of L1,200.00 inside the base window,
  the gratuity is excluded from the base and the habitual bonus enters the
  ordinary-remuneration sum (classification consumed from file 10)
  (FR-276).
- **AC-009:** Given an active contract, a request to pay 10 vacation days
  in cash is blocked; given a dated STSS authorization reference recorded
  on the exception flow, the payout is allowed and flagged (FR-270).
- **AC-010:** Given a technical-role worker accumulating the year-1 (10) and
  year-2 (12) entitlements into one 22-day block, the accumulation is
  allowed (once, ≤2 years); a subsequent attempt to accumulate the year-3
  entitlement is blocked (FR-271).
- **AC-011:** Given a worker with an acquired, unenjoyed 12-day entitlement
  ceasing for any cause, the cash-out = 12 × daily base; given 8 months of
  service ended by an employer-imputable cause, the proportional payout =
  10 × 8/12 = 6.67 days × daily base (year-1 scale); the indemnity
  composition resolves in file 08 (FR-278, FR-279).
- **AC-012:** Given a 2026-06-01 go-live for a worker hired 2024-03-10, the
  hire-date monthly aggregates yield 2 completed years → 12 días laborables
  at the 2026-03-10 anniversary, computed with no payslip-level import
  (FR-266, FR-261).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | CT consolidation vintage (origin `EV85:86_ OQ-1`): the 86_ print is pinned only through D.278-2013 (fn.36 p.152); any 2014-2026 reform of the vacaciones family (Arts. 345-356, 358) would be silently missing. Verify against an official current consolidation before treating the quotes as current law; reforms enter as new dated rows (D-H2). | no | Takumi S-HN4 + controller / acquisition queue | open |
| OQ-002 | Vacation base width (origin `EV85:86_ OQ-6`): Art. 352's base = «remuneraciones ordinarias» — ordinary-only (practice default, encoded in FR-275) vs OT-inclusive (Art. 361 counts OT as salario; Art. 358 excludes only liberalities). Confirm with STSS/consultor before locking the routine; the `base_width` config flag carries the election, never a derived compromise. | no | Takumi S-HN4 + controller | open |
