# HN — Payroll — RAP fondo de reserva laboral, FOVIIF cotizaciones and the D. 40-2026 regularization window

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for Honduras' private-pension
RAP layer created by D. 47-2024 (Ley del Fondo de Reserva Laboral de
Capitalización Individual, in force 28-may-2024) and amended in scope by
D. 40-2026 (regularización + FOVIIF integration). It owns: the **stacked
employer loads** (R-H56) — the employer-only 4% *fondo de reserva laboral*
(labor-reserve fund) contribution on *salario ordinario* (ordinary salary)
capped at 3 × SMM *en su nivel más alto* (at its highest level) plus the
employer 1.5% RAP *cotización* on the IHSS-IVM-excess base — and the
**worker-side RAP entries**: the 1.5% retention on the same IVM-excess base
(*IHSS-worker-share kin*, a payslip deduction line), RAP-loan repayment
retentions, the ≤15-días-calendario remittance calendar, the per-worker
*cuenta individual* (individual account) model, and the RAP Consejo Directivo
rate-change watch; the base-definition and universality **config-gap flags**
(salario ordinario undefined; techo level-set DECIDE; Art. 43
universality/pre-reform values — flagged, never guessed); the **termination
settlement engine** applying the coexists-with-offset matrix (R-H55) — CT
cesantía offset on *despido injustificado* (unjustified dismissal), 100%
fondo payout as *prima de antigüedad* otherwise, 35%/75% employer complement
floors, preaviso untouched, ≤1-month RAP payout, *inembargabilidad*
(unattachability, alimony-only 50% exception) — CONSUMING file 08's CT
formulas by range; the grandfathering carve-out for pre-existing annual
cesantía/prima pacts (R-H58); the ISR interface (Art. 14 exclusions, paired
by id with taxation/04's plantilla); the **D. 40-2026 regularization window**
(28-mar-2026 → 28-sep-2026, full waiver for never-affiliates; post-window
full retro + ≤60-month plans; Pensiones→FOVIIF integration); the
**affiliation exceptions** (INJUPEMP/INPREMA/IPM/INPREUNAH, diplomatic
convenios, prevision-plan survival); registration/notification duties (60-day
windows); and the D-H3 hire-date ingestion depth for fondo saldo modeling.

It does **not** own: the CT cesantía/preaviso formulas and scales — file 08
`08_cesantia-preaviso.md` (HN-PAYR-FR-291..325), consumed by range; the IHSS
IVM contribution ceiling rows — file 03 IHSS cotizaciones
(HN-PAYR-FR-101..135), consumed by range; SMM values/bienio rows and the SMM
*promedio* (average) feed — file 01 SMM (HN-PAYR-FR-001..040) and the
ISR-side 10 × SMM promedio caps = taxation/04 (HN-TAX-FR-121..153,
specifically FR-134) — the fondo techo NEVER shares that config (R-H56(c));
the ISR plantilla/asalariados withholding engines and pension-deduction
semantics = taxation/04 (`HN-TAX-FR-121..153`, FR-130/FR-132 legs) and
taxation/02 (HN-TAX-FR-046..078), consumed by id; IHSS incapacidad (file 04,
HN-PAYR-FR-141..170); jornada, vacaciones, suspension/maternity and
salary/records mechanics (files 06/07/09/10 by range); the RAP sancionatorio
procedure and FOVIIF benefit/retiro conditions (RAP reglamentos — unacquired
leads, placeholder flags only); and DJIMR/export surfaces (S-HN3, none owed
by this file).

## 2. Legal Basis

Authority order (binding, per master evidence index): the RAP fondo/cotización
layer = `27_` (D. 47-2024, G 36,545 of 28-may-2024) — including its Art. 16
TRANSCRIPTION of the reformed Ley RAP (D.L. 107-2013) Arts. 42/43/61, the
full text of which remains UNACQUIRED and doubly load-bearing (acquisition
lead 1); the regularization window and FOVIIF integration = `28_`
(D. 40-2026, G 37,106 of 28-mar-2026). D-H1/D-H2/D-H3 bind everything:
every statutory value below = dated rows `valid_from` 28-may-2024 (or
28-mar-2026 for the window/integration), additive-only, resolved at the
payslip period / hecho generador, never "today".

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D. 47-2024, Considerandos 3/5 + Art. 17 | Lineage and vigencia: RAP is "una institución sin fines de lucro, que administra recursos de naturaleza privada, con el objetivo social de proveer servicios financieros que contribuyan a mejorar la calidad de vida y condición socioeconómica de los(as) trabajadores(as) mediante aportaciones obrero-patronales"; SCJ "declaró mediante Sentencia de inconstitucionalidad recaída en el Recurso No. SCO-858-2015, la derogatoria total del Decreto No.56-2015 del 21 de Mayo de 2015 «…» contentivo de la Ley Marco del Sistema de Protección Social; Sentencia que fue mandada a publicar por este Poder del Estado y que consta en el Diario Oficial 'La Gaceta' de fecha 27 de Octubre de 2022, lo que conllevó a la supresión del Régimen del Seguro de Cobertura Laboral del cual se derivaba el Fondo de Reserva Laboral, dando como resultado que a la fecha las aportaciones patronales no se encuentren reguladas en un marco legal para tal finalidad"; Art. 17: "El presente Decreto entrará en vigencia el día de su publicación en el Diario Oficial 'La Gaceta'" (= G 36,545, 28-may-2024; Congreso 30-abr-2024; Ejecútese 9-may-2024). D.56-2015 fondo → SCJ void → D.47-2024 re-creates it inside RAP; vigencia boundary 28-may-2024 | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Considerandos 3/5 pp.1-2; Art. 17 p.8 (EV27:EVID-275) |
| LB-002 | D. 47-2024, Arts. 1-3 | Object/scope/administration: the Law creates the Fondo de Reserva Laboral de Capitalización Individual in RAP "con la finalidad de garantizar los derechos adquiridos de las y los trabajadores"; "La presente Ley es de orden público y social obliga a todas las personas naturales o jurídicas no estatales, que rijan sus relaciones laborales conforme al Código del Trabajo"; RAP administers the Fondo "constituido por los aportes que realice el patrono a efecto de garantizar el pago por concepto de cesantía o prima de antigüedad a los (las) trabajadores(as) una vez que haya terminado la relación individual de trabajo", under CNBS supervision (Ley RAP Art. 33). Private/non-state CT-governed employers only; fondo funded by EMPLOYER aportes only | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Arts. 1-3 pp.2-3 (EV27:EVID-276) |
| LB-003 | D. 47-2024, Art. 4 | THE fondo contribution: "El Fondo de Reserva Laboral de Capitalización Individual, constituido en el Régimen de Aportaciones Privadas (RAP) será integrado con los aportes patronales obligatorios equivalentes al cuatro por ciento (4%) mensual del salario ordinario, con base a un techo de cotización obligatoria de tres (3) salarios mínimos en su nivel más alto. Las aportaciones realizadas por el patrono deben acreditarse a nombre expreso del trabajador(a) en la cuenta individual en el Régimen de Aportaciones Privadas (RAP). Dichas cuentas de capitalización individual serán objeto de regulación por la Comisión Nacional de Bancos y Seguros (CNBS) «…»". Employer 4% monthly of salario ordinario, ceiling 3 × SMM "en su nivel más alto" (instrument unnamed; NOT promedio); per-worker cuenta individual; "salario ordinario" undefined in the law (27_ OQ-1) | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 4 p.3 (EV27:EVID-277) |
| LB-004 | D. 47-2024, Art. 5 | Pacto prohibition + grandfathering: "Queda prohibido a los trabajadores y patronos realizar pactos o acuerdos para cambiar, sustituir o modificar las características establecidas para la cuenta individual de Reserva Laboral creada mediante la presente Ley. Los patronos que, a su entrada en vigencia, ya tuvieren pactado por acuerdos individuales o colectivos o por leyes especiales, el pago anual del auxilio de cesantía o prima de antigüedad, no están obligados(as) a constituir la Reserva Laboral de Capitalización Individual, deduciendo la misma del pago acordado o en su defecto conforme a lo convenido entre ambas partes". Pre-existing ANNUAL cesantía/prima arrangements exempt the fondo constitution (grandfathering anchor D. 150-2008 Art. 2 at CT-Art. 120-A fn.19, R-H58) | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 5 p.3 (EV27:EVID-278) |
| LB-005 | D. 47-2024, Art. 6 | Termination payout matrix: ¶1: any termination cause → worker "tendrá derecho a percibir de parte del Régimen de Aportaciones Privadas (RAP) el valor constituido en la cuenta de Reserva Laboral de Capitalización Individual a su nombre". ¶2 (*despido injustificado*): "El monto constituido como reserva laboral junto con sus rendimientos «…» será deducido del valor a percibir por el(a) trabajador(a) en concepto de auxilio de cesantía. En el caso que el saldo «…» fuese superior al Auxilio de Cesantía correspondiente, dicha diferencia, independientemente del monto resultante, también debe ser otorgada al trabajador(a) en concepto de Compensación Laboral a la Estabilidad en el Empleo o Prima de Antigüedad". ¶3: any other cause → saldo + rendimientos paid "en concepto de Prima por Antigüedad en concepto de Compensación Laboral a la Estabilidad". ¶4 (voluntary quit): 100% of the saldo; employer must complement "si el saldo de la cuenta en el RAP es inferior al treinta y cinco por ciento (35%) del importe que le correspondería como indemnización por auxilio de cesantía, en el caso de aquellos trabajadores con una antigüedad superior de quince (15) años de servicios continuos". ¶5 (death / total non-occupational invalidity, ≥6 months): 100% to beneficiaries/worker; employer complements if saldo "es inferior al setenta y cinco por ciento (75%) del importe que le correspondería como indemnización por Auxilio de Cesantía, según lo dispuesto en el Artículo 120 literal f) del Código de Trabajo". ¶6 (death): delivery to RAP-designated beneficiaries or by registered heredero sentence. ¶7: RAP "debe establecer un procedimiento expedito para que en un plazo no mayor de un (1) mes se entere el valor constituido en la cuenta de reserva laboral". Preaviso never mentioned — untouched (27_ OQ-5) | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 6 pp.3-5 (EV27:EVID-279) |
| LB-006 | D. 47-2024, Art. 7 | Affiliation exceptions + prevision survival: excepted from mandatory affiliation: workers "cotizantes al Instituto Nacional de Jubilaciones y Pensiones de los Empleados y Funcionarios del Poder Ejecutivo (INJUPEMP), al Instituto Nacional de Previsión del Magisterio (INPREMA), al Instituto de Previsión Militar (IPM), al Instituto de Previsión Social de los Empleados de la Universidad Nacional Autónoma de Honduras (INPREUNAH), así como las delegaciones diplomáticas y organismos internacionales acreditados en el país, cuando éstos tengan convenios que implique un tratamiento diferente de aseguramiento de su personal. Los planes y programas de previsión social existentes en el sector privado y las instituciones del Estado, autorizados por la Secretaría de Estado en los Despachos de Trabajo y Seguridad Social y reguladas por el Código del Trabajo, deben continuar vigentes en beneficio de los(as) trabajadores(as), salvo que los beneficios de la presente Ley fueran superiores a las ya reguladas". Mas-favorable comparison predicate, not a wholesale exemption | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 7 p.5 (EV27:EVID-280) |
| LB-007 | D. 47-2024, Arts. 8-10 | Transition (no retro 4%): Art. 9: administration of all funds RAP "haya captado a la fecha con ocasión de la aplicación de la Ley Marco del Sistema de Protección Social se sujetará a lo establecido en la presente Ley"; pending Ley-Marco payment requests proceed under RAP procedures; Art. 10: RAP is authorized "para que continue (sic) administrando los recursos constituidos a nombre de cada trabajador previo a la entrada en vigencia de la presente Ley" and to capture/administer the Fondo de Reserva Laboral from vigencia; Art. 8: RAP may invest per its institutional plans under CNBS "sana, segura y rentable administración". No retroactive 4% obligation is enacted for pre-vigencia periods; accrual-start rule for pre-vigencia workers open (27_ OQ-4) | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Arts. 8-10 pp.5-6 (EV27:EVID-281) |
| LB-008 | D. 47-2024, Arts. 11-13 + 15 | Inembargabilidad + sanctions frame: Art. 11: "Las aportaciones y cotizaciones de los trabajadores y patronos a todos los Fondos administrados por el Régimen de Aportaciones Privadas (RAP), así como las prestaciones otorgadas en el marco de la presente Ley, no pueden ser objeto de transacciones que no estén fijadas en la Ley, ni podrán ser embargadas, ni sujetas a cualquier otra medida cautelar, salvo por concepto de pensión alimenticia hasta en un cincuenta por ciento (50%)". Art. 12: the employer who fails affiliation/remittance obligations "será sujeto al régimen sancionatorio que para tales efectos establezca el Régimen de Aportaciones Privadas (RAP)" (unspecified — acquisition lead). Art. 13: RAP reglamentación remitted to CNBS knowledge; Art. 15: RAP exempt from taxes/duties | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Arts. 11-13, 15 pp.6-7 (EV27:EVID-282) |
| LB-009 | D. 47-2024, Art. 14 | ISR treatment: "Los aportes efectuados a las cuentas individuales del Fondo de Reserva Laboral de Capitalización Individual, realizadas por el patrono, no formarán parte de la renta neta gravable para el Impuesto Sobre la Renta. Adicionalmente, los valores recibidos por los (las) trabajadores(as) en concepto de prestaciones derivados de los fondos establecidos en esta Ley no formarán parte de la renta bruta para efectos del cálculo del Impuesto Sobre la Renta". Double worker-side exclusion (contribution + payout); employer-side expense deductibility NOT addressed — no inference | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 14 pp.6-7 (EV27:EVID-283) |
| LB-010 | D. 47-2024, Art. 16 (first reform: Ley RAP D.L. 107-2013 Art. 42) — TRANSCRIPTION | Universal registration duty: "Todo patrono, persona natural o jurídica, está obligado a inscribirse e inscribir a sus trabajadores en el registro de cotizantes del Régimen de Aportaciones Privadas (RAP) a más tardar dentro de los sesenta (60) días siguientes a la publicación de la presente Ley en el Diario Oficial La Gaceta; igualmente deben notificar al Régimen de Aportaciones Privadas (RAP) las nuevas contrataciones de trabajadores obligados a cotizar, o del cese de los mismos, dentro de los sesenta (60) días posteriores a la fecha de ocurrencia del nombramiento o cesantía. Asimismo…". NOTE: transcription of the reformed Ley RAP article inside D.47-2024, ending in a printed ellipsis — complete reform text may be missing (27_ OQ-6); full D.L. 107-2013 UNACQUIRED (doubly load-bearing lead). Universality signal for the Art. 43 cotización obligations; initial window reads 28-may-2024 + 60 days (~27-jul-2024) | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 16 first reform p.7 (EV27:EVID-284) |
| LB-011 | D. 47-2024, Art. 16 (second/third reforms: Ley RAP Arts. 43 + 61) — TRANSCRIPTION | The RAP cotización layer: reformed Art. 43: "El Patrono aportante debe retener el uno punto cinco por ciento (1.5%) del salario mensual ordinario de cada trabajador, el que debe enterar al Régimen de Aportaciones Privadas (RAP) juntamente con la aportación patronal del uno punto cinco por ciento (1.5%) para totalizar el tres por ciento (3%) que se registrará como ahorro a favor del trabajador en una cuenta individual a su nombre; el pago lo hará el patrono directamente al Régimen de Aportaciones Privadas (RAP) o por medio de las entidades recaudadoras autorizadas por aquel, dentro de los quince (15) días calendario siguientes a la retención. La retención se hará sobre el monto que exceda el techo establecido para las contribuciones destinadas al Régimen de Invalidez, Vejez y Muerte (IVM) del Instituto Hondureño de Seguridad Social (IHSS). El Consejo Directivo con el voto favorable del sector productivo puede modificar el porcentaje de cotización tanto del trabajador como del patrono. Las certificaciones extendidas por el Departamento contable del Régimen de Aportaciones Privadas (RAP) sobre el adeudo a cargo de la empresa infractora, tiene el carácter de título ejecutivo. El patrono está obligado a retener del salario los créditos otorgados a los afiliados del Régimen de Aportaciones Privadas (RAP) y enterarlos en la misma fecha en que entregue la retención mensual de la empresa". Reformed Art. 61: "Queda derogada toda disposición que se oponga a lo dispuesto en la presente Ley". Worker 1.5% retention + employer 1.5% = 3% ahorro; base = excess over the IHSS IVM techo (worker-side literal; patronal base ambiguous — 27_ OQ-3); 15 días calendario; rate-change power; título ejecutivo; RAP-loan retentions; pre-reform values unknown (27_ OQ-3) | `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | Art. 16 reforms pp.7-8 (EV27:EVID-285) |
| LB-012 | D. 40-2026, Considerandos 3-6 | Three-fund taxonomy: RAP "actualmente administra tres (3) fondos": (1) "creado en la Ley del Régimen de Aportaciones Privadas (RAP), que se denomina Fondo de Vivienda e Inclusión Financiera (FOVIIF)"; (2) "denominado Fondo de Pensiones, el cual fue creado por mandato de la Ley Marco del Sistema de Protección Social, contenido en el Decreto No. 56-2015 «…» continúa existiendo únicamente para la administración, inversión y protección de los fondos acumulados «…» pero, se encuentra cerrado a la captación de nuevas aportaciones"; (3) "el Fondo de Reserva Laboral de Capitalización Individual creado mediante Decreto No. 47-2024". Regularization rationale: significant unaffiliated employers "principalmente por limitaciones de liquidez para asumir pagos retroactivos acumulados, especialmente en micro, pequeñas y medianas empresas «…» sin obligación de pagar aportaciones retroactivas, ni intereses, multas, recargos o sanciones derivadas de la falta de afiliación previa". FOVIIF/Pensiones share the IVM previsional purpose (OIT C102). Two LIVE streams stack into two distinct funds — no merging, no offset | `hn/sources/28_Decreto_40-2026_reg_RAP.pdf` | Considerandos 3-6 pp.11-12 (EV27:EVID-286) |
| LB-013 | D. 40-2026, D40-Art. 1 | The regularization window: "Se concede un período excepcional de regularización de seis (6) meses, contado a partir de la entrada en vigencia del presente Decreto, para que las empresas que no se encuentren afiliadas al Régimen de Aportaciones Privadas (RAP) puedan hacerlo. Durante este período las empresas privadas podrán afiliarse e iniciar el pago de las aportaciones y cotizaciones obrero-patronales correspondientes al Fondo de Vivienda e Inclusión Financiera (FOVIIF) y al Fondo de Reserva Laboral de Capitalización Individual, sin obligación de pagar aportaciones correspondientes a períodos anteriores o retroactivas, ni intereses, multas, recargos o sanciones derivadas de la falta de afiliación previa al RAP. Esta medida de regularización no es aplicable a las empresas que ya han sido afiliadas al RAP y que actualmente se mantienen en mora, ni a las empresas que tengan convenios de pago vigentes, los cuales deberán cumplirse al tenor de sus términos". Window 28-mar-2026 → ~28-sep-2026 (calendar convention open, 28_ OQ-1); both live funds; full waiver for never-affiliates only | `hn/sources/28_Decreto_40-2026_reg_RAP.pdf` | D40-Art. 1 pp.12-13 (EV27:EVID-287) |
| LB-014 | D. 40-2026, D40-Art. 2 | Post-window liability + plans: "Vencido el plazo establecido en el Artículo anterior, los empleadores que no se hayan acogido al proceso de regularización deberán pagar la totalidad de las aportaciones obrero-patronales adeudadas conforme a la legislación vigente. Se autoriza al Régimen de Aportaciones Privadas (RAP) para celebrar con los empleadores planes de pago o mecanismos de financiamiamiento (sic) por plazos de hasta sesenta (60) meses, conforme a su normativa interna y políticas institucionales". Full retro from each obligation's own start; ≤60-month RAP plans (normativa not in corpus) | `hn/sources/28_Decreto_40-2026_reg_RAP.pdf` | D40-Art. 2 p.13 (EV27:EVID-288) |
| LB-015 | D. 40-2026, D40-Arts. 3-4 | FOVIIF integration + vigencia: "Se autoriza integrar al Fondo de Vivienda e Inclusión Financiera (FOVIIF) los recursos acumulados en el Fondo de Pensiones administrado por el RAP durante la vigencia de la Ley Marco del Sistema de Protección Social (Decreto No.56-2015) «…» La integración autorizada garantiza los derechos adquiridos de los afiliados al RAP «…» estarán sujetos a las condiciones de beneficios, retiro y devolución establecidos en los reglamentos aprobados por el RAP para el Fondo de Vivienda e Inclusión Financiera (FOVIIF) de acuerdo a la Ley del Régimen de Aportaciones Privadas vigente. La Comisión Nacional de Bancos y Seguros (CNBS) velará «…»". Art. 4: vigencia = publication day = 28-mar-2026 (also the window start). Balance-level merge preserving derechos adquiridos; conditions delegated to RAP reglamentos (unacquired — 28_ OQ-3) | `hn/sources/28_Decreto_40-2026_reg_RAP.pdf` | D40-Arts. 3-4 pp.13-14 (EV27:EVID-289) |

## 3. Functional Requirements

### 3.1 Regime scope, vigencia and fund taxonomy

- **HN-PAYR-FR-181:** The system shall apply the fondo/cotización obligation
  predicate exactly: every *persona natural o jurídica no estatal* (non-state
  natural or juridical person) whose labor relations are governed by the
  Código del Trabajo is obliged — State employees are out (their regimes are
  the Art. 7 exceptions, FR-212) — and the fondo is funded by EMPLOYER
  aportes only: workers never contribute to the 4% fondo (their RAP entry is
  solely the 1.5% retention of FR-186 and RAP-loan retentions of FR-190).
  (LB-002; LB-003; EV27:EVID-276/277)
- **HN-PAYR-FR-182:** The system shall treat 28-may-2024 (D. 47-2024
  publication, Art. 17) as the `valid_from` boundary of every statutory row
  of this file, shall NEVER back-accrue the 4% fondo for pre-vigencia
  service (Arts. 9-10 only sweep already-captured Ley-Marco funds and keep
  pre-existing per-worker cuentas alive at RAP), and shall carry the
  fund-state lineage metadata D.56-2015 → SCJ Sentencia SCO-858-2015
  (published 27-oct-2022) → D.47-2024 for migration history.
  (LB-001; LB-007; EV27:EVID-275/281)
- **HN-PAYR-FR-183:** The system shall model RAP's three-fund taxonomy with
  live/closed contribution-destination flags: FOVIIF (Ley-RAP-created;
  destination of the reformed-Art. 43 3% ahorro), Fondo de Pensiones
  (D.56-2015; closed to new aportes — legacy balances only), and Fondo de
  Reserva Laboral (D.47-2024 4%); the two live streams never merge, offset
  or cross-credit (see FR-188). (LB-012; EV27:EVID-286)

### 3.2 Stacked contribution loads and worker retention

- **HN-PAYR-FR-184:** The system shall accrue the employer fondo
  contribution — 4% monthly of *salario ordinario* with a contribution
  ceiling of 3 × SMM *en su nivel más alto* — as DATED legal data
  (`valid_from` 2024-05-28, additive-only), with the ceiling re-resolved per
  SMM decree as of each payslip period (D-H2 resolution key: payslip period
  + worker attributes; paid slips frozen; corrections recompute with
  ORIGINAL-period rows; filed periods write-protected); the 4% is
  employer-only (R-H56). (LB-003; EV27:EVID-277; R-H56)
- **HN-PAYR-FR-185:** The system shall credit every fondo aporte to the
  named worker's RAP *cuenta individual*, modeling the fondo accumulator
  with segments — Ley-Marco-era carry-over balances (pre-vigencia, RAP
  continues administering them) and post-28-may-2024 4% accruals — never
  netting one against the other. (LB-003; LB-007; EV27:EVID-277/281)
- **HN-PAYR-FR-186:** The system shall compute the worker RAP retention —
  1.5% of *salario mensual ordinario* — as a payslip deduction line
  (IHSS-worker-share kin) whose base is ONLY the amount EXCEEDING the IHSS
  IVM contribution ceiling (*techo IVM*), the ceiling rows consumed by range
  from file 03 IHSS cotizaciones (HN-PAYR-FR-101..135) with no
  re-derivation; at or below the techo the retention is zero (excess-only
  base, never a cliff). (LB-011; EV27:EVID-285)
- **HN-PAYR-FR-187:** The system shall accrue the employer RAP *aportación*
  of 1.5% entered together with the FR-186 retention to total 3% registered
  as *ahorro* (savings) in the worker's individual cuenta (FOVIIF
  destination per FR-183); modeling default per 27_ OQ-3: the patronal 1.5%
  rides the SAME IVM-excess base as the worker retention — carried as an
  explicit config flag, never a silent assumption.
  (LB-011; LB-012; EV27:EVID-285/286)
- **HN-PAYR-FR-188:** The system shall implement the stacked-loads
  resolution (R-H56): fondo 4% (own base: salario ordinario capped at 3 × SMM
  nivel más alto) AND the RAP 1.5%/1.5% pair (IVM-excess base) accrue
  independently with ZERO offset, credit or compensation between funds —
  total employer RAP-side load = 5.5% (+ the IHSS employer share, separate
  batch) — and the THREE distinct SMM/bases never share configuration: (a)
  fondo 4%-ordinario ≤ 3×SMM-nivel-más-alto; (b) the 1.5-pair IVM-excess
  base; (c) the ISR Art. 10.h 10 × SMM *promedio* caps owned by
  taxation/04 (FR-134 within HN-TAX-FR-121..153, consumed by id).
  (LB-003; LB-011; LB-012; EV27:EVID-277/285/286; R-H56)
- **HN-PAYR-FR-189:** The system shall anchor RAP remittance to the
  instrument's own deadline: the 3% pair (retention + patronal aportación)
  paid directly to RAP or its authorized *entidades recaudadoras* within
  15 días CALENDARIO following the retention — per-instrument due-day
  semantics (calendario here; never normalized to other instruments'
  hábil/calendario rows). (LB-011; EV27:EVID-285)
- **HN-PAYR-FR-190:** The system shall implement the RAP-loan retention
  family as a distinct deduction line: employer must withhold RAP credit
  repayments (*créditos otorgados a los afiliados*) from salary and remit
  them on the same date as the monthly RAP retention (FR-189).
  (LB-011; EV27:EVID-285)
- **HN-PAYR-FR-191:** The system shall treat the cotización percentages
  (worker 1.5% / employer 1.5%) as watch-listed dated rows: the RAP Consejo
  Directivo with the productive sector's favorable vote may modify them —
  any change arrives as a NEW dated row (additive-only, D-H2), never an
  in-place replacement, and pending instruments are configuration gaps,
  never guessed values. (LB-011; EV27:EVID-285)
- **HN-PAYR-FR-192:** The system shall carry enforcement metadata only:
  non-affiliation / non-remission exposes the employer to the RAP
  *sancionatorio* (unspecified in corpus — placeholder exposure flag, never
  a rate or multa amount; interacts with the FR-208 waiver), and RAP
  accounting certifications of employer debt carry *título ejecutivo*
  (enforceable-instrument) character — informational flags, no computation.
  (LB-008; LB-011; EV27:EVID-282/285)

### 3.3 Base and scope caveats as configuration flags (never guessed)

- **HN-PAYR-FR-193:** The system shall carry the *salario ordinario*
  config-gap flag: the law defines neither the term nor any exclusion list
  (13th/14th month, vacaciones, BSP never mentioned) — synthesis hypothesis
  = the CT ordinary-salary concept with 13th/14th excluded as
  non-ordinario, FLAGGED ONLY (27_ OQ-1); the system shall never encode an
  inclusion/exclusion list into configuration until pinned by CT-batch or
  RAP-reglamentación acquisition. (LB-003; EV27:EVID-277; EV27:27_ OQ-1)
- **HN-PAYR-FR-194:** The system shall implement the techo level-set as a
  DECIDE configuration: 3 × SMM "en su nivel más alto" with the instrument
  unnamed — plain reading (3 × the highest level of the current national SMM
  table) as default vs 3 × the highest level applicable to the employer's
  sector (27_ OQ-2); ceiling rows are dated per SMM decree regardless of the
  DECIDE outcome, consume file 01 SMM rows by range, and shall NEVER use the
  SMM *promedio* nor share the ISR 10.h promedio config (R-H56(c)).
  (LB-003; EV27:EVID-277; EV27:27_ OQ-2; R-H56)
- **HN-PAYR-FR-195:** The system shall carry the reformed-Ley-RAP-Art. 43
  scope flags: (a) universality — Art. 42 reads "Todo patrono" (universal)
  but the full D.L. 107-2013 is unacquired and may condition the obligation
  to *patronos aportantes*; (b) the IVM-excess base scope for the PATRONAL
  1.5% (literal text binds "la retención" — worker-side; FR-187 default
  carries the flag); (c) pre-28-may-2024 percentage values unknown
  (pre-reform text unavailable) — the 1.5/1.5 rows are pinned from
  2024-05-28 only. All three as flags with modeling defaults, never guessed
  values. (LB-010; LB-011; EV27:EVID-284/285; EV27:27_ OQ-3)

### 3.4 Termination settlement engine: the coexists-with-offset matrix

- **HN-PAYR-FR-196:** The system shall implement the termination settlement
  ENGINE (matrix application + fondo-saldo mechanics) while CONSUMING the CT
  *auxilio de cesantía* (severance) and preaviso formulas by range from file
  08 `08_cesantia-preaviso.md` (HN-PAYR-FR-291..325) — this file never
  restates or re-derives the CT scales; the engine's inputs are (i) the
  termination cause family, (ii) the file-08 cesantía amount, and (iii) the
  certified RAP fondo saldo + *rendimientos* (yields). (LB-005;
  EV27:EVID-279)
- **HN-PAYR-FR-197:** On *despido injustificado* the system shall apply the
  coexists-with-offset rule (R-H55): compute the CT cesantía per file 08,
  deduct the fondo saldo (principal + rendimientos) from the worker's
  cesantía entitlement (employer cash-out = cesantía − saldo, floored at
  zero), and when the saldo EXCEEDS the cesantía, additionally pay the
  difference to the worker as *Compensación Laboral a la Estabilidad en el
  Empleo o Prima de Antigüedad* — worker total = max(cesantía, saldo).
  (LB-005; EV27:EVID-279; R-H55)
- **HN-PAYR-FR-198:** On ANY termination cause other than despido
  injustificado, the system shall pay out 100% of the fondo saldo +
  rendimientos to the worker as *Prima por Antigüedad* / Compensación
  Laboral a la Estabilidad (no cesantía offset), with employer complements
  only where FR-199/FR-200 apply. (LB-005; EV27:EVID-279)
- **HN-PAYR-FR-199:** On voluntary quit with antiquity GREATER than 15 years
  of continuous service, the system shall apply the 35% complement floor:
  if the RAP saldo < 35% of the *importe* that would correspond as cesantía
  indemnización (file-08 formula), the employer complements the payment up
  to the 35% floor. (LB-005; EV27:EVID-279)
- **HN-PAYR-FR-200:** On death or total non-occupational invalidity of a
  worker with ≥ 6 months of service, the system shall apply the 75%
  complement floor (the law's own cross-reference: CT Art. 120 literal f;
  grandfathering anchor D. 150-2008 Art. 2 at CT-Art. 120-A fn.19, R-H58):
  100% of the saldo to the legal beneficiaries or the worker, employer
  complementing up to 75% of the cesantía importe when the saldo is lower;
  death-case delivery to RAP-designated beneficiaries, or absent designation
  by registered *sentencia de declaratoria de heredero testamentario o Ab
  Intestato*. (LB-005; EV27:EVID-279; R-H58)
- **HN-PAYR-FR-201:** The system shall compute and pay CT *preaviso*
  (notice pay) fully independently of the fondo: the law offsets the fondo
  only against cesantía and never mentions preaviso — no fondo amount shall
  reduce, fund or condition any preaviso line (verification note against
  file 08 carried as OQ-005). (LB-005; EV27:EVID-279; EV27:27_ OQ-5)
- **HN-PAYR-FR-202:** The system shall take the fondo saldo + rendimientos
  as an EXTERNAL certified input on the final settlement (RAP must pay out
  within 1 month of termination): the settlement records the RAP
  certification (amount, date) — or, where FR-215 aggregates are tracked
  Odoo-side, reconciles them against the certification — and the RAP ≤1-month
  payout SLA as a compliance event, never as an internal payment obligation
  of the employer subsystem. (LB-005; EV27:EVID-279)
- **HN-PAYR-FR-203:** The system shall implement the employer-level regime
  selector effective 2024-05-28 (R-H58 grandfathering): employers who at
  vigencia already pay the annual auxilio de cesantía / prima de antigüedad
  under individual agreements, collective agreements or special laws are
  EXEMPT from constituting the RAP fondo — deducting the fondo-equivalent
  from the agreed payment or as otherwise agreed between the parties —
  encoded as `rap_regime ∈ {rap_fondo, grandfathered_annual_pact}`; all
  other employers take the FR-184 obligation with the FR-197..201 matrix.
  (LB-004; EV27:EVID-278; R-H58)
- **HN-PAYR-FR-204:** The system shall reject any pact or agreement recorded
  against a worker/employer pair that changes, substitutes or modifies the
  characteristics of the individual Reserva Laboral cuenta (Art. 5 first
  clause — validation block on cuenta-attribute overrides).
  (LB-004; EV27:EVID-278)
- **HN-PAYR-FR-205:** The system shall mark all RAP aportes, worker
  cotizaciones and prestaciones of this file as *inembargables* (unattachable
  and exempt from other contractual transactions not fixed in the Law) in
  every garnishment/embargo computation, with the single exception of
  *pensión alimenticia* (alimony) capped at 50% of the attachable amount.
  (LB-008; EV27:EVID-282)

### 3.5 ISR interface (consumed by id)

- **HN-PAYR-FR-206:** The system shall expose the Art. 14 ISR exclusions for
  consumption BY ID by taxation/04 (HN-TAX-FR-121..153): (a) employer aportes
  to the fondo cuentas do NOT form part of *renta neta gravable* (taxable net
  income); (b) prestaciones paid out under this Law (including
  rendimientos) do NOT form part of *renta bruta* (gross income) — fondo
  payouts at termination are ISR-free; and (c) the worker RAP 1.5% retention
  feeds the plantilla pension-contribution deduction leg (taxation/04
  FR-132); employer-side expense deductibility is NOT addressed by the
  statute and shall not be inferred. (LB-009; LB-011; EV27:EVID-283/285)

### 3.6 D. 40-2026: regularization window, post-window liability, FOVIIF integration

- **HN-PAYR-FR-207:** The system shall carry the exceptional regularization
  window as DATED rows: start 2026-03-28 (D. 40-2026 publication/vigencia),
  end 2026-09-28 under the same-date convention for "seis (6) meses contados
  a partir de la entrada en vigencia" — the calendar convention is unpinned
  (28_ OQ-1) and the end date is stored with its convention flag and a
  prorogation watch (any later prorrogante decree = new dated row; the end
  date is never silently shifted). (LB-013; LB-015; EV27:EVID-287/289;
  EV27:28_ OQ-1)
- **HN-PAYR-FR-208:** The system shall implement the waiver predicate:
  private employers *never previously affiliated* to RAP that affiliate
  during the FR-207 window — covering BOTH live funds (FOVIIF cotizaciones
  and Fondo de Reserva aportes) — owe aportes/cotizaciones only FROM
  AFFILIATION FORWARD, with full waiver of retroactive aportes (including
  the fondo 4% accrued since 28-may-2024), intereses, multas, recargos and
  sanciones derived from the prior non-affiliation (this waives the FR-192
  sancionatorio exposure for never-affiliates); encoded as
  affiliation_date + never-affiliated flags driving a no-retro-accrual
  marker. (LB-013; EV27:EVID-287; EV27:28_ OQ-2)
- **HN-PAYR-FR-209:** The system shall EXCLUDE from the FR-208 waiver:
  employers already affiliated to RAP and in *mora* (arrears stand), and
  employers with live payment *convenios* (which must be performed according
  to their terms) — the waiver predicate evaluates false for both and no
  retro or sanction rows are waived. (LB-013; EV27:EVID-287)
- **HN-PAYR-FR-210:** The system shall compute post-window exposure for
  employers still unaffiliated after the FR-207 window: the TOTALITY of owed
  obrero-patronal aportes retroactively — each stream from its own
  `valid_from` (fondo 4% from 2024-05-28; FOVIIF cotizaciones per the Ley
  RAP) — provisioned as retro-exposure liability rows, schedulable via RAP
  payment plans / financing mechanisms of up to 60 months (liability
  scheduling only; plan terms per RAP normativa, not rate configuration).
  (LB-014; EV27:EVID-288)
- **HN-PAYR-FR-211:** The system shall carry the Pensiones→FOVIIF integration
  as a fund-mapping row effective 2026-03-28: accumulated D.56-2015 Fondo de
  Pensiones resources integrate into FOVIIF preserving *derechos adquiridos*
  (acquired rights); post-integration conditions (benefits, retiro,
  devolución) follow the RAP-approved FOVIIF reglamentos under the vigente
  Ley RAP — carried as EXTERNAL-REFERENCE configuration, unpinned until the
  reglamentos are acquired (28_ OQ-3), never guessed; CNBS-supervision
  metadata recorded. (LB-015; LB-012; EV27:EVID-289/286; EV27:28_ OQ-3)

### 3.7 Affiliation exceptions, registration duties, ingestion depth

- **HN-PAYR-FR-212:** The system shall implement the worker-level
  eligibility exceptions: *cotizantes* to INJUPEMP, INPREMA, IPM or
  INPREUNAH are excepted from mandatory affiliation (no fondo 4% accrual, no
  RAP 1.5%/1.5% pair), as are staff of diplomatic delegations and
  international organisms accredited in Honduras WHEN their *convenio*
  implies a different coverage treatment for their personnel (conditional
  flag, not a blanket exclusion). (LB-006; EV27:EVID-280)
- **HN-PAYR-FR-213:** The system shall implement the prevision-plan
  survival rule: pre-existing private-sector and State-institution
  *planes y programas de previsión social* authorized by the STSS and
  CT-regulated continue in force UNLESS this Law's benefits are superior —
  a comparison hook whose borderline cases are flagged for human ruling,
  never auto-decided. (LB-006; EV27:EVID-280)
- **HN-PAYR-FR-214:** The system shall implement the registration duty
  compliance calendar (reformed Ley RAP Art. 42 via transcription):
  universal registration — every *patrono* inscribes itself and its workers
  in the RAP cotizantes registry — with the initial window 60 days from
  D. 47-2024 publication (2024-05-28 → ~2024-07-27; the publication
  reference sits inside a Ley-RAP reform, reading flagged by 27_ OQ-6) and
  ongoing hire/cessation notifications to RAP within 60 days of occurrence,
  fed by the same hire/termination events the payroll emits; the
  transcription ends in a printed ellipsis — completeness caveat carried
  (OQ-006). (LB-010; EV27:EVID-284; EV27:27_ OQ-6)
- **HN-PAYR-FR-215:** The system shall model the fondo saldo at D-H3
  hire-date depth: monthly aggregates per contract (no payslip-level import)
  from the accrual start, where the accrual start for pre-vigencia workers
  is the hypothesis max(hire_date, 2024-05-28) carried as a CONFIG-GAPPED
  flag (27_ OQ-4 — never assumed earlier, never guessed); FR-202 consumes
  the resulting saldo against RAP certification, and the cuenta may carry a
  Ley-Marco-era pre-2024 segment per FR-185.
  (LB-003; LB-007; EV27:EVID-277/281; EV27:27_ OQ-4)

## 4. Data Model

No CSV sidecar is allocated to this file in wave S-HN4: the dated rows are
few (three rate rows + one ceiling rule + two window rows) and are specified
in-line below; SMM feeds are imported from file 01's rows and the IVM techo
from file 03's rows (both by range, read-only). Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**Contribution configuration (dated, additive-only):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.rap.rate (new) | stream, rate_pct, base_rule, valid_from, valid_to, instrument, watch_flag | select/monetary/date/char/boolean | streams: fondo_employer (4%, base salario_ordinario, techo 3×SMM nivel más alto) · rap_worker (1.5%, base ivm_excess) · rap_employer (1.5%, base ivm_excess default, flag); all valid_from 2024-05-28; watch_flag for RAP Consejo Directivo instruments; never replaced in place (D-H2) | FR-184, FR-186..FR-188, FR-191 |
| l10n_hn.rap.ceiling (new) | multiple, smm_measure, level_set, valid_from, valid_to | monetary(computed)/select/date | multiple = 3; smm_measure = nivel_mas_alto (NEVER promedio; never shares the ISR 10.h config — R-H56(c)); level_set DECIDE: national_highest (default, plain reading) \| employer_sector (27_ OQ-2); re-resolves per SMM decree (file 01 feed) per payslip period; snapshot-on-write of the resolved techo onto payslip rows (D15) | FR-184, FR-194 |
| l10n_hn.rap.base.flag (new) | flag, hypothesis, status | select/char | salario_ordinario_undefined (CT-ordinary, 13th/14th excluded — hypothesis only) · art43_universality · patronal_base_scope · pre_reform_values_unknown (27_ OQ-3); flags never inject values into config | FR-193, FR-195 |

**Employer / worker / contract regime:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | rap_regime, rap_affiliation_date, rap_never_affiliated, rap_mora, rap_payment_convenio | select/date/boolean | rap_regime: rap_fondo \| grandfathered_annual_pact (effective 2024-05-28, Art. 5); affiliation_date drives FR-208 no-retro marker and FR-210 exposure start | FR-203, FR-207..FR-210 |
| hr.employee | rap_exception_institute, rap_diplomatic_convenio, prevision_plan | select/boolean | institutes: injupemp \| inprema \| ipm \| inpreunah \| none; prevision_plan carries the mas-favorable comparison hook | FR-212, FR-213 |
| hr.contract | rap_accrual_start | date | hypothesis max(hire_date, 2024-05-28), config-gapped (27_ OQ-4) | FR-215 |
| l10n_hn.rap.notification (new) | event, worker, occurred_on, due_on | select/m2o/date | events: initial_registration \| hire \| cessation; SLA = 60 días from occurrence (initial window from 2024-05-28 publication); compliance-calendar rows | FR-214 |

**Payslip lines and the cuenta individual:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip | rap_fondo_employer, rap_ivm_excess_base, rap_worker_retention, rap_employer_share, rap_loan_deduction, rap_techo_snapshot | monetary (computed) | 4% employer-only on min(salario_ordinario, techo); 1.5% pair on IVM-excess (techo rows consumed from file 03 by range); RAP-loan family; techo snapshot-on-write (D15) | FR-184, FR-186..FR-190 |
| l10n_hn.rap.cuenta (new) | worker, fund, segment, saldo_certified, certified_on | m2o/select/monetary/date | funds: fondo_reserva \| foviif \| pensiones_closed; segments: ley_marco_carryover \| post_2024_05_28; saldo from RAP certification (external) reconciled vs FR-215 aggregates | FR-183, FR-185, FR-202, FR-215 |
| hr.payslip (final settlement) | termination_cause_family, ct_cesantia_amount, fondo_saldo_amount, cesantia_offset, complement_floor_pct, complement_paid, estabilidad_excess, rap_payout_sla_due | select/monetary/date | cause families: despido_injustificado \| other; ct_cesantia_amount consumed from file 08 (HN-PAYR-FR-291..325) by range; floors 35.0 \| 75.0 \| none; rap_payout_sla_due = termination + 1 month | FR-196..FR-202 |
| account.move.line (garnishment view) | rap_inembargable, alimony_exception_cap_pct | boolean/monetary | alimony-only exception, cap 50% of the attachable amount | FR-205 |

**Window, liability and fund mapping:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.rap.window (new) | valid_from, valid_to, end_convention, prorogation_watch | date/select/boolean | 2026-03-28 → 2026-09-28 (same_date convention flag — 28_ OQ-1); waiver scope flags (never-affiliated private employers; both live funds) | FR-207..FR-209 |
| l10n_hn.rap.liability (new) | company, stream, exposure_from, plan_months | m2o/select/date/integer | post-window retro exposure (fondo 4% from 2024-05-28; FOVIIF per Ley RAP); plans ≤ 60 months (liability scheduling, not rate config) | FR-210 |
| l10n_hn.rap.fund.mapping (new) | from_fund, to_fund, valid_from, conditions_ref | select/date/char | pensiones_closed → foviif effective 2026-03-28; conditions_ref = RAP reglamentos EXTERNAL reference (unpinned — 28_ OQ-3) | FR-211 |

## 5. Odoo Mapping

Layer semantics for this file: `odoo` = computation/bookkeeping logic living
in the LGPL client (payroll rules, dated config models, settlement engine).
No SaaS rows are introduced: none of these FRs touch the thin-client/SaaS
architecture split (no DTE-like surface exists for RAP remittances in the
corpus; RAP recaudadora formats are unacquired leads). Model names stable
across Odoo 17/18/19/20; version-specific behavior recorded per row where a
legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-181..FR-183 | odoo | res.company / hr.employee predicates + l10n_hn.rap.cuenta | regime, fund taxonomy | D12: vigencia regime boundary 2024-05-28; D15/D16: dated rows + original-period recompute on corrections; lineage metadata (D.56-2015 → SCO-858-2015 → D.47-2024) |
| FR-184, FR-185 | odoo | hr.salary.rule (employer 4%) + l10n_hn.rap.rate / l10n_hn.rap.ceiling | dated rate + techo | Techo resolves per SMM decree per payslip period; snapshot-on-write (D15); level_set DECIDE (OQ-002); D16: paid slips frozen, filed periods write-protected |
| FR-186..FR-188 | odoo | hr.salary.rule (RAP 1.5 pair) + l10n_hn.rap.rate | IVM-excess base | IVM techo rows consumed by range from file 03 (HN-PAYR-FR-101..135); patronal-base default = same excess base (flag, OQ-003); R-H56 stacking, no cross-credit |
| FR-189, FR-190 | odoo | hr.payslip deduction lines + payment due-date engine | 15 días calendario | Per-instrument due-day semantics (calendario here); RAP loans remit same date as the monthly retention |
| FR-191, FR-192 | odoo | l10n_hn.rap.rate metadata + exposure flags | watch flags | RAP Consejo Directivo rate changes = new dated rows (additive-only); sancionatorio placeholder + título ejecutivo = informational flags, never amounts |
| FR-193..FR-195 | odoo | l10n_hn.rap.base.flag | config-gap flags | Never-guess rule (D-H2): hypotheses flagged (salario ordinario; techo level-set; Art. 43 universality/base/pre-reform) — no flag injects a value into computation |
| FR-196..FR-202 | odoo | hr.payslip final-settlement rules + l10n_hn.rap.cuenta | matrix engine | Consumes ct_cesantia_amount from `08_cesantia-preaviso.md` (HN-PAYR-FR-291..325) by range — never restated; external saldo certification input; R-H55 matrix; RAP ≤1-month SLA event |
| FR-203, FR-204 | odoo | res.company rap_regime selector + cuenta-attribute guard | regime selector | Grandfathering effective 2024-05-28 (R-H58 anchor D. 150-2008 Art. 2 at CT-Art. 120-A fn.19); pacto-prohibition validation block on cuenta overrides |
| FR-205 | odoo | garnishment engine exemption flags | inembargable | Alimony-only exception, 50% cap; applies to aportes, cotizaciones and prestaciones |
| FR-206 | odoo | ISR interface flags | exclusion outputs | Consumed BY ID by taxation/04 (FR-130/FR-132 legs within HN-TAX-FR-121..153): contribution-side + payout-side exclusions and the pension-deduction feed; no plantilla logic here |
| FR-207..FR-209 | odoo | l10n_hn.rap.window dated rows | window regime | D12: window regime 2026-03-28 → 2026-09-28 (convention flag, prorogation watch); D19 go-live note: window affiliations post NO retro accrual — GL-neutral, no historical import required |
| FR-210 | odoo | l10n_hn.rap.liability | retro exposure + plans | D19: provisioning via configurable control accounts for the retro exposure; ≤60-month plan scheduling = liability calendar, not rate config |
| FR-211 | odoo | l10n_hn.rap.fund.mapping | fund mapping | Effective 2026-03-28; conditions = RAP reglamentos external reference (unpinned, OQ-009); CNBS supervision metadata |
| FR-212..FR-214 | odoo | hr.employee exceptions + l10n_hn.rap.notification | eligibility + SLA | 60-day notification SLAs fed by hire/termination events; transcription-ellipsis caveat (OQ-006); diplomatic convenio = conditional flag |
| FR-215 | odoo | l10n_hn.rap.cuenta ingestion | monthly aggregates | D-H3 hire-date depth, monthly per contract (no payslip-level import); D18: tiered ingestion for straddle-period saldo detail at go-live; accrual-start hypothesis max(hire_date, 2024-05-28) config-gapped (OQ-004) |

Version-regime notes (D12): FR-184/FR-186..FR-188 record the D. 47-2024
regime start 2024-05-28 (rate rows and techo rule) with the RAP
Consejo-Directivo change power as watch metadata (FR-191). FR-207..FR-211
record the D. 40-2026 regime: window 2026-03-28 → 2026-09-28 (end
convention open) and the Pensiones→FOVIIF integration on 2026-03-28 —
regime cutovers modeled as dated config rows, never in-place edits (D-H2).
D15/D16 apply to every dated parameter (snapshot-on-write of resolved techo/
rates onto payslip rows; corrections recompute with ORIGINAL-period rows).
D18 applies to the FR-215 saldo ingestion (historical journals for
pre-go-live monthly aggregates); D19 applies to FR-210 provisioning accounts
at cut-over.

## 6. Acceptance Criteria

- **AC-001:** Given a payroll run for April 2024 (pre-vigencia), then no
  fondo 4% accrual row is created (obligation valid_from 2024-05-28; never
  back-accrued — FR-182); given June 2024 for the same contract, then the
  4% row accrues (FR-184).
- **AC-002:** Given the highest level of the current SMM table = L20,000.00
  (hypothetical file-01 feed; techo = 3 × 20,000 = L60,000.00), then a
  salario ordinario of L50,000.00 yields fondo 4% = L2,000.00, and a salario
  ordinario of L90,000.00 yields 4% × capped base 60,000 = L2,400.00
  (FR-184).
- **AC-003:** Given the 2026 SMM promedio feed L14,917.20 (10× cap
  L149,172.00 owned by taxation/04 FR-134), then the fondo techo
  configuration references neither the promedio row nor the IVM techo —
  three separate config ids (R-H56(c)) — and the 1.5-pair base references
  only the IVM techo row from file 03 (FR-188, FR-194).
- **AC-004:** Given salario mensual ordinario L12,000.00 and an IVM techo of
  L9,000.00 for the period (hypothetical file-03 row), then the worker RAP
  retention = 1.5% × 3,000 = L45.00, the employer aportación = L45.00
  (default same base, flag shown), 3% ahorro = L90.00 credited to the FOVIIF
  cuenta, and the fondo 4% computed separately on min(12,000, techo_fondo)
  (FR-186..FR-188).
- **AC-005:** Given salario mensual ordinario L8,000.00 below the IVM techo
  L9,000.00, then the worker retention = L0.00 (excess-only base) and the
  employer 1.5% = L0.00 under the default base reading with the OQ-003 flag
  visible on the run (FR-186, FR-187).
- **AC-006:** Given a RAP retention practiced 31-Jan-2026 (with RAP-loan
  withholdings of the same month), then the entero deadline for the 3% pair
  and the loan withholdings = 2026-02-15 (15 días calendario following the
  retention) (FR-189, FR-190).
- **AC-007:** Given despido injustificado with file-08 CT cesantía =
  L100,000.00 and certified RAP saldo + rendimientos = L62,000.00, then the
  employer pays 100,000 − 62,000 = L38,000.00, RAP pays L62,000.00, worker
  total = L100,000.00 (FR-197).
- **AC-008:** Given despido injustificado with cesantía L100,000.00 and
  saldo L120,000.00, then the employer cesantía cash-out = L0.00 and the
  worker receives L120,000.00 total (L20,000.00 as Compensación Laboral a la
  Estabilidad en el Empleo) (FR-197).
- **AC-009:** Given a voluntary quit after 16 years continuous service with
  cesantía-equivalent indemnización L100,000.00 and saldo L20,000.00, then
  the 35% floor = L35,000.00 and the employer complement = L15,000.00
  (worker total L35,000.00); given saldo L40,000.00 ≥ the floor, then no
  complement (FR-199).
- **AC-010:** Given death of a worker with 8 months service, cesantía
  importe L100,000.00 and saldo L30,000.00, then the 75% floor = L75,000.00
  and the employer complement to the beneficiaries = L45,000.00; delivery
  follows the RAP designation or a registered heredero sentence (FR-200).
- **AC-011:** Given the AC-007 settlement, then the preaviso line computes
  independently per file 08 and no fondo amount reduces or conditions it
  (FR-201).
- **AC-012:** Given an employer with a collective pact paying annual prima
  de antigüedad since 2023, then rap_regime = grandfathered_annual_pact
  from 2024-05-28 and no fondo 4% accrual rows post-vigencia; the
  fondo-equivalent deduction follows the agreed terms (FR-203).
- **AC-013:** Given a generic garnishment order against a worker's RAP
  entries, then it is blocked (inembargable); given an alimony order, then
  attachment is capped at 50% of the attachable prestación/cotización
  (FR-205).
- **AC-014:** Given a termination fondo payout of L62,000.00, then it is
  excluded from renta bruta (no ISR line); the employer 4% aporte never
  enters the worker's renta neta gravable; and the worker 1.5% retention of
  L45.00 flows to the plantilla pension-deduction leg of taxation/04 FR-132
  by id (FR-206).
- **AC-015:** Given a never-affiliated private employer affiliating
  15-Jul-2026 (inside the window), then aportes accrue from 2026-07-15 with
  NO retro rows for 2024-05-28 → 2026-07-14 and no interés/multa/recargo/
  sanción rows; given an already-affiliated employer in mora, then the
  waiver evaluates false and mora balances stand (FR-207..FR-209).
- **AC-016:** Given an employer still unaffiliated on 2026-10-01
  (post-window), then retro-exposure rows provision the fondo 4% from
  2024-05-28 and FOVIIF cotizaciones per the Ley RAP, schedulable in ≤ 60
  monthly installments (FR-210).
- **AC-017:** Given a worker who is an INJUPEMP cotizante, then no fondo 4%
  accrual and no RAP 1.5%/1.5% rows are produced for the contract
  (FR-212).
- **AC-018:** Given a worker hired 2019-03-01 (pre-vigencia), then saldo
  aggregates start at max(2019-03-01, 2024-05-28) = 2024-05-28 with the
  accrual-start hypothesis flag visible — an earlier start is never assumed
  and the start rule is never guessed into config (FR-215).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `salario_ordinario` undefined in D. 47-2024 Art. 4 (EV27:27_ OQ-1): no inclusion/exclusion list (13th/14th, vacaciones, BSP unaddressed). FR-193 flags the CT-ordinary hypothesis (13th/14th excluded) — FLAG ONLY; pin against the CT salary batch / RAP reglamentación before freezing the 4% base composition. V-HN1 lean (flag stays): D. 117-2021 Art. 2 (`89_`, EVID-335) — 13th month exempt from cotizaciones/deducciones — supports the excluded leg for the 13th month specifically (payroll/02 OQ-007 kin). | no | Takumi S-HN4 + controller | open |
| OQ-002 | Fondo techo level-set (EV27:27_ OQ-2): "tres (3) salarios mínimos en su nivel más alto" names no instrument — plain reading 3 × national-highest vs 3 × employer-sector-highest = DECIDE config (FR-194, default national-highest); rows dated per SMM decree regardless; NEVER promedio, never the ISR 10.h config. Confirm vs SMM decree batch and RAP practice. | no | Takumi S-HN4 + controller | open |
| OQ-003 | Reformed Ley RAP Art. 43 scope (EV27:27_ OQ-3): (i) universality ("Todo patrono" per Art. 42 vs possible patrono-aportante conditioning); (ii) whether the IVM-excess base governs the patronal 1.5% (FR-187 default: yes, flagged); (iii) pre-28-may-2024 percentage values unknown. TOP ACQUISITION LEAD: Ley RAP D.L. 107-2013 full/consolidated text — UNACQUIRED and doubly load-bearing (Arts. 42/43/61 known only via 47_'s ellipsis-truncated transcription; FOVIIF's own creation/conditions live there). | no | acquisition queue | open |
| OQ-004 | Fondo accrual start for pre-vigencia workers (EV27:27_ OQ-4): law fixes no start and creates no retro duty (Arts. 9-10); D-H3 hire-date depth needs the rule — hypothesis max(hire_date, 2024-05-28) config-gapped (FR-215); check RAP reglamentación (47-Art. 13 lead) or CNBS/RAP practice. | no | Takumi S-HN4 + controller | open |
| OQ-005 | Preaviso interplay (EV27:27_ OQ-5): the law offsets the fondo only against cesantía and never mentions preaviso — FR-201 encodes untouched/independent; verify against file 08 `08_cesantia-preaviso.md` (HN-PAYR-FR-291..325) termination articles before freezing final-pay formulas. | no | Takumi S-HN4 (file 05) + file 08 | open |
| OQ-006 | Art. 16 transcription integrity + 60-day reference (EV27:27_ OQ-6): the gazette transcription of reformed Art. 42 ends in a printed ellipsis ("Asimismo…") — clauses may be missing; "la publicación de la presente Ley" inside the 60-day registration duty reads as D. 47-2024's publication (→ ~27-jul-2024) but sits inside a Ley-RAP reform. Verify both against the consolidated Ley RAP (same lead as OQ-003). | no | acquisition queue | open |
| OQ-007 | Window end-date convention + prorogation (EV27:28_ OQ-1): "seis (6) meses contados a partir de la entrada en vigencia" from 2026-03-28 → 2026-09-28 same-date convention (end-of-month would give 30-sep-2026); convention unpinned — FR-207 stores the convention flag; watch for prorogation decrees before freezing. | no | Takumi S-HN4 + controller | open |
| OQ-008 | Waiver scope (EV27:28_ OQ-2): (i) worker-side effect — nothing compensates affected workers' unfunded fondo cuentas for the waived period (2024-05-28 → affiliation); (ii) "empresas privadas" breadth — considerando motivates with MiPyMEs but operative Art. 1 covers all unaffiliated private employers (operative text favored; non-corporate individual employers treated as covered unless RAP practice says otherwise). | no | Takumi S-HN4 + controller | open |
| OQ-009 | FOVIIF integration mechanics (EV27:28_ OQ-3): D40-Art. 3 delegates balance mapping, benefit/retiro/devolución conditions to RAP-approved reglamentos under the vigente Ley RAP — neither in corpus; FR-211 carries an external-reference config (unpinned, never guessed). Acquisition leads: RAP reglamentos + sancionatorio (47-Arts. 12-13); current SMM decree (techo rows, OQ-002); any RAP Consejo Directivo rate instrument; post-window D. 40-2026 prorogations. | no | acquisition queue | open |
