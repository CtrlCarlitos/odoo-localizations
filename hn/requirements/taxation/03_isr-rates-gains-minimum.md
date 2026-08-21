# HN — Taxation — ISR Art. 22-A minimum tax, ganancias de capital & non-resident taxation

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for two clusters of Honduras'
*Impuesto sobre la Renta* (ISR, income tax; Decreto-Ley 25 of 1963,
consolidated through Acuerdo SAR-07-2025). **Cluster T4** — the Art. 22-A
minimum tax on gross receipts for large taxpayers: the max(normal tax,
% × gross) comparator engine; the THREE dated threshold/rate regimes per
R-H32 (FY2018 L300M/1.5%+0.75%; FY2019 L300M–600M band at 0.75% and >L600M
at 1%, sectors 0.5%; FY2020+ L1,000M/1% with 0.5% sectors and the
AT-notification duty); the six-sector reduction catalog; the exclusion
catalog; the resulting tax as the *pagos a cuenta* (advance installment)
base; the SEFIN escape-hatch exception (Apr-30 petition, CNBS category-A/B
audit firm, 60 *días hábiles* (business days) resolution clock); the 22-A
credit/cession mechanics; the café anti-shifting audit duty; and the
recorded supersession tension against D. 17-2010 L-Art 19's 1%-of-net-sales
minimum — an open CONFLICT never resolved silently. **Cluster T5** —
*ganancias de capital* (capital gains) and non-resident taxation: the flat
10% *impuesto único* (single tax) on capital gains for all persons,
domiciled or not; per-transaction payment mechanics (10 *días hábiles* from
perception of the agreed value) plus the April-30 annual consolidation;
same-year loss netting; the value formula (market floor minus *mejoras
comprobadas* (documented improvements) and *gastos de legalización*
(legalization costs)); the State-as-payor 10% retention; the non-resident
real-estate 4% buyer retention; the 13-category non-resident
gross-withholding table (25%/10% — current authority = Ley ISR Art. 5 per
R-H1, the 2010-2012 all-10% window kept as dated historical rows); the
related-party-interest → dividend reclassification; and the *tradición*
(real-property delivery) rescission refund.

It does **not** cover: the PN progressive scale vintages, plantilla and the
resident retention engines 12.5%/1% (`04_isr-withholding.md`,
HN-TAX-FR-121..153); deductions and NOL (file 02, HN-TAX-FR-046..078 —
consumed by id); the dividend 10%, cédular alquiler, enseñanza and
revaluation 6% engines (file 05, cluster T7 — parallel synthesis;
the related-party-interest reclassification of this file hands off to it by
id); ISV (`06_isv.md`, HN-TAX-FR-211..255); selectivo and special regimes
(file 07, clusters T10/T12); the AS/ATN 30-abril package including the 103
form's 22-A selector surface and the GC/ZOLITUR/tradición declaration
surfaces — códigos 119/120/152/138 (W2 clusters F7/F8/F2, future S-HN3
wave — cross-referenced by cluster id only); and the CT procedural chassis
(`01_isr-framework.md`, HN-TAX-FR-001..045 — cesión/compensación gates
FR-039, entero anchor FR-031). Those files reference this one for the
22-A engine and the GC/non-resident rates.

## 2. Legal Basis

Authority order (binding, per master evidence index): ISR = `01_`
(consolidation SAR-07-2025 — current article text) with reform decrees
`80_` (D. 31-2018 transition) and `93_` (D. 31-2019 interp/reforma, per the
R-H15 authority map); Eficiencia = `05_` (Enero-2022 consolidation print —
vintage caveat `05_ OQ-2`, post-2017 reforms unverified); D. 17-2010 family
= `04_` + reglamento `21_` (historical for the non-resident table per R-H1);
SAR Generalidades print `68_` (the 22-A dated-evolution print behind R-H32;
per-row cite only, R-H27 discipline). Binding rulings applied: R-H1
(non-resident table current = `01_` Art. 5; D. 17-2010 all-10% = 2010-2012
window), R-H15 (22-A authority map: current text `01_` + `80_` transition +
`93_` interp), R-H26 PARTIAL (GC non-resident retention 4% per D. 273-2013
Art. 13 → Eficiencia Art. 14 operative; `46_`'s 2% print = unresolved
conflict), R-H32 (three dated 22-A regimes; "(1.05%)" print flagged, 1%
text-primary), R-H11 (financial-transactions contribution = the only
retention-liquidity exception, D. 105/199-2011 permanent — closes E-Art 35's
exception). D-H1/D-H2/D-H3 bind all rows (dated rows, hecho-generador
resolution).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR, Art. 22-A (texto vigente, num. 3): no sujetos los contribuyentes cuyo ingreso bruto del año anterior sea ≤ L1,000,000,000; superior → "pagarán el uno por ciento (1.0%) de los ingresos brutos" cuando el impuesto ordinario del Art. 22 resulte menor al 1.0% de los ingresos brutos declarados; tasa reducida 0.5% para: cemento; servicios públicos prestados por empresas estatales; medicamentos y productos farmacéuticos humanos (productor/importador/comercializador); panadería; derivados del acero para la construcción (excl. chatarra/minería); producción/comercialización/exportación de café. Num. 4 no sujetos: a) personas naturales con ingresos de sueldos y salarios; b) prensa escrita; c) empresas en sus primeros 2 años o en período preoperativo (hasta la primera venta); d) pérdidas por caso fortuito o fuerza mayor, desastres naturales, catástrofes, guerras, estado de excepción (hasta 2 ejercicios, certificadas por firma auditora); e) producción/venta/distribución de petróleo y derivados; f) ingresos bajo el umbral aplicable. Num. 5: el impuesto resultante es base de los pagos a cuenta. Num. 6: ingreso bruto ≥ L100M con pérdidas operativas en 2 períodos alternos o consecutivos → régimen del D. 96-2012. Num. 7: excepción por resolución favorable de SEFIN; crédito fiscal 22-A aplicable a cualquier impuesto de la AT o cedible conforme al Art. 142 del CT | Art. 22-A (current text, num. 3): taxpayers whose prior-year gross income is ≤ L1,000,000,000 are NOT subject; above that, they pay 1.0% of gross income whenever the ordinary Art. 22 tax is less than 1.0% of declared gross; reduced 0.5% rate for six sectors (cement; state-public services; human pharma products; bakery; steel construction derivatives excluding scrap/mining; coffee production/marketing/export). Num. 4 exclusions: salaried natural persons; written press; first-2-years/pre-operational companies until first sale; fortuitous-event/force-majeure losses (natural disasters, catastrophes, wars, states of exception — up to 2 fiscal years, auditor-certified); petroleum producers/distributors; below-threshold cases. Num. 5: the resulting tax is the pagos-a-cuenta base. Num. 6: gross ≥ L100M with operating losses in 2 alternate or consecutive periods → D. 96-2012 regime. Num. 7: SEFIN favorable-resolution exception; the 22-A credit balance applies against any AT tax or is assignable (cesionable) per CT Art. 142 | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 22-A pp.17-21 (EV01:EVID-011; R-H15) |
| LB-002 | D. 31-2018, Art. 1 (texto de reemplazo del Art. 22-A): 1) FY2018 (vs gross del año anterior): ≤L300M no sujetos; sectores reducidos 0.75%. 2) FY2019: rango L300M–L600M → 0.75% cuando el impuesto Art. 22 a)/b) resulte menor al 0.75% del bruto declarado (sectores 0.5%); >L600M → 1.0% (sectores 0.5%). 3) FY2020 y subsiguientes: ≤L1,000M no sujetos; >L1,000M → 1.0% (sectores 0.5%). 5) impuesto resultante = base de pagos a cuenta. 7) excepción SEFIN: solicitud a más tardar el 30 de abril (o fecha de la DJ), 3 pagos a cuenta del año anterior pagados, informe de auditoría fiscal externa de firma inscrita ante la CNBS categoría A o B distinta del auditor de los EEFF, que compruebe que todos los ingresos gravables están registrados y que no existen gastos no deducibles; SEFIN resuelve en un máximo de 60 días hábiles; recursos de reposición/revisión conforme al CT; la reposición agota la vía administrativa. 8) SEFIN actúa sin perjuicio de la fiscalización de la AT/Aduanera. 9) SEFIN emitirá instructivo en un máximo de 20 días hábiles | D. 31-2018, Art. 1 (replacement Art. 22-A text): FY2018 (vs prior-year gross): ≤L300M not subject; reduced-sector rate 0.75%. FY2019: L300M–L600M band → 0.75% when the Art. 22 a)/b) tax is below 0.75% of declared gross (sectors 0.5%); >L600M → 1.0% (sectors 0.5%). FY2020 and after: ≤L1,000M not subject; >L1,000M → 1.0% (sectors 0.5%). The resulting tax = pagos-a-cuenta base. SEFIN exception: petition by April 30 (or the DJ due date), the 3 prior-year pagos a cuenta paid, an external fiscal-audit report by a CNBS-registered category A or B firm DIFFERENT from the EEFF auditor proving all taxable income booked and no non-deductible expenses; SEFIN resolves within at most 60 business days; reposición/revisión recourse per the CT, reposición exhausting the administrative route; SEFIN acts without prejudice to AT/Customs fiscalization; SEFIN to issue an instructivo within 20 business days (→ Instructivo 461-2020 lead) | `hn/sources/80_Decreto_31-2018_reforma_22A.pdf` | D31-Art 1 pp.1-5 (EV05:EVID-070; R-H15) |
| LB-003 | D. 31-2018, Art. 5: "La Administración Tributaria auditará al sector café, a fin de verificar que los efectos del pago del impuesto contemplado en este Decreto no sean trasladados a los productores; en caso de comprobarse la traslación, la Administración Tributaria notificará la cuantía que deberá enterarse" | D. 31-2018, Art. 5: the AT shall audit the coffee sector to verify that the effects of the 22-A tax are not shifted to producers; if shifting is proven, the AT notifies the amount that must be remitted (anti-shifting audit duty backing the coffee sector reduction) | `hn/sources/80_Decreto_31-2018_reforma_22A.pdf` | D31-Art 5 p.8 (EV05:EVID-071) |
| LB-004 | D. 17-2010, L-Art 19 (texto 2010 — HISTÓRICO/con conflicto abierto): personas naturales/jurídicas y comerciantes individuales pagan el ISR "de conformidad al Artículo 22... o el uno por ciento (1%) de las ventas netas del año o el que resultare mayor"; el 1% no deducible; sujeto a pagos a cuenta; instituciones financieras según procedimientos DEI | D. 17-2010, L-Art 19 (2010 text — historical, open conflict): natural/juridical persons and individual merchants pay ISR per Art. 22 OR 1% of the year's NET sales, whichever is greater; the 1% non-deductible; subject to pagos a cuenta. No express derogation vs Art. 22-A exists (`04_ OQ-1` CONFLICT — never resolve silently; the article also carries the 1% purchases-retention mandate and its OCR text is possibly truncated) | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` | L-Art 19 p.6 (EV04:EVID-046) |
| LB-005 | SAR Generalidades ISR (print 68_), secciones 22-A: FY2018 — gross 2017 ">L.300,000,000.00 [...] pagarán el 1.5% de los ingresos brutos siempre y cuando las tarifas del Artículo 22 [...] resulten menor", sectores 0.75%; FY2019 — gross 2018 "en el rango de L.300,000,000.00 a L.600,000,000.00 deben pagar el 0.75% [...]; Superiores a L.600,000,000.00 [...] el 1% de los ingresos brutos declarados, siempre y cuando [...] resultaren menores al uno por ciento (1.05%) [sic]", sectores 0.5%; FY2020+ — ≤L1,000M no sujetos, >L1,000M → 1%, sectores 0.5%; para aplicar la reducción "deberá comunicar a la Administración Tributaria cuál de los productos anteriores produce, distribuye y/o comercializa"; base legal: "Decreto No. 31-2018 / Ley de Impuesto Sobre la Renta / Acuerdo No. SAR-015-2019 / Decreto No. 170-2016" | SAR Generalidades print (68_), 22-A sections: FY2018 — 2017 gross > L300M → 1.5% of gross whenever the Art. 22 rates yield less, sectors 0.75%; FY2019 — 2018 gross in the L300M–L600M range → 0.75%, above L600M → 1% of declared gross (the "(1.05%)" figure is a print defect — 1% text-primary per R-H32), sectors 0.5%; FY2020+ — ≤L1,000M not subject, >L1,000M → 1%, sectors 0.5%; to apply the reduction the taxpayer must notify the AT which of the listed products it produces, distributes and/or markets (the R-H32 "AT-notified" element); sanctions hook CT Arts. 160/163 | `hn/sources/68_Generalidades_ISR.pdf` | 68_ pp.4-9 (EV29:68_ EVID-109; R-H32) |
| LB-006 | Ley ISR, Art. 10 párr. 2: "Las ganancias de capital obtenidas por las personas naturales o jurídicas, domiciliadas o no en Honduras, pagarán un impuesto único del 10%... por lo que no estarán sujetas a la tarifa progresiva"; el Estado, al pagar compras de bienes, indemnizaciones o compra de derechos/títulos, retiene el 10% como impuesto sobre ganancias de capital | Ley ISR, Art. 10 para. 2: capital gains obtained by natural or juridical persons, domiciled or not, bear a single 10% tax and are NOT subject to the progressive tariff; the State, when paying for purchases of goods, indemnities or the purchase of rights/titles, withholds 10% as the capital-gains tax | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 10 pp.9-10 (EV01:EVID-006) |
| LB-007 | Ley ISR, Arts. 4-5: los ingresos brutos de fuente hondureña de no residentes pagan según 13 categorías: 1) arrendamiento de bienes muebles/inmuebles 25%; 2) regalías mineras/canteras/recursos naturales 25%; 3) sueldos, salarios, comisiones u otra compensación por servicios dentro o fuera del territorio, "excluidas las remesas" 25%; 4) utilidades de sucursales/agencias de empresas extranjeras 10%; 5) rentas, utilidades, dividendos o participaciones 10%; 6) regalías de patentes/diseños/fórmulas/marcas/derecho de autor 25%; 7) intereses de operaciones comerciales, bonos, valores 10% — reconocidos al 10% "cuando se paguen a entidades no relacionadas directa o indirectamente, caso contrario se gravarán como dividendos"; 8) transporte aéreo/marítimo/terrestre 10%; 9) comunicaciones, "uso de software, soluciones informáticas, telemáticas" 10%; 10) primas de seguros/fianzas 10%; 11) espectáculos públicos 25%; 12) films/videocinta/derechos de cable 25%; 13) "cualquier otro ingreso de operación" 10%; los pagadores retienen conforme los Arts. 50 y 51; la capitalización de reservas exenta | Ley ISR, Arts. 4-5: non-residents' Honduran-source gross income pays per 13 categories: (1) movable/immovable rent 25%; (2) mining/quarry/resource royalties 25%; (3) salaries, commissions or any service compensation in or out of the territory, remittances excluded, 25%; (4) profits of branches/agencies of foreign enterprises 10%; (5) rents, utilities, dividends or participations 10%; (6) IP royalties 25%; (7) interest on commercial operations, bonds, securities 10% — at 10% only when paid to entities not directly or indirectly related, otherwise taxed AS DIVIDENDS; (8) air/sea/land transport 10%; (9) communications, software use, IT solutions, telematics 10%; (10) insurance/bond premiums 10%; (11) public shows 25%; (12) films/videotape/cable rights 25%; (13) any other operating income 10%; payers are withholding agents per Arts. 50-51; capitalization of reserves exempt (R-H1: current authority) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Arts. 4-5 pp.4-6 (EV01:EVID-003; R-H1) |
| LB-008 | Ley de Eficiencia, E-Art 14 (reformado D. 273-2013 Art. 13 y D. 170-2016 Art. 195): ganancias de capital de personas naturales/jurídicas residentes o no: "tarifa única 10%", fuera de la tarifa progresiva; pago "por cada transacción dentro de los diez (10) días hábiles siguientes en que se percibió el valor pactado"; declaración anual a más tardar el 30 de abril del ejercicio siguiente; las pérdidas de capital se compensan sólo contra ganancias de capital "del mismo ejercicio fiscal"; ámbito: transferencia/cesión/compraventa/negociación de bienes o derechos por personas cuyo giro habitual NO es el comercio de esos bienes; excluida la enajenación de la vivienda habitual; permuta: ambas partes computan su ganancia al valor de transferencia; valor de la transacción = valor pactado no inferior al de mercado, "deduciendo las mejoras comprobadas y gastos de legalización"; enajenaciones de inmuebles/derechos/valores por no residentes: "el adquiriente debe retener el cuatro por ciento (4%) del valor de la transmisión... a cuenta de este impuesto", entero dentro de los 10 días calendario siguientes a la transacción; excepción de reorganización (fusión/absorción/cesión/escisión "al momento de su cambio"); pérdidas excluidas: juegos de azar y autoconsumo; no son ganancias/pérdidas: separación de gananciales; división de copropiedad (valor histórico); reducción de capital con devolución "siempre que sean utilidades no distribuidas previamente" | Efficiency Law, E-Art 14 (as reformed by D. 273-2013 Art. 13 and D. 170-2016 Art. 195): capital gains of resident or non-resident persons bear a single 10% rate outside the progressive tariff; payment per transaction within the ten (10) business days following perception of the agreed value; annual declaration by April 30 of the following fiscal year; capital losses offset only against capital gains of the SAME fiscal year; scope: transfers by persons whose habitual business is not trading those goods; enajenación of the taxpayer's habitual dwelling excluded; barter (permuta): both parties compute their own gain at transfer value; transaction value = agreed value provided not below market, minus documented improvements and legalization costs; non-resident transfers of real estate/rights/securities: the ACQUIRER must retain 4% of the transmission value on account of this tax, remitted within the 10 calendar days following the transaction; reorganization exception (merger/absorption/cesion/escisión at the moment of change); excluded losses: gambling and self-consumption; non-events: marital-property separation, co-ownership division (historical value preserved), capital reduction with devolution only of previously-undistributed profits | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 14 pp.7-9 (EV05:EVID-062; vintage caveat `05_ OQ-2`; R-H26) |
| LB-009 | D. 273-2013, Art. 13 (vía Ayuda 138): "Reformar el artículo [14] párrafo [sexto] de la Ley de Eficiencia... Cuando las enajenaciones de bienes inmuebles o derechos y valores sean realizadas por un no residente, el adquiriente debe retener el cuatro por ciento (4%) del valor de la transmisión de dominio a cuenta de este impuesto. Dicho valor debe ser enterado dentro de los diez (10) días calendario siguiente a la transacción." (el encabezado del articulado en 38_ arrastra defectos de impresión — ver OQ) | D. 273-2013, Art. 13 (as quoted in the Ayuda 138 manual): reforms the Eficiencia Law article so that when disposals of real estate or rights and securities are made by a non-resident, the acquirer must retain 4% of the ownership-transmission value on account of this tax, the amount remitted within the ten (10) calendar days following the transaction — the reform anchor R-H26 relies on for the operative 4% (the 38_ print carries citation defects; the 05_ consolidation header prints a different reform anchor pair, see LB-008 note) | `hn/sources/38_Ayuda_ret_gc_no_residente_138.pdf` | 38-§I.4 p.5 (EV31:38_ EVID-120; R-H26) |
| LB-010 | D. 17-2010, L-Art 4 + Reglamento Acuerdo 1121-2010, R-Arts 7-8 — **HISTÓRICO**: la tabla reglamentaria imprime 10% para TODAS las 13 categorías de no residentes; retención por PJ, comerciantes individuales y profesionales independientes per Arts. 50-51 ISR | D. 17-2010, L-Art 4 + Reglamento R-Arts 7-8 — **HISTORICAL**: the regulatory table prints 10% for ALL 13 non-resident categories (superseded window 2010-2012: D. 17-2010 in vigencia 21-may-2010; displaced by D. 182-2012, Gaceta 04-dic-2012, which restored the 25% categories — R-H1; relevant only for back-dated periods); retention by juridical persons, individual merchants and independent professionals per ISR Arts. 50-51 | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` + `hn/sources/21_Acuerdo_1121-2010_Regl_D17-2010.pdf` | L-Art 4 p.3; R-Arts 7-8 pp.2-3 (EV04:EVID-041; R-H1) |
| LB-011 | D. 17-2010, L-Art 46 (reforma al D. 76-1957, tradición de inmuebles): impuesto sobre el valor de mercado o catastral (el que sea mayor); "el contribuyente tendrá derecho a que se le reembolse el impuesto pagado, si la tradición quedare rescindida dentro de los seis (6) meses siguientes a la fecha en que se realizó" | D. 17-2010, L-Art 46 (amending D. 76-1957, real-property tradición): tax on the market or cadastral value, whichever is higher; the taxpayer has the right to a refund of the tax paid if the tradición is rescinded within the six (6) months following its date (rate and the 152 declaration surface owned by cluster F8, S-HN3) | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` | L-Art 46 p.12 (EV04:EVID-053) |
| LB-012 | Ley de Eficiencia, E-Art 52: los intereses/dividendos por préstamos o aportes de capital para programas de inversión social entre bancos/instituciones financieras reguladas u organismos internacionales de desarrollo "no estarán sujetos a las retenciones establecidas en los numerales 5) y 7) del Artículo 5 de la Ley del Impuesto Sobre la Renta" | Efficiency Law, E-Art 52: interest/dividends on loans or capital contributions for social-investment programs between banks/regulated financial institutions or international development organisms are NOT subject to the Art. 5 numerals 5) and 7) retentions (vintage caveat — Enero-2022 print) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 52 p.19 (EV05:EVID-066) |
| LB-013 | D. 31-2019 (93_), Arts. 1-2 (G 34,932, 30-abr-2019; catalog's "34,934" is an error — pinned EVID-350): Art. 1: "Interpretar el numeral 1) del Artículo 1 del Decreto Legislativo No. 31-2018 [...] en el sentido siguiente: El cálculo del Impuesto Sobre la Renta para el Período Fiscal 2017 se realizará conforme a las reglas del Artículo 9 del Decreto No. 278-2013, el cual adicionó el Artículo 22-A de la Ley del Impuesto sobre la Renta."; considerando 2 recites the original 22-A design: floors "cuando los obligados tributarios obtuvieran ingresos brutos iguales o mayores a DIEZ MILLONES DE LEMPIRAS (L.10,000,000.00)" and the Art. 22 a)/b) tariff "resultaren inferiores al uno punto cinco por ciento (1.5%) o cero punto setenta y cinco por ciento (0.75%) de los ingresos brutos, según corresponde" | FY2017 = the ORIGINAL 22-A regime (D. 278-2013 Art. 9): L10M gross trigger, 1.5%/0.75% floors vs Art. 22 tariffs; D. 31-2018's bands govern FY2018+ only (regime 0 of FR-082, added V-HN1b) | `hn/sources/93_Decreto_31-2019_interp_reforma_D31-2018_22A.pdf` | Arts. 1-2 p.2; considerandos pp.1-2 (EV93:EVID-350/351) |

Dead or superseded text — never implementable as current law (recorded as
LB notes, not FRs, per wave constraint): the D. 17-2010 L-Art 4 / R-Arts 7-8
all-10% non-resident table (LB-010 — superseded window per R-H1; back-dated
rows only). L-Art 19's 1%-of-net-sales minimum (LB-004) is neither dead nor
operative: its displacement by Art. 22-A is an OPEN conflict (`04_ OQ-1`)
carried as OQ-001 — never applied, never deleted silently.

## 3. Functional Requirements

### 3.1 Art. 22-A minimum tax on gross receipts (T4)

- **HN-TAX-FR-081:** The system shall compute, for each fiscal year of a
  taxpayer subject to Art. 22-A, the ISR liability as the GREATER of
  (a) the ordinary Art. 22 tax (25% PJ / progressive PN tracks owned by
  `04_isr-withholding.md` and file 01 FR-010..011) and (b) the applicable
  minimum = minimum-tax rate × the year's declared gross income
  (*ingresos brutos declarados*), where the rate is the general or
  sector-reduced percentage of the regime selected by FR-082/FR-083; when
  the ordinary tax is lower, the minimum governs. (LB-001; LB-002;
  EV01:EVID-011; EV05:EVID-070)
- **HN-TAX-FR-082:** The system shall gate 22-A applicability on the
  PRIOR fiscal year's gross income against a dated regime table (D-H2:
  additive `valid_from`/`valid_to` rows resolved by the fiscal year being
  computed, never replaced in place) with THREE regimes per R-H32:
  regime A (FY2018): prior-year gross ≤ L300,000,000 not subject; above →
  general 1.5%, sectors 0.75%; regime B (FY2019): > L300M split —
  L300M–L600M band at 0.75%, > L600M at 1%, sectors 0.5%; regime C
  (FY2020+): ≤ L1,000,000,000 not subject, above → 1.0%, sectors 0.5%.
  The FY2019 "(1.05%)" print is a defect — 1% text-primary (R-H32); the
  FY2018 general 1.5% is pinned by the 68_ print (LB-005; the 80_
  statutory capture prints only that year's 0.75% reduced rate). **Regime
  0 (FY2017), added V-HN1b from the `93_` evidence read:** FY2017 is
  computed under the ORIGINAL D. 278-2013 Art. 9 rules (authentic
  interpretation D. 31-2019 Art. 1 — EVID-351): antievasión floor when
  ingresos brutos ≥ L10,000,000, at max(Art. 22 a)/b) tariff result,
  1.5%/0.75%-of-gross floors; the D. 31-2018 bands start at FY2018 only.
  Fiscal years before 2017 have no 22-A regime row (see FR-092 for the
  L-Art 19 flag). (LB-002; LB-005; LB-013; EV05:EVID-070;
  EV29:68_ EVID-109; EV93:EVID-350/351; R-H32)
- **HN-TAX-FR-083:** The system shall apply the reduced sector rate only
  to taxpayers flagged with one of the six statutory sectors — cement;
  state public services; human pharma products (producer/importer/
  marketer); bakery; steel construction derivatives (excluding scrap and
  mining); coffee production/marketing/export — and only where the
  taxpayer has notified the AT which of the listed products it produces,
  distributes and/or markets (the R-H32 "AT-notified" duty): an
  unnotified sector flag shall block the reduced rate (general rate
  applies) and surface the notification requirement. (LB-001; LB-005;
  EV01:EVID-011; EV29:68_ EVID-109)
- **HN-TAX-FR-084:** The system shall flag as NOT subject to 22-A the
  num. 4 exclusion classes: natural persons whose income is salaries/
  wages; written press (*prensa escrita*); companies within their first
  two years of constitution or in pre-operational period (until their
  first sale); taxpayers with losses from *caso fortuito o fuerza mayor*
  (fortuitous event or force majeure) — natural disasters, catastrophes,
  wars, states of exception — for up to two fiscal years, certified by an
  audit firm; petroleum and derivatives producers/sellers/distributors;
  and taxpayers below the applicable regime threshold (FR-082).
  (LB-001; LB-005; EV01:EVID-011; EV29:68_ EVID-109)
- **HN-TAX-FR-085:** The system shall treat the 22-A resulting tax
  (FR-081) as the base of the *pagos a cuenta* regime: the December
  *Manifestación de Pagos a Cuenta* and the quarterly minimum (average of
  the last three years' tax, per file 01's calendar chassis) compute on
  the 22-A result whenever the minimum governs (eligibility gate = file 01
  FR-009; calendar surfaces owned by cluster F7, S-HN3 — crossref by id).
  (LB-001; LB-002; EV01:EVID-011)
- **HN-TAX-FR-086:** The system shall raise a loss-pattern flag when a
  taxpayer with gross income ≥ L100,000,000 declares operating losses in
  two alternate or consecutive periods, routing it to the D. 96-2012
  anticipo regime (num. 6 pointer; engine and credit-panel surfaces owned
  by cluster F7 — crossref by id). (LB-001; LB-002; EV01:EVID-011;
  EV05:EVID-070)
- **HN-TAX-FR-087:** The system shall model the SEFIN escape-hatch
  exception as a workflow with hard gates: a petition filed by April 30
  (or the annual DJ due date) of the applicable year, accompanied by proof
  that the three prior-year *pagos a cuenta* were paid, and an external
  fiscal-audit report issued by a CNBS-registered category A or B firm
  DISTINCT from the EEFF auditor certifying that all gravable income is
  booked and no non-deductible expenses exist; SEFIN's resolution deadline
  = petition date + 60 *días hábiles* on the HN business-day calendar;
  denials open the CT recourse ladder (*reposición* — which exhausts the
  administrative route — then *revisión*). A favorable resolution exempts
  the petitioner from 22-A for the petitioned regime. (LB-002; EV05:EVID-070)
- **HN-TAX-FR-088:** The system shall record that a favorable SEFIN
  resolution binds the AT while SEFIN acts WITHOUT prejudice to AT and
  Aduanera fiscalization (num. 8) — the exemption flag coexists with
  audit-exposure tracking, never suppressing fiscalización status.
  (LB-002; EV05:EVID-070)
- **HN-TAX-FR-089:** The system shall maintain the 22-A credit balance in
  the taxpayer's *cuenta corriente tributaria* as applicable against ANY
  AT tax or assignable (*cedible*) per CT Art. 142 — consuming the
  compensación/cesión gates of file 01 FR-039 (credits liquid, due and
  not prescribed) by id, with 22-A as a distinct credit origin.
  (LB-001; LB-002; EV01:EVID-011; EV05:EVID-070)
- **HN-TAX-FR-090:** The system shall expose, for coffee-sector taxpayers
  benefiting from the reduced rate, an anti-shifting audit surface
  recording producer-side cost allocations that could shift the 22-A
  effect to producers, per D. 31-2018 Art. 5 (if the AT proves shifting
  and notifies the *cuantía*, the notified amount becomes a remittance
  obligation on the shifting party). (LB-003; EV05:EVID-071)
- **HN-TAX-FR-091:** The system shall carry the SEFIN petition procedure's
  operative detail (Instructivo Acuerdo 461-2020, mandated by num. 9 to
  issue within 20 días hábiles) as a LEAD config-gap: FR-087's gates stand
  on the D. 31-2018 statutory text; form fields beyond it are marked
  pending-acquisition and never guessed (D-H3 never-guess).
  (LB-002; EV05:EVID-070; OQ-005)
- **HN-TAX-FR-092:** The system shall apply Art. 22-A as the sole
  operative gross-receipts minimum for periods from FY2017 (regime 0
  onward — the D. 31-2019 authentic interpretation confirms 22-A governed
  FY2017 too, V-HN1b; current
  consolidation text; R-H15 authority map) and shall NOT apply the
  D. 17-2010 L-Art 19 1%-of-net-sales minimum to any period by default;
  the L-Art 19 survival question for sub-threshold taxpayers stays an
  OPEN conflict (`04_ OQ-1` — no express derogation; the article's OCR
  text is also possibly truncated and carries the purchases-retention
  mandate): if a controller ruling establishes survival, the 2010 minimum
  enters as an additional dated regime row on the same comparator engine
  — never resolved silently in either direction (OQ-001).
  (LB-004; EV04:EVID-046; OQ-001)

### 3.2 Ganancias de capital: the 10% impuesto único (T5)

- **HN-TAX-FR-093:** The system shall route *ganancias de capital* to the
  flat 10% *impuesto único* track for every person — natural or juridical,
  domiciled or not — outside the progressive tariff and the PJ 25% track
  (rate-track stamp `gc_unico_10` per file 01 §4), gated by scope: the
  transfer/*cesión*/negotiation of goods or rights by persons whose
  habitual business is NOT trading those goods; the *enajenación*
  (disposal) of the taxpayer's habitual dwelling is excluded (no 10% GC
  event); habitual-giro disposals follow the ordinary tracks (file 01
  FR-010..013). (LB-006; LB-008; EV01:EVID-006; EV05:EVID-062)
- **HN-TAX-FR-094:** The system shall compute GC tax per transaction and
  schedule payment within ten (10) *días hábiles* following the date the
  agreed value is perceived (*percibido el valor pactado*) — a
  per-transaction clock on the HN business-day calendar, distinct from
  calendar-day retention deadlines — and shall schedule the annual
  consolidation declaration by April 30 of the following fiscal year
  (declaration/payment surfaces — código 119 Boletín de Pago Libre + DJ —
  owned by cluster F8, S-HN3: crossref by id). (LB-008; EV05:EVID-062)
- **HN-TAX-FR-095:** The system shall net capital losses ONLY against
  capital gains of the SAME fiscal year — no carryforward of the excess to
  any later year — and shall exclude gambling losses and self-consumption
  losses from the netting ledger entirely. (LB-008; EV05:EVID-062)
- **HN-TAX-FR-096:** The system shall determine each GC transaction's
  taxable result as: transaction value − documented improvements
  (*mejoras comprobadas*) − legalization costs (*gastos de legalización*),
  where the transaction value is the agreed value provided it is not below
  market (market value floors the computation); for *permuta* (barter),
  BOTH parties are subjects, each computing its own gain at the transfer
  value. (LB-008; EV05:EVID-062)
- **HN-TAX-FR-097:** The system shall recognize as GC non-events (no tax,
  historical values preserved): separation of marital property
  (*gananciales*); division of co-ownership (*copropiedad*); and capital
  reduction with devolution ONLY to the extent of previously-undistributed
  profits; and shall flag reorganizations — merger (*fusión*), absorption,
  *cesión*, split (*escisión*) — as producing no GC tax at the moment of
  the change. (LB-008; EV05:EVID-062)
- **HN-TAX-FR-098:** The system shall apply the State-as-payor retention:
  when the State pays for purchases of goods, indemnities, or the purchase
  of rights/titles, it withholds 10% as the capital-gains tax on the
  beneficiary's gain (retention-booking engine shared with the
  non-resident table's payer rule, FR-101). (LB-006; EV01:EVID-006)
- **HN-TAX-FR-099:** The system shall compute the non-resident
  real-estate buyer retention at 4% of the transmission value whenever a
  non-resident disposes of real estate, rights or securities
  (*bienes inmuebles, derechos o valores*): the ACQUIRER is the retention
  agent, the retained amount is a payment on account of the seller's 10%
  GC tax (*a cuenta de este impuesto*), and the *entero* (remittance) is
  due within ten (10) días calendario following the transaction — a
  per-transaction deadline shorter than the monthly retention cycle.
  Rate authority: R-H26 PARTIAL — 4% per D. 273-2013 Art. 13 → Eficiencia
  Art. 14 operative; `46_`'s 2% print is an unresolved cross-source
  conflict NEVER encoded (OQ-006). Filing cadence = código 138,
  transaction-triggered (eventual) — cluster F2 surface, crossref by id.
  (LB-008; LB-009; EV05:EVID-062; EV31:38_ EVID-120; R-H26; OQ-006)
- **HN-TAX-FR-100:** The system shall support the *tradición* (delivery)
  of real property tax event and its rescission refund: tax computed on
  the higher of market or cadastral value (rate and the 152 declaration
  surface owned by cluster F8, S-HN3), and where the tradición is
  rescinded within six (6) months of its date, the system shall generate
  the taxpayer's refund claim for the tax paid (refund workflow chassis =
  file 01 FR-034). (LB-011; EV04:EVID-053)

### 3.3 Non-resident withholding table (T5)

- **HN-TAX-FR-101:** The system shall compute retentions on Honduran-source
  gross income of non-resident natural or juridical persons per the
  13-category table of Art. 5 (catalog in §4) — gross basis, no cost or
  expense deduction — at 25% or 10% by category, withheld by the payer as
  agent per ISR Arts. 50-51, with the *entero* riding the general
  10-días-calendario monthly retention anchor owned by file 01 FR-031 /
  `04_isr-withholding.md` (the ONLY instrument exempt from that cycle is
  the financial-transactions contribution per R-H11 — no ISR retention
  enjoys a different deadline). Character: encoded as definitive payment
  (gross-basis, no annual netting surface in corpus) with the
  definitive-vs-*anticipo* verification marker preserved (OQ-003).
  (LB-007; EV01:EVID-003; R-H1; R-H11; OQ-003)
- **HN-TAX-FR-102:** The system shall source the category rates from dated
  vintage rows: current vintage = the 25%/10% mix of `01_` Art. 5
  (restored by D. 182-2012, Gaceta 04-dic-2012 — R-H1); historical
  vintage = the D. 17-2010 all-10% window (valid from vigencia 21-may-2010
  through the D. 182-2012 cutover), applicable ONLY to back-dated period
  computations (D-H2: resolved by the retention's hecho-generador date;
  snapshot-on-write per D15). The exact vigencia convention of the 2012
  decree (gazette date vs lag) is unpinned — the cutover row is dated at
  the gazette and flagged for verification before 2012-edge computations.
  (LB-007; LB-010; EV01:EVID-003; EV04:EVID-041; R-H1)
- **HN-TAX-FR-103:** The system shall reclassify numeral-7 interest paid
  by a resident payer to a DIRECTLY or INDIRECTLY related foreign creditor
  out of the 10% interest category and into DIVIDEND treatment
  ("caso contrario se gravarán como dividendos") — a retention-character
  and declaration-surface reclassification feeding the dividend engine
  owned by file 05 (cluster T7) by id; only unrelated-creditor interest
  retains the numeral-7 10% treatment. (LB-007; EV01:EVID-003)
- **HN-TAX-FR-104:** The system shall exempt from the Art. 5 numeral-5 and
  numeral-7 retentions the interest/dividends on loans or capital
  contributions for social-investment programs paid between banks/
  regulated financial institutions or international development organisms
  (E-Art 52; Enero-2022 consolidation print — vintage caveat `05_ OQ-2`,
  re-verify on acquisition of a later consolidation). (LB-012;
  EV05:EVID-066)

## 4. Data Model

Machine-readable sidecars (the regime/vintage tables below as CSV/JSON)
live next to this markdown file when produced. Dated statutory values are
additive `valid_from`/`valid_to` rows resolved by the computation's fiscal
year or the retention's hecho-generador date (D-H2), snapshot-on-write (D15).

**Art. 22-A dated regime rows (verbatim anchored, R-H32):**

| Regime | Fiscal years | Prior-FY gross gate | General rate | Sector rate |
|--------|--------------|---------------------|--------------|-------------|
| A | 2018 | ≤ L300,000,000 not subject; > L300M subject | 1.5% | 0.75% |
| B | 2019 | ≤ L300M not subject; L300M–L600M → 0.75%; > L600M → 1% | 0.75% / 1% (banded) | 0.5% |
| C | 2020+ | ≤ L1,000,000,000 not subject; > L1B subject | 1.0% | 0.5% |

Notes: FY2019 "(1.05%)" = print defect, 1% text-primary (R-H32); regime C
sector reduction requires the AT product notification (FR-083); pre-2018 =
no regime row (FR-092 flag for L-Art 19).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isr.22a.regime (new) | name · valid_from · valid_to · band_floor · band_ceiling · rate_general · rate_sector · note | char/dates/monetary/percent | three seeded regimes A/B/C (above); banded regime B = two rows | FR-082 |
| l10n_hn.isr.22a.sector (new) | code · name_es · valid_from | select catalog | cement · steel_construction_deriv · state_public_services · pharma_human · bakery · coffee | FR-083 |
| res.company | hn_isr_22a_sector | m2o (nullable) | six-sector catalog; drives reduced rate | FR-083 |
| res.company | hn_isr_22a_sector_notified_on | date | AT product-notification date; null → general rate enforced | FR-083 |
| res.company | hn_isr_22a_exclusion | select (nullable) | salaried_pn · written_press · first_2y_preoperational · force_majeure_2fy · petroleum · below_threshold | FR-084 |
| l10n_hn.isr.22a.computation (new) | company · fiscal_year · prior_fy_gross (snapshot) · regime_id · ordinary_tax · minimum_tax · resulting_tax · is_pagos_a_cuenta_base | m2o/year/monetary/computed | annual comparator run; prior_fy_gross snapshotted (D15) | FR-081, FR-085 |
| l10n_hn.sefin.22a.exception (new) | company · petition_date (≤ Apr-30/DJ date) · pagos_paid_count (≥3 gate) · audit_firm_id · cnbs_category (A/B) · distinct_from_eeff_auditor (constraint) · resolution_due · status · recourse | dates/m2o/select | status: draft · filed · favorable · denied; recourse: reposicion · revision | FR-087, FR-088 |
| l10n_hn.cuenta.corriente (file 01 entity) | credit origin value `isr_22a` | catalog extension | applicable to any AT tax; cession via l10n_hn.credit.move gates (file 01 FR-039) | FR-089 |
| l10n_hn.isr.22a.loss.flag (computed) | gross ≥ L100M ∧ operating losses in 2 alternate/consecutive FYs | boolean + FY pair | routes to D. 96-2012 anticipo (cluster F7 consumer) | FR-086 |

**Ganancias de capital (per-transaction):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (disposal) | hn_gc_agreed_value · hn_gc_market_value · hn_gc_mejoras · hn_gc_legalization_costs · hn_gc_taxable_gain | monetary (gain computed) | value = max(agreed, market) − mejoras − gastos | FR-093, FR-096 |
| account.move (disposal) | hn_gc_perception_date · hn_gc_payment_due | date (due computed) | due = perception + 10 días hábiles (HN business calendar) | FR-094 |
| account.move (disposal) | hn_gc_annual_consolidation_year | year/FK | Apr-30 annual consolidation set (surface = cluster F8) | FR-094 |
| account.move (GC loss) | hn_gc_loss_year (locked = transaction FY) | year | same-year netting only; no carryforward rows ever created | FR-095 |
| account.move (disposal) | hn_gc_excluded_loss | boolean/multi | gambling · self_consumption — never enter netting | FR-095 |
| account.move (disposal) | hn_gc_nonevent | select (nullable) | gananciales_separation · copropiedad_division · capital_reduction_undistributed · reorganization | FR-097 |
| account.move (disposal) | hn_gc_habitual_dwelling | boolean | true → excluded from GC track | FR-093 |
| account.move / account.payment | hn_state_gc_retention_10 | monetary (computed) | State-payor purchases/indemnities/rights purchases | FR-098 |
| account.move (purchase from non-resident) | hn_nr_buyer_retention_4pct · hn_nr_transmission_value · hn_nr_entero_due | monetary/date | retention = 4% × transmission value; entero = transaction + 10 días calendario; applied against seller's GC | FR-099 |
| account.move (tradición) | hn_tradicion_base · hn_tradicion_date · hn_tradicion_rescinded_within_6m · refund_claim_id | monetary/date/boolean/m2o | base = max(market, catastral); refund via file 01 FR-034 chassis | FR-100 |

**Non-resident 13-category catalog (current vintage = `01_` Art. 5, R-H1):**

| Cat | Concept (Spanish anchor) | Rate |
|-----|--------------------------|------|
| 1 | Arrendamiento de bienes muebles/inmuebles | 25% |
| 2 | Regalías mineras/canteras/recursos naturales | 25% |
| 3 | Sueldos, salarios, comisiones u otra compensación por servicios (excl. remesas) | 25% |
| 4 | Utilidades de sucursales/agencias de empresas extranjeras | 10% |
| 5 | Rentas, utilidades, dividendos o participaciones | 10% |
| 6 | Regalías de patentes/diseños/fórmulas secretas/marcas/derecho de autor | 25% |
| 7 | Intereses de operaciones comerciales, bonos, valores (sólo acreedores NO relacionados) | 10% |
| 8 | Ingresos de operación de transporte aéreo/marítimo/terrestre | 10% |
| 9 | Comunicaciones; uso de software, soluciones informáticas, telemáticas | 10% |
| 10 | Primas de seguros y fianzas | 10% |
| 11 | Espectáculos públicos | 25% |
| 12 | Films, videocinta, derechos de cable | 25% |
| 13 | Cualquier otro ingreso de operación | 10% |

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isr.nonresident.category (new) | code (1-13) · rate_pct · valid_from · valid_to | int/percent/dates | current vintage from D. 182-2012 cutover; 2010-05-21→cutover vintage = all rows 10% | FR-101, FR-102 |
| account.move.line | hn_isr_nonresident_category | m2o (nullable) | drives gross-basis retention on Honduran-source non-resident income | FR-101 |
| account.move.line | hn_nr_related_party_interest | boolean | true → dividend reclassification to file 05 engine | FR-103 |
| account.move.line | hn_nr_social_program_exempt | boolean | E-Art 52 numeral-5/7 exemption flag | FR-104 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living
in the LGPL client. No `saas`/`shared` rows are introduced: none of these
FRs touch a transmission/DTE surface (the only architecture-split surface
per
[saas-thin-client-architecture.md](../../../shared/docs/saas-thin-client-architecture.md));
declaration surfaces (códigos 119/138/152, 103 selector) are cluster
F7/F8/F2 property of the S-HN3 wave, consumed by id. Models are stable
across Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-081 | odoo | l10n_hn.isr.22a.computation | comparator compute | max(ordinary, rate×declared gross); ordinary tax consumed from the 04-file engine by id |
| FR-082 | odoo | l10n_hn.isr.22a.regime | dated rows | Version regime (D12): three seeded regimes (2018/2019/2020+), additive rows, never overwritten (D-H2); prior_fy_gross snapshot (D15); "(1.05%)" print defect never seeded |
| FR-083 | odoo | res.company + l10n_hn.isr.22a.sector | sector flag + notification date | Reduced rate blocked while notification date null; six-sector catalog seeded |
| FR-084 | odoo | res.company | hn_isr_22a_exclusion | first-2y/preoperational auto-flags from company start_date + first-sale event |
| FR-085 | odoo | l10n_hn.isr.22a.computation | is_pagos_a_cuenta_base | December manifestación/quarterly minimum consume the result (calendar = cluster F7) |
| FR-086 | odoo | computed flag on computation records | loss-pattern pair | Consumer = D. 96-2012 anticipo panel (cluster F7) |
| FR-087 | odoo | l10n_hn.sefin.22a.exception | gates + timer | 60-días-hábiles clock needs the HN business-day calendar (shared with file 01 FR-045); constraint audit_firm ≠ EEFF auditor; Instructivo fields = config gap (FR-091) |
| FR-088 | odoo | l10n_hn.sefin.22a.exception | status semantics | favorable binds AT; fiscalización tracking never suppressed |
| FR-089 | odoo | l10n_hn.cuenta.corriente + l10n_hn.credit.move | origin `isr_22a` | Any-AT-tax application + CT-142 cession via file 01 FR-039 gates |
| FR-090 | odoo | coffee-sector audit worksheet | data surface | Awareness-level: allocations feed AT-notification exposure records |
| FR-091 | odoo | l10n_hn.sefin.22a.exception | LEAD marker | Config-gap flags; never-guess (D-H3) |
| FR-092 | odoo | l10n_hn.isr.22a.regime | absence + reversible row | L-Art 19 never seeded by default; controller-ruled survival would add a dated regime B-1910 row on the same comparator (OQ-001) |
| FR-093 | odoo | account.move (disposal) | hn_gc routing | Track stamp `gc_unico_10` (file 01 §4); habitual-dwelling + habitual-giro gates |
| FR-094 | odoo | account.move (disposal) | perception + due dates | 10-días-hábiles timer on HN business calendar; Apr-30 consolidation set exported to cluster F8 by id |
| FR-095 | odoo | GC loss lines | same-year netting | Ledger closes at FY-end; no carryforward table exists |
| FR-096 | odoo | account.move (disposal) | value formula fields | max(agreed, market) floor; mejoras/legalización deductions; permuta dual postings |
| FR-097 | odoo | account.move (disposal) | hn_gc_nonevent | Non-event + reorganization flags suppress the 10% compute |
| FR-098 | odoo | account.payment (State payor) | state_gc_retention_10 | Payor = State entities (partner flag) |
| FR-099 | odoo | account.move (purchase) | 4% retention fields | Per-transaction 10-días-calendario entero (distinct from monthly cycle); 2% never encoded (R-H26/OQ-006); 138 eventual filing = cluster F2 |
| FR-100 | odoo | account.move (tradición) | base + refund claim | Rate/surface owned by cluster F8; refund via file 01 FR-034 chassis |
| FR-101 | odoo | l10n_hn.isr.nonresident.category + account.move.line | category retention | Gross-basis compute; entero via the 04-file anchor by id; character marker OQ-003 attached |
| FR-102 | odoo | l10n_hn.isr.nonresident.category | vintage rows | D-H2 resolution by hecho-generador date; 2012-cutover convention flag |
| FR-103 | odoo | account.move.line | related-party reclass | Handoff to file 05 (T7) dividend engine by id |
| FR-104 | odoo | account.move.line | social-program exemption | Vintage caveat from the 05_ Enero-2022 print |

Version-regime notes (D12): FR-082/FR-102 carry the dated-regime/vintage
contracts (regimes A/B/C with Jan-1-of-FY effectivity; non-resident table
vintages with the D. 182-2012 cutover); FR-087's clock and FR-094's timer
require the HN business-day calendar (hábil) vs calendar-day math elsewhere
— encoded per-instrument per `04_ OQ-3` discipline. D15/D16: every dated
parameter resolved as-of its anchor date and snapshotted on write; retro
computations re-resolve original-period rows.

## 6. Acceptance Criteria

- **AC-001:** Given a PJ subject to 22-A in FY2026 (prior-FY gross
  L1.4B) with current-FY declared gross L1.2B and ordinary Art. 22 tax
  L9.0M, then the minimum = 1.0% × L1.2B = L12.0M > L9.0M, the FY2026 ISR
  = L12.0M, and that result becomes the pagos-a-cuenta base (FR-081,
  FR-085).
- **AC-002:** Given the same company flagged coffee-sector with AT
  notification on file, then the minimum = 0.5% × L1.2B = L6.0M < L9.0M
  ordinary → the ordinary L9.0M governs (max semantics); given the same
  sector flag with NO notification date, then the general 1.0% applies and
  the notification requirement is surfaced (FR-081, FR-083).
- **AC-003:** Given prior-FY (2025) gross of L900M, then FY2026 is not
  subject to 22-A (regime C threshold L1B) and only the ordinary track
  runs; given prior-FY gross L1.1B, then the FR-081 comparator runs
  (FR-082).
- **AC-004:** Given a back-dated FY2019 computation with 2018 gross
  L450M, then regime B selects the 0.75% band (not 1%, and never a
  "1.05%" rate); given 2018 gross L700M, then 1% applies with sectors at
  0.5% (FR-082, R-H32).
- **AC-005:** Given a FY2017 computation with ingresos brutos L12,000,000
  whose Art. 22 tariff result is below 1.5% of gross, then regime 0 applies
  and the 22-A floor computes at 1.5% of gross (D. 278-2013 Art. 9 rules
  per D. 31-2019 Art. 1); given gross L8,000,000, then no floor (below the
  L10M trigger); given a FY2016 computation, then no 22-A regime row exists
  and the L-Art 19 open-conflict marker (OQ-001) is recorded on the run
  (FR-082, FR-092).
- **AC-006:** Given a pre-operational company two years from constitution
  with no sales, then 22-A does not apply; given its first sale occurs in
  the third year with prior-FY gross below threshold, then it remains not
  subject; a petroleum-products distributor is never subject regardless of
  gross (FR-084).
- **AC-007:** Given a SEFIN petition filed 12-March with only 2 of 3
  prior-year pagos a cuenta paid, then the exception workflow blocks
  submission as incomplete; given all gates satisfied (3 pagos paid,
  CNBS-B firm distinct from the EEFF auditor, qualifying report), then the
  resolution deadline = filing date + 60 días hábiles on the HN business
  calendar, and a favorable outcome sets the exemption while
  fiscalization tracking remains active (FR-087, FR-088).
- **AC-008:** Given a 22-A credit balance of L2M, then it is applicable
  against any AT tax liability (e.g. ISV) or assignable per CT Art. 142
  through the liquid/due/not-prescribed gates, and never expires by
  default earlier than the prescription horizons of file 01 FR-040
  (FR-089).
- **AC-009:** Given a non-habitual disposal with agreed value L500,000,
  market value L520,000, documented improvements L30,000 and legalization
  costs L8,000, then the transaction value is floored at L520,000, the
  taxable gain = L520,000 − L30,000 − L8,000 = L482,000, and the tax =
  10% × L482,000 = L48,200 (FR-093, FR-096).
- **AC-010:** Given the agreed value perceived 5-March-2026, then the
  L48,200 payment is due within 10 días hábiles (19-March-2026 on the HN
  business calendar absent holidays), and the transaction enters the
  fiscal-year consolidation set due 30-April-2027 (FR-094).
- **AC-011:** Given 2026 GC losses of L100,000 and 2026 GC gains of
  L40,000, then 2026 nets to zero taxable gain with the L60,000 excess
  expiring (no carryforward), and 2027 gains of L50,000 are taxed in full
  (L5,000); given a 2026 gambling loss, then it never enters the netting
  ledger (FR-095).
- **AC-012:** Given the enajenación of a taxpayer's habitual dwelling,
  then no GC event is booked; given a merchant's disposal of goods of its
  own giro, then the ordinary track (not GC) applies (FR-093).
- **AC-013:** Given a permuta of two non-habitual assets, then each party
  computes its own gain at the transfer value and each owes its own 10%
  (FR-096).
- **AC-014:** Given a non-resident paid L1M mining royalties and L1M
  software-use fees, then the retentions = L250,000 (25%, cat. 2) and
  L100,000 (10%, cat. 9) on gross, with no deduction surface (FR-101).
- **AC-015:** Given the same royalties earned in 2011 (back-dated), then
  the retention = 10% under the all-10% window vintage, not 25%
  (FR-102).
- **AC-016:** Given L500,000 interest paid to a directly related foreign
  creditor, then the payment is reclassified to dividend treatment
  (file 05 engine) and never retains the numeral-7 10% interest treatment;
  given a bank-to-bank social-investment-program loan between regulated
  financials, then no numeral-5/7 retention applies (FR-103, FR-104).
- **AC-017:** Given a non-resident's real-estate disposal with
  transmission value L10M, then the buyer retains L400,000 on account of
  the seller's GC tax, remits it within 10 días calendario of the
  transaction, and a 2% computation never occurs (R-H26; OQ-006 marker
  attached) (FR-099).
- **AC-018:** Given a State entity paying L1M for the purchase of rights,
  then it withholds L100,000 as the beneficiary's GC tax (FR-098).
- **AC-019:** Given an asset contribution in a fusión effective FY2026,
  then no GC tax books at the change moment; given a capital reduction
  returning only previously-taxed/undistributed-profit amounts, then it is
  a non-event (FR-097).
- **AC-020:** Given a tradición taxed and then rescinded 4 months after
  its date, then the system generates the refund claim for the tax paid
  (within the 6-month statutory window); given rescission at month 7, then
  no refund claim (FR-100).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | L-Art 19 vs Art. 22-A displacement (origin `04_ OQ-1`, register C1 — CONFLICT): D. 17-2010 Art. 19's 1%-of-NET-sales minimum (no threshold, all taxpayers) has no express derogation, while 22-A (later, specific, threshold-gated) is the current consolidation's operative minimum. FR-092 encodes 22-A-only as the operative default with the 2010 minimum never applied and never deleted — a controller ruling either way adds/removes a dated regime row, never a silent branch. Residual: the article's OCR text (it also carries the 1% purchases-retention mandate) must be checked against the original print before ruling. | no (default reversible) | controller (ruling) | open |
| OQ-002 | GC instrument map (origin `01_ OQ-2`, register C1 — VERIFY): which instrument governs which GC transaction class — Ley ISR Art. 10 (rate: 10% impuesto único, all persons) vs the D. 17-2010-era GC-10% regime carried forward in Eficiencia E-Art 14. This file encodes rate = `01_` Art. 10 / mechanics = E-Art 14 (LB-008); final confirmation requires the un-acquired ISR Reglamento ("Acuerdo N°799" — `07_ OQ-3`/`13_ OQ-2` kin). **W8/R-H83:** the instrument is IDENTITY-DECODED via the official congreso inventory (`119_` entry 324, EV119:EVID-479): Reglamento Ley ISR = **Acuerdo 799, G 19,972 (13-ene-1970)**, derogating the 1955 reglamento, its Art. 33 reformed by Acuerdo 6-B (G 21,505 4-feb-1975); the "799-1963"-style year suffixes in manual citations = slips (1963 = the LEY's year). TEXT still unacquired (1970 gazette, pre-ENAG) — citations remain print-based, never asserted as acquired text. | no | Takumi S-HN1 (acquisition queue, identity pinned) | open |
| OQ-003 | Art. 5 non-resident character (origin `01_ OQ-3`, register C1 — VERIFY): are the 25/10 retentions definitive payments or anticipos (Arts. 50-51 call retentions "anticipos")? FR-101 encodes definitive (gross basis, no annual-netting surface in corpus — Ayuda 138 introduces the Art. 5 table without reproducing it, EV31:38_ EVID-120) with the marker preserved; re-verify at the S-HN3 F2 wave against the 122-134/138 card semantics. | no | Takumi S-HN3 (F2) | open |
| OQ-004 | GC mechanics locus (origin `05_ OQ-3`, register C1 — VERIFY): `01_` Art. 10 is rate-sparse while `05_` E-Art 14 (per-transaction clock, Apr-30 annual, value formula, 4%) is the mechanics-rich text — but from the Enero-2022 consolidation print (`05_ OQ-2`: post-2017 reforms unverified). FR-094/096/099 stand on E-Art 14 with the vintage caveat; re-verify per-article when a later consolidation or the ISR Reglamento lands. | no | Takumi S-HN1 | open |
| OQ-005 | Instructivo Acuerdo 461-2020 (origin `05_ OQ-4`, register C1 — LEAD): the operative SEFIN 22-A-petition procedure instrument — needs La Gaceta date → ENAG acquisition. FR-087's gates stand on the D. 31-2018 Art. 1 statutory text; FR-091 carries the config gap. (D. 31-2019 = `93_` acquired per register; its delta over the `01_` consolidated 22-A text was not re-verified in this wave — regime rows follow R-H32/`01_`.) | no | acquisition queue | open |
| OQ-006 | GC non-resident retention rate conflict (origin `46_ OQ-1`, register C2 — CONFLICT, R-H26 PARTIAL): `46_` Ayuda prints 2% for the non-resident inmueble/derechos retention vs the 4% of D. 273-2013 Art. 13 → Eficiencia E-Art 14 (05_/38_ prints). 4% is operative (R-H26); 2% is never encoded and stays flagged until SAR corrects/reconfirms the Ayuda print. | no | controller + S-HN3 (F8 re-print watch) | open |
| OQ-007 | FY2026 composite sole-source gate (origin `01_ OQ-6`, register C1 — CONFIG; R-H9 kin): L40,000 + exempt-band L228,324.32 = L268,324.32 computed, no SAR print yet — dated config; the primary home of this OQ is `04_isr-withholding.md` OQ-005 (FR-135 computes from components); carried here as register pointer only (this file's non-resident engines are unaffected). | no | Takumi S-HN1 (file 04 lead) | open (pointer) |
| OQ-008 | NEW (synthesis finding): foreign transport companies face BOTH Art. 5 numeral 8 (10% gross retention on transport operating income, LB-007) and Art. 22.c (presumed net = 10% of gross taxed at 25% — file 01 FR-012, LB-006 of file 01): the reconciliation (retention-as-final vs retention-against-annual-presumed-net credit) is stated nowhere in the corpus. No default interaction encoded; flag for a ruling or the ISR Reglamento acquisition. | no | controller | open |
