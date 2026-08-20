# GT — Taxation — ISR rentas del trabajo (employment income & employer withholding)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala *Impuesto
sobre la Renta* (ISR, income tax) on **rentas del trabajo en relación de
dependencia** (employment income under an employment relationship): the
*hecho generador* (taxable event) — all cash remuneration from dependent
personal work of resident individuals (Art. 68); the perception rule
(Art. 69) and taxpayer class (Art. 71); the Art. 70 exemptions (*aguinaldo*
and *bono 14* each exempt up to 100% of one ordinary monthly salary,
*indemnización por tiempo servido* fully exempt, pensions removed by D-14-2013);
the Art. 72 deductions as dated rows (Q48,000 personal without vouchers +
Q12,000 IVA credit via the January *planilla* within the first 10 días
hábiles + worker IGSS/IPM/previsión shares + 5% donations + no-surrender
life insurance); the Art. 73 ANNUAL two-bracket scale (5% ≤ Q300,000;
Q15,000 + 7% over) as the single scale for monthly withholding AND definitive
liquidation over the Art. 74 calendar-year period; the Arts. 75–82 employer
withholding algorithm (annual projection minus Q48,000-only minus estimated
IGSS/IPM → scale → ÷12, mid-year remaining-months projection, no-pro-rata
full Q48,000 for partial-year workers, multi-employer highest-*patrono*
rule, *constancias*, 10-day payment even if retention was omitted, refund
within the first 2 months, worker DJ within the first 3 months, Art. 82
delegation to the reglamento); the 28_ (AG 213-2013 Arts. 67–73) operational
detail (planilla field schema, January reconciliation, refunds in *cuotas*);
and the 47_-sourced practice layer (SAT-1901, SAT-1331, RETENISR2, Planilla
IVA-FEL, BancaSAT) under the R46 form-identity guard.

It does **not** cover: ISR on actividades lucrativas, rentas de capital,
no-residentes or facturas especiales (Task 5 file — which cross-references
this file's Art. 73 scale by FR id); the IVA retention matrix (Task 3 file,
`03_iva-retenciones.md`); the wage-side IVA-retention rows of facturas
especiales (Task 5); sanction amounts (Task 6 — CT 94.7/94.9/94.18/94"A",
CP 358"C"); the bonus laws themselves (aguinaldo D-76-78, bono 14 D-42-92,
incentivo — P-wave payroll files, cross-referenced); IGSS rate/base values
(GOQ-04, external); declaration form generation (F-wave); or FEL DTE
mechanics (`gt/requirements/e-invoicing/`).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): **ISR =
26_ LAT D-10-2012 consolidated through Dto. 46-2022 (27-09-2022) governs;
28_ AG 213-2013 develops; 47_ = self-disclaimed SAT digest — 26_ > 28_ >
47_, law wins every delta.** The 47_ digest ("Este material solo puede ser
utilizado con fines ilustrativos…") is used ONLY for practice-layer signals
(EVID-245) with every number cross-checked (EVID-243: ALL match — no
post-2022 reform signal on the asalariados side up to the digest's date;
residual post-46-2022 window = GOQ-58 caveat on every Art. 72/73 value).
Form identities cite 48_/RetWeb (R46), never the digest. Dated values
follow the dated-instrument regime D15/D16 (cite together):
valid_from/valid_to rows + instrument provenance; rate/cap rows are
decree-bound, never constants.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Actualización Tributaria, Decreto Número 10-2012 (texto consolidado, última reforma impresa: Dto. 46-2022 del 27-09-2022), Libro I Título II "Rentas del Trabajo" arts. 68-82 + art. 82: "El reglamento indicará los procedimientos para efectuar, cobrar y pagar las retenciones." | LAT D-10-2012 as consolidated through D-46-2022: the governing ISR instrument for employment income (Arts. 68–82); Art. 82 expressly delegates retention procedures to the reglamento (developed by 28_ arts. 67–73). Residual post-27-09-2022 window unverified (GOQ-58) | `gt/sources/26_LAT_10-2012.pdf` | Libro I arts. 68-82, pp. 33-36 (EVID-216, EVID-229) |
| LB-002 | D-10-2012, Art. 68: "Constituye hecho generador del Impuesto Sobre la Renta regulado en este título, la obtención de toda retribución o ingreso en dinero, cualquiera que sea su denominación o naturaleza, que provenga del trabajo personal prestado en relación de dependencia, por personas individuales residentes en el país." Num. 1 (reformado por Dto. 19-2013): "Los sueldos, bonificaciones, comisiones, aguinaldos, viáticos no sujetos a liquidación o que no constituyan reintegro de gastos, y otras remuneraciones…" / Art. 69: "Las rentas gravadas en el presente título se imputan al período de liquidación en que sean percibidas o puestas a disposición del trabajador." / Art. 71: "Son contribuyentes… las personas individuales, residentes en el país, que obtengan ingresos en dinero por la prestación de servicios personales en relación de dependencia." | Art. 68 taxable event: ANY cash remuneration from dependent work of resident individuals; num. 1 list (sueldos, bonificaciones, comisiones, aguinaldos, non-liquidation viáticos + catch-all), num. 2 crews of Guatemala-based/matriculated vessels, num. 3 board/council remunerations when in relación de dependencia; Art. 69 perception imputation (perceived or placed at disposal); Art. 71 taxpayers = resident individuals | `gt/sources/26_LAT_10-2012.pdf` | p.33 arts. 68-69, p.34 art. 71 (EVID-226) |
| LB-003 | D-10-2012, Art. 70: "Están exentas del impuesto: 1. Las indemnizaciones o pensiones percibidas por causa de muerte o por incapacidad… No están exentas las remuneraciones que se perciban del patrono, durante el tiempo de vigencia de las licencias laborales con goce de sueldo. 2. El pago de la indemnización por tiempo servido… 3. Las remuneraciones que los diplomáticos… reciban… en condición de reciprocidad. 4. Los gastos de representación y viáticos comprobables… 5. El aguinaldo hasta el cien por ciento (100%) del sueldo o salario ordinario mensual. 6. La bonificación anual para trabajadores del sector privado y público… hasta el cien por ciento (100%) del sueldo o salario ordinario mensual. *7. Las pensiones, jubilaciones o montepíos… (*Adicionado… por el Decreto Número 14-2013 el 03-12-2013)" | Art. 70 exemptions: death/incapacity indemnities-pensions (but salaries during paid leave ARE taxable); indemnización por tiempo servido fully exempt; diplomats on reciprocity; documented representation expenses/viáticos (in-country: invoices; abroad: entry/exit + activity + tickets proof); aguinaldo exempt ≤ 100% of one ordinary monthly salary; bono 14 (bonificación anual) exempt ≤ 100% of one ordinary monthly salary; pensions/jubilaciones/montepíos removed from the gravamen by numeral 7 (added by D-14-2013, 03-12-2013) | `gt/sources/26_LAT_10-2012.pdf` | pp. 33-34 art. 70 (EVID-226) |
| LB-004 | D-10-2012, Art. 72: renta bruta = "la suma de sus ingresos gravados y exentos"; renta neta = "la diferencia entre la renta bruta y las rentas exentas". "a. Hasta sesenta mil Quetzales (Q.60,000.00), de los cuales cuarenta y ocho mil Quetzales (Q.48,000.00) corresponden a gastos personales sin necesidad de comprobación alguna; y, doce mil Quetzales (Q.12,000.00) que podrá acreditar por el Impuesto al Valor Agregado pagado en gastos personales… La planilla deberá presentarse ante la Administración Tributaria, dentro de los primeros diez (10) días hábiles del mes de enero de cada año, debiendo el patrono conciliar entre las retenciones efectuadas y la liquidación o declaración definitiva que deberá presentar el trabajador." / "b. Las donaciones… no puede exceder del cinco por ciento (5%) de la renta bruta." / "c. Las cuotas por contribuciones al Instituto Guatemalteco de Seguridad Social, al Instituto de Previsión Militar y al Estado y sus instituciones por cuotas de regímenes de previsión social." / "d. Las primas de seguros de vida para cubrir riesgos en casos de muerte exclusivamente… siempre que el contrato de seguro no devengue suma alguna por concepto de retorno, reintegro o rescate." | Art. 72 deductions: Q60,000 aggregate = Q48,000 personal (no vouchers) + Q12,000 IVA credit on personal purchases evidenced by the planilla filed within the first 10 días hábiles of January (employer reconciles retentions vs the worker's definitive liquidation); donations to the listed entities ≤ 5% of renta bruta (with fiscal solvencia); worker-share IGSS/IPM/state-previsión contributions; death-risk-only life-insurance premiums with no surrender value | `gt/sources/26_LAT_10-2012.pdf` | pp. 34-35 art. 72 (EVID-227) |
| LB-005 | D-10-2012, Art. 73 (bajo el acápite "CAPÍTULO IV BASE IMPONIBLE Y TIPO IMPOSITIVO"): "Los tipos impositivos aplicables a la renta imponible… son del cinco y siete por ciento (5% y 7%), según el rango de renta imponible, y se aplican de acuerdo con la siguiente escala: / Rango de renta imponible | Importe fijo | Tipo impositivo de / Q.0.01 a Q 300,000.00 | Q.0.00 | 5% sobre la renta imponible. / Q.300,000.01 en adelante | Q.15,000.00 | 7% sobre el excedente de Q.300,000.00. / El impuesto a pagar se determina, para el primer rango, aplicando el tipo impositivo de cinco por ciento (5%)… Para el segundo rango, se determina sumando al importe fijo, la cantidad que resulte de aplicar el tipo impositivo del siete por ciento (7%) al excedente de renta imponible…" / Art. 74: "El período de liquidación del impuesto es anual, principia el uno (1) de enero y termina el treinta y uno (31) de diciembre de cada año." | Art. 73 THE annual employment-income scale, verbatim: two brackets — 5% on taxable income from Q0.01 to Q300,000.00 (fixed amount Q0.00); Q15,000.00 + 7% on the excess over Q300,000.00; Art. 74: annual liquidation period = calendar year (1 January – 31 December) | `gt/sources/26_LAT_10-2012.pdf` | p.35 arts. 73-74 (EVID-228) |
| LB-006 | D-10-2012, Arts. 75-76: Art. 75: "Todo patrono que pague o acredite a personas residentes en Guatemala remuneraciones de cualquier naturaleza por servicios provenientes del trabajo personal ejecutado en relación de dependencia, sean permanentes o eventuales, debe retener el Impuesto Sobre la Renta del trabajador…" (no retención on diplomats; resident employees of missions still file annual DJ; missions file the annual list of workers and salaries) / Art. 76: "Al principio de cada año o al inicio de la relación laboral, el patrono o pagador hará una proyección de la renta neta anual del trabajador, a la cual le deducirá el monto de cuarenta y ocho mil quetzales por concepto de gastos personales y el monto de las cuotas anuales estimadas por concepto de pagos al Instituto Guatemalteco de Seguridad Social, Instituto de Previsión Militar y al Estado… Al valor obtenido, le aplicará el tipo impositivo correspondiente, de acuerdo a lo establecido en el artículo 73… y cada mes, el patrono o pagador retendrá al trabajador, la doceava parte del monto proyectado." (prior-patrono constancias summed; mid-year start "por el número de meses que hagan falta"; recalc "sin necesidad de declaración del trabajador") | Arts. 75–76: every employer paying/crediting dependent-work remuneration must withhold; projection algorithm — project the annual net rent at year start or hire date, deduct Q48,000 (only) + estimated annual IGSS/IPM/state-previsión contributions, apply the Art. 73 scale, withhold 1/12 monthly; prior-employer constancias added to the projection; mid-year start projects only remaining months; recalculation on change without a worker declaration | `gt/sources/26_LAT_10-2012.pdf` | pp. 35-36 arts. 75-76 (EVID-229) |
| LB-007 | D-10-2012, Arts. 77-79: Art. 77: multi-patrono — worker "debe informar dicho extremo al patrono que le pague o acredite la mayor remuneración anual" + declaración jurada of each employer's retributions + copy to the other patronos / Art. 78: "Los agentes de retención proporcionarán a los trabajadores… dentro de los diez (10) días inmediatos siguientes de efectuado el pago de la renta, las constancias que indiquen el nombre, Número de Identificación Tributaria del patrono y del trabajador, la renta acreditada o pagada y el monto retenido." / Art. 79: year-end donation constancias → patrono "determinará el impuesto definitivo"; excess refunds + informe a la SAT "dentro de los primeros dos (2) meses del año calendario"; early contract end → definitive determination + refund/charge at exit | Arts. 77–79: multi-employer aggregation (highest-paying employer is the retention agent, informed via DJ with copies to the others); retention constancia within the 10 days immediately following payment (name, employer/worker NIT, rent, amount withheld); year-end definitive determination by the employer with donation evidence; refunds reported within the first 2 months of the calendar year; exit-time definitive settlement | `gt/sources/26_LAT_10-2012.pdf` | p.36 arts. 77-79 (EVID-229) |
| LB-008 | D-10-2012, Arts. 80-81: Art. 80: DJ de retenciones + pago con anexo (nombre completo y NIT de cada retenido, concepto, renta, monto) "dentro de los primeros diez (10) días del mes siguiente al que corresponda el pago de las remuneraciones, aunque se hubiese omitido realizar la retención." / Art. 81: worker's own annual DJ + pago "únicamente" cuando (1) no retención o (2) retención menor a la correspondiente — "dentro del plazo de los tres (3) primeros meses del año siguiente al período que se liquida." | Art. 80: employer's monthly retention DJ + payment with per-worker annex within the first 10 días (plain, as printed) of the following month — even if the retention was omitted; Art. 81: the worker files an annual DJ only when retention was absent or short, within the first 3 months of the following year | `gt/sources/26_LAT_10-2012.pdf` | p.36 arts. 80-81 (EVID-229) |
| LB-009 | Reglamento del Libro I de la LAT, AG 213-2013, Arts. 67-69: art. 67 (pensiones/jubilaciones corroboration) / art. 68 (planilla fields): "Fecha de emisión y número correlativo de la factura"; "Valor total de cada compra por factura, que ya incluye el Impuesto al Valor Agregado (IVA)"; "las emitidas por un mismo proveedor no podrán ser consolidadas en un solo renglón."; IVA de vehículos (IVA art. 55) e importaciones includible; "no pueden ser utilizados por el contribuyente en otra categoría de renta"; "No podrá deducirse… el impuesto… de gastos que no sean razonables conforme a la capacidad de consumo"; planilla extemporánea → "Dicho crédito será improcedente" / art. 69: "Al ingreso total así determinado, descontarán únicamente la suma de cuarenta y ocho mil quetzales exactos (Q 48,000.00), en concepto de gastos personales deducibles… así como el valor de las cuotas o contribuciones anuales estimadas correspondientes al IGSS, al IPM y al Estado…"; recalcs "en cuotas mensuales hasta la conclusión del periodo anual"; multi-patrono agent = "el patrono que le pague la mayor cantidad de rentas afectas"; "No podrá limitarse la deducción por gastos personales aun en los casos en que la relación laboral no haya durado el período anual completo. Tampoco podrá realizarse estimación de ingresos proyectados a doce meses por igual causa." | Reglamento arts. 67–69: planilla field schema (invoice date + correlativo, IVA-inclusive per-invoice totals, per-supplier rows never consolidated, vehicle/import IVA includible, no cross-category use, reasonable-consumption cap, late planilla kills the Q12,000 credit); projection subtracts ONLY Q48,000 + estimated IGSS/IPM/state shares; recalculation adjustments spread in monthly installments; highest-paying employer rule; partial-year workers keep the FULL Q48,000 with no 12-month annualization | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | pp. 30-32 arts. 67-69 (EVID-239) |
| LB-010 | AG 213-2013, Arts. 70-73: art. 70: monthly constancia may be embedded "en la boleta de pago" del asalariado; "constancia final del impuesto retenido durante todo el período, dentro de los diez (10) días hábiles, contados a partir de la fecha en que se efectúe el último pago correspondiente del período de liquidación definitiva anual" (also at early contract end, per art. 79 ¶2 Ley) / art. 71: January informe/reconciliación incl. "la deducción que hasta por doce mil quetzales (Q 12,000.00) podrá considerarse a su favor, con base en la planilla" / art. 72: refunds "en una o varias cuotas" / art. 73: worker's own DJ when retention missing/short; patron sanction per Código Tributario — "Esta sanción no será aplicable en los casos establecidos en el segundo párrafo del artículo 75 de la Ley" (diplomáticos) | Reglamento arts. 70–73: constancia-in-boleta option; final constancia within 10 días hábiles of the last payment (and at exit); January annual reconciliation report including the up-to-Q12,000 planilla credit; refunds payable in one or several installments; worker DJ duty with the CT-sanction note and the diplomatic carve-out | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | pp. 32-33 arts. 70-73 (EVID-239) |
| LB-011 | D-10-2012, Art. 21 nums. 5/6/8 (employer-side caps): "Tanto el aguinaldo como la bonificación anual… (bono 14), serán deducibles hasta el cien por ciento (100%) del salario mensual, salvo lo establecido en los pactos colectivos…"; cuotas patronales IGSS/IRTRA/INTECAP deductibles; indemnizaciones "hasta el límite del ocho punto treinta y tres por ciento (8.33%) del total de las remuneraciones anuales" / Art. 23: c) "Los que el titular de la deducción no haya cumplido con la obligación de efectuar la retención y pagar el Impuesto Sobre la Renta, cuando corresponda. Serán deducibles una vez se haya enterado la retención."; f) sueldos sin planilla IGSS | Employer-side pairing: aguinaldo/bono 14 each deductible up to 100% of one monthly salary (unless collective agreement), IGSS/IRTRA/INTECAP employer quotas fully, indemnización capped at 8.33% of annual remunerations; and the retention↔deduction dependency — expenses are non-deductible until the omitted ISR retention is entered (23.c) and salaries off the IGSS planilla are non-deductible (23.f). Full art. 21/23 matrices owned by Task 5 — cross-referenced | `gt/sources/26_LAT_10-2012.pdf` | pp. 10-17 arts. 21, 23 (EVID-219, EVID-220) |
| LB-012 | Catálogo SAT Formularios Vigentes (48_, Wayback 2025-10-06): "ISR Retenciones | – | – | – | 1331" / "ISR Relación de Dependencia. Impuesto Sobre la Renta. Rentas del Trabajo en Relación de Dependencia, Declaración Jurada y Pago Anual. | – | – | – | 1431" / (RETENISR anexo:) "RETENISR | Declaración Jurada ante el Patrono del ISR. | 1901"; "RETENISR | Informe Anual de Liquidación y Devolución de lo Retenido en Exceso | 1481"; "RETENISR | Constancia de Retención del ISR del Trabajo. | 1921" / (PLANILLA IVA-FEL:) "PLANILLA IVA-FEL | Planilla para el Crédito por Impuesto al Valor Agregado | 1111" | Form identities (R46, binding): monthly ISR retenciones declaration = **SAT-1331**; asalariados annual DJ (relación de dependencia) = **SAT-1431** (NOT SAT-1411, which is the lucrativas-family annual); RETENISR family: SAT-1901 (DJ ante el patrono), SAT-1481 (annual liquidation/devolución informe), SAT-1921 (trabajo retention constancia); Planilla IVA-FEL = SAT-1111 (paper 1111 superseded) | `gt/sources/48_FormulariosVigentes.pdf` | dump lines 32-41, 105-109, 118 (EVID-372, EVID-373, EVID-376, EVID-377) |

## 3. Functional Requirements

### 3.1 Hecho generador, taxpayers & retention obligation

- **GT-TAX-FR-111:** The system shall treat as ISR-rentas-del-trabajo every
  retribution or income **in cash** ("en dinero") of any denomination or
  nature from personal work performed in *relación de dependencia*
  (employment relationship) by resident individuals — including the Art. 68
  list: sueldos, bonificaciones, comisiones, aguinaldos, viáticos not
  subject to liquidation or not constituting expense reimbursement, and the
  catch-all "otras remuneraciones"; crews of Guatemala-based/matriculated
  vessels and vehicles regardless of the beneficiary's nationality; and
  board/council remunerations when the member is in relación de
  dependencia. (LB-002; EVID-226)
- **GT-TAX-FR-112:** Rents shall be imputed to the liquidation period in
  which they are **perceived or placed at the worker's disposal** (Art. 69);
  taxpayers are resident individuals earning cash income from dependent
  personal services (Art. 71). (LB-002; EVID-226)
- **GT-TAX-FR-113:** R25 guard: the taxable-remuneration list shall follow
  the 26_ consolidated text of Art. 68 num. 1 (as reformed by D-19-2013);
  the word "propinas" (tips) appears ONLY in the 47_ digest's quotation and
  shall never be asserted as law — recorded as an unverified digest delta
  pending the GOQ-58 post-46-2022 window check; no tip-specific withholding
  behavior shall be implemented from this layer. (LB-002; EVID-226,
  EVID-244; GOQ-58 → OQ-001)
- **GT-TAX-FR-114:** Every *patrono* (employer) paying or crediting
  remunerations — permanent or eventual, including public officials paying
  State salaries — shall be modeled as a mandatory retention agent
  (Art. 75); no retention applies on foreign diplomats/consuls/international
  -organism staff (reciprocity), but resident employees of those missions
  still owe the annual DJ and the missions owe SAT the annual list of
  workers and salaries paid. (LB-006; EVID-229)

### 3.2 Exenciones (Art. 70)

- **GT-TAX-FR-115:** *Aguinaldo* (December statutory bonus) shall be exempt
  up to **100% of one ordinary monthly salary** (*sueldo o salario ordinario
  mensual*); any excess over that cap is taxable remuneration. The bonus
  accrual/payment mechanics themselves are owned by the P-wave payroll files
  (bonus laws D-76-78/D-42-92 cross-ref; never re-derived here).
  (LB-003; EVID-226)
- **GT-TAX-FR-116:** *Bono 14* (bonificación anual para trabajadores del
  sector privado y público) shall be exempt up to **100% of one ordinary
  monthly salary**; excess taxable. Same P-wave cross-ref as FR-115.
  (LB-003; EVID-226)
- **GT-TAX-FR-117:** *Indemnización por tiempo servido* (seniority
  severance) shall be fully exempt; death/incapacity indemnities and
  pensions under social security, insurance or judgment shall be exempt —
  but remunerations received from the employer during *licencias laborales
  con goce de sueldo* (paid leave) are expressly NOT exempt and stay in the
  withholding base. (LB-003; EVID-226)
- **GT-TAX-FR-118:** Diplomatic/consular remunerations (reciprocity) and
  documented *gastos de representación* and *viáticos* shall be exempt —
  in-country viáticos only with invoices issued under national legislation;
  foreign-trip viáticos only with demonstrated exit/entry to Guatemala, the
  activity and transport tickets. (LB-003; EVID-226)
- **GT-TAX-FR-119:** Pensions, jubilaciones and montepíos (IGSS, IPM,
  Clases Pasivas, professional colleges, direct payers to
  disabled/major-age persons) shall be a non-taxable category, stored as a
  dated row: Art. 70 num. 7 added by D-14-2013 art. 72, valid from
  03-12-2013 (pre-2013 treatment is history, non-transmittable class);
  corroborated by 28_ art. 67. (LB-003; LB-009; EVID-226, EVID-239)

### 3.3 Deductions (Art. 72) — dated rows

- **GT-TAX-FR-120:** The personal deduction shall be a dated row:
  **Q48,000.00** per worker per liquidation year, without any vouchers
  ("sin necesidad de comprobación alguna"); provenance "D-10-2012 art. 72.a,
  texto consolidado ≤ D-46-2022" with the GOQ-58 post-46-2022 caveat;
  LAT-era figure, no reform signal in 47_ (EVID-243 cross-check).
  (LB-004; EVID-227, EVID-243; GOQ-58 → OQ-001)
- **GT-TAX-FR-121:** The IVA-paid credit shall be a dated row:
  up to **Q12,000.00** per year on personal goods/services purchases,
  evidenced by the *planilla* (detail of invoices) filed before SAT within
  the **first 10 días hábiles of January** — exactly as printed, with the
  "hábiles" qualifier recorded (GOQ-99); the employer reconciles it against
  retentions and the worker's definitive liquidation. (LB-004; EVID-227;
  GOQ-99 → OQ-004)
- **GT-TAX-FR-122:** The planilla field schema shall implement 28_ art. 68:
  taxpayer identification + NIT + period; employer name + NIT; issuer name
  + NIT; invoice emission date and correlativo; description; per-invoice
  total **IVA included**; per-supplier rows never consolidated into one
  line; vehicle IVA (IVA art. 55) and import IVA includible; amounts not
  usable in any other renta category; no deduction of IVA on expenses
  unreasonable relative to the worker's consumption capacity; **late-filed
  planilla = credit improcedente** ("Dicho crédito será improcedente").
  (LB-009; EVID-239)
- **GT-TAX-FR-123:** The Q48,000 + Q12,000 deductions shall operate under
  the aggregate **Q60,000.00** cap of Art. 72.a, stored as a dated row with
  the same provenance/caveat as FR-120/FR-121. (LB-004; EVID-227)
- **GT-TAX-FR-124:** Worker-share contributions to IGSS, IPM and State
  previsión regimes shall be deductible (Art. 72.c); the contribution
  RATES/base values are external (GOQ-04 — IGSS reglamentos outside the
  corpus) and enter the projection as **estimated** parameters only.
  (LB-004; EVID-227; GOQ-04 → OQ-005)
- **GT-TAX-FR-125:** Donations to the Art. 72.b beneficiaries (Estado,
  universities, cultural/scientific entities; legally constituted
  associations/foundations, churches, religious entities, political
  parties — with fiscal solvencia of the period) shall be deductible up to
  **5% of renta bruta**; donation-receipt mechanics are owned by Task 5
  (28_ art. 19 receipt/solvencia pair — cross-referenced, not duplicated).
  (LB-004; EVID-227)
- **GT-TAX-FR-126:** Life-insurance premiums shall be deductible only for
  contracts covering **death risk exclusively** and only when the contract
  yields no return, reimbursement or surrender value ("no devengue suma
  alguna por concepto de retorno, reintegro o rescate"). (LB-004; EVID-227)
- **GT-TAX-FR-127:** Base definitions shall follow Art. 72 ¶1-2: renta
  bruta = gravados + exentos income of the annual period; renta neta =
  renta bruta − rentas exentas; deductions apply against renta neta.
  (LB-004; EVID-227)

### 3.4 Rate table (Art. 73) & period (Art. 74)

- **GT-TAX-FR-128:** The ISR rentas-del-trabajo scale shall be stored
  verbatim as dated rows — **ANNUAL, exactly two brackets**: "Q.0.01 a Q
  300,000.00 | Q.0.00 | 5% sobre la renta imponible" and
  "Q.300,000.01 en adelante | Q.15,000.00 | 7% sobre el excedente de
  Q.300,000.00"; first bracket = 5% of taxable income, second = Q15,000.00
  + 7% of the excess over Q300,000.00; provenance "D-10-2012 art. 73,
  texto consolidado ≤ D-46-2022" with GOQ-58 caveat (no post-2022 reform
  signal; 47_ reprints identical figures, EVID-243). Task 5 cites this FR
  (single-scale reuse); no other employment-withholding table exists.
  (LB-005; EVID-228, EVID-243; GOQ-58 → OQ-001)
- **GT-TAX-FR-129:** The liquidation period shall be the calendar year,
  1 January through 31 December (Art. 74). (LB-005; EVID-228)

### 3.5 Withholding algorithm (Arts. 75-82 + 28_ arts. 69-73)

- **GT-TAX-FR-130:** The employer monthly withholding shall implement the
  projection algorithm: at the start of each year (or of the employment
  relationship) project the worker's annual net rent; subtract **only**
  the Q48,000 personal deduction plus estimated annual IGSS/IPM/State
  previsión worker shares (the Q12,000 IVA credit is NOT subtracted in the
  projection — it reconciles in January per FR-138); apply the Art. 73
  annual scale (FR-128); withhold **1/12 of the projected amount** each
  month ("la doceava parte del monto proyectado"). (LB-006; LB-009;
  EVID-229, EVID-239)
- **GT-TAX-FR-131:** Mid-year starts: when the projection is made after the
  liquidation period has begun, it shall cover **only the months remaining
  to year-end** ("por el número de meses que hagan falta para la
  finalización del período"); if the worker labored earlier in the same
  period under another employer, the prior income shown in the retention
  constancia presented by the worker shall be **summed** into the annual
  projection. (LB-006; EVID-229)
- **GT-TAX-FR-132:** On any change in the estimated annual net rent, the
  employer shall recalculate **without needing a worker declaration** and
  update the successive monthly retentions; per 28_ art. 69 the adjustment
  of additional payments (gratificaciones/bonificaciones) is spread in
  monthly installments up to the conclusion of the annual period ("en
  cuotas mensuales hasta la conclusión del periodo anual"). (LB-006;
  LB-009; EVID-229, EVID-239)
- **GT-TAX-FR-133:** Partial-year workers shall keep the **FULL Q48,000**
  personal deduction — no pro-rata — and their projected income shall NOT
  be annualized to 12 months ("No podrá limitarse la deducción por gastos
  personales aun en los casos en que la relación laboral no haya durado el
  período anual completo. Tampoco podrá realizarse estimación de ingresos
  proyectados a doce meses por igual causa."). (LB-009; EVID-239)
- **GT-TAX-FR-134:** Multi-employer rule: the worker must inform the fact to
  the employer paying/crediting the **greatest annual remuneration**, which
  becomes the sole retention agent computing the total retention on a
  declaración jurada listing each employer's retributions; copies of the
  form go to the other employers (Art. 77; 28_ art. 69: agent = "el patrono
  que le pague la mayor cantidad de rentas afectas"). (LB-007; LB-009;
  EVID-229, EVID-239)
- **GT-TAX-FR-135:** IGSS/IPM/State previsión shares used in the projection
  shall be flagged **estimated** (Art. 76 "cuotas anuales estimadas"); the
  operative rates are external (GOQ-04) and shall be configurable
  parameters, never constants sourced from this corpus. (LB-006; EVID-229;
  GOQ-04 → OQ-005)

### 3.6 Constancias & worker-facing outputs

- **GT-TAX-FR-136:** Retention *constancias* shall be delivered within the
  **10 days immediately following payment** ("dentro de los diez (10) días
  inmediatos siguientes de efectuado el pago de la renta" — plain días, as
  printed, GOQ-99) with the Art. 78 content set: worker name, employer NIT,
  worker NIT, rent credited/paid, amount withheld; workers not receiving
  constancias may report the agent to SAT. Monthly constancias may be
  **embedded in the payroll boleta** (28_ art. 70). (LB-007; LB-010;
  EVID-229, EVID-239)
- **GT-TAX-FR-137:** A **final constancia** of the total tax retained over
  the whole period shall be delivered within **10 días hábiles** counted
  from the last payment of the annual definitive liquidation period —
  "hábiles" as printed in 28_ art. 70 (GOQ-99) — and likewise at early
  contract termination, where the employer determines the definitive tax and
  refunds/collects the difference (Art. 79 ¶2). (LB-007; LB-010; EVID-229,
  EVID-239)
- **GT-TAX-FR-138:** January reconciliation: at year-end the worker
  presents donation constancias and the employer **determines the
  definitive tax**; in January the employer reconciles retentions vs the
  definitive liquidation — including the up-to-Q12,000 planilla credit
  ("la deducción que hasta por doce mil quetzales (Q 12,000.00) podrá
  considerarse a su favor, con base en la planilla") — and issues the
  annual informe (28_ art. 71). (LB-004; LB-010; EVID-227, EVID-239)
- **GT-TAX-FR-139:** Excess retentions shall be refunded to the worker and
  informed to SAT **within the first 2 months of the calendar year**
  (Art. 79), payable **in one or several cuotas** (28_ art. 72); the
  employer deducts refunds from the monthly retention totals due until
  covering them. (LB-007; LB-010; EVID-229, EVID-239)
- **GT-TAX-FR-140:** The worker's own annual DJ + payment exists **only**
  when the retention agent(s) did not retain or retained less than due
  (Art. 81) — deducing retained amounts — filed **within the first 3 months
  of the following year**; the 28_ art. 73 sanction on the patron follows
  CT (Task 6 cross-ref — amounts never cited from the digest), inapplicable
  to the Art. 75 ¶2 diplomatic cases. (LB-008; LB-010; EVID-229, EVID-239,
  EVID-244)

### 3.7 Employer declaration & payment deadlines (GOQ-99 statutory half)

- **GT-TAX-FR-141:** The employer shall file the monthly retention DJ and
  pay the retained tax **within the first 10 días (plain, as printed) of
  the month following the payment month — even if the retention was
  omitted** ("aunque se hubiese omitido realizar la retención") — with the
  per-worker annex (full name, NIT, concept, rent, amount withheld)
  (Art. 80). Monthly declaration form identity = **SAT-1331** (R46;
  48_/RetWeb, never the digest); filing surfaces = F-wave cross-ref.
  (LB-008; LB-012; EVID-229, EVID-372)
- **GT-TAX-FR-142:** The deadline-qualifier registry (GOQ-99 statutory
  half) shall transcribe each deadline EXACTLY per instrument: **"días
  hábiles"** — Art. 72.a January planilla (first 10) and 28_ art. 70 final
  constancia (10 from last payment); **plain "días"** — Art. 78 constancia
  (10 inmediatos siguientes) and Art. 80 retention DJ/payment (first 10 of
  following month); **months** — Art. 79 refund (first 2 of the year) and
  Art. 81 worker DJ (first 3 of the following year). The RetWeb
  constancia-delivery asymmetry ("primeros (5) días" WITHOUT hábiles,
  R54/EVID-412) is an F-wave cross-ref, not this layer's rule.
  (LB-004; LB-007; LB-008; LB-010; EVID-227, EVID-229, EVID-239; GOQ-99 →
  OQ-004)

### 3.8 Practice layer (GOQ-61; 47_-sourced, never law)

- **GT-TAX-FR-143:** The employer-side annual declaration-before-patrono
  workflow shall be modeled per the practice layer as **SAT-1901 "ISR
  ANTE PATRONO"** with its two modes — PROYECTADA (year-start projection /
  multi-employer election) and DEFINITIVA (year-end/exit) — identity
  anchored to the 48_ RETENISR family (EVID-376), mechanics described by
  the 47_ digest only (GOQ-61 validity/dating caveat; never cited as law).
  (LB-012; EVID-245, EVID-376; GOQ-61 → OQ-002)
- **GT-TAX-FR-144:** Practice instruments recorded as identity-guarded
  rows: monthly ISR retenciones DJ = **SAT-1331**; worker annual DJ
  (relación de dependencia) = **SAT-1431** (R46 corrected identities —
  never SAT-1321/SAT-1411); **RETENISR2** desktop tool (capture/print,
  auto-generates the annual conciliation and retention DJ, BancaSAT
  transmission); **SAT-1481** (annual liquidation/devolución informe) and
  **SAT-1921** (trabajo retention constancia) from the 48_ RETENISR
  family; 47_-sourced signals carry the GOQ-61 flag pending catalog
  confirmation. (LB-012; EVID-245, EVID-372, EVID-373, EVID-376; GOQ-61 →
  OQ-002)
- **GT-TAX-FR-145:** The Q12,000 planilla intake shall integrate the
  practice-layer **Planilla IVA-FEL** (SAT-1111, application-generated;
  paper 1111 superseded — EVID-377): auto-loading the employee's FEL
  invoices as the credit source data, per the 47_ description with
  prerequisites (Agencia Virtual user, RTU Digital update, "Régimen
  Asalariado" affiliation) and QR-verifiable electronic reception notice —
  all GOQ-61-flagged; the FEL invoice side is owned by GT-EINV
  (cross-ref). (LB-012; EVID-245, EVID-377; GOQ-61 → OQ-002)

### 3.9 Employer-side interfaces (cross-references)

- **GT-TAX-FR-146:** Employer deduction pairing (Task 5 owns the full
  art. 21/23 matrices — cited, not duplicated): aguinaldo and bono 14
  deductible up to 100% of one monthly salary each (subject to collective
  agreements), indemnizaciones capped at 8.33% of annual remunerations,
  IGSS/IRTRA/INTECAP employer quotas fully deductible (art. 21); expenses
  are NON-deductible while the corresponding ISR retention is unpaid
  (art. 23.c — "Serán deducibles una vez se haya enterado la retención")
  and salaries off the IGSS planilla are non-deductible (art. 23.f) —
  the retention↔deduction dependency Odoo must model; sanction hooks =
  CT 94.7/94.18 via Task 6. (LB-011; EVID-219, EVID-220, EVID-244)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance + as-of qualifier; snapshot-on-write; rate/cap/deadline rows are
decree-bound, never constants (GOQ-50 pattern); historical rows are
non-transmittable class. Art. 72/73 values are LAT D-10-2012-era figures
with the GOQ-58 post-46-2022 caveat on every row.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.isr.trabajo.scale | bracket_floor / bracket_ceiling / fixed_amount / rate / valid_from / provenance | decimal / decimal / decimal / decimal / date / char | Row 1: Q0.01–Q300,000.00, Q0.00, 5%; Row 2: Q300,000.01–∞, Q15,000.00, 7% over the Q300,000.00 excess; annual base; provenance "D-10-2012 art. 73, texto ≤ D-46-2022" (GOQ-58 caveat); single scale serves withholding AND liquidation | FR-128 |
| l10n_gt.isr.trabajo.deduction | key / amount_or_pct / valid_from / provenance | char / decimal / date / char | personal Q48,000.00 (no vouchers); iva_credit Q12,000.00 (planilla-gated); aggregate cap Q60,000.00; donaciones 0.05 × renta bruta; igss_ipm_prevision (worker shares, estimated — GOQ-04 external rates); life_insurance (no-surrender flag) | FR-120, FR-121, FR-123..127 |
| l10n_gt.isr.trabajo.exemption | numeral / description / params / valid_from | integer / char / json / date | aguinaldo ≤100% ordinary monthly salary; bono 14 ≤100%; indemnización tiempo servido (full); death/incapacity indemnities; diplomats (reciprocity); representación/viáticos comprobables; pensions num. 7 valid_from 2013-12-03 (D-14-2013); licencias con goce de sueldo expressly taxable | FR-115..119 |
| l10n_gt.isr.trabajo.withholding.config | subtract_iva_credit_in_projection / pro_rate_personal_deduction / annualize_partial_year / months_divisor | boolean / boolean / boolean / integer | false / false / false / 12 (Q48,000-only projection; no pro-rata; remaining-months projection; doceava parte) | FR-130..133 |
| l10n_gt.isr.trabajo.planilla.line | field set per 28_ art. 68 | char/decimal/date | taxpayer ID+NIT+período; patrono name+NIT; emisor name+NIT; factura fecha+correlativo; description; valor total IVA-incluido per factura; per-supplier no-consolidation flag; vehicle/import IVA includible; late_filed → credit_improcedente | FR-122 |
| l10n_gt.isr.trabajo.deadline | key / count / unit / habiles / instrument | char / integer / selection(dias/meses) / boolean / char | planilla_january 10 días hábiles (art. 72.a); constancia_pago 10 días (art. 78); constancia_final 10 días hábiles (28_ art. 70); retencion_dj_pago 10 días (art. 80, omitted-retention survives); refund 2 meses (art. 79); worker_dj 3 meses (art. 81) | FR-121, FR-136..142 |
| l10n_gt.isr.trabajo.form.practice | form_code / name / modes / source / goq_flag | char / char / char / char / char | SAT-1901 ISR ANTE PATRONO (PROYECTADA/DEFINITIVA); SAT-1331 ISR Retenciones (R46 identity — 48_); SAT-1431 Relación de Dependencia anual (R46 — 48_); SAT-1481; SAT-1921; SAT-1111 Planilla IVA-FEL; RETENISR2 tool — 47_-sourced rows carry GOQ-61 | FR-141, FR-143..145 |
| l10n_gt.isr.trabajo.delta.guard | delta_key / disposition | char / char | "propinas" (47_ art. 68.1 insertion) = unverified digest addendum, never law (R25); "Decreto 10-2013" [sic] fn. 15 = typo | FR-113 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = emission,
transformation and authoritative validation in the Elixir core; `shared` =
contract items both sides must honor identically. Taxation-wave defaults
(binding): bracket/cap dated data = `shared`; payroll withholding
computation + constancia = `odoo` (cross-ref P-wave payroll engine); DJ
surfaces = F-wave cross-ref. Model names stable across Odoo 17/18/19/20; no
version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-111 | odoo | hr.payslip input / hr.contract | cash-remuneration classifier | "en dinero" test + art. 68 list incl. crews/board members; P-wave payroll engine owns payslip structure (cross-ref) |
| FR-112 | odoo | hr.payslip | perception date imputation | Percibidas o puestas a disposición |
| FR-113 | shared | — | guard row | "propinas" never asserted as law (R25); GOQ-58 watch |
| FR-114 | odoo | hr.employee / res.partner (employer) | retention-agent flag + diplomat carve-out | Missions' annual list duty recorded as obligation data |
| FR-115 | odoo | hr.payslip (aguinaldo line) | exempt ≤ 1 ordinary monthly salary | Excess spills into taxable base; bonus law mechanics = P-wave |
| FR-116 | odoo | hr.payslip (bono 14 line) | exempt ≤ 1 ordinary monthly salary | Same P-wave cross-ref |
| FR-117 | odoo | hr.payslip / hr.exit flow | indemnización exempt; paid-leave taxable | P-wave severance/doubling files pair here |
| FR-118 | odoo | hr.expense / payslip input | viáticos documentation flags | In-country invoices vs abroad exit/entry+tickets |
| FR-119 | shared | — (config data §4) | exemption row valid_from 2013-12-03 | Dated row; corroborated 28_ art. 67 |
| FR-120 | shared | — (config data §4) | Q48,000 dated row | GOQ-58 caveat; both sides resolve same row |
| FR-121 | shared | — (config data §4) | Q12,000 + 10-días-hábiles January row | Qualifier exact (GOQ-99) |
| FR-122 | odoo | l10n_gt planilla lines | 28_ art. 68 field schema | Late-filed → credit improcedente; per-supplier rows |
| FR-123 | shared | — (config data §4) | Q60,000 aggregate row | |
| FR-124 | shared | — (config data §4) | IGSS/IPM deduction row, estimated | Rates external (GOQ-04) |
| FR-125 | odoo | hr.payslip donation input | 5% renta bruta cap | Receipt/solvencia mechanics = Task 5 |
| FR-126 | odoo | hr.payslip insurance input | no-surrender test | |
| FR-127 | odoo | hr.payslip aggregation | bruta/neta definitions | |
| FR-128 | shared | — (config data §4) | art. 73 scale rows verbatim | Single scale for withholding + liquidation; T5 cites by FR id |
| FR-129 | shared | — | calendar-year period | |
| FR-130 | odoo | hr.payslip (ISR rule) | projection algorithm | Q48,000-only; ÷12; P-wave payroll engine pairing |
| FR-131 | odoo | hr.contract start flow | remaining-months projection | Prior-employer constancias summed |
| FR-132 | odoo | hr.payslip recalc | change-driven recalc, monthly installments | No worker declaration needed |
| FR-133 | odoo | hr.payslip (partial year) | full Q48,000, no annualization | 28_ art. 69 verbatim rule |
| FR-134 | odoo | hr.employee multi-employer | highest-patrono agent election | DJ listing + copies to others |
| FR-135 | shared | — (config data §4) | estimated-shares parameter | GOQ-04 external rates, configurable |
| FR-136 | odoo | hr.payslip report (boleta) | constancia ≤10 días; boleta embedding | SAT-1921 practice identity (GOQ-61) |
| FR-137 | odoo | hr.payslip year-end report | final constancia 10 días hábiles | Exit variant per art. 79 ¶2 |
| FR-138 | odoo | hr.payslip January close | reconciliation + Q12,000 credit | 28_ art. 71 informe |
| FR-139 | odoo | hr.payslip refund flow | ≤2 months, one or several cuotas | Deduct from monthly retention totals |
| FR-140 | odoo | worker DJ eligibility | only no/short retention, ≤3 months | Surface = SAT-1431 (F-wave cross-ref) |
| FR-141 | odoo | account.move (retention entries) + monthly DJ data | 10 días, omitted-retention survives | Form identity SAT-1331 (R46); F-wave owns filing surface |
| FR-142 | shared | — (config data §4) | deadline-qualifier registry | GOQ-99 statutory half; R54 asymmetry = F-wave |
| FR-143 | shared | — (config data §4) | SAT-1901 modes row | Practice layer (GOQ-61); odoo surfaces the modes |
| FR-144 | shared | — (config data §4) | practice form registry | R46 identities from 48_; GOQ-61 flag |
| FR-145 | odoo | FEL invoice intake (planilla) | Planilla IVA-FEL / SAT-1111 | FEL side = GT-EINV; GOQ-61 flag |
| FR-146 | odoo | account.move line (employer expense) | deduction gating flags | art. 21/23 matrices owned by Task 5; CT hooks = Task 6 |

## 6. Acceptance Criteria

- **AC-001:** Given any cash remuneration of a resident individual in
  relación de dependencia (sueldos, bonificaciones, comisiones, aguinaldos,
  non-liquidation viáticos, crew/board remunerations), when processed,
  then it enters the ISR withholding base; given a non-cash item or income
  outside Art. 68, then it does not. (FR-111, FR-112)
- **AC-002:** Given the word "propinas" anywhere in seeded taxable-income
  catalogs, when inspected, then it appears only inside the R25 delta-guard
  row marked unverified digest addendum — never as a statutory category.
  (FR-113)
- **AC-003:** Given an aguinaldo or bono 14 payment exceeding one ordinary
  monthly salary, when the payslip computes, then only the exempt portion
  (≤ 100% of one monthly salary each) is excluded and the excess is
  withheld upon; given an indemnización por tiempo servido payment, then it
  is fully exempt; given paid-leave remuneration, then it is fully taxable.
  (FR-115..117)
- **AC-004:** Given the scale registry read as-of any payslip date, then it
  resolves exactly two annual rows — 5% ≤ Q300,000.00 (fixed Q0.00) and
  Q15,000.00 + 7% over Q300,000.00 — with provenance "D-10-2012 art. 73,
  texto ≤ D-46-2022" and the GOQ-58 caveat, and no per-payroll or monthly
  withholding table exists anywhere. (FR-128)
- **AC-005:** Given a worker with projected annual net rent Q200,000, no
  other deductions, when January withholding runs, then the monthly
  retention equals (200,000 − 48,000 − estimated IGSS/IPM shares) × 5% ÷
  12 — the Q12,000 IVA credit is NOT subtracted. (FR-130)
- **AC-006:** Given a worker hired 1-July with no prior employer, when the
  projection is built, then it covers July–December only while still
  subtracting the FULL Q48,000; no 12-month income annualization occurs.
  (FR-131, FR-133)
- **AC-007:** Given a worker with two employers, when multi-employer
  handling runs, then only the highest-remuneration employer withholds on
  the aggregated declared retributions and the other employer receives the
  form copy and withholds nothing. (FR-134)
- **AC-008:** Given the deadline registry, when inspected, then the
  "hábiles" qualifier is present ONLY on the January planilla and final
  constancia rows, absent (plain días) on the Art. 78 constancia and
  Art. 80 DJ/payment rows, and month-based on the refund (2) and worker DJ
  (3) rows — each transcribed per its instrument (GOQ-99). (FR-142)
- **AC-009:** Given a month where an employer omitted a retention, when
  the monthly close runs, then the DJ + payment obligation still generates
  for the first 10 días of the following month with the per-worker annex.
  (FR-141)
- **AC-010:** Given a planilla line consolidating two invoices of one
  supplier into a single row, or a planilla filed after the first 10 días
  hábiles of January, when validated, then it is rejected (per-supplier
  rule; credit improcedente). (FR-121, FR-122)
- **AC-011:** Given excess retention at year-end, when reconciliation
  closes, then the refund registers within the first 2 months of the year
  in one or several cuotas, offset against monthly retention totals.
  (FR-139)
- **AC-012:** Given any form-naming surface, when citations are generated,
  then ISR retenciones = SAT-1331 and asalariados anual = SAT-1431 (R46)
  with identities sourced to 48_/RetWeb — never to the 47_ digest, and
  never SAT-1321/SAT-1411. (FR-141, FR-144)
- **AC-013:** Given an employer expense backed by an unretained/unpaid ISR
  retention or a salary off the IGSS planilla, when deduction eligibility
  evaluates, then it is blocked/suspended until the retention is entered
  (art. 23.c/f gating; full matrix owned by Task 5). (FR-146)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
allowed set for this file: GOQ-58/60/61 (owned), GOQ-99 (kin, statutory
half), GOQ-04 (kin). All rows Status open; GOQs are trace-pending, not
blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-58 (owned): "LAT post-46-2022 window: any Libro I reform after 27-09-2022 absent (the 47_ 'propinas' hint re-checked here)." Affects FR-113 (propinas delta), FR-120/121/123 (Q48,000/Q12,000/Q60,000), FR-128 (art. 73 scale) — every dated row carries the caveat until a current consolidated LAT or DCA check clears the window. | no | GT synthesis wave S-GT2 → acquisition queue (current consolidated LAT / DCA) | open |
| OQ-002 | GOQ-61 (owned): "47_ practice layer: forms SAT-1901/SAT-1331/RETENISR2/Planilla IVA-FEL/BancaSAT validity + snapshot dating (undated unsigned digest)." Affects FR-143/144/145 practice rows — identities anchored to 48_ where possible (R46); mechanics/dating pending SAT catalog confirmation. | no | GT synthesis wave S-GT2 → F-wave catalog confirmation | open |
| OQ-003 | GOQ-60 (owned): dieta retention "con carácter definitivo" (28_ art. 9) — operative rate not spelled. Affects board-member remunerations that fall in relación de dependencia (FR-111 num. 3); Task 5 shares the gap. | no | GT synthesis wave S-GT2 → SAT practice determination | open |
| OQ-004 | GOQ-99 (kin, statutory half): deadline qualifiers transcribed exactly per instrument (FR-142 registry); the RetWeb "primeros (5) días" constancia-delivery asymmetry (R54) and the 64_ formulations defer to the F-wave deadline CRs. | no | F-wave (deadline CRs); this file supplies the statutory half | open |
| OQ-005 | GOQ-04 (kin): IGSS cuota rates / minimum base / tope / cotizable components all external (JD reglamentos, Acuerdo 1118 family / 1421). Affects FR-124/FR-135 — projection consumes estimated worker shares as configurable parameters; never constants from this corpus. | no | P4 (IGSS rate/base CRs) → acquisition queue | open |
