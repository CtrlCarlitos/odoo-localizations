# HN — Payroll — Cesantía / preaviso / termination payouts: CT indemnity engines & final-settlement chassis

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the *Código del Trabajo*
(Labor Code, D. 189-59) termination-payout layer of cluster P10. It owns: (a)
the **preaviso** (statutory notice of termination) engine — the
24h/1w/2w/1m/2m tenure bands for indefinido contracts only, the in-lieu
payment rules (1.0× employer / 0.5× worker) and the paid weekly job-seeking
license; (b) the **auxilio de cesantía** (severance indemnity) engine — the
10-day/20-day/1-month-per-year bands with exact fraction proration, the
25-month cap (15 for microenterprises ≤10 employees), the lit. f) exclusion
evaluator, the ≥15-year voluntary-quit 35% and natural-death 75% variants, all
computed on the common Art. 123 base = last-6-month average ÷ days actually
worked (D. 65-1966); (c) the CT-side formulas exported by id to the RAP fondo
settlement engine (file 05) and the D. 150-2008 annual-pact grandfathering
mode; (d) the other termination payouts — fixed-term/obra salary-to-term
indemnity (capped), worker-side walk-away liability (≤30 days' damages),
*salarios caídos* (litigation back-wages), constructive-dismissal (*despido
indirecto*) parity, pregnancy-window stacked penalties, and probation-period
exemptions; (e) the settlement chassis — the Art. 125 *constancia*
(end-of-contract certificate), inalienability with the ½-alimony garnishment
exception, the 30-day insolvency privilege, the NEGATIVE finding that the CT
sets no general final-pay deadline, and the 2-month dismissal-claims
prescription; and (f) the D-H2/D-H3 ingestion surface — hire-date monthly
aggregates and frozen per-period rows feeding tenure and the 6-month averages.

It does **not** own: the RAP fondo offset/complement settlement engine, saldo
tracking and the 28-may-2024 vigencia boundary — file 05
(HN-PAYR-FR-181..215), which CONSUMES this file's exported amounts by id; SMM
values (file 01, HN-PAYR-FR-001..040); 13th/14th-month/bono mechanics (file
02, HN-PAYR-FR-051..087); IHSS cotizaciones/incapacidad (files 03/04,
HN-PAYR-FR-101..135 / 141..170 — this file only consumes IHSS status flags
for the lit. f) exclusions, never computes IHSS benefits); jornada/overtime
(file 06, HN-PAYR-FR-221..247); the vacaciones scale and its termination
cash-out (file 07, HN-PAYR-FR-261..280 — CT Arts. 345-356 per R-H59);
suspension causes and the maternity rest regime incl. its 180-day base (file
09, HN-PAYR-FR-331..357); the *salario completo* definition, general salary
protections and records (file 10, HN-PAYR-FR-371..405); the ISR treatment of
termination payouts through the plantilla engines (HN-TAX-FR-121..153,
taxation/04) and deduction semantics (HN-TAX-FR-046..078, taxation/02).

## 2. Legal Basis

Authority order (binding, per master evidence index): CT = `86_` (CEDIJ print
of D. 189-1959; consolidation window pinned through D. 278-2013 — fn. 36,
vintage caveat `EV85:86_ OQ-1`; fn. 19 = D. 150-2008, G 31,753, 5-nov-2008,
"Vigente a partir de su publicación"); the Art. 113.1 interpretation = `89_`
(D. 117-2021, corpus file) — cited there, never from the pre-2014 86_ print;
RAP cross-hook = `27_` (D. 47-2024 Art. 6); `85_` = mislabel guard ONLY
(R-H57: D. 93-2021 derogates zero CT articles). R-H59 article map applies:
preaviso/cesantía family = Arts. 111-126 + 862-867; vacaciones = Arts.
345-356 (file 07); no aguinaldo articles exist in the CT (file 02 territory,
special law). D-H1/D-H2/D-H3 bind every cluster (dated rows,
hecho-generador/period resolution, never-guess rule).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código del Trabajo (D. 189-1959), Arts. 46-48 | Contract modalities: "El contrato individual de trabajo puede ser: a) Por tiempo indefinido, cuando no se especifica fecha para su terminación; b) Por tiempo limitado, cuando se especifica fecha para su terminación o cuando se ha previsto el acaecimiento de algún hecho o circunstancia como la construcción de una obra…; y, c) Para obra o servicios determinados…"; Art. 47 recharacterization: "Los contratos relativos a labores que por su naturaleza sean permanentes o continuas en la empresa, se considerarán como celebrados por tiempo indefinido aunque en ellos se exprese término de duración…El tiempo de servicio se contará desde la fecha de inicio de la relación de trabajo, aunque no coincida con la del otorgamiento del contrato por escrito" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 46-48 pp.16-17 (EV85:EVID-297) |
| LB-002 | CT, Arts. 49-52 (período de prueba) | "El período de prueba, que no puede exceder de sesenta (60) días…Este período será remunerado…"; Art. 50: written stipulation required, otherwise the general contract rules apply; Art. 52: "Los trabajadores en período de prueba gozan de todas las prestaciones, a excepción del preaviso y la indemnización por despido. Si antes de transcurrido un (1) año se celebra nuevo contrato entre las mismas partes contratantes y para la misma clase de trabajo, deberá entenderse éste por tiempo indefinido, sin que tenga lugar en este caso el período de prueba" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 49-52 p.18 (EV85:EVID-298) |
| LB-003 | CT, Arts. 111-112 (termination causes; patrono just causes) | Art. 111: "Son causas de terminación de los contratos de trabajo: 1. Cualquiera de las estipuladas en ellos…; 2. El mutuo consentimiento de las partes; 3. Muerte del trabajador…; 10. Ejercicio de las facultades que conceden a las partes los artículos 112 y 114…; 12. Resolución del contrato decretada por autoridad competente. En los casos previstos en los siete (7) primeros incisos…la terminación del contrato no acarreará responsabilidades para ninguna de las partes"; Art. 112 lists the patrono just causes a)-l) for dismissal without liability | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 111-112 pp.42-44 (EV85:EVID-301) |
| LB-004 | CT, Art. 113 + fn.17 (salarios caídos; reinstatement) | "…Si el patrono no prueba dicha causa debe pagar al trabajador las indemnizaciones que según este Código le puedan corresponder y, a título de daños y perjuicios, los salarios que éste habría percibido desde la terminación del contrato hasta la fecha en que con sujeción a las normas procésales del presente Código debe quedar firme la sentencia condenatoria respectiva"; fn.17 (D. 89-1969): "…los Tribunales de Justicia, no deben hacer deducción alguna del tiempo que dure el juicio…"; reinstatement branch: the reinstated worker "no tiene derecho a las indemnizaciones correspondientes al despido injustificado; pero si a los salarios que hubiere dejado de percibir…"; the Art. 113.1 interpretation is governed by `89_` (D. 117-2021), which the 86_ print predates | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 113 pp.44-45 (EV85:EVID-302) |
| LB-005 | CT, Arts. 114-115 (worker just causes; despido indirecto; worker liability) | Art. 114: "Son causas justas que facultan al trabajador para dar por terminado el contrato de trabajo, sin preaviso y sin responsabilidad de su parte, conservando el derecho a las prestaciones e indemnizaciones legales, como en el caso de despido injusto:" — lit. f): "No pagarle el patrono el salario completo que le corresponda, en la fecha y lugar convenidos o acostumbrados, salvo las deducciones autorizadas por la ley"; lit. i): "Incumplimiento, de parte del patrono, de las obligaciones convencionales o legales"; Art. 115: the worker failing to prove his causes "debe el trabajador pagarle el importe del preaviso y los daños y peruicios [sic] que haya ocasionado, según estimación prudencial que deben hacer dichos tribunales. Si se trata de contratos a plazo fijo o para obra determinada, deberá pagarle únicamente los daños y perjuicios correspondientes. Por cualquiera de las causas que enumera el artículo anterior, constitutivas de despido indirecto, el trabajador puede separarse de su puesto conservando su derecho a percibir las indemnizaciones y prestaciones legales que procedan" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 114-115 pp.44-47 (EV85:EVID-303) |
| LB-006 | CT, Arts. 116-119 (preaviso) | Art. 116: "…Durante el término de éste el trabajador que va a ser despedido tiene derecho a licencia remunerada de un (1) día en cada semana a fin de que pueda buscar nueva colocación. El preaviso será notificado con anticipación así: a) De veinticuatro (24) horas, cuando el trabajador ha servido a un mismo patrono de modo continúo menos de tres (3) meses; b) De una (1) semana, cuando le haya servido de tres (3) a seis (6) meses; c) De dos (2) semanas, cuando le haya servido de seis (6) meses a un (1) año; d) De un (1) mes, cuando le ha servido de uno (1) a dos (2) años; y e) De dos (2) meses, cuando le ha servido por más de dos (2) años. Dichos avisos pueden omitirse por cualquiera de las partes pagando a la otra la cantidad que le corresponda según lo dispuesto en el artículo 118"; Art. 117: notice in writing, personally; "Después no podrá alegar validamente causales o motivos distintos"; Art. 118: "El trabajador culpable de no haber dado el preaviso…quedará obligado a pagar al patrono una cantidad equivalente a la mitad del salario que corresponda al término del preaviso. En caso de que el patrono sea el culpable quedará obligado a pagar al trabajador una cantidad equivalente a su salario durante el término del preaviso"; Art. 119: "El término del preaviso empezará a contar desde el día siguiente al de la notificación respectiva" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 116-119 pp.47-48 (EV85:EVID-304) |

| LB-007 | CT, Art. 120 (auxilio de cesantía) + fn.19 (reforma D. 150-2008) | "Si el contrato de trabajo por tiempo indeterminado concluye por razón de despido injustificado, o por alguna de las causas previstas en el artículo 114 u otra ajena a la voluntad del trabajador, o según se regula en éste artículo por retiro voluntario o por fallecimiento del trabajador, el patrono deberá pagarle a éste un auxilio de cesantía de acuerdo con las siguientes reglas: a) Después de un trabajo continuo no menor de tres (3) meses ni mayor de seis (6), con un importe igual a diez (10) días de salario; b) Después de un trabajo continuo mayor de seis (6) meses pero menor de un (1) año, con un importe igual a veinte (20) días de salario; c) Después de un trabajo continuo mayor de un (1) año, con un importe igual a un (1) mes de salario, por cada año de trabajo y si los servicios no alcanzan a un (1) año, en forma proporcional al plazo trabajado; d) En ningún caso podrá exceder dicho auxilio del salario de veinticinco (25) meses; e) El auxilio de cesantía deberá pagarse aunque el trabajador pase inmediatamente a servir a las órdenes de otro patrono"; lit. f): no entitlement for the worker who at contract end is automatically protected by a State- or IHSS-granted "jubilación, pensión de vejez o de retiro…cuyo valor actuarial sea equivalente o mayor" to the indemnity, nor one who takes up the IHSS "Seguro contra el desempleo involuntario" by the dismissal itself, nor on professional-risk death where the employer proves insurance, nor on natural death with IHSS death-risk coverage; lit. g): "También tendrá derecho al auxilio de cesantía después de un trabajo continuo de quince (15) años o más, si el trabajador decide voluntariamente dar por terminado un contrato de trabajo, tendrá derecho a recibir un treinta y cinco (35) por ciento del importe que le correspondería por los años de servicio según los literales c) y d) de este artículo; en caso de fallecimiento natural después de seis (6) meses de laborar, el porcentaje se eleva a un setenta y cinco (75%) por ciento pagadero a sus beneficiarios. El beneficio anterior será aplicable siempre y cuando no se presenten las circunstancias previstas en el artículo 112 de este Código o cuando el trabajador este acogido a los beneficios señalados en el literal f)…"; fn.19: "Reforma del artículo 120 y 120-A adicionado por Decreto No.150-2008…La Gaceta No.31,753 de fecha 5 de noviembre de 2008. Vigente a partir de su publicación" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 120 pp.48-49 + fn.19 p.49 (EV85:EVID-305) |
| LB-008 | CT, Art. 120-A (microempresas) + fn.19 second block (D. 150-2008 Art. 2 annual pact) | "Las microempresas definidas como toda unidad económica con un máximo de diez (10) empleados remunerados, no les será aplicable el contenido del literal g) del artículo anterior, y en relación al literal d) están obligadas a reconocer quince (15) meses en concepto de auxilio de cesantía"; fn.19 second block (D. 150-2008 Art. 2): "Los trabajadores y patronos podrán pactar a favor del trabajador, el pago patronal anual de un importe equivalente del auxilio de cesantía, teniendo dichos pagos las consideraciones siguientes: 1- Si el contrato de trabajo termina por causas imputables al patrono y como consecuencia de ello el trabajador adquiere el derecho de pago de cesantía, los pagos efectuados se aplicarán a la cancelación de los derechos adeudados, sin perjuicio del derecho del trabajador de demandar su reintegro. 2- Si la terminación del contrato fuese por causa imputable al trabajador, y por lo tanto éste no adquiere el derecho de pago de la cesantía, los pagos efectuados por el patrono quedan a favor del trabajador, y; 3- Los pagos citados en los numerales 1) y 2) no serán incorporados en los importes para el cálculo de beneficios laborales" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Art. 120-A p.49 + fn.19 second block p.49 (EV85:EVID-306) |
| LB-009 | CT, Arts. 121-123 + fn.20 (fixed-term indemnity; damages; indemnity common rules) | Art. 121: "…será indemnizado por el patrono con el importe del salario que habría devengado en el tiempo que falte para que se venza el plazo o para que finalice la obra; pero en ningún caso la cantidad podrá exceder de la que le correspondería según los términos del artículo anterior si hubiere sido contratado por tiempo indefinido"; Art. 122: "…el monto de los daños y perjuicios no podrá exceder al salario correspondiente a treinta (30) días"; Art. 123: "a) El importe de los mismos no podrá ser objeto de compensación, venta o cesión, ni podrá ser embargado, salvo en la mitad, por concepto de pensiones alimenticias; b) La Indemnización que corresponda se calculará tomando como base el promedio de salarios devengados por el trabajador durante los últimos seis (6) meses que tenga de vigencia del contrato, o fracción de tiempo menor si no se hubiere ajustado dicho término; c) La continuidad del trabajo no se interrumpe por enfermedad, vacaciones, huelga o paros legales…"; fn.20 (D. 65-1966): "El cálculo…debe hacerse tomando como base el promedio de los salarios devengados por el trabajador en los días efectivamente trabajados durante los últimos seis (6) meses…" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 121-123 pp.49-50 + fn.20 p.50 (EV85:EVID-307) |
| LB-010 | CT, Arts. 124, 144, 146 (pregnancy/lactancia dismissal protection) | Art. 124: "El patrono no podrá dar por terminado el contrato de trabajo de la mujer embarazada sin justificar previamente ante el Juez de Trabajo respectivo, alguna de las causales enumeradas en el artículo 112"; Art. 144: "Se presume que el despido se ha efectuado por motivo de embarazo o lactancia, cuando a tenido lugar dentro del período del embarazo o dentro de los tres (3) meses posteriores al parto, y sin la autorización de que trata el artículo siguiente. La trabajadora despedida sin autorización de la autoridad tiene derecho al pago de una indemnización equivalente a los salarios de sesenta (60) días, fuera de las indemnizaciones y prestaciones a que hubiere lugar de acuerdo con el contrato de trabajo, y además, al pago de las diez (10) semanas de descanso remunerado de que trata este Capítulo, si no lo ha tomado"; Art. 146: "…la trabajadora tiene derecho como indemnización al doble de la remuneración de los descansos no concedidos" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 124, 144, 146 pp.50, 56-57 (EV85:EVID-308) |
| LB-011 | CT, Arts. 125-126 + 374 (constancia; liquidation; insolvency 30 days; NO general deadline) | Art. 125: "A la terminación de todo contrato de trabajo, cualquiera que sea la causa que la haya motivado, el patrono debe dar gratuitamente al trabajador una constancia que exprese: a) La fecha de iniciación y terminación de las labores; b) La clase de trabajo desempeñado; y, c) El salario devengado durante el último período de pago. Si el trabajador lo desea, la constancia deberá expresar también: a) La eficiencia y comportamiento del trabajador; y, b) La causa o causas de la terminación del contrato"; Art. 126: "Las indemnizaciones previstas en los artículos 116, 120 y 121 procederán también cuando el patrono liquide o cese en sus negocios, voluntariamente o no. En caso de insolvencia, concurso, quiebra, embargo, sucesión u otros similares, gozarán los créditos que por estos conceptos correspondan a los trabajadores de un privilegio especialísimo sobre todos los demás acreedores de la masa, excepto los alimentarios; y el curador depositario, ejecutor testamentario o interventor, estarán obligados a pagarlos dentro de los treinta (30) días siguientes al reconocimiento formal…"; Art. 374: privileged wage/indemnity credits payable "dentro de los treinta (30) días siguientes al reconocimiento formal que el Juez de Trabajo haga de dichos crédritos [sic], o en el momento que hayan fondos"; NEGATIVE: the CT fixes NO general final-settlement payment deadline — only the insolvency-context 30-day rules (`EV85:86_ OQ-2`) | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 125-126 p.51; Art. 374 p.108 (EV85:EVID-309) |
| LB-012 | CT, Arts. 862-867 (prescription) | Art. 864: "Los derechos y acciones de los trabajadores para reclamar contra los despidos injustificados…prescriben en el término de dos (2) meses contados a partir de la terminación del contrato…"; Art. 867 final ¶: the prescription term for overtime claims "empezará a contarse el día en que fue pagado o debió pagarse el salario ordinario correspondiente al período" | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | Arts. 862-867 pp.267-268 (EV85:EVID-326) |
| LB-013 | D. 47-2024 (RAP fondo de reserva laboral), Art. 6 | Termination matrix (cross-hook; settlement engine owned by file 05): "El monto constituido como reserva laboral junto con sus rendimientos en caso de despido injustificado será deducido del valor a percibir por el(a) trabajador(a) en concepto de auxilio de cesantía. En el caso que el saldo…fuese superior al Auxilio de Cesantía correspondiente, dicha diferencia…también debe ser otorgada al trabajador(a) en concepto de Compensación Laboral a la Estabilidad en el Empleo o Prima de Antigüedad"; on any other termination cause the saldo pays 100% as *prima de antigüedad*, the employer complementing at the 35% floor (voluntary quit, >15 years' continuous service) and the 75% floor (death/total invalidity, non-occupational, ≥6 months; the law cross-refs CT Art. 120 lit. f); RAP pays within one month; preaviso is never mentioned — untouched | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 6 pp.3-5 (EV27:EVID-279) |
| LB-014 | D. 93-2021 (G 35,760) — mislabel guard only | Art. 1: "Derogar los artículos 102, 103…596; todos del Decreto No.130-2017…que contiene el CÓDIGO PENAL" — zero Código del Trabajo articles derogated, reformed or added; the derogated PENAL numbers (102-106, 176, 182, 225, 263, 275, 309, 317, 337, 346, 368, 397, 403, 411, 417, 430, 434, 437, 444, 469, 511, 569, 596) numerically collide with live CT articles (112, 337, 346, 368, 417…) but are NOT them (R-H57; EVID-333 collision table) | `hn/sources/85_Gaceta_35760_DO_93-2021_derogaciones_CT.pdf` | 93-Arts. 1-2 pp.A.2-A.3; cross-check table (EV85:EVID-329; EV85:EVID-333) |

## 3. Functional Requirements

### 3.1 Termination taxonomy, modality gate and computation bases

- **HN-PAYR-FR-291:** The system shall maintain a termination-cause catalog
  mapped to a payout matrix — CT Art. 111's twelve causes, with causes 1-7 and
  12 flagged no-liability (no preaviso/cesantía) and cause 10 branching to the
  dismissal (Art. 112), worker-quit (Arts. 114/115) and event engines of this
  file — and the catalog is LIVE law notwithstanding file `85_`/D. 93-2021,
  which derogates only Código Penal articles (R-H57 collision guard: penal
  numbers 112/337/346/368/417 collide numerically with live CT articles —
  zero CT effect). (LB-003; LB-014; EV85:EVID-301; EV85:EVID-333)
- **HN-PAYR-FR-292:** The system shall gate the preaviso/cesantía engines on
  contract modality: they apply ONLY to *contratos por tiempo indefinido*
  (indefinite-term contracts); fixed-term (*plazo fijo*) and
  obra/servicios-determinados contracts route to the Art. 121 indemnity
  engine (FR-309); and per Art. 47, contracts for work that is by its nature
  permanent or continuous in the enterprise shall be RECHARACTERIZED as
  indefinido notwithstanding an expressed term when at expiry the originating
  cause or subject matter subsists, with service time counted from the start
  of the relation even when it precedes the written contract.
  (LB-001; EV85:EVID-297)
- **HN-PAYR-FR-293:** The system shall compute tenure as continuous service
  from the hire date per contract, ingesting MONTHLY AGGREGATES per contract
  from the hire date (D-H3 depth (a); no payslip-level import), and shall not
  interrupt continuity for sickness, vacaciones, legal *huelga* (strike) or
  *paros legales* (legal lockouts) per Art. 123.c.
  (LB-001; LB-009; EV85:EVID-297; EV85:EVID-307)
- **HN-PAYR-FR-294:** The system shall compute every indemnity of this file
  (preaviso in-lieu, cesantía, Art. 121 indemnity, the damages-valuation
  base) on the common Art. 123 base: the average of salaries earned over the
  last six months of the contract (or the shorter fraction when tenure is
  below six months), computed as Σ *salario completo* (complete salary =
  ordinary + extraordinary hours) ÷ DAYS EFFECTIVELY WORKED in the period
  (interpretation D. 65-1966, fn. 20); the *salario completo* composition is
  consumed from file 10 (HN-PAYR-FR-371..405) by range, never re-derived
  here. (LB-009; EV85:EVID-307)
- **HN-PAYR-FR-295:** The system shall resolve every settlement of this file
  at the termination date as *hecho generador* (triggering event, D-H2):
  bases are computed from per-period rows frozen at their original periods;
  paid slips are frozen; corrections recompute with ORIGINAL-period rows;
  filed periods are write-protected; and resolved band/cap/percentage values
  are snapshot-on-write onto the settlement record (D15).
  (LB-009; EV85:EVID-307)

### 3.2 Preaviso engine (Arts. 116-119)

- **HN-PAYR-FR-296:** The system shall implement the preaviso scale for
  indefinido contracts as dated config bands keyed to tenure resolved at the
  termination date: less than 3 months → 24 hours; 3 to 6 months → 1 week;
  6 months to 1 year → 2 weeks; 1 to 2 years → 1 month; more than 2 years →
  2 months. (LB-006; EV85:EVID-304)
- **HN-PAYR-FR-297:** The system shall implement the in-lieu rules: either
  party may omit the notice by paying the other — the employer owes an amount
  equal to the salary DURING the notice term (1.0 × term); the worker owes
  HALF the salary of the notice term (0.5 × term), each valued on the FR-294
  base. (LB-006; EV85:EVID-304)
- **HN-PAYR-FR-298:** The system shall grant, during a worked notice term, a
  paid license of one (1) day per week for job-seeking, without salary
  reduction. (LB-006; EV85:EVID-304)
- **HN-PAYR-FR-299:** The system shall enforce notice mechanics: the preaviso
  is given in writing and personally; after notification no other causes may
  validly be alleged (Art. 117); and the term counts from the day AFTER
  notification (Art. 119). (LB-006; EV85:EVID-304)

### 3.3 Cesantía engine (Arts. 120 / 120-A)

- **HN-PAYR-FR-300:** The system shall gate the *auxilio de cesantía* on the
  qualifying events of Art. 120: unjustified dismissal (*despido
  injustificado*); termination under Art. 114 causes (*despido indirecto*);
  other causes beyond the worker's will; qualifying voluntary quit (FR-305);
  and worker death (FR-306) — and shall NOT pay cesantía on proven Art. 112
  just-cause dismissal or unqualified quits.
  (LB-007; EV85:EVID-305)
- **HN-PAYR-FR-301:** The system shall compute the cesantía amount exactly
  per Art. 120 literals a)-c): tenure ≥3 and ≤6 months → 10 DAYS of salary;
  >6 months and <1 year → 20 DAYS of salary; >1 year → one MONTH of salary
  per year of work with the incomplete-year fraction prorated to time worked
  ("…un (1) mes de salario, por cada año de trabajo y si los servicios no
  alcanzan a un (1) año, en forma proporcional al plazo trabajado" — the
  fraction clause covers the year fraction beyond completed years per the
  EVID-305 gloss); day-multiples are valued at the FR-294 daily base and
  month-multiples at the average monthly *salario completo* of the same
  6-month window, with the month-equivalence for non-monthly pay bases
  carried as a configuration gap (OQ-006), never guessed.
  (LB-007; EV85:EVID-305)
- **HN-PAYR-FR-302:** The system shall cap the cesantía at 25 months'
  salary ("En ningún caso podrá exceder dicho auxilio del salario de
  veinticinco (25) meses"), applied after proration.
  (LB-007; EV85:EVID-305)
- **HN-PAYR-FR-303:** The system shall apply the microenterprise variant:
  economic units with a maximum of ten (10) remunerated employees owe a
  cesantía cap of FIFTEEN (15) months and literal g) (the ≥15-year
  voluntary-quit 35%) does not apply to them; the headcount measurement rule
  is a configuration gap (OQ-005). (LB-008; EV85:EVID-306)
- **HN-PAYR-FR-304:** The system shall implement the lit. f) exclusion
  evaluator — NO cesantía when: (i) at contract end the worker is
  automatically protected by a State- or IHSS-granted *jubilación*, *pensión
  de vejez* or *retiro* whose actuarial value is equivalent or greater than
  the indemnity; (ii) the worker takes up the IHSS involuntary-unemployment
  insurance by the fact of the dismissal; (iii) death from professional risk
  where the employer proves the worker was insured against it; or (iv) death
  from other cause with the deceased covered against death risk at IHSS.
  (LB-007; EV85:EVID-305)
- **HN-PAYR-FR-305:** The system shall compute the ≥15-year voluntary-quit
  variant: after fifteen (15) or more years of continuous service, a worker
  who voluntarily terminates receives THIRTY-FIVE PERCENT (35%) of the amount
  corresponding for years of service per literals c) and d); applicable only
  when no Art. 112 circumstances exist and the worker is not under lit. f)
  benefits. (LB-007; EV85:EVID-305)
- **HN-PAYR-FR-306:** The system shall compute the death variant: natural
  death after six (6) or more months of service raises the percentage to
  SEVENTY-FIVE PERCENT (75%), payable to the worker's legal beneficiaries,
  subject to the lit. f) insured-death exclusions (FR-304 (iii)/(iv)); the
  fondo-side mirror (employer complement vs the RAP saldo) is owned by file
  05 (HN-PAYR-FR-181..215) — cited both directions by range.
  (LB-007; LB-013; EV85:EVID-305; EV27:EVID-279)
- **HN-PAYR-FR-307:** The system shall pay cesantía regardless of immediate
  re-employment ("…aunque el trabajador pase inmediatamente a servir a las
  órdenes de otro patrono" — lit. e). (LB-007; EV85:EVID-305)
- **HN-PAYR-FR-308:** The system shall trigger the Arts. 116/120/121
  indemnities also when the employer liquidates or ceases business,
  voluntarily or not (Art. 126 first clause).
  (LB-011; EV85:EVID-309)

### 3.4 Other termination payouts

- **HN-PAYR-FR-309:** The system shall compute the fixed-term/obra dismissal
  indemnity: a worker under *plazo fijo* or obra contracts dismissed without
  just cause — or separating under Art. 114 causes — is indemnified with the
  salary they would have earned for the time remaining to term or obra
  completion, NEVER exceeding the amount that would correspond under Art. 120
  for an indefinido contract (the below-3-months cap edge is a configuration
  gap — OQ-004 — flagged, never guessed). (LB-009; EV85:EVID-307)
- **HN-PAYR-FR-310:** The system shall compute worker-side walk-away
  liability on unjustified quit: indefinido contracts → the preaviso amount
  (FR-297 worker leg) plus damages estimated prudentially by the labor
  courts; fixed-term/obra contracts → damages only; and the worker-caused
  damages ceiling = 30 days' salary (Art. 122), valued on the FR-294 base.
  (LB-005; LB-009; EV85:EVID-303; EV85:EVID-307)
- **HN-PAYR-FR-311:** The system shall reserve *salarios caídos* (lapsed
  wages) on unjustified dismissal: indemnities PLUS, as damages, the wages the
  worker would have earned from termination until the condemnatory sentence
  is firm, with NO deduction for the duration of the trial (fn. 17,
  D. 89-1969); the end date is judgment-supplied, not payroll-dated; and the
  Art. 113.1 interpretation is governed by `89_` (D. 117-2021) — cite `89_`,
  never the 86_ print, for that point. (LB-004; EV85:EVID-302)
- **HN-PAYR-FR-312:** The system shall support the reinstatement
  alternative: a reinstated worker (demand for *cumplimiento del contrato*)
  retains the missed salaries but NOT the unjustified-dismissal indemnities.
  (LB-004; EV85:EVID-302)
- **HN-PAYR-FR-313:** The system shall implement constructive dismissal
  (*despido indirecto*) parity: termination under any Art. 114 just cause —
  including non-payment of the complete salary at the agreed or customary
  date and place (lit. f) and breach of legal/conventional obligations
  (lit. i)) — allows the worker to separate WITHOUT preaviso and without
  worker liability, conserving ALL *prestaciones* and legal indemnities as in
  unjustified dismissal (preaviso in-lieu + cesantía + the file-07
  vacaciones cash-out by range). (LB-005; EV85:EVID-303)
- **HN-PAYR-FR-314:** The system shall gate dismissals of pregnant/lactating
  workers: within the presumption window (pregnancy + three (3) months
  postpartum) the employer cannot terminate without prior judicial
  justification; an unauthorized in-window dismissal stacks ON TOP of the
  ordinary termination payouts: 60 days' wages + the value of the untaken
  10-week paid rest + double remuneration of nursing rests not conceded —
  with the maternity-rest regime and its 180-day average base owned by file
  09 (HN-PAYR-FR-331..357), consumed by range.
  (LB-010; EV85:EVID-308)
- **HN-PAYR-FR-315:** The system shall implement the *período de prueba*
  (probation period) exemptions: probation capped at 60 days, paid,
  written-only (absent written stipulation the general contract rules apply);
  during probation either party may terminate without liability, and
  probationary workers are exempt ONLY from preaviso and the dismissal
  indemnity — all other *prestaciones* accrue; rehire within one (1) year
  between the same parties for the same class of work = indefinido contract
  with no new probation. (LB-002; EV85:EVID-298)

### 3.5 RAP interplay and the D. 150-2008 annual pact

- **HN-PAYR-FR-316:** The system shall export the CT-side reference amounts
  computed by this file — preaviso, cesantía (including the FR-305/306
  35%/75% base amounts) and the Art. 121 indemnity — as an id-addressed
  input consumed by file 05's RAP fondo offset/complement settlement engine
  (HN-PAYR-FR-181..215): on despido injustificado the CT cesantía is the
  reference from which the fondo saldo + *rendimientos* is deducted (any
  excess paid to the worker); on other causes the fondo pays 100% as *prima
  de antigüedad* with the 35%/75% employer-complement floors (R-H55; cited
  by range both directions, no re-derivation).
  (LB-013; LB-007; EV27:EVID-279; EV85:EVID-305)
- **HN-PAYR-FR-317:** The system shall keep the two engines' outputs
  distinct: the 35%/75% CT entitlement amounts of FR-305/306 (payable by the
  employer where no fondo settlement applies, e.g. grandfathered-pact
  employers) versus the fondo-side complement-floor computations of file 05
  (comparing the RAP saldo against the same CT base) are separate ledger
  rows never netted inside this file; and preaviso is NEVER offset,
  deducted or interfered with by the fondo (D. 47-2024 Art. 6 mentions only
  *auxilio de cesantía* — `EV27:27_ OQ-5` confirmation carried as OQ-003).
  (LB-013; LB-007; EV27:EVID-279; EV85:EVID-305)
- **HN-PAYR-FR-318:** The system shall carry the D. 150-2008 annual-pact
  grandfathering flag anchored at CT Art. 120-A fn. 19 (R-H58; NOT
  "CT-Art.-95 pacts" — gloss drift corrected): pact-registered employers and
  workers agree the annual employer payment of a cesantía-equivalent amount;
  on termination imputable to the employer the payments made are CREDITED
  against the cesantía debt, without prejudice to the worker's right to
  demand reimbursement; the flag is the CT-side input to file 05's
  fondo-exemption evaluation (HN-PAYR-FR-181..215).
  (LB-008; EV85:EVID-306)
- **HN-PAYR-FR-319:** The system shall EXCLUDE annual-pact payments from
  every benefit-calculation base of the payroll ("…no serán incorporados en
  los importes para el cálculo de beneficios laborales" — fn. 19 numeral 3):
  they enter neither the FR-294 6-month average nor any vacaciones/13th/14th
  average owned by files 07/02. (LB-008; EV85:EVID-306)
- **HN-PAYR-FR-320:** The system shall leave forfeited pact payments with
  the worker: when termination is imputable to the worker (no cesantía right
  arises), annual-pact payments already made STAY in the worker's favor
  (fn. 19 numeral 2). (LB-008; EV85:EVID-306)

### 3.6 Settlement chassis

- **HN-PAYR-FR-321:** The system shall produce the end-of-contract
  *constancia* (certificate of employment) free of charge at every
  termination regardless of cause, with mandatory fields: (a) labor start
  and end dates; (b) class of work performed; (c) salary earned in the last
  pay period; and, only at the worker's request: efficiency/behavior and
  the termination cause(s). (LB-011; EV85:EVID-309)
- **HN-PAYR-FR-322:** The system shall enforce inalienability on every
  indemnity of this file: no compensation, sale or assignment; garnishable
  (*embargo*) ONLY up to one half for *pensiones alimenticias* (alimony)
  (Art. 123.a). (LB-009; EV85:EVID-307)
- **HN-PAYR-FR-323:** The system shall implement the insolvency/liquidation
  privilege: worker credits for these indemnities and *prestaciones* are
  privileged over all other creditors of the estate except *alimentarios*,
  payable within thirty (30) days of the formal recognition by the Juez de
  Trabajo (or as funds exist). (LB-011; EV85:EVID-309)
- **HN-PAYR-FR-324:** The system shall encode the NEGATIVE finding that the
  CT fixes NO general final-settlement payment deadline: the only statutory
  deadlines are the insolvency-context 30-day rules (FR-323); no "pay within
  X days of termination" rule shall be implemented, defaulted or guessed —
  the deadline surface is a configuration gap until an LB from the CT
  Reglamento or STSS practice is acquired (`EV85:86_ OQ-2`).
  (LB-011; EV85:EVID-309)
- **HN-PAYR-FR-325:** The system shall stamp the dismissal-claims
  prescription flag: two (2) months from contract termination (Art. 864),
  recorded as a dispute-window date on the settlement record.
  (LB-012; EV85:EVID-326)

## 4. Data Model

No CSV sidecar is allocated to this file: the band/cap/percentage sets are
small and live as DATED config rows (D-H2 — additive-only, never replaced in
place; the preaviso/cesantía scale dates to the 1959 CT text as consolidated
in the 86_ print, with the D. 150-2008 literals dated 2008-11-05 per fn. 19
"Vigente a partir de su publicación"). Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.ct.preaviso.band (new) | tenure_from, tenure_to, notice_value, notice_unit, in_lieu_factor_patrono, in_lieu_factor_trabajador, valid_from, valid_to | char/int/select/date | bands: <3m→24 hours · 3-6m→1 week · 6m-1y→2 weeks · 1-2y→1 month · >2y→2 months; factors 1.0 / 0.5; license 1 paid day/week | FR-296..FR-299 |
| l10n_hn.ct.cesantia.rule (new) | band, multiplier_unit, multiplier_value, cap_months, pct_voluntary_quit, pct_death, valid_from, valid_to, instrument | select/int/date/char | bands: d10 (3-6m) · d20 (6m-1y) · month_per_year (>1y, fraction prorated); caps: 25 (general) · 15 (micro ≤10); pct 35 (lit. g) / 75 (natural death ≥6m) — D. 150-2008 rows valid_from 2008-11-05; exclusion catalog: pension_protected · ihss_unemployment · insured_risk_death · insured_natural_death | FR-300..FR-308 |
| l10n_hn.ct.settlement (new) | contract_id, employee_id, event, event_date, modality, preaviso_due, preaviso_in_lieu, cesantia_base_daily, cesantia_base_monthly, cesantia_amount, cap_applied, art121_amount, worker_damages, salarios_caidos_reservation, pregnancy_rows, exclusion_flags, beneficiaries, prescription_date, constancia_id | m2o/select/date/monetary/boolean | full settlement record; event catalog per FR-291; snapshot-on-write of resolved band/cap/pct (D15); recompute uses original-period rows (D16) | FR-291..FR-325 |
| hr.contract | l10n_hn_ct_modality, l10n_hn_ct_recharacterized, l10n_hn_prueba_start, l10n_hn_prueba_end, l10n_hn_ct_annual_pact | select/boolean/date | indefinido · plazo_fijo · obra; Art. 47 recharacterization; prueba ≤60d written; D. 150-2008 pact flag | FR-292, FR-315, FR-318 |
| hr.employee | l10n_hn_ct_exclusion_pension, l10n_hn_ct_exclusion_unemployment, l10n_hn_ct_death_insured, l10n_hn_ct_beneficiary_ids | boolean/m2o | lit. f) exclusion predicates (IHSS/public-pension status consumed as flags — never computed here); death-75% beneficiaries | FR-304, FR-306 |
| res.company | l10n_hn_ct_microenterprise | boolean | ≤10 remunerated employees (measurement rule = OQ-005) | FR-303 |
| l10n_hn.ct.cesantia.pact.ledger (new) | contract_id, period, amount, credited_on_settlement_id, forfeited | m2o/date/monetary/boolean | annual pact rows; credit on employer-imputable termination; forfeited rows stay with worker; excluded from all benefit bases | FR-318..FR-320 |
| l10n_hn.payroll.monthly.aggregate | contract_id, period, salario_completo_total, days_worked | m2o/date/monetary/int | D-H3 hire-date ingestion (tenure + 6-month averages); frozen per-period rows, additive-only | FR-293..FR-295 |
| l10n_hn.ct.settlement.export (new) | settlement_id, amount_kind, amount, consumer | m2o/select/monetary | amount_kind: preaviso · cesantia_ct · cesantia_35_base · cesantia_75_base · art121; consumer = file 05 settlement engine (HN-PAYR-FR-181..215) by id | FR-316, FR-317 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living
in the LGPL client. No `saas`/`shared` rows are introduced: none of these FRs
touch the thin-client/SaaS architecture split (no DTE-like external channel
exists for CT settlements in the corpus). Model names stable across Odoo
17/18/19/20 (`hr.departure` available since 16); version-specific behavior
recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-291 | odoo | hr.departure.reason (catalog) + l10n_hn.ct.settlement | cause→payout matrix | R-H57 guard recorded on the catalog (85_ = penal-only, zero CT effect); causes 1-7+12 no-liability flags; cause 10 branches |
| FR-292, FR-315 | odoo | hr.contract | ct_modality, recharacterized, prueba dates | Art. 47 recharacterization compute on renewal/expiry; prueba ≤60d validation + written-only rule; rehire-within-1y → indefinido, no new prueba |
| FR-293 | odoo | hr.contract + l10n_hn.payroll.monthly.aggregate | hire-date aggregates | D-H3 (a): monthly aggregates per contract, no payslip-level import; D12 ingestion contract documented on the model |
| FR-294, FR-295 | odoo | l10n_hn.ct.settlement compute + frozen payslip rows | 6-month average ÷ days worked | D-H2: original-period recompute for corrections; D15 snapshot-on-write; D16 filed-period protection; salario completo consumed from file 10 (HN-PAYR-FR-371..405) |
| FR-296..FR-299 | odoo | l10n_hn.ct.preaviso.band + hr.contract notice workflow | dated band rows | D12: bands statutory since the 1959 text (86_ print vintage through D. 278-2013 — OQ-001); in-lieu 1.0×/0.5×; 1 paid day/week license; day-after-notification start |
| FR-300..FR-308 | odoo | l10n_hn.ct.cesantia.rule + l10n_hn.ct.settlement | cesantía compute | D12: lit. g)/death-75% dated 2008-11-05 (D. 150-2008 fn. 19); caps 25/15 as dated rows; D15/D16: resolved values snapshot on the settlement; exclusion predicates as worker flags |
| FR-309, FR-310 | odoo | l10n_hn.ct.settlement branches | art121 + worker liability | Art. 121 cap; 30-day damages ceiling; <3m cap edge = OQ-004 flag |
| FR-311, FR-312 | odoo | l10n_hn.ct.settlement (salarios caídos reservation) | judgment-dated rows | End date = firm-sentence input (judgment-dated, D-H2 discipline); citation discipline: Art. 113.1 interp = 89_ (D. 117-2021) |
| FR-313, FR-314 | odoo | hr.departure + l10n_hn.ct.settlement stacks | constructive parity; pregnancy stack | Maternity rest regime + 180-day base consumed from file 09 (HN-PAYR-FR-331..357) by range |
| FR-316, FR-317 | odoo | l10n_hn.ct.settlement.export | reference amounts | Consumed by file 05 (HN-PAYR-FR-181..215) by id — R-H55; RAP vigencia boundary 28-may-2024 owned by file 05; preaviso never offset (OQ-003) |
| FR-318..FR-320 | odoo | l10n_hn.ct.cesantia.pact.ledger + hr.contract/res.company flags | pact mode | R-H58 anchor (D. 150-2008 Art. 2 at CT-Art. 120-A fn. 19); base-exclusion hooks to files 02/07 averages; forfeit rule |
| FR-321 | odoo | ir.actions.report (QWeb) on l10n_hn.ct.settlement | constancia | Mandatory fields a-c; optional d-e on worker request |
| FR-322 | odoo | garnishment cap hook on settlement lines | ½ alimony only | Ordering with the file-10 embargo engine (HN-PAYR-FR-371..405) by range |
| FR-323, FR-324 | odoo | l10n_hn.ct.settlement workflow + config-gap flag | insolvency 30d; deadline gap | Never-guess: no default deadline (OQ-002); insolvency branch = recognition-date + 30 days |
| FR-325 | odoo | l10n_hn.ct.settlement.prescription_date | 2-month window | Computed from termination date (Art. 864) |

Version-regime notes (D12): the preaviso/cesantía scales ride the 86_
consolidation vintage (through D. 278-2013 — OQ-001); the D. 150-2008
literals (lit. g 35%, death 75%, 120-A, annual pact) carry valid_from
2008-11-05 with additive-only rows; the RAP-boundary regime date (28-may-2024)
is owned by file 05 and consumed by id. D15/D16: every resolved
band/cap/percentage is snapshot-on-write onto the settlement record and
corrections recompute with original-period rows. D18/D19: not applicable —
this file owns no historical-GL or go-live posting surface (settlements are a
payroll computation surface; GL effects flow through standard payslip
journal posting owned elsewhere).

## 6. Acceptance Criteria

- **AC-001:** Given indefinido contracts ending at 5 months, 14 months and
  26 months of tenure, then the preaviso bands selected are 1 week, 1 month
  and 2 months respectively; given a fixed-term contract at any tenure, then
  no preaviso band is selected (Art. 121 branch instead) (FR-292, FR-296).
- **AC-002:** Given a monthly salary of L20,000.00 and 3 years' tenure
  (notice = 2 months), when the employer omits notice, then the in-lieu
  payment = L40,000.00 (1.0 × 2 months); when the worker omits notice, then
  the worker owes L20,000.00 (0.5 × term) (FR-297).
- **AC-003:** Given a worked 60-day notice term, then at least 8 paid
  job-seeking license days (1 per week) are granted with no salary reduction
  (FR-298).
- **AC-004:** Given a last-6-month Σ salario completo of L72,000.00 over 120
  days actually worked, then the daily indemnity base = 72,000 ÷ 120 =
  L600.00 (FR-294).
- **AC-005:** Given 8 months' tenure, then cesantía = 20 days × L600.00 =
  L12,000.00; given 1 year 8 months' tenure with average monthly salario
  completo L20,000.00, then cesantía = 20,000 × (1 + 8/12) = L33,333.33
  (fraction prorated per lit. c) (FR-301).
- **AC-006:** Given 30 years' tenure and average monthly salary L20,000.00,
  then the prorated 30 months are capped at 25 → L500,000.00 (FR-302).
- **AC-007:** Given a microenterprise (≤10 employees, flag set) with the same
  30-year worker, then the cap is 15 months → L300,000.00; and a voluntary
  quit after 15+ years yields L0.00 under lit. g) (inapplicable to micro)
  (FR-303).
- **AC-008:** Given a worker who at contract end draws an IHSS pension of
  actuarial value ≥ the cesantía, then the exclusion flag suppresses the
  cesantía to L0.00 with the exclusion reason recorded (FR-304).
- **AC-009:** Given a voluntary quit at 18 years with average monthly salary
  L15,000.00, then the lit. c)+d) base = 18 months = L270,000.00 and the
  35% variant pays L94,500.00 (FR-305).
- **AC-010:** Given natural death after 2 years of service (≥6 months) with
  average monthly salary L15,000.00 and no lit. f) insurance exclusion, then
  the beneficiaries receive 75% × (2 months × 15,000) = L22,500.00 (FR-306).
- **AC-011:** Given a 12-month fixed contract unjustifiably dismissed at
  month 4 (monthly salary L15,000.00, unexpired 8 months, daily base
  L600.00), then salary-to-term = L120,000.00 but the Art. 121 cap at 4
  months' tenure = 10 days × 600 = L6,000.00 → the indemnity paid is
  L6,000.00 (FR-309).
- **AC-012:** Given an unjustified quit at 3 years (monthly L15,000.00,
  daily base L600.00), then the worker owes the half-preaviso L15,000.00
  (0.5 × 2 months) plus court-estimated damages never exceeding 30 × 600 =
  L18,000.00 (FR-310).
- **AC-013:** Given an in-window pregnant worker dismissed without judicial
  authorization (daily base L600.00, rest untaken), then the settlement
  stacks 60 × 600 = L36,000.00 plus the 10-week-rest value and 2× nursing
  rests computed per file 09's maternity base, on top of the ordinary
  preaviso/cesantía rows (FR-314).
- **AC-014:** Given termination at day 45 of a written prueba period, then
  preaviso and dismissal indemnity are suppressed while all other
  prestaciones (vacaciones-type accruals) remain intact (FR-315).
- **AC-015:** Given a worker who quits for documented non-payment of the
  complete salary (Art. 114.f), then the settlement carries full unjustified-
  dismissal parity: preaviso in-lieu + cesantía + the file-07 vacaciones
  cash-out, with no worker-side liability row (FR-313).
- **AC-016:** Given an unjustified-dismissal settlement, then a salarios
  caídos reservation row exists with an empty end date until the firm-sentence
  date is supplied, and no mitigation deduction is applied (FR-311).
- **AC-017:** Given a cesantía of L40,000.00 subject to an alimony order,
  then at most L20,000.00 (½) is garnishable and no compensation/sale/cession
  of the indemnity is bookable (FR-322).
- **AC-018:** Given any termination, then the constancia prints fields a)-c)
  mandatorily and d)-e only when the worker requests them (FR-321).
- **AC-019:** Given the settlement screen, then no statutory final-pay
  deadline value is populated and the deadline config-gap flag is raised
  (`86_` OQ-2) — never a defaulted X-days rule (FR-324).
- **AC-020:** Given a despido-injustificado settlement with CT cesantía
  L500,000.00 (AC-006 numbers), then the export record carries
  cesantia_ct = 500,000.00 for file 05's offset engine while the preaviso
  row is marked non-offsettable (FR-316, FR-317).
- **AC-021:** Given a pact-mode employer with two annual rows of L15,000.00
  and a worker-fault termination, then the L30,000.00 stays with the worker
  (forfeit rule) and the amounts are absent from every benefit average
  (FR-318..FR-320).
- **AC-022:** Given a termination dated 2026-03-15, then the
  dismissal-claims prescription flag date = 2026-05-15 (2 months)
  (FR-325).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `EV85:86_ OQ-1` consolidation vintage: the 86_ CEDIJ print integrates instruments only through D. 278-2013 (fn. 36). Any 2014-2026 CT reform touching Arts. 46-52/111-126/862-867 would be silently missing — most relevantly D. 117-2021 (Art. 113.1 interpretation, corpus file `89_`), which FR-311 already cites from `89_`. Verify against an official current consolidation before freezing quotes as current law. | no | Takumi S-HN4 + acquisition | open |
| OQ-002 | `EV85:86_ OQ-2` NO general final-pay deadline: the CT contains no "pay final settlement within X days of termination" rule — only insolvency-context 30-day rules (Arts. 126/374). FR-324 encodes the gap; the deadline LB must come from the CT Reglamento or STSS practice. LEAD. | no | acquisition queue | open |
| OQ-003 | `EV27:27_ OQ-5` preaviso-RAP interplay: D. 47-2024 Art. 6 offsets the fondo only against auxilio de cesantía and never mentions preaviso — FR-317 configures preaviso as untouched. Confirm note (originated in the RAP evidence file; to be countersigned by file 05). | no | Takumi S-HN4 + file 05 owner | open (confirm) |
| OQ-004 | Art. 121 cap edge (synthesis, this file): the fixed-term indemnity is capped at "what Art. 120 would give if indefinido", but Art. 120 bands start at 3 months — a fixed-term worker dismissed with <3 months' service has an Art. 120 equivalent of L0.00. Never-guess: the cap is encoded as written with the edge flagged; confirm doctrinal/STSS reading before freezing. | no | Takumi S-HN4 | open |
| OQ-005 | Microenterprise headcount measurement (synthesis): Art. 120-A defines "máximo de diez (10) empleados remunerados" but not the measurement date/convention (at termination? average period?). FR-303 leaves the measurement as dated config; pin before go-live. | no | Takumi S-HN4 | open |
| OQ-006 | Month-unit for non-monthly pay bases (synthesis): "un (1) mes de salario" in Art. 120.c is the average monthly salario completo for monthly-paid workers; the day-equivalence (e.g. 30 days) for daily/obra-paid workers is not printed in the corpus — FR-301 carries it as a config gap, never derived (no 360-day divisor exists in the CT). | no | Takumi S-HN4 | open |

| OQ-007 | NEW (V-HN1 adversarial review): exact-one-year band edges — preaviso's statutory "de seis meses a un año" band and cesantía's ">6 months and <1 year" / "more than 1 year" bands leave the exactly-one-year boundary formally unassigned (inclusive "de…a" reading vs strict inequalities); no AC tests the boundary. Ruling needed: which band owns tenure of exactly 1.0 year for preaviso AND for cesantía's first-year proration. | no | controller ruling | open |