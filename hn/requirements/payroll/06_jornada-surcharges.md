# HN — Payroll — CT jornada, surcharges, séptimo día & feriados

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster P8 — the Código del
Trabajo (Labor Code, CT) working-time and surcharge layer. It owns: (a) the
**jornada ordinaria frame** — the three statutory shift types (*jornada
diurna/nocturna/mixta*, day/night/mixed working day) with the 05:00/19:00
clock boundaries, the mixta ≥3-night-hours flip, the daily/weekly caps, the
44-worked-hours-paid-as-48 rule for diurna (R-H61) with the fn.29 salary
equivalences (48h diurna = 36h nocturna = 42h mixta), the Art. 325
excluded-roles catalog with its 12-hour presence cap, and the Art. 322
absence-proration base; (b) the **surcharge engine** — the night +25% recargo,
the overtime multiplier matrix ×1.25/×1.50/×1.75 (the ×1.75 tier being
prolongation of a night shift on the night-salary base), the ≤12h/day and
≤4×/week caps, the error-recovery exclusion, and the Art. 335 statutory duty
to book overtime SEPARATELY in planillas (payroll registers); (c) the
**séptimo día** (7th-day weekly paid rest, 1 per 6 worked) with the ÷6 /
÷-days-worked prior-week average routine; (d) the **11 paid feriados**
(national holidays) as dated configuration (D. 275-1960 vintage text) with
the pay-even-on-Sunday rule, the two-holiday collision collapse, the ÷6
average holiday pay, the quincenal/monthly implicit-inclusion rule and the
suspended-unlisted-fiesta pay rule; (e) **work on rest days/holidays** — ×2
pay proportional to time plus the substitute-rest right, and the railway
variant (duplo OR +1 vacation day, ≤12×/year); (f) the **OT prescription
timing anchor** (Art. 867: OT claims run from the payment date of the
covering period's ordinary salary); and (g) the **classification interface**
— surcharge earnings are *salario* per CT Art. 361 and feed the salary
concept families and the ISR plantilla strictly by id.

It does **not** own: SMM values/promedio rows — `01_smm-chassis.md`
(HN-PAYR-FR-001..040); 13th/14th month and bono — `02_13th-14th-bono.md`
(HN-PAYR-FR-051..087); IHSS contributions and incapacidad —
`03_ihss-cotizaciones.md` (HN-PAYR-FR-101..135) and
`04_ihss-incapacidad.md` (HN-PAYR-FR-141..170); RAP/fondo —
`05_rap-fondo.md` (HN-PAYR-FR-181..215); vacaciones computation (this file
only ACCRUES the railway +1-vacation-day election and forwards it) —
`07_vacaciones.md` (HN-PAYR-FR-261..280); cesantía/preaviso —
`08_cesantia-preaviso.md` (HN-PAYR-FR-291..325); suspension and
maternity/minor schedule shaping — `09_suspension-maternity-special.md`
(HN-PAYR-FR-331..357); the salario definition, pay periods, salario-completo
indemnity base and Libro de Salarios/planilla record formats —
`10_salario-concepts-records.md` (HN-PAYR-FR-371..405); the ISR plantilla engines
(this file only supplies OT/bonus amounts into annual gross, by id) —
taxation/04 (HN-TAX-FR-121..153, esp. FR-126); deduction semantics /
Art. 10 exclusions — taxation/02 (HN-TAX-FR-046..078); the DJIMR export
contract — fiscal-reporting/02 (HN-FREP-FR-054/055) on the
fiscal-reporting/01 chassis (HN-FREP-FR-001..032); comprobante de retención /
patronos-exempt-unless-requested — e-invoicing/03 (HN-EINV-FR-139/140).

## 2. Legal Basis

Authority order (binding, per master evidence index): jornada family = `86_`
(Código del Trabajo, D. 189-1959, CEDIJ consolidation print) Arts. 318-341
(+ Art. 283 railway rest-day variant + Art. 867 prescription), article map
per R-H59 — jornada = Arts. 318-341, never the drifted numbers (`86_ OQ-4`);
consolidation vintage pinned to D. 278-2013 (`86_ OQ-1` — file-level OQ-001).
D. 117-2021 (`89_`) interprets Art. 113.1 only — never cited for jornada
articles. **R-H57 guard (cited once, this table's LB-013)**: `85_` (D. 93-2021)
derogates ZERO Código del Trabajo articles — its derogated PENAL article
numbers collide numerically with live CT articles 337/346/368 etc.; no
D. 93-2021 never-implement flag applies to any article of this file.
D-H1/D-H2/D-H3 bind everything (dated rows, payslip-period resolution,
never-guess rule, aggregate ingestion depths).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT Art. 321: "Trabajo diurno es el que se ejecuta entre las cinco horas (5:00 a. m.) y las diecinueve (7:00 p. m.); nocturno, el que se realiza entre las diecinueve horas (7:00 p. m.) y las cinco (5:00 a. m.). Es jornada mixta, la que comprende períodos de tiempo de las jornadas diurna y nocturna, siempre que el período nocturno abarque menos de tres (3) horas, pues en caso contrario, se reputará como jornada nocturna. La duración máxima de la jornada mixta será de siete (7) horas diarias y de cuarenta y dos (42) a la semana." | CT Art. 321: day work is that performed between 05:00 and 19:00; night work between 19:00 and 05:00; a mixed working day comprises both day and night periods provided the night period covers less than 3 hours — otherwise it is deemed a night working day; mixed-day maximum duration 7 hours daily and 42 weekly. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 321 (p.94) (EV85:EVID-310) |
| LB-002 | CT Art. 322 + fn.29 (interp. D.96-1961): "La jornada ordinaria de trabajo diurno no podrá exceder de ocho (8) horas diarias y cuarenta y cuatro (44) a la semana, equivalentes a cuarenta y ocho (48) de salario. La jornada ordinaria de trabajo nocturno no podrá exceder de seis (6) horas diarias y treinta y seis (36) a la semana…El trabajador que faltare en alguno de los días de la semana y no completare la jornada de cuarenta y cuatro (44) horas de trabajo, sólo tendrá derecho a recibir un salario proporcional al tiempo trabajado, con base en el salario de cuarenta y ocho (48) horas semanales." fn.29: "El salario que corresponde a cuarenta y ocho (48) horas semanales de las jornadas de trabajo diurno, será igual al salario de treinta y seis (36) horas de la jornada nocturna y cuarenta y dos (42) de la mixta." | CT Art. 322 + fn.29: the ordinary day shift may not exceed 8 hours daily and 44 weekly, EQUIVALENT TO 48 OF SALARY (44 worked hours paid as 48 — R-H61); the ordinary night shift may not exceed 6 hours daily and 36 weekly; a worker who misses a day and does not complete the 44-hour week is entitled only to salary proportional to time worked, computed on the base of the 48-hour weekly salary. fn.29: the salary corresponding to 48 weekly day-shift hours equals the salary of the 36-hour night shift and the 42-hour mixed shift (weekly-salary equality across types). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 322 (p.94) + fn.29 (p.95) (EV85:EVID-310) |
| LB-003 | CT Art. 325 (exclusions): "a) Los que desempeñen cargos de dirección, de confianza o de manejo; b) Los del servicio doméstico…; c) Los que ejecuten actividades discontinuas o intermitentes…; d) Los chóferes particulares…; e) Los que realizan labores que por su propia naturaleza no están sujetas a jornadas…tales como las labores agrícolas, ganaderas y afines; y, f) Los trabajadores remunerados a base de comisión…Sin embargo, tales personas no estarán obligadas a permanecer más de doce (12) horas diarias…y tendrán derecho dentro de la jornada a un descanso mínimo de hora y media (1-1/2)…" (fn.30, interp. D.21-1963 — evidence gloss: watchmen *celadores/serenos/wachimanes* are NOT dirección/confianza roles; fn.30 tail truncated in the evidence print) | CT Art. 325 — excluded from the jornada caps: (a) direction, trust or handling positions; (b) domestic service; (c) discontinuous/intermittent activities; (d) private drivers; (e) work not subject to shifts by its own nature (agricultural, livestock and similar); (f) commission-paid workers; however such persons may not be obliged to remain more than 12 hours daily and are entitled to a minimum 1.5-hour rest within the shift. fn.30: night watchmen are not "trust" roles by title alone (guard against misclassification). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 325 (pp.95-96) + fn.30 (EV85:EVID-310) |
| LB-004 | CT Art. 320: "Trabajo suplementario o de horas extras es el que excede de la jornada ordinaria, y en todo caso el que exceda de la máxima legal." + CT Art. 329: "El trabajo nocturno, por el solo hecho de ser nocturno, se remunera con un recargo del veinticinco por ciento (25%) sobre el valor del trabajo diurno. Con el mismo recargo se pagarán las horas trabajadas durante el período nocturno en la jornada mixta." | CT Art. 320: supplementary work or overtime is work exceeding the ordinary shift and, in any case, exceeding the legal maximum. CT Art. 329: night work, by the sole fact of being night work, is remunerated with a 25% surcharge over the value of day work; hours worked during the night period of a mixed shift are paid with the same surcharge. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Arts. 320 (p.94) y 329 (p.96) (EV85:EVID-311) |
| LB-005 | CT Art. 330: "…constituye jornada extraordinaria, y debe ser remunerada, así: 1. Con un veinticinco por ciento (25%) de recargo sobre el salario de la jornada diurna cuando se efectúe en el período diurno; 2. Con un cincuenta por ciento (50%) de recargo sobre el salario de la jornada diurna cuando se efectúe en el período nocturno; y, 3. Con un setenta y cinco por ciento (75%) de recargo sobre el salario nocturna cuando la jornada extraordinaria sea prolongación de aquélla." | CT Art. 330 — the overtime multipliers: (1) +25% over the day-shift salary when performed in the day period; (2) +50% over the day-shift salary when performed in the night period; (3) +75% over the NIGHT salary when the overtime is a prolongation of the night shift (the ×1.75 tier is prolongation of nocturnal work on the night-salary base — not a generic third tier). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 330 (pp.96-97) (EV85:EVID-311) |
| LB-006 | CT Arts. 331-333, 335 y 337: Art. 331: "No serán remuneradas las horas extraordinarias cuando el trabajador las ocupe en subsanar los errores imputables sólo a él…". Art. 332: "La jornada extraordinaria, sumada a la ordinaria, no podrá exceder de doce (12) horas, salvo…siniestro…riesgo inminente…". Art. 333: "…Queda también prohibido al patrono permitir la jornada extraordinaria de un mismo trabajador durante más de cuatro (4) veces a la semana…". Art. 335: "Los patronos estarán obligados a consignar en sus libros de salarios o planillas, debidamente separados de lo que se refiere a trabajo ordinario, lo que a cada uno de sus trabajadores paguen por concepto de trabajo extraordinario." Art. 337: "Evitará también el patrono cambiar los turnos en forma que produzca alteración en las horas destinadas por los trabajadores al descanso y a las comidas." | CT Arts. 331-333/335/337: overtime hours used by the worker solely to correct his own errors are not remunerated as OT; ordinary + overtime may not exceed 12 hours daily (except accident/imminent-risk cases); the employer may not allow a worker's overtime more than 4 times per week; employers must record in their salary books or planillas, duly SEPARATED from ordinary-work pay, whatever they pay each worker for extraordinary work (statutory payslip/register line separation); shift changes must avoid altering rest and meal hours. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Arts. 331-333 (p.97), 335 (p.97), 337 (p.98) (EV85:EVID-311) |
| LB-007 | CT Art. 338: "El trabajador gozará de un (1) día de descanso, preferentemente el domingo, por cada seis (6) de trabajo…En todo caso deberá quedar asegurado para el trabajador el descanso semanal. Ninguna excepción respecto a la obligación del descanso dominical será aplicable a los menores de dieciséis (16) años." | CT Art. 338: the worker enjoys one rest day, preferably Sunday, for every six days of work; in any case the weekly rest must remain assured for the worker; no exception to the Sunday-rest obligation applies to workers under 16 years of age. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 338 (p.98) (EV85:EVID-312) |
| LB-008 | CT Art. 339 + fn.31 (reformed D.275-1960 + interp. D.116-1960): "Los patronos pagarán los siguientes días feriados o de fiesta nacional: 1º de enero, 14 de abril, 1º. de mayo, 15 de septiembre, 3 de octubre, 12 de octubre, 21 de octubre y 25 de diciembre, aunque caigan en domingo; el jueves, viernes y sábado de la Semana Santa. Cuando coincidan dos (2) feriados en un mismo día, se entenderá cumplida la obligación pagando el patrono a sus trabajadores un (1) día feriado o de fiesta nacional…Cuando por motivo de cualquier fiesta no determinada en el párrafo anterior el patrono suspendiere el trabajo, está obligado a pagar el salario de ese día como si se hubiere realizado. El pago de los días feriados o de fiesta nacional, cuando no se trabajen, deben hacerse con el promedio diario de salarios ordinarios y extraordinarios que haya devengado el trabajador durante la semana inmediata anterior al día feriado o de fiesta nacional de que se trate. Si éste no hubiere trabajado durante la semana inmediata anterior se tomará como base el salario correspondiente a una jornada normal de trabajo. Es entendido que cuando el salario se estipule por quincena o por mes, incluye en forma implícita el pago de los días feriados o de fiesta nacional que no se trabajen." fn.31 (interp. ¶3): "El promedio diario de salarios ordinarios y extraordinarios…se obtendrá, dividiendo entre (6) seis el total de salarios ordinarios y extraordinarios devengados en dicha semana anterior, cuando se hubiere trabajador completa, y en caso de que no se hubiere trabajador completa, se dividirá la suma de salarios ordinarios y extraordinarios devengados por el trabajador en dicha semana inmediata anterior entre el número de dí…" (fn.31 tail truncated in the evidence print; gloss: divisor = days actually worked) | CT Art. 339 + fn.31 — the paid-holiday block: employers pay 10 holidays — Jan 1, Apr 14, May 1, Sep 15, Oct 3, Oct 12, Oct 21, Dec 25 (paid EVEN when falling on Sunday), plus Holy Thursday, Good Friday and Holy Saturday; when two holidays coincide on the same day the obligation is discharged by paying ONE holiday; when the employer suspends work for any UNLISTED fiesta the day is paid as if worked; non-worked holiday pay = daily average of ordinary AND extraordinary salaries earned in the week immediately before the holiday; if the worker did not work that prior week, the base is the salary of one normal working day; salaries stipulated by fortnight or month IMPLICITLY include non-worked holidays. fn.31: the average = prior-week total ÷ 6 when the week was fully worked; when partial, ÷ the number of days actually worked. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 339 (pp.98-99) + fn.31 (EV85:EVID-312) |
| LB-009 | CT Art. 340: "Si en virtud de convenio se trabajare durante los días de descanso o los días feriados o de fiesta nacional, se pagarán con el duplo de salario correspondiente a la jornada ordinaria en proporción al tiempo trabajado, sin perjuicio del derecho del trabajador a cualquier otro día de descanso en la semana conforme al artículo 338." | CT Art. 340: when by agreement work is performed on rest days or holidays, it is paid at DOUBLE the salary corresponding to the ordinary shift, proportional to the time worked, without prejudice to the worker's right to another day of rest in the week per Art. 338 (the substitute-rest right). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 340 (p.99) (EV85:EVID-313) |
| LB-010 | CT Art. 283 (ferrocarrilero chapter): "Las empresas no podrán ocupar habitualmente a sus trabajadores en su día de descanso semanal, pero podrán hacerlo por vía de excepción pagando el duplo del salario correspondiente en proporción a las horas trabajadas. Las empresas no estarán obligadas al pago de doble salario si convienen con el trabajador en que éste goce de un descanso substitutivo en la misma semana o de un (1) día más de vacaciones anuales por cada día de descanso trabajado, como acumulación de descansos no gozado, siempre que tal acuerdo conste por escrito, en cada caso. Las empresas no podrán utilizar a sus trabajadores en su día de descanso más de doce (12) veces en cada año ni aún bajo las formas precedentemente establecidas." | CT Art. 283 (railway regime): companies may not habitually use workers on their weekly rest day, but may do so by way of exception paying double salary proportional to hours worked; companies are not obliged to double pay if they agree IN WRITING, in each case, that the worker enjoy a substitute rest in the same week OR one additional annual vacation day per worked rest day (accumulation of unenjoyed rest); workers may not be used on their rest day more than 12 times per year under any of the foregoing forms. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 283 (p.87) (EV85:EVID-313) |
| LB-011 | CT Art. 867 (final ¶): "El término de prescripción para el cobro de jornadas extraordinarias de trabajo empezará a contarse el día en que fue pagado o debió pagarse el salario ordinario correspondiente al período en que hubiere sido laborado del trabajo extraordinario." | CT Art. 867 (final paragraph): the prescription period for claiming overtime payment begins on the day the ordinary salary corresponding to the period in which the overtime was worked was paid — or fell due (per-period payment-date anchor). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 867 (p.268, final ¶) (EV85:EVID-326) |
| LB-012 | CT Art. 361: "Constituye salario no sólo la remuneración fija u ordinaria, sino todo lo que recibe el trabajador en dinero o en especie y que implique retribución de servicios, sea cualquiera la forma o denominación que se adopte, como las primas, sobresueldos, bonificaciones habituales, valor del trabajo suplementario o de las horas extras, valor del trabajo en días de descanso obligatorio, porcentaje sobre ventas, comisiones o participación de utilidades." | CT Art. 361: salary comprises not only the fixed or ordinary remuneration but everything the worker receives in money or in kind implying retribution of services — including premiums, habitual bonuses, the value of supplementary work or overtime, the value of work on mandatory rest days, sales percentages, commissions or profit participation (OT and rest-day pay ARE salario). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 361 (pp.104-105) (EV85:EVID-317) |
| LB-013 | D. 93-2021 (85_), Art. 1 (guard, R-H57): "Derogar los artículos 102, 103, 104, 105, 106, 176, 182, 225, 263, 275, 309, 317, 337, 346, 368, 397, 403, 411, 417, 430, 434, 437, 444, 469, 511, 569 y 596; todos del Decreto No.130-2017…que contiene el CÓDIGO PENAL…" — cross-check table verdict: "0 CT articles derogated by D.93-2021. No target family (jornada 318-337, vacaciones 345-356, salario 360-390, preaviso/cesantía 116-123, terminación 111-126, maternidad 135-146) is affected." | D. 93-2021 (G 35,760) derogates 31 articles of the PENAL Code D. 130-2017 (plus CPP and Lavado reforms) — ZERO Código del Trabajo articles. The derogated penal numbers collide numerically with live CT articles of this file (CT-337 turnos, CT-346 vacaciones, CT-368 pay periods): they are NOT those articles. No D. 93-2021-derived never-implement flag applies to Arts. 318-341/283/339/867 (R-H57 guard, cited once). | `hn/sources/85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf` | 93-Art. 1 (p.A.2) + cross-check table (EV85:EVID-329/333) |

## 3. Functional Requirements

### 3.1 Jornada ordinaria frame: types, boundaries, caps, exclusions

- **HN-PAYR-FR-221:** The system shall model the three statutory jornada
  types on the labor contract as configuration — *jornada diurna* (day
  working day, work executed 05:00-19:00), *jornada nocturna* (night working
  day, 19:00-05:00) and *jornada mixta* (mixed, comprising both periods) —
  with the statutory clock boundaries used as the classification axis for
  every worked hour (day period vs night period), and with the mixed type
  capped at 7 hours daily and 42 weekly. (LB-001; EV85:EVID-310)
- **HN-PAYR-FR-222:** The system shall auto-reclassify a mixed shift as
  *jornada nocturna* whenever its night period covers 3 or more hours
  ("pues en caso contrario, se reputará como jornada nocturna" — the ≥3
  night-hours flip), applying the nocturna caps (6h/36h) from that
  classification. (LB-001; EV85:EVID-310)
- **HN-PAYR-FR-223:** The system shall implement the diurna 44-worked/48-
  PAID rule (R-H61): the ordinary day shift is capped at 8 hours daily and
  44 hours weekly WORKED, "equivalentes a cuarenta y ocho (48) de salario" —
  a full-week diurna worker's weekly salary covers 44 worked hours at the
  ordinary rate plus 4 paid unworked hours; the payslip engine shall pay the
  full weekly salary for a completed 44-hour week with NO overtime arising
  from the 4-hour gap (48-paid ≠ 48-worked). (LB-002; EV85:EVID-310; R-H61)
- **HN-PAYR-FR-224:** The system shall enforce the fn.29 weekly-salary
  equality as schedule-conversion validation: the salary corresponding to 48
  weekly diurna hours EQUALS the salary of the 36-hour nocturna week and the
  42-hour mixta week — converting a worker between jornada types shall not
  reduce the ordinary weekly salary (both rules encoded as printed; their
  per-hour reconciliation with the Art. 329 +25% recargo is carried as
  OQ-004, never derived). (LB-002; LB-004; EV85:EVID-310/311)
- **HN-PAYR-FR-225:** The system shall compute absence proration on the
  48-hour base: a worker who misses one or more days and does not complete
  the 44-hour work week is entitled only to salary proportional to the time
  worked, computed on the 48-hour weekly salary base (Art. 322 ¶2); workers
  whose AGREED week is shorter (monthly/quincenal salaried permanent
  workers) still receive the full salary — Art. 328's full-pay floor per
  EVID-310 gloss. (LB-002; EV85:EVID-310)
- **HN-PAYR-FR-226:** The system shall carry the Art. 325 excluded-roles
  catalog as a contract flag (dirección/confianza/manejo; domestic service;
  discontinuous/intermittent activities; private drivers; work not subject
  to shifts by nature — agricultural/livestock and similar;
  commission-paid) that disapplies the jornada caps BUT enforces the
  12-hour daily presence ceiling and the minimum 1.5-hour in-shift rest for
  such roles; and shall apply the fn.30 guard that watchmen
  (*celadores/serenos/wachimanes*, vigilantes) are NOT dirección/confianza
  roles by title alone — no automatic exclusion from jornada protection
  based on the role name. (LB-003; EV85:EVID-310)

### 3.2 Surcharges: night +25% and the overtime engine

- **HN-PAYR-FR-227:** The system shall apply the night-work surcharge of
  25% over the value of day work ("por el solo hecho de ser nocturno") to
  night-period hours, including the night-period hours of a mixed shift
  ("Con el mismo recargo se pagarán las horas trabajadas durante el período
  nocturno en la jornada mixta"), as a distinct earning class from overtime
  multipliers. (LB-004; EV85:EVID-311)
- **HN-PAYR-FR-228:** The system shall classify overtime under BOTH
  statutory tests of Art. 320 — work exceeding the ordinary jornada AND, in
  any case, work exceeding the legal maximum (8/44 diurna, 6/36 nocturna,
  7/42 mixta) — so that hours beyond the legal max are overtime even if
  within an agreed longer shift; each OT hour shall be classified by clock
  boundary (day period / night period) and by shift origin (prolongation of
  a night shift or not) to select its multiplier. (LB-004; LB-001;
  EV85:EVID-311/310)
- **HN-PAYR-FR-229:** The system shall implement the Art. 330 overtime
  multiplier matrix exactly as printed: (1) +25% over the day-shift salary
  when the overtime is performed in the day period; (2) +50% over the
  day-shift salary when performed in the night period; (3) +75% over the
  NIGHT salary ("sobre el salario nocturna") when the overtime is a
  PROLONGATION of the night shift — the ×1.75 tier exists only as
  prolongation-of-nocturnal-work on the night-salary base, never as a
  generic third tier. (LB-005; EV85:EVID-311)
- **HN-PAYR-FR-230:** The system shall enforce the 12-hour daily ceiling on
  ordinary + overtime combined ("La jornada extraordinaria, sumada a la
  ordinaria, no podrá exceder de doce (12) horas"), blocking or flagging any
  day whose combined hours exceed 12, with the statutory exceptions
  (*siniestro*, accident; *riesgo inminente*, imminent risk) recordable only
  as explicit flagged exception rows. (LB-006; EV85:EVID-311)
- **HN-PAYR-FR-231:** The system shall enforce the weekly overtime
  frequency guard: overtime of the same worker may not be permitted more
  than 4 times per week — a 5th OT occurrence in one week is blocked or
  flagged as a statutory violation. (LB-006; EV85:EVID-311)
- **HN-PAYR-FR-232:** The system shall exclude from overtime remuneration
  the hours a worker uses solely to correct his own errors ("subsanar los
  errores imputables sólo a él") — such hours are recorded but not paid as
  OT. (LB-006; EV85:EVID-311)
- **HN-PAYR-FR-233:** The system shall book overtime SEPARATELY from
  ordinary pay in all payroll output — payslip lines and the Libro de
  Salarios/planilla registers ("debidamente separados de lo que se refiere a
  trabajo ordinario", Art. 335) — as a statutory line-separation duty; the
  register/report formats themselves are owned by file 10
  (`10_salario-concepts-records.md`, HN-PAYR-FR-371..405), consumed by range; shift
  changes shall additionally respect rest/meal-hour alignment (Art. 337,
  informational scheduling constraint). (LB-006; EV85:EVID-311)

### 3.3 Séptimo día (weekly rest)

- **HN-PAYR-FR-234:** The system shall accrue the *séptimo día* (7th-day
  weekly rest) as one rest day per six days worked, preferably Sunday, with
  the weekly-rest guarantee enforced in every scheduling week; and shall
  apply the minors rule that NO exception to the Sunday-rest obligation is
  available for workers under 16 years of age. (LB-007; EV85:EVID-312)
- **HN-PAYR-FR-235:** The system shall value the séptimo día as follows:
  for a full-week diurna worker it is embedded in the 44-worked/48-paid
  equivalence (no separate earning line — FR-223); accrual counts only days
  actually worked (1 per 6); and for day-rated workers and partial weeks the
  valuation uses the fn.31 prior-week average routine of FR-239 (total
  ordinary + extraordinary earnings of the immediately prior week ÷ 6 when
  fully worked, ÷ days actually worked when partial — the routine the
  evidence gloss applies to the weekly-rest valuation; no separate statutory
  sentence exists, wording anchored to fn.31). (LB-002; LB-008;
  EV85:EVID-310/312)

### 3.4 Feriados (paid national holidays)

- **HN-PAYR-FR-236:** The system shall load the 11 paid holidays as DATED
  configuration rows (D-H2 additive-only, never replaced in place): eight
  fixed-date holidays — 1-jan, 14-apr, 1-may, 15-sep, 3-oct, 12-oct, 21-oct,
  25-dec — plus Holy Thursday, Good Friday and Holy Saturday (*jueves,
  viernes y sábado de la Semana Santa*) as Easter-relative rows (offsets
  −3/−2/−1 days from Easter Sunday); `valid_from` = the D. 275-1960 reform
  (fn.31), `valid_to` open-ended; the list is 1960-vintage text with the
  `86_ OQ-9` spot-check flag carried (OQ-002 — no post-2013 change found
  in-print); resolution is by payslip period, and corrections recompute with
  ORIGINAL-period calendar rows (D-H2). (LB-008; EV85:EVID-312)
- **HN-PAYR-FR-237:** The system shall pay the eight fixed-date holidays
  EVEN when they fall on Sunday ("aunque caigan en domingo") — a
  Sunday-colliding fixed holiday loses nothing; the statutory COLLAPSE rule
  is holiday-on-holiday (FR-238), not holiday-on-Sunday, encoded exactly as
  EVID-312 states. (LB-008; EV85:EVID-312)
- **HN-PAYR-FR-238:** The system shall apply the collision collapse: when
  two holidays coincide on the same calendar day, the obligation is
  discharged by paying ONE holiday day ("se entenderá cumplida la obligación
  pagando el patrono a sus trabajadores un (1) día feriado o de fiesta
  nacional") — one paid day, not two (e.g. 14-apr falling on Holy Thursday).
  (LB-008; EV85:EVID-312)
- **HN-PAYR-FR-239:** The system shall compute non-worked holiday pay as
  the daily average of ORDINARY AND EXTRAORDINARY salaries earned in the
  week immediately before the holiday: ÷ 6 when that prior week was fully
  worked; ÷ the number of days actually worked when partial (fn.31,
  D. 116-1960 — divisor per evidence gloss, OQ-003); and when the worker did
  not work the immediately prior week, the base is the salary of one normal
  working day ("jornada normal de trabajo"). (LB-008; EV85:EVID-312)
- **HN-PAYR-FR-240:** The system shall treat quincenal and monthly
  salaries as IMPLICITLY including non-worked holidays ("incluye en forma
  implícita el pago de los días feriados o de fiesta nacional que no se
  trabajen") — no additional holiday earning line and no duplicate accrual
  for such workers beyond the monthly/quincenal salary. (LB-008;
  EV85:EVID-312)
- **HN-PAYR-FR-241:** The system shall pay as worked any day the employer
  suspends work on account of a fiesta NOT determined in the holiday list
  ("cualquier fiesta no determinada en el párrafo anterior") — an
  employer-suspended unlisted-fiesta day is paid at the normal salary, as an
  employer-decision event distinct from the 11 statutory holidays.
  (LB-008; EV85:EVID-312)

### 3.5 Work on rest days and holidays

- **HN-PAYR-FR-242:** The system shall pay work performed on rest days or
  holidays (by agreement, "en virtud de convenio") at DOUBLE the ordinary-
  shift salary, proportional to the time worked ("el duplo de salario
  correspondiente a la jornada ordinaria en proporción al tiempo
  trabajado"), and shall record the worker's substitute-rest right — another
  day of rest in the week per Art. 338 — as a compensatory-rest accrual.
  (LB-009; LB-007; EV85:EVID-313/312)
- **HN-PAYR-FR-243:** The system shall implement the railway-variant rest-
  day regime (Art. 283, applicable to railway and analogous continuous
  regimes): rest-day work is exceptional, never habitual; per worked rest
  day the employer elects — by WRITTEN per-case agreement — either the ×2
  payment, or a substitute rest within the same week, or ONE additional
  annual vacation day per worked rest day (accumulation of unenjoyed rest,
  forwarded to the vacaciones engine of file 07, HN-PAYR-FR-261..280, by
  range); and the use of a worker on rest days may never exceed 12 times per
  year under ANY of the three forms. (LB-010; EV85:EVID-313)

### 3.6 Timing anchor and consumption interfaces

- **HN-PAYR-FR-244:** The system shall stamp every surcharge row with the
  per-period prescription anchor of Art. 867: the prescription term for
  claiming overtime starts on the day the ORDINARY salary of the period
  covering that overtime was paid — or fell due — so each payslip's OT rows
  carry the covering period's ordinary-salary payment/due date as their
  timing anchor (D-H2 kin: prescription ties to per-period payment dates,
  never to "today"). (LB-011; EV85:EVID-326)
- **HN-PAYR-FR-245:** The system shall classify every surcharge earning of
  this file — night +25%, the three OT multipliers, and rest-day/holiday
  work pay — as *salario* per CT Art. 361 ("valor del trabajo suplementario
  o de las horas extras, valor del trabajo en días de descanso obligatorio"
  are salary), feeding the salary-concept families and the *salario
  completo* (ordinary + extraordinary) indemnity bases owned by file 10
  (`10_salario-concepts-records.md`, HN-PAYR-FR-371..405) and the benefit averages
  of files 07/08 by range — classification only, no re-derivation of those
  bases here. (LB-012; EV85:EVID-317)
- **HN-PAYR-FR-246:** The system shall expose the OT and surcharge amounts
  of this file to the ISR plantilla engines of taxation/04 strictly by id —
  they enter the annual gross at HN-TAX-FR-126 (bonuses/overtime line) — and
  shall never restate, pre-cap or recompute any plantilla mechanics (caps,
  promedio, prorate) in this file. (LB-012; LB-006; EV85:EVID-317/311)
- **HN-PAYR-FR-247:** The system shall maintain per-contract WEEKLY
  aggregates as the computation surface for this file (D-H3 discipline,
  no payslip-level import): days worked, ordinary hours by period class,
  OT hours by multiplier class, ordinary and extraordinary earnings, OT
  occurrences, and rest-day uses — the inputs for the fn.31 ÷6/÷-days
  averages (FR-239/235), the 1-per-6 séptimo día accrual (FR-234), the
  12h/4×/12×-per-year guards (FR-230/231/243) and the weekly-rest
  guarantee. (LB-006; LB-007; LB-008; EV85:EVID-311/312)

## 4. Data Model

No machine-readable CSV sidecar is allocated to this file (the feriado
calendar is small, self-describing and seeded as dated config rows; the
sibling sidecars of files 01/02 own tabular parameter feeds). Layer
semantics: Odoo-side computation/bookkeeping data only (wave default
`odoo`; see §5).

**Jornada and surcharge engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | l10n_hn_jornada_type | select | diurna · nocturna · mixta (auto-flip to nocturna at ≥3 night hours) | FR-221, FR-222 |
| hr.contract | l10n_hn_excluded_role | select (nullable) | art325_direccion_confianza_manejo · art325_domestico · art325_discontinuo · art325_chufer_particular · art325_naturaleza_no_sujeta · art325_comisionista; drives 12h presence cap + 1.5h rest; fn.30 watchmen guard = no auto-set | FR-226 |
| hr.contract | l10n_hn_restday_regime | select | general (Art. 340) · railway_style (Art. 283 election) | FR-242, FR-243 |
| resource.calendar / hr.work.entry | hours by period class | computed | day_period (05:00-19:00) / night_period (19:00-05:00) per worked hour | FR-221, FR-227, FR-228 |
| hr.work.entry.type (catalog) | surcharge classes | code list | NIGHT_25 · OT_DAY_125 · OT_NIGHT_150 · OT_NIGHTPROL_175 · RESTDAY_FERIADO_200 · SEPTIMO_DIA · FERIADO_AVG · FIESTA_SUSPENSION | FR-227..FR-239, FR-241 |
| hr.payslip.line | separation flag, prescription anchor | boolean/date | OT lines in a category SEPARATE from ordinary pay (Art. 335); ot_prescription_anchor = covering period's ordinary-salary paid/due date | FR-233, FR-244 |
| l10n_hn.payroll.workweek (new) | contract, week, days_worked, hours_ordinary_day, hours_ordinary_night, hours_ot_day/night/prolong, salary_ordinary, salary_extraordinary, ot_occurrences, restday_uses | m2o/integer/monetary | weekly aggregation surface (D-H3: from monthly aggregates, no payslip-level import) | FR-247 |
| l10n_hn.payroll.guard (new) | contract, date, type, exception_ref | select/char | daily_12h_excess (exception: siniestro/riesgo_inminente only) · ot_5th_week · restday_13th_year | FR-230, FR-231, FR-243 |

**Feriado calendar and compensatory rest:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.payroll.feriado (new) | name, kind, month, day, easter_offset, valid_from, valid_to | char/select/int/date | kind: fixed (8 rows) · easter_relative (offsets −3/−2/−1 = Jueves/Viernes/Sábado Santo); valid_from = D. 275-1960 reform, valid_to open; additive-only (D-H2); carries the OQ-002 spot-check flag as metadata | FR-236 |
| l10n_hn.payroll.feriado.run (computed) | date, payable_holidays, collapsed | date/int/boolean | materialized calendar per year; collision → payable_holidays = 1 | FR-237, FR-238 |
| l10n_hn.payroll.rest.compensation (new) | contract, origin_date, type, written_election_ref, consumed | m2o/date/select/char/boolean | origin: rest_day · feriado; type: substitute_in_week · plus_vacation_day (railway Art. 283 only; written per-case ref mandatory); consumed → file 07 vacaciones feed | FR-242, FR-243 |

## 5. Odoo Mapping

Layer semantics for this file: `odoo` = computation/bookkeeping logic living
in the LGPL client. No SaaS rows are introduced: none of these FRs touch the
thin-client/SaaS architecture split (no DTE/e-invoicing surface exists for
working-time records in the corpus). Model names stable across Odoo
17/18/19/20; `hr.work.entry`/`hr.work.entry.type` available in all four
(since Odoo 15); version-specific behavior recorded per row where a dated
legal parameter exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-221..FR-224 | odoo | hr.contract + resource.calendar + hr.work.entry | jornada type, calendar boundaries | Boundary classification per worked entry (attendance); mixta flip computed on shift composition; no 17-20 differences |
| FR-223, FR-225 | odoo | hr.payslip (worked-hours rules) + resource.calendar | 44/48 equivalence, absence proration | R-H61: proration base = 48-hour weekly salary; Art. 328 full-pay floor for shorter agreed weeks (monthly/quincenal); D15: resolved values snapshotted on the slip |
| FR-226 | odoo | hr.contract (excluded-role select) + hr.attendance validation | 12h presence, 1.5h rest | fn.30 guard: no inference from job title (watchmen); validation warns rather than hard-blocks (role data quality) |
| FR-227..FR-229 | odoo | hr.work.entry.type + hr.salary.rule | NIGHT_25 / OT_DAY_125 / OT_NIGHT_150 / OT_NIGHTPROL_175 | ×1.75 base = night salary (Art. 330.3 verbatim); multipliers are statutory constants (not dated parameters — no vintage rows); D15: classification snapshot on slip lines |
| FR-230, FR-231 | odoo | hr.attendance + l10n_hn.payroll.guard | 12h/day, 4×/week guards | Exceptions only siniestro/riesgo inminente, explicit flagged rows; guard visible in payroll run review |
| FR-232 | odoo | hr.work.entry (error-recovery flag) | unpaid-OT marker | Recorded not paid; audit trail only |
| FR-233 | odoo | hr.payslip.line category + hr.salary.rule categories | OT line separation | Art. 335 statutory separation; register formats owned by file 10 (by range); Art. 337 informational note on shift-change validation |
| FR-234, FR-235 | odoo | hr.work.entry (rest entries) + hr.salary.rule SEPTIMO_DIA | 1-per-6 accrual | Embedded valuation for full-week diurna (FR-223); fn.31 routine for day-rated/partial — consumes FR-247 aggregates |
| FR-236..FR-238 | odoo | l10n_hn.payroll.feriado (new) + resource.calendar.leaves | dated holiday rows | D12 version regime: rows valid from D. 275-1960 reform (fn.31), open-ended; additive-only (D-H2); Easter-relative computed rows (offsets −3/−2/−1); OQ-002 spot-check flag as row metadata; D16: retro payroll resolves the ORIGINAL-period calendar |
| FR-239 | odoo | hr.salary.rule FERIADO_AVG + l10n_hn.payroll.workweek | ÷6 / ÷-worked-days average | Fallback = one normal jornada salary; divisor variant per fn.31 gloss (OQ-003) |
| FR-240 | odoo | hr.contract wage period flag | implicit inclusion | No extra line for monthly/quincenal workers; prevents duplicate accrual |
| FR-241 | odoo | hr.work.entry type FIESTA_SUSPENSION | paid-as-worked | Employer-decision event, distinct from statutory holidays |
| FR-242, FR-243 | odoo | hr.salary.rule RESTDAY_FERIADO_200 + l10n_hn.payroll.rest.compensation + hr.leave | ×2 pay, compensatory rest | Railway election requires written_election_ref per case; ≤12×/year counter on workweek aggregates; +1 vacation day feed consumed by file 07 (by range) |
| FR-244 | odoo | hr.payslip.line (ot_prescription_anchor) + hr.payslip date fields | anchor stamp | Art. 867: anchor = covering period's ordinary-salary paid/due date; per-period rows (D-H2) |
| FR-245 | odoo | hr.salary.rule categories → salary concept families | salario classification | Art. 361: OT + rest-day pay = salario; consumo by file 10 (371..405) and files 07/08 averages, by range |
| FR-246 | odoo | payslip output feed ( earning tags) | ISR interface | taxation/04 HN-TAX-FR-126 consumes by id; never restate plantilla mechanics |
| FR-247 | odoo | l10n_hn.payroll.workweek (new) | weekly aggregates | D-H3: built from monthly aggregates per contract (no payslip-level import); feeds FR-230/231/234/239/243 |

Version-regime notes (D12): FR-236 records the feriado-calendar provenance
(D. 275-1960 reform per fn.31; 1960-vintage list) with additive-only dated
rows — no adaptation windows exist in the instrument. FR-244's anchor is a
computation rule, not a dated parameter. No D18/D19 go-live surfaces arise
in this file (working-time config, not GL-bearing declarations); historical
ingestion follows the D-H3 aggregate contract of FR-247 (tiered monthly
aggregates per contract from hire date).

## 6. Acceptance Criteria

- **AC-001:** Given a diurna worker with agreed weekly salary L4,800.00
  (48 salary-hours × L100.00 ordinary hourly), when the worker completes the
  full 44-hour work week, then the payslip pays L4,800.00 with no overtime
  line — the 4 unworked hours are ordinary-paid inside the 44/48 equivalence
  (FR-223).
- **AC-002:** Given the same worker misses one full 8-hour day (36 hours
  worked), then the proportional salary = 36 × L100.00 = L3,600.00, computed
  on the 48-hour weekly salary base — never 36/44 of the weekly salary
  (FR-225).
- **AC-003:** Given a shift 15:00-21:00 (2 night hours), it remains
  *jornada mixta* (7h/42h caps); given a shift 15:00-23:00 (4 night hours ≥
  3), it is reclassified *jornada nocturna* (6h/36h caps); in both cases the
  ordinary weekly salary is unchanged (fn.29 equality) (FR-221, FR-222,
  FR-224).
- **AC-004:** Given a night-period ordinary hour whose diurno value is
  L100.00, then the hour pays L125.00 (+25%); the same recargo applies to
  the night-period hours of a mixed shift (FR-227).
- **AC-005:** Given a diurno hourly salary of L100.00 (night salary =
  L125.00 per Art. 329), then one OT hour pays: L125.00 in the day period
  (×1.25); L150.00 in the night period (×1.50); and L218.75 when the OT
  prolongs a night shift (×1.75 × night salary 125.00 — the third tier
  exists only as night-shift prolongation) (FR-229).
- **AC-006:** Given a day with 8 ordinary hours and 5 requested OT hours
  (13 combined), then the entry is blocked/flagged (12-hour cap); given 8+4
  = 12, it is allowed; and a 13-hour day under a recorded siniestro
  exception is allowed only with the explicit exception row (FR-230).
- **AC-007:** Given a worker with OT on 4 days of one week, then a 5th OT
  occurrence that week is flagged as prohibited ("más de cuatro (4) veces a
  la semana") (FR-231).
- **AC-008:** Given a payslip containing ordinary salary and OT, then the
  OT amount appears in earning lines of a category separate from ordinary
  pay (Art. 335), and the OT rows carry ot_prescription_anchor = the
  covering period's ordinary-salary paid/due date (FR-233, FR-244).
- **AC-009:** Given a fully-worked prior week (6 days) with ordinary
  L4,800.00 + OT L600.00 = L5,400.00, then the non-worked-holiday /
  séptimo-día average = 5,400 ÷ 6 = L900.00; given a partial prior week (4
  days worked, ordinary + OT = L3,600.00), then the average = 3,600 ÷ 4 =
  L900.00; given no prior-week work, then the base = one normal jornada
  salary (FR-239, FR-235).
- **AC-010:** Given 14-apr falling on Holy Thursday (as in 2022), then the
  collision collapses to ONE paid holiday day — not two (FR-238); and given
  25-dec falling on Sunday, then the fixed holiday is paid all the same
  ("aunque caigan en domingo") (FR-237).
- **AC-011:** Given a monthly-salaried worker and a non-worked statutory
  holiday, then no extra holiday line is added — the monthly salary already
  includes it implicitly (FR-240); given the employer suspends work on an
  unlisted fiesta day, then that day is paid as if worked (FR-241).
- **AC-012:** Given 6 hours of work on the Sunday rest day at an ordinary
  hourly rate of L100.00, then the rest-day pay = 6 × 100 × 2 = L1,200.00,
  and a substitute-rest accrual is recorded for the week (FR-242).
- **AC-013:** Given a railway-style worker with 12 rest-day uses in the
  year, each with a written per-case election (duplo, or in-week substitute
  rest, or +1 vacation day forwarded to file 07), then a 13th use is blocked
  ("no… más de doce (12) veces en cada año") (FR-243).
- **AC-014:** Given OT worked in the May-2026 period whose ordinary salary
  was paid 2026-05-29, then the OT rows' prescription anchor = 2026-05-29 —
  never the payslip run date nor "today" (FR-244).
- **AC-015:** Given a vigilante (watchman) scheduled 13 hours of presence,
  then the schedule is flagged against the 12-hour presence cap; and given
  the role title alone, the system does NOT set the Art. 325
  dirección/confianza exclusion (fn.30 guard) (FR-226).
- **AC-016:** Given OT and rest-day pay lines of L2,400.00 in a fiscal
  year, then they are tagged salario (Art. 361) and flow into the ISR
  plantilla annual gross at HN-TAX-FR-126 by id, with no cap, promedio or
  prorate logic restated in this file (FR-245, FR-246).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `EV85:86_ OQ-1` carried — file-level consolidation vintage: the 86_ CEDIJ print integrates instruments only through D. 278-2013 (fn.36), so any 2014-2026 reform of the jornada family (Arts. 318-341, 283, 339, 861-867) would be silently missing. FRs are drafted from the evidenced text with additive-only config able to absorb reforms; verify against an official current consolidation before approval. | no | Takumi S-HN4 + controller | open |
| OQ-002 | `EV85:86_ OQ-9` carried — feriado-list currency: Art. 339's 10-holiday list is 1960-vintage text (D. 275-1960 per fn.31); no post-2013 in-print amendment was found, but the spot-check for any post-2013 holiday change (additions/replacements) must complete before the seeded calendar rows are treated as exhaustive beyond their valid_from window (FR-236 carries the flag as row metadata). | no | Takumi S-HN4 + controller | open |
| OQ-003 | fn.31 (D. 116-1960 interp. ¶3) partial-week divisor: the evidence verbatim truncates mid-sentence ("…entre el número de dí…"); the evidence gloss resolves the divisor as the number of days ACTUALLY worked (FR-239/AC-009 implement the gloss). Confirm the full fn.31 text against the print before freezing the routine. | no | Takumi S-HN4 + controller | open |
| OQ-004 | fn.29 weekly-salary equality (48h diurna = 36h nocturna = 42h mixta) vs Art. 329's per-hour +25% night recargo: both rules are encoded as printed (FR-224 + FR-227) without reconciliation — how the quoted nocturna weekly salary relates to the per-hour recargo for full-time nocturna workers (rate-quoted-at-equality vs recargo-on-top) is a payroll-practice question; never derived by the engine (D-H2 never-guess). | no | Takumi S-HN4 + controller | open |

| OQ-005 | NEW (V-HN1 adversarial review): weekly-data ingestion depth — the fn.31 prior-week ÷6/÷days-worked routine (FR-235/FR-239/FR-247) requires week-level day counts and earnings, which D-H3's monthly-aggregate ingestion cannot reconstruct; either an enhanced weekly-aggregate ingestion depth or a documented approximation rule must be ruled before go-live payroll history import. | no | controller ruling (D-H3 extension) | open |