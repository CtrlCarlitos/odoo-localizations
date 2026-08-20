# HN — Payroll — Salario concepts, mandatory deductions, protection, records & CT chassis + 85_ mislabel guard

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the Código del Trabajo (CT, Labor Code, D.189-1959 CEDIJ
consolidation) *chassis* and the *salario* (salary/wage) concept layer of the
Honduras payroll localization (cluster P12). It owns: (a) CT applicability
scope — who is inside (all empresas/personas naturales), who keeps only the
salario chapter (small farms ≤10 permanent workers) and who is outside
(public servants under Servicio Civil) — plus *orden público* (public-order)
and *irrenunciabilidad* (statutory rights cannot be waived) upward-only
floors; (b) the labor-contract data model: three essential elements,
contract-of-work presumption, mandatory written fields (Art. 37) including
the RETROACTIVE SERVICE-START clause that anchors D-H3 hire-date accruals;
(c) the **salario concept taxonomy** — the classification engine every
sibling payroll file consumes: habitual+retributive = salario (primes,
habitual bonuses, overtime, rest-day pay, commissions, profit-share);
exclusions (mere liberality, expense reimbursements, *prestaciones
sociales*/social benefits); in-kind ≤30% at employer's cost; free pay-basis
choice (mes/quincena/semana/día/hora/obra/participación); and *salario
completo* (ordinary+extraordinary) as THE indemnity base; (d) pay-period
ceilings (≤1 week manual / ≤1 month intellectual+domestic, Art. 368),
payment place/mode, profit-share annual liquidation; (e) the
labor-mandated deduction families beyond ISR/IHSS/RAP — *cuotas sindicales*
(union dues, Art. 95.12-13), Art. 60-A non-unionized dues, cooperative
quotas — each authorization-gated, plus the comprobante-retención
patronos-exempt interface; (f) salary protection: unembargable minimum
(SMM-level wage + vacaciones + first L100, 1959 nominals = dated caveat),
embargo caps 25%/50% alimentos/40% room-food, interest-free advances
amortizing ≥5 pay periods, privileged 30-day wage credits; (g) statutory
records: *Libro de Salarios* (≥10 workers) / IHSS-model planillas (3-9)
with overtime booked separately; (h) the contract-side SMM auto-elevation
rule (rows owned by file 01); and (i) the **85_ mislabel guard (R-H57)** —
D.93-2021 has ZERO CT effect — the CT-negatives guard (R-H60), the
article-map/pact-anchor corrections (R-H58/R-H59) and the consolidation
vintage pin (through D.278-2013).

It does **not** own (consumed by id, never re-derived): ISR withholding
engines and the código-111 record shape = taxation/04
(`HN-TAX-FR-121..153`, esp. FR-153); deduction semantics / Art. 10
exclusions = taxation/02 (`HN-TAX-FR-046..078`); SMM row values, bienio
tables and promedio = payroll/01 (`HN-PAYR-FR-001..040`); 13th/14th-month
special-law mechanics = payroll/02 (`HN-PAYR-FR-051..090`); IHSS
cotizaciones = payroll/03 (`HN-PAYR-FR-101..135`); IHSS incapacidad =
payroll/04 (`HN-PAYR-FR-141..170`); RAP/fondo accrual and the D.150-2008
cesantía-pact mechanics = payroll/05 (`HN-PAYR-FR-181..215`);
jornada/OT computation (44/48 equivalence, multipliers, Art. 335 valuation)
= payroll/06 (`HN-PAYR-FR-221..250`); vacaciones entitlement/base mechanics
= payroll/07 (`HN-PAYR-FR-261..280`); preaviso/cesantía/termination payouts
= payroll/08 (`HN-PAYR-FR-291..325`); suspension/maternity = payroll/09
(`HN-PAYR-FR-331..360`); DJIMR-111 export contract = fiscal-reporting/02
(`HN-FREP-FR-054/055`); comprobante de retención issuance mechanics =
e-invoicing/03 (`HN-EINV-FR-139/140`).

## 2. Legal Basis

Authority order (binding, per master evidence index): CT = `86_` (CEDIJ
consolidation of D.189-1959, vintage pinned through D.278-2013, EV85); the
85_ gazette = D.93-2021 (G 35,760) — PENAL family only, ZERO CT content,
carried exclusively as the mislabel guard (R-H57). D-H1/D-H2/D-H3 bind
everything (dated rows, hecho-generador/payslip-period resolution,
never-guess rule).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código del Trabajo, Arts. 1-4 | Art. 1: "El presente Código regula las relaciones entre el capital y el trabajo, colocándolas sobre una base de justicia social…". Art. 2: "Son de orden público las disposiciones contenidas en el presente Código y obligan a todas las empresas, explotaciones o establecimientos, así como a las personas naturales. Se exceptúan: 1) Las explotaciones agrícolas o ganaderas que no ocupen permanentemente más de diez (10) trabajadores; sin embargo le serán aplicables las disposiciones del Título IV, de este Código, Capítulo IV relativo a los salarios. 2) Los empleados públicos nacionales, departamentales y municipales…Las relaciones entre el Estado, el Departamento y el Municipio y sus servidores, se regirán por las leyes del Servicio Civil…". Art. 3: "Son nulos ipso jure todos los actos o estipulaciones que impliquen renuncia, disminución o tergiversación de los derechos que la Constitución, el presente Código, sus reglamentos o las demás leyes de trabajo o previsión social otorguen a los trabajadores…". Art. 4: "Trabajador es toda persona natural que preste a otra u otras, natural o jurídica, servicios materiales, intelectuales o de ambos géneros, mediante el pago de una remuneración y en virtud de un contrato o relación de trabajo." | CT scope is public-order and binds all undertakings and natural persons; exceptions: small farms ≤10 permanent workers keep only the salario chapter; state employees are governed by Servicio Civil law. Waiver clauses reducing statutory rights are null ipso jure. Worker = any natural person rendering material/intellectual services for remuneration under a contract or work relation. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 1-4 pp.1-3; Art. 8 p.4 (EV85:EVID-295) |
| LB-002 | CT, Arts. 20-21 | Art. 20: "Para que haya contrato de trabajo se requiere que concurran estos tres (3) elementos esenciales: a) La actividad personal del trabajador…; b) La continuada subordinación o dependencia…; y, c) Un salario como retribución del servicio." Art. 21: "Se presume que toda relación de trabajo personal está regida por un contrato de trabajo." | A labor contract requires three essential elements: (a) the worker's personal activity, (b) continued subordination/dependence, (c) salary as retribution for the service. Every personal work relation is presumed governed by a labor contract. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 19-23 p.8 (EV85:EVID-296) |
| LB-003 | CT, Art. 37 lit. c)/f)/g)/h)/j) + Art. 40 | Written-contract mandatory content: "c) La duración del contrato o la expresión de ser por tiempo indefinido y la fecha en que se iniciará el trabajo. Cuando la relación de trabajo haya precedido al otorgamiento por escrito del contrato, se hará constar también la fecha en que el trabajador inició la prestación de sus servicios al patrono"; "f) El tiempo de la jornada de trabajo y las horas que deberá prestarse"; "g) Si el trabajo se ha de efectuar por unidad de tiempo, de obra, por tarea o a destajo…"; "h) El salario, beneficio, comisión o participación que debe recibir el trabajador; si se debe calcular por unidad de tiempo, por unidad de obra o de alguna otra manera; y la forma, período y lugar de pagos"; "j) Beneficios que suministre el patrono en la forma de habitación, luz, combustible, alimentación, etc.,…y la estimación de su valor". Art. 40 (verbal contract minimum): "2. La cuantía y forma de la remuneración…y los períodos que regulen su pago; 3. La duración del contrato." | Contract data model: duration or indefinite flag + start date; when the work relation preceded the written contract, the actual service-start date must also be recorded (retroactive start); working hours/schedule; pay unit system (time/obra/tarea/destajo); salary/benefit/commission/participation and the form, period and place of payment; employer-supplied benefits with agreed valuation. Verbal contracts must at minimum fix remuneration amount/form and pay periods, and duration. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 37 pp.12-13; Art. 40 p.14 (EV85:EVID-296) |
| LB-004 | CT, Art. 60-A (added D.30, 15-mar-1973, G 20,941 — fn.11) | "En las empresas en que se encuentre vigente un contrato colectivo, los trabajadores no sindicalizados que reciban en forma directa beneficios de ésta pagarán al sindicato que hubiere concertado el contrato, una suma igual a la cuota ordinaria con que contribuyen los afiliados a la organización…Lo dispuesto en este artículo no será aplicable a los representantes del patronato, gerentes, sub-gerentes, administradores, jefes de personal, jefe de departamento y a los secretarios privados de éstos, así como aquellos trabajadores que de acuerdo con el contrato colectivo o el reglamento interno de trabajo sean empleados de confianza." | In companies with a live collective contract, non-unionized workers who directly receive its benefits pay the concluding union a sum equal to the ordinary member quota — automatically, no request needed. Excluded: employer representatives, managers, sub-managers, administrators, HR heads, department heads and their private secretaries, plus confianza employees per collective contract/internal regulations. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 60-A p.22 + fn.11 (EV85:EVID-299) |
| LB-005 | CT, Art. 95 lit. 12-13 | 12: "Hacer las deducciones que por cuotas sindicales ordinarias o extraordinarias soliciten los sindicatos. Estos comprobarán que las cuotas cuyo descuento piden, son las que establecen sus estatutos. Asimismo, deberán hacer las deducciones que fija el Artículo 60-A de este Código a los trabajadores no sindicalizados que en él se especifican, y las pondrán a disposición del sindicato sin necesidad de solicitud ni requerimiento." 13: "Hacer las deducciones de cuotas ordinarias para la constitución y fomento de las cooperativas y cajas de ahorro formadas por los trabajadores sindicalizados…". | Employer obligation to deduct ordinary/extraordinary union dues on union request (union must prove the dues match its statutes), to apply Art. 60-A dues to specified non-unionized workers automatically, and to deduct ordinary quotas for cooperatives and savings banks formed by unionized workers. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 95.12-13 pp.32-33 (EV85:EVID-299) |
| LB-006 | CT, Arts. 361-362 | Art. 361: "Constituye salario no sólo la remuneración fija u ordinaria, sino todo lo que recibe el trabajador en dinero o en especie y que implique retribución de servicios, sea cualquiera la forma o denominación que se adopte, como las primas, sobresueldos, bonificaciones habituales, valor del trabajo suplementario o de las horas extras, valor del trabajo en días de descanso obligatorio, porcentaje sobre ventas, comisiones o participación de utilidades." Art. 362: "No constituyen salario las sumas que ocasionalmente y por mera liberalidad recibe el trabajador…como las primas, bonificaciones y gratificaciones ocasionales y lo que recibe en dinero o en especie no para su beneficio…como los gastos de representación, medios de transporte, elementos de trabajo u otros semejantes, ni tampoco las prestaciones sociales." | Salary = not only fixed/ordinary remuneration but everything the worker receives in money or kind implying retribution of services, in any form or name: primes, supplements, habitual bonuses, overtime value, mandatory-rest-day work value, sales percentages, commissions, profit-share. NOT salary: occasional mere-liberality sums; amounts not for the worker's benefit (representation expenses, transport, work elements); social benefits (*prestaciones sociales*). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 361-362 pp.104-105 (EV85:EVID-317) |
| LB-007 | CT, Arts. 364-365 | Art. 364: "El cálculo de la remuneración para el efecto de su pago, puede pactarse: a) Por unidad de tiempo, (mes, quincena, semana, día y hora); b) Por unidad de obra, (pieza, tarea, precio alzado o a destajo); y, c) Por participación en las utilidades, ventas o cobros que haga el patrono." Art. 365: "El salario deberá pagarse en moneda de curso legal…". | Remuneration may be agreed: (a) per time unit (month, fortnight, week, day, hour); (b) per work unit (piece, task, lump price or *destajo* piece-rate); (c) by participation in profits, sales or collections. Salary must be paid in legal-tender currency. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 364-365 p.105 (EV85:EVID-317) |
| LB-008 | CT, Art. 366 | "Las prestaciones complementarias que reciba el trabajador campesino o su familia, en forma de alimentos, habitación y demás artículos…se considerarán como parte de la retribución ordinaria…siempre que el valor que se le atribuya no exceda del treinta por ciento (30%) del salario en dinero y que el patrono haga el suministro de esos artículos a precio de costo o menos." | Complementary benefits in kind (food, housing and similar articles) received by rural workers or their families count as part of ordinary remuneration only if the attributed value does not exceed 30% of the cash salary AND the employer supplies them at cost price or less. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 366 pp.105-106 (EV85:EVID-317) |
| LB-009 | CT, Art. 367 | "A trabajo igual debe corresponder salario igual, sin discriminación alguna…No pueden establecerse diferencias en el salario por razones de edad, sexo, nacionalidad, raza, religión, opinión política o actividades sindicales." | Equal work must carry equal pay, without discrimination; no salary differences for reasons of age, sex, nationality, race, religion, political opinion or union activity. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 367 p.106 (EV85:EVID-317) |
| LB-010 | CT, Art. 368 | "Las partes fijarán el plazo para el pago del salario, pero dicho plazo nunca podrá ser mayor de una (1) semana para los trabajadores manuales, ni de un (1) mes para los trabajadores intelectuales y los servidores domésticos. Si el salario consistiere en participación de las utilidades, ventas o cobros…se señalará una suma semanal o mensual…La liquidación definitiva se hará por lo menos anualmente. Salvo lo dispuesto en el párrafo anterior, el salario debe liquidarse completo en cada período de pago. Para el cómputo de todas las indemnizaciones o prestaciones que otorga este Código, se entiende por salario completo el devengado durante las jornadas ordinaria y extraordinaria, o el equivalente de las mismas para los trabajos contratados por unidad de obra." | Pay period ceilings: never >1 week for manual workers, >1 month for intellectual workers and domestic servants. Profit/participation pay: weekly/monthly advance sum, definitive liquidation at least annually. Otherwise salary is liquidated COMPLETE each pay period. For ALL Code indemnities/benefits, *salario completo* = amounts earned in ordinary AND extraordinary jornadas (or their equivalent for piece-work). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 368 p.106 (EV85:EVID-318) |
| LB-011 | CT, Arts. 369-370 + Art. 170 | Art. 369: "Salvo convenio por escrito, el pago debe efectuarse en el lugar donde el trabajador presta sus servicios…" Art. 370: "El salario se paga directamente al trabajador o la persona que él autorice por escrito…". Art. 170: "Las retribuciones de los trabajadores a domicilio serán canceladas por entrega de labor o por períodos no mayores de una (1) semana." | Payment at the workplace unless otherwise agreed in writing; paid directly to the worker or a person he authorizes in writing. Homeworkers (*a domicilio*) are paid per delivery of work or per periods not longer than one week. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 369-370 p.107; Art. 170 p.61 (EV85:EVID-318) |
| LB-012 | CT, Arts. 371 + 373 | Art. 371: "No es embargable el salario mínimo legal o convencional, la prestación en concepto de vacaciones, ni los primeros cien lempiras (L.100.00) del cómputo mensual de cualquier salario. El excedente de cien lempiras (L.100.00) del cómputo mensual de cualquier salario sólo es embargable en una (1/4) cuarta parte. Véase Decreto No.14-1973 No obstante lo dispuesto en los párrafos anteriores, son embargables toda clase de salarios en los siguientes casos: a) Hasta en un cincuenta por ciento (50%) para el pago de prestaciones alimenticias en la forma que establece la ley; y, b) Hasta en un cuarenta por ciento (40%) para pagar la habitación donde vive el trabajador, o los artículos alimenticios que él haya comprado para su consumo…". Art. 373: "Los salarios que no excedan de doscientos lempiras mensuales (L.200.00), no podrán cederse, venderse, compensarse ni gravarse…sino en la proporción en que sean embargables." | Unembargable: the legal/collective minimum wage, vacation pay, and the first L100 of any monthly salary; the L100 excess is embargoable only up to one-fourth (25%). Exceptions: any salary up to 50% for alimony, up to 40% for the worker's housing or food purchases. Salaries ≤L200/month cannot be assigned/sold/offset/encumbered except in the embargoable proportion. NOTE: L100/L200 are 1959 nominals with in-text "Véase Decreto No.14-1973" — dated caveat (OQ-002). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 371, 373 pp.107-108 (EV85:EVID-319) |
| LB-013 | CT, Art. 372 | "Los anticipos que haga el patrono al trabajador por cuenta de salarios, en ningún caso devengarán intereses. Las deudas que el trabajador contraiga con el patrono por este concepto, por pagos hechos en exceso o por responsabilidades civiles con motivo del trabajo, se deben amortizar durante la vigencia del contrato en un mínimo de cinco (5) períodos de pago. Es entendido que al terminar el contrato, el patrono podrá hacer la liquidación definitiva que proceda." | Salary advances bear no interest. Worker debts from advances, overpayments or work-related civil liabilities amortize during the contract over a MINIMUM of five pay periods; final liquidation of advances at contract end. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 372 pp.107-108 (EV85:EVID-319) |
| LB-014 | CT, Art. 374 | "Los créditos a favor de los trabajadores por salarios devengados en el último año, o por indemnizaciones…y las prestaciones sociales, se considerarán singularmente privilegiados…pagarlos dentro de los treinta (30) días siguientes…". | Workers' wage credits (last year's salaries, indemnities, social benefits) are singularly privileged; on insolvency they are paid within 30 days of formal judicial recognition. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 374 p.108 (EV85:EVID-319) |
| LB-015 | CT, Arts. 380 + 335 | Art. 380: "Todo patrono que ocupe permanentemente a diez (10) o más trabajadores deberá llevar un Libro de Salarios autorizado y sellado por la Dirección General del Trabajo, que se encargará de suministrar modelos y normas para su debida impresión. Todo patrono que ocupe permanentemente a tres (3) o más trabajadores, sin llegar al límite de diez (10) está obligado a llevar planillas de conformidad con los modelos adoptados por el Instituto Hondureño de Seguridad Social." Art. 335: "Los patronos estarán obligados a consignar en sus libros de salarios o planillas, debidamente separados de lo que se refiere a trabajo ordinario, lo que a cada uno de sus trabajadores paguen por concepto de trabajo extraordinario." | Employers with ≥10 permanent workers keep a Wages Book (Libro de Salarios) authorized and stamped by the Dirección General del Trabajo; employers with 3-9 keep payrolls (planillas) per IHSS-adopted models. Overtime pay must be recorded in the books/planillas SEPARATELY from ordinary pay. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 380 p.109 (EV85:EVID-320); Art. 335 p.97 carried at EV85:EVID-320 (Loc; OT context EV85:EVID-311) |
| LB-016 | CT, Arts. 363 + 389 (+ fn.34: D.103-1971 tacit reform; C-1982 Art. 128.5) | Art. 363: "El salario se estipulará libremente, pero no podrá ser inferior al que se fije como mínimo…". Art. 389: "La fijación del salario mínimo modifica automáticamente los contratos de trabajo que estipulen uno inferior elevando éste al mínimo, sin afectarlo en lo demás." fn.34: "Artículo 383. Reformado tácitamente por decreto No.103, Ley del Salario Mínimo de fecha 20 de enero de 1971…La Constitución de la República de 1982 Vigente se refiere al Artículo 128 numeral 5)…5. Todo trabajador tiene derecho a devengar un salario mínimo, fijado periódicamente…El salario mínimo está exento de embargo, compensación y deducciones, salvo lo dispuesto por la ley atendiendo a obligaciones familiares y sindicales del trabajador." | Salary is freely agreed but never below the fixed minimum. Each new minimum-wage fixation AUTOMATICALLY modifies contracts stipulating less, elevating them to the minimum without affecting anything else. Art. 383 was tacitly reformed by the Salario Mínimo law D.103-1971; Constitution Art. 128.5: periodic minimum, exempt from embargo/compensation/deductions except family and union obligations. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 363, 389, fn.34 pp.105, 110-112 (EV85:EVID-321) |
| LB-017 | CT, Arts. 376-380 + corpus negatives (greps) | Art. 376: "Durante la vigencia del contrato el trabajador tiene derecho a percibir el salario, aún cuando no haya prestación del servicio por disposición o culpa del patrono." Negatives: 0 corpus hits for "aguinald*", "décimo tercer", "décimo cuarto"; INVI absent; "integral" absent as a salary concept; "acoso/hostigamiento" absent; Arts. 376-380 are salario rules, not an aguinaldo family. | The CT contains NO 13th-month (aguinaldo), NO 14th-month, NO INVI/labor-fund articles, NO "salario integral" concept and NO harassment provisions; aguinaldo/14th exist only in special law (D.135-94/Acuerdo 02-95), the fondo in D.47-2024. Arts. 376-380 are salary rules (Art. 376: salary payable even without service due to employer's disposition/fault). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 376-380 p.109 + corpus greps (EV85:EVID-327) |
| LB-018 | CT, fn.36 (p.152) + fn.19 (p.49) — vintage pins | fn.36: "Artículo 464. Derogado por Decreto 278-2013 de fecha 21 de diciembre de 2013 y publicado en el Diario La Gaceta No.33,316 de fecha 30 de diciembre de 2013." fn.19: "Reforma del artículo 120 y 120-A adicionado por Decreto No.150-2008 de fecha 3 de octubre de 2008 y publicado en el Diario Oficial La Gaceta No.31,753 de fecha 5 de noviembre de 2008. Vigente a partir de su publicación." | Consolidation window pinned: newest instrument integrated = D.278-2013 (30-dic-2013); Arts. 120/120-A (incl. the annual cesantía-pact anchor of D.150-2008 Art. 2) reformed/added by D.150-2008. The print does NOT carry any post-2013 CT instrument (notably D.117-2021, Art. 113.1 interp = corpus file 89_). | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | fn.36 p.152; fn.19 p.49 (EV85:EVID-328) |
| LB-019 | D.93-2021 (La Gaceta 35,760, 1-nov-2021), Arts. 1-2 + sumario | Art. 1: "Derogar los artículos 102, 103, 104, 105, 106, 176, 182, 225, 263, 275, 309, 317, 337, 346, 368, 397, 403, 411, 417, 430, 434, 437, 444, 469, 511, 569 y 596; todos del Decreto No.130-2017…que contiene el CÓDIGO PENAL…". Art. 2: "Derogar los artículos 28 y 153 del Decreto No.130-2017…". D.93-2021 amends only Código Penal D.130-2017, Código Procesal Penal D.9-99-E and Ley Lavado de Activos D.144-2014; vigencia the day after publication (2-nov-2021). | D.93-2021 derogates/reforms PENAL-family articles only (31 CP articles total incl. Arts. 2/6 lists: 28, 153, 296, 353, 613); ZERO Código del Trabajo content — the registry filename "derogaciones_CT" is a MISLABEL. Never a CT legal basis. | `hn/sources/85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf` | 93-Arts. 1-2 pp.A.2-A.3; sumario p.A.1; vigencia 93-Art. 11 pp.A.18-A.19 (EV85:EVID-329) |
| LB-020 | D.93-2021 derogated numbers × CT status — collision table (synthesis) | Every derogated number belongs to CP D.130-2017. Same-number CT counterparts remain LIVE: CT-28 (sustitución patronos), CT-102-106 (suspension/sickness), CT-153 (doméstico), CT-176/182/225/263/275 (special contracts), CT-309/317, **CT-337 (turnos), CT-346 (vacaciones scale), CT-368 (pay periods/salario completo), CT-417 (riesgo base)**, CT-397…596 — verdict per row: "CT effect: NONE". 0 CT articles derogated by D.93-2021; no target family (jornada 318-337, vacaciones 345-356, salario 360-390, preaviso/cesantía 116-123, terminación 111-126, maternidad 135-146) is affected. | The numeric collision of derogated penal numbers with live CT payroll articles (337/346/368/417 etc.) is the mislabel root cause; the guard table maps each derogated number to its LIVE CT counterpart with verdict "no CT effect". | `hn/sources/85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf` | synthesis of 93-Arts. 1, 2, 6, 10 vs 86_ full text (EV85:EVID-333) |

## 3. Functional Requirements

### 3.1 CT chassis: scope, irrenunciabilidad, contract data model

- **HN-PAYR-FR-371:** The system shall classify employers for CT payroll
  applicability as company-level regime flags: default = inside the CT (all
  *empresas, explotaciones o establecimientos* and natural persons);
  (a) agricultural/livestock exploitations with ≤10 permanent workers → ONLY
  the salario chapter (Título IV Cap. IV) applies; (b) national,
  departmental and municipal public employees → governed by Servicio Civil
  law, outside the CT payroll rule families. The flags gate which payroll
  rule families activate per company. (LB-001; EV85:EVID-295)
- **HN-PAYR-FR-372:** The system shall treat every statutory payroll floor
  of the CT and its special laws as *orden público* / *irrenunciabilidad*
  (non-waivable) defaults: contract clauses or manual overrides that would
  lower any floor (SMM, vacaciones, jornada ceilings, salario completo
  bases, protection minimums) below the statutory level are *nulos ipso
  jure* (null by operation of law) — the engine shall refuse the
  modification or clamp upward, never downward; improvements above the
  floor are always permitted. (LB-001; EV85:EVID-295)
- **HN-PAYR-FR-373:** The system shall model the employment contract on the
  CT's three essential elements — (a) the worker's personal activity,
  (b) continued subordination or dependence, (c) salary as retribution —
  and shall apply the Art. 21 presumption that EVERY personal work relation
  is governed by a labor contract (*trabajador* = any natural person
  rendering material or intellectual services to another, natural or
  juridical, for remuneration), so that payroll accruals attach to the
  relation regardless of written form. (LB-001; LB-002; EV85:EVID-295/296)
- **HN-PAYR-FR-374:** The system shall carry the Art. 37 mandatory
  written-contract fields as contract data: duration or *por tiempo
  indefinido* (indefinite-term) flag + work-start date; jornada
  (working-schedule) hours and schedule; work unit (tiempo/obra/tarea/
  destajo); the salary, benefit, commission or participation amount with
  its computation form, payment form, period and place; and
  employer-supplied benefits (housing, light, fuel, food) with their agreed
  valuation; plus the Art. 40 verbal-contract minimums (remuneration
  amount and form, pay periods, duration) for unwritten relations. Jornada
  computation semantics (incl. the 44-worked/48-paid equivalence, R-H61) =
  file 06 (`HN-PAYR-FR-221..250`), consumed by id.
  (LB-003; EV85:EVID-296; R-H61)
- **HN-PAYR-FR-375:** The system shall record on the contract a service
  start date distinct from (and possibly earlier than) the written-contract
  date — "Cuando la relación de trabajo haya precedido al otorgamiento por
  escrito del contrato, se hará constar también la fecha en que el
  trabajador inició la prestación de sus servicios al patrono" — and shall
  anchor ALL hire-date-depth accruals (fondo/cesantía tenure per file 05
  `HN-PAYR-FR-181..215`, vacaciones tenure per file 07
  `HN-PAYR-FR-261..280`, preaviso/cesantía per file 08
  `HN-PAYR-FR-291..325`) to the service start, not the registration date.
  Ingestion of pre-registration service follows D-H3: monthly aggregates
  per contract FROM SERVICE START — never payslip-level import; corrections
  and retro computations resolve with ORIGINAL-period rows (D-H2).
  (LB-003; EV85:EVID-296)

### 3.2 Salario concept taxonomy (the classification engine)

- **HN-PAYR-FR-376:** The system shall implement a salary-concept
  classification engine per Art. 361: *salario* = not only the fixed or
  ordinary remuneration but EVERYTHING the worker receives in money or in
  kind that implies retribution of services, whatever its form or
  denomination — *primas* (primes/bonuses), *sobresueldos* (wage
  supplements), *bonificaciones habituales* (habitual bonuses), the value
  of *trabajo suplementario o de horas extras* (overtime), the value of
  work on mandatory rest days, sales percentages, commissions and
  *participación de utilidades* (profit-share) — with the resulting
  per-concept `is_salario` flag consumed BY ID (no re-derivation) by every
  sibling base: fondo salario-ordinario hypothesis (file 05,
  `HN-PAYR-FR-181..215`), IHSS base config (file 03,
  `HN-PAYR-FR-101..135`), ISR annual gross (`HN-TAX-FR-126`), vacaciones
  base (file 07, `HN-PAYR-FR-261..280`), preaviso/cesantía base (file 08,
  `HN-PAYR-FR-291..325`). (LB-006; EV85:EVID-317)
- **HN-PAYR-FR-377:** The system shall classify as NOT salario (never
  entering benefit averages or the salario completo base): (a) sums
  received occasionally and by mere liberality (occasional *primas*,
  *bonificaciones* and *gratificaciones*); (b) amounts received in money or
  kind not for the worker's benefit — *gastos de representación*
  (representation expenses), transport means, work elements and similar;
  (c) *prestaciones sociales* (statutory social benefits).
  (LB-006; EV85:EVID-317)
- **HN-PAYR-FR-378:** The system shall value in-kind complementary
  benefits (food, housing and similar articles supplied to the rural worker
  or family) as part of ordinary remuneration ONLY while (a) the attributed
  value does not exceed 30% of the cash salary AND (b) the employer
  supplies them at cost price or less; the excess above either condition
  does not count as salario. (LB-008; EV85:EVID-317)
- **HN-PAYR-FR-379:** The system shall support the Art. 364 pay bases as
  contract configuration: time unit (mes, quincena, semana, día, hora),
  obra unit (pieza, tarea, precio alzado, a destajo), or participation
  (utilidades, ventas, cobros) — recording that NO "empleo por hora" regime
  exists in the CT beyond *hora* as one pay-unit option.
  (LB-007; EV85:EVID-317)
- **HN-PAYR-FR-380:** The system shall flag — advisory, never
  auto-adjusting — salary differences for equal work attributable to age,
  sex, nationality, race, religion, political opinion or union activity
  ("A trabajo igual debe corresponder salario igual, sin discriminación
  alguna"), as an equal-pay review output.
  (LB-009; EV85:EVID-317)
- **HN-PAYR-FR-381:** The system shall define the SINGLE indemnity base
  for ALL CT indemnities and prestaciones: *salario completo* = the amounts
  earned during the ordinary AND extraordinary jornadas (or their
  equivalent for obra-contracted work) — this file owns the definition;
  files 05/07/08 own each instrument's base composition and consume it by
  id (file 08's 6-month ÷ days-worked average routine, file 05's fondo
  base, file 07's vacation-base width question remain theirs).
  (LB-010; EV85:EVID-318)

### 3.3 Pay periods, payment mechanics, profit-share

- **HN-PAYR-FR-382:** The system shall validate pay periods by worker
  class: manual workers ≤ 1 week; intellectual workers and *servidores
  domésticos* (domestic workers) ≤ 1 month; *a domicilio* (homeworkers) ≤
  1 week or per delivery of work — and shall enforce that the salary is
  liquidated COMPLETE in each pay period (no unlawful partial retention
  inside an agreed period). (LB-010; LB-011; EV85:EVID-318)
- **HN-PAYR-FR-383:** The system shall record payment place (default:
  where the worker renders the services, departed from only by written
  agreement), payment mode (directly to the worker or to a person
  authorized by him in writing) and payment currency (*moneda de curso
  legal*, legal tender) as contract-level payment configuration.
  (LB-007; LB-011; EV85:EVID-317/318)
- **HN-PAYR-FR-384:** For pay bases by participation in profits, sales or
  collections, the system shall support a fixed weekly or monthly advance
  sum plus an at-least-ANNUAL definitive liquidation flagged on the payroll
  calendar. (LB-010; EV85:EVID-318)
### 3.4 Labor-mandated deductions and salary protection

- **HN-PAYR-FR-385:** The system shall implement *cuotas sindicales*
  (union dues) as an authorization-gated deduction type: ordinary and
  extraordinary dues deducted upon the union's request, with the union's
  proof that the requested dues are those established in its *estatutos*
  (statutes); deducted amounts remitted to the requesting union.
  (LB-005; EV85:EVID-299)
- **HN-PAYR-FR-386:** The system shall implement the Art. 60-A
  non-unionized dues deduction: in companies where a collective contract
  is in force, non-unionized workers who directly receive its benefits pay
  the concluding union a sum equal to the ordinary member quota — applied
  AUTOMATICALLY, without worker request or union solicitation
  ("sin necesidad de solicitud ni requerimiento") — with a mandatory
  exclusion-role gate: representatives of the employer, *gerentes*,
  *sub-gerentes*, *administradores*, *jefes de personal*, *jefes de
  departamento*, their private secretaries, and *empleados de confianza*
  (trust employees) per the collective contract or internal regulations
  are never subject to the deduction. (LB-004; LB-005; EV85:EVID-299)
- **HN-PAYR-FR-387:** The system shall implement ordinary
  cooperative/savings quotas (*cuotas ordinarias para la constitución y
  fomento de las cooperativas y cajas de ahorro* formed by unionized
  workers) as authorization-gated deduction types with worker-consent
  records and beneficiary remittance to the cooperative/savings entity.
  (LB-005; EV85:EVID-299)
- **HN-PAYR-FR-388:** The system shall gate EVERY payroll deduction of
  this file on statutory authority plus (where the instrument is
  consent-based) a recorded worker authorization: the deduction families
  owned here = union dues, Art. 60-A non-union dues, cooperative quotas
  and the salary-protection limits ONLY — ISR withholding
  (`HN-TAX-FR-121..153`, record shape FR-153), IHSS cotizaciones (file 03,
  `HN-PAYR-FR-101..135`) and RAP/fondo retentions (file 05,
  `HN-PAYR-FR-181..215`) are consumed by id and never re-derived here; the
  salary-retention voucher interface = `HN-EINV-FR-139/140` — employers
  (*patronos*) are exempt from issuing retention vouchers on salary unless
  the worker requests one (EV24:EVID-200).
  (LB-004; LB-005; EV85:EVID-299; EV24:EVID-200)
- **HN-PAYR-FR-389:** The system shall implement the salary-protection
  (*embargo*/garnishment) engine: unembargable = the legal or conventional
  minimum wage, the vacation pay, and the first L100 of any monthly salary
  computation; the excess above L100 is embargoable at most one-fourth
  (25%); exceptions up to 50% for *prestaciones alimenticias* (alimony)
  and up to 40% for the worker's housing or purchased food; concurrent
  orders stack on the embargable remainder. The L100/L200 thresholds are
  1959 NOMINAL values (in-text "Véase Decreto No.14-1973") — the system
  shall carry them as DATED rows with a configuration-gap flag and shall
  NOT implement literal lempira thresholds without a modern LB (D-H2
  never-guess; 86_ OQ-7 → OQ-002); the percentage caps and the
  minimum-wage/vacaciones floors are implementable as printed.
  (LB-012; EV85:EVID-319)
- **HN-PAYR-FR-390:** The system shall implement salary advances as
  interest-free; worker debts to the employer (advances on account of
  salary, excess payments, work-related civil liabilities) amortize over a
  MINIMUM of five pay periods during the contract's life, with per-period
  recovery capped accordingly; the final liquidation of the advance balance
  occurs at contract termination. (LB-013; EV85:EVID-319)
- **HN-PAYR-FR-391:** The system shall flag worker credits — salaries
  earned in the last year, indemnities and *prestaciones sociales* — as
  singularly privileged against all other creditors except *alimentarios*
  (support creditors), payable within 30 days of formal judicial
  recognition on insolvency/concours/quiebra scenarios (informational
  priority flag on the settlement ledger).
  (LB-014; EV85:EVID-319)

### 3.5 Statutory payroll records

- **HN-PAYR-FR-392:** The system shall reproduce the statutory payroll
  records by employer size: ≥10 permanent workers → *Libro de Salarios*
  (Wages Book, authorized and stamped by the Dirección General del
  Trabajo); 3-9 permanent workers → *planillas* (payrolls) per the models
  adopted by the IHSS; regime selection driven by live permanent headcount.
  (LB-015; EV85:EVID-320)
- **HN-PAYR-FR-393:** The system shall book overtime pay SEPARATELY from
  ordinary pay in the Libro de Salarios / planillas outputs
  ("debidamente separados de lo que se refiere a trabajo ordinario, lo que
  a cada uno de sus trabajadores paguen por concepto de trabajo
  extraordinario"); overtime computation and multipliers = file 06
  (`HN-PAYR-FR-221..250`) — this file owns only the record-separation
  duty. (LB-015; EV85:EVID-320)

### 3.6 Minimum-wage auto-elevation (contract side)

- **HN-PAYR-FR-394:** The system shall implement the contract-side
  elevation rule: salary is freely stipulated but never below the fixed
  minimum ("El salario se estipulará libremente, pero no podrá ser inferior
  al que se fije como mínimo"); when a newly fixed salario mínimo row takes
  effect, contracts stipulating a lower wage are AUTOMATICALLY elevated to
  it ("La fijación del salario mínimo modifica automáticamente los
  contratos de trabajo que estipulen uno inferior elevando éste al mínimo,
  sin afectarlo en lo demás") — computed from the dated SMM rows owned by
  file 01 (`HN-PAYR-FR-001..040`), resolved by payslip period (D-H2), paid
  slips frozen, corrections recomputed with original-period rows; the
  minimum wage itself is exempt from embargo/compensation/deductions
  except family and union obligations (fn.34/C-1982 Art. 128.5, consumed
  by FR-389's floor). (LB-016; EV85:EVID-321)

### 3.7 Guards: 85_ mislabel, CT negatives, article map, vintage

- **HN-PAYR-FR-395:** The system shall encode the 85_ mislabel guard as a
  NEVER-IMPLEMENT block (R-H57): D.93-2021 (G 35,760) amends ONLY the
  Código Penal D.130-2017, Código Procesal Penal D.9-99-E and Ley Lavado
  de Activos D.144-2014 and has ZERO Código del Trabajo effect — no CT
  article may be flagged derogated/reformed by 85_, 85_ shall never be
  citable as a CT legal basis, and the numeric collisions shall be mapped
  in a collision table pairing each derogated PENAL number (28, 102-106,
  153, 176, 182, 225, 263, 275, 296, 309, 317, 337, 346, 353, 368, 397,
  403, 411, 417, 430, 434, 437, 444, 469, 511, 569, 596, 613) with its
  LIVE CT counterpart and the verdict "CT effect: NONE" — notably CT-337
  (turnos), CT-346 (vacaciones scale), CT-368 (pay periods / salario
  completo), CT-417 (riesgo base) all remain live law.
  (LB-019; LB-020; EV85:EVID-329/333; R-H57)
- **HN-PAYR-FR-396:** The system shall encode the CT-negatives guard
  (R-H60): the CT contains NO *aguinaldo*/décimo tercer mes, NO décimo
  cuarto mes, NO INVI/labor-fund articles, NO *salario integral* concept
  and NO *acoso* (harassment) provisions — 13th/14th-month mechanics
  belong to special law (file 02, `HN-PAYR-FR-051..090`) and the fondo to
  D.47-2024 (file 05, `HN-PAYR-FR-181..215`); Arts. 376-380 of the CT are
  salario rules (Art. 376 = salary payable even without service due to the
  employer's disposition or fault; Art. 380 = Libro de Salarios), NOT an
  aguinaldo family; any configuration surface citing a CT article number
  for these concepts is rejected with the negative-finding note.
  (LB-017; LB-015; EV85:EVID-327/320; R-H60)
- **HN-PAYR-FR-397:** The system shall carry the corrected article map and
  anchor discipline (R-H58/R-H59): vacaciones = CT Arts. 345-356 (NOT a
  "328-family" — Art. 328 = full pay for <44h weeks; consumed by file 07);
  jornada = Arts. 318-337 (file 06); salario = Arts. 360-390 (this file);
  the ANNUAL CESANTÍA PACT anchor = D.150-2008 Art. 2, printed at CT
  Art. 120-A fn.19 — never "CT-Art.-95 pacts" (Art. 95 = patrono
  obligations; gloss drift corrected per R-H58) — its payroll mechanics
  consumed by files 05/08; termination-payout articles 111-126 = file 08.
  (LB-017; LB-018; EV85:EVID-327/328; R-H58, R-H59)
- **HN-PAYR-FR-398:** The system shall record the consolidation vintage of
  the CT source: integration window through D.278-2013 (G 33,316,
  30-dic-2013, fn.36); Art. 60-A added by D.30-1973; Arts. 120/120-A by
  D.150-2008 (fn.19) — and shall NOT cite the 86_ print for any post-2013
  CT point: the Art. 113.1 interpretation routes to D.117-2021 (corpus
  file `89_`, outside this print) and any other post-2013 reform routes to
  acquisition (86_ OQ-1 → OQ-001).
  (LB-018; EV85:EVID-328)

## 4. Data Model

No CSV sidecar is allocated to this file (the salary-concept classification
catalog is configuration seeded in-model; the statutory dated rows it
consumes — SMM tables, promedio — live in file 01's sidecars; embargo
nominals are a config-gap family, never stored as legal data). D-H3
ingestion depth: monthly aggregates per contract from service start
(FR-375) — no payslip-level import surfaces exist in this file.

**Contract chassis and scope:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | ct_regime | select | full_ct · agro_small_salario_only (≤10 permanent agro workers — salario chapter only) · public_servicio_civil (outside CT payroll) | FR-371 |
| res.company | ct_permanent_headcount | integer (computed) | drives records regime: ≥10 libro / 3-9 planillas / ≤2 none | FR-392 |
| hr.contract | ct_service_start, ct_written_date | date | service start ≤ written date; retroactive anchor for ALL hire-date-depth accruals (D-H3); monthly-aggregate ingestion from service start | FR-373..FR-375 |
| hr.contract | ct_indefinido, ct_end_date, ct_jornada_hours | boolean/date/float | duration or indefinite flag + start (Art. 37.c); jornada semantics consumed from file 06 | FR-374 |
| hr.contract | ct_worker_class, ct_pay_period, ct_pay_basis | select | worker_class: manual · intellectual · domestic · a_domicilio; pay_period validation manual ≤ semana / intellectual+domestic ≤ mensual; pay_basis: tiempo_mes/quincena/semana/dia/hora · obra_pieza/tarea/destajo · participacion | FR-379, FR-382 |
| hr.contract | ct_payment_place_mode, ct_inkind_valuation | char/monetary | payment place default = workplace; in-kind benefits with agreed valuation (feeds FR-378 30% validation) | FR-374, FR-383 |

**Salary taxonomy (single classification source, consumed by id):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.salary.concept (new) | code, is_salario, classification, exclusion_reason, in_kind, valuation_basis | char/boolean/select | classification: salario (salario_fijo · prima · sobresueldo · bonificacion_habitual · ht_extra · descanso_trabajado · comision · participacion_utilidades) / no_salario (liberalidad_ocasional · gasto_representacion · transporte · elementos_trabajo · prestacion_social); in-kind ≤30% cash at cost; THE flag source for sibling bases (files 03/05/07/08, HN-TAX-FR-126) | FR-376..FR-378 |
| hr.payslip line | salario_completo_component | boolean | lines tagged ordinary/extraordinary feed the salario completo indemnity base (consumed by files 05/07/08) | FR-381 |

**Deductions and protection:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.deduction.type (new) | family, authorization_basis, consent_record, beneficiary | select/m2o | union_dues (union request + estatutos proof) · nonunion_60a (automatic, collective-contract gate) · cooperative_quota; ISR/IHSS/RAP NOT here — consumed by id | FR-385..FR-388 |
| hr.employee | ct_60a_exclusion_role | boolean/select | management/confianza roles exempt from Art. 60-A dues (gerente, subgerente, administrador, jefe de personal, jefe de departamento, secretario privado, confianza per collective contract/internal regs) | FR-386 |
| l10n_hn.embargo.protection (new) | floor_source, cap_pct_general, cap_pct_alimentos, cap_pct_room_food, nominal_slice | select/percent/boolean | floor = applicable SMM row (file 01 import) + vacaciones; caps 25 / 50 / 40; L100/L200 = dated config-gap rows (1959 nominals, D.14-1973 lead — never literal without modern LB) | FR-389 |
| l10n_hn.salary.advance (new) | amount, amortization_periods, per_period_amount | monetary/integer | amortization_periods ≥ 5; interest-free; terminal liquidation row | FR-390 |
| hr.employee settlement | privileged_credit | boolean | last-year wages + indemnities + prestaciones sociales; 30-day insolvency payment flag | FR-391 |

**Records, elevation and guards:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.payroll.record.surface (new) | regime, ot_separate | select/boolean | libro_salarios (≥10) · planilla_ihss (3-9); overtime lines booked separately from ordinary | FR-392, FR-393 |
| hr.contract wage | smm_floor_ref, elevated_to | m2o/monetary | auto-elevation rows on SMM vintage change (dated rows from file 01; snapshot-on-write per D15) | FR-394 |
| l10n_hn.ct.article.guard (new) | article_no, source, status, collision_of | char | live-in-print map; 85_ collision rows (28, 102-106, 153, 176, 182, 225, 263, 275, 296, 309, 317, 337, 346, 353, 368, 397..596) → verdict "CT effect: NONE"; negatives list (no aguinaldo/14th/INVI/integral/acoso CT articles); vintage ≤ D.278-2013 | FR-395..FR-398 |
## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic in the
LGPL client. No SaaS rows are introduced: none of these FRs touch the
thin-client/SaaS architecture split (no SEE/e-invoicing emission surface
here; the comprobante interface is consumed from e-invoicing/03 by id).
Model names stable across Odoo 17/18/19/20; version-specific behavior
recorded where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-371 | odoo | res.company | ct_regime flags | Scope gating of rule families; agro-small = salario-chapter-only rule activation; Servicio Civil = CT payroll rules off |
| FR-372 | odoo | hr.contract + hr.salary.rule guards | upward-only clamps | Override refusals / upward clamps at rule-engine level; ipso-jure nullity = never persist a below-floor wage row |
| FR-373..FR-375 | odoo | hr.contract | ct_service_start et al. | D15/D16: service-start anchor; D-H3 monthly-aggregate ingestion (no payslip import); corrections recompute with original-period rows; accrual consumers = files 05/07/08 by id |
| FR-376..FR-381 | odoo | l10n_hn.salary.concept + hr.payslip line tagging | is_salario / salario_completo_component | Single classification source consumed by id by files 03/05/07/08 + HN-TAX-FR-126; in-kind 30%-at-cost validation at concept level; equal-pay = advisory report only |
| FR-382..FR-384 | odoo | hr.contract (+ hr.payslip period validation) | ct_worker_class / ct_pay_period | Period ceilings by class; complete-liquidation-per-period check; profit-share advance + annual-liquidation calendar flag |
| FR-385..FR-388 | odoo | l10n_hn.deduction.type + hr.employee flags + hr.payslip deduction lines | authorization-gated types | 60-A automatic application with exclusion-role gate (role flags); union request + estatutos proof record; ISR/IHSS/RAP lines consumed by id (HN-TAX-FR-121..153, files 03/05); comprobante = HN-EINV-FR-139/140, worker-request-only (EV24:EVID-200) |
| FR-389 | odoo | l10n_hn.embargo.protection + hr.payslip garnishment lines | floors + caps | Caps 25/50/40 + SMM/vacaciones floors implementable; L100/L200 nominals = DATED config-gap rows (1959; D.14-1973 lead, OQ-002) — never literal lempira thresholds without modern LB; concurrent-order stacking on embargable remainder |
| FR-390, FR-391 | odoo | l10n_hn.salary.advance + settlement flag | ≥5-period amortization | Per-period recovery ≤ debt ÷ 5; interest-free enforced; privileged-credit informational flag on termination settlements |
| FR-392, FR-393 | odoo | l10n_hn.payroll.record.surface (report) | libro/planilla regime | Headcount-driven regime select; OT lines separated in outputs; IHSS planilla models = file 03 crossref |
| FR-394 | odoo | hr.contract wage rows + file 01 SMM import | auto-elevation | D12 version-regime: SMM bienio/acuerdo dated rows (file 01 owns values); elevation resolved by payslip period; D15 snapshot-on-write of the elevated wage; paid slips frozen (D16) |
| FR-395..FR-398 | odoo | l10n_hn.ct.article.guard (config data) | guard rows | R-H57 collision table + never-implement block; R-H60 negatives; R-H58/R-H59 article map; vintage pin ≤ D.278-2013 with 89_ routing for Art. 113.1; version-stable static config |

Version-regime notes (D12): FR-386 records the D.30-1973 origin (fn.11) of
Art. 60-A; FR-389 records the 1959 nominal vintage of the L100/L200
thresholds with the D.14-1973 cross-flag (config-gap discipline); FR-394
depends on file 01's SMM bienio cycle (mid-year vintages can straddle
periods — rows resolve by their own valid_from/valid_to); FR-398 records
the 86_ consolidation window (≤ 30-dic-2013). No adaptation windows or
go-live emission surfaces exist in this file's instruments (no D18/D19
rows required; the D-H3 historical ingestion surface is encoded at
FR-375).

## 6. Acceptance Criteria

- **AC-001:** Given a monthly payslip carrying a fixed salary L12,000, a
  habitual productivity bonus L1,500, commissions L800, an occasional
  year-end gratuity L2,000 (mere liberality) and a transport expense
  reimbursement L500, then the classification engine marks
  salario = 12,000 + 1,500 + 800 = L14,300 and no-salario = L2,500
  (FR-376, FR-377).
- **AC-002:** Given a rural worker with cash salary L10,000/month and
  food+housing supplied at cost and valued at L3,500, then the in-kind
  countable as salario = min(3,500, 30% × 10,000) = L3,000; given supply
  above cost, then L0 counts (FR-378).
- **AC-003:** Given a manual worker with a quincenal (15-day) pay period,
  then validation blocks the contract (period > 1 week); given an
  intellectual worker on monthly and a domestic worker on monthly, then
  both pass; given an a domicilio worker on weekly, then it passes
  (FR-382).
- **AC-004:** Given a termination month with ordinary earnings L20,000 and
  overtime earnings L4,000, then the salario completo indemnity base
  exposed to files 05/07/08 = L24,000 (ordinary + extraordinary)
  (FR-381).
- **AC-005:** Given a non-union worker in a company with a live collective
  contract who directly receives its benefits and holds no exclusion role,
  then the Art. 60-A deduction equal to the ordinary member quota applies
  automatically with no request record; given the same worker flagged
  *gerente* or *empleado de confianza*, then no 60-A deduction arises
  (FR-386).
- **AC-006:** Given a monthly salary at or below the applicable SMM row,
  then the embargable amount = L0 (minimum unembargable, plus vacaciones
  protection); given a 50% alimentos order on a higher salary, then the
  embargo computes on the 50% cap over the protected floors — while the
  L100 first-slice displays a dated-nominal config-gap flag and no literal
  lempira threshold is applied without a modern LB row (FR-389; OQ-002).
- **AC-007:** Given a L5,000 salary advance on a weekly pay period, then
  the recovery plan spreads over ≥5 periods (≤ L1,000/week) with zero
  interest; the terminal settlement liquidates any remainder (FR-390).
- **AC-008:** Given employers with 12, 7 and 2 permanent workers, then the
  records regime = Libro de Salarios, IHSS-model planillas, none
  respectively (FR-392).
- **AC-009:** Given a payslip with ordinary pay L12,000 and overtime
  L1,800, then the libro/planilla output books the overtime L1,800 on
  separate lines from the ordinary L12,000 (FR-393).
- **AC-010:** Given a contract wage of L13,000/month and a new SMM row of
  L14,917.20 with valid_from 1-jul, then payslips from July compute the
  wage at L14,917.20 (auto-elevation from the file 01 rows); a June
  correction recomputes with the June-period row (FR-394).
- **AC-011:** Given a user importing `85_` and marking CT Art. 368 as
  derogated, then the guard blocks the operation: D.93-2021 derogated
  Código Penal D.130-2017 Art. 368 only, and CT Art. 368 (pay periods /
  salario completo) remains live with verdict "CT effect: NONE"
  (FR-395).
- **AC-012:** Given a 13th-month concept configured with a CT article
  citation, then the negatives guard rejects it: no aguinaldo/décimo
  tercero article exists in the CT — the correct authority family is
  special law consumed from file 02 (`HN-PAYR-FR-051..090`) (FR-396).
- **AC-013:** Given a cesantía-pact configuration citing "CT Art. 95",
  then the anchor-correction note rewrites it to D.150-2008 Art. 2 printed
  at CT Art. 120-A fn.19 (R-H58) with the payroll mechanics consumed from
  files 05/08 (FR-397).
- **AC-014:** Given a termination record needing the Art. 113.1
  interpretation, then the vintage guard routes the authority to D.117-2021
  (file `89_`), never to the 86_ print whose window closes 30-dic-2013
  (FR-398).
- **AC-015:** Given a written contract registered 2026-03-01 whose Art. 37
  record states service start 2025-11-15, then all hire-date-depth accrual
  anchors compute from 2025-11-15 via D-H3 monthly aggregates (no payslip
  import), and tenure at 2026-11-15 = 12 months for the sibling tenure
  engines (FR-375).
- **AC-016:** Given a payslip whose deductions include ISR, IHSS, RAP
  fondo, union dues and a 60-A quota, then only the union-dues and 60-A
  lines are computed by this file's engines; the ISR/IHSS/RAP amounts are
  consumed by id from `HN-TAX-FR-121..153`, file 03 and file 05 — and the
  retention voucher is emitted only on worker request per
  `HN-EINV-FR-139/140` (FR-385..FR-388).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Consolidation vintage (`EV85:86_ OQ-1`): the 86_ CEDIJ print integrates instruments only through D.278-2013 (fn.36, p.152). Any CT reform of 2014-2026 silently missing from the print would not be reflected — most relevantly D.117-2021 (Art. 113.1 interp, file `89_`, routed by FR-398). Verify against an official current consolidation that no post-2013 reform touches this file's families (scope/contract/salario 360-390/deductions/protection/records) before treating 86_ quotes as current law. | no | Takumi S-HN4 + acquisition queue | open |
| OQ-002 | Embargo nominal thresholds (`EV85:86_ OQ-7`): Art. 371/373 L100/L200 figures are 1959 nominals with in-text "Véase Decreto No.14-1973" (unacquired — LEAD). FR-389 implements the percentage caps (25/50/40) and the SMM/vacaciones floors but carries the lempira slices as dated config-gap rows; pin the modern thresholds when D.14-1973 (or successor) is acquired. | no | acquisition queue | open |
| OQ-003 | 85_ registry mislabel (`EV85:85_ OQ-1`/`OQ-2`) → RESOLVED by R-H57: the guard (FR-395) encodes EVID-333's collision table, blocks any 85_-derived CT derogation flag and bars 85_ as a CT legal basis. Residual (report-only, outside this wave): recommend renaming the source registry entry to reflect its penal-family content (e.g. "85_Gaceta_35760_DO_93-2021_penal_derogaciones"). | no | controller / registry | resolved |
