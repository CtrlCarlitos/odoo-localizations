# HN — E-Invoicing — Registration, emission topologies, medios & the SEE/CAEE placeholder contract

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN2 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the *Régimen de Facturación*
(facturación regime, Acuerdo 481-2017) infrastructure layer: inscription — the
declared matrix of *modalidades* (printing modalities) × document types ×
*establecimientos* (establishments) × *puntos de emisión* (emission points),
filed as Form SAR-926 through the Oficina Virtual; per-device/per-system
registration (each *máquina registradora* dispositivo and each *sistema
computarizado* (SFC) at its own granularity, Art. 61 kin); the emission-point
entity — fixed (*fijo*) vs mobile (*móvil*) — which per decision D-H1 does
NOT live on `account.journal` but on the move and a dedicated entity feeding
sequences; the three numbering topologies (*sistema centralizado / regional /
por sucursal*) reconciled with the D-H1 sequence key (establecimiento →
`stock.warehouse`, punto de emisión → child emission point, document type →
`l10n_latam.document.type`); the modalidades (imprenta / autoimpresor) and
their *medios* (means); the imprenta-EXCLUSIVE documents (prevalorada, recibo
por honorarios, constancia de donación — no electronic path); the five SFC
specifications plus the *Declaración Jurada* (sworn declaration)
attestation; the *Sistema de Emisión Electrónica* (SEE, Arts. 50-58) with its
per-document *CAEE* (electronic-emission authorization code) — CONFIG-GAPPED
placeholders because Art. 58's technical documentation is UNPUBLISHED (open
lead 1; quarterly re-check); the Art. 57 gradual mandate as dated per-company
rows (D-H2.6); contingency emission by switching to imprenta preprinted
stock; and the user ↔ emission-point authorization matrix seeded by the
*acreditación de responsables* (accreditation of responsible persons)
inscription practice — an explicitly NON-statutory operational control.
Honduras currently has NO transmission regime: *facturación electrónica*
(electronic invoicing) is legally a medium of the autoimpresor modality
(def. 22), with no XML/DTE mandate in the text — the SEE placeholder contract
in §3.8 is the hook through which any future mandate lands.

It does **not** cover: the document taxonomy, type-code catalog and 16-digit
correlativo grammar (`01_document-types-numbering.md`, HN-EINV-FR-001..031);
the CAI/rango authorization ledger, its state chain (SAR-924/SAR-927),
authorization granularity (Art. 61), vigencia and the hard emission gate
(`02_cai-ledger-emission-gate.md`, HN-EINV-FR-046..090); print/per-document
mechanics incl. cinta de auditoría (`03_document-mechanics.md`,
HN-EINV-FR-091..140); the Registro Fiscal de Imprentas regime and
no-utilizados notifications (cluster E7, sibling files); and RTN suspension
blocking facturación (`../taxation/01_isr-framework.md`, HN-TAX-FR-001..045)
— crossref only.

## 2. Legal Basis

Authority order (binding, per master evidence index): `24_` (Acuerdo 481-2017
consolidado, effective 31-dic-2017) R-Arts govern; helps `76_-78_` are
operational-workflow authority only and their Base-Legal sections are
DEFECTIVE (R-H37: 76_ miscites Art. 42 — the no-utilizados duty — instead of
the inscription basis), so every LB below cites the reglamento R-Arts
directly. D-H1/D-H2 bind all rows; D-H2.6 lands in §3.8.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglamento (Acuerdo 481-2017), Art. 45: requisitos de inscripción — datos del RTN actualizados; "Estar al día en la presentación y pago de las obligaciones formales y materiales"; suscribir contrato de adhesión; formulario SAR; declarando "a) Modalidades de Impresión; b) Comprobantes Fiscales y/o Documentos Complementarios; c) Establecimientos; d) Puntos de Emisión" | Inscription requirements: updated RTN data; be current on the presentation and payment of formal and material obligations; sign the adhesion contract; SAR form; declaring printing modalities, fiscal/complementary documents, establishments, and emission points | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 45 pp.51-52 (EV24:EVID-203) |
| LB-002 | Reglamento, Art. 46: modalidad por imprenta — selección de imprenta del Registro Fiscal de Imprentas; "En el caso de las Facturas Prevaloradas y Recibo por Honorarios Profesionales, deben ser exclusivamente emitidos bajo la modalidad de imprenta" | Print-shop modality — the taxpayer selects a print shop from the Fiscal Print-Shops Registry; Pre-Valued Invoices and Professional Fees Receipts must be EXCLUSIVELY issued under the print-shop modality | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 46 p.52 (EV24:EVID-203) |
| LB-003 | Reglamento, Art. 47: inscripción como autoimpresor "a excepción de las Facturas Prevaloradas, Recibos por Honorarios Profesionales y Constancias de Donación"; usuarios de máquinas registradoras "deben registrar cada dispositivo ... y el establecimiento donde se encuentre instalado cada equipo"; usuarios de sistemas computarizados registran cada sistema "a fin de identificar el software ... el establecimiento donde se encuentre el servidor y los distintos puntos de emisión. Los Sistemas Computarizados pueden ser de dos tipos: 1. Sistema Computarizado Independiente; 2. Sistema Computarizado en Red" | Autoimpresor inscription EXCEPTS pre-valued invoices, professional fees receipts and donation certificates; cash-register users must register EACH device and the establishment where it is installed; computerized-system users register each system identifying the software, the establishment hosting the server and the emission points; systems are standalone (independiente) or networked (en red) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 47 pp.52-53 (EV24:EVID-203) |
| LB-004 | Reglamento, Art. 48: "a) SISTEMA CENTRALIZADO: La generación ... de los establecimientos registrados en el RTN, se origina en un único punto de emisión de su Sistema Computarizado a nivel nacional. En este caso se operará con una sola numeración correlativa, sin perjuicio de la casa matriz o sucursales. b) SISTEMA REGIONAL: ... en una misma región, se origina en un único punto de emisión ... En este caso se operará con una sola numeración correlativa para cada región. c) SISTEMA POR SUCURSAL: ... se originan en los puntos de emisión de su Sistema Computarizado de dicha sucursal. En este caso se puede operar con varias numeraciones correlativas, para cada sucursal" | Numbering topologies: CENTRALIZED — generation for ALL establishments registered in the RTN originates at a single emission point nationwide, operating ONE correlative numbering regardless of head office or branches; REGIONAL — one emission point per region, one correlative numbering per region; PER BRANCH — documents originate at each branch's own emission points, with multiple correlative numberings, one per branch | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 48 p.53 (EV24:EVID-203) |
| LB-005 | Reglamento, Art. 49: "Los puntos de emisión pueden ser: 1. Fijos: Son los puntos ubicados en los establecimientos del Obligado Tributario. 2. Móviles: Son los puntos que se utilizan para ventas itinerantes, y estos ..." [texto continúa — pasaje truncado en la extracción de evidencia; registro bajo un establecimiento per EVID-203 gloss] | Emission points may be: 1. FIXED — points located within the taxpayer's establishments; 2. MOBILE — points used for itinerant sales, [text continues — truncated in the evidence extract; registered under an establishment per the evidence gloss] | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 49 p.54 (EV24:EVID-203) |
| LB-006 | Reglamento, Art. 50: "Son modalidades de impresión: 1. Por Imprenta 2. Autoimpresor" | Printing modalities: 1. print shop; 2. self-printer | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 50 p.54 (EV24:EVID-204) |
| LB-007 | Reglamento, Art. 51: medios (del autoimpresor) = "1. Máquinas Registradoras 2. Sistemas Computarizados 3. Sistemas de Autorización de emisión electrónica" | Means (of the autoimpresor modality): 1. cash registers; 2. computerized systems; 3. electronic-emission authorization systems (SEE) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 51 p.54 (EV24:EVID-204) |
| LB-008 | Reglamento, Art. 52 (máquina registradora): "Programa cerrado que no permita modificaciones o alteraciones de los programas de fábrica ... número correlativo autogenerado, número correlativo de totales y el total de ventas desde que se inicia el uso"; "Unidad de Memoria fiscal fijada al armazón de forma inamovible"; pantalla de reporte; "Cinta o copia para auditoría de los tickets emitidos, anulados y operaciones de corrección o devolución"; teclado | Cash-register specifications: closed factory program allowing no modifications; auto-generated correlative number, totals counter and total sales since first use; fiscal memory unit fixed immovably to the chassis; report display; audit tape/copy of tickets issued, voided and correction/return operations; keyboard | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 52 p.55 (EV24:EVID-204) |
| LB-009 | Reglamento, Art. 53 (sistemas computarizados): "1. El sistema de facturación debe estar integrado al menos a un sistema contable o de inventarios. 2. El software utilizado debe contar con mecanismos de seguridad y controles de auditoría. 3. El software debe garantizar la persistencia y disponibilidad inmediata de la información actual e histórica ... 4. El sistema podrá permitir incorporar la matriz de código bidimensional o tridimensional. 5. El Sistema debe tener la capacidad de generación de archivos tipo texto para su almacenamiento y traslado hacia la Administración Tributaria a través de servicios web o intercambio de protocolo." + "El Obligado Tributario debe presentar Declaración Jurada ante la Administración Tributaria previo a ser autorizado como autoimpresor ... haciendo constar que sus sistemas computarizados cumplen los requisitos" | Computerized-system (SFC) specifications: 1. the invoicing system must be integrated with at least one accounting or inventory system; 2. the software must have security mechanisms and audit controls; 3. the software must guarantee persistence and immediate availability of current and historical information; 4. the system MAY incorporate 2D/3D code matrices; 5. the system must generate text-type files for storage and transfer to the Tax Administration via web services or protocol exchange; the taxpayer must present a sworn declaration to the AT before being authorized as autoimpresor, attesting that its computerized systems meet the requirements | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 53 pp.55-56 (EV24:EVID-204) |
| LB-010 | Reglamento, Art. 54: "Este medio de impresión debe interactuar simultáneamente con los sistemas informáticos de la Administración Tributaria con el fin de obtener el Código de Autorización de Emisión Electrónica (CAEE) y el almacenamiento de la información" | This means of printing (the SEE) must interact SIMULTANEOUSLY with the Tax Administration's information systems in order to obtain the CAEE and the storage of the information | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 54 p.56 (EV24:EVID-204) |
| LB-011 | Reglamento, Art. 55 (contingencia): los obligados "pueden contar con Comprobantes Fiscales y/o Documentos Complementarios preimpresos por una imprenta certificada. En caso de contingencia, si el Obligado Tributario ... no cuenta con formatos preimpresos autorizados y realiza ac..." [texto truncado en la extracción de evidencia — ver OQ-004] | Contingency: taxpayers may hold fiscal/complementary documents preprinted by a certified print shop; in a contingency, if the taxpayer ... does not hold authorized preprinted formats and [carries out ... — text truncated in the evidence extract; see OQ-004] | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 55 p.56 (EV24:EVID-204) |
| LB-012 | Reglamento, Art. 57 (reformado por 609-2017): incorporación obligatoria al medio electrónico de forma GRADUAL, per la calendarización que publique SEFIN/SAR — el texto operativo del artículo no quedó capturado verbatim en la extracción (truncamiento de línea en EVID-204); semántica per cluster E8 + D-H2.6: fila de configuración datada por empresa, `valid_from` = fecha de calendarización | Art. 57 (reformed by 609-2017): mandatory incorporation of the electronic means is GRADUAL, per the calendarization SEFIN/SAR publish — the article's operative text was not captured verbatim in the evidence extract; semantics per cluster E8 + decision D-H2.6: a dated config row per company, `valid_from` = the calendarization date | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 57 p.57 (EV24:EVID-204; verbatim gap → 24_ OQ-4) |
| LB-013 | Reglamento, Art. 58: los procedimientos de operación y la documentación técnica del sistema de emisión electrónica serán emitidos por la Administración Tributaria — INSTRUMENTOS NO PUBLICADOS (lead 1, `24_ OQ-4`; re-chequeo trimestral) | Art. 58: the operating procedures and technical documentation of the electronic emission system are to be issued by the Tax Administration — instruments NOT PUBLISHED (open lead 1, `24_ OQ-4`; quarterly re-check) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 58 p.57 (EV24:EVID-204; 24_ OQ-4) |
| LB-014 | Reglamento, Art. 4 defs.: num. 9 "CÓDIGO DE AUTORIZACIÓN DE EMISIÓN ELECTRÓNICA (CAEE): Es el código único generado por un algoritmo para cada Comprobante Fiscal y/o Documentos Complementarios electrónicos"; num. 22 "FACTURACIÓN ELECTRÓNICA: Es un medio de la modalidad de impresión por autoimpresor, donde los sistemas informáticos del Obligado Tributario interactúan con los sistemas de la Administración Tributaria para crear, transmitir, autorizar, emitir y resguardar los Documentos Fiscales Electrónicos"; num. 35 "PUNTO DE EMISIÓN: Es el lugar determinado por el Obligado Tributario, para emitir los Comprobantes Fiscales y/o Documentos Complementarios autorizados ... Pueden existir uno o más puntos de emisión en cada establecimiento"; num. 40 "SISTEMA DE FACTURACIÓN COMPUTARIZADO (SFC): Es un sistema informático (hardware y software) autorizado por la Administración Tributaria, que permite crear, procesar, ..." [truncado] | Definitions: CAEE = the unique code generated by an algorithm for each electronic fiscal/complementary document; ELECTRONIC INVOICING = a means of the self-printer modality, where the taxpayer's systems interact with the Tax Administration's systems to create, transmit, authorize, issue and safeguard Electronic Fiscal Documents; EMISSION POINT = the place determined by the taxpayer to issue authorized fiscal/complementary documents — one or more emission points may exist per establishment; SFC = a computerized system (hardware and software) authorized by the AT enabling creation, processing, ... [truncated] | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 4 nums. 9/22/35/40 pp.6-12 (EV24:EVID-186) |
| LB-015 | Reglamento, Art. 2: "Las gestiones para la aplicación del presente Reglamento serán desarrolladas de forma eminentemente electrónica, sin perjuicio que la Administración Tributaria disponga de otros medios"; considerandos (pp.2-3) anclan la potestad reglamentaria en D. 17-2010 L-Art. 57 (reformado por CT D. 170-2016 Art. 211.3), CT Arts. 212.2 y 65 | The regime's administration is developed EMINENTLY ELECTRONICALLY, without prejudice to other means the Tax Administration provides; the considerandos anchor the regulatory power in D. 17-2010 Art. 57 (as reformed by Tax Code D. 170-2016 Art. 211.3), CT Arts. 212.2 and 65 — the statutory birth chain of the facturación regime | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 2 p.6 + considerandos pp.2-3 (EV24:EVID-186) |
| LB-016 | Ayuda 76_ (flujo operacional, NO base legal — R-H37: su sección Base Legal cita por error el Art. 42): inscripción por Oficina Virtual — "+ Nuevo punto de emisión"; "Acreditación de imprentas: Introducir el RTN y seleccione el nombre de la imprenta"; "Acreditación de responsables: Introducir el Nombre completo del responsable, correo electrónico, documento de identificación y número de identificación"; selección de documentos fiscales; al finalizar "se le mostrará el formulario SAR-926 'Declaración Jurada de Inscripción al Régimen de Facturación'" | Help 76_ (operational workflow authority ONLY — R-H37: its Base-Legal section mistakenly cites Art. 42): Oficina Virtual inscription — new emission point; print-shop accreditation (enter the print shop's RTN and name); accreditation of responsible persons (full name, email, identification document type and number); fiscal-document selection; finishing renders Form SAR-926, Sworn Declaration of Inscription to the Facturación Regime | `hn/sources/76_Ayuda_inscripcion_facturacion.pdf` | pp.5-10 (EV24:EVID-212; R-H37) |

## 3. Functional Requirements

### 3.1 Inscription and the declared matrix (R-Art. 45; SAR-926)

- **HN-EINV-FR-141:** The system shall model the company's inscription in the
  *Régimen de Facturación* as a registration record holding the statutory
  prerequisites — updated RTN data, *contrato de adhesión* (adhesion
  contract) acceptance, and the SAR filing reference (Form SAR-926
  *Declaración Jurada de Inscripción*) — with registration state
  (draft/registered) gating emission configuration. (LB-001; LB-016; EV24:EVID-203/212)
- **HN-EINV-FR-142:** The system shall capture the inscription's declared
  matrix across its four statutory dimensions — *Modalidades de Impresión* ×
  Comprobantes Fiscales/Documentos Complementarios (document types) ×
  *Establecimientos* × *Puntos de Emisión* — complete only when every
  dimension is declared and internally consistent (each document type mapped
  to a modality; each punto attached to an establecimiento). (LB-001; EV24:EVID-203)
- **HN-EINV-FR-143:** The system shall store, per establecimiento and punto
  de emisión, the SAR-assigned registration codes produced at inscription
  (casa matriz = 000) — the two 3-digit location segments of the document
  identifier whose grammar is owned by `01_document-types-numbering.md`
  (HN-EINV-FR-001..031). (LB-001; LB-014 num. 35; EV24:EVID-203/186)
- **HN-EINV-FR-144:** The system shall reproduce the Oficina Virtual
  inscription e-workflow surfaces so the declared matrix transcribes without
  restructuring: new emission point entry, *acreditación de imprentas*
  (print-shop accreditation: imprenta RTN + name), fiscal-document selection,
  and the SAR-926 filing as registration artifact. (LB-016; EV24:EVID-212)
- **HN-EINV-FR-145:** The system shall surface the inscription's solvency
  prerequisite ("estar al día") from the RTN-suspension regime owned by
  `../taxation/01_isr-framework.md` (HN-TAX-FR-001..045): while the RTN is
  suspended, inscription finalization is blocked and the state shown on the
  registration record. (LB-001; EV24:EVID-203)

### 3.2 Modalidades, medios and the imprenta-exclusivity guard (R-Arts. 46-47, 50-51)

- **HN-EINV-FR-146:** The system shall model exactly two *modalidades de
  impresión* — 1. *Por Imprenta* and 2. *Autoimpresor* — selected per company
  and per declared document type, and shall treat *facturación electrónica*
  as a MEDIUM of the autoimpresor modality (def. 22: the taxpayer's systems
  interact with SAR's to create, transmit, authorize, emit and safeguard
  electronic documents), never a separate transmission regime. (LB-006; LB-014 num. 22; EV24:EVID-204/186)
- **HN-EINV-FR-147:** The system shall model the three *medios* of the
  autoimpresor modality — 1. *Máquinas Registradoras*, 2. *Sistemas
  Computarizados*, 3. *Sistemas de Autorización de emisión electrónica*
  (SEE) — each with its own registration granularity (FR-150/151; SEE =
  FR-166..169). (LB-007; EV24:EVID-204)
- **HN-EINV-FR-148:** The system shall enforce the imprenta-exclusivity
  guard: *Factura Prevalorada* (pre-valued invoice, code 10), *Recibo por
  Honorarios Profesionales* (professional fees receipt, code 04) and
  *Constancia de Donación* (donation certificate, code 12) are emittable ONLY
  under the imprenta modality — excluded from autoimpresor inscription
  (Art. 47); Prevalorada/RHP expressly imprenta-exclusive (Art. 46) — with no
  autoimpresor or SEE emission path. (LB-002; LB-003; EV24:EVID-203)
- **HN-EINV-FR-149:** For each declared punto under the imprenta modality,
  the system shall record the accredited imprenta(s) — RTN and name, as
  captured at inscription — cross-referenced against the CAI/rango ledger of
  `02_cai-ledger-emission-gate.md` (HN-EINV-FR-046..090). (LB-016; EV24:EVID-212)

### 3.3 Per-device and per-system registration (R-Art. 47)

- **HN-EINV-FR-150:** For taxpayers using *máquinas registradoras*, the
  system shall register EACH dispositivo as its own punto de emisión, with
  the establecimiento where it is installed — the per-device granularity
  Art. 61 rango authorization rides (ledger in `02_...`). (LB-003; EV24:EVID-203)
- **HN-EINV-FR-151:** For taxpayers using *sistemas computarizados*, the
  system shall register each system — software identification, the
  establecimiento hosting the server, and its puntos de emisión — classified
  as *Sistema Computarizado Independiente* (standalone) or *en Red*
  (networked); rango authorization granularity = per system × document type
  (Art. 61, ledger in `02_...`). (LB-003; EV24:EVID-203)

### 3.4 The emission-point entity: fijo and móvil (R-Art. 49; def. 35; D-H1)

- **HN-EINV-FR-152:** The system shall implement the punto de emisión as a
  first-class emission-point entity NOT living on `account.journal` (D-H1):
  carried on the fiscal document (move), it feeds the sequences; one or more
  puntos may exist per establecimiento; each *punto fijo* (fixed emission
  point) sits within a declared establecimiento. ("Caja" = implementation
  vocabulary; the statute says punto de emisión.) (LB-014 num. 35; LB-005; D-H1; EV24:EVID-186/203)
- **HN-EINV-FR-153:** The system shall support *puntos móviles* (mobile
  emission points) for *ventas itinerantes* (itinerant sales), each
  registered under a parent establecimiento; emission from a móvil punto
  carries the parent registration while permitting emission off-site
  (transport interplay owned by `03_...`). (LB-005; EV24:EVID-203)

### 3.5 Numbering topologies and the D-H1 sequence-key reconciliation (R-Art. 48)

- **HN-EINV-FR-154:** The system shall offer a per-company topology selector
  for sistema-computarizado numbering — *Sistema Centralizado*, *Sistema
  Regional*, *Sistema por Sucursal* — constraining sequence assignment and
  validated against the declared matrix (centralizado ⇒ exactly one system
  emission point company-wide; regional ⇒ one per configured region; por
  sucursal ⇒ ≥1 per sucursal). (LB-004; EV24:EVID-203)
- **HN-EINV-FR-155:** Under *Sistema Centralizado*, the system shall generate
  documents for ALL establecimientos registered in the RTN from the single
  nationwide punto, operating ONE correlativo per document type regardless of
  casa matriz or sucursales: the D-H1 sequence key collapses its
  establecimiento segment to the single punto's registered establecimiento
  code, so any warehouse's documents consume the same sequence (which code
  prints for non-parent establishments → OQ-003). (LB-004; EV24:EVID-203)
- **HN-EINV-FR-156:** Under *Sistema Regional*, the system shall operate one
  correlativo per document type per region — a single emission point serving
  all the company's establecimientos in that region — with regions held as
  configuration data (the statute does not define the region unit → OQ-005). (LB-004; EV24:EVID-203)
- **HN-EINV-FR-157:** Under *Sistema por Sucursal*, the system shall operate
  each sucursal's own puntos with their own correlativos ("varias
  numeraciones correlativas, para cada sucursal") — the general case matching
  the full D-H1 sequence key (warehouse, emission point, document type). (LB-004; EV24:EVID-203)
- **HN-EINV-FR-158:** The system shall map establecimiento → `stock.warehouse`
  (company-level branch, casa matriz = 000; NOT `stock.location`) and punto de
  emisión → a child emission-point entity of the warehouse (D-H1); the
  emission point on a move, with the document type
  (`l10n_latam.document.type`), resolves the sequence — never the journal;
  topology (FR-154) sets how the warehouse dimension enters that resolution
  (collapsed under centralizado/regional, full under por sucursal). (LB-014 num. 35; LB-004; D-H1; EV24:EVID-186/203)

### 3.6 SFC specifications and the DJ attestation (R-Art. 53)

- **HN-EINV-FR-159:** The system shall satisfy SFC specification 1 — the
  facturación system integrated with at least one accounting or inventory
  system — natively, exposing the integration as compliance evidence for the
  attestation flow (FR-164). (LB-009 num. 1; EV24:EVID-204)
- **HN-EINV-FR-160:** The system shall satisfy SFC specification 2 —
  security mechanisms and audit controls over fiscal documents: access
  control on emission points (FR-172..173), change tracking, and the fiscal
  lock rules owned by `02_...`/`03_...`. (LB-009 num. 2; EV24:EVID-204)
- **HN-EINV-FR-161:** The system shall satisfy SFC specification 3 —
  persistence and immediate availability of current and historical fiscal
  information, with no purge inside the Código Tributario prescription
  windows (custody owned by the sibling files). (LB-009 num. 3; EV24:EVID-204)
- **HN-EINV-FR-162:** The system shall support SFC specification 4 as
  facultative capability — 2D/3D code matrices (QR/barcode optional per
  R-Art. 36; print handling in `03_document-mechanics.md`) — never
  mandatory. (LB-009 num. 4; EV24:EVID-204)
- **HN-EINV-FR-163:** The system shall provide an export surface satisfying
  SFC specification 5 — text-type files carrying fiscal information for
  storage and transfer toward SAR via web services or protocol exchange —
  with format, endpoint and protocol held as configuration data (the
  SAR-side target is UNPUBLISHED, OQ-001). (LB-009 num. 5; EV24:EVID-204)
- **HN-EINV-FR-164:** The system shall generate the *Declaración Jurada*
  artifact required before authorization as autoimpresor — attesting that
  the computerized systems meet the Art. 53 requirements — pre-filled from
  the declared matrix and system registry (FR-151), for signature by the
  Obligado Tributario. (LB-009; EV24:EVID-204)

### 3.7 Máquina registradora device registry (R-Art. 52)

- **HN-EINV-FR-165:** The system shall hold the máquina registradora device
  registry with the Art. 52 configuration-relevant invariants — closed
  factory program (no alterations), autogenerado correlativo with totals
  counters, non-removable fiscal memory unit, per-device *cinta de
  auditoría* (audit tape) reference — as registration metadata for
  mixed-media taxpayers; numbering/tape mechanics are owned by `01_`/`03_`
  (Odoo operates as sistema computarizado, never a máquina registradora). (LB-008; EV24:EVID-204)

### 3.8 SEE / CAEE — statutory placeholder contract (R-Arts. 50-58) — CONFIG-GAPPED, BLOCKED

The SEE sub-cluster is BLOCKED on open lead 1 (`24_ OQ-4`): Art. 57's
calendarización and Art. 58's operating procedures/technical documentation
are unpublished. The FRs below implement ONLY what the reglamento states;
every transport, message, algorithm and deadline parameter is unresolved
configuration.

- **HN-EINV-FR-166:** The system shall implement the SEE as a CONFIG-GAPPED
  placeholder: a per-document interaction acquiring the CAEE (LB-014 num. 9 —
  the unique algorithmic code per electronic document) through simultaneous
  interaction with SAR's systems per Art. 54; all integration parameters
  remain empty blocked configuration until the Art. 58 instruments are
  acquired (OQ-001; quarterly re-check). (LB-010; LB-014 num. 9; LB-013; EV24:EVID-204/186)
- **HN-EINV-FR-167:** The system shall reserve, per electronic document, a
  CAEE storage field (unique per document) and an emission-state placeholder
  covering the def.-22 lifecycle verbs (create, transmit, authorize, emit,
  safeguard) WITHOUT inventing state semantics — no transition, validation or
  deadline activates before the Art. 58 documentation is acquired; the
  placeholder renders visibly as blocked. (LB-014 num. 22; LB-010; EV24:EVID-186/204)
- **HN-EINV-FR-168:** The system shall store the Art. 57 gradual mandate as
  DATED per-company config rows (D-H2.6): `valid_from` = the calendarización
  date each company is scheduled for (per SAR/SEFIN notification), scope =
  the document types covered, source-instrument reference, `valid_to`
  backfilled only when a successor arrives; no guessed default dates — rows
  exist only when the notification is recorded. (LB-012; EV24:EVID-204)
- **HN-EINV-FR-169:** From its mandate row's `valid_from`, the system shall
  route the company's in-scope document types to the electronic path; since
  that path is blocked (FR-166), an active mandate surfaces as a blocking
  compliance alert rather than silently emitting in another modality — the
  statutory contingency fallback (FR-170/171) remains available. (LB-012; LB-011; EV24:EVID-204)

### 3.9 Contingencia: switch to imprenta preprinted stock (R-Art. 55)

- **HN-EINV-FR-170:** The system shall support contingency emission by
  switching the affected punto/documents to the imprenta modality: documents
  preprinted by a certified imprenta under an authorized, unexhausted rango
  whose vigencia covers the emission date shall pass the emission gate (gate
  owned by `02_...`); each contingency document records the modality used
  and the reason. (LB-011; EV24:EVID-204)
- **HN-EINV-FR-171:** The system shall maintain a contingency-readiness
  surface (operational, non-statutory): per autoimpresor/SEE operation,
  whether preprinted stock exists — derived from the CAI ledger (02) as an
  authorized rango with remaining numbers and live vigencia — warning when
  operation lacks imprenta fallback; the Art. 55 consequences of NOT
  holding stock are partially evidenced (truncated passage → OQ-004) and
  shall not be guessed into configuration. (LB-011; EV24:EVID-204)

### 3.10 Acreditación de responsables — operational, NON-STATUTORY (76_ hook)

- **HN-EINV-FR-172:** The system shall implement a user ↔ emission-point
  authorization matrix as an OPERATIONAL internal-control feature, explicitly
  labeled NON-STATUTORY in its documentation (the reglamento imposes no
  operator restrictions; hook = the Oficina Virtual *acreditación de
  responsables* inscription practice), restricting which users emit from
  which puntos. (LB-016; D-H1; EV24:EVID-212)
- **HN-EINV-FR-173:** The system shall seed the authorization matrix from the
  responsible-persons registry captured at inscription (full name, email,
  identification document type and number — FR-144), with later
  accreditations/de-accreditations as dated rows. (LB-016; EV24:EVID-212)

### 3.11 Emission-point lifecycle and matrix change discipline

- **HN-EINV-FR-174:** The system shall support deactivating (baja de) an
  emission point: deactivated puntos block new emissions immediately while
  historical documents keep their reference; deactivation surfaces the
  no-utilizados duty for the punto's unused documents (cause 5, generator
  in `02_...`). (LB-014 num. 35; EV24:EVID-203/202)
- **HN-EINV-FR-175:** The system shall record every change to the declared
  matrix (new puntos, modality or topology changes, device/system
  registrations) as additive dated configuration rows per D-H2.1 —
  `valid_from` = the declaration date, never replaced in place — so
  historical documents resolve against the matrix in force at their emission
  dates. (LB-001; D-H2.1; EV24:EVID-203)

## 4. Data Model

No machine-readable sidecar ships with this file: every catalog here is an
in-model select or blocked SEE configuration (OQ-001).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.facturation.registration | company_id | m2o res.company | — | FR-141 |
| l10n_hn.facturation.registration | state | select | draft · registered | FR-141; AC-001 |
| l10n_hn.facturation.registration | sar_926_ref / inscription_date | char / date | Form SAR-926 filing reference | FR-141/144; LB-016 |
| l10n_hn.facturation.registration | adhesion_contract | boolean | contrato de adhesión accepted | FR-141; LB-001 |
| l10n_hn.facturation.registration | solvency_state | related | from RTN-suspension regime (taxation/01 crossref) | FR-145 |
| l10n_hn.emission.point | name / code | char / char(3) | SAR-assigned punto segment | FR-143/152 |
| l10n_hn.emission.point | type | select | fijo · móvil | FR-152/153; LB-005 |
| l10n_hn.emission.point | warehouse_id | m2o stock.warehouse | establecimiento (casa matriz = 000); NOT stock.location (D-H1) | FR-152/158 |
| l10n_hn.emission.point | medio | select | imprenta · maquina_registradora · sistema_computarizado · see | FR-147; LB-007 |
| l10n_hn.emission.point | device_serial | char | máquina registradora dispositivo (own punto per Art. 61) | FR-150/165 |
| l10n_hn.emission.point | computer_system_id | m2o l10n_hn.computer.system | — | FR-151 |
| l10n_hn.emission.point | imprenta_ids | m2m res.partner | accredited imprentas (RTN + name) | FR-149; LB-016 |
| l10n_hn.emission.point | region_id | m2o l10n_hn.region | regional topology grouping (OQ-005) | FR-156 |
| l10n_hn.emission.point | active / valid_from / valid_to | bool / date | dated config rows (D-H2.1) | FR-174/175 |
| l10n_hn.computer.system | name / kind | char / select | sistema computarizado: independiente · en_red | FR-151; LB-003 |
| l10n_hn.computer.system | software_ref | char | software identification | FR-151 |
| l10n_hn.computer.system | server_warehouse_id | m2o stock.warehouse | establecimiento hosting the server | FR-151 |
| l10n_hn.emission.point.responsible | emission_point_id / user_id | m2o / m2o res.users | NON-STATUTORY matrix (labeled) | FR-172/173 |
| l10n_hn.emission.point.responsible | full_name / email / id_type / id_number | char | acreditación de responsables capture (76_) | FR-173; LB-016 |
| l10n_hn.see.mandate | company_id / valid_from / valid_to | m2o / date / date | DATED mandate rows; valid_from = calendarización date (D-H2.6) | FR-168; LB-012 |
| l10n_hn.see.mandate | scope_doc_type_ids | m2m l10n_latam.document.type | in-scope document types | FR-168 |
| l10n_hn.see.mandate | source_instrument / state | char / select | SAR/SEFIN notification ref; blocked · active | FR-168/169; OQ-001 |
| res.company | l10n_hn_numbering_topology | select | centralizado · regional · por_sucursal | FR-154; LB-004 |
| account.move | l10n_hn_emission_point_id | m2o l10n_hn.emission.point | on the MOVE, never the journal (D-H1) | FR-152/158 |
| account.move | l10n_hn_emission_modality | select | imprenta · autoimpresor | FR-170 |
| account.move | l10n_hn_contingency_reason | char | set when modality switched | FR-170 |
| account.move | l10n_hn_caee | char | RESERVED, blocked — per-document code (def. 9) | FR-167; OQ-001 |

## 5. Odoo Mapping

Layer semantics per [saas-thin-client-architecture.md]: HN has no
transmission regime today, so all surfaces in this file are `odoo`-layer
configuration and data model; the future SEE connector is expected SaaS-side
like SV's MH connector — hence its rows are `n/a` (blocked). Model names are
stable across Odoo 17/18/19/20; nothing requires version-specific behavior.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-141 | odoo | l10n_hn.facturation.registration (new) | state, sar_926_ref, adhesion_contract | New entity; identical 17-20 |
| FR-142 | odoo | l10n_hn.facturation.registration + children | declared matrix constraints | Completeness constraint at registration finalize |
| FR-143 | odoo | l10n_hn.emission.point / stock.warehouse | code | Warehouse carries the establecimiento code (casa matriz 000); segments feed `01_`'s grammar |
| FR-144 | odoo | l10n_hn.facturation.registration | workflow surfaces | Mirrors Oficina Virtual intake (76_); SAR-926 artifact = report/template |
| FR-145 | odoo | l10n_hn.facturation.registration | solvency_state | Crossref to taxation/01 HN-TAX-FR-001..045 (CT Art. 164 regime); no suspension logic here |
| FR-146 | odoo | l10n_latam.document.type + config | modality flag | One journal per company (D-H1); modality lives on document-type config, not journal |
| FR-147 | odoo | l10n_hn.emission.point | medio | SEE medio = placeholder only (FR-166) |
| FR-148 | odoo | l10n_latam.document.type | imprenta-exclusive flag | Hard guard for codes 10/04/12; no autoimpresor/SEE path |
| FR-149 | odoo | l10n_hn.emission.point | imprenta_ids | Feeds ledger cross-check in `02_` |
| FR-150 | odoo | l10n_hn.emission.point | device_serial + warehouse_id | One punto per dispositivo (Art. 61 granularity) |
| FR-151 | odoo | l10n_hn.computer.system (new) | kind, software_ref, server_warehouse_id | New entity; identical 17-20 |
| FR-152 | odoo | l10n_hn.emission.point (new) + account.move | l10n_hn_emission_point_id | D-H1: NOT on account.journal; emission point feeds sequences via move |
| FR-153 | odoo | l10n_hn.emission.point | type=móvil, parent warehouse | Itinerant sales; guía interplay in `03_` |
| FR-154 | odoo | res.company | l10n_hn_numbering_topology | Constraint vs declared matrix at registration |
| FR-155 | odoo | sequence resolution | warehouse-segment collapse | Centralizado: one sequence per doc type company-wide; printed segment → OQ-003 |
| FR-156 | odoo | l10n_hn.region (new) + sequence resolution | region_id | Region unit = config data (OQ-005) |
| FR-157 | odoo | sequence resolution | full key | General case: (warehouse, emission point, doc type) |
| FR-158 | odoo | stock.warehouse + l10n_hn.emission.point + l10n_latam.document.type | sequence key | D-H1 design guidance; establecimiento = warehouse NOT stock.location |
| FR-159 | odoo | (native) | — | Odoo accounting/inventory integration is native; evidence surface for FR-164 |
| FR-160 | odoo | (existing security surfaces) + FR-172 matrix | — | Audit controls; document locks owned by `02_`/`03_` |
| FR-161 | odoo | (native retention) | — | No purge inside CT prescription windows; custody in sibling files |
| FR-162 | odoo | (optional QR fields in `03_`) | — | Facultative "podrá"; never enforced |
| FR-163 | odoo | export surface | text-file export | Format/endpoint = config; SAR target unpublished (OQ-001) |
| FR-164 | odoo | report/template on registration | DJ artifact | Pre-filled from matrix + system registry |
| FR-165 | odoo | l10n_hn.emission.point | device metadata | Registry metadata only; Odoo is SFC, never a máquina registradora |
| FR-166 | n/a | — | — | BLOCKED: Art. 58 technical docs unpublished (24_ OQ-4); when acquired, connector expected saas-side per thin-client architecture |
| FR-167 | odoo | account.move | l10n_hn_caee (reserved) | Field reserved, write-blocked; no state machine until OQ-001 resolves |
| FR-168 | odoo | l10n_hn.see.mandate (new) | dated rows | D-H2.6; valid_from = calendarización per company; no defaults |
| FR-169 | odoo | l10n_hn.see.mandate + registration | gating alert | Active mandate + blocked path = blocking alert; contingency remains |
| FR-170 | odoo | account.move + emission gate (`02_`) | l10n_hn_emission_modality, l10n_hn_contingency_reason | Per-document modality switch; gate itself owned by `02_` |
| FR-171 | odoo | derived from CAI ledger (`02_`) | readiness flag | Operational derivation; no statutory stock mandate encoded (OQ-004) |
| FR-172 | odoo | l10n_hn.emission.point.responsible (new) | user ↔ punto matrix | NON-STATUTORY label in model help/docs; hook = 76_ acreditación |
| FR-173 | odoo | l10n_hn.emission.point.responsible | dated rows | Seeded from inscription capture |
| FR-174 | odoo | l10n_hn.emission.point | active=False | Blocks emission; surfaces cause-5 notification (generator in `02_`) |
| FR-175 | odoo | all matrix entities | valid_from/valid_to | D-H2.1 additive rows; historical resolution at emission date |

## 6. Acceptance Criteria

- **AC-001:** Given a registration declaring modality and document types but
  no emission point on any establecimiento, when finalizing, then it is
  rejected until all four matrix dimensions are consistent (FR-142).
- **AC-002:** Given a declared matrix attempting autoimpresor modality for
  Factura Prevalorada, RHP or Constancia de Donación, when saving, then the
  combination is rejected with the imprenta-exclusivity explanation (FR-148).
- **AC-003:** Given registration of a second máquina registradora dispositivo
  in establecimiento 002, when saved, then a NEW emission point is created
  under warehouse 002 carrying the device serial (FR-150).
- **AC-004:** Given topology centralizado with the single punto under
  establecimiento 000, when facturas are emitted from warehouses 001 and 003,
  then both consume the same Factura sequence and identifier prefix (FR-155).
- **AC-005:** Given topology regional with regions Norte (warehouses 001,
  002) and Sur (003), when facturas are emitted from all three, then 001/002
  share one correlativo and 003 consumes another (FR-156).
- **AC-006:** Given topology por sucursal, when facturas are emitted from two
  sucursales' puntos, then each consumes its own sequence keyed by the full
  (warehouse, emission point, document type) triple (FR-157).
- **AC-007:** Given a punto móvil under establecimiento 001, when an
  itinerant sale is invoiced off-site, then the move carries the móvil punto
  and its parent registration (FR-153).
- **AC-008:** Given the SFC compliance checklist, when generated, then
  specification 1 reflects the live Odoo accounting/inventory integration;
  given a period's fiscal documents, when the text-file export runs, then
  text-type files are produced with format/endpoint read from configuration
  (FR-159/163).
- **AC-009:** Given a completed declared matrix and system registry, when the
  DJ attestation is generated, then it is pre-filled and rendered for
  signature (FR-164).
- **AC-010:** Given the SEE placeholder, when any path attempts CAEE
  acquisition, then it is visibly blocked citing the unpublished Art. 58
  documentation (OQ-001), and no CAEE state transitions exist (FR-166/167).
- **AC-011:** Given a mandate row valid_from = 2027-01-01 for Factura, when
  emission is attempted 2026-12-15, then no electronic routing applies; when
  attempted 2027-01-05 with the SEE path blocked, then a blocking compliance
  alert is raised (contingency excepted) (FR-168/169).
- **AC-012:** Given an autoimpresor punto under contingency with a valid
  imprenta rango covering today, when a factura is posted with the modality
  switched, then it passes the gate and records modality imprenta plus the
  contingency reason (FR-170).
- **AC-013:** Given a user not accredited to punto P, when the user attempts
  to emit from P, then emission is blocked by the authorization matrix, whose
  documentation states its non-statutory character (FR-172).
- **AC-014:** Given an emission point deactivated today, when emission is
  attempted tomorrow, then it is blocked, historical documents keep their
  references, and the cause-5 notification duty is surfaced (FR-174).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Carried register `24_ OQ-4` [LEAD]: SEE calendarización (Art. 57) + Art. 58 operating procedures/technical documentation UNPUBLISHED — ALL SEE/CAEE FRs (FR-166..169) are config-gapped placeholders on the reglamento's own text; re-check SAR /facturacion/ + wp-search quarterly. Also blocks the Art. 57 verbatim recovery noted in LB-012. | yes (SEE sub-cluster only) | acquisition wave / controller | open |
| OQ-002 | Carried register `76-78_ OQ-2` [LEAD]: SAR-924/SAR-926/SAR-927 form prints not in corpus (rendered inside the Oficina Virtual); acquire only if field-level fidelity is needed for the SAR-926 inscription export (FR-144) or the authorization request surfaces. | no | acquisition wave | open |
| OQ-003 | Centralizado printed segment: with ONE correlativo for many establecimientos, which establecimiento code prints in the 16-digit identifier for documents generated at non-parent establishments — the punto's registered establecimiento (default per D-H1 collapse, FR-155) or the emitting establishment? Corpus silent; verify vs SAR validador / real centralizado invoices. | no | Takumi + product owner | open |
| OQ-004 | R-Art. 55 truncation: the consequence branch for contingencies when the taxpayer does NOT hold authorized preprinted formats ("...no cuenta con formatos preimpresos autorizados y realiza ac[...]") is truncated in the evidence extract — re-extract p.56 before encoding any stock-mandate behavior (FR-171 written conservatively). | no | Takumi (re-extraction) | open |
| OQ-005 | Region unit for SISTEMA REGIONAL: the statute does not define how regions are constituted or registered with SAR; model as configuration (FR-156) and confirm against SAR practice / a real regional taxpayer. | no | Takumi + product owner | open |
| OQ-006 | Arts. 56-58 verbatim coverage: the evidence entry (EVID-204) lists Art. 56 in its locus but quotes no text, and Arts. 57-58 are gloss-level only; confirm at re-extraction that nothing inside E8 scope sits in the unquoted passages (esp. Art. 56). | no | Takumi (re-extraction) | open |
| OQ-007 | Acreditación de responsables granularity: 76_ captures responsible persons at inscription, but whether SAR's practice binds them per emission point or per company is not shown; the matrix (FR-172) models per-punto binding — verify against the Oficina Virtual intake when field-level fidelity lands (kin OQ-002). | no | Takumi | open |
| OQ-008 | Truncated-passage re-extraction queue (V-HN1, kin of OQ-004/OQ-006): (a) Art. 49 móvil text breaks mid-sentence in LB-005 (registration-under-establecimiento reading rides the EVID-203 gloss only); (b) Art. 4 num. 40 SFC definition breaks mid-sentence in LB-014; (c) file 02's LB-014 Art. 40 no-utilizados anchor carries the same truncation class. Re-extract `24_` pp.54/6-12 and the Art. 40 zone before implementing FR-153/FR-079 verbatim-critical paths. | no | extraction queue | open |
