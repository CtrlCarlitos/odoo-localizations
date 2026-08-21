# SV — Payroll — Working time & surcharges: jornada, recargos, descanso semanal (séptimo día) and asuetos

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador working-time model every time-based
payroll computation runs on: the Código de Trabajo (Labor Code, CT)
*jornada* (workday/workweek) classification of Arts. 161-167 — diurna
8/44, nocturna 7/39, the more-than-four-nocturnal-hours mixed-jornada
rule, the dangerous/unhealthy 7/39-6/36 limits with the MTP-authorization
exception, the *trabajo efectivo* (effective work time) definition and
the ≥8-hour inter-jornada rest; the surcharge engine of Arts. 168-170 —
nocturnal work +25% (floor), overtime +100% of the hourly *salario
básico* with the weekly-excess base consumed from file 01 by FR id, the
*fuerza mayor* (force majeure) plain-básico exception and the
Director-approved permanent-extra-hour pacts; the *descanso semanal*
(weekly rest) engine of Arts. 171-176 — *séptimo día* (seventh day)
accrual per complete week with the just-cause/unjustified-loss rules,
the no-horario six-day rule, the Sunday default and assignment
exceptions, the presumed-included DECOMPOSITION invariant for
period salaries (never double-pay), and rest-day work = básico +
≥50% floor + compensatory day counted as effective work; and the
*asueto* (public holiday) chapter of Arts. 190-195 — the static legal
day set (with the San Salvador 3&5-August and local-festivity rows),
pay at básico presumed included, asueto-worked 2× pay with the
extraordinary-hours base, essential-services stay-open sectors, the
coincidence-with-descanso no-double-pay rule and the a domicilio /
commission / destajo exclusions — plus the SOQ-19 dual-layer calendar:
CT Art. 190 static base UNION a decree-driven dated overlay consumed
from `fiscal-reporting/08_filing-calendar.md` by FR id.

It does **not** cover: the *salario* / *salario básico* model and the
canonical earning-category matrix (`01_salary-model.md` — the derivation
rules, the Art. 142 final-inciso weekly-excess hourly base FR-007 and
the matrix row classification are consumed by FR id, never restated);
the SMM chassis, dated tariff tables and the Art. 6 piece-rate
descanso prestación VALUES (`02_minimum-wage.md` — consumed by FR id);
the vacaciones and aguinaldo engines (`04_statutory-benefits.md`);
social-security rates, caps and IBC
(`05_social-security-contributions.md`, `06_ss-declaration-remittance.md`);
contracts, termination, indemnización and illness/maternity subsidies
(`07_contracts-termination.md`); ISR/F-14 interfaces
(`08_isr-interfaces.md`); or the filing-calendar obligation inventory,
asueto TABLE and días-hábiles engine
(`fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202/203 — this file
consumes that engine and owns only the payroll-side asueto pay rules).

## 2. Legal Basis

Authority order (binding, per master evidence index S4): labor = 11_
(Código de Trabajo, D.L. 15-1972, Índice Legislativo edition, reform
stamps (1)-(22) — SOQ-21/OQ watch); the piece-rate descanso prestación
values = 16_ (Decreto 11-2025) consumed from `02_minimum-wage.md` by FR
id; the dated asueto overlay = 30_ (Calendario Tributario 2026)
consumed from `fiscal-reporting/08_filing-calendar.md` by FR id; the
salary/básico bases and the category matrix are consumed from
`01_salary-model.md` by FR id.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Trabajo, Art. 161: diurno = 06:00-19:00, nocturno = 19:00-06:00; "jornada ordinaria de trabajo efectivo diurno ... no excederá de ocho horas diarias, ni la nocturna de siete. La jornada ... más de cuatro horas nocturnas, será considerada nocturna para el efecto de su duración. La semana laboral diurna no excederá de cuarenta y cuatro horas ni la nocturna de treinta y nueve." | Ordinary effective diurnal jornada must not exceed 8 hours/day, nor the nocturnal 7; a jornada containing more than four nocturnal hours is considered nocturnal for the purpose of its duration; the diurnal working week must not exceed 44 hours nor the nocturnal 39; diurnal window 06:00-19:00, nocturnal 19:00-06:00 | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 161, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-002 | Código de Trabajo, Art. 162: dangerous/unhealthy tasks — jornada limits of 7 hours/39 week diurnal, 6 hours/36 nocturnal; the Ministerio de Trabajo y Previsión Social may authorize exceptions | For tasks proving dangerous to health or life: 7h/day 39h/week diurnal and 6h/day 36h/week nocturnal limits, with an MTP authorization exception | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 162, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-003 | Código de Trabajo, Art. 163: *trabajo efectivo* definition — includes the rest/eating pauses within the jornada | Effective-work-time definition: the jornada counts as effective time including inner rest and meal pauses | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 163, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-004 | Código de Trabajo, Art. 167: at least 8 hours of rest between the end of one jornada and the start of the next | Minimum 8-hour inter-jornada rest interval | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 167, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-005 | Código de Trabajo, Art. 168: "Las labores que se ejecuten en horas nocturnas se pagarán, por lo menos, con un veinticinco por ciento de recargo sobre el salario establecido para igual trabajo en horas diurnas." | Work executed in nocturnal hours is paid, at least ("por lo menos" — floor), with a 25% surcharge over the rate established for equal work in diurnal hours | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 168 p.39, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-006 | Código de Trabajo, Art. 169: "Todo trabajo verificado en exceso de la jornada ordinaria, será remunerado con un recargo consistente en el ciento por ciento del salario básico por hora, hasta el límite legal." (fuerza mayor → plain salario básico) | All work in excess of the ordinary jornada is remunerated with a 100% recargo of the hourly salario básico, up to the legal limit; under fuerza mayor (force majeure) the excess hours pay plain salario básico | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 169, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-007 | Código de Trabajo, Art. 170: overtime is occasional; permanent one-extra-hour pacts only for (a) enterprises whose labor cannot be interrupted for 24 hours, or (b) recovering the 6th day's four hours (granting Saturday+Sunday consecutive rest), with Director General de Trabajo approval | Extraordinary work is occasional by rule; permanent extraordinary-hours schemes require an approved pact under the two Art. 170 cases (24-hour enterprises; 6th-day recovery) with Director General de Trabajo approval | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 170, Arts. 161-170 pp.38-40 (EVID-202) |
| LB-008 | Código de Trabajo, Art. 171: "Todo trabajador tiene derecho a un día de descanso remunerado por cada semana laboral. El trabajador que no complete su semana laboral sin causa justificada de su parte, no tendrá derecho a la remuneración establecida..." | Every worker is entitled to one remunerated rest day per worked week; a worker who does not complete the working week without just cause on their part loses that remuneration | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 171, Arts. 171-176 p.40 (EVID-203) |
| LB-009 | Código de Trabajo, Art. 172: no-horario workers are entitled when they "hubieren laborado seis días de la semana y trabajado la jornada ordinaria en cada uno de ellos"; just-cause absence preserves the right | Workers not subject to work schedules earn the rest-day remuneration when they worked six days of the week with the ordinary jornada in each; a just-cause absence preserves the entitlement | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 172, Arts. 171-176 p.40 (EVID-203) |
| LB-010 | Código de Trabajo, Art. 173: the rest day is Sunday, except for continuous-labor / public-service / normally-Sunday enterprises (which may assign another day); otherwise a Director authorization is needed | Default weekly rest day = Sunday; enterprises of continuous labor, public services or those that normally work Sundays may assign a different day; other employers need authorization to do so | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 173, Arts. 171-176 p.40 (EVID-203) |
| LB-011 | Código de Trabajo, Art. 174: "derecho a gozar de una prestación equivalente al salario básico en su correspondiente día de descanso. Si el salario se estipulare por semana, quincena, mes u otro período mayor, se presume que en su monto va incluida la prestación pecuniaria del día de descanso semanal." | Right to a prestación equal to the salario básico on the corresponding rest day; when salary is stipulated by week, quincena, month or longer period, the weekly-rest money prestación is PRESUMED included in its amount | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 174, Arts. 171-176 p.40 (EVID-203) |
| LB-012 | Código de Trabajo, Art. 175: rest-day work by mutual agreement: "salario básico correspondiente a ese día, más una remuneración del cincuenta por ciento como mínimo, por las horas que trabajen y a un día de descanso compensatorio remunerado"; overtime that day computes on the extraordinary salary | Work on the rest day pays the básico of that day plus an additional remuneration of fifty percent AS A MINIMUM (floor) for the hours worked, plus one remunerated compensatory rest day; overtime worked that day computes on the extraordinary salary | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 175, Arts. 171-176 p.40 (EVID-203) |
| LB-013 | Código de Trabajo, Art. 176: the compensatory day is remunerated at salario básico, taken the same or the following week, and counts as effective work time | Compensatory rest day = salario básico, same or next week, counted as effective work | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 176, Arts. 171-176 p.40 (EVID-203) |
| LB-014 | Código de Trabajo, Art. 190: remunerated asuetos: "a) Primero de enero; b) Jueves, viernes y sábado de la Semana Santa; c) Primero de mayo; ch) SEIS DE AGOSTO;(9) d) Quince de septiembre; e) Dos de noviembre; y f) Veinticinco de diciembre. ADEMAS SE ESTABLECEN EL TRES Y CINCO DE AGOSTO EN LA CIUDAD DE SAN SALVADOR; Y EN EL RESTO DE LA REPUBLICA, EL DIA PRINCIPAL DE LA FESTIVIDAD MAS IMPORTANTE DEL LUGAR, SEGUN LA COSTUMBRE.(9)" | The static legal holiday set: 1 January; Holy-Week Thursday, Friday and Saturday; 1 May; 6 August (stamp (9)); 15 September; 2 November; 25 December; PLUS 3 and 5 August in the city of San Salvador, and in the rest of the Republic the principal day of the locality's most important festivity per custom (stamp (9)) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 190, Arts. 190-195 pp.42-43 (EVID-205; 11_ OQ-1) |
| LB-015 | Código de Trabajo, Art. 191: asuetos are remunerated "con salario básico, calculado de acuerdo con las reglas establecidas en la letra A) del Art. 142"; period salaries are presumed to include the asueto prestación | Asueto pay = salario básico computed under the Art. 142-A derivation rules (owned by `01_salary-model.md` SV-PAY-FR-006); period salaries presumptively include it | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 191, Arts. 190-195 pp.42-43 (EVID-205) |
| LB-016 | Código de Trabajo, Art. 192: asueto work pays "un salario extraordinario integrado por el salario ordinario más un recargo del ciento por ciento de éste. SI TRABAJAN EN HORAS EXTRAORDINARIAS, EL CALCULO ... SE HARA EN BASE AL SALARIO EXTRAORDINARIO ESTABLECIDO EN EL INCISO ANTERIOR.(1)" | Working on an asueto pays an extraordinary salary = ordinary salary plus a 100% recargo of it (2×); when extraordinary hours are worked [that day], the computation is made ON the extraordinary salary established in the prior paragraph (stamp (1)) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 192, Arts. 190-195 pp.42-43 (EVID-205) |
| LB-017 | Código de Trabajo, Art. 193: public essential services may remain open on asuetos (enumerated sectors) | The stay-open exception catalog for public essential services on holiday days | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 193, Arts. 190-195 pp.42-43 (EVID-205) |
| LB-018 | Código de Trabajo, Art. 194: an asueto coinciding with the descanso semanal pays only the salario básico; if the worker works that day → Art. 192 pay plus a remunerated compensatory rest | Coincidence rule: a holiday falling on the weekly-rest day pays a single salario básico (no duplication); working the coincident day pays the Art. 192 extraordinary salary plus a remunerated compensatory rest day | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 194, Arts. 190-195 pp.42-43 (EVID-205) |
| LB-019 | Código de Trabajo, Art. 195: excluded from this chapter [asueto]: *a domicilio* (home) workers and commission / *destajo* (piecework) / *ajuste por obra* (work-adjustment) workers | The asueto chapter does not apply to home workers or commission/piecework/work-adjustment workers | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 195, Arts. 190-195 pp.42-43 (EVID-205) |
| LB-020 | Código de Trabajo, Arts. 90-93: general descanso provisions (Art. 90, whose inciso 3º is the computation anchor the SMM decree cites); agropecuario paid-rest special (Art. 93) | The general weekly-rest chapter behind Arts. 171-176 — incl. Art. 90 inciso 3º, the anchor cited by Decreto 11-2025 Art. 6 for piece-rate workers, and the agropecuario special | `sv/sources/11_Codigo_Trabajo.pdf` | Arts. 90-93 p.25 (EVID-203) |
| LB-021 | Decreto 11-2025, Art. 5: "Para las personas trabajadoras contratadas por unidad de tiempo, su día de descanso será remunerado con una cantidad equivalente al salario ordinario de un día." | Time-unit workers' weekly-rest day is remunerated with an amount equal to one day's ordinary salary | `sv/sources/16_Salarios_Minimos_2025.pdf` | p.20 Art. 5 (EVID-192) |
| LB-022 | Calendario Tributario 2026, p.1 leyenda "Días de asueto": "Año Nuevo (1 y 2 Enero) / Semana Santa / Día del Trabajo / Día del Padre / Fiestas Patronales del Salvador del Mundo / Día de la Independencia / Día de los Difuntos / Fiestas Navideñas y Fin de Año" — interface anchor only; the dated asueto TABLE and the días-hábiles engine are OWNED by `fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202/203 and consumed by reference | The 2026 calendar's holiday legend — the decree-driven overlay source (2-January, Father's Day, the San-Salvador-del-Mundo patronales pattern, Christmas/year-end) whose dated rows this file consumes by FR id, never restating values | `sv/sources/30_Calendario_Tributario_2026.pdf` | p.1 legend + month grids (EVID-186; via fiscal-reporting/08 LB-003) |

Version regime (D12): the ONLY dated data in scope is the asueto overlay,
and it is owned by `fiscal-reporting/08_filing-calendar.md`
(SV-FREP-FR-202: year-keyed rows re-seeded annually from the published
calendar; exact-date pinning open there as OQ-003); the CT Art. 190 set
is STATIC law, and the CT text basis is the Índice Legislativo edition
(stamps through (22), no as-of date — SOQ-21 watch, kin of file 01's
OQ-001). No SMM values live in this file — `02_minimum-wage.md`'s
`smm_2025.csv` owns every dated tariff (incl. the Art. 6 prestación rows
consumed here by FR id).

## 3. Functional Requirements

### 3.1 Jornada model (CT Arts. 161-167)

- **SV-PAY-FR-024:** The system shall classify every worker's
  *jornada* as (a) *diurna* — work executed 06:00-19:00, ordinary
  limits 8 hours/day and 44 hours/*semana laboral* (working week), or
  (b) *nocturna* — work executed 19:00-06:00, ordinary limits 7
  hours/day and 39 hours/week, or (c) *mixta* (mixed) — classified
  NOCTURNAL for duration purposes when more than four of its hours
  fall in the nocturnal window (diurnal limits otherwise); the
  classification selects the limit set every downstream hour bucket
  (ordinary / daily-excess / weekly-excess) is measured against.
  (LB-001; EVID-202)
- **SV-PAY-FR-025:** The system shall apply the dangerous/unhealthy
  jornada limits — 7 hours/day, 39 hours/week diurnal; 6 hours/day, 36
  hours/week nocturnal — to tasks designated as dangerous to health or
  life, and shall record the Ministerio de Trabajo y Previsión Social
  (MTP) authorization exception as configuration (authorization
  reference, scope, validity window) that relaxes the designation's
  limits while valid. (LB-002; EVID-202)
- **SV-PAY-FR-026:** The system shall compute every jornada-limit and
  surcharge hour bucket on *trabajo efectivo* (effective work time —
  time at the employer's disposal INCLUDING the rest/eating pauses
  inside the jornada), per the Art. 163 definition; no pause inside
  the jornada reduces effective time. (LB-003; EVID-202)
- **SV-PAY-FR-027:** The system shall validate that consecutive
  jornadas of the same worker are separated by at least 8 hours of
  rest (inter-jornada rest), flagging schedule or attendance patterns
  that violate the interval as compliance findings on the timesheet
  feed — the flag gates recargo-context review, not a payslip amount
  of its own. (LB-004; EVID-202)

### 3.2 Surcharges (CT Arts. 168-170)

- **SV-PAY-FR-028:** The system shall remunerate hours worked within
  the nocturnal window with a surcharge of AT LEAST 25% over the rate
  established for equal work in diurnal hours — "por lo menos" makes
  25% a FLOOR (configurable upward, never below) — computed on the
  stored hourly *salario básico* of `01_salary-model.md` SV-PAY-FR-005
  (never re-derived here); the surcharge line classifies per the
  canonical matrix of SV-PAY-FR-004. (LB-005; EVID-202)
- **SV-PAY-FR-029:** The system shall remunerate every hour worked in
  excess of the ordinary jornada with a recargo of 100% of the hourly
  *salario básico* — i.e. each excess hour pays 2× the stored hourly
  base of SV-PAY-FR-005 — applying the SAME hourly base to hours
  worked in excess of the *semana laboral* (weekly-excess hours) per
  the Art. 142 final-*inciso* rule OWNED by `01_salary-model.md`
  SV-PAY-FR-007 (consumed by id). The Art. 169 recargo applies
  "hasta el límite legal" under TWO distinct resolutions: (a) the
  CAP resolution — the excess-hour recargo resolves to the
  jornada/semana caps of FR-024/FR-025; and (b) the PROVENANCE
  resolution — the pre-reform cap reference itself (Art. 168 of the
  pre-reform numbering) lands on the weekly-excess rule (EVID-202
  gloss). Overtime lines classify as *trabajo extraordinario* per
  SV-PAY-FR-004 (overtime_pay class). (LB-006; LB-001; EVID-202)
- **SV-PAY-FR-030:** The system shall remunerate excess-day/
  excess-week hours worked under *fuerza mayor* (force majeure) at
  PLAIN *salario básico* — no Art. 169 recargo — gated on a recorded
  fuerza-mayor condition flag (event reference and scope) on the
  affected attendance rows; unflagged extraordinary hours never take
  the plain rate. (LB-006; EVID-202)
- **SV-PAY-FR-031:** The system shall treat extraordinary work as
  OCCASIONAL by default and admit permanent extraordinary-hours
  schemes only as recorded pacts under Art. 170 — (a) enterprises
  whose operations cannot be interrupted for 24 hours, or (b) the
  recovery of the 6th day's four hours granting Saturday+Sunday
  consecutive rest — each carrying Director General de Trabajo
  approval reference and effective window; hours scheduled under a
  valid pact remain extraordinary for remuneration purposes
  (FR-029/FR-030 govern; the corpus states no separate rate for pact
  hours), and permanent extra hours without a valid pact raise a
  compliance flag. (LB-007; EVID-202)

### 3.3 Descanso semanal / séptimo día (CT Arts. 171-176)

- **SV-PAY-FR-032:** The system shall accrue the *séptimo día* — one
  day of remunerated weekly rest per COMPLETE *semana laboral* — as a
  prestación equal to the stored daily *salario básico*
  (`01_salary-model.md` SV-PAY-FR-005; the Art. 174 base), or for
  SMM-level workers the 16_ Art. 7 max-rule base of
  `02_minimum-wage.md` SV-PAY-FR-021 (max of actual daily salary and
  sector daily SMM — consumed by id); a worker who does NOT complete
  the working week WITHOUT just cause loses the prestación, while
  just-cause absences preserve it (per-complete-week accrual: the right
  attaches to complete semanas laborales — a week not completed within
  the employment, e.g. a mid-week hire's or a termination's tail week,
  is treated as not a complete semana laboral and accruing nothing —
  a disclosed working assumption, the corpus being silent on the tail
  week (OQ-005); justification governs absences inside an employment
  week, not the employment window itself). (LB-008; LB-011; EVID-203)
- **SV-PAY-FR-033:** The system shall accrue the rest-day prestación
  for workers NOT subject to work schedules (incl. the Decreto
  11-2025 Art. 3 collection rubros, "no sujetos a horarios de
  trabajo") on the SIX-day rule: entitled when the worker labored six
  days of the week working the ordinary jornada in each, a just-cause
  absence preserving the entitlement; the piece-rate collection VALUES
  (caña per tarea/tonelada, café per arroba) are the Art. 6 table of
  `02_minimum-wage.md` SV-PAY-FR-019 — consumed by FR id, never
  restated here. (LB-009; LB-021; EVID-203; EVID-192)
- **SV-PAY-FR-034:** The system shall schedule the weekly rest day on
  SUNDAY by default, permitting a different fixed day only for (a)
  continuous-labor enterprises, (b) public services and (c)
  enterprises that normally work Sundays — or under a recorded
  Director authorization otherwise — with the assignment basis stored
  on the work calendar driving the séptimo/coincidence computations of
  this file. (LB-010; EVID-203)
- **SV-PAY-FR-035:** The system shall implement the
  presumed-included DECOMPOSITION invariant: salaries stipulated by
  week, *quincena* (fortnight), month or longer period are PRESUMED
  to include the weekly-rest prestación (Art. 174) and the asueto
  prestación (Art. 191 — FR-039), so payroll shall DECOMPOSE each
  period salary into *días laborados* (worked days) + *séptimos* +
  *asuetos* for proration (mid-week hires, terminations, partial
  absences), termination feeds and reporting — the decomposition of a
  full worked period reproduces the period total exactly, and the
  system shall NEVER pay a separate séptimo/asueto line on top of a
  period salary that already presumes it (no double pay); decomposed
  séptimo/asueto components classify as ordinary pay per the canonical
  matrix of `01_salary-model.md` SV-PAY-FR-004 (Art. 174 decomposition
  row), not as a separate prestación class. (LB-011; LB-015;
  EVID-203; EVID-205)
- **SV-PAY-FR-036:** The system shall remunerate work performed on
  the assigned rest day (by mutual agreement) with (a) the *salario
  básico* of that day PLUS (b) an additional remuneration of AT LEAST
  50% for the hours worked — "como mínimo" makes the 50% a FLOOR
  (configurable upward) — plus (c) one remunerated compensatory rest
  day taken the same or the following week, counted as effective work
  time (Art. 176) and tracked on a per-worker compensatory-days
  counter; overtime worked on the rest day computes on the
  extraordinary salary (the básico-plus-50% rate is the base the
  further recargo applies to). (LB-012; LB-013; EVID-203)

### 3.4 Asuetos (CT Arts. 190-195) and the dual-layer calendar (SOQ-19)

- **SV-PAY-FR-037:** The system shall store the STATIC legal asueto
  base set of CT Art. 190 as undated law: 1 January; Holy-Week
  Thursday, Friday and Saturday; 1 May; 6 August; 15 September; 2
  November; 25 December; PLUS 3 August and 5 August for the city of
  San Salvador (geographic scope: that city); PLUS, for the rest of
  the Republic, the principal day of the locality's most important
  festivity *según la costumbre* (per custom — a municipality-level
  configuration, OQ-002); day-of-week-mobile entries (Semana Santa,
  local festivities) resolve to concrete dates per year. (LB-014;
  EVID-205)
- **SV-PAY-FR-038:** The system shall compute the operative payroll
  asueto-day set as the UNION of two provenance layers: (a) the CT
  Art. 190 static base (FR-037) and (b) the decree-driven DATED
  overlay — the asueto table OWNED by
  `fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202 (2026
  legend: Año Nuevo 1-2 January, Día del Padre, Fiestas Patronales del
  Salvador del Mundo, Fiestas Navideñas y Fin de Año, etc.), consumed
  by FR id with the layer recorded on every day (ct_static ·
  decree_overlay) and never merged into the CT rows; días-hábiles
  arithmetic runs on the shared engine SV-FREP-FR-203 (never
  re-implemented here); the asueto PAY rules of FR-039/FR-040 attach
  by default ONLY to the CT static rows — overlay-only days (2-Jan,
  Día del Padre, the 5-6-Aug patronales pattern, fin-de-año) carry no
  CT pay obligation and take a configurable pay treatment pending the
  decree instruments (OQ-001; SOQ-19). (LB-014; LB-022; EVID-205;
  EVID-186)
- **SV-PAY-FR-039:** The system shall remunerate asueto days (not
  worked) at *salario básico* computed per the Art. 142-A derivation
  rules — the stored rate of `01_salary-model.md` SV-PAY-FR-005/
  FR-006, never re-derived here — or, for SMM-level workers, the
  max-rule base of `02_minimum-wage.md` SV-PAY-FR-021; period salaries
  are PRESUMED to include asueto pay, so it flows through the
  decomposition invariant of FR-035 (never double-paid as a separate
  line on top of a period salary). (LB-015; EVID-205)
- **SV-PAY-FR-040:** The system shall remunerate work performed on an
  asueto with the *salario extraordinario* — the ordinary salary of
  the day PLUS a 100% recargo of it (= 2×) — and shall compute any
  extraordinary hours worked that day ON the extraordinary salary
  (the 2× day rate is the base the Art. 169 recargo of FR-029 applies
  to, per the Art. 192 second paragraph, stamp (1)); the asueto-worked
  line classifies as rest/asueto-day pay per the canonical matrix of
  SV-PAY-FR-004. (LB-016; EVID-205)
- **SV-PAY-FR-041:** The system shall record the Art. 193 stay-open
  sectors (public essential services that may remain open on asuetos)
  as a sector catalog loaded from the article text (transcription
  pending, OQ-003 — no sectors are invented here); the catalog gates
  SCHEDULING (whether the enterprise may lawfully operate on the
  asueto), while work actually performed under it remunerates per
  FR-040 — the exception is not a pay exception. (LB-017; EVID-205)
- **SV-PAY-FR-042:** The system shall apply the coincidence rule: an
  asueto falling on the worker's assigned descanso semanal pays a
  SINGLE *salario básico* — never séptimo + asueto stacked (no double
  pay) — and if the worker works the coincident day, pays the Art. 192
  extraordinary salary of FR-040 PLUS one remunerated compensatory
  rest day taken the same or the following week, counted as effective
  work and tracked on the FR-036 compensatory counter.
  (LB-018; EVID-205)
- **SV-PAY-FR-043:** The system shall scope the asueto chapter
  (FR-037..FR-042) OUT of *a domicilio* (home) workers and commission,
  *destajo* (piecework) and *ajuste por obra* (work-adjustment)
  workers per Art. 195 — no asueto prestación or asueto-worked recargo
  lines generate for those pay forms (the pay-form flags live on
  `01_salary-model.md` SV-PAY-FR-006); their weekly-rest entitlement
  remains governed by the Arts. 171-176/90-93 rules of §3.3 and, for
  the collection rubros, the `02_minimum-wage.md` SV-PAY-FR-019
  prestación table. (LB-019; LB-020; EVID-205; EVID-203)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in
the client (wave default `odoo`; see §5). No sidecar lives next to this
file: the only dated data consumed is the asueto overlay owned by
`fiscal-reporting/08_filing-calendar.md` (SV-FREP-FR-202 year-keyed
rows) and the SMM prestación values owned by `02_minimum-wage.md`'s
`smm_2025.csv` (SV-PAY-FR-019) — both consumed by FR id.

**Jornada model:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract (work calendar) | sv_pay_jornada_type | select | diurna · nocturna · mixta (classification computed per FR-024) | FR-024 |
| hr.contract (work calendar) | sv_pay_daily_limit / sv_pay_weekly_limit | numeric (computed) | 8/44 · 7/39; peligrosas 7/39 · 6/36; overridden while a valid MTP authorization applies | FR-024, FR-025 |
| hr.contract | sv_pay_mtp_authorization_ref / _valid_from / _valid_to | char/date | dangerous-work MTP exception record | FR-025 |
| hr.attendance (derived) | effective-time flag | computation | pauses inside the jornada count as effective time | FR-026 |
| hr.attendance (validation) | inter-jornada rest ≥ 8h | constraint/flag | compliance finding on violations | FR-027 |

**Recargo engine (on salary rules + attendance buckets):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.salary.rule | sv_pay_recargo_type | select | nocturnal_25_floor · overtime_100 · overtime_fuerza_mayor · rest_day_50_floor · asueto_100 | FR-028, FR-029, FR-030, FR-036, FR-040 |
| hr.payslip (worked-days inputs) | nocturnal_hours / daily_excess_hours / weekly_excess_hours | numeric (computed from attendance) | buckets measured against the FR-024/025 limits; bases read the stored hourly básico (01 FR-005; weekly-excess base = 01 FR-007) | FR-028, FR-029 |
| l10n_sv.pay.permanent.pact (new) | enterprise_case · approval_ref · date_from · date_to · hours/week | select/char/date/numeric | enterprise_case: continuous_24h · sixth_day_recovery_4h; Director General de Trabajo approval recorded | FR-031 |

**Séptimo-día engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip | sv_pay_complete_weeks / sv_pay_septimos | integer (computed) | one per complete semana laboral; incomplete unjustified week = 0 | FR-032 |
| hr.payslip | sv_pay_just_cause_absences | boolean/count | just-cause absence flags preserving the prestación | FR-032, FR-033 |
| hr.payslip | sv_pay_period_decomposition | json (computed) | días laborados + séptimos + asuetos decomposition of the period salary | FR-035 |
| hr.contract (calendar) | sv_pay_rest_day | select + basis | sunday_default · assigned_day (basis: continuous · public_service · normally_sunday · director_auth ref) | FR-034 |
| hr.employee | sv_pay_compensatory_days | counter | rest-day/coincidence compensatory rest owed/taken, same-or-next week, effective-work counted | FR-036, FR-042 |

**Asueto model (dual layer):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.asueto.static (new) | code · name · day_rule · scope | char/select | day_rule: fixed_date · easter_offset (Jue/Vie/Sáb Santo) · san_salvador_aug_3 · san_salvador_aug_5 · local_festivity; scope: national · san_salvador_city · municipality | FR-037 |
| l10n_sv.fiscal.asueto (consumed read-only) | overlay rows + provenance | dated data | OWNED by SV-FREP-FR-202; union view stamps layer = ct_static · decree_overlay | FR-038 |
| l10n_sv.pay.asueto.overlay.config (new) | overlay_pay_treatment | select per overlay day | default: no_ct_pay_obligation; configurable pending decree instruments (OQ-001) | FR-038 |
| res.company / hr.work.location | sv_pay_municipality_festivity | date (config) | the locality's principal festivity day per custom (OQ-002) | FR-037 |
| l10n_sv.pay.asueto.essential.sector (new) | name · active | char/boolean | Art. 193 stay-open sector catalog (transcription pending, OQ-003) | FR-041 |
| hr.salary.rule routing | asueto-scope gate | computation | skip asueto rules for pay forms home_worker · commission_other · destajo/unit_of_work classes (01 FR-006 flags) | FR-043 |

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr / hr_payroll
module family) — every FR maps `odoo`; no SaaS rows are introduced
because none of these FRs touch DTE generation/transformation (the only
architecture-split surface per `shared/docs/saas-thin-client-architecture.md`
D2). Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required beyond the dated-data regime below.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-024 | odoo | hr.contract / resource.calendar | sv_pay_jornada_type, limits | >4 nocturnal hours ⇒ nocturnal limit set (7/39); classification feeds every hour bucket |
| FR-025 | odoo | hr.contract | peligrosas limits + MTP authorization | 7/39 · 6/36; MTP exception as dated config relaxing scope while valid |
| FR-026 | odoo | hr.attendance (computation) | effective time | Pauses inside the jornada count; no limit/surcharge bucket shrinks by them |
| FR-027 | odoo | hr.attendance (validation) | ≥8h inter-jornada rest | Compliance flag; no payslip line of its own |
| FR-028 | odoo | hr.salary.rule / hr.payslip | nocturnal_25_floor × nocturnal_hours | 25% = floor ("por lo menos"); base = stored hourly básico (01 FR-005) |
| FR-029 | odoo | hr.salary.rule / hr.payslip | overtime_100 × excess buckets | 2× hourly básico; weekly-excess base = 01 FR-007 (Art. 142 final); "límite legal" = FR-024/025 caps |
| FR-030 | odoo | hr.salary.rule / attendance flag | overtime_fuerza_mayor | Plain básico, gated on recorded fuerza-mayor condition |
| FR-031 | odoo | l10n_sv.pay.permanent.pact | pact config | 24h-enterprise · 6th-day-recovery-4h cases; Director approval ref; pay stays FR-029/030 |
| FR-032 | odoo | hr.payslip | sv_pay_complete_weeks / septimos | Per-complete-week accrual; unjustified incomplete week loses; SMM base via 02 FR-021 |
| FR-033 | odoo | hr.payslip | no-horario six-day rule | 6 days × ordinary jornada; values = 02 FR-019 Art. 6 table (by id) |
| FR-034 | odoo | hr.contract (calendar) | sv_pay_rest_day + basis | Sunday default; continuous/public-service/normally-Sunday assignment; Director auth otherwise |
| FR-035 | odoo | hr.payslip (computation) | sv_pay_period_decomposition | Presumed-included decomposition; never double-pay; classifies ordinary per 01 FR-004 |
| FR-036 | odoo | hr.salary.rule / hr.employee | rest_day_50_floor + compensatory counter | 50% = floor; compensatory = same/next week, effective work (Art. 176) |
| FR-037 | odoo | l10n_sv.pay.asueto.static | CT Art. 190 base set | STATIC law; municipality festivity config (OQ-002); mobile days resolved per year |
| FR-038 | odoo | l10n_sv.fiscal.asueto (read) + overlay config | union view + provenance layer | Overlay OWNED by SV-FREP-FR-202 (dated, re-seeded annually); engine = SV-FREP-FR-203; overlay pay treatment default none (OQ-001) |
| FR-039 | odoo | hr.salary.rule / hr.payslip | asueto-at-rest básico | Base per 01 FR-005/006; SMM max rule 02 FR-021; decomposition via FR-035 |
| FR-040 | odoo | hr.salary.rule / hr.payslip | asueto_100 (2×) | Extraordinary hours that day compute on the 2× base (Art. 192 stamp (1)) |
| FR-041 | odoo | l10n_sv.pay.asueto.essential.sector | Art. 193 catalog | Scheduling gate, not a pay exception; transcription OQ-003 |
| FR-042 | odoo | hr.payslip / hr.employee | coincidence rule + compensatory | Single básico on coincidence; worked ⇒ FR-040 + compensatory (FR-036 counter) |
| FR-043 | odoo | hr.salary.rule routing | pay-form scope gate | Skip asueto rules for a domicilio / commission / destajo / ajuste (Art. 195); forms per 01 FR-006 |

Version-regime notes (D12): the only dated data in this file's scope is
the asueto overlay (year-keyed rows re-seeded annually from the
published calendar; owned and versioned by
`fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202 — its OQ-003
exact-date pinning applies here kin-wise); the CT Art. 190 base set,
the jornada limits and every recargo rate are STATIC law (SOQ-21 CT
vintage watch). No SMM values are encoded here — file 02's sidecar owns
them.

## 6. Acceptance Criteria

- **AC-001:** Given a *mixta* jornada of 8 scheduled hours of which 5
  fall inside the 19:00-06:00 window, then the jornada classifies as
  NOCTURNAL for duration purposes, its ordinary limits become 7h/day
  and 39h/week, and the 8th hour is extraordinary — remunerated per
  the 2× recargo (FR-024, FR-029).
- **AC-002:** Given a commission-only worker whose SB-R7 daily
  *salario básico* is US$70.00 (the `01_salary-model.md` AC-001 case)
  with the stored hourly básico of US$8.75, when 2 daily-excess hours
  are worked, then the overtime pays 2 × (2 × 8.75) = US$35.00 — the
  Art. 169 recargo on the stored hourly base (FR-029; bases
  SV-PAY-FR-005/007).
- **AC-003:** Given a worker hired Wednesday 15-July-2026 on a
  Monday-Saturday schedule with Sunday rest and a US$480.00 monthly
  salary (daily US$16.00), then July decomposes into días laborados +
  séptimos where the séptimos count ONLY complete semanas laborales
  (the Mon-15→Sat-18 fragment is not a complete week: no séptimo), pay
  prorates as daily × (días laborados + séptimos + asuetos), and NO
  separate séptimo line is added on top of the period salary
  (FR-032, FR-035).
- **AC-004:** Given 15-September falling on the assigned rest day of a
  continuous-enterprise worker with daily básico US$16.00, when the
  day is NOT worked, then the worker receives a single US$16.00 (no
  séptimo+asueto stacking); when the day IS worked, then the pay is
  2 × US$16.00 = US$32.00 plus one remunerated compensatory rest day
  in the same or next week counted as effective work (FR-040, FR-042).
- **AC-005:** Given an hourly básico of US$2.00 and 3 ordinary
  nocturnal-window hours inside the jornada, then the nocturnal
  remuneration is at least 3 × 2.00 × 1.25 = US$7.50 — the 25% is a
  floor and a collective uplift to 30% would pay US$7.80 (FR-028).
- **AC-006:** Given mutual-agreement rest-day work of a full 8-hour
  jornada with daily básico US$16.00, then the day pays US$16.00 +
  US$8.00 (50% floor) = US$24.00 minimum, plus one remunerated
  compensatory day tracked same/next week as effective work; a
  contractual 75% would pay US$28.00 (FR-036).
- **AC-007:** Given a caña collection worker (no horario) who labored
  6 days at the ordinary jornada, then the rest prestación accrues at
  the Art. 6 values of `02_minimum-wage.md` SV-PAY-FR-019 (per
  tarea/tonelada — never restated here); given the same week with 5
  days worked and one UNJUSTIFIED absence, then no prestación accrues
  — a just-cause absence would preserve it (FR-033).
- **AC-008:** Given 2-January-2026 (an overlay-only day in the
  SV-FREP-FR-202 table, absent from CT Art. 190), then the day is
  excluded from días-hábiles arithmetic via the shared engine
  SV-FREP-FR-203 and payroll attaches NO CT asueto pay obligation
  (config default pending decree instruments, OQ-001); given
  6-August, then the CT static row applies and the FR-039/FR-040 pay
  rules run (FR-037, FR-038).
- **AC-009:** Given 2 extraordinary hours worked under a recorded
  fuerza-mayor event with hourly básico US$2.00, then those hours pay
  plain 2 × US$2.00 = US$4.00 — no recargo; absent the flag the same
  hours would pay US$8.00 (FR-030, FR-029).
- **AC-010:** Given a dangerous-task worker on the 7-hour diurnal
  limit with an 8-hour attendance day, then hour 8 is extraordinary
  at the 2× recargo; given a valid MTP authorization relaxing the
  designation for that site, then the ordinary limits revert per the
  authorization scope while valid (FR-025, FR-029).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-19 carried (11_ OQ-1): asueto divergence — the overlay extras (2-Jan, Día del Padre, the Fiestas Patronales del Salvador del Mundo 5-6-Aug pattern vs CT's 3&5-Aug, Fiestas Navideñas y Fin de Año) are executive-decree instruments ABSENT from the corpus; FR-038 defaults overlay-only days to no CT pay obligation with configurable treatment, and exact-date pinning rides fiscal-reporting/08's OQ-003 (annual manual load from the month grids). Decree acquisition would pin the private-pay effects. | no | Takumi S4 (sources watch) | open |
| OQ-002 | Local-festivity day quantification: CT Art. 190's third row is "el día principal de la festividad más importante del lugar, según la costumbre" — no national municipality catalog exists in the corpus; FR-037 carries it as per-locality configuration and each deployment must record its municipality's day (custom, not corpus). | no | Takumi S4 (payroll config) | open |
| OQ-003 | Art. 193 stay-open sector catalog: the article enumerates the public essential services that may remain open on asuetos, but the evidence record abbreviates the list ("enumerated sectors"); FR-041 ships the catalog structure empty of invented values pending transcription from the article at implementation. | no | Takumi S4 (sources watch) | open |
| OQ-004 | Hourly-básico conversion for sub-8h jornadas: file 01's stored hourly rate derives daily ÷ 8 on the 8-hour precedent (its AC-002), and Art. 142-B pins ÷ 8 only for a domicilio (SB-R6); whether a 7-hour nocturna or 6-hour peligrosa jornada converts daily ÷ its own jornada hours is corpus-silent — implementations must not re-derive here (file 01 owns the rate), so the divisor convention needs an 01-side ruling before sub-8h nocturnal recargos compute on a stored hourly rate. | no | Takumi S4 (file 01 owner) | open |
| OQ-005 | Séptimo día of an employment-incomplete week: CT Arts. 171-176 condition the prestación on completing the semana laboral and address absences inside a week, but are silent on whether a termination's tail week (or a mid-week hire's first week) earns a proportional séptimo or nothing; FR-032's zero-accrual reading ships as a disclosed working assumption (corpus-silent default) pending guidance — proportional proration being the live alternative. | no | Takumi S4 (labor ruling watch) | open |
