# SV — Taxation — IVA base imponible, tasa and débito: the Arts. 47-55 computation core + the FOVIAL/COTRANS never-in-base guard and the SOQ-40 DTE-chain design pass (Ley IVA Arts. 47-55; Rgto. Arts. 17-18; 31_ Guía DG-002/2001)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the computation core of El
Salvador's *Impuesto a la Transferencia de Bienes Muebles y a la Prestación de
Servicios* (transfer-of-movable-goods-and-services tax, "IVA", D.L.
296-1992): the *base imponible* (tax base) and *tasa* (rate) machinery that
turns a classified operation into a *débito fiscal* (fiscal debit). It owns:
the Art. 47 generic base — the *precio o remuneración pactada* (pacted price
or remuneration) for transfers and services, the *valor aduanero* (customs
value) for imports/internations, cash or credit indifferently — with its
documented-amounts floor (the base can never fall below the amounts appearing
in the law-mandated documents, subject only to the Arts. 51/52/53 additions
and deductions) and its no-impediment rule for omitted or deferred payment;
the FULL Art. 48 a)-m) specific-base catalog — transfers at the price fixed
in the operation with *remates* (auctions) adding the *derechos del
subastador* (auctioneer's rights) to the adjudication price; leasing with
sale promise or purchase option taxing the periodic *renta* and, on the
sale/purchase becoming effective, the *valor residual* — per Reglamento Art.
17 the value of the last *cuota* (installment) or an additional one as
pacted, the tax caused per EACH periodic renta AND per the residual value;
retiros at the contribuyente's assigned public-sale price per records, else
the *precio corriente de mercado* (current market price); establishment and
universalities transfers at the value of the corporal movable goods
comprised; permutas where EACH party is a seller on its OWN side's value
(two débitos, one per side — the same rule for *mutuos de cosas*);
sales-paid-with-services at the value of the alienated goods; imports and
internations = *valor CIF o valor aduanero* + *derechos arancelarios*
(tariff duties) + *impuestos específicos al consumo* (specific consumption
taxes) with the present tax NEVER forming part of the base; services at the
total consideration with goods delivered in payment valued at the
transferred goods' value; installation/works/specialties and general
construction contracts at the agreed price or value; the service-supplied
goods aggregation — goods transferred or supplied by the prestador inside
Art. 48-i)/j) services join the base EVEN IF their standalone transfer would
not be affected to the tax, unless the contract value already comprises
them; self-used services at the assigned value floored at market;
commercial/industrial real-estate leases at the pacted *renta*; and
commission agents, consignees, brokers and mandates at the commission or
pacted remuneration only; the Art. 49 non-base amounts (*indemnizaciones*
that by nature or purpose are no consideration; *propinas* — tips;
provisional, union or similar *cotizaciones*); the Art. 51 additions to the
price — a) price *reajustes* (readjustments), financing commissions, rights,
rates, interests and expenses INCLUDING late-payment interest, gastos of
every class, *fletes* (freight) and expense reimbursements EXCEPT sums paid
in the name and account of the buyer/acquirer/service receiver under his
mandate, WITH the express exclusions of *multas* (fines) stipulated in
conventional penal clauses and of interest paid to THIRD PARTIES other than
the seller/provider/prestador; b) the accessories list (*embalaje*, flete,
transporte, limpieza, seguro, garantías, colocación, mantenimiento — when no
independent prestación); c) *envases* (containers) and guarantee deposits;
d) special, additional, specific or selective taxes devengados by the same
operations — with the present tax excluded — the FOVIAL/COTRANS guard's Ley
root; plus the mixed gravada/exenta proration of the additions; the Art. 52
exclusions (general, unconditional commerce discounts already documented in
CCF and debit/credit notes); the Art. 53 foreign-currency bases (conversion
at the hecho-generador-day rate; payment-date FX differences NEVER in the
base; installment-sale FX differences BETWEEN celebration and saldo/cuota
payment ADDED to the base) and the Rgto. Art. 18 customs-value conversion at
the *póliza de importación*/formulario aduanero acceptance-day rate; the
Art. 54 13% rate as a DATED row with its D.L. 370-1995 history (10% → 13%,
1995); and the Art. 55 débito = rate × base per operation — the authority
the F-07 Anexo 1/2 M/O débito companion columns consume (S3 rate-anchor
closure). It also owns the Ley-side FOVIAL/COTRANS never-in-base guard —
the *contribución especial* is no base and no addition to it, and IVA is
never charged or recargado over the contribution (Ley IVA Arts. 2 + 47 +
48-a + 51-d as printed by the 31_ guide) — and the SOQ-40 DESIGN PASS: the
mapping of the 2001 control-account B2B recovery chain (RETENCIÓN-FOVIAL /
CUENTAS-POR-COBRAR-FOVIAL re-bill) onto DTE-embedded D1 tributo lines, with
the COTRANS rows config-gated on the 89_ instrument (D.L. 257-2021, owned
W18; vigencia through 31-dic-2026 per the prorroga chain — terminal limb
D.L. 387-2025 owned W21 as 106_, Art. 2; spe/08 FR-189 by id).

It does **not** cover: the operation classification and tax-point machinery
(Arts. 1-32 — `07_iva-framework.md` SV-TAX-FR-176..205, consumed BY ID: the
base engine computes on already-classified operations, snapshotted at the
07-file tax point); the exemption catalogs and reason codes (Arts. 45/46 —
`08_iva-exemptions.md` SV-TAX-FR-206..224, consumed BY ID: exemption
qualification precedes base computation — an exempt operation carries no
base at all; the 48-j aggregation pulls T2-exempt goods in regardless); the
débito/crédito determination and adjustment machinery (Arts. 56-66 — the
determination/credit file of this wave owns it; Arts. 57-58
traslación/retiro-document rules are cited here as POINTERS only, the
separate-from-price CCF discipline being Art. 57's); the exportación
regime; the IVA retention matrix (CT Arts. 161/162 zone); the FOVIAL/COTRANS
quantity-tax configuration, control accounts and F-07 fuel feeds
(`special-regimes/08_fovial-cotrans.md` SV-SPE-FR-166..175 — consumed BY
ID; this file supplies the Ley-side base-guard root and the chain→DTE
design, never re-implementing the SR8 surfaces); the DTE tributo emission
itself (`e-invoicing/01_document-types.md` SV-EINV-FR-017 — by id); and the
F-07 annex semantics (`fiscal-reporting/02_f07-annexes-sales.md` — by id,
FR-241's consumers).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). Embedded *interpretaciones auténticas* are part of 01_ AS
PRINTED (D.L. 634-1993, 820-1994, 645-2005 — all outside this file's
range). Articles 113/123/124/161 are void (Sala de lo Constitucional,
17-Dec-1992, expedientes 3-92/6-92) — none in this file's range (Arts.
47-55 all live). **SOQ-54 vintage note (rides every 01_/02_ LB in this
file):** the consolidation's last reform stamp is D.L. 71-2015 — post-2015
reforms unverified; corpus-internal signals negative (DTE stack 44_/45_,
Quincena-25 package 66_/67_, F-07 v14 manual silent); re-verify at
implementation — load-bearing for the 13% rate row (FR-240) above all.
**Reglamento = 02_ survivors only** (D.E. 83-1992 consolidated through
D.E. 60-1993/10-1996/**117-2001**; the mass repeal = D.E. 117-2001 stamp
(3) — ruling R30(a), R17-bis kin); survivor articles = 1-10, 16-26, 29-30,
50-51 (+ 52 vigencia; corrected set per R30(a) addendum, 75_ Art. 147(b)
audit 2026-08-20); this file cites Rgto. Arts. 17-18 — both survivors. The
Art. 48 preamble cross-references **CT Art. 199-A** (administrative base
estimation) as printed — a CT-side authority outside this corpus pass,
recorded as provenance, no FR asserted on it. **31_ = the FOVIAL guide**
(DGII Guía de Orientación Nº DG-002/2001, 26-nov-2001) — administrative
guidance printing the D.L. 208-2000 Art. 26 chain (as reformed D.L.
597-2001): the §IV.1 base-exclusion text is the verbatim Ley-side anchor
of the guard, and the chain ledger examples are the SOQ-40 design input;
the underlying LAW texts are now OWNED (SOQ-39 RESOLVED W18/consumed
W19: 86_ = D.L. 208-2000 consolidated through D.L. 93-2012 + 87_/88_
D.O. prints — the $0.20/galón is D.L. 597-2001's Art. 26 reform text
per 88_; 89_ = COTRANS D.L. 257-2021, passenger-tariff contribution
$0.10/galón Art. 3). **V1 citation
rule:** every LB row below cites 01_, 02_ or 31_ with the EVID id and the
txt page anchor (`=== PAGE n ===` markers of `01_Ley_IVA.pdf.txt` /
`02_Reglamento_IVA.pdf.txt`, verified this task); the SOQ-54 watch rides
all of them.

| LB | ID | Citation (Spanish) | English translation | Source file | Location |
|----|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA (D.L. 296-1992, texto consolidado), Art. 47 | "La base imponible genérica del impuesto, sea que la operación se realice al contado o al crédito, es la cantidad en que se cuantifiquen monetariamente los diferentes hechos generadores del impuesto, la cual corresponderá, por regla general, al precio o remuneración pactada en las transferencias de bienes o en las prestaciones de servicios, respectivamente, o al valor aduanero en las importaciones o internaciones. No podrá considerarse, para los efectos del impuesto, una base imponible inferior a los montos que consten en los documentos que de conformidad con lo dispuesto en esta ley, deban emitirse, con las adiciones y deducciones que se contemplan en los artículos 51, 52 y 53 de esta ley. No es impedimento para la determinación de la base imponible, la omisión o plazo de pago del precio o de la remuneración convenida entre las partes." | Generic base: the monetary quantification of the hechos generadores — generally the pacted price/remuneration for transfers/services, or the customs value for imports/internations, cash or credit; the base may NEVER be lower than the amounts appearing in the law-mandated documents (subject to the Arts. 51/52/53 additions and deductions); omission or deferral of payment is no impediment to base determination | `sv/sources/01_Ley_IVA.pdf` | Art. 47 p.23 (EVID-315; verified 01_ txt lines 770-778, PAGE 23) |
| LB-002 | Ley IVA, Art. 48 intro + a)-g) — FULL CATALOG (part 1) | Intro: "SIN PERJUICIO DE LA REGLA GENERAL ESTABLECIDA EN EL ARTÍCULO ANTERIOR Y DE LA CONTENIDA EN EL ARTÍCULO 199-A DEL CÓDIGO TRIBUTARIO, LA BASE IMPONIBLE ESPECÍFICA DE LAS OPERACIONES QUE CONSTITUYEN LOS DIFERENTES HECHOS GENERADORES DEL IMPUESTO ES LA QUE A CONTINUACIÓN SE SEÑALA: (8)" a) "En las transferencias de bienes muebles corporales es el precio fijado en la operación. En las ventas por remate, al precio de adjudicación se debe adicionar los derechos del subastador;" b) "En los arrendamientos de bienes con promesa de venta u opción de compra es la renta periódica de arrendamiento y, en caso de hacerse efectiva la venta o la compra, es el valor residual del bien;" c) "En los retiros de bienes de la empresa es el valor que el contribuyente les tenga asignado como precio de venta al público según sus documentos y registros contables, y a falta de éstos, el precio corriente de mercado;" d) "En las ventas y transferencias de establecimientos mercantiles y otras universalidades, es el valor de los bienes muebles corporales comprendidos en la transferencia;" e) "En las permutas u otras operaciones semejantes, se considera que cada parte tiene el carácter de vendedor, tomándose como base imponible de cada venta el valor de los bienes de cada parte. La misma regla se aplicará en los casos de mutuos de cosas;" f) "En las ventas que se paguen con servicios se tendrá como precio de los bienes enajenados, el valor de dichos bienes;" g) "EN LAS IMPORTACIONES E INTERNACIONES SE TOMARÁ COMO BASE IMPONIBLE, LA CANTIDAD QUE RESULTE DE SUMAR AL VALOR CIF O VALOR ADUANERO, LOS DERECHOS ARANCELARIOS Y LOS IMPUESTOS ESPECÍFICOS AL CONSUMO QUE CORRESPONDAN. EN NINGÚN CASO EL PRESENTE IMPUESTO FORMARÁ PARTE DE LA BASE IMPONIBLE. (1)" | Specific bases goods-side: transfers = the price fixed in the operation (auctions: adjudication price PLUS the auctioneer's rights); leasing with sale promise/purchase option = the periodic renta, and on the sale/purchase becoming effective, the residual value; retiros = assigned public-sale price per documents/records, else market price; establishment/universalities transfers = value of the corporal movable goods comprised; permutas = each party is a SELLER, the base of each sale being the value of each party's goods (same rule for mutuos of things); sales paid with services = the value of the alienated goods; imports/internations = CIF or customs value + tariff duties + specific consumption taxes — the present tax NEVER part of the base. The preamble cites CT Art. 199-A (estimation) as printed | `sv/sources/01_Ley_IVA.pdf` | Art. 48 intro + a)-g) p.23 (EVID-315; verified 01_ txt lines 780-804, PAGE 23) |
| LB-003 | Ley IVA, Art. 48 h)-m) — FULL CATALOG (part 2) | h) "En las prestaciones de servicios es el valor total de la contraprestación. Cuando se dieren bienes muebles corporales en pago de una prestación de servicios, se tendrá como precio de éste, el valor de los bienes transferidos;" i) "En los contratos de instalación, de ejecución de obras y de especialidades, como en los contratos generales de construcción, es el valor o precio convenido;" j) "Si en las prestaciones de servicios a que se refieren los dos literales anteriores, se incluyen transferencias o suministro de bienes muebles corporales por parte del prestador del servicio, el valor de esos bienes se agregará a la base imponible, aunque la transferencia de esos bienes independientemente considerados no estuviere afecta al impuesto; excepto el caso que en el valor de los contratos ya se comprendan el de dichos bienes;" k) "En los casos de utilización de servicios a que se refiere el Art. 16 de esta ley, la base imponible es el valor que el contribuyente les tenga asignado, según sus documentos y registros contables. En todo caso, la base imponible no podrá ser inferior al precio corriente de mercado de los respectivos servicios;" l) "En los arrendamientos, subarrendamientos o cesión del uso o goce temporal de inmuebles destinados a actividades comerciales o industriales, es el monto de la renta convenida; y" m) "En las prestaciones de servicios de comisionistas, consignatarios, corredores y mandatarios en general, la base imponible está constituida por la comisión o remuneración pactada." | Services-side bases: services = total consideration (goods delivered in payment of a service = the transferred goods' value); installation/works/specialties and general construction contracts = the agreed price or value; goods supplied by the prestador within i)-j) services are ADDED to the base even if their standalone transfer would not be affected to the tax, EXCEPT where the contract value already comprises them; self-used services (Art. 16) = assigned value per records, NEVER below the market price of the respective services; commercial/industrial real-estate leases = the pacted renta; commission agents, consignees, brokers and mandates in general = the commission or pacted remuneration | `sv/sources/01_Ley_IVA.pdf` | Art. 48 h)-m) p.24 (EVID-315; verified 01_ txt lines 812-831, PAGE 24) |
| LB-004 | Reglamento IVA (D.E. 83-1992 consolidado), Art. 17 | "Se entenderá por valor residual del bien señalado en el artículo 48 literal b) de la ley, el valor de la última cuota o de una adicional de acuerdo a lo que se hubiere pactado en el contrato de arrendamiento. Para efectos del impuesto, éste se causará por cada renta periódica y por el valor residual pactado." | The Art. 48-b residual value = the value of the LAST cuota or of an ADDITIONAL one, as pacted in the lease contract; the tax is caused per EACH periodic renta AND per the pacted residual value (two independent causation tracks) | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 17 p.6 (EVID-335; verified 02_ txt lines 208-212, Rgto. PAGE 6) |
| LB-005 | Ley IVA, Art. 49 | "No conforman la base imponible del impuesto, las cantidades pagadas a título de indemnizaciones, que por su naturaleza o finalidad no constituyen contraprestación de la transferencia de dominio o de la prestación de servicios. Tampoco integra la base imponible, el monto correspondiente a propinas, cotizaciones provisionales, sindicales o similares, que consten en los documentos señalados en el Art. 97 de esta ley." | Not part of the base: amounts paid as indemnizations that by nature or purpose are no consideration for the transfer or service; nor tips, provisional/union or similar dues appearing in the documents of the (repealed) Art. 97 — re-anchored to the CT document regime | `sv/sources/01_Ley_IVA.pdf` | Art. 49 p.24 (EVID-315; verified 01_ txt lines 833-837, PAGE 24) |
| LB-006 | Ley IVA, Art. 51 a)-d) + inciso final — FULL CATALOG | Intro: "Para determinar la base imponible del impuesto, deberán adicionarse al precio o remuneración cuando no las incluyeran, todas las cantidades o valores que integran la contraprestación y se carguen o cobren adicionalmente en la operación, aunque se documenten o contabilicen separadamente o correspondan a operaciones que consideradas independientemente no estarían sometidas al impuesto, tales como:" a) "REAJUSTES, ACTUALIZACIONES O FIJACIONES DE PRECIOS O VALORES, PACTADOS ANTES O AL CONVENIRSE O CELEBRARSE EL CONTRATO O CON POSTERIORIDAD; COMISIONES, DERECHOS, TASAS, INTERESES Y GASTOS DE FINANCIAMIENTO DE LA OPERACIÓN A PLAZO, INCLUYENDO LOS INTERESES POR EL RETARDO EN EL PAGO Y OTRAS CONTRAPRESTACIONES SEMEJANTES; GASTOS DE TODA CLASE, FLETES, REEMBOLSOS DE GASTOS, EXCEPTO SI SE TRATARE DE SUMAS PAGADAS EN NOMBRE Y POR CUENTA DEL COMPRADOR O ADQUIRIENTE O PRESTATARIO DE LOS SERVICIOS, EN VIRTUD DE MANDATO DE ÉSTE. SE EXCLUYEN DE LA BASE IMPONIBLE LAS MULTAS O SANCIONES ESTIPULADAS EN CLÁUSULAS PENALES CONVENCIONALES, COMO ASIMISMO LOS INTERESES PAGADOS A TERCEROS, DISTINTOS DEL VENDEDOR O PROVEEDOR O PRESTADOR DEL SERVICIO, POR CONCEPTO DE FINANCIAMIENTO DE LA OPERACIÓN; (1)" b) "El valor de los bienes y servicios accesorios a la operación, tales como embalaje, flete, transporte, limpieza, seguro, garantías, colocación y mantenimiento cuando no constituyan una prestación de servicios independiente;" c) "El valor de los envases, aunque se documenten separadamente o el monto de los depósitos dejados en garantía por la devolución de los envases utilizados; y" d) "El monto de los impuestos especiales, adicionales, específicos o selectivos que se devenguen por las mismas operaciones. Pero se excluye de la base imponible el presente impuesto." + inciso: "Cuando las anteriores adiciones afectan a operaciones gravadas y exentas, deberán prorratearse para ajustar la base imponible del impuesto." | Additions when not already included, even if separately documented/accounted or independently non-taxable: a) readjustments/actualizations/price fixings whenever pacted; financing commissions, rights, rates, interests and expenses of the deferred operation INCLUDING late-payment interest; gastos of every class, freights and expense reimbursements EXCEPT sums paid in the name and account of the buyer/acquirer/service receiver under his mandate — with multas of conventional penal clauses EXCLUDED and interest paid to third parties other than the seller/provider/prestador EXCLUDED; b) accessory goods/services (packing, freight, transport, cleaning, insurance, warranties, placement, maintenance — when no independent prestación); c) containers even separately documented, and guarantee deposits for container return; d) special/additional/specific/selective taxes devengados by the same operations — the PRESENT tax excluded; final: additions affecting gravada AND exenta operations are PRORATED to adjust the base | `sv/sources/01_Ley_IVA.pdf` | Art. 51 a)-d) + inciso pp.24-25 (EVID-316; verified 01_ txt lines 841-874, PAGE 24-25) |
| LB-007 | Ley IVA, Art. 52 | "Deberán excluirse de la base imponible si ya constan en los comprobantes de crédito fiscal y notas de débito o crédito, las reducciones de precios, bonificaciones, descuentos normales del comercio de carácter general y no condicionados, otorgados directamente a los adquirentes de bienes o prestatarios de servicios." | Exclude from the base — IF already appearing in the CCF and debit/credit notes — price reductions, bonuses and NORMAL commerce discounts of a general, UNCONDITIONAL character, granted directly to acquirers or service receivers | `sv/sources/01_Ley_IVA.pdf` | Art. 52 p.25 (EVID-316; verified 01_ txt lines 876-879, PAGE 25) |
| LB-008 | Ley IVA, Art. 53 | "La base imponible expresada en moneda extranjera se ha de convertir en moneda nacional, aplicándose el tipo de cambio que corresponda al día en que ocurra el hecho generador del impuesto. La diferencia de cambio que se genere entre aquella fecha y el pago total o parcial del impuesto no forma parte de la base imponible del mismo. Pero se deben adicionar a la base imponible las diferencias en el tipo de cambio en el caso de ventas a plazo en moneda extranjera, ocurridas entre la fecha de celebración de ellas y el pago del saldo de precio o de las cuotas de éste." | Foreign-currency bases convert to national currency at the rate corresponding to the DAY THE HECHO GENERADOR occurs; the FX difference generated between that date and the total or partial payment of the tax is NOT part of the base; BUT installment-sale FX differences occurring between the celebration date and the payment of the saldo or of its cuotas SHALL be added to the base | `sv/sources/01_Ley_IVA.pdf` | Art. 53 p.25 (EVID-316; verified 01_ txt lines 881-886, PAGE 25) |
| LB-009 | Reglamento IVA, Art. 18 | "Para efectos de la liquidación del impuesto, el valor aduanero de la mercancía expresado en moneda extranjera se convertirá en moneda nacional al tipo de cambio del día de aceptación de la Póliza de Importación o del Formulario Aduanero correspondiente." | For tax liquidation, the customs value of merchandise expressed in foreign currency converts to national currency at the exchange rate of the ACCEPTANCE DAY of the import póliza or the corresponding customs form (DUCA-acceptance kin, SOQ-45 kin) | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 18 p.6 (EVID-335; verified 02_ txt lines 213-216, Rgto. PAGE 6) |
| LB-010 | Ley IVA, Arts. 54-55 + reform stamp (2) | Art. 54: "LA TASA DEL IMPUESTO ES EL TRECE POR CIENTO, APLICABLE SOBRE LA BASE IMPONIBLE. (2)" — stamp (2): "D.L. Nº 370, 8 DE JUNIO DE 1995; D.O. Nº 114, T. 327, 21 DE JUNIO DE 1995. (13 %)" [the "(13 %)" note is the Asamblea reformas block's own]. Art. 55: "La aplicación de la tasa a la base imponible de los hechos generadores, determina el impuesto que se causa por cada operación realizada en el período tributario correspondiente y que para los efectos del presente impuesto, se denomina 'Débito Fiscal'." | Art. 54: the rate is THIRTEEN PER CENT applicable over the base (stamp 2 = the D.L. 370-1995 reform that raised the rate from 10% — per EVID-317 gloss — effective jun-1995); Art. 55: applying the rate to the base of the hechos generadores determines the tax caused PER EACH OPERATION realized in the corresponding tax period — the "Débito Fiscal" | `sv/sources/01_Ley_IVA.pdf` | Arts. 54-55 p.26 + reformas block p.56 (EVID-317/304; verified 01_ txt lines 897-904, PAGE 26 + lines 2022-2023, PAGE 56) |
| LB-011 | Ley IVA, Art. 2 — **POINTER** | "Este impuesto se aplicará sin perjuicio de la imposición de otros impuestos que graven los mismos actos o hechos…" | The coexistence rule owned by `07_iva-framework.md` (LB-001 / SV-TAX-FR-176, by id — never restated therefrom beyond this anchor sentence); consumed here as the coexistence ROOT of the FOVIAL/COTRANS never-in-base guard: IVA applies over fuel operations ALONGSIDE the contributions, each with its own base discipline | `sv/sources/01_Ley_IVA.pdf` | Art. 2 p.2 (EVID-305; verified 01_ txt lines 58-66, PAGE 2) |
| LB-012 | 31_ Guía DG-002/2001 (DGII, 26-nov-2001) — §IV.1 base exclusion + chain | Fundamento: "Art. 26 Ley del Fondo de Conservación Vial, D.L. N° 208 (D.O. N° 237 T.349 18-dic-2000), reformado por D.L. N° 597 (31-oct-2001, D.O. N° 212 T.353 9-nov-2001)". "EL VALOR DE LA CONTRIBUCIÓN… ES DE VEINTE CENTAVOS DE DÓLAR (US $0.20) POR GALÓN DE DIESEL, GASOLINAS O SUS MEZCLAS". §IV.1: "CONSTITUYE UNA CONTRIBUCIÓN ESPECIAL, LA CUAL DE ACUERDO A LOS ARTS. 47, 48 LITERAL a) Y 51 LITERAL d) DE LA LEY DE [IVA] NO PUEDE CONSIDERARSE COMO BASE IMPONIBLE, NI COMO UNA ADICIÓN A ÉSTA… EN NINGÚN CASO SE DEBERÁ COBRAR NI RECARGAR TAL IMPUESTO SOBRE LA REFERIDA CONTRIBUCIÓN" [the bracketed "IVA" is 31_'s own citation elision]. Documentation: "SE DETALLARÁ EN UNA FILA O CASILLA ESPECIAL SEPARADAMENTE DEL PRECIO DE VENTA… Y DEL IMPUESTO (IVA)". Registro contable: "LLEVARÁN CUENTAS DE CONTROL ESPECIALES". Chain ledger example (1,000 gal): refinería/importador sale — CLIENTES 2,460 / IVA DÉBITO 260 / RETENCIÓN FOVIAL 200 / VENTAS 2,000; each B2B intermediate books CUENTAS POR COBRAR-FOVIAL at purchase and re-bills $200 at sale until the final consumer absorbs it; final consumer/consuming contribuyente "PODRÁN CONTABILIZAR LA CONTRIBUCIÓN… COMO PARTE DEL COSTO DE LOS COMBUSTIBLES, COMO UN GASTO DE OPERACIÓN… O COMO UN GASTO DE FABRICACIÓN" | The FOVIAL contribution ($0.20/galón, D.L. 208-2000 Art. 26 as reformed D.L. 597-2001) is a contribución especial that per Ley IVA Arts. 47, 48-a) and 51-d) can be NO base and NO addition to the base — and IVA must NEVER be charged or recargado over the contribution; it prints in a special row/box SEPARATE from both the sale price and the IVA; special control accounts carry it through the B2B chain (first-tier RETENCIÓN FOVIAL credit; intermediates' CUENTAS POR COBRAR-FOVIAL re-bill) until the final consumer absorbs it, booking it as fuel cost / operating / manufacturing expense. 2001-vintage administrative guidance; the underlying laws are now OWNED (SOQ-39 resolved: 86_-88_ FOVIAL — $0.20 = D.L. 597-2001 Art. 26 reform per 88_; 89_ COTRANS — passenger-tariff $0.10/galón Art. 3) | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | Whole guide pp.1-6 (EVID-274) |
| LB-013 | Ley IVA, Art. 57 first inciso — **POINTER** | "Los contribuyentes deberán trasladar a los adquirentes de los bienes y a los prestatarios de los servicios, una cantidad equivalente al monto del débito fiscal generado en cada operación gravada. Dicha cantidad deberá constar en el Comprobante de Crédito Fiscal… en forma separada del precio o remuneración de la operación…" | The traslación and separate-from-price discipline owned by the determination/credit file of this wave (T4; EVID-317); consumed here ONLY as the separate-line root the FOVIAL fila/casilla guard (FR-243) parallels, never restated as a document rule | `sv/sources/01_Ley_IVA.pdf` | Art. 57 first inciso p.26 (EVID-317; verified 01_ txt lines 911-918, PAGE 26) |

Dead text — never implementable as current law (recorded as notes, not FRs,
per wave constraints): Art. 50 (ESTIMACION DE LA BASE IMPONIBLE) is
DEROGADO — stamp (8) — the printed omission marker sits between the Art. 49
non-base rule and the Art. 51 additions, and DGII's estimation authority now
lives in the CT Art. 199-A crossref printed in the Art. 48 preamble (CT-side,
outside this pass); Art. 56 (CALCULO EN EXCESO) is DEROGADO by D.L. 230/00 —
T4's boundary row, noted here only because it prints inside the Arts. 54-55
run; Arts. 113/123/124/161 (void) and the D.L. 230/00-repealed procedural
belt sit outside this file's range. The vetoed D.L. 24-2003 never entered
into force. Reglamento non-survivors (everything outside 1-10, 16-26, 29-30,
50-51 — corrected set, R30(a) addendum)
are per R30(a) derogated and never cited. The FOVIAL/COTRANS instruments
are NOW OWNED (SOQ-39 resolved: 86_ = the D.L. 208-2000 consolidation;
88_ = D.L. 597-2001, the $0.20/galón instrument; 89_ = D.L. 257-2021
COTRANS, passenger-tariff $0.10/galón Art. 3): the guard rows below
defend the base regardless, and statutory chain mechanics beyond 31_'s
print route to the SR8 fold-in (spe/08 FR-185..189). The SOQ-54 vintage
watch (§2 preamble) applies to every row above.

## 3. Functional Requirements

### 3.1 Generic base and the documented-amounts floor (Art. 47)

- **SV-TAX-FR-225:** The system shall compute the IVA *base imponible* of
  every gravada operation as its monetary quantification: GENERALLY the
  *precio o remuneración pactada* (pacted price or remuneration) for
  transfers of goods and prestations of services, or the *valor aduanero*
  (customs value) for imports/internations — the rule applying IDENTICALLY
  whether the operation is *al contado o al crédito* (cash or credit); and
  shall enforce the DOCUMENTED-AMOUNTS FLOOR: the computed base shall NEVER
  be lower than the amounts appearing in the documents the law mandates for
  the operation, subject only to the Art. 51 additions and the Art. 52/53
  deductions/exclusions (the floor check runs on the base AFTER those
  adjustments); and omission or deferral of the price or remuneration shall
  never block base determination (the base computes on the pacted/quantified
  value, payment state irrelevant). The base engine consumes the
  already-classified, already-tax-point-resolved operation from the
  framework file of this wave (`07_iva-framework.md` SV-TAX-FR-176..205 —
  by id) and the exemption outcome from `08_iva-exemptions.md`
  (SV-TAX-FR-206..224 — by id): an exempt operation generates NO base
  computation at all.
  (LB-001; EVID-315)

### 3.2 Specific bases — the FULL Art. 48 a)-m) catalog (Art. 48; Rgto. Art. 17)

- **SV-TAX-FR-226:** The system shall resolve the specific base of plain
  goods transfers per Art. 48-a) as the PRICE FIXED IN THE OPERATION; for
  *ventas por remate* (auction sales) it shall ADD the *derechos del
  subastador* (auctioneer's rights) to the *precio de adjudicación*
  (adjudication price — base = adjudication + auctioneer rights); for sales
  and transfers of *establecimientos mercantiles y otras universalidades*
  (mercantile establishments and other universalities) per 48-d) it shall
  take ONLY the value of the *bienes muebles corporales comprendidos en la
  transferencia* (the corporal movable goods comprised in the transfer —
  never goodwill or incorporeal elements); and for sales paid with services
  per 48-f) it shall take as the price of the alienated goods the VALUE OF
  THOSE GOODS.
  (LB-002; EVID-315)
- **SV-TAX-FR-227:** The system shall resolve the base of leases of goods
  with sale promise or purchase option per Art. 48-b) as the PERIODIC RENTA
  while the lease runs — each renta carrying its own débito at its own tax
  point (consumed from 07 by id: SV-TAX-FR-195 canone-exigibilidad) — and,
  when the sale or purchase becomes effective, as the *VALOR RESIDUAL* of
  the good; per Rgto. Art. 17 the residual value is THE VALUE OF THE LAST
  CUOTA OR OF AN ADDITIONAL ONE as pacted in the lease contract, and the
  tax is caused per EACH periodic renta AND per the pacted residual value —
  the option-exercise operation generates a SEPARATE débito over the
  residual, never folded into the last renta's base.
  (LB-002; LB-004; EVID-315/335)
- **SV-TAX-FR-228:** The system shall resolve the base of *retiros de
  bienes* per Art. 48-c) as the value the contribuyente has ASSIGNED as
  public-sale price (*precio de venta al público*) according to its
  documents and accounting records, and — ABSENT such assigned value — the
  *precio corriente de mercado* (current market price, per the Rgto. Art. 2
  num. 21 definition consumed from 07 by id); this file owns the 48-c
  computation that the framework file's retiro invoice consumes
  (`07_iva-framework.md` SV-TAX-FR-186 cites it by pointer — LB-027 there).
  (LB-002; EVID-315)
- **SV-TAX-FR-229:** The system shall resolve *permutas u otras operaciones
  semejantes* (barters and similar operations) per Art. 48-e) as TWO
  INDEPENDENT SALES: each party has the character of SELLER on its own
  side, and the base imponible of EACH sale is the value of the goods of
  EACH party — the operation books TWO débitos (one per side, each computed
  on that side's goods value at that party's rate and classification); the
  SAME rule applies to *mutuos de cosas* (loans of things — restitution in
  kind of the same genus and quality).
  (LB-002; EVID-315)
- **SV-TAX-FR-230:** The system shall resolve the base of imports and
  internations per Art. 48-g) as the sum of the *VALOR CIF O VALOR
  ADUANERO* (CIF or customs value) + the *DERECHOS ARANCELARIOS* (tariff
  duties) + the *IMPUESTOS ESPECÍFICOS AL CONSUMO* (specific consumption
  taxes) that correspond — and shall enforce the ABSOLUTE exclusion: the
  present tax (IVA itself, at any vintage rate) shall NEVER form part of
  the base imponible (no IVA-over-IVA; the Art. 15 import tax point and the
  SR4 customs-clock devengo feed — consumed from 07 by id, SV-TAX-FR-187/
  190 — trigger this base, never modify it); foreign-currency customs
  values convert per FR-239 (Rgto. Art. 18 acceptance-day rate).
  (LB-002; LB-009; EVID-315/335)
- **SV-TAX-FR-231:** The system shall resolve the base of service
  prestations per Art. 48-h) as the TOTAL VALUE OF THE CONTRAPRESTACIÓN
  (consideration) — where *bienes muebles corporales* are delivered IN
  PAYMENT of a service, the service's price is the VALUE OF THE TRANSFERRED
  GOODS; per 48-i) installation, obra-execution and specialties contracts
  and general construction contracts base at the AGREED VALUE OR PRICE; and
  per 48-j), where the 48-i) services INCLUDE transfers or supplies of
  corporal movable goods BY THE PRESTADOR, the value of those goods shall
  be ADDED to the base EVEN IF the standalone transfer of those goods would
  not be affected to the tax (an exemption classification consumed from
  `08_iva-exemptions.md` by id does NOT keep the supplied goods out), EXCEPT
  where the contract value ALREADY comprises them (no double count — an
  aggregation flag with the already-comprised exception).
  (LB-003; EVID-315)
- **SV-TAX-FR-232:** The system shall resolve: the base of self-used
  services (the Art. 16 utilization cases — autoconsumo, consumed from 07
  by id SV-TAX-FR-191) per Art. 48-k) as the value the contribuyente has
  assigned per its documents and records, with the FLOOR that the base
  shall NEVER be inferior to the *precio corriente de mercado* of the
  respective services; the base of leases, subleases or cession of
  temporary use or enjoyment of *inmuebles* destined to COMMERCIAL or
  INDUSTRIAL activities per 48-l) as the pacted *renta* (housing leases are
  the Art. 46-b exemption file's surface — 08 by id); and the base of
  *comisionistas, consignatarios, corredores y mandatarios en general*
  (commission agents, consignees, brokers and mandates in general) per
  48-m) as the COMMISSION OR PACTED REMUNERATION ONLY — never the value of
  the goods or services the intermediary intermediates.
  (LB-003; EVID-315)

### 3.3 Non-base amounts, additions and exclusions (Arts. 49, 51-52)

- **SV-TAX-FR-233:** The system shall EXCLUDE from every IVA base, per
  Art. 49: amounts paid as *indemnizaciones* (indemnities) that by their
  nature or purpose constitute NO consideration for the transfer of dominion
  or the service prestation (the Art. 16 hecho-generador exclusion's base
  echo — consumed from 07 by id); the amounts corresponding to *propinas*
  (tips); and *cotizaciones provisionales, sindicales o similares*
  (provisional, trade-union or similar dues) appearing in the operation
  documents — each carried as a tagged non-base line that the composition
  engine skips (an indemnization tagged line never enters any base).
  (LB-005; EVID-315)
- **SV-TAX-FR-234:** The system shall ADD to the price or remuneration, per
  Art. 51 intro + a), every amount or value that integrates the
  consideration and is charged or collected additionally in the operation —
  EVEN IF separately documented or accounted, or corresponding to
  operations that independently considered would not be subject to the tax —
  specifically: price *reajustes, actualizaciones o fijaciones* whenever
  pacted (before, at, or after the contract); commissions, rights, rates,
  interests and expenses of the financing of the deferred operation,
  INCLUDING the interest for late payment (*intereses por el retardo en el
  pago*); and *gastos de toda clase* (expenses of every class), *fletes*
  (freights) and *reembolsos de gastos* (expense reimbursements) — EXCEPT
  sums paid in the NAME AND ACCOUNT of the buyer, acquirer or service
  receiver under HIS MANDATE (the mandate-reimbursement gate: name-and-
  account-of + mandate authority recorded, kin to the Art. 17 final /
  SV-TAX-FR-193 no-credit condition); and it shall EXCLUDE from the base,
  per the same literal: *multas o sanciones* stipulated in conventional
  PENAL CLAUSES (*cláusulas penales convencionales*), and interest paid to
  THIRD PARTIES distinct from the seller, provider or service prestator by
  concept of financing of the operation (third-party-financing interest).
  (LB-006; EVID-316)
- **SV-TAX-FR-235:** The system shall ADD to the base, per Art. 51 b)-c):
  the value of ACCESSORY goods and services of the operation — *embalaje*
  (packing), *flete*, *transporte*, *limpieza* (cleaning), *seguro*
  (insurance), *garantías* (warranties), *colocación* (placement) and
  *mantenimiento* (maintenance) — WHEN they do not constitute an
  independent service prestation (an accessory line flagged independent
  drops out and computes its own base); and the value of *envases*
  (containers) EVEN IF separately documented, plus the amounts of
  *depósitos dejados en garantía* (deposits left as guarantee) for the
  return of the containers used.
  (LB-006; EVID-316)
- **SV-TAX-FR-236:** The system shall ADD to the base, per Art. 51-d), the
  amount of the *impuestos especiales, adicionales, específicos o
  selectivos* (special, additional, specific or selective taxes) devengados
  by the SAME operations — and shall ALWAYS exclude from the base the
  PRESENT tax (IVA never compounds itself); this literal is the Ley-side
  root the FOVIAL/COTRANS guard consumes (FR-242: the per-unit
  contributions are impuestos especiales-family charges that 31_ §IV.1
  REMOVES from the base discipline entirely — never base, never addition);
  and where the additions affect operations that are BOTH gravadas and
  exentas, the system shall PRORATE them to adjust the base imponible (the
  gravada/exenta split consumed from the T1/T2 classification-exemption
  feeds by id — SV-TAX-FR-176 taxonomy + SV-TAX-FR-206..224 exemption
  codes; a mixed operation's addition apportions between its gravada and
  exenta components).
  (LB-006; LB-012; EVID-316/274)
- **SV-TAX-FR-237:** The system shall EXCLUDE from the base, per Art. 52,
  the *reducciones de precios* (price reductions), *bonificaciones*
  (bonuses) and *descuentos normales del comercio* (normal commerce
  discounts) of a GENERAL and UNCONDITIONED character granted DIRECTLY to
  the acquirers of goods or service receivers — ONLY where they already
  appear in the *comprobantes de crédito fiscal y notas de débito o crédito*
  (CCF and debit/credit notes: the documented precondition); every element
  of the exclusion is a gate: general (not particular), unconditional (a
  conditioned discount — e.g. future-purchase-contingent — stays IN the
  base), granted directly, and already documented in the operation's fiscal
  documents.
  (LB-007; EVID-316)

### 3.4 Foreign-currency bases (Art. 53; Rgto. Art. 18)

- **SV-TAX-FR-238:** The system shall convert every IVA base expressed in
  foreign currency to national currency at the exchange rate corresponding
  to the DAY THE HECHO GENERADOR occurs (the tax-point snapshot consumed
  from 07 by id — SV-TAX-FR-180/186/189/194/195; the resolved rate
  snapshotted on the record, D15); it shall EXCLUDE from the base the FX
  difference generated between that date and the total or partial payment
  of the tax (payment-date FX differences are financial results, never
  base — the CT Art. 62 two-clock kin consumed BY ID as SV-TAX-FR-020, and
  the DTE correction surface reuses the ORIGIN rate BY ID as
  SV-EINV-FR-164: corrections never re-convert); BUT it shall ADD to the
  base the FX differences of INSTALLMENT SALES in foreign currency
  occurring between the celebration date and the payment of the saldo or
  of its cuotas — each collection computes the celebration-vs-payment
  exchange delta and adds it to the base in the collection period (the
  origin-rate discipline of the DTE layer never suppresses this statutory
  addition, which is a NEW base component at collection, not a
  re-conversion). The operational rate source/feed selection stays OPEN
  (taxation `00_index.md` OQ-006 kin).
  (LB-008; EVID-316)
- **SV-TAX-FR-239:** The system shall convert the foreign-currency customs
  value of imported/interned merchandise to national currency, per Rgto.
  Art. 18, at the exchange rate of the ACCEPTANCE DAY of the *póliza de
  importación* or the corresponding *formulario aduanero* (the DUCA-family
  acceptance date — SOQ-45 kin) — the import base of FR-230 (CIF/aduanero
  + aranceles + impuestos específicos) resolving its USD conversion at
  that acceptance-day rate, recorded on the import move as the FX anchor.
  (LB-009; EVID-335)

### 3.5 Rate and débito fiscal (Arts. 54-55)

- **SV-TAX-FR-240:** The system shall carry the IVA rate as a DATED
  parameter with full history, resolving as-of each operation's tax-point
  date (D15 snapshot): current row 13% *aplicable sobre la base imponible*
  (Art. 54 as printed, stamp 2), provenance D.L. 370 (8-jun-1995, D.O. Nº
  114 T.327 21-jun-1995 — the reform that raised the rate from 10% per
  EVID-317 gloss); history row 10% from vigencia 1-sep-1992 until the D.L.
  370 cutover (exact cutover day unpinned — OQ-4); the rate history ships
  as configuration rows with instrument provenance per row, and the SOQ-54
  watch rides the current 13% row (no post-2015 reform signal in corpus —
  re-verify at implementation).
  (LB-010; EVID-317/304)
- **SV-TAX-FR-241:** The system shall compute the *débito fiscal* per
  Art. 55 as the application of the resolved rate to the resolved base of
  the hechos generadores — the tax caused PER EACH OPERATION realized in
  the corresponding tax period (per-operation computation, never an
  aggregate-first multiplication; each operation line carries its own
  base × rate débito, summed only at determination — the T4 file's
  surface, by pointer); and this file's rate × base engine IS the
  authority the F-07 sale-annex débito columns consume
  (`fiscal-reporting/02_f07-annexes-sales.md` SV-FREP-FR-048 — Anexo 1 M
  *débito fiscal* and N's O companion computed by the IVA engine — and
  SV-FREP-FR-066 — the casilla wiring whose 142 débito is computed by the
  IVA engine on the Anexo 2 side — BY ID): the rate-anchor forward pointer
  recorded in fiscal-reporting/02 FR-048's mapping note closes HERE (its
  remaining OQ-002 items — the L net convention and the P formula — stay
  S3's); the CCF 13%-on-top convention of the DTE layer
  (SV-EINV-FR-024 kin) likewise consumes this engine's output, by id.
  (LB-010; EVID-317)

### 3.6 FOVIAL/COTRANS never-in-base guard — the Ley-side root (Ley IVA Arts. 2, 47, 48-a, 51-d via 31_ §IV.1)

- **SV-TAX-FR-242:** The system shall enforce, on the IVA base engine, the
  FOVIAL/COTRANS NEVER-IN-BASE guard rooted in Ley IVA Arts. 47 + 48-a +
  51-d as printed by 31_ §IV.1: the *contribución especial* ($0.20/galón
  FOVIAL; COTRANS kin) can NOT be considered *base imponible* NOR an
  addition to it, and IN NO CASE shall IVA be charged or recargado over
  the contribution — implemented as a composition invariant: the per-unit
  contribution amount (quantity-tax family — SR8 SV-SPE-FR-167 by id) is
  excluded from EVERY base composition of FR-225..237 (never in the price
  subtotal, never an Art. 51 addition, never inside the Art. 47
  documented-amounts floor's document total for IVA purposes), and a
  validation REJECTS any tax-combination config or computed line where the
  contribution amount contaminates the IVA base (IVA applies to the fuel
  price ONLY); the guard's coexistence root is Art. 2 (LB-011 pointer —
  IVA applies over the same fuel acts alongside the contributions, each on
  its own base discipline); the SR8 file owns the quantity-tax-side twin
  of this guard (SV-SPE-FR-168 by id — never restated), this file owning
  the Ley-side rule the base engine enforces. SOQ-39 resolved (86_-89_
  owned): the guard holds for ANY per-unit fuel contribution configured
  in the family, provenance now instrument-dated ($0.20 = D.L. 597-2001
  Art. 26 reform per 88_; $0.10 = COTRANS 89_ Art. 3 — OQ-3 resolved).
  (LB-001; LB-002; LB-006; LB-011; LB-012; EVID-315/316/305/274)
- **SV-TAX-FR-243:** The system shall carry the contribution on legal
  documents in a FILA O CASILLA ESPECIAL (special row or box) SEPARATELY
  from BOTH the sale price AND the IVA (31_ §IV.1 documentation rule) —
  on the DTE surface this is the CAT-015 D1 tributo line consumed from
  e-invoicing BY ID (SV-EINV-FR-017 per-type tributo wiring — never
  restated here), the document-side twin owned by SR8 SV-SPE-FR-169 by
  id; the base-side consequence THIS file enforces: the IVA line and the
  contribution line are computed on independent inputs (IVA = rate ×
  price-only base per FR-241/242; contribution = $/gal × quantity) and
  the printed/stored totals keep them in separate filas — parallel to the
  Art. 57 separate-from-price CCF discipline (LB-013 pointer: the
  trasladado IVA constates separate from the price; the contribution
  constates separate from BOTH).
  (LB-012; LB-013; EVID-274/317)

### 3.7 SOQ-40 design pass — the B2B recovery chain mapped onto DTE tributo lines (DESIGN rows)

- **SV-TAX-FR-244:** **[DESIGN — SOQ-40]** The system shall implement the
  B2B recovery-chain → DTE mapping as follows: each chain seller — first
  tier (importador/refinador) and every B2B intermediate — emits its fuel
  sale document WITH the D1 tributo line for the operation's contribution
  amount ($0.20 × galones per line, the FR-242/243 disciplines), while the
  accounting surface books: the first-tier sale a RETENCIÓN-FOVIAL credit
  (liability), and each intermediate's purchase a CUENTAS-POR-COBRAR-FOVIAL
  debit which its own sale's re-billed contribution CREDITS closed — the
  control-account mechanics OWNED by SR8 (SV-SPE-FR-170/171 by id, never
  restated) — so that the D1 tributo line on every FE/CCF in the chain is
  the fiscal-document echo of the same $0.20×gal that the control accounts
  pass through, and the FINAL CONSUMER absorbs it (booking per SR8
  SV-SPE-FR-172's cost/expense election, by id). CHAIN INVARIANT
  (design-level): for every pass-through intermediate, purchases-side
  CUENTAS-POR-COBRAR-FOVIAL debits = sales-side re-billed credits (net
  zero at tier close), and the D1 line per operation always equals $rate ×
  quantity at the operation date. PROVENANCE-VINTAGE NOTE (binding): the
  chain mechanics are 2001-GUIDE VINTAGE (31_ predates e-invoicing); the
  DTE mapping is DESIGN (SOQ-40), NOT statutory — no corpus instrument
  prescribes D1-on-chain-documents as the recovery mechanism; the rows are
  labeled design and re-validate at the OQ-2 design confirmation (instruments owned since W18).
  (LB-012; EVID-274; SOQ-40; SPE 08-file SV-SPE-FR-170/171/172)
- **SV-TAX-FR-245:** **[DESIGN — SOQ-40]** The system shall ship
  the COTRANS side of the design pass CONFIG-GATED: the C8 tributo line
  (CAT-015 code consumed from e-invoicing by id — SV-EINV-FR-017) and the
  COTRANS quantity-tax family row (SR8 SV-SPE-FR-174 by id —
  instrument-anchored via 89_ (spe/08 LB-011 by id)) wire into the SAME
  never-in-base guard (FR-242), fila/casilla separation (FR-243) and
  chain-mapping design (FR-244) as FOVIAL, but the chain/config rows ship
  ANCHORED to 89_ (activation satisfiable since W19; the C8 row activates
  inside the 89_ vigencia window, valid_from 23-dic-2021 through
  31-dic-2026 per the registry prorroga chain — texts not acquired,
  spe/08 OQ-8 watch) while the never-in-base guard stays
  instrument-independent per FR-242.
  (LB-012; EVID-274; SOQ-39; SPE 08-file SV-SPE-FR-174)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the Art. 54 rate history and the per-unit
contribution values are D15 dated configuration rows with instrument
provenance (the rate rows in-file here; the $/gal rows owned by SR8's
quantity-tax family, by id — never duplicated). Layer semantics: Odoo-side
base/rate/guard computation data only (wave default `odoo`; see §5).
**Interface entity for the wave's later files (determination/credit,
adjustments-assets, retention) and the index:** the base-composition
record + per-operation débito below.

**Base-composition engine (Art. 47-53):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (SV extension) | l10n_sv_iva_base_source | select | precio_pactado · remate_adjudicacion_mas_subastador · renta_periodica · valor_residual · retiro_asignado_publico · retiro_mercado · establecimiento_bienes · permuta_lado_propio · bienes_pago_servicio · import_cif_aduanero_aranceles_especificos · contraprestacion_total · contrato_convenido · bienes_agregados_48j · autoconsumo_asignado_mercado · renta_convenida · comision | FR-226..232 |
| account.move (SV extension) | l10n_sv_iva_base_documented_floor | monetary (computed) | Art. 47 floor: max(computed base, documented amounts) after 51/52/53 adjustments | FR-225 |
| account.move.line (SV extension) | l10n_sv_iva_nonbase_tag | select | indemnizacion · propina · cotizacion_provisional_sindical · multa_penal_clausula · interes_terceros_financiador · mandato_nombre_y_cuenta · descuento_general_incondicionado_documentado | FR-233, FR-234, FR-237 |
| account.move.line (SV extension) | l10n_sv_iva_addition_kind | select | reajuste_actualizacion · financiacion_operacion · interes_mora · gastos_fletes · reembolso (unless nonbase-tagged) · accesorio (independent-prestación flag) · envase · deposito_garantia · impuesto_especial · fx_delta_cuota | FR-234, FR-235, FR-236, FR-238 |
| account.move (SV extension) | l10n_sv_iva_mixed_proration | boolean + factor | additions over gravada+exenta operations prorated (T1/T2 classification feed, by id) | FR-236 |

**Rate and débito (Arts. 54-55):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.rate (new) | valid_from · valid_to · rate · provenance | date / date / % / char | 1992-09-01 · [cutover OQ-4] · 10% · "Ley original D.L. 296-1992 (EVID-317 gloss)"; [cutover] · open · 13% · "Art. 54 stamp (2) = D.L. 370-1995, D.O. 114 T.327 21-jun-1995" | FR-240 |
| account.tax (IVA template) | l10n_sv_iva_rate_row_id | m2o | resolved as-of tax-point date (D15 snapshot on the move) | FR-240, FR-241 |
| account.move.line (tax line) | l10n_sv_iva_debito | monetary (computed) | rate × base PER OPERATION line; determination sums (T4 pointer) | FR-241 |

**FX (Art. 53; Rgto. Art. 18):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (SV extension) | l10n_sv_iva_fx_rate_hecho_generador | float (snapshot) | hecho-generador-day rate (D15; rate source open — 00_index OQ-006 kin) | FR-238 |
| account.move (installment collection) | l10n_sv_iva_fx_cuota_delta | monetary (computed) | celebration-vs-payment FX delta of ventas a plazo, ADDED to base at collection | FR-238 |
| account.move (import) | l10n_sv_iva_aduana_acceptance_rate · acceptance_date | float / date | Rgto. Art. 18: póliza/formulario aduanero acceptance-day conversion | FR-239 |

**FOVIAL/COTRANS guard + SOQ-40 design (Ley-side; SR8 twins by id):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.tax (quantity-tax family) | iva_base_exclusion invariant | boolean/computed | consumed from SR8's field family (SV-SPE-FR-167/168 by id — never duplicated); the base-engine validation rejects any composition where the contribution enters an IVA base | FR-242 |
| account.move.line (fuel line) | l10n_sv_iva_price_only_base | monetary (computed) | IVA base = price only; D1/C8 tributo line = $/gal × qty on its own fila (DTE emission = e-invoicing SV-EINV-FR-017, by id) | FR-242, FR-243 |
| account.move.line (fuel, B2B) | l10n_sv_fovial_chain_echo | m2o control-account move | design: D1 line ↔ RETENCIÓN/CUENTAS-POR-COBRAR-FOVIAL booking link (SR8 SV-SPE-FR-170/171 own the accounts); chain invariant net-zero monitor | FR-244 |
| account.tax (COTRANS row) | l10n_sv_config_gated | boolean + activation slot | design: C8 chain/config rows anchored to 89_ (satisfiable since W19; SOQ-39 consumed; SR8 SV-SPE-FR-174 by id) | FR-245 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = base/rate/guard computation logic
living in the LGPL client. No SaaS rows are introduced in this file: nothing
here touches DTE generation (the D1/C8 tributo emission is e-invoicing's
SV-EINV-FR-017 by id; the F-07 annex surfaces are fiscal-reporting's
SV-FREP-FR-048/066 by id — this file supplies the computed values they
consume). Model names are stable across Odoo 17/18/19/20 (`account.move`,
`account.move.line`, `account.tax`, `l10n_sv.*` new config models);
version-specific behavior is recorded per row where a legal vintage exists.
D15 doctrine (binding): every parameter (rate row, FX rate, $/gal value)
resolves as-of the tax-point date snapshotted on the record; corrections
use ORIGINAL-period parameters.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-225 | odoo | account.move.line + computation | base_source + documented floor | Art. 47 generic rule; contado/crédito indifferent; omission/mora never blocks; consumes 07/08 classification by id |
| FR-226 | odoo | account.move.line | base_source (a/d/f) | Remate = adjudicación + subastador rights; establecimientos = movable-goods value only; services-paid sales = goods value |
| FR-227 | odoo | account.move.line (lease) | renta_periodica / valor_residual | Rgto. 17: residual = última cuota o adicional as pacted; débito per renta AND per residual (two tracks) |
| FR-228 | odoo | account.stock.usage → move line | retiro base source | 48-c owned here; 07 FR-186 consumes (LB-027 pointer there); assigned public price else mercado |
| FR-229 | odoo | account.move.line (permuta pair) | permuta_lado_propio | TWO débitos, one per side; mutuos de cosas same rule |
| FR-230 | odoo | account.move (import) | CIF+arancel+específicos composition | IVA NEVER in base (absolute); FX per FR-239; SR4 clock feed by id (07 FR-190) |
| FR-231 | odoo | account.move.line (service) | contraprestacion_total / bienes_agregados_48j | 48-j aggregation even over standalone-exempt goods (08 codes by id) unless already in contract value |
| FR-232 | odoo | account.move.line | autoconsumo (market floor) / renta_convenida / comision | Commission-only for intermediaries; housing leases = 08 surface by id |
| FR-233 | odoo | account.move.line | nonbase_tag | Indemnizaciones/propinas/cotizaciones never enter any base |
| FR-234 | odoo | account.move.line | addition_kind (51-a) | Financing interest INCL. mora; mandate name-and-account exception; multas/penal-clause and third-party-interest OUT |
| FR-235 | odoo | account.move.line | addition_kind (51-b/c) | Accessories list with independent-prestación flag; envases + depósitos-garantía IN |
| FR-236 | odoo | account.move.line + proration | impuesto_especial + mixed proration | IVA excluded from base ALWAYS; FOVIAL/COTRANS handled by FR-242 guard; T1/T2 split feed by id |
| FR-237 | odoo | account.move.line | descuento gate | 52 exclusion: general + unconditional + direct + already documented in CCF/ND/NC — all four gates |
| FR-238 | odoo | account.move | fx_rate_hecho_generador + cuota_delta | Hecho-generador-day conversion; payment diffs OUT; installment deltas IN at collection; CT-62 kin SV-TAX-FR-020 + origin-rate SV-EINV-FR-164 by id; rate source open (OQ-006 kin) |
| FR-239 | odoo | account.move (import) | aduana_acceptance_rate/date | Rgto. 18 acceptance-day conversion (DUCA kin, SOQ-45 kin) |
| FR-240 | odoo | l10n_sv.iva.rate | dated rows + provenance | 13% (D.L. 370-1995 stamp) + 10% history; D15 as-of resolution; SOQ-54 watch; cutover day OQ-4 |
| FR-241 | odoo | account.move.line (tax line) | debito per operation | rate × base per operation; F-07 M/O consumers SV-FREP-FR-048/066 by id (S3 02 rate-anchor closure); CCF on-top kin SV-EINV-FR-024 by id |
| FR-242 | odoo | computation guard (base engine) | price_only_base + validation | Ley-side root (Arts. 47/48-a/51-d via 31_ §IV.1); SR8 SV-SPE-FR-168 twin by id; rejects base contamination; instrument-independent |
| FR-243 | odoo | account.move.line (fuel) + doc fields | fila/casilla separation | Price/IVA/contribution in separate filas; D1 emission = SV-EINV-FR-017 by id; Art. 57 separate-from-price parallel (LB-013 pointer) |
| FR-244 | odoo | account.move.line + control-account link | chain_echo [DESIGN] | SOQ-40: D1-per-operation ↔ RETENCIÓN/CUENTAS-POR-COBRAR-FOVIAL (SR8 FR-170/171 own accounts); net-zero chain invariant; 2001-vintage vs design labeled |
| FR-245 | odoo | account.tax (COTRANS) | config_gated [DESIGN] | anchored to 89_ (SOQ-39 consumed W19); guard itself already live per FR-242; SR8 SV-SPE-FR-174 by id |

Version-regime notes (D12/D15): FR-240 carries the rate-history rows (10%
1992 → 13% D.L. 370-1995; exact cutover day unpinned — OQ-4; SOQ-54 watch
on the current row). FR-238/239/240 carry the D15 snapshot doctrine
(hecho-generador-day / acceptance-day / tax-point-dated resolution with
original-period correction parameters). FR-244/245 are DESIGN rows (SOQ-40):
the chain mechanics are 31_'s 2001 print and the DTE mapping is this wave's
design — instruments now OWNED (SOQ-39 resolved, 86_-89_: $0.20 = D.L.
597-2001 Art. 26 reform per 88_; COTRANS = passenger-tariff $0.10/galón,
89_ Art. 3), so the DTE-mapping design confirmation (OQ-2) is unblocked
and the provenance rows stand re-dated (OQ-3 resolved).
The SOQ-54 consolidation watch rides every LB (§2 preamble) — re-verify
against a current official consolidation at implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a gravada sale whose law-mandated documents state
  $1,000.00 while the parties renegotiated $900.00, when the base computes,
  then the base resolves to $1,000.00 — the documented-amounts floor
  prevails — and given a credit (al crédito) sale with payment deferred 90
  days, then the base computes identically at the tax point (omission/plazo
  never blocks) (FR-225).
- **AC-002:** Given an auction (remate) sale adjudicated at $5,000.00 with
  $300.00 auctioneer rights, when the base computes, then it resolves to
  $5,300.00 (FR-226).
- **AC-003:** Given a goods lease with purchase option at $500.00 monthly
  renta and a pacted residual equal to the last cuota's value, when 12 rentas
  run, then EACH renta carries its own débito on its $500.00 base; and when
  the option is exercised, then a SEPARATE débito computes on the residual
  value (Rgto. Art. 17 — never folded into the last renta) (FR-227).
- **AC-004:** Given a permuta where party A delivers goods valued $10,000.00
  and party B goods valued $7,000.00, when the operation books, then TWO
  débitos compute — one per side, each on its OWN side's goods value
  ($10,000.00 base for A's sale, $7,000.00 base for B's) (FR-229).
- **AC-005:** Given a retiro of goods with an assigned public-sale price of
  $130.00 in the records, when the retiro invoice computes, then the base is
  $130.00 — or, absent any assigned price, the precio corriente de mercado
  (FR-228).
- **AC-006:** Given an import with CIF value $1,000.00, aranceles $100.00
  and a specific consumption tax $50.00, when the base computes, then it
  resolves to $1,150.00 and the IVA paid at import NEVER re-enters the base
  (absolute exclusion) (FR-230).
- **AC-007:** Given an installation contract priced $2,000.00 where the
  prestador supplies materials worth $500.00 whose standalone transfer would
  be exempt (T2 code, by id) and the contract value does NOT comprise them,
  when the base computes, then it resolves to $2,500.00 (48-j aggregation
  over standalone-exempt goods); given the same contract that ALREADY
  comprises the materials, then the base stays $2,000.00 (no double count)
  (FR-231).
- **AC-008:** Given a deferred sale carrying 2% financing interest and a
  $200.00 penal-clause fine, when the base recomputes, then the financing
  interest ADDS to the base (incl. late-payment interest when it accrues)
  and the penal-clause multa is REJECTED from the base (FR-234).
- **AC-009:** Given a $150.00 expense reimbursement paid in the name and
  account of the buyer under his recorded mandate, when the base computes,
  then the reimbursement stays OUT of the base; given the same amount rebilled
  as the seller's own charge, then it ADDS (FR-234).
- **AC-010:** Given a sale with separately documented envases worth $20.00
  and a $10.00 returnable-container guarantee deposit, when the base
  computes, then both ADD to the base (FR-235).
- **AC-011:** Given a fuel line of 1,000 galones at $2.00/gal with FOVIAL
  configured, when the document computes, then the D1 tributo line resolves
  to $200.00 ($0.20 × 1,000) in its OWN fila, the IVA base resolves to
  $2,000.00 (price only) and the IVA to $260.00 — and any composition or
  tax-config attempt feeding the $200.00 into the IVA base is REJECTED by
  the guard (FR-242, FR-243).
- **AC-012:** Given a mixed operation 60% gravada / 40% exenta (T1/T2
  split, by id) with a $100.00 accessory addition, when the base adjusts,
  then $60.00 of the addition apportions to the gravada base and $40.00 to
  the exenta side (proration) (FR-236).
- **AC-013:** Given a $50.00 general unconditional discount already
  documented in the CCF, when the base computes, then it is EXCLUDED;
  given a $50.00 discount conditioned on a future purchase, then it STAYS
  in the base (FR-237).
- **AC-014:** Given an installment sale in foreign currency celebrated at
  rate X with a cuota collected at a worse rate, when the collection posts,
  then the celebration-vs-payment FX delta ADDS to the base in the
  collection period; given instead a spot sale paid later at a different
  rate, then the payment FX difference NEVER enters the base (FR-238).
- **AC-015:** Given operations dated after the D.L. 370-1995 cutover, when
  the débito computes, then the rate row resolves to 13% and the débito =
  0.13 × base PER OPERATION line; given a 1993-dated operation (historical
  import), then the 10% history row applies (D15 original-period
  resolution) (FR-240, FR-241).
- **AC-016:** Given the FR-048 consumer surface (F-07 Anexo 1 row, by id),
  when the M débito column fills, then it carries this engine's per-document
  débito (rate × base) — the S3 rate-anchor pointer is closed by this file
  (FR-241).
- **AC-017:** Given a B2B fuel chain distributor buying 1,000 gal (D1 $200
  on the purchase document) and selling the same 1,000 gal onward (D1 $200
  re-billed on its sale document), when the tier closes, then its
  CUENTAS-POR-COBRAR-FOVIAL nets to zero and each document carried its own
  per-operation D1 line — the design chain invariant (FR-244); given
  COTRANS outside the 89_ vigencia window (or the C8 row disabled), then no
  C8 chain rows activate while the never-in-base guard already covers the
  family (FR-245).
- **AC-018:** Given an import whose foreign-currency customs value
  converts, when the import move resolves, then the USD conversion uses the
  póliza/formulario ACCEPTANCE-day rate recorded as the FX anchor (FR-239).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Load-bearing here for the 13% rate row (FR-240) and the base machinery alike. Re-verify Arts. 47-55 + Rgto. Arts. 17-18 at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | SOQ-40 (design pass): the 2001 control-account chain (RETENCIÓN-FOVIAL / CUENTAS-POR-COBRAR-FOVIAL re-bill) is 31_-guide vintage and PREDATES e-invoicing; the mapping onto DTE-embedded D1 tributo lines (one per operation across FE/CCF chains, final consumer absorbing) is THIS file's DESIGN (FR-244/245), not statutory — no corpus instrument prescribes it. Confirm the intended modern mechanics (D1-line-per-document as the recovery echo vs any MH/DGII chain rule) at FOVIAL-law acquisition; SR8's design-pass pointer (SV-SPE-FR-175) records the same handoff. | no | Takumi S9 + Odoo implementation | open |
| OQ-3 | SOQ-39/MOQ-04 (guard note): **RESOLVED — instruments ACQUIRED W18, consumed W19 (86_-89_; spe/08 LB-008..012 + FR-185..189 own the instrument-side mechanics)**: FOVIAL = 86_ (D.L. 208-2000 consolidated through D.L. 93-2012) + 87_/88_ D.O. prints — the $0.20/galón value is D.L. 597-2001's Art. 26 reform text per 88_ (in force 17-nov-2001), no longer catalog-print-only; COTRANS = 89_ (D.L. 257-2021, passenger-tariff-stabilization contribution — NOT transportistas de carga — $0.10/galón Art. 3, vigencia through 31-dic-2026 per the prorroga tail). FR-242's guard is UNCHANGED (instrument-independent — it excludes ANY configured per-unit fuel contribution from the IVA base); FR anchors intact; FR-245's COTRANS activation gate is now satisfiable via 89_ (chain-mechanics rewire rides the SR8 wave). Residual = OQ-2's D1-mapping design confirmation (now unblocked). **Rewire landed W20: FR-245/§4/§5/AC-017 now anchor to 89_ (vigencia window through 31-dic-2026).** | no | Takumi S9 (sources registry) | **resolved** (W19; 86_-89_) |
| OQ-4 | Rate-cutover precision: Art. 54's stamp (2) prints D.L. 370 dated 8-jun-1995 with D.O. 114 T.327 of 21-jun-1995 "(13 %)", and EVID-317 glosses "effective jun-1995" — but the exact vigencia DAY (publication date? eight days after? retro to the decree date?) is unprinted in the corpus, and the pre-reform 10% value itself rests on the EVID-317 gloss, not on a printed 1992 Art. 54 text. The FR-240 history rows carry the cutover as an unpinned boundary (conservative default: D.O. publication 21-jun-1995, flagged). Pin from the D.L. 370 text or an official consolidation before historical-import certification. | no | Takumi S9 (sources registry) | open |
