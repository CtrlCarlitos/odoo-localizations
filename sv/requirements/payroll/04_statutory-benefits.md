# SV — Payroll — Statutory benefits: vacaciones, aguinaldo and Quincena Veinticinco (labor computation + by-reference interfaces)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the statutory annual benefits of Salvadoran labor
law: the *vacaciones* (annual vacation) engine of Código de
Trabajo (Labor Code, CT) Arts. 177-189 — 15 days after one year of
continuous work remunerated at the ordinary salary of the period PLUS
a 30% surcharge (Art. 177), the non-extension rules for
asuetos/rest/compensatory days (178), anniversary-year accounting
(179), the 200-worked-days accreditation gate (180) with the
suspension-preserves-continuity-but-not-worked-days rule (181),
employer scheduling with ≥30-day notice and the 4-month (≤100
workers) / 6-month (>100 workers) take windows (182), the base
derivation of Art. 183 (current *salario básico* for time pay;
six-month ÷ *días laborables* for other forms), the +25% lodging and
+25% food additions (184), the pay-immediately-before-starting rule
(185), termination proration with the completed-year-full-pay
regardless-of-responsibility rule (187), and the cash-compensation
prohibition with the collective-vacation and fractional-enjoyment
schemes (188-189); and the *aguinaldo* (statutory year-end bonus)
engine of Arts. 196-203 — the annual prima with seniority tiers of
15/19/21 days (1-<3y / 3-<10y / ≥10y, Art. 198), proportional payment
for workers under one year at 12-December (197), the Art. 199 base,
the 12-20 December payment window (200), the no-disciplinary-
forfeiture invariant (201), termination proration before 12-December
(202) and the justifiable-absence days that count as worked (203);
and the *Quincena Veinticinco* (special-law annual complement)
engine of Ley Especial Quincena Veinticinco, D.L. 499 (effective
14-ene-2026) — the annual complementary income paid inside the
15–25 January window at 50% of the monthly *salario básico o
nominal* perceived at materialization, gated to a monthly salario
básico o nominal of ≤ US$1,500.00 (Arts. 1-2), eligibility
MIRRORED from the aguinaldo / compensación-adicional-en-efectivo
requirements of each sector regime (the Art. 2 cross-reference —
requirements mirrored, the benefit never equated; §3.2 consumed by
reference), the termination proportional right (Art. 3 [printed
"Art. 5" — sic]), the 2026 public-mandatory / private-voluntary
transitory split becoming mandatory for ALL employers from 2027
(Art. 6), and the paid-in-full invariants — no retention of any
kind, no SS/pension cotización, never a calculation base of
another prestación, *inembargable* (Arts. 1/4).
The file also records the ISR/IBC/*salario* interfaces — strictly BY
REFERENCE: the exento/gravado split and vintages (taxation/04
SV-TAX-FR-120), the extraordinary-remuneration aggregation and
June/December *recálculo* interplay (SV-TAX-FR-116/110/111) and the
canonical classification rows (Task 1's matrix
`01_salary-model.md` SV-PAY-FR-004) — payroll supplies the GROSS
prima and the seniority tiers and never re-derives taxation.

It does **not** cover: the *salario* / *salario básico* model and the
canonical earning-category matrix (`01_salary-model.md` — the stored
rates of FR-005, the SB-R7 six-month derivation of FR-006 and the
matrix row classification are consumed by id, never restated); the
SMM chassis and dated tariff tables (`02_minimum-wage.md` — the
sidecar `smm_2025.csv` owns the comercio-y-servicios row feeding the
2-SMM aguinaldo floor, loaded per its FR-011 and pinned per its
FR-022); jornada, surcharges, *descanso semanal* and asuetos
(`03_working-time-surcharges.md`); social-security rates, caps and
the IBC computation itself (`05_social-security-contributions.md`);
SS declaration/remittance (`06_ss-declaration-remittance.md`);
contracts, termination and *indemnización* (`07_contracts-termination.md`
— owns the termination-flow mechanics this file's prorations plug
into); the ISR retention computation (owned by
`taxation/04_isr-withholding.md`); and the F-14 column model (owned
by `fiscal-reporting/06_f14-declaration.md`).

## 2. Legal Basis

Authority order (binding, per master evidence index S4): labor = 11_
(Código de Trabajo, D.L. 15-1972, Índice Legislativo edition, reform
stamps (1)-(22) — SOQ-21/OQ watch); pensions interface = 09_ (Ley
Integral del Sistema de Pensiones, D.L. 614); ISR interface anchors
consumed from the S2 files by FR id (54_ Ley ISR / 53_ D.E. 10-2025);
SMM feed consumed from `02_minimum-wage.md`'s sidecar by FR id (16_
Decreto 11-2025); Quincena Veinticinco = 66_ (Ley Especial Quincena
Veinticinco, D.L. 499, D.O. N° 8 T.450 14-ene-2026 — the law,
current, effective on publication 14-ene-2026; official DGII OCR'd
copy — LB quotes reproduce its print).

W17 75_ fold-in: one historical-corroboration row (LB-029) cites the
Reglamento de Aplicación del Código Tributario (D.E. N° 117-2001,
D.O. N° 234 T.353 11-dic-2001; source `75_`) as printed — vintage-note
rule: the 75_ print carries NO REFORMAS block (EV75 OQ-1) and
post-2001 repeal by CT Art. 344 ff is print-unresolvable (OQ-8,
SOQ-06-kin), so the row is cited as printed with the watch note;
procedure-layer corroboration only, no FR attaches (R22 and the S2
files govern current substance).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Trabajo, Art. 177: "Después de un año de trabajo continuo ... derecho a un período de vacaciones cuya duración será de quince días, los cuales serán remunerados con una prestación equivalente al salario ordinario correspondiente a dicho lapso más un 30% del mismo." | After one year of continuous work the worker is entitled to a vacation period of fifteen days, remunerated with a prestación equal to the ordinary salary corresponding to that period PLUS 30% of it | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 177, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-002 | Código de Trabajo, Art. 178: asuetos and descansos falling inside the vacation period do not extend it; the vacation period cannot start on them; compensatory days are excluded | Holidays/weekly-rest days inside the vacation period do not extend it and the period may not begin on such a day; compensatory rest days are excluded from the count | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 178, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-003 | Código de Trabajo, Art. 179: the vacation year runs from the start date of the contract, in anniversary years | Anniversary accounting: the qualifying year is measured from the contract start date, by anniversaries | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 179, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-004 | Código de Trabajo, Art. 180: the worker "deberá acreditar un mínimo de doscientos días trabajados en el año" | 200-worked-days gate: the worker must accredit a minimum of two hundred worked days in the (anniversary) year | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 180, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-005 | Código de Trabajo, Art. 181: suspension preserves the continuity of the contract year, but suspension days do not count as worked days | Continuity rule: suspension leaves (illness, maternity, contract-suspension causes) do NOT break the one-year continuity, but their days are not worked days for the 200-day accreditation | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 181, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-006 | Código de Trabajo, Art. 182: the employer schedules vacations with notice of at least thirty days; the worker must take them within four months of qualifying (enterprises with up to one hundred workers) / six months (more than one hundred workers) | Employer scheduling: ≥30-day notice; the vacation must be taken within 4 months of qualifying when the enterprise has ≤100 workers, 6 months when >100 | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 182, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-007 | Código de Trabajo, Art. 183: vacation base = the current salario básico (time-unit pay) or the ordinary salaries of the last six months ÷ días laborables (other pay forms) | Vacation base: current *salario básico* for time pay; for other pay forms, last-six-months ordinary salaries divided by working days of that window | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 183, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-008 | Código de Trabajo, Art. 184: when the worker receives lodging or food from the employer and that benefit is interrupted during the vacation, the vacation pay increases by twenty-five percent for each interrupted benefit | +25% vacation-pay addition for EACH of lodging and food interrupted during the vacation (both interrupted ⇒ +50%) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 184, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-009 | Código de Trabajo, Art. 185: the vacation prestación shall be paid "inmediatamente antes de que el trabajador empiece a gozarlas", covering all days until return | The vacation prestación is paid IMMEDIATELY BEFORE the worker starts enjoying the period, covering every day up to return | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 185, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-010 | Código de Trabajo, Art. 187: proportional vacation pay on termination with employer responsibility or despacho de hecho; a worker who has completed the qualifying year receives the full vacation pay regardless of whose responsibility the termination is | Termination proration: proportional payment when the termination is the employer's responsibility or a de-facto dismissal (despacho de hecho); completed year ⇒ FULL vacation pay regardless of responsibility | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 187, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-011 | Código de Trabajo, Art. 188: "Se prohíbe compensar las vacaciones en dinero o en especie. Asimismo se prohíbe fraccionar o acumular los períodos de vacaciones." | Cash-or-in-kind compensation of vacations is PROHIBITED; fractioning and accumulation of vacation periods are equally prohibited | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 188, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-012 | Código de Trabajo, Art. 189: collective vacation possible (waiving the one-year and 200-day requirements); by majority agreement the period may be fractioned: into two periods of not less than ten days each, or into three or more periods of not less than seven days each | Collective-vacation exception (gates waived) and the fractional-enjoyment schemes by majority agreement: exactly 2 periods ≥10 days each, or ≥3 periods ≥7 days each | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 189, Arts. 177-189 pp.41-42 (EVID-204) |
| LB-013 | Código de Trabajo, Art. 196: the employer is obliged to give, in the concept of aguinaldo, "una prima por cada año de trabajo" | Aguinaldo obligation: a prima for each year of work | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 196, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-014 | Código de Trabajo, Art. 197: full prima with one year or more of service; "Los trabajadores que al día doce de diciembre no tuvieren un año de servir a un mismo patrono, tendrán derecho a que se les pague la parte proporcional al tiempo laborado de la cantidad que les habría correspondido si hubieren completado un año de servicios a la fecha indicada." | Full prima at ≥1 year; workers who at 12-December have under one year with the same employer receive the part PROPORTIONAL to the time worked of the amount that would have corresponded had they completed one year at that date | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 197, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-015 | Código de Trabajo, Art. 198 (stamps (4)(14)): "LA CANTIDAD MÍNIMA QUE DEBERÁ PAGARSE ... SERÁ: 1º PARA QUIEN TUVIERE UN AÑO Y MENOS DE TRES AÑOS DE SERVICIO, LA PRESTACIÓN EQUIVALENTE AL SALARIO DE QUINCE DÍAS; 2º PARA QUIEN TUVIERE TRES AÑOS O MÁS Y MENOS DE DIEZ AÑOS ... DIECINUEVE DÍAS; y, 3º PARA QUIEN TUVIERE DIEZ O MÁS AÑOS ... VEINTIÚN DÍAS." | MINIMUM aguinaldo amounts by seniority: 1 to <3 years = 15 days' salary; 3 to <10 years = 19 days; 10 or more years = 21 days (floors — "la cantidad mínima", configurable upward) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 198, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-016 | Código de Trabajo, Art. 199: aguinaldo base = the current salario básico (time-unit pay) / the ordinary salaries of the last six months ÷ días laborables (other pay forms) | Aguinaldo base: current *salario básico* for time pay; last-six-months ordinary salaries ÷ working days for other forms (same structure as Art. 183) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 199, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-017 | Código de Trabajo, Art. 200: the aguinaldo "deberá pagarse en el lapso comprendido entre el doce y el veinte de diciembre de cada año." | Payment window: the aguinaldo must be paid between 12 and 20 December of each year | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 200, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-018 | Código de Trabajo, Art. 201 (stamp (22)): "NINGÚN TRABAJADOR O TRABAJADORA PERDERÁ EL DERECHO AL AGUINALDO POR RAZONES DISCIPLINARIAS, INASISTENCIAS INJUSTIFICADAS AL TRABAJO O CUALQUIER OTRA CAUSA." | No worker loses the aguinaldo right for disciplinary reasons, unjustified absences from work, or ANY other cause — the no-forfeiture invariant | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 201, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-019 | Código de Trabajo, Art. 202: proportional aguinaldo on termination with employer responsibility / despacho de hecho before December 12 | Termination proration: before 12-December, a termination with employer responsibility or de-facto dismissal pays the proportional aguinaldo for the time worked | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 202, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-020 | Código de Trabajo, Art. 203: the following absences count as worked days — vacations, licenses, disciplinary suspension, the contract-suspension causes, fortuitous-case or force-majeure absences; detention-sanction absences do NOT count | Justifiable absences count as worked days for the aguinaldo computation; absences owed to a detention sanction are excluded from the count | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 203, Arts. 196-203 pp.43-44 (EVID-206) |
| LB-021 | Ley Integral del Sistema de Pensiones (D.L. 614), Art. 14: IBC = money retribution for ordinary services "incluido el período de vacaciones, comisiones y porcentajes sobre ventas"; "No forman parte del Ingreso Base de Cotización ... b) El aguinaldo. c) Viáticos, gastos de representación y prestaciones sociales establecidas por la ley." — interface anchor only; the classification matrix is OWNED by `01_salary-model.md` SV-PAY-FR-004 and consumed by reference | IBC interface: vacation period is an EXPRESS inclusion in the contribution base; the aguinaldo is an EXPRESS exclusion (Art. 14 b); legal social benefits are excluded (14 c) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 14 pp.6-7 (EVID-197; via 01 FR-004 matrix) |
| LB-022 | Código de Trabajo, Art. 119 (final clause): "ni tampoco las prestaciones sociales de que trata este Código" constitute salario — interface anchor only; the matrix is OWNED by `01_salary-model.md` SV-PAY-FR-004 and consumed by reference | Salario interface: the CT statutory social benefits (vacaciones, aguinaldo among them) are NOT *salario* for CT purposes — the CT exclusion never propagates to the ISR base, which uses its own remuneraciones-gravadas concept | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 119 p.31 (EVID-201/204; via 01 FR-004 matrix) |
| LB-023 | Ley ISR, Art. 4 num. 16 + D.E. 10-2025, Arts. 1 f)/g): aguinaldo exempt up to TWO SMM of the commerce-and-services sector, excess retained DEDUCTING the floor (stamp (23) = D.L. 458-2019; R22 — vintages 2014-2018 full exemption, 2021 $1,100, 2022-2024 $1,500, 2025+ standing 2-SMM); aguinaldo = extraordinary remuneration aggregated per Art. 1 g) and entering the June/December recálculo per Art. 1 f) — interface anchors OWNED by `taxation/04_isr-withholding.md` (SV-TAX-FR-120 split/vintages; SV-TAX-FR-116 aggregation; SV-TAX-FR-110/111 recálculo) and consumed by reference | ISR interface by reference: the exento/gravado split, the retention vintages and the recálculo mechanics are taxation-owned; this file supplies only the gross prima and the payment date | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` + `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 4.16 p.7 (EVID-165); Arts. 1 f)/g) (EVID-158/159; via taxation/04 LB-004/LB-010/LB-011) |
| LB-024 | Decreto 11-2025, Art. 2, comercio y servicios sector row (monthly SMM $408.80, valid_from 2025-06-01) — interface anchor only; the dated VALUE is OWNED by `02_minimum-wage.md`'s sidecar `smm_2025.csv` (loaded per its SV-PAY-FR-011; sector pinning per its SV-PAY-FR-022) and consumed by reference, never restated as a constant of this file | The 2-SMM aguinaldo floor's SMM value is dated data from the Task-2 sidecar row (floor 2 × $408.80 = US$817.60 while that vintage is operative); re-seeded per SMM decree | `sv/sources/16_Salarios_Minimos_2025.pdf` | Art. 2 p.20 (EVID-191; via 02 smm_2025.csv) |
| LB-025 | Ley Especial Quincena Veinticinco (D.L. 499), Art. 1: "'Quincena Veinticinco' ... consiste en un ingreso complementario, que deberá pagarse entre el quince y el veinticinco de enero de cada año, a partir del año dos mil veintisiete, a todos los servidores públicos, personal civil o militar al servicio de la Administración Pública, a los empleados municipales, así como a los empleados y trabajadores del sector privado. La Quincena Veinticinco es un beneficio económico de carácter especial que debe ser pagado de forma integra y sin ningún descuento a los sujetos beneficiados, independiente del salario ordinario, aguinaldo, compensación adicional en efectivo y de otras prestaciones laborales... y no formará parte de la base de cálculo de otras prestaciones, por lo que no sera objeto de ninguna clase de retención. Consecuentemente, el ingreso complementario Quincena Veinticinco... en ningún caso deberá ser objeto de retención ni descuento alguno por concepto de aportes u otras obligaciones de Seguridad Social o del Régimen Previsional." | The Quincena Veinticinco is a complementary income paid between 15 and 25 January of each year from 2027, to ALL public servants, civil/military personnel of the Administración Pública, municipal employees and private-sector employees/workers; a special-character economic benefit paid IN FULL and without any discount, INDEPENDENT of ordinary salary, aguinaldo, compensación adicional en efectivo and other labor benefits; it never forms part of the calculation base of other prestaciones, is never subject to any retention, and in no case to retention nor deduction of any kind for SS or Régimen Previsional contributions | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 1, Arts. 1-3, 5-6 pp.2-6 (EVID-236) |
| LB-026 | Ley Especial Quincena Veinticinco, Art. 2: "La cantidad gue deberá pagarse en concepto de Quincena Veinticinco, será del cincuenta por ciento (50%) sobre el salario básico o nominal mensual que cada uno de los sujetos beneficiados esté percibiendo al momento en que la prestación se materialice... y solo será aplicable para aquellos trabajadores cuyo salario básico o nominal mensual sea igual o Inferior a mil quinientos dólares de los Estados Unidos de América." (elegibilidad = mismos requisitos que aguinaldo/compensación adicional en efectivo per sector regime, "sin que ello implique equiparar"; public sector + municipalities must be "laborando para la entidad pública correspondiente al momento de materializarse el pago"; special-regime institutions: Ley Compensación Adicional supletoria) | Quincena amount = 50% of the monthly *salario básico o nominal* each beneficiary is perceiving at the moment the prestación materializes, applicable ONLY to workers whose monthly salario básico o nominal is ≤ US$1,500.00 (the law's printed constant — its OWN base, not the CT 119 salario integrante); eligibility requirements = the SAME as the aguinaldo/CAE of the worker's sector regime ("without this implying an equation" — requirements mirrored, the benefit never equated); public-sector/municipal workers must be laborando for the corresponding entity at the moment of payment; special-regime institutions follow the Ley Compensación Adicional supletoria | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 2, Arts. 1-3, 5-6 pp.2-6 (EVID-236) |
| LB-027 | Ley Especial Quincena Veinticinco, Art. 3 [printed "Art. 5" — sic; positional attribution per the evidence OQ-1, carried as this file's OQ-006] (gloss-level per EVID-236): Condición especial — a worker terminated with employer responsibility or *despido de hecho* before or on 25-January retains the right to the benefit, proportional per the aguinaldo/CAE proportional rules | Termination before or on 25-January with employer responsibility or de-facto dismissal preserves a PROPORTIONAL right to the Quincena, computed per the aguinaldo / compensación-adicional-en-efectivo proportional rules (the §3.2 kin, consumed by reference) | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 3 [printed Art. 5], Arts. 1-3, 5-6 pp.2-6 (EVID-236) |
| LB-028 | Ley Especial Quincena Veinticinco, Art. 6 (transitory): public sector 2026 = mandatory (budget modifications); "En el caso del sector privado, para el año dos mil veintiséis, el pago de la Quincena Veinticinco... tendrá carácter voluntario para los patronos, debiendo realizarse en su caso, a mas tardar el veinticinco de enero de dos mil veintiséis. Los patronos que realicen voluntariamente el pago referido... tendrán derecho a un crédito tributario acreditable contra el pago del Impuesto sobre la Renta del ejercicio fiscal dos mil veintiséis, por el monto total pagado" | 2026 transitory split: public sector MANDATORY (budget modifications); private sector VOLUNTARY, any voluntary payment falling due at the latest 25-January-2026, voluntary payers earning a tax credit for the FULL amount paid against FY-2026 ISR (credit mechanics = taxation-owned, SV-TAX-FR-174 cited by id); from 2027 the payment is mandatory for ALL employers public and private (Art. 1) | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 6, Arts. 1-3, 5-6 pp.2-6 (EVID-236/237) |
| LB-029 | Reglamento de Aplicación del Código Tributario (D.E. N° 117-2001), Art. 95 final inciso (restates CT 155-II as of the 2001 print): "No obstante que los aguinaldos constituyen remuneraciones de carácter permanente gravados con el Impuesto sobre la Renta, no serán sujetos a retención toda vez que mediante Decreto Legislativo gocen de tal prerrogativa." — HISTORICAL CORROBORATION ONLY: the 2001-print restatement of CT 155 inc. 2's blanket no-retention; R22 GOVERNS current periods (Ley ISR Art. 4.16 standing 2-SMM exemption split + D.L. 458-2019 floor-deducted excess — vintages OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-120, consumed by reference); no FR attaches to this row (the ISR interface stays §3.3's, by id) | Historical layer: as of 2001 the aguinaldo was a gravada remuneración whose retention exemption depended on a Decreto Legislativo prerogative — corroborating the starting point of the vintage chain (2014-2018 full exemption); the blanket no-retention print never applies to current periods | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 95 p.60 (EVID-351; verified 75_ txt lines 3121-3123) |

Version regime (D12): NO dated data is owned by this file — the SMM
feed lives in `02_minimum-wage.md`'s `smm_2025.csv` (SV-PAY-FR-011,
re-seeded per SMM decree), and the aguinaldo exemption vintages live
in `taxation/04_isr-withholding.md` (SV-TAX-FR-120). The 15/19/21
tiers, the 30% surcharge, the 200-day gate, the scheduling windows,
the December window and every other value cited here are STATIC law
(CT Arts. 177-203); the CT text basis is the Índice Legislativo
edition (stamps through (22), no as-of date — SOQ-21 watch, kin of
file 01's OQ-001). Exception (S6): the Quincena-25 US$1,500.00 gate
is D.L. 499's printed constant (66_ Art. 2; EVID-236) and the
Quincena regime flag is configuration DATED BY EJERCICIO (2026
public-mandatory/private-voluntary split, 2027+ mandatory — 66_
Art. 6; FR-140); both are cited from 66_ (current, effective
14-ene-2026), never restated as undated constants of this file.

## 3. Functional Requirements

### 3.1 Vacaciones (CT Arts. 177-189)

- **SV-PAY-FR-044:** The system shall accrue for every worker, after
  one year of CONTINUOUS work, a vacation entitlement of FIFTEEN days
  remunerated with a prestación equal to the ordinary salary
  corresponding to that period PLUS 30% of it — computed as
  15 × daily base (FR-047) × 1.30 and emitted as ONE vacation-pay
  line carrying base + surcharge (the surcharge is a component of the
  single Art. 177 prestación, never a separate cash line —
  FR-052); the line classifies as *vacation pay* per the canonical
  matrix of `01_salary-model.md` SV-PAY-FR-004 (consumed by id).
  (LB-001; EVID-204)
- **SV-PAY-FR-045:** The system shall measure the vacation year in
  ANNIVERSARY years from the contract start date (Art. 179), and
  shall apply the Art. 178 non-extension rules: days of asueto,
  weekly rest and compensatory rest falling inside the vacation
  period do NOT extend it and are not counted as vacation days, and
  the vacation period may NOT start on any of them (start-date
  validation on the leave record); the fifteen days are counted per
  the day-count convention of OQ-001 (días laborables by default).
  (LB-002; LB-003; EVID-204)
- **SV-PAY-FR-046:** The system shall gate the Art. 177 entitlement
  on the 200-worked-days accreditation: the worker must accredit a
  MINIMUM of 200 WORKED days in the anniversary year (Art. 180);
  suspension leaves (illness, maternity, contract-suspension causes)
  PRESERVE the one-year continuity but their days are NOT worked
  days for the count (Art. 181); whether justifiable non-worked days
  count toward the 200 is corpus-silent (Art. 203 is
  aguinaldo-chapter express) — strict worked days by default
  (OQ-002); the per-year worked-days counter and the
  qualified/deferred status are stored on the vacation period
  record. (LB-004; LB-005; EVID-204)
- **SV-PAY-FR-047:** The system shall derive the vacation daily base
  per Art. 183 WITHOUT re-derivation: (a) time-unit pay — the
  CURRENT stored daily *salario básico* of `01_salary-model.md`
  SV-PAY-FR-005; (b) commission and other variable forms — the SB-R7
  six-month derivation (last-six-months ordinary salaries ÷
  *días laborables*) of `01_salary-model.md` SV-PAY-FR-006 (the rule
  Art. 183 invokes, consumed by id); (c) SMM-level workers — the
  max-rule base of `02_minimum-wage.md` SV-PAY-FR-021
  (max(actual daily salary, sector daily SMM)); the base at
  computation time is the CURRENT rate, not the hire-date rate.
  (LB-007; EVID-204)
- **SV-PAY-FR-048:** The system shall schedule vacations as an
  EMPLOYER decision recorded with an advance notice of at least
  THIRTY days to the worker (notice date stored), and shall enforce
  the take-windows: the vacation must be enjoyed within FOUR months
  of qualifying when the enterprise employs up to one hundred
  workers, and within SIX months when it employs more than one
  hundred — the window deadline is computed per enterprise size and
  an unenjoyed expired window raises a compliance flag (no payslip
  computation is altered by the flag). (LB-006; EVID-204)
- **SV-PAY-FR-049:** The system shall increase the vacation
  prestación by TWENTY-FIVE PERCENT for EACH of lodging and food the
  employer provides and which is interrupted during the vacation
  (both interrupted ⇒ +50% over the Art. 177 prestación) — gated on
  per-worker records of employer-provided lodging/food and of the
  interruption during the period; the additions are components of
  the vacation-pay line (FR-044), not separate prestaciones.
  (LB-008; EVID-204)
- **SV-PAY-FR-050:** The system shall pay the vacation prestación
  (Art. 177 quantum + Art. 184 additions) IMMEDIATELY BEFORE the
  worker starts enjoying the period, covering ALL days of the period
  up to return — the payslip is dated no later than the vacation
  start date; a vacation-pay line dated after the period start is a
  compliance finding (late payment), never silently accepted.
  (LB-009; EVID-204)
- **SV-PAY-FR-051:** The system shall pay, on termination with
  EMPLOYER responsibility or *despacho de hecho* (de-facto dismissal
  — the Art. 55 presumption family owned by
  `07_contracts-termination.md`), the vacation pay PROPORTIONAL to
  the time worked since the last qualifying anniversary (Art. 187);
  and shall pay a worker who has COMPLETED a qualifying year the
  FULL vacation prestación REGARDLESS of whose responsibility the
  termination is; termination proration and the completed-year
  full-pay rule are the ONLY exceptions under which a vacation
  prestacion is paid outside an enjoyed vacation period (see
  FR-052). (LB-010; EVID-204)
- **SV-PAY-FR-052:** The system shall enforce the Art. 188
  prohibitions as payroll invariants: NO compensation of vacations
  in money or in kind, and NO fractioning or accumulation of vacation
  periods — no vacation-pay line may exist without an attached
  enjoyed vacation period, except the Art. 187 termination payments
  of FR-051; and shall support the Art. 189 exceptions as recorded
  agreements: (a) COLLECTIVE vacation (enterprise-closure vacation by
  majority agreement), which WAIVES the one-year-continuous and
  200-day gates of FR-044/FR-046, and (b) FRACTIONAL enjoyment by
  majority agreement, validated as exactly two periods of not less
  than TEN days each, or three or more periods of not less than
  SEVEN days each. (LB-011; LB-012; EVID-204)

### 3.2 Aguinaldo (CT Arts. 196-203)

- **SV-PAY-FR-053:** The system shall compute for every worker an
  annual aguinaldo prima per year of work (Art. 196) with the
  seniority-tier MINIMUM quantities of Art. 198 (stamps (4)(14)):
  one year and less than three years of service = the prestación
  equivalent to FIFTEEN days' salary; three years or more and less
  than ten = NINETEEN days; ten years or more = TWENTY-ONE days —
  quantum = daily base (FR-055) × tier days; seniority is measured
  at the payment date (an anniversary falling inside the payment
  window flips the tier — OQ-003 records the Dec-12-alternative
  reading); "la cantidad mínima" makes each tier a FLOOR
  (configurable upward, never below). (LB-013; LB-015; EVID-206)
- **SV-PAY-FR-054:** The system shall pay workers who at
  12-DECEMBER have less than one year serving the same employer the
  PART PROPORTIONAL to the time worked of the amount that would have
  corresponded had they completed one year at that date (Art. 197) —
  quantum = (worked days since hire, counting the Art. 203
  justifiable days of FR-059 ÷ year denominator) × 15 × daily base,
  with the would-have-completed tier being the 1-<3y 15-day tier and
  the denominator defaulted to 365 days (corpus-silent — OQ-004);
  the measurement date is 12-December while the payment runs in the
  Art. 200 window (FR-056). (LB-014; EVID-206)
- **SV-PAY-FR-055:** The system shall derive the aguinaldo daily
  base per Art. 199 with the SAME structure as the vacation base,
  without re-derivation: (a) time-unit pay — the CURRENT stored
  daily *salario básico* (`01_salary-model.md` SV-PAY-FR-005);
  (b) commission and other variable forms — the SB-R7 six-month
  derivation of `01_salary-model.md` SV-PAY-FR-006; (c) SMM-level
  workers — the max-rule base of `02_minimum-wage.md`
  SV-PAY-FR-021. (LB-016; EVID-206)
- **SV-PAY-FR-056:** The system shall pay the aguinaldo inside the
  ANNUAL WINDOW of 12 through 20 December (Art. 200) — aguinaldo
  payment lines dated outside the window raise a compliance flag,
  with the single exception of the Art. 202 termination prorations
  of FR-058 (paid at termination, whatever the date); the window is
  a payment-timing rule only and never alters the quantum.
  (LB-017; EVID-206)
- **SV-PAY-FR-057:** The system shall implement the
  no-disciplinary-forfeiture invariant of Art. 201 (stamp (22)): NO
  worker loses the aguinaldo right for disciplinary reasons,
  unjustified absences or ANY other cause — the gross prima of
  FR-053/FR-054/FR-058 computes independent of disciplinary records
  and absence justification, and NO deduction, netting, conditioning
  or forfeiture line may attach to the aguinaldo prestación
  (contrasting with the séptimo-día loss rule of
  `03_working-time-surcharges.md` FR-032, which the stamp-(22)
  reform left untouched for weekly rest). (LB-018; EVID-206)
- **SV-PAY-FR-058:** The system shall pay, on termination with
  EMPLOYER responsibility or *despacho de hecho* occurring BEFORE
  12-December, the PROPORTIONAL aguinaldo for the time worked in the
  calendar year (Art. 202) — same mechanics as FR-054 (worked days
  counting Art. 203 justifiable days ÷ denominator × 15 × daily
  base), paid at termination as the FR-056 window exception; a
  worker still employed at 12-December takes the Art. 197
  proportional right of FR-054 instead. (LB-019; EVID-206)
- **SV-PAY-FR-059:** The system shall count as WORKED days, for the
  aguinaldo computations (FR-053 seniority continuity, FR-054/FR-058
  proportional numerators), the days of: enjoyed vacations; legal
  licenses; disciplinary suspension; the CT contract-suspension
  causes; and fortuitous-case or force-majeure absences (Art. 203);
  days of absence owed to a DETENTION SANCTION do NOT count (the
  countable-day flags live on the absence/leave records of the
  working-time model). (LB-020; EVID-206)

### 3.3 ISR / IBC / salario interfaces (by reference only)

- **SV-PAY-FR-060:** The system shall supply to the ISR layer the
  GROSS aguinaldo prima (FR-053/FR-054/FR-058) and NOTHING ELSE: the
  exento/gravado split and its vintages are OWNED by
  `taxation/04_isr-withholding.md` SV-TAX-FR-120 (exemption up to two
  SMM of the comercio-y-servicios sector with the floor DEDUCTED
  from the retained excess — D.L. 458-2019 wording, R22; vintage
  rows 2014-2018 full exemption, 2021 $1,100, 2022-2024 $1,500,
  2025+ standing 2-SMM) — never re-derived here; the 2-SMM floor
  VALUE is dated data consumed from `02_minimum-wage.md`: the
  `smm_2025.csv` comercio_y_servicios monthly row ($408.80,
  valid_from 2025-06-01 ⇒ floor US$817.60) loaded per its
  SV-PAY-FR-011 and sector-pinned per its SV-PAY-FR-022; the F-14
  J/K exento/gravado columns receive the split per the matrix row of
  `01_salary-model.md` SV-PAY-FR-004 → `fiscal-reporting/
  06_f14-declaration.md` SV-FREP-FR-143/144 (consumed by id).
  (LB-023; LB-024; EVID-206/191)
- **SV-PAY-FR-061:** The system shall TAG the aguinaldo line as an
  extraordinary remuneration carrying its payment date, and consume
  by id the retention mechanics OWNED by `taxation/
  04_isr-withholding.md`: the D.E. 10-2025 Art. 1 g) aggregation of
  extraordinary remunerations (same-date aggregation into the
  monthly total; different-date aggregation into the LAST
  remuneration paid of the monthly period — SV-TAX-FR-116) and the
  June/December *recálculo* engines (SV-TAX-FR-110 June cumulative /
  SV-TAX-FR-111 December full-year, with prior-retention netting and
  the zero floor per their FRs); NO recálculo or aggregation
  arithmetic is implemented or restated in this file — the December
  aguinaldo flows into the December recálculo, and a termination
  proration paid mid-year flows into that month's computation, both
  entirely per the taxation-owned FRs. (LB-023; EVID-206)
- **SV-PAY-FR-062:** The system shall classify the two benefit lines
  exclusively through the canonical mapping matrix of
  `01_salary-model.md` SV-PAY-FR-004 (consumed by id, never
  re-derived): vacation pay — *prestación social*, NOT *salario*
  (CT Art. 119 final clause), IBC INCLUDED (SIP Art. 14 express
  "incluido el período de vacaciones"), ISR *remuneración gravada*
  (the CT exclusion from salario never propagates to the ISR base —
  EVID-204 mapping note), F-14 column G — the single line including
  its 30% surcharge; aguinaldo — *prestación social*, NOT *salario*
  (CT 119), IBC EXCLUDED (SIP Art. 14 b), ISR
  split_exento_gravado (SV-TAX-FR-120), F-14 J/K pair; consumer
  files (`05_social-security-contributions.md`,
  `08_isr-interfaces.md`, fiscal-reporting/06-07) read the matrix
  flags stamped on these lines. (LB-021; LB-022; EVID-197/201/204)

Note (75_ LB-029, historical layer — aguinaldo exemption vintages):
the 2001 Reglamento CT Art. 95 final inciso restates CT 155-II's
blanket no-retention as of that print, corroborating the vintage
chain's starting point; R22 (Ley ISR Art. 4.16 + D.L. 458-2019 2-SMM
floor) GOVERNS current periods — the vintages remain SV-TAX-FR-120's
by id, never restated here (see also `08_isr-interfaces.md` §3.8
FR-147).

### 3.4 Quincena Veinticinco (D.L. 499)

- **SV-PAY-FR-138:** The system shall compute, for every eligible
  worker, the annual Quincena Veinticinco benefit as FIFTY PERCENT
  of the monthly *salario básico o nominal* the worker is perceiving
  at the moment the prestación materializes — the law's OWN base
  (salario básico o nominal, NOT the CT 119 *salario integrante*;
  the law names its base), gated to workers whose monthly salario
  básico o nominal is ≤ US$1,500.00, and shall schedule payment
  inside the ANNUAL WINDOW of 15 through 25 January (payment lines
  dated outside the window raise a compliance flag; sole exception
  the FR-139 termination prorations, paid at termination) — the
  line classifies per the canonical matrix of
  `01_salary-model.md` SV-PAY-FR-004 (quincena_25 row, consumed by
  id); the gate threshold is the law's printed constant as dated
  data (D12, §2 exception), never an invented or re-derived value.
  (LB-026; LB-025; EVID-236)
- **SV-PAY-FR-139:** The system shall derive Quincena eligibility
  by MIRRORING the aguinaldo / compensación-adicional-en-efectivo
  requirements of the worker's sector regime — the law's express
  cross-reference, "sin que ello implique equiparar": requirements
  mirrored, the benefit NEVER equated (the aguinaldo rules of §3.2
  are consumed by reference, never re-implemented): the
  continuous/durational gates per §3.2 FR-053/FR-054 kin; the
  Art. 203 countable days of FR-059 apply to the proportional
  numerators; public-sector and municipal workers must be
  *laborando* for the entity at the moment of payment;
  special-regime institutions follow the Ley Compensación Adicional
  supletoria; and a worker terminated with employer responsibility
  or *despido de hecho* before or on 25-January retains a
  PROPORTIONAL right computed per the aguinaldo/CAE proportional
  rules (66_ Art. 3 [printed Art. 5 — sic]; positional attribution
  per the evidence OQ-1, carried as this file's OQ-006).
  (LB-027; LB-026; EVID-236; cross-ref FR-053..059)
- **SV-PAY-FR-140:** The system shall drive the Quincena payment
  duty by a DATED regime flag (D12): ejercicio 2026 = public sector
  MANDATORY (budget modification) / private sector VOLUNTARY — a
  voluntary private payment falling due at the latest
  25-January-2026 and carrying the employer tax credit owned by
  `taxation/01_isr-framework.md` SV-TAX-FR-174 (cited by id, never
  restated here); from ejercicio 2027 = MANDATORY for ALL
  employers, public and private (66_ Art. 1 "a partir del año dos
  mil veintisiete"); the flag is configuration dated by ejercicio
  (l10n_sv.pay.quincena.regime, §4), never a global constant.
  (LB-025; LB-028; EVID-236/238)
- **SV-PAY-FR-141:** The system shall enforce the Quincena payment
  invariants: the benefit is paid IN FULL — NO ISR retention, NO SS
  or pension cotización, NO deduction or discount of any kind
  attaches to the Quincena line; it NEVER enters the calculation
  base of any other prestación (the aguinaldo daily base FR-055,
  the vacaciones base FR-047, the indemnización bases of
  `07_contracts-termination.md` FR-105, the SMM-derived gates) nor
  the SS IBC (`05_social-security-contributions.md` FR-075); and it
  is *inembargable* (66_ Art. 4); the not-in-any-base invariant is
  verified as a NEGATIVE test (AC-014) — every base and the IBC
  compute exactly as if the Quincena were absent.
  (LB-025; LB-027; EVID-236)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in
the client (wave default `odoo`; see §5). No sidecar lives next to
this file: the only dated data consumed is the SMM feed owned by
`02_minimum-wage.md` (`smm_2025.csv` rows, SV-PAY-FR-011) and the
ISR vintages owned by `taxation/04_isr-withholding.md`
(SV-TAX-FR-120) — both consumed by FR id; the Quincena-25 regime
flag is configuration dated BY EJERCICIO owned by this file (FR-140)
and its US$1,500.00 gate is 66_'s printed constant (FR-138) — no
sidecar rows, per the §2 exception.

**Vacaciones engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.vacation.period (new) | anniversary_year · qualified · worked_days_in_year | integer/boolean (computed) | one record per contract × anniversary year; qualified = 1y continuous AND ≥200 worked days | FR-044, FR-046 |
| l10n_sv.pay.vacation.period | state | select | deferred · accrued · noticed · scheduled · in_progress · enjoyed · prorated_termination · collective | FR-044, FR-046, FR-048, FR-051, FR-052 |
| l10n_sv.pay.vacation.period | notice_date · window_deadline | date (computed) | ≥30-day notice; deadline = qualifying date + 4 months (≤100 workers) / 6 months (>100) per enterprise size | FR-048 |
| hr.leave (vacation type) | sv_pay_vacation_period_id · start validation | m2o/constraint | period may not start on an asueto/rest/compensatory day; those days inside are not counted | FR-045 |
| hr.payslip.line (vacation) | sv_pay_vacation_pay | monetary (computed) | 15 × daily base (FR-047 provenance) × 1.30, ONE line incl. surcharge; + Art. 184 additions 25%/50% | FR-044, FR-049 |
| l10n_sv.pay.vacation.scheme (new) | scheme_type · majority_agreement_ref | select/char | none · collective (waives FR-044/046 gates) · two_periods_ge_10 · three_or_more_ge_7 | FR-052 |
| hr.employee | sv_pay_employer_lodging · sv_pay_employer_food | boolean (config) | employer-provided benefits gating the Art. 184 additions | FR-049 |
| termination flow (hr.departure) | sv_pay_vacation_proration | monetary (computed) | proportional with employer responsibility / despacho de hecho; completed year ⇒ full pay; mechanics owned by 07 | FR-051 |

**Aguinaldo engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.aguinaldo (new) | year · employee · seniority_at_payment · tier_days | integer/date/select (computed) | tier_days ∈ {15, 19, 21} — floors (configurable upward); seniority at payment date (OQ-003 watch) | FR-053 |
| l10n_sv.pay.aguinaldo | daily_base · base_provenance | monetary/select | provenance: 01 FR-005 stored básico · 01 FR-006 SB-R7 · 02 FR-021 max-rule (never re-derived) | FR-055 |
| l10n_sv.pay.aguinaldo | proportional · worked_days · denominator | boolean/integer | <1y at Dec-12 (or termination pre-Dec-12): worked days incl. Art. 203 countable days ÷ denominator (365 default, OQ-004) × 15 × base | FR-054, FR-058 |
| l10n_sv.pay.aguinaldo | gross_prima · payment_date · termination_proration | monetary/date/boolean | payment_date window-checked 12-20 Dec (exception: termination proration) | FR-056, FR-058 |
| hr.payslip.line (aguinaldo) | sv_pay_aguinaldo_gross · sv_pay_extraordinary_remuneration · payment_date | monetary/boolean/date | gross supply to the ISR layer; extraordinary tag consumed by SV-TAX-FR-116/110/111 | FR-060, FR-061 |
| absence/leave records | sv_pay_art203_countable | boolean (catalog) | countable: vacations · licenses · disciplinary suspension · contract-suspension causes · fortuito/fuerza mayor; NOT detention-sanction | FR-059 |

**Interface provenance (no computation):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.aguinaldo | isr_split_owner | char (reference) | fixed pointer `taxation/04 SV-TAX-FR-120` — the split is never computed payroll-side | FR-060 |
| l10n_sv.pay.aguinaldo | exempt_floor_smm_row | m2o (dated data) | the `smm_2025.csv` comercio_y_servicios month row via 02 FR-011/FR-022; floor = 2 × row value at runtime | FR-060 |
| hr.payslip.line (both benefits) | matrix flags | stamped (from 01 FR-004) | vacation: IBC in · gravada · G; aguinaldo: IBC out · split_exento_gravado · J/K | FR-062 |

**Quincena Veinticinco engine (D.L. 499):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.quincena.regime (new, config) | ejercicio · regime | integer/select | regime: mandatory (2027+ ALL employers) · voluntary_2026 (private-sector 2026 opt-in) · public_2026 (public-sector 2026 mandatory) — computed by ejercicio per 66_ Art. 6, never a global constant | FR-140 |
| l10n_sv.pay.quincena.regime | payment_window | date range (derived) | 15–25 January of each ejercicio; outside-window lines = compliance flag (termination prorations excepted) | FR-138 |
| hr.salary.rule (quincena category) | existing matrix flags only — NO new rule fields | stamped (from 01 FR-004) | sv_pay_earning_class = quincena_25; every other classification rides the 01 matrix row consumed by id | FR-138, FR-141 |
| hr.payslip.line (quincena) | amount · base · gate_provenance | monetary/select (computed) | 0.5 × monthly salario básico o nominal at materialization; gate ≤ US$1,500.00 (66_ Art. 2 printed constant, D12); base = the law's own, never CT 119 integrante | FR-138 |
| l10n_sv.pay.quincena (eligibility) | eligible · proportional | boolean (by reference) | §3.2 mirroring (FR-053..059 kin); laborando-at-payment flag for public/municipal workers; Ley Compensación Adicional supletoria routing for special-regime institutions | FR-139 |
| termination flow (hr.departure) | sv_pay_quincena_proration | monetary (computed) | proportional right on employer-responsibility / despacho de hecho before or on 25-Jan, per the aguinaldo/CAE proportional rules; paid at termination | FR-139 |

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr /
hr_payroll / hr_holidays module family) — every FR maps `odoo`; no
SaaS rows are introduced because none of these FRs touch DTE
generation/transformation (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is
required beyond the dated-data regime below.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-044 | odoo | hr.payslip.line / l10n_sv.pay.vacation.period | sv_pay_vacation_pay | 15 × base × 1.30 as ONE line; class vacation_pay per 01 FR-004 |
| FR-045 | odoo | hr.leave | start validation + non-extension | Anniversary years; asueto/rest/compensatory days inside never extend nor count; day-count convention OQ-001 |
| FR-046 | odoo | l10n_sv.pay.vacation.period | worked_days_in_year / qualified | 200 WORKED days; suspension keeps continuity, adds no worked days; OQ-002 on justifiable days |
| FR-047 | odoo | hr.payslip (computation) | daily base provenance | 01 FR-005 stored básico · 01 FR-006 SB-R7 · 02 FR-021 max-rule — by id, current rate at computation |
| FR-048 | odoo | l10n_sv.pay.vacation.period | notice_date / window_deadline | ≥30-day notice; 4 months ≤100 workers / 6 months >100; expiry = compliance flag only |
| FR-049 | odoo | hr.employee + hr.payslip.line | lodging/food additions | +25% each, +50% both; components of the vacation line |
| FR-050 | odoo | hr.payslip (validation) | payment date ≤ start date | Late payment = compliance finding; covers all days until return |
| FR-051 | odoo | hr.departure flow / hr.payslip.line | sv_pay_vacation_proration | Proportional on employer-responsibility/despacho-de-hecho termination; completed year ⇒ full pay regardless |
| FR-052 | odoo | l10n_sv.pay.vacation.scheme + payslip gating | Art. 188 invariants | No cash/kind compensation; no fractioning/accumulation; collective waives gates; fractional 2×≥10 / ≥3×≥7 by majority agreement |
| FR-053 | odoo | l10n_sv.pay.aguinaldo | tier_days | 15/19/21 floors by seniority at payment date (OQ-003); quantum = base × tier |
| FR-054 | odoo | l10n_sv.pay.aguinaldo | proportional computation | <1y at Dec-12: (countable days ÷ denominator) × 15 × base; denominator 365 default (OQ-004) |
| FR-055 | odoo | l10n_sv.pay.aguinaldo | daily_base provenance | Same structure as FR-047 (Arts. 183/199 parallel); by id |
| FR-056 | odoo | l10n_sv.pay.aguinaldo | payment_date window check | 12-20 December; sole exception = FR-058 termination proration |
| FR-057 | odoo | l10n_sv.pay.aguinaldo (invariant) | no-forfeiture | No deduction/netting/conditioning line may attach; computes independent of disciplinary state |
| FR-058 | odoo | hr.departure flow / l10n_sv.pay.aguinaldo | termination proration | Pre-Dec-12 employer-responsibility/despacho-de-hecho termination; FR-054 mechanics |
| FR-059 | odoo | hr.leave / absence records | sv_pay_art203_countable | Vacations/licenses/disciplinary suspension/contract-suspension/fortuito-fuerza mayor count; detention-sanction does not |
| FR-060 | odoo | l10n_sv.pay.aguinaldo | gross supply + floor provenance | Split/vintages = SV-TAX-FR-120 (by reference); floor = 2 × smm_2025.csv comercio row (02 FR-011/FR-022); F-14 J/K via SV-FREP-FR-143/144 |
| FR-061 | odoo | hr.payslip.line | extraordinary tag + payment date | Aggregation/recálculo = SV-TAX-FR-116/110/111 (by reference; 53_-owned) |
| FR-062 | odoo | hr.payslip.line (stamped flags) | matrix consumption | Vacation: IBC in/gravada/G; aguinaldo: IBC out (14.b)/split/J-K; matrix owner 01 FR-004 |
| FR-138 | odoo | hr.payslip (computation) + hr.payslip.line | 0.5 × salario básico o nominal; ≤ US$1,500.00 gate | Law's own base (never CT 119 integrante); gate = 66_ printed constant (D12); 15–25 Jan window compliance check; class per 01 FR-004 quincena_25 row (by id) |
| FR-139 | odoo | l10n_sv.pay.quincena + hr.departure flow | eligibility mirroring | §3.2 FR-053..059 consumed by reference; laborando-at-payment (public/municipal); Art. 3 [printed Art. 5 — sic] proportional right before/on 25-Jan |
| FR-140 | odoo | l10n_sv.pay.quincena.regime | regime select by ejercicio | mandatory (2027+) · voluntary_2026 · public_2026; voluntary due ≤ 25-Jan-2026 + SV-TAX-FR-174 credit (by id); never a global constant |
| FR-141 | odoo | hr.payslip.line (invariants) + salary-rule gating | paid-in-full / not-in-any-base | No retention/cotización/deduction line; never in FR-047/FR-055/07-FR-105 bases nor the IBC (05 FR-075); inembargable (66_ Art. 4); negative AC test |

Version-regime notes (D12): no dated values live in this file. The
SMM feed re-seeds per SMM decree (owned by 02's sidecar — the
comercio-y-servicios row driving the 2-SMM floor); the aguinaldo
exemption vintages re-key per transitory law (owned by taxation/04
SV-TAX-FR-120 — SOQ-05 re-verification rides its OQ-003); the CT
tier/surcharge/window values are STATIC law (SOQ-21 vintage watch).
Exception (S6): the Quincena-25 regime flag re-keys by ejercicio
(2026 split / 2027+ mandatory — FR-140 configuration) and the
US$1,500.00 gate stands as 66_'s printed constant (FR-138); the
15–25 January window and the 50% quantum are STATIC law of D.L. 499
(effective 14-ene-2026).

## 6. Acceptance Criteria

- **AC-001:** Given a commission-only worker whose SB-R7 daily base
  is US$70.00 (the `01_salary-model.md` AC-001 case) qualifying for
  vacation, then the Art. 177 prestación is
  15 × 70.00 × 1.30 = US$1,365.00 emitted as ONE vacation-pay line
  (base + 30% surcharge), classified vacation_pay per the matrix of
  `01_salary-model.md` SV-PAY-FR-004 (FR-044, FR-047).
- **AC-002:** Given a worker with one continuous year of service of
  which 40 days were maternity-suspension leaves and 190 days were
  worked, then continuity holds (the year is complete) but the
  200-worked-days gate FAILS (190 < 200; suspension days are not
  worked days) — the vacation period stays deferred until the count
  reaches 200 (FR-046).
- **AC-003:** Given a qualified worker of a 60-employee enterprise
  whose vacation qualified on 1-March-2027, then the system records
  the ≥30-day employer notice, computes the take-window deadline
  1-July-2027 (4 months, ≤100 workers), and flags the period if
  still unenjoyed past that date; the same worker at a 150-employee
  enterprise would carry a 1-September-2027 deadline (6 months)
  (FR-048).
- **AC-004:** Given a qualifying worker whose daily base is
  US$16.00, with employer-provided lodging AND food both interrupted
  during the vacation, then the prestación is
  15 × 16.00 × 1.30 × 1.50 = US$468.00 (30% surcharge + 25% + 25%
  additions, one line); with only food interrupted it is
  US$390.00 (×1.25) (FR-044, FR-049).
- **AC-005:** Given (a) a worker who completed a qualifying year
  (1y + 200 days) and resigns 15-June (worker-side termination),
  then the FULL vacation prestación is paid regardless of
  responsibility; and (b) a worker 8 months past the last
  anniversary terminated with employer responsibility, then only the
  PROPORTIONAL vacation pay for those 8 months is paid — both as the
  sole Art. 188 exceptions (FR-051, FR-052).
- **AC-006:** Given one worker hired 10-December-2022 and another
  hired 20-December-2022, both employed at the 2025 aguinaldo paid
  15-December-2025, then the first takes the 19-day tier (3 years
  and 5 days of service at payment) and the second the 15-day tier
  (2y11m25d) — each at minimum quantum = tier × daily base (FR-053;
  the Dec-12-alternative reading recorded as OQ-003).
- **AC-007:** Given a worker hired 1-April-2026 with 254 countable
  days (239 worked + 15 vacation/license days per Art. 203),
  terminated 10-December-2026 with employer responsibility, then
  the Art. 202 termination proration pays
  (254 ÷ 365) × 15 × daily base at termination — outside the
  12-20-December window as the FR-056 exception; had the employment
  survived to 12-December, the same proportional computation would
  apply under Art. 197 inside the window (FR-054, FR-058, FR-059).
- **AC-008:** Given two same-seniority same-base colleagues, one
  with recorded unjustified absences and an active disciplinary
  sanction, then both receive the IDENTICAL gross aguinaldo prima —
  no netting, deduction or forfeiture line exists on the sanctioned
  worker's prima (FR-057), in contrast with the séptimo-día loss
  rule of `03_working-time-surcharges.md` FR-032.
- **AC-009:** Given an aguinaldo of US$1,800.00 paid 15-December-
  2025, then payroll supplies the GROSS US$1,800.00 tagged
  extraordinary with its payment date; the exempt-floor parameter
  resolves to the `smm_2025.csv` comercio_y_servicios row
  ($408.80, valid 2025-06-01) ⇒ floor US$817.60 (provenance check
  only); the exento/gravado split, the aggregation and the December
  recálculo outcomes are the computations of SV-TAX-FR-120/116/111
  — asserted by id, never reproduced in payroll (FR-060, FR-061).
- **AC-010:** Given a December payslip carrying a vacation-pay line
  (US$1,365.00) and an aguinaldo line (US$1,800.00), then the
  stamped matrix flags read: vacation — IBC included (SIP 14
  express), ISR gravada, F-14 G; aguinaldo — IBC excluded (SIP
  14.b), ISR split_exento_gravado (SV-TAX-FR-120), F-14 J/K; both
  prestación_social and NOT salario per CT 119 — flags consumed
  from `01_salary-model.md` SV-PAY-FR-004, never restated (FR-062).
- **AC-011:** Given a worker whose monthly salario básico o nominal
  is US$1,500.00 in January 2027 (mandatory ejercicio), then the
  Quincena Veinticinco benefit = 50% × 1,500.00 = US$750.00
  scheduled inside 15–25 January 2027; a same-window colleague at
  US$1,500.01 generates NO entitlement line at all — the gate is
  the printed ≤ US$1,500.00 constant with no boundary rounding
  (FR-138).
- **AC-012:** Given a worker hired 1-November-2026 continuously
  employed to 25-January-2027 (under one year of service), then
  the eligibility mirror grants a PROPORTIONAL Quincena right
  computed per the §3.2 aguinaldo proportional mechanics
  (FR-054/FR-059 kin — countable days ÷ denominator × the 50%
  benefit); and a same-schedule worker dismissed *despido de
  hecho* 10-January-2027 retains the proportional right (66_
  Art. 3 [printed Art. 5 — sic]) (FR-139).
- **AC-013:** Given a private employer in ejercicio 2026 WITHOUT
  the voluntary opt-in, then NO Quincena accrual exists
  (voluntary_2026 regime is opt-in only); with the opt-in, the
  payment is scheduled ≤ 25-January-2026 and the employer credit
  feed of `taxation/01_isr-framework.md` SV-TAX-FR-174 activates
  (asserted by id, never restated); the same employer in ejercicio
  2027 accrues MANDATORILY with no opt-in (regime = mandatory)
  (FR-140).
- **AC-014:** Given a worker with an ordinary salary, an accrued
  aguinaldo and a Quincena Veinticinco line of US$750.00, then the
  aguinaldo daily base (FR-055) and the SS IBC
  (`05_social-security-contributions.md` FR-075) compute EXACTLY as
  if the Quincena were absent (before/after delta = zero), and NO
  retention, cotización or deduction line of any kind appears
  attached to the Quincena line (FR-141; negative test).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Vacation day-count convention: Art. 177 grants "quince días" without stating días laborables vs calendario; Art. 178's non-extension rules (asuetos/rest inside never extend, period cannot start on them) imply días laborables, but the corpus never says so explicitly. Working assumption: 15 días laborables × daily base; a calendar-day reading would change both the count and the Art. 183 "salario ordinario correspondiente a dicho lapso" base span. | no | Takumi S4 (labor ruling watch) | open |
| OQ-002 | 200-day gate counting of justifiable absences: Art. 203's countable-days rule is EXPRESS only for the aguinaldo chapter; the vacation chapter (Arts. 177-189) is silent on whether vacations/licenses/suspension-cause days count toward the 200 worked days (Art. 181 excludes suspension days expressly). FR-046 defaults to strict worked days; a labor-authority or doctrine ruling could extend Art. 203 kin-wise. | no | Takumi S4 (labor ruling watch) | open |
| OQ-003 | Aguinaldo tier measurement date: Art. 197 fixes 12-December only for the <1-year proportional right; Art. 198's tiers say "tuviere" without a date. FR-053 measures seniority at the payment date (per cluster P5); an anniversary falling 13-20 December would flip the tier under that reading but not under a Dec-12 measurement. Corpus-silent; default = payment date. | no | Takumi S4 (labor ruling watch) | open |
| OQ-004 | Aguinaldo proportional denominator: Art. 197 says "parte proporcional al tiempo laborado" without a denominator (365 calendar days? días laborables of the year?); FR-054/FR-058 default to 365. Consistent market practice in SV payroll; no corpus norm pins it. | no | Takumi S4 (payroll config) | open |
| OQ-005 | SOQ-05 carried (via taxation/04 OQ-003): does a 2025/2026 aguinaldo transitory exist capping the Art. 4.16 2-SMM exemption at a fixed $-figure? The 54_ related-laws tail lists none after D.L. 159-2024 → SV-TAX-FR-120's 2025+ standing-2-SMM row stands; this file re-verifies at encoding time and owns only the SMM feed provenance (the 02 sidecar row — never the split, which is taxation-owned). | no | Takumi S4 (sources watch) | open |
| OQ-006 | 66_ print article numbering [sic]: "Art. 5." prints twice (Condición especial + Compatibilidad); the Condición especial (the termination proportional right of FR-139) is cited as Art. 3 POSITIONALLY — sequence 1-9 inferred from Art. 9 = Vigencia last, and the guía cites Art. 4 = Tratamiento fiscal explicitly (matches). Pin the numbering from a cleaner D.O. print if the /seleccion route recovers (volume Id 31679) — evidence OQ-1 carried. | no | Takumi S4 (sources watch) | open |
