# HN — Payroll — Suspension of contract, CT maternity & special regimes: sickness half-pay, minors, domésticos, riesgo residual (P11)

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster P11 — the Código
del Trabajo (CT, D.189-59) surfaces that alter the EMPLOYMENT STATUS or the
pay basis rather than the ordinary wage computation. It owns: (a) the
**suspension chassis** — the 15 Art. 100 causes as a contract-status catalog
affecting payslip generation, with the default no-salary rule and its
express CT exceptions, and the suspension-≠-termination guarantee for the
contract registry; (b) the **CT sickness half-pay** tenure schedule
(1/2/3 months at *medio salario* by tenure band; >5 years → 30 days of
salary per year of service), the terminate-after-6-months trigger flag, and
the explicit layering with the IHSS incapacidad cost-split (file 04): RIT
days 1-3 full-salary + 66% subsidy + complement run first; the CT schedule
applies only to non-covered sickness; (c) **CT maternity** — the 4+6-week
paid *descanso forzoso* (mandatory rest) at "same as her work" retribution
on the 180-day average base (variable salary: last-year average), the
Art. 136 employer top-up (full employer cost when IHSS is not obliged), the
ONE reconciliation FR bridging the IHSS 42+42-day subsidy calendar to the
CT 28+42-day rest calendar without ever merging them, *aborto* (miscarriage/
non-viable premature birth) 2-4 paid weeks, and *lactancia* (nursing)
2×30-minute paid breaks to 6 months of age; (d) **minors** — the <14
prohibition, the <17 6h/30h diurnal-only constitutional caps, the <16
Sunday-rest non-waivability and the 2-hour intermediate rest for
women/minors, as contract-level constraints feeding jornada validation;
(e) the **domésticos** (domestic workers) sub-regime — 1 paid rest day per
6, 15-day probation presumption, the 7-day/1-month preaviso (notice)
variant with pay-in-lieu, the CASH-only computation base, and the Art.
160/163 special indemnities; (f) the **riesgo profesional residual** — the
Art. 417 indemnization base (daily salary at the risk date, obra-worker
trailing averages, floored at the applicable *salario mínimo*), applying
only where IHSS coverage does not.

It does **not** own: the IHSS incapacidad subsidy cost-split (days 1-3,
66% subsidy, employer complement), the IHSS 42+42(+14) maternity subsidy
calendar and its qualifiers — file 04 (`04_ihss-incapacidad.md`,
HN-PAYR-FR-141..170, EV81), consumed by id; IHSS cotizaciones/techos —
file 03 (HN-PAYR-FR-101..135); RAP/fondo — file 05 (HN-PAYR-FR-181..215);
the jornada engine that enforces the minor caps — file 06
(HN-PAYR-FR-221..247); vacaciones and continuity accruals through
suspension — file 07 (HN-PAYR-FR-261..280); the general preaviso/cesantía
engines and ALL dismissal-penalty sides (including the pregnancy-window
60-day + 10-week + double-rest penalties) — file 08 (HN-PAYR-FR-291..325);
SMM dated rows and promedio feed — file 01 (HN-PAYR-FR-001..040); salario
classification (in-kind ≤30% general rule) and payroll records — file 10
(HN-PAYR-FR-371..405); ISR treatment of these payments — taxation/02
(HN-TAX-FR-046..078) and taxation/04 (HN-TAX-FR-121..153) by id.

## 2. Legal Basis

Authority order (binding, per master evidence index): CT = `86_` (CEDIJ
print of D.189-59; consolidation window pinned through D.278-2013 —
EVID-328, `EV85:86_ OQ-1` verification lead). `85_` (D.93-2021, G 35,760)
is a MISLABELED PENAL instrument: it derogates only articles of the Código
Penal D.130-2017 and touches ZERO CT articles (R-H57; EVID-329/333) — it is
cited here solely as the mislabel guard and is NEVER citable as CT legal
basis. Article map per R-H59 (suspension Arts. 99-105; maternity Arts.
135-146; minors Arts. 130-132 + 338; domésticos Arts. 154-163; riesgo Arts.
417-418); R-H60 negatives honored — no CT article outside the evidence-
pinned set is ever cited or invented. D-H1/D-H2/D-H3 bind everything
(dated rows, hecho-generador resolution by suspension/rest/risk date,
monthly per-contract aggregates from hire date, never-guess rule).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT Arts. 99-100 (suspension causes) | Art. 100: "Son causas de suspensión de los contratos de trabajo sin responsabilidad para las partes: 1. La falta de materia prima o fuerza motriz…7. Las enfermedades que imposibiliten al trabajador…8. El descanso pre y post-natal; licencias, descansos y vacaciones; 9. La detención o la prisión…11. El ser llamado el trabajador a prestar servicio militar; 12. El ejercicio de un cargo sindical…13. La huelga legal; 14. El paro legal; y, 15. Cualquier otra causa justificada…" | Suspension causes WITHOUT responsibility for the parties: lack of raw material or motive power…; diseases disabling the worker…; pre- and post-natal rest; leaves, rests and vacations; detention or imprisonment…; call to military service; exercise of a union office…; legal strike; legal lockout; and any other justified cause… | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 99 (p.37); CT-Art. 100 (pp.37-38) (EV85:EVID-300) |
| LB-002 | CT Arts. 104-105 (sickness half-pay schedule; termination trigger) | Art. 104: "…la única obligación del patrono es la de dar licencia al trabajador, hasta su total restablecimiento…y de acuerdo con las reglas siguientes: 1. Después de un trabajo continuo no menor de tres (3) meses, ni mayor de seis (6), le pagará medio salario durante un (1) mes; 2. Después de un trabajo continuo mayor de seis (6) meses, pero menor de nueve (9), le pagará medio salario durante dos (2) meses; 3. Después de un trabajo continuo mayor de nueve (9) meses le pagará medio salario durante tres (3) meses; y, 4. Después de un trabajo continuo mayor de cinco (5) años le pagará treinta (30) días de salario por cada año de servicio." Art. 105: "…el patrono podrá dar por terminado el contrato de trabajo cubriendo al trabajador el importe del preaviso, el auxilio de cesantía y demás indemnizaciones…" (six-month-sickness condition per EVID-300 gloss; quote trimmed with …) | The employer's only duty is to grant leave until total reestablishment and pay per the rules: ≥3-6 months of continuous work → half salary for 1 month; >6-9 months → half salary for 2 months; >9 months → half salary for 3 months; >5 years → 30 days of SALARY per year of service (the fourth rule does not repeat the medio-salario qualifier). After six months of sickness suspension the employer may terminate the contract covering preaviso, cesantía and other indemnities | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 104 (p.40, fn.14); CT-Art. 105 (pp.40-41) (EV85:EVID-300) |
| LB-003 | CT Arts. 135-136 (maternity rest; employer top-up) | Art. 135: "Toda trabajadora en estado de gravidez gozará de un descanso forzoso, retribuido del mismo modo que su trabajo, durante las cuatro (4) semanas que precedan al parto y las seis (6) que le sigan, y conservará el empleo y todos los derechos correspondientes a su contrato de trabajo. Si se tratare de un salario que no sea fijo…se tomará en cuenta el salario promedio devengado por la trabajadora en el último año de servicio, o en todo el tiempo si fuere menor." Art. 136: "Los patronos cubrirán la diferencia existente entre el subsidio económico que por maternidad del Instituto Hondureño de Seguridad Social, y la retribución que conforme al artículo anterior corresponde a la trabajadora en estado de gravidez. Cuando el Instituto Hondureño de Seguridad Social no esté obligado a cubrir el subsidio de maternidad, la obligación que señala este artículo corre íntegramente a cargo del patrono." | Every pregnant worker enjoys mandatory paid rest, remunerated the same way as her work, during the 4 weeks preceding birth and the 6 following it, keeping the job and all contract rights; non-fixed salary → average of the last year of service (or the whole time if shorter). Employers cover the difference between the IHSS maternity subsidy and that retribution; when IHSS is not obliged to pay the subsidy, the obligation runs entirely at the employer's cost | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 135 (p.53); CT-Art. 136 (p.54) (EV85:EVID-322) |
| LB-004 | CT Art. 137 (aborto) | "La trabajadora que en el curso del embarazo sufra un aborto o un parto prematuro no viable tiene derecho a una licencia de dos (2) a cuatro (4) semanas, remuneradas con el salario que devengaba en el momento de iniciarse el descanso." | A worker who suffers an abortion or non-viable premature birth is entitled to leave of 2 to 4 weeks, remunerated at the salary she was earning when the rest began | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 137 (p.54) (EV85:EVID-322) |
| LB-005 | CT Arts. 140-141 (lactancia; retribution base) | Art. 140: "El patrono está en la obligación de conceder a la trabajadora dos (2) descansos, de treinta (30) minutos cada uno, dentro de la jornada para alimentar a su hijo…sin descuento alguno en el salario por dicho concepto, durante los primeros seis (6) meses de edad." Art. 141: "La retribución del descanso forzoso se fijará sacando el promedio de salarios devengados durante los últimos ciento ochenta (180) días o fracción de tiempo menor…El valor del tiempo diario destinado a la lactancia se determinará dividiendo el salario devengado en el respectivo período de pago por el número de horas efectivamente trabajadas…" | The employer must grant two 30-minute breaks within the workday to nurse her child, with no salary deduction, during the first 6 months of age. The forced-rest retribution is fixed as the average of salaries earned over the last 180 days (or a shorter fraction); the value of daily nursing time = salary earned in the respective pay period ÷ hours actually worked | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 140 (p.55); CT-Art. 141 (p.55) (EV85:EVID-322) |
| LB-006 | CT Arts. 124, 144 (pregnancy dismissal protection — PENALTY SIDE crossref) | Art. 124: "El patrono no podrá dar por terminado el contrato de trabajo de la mujer embarazada sin justificar previamente ante el Juez de Trabajo respectivo, alguna de las causales enumeradas en el artículo 112. En estos casos subsistirá la relación de trabajo hasta que termine el descanso post-natal o hasta que quedare ejecutoriada la sentencia que declare la terminación del contrato." (Art. 144: presumption window pregnancy + 3 months postpartum; unauthorized dismissal → 60 days' wages + the 10 weeks' rest value if untaken — penalty computation OWNED by file 08) | The employer may not terminate a pregnant worker's contract without first justifying a just cause before the labor judge; the relationship subsists until the post-natal rest ends or a final judgment terminates it. Termination-window guards and stacked penalties are cross-referenced, not owned here | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 124 (p.50); CT-Art. 144 (p.56) (EV85:EVID-308) |
| LB-007 | CT Arts. 130, 132 + fn.21 + Art. 338 final ¶ (minors; women/minors rest) | Art. 130: "Dentro de la jornada ordinaria de trabajo, las mujeres y los menores gozarán de un descanso intermedio de dos (2) horas." Art. 132 ¶1: "Los menores de catorce (14) años y los que habiendo cumplido esa edad, sigan sometidos a la enseñanza en virtud de la legislación nacional, no podrán ser ocupados en ninguna clase de trabajo." fn.21 (Constitution C-1982 Art. 128.7): "…Para los menores de diez y siete (17) años la jornada de trabajo que deberá ser diurna, no podrá exceder de seis (6) horas ni de treinta a la semana, en cualquier clase de trabajo." Art. 338 final ¶: "Ninguna excepción respecto a la obligación del descanso dominical será aplicable a los menores de dieciséis (16) años." | Within the ordinary workday women and minors enjoy a 2-hour intermediate rest. Under-14s (and over-14s still under compulsory schooling) may not be employed in any work. Under-17s: workday must be DIURNAL, max 6 hours daily and 30 weekly, in any kind of work. No Sunday-rest exception applies to under-16s | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 130 (p.52); CT-Art. 132 (p.52, fn.6); fn.21 (p.52) + fn.8 (p.11); CT-Art. 338 final ¶ (p.98) (EV85:EVID-323) |
| LB-008 | CT Arts. 154, 158, 160, 161, 163 (domésticos) | Art. 154 ¶: "…tendrán derecho a un (1) día de descanso remunerado por cada seis (6) de trabajo." Art. 158: "En el trabajo doméstico los primeros quince (15) días se considerarán de prueba…Después del período de prueba, para terminar el contrato será necesario dar un aviso con siete (7) días de anticipación, y si el trabajador doméstico tiene más de un (1) año de trabajo continuo deberá darse el preaviso con un (1) mes de anticipación. En estos casos, podrá en defecto del aviso, abonar el importe correspondiente." Art. 160 ¶: "…cuando el patrono no le pague el salario que le corresponde, en cuyo caso deberá ser indemnizado con siete (7) días de salario si tiene menos de un (1) año de servicio y con un (1) mes si ha laborado un (1) año o más." Art. 161: "Los preavisos e indemnizaciones a que tenga derecho el trabajador doméstico se pagarán tomando en cuenta únicamente la remuneración en dinero que perciba." Art. 163: "…pagar a la otra parte un (1) mes de salario por cada año de trabajo continuo, o fracción de tiempo no menor de tres (3) meses. Está indemnización no podrá exceder del importe correspondiente a cuatro (4) meses de salario." | Domestic workers: one paid rest day per six worked; first 15 days presumed probation; post-probation termination needs 7 days' notice (<1 year) or 1 month (≥1 year), or payment of the corresponding amount in lieu; salary non-payment indemnity of 7 days (<1y) / 1 month (≥1y); preavisos and indemnities computed on CASH remuneration ONLY; special indemnity of 1 month per continuous year (fractions ≥3 months count), capped at 4 months | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 154 (p.58); Art. 158 (pp.58-59); Art. 160 (p.59); Art. 161 (p.59); Art. 163 (p.60) (EV85:EVID-324) |
| LB-009 | CT Arts. 417-418 (riesgo profesional base) | Art. 417: "Se tomará como base para calcular las indemnizaciones de que trata éste Título, el salario diario que perciba el trabajador en el momento en que se realice el riesgo. Tratándose de trabajadores cuyo salario se calcule por unidad de obra se tomará como base la cantidad que resulte como promedio diario en el último mes anterior al accidente y a falta de este dato el promedio diario en la última semana anterior al accidente…En ningún caso la cantidad que se tome como base para indemnización será inferior al salario mínimo." Art. 418: "Los trabajadores que sufran un riesgo profesional, tendrán derecho a: 1. Asistencia médica y quirúrgica; 2. Administración de medicamentos…; 3. La indemnización fijada en el presente Título…" | Indemnization base = the daily salary the worker receives at the moment the risk occurs; piece/unit-of-work workers → the daily average of the last month before the accident, failing that the last week's; in NO case may the base be lower than the salario mínimo (the text names salario mínimo, NOT promedio). Entitlements: medical/surgical assistance, medicines, and the indemnity fixed in the Title (scale NOT in the extracted corpus) | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | CT-Art. 417 (p.121); CT-Art. 418 (p.121) (EV85:EVID-325) |
| LB-010 | D. 93-2021 (85_), Art. 1 (mislabel guard — R-H57) | "Derogar los artículos 102, 103, 104, 105, 106, 176, 182, 225, 263, 275, 309, 317, 337, 346, 368, 397, 403, 411, 417, 430, 434, 437, 444, 469, 511, 569 y 596; todos del Decreto No.130-2017 de fecha 18 de Enero de 2018, que contiene el CÓDIGO PENAL…" | Derogation list of Código Penal D.130-2017 articles — the numerals (102-106, 337, 346, 368, 417…) COLLIDE with live CT articles but are PENAL articles: zero CT effect (EVID-333 cross-check verdict: 0 CT articles derogated) | `hn/sources/85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf` | 93-Art. 1 (p.2 / A.2) (EV85:EVID-329; EV85:EVID-333) |
| LB-011 | CT fn.36 p.152 + fn.19 p.49 + closing (vintage pins) | fn.36: "Artículo 464. Derogado por Decreto 278-2013 de fecha 21 de diciembre de 2013 y publicado en el Diario La Gaceta No.33,316 de fecha 30 de diciembre de 2013." Closing (p.271): publication in G 16,827-16,834, July 1959; Art. 875: "Este Código empezará a regir desde el día de su publicación en el Diario Oficial La Gaceta." | Consolidation window evidence: newest integrated instrument = D.278-2013; promulgation D.189-59 published 15-23 July 1959, in force from publication — the vintage boundary for every dated row of this file | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | fn.36 (p.152); fn.19 (p.49); closing (p.271); Art. 875 (pp.269-270) (EV85:EVID-328) |

## 3. Functional Requirements

### 3.1 Chassis: vintage guard and the suspension catalog

- **HN-PAYR-FR-331:** The system shall carry the CT regime as a DATED
  provenance row — source consolidation `86_` (D.189-59), `valid_from` the
  July-1959 publication (G 16,827-16,834, Art. 875 effectivity-from-
  publication), `pinned_through` D.278-2013 (fn.36) — and shall apply the
  R-H57 mislabel guard: D.93-2021 (`85_`) derogates only Código Penal
  D.130-2017 articles and has ZERO CT effect, so no CT article of this file
  (including the numerically colliding 102-106, 337, 346, 368, 417) may
  ever be flagged derogated by it and `85_` is never citable as CT legal
  basis; per R-H60 no CT article outside the evidence-pinned set may be
  cited, and any post-2013 CT reform surfacing against an official current
  consolidation is an acquisition lead (`EV85:86_ OQ-1`, OQ-001), never a
  silent text change. (LB-011; LB-010; EV85:EVID-328; EV85:EVID-329;
  EV85:EVID-333; R-H57; R-H59; R-H60)
- **HN-PAYR-FR-332:** The system shall load the 15 suspension causes of
  CT Art. 100 as a catalog of contract-status values affecting payslip
  generation — each row carrying the numeral, the Spanish text, and a
  payroll treatment class (`no_salary`, `paid_by_ct_rule`,
  `rides_own_regime`) — with the verbatim-pinned numerals 1, 7, 8, 9, 11,
  12, 13, 14, 15 seeded from the evidence text and numerals 2-6 and 10
  seeded from the same article marked `evid_elided` for verification
  (OQ-005); cause 7 (sickness) routes to the FR-335..338 half-pay/layering
  rules, and cause 8 (pre/post-natal rest; licencias, descansos y
  vacaciones) routes to the FR-339..344 maternity rules and to the owning
  sibling files by range (file 07 for vacaciones).
  (LB-001; EV85:EVID-300)
- **HN-PAYR-FR-333:** The system shall model suspension as NON-termination:
  the employment relationship persists ("sin responsabilidad para las
  partes" suspends obligations, it does not extinguish the contract), so a
  suspension record sets no termination date, triggers no final-settlement,
  preaviso or cesantía flows (termination surfaces owned by file 08,
  HN-PAYR-FR-291..325), and leaves tenure counters running — the continuity
  consequences for vacaciones/cesantía accruals are consumed from files 07
  (HN-PAYR-FR-261..280) and 08 by range, never recomputed here.
  (LB-001; EV85:EVID-300)
- **HN-PAYR-FR-334:** The system shall apply the default no-salary rule:
  suspension days generate NO salary obligation arising from the CT itself,
  and payslips covering suspension days emit no ordinary salary lines for
  those days EXCEPT where the CT itself provides pay — the Art. 104
  sickness half-pay (FR-335..336), the Arts. 135-141 maternity retribution
  (FR-339..344), and cause-8 items paid under their own regimes (vacaciones
  per file 07; unpaid *licencias sin goce de salario* (unpaid leaves) stay
  unpaid) — with *huelga legal* and *paro legal* (legal strike/lockout,
  causes 13-14) unpaid unless otherwise agreed, and collectively bargained
  improvements applying upward-only.
  (LB-001; LB-002; LB-003; EV85:EVID-300; EV85:EVID-322)

### 3.2 CT sickness half-pay and the IHSS layering

- **HN-PAYR-FR-335:** The system shall implement the CT sickness half-pay
  schedule as DATED statutory band rows (`valid_from` the 1959 regime row
  of FR-331, never replaced in place): after continuous work of ≥3 months
  and ≤6 months → half salary (*medio salario*) for 1 month; >6 months and
  <9 months → half salary for 2 months; >9 months → half salary for 3
  months — the employer's concurrent duty being to grant the *licencia*
  (leave) until total reestablishment; continuous-work tenure is measured
  from per-contract hire-date monthly aggregates (D-H3(a)), never from
  calendar accident. (LB-002; EV85:EVID-300)
- **HN-PAYR-FR-336:** The system shall implement the >5-years branch
  verbatim: after continuous work of more than 5 years, the schedule pays
  "treinta (30) días de salario por cada año de servicio" — 30 days of
  SALARY per year of service — encoded at full-salary value because the
  fourth rule, unlike rules 1-3, carries no *medio salario* qualifier (the
  drafting nuance is flagged, OQ-003, never silently resolved); band edges
  follow the printed comparators ("no menor de…ni mayor de", "mayor
  de…pero menor de", "mayor de"). (LB-002; EV85:EVID-300)
- **HN-PAYR-FR-337:** The system shall emit, and only emit, the
  terminate-after-6-months trigger flag: when a sickness suspension reaches
  six months, the employer MAY terminate the contract covering preaviso,
  auxilio de cesantía and other indemnities — the election and every payout
  computation belong to file 08 (HN-PAYR-FR-291..325, consumed by range);
  no automatic termination shall ever occur from the flag alone.
  (LB-002; EV85:EVID-300)
- **HN-PAYR-FR-338:** The system shall encode the PRECEDENCE between the
  IHSS incapacidad regime and the CT half-pay schedule explicitly, never as
  a merged rule: (a) any sickness day belonging to an IHSS incapacidad case
  runs under the RIT cost-split consumed BY ID from file 04
  (HN-PAYR-FR-150..153: days 1-3 employer-paid FULL salary; days 4-365 the
  66% subsidy plus the Art. 73 ¶2 employer complement to full salary) and
  the CT Art. 104 half-pay shall NEVER apply to that day; (b) the CT
  Art. 104 half-pay schedule applies to sickness days of suspended
  contracts NOT covered by any IHSS case (non-affiliated workers, unmet
  subsidy qualifiers, interstices outside any case); (c) days whose IHSS
  coverage state is unknown or unresolvable raise an explicit
  configuration flag and pay NOTHING under either regime until resolved
  (D-H2 never-guess; the un-covered edge stays config, OQ-004 — file 04's
  grace-window funding toggle family FR-160 is a separate configuration
  and is never reused here). (LB-002; EV85:EVID-300)

### 3.3 CT maternity: paid rest, base, top-up, and the reconciliation

- **HN-PAYR-FR-339:** The system shall implement the mandatory maternity
  rest as 4 weeks preceding the birth plus 6 weeks following it, paid "del
  mismo modo que su trabajo" (the same way as her work), with the
  employment and ALL rights of the contract conserved — the rest is
  suspension cause 8 in the FR-332 catalog and never a termination event;
  the in-window dismissal guard, the pregnancy/lactancia presumption window
  and its stacked penalties (60 days' wages + untaken 10-weeks' rest value
  + double remuneration of unconceded rests) are owned by file 08
  (HN-PAYR-FR-291..325) and consumed by range.
  (LB-003; LB-006; EV85:EVID-322; EV85:EVID-308)
- **HN-PAYR-FR-340:** The system shall compute the rest retribution on the
  180-day average base: the average of salaries earned during the last 180
  days or a shorter fraction (Art. 141), with the variable-salary override
  of Art. 135 ¶2 — non-fixed salaries take the average of the last year of
  service, or the whole service if shorter; both averages are computed from
  per-contract monthly salary aggregates from the hire date (D-H3(a)) and
  snapshot-on-write onto the leave record with their inputs (D15); the
  resolved base is never recomputed with later-period rows on correction —
  retro recomputes use ORIGINAL-period aggregates (D16).
  (LB-003; LB-005; EV85:EVID-322)
- **HN-PAYR-FR-341:** The system shall compute the employer top-up of
  Art. 136 as the day-by-day difference between the FR-340 retribution and
  the IHSS maternity subsidy economically payable for the same day (subsidy
  figures imported BY ID from file 04, HN-PAYR-FR-141..170 — never
  restated), and shall charge the ENTIRE retribution at employer cost for
  rest days where IHSS is not obliged to cover the subsidy (uncovered
  workers, unmet qualifiers). (LB-003; EV85:EVID-322)
- **HN-PAYR-FR-342:** The system shall keep TWO maternity calendars that
  are NEVER merged, bridged by ONE reconciliation: (a) the IHSS subsidy
  calendar — 42 prenatal + 42 postnatal días calendario (+14 late-birth)
  anchored to the probable-partum date, owned by file 04
  (HN-PAYR-FR-154..157); (b) the CT paid-rest calendar — 4 weeks pre +
  6 weeks post (FR-339), anchored to the actual rest window; the bridge is
  the FR-341 employer complement: for every CT-rest day the worker receives
  her full CT retribution = IHSS subsidy payable that day + employer
  difference, IHSS-reposo days falling OUTSIDE the CT-rest window (e.g.
  prenatal subsidy days before the 4-week rest starts) run under the
  file-04 subsidy + RIT Art. 73 ¶2 complement regime, and rest days beyond
  the IHSS 42+42(+14) grant (contractual or CT excess) are
  employer-exclusive cost per the file 04 FR-157 interface; the 42+42 and
  4+6 numbers shall never be fused into a single regime, calendar or rate
  row. (LB-003; LB-005; EV85:EVID-322; EV81:EVID-267; EV81:EVID-263)
- **HN-PAYR-FR-343:** The system shall implement the *aborto* / non-viable
  premature-birth leave as a paid *licencia* of 2 to 4 weeks — the exact
  duration inside the band set by medical certification, never defaulted —
  remunerated at the salary the worker was earning at the moment the rest
  began (no averaging, no 180-day base). (LB-004; EV85:EVID-322)
- **HN-PAYR-FR-344:** The system shall implement *lactancia* (nursing) as
  two daily 30-minute breaks within the ordinary jornada, with NO salary
  deduction, during the first 6 months of the child's age; the paid value
  of the nursing time = salary earned in the respective pay period ÷ hours
  actually worked in that period (per-hour rate), applied to the break
  time so the payslip shows the time as paid, never deducted.
  (LB-005; EV85:EVID-322)

### 3.4 Minors and women: contract-level constraints

- **HN-PAYR-FR-345:** The system shall block the creation or activation of
  any labor contract for workers under 14 years of age, and for workers
  who having turned 14 remain under compulsory schooling under national
  legislation — an absolute hiring prohibition surfaced as a hard
  validation error, not a warning. (LB-007; EV85:EVID-323)
- **HN-PAYR-FR-346:** The system shall attach to every contract of a
  worker under 17 the constitutional schedule caps — maximum 6 hours daily
  and 30 weekly, DIURNAL work only, in any kind of work (C-1982 Art. 128.7
  as quoted in the CT footnotes) — as contract-level constraints emitted
  to the jornada validation engine owned by file 06 (HN-PAYR-FR-221..247,
  consumed by range); age is resolved as of each schedule/payslip date
  (D-H2 birthday discipline), never as of contract signature alone.
  (LB-007; EV85:EVID-323)
- **HN-PAYR-FR-347:** The system shall mark workers under 16 as
  NON-waivable for the Sunday rest obligation — no exception to the
  descanso dominical may be configured or accepted for them (the
  constraint rides the weekly-rest surfaces of file 06 by range).
  (LB-007; EV85:EVID-323)
- **HN-PAYR-FR-348:** The system shall require a 2-hour intermediate rest
  inside the ordinary jornada for women and minors (schedule shaping with
  no pay addition or reduction) on every calendar where a woman- or
  minor-worker contract applies, feeding the same jornada validation
  interface of file 06. (LB-007; EV85:EVID-323)

### 3.5 Domésticos sub-regime

- **HN-PAYR-FR-349:** The system shall accrue for domestic workers one
  paid rest day for every six days worked (the general weekly-rest
  surfaces being disapplied to domésticos, this 1-per-6 accrual stands as
  their statutory rest rule). (LB-008; EV85:EVID-324)
- **HN-PAYR-FR-350:** The system shall apply the 15-day probation
  PRESUMPTION to domestic-worker contracts — the first 15 days of service
  are presumed *período de prueba* (probation) with no written stipulation
  required (contrast: the general 60-day probation requires writing) — and
  the probation-exclusion semantics (all prestaciones accrue except
  preaviso and despido indemnization) resolve on the general probation
  surface of the contract chassis. (LB-008; EV85:EVID-324)
- **HN-PAYR-FR-351:** The system shall apply the doméstico preaviso
  variant: after the probation period, termination requires notice of 7
  days (less than 1 year of continuous work) or 1 month (1 year or more),
  or payment of the corresponding amount IN LIEU of the notice — this
  variant replaces the general Art. 116 scale inside the doméstico
  contract template; the general preaviso engine, notice-period working
  rules and in-lieu multipliers are owned by file 08
  (HN-PAYR-FR-291..325, consumed by range).
  (LB-008; EV85:EVID-324)
- **HN-PAYR-FR-352:** The system shall compute doméstico preavisos and
  indemnidades on the CASH remuneration ONLY ("únicamente la remuneración
  en dinero que perciba") — in-kind benefits are excluded from every
  doméstico termination computation base, the INVERSE of the general rule
  that values qualifying in-kind benefits into salario (general in-kind
  ≤30%-at-cost classification owned by file 10, HN-PAYR-FR-371..405).
  (LB-008; EV85:EVID-324)
- **HN-PAYR-FR-353:** The system shall compute the special doméstico
  indemnity of Art. 163 — 1 month of salary per continuous year of
  service, with any fraction of service of 3 months or more counting as a
  year — capped at 4 months of salary, on the FR-352 cash-only base.
  (LB-008; EV85:EVID-324)
- **HN-PAYR-FR-354:** The system shall compute the doméstico salary
  non-payment indemnity of Art. 160: when the employer does not pay the
  corresponding salary, the domestic worker is indemnified with 7 days of
  salary (less than 1 year of service) or 1 month (1 year or more), on the
  FR-352 cash-only base. (LB-008; EV85:EVID-324)

### 3.6 Riesgo profesional residual

- **HN-PAYR-FR-355:** The system shall apply the IHSS-first rule:
  occupational-risk handling is implemented on the IHSS side — RP
  cotizaciones and ceilings in file 03 (HN-PAYR-FR-101..135), RP
  incapacity subsidy and no-subsidy/full-employer-salary triggers in file
  04 (HN-PAYR-FR-141..170) — and the CT Título V residual (Arts. 417-418)
  computes ONLY for cases outside IHSS coverage (`EV85:86_ OQ-8`,
  OQ-002); the R-H57 guard of FR-331 protects live CT Art. 417 from the
  D.93-2021 penal-numeral collision.
  (LB-009; LB-010; EV85:EVID-325; EV85:EVID-329)
- **HN-PAYR-FR-356:** The system shall compute the residual indemnization
  base as: (a) the daily salary the worker receives at the moment the risk
  occurs; (b) for piece/unit-of-work (*obra*) workers, the daily average
  of the last month before the accident, failing that the daily average of
  the last week — both from hire-date monthly aggregates (D-H3(a)),
  snapshot-on-write (D15); and (c) floored so the base is NEVER below the
  salario mínimo — the article names salario mínimo generically (NOT
  promedio), so the floor consumes the worker's APPLICABLE SMM dated row
  (rama × band) from file 01 (HN-PAYR-FR-001..040) resolved as of the RISK
  DATE (the hecho generador), never the promedio row and never "today"'s
  row (D-H2). (LB-009; EV85:EVID-325)
- **HN-PAYR-FR-357:** The system shall record the Art. 418 entitlement
  surface for residual cases — medical and surgical assistance,
  medicines, and the indemnization fixed in Título V — and shall BLOCK the
  residual indemnity amount computation with an explicit configuration gap
  flag, because the Título V disability-grade indemnity SCALE is not in
  the extracted corpus: no percentage, multiplier or duration may be
  derived, averaged or hardcoded (D-H2 never-guess; OQ-002 acquisition
  lead). (LB-009; EV85:EVID-325)

## 4. Data Model

No machine-readable CSV sidecar is allocated to this file: every statutory
value here is either a band/boolean rule (encoded as model rows below) or
an imported dated input owned by a sibling file (SMM rows file 01; subsidy
figures file 04). Odoo-side computation/bookkeeping data only (wave default
`odoo`; see §5).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.ct.regime (new) | source, valid_from, pinned_through, gaceta_refs, verification_flag | char/date/char/boolean | `86_` D.189-59; valid_from 1959-07 (G 16,827-16,834 publication series, Art. 875); pinned_through D.278-2013; flag carries `EV85:86_ OQ-1` | FR-331 |
| l10n_hn.ct.suspension.cause (new) | numeral, text_es, payroll_treatment, evid_status | int/text/select/char | numerals 1-15 (Art. 100); treatment: no_salary · paid_by_ct_rule · rides_own_regime; evid_status: pinned (1,7,8,9,11-15) · evid_elided (2-6, 10 — OQ-005) | FR-332 |
| l10n_hn.ct.suspension (new) | contract_id, cause_id, date_start, date_end, doc_ref | m2o/m2o/date/date/char | one row per suspension episode; contract stays open (no termination flows) | FR-332, FR-333 |
| l10n_hn.ct.sickness.band (new) | tenure_from, tenure_to, pay_days, pay_unit, pay_fraction, valid_from | int/int/select/float/date | rows: 3-6m → 1 month @0.5; >6-9m → 2 months @0.5; >9m → 3 months @0.5; >5y → 30 days/year @1.0 (verbatim no-half qualifier, OQ-003); all valid_from the 1959 regime row | FR-335, FR-336 |
| hr.payslip | sickness_halfpay_days, sickness_halfpay_amount, coverage_flag | int/monetary/select | coverage: ihss_case · ct_non_covered · unknown (unknown pays nothing under either regime) | FR-334, FR-338 |
| l10n_hn.ct.maternity.leave (new) | worker_id, contract_id, partum_date, probable_partum_date, rest_pre_start, rest_post_end, base_kind, base_amount, retribution_daily, subsidy_daily, complement_daily | m2o/date/select/monetary | base_kind: fixed_180d_avg · variable_last_year_avg; subsidy_daily IMPORTED by id from file 04; rest calendar separate from the file-04 subsidy calendar | FR-339..FR-342 |
| l10n_hn.ct.maternity.aborto (new) | leave_id, weeks_certified (2-4), salary_at_start | m2o/int/monetary | paid at salary at moment rest began; no averaging | FR-343 |
| hr.payslip (lactancia lines) | lactancia_minutes, lactancia_hour_value | int/monetary | hour value = period salary ÷ hours actually worked; 2×30 min/day to child age 6 months | FR-344 |
| hr.contract / hr.employee (minor guards) | birth_date (derived), minor_max_daily_hours (6), minor_max_weekly_hours (30), diurnal_only, sunday_waiver_blocked (<16), intermediate_rest_hours (2, women/minors) | date/int/boolean | emitted to jornada validation (file 06 by range); age resolved per schedule/payslip date | FR-345..FR-348 |
| hr.contract (doméstico) | domestic_worker, prueba_days (15 presumed), preaviso_variant, cash_only_base | boolean/int/select/boolean | preaviso_variant rows: <1y → 7 days; ≥1y → 1 month; in-lieu = corresponding amount; cash-only excludes in-kind | FR-349..FR-352 |
| hr.payslip (doméstico settlement) | illness_indemnity_months, illness_indemnity_cap (4m), nonpayment_indemnity (7d/1m) | int/monetary | fraction ≥3 months counts as a year; cash base | FR-353, FR-354 |
| l10n_hn.ct.riesgo.case (new) | worker_id, risk_date, base_kind, base_daily, smm_floor_row, coverage, scale_blocked | m2o/date/select/monetary/m2o | base_kind: date_salary · obra_month_avg · obra_week_fallback; smm_floor_row → file-01 SMM row (rama×band) resolved at risk date (NEVER promedio); coverage: ihss · residual; scale_blocked true pending OQ-002 | FR-355..FR-357 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these FRs
touch the thin-client/SaaS architecture split (no electronic-invoicing-like
surface exists for labor-law status in the corpus). Model names stable
across Odoo 17/18/19/20 (hr.contract, hr.payslip, hr.salary.rule, hr.leave,
hr.work.entry); version-specific behavior recorded per row where a legal
vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-331 | odoo | l10n_hn.ct.regime | dated provenance row | Version regime (D12): consolidation pinned through D.278-2013, valid_from 1959-07; R-H57 guard encoded as a never-implement list keyed to `85_`; D15/D16: regime row selection by suspension/rest/risk date |
| FR-332..FR-334 | odoo | l10n_hn.ct.suspension.cause + l10n_hn.ct.suspension + hr.contract | status catalog + episode rows | Cause 8 sub-routing (maternity here; vacaciones → file 07); payslip generation reads suspension days from work entries; no termination side-effects (FR-333 guard on the hr.contract state machine) |
| FR-335, FR-336 | odoo | l10n_hn.ct.sickness.band + hr.payslip (salary rule MEDIO_SALARIO_ENFERMEDAD) | dated band rows | D12: bands valid from the 1959 regime row, additive-only; D-H3(a): tenure from hire-date monthly aggregates; >5y branch at 1.0 fraction per verbatim (OQ-003) |
| FR-337 | odoo | l10n_hn.ct.suspension (sickness) + activity/flag | trigger at 6 months | Flag-only interface to file 08 termination surfaces (by range); no auto-termination |
| FR-338 | odoo | hr.payslip coverage resolver | precedence layering | Consumes file 04 HN-PAYR-FR-150..153 case ledger by id; unknown coverage = blocked flag (OQ-004); no rate mixing between regimes |
| FR-339..FR-341 | odoo | hr.leave (maternity) + l10n_hn.ct.maternity.leave + hr.payslip rules | 4+6w paid rest + top-up | Base snapshot-on-write (D15); retro recomputes with ORIGINAL-period aggregates (D16); subsidy_daily imported from file 04 — never restated |
| FR-342 | odoo | l10n_hn.ct.maternity.leave (calendar pair + bridge compute) | reconciliation | TWO calendar fields never merged; day-by-day bridge complement; excess-beyond-42+42 hooks the file 04 FR-157 interface |
| FR-343, FR-344 | odoo | hr.leave (aborto) + hr.payslip lactancia lines | band leave + paid breaks | Aborto 2-4w at salary-at-start (no averaging); lactancia hourly value = period salary ÷ hours actually worked |
| FR-345..FR-348 | odoo | hr.employee + hr.contract constraints | age-keyed guards | Validation emitted to file 06 jornada engine (by range); age resolved per schedule/payslip date (D-H2); <14 hard block at contract create |
| FR-349..FR-352 | odoo | hr.contract (doméstico template) + hr.salary.rule | sub-regime parameters | 1-per-6 rest accrual; 15d presumed prueba; preaviso 7d/1m + in-lieu; cash-only base flag (inverse of file 10 in-kind rule) |
| FR-353, FR-354 | odoo | hr.payslip settlement lines | Art. 163/160 indemnities | Fraction ≥3m counts as a year; cap 4 months; cash base; computed only on file 08 termination-chassis events |
| FR-355..FR-357 | odoo | l10n_hn.ct.riesgo.case | residual base + gap flag | IHSS-first routing (files 03/04 by id); floor consumes file 01 SMM rama×band row AT THE RISK DATE (never promedio); scale_blocked = true pending OQ-002 (never-guess) |

Version-regime notes (D12): FR-331 records the 86_ consolidation vintage
(1959 → pinned D.278-2013) as the regime boundary for every statutory row
of this file — no adaptation windows exist in the instrument. FR-335/336
band rows and FR-349..354 doméstico parameters are 1959-vintage constants
carried on that regime row. FR-342's reconciliation depends on the RIT
regime row of file 04 (`valid_from` 2020-07-29): episodes before that date
resolve against the predecessor IHSS regime rows owned there, never against
RIT semantics. FR-356 floor rows ride the SMM bienio cycle (mid-year
changes possible; the floor re-resolves per risk date, file 01-owned
rows).

## 6. Acceptance Criteria

- **AC-001:** Given a contract with a suspension record of cause 8
  (pre/post-natal rest), then the contract registry shows the contract OPEN
  under suspension (no termination date, no final-settlement trigger, no
  preaviso/cesantía computation), and the payslip for suspension days emits
  no ordinary salary lines but does emit the FR-339 maternity-rest
  retribution lines (FR-332..FR-334).
- **AC-002:** Given a non-IHSS-covered sickness suspension of a worker with
  7 months of continuous service and monthly salary L15,000.00, then the
  ">6 and <9 months" band applies and the payslip shows half salary
  L7,500.00 for each of 2 months (FR-335).
- **AC-003:** Given a non-IHSS-covered sickness suspension of a worker
  with 6 years of continuous service and monthly salary L15,000.00 (daily
  L500.00 = 15,000 ÷ 30), then the >5-years branch pays 30 × 6 = 180 days
  of salary = L90,000.00 at the encoded 1.0 fraction (OQ-003) (FR-336).
- **AC-004:** Given day 5 of an IHSS-covered incapacidad case, then the
  payslip shows FULL salary via the file-04 cost-split (subsidy offset +
  complement) and the CT half-pay line = L0.00 for that day; given the
  same calendar day for a non-affiliated worker, then the CT half-pay line
  pays 50%; given a day whose coverage state is `unknown`, then both lines
  are L0.00 and the blocked-coverage flag is raised (FR-338).
- **AC-005:** Given a sickness suspension that reaches its 6-month
  anniversary, then the terminate-after-6-months flag is emitted to the
  termination surface and NO termination or payout occurs from the flag
  alone (FR-337).
- **AC-006:** Given a fixed-salary worker earning L10,000.00/month whose
  last-180-day salaries are 6 × L10,000.00, then the 180-day average base
  = L10,000.00/month, the daily retribution = L333.33 (10,000 ÷ 30), and
  given an imported IHSS subsidy of L200.00/day the employer complement =
  L133.33/day; given IHSS not obliged for the same worker, then the
  employer pays the full L333.33/day (FR-340, FR-341).
- **AC-007:** Given birth on 2026-03-10 equal to the probable-partum date,
  then the IHSS prenatal reposo runs 2026-01-28..2026-03-10 (42 días
  calendario including the partum, file-04 calendar) while the CT prenatal
  rest runs 2026-02-11..2026-03-10 (4 weeks) — the 14-day interstice
  2026-01-28..2026-02-10 is paid under the file-04 subsidy + RIT Art. 73
  ¶2 complement, NOT as CT rest — and both postnatal windows end
  2026-04-20 (42 days); the system never emits a merged 84-day calendar
  (FR-342).
- **AC-008:** Given a certified *aborto* rest of 2 weeks for a worker
  earning L9,600.00/month at the moment the rest began, then the leave
  pays the salary-at-start with no averaging: 14 days × L320.00
  (9,600 ÷ 30, the file-01 jornada convention) = L4,480.00; a certification
  outside the 2-4-week band is rejected (FR-343).
- **AC-009:** Given a nursing worker with period salary L9,000.00 and 160
  hours actually worked in the period, then the lactancia hour value =
  L56.25 and the 2×30-minute daily breaks pay L56.25/day with NO deduction,
  until the child completes 6 months of age (FR-344).
- **AC-010:** Given a 15-year-old worker scheduled 8 diurnal hours, then
  jornada validation blocks the schedule (cap 6h/30h diurnal-only); given a
  Sunday-rest waiver configured for the same worker, then the waiver is
  rejected (<16 non-waivable); given a woman worker's calendar without a
  2-hour intermediate rest, then validation blocks it; given a hire dated
  at age 13, then contract creation fails outright (FR-345..FR-348).
- **AC-011:** Given a doméstico with 2.5 years of service, cash salary
  L6,000.00 and in-kind benefits valued L2,000.00, then the preaviso = 1
  month on L6,000.00 (cash-only base; in-kind excluded) and the Art. 163
  indemnity = 3 months (2 years + one fraction ≥3 months) × L6,000.00 =
  L18,000.00 ≤ the 4-month cap; given 5 years of service, then 5 months
  compute and the payment caps at 4 × L6,000.00 = L24,000.00
  (FR-351..FR-353).
- **AC-012:** Given a residual (non-IHSS-covered) riesgo case of a
  salaried worker earning L500.00/day at the risk date, then the base =
  L500.00; given an obra worker whose last-month earnings average
  L400.00/day and an applicable file-01 SMM jornada row of L428.97 at the
  risk date, then the floored base = L428.97 (never the promedio row); and
  given no Título V scale row loaded, then the indemnity amount is blocked
  with the config-gap flag (FR-355..FR-357).
- **AC-013:** Given the registry question "is CT Art. 417 derogated by
  D.93-2021?", then the system answers NO — CT Art. 417 is live, the
  D.93-2021 "417" is a Código Penal article, and no dead-list entry from
  `85_` attaches to any CT article of this file (FR-331, FR-355).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `EV85:86_ OQ-1` carried: the 86_ consolidation is pinned only through D.278-2013 (fn.36); any CT reform 2014-2026 silently absent from the CEDIJ print would be missing — verify the target families (suspension 99-105, maternity 135-146, minors 130-132/338, domésticos 154-163, riesgo 417-418) against an official current consolidation before treating the quotes as current law (D.117-2021-style post-2013 instruments; FR-331 regime row carries the flag). | no | Takumi S-HN4 + acquisition queue | open |
| OQ-002 | `EV85:86_ OQ-8` carried: riesgo profesional is IHSS-first — files 03/04 implement the covered side; CT Art. 417 base applies only to non-covered residual cases (FR-355). Residual open: the Título V disability-grade indemnity SCALE (percentages/durations) is not in the extracted corpus — FR-357 blocks residual amounts until acquired (lead: full CT Título V text + any IHSS-era supersession analysis). | no | acquisition queue | open |
| OQ-003 | Art. 104 drafting nuance: rules 1-3 expressly pay *medio salario*, rule 4 (>5 years) pays "treinta (30) días de salario por cada año de servicio" with no half qualifier — FR-336 encodes the verbatim full-salary reading; confirm against STSS/consultor practice (and whether rule 4 caps or replaces the 1/2/3-month payments) before freezing the band rows. | no | Takumi S-HN4 | open |
| OQ-004 | Coverage-unknown sickness days (FR-338(c)): the corpus fixes no rule for days whose IHSS coverage state cannot be resolved — encoded as pay-nothing + blocked flag; decide the operational default resolution workflow (IHSS ledger backfill vs manual ruling) with file 04's config family owners. | no | Takumi S-HN4 | open |
| OQ-005 | Art. 100 numerals 2-6 and 10 are quoted only in elision («…») in the evidence file — the FR-332 catalog seeds them from the same article marked `evid_elided`; transcribe the full texts verbatim on acquisition of a clean CT print and drop the flag. | no | acquisition queue | open |
