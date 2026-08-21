# SV — E-Invoicing — Transmission connector & document state machine

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave 1 |
| Updated | 2026-08-17 |

## 1. Purpose

This file defines the functional requirements for transmitting DTEs and
events to the Ministerio de Hacienda (MH) reception platform and for the
document transmission state machine: authentication and token lifecycle,
the MH reception services (uno-a-uno, lote, consultations, events), the
retry and contingency-escalation policy, lote batching and service
windows, the three transmission modalities and their deadlines, the
emission-time vs transmission-time windows, the affected-before-affecting
ordering rule, the document/event states (*estado transitorio* — transitory
state —, PROCESADO with observaciones/ajustado, RECHAZADO, INVALIDADO), and
the 24-hour same-*códigoGeneración* (generation code) correction rule for
rejected documents. It merges
master-index clusters A2 (transmission & connector) and A8 (state machine
& correction).

Per the product architecture (decisions D1/D2/D6), the MH-facing connector
lives **SaaS-side**: the Odoo thin client never calls MH endpoints; it
speaks the private minimal protocol to the SaaS, which owns
transmission, retry, ordering and state. This file therefore assigns most
logic to the `saas` layer and defines the client-side queue/state surface
(`odoo`) and the state-contract items both sides must honor (`shared`).

It does **not** cover: per-type document structures (`01_document-types.md`),
event semantics, clocks and deadlines per event type (`03_events.md`,
clusters A3–A5), signing and certificates (`04_signing_delivery.md`, A6),
Representación Gráfica / delivery mechanics (`04_signing_delivery.md`, A7),
catalog governance (A9), onboarding/authorization (A11), or the private
protocol's own contract detail (`06_api-protocol.md`, A12). Event
transmission deadlines are owned by `03_events.md`; this file owns the
transport they ride on.

## 2. Legal Basis

Authority order (binding, per master evidence index): 44_/45_/46_/50_/51_/52_
(2026) > 18_/19_/22_ (2025) > 40_/41_/25_ (2022). Conflict resolutions
R4, R11, R15 and R16 from the master index are noted where they apply.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D.L. 487-2022 (reforma al Código Tributario), Arts. 119-A, 119-C y 119-D | Art. 119-A: AT sets transmission rules; 119-C: emission = generation→signature→transmission→delivery; 119-D: transmission rules, seal effects, seal ≠ operation validation | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Arts. 119-A/119-C/119-D (EVID-083) |
| LB-002 | D.L. 487-2022, Arts. 9–10 (CT 199 y 206 reformados) | CT 199: untransmitted DTEs presume taxable income; CT 206: deductions require seal; evidential hierarchy AT copy > taxpayer copy > Representación Gráfica | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Arts. 9–10 (EVID-083) |
| LB-003 | D.L. 487-2022, Art. 2 (CT 141 reformado) | CT 141: books record DTEs by código de generación; contingency/unsealed DTEs recordable; 10 días hábiles backlog | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 2 (EVID-083) |
| LB-004 | Normativa de Cumplimiento DTE v2.0, §§6, 9, 10 y 11.2 | DTE Regulation v2.0: emission modalities (§6), transmission deadlines Cuadros 4–5 + §9.2 ordering rule, sello de recepción rules incl. 24-hour correction (§10), entrega en estado transitorio (§11.2) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | §§6, 9, 10, 11.2 pp. 12–25 (raw-text verified) |
| LB-005 | Normativa v2.0, Anexo I, regla 3 (Transmisión) | Annex I rule 3: environments 00/01, uno-a-uno/lote reception, rule 3.5 service-status consultation (new in v2.0) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I pp. 36–47 (via DG45 §4) |
| LB-006 | Normativa v2.0, Anexo IV, N°10–11 | Annex IV N°10: fecEmi up to 5 days after transmission without crossing the next tax period; N°11: horEmi 30-minute holgura on the last day of the month | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo IV pp. 102–104 (via DG45 §3.1) |
| LB-007 | Manual Tecnológico para la Integración del Sistema de Transmisión v2.0 (46_), §§3.4, 4 y 5.5 | Technology Integration Manual v2.0: authentication service (configurable token validity, once-per-24h guidance), API endpoint inventory, 8-second/2-retry policy, lote caps and service windows | `sv/sources/46_Manual_Tecnologico_Integracion_v2.0_2026-05-25.pdf` | §§3.4, 4, 5.5 pp. 13–19 (EVID-085; raw-text verified) |
| LB-008 | Manual Tecnológico (22_), §§2–5 | Prior technology manual: full API surface (verified identical in 46_ per EVID-085), fixed 24h/48h token validity (superseded by configurable — R15), 1-day-after-fecEmi reception holgura (status in v2.0 unresolved — R16/MOQ-07) | `sv/sources/22_Manual_Tecnologico_Transmision.pdf` | §§2–5 (EVID-079) |
| LB-009 | Normativa de Cumplimiento DTE v1.2 (18_), §§10–10.2 | DTE Regulation v1.2: state taxonomy (Transmitido [Ajustado/Observado]/Rechazado/Invalidado), 24-hour same-code correction then new code, generation-date bookkeeping (mid authority; yields to 45_ where they overlap) | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §§10–10.2 pp. 14–16 (EVID-072) |
| LB-010 | Catálogos de Facturación Electrónica v1.1 (jul-2026) | e-Invoicing Catalogs v1.1: CAT-001 ambiente (00 pruebas / 01 producción), CAT-004 tipo de transmisión (1 normal / 2 contingencia) | `sv/sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx` | CAT-001, CAT-004 sidecars (EVID-086) |
| LB-011 | Product architecture decision log D1–D6 | SaaS-only MH connector, private minimal protocol, shared transmission state machine in the protocol core (binding architecture constraint) | `shared/docs/saas-thin-client-architecture.md` | §S0.5 D1–D6 |

## 3. Functional Requirements

### 3.1 Connector topology & environments

- **SV-EINV-FR-053:** The system shall implement all MH-facing transmission (authentication, reception, consultation, event endpoints, retry, ordering) exclusively in the SaaS core; the Odoo client shall have no code path that calls any MH endpoint directly, communicating only through the private minimal protocol. (LB-011; LB-001 Art. 119-A)
- **SV-EINV-FR-054:** The system shall keep the two MH environments strictly separate with per-environment credentials: ambiente 00 *pruebas* (test, no tax effects) and 01 *producción* (production) per CAT-001; a client configured for one environment shall not be pointed at the other environment's base URL, and test credentials shall never transmit production documents or vice versa. (LB-005; LB-010; LB-007 §4)

### 3.2 Authentication & token lifecycle

- **SV-EINV-FR-055:** The SaaS shall authenticate each emitter per environment via `POST /seguridad/auth` (test host `apitest.dtes.mh.gob.sv`, production host `api.dtes.mh.gob.sv`), form-urlencoded user+password, obtaining the Bearer JWT (with roles) required by every reception service; without a token no reception service is consumable. (LB-007 §4.1; LB-008; EVID-085)
- **SV-EINV-FR-056:** The SaaS shall treat token validity as configurable in the AT platform (R15: not fixed 24h/48h), shall authenticate at least once per 24 hours per the MH guidance, and shall cache and proactively refresh the token before expiry; authentication error codes 100–111 shall be surfaced distinctly from transmission errors. (LB-007 §4.1; LB-008; R15; EVID-085)
- **SV-EINV-FR-057:** The system shall store each emitter's MH API credentials (user/password; password policy 13–25 characters with letters, numbers and specials) encrypted and per environment SaaS-side; credential custody and security risk remain the emitter's legal responsibility, and credentials shall never be exposed through the client or protocol responses. (LB-007 §4; LB-004 §9.2; EVID-085)

### 3.3 MH reception services

- **SV-EINV-FR-058:** The SaaS shall transmit single documents via `POST /fesv/recepciondte` (uno-a-uno) with payload ambiente, idEnvio, version, tipoDte, documento (the signed JWS DTE) and codigoGeneracion; the synchronous response shall be captured in full: estado (PROCESADO/RECHAZADO), selloRecibido, clasificaMsg, codigoMsg and observaciones[]. (LB-007 §4; LB-008; EVID-079/085)
- **SV-EINV-FR-059:** The SaaS shall transmit batches via `POST /fesv/recepcionlote` with idEnvio (UUID v4, uppercase), nitEmisor and at most 100 signed DTEs per *lote* (batch); the platform responds asynchronously with a codigoLote after acknowledging receipt (a 100-DTE lot processes in ~2–4 minutes). (LB-007 §4; LB-008; EVID-079/085)
- **SV-EINV-FR-060:** The SaaS shall poll lote results via `GET /fesv/recepcion/consultadtelote/{codigoLote}` until every DTE in the lot has a final result, applying each per-DTE estado/selloRecibido/observaciones individually. (LB-007 §4; LB-008)
- **SV-EINV-FR-061:** The SaaS shall expose document-level reconciliation via `POST /fesv/recepcion/consultadte` (nitEmisor, tdte, codigoGeneracion), which the retry policy (FR-064/065) and daily consistency runs shall use to detect lost responses and duplicates. (LB-007 §4; LB-008)
- **SV-EINV-FR-062:** The SaaS shall transmit events via `POST /fesv/contingencia` and `POST /fesv/anulardte`; the Retorno and Operaciones Especiales event endpoint paths are not published in Manual Tecnológico v2.0 (MOQ-05) and shall be integrated through the same connector when the AT publishes them. (LB-007 §4; LB-008; EVID-085; → OQ-003)
- **SV-EINV-FR-063:** The SaaS shall consult the reception service status before submission waves per Anexo I rule 3.5 (new in v2.0); the consultation endpoint contract is deferred to AT manuals and shall be integrated when published. (LB-005 rule 3.5; DG45 §4; → OQ-005)

### 3.4 Retry policy & contingency escalation

- **SV-EINV-FR-064:** The SaaS shall implement the MH retry policy per document: if the reception service does not respond within 8 seconds, first query the document's status (consultadte) to check whether it was received; if not received, resend the reception request; repeat the resend at most 2 times; if still unsuccessful, escalate to contingency mode. (LB-007 §5.5; R4; R11; EVID-085)
- **SV-EINV-FR-065:** The SaaS shall apply the same status-query-then-resend sequence when the emitter-side system fails to process a reception response, so that an already-received document is never redundantly retransmitted after a response-processing failure. (LB-007 §5.5; LB-004 §10)

### 3.5 Lote batching & service windows

- **SV-EINV-FR-066:** The SaaS shall schedule lote dispatch inside the MH service windows: test environment at most 100 DTEs per lot and at most 400 lots, received 08:00–17:00; production at most 100 DTEs per lot and at most 400 lots, received 22:00–05:00; contingency lots are received 24 hours a day, 365 days a year; the schedule restriction applies to emitters with *facturación cíclica* (cyclic invoicing). The 22_-era test figure of 300 lots is superseded by 46_ v2.0's 400. (LB-007 §3.4; LB-008; → OQ-004)

### 3.6 Transmission modalities & deadlines

- **SV-EINV-FR-067:** The system shall use *Transmisión Normal Previa* (prior normal transmission) as the default modality for every DTE and event type: transmission to the MH before delivery to the receiver, so the *entrega* (delivery) carries the *sello de recepción* (reception seal). (LB-004 §9 Cuadro 4 regla 1)
- **SV-EINV-FR-068:** The system shall support *Transmisión Normal Diferida* (deferred normal transmission) only when the emitter holds a prior AT resolution (granted exceptionally upon proof that simultaneous transmission and delivery is impossible), only for DTE types FE, CCFE, NRE, NCE, NDE, CRE, FEXE and FSEE, only via lote, with the order generation → signature → entrega in *estado transitorio* → transmission, and with transmission completed at most 1 day after generation and delivery. (LB-004 §6.2 + §9 Cuadro 4 regla 2)
- **SV-EINV-FR-069:** The system shall support *Transmisión Diferida por Contingencia* without prior AT resolution, with the order generation → signature → entrega in estado transitorio → (after the force majeure ceases) transmission of the contingency event → transmission of all documents generated during the contingency, completing document transmission at most 72 hours after the sello of the contingency event, via uno-a-uno or lote. (LB-004 §6.3 + §9 Cuadro 4 regla 3; event clocks owned by `03_events.md`)
- **SV-EINV-FR-070:** The system shall treat deferred documents delivered in estado transitorio as retaining the probative value granted by the Ley de Firma Electrónica until the sello is obtained; if the modality deadline (FR-068/069) passes without transmission and seal, the document shall be marked as not emitted and not effective for tax purposes, with the CT 199 inc. 2 presumed-income consequence flagged, and an overdue alarm raised to the client. (LB-004 §§6.2–6.3, 10; LB-002 CT 199)

### 3.7 Emission-time vs transmission-time windows

- **SV-EINV-FR-071:** The SaaS shall accept for transmission a DTE whose `fecEmi` precedes the transmission, and exceptionally one whose `fecEmi` is up to 5 days after transmission, provided it does not cross into the next tax period (e.g. transmitted 27-June ⇒ fecEmi 28/29/30-June accepted, 01/02-July rejected). (LB-006 N°10; DG45 §3.1)
- **SV-EINV-FR-072:** The SaaS shall accept `horEmi` with a 30-minute *holgura* (tolerance) when emission falls on the last day of a month, covering differences between the emitter's clock and the MH system clock. (LB-006 N°11; DG45 §3.1)
- **SV-EINV-FR-073:** The system shall NOT rely on the 22_-era reception *holgura de transmisión* (documents accepted up to 1 day after fecEmi, except period-end where only +30 minutes applied): it is not restated in 46_ v2.0, and the Normativa v2.0 modalities (FR-067–069) govern deferred transmission instead (R16 — flag until 46_/AT confirm the grace's status). (LB-008; LB-004 §9; R16; MOQ-07; → OQ-002)

### 3.8 Transmission ordering

- **SV-EINV-FR-074:** The SaaS shall enforce affected-before-affecting ordering: DTEs and events that affect, adjust, diminish or invalidate an operation shall be transmitted after the DTE or event they affect; the rule applies to uno-a-uno and lote transmission of DTEs, Evento de Retorno and Evento de Operaciones Especiales, and to uno-a-uno transmission of Evento de Invalidación and Evento de Contingencia; a DTE may only be affected by another DTE, an invalidation event or a retorno event if it is already transmitted (sealed), and likewise an event only by a previously transmitted event. (LB-004 §9.2; EVID-084)
- **SV-EINV-FR-075:** The SaaS shall hold dependent documents in the transmission queue until their dependency is sealed, and shall surface to the client which queue items are blocked and on which dependency. (LB-004 §9.2; LB-011 D2/D6)

### 3.9 Transmission states & correction windows

- **SV-EINV-FR-076:** The system shall maintain this transmission state machine per document/event: *TRANSITORIO* (deferred, signed and delivered, not yet sealed) → *PROCESADO* (received, sello granted) or *RECHAZADO* (rejected); PROCESADO carries the sub-conditions *OBSERVADO* (AT observations that do not affect validity) and *AJUSTADO* (adjusted by a later document/event); *INVALIDADO* is reached via invalidation events (owned by `03_events.md`); rejected-and-abandoned and overdue-transitory documents end as not-emitted. (LB-009 §10; LB-004 §§6, 10; EVID-072)
- **SV-EINV-FR-077:** The system shall treat reception observaciones[] as non-blocking warnings (e.g. codigoMsg 002 "RECIBIDO CON OBSERVACIONES"): they shall be recorded and displayed but shall not block entrega, posting or downstream flows. (LB-007 §4; LB-008; EVID-079)
- **SV-EINV-FR-078:** The system shall correct and retransmit a rejected DTE or event within 24 hours of the rejection communication, keeping the SAME codigoGeneración as the rejected original — unless the rejection motive is the codigoGeneración itself, in which case a corrected transmission with a new code is required. (LB-004 §10, raw-text verified; LB-009; MOQ-07 → OQ-001)
- **SV-EINV-FR-079:** The system, once the 24-hour correction window has expired without successful retransmission, shall transmit the corrected document as a NEW document with a new codigoGeneración (and related-document linkage to the abandoned one where applicable). (LB-009 §10; MOQ-07 → OQ-001)
- **SV-EINV-FR-080:** The SaaS shall push every state change (reception response, lote result, seal, rejection, sub-condition, overdue flag) to the client through the private protocol's state events and webhooks/callbacks, as a standing contract of the shared protocol core. (LB-011 D2/D6; LB-007)
- **SV-EINV-FR-081:** The system shall surface the seal's legal effects: only sealed DTEs enable CT 206 deductions; the seal does not validate or authorize the documented operation (CT 119-D inc. 3); rejected and unsealed documents are flagged as non-deductible, and rejected documents additionally carry the CT 199 presumed-income warning. (LB-001 Art. 119-D; LB-002 CT 199/206)
- **SV-EINV-FR-082:** The system shall record the evidential hierarchy for archived DTEs — AT copy > taxpayer copy > Representación Gráfica (CT 206) — as metadata on the mirrored archive, with deduction workflows consulting the sealed state (FR-081) rather than the RG. (LB-002 CT 206; LB-011 D3)
- **SV-EINV-FR-083:** The system shall keep books and records by GENERATION date (not seal date), including untransmitted and rejected documents, so declarations cover the generation period; contingency and unsealed DTEs are recordable without seal per CT 141 as reformed. (LB-009 §10.2; LB-003 CT 141)

### 3.10 Odoo client surface (queue & state display)

- **SV-EINV-FR-084:** The Odoo client shall render a per-environment transmission outbox with live state per document (queued, blocked-by-dependency, in-flight, transitory, processed [observado/ajustado], rejected with 24-hour countdown, not-emitted), so users see exactly what the SaaS queue holds without accessing MH consoles. (LB-011 D2; LB-009)
- **SV-EINV-FR-085:** The system shall prevent redundant retransmission: once a reception or rejection response has been obtained for a document, the connector shall deduplicate any repeat submission of the same codigoGeneración/idEnvio. (LB-004 §10; LB-007 §5.5)
- **SV-EINV-FR-086:** The Odoo client shall store and display every MH response field on the document (estado, clasificaMsg, codigoMsg, observaciones, selloRecibido, codigoLote/idEnvio) as read-only transmission metadata, for audit and support. (LB-007 §4; LB-011 D2/D3)

### 3.11 Fiscal immutability & correction accounting (post-S1 addendum, FR-159..164)

The transmission state machine (§3.9) governs the DTE lifecycle at MH; this section governs what those states mean for the Odoo `account.move` ledger surface — the safeguard layer that makes Odoo's native draft/cancel/delete affordances safe on fiscally sealed documents. Corrections ALWAYS post as new entries in the correction period; originals are immutable (D9 corollary, regulatory-change decision log).

- **SV-EINV-FR-159:** The client shall lock the account.move lifecycle by transmission state: a move never transmitted (no codigoGeneración issued) is unrestricted (native draft/edit/delete); from first transmission onward deletion shall be blocked; once sealed (PROCESADO), reset-to-draft, cancellation and any edit altering fiscal content (partner, lines, amounts, dates, document type) shall be blocked — only non-fiscal metadata may change; once INVALIDADO the move is locked forever. The 24-hour rejection correction flow (FR-078/079) is the only authorized edit path past first transmission. (LB-009 §10; FR-076; FR-096; D9 corollary)
- **SV-EINV-FR-160:** The system shall account a sealed DTE's invalidation as an auto-generated, NON-EDITABLE full-mirror reversal entry (unlike Odoo's native credit note, which opens an editable draft): the reversal mirrors every line of the invalidated DTE, is posted in the invalidation event's period, and is never user-modifiable; the original move stays posted, marked INVALIDADO, and is never cancelled, reset or deleted. Same-month invalidation nets both legs to zero within the month; cross-month invalidation keeps the original in its filed period M and posts the reversal in M+1 (credit-note treatment), so no filed period ever changes; where a replacement DTE exists (codigoGeneracionR, FR-101), it posts in its own generation period and the correction-period legs (reversal + replacement) net to the corrected operation. (LB-009 §10.2 generation-date books; FR-083; FR-096; `03_events.md` FR-096/101/103; D9 corollary)
- **SV-EINV-FR-161:** The system shall route window-expired adjustments of CCF and CR documents through NCE/NDE (Ley IVA Arts. 62–63 deadlines; `03_events.md` FR-101) instead of invalidation; the NCE/NDE move itself is the correction document and no internal reversal entry is generated for that path. (LB-008 via `01_document-types.md` FR-015; cross-ref FR-101)
- **SV-EINV-FR-162:** The system shall account a sealed retorno event as a credit entry posted in the retorno period implementing FR-118's fiscal effects (FE: decrease sale + IVA débito; FEXE: decrease export value + crédito-fiscal remanente; FSEE: decrease purchases), linked to the origin move; the origin stays posted (retorno never invalidates it, FR-119). Traceability invariants (requirement level): a correction entry whose goods physically moved back shall reference the origin delivery and the return reception; a price-only correction shall carry no stock movement linkage; a product exchange = retorno (returned item) + new FE (replacement item) as two independent fiscal documents. Selection rule: goods physically returned ⇒ retorno; invoice wrong / not delivered as invoiced ⇒ invalidación code 3 + replacement (FR-097). (Line-level move↔picking linkage mechanics → OQ-011.) (LB-005 §13.3; `03_events.md` FR-118/119; D9 corollary)
- **SV-EINV-FR-163:** On invalidation-with-replacement of a DIFFERENT document type (e.g. FE invalidated, CCF issued for the same operation), the replacement move shall link to the same sale order and the same delivery pickings as the invalidated original, and the invalidated move's picking links shall be marked superseded — never deleted — so the physical flow remains auditable across the correction chain (original → invalidation event → reversal → replacement). Where an NRE (Guía de Remisión) documented the transport, the working assumption is the NRE remains valid (the transport physically occurred; no invalidation precondition involves NREs) and the replacement should relate it — timing-rule conflict → OQ-009. (FR-015; `03_events.md` FR-102; D9 corollary)
- **SV-EINV-FR-164:** The client shall support commercial transactions in any Odoo-supported currency (Quetzales, Lempiras, Mexican Pesos, Euros, etc. — all bank-tradable in El Salvador) while the DTE layer remains USD-only (FR-007/093): the origin DTE's USD amounts are converted once at the origin document's date-rate, and every correction DTE and correction entry (NCE/NDE, invalidation reversal, retorno credit) shall derive its USD amounts from the ORIGIN document's rate — never re-converted at the correction-date rate — so the act of correction can never create currency gain or loss; ordinary Odoo multi-currency behavior (payment-realization FX differences) is unaffected. (LB-004 N°12 via FR-007; D9 corollary; declaration-side FX → OQ-010)

## 4. Data Model

The MH wire protocol exists only SaaS-side (D2); this section documents the
state vocabulary and fields both sides and the SaaS team must agree on.
Catalog sidecars live in [../catalogs/](../catalogs/) (CAT-001, CAT-004).

**Transmission state enum** (private-protocol contract value):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.document.state | state | select | transitorio · procesado · rechazado · invalidado · not_emitted | FR-076; 18_ §10 / 45_ §10 mapping |
| l10n_sv_edi.document.state | sub_condition | select | observado · ajustado (procesado only) | FR-076/077 |
| l10n_sv_edi.document.state | rejection_deadline | datetime | now + 24h at rejection communication | FR-078 |
| l10n_sv_edi.document.state | transmission_mode | select | normal_previa · normal_diferida · contingencia | FR-067–069; CAT-003/CAT-004 |

**MH endpoint & environment registry** (SaaS configuration, seeded):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| saas.mh_environment | code | char(2) | 00 pruebas · 01 producción | CAT-001; FR-054 |
| saas.mh_environment | base_url | char | apitest.dtes.mh.gob.sv / api.dtes.mh.gob.sv (OCR variant → OQ-006) | FR-055 |
| saas.mh_environment | services | json | /seguridad/auth · /fesv/recepciondte · /fesv/recepcionlote · /fesv/recepcion/consultadte · /fesv/recepcion/consultadtelote/{codigoLote} · /fesv/contingencia · /fesv/anulardte | FR-055–062 |
| saas.mh_environment | lot_window | json | test: 100 docs/400 lots 08:00–17:00 · prod: 100 docs/400 lots 22:00–05:00 · contingency 24/7 | FR-066 |
| saas.mh_environment | token_policy | json | validity=AT-configurable; refresh cycle ≤24h; auth errors 100–111 | FR-056 |

**Client-side transmission fields** (mirrored via protocol):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (DTE/event) | l10n_sv_edi_state / sub_condition | select | per state enum above | FR-076/084 |
| account.move (DTE/event) | l10n_sv_edi_sello | char(40) | selloRecibido: 40 alphanumerics, uppercase, no hyphens | FR-058; DG45 §4 |
| account.move (DTE/event) | l10n_sv_edi_codigo_msg / clasifica_msg | char | e.g. 002 received-with-observations | FR-077/086 |
| account.move (DTE/event) | l10n_sv_edi_observaciones | text list | observaciones[] verbatim | FR-077/086 |
| account.move (DTE/event) | l10n_sv_edi_id_envio / codigo_lote | char(36) | UUID v4 — 36 chars, uppercase hexadecimal digits [0-9A-F], 8-4-4-4-12 hyphen groups (52_ schema) / codigoLote | FR-058/059 |
| saas.transmission_queue | depends_on | many2one queue item | dependency edge; item held until dependency sealed | FR-074/075 |
| saas.transmission_queue | retry_count / next_attempt_at | integer / datetime | ≤2 resends after 8s timeout | FR-064 |

**Correction-accounting fields** (post-S1 addendum):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (correction entry) | l10n_sv_edi_correction_of | many2one account.move | origin DTE move (invalidation reversal · retorno credit · reissue replacement) | FR-160/162/163 |
| account.move (correction entry) | l10n_sv_edi_correction_kind | select | invalidation_reversal · retorno_credit · reissue_replacement · nc_nd | FR-160/161/162/163 |
| account.move (correction entry) | l10n_sv_edi_origin_rate | float | origin DTE's USD conversion rate, reused by all its corrections | FR-164 |
| account.move (goods-return correction) | l10n_sv_edi_return_picking_id | many2one stock.picking, null | set only when goods physically returned; null = price-only correction | FR-162 (line-level linkage → OQ-011) |
| account.move (invalidated origin) | l10n_sv_edi_picking_superseded_by | many2one account.move | replacement move inheriting the delivery links; links marked, never deleted | FR-163 |

## 5. Odoo Mapping

Layer semantics per the architecture doc: `saas` = MH-facing transmission
logic in the Elixir core (the client never builds MH requests); `odoo` =
queue/state display and configuration surface in the LGPL client; `shared`
= private-protocol contract items both sides must honor (state vocabulary,
push semantics). Model names are stable across Odoo 17/18/19/20; nothing
in this file requires version-specific behavior.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-053 | saas | — | — | Architecture constraint (D2); enforced by code review + AC-011 static check |
| FR-054 | shared | res.company | l10n_sv_edi_environment | Environment chosen once per company; client blocks host/env mismatch; credentials never leave SaaS |
| FR-055 | saas | — | — | Auth entirely SaaS-side; client never sees the JWT |
| FR-056 | saas | — | — | Token store + refresh scheduler in Elixir core; error taxonomy surfaced via protocol |
| FR-057 | saas | res.company | credential refs only | Client stores opaque references; secrets encrypted SaaS-side; custody note in ToS (LB-004 §9.2) |
| FR-058 | saas | — | — | Uno-a-uno service; response mapped to protocol state event (FR-080) |
| FR-059 | saas | — | — | Lote assembly server-side; client submits document batches, not MH lots |
| FR-060 | saas | — | — | Polling scheduler; final per-DTE results pushed (FR-080) |
| FR-061 | saas | — | — | Also feeds daily reconciliation job |
| FR-062 | saas | — | — | Retorno/OpEsp paths pending (OQ-003); same-connector integration when published |
| FR-063 | saas | — | — | Rule 3.5 service-status check before waves; endpoint contract pending (OQ-005) |
| FR-064 | saas | — | — | Retry state machine in queue; escalation flags contingency mode (03_events.md owns clocks) |
| FR-065 | saas | — | — | Response-loss dedup; same consultadte path as FR-061 |
| FR-066 | saas | — | — | Window scheduler per environment registry; cyclic-invoicing emitters only |
| FR-067 | saas | account.move | l10n_sv_edi_transmission_mode | Default mode; entrega flow gated on seal (`04_signing_delivery.md`) |
| FR-068 | saas | res.company | l10n_sv_edi_diferida_resolution | AT-resolution flag stored per emitter; lote-only; 8-type gate |
| FR-069 | saas | account.move | l10n_sv_edi_transmission_mode | Contingency mode; 72h doc clock from event seal; alarm to client on deadline approach |
| FR-070 | shared | account.move | l10n_sv_edi_state, overdue alarm | Transitory semantics contract; overdue computation SaaS-side, banner client-side |
| FR-071 | saas | — | — | fecEmi window validated at generation AND transmission; rejections surfaced with the worked example rule |
| FR-072 | saas | — | — | Month-end holgura; clock-skew tolerance |
| FR-073 | saas | — | — | Defensive: do-not-rely note; revisit on OQ-002 resolution |
| FR-074 | saas | — | — | Dependency edges in SaaS queue (single sequencer per D2) |
| FR-075 | shared | l10n_sv_edi.outbox.item | blocked_by | Blocked-state vocabulary part of protocol contract; client renders it |
| FR-076 | shared | l10n_sv_edi.document.state | state, sub_condition | State enum = protocol contract; authoritative transition SaaS-side, client mirrors |
| FR-077 | odoo | account.move | l10n_sv_edi_observaciones | Display-only; non-blocking semantics agreed in contract (FR-076) |
| FR-078 | saas | — | — | 24h window enforced at retransmission; code-motive exception auto-detected from codigoMsg |
| FR-079 | saas | account.move | ref linkage to abandoned doc | New-code path; related-doc linkage rules from 01_document-types.md FR-014/015 |
| FR-080 | shared | l10n_sv_edi.state.event | — | Protocol push + webhook contract (D6 core); client applies idempotently |
| FR-081 | saas | account.move | deductibility flag | Legal-effect flags surfaced; tax behavior owned by taxation file (A10) |
| FR-082 | odoo | account.move (archive) | hierarchy metadata | Tier A mirror metadata (D3); read path exempt from entitlement (D4) |
| FR-083 | odoo | account.move | invoice_date basis | Books post by fecGeneracion; untransmitted/rejected included; CT 141 backlog window |
| FR-084 | odoo | l10n_sv_edi.outbox | state, countdown | Pure client surface over pushed states; per environment |
| FR-085 | saas | — | — | Dedup at connector; client cannot force duplicate transmission |
| FR-086 | odoo | account.move | response metadata fields | Read-only mirror fields (see Data Model); audit surface |
| FR-159 | odoo | account.move | lock overrides (button_draft/button_cancel/unlink) | Lock keyed on l10n_sv_edi_state; rejection-correction path (FR-078/079) is the sole edit gate |
| FR-160 | odoo | account.move (reversal) | l10n_sv_edi_correction_of/kind, locked lines | Generated full mirror, never a user-draft credit note; posting date = event period; identical across 17–20 |
| FR-161 | shared | account.move (NC/ND) | l10n_sv_edi_correction_kind = nc_nd | Routing decision (window expired ⇒ NCE/NDE) SaaS-validated, client surfaces it |
| FR-162 | odoo | account.move (retorno credit) | l10n_sv_edi_correction_of/kind, l10n_sv_edi_return_picking_id | Credit entry from sealed retorno event; goods vs price-only linkage invariant (line-level design → OQ-011) |
| FR-163 | odoo | account.move + stock.picking | l10n_sv_edi_picking_superseded_by | Reissue inherits sale order + pickings; supersede marks, never unlink |
| FR-164 | odoo | account.move | l10n_sv_edi_origin_rate, currency_id | Origin-rate reuse on corrections; native Odoo multi-currency untouched otherwise |

## 6. Acceptance Criteria

- **AC-001:** Given a uno-a-uno send with no response after 8 seconds, when the retry policy runs, then consultadte is called before any resend, resends occur at most 2 times, and on the last failure the document is flagged for contingency escalation (FR-064).
- **AC-002:** Given a response that the emitter side failed to process, when recovery runs, then the connector queries status first and does not resend a document already received (FR-065, FR-085).
- **AC-003:** Given a cyclic-invoicing emitter (the scope FR-066's schedule restriction applies to), when it submits a lote containing 101 documents, then the SaaS splits it before submission; given such an emitter's lot built at 17:30 in the test environment, then dispatch waits until the next 08:00–17:00 window (FR-066).
- **AC-004:** Given a DTE rejected at time T, when the corrected document is retransmitted at T+23h with the same codigoGeneración, then it is accepted for processing; given retransmission attempted at T+25h with the same code, then it is blocked and the new-code path (FR-079) is required (FR-078/079).
- **AC-005:** Given a rejection whose motive is the codigoGeneración itself, when correcting within 24h, then retransmission proceeds with a NEW codigoGeneración (FR-078).
- **AC-006:** Given an NCE queued while its related CCFE has no seal, when the queue is evaluated, then the NCE is held (blocked-by-dependency); when the CCFE seal arrives, then the NCE is released for transmission (FR-074/075).
- **AC-007:** Given a DTE received with estado PROCESADO and observaciones (codigoMsg 002), then the document shows state procesado/observado, the observations are stored and displayed, and no downstream flow is blocked (FR-076/077).
- **AC-008:** Given a DTE transmitted 27-June with fecEmi 30-June, then it passes the window check; given the same transmission with fecEmi 01-July, then it is rejected as crossing the tax period (FR-071).
- **AC-009:** Given an emission on the last day of a month whose emitter clock reads horEmi 25 minutes past the transitory deadline, then horEmi is accepted — the referent is the emitter's recorded `horEmi` vs the MH system clock, which is the skew FR-072's 30-minute holgura bridges; at 35 minutes past on the emitter's clock, then rejected (FR-072).
- **AC-010:** Given a cached token nearing expiry before a submission wave, then the connector refreshes it; given an auth error in the 100–111 range, then it is surfaced as an authentication failure, not a document rejection (FR-056).
- **AC-011:** Given the Odoo client codebase, when statically scanned, then no reference to `*.dtes.mh.gob.sv` API endpoints exists in client code paths outside SaaS configuration test fixtures — MH portal URLs (human documentation/validation pages, not API surfaces) are out of scope (FR-053).
- **AC-012:** Given a company configured with environment 00, when a user attempts to set the production base URL (or vice versa), then the configuration is rejected (FR-054).
- **AC-013:** Given a consultadtelote response with mixed per-DTE results (2 PROCESADO, 1 RECHAZADO), then each document's state, seal (40-char) and observaciones are applied individually (FR-060, FR-076).
- **AC-014:** Given a transitory document whose modality deadline passes without transmission, then its state becomes not_emitted, the CT 199 presumed-income warning is displayed, and an overdue alarm fires (FR-070, FR-081).
- **AC-015:** Given any document with reception or rejection response already recorded, when a duplicate submission of the same codigoGeneración/idEnvio arrives, then the connector suppresses it (FR-085).
- **AC-016:** Given a sealed FE, when a user clicks Reset to Draft (or Cancel, or Delete), then the action is blocked with an explanatory message; given the same move before any transmission, then all three actions work natively (FR-159).
- **AC-017:** Given an FE sealed in month M and invalidated by an event sealed in month M+1, when the invalidation is sealed, then a non-editable full-mirror reversal entry posts dated in M+1, the original stays posted in M marked invalidado, and no M-period figure changes; given the invalidation lands within month M, then both legs post in M and net to zero (FR-160).
- **AC-018:** Given a correction attempt on a CCF whose 3-month invalidation window has expired, then the system routes to NCE generation (no invalidation event, no internal reversal) (FR-161).
- **AC-019:** Given a sealed retorno event for one returned item of a 3-item FE, then a credit entry posts for that item's values referencing the origin move and the return picking, the origin stays posted, and no delivery link is created for a price-only NCE (FR-162).
- **AC-020:** Given an FE invalidated and replaced by a CCF for the same delivered goods, then the CCF move links to the same sale order and delivery pickings, and the FE's picking links are marked superseded (queryable, not deleted) (FR-163).
- **AC-021:** Given a EUR-denominated sale whose origin DTE converted at rate R on its document date, when a retorno credit is posted 2 months later, then its USD amounts derive from rate R — not the retorno-date rate — and the correction legs produce zero FX gain/loss (FR-164).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | MOQ-07 (residual): 45_ §10 raw text now confirms the 24-hour correction window, same-codigoGeneración retransmission and the code-motive exception, but the after-window behavior (FR-079: new codigoGeneración) still rests on 18_ v1.2 §10 — re-read 45_ §10/§10.2 fully at implementation to confirm no v2.0 delta. | no | Takumi synthesis wave 1 | open |
| OQ-002 | R16: 22_-era reception holgura (documents accepted up to 1 day after fecEmi; period-end +30 min only) is not restated in 46_ v2.0 — confirm with 46_ revision or AT whether the reception grace still exists alongside the Normativa v2.0 modalities (FR-073 written defensively). | no | Takumi + SaaS team | open |
| OQ-003 | MOQ-05: Retorno / Operaciones Especiales event endpoint paths absent from 46_ v2.0 (25-May) and from the Anexos — check 52_ schemas and later manual revisions for service paths. | no | Takumi (schema pass) | open — schema pass 2026-08-17: all 15 files in the 52_ zip scanned; **zero endpoint/service-path strings** (only json-schema.org `$schema` refs). Absence now schema-verified; remains externally blocked on AT publication |
| OQ-004 | Test-environment lot cap: 22_ says 300 lots, 46_ v2.0 says 400 (both 08:00–17:00) — 46_ governs (FR-066); confirm the live figure during integration testing. | no | SaaS team | open |
| OQ-005 | Service-status consultation endpoint (Anexo I rule 3.5, new in v2.0): URL and contract not published in 46_ — obtain from AT manuals before wave scheduling (FR-063) ships. | no | SaaS team | open |
| OQ-006 | Production base URL OCR variants in 46_: "apidtes.mh.gob.sv" vs "api.dtes.mh.gob.sv" (22_ form) — confirm exact hostname at integration. | no | Takumi (schema pass) | open |
| OQ-007 | MOQ-11: CDE async seal "24–72h after transmission" (2022 manual) — still true under v2.0? Affects CDE state-machine timing (seal may lag reception) and entrega flow (`04_signing_delivery.md`). | no | SaaS team | open |
| OQ-008 | How do invalidated DTEs and retorno events present in the F-07/F-14 declaration annexes (anulados/invalidados columns, period attribution of the reversal)? Books keep both legs per FR-160/162; the declaration PRESENTATION rules are S2 fiscal-reporting scope (34_/35_ manuals likely carry the annex field definitions). | no | S2 fiscal-reporting wave | open |
| OQ-009 | NRE (Guía de Remisión) fate when its related FE/CCF is invalidated: no invalidation precondition involves NREs (FR-102 blocks only on NCE/NDE and retorno events); working assumption = NRE survives (transport physically occurred) and the replacement DTE should relate it — but FR-015's same-period/3-day window may block re-relation when the replacement issues later. Research: 41_/45_ invalidation manual silent; needs AT guidance or a 45_ revision. | no | Takumi + SaaS team | open |
| OQ-010 | Declaration-side FX: whether F-07/F-14 annexes state any conversion rule for non-USD operations (expected silent — DTE layer is USD-only per FR-007); S2 annex scan confirms or closes. | no | S2 fiscal-reporting wave | open |
| OQ-011 | Line-level account.move ↔ stock.picking linkage design: Odoo links them only indirectly via sale.order (header level); the real audit relationship is line-level (move lines ↔ picking move lines). A prior implementation by the product owner holds working mechanics — import as design input in a dedicated pass before FR-162/163 implementation. | no | Takumi + product owner | open |
