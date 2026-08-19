# SV — Special regimes — FOVIAL/COTRANS quantity contributions

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes) |
| Updated | 2026-08-19 |

## 1. Purpose

This file owns the fuel-quantity contribution layer of the
special-regimes wave (master cluster SR8): the FOVIAL *Contribución de
Conservación Vial* (road-conservation contribution) of **$0.20 per
galón** (gallon) on diesel, gasolinas y sus mezclas con otros
carburantes (gasoline and its blends with other fuels — aviation
gasoline excluded), whose corpus authority is the DGII orientation
guide 31_ printing D.L. N° 208-2000 Art. 26 as reformed by D.L. N°
597-2001 (the LAW text itself is not in corpus — SOQ-39): its hechos
generadores (taxable events — first-tier sale/transfer by
importadores/refinadores and direct import for own consumption), the
quantity-based Odoo `account.tax` per-unit design with D15 dated value
rows and instrument provenance, the IVA-base exclusion guard (the
contribution is NOT *base imponible* nor an addition to it — never
charge/recargar IVA on it), the separate document *fila o casilla*
(row/box), the B2B control-account chain the guide prints
ledger-by-ledger (RETENCIÓN FOVIAL at the first sale; CUENTAS POR
COBRAR-FOVIAL re-billed through every intermediate until the final
consumer absorbs it, then cost/operating/manufacturing-expense
classification with the Ley ISR Art. 29.6 own-consumption deduction),
and the COTRANS print-anchor surface (CAT-015 code C8, $0.10/galón —
instrument absent, MOQ-04 half-open).

It does **not** cover: the Ley IVA computation mechanics themselves
(IVA-core wave territory — this file records the base-exclusion
invariant and the SOQ-40 design-pass pointer, never the engine); DTE
tributo-line generation and per-type CAT-015 restrictions
(`e-invoicing/01_document-types.md` SV-EINV-FR-017/SV-EINV-FR-046 by
id); the F-07 fuel annexes 13-14 and the casilla-525 credit interplay
(`fiscal-reporting/05_f07-annexes-special.md` SV-FREP-FR-124..129 and
`01_f07-declaration.md` SV-FREP-FR-020 by id — pointers only); the
ISR deduction surface (`taxation/02_isr-deductions.md` SV-TAX-FR-045
by id); the fuel price-cap/tasa-diferenciada regimes of Decreto 321
and the Ley Especial Transitoria (fiscal-reporting/05 by id); and the
regime profile/benefit-state surfaces of files 01-07 (FOVIAL/COTRANS
ride ordinary fuel transactions, not regime admissions).

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): FOVIAL =
**31_** — *Guía de Orientación Nº DG-002/2001*, DGII, 26-nov-2001,
"Guía de orientación general para el tratamiento, documentación,
control tributario y contabilización de la Contribución de
Conservación Vial" (6 pp.). **Provenance chain (THE point of this
file): 31_ is a DGII orientation guide = SECONDARY authority** whose
§II/§IV.1 fundamento prints **Art. 26 de la Ley del Fondo de
Conservación Vial, D.L. N° 208 (D.O. N° 237 T.349 18-dic-2000),
reformado por D.L. N° 597 (31-oct-2001, D.O. N° 212 T.353 9-nov-2001)**
— the LAW TEXT IS NOT IN CORPUS (SOQ-39); LB rows therefore cite 31_
with the law articles **as printed BY the guide**, and the Ley IVA
Arts. 47/48-a)/51-d) anchors equally ride the guide (the guide quotes
their effect; the Ley IVA text and its engine belong to the taxation
IVA-core wave). The guide additionally cites CT Art. 15 inciso
primero (contribución especial nature), CT Art. 116 (document
printing) and CT Art. 139 incisos 2°/3° (formal-accounting
obligation) — all as printed by 31_ (the CT corpus text belongs to
the taxation wave). **Title-vs-content defect (recorded at W13):**
the source file/registry title says "Guía FOVIAL y COTRANS" but the
content covers ONLY FOVIAL — COTRANS is absent from 31_ (registry row
amended; EVID-274 header).

**SOQ-30 verification note (adapted to this file, rides EVERY LB
below):** the vintage risk here is the **2001 guide + the 2000/2001
law chain** — post-597-2001 reforms and the current per-gallon value
are unverified against the instrument; article text is cited **as
printed**. CAT-015 v1.1 (2026-07 re-versioning, source 51_) prints
"$0.20 Ctvs. por galón" for code D1 — consistent with the 2001 guide,
which is NOTED as a consistency check only: the catalog is NOT the
authority (instrument-provenance discipline; SOQ-39). Verbatim text
below is copied from the W13 evidence file (EVID-274) and, where the
evidence abbreviates, from the extraction txt
`sv/.extractions/31_Guia_FOVIAL_COTRANS.pdf.txt` (citable per
standing S3 ruling 25; page pointers = txt PAGE markers).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Guía DG-002/2001, §IV.1 (general aspects, quoting the law): el Art. 26 de la Ley del Fondo de Conservación Vial "ESTABLECE LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL Y TIPIFICA COMO HECHOS GENERADORES DE LA MISMA: a) LA VENTA O CUALQUIER FORMA DE TRANSFERENCIA DE PROPIEDAD DE DIESEL Y GASOLINAS O SUS MEZCLAS CON OTROS CARBURANTES EXCEPTUANDO LA GASOLINA DE AVIACIÓN, QUE REALICEN IMPORTADORES O REFINADORES; Y, b) LA IMPORTACIÓN QUE DE LOS MISMOS PRODUCTOS REALICEN DIRECTAMENTE OTRAS PERSONAS NATURALES O JURÍDICAS PARA SU CONSUMO PROPIO. EL VALOR DE LA CONTRIBUCIÓN DE LA CONSERVACIÓN VIAL ESTABLECIDA EN DICHA LEY ES DE VEINTE CENTAVOS DE DÓLAR DE LOS ESTADOS UNIDOS DE AMÉRICA (US $0.20) POR GALÓN DE DIESEL, GASOLINAS O SUS MEZCLAS CON OTROS CARBURANTES". §III ámbito: dirigida a las personas naturales o jurídicas que se dediquen a la venta o cualquier forma de transferencia de propiedad en el mercado local de diesel y gasolinas o sus mezclas con otros carburantes, exceptuando la gasolina de aviación, sean éstos importadores o refinadores; también aplicable a aquellas que realicen importación o internación directa de los mismos bienes para su consumo propio | Guide §IV.1 (general aspects, quoting the law): Art. 26 of the Road-Conservation Fund Law ESTABLISHES the road-conservation contribution and typifies as its taxable events: a) THE SALE OR ANY FORM OF TRANSFER OF OWNERSHIP OF DIESEL AND GASOLINES OR THEIR BLENDS WITH OTHER FUELS, EXCLUDING AVIATION GASOLINE, MADE BY IMPORTERS OR REFINERS; and b) THE IMPORT of the same products made DIRECTLY by other natural or legal persons FOR THEIR OWN CONSUMPTION. The value of the contribution established in said law is TWENTY CENTS OF UNITED STATES DOLLARS (US $0.20) PER GALLON of diesel, gasoline or their blends with other fuels. §III scope: natural or legal persons selling or otherwise transferring ownership in the local market of diesel/gasolines or blends (aviation gasoline excluded), whether importers or refiners; also those making direct import or internación of the same goods for their own consumption | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | §III/§IV.1 pp.1-2 (EVID-274; txt PAGES 1-2; law chain D.L. 208-2000 Art. 26 as reformed D.L. 597-2001 AS PRINTED BY 31_ — SOQ-39) |
| LB-002 | Guía DG-002/2001, §IV.1: "DICHO TRIBUTO DE ACUERDO A LO QUE ESTABLECE EL INCISO PRIMERO DEL ART. 15 DEL CÓDIGO TRIBUTARIO, CONSTITUYE UNA CONTRIBUCIÓN ESPECIAL, LA CUAL DE ACUERDO A LOS ARTS. 47, 48 LITERAL a) Y 51 LITERAL d) DE LA LEY DE IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS NO PUEDE CONSIDERARSE COMO BASE IMPONIBLE, NI COMO UNA ADICIÓN A ÉSTA PARA EFECTOS DE LA DETERMINACIÓN DEL REFERIDO IMPUESTO. EN TAL SENTIDO LOS VEINTE CENTAVOS DE DÓLAR DE LOS ESTADOS UNIDOS DE AMÉRICA ($0.20) CORRESPONDIENTES A LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL, NO ESTÁN AFECTOS AL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS (IVA), POR LO TANTO EN NINGÚN CASO SE DEBERÁ COBRAR NI RECARGAR TAL IMPUESTO SOBRE LA REFERIDA CONTRIBUCIÓN" | The tribute, per CT Art. 15 first inciso, CONSTITUTES A SPECIAL CONTRIBUTION which, per Arts. 47, 48 literal a) and 51 literal d) of the IVA Law, CANNOT be considered as the taxable base nor as an addition to it for purposes of determining that tax. The $0.20 corresponding to the road-conservation contribution is NOT subject to IVA — therefore IN NO CASE may such tax be charged or surcharged over said contribution | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | §IV.1 p.2 (EVID-274; txt PAGE 2; Ley IVA Arts. 47/48-a/51-d anchors via the guide — IVA-core wave owns the mechanics) |
| LB-003 | Guía DG-002/2001, §IV.2: el cobro "SE REALIZARÁ Y REFLEJARÁ EN LOS DOCUMENTOS LEGALES QUE EXIGE EL CÓDIGO TRIBUTARIO PARA EL CONTROL DEL [IVA]; EL VALOR DE DICHA CONTRIBUCIÓN, SE DETALLARÁ EN UNA FILA O CASILLA ESPECIAL SEPARADAMENTE DEL PRECIO DE VENTA DE LOS REFERIDOS COMBUSTIBLES Y DEL IMPUESTO (IVA) CORRESPONDIENTE A DICHOS COMBUSTIBLES"; los sujetos del Romano III podrán continuar utilizando los documentos legales existentes con los ajustes necesarios, y en las nuevas impresiones incluirán "UN ESPACIO O UNA CASILLA ESPECIAL PARA CONSIGNAR EL VALOR DE LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL" (requisito que incorporarán los impresores autorizados, para cumplir el Art. 116 del Código Tributario); "EN LOS CASOS DE CONTRIBUYENTES QUE ESTÉN AUTORIZADOS POR LA ADMINISTRACIÓN TRIBUTARIA PARA LA EMISIÓN DE OTROS DOCUMENTOS LEGALES EN SUSTITUCIÓN DE FACTURAS, TAMBIÉN SE CONSIGNARÁ EL VALOR DE LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL POR SEPARADO"; modelos ilustrativos en anexos | Collection is made and reflected in the legal documents the Tax Code requires for IVA control; the contribution's value is detailed in a SPECIAL ROW OR BOX, SEPARATE from the fuels' sale price AND from the corresponding IVA. The §III subjects may keep using their existing legal documents with the necessary adjustments; new printings include a space or special box for the contribution value (authorized printers incorporate this requirement, to comply with Tax Code Art. 116). Taxpayers authorized to issue OTHER legal documents in substitution of invoices also consign the contribution value SEPARATELY; illustrative models in annexes | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | §IV.2 p.3 (EVID-274; txt PAGE 3) |
| LB-004 | Guía DG-002/2001, §IV.3 (registro contable): los contribuyentes obligados a llevar contabilidad formal conforme el Art. 139 Incisos 2° y 3° del Código Tributario "CONTABILIZARÁN LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL, SEPARADAMENTE DE LOS VALORES DE VENTA E IMPUESTO (IVA), PARA TALES EFECTOS LLEVARÁN CUENTAS DE CONTROL ESPECIALES". Ejemplos 1°-4° (1,000 gal gas 90 octanos): 1° compra importación refinería/importador: INVENTARIO O COMPRAS $1,000.00 + IVA CRÉDITO FISCAL $130.00 contra BANCOS $1,130.00; 2° venta local de refinerías a distribuidores (e importadores a concesionarios, gasolineras y otros clientes): CLIENTES O CAJA $2,460.00 contra IVA DÉBITO FISCAL $260.00, RETENCIÓN FOVIAL $200.00 (1000 gal por $0.20) y VENTAS $2,000.00; 3° compra de distribuidores a refinerías: INVENTARIOS O COMPRAS $2,000.00 + CUENTAS POR COBRAR-FOVIAL $200.00 (1000 galones por $0.20) + IVA CRÉDITO FISCAL $260.00 contra BANCOS O PROVEEDORES $2,460.00; 4° venta local de distribuidores a concesionarios/gasolineras/otros: CLIENTES O CAJA $3,590.00 contra IVA DÉBITO FISCAL $390.00, CUENTAS POR COBRAR FOVIAL $200.00 (1000 galones por $0.20) y VENTAS $3,000.00 | §IV.3 (ledger register): taxpayers obliged to formal accounting per Tax Code Art. 139 incisos 2°/3° account the contribution SEPARATELY from sale values and IVA, carrying SPECIAL CONTROL ACCOUNTS. Ledger examples 1°-4° (1,000 gal 90-octane gas): 1° refiner/importer import purchase: INVENTORY/PURCHASES $1,000.00 + IVA FISCAL CREDIT $130.00 against BANKS $1,130.00; 2° local sale by refiners to distributors (and importers to concessionaires, service stations and other clients): CLIENTS/CASH $2,460.00 against IVA FISCAL DEBIT $260.00, FOVIAL RETENTION $200.00 (1,000 gal × $0.20) and SALES $2,000.00; 3° distributor purchase from refiners: INVENTORIES/PURCHASES $2,000.00 + FOVIAL ACCOUNTS-RECEIVABLE $200.00 (1,000 gal × $0.20) + IVA FISCAL CREDIT $260.00 against BANKS/SUPPLIERS $2,460.00; 4° distributor local sale to concessionaires/service stations/others: CLIENTS/CASH $3,590.00 against IVA FISCAL DEBIT $390.00, FOVIAL ACCOUNTS-RECEIVABLE $200.00 and SALES $3,000.00 | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | §IV.3 pp.3-4 (EVID-274; txt PAGES 3-4) |
| LB-005 | Guía DG-002/2001, §IV.3 ejemplos 5°-7° y NOTA: 5° compra por concesionarios/gasolineras/detallistas a distribuidores: INVENTARIOS O COMPRAS $3,000.00 + CUENTAS POR COBRAR-FOVIAL $200.00 + IVA CRÉDITO FISCAL $390.00 contra BANCOS O PROVEEDORES $3,590.00; 6° venta de concesionarios/gasolineras/detallistas a los consumidores "SEAN ÉSTOS CONTRIBUYENTES O CONSUMIDORES FINALES": CLIENTES O CAJA $4,720.00 contra IVA DÉBITO FISCAL $520.00, CUENTAS POR COBRAR FOVIAL $200.00 y VENTAS $4,000.00; 7° compra de combustibles hechas por CONTRIBUYENTES PARA SU CONSUMO PROPIO: INVENTARIOS O COMPRAS $4,200.00 "(COMPRA DE 1000 GAL. GAS 90 OCTANOS INCLUYENDO LA CONTRIBUCIÓN)" + IVA CRÉDITO FISCAL $520.00 contra BANCOS O PROVEEDORES $4,720.00. NOTA: "EN ESTE CASO, LOS CONTRIBUYENTES CUANDO ADQUIERAN LOS COMBUSTIBLES A SU ELECCIÓN Y DADAS LAS CARACTERÍSTICAS ESPECÍFICAS DEL GIRO DE LA ENTIDAD, PODRÁN CONTABILIZAR LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL COMO PARTE DEL COSTO DE LOS COMBUSTIBLES, COMO UN GASTO DE OPERACIÓN (CONTRIBUCIONES FISCALES O IMPUESTOS) O COMO UN GASTO DE FABRICACIÓN (CONTRIBUCIONES FISCALES O IMPUESTOS). IGUAL TRATAMIENTO ES APLICABLE A LOS CONSUMIDORES FINALES" | Ledger examples 5°-7° and NOTE: 5° purchase by concessionaires/service stations/retail sellers from distributors: INVENTORIES/PURCHASES $3,000.00 + FOVIAL ACCOUNTS-RECEIVABLE $200.00 + IVA FISCAL CREDIT $390.00 against BANKS/SUPPLIERS $3,590.00; 6° sale by those retailers to the fuel consumers "WHETHER TAXPAYERS OR FINAL CONSUMERS": CLIENTS/CASH $4,720.00 against IVA FISCAL DEBIT $520.00, FOVIAL ACCOUNTS-RECEIVABLE $200.00 and SALES $4,000.00; 7° purchase by TAXPAYERS FOR THEIR OWN CONSUMPTION: INVENTORIES/PURCHASES $4,200.00 (1,000-gal purchase INCLUDING THE CONTRIBUTION) + IVA FISCAL CREDIT $520.00 against BANKS/SUPPLIERS $4,720.00. NOTE: such taxpayers, when acquiring fuels, AT THEIR ELECTION and given the entity's specific business characteristics, may account the contribution AS PART OF THE COST OF THE FUELS, AS AN OPERATING EXPENSE (fiscal contributions or taxes) OR AS A MANUFACTURING EXPENSE (fiscal contributions or taxes); THE SAME TREATMENT APPLIES TO FINAL CONSUMERS | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | §IV.3 pp.4-5 (EVID-274; txt PAGES 4-5; IVA crédito $520 = 13% × $4,000 price only — the $200 contribution never enters the IVA base) |
| LB-006 | Guía DG-002/2001, §IV.3 NOTA final (ISR): "LOS SUJETOS PASIVOS DEL IMPUESTO SOBRE LA RENTA QUE IMPORTEN DIRECTAMENTE O ADQUIERAN LOCALMENTE DIESEL Y GASOLINAS O SUS MEZCLAS CON OTROS CARBURANTES EXCEPTUANDO LOS QUE ESTABLECE EL ARTÍCULO 26 DE LA LEY DEL FONDO DE CONSERVACIÓN VIAL, PARA SU PROPIO CONSUMO Y QUE SEAN NECESARIOS EN EL DESARROLLO EXCLUSIVO DE LA GENERACIÓN Y PRODUCCIÓN DE SUS RENTAS GRAVABLES O QUE GRAVEN LA FUENTE PRODUCTORA DE LA RENTA, PODRÁN DEDUCIRSE COMO COSTO O GASTO PARA EFECTOS DEL REFERIDO IMPUESTO, LA CONTRIBUCIÓN DE CONSERVACIÓN VIAL SEGÚN LO ESTABLECE EL ARTÍCULO 29 NUMERAL 6) DE LA LEY DE IMPUESTO SOBRE LA RENTA" (Ley ISR contenida en el D.L. N° 134 del 18-dic-1991, per §II fundamento) | Final NOTE (ISR): ISR taxpayers who import DIRECTLY or acquire LOCALLY diesel/gasolines or blends (excepting those established by Art. 26 of the Road-Conservation Fund Law) FOR THEIR OWN CONSUMPTION and NECESSARY for the exclusive development of the generation and production of their taxable income or of the income-producing source, MAY DEDUCT the road-conservation contribution AS COST OR EXPENSE for ISR purposes, as established by ARTICLE 29 NUMERAL 6) of the ISR Law (D.L. N° 134-1991, per the guide's §II fundamento; the consolidated Art. 29.6 deduction surface = taxation/02 SV-TAX-FR-045 by id — never restated here) | `sv/sources/31_Guia_FOVIAL_COTRANS.pdf` | §IV.3 NOTA final pp.5-6 (EVID-274; txt PAGES 5-6) |
| LB-007 | Catálogo de Tributos CAT-015 v1.1 (2026-07 re-versioning), sección "TRIBUTOS APLICADOS POR ÍTEMS REFLEJADOS EN EL RESUMEN DEL DTE": fila "D1, FOVIAL ($0.20 Ctvs. por galón)"; fila "C8, COTRANS ($0.10 Ctvs. por galón)" | Tributes catalog CAT-015 v1.1, section "tributes applied per item reflected in the DTE summary": row D1 FOVIAL ($0.20 cents per gallon); row C8 COTRANS ($0.10 cents per gallon) — the DTE tributo print anchors. PRINT ANCHOR ONLY, NOT the legal instrument: D1's instrument chain rides 31_/D.L. 208-2000 (LB-001); C8's instrument is ABSENT (SOQ-39/MOQ-04 half-open) — the $0.10 is dated catalog data, never authority | `sv/sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx` (sidecar `sv/requirements/catalogs/CAT-015_tributos.csv` §1; D1/C8 consumption by e-invoicing SV-EINV-FR-017/046 by id) | CAT-015 §1 rows D1/C8 (2026-07 print; EVID-274 wire-kin; SOQ-39) |

## 3. Functional Requirements

### 3.1 FOVIAL — scope, hechos generadores and the quantity-tax model

- **SV-SPE-FR-166:** The system shall carry the FOVIAL scope as a
  product-and-role predicate: the contribution applies to DIESEL,
  GASOLINAS O SUS MEZCLAS CON OTROS CARBURANTES (diesel, gasoline or
  their blends with other fuels — product-scope flag on the fuel
  product records), with GASOLINA DE AVIACIÓN (aviation gasoline)
  EXCLUDED, and is triggered by exactly two hechos generadores:
  (a) the venta o cualquier forma de transferencia de propiedad
  (sale or any form of ownership transfer) in the local market by
  IMPORTADORES O REFINADORES (importers or refiners), and (b) the
  importación o internación directa (direct import) of the same goods
  by other personas naturales o jurídicas (natural or legal persons)
  PARA SU CONSUMO PROPIO (for their own consumption) — the fuel-chain
  role on the company/partner record (importador · refinador ·
  intermediate seller · consuming contribuyente) selects which
  trigger applies.
  (LB-001; EVID-274)
- **SV-SPE-FR-167:** The system shall model the FOVIAL contribution
  as a QUANTITY-BASED tax: an Odoo `account.tax` in the per-unit mode
  (amount_type `fixed` — unit amount × quantity; stable across Odoo
  17-20) computing $0.20 × galones, with the fuel products carried in
  the galón unit of measure so the tax line derives from the
  invoiced/moved quantity, NEVER from a price. The $0.20 value is a
  D15 DATED config row with instrument provenance (valid_from +
  provenance = D.L. 208-2000 Art. 26 as reformed D.L. 597-2001, AS
  PRINTED BY 31_; $0.20 = the 2001-printed value), resolved as-of the
  TRANSACTION DATE and snapshotted on the tax line; the CAT-015 v1.1
  2026-07 print of $0.20 (LB-007) is recorded as a CONSISTENCY NOTE
  on the row — the catalog is NOT the authority (SOQ-39). The tax
  config carries the legal nature *contribución especial* (special
  contribution, CT Art. 15 inciso primero as printed by 31_) and its
  CAT-015 code D1 for the DTE tributo wiring consumed from
  e-invoicing BY ID (SV-EINV-FR-017 per-type restrictions;
  SV-EINV-FR-046 FEXE prior-AT-authorization gate — never restated
  here).
  (LB-001; LB-002; LB-007; EVID-274; SOQ-39)
- **SV-SPE-FR-168:** The system shall enforce the IVA-base exclusion
  guard: the FOVIAL contribution is NOT *base imponible* (tax base)
  nor an addition to it (Ley IVA Arts. 47/48-a)/51-d) as printed by
  31_), so IVA computes ON THE PRICE ONLY and the system shall NEVER
  charge or recargar (surcharge) IVA — at any operative rate, the
  general 13% at current vintage — over the contribution. Implemented
  as an invariant on the quantity-tax family: the FOVIAL tax amount
  is excluded from every IVA base composition (never part of the
  price subtotal feeding IVA, never an adición) and a validation
  rejects any tax-combination config or computed line where the FOVIAL
  amount enters the IVA base; the D1 tributo line this guard feeds is
  e-invoicing's surface by id (SV-EINV-FR-017).
  (LB-002; LB-005; EVID-274)

### 3.2 Documentation — the separate fila/casilla

- **SV-SPE-FR-169:** The system shall reflect the contribution in the
  legal documents in a FILA O CASILLA ESPECIAL (special row or box)
  SEPARATELY from BOTH the fuel sale price AND the IVA: on the DTE
  surface this is the CAT-015 D1 tributo line (consumed from
  e-invoicing BY ID — SV-EINV-FR-017 wiring, LB-007 sidecar rows;
  this file owns only the amount/quantity that feeds it); on other
  legal documents authorized in substitution of facturas, the
  contribution value is likewise consigned SEPARATELY; the printed-
  document discipline of 31_ §IV.2 (existing documents adjusted; new
  printings carrying the special casilla per CT Art. 116 — the 2001
  print rule the DTE wiring inherits) is recorded as provenance.
  (LB-003; LB-007; EVID-274)

### 3.3 B2B chain control accounts (the 31_ ledger examples)

- **SV-SPE-FR-170:** The system shall account the contribution
  SEPARATELY from sale values and IVA through CUENTAS DE CONTROL
  ESPECIALES (special control accounts) for taxpayers under formal
  accounting (CT Art. 139 incisos 2°/3° as printed by 31_): the
  first-tier sale by a refiner/importer books the contribution as a
  RETENCIÓN FOVIAL credit (liability) — ledger example 2°: CLIENTES
  $2,460.00 against IVA DÉBITO FISCAL $260.00 + RETENCIÓN FOVIAL
  $200.00 (1,000 gal × $0.20) + VENTAS $2,000.00 — while the
  first-tier import purchase books inventories and IVA crédito only
  (example 1°: INVENTARIO $1,000.00 + IVA CRÉDITO $130.00 against
  BANCOS $1,130.00), the contribution entering the chain at the sale.
  (LB-004; EVID-274)
- **SV-SPE-FR-171:** The system shall implement the intermediate
  re-bill chain: every B2B intermediate (distribuidores,
  concesionarios, gasolineras y otros vendedores detallistas —
  distributors, concessionaires, service stations and other fuel
  retailers) books a CUENTAS POR COBRAR-FOVIAL (FOVIAL
  accounts-receivable) DEBIT at purchase (examples 3°/5°: the $200.00
  for 1,000 gal alongside inventories and IVA crédito) and RE-BILLS
  $0.20 × gal at its sale as the CREDIT closing the receivable
  (examples 4°/6°: CLIENTES $3,590.00/$4,720.00 against IVA DÉBITO +
  CUENTAS POR COBRAR FOVIAL $200.00 + VENTAS), so the $0.20×gal
  amount passes through every tier of the chain until the FINAL
  CONSUMER absorbs it; the control account's balance monitors the
  chain position (a pass-through intermediate's purchase-side
  receivable and sale-side re-bill net to zero).
  (LB-004; LB-005; EVID-274)
- **SV-SPE-FR-172:** The system shall carry the final-consumer
  classification as a per-entity ELECTION config: the consuming
  contribuyente — and equally the *consumidor final* (final
  consumer) — books the contribution, at its election and per the
  specific characteristics of its giro (business line), as part of
  the COSTO DE LOS COMBUSTIBLES (fuel cost), as a GASTO DE OPERACIÓN
  (operating expense — fiscal contributions or taxes) or as a GASTO
  DE FABRICACIÓN (manufacturing expense — fiscal contributions or
  taxes); the acquisition entry INCLUDES the contribution in the
  inventory/cost line (ledger example 7°: INVENTARIOS O COMPRAS
  $4,200.00 — 1,000 gal INCLUDING LA CONTRIBUCIÓN — + IVA CRÉDITO
  FISCAL $520.00 against BANCOS $4,720.00, the IVA crédito computed
  on the $4,000.00 price only, per FR-168's guard).
  (LB-005; EVID-274)
- **SV-SPE-FR-173:** The system shall expose the own-consumption
  acquisition for the ISR deduction: ISR sujetos pasivos (taxpayers)
  who import DIRECTLY or acquire LOCALLY in-scope fuels for their own
  consumption, when necessary in the exclusive development of the
  generation and production of their gravable rentas or the
  income-producing source, deduct the contribution as COSTO O GASTO
  per Ley ISR Art. 29 numeral 6) (D.L. 134-1991 as cited by 31_) —
  the deduction surface consumed from taxation BY ID (SV-TAX-FR-045,
  the Art. 29.6 taxes/rates/special-contributions caused-and-paid
  rule), with FR-172's classification election feeding the cost/expense
  account that the deduction reads; never restated here.
  (LB-006; EVID-274)

### 3.4 COTRANS — instrument-absent print-anchor surface

- **SV-SPE-FR-174:** The system shall ship COTRANS ONLY as a
  print-anchored config surface: the $0.10/galón value exists in the
  corpus solely as the CAT-015 code C8 print (LB-007) wiring a DTE
  tributo line (e-invoicing SV-EINV-FR-017/046 by id), while its
  INSTRUMENT is absent (MOQ-04 half-open; SOQ-39 — 31_'s
  title-vs-content defect left COTRANS uncovered). The row lives in
  the SAME quantity-tax model family as FOVIAL (per-unit `account.tax`
  computing $ × galones, galón UoM), selectable on fuel tax configs
  but VALUE-FLAGGED: the $0.10 carries dated-data provenance = the
  CAT-015 v1.1 2026-07 print (never an instrument value), and NO
  hecho-generador scope, chain mechanics, IVA-base status, document
  rule or ISR treatment is invented beyond that anchor — the surface
  activates its dated instrument rows upon acquisition (config slots,
  zero shipped mechanics; OQ-2).
  (LB-007; EVID-274; SOQ-39; MOQ-04)

### 3.5 Reporting feeds and the design-pass pointer

- **SV-SPE-FR-175:** The system shall feed — and only feed — the
  fiscal-reporting fuel surfaces from this file's data: fuel-line
  quantities (galones), grades and D1 tributo amounts flow to the
  F-07 fuel annexes 13-14 consumed from fiscal-reporting BY ID
  (SV-FREP-FR-124..126 Anexo 13 tasas diferenciadas;
  SV-FREP-FR-127..129 Anexo 14 price-cap detail — their consumption
  contracts, never restated); the F-07 casilla-525 FOVIAL credit
  interplay stays OPEN with the taxation waves (fiscal-reporting/01
  SV-FREP-FR-020 consumes it as an input only, + its §7 OQ-003 and
  05 §7 OQ-003 pointers — 31_ prints NO declaration or credit
  mechanics, so this file invents zero computation); and the mapping
  of the 2001 B2B control-account chain onto DTE-embedded tributos
  (D1 lines across FE/CCF chains) is recorded as the IVA-CORE WAVE
  DESIGN-PASS POINTER (SOQ-40) — this file delivers the accounting
  surfaces the guide prints (FR-170..172) and no chain FR beyond
  them.
  (LB-004; LB-005; EVID-274; SOQ-40)

## 4. Data Model

Layer semantics: the quantity-tax config, control-account wiring and
chain-role/classification config are Odoo-native (core `account.*`/
`product.*` models + dated config rows); the DTE tributo surface is
e-invoicing's by id; the F-07 feeds are fiscal-reporting's by id. No
printed data table in this file warrants a CSV sidecar (a single
dated value row per contribution + two CAT-015 codes — the codes
already live in `catalogs/CAT-015_tributos.csv`, consumed by id,
never duplicated; default none per plan).

**Quantity-tax family (account.tax + product scope):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.tax | amount_type | select | `fixed` (per-unit: unit amount × quantity; Odoo 17-20) — the quantity-based mode, never percentage | FR-167, FR-174 |
| account.tax | unit_amount (dated) · valid_from · instrument_provenance | monetary · date · char | FOVIAL $0.20/galón — provenance "D.L. 208-2000 Art. 26 as reformed D.L. 597-2001, as printed by 31_ (2001)"; COTRANS $0.10/galón — provenance "CAT-015 v1.1 2026-07 print (instrument absent)" + value_flag | FR-167, FR-174 |
| account.tax | l10n_sv_tributo_code · legal_nature | char · char | D1 (FOVIAL) · C8 (COTRANS) — codes consumed from `catalogs/CAT-015_tributos.csv`; contribución especial (CT Art. 15 inc. 1 via 31_) | FR-167, FR-174 |
| account.tax | iva_base_exclusion (invariant) | boolean/computed | contribution never enters any IVA base composition nor adición; validation rejects base contamination | FR-168 |
| product.template | l10n_sv_fovial_scope · uom_id | boolean · m2o uom | true on diesel/gasolinas y mezclas; gasolina de aviación excluded; galón UoM (quantity base) | FR-166, FR-167 |
| res.company / res.partner | l10n_sv_fuel_chain_role | select | importador · refinador · distribuidor · concesionario/gasolinera/detallista · consumidor (contribuyente/final) | FR-166, FR-171 |

**Chain accounting + classification (config):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.account (control) | l10n_sv_fovial_control_role | select | retencion_fovial (first-sale credit/liability) · cuentas_por_cobrar_fovial (intermediate receivable/re-bill) — cuentas de control especiales, separate from VENTAS/IVA | FR-170, FR-171 |
| res.company (consuming) | l10n_sv_fovial_classification | select | costo_combustibles · gasto_operacion · gasto_fabricacion (per-entity election per giro; same for consumidor final) | FR-172 |
| (deduction link) | isr_surface_ref | pointer | taxation/02 SV-TAX-FR-045 by id (Art. 29.6 caused-and-paid surface) — election feeds the deductible cost/expense account | FR-173 |

## 5. Odoo Mapping

Layer semantics for this file: the quantity-tax design, base-exclusion
guard, control-account chain and classification config are Odoo-native
ledger/tax surfaces — every FR maps `odoo`; the architecture-split
surface (DTE generation/transmission carrying the D1/C8 tributo lines)
belongs to e-invoicing by id (SV-EINV-FR-017/046; per
`shared/docs/saas-thin-client-architecture.md` D2, the only split
surface this file touches — as data provider only); the F-07 feeds are
fiscal-reporting exports by id. Model names are stable across Odoo
17/18/19/20 (per-unit `fixed` amount_type included); no
version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-166 | odoo | product.template + res.company/res.partner | l10n_sv_fovial_scope · l10n_sv_fuel_chain_role | scope predicate: fuels minus gasolina de aviación; triggers (a) importador/refinador sale (b) direct import own-consumption |
| FR-167 | odoo | account.tax | amount_type=fixed · unit_amount (dated $0.20) · valid_from/provenance · l10n_sv_tributo_code D1 | D15: resolved as-of transaction date, snapshotted on tax lines; 2001-print provenance (SOQ-39); CAT-015 v1.1 consistency note, not authority; DTE wiring = e-invoicing SV-EINV-FR-017/046 by id |
| FR-168 | odoo | account.tax (invariant) + tax-combination validation | iva_base_exclusion | IVA on price only (Ley IVA 47/48-a/51-d via 31_); never charge/recargar IVA on the contribution; rejects base contamination in any combination |
| FR-169 | odoo | account.move.line (tax line → DTE feed) | separate fila/casilla data | DTE casilla = D1 tributo line (e-invoicing by id); other authorized documents consign separately; CT Art. 116 print rule recorded as provenance |
| FR-170 | odoo | account.account + account.move (first sale) | retencion_fovial control credit | example 2° wiring: CLIENTES 2,460 / IVA débito 260 / RETENCIÓN FOVIAL 200 / VENTAS 2,000; separate from venta/IVA values |
| FR-171 | odoo | account.account + account.move (chain) | cuentas_por_cobrar_fovial debit-at-purchase / credit-at-re-bill | $0.20×gal re-billed through every intermediate to the final consumer; balance monitors chain position; examples 3°-6° |
| FR-172 | odoo | res.company (consuming) + account.move | l10n_sv_fovial_classification election | costo de combustibles / gasto de operación / gasto de fabricación; example 7°: inventory $4,200 including contribution, IVA crédito on price only |
| FR-173 | odoo | (link) res.company → account.account | isr_surface_ref | taxation/02 SV-TAX-FR-045 by id (Art. 29.6 caused-and-paid); election feeds the deductible account; never restated |
| FR-174 | odoo | account.tax (COTRANS row) | unit_amount $0.10 value_flag + CAT-015 C8 | instrument absent (SOQ-39/MOQ-04 half-open); dated rows on acquisition; zero mechanics beyond the print anchor (OQ-2) |
| FR-175 | odoo | (feed) fuel-line data exports | galones/grade/D1 amounts | F-07 annexes 13-14 = SV-FREP-FR-124..129 by id; casilla-525 interplay open (fiscal-reporting/01 FR-020 + OQ-003 kin); B2B-chain-vs-DTE mapping = SOQ-40 IVA-core pointer |

Version-regime notes (D12/D15/D16/D18/D19): the $0.20/$0.10 values
are DATED rows with instrument provenance resolved as-of the
transaction date and snapshotted on the record (D15) — never global
constants; the 2001-print vintage watch rides §2 (SOQ-30 adapted,
SOQ-39 — a post-597-2001 reform or value change lands as a new dated
row after instrument verification, never a silent edit). Mid-year
go-live (D18): a migrating fuel company's chain history ingests as
`is_historical` rows with original-period semantics (original dated
value rows govern historical lines); cut-over (D19): open
CUENTAS-POR-COBRAR-FOVIAL balances and RETENCIÓN FOVIAL liabilities
post through configurable control accounts with XML-ID defaults, GL-
neutral for closed items. No hard gates beyond the IVA-base exclusion
invariant (D16 no-override: the guard is never switched off by
configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a distributor selling 1,000 gal to a service
  station (price $3,000.00), when the invoice posts, then the entry
  books CLIENTES $3,590.00 against IVA DÉBITO FISCAL $390.00 +
  CUENTAS POR COBRAR FOVIAL $200.00 (the re-bill) + VENTAS $3,000.00
  — and the $200.00 purchase-side receivable from its own supplier
  nets the re-bill to zero (ledger examples 3°/4°).
- **AC-002:** Given an FE fuel line of 1,000 gal at $2.00/gal, when
  the DTE is assembled, then the D1 tributo line carries $200.00
  separate from the $2,000.00 price and the $260.00 IVA — with IVA
  computed on the price only (13% × $2,000, never 13% × $2,200), the
  exclusion guard rejecting any base-contaminated computation.
- **AC-003:** Given a manufacturing contribuyente directly importing
  500 gal for own consumption, when the import lands, then the
  quantity tax computes $100.00 (500 × the dated $0.20 row, snapshot
  provenance stamped) and the classification election routes it to
  the manufacturing-expense account feeding the SV-TAX-FR-045
  deduction surface by id.
- **AC-004:** Given a fuel tax config screen, when COTRANS is
  selected, then the row is creatable in the same per-unit family but
  its $0.10 value shows the catalog-print provenance flag
  (CAT-015 v1.1 2026-07) with the instrument OQ marker — and no
  hecho-generador scope, chain or IVA-base fields ship for it.
- **AC-005:** Given a refiner's first-tier sale of 1,000 gal at
  $2.00/gal to a distributor, when the invoice posts, then the entry
  books the RETENCIÓN FOVIAL credit $200.00 separate from VENTAS
  $2,000.00 and IVA DÉBITO $260.00 (ledger example 2°), the
  contribution entering the chain at this sale.
- **AC-006:** Given a consuming contribuyente (election: fuel cost)
  purchasing 1,000 gal at $4.00/gal from a service station, when the
  bill posts, then the inventory/cost line books $4,200.00 INCLUDING
  the $200.00 contribution with IVA CRÉDITO FISCAL $520.00 on the
  price only (ledger example 7°), and the same election semantics
  apply to a consumidor final.

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-39 carried: the Ley del Fondo de Conservación Vial (D.L. 208-2000 text + post-597-2001 reforms) is NOT in corpus — FR-167's $0.20 cites the 31_ 2001 guide print as its provenance chain (secondary authority printing the law); CAT-015 v1.1 prints $0.20 consistently as of 2026-07 but the catalog is not the authority. Current per-gallon value and any reform chain unverified until the instrument lands. Acquisition candidate (31_ file OQ-1 kin). | no | Takumi S7 (sources watch) | open |
| OQ-2 | SOQ-39 carried (COTRANS half; MOQ-04 half-open): the COTRANS instrument is NOT in corpus — the 31_ file title promised it, the content lacks it (title-vs-content defect); the only corpus anchors are the CAT-015 C8 print ($0.10/galón, LB-007) + e-invoicing's DTE wiring (SV-EINV-FR-017/046 by id). FR-174 ships the value-flagged config surface with zero mechanics; dated rows land upon acquisition. Acquisition candidate (31_ file OQ-2 kin). | no | Takumi S7 (sources watch) | open |
| OQ-3 | SOQ-40 carried: the B2B recovery chain (the 2001 control-account mechanics of FR-170..171) predates e-invoicing — mapping the $0.20×gal recovery onto D1-tributo lines across FE/CCF chains is a DESIGN PASS in the IVA-core taxation wave; this file records the pointer plus the accounting surfaces the guide prints, no chain FR beyond them. Kin: the F-07 casilla-525 FOVIAL credit interplay (fiscal-reporting/01 §7 OQ-003 + 05 §7 OQ-003) — 31_ prints no declaration/credit mechanics, so FR-175 feeds data only and invents zero computation (31_ file OQ-3 kin). | no | Takumi IVA-core wave (design pass) | open |
| OQ-4 | SOQ-30 adapted: the vintage risk of this file is the 2001 guide + the 2000/2001 law chain (D.L. 208-2000 as reformed D.L. 597-2001) — the oldest vintage of the S7 wave; post-2001 reforms, the current per-gallon value and the guide's own currency are unverified until official routes recover (SOQ-22 kin). Every LB cites as printed; re-verify before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-5 | MOQ-04 linkage note (master index Section C): MOQ-04 asked (i) the FOVIAL/COTRANS legal basis (laws absent, only guide 31_), (ii) whether they are in the IVA base (Art. 51-d tension), (iii) FEXE usage requiring AT authorization. State after S7: (i) FOVIAL half RESOLVED-BY-CHAIN — instrument chain = D.L. 208-2000 Art. 26 as reformed D.L. 597-2001, cited via 31_ (law text still absent, OQ-1); COTRANS half OPEN (OQ-2); (ii) RESOLVED for FOVIAL by 31_ §IV.1 — NOT base imponible nor adición (Ley IVA Arts. 47/48-a/51-d), FR-168's guard; unstated for COTRANS (no instrument — no invention); (iii) owned by e-invoicing SV-EINV-FR-046 by id. The master-index MOQ row closes when the index task rolls this up. | no | Takumi S7 + T9 index rollup | open (linkage recorded) |
