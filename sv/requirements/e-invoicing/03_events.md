# SV — E-Invoicing — Events: invalidación, contingencia, retorno, operaciones especiales

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave 1 |
| Updated | 2026-08-17 |

## 1. Purpose

This file defines the functional requirements for the four El Salvadorian
event types under Normativa de Cumplimiento DTE v2.0: *Evento de
Invalidación* (invalidation event — cancels a sealed DTE or event), *Evento
de Contingencia* (contingency event — declares documents generated during a
force-majeure transmission outage), *Evento de Retorno* (return event — new
in 2026, reports goods returns and service diminutions against FE/FEXE/FSEE
documents), and *Evento de Operaciones Especiales* (special-operations
event — new in 2026, monthly reporting of physical FVS and internal-control
documents). It covers event taxonomy and business-effect semantics, the
authoritative JSON structure versions, per-event structures and validation
rules, the differentiated invalidation deadlines and precondition blocks,
the contingency clocks (24 h event / 72 h documents) and the 1000-item
detail cap, the retorno three-month window / value caps / fiscal effects,
and the special-operations reporting regime. It merges master-index
clusters A3 (invalidación), A4 (contingencia) and A5 (retorno +
operaciones especiales).

Per the product architecture (decisions D1/D2/D3/D6), events are generated,
validated and transmitted **SaaS-side** through the private minimal
protocol; the Odoo thin client initiates events, surfaces their state,
delivers the corresponding Representación Gráfica where applicable, and
mirrors the sealed event archive (Tier A).

It does **not** cover: the transport the events ride on — authentication,
endpoints, retry, lots, state vocabulary and the 24-hour correction rule
(`02_transmission.md`, cluster A2/A8), per-type DTE structures
(`01_document-types.md`, A1), signing (`04_signing.md`, A6), RG/QR/delivery
mechanics (`05_delivery.md`, A7), catalog governance (A9), the tax
computation feeding retorno caps (A10, `taxation/`), onboarding tests per
event (A11), or the private protocol's own contract detail (A12,
`07_api-contract.md`).

## 2. Legal Basis

Authority order (binding, per master evidence index): 44_/45_/46_/50_/51_/52_
(2026) > 18_/19_/22_ (2025) > 40_/41_/25_ (2022). Conflict resolutions R2,
R4, R5, R6, R9, R11 and R12 from the master index are noted where they
apply. Where the 45_ Anexo digest (DG45, OCR) and the official 52_ JSON
Schemas (2026-08-11, read directly for this file) disagree, the schemas
govern as the later, machine-checkable authority; divergences are flagged
inline and in Section 7.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D.L. 487-2022 (reforma al Código Tributario), Art. 119-A | Art. 119-A: AT faculties incl. "podrá establecer los eventos que sean necesarios" — the legal root of the 2026 event regime | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 119-A (EVID-083) |
| LB-002 | D.L. 487-2022, Art. 119-E | Art. 119-E: invalidation paths (error / rescission / affected-operation adjustment via invalidation + reissue); receiver-ID data in the event for FE/FEXE/FSEE; post-window CCF/CR adjustment via NC/ND under Ley IVA 62–63 | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 119-E (EVID-083) |
| LB-003 | D.L. 487-2022, Art. 119-F | Art. 119-F: contingency duty — event with detail of untransmitted documents, transmission of all detailed documents within the AT deadline; compliance exempts sanctions 239-A g)/h) | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 119-F (EVID-083) |
| LB-004 | D.L. 487-2022, Art. 11 (CT 239-A reformado) | CT 239-A: event sanctions — d) omit transmission 100% (min 9 SMM); g) omit event 9 SMM; h) late event 9 SMM; i) non-compliant event structure 9 SMM; j) breach of AT e-document normativa 9 SMM | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 11 (EVID-083) |
| LB-005 | Normativa de Cumplimiento DTE v2.0, §4, §9 Cuadro 5 y §§13.3–13.4 | DTE Regulation v2.0: the four-event regime; event transmission modalities and clocks (Cuadro 5); retorno and operaciones-especiales regimes | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | §4, §9, §13.3–13.4 (EVID-084) |
| LB-006 | Normativa v2.0, Anexo III (estructuras de eventos) | Annex III: unified event field table, Secciones 1–13, fields N° 1–121 | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo III pp. 81–101 (via DG45 §2) |
| LB-007 | Normativa v2.0, Anexo V (validaciones de eventos) | Annex V: per-field event validation rules incl. deadlines, preconditions, clocks, caps | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo V pp. 123–135 (via DG45 §3.2; §3.3 contingency types) |
| LB-008 | Normativa de Cumplimiento DTE v1.2 (18_), §13.1.1 Cuadro 2 y §§13.1.2–13.4 | DTE Regulation v1.2: invalidation taxonomy (business-effect semantics) and contingency model (mid authority; semantics carried per R6, clocks superseded by 45_ Cuadro 5) | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §13 pp. 19–22 (EVID-075/076) |
| LB-009 | Manual de Eventos de Invalidación y Contingencia v1.1 (2022) | 2022 events manual: invalidation state effects, replacement rules, contingency model (historical; carried where 45_/52_ are silent) | `sv/sources/41_manual_eventos_invalidacion.md` | §§2–3 (EVID-037–044) |
| LB-010 | Esquemas JSON DTE/Eventos, 11-ago-2026 | Official JSON Schemas: invalidacion v3, contingencia v4, fe-eret v1, fe-eop v1 (wire-format authority; read directly 2026-08-17) | `sv/sources/52_Json_Schemas_DTE_Eventos_2026-08-11.zip` | schema files (EVID-087 + direct read) |
| LB-011 | Catálogos de Facturación Electrónica v1.1 (jul-2026) | e-Invoicing Catalogs v1.1: CAT-002 (17/18 event codes), CAT-005 (contingency motives 1–5), CAT-011 (tipo item), CAT-022 (identification docs), CAT-023 (Operaciones Especiales 02/97), CAT-024 (Motivo del evento 1/2/3) | `sv/sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx` | sidecars in [../catalogs/](../catalogs/) (EVID-086) |
| LB-012 | Ley IVA, Arts. 62–63 | IVA Law Arts. 62–63: débito/crédito adjustment windows backing post-invalidation-window NC/ND adjustments | `sv/sources/01_Ley_IVA.pdf` | Arts. 62–63 pp. 27–29 (EVID-054) |
| LB-013 | Product architecture decision log D1/D2/D3/D6 | SaaS-side event generation via private minimal protocol; Tier A client mirror; shared protocol core (binding architecture constraint) | `shared/docs/saas-thin-client-architecture.md` | §S0.5 D1, D2, D3, D6 |
| LB-014 | Manual Tecnológico para la Integración v2.0 (46_), §§4–5 | Technology Integration Manual v2.0: event endpoints (`/fesv/contingencia`, `/fesv/anulardte`), retry policy feeding the contingency trigger | `sv/sources/46_Manual_Tecnologico_Integracion_v2.0_2026-05-25.pdf` | §§4–5 (EVID-085) |

## 3. Functional Requirements

### 3.1 Shared event requirements (all four events)

- **SV-EINV-FR-087:** The system shall support the four event types with their CAT-002 v1.1 identities: *Evento de Invalidación* (invalidation, structural — carries no tipoEvento field), *Evento de Contingencia* (contingency, structural), *Evento de Retorno* (return, tipoEvento "18") and *Evento de Operaciones Especiales* (special operations, tipoEvento "17"); events are signed JSON messages legally distinct from DTEs (CT Art. 119-A event power; 2022 principle carried per EVID-036). (LB-001; LB-011; EVID-084/086)
- **SV-EINV-FR-088:** The system shall stamp each event with its authoritative JSON `version`: invalidación = 3, contingencia = 4, retorno = 1, operaciones especiales = 1. The 52_ schemas are authoritative (contingencia `const: 4`, invalidacion `const: 3`, fe-eret/fe-eop `const: 1`, verified by direct read); Anexo V N°1 prints "3" for contingencia and is superseded by the later schema set (master-index R7 amendment → OQ-001). (LB-010; DG45 §2 vs 52_; R7)
- **SV-EINV-FR-089:** The system shall generate each event's `codigoGeneracion` as a UUID v4, 36 characters including 4 hyphens, digits and UPPERCASE letters only, unique per event. (LB-007 N°7; LB-010)
- **SV-EINV-FR-090:** The system shall generate, validate, sign and transmit all four event types exclusively in the SaaS core via the private minimal protocol (D2); the Odoo client shall initiate events with protocol payloads, receive event state pushes, render the event's Representación Gráfica where produced, and mirror every sealed event file in the Tier A local archive (D3). (LB-013)
- **SV-EINV-FR-091:** The system shall enforce affected-before-affecting ordering for events: an invalidation or retorno event may only reference a DTE or event that is already transmitted and sealed, and a DTE may only be affected by an event if it is already transmitted; dependent events shall be held in the SaaS queue until their target is sealed (cross-ref `02_transmission.md` FR-074/075). (LB-005 §9.2; EVID-084)
- **SV-EINV-FR-092:** The system shall obtain and archive the 40-character alphanumeric `selloRecibido` for every event, excepting retorno operations generated in contingency (Anexo V N°121); a rejected event follows the 24-hour same-codigoGeneración correction rule owned by `02_transmission.md` FR-078/079. (LB-007 N°121; DG45 §4; cross-ref 02)
- **SV-EINV-FR-093:** The system shall emit the shared identification fields per event: `ambiente` from CAT-001 (00 pruebas / 01 producción); `tipoEvento` const "18"/"17" for retorno/OpEsp only; the merger NIT field (`fusion` per schemas) for invalidación and retorno, null or a 9/14-digit NIT on the AT merged-contributors list; `tipoMoneda` = "USD" for retorno and OpEsp. (LB-006 N°2/7/8/13/14; LB-010; DG45 §2.1)
- **SV-EINV-FR-094:** The system shall enforce the event timestamp windows: an event emission date may be any date up to 5 days after the event generation without crossing into the next tax period, and the emission-time fields accept a 30-minute holgura on the last day of a month (Anexo V N°9/11/12, per-event field names per schema: invalidación/retorno/OpEsp use fecEmi/horEmi, contingencia uses fTransmision/hTransmision). (LB-007 N°9/11/12; LB-010)
- **SV-EINV-FR-095:** The system shall run every event through the transmission state machine of `02_transmission.md` (transitorio → procesado/rechazado; invalidado reachable for events themselves), push each event state change to the client, and expose a per-event state surface including seal, rejection reason and deadline countdowns. (LB-013 D2/D6; cross-ref 02 FR-076/080)

### 3.2 Evento de Invalidación

- **SV-EINV-FR-096:** The invalidation event, once sealed, shall flip the target DTE or event to state INVALIDADO; the target is never deleted from the MH database and its status is visible in public consultation; the client shall mark the target non-deliverable and flag the CT 206 consequence that an invalidated DTE's RG loses deductibility. (LB-009 §2 EVID-037; cross-ref 02 FR-081)
- **SV-EINV-FR-097:** The system shall emit `motivo.tipoAnulacion` (CAT-024 "Motivo del evento") with its business-effect semantics per Cuadro 2 + Art. 119-E: code 1 = errors not affecting the underlying operation (data-entry: date, name, description — all document types); code 2 = total rescission of the operation (types CCFE, NRE, NCE, NDE, CLE, CRE, DCLE, FSEE, CDE); code 3 = FE/FEXE-only rescission or operation-affecting adjustment (price reduction, product change), the FE/FEXE adjustment path being invalidation + reissue of a corrected document. (LB-008 §13.1.1 Cuadro 2; LB-002; LB-011 CAT-024; R6)
- **SV-EINV-FR-098:** The invalidation motive block shall carry `motivoAnulacion` (max 200 characters, describing the erroneous fields), the responsible party (nombreResponsable + tipDocResponsable + numDocResponsable, CAT-022 identification) and the requesting party (nombreSolicita + tipDocSolicita + numDocSolicita — the receiver's data, or the emitter's again when self-requested). (LB-006 N°110–117; LB-010 schema keys; EVID-040 carried)
- **SV-EINV-FR-099:** The system shall copy the target document's receptor block (tipoDocumento, numDocumento, nombre, telefono, correo) exactly from the DTE, null where null in the origin; for FE/FEXE/FSEE targets the event shall satisfy Art. 119-E receiver identification (NIT, passport for foreigners, foreign registry number for non-domiciled parties; donor identification for CDE); codPais/nombrePais shall be emitted only for FEXE targets. (LB-002; LB-006 N°49–55; DG45 §3.2)
- **SV-EINV-FR-100:** The invalidation event shall target exactly one document per event via the quad `documento.tipoDte`, `codigoGeneracion` of the target, the target's `selloRecibido` (40 chars), `numeroControl` (null when the target is an event — Anexo V N°46 prints the null-types "16/17/18" under a code scheme that conflicts with CAT-002 v1.1 → OQ-003) and the target's `fecEmi`; the v2.0-eliminated monto field shall not be emitted. (LB-006 N°43–47; LB-010; DG45 §2.2)
- **SV-EINV-FR-101:** The system shall enforce the replacement-code rules for `codigoGeneracionR` (36 chars): emitted only for tipoInvalidación 1 or 3; the replacement DTE must already be transmitted and sealed before the event is transmitted; null for tipoInvalidación 2 (rescission keeps a single reference); null for the adjustment/liquidation types listed in Anexo V N°48 (OCR "05, 08, 16, 17, 18" → OQ-003). After an invalidation window expires, CCF and CR remain adjustable via NCE/NDE within the Ley IVA Arts. 62–63 deadlines. (LB-006 N°48; LB-002; LB-012; EVID-039 carried; R6)
- **SV-EINV-FR-102:** The system shall block invalidation events failing the precondition rules: a CCFE or CRE with an active (uninvalidated) NCE/NDE adjustment must have the NC/ND invalidated first; an FE/FEXE/FSEE with an applied Evento de Retorno must have the retorno event invalidated first. (LB-007 N°43–48; DG45 §3.2; R6)
- **SV-EINV-FR-103:** The system shall enforce the differentiated invalidation deadlines, measured from the target's seal: CCFE, CRE, NCE and NDE ⇒ 1 day; CLE and DCLE ⇒ the first 10 días hábiles of the month following the settlement period; NRE, CDE, Evento de Retorno and Evento de Operaciones Especiales ⇒ 4 calendar days; FE, FEXE and FSEE ⇒ 3 months, extended to 2 years when the emitter's actividad-económica code is one of {21001, 21008, 46482, 46484, 46491, 47721} (scope of the 2-year rule → OQ-002). (LB-007 N°9 + N°43–48; DG45 §3.2; R6)
- **SV-EINV-FR-104:** The system shall enforce the event-date correspondence rules of Anexo V N°9: when invalidating a DTE other than FE/FEXE/FSEE (or an event), the event's date shall match the target's fecEmi/fecEvento; for FE/FEXE/FSEE targets the event date may be up to 3 months after the target's generation (OCR-mixed rule → OQ-002). (LB-007 N°9; DG45 §3.2)
- **SV-EINV-FR-105:** The system shall refuse (no sello) any invalidation event transmitted after its deadline, in which case the target DTE retains its original validity; the client shall warn before submission when the deadline is expired or expiring. (LB-007 N°43–48; EVID-038 carried)
- **SV-EINV-FR-106:** The system shall sequence invalidation-with-replacement per the ordering rule: the replacement DTE referenced by codigoGeneracionR is transmitted and sealed before the invalidation event, and the SaaS queue shall hold the event until the replacement's seal arrives. (LB-005 §9.2; LB-006 N°48; EVID-039 carried; cross-ref FR-091)

### 3.3 Evento de Contingencia

- **SV-EINV-FR-107:** The system shall enter contingency mode only after the retry policy is exhausted (8-second timeout, status query, at most 2 resends — `02_transmission.md` FR-064) or when a force-majeure condition per CAT-005 applies (1 MH system unavailability, 2 emitter system unavailability, 3 emitter Internet outage, 4 emitter power outage, 5 otro with motive text), always provided generation and RG delivery remain possible; the escalation decision is made SaaS-side and flagged to the client. (LB-008 §13.1.2; LB-011 CAT-005; LB-014; R4, R11)
- **SV-EINV-FR-108:** The system shall restrict contingency generation and contingency-event detail entries to DTE types 01-FE, 03-CCFE, 04-NRE, 05-NCE, 06-NDE, 07-CRE, 11-FEXE, 14-FSEE plus the Evento de Retorno (18); CLE, DCLE and CDE shall never appear in a contingency event detail nor be generated with modelo/transmisión 2 (R2; cross-ref `01_document-types.md` FR-013). (LB-006 Sección 4; LB-007 N°34–36; DG45 §3.3; R2)
- **SV-EINV-FR-109:** The contingency event shall carry the motive block with `fInicio`/`fFin` (fFin ≥ fInicio), `hInicio`/`hFin` (hFin > hInicio), `tipoContingencia` from CAT-005 and `motivoContingencia` (max 500 characters, emitted only for code 5 — schema maxLength 500 resolves MOQ-02). (LB-006 N°37–42; LB-010 schema; MOQ-02 resolved)
- **SV-EINV-FR-110:** The contingency event detail (`detalleDTE`) shall list consecutive items (noItem ≥ 1) with at most 1000 items per event — more than 1000 declared documents requires a new contingency event; different DTE types may mix within one event; each item carries exactly one codigoGeneración; detailed documents must be unsealed and not invalidated at declaration time. (LB-006 N°34–36; LB-010 schema maxItems 1000; R9)
- **SV-EINV-FR-111:** The system shall transmit the contingency event at most 24 hours after the contingency (force majeure) ends, with no event date earlier than the contingency; the client shall surface the 24-hour countdown from the moment the SaaS declares the contingency ended. (LB-007 N°10; LB-005 §9 Cuadro 5; EVID-084)
- **SV-EINV-FR-112:** The system shall transmit every declared document at most 72 hours after the contingency event's seal, via uno-a-uno or lote, with the batch containing only documents declared in the event (normal-transmission documents may not join); contingency lots are received by the MH 24 hours a day, 365 days a year (cross-ref 02 FR-066); each document is then individually sealed. (LB-005 §9 Cuadro 5; LB-008 §13.2 EVID-042; LB-014)
- **SV-EINV-FR-113:** The system shall correct and retransmit a rejected contingency event within 24 hours of the rejection communication under the same-code correction rule (cross-ref 02 FR-078). (LB-008 §13.4 EVID-042; LB-014)
- **SV-EINV-FR-114:** The system shall reflect contingency operations in declarations only once the documents are sealed, keep books by generation date including contingency documents (cross-ref 02 FR-083), and flag sanction exposure per CT 239-A d)/g)/h) when the event or document clocks are breached, noting that timely compliance with Art. 119-F exempts 239-A g)/h). (LB-003; LB-004; LB-008 §13.2 EVID-076)

### 3.4 Evento de Retorno

- **SV-EINV-FR-115:** The retorno event (tipoEvento "18", schema fe-eret v1) shall report returns of goods sold or purchased and diminutions/refunds of services, covering: receiver or third-party returns under FE/FEXE/FSEE documents; hidden-defect service refunds; *envase/empaque* (packaging) deposit recovery; *reimportación* (re-import) of exported goods; and export value diminution through loss or damage. (LB-005 §4/§13.3; EVID-084; LB-010)
- **SV-EINV-FR-116:** The retorno event shall reference only sealed documents of types 01-FE, 11-FEXE or 14-FSEE in `documentoRelacionado` (1–50 entries, all of the same type, each with codigoGeneracion + fechaEmision); one codigoGeneración may appear in at most one entry per event, multiple retorno events per document are allowed, and every related codigoGeneración shall appear across the cuerpo items' codigoGeneración field. (LB-006 N°15–17 + N°67; LB-010 schema 1..50; DG45 §3.2)
- **SV-EINV-FR-117:** The system shall enforce the retorno deadline — transmission at most 3 months from the seal of the related document — and shall support both event transmission modalities of Cuadro 5: normal-previa, or normal-diferida with transmission at most 1 day after generation and delivery (the events-only differential mode); when generated in contingency, the 24 h/72 h clocks of Section 3.3 apply. (LB-005 §9 Cuadro 5; LB-007 N°9; EVID-084)
- **SV-EINV-FR-118:** The system shall apply the retorno fiscal effects per related-document type: FE ⇒ decrease of the sale and of the IVA débito; FEXE ⇒ decrease of the export value and of the *remanente de crédito fiscal* (remaining tax credit); FSEE ⇒ decrease of purchases; no crédito fiscal shall be generated for the receptor. (LB-005 §13.3; EVID-084)
- **SV-EINV-FR-119:** The system shall enforce the retorno boundary rules: a retorno is not a discount; item values may not exceed the origin document's values; a retorno is not itself adjustable by event or document; a retorno does not invalidate the origin document even at 100% of its value; and the retorno event itself is invalidable under the 4-calendar-day deadline of FR-103. (LB-005 §13.3; EVID-084; LB-007 N°43–48)
- **SV-EINV-FR-120:** The system shall enforce the per-item value caps and type rules: ventaNoSuj/ventaExenta/ventaGravada/compra may not exceed the origin item values; `ivaRete` is capped at (ventaGravada / 1.13) × 1%; `reteRenta` at 10% (FSEE origins); FEXE origins ⇒ ventaNoSuj = ventaExenta = $0.00 with seguro/flete emitted; FSEE origins ⇒ ventaGravada = $0.00 using `compra`; tipoItem uses CAT-011 (code 3 forbidden for FEXE); cantidad = 1 for cargos/abonos or tipoItem 4; the body holds at most 2000 items. (LB-007 N°61–88; LB-010 schema; DG45 §3.2)
- **SV-EINV-FR-121:** The retorno event shall copy the receptor block exactly from the origin document (null where null), copy `ventaTercero` from the origin (null for FSEE) with `codDomiciliado` per CAT-032 matching the origin FE/FEXE (FE v1/FEXE v1–v2 origins admit any CAT-032 code), and copy `compraTercero` from FEXE origins (null for FE/FSEE). (LB-007 N°49–60; LB-010; DG45 §3.2)
- **SV-EINV-FR-122:** The retorno resumen shall compute subTotalVentas = totalNoSuj + totalExenta + totalGravada + totalCompraExcluidos; montoTotalOperacion = subTotalVentas + tributos + totalSeguro + totalFlete; totalPagar = montoTotalOperacion − ivaRete − reteRenta ± cargos/abonos, floored at $0.00 when abonos exceed the monto; every computed resumen field accepted within the +$0.01 holgura; `totalNoOnerosas` reported for FEXE origins. (LB-007 N°89–109; LB-010 schema keys; DG45 §3.2)
- **SV-EINV-FR-123:** The retorno event may be generated in contingency (tipoModelo 2 / tipoOperación 2 with CAT-005 tipoContingencia and motivoContin per schema) as the only event type admitted in the contingency detail besides DTEs; its sello exception (operations generated in contingency) is governed by FR-092. (LB-006 N°3–6; LB-007 N°3–4 + N°35; LB-010; DG45 §3.3)

### 3.5 Evento de Operaciones Especiales

- **SV-EINV-FR-124:** The OpEsp event (tipoEvento "17", schema fe-eop v1) shall be the monthly reporting vehicle for special operations — physical *Factura de Venta Simplificada* (FVS) and CT Art.-113 *Comprobantes de Control Interno* (internal-control documents) — and may be emitted only by taxpayers designated by the AT, only with tipoModelo 1 and tipoOperación 1 (no contingency mode; schema const 1). (LB-005 §13.4; LB-007 N°18 + N°3–4; LB-010; EVID-084/086)
- **SV-EINV-FR-125:** The OpEsp body shall classify each item with `tipoDocumento` from CAT-023 (Operaciones Especiales): code 02 = FVS reported as a document range with `docDel`/`docAl` (max 36 characters each) required and `numDocumento` null; code 97 = Comprobantes de Control Interno reported individually with `numDocumento`. (LB-006 N°63–64 + N°73–74; LB-011 CAT-023; LB-010; R5)
- **SV-EINV-FR-126:** The system shall enforce the OpEsp reporting deadline — transmission within the first 10 días hábiles of the month following the reported operations — with an overdue flag and CT 239-A g)/h) exposure surfaced to the client when breached. (LB-005 §13.4; EVID-084; LB-004)
- **SV-EINV-FR-127:** The OpEsp body shall enforce: `codigoGeneracionRef` referencing an active prior OpEsp event when adjusting previously reported operations; origin documents admitted when their fechaEmision is at most 3 months before the event; annulments of reported operations emitted as positive values referencing the prior EOE's codigoGeneración, with one generation code used consistently across all items referencing it; cantidad as integers > 0, fixed at 1 when a documento origen, cargos/abonos or tipoItem 4 applies; body cap 2000 items. (LB-007 N°61–68; LB-010 schema)
- **SV-EINV-FR-128:** The OpEsp resumen shall compute `total` = subTotal + tributo value, with tributo code C3 stated at $0.00, and totals within the +$0.01 holgura. (LB-007 N°89–104; LB-010)
- **SV-EINV-FR-129:** The system shall encode the coexistence rule: AT-authorized FVS and Art.-113 internal-control systems may coexist with DTE emission if and only if the OpEsp event is transmitted; pre-Normativa Art.-115 systems (tiquetes) may not coexist and are banned for DTE emitters since 01-Jan-2025 (R12; business decision on an Odoo FVS print flow → OQ-004 per MOQ-06). (LB-005 §13.4/§15; EVID-084; R12)

## 4. Data Model

The MH event JSON exists only SaaS-side (D2); this section records the
semantic contract both sides honor. Wire-format key names follow the 52_
schemas, NOT the Anexo III unified table names (verified divergences:
invalidación/retorno use `fecEmi`/`horEmi` and `fusion`; contingencia uses
`fTransmision`/`hTransmision`; eret uses `tipoOperacion`, `motivoContin`,
`codTributo`, `totalCompraExcluidos`, `ivaRete`, `totalNoOnerosas`,
`ventaTercero.codDomiciliado`; eop uses `docDel`/`docAl`). Catalog sidecars
live in [../catalogs/](../catalogs/) (CAT-002, CAT-005, CAT-011, CAT-022,
CAT-023, CAT-024).

**Event type registry** (seed data):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.event.type | key | char | invalidacion · contingencia · retorno · operacion_especial | FR-087 |
| l10n_sv_edi.event.type | json_version | integer | 3 · 4 · 1 · 1 (52_ schema consts) | FR-088 |
| l10n_sv_edi.event.type | tipoEvento | char(2) null | 18 · 17 · null (structural events) | FR-087; CAT-002 |
| l10n_sv_edi.event.type | detail_cap | integer | contingencia 1000 · retorno/OpEsp body 2000 · invalidación 1 target | FR-100/110/120/127 |
| l10n_sv_edi.event.type | contingency_allowed | boolean | true: retorno · false: OpEsp (structural for the other two) | FR-123/124 |

**Invalidación:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.event.invalidacion | documento.tipoDte / codigoGeneracion / selloRecibido / numeroControl / fecEmi | char(2)/char(36)/char(40)/char(31)/date | single sealed target; numeroControl null for event targets | FR-100 |
| l10n_sv_edi.event.invalidacion | codigoGeneracionR | char(36) null | replacement, sealed first; null for tipo 2 + N°48 types | FR-101/106 |
| l10n_sv_edi.event.invalidacion | motivo.tipoAnulacion | select CAT-024 | 1 error · 2 rescission · 3 otro (business semantics per Cuadro 2) | FR-097 |
| l10n_sv_edi.event.invalidacion | motivoAnulacion | char(200) | erroneous-field description | FR-098 |
| l10n_sv_edi.event.invalidacion | responsable / solicitante | char + CAT-022 doc | name + doc type + doc number each | FR-098 |
| l10n_sv_edi.event.invalidacion | deadline_basis | computed | per-type: 1d · 10 háb · 4d · 3mo · 2y (activity codes) | FR-103 |

**Contingencia:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.event.contingencia | motivo.fInicio/fFin/hInicio/hFin | date/date/time/time | fFin ≥ fInicio; hFin > hInicio | FR-109 |
| l10n_sv_edi.event.contingencia | motivo.tipoContingencia | select CAT-005 | 1–5 | FR-107/109 |
| l10n_sv_edi.event.contingencia | motivo.motivoContingencia | char(500) null | only code 5 | FR-109 |
| l10n_sv_edi.event.contingencia | detalleDTE[] | 1..1000 items | noItem 1..1000 · tipoDoc (01,03,04,05,06,07,11,14,18) · codigoGeneracion | FR-108/110 |
| l10n_sv_edi.event.contingencia | clock_event / clock_docs | datetime | end+24h / event-seal+72h | FR-111/112 |

**Retorno (fe-eret v1):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.event.retorno | documentoRelacionado[] | 1..50 | tipoDocumento ∈ {01, 11, 14} · codigoGeneracion(36) · fechaEmision; same type; sealed | FR-116 |
| l10n_sv_edi.event.retorno | cuerpoDocumento[] | 1..2000 | tipoItem CAT-011 · codigoGeneracion · cantidad · codTributo · ventaNoSuj/Exenta/Gravada · compra · ivaRete · reteRenta · seguro/flete (FEXE) · psv/ivaItem (FE) · noGravado | FR-120 |
| l10n_sv_edi.event.retorno | ventaTercero.codDomiciliado | select CAT-032 | copied from origin; null for FSEE | FR-121 |
| l10n_sv_edi.event.retorno | resumen | computed | subTotalVentas · montoTotalOperacion · totalPagar (formulas FR-122) · totalNoOnerosas (FEXE) · totalCompraExcluidos | FR-122 |

**Operaciones Especiales (fe-eop v1):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.event.opesp | cuerpoDocumento[] | 1..2000 | codigoGeneracionRef · tipoDocumento CAT-023 (02/97) · numDocumento (97 only) · fechaEmision · docDel/docAl(36) (02 only) · cantidad (integer >0) | FR-125/127 |
| l10n_sv_edi.event.opesp | resumen | computed | subTotal · total = subTotal + tributo (C3 = $0.00) | FR-128 |
| l10n_sv_edi.event.opesp | reporting_deadline | computed | 10 primeros días hábiles of following month | FR-126 |

**Client-mirrored event fields** (private protocol):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.event (client mirror) | state / sello / codigo_msg / observaciones | select / char(40) / char / text list | per 02 state contract | FR-092/095 |
| l10n_sv_edi.event (client mirror) | deadline_at / deadline_kind | datetime / select | invalidación group · contingencia 24h/72h · retorno 3mo/1d · OpEsp 10-hábiles | FR-103/111/112/117/126 |
| account.move (DTE) | invalidated_by_event / retorno_event_ids | many2one/many2many | state-flip lineage | FR-096/119 |

## 5. Odoo Mapping

Layer semantics per the architecture doc: `saas` = event generation,
validation and MH transmission in the Elixir core (the client never builds
event JSON); `odoo` = initiation UX, state/deadline surfaces and archive
mirroring in the LGPL client; `shared` = private-protocol contract items
both sides must honor. Model names are stable across Odoo 17/18/19/20;
nothing in this file requires version-specific behavior.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-087 | saas | l10n_sv_edi.event.type | key, tipoEvento | Registry seeded per CAT-002; per-event enablement gated by acreditamiento (A11) |
| FR-088 | saas | l10n_sv_edi.event.type | json_version | Stamped at generation; contingencia = 4 per 52_ (OQ-001 record) |
| FR-089 | saas | — | codigoGeneracion | UUID v4 server-side; mirrored to client |
| FR-090 | shared | l10n_sv_edi.event | protocol payload contract | D2/D3: client initiates, never compiles; Tier A mirror at response time |
| FR-091 | saas | saas.transmission_queue | depends_on | Same dependency edges as 02 FR-074/075 |
| FR-092 | saas | l10n_sv_edi.event | l10n_sv_edi_sello | Sello exception rule for contingency retorno encoded SaaS-side |
| FR-093 | saas | — | — | Identification fields at compilation |
| FR-094 | saas | — | — | Timestamp windows at generation + transmission |
| FR-095 | shared | l10n_sv_edi.event | state fields | State vocabulary = 02 contract; deadline countdowns pushed |
| FR-096 | odoo | account.move | l10n_sv_edi_state = invalidado | State flip on event seal; deduction flag + RG warning surfaced |
| FR-097 | shared | l10n_sv_edi.event.invalidacion | motivo.tipoAnulacion | Motive picker with Cuadro-2 semantics in odoo UX; validation SaaS-side |
| FR-098 | odoo | l10n_sv_edi.event.invalidacion | motive + party fields | Capture form; CAT-022 doc pickers |
| FR-099 | saas | — | — | Receptor copy at compilation; 119-E ID rules authoritative SaaS-side |
| FR-100 | saas | account.move | target lookup by codigoGeneracion | Single-target contract; odoo picker filters sealed docs |
| FR-101 | saas | l10n_sv_edi.event.invalidacion | codigoGeneracionR | Replacement gate (sealed-first); N°48 null-set (OQ-003) |
| FR-102 | saas | account.move | active-adjustment / applied-event checks | Precondition evaluation server-side; odoo shows the blocking reason |
| FR-103 | saas | l10n_sv_edi.event | deadline_at | Deadline table = core IP; activity-code 2-year lookup from emitter profile |
| FR-104 | saas | — | — | Date-correspondence at validation |
| FR-105 | odoo | l10n_sv_edi.event | deadline warning banner | Pre-submission warning client-side; refusal handled SaaS-side |
| FR-106 | saas | saas.transmission_queue | depends_on | Replacement-before-event edge |
| FR-107 | saas | res.company / saas session | contingency_mode flag | Escalation decision server-side; client banner + generation continues |
| FR-108 | saas | account.move | l10n_latam_document_type_id | Type gate (mirrors 01 FR-013); odoo blocks excluded types in UX |
| FR-109 | shared | l10n_sv_edi.event.contingencia | motive quad + CAT-005 | Period capture in odoo; motive text ≤500 enforced both ends |
| FR-110 | saas | l10n_sv_edi.event.contingencia | detalleDTE | >1000 ⇒ auto-split into successive events; odoo pre-check |
| FR-111 | saas | l10n_sv_edi.event | clock_event | 24h countdown pushed to client |
| FR-112 | saas | saas.transmission_queue | declared-docs batch | Only declared docs; 24/7 lot window (02 FR-066) |
| FR-113 | saas | — | — | Rejection path per 02 FR-078 |
| FR-114 | odoo | account.move | sanction-risk banner | Declarations gated on seal (books per 02 FR-083) |
| FR-115 | saas | l10n_sv_edi.event.retorno | case classification | Case taxonomy drives odoo wizard labels |
| FR-116 | saas | account.move | retorno target picker | Sealed 01/11/14 only; ≤50 same-type; odoo picker enforces |
| FR-117 | saas | l10n_sv_edi.event | transmission_mode + deadline | 3mo/1d clocks; modality per Cuadro 5 |
| FR-118 | saas | account.move | effect postings | Fiscal-effect postings SaaS-computed; odoo journal entries mirror |
| FR-119 | saas | l10n_sv_edi.event.retorno | boundary checks | Not-a-discount/exceed/origin rules authoritative SaaS-side |
| FR-120 | saas | l10n_sv_edi.event.retorno | cuerpo validation | Caps + per-type zero rules at compilation |
| FR-121 | saas | — | — | Copies at compilation |
| FR-122 | saas | l10n_sv_edi.event.retorno | resumen formulas | +$0.01 holgura; formulas core IP |
| FR-123 | saas | l10n_sv_edi.event.retorno | contingency fields | Retorno-in-contingency compilation |
| FR-124 | saas | res.company | at_designated flag | AT-designation gate for OpEsp; modelo/transmisión const 1 |
| FR-125 | shared | l10n_sv_edi.event.opesp | tipoDocumento CAT-023 | Range vs individual capture in odoo staging; validation SaaS-side |
| FR-126 | odoo | l10n_sv_edi.event | reporting deadline banner | Monthly 10-hábiles countdown; sanction flag |
| FR-127 | saas | l10n_sv_edi.event.opesp | cuerpo validation | Ref/annulment rules; 3-month origin window |
| FR-128 | saas | l10n_sv_edi.event.opesp | resumen | C3 $0.00 rule |
| FR-129 | odoo | res.company | fvs_authorized flag | Coexistence gate surfaced; FVS print flow decision → OQ-004 |

## 6. Acceptance Criteria

- **AC-001:** Given each of the four events is generated, when the JSON is compiled, then `identificacion.version` equals 3 (invalidación), 4 (contingencia), 1 (retorno) and 1 (OpEsp) per the 52_ schema consts (FR-088).
- **AC-002:** Given a CCFE sealed at T, when an invalidation event for it is transmitted at T+2 days, then the MH refuses it (no sello) and the CCFE retains its original valid state, with the refusal surfaced to the client (FR-103/105).
- **AC-003:** Given a CLE for period P, when an invalidation event is transmitted after the 10th día hábil of the month following P, then it is refused; transmitted within those 10 días hábiles, then it is accepted (FR-103).
- **AC-004:** Given a CCFE with an active (uninvalidated) NCE adjusting it, when an invalidation event for the CCFE is initiated, then it is blocked with the reason "invalidate the NC/ND first"; after the NCE's own invalidation is sealed, then the CCFE event is admitted (FR-102).
- **AC-005:** Given an FE with an applied sealed retorno event, when an invalidation of the FE is attempted, then it is blocked until the retorno event is invalidated first (FR-102).
- **AC-006:** Given an invalidation with tipoAnulacion = 2 and codigoGeneracionR filled, then the SaaS rejects the event; with codigoGeneracionR null, then it passes structure validation (FR-101).
- **AC-007:** Given an invalidation whose codigoGeneracionR references a replacement DTE not yet sealed, when the queue is evaluated, then the event is held blocked-by-dependency and released once the replacement's seal arrives (FR-091/106).
- **AC-008:** Given a contingency declaring 1,001 documents, when the event is assembled, then it splits into two events (≤1000 items each); given a detail of 1,000 items, then a single event compiles (FR-110).
- **AC-009:** Given a contingency event detail containing a CLE/DCLE/CDE entry, or a document already sealed or invalidated, then the SaaS rejects the event (FR-108/110).
- **AC-010:** Given a contingency that ends at T, when the event is transmitted at T+25 h, then it is refused as out of window and the sanction exposure (CT 239-A h) is flagged; at T+23 h, then it is admitted (FR-111/114).
- **AC-011:** Given a contingency event sealed at S, when a declared document is transmitted at S+73 h, then it is flagged overdue with 239-A d) exposure; at S+71 h, then it is within window (FR-112/114).
- **AC-012:** Given a motivoContingencia text of 501 characters for CAT-005 code 5, then client pre-validation blocks it before any SaaS call (FR-109).
- **AC-013:** Given a retorno event relating an NRE (04) or a 51st document, or mixing 01 and 11 in one event, then the SaaS rejects it (FR-116).
- **AC-014:** Given a retorno item whose ventaGravada exceeds the origin item's value, or an FSEE-origin item with ventaGravada ≠ $0.00, then the SaaS rejects the event (FR-120).
- **AC-015:** Given a retorno covering 100% of an FE's value and sealed, then the FE's state becomes ajustado (not invalidado), its deductibility flag reflects the retorno, and no crédito fiscal is generated for the receptor (FR-118/119).
- **AC-016:** Given a non-AT-designated emitter, when an OpEsp event is initiated, then generation is blocked; given an OpEsp item with tipoDocumento 02 and docDel/docAl missing or numDocumento filled, then the SaaS rejects it (FR-124/125).
- **AC-017:** Given FVS operations from month M, when the OpEsp event is transmitted after the 10th día hábil of M+1, then an overdue flag with CT 239-A g)/h) exposure is raised; within the window, then no flag (FR-126).
- **AC-018:** Given an OpEsp item adjusting a prior EOE whose codigoGeneracionRef points to a sealed-then-invalidated (inactive) event, then the SaaS rejects it; pointing to an active one, then it passes (FR-127).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Contingencia `version`: Anexo V N°1 (45_, May-2026) prints 3, but the 52_ schema (Aug-2026, later authority) sets const 4 — requirements adopt 4 (FR-088). Master-index R7 ("contingencia 3 ... confirmed by 52_") needs amendment. Confirm no Normativa/schema cycle mismatch at implementation. | no | Takumi (schema pass) | open |
| OQ-002 | Anexo V N°9 scope (OCR-mixed): does the 2-year window for emitter activity codes {21001, 21008, 46482, 46484, 46491, 47721} attach to invalidation of FE/FEXE/FSEE (written FR-103), to retorno transmission windows, or both? Likewise the "same date as the invalidado" correspondence (FR-104) and which date fields it binds — the invalidación schema carries fecEmi/horEmi (no fecEmiEvento). Confirm from 45_ original tables or AT guidance. | no | Takumi synthesis wave 1 | open |
| OQ-003 | Anexo V N°48 codigoGeneracionR null-type list prints "05, 08, 16, 17, 18" under a code scheme conflicting with CAT-002 v1.1 (CLE=08/DCLE=09/CDE=15 vs 15/16/17 in DG45 §3.3 parentheticals — see `01_document-types.md` OQ-008); schemas encode tipoDte as free string so the business rule is not machine-checkable. Confirm the exact null-set (presumably NCE + liquidation/donation types + events). | no | Takumi (schema pass) | open |
| OQ-004 | MOQ-06: FVS survives as a PHYSICAL document for AT-authorized DTE emitters, reported monthly via OpEsp — does Odoo need an FVS print/numbering flow (for SMM-threshold users) or is FE always used with OpEsp reporting only for legacy Art.-113 systems? Business decision gating FR-129 client scope. | no | Takumi + SaaS team | open |
| OQ-005 | Wire keys vs Anexo III unified names: 52_ schemas use `tipoOperacion` (eret), `motivoContin`, `tipoAnulacion`/`motivoAnulacion`, `fTransmision`/`hTransmision`, `fusion`, `ventaTercero.codDomiciliado`, `docDel`/`docAl` — diverging from the Anexo III digest names (tipoTransmision, tipoInvalidacion, fecEvento, fusiones, domicilioFiscal, DocDel/DocAl). Schemas govern (noted in §4); confirm the mapping table in the SaaS schema pass so a future Normativa bump renaming keys is caught by the catalog-version SLA. | no | Takumi (schema pass) | open |
| OQ-006 | MOQ-05 (cross-ref `02_transmission.md` OQ-003): Retorno/OpEsp endpoint paths still unpublished — FR-090 depends on the connector integrating them when the AT publishes the services. | no | SaaS team | open |
