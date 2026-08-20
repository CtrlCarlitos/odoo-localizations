# GT — Taxation — ISR actividades lucrativas, capital, no-residentes & facturas especiales

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala *Impuesto
Sobre la Renta* (ISR, income tax) under the Ley de Actualización Tributaria
(LAT) Libro I outside the employment title: the renta/régime taxonomy and
régime lifecycle (Arts. 2, 14, 50-51, 174, 180-181); the Régimen Sobre las
Utilidades (25% annual with quarterly advance payments, the 8%-of-gross
presumptive option, the "sujeto a pagos trimestrales" invoice legend and
the NO-multi-year-NOL absence finding); the Régimen Opcional Simplificado
(5%/7% monthly on gross collected through payer retention, Q30,000 split,
Q2,500 per-operation floor); the Art. 21 deduction caps matrix, Art. 23
no-deductibles with the retention↔deduction gating, Art. 24 thin-cap
interest limitation and the Arts. 25-28 straight-line depreciation table;
rentas y ganancias de capital (10% definitive, dividends 5%, 30% presumed
expenses for lessors, 2-year same-nature loss fencing); no-residentes
without permanent establishment (5/3/10/15/25 definitive retention matrix,
10-day cycles); and the facturas especiales ISR retention (5% definitive,
Art. 16). Rate/bracket data lives in the CSV sidecar `isr_rates.csv`.

It does **not** cover: rentas del trabajo in relación de dependencia
(withholding algorithm, Art. 73 scale, Q48,000/Q12,000 — Task 4 file
`04_isr-trabajo.md`, FR-111..146, cited by FR id); the IVA-side retention
matrix D-20-2006/AG 425-2006 and the IVA half of facturas especiales
(Task 3 file `03_iva-retenciones.md` — cross-lock via 23_ Art. 52/52"A",
EVID-177); the pequeño contribuyente regime (IVA-side only — Task 2 file;
the LAT creates NO ISR pequeño regime, FR-148 guard); Código Tributario
sanctions on retention agents (Task 6 — CT 94.7/94.9/94.18/94"A" hooks via
FR-168); the payroll-side dietas/deducibilidad holdings of Criterio 6-2018
beyond what this file cites as interpretive layer; declaration form
generation (F-wave — form identities cited from 48_ per R46); or FEL DTE
mechanics (`gt/requirements/e-invoicing/`).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): **ISR =
26_ LAT D-10-2012 consolidated through Dto. 46-2022 (27-09-2022) governs;
28_ AG 213-2013 develops; 47_ = self-disclaimed SAT digest — 26_ > 28_ >
47_, law wins every delta.** Residual post-27-09-2022 window unverified
(GOQ-58 caveat on every dated value, and expressly on the NOL absence
finding, FR-158). 28_ prints no DCA publication date and its stamps stop
at AG 167-2014 (06-06-2014): every 28_-anchored row carries the GOQ-59
caveat. Form identities cite 48_/RetWeb (R46), never the digest. Dated
values follow the dated-instrument regime D15/D16 (cite together):
valid_from/valid_to rows + instrument provenance; rate/cap rows are
decree-bound, never constants.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Actualización Tributaria, Decreto Número 10-2012 (texto consolidado, última reforma impresa: Dto. 46-2022 del 27-09-2022): "DECRETO NÚMERO 10-2012"; stamps: "*Reformado el primer párrafo, por el Artículo 4, del Decreto Del Congreso Número 4-2019 el 08-05-2019" (art. 16); "*Adicionado por el Artículo 13, del Decreto Del Congreso Número 46-2022 el 27-09-2022" (art. 53 Bis) | LAT D-10-2012 as consolidated through D-46-2022 (emitted 16-Feb-2012, sanctioned 1-Mar-2012): the governing ISR instrument; operative Libro I reform instruments 19-2013 (bulk), 14-2013, 2-2020, 46-2022; residual post-27-09-2022 window unverified (GOQ-58) | `gt/sources/26_LAT_10-2012.pdf` | p.1 title block; p.64 date block; marginal stamps (EVID-216) |
| LB-002 | D-10-2012, Arts. 2/14/180/181: "Se gravan las siguientes rentas según su procedencia: 1. Las rentas de las actividades lucrativas. 2. Las rentas del trabajo. 3. Las rentas de capital y las ganancias de capital." (art. 2) / "Se establecen los siguientes regímenes para las rentas de actividades lucrativas: 1. Régimen Sobre las Utilidades de Actividades Lucrativas. 2. Régimen Opcional Simplificado Sobre Ingresos de Actividades Lucrativas." (art. 14) / "Se derogan: 1. El Decreto Número 26-92 [sic spacing] del Congreso de la República, Ley del Impuesto Sobre la Renta, y sus reformas…" (art. 180.1) / "El Impuesto Sobre la Renta contenido en el Libro I de esta Ley, el cual entrará en vigencia el uno (1) de enero de dos mil trece (2013)." (art. 181.1) | The ISR taxonomy: three renta categories (lucrativas / trabajo / capital+ganancias) × two lucrativas regimes (Utilidades = general; Opcional Simplificado = 5%/7%); old D-26-92 (and D-26-95) died 1-Jan-2013 with ISR Libro I vigente that day; the LAT creates NO ISR pequeño contribuyente regime (pequeño remains IVA-side registration) | `gt/sources/26_LAT_10-2012.pdf` | p.2 arts. 1-2; p.9 art. 14; pp. 63-64 arts. 180-181 (EVID-217) |
| LB-003 | D-10-2012, Arts. 8/11/87: art. 8: "Están exentos del impuesto: 1. Los organismos del Estado… 2. Las universidades legalmente autorizadas… 3. Los centros educativos privados… exclusivamente en las rentas derivadas de: matrícula de inscripción, colegiaturas y derechos de examen… 4. Las herencias, legados y donaciones por causa de muerte… 5. Las rentas que obtengan las iglesias, exclusivamente por razón de culto." / art. 11.1: no-lucrativas exempt "únicamente por la parte que provenga de donaciones o cuotas ordinarias o extraordinarias… las rentas obtenidas… en el desarrollo de actividades lucrativas mercantiles, agropecuarias, financieras o de servicios…" están gravadas; art. 11.2 cooperativas con asociados vs terceros / art. 87: state/international subsidies (salud, vivienda, educación, alimentación); "enajenación ocasional de bienes muebles de uso personal" (except registered vehicles/vessels/aircraft) | ISR exemptions are PARTIAL per entity: exempt classes keep retention/formal obligations ("sin perjuicio de las obligaciones contables, formales o de retención"); universities/centros educativos exempt only on the education revenue stream (ancillary businesses gravadas); cooperatives only with members; Art. 87 capital-side exemptions. Exemption windows are per-beneficiary facts, never global flags | `gt/sources/26_LAT_10-2012.pdf` | pp. 6-7 art. 8; p.8 art. 11; p.39 art. 87 (EVID-218) |
| LB-004 | D-10-2012, Art. 21 (caps): num. 4 ¶2: "La deducción máxima por sueldos pagados a los socios o consejeros de sociedades civiles y mercantiles, cónyuges, así como a sus parientes dentro de los grados de ley, se limita a un monto total anual del diez por ciento (10%) sobre la renta bruta." / num. 5: "Tanto el aguinaldo como la bonificación anual para los trabajadores del sector privado y público (bono 14), serán deducibles hasta el cien por ciento (100%) del salario mensual, salvo lo establecido en los pactos colectivos…" / num. 6: cuotas patronales IGSS/IRTRA/INTECAP "y otras cuotas o desembolsos obligatorios establecidos por ley" / num. 8: indemnizaciones "hasta el límite del ocho punto treinta y tres por ciento (8.33%) del total de las remuneraciones anuales" / num. 20: incobrables "no podrá exceder del tres por ciento (3%) de los saldos deudores de cuentas y documentos por cobrar" / num. 22: donaciones a asociaciones-fundaciones/iglesias/partidos "no puede exceder del cinco por ciento (5%) de la renta bruta, ni de un monto máximo de quinientos mil Quetzales (Q.500,000.00) anuales" / num. 23: asesoría desde el exterior "no debe exceder del cinco por ciento (5%) de la renta bruta" / num. 24: viáticos "no debe exceder el tres por ciento (3%) de la renta bruta" / num. 25: regalías "en ningún caso debe exceder del cinco por ciento (5%) de la renta bruta" / num. 27: gastos de organización "se amortizan mediante cinco (5) cuotas anuales, sucesivas e iguales" | The authorized-deduction caps matrix, verbatim: related-party sueldos 10% of renta bruta (annual total); aguinaldo + bono 14 each ≤ 100% of one monthly salary (unless pacto colectivo); IGSS/IRTRA/INTECAP employer quotas fully; indemnizaciones ≤ 8.33% of annual remunerations; bad-debt reserve ≤ 3% of receivable balances; donations ≤ 5% of renta bruta and ≤ Q500,000.00/year; foreign advisory ≤ 5%; viáticos ≤ 3%; royalties ≤ 5%; organization costs amortized in 5 equal annual installments | `gt/sources/26_LAT_10-2012.pdf` | pp. 10-14 art. 21 nums. 4/5/6/8/20/22/23/24/25/27 + reform stamps (EVID-219) |
| LB-005 | D-10-2012, Art. 23 (no deducibles): a) gastos ajenos al negocio (oficio prorratea si no hay cuentas separadas); c) "Los que el titular de la deducción no haya cumplido con la obligación de efectuar la retención y pagar el Impuesto Sobre la Renta, cuando corresponda. Serán deducibles una vez se haya enterado la retención."; f) sueldos sin planilla IGSS; h) bonificaciones sobre utilidades a directivos/gerentes; i) dividendos/participaciones; j) retiros del propietario; q) bienes uso mixto "sólo se considerará deducible, salvo prueba en contrario, el cincuenta por ciento (50%)"; r) depreciación de inmuebles sobre valor que exceda matrícula fiscal/catastro / Art. 24 (thin cap): "el monto deducible por dicho concepto no podrá exceder al valor de multiplicar la tasa de interés referida en los párrafos siguientes por un monto de tres veces el activo neto total promedio…"; tasa = Junta Monetaria tasa simple máxima anual (publicada enero y julio); promedio = (cierre año anterior + cierre actual)/2; exclusion: "entidades bancarias y sociedades financieras… y a las cooperativas legalmente autorizadas" | No-deductible catalog + deduction gating: expenses non-deductible until the corresponding ISR retention is entered (23.c — the retention↔deduction dependency) and salaries off the IGSS planilla non-deductible (23.f); mixed-use assets 50% presumption; thin-cap: deductible interest ≤ JM maximum annual simple rate × 3 × average total net equity, banks/finance companies/cooperativas excluded. JM reference-rate values are external to the corpus | `gt/sources/26_LAT_10-2012.pdf` | pp. 15-17 arts. 23-24 (EVID-220) |
| LB-006 | D-10-2012, Arts. 25-28: art. 27: "el cálculo de la depreciación se hará usando el método de línea recta…" (other methods only with SAT authorization); art. 26: inmuebles base = "el valor más reciente que conste en la matrícula fiscal o en el catastro municipal, el que sea mayor. En ningún caso se admite depreciación sobre el valor de la tierra. Cuando no se precise el valor del edificio y mejoras, se presume… que éste es equivalente al setenta por ciento (70%) del valor total del inmueble, incluyendo el terreno."; art. 28 table: "1. Edificios, construcciones e instalaciones… cinco por ciento (5%). 2. Árboles, arbustos, frutales… quince por ciento (15%). 3. Instalaciones no adheridas… buques-tanques, barcos y material ferroviario… veinte por ciento (20%). 4. Los semovientes… maquinaria, vehículos en general… veinte por ciento (20%). 5. Equipo de computación, treinta y tres punto treinta y tres por ciento (33.33%). 6. Herramientas, porcelana, cristalería… veinticinco por ciento (25%). 7. Reproductores de raza… veinticinco por ciento (25%). 8. Para los bienes muebles no indicados… diez por ciento (10%)." | Depreciation: straight-line statutory maxima by asset class (5/15/20/20/33.33/25/25/10%); land never depreciated; real-estate base = the higher of matrícula fiscal / catastro municipal value; 70% building presumption when the building/land split is unknown | `gt/sources/26_LAT_10-2012.pdf` | pp. 17-18 arts. 25-28 (EVID-221) |
| LB-007 | D-10-2012, Arts. 36-42: art. 36: "…aplican a la base imponible determinada el tipo impositivo del veinticinco por ciento (25%)." / art. 37: período "principia el uno (1) de enero y termina el treinta y uno (31) de diciembre" / art. 38: "deben realizar pagos trimestrales", opción 2: "renta imponible estimada en ocho por ciento (8%) del total de las rentas brutas… en el trimestre respectivo, excluidas las rentas exentas" (art. 21-Bis air-transport taxpayers use 15%); "El pago del impuesto trimestral se efectúa por medio de declaración jurada y lo enterará dentro del mes siguiente a la finalización del trimestre… El pago del impuesto correspondiente al cuarto trimestre se realizará juntamente con la declaración de liquidación definitiva anual." / art. 39: annual DJ "dentro de los primeros tres (3) meses del año calendario" / art. 42.1: invoices carry the frase "sujeto a pagos trimestrales"; art. 42.3: inventories at 30-Jun & 31-Dec reported in January and July | Régimen Utilidades package: 25% on net income (2015+; transitional 31/28 — LB-008), annual calendar-year period, quarterly advance payments by DJ paid within the month following each quarter (real partial closings OR 8%-of-quarterly-gross presumptive excluding exempt rentas; 15% for air transport per art. 21 Bis), Q4 paid together with the annual DJ filed in the first 3 months; mandatory invoice legend; biannual inventory reporting | `gt/sources/26_LAT_10-2012.pdf` | pp. 22-24 arts. 36-42 + stamps 19-2013/2-2020 (EVID-222) |
| LB-008 | D-10-2012, Arts. 172-173: art. 172: "1. Para el período de liquidación del uno (1) de enero al treinta y uno (31) de diciembre de dos mil trece (2013), el tipo impositivo será el treinta y uno por ciento (31%). 2. …dos mil catorce (2014)… veintiocho por ciento (28%). 3. Para los períodos de liquidación del uno (1) de enero de dos mil quince (2015) en adelante, el tipo impositivo será el contenido en la Sección III…" / art. 173: "1. Del uno (1) de enero al treinta y uno (31) de diciembre de dos mil trece (2013) el tipo impositivo será de seis por ciento (6%). 2. A partir del uno (1) de enero de dos mil catorce (2014) en adelante… el contenido en la Sección IV…" (stamp: reformado por art. 25, Dto. 19-2013) | Transitional rate history: Utilidades 31% FY2013 / 28% FY2014 / 25% from FY2015; Opcional Simplificado upper bracket 6% in 2013 / 7% from 2014 — 31% is NOT the current rate (guard) | `gt/sources/26_LAT_10-2012.pdf` | p.62 arts. 172-173 (EVID-223) |
| LB-009 | D-10-2012, Arts. 43-49: art. 44 table: "Rango de renta imponible mensual / Importe fijo / Tipo impositivo de / Q.0.01 a Q.30,000.00 | Q.0.00 | 5% sobre la renta imponible / Q.30,000.01 en adelante | Q.1,500.00 | 7% sobre el excedente de Q.30,000.00" / art. 45: "el período de liquidación es mensual." / art. 46: "liquidan y pagan el impuesto por medio de retenciones que le efectúen quienes realicen el pago o acreditación en cuenta…" (direct payment only with SAT authorization resolved ≤15 días; invoice must state "que pagan directamente el impuesto a la Administración Tributaria, identificando la autorización respectiva") / art. 47: retention agents (contabilidad completa, Estado, asociaciones, fideicomisos…) / art. 48: retention = "El cinco por ciento (5%) sobre el monto de hasta treinta mil quetzales (Q.30,000.00) y el siete por ciento (7%) sobre el monto que exceda los treinta mil quetzales" + per-op floor: "cuando les presten servicios o hagan compras de bienes por un valor menor a dos mil quinientos quetzales (Q.2,500.00), excluyendo el Impuesto al Valor Agregado, no están obligados a practicar la retención" + no retention to direct-payment-authorized or Régimen Utilidades taxpayers; constancia "dentro de los primeros cinco (05) días del mes inmediato siguiente"; enterar + anexo (nombre, NIT, valor, retención) "dentro del plazo de los primeros diez (10) días del mes siguiente" / art. 49: monthly DJ "dentro del plazo de los primeros diez (10) días del mes siguiente" + "En los primeros tres (03) meses de cada año… declaración jurada anual informativa." | Opcional Simplificado: monthly two-bracket scale on gross income (renta bruta menos exentas, IVA excluded) — 5% ≤ Q30,000.00 / Q1,500.00 + 7% over; collection mechanism IS retention by payers (agents per art. 47); Q2,500 per-operation retention floor (IVA excluded); 5-day constancia, 10-day enter + monthly DJ, annual informative DJ in Q1 | `gt/sources/26_LAT_10-2012.pdf` | pp. 24-25 arts. 43-49 (EVID-224) |
| LB-010 | D-10-2012, Arts. 50-51/174: art. 50: taxpayers "deben indicar a la Administración Tributaria, el régimen que aplicarán, de lo contrario la Administración Tributaria los inscribirá en el Régimen Sobre las Utilidades de Actividades Lucrativas." / art. 51: "pueden cambiar de régimen previo aviso… durante el mes anterior al inicio de la vigencia del nuevo período anual de liquidación. El cambio de régimen se aplica a partir del uno (1) de enero del año siguiente." / art. 174: pre-LAT taxpayers migrated (44/44"A" → Opcional de oficio or Utilidades; art. 72 → Utilidades de oficio or Opcional) | Régime lifecycle: election at inscription with DEFAULT = Utilidades when silent; régime change only by aviso in the month before the annual period starts (in practice December), effective the following 1-Jan; no monetary threshold gates either ISR régime (the only quantitative hook is the Q30,000 rate split inside Opcional) | `gt/sources/26_LAT_10-2012.pdf` | p.26 arts. 50-51; p.62 art. 174 (EVID-225) |
| LB-011 | D-10-2012, Arts. 83-89: art. 84 classification: 1. capital inmobiliario (arrendamiento/subarrendamiento/cesión de uso de inmuebles, giro no habitual); 2. capital mobiliario (intereses y rentas de créditos; arrendamiento de muebles tangibles e intangibles — derechos de llave, regalías, derechos de autor; rentas vitalicias, seguros; "La distribución de dividendos, ganancias y utilidades"); 3. ganancias y pérdidas de capital (enajenación fuera de giro habitual; revaluaciones; activo fijo); 4. loterías, rifas, sorteos, bingos / art. 88 num. 2: base = renta "menos un treinta por ciento (30%) de esa renta en concepto de gastos, salvo prueba en contrario" (DJ en enero si gasto mayor + solicitud de devolución) / art. 89: ganancia = precio de enajenación − costo; transaction costs (comisiones, notariales, registro) deductible "hasta… el quince por ciento (15%) del valor de la enajenación" (uncapped with contabilidad completa + documentation); acciones/participaciones cost = documented acquisition value or book value certificado por la emisora (num. 3, reformed 19-2013) | Capital taxonomy and bases: four classes (inmobiliario, mobiliario incl. dividends, ganancias/pérdidas de capital, loterías); lessors of real estate apply a flat 30% presumed-expense deduction (base = 70% of rent) unless greater actual expense proven by January DJ; capital gain = price − cost with transaction costs ≤ 15% of the enajenación value (cap waived with full accounting + documentation); shares at certified book value | `gt/sources/26_LAT_10-2012.pdf` | pp. 37-40 arts. 83-89 (EVID-230) |
| LB-012 | D-10-2012, Arts. 90-96: art. 92: "El tipo impositivo aplicable a la base imponible de las rentas de capital mobiliarias e inmobiliarias y para las ganancias de capital es del diez por ciento (10%)." / art. 93: "El tipo impositivo para la distribución de dividendos, ganancias y utilidades… es del cinco por ciento (5%)." (banking groups: retention only on distribution to shareholders of the controlling entity) / art. 91: pérdidas de capital "solamente se pueden compensar con ganancias futuras de la misma naturaleza, hasta por un plazo máximo de dos (2) años… La pérdida no compensada no da derecho… a deducción o crédito alguno… Si al concluir dicho plazo aún existe un saldo… ya no puede compensarse por ningún motivo." / art. 90: capital rentas "sujetas a retención definitiva desde el momento en que se haga efectivo el pago, acreditamiento o abono bancario" (except payments to banks/financieras/cooperativas supervised by SIB) / art. 94: retention + DJ "dentro del plazo de los primeros diez (10) días del mes inmediato siguiente a aquel en que se efectuó el pago o acreditamiento bancario" / art. 95: no-retention case → self-pay within 10 days; ganancias de capital → 10 days of month following surgimiento / art. 96: compensation DJ "dentro del plazo de los tres (3) meses siguientes al término del año calendario" | Capital rates & loss fencing: 10% flat definitive on all rentas de capital + ganancias de capital; 5% definitive on dividends; capital losses carry forward only against same-nature gains and only 2 years, then dead — never against ordinary/giro income; retention definitive at payment/credit/bank-credit moment with the SIB-supervised carve-out; all cycles on the 10-day month-following rule; loss-compensation DJ within 3 months of year end | `gt/sources/26_LAT_10-2012.pdf` | p.41 arts. 90-96 (EVID-231) |
| LB-013 | D-10-2012, Arts. 97-107 (no residentes sin establecimiento permanente): art. 104: "1. …cinco por ciento (5%): a. transporte internacional…; b. primas de seguros, fianzas, reaseguros, retrocesiones, reafianzamientos; c. telefonía, transmisión de datos y comunicaciones internacionales; [d. Derogado por 19-2013]; e. dividendos, reparto de utilidades… y toda transferencia o acreditamiento en cuenta a sus casas matrices en el extranjero, sin contraprestación" + excepción: "el tipo impositivo del tres por ciento (3%) por el suministro de noticias internacionales… y por la utilización en Guatemala de películas cinematográficas… grabaciones musicales…"; "2. …diez por ciento (10%): a. Los intereses… pagados o acreditados a no residentes" (excepción: préstamos de bancos/financieras reguladas en su país de origen y multilaterales); "3. …quince por ciento (15%): a. sueldos y salarios, dietas, comisiones, bonificaciones…; b. deportistas y artistas…; c. Las regalías…; d. Los honorarios. e. El asesoramiento científico, económico, técnico o financiero."; "4. …veinticinco por ciento (25%): Otras rentas gravadas no especificadas." / art. 105: pagadores con contabilidad completa "deben retener el impuesto con carácter definitivo… y enterarlo mediante declaración jurada… dentro del plazo de los primeros diez (10) días del mes inmediato siguiente" / art. 103: base = amount effectively paid/credited per operation, "sin que sea posible compensación alguna entre éstas" / arts. 106-107: self-liquidation 10 days if not retained; retention detail DJ same 10-day rule | Non-resident rate matrix (all retentions definitive, per-payment isolation, no cross-compensation): 5% transport/insurance/telecom/dividends-and-home-office transfers (3% exception for international news and films/music recordings); 10% interest (exempt when from regulated foreign banks/multilaterals); 15% salaries/dietas/commissions, athletes/artists, royalties, honorarios, scientific/economic/technical/financial advisory; 25% residual; payers with full accounting retain and enter by DJ within the first 10 días of the following month; with EP → Title II rules apply (art. 102) | `gt/sources/26_LAT_10-2012.pdf` | pp. 43-45 arts. 97-107 (EVID-232) |
| LB-014 | D-10-2012, Arts. 16-17: art. 16 (párrafo 1 reformado por Dto. 4-2019, 08-05-2019): emitters of facturas especiales "deberán retener, con carácter de pago definitivo, el Impuesto Sobre la Renta, aplicando el tipo impositivo del cinco por ciento (5%) sobre el valor de la factura sin incluir el Impuesto al Valor Agregado"; copy of the factura especial = constancia de retención; enterar con DJ de retenciones + anexo "dentro de los primeros diez (10) días del mes siguiente" / art. 17: "Cuando el profesional universitario haya percibido renta y no esté inscrito como contribuyente, o esté inscrito pero no haya presentado sus declaraciones de renta, se presume salvo prueba en contrario, que obtiene por el ejercicio liberal de su profesión una renta imponible de treinta mil quetzales mensuales. / La renta imponible mencionada, se disminuye en un cincuenta por ciento (50%) cuando el profesional… tenga menos de tres (3) años de graduado o sea mayor de sesenta (60) años de edad." (unregistered → oficio inscription in Utilidades) | Facturas especiales ISR retention: 5% definitive on the invoice value EXCLUDING IVA (text as reformed by D-4-2019; before that it tied to the Opcional regime — EVID-234 gloss); the factura-especial copy is the retention constancia; 10-day enter + DJ + annex. Unregistered/non-filing university professionals assessed on a Q30,000/month presumption (−50% if <3 years graduated or >60 years old) | `gt/sources/26_LAT_10-2012.pdf` | pp. 8-9 arts. 16-17 + stamp (EVID-234) |
| LB-015 | D-10-2012, whole Libro I searched — no lucrativas-NOL article; nearest texts: art. 96: "compensación de pérdidas de capital… deduciendo la pérdida anterior." (capital only); art. 101: no residents "tributan en forma separada por cada pago o acreditación… sin que sea posible compensación alguna entre éstas." / 28_ art. 27 num. 1: "deberán acumular la renta imponible o pérdida fiscal obtenida en cada cierre trimestral, al trimestre inmediato siguiente." | ABSENCE FINDING (EVID-235): unlike old D-26-92 (art. 25 carryforward), LAT Libro I contains NO general multi-year net-operating-loss carryforward for Régimen Sobre las Utilidades — losses net only within the annual period via quarterly accumulation; capital losses keep the 2-year same-nature rule (LB-012); finding contingent on the GOQ-58 post-46-2022 window | `gt/sources/26_LAT_10-2012.pdf` | whole Libro I (absence); arts. 96/101 nearest texts (EVID-235) |
| LB-016 | Reglamento del Libro I de la LAT, AG 213-2013 (Guatemala, 8 de mayo de 2013; consolidated with AG 167-2014 stamps; deroga AG 206-2004): "ACUERDO GUBERNATIVO NÚMERO 213-2013…" / "ARTICULO 91. Vigencia. El presente Acuerdo Gubernativo empezará a regir el día de su publicación en el Diario de Centro América." (DCA date not printed) | The ISR reglamento identity: AG 213-2013 issued under LAT art. 179, stamps stop at AG 167-2014 (arts. 7 ¶3, 25 reformed; 25"A"/25"B" added); effective date and post-167-2014 reforms unverifiable from the corpus (GOQ-59) | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | p.1 header; pp. 39-40 signature/vigencia; stamps (EVID-236) |
| LB-017 | AG 213-2013, Arts. 34-35: art. 34: agents of Ley art. 47 do NOT retain: "1. A los contribuyentes inscritos en el Régimen Sobre las Utilidades… consignarán en sus facturas la frase 'Sujeto a Pagos Trimestrales'… 2. Cuando la renta se encuentre exenta… el fundamento legal de la exención, deberá consignarlo su emisor en la factura… Cuando el contribuyente tenga la calidad de Pequeño Contribuyente y así lo haga constar en la factura respectiva, el agente de retención deberá proceder conforme lo establece el artículo 48 de la Ley del Impuesto al Valor Agregado." / art. 35: "cuando adquieran servicios o bienes con valor menor a dos mil quinientos quetzales (Q 2,500.00), excluyendo el Impuesto al Valor Agregado, no están obligados a practicar la retención y podrán deducir el monto pagado o acreditado." | Retention-suppression matrix (buyer side): Utilidades taxpayers (legend on invoice), exempt rentas (legal basis printed), pequeño contribuyente (defer to IVA art. 48 — outside this file), and the < Q2,500.00 per-operation floor (IVA excluded) which ALSO permits the payer to deduct the amount | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | p.17 arts. 34-35 (EVID-238) |
| LB-018 | AG 213-2013, Arts. 74-89: art. 81: "el contribuyente que perciba rentas de capital, y se le haya efectuado retención no está obligado a presentar declaración por las rentas de capital que hayan sido objeto de retención." / art. 80: pérdidas de capital "sólo podrán compensarse contra las ganancias de capital futuras, y en ningún caso podrán ser compensadas con ganancias del giro habitual o rentas ordinarias." / art. 83: transportistas con base en puerto extranjero = sin EP; unretained → pay "dentro de los primeros diez (10) días del mes siguiente" / art. 84: freight retention base add-backs (combustible, almacenaje, demoras…) minus documented Guatemalan land/air freight / art. 85: foreign-currency retentions at "tipo de cambio de referencia publicado diariamente por el Banco de Guatemala… a la fecha del pago"; "El formulario de pago del impuesto retenido, constituirá además la constancia de retención." / art. 87 (transitorio): "durante el año 2013, el tipo impositivo de siete por ciento (7%) se sustituirá por el tipo impositivo de seis por ciento (6%)." / art. 86 (transitorio): Q2,500-amnesty — multas/recargos exonerated for pre-vigencia failures to retain on ops ≤ Q2,500.00 regularized within 30 days / art. 89: leftover pre-LAT invoices reusable with the new régime legend (sello) | Capital/non-resident operational closure: retention = final discharge (no DJ) for retained capital income; loss compensation fenced to capital gains only; transportista treatment; freight-base add-backs; Banguat reference FX at payment date with the payment form doubling as constancia; 2013 6% substitution; 2013 Q2,500 retention amnesty (historical-only); pre-LAT invoice reuse with régime legend. GOQ-59 caveat on all 28_-anchored values | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | pp. 34-39 arts. 74-89 (EVID-240) |
| LB-019 | AG 213-2013, Arts. 19/24/25/25"A"/25"B"/27: art. 27 num. 1: "deberán acumular la renta imponible o pérdida fiscal obtenida en cada cierre trimestral, al trimestre inmediato siguiente… al cual se acreditará el impuesto determinado y pagado en él o los trimestres inmediato anteriores." (sic) / art. 27 num. 2: 8%-of-gross estimate "excluyendo las rentas exentas, las sujetas a retención definitiva o a otra categoría de renta"; "La declaración jurada correspondiente, deberá ser presentada y el pago hacerse efectivo, aún en el caso de trimestres que resulten incompletos por el inicio de actividades."; Q4 inside the annual DJ / art. 24: "podrán aplicar… porcentajes menores de depreciación a los establecidos en el artículo 28 de la Ley… el cual una vez adoptado no podrá ser variado." / art. 19: donation receipt data (a-j: entidad, NIT, correlativo, fecha, donante+NIT+domicilio, bien, monto en números y letras) + "copia de la solvencia fiscal del donatario… emitida en el mismo período fiscal" / arts. 25/25"A"/25"B" (AG 167-2014): obra-programación at project start + integración de costo final as annual-DJ annex; 25"A" defines "proyectos inmobiliarios de múltiples unidades" | Lucrativas procedure: quarterly payments accumulate year-to-date (losses carry to the next quarter within the year) with credit for prior-quarter tax; the 8% base excludes exempt, definitively-retained and other-category revenue; incomplete quarters still file; lower depreciation percentages allowed but IRREVOCABLE once adopted; donation deductions need the SAT-authorized receipt fields + donor-side copy of fiscal solvencia; real-estate development projects file obra programación + final cost integration annexes | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | pp. 9-15 arts. 19, 24, 25, 25"A", 25"B", 27 (EVID-241) |
| LB-020 | AG 213-2013, Art. 9: "De conformidad con lo establecido en los artículos 4 numeral 1 literal j) y 10 numeral 8 de la Ley, y para facilitar la recaudación, la persona individual o jurídica que pague dietas, deberá practicar retención del Impuesto sobre la Renta, con carácter definitivo, en la forma prevista por la Ley, excepto cuando quien reciba la dieta demuestre que se encuentra inscrito en el régimen sobre las utilidades de actividades lucrativas. / La deducción de este gasto se comprobará con el recibo emitido por los miembros… afecto al Impuesto de Timbres Fiscales y Papel Sellado Especial para Protocolos." | Dieta (per-diem/board-member fee) retention is DEFINITIVE for recipients not inscribed in Utilidades (dietas are a lucrativas hecho generador per Ley art. 10 num. 8); the operative RATE is not printed in art. 9 — GOQ-60, recorded open, never guessed; Criterio 6-2018 applies the art. 44 rates (LB-023, interpretive layer); payer deduction evidenced by the timbre-affected receipt | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | p.4 art. 9 (EV02c OQ-4; EVID-500) |
| LB-021 | Ley del IVA, D-27-92 (texto ≤ D-10-2012), Arts. 52/52"A": Art. 52: "Cuando un contribuyente adquiera bienes o servicios de personas individuales que… no extiendan o no le entreguen las facturas correspondientes, deberá emitir una factura especial por cuenta del vendedor o prestador del servicio, y le retendrá el impuesto respectivo." / Art. 52"A" intermediaries: "deberán emitir una factura especial al intermediario, reteniendo el Impuesto al Valor Agregado y el Impuesto Sobre la Renta que corresponda" | Cross-lock: this LB owns the statutory cross-lock anchor for the IVA side (Ley IVA Art. 52/52"A" as printed ≤ D-10-2012); the factura especial is the buyer-issued document on non-invoicing sellers carrying BOTH retentions — IVA (operative retention mechanics cross-ref GT-TAX-FR-097 + GT-EINV-FR-036) and ISR 5% definitive (26_ Art. 16, this file FR-191); cited for the dual-retention cross-reference only, never re-derived here | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 34-37 Arts. 52, 52"A" (EVID-177) |
| LB-022 | Catálogo SAT Formularios Vigentes (48_, snapshot 2025-10-06): "ISR Anual | – | – | – | 1411" (lucrativas family: Utilidades + Opcional Simplificado + Sobre Ingresos + Exentos); "ISR Capital | Mensual | – | – | 1321"; "ISR No Residentes | Pago Directo | Mensual | – | 1371"; "ISR Opcional | Mensual | – | – | 1311"; trimestral lucrativas = 1361; no-resident retenciones = 1352 | Form identities (R46, binding — cite 48_, never the digest): annual ISR lucrativas family = **SAT-1411**; capital monthly = **SAT-1321**; no-resident direct-payment monthly = **SAT-1371** (NOT the annual); opcional monthly = SAT-1311; quarterly lucrativas = SAT-1361; no-resident retentions = SAT-1352. Filing surfaces themselves are F-wave | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` | ISR family rows, dump lines 32-41 (EVID-372, EVID-373) |
| LB-023 | SAT Criterio Tributario Institucional 6-2018 (aprobado 23-abr-2018), holdings on LAT arts. 21/23 deducibilidad: sueldos deductible iff general requirements + worker in IGSS planilla when the patrono is registration-obliged (≥3 workers; transporte terrestre ≥1, Acuerdo 1123); "la deducción máxima por sueldos pagados a los socios o consejeros… se limita a un monto total anual del diez por ciento (10%) sobre la renta bruta."; aguinaldo/bono 14 excess deductible only with pacto colectivo "debidamente homologado por el Ministerio de Trabajo"; dietas a pequeño contribuyente deductible only if payer applies "la retención del Impuesto Sobre la Renta, con carácter definitivo, aplicando los tipos impositivos establecidos en el artículo 44 de la Ley" + timbre-affected receipt | Interpretive layer (SAT criterion, not law — law wins): the art. 23.f IGSS-planilla gate applies only to IGSS-registration-obliged employers (<3 workers may deduct with libros/planillas); pacto-colectivo homologación is the only route to deduct aguinaldo/bono 14 excess; dieta retention per Criterio = art. 44 rates — cited as practice interpretation of the GOQ-60 rate question, not as statutory resolution | `gt/sources/65_SAT_Criterio_6-2018.pdf` | pp. 2-8 holdings 1-3 (EVID-498, EVID-499, EVID-500) |

## 3. Functional Requirements

### 3.1 Taxonomy, exemptions & régime lifecycle

- **GT-TAX-FR-147:** The system shall classify every ISR taxpayer/operation
  against the Art. 2 renta categories (*actividades lucrativas*, *trabajo*,
  *capital y ganancias de capital*) and every lucrativas taxpayer against
  exactly one Art. 14 régime — **Régimen Sobre las Utilidades** (general
  régime) or **Régimen Opcional Simplificado Sobre Ingresos** — with no
  third lucrativas régime; the no-resident title (V) applies to
  non-residents without permanent establishment (with EP → Title II, per
  art. 102 — FR-183). (LB-002; EVID-217)
- **GT-TAX-FR-148:** Guard rows: the system shall never model post-2012
  Guatemala ISR on D-26-92 (derogated at ISR Libro I vigencia,
  **1-Jan-2013**, stored as a dated row) and shall never model an ISR
  "pequeño contribuyente" régime or ISR-side pequeño threshold — the LAT
  creates none (pequeño remains IVA-side registration; cross-ref Task 2
  guard). (LB-002; EVID-217)
- **GT-TAX-FR-149:** ISR exemptions (Arts. 8/11/87) shall be implemented
  as PARTIAL, per-beneficiary revenue-stream facts — never global
  taxpayer flags: universities/centros educativos exempt only on the
  education stream (matrícula, colegiaturas, derechos de examen);
  no-lucrativas exempt only on donations/dues revenue (mercantile,
  agropecuaria, financiera, services activity gravada); cooperatives only
  on member transactions; churches only on culto; Art. 87 capital-side
  rows (subsidies, occasional personal-goods sales except registered
  vehicles/vessels/aircraft). Retention and formal obligations SURVIVE
  exemption. Exemption windows are per-beneficiary facts (SR-wave
  incentive/regime files cross-ref — never global). (LB-003; EVID-218)
- **GT-TAX-FR-150:** Régime selection shall be a company-level election
  recorded at inscription with **default = Régimen Sobre las Utilidades
  when the taxpayer is silent** (Art. 50); régime change shall be possible
  only by aviso filed in the month before the annual period starts (in
  practice December), **effective the following 1-January** — no mid-year
  régime switches; pre-LAT migration semantics (Art. 174) recorded as
  history. No monetary threshold gates either régime. (LB-010; EVID-225)
- **GT-TAX-FR-151:** The retention-agent registry for Opcional Simplificado
  collection shall implement Art. 47 (payers with contabilidad completa,
  the State and its entities, associations, fideicomisos and similar) and
  the 28_ art. 7 inscription rule (principal economic activity = the one
  > 50% of ingresos, else the largest — feeds régime/activity
  classification; GOQ-59 caveat on the reglamento layer).
  (LB-009; LB-016; EVID-224, EVID-237)

### 3.2 Régimen Sobre las Utilidades

- **GT-TAX-FR-152:** The Utilidades rate shall be stored as dated rows
  with instrument provenance "D-10-2012 arts. 36/172, texto ≤ D-46-2022":
  **25%** valid_from 2015-01-01 (open) — the current permanent rate;
  transitional rows **31% FY2013** (valid_to 2013-12-31) and **28%
  FY2014** (valid 2014-01-01..2014-12-31) are historical, non-transmittable
  class; 31% shall never resolve as the current rate (GOQ-58 caveat on
  all rows). (LB-007; LB-008; EVID-222, EVID-223)
- **GT-TAX-FR-153:** The liquidation period shall be the calendar year
  (1-January to 31-December); the annual DJ shall be filed within the
  **first 3 months** of the following calendar year (Art. 39), and it
  absorbs the Q4 payment (FR-155). Form identity: annual ISR of the
  lucrativas family = **SAT-1411** (R46, 48_); the filing surface is
  F-wave — cross-referenced, never duplicated. (LB-007; LB-022; EVID-222,
  EVID-373)
- **GT-TAX-FR-154:** Quarterly advance payments shall support exactly the
  two Art. 38 options, chosen per taxable year: (1) **real partial
  closings** (renta imponible of the quarter), or (2) **presumptive
  estimated renta = 8% of total rentas brutas of the quarter, excluding
  exempt rentas** (and, per 28_ art. 27.2, excluding revenue subject to
  definitive retention or other renta categories); air-transport
  taxpayers under Art. 21 Bis use **15%** instead of 8%. Each option's
  percentages are dated rows (D-10-2012 art. 38 / art. 21 Bis, GOQ-58
  caveat). (LB-007; LB-019; EVID-222, EVID-241)
- **GT-TAX-FR-155:** Quarterly payment mechanics shall implement 28_ art.
  27 (GOQ-59 caveat): year-to-date accumulation of renta imponible or
  pérdida fiscal from each quarterly closing into the next quarter, with
  credit for ISR determined and paid in prior quarters of the same year;
  quarterly DJ + payment within the month following quarter end; Q4 is
  NOT paid on the quarterly cycle — it is absorbed into the annual
  liquidation DJ (FR-153); incomplete quarters (activity start mid-quarter)
  still file. Form identity: quarterly lucrativas = **SAT-1361** (48_);
  surface = F-wave. (LB-007; LB-019; LB-022; EVID-222, EVID-241, EVID-373)
- **GT-TAX-FR-156:** Utilidades taxpayers' invoices for gravadas
  activities shall carry the mandatory phrase **"sujeto a pagos
  trimestrales"** (Art. 42.1; printed capitalized in 28_ art. 34 as
  "Sujeto a Pagos Trimestrales") — the legend that suppresses client-side
  Opcional retention (FR-165); FEL emission of the legend is owned by
  GT-EINV (cross-ref). (LB-007; LB-017; EVID-222, EVID-238)
- **GT-TAX-FR-157:** Utilidades taxpayers shall report inventories taken
  at 30-June and 31-December in January and July respectively (Art. 42.3)
  — biannual inventory-reporting calendar rows. (LB-007; EVID-222)
- **GT-TAX-FR-158:** Negative-FR (absence finding, EVID-235): the system
  shall implement **NO multi-year net-operating-loss carryforward** for
  lucrativas — LAT Libro I contains none (unlike old D-26-92 art. 25);
  Utilidades losses net only WITHIN the annual period via the FR-155
  quarterly YTD accumulation into the annual liquidation. The ONLY
  statutory loss carryforwards are capital losses: 2 years, same-nature
  only (FR-181). This finding is contingent on the GOQ-58 post-46-2022
  window — if a later reform added a NOL regime, re-verify. No product
  default NOL/carryforward behavior shall be imported from other
  localizations. (LB-015; LB-012; EVID-235, EVID-231; GOQ-58 → OQ-001)

### 3.3 Régimen Opcional Simplificado

- **GT-TAX-FR-159:** The Opcional Simplificado scale shall be stored
  verbatim as dated rows (provenance "D-10-2012 art. 44, texto ≤
  D-46-2022", GOQ-58 caveat): **monthly** renta imponible — bracket 1:
  Q0.01–Q30,000.00, fixed Q0.00, **5%** over the renta imponible;
  bracket 2: Q30,000.01 onward, fixed **Q1,500.00 + 7%** over the
  Q30,000.00 excess. Base = gross income of the month (renta bruta menos
  rentas exentas), IVA excluded; liquidation period = monthly (Art. 45).
  (LB-009; EVID-224)
- **GT-TAX-FR-160:** Transitional dated rows for the upper bracket:
  **6%** in place of 7% for tax year 2013 only (Art. 173.1 as reformed by
  D-19-2013 + 28_ art. 87 transitorio, valid 2013-01-01..2013-12-31),
  7% from 2014-01-01 (Art. 173.2); the 5% lower bracket was never
  transitional. Historical class rows (GOQ-58 caveat on the art. 44/173
  values; GOQ-59 caveat on the 28_ anchor). (LB-008; LB-018; EVID-223,
  EVID-240; GOQ-58, GOQ-59 → OQ-001, OQ-002)
- **GT-TAX-FR-161:** Opcional Simplificado tax shall be collected
  **THROUGH retention by payers** (Art. 46): retention agents (FR-151)
  apply the FR-159 split to each payment/accreditation; direct payment by
  the taxpayer exists only with SAT authorization (resolved ≤ 15 días) and
  the taxpayer's invoices must then state "que pagan directamente el
  impuesto a la Administración Tributaria, identificando la autorización
  respectiva". The monthly DJ (first 10 días of the following month,
  Art. 49) exists for the direct-payment authorized and as the
  informative surface; the retention itself is the discharge for ordinary
  taxpayers. Form identity: opcional monthly = **SAT-1311** (48_);
  surface = F-wave. (LB-009; LB-022; EVID-224, EVID-372)
- **GT-TAX-FR-162:** The retention floor shall be a dated row: agents do
  NOT retain on services or goods purchases **< Q2,500.00 per operation,
  IVA excluded** (Art. 48 ¶2; mirrored 28_ art. 35 which also allows the
  payer to deduct the amount) — and the payer may still deduct the paid
  amount. (LB-009; LB-017; EVID-224, EVID-238)
- **GT-TAX-FR-163:** Agent-side deadlines for Opcional retentions shall
  be: constancia delivered within the **first 5 días** of the immediately
  following month; retention entered with DJ + annex (nombre, NIT, valor,
  retención) within the **first 10 días** of the following month
  (Art. 48). (LB-009; EVID-224)
- **GT-TAX-FR-164:** Opcional Simplificado taxpayers under direct-payment
  authorization shall file the monthly DJ within the first 10 días of the
  following month and an **annual informative DJ within the first 3
  months** of each year (Art. 49); the annual informative duty is
  informational, not a liquidation (the retentions were definitive).
  (LB-009; EVID-224)
- **GT-TAX-FR-165:** Retention suppression shall apply exactly per 28_
  art. 34 (GOQ-59 caveat): no Opcional ISR retention on (1) Utilidades
  taxpayers evidencing the "Sujeto a Pagos Trimestrales" legend
  (FR-156), (2) exempt rentas with the legal basis printed on the
  invoice, (3) pequeño contribuyente counterparts (defer to IVA art. 48 —
  Task 2 owns, never re-derived), (4) operations < Q2,500.00 (FR-162),
  (5) direct-payment-authorized taxpayers. (LB-017; EVID-238)
- **GT-TAX-FR-166:** For Utilidades-side interplay, this file cites
  Task 4's art. 73 scale rows (GT-TAX-FR-128) and art. 70/72 deduction
  rows (GT-TAX-FR-115..127) by FR id — never re-deriving them; the
  Opcional Simplificado scale (FR-159) is distinct from the employment
  scale and the two shall never be conflated (both are 5%/7% two-bracket
  tables with different bases: monthly gross vs annual net).
  (LB-009; EVID-224; cross-ref 04_isr-trabajo.md FR-128)

### 3.4 Deducciones, no-deducibles, thin cap & depreciation

- **GT-TAX-FR-167:** The Art. 21 quantitative deduction caps shall be
  seeded as dated rows (provenance "D-10-2012 art. 21, texto ≤ D-46-2022
  (reformado D-19-2013/D-2-2020 en nums. indicados)", GOQ-58 caveat):
  related-party sueldos (socios/consejeros/cónyuges/parientes) ≤ **10%**
  of renta bruta (annual total); aguinaldo and bono 14 each ≤ **100% of
  one monthly salary** (unless pacto colectivo — FR-169); IGSS/IRTRA/
  INTECAP employer quotas **fully** deductible; indemnizaciones ≤
  **8.33%** of total annual remunerations; bad-debt reserve ≤ **3%** of
  accounts/documents-receivable debtor balances; donations to
  asociaciones/fundaciones/iglesias/partidos ≤ **5%** of renta bruta AND
  ≤ **Q500,000.00** per year (Estado/universidades/cultural-scientific
  rows without a printed cap — deducibility still subject to art. 22
  requirements + FR-174 receipts); foreign advisory ≤ **5%**; viáticos
  ≤ **3%**; royalties ≤ **5%**; organization costs amortized in **5
  successive equal annual installments**. (LB-004; EVID-219)
- **GT-TAX-FR-168:** The Art. 23 no-deductible catalog shall be
  implemented with the gating dependencies: a) expenses alien to the
  business (oficio prorrateo if no separate accounts); c) expenses whose
  corresponding ISR retention was not effected and paid — **deductible
  only once the retention is entered** (retención↔deducción dependency;
  sanction hooks = CT 94.7 via Task 6); f) sueldos not evidenced on the
  IGSS planilla (interpretive scope per FR-169); h) profit-sharing
  bonuses to directors/managers; i) dividends/participations; j) owner
  withdrawals; q) mixed professional/personal-use assets presumed
  deductible at **50%** only; r) depreciation of real estate over the
  matrícula fiscal/catastro value. (LB-005; EVID-220; cross-ref Task 4
  FR-146)
- **GT-TAX-FR-169:** The Criterio 6-2018 interpretive layer (SAT
  criterion, not law) shall configure — never override — FR-167/168: the
  IGSS-planilla gate binds only IGSS-registration-obliged employers
  (≥ 3 workers; terrestrial transport ≥ 1); non-obliged employers deduct
  with libros de salarios/planillas as backing; aguinaldo/bono 14 excess
  over one monthly salary is deductible ONLY with a MinTrabajo-homologado
  pacto colectivo; related-party 10% cap corroborated. (LB-023; EVID-498,
  EVID-499)
- **GT-TAX-FR-170:** Thin-cap interest limitation (Art. 24): deductible
  interest ≤ **Junta Monetaria maximum annual simple reference rate × 3 ×
  average total net equity** (average = (prior-year close + current-year
  close) ÷ 2; rate published January and July); banks, sociedades
  financieras and authorized cooperativas excluded. JM reference-rate
  values are external dated data — configuration input, never
  hard-coded. (LB-005; EVID-220)
- **GT-TAX-FR-171:** Depreciation shall use straight-line (*línea recta*)
  with the Art. 28 statutory-maximum table as dated rows (GOQ-58 caveat):
  edificios/construcciones/instalaciones adheridas y mejoras **5%**;
  árboles/arbustos/frutales **15%**; instalaciones no adheridas,
  mobiliario y equipo de oficina, buques-tanques/barcos/material
  ferroviario **20%**; semovientes, maquinaria, vehículos en general,
  grúas, aviones, remolques/semirremolques, contenedores y material
  rodante (ex-rail) **20%**; equipo de computación **33.33%**;
  herramientas/porcelana/cristalería/mantelería/cubiertos **25%**;
  reproductores de raza **25%**; other unlisted muebles **10%**. Other
  methods only with SAT authorization (Art. 27). (LB-006; EVID-221)
- **GT-TAX-FR-172:** Land shall NEVER be depreciated; real-estate
  depreciation base = the more recent of matrícula fiscal vs catastro
  municipal value, whichever is higher; when the building/improvements
  value cannot be isolated, the building share is **presumed at 70%** of
  the total property value including land (Art. 26). Credited IVA is
  excluded from the depreciation base (IVA art. 16 pairing — Task 1
  FR-020 owns). (LB-006; EVID-221)
- **GT-TAX-FR-173:** Taxpayers may adopt LOWER depreciation percentages
  than the Art. 28 maxima; once adopted the choice is **IRREVOCABLE**
  (28_ art. 24 — GOQ-59 caveat): per-asset-class election stored with
  adoption date, never silently changed. (LB-019; EVID-241)
- **GT-TAX-FR-174:** Donation deductions shall require the 28_ art. 19
  receipt (fields a-j: entidad, NIT, correlativo, fecha, donante + NIT +
  domicilio, bien, monto en números y letras — SAT-authorized) AND the
  donor-side copy of the donatario's fiscal solvencia issued in the same
  fiscal period (GOQ-59 caveat). (LB-019; EVID-241)
- **GT-TAX-FR-175:** Real-estate development projects (*proyectos
  inmobiliarios*) shall support the 28_ arts. 25/25"A"/25"B" annexes
  (AG 167-2014 texts — GOQ-59 caveat): obra programación at project
  start and integración de costo final as annual-DJ annex; 25"A" scope =
  multi-unit projects (copropiedad, propiedad horizontal, condominios).
  (LB-019; EVID-241)

### 3.5 Rentas y ganancias de capital

- **GT-TAX-FR-176:** Capital income shall be classified per Art. 84:
  capital inmobiliario (non-habitual leasing/subleasing/use-transfer of
  real estate — habitual property renting stays in lucrativas per
  art. 15); capital mobiliario (interests/credit rents, tangible and
  intangible movable leases incl. derechos de llave/regalías/derechos de
  autor, vitalicias/insurance, dividend/profit distributions);
  ganancias y pérdidas de capital (non-ordinary-course enajenación,
  revaluaciones, fixed assets); loterías/rifas/sorteos/bingos.
  (LB-011; EVID-230)
- **GT-TAX-FR-177:** Capital-inmobiliario taxable base shall default to
  **70% of the rent** (flat 30% presumed expenses, Art. 88 num. 2);
  greater actual expense only via January declaración jurada + refund
  request. The 30% presumption and the Art. 89 transaction-cost cap
  (FR-178) are dated rows (provenance "D-10-2012 arts. 88-89, texto ≤
  D-46-2022", GOQ-58 caveat). (LB-011; EVID-230; GOQ-58 → OQ-001)
- **GT-TAX-FR-178:** Ganancia de capital = enajenación price − cost;
  transaction costs (comisiones, notariales, registro) deductible up to
  **15% of the enajenación value**, the cap waived for taxpayers with
  contabilidad completa and documentation; shares/participaciones cost =
  documented acquisition value or book value certified by the issuer
  (num. 3, reformed D-19-2013) — the 15% cap is a dated row (GOQ-58
  caveat). (LB-011; EVID-230; GOQ-58 → OQ-001)
- **GT-TAX-FR-179:** Capital rentas (mobiliarias + inmobiliarias) and
  ganancias de capital shall bear a flat **10% definitive retention**
  applied from the moment of effective payment, crediting or bank credit
  (Art. 90/92) — dated row, provenance "D-10-2012 arts. 90/92, texto ≤
  D-46-2022" (GOQ-58 caveat); the **SIB carve-out**: payments to
  entities supervised by the SIB (banks, financieras, cooperativas) are
  NOT subject to this retention (they self-liquidate). Form identity:
  capital monthly = **SAT-1321** (R46, 48_); surface = F-wave.
  (LB-012; LB-022; EVID-231, EVID-372)
- **GT-TAX-FR-180:** Dividend, ganancia and utilidad distributions shall
  bear a **5% definitive retention** (Art. 93) — dated row (GOQ-58
  caveat); banking groups retain only on distributions to shareholders
  of the controlling entity. Non-resident dividends + home-office
  transfers instead ride the FR-184 matrix (5%). (LB-012; LB-013;
  EVID-231, EVID-232)
- **GT-TAX-FR-181:** Capital-loss carryforward shall be fenced:
  compensable ONLY against future ganancias de capital of the SAME
  nature, for a **maximum of 2 years** from the loss; uncompensated
  balance at expiry is dead — no deduction, credit or carryforward
  whatsoever (Art. 91); in no case compensable against ordinary-course
  income (28_ art. 80 — GOQ-59 caveat); loss-compensation DJ within 3
  months of calendar-year end (Art. 96). (LB-012; LB-018; EVID-231,
  EVID-240)
- **GT-TAX-FR-182:** Capital payment cycles: retention + DJ within the
  **first 10 días** of the month following payment/crediting (Art. 94);
  unretained capital rentas self-pay within 10 días (Art. 95);
  ganancias de capital pay within 10 días of the month following
  surgimiento; and taxpayers whose capital rentas were fully retained
  file **NO capital DJ** — retention is final discharge (28_ art. 81 —
  GOQ-59 caveat). (LB-012; LB-018; EVID-231, EVID-240)

### 3.6 No residentes (sin establecimiento permanente)

- **GT-TAX-FR-183:** Non-resident ISR (no EP) shall apply the Art. 104
  definitive retention matrix as dated rows (provenance "D-10-2012
  art. 104, texto ≤ D-46-2022"; numeral d of the 5% band derogated by
  D-19-2013; GOQ-58 caveat): **5%** — international transport (pasajes
  sold in/for Guatemala, carga freight with Guatemala origin or paid in
  Guatemala, user surcharges), insurance/reinsurance premiums (fianzas,
  reaseguros, retrocesiones, reafianzamientos), international telephony/
  data-transmission/communications, dividends/profit distributions and
  all transfers or account-credits to foreign head offices without
  consideration; **3%** exception — international news supply and use in
  Guatemala of films, music recordings and similar. Base = amount
  effectively paid/credited per operation with **no compensation between
  operations** (Art. 103). (LB-013; EVID-232)
- **GT-TAX-FR-184:** Matrix (continued): **10%** — interests paid or
  credited to non-residents, EXCEPT loans from banks/financial entities
  regulated in their country of origin and multilateral organizations
  (exemption test on the payer); **15%** — sueldos y salarios, dietas,
  comisiones, bonificaciones; deportistas y artistas; regalías;
  honorarios; asesoramiento científico, económico, técnico o financiero;
  **25%** — residual ("Otras rentas gravadas no especificadas").
  (LB-013; EVID-232)
- **GT-TAX-FR-185:** Payers with contabilidad completa shall retain the
  matrix percentages **with definitive character** and enter them by DJ
  within the first 10 días of the following month (Art. 105);
  non-retained rentas self-liquidate within 10 días (Arts. 106-107,
  direct-payment surface = **SAT-1371 monthly**, R46/48_; retention-DJ
  surface = SAT-1352, 48_); the payment form doubles as the retention
  constancia (28_ art. 85). Application of the matrix at payment time =
  odoo with saas validation. (LB-013; LB-018; LB-022; EVID-232,
  EVID-240, EVID-372, EVID-373)
- **GT-TAX-FR-186:** International transportistas with base in a foreign
  port are treated as without EP; freight retentions compute on the
  gross amount plus add-backs (combustible, almacenaje, demoras, and
  similar) minus documented Guatemalan land/air freight costs (28_ art.
  84 — GOQ-59 caveat). (LB-018; EVID-240)
- **GT-TAX-FR-187:** Foreign-currency operations shall convert at the
  **Banco de Guatemala reference exchange rate published daily, at the
  payment date** (28_ art. 85 — GOQ-59 caveat); the rate is external
  dated data consumed from market feeds, never hard-coded.
  (LB-018; EVID-240)

### 3.7 Facturas especiales (ISR side) & professional presumption

- **GT-TAX-FR-188:** Emitters of facturas especiales (buyers invoicing on
  behalf of non-invoicing sellers — IVA-side mechanics owned by Task 3,
  cross-lock 23_ Arts. 52/52"A", EVID-177) shall withhold ISR at **5%
  with definitive-payment character on the factura value EXCLUDING
  IVA** (26_ Art. 16 párrafo 1, as reformed by Dto. 4-2019 of
  08-05-2019) — dated rows: 5% valid_from 2019-05-08; the pre-reform
  text tied the retention to the Opcional regime rates (historical row,
  valid 2013-01-01..2019-05-07, EVID-234 gloss). Dual-retention behavior
  (IVA + ISR on the same document): this file's LB-021 owns the statutory
  cross-lock anchor for the IVA side (Ley IVA Art. 52/52"A" as printed
  ≤ D-10-2012); operative IVA retention mechanics cross-ref GT-TAX-FR-097
  (03_) + GT-EINV-FR-036.
  (LB-014; LB-021; EVID-234, EVID-177)
- **GT-TAX-FR-189:** Factura-especial ISR mechanics: a copy of the
  factura especial serves as the retention constancia; the emitter
  enters the retention with retention DJ + annex within the **first 10
  días of the following month** (Art. 16). Application at emission =
  odoo with saas validation. (LB-014; EVID-234)
- **GT-TAX-FR-190:** Professional presumption (Art. 17): unregistered or
  non-filing university professionals are assessed on a **Q30,000.00
  monthly presumed renta imponible** (salvo prueba en contrario), reduced
  **50%** (to Q15,000.00) when graduated < 3 years or older than 60;
  unregistered professionals are inscribed de oficio in Utilidades.
  Dated rows (GOQ-58 caveat). (LB-014; EVID-234)

### 3.8 Dietas, FX & historical transitorios

- **GT-TAX-FR-191:** Dieta retention (28_ art. 9): payers of dietas
  (a lucrativas hecho generador per Ley art. 10 num. 8) shall retain ISR
  **con carácter definitivo**, except when the recipient demonstrates
  inscription in Régimen Utilidades; payer deduction evidenced by the
  recipient's timbre-affected receipt. The operative RATE is not printed
  in the reglamento — recorded as GOQ-60 open: NO rate shall be
  hard-coded; Criterio 6-2018's art. 44 application (LB-023) is recorded
  as practice interpretation only. (LB-020; LB-023; EVID-500; GOQ-60 →
  OQ-003)
- **GT-TAX-FR-192:** Historical transitorios (non-transmittable class,
  stored as dated rows with valid_to): the 2013 opcional-upper 6%
  substitution (28_ art. 87 — FR-160) and the 2013 Q2,500 retention
  amnesty (28_ art. 86: fines/surcharges exonerated for pre-vigencia
  retention failures ≤ Q2,500.00 regularized within 30 days of vigencia)
  shall never affect post-2013 behavior; leftover pre-LAT invoices were
  reusable with the new régime legend (28_ art. 89) — recorded as
  history. (LB-018; EVID-240; GOQ-59 → OQ-002)
- **GT-TAX-FR-193:** Declaration-surface cross-references (F-wave owns
  all filing surfaces; identities per R46 from 48_): annual lucrativas
  family = SAT-1411; quarterly lucrativas = SAT-1361; opcional monthly =
  SAT-1311; capital monthly = SAT-1321; no-resident direct payment
  monthly = SAT-1371; no-resident retentions = SAT-1352; retention
  constancia documents (opcional 5-day, factura-especial copy, payment
  form as constancia) are data-capture surfaces in odoo, filing in
  F-wave. (LB-022; EVID-372, EVID-373)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance + as-of qualifier; snapshot-on-write; rate/bracket/cap rows are
decree-bound, never constants (dated-instrument regime per D15/D16,
cited above); historical rows are
non-transmittable class. Machine-readable rate/bracket data lives in
`isr_rates.csv` (one row per régime/category × bracket/rate, with
valid_from/valid_to + provenance + EVID; transitional rows carry valid_to).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.isr.regime | code / default_flag / switch_window | selection / boolean / char | utilidades, opcional_simplificado; default = utilidades when silent; switch = aviso in December, effective next 1-Jan | FR-147, FR-150 |
| l10n_gt.isr.utilidades.rate | rate / valid_from / valid_to / provenance | decimal / date / date / char | 31% (2013), 28% (2014), 25% (2015-01-01→, open); "D-10-2012 arts. 36/172, texto ≤ D-46-2022" (GOQ-58) | FR-152 |
| l10n_gt.isr.utilidades.quarterly | method / presumptive_pct / exclusions | selection / decimal / json | real_closing \| presumptive_8pct (15% art. 21 Bis air transport); base excludes exempt + definitively-retained + other-category revenue; YTD accumulation with prior-quarter credit; Q4 inside annual DJ | FR-154, FR-155 |
| l10n_gt.isr.opcional.scale | bracket_floor / bracket_ceiling / fixed_amount / rate / valid_from / valid_to / provenance | decimal ×4 / date ×2 / char | monthly: Q0.01–Q30,000.00, Q0.00, 5%; Q30,000.01→, Q1,500.00, 7% (6% 2013 only); "D-10-2012 arts. 44/173 (+28_ art. 87)" (GOQ-58/59) | FR-159, FR-160 |
| l10n_gt.isr.opcional.parameter | key / value / provenance | char / decimal / char | retention_floor_per_op Q2,500.00 (IVA excl.); constancia_days 5; enter_days 10; annual_informative_dj_months 3; direct-payment SAT authorization ≤15 días | FR-162..164 |
| l10n_gt.isr.deduction.cap | cap_key / pct_or_amount / base / valid_from / provenance | char / decimal / char / date / char | sueldos_relacionados 10% renta bruta; aguinaldo 100% monthly; bono14 100% monthly; indemnizacion 8.33% annual remunerations; incobrables 3% receivables; donaciones 5% + Q500,000.00; asesoría_ext 5%; viáticos 3%; regalías 5%; organización 5 cuotas; thin-cap JM rate × 3 × average net equity | FR-167, FR-170 |
| l10n_gt.isr.nodeducible | rule_key / params | char / json | ajenos, unpaid_retention_gate (23.c), no_igss_planilla (23.f), utilidades_bonuses, dividends, retiros, mixed_use_50pct, inmueble_over_matricula | FR-168 |
| l10n_gt.isr.depreciation.class | class_no / description / max_pct | integer / char / decimal | 1 edificios 5%; 2 árboles/frutales 15%; 3 instalaciones no adheridas/mobiliario/buques/ferroviario 20%; 4 semovientes/maquinaria/vehículos 20%; 5 computación 33.33%; 6 herramientas 25%; 7 reproductores 25%; 8 otros muebles 10%; land never; building presumption 70%; lower-rate election irrevocable | FR-171..173 |
| l10n_gt.isr.capital.rate | concept / rate / character / valid_from / provenance | char / decimal / char / date / char | capital+ganancias 10% definitiva; dividendos 5% definitiva; presumed_expenses 30% (base 70%); transaction_costs_cap 15%; SIB carve-out flag | FR-177..180 |
| l10n_gt.isr.capital.loss | carryforward_years / same_nature / fence | integer / boolean / char | 2 years, same-nature only, never vs ordinary income; expiry = dead balance | FR-181 |
| l10n_gt.isr.noresidente.rate | band / concept / rate / valid_from / provenance | char / char / decimal / date / char | 5% transport/insurance/telecom/dividends+transfers; 3% news/films; 10% interests; 15% sueldos/dietas/comisiones, artistas, regalías, honorarios, asesoría; 25% residual; per-payment isolation | FR-183, FR-184 |
| l10n_gt.isr.factura.especial | rate / character / base / valid_from / valid_to / provenance | decimal / char / char / date ×2 / char | 5% definitiva on value excl. IVA (2019-05-08→); pre-reform tied to art. 44 (→2019-05-07); copy = constancia; 10-day enter | FR-188, FR-189 |
| l10n_gt.isr.presuncion.profesional | monthly_amount / reducer_pct / conditions | decimal / decimal / char | Q30,000.00/month; −50% (<3 years graduated or >60 years); oficio inscription in Utilidades | FR-190 |
| l10n_gt.isr.form.practice | form_code / name / surface | char / char / char | SAT-1411 anual lucrativas; SAT-1361 trimestral; SAT-1311 opcional mensual; SAT-1321 capital mensual; SAT-1371 no-residentes pago directo mensual; SAT-1352 no-resident retenciones (R46 — 48_) | FR-153, FR-155, FR-161, FR-179, FR-185, FR-193 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = XML
emission, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Taxation
defaults per wave plan: rate/bracket/cap dated data = `shared`; régime
selection on company + quarterly-payment computation + legends +
no-resident/factura-especial retention application = `odoo` with saas
validation; annual/quarterly DJ surfaces = F-wave cross-ref. Model names
stable across Odoo 17/18/19/20; no version-specific behavior required.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-147 | odoo | res.company / res.partner fiscal classifier | renta category + régime field | Drives which ISR engine applies; no-EP vs Title II test on partner |
| FR-148 | shared | — | guard rows | D-26-92 dead 2013-01-01; no ISR pequeño regime ever |
| FR-149 | shared | — (config data §4) | partial-exemption catalog | Per-beneficiary stream flags; retention duties survive |
| FR-150 | odoo | res.company (régimen selection) | régime + December-aviso switch | Default utilidades when silent; effective next 1-Jan; saas validates switch window |
| FR-151 | odoo | res.partner (agent qualification) + RTU activity | principal-activity >50% rule | 28_ art. 7 (GOQ-59); feeds CAE/activity layer |
| FR-152 | shared | — (config data §4 / CSV) | utilidades rate dated rows | 31/28/25 with valid_to; GOQ-58 caveat |
| FR-153 | shared | — | annual period + DJ window rows | SAT-1411 identity (R46); surface = F-wave |
| FR-154 | odoo | account.move quarterly computation | closing vs 8%/15% presumptive | saas validates option choice binding for the year |
| FR-155 | odoo | account.move quarterly close | YTD accumulation + prior-quarter credit | Q4 inside annual DJ; incomplete quarters file |
| FR-156 | odoo | account.move (invoice legend) | "sujeto a pagos trimestrales" | FEL emission side = GT-EINV; 28_ art. 34 prints capitalized |
| FR-157 | odoo | stock.quant inventory reports | Jan + Jul inventory calendar | Values at 30-Jun/31-Dec |
| FR-158 | shared | — | NOL guard row | NO multi-year NOL; 2-yr capital-only; contingent GOQ-58 |
| FR-159 | shared | — (config data §4 / CSV) | opcional scale rows | Monthly gross base, IVA excl., minus exempt |
| FR-160 | shared | — (config data §4 / CSV) | 6%/7% transitional rows | 28_ art. 87 anchor (GOQ-58/59 caveats) |
| FR-161 | odoo | account.tax (retention) + res.partner authorization | payer-retention collection + direct-payment flag | saas validates retention application; SAT-1311 surface = F-wave |
| FR-162 | shared | — (config data §4) | Q2,500 per-op floor row | Mirrors 28_ art. 35; deduction allowed |
| FR-163 | odoo | account.move (constancia) + retention DJ data | 5-day constancia, 10-day enter | Annex fields nombre/NIT/valor/retención |
| FR-164 | odoo | account.move monthly DJ data | 10-day monthly + Q1 informative DJ | Direct-payment-authorized taxpayers |
| FR-165 | odoo | account.move retention suppression tests | counterparty-status gating | legend/exenta/pequeño→IVA-48/<Q2,500/authorized |
| FR-166 | shared | — | cross-ref row | T4 FR-128 + FR-115..127 cited by id; scales never conflated |
| FR-167 | shared | — (config data §4) | art. 21 caps dated rows | GOQ-58; pacto colectivo flag on aguinaldo/bono14 |
| FR-168 | odoo | account.move.line (deduction eligibility) | gating flags (23.c/23.f/50% mixed) | CT 94.7 sanction hooks = Task 6; saas validates |
| FR-169 | shared | — (config data §4) | criterio interpretive params | ≥3-worker IGSS gate; pacto homologado excess route |
| FR-170 | shared | — (config data §4) | thin-cap formula params | JM rate external dated input; SIB-sector exclusion |
| FR-171 | shared | — (config data §4) | depreciation maxima table | Straight-line only unless SAT authorization |
| FR-172 | odoo | account.asset | land-never + 70% presumption + base rule | Credited-IVA exclusion pairs Task 1 FR-020 |
| FR-173 | odoo | account.asset.class config | lower-rate irrevocable election | Adoption date recorded; 28_ art. 24 (GOQ-59) |
| FR-174 | odoo | donation receipt model | art. 19 receipt fields + solvencia copy | GOQ-59 |
| FR-175 | odoo | project/real-estate annex surfaces | obra programación + integración final | 25"A" multi-unit scope (GOQ-59) |
| FR-176 | odoo | account.move classifier | art. 84 capital classes | art. 15 habitual-renting boundary to lucrativas |
| FR-177 | shared | — (config data §4) | 30% presumed expenses row | January DJ + refund route for greater actual |
| FR-178 | odoo | capital-gain computation | price−cost; ≤15% transaction costs | Full-accounting waiver; shares at certified book value |
| FR-179 | shared | — (config data §4 / CSV) | 10% definitive row + SIB carve-out | SAT-1321 identity; retention at payment/credit moment |
| FR-180 | shared | — (config data §4 / CSV) | 5% dividends row | Banking-group controlling-entity nuance |
| FR-181 | odoo | capital-loss carryforward engine | 2-yr same-nature fencing | 3-month compensation DJ; expiry = dead |
| FR-182 | odoo | account.move (capital cycles) | 10-day enter/self-pay; no-DJ-when-retained | 28_ art. 81 (GOQ-59) |
| FR-183 | shared | — (config data §4 / CSV) | 5%/3% matrix rows | Per-payment isolation (art. 103) |
| FR-184 | shared | — (config data §4 / CSV) | 10%/15%/25% matrix rows | Regulated foreign-bank interest exemption test |
| FR-185 | odoo | account.move (non-resident retention) + partner EP flag | matrix application at payment | saas validates; SAT-1371/SAT-1352 identities; form = constancia |
| FR-186 | odoo | freight retention base computation | add-backs − documented GT freight | 28_ art. 84 (GOQ-59) |
| FR-187 | shared | — | Banguat FX rule row | Rate from market feed; payment-date anchor |
| FR-188 | shared | — (config data §4 / CSV) | factura especial 5% rows (pre/post 2019) | Dual retention: IVA-side statutory anchor = LB-021 (this file); mechanics cross-ref GT-TAX-FR-097 + GT-EINV-FR-036 |
| FR-189 | odoo | account.move (FESP emission) ISR line | 5% excl. IVA; copy = constancia; 10-day | saas validates; emission doc = GT-EINV FESP |
| FR-190 | shared | — (config data §4) | Q30,000/month presumption rows | −50% reducers; oficio inscription utilidades |
| FR-191 | shared | — | dieta retention row (rate = GOQ-60 open) | No rate hard-coded; criterio recorded as interpretation |
| FR-192 | shared | — | historical transitorio rows (valid_to 2013) | 6% substitution + Q2,500 amnesty; non-transmittable |
| FR-193 | shared | — | form-identity cross-ref registry | R46/48_; F-wave owns all filing surfaces |

## 6. Acceptance Criteria

- **AC-001:** Given a lucrativas taxpayer, when régime is resolved, then it
  is exactly one of {Utilidades, Opcional Simplificado}; given no election
  at inscription, then Utilidades applies; given an aviso filed in
  December, then the régime changes on the following 1-January and never
  mid-year. (FR-147, FR-150)
- **AC-002:** Given the Utilidades rate registry read as-of any date, then
  it resolves 31% for FY2013, 28% for FY2014 and 25% from 2015-01-01 —
  each row with valid_to where applicable and provenance "D-10-2012 arts.
  36/172, texto ≤ D-46-2022" — and 31% never resolves for any period
  after 2013-12-31. (FR-152)
- **AC-003:** Given a Utilidades taxpayer electing the presumptive option
  with quarterly rentas brutas Q100,000 of which Q10,000 exempt and
  Q5,000 subject to definitive retention, when the quarterly payment
  computes, then the estimated renta base is 8% of Q85,000 (exempt and
  definitively-retained revenue excluded) and the payment is due within
  the month following quarter end with YTD credit for prior quarters.
  (FR-154, FR-155)
- **AC-004:** Given a loss quarter inside the year, when the next quarter
  closes, then the loss accumulates into that quarter's YTD base; given
  fiscal-year end with a net annual loss, then NO loss amount carries to
  any later year (absence finding) — only capital losses carry (2 years,
  same nature). (FR-155, FR-158, FR-181)
- **AC-005:** Given the Opcional Simplificado scale applied to monthly
  gross Q45,000 (IVA excluded, no exempt revenue), when the retention
  computes, then it equals Q1,500.00 + 7% × Q15,000.00 = Q2,550.00; given
  a single operation of Q2,400.00, then no retention applies and the
  payer may still deduct it. (FR-159, FR-162)
- **AC-006:** Given a payer invoicing a Utilidades taxpayer bearing the
  legend "Sujeto a Pagos Trimestrales", an exempt renta with printed
  legal basis, or a pequeño contribuyente counterpart, when Opcional
  retention runs, then it is suppressed per the 28_ art. 34 matrix.
  (FR-156, FR-165)
- **AC-007:** Given the deduction-cap registry, when a fiscal year closes
  with related-party sueldos at 12% of renta bruta, donations at 6% or
  over Q500,000.00, viáticos at 4%, or an aguinaldo at 150% of monthly
  salary without a homologado pacto colectivo, then each excess is
  non-deductible to the extent over its cap. (FR-167, FR-169)
- **AC-008:** Given an expense whose corresponding ISR retention remains
  unentered, or a salary absent from the IGSS planilla of a
  registration-obliged employer, when deductibility evaluates, then the
  expense is suspended/non-deductible (23.c/23.f gating).
  (FR-168, FR-169)
- **AC-009:** Given a depreciable asset of class 5 (computing equipment),
  then annual depreciation is 33.33% straight-line of the excluded-IVA
  base; given land, then depreciation is refused; given a property
  without building/land split, then the building base is 70% of total;
  given a lower-rate election, then it cannot later be reverted.
  (FR-171..173)
- **AC-010:** Given a capital renta of Q10,000 rent, then the taxable base
  is Q7,000 (30% presumed expenses) and the definitive retention is
  Q700.00 (10%); given a fully-retained capital year, then no capital DJ
  is generated; given a capital loss older than 2 years, then it is dead.
  (FR-177, FR-179, FR-181, FR-182)
- **AC-011:** Given the no-resident matrix, when a royalty payment to a
  non-resident without EP is made, then the retention is 15% definitive
  on the paid amount with no cross-operation compensation, entered by DJ
  within the first 10 días of the following month; given interest from a
  regulated foreign-bank loan, then the 10% band's exemption test
  applies. (FR-183..185)
- **AC-012:** Given a factura especial emitted 2025 for Q10,000 plus IVA,
  then the ISR retention is Q500.00 (5% of the value excluding IVA), the
  document copy serves as constancia, and the retention enters within the
  first 10 días of the following month — with the IVA-side retention
  handled by the Task 3 engine on the same document. (FR-188, FR-189)
- **AC-013:** Given any dieta retention configuration, when inspected,
  then no operative rate is hard-coded anywhere — the GOQ-60 row records
  the question open with the Criterio 6-2018 interpretation flagged as
  non-statutory. (FR-191)
- **AC-014:** Given any surface citing ISR forms, when form identities
  are generated, then annual lucrativas = SAT-1411, capital mensual =
  SAT-1321, no-residentes pago directo mensual = SAT-1371 (R46, 48_) and
  no W4-era plan-map identity (1371-as-anual, 1411-as-asalariados)
  appears anywhere. (FR-153, FR-179, FR-185, FR-193)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
All rows Status open; GOQs are trace-pending, not blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-58 (owned): "LAT post-46-2022 window: any Libro I reform after 27-09-2022 absent (the 47_ 'propinas' hint re-checked here); NOL-absence finding contingent on this window." Affects every dated row (FR-152/154/159/160/167/171/177/178/179..184/188/190) and expressly the FR-158 negative-FR. | no | GT synthesis wave S-GT2 → acquisition queue (current consolidated LAT / DCA) | open |
| OQ-002 | GOQ-59 (owned): "28_ (Reglamento LAT) prints no DCA date; post-AG-167-2014 reforms unverifiable." Affects every 28_-anchored row: FR-151 (art. 7), FR-155/165 (arts. 27/34-35), FR-173..175 (arts. 19/24/25), FR-181/182 (arts. 80/81), FR-186/187 (arts. 84/85), FR-191 (art. 9), FR-192 (arts. 86/87/89). | no | GT synthesis wave S-GT2 → acquisition queue (DCA publication record) | open |
| OQ-003 | GOQ-60 (owned): "Dieta retention 'con carácter definitivo' (28_ art. 9) — operative rate not spelled (5%/7% opcional vs other); determine + SAT practice." Affects FR-191 (rate left unconfigured; Criterio 6-2018's art. 44 application recorded as interpretation only). | no | GT synthesis wave S-GT2 → W6 partner ask (accountant/SAT practice) | open |
| OQ-004 | GOQ-61 (kin, practice forms): 47_-sourced practice signals and 48_ catalog snapshot dating — the SAT-1311/1321/1352/1361/1371/1411 identities herein come from 48_ (R46) and carry the Wayback 2025-10-06 snapshot caveat; re-verify against live RetWeb before F-wave implementation. | no | GT synthesis wave S-GT2 → F-wave form confirmation | open |
