# GT — Payroll — Working time & overtime: jornada, jornada extraordinaria, descanso semanal y asuetos

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the Guatemala Código de Trabajo (Labor Code, CT, Decreto
1441) working-time model every GT payroll computation runs on: the *jornada*
(workday/workweek) classification of Arts. 116-118 — *diurna* (diurnal)
8h/day 48h/week in the 6:00-18:00 window with the distinctive
45-effective-hours-paid-as-48 rule and its two exception classes
(agro/ganadero workers and <10-worker firms at 48 real hours, with 500+-
worker agro enterprises excluded from the exception), *nocturna* (nocturnal)
6h/36h in the 18:00-6:00 window, *mixta* (mixed) 7h/42h with the
four-or-more-nocturnal-hours reclassification test, and the pactable +2h
daily ordinary increase within the weekly caps; the *jornada extraordinaria*
(overtime) engine of Arts. 121-123 — trigger at the statutory limits OR the
lower contractually-pacted limit, rate floor ≥ +50% over the base salary =
max(statutory minimum, agreed wage), the 12h total daily cap with its
reglamento/siniestro exception family, separate booking of extraordinary
pay in the salary books, the own-fault exclusion, and calamity work paid as
ordinary; the excluded-roles model of Art. 124 — five categories free of
jornada limits yet OT-entitled only beyond 12h/day; the *descanso semanal*
(weekly rest) engine of Art. 126 — one paid rest day after each 5-6-day
workweek per workplace custom, the +1/6 weekly-earnings addition for
unidad-de-obra/comisión workers, and the no-offset coincidence rule of
Art. 127 ¶2; the *asueto* (paid holiday) calendar of Art. 127 — eleven
statutory day-rules including the two half-day entries (24 and 31 December
from 12:00) and the local-festivity day, stored as dated rows with edition
provenance; and the worked rest-day/asueto regime of Arts. 128-129 — the
prior-week ordinary+extraordinary daily-average basis, the implicit
inclusion of unworked rest/asueto days in quincenal/mensual salaries (never
double-paid), worked days paid as the day PLUS hours computed as trabajo
extraordinario (R38: no literal 2× anywhere), and the last-quincena/month
reference for salaried workers' worked hours — plus the weekly-hours
accounting model (horas efectivas vs horas pagadas) and the calendar
distribution validation surface.

It does **not** cover: the *salario* / *salario completo* model, pay-basis
taxonomy and salary books (`01_ct-salary-model.md` — GT-PAY-FR-002,
GT-PAY-FR-005, GT-PAY-FR-017, GT-PAY-FR-019 consumed by id, never
restated); the salario mínimo chassis and dated AG rate tables whose floors
feed the OT base (`03_minimum-wage.md`); statutory bonuses — bono 14,
incentivo, December aguinaldo (`04_statutory-bonuses.md`); vacaciones,
maternidad and menores, whose días-hábiles counting depends on this file's
jornada/week structure (`05_vacaciones-maternidad.md`); contracts, despido
and indemnización (`06_contracts-termination.md`); IGSS contributions and
planilla electrónica (`07_igss-contributions.md`); IRTRA/INTECAP patronal
charges (`08_irtra-intecap.md`); ISR/IVA payroll interfaces
(`09_isr-iva-interfaces.md`); or sanction values (owned by
`gt/requirements/taxation/06_ct-procedures.md` — never derived here).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): **CT labor
LBs cite 32_ as "CT art. N (texto según edición conmemorativa 2024,
MinTrabajo)" — no "current through" date claimable** (commemorative
MinTrabajo print of indeterminate consolidation cutoff — GOQ-70/71; the
qualifier carried on every CT row below IS the R44 mitigation). Rejected
myth never implemented (R38): **no holiday-work literal 2×** — worked
rest-day/asueto pay is the paid day plus OT-computed hours only; no
doubling rule exists anywhere in arts. 126-129. Two evidence elisions
(arts. 118 continuation, 128 gate prefix, 129 ¶3 reference period) are
completed verbatim from the source layer
`gt/.extractions/32_Codigo_Trabajo_D1441.pdf.txt` and marked "(continuación
verificada en el texto fuente)" on the rows below.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT art. 116 ¶1, ¶2, ¶4, ¶5 (texto según edición conmemorativa 2024, MinTrabajo): "La jornada ordinaria de trabajo efectivo diurno no puede ser mayor de ocho horas diarias, ni exceder de un total de cuarenta y ocho horas a la semana." / "La jornada ordinaria de trabajo efectivo nocturno no puede ser mayor de seis horas diarias, ni exceder de un total de treinta y seis horas a la semana." / "Trabajo diurno es el que se ejecuta entre las seis y las dieciocho horas de un mismo día." / "Trabajo nocturno es el que se ejecuta entre las dieciocho horas de un día y las seis horas del día siguiente." | Art. 116: ordinary effective diurnal jornada may not exceed 8 hours/day nor 48 hours/week total; ordinary effective nocturnal jornada may not exceed 6 hours/day nor 36 hours/week; diurnal work = executed between 6:00 and 18:00 of the same day; nocturnal work = executed between 18:00 of one day and 6:00 of the next | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 116 p.63 (EVID-286) |
| LB-002 | CT art. 116 ¶6 (texto según edición conmemorativa 2024, MinTrabajo): "La labor diurna normal semanal será de cuarenta y cinco horas de trabajo efectivo, equivalente a cuarenta y ocho horas para los efectos exclusivos del pago de salario. Se exceptúan… los trabajadores agrícolas y ganaderos y los de las empresas donde labore un número menor de diez, cuya labor diurna normal semanal será de cuarenta y ocho horas de trabajo efectivo, salvo costumbre más favorable al trabajador. Pero esta excepción no debe extenderse a las empresas agrícolas donde trabajen quinientos o más trabajadores." | Art. 116 ¶6: the normal weekly diurnal labor is 45 effective hours, equivalent to 48 hours EXCLUSIVELY for salary-payment purposes; excepted — agricultural and livestock workers and firms where fewer than ten work, whose normal weekly diurnal labor is 48 effective hours, save more-favorable custom for the worker; the exception does not extend to agricultural enterprises with five hundred or more workers | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 116 p.63 (EVID-286) |
| LB-003 | CT art. 117 (texto según edición conmemorativa 2024, MinTrabajo): "La jornada ordinaria de trabajo efectivo mixto no puede ser mayor de siete horas diarias ni exceder de un total de cuarenta y dos horas a la semana." / "No obstante, se entiende por jornada nocturna la jornada mixta en que se laboren cuatro o más horas durante el período nocturno." | Art. 117: the ordinary effective mixed jornada may not exceed 7 hours/day nor 42 hours/week; notwithstanding, a mixed jornada in which four or more hours are worked during the nocturnal period is understood as a nocturnal jornada | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 117 p.64 (EVID-286) |
| LB-004 | CT art. 118 (texto según edición conmemorativa 2024, MinTrabajo): ordinary jornada in work "que por su propia naturaleza no sean insalubres o peligrosos" may "aumentarse entre patronos y trabajadores, hasta en dos horas diarias, siempre que no exceda, a la semana, de los correspondientes límites de cuarenta y ocho horas, treinta y seis horas y cuarenta y dos horas que para la jornada diurna, nocturna o mixta determinen los dos artículos anteriores." (continuación verificada en el texto fuente p.64) | Art. 118: for work not by its own nature unhealthy or dangerous, the ordinary jornada may be increased between employers and workers by up to two hours daily, provided the weekly limits (48/36/42 for diurnal/nocturnal/mixed) of the two preceding articles are not exceeded | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 118 p.64 (EVID-286) |
| LB-005 | CT art. 121 (texto según edición conmemorativa 2024, MinTrabajo): "El trabajo efectivo que se ejecute fuera de los límites de tiempo que determinan los artículos anteriores para la jornada de ordinaria, o que exceda del límite inferior que contractualmente se pacte, constituye jornada extraordinaria y debe ser remunerada por lo menos con un cincuenta por ciento más de los salarios mínimos o de los salarios superiores a estos que hayan estipulado las partes." / "No se consideran horas extraordinarias las que el trabajador ocupe en subsanar los errores imputables sólo a él…" | Art. 121: effective work executed outside the time limits of the preceding articles for the ordinary jornada, or exceeding the lower limit contractually pacted, constitutes extraordinary jornada and must be remunerated at least with fifty percent more than the statutory minimum wages or the wages superior to those that the parties stipulated; hours the worker spends correcting errors attributable solely to himself are not extraordinary hours | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 121 p.65 (EVID-287) |
| LB-006 | CT art. 122 (texto según edición conmemorativa 2024, MinTrabajo): "Las jornadas ordinarias y extraordinarias no pueden exceder de un total de doce horas diarias, salvo casos de excepción muy calificados…" / calamity: "el trabajo que se realice se debe pagar como ordinario" | Art. 122: ordinary and extraordinary jornadas together may not exceed 12 hours daily, save highly qualified exception cases determined in the respective reglamento or where persons, establishments, machines, installations, crops or harvests are endangered by an occurred disaster or imminent risk and workers cannot be substituted or labors suspended; in public calamity the same proviso applies and the work performed must be paid as ordinary | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 122 p.65 (EVID-287) |
| LB-007 | CT art. 123 (texto según edición conmemorativa 2024, MinTrabajo): "Los patronos deben consignar en sus libros de salarios o planillas, separado de lo que se refiera a trabajo ordinario, lo que paguen a cada uno de sus trabajadores por concepto de trabajo extraordinario." | Art. 123: employers must record in their salary books or planillas, SEPARATE from ordinary-work entries, whatever they pay each worker for extraordinary work | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 123 p.66 (EVID-287) |
| LB-008 | CT art. 124 (texto según edición conmemorativa 2024, MinTrabajo): "No están sujetos a las limitaciones de la jornada de trabajo: a) Los representantes del patrono; b) Los que laboren sin fiscalización superior inmediata; c) Los que ocupen puestos de vigilancia o que requieran su sola presencia; d) Los que cumplan su cometido fuera del local… y e) Los demás trabajadores que desempeñen labores que por su indudable naturaleza no están sometidas a jornadas de trabajo." / "…no pueden ser obligadas a trabajar más de doce horas… correspondiéndoles en este supuesto el pago de las horas extraordinarias que se laboren con exceso al límite de doce horas diarias." | Art. 124: not subject to jornada limitations — (a) the employer's representatives, (b) those working without immediate superior supervision, (c) those holding vigilance posts or posts requiring their mere presence, (d) those fulfilling their task outside the business premises (commission agents with worker character), (e) other workers in labors by their undoubted nature not subject to work jornadas; nevertheless none may be obliged to work more than twelve hours, being entitled in that case to payment of extraordinary hours worked in excess of the twelve-hour daily limit | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 124 p.66 (EVID-288) |
| LB-009 | CT art. 126 ¶1-¶2 (texto según edición conmemorativa 2024, MinTrabajo): "Todo trabajador tiene derecho a disfrutar de un día de descanso remunerado después de cada semana de trabajo. La semana se computará de cinco a seis días según, costumbre en la empresa o centro de trabajo." / "A quienes laboran por unidad de obra o por comisión, se les adicionará una sexta parte de los salarios totales devengados en la semana." | Art. 126: every worker is entitled to enjoy one day of remunerated rest after each week of work; the week is computed at five to six days according to the custom in the enterprise or workplace; for those who work by unit of work or on commission, a sixth part of the total salaries earned in the week is ADDED to them | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 126 p.67 (EVID-289) |
| LB-010 | CT art. 127 (texto según edición conmemorativa 2024, MinTrabajo): "Son días de asueto con goce de salario para los trabajadores particulares: el 1o. de enero; el Jueves, Viernes y Sábado Santos; el 1o. de mayo, el 30 de junio, el 15 de septiembre, el 20 de octubre, el 1o. de noviembre, el 24 de diciembre, mediodía, a partir de las doce horas, el 25 de diciembre, el 31 de diciembre, mediodía, a partir de las doce horas, y el día de la festividad de la localidad." / "El patrono esta [sic] obligado a pagar el día de descanso semanal, aún [sic] cuando en una misma semana coincidan uno o más días de asueto, y así mismo cuando coincidan un día de asueto pagado y un día de descanso semanal." | Art. 127: paid-holiday days for private workers — 1 January; Holy Thursday, Friday and Saturday; 1 May; 30 June; 15 September; 20 October; 1 November; 24 December at midday from 12:00; 25 December; 31 December at midday from 12:00; and the day of the locality's festivity; the employer is obligated to pay the weekly-rest day even when one or more holidays coincide within the same week, and likewise when a paid holiday and a weekly-rest day coincide | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 127 p.67 (EVID-289) |
| LB-011 | CT art. 128 (texto según edición conmemorativa 2024, MinTrabajo): "En las empresas en las que se ejecuten trabajos de naturaleza muy especial o de índole continua… se puede trabajar durante los días de asueto o de descanso semanal, pero en estos supuestos el trabajador tiene derecho a que, sin perjuicio del salario que por tal asueto o descanso semanal se le cancele el tiempo trabajado, computándosele como trabajo extraordinario." (prefijo de puerta verificado en el texto fuente p.67: "…según determinación que debe hacer el reglamento, o en casos concretos muy calificados, según determinación de la Inspección General de Trabajo…") | Art. 128: in enterprises executing work of a very special or continuous nature (per reglamento determination) or in concrete highly qualified cases (per the Labor Inspection's determination), work may be performed on holidays or weekly-rest days — but in those cases the worker is entitled, without prejudice to the salary cancelled for such holiday or weekly rest, to the time worked, computed as extraordinary work | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 128 p.67 (EVID-290) |
| LB-012 | CT art. 129 (texto según edición conmemorativa 2024, MinTrabajo): "El pago de los días de descanso semanal o de los días de asueto se debe hacer de acuerdo con el promedio diario de salarios ordinarios y extraordinarios que haya devengado el trabajador durante la semana inmediata anterior al descanso o asueto…" / "…cuando el salario se estipule por quincena o por mes, incluye en forma implícita el pago de los días de descanso semanal o de los días de asueto que no se trabajen." / "…si dichos días se trabajan, el pago de los mismos debe hacerse computando el tiempo trabajado como extraordinario…" (continuación verificada en el texto fuente p.67: "…de conformidad con los salarios ordinarios y extraordinarios que haya devengado el trabajador durante, la ultima [sic] quincena o mes, según corresponda.") | Art. 129: payment of weekly-rest days and holidays is made per the daily average of ordinary and extraordinary salaries earned during the week immediately prior to the rest or holiday; when salary is stipulated by fortnight or month it implicitly includes payment of unworked weekly-rest and holiday days; when those days ARE worked, payment computes the worked time as extraordinary — in accordance with the ordinary and extraordinary salaries earned during the last fortnight or month, as corresponds (source-verified continuation) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 129 p.67 (EVID-290) |

Version regime (D15/D16/D-GT10): the only dated data in this file is the
asueto calendar — stored as day-rule rows of STATIC law (provenance = CT
art. 127, texto según edición conmemorativa 2024, MinTrabajo; no
valid_from claim beyond the edition qualifier, R44/GOQ-70/71) resolved to
concrete per-year dated rows (valid_from/valid_to + provenance,
snapshot-on-write); the Holy-Week entries are moveable and resolve per year
(liturgical computus — deterministic product logic, EVID-289 doubts note);
the festividad de la localidad is per-locality configuration (no national
catalog in the corpus). NO salario mínimo values live in this file — the OT
base floors are owned by `03_minimum-wage.md`'s dated AG tables, consumed
by cross-reference only. The CT text basis never supports a dated
consolidation claim (R44).

## 3. Functional Requirements

### 3.1 Jornada classification and weekly-hours accounting (CT Arts. 116-118)

- **GT-PAY-FR-026:** The system shall classify every worker's ordinary
  *jornada* as (a) *diurna* (diurnal) — work executed between the six and
  eighteen hours of the same day (06:00-18:00), ordinary limits 8 hours/day
  and 48 hours/week; (b) *nocturna* (nocturnal) — work executed between the
  eighteen hours of one day and the six hours of the next (18:00-06:00),
  ordinary limits 6 hours/day and 36 hours/week; or (c) *mixta* (mixed) —
  executed across both periods, ordinary limits 7 hours/day and 42
  hours/week; the classification selects the limit set every downstream
  hour bucket (ordinary / extraordinary) is measured against.
  (LB-001; LB-003; EVID-286)
- **GT-PAY-FR-027:** The system shall apply the mixta→nocturna
  reclassification test: a *jornada mixta* in which four or more hours are
  worked during the nocturnal period (18:00-06:00) is understood as a
  *jornada nocturna* for the purpose of its duration — its ordinary limits
  become 6 hours/day and 36 hours/week, and hours beyond those limits are
  extraordinary (FR-032). (LB-003; EVID-286)
- **GT-PAY-FR-028:** The system shall implement the 45-effective-paid-as-48
  rule: the normal weekly diurnal labor is **45 hours of effective work,
  equivalent to 48 hours exclusively for salary-payment purposes** — the
  weekly salary of a full standard diurnal week pays the 48-hour equivalent
  although effective time is 45; the equivalence operates on PAY only (the
  ordinary/extraordinary boundary of FR-032 still runs at the Art. 116
  limits or the contractual lower limit, never at 45). (LB-002; EVID-286)
- **GT-PAY-FR-029:** The system shall classify every diurnal worker into
  the Art. 116 ¶6 exception classes: (a) *standard* — 45 effective hours
  paid as 48 (FR-028); (b) *agro/ganadero* — agricultural and livestock
  workers whose normal weekly diurnal labor is **48 real effective hours**
  (no 45→48 uplift); (c) *under-ten* — workers of enterprises where fewer
  than ten work, likewise 48 real effective hours; with (d) the exception
  NEVER extending to agricultural enterprises where five hundred or more
  workers work (they revert to standard 45-paid-as-48), and (e) a recorded
  *costumbre más favorable al trabajador* (custom more favorable to the
  worker) prevailing over the 48-real rule of classes (b)/(c). The class
  drives FR-028's application and FR-031's counters.
  (LB-002; EVID-286)
- **GT-PAY-FR-030:** The system shall admit a recorded +2h daily-increase
  pact: for work not by its own nature *insalubres o peligrosos* (unhealthy
  or dangerous), the ordinary jornada may be increased between employers
  and workers by up to **two hours daily**, provided the weekly limits
  (48/36/42 per class) are not exceeded — hours within the raised daily
  limit remain ordinary; hours beyond it are extraordinary (FR-032).
  (LB-004; EVID-286)
- **GT-PAY-FR-031:** The system shall keep a weekly-hours accounting model
  with two separate counters per worker and week — *horas efectivas*
  (effective hours: attendance-classified time per FR-026/FR-027 buckets)
  and *horas pagadas* (paid hours: effective hours transformed by the
  FR-028/FR-029 rule of the worker's exception class) — feeding the
  ordinary/extraordinary separation of the salary books
  (`01_ct-salary-model.md` GT-PAY-FR-017), the MinTrabajo annual report
  (GT-PAY-FR-019) and the *salario completo* component tagging
  (GT-PAY-FR-005), never merged into a single bucket.
  (LB-002; LB-001; EVID-286, EVID-287)

### 3.2 Jornada extraordinaria — the overtime engine (CT Arts. 121-123)

- **GT-PAY-FR-032:** The system shall constitute *jornada extraordinaria*
  (extraordinary jornada/overtime) for all effective work executed outside
  the time limits of Arts. 116-118 for the ordinary jornada (per the
  FR-026/FR-027 class limits, as optionally raised by a valid FR-030 pact)
  **or exceeding the lower limit contractually pacted** — a contractual
  ordinary limit below the statutory one moves the OT boundary to the
  contractual line. (LB-005; EVID-287, EVID-286)
- **GT-PAY-FR-033:** The system shall remunerate every extraordinary hour
  at a rate of AT LEAST +50% (≥ 1.5×) over the base salary — the statutory
  minimum wage OR the wage superior to it that the parties stipulated
  (*max(statutory minimum, agreed wage)*): an agreed wage above the minimum
  is the base; an agreed wage below the minimum floors at the statutory
  minimum ("por lo menos" makes +50% a floor, configurable upward, never
  below). The minimum side of the base is the dated AG floor owned by
  `03_minimum-wage.md` (consumed by filename cross-reference, never
  restated here). (LB-005; EVID-287)
- **GT-PAY-FR-034:** The system shall validate that ordinary and
  extraordinary jornadas together do not exceed **twelve hours daily**,
  admitting exceptions only under the Art. 122 family — highly qualified
  cases determined in the respective *reglamento*, or disaster/imminent
  risk endangering persons, establishments, machines, installations, crops
  or harvests where workers cannot be substituted or labors suspended —
  each as a recorded exception flag; unflagged >12h days raise a compliance
  finding on the timesheet/calendar feed. (LB-006; EVID-287)
- **GT-PAY-FR-035:** The system shall book extraordinary-work pay
  SEPARATELY from ordinary work in the *libros de salarios o planillas*
  (salary books or planillas) — the Art. 123 separation lands on the
  book-mode machinery of `01_ct-salary-model.md` GT-PAY-FR-017/GT-PAY-FR-018
  and the OT lines carry the *extraordinaria* component tag of GT-PAY-FR-005.
  (LB-007; EVID-287)
- **GT-PAY-FR-036:** The system shall exclude from extraordinary hours the
  hours the worker spends *subsanar los errores imputables sólo a él*
  (correcting errors attributable solely to himself) and hours that are the
  consequence of his own lack of activity during the ordinary jornada where
  attributable to him — no OT line generates for such hours.
  (LB-005; EVID-287)
- **GT-PAY-FR-037:** The system shall remunerate extraordinary work
  performed under a recorded *calamidad pública* (public calamity)
  condition — where the extraordinary work is necessary to conjure or
  attenuate it — AS ORDINARY work (plain rate, no +50% recargo); unflagged
  extraordinary hours never take the plain rate.
  (LB-006; EVID-287)

### 3.3 Excluded roles — jornada-limit exemptions (CT Art. 124)

- **GT-PAY-FR-038:** The system shall flag as exempt from jornada-limit
  application (no ordinary daily/weekly caps of FR-026/FR-027 tested) the
  five Art. 124 categories: (a) *representantes del patrono* (the
  employer's representatives); (b) those working *sin fiscalización
  superior inmediata* (without immediate superior supervision); (c)
  *puestos de vigilancia o que requieran su sola presencia* (vigilance
  posts or posts requiring mere presence); (d) those fulfilling their task
  outside the business premises (commission agents with worker character);
  (e) labors by their undoubted nature not subject to work jornadas. The
  exemption flag is contract/employee configuration with its category
  recorded. (LB-008; EVID-288)
- **GT-PAY-FR-039:** For FR-038-excluded workers the system shall enforce
  the twelve-hour protection: they cannot be obliged to work more than
  twelve hours daily (save the same qualified-exception flags of FR-034),
  and their overtime entitlement attaches ONLY to hours worked *con exceso
  al límite de doce horas diarias* (in excess of the twelve-hour daily
  limit) — hours within the first twelve pay ordinary and generate no OT
  line; hours beyond twelve are extraordinary per FR-032/FR-033.
  (LB-008; EVID-288)

### 3.4 Descanso semanal (CT Art. 126)

- **GT-PAY-FR-040:** The system shall accrue one day of *descanso
  remunerado* (remunerated rest) after each week of work for every worker,
  with the week computed at **five to six days** according to the custom in
  the enterprise or workplace — the recorded week-length configuration
  (5-day or 6-day semana, with its custom basis) drives the rest-day
  accrual cadence and the day-counting surface consumed by
  `05_vacaciones-maternidad.md` for días-hábiles arithmetic.
  (LB-009; EVID-289)
- **GT-PAY-FR-041:** For workers paid *por unidad de obra o por comisión*
  (unit of work or commission — the taxonomy of
  `01_ct-salary-model.md` GT-PAY-FR-002), the system shall ADD *una sexta
  parte* (a sixth part, 1/6) of the *total weekly earnings* as the rest-day
  remuneration — the addition is an explicit line on top of the week's
  earnings (no implicit inclusion for these pay forms), computed as
  (ordinary + extraordinary weekly earnings) ÷ 6.
  (LB-009; EVID-289)
- **GT-PAY-FR-042:** The system shall apply the no-offset coincidence
  rule: the weekly-rest-day pay obligation stands EVEN WHEN one or more
  asueto days coincide within the same week, and likewise when a paid
  asueto day coincides with the weekly-rest day — neither day cancels,
  offsets or absorbs the other; each remains payable under its own rule
  (FR-045/FR-046), with no double-counting of the same day as two rest
  days. (LB-010; EVID-289)

### 3.5 Asueto calendar — statutory paid holidays (CT Art. 127)

- **GT-PAY-FR-043:** The system shall store the statutory *días de asueto
  con goce de salario* (paid holidays) for *trabajadores particulares*
  (private workers) as day-rule rows with edition provenance: 1 January;
  Jueves Santo (Holy Thursday); Viernes Santo (Good Friday); Sábado Santo
  (Holy Saturday); 1 May; 30 June; 15 September; 20 October; 1 November;
  **24 December — half day, from 12:00 (mediodía)**; 25 December; **31
  December — half day, from 12:00**; plus the day of the *festividad de la
  localidad* (locality's festivity). Rows are STATIC law (provenance = CT
  art. 127, texto según edición conmemorativa 2024, MinTrabajo) resolved to
  per-year dated rows under the D15/D16 regime (valid_from/valid_to,
  snapshot-on-write); half-day entries pay half the daily-average basis and
  their worked-time computation covers the worked (afternoon) portion
  only. (LB-010; EVID-289)
- **GT-PAY-FR-044:** The system shall resolve the calendar's moveable and
  local entries per year: the Holy-Week Thursday/Friday/Saturday rows
  resolve to concrete dates via the liturgical (Easter) computus —
  deterministic product-side arithmetic (EVID-289 doubts note), stamped
  with year + provenance on the resolved rows; the *festividad de la
  localidad* resolves from per-locality configuration (the corpus names no
  national municipality catalog — each deployment records its locality's
  festivity day; a configuration requirement, not an invented value).
  (LB-010; EVID-289)

### 3.6 Rest-day/asueto pay and worked days (CT Arts. 128-129) — R38 territory

- **GT-PAY-FR-045:** The system shall pay unworked *descanso semanal* and
  *asueto* days at the daily average of **ordinary AND extraordinary**
  salaries earned during the week immediately prior to the rest or holiday
  (*promedio diario de salarios ordinarios y extraordinarios… semana
  inmediata anterior*) — composition mirrors the *salario completo*
  tagging of `01_ct-salary-model.md` GT-PAY-FR-005 (ordinary +
  extraordinary components, never re-derived here); half-day asuetos take
  half the daily average. (LB-012; EVID-290)
- **GT-PAY-FR-046:** The system shall implement the implicit-inclusion
  invariant: when the salary is stipulated *por quincena o por mes* (by
  fortnight or month), it **implicitly includes** the pay of unworked
  weekly-rest and asueto days — payroll shall NOT add a separate
  rest/asueto line on top of such a period salary (no double pay);
  decomposition into worked days + rest days + asuetos serves proration
  and reporting only, reproducing the period total exactly. Explicit
  rest-day lines exist only for pay forms outside quincenal/mensual
  stipulation (e.g. the FR-041 sixth-part line for obra/comisión workers).
  (LB-012; EVID-289, EVID-290)
- **GT-PAY-FR-047:** The system shall remunerate work performed on an
  asueto or weekly-rest day as the composite: (a) the day's salary — the
  FR-045 daily average, implicitly included for quincenal/mensual salaries
  per FR-046 — PLUS (b) the worked time *computándosele como trabajo
  extraordinario* (computed as extraordinary work) at the FR-033 rate.
  Work on such days arises lawfully only within the Art. 128 gate
  (very-special/continuous-enterprise work per reglamento determination,
  or concrete highly-qualified cases per the Inspección General de
  Trabajo — LB-011 gate prefix, source-verified): the gate is a scheduling
  compliance flag on the calendar, never a pay modifier.
  (LB-011; EVID-290, EVID-287)
- **GT-PAY-FR-048:** For workers whose salary is stipulated *por quincena
  o por mes*, the system shall compute the extraordinario component of
  worked rest-day/asueto hours on the reference period of Art. 129 ¶3 —
  the ordinary and extraordinary salaries earned during the **last
  quincena or month, as corresponds** (source-verified continuation of
  LB-012; the evidence quote elides the reference period) — rather than
  the FR-045 prior-week average, which governs the DAY pay.
  (LB-012; EVID-290)
- **GT-PAY-FR-049:** NEGATIVE FR (R38 citation guard): NO payroll rule
  shall implement holiday or rest-day work as a literal 2× (doubling) rate
  — the CT regime is exclusively the FR-047 composite (paid day +
  OT-computed hours; economically ≈ up to 2.5× the ordinary day built from
  the two components, never a doubling rule), and any 2×-shaped rule
  citing arts. 126-129 is rejected at definition time.
  (LB-011; LB-012; EVID-290; R38)

### 3.7 Calendar distribution validation

- **GT-PAY-FR-050:** The system shall validate each worker's weekly
  calendar distribution authoritatively on the saas side: day-level jornada
  classes vs the FR-026/FR-027 windows and limits, the FR-034 twelve-hour
  cap, the FR-030 weekly caps, the FR-040 5-6-day week structure, and
  rest-day placement vs asueto coincidences (FR-042) — emitting compliance
  findings consumed by the odoo surfaces; the odoo-side classification and
  attendance buckets (FR-026..FR-039) feed the validation, which never
  computes payslip amounts of its own.
  (LB-001; LB-003; LB-006; LB-009; EVID-286, EVID-287, EVID-289)

## 4. Data Model

Layer semantics: payroll computation is Odoo-native; the asueto calendar
dated rows are `shared` (both sides resolve the same row); calendar
distribution validation is `saas` with odoo surfaces. The only dated data
in scope is the asueto calendar (§2 version regime); no salario mínimo
values live here (file 03 owns the AG tables).

**Jornada model and weekly accounting:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract / resource.calendar | gt_pay_jornada_type | select | diurna · nocturna · mixta (classification per windows; ≥4 nocturna hours ⇒ nocturna limits) | FR-026, FR-027 |
| hr.contract | gt_pay_daily_limit / gt_pay_weekly_limit | numeric (computed) | 8/48 · 6/36 · 7/42; +2h/day while a valid FR-030 pact applies | FR-026, FR-030 |
| hr.contract (pact) | gt_pay_plus2h_pact / basis | boolean + ref | recorded daily-increase pact (non-insalubres work) | FR-030 |
| hr.payroll (company config) | gt_pay_45_48_class | computed select | standard_45_paid_48 · real_48_agro_ganadero · real_48_under10 · standard_45_paid_48_agro_500plus; costumbre-más-favorable override ref | FR-028, FR-029 |
| hr.payslip (weekly counters) | gt_pay_effective_hours / gt_pay_paid_hours | numeric (computed) | effective vs paid hours per week; 45→48 transformation per class | FR-031 |

**Overtime engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip (worked-days inputs) | gt_pay_ordinary_hours / gt_pay_extraordinary_hours | numeric (computed from attendance) | buckets vs class limits or the contractual lower limit; excluded-role workers: only >12h hours are OT | FR-032, FR-039 |
| hr.salary.rule | gt_pay_ot_rate | formula | ≥ 1.5 × hourly base of max(statutory minimum, agreed wage); floor configurable upward | FR-033 |
| hr.attendance (flags) | gt_pay_own_fault / gt_pay_calamity | boolean | own-fault make-up time (no OT); recorded public-calamity condition (plain rate) | FR-036, FR-037 |
| hr.attendance (validation) | 12h daily cap | constraint/flag | >12h ordinary+extraordinary raises a finding save qualified-exception flags (reglamento / siniestro) | FR-034 |
| hr.payroll (books) | extraordinary separation | book constraint | OT pay consigned separately from ordinary in libro/planilla (GT-PAY-FR-017 machinery) | FR-035 |

**Excluded roles:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract / hr.employee | gt_pay_jornada_exemption | select + category | representatives · no_immediate_supervision · vigilance_presence · off_premises_commissionist · nature_of_work | FR-038 |
| hr.attendance (derived) | excluded-role OT bucket | computation | hours in excess of 12/day = extraordinario; ≤12h = ordinary | FR-039 |

**Descanso semanal:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| resource.calendar (week config) | gt_pay_week_days / custom basis | select + ref | 5 · 6 days per workplace custom | FR-040 |
| hr.payslip line | gt_pay_sixth_part | monetary (computed) | (ordinary+extraordinary weekly earnings) ÷ 6 — obra/comisión pay forms only | FR-041 |
| hr.payslip | coincidence handling | computation | rest day owed despite same-week or same-day asueto coincidence; no offset | FR-042 |

**Asueto calendar (shared dated rows) and worked days:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.asueto (shared) | code · name · day_rule · half_day · scope · provenance · valid_from/valid_to | char/select/date rows | day_rule: fixed_date (1-Jan, 1-May, 30-Jun, 15-Sep, 20-Oct, 1-Nov, 25-Dec) · easter_offset (Thu/Fri/Sat Santo) · half_day_from_noon (24-Dec, 31-Dec) · local_festivity; provenance = CT art. 127 (texto según edición conmemorativa 2024, MinTrabajo); snapshot-on-write | FR-043 |
| l10n_gt.pay.asueto.resolved (shared) | date · year · provenance | dated rows | per-year resolution (computus for Holy Week; per-locality config for festividad) | FR-044 |
| res.company / hr.work.location | gt_pay_local_festivity | date (config) | the locality's festivity day (deployment configuration; no national catalog) | FR-044 |
| hr.payslip | gt_pay_rest_day_basis | monetary (computed) | prior-week ordinary+extraordinary daily average (half for half-day asuetos) | FR-045 |
| hr.payslip (decomposition) | gt_pay_period_decomposition | json (computed) | worked days + rest days + asuetos of a quincenal/mensual salary; reproduces period total; never a separate line on top | FR-046 |
| hr.payslip line | gt_pay_worked_rest_ot | monetary (computed) | worked rest/asueto hours at the FR-033 rate; reference period selector: prior_week (day workers) · last_quincena · last_month (salaried, Art. 129 ¶3) | FR-047, FR-048 |
| l10n_gt.pay.guard | negative row | char | holiday_2x = REJECTED (R38): day + OT components only | FR-049 |

**Validation surface:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| saas calendar validator | weekly distribution findings | validation output | windows/limits · 12h cap · week structure · rest-day/asueto coincidences; odoo feeds, saas validates | FR-050 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `saas` =
authoritative computation/validation in the Elixir core; `shared` =
contract items both sides must honor identically. Payroll-wave defaults
(binding): jornada classification + OT computation = `odoo`; asueto
calendar dated rows = `shared`; calendar distribution validation = `saas`.
Model names stable across Odoo 17/18/19/20; no version-specific behavior
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-026 | odoo | hr.contract / resource.calendar | gt_pay_jornada_type + limits | Windows 6-18 / 18-6; 8/48 · 6/36 · 7/42; classification feeds every hour bucket |
| FR-027 | odoo | hr.contract (computed) | ≥4 nocturna hours ⇒ nocturna | Reclassification test on daily distribution; limits become 6/36 |
| FR-028 | odoo | hr.payslip (computation) | 45→48 paid-hours transform | Pay-equivalence only; OT boundary stays at Art. 116 limits/contractual limit |
| FR-029 | odoo | hr.payroll (company config) | gt_pay_45_48_class | agro/ganadero + <10 real 48; agro ≥500 excluded; costumbre más favorable override |
| FR-030 | odoo | hr.contract (pact) | +2h/day pact | Non-insalubres work; within 48/36/42 weekly caps |
| FR-031 | odoo | hr.payslip | effective/paid hours counters | Feeds GT-PAY-FR-017/019 separation and GT-PAY-FR-005 tagging |
| FR-032 | odoo | hr.attendance / hr.payslip | OT bucket | Trigger at statutory limits OR contractual lower limit |
| FR-033 | odoo | hr.salary.rule / hr.payslip | ≥1.5 × max(minimum, agreed) | Floor configurable upward; AG minimum side owned by file 03 (cross-ref) |
| FR-034 | odoo | hr.attendance (validation) | 12h/day cap flag | Exceptions: reglamento cases / siniestro-riesgo inminente flags |
| FR-035 | odoo | hr.payroll (books) | separate extraordinary booking | Art. 123 separation on GT-PAY-FR-017 book modes |
| FR-036 | odoo | hr.attendance (flag) | own-fault exclusion | Own-error correction / own inactivity: no OT line |
| FR-037 | odoo | hr.salary.rule / attendance flag | calamity plain rate | Recorded calamidad pública condition gates the plain rate |
| FR-038 | odoo | hr.contract / hr.employee | gt_pay_jornada_exemption | Five Art. 124 categories; no limit tests apply |
| FR-039 | odoo | hr.attendance (derived) | >12h = OT only | Excluded-role workers: hours 1-12 ordinary |
| FR-040 | odoo | resource.calendar | week = 5-6 days | Custom basis recorded; días-hábiles surface consumed by file 05 |
| FR-041 | odoo | hr.payslip line | sixth-part line | (ordinary+extraordinary weekly earnings) ÷ 6; obra/comisión only |
| FR-042 | odoo | hr.payslip | coincidence no-offset | Rest day owed despite same-week/same-day asueto; no double-count |
| FR-043 | shared | — (dated rows §4) | l10n_gt.pay.asueto rows | STATIC law provenance (CT art. 127, edición conmemorativa 2024); both sides resolve the same rows |
| FR-044 | shared | — (dated rows §4) | resolved per-year rows | Easter computus (deterministic); local festivity = per-locality config |
| FR-045 | odoo | hr.payslip | rest/asueto day basis | Prior-week ordinary+extraordinary daily average; half for half-days |
| FR-046 | odoo | hr.payslip (computation) | implicit inclusion | Quincenal/mensual salaries: no separate rest/asueto line on top |
| FR-047 | odoo | hr.salary.rule / hr.payslip line | day + worked-hours OT | Art. 128 gate = scheduling flag, never a pay modifier |
| FR-048 | odoo | hr.payslip line | reference-period selector | Salaried worked hours: last quincena/month (Art. 129 ¶3) |
| FR-049 | shared | — (guard row §4) | holiday_2x = REJECTED | R38 guard honored identically by both sides' catalogs |
| FR-050 | saas | — (odoo emits feeds) | calendar distribution validation | Authoritative saas validation; findings consumed by odoo surfaces; no payslip amounts |

Version-regime notes: the asueto calendar rows are the only dated data
(per-year resolved rows re-seeded annually via computus/configuration,
provenance = the CT edition — R44: no dated-consolidation claim); every
jornada limit and rate in this file is STATIC law; the OT base's minimum
side is file 03's dated AG data, consumed by cross-reference only.

## 6. Acceptance Criteria

- **AC-001:** Given a *mixta* day of 7 scheduled hours of which 4 fall
  inside 18:00-06:00, then the day classifies as NOCTURNA for duration
  purposes, its ordinary limits become 6h/day and 36h/week, and the 7th
  hour is extraordinary at the FR-033 rate (≥1.5× the base).
  (FR-026, FR-027, FR-032, FR-033)
- **AC-002:** Given a standard-class diurnal worker completing 45
  effective hours in the week, then the weekly salary pays the 48-hour
  equivalent (paid-hours counter = 48, effective = 45); given the same
  worker at 47 effective hours (within the 48h cap, no lower contractual
  limit), then hours 46-47 are ordinary paid hours and the week's ordinary
  salary still anchors on the 48-paid-hour equivalence.
  (FR-028, FR-029, FR-031, FR-032)
- **AC-003:** Given an agricultural enterprise with 8 workers, then its
  diurnal class = real 48 effective hours (no 45→48 uplift); given an
  agricultural enterprise with 600 workers, then the standard 45-as-48
  class applies; given a recorded costumbre más favorable in the 8-worker
  firm, then the custom prevails over the 48-real rule.
  (FR-029)
- **AC-004:** Given a worker whose agreed wage exceeds the statutory
  minimum, then the OT base = the agreed wage; given an agreed wage below
  the minimum, then the base floors at the statutory minimum (file 03's
  dated AG value — never restated here); in both cases each extraordinary
  hour pays at least 1.5× the hourly base, and a contractual uplift to
  1.75× pays 1.75× ("por lo menos" floor). (FR-033)
- **AC-005:** Given a contract pacting a 7-hour ordinary diurnal day
  (below the statutory 8), when an 8th hour is worked, then that hour
  constitutes jornada extraordinaria (contractual lower-limit trigger).
  (FR-032)
- **AC-006:** Given a day of 9 ordinary + 4 extraordinary hours = 13h
  without an exception flag, then the FR-034 violation finding raises;
  given a vigilance-post worker (excluded role) working 14 hours, then
  hours 1-12 pay ordinary and only hours 13-14 generate OT lines.
  (FR-034, FR-038, FR-039)
- **AC-007:** Given a pay period with Q500 of trabajo extraordinario, then
  the libro de salarios / planilla carries that amount SEPARATED from
  ordinary-work pay, and the OT lines carry the extraordinaria component
  tag of GT-PAY-FR-005. (FR-035)
- **AC-008:** Given one after-shift hour spent correcting the worker's own
  error (own-fault flag), then no extraordinary line generates for it;
  given the same hour spent on employer-driven excess work, then it is
  extraordinary. (FR-036, FR-032)
- **AC-009:** Given 3 extraordinary hours worked under a recorded public
  calamity condition, then those hours pay at the plain ordinary rate (no
  +50%); absent the flag, the same hours pay ≥1.5×.
  (FR-037, FR-033)
- **AC-010:** Given a destajo (unit-of-work) worker with total weekly
  earnings of Q600 (ordinary + extraordinary), then the rest-day addition
  computes Q600 ÷ 6 = Q100 as an explicit line on top of the week's
  earnings. (FR-041)
- **AC-011:** Given a week containing one asueto and the worker's rest
  day, and separately an asueto falling exactly on the rest day, then in
  both cases the rest-day pay obligation stands — nothing cancels and the
  same day is never paid twice as two rest days. (FR-042)
- **AC-012:** Given 24 December, then the asueto row is a half-day from
  12:00 paying half the FR-045 daily average; given the Holy-Week rows,
  then each year's resolution carries concrete dates from the computus
  with year + provenance stamped; given a locality with its festivity day
  configured, then that dated row participates in the calendar.
  (FR-043, FR-044, FR-045)
- **AC-013:** Given a day-paid worker with a prior-week ordinary +
  extraordinary daily average of Q120 (hourly base Q15 over 8h) working a
  full 8-hour asueto, then the pay = Q120 (the day) + 8 × Q15 × 1.5 =
  Q120 + Q180 = Q300 — the composite of day + OT hours, and NEVER a
  2×-day rule (which would pay Q240-shaped output); given a monthly-salaried
  worker working the same day, then no separate day line pays (implicit
  inclusion) and the worked hours compute as extraordinario on the
  last-month ordinary+extraordinary average. (FR-045..FR-049)
- **AC-014:** Given a proposed salary rule "holiday work = 2× the day"
  citing arts. 127-129, then the FR-049 citation guard rejects it at
  definition time (R38). (FR-049)
- **AC-015:** Given a work calendar distributing 13h days or 50
  diurnal hours in a week, then the saas calendar-distribution validation
  emits findings against the FR-026/FR-027 limits and the FR-034 cap,
  consumed by the odoo surfaces; the validator itself produces no payslip
  amounts. (FR-050)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.3);
NONE are assigned to this file. GOQ-70/71 (R44 edition discipline) are
discharged by the qualifier on every CT LB row (§2) — the same treatment
as `01_ct-salary-model.md`; GOQ-72/73 belong to other P1 slices. No OQ
rows are registered here, and no new OQ ids are invented. Two genuine
gaps surfaced during synthesis and are REPORTED to the wave lead (task
report) instead of being registered: (a) the OT hourly-base derivation
divisor (daily ÷ jornada hours vs the AG tables' printed hourly rates) is
corpus-silent in this file's evidence slice — FR-033 pins only
max(minimum, agreed), and the interplay belongs with file 03's rate
tables; (b) the festividad de la localidad has no national catalog in the
corpus — FR-044 carries it as per-locality configuration, a deployment
data-acquisition need rather than a trace gap.
