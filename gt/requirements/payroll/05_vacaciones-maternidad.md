# GT — Payroll — Vacaciones, maternidad, lactancia and menores (CT Arts. 130-137, 148-155)

| Field   | Value |
|-------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the Guatemala Código de Trabajo (Labor Code, CT, Decreto
1441) statutory-benefits core of the P1 cluster: the *vacaciones* (annual
vacation) engine of Arts. 130-137 — FIFTEEN *días hábiles* (working days)
after each year of continuous service for the same employer (Art. 130, with
continuity per Art. 82 c)/d) — whose mechanics those files own), gated on a
minimum of 150 worked days in the year with paid-license and
illness/accident days counted as worked (Art. 131), employer scheduling of
effective enjoyment within the 60 days following the anniversary (Art. 132),
the NO-cash-compensation-while-employed rule with its sole termination
exception — proportional cash-out on cese whatever the cause (Art. 133) —
the prepaid valuation base = average of ordinary AND extraordinary
remunerations over the last three months (agricultural/livestock
enterprises) or the last year (all others) counted from acquisition of the
right, paid in advance (Art. 134), the no-deduction rule for unjustified
absences (Art. 135, gloss-level), the non-accumulation rule with the
at-most-two-parts split and the omitted-vacations retro claim capped at the
last five years at termination (Art. 136), and the signed-*constancia*
presumption of non-grant (Art. 137); the *maternidad* (maternity) engine of
Art. 152 — EIGHTY-FOUR effective rest days paid at 100% of salary, 30
prenatal + 54 postnatal, with unused prenatal days rolling forward so the
mother always enjoys 84 effective days anchored on the actual birth, halved
rests for non-intentional abortion or non-viable premature birth, the
≤3-month medically-certified extension, the adoption license starting the
day after delivery of the child, and the employer-pays branch unless the
worker is covered by IGSS (EVID-309 cross-ref by id; program mechanics owned
by `07_igss-contributions.md`); the *inamovilidad* (immovability) guard of
Art. 151 c)-e) — the dismissal ban for pregnant and lactating workers, the
prior express-and-written judicial-authorization gate even for justa causa,
the reinstatement + backpay remedy, the notice→provisional /
certificate→definitive protection triggers, and the no-heavy-work rule for
the last three prenatal months; the *lactancia* (nursing) engine of Arts.
153-155 — two paid half-hour daily breaks or one accumulated hour for ten
months from return (extendable by prescription), the Art. 154 computation
bases (gloss-level) and the nursery-room duty of employers with more than
thirty female workers; and the *menores* (minors) rules of Arts. 148-150 —
the absolute age-14 hire floor with its sole Inspección General de Trabajo
(IGT) written-authorization exception, the ban on night and overtime work
for all minors, and the −1h/day −6h/week (>14) and −2h/day −12h/week (≤14,
where IGT-authorized) reductions of the ordinary diurnal jornada. The
anti-discrimination hires rule of Art. 151 a)-b) is recorded as LB-021
(non-computational; no FR).

It does **not** cover: the *salario* / *salario completo* model whose
ordinary+extraordinary component tagging feeds every average here
(`01_ct-salary-model.md` — GT-PAY-FR-005 consumed by id, never restated);
jornada classification, weekly-hours accounting, descanso semanal and the
asueto calendar whose structure the días-hábiles counting consumes
(`02_working-time-overtime.md` — GT-PAY-FR-026, GT-PAY-FR-040,
GT-PAY-FR-043, GT-PAY-FR-033 consumed by id); the salario mínimo chassis
and dated AG tables (`03_minimum-wage.md`); statutory bonuses, including
the incentivo non-integration rule consumed here by id
(`04_statutory-bonuses.md` — GT-PAY-FR-090); contracts, despido, the
Art. 82 continuity rules and indemnización (`06_contracts-termination.md`
— owns the termination-flow mechanics this file's prorations plug into, and
the Art. 177 justa-cause framework the judicial gate cites); IGSS
contributions, planilla electrónica and the IGSS maternity program branch
(`07_igss-contributions.md`); IRTRA/INTECAP patronal charges
(`08_irtra-intecap.md`); the ISR computation itself (`09_isr-iva-interfaces.md`;
the perception-rule anchors are consumed from
`gt/requirements/taxation/04_isr-trabajo.md` GT-TAX-FR-111/112 by id); or
sanction values (owned by `gt/requirements/taxation/06_ct-procedures.md`).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): **CT labor
LBs cite 32_ as "CT art. N (texto según edición conmemorativa 2024,
MinTrabajo)" — no "current through" date claimable** (the edition is a
commemorative MinTrabajo print of indeterminate consolidation cutoff: latest
printed annotation D18-2001 with demonstrably later unannotated content —
GOQ-70/71; the R44 mitigation is the qualifier carried on every CT row
below). This file's LB slice is EVID-291..296 (EV03a). The IGSS-side
maternity program split is EVID-309 (EV03b) — cross-referenced BY ID ONLY,
no LB row here (the employer-pay branch of Art. 152 b) is CT-side and
LB-anchored below). The ISR perception-rule anchors GT-TAX-FR-111/112 are
external ids consumed by id. Gloss-level rows are marked as such (no
Spanish verbatim exists in this file's evidence slice for them; the source
txt layer is cited for corroboration only).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT art. 130 (texto según edición conmemorativa 2024, MinTrabajo): "Todo trabajador sin excepción, tiene derecho a un período de vacaciones remuneradas después de cada año de trabajo continuo al servicio de un mismo patrono, cuya duración mínima es de quince días hábiles. El hecho de la continuidad del trabajo se determina conforme a las reglas de los incisos c) y d) del Artículo 82." | Art. 130: every worker without exception has the right to a paid vacation period after each year of continuous work for the same employer, whose minimum duration is fifteen working days (días hábiles); the continuity of work is determined per the rules of Art. 82 c) and d) (continuity rules owned by `06_contracts-termination.md`, by filename) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 130 p.68 (EVID-291) |
| LB-002 | CT art. 131 (texto según edición conmemorativa 2024, MinTrabajo): "Para que el trabajador tenga derecho a vacaciones, aunque el contrato no le exija trabajar todas las horas de la jornada ordinaria ni todos los días de la semana, deberá tener un minino [sic] de ciento cincuenta (150) días trabajados en el año. Se computarán como trabajados los días en que el trabajador no preste servicios por gozar de licencia retribuida… por enfermedad profesional, enfermedad común o por accidente de trabajo." | Art. 131: to acquire the vacation right the worker needs a minimum of 150 WORKED days in the year (even when the contract does not require the full ordinary jornada or every day of the week); days not worked while enjoying PAID leave (statutory or collective-agreement), occupational disease, common illness or work accident COUNT as worked days (deemed-worked days) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 131 p.68 (EVID-291) |
| LB-003 | CT art. 132 (texto según edición conmemorativa 2024, MinTrabajo): "El patrono debe señalar al trabajador la época en que dentro de los sesenta días siguientes a aquél en que se cumplió el año de servicio continuo, debe gozar efectivamente de sus vacaciones." | Art. 132: the employer must designate the time within the SIXTY days following completion of the continuous-service year in which the worker must EFFECTIVELY enjoy the vacation | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 132 pp.68-69 (EVID-292) |
| LB-004 | CT art. 133 (texto según edición conmemorativa 2024, MinTrabajo): "Las vacaciones no son compensables en dinero, salvo cuando el trabajador que haya adquirido el derecho a gozarlas no las haya disfrutado por cesar en su trabajo cualquiera que sea la causa." / "Cuando el trabajador cese en su trabajo cualquiera que sea la causa, antes de cumplir un año de servicios continuos, o antes de adquirir el derecho a un nuevo período, el patrono debe compensarle en dinero la parte proporcional de sus vacaciones de acuerdo con su tiempo de servicio." | Art. 133: vacations are NOT compensable in money, except when the worker who acquired the right did not enjoy it because employment ceased, WHATEVER the cause; on cese whatever the cause before completing one year of continuous service, or before acquiring the right to a new period, the employer must compensate in money the PROPORTIONAL part of the vacations according to time of service | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 133 p.69 (EVID-292) |
| LB-005 | CT art. 134 (texto según edición conmemorativa 2024, MinTrabajo): "Para calcular el salario que el trabajador debe recibir con motivo de sus vacaciones, debe tomarse el promedio de las remuneraciones ordinarias y extraordinarias devengadas por él durante los últimos tres meses, si el beneficiario presta sus servicios en una empresa agrícola o ganadera, o durante el último año en los demás casos." / "El importe de este salario debe cubrirse por anticipado." | Art. 134: the vacation salary = the average of the ordinary AND extraordinary remunerations earned during the last THREE months (agricultural or livestock enterprise) or the LAST YEAR (all other cases); the terms run from the moment the worker acquires the vacation right; the amount must be paid IN ADVANCE | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 134 p.69 (EVID-292) |
| LB-006 | CT art. 135 (gloss-level per EVID-292 — no Spanish verbatim in this file's evidence slice): unjustified absences not deducted from vacation period (subject to paid-absence third-part rule) | Art. 135 (gloss): unjustified-absence days must NOT be deducted from the vacation period; for workers paid by quincena or month, PAID unjustified absences may not be deducted beyond a number of days equivalent to one third of the corresponding vacation period | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 135 p.69 (EVID-292, gloss) |
| LB-007 | CT art. 136 (texto según edición conmemorativa 2024, MinTrabajo): "Las vacaciones no son acumulables de año en año… pero el trabajador a la terminación del contrato puede reclamar la compensación en efectivo de las que se les haya omitido correspondiente a los cinco (5) últimos años”.”" [sic — closing-quote reform-stamp artifact as printed, per EVID-292 doubts] / (gloss, same EVID): enjoyment must be uninterrupted, split into at most two parts only for special-labors cases | Art. 136: vacations are NOT accumulable from year to year (to bank a longer later rest); at contract termination the worker may claim cash compensation of OMITTED vacations corresponding to the last FIVE (5) years; enjoyment is without interruptions, divisible into at most TWO parts only when special labors do not allow a very prolonged absence | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 136 p.69 (EVID-292) |
| LB-008 | CT art. 137 (texto según edición conmemorativa 2024, MinTrabajo): "se presume, salvo prueba en contrario, que las vacaciones no han sido otorgadas si el patrono… no muestran la respectiva constancia firmada…" | Art. 137: written record of the vacation grant must be left at the request of employer or worker; in private enterprises it is PRESUMED, save proof to the contrary, that vacations were NOT granted when the employer, at the labor authorities' request, fails to show the respective constancia SIGNED by the worker (or with the worker's fingerprint) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 137 p.69 (EVID-292) |
| LB-009 | CT art. 152 head (texto según edición conmemorativa 2024, MinTrabajo): "La madre trabajadora gozará de un descanso retribuido con el ciento por ciento (100%) de su salario durante los treinta (30) días que precedan al parto y los 54 días siguientes; los días que no pueda disfrutar antes del parto, se le acumularán para ser disfrutados en la etapa post-parto, de tal manera que la madre trabajadora goce de ochenta y cuatro (84) días efectivos de descanso durante ese período:" | The working mother enjoys a rest paid at one hundred percent (100%) of her salary during the thirty (30) days preceding the birth and the 54 days following; days she cannot enjoy before the birth ACCUMULATE for enjoyment in the post-partum stage, so that the working mother enjoys eighty-four (84) EFFECTIVE rest days during that period | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 152 head pp.74-76 (EVID-293) |
| LB-010 | CT art. 152 b) (texto según edición conmemorativa 2024, MinTrabajo): "…tiene derecho a que su patrono le pague su salario, salvo que esté acogida a los beneficios del Instituto Guatemalteco de Seguridad Social…" | Art. 152 b): the worker granted the rest has the right that her EMPLOYER pay her salary, UNLESS she is covered by the benefits of the Instituto Guatemalteco de Seguridad Social (IGSS), in which case the IGSS reglamentos govern — the employer-pay branch is CT-side; the IGSS program mechanics are owned by `07_igss-contributions.md` (EVID-309, cross-ref by id only, no LB row here) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 152 b) pp.74-76 (EVID-293) |
| LB-011 | CT art. 152 c) (texto según edición conmemorativa 2024, MinTrabajo): c) aborto no intencional / parto prematuro no viable: "los descansos remunerados… se deben reducir a la mitad"; post-birth incapacity benefits continue "siempre que éste no exceda de tres meses contados a partir del momento en que dejó sus labores" | Art. 152 c): for non-intentional abortion or non-viable premature birth, the remunerated rests are REDUCED TO HALF; absence beyond the granted rest due to medically-certified illness originating in the pregnancy or birth preserves the Art. 152 b) prestaciones during the whole recovery period, provided it does not exceed THREE months counted from the moment she left her labors | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 152 c) pp.74-76 (EVID-293) |
| LB-012 | CT art. 152 f) (texto según edición conmemorativa 2024, MinTrabajo): f) adopción: "La trabajadora que adopte a un menor de edad, tendrá derecho a la licencia post-parto… la licencia se iniciará a partir del día inmediato siguiente a aquel en que se le haga entrega del o la menor." | Art. 152 f): a worker who ADOPTS a minor is entitled to the post-partum license so both enjoy an adaptation period; the license starts on the day immediately following the day the child is delivered to her (adoption-process documents gate the right) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 152 f) p.76 (EVID-293) |
| LB-013 | CT art. 154 (gloss-level per EVID-293 doubts/xref + EVID-295 gloss — no Spanish verbatim in this file's evidence slice): the art. 152 and art. 153 prestación values fold ordinary+extraordinary salary averages (art. 154 p.76), counted from the moment the worker left her labors; lactancia break time counts as effective working time in pay computations (art. 154 a)) | Art. 154 (gloss): maternity/lactancia pay computation — the art. 152 prestación value derives from an ordinary+extraordinary salary AVERAGE (time-unit pay: last six months or fraction; other pay forms: last ninety days or fraction — windows corroborated in the source txt layer p.76), counted from the moment she left her labors; the art. 153 break time is computed AS effective working time | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 154 p.76 (EVID-293 doubts/xref; EVID-295 gloss) |
| LB-014 | CT art. 151 c) (texto según edición conmemorativa 2024, MinTrabajo): c) "Despedir a las trabajadoras que estuvieren en estado de embarazo o período de lactancia, quienes gozan de inamovilidad. Salvo que por causa justificada originada en falta grave a los deberes derivados del contrato, de conformidad con lo dispuesto en el Artículo 177 de este Código. En este caso, el patrono debe gestionar el despido ante los tribunales de trabajo para lo cual deberá comprobar la falta y no podrá hacer efectivo el mismo hasta no tener la autorización expresa y por escrito del Tribunal. En caso el patrono no cumpliera… la trabajadora podrá concurrir a los tribunales a ejercitar su derecho de reinstalación… y tendrá derecho a que se le paguen los salarios dejados de devengar durante el tiempo que estuvo sin laborar." | Art. 151 c): employers are prohibited from dismissing workers who are pregnant or in the lactancia period — they enjoy INAMOVILIDAD — save for justified cause originating in a grave breach of contract duties per Art. 177; in that case the employer must PROCESS the dismissal before the labor courts, proving the breach, and may not make it effective until the tribunal's EXPRESS WRITTEN authorization; failing which the worker may go to the courts to exercise her REINSTATEMENT right and is entitled to payment of the salaries not earned during the time she was without work | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 151 c) pp.74-75 (EVID-294) |
| LB-015 | CT art. 151 d)-e) (texto según edición conmemorativa 2024, MinTrabajo), d): "…la trabajadora deberá darle aviso de su estado al empleador, quedando desde ese momento provisionalmente protegida y dentro de los dos meses siguientes deberá aportar certificación médica de su estado de embarazo para su protección definitiva." / e) no heavy work for pregnant workers "durante los tres (3) meses anteriores al alumbramiento" | Art. 151 d): to gain the c)-protection the worker must give the employer NOTICE of her state — provisionally protected from that moment — and within the following TWO months produce the medical certificate of pregnancy for DEFINITIVE protection; e) employers may not require pregnant workers to perform work requiring considerable physical effort during the THREE months before the birth | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 151 d)-e) pp.74-75 (EVID-294) |
| LB-016 | CT art. 153 (texto según edición conmemorativa 2024, MinTrabajo): "Toda trabajadora en época de lactancia puede disponer en el lugar donde trabaja de media hora dos veces al día durante sus labores con el objeto de alimentar a su hijo." / "La trabajadora en época de lactancia podrá acumular las dos medias horas a que tiene derecho y entrar una hora después del inicio de la jornada o salir una hora antes de que ésta finalice… Dicha hora será remunerada y el incumplimiento dará lugar a la sanción correspondiente para el empleador." / "El período de lactancia se debe computar a partir del día en que la madre retorne a sus labores y hasta diez (10) meses después, salvo que por prescripción médica éste deba prolongarse." | Art. 153: every lactating worker may take HALF an hour TWICE a day at the workplace to breastfeed her child; she may ACCUMULATE the two half hours and enter one hour after the jornada starts or leave one hour before it ends; that hour is REMUNERATED and non-compliance sanctions the employer; the lactancia period runs from the day the mother RETURNS to her work until TEN (10) months later, unless extended by medical prescription | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 153 pp.75-76 (EVID-295) |
| LB-017 | CT art. 155 (texto según edición conmemorativa 2024, MinTrabajo), gloss-level partial quote: employers "que tenga a su servicio más de treinta trabajadoras" must fit a nursing room/care space for children under three | Art. 155: every employer with MORE THAN THIRTY female workers must fit out a suitable local so mothers can safely breastfeed their children UNDER THREE years of age and leave them there during work hours under the care of a competent person designated and paid by the employer; simple fitment within the employer's economic possibilities, at the judgment and with the approval ("visto bueno") of the Inspección General de Trabajo | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 155 p.76 (EVID-295) |
| LB-018 | CT art. 148 (texto según edición conmemorativa 2024, MinTrabajo): "Se prohíbe: … b) Se suprime. c) El trabajo nocturno y la jornada extraordinaria de los menores de edad; d) El trabajo diurno de los menores de edad en cantinas…; y e) El trabajo de los menores de catorce años." | Art. 148 (prohibitions): c) night work and extraordinary jornada (overtime) of MINORS; d) diurnal work of minors in cantinas or analogous establishments selling alcoholic beverages for immediate consumption; e) the work of persons under FOURTEEN years; b) is printed "Se suprime." (suppressed) as printed | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 148 pp.72-74 (EVID-296) |
| LB-019 | CT art. 149 (texto según edición conmemorativa 2024, MinTrabajo): diurnal jornada reduced "a) En una hora diaria y en seis horas a la semana para los mayores de catorce años; y b) En dos horas diarias y en doce horas a la semana para los jóvenes que tengan esa edad o menos, siempre que el trabajo de éstos se autorice conforme al artículo 150 siguiente." ["esa edad" = catorce, as context shows — EVID-296 doubts] | Art. 149: the ordinary DIURNAL jornada of Art. 116 ¶1 is REDUCED for minors: a) by ONE hour daily and SIX hours weekly for those OVER fourteen; b) by TWO hours daily and TWELVE hours weekly for those aged fourteen or less, whenever their work is authorized per Art. 150; IGT-authorized lesser reductions are also possible | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 149 pp.72-74 (EVID-296) |
| LB-020 | CT art. 150 (gloss-level per EVID-296): Inspección General de Trabajo may authorize in exceptional cases work of under-14s (learning/family-economy need, light work, schooling) | Art. 150 (gloss): the IGT may extend, in duly-qualified exceptional cases, WRITTEN authorizations permitting ordinary diurnal work of under-14s, or reducing (totally or partially) the Art. 149 jornada reductions; applicants must prove the minor will work as apprenticeship or from family-economy necessity (extreme poverty), that the work is light in duration and intensity and compatible with the minor's health, and that schooling obligations are met in some form; each authorization records the minimum protection conditions | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 150 pp.72-74 (EVID-296, gloss) |
| LB-021 | CT art. 151 a)-b) (texto según edición conmemorativa 2024, MinTrabajo): job ads may not specify "sexo, raza, etnia y estado civil" nor "hacer diferencia entre mujeres solteras y casadas y/o con responsabilidades familiares" | Art. 151 a)-b): job advertisements may not specify sex, race, ethnicity or marital status as a requirement (save nature-of-the-job exceptions with IGT + Oficina Nacional de la Mujer authorization), and employers may not differentiate between single and married women and/or women with family responsibilities — recorded here as recruitment-surface metadata; NON-COMPUTATIONAL, no FR in this file | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 151 a)-b) p.74 (EVID-296) |

Version regime (D15/D16): NO dated data is owned by this file. Every value
cited here (15 días hábiles, 150 days, 60 days, 3-month/12-month windows,
84/30/54 days, 10 months, −1h/−2h reductions, age 14, >30 trabajadoras) is
STATIC law of CT D1441 as printed in the commemorative edition (R44 — the
edition qualifier on every row above is the GOQ-70/71 mitigation; no dated
consolidation claim). The per-year dated asueto rows the días-hábiles
counting consumes are owned by `02_working-time-overtime.md` GT-PAY-FR-043
(valid_from/valid_to + provenance per D15/D16); the maternity IGSS branch
re-keys per the IGSS instruments owned by `07_igss-contributions.md`.

## 3. Functional Requirements

### 3.1 Vacaciones engine (CT Arts. 130-137)

- **GT-PAY-FR-101:** The system shall accrue for every worker, after each
  year of continuous work for the same employer, a vacation-period
  entitlement of a MINIMUM of FIFTEEN días hábiles (working days), paid —
  universal (*sin excepción*); the qualifying year's CONTINUITY is
  determined per the Art. 82 c)/d) rules owned by
  `06_contracts-termination.md` (consumed by filename); entitlement state
  and its clocks are shared-row data (§5) both sides resolve identically.
  (LB-001; EVID-291)
- **GT-PAY-FR-102:** The system shall count the fifteen vacation days as
  DÍAS HÁBILES of the worker's own jornada structure — a calendar day
  counts toward the fifteen ONLY when it is a working day per the worker's
  recorded calendar: weekly rest days of the 5-6-day semana
  (`02_working-time-overtime.md` GT-PAY-FR-040), días de asueto including
  the two half-day entries (GT-PAY-FR-043, half-day entries counting one
  half) and non-working days NEVER count, and the calendar span of the
  vacation period extends until fifteen días hábiles have effectively
  elapsed; enjoyment is UNINTERRUPTED, divisible into at most TWO parts
  only for the special-labors cases of Art. 136 (gloss).
  (LB-001; LB-007; EVID-291, EVID-292)
- **GT-PAY-FR-103:** The system shall gate each vacation-period entitlement
  on the 150-worked-day qualification: a minimum of ONE HUNDRED FIFTY
  worked days in the qualifying year, with DEEMED-WORKED days counting
  toward it — days not worked while enjoying paid leave (licencia
  retribuida, statutory or collective-agreement), occupational disease,
  common illness or work accident count as worked; the worked/deemed
  counter and the qualified/deferred state are stored on the vacation
  period record (shared clock rows). (LB-002; EVID-291)
- **GT-PAY-FR-104:** The system shall enforce the enjoyment window: the
  employer records the designated época with a deadline computed at SIXTY
  days following the day the continuous-service year completed, within
  which the worker must EFFECTIVELY enjoy the vacation; an unenjoyed
  expired window raises a compliance flag on the record (no payslip
  computation is altered by the flag; the window-unit reading — calendar
  vs hábiles — is corpus-silent and gap-reported, §7). (LB-003; EVID-292)
- **GT-PAY-FR-105:** The system shall enforce the no-cash-out invariant as
  a payroll guard: vacations are NOT compensable in money — NO
  money-compensation vacation line may exist for an active employment;
  cash compensation exists ONLY at cese (termination) of the employment,
  whatever the cause, for vested-but-unenjoyed periods (FR-106/FR-107),
  and any in-employment compensation line is rejected at definition time.
  (LB-004; EVID-292)
- **GT-PAY-FR-106:** On termination whatever the cause (no responsibility
  test), the system shall cash-compensate the PROPORTIONAL part of the
  vacations corresponding to the worker's time of service — for a worker
  ceasing before completing one year of continuous service, or before
  acquiring the right to a new period; the proportional fraction derives
  from time served since the last qualifying anniversary (method
  corpus-silent — design default time-served ÷ one year, gap-reported
  §7); the departure-run mechanics are owned by
  `06_contracts-termination.md` (by filename; this FR supplies the
  proration hook the departure run calls). (LB-004; EVID-292)
- **GT-PAY-FR-107:** The system shall enforce non-accumulation — vacation
  periods do NOT accrue from year to year for later enjoyment — and shall
  pay at termination the OMITTED-vacations retro compensation in cash for
  the periods omitted by the employer, capped at the LAST FIVE YEARS
  before termination (its interplay with the 2-year general prescription
  of `01_ct-salary-model.md` GT-PAY-FR-020 is gap-reported, §7).
  (LB-007; EVID-292)
- **GT-PAY-FR-108:** The system shall value the vacation prestación as the
  AVERAGE of ordinary AND extraordinary remunerations earned by the worker
  — over the LAST THREE MONTHS for agricultural or livestock enterprises,
  over the LAST YEAR in all other cases — counted from the moment the
  right is acquired, and shall pay it IN ADVANCE (the vacation payslip
  line is dated no later than the enjoyment start); composition rides the
  salario-completo component tagging of `01_ct-salary-model.md`
  GT-PAY-FR-005 (consumed by id, never re-derived) and EXCLUDES the
  incentivo per the non-integration nature rule of
  `04_statutory-bonuses.md` GT-PAY-FR-090 (consumed by id); the
  daily-equivalent divisor turning the average into the 15-días-hábiles
  quantum is corpus-silent (design default: window total ÷ window días
  hábiles per FR-102; gap-reported §7). (LB-005; EVID-292)
- **GT-PAY-FR-109:** The system shall NOT deduct unjustified-absence days
  from the vacation period; for workers paid by quincena or month, PAID
  unjustified absences may not be deducted beyond a number of days
  equivalent to ONE THIRD of the corresponding vacation period
  (gloss-level rule; the FR enforces the no-deduction default and the
  one-third cap on any absence-driven vacation reduction).
  (LB-006; EVID-292)
- **GT-PAY-FR-110:** The system shall keep a written vacation-grant record
  (constancia) — left at the request of employer or worker — carrying the
  worker's signature (or fingerprint); and shall raise the
  presumption-of-non-grant flag (vacations presumed NOT granted, salvo
  prueba en contrario) on any vacation period lacking a signed constancia
  when inspected by the labor authorities — a compliance surface only,
  never a payslip computation. (LB-008; EVID-292)

### 3.2 Maternidad engine (CT Art. 152)

- **GT-PAY-FR-111:** The system shall model the maternity-rest entitlement
  as EIGHTY-FOUR effective rest days paid at ONE HUNDRED PERCENT (100%) of
  the worker's salary — structured as the THIRTY days preceding the birth
  plus the FIFTY-FOUR days following it — an entitlement-window clock
  (shared rows, §5). (LB-009; EVID-293)
- **GT-PAY-FR-112:** The system shall anchor the rest window on the ACTUAL
  birth: prenatal days the mother could not enjoy before the birth
  ACCUMULATE into the post-partum stage so that the mother always enjoys
  EIGHTY-FOUR effective rest days — postnatal days = 84 − prenatal days
  effectively enjoyed; the roll-forward recomputes on the recorded birth
  date. (LB-009; EVID-293)
- **GT-PAY-FR-113:** For non-intentional abortion (*aborto no
  intencional*) or non-viable premature birth (*parto prematuro no
  viable*), the system shall reduce the remunerated rests TO HALF — 42
  effective days of the 84-day scale — at 100% of salary, recomputing the
  window of FR-111/FR-112. (LB-011; EVID-293)
- **GT-PAY-FR-114:** The system shall preserve the Art. 152 b)
  prestaciones through a post-birth incapacity EXTENSION: when the worker
  remains absent beyond the granted rest due to illness that a medical
  certificate attributes to the pregnancy or birth and that incapacitates
  her for work, she keeps the FR-116 prestaciones during the whole
  recovery period, up to a maximum of THREE months counted from the
  moment she left her labors. (LB-011; EVID-293)
- **GT-PAY-FR-115:** The system shall grant the ADOPTION license: a worker
  who adopts a menor de edad is entitled to the post-parto license (the
  54-day postnatal component of FR-111) starting the day IMMEDIATELY
  following the day the child is delivered to her, gated on the recorded
  adoption-process documents. (LB-012; EVID-293)
- **GT-PAY-FR-116:** The system shall implement the employer-pay branch:
  the employer pays the worker's salary during the rests UNLESS she is
  covered by IGSS benefits (*acogida a los beneficios del Instituto
  Guatemalteco de Seguridad Social*), in which case the IGSS reglamentos
  govern and the employer line is suppressed — the IGSS program mechanics
  are owned by `07_igss-contributions.md` (by filename; EVID-309
  cross-referenced by id only, no LB row here); the branch selection is a
  per-worker coverage flag on the leave record. (LB-010; EVID-293)
- **GT-PAY-FR-117:** The system shall compute the maternity-rest pay value
  from the Art. 154 bases (gloss-level, LB-013): an ordinary+extraordinary
  salary AVERAGE — time-unit pay over the last SIX months or fraction,
  other pay forms over the last NINETY days or fraction — counted from
  the moment the worker left her labors (windows corroborated in the
  source txt layer p.76; verbatim re-extraction gap-reported, §7);
  composition rides the GT-PAY-FR-005 tagging and excludes the incentivo
  per `04_statutory-bonuses.md` GT-PAY-FR-090 (consumed by id); lactancia
  break time counts as effective working time (art. 154 a) gloss —
  FR-123). (LB-013; LB-009; EVID-293, EVID-295)
- **GT-PAY-FR-118:** FEED ONLY (never re-derived): every vacation and
  maternity remuneration line of this file is taxable work remuneration
  under the perception rule — the ISR anchors are consumed by id from
  `gt/requirements/taxation/04_isr-trabajo.md`: GT-TAX-FR-111 (every cash
  retribution of any denomination from dependent personal work) and
  GT-TAX-FR-112 (imputed to the liquidation period in which perceived or
  placed at the worker's disposal — the in-advance vacation payment feeds
  its payment-date period); NO exemption, split or retention arithmetic
  is implemented payroll-side. (LB-009; LB-005; EVID-293, EVID-292)

### 3.3 Inamovilidad — pregnancy/lactancia dismissal guard (CT Art. 151 c)-e))

- **GT-PAY-FR-119:** The system shall attach an inamovilidad guard to
  every termination flow touching a worker who is pregnant or in the
  lactancia period (the lactancia window running per FR-123's ten-month
  clock): the dismissal is PROHIBITED save through the FR-120 gate; the
  guard state machine runs on the termination flows of
  `06_contracts-termination.md` (by filename) with odoo surfaces and saas
  validation (§5). (LB-014; LB-016; EVID-294, EVID-295)
- **GT-PAY-FR-120:** The system shall enforce the judicial-authorization
  gate: a dismissal within the inamovilidad window may proceed ONLY for
  justified cause originating in a grave breach of contract duties under
  the Art. 177 justa-cause framework (owned by
  `06_contracts-termination.md`, by filename), and ONLY after the employer
  has processed the dismissal before the labor courts proving the breach
  and obtained the tribunal's EXPRESS AND WRITTEN authorization — without
  the recorded authorization document, the dismissal cannot be made
  effective and any termination action on the guard is blocked (odoo
  guard, saas validation). (LB-014; EVID-294)
- **GT-PAY-FR-121:** The system shall model the unauthorized-dismissal
  remedy branch: when the employer effects the dismissal without the
  FR-120 authorization, the worker may exercise her REINSTATEMENT right
  to the post she was performing, with BACK PAY of the salaries not
  earned (*salarios dejados de devengar*) during the time she was without
  work — recorded as a reinstatement order + backpay accrual on the
  employment record (odoo surface; saas-validated liability clock).
  (LB-014; EVID-294)
- **GT-PAY-FR-122:** The system shall drive the protection triggers: (a)
  NOTICE — the worker's recorded notice of her state protects her
  PROVISIONALLY from that moment; (b) CERTIFICATE — the medical
  certification of pregnancy recorded within the following TWO months
  makes the protection DEFINITIVE; and (c) the no-heavy-work guard — work
  assignments requiring considerable physical effort are prohibited for
  pregnant workers during the THREE months before the birth (assignment
  validation on the schedule, no pay computation). (LB-015; EVID-294)

### 3.4 Lactancia breaks and nursery duty (CT Arts. 153-155)

- **GT-PAY-FR-123:** The system shall grant every lactating worker the
  nursing-break entitlement: (a) TWO paid half-hour breaks per working day
  at the workplace to breastfeed her child, or (b) the ACCUMULATED
  alternative — enter one hour after the jornada starts or leave one hour
  before it ends; the hour is REMUNERATED and counted as effective
  working time (LB-013, art. 154 a) gloss — no salary reduction line may
  attach to the breaks); the entitlement window is the TEN months
  following the day the mother returns to her work, EXTENDABLE by medical
  prescription (window clock shared, break computation odoo, §5).
  (LB-016; EVID-295)
- **GT-PAY-FR-124:** The system shall flag the nursery duty as an
  OPERATIONAL obligation (facility, not money): every employer with MORE
  THAN THIRTY female workers must fit out a suitable local where mothers
  can safely breastfeed children UNDER THREE years of age and leave them
  during work hours under a designated competent caregiver paid by the
  employer — simple fitment within the employer's economic possibilities,
  subject to the Inspección General de Trabajo's judgment and approval;
  modeled as a headcount-triggered duty flag + task with an IGT-approval
  record, and NO payslip line of any kind (the fitment scale is external
  to the corpus — gap-reported, §7). (LB-017; EVID-295)

### 3.5 Menores — minors' work rules (CT Arts. 148-150)

- **GT-PAY-FR-125:** The system shall enforce the minors' prohibitions:
  (a) NO nocturna work and NO jornada extraordinaria for minors — no
  extraordinary-hours line may exist for a minor (the OT engine of
  `02_working-time-overtime.md` GT-PAY-FR-033 never fires for them;
  nocturna-window shifts are rejected by the FR-026 classifier surface);
  (b) no diurnal work of minors in cantinas or analogous
  alcoholic-beverage establishments; and (c) the absolute hire floor —
  the work of persons under FOURTEEN years is prohibited, with the sole
  exception of a recorded WRITTEN IGT authorization per Art. 150
  (qualified exceptional cases: apprenticeship or family-economy
  necessity, light work compatible with health, schooling satisfied;
  authorization may also reduce the Art. 149 rebajas partially or
  totally). (LB-018; LB-020; EVID-296)
- **GT-PAY-FR-126:** The system shall reduce the ordinary DIURNAL jornada
  of Art. 116 ¶1 for minor workers (limits consumed from
  `02_working-time-overtime.md` GT-PAY-FR-026): (a) minus ONE hour daily
  and SIX hours weekly for minors OVER fourteen; (b) minus TWO hours
  daily and TWELVE hours weekly for those aged fourteen or less whose
  work is IGT-authorized; (c) recorded IGT-authorized LESSER reductions
  admitted where granted; the reduced limits drive the ordinary/
  extraordinary boundary for minors (no OT lines may result — FR-125)
  and feed the weekly-hours counters of GT-PAY-FR-031.
  (LB-019; LB-020; EVID-296)

## 4. Data Model

Layer semantics: entitlement windows/clocks = `shared` (both sides resolve
the same rows); payslip vacation/maternidad computation + constancia =
`odoo`; the inamovilidad guard on termination flows = `odoo` with `saas`
validation. No dated values live in this file (§2 version regime); the
dated asueto rows consumed by FR-102 are owned by file 02 (GT-PAY-FR-043).

**Vacaciones engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.vacation.period (new) | anniversary_year · continuity_ref | integer / reference | one record per contract × anniversary year; continuity per art. 82 c)/d) (file 06) | FR-101 |
| l10n_gt.pay.vacation.period | qualified · worked_days · deemed_days | boolean / integer (computed) | 150-day gate; deemed: licencia retribuida · enfermedad profesional · enfermedad común · accidente de trabajo | FR-103 |
| l10n_gt.pay.vacation.period | state | select | deferred · accrued · scheduled · in_progress · enjoyed · cashed_out_termination · retro_omitted | FR-101, FR-103, FR-104, FR-106, FR-107 |
| l10n_gt.pay.vacation.period | window_deadline | date (computed) | anniversary + 60 days; expiry = compliance flag only | FR-104 |
| l10n_gt.pay.vacation.period | base_window · base_avg · prepaid | select / monetary / boolean | 3m (agro/ganadero) · 12m (others), ordinary+extraordinary per 01 GT-PAY-FR-005 tagging; incentivo excluded per 04 GT-PAY-FR-090; paid in advance | FR-108 |
| l10n_gt.pay.vacation.period | split_parts | integer (constraint) | default uninterrupted; ≤ 2 parts only for special labors (art. 136 gloss) | FR-102 |
| l10n_gt.pay.vacation.constancia (new) | period · signed_by · signature_mode | m2o / char / select | signature · fingerprint; absence ⇒ presumption-of-non-grant flag | FR-110 |
| hr.leave (vacaciones type) | días-hábiles counter | computed | counts only FR-040-week working days; asuetos (FR-043) and rest days never count | FR-102 |
| termination flow (file 06 hook) | gt_pay_vacation_proration · gt_pay_vacation_retro_5y | monetary (computed) | proportional any-cause; omitted-periods retro capped at last 5 years | FR-106, FR-107 |

**Maternidad engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.maternity.leave (new) | mode | select | normal_84d · halved_42d · adoption_54d | FR-111, FR-113, FR-115 |
| l10n_gt.pay.maternity.leave | birth_date (anchor) · prenatal_enjoyed · postnatal_days | date / integer (computed) | postnatal = 84 − prenatal enjoyed; recomputed on actual birth | FR-112 |
| l10n_gt.pay.maternity.leave | extension_months | integer (constraint) | medically-certified pregnancy/birth-origin incapacity; ≤ 3 months from leaving labors | FR-114 |
| l10n_gt.pay.maternity.leave | pay_branch | select | employer · igss_covered (IGSS mechanics = file 07; EVID-309 by id) | FR-116 |
| l10n_gt.pay.maternity.leave | base_avg · base_window | monetary / select (computed) | 6m (time pay) · 90d (other pay) ordinary+extraordinary from leaving labors (gloss LB-013); 01 GT-PAY-FR-005 tagging; incentivo out per 04 GT-PAY-FR-090 | FR-117 |
| hr.payslip.line (vacation/maternidad) | gt_pay_tax_feed | stamped (reference) | feed pointers to GT-TAX-FR-111 (rentas del trabajo) + GT-TAX-FR-112 (perception period); no split computed here | FR-118 |

**Inamovilidad, lactancia y menores:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.inamovilidad.guard (new) | state | select | unprotected · provisional (notice) · definitive (cert ≤ 2 months) | FR-122 |
| l10n_gt.pay.inamovilidad.guard | window_end | date (computed) | through lactancia end (10-month clock of FR-123; extendable) | FR-119 |
| l10n_gt.pay.inamovilidad.guard | tribunal_authorization | attachment / char (required gate) | express + written; without it the dismissal is blocked | FR-120 |
| l10n_gt.pay.inamovilidad.guard | reinstatement_order · backpay_accrual | boolean / monetary | salarios dejados de devengar accrual for the time without work | FR-121 |
| hr.employee (pregnant) | gt_pay_heavy_work_ban | boolean (constraint) | no considerable-physical-effort assignments in the 3 months before alumbramiento | FR-122 |
| l10n_gt.pay.lactancia.clock (new) | return_date · end_date · extension | date (computed) / boolean | end = return + 10 months; extension by medical prescription | FR-123 |
| hr.employee (lactancia) | gt_pay_lactancia_break_mode | select | two_half_hours · accumulated_one_hour; remunerated, effective working time | FR-123 |
| hr.payroll (company config) | gt_pay_nursery_duty | computed boolean + task | > 30 trabajadoras ⇒ local for children < 3 years + designated caregiver; IGT visto bueno record; no money line | FR-124 |
| hr.employee / hr.contract (minor) | birth_date · gt_pay_minor_band | date / select | none (≥18) · over_14 (−1h/−6h) · fourteen_or_less (−2h/−12h, IGT-authorized); night/OT prohibited | FR-125, FR-126 |
| hr.contract (minor, IGT) | gt_pay_igt_authorization | attachment / select | under-14 written authorization · lesser-reduction grant · none | FR-125, FR-126 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `saas` =
authoritative computation/validation in the Elixir core; `shared` =
contract items both sides must honor identically. This file's binding
defaults: entitlement windows/clocks = `shared`; payslip vacation/
maternidad computation + constancia = `odoo`; the inamovilidad guard on
termination flows = `odoo` with `saas` validation. Model names stable
across Odoo 17/18/19/20; no version-specific behavior required.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-101 | shared | — (config data §4) | entitlement year/period rows | Both sides resolve the same accrual state; continuity per file 06 |
| FR-102 | shared | — (consumes odoo calendar) | días-hábiles counter | Feeds from FR-026 jornada + FR-040 semana + FR-043 asuetos (file 02, by id); asuetos/rest days never count; split ≤ 2 parts |
| FR-103 | shared | — (config data §4) | worked/deemed counters | 150-day gate; deemed days: licencia retribuida/enfermedad/accidente count |
| FR-104 | shared | — (odoo scheduling surface) | window_deadline | Anniversary + 60 days; expiry = compliance flag only; unit gap §7 |
| FR-105 | odoo | hr.salary.rule (guard) | no-cash-out invariant | Money lines only at cese (FR-106/107); active-employment compensation rejected |
| FR-106 | odoo | hr.departure hook / hr.payslip.line | gt_pay_vacation_proration | Any-cause cese; proportional per time served; flow owned by file 06 (filename) |
| FR-107 | odoo | hr.departure hook / hr.payslip.line | gt_pay_vacation_retro_5y | Non-accumulation; omitted periods cash-compensated, last 5 years; prescription interplay gap §7 |
| FR-108 | odoo | l10n_gt.pay.vacation.period / hr.payslip (computation) | base_window/base_avg/prepaid | 3m agro / 12m others, ordinary+extraordinary (01 FR-005 tagging; incentivo out per 04 FR-090); in-advance payment; divisor gap §7 |
| FR-109 | odoo | hr.payslip (absence gating) | no-deduction + one-third cap | Unjustified absences never shrink the period; paid-absence cap ⅓ of period (gloss) |
| FR-110 | odoo | l10n_gt.pay.vacation.constancia | signed constancia record | Presumption-of-non-grant flag when absent; compliance surface only |
| FR-111 | shared | — (config data §4) | 84-day entitlement window | 30 pre + 54 post @100%; both sides resolve the same window |
| FR-112 | shared | l10n_gt.pay.maternity.leave (odoo surface) | birth anchor + roll-forward | postnatal = 84 − prenatal enjoyed; recomputed on actual birth |
| FR-113 | shared | l10n_gt.pay.maternity.leave | halved_42d mode | aborto no intencional / parto prematuro no viable |
| FR-114 | shared | l10n_gt.pay.maternity.leave | extension_months ≤ 3 | Certified pregnancy/birth-origin incapacity; from leaving labors |
| FR-115 | shared | l10n_gt.pay.maternity.leave | adoption_54d mode | Starts day after entrega; adoption documents gate |
| FR-116 | odoo | l10n_gt.pay.maternity.leave / hr.payslip.line | pay_branch | Employer pays unless IGSS-covered; IGSS mechanics = file 07 (EVID-309 by id only) |
| FR-117 | odoo | hr.payslip (computation) | base_avg 6m/90d | Gloss-level LB-013 (verbatim gap §7); 01 FR-005 tagging; incentivo out per 04 FR-090 |
| FR-118 | odoo | hr.payslip.line | gt_pay_tax_feed | GT-TAX-FR-111/112 consumed by id; perception-period feed; no split here |
| FR-119 | odoo (saas validation) | l10n_gt.pay.inamovilidad.guard + file-06 termination flow | guard attachment | Ban from notice through lactancia end; saas validates every guarded termination |
| FR-120 | odoo (saas validation) | l10n_gt.pay.inamovilidad.guard | tribunal_authorization | Express + written; without it the dismissal cannot be made effective |
| FR-121 | odoo (saas validation) | l10n_gt.pay.inamovilidad.guard | reinstatement + backpay | salarios dejados de devengar accrual; saas-validated liability clock |
| FR-122 | odoo (saas validation) | hr.employee + schedule validation | notice/cert triggers + heavy-work ban | Provisional on notice; definitive on cert ≤ 2 months; 3-month heavy-work ban |
| FR-123 | shared (window) · odoo (break computation) | l10n_gt.pay.lactancia.clock + hr.employee | 2×30min or 1h, 10 months | Remunerated, effective working time; extension by prescription |
| FR-124 | odoo | hr.payroll (company config) | gt_pay_nursery_duty | >30 trabajadoras facility flag + IGT record; NO money line |
| FR-125 | odoo | hr.employee / hr.contract (validators) | age-14 floor + night/OT ban | No OT line may exist for minors (02 FR-033 never fires); IGT written authorization exception |
| FR-126 | odoo | hr.contract (minor jornada) | −1h/−6h · −2h/−12h bands | Reduced diurnal limits feed 02 FR-031 counters; lesser IGT reductions admitted |

Version-regime notes (D12/D15/D16): no dated values live in this file —
every CT parameter cited is static law of the commemorative edition (R44
qualifier per row, §2); the per-year asueto rows the días-hábiles counter
consumes re-seed annually under file 02's GT-PAY-FR-043 regime; the IGSS
maternity branch re-keys per the instruments owned by file 07 (filename).

## 6. Acceptance Criteria

- **AC-001:** Given a qualified worker beginning a vacation period whose
  calendar span contains one full asueto day and one weekly rest day, when
  the días-hábiles counter runs, then only working days count toward the
  fifteen and the calendar span extends until 15 días hábiles have
  elapsed (the asueto and rest day never count); an attempt to schedule
  the period split into three parts is rejected (max two, special labors).
  (FR-101, FR-102)
- **AC-002:** Given a qualifying year with 130 effective worked days, 14
  licencia-retribuida days and 10 common-illness days, when the gate
  resolves, then deemed days count and 154 ≥ 150 qualifies the period;
  given 130 worked + 5 deemed days, then the period stays deferred
  (135 < 150). (FR-103)
- **AC-003:** Given a continuous-service anniversary completing
  1-March-2027 with the vacation unenjoyed, when the window resolves, then
  the deadline = 60 days following that day and an expired unenjoyed
  period raises a compliance flag — the payslip is unchanged (FR-104).
- **AC-004:** Given an active (non-terminating) qualified worker for whom
  a money-compensation vacation line is requested, when validated, then
  the line is rejected — cash compensation exists only at cese, whatever
  the cause (FR-105).
- **AC-005:** Given a worker resigning (worker-side cause, no
  responsibility test) 8 months after the last qualifying anniversary,
  when the departure run computes, then a proportional cash-out line for
  those 8 months is paid (fraction method per the gap-reported default),
  hooked into the file-06 departure flow (FR-106).
- **AC-006:** Given a worker terminated in 2026 whose employer omitted
  vacation grants for service years 2019 through 2025, when the retro
  computation runs, then cash compensation exists for the omitted periods
  of the last five years (2021-2025) and no row exists for 2019/2020 —
  and no in-employment accumulation ever accrued (FR-107).
- **AC-007:** Given a non-agro worker whose last-year remunerations are
  Q28,800 ordinary + Q2,400 extraordinary over 300 días hábiles, when the
  vacation prestación values, then the daily equivalent is Q104.00 and
  the prepaid prestación is 15 × Q104.00 = Q1,560.00 dated no later than
  the enjoyment start (per the gap-reported divisor default); the same
  worker at an agro/ganadero enterprise values over the last 3 months
  instead; the incentivo never enters the average (04 GT-PAY-FR-090).
  (FR-108)
- **AC-008:** Given a granted vacation period lacking a signed
  constancia, when inspected, then the record carries the
  presumption-of-non-grant flag (vacations deemed not granted salvo prueba
  en contrario); with the signed constancia recorded, the flag clears
  (FR-110).
- **AC-009:** Given a worker who begins prenatal rest 1-August expecting
  birth around 31-August, with actual birth on 21-August, when the window
  recomputes on the actual birth, then prenatal enjoyed = 20 days,
  postnatal = 64 days, total = 84 effective days at 100% of salary
  (FR-111, FR-112).
- **AC-010:** Given a non-intentional abortion or a non-viable premature
  birth, when the leave mode resolves, then the remunerated rests halve
  to 42 effective days at 100% of salary (FR-113).
- **AC-011:** Given a medically-certified pregnancy-origin incapacity
  keeping the worker absent 2 months beyond the granted rest, when the
  extension resolves, then the Art. 152 b) prestaciones persist through
  the whole recovery period (≤ the 3-month cap counted from leaving her
  labors) (FR-114).
- **AC-012:** Given an adoption with delivery of the child on 5-May, when
  the adoption license starts, then the post-parto license (54 days)
  runs from 6-May, gated on the recorded adoption documents (FR-115).
- **AC-013:** Given two workers on maternity rest — one not IGSS-covered,
  one acogida to IGSS benefits — when the payslips compute, then the
  first carries the employer-pay line at 100% and the second carries no
  employer line, only the branch pointer to `07_igss-contributions.md`
  (EVID-309 by id; no IGSS arithmetic here) (FR-116).
- **AC-014:** Given a definitively-protected pregnant worker for whom a
  dismissal is attempted without any recorded express-and-written
  tribunal authorization, when the termination action runs, then the
  guard blocks it (odoo surface, saas validation fails); given the
  dismissal was effected anyway, then the record carries the
  reinstatement order and the salarios-dejados-de-devengar backpay
  accrual (FR-119..FR-121).
- **AC-015:** Given a worker who returns from maternity rest on
  1-October-2026, when the lactancia clock resolves, then the break
  entitlement window runs to 31-July-2027 (10 months, extendable only by
  prescription), her daily 2×30-minute breaks (or accumulated hour) are
  remunerated as effective working time, and NO salary-reduction line
  attaches to them (FR-123).
- **AC-016:** Given an enterprise with 31 female workers, when the duty
  flag computes, then the nursery duty task is raised (local for children
  under three, designated caregiver, IGT record) and no payslip line
  exists for it; given 30 female workers, then no duty is raised
  (FR-124).
- **AC-017:** Given a 16-year-old diurnal worker, when the schedule and
  payslip validate, then the ordinary jornada runs at −1h/day and −6h/
  week (reduced Art. 116 limits), any 18:00-06:00 shift assignment is
  rejected, and no extraordinary-hours line can exist for the worker;
  given a 13-year-old hire attempt without a recorded IGT authorization,
  then it is rejected (FR-125, FR-126).
- **AC-018:** Given payslips carrying vacation and maternity pay lines,
  when the taxation interface inspects them, then each line carries only
  the feed stamps to GT-TAX-FR-111/112 (taxable work remuneration,
  perceived/at-disposal period) — no exemption, split or retention is
  computed payroll-side (FR-118).

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C):
NONE are assigned to this file. GOQ-70/71 (R44 edition discipline) are
discharged by the qualifier on every CT LB row (§2), the same treatment as
`01_ct-salary-model.md` and `02_working-time-overtime.md`. No OQ rows are
registered here and no new OQ ids are invented. Genuine gaps surfaced
during synthesis are REPORTED to the wave lead (task report) instead:

1. **Daily-equivalent divisor (affects FR-108/FR-117):** Art. 134 fixes
   the vacation valuation as the 3-month/12-month ordinary+extraordinary
   average but is silent on the divisor converting it into the
   15-días-hábiles (and, gloss-side, the 84-day) quantum; design default =
   window total ÷ window días hábiles, configurable pending an
   authority-grounded convention.
2. **Proportional-fraction method (FR-106):** Art. 133 says "la parte
   proporcional… de acuerdo con su tiempo de servicio" without a method;
   default = time served since the last qualifying anniversary ÷ one year.
3. **Art. 132 window unit (FR-104):** "sesenta días siguientes" does not
   state calendar vs días hábiles; default = calendar days.
4. **Art. 152 untraced continuations (this file's evidence slice):** the
   a) 5-week prenatal medical-certificate/acuse gate; the b)
   return-to-post / equivalent-post guarantee continuation; the d)
   asueto/rest/vacaciones coincidence relief inside the maternity rests;
   and the e) reposo-conditioned payment-suspension clause — all visible
   in the source txt layer (pp.74-76) but ABSENT from the EVID-293
   verbatim; no FRs written for them; extraction follow-up requested.
5. **Art. 154 verbatim (LB-013 gloss-level):** the 6-month (time pay) /
   90-day (other pay) averaging windows are corroborated in the source
   txt layer (p.76) but carried only at gloss level in EVID-293
   doubts/xref + EVID-295 gloss; re-extract as verbatim rows.
6. **Five-year retro vs prescription (FR-107):** the Art. 136 last-5-years
   omitted-claim reach vs the Art. 264 2-year general prescription
   (`01_ct-salary-model.md` GT-PAY-FR-020) — substantive reach vs
   procedural cut-off interplay unresolved in the corpus.
7. **Nursery fitment standard (FR-124):** "forma sencilla dentro de las
   posibilidades económicas del patrono, a juicio y con el 'visto bueno'
   de la Inspección General de Trabajo" — the operational scale is
   external to the corpus; duty flag only, no implementable standard.
8. **Art. 151 a)-b) anti-discrimination (LB-021):** recorded as
   recruitment-surface metadata (sex/race/ethnicity/marital-status ads
   ban; no single/married differentiation) — non-computational, no FR;
   ownership deferred to a future HR-surface file.
