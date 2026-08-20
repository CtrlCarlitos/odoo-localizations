# HN — Taxation — ISR framework: subjects, scope, rate architecture & Código Tributario chassis

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional framework for Honduras' *Impuesto sobre la
Renta* (ISR, income tax; Decreto-Ley 25 of 1963, consolidated through Acuerdo
SAR-07-2025) and the procedural chassis every HN tax obligation runs on — the
*Código Tributario* (CT, Tax Code, D. 170-2016 as updated through D.
180-2020). Covered: the *hecho generador* (taxable event) and the statutory
*ingreso* (income) concept; the ISR subject registry (domiciled residents,
State concessionaires, *herencias indivisas* (undivided estates), goods held
*en virtud de un cargo* (by virtue of an office)); the scope tension between
Ley ISR Art. 2's worldwide text (1963) and CT Art. 1.2's *renta territorial*
(territorial-income principle, 2016) — encoded as a dated regime flag under
proposed ruling R-H66, never silently; Honduran-source classification and the
1963 *vinculación económica* (economic relatedness) valuation rules (statutory
base of the modern TP regime — future TP work, cluster F10); subjective
exemptions with the public-enterprise carve-out (D. 219-2003); *pagos a
cuenta* (advance installment) eligibility; the rate-architecture ROUTING
(juridical persons 25% flat, natural persons progressive IPC-indexed, foreign
transport companies 10%-presumed-net, capital gains 10% *impuesto único*
routing) — bracket amounts and every dated value are owned by the
computation files of this directory (clusters T3-T7, S-HN1 wave) and are
never restated here; fiscal periods
and merger succession; the 40/60-day start/cessation sworn declarations
(*declaraciones juradas*, DJs); retention agents and the earliest-of
retention trigger; the single *domicilio tributario* (tax domicile) and RTN;
NIIF accounting books with 30-day posting plus the ISR book matrix and
*determinación de oficio* (assessment by the Administration) indicia;
retention *entero* (remittance) deferral and the retention *comprobante*
(voucher) duty; the *buzón electrónico* (electronic mailbox); refunds,
*rectificación* (rectification) and the *cuenta corriente tributaria* (tax
current account) with the February *depuración* (write-off ≤ 1 SMM); payment,
*compensación* (offset), *cesión* (assignment) and prescription (4/5/7
years); and the CT sanctions chassis — the formal-infraction multa table, the
ISR-late-declaration 5→25% escalator, moratory interest at 3% monthly capped
at 36%, RTN suspension and the administrative recourse ladder.

It does **not** cover: PN scale vintages, the withholding-asalariados
computation contract and the resident retention engines 12.5%/1%
(`04_isr-withholding.md`, clusters T3/T6; W4 payroll interfaces); the Art.
22-A gross minimum tax (cluster T4); capital-gains mechanics and the
non-resident withholding schedule (cluster T5); deductions and NOL (T2); the annual
declaration package, EEFF gate and DJIMR/OVI-SW chassis (clusters F1/F6/F7 of
the S-HN3 fiscal-reporting wave — referenced by cluster id only); payroll
withholding computation (S-HN4 wave); the facturación document taxonomy
(S-HN2 wave, clusters E1-E8); ISV (`06_isv.md`); and special regimes (T12).
Municipal taxes are outside CT scope by CT Art. 1.3 and are not modeled here.
Those files and waves reference this one for the subject/period/procedure
chassis.

## 2. Legal Basis

Authority order (binding, per master evidence index): ISR = `01_` (D.L. 25
consolidation SAR-07-2025 — current article text); CT = `03_` (D. 170-2016
act. D. 180-2020) with `23_` (Art. 206 void sentencia); sanction and
procedure locus = CT (R-H13: D. 22-97 Art. 222 mass derogation). Binding
rulings applied: R-H5 (CT Art. 206 VOID — dead text), R-H6 (mora = CT Art.
163: 3%/month, fraction pro-rated, cumulative, 36% cap), R-H12 (CT Art. 131
February depuración ≤ 1 SMM *promedio*, executed by SAR-125-2024 and
SAR-43-2026), R-H13 (CT locus). D-H1/D-H2/D-H3 (EXTRACTION_PLAN Decisions)
bind all rows.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR, Art. 1: "Se establece un impuesto anual denominado Impuesto sobre la Renta, que grava los ingresos provenientes del capital, del trabajo o de la combinación de ambos"; ingreso = "cualquier percepción en efectivo, en valores, en especie o en crédito, que modifique el patrimonio del contribuyente" | An annual tax called Income Tax is established, levied on income from capital, work or a combination of both; income = any perception in cash, securities, kind or credit that modifies the taxpayer's patrimony | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 1 p.3 (EV01:EVID-001) |
| LB-002 | Ley ISR, Arts. 2 y 6: sujetos = "Toda persona domiciliada o residente en Honduras, sea natural o jurídica, nacional o extranjera, inclusive la que goce de una concesión del Estado", gravándose la renta "ya sea que la fuente de la renta o ingreso esté situada dentro del país o fuera de él" (Art. 2; buques con bandera u operación hondureña, literales a-b); herencias indivisas y bienes administrados "en virtud de un cargo" (Art. 6) | Subjects: every person domiciled or resident in Honduras, natural or juridical, national or foreign, including State concessionaires, taxed on income "whether the source is located inside the country or outside it" (1963 worldwide text); Honduran-flag/operated merchant ships; undivided estates and goods administered by virtue of an office | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 2 pp.3-4; Art. 6 p.6 (EV01:EVID-001) |
| LB-003 | Ley ISR, Art. 3: exportación de bienes producidos/elaborados/tratados/comprados en el país = "totalmente de fuente hondureña"; valor bruto exportación = precio mayorista en destino deducidos costo de los bienes, transporte y seguro; sin precio o precio inferior → "se considerará, salvo prueba en contrario, que existe vinculación económica entre el exportador del país y el importador del exterior"; regla espejo importaciones ("de cuyo impuesto ambos son solidariamente responsables"); comparables = "los coeficientes de resultados obtenidos por empresas independientes que se dedican a idéntica o similar actividad"; en defecto la AT fija "el por ciento neto" por analogía | Exports of goods produced/manufactured/treated/bought in-country are wholly Honduran-source; export gross value = destination wholesale price less cost of the goods, transport and insurance; absent or below-price declarations raise a rebuttable presumption of economic relatedness between exporter and foreign importer (destination wholesale price governs); mirror rule for imports (both solidarily responsible for the tax); comparables = results coefficients of independent companies in identical or similar activity; else the AT sets the net percentage by analogy | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 3 pp.4-5 (EV01:EVID-002) |
| LB-004 | Ley ISR, Art. 7 (exenciones subjetivas): a) Estado, Distritos, Municipalidades y sus establecimientos e instituciones autónomas/semi-autónomas [fn.5, D. 219-2003 Art. 7: "Quedan sujetas al pago del impuesto sobre la renta las empresas públicas"]; b) beneficencia e instituciones sin fines de lucro científicas/políticas/religiosas/culturales/deportivas; c) "La Iglesia como institución"; d) diplomáticos (reciprocidad, remuneraciones de su propio país); e) cámaras/colegios/sindicatos (actividades sin fines de lucro); f) maestros de primaria/secundaria/UNAH por sus sueldos y jubilaciones (D. 71-88) | Subjective exemptions: the State, Districts, municipalities and their autonomous/semi-autonomous establishments [fn.5: public enterprises ARE subject to ISR per D. 219-2003]; charities and non-profit scientific/political/religious/cultural/sports institutions; the Church as an institution; diplomats (reciprocity, own-country remuneration only); employer/professional associations and unions (non-profit activities); teachers on primary/secondary/UNAH salaries plus their retirement payments from those sources | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 7 pp.6-7 (EV01:EVID-004) |
| LB-005 | Ley ISR, Art. 8: "Pagos a Cuenta": "Cada una de las cuatro cuotas trimestrales de pago del impuesto sobre la renta"; sujetos = todas las personas del Art. 2 salvo "aquellas personas cuyos ingresos provengan del trabajo personal y que sus respectivos impuestos están sujetos a retención en la fuente mensual"; residente = quien vive en el país sin ser "un mero transeúnte"; tripulantes de buques con bandera hondureña = residentes | Pagos a cuenta = each of the four quarterly installments of the ISR; subjects = all Art. 2 persons EXCEPT those whose income derives from personal work whose taxes are subject to monthly withholding at source; a resident lives in the country without being a mere transient; crews of Honduran-flag ships are residents | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 8 pp.7-8 (EV01:EVID-005) |
| LB-006 | Ley ISR, Arts. 22-23: "Las personas jurídicas pagarán una tarifa de veinticinco por ciento (25%) sobre el total de la renta neta gravable" (22.a); "Esta escala de tasas progresivas será ajustada automáticamente de forma anual a partir del año 2017... aplicando la variación interanual del Índice de Precios al Consumidor (IPC)... Asimismo, estos valores se ajustarán en los artículos de la presente Ley que hagan referencia a los mismos" (22.b; exención del primer tramo, Art. 23); transporte internacional aéreo/marítimo/terrestre: renta neta presunta "equivalente al diez por ciento (10%) del total de los ingresos brutos anuales de fuente hondureña", tarifa 25% (22.c) | Juridical persons pay 25% on total net taxable income; the PN progressive scale auto-adjusts annually from 2017 by the interannual CPI variation, and reference values in other articles adjust with it (Art. 23 exempts the first band — amounts owned by cluster T3 as dated SAR-acuerdo rows); international air/sea/land transport companies apply a presumed net base equal to 10% of gross Honduran-source income, taxed at 25% | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 22 (pp.16-17), 23 (p.21) (EV01:EVID-010) |
| LB-007 | Código Tributario, Art. 1: "1) Las disposiciones de este Código... son aplicables a todos los tributos; 2) Honduras se rige en el principio de renta territorial. Se faculta al Poder Ejecutivo para aprobar Convenios para evitar la doble tributación...; 3) Lo prescrito en este Código no debe ser aplicable al Régimen Tributario Municipal" | CT scope: provisions apply to all tributes; Honduras is governed by the territorial-income principle, with Executive authorization for double-taxation conventions; the CT does not apply to the municipal tax regime | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Art. 1 p.3 (EV03:EVID-027) |
| LB-008 | CT, Art. 26 (períodos): tributos anuales = año calendario "que principia el uno (1) de enero y termina el treinta y uno (31) de diciembre"; inicio mediano de año → desde el inicio de actividades; tributos mensuales = mes natural; la AT puede autorizar período fiscal especial en casos excepcionales justificados; la muerte o cese cierra el ejercicio en esa fecha; fusión/absorción: el ejercicio se cierra en la fecha de la fusión y la entidad superviviente "debe asumir las obligaciones tributarias y los créditos fiscales del que haya desaparecido" | Annual taxes run on the calendar year; mid-year starters compute from activity start; monthly taxes on the natural month; the AT may authorize special fiscal periods in exceptional justified cases; death or cessation closes the exercise at that date; on merger/absorption the exercise closes at the merger date and the surviving entity must assume the tax obligations and the fiscal credits of the disappeared entity | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Art. 26 pp.34-35 (EV03:EVID-028) |
| LB-009 | CT, Arts. 30-35: contribuyentes = personas directamente obligadas al hecho generador; agente de retención designado por ley o la AT "atendiendo a su actividad, función o posición contractual"; "La retención se debe efectuar en el momento en que se realice el pago o devengo del tributo, lo que se realice primero" (32.2); agente de percepción cobra al recibir el pago (33); herederos responden hasta el monto de la cuota hereditaria (34); terceros responsables por ley (35) | Taxpayers are persons directly bound by the taxable event; withholding agents are designated by law or the AT according to activity, function or contractual position; the retention must be effected at the moment the payment or the accrual of the tribute occurs, whichever happens first; collection agents collect upon payment receipt; heirs are liable up to the inherited portion; third parties responsible by law | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 30-35 pp.38-42 (EV03:EVID-029) |
| LB-010 | CT, Arts. 50-57: cascada de domicilio PN (residencia → actividad habitual → hecho generador → elección AT, Art. 50) y PJ (domicilio social → administración efectiva → centro principal de actividad, Art. 51); declarado y modificable, subsiste hasta notificarse el cambio (53); "toda persona natural, jurídica o entidad solo debe tener un domicilio" (54); primera emisión de RTN gratuita (55.2); asistencia de la AT + software gratuito (56); Defensoría CONADEH (57) | Tax-domicile cascade for natural persons (residence → habitual activity → taxable event → AT election) and juridical persons (registered office → effective management → main activity center); declared and changeable, subsisting until the change is notified; every person or entity may have only ONE domicile; first RTN issuance free; AT assistance duties; CONADEH ombudsman | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 50-57 pp.50-60 (EV03:EVID-030) |
| LB-011 | CT, Arts. 59, 62, 64-66: la AT categoriza contribuyentes por Acuerdo Ejecutivo (criterios publicados, actualizados ≥ cada 2 años, Art. 59); declaraciones/autoliquidaciones/informes según ley (62); obligación de llevar contabilidad: "1) Llevar y mantener los registros contables que determinen las leyes, los respectivos reglamentos y las Normas Internacionales de Información Financiera generalmente aceptadas en Honduras; 2) Los asientos... se deben efectuar dentro de los treinta (30) días siguientes a la fecha en que se realizó el hecho generador de la operación" (64); documentos fiscales identificando emisor/receptor/operación (65); inscripción en el RTN (66) | The AT categorizes taxpayers by Executive Accord (published criteria refreshed at least every 2 years); declarations per law; bookkeeping obligation: keep the accounting records determined by laws, regulations and generally-accepted IFRS (NIIF), with entries posted within 30 days of the operation's taxable event; issue fiscal documents identifying issuer, receiver and operation; RTN inscription duty | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 59, 62-66 pp.63-70 (EV03:EVID-031) |
| LB-012 | CT, Arts. 67-68, 74-75: inicio de actividades → DJ "dentro de los cuarenta (40) días calendarios siguientes" (67); cese → DJ y pago "dentro de los sesenta (60) días calendarios siguientes" + comunicación de los documentos retenidos (68); entero: lo recaudado por retención/percepción ingresa a la TGR o bancos autorizados SEFIN "dentro de los plazos señalados en las leyes tributarias o aduaneras especiales" en formularios de la AT (74); el agente debe entregar al contribuyente "un documento fiscal de la suma retenida" (75) | Start of activities → sworn declaration within the 40 following calendar days; cessation → DJ and payment within the 60 following calendar days plus notice of the retained documents; remitted retention amounts go to the TGR or SEFIN-authorized banks within the deadlines set by the special tax/customs laws, on AT forms; the agent must deliver each taxpayer a fiscal document for the retained sum (the retention voucher) | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 67-68, 74-75 pp.71-85 (EV03:EVID-032) |
| LB-013 | CT, Arts. 83-84: documentos/copias electrónicos emitidos o conservados por SEFIN/AT "tienen la misma validez y eficacia jurídica" que los físicos (83); buzón electrónico = herramienta tecnológica permanente que "debe sustituir al domicilio tributario como lugar para recibir notificaciones" para los inscritos, con sistema de alertas (84) | Electronic documents/copies issued or stored by SEFIN/AT have the same legal validity and effect as physical ones; the electronic mailbox is a permanent technological tool that must replace the tax domicile as the place to receive notifications for enrolled taxpayers, with an alerts system | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 83-84 pp.92-93 (EV03:EVID-033) |
| LB-014 | CT, Arts. 115-118, 129-131: derecho a la restitución por pago en exceso o indebido (115); procedencia por pago duplicado, mayor que el determinado o indebido (116); rectificación de declaraciones que reduzcan el impuesto o aumenten el saldo a favor — verificación previa de la AT (117); liquidación administrativa aceptada → "exento de las multas. La liquidación sirve como documento válido para generar los débitos en la cuenta corriente" (118.6); cobro persuasivo pre-judicial (129); depuración anual: "cada febrero" la AT/Aduanera descarga de oficio los créditos firmes ≤ 1 salario mínimo promedio vigente (131) | Restitution right for excess/undue payment; refund triggers: duplicate payment, payment above assessment, undue payment; rectified declarations reducing tax or increasing credit balance require prior AT verification; an accepted administrative liquidation is multa-exempt and is a valid document to generate current-account debits; persuasive pre-judicial collection; each February the AT/Customs writes off of office the firm credits of up to 1 average minimum wage in force (R-H12; executed by SAR-125-2024/SAR-43-2026) | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 115-118 pp.122-127; 129-131 pp.149-153 (EV03:EVID-034) |
| LB-015 | CT, Arts. 134-148: modos de extinción: pago, "compensación y cesión", confusión, condonación, prescripción, abandono (134); pago el mismo día de la autoliquidación salvo norma en contrario (137.1); imputación por el contribuyente, en su defecto la AT (139); facilidades de pago (140); lugar: TGR/bancos con convenio SEFIN (141); compensación de obligaciones "con créditos por tributos, sus accesorios, líquidos, exigibles y no prescritos", a petición o de oficio, y cesión regulada en el Art. 142; condonación sólo por Ley (143); prescripción (144.2): a) 4 años [operaciones bajo regímenes aduaneros]; b) 5 años [inscritos en el RTN]; c) 7 años [demás casos]; herederos: suspensión de 3 años para repeticiones (d); cómputo e interrupción (145, 148) | Extinction modes: payment, offset and assignment, merger of parties, condonation, prescription, abandonment; payment due the same day as the self-assessment unless a rule differs; imputation chosen by the taxpayer else the AT; payment facilities; place = TGR/SEFIN-agreement banks; obligations offset against tax credits that are liquid, due and not prescribed, on petition or ex officio, with assignment regulated in Art. 142; condonation only by statute; prescription: 4 years customs-regime operations, 5 years RTN-inscribed taxpayers, 7 years other cases; 3-year suspension for heirs' refund petitions; computation and interruption rules | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 134-148 pp.154-167 (EV03:EVID-035) |
| LB-016 | CT, Arts. 149-160: faltas formales vs materiales (149-150); multa formal "no causa intereses" (158); sanción independiente (159); tabla Art. 160.1 por rango de ingresos brutos anuales: L0.01-250,000 → 10% SMM promedio; 250,000-500,000 → 25%; 500,000-1,000,000 → 50%; 1-5 millones → 1 SMM; 5-10 millones → 2 SMM; 10-50 millones → 5 SMM; 50-100 millones → 10 SMM; >100 millones → 10 SMM + 1% SMM por cada L500,000 adicionales; Art. 160.2 declaración ISR extemporánea/omitida (no acumulativa): "5% del impuesto causado" (mes 1), 10% (mes 2), 15% (mes 3), 20% (mes 4), 25% (mes 5 y siguientes) — "proporcional a los días transcurridos"; ISR conectado/cédula igual tratamiento (160.3); ventana de rectificación ≥10 días hábiles antes de multa; reducción por subsanación espontánea (162) | Formal vs material infractions; formal multas bear no interest; sanctions independent; the Art. 160.1 formal-infraction multa table keyed to gross annual income bands × fractions/multiples of the SMM promedio; Art. 160.2 late/missing ISR declaration (non-cumulative): 5% of tax caused (month 1), 10/15/20/25% for months 2 through 5+, proportional to days elapsed; connected/cédular ISR taxes follow the same treatment; ≥10-business-day rectification window before sanction; reduction for spontaneous cure | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 149-160 pp.167-181 (EV03:EVID-036) |
| LB-017 | CT, Arts. 161-164: cierre temporal por reincidencia (161); reducción por subsanación (162); Art. 163: "A falta de pago en plazo de los tributos y de los pagos a cuenta, el obligado tributario debe pagar... b) Los intereses moratorios del tres por ciento (3%) mensual o fracción de mes calculado sobre el tributo a pagar, acumulándose mensualmente hasta que se produzca el pago, hasta un máximo de treinta y seis por ciento (36%)"; suspensión del RTN al no estar solvente en obligaciones materiales firmes agotados los recursos (164) | Temporary closure for recidivism; sanction reduction for cure; Art. 163: failure to pay tributes or advance installments on time accrues moratory interest of 3% monthly or fraction thereof computed on the tax due, accumulating monthly until payment occurs, capped at 36%; RTN suspension when not solvent on firm material obligations after recourse is exhausted | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 161-164 pp.182-189 (EV03:EVID-037; R-H6) |
| LB-018 | CT, Arts. 168-184, 195-211: cadena de recursos — Reposición (mismo órgano, 20 días hábiles para resolver) → Apelación (SEFIN/Superintendencia, agotamiento) → Revisión extraordinaria (dentro de 2 años, resoluciones firmes) (169-182); expediente electrónico/portal (184); SAR como entidad desconcentrada de la Presidencia (zona Art. 195); interpretación/consultas (201-204; Art. 206 = VOID, ver LB-023) | Recourse ladder: reposición (same organ, resolved within 20 business days) → appeal (SEFIN/Superintendence, exhaustion) → extraordinary revision (within 2 years against firm resolutions); electronic case file/portal duty; SAR institutional law; interpretation/consultations regime (Art. 206 void — LB-023) | `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` | Arts. 168-184 pp.193-206; 195-211 pp.216-232+ (EV03:EVID-038) |
| LB-019 | Ley ISR, Arts. 30, 30-A, 31: libros según la Ley Sobre Normas de Contabilidad y de Auditoría (D. 189-2004); agricultores/ganaderos/profesionales/talleres: "un libro de entradas y salidas" + balance anual de operaciones; "Los importadores obligatoriamente llevarán un libro de costos o de prorrateo de mercaderías"; contadores solidariamente responsables del fraude (30); registros de control de inventarios con movimiento/valuación/identificación reales "a satisfacción de la Administración Tributaria" (30-A); determinación de oficio sobre indicios (libros ausentes/irregulares o sin comprobantes): compras/ventas/rotación, márgenes de plaza, gastos personales, patrimonio, contratos, intereses (31) | Books per the Accounting and Auditing Standards Law (D. 189-2004); farmers/ranchers/professionals/workshops keep a single income-and-expenses book plus a year-end operations balance; importers mandatorily keep a cost or merchandise-allocation book; accountants solidarily responsible for fraud; inventory control records reflecting real movement/valuation/identification to the AT's satisfaction; assessment ex officio on indicia where books/vouchers are missing or irregular: purchases/sales/rotation, market margins, personal expenses, patrimony, contracts, interest | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 30-31 pp.24-26 (EV01:EVID-014) |
| LB-020 | Ley ISR, Arts. 36-37: cese de actividades → DJ y balance final certificado dentro de los 90 días; salida definitiva del país → DJ y pago antes de salir; muerte → los herederos presentan/pagan dentro de 90 días (36); disolución de sociedades: 90 días (37) | Cessation of activities → DJ and final certified balance within 90 days; definitive departure → DJ and payment before leaving the country; death → heirs file/pay within 90 days; society dissolution: 90 days — pre-CT residues in tension with LB-012's 60-day rule (see OQ-005) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 36-37 p.28 (EV01:EVID-014) |
| LB-021 | Ley ISR, Arts. 44, 46, 47: los registradores de la propiedad exigen certificación de solvencia ISR para inscribir transmisiones de bienes raíces (44/46); Art. 47: las sociedades que distribuyan dividendos informan antes del último día de febrero — nombre de socios, acciones, valor nominal, % de dividendo por semestre y total pagado por accionista | Property registrars require an ISR solvency certificate to register real-estate transfers; dividend-paying companies report before the last day of February the shareholder roster (name, shares, nominal value, per-semester dividend percentage, total paid per shareholder — feeds código 541, cluster F10) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 44, 46, 47 pp.29-30 (EV01:EVID-014) |
| LB-022 | Ley ISR, Arts. 26 y 34: retención de dividendos depositada "dentro de los diez (10) días calendario del mes siguiente" a la TGR/instituciones autorizada SEFIN (26); agentes de retención: DJ mensual y entero "a más tardar dentro de los diez (10) días calendario del mes siguiente" (34) — los plazos especiales a los que el Art. 74 CT (LB-012) difiere | Dividend withholding deposited within the first ten calendar days of the following month with the TGR/SEFIN-authorized institutions; retention agents file a monthly DJ and remit at latest within the ten calendar days of the following month — the special-law deadlines that CT Art. 74 defers to | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 26 (p.22), 34 (pp.26-27) (EV01:EVID-012/013) |
| LB-023 | Sentencia Sala Constitucional CSJ, expediente SCO-800-2017 (fallo 22-feb-2022; certificación 18-mar-2022; La Gaceta 36,131, 17-ene-2023), FALLO: "DECLARANDO LA INCONSTITUCIONALIDAD E INAPLICABILIDAD del artículo 206... en forma parcial y por razón de contenido... con efecto erga omnes, lo cual opera de pleno derecho a partir de la rúbrica de la presente sentencia" — contenido nulo: garantía para admisión de demanda del 5/10/20% por tamaño de contribuyente (Arts. 206.2 a-c); el fallo deroga el artículo completo, numeral 1 incluido | Constitutional Chamber judgment striking CT Art. 206 (demand-admission guarantee of 5/10/20% of the claim by taxpayer size) as unconstitutional and inapplicable with erga omnes effect operating from the 22-feb-2022 rubric — the whole article including numeral 1 is dead text (R-H5): never implement any litigation-guarantee logic | `hn/sources/23_Sentencia_inconst_Art206_CT_2023.pdf` | CONSIDERANDO 10 p.5; FALLO pp.8-9 (EV05:EVID-068; R-H5) |
| LB-024 | Ley ISR, Art. 10: "Las ganancias de capital obtenidas por las personas naturales o jurídicas, domiciliadas o no en Honduras, pagarán un impuesto único del 10%... por lo que no estarán sujetas a la tarifa progresiva"; rentas no gravadas: a) indemnizaciones/seguros de instituciones hondureñas; c) subsidios Estado/municipales; d) herencias/legados/donaciones; e) lotería nacional; f) riesgos profesionales e IHSS; g) rentas de fondos de pensiones (instituciones del país); h) prestaciones laborales y bonificación por vacaciones hasta un pago adicional de 30 días, jubilaciones, pensiones y montepíos; "El décimo tercer mes en concepto de aguinaldo, así como el décimo cuarto mes de salario, hasta por el monto de diez (10) salarios mínimos promedio" (exceso gravable) | Capital gains by natural or juridical persons, domiciled or not, bear a single 10% tax and are NOT subject to the progressive tariff (mechanics owned by cluster T5); non-grossable rents: Honduran-institution insurance payouts; State/municipal subsidies; inheritances/legacies/donations; national lottery prizes; occupational-risk and IHSS benefits; pension-fund investment income; labor benefits and vacation bonus up to 30 additional days, retirements, pensions and death benefits; 13th and 14th month salaries each up to 10 average minimum wages (excess taxable — caps computed by payroll/withholding surfaces) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 10 pp.9-10 (EV01:EVID-006) |

Dead text — never implementable as current law (recorded as LB notes, not
FRs, per wave constraint): CT Art. 206 litigation guarantee, void since
22-feb-2022 (LB-023; R-H5; EV05:EVID-068). Superseded SAR/DEI-era 1%/month
mora references are displaced by CT Art. 163's 3%/36% regime (LB-017; R-H6).
ISR-law sanction/procedure articles were mass-derogated to the CT by D. 22-97
Art. 222 (R-H13; EV01 reform-history anchor — EVID-014 Cuadros 1-2).

## 3. Functional Requirements

### 3.1 Hecho generador, income concept and subjects (T1)

- **HN-TAX-FR-001:** The system shall recognize the ISR obligation as an
  *annual* tax on income from capital, work, or a combination of both, and
  shall treat as *ingreso* (income) every perception in cash, securities,
  kind or credit that modifies the taxpayer's patrimony. (LB-001; EV01:EVID-001)
- **HN-TAX-FR-002:** The system shall support ISR-subject registration for
  every person domiciled or resident in Honduras — natural or juridical,
  national or foreign, including holders of State concessions — plus the
  special categories *herencias indivisas* (undivided estates) and taxpayers
  administering goods *en virtud de un cargo* (by virtue of an office), and
  Honduran-flagged or Honduras-operated merchant ships as taxable units.
  (LB-002; EV01:EVID-001)
- **HN-TAX-FR-003:** The system shall apply the statutory residency test —
  living in the country without being a *mere transient* (*un mero
  transeúnte*) — and shall treat crews of Honduran-flag ships as residents,
  flagging them for the domiciled-scope regime of FR-004. (LB-002; LB-005; EV01:EVID-001/005)
- **HN-TAX-FR-004:** The system shall resolve the tax-scope regime for
  foreign-source income of domiciled persons from a dated configuration table
  (`worldwide` per Ley ISR Art. 2, the 1963 text, for periods before
  2017-01-01; `territorial` per CT Art. 1.2 from 2017-01-01 — the proposed
  master-index ruling R-H66, see OQ-001), resolved as-of each computation's
  period date per D-H2 (never "today"); under the territorial rows,
  foreign-source income of domiciled persons is excluded from the ISR base
  absent a specific statutory inclusion. The regime selection shall remain a
  reversible dated row pending controller confirmation of R-H66 — neither
  text is encoded silently. (LB-002; LB-007; EV01:EVID-001; EV03:EVID-027; OQ-001)
- **HN-TAX-FR-005:** The system shall classify as wholly Honduran-source
  (*totalmente de fuente hondureña*) the export income of goods produced,
  manufactured, treated or bought in the country, valuing export gross income
  at the destination wholesale price less the cost of the goods, transport
  and insurance; and shall apply the mirror rule on imports — the value
  difference constitutes Honduran-source income for which exporter and
  importer are *solidarily responsible*. (LB-003; EV01:EVID-002)
- **HN-TAX-FR-006:** The system shall raise a rebuttable presumption of
  *vinculación económica* (economic relatedness) between the local exporter
  and the foreign importer when no price is declared or the declared price is
  below the destination wholesale price — which then governs — and shall
  record the valuation fallback chain: results coefficients of independent
  companies in identical or similar activity, else the AT-set net percentage
  by analogy; these 1963 rules are the recorded base of the modern TP regime
  (declaration surfaces and ajustes owned by future TP work, cluster F10).
  (LB-003; EV01:EVID-002)
- **HN-TAX-FR-007:** The system shall flag as subjectively exempt (no
  substantive ISR obligation, formal duties surviving) the Art. 7 categories:
  the State, Districts, municipalities and their autonomous/semi-autonomous
  establishments; charities and non-profit scientific, political, religious,
  cultural or sports institutions; the Church as an institution; diplomats
  under reciprocity (own-country remuneration only); employer and
  professional associations and unions (non-profit activities); and teachers
  on primary/secondary/UNAH salaries plus those retirement payments.
  (LB-004; EV01:EVID-004)
- **HN-TAX-FR-008:** The system shall force *empresas públicas* (public
  enterprises) to remain taxable notwithstanding the Art. 7.a State-category
  exemption, per the D. 219-2003 Art. 7 carve-out recorded in the
  consolidation's footnote 5. (LB-004; EV01:EVID-004)
- **HN-TAX-FR-009:** The system shall gate *pagos a cuenta* (advance
  installment) eligibility: all Art. 2 subjects qualify EXCEPT persons whose
  income derives from personal work whose taxes are subject to monthly
  withholding at source (salary-only taxpayers excluded — monthly withholding
  replaces the advance regime; computation and calendar surfaces owned by
  clusters T3/W4 and F7). (LB-005; EV01:EVID-005)

### 3.2 Rate-architecture routing (T1 — overview only; values never restated)

- **HN-TAX-FR-010:** The system shall route juridical persons to the flat
  25% track over the total *renta neta gravable* (net taxable income) — the
  structural rate recorded here; every computation, threshold and dated value
  is owned by the computation files of this directory (clusters T3-T7).
  (LB-006; EV01:EVID-010)
- **HN-TAX-FR-011:** The system shall route natural persons to the
  progressive track (15/20/25 bracket structure over an exempt first band)
  whose amounts are auto-adjusted annually from 2017 by the interannual IPC
  variation — reference values elsewhere in the Law adjusting in step — and
  shall source each fiscal year's bracket amounts exclusively from the dated
  SAR-acuerdo rows owned by `04_isr-withholding.md` (cluster T3; D-H2: additive
  `valid_from`/`valid_to` rows resolved by period date, never replaced in
  place). This file records the mechanism only; no bracket value is restated
  here. (LB-006; EV01:EVID-010)
- **HN-TAX-FR-012:** The system shall route foreign air/sea/land transport
  companies operating in the country to the presumed-net regime: presumed net
  base = 10% of total annual gross Honduran-source income, taxed at the 25%
  tariff on the presumed base. (LB-006; EV01:EVID-010)
- **HN-TAX-FR-013:** The system shall route *ganancias de capital* (capital
  gains) of any person, domiciled or not, to the single 10% *impuesto único*
  track, outside the progressive tariff (per-transaction mechanics, value
  formula and non-resident retentions owned by the cluster-T5 file).
  (LB-024; EV01:EVID-006)
- **HN-TAX-FR-014:** The system shall provide a *rentas no gravadas*
  (non-grossable income) classification stamp with the Art. 10 catalog —
  Honduran-institution insurance payouts; State/municipal subsidies;
  inheritances, legacies and donations; national lottery prizes;
  occupational-risk indemnities and IHSS benefits; pension-fund investment
  income; labor benefits, vacation bonus up to 30 additional days,
  retirements, pensions and *montepíos*; and 13th/14th-month amounts up to
  10 × SMM *promedio* each (excess taxable) — amount computations and
  promedio feeds owned by the deductions/withholding files (clusters
  T2/T3 = `04_isr-withholding.md`) and the payroll wave (W4-P1; R-H47: never
  recompute the promedio). (LB-024; EV01:EVID-006)

### 3.3 Fiscal periods, entity lifecycle and DJs (T11)

- **HN-TAX-FR-015:** The system shall compute annual tributes on the calendar
  fiscal year (1-January through 31-December), computing the exercise of
  mid-year starters from the start of activities, and monthly tributes on the
  natural month. (LB-008; EV03:EVID-028)
- **HN-TAX-FR-016:** The system shall support AT-authorized special fiscal
  periods in exceptional justified cases (CT Art. 26.5; Ley ISR Art. 27
  requires prior written notice) as a dated per-company regime row with its
  own closing date; the declaration window for special-period taxpayers is
  owned by cluster F7. (LB-008; EV01:EVID-013; EV03:EVID-028; OQ-002)
- **HN-TAX-FR-017:** The system shall close the fiscal exercise at the date
  of death or cessation of activities, generating a short-period computation
  for that exercise. (LB-008; EV03:EVID-028)
- **HN-TAX-FR-018:** The system shall, on merger/absorción (*fusión*), close
  the absorbed entity's exercise at the merger date and migrate ALL its tax
  obligations AND fiscal credits to the surviving entity (both sides of the
  FR-036 cuenta corriente). (LB-008; EV03:EVID-028)
- **HN-TAX-FR-019:** The system shall schedule the start-of-activities
  sworn declaration (*declaración jurada de inicio*) due within the forty
  (40) calendar days following the start. (LB-012; EV03:EVID-032)
- **HN-TAX-FR-020:** The system shall schedule cessation obligations per the
  CT 60-calendar-day rule (DJ plus payment, with notice of retained
  documents) as the operative deadline (lex posterior 2017; R-H13 procedural
  locus), while carrying the ISR-law residues for events the CT rule does
  not cover — final certified balance, definitive-departure DJ and payment
  before leaving the country, heirs' 90-day filing on death, and 90-day
  society dissolution — flagged for verification against the pre-CT texts
  (OQ-005). (LB-012; LB-020; EV03:EVID-032; EV01:EVID-014; OQ-005)
- **HN-TAX-FR-021:** The system shall gate real-estate transfer registration
  workflows on the AT-issued ISR solvency certificate (registrars may not
  record transmissions without it). (LB-021; EV01:EVID-014)
- **HN-TAX-FR-022:** The system shall maintain the Art. 47 shareholder
  dataset — partner name, shares, nominal value, per-semester dividend
  percentage and total paid per shareholder — feeding the end-of-February
  informative filing owned by cluster F10 (código 541). (LB-021; EV01:EVID-014)

### 3.4 Agents, retention timing, domicilio and RTN (T11)

- **HN-TAX-FR-023:** The system shall stamp every retention — across all
  retention engines owned by `04_isr-withholding.md` and the payroll wave — with a
  trigger date computed as the earliest of payment or accrual (*el momento en
  que se realice el pago o devengo del tributo, lo que se realice primero*).
  (LB-009; EV03:EVID-029)
- **HN-TAX-FR-024:** The system shall maintain the retention/collection
  agent registry — agents designated by law or by the AT according to their
  activity, function or contractual position (*atendiendo a su actividad,
  función o posición contractual*) — distinguishing *agente de retención*
  (withholding agent) from *agente de percepción* (collection agent).
  (LB-009; EV03:EVID-029)
- **HN-TAX-FR-025:** The system shall record solidarity exposures: heirs
  liable up to the inherited portion, and third parties responsible by law
  (including non-retaining agents flagged by the retention engines' owner
  files). (LB-009; EV03:EVID-029)
- **HN-TAX-FR-026:** The system shall model the *domicilio tributario* with
  the statutory cascade (natural persons: residence → habitual activity →
  taxable event → AT election; juridical persons: registered office →
  effective management → main activity center), declared and changeable,
  subsisting until the change is notified, and shall enforce the invariant
  that a taxpayer holds exactly ONE domicilio. (LB-010; EV03:EVID-030)
- **HN-TAX-FR-027:** The system shall treat the RTN (Registro Tributario
  Nacional number, 14 characters) as the single fiscal identity for
  inscription and all obligations (first issuance free), with AT taxpayer
  categorization (Acuerdo Ejecutivo criteria refreshed ≥ every 2 years)
  carried as dated configuration. (LB-010; LB-011; EV03:EVID-030/031)

### 3.5 Books, records and assessment indicia (T11 + Ley ISR Arts. 30-31)

- **HN-TAX-FR-028:** The system shall keep the statutory accounting records
  under NIIF (generally-accepted IFRS) as anchored by CT Art. 64, and shall
  flag accounting entries posted later than thirty (30) calendar days after
  the operation's *hecho generador* as outside the statutory posting window.
  (LB-011; EV03:EVID-031)
- **HN-TAX-FR-029:** The system shall maintain the ISR book-requirement
  matrix by taxpayer class: full D. 189-2004-standard books for mercantile
  enterprises; the simplified single income-and-expenses book plus annual
  operations balance for farmers, ranchers, professionals and workshops; the
  mandatory cost or merchandise-allocation book for importers; and inventory
  control records reflecting real movement, valuation and identification
  (accountants recorded as solidarily responsible for fraud).
  (LB-019; EV01:EVID-014)
- **HN-TAX-FR-030:** The system shall expose a *determinación de oficio*
  (ex-officio assessment) indicia monitor for taxpayers without books,
  without vouchers or with irregular books, tracking the statutory indicia
  set — purchases, sales and rotation; market (*plaza*) margins; personal
  expenses; patrimony; contracts; interest — as data sources for an
  AT-computed assessment scenario. (LB-019; EV01:EVID-014)

### 3.6 Retention entero, comprobantes and buzón (T11)

- **HN-TAX-FR-031:** The system shall defer each retention engine's *entero*
  (remittance) deadline to the special-law deadline registry — defaulting to
  the ISR plazos of ten (10) calendar days of the month following the
  retention (dividend Art. 26; retention agents Art. 34) — with remittance to
  the TGR or SEFIN-authorized banks on AT forms, and shall track
  per-instrument exceptions on the engines' owner files (clusters T6/F2).
  (LB-012; LB-022; EV03:EVID-032; EV01:EVID-012/013)
- **HN-TAX-FR-032:** The system shall flag the retention-agent duty to
  deliver each taxpayer a *comprobante de retención* (retention voucher — a
  documento fiscal for the retained sum; document taxonomy owned by cluster
  E6 of the S-HN2 wave). (LB-012; EV03:EVID-032)
- **HN-TAX-FR-033:** The system shall recognize SEFIN/AT-issued electronic
  documents as fully valid and shall record per-taxpayer enrollment in the
  *buzón electrónico* as the notification channel that replaces the tax
  domicile (execution and SAR-integration surfaces owned by cluster F1,
  S-HN3 wave — informational configuration here). (LB-013; EV03:EVID-033)

### 3.7 Refunds, rectificación and cuenta corriente (T11)

- **HN-TAX-FR-034:** The system shall support refund/restitution workflows
  for excess or undue payments with the CT triggers — duplicate payment,
  payment above the assessed amount, and undue payment. (LB-014; EV03:EVID-034)
- **HN-TAX-FR-035:** The system shall route rectified declarations that
  REDUCE tax or INCREASE a credit balance through prior AT verification
  before acceptance — such rectifications never silently re-book balances
  (filed-period freeze per D-H2.5; declaration-surface chassis = cluster
  F1). (LB-014; EV03:EVID-034)
- **HN-TAX-FR-036:** The system shall maintain a *cuenta corriente
  tributaria* ledger per taxpayer and obligation — débitos and créditos with
  origins (self-assessment, accepted administrative liquidation, retention,
  payment, offset, assignment, refund) — where an accepted administrative
  liquidation is multa-exempt and generates valid débitos, feeding
  pre-judicial persuasive collection status. (LB-014; EV03:EVID-034)
- **HN-TAX-FR-037:** The system shall mark, each February, firm credit
  balances ≤ 1 SMM *promedio* vigente as dischargeable by AT *oficio*
  (*depuración anual*), resolving the threshold from the dated SMM-promedio
  rows (snapshot-on-write per D-H2; R-H12 — L13,985.16 promedio anchor per
  SAR-43-2026 for the 2026 execution; promedio values consumed from the
  P1/R-H47 rows, never recomputed). (LB-014; EV03:EVID-034; R-H12)

### 3.8 Payment, compensación, cesión and prescription (T11)

- **HN-TAX-FR-038:** The system shall schedule tax payments on the same date
  as the self-assessment unless the applicable law differs, allow
  taxpayer-chosen imputation (AT deciding in its absence), expose payment
  facilities (*facilidades de pago*), and record TGR/SEFIN-agreement banks
  as the payment places, under the CT extinction-mode catalog (payment,
  offset and assignment, merger of parties, condonation — only by statute,
  prescription, abandonment). (LB-015; EV03:EVID-035)
- **HN-TAX-FR-039:** The system shall support *compensación* (offset) of tax
  obligations against tax credits only where the credits are liquid, due and
  not prescribed — on petition or ex officio — and *cesión* (assignment) of
  credits per CT Art. 142 (consumed by the 22-A credit ledger, cluster T4,
  by id). (LB-015; EV03:EVID-035)
- **HN-TAX-FR-040:** The system shall compute prescription horizons per
  obligation — 4 years for customs-regime operations, 5 years for
  RTN-inscribed taxpayers, 7 years otherwise — with a 3-year suspension for
  heirs' refund petitions, and shall record interruption events (e.g.
  notification of the start of determination) resetting the horizon; the
  5-year RTN horizon is the default credit-ledger expiry for retention
  credit documents. (LB-015; EV03:EVID-035)

### 3.9 Sanctions, mora and recourse (T11)

- **HN-TAX-FR-041:** The system shall compute formal-infraction multas from
  the Art. 160.1 table — gross-annual-income bands (L0.01-250k; 250k-500k;
  500k-1M; 1M-5M; 5M-10M; 10M-50M; 50M-100M; >100M) × the SMM *promedio*
  (10%, 25%, 50%, 1, 2, 5, 10, and 10 SMM + 1% SMM per additional L500k
  respectively) — resolving the SMM *promedio* as a dated row per D-H2,
  marking formal multas as interest-free, and opening the ≥10-business-day
  rectification window (with spontaneous-cure reduction per Art. 162)
  before the sanction hardens. (LB-016; EV03:EVID-036; OQ-003)
- **HN-TAX-FR-042:** The system shall compute the late/missing ISR
  declaration sanction as a non-cumulative percentage of tax caused by
  elapsed month — 5% (month 1), 10% (month 2), 15% (month 3), 20% (month 4),
  25% (month 5 and later) — each band prorated to days elapsed
  ("proporcional a los días transcurridos"; denominator unpinned — encoded
  with the OQ-004 marker), extending the same treatment to connected and
  cédular ISR taxes. (LB-016; EV03:EVID-036; OQ-004)
- **HN-TAX-FR-043:** The system shall compute moratory interest on tributes
  and *pagos a cuenta* paid late at 3% monthly or fraction thereof,
  pro-rated, accumulating monthly until payment, capped at 36% of the
  principal (CT Art. 163; R-H6 — superseding any 1%/month SAR/DEI-era
  reference; proration basis for the month fraction = OQ-006).
  (LB-017; EV03:EVID-037; R-H6; OQ-006)
- **HN-TAX-FR-044:** The system shall record RTN suspension when the
  taxpayer is not solvent on firm material obligations after recourse is
  exhausted, and shall expose the suspension state to the facturación
  emission surfaces (cluster E3, S-HN2 wave) and the prescription regime
  (inscribed-5y vs otherwise). (LB-017; EV03:EVID-037)
- **HN-TAX-FR-045:** The system shall track the administrative recourse
  ladder on assessments and sanctions — *Reposición* (same organ, resolution
  within 20 business days), *Apelación* (SEFIN/Superintendence; exhaustion of
  the administrative route), and extraordinary *Revisión* (within 2 years
  against firm resolutions) — with no litigation-guarantee prerequisite
  anywhere (CT Art. 206 void, LB-023/R-H5 — dead text, never an FR).
  (LB-018; EV03:EVID-038)

## 4. Data Model

Machine-readable sidecars (e.g. the formal-multa band table) live next to
this markdown file when produced. Dated statutory values are additive
`valid_from`/`valid_to` rows resolved by the period/hecho-generador date
(D-H2); SMM *promedio* values are consumed from the payroll P1/R-H47 rows
and never recomputed.

**ISR subject profile (per company/partner):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | hn_isr_subject_type | select | domiciled_person · domiciled_company · non_resident · undivided_estate · cargo_administered · transport_presumed | FR-002 |
| res.company | hn_isr_domiciled | boolean | drives scope-regime resolution + Art. 5 tracks (cluster T5 file) | FR-003, FR-004 |
| res.company | hn_isr_exempt_art7 | boolean | substantive-exemption flag; formal duties always on | FR-007 |
| res.company | hn_isr_exemption_category | select | state_entity · nonprofit_charity · church · diplomat_reciprocity · association_union · teacher | FR-007 |
| res.company | hn_public_enterprise | boolean | true → taxable override of state_entity exemption (D. 219-2003) | FR-008 |
| res.company | hn_isr_pagos_a_cuenta_eligible | boolean (computed) | false for labor-income-only retained subjects | FR-009 |
| l10n_hn.isr.scope.regime (new) | regime · valid_from · valid_to | select + dates | worldwide (pre-2017) · territorial (2017-01-01+, proposed R-H66) | FR-004 |
| res.company | hn_taxpayer_category | select + dates | AT Acuerdo Ejecutivo categories (refreshed ≥2y; dated config) | FR-027 |

**Income classification and rate routing (on journal items):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line | hn_isr_income | boolean (computed) | any patrimony-modifying perception (cash/securities/kind/credit) | FR-001 |
| account.move.line | hn_isr_source_status | select | honduran_source_total · honduran_source_partial · foreign_source_out | FR-004, FR-005 |
| account.move.line | hn_isr_source_rule | select | export_goods · import_mirror · other_statutory | FR-005 |
| account.move.line | hn_isr_related_party | boolean | triggers vinculación valuation chain | FR-006 |
| account.move.line | hn_isr_valuation_basis | select | destination_wholesale · comparables_coefficient · at_net_percentage | FR-006 |
| account.move.line | hn_isr_rate_track | select | pj_flat_25 · pn_progressive (`04_isr-withholding.md`) · transport_presumed · gc_unico_10 (cluster T5) | FR-010..013 |
| account.move.line | hn_isr_no_gravable_rule | select null | insurance_payout · state_subsidy · inheritance_legacy_donation · lottery · occupational_ihss · pension_fund · labor_prestaciones · aguinaldo_14th_10smm | FR-014 |

**Fiscal periods, lifecycle and merger:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | hn_special_fiscal_period | boolean + dates | AT-authorized regime row (Art. 26.5 / ISR Art. 27) | FR-016 |
| res.company | hn_exercise_close_reason | select | death · cessation · merger · year_end | FR-017, FR-018 |
| l10n_hn.merger.event (new) | merger_date · absorbed_company_id · surviving_company_id | date · m2o · m2o | closes absorbed exercise; migrates obligations + fiscal credits | FR-018 |
| l10n_hn.lifecycle.duty (new) | type · event_date · due_date | select + dates | start_dj_40d · cessation_dj_60d · departure_isr · death_heirs_isr · dissolution_isr (ISR residues flagged OQ-005) | FR-019, FR-020 |
| l10n_hn.shareholder.informe (new) | fiscal_year · lines (partner, shares, nominal_value, dividend_pct_semester, total_paid) | year · o2m | feeds código 541 (cluster F10) | FR-022 |

**Agents, domicilio, RTN, books:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move / account.payment | hn_retention_trigger_date | date (computed) | earliest-of pago/devengo stamp for retention engines | FR-023 |
| res.partner | hn_retention_agent / hn_collection_agent | boolean | law- or AT-designated agents | FR-024 |
| res.partner | hn_solidary_exposure | select null | heir_portion · third_party_statutory · non_retaining_agent | FR-025 |
| res.partner | hn_single_domicile_lock | boolean (constraint) | one declared domicilio; cascade fields on company/partner | FR-026 |
| res.partner | hn_buzon_enrolled | boolean | notification channel replacing domicilio (SAR-side execution, cluster F1) | FR-033 |
| l10n_hn.book.requirement (new) | company · book_type · active | m2o · select · boolean | niif_full · simplified_farmer_professional · importer_cost_prorrateo · inventory_records | FR-029 |
| account.move | hn_posting_deadline | date (computed) | hecho-generador date + 30 días calendario | FR-028 |
| l10n_hn.oficio.indicia (new) | company · factor · source | m2o · select · char | purchases_rotation · plaza_margins · personal_expenses · patrimony · contracts · interest | FR-030 |

**Cuenta corriente, credits, prescription, sanctions:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.cuenta.corriente (new) | company · obligation_ref · tax · period · kind · origin | m2o · char · select · char · select | kind: debito/credito; origin: autoliquidacion · liquidacion_aceptada · retention · pago · compensacion · cesion · devolucion · feb_depuracion | FR-036 |
| l10n_hn.cuenta.corriente | amount · prescription_date · prescription_basis | monetary · date · select | basis: customs_4y · rtn_inscribed_5y · other_7y; heirs suspension flag | FR-040 |
| l10n_hn.cuenta.corriente | feb_depurable · smm_promedio_snapshot | boolean · monetary | threshold ≤1 SMM promedio, snapshot-on-write (D-H2) | FR-037 |
| l10n_hn.credit.move (new) | credit_id · cession_counterpart · liquid · exigible · not_prescribed | m2o · m2o · booleans | compensación/cesión gates (CT Art. 142) | FR-039 |
| l10n_hn.formal.multa.table (dated data) | income_floor · income_ceiling · base_rule · smm_promedio_id · valid_from/valid_to | monetary · monetary · char · m2o · dates | 8 bands; base_rule = fraction/multiple of SMM promedio (+1% SMM per L500k over L100M) | FR-041 |
| l10n_hn.isr.late.mult (new) | period · due_date · filed_date · band_rate · prorated_amount | dates · selection | bands 5/10/15/20/25%; proration denominator = config (OQ-004) | FR-042 |
| l10n_hn.mora.run (new) | principal · start_date · payment_date · interest · capped | monetary · dates · computed | 3%/month fraction pro-rated, cumulative, ≤36% cap; proration basis = config (OQ-006) | FR-043 |
| res.company | hn_rtn_suspended · hn_rtn_suspension_date | boolean · date | surfaced to emission surfaces (cluster E3) | FR-044 |
| l10n_hn.recourse.tracking (new) | kind · filed_on · resolve_by · status | select + dates | reposicion_20hb · apelacion · revision_2y | FR-045 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No `saas`/`shared` rows are introduced here: none
of these FRs touch a transmission/DTE surface (the only architecture-split
surface per
[saas-thin-client-architecture.md](../../../shared/docs/saas-thin-client-architecture.md));
SAR-side chassis execution (OVI/SW, buzón integration, DJIMR) is owned by
cluster F1 of the S-HN3 wave. Models cited are stable across Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | account.move.line | hn_isr_income (computed) | Income-account mapping feeds the ISR base; recognition independent of form (cash/kind/credit) |
| FR-002 | odoo | res.company / res.partner | hn_isr_subject_type | Partner/company fiscal category; ships/cargo-administered units modeled as company/partner flags |
| FR-003 | odoo | res.company | hn_isr_domiciled | Residency test data entry (manual flag + crew rule default) |
| FR-004 | odoo | l10n_hn.isr.scope.regime | regime, valid_from/valid_to | D-H2: resolved by period date; territorial default from 2017-01-01 pending OQ-001/R-H66 confirmation — reversible row, no code branch |
| FR-005 | odoo | account.move.line | hn_isr_source_status/_rule | Export/import classification defaults by incoterm/partner country; solidarity flag on import mirrors |
| FR-006 | odoo | account.move.line | hn_isr_related_party, hn_isr_valuation_basis | Related-party guard feeds TP worksheets (cluster F10 future); presumption auto-set on below-wholesale declarations |
| FR-007 | odoo | res.company | hn_isr_exempt_art7 + category | Formal-duty grid stays active when exempt |
| FR-008 | odoo | res.company | hn_public_enterprise | Override precedence over exemption flag |
| FR-009 | odoo | res.company | hn_isr_pagos_a_cuenta_eligible (computed) | Consumes payroll income-mix flags (W4); calendar surfaces = F7 |
| FR-010 | odoo | account.move.line | hn_isr_rate_track = pj_flat_25 | Structural routing only; computation in the cluster T3-T7 files |
| FR-011 | odoo | account.move.line | hn_isr_rate_track = pn_progressive | Bracket values resolved from `04_isr-withholding.md` dated rows (D-H2 additive; snapshot per period) |
| FR-012 | odoo | res.company + account.move.line | subject_type=transport_presumed; rate_track | Presumed base = 10% × gross flagged lines |
| FR-013 | odoo | account.move.line | hn_isr_rate_track = gc_unico_10 | Routing only; per-transaction mechanics = cluster-T5 file |
| FR-014 | odoo | account.move.line | hn_isr_no_gravable_rule | 10×SMM promedio caps computed by payroll/withholding surfaces (R-H47 feed) |
| FR-015 | odoo | date.range / account.fiscal.year | — | Calendar-year default; mid-year start handled by company start_date; stable 17-20 |
| FR-016 | odoo | res.company | hn_special_fiscal_period (dated row) | OQ-002 lead; F7 consumes the close date |
| FR-017 | odoo | res.company | hn_exercise_close_reason + date | Short-period run trigger |
| FR-018 | odoo | l10n_hn.merger.event | all | Migration wizard moves cuenta-corriente rows; GL merge native (Odoo 17+ merger tools assist, custom for credits) |
| FR-019 | odoo | l10n_hn.lifecycle.duty | due_date = start + 40d calendario | Calendar-day math (no hábiles conversion) |
| FR-020 | odoo | l10n_hn.lifecycle.duty | type, due_date | 60d CT operative; ISR 90d residues as flagged types (OQ-005) |
| FR-021 | odoo | res.partner (registrar workflow) | solvency-certificate gate field | Awareness-level checkpoint on transfer workflows |
| FR-022 | odoo | l10n_hn.shareholder.informe | all | Dataset export for 541 (cluster F10 owns filing) |
| FR-023 | odoo | account.move / account.payment | hn_retention_trigger_date (computed) | min(invoice_date/accrual, payment_date); consumed by all retention engines (`04_isr-withholding.md`, W4) |
| FR-024 | odoo | res.partner | agent flags | AT-designation data entry |
| FR-025 | odoo | res.partner | hn_solidary_exposure | Posted as liability flags by owner engines |
| FR-026 | odoo | res.partner | hn_single_domicile_lock | SQL constraint single active domicilio record; change requires notification log |
| FR-027 | odoo | res.partner | vat (RTN 14-char) + l10n_latam | RTN validation regex; categorization as dated config (ir.config_parameter keys per cohort) |
| FR-028 | odoo | account.move | hn_posting_deadline | Posted-after-deadline flagged (report), not blocked — statutory bookkeeping discipline monitor |
| FR-029 | odoo | l10n_hn.book.requirement | book_type | Defaults from company activity flags (importer → cost book); NIIF anchor shared with chart-of-accounts topic |
| FR-030 | odoo | l10n_hn.oficio.indicia | factor | Scenario worksheet only — AT-side determination input |
| FR-031 | odoo | account.move (retention entries) | entero due-date resolver | Deadline registry: default 10d calendario; per-instrument exceptions keyed by engine (T6/F2) |
| FR-032 | odoo | account.move | comprobante-required flag | Voucher emission = cluster E6 (S-HN2); here only the duty flag |
| FR-033 | odoo | res.partner | hn_buzon_enrolled | Informational; SAR integration = cluster F1 (S-HN3) |
| FR-034 | odoo | l10n_hn.cuenta.corriente | origin=devolucion | Refund petition workflow; approval AT-side |
| FR-035 | odoo | l10n_hn.cuenta.corriente | rectification gate | Reduction/credit-increase entries parked as pending-AT (no GL release); D-H2.5 freeze |
| FR-036 | odoo | l10n_hn.cuenta.corriente | all | Mirror ledger of SAR's cuenta corriente; débitos/créditos reconciliation report |
| FR-037 | odoo | l10n_hn.cuenta.corriente | feb_depurable, smm_promedio_snapshot | February job marks dischargeable rows; promedio from P1 dated rows (never recompute, R-H47/R-H12) |
| FR-038 | odoo | account.payment | imputation + place | Payment same-day default on autoliquidación postings; facilidades = installment plan flag |
| FR-039 | odoo | l10n_hn.credit.move | gates | Offset/assignment postings gated by liquid+exigible+not-prescribed checks; 22-A consumer = T4 by id |
| FR-040 | odoo | l10n_hn.cuenta.corriente | prescription_date/basis | Interruption events (assessment notifications) reset; D-H3: prior-years aggregates re-export on demand within window |
| FR-041 | odoo | l10n_hn.formal.multa.table | dated data rows | SMM promedio FK; band resolution by gross income as-of period (D-H2); rectification window timer |
| FR-042 | odoo | l10n_hn.isr.late.mult | band computation | Denominator configurable pending OQ-004 (03_ OQ-4 marker preserved) |
| FR-043 | odoo | l10n_hn.mora.run | computed | 3% monthly cumulative, fraction pro-rated (basis config, OQ-006), 36% cap; R-H6 — reject any 1%/month legacy feed |
| FR-044 | odoo | res.company | hn_rtn_suspended | Blocks emission-surface hooks (cluster E3 contract); prescription basis switch |
| FR-045 | odoo | l10n_hn.recourse.tracking | ladder statuses | 20-días-hábiles timer needs the HN business-day calendar (shared with FR-041 window); no guarantee-deposit field exists — Art. 206 void (LB-023) |

Version-regime notes (D-H2/D12): FR-004 carries the 2017-01-01 regime
cutover row; FR-011/FR-014/FR-037/FR-041 resolve dated parameters (scale
rows, SMM promedio) as-of the period/hecho-generador date with
snapshot-on-write (D15); FR-035 enforces the filed-period freeze (D-H2.5);
FR-018/FR-040 interact with the D-H3 ingestion contract (prior-year
aggregates re-exportable within the prescription window). No cross-border
payroll/FX surfaces are introduced in this file; FX anchoring follows the
computation files of this directory when they pin their own anchors.

## 6. Acceptance Criteria

- **AC-001:** Given a journal line booking a barter delivery (in-kind
  perception) that increases the company's patrimony, when classified, then
  hn_isr_income = true for the line (income recognized regardless of form)
  (FR-001).
- **AC-002:** Given a foreign-domiciled company holding a State concession
  with a Honduras address, when registered, then it is an ISR subject with
  hn_isr_subject_type set and the domiciled flag per FR-003's test (FR-002).
- **AC-003:** Given a crew member of a Honduran-flag merchant ship, when the
  residency test runs, then the crew member resolves as resident/domiciled
  (FR-003).
- **AC-004:** Given a domiciled company receiving a foreign-source dividend
  in ejercicio 2026, when the scope regime resolves, then the regime row for
  2026 = territorial (valid_from 2017-01-01) and the dividend is classified
  foreign_source_out of the ISR base; given the same facts in ejercicio 2015,
  then the worldwide row applies and the dividend enters the base (FR-004,
  OQ-001 marker recorded).
- **AC-005:** Given an export of goods bought and treated in Honduras, when
  classified, then hn_isr_source_status = honduran_source_total and the gross
  valuation uses the destination wholesale price less cost, transport and
  insurance (FR-005).
- **AC-006:** Given an export invoiced below the destination wholesale price
  without proof to the contrary, when the valuation runs, then
  hn_isr_related_party = true (vinculación presumption) and the destination
  wholesale price governs; with a comparable-company coefficient on file,
  then hn_isr_valuation_basis = comparables_coefficient (FR-006).
- **AC-007:** Given a municipal establishment flagged state_entity exempt
  that operates as an *empresa pública*, when the exemption resolves, then
  hn_public_enterprise forces taxable status while formal duties remain
  active in both states (FR-007, FR-008).
- **AC-008:** Given a natural person whose only income is a salary fully
  subject to monthly withholding, when pagos-a-cuenta eligibility computes,
  then hn_isr_pagos_a_cuenta_eligible = false (FR-009).
- **AC-009:** Given a domiciled *persona jurídica*, when the rate track
  resolves, then hn_isr_rate_track = pj_flat_25 with no bracket lookup
  (values consumed by the computation files, never restated here) (FR-010).
- **AC-010:** Given a foreign transport company with L1,000,000 gross
  Honduran-source income, when the presumed-net regime runs, then the
  presumed base = L100,000 and the 25% tariff applies to that base (FR-012).
- **AC-011:** Given a company starting activities on 15-April, when the
  exercise computes, then its first annual exercise runs 15-April through
  31-December (FR-015).
- **AC-012:** Given an absorption effective 10-June where the absorbed
  company holds unpaid obligations and a firm retention credit, when the
  merger processes, then the absorbed exercise closes 10-June and BOTH the
  obligations and the credit migrate to the survivor's cuenta corriente
  (FR-018, FR-036).
- **AC-013:** Given activities starting 1-March, when the lifecycle duty
  schedules, then the start DJ due date = 10-April (40 días calendario)
  (FR-019).
- **AC-014:** Given cessation on 20-February, when the lifecycle duty
  schedules, then the cessation DJ + payment due date = 21-April (60 días
  calendario, CT operative rule; no ISR 90-day residue type for plain
  cessation) (FR-020, OQ-005).
- **AC-015:** Given a retentable service accrued (devengo) 20-May and paid
  5-June, when the retention stamps, then hn_retention_trigger_date = 20-May
  and the entero month = May (due within the first 10 calendar days of
  June) (FR-023, FR-031).
- **AC-016:** Given a taxpayer with a declared domicilio, when a second
  concurrent domicilio declaration is attempted, then the write is rejected
  by the single-domicile constraint and a change-notification log entry is
  required instead (FR-026).
- **AC-017:** Given an operation whose hecho generador occurred 31-January,
  when posting on 5-March, then the entry is flagged as posted after the
  30-day statutory window (deadline 2-March) (FR-028).
- **AC-018:** Given a firm credit balance of L13,000 on 1-February-2026 with
  the depuración threshold resolved at L13,985.16 (the SAR-43-2026 anchor per
  R-H12), when the February depuración job runs, then the credit is marked
  feb_depurable = true; given L15,000, then feb_depurable = false (FR-037).
- **AC-019:** Given an ISR declaration with tax caused due 30-April-2026 and
  filed 15-July-2026, when the late sanction computes, then the band = month
  3 (15%), prorated to days elapsed under the configured denominator
  (OQ-004 marker attached to the result) (FR-042).
- **AC-020:** Given an unpaid cuota of L10,000 due 30-June paid on 15-October
  (3 full months + fraction), when mora computes, then interest accumulates
  3% per elapsed month plus the pro-rated fraction (basis per OQ-006 config)
  and the total never exceeds 36% of the principal (L3,600) (FR-043).
- **AC-021:** Given a formal infraction by a taxpayer with gross annual
  income L3,000,000 resolved in 2026, when the multa computes, then the band
  resolves to 1 × SMM promedio, a ≥10-business-day rectification window
  opens before the sanction hardens, and the multa line carries no interest
  (FR-041).
- **AC-022:** Given a firm material obligation unpaid after reposición and
  apelación are exhausted, when the enforcement state updates, then
  hn_rtn_suspended = true and the facturación emission surfaces (cluster E3
  contract) read the blocked state; given payment in full, the suspension
  lifts (FR-044).
- **AC-023:** Given an assessment contested by reposición filed 1-March,
  then the resolution deadline = 20 business days later on the HN
  business-day calendar, and no guarantee deposit is requested or recorded
  anywhere in the recourse flow (CT Art. 206 void — LB-023/R-H5) (FR-045).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Territoriality conflict (origin `03_ OQ-1`, register C1): CT Art. 1.2 "renta territorial" (2016) vs Ley ISR Art. 2 worldwide text (1963, unreformed) for foreign-source income of domiciled persons. Proposed master-index ruling R-H66 presented by this synthesis for controller confirmation — operative scope modeled as territorial from 2017-01-01 (lex posterior; CT as general chassis applicable to all tributes; no foreign-tax-credit mechanism anywhere in the Ley ISR, making an operative worldwide base incoherent; modern architecture (Art. 3 fuente rules, Art. 5 non-resident schedule, retention-based collection) wholly source-based; DTA-authorization clause read as treaty-level, not domestic scope). FR-004 encodes the dated regime row as reversible — neither text applied silently. Awaiting controller ruling. | no (flag default reversible) | controller (ruling R-H66) | open |
| OQ-002 | Special fiscal period instrument (origin `03_ OQ-2`): CT Art. 26.5 authorizes AT-approved special periods and ISR Art. 27 requires prior written notice, but the conditions/procedure instrument (acuerdo) is unacquired. FR-016 carries the regime row; low priority. | no | Takumi S-HN1 (acquisition queue) | open |
| OQ-003 | Art. 160 multa-table vintage (origin `03_ OQ-3`): the 03_ consolidation stops at D. 180-2020 and the SAR catalog shows no later CT reform except the 89_ interpretation — verify no post-2020 instrument altered the income bands or SMM fractions before freezing the table data. | no | Takumi S-HN1 | open |
| OQ-004 | ISR-late pro-diem denominator (origin `03_ OQ-4`): "5% del impuesto causado... proporcional a los días transcurridos" — the denominator (days of the elapsed month? 30?) is unstated; FR-042 encodes the bands with a configurable denominator and preserves the marker; check SAR Ayudas 102/103 practice at the S-HN3 wave. | no | Takumi S-HN3 (Ayudas 102/103) | open |
| OQ-005 | NEW (synthesis finding): Ley ISR Arts. 36-37 (1963) set 90-day deadlines (cessation DJ + certified balance; departure; heirs on death; society dissolution) while CT Art. 68 (2017) sets 60 días calendario for the cessation DJ. FR-020 encodes the CT 60-day rule as operative for cessation (lex posterior + R-H13 procedural locus) with the ISR 90-day residues carried for the events CT does not cover — verify against practice/any consolidating reform whether the 90-day items were displaced too. | no | Takumi S-HN1 + controller | open |
| OQ-006 | NEW (synthesis finding): mora month-fraction proration basis — CT Art. 163 charges "3% mensual o fracción de mes" (R-H6: fraction pro-rated) but the proration denominator (calendar days of the month vs 30-day commercial month) is unstated; FR-043 encodes a configurable basis; confirm vs SAR cuenta-corriente statements. | no | Takumi S-HN1 | open |
