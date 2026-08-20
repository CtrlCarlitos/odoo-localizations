# HN — E-Invoicing — Document taxonomy, type-code catalog & correlativo grammar

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN2 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for Honduras' document
taxonomy and numbering grammar under the *Régimen de Facturación* (invoicing
regime, Acuerdo 481-2017 consolidado) — clusters E1 and E2 of the master
index. It owns: (a) the three statutory document categories — *Comprobantes
Fiscales* (fiscal vouchers), *Documentos Complementarios* (complementary
documents) and *Otros Comprobantes* (other supporting documents, R-Arts.
5-8) — with the original+copia custody rule and the four-condition
credit/cost gate for Otros Comprobantes; (b) the 2-digit type-code catalog
(01 Factura, 03 Ticket, 04 RHP, 05 Retención, 06 NC, 07 ND, 08 Guía, 10
Prevalorada, 11 Boleta de Compra, 12 Constancia de Donación; 02 unassigned)
including the **code-10 collision guard** (R-H38: DEI-279-2015 *Compras
Eventuales* vs 481-2017 *Prevalorada* — never both) and the ticket dual-code
default (R-H41); and (c) the *correlativo* (consecutive document number)
grammar — the 16-digit 3+3+2+8 structure of 481-2017 (establecimiento /
punto de emisión / tipo / consecutivo with wrap at 99999999), the historical
14-digit 4+2+8 grammar of Acuerdo 189-2014, the dual historical parser
switching by regime date (crossover 31-dic-2017), the Boleta-de-Venta→
Factura remap, the 01-mar-2019 print-requirements grace boundary, and the
dropped chain-linking rule. HN has NO national XML/DTE e-invoicing regime:
requirements model the taxonomy, the numbering grammar and the authorization
ledger inputs — never XML payloads.

It does **not** cover: the CAI/rango/vigencia authorization ledger and the
hard emission gate — `02_cai-ledger-emission-gate.md`
(HN-EINV-FR-046..090); per-document print content, the format vs
emission-time layers, the L10,000 consumer-final ID threshold, thermal/QR
rules and per-type emission mechanics (NC/ND origin triple, guía motivo
catalog, boleta caps) — `03_document-mechanics.md` (HN-EINV-FR-091..140);
inscription, topologies, medios (máquina registradora / SFC), SEE/CAEE and
contingencia — `04_registration-topologies-medios-see.md`
(HN-EINV-FR-141..175) — all three written in parallel with this file. Tax
computation lives in `../taxation/` (retention engines:
`04_isr-withholding.md`, HN-TAX-FR-121..153); DMC/DJIMR export contracts
are S-HN3 (W2) surfaces cross-referenced by id only.

## 2. Legal Basis

Authority order (binding, per master evidence index): `24_` (Acuerdo
481-2017 consolidado, effective 31-dic-2017) > `25_` (Acuerdo 189-2014,
HISTORICAL — repealed by R-Art. 78 + its 058-2014 reforma) > `26_`
(817-2018; Art. 1 cross-checks 24_ R-Art. 76-A verbatim). DEI-279-2015
(`18_`) governs *compras eventuales* (code-10 collision open, R-H38). Helps
`76_-78_` = operational workflow only — their Base-Legal sections are
DEFECTIVE; cite the *reglamento* R-Arts, never the helps (R-H37). D-H1
(one journal per company; sequence key = establecimiento/punto de
emisión/document type), D-H2 (dated rows; resolution by hecho-generador
date) and D-H3 (historical ingestion depths) bind this file.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglamento 481-2017, R-Art. 5 | "Son Documentos Fiscales: 1. Comprobantes Fiscales. 2. Documentos Complementarios. 3. Otros Comprobantes. Los Comprobantes Fiscales y los Documentos Complementarios expedidos en cualquier modalidad autorizada por la Administración Tributaria, deben generarse en original y copia. Las copias físicas o electrónicas serán resguardadas por los Obligados Tributarios según los plazos de prescripción que establece el Código Tributario." | Tax-document categories (3); original+copy universal for categories 1-2 in every authorized modality; copies physical or electronic; custody per CT prescription periods | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 5 p.13 (EV24:EVID-187) |
| LB-002 | 481-2017, R-Art. 6 | Comprobantes Fiscales = "1. Factura; 2. Factura Prevalorada; 3. Ticket; 4. Recibo por Honorarios Profesionales; 5. Boleta de Compra; 6. Constancia de Donación; y, 7. Los demás Comprobantes Fiscales que la Administración Tributaria autorice." | Fiscal-voucher roster with open slot 6.7 for SAR-added types | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 6 p.13 (EV24:EVID-187) |
| LB-003 | 481-2017, R-Art. 7 | Documentos Complementarios = "1. Notas de Crédito; 2. Notas de Débito; 3. Guías de Remisión; 4. Comprobantes de Retención; 5. Los demás ... que la Administración Tributaria autorice." | Complementary-document roster with open slot 7.5 | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 7 p.14 (EV24:EVID-187) |
| LB-004 | 481-2017, R-Art. 8 | Otros Comprobantes (public-utility receipts, CNBS-regulated banks/insurers, State and Municipalidad payment supports, import documents, treaty documents incl. IATA air tickets, State administrative acts) "no requieren trámite autorizante ante la Administración Tributaria y permiten sustentar el crédito fiscal del Impuesto Sobre Ventas, costo o gasto del Impuesto Sobre la Renta ... siempre que identifique el emisor y adquirente ... discrimine los impuestos por tarifas o alícuotas y conste la fecha de emisión." | Other documents: no authorization procedure; support ISV credit / ISR cost-expense subject to the 4 identification conditions | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 8 pp.14-15 (EV24:EVID-187) |
| LB-005 | 481-2017, R-Art. 10 num. 7 | "Número correlativo de la Factura. Constará de dieciséis (16) dígitos (NNN-NNN-NN-NNNNNNNN) ... a) Los tres primeros dígitos identificarán al establecimiento del Obligado Tributario, en función al código asignado por la Administración Tributaria al momento de su registro y para la casa matriz el sistema asignará el código 000; b) Los siguientes tres dígitos identificarán al punto de emisión, en función al código asignado por la Administración Tributaria; c) Los siguientes dos dígitos identificarán el código de la Factura, según el siguiente detalle: 01 = Factura; d) Los ocho dígitos restantes, corresponderán a la numeración correlativa de la Factura que deberá iniciarse en uno (00000001). Una vez completados los ocho dígitos (99999999), se reiniciará la numeración correlativa. Los primeros tres grupos de dígitos, se denominan identificador del documento" | The 16-digit grammar: establecimiento (3, matriz 000) + punto de emisión (3) + type code (2) + consecutive (8, starts 00000001, WRAPS at 99999999); first three groups = document identifier | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 10.7 pp.16-17 (EV24:EVID-188) |
| LB-006 | 481-2017, per-document code clauses | Type codes: **01 = Factura** (10.7c); **03 = Ticket** — "El Ticket tendrá como código 03, el cual podrá consignarse dentro del mismo" (Art. 17 last ¶); **04 = Recibo por Honorarios Profesionales** (18.7c); **05 = Comprobante de Retención** (33.5c); **06 = Nota de Crédito** (25.5c); **07 = Nota de Débito** (27.5c); **08 = Guía de Remisión** (29.4c); **10 = Factura Prevalorada** (15.6c); **11 = Boleta de Compra** (20.5c); **12 = Constancia de Donación** (23.7c). Code 02 appears nowhere in the 481-2017 text. | The 16-digit-era type-code catalog (code 02 unassigned — 24_ OQ-3) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Arts. 10.7c/15.6c/17/18.7c/20.5c/23.7c/25.5c/27.5c/29.4c/33.5c pp.16-45 (EV24:EVID-188) |
| LB-007 | 481-2017, R-Art. 17 num. 4 + last ¶ | Ticket numbering: "Numeración correlativa y autogenerada por la máquina registradora que debe constar como mínimo de diez (10) dígitos ... a) Los dos primeros dígitos identificarán el código del Ticket, según el siguiente detalle: 09=Ticket b) Los restantes ocho dígitos corresponderán a la numeración correlativa del Ticket que deberá iniciarse en uno (00000001)" | Ticket: machine-autogenerated numbering ≥ 10 digits with prefix 09 — the only document outside the 16-digit grammar, while its catalog code is 03 (dual-code quirk, R-H41) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 17 pp.24-25 (EV24:EVID-194; EVID-188) |
| LB-008 | Acuerdo 189-2014, Art. 41 num. 5 | "Número correlativo del Documento Fiscal, constará de catorce (14) dígitos (NNNN-NN-NNNNNNNN) ... a) Los cuatro primeros dígitos identificarán al punto de emisión ... b) Los siguientes dos dígitos identificarán el código del documento fiscal, según el siguiente detalle: 01 = Factura, 02 = Boleta de Venta, 03 = Recibo de alquiler, 04 = Recibo por honorarios, 05 = Comprobante de retención, 06 = Nota de crédito, 07 = Nota de débito; c) Los ocho dígitos restantes ... iniciarse en uno (00000001)" | Historical 14-digit grammar (punto de emisión 4 digits, NO establecimiento segment) and the 189-2014 code catalog 01-07 | `hn/sources/25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf` | Art. 41.5 p.10 (EV24:EVID-208) |
| LB-009 | 189-2014, Art. 7 | "La Dirección Ejecutiva de Ingresos autorizará la impresión de los documentos fiscales, para ser utilizados dentro de un plazo máximo de dos (2) años. ... A partir de la segunda autorización de impresión, el contribuyente deberá consignar el número del último documento fiscal emitido, previo a la solicitud, como un dato referencial." | 2-year vigencia (superseded by 481-2017's 1-year, ledger file 02) + the chain-linking rule (declare last emitted number on renewals) — dropped in 481-2017 (25_ OQ-1) | `hn/sources/25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf` | Art. 7 p.4 (EV24:EVID-208) |
| LB-010 | 189-2014, Arts. 10, 13-15 | Taxonomy: Comprobantes de Venta = "a. Factura b. Ticket c. Boleta de venta d. Recibo de alquiler e. Recibo por honorarios f. Otros comprobantes de venta, autorizados por la Dirección Ejecutiva de Ingresos". Art. 13: Ticket "no podrá sustentar crédito fiscal ... ni costos y gastos". Art. 14: Boleta de Venta = Régimen Simplificado + non-ISV contributors, costs/gastos only, "En ningún caso ... crédito fiscal". Art. 15: Recibo de Alquiler = PN rental of viviendas/locales under the ISV Art. 15.f threshold; ISV-subject landlords must factura. | Historical taxonomy and the two types 481-2017 abolished (Boleta de Venta 02, Recibo de Alquiler 03) with their historical support rights | `hn/sources/25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf` | Arts. 10, 13-15 pp.4-6 (EV24:EVID-208) |
| LB-011 | 481-2017, R-Arts. 78-79 | Art. 78: "Se derogan ... 1. Acuerdos No. 189-2014 ... y su reforma establecida en el Acuerdo No. 058-2014. 2. Toda norma reglamentaria que se oponga a las presentes disposiciones." Art. 79 (reformed 609-2017): "entrar en vigencia el 31 de diciembre de 2017." | Repeal of 189-2014 (+058-2014) and the regime-crossover date 31-dic-2017; the blanket "toda norma que se oponga" clause leaves DEI-279-2015 unexpressed (R-H38) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Arts. 78-79 pp.66-67 (EV24:EVID-207) |
| LB-012 | 481-2017, R-Arts. 76 y 76-A | Art. 76: 189-2014-authorized documents usable "hasta la Fecha Límite de Emisión o que finalice el Rango Autorizado ... lo que suceda primero"; "En los casos en que los Instructivos Tributarios Aduaneros, Reglamentos o Actos Administrativos indiquen el uso de la Boleta de Venta se deben entender que el Documento Fiscal a emitir es la Factura." Art. 76-A (added 725-2018, reformed 817-2018): facturas/boletas de compra/prevaloradas emitted hasta 28-feb-2019 without the exonerado-data + descuentos requirements "serán documentos válidos"; "A partir del 01 de marzo de 2019 ... todos los requisitos." | Transition: legacy stock until its fecha límite/rango end; Boleta-de-Venta→Factura remap; print-requirements grace boundary 01-mar-2019 | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Arts. 76, 76-A pp.65-66 (EV24:EVID-207; EVID-211) |
| LB-013 | DEI-SG-279-2015 (Comprobante de Compras Eventuales) | The compras-eventuales voucher (cat-D-municipality occasional purchases: grava/arena/material selecto + hospedaje/alimentación/mano de obra/flete; seller ≤ 10 SMM promedio/FY; provider ID flexible RTN/cédula/pasaporte/residencia; NO crédito fiscal; buyer retains the ISV caused — rate unstated). Its own text uses the 16-digit correlativo with **code 10 = Comprobante de Compras Eventuales** (the 16-digit grammar entered the corpus via this 22-mar-2016 instrument, before 481-2017 reassigned 10 to Prevalorada). | Occasional-purchases voucher: the OTHER claimant to code 10 (R-H38 collision; never implement 10 as both) | `hn/sources/18_Acuerdo_DEI-SG-279-2015_compras_eventuales.pdf` | Acuerdo DEI-SG-279-2015, 22-mar-2016 (via EV24:EVID-209, quoting W2a EV13:EVID-085) |
| LB-014 | 189-2014, Arts. 10.f / 21.7 / 69 | Art. 10.f: Comprobantes de Venta include "f. Otros comprobantes de venta, autorizados por la Dirección Ejecutiva de Ingresos." Art. 21.7: "Otros que la Dirección Ejecutiva de Ingresos autorice expresamente a través de Acuerdo de carácter general." Art. 69: DEI "emitirá los procedimientos necesarios para implementar el presente Reglamento". | The delegation hooks DEI-279-2015 was issued under — all repealed by R-Art. 78, so the procedure's substantive survival is plausible but unexpressed (R-H38) | `hn/sources/25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf` | Arts. 10.f, 21.7, 69 pp.4, 6, 20 (EV24:EVID-209) |
| LB-015 | 189-2014, Arts. 70-72 | Art. 71 derogó "a) Acuerdo No. 1314-2003 ... Reglamento de Registro Fiscal de Imprentas, Autorización y Uso de Facturas o Documentos de Carácter Fiscal; ... d) Toda norma que se oponga." Art. 72: vigencia "a partir del primer día del mes siguiente a la fecha de su publicación" (published 21-abr-2014 → effective 1-may-2014). | Reglamento lineage 1314-2003 → 189-2014 (1-may-2014) → 481-2017 (31-dic-2017), R-H39 | `hn/sources/25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf` | Arts. 70-72 p.20 (EV24:EVID-210) |
| LB-016 | Acuerdo 817-2018, Art. 1 | Reforms R-Art. 76-A: the quoted replacement text (grace hasta 28-feb-2019 / full requisitos from 01-mar-2019) "matches 24_ consolidated text verbatim — cross-check PASS" (R-H40). | Gazetted confirmation of the 76-A grace boundary (Arts. 2-3 of the same acuerdo are non-facturación) | `hn/sources/26_Acuerdo_817-2018_tercera_reforma.pdf` | 817-Art. 1 p.16 (EV24:EVID-211) |

## 3. Functional Requirements

### 3.1 Statutory document taxonomy (R-Arts. 5-8)

- **HN-EINV-FR-001:** The system shall model the three statutory categories
  of *Documentos Fiscales* — Comprobantes Fiscales, Documentos
  Complementarios, Otros Comprobantes — as a category attribute on document
  type records, and shall represent every HN facturación document type as a
  `l10n_latam.document.type` record under ONE invoicing journal per company
  (`l10n_latam_invoice_document`), never as one journal per document type
  (D-H1). (LB-001; EV24:EVID-187)
- **HN-EINV-FR-002:** The system shall seed the Comprobantes Fiscales
  roster per R-Art. 6: Factura, Factura Prevalorada, Ticket, Recibo por
  Honorarios Profesionales, Boleta de Compra, Constancia de Donación — with
  an open extension slot for "los demás Comprobantes Fiscales que la
  Administración Tributaria autorice" (num. 6.7).
  (LB-002; EV24:EVID-187)
- **HN-EINV-FR-003:** The system shall seed the Documentos Complementarios
  roster per R-Art. 7: Notas de Crédito, Notas de Débito, Guías de
  Remisión, Comprobantes de Retención — with the parallel open slot
  (num. 7.5). (LB-003; EV24:EVID-187)
- **HN-EINV-FR-004:** The system shall register Otros Comprobantes
  (public-utility receipts, CNBS-regulated bank/insurer documents, State
  and *Municipalidad* payment supports, import documents, treaty documents
  including IATA air tickets, State administrative acts) as an open family
  category requiring NO authorization procedure (no CAI, no rango, no
  vigencia), ingestible as supplier-document support without authorization
  data. (LB-004; EV24:EVID-187)
- **HN-EINV-FR-005:** The system shall accept an Otros Comprobante as
  support for ISV *crédito fiscal* (tax credit) or ISR cost/expense only
  when it satisfies ALL four statutory conditions: (a) identifies the
  emitter, (b) identifies the *adquirente* (acquirer), (c) discriminates
  taxes by rate/*alícuota*, (d) states the emission date; failure of any
  condition shall block credit/cost rights attribution on ingestion.
  (LB-004; EV24:EVID-187)
- **HN-EINV-FR-006:** The system shall require original + copia generation
  for every Comprobante Fiscal and Documento Complementario in every
  authorized modality (physical or electronic copies both valid), and shall
  archive both for the Código Tributario prescription periods (4/5/7 years,
  owned by the CT/T11 taxation file by id). (LB-001; EV24:EVID-187)

### 3.2 Type-code catalog & collision guards

- **HN-EINV-FR-007:** The system shall seed the 16-digit-era type-code
  catalog exactly as the per-document clauses assign it — 01 Factura
  (Comprobante Fiscal), 03 Ticket (CF), 04 Recibo por Honorarios
  Profesionales (CF), 05 Comprobante de Retención (DC), 06 Nota de Crédito
  (DC), 07 Nota de Débito (DC), 08 Guía de Remisión (DC), 10 Factura
  Prevalorada (CF), 11 Boleta de Compra (CF), 12 Constancia de Donación
  (CF) — with the `document_types.csv` sidecar (§4) as the
  machine-readable source of truth. (LB-006; EV24:EVID-188)
- **HN-EINV-FR-008:** The system shall treat type code 02 as
  unassigned-reserved: no emittable document type shall carry code 02 under
  the 481-2017 regime, and SAR assignment of 02 (or any new code) via the
  R-Art. 6.7/7.5 slots shall enter as a new dated catalog row, never as an
  edit of existing rows (24_ OQ-3 watch). (LB-006; EV24:EVID-188)
- **HN-EINV-FR-009:** The system shall enforce the code-10 single-assignment
  invariant (R-H38): code 10 in the 16-digit grammar shall map to exactly
  ONE document type. Default active assignment = 10 Factura Prevalorada
  (481-2017, current authority). The DEI-279-2015 Comprobante de Compras
  Eventuales claim on code 10 shall ship as a collision-open, non-emittable
  catalog row; the system shall NEVER implement code 10 as both, and shall
  block any configuration that activates both claims (resolving lead = a
  post-2017 SAR instrument, none in corpus). (LB-006; LB-013; LB-014;
  EV24:EVID-188; EV24:EVID-209)
- **HN-EINV-FR-010:** The system shall implement the ticket dual-code
  default (R-H41): the Ticket's catalog code is 03; the máquina registradora
  autogenerated numbering (≥ 10 digits, prefix 09, consecutive starting
  00000001) shall be stored as machine numbering, untouched; no 16-digit
  grammar enforcement shall apply to tickets; prefix 09 shall never be
  implemented as a document-type code. (LB-007; EV24:EVID-194)
- **HN-EINV-FR-011:** The system shall provide a catalog-extension mechanism
  for SAR-authorized additional types (R-Arts. 6.7/7.5): additions arrive
  as new rows with their own code, name, category, `valid_from` and source
  instrument — additive-only, never overwriting existing rows (D-H2 dated
  rows). (LB-002; LB-003; EV24:EVID-187)

### 3.3 The 16-digit correlativo grammar (481-2017)

- **HN-EINV-FR-012:** The system shall compose every 16-digit *correlativo*
  as NNN-NNN-NN-NNNNNNNN — establecimiento (3) + punto de emisión (3) +
  type code (2) + consecutive (8) — and shall store both the four segments
  and the hyphenated full string; the first three groups constitute the
  statutory *identificador del documento* (document identifier).
  (LB-005; EV24:EVID-188)
- **HN-EINV-FR-013:** The system shall source the establecimiento segment
  from the SAR-assigned registration code of the emitting establishment,
  defaulting to 000 for the *casa matriz* (main establishment) — stored
  configuration data, never derived. (LB-005; EV24:EVID-188)
- **HN-EINV-FR-014:** The system shall source the punto de emisión segment
  from the SAR-assigned code of the emission point (one or more per
  establecimiento), likewise stored data. (LB-005; EV24:EVID-188)
- **HN-EINV-FR-015:** The system shall set the two-digit type segment equal
  to the document's catalog type code, and shall validate the match at
  emission and at ingestion (mismatch = hard validation error).
  (LB-005; LB-006; EV24:EVID-188)
- **HN-EINV-FR-016:** The system shall generate the 8-digit consecutive
  starting at 00000001 and shall WRAP back to 00000001 after 99999999 — a
  statutory restart, never an error state (rango-span linkage owned by file
  02). (LB-005; EV24:EVID-188)
- **HN-EINV-FR-017:** The system shall NOT reset the consecutive at fiscal
  year or any calendar boundary: the HN correlativo is a continuum per
  sequence key until the 99999999 wrap (no reset clause exists in either
  reglamento; contrast with FY-reset regimes such as SV).
  (LB-005; EV24:EVID-188)
- **HN-EINV-FR-018:** The system shall key numbering series on
  (establecimiento, punto de emisión, document type) with independent
  consecutives per key (D-H1); topology variants that collapse the key —
  one correlativo for many establecimientos under SISTEMA CENTRALIZADO /
  REGIONAL — are owned by file 04 and reconcile here as key collapses, not
  new grammars. (LB-005; EV24:EVID-188; crossref EV24:EVID-203 → file 04)
- **HN-EINV-FR-019:** The system shall never reuse or reissue a document
  number within a sequence key: voided documents keep their number and are
  marked per the lifecycle rules (file 02); the imprenta no-reprint
  prohibition is the external guarantee of correlativo uniqueness.
  (LB-005; EV24:EVID-188; crossref EV24:EVID-206)

### 3.4 Historical grammar, dual parser & regime crossover

- **HN-EINV-FR-020:** The system shall parse historical 14-digit
  correlativos under the 189-2014 grammar NNNN-NN-NNNNNNNN — punto de
  emisión (4, no establecimiento segment) + type code (2) + consecutive (8,
  starting 00000001). (LB-008; EV24:EVID-208)
- **HN-EINV-FR-021:** The system shall seed the 189-2014-era code catalog
  01-07 (Factura, Boleta de Venta, Recibo de Alquiler, Recibo por
  honorarios, Comprobante de retención, Nota de crédito, Nota de débito) as
  grammar-era rows in the sidecar, with Boleta de Venta (02) and Recibo de
  Alquiler (03) flagged abolished-pre-2018. (LB-008; LB-010;
  EV24:EVID-208)
- **HN-EINV-FR-022:** The system shall resolve the correlativo grammar by
  the document's emission date against the regime rows (D-H2 resolution by
  domain date, never "today"): emission date in [1-may-2014, 30-dic-2017]
  → 14-digit; from 31-dic-2017 → 16-digit; within the transition window
  (from 31-dic-2017 until each legacy authorization's fecha límite/rango
  end per R-Art. 76) BOTH grammars shall be accepted for validation of
  189-2014-authorized stock. Documents dated before 1-may-2014 (1314-2003
  era, grammar not in corpus) are out of ingestion depth (D-H3) and shall
  be rejected by the parser with an explicit era error. (LB-008; LB-011;
  LB-012; EV24:EVID-207; EV24:EVID-208)
- **HN-EINV-FR-023:** The system shall remap Boleta de Venta references:
  any Instructivo Tributario Aduanero, Reglamento or administrative act
  indicating use of the Boleta de Venta shall be interpreted — for
  post-crossover operations — as requiring the Factura (R-Art. 76);
  historical Boletas de Venta remain valid period cost/gasto support only
  (never crédito fiscal, LB-010). (LB-010; LB-012; EV24:EVID-207;
  EV24:EVID-208)
- **HN-EINV-FR-024:** The system shall flag the two abolished types as
  non-emittable for every date from 31-dic-2017: Boleta de Venta (remap per
  FR-023) and Recibo de Alquiler (R-H42: abolished; pre-2018 recibos de
  alquiler remain legitimate historical cost support; the cédular-alquiler
  retention family is unaffected — retention ≠ document type).
  (LB-010; LB-012; EV24:EVID-207; EV24:EVID-208)
- **HN-EINV-FR-025:** The system shall carry the regime-crossover rows as
  dated configuration per R-H39 lineage: 1314-2003 → 189-2014
  (`valid_from` 1-may-2014) → 481-2017 (`valid_from` 31-dic-2017), plus
  the print-requirements grace boundary of R-Art. 76-A (documents emitted
  until 28-feb-2019 valid without the exonerado-data + descuentos
  requirements; full conformance mandatory from 01-mar-2019 — requirement
  content owned by file 03, boundary row owned here).
  (LB-011; LB-012; LB-015; LB-016; EV24:EVID-207; EV24:EVID-210;
  EV24:EVID-211)
- **HN-EINV-FR-026:** The system shall treat chain-linking as optional
  reference data only: 189-2014 Art. 7 required declaring the last emitted
  number on second+ print authorizations; 481-2017 drops the rule, so
  renewal requests may carry a last-issued-number reference field
  (operational continuity data for file 02's renewal workflow) but the
  system shall never require it. (LB-009; EV24:EVID-208)
- **HN-EINV-FR-027:** The system shall ingest historical documents per
  D-H3 as read-only flagged records: current-FY document detail with
  original numbers and original dates, validated against the grammar/rows
  in force at those dates (FR-022 resolution); no sequence consumption; no
  re-emission; prior years as aggregates only. (LB-008; LB-011;
  EV24:EVID-207; EV24:EVID-208)

### 3.5 Ingestion validation & machine-readable catalog

- **HN-EINV-FR-028:** The system shall validate every ingested fiscal
  document number by era-resolved grammar: 16-digit regex
  `^\d{3}-\d{3}-\d{2}-\d{8}$` (or unhyphenated 16) with code membership in
  the 481-2017 catalog; 14-digit regex `^\d{4}-\d{2}-\d{8}$` (or
  unhyphenated 14) with code membership in the 189-2014 catalog; and shall
  expose the number in the 4-segment form used as the DMC line key
  (establecimiento/punto/tipo/correlativo — W2 F3 kin crossref,
  EV43:EVID-145). (LB-005; LB-006; LB-008; EV24:EVID-188; EV24:EVID-208)
- **HN-EINV-FR-029:** The system shall cross-reference — without owning —
  the compras-eventuales duties: type-10 purchases carry a DMC registration
  duty (W2 F3, EV13:EVID-087) and a buyer-ISV retention whose rate/base is
  UNSTATED in the corpus (18_ OQ-6 / 45_ OQ-2, fiscal-reporting open);
  nothing in this file shall emit a type-10 compras-eventuales document
  while FR-009's collision stands open. (LB-013; EV24:EVID-209)
- **HN-EINV-FR-030:** The system shall load `document_types.csv` (§4) as
  the seed catalog — one row per type code × grammar era — with columns
  code, name_es, name_en, category, grammar, status, valid_from,
  valid_to, notes; statuses: active · historical · abolished-pre-2018 ·
  unassigned · collision-guarded · collision-open · reserved-machine-prefix
  (extensions of the base set documented in §4). (LB-006; LB-008;
  EV24:EVID-188; EV24:EVID-208)
- **HN-EINV-FR-031:** The system shall carry taxonomy metadata on catalog
  rows consumed from sibling files by id: issuer direction (emitter-issued
  default; Boleta de Compra = buyer-issued with reversed original/copia;
  Constancia de Donación = donee-issued) and modality eligibility
  (Factura Prevalorada, RHP and Constancia de Donación = imprenta-exclusive
  — no electronic path; Ticket = máquina registradora exclusive; rules
  owned by file 04). (LB-002; EV24:EVID-196; EV24:EVID-197; crossref
  EV24:EVID-203 → file 04)

## 4. Data Model

Machine-readable sidecar next to this file: `document_types.csv` — one row
per type code × grammar era (20 rows). CSV discipline: comma-separated,
header row, LF endings, UTF-8 without accents inside `name_es` values
(ASCII-safe for seed loaders; the markdown above carries the accented legal
spellings). Dated-row semantics per D-H2: 16-digit-era rows carry
`valid_from` 2017-12-31 (481-2017 Art. 79) with open-ended `valid_to`
(current regime); 14-digit-era rows carry `valid_from` 2014-05-01 (189-2014
Art. 72) and `valid_to` 2017-12-30 = the PRIMARY regime window — the
R-Art. 76 transition tolerance (legacy stock valid until its own fecha
límite/rango end) is engine behavior (FR-022), not a row date. Status value
set: `active` (emittable under the current regime) · `historical`
(surviving type, superseded grammar era) · `abolished-pre-2018` (type
abolished by 481-2017: Boleta de Venta, Recibo de Alquiler) · `unassigned`
(code 02, reserved) · `collision-guarded` (10 Prevalorada — active under
R-H38 single-assignment guard) · `collision-open` (10 Compras Eventuales —
non-emittable until resolved) · `reserved-machine-prefix` (09 — a máquina
registradora numbering prefix, never a document type). The 189-2014 regime
listed the Ticket in its taxonomy (Art. 10 literal b) but assigned it no
2-digit code clause, hence no 14-digit ticket row exists.

**Document-type catalog (taxonomy layer, D-H1):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_latam.document.type | code | char(2) | 01, 03-08, 10, 11, 12 (16-digit era); 01-07 (14-digit era rows); 02 unassigned | FR-007, FR-008, FR-021 |
| l10n_latam.document.type | name / name_en | char | Spanish statutory name + English translation | FR-007 |
| l10n_latam.document.type (HN extension) | hn_category | select | comprobante_fiscal · documento_complementario · otros_comprobante (family) | FR-001..FR-004 |
| l10n_latam.document.type (HN extension) | hn_grammar | select | 16-digit · 14-digit · machine-autogen (ticket) | FR-007, FR-010, FR-020 |
| l10n_latam.document.type (HN extension) | hn_status | select | active · historical · abolished-pre-2018 · unassigned · collision-guarded · collision-open · reserved-machine-prefix | FR-008, FR-009, FR-024 |
| l10n_latam.document.type (HN extension) | hn_issuer_direction | select | emitter · buyer (11 Boleta de Compra) · donee (12 Constancia de Donación) | FR-031 |
| l10n_latam.document.type (HN extension) | valid_from / valid_to | date | era rows per CSV (2014-05-01→2017-12-30; 2017-12-31→open) | FR-025, FR-030 |

**Numbering structures (sequence key per D-H1):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| stock.warehouse (HN extension) | l10n_hn_establecimiento_code | char(3) | SAR-assigned at registration; casa matriz = 000; NOT stock.location | FR-013 |
| l10n_hn.emission.point (new) | warehouse_id, code (char 3), type (fijo/móvil) | m2o/char/select | child emission point of the warehouse; SAR-assigned code; does NOT live on account.journal (D-H1) | FR-014 |
| ir.sequence (per key) | prefix, padding | char/int | key = (warehouse, emission point, document type); padding 8; NO date_range year reset (FR-017); wrap-at-99999999 = custom restart (FR-016) | FR-012, FR-016..FR-018 |
| account.move | l10n_latam_document_type_id + l10n_hn_number_*, l10n_hn_document_number, l10n_hn_grammar, is_historical | m2o/char(16)/select/boolean | segments + composed hyphenated string + era + read-only historical flag (D-H3) | FR-012, FR-022, FR-027 |
| account.move (supplier side) | otros_comprobante flag + 4-condition checklist | boolean | ingestion acceptance gate for Otros Comprobantes | FR-004, FR-005 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = catalog, numbering and validation
logic living in the LGPL client. No `saas`/`shared` rows are introduced:
HN's current regime is paper-based (CAI), and the statutory electronic
surface (SEE/CAEE) is blocked on unpublished technical docs (lead 1, file
04) — no DTE-like payload exists for this file to split across the
thin-client architecture. Model names stable across Odoo 17/18/19/20;
version-specific behavior recorded per row where relevant.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001..FR-003 | odoo | account.journal (`l10n_latam_invoice_document`=True) + l10n_latam.document.type | document types per journal | ONE journal per company carrying multiple document types (D-H1); `l10n_latam_invoice_document` pattern available 17-20 unchanged |
| FR-004, FR-005 | odoo | account.move (supplier) + l10n_latam.document.type (otros family) | otros flag + condition checklist | Acceptance gate on vendor-bill ingestion; no CAI required for this family |
| FR-006 | odoo | account.move + document archival | original/copia custody | Electronic copies satisfy the rule; retention follows CT prescription config (taxation T11 file) |
| FR-007..FR-011 | odoo | l10n_latam.document.type | code/name/category/grammar/status/dates | Seeded from `document_types.csv`; additive-only extension (D-H2); per-company activation gated by file 02/04 authorization data |
| FR-009 | odoo | l10n_latam.document.type | config constraint | Single-assignment constraint on code 10 (R-H38): activating both 10-rows raises a configuration error; compras-eventuales row ships non-emittable |
| FR-010 | odoo | l10n_latam.document.type + POS ticket numbering | machine number field | Catalog code 03; store máquina autogen number (prefix 09) verbatim; suppress 16-digit validation for the ticket type (R-H41) |
| FR-012..FR-016 | odoo | ir.sequence + l10n_hn.emission.point + stock.warehouse | prefix/padding/segments | Sequence prefix composes establecimiento+punto+type; padding 8. **17-20:** ir.sequence has NO native wrap-at-99999999 — implement statutory restart (FR-016) as override; ticket/exception paths unaffected |
| FR-017 | odoo | ir.sequence | no date_range | **17-20 default sequences reset yearly via date_range ranges** — HN must not attach fiscal-year ranges to these sequences (continuum until wrap) |
| FR-018 | odoo | l10n_hn.emission.point × l10n_latam.document.type × stock.warehouse | sequence key | Full key = (warehouse, emission point, document type) per D-H1; centralizado/regional topology key collapse consumed from file 04 |
| FR-019 | odoo | ir.sequence + account.move | uniqueness constraint | No-reuse constraint on (emission point, type, consecutive); voided docs keep numbers (lifecycle marking = file 02) |
| FR-020..FR-022 | odoo | account.move parser | l10n_hn_grammar resolution | Era resolved from the document's own date (D-H2), never `today`; dual acceptance in the R-Art. 76 transition window; pre-2014 → explicit era error (out of D-H3 depth) |
| FR-023, FR-024 | odoo | l10n_latam.document.type | abolished flags + remap helper | Boleta-de-Venta remap applies to legacy instrument references, not to stored historical documents (kept verbatim under their own type) |
| FR-025 | odoo | l10n_hn.regime rows (new config) | dated rows | Lineage + grace boundary as data (R-H39); conformance-content enforcement = file 03 |
| FR-026 | odoo | renewal request model (file 02 surface) | optional last-issued reference | Never mandatory; captured as operational continuity data |
| FR-027 | odoo | account.move (historical journals) | is_historical + original numbers | D-H3: read-only flagged imports; validated against era rows; excluded from sequence consumption and from filings Odoo didn't make |
| FR-028 | odoo | account.move ingestion validator | regex + code membership + 4-segment export | Exposes the DMC line-key shape consumed by S-HN3 (F3) |
| FR-029 | odoo | — | crossref only | Type-10 registration duty + retention rate/base = fiscal-reporting open items (18_ OQ-6); no emission surface here |
| FR-030 | odoo | CSV seed loader | document_types.csv | 20 rows; statuses per §4 value set; reload = additive |
| FR-031 | odoo | l10n_latam.document.type metadata | issuer direction / modality eligibility | Modality-eligibility rules authoritative in file 04; this file only carries the flags |

Version-regime note (D12): FR-025 records the reglamento lineage with per-
regime dated rows (1-may-2014 / 31-dic-2017) and the 01-mar-2019 grace
boundary; no adaptation windows exist beyond the statutory transition
itself. FR-030's CSV carries `valid_from`/`valid_to` per row; a future SAR
type addition (FR-011) extends the file additively.

## 6. Acceptance Criteria

- **AC-001:** Given the seeded catalog, then exactly these codes are active
  16-digit-era types — 01, 03, 04, 05, 06, 07, 08, 10, 11, 12 — with
  categories CF for 01/03/04/10/11/12 and DC for 05/06/07/08, and code 02
  exists only as an unassigned-reserved row (FR-007, FR-008).
- **AC-002:** Given a CNBS-regulated bank statement ingested as a supplier
  document identifying emitter and acquirer, discriminating ISV by rate and
  dated, then it is accepted as cost/credit support; given the same
  document without tax discrimination, then credit/cost attribution is
  blocked with a condition-level error (FR-005).
- **AC-003:** Given an attempt to activate both code-10 rows (Prevalorada
  and Compras Eventuales) as emittable types, then the configuration is
  rejected with a code-10 collision error (R-H38); given only Prevalorada
  active, then code 10 validates (FR-009).
- **AC-004:** Given a ticket emission, then the document stores its
  máquina-autogenerated number (prefix 09, ≥ 10 digits) verbatim, carries
  catalog code 03, and no 16-digit grammar validation is applied; given an
  attempt to create a document type with code 09, then it is rejected
  (FR-010).
- **AC-005:** Given the first factura at key (establecimiento 001, punto
  001, type 01), then its number is 001-001-01-00000001; given the document
  following consecutive 99999999 at the same key, then the consecutive
  restarts at 00000001 (wrap, not error) (FR-012, FR-016).
- **AC-006:** Given the last factura of December 2026 and the first of
  January 2027 at the same key, then the consecutive continues without
  reset (no fiscal-year range attached) (FR-017).
- **AC-007:** Given a company's registered main establishment, then its
  establecimiento segment is 000; given a sucursal with SAR code 003, then
  the segment is 003 (FR-013).
- **AC-008:** Given a stored factura whose type segment reads 04, then
  emission/ingestion validation fails with a segment/type mismatch
  (FR-015).
- **AC-009:** Given the ingested number 0123-02-00000001 with emission date
  15-jun-2015, then it parses under the 14-digit grammar as punto 0123,
  type 02 Boleta de Venta (abolished-pre-2018 row, read-only); given the
  same number dated 01-mar-2019 without legacy-authorization declaration,
  then it is rejected as out-of-era (FR-020..FR-022).
- **AC-010:** Given a 14-digit document dated 15-feb-2018 flagged as
  189-2014-authorized stock (transition window), then it validates as a
  read-only historical record; given a 16-digit document dated the same
  day, then it also validates (dual acceptance) (FR-022).
- **AC-011:** Given a post-crossover operation whose governing instrument
  says "Boleta de Venta", then the document-type selector resolves to
  Factura (FR-023).
- **AC-012:** Given a renewal request, then the last-issued-number field is
  optional — submission succeeds empty; the field, when provided, is stored
  as reference data (FR-026).
- **AC-013:** Given an imported pre-2018 Recibo de Alquiler (code 03,
  14-digit), then it ingests read-only flagged with `is_historical`=True,
  validates against the 189-era catalog, consumes no sequence and cannot be
  amended or re-emitted (FR-021, FR-024, FR-027).
- **AC-014:** Given `document_types.csv` loaded, then 20 rows exist (13
  current-era incl. 02/09/10×2 special rows + 7 historical-era), each with
  a status from the §4 value set and era-consistent valid_from/valid_to
  (FR-030).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `24_ OQ-1` (C3 carry, VERIFY): ticket dual code — catalog 03 vs máquina prefix 09, no 16-digit enforcement for tickets. FR-010 encodes the default; verify vs SAR's Oficina Virtual validador or a real ticket (does a 481-2017-regime ticket live in the (establecimiento, punto, 03) sequence space at all?). | no | Takumi S-HN2 + controller | open |
| OQ-002 | `24_ OQ-2` (C3 carry, CONFLICT): **code-10 collision** — DEI-279-2015 "10 = Compras Eventuales" vs 481-2017 "10 = Prevalorada"; 279's host articles repealed by R-Art. 78, survival unexpressed. R-H38 ruling stands: NEVER implement both (FR-009). Resolving lead = a post-2017 SAR instrument on compras eventuales (none in corpus); also watch the Oficina Virtual intake or a SAR consult. | no (guarded) | acquisition queue | open |
| OQ-003 | `24_ OQ-3` (C3 carry, VERIFY): code 02 unassigned in 481-2017 — assumed reserved (FR-008); watch for SAR-added types via the R-Art. 6.7/7.5 slots. | no | Takumi S-HN2 | open |
| OQ-004 | `25_ OQ-1` (C3 carry, VERIFY): chain-linking dropped in 481-2017 — do current SAR-924/927 solicitudes still capture last-issued-number as continuity data? FR-026 supports it as optional; confirm against the live solicitud forms (76-78_ OQ-2 form-layout lead) before building the renewal surface. | no | Takumi S-HN2 (with file 02) | open |
| OQ-005 | ~~`25_ OQ-2`~~ (C3 carry, struck — resolved): Recibo de Alquiler post-2018 → **resolved by R-H42**: abolished as a document type; pre-2018 recibos = legitimate historical cost support (FR-024, AC-013); cédular alquiler retention unaffected (retention ≠ document type). Encoded; no further action. | no | — | resolved (R-H42) |
| OQ-006 | Local derivation (VERIFY): FR-022's transition-window dual acceptance — 14-digit documents dated after 31-dic-2017 validate only when flagged as 189-2014-authorized stock (R-Art. 76 "hasta la Fecha Límite de Emisión o que finalice el Rango Autorizado"). Default is defensible on the statute; verify against SAR's DMC intake behavior for Jan-2018..2019 window documents (EVID-145 surface, S-HN3 kin) before freezing the validator. | no | Takumi S-HN2 + S-HN3 | open |
