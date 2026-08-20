# HN — E-Invoicing — CAI/rango authorization ledger, emission gate, lifecycle & imprenta regime

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN2 + controller |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the heart of Honduras'
paper-based facturación regime — clusters **E3** and **E7** of the master
index under the *Reglamento del Régimen de Facturación, Otros Documentos
Fiscales y Registro Fiscal de Imprentas* (Acuerdo 481-2017 consolidado).
E3 owns: the *Clave de Autorización de Impresión* (CAI, print-authorization
key) ledger and its distinction from the CAEE; the *rango autorizado*
(authorized range) as a taxpayer-requested QUANTITY with SAR
limit/condition overlay; the ledger key — statutory (punto de emisión ×
document type) with dispositivo/sistema granularity, reconciled with D-H1's
(establecimiento → `stock.warehouse`, punto de emisión → child emission
point, document type → `l10n_latam.document.type`) sequence key and the
centralizado one-correlativo-for-many-establishments topology; the
ONE-active-rango-until-exhaustion rule; the T-2-month renewal window;
*vigencia* (validity) ≤ 1 year as dated rows (2 years pre-2018); the SAR
limit/condition/cancellation states of Art. 63; the print-authorization
state chain (Pendiente de Aceptación → Solicitada → Autorizada → ACTIVADA
→ vencida/cancelada, forms SAR-924/SAR-927) with consumption starting only
at ACTIVADA; the *momento de emisión* (moment of issuance) earliest-of
family (Art. 14) as gate input; and the **D-H2.2 HARD emission gate** — a
fiscal document cannot be posted unless its date resolves to a CAI rango
whose vigencia covers it for that (establecimiento, punto de emisión,
document type), with NO supervisor override and backdating only inside a
historically-valid range. E7 owns the lifecycle events: ANULADA void
marking + prescription custody; the 12-cause *no-utilizados* (unused
documents) notification within the first 10 días hábiles of the following
month (cause 1 = vigencia expiry, AUTOMATIC — the ledger monitor);
*uso temporal* (temporary use); and the *Registro Fiscal de Imprentas*
(fiscal registry of print shops) — requisites, 2-year certificate, T-6-month
renewal, obligaciones, prohibitions — as customer-side data and invariants.
Honduras has NO XML/DTE transmission regime: this emission gate is HN's
functional counterpart to SV's transmission gate (there is nothing else to
gate).

FR range HN-EINV-FR-046..090 is owned by this file; FR-046..084 are used,
FR-085..090 stay reserved. It does **not** cover: document taxonomy, type
codes and the correlativo grammar (`01_document-types-numbering.md`,
HN-EINV-FR-001..031 — wrap/FY-continuum rules consumed by id);
per-document print content and the FORMAT-layer placement of CAI/fecha
límite/rango (`03_document-mechanics.md`, HN-EINV-FR-091..140 — its FR-093
print quad consumes this ledger); inscription, topologies, medios, SEE/CAEE
and contingencia (`04_registration-topologies-medios-see.md`,
HN-EINV-FR-141..175 — device/system registration and the SEE placeholder
live there); retention rates (`../taxation/04_isr-withholding.md`);
prescription horizons themselves (`../taxation/01_isr-framework.md`,
HN-TAX-FR-001..045, FR-040 — crossref only); and DMC/DJIMR export surfaces
(S-HN3 wave).

## 2. Legal Basis

Authority order (binding, per master evidence index): `24_` (Acuerdo
481-2017 consolidado, effective 31-dic-2017) > `25_` (Acuerdo 189-2014,
HISTORICAL — repealed by R-Art. 78; supplies the pre-2018 2-year vigencia
rows). Helps `77_/78_` are operational-workflow authority ONLY — their
Base-Legal sections are DEFECTIVE, so every LB cites the reglamento
R-Arts and marks the helps as operational corroboration (R-H37 binding).
D-H1 (ledger/sequence key; never journal), D-H2 (dated rows; resolution by
domain date; D-H2.2 hard gate) and D-H3 (historical ingestion depths) bind
every row below.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglamento 481-2017, Art. 4 defs. 7 y 9: "CLAVE DE AUTORIZACIÓN DE IMPRESIÓN (CAI): Es una serie alfanumérica generado electrónicamente por la Administración Tributaria para autenticar el Procedimiento de Autorización de Impresión." / "CÓDIGO DE AUTORIZACIÓN DE EMISIÓN ELECTRÓNICA (CAEE): Es el código único generado por un algoritmo para cada Comprobante Fiscal y/o Documentos Complementarios electrónicos." | CAI = alphanumeric series generated electronically by the Tax Administration to authenticate the Print Authorization Procedure; CAEE = unique per-document algorithmic code for ELECTRONIC documents (SEE medium) — the two authorization artifacts are distinct | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 4 nums. 7/9 pp.6-7 (EV24:EVID-186) |
| LB-002 | Reglamento, Art. 4 defs. 35 y 36: "PUNTO DE EMISIÓN: Es el lugar determinado por el Obligado Tributario, para emitir los Comprobantes Fiscales y/o Documentos Complementarios autorizados por la Administración Tributaria. Pueden existir uno o más puntos de emisión en cada establecimiento." / "RANGO AUTORIZADO: Es la cantidad de Comprobantes Fiscales y/o Documentos Complementarios autorizados por la Administración Tributaria, el cual es definido por el Obligado Tributario al momento de la solicitud de la autorización de impresión, sin perjuicio de las limitaciones o condiciones que la Administración Tributaria disponga." | Emission point = the place determined by the taxpayer to issue authorized documents (one or more per establishment); AUTHORIZED RANGE = the QUANTITY of documents authorized, DEFINED BY THE TAXPAYER at the moment of the solicitud, without prejudice to the limitations or conditions the Tax Administration may impose | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 4 nums. 35/36 pp.10-11 (EV24:EVID-186; def. 35 kin file 04 LB-014) |
| LB-003 | Reglamento, Art. 59: "La autorización de impresión y vigencia será eminentemente electrónica ... La autorización será por punto de emisión y por tipo de documento, estableciendo el rango de la numeración correlativa. El Obligado Tributario podrá realizar una sola solicitud de autorización de impresión y vigencia por punto de emisión hasta agotar los documentos autorizados, dentro de los dos (2) meses previos a la fecha límite de emisión o regularice su situación tributaria en caso de denegatoria." | Authorization is eminently electronic; granted PER EMISSION POINT and PER DOCUMENT TYPE, establishing the range of the correlative numbering; the taxpayer may file a SINGLE solicitud per emission point UNTIL the authorized documents are exhausted, within the TWO (2) MONTHS prior to the emission deadline, or regularize its situation in case of denial | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 59 p.57 (EV24:EVID-205) |
| LB-004 | Reglamento, Art. 61 (autoimpresores): máquina registradora — "la autorización será por cada dispositivo, estableciendo el rango de la numeración correlativa en la forma establecida del Artículo 17 numeral 4)"; sistema computarizado — "la autorización será por cada Sistema y tipo de Comprobantes Fiscales y/o Documentos Complementarios" | Autoimpresor granularity: cash registers authorized PER DEVICE with the range established in the Art. 17.4 machine-numbering form; computerized systems authorized PER SYSTEM and per document type | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 61 p.59 (EV24:EVID-205) |
| LB-005 | Reglamento, Art. 62: "La Administración Tributaria autorizará la impresión y vigencia ... por un plazo máximo de un (1) año. Los Comprobantes ... perderán su validez y no podrán ser utilizados cuando se haya vencido el plazo de tiempo autorizado." | SAR authorizes printing and vigencia for a MAXIMUM of ONE (1) YEAR; documents LOSE THEIR VALIDITY and MAY NOT BE USED once the authorized time period has expired — the statutory anchor of the hard emission gate | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 62 p.59 (EV24:EVID-205) |
| LB-006 | Reglamento, Art. 63: criterios de comportamiento tributario (RTN currency; formal/material compliance; "Deudas líquidas firmes y exigibles pendientes de pago"; pending procedures) → "podrá limitar y/o condicionar la autorización" + "podrá cancelar la vigencia de las autorizaciones otorgadas cuando se compruebe inconsistencias o alteraciones" | Tax-conduct criteria (current RTN; formal/material compliance; liquid, firm and due pending debts; pending procedures) → SAR may LIMIT and/or CONDITION the authorization, and may CANCEL the vigencia of granted authorizations when inconsistencies or alterations are proven | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 63 p.59 (EV24:EVID-205) |
| LB-007 | Reglamento, Art. 64: on rejection, the taxpayer has 10 días hábiles to regularize its situación tributaria or request verificación [operación resumida en el glosa de EVID-205; texto verbatim no capturado — verificar contra el PDF al implementar] | On denial, 10 business days to regularize or request verification (verbatim gap flagged; semantics per evidence gloss) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 64 p.60 (EV24:EVID-205) |
| LB-008 | Reglamento, Art. 14 (momento de emisión): "1. En la venta de bienes incluyendo las exportaciones, en el momento de la entrega del bien o en la fecha de pago al contado o en la que se otorgue al crédito (devengo), lo que suceda primero, aunque se haya pactado reserva de dominio, pacto de retroventa o cualquier otra condición; 2. En la prestación de servicios, en la fecha de pago al contado o en la que se otorgue al crédito (devengo), lo que suceda primero; 3. En el uso o consumo de mercancías para uso propio o para formar parte de los activos fijos de la empresa, en la fecha del retiro; 4. Cuando la venta se realice a través de internet, teléfono u otro medio similar, cuyo pago se realice mediante Tarjeta de Crédito, Débito o Depósito en Cuenta Bancaria, previo a la entrega del bien, la factura debe emitirse en la fecha en que se efectuó el pago y entregarse en forma conjunta con el bien; 5. Cuando el cliente no se encuentre en el lugar donde se realizó la emisión, será responsabilidad del emisor, que el original de la Factura, llegue a poder y dominio del cliente..." | Issuance-moment family: goods (incl. exports) — earliest of delivery, cash payment or credit granted, even under title-retention/repurchase pacts; services — earliest of cash/credit payment; self-consumption or fixed-asset incorporation — the withdrawal date; internet/phone/card/pre-deposit sales — the PAYMENT date, invoice delivered together with the good; remote clients — the emitter must get the original to the client | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 14 pp.21-22 (EV24:EVID-191) |
| LB-009 | Reglamento, Art. 10 nums. 3-5 (formato): "3. Clave de Autorización de Impresión (CAI), otorgada por la Administración Tributaria; 4. Fecha límite de emisión, vigente; 5. Rango autorizado, vigente" | The factura FORMAT layer prints the CAI, the valid emission deadline (fecha límite) and the valid authorized range — the authorization-quad values this ledger owns as data (print placement owned by file 03 FR-093) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 10 pp.15-17 (EV24:EVID-190) |
| LB-010 | Acuerdo 189-2014, Art. 7: "La Dirección Ejecutiva de Ingresos autorizará la impresión de los documentos fiscales, para ser utilizados dentro de un plazo máximo de dos (2) años. Los documentos fiscales perderán su validez cuando se haya vencido el plazo ... A partir de la segunda autorización de impresión, el contribuyente deberá consignar el número del último documento fiscal emitido, previo a la solicitud, como un dato referencial." | Historical (pre-2018) regime: authorizations valid for a MAXIMUM OF TWO (2) YEARS; chain-linking (declare the last emitted number on second+ authorizations) — dropped by 481-2017 (file 01 FR-026) | `hn/sources/25_Acuerdo_189-2014_Regl_Facturacion_hist.pdf` | Art. 7 p.4 (EV24:EVID-208) |
| LB-011 | Ayuda 78_ (autorización de impresión, flujo operacional — NO base legal, R-H37): "La Solicitud pasará a estado 'Pendiente de Aceptación'. ... Al ser aceptada la solicitud por la imprenta el estado de esta se verá reflejado como 'Solicitada'. ... La imprenta confirmará la entrega de los documentos y cambiará el estado de la solicitud a 'Activada'. Se generará el Formulario SAR-924 Solicitud de Autorización de Impresión por Imprenta." / autoimpresor: "Al enviar la solicitud se activarán automáticamente los documentos y se generará el Formulario SAR-927 Solicitud de Autorización de Impresión por Auto Impresor." | Oficina Virtual print-authorization chain: Pendiente de Aceptación → Solicitada (imprenta accepted) → Activada (imprenta confirms DELIVERY) generating Form SAR-924; autoimpresor solicitudes AUTO-ACTIVATE on submission generating Form SAR-927 | `hn/sources/78_Ayuda_autorizacion_impresion_2026.pdf` | pp.4-11 (EV24:EVID-214; operational corroboration of R-Arts. 59-64/69) |
| LB-012 | Reglamento, Art. 41 (anulados): "deben ser anulados, consignando en los mismos la leyenda 'ANULADA' de forma manuscrita, impresa o con sello"; custodia del original y copia "de forma cronológica y ordenada, por el plazo de la prescripción" | Voided documents must carry the legend ANULADA (handwritten, printed or stamped) and be kept — original and copy — chronologically and orderly for the prescription period (CT 4/5/7y horizons, taxation file by id) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 41 p.49 (EV24:EVID-202) |
| LB-013 | Reglamento, Art. 42 (no utilizados): "deben comunicar mediante el sistema que la Administración Tributaria establezca, la no utilización ... dentro de los primeros diez (10) días hábiles del mes siguiente de haberse producido los siguientes acontecimientos: 1. Cuando se produzca el vencimiento del plazo de vigencia de la autorización de impresión y vigencia; 2. Por modificaciones en los datos del Obligado Tributario ...; 3. Por cese temporal o definitivo de operaciones de uno o más establecimientos ...; 4. Por cese de operaciones del obligado tributario; 5. Por baja del punto de emisión; 6. Por deterioro ...; 7. Por robo o extravío ... sustentado con la respectiva denuncia ...; 8. Por errores de requisitos detectados con posterioridad a la entrega ... realizados por las imprentas ...; 9. Por Facturas Prevaloradas que no hayan sido utilizadas; 10. Por problemas o fallas técnicas en el sistema ...; 11. Por Comprobantes ... vencidos y no utilizados; 12. Por caso fortuito o fuerza mayor ..." | Unused documents must be communicated through the system SAR establishes, within the FIRST TEN (10) BUSINESS DAYS of the month FOLLOWING the event, across the 12 statutory causes (1 vigencia expiry; 2 taxpayer-data changes; 3 temporary/definitive cessation of one or more establishments; 4 total cessation; 5 emission-point deactivation; 6 deterioration; 7 theft or loss with police report; 8 print-shop requirement errors detected after delivery; 9 unused prevaloradas; 10 system problems/failures; 11 expired-and-unused documents; 12 fortuitous case or force majeure) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 42 pp.49-50 (EV24:EVID-202) |
| LB-014 | Reglamento, Art. 40 (uso temporal): comunicación del uso temporal de documentos previamente autorizados ante cambios de domicilio/nombre comercial declarados en el RTN o en ferias/eventos (consignando la ubicación), consignando legiblemente los datos modificados en los documentos emitidos [operación resumida en el glosa de EVID-202; verbatim no capturado — verificar contra el PDF al implementar] | Temporary use: previously authorized documents may continue in temporary use upon RTN-declared address/trade-name changes or at fairs/events, communicating to SAR and legibly consigning the modified data/location on emitted documents (verbatim gap flagged) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 40 p.49 (EV24:EVID-202) |
| LB-015 | Ayuda 77_ (notificación e-filing, flujo operacional — su Base Legal cita correctamente el Art. 42): pestaña "Notificaciones y Autorizaciones" → "Documentos Fiscales no Utilizados"; "En la casilla de 'Motivos' debe seleccionar la razón"; "se le solicita indicar si lo está notificando por Rango o Individual"; al presentar, "el sistema genera el Comprobante de la Notificación de Documentos Fiscales No Utilizados"; las notificaciones quedan guardadas con descarga | The Art. 42 duty as SAR runs it: motivo-driven selection, notification BY RANGE or INDIVIDUAL granularity, system-generated filing receipt (comprobante), archived under Notificaciones y Autorizaciones | `hn/sources/77_Ayuda_notif_docs_no_usados.pdf` | pp.4-9 (EV24:EVID-213; operational corroboration of R-Art. 42) |
| LB-016 | Reglamento, Art. 66 (requisitos imprentas): RTN; domicilio/teléfono/correo actualizados; "Actividades de Impresión" como actividad económica; contrato de adhesión; sin obligaciones pendientes; "Tener acceso permanente a internet"; "Contar con la maquinaria de impresión necesaria para la elaboración completa ... en sus instalaciones, ya sea de su propiedad o arrendada de forma exclusiva"; "Aprobar las pruebas de autorización de impresión" | Print-shop registry requisites: RTN; updated contact data; printing activities as economic activity; adhesion contract; no pending obligations; permanent internet access; in-premises printing machinery for the COMPLETE elaboration (owned or exclusively leased); pass the print-authorization tests | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 66 p.60 (EV24:EVID-206) |
| LB-017 | Reglamento, Art. 67: "se extenderá un Certificado de Autorización de Impresión a la imprenta con una vigencia de dos (2) años"; renovación solicitada "con seis (6) meses de anticipación al vencimiento" | A Print Authorization CERTIFICATE is issued to the print shop with a TWO (2) YEAR validity; renewal requested SIX (6) MONTHS before expiry | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 67 p.61 (EV24:EVID-206) |
| LB-018 | Reglamento, Art. 69 (obligaciones imprentas): verificar y archivar la identificación del cliente; solicitar la autorización por cada solicitud del cliente; requerir firma y sello del cliente en la solicitud ANTES de imprimir; imprimir la TOTALIDAD autorizada con los datos autorizados; "Informar a la Administración Tributaria, a través de la solicitud de Activación o Cancelación ... al momento de la entrega de los trabajos"; ídem para trabajos no reclamados luego de 1 mes; permitir inspecciones; tener documentos propios; notificar robo/extravío dentro de 10 días hábiles con denuncia; conservar solicitudes y recibos por el plazo del Código Tributario | Print-shop obligations: verify/archive client identification; request authorization per client solicitud; client signature/seal on the solicitud BEFORE printing; print the TOTALITY authorized with the authorized data; inform SAR via the ACTIVATION or CANCELLATION solicitud AT DELIVERY; same for work unclaimed after 1 month; allow inspections; hold own fiscal documents; theft/loss notified within 10 días hábiles with police report; conserve solicitudes and receipts for the CT period | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 69 pp.62-63 (EV24:EVID-206) |
| LB-019 | Reglamento, Art. 70 (prohibiciones imprentas): imprimir no autorizado; "Repetir por cualquier motivo la impresión" de documentos ya entregados; imprimir documentos que la propia imprenta reportó como no realizados; reponer documentos no entregados perdidos/robados/deteriorados; imprimir trabajos autorizados a OTRA imprenta; "Subcontratar a otras imprentas ... parcialmente o en su totalidad" | Print-shop prohibitions: printing without authorization; REPRINTING delivered documents for any motive; printing documents the shop itself reported as not realized; replacing undelivered lost/stolen/damaged documents; printing jobs authorized to ANOTHER print shop; subcontracting — the no-reprint rule is the external guarantee of correlativo uniqueness | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | Art. 70 pp.63-64 (EV24:EVID-206) |
| LB-020 | Acuerdo SAR-238-2024 (DJIMR), Arts. 5-7 (rectificativa + coverage frame consumed from the W2 evidence): the DJIMR informativa covers each retention period's detail, and its rectificativa auto-rectifies the determinativa of office (accepted only when tax increases); CT Art. 117 as the general rectification frame (quoted in the manuals' filing chassis) | The filing-side contract behind FR-085/FR-086: periods covered by a filed declaration are frozen facts at SAR — corrections exist only as rectificativas from the filed snapshot; the previous system's filed DJIMR/DMC/DJI aggregates are the authoritative external truth for go-live reconciliation (D-H3.2) | `hn/sources/14_Acuerdo_SAR-238-2024_DJIMR.pdf` + `hn/sources/03_Codigo_Tributario_D170-2016_act_D180-2020.pdf` (Art. 117) | 14-Arts. 5-7 (EV13:EVID-078/079); CT-Art. 117 as quoted in the W2b manuals (EV31:EVID-113) |

## 3. Functional Requirements

Correlativo grammar, wrap-at-99999999 and the no-FY-reset continuum are
owned by `01_document-types-numbering.md` (FR-012..FR-019) and consumed
here by id. Registration of devices/systems and topology selection are
owned by `04_registration-topologies-medios-see.md` (FR-150/151/154-157).

### 3.1 The CAI/rango authorization ledger (cluster E3)

- **HN-EINV-FR-046:** The system shall treat the CAI — the alphanumeric
  series SAR generates electronically "para autenticar el Procedimiento de
  Autorización de Impresión" — as the paper-regime authorization artifact
  tracked by a dedicated ledger, ALWAYS distinct from the CAEE (the unique
  per-electronic-document algorithmic code of the SEE medium): the ledger
  shall hold no CAEE field, and CAEE generation remains the config-gapped
  SEE surface of `04_registration-topologies-medios-see.md`
  (FR-166..169). (LB-001; EV24:EVID-186)
- **HN-EINV-FR-047:** The system shall implement the ledger as a dedicated
  model (`l10n_hn.cai.range`) keyed on the STATUTORY authorization key —
  (punto de emisión × document type, Art. 59) — extended in Odoo with the
  emission point's parent establecimiento per D-H1's full sequence key
  (establecimiento → `stock.warehouse`, punto de emisión → child emission
  point, document type → `l10n_latam.document.type`); the ledger shall
  NEVER key on `account.journal` (D-H1 one-journal architecture), and
  under SISTEMA CENTRALIZADO the establecimiento dimension collapses (file
  04 FR-155) without altering the statutory key.
  (LB-002 def. 35; LB-003; EV24:EVID-186; EV24:EVID-205; D-H1)
- **HN-EINV-FR-048:** The system shall store the *rango autorizado* as a
  taxpayer-REQUESTED QUANTITY — "definido por el Obligado Tributario al
  momento de la solicitud" — recording both the requested quantity and the
  granted span, with the SAR "limitaciones o condiciones" carried as data
  (FR-061); the rango is application data, never a fixed allotment.
  (LB-002 def. 36; EV24:EVID-186)
- **HN-EINV-FR-049:** The system shall honor the Art. 61 authorization
  granularity: default per punto de emisión × per document type; for
  *máquinas registradoras* PER DISPOSITIVO (rango established in the
  Art. 17.4 machine-numbering form); for *sistemas computarizados* PER
  SYSTEM × per document type — device and system references resolve from
  the registration matrix owned by file 04 (FR-150/151) and extend the
  ledger key. (LB-004; EV24:EVID-205)
- **HN-EINV-FR-050:** The system shall enforce ONE active rango per key
  until exhaustion: a partial-unique constraint shall prevent two rangos
  in state *activada* for the same (punto de emisión × document type
  [+ device/system]) key, and a new solicitud for a key whose active rango
  has not reached a terminal state shall be rejected — "una sola solicitud
  ... hasta agotar los documentos autorizados" (post-denegatoria
  regularization per FR-056 excepted). (LB-003; EV24:EVID-205)
- **HN-EINV-FR-051:** The system shall store each rango's consecutive
  span (from_number/to_number, 8-digit space) plus consumption counters
  (next_number, consumed_count), maintaining the continuity invariant:
  the correlativo is a continuum per key (file 01 FR-017), so a successor
  rango continues the consecutive where its predecessor ended, with the
  statutory WRAP at 99999999 (file 01 FR-016) linking spans across the
  boundary — derivation flagged (→ OQ-004). (LB-003; EV24:EVID-205;
  crossref EV24:EVID-188 → file 01 FR-016/017)
- **HN-EINV-FR-052:** For dispositivo-keyed (máquina registradora)
  authorizations the system shall store machine-numbering bounds in the
  Art. 17.4 form (≥ 10 digits, prefix 09, consecutive from 00000001)
  WITHOUT 16-digit enforcement (file 01 FR-010); whether SAR's device
  authorization bounds machine numbers as a consumable rango or merely
  authorizes the device is unpinned (→ OQ-005, kin file 01 OQ-001).
  (LB-004; EV24:EVID-205; crossref EV24:EVID-194)

### 3.2 Print-authorization state chain & activation semantics

- **HN-EINV-FR-053:** The system shall implement the rango state chain —
  draft → *pendiente_de_aceptación* → *solicitada* → *autorizada* →
  **ACTIVADA** → terminal (*agotada* | *vencida* | *cancelada*), with
  *rechazada* on denegatoria — mirroring SAR's Oficina Virtual chain:
  imprenta modality = 4-party handshake (taxpayer solicitud → imprenta
  aceptación → SAR autorización → imprenta entrega/activación);
  autoimpresor = instant auto-activation. Helps are operational
  corroboration only; states are ledger data (R-H37). (LB-011; LB-005;
  EV24:EVID-214; EV24:EVID-205)
- **HN-EINV-FR-054:** The system shall start number consumption ONLY at
  ACTIVADA: activation semantics = the imprenta's delivery confirmation
  (the Art. 69 activación/cancelación notification "al momento de la
  entrega de los trabajos") or the autoimpresor's auto-activation; no
  number shall be consumed from — and the emission gate (FR-066) shall
  refuse — any authorization in a pre-activación state. (LB-011; LB-018;
  EV24:EVID-214; EV24:EVID-206)
- **HN-EINV-FR-055:** The system shall store the form artifacts of the
  chain — SAR-924 (*Solicitud de Autorización de Impresión por Imprenta*,
  generated at imprenta-flow activation) and SAR-927 (*... por Auto
  Impresor*, generated at autoimpresor auto-activation) — as references
  on the authorization record (field-level fidelity → OQ-002).
  (LB-011; EV24:EVID-214)
- **HN-EINV-FR-056:** On denegatoria the system shall set state
  *rechazada* and raise a 10-días-hábiles regularization monitor (Art. 64:
  regularize the situación tributaria or request verificación), blocking
  new emission from the key until resolved. (LB-007; LB-003;
  EV24:EVID-205)

### 3.3 Vigencia & renewal

- **HN-EINV-FR-057:** The system shall carry the vigencia maxima as DATED
  ROWS (D-H2): 481-2017 — maximum one (1) year, `valid_from` 2017-12-31;
  189-2014 — maximum two (2) years, `valid_from` 2014-05-01,
  `valid_to` 2017-12-30 (historical authorizations only) — and shall store
  each authorization's GRANTED vigencia/fecha límite as data, never
  assuming the statutory maximum (Art. 63 limits; practice open → OQ-001).
  (LB-005; LB-010; EV24:EVID-205; EV24:EVID-208)
- **HN-EINV-FR-058:** The system shall treat expiry as hard validity loss
  — "perderán su validez y no podrán ser utilizados cuando se haya
  vencido el plazo" — storing the *fecha límite de emisión* per
  authorization; the FORMAT-layer print of the authorization quad is owned
  by file 03 (FR-093) and consumes this ledger. (LB-005; LB-009;
  EV24:EVID-205; EV24:EVID-190)
- **HN-EINV-FR-059:** The system shall monitor the renewal window —
  renewal solicitudes are fileable only "dentro de los dos (2) meses
  previos a la fecha límite de emisión" — raising a renewal-window-open
  alert at T-2 months and tracking filing state (the alert itself is an
  operational derivation; the window is statutory).
  (LB-003; EV24:EVID-205)
- **HN-EINV-FR-060:** The system shall monitor exhaustion: when
  consumed_count reaches the span end the rango goes *agotada*
  (terminal-success), unlocking the successor solicitud (FR-050), with a
  configurable near-exhaustion alert — operational derivation (the
  exhaustion-alert family, flagged per RESEARCH §7).
  (LB-003; EV24:EVID-205)

### 3.4 SAR limits, conditions & cancellation (Art. 63)

- **HN-EINV-FR-061:** The system shall carry SAR's power to "limitar y/o
  condicionar la autorización" as overlay DATA on each authorization —
  limit text, condition text, effective dates (e.g. spans shorter than
  requested, conditional vigencias) — resolved per authorization and never
  re-derived (practice VERIFY → OQ-001). (LB-006; EV24:EVID-205)
- **HN-EINV-FR-062:** The system shall support mid-vigencia cancellation —
  SAR "podrá cancelar la vigencia de las autorizaciones otorgadas cuando
  se compruebe inconsistencias o alteraciones": the rango moves to
  *cancelada* with cancellation date and reason; the emission gate blocks
  the key from that date; the unused span becomes notifiable under the
  applicable no-utilizados cause (FR-074/076).
  (LB-006; EV24:EVID-205)
- **HN-EINV-FR-063:** The system shall store the Art. 63 comportamiento
  tributario criteria (RTN currency; formal/material compliance; "deudas
  líquidas firmes y exigibles pendientes de pago"; pending procedures) as
  evaluation-context data on any authorization affected by a
  limit/condition/cancellation — recorded context only, never evaluated by
  Odoo. (LB-006; EV24:EVID-205)

### 3.5 Momento de emisión & the hard emission gate (D-H2.2)

- **HN-EINV-FR-064:** The system shall compute each document's emission
  date per the Art. 14 earliest-of family: (1) goods including exports —
  earliest of delivery, cash payment or credit granted (devengo), with
  suspensory conditions (reserva de dominio, pacto de retroventa) NOT
  deferring; (2) services — earliest of cash/credit payment; (3)
  self-consumption or fixed-asset incorporation — the retiro date; (4)
  internet/phone sales prepaid by card, debit or bank deposit — the
  PAYMENT date, the factura delivered together with the good; (5) remote
  clients — the emitter is responsible the original reaches the client.
  (LB-008; EV24:EVID-191)
- **HN-EINV-FR-065:** The system shall use the momento-de-emisión date
  computed by FR-064 — with its basis (entrega / pago / devengo / retiro /
  prepago) recorded on the document — as THE emission-gate input, never
  the system or posting date (D-H2: resolution by domain date, never
  "today"). (LB-008; EV24:EVID-191; D-H2)
- **HN-EINV-FR-066:** **HARD EMISSION BLOCK (D-H2.2, user decision
  2026-08-20 — supervisor override explicitly rejected):** a fiscal
  document shall NOT be postable unless its emission date resolves to a
  CAI rango in state *activada*, of the exact (establecimiento, punto de
  emisión, document type) key, whose coverage window [activation date,
  min(fecha límite, cancellation date)] contains the date and whose span
  is not exhausted; no role, group, or configuration shall bypass the
  block — HN has no transmission regime, so this gate IS the regime's
  emission control. (LB-005; LB-003; EV24:EVID-205; D-H2.2)
- **HN-EINV-FR-067:** The system shall treat backdating as a coverage
  question: a document dated in the past posts only inside a
  historically-valid rango (coverage evaluated at the DOCUMENT date);
  a date outside every rango's historical coverage is blocked — this is
  HN's "cannot emit in the past" rule, and backdating is never a gate
  bypass. (LB-005; EV24:EVID-205; D-H2.2)
- **HN-EINV-FR-068:** The system shall emit distinct gate errors per
  failure mode: no authorization record for key; authorization not yet
  *activada*; date before activation; date after fecha límite (*vencida*);
  span exhausted (*agotada*); rango *cancelada*; company RTN suspended
  (FR-071). (LB-005; LB-003; LB-006; EV24:EVID-205)
- **HN-EINV-FR-069:** At posting the system shall snapshot the resolved
  authorization data — CAI, rango label (from-to), fecha límite, emission
  date + basis — onto the move (D15/D-H2 snapshot-on-write) and shall
  increment the rango's counters atomically within the posting
  transaction; reset-to-draft and re-post shall not double-count.
  (LB-009; EV24:EVID-190; D-H2)
- **HN-EINV-FR-070:** Every posted fiscal document shall consume exactly
  one number of its rango — including documents later voided (the number
  stays burned, FR-073) — while historical imports (D-H3; file 01 FR-027)
  shall NEVER consume range numbers and shall never pass the gate as
  emitters: they are flagged read-only records validated against the
  rango rows in force at their ORIGINAL dates.
  (LB-003; EV24:EVID-205; D-H3; crossref EV24:EVID-207)
- **HN-EINV-FR-071:** While the company's RTN is suspended
  (`../taxation/01_isr-framework.md`, HN-TAX-FR-044), the emission gate
  shall block all emission surfaces for the company with a distinct
  RTN-suspension error (inscription-side effects owned by file 04
  FR-145). (LB-006; EV24:EVID-205; crossref T11 EVID-027..038)

### 3.6 Lifecycle events (cluster E7)

- **HN-EINV-FR-072:** The system shall void fiscal documents by marking
  them with the legend "ANULADA" (manuscrita, impresa o con sello —
  system-generated documents print it) and shall keep original + copia
  "de forma cronológica y ordenada, por el plazo de la prescripción" —
  retention horizons per the CT 4/5/7-year rules owned by
  `../taxation/01_isr-framework.md` (HN-TAX-FR-040), consumed by id.
  (LB-012; EV24:EVID-202)
- **HN-EINV-FR-073:** Void shall never equal delete: a voided document
  retains its number and its rango consumption (FR-070), is flagged
  *anulada* with date and motive, stays queryable, and can never be
  deleted or renumbered. (LB-012; EV24:EVID-202)
- **HN-EINV-FR-074:** The system shall seed the 12-cause no-utilizados
  catalog verbatim per Art. 42 (vigencia expiry; taxpayer-data changes;
  cese temporal/definitivo de establecimientos; cese de operaciones; baja
  del punto de emisión; deterioro; robo/extravío with denuncia; imprenta
  requirement errors post-delivery; unused prevaloradas; system
  failures; vencidos y no utilizados; caso fortuito o fuerza mayor) as
  the motive catalog of the notification generator. (LB-013;
  EV24:EVID-202)
- **HN-EINV-FR-075:** The system shall compute each notification's
  deadline as the FIRST 10 DÍAS HÁBILES of the month FOLLOWING the
  triggering event — "dentro de los primeros diez (10) días hábiles del
  mes siguiente" — monitoring compliance per notification (días hábiles
  per the statute; per-instrument deadline semantics discipline).
  (LB-013; EV24:EVID-202)
- **HN-EINV-FR-076:** The system shall auto-detect cause 1 (vigencia
  expiry with unused numbers — the AUTOMATIC cause per EVID-202): the
  ledger monitor shall detect every rango reaching *vencida* — or
  *cancelada*, FR-062 — with an unused span, and queue a notification
  with the applicable cause and its 10-días-hábiles due date (operational
  derivation feeding the statutory duty). (LB-013; LB-005;
  EV24:EVID-202; EV24:EVID-205)
- **HN-EINV-FR-077:** The notification generator shall be motivo-driven
  and granular per SAR's intake — "por Rango o Individual" — with
  RANGO-granular output as the natural product of the ledger's unused-span
  tracking and individual granularity available for document-level causes
  (e.g. cause 7 robo/extravío with its denuncia reference); field-level
  mapping → OQ-002. (LB-015; LB-013; EV24:EVID-213; EV24:EVID-202)
- **HN-EINV-FR-078:** The system shall capture the *Comprobante de la
  Notificación de Documentos Fiscales No Utilizados* (system-generated
  filing receipt) on every filed notification, storing it with the
  record, and shall mirror SAR's *Notificaciones y Autorizaciones*
  archive with download. (LB-015; EV24:EVID-213)
- **HN-EINV-FR-079:** The system shall support *uso temporal*: on
  RTN-declared domicilio/nombre-comercial changes, or at
  ferias/eventos, previously-authorized documents may continue in
  temporary use — with a communication to SAR and the temporary location
  / modified data consigned legibly on emitted documents; uso-temporal
  registrations hang off the rango (verbatim gap → LB-014 caveat).
  (LB-014; EV24:EVID-202)

### 3.7 Registro Fiscal de Imprentas (cluster E7)

- **HN-EINV-FR-080:** The system shall model certified imprentas as
  partners flagged in the *Registro Fiscal de Imprentas* (partner flag
  consumed from file 03) carrying the *Certificado de Autorización de
  Impresión* data — certificate number, 2-year vigencia — with a renewal
  monitor at T-6 months ("con seis (6) meses de anticipación al
  vencimiento"). (LB-017; EV24:EVID-206)
- **HN-EINV-FR-081:** The system shall carry the Art. 66 requisites as an
  accreditation checklist on the imprenta record — RTN; updated
  domicilio/teléfono/correo; "Actividades de Impresión" as actividad
  económica; contrato de adhesión; al día en obligaciones; "acceso
  permanente a internet"; in-premises machinery (owned or exclusively
  leased) for the complete elaboration; passed authorization tests —
  recording SAR's evaluation outcomes as data, never evaluating them.
  (LB-016; EV24:EVID-206)
- **HN-EINV-FR-082:** For autorizations under the imprenta modality the
  system shall reflect the Art. 69 handshake on the ledger: the solicitud
  requires the client's signature/seal BEFORE printing; the imprenta
  prints the TOTALITY authorized with the authorized data; activación
  (FR-053/054) is notified to SAR "al momento de la entrega de los
  trabajos"; unclaimed work after 1 month is likewise notified;
  theft/loss is notified within 10 días hábiles with denuncia;
  solicitudes and recibos are conserved for the CT prescription period.
  (LB-018; EV24:EVID-206)
- **HN-EINV-FR-083:** The system shall enforce the Art. 70 prohibitions
  as customer-side invariants: no reprint of delivered numbers ("Repetir
  por cualquier motivo la impresión" — the external guarantee of
  correlativo uniqueness, file 01 FR-019), no printing of jobs authorized
  to another imprenta, no subcontracting, no replacement of undelivered
  lost/robbed/deteriorated stock — a rango is bound to exactly one
  imprenta and its numbers can never be reissued.
  (LB-019; EV24:EVID-206)
- **HN-EINV-FR-084:** The imprenta's Registro Fiscal de Imprentas
  identification recorded on the rango (partner + certificate data) shall
  feed the *Datos de la imprenta* FORMAT print owned by file 03 (FR-096)
  and the accreditation surface of file 04 (FR-149).
  (LB-018; LB-019; EV24:EVID-206; crossref EV24:EVID-190)

### 3.9 Filed-period freeze & go-live reconciliation (V-HN1 additions, reserved tail 085-090)

- **HN-EINV-FR-085:** The system shall write-protect fiscal documents
  (facturas/NC/ND/retention vouchers and their CAI ledger consumption
  rows) belonging to periods covered by a FILED SAR declaration (DJIMR
  retenciones / DMC compras / DJI mensual — the filing freeze of
  D-H2.5): such records become read-only, and any correction flows as a
  rectificativa computed from the frozen snapshot (CT Art. 117 frame),
  never as a silent edit or re-emission; the freeze state is per
  (declaration, period) and reversible only by the rectificativa
  lifecycle owned by fiscal-reporting file 01 (consumed by id).
  (LB-020; D-H2.5)
- **HN-EINV-FR-086:** The system shall provide the go-live reconciliation
  report of D-H3.2: current-FY imported fiscal documents (FR-027
  read-only detail) reconciled against the monthly declarations the
  PREVIOUS system filed with SAR (DMC compras / DJIMR retenciones / DJI
  mensual aggregates = the authoritative external truth), flagging deltas
  per period and document family; no re-emission, no re-numbering, no
  sequence consumption (D-H3.1).
  (LB-020; D-H3.2; fiscal-reporting/01 HN-FREP-FR-031 by id)

## 4. Data Model

Entities owned by siblings (document-type catalog, emission-point entity,
device/system registry, partner exonerado fields) are referenced, not
redefined. Machine-readable sidecars (the 12-cause catalog, the vigencia
dated rows) join the catalogs wave; none are created by this file — the
rows below are the contract.

**CAI/rango ledger (dedicated model):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.cai.range | company_id / warehouse_id / emission_point_id / document_type_id | m2o | statutory key = (emission point × document type); warehouse = establecimiento for the D-H1 sequence key; NEVER account.journal | FR-047 |
| l10n_hn.cai.range | device_id / system_id | m2o file-04 registry, null | máquina-registradora dispositivo / SFC system granularity | FR-049, FR-052 |
| l10n_hn.cai.range | cai | char | SAR alphanumeric key; no CAEE field ever (SEE = file 04) | FR-046 |
| l10n_hn.cai.range | state | select | draft · pendiente_aceptacion · solicitada · autorizada · activada · agotada · vencida · cancelada · rechazada | FR-053 |
| l10n_hn.cai.range | from_number / to_number / next_number / consumed_count | int (8-digit space) | span + consumption counters; wrap at 99999999 links spans (file 01 FR-016) | FR-051, FR-069/070 |
| l10n_hn.cai.range | machine_from / machine_to / machine_prefix | char/int | dispositivo-keyed bounds, Art. 17.4 form (prefix 09, ≥ 10 digits) | FR-052 |
| l10n_hn.cai.range | requested_quantity / granted_quantity | int | requested (def. 36) vs granted span size | FR-048 |
| l10n_hn.cai.range | limit_overlay / condition_overlay / comportamiento_context | text / text / json | Art. 63 overlay as data (RTN currency, compliance, firm debts, procedures) | FR-061..FR-063 |
| l10n_hn.cai.range | authorization_date / activation_date / fecha_limite | date | SAR authorization vs delivery/auto activation; fecha límite STORED, never derived | FR-054, FR-057, FR-058 |
| l10n_hn.cai.range | cancelled_on / cancellation_reason | date / text | mid-vigencia cancellation (Art. 63) | FR-062 |
| l10n_hn.cai.range | form_ref / imprenta_partner_id / last_issued_reference | char / m2o res.partner / int | SAR-924/SAR-927 artifacts; imprenta binding (FR-083); optional chain-link continuity data (file 01 FR-026) | FR-055, FR-082 |
| l10n_hn.cai.range | constraint | — | partial-unique: ONE activada span per (emission_point, document_type [+ device/system]) | FR-050 |
| l10n_hn.vigencia.rule | regime / max_vigencia / valid_from / valid_to | char / int months / date / date | 481-2017: 12 mo, 2017-12-31→open · 189-2014: 24 mo, 2014-05-01→2017-12-30 | FR-057 |

**Lifecycle records (E7):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.no.utilizados.notification | rango_id / cause / granularity | m2o / select 1-12 / select | cause catalog verbatim per LB-013; rango · individual | FR-074, FR-077 |
| l10n_hn.no.utilizados.notification | event_date / due_date / filed_on / comprobante_ref / state | date ×2 + char | due = first 10 días hábiles of following month; comprobante receipt stored | FR-075, FR-076, FR-078 |
| l10n_hn.uso.temporal | rango_id / kind / location / notified_on | m2o / select (domicilio · nombre_comercial · feria_evento) / char / date | temporary-use registrations; modified data consigned on documents | FR-079 |
| res.partner (imprenta ext.) | is_imprenta (file 03) / certificate_no / certificate_from / certificate_to / renewal_alert_at / requisites checklist | boolean / char / date ×2 / json | 2-year certificate; T-6mo monitor; Art. 66 checklist outcomes | FR-080, FR-081 |

**Move-side fields (gate + snapshots):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move | l10n_hn_cai_range_id / l10n_hn_cai / l10n_hn_rango_label / l10n_hn_fecha_limite | m2o / char / char / date | snapshot-on-write of the resolved authorization (D15) | FR-069 |
| account.move | l10n_hn_emission_date / l10n_hn_emission_basis | date / select | entrega · pago_contado · credito_devengo · retiro · prepago (Art. 14 family) | FR-064, FR-065 |
| account.move | l10n_hn_anulada / anulada_on / anulada_motivo | boolean / date / text | ANULADA marking; retention per CT prescription config (taxation FR-040) | FR-072, FR-073 |
| account.move (historical) | is_historical | boolean | read-only imports; never consume, never gate (D-H3) | FR-070 |

## 5. Odoo Mapping

Layer semantics: `odoo` = ledger, monitors, notification and posting-gate
logic in the LGPL client; `shared` = contract items any side must honor —
the emission-date computation and the HARD gate/snapshot contract, which a
future SEE server-side service must honor identically (HN's paper regime
has no SaaS surface today; `saas` is deliberately unused, as in files
01/03). Model names stable across Odoo 17/18/19/20; version-specific
behavior noted per row.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-046 | odoo | l10n_hn.cai.range | cai | No CAEE field; SEE placeholder untouched (file 04 FR-166..169) |
| FR-047 | odoo | l10n_hn.cai.range + l10n_hn.emission.point + stock.warehouse + l10n_latam.document.type | key fields | Journal-independent (D-H1); centralizado collapse consumed from file 04 FR-155; identical 17-20 |
| FR-048 | odoo | l10n_hn.cai.range | requested/granted quantities | Def. 36 semantics; solicitud UI captures request, SAR response fills grant |
| FR-049 / FR-052 | odoo | l10n_hn.cai.range | device_id/system_id + machine bounds | Device/system rows from file 04 registry; machine rows bypass 16-digit validation (file 01 FR-010) |
| FR-050 / FR-051 | odoo | l10n_hn.cai.range | partial-unique constraint + counters | Postgres partial unique index on state=activada; counters via atomic SQL increment at posting; ir.sequence used as execution surface only (no native wrap, file 01 §5 note — 17-20) |
| FR-053..FR-055 | odoo | l10n_hn.cai.range | state machine + form_ref | State transitions mirror SAR-924/927 chain; artifacts stored as refs (fidelity → OQ-002) |
| FR-056 | odoo | l10n_hn.cai.range + ir.cron | rechazada + due monitor | 10 días hábiles counter needs the hábil-calendar config (→ OQ-006) |
| FR-057 | odoo | l10n_hn.vigencia.rule + l10n_hn.cai.range | dated rows + stored fecha_limite | Additive dated rows (D-H2); granted value snapshot per authorization, never re-derived |
| FR-058 | odoo | l10n_hn.cai.range | fecha_limite | Feeds file 03 FR-093 print quad |
| FR-059 / FR-060 | odoo | ir.cron | renewal T-2mo + exhaustion alerts | Operational derivations; thresholds company-configurable |
| FR-061..FR-063 | odoo | l10n_hn.cai.range | overlay + context fields | Data-only capture of Art. 63; no evaluation logic |
| FR-064 / FR-065 | shared | account.move | l10n_hn_emission_date + basis | Pre-posting computation; any future server-side emission service must honor identical date semantics |
| FR-066 | shared | account.move `_post` override | hard-block constraint | UserError on gate failure; `_post` stable 17-20; NO override group/setting — enforce by absence of bypass code (static check, AC-020 kin of SV FR-053/AC-011) |
| FR-067 | shared | account.move | coverage evaluation at document date | Evaluation date = the move's own emission date, never `today` |
| FR-068 | odoo | gate error taxonomy | 7 failure modes | Distinct error codes surfaced + logged |
| FR-069 | shared | account.move + l10n_hn.cai.range | snapshot fields + atomic increment | Same-transaction counter increment; draft-reset/re-post deduplicated |
| FR-070 | odoo | l10n_hn.cai.range + account.move | consumption linkage | `is_historical` bypasses counters and gate (D-H3, file 01 FR-027) |
| FR-071 | odoo | account.move gate | company RTN flag | Consumes taxation 01 HN-TAX-FR-044 flag; distinct error code |
| FR-072 / FR-073 | odoo | account.move | l10n_hn_anulada + unlink block | Legend prints with document; retention per CT prescription config (taxation FR-040); deletion blocked |
| FR-074 / FR-075 | odoo | l10n_hn.no.utilizados.notification | cause select + due date | Cause catalog seed; 10-días-hábiles engine (hábil calendar → OQ-006) |
| FR-076 | odoo | ir.cron + notification queue | expiry/cancellation monitor | Cause-1 auto-queue (operational derivation, EVID-202 gloss) |
| FR-077 / FR-078 | odoo | notification generator + comprobante store | granularity + receipt | Mirrors 77_ intake; comprobante attachment; archived list view |
| FR-079 | odoo | l10n_hn.uso.temporal | registration rows | Location printing note on documents; verbatim-gap caveat (LB-014) |
| FR-080 / FR-081 | odoo | res.partner (imprenta ext.) + ir.cron | certificate + checklist + T-6mo alert | Reuses file 03 partner flag; checklist outcomes recorded |
| FR-082 | odoo | l10n_hn.cai.range | handshake fields | Signature-before-print checklist on solicitudes; activación ties FR-053/054 |
| FR-083 | odoo | l10n_hn.cai.range constraints | no-reprint invariants | One imprenta per rango; reissue/cross-shop attempts rejected |
| FR-084 | odoo | l10n_hn.cai.range → print surfaces | imprenta data feed | Consumed by file 03 FR-096 and file 04 FR-149 |

Version-regime note (D12/D15): the vigencia maxima ships as dated rows
(2014-05-01 / 2017-12-31) additive-only; snapshots resolve as-of each
document's emission date and are frozen on write (D15 anchor-date
pattern); the gate's behavior does not vary by Odoo version.

## 6. Acceptance Criteria

- **AC-001:** Given an imprenta-modality authorization, then its ledger
  record stores the CAI and no CAEE field exists anywhere on the ledger;
  the CAEE reservation surface remains exclusively the move-level SEE
  placeholder of file 04 (FR-046).
- **AC-002:** Given key (punto 001, type 01) with rango A in state
  *activada*, when a solicitud for rango B is filed at the same key, then
  it is rejected until A reaches *agotada*/*vencida*/*cancelada*; given A
  *agotada*, then B proceeds through the chain (FR-050).
- **AC-003:** Given a rango in state *autorizada* (not yet delivered),
  when emission is attempted, then it is blocked with a not-active error;
  given the same rango *activada* with activation date 05-mar, then
  emission for dates on/after 05-mar inside the span proceeds (FR-054,
  FR-066).
- **AC-004:** Given an imprenta solicitud, then states progress
  *pendiente_de_aceptación* → *solicitada* → *autorizada* → *activada*
  with the SAR-924 artifact stored at activation; given an autoimpresor
  solicitud, then sending it auto-activates and stores SAR-927 (FR-053,
  FR-055).
- **AC-005:** Given a factura dated 10-mar-2027 at key K whose rango
  coverage = [05-mar-2027, 04-mar-2028], when posted, then it posts, the
  CAI/rango/fecha límite snapshot lands on the move and the counter
  increments; given the same document dated 05-mar-2028, then posting is
  blocked with a *vencida* error and no supervisor account can override
  (FR-066, FR-069).
- **AC-006:** Given a historically-valid rango coverage
  [01-feb-2026, 31-ene-2027] and today = 2027-06, when a document dated
  15-mar-2026 is posted, then it posts (backdating inside valid
  coverage); given the same document dated 15-mar-2027, then it is
  blocked (FR-067).
- **AC-007:** Given goods delivered 20-jun under a credit granted 15-jun
  with a reserva-de-dominio pact, then the emission date = 15-jun with
  basis credito_devengo (the condition does not defer) (FR-064).
- **AC-008:** Given an internet sale paid by card on 01-jul and delivered
  05-jul, then the emission date = 01-jul with basis prepago, the factura
  delivered together with the good (FR-064).
- **AC-009:** Given a service paid 30-sep, then the emission date =
  30-sep with basis pago_contado (FR-064).
- **AC-010:** Given a rango with to_number 00005000 and consumed_count
  5000, when the next document posts at the key, then it is blocked with
  an *agotada* error and the successor solicitud unlocks; the
  near-exhaustion alert fired earlier at the configured threshold
  (FR-060, FR-066, FR-068).
- **AC-011:** Given SAR cancels a live rango on 10-abr, then documents
  dated on/after 10-abr at the key are blocked with a *cancelada* error
  and the unused span queues a no-utilizados evaluation (FR-062, FR-076).
- **AC-012:** Given a rango granted a 6-month vigencia under an Art. 63
  limit, then fecha límite = activation + 6 months (never the 1-year
  maximum) and the limit text is stored on the record (FR-057, FR-061).
- **AC-013:** Given a rango with fecha límite 31-dic, then the
  renewal-window-open alert fires 01-nov (T-2 months) (FR-059).
- **AC-014:** Given a posted factura that is voided, then it prints the
  ANULADA legend, keeps its number and consumption, cannot be deleted or
  renumbered, and remains archived per the CT prescription config
  (FR-072, FR-073, FR-070).
- **AC-015:** Given a rango expiring 30-sep with 200 unused numbers, then
  on 01-oct a cause-1 notification is queued with due date inside the
  first 10 días hábiles of October (FR-076, FR-075).
- **AC-016:** Given the queued notification, when filed por-Rango, then
  the record carries the full unused span and the comprobante reference,
  and is retrievable from the notifications archive (FR-077, FR-078).
- **AC-017:** Given the company RTN suspended, when any emission is
  attempted at any key, then it is blocked company-wide with the
  RTN-suspension error (FR-071).
- **AC-018:** Given an imprenta certificate expiring 31-dic-2027, then
  the renewal alert fires 30-jun-2027 (T-6 months) (FR-080).
- **AC-019:** Given a delivered rango bound to imprenta X, when any
  configuration attempts reissuing an already-consumed number at the key
  or rebinding the rango to imprenta Y, then it is rejected (FR-083).
- **AC-020:** Given the codebase, when statically scanned, then no
  bypass path (group, setting, context flag) around the FR-066 posting
  constraint exists (FR-066).
- **AC-021:** Given a D-H3 historical import of a current-FY document,
  then no counter increments and the gate is not evaluated as an emission
  (flagged read-only) (FR-070).
- **AC-022:** Given a factura whose period is covered by a filed DMC
  (compras) declaration, then any attempted edit to the document or its
  CAI consumption row is refused (write-protected), and the only mutation
  path offered is the rectificativa flow from the frozen snapshot
  (FR-085).
- **AC-023:** Given a go-live import whose January current-FY document
  totals differ from the January DJIMR/DMC aggregates filed by the
  previous system, then the reconciliation report flags the delta per
  document family with zero re-emission and zero sequence consumption
  (FR-086).
- **AC-024:** Given an emission attempt with NO authorization record for
  the (establecimiento, punto de emisión, document type) key, then the
  FR-066 hard block fires with the no-authorization-record reason
  (FR-068).
- **AC-025:** Given an emission attempt dated before the rango's
  activation date (e.g. a backdated document preceding consumable-state
  activation), then the FR-066 hard block fires with the
  date-before-activation reason (FR-068).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `24_ OQ-6` (C3 carry, VERIFY): mid-vigencia SAR limits/conditions/cancellations (Art. 63) practice — does SAR commonly grant <1y vigencias, and does the T-2mo renewal window compound into operational dead zones near year-end? FR-057/061/062 carry the granted vigencia and overlays as data (never assume 1y); verify against live SAR-924/927 grants before freezing alerts tuning. | no | Takumi S-HN2 + controller | open |
| OQ-002 | `76-78_ OQ-2` (C3 carry, LEAD): SAR-924/SAR-926/927 form prints not in corpus — acquire ONLY if field-level fidelity is needed for the FR-055 artifact references, the FR-077 notification field mapping, or the renewal solicitud surface; would also pin the Art. 64 rejection state naming (FR-053/056 derive it from the gloss). | no | controller (acquisition queue) | open |
| OQ-003 | `24_ OQ-5` (C3 carry, kin — note only): L10,000 consumer-final ID threshold is SEFIN-modifiable; PRIMARY home = `03_document-mechanics.md` OQ-001 (dated row there). No FR in this file depends on the threshold; carried as a cross-file note per the master index, nothing to resolve here. | no | — | open (kin note; home = file 03) |
| OQ-004 | Local derivation (VERIFY): successor-rango continuity — FR-051 assumes a renewal's span continues the key's consecutive from predecessor end + 1 (continuum + wrap), and FR-050 forbids two ACTIVADA spans although the T-2mo renewal window (FR-059) opens while the predecessor is still active: how do solicitudes chain in practice (filed in-window, activated at predecessor exhaustion/expiry)? Statute silent; resolve vs SAR-924 practice — kin of `25_ OQ-1` (chain-linking, file 01 OQ-004). | no | Takumi S-HN2 | open |
| OQ-005 | Local derivation (VERIFY): dispositivo-keyed (ticket) authorization semantics — Art. 61 establishes the rango per device in the Art. 17.4 machine-numbering form, but machine numbering is autogen: does the device rango bound numbers as a consumable quantity (counters apply) or merely authorize the device (bounds recorded only)? FR-052 stores bounds without consumption; kin of `24_ OQ-1` (ticket dual code, file 01 OQ-001). | no | Takumi S-HN2 | open |
| OQ-006 | Local config (CONFIG): días hábiles engine — FR-056/075/082 deadlines need an HN holiday-calendar configuration (default = SAR-published calendar; watch for a determining instrument); per-instrument hábil-vs-calendario discipline per the `04_ OQ-3` pattern (this file's deadlines are all statutory HÁBILES). | no | Takumi S-HN2 | open |
