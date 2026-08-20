# HN — E-Invoicing — Document mechanics: print contract, sales documents & complements

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN2 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines WHAT each Honduran fiscal document must contain and HOW
each document type is used under the CAI paper regime of the *Reglamento
del Régimen de Facturación, Otros Documentos Fiscales y Registro Fiscal de
Imprentas* (Acuerdo 481-2017, consolidated). Clusters: (E4) the print
contract — the two-layer doctrine separating pre-printed FORMAT data (CAI,
*fecha límite*, *rango autorizado*, exonerado block, imprenta
identification) from EMISSION-TIME transaction data, plus conformance
(identical copies, thermal paper, sustento exclusivity, buyer verification
duty, the 01-mar-2019 grace boundary); (E5) sales-document mechanics —
*factura* field set, export *tasa cero* + reduced literals, the zona-libre
document matrix, *factura prevalorada*, *ticket*, *recibo por honorarios
profesionales* (RHP, professional-fees receipt), the L50 consumer-final
end-of-day consolidation, gratuito operations; (E6) complement and
buyer/donee-issued documents — *boleta de compra* (purchase slip),
*constancia de donación* (donation certificate), NC/ND origin-triple,
*guías de remisión* (remission guides), *comprobante de retención*
(retention voucher).

It does **not** cover: document taxonomy, type codes and correlativo grammar
(`01_document-types-numbering.md`, HN-EINV-FR-001..045); the CAI/rango
ledger, the authorization procedure and the emission gate including
*momento de emisión* (`02_cai-ledger-emission-gate.md`, HN-EINV-FR-046..090);
inscription, topologies, printing means, SFC specs, SEE/CAEE and the
contingency/mandate rows (`04_registration-topologies-medios-see.md`,
HN-EINV-FR-141..175); retention RATES (cited by id from
`../taxation/04_isr-withholding.md`, HN-TAX-FR-137..148 zone — never
restated here); and DJIMR retention reporting (future S-HN3
fiscal-reporting wave, W2 cluster F2). D-H2 binds throughout: dated
thresholds resolve as-of the emission date with snapshot-on-write, and
emission-time content is validated against the regime rows in force at that
date.

## 2. Legal Basis

Authority order (master index Section A): `24_` (Acuerdo 481-2017
consolidado, effective 31-dic-2017; reform chain 609-2017 / 725-2018 /
817-2018) is the current authority for everything below. `26_` (817-2018)
Art. 1 corroborates the Art. 76-A grace boundary verbatim (cross-check PASS,
R-H40). Helps 76_-78_ are operational-only and their Base-Legal sections are
DEFECTIVE — the reglamento articles are cited instead (R-H37 binding).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglamento 481-2017, Art. 9: "Están obligados a expedir Comprobantes Fiscales, los Obligados Tributarios que transfieran bienes y/o presten servicios de cualquier naturaleza. … Esta obligación rige aun cuando la transferencia de bienes y/o prestación de servicios no se encuentre gravada con tributos o se realice a título gratuito." | Art. 9: taxpayers transferring goods and/or rendering services of any nature must issue Comprobantes Fiscales; the duty applies even when the operation is untaxed or gratuitous (incl. the L50 consumer-final exception). | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 9 (p.15); EV24:EVID-189 |
| LB-002 | Art. 10 (formato de la Factura): "2. Denominación del documento: 'Factura'; 3. Clave de Autorización de Impresión (CAI), otorgada por la Administración Tributaria; 4. Fecha límite de emisión, vigente; 5. Rango autorizado, vigente; 6. Destino de los ejemplares … 8. Datos del Adquirente exonerado: a) Número correlativo de la Orden de Compra Exenta; b) Número correlativo de la Constancia del Registro de Exonerados; c) Número identificativo del Registro de la Secretaría de Estado en el Despacho de Agricultura y Ganadería. 9. Datos de la imprenta, para las Facturas preimpresas … 10. Descuentos y rebajas otorgados." | Art. 10: factura FORMAT (pre-printed) layer — document denomination, CAI, valid emission deadline, valid authorized range, copy destination, exonerated-acquirer data (3 registers), imprenta data, discounts block. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 10 (pp.15-17); EV24:EVID-190 |
| LB-003 | Art. 11 (requisitos al momento de la emisión): "… g) Discriminación de los valores exentos, exonerados y de los gravados con alícuota cero, cuando corresponda; h) Subtotales sujetos a los impuestos discriminados por tarifa o alícuota; i) Discriminación de los impuestos por tarifa o alícuota … k) Importe total en números y letras … cuando el Obligado Tributario emita facturas con otra denominación monetaria, debe indicar la tasa de cambio vigente a la fecha de emisión. Cuando la venta … al Consumidor Final y excediera la suma de diez mil Lempiras (L10,000.00), debe consignarse obligatoriamente los datos del cliente, indicando nombres y apellidos, el tipo y número de documento de identificación en el espacio del RTN. El monto señalado … podrá ser modificado por la Secretaría de Estado en el Despacho de Finanzas mediante Acuerdo de Carácter General. … Para respaldar el crédito fiscal en los casos que la factura sustente ventas exentas y gravadas, se reconocerán únicamente las ventas gravadas." | Art. 11: emission-time requirements — tax discrimination by rate, totals in numbers and words, FX rate for non-Lempira invoices, mandatory consumer-final identification above L10,000 (SEFIN-modifiable), gravadas-only credit on mixed exempt/taxed invoices. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 11 (pp.18-20); EV24:EVID-190 |
| LB-004 | Arts. 12-13: "En caso de exportaciones con mercancías gravadas … los Obligados Tributarios deben extender la Factura con tasa cero. … Las ventas que se realicen entre zonas libres legalmente autorizadas se deben documentar únicamente con factura sin el cobro del Impuesto Sobre Ventas ni orden de compra exenta." | Arts. 12-13: zero-rate export invoicing; fomento-regime consolidated vs labor-only value; the zona-libre document matrix (oficio+guía / factura+guía / DUA+factura / labor-only / inter-ZL factura without ISV or exempt purchase order); transporter and sample rules; reduced Art. 11.1 literal set for export invoices. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 12-13 (pp.20-21); EV24:EVID-192 |
| LB-005 | Art. 16: "La Factura Prevalorada se utiliza únicamente en transacciones a consumidores finales. … deberá solicitar la cantidad específica de Facturas Prevaloradas que pretende utilizar por cada una de las ferias, eventos o espectáculos públicos … deberá notificar a la Administración Tributaria con una antelación no menor de diez (10) días hábiles antes de la fecha de realización de la feria, evento espectáculo público, debiendo indicar el rango autorizado de Factura Prevalorada que utilizará." | Art. 16 (with Art. 15): prevalorada is consumer-final-only, imprenta-printed with pre-printed values, requested per event in exact quantity, with ≥10 business-day advance notice to SAR naming the authorized range. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 15-16 (pp.22-24); EV24:EVID-193 |
| LB-006 | Art. 17: "El Ticket debe ser emitido en original y la copia en cinta de auditoría: a) Original: Cliente. b) Copia: Obligado tributario emisor. … las cintas de auditoría deben archivarse por cada una de las máquinas registradoras. Las rectificaciones, anulaciones o cancelaciones de operaciones realizadas, deben ser sustentadas con los respectivos Tickets originales." | Art. 17: ticket emitted by cash register with the audit tape as the emitter's copy; tapes archived per machine; corrections/voids/cancellations sustained by the original tickets. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 17 (pp.24-25); EV24:EVID-194 |
| LB-007 | Art. 19: "4. Monto de los honorarios brutos percibidos; 5. Monto de la retención en su caso; 6. Monto neto recibido; 7. Fecha de emisión." | Arts. 18-19: professional-fees receipt emission fields including the gross/withholding/net triple. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 18-19 (pp.26-28); EV24:EVID-195 |
| LB-008 | Art. 22: "La boleta de compra debe ser utilizada única y exclusivamente para respaldar los costos y gastos … por las compras de bienes y/o prestación de servicios de mano de obra no calificada, y no podrá ser utilizada para respaldar crédito fiscal del Impuesto Sobre Ventas. El monto total de las transacciones … no podrán exceder del cinco por ciento (5%) del total de gastos operativos deducibles de la Renta Bruta Gravable, excluyendo los gastos financieros. … cuando no exceda del monto que constituye la base exenta del Impuesto Sobre la Renta en un mismo período fiscal. En caso de exceder … el proveedor debe emitir factura." Destino (Art. 20.6): "a) Original: Contribuyente Adquirente; y, Copia: Proveedor." | Arts. 20-22: purchase slip buyer-issued for unskilled labor; cost/gasto support only, never ISV credit; aggregate 5%-of-deductible-opex (ex-financial) cap; per-provider per-FY ISR-exempt-base cap beyond which the provider must invoice; reversed copy custody. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 20-22 (pp.28-31); EV24:EVID-196 |
| LB-009 | Arts. 23-24: "5. Firma y sello del Representante Legal del Beneficiario; 6. Firma y sello del Donante." Destino: "a) Original: Donante; y, b) Copia: Beneficiario." | Arts. 23-24: donation certificate issued by the beneficiary (donee) with donor identification block and dual signatures; original goes to the donor. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 23-24 (pp.31-33); EV24:EVID-197 |
| LB-010 | Art. 26: "3. Datos del Comprobante Fiscal que da lugar a la Nota de Crédito: a) Clave de Autorización de Impresión (CAI); b) Número correlativo del Comprobante Fiscal al que le está aplicando la Nota Crédito; c) Fecha de emisión del Comprobante Fiscal … 4. Motivo de la emisión del documento. 5. Importe total literal y numeral … 10. Unidades del bien vendido o servicio prestado." | Arts. 25-28: credit/debit notes must carry the origin triple (origin CAI + correlativo + emission date) and the issuance motive, with tax discrimination by rate, national-currency denomination and units. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 25-28 (pp.33-38); EV24:EVID-198 |
| LB-011 | Art. 30: "10. Motivo de traslado: a) Venta; b) Consignación; c) Exportación; d) Compra; e) Devolución; f) Traslado entre establecimientos del mismo Obligado Tributario; g) Traslado de bienes para transformación; h) Traslado de bienes para reparación; i) Traslado por venta emisor móvil; j) Exhibición o demostración; k) Participación en ferias; l) Otros … 11. Tipo, número de autorización, numeración y fecha de emisión del Documento Complementario o documento de importación, cuando el motivo … sea … a), c), d), e) y f)." Art. 29.7: "copia 2: Debe ser entregada en los controles que realice la Administración Tributaria." Art. 31: "podrá ser emitida por el vendedor, el comprador, el transportista o el poseedor de la mercancía al inicio del traslado." Art. 32: "La Guía de Remisión acredita la legítima tenencia … debe ser emitida en forma previa al traslado." | Arts. 29-32: remission-guide field set, 12-item transfer-motive catalog, origin-document reference for motives a/c/d/e/f, 3-copy distribution incl. the SAR control copy, four possible emitters, pre-transfer emission, legitimate-possession function, invoice-substitution rule. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 29-32 (pp.38-43); EV24:EVID-199 |
| LB-012 | Art. 35: "El Comprobante de Retención debe extenderse al momento que se origine el hecho generador o la respectiva transacción comercial. Al momento de la emisión … pueden figurar varias retenciones … En el caso de los Operadores y Concesionarios de Servicios de Tarjetas de Crédito y Débito (OTCD), deben emitir el Comprobante de Retención al final de cada mes y entregarlo dentro de los primeros diez (10) días hábiles del mes siguiente … Los patronos no están obligados a extender Comprobantes de Retención a sus trabajadores permanentes, salvo en los casos que el trabajador solicite dicho comprobante." | Arts. 33-35: retention voucher issued at the triggering event, consolidable, individually closed and page-numbered; OTCD monthly variant with 10-business-day delivery; employers exempt for permanent workers unless requested. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 33-35 (pp.44-47); EV24:EVID-200 |
| LB-013 | Art. 37: "se consideran válidos únicamente los Documentos Fiscales que correspondan, siempre que contengan los requisitos señalados en presente Reglamento." Art. 38: thermal paper requires provider certification of "garantía de la impresión … por un plazo no menor de 5 años" plus sales summaries; "la información contenida en las copias debe ser idéntica a la descrita en la original." Art. 39: "Los Obligados Tributarios serán responsables de comprobar la validez de los Comprobantes Fiscales y Documentos Complementarios que sustentan crédito fiscal … y costos o gastos." Art. 36: "Sistema de seguridad electrónica (código de barras, QR entre otros); 2. Logotipos, eslogan, sitio web…" | Arts. 36-39: exclusivity of conforming documents as credit/cost support; thermal-paper 5-year warranty + sales-summary duties with loss of deduction/credit on breach; identical copies; buyer's verification duty; optional QR/barcodes/logos. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 36-39 (pp.47-49); EV24:EVID-201 |
| LB-014 | Art. 76-A: "… hasta el 28 de febrero de 2019 … serán documentos válidos … A partir del 01 de marzo de 2019, todos los obligados tributarios … únicamente deben emitir documentos fiscales que cumplan con todos los requisitos." Art. 76: "… el uso de la Boleta de Venta se deben entender que el Documento Fiscal a emitir es la Factura." | Arts. 76 / 76-A: grace boundary — invoices/slips/prevaloradas emitted through 28-feb-2019 are valid without the exonerado-data and discounts requirements; full requirements enforced from 01-mar-2019; Boleta-de-Venta references in legacy instruments remap to Factura. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 76, 76-A (pp.65-67); EV24:EVID-207 |
| LB-015 | Acuerdo 817-2018, Art. 1 (reforms 76-A): "A partir del 01 de marzo de 2019 … todos los requisitos" (replacement text matches the 24_ consolidated text verbatim — cross-check PASS, R-H40). | 817-2018 Art. 1 extends and fixes the 76-A grace boundary; gazette-original corroboration of the consolidated text. | `hn/sources/26_Acuerdo_817-2018_tercera_reforma.pdf` | Art. 1 (p.16); EV24:EVID-211 |
| LB-016 | Art. 46: "En el caso de las Facturas Prevaloradas y Recibo por Honorarios Profesionales, deben ser exclusivamente emitidos bajo la modalidad de imprenta." Art. 47: autoimpresor inscription "a excepción de las Facturas Prevaloradas, Recibos por Honorarios Profesionales y Constancias de Donación." | Arts. 46-47: modality exclusions — prevalorada and RHP are imprenta-only; constancia de donación excluded from the autoimpresor modality (imprenta-only by elimination; no electronic emission path in the current text). | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Arts. 46-47 (pp.51-54); EV24:EVID-203 |
| LB-017 | Art. 4 num. 32 (Nota de Crédito): "anular operaciones, aceptar devoluciones y conceder descuentos efectuados con posterioridad a la emisión." (Defs. 5 BASE desprendible, 13 constancia emisors, 43 ticket consumer-final-exclusive, cited by number.) | Art. 4 definitions feeding this file: NC statutory purposes; detachable base copy; the closed list of constancia emisors; ticket's consumer-final exclusivity. | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 4 (pp.6-12); EV24:EVID-198, EVID-193, EVID-197, EVID-194 |

## 3. Functional Requirements

Document types, type codes and correlativo grammar are owned by
`01_document-types-numbering.md` (HN-EINV-FR-001..045) and referenced here by
name. The CAI / *fecha límite* / *rango autorizado* values printed by FR-093
are consumed from the ledger of `02_cai-ledger-emission-gate.md`
(HN-EINV-FR-046..090); this file owns only their print placement. Which
modality/device may emit each document is registered per
`04_registration-topologies-medios-see.md` (HN-EINV-FR-141..175); the guards
below only enforce the document-side consequences.

### 3.1 Print contract — two layers & conformance (cluster E4)

- **HN-EINV-FR-091:** The system shall model every Comprobante Fiscal / Documento Complementario
layout in two separated layers: a FORMAT layer (pre-printed/fixed data: emisor identity,
denominación, CAI, fecha límite, rango autorizado, exonerado block, imprenta data, descuentos
block) and an EMISSION-TIME layer (transaction data); format-layer data never derives from, nor
varies with, individual transactions. (LB-002, LB-003; EV24:EVID-190)
- **HN-EINV-FR-092:** The factura FORMAT layer shall print the emisor identity block: RTN,
nombres/apellidos or razón/denominación social, *nombre comercial* (trade name), dirección of the
casa matriz and the emitting establecimiento, teléfono and correo as declared in the *contrato de
adhesión* (adhesion contract). (LB-002; EV24:EVID-190)
- **HN-EINV-FR-093:** The factura FORMAT layer shall print the authorization quad — denominación
del documento ("Factura"), CAI granted by SAR, *fecha límite de emisión* and *rango autorizado* in
force — the three dynamic values read from the active CAI ledger entry
(`02_cai-ledger-emission-gate.md`). (LB-002; EV24:EVID-190)
- **HN-EINV-FR-094:** The factura FORMAT layer shall print the copy destination block: Original →
Cliente; Copia → Obligado Tributario emisor. (LB-002; EV24:EVID-190)
- **HN-EINV-FR-095:** The factura FORMAT layer shall include the exonerado block for exonerated
acquirers with the three register identifiers: (a) correlativo of the *Orden de Compra Exenta*
(OCE, exempt purchase order); (b) correlativo of the *Constancia del Registro de Exonerados* (CRE,
exoneration-registry certificate); (c) number of the *Registro de la Secretaría de Estado en el
Despacho de Agricultura y Ganadería* (SAG agro-registry) — populated from partner register data
(applicability → OQ-007). (LB-002; EV24:EVID-190)
- **HN-EINV-FR-096:** For imprenta-printed facturas the FORMAT layer shall print the *Datos de la
imprenta* (certified printer's Registro Fiscal de Imprentas data) from the imprenta partner
recorded at authorization — cite the reglamento, never the Ayudas' Base-Legal sections (R-H37).
(LB-002; EV24:EVID-190, EV24:78_ OQ-1)
- **HN-EINV-FR-097:** The factura FORMAT layer shall include the *Descuentos y rebajas otorgados*
block (discounts and allowances granted; numeral added by reforma 725-2018, enforced from
01-mar-2019 per FR-109). (LB-002, LB-014; EV24:EVID-190, EVID-207)
- **HN-EINV-FR-098:** The factura EMISSION-TIME layer shall capture/print the adquirente field set
for credit-supporting sales: client identification (nombres y apellidos / razón o denominación
social) with RTN, fecha de emisión, per-line descripción, cantidad and valor unitario (Art. 11.1
literals a)–f); literal-to-field map for a)–f)/j) → OQ-003. (LB-003; EV24:EVID-190)
- **HN-EINV-FR-099:** The factura EMISSION-TIME layer shall discriminate: exempt, exonerated and
zero-rate (*alícuota cero*) values; subtotals by *tarifa o alícuota* (rate); each tax amount by
rate; the total importe in numbers and words; discounts and allowances granted. (LB-003;
EV24:EVID-190)
- **HN-EINV-FR-100:** For consumer-final sales whose total EXCEEDS the identification threshold,
the system shall require client data — nombres y apellidos plus tipo y número de documento de
identificación in the RTN field space; at or below it, no identification is required. Dated
parameter row: L10,000.00, valid_from 31-dic-2017 (481-2017), SEFIN-modifiable by Acuerdo de
Carácter General (no modifying instrument in corpus → OQ-001); resolved value + exceeded flag
snapshotted on the move at write (D-H2/D15). (LB-003; EV24:EVID-190; 24_ OQ-5)
- **HN-EINV-FR-101:** When a factura is issued in a monetary denomination other than the Lempira,
the system shall print the exchange rate (*tasa de cambio*) in force at the emission date.
(LB-003; EV24:EVID-190)
- **HN-EINV-FR-102:** On mixed facturas supporting both exempt and taxed sales, the system shall
recognize only the taxed (*gravadas*) sales for *crédito fiscal* (ISV input credit) support;
computation and pro-rata discipline are owned by the taxation files (cited by id, not restated).
(LB-003; EV24:EVID-190)
- **HN-EINV-FR-103:** The information printed on the copia (and any electronic copy) shall be
identical, field by field, to the original. (LB-013; EV24:EVID-201)
- **HN-EINV-FR-104:** Electronic security systems (barcode, QR, others) and logos/slogan/web site
shall be treated as OPTIONAL layout elements; no conformance validation shall ever require a QR or
barcode on a document. (LB-013; EV24:EVID-201)
- **HN-EINV-FR-105:** Thermal-paper documents shall be backed by a provider certification of print
durability ≥ 5 years presented to SAR before use; the system shall record it (vendor, warranty,
date) and block thermal-layout emission without it. (LB-013; EV24:EVID-201)
- **HN-EINV-FR-106:** Thermal-paper emitters shall be able to produce the *resúmenes de ventas*
(sales summaries) in the deadlines, media and forms SAR determines (instrument absent → OQ-004);
documents failing the thermal regime lose deductible-cost and crédito-fiscal support. (LB-013;
EV24:EVID-201)
- **HN-EINV-FR-107:** Only Documentos Fiscales carrying all reglamento requirements of their type
shall be accepted as support for crédito fiscal, ISR cost/gasto or other tax-credit purposes;
non-conforming supplier documents are flagged non-supporting. (LB-013; EV24:EVID-201)
- **HN-EINV-FR-108:** The system shall expose a buyer-side verification hook: validity of a
Comprobante Fiscal / Documento Complementario can be checked against SAR's means (Oficina Virtual
"Verificador") before relying on it for credit/cost — an operational (manual/voluntary) surface,
logged as a verification attempt on the supplier document. (LB-013; EV24:EVID-201)
- **HN-EINV-FR-109:** Document conformance shall be resolved by emission date against the regime
rows: 189-2014 regime (pre-31-dic-2017; grammar per the 01 file); 481-2017 phased enforcement —
facturas, boletas de compra and facturas prevaloradas through 28-feb-2019 are valid WITHOUT the
exonerado-data and descuentos requirements; from 01-mar-2019 all requirements apply; legacy
*Boleta de Venta* references remap to Factura. (LB-014, LB-015; EV24:EVID-207, EVID-211)

### 3.2 Sales-document mechanics (cluster E5)

- **HN-EINV-FR-110:** The system shall require a Comprobante Fiscal for every operation in which
the Obligado Tributario transfers goods and/or renders services of any nature. (LB-001;
EV24:EVID-189)
- **HN-EINV-FR-111:** The emission duty applies even when the operation is not subject to any tax
or is performed *a título gratuito* (free of charge); gratuitous operations (samples, gifts) are
documented on the corresponding fiscal document. (LB-001; EV24:EVID-189)
- **HN-EINV-FR-112:** For consumer-final operations whose total does not exceed L50.00, the system
may skip the per-transaction document unless the acquirer requires one, consolidating all such
sales of the day onto the authorized Comprobante Fiscal / Documento Complementario at end of day
(imprenta modality pattern). (LB-001; EV24:EVID-189)
- **HN-EINV-FR-113:** The L50 exception shall be DISABLED for Obligados Tributarios subscribed in
the *autoimpresores de máquinas registradoras y sistemas computarizados* modalities — every sale
documented per transaction (ticket/factura); modality subscription data from the registration file
(`04_registration-topologies-medios-see.md`). (LB-001; EV24:EVID-189)
- **HN-EINV-FR-114:** Exports of taxed goods shall be invoiced with the *Factura con tasa cero*
(zero-rate invoice; 0% ISV treatment per the taxation files, cited by id). (LB-004; EV24:EVID-192)
- **HN-EINV-FR-115:** For *regímenes de fomento a las exportaciones* (export-promotion regimes):
exporter supplies BOTH materials and labor → one factura consolidating both values; ONLY labor →
the factura consigns the labor value only. (LB-004; EV24:EVID-192)
- **HN-EINV-FR-116:** Export facturas (Art. 12 context) carry only the reduced requirement set —
Art. 11.1 literals a), b), c), d), j), k) — literal b) (RTN) required only for
*nacionalizaciones*; literal map per OQ-003. (LB-004, LB-003; EV24:EVID-192)
- **HN-EINV-FR-117:** Zona-libre operations shall follow the statutory matrix: (1) transfers
without tradición by free-of-charge service companies → *Declaración de Oficio* + guía de
remisión; (2) transformation with cost → factura per FR-114/FR-115 + guía for the return of goods;
(3) tradición with DUA → DUA + factura; (4) client-supplied materials → factura consigning ONLY
the mano de obra (labor) value. (LB-004; EV24:EVID-192)
- **HN-EINV-FR-118:** Sales between legally authorized zonas libres are documented exclusively
with factura, WITHOUT ISV charge and WITHOUT *orden de compra exenta* — the system suppresses both
the ISV lines and the exonerado block for inter-ZL sales. (LB-004; EV24:EVID-192)
- **HN-EINV-FR-119:** Within zonas libres: the transportista's transport service is invoiced with
a zero-rate factura; samples (*muestras*) move under guía de remisión (or the customs document
when destined abroad). (LB-004; EV24:EVID-192)
- **HN-EINV-FR-120:** The *Factura Prevalorada* (pre-valued invoice, type 10) shall be emitted
ONLY for consumer-final transactions and ONLY under the imprenta modality (the certified imprenta
requests the authorization in the taxpayer's name); emission is blocked for identified
(non-consumer-final) acquirers and non-imprenta modalities. (LB-005, LB-016; EV24:EVID-193,
EVID-203)
- **HN-EINV-FR-121:** Prevalorada authorization is event-driven: the taxpayer requests through the
imprenta the SPECIFIC quantity per feria/evento/espectáculo público, the total requested quantity
is printed, and SAR is notified ≥10 días hábiles before the event declaring the rango to be used;
the system tracks the event record and warns/blocks emission outside a noticed event window.
(LB-005; EV24:EVID-193)
- **HN-EINV-FR-122:** Prevalorada format carries pre-printed fixed values (mass-consumption goods
at ferias/espectáculos) with no buyer identification, plus a *base desprendible* (detachable stub)
with the same information as the original. (LB-005, LB-013, LB-017; EV24:EVID-193, EVID-201)
- **HN-EINV-FR-123:** The *Ticket* (catalog code 03 / machine prefix 09 — dual code per the 01
file, R-H41) is emitted exclusively by *máquina registradora* per registered device: original to
the client, copia embodied in the *cinta de auditoría* (audit tape); tapes (including
voided/corrected operations) archived per machine. (LB-006; EV24:EVID-194)
- **HN-EINV-FR-124:** Rectifications, anulaciones and cancellations of ticket operations are
sustained by the respective original tickets; the correction flow references the origin ticket(s).
(LB-006; EV24:EVID-194)
- **HN-EINV-FR-125:** The *Recibo por Honorarios Profesionales* (RHP, type 04; imprenta-exclusive
per LB-016) shall print: adquirente RTN *cuando corresponda* (→ OQ-006), adquirente name, detailed
service description, fecha de emisión, and the bruto/retención/neto triple — *honorarios brutos
percibidos*, *monto de la retención* (from the taxation retention engine,
`../taxation/04_isr-withholding.md` HN-TAX-FR-137..148 zone — never restated here), *monto neto
recibido*; DJIMR reporting = S-HN3 surface. (LB-007, LB-016; EV24:EVID-195, EVID-203)

### 3.3 Complement & buyer/donee-issued documents (cluster E6)

Retention comprobantes are themselves CAI-authorized documents (ledger in
`02_cai-ledger-emission-gate.md`; corroborated EV31:EVID-115/118/119/122);
this section owns their content and issuance mechanics only.

- **HN-EINV-FR-126:** The *Boleta de Compra* (purchase slip, type 11) is issued by the BUYER,
printing the provider block (nombres y apellidos, RTN OR identity-card number, dirección
domiciliar) plus descripción, cantidad, moneda, importe in words and numbers, and fecha, carrying
the provider's *firma y huella digital* (signature and thumbprint; thumbprint alone if the
provider cannot sign). (LB-008; EV24:EVID-196)
- **HN-EINV-FR-127:** The boleta de compra is usable exclusively to support ISR costs/gastos for
purchases of goods and/or *mano de obra no calificada* (unskilled labor), and NEVER supports ISV
crédito fiscal; boleta lines are excluded from ISV credit computation. (LB-008; EV24:EVID-196)
- **HN-EINV-FR-128:** Boleta-supported transactions in aggregate shall not exceed 5% of total
deductible operating expenses of the *Renta Bruta Gravable*, EXCLUDING *gastos financieros*; the
monitor computes per fiscal year and flags/blocks excess with a reclassification alert. (LB-008;
EV24:EVID-196)
- **HN-EINV-FR-129:** Boletas may support purchases from a natural-person provider only while the
FY accumulated amount does not exceed the ISR *base exenta* for that fiscal year (resolved as-of
FY from the taxation scale dated rows, cited by id — element choice → OQ-005); on exceedance the
system flags that the provider must emit facturas instead. (LB-008; EV24:EVID-196)
- **HN-EINV-FR-130:** Boleta custody is REVERSED vs vendor documents: Original → *Contribuyente
Adquirente* (the issuing buyer); Copia → *Proveedor*. (LB-008; EV24:EVID-196)
- **HN-EINV-FR-131:** The *Constancia de Donación* (type 12) shall be issued by the DONEE,
restricted to the statutory emisor class (State, Municipalidades, legally recognized
educational/fomento-educativo, beneficencia, deportiva/fomento-deportivo institutions — def. 13),
printing the donante block (RTN, name, address, phone), descripción, valor, fecha and BOTH
signature-and-seal blocks (beneficiary's legal representative + donor); custody: Original →
Donante, Copia → Beneficiario; imprenta-exclusive (Art. 47, LB-016); the donor's original supports
the ISR donation deduction (taxation files by id). (LB-009, LB-016, LB-017; EV24:EVID-197,
EVID-203)
- **HN-EINV-FR-132:** *Notas de Crédito* (06) and *Notas de Débito* (07) carry the mandatory
origin triple of the adjusted Comprobante Fiscal — origin CAI + origin correlativo number + origin
fecha de emisión; posting is blocked when any element is missing, and the origin is validated to
exist in the issued-document ledger. (LB-010; EV24:EVID-198)
- **HN-EINV-FR-133:** NC/ND shall print the *motivo de la emisión*, the importe total in words and
numbers, tax discrimination by *tarifa, alícuota o porcentaje*, the literal national-currency
denomination, the adquirente name + RTN and the units; NC statutory purposes = anular operaciones,
aceptar devoluciones, conceder descuentos post-emisión (def. 32). (LB-010, LB-017; EV24:EVID-198)
- **HN-EINV-FR-134:** The *Guía de Remisión* (remission guide, type 08) shall be emittable by any
of the four statutory emitters (seller, buyer, transportista, or possessor of the goods at the
start of the transfer), emitted BEFORE the transfer (*en forma previa al traslado*), distributed
in three copies (Original → Destinatario; copia 1 → Emisor; copia 2 → handed over at SAR
controls), and shall prove *legítima tenencia*, including warehouse possession (guía that
sustained the transfer OR the corresponding Documento Fiscal). (LB-011; EV24:EVID-199)
- **HN-EINV-FR-135:** The guía carries the transport field set: remitente RTN + name; full
addresses of punto de partida (origin) and destino; destinatario identification; transportista;
conductor; vehicle marca and placa; detailed goods description (annotatable as an anexo);
quantity. (LB-011; EV24:EVID-199)
- **HN-EINV-FR-136:** The guía *motivo de traslado* (transfer motive) shall use the statutory
12-item catalog: a) Venta; b) Consignación; c) Exportación; d) Compra; e) Devolución; f) Traslado
entre establecimientos del mismo Obligado Tributario; g) Traslado para transformación; h) Traslado
para reparación; i) Traslado por venta emisor móvil; j) Exhibición o demostración; k)
Participación en ferias; l) Otros. (LB-011; EV24:EVID-199)
- **HN-EINV-FR-137:** When the motive is a) Venta, c) Exportación, d) Compra, e) Devolución or f)
traslado between establecimientos, the guía additionally references the origin document — tipo,
número de autorización, numeración, fecha de emisión (Comprobante Fiscal / Documento
Complementario or import document). (LB-011; EV24:EVID-199)
- **HN-EINV-FR-138:** Substitution and exceptions: a traslado covered by a comprobante fiscal
carrying partida/destino/fechas/transportista/vehículo/conductor data may run WITHOUT a separate
guía; itinerant (emisor móvil) sellers consign fiscal numbers on the guía after each sale;
export-bound goods move under the customs document or the guía; international transit and *menaje
de casa* (household-goods moves) require NO guía. (LB-011; EV24:EVID-199)
- **HN-EINV-FR-139:** The *Comprobante de Retención* (retention voucher, type 05) shall be issued
to each retained-upon Obligado Tributario AT the moment the hecho generador / commercial
transaction arises; it may consolidate several retentions from distinct transactions (origin
comprobante data CAI/correlativo/fecha *cuando corresponda*; per-transaction detail in the voucher
or an integral anexo); each voucher is totalized and closed individually, with numbered pages for
multi-page computerized emissions. Content: sujeto name + RTN, base imponible, descripción del
tributo retenido, alícuota cuando corresponda, importe total retenido, firma y sello del agente,
fecha de emisión. (LB-012; EV24:EVID-200)
- **HN-EINV-FR-140:** Issuance variants: (a) OTCD — Operadores y Concesionarios de Servicios de
Tarjetas de Crédito y Débito — emit at the end of each month, delivering within the first 10 días
hábiles of the following month; (b) *patronos* (employers) are NOT obligated to issue vouchers to
permanent workers — only on worker request (the payslip carries the withholding otherwise; payroll
crossref W4). (LB-012; EV24:EVID-200)

## 4. Data Model

Entities and fields owned by the sibling files (sequence/CAI ledger,
registration matrix, device registry) are referenced, not redefined.
Machine-readable sidecars (guía motivo catalog, dated-parameter rows) will
be added by the catalogs wave; none are created by this file.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.document.format | document_type_id | m2o l10n_latam.document.type | per 01-file catalog | FR-091 |
| l10n_hn.document.format | cai_id / fecha_limite / rango_label | m2o / date / char | from 02-file ledger | FR-093 |
| l10n_hn.document.format | imprenta_partner_id | m2o res.partner | partner flagged imprenta | FR-096 |
| l10n_hn.document.format | exonerado_block_enabled / descuentos_block_enabled | boolean | grace-boundary aware | FR-095, FR-097, FR-109 |
| l10n_hn.parameter | code = consumer_final_id_threshold | monetary + valid_from/valid_to | 10000.00, valid_from 2017-12-31 (SEFIN-modifiable) | FR-100; OQ-001 |
| res.partner | l10n_hn_oce_no / l10n_hn_cre_no / l10n_hn_sag_no | char | exonerado 3-register block | FR-095 |
| res.partner | l10n_latam_identification_type_id + vat | — | consumer-final ID type + number (RTN space) | FR-100 |
| res.partner | l10n_hn_is_imprenta | boolean | Registro Fiscal de Imprentas member | FR-096 |
| account.move | l10n_hn_threshold_snapshot / l10n_hn_id_required | monetary / boolean | snapshot-on-write (D15) | FR-100 |
| account.move | l10n_hn_fx_rate_print | computed | res.currency.rate at emission date | FR-101 |
| account.move | l10n_hn_amount_in_words | computed text | currency.amount_to_text | FR-099 |
| account.move (NC/ND) | l10n_hn_origin_cai / l10n_hn_origin_number / l10n_hn_origin_date / l10n_hn_motivo | char / char / date / text | origin triple + motive | FR-132, FR-133 |
| account.move (RHP type 04) | honorarios_brutos / retencion / neto | monetary | bruto/retención/neto triple | FR-125 |
| account.move (retention type 05) | l10n_hn_otcd_monthly / l10n_hn_delivery_due | boolean / date | 10 días hábiles monitor | FR-140 |
| account.move (boleta type 11) | l10n_hn_provider_ref (m2o res.partner) + provider signature/thumbprint flags | — | buyer-issued doc | FR-126 |
| stock.picking (guía type 08) | remitente / destinatario / transportista / conductor / placa / partida / destino / descripción_anexo / cantidad | char/m2o | transport field set | FR-135 |
| stock.picking (guía type 08) | l10n_hn_motivo_traslado | selection | 12-item catalog (FR-136) | FR-136 |
| stock.picking (guía type 08) | l10n_hn_origin_doc_ref (tipo/autorización/numeración/fecha) | char set | required for motives a/c/d/e/f | FR-137 |
| l10n_hn.prevalorada.event | event_date / rango_id / quantity_requested / notified_on / state | date / m2o / int / date / select | per-event authorization workflow | FR-121 |
| l10n_hn.boleta.cap.summary | partner_id / fiscal_year / exempt_base_resolved / accumulated | monitor | per-provider FY cap | FR-129 |
| l10n_hn.thermal.certification | vendor_id / warranty_years / presented_on | ≥5 | thermal regime record | FR-105 |
| l10n_hn.ticket.machine (xref 04 file) | cinta_archive_ref | char | per-machine audit-tape archive | FR-123 |
| account.move.line | l10n_hn_no_credit (boleta) | boolean | excluded from ISV credit | FR-127 |

## 5. Odoo Mapping

Layer semantics: `odoo` = print/master-data/posting surface in the LGPL
client (QWeb report engine); `shared` = contract items both sides honor
(dated parameters, origin-triple block, exonerado block semantics). No
SaaS-side compilation exists for HN's paper regime (no XML/DTE, no SEE
mandate in force) — `saas` is deliberately unused in this file (a future
SEE mandate re-opens the split per the 04 file). QWeb reporting and the
res.partner/account.move/stock.picking/l10n_latam.document.type surfaces
behave identically on Odoo 17/18/19/20; the D12/D15 regime note applies
wherever dated rows appear (FR-100, FR-109, FR-129).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-091 | odoo | ir.actions.report + QWeb template | layout structure | Two named render blocks per document template (format vs emission); 17-20 QWeb stable |
| FR-092 | odoo | res.company | RTN/name/nombre comercial/address/phone/email | Emitter master data; printed from company + establecimiento |
| FR-093 | odoo | l10n_hn.document.format | cai_id, fecha_limite, rango_label | Values consumed from the 02-file ledger at print time |
| FR-094 | odoo | QWeb template | destino block | Static print text |
| FR-095 | shared | res.partner | l10n_hn_oce_no/cre_no/sag_no | Partner master captured client-side; print + ingestion validation both honor the block |
| FR-096 | odoo | res.partner | l10n_hn_is_imprenta + imprenta data | R-H37: cite reglamento Art. 10.9, never the Ayudas |
| FR-097 | odoo | QWeb template | descuentos block | Post-01-mar-2019 layouts only (FR-109) |
| FR-098 | odoo | account.move + partner | name, vat, invoice_date, lines | Literal map verification OQ-003 |
| FR-099 | odoo | account.move.line + account.move | tax grid + amount_in_words | Totals-by-rate grid mirrors tax groups; amount-to-words via currency helper |
| FR-100 | shared | l10n_hn.parameter + account.move | threshold row + snapshot | Dated row L10,000 valid_from 2017-12-31; SEFIN-modifiable (OQ-001); D15 snapshot-on-write |
| FR-101 | odoo | res.currency.rate | rate at emission date | Print-only; base currency conversions unchanged |
| FR-102 | odoo | account.tax / account.move.line | credit-eligibility filter | Rate/pro-rata logic owned by taxation files by id |
| FR-103 | odoo | QWeb template | copia rendering | Same renderer for original/copia; per-destination footer only |
| FR-104 | odoo | QWeb template | optional QR/logo blocks | Never validated as required |
| FR-105 | odoo | l10n_hn.thermal.certification | vendor, warranty_years | Block thermal layout without record |
| FR-106 | odoo | report/export wizard | resúmenes generator | SAR plazos/medios undetermined (OQ-004) |
| FR-107 | odoo | account.move (supplier) | conformity flag | Ingestion-side check vs per-type requirement set |
| FR-108 | odoo | account.move (supplier) | verification attempt log | Manual/voluntary Verificador hook; no API |
| FR-109 | shared | dated regime rows | conformance resolver | Emission-date-driven; rows: pre-2018 / grace / full 481-2017 |
| FR-110 | odoo | sale/account flow | document-required gate | Universal emission duty |
| FR-111 | odoo | account.move | gratuitous flag | Free-of-charge ops still documented; zero-value lines allowed |
| FR-112 | odoo | pos/session close | end-of-day consolidation | Imprenta-modality pattern; generates consolidated document |
| FR-113 | odoo | res.company modality config (04 file) | exception disablement | Máquina-registradora/sistema-computarizado subscribers: per-transaction docs |
| FR-114 | odoo | account.move + fiscal position | tasa-cero tax | 0% ISV treatment per taxation files by id |
| FR-115 | odoo | account.move.line | consolidated vs labor-only | Fomento-regime valuation switch |
| FR-116 | odoo | QWeb template variant | reduced export layout | Literal set a/b/c/d/j/k; b only nacionalizaciones |
| FR-117 | odoo | stock/wizard | ZL matrix selector | Scenario-driven document pair generation |
| FR-118 | odoo | account.move + template | inter-ZL flags | Suppress ISV lines + exonerado block |
| FR-119 | odoo | account.move / stock.picking | transportista factura + muestra guía | Zero-rate service factura; guía for samples |
| FR-120 | odoo | document type + modality guard | prevalorada block | Consumer-final-only + imprenta-only enforcement |
| FR-121 | odoo | l10n_hn.prevalorada.event | event + notice tracker | ≥10 días hábiles pre-notice; rango declared |
| FR-122 | odoo | QWeb template | desprendible stub | Same info as original; detachable base (def. 5) |
| FR-123 | odoo | POS device config (04 file) | ticket + cinta archive | Per-machine audit-tape archival reference |
| FR-124 | odoo | account.move (correction) | origin ticket ref | Correction references original tickets |
| FR-125 | odoo | account.move (type 04) | bruto/retención/neto | Retención amount from taxation engine by id (HN-TAX-FR-137..148); DJIMR = S-HN3 |
| FR-126 | odoo | account.move (type 11) | provider block + firma/huella | Buyer-issued document |
| FR-127 | odoo | account.move.line | l10n_hn_no_credit | Excluded from ISV credit computation |
| FR-128 | odoo | l10n_hn.boleta.cap.summary | 5% aggregate monitor | Ex-financial deductible opex base from taxation files |
| FR-129 | shared | l10n_hn.boleta.cap.summary | exempt_base_resolved | FY-resolved from taxation dated rows by id (OQ-005) |
| FR-130 | odoo | QWeb template | reversed destino | Original→buyer, Copia→provider |
| FR-131 | odoo | account.move (type 12) | donee flow + dual seals | Emisor class restriction; imprenta-only (Art. 47) |
| FR-132 | odoo | account.move (NC/ND) | origin triple fields | Mandatory block + ledger existence validation (02-file ledger) |
| FR-133 | odoo | account.move (NC/ND) | motive + field set | Native reversal extended with HN block |
| FR-134 | odoo | stock.picking (guía) | emitter + 3-copy + tenencia | Pre-traslado validation; SAR control copy in print run |
| FR-135 | odoo | stock.picking | transport field set | Custom fields; carrier/driver/placa/partida/destino |
| FR-136 | shared | stock.picking | motivo selection | 12-item catalog; seed data shared with catalogs wave |
| FR-137 | odoo | stock.picking | origin doc ref | Required for motives a/c/d/e/f |
| FR-138 | odoo | stock.picking / sale flow | substitution + exceptions | Comprobante-with-transport-data path; itinerante; transit/menaje exemptions |
| FR-139 | odoo | account.move (type 05) | consolidation + anexo + paging | Per-retention or consolidated issuance |
| FR-140 | odoo | account.move (type 05) | OTCD variant + patronos flag | Monthly emission + 10 días hábiles delivery; on-request payroll issuance |

## 6. Acceptance Criteria

- **AC-001:** Given an approved factura layout, when any number of facturas is printed against it,
then the FORMAT-layer fields (CAI, fecha límite, rango, exonerado block, imprenta data) are
identical across all prints and no emission-time field overwrites them (FR-091).
- **AC-002:** Given a consumer-final sale of L10,000.01 with no client identification, when
confirmed, then it is blocked; given L10,000.00 exactly, then confirmation succeeds without client
data (FR-100).
- **AC-003:** Given a factura issued in USD, when printed, then the exchange rate in force at the
emission date appears; given a Lempira factura, then no rate is required (FR-101).
- **AC-004:** Given an original and its copia, when compared field by field, then they are
identical (FR-103).
- **AC-005:** Given a layout without QR/barcode/logo, when conformance is validated, then the
document passes (optionality, FR-104).
- **AC-006:** Given a factura dated 15-feb-2019 lacking the exonerado and descuentos blocks, when
conformance is resolved, then it is valid; dated 01-mar-2019, then it is non-conforming (FR-109).
- **AC-007:** Given consumer-final sales of L20 + L20 + L15 in one day by an imprenta-modality
taxpayer, when the day closes, then one consolidated document for L55 is generated; under a
sistema-computarizado subscription, then each sale carries its own document (FR-112, FR-113).
- **AC-008:** Given an export of taxed goods, when the factura is issued, then ISV applies at zero
rate with the reduced literal set, RTN literal present only for nacionalizaciones (FR-114,
FR-116).
- **AC-009:** Given a sale between two authorized zonas libres, when the factura is issued, then
it carries no ISV lines and no exonerado/OCE block (FR-118).
- **AC-010:** Given a prevalorada event on 20-feb with SAR notice recorded 15-feb (4 días
hábiles), when prevaloradas are issued, then emission is blocked/warned; with notice ≥10 días
hábiles prior, it proceeds (FR-121).
- **AC-011:** Given a prevalorada issued to an RTN-identified acquirer or from a
sistema-computarizado modality, when confirmed, then emission is blocked (FR-120).
- **AC-012:** Given an RHP with gross fees where the retention engine (by id) computes the
withholding, when printed, then the bruto/retención/neto triple appears and neto = brutos −
retención (FR-125).
- **AC-013:** Given FY deductible opex ex-financial of L1,000,000 and boleta-supported
transactions of L60,000, when the monitor runs, then the 5% cap (L50,000) is flagged exceeded with
a reclassification alert (FR-128).
- **AC-014:** Given a provider whose FY boleta-supported cumulative amount exceeds the resolved
ISR exempt-base amount, when the next boleta is prepared, then the system flags that the provider
must emit facturas (FR-129).
- **AC-015:** Given an NC lacking any of origin CAI / number / date, when posted, then posting is
blocked; given the full triple, then the origin is validated against the issued-document ledger
(FR-132).
- **AC-016:** Given a goods transfer without a guía and without a covering comprobante carrying
partida/destino/fechas/transportista/vehículo/conductor, when validated, then it is blocked;
given a guía, then three copies print including the SAR control copy (FR-134, FR-138).
- **AC-017:** Given January card retentions by an OTCD, when the month closes, then the
comprobante de retención is emitted Jan-31 with delivery due within the first 10 días hábiles of
February (FR-140).
- **AC-018:** Given a payroll retention on a permanent worker, when the payroll posts, then no
comprobante de retención is auto-issued; given a worker request, then it is issued (FR-140).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | L10,000 consumer-final ID threshold is SEFIN-modifiable by Acuerdo de Carácter General (Art. 11 final ¶); no modifying instrument in corpus. Primary home: this file. Ship as dated row (valid_from 31-dic-2017) and watch for a SEFIN acuerdo. (Origin: `24_ OQ-5`, master index C3.) | no | Takumi S-HN2 + controller | open |
| OQ-002 | 817-2018 Art. 3 cross-references a Código Tributario article for tax-reduction rectifications whose number is garbled by mojibake; candidate CT Art. 157 is UNVERIFIED and must not be cited. Non-facturación content (customs side); carried unchanged per master index C3. (Origin: `26_ OQ-1`, master index C3.) | no | controller (acquisition/re-OCR queue) | open (carried) |
| OQ-003 | Art. 11 inventory gaps: numeral 4 (exonerated-purchase clause) is truncated in EVID-190, and literals a)–f)/j) are quoted only as a compressed gloss — verify both against the 24_ PDF before implementing FR-098/FR-116 literal maps. | no | Takumi S-HN2 | open |
| OQ-004 | Thermal resúmenes de ventas: SAR sets plazos/medios/formas; no determining instrument in corpus — the FR-106 export surface stays parameterized. (LEAD/CONFIG.) | no | controller | open |
| OQ-005 | Boleta per-provider cap: which dated scale element is the "base exenta del ISR" (first-bracket exempt ceiling, IPC-adjusted)? Resolve by id from the taxation scale dated rows at implementation; do not restate the figure here. (VERIFY/CONFIG.) | no | Takumi S-HN2 + S-HN1 | open |
| OQ-006 | RHP adquirente RTN "cuando corresponda": no threshold analog to Art. 11's L10,000 appears in the text; default = no threshold extension to RHP. (DECIDE/VERIFY.) | no | Takumi S-HN2 | open |
| OQ-007 | Exonerado block: whether all three register identifiers (OCE/CRE/SAG) print for every exonerado operation or a per-regime subset applies — applicability rules live in the exonerations regime (05_/cluster T12) and are not pinned in 24_. (VERIFY.) | no | Takumi S-HN2 + S-HN1 | open |
