# GT — Payroll — IGSS contributions: D-295 architecture, 08-SGF/2026 recaudación and the Planilla Electrónica lifecycle

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-23 (W-GT8 backfill: IGSS program-reglamento set 104_-108_, LB-026) |

## 1. Purpose

This file defines the Guatemalan social-security contribution and collection
cycle (cluster P4): the *Instituto Guatemalteco de Seguridad Social* (IGSS)
law layer of Decreto 295, *Ley Orgánica del IGSS* (1946; D-11-2004 is a
governance-only reform, R39) — the *triple contribución* financing structure
(25% trabajadores / 50% patronos / 25% Estado of the total cost — financing
PROPORTIONS, never cuota rates) with the cuota MONTOS expressly delegated to
Junta Directiva PROGRAM reglamentos (Acuerdo 1421 art. 1 delegates the
montos to the reglamentos of the respective coverage programs — ALL rate,
base, tope and component values external per GOQ-04, target REFINED to the
program reglamentos — SEM set `104_`-`106_` acquired 2026-08-23 RATELESS,
rate target now the IVS Acuerdo 1124 + the 410 art.-85 chain — LB-026), the
employer-share
no-deduction invariant (*nulo ípso jure*), the share-shift cases
(salario-mínimo earners and riesgos profesionales may load the worker share
onto the patrono), the first-class credit privilege with the *certificación
de Gerencia* as *título ejecutivo* (económico-coactivo), and the art. 50
inspection powers over libros and planillas; and the procedure layer of
Resolución 08-SGF/2026 (19-Jan-2026, repeals SGF-R/2020 No. 342) — the
patrono as collection agent withholding and delivering BOTH shares
(*contribuciones laborales y patronales*) for permanent, temporary and
part-time workers, the monthly minimum contribution BASE as a FLOOR (employer
tops up the difference when salary < base; amount external) with NO tope
máximo anywhere in the corpus (negative finding), proration for mid-month
alta/baja and IGSS medical suspensions, the CPR arts. 88/100 exempt-patrono
carve-outs, the Planilla Electrónica lifecycle state machine
GENERAR→TRANSMITIR→VALIDAR→PAGAR with rectificación/complemento gated on
estado "pagada" and auto-generated recargos, ONE planilla per registro
patronal (afectos y no afectos a IVS reported together) plus additional
planillas per obra/servicios contract, the SINGLE payment receipt settling
IGSS + IRTRA + INTECAP in one event, late payment accepted with mora, the
mora engine (day after due date; Cuotas IGSS × tasa × días/365(366); tasa
RULE anchored at Acuerdo 1421 art. 38 — the Junta Monetaria's latest
maximum simple-annual rate on the weighted banking rate for active
operations, an inherently external floating index publication, GOQ-10
resolved at rule level) with the +5% gastos administrativos cap Q3,000
(source layer: Acuerdo 1421 arts. 22/24), the nota de
cargo clock chain (5/15/15/5 días hábiles), the reconocimiento de deuda
regime (≤60 months, same-day first payment, 2-missed acceleration, 100% cap),
the four recargo-waiver cases with 6-month windows and 45-días-hábiles
execution (retroactive pay IS contribution-bearing), the revisiones contables
with estimate floor = salario mínimo of the AG vigente, the Q500
incobrabilidad minimum, the closed ±1% rounding tolerance, and the
Mar-1977/Sep-2022 historical cutoff ledger.

It does **not** cover: the salario/salario-completo model and the CT art. 102
headcount-triggered book-mode selection (`01_ct-salary-model.md` — GT-PAY-FR-005
salario completo; GT-PAY-FR-018 selects IGSS-model planillas for 3–9 workers,
of which THIS file owns the mechanics); the salario mínimo chassis and dated
AG tables (`03_minimum-wage.md` — GT-PAY-FR-073 supplies the "AG vigente"
as-of resolution for the estimate floor and the minimum-base kinship);
statutory bonuses, including the incentivo's non-contributory character
(`04_statutory-bonuses.md` — GT-PAY-FR-091: incentivo enters IGSS/IRTRA/
INTECAP bases ONLY on recorded joint agreement); vacaciones and maternidad
(`05_vacaciones-maternidad.md` — GT-PAY-FR-116 owns the maternity
employer-pay-vs-IGSS-covered branch; this file owns the IGSS program side);
IRTRA and INTECAP patronal charges and their rates
(`08_irtra-intecap.md` — their quotas ride this file's single receipt but
their values are owned there, never printed here); the ISR/IVA payroll
interfaces (`09_isr-iva-interfaces.md` — the estimated worker-side IGSS
shares feeding GT-TAX-FR-124 and GT-TAX-FR-135 arrive from this file's
external-parameter rows as configuration, never as corpus-sourced values);
occupational-safety duties (`10_sso-provenance.md` — AG 229-2014 is an
occupational-safety instrument with ZERO cuota content, R40); the Planilla
IVA-FEL (a SAT asalariado January filing sharing only the word "planilla");
and the special-regimes IGSS-suspension ladder of the ZF/maquila wave
(S-GT6/S-GT7 — cross-reference only at their dispatch). Sanction values of
the Código Tributario art. 94 family belong to
`gt/requirements/taxation/06_ct-procedures.md`; the art. 23.f no-IGSS-planilla
deduction gate is consumed by id (GT-TAX-FR-146).

## 2. Legal Basis

Authority order (binding, per master evidence index P4): IGSS mechanics cite
`35_` (Resolución 08-SGF/2026 + its 45-hoja Instructivo) at the procedure
layer, `33_` (D-295) at the law layer and `87_` (JD Acuerdo 1421, approved
by AG 180-2018 — LB-025) at the collection-reglamento layer — but **ALL
rate/base/tope values are external** (JD PROGRAM reglamentos: Acuerdo 1421
art. 1 expressly delegates the montos to the reglamentos of the respective
coverage programs — GOQ-04, acquisition target REFINED to the program
reglamentos, not the recaudación line — and RE-REFINED 2026-08-23 per
LB-026: the SEM program reglamento, Acuerdo 410 (`104_`/`106_`), is NOW IN
CORPUS but RATELESS): never cite 33_-36_ or 87_ for a
rate — 1421 prints NO cuota rate, base amount, tope or component percentage
anywhere — and the `104_`-`108_` set prints NO operative rate either: its
only cuota text is art. 62's 1964 originals (4%/2%/1%; the `106_` 2011
print reads 3%), departamento-de-Guatemala-only per art. 85 and superseded
by the unprinted extension chain Acuerdos 475→1243 — the operative-rate
targets are the IVS program reglamento Acuerdo 1124 (named by `107_`) +
that chain (LB-026). The 12.67% patronal / 4.83%
laboral priors are NOT verifiable from this corpus (R34) — rejected priors,
never constants. What `35_` prints and owns are the procedural values: 5%
gastos administrativos (cap Q3,000), 100% recargo/interés cap inside
reconocimientos de deuda, ±1% tolerance, Q500 incobrabilidad, and every
días-hábiles clock below — and their statutory SOURCE layer is now also in
corpus: `87_` supplies the planilla due date (art. 9: day 20), the mora
tasa rule + general 100% cap (art. 38), the 5%/Q3,000 admin recargo at
source (arts. 22/24), the RD interest index rule (art. 31 c)) and the
incobrabilidad triggers (arts. 39-40, LB-025). The 1946 `33_` pages are the noisiest OCR in the
corpus — every D-295 verbatim carries `[sic]` tolerance (GOQ-74); D-11-2004
is governance-only (R39). `36_` is an undated IGSS guide: corroboration
only, never authority (EVID-323). `34_` (AG 229-2014) is an
occupational-safety reglamento with zero cuota/recaudación content (R40).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D-295, identity/provenance (Hemeroteca-certified copy): "ORGANO LEGISLATIVO / DECRETO NUMERO 295" / certification: "son copia fiel del original … consisten en el DIARIO DE CENTRO AMÉRICA de fecha treinta y uno (31) de octubre, diario número ochenta y tres (83) páginas número novecientos veintisiete (927) a la novecientos veintinueve (929), donde inicia la publicación del DECRETO NÚMERO 295 LEY ORGÁNICA DEL INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL; continua el uno (1) de noviembre, diario número ochenta y cuatro (84) … y concluye el cuatro (4) de noviembre, diario número ochenta y cinco (85)" / art. 12 transitorio: "Esta ley debe entrar en vigor el día de su publicación en el Diario oficial" | D-295 = the 1946 IGSS Organic Law, published in THREE DCA installments (31-Oct/1-Nov/4-Nov-1946; given 28-Oct-1946, sanctioned 30-Oct-1946; certified photocopy 13-Oct-2023); it enters into force on the day of its publication in the official gazette — WHICH installment triggers vigencia is not determinable from this print (GOQ-74) | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | p.1 masthead; p.6 art. 12; p.12 certification (EVID-301, EVID-308) |
| LB-002 | D-295, arts. 38-39 (Capítulo V): "El régimen de Seguridad social debe financiarse así: a) Durante todo el tiempo en que sólo se extienda y beneficie a la clase trabajadora, o a parte de ella, por el método de triple contribución a base de las cuotas obligatorias de los trabajadores, de los patronos y del Estado" / "Los reglamentos deben determinar en cada caso, el monto de las cuotas o contribuciones, de acuerdo con el costo total…" / "Las tres partes deben contribuir a sufragar el costo total de los beneficios que en determinado momento se den, en la siguiente proporción: Trabajadores … 25% / Patronos … 50% / Estado … 25%" (OCR interleaves the labels: ".. 25% ... 50% 2... 25% Trabajadores + Patronos .... Estado" [sic]) / "[L]as cuotas de los patronos no pueden ser deducidas de los salarios de los trabajadores y es nulo ípso jure todo acto o convenio en contrario." / exceptions: for "riesgos profesionales o de trabajadores que sólo devenguen el salario mínimo … el Instituto queda facultado para poner la totalidad de las cuotas de trabaj[a]dores y de patronos a cargo exclusivo de estos últimos" | Arts. 38-39: the regime is financed by triple contribución (obligatory cuotas of workers, employers and the State); the REGLAMENTOS determine in each case the monto of the cuotas per actuarial cost; the three parts contribute to the total cost in the proportion trabajadores 25% / patronos 50% / Estado 25% — FINANCING PROPORTIONS of total cost, never cuota rates; employer cuotas may NEVER be deducted from worker salaries, any contrary act or agreement being null ipso jure; for occupational risks or minimum-wage-only earners the Institute may load the TOTALITY of both cuota shares exclusively onto the employer | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | p.6, arts. 38-39 (EVID-302) |
| LB-003 | D-295, art. 19 a): "Dictar, a propuesta del gerente los reglamentos necesarios para la correcta aplicación de esta ley … Los reglamentos que se refieran a fijación de cuotas « [sic] de beneficios, a aplicación de algun[a] clase de éstos a cierta circunscripción territorial o capa de la población, o a determinación de penas, deben ser elevados al Organismo Ejecutivo, por conducto del Ministerio de Economía y Trabajo, para su aprobación y publicación inmediata en el Diario oficial." | Art. 19 a): JD reglamentos that FIX cuotas (or benefits-application or penalties) must be elevated to the Organismo Ejecutivo for approval and immediate DCA publication — the procedural chain locating every operative rate instrument (reglamento → AG approval → gazette); none of those instruments is in this corpus (GOQ-04) | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | p.2, art. 19 a) (EVID-303) |
| LB-004 | D-295, arts. 40 y 42: "La cuota del Estado como tal y como patrono se debe financiar con los impuestos que al efecto se creen o determinen" / "a) Las certificaciones de la Gerencia sobre sumas adeudadas al Instituto, constituyen título ejecutivo, y estas últimas se deben cobrar conforme al procedimiento económico-coactivo, siempre que se trate de cuotas o contribuciones; b) Los créditos a favor del Instituto tienen el privilegio de créditos de primera clase con preferencia absoluta sobre cuá[l]squiera otros, excepto los que el deudor respectivo tenga a favor de terceros por concepto de salarios…" | Art. 40: the State's own cuota (as State and as employer) is financed with taxes created for the purpose; art. 42: Gerencia certifications of sums owed to the Institute are TÍTULO EJECUTIVO collectible under the económico-coactivo procedure for cuotas/contributions, and IGSS credits are FIRST-CLASS privileged with absolute preference over any others EXCEPT the debtor's salary credits toward third parties | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | pp.6-7, arts. 40 y 42 (EVID-304) |
| LB-005 | D-295, art. 50 a)-b), f): "El Departamento de inspección y de visitaduría social del Instituto debe velar por que patronos y afiliados cumplan las prescripciones de esta ley y de sus reglamentos … a) Pueden visitar los lugares de trabajo … b) Pueden revisar libros de contabilidad, de salarios, planillas, constancias de pago y cualesquiera otros documentos … f) Las actas que levanten y los informes [de sus inspeccio]nes, tienen plena validez en tanto no se demuestre de modo evidente su inexactitud, falsedad o parcialidad" | Art. 50: the IGSS inspection department may visit workplaces and examine accounting books, salary books, PLANILLAS, payment certificates and any other documents; its actas and reports carry FULL VALIDITY (prima facie) unless evident inaccuracy, falsity or partiality is shown — the statutory basis of the 08-SGF/2026 revisiones contables | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | p.8, art. 50 a)-b), f) (EVID-305) |
| LB-006 | D-295, arts. 52-57 (sanctions frame): "a) Las penas consisten en multas, que son convertibles en arresto en caso de no pago oportuno … b) Los límites máximo y mínimo de cada pena ordinaria deben fijarse entre uno y quinientos quetzales, de acuerdo con la gravedad de la infracción; … c) Toda reincidencia debe dar lugar a una duplicación de la pena anteriormente impuesta" / art. 57: penas apply "tanto [a] la persona directamente responsable de la infracción, como al patrono en cuya empresa se haya cometido la falta" | The 1946 sanction envelope: court-imposed fines Q1–Q500 (1946 quetzals, convertible to arrest), doubling on reincidence, joint liability of responsible person and patrono — SUPERSEDED IN PRACTICE for recaudación matters by the Acuerdo 1421/08-SGF/2026 recargos + económico-coactivo apparatus (never the operative collection teeth for cuotas) | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | p.8, arts. 52-57 (EVID-306) |
| LB-007 | D-295, arts. 34-35: "Las prestaciones en dinero acordadas a los afiliados, no pueden cederse, compensarse ni gravarse, ni son susceptibles de embargo, salvo en la mitad por concepto [de] pagar alimentos." / "El derecho de reclamar el otorgamiento de una pensión prescribe en un año y el derecho de cobrar las pensiones o indemnizaciones acordadas prescribe en seis meses" | Benefit-side protections: money benefits granted to affiliates cannot be assigned, compensated, encumbered or attached EXCEPT up to one half for alimony; the right to claim a pension prescribes in ONE YEAR and the right to collect granted pensions/indemnizations in SIX MONTHS — CLAIM-side clocks, never employer-contribution-side | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | pp.5-6, arts. 34-35 (EVID-307) |
| LB-008 | D-11-2004 (whole, arts. 1-5): "Artículo 1. Se reforman las literales a) y d) del artículo 16 … 'a) Deben ser nombrados por la Junta Directiva, por mayoría representada por un mínimo de cinco votos…'" / "Artículo 2. Se reforma el artículo 18 … la Junta Directiva puede removerlos en cualquier momento, libremente y sín [sic] expresión de causa" / "Artículo 5. … entra en vigencia el día siguiente de su publicación en el diario oficial" | D-11-2004 (DCA 7-May-2004; vigencia 8-May-2004 computed) touches ONLY arts. 16 a)/d) and 18 of D-295 — the Junta Directiva appoints and may freely remove the Gerencia: a GOVERNANCE reform with ZERO effect on cuotas, recaudación or payroll (R39; the file label "D295_D11-2004" is base law + governance reform only) | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | pp.13-14, arts. 1-5 (EVID-308) |
| LB-009 | D-295, arts. 28 y 32: "El régimen de Seguridad social comprende protección y beneficios en caso de que ocurran [los] siguientes riesgos de carácter social: a) Accidentes de trabajo y enfermedades profesionales; b) Maternidad; c) Enfermedades generales; d) Invalidez; e) Orfandad; f) Viudedad; g) Vejez; h) Muerte (gastos de entierro); i) Los demás que los reglamentos determinen." / "La protección relativa a invalidez, orfandad, viudedad y vejez, consiste en pensiones a los afiliados…" | The risk catalog the cuotas finance (art. 28); "los demás que los reglamentos determinen" is the opening through which the modern program split — IM (enfermedad/maternidad) vs IVS (Invalidez, Vejez y Sobrevivencia, as named in 08-SGF/2026) — was built at REGLAMENTO layer, outside this corpus (GOQ-04) | `gt/sources/33_IGSS_Ley_Organica_D295_D11-2004.pdf` | p.5, art. 28; pp.5-6, art. 32 (EVID-309) |
| LB-010 | Resolución 08-SGF/2026, identity + resolutivos: "RESOLUCIÓN 08-SGF/2026 / LA SUBGERENCIA FINANCIERA DEL INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL: En la ciudad de Guatemala, el diecinueve de enero de dos mil veintiséis." / "Primero. Aprobar el “INSTRUCTIVO PARA LA APLICACIÓN DEL REGLAMENTO SOBRE RECAUDACIÓN DE CONTRIBUCIONES AL RÉGIMEN DE SEGURIDAD SOCIAL”, el cual queda contenido en cuarenta y cinco (45) hojas…" / "Sexto. La presente Resolución deja sin efecto la Resolución SGF-R/2020 No. 342, emitida por el Subgerente Financiero el tres de julio del dos mil veinte … la cual entra en vigencia a los 30 días hábiles contados" [text cut by OCR] | Resolución 08-SGF/2026 (19-Jan-2026) of the IGSS Subgerencia Financiera approves the 45-sheet recaudación instructivo and repeals SGF-R/2020 No. 342 (3-Jul-2020); its vigencia rule — "30 días hábiles contados…" — is OCR-truncated: the count basis is unknown (GOQ-75); no DCA publication is evidenced (internal IGSS instrument) | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.1-3, resolutivos Primero-Sexto (EVID-310) |
| LB-011 | 08-SGF/2026 §V num. 1: "Para financiar el Régimen de Seguridad Social, es obligatorio que se contribuya con un porcentaje de los salarios que paguen los patronos del sector privado, el Estado como patrono y el Estado como tal, así también deben contribuir los trabajadores permanentes, temporales y a tiempo parcial si los hubiere, según los porcentajes que sobre los salarios fijan los reglamentos emitidos por la Junta Directiva, relacionados con los programas de cobertura del Instituto Guatemalteco de Seguridad Social." / Introducción: "El Reglamento establece las normas para la recaudación de las cuotas o contribuciones patronales y laborales que deben entregar los patronos al Instituto en la forma y plazo establecidos en la normativa interna respectiva" | WHO contributes and WHERE rates live: contribution is obligatory as a PERCENTAGE of the salaries paid by private-sector employers, the State as employer and the State as such; permanent, temporary and part-time workers ALL contribute; the percentages are those that "los reglamentos emitidos por la Junta Directiva" fix on salaries — NO percentage is printed anywhere in the instrument (a full-text sweep confirms only procedural percentages: 5% admin, 100% RD cap, ±1% tolerance, Q500) | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | p.6, §V num. 1; p.5 Introducción (EVID-311) |
| LB-012 | 08-SGF/2026 §V num. 1 ¶2-3: "El monto base para el cálculo de la contribución mensual mínima a la Seguridad Social, es independiente del tipo de contrato o relación de trabajo existente entre los trabajadores y sus patronos, así como el tipo de jornada de trabajo efectivo, días laborados dentro del periodo de contribución, circunscripciones económicas o geográficas; y éste se aplicará únicamente cuando un trabajador devengue un salario menor a dicha base, para lo cual el patrono es responsable del pago de la diferencia entre la contribución mínima mensual y la suma de las contribuciones laboral y patronal calculadas con base al salario devengado por el trabajador." / "Cuando la relación laboral inicie o finalice cualquier día diferente al primero o al último día del mes calendario o periodo que corresponda, así como las suspensiones médicas emitidas por el Instituto, se calculará proporcionalmente al tiempo trabajado y en el caso de los patronos referidos en los Artículos 88 y 100 de la Constitución Política de la República de Guatemala, se respetará su calidad de exentos." | The minimum monthly contribution BASE is a FLOOR: independent of contract type, relation, jornada, days worked or geography; it applies ONLY when a worker earns a salary BELOW the base, and the PATRONO pays the difference between the minimum monthly contribution and the sum of the worker+employer contributions computed on the earned salary (the base AMOUNT is not printed — GOQ-04); when the relation starts/ends other than the first/last day of the calendar month, and for IGSS-issued medical suspensions, computation is PROPORTIONAL to time worked; patrons covered by CPR arts. 88/100 keep their exempt status | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | p.7, num. 1 ¶2-3 (EVID-312) |
| LB-013 | 08-SGF/2026 §VI numerales 2-4: "La generación, transmisión y validación de la Planilla de Seguridad Social en forma electrónica, es el mecanismo para que los patronos declaren ante la seguridad social, a sus trabajadores y salarios devengados por estos; asimismo, constituye la base para el pago de las contribuciones y la acreditación de derechos de los afiliados y beneficiarios para obtener las prestaciones reglamentarias." / rectificación: "El patrono podrá solicitar rectificación, complementos y cambios de estado de Planillas de Seguridad Social por diferencia de salarios, incluir trabajadores que no hayan sido incluidos en la planilla original, cambio de actividad económica, suspensiones no incluidas o mal consignadas, fechas de alta y baja de trabajador, entre otras, esto lo podrá realizar cuando la planilla original se encuentre en estado “pagada”." / "En los casos de rectificaciones y planillas complementarias, el sistema informático correspondiente generará sus respectivos recargos al momento de realizar el procedimiento." | The electronic planilla lifecycle: GENERATION, TRANSMISSION and VALIDATION of the Planilla de Seguridad Social electronically is the mechanism by which employers declare their workers and earned salaries — the base for payment of contributions and accrual of benefit rights; the employer may request rectification, complements and status changes (salary differences, omitted workers, economic-activity change, omitted/misstated suspensions, alta/baja dates) ONLY when the ORIGINAL planilla is in estado "pagada"; on rectifications and complementary planillas the system AUTO-GENERATES the corresponding recargos at procedure time | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.7-8, numerales 2-4 (EVID-313) |
| LB-014 | 08-SGF/2026 §§VI numerales 9-13, 22: banks authorized "para la recepción de pagos de contribuciones patronales, laborales, impuesto IRTRA y tasa INTECAP por medios electrónicos" / formas de pago: "1. Por transferencia de fondos a través de la banca virtual. 2. Efectivo con moneda de curso legal. 3. Cheque de caja o de Gerencia … 4. Cheque de cuenta propia … 5. Tarjeta de crédito." / "se deberá generar el recibo de pago a través del formulario Recibo Electrónico de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa INTECAP o forma vigente que defina la Dirección de Recaudación, por el cálculo del total de salarios reportados en dicha Planilla." / num. 22: "El pago de las cuotas patronales y de trabajadores se realizará únicamente a través del formulario Recibo Electrónico de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa INTECAP, previa generación, transmisión y validación de la Planilla de Seguridad Social por el período correspondiente." / num. 11: late planillas accepted at banks "con el recargo por mora e intereses resarcitorios, cuando corresponda" | Payment plumbing: authorized banks receive employer+worker contributions, the IRTRA impuesto and the INTECAP tasa together; five payment forms (virtual-bank transfer, cash, cashier/manager cheque, own-account cheque, credit card); the payment medium of the electronic planilla is virtual banking, generating the receipt through the single form "Recibo Electrónico de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa INTECAP" computed on the total salaries reported in the planilla — ONE receipt settles IGSS + IRTRA + INTECAP in a single payment event, after generation/transmission/validation; LATE planillas are accepted at the banks WITH mora and resarcitory interest (never refused) | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.9-10, 12, numerales 9-13 y 22 (EVID-314) |
| LB-015 | 08-SGF/2026 numerales 15-17: "El patrono inscrito que tenga varios centros de trabajo, deberá presentar la correspondiente Planilla de Seguridad Social por los trabajadores afectos y no afectos al programa de Invalidez, Vejez y Sobrevivencia y deben generar, transmitir, validar y pagar por medio de una sola Planilla de Seguridad Social en forma electrónica." / "En el caso que un patrono ejecute un contrato de obra pública, privada o de servicios y proceda su inscripción, se deberá generar, transmitir y validar una Planilla de Seguridad Social adicional por cada contrato." / "Si como resultado de la fiscalización se determina que los patronos tienen contratos adjudicados en el sistema GUATECOMPRAS, el Departamento de Cobro Administrativo solicitará a los Inspectores Patronales que realicen la revisión contable…" / inhabilitación: "cuando incumpla en la presentación y/o pago de Planillas de Seguridad Social en forma electrónica, cuando exista nota de cargo y que esta esté firme, cuando haya incumplimiento del pago de dos amortizaciones consecutivas de un reconocimiento de deuda…" | Filing-unit structure: an enrolled employer with several work centers files ONE electronic planilla covering workers AFECTOS AND NO AFECTOS to the IVS program, generated/transmitted/validated/paid as a single planilla; an employer executing a public/private obra or servicios contract generates an ADDITIONAL planilla per contract upon enrollment; GUATECOMPRAS awards discovered in fiscalization trigger a contable review; State-supplier INHABILITACIÓN attaches on planilla non-filing/non-payment, firm notas de cargo, or two missed consecutive RD amortizations | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | p.11, numerales 15-17 (EVID-315) |
| LB-016 | 08-SGF/2026 §VIII numerales 37-38: "Dicha solvencia tendrá vigencia desde su fecha de emisión hasta la próxima fecha límite de pago de la Planilla de Seguridad Social en forma electrónica." / "Cuando exista nota de cargo notificada y esta no se encuentre firme, no será un impedimento para extender la Solvencia Patronal. / No se extenderá solvencia, aunque el patrono tenga suscrito reconocimiento de deuda, en virtud de persistir la deuda con el Instituto." / "Las constancias de patrono inscrito al Seguro Social, se tramitarán y extenderán por el Departamento de Registro de Patronos y Trabajadores … dentro del plazo de diez (10) días hábiles contados a partir de la recepción de la solicitud" | The solvencia (employer clearance) is valid from issuance UNTIL the next planilla payment due date (one contribution period — the fecha límite VALUE is not printed, GOQ-10); a notified-but-not-firm nota de cargo does NOT bar solvencia, but an open reconocimiento de deuda DOES (debt persists); enrollment constancias issue within TEN días hábiles of the request | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.16-17, numerales 37-38 (EVID-316) |
| LB-017 | 08-SGF/2026 §IX numerales 39-45: "efectuarán revisión contable, a cada patrono inscrito según su jurisdicción y capacidad instalada, con el propósito de verificar si los patronos reportan a todos los trabajadores, sus salarios afectos al Régimen de Seguridad Social" / bases for notas de cargo: "b. Por medio de estimación salarial con base en el promedio de salarios reportados en planillas de seguridad social o por otro medio que se considere acorde a la realidad" / "Los salarios establecidos con este procedimiento no podrán ser, menores al salario mínimo mensual establecido en el Acuerdo Gubernativo vigente a la fecha en que se detectaron los hallazgos" / method: "a. En empresas agropecuarias se tomará de base el promedio de salarios reportados por el patrono, en las Planillas de Seguridad Social correspondientes a los últimos doce (12) meses. b. En las demás empresas … últimos seis (6) meses. [c.] Cuando el patrono no tenga ningún pago registrado … la información salarial reportada en el trámite de inscripción patronal" | Contable reviews verify that employers report ALL workers and their salarios afectos; estimated-salary notas de cargo are built on the AVERAGE of salaries reported in planillas (agropecuarias: last 12 months; all other enterprises: last 6 months; no payment history: the enrollment filing's reported salaries); estimated salaries may NEVER fall below the monthly salario mínimo of the AG vigente at the date the findings were detected — the estimate-floor feed consumed from `03_minimum-wage.md` GT-PAY-FR-073 | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.19-22, numerales 39-45 (EVID-317) |
| LB-018 | 08-SGF/2026 numerales 52, 78-79: "Los recargos por mora que genere el atraso del pago correspondiente, se cobrarán a partir del día siguiente en que el patrono debió efectuar el pago de sus cuotas, mismos que se calcularán hasta la fecha en que el patrono haga efectivo el pago." / "el Instituto cobrará al patrono un recargo por mora sobre el importe de las contribuciones adeudadas por cada día de atraso; el que se calculará según lo regulado en el Artículo 38 del Acuerdo 1421 de Junta Directiva." / "La fórmula para calcular los recargos sobre el importe de contribuciones adeudadas es la siguiente: Cuotas IGSS x tasa aplicable x días de atraso/365 días (366 días si el año es bisiesto)." / "debe cobrarse recargo del 5% adicional por gastos administrativos en toda liquidación que origine nota de cargo" | The mora apparatus as printed: recargos run PER DAY from the DAY AFTER the due date until effective payment; the mora formula is Cuotas IGSS × tasa aplicable × días de atraso/365 (366 in leap years) — the tasa aplicable lives in Acuerdo 1421 art. 38 (now in corpus, `87_`/LB-025: the Junta Monetaria's latest maximum simple-annual rate — a floating index whose numeric value stays an external publication); every liquidation originating a nota de cargo carries an additional 5% for gastos administrativos (capped Q3,000 inside the Certificación de Gerencia / reconocimiento de deuda, LB-019/LB-020; source layer = 1421 arts. 22/24, LB-025) | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.23, 39-40, numerales 52, 78-79 (EVID-318) |
| LB-019 | 08-SGF/2026 numerales 51-66: notificación: "La nota de cargo debe ser notificada al patrono dentro de los cinco (5) días hábiles siguientes a la fecha de su aprobación en el sistema vigente, más el término de la distancia" / firmeza: "se le concederá un plazo de quince (15) días hábiles para que efectúe el pago o impugne … si al transcurrir el plazo … el patrono no paga, no suscribe reconocimiento de deuda o no impugna, la nota de cargo quedará firme" / Certificación de Gerencia: "contendrá según el caso, la cuota patronal y laboral, los recargos, intereses correspondientes, más el 5% de recargo adicional por gastos administrativos sobre dichas cuotas, el cual no podrá ser mayor a tres mil quetzales (Q 3,000.00)." / juicio: "iniciar el juicio económico coactivo, dentro del plazo de quince (15) días hábiles contados a partir de la recepción de la Certificación de Gerencia" / impugnación: "dentro de los quince (15) días hábiles posteriores a su notificación" / resolución: "deberá notificarse al patrono dentro de los diez (10) días hábiles posteriores a la fecha de su emisión" / revocatoria: "Si el patrono no presenta el recurso antes indicado en el plazo que estipula la Ley de lo Contencioso Administrativo (5 días), la Resolución quedará firme" | The nota de cargo dispute-clock chain: approval → notification within 5 días hábiles (+ término de la distancia) → pay-or-impugn 15 días hábiles (else FIRME) → Certificación de Gerencia itemizing cuotas, recargos, intereses + the 5% admin surcharge CAPPED AT Q3,000 → juicio económico coactivo within 15 días hábiles of reception; impugnación filed within 15 días hábiles of notification; resolution notified within 10 días hábiles of emission; revocatoria within 5 días (Ley de lo Contencioso Administrativo) else firm | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.22-25, 29-31, numerales 51-66 (EVID-319) |
| LB-020 | 08-SGF/2026 §XIII numerales 67-77: "Incluirá cuotas patronales, laborales, recargos por mora, intereses resarcitorios si los hubiere, gastos administrativos que corresponden al cinco por ciento (5%) de recargo adicional, calculado sobre la totalidad del capital adeudado, el cual no podrá ser mayor a tres mil quetzales (Q 3,000.00)… Los recargos por mora e intereses resarcitorios, no podrán exceder del 100% de las cuotas. El monto total del adeudo será distribuido proporcionalmente en cuotas niveladas mensuales." / "El plazo máximo para suscribir reconocimiento de deuda ante el Instituto será hasta de 60 meses, contados a partir del momento de suscripción, para lo cual se debe hacer efectivo el primer pago el mismo día de su otorgamiento." / "a la falta de pago de dos amortizaciones consecutivas, queda automáticamente, sin necesidad de declaración, vencido el plazo del reconocimiento de deuda" / num. 76: "el patrono [que suscriba reconocimiento de deuda] tendrá que cancelar simultáneamente con la primera cuota de dicho reconocimiento, lo correspondiente al impuesto IRTRA y tasa INTECAP y sus recargos" / num. 77: "El Instituto no podrá mantener simultáneamente más de un reconocimiento de deuda con un solo patrono" | Reconocimiento de deuda (installment agreement): includes both cuota shares, mora recargos, resarcitory interest, the 5% admin surcharge (cap Q3,000) and the Acuerdo 1421 art. 31 c) interest; mora + resarcitory interest TOGETHER may not exceed 100% of the cuotas; the total spreads in level monthly installments over AT MOST 60 months with the FIRST payment due the SAME DAY of signing; two missed consecutive amortizations automatically accelerate the term; the omitted planillas must be generated/transmitted/validated BEFORE signing; IRTRA + INTECAP arrears settle SIMULTANEOUSLY with the first installment; only ONE RD per patrono at a time | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.31-39, numerales 67-77 (EVID-320) |
| LB-021 | 08-SGF/2026 numerales 80-83: extemporánea planillas WITHOUT recargos "a. Cuando exista interrupción de la relación laboral … y estos llegan a un arreglo directo … una vez se solicite dentro del término de seis meses contados a partir de la reanudación de la relación laboral. b. Cuando exista aumento de salario o cualquier remuneración afecta a las contribuciones a la Seguridad Social otorgadas de forma retroactiva, como consecuencia de la negociación colectiva … dentro del término de seis meses … c. Cuando exista orden de Juez competente, que ordene la reinstalación y/o reajuste en el salario devengado … dentro del término de seis meses contados a partir de la reinstalación, salvo que el juez fije un plazo para el efecto. d. Cuando la causa … sea imputable al Instituto." / num. 83: "El patrono tendrá hasta un máximo de cuarenta y cinco (45) días hábiles a partir del día siguiente de la fecha de notificación del oficio antes indicado para la generación, transmisión, validación y pago de las Planillas … por única vez y a solicitud del patrono se podrá ampliar por otro plazo menor o igual" | The ONLY four recargo-waiver cases, each with a SIX-MONTH application window: (a) rehires after an interrupted relation settled by direct arrangement; (b) RETROACTIVE salary increases — "aumento de salario o cualquier remuneración afecta a las contribuciones" — from collective bargaining (retroactive pay IS contribution-bearing); (c) judicial reinstatement/back-pay orders; (d) IGSS-attributable delay; after the authorization oficio is notified, the employer has 45 días hábiles to generate, transmit, validate AND pay, with ONE extension ≤ the original term | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.40-42, numerales 80-83 (EVID-321) |
| LB-022 | 08-SGF/2026 §§XV-XVI numerales 84-95: "el Instituto no efectuará gestiones de cobro ni se emitirán notas de cargo por diferencias a su favor cuando los montos sean iguales o menores a quinientos quetzales (Q 500.00) o que dichos montos provengan de error en el pago de cuotas, recargos e interés siempre que la liquidación corresponda a 12 o más periodos de contribución" / "Se establece un intervalo de tolerancia aceptable entre los montos de las contribuciones obtenidos y plasmados en los documentos de cobro … Dicho intervalo será cerrado y estará delimitado al valor un [sic] más/menos (+/-) 1% del monto total de las Contribuciones de Seguridad Social." / "Cuando sea necesario que el patrono presente Planillas de Seguridad Social por periodos anteriores a la vigencia del Acuerdo 1520 de Junta Directiva, se podrá utilizar el formato de planilla aplicable en dichos periodos" / "No es exigible la presentación de las Planillas de Seguridad Social para los pagos de adeudos anteriores al mes de marzo del año 1977." | Materiality and history: no collection efforts nor notas de cargo for differences ≤ Q500 (error cases require a 12+-period liquidation); notas de cargo ≤ Q500 are annulled; a CLOSED ±1% tolerance interval bounds computed vs printed contribution totals; periods before the Acuerdo 1520 vigencia (= Sep-2022 boundary per the marco-jurídico recital, AG 239-2022) may use the planilla format of those periods; planillas for debts before March-1977 are not demandable | `gt/sources/35_IGSS_Resolucion_08-SGF-2026_recaudacion.pdf` | pp.43-47, numerales 84-95 (EVID-322) |
| LB-023 | `36_` Guía Dirección de Recaudación (undated, unnumbered): copia de recibos "La entrega se realizará en 15 días hábiles." / impugnación: "el patrono cuenta con 15 días hábiles para presentar su Impugnación, según Acuerdo 1,421 de Junta Directiva en su artículo 21." / credit: "Material realizado por el Departamento de Comunicación Social y Relaciones Públicas" | An IGSS outreach slide-deck with NO number and NO date anywhere: its content corroborates 08-SGF/2026 (15-dh impugnación, adding the Acuerdo 1421 art. 21 citation) but its currency cannot be established — CORROBORATION ONLY, never an authority or rate source; cite 08-SGF/2026 / Acuerdo 1421 instead | `gt/sources/36_IGSS_Guia_Direccion_Recaudacion.pdf` | pp.5-7 (EVID-323) |
| LB-024 | AG 229-2014 (34_), scope verdict: "El presente reglamento tiene por objeto regular las condiciones mínimas en salud y seguridad ocupacional con el fin de proteger la vida, seguridad, salud e integridad de todos los trabajadores que se encuentran en un lugar de trabajo…" / Art. 552: "Toda violación a cualquier disposición preceptiva o prohibitiva … da lugar a la imposición de una sanción según lo establecido en los artículos 271 y 272 del Código de Trabajo." | AG 229-2014 (Reglamento de Salud y Seguridad Ocupacional; vigencia 8-Sep-2015, reforms 33-2016/57-2022) is an occupational-safety instrument of ORDEN PÚBLICO with ZERO cuota/recaudación/payroll-money provisions — NEVER a source for IGSS rates (R40); its payroll-touching duties (comité bipartito ≥10 workers, SSO plan 3-year review, medical exams; sanctions via CT arts. 271-272) are owned by `10_sso-provenance.md` | `gt/sources/34_IGSS_Reglamento_SSO_AG_229-2014.pdf` | pp.2-6, arts. 1-3; p.90, arts. 552-559 (EVID-324) |
| LB-025 | JD Acuerdo 1421 + AG 180-2018 (two-instrument file `87_`), identity + arts. 9, 42, 38, 31 c), 40: "INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL / ACUERDO NÚMERO 1421" / "REGLAMENTO SOBRE RECAUDACIÓN DE CONTRIBUCIONES AL RÉGIMEN DE SEGURIDAD SOCIAL" / "Dado en el Salón de Sesiones de la Junta Directiva … a los diecisiete días del mes de mayo del año dos mil dieciocho." / p.11: "ACUERDO GUBERNATIVO MúMERO. 18 0-2 018 [sic — digits damaged; read 180-2018] GUATEMALA, 18 OCT 2018" / Art. 9 (two-column OCR; sentence a marked reconstruction, the day-20 value cleanly printed): "Todo patrono inscrito en el Régimen de Seguridad Social debe entregar al Instituto, bajo su responsabilidad y a más tardar el veinte (20) de cada mes calendario, la Planilla de Seguridad Social, con los soportes respectivos y el monto de las cuotas correspondientes a los salarios pagados dentro del mes calendario anterior, salvo que el Instituto establezca su propio calendario de pagos." / Art. 42: "Cuando el vencimiento de cualquiera de los plazos establecidos en el presente reglamento coincidiere con un día inhábil del Instituto, el mismo se trasladará al primer día hábil siguiente." / Art. 38: "será equivalente a la suma que resulte de aplicar a la contribución adeudada, la última tasa de interés simple máxima anual, determinada por la Junta Monetaria, tomando como base la tasa ponderada bancaria para operaciones activas." / "El recargo a que se refiere este Artículo, debe ser pagado exclusivamente por el patrono … Los recargos por incumplimiento, en ningún caso podrán ser mayores al valor de las contribuciones patronales y de trabajadores que se encuentren en mora" / Art. 31 c): "La tasa de interés que se aplique a la deuda, será igual a la tasa de interés activa promedio ponderado del sistema bancario, de acuerdo a la última publicación del Banco de Guatemala, al día de la firma." / art. 40 [printed "ARTÍCULO 49. [sic]"]: incobrabilidad — prescription appears only as the trigger "a) Judicialmente se declare la prescripción del adeudo" | Acuerdo 1421 = the IGSS Junta Directiva's COLLECTION reglamento (49 arts., 9 chapters; given 17-May-2018 under Ley Orgánica art. 19 a); approved in full by AG 180-2018 of 18-Oct-2018, which repeals AGs 85-2003/17-2007/428-2013; art. 47 repeals JD Acuerdos 1118/1200/1310 — the RECAUDACIÓN line only, not the program rate reglamentos; no DCA date printed — vigencia = day after publication, date open; file name "1421-2018" informal, the acuerdo being "1421"). PLANILLA DUE DATE (art. 9): day 20 of each calendar month for the PRECEDING month's salaries, subject to the printed override "salvo que el Instituto establezca su propio calendario de pagos" + art. 42 inhábil roll-forward. MORA (art. 38): tasa = the Junta Monetaria's latest maximum SIMPLE-annual rate (base = tasa ponderada bancaria activa) — an INDEX-linked rule whose numeric value is an inherently external JM/Banguat publication (never frozen in corpus); patrono-exclusive; general CAP = 100% of the patronal+laboral contributions in mora. RD INTEREST (art. 31 c)): Banguat tasa activa promedio ponderado, latest publication at signing. ART. 40 = INCOBRABILIDAD (Gerente write-off ≤Q1,000 after exhausted efforts; Q500/12-period error rule next door at art. 39) — 1421 contains NO freestanding prescription clock. Art. 1 delegates cuota MONTOS to the PROGRAM reglamentos — NO rates here (GOQ-04 stays open, target refined) | `gt/sources/87_IGSS_Acuerdo_1421-2018.pdf` | pp.1-2 arts. 1-4 (EVID-867/868); p.3 art. 9 (EVID-870); p.7 arts. 31, 38 (EVID-876/878); pp.7-8 arts. 39-40 (EVID-879); pp.8-9 art. 42 (EVID-880); p.9 art. 49 (EVID-881); p.11 AG 180-2018 (EVID-882); full range EVID-866..882 |
| LB-026 | IGSS program-reglamento set, five files `104_`/`105_`/`106_`/`107_`/`108_` (SEM: JD Acuerdo 410 consolidations + reform Acuerdo 1154; IVS: requisitos sheet + IVS-103 form). `104_` art. 6 (as amended by Acuerdo 1154, quoted-reform block): "El derecho al subsidio diario de enfermedad se otorga al trabajador afiliado, siempre que dentro de los seis meses calendario anteriores al mes en que se inicie la incapacidad, haya contribuido en tres períodos o meses de contribución. Para la mujer afiliada se toman en cuenta los períodos o meses de goce del subsidio de maternidad, según el Artículo 26., al efecto del cómputo de esos tres períodos o meses de contribución" ["Artículo 26., al efecto" as printed; `105_` reads "26.. al efecto", sic] — the maternidad-art.-26 credit clause: months of GOCE del subsidio de maternidad COUNT toward the 3 contribution months. `104_` art. 62 (the set's ONLY cuota text) + art. 85: "a) Los patronos particulares y el Estado como patrono, el 4 % del total de salarios de sus trabajadores; b) Los trabajadores, el 2% de su salario; y c) El Estado como tal, el 1%, del total de salarios de los trabajadores de patronos particulares y de sus propios trabajadores." / "Artículo 85.- Las tasas de contribución contenidas en el artículo 62 del presente Reglamento, son tasas establecidas para la aplicación de la Protección Relativa a Enfermedad y Maternidad en el departamento de Guatemala, exclusivamente." — the 1964 ORIGINALS (4%/2%/1% = 7% total) valid ONLY for the departamento de Guatemala and historically superseded/extended by the unprinted footnote-21/23 chain of JD acuerdos 475→616→621→849→1024→1095→1121→1243 (the 2011 print `106_` reads 3%/2%/1%; SEM + Accidentes pool into a fondo común). `107_` requisitos sheet (pensión de sobrevivencia): "(Artículo 22 y 23 del Acuerdo 1124 de Junta Directiva)" — the citation that NAMES the IVS program reglamento | (i) the SEM program reglamento (the GOQ-04 target file) is IN CORPUS — benefits/qualification mechanics (3/6 enfermedad anchored to the incapacidad month; 84 Bis 4/6 for post-2005 affiliates; quantum 2/3 and 100%; maternidad 30+54=84 días) now PRIMARY — but the set prints ZERO operative cuota rates (only the superseded 1964 4/2/1 Guatemala-only originals — EVID-1155 full-percentage negative scan): GOQ-04's rate hunt REFINES to the IVS program reglamento Acuerdo 1124 (named by `107_`) + the art.-85 extension chain (475→1243); the 12.67/4.83 priors REMAIN REJECTED; (ii) `106_` = 410 consolidation of vintage 24-11-2011 with the 1154 reforms ALREADY integrated (the file label "original" is a MISNOMER — registry corrected; no pre-1154 art. 6 baseline exists in corpus); (iii) IVS survivorship qualification AS PRINTED by the administrative sheet (secondary wording, as-of Aug-2026): enfermedad ≥36 months of IVS contributions within the 6 years before the risk; accidente vigencia laboral at the accident + ≥3 months within the 6 months before the risk; vejez vesting = 60 años cumplidos + 240 meses efectivamente contribuidos (Acuerdo 1124 arts. 22 y 23, cited jointly; art. 24 = the beneficiary gate); (iv) `108_` = IVS-103 "Historial Laboral" SOBREVIVENCIA variant, captured as blank FORM LAYOUT only (patrono-table floor "a partir de marzo de 1977" — never treat as the generic IVS-103) | `gt/sources/104_IGSS_Acuerdo410_SEM_rev2018.pdf` + `gt/sources/105_IGSS_Acuerdo1154_SEM.pdf` + `gt/sources/106_IGSS_Acuerdo410_SEM_original.pdf` + `gt/sources/107_IGSS_IVS_PensionSobrevivencia_2026-08.pdf` + `gt/sources/108_IGSS_IVS103_HistorialLaboral.xlsx` | 104_: p.4 art. 6; pp.23-24 art. 62 + fn. 21/23; p.29 art. 85 · 105_: p.1 art. 1 · 106_: pp.23-24 art. 62; stamp p.29 · 107_: p.1 §1 · 108_: whole sheet (EVID-1132..1176, esp. 1136/1151/1155/1164/1167; EVID-1172..1185) |

Notes (LB-level, not FRs): (i) REJECTED PRIORS (R34/GOQ-04): the
12.67% patronal / 4.83% laboral percentages circulating as IGSS lore are
NOT verifiable anywhere in 33_-36_ (nor in 87_ — Acuerdo 1421 prints no
rate, art. 1 delegating the montos to the program reglamentos) — they are
never encoded, and every cuota rate, the minimum-base AMOUNT, any tope
máximo and the afecto-a-IVS test load exclusively from external JD PROGRAM
reglamento rows (GOQ-04, target re-refined 2026-08-23: SEM set `104_`-`106_`
acquired RATELESS per LB-026 — operative rates → IVS Acuerdo 1124 named by
`107_` + the 410 art.-85 chain 475→1243); the COTIZABLE-COMPONENT LIST,
by contrast, is now anchored in corpus at 1421 art. 4 (LB-025; EVID-868)
— the RATES applying to that base remain external. (ii) The D-295 25/50/25 figures are FINANCING PROPORTIONS of the
total cost of benefits — structural metadata about who finances the regime,
never a cuota-rate split; no payroll percentage may be derived from them.
(iii) The D-295 arts. 52-57 multas (Q1-Q500, 1946 quetzals) are a superseded
sanction envelope — never implemented as operative collection charges (the
recargos/económico-coactivo apparatus governs). (iv) Edition vintage: `33_`
is a Hemeroteca-certified photocopy of degraded 1946 gazette print — quotes
carry `[sic]` tolerance (GOQ-74); `35_` prints no rate anywhere (only the
procedural percentages it owns). Version regime (D15/D16): the dated rows
owned here (vigencia boundaries, cutoffs, clocks) carry valid_from/provenance;
the 08-SGF/2026 switchover row stays undated pending GOQ-75.

## 3. Functional Requirements

### 3.1 Law layer — D-295 architecture (all values external)

- **GT-PAY-FR-153:** The system shall register D-295 as a dated instrument
  row set: given 28-Oct-1946, sanctioned 30-Oct-1946, published in THREE DCA
  installments (31-Oct/1-Nov/4-Nov-1946 — the Hemeroteca-certified-copy
  provenance), vigencia rule "el día de su publicación en el Diario oficial";
  the operative vigencia DATE stays an open configuration slot because the
  installments span three days and the corpus cannot determine which triggers
  (GOQ-74) — no date is asserted, and every D-295-sourced rule resolves its
  instrument through this row set. (LB-001; EVID-301, EVID-308)
- **GT-PAY-FR-154:** The system shall carry the D-295 financing structure as
  STRUCTURE-ONLY metadata: the regime is financed by *triple contribución*
  (cuotas of trabajadores, patronos and the Estado) with the three parts
  contributing to the TOTAL COST of benefits in the proportion 25%
  trabajadores / 50% patronos / 25% Estado — financing proportions of
  aggregate cost, NEVER cuota rates; the *monto de las cuotas* is expressly
  determined by Junta Directiva reglamentos, and no payroll percentage,
  worker/employer split or rate may be derived, implied or seeded from the
  25/50/25 figures. (LB-002; LB-003; EVID-302, EVID-303)
- **GT-PAY-FR-155:** EXTERNAL-PARAMETER MODEL (GOQ-04, this file owns it):
  every IGSS contribution VALUE — cuota rates (worker and employer), the
  minimum monthly contribution-base amount, any tope máximo (none exists in
  corpus — FR-166), the cotizable-salary component list ("remuneración
  afecta" itemization), and the afecto-a-IVS test — shall load exclusively
  from configurable parameter rows (valid_from/valid_to + instrument
  provenance per D15/D16), each flagged GOQ-04 pending acquisition of the JD
  reglamentos (Acuerdo 1118 family / Acuerdo 1421); the 12.67%/4.83% priors
  are rejected (never encoded); these rows are the single feed consumed by
  file 09's estimated worker-share surfaces (GT-TAX-FR-124, GT-TAX-FR-135 —
  cited by id, estimated parameters only, never corpus-sourced values).
  (LB-002; LB-003; LB-011; EVID-302, EVID-303, EVID-311; GOQ-04 → OQ-001)
- **GT-PAY-FR-156:** The system shall enforce the employer-share
  no-deduction invariant as a HARD rule: *las cuotas de los patronos no
  pueden ser deducidas de los salarios de los trabajadores y es nulo ípso
  jure todo acto o convenio en contrario* (employer cuotas may never be
  deducted from worker salaries in any form; every contrary act or agreement
  is null ipso jure) — any salary-rule configuration charging the employer
  IGSS share (or any part of it) to the worker is rejected, and a computed
  invariant check on each payslip blocks posting on violation.
  (LB-002; EVID-302)
- **GT-PAY-FR-157:** The system shall carry the D-295 share-shift cases as
  configuration slots with NO encoded mechanics: for *riesgos profesionales*
  (occupational risks) and workers who earn only the *salario mínimo*, the
  Instituto is empowered to place the TOTALITY of both cuota shares
  exclusively on the patrono — the slot flips the worker-side charge to
  employer-side per the operative reglamento (external, GOQ-04); until that
  instrument is acquired, the slot ships as a flagged config row and no
  default shift is applied. (LB-002; EVID-302; GOQ-04 → OQ-001)
- **GT-PAY-FR-158:** IGSS collection credits shall carry privileged-credit
  metadata: first-class credits (*créditos de primera clase*) with absolute
  preference over any others EXCEPT the debtor's salary credits toward third
  parties (settlement ordering: salary credits > IGSS credit > other
  creditors), and the *certificación de la Gerencia* on sums owed to the
  Institute is a *título ejecutivo* collectible via the económico-coactivo
  procedure for cuotas/contributions — mirrored as enforcement-stage data on
  payables; the Estado's own share is tax-financed (never a payroll
  computation). (LB-004; EVID-304)
- **GT-PAY-FR-159:** The employer's books and planillas shall be maintained
  as the IGSS inspection surface: IGSS inspection may visit workplaces and
  revise *libros de contabilidad, de salarios, planillas, constancias de
  pago y cualesquiera otros documentos*, and inspection actas carry prima
  facie validity unless evident inaccuracy/falsity/partiality is demonstrated
  — the payroll record set (feeding FR-170's planilla and the file-01 salary
  books GT-PAY-FR-017/018) exports consistently for inspection, and the
  contabilidad↔planilla reconciliation discipline of FR-178 exists because
  these actas are prima-facie evidence. (LB-005; EVID-305; cross-ref
  GT-PAY-FR-018)
- **GT-PAY-FR-160:** CITATION GUARD (superseded sanction frame): the D-295
  arts. 52-57 multas envelope — court-imposed fines between Q1 and Q500
  (1946 quetzals, convertible to arrest; doubling on reincidence; joint
  responsible-person + patrono liability) — is recorded as the statutory
  sanction kin and NEVER implemented as an operative collection charge for
  cuotas: the operative teeth are the mora/recargos apparatus (FR-179), the
  nota de cargo chain (FR-180) and económico-coactivo execution (FR-158);
  no 1946-quetzal fine value is ever converted, indexed or posted.
  (LB-006; EVID-306)
- **GT-PAY-FR-161:** IGSS benefit payments to affiliates shall carry
  protection metadata (no payslip computation): money benefits (*prestaciones
  en dinero*) cannot be assigned, compensated, encumbered or attached EXCEPT
  up to one half for *alimentos* (alimony — feeding the file-01
  GT-PAY-FR-011 garnishment ladder on the benefit side), and the CLAIM-side
  prescription clocks are one year to claim a pension grant and six months
  to collect granted pensions/indemnizations — these are benefit-claim
  clocks ONLY; and NO employer-contribution-side prescription clock is
  asserted anywhere in the corpus: Acuerdo 1421's art. 40 [printed
  "ARTÍCULO 49", sic] is INCOBRABILIDAD, not prescription (LB-025;
  EVID-879) — the Gerente's write-off power (≤Q1,000 after exhausted
  collection/localization efforts; beyond that only on a JUDICIALLY
  DECLARED prescription, concurso/quiebra, deceased/absent-declared
  patrons or dissolved legal persons, revivable if assets appear), so
  prescription appears in 1421 only as a judicial trigger, never as a
  freestanding period; no prescription period is invented or defaulted.
  (LB-007; LB-025; EVID-307, EVID-879)
- **GT-PAY-FR-162:** NEGATIVE FR (R39): D-11-2004 is a GOVERNANCE-ONLY
  reform — it touches solely D-295 arts. 16 a)/d) and 18 (Junta Directiva
  appoints and may freely remove the Gerencia; vigencia 8-May-2004 computed)
  and has ZERO effect on cuotas, recaudación or payroll: no requirement of
  this wave may cite D-11-2004 as a contribution/recaudación authority, and
  the file label "D295_D11-2004" resolves to base law + governance reform
  only. (LB-008; EVID-308)
- **GT-PAY-FR-163:** The IM/IVS program split shall be carried as a
  reglamento-layer routing dimension: D-295 art. 28 fixes the risk catalog
  (accidents/professional illness, maternity, general illness, invalidez,
  orfandad, viudedad, vejez, muerte, plus whatever the reglamentos
  determine) and art. 32 the pension character of the I-V-S protections —
  the modern program universe (IM vs IVS, "Invalidez, Vejez y Sobrevivencia"
  as named in 08-SGF/2026) and the *afecto/no afecto a IVS* test are
  reglamento-built and EXTERNAL (GOQ-04); the system stamps each worker's
  IVS-afecto flag from configuration and reports afectos and no afectos
  together per FR-172. (LB-009; LB-015; EVID-309, EVID-315; GOQ-04 → OQ-001)

### 3.2 Contribution mechanics — 08-SGF/2026 §V (rates external)

- **GT-PAY-FR-164:** The patrono shall be modeled as the IGSS collection
  agent delivering BOTH shares wholesale: the system computes and withholds
  the worker share (*contribución laboral*) and the employer share
  (*contribución patronal*) over the salaries paid, and delivers both to the
  Institute through the planilla cycle (FR-170) — the withholding obligation
  covers *trabajadores permanentes, temporales y a tiempo parcial* (permanent,
  temporary and part-time workers) alike, and the Estado contributes as
  patrono and as such (never a payroll charge); the worker share posts as a
  payslip deduction and the employer share as employer cost, both computed
  exclusively from the FR-155 external parameter rows.
  (LB-011; EVID-311)
- **GT-PAY-FR-165:** The system shall implement the minimum monthly
  contribution base as a FLOOR: the base amount is independent of contract
  type, labor relation, effective jornada, days worked in the period or
  economic/geographic circumscription, and applies ONLY when a worker earns
  a salary below it — in which case the PATRONO is responsible for paying
  the difference between the minimum monthly contribution and the sum of the
  worker+employer contributions computed on the earned salary (employer
  top-up posting, not a worker deduction); the base AMOUNT itself is an
  external parameter row (GOQ-04, FR-155) — never a printed constant — and
  its kinship to the salario mínimo floor concept is consumed from
  `03_minimum-wage.md` GT-PAY-FR-073 (by id; the AG-vigente as-of resolution
  is owned there). (LB-012; EVID-312; cross-ref GT-PAY-FR-073)
- **GT-PAY-FR-166:** NEGATIVE FR (no tope máximo): NO contribution-base
  ceiling exists anywhere in the corpus — the system shall never assert,
  derive, encode or imply any tope máximo, capital máximo or capping
  arithmetic on IGSS contribution bases; the only printed base rule is the
  FLOOR of FR-165 (EVID-312), and a ceiling may enter ONLY as an explicit
  external parameter row when a JD reglamento supplies one (GOQ-04) — until
  then the base builder applies floor logic and no cap logic, and any
  configuration proposing a ceiling without an instrument row is rejected.
  (LB-011; LB-012; EVID-311, EVID-312; GOQ-04 → OQ-001)
- **GT-PAY-FR-167:** The system shall prorate the monthly contribution
  computation *proporcionalmente al tiempo trabajado* when the labor
  relation starts or ends on any day other than the first or last day of
  the calendar month or period, and equally for *suspensiones médicas
  emitidas por el Instituto* (IGSS-issued medical suspensions) — the same
  proration engine serving both mid-month alta/baja and IGSS medical
  suspensions; the maternity IGSS-coverage branch that suppresses the
  employer salary line is owned by `05_vacaciones-maternidad.md`
  GT-PAY-FR-116 (consumed by id; this file owns only the suspension-proration
  mechanic printed at LB-012). (LB-012; EVID-312; cross-ref GT-PAY-FR-116)
- **GT-PAY-FR-168:** Patrons covered by arts. 88 and 100 of the Constitución
  Política de la República de Guatemala shall keep their *calidad de
  exentos* (exempt status) — carried as an employer-level constitutional
  exemption flag that suppresses the IGSS contribution postings for the
  exempt patron; the IDENTIFICATION of which patrons arts. 88/100 exempt is
  constitutional text outside this corpus (never asserted here) — the flag
  loads from employer configuration, and no exempting test is invented.
  (LB-012; EVID-312)
- **GT-PAY-FR-169:** The cotizable-component surface shall be
  anchored at Acuerdo 1421 art. 4 (LB-025; EVID-868 — the REGLAMENTO-layer
  itemization the anchor phrases lacked): the cuotas compute over the
  *salario total del trabajador*, comprising the *devengado durante las
  jornadas ordinarias, extraordinarias y bonificaciones excepto aquellas
  cuyas leyes de creación las excluyan*, and EXPRESSLY EXCLUDING the
  termination-pay *indemnización*, *compensación de vacaciones en dinero*,
  *el aguinaldo* (excluding creation law = D-76-78 art. 15, EVID-862) and
  employer complements to IGSS-recognized temporary-incapacity subsidies;
  the operative salary concepts remain the printed anchor phrases — "los
  salarios que paguen los patronos", "salarios afectos al Régimen de
  Seguridad Social", "aumento de salario o cualquier remuneración afecta a
  las contribuciones a la Seguridad Social" — now itemized at reglamento
  layer as above; earning-category inclusion flags load that anchored list
  (the RATES applying to the base remain external program-reglamento rows,
  FR-155/GOQ-04), with two corpus-pinned
  consumption rules: RETROACTIVE pay IS contribution-bearing (LB-021 —
  retroactive increases enter the period-specific planilla, never a
  non-contributory lump), and the *bonificación incentivo* is non-contributory
  UNLESS a recorded joint patrono+trabajador agreement exists (consumed by
  id from `04_statutory-bonuses.md` GT-PAY-FR-091 — the aguinaldo, by
  contrast, is excluded UNCONDITIONALLY, no joint-agreement opt-in).
  (LB-011; LB-021; LB-025; EVID-311, EVID-321, EVID-868; cross-ref
  GT-PAY-FR-091, GT-PAY-FR-095)

### 3.3 Planilla Electrónica — lifecycle, filing unit and payment

- **GT-PAY-FR-170:** The system shall implement the Planilla de Seguridad
  Social electrónica as a four-state lifecycle — GENERAR (generate: employer
  assembles workers + salarios devengados from payroll data), TRANSMITIR
  (transmit to IGSS), VALIDAR (IGSS validation) and PAGAR (pay) — where
  generation/transmission/validation is THE mechanism by which patrons
  declare their workers and earned salaries to social security, the base for
  contribution payment and the accrual of benefit rights: odoo assembles the
  declaration data (per-worker lines with the FR-155-configured bases and
  both shares) while the ingestion/transmission services live in the saas
  core; the file formats and standards are "establecidos por el Instituto"
  and absent from the corpus — no layout is invented. This file owns the
  planilla MECHANICS for the CT art. 102 3-9-worker mode selected by
  `01_ct-salary-model.md` GT-PAY-FR-018 (by id); the completed PAGAR state
  is the employer-side evidence surface consumed by GT-TAX-FR-146 (art. 23.f:
  salaries off the IGSS planilla are non-deductible — feed only, never
  re-derived). (LB-013; EVID-313; cross-ref GT-PAY-FR-018, GT-TAX-FR-146)
- **GT-PAY-FR-171:** Rectificación and complemento shall be gated on the
  pago state: the patrono may request rectification, complements and estado
  changes — salary differences, workers omitted from the original planilla,
  economic-activity change, omitted or misstated suspensions, alta/baja
  dates — ONLY when the original planilla is in estado "pagada"; when a
  rectification or complementary planilla processes, the system
  AUTO-GENERATES its recargos at procedure time (mora engine FR-179), and no
  amendment path exists against a planilla still in generada/transmitida/
  validada states. (LB-013; EVID-313)
- **GT-PAY-FR-172:** The filing unit shall be the registro patronal: an
  enrolled patrono with several *centros de trabajo* (work centers) files
  ONE electronic planilla — generate, transmit, validate AND pay through a
  single Planilla de Seguridad Social — covering the workers AFECTOS Y NO
  AFECTOS to the IVS program TOGETHER (the afecto flag of FR-163 is a
  reported attribute, never a filing splitter). (LB-015; EVID-315)
- **GT-PAY-FR-173:** An employer executing a *contrato de obra pública,
  privada o de servicios* (public/private works or services contract), upon
  enrollment, shall generate, transmit and validate an ADDITIONAL Planilla
  de Seguridad Social per contract — one per-obra planilla parallel to the
  registro-patronal planilla of FR-172, each with its own lifecycle and
  payment. (LB-015; EVID-315)
- **GT-PAY-FR-174:** Payment integration shall settle IGSS + IRTRA + INTECAP
  in ONE event: the payment medium of the electronic planilla is virtual
  banking, and the receipt generates through the single form *Recibo
  Electrónico de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa
  INTECAP* computed on the total salaries reported in the planilla — one
  receipt, one payment event covering the IGSS patronal+laboral cuotas, the
  IRTRA impuesto and the INTECAP tasa (whose VALUES are owned by
  `08_irtra-intecap.md` — never printed here); payment is possible only
  after generación/transmisión/validación of the period's planilla, through
  the authorized channels (virtual-bank transfer, cash in legal currency,
  cashier/manager cheque, own-account cheque, credit card) at
  IGSS-authorized banks, which also receive notas de cargo, reconocimientos
  de deuda and certificaciones de gerencia with prior recargo computation.
  (LB-014; EVID-314)
- **GT-PAY-FR-175:** Late planillas shall be ACCEPTED with mora, never
  refused: planillas paid after the reglamentario plazo are received at the
  banks *con el recargo por mora e intereses resarcitorios, cuando
  corresponda* (the FR-179 mora engine; the waiver cases of FR-182) — the
  payment channel keeps accepting the obligation and the system's exposure
  record distinguishes on-time vs late payment, never blocking transmission
  of the late filing. (LB-014; EVID-314)
- **GT-PAY-FR-176:** The *solvencia patronal* shall carry a dynamic validity
  window: valid from issuance until the NEXT fecha límite de pago of the
  electronic planilla (one contribution period); a notified nota de cargo
  not yet firme does NOT bar solvencia, while an open reconocimiento de
  deuda DOES (debt persists); enrollment *constancias* (patrono inscrito)
  issue within TEN días hábiles of the request — surfaced as compliance
  watchdates; the fecha límite VALUE feeding the window is the FR-177
  due-date row (day 20, with its IGSS-calendario override slot; LB-025).
  (LB-016; LB-025; EVID-316)
- **GT-PAY-FR-177:** The planilla due date (*fecha límite de pago* /
  reglamentario plazo) is ANCHORED at Acuerdo 1421 art. 9 (GOQ-10 IGSS
  half RESOLVED — `87_`/LB-025; EVID-870): every enrolled patrono must
  deliver the Planilla de Seguridad Social with its soportes and cuotas
  *a más tardar el veinte (20) de cada mes calendario* — day 20 of each
  calendar month — covering the cuotas on salaries paid *dentro del mes
  calendario anterior* (the PRECEDING calendar month), subject to the
  printed override *"salvo que el Instituto establezca su propio
  calendario de pagos"* (an IGSS-set payment calendar may supersede —
  the override slot loads from configuration and the 08-SGF/2026
  procedural layer may BE that calendar; verification slot open, evidence
  OQ 87_-4); art. 42 rolls a deadline falling on an IGSS inhábil day to
  the first hábil day following (EVID-880); art. 9's full sentence is a
  marked OCR reconstruction (the day-20 value itself is cleanly printed —
  verify the joined text in a clean print before freezing the verbatim
  citation, evidence OQ 87_-1) and no day other than 20 is invented or
  defaulted; every downstream clock — mora from the day after
  (FR-179), solvencia until the next due date (FR-176) — resolves
  through this day-20 row as dated configuration with its override slot.
  (LB-025; LB-016; EVID-870, EVID-880; GOQ-10 → OQ-004)

### 3.4 Audit, mora, enforcement clocks, RD, waivers, materiality

- **GT-PAY-FR-178:** The system shall maintain the contable-review
  reconciliation surface and the salary-estimation engine: IGSS revisiones
  contables verify that patrons report ALL workers and their salarios
  afectos — so reported salaries must equal contabilidad salaries (the
  FR-159 inspection surface); when a nota de cargo rests on salary
  estimation, the estimate averages the salaries reported in the planillas
  (agropecuaria enterprises: last TWELVE months; all other enterprises: last
  SIX months; no payment history: the enrollment filing's reported
  salaries), and estimated salaries may NEVER fall below the monthly
  *salario mínimo* of the AG vigente at the date the findings were detected
  — the dated AG row consumed by id from `03_minimum-wage.md` GT-PAY-FR-073;
  GUATECOMPRAS-awarded patrons discovered in fiscalization route to the
  contable review queue, and the State-supplier inhabilitación triggers
  (planilla non-filing/non-payment; firm nota de cargo; two missed
  consecutive RD amortizations) surface as compliance flags.
  (LB-015; LB-017; EVID-315, EVID-317; cross-ref GT-PAY-FR-073)
- **GT-PAY-FR-179:** The mora engine shall run per-day from the DAY AFTER
  the due date (FR-177 row) until the date the patrono makes payment
  effective, computed as *Cuotas IGSS × tasa aplicable × días de atraso/365
  días (366 días si el año es bisiesto)* — the formula SHAPE and day-after
  start are printed and owned here, while the *tasa aplicable* RULE is
  anchored at Acuerdo 1421 art. 38 (GOQ-10 mora half RESOLVED — `87_`/
  LB-025; EVID-878): the recargo equals *la última tasa de interés simple
  máxima anual, determinada por la Junta Monetaria, tomando como base la
  tasa ponderada bancaria para operaciones activas* — an INDEX-LINKED
  parameter whose periodic numeric value is an inherently external Junta
  Monetaria/Banguat publication (a runtime index feed, never a constant
  frozen in corpus; the config row keeps its dated-value discipline and no
  figure is hard-coded); the mora is the PATRONO's exclusive obligation
  (never deducted from or charged to workers) and the recargos may NEVER
  exceed the value of the patronal + laboral contributions in mora (art.
  38's GENERAL 100% cap — broader than the RD-scoped cap of FR-181); the
  two layers COMPOSE: formula shape + day-after start (`35_`, LB-018) +
  tasa index + cap (1421, LB-025) — composition, not duplication. Every
  liquidation originating a nota de cargo additionally carries the 5%
  *gastos administrativos* surcharge, capped at Q3,000 inside the
  Certificación de Gerencia and the reconocimiento de deuda (procedural
  value printed at `35_` LB-019/LB-020; SOURCE layer = 1421 arts. 22/24,
  LB-025, EVID-874 — primary anchor annotated; computation in the saas
  core, exposure and payment surfaces in odoo); the resarcitory-interest
  leg applies only to expedientes opened during Acuerdo 1087's vigencia
  (flagged, formula external). (LB-018; LB-019; LB-020; LB-025;
  EVID-318, EVID-319, EVID-320, EVID-874, EVID-878; GOQ-10 → OQ-004)
- **GT-PAY-FR-180:** The nota de cargo lifecycle shall carry the printed
  dispute-clock chain as staged case data (clocks computed in saas, surfaced
  as odoo compliance alerts; the procedural acts are IGSS's, only mirrored):
  notification within 5 días hábiles of system approval (+ término de la
  distancia) → pay-or-impugn window of 15 días hábiles (non-payment, no RD
  subscription and no impugnación make the nota FIRME) → Certificación de
  Gerencia itemizing cuota patronal y laboral, recargos, intereses + the 5%
  admin surcharge (cap Q3,000) → juicio económico coactivo initiated within
  15 días hábiles of the certification's reception; an impugnación filed
  within 15 días hábiles of notification delays, with resolution notified
  within 10 días hábiles of emission and revocatoria (Ley de lo Contencioso
  Administrativo) within 5 días else firm. (LB-019; EVID-319)
- **GT-PAY-FR-181:** The *reconocimiento de deuda* (RD) shall implement:
  contents = cuotas patronales y laborales + mora recargos + resarcitory
  interest (if any) + the 5% admin surcharge on the totality of the capital
  owed (cap Q3,000) + the Acuerdo 1421 art. 31 c) interest — RULE now
  anchored (`87_`/LB-025; EVID-876): *la tasa de interés activa promedio
  ponderado del sistema bancario, de acuerdo a la última publicación del
  Banco de Guatemala, al día de la firma* (Banguat's latest publication as
  of the signing day — an index-linked rule whose numeric value stays an
  inherently external floating publication, never frozen in corpus); the mora + resarcitory-interest stack may NEVER exceed 100% of
  the cuotas; the total distributes in level monthly installments over AT
  MOST 60 months with the FIRST payment effective the SAME DAY of signing;
  TWO missed consecutive amortizations automatically accelerate the term
  (no declaration needed); the omitted planillas must be
  generated/transmitted/validated BEFORE signing (pre-condition); IRTRA and
  INTECAP arrears settle SIMULTANEOUSLY with the first installment (their
  values owned by `08_irtra-intecap.md`); and the Institute maintains at
  most ONE RD per patrono — a second request while one is open is rejected.
  (LB-020; LB-025; EVID-320, EVID-876)
- **GT-PAY-FR-182:** The recargo-waiver workflow shall implement the ONLY
  FOUR cases in which extemporánea planillas process WITHOUT reglamentary
  recargos, each with its SIX-MONTH application window running from the
  stated anchor: (a) rehires after an interrupted labor relation settled by
  *arreglo directo* (window from relation resumption); (b) retroactive
  salary increases — any *remuneración afecta a las contribuciones* granted
  retroactively through collective bargaining (window from the increase
  grant; the retroactive pay enters the period-specific planillas as
  contribution-bearing complements, per FR-169); (c) judicial
  reinstatement/reajuste orders (window from reinstatement, unless the judge
  fixes another term); (d) IGSS-attributable cause (no window cap printed —
  as-extract); after the authorization oficio notifies, the employer has 45
  días hábiles from the next day to generate, transmit, validate AND pay,
  with ONE extension ≤ the original term granted at the patrono's request.
  (LB-021; EVID-321)
- **GT-PAY-FR-183:** Materiality and historical-cutoff ledger: no collection
  efforts and no notas de cargo issue for differences in the Institute's
  favor ≤ Q500 (error-derived differences additionally require a
  12-or-more-period liquidation) and existing ≤Q500 notas de cargo are
  annulled; a CLOSED ±1% tolerance interval bounds the acceptable spread
  between computed and printed contribution totals (rounding policy, never
  a rate statement); planillas for periods before the Acuerdo 1520 vigencia
  boundary (Sep-2022 per the AG 239-2022 recital) may use those periods'
  planilla format (dated format-boundary row); and planillas for debts
  earlier than March-1977 are not demandable (exigibility cutoff row).
  (LB-022; EVID-322)
- **GT-PAY-FR-184:** CORROBORATION GUARDS (citation hygiene): the `36_`
  Guía Dirección de Recaudación is an undated, unnumbered IGSS outreach
  document — its content may CORROBORATE 08-SGF/2026 mechanics (e.g. the
  15-días-hábiles impugnación, adding Acuerdo 1421 art. 21) but is NEVER an
  authority, deadline source or rate source (cite 08-SGF/2026 / Acuerdo 1421
  instead); and AG 229-2014 (34_) is an occupational-safety reglamento with
  ZERO cuota/recaudación/payroll-money content — never a source for IGSS
  rates (R40; its SSO duties are owned by `10_sso-provenance.md`). Both
  guards ride the shared citation-hygiene catalog so neither side of the
  architecture resolves a rule to the wrong instrument.
  (LB-023; LB-024; EVID-323, EVID-324)

## 4. Data Model

Layer semantics: payroll computation and record surfaces are Odoo-native;
the planilla lifecycle state machine, payment integration and the
mora/RD/nota-de-cargo clocks are `saas` ingestion/transmission/computation
services with `odoo` data assembly and surfaces; every external rate/base/
tope/component parameter is a `shared` config row (GOQ-04) both sides
resolve identically. No dated VALUE owned by this file is a rate: the only
dated data are the instrument/vigencia rows, the printed procedural clocks
and the cutoff ledger.

**External parameter feed (GOQ-04 — the single IGSS value source):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.igss.parameter (new) | row_type | select | cuota_rate_worker · cuota_rate_employer · base_floor_amount · base_ceiling (EMPTY — FR-166) · cotizable_component (anchored list, 1421 art. 4 — LB-025) · ivs_afecto_test · mora_tasa (anchored index rule, 1421 art. 38) · rd_interes (anchored index rule, 1421 art. 31 c) · planilla_due_date (anchored day-20 rule + override slot, 1421 art. 9) | FR-155, FR-165, FR-166, FR-169, FR-179, FR-181, FR-177 |
| l10n_gt.pay.igss.parameter | value_pct · value_amount · component_ref | float/monetary/char | rate/base/tope rows ALL EMPTY at seed — GOQ-04 pending the JD PROGRAM reglamentos (1421 prints no rates, art. 1 delegating — LB-025); the 12.67/4.83 priors are rejected and never seeded; the mora_tasa/rd_interes rows carry the anchored INDEX RULES whose numeric values are inherently external JM/Banguat floating publications (dated-row discipline, never frozen); the planilla_due_date row seeds the art.-9 day-20 rule with the "propio calendario" override slot | FR-155, FR-177, FR-179, FR-181 |
| l10n_gt.pay.igss.parameter | valid_from · valid_to · provenance | date/date/char | D15/D16 regime; provenance = the JD PROGRAM reglamento (Acuerdo 1118 family; 1421 delegates montos — LB-025) once acquired | FR-155 |

**Contribution mechanics:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip.line (IGSS) | gt_pay_igss_share | select | laboral (worker deduction) · patronal (employer cost) | FR-164 |
| hr.payslip (IGSS base) | gt_pay_igss_base | monetary (computed) | from cotizable_component flags (FR-169); floor per FR-165; NO ceiling computation exists (FR-166) | FR-164..166 |
| hr.payslip (top-up) | gt_pay_igss_floor_topup | monetary (computed) | employer pays diferencia when salary < base_floor_amount row | FR-165 |
| hr.payslip (proration) | gt_pay_igss_proration_days | integer/float | mid-month alta/baja + IGSS medical suspensions → proportional computation | FR-167 |
| res.company / hr.employee (patrono) | gt_pay_igss_exempt_cpr88_100 | boolean | constitutional exemption flag; identification external (CPR text not in corpus) | FR-168 |
| hr.contract (share shift) | gt_pay_igss_share_shift | select | none · riesgos_profesionales · salario_minimo (D-295 art. 39 slots; operative detail GOQ-04) | FR-157 |
| salary-rule guard | employer-share no-deduction invariant | constraint | any rule charging cuota patronal to the worker → reject + payslip block | FR-156 |
| account.move.line (IGSS payable) | gt_pay_igss_first_class | tag | first-class credit; subordinated only to salary credits; certificación = título ejecutivo (económico-coactivo stage char) | FR-158 |

**Planilla lifecycle — l10n_gt.pay.igss.planilla (new) + lines:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.igss.planilla (new) | registro_patronal · period · scope | m2o · char (M/YYYY) · select | scope: regular (one per patrono, FR-172) · obra_servicios (per contract, FR-173) | FR-170, FR-172, FR-173 |
| l10n_gt.pay.igss.planilla | state | select | generada · transmitida · validada · pagada (+ rectificada/complementaria linkage) | FR-170, FR-171 |
| l10n_gt.pay.igss.planilla.line | worker · ivs_afecto · base · share_laboral · share_patronal | m2o · boolean (config FR-163) · monetary | afectos y no afectos reported together in one planilla; values from FR-155 rows — never recomputed elsewhere | FR-163, FR-172 |
| l10n_gt.pay.igss.rectificacion (new) | original_planilla · reason · recargos_generated | m2o (state=pagada) · select · monetary (auto) | reasons: diferencia_salarios · trabajador_omitido · actividad_economica · suspensiones · fechas_alta_baja · otros | FR-171 |
| l10n_gt.pay.igss.payment (new) | receipt_form · channel · covers | char · select · tags | receipt = Recibo Electrónico (IGSS+IRTRA+INTECAP single event); channel: banca_virtual · efectivo · cheque_caja_gerencia · cheque_cuenta_propia · tarjeta_credito; covers: igss · irtra · intecap (values from 08) | FR-174, FR-175 |
| l10n_gt.pay.igss.solvencia (new) | issued_at · valid_until · barred_by_rd | date · date (computed) · boolean | valid_until = next planilla due date (FR-177 row); constancia watchdate 10 dh | FR-176 |

**Enforcement — mora, nota de cargo, RD, waivers, audit:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.igss.mora (new) | due_row · days_late · formula · tasa_row · amount | m2o (FR-177) · int · char (Cuotas × tasa × días/365(366)) · m2o (art. 38 index row — LB-025) · monetary | day-after-due accrual to effective payment; patrono-exclusive; general 100% mora cap (art. 38); +5% admin (cap Q3,000, source 1421 arts. 22/24) on nota-de-cargo liquidations | FR-179 |
| l10n_gt.pay.igss.nota.cargo (new) | stage · clocks | select · dates (computed) | aprobada → notificada (5 dh + distancia) → pago/impugnación (15 dh) → firme → certificación → económico_coactivo (15 dh); impugnación 15 dh; resolución 10 dh; revocatoria 5 días | FR-180 |
| l10n_gt.pay.igss.rd (new) | months_max · first_payment_same_day · missed_acceleration · cap_100 · irtra_intecap_first_cuota | 60 · boolean · 2-consecutive trigger · mora+interés ≤ 100% cuotas · boolean | one RD per patrono (unique constraint); pre-condition: omitted planillas filed | FR-181 |
| l10n_gt.pay.igss.waiver (new) | case · window · execution | select a-d · 6 meses anchors · 45 dh + one extension | (a) arreglo directo (b) retroactive collective raise (c) judicial reinstatement (d) IGSS-attributable | FR-182 |
| l10n_gt.pay.igss.audit (new) | estimate_base · averaging · floor_row | select · 12m agro / 6m others / enrollment · salario mínimo AG vigente (GT-PAY-FR-073 feed) | GUATECOMPRAS flag; inhabilitación triggers | FR-178 |
| l10n_gt.pay.igss.materiality (new) | q500_minimum · tolerance · cutoffs | Q500 · closed ±1% · Mar-1977 exigibility / Sep-2022 format boundary | printed values owned here | FR-183 |
| l10n_gt.pay.igss.guard (new) | negative rows | char | 36_ = corroboration_only; AG 229-2014 = NOT a rate source (R40); D-11-2004 = governance-only (R39); D-295 multas Q1-500 = superseded; NO tope máximo in corpus | FR-160, FR-162, FR-166, FR-184 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface; `saas` = authoritative
computation/validation and the ingestion/transmission services; `shared` =
contract items both sides resolve identically. Payroll-wave bindings for
this file: planilla lifecycle + payment integration = `saas`
ingestion/transmission with `odoo` data assembly; mora/RD/nota-de-cargo
clocks = `saas` with `odoo` surfaces; external-rate parameters = `shared`
config rows (GOQ-04). Model names stable across Odoo 17/18/19/20; no
version-specific behavior required.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-153 | shared | — (instrument registry §4) | D-295 dated rows | GOQ-74: vigencia installment question open; no date asserted |
| FR-154 | shared | — (metadata §4) | 25/50/25 financing proportions | Structure-only; never cuota rates; no payroll percentage derived |
| FR-155 | shared | — (l10n_gt.pay.igss.parameter rows) | GOQ-04 external feed | ALL rate/base/tope/component rows; feeds file 09 GT-TAX-FR-124/135 as estimates |
| FR-156 | odoo | salary-rule constraint + payslip check | nulo ipso jure invariant | Blocks posting on employer-share pass-through |
| FR-157 | odoo | hr.contract | gt_pay_igss_share_shift slots | Riesgos/mínimo-earner shift; operative detail GOQ-04 |
| FR-158 | shared | — (metadata §4) | first-class tag + título ejecutivo | Settlement ordering: salary > IGSS > others |
| FR-159 | odoo | inspection export surface | libros/planillas export | Prima-facie actas discipline; feeds FR-178 reconciliation |
| FR-160 | shared | — (guard rows §4) | D-295 multas superseded | Never operative collection charges; no Q-value converted |
| FR-161 | shared | — (metadata §4) | benefit inembargabilidad + claim clocks | 50% alimony exception; 1y/6m claim-side only; 1421 art. 40 = incobrabilidad, no prescription clock (LB-025) |
| FR-162 | shared | — (guard rows §4) | D-11-2004 governance-only | R39 negative; zero cuota effect |
| FR-163 | odoo | hr.employee / planilla.line | ivs_afecto flag | Test external GOQ-04; afectos + no afectos reported together |
| FR-164 | odoo | hr.payslip.line (IGSS rules) | laboral/patronal legs | Both shares delivered by patrono; permanent/temporary/part-time |
| FR-165 | odoo | hr.payslip | floor + employer top-up | base_floor_amount = shared row (FR-155); kin feed GT-PAY-FR-073 |
| FR-166 | shared | — (guard + empty ceiling slot) | NO tope máximo | Negative FR; ceiling only via explicit instrument row |
| FR-167 | odoo | hr.payslip (computation) | proration engine | Mid-month alta/baja + IGSS medical suspensions; maternity branch = GT-PAY-FR-116 |
| FR-168 | odoo | res.company / hr.employee | cpr_88_100 exempt flag | Identification external (constitutional text not in corpus) |
| FR-169 | odoo | payslip-line inclusion flags | cotizable components | List anchored at 1421 art. 4 (LB-025); rates still GOQ-04; retro pay IN (LB-021); incentivo OUT unless joint agreement (GT-PAY-FR-091); aguinaldo OUT unconditionally |
| FR-170 | saas + odoo | l10n_gt.pay.igss.planilla | state machine | saas ingestion/transmission; odoo data assembly; formats external; GT-TAX-FR-146 gating feed |
| FR-171 | saas | l10n_gt.pay.igss.rectificacion | estado "pagada" gate | Auto-recargos at procedure time |
| FR-172 | saas + odoo | planilla (scope=regular) | one per registro patronal | Multi-centro single filing; afectos y no afectos together |
| FR-173 | odoo + saas | planilla (scope=obra_servicios) | per-contract extras | One additional planilla per obra/servicios contract |
| FR-174 | saas + odoo | l10n_gt.pay.igss.payment | single receipt event | IGSS+IRTRA+INTECAP one payment; values of IRTRA/INTECAP owned by file 08 |
| FR-175 | saas | payment intake | late accepted + mora | Never refused; exposure record distinguishes on-time/late |
| FR-176 | odoo | l10n_gt.pay.igss.solvencia | dynamic window | Until next fecha límite (FR-177 row); RD bars; constancias 10 dh |
| FR-177 | shared | — (due-date config row) | fecha límite = day 20 | Art. 9 anchored (LB-025) + "propio calendario" override slot; art. 42 inhábil roll-forward |
| FR-178 | saas + odoo | l10n_gt.pay.igss.audit | estimate engine | 12m/6m averaging; floor = AG salario mínimo (GT-PAY-FR-073); GUATECOMPRAS queue |
| FR-179 | saas | l10n_gt.pay.igss.mora | formula + index tasa (art. 38 — LB-025) | Day-after due; Cuotas × tasa × días/365(366); patrono-exclusive; 100% mora cap; +5% cap Q3,000 (source 1421 arts. 22/24); odoo surfaces |
| FR-180 | saas | l10n_gt.pay.igss.nota.cargo | clock chain 5/15/15/5 | Staged case data; impugnación 15 dh; resolución 10 dh; revocatoria 5 días; odoo alerts |
| FR-181 | saas | l10n_gt.pay.igss.rd | ≤60m · same-day · 2-missed · 100% cap | One RD per patrono; IRTRA/INTECAP ride first cuota; odoo surfaces |
| FR-182 | saas | l10n_gt.pay.igss.waiver | 4 cases · 6m windows · 45 dh | Retro pay = contribution-bearing complements; odoo surfaces |
| FR-183 | saas + odoo | l10n_gt.pay.igss.materiality | Q500 · ±1% · cutoffs | Mar-1977 exigibility; Sep-2022 format boundary |
| FR-184 | shared | — (guard rows §4) | corroboration guards | 36_ never authority; AG 229-2014 never a rate source (R40 → file 10) |

Version-regime notes (D15/D16): the dated rows owned here are
instrument/boundary data — the D-295 provenance set (FR-153, GOQ-74 slot),
the 08-SGF/2026 switchover row (undated pending GOQ-75), the Sep-2022
format boundary and Mar-1977 exigibility cutoffs (FR-183) — each with
valid_from/provenance. Every rate/base/tope VALUE row stays an empty
GOQ-04 config row pending the JD PROGRAM reglamentos; the due-date row
now carries the anchored art.-9 rule (day 20 + override slot, LB-025)
and the tasa rows carry anchored INDEX RULES (1421 arts. 38 / 31 c))
whose numeric values are inherently external publications (Junta
Monetaria / Banguat) — dated-row discipline preserved, no figure frozen.

## 6. Acceptance Criteria

- **AC-001:** Given any payslip-run configuration or salary rule that
  charges any part of the *contribución patronal* to a worker's salary,
  when the configuration is validated or the payslip computed, then the
  rule is rejected — and if it reaches a payslip, posting is blocked
  (*nulo ípso jure* invariant). (FR-156)
- **AC-002:** Given an inspection of the IGSS parameter registry, when
  searched for any cuota rate, base-floor amount, tope, cotizable-component
  value or afecto-a-IVS test, then every such row exists only as an EMPTY
  GOQ-04-flagged configuration row — no value row anywhere, and the 12.67%/
  4.83% priors appear nowhere as data (rejected priors). (FR-155)
- **AC-003:** Given any component or computation attempting to derive a
  worker/employer cuota percentage from the D-295 financing proportions
  (25/50/25), when inspected, then no such derivation exists — the
  proportions are stored only as aggregate-financing structure metadata.
  (FR-154)
- **AC-004:** Given a worker earning a monthly salary below the configured
  base-floor row (amount loaded externally, GOQ-04), when the IGSS lines
  compute, then the patrono posts the TOP-UP difference between the minimum
  monthly contribution and the sum of the two shares computed on the earned
  salary — and no worker-side deduction arises from the top-up; given a
  worker earning at or above the floor, then no floor logic applies and NO
  ceiling computation runs (no tope exists). (FR-165, FR-166)
- **AC-005:** Given a worker hired on 10-March (mid-month alta) and another
  whose IGSS medical suspension covers part of a month, when the monthly
  contribution computes, then both prorate *proporcionalmente al tiempo
  trabajado* on the same engine; given a CPR art. 88/100-flagged exempt
  patron, then its workers' IGSS postings are suppressed by the exemption
  flag. (FR-167, FR-168)
- **AC-006:** Given a patrono with three centros de trabajo and 40 workers
  (35 afectos a IVS, 5 no afectos), when the period files, then ONE
  electronic planilla covers all workers of the registro patronal with the
  afecto flag stamped per line — never split filing; given the same patrono
  winning a public obra contract and enrolling for it, then an ADDITIONAL
  planilla generates per that contract. (FR-172, FR-173)
- **AC-007:** Given a planilla in estado "validada" (not yet paid), when a
  rectification is requested, then it is REJECTED (gate: estado "pagada");
  given the planilla reaches "pagada" and a rectificación for a salary
  difference then processes, then the system auto-generates the recargos of
  the mora engine at procedure time. (FR-171, FR-179)
- **AC-008:** Given a validated planilla of the period, when payment runs
  through virtual banking, then ONE receipt generates via the *Recibo
  Electrónico de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa
  INTECAP* settling the IGSS cuotas, the IRTRA impuesto and the INTECAP
  tasa in a single payment event — with the IRTRA/INTECAP amounts consumed
  from file 08's own rows, never printed here; given the same planilla paid
  after the due-date row, then the bank accepts it WITH mora (never
  refuses). (FR-174, FR-175)
- **AC-009:** Given cuotas paid N days after the external due-date row, when
  the mora exposure computes, then it equals Cuotas IGSS × tasa row × N/365
  (366 in a leap year) accrued from the day after the due date to effective
  payment, plus 5% gastos administrativos capped at Q3,000 when the
  liquidation originates a nota de cargo — with the tasa resolved only
  from the art.-38 index row (Junta Monetaria floating publication —
  no constant) and the recargos never exceeding 100% of the cuotas in
  mora. (FR-179)
- **AC-010:** Given a nota de cargo approved in the IGSS system on day 0,
  when the case clocks compute, then: notification due ≤ 5 días hábiles
  (+ distancia); pay-or-impugn window 15 días hábiles from notification
  (silence on all three exits → FIRME); Certificación de Gerencia itemizes
  both cuota shares + recargos + intereses + 5% admin (≤ Q3,000); and the
  económico-coactivo window is 15 días hábiles from the certification's
  reception. (FR-180)
- **AC-011:** Given a firm debt of cuotas Q50,000 with mora+interés Q18,000
  subscribed as a reconocimiento de deuda on day 0, then: the first level
  monthly installment is due the SAME day 0; the term ≤ 60 months; the
  mora+interés stack (Q18,000) is ≤ 100% of the cuotas (compliant) and
  would be capped at Q50,000 if it exceeded; the IRTRA/INTECAP arrears are
  demanded simultaneously with the first cuota; and on the second
  consecutive missed amortization the term AUTOMATICALLY accelerates —
  while any second RD request against the same patrono is rejected (one RD
  rule). (FR-181)
- **AC-012:** Given a collective-bargaining retroactive salary increase
  effective 6 months back, when the employer applies for the recargo
  waiver within the 6-month window, then the authorization oficio notifies
  and the employer has 45 días hábiles (one extension ≤ original) to
  generate, transmit, validate and pay the PERIOD-SPECIFIC complementary
  planillas — the retroactive pay entering as contribution-bearing
  complements of their devengo periods, never a current-period
  non-contributory lump. (FR-182; FR-169)
- **AC-013:** Given a contable review of a non-agro enterprise finding
  under-reported salaries and no payment history disputes, when the
  estimated-salary nota de cargo builds, then the estimate averages the
  planilla-reported salaries of the last SIX months (TWELVE for
  agropecuarias; enrollment filing when no history) and never falls below
  the salario mínimo of the AG vigente at detection (row consumed from
  GT-PAY-FR-073); given a computed-vs-printed contribution difference of
  0.4% of the total, then it sits inside the closed ±1% tolerance; given a
  difference ≤ Q500 in the Institute's favor, then no collection effort or
  nota de cargo issues (and a ≤Q500 note is annulled). (FR-178, FR-183)
- **AC-014:** Given a solvencia issued the day after a period's payment,
  when its validity computes, then it runs until the NEXT fecha límite row
  (FR-177: day 20 with its override slot); given an open reconocimiento de deuda, then solvencia
  is barred even though a merely-notified (not firm) nota de cargo would
  not bar it; given an enrollment-constancia request, then the issuance
  watchdate is 10 días hábiles. (FR-176)
- **AC-015:** Given any requirement, rule or citation resolving a deadline
  or mechanic to the `36_` guide, or an IGSS rate to AG 229-2014 (34_), or
  any cuota/recaudación effect to D-11-2004, when the citation-hygiene
  guard runs, then each is rejected — 36_ corroborates only, AG 229-2014 is
  SSO-scope (R40, duties owned by `10_sso-provenance.md`), D-11-2004 is
  governance-only (R39). (FR-184, FR-162)
- **AC-016:** Given the D-295 instrument row set, when the vigencia slot is
  inspected, then the three DCA installments (31-Oct/1-Nov/4-Nov-1946) are
  recorded with the vigencia-on-publication rule and NO operative date
  asserted (GOQ-74); given the 08-SGF/2026 switchover row, then its vigencia
  carries the OCR-truncated "30 días hábiles contados…" rule with the count
  basis open (GOQ-75) and no 2026 switchover date is dated.
  (FR-153; LB-010)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
allowed set for this file: GOQ-04, GOQ-74, GOQ-75 and the IGSS half of
GOQ-10 — each carried below. GOQ-10's IGSS half is RESOLVED (2026-08-22:
`87_` in corpus, LB-025 — the tasa's numeric value remains an inherently
external floating index); GOQ-04's target is REFINED (program
reglamentos) and RE-REFINED 2026-08-23 (LB-026: the SEM set `104_`-`106_`
acquired RATELESS — the rate hunt moves to the IVS Acuerdo 1124 named by
`107_` + the 410 art.-85 chain 475→1243); GOQ-74/75 stay open; GOQs are
trace-pending, not blockers. No new gaps beyond these owned registers were
found in this slice (the planilla file-format/layout absence rides GOQ-04's
acquisition family; the CPR arts. 88/100 identification text and the
D-295 clean-consolidation re-read ride GOQ-74).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-04 (owned, =OQ11, TARGET REFINED 2026-08-22): NONE of the corpus instruments prints the cuota percentages (12.67% patronal / 4.83% laboral priors unverifiable — rejected), the minimum monthly contribution-base amount, any tope máximo (no ceiling text anywhere — FR-166 negative) or the afecto-a-IVS test — Acuerdo 1421 is NOW IN CORPUS (`87_`/LB-025) and its art. 1 EXPRESSLY DELEGATES the montos to the reglamentos of the respective coverage programs (EVID-867): the acquisition target is thereby REFINED to the JD PROGRAM reglamentos (IM/IVS program sense of the 1118 family), NOT the recaudación line (art. 47's repeal of JD 1118/1200/1310 affects only the collection reglamentos; the cotizable-COMPONENT list, by contrast, is anchored at 1421 art. 4 — FR-169). **W-GT8 RE-REFINEMENT 2026-08-23 (`104_`-`108_` in corpus, LB-026; EVID-1132..1185): the SEM program-reglamento set (Acuerdo 410 consolidations `104_`/`106_` + reform Acuerdo 1154 `105_`) is IN CORPUS — RATELESS**: its only cuota text is art. 62's 1964 originals (4%/2%/1%; the 2011 print `106_` reads 3%/2%/1%), departamento-de-Guatemala-only per art. 85 and superseded by the unprinted footnote-21/23 extension chain (Acuerdos 475→616→621→849→1024→1095→1121→1243 — EVID-1151/1155/1167) — the rate target is thereby the IVS program reglamento **Acuerdo 1124 de Junta Directiva** (NAMED by the `107_` requisitos sheet: "(Artículo 22 y 23 del Acuerdo 1124 de Junta Directiva)") + that chain; the 12.67/4.83 priors remain rejected; the SEM set's benefit/qualification mechanics (art. 6's 3/6 + art.-26 maternidad credit; 84 Bis 4/6) are now primary. Until acquired: FR-155 ships EMPTY flagged rows (feeds file 09's estimated surfaces GT-TAX-FR-124/135); FR-165 floor = row only; FR-163 afecto test = config; FR-157 share-shift operative detail = config. Acquisition candidates: the IVS program reglamento Acuerdo 1124 (igssgt.org legislación; also carries the planilla file-format spec EVID-313 flags as absent) + the art.-85 rate chain acuerdos (475→1243). | no | GT synthesis wave S-GT3 → acquisition queue (IVS program reglamento Acuerdo 1124 + the 475→1243 rate chain — NOT 410 (SEM set acquired rateless, LB-026) nor 1421, which prints no rates) | open (target re-refined 2026-08-23: SEM set acquired rateless → Acuerdo 1124 + art.-85 chain) |
| OQ-002 | GOQ-74 (owned): D-295's 1946 gazette OCR is heavily degraded (every verbatim carries [sic] tolerance; re-verify clause wording against a clean consolidation before quoting beyond substance) and art. 12 sets vigencia "el día de su publicación en el Diario oficial" while publication ran in THREE installments (31-Oct/1-Nov/4-Nov-1946) — which installment legally triggers vigencia is not determinable from the Hemeroteca-certified print. FR-153 ships the row set with the date slot open. | no | GT synthesis wave S-GT3 → evidence re-read / acquisition queue (clean D-295 consolidation) | open |
| OQ-003 | GOQ-75 (owned): Resolución 08-SGF/2026 Sexto — "entra en vigencia a los 30 días hábiles contados…" — the OCR cuts the count basis (from emission? from a later publication/portal posting per Quinto?) and no DCA publication exists for this internal IGSS instrument. The 2026 recaudación switchover row (from SGF-R/2020 No. 342 to 08-SGF/2026) stays undated; verify the count basis externally before dating any switchover-driven behavior. | no | GT synthesis wave S-GT3 → evidence re-read (external verification of vigencia basis) | open |
| OQ-004 | GOQ-10, IGSS half (owned, RESOLVED 2026-08-22): the monthly planilla *fecha límite de pago*, the mora *tasa aplicable* and the RD interest all lived in Acuerdo 1421 — NOW IN CORPUS (`87_`/LB-025, EVID-866..882): due date = art. 9 *"a más tardar el veinte (20) de cada mes calendario"* for prior-calendar-month salaries, with the *"salvo que el Instituto establezca su propio calendario de pagos"* override slot and art. 42 inhábil roll-forward (FR-177 anchored); mora tasa = art. 38 Junta Monetaria *última tasa de interés simple máxima anual* (base *tasa ponderada bancaria para operaciones activas*), patrono-exclusive, general 100% cap (FR-179 anchored); RD interest = art. 31 c) Banguat *tasa activa promedio ponderado* at signing (FR-181 anchored); art. 21's 15-dh clock primary-verifies the `36_` guide citation (FR-184); art. 40 [printed "49", sic] = incobrabilidad, no prescription clock (FR-161 corrected). RESIDUALS: the tasa NUMERIC VALUES are inherently external floating index publications (runtime JM/Banguat feeds, never corpus-frozen — dated-row/config discipline preserved); whether an IGSS-issued calendar (e.g. the 08-SGF/2026 layer) supersedes day-20 in current practice stays a verification slot (evidence OQ 87_-4); art. 9's joined sentence is a marked OCR reconstruction (day-20 value cleanly printed — verify in clean print, evidence OQ 87_-1). (The GOQ-10 affiliation-deadlines and INTECAP-acta halves are owned outside this file.) | no | GT synthesis wave S-GT3 → resolved by `87_` acquisition (LB-025); residual index feeds tracked as runtime configuration | resolved (rules anchored; index values external) |
