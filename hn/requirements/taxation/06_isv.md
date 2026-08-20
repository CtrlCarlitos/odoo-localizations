# HN — Taxation — ISV core & liquidation regime (sales tax)

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for Honduras' *Impuesto sobre
Ventas* (ISV, sales tax — D.L. 24-1963, consolidated through D.L. 59-2022):
the non-cumulative multi-stage frame; the *venta* (sale) concept including
*autoconsumo / retiro* (self-supply / withdrawal for own use); *base
imponible* (taxable base) composition — finance-charge exclusion, import
CIF + duties + *selectivo* (consumption tax) composition, effective
discounts, returnable packaging — with the market-price floor and
related-party *plaza* (market) pricing; the *hecho generador* (taxable
event) triggers — invoice-else-delivery for goods, earliest-of
invoice/performance/payment for services (advances trigger), retirement
date for self-supply, *nacionalización* (customs clearance) for imports,
used-goods import-only rule; the rate matrix 15% / 18% / 0% (exports) with
the D. 17-2010 12%-tier rows retained as dated history (R-H2); the 0.005
rounding rule; RTN registration; the exemption surface (Anexo I SAC-coded
*canasta básica* (basic-basket goods) plus goods/services schedules,
prepared food expressly taxable, rent carve-outs at L5,000); service
territoriality (partial-presence rule); 5-year document retention; and the liquidation regime (master-index clusters T8 + T9): *débito
fiscal* − *crédito fiscal* (output tax − input credit) with the 4-month
credit window, the pro-rata mixed-activity rule, the ISR-cost bar, credit
non-transferability with the merger exception, and *Orden de Compra
Exenta* (OCE) exporters; the OTCD card-retention regime (10%-of-tax + the
15% no-discrimination fallback); the monthly *declaración jurada* (sworn
declaration) 10-day cycle; the *Régimen Simplificado* (simplified regime)
gates — informative per R-H23; consumer tax-in-price display; and the 8%
card-purchase *devolución* (refund) regime (alive per R-H22).

It does **not** cover: ISR (the rest of this wave's taxation set, clusters
T1-T7 — interfaces cross-referenced by cluster id); the *selectivo* family
itself (cluster T10 — the selectivo-in-ISV-base stacking interplay is
carried here as OQ-004 with the `98_/99_/100_` cross-check hint); CT
procedure/sanctions/prescription (cluster T11 — the CT Arts. 129/131
refund gate cross-referenced by id); facturación document content,
including the zero-discrimination invoice duty (W3 clusters E4/E5, S-HN2
wave — crossref by id, not restated); and the declaration surfaces
ISV-201 / RS-202 / tarjetas 215-523 (W2 clusters F4/F5, S-HN3 — crossref
by id).

## 2. Legal Basis

Authority order (binding, per master evidence index): ISV = `02_` (D.L.
24-1963 DNJ consolidation through D.L. 59-2022, 26-jul-2022 — current
authority for every article cited below); D. 17-2010 L-Arts 13-18 (`04_`)
= rate HISTORY only (R-H2 — never feed the 12% rows to current periods);
Ley de Eficiencia (`05_`, print Enero-2022, vintage caveat 05_ OQ-2)
supplies the devolución-8% text (E-Art 3) and the OTCD origin instrument
(E-Art 4 — cite `02_` Art. 8 for current text, `05_` for origin); E-Arts 5
and 10 of Eficiencia are VOID dead text (R-H3/R-H4). CT D. 22-97 Art. 222
moved the old ISV administrative/sanction block (Arts. 18/20-27) into the
Código Tributario (R-H13) — procedure/sanction interfaces cite T11 by id.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISV (D.L. 24-1963, texto consolidado), Arts. 1-2 | Tax on sales "en forma no acumulativa en la etapa de importación y en cada etapa de venta" (non-cumulative at import and at each sale stage); venta = any onerous transfer of dominion regardless of contract name or payment form, INCLUDING taxable services and "el consumo o uso por el importador de las mercaderías que introduzca al país, o por el industrial o productor de las mercaderías o productos que, respectivamente, elabore o produzca" (self-supply) unless expressly exempt | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Arts. 1-2 p.4 (EVID-016) |
| LB-002 | Ley ISV, Art. 3 | Base: a) goods/services = value EXCLUDING "gastos directos de financiación ordinaria o extraordinaria" (direct ordinary/extraordinary financing charges); b) imports = CIF + arancelarios + selectivos + específicos + demás cargos; c) self-use/self-supply/gifts = commercial value; NOT in base: "descuentos efectivos que consten en la factura o documento equivalente" (customary) and returnable packaging | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 3 pp.4-5 (EVID-016) |
| LB-003 | Ley ISV, Art. 4 | Absent invoice, or invoice below market → the AT uses "el precio de mercado en plaza" (market price in the local market) *salvo prueba en contrario* (unless proven otherwise) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 4 p.5 (EVID-016) |
| LB-004 | Ley ISV, Art. 5 | Sales to administrators, council members, *socios* (partners), *comisarios*, relatives or spouse "se gravarán a los precios normales de plaza" (taxed at normal market prices) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 5 p.5 (EVID-017) |
| LB-005 | Ley ISV, Art. 5-A | Taxable event: a) goods = "la fecha de emisión de la factura o documento equivalente y, a falta de éste, en el momento de la entrega" (invoice date, else delivery — even with *reserva de dominio* (title reservation) or *retroventa*); b) services = invoice date OR service date OR payment/*abono* — "dependiendo de cual se realice primero" (whichever occurs first); c) self-use/fixed-asset incorporation = retirement date; d) imports = nacionalización/póliza payment; e) used goods taxed only on import (then a cost); internal resale of used goods NOT taxed | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 5-A pp.5-6 (EVID-017) |
| LB-006 | Ley ISV, Art. 6 | "La tasa general del impuesto es del quince por ciento (15%)"; 18% on import/sale of cerveza, aguardiente, licor compuesto y otras bebidas alcohólicas, cigarrillos — beer/sodas applied "sobre el precio de venta en la etapa de distribuidor, incluyendo el valor del impuesto de producción y consumo" (on the distributor-stage sale price including the production-and-consumption tax), collected "a nivel de productor y en la importación al momento de liquidación y pago"; cigarettes at wholesale-stage price; domestic air tickets collected at emission/boarding, airlines = withholding agents depositing within 10 días calendario; business/first/class-beyond-economy international+national tickets = 18%; exports "se calculará a tasa cero" with credit/refund right on inputs "cuando el productor sea el mismo exportador" (producer-exporter condition) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 6 pp.6-8 (EVID-018) |
| LB-007 | D. 17-2010, L-Arts 13-18 — **HISTORICAL (rate history)** | 2010-vintage telecom scales: 12% postpaid ≤US$40 / 15% above; prepaid 12%; internet ≤1.024 Mbps 12% / above 15%; TV-by-subscription ≤L500 12% / above 15%; residential electricity >750 kWh = 12% (2010 vintage; current 02_ text = NOT exempt, i.e. general 15%); air premium classes 18% (current). All 12% tiers later HOMOGENIZED to 15% (R-H2): cite `02_` for current rates; this family only as dated history rows | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` | L-Arts 13-18 pp.5-6 (EVID-047; R-H2) |
| LB-008 | Ley ISV, Art. 7 | All responsables (except Régimen Simplificado, Art. 11-A) must issue "factura o documento equivalente" for sales/services; seller registers tax "en una cuenta especial... a la orden del Fisco" (special account at the order of the Treasury); to final consumers "el impuesto será incluido en el precio final" (tax included in the final price); computer records/*máquinas registradoras* (cash registers) allowed with AT notice + requirements; defective invoices → AT may disable machines/documents, forcing print-shop printing meanwhile | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 7 pp.8-9 (EVID-019) |
| LB-009 | Ley ISV, Art. 8 | Responsables: sellers, service providers, importers/customs agents; simplified sellers ≤L250,000 = not collection agents; AT may appoint productores/wholesalers as *percepción* (collection-at-source) agents on consumer-final-price base (goods then not re-taxed downstream); OTCD card issuers/operators/concessionaires = retention agents: automatic "retención del diez por ciento (10%) sobre el monto total del Impuesto Sobre Ventas que sea discriminado" (10% of the total discriminated ISV) in affiliates' taxable transactions, remainder reimbursed, retention comprobante preserves affiliate credit; systems must force ISV discrimination "incluso cuando el mismo sea igual a cero (0)"; affiliates must register ISV even at zero; no discrimination → OTCD applies 15% automatically; all-exempt affiliates need AT exclusion resolution; monthly banking entero "dentro de los primeros diez (10) días calendario del mes siguiente"; AT may also appoint habitual buyers as retention agents (total or partial) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 8 pp.9-12 (EVID-020) |
| LB-010 | Ley ISV, Arts. 9-10 | Pass-through rounding: fraction "< 0.005 de Lempira" → round DOWN to the next cent; "≥ 0.005" → round UP; charging outside the rule = *hurto* (theft) + CT Art. 160 sanction + penal liability; taxpayers registered at AT on notifying start of operations or first declaration; RTN issued free (fn.11: D. 284-2013 regulates the RTN with the start-of-operations notice) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Arts. 9-10 p.12 (EVID-021) |
| LB-011 | Ley ISV, Arts. 11, 11-A | Monthly DJ of sales + entero "dentro de los primeros diez (10) días calendario del mes siguiente"; declaration due even at zero / crédito-fiscal-favor balance / temporary closure. Simplified regime: single-establishment natural/juridical persons with taxable sales ≤ L250,000/year — no DJ, annual ventas declaration by 31-ene only; non-concurrence of requirements → ordinary rules; opt-in requires proving conditions in the 2 prior fiscal years; AT may *reclasificar de oficio* (reclassify ex officio); mid-year start annualization = first-2-months sales ÷ 60 × 360; the L250,000 base excludes exempt sales and factory-level-taxed goods | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Arts. 11/11-A pp.12-14 (EVID-022) |
| LB-012 | Ley ISV, Art. 12 | Liquidation = débito − crédito. Débito = rate × sales value, minus taxes returned for "ventas anuladas o rescindidas" (annulled/rescinded sales) and rebates/discounts of the period. Crédito = ISV paid on imports + domestic purchases, minus taxes refunded for cancelled purchases/price reductions. Credit rights: inputs "vinculados directamente con la producción"; fixed-asset goods used to produce taxable consumption goods (also intangibles); repair/maintenance services on fixed assets (not increasing value); services "indispensables para la producción, elaboración o venta"; credit requires ISV actually PAID at purchase/import; EXCLUDED: special export regimes' enterprises; no credit for self-use/gifts or undocumented/non-compliant purchases; ISV credit never also an ISR cost/gasto "salvo cuando el impuesto sobre ventas pagado esté relacionado con operaciones exentas de este impuesto"; bad debts do NOT release the débito; monthly declarants control credit in the causation period "o en uno de los tres períodos mensuales inmediatos siguientes" (4-month window); mixed taxpayers: linked credit 100%, unidentifiable → pro-rata "en el porcentaje correspondiente a las ventas gravadas del período", exempt-linked credit = costo/gasto; favorable balance carries month to month; no cash refund except express cases (CT Arts. 129/131 or credit notes); credit non-transferable EXCEPT fusión/absorción continuing the giro; cessation forfeits remaining credit; exporters' purchases via "Orden de Compra Exenta" (AT-granted) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 12 pp.14-17 (EVID-023) |
| LB-013 | Ley ISV, Arts. 13-14 | DJ on AT-provided forms; cessation for any cause → DJ "dentro de los treinta (30) días siguientes de haber ocurrido el hecho" (within 30 days of the event); heirs same on death; lack of forms no excuse | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Arts. 13-14 pp.17-18 (EVID-024) |
| LB-014 | Ley ISV, Art. 15 + Anexo I | Exempt: a) canasta básica = Anexo I of Acuerdo Ejecutivo 005-2014 (273-item SAC-coded product list with exceptions and D. 290-2013 interpretations; coffee added through the whole production chain by Acuerdo 352-2022 ratified by D. 59-2022); b) human pharma + surgical material + syringes; c) energy-generation machinery, fuels (gasolina/diesel/bunker/kerosene/LPG/Av-jet/crude), books/press, school supplies, art, handicrafts, music scores, bovine leathers for small industry; d) services: electricity (residential >750 kWh/month NOT exempt), water/sewer, construcción, municipal services, honorarios profesionales by natural persons, teaching, hospitalization/ambulance, clinical labs, medical/radiological/surgical (NOT aesthetic), land passenger transport, petroleum-product transport, banking/financial services (except movable leasing with purchase option), person-insurance premiums and reinsurance; "Quedan sujetos a este impuesto, la venta o servicio de alimentos preparados para consumo dentro o fuera del local" (prepared food TAXABLE); e) agro inputs, vet pharma, fertilizers, living animals, seeds, feed raw materials & finished feed (not pets); f) diplomats (reciprocity), constitutionally-exonerated institutions, program-related purchases, fusión/absorción/dissolution transfers, real-estate sale and lease-with-option exempt, commercial-local rent ≤ L5,000/month exempt, residential rent exempt except hotels/moteles; g) sports-event admission; h) church concerts/conferences/crusades (certification: Obispo/Vicario, CEH, or Gobernador Político) | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Art. 15 pp.18-20 + Anexo I pp.23-38 (EVID-025) |
| LB-015 | Ley ISV, Arts. 17, 19 | Service rendered in-country when it takes place "total o parcialmente, dentro de las fronteras de Honduras" (totally or partially in-country) regardless of parties' nationality/domicile; responsables keep daily buy-sell accounting records and invoices/documents ≥ 5 years; simplified-regime persons: no accounting, but daily buy-sell annotations + same 5-year retention | `hn/sources/02_Ley_ISV_DL24_consolidada_DL59-2022.pdf` | Arts. 17/19 pp.20-21 (EVID-026) |
| LB-016 | Ley de Eficiencia (D. 113-2011), E-Art 3 | Natural persons acquiring taxed goods/services with credit or debit cards have the right to "la devolución de ocho por ciento (8%) del importe del impuesto efectivamente pagado" (refund of 8% of the tax effectively paid), in the form/conditions of the DEI reglamento; OTCDs process the devolution and report; footnote: D. 278-2013 Art. 20 suspended its application for six (6) months from ~30-dic-2013 — regime operationally ALIVE 2024 per R-H22 (SAR-240-2024 IX per-merchant field; 215 declaration nets it) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 3 p.2 (EVID-057; R-H22) |
| LB-017 | Ley de Eficiencia, E-Art 4 (origin instrument of the OTCD complement) | Reformed by D. 278-2013 Art. 21, D. 170-2016 Art. 195, D. 7-2017 Art. 1: OTCD solidarity "únicamente por la retención... cuando haya sido reportado por los negocios afiliados"; per-transaction ISV discrimination forced "incluso cuando el mismo sea igual a cero (0)"; affiliate zero-registration duty "bajo advertencia de que... el OTCD lo haga de manera automática"; no discrimination → OTCD applies 15% on the total amount; fully-exempt affiliates need an AT exclusion resolution communicated to the OTCDs; monthly banking entero within the first 10 días calendario; administrative/civil/penal liability | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 4 pp.2-4 (EVID-058) |
| LB-018 | Ley de Eficiencia, E-Art 5 — **VOID (dead text)** | "El crédito fiscal generado en las compras gravadas... no será sujeto a devolución ni compensación... debiendo consumirse hasta su total agotamiento; si el contribuyente al cerrar actividades no hubiera agotado su crédito fiscal acumulado por el ISV, éste se consolidará a favor del fisco. (DECLARADO INCONSTITUCIONAL)" — struck by sentencia RI-0763-2011 (Sala de lo Constitucional CSJ, 25-mar-2021); current credit rules = Ley ISV Art. 12 (LB-012) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 5 p.3 (EVID-059; R-H3) |

Dead text — never implementable as current law (recorded as LB notes, not
FRs): Eficiencia E-Art 5 credit-closure rule (VOID, R-H3 — LB-018);
Eficiencia E-Art 10 budget transfers (VOID per RI-0763-2011, R-H4 —
non-ISV content, recorded for dead-text discipline); D. 17-2010 L-Arts
13-18 12%-tier scales (homogenized to 15%, R-H2 — LB-007 history only).

## 3. Functional Requirements

Hecho-generador discipline (D-H2): every FR resolves the tax point
event-first — the statutory trigger date drives the declaration period,
not the posting date. Dated parameters (rates, L250,000 / L5,000
thresholds, Anexo I vintage) resolve as-of the trigger date and are
carried as dated rows (§4).

### 3.1 Frame, venta and hecho generador (Arts. 1-2, 5-A, 17)

- **HN-TAX-FR-211:** The system shall model ISV as a non-cumulative
  multi-stage tax levied at import and at each sale stage, where *venta*
  (sale) is any onerous transfer of dominion regardless of contract name or
  payment form, and where taxable services are ventas of service. (LB-001;
  EV02:EVID-016)
- **HN-TAX-FR-212:** The system shall treat *autoconsumo / retiro*
  (self-supply — the importer's consumption/use of goods introduced to the
  country, the industrial/producer's consumption of goods it manufactures
  or produces, and the incorporation of goods into fixed assets) as a
  taxable venta unless expressly exempt, with taxable event at the
  retirement date and base = commercial value. (LB-001; LB-002; LB-005;
  EV02:EVID-016/017)
- **HN-TAX-FR-213:** The system shall stamp the hecho generador of goods
  at the emission date of the *factura o documento equivalente* (invoice
  or equivalent document) and, absent such document, at delivery —
  invoice-first even under *reserva de dominio* (title reservation) or
  *retroventa* (resale-back) clauses. (LB-005; EV02:EVID-017)
- **HN-TAX-FR-214:** The system shall stamp the hecho generador of services
  at the EARLIEST of invoice date, service-rendered date, or
  payment/*abono* (advance) date — advances trigger ISV at receipt.
  (LB-005; EV02:EVID-017)
- **HN-TAX-FR-215:** The system shall stamp the hecho generador of imports
  at the *nacionalización* / póliza payment (customs clearance). (LB-005;
  EV02:EVID-017)
- **HN-TAX-FR-216:** The system shall tax used goods ONLY at import (the
  tax becoming part of cost) and shall NOT tax the internal resale of
  used goods. (LB-005; EV02:EVID-017)
- **HN-TAX-FR-217:** The system shall classify a service as rendered
  in-country — therefore ISV-taxable — when it takes place totally OR
  partially within Honduras' borders, regardless of the parties'
  nationality or domicile (partial-presence territoriality; no
  destination-based zero-rating exists for services). (LB-015;
  EV02:EVID-026)

### 3.2 Base imponible (Arts. 3-5)

- **HN-TAX-FR-218:** The system shall compute the base of goods/services
  as the sale value EXCLUDING direct ordinary or extraordinary financing
  charges (*gastos directos de financiación ordinaria o
  extraordinaria*). (LB-002; EV02:EVID-016)
- **HN-TAX-FR-219:** The system shall compute the import base as CIF
  value + *derechos arancelarios* (customs duties) + *impuestos
  selectivos* + *impuestos específicos* (specific taxes) + *demás
  cargos* (other charges). (LB-002; EV02:EVID-016)
- **HN-TAX-FR-220:** The system shall exclude from the base: (a)
  effective discounts appearing in the factura or equivalent document
  (customary discounts), and (b) returnable packaging (*envases
  retornables*). (LB-002; EV02:EVID-016)
- **HN-TAX-FR-221:** The system shall floor the base at the *precio de
  mercado en plaza* (local market price) when the invoice is absent or
  booked below market, *salvo prueba en contrario* (rebuttable with
  evidence attached). (LB-003; EV02:EVID-016)
- **HN-TAX-FR-222:** The system shall override the invoiced price with
  *precios normales de plaza* (normal market prices) for sales to
  administrators, council members, *socios* (partners), *comisarios*,
  relatives or spouse of the seller. (LB-004; EV02:EVID-017)

### 3.3 Rates and rounding (Art. 6, Art. 9; D. 17-2010 history)

- **HN-TAX-FR-223:** The system shall apply the ISV rate matrix as dated
  rows (D15): **15% general**; **18%** on the import/sale of cerveza,
  aguardiente, licor compuesto, otras bebidas alcohólicas and cigarrillos;
  **0% (tasa cero)** on exports; with the D. 17-2010 12%-tier scales
  (telecom postpaid ≤US$40 / prepaid / internet ≤1.024 Mbps / TV ≤L500;
  residential electricity >750 kWh) retained ONLY as historical vintages
  (R-H2 — homogenized to 15%; history rows carry `valid_to` =
  homogenization, dated-data caveat). (LB-006; LB-007; EV02:EVID-018;
  EV04:EVID-047; R-H2)
- **HN-TAX-FR-224:** For the 18% family, the system shall compute the tax
  on the **distributor-stage sale price including the value of the
  impuesto de producción y consumo** (selectivo) for beer/sodas, on the
  wholesale-stage price for cigarettes, collected at producer level and at
  import at liquidation/payment. Exact stacking order = OQ-004
  (cross-check hint: selectivo IPC acuerdos `98_/99_/100_`). (LB-006;
  EV02:EVID-018)
- **HN-TAX-FR-225:** The system shall apply 18% to air tickets in
  business class, first class or classes beyond economy (international and
  national), and shall treat airlines as responsible withholding agents
  depositing within the first 10 días calendario of the following month.
  (LB-006; EV02:EVID-018)
- **HN-TAX-FR-226:** The system shall compute exports at *tasa cero*
  (zero rate) with the input-credit/refund right for ISV paid on inputs
  and services incorporated or used in production of the exported goods,
  gated on the *productor-exportador* condition (producer = exporter).
  (LB-006; EV02:EVID-018)
- **HN-TAX-FR-227:** The system shall round the passed-on tax at cent
  level with the 0.005 rule — below L0.005 rounds DOWN to the next cent,
  ≥ L0.005 rounds UP — and shall flag any tax charged outside the rule as
  an overcharge violation (statutory *hurto*/sanction exposure; sanction
  interface = cluster T11 by id). (LB-010; EV02:EVID-021)

### 3.4 Registration and records (Arts. 10, 19)

- **HN-TAX-FR-228:** The system shall record the taxpayer's RTN
  registration as triggered by the start-of-operations notice to the AT or
  the first declaration (RTN issued free; D. 284-2013 regulates — RTN
  mechanics owned by cluster T11/W3-E3, crossref by id). (LB-010;
  EV02:EVID-021)
- **HN-TAX-FR-229:** The system shall retain ISV buy-sell source
  documents ≥ 5 years (daily buy-sell accounting records for ordinary
  responsables; daily annotations without formal accounting for
  simplified-regime persons), enforcing the retention policy on the
  document archive. (LB-015; EV02:EVID-026)

### 3.5 Exemptions (Art. 15 + Anexo I)

- **HN-TAX-FR-230:** The system shall load the Anexo I *canasta básica*
  as a SAC-coded product exemption catalog (Acuerdo Ejecutivo 005-2014,
  273 items with exception lists and D. 290-2013 interpretations; coffee
  through the whole production chain per Acuerdo 352-2022 ratified by
  D. 59-2022) as dated rows keyed by SAC code with per-item exception
  semantics; canonical-source decision = OQ-002. (LB-014; EV02:EVID-025)

- **HN-TAX-FR-231:** The system shall apply the goods exemptions: human
  pharmaceuticals, surgical material and syringes; energy-generation
  machinery; fuels (gasolina, diesel, bunker, kerosene, LPG, Av-jet,
  crude); books/press; school supplies; art; handicrafts; music scores;
  bovine leathers for small industry. (LB-014; EV02:EVID-025)
- **HN-TAX-FR-232:** The system shall apply the service exemptions:
  residential electricity BELOW the >750 kWh/month threshold, water/sewer,
  construcción (scope open — OQ-003), municipal services, *honorarios
  profesionales* (professional fees) by natural persons, teaching,
  hospitalization/ambulance, clinical labs, medical/radiological/surgical
  services (NOT aesthetic), land passenger transport, petroleum-product
  transport, banking/financial services (EXCEPT movable leasing with
  purchase option), person-insurance premiums and reinsurance. (LB-014;
  EV02:EVID-025)

- **HN-TAX-FR-233:** The system shall TAX the sale or service of prepared
  foods for consumption inside or outside the premises (prepared food is
  not canasta). (LB-014; EV02:EVID-025)
- **HN-TAX-FR-234:** The system shall apply the real-estate carve-outs as
  dated thresholds (D15): sale of real estate and lease-with-option-to-buy
  exempt; commercial-local rent exempt only up to L5,000/month (dated
  parameter, snapshot-on-write); residential rent exempt EXCEPT
  hotels/moteles. (LB-014; EV02:EVID-025)
- **HN-TAX-FR-235:** The system shall apply the remaining exemption
  schedules: agro inputs, veterinary pharma, fertilizers, living animals,
  seeds, feed raw materials and finished feed (not pets); diplomats
  (reciprocity), constitutionally-exonerated institutions,
  program-related purchases, fusión/absorción/dissolution transfers;
  sports-event admission; church concerts/conferences/crusades gated on
  the certification workflow (Obispo/Vicario, CEH, or Gobernador
  Político). (LB-014; EV02:EVID-025)

### 3.6 Liquidation: débito fiscal − crédito fiscal (Art. 12)

- **HN-TAX-FR-236:** The system shall liquidate each monthly period as
  *débito fiscal* − *crédito fiscal* (output tax − input credit), where
  débito = rate × sales value of the period's taxable ventas, reduced by
  the tax returned for *ventas anuladas o rescindidas* (annulled/rescinded
  sales) and for rebates/discounts of the period. (LB-012; EV02:EVID-023)
- **HN-TAX-FR-237:** The system shall compose crédito fiscal from ISV
  actually PAID at purchase or import on goods/services, reduced by taxes
  refunded for cancelled purchases or price reductions; unpaid or
  undocumented/non-compliant purchases generate no credit. (LB-012;
  EV02:EVID-023)
- **HN-TAX-FR-238:** The system shall grant crédito fiscal only for:
  inputs directly linked to production (*vinculados directamente con la
  producción*); fixed-asset goods used to produce taxable consumption
  goods, including intangibles; repair/maintenance services on fixed
  assets not increasing their value; and services indispensable for
  production, elaboration or sale of the activity. (LB-012; EV02:EVID-023)
- **HN-TAX-FR-239:** The system shall DENY crédito fiscal for: inputs of
  self-use/gift withdrawals; undocumented or non-compliant purchases; and
  — as an express statutory exclusion — the purchases of enterprises under
  special export regimes (their recovery runs through the OCE / special
  regime channel, FR-246; regime detail = cluster T12 by id). (LB-012;
  EV02:EVID-023)

- **HN-TAX-FR-240:** The system shall enforce the ISR-cost bar: ISV
  computed as crédito fiscal shall never ALSO be admitted as an ISR
  cost/gasto (deduction), EXCEPT ISV paid on ISV-exempt-operation-related
  purchases, which — denied as credit — becomes a deductible cost
  (interface to the ISR deduction engine, cluster T2 by id). (LB-012;
  EV02:EVID-023)
- **HN-TAX-FR-241:** The system shall NOT release débito fiscal when a
  sale becomes a bad debt (the ISR-side bad-debt deduction is a T2
  matter). (LB-012; EV02:EVID-023)
- **HN-TAX-FR-242:** The system shall enforce the 4-month credit window
  for monthly declarants: a purchase's credit is controllable in its
  causation period OR in one of the three immediately following monthly
  periods; credits not applied within the window lapse for application
  ("no utilizadas en plazo" surface = cluster W2-F5 by id). (LB-012;
  EV02:EVID-023)
- **HN-TAX-FR-243:** For mixed taxpayers, the system shall split credit:
  (a) credit linked to taxable operations → 100% credit; (b) credit
  linked to exempt operations → costo/gasto (FR-240 exception); (c)
  unidentifiable credit → pro-rata "en el porcentaje correspondiente a
  las ventas gravadas del período" (percentage of the period's taxable
  sales), applied at period close (refinement = OQ-006). (LB-012;
  EV02:EVID-023)
- **HN-TAX-FR-244:** The system shall carry a favorable monthly balance
  (crédito > débito) forward month to month, granting NO cash refund
  except the express statutory cases — CT Arts. 129/131 procedures or
  *notas de crédito* (credit notes) — per the refund gate owned by
  cluster T11; per R-H3 the Eficiencia E-Art 5 no-refund/
  closure-to-fisco rule is VOID dead text, never encoded. (LB-012;
  LB-018; EV02:EVID-023; EV05:EVID-059; R-H3)
- **HN-TAX-FR-245:** The system shall block transfer of crédito fiscal to
  third parties, with the SINGLE exception of *fusión/absorción* (merger/
  absorption) where the surviving entity continues the same giro (credit
  succession); cessation forfeits the remaining credit (no refund, subject
  to the FR-244 gate). (LB-012; EV02:EVID-023)
- **HN-TAX-FR-246:** The system shall support the exporters' *Orden de
  Compra Exenta* (OCE) mechanism: AT-granted tax-free purchase orders for
  exporter inputs, so qualifying purchases carry no ISV at source
  (complementary to FR-226; export documentation flows = cluster W3-E5 by
  id). (LB-012; EV02:EVID-023)

### 3.7 Collection, OTCD cards, declarations and special regimes (Arts. 7-8, 11, 11-A, 13; Eficiencia E-Arts 3-4)

- **HN-TAX-FR-247:** The system shall require every responsable (except
  Régimen Simplificado) to issue factura/equivalent for sales and services
  and to record the tax in a special account *a la orden del Fisco* (at
  the order of the Treasury), and shall present final-consumer prices with
  the tax INCLUDED in the final price as the consumer-display mode;
  document content — including the zero-discrimination duty even at ISV 0 —
  is owned by W3 clusters E4/E5, and AT machine/document disablement is
  carried there as an emission-suspension flag. (LB-008; EV02:EVID-019)
- **HN-TAX-FR-248:** For card transactions of affiliated merchants, the
  system shall compute the OTCD (*operadoras/administradoras de tarjetas
  de crédito/débito* — card issuers/operators/concessionaires) retention
  as 10% of the total ISV discriminated in the affiliate's taxable
  transaction, reimburse the remainder, and issue the retention
  comprobante preserving the affiliate's crédito fiscal rights
  (declaration surfaces 215/523 = cluster W2-F4 by id). (LB-009;
  EV02:EVID-020)
- **HN-TAX-FR-249:** The system shall enforce the no-discrimination
  fallback: when an affiliate card transaction carries no discriminated
  ISV, the OTCD applies 15% automatically on the total amount; affiliates
  must register the ISV caused even at zero or on final-consumer sales
  (else the OTCD does it automatically); fully-exempt affiliates are
  excluded only via an AT exclusion resolution communicated to the OTCDs.
  (LB-009; LB-017; EV02:EVID-020; EV05:EVID-058)
- **HN-TAX-FR-250:** The system shall compute the OTCD monthly entero of
  all retained amounts within the first 10 días calendario of the
  following month through the banking system, OTCD solidarity limited to
  retentions on operations reported by the affiliates. (LB-009; LB-017;
  EV02:EVID-020; EV05:EVID-058)
- **HN-TAX-FR-251:** The system shall support AT-designated collection
  agents as configuration: (a) *percepción* agents among
  productores/wholesalers, collecting ISV on the consumer-final-price
  base (designated goods not re-taxed downstream); (b) habitual buyers
  of goods/services appointed as retention agents, total or partial.
  (LB-009; EV02:EVID-020)
- **HN-TAX-FR-252:** The system shall generate the monthly ISV
  *declaración jurada* of sales and the entero within the first 10 días
  calendario of the following month, EVEN when the period's balance is
  zero, a crédito-fiscal-favor balance, or the taxpayer is temporarily
  closed (determination surface 201 = cluster W2-F5 by id). (LB-011;
  EV02:EVID-022)
- **HN-TAX-FR-253:** The system shall generate a final DJ within 30 days
  of cessation for any cause (including death, where heirs carry the
  duty), on AT-provided forms (form availability never excuses filing).
  (LB-013; EV02:EVID-024)
- **HN-TAX-FR-254:** The system shall model the *Régimen Simplificado*
  gates: natural or juridical persons, single establishment, taxable
  sales ≤ L250,000/year (dated parameter, D15; base EXCLUDES exempt sales
  and factory-level-taxed goods); simplified subjects are not collection
  agents, file NO monthly DJ, and file only the annual ventas declaration
  by 31-ene — INFORMATIVE per R-H23 (no payment surface; NO reduced rate
  exists anywhere in the prints); opt-in requires proving the conditions
  in the 2 prior fiscal years; the AT may reclassify ex officio; mid-year
  starts annualize at first-2-months sales ÷ 60 × 360 (surface 202 =
  cluster W2-F5 by id). (LB-011; EV02:EVID-022; R-H23)
- **HN-TAX-FR-255:** The system shall support the 8% card-purchase
  *devolución* (refund to natural persons of 8% of the ISV effectively
  paid on credit/debit-card acquisitions), processed and reported by the
  OTCDs per the DEI reglamento: operationally ALIVE per R-H22 (SAR-240-IX
  per-merchant devolución field; the 215 base nets it); the D. 278-2013
  Art. 20 six-month suspension (~30-dic-2013) recorded as suspension
  history; when-it-applies open (OQ-005; W2-F4 kin 41_ OQ-3). (LB-016;
  EV05:EVID-057; R-H22)

## 4. Data Model

Machine-readable sidecars (rate vintages JSON/CSV, Anexo I SAC catalog)
live next to this markdown file when produced. Layer semantics: Odoo-side
computation/bookkeeping data only (see §5). Dated legal parameters carry
`valid_from/valid_to` rows (D15) and resolve as-of the hecho-generador
date (D-H2).

**ISV rate matrix — dated rows (current + history):**

| Rate | Scope | valid_from | valid_to | Notes |
|------|-------|-----------|----------|-------|
| 15% | General (all ventas not otherwise listed) | 1964-01-01 (as consolidated) | open | Current general rate (02_ Art. 6) |
| 18% | Cerveza, aguardiente, licor compuesto, otras bebidas alcohólicas, cigarrillos — distributor-stage base incl. selectivo (beer/sodas); wholesale-stage (cigarettes) | 2010-era (as consolidated) | open | Stacking order OQ-004; collection at producer/import |
| 18% | Air tickets business/first/beyond-economy (intl+national) | as consolidated | open | Airlines = withholding agents, 10 días |
| 0% | Exports (producer-exporter condition; credit right FR-226) | as consolidated | open | Tasa cero ≠ exempt: credit survives |
| 12% (history) | Telecom postpaid ≤US$40; prepaid; internet ≤1.024 Mbps; TV ≤L500; residential electricity >750 kWh | 2010 (D. 17-2010) | homogenization (R-H2; chain unpinned) | NEVER apply to current periods |

**Core computation entities:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (sale/service) | isv_hecho_generador_date, isv_trigger_type | date · select | trigger: goods_invoice · goods_delivery · services_earliest · self_use_retirement · import_nacionalizacion | FR-212..216 |
| account.move.line | isv_base_component + exclusion flags | select null + booleans | goods_services_value_ex_finance · import_cif_duties_selectivo · commercial_value_self_use; finance-charge exclusion, effective discounts (printed on the factura), returnable packaging | FR-212, FR-218..220 |
| account.move.line | isv_price_floor_applied | boolean + monetary override | plaza-market floor (absent/below-market invoice; related-party) | FR-221/222 |
| account.tax (ISV) | rate rows via l10n_hn.isv.rate.parameter | monetary/percent | general_15 · selectivo_attached_18 · air_premium_18 · export_0 (+ 12% history rows) | FR-223..226 |
| l10n_hn.isv.exemption (new) | schedule, sac_code, item, exceptions, instrument, valid_from/valid_to | char/select | schedules: anexo_i_005_2014 (+352-2022 café) · goods_b_c · services_d · rents_f · other_e_g_h; carries the dated L5,000 commercial-rent threshold | FR-230..235 |
| res.company | isv_regime | select | general · simplificado (+ gates snapshot: establishments, gravadas base, 2-year proof) | FR-254 |

**Liquidation engine (débito/crédito):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (vendor tax) | isv_credit_eligible, isv_credit_paid | boolean | eligibility catalog FR-238; PAID requirement | FR-237/238 |
| account.move.line (vendor tax) | isv_credit_causation_period, isv_credit_window_expires | date (computed) | causation month + 3 monthly periods | FR-242 |
| account.move.line (vendor tax) | isv_credit_linkage | select | taxable_linked · exempt_linked · unidentifiable (→ pro-rata) | FR-243 |
| l10n_hn.isv.period.close (new) | gravadas_sales, exentas_sales, prorata_percent, credit_applied, credit_expired | monetary/percent | pro-rata = gravadas ÷ total sales of the period | FR-243 |
| account.move.line | isv_isr_cost_bar | boolean (computed) | true = blocked as ISR deduction (credit taken); exempt-linked ISV = deductible | FR-240 |
| l10n_hn.isv.credit.balance (new) | period, favorable_balance, carryforward | monetary | month-to-month carryforward; refund only via CT 129/131 gate | FR-244 |
| l10n_hn.isv.credit.transfer (new) | type, successor_ref | select | blocked (default) · merger_absorption_continuing_giro · cessation_forfeiture | FR-245 |
| purchase.order / account.move | isv_oce_reference | char | Orden de Compra Exenta (AT-granted) — tax-free source | FR-246 |

**OTCD / declarations / devolución:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isv.otcd.retention (new) | affiliate_txn, isv_discriminated, retained_10pct, reimbursed, comprobante_ref, fallback_15_applied, affiliate_exclusion_resolution | monetary/char/boolean | 10%-of-tax retention, credit preserved via comprobante; no-discrimination → 15% on total; all-exempt AT resolution | FR-248/249 |
| l10n_hn.isv.agent.designation (new) | agent_type, scope, base_rule | select | percepción_wholesaler (consumer-final-price base, no downstream re-tax) · habitual_buyer_retention (total/partial) | FR-251 |
| l10n_hn.isv.dj.monthly (new) | period, debito, credito, net, status, cessation fields | monetary/select/date | generated even at zero / credit-favor / temporary closure; cessation_event + event + 30 días (heirs on death) drives the final-DJ task | FR-252/253 |
| res.company (simplified) | isv_simplified_annualization | monetary (computed) | first-2-months ÷ 60 × 360; annual 31-ene informative | FR-254 |
| l10n_hn.isv.devolucion8 (new) | status, instrument_rows | select/dated rows | alive (R-H22); suspension history D. 278-2013 Art. 20; 8% of tax effectively paid, OTCD-processed | FR-255 |

## 5. Odoo Mapping

Layer semantics: `odoo` = computation/bookkeeping logic in the LGPL
client. No `saas` rows: the only architecture-split surface for HN is the
facturación/SEE emission channel (W3, S-HN2) — document content duties
(zero-discrimination) live with W3-E4/E5. Model names are stable across
Odoo 17/18/19/20; legal vintages are recorded per row.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-211 | odoo | account.tax (group ISV) | — | Multi-stage non-cumulative = standard VAT-family tax application on sale/import moves; no special engine |
| FR-212 | odoo | stock.move / account.move | isv_self_supply | Self-supply: consumption/production-withdrawal moves generate a self-invoice tax line; fixed-asset incorporation at retirement date (17-20: hook on stock valuation moves) |
| FR-213 | odoo | account.move | invoice_date (default) | Odoo's invoice_date default satisfies invoice-first; delivery fallback = custom stamper when no factura exists at delivery (D-H2 event-first override of posting date) |
| FR-214 | odoo | account.move + account.payment | isv_hecho_generador_date | Services earliest-of(invoice_date, service/performance date, payment date); advances: down payments (account.payment) create tax-point lines — proposal: tax-point stamper service, all versions |
| FR-215 | odoo | account.move (import bill) | customs clearance date | Import tax point at nacionalización (landed-cost moment), not vendor bill date |
| FR-216 | odoo | product.template / account.tax fp | isv_used_goods | Used goods: taxed on import only; internal resale maps to 0/exempt-not-zero fiscal position with no credit side (kin W2-F5 bienes usados; 69_ OQ-2 design) |
| FR-217 | odoo | account.move.line | isv_service_territorial | Partial-presence rule: foreign-customer services remain taxable; do NOT create a destination-based export fiscal position for services (contrast goods FR-226) |
| FR-218..220 | odoo | account.move.line | base composition | Financing charges excluded from base (line nature flag); import base via landed-cost allocation (CIF/duties/selectivo/específicos/cargos, stacking OQ-004); customary discounts must print on the factura (W3-E4 print layer crossref); returnable-packaging product flag |
| FR-221/222 | odoo | account.move | isv_price_floor | Plaza-market floor (absent/below-market invoice) + related-party partner-relation flags forcing plaza-price base; evidence-attachment rebuttal |
| FR-223 | odoo | account.tax + l10n_hn.isv.rate.parameter | dated rows | 15/18/0 current + 12% history vintages with valid_to (R-H2); account.tax has no native validity window — version note: manage dated application via the parameter table + fiscal-position date gating in 17-20 |
| FR-224 | odoo | account.tax (18% family) | base composition flag | Distributor-stage base incl. selectivo; collection-at-producer: product-level tax template on producer/import moves (stacking = OQ-004) |
| FR-225 | odoo | account.tax (air premium) + withholding | airline agent flag | Premium-class product variants at 18%; airline entero rides the 10-días retention calendar (cluster T6 calendar anchor) |
| FR-226 | odoo | fiscal position (export) + credit | export_0 + credit right | Tasa cero position preserving input credit; producer-exporter condition gate; OCE alternative FR-246 |
| FR-227 | odoo | account.tax computation | rounding 0.005 | Odoo round-half-up at 0.01 matches ≥0.005-up; verify tax precision setting per company (rounding=0.01); overcharge guard = validation constraint |
| FR-228/229 | odoo | res.partner/res.company · account.move | vat (RTN 14-char) · retention policy | RTN format validation here, mechanics with T11/W3-E3; 5-year document-retention flag aligns with CT prescription (T11) |
| FR-230 | odoo | l10n_hn.isv.exemption | SAC-coded catalog | Anexo I load as dated catalog rows + product-SAC mapping (product.default_code / hs_code); canonical source OQ-002 |
| FR-231..235 | odoo | fiscal position mappings | exemption schedules | Service/goods/rent/other exemptions as fiscal-position templates keyed to §4 catalog; L5,000 rent threshold snapshot-on-write (D15); prepared-food taxable guard on product category |
| FR-236/237 | odoo | account.tax aggregation + vendor tax lines | débito · isv_credit_paid | Output-tax ledger per period with anulada/rescisión and rebate/discount reversals; credit recognized on payment-completed purchases (payment-state gate on vendor tax lines, all versions) |
| FR-238 | odoo | account.move.line tags | eligibility catalog | Input/fixed-asset/R&M/indispensable-service tags; intangibles included |
| FR-239 | odoo | account.move.line | exclusion flags | Self-use/undocumented/special-export-regime supplier gate (T12 regime registry crossref) |
| FR-240/241 | odoo | account.move.line · account.move | isv_isr_cost_bar · bad-debt guard | Cross-tax bar feeding the ISR deduction engine (T2): credited ISV blocked, exempt-linked ISV allowed as cost; no débito release on credit losses |
| FR-242 | odoo | l10n_hn.isv.period.close | credit window | 4-month window: causation month + 3; expiry writes off application rights ("no utilizadas en plazo" reporting = W2-F5 casilla kin) |
| FR-243 | odoo | l10n_hn.isv.period.close | pro-rata | Monthly pro-rata on gravadas-share of sales; proposal mirrors l10n_ar-style pro-rata tax computation (version-stable pattern) |
| FR-244/245 | odoo | l10n_hn.isv.credit.balance / .credit.transfer | carryforward · succession | Favorable balance carries month-to-month, refund gated to CT 129/131 cases (T11; R-H3 dead-text guard: no closure-to-fisco); transfer blocked except fusión/absorción continuing the giro (res.company succession hook); cessation forfeits |
| FR-246 | odoo | purchase.order | isv_oce_reference | OCE flag suppresses supplier ISV at source for AT-granted exporter orders |
| FR-247 | odoo | account.move (consumer) | tax-in-price display | Final-consumer price display mode: tax included (price_include=True on consumer-channel taxes); factura duty + zero-discrimination content = W3-E4/E5 |
| FR-248 | odoo | payment.transaction / account.move | OTCD retention split | Card-journal payments on affiliated sales trigger 10%-of-tax retention split; comprobante artifact preserves affiliate credit (215/523 = W2-F4) |
| FR-249/250 | odoo | same | fallback_15 · monthly entero | Missing-discrimination validation → 15%-on-total fallback; exclusion-resolution field for all-exempt affiliates; OTCD 10-días entero aggregate (banking channel), solidarity scoped to reported ops |
| FR-251 | odoo | l10n_hn.isv.agent.designation | config | Percepción/habitual-buyer designations as partner-level config driving retention/perception at invoice or payment |
| FR-252/253 | odoo | l10n_hn.isv.dj.monthly / .dj.final | declaration data | Monthly DJ dataset (201 surface data = W2-F5), always-generated including zero/credit-favor/closure states; cessation/death event hook → 30-day final DJ task |
| FR-254 | odoo | res.company | isv_regime | Simplificado gates monitor: establishment count, gravadas-base vs dated L250k threshold, 2-year proof snapshot, ÷60×360 annualization; annual 31-ene informative report (202 = W2-F5; R-H23 informative mirror, no reduced rate) |
| FR-255 | odoo | l10n_hn.isv.devolucion8 | status config | 8% devolución as OTCD-side regime flag with dated status rows (alive per R-H22; suspension history); consumer-side informational in Odoo |

Version-regime notes (D12/D15/D16): FR-223 records the rate-vintage regime
(15/18/0 current; 12% history rows valid_to homogenization per R-H2);
FR-234/FR-254 record dated parameters (L5,000; L250k) resolved as-of the
trigger date, snapshot-on-write; FR-213/214/215 record the D-H2
event-first tax point overriding posting-date defaults; FR-242 records the
4-month credit window, mid-year go-live imports carrying original-period
windows (D18 kin).

## 6. Acceptance Criteria

- **AC-001:** Given a taxable base of L10.03 at 15%, then tax = L1.5045 →
  charged L1.50 (< 0.005 rounds down); given L10.04, then L1.5060 →
  charged L1.51 (≥ 0.005 rounds up) (FR-227).
- **AC-002:** Given a services contract invoiced 20-mar but paid in
  advance 5-mar and performed 2-abr, then the hecho generador stamps
  5-mar and the tax falls in March's DJ (FR-214).
- **AC-003:** Given goods delivered 2-abr under reserva de dominio with
  factura emitted 10-abr, then the tax point is 10-abr; given no factura
  by delivery, then the delivery date (FR-213).
- **AC-004:** Given an import with CIF L1,000, duties L50, selectivo
  L100, específico L20 and other charges L30, then the ISV base = L1,200
  and tax at 15% = L180 (FR-219).
- **AC-005:** Given a related-party sale invoiced at L80 with plaza
  normal price L100, then the base books at L100 absent contrary
  evidence; given evidence attached, the invoiced value stands
  (FR-221/222).
- **AC-006:** Given period sales of L60 gravadas and L40 exentas with
  L100 of unidentifiable input credit, then L60 enters crédito fiscal
  and L40 becomes costo/gasto (FR-243/240).
- **AC-007:** Given a purchase credit causated in January and first
  applied in May, then the application is rejected (window = Jan +
  Feb–Apr), surfacing as not-utilized-in-term (FR-242).
- **AC-008:** Given an affiliated card sale of L200 + L30 discriminated
  ISV, then the OTCD retains L3, reimburses L227, and the comprobante
  preserves the L3 credit; given no discrimination, then 15% on the total
  (FR-248/249).
- **AC-009:** Given a distributor-stage beer sale price of L100 including
  the selectivo value, then ISV = L18 at 18% (stacking order per OQ-004)
  (FR-224).
- **AC-010:** Given a producer-exporter's export sale, then the invoice
  taxes at 0% and the input credit survives (refund via the CT 129/131
  gate); given a trading-only exporter, then no refund right (FR-226/244).
- **AC-011:** Given a single-establishment retailer with annual gravadas
  sales of exactly L250,000, then the simplified gates pass (≤); given
  L250,001 or a second establishment, then ordinary rules apply; given a
  1-jul start with first-2-month sales of L41,667, then annualized =
  41,667 ÷ 60 × 360 = L250,002 → simplified regime denied (FR-254).
- **AC-013:** Given a commercial-local rent of L5,000/month, then exempt;
  given L5,001, then taxable at 15%; given residential rent, then exempt;
  given hotel/motel lodging, then taxable (FR-234).
- **AC-014:** Given a restaurant meal prepared on premises from exempt
  canasta inputs, then the sale is TAXABLE (FR-233).
- **AC-015:** Given L30 ISV credited on a taxable input purchase, then
  the L30 is blocked as an ISR deduction; given L30 ISV on an
  exempt-linked purchase, then denied as credit but deductible as cost
  (FR-240).
- **AC-016:** Given a used-vehicle import taxed at entry and its later
  internal resale, then the import bears ISV (into cost) and the resale
  bears none (FR-216).
- **AC-017:** Given a fusión where the surviving entity continues the
  same giro with a L50,000 credit balance, then the balance transfers;
  given outright cessation, then forfeited with no refund (FR-244/245).
- **AC-018:** Given a natural person's card purchase bearing L30 of ISV,
  then the devolución right = 8% × L30 = L2.40, OTCD-processed and netted
  in the 215 base (status per R-H22; scope open OQ-005) (FR-255).
- **AC-019:** Given a telecom service invoice in a current period, then
  it taxes at the general 15% (the 12% tiers are history rows never
  applied) (FR-223; R-H2).
- **AC-020:** Given a temporary closure month with zero sales and a
  credit-favor balance, then the monthly DJ is still generated as due
  (FR-252).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `02_ OQ-1` (carried, C1) OTCD 10% card retention vs the affiliate's own débito: does the retained 10% enter the affiliate's 201 as a credit line, a separate casilla, or reduce débito? Resolution surface = the 215/523/201 declaration families (clusters W2-F4/F5, S-HN3 wave — crossref by id; EV02:file OQ-1). | no | Takumi S-HN3 (W2-F4/F5) | open |
| OQ-002 | `02_ OQ-2` (carried, C1) Anexo I canonical source: the consolidated 02_ embeds Anexo I (with the consolidation's own 352-2022 café update note); the standalone Acuerdo 005-2014 + reforms (017-2017, 352-2022) also circulate. Recommendation recorded (not decided): use the 02_ consolidated Anexo I as the working base for §4 catalog rows (it is the current-authority print) while queueing acquisition of the standalone 005-2014 original for verbatim/machine-extraction fidelity; final call = controller DECIDE (EV02:file OQ-2). | no | controller (DECIDE) | open |
| OQ-003 | `02_ OQ-3` (carried, C1) "Servicios de construcción" exemption scope — housing only vs all construction; materiality for a construction-sector fiscal-position config; needs reglamento/instructivo (LEAD acquisition) (EV02:file OQ-3). | no | acquisition queue | open |
| OQ-004 | `02_ OQ-4` (carried, C1) 18% ISV vs selectivo stacking order: beer/sodas base "incluyendo el valor del impuesto de producción y consumo" — exact composition order at the distributor-stage price to encode. Cross-check hint: selectivo IPC acuerdos `98_/99_/100_` (172-2022 → 014-2023 → 218-2024; acquired under `hn/sources/`, not yet evidence-extracted — the T10/F9 selectivo synthesis owns the values). FR-224 written with the statutory inclusion; encode the exact order only after the cross-check (EV02:file OQ-4). | no | Takumi T10/F9 synthesis | open |
| OQ-005 | `05_ OQ-1` kin (carried, C1 — primary home here) devolución 8% post-2013-suspension status + DEI reglamento: narrowed by R-H22 (operationally alive 2024; SAR-240-IX per-merchant field; 215 base nets it); when-it-applies = 41_ OQ-3 (C2, W2-F4). FR-255 written on the alive reading with dated status rows (EV05:file OQ-1; R-H22). | no | acquisition queue (DEI reglamento) | open |
| OQ-006 | Pro-rata formula refinement (from EV02:EVID-023 doubts): Art. 12 expresses the mixed-activity split as a percentage "correspondiente a las ventas gravadas del período" (sales-value based); reglamento/practice may refine (Generalidades `70_` crédito-ISV manual flagged for the fiscal-reporting wave) — verify the denominator (gravadas vs total, value vs count) before freezing FR-243's computation. | no | Takumi S-HN3 (W2, 70_ check) | open |
