# SV — E-Invoicing — Signing, certificates, delivery & archive

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave 1 |
| Updated | 2026-08-17 |

## 1. Purpose

This file defines the functional requirements for cluster A6 (signing &
certificates) and cluster A7 (Representación Gráfica, QR, delivery and
archive): the JWS RS512 signing standard and the AT-issued
simple-signature certificate model, the client-side signer and encrypted
certificate vault (architecture decision D2 — the SaaS never holds
private keys), the signing round-trip over the private minimal protocol,
per-environment acreditamiento and the credential password policy, the
*Representación Gráfica* (RG, graphic representation) with its binding
A/B/C/D *Versión Legible* (readable version) categories and mandatory QR,
electronic delivery of the *entrega* (delivery package = Archivo DTE +
RG) under both transmission modalities and both channels, the composition
of the *Archivo DTE* (DTE file), and archive/conservation under decision
D3 (mandatory Tier A client mirror + paid Tier B SaaS hosting). It merges
the originally planned signing cluster (A6) and delivery cluster (A7) into
this single file.

It does **not** cover: document structures (`01_document-types.md`), the
MH connector, transmission modalities' clocks and the state machine
(`02_transmission.md` — this file cross-references its FRs), event
semantics and deadlines (`03_events.md`), catalog governance (A9,
`../catalogs/`), tax computation (A10), onboarding/authorization beyond
certificate acquisition (A11), or the private protocol's own contract
detail and versioning (`06_api-protocol.md`, A12). Where event signing
executes, `03_events.md` FR-090 (as amended, S1) and this file agree:
the SaaS orchestrates — it generates and validates, the CLIENT signs
(per D2 and FR-131/134 here), the SaaS transmits; see OQ-008 (resolved).

## 2. Legal Basis

Authority order (binding, per master evidence index): 44_/45_/46_/50_/51_/52_
(2026) > 18_/19_ (2025) > 40_/41_/25_ (2022). Where a conflict was
arbitrated, the resolution id (R1–R16) from the master index is noted.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D.L. 487-2022 (reforma al Código Tributario, régimen DTE), Arts. 119-B y 119-C | Art. 119-B: a DTE exists once generated, signed, transmitted and sealed; Art. 119-C: emission = generation → signature → transmission → delivery, electronically; receivers are OBLIGED to demand sealed DTEs (except *fedatarios*) | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Arts. 119-B/119-C (EVID-083) |
| LB-002 | D.L. 487-2022, Art. 3 (CT 147 reformado) | CT 147 as reformed: DTE conservation for 10 years (term per CT 147 itself, carried by LB-010 / 18_ §12) counted from GENERATION date, emitter's responsibility; AT is explicitly not the emitter's storage service; RGs conserved in their original format/medium | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 3 (EVID-083) |
| LB-003 | Normativa de Cumplimiento DTE v2.0, Anexo I, Cuadro 10 (firma electrónica) | Annex I Table 10: *firma electrónica simple* (simple electronic signature) with AT-issued certificates; JSON Web Signature (JWS) standard; PKCS8-encoded key material; asymmetric private/public keys; `firmaElectronica` = JWS over the full DTE/event JSON; AT validates the certificate on every document and event | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I Cuadro 10 pp. 40–41 (via DG45 §4; OCR items resolved — OQ-002) |
| LB-004 | Normativa v2.0, Anexo I, Cuadro 11 (Archivo DTE y entrega) | Annex I Table 11: Archivo DTE parts (JSON structure + `firmaElectronica` + `selloRecibido`); base objects list; the signed structure must be incorporated *íntegra* (unaltered — alteration is *lesiva al interés fiscal*, harmful to the fiscal interest); entrega = faithful RG via download site (minimum requirements) or email (entrega content only) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I Cuadro 11 pp. 43–44 (via DG45 §4; site requirements → OQ-004) |
| LB-005 | Normativa v2.0, Anexo I, módulos y seguridad | Annex I: the four emission modules — 1 Generación, 2 Firmado, 3 Transmisión, 4 Entrega (Módulo de Entrega newly incorporated); suggested reference architecture (high availability, DRP, load balancing, auto-scaling, backups, traceability, monitoring); backups of the JSON + sello (Sistema de Transmisión) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I pp. 44–45 (via DG45 §4) |
| LB-006 | Manual Tecnológico para la Integración v2.0 (46_) | Technology Integration Manual v2.0: credential password policy — 13 to 25 characters combining letters, numbers and special characters | `sv/sources/46_Manual_Tecnologico_Integracion_v2.0_2026-05-25.pdf` | §credential management (EVID-085) |
| LB-007 | Manual Tecnológico (22_), §§2–5 | Prior technology manual: MH reference *firmador* (signer) — Java Spring Boot source, Docker (SSL/non-SSL) or Windows service, local only; sign endpoint `http://localhost:8113/firmardocumento/` POST {nit, activo, passwordPri, dteJson} → JWS RS512 body; QR consultaPublica URL | `sv/sources/22_Manual_Tecnologico_Transmision.pdf` | §§2–5 pp. 5–32 (EVID-079) |
| LB-008 | Manual de Obtención de Certificado (27_) | Certificate Obtention Manual: *acreditamiento* required once per environment (test AND production — credentials personalized per environment); test credentials valid 2 months (Sistema de Transmisión) or 15 days (Sistema de Facturación) to complete the minimum tests; portal https://info.dtes.mh.gob.sv/ (NIT + DGII services password) → Sitio Emisores DTE: info verification → certificate generation → API user management | `sv/sources/27_Manual_Obtencion_Certificado.pdf` | pp. 5–10 (EVID-080) |
| LB-009 | Normativa de Cumplimiento DTE v1.2 (18_), §11 | DTE Regulation v1.2 §11: entrega = Archivo DTE + interpreted readable version (RG), electronic, both modalities; contingency documents without seal must show CAT-004 code 2; RG has no probative value, is generated simultaneously with the DTE, is delivered per operation, and carries a mandatory QR; receiver obliged to demand the sealed DTE; fedatarios not obliged | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §11–11.3 pp. 16–17 (EVID-073; carried into v2.0 entrega framework) |
| LB-010 | Normativa v1.2 (18_), §12 | Regulation v1.2 §12: electronic conservation per CT 147 (10 years), exact structure and format preserved, including untransmitted documents | `sv/sources/18_Normativa_Cumplimiento_DTE.pdf` | §12–12.1 p. 18 (EVID-074) |
| LB-011 | Manual de Estructuras y Catálogos (2022), categorías Versión Legible | Structures Manual: Versión Legible column categories — A must be reflected; B reflected when required by business/activity/operation/amount or other conditions; C never displayed; D when unused, the section/field name is printed followed by a dash; layouts are suggested, categories binding; sello NOT part of the emitter's outbound JSON (response-only) but must appear in the Versión Legible except contingency documents | `sv/sources/40_manual_estructuras_catalogo.md` | Versión Legible category tables (EVID-020; concept carried into v2.0 Anexo column structure per DG45 §4) |
| LB-012 | Catálogos de Facturación Electrónica v1.1 (jul-2026) | e-Invoicing Catalogs v1.1: CAT-001 ambiente (00 pruebas / 01 producción); CAT-004 tipo de transmisión (1 normal / 2 contingencia) | `sv/sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx` | CAT-001, CAT-004 sidecars (EVID-086) |
| LB-013 | Product architecture decisions D2/D3/D4 | D2: signing client-side (encrypted cert vault in Odoo, Python JWS/RS512, SaaS never touches private keys; private minimal protocol; dual validation); D3: archive tiering (Tier A mandatory local mirror at response time, Tier B paid SaaS hosting with exit export); D4: entitlement hard wall with read-path exemption for the mirrored archive | `shared/docs/saas-thin-client-architecture.md` | §S0.5 D2, D3, D4 |

## 3. Functional Requirements

### 3.1 Emission chain & the signing round-trip (D2)

- **SV-EINV-FR-130:** The system shall enforce the CT 119-B/119-C emission chain — generation → signature → transmission → delivery — such that no DTE or event is transmitted to the MH without a valid `firmaElectronica`, and no entrega is made without either the *sello de recepción* (reception seal, normal modality) or the transitory/contingency marking of FR-145. (LB-001; cross-ref `02_transmission.md` FR-067–070)
- **SV-EINV-FR-131:** The system shall implement the JWS signer CLIENT-SIDE in the Odoo module (Python, RS512): the emitter's certificate and private key live only in the client's encrypted vault, and the SaaS shall never hold, receive, generate, proxy or back up private key material; no private key or key password shall ever cross the private protocol. The implementation follows the MH reference *firmador* pattern (local-only signer; MH distributes Java/Docker/Windows references) but is an independent Python re-implementation with no runtime dependency on the MH firmador. (LB-013 D2; LB-007; LB-003)
- **SV-EINV-FR-132:** The system shall implement the signing round-trip over the private minimal protocol: (a) the SaaS generates/validates the document payload and returns a signing request (exact bytes to be signed, artifact type DTE/event, ambiente, algorithm RS512); (b) the Odoo client checks the request's ambiente against the vault's per-environment certificate, signs locally, and returns the JWS compact serialization; (c) the SaaS verifies the signature against the emitter's public certificate before transmission, assembles the signed artifact, and transmits it; (d) every round-trip state (pending-sign, signed, verify-failed) is surfaced to the client. The exact wire envelope (full MH JSON vs. an opaque canonical payload — see OQ-001) is owned by `06_api-protocol.md`. (LB-013 D2; LB-003)
- **SV-EINV-FR-133:** The signer shall produce `firmaElectronica` as a JWS compact serialization (algorithm RS512) computed over the full DTE or event JSON, using the emitter's AT-issued simple-signature certificate and asymmetric keys with the private key held PKCS8-encoded and password-protected in the vault. (LB-003; LB-007; OQ-002 resolved — RS512 confirmed by the normativas' example header, CAdES/PKCS8EncodedKeySpec by the 18_ twin row)
- **SV-EINV-FR-134:** All four event types (invalidación, contingencia, retorno, operaciones especiales) shall ride the SAME client-side signing round-trip as DTEs — events are signed with the emitter's certificate before transmission, and the AT validates the certificate on every document and event. (LB-003; LB-013 D2; cross-ref `03_events.md` FR-090 — amended S1 to orchestration wording consistent with this FR; OQ-008 resolved)
- **SV-EINV-FR-135:** The system shall classify certificate-related MH rejections (expired, revoked or mismatched certificate) as a distinct error family — separate from data/validation errors — shall block further signing attempts with the offending certificate, and shall raise proactive expiry alarms from the vault (FR-138). (LB-003; LB-008)

### 3.2 Certificate vault & credential lifecycle

- **SV-EINV-FR-136:** The Odoo client shall keep an encrypted certificate vault with one ACTIVE MH-issued signing certificate per environment at any time — ambiente 00 *pruebas* (test) and 01 *producción* (production), each personalized and obtained through that environment's acreditamiento; renewal may stage a successor certificate while the current one remains valid, with activation swapping atomically and the vault refusing concurrent ACTIVE certificates per environment — and shall bind every signing operation to the certificate whose ambiente matches the payload's ambiente, refusing cross-environment signing (a test certificate shall never sign a production payload or vice versa). (LB-008; LB-012 CAT-001; LB-013 D2)
- **SV-EINV-FR-137:** The vault shall enforce the MH password policy on every vault credential and private-key password: 13 to 25 characters combining letters, numbers and special characters; weaker passwords shall be rejected at entry. (The SaaS-side MH API-user credentials follow the same policy — owned by `02_transmission.md` FR-057.) (LB-006; LB-007)
- **SV-EINV-FR-138:** The client shall support the certificate lifecycle: acquisition through the acreditamiento flow per environment (portal https://info.dtes.mh.gob.sv/ → RUC data verification → certificate generation → API user management), with the test environment's 2-month credential window (Sistema de Transmisión) tracked as a deadline against completing the minimum tests; plus validity monitoring (valid-from/valid-to), renewal, and revocation handling, with expiry alarms raised ahead of expiry so emission never halts unexpectedly. (LB-008; onboarding test regime owned by the A11 onboarding file)
- **SV-EINV-FR-139:** The vault shall be an access-controlled security surface: key material encrypted at rest, never logged, never included in protocol responses, webhooks, diagnostics, support bundles or ordinary database backups in readable form; vault access shall be permissioned and audited. (LB-013 D2; LB-005)

### 3.3 Representación Gráfica (RG)

- **SV-EINV-FR-140:** The system shall deliver every DTE electronically as the *entrega* package: the Archivo DTE (FR-152) PLUS its *Representación Gráfica* (RG, graphic representation / *versión interpretada legible* — interpreted readable version); neither component alone is a valid entrega. (LB-009 §11; LB-001)
- **SV-EINV-FR-141:** The RG shall be generated simultaneously with the DTE (same generation event, same codigoGeneración), not retroactively, so delivery per operation is always possible at entrega time. (LB-009 §11)
- **SV-EINV-FR-142:** The system shall treat the RG as having NO probative value, and shall record the CT 206 evidential hierarchy (AT copy > taxpayer copy > RG) on the archived document — deduction and audit workflows shall never rely on the RG. (LB-009 §11; cross-ref `02_transmission.md` FR-082)
- **SV-EINV-FR-143:** The system shall render every RG according to the binding Versión Legible field categories: A = must be reflected; B = reflected whenever required by business, activity, operation, amount or other conditions; C = never displayed; D = when unused, the section/field name is printed followed by a dash. Suggested layouts in the structures manual are NOT binding; the category assignment per field is. A machine-readable per-type category sidecar (Anexo II Versión Legible column) shall drive rendering (→ OQ-007). (LB-011)
- **SV-EINV-FR-144:** The RG shall display the *sello de recepción* for sealed documents; the sello is NOT part of the emitter's outbound signed JSON (it exists only in the MH response) and is incorporated into the Archivo DTE and RG after reception — except contingency/unsealed documents, which carry the FR-145 marking instead. (LB-011; LB-004; LB-003 selloRecibido N°175)
- **SV-EINV-FR-145:** Documents delivered under a deferred modality without seal (normal diferida or contingency — `02_transmission.md` FR-068/069) shall be delivered in *estado transitorio*; the explicit RG marking as contingency transmission, CAT-004 code 2 (tipo de transmisión *contingencia*), applies ONLY to contingency-modality documents — normal diferida is a NORMAL transmission modality held under AT resolution (EVID-073 ties the code-2 marking to contingency documents; cross-ref `02_transmission.md` FR-068; whether 45_ §11.2 mandates any additional marking for normal-diferida entregas → OQ-009). The transitory marking shall disappear from the record's current view once the document is sealed, while the delivered transitory copies remain as delivered. (LB-009 §11; LB-012 CAT-004)
- **SV-EINV-FR-146:** RG rendering shall be implemented SaaS-side (shared decision point, recorded here): a single rendering service keeps per-type templates, category assignments and version churn centralized as core IP, guaranteeing uniform compliance across clients; the Odoo client shall display, print and re-download RGs from its Tier A mirror and shall be able to re-render on demand through the SaaS. Offline read access to the mirrored RG is a Tier A right (FR-157). (LB-013 D2/D3; LB-011)

### 3.4 QR code

- **SV-EINV-FR-147:** Every RG shall carry a QR code encoding the public consultation URL `https://admin.factura.gob.sv/consultaPublica?ambiente={ambiente}&codGen={codigoGeneracion}&fechaEmi={fecEmi}` with the document's ambiente (CAT-001), codigoGeneración and emission date; the QR is mandatory on the entrega's RG. (The Anexos state QR only as an entrega requirement and defer specifics to the manuals — parameter date format → OQ-003.) (LB-009 §11; LB-007; DG45 §4)

### 3.5 Electronic delivery — modalities & channels

- **SV-EINV-FR-148:** The system shall deliver electronically under BOTH modalities: (a) normal prior transmission — entrega carries the sello de recepción (`02_transmission.md` FR-067); and (b) transitory delivery for the deferred modalities — entrega in estado transitorio, with the CAT-004 code 2 contingency marking of FR-145 scoped to contingency-modality documents only (normal diferida carries the transitory state without it — → OQ-009), with the modality clocks owned by `02_transmission.md` FR-068–070. (LB-009 §11; LB-001)
- **SV-EINV-FR-149:** The system shall support the two entrega channels per Cuadro 11: (a) a download site — hosted by the SaaS on behalf of the emitter, satisfying the AT minimum requirements (→ OQ-004) — where the receiver obtains the Archivo DTE + RG; and (b) email, carrying the entrega content (scope → OQ-005), triggered from the Odoo client's document flow. Both channels shall deliver the same package defined by FR-140. (LB-004; LB-005 Módulo de Entrega)
- **SV-EINV-FR-150:** The system shall support the RECEIVER-side obligation on the emitter's own purchase flows: documents received by the client company shall display seal presence, and unsealed/non-compliant DTEs shall carry a warning that accepting them forfeits CT 206 deductions (receivers are obliged to demand sealed DTEs; *fedatarios* are the exception and verify RG delivery instead). (LB-001 119-C inc. 6; LB-009)
- **SV-EINV-FR-151:** The system shall map onto the four AT emission modules — 1 Generación, 2 Firmado, 3 Transmisión, 4 Entrega — as: Generación/Transmisión/Entrega orchestrated by the SaaS, Firmado executed client-side (FR-131); the AT's suggested reference architecture (high availability, DRP, load balancing, security, auto-scaling, backup, traceability, monitoring, reporting) is recorded as design guidance for the SaaS deployment posture (D1 multi-region). (LB-005; LB-013 D1/D2)

### 3.6 Archivo DTE composition

- **SV-EINV-FR-152:** The system shall define the delivered/conserved artifact as the *Archivo DTE*: the plain JSON document structure (base objects `identificacion`, `emisor`, `receptor`, `otrosDocumentos`, `documentoRelacionado`, `ventaTercero`, `compraTercero`, `cuerpoDocumento`, `resumen`, `apendice`) plus `firmaElectronica` and `selloRecibido` (the latter absent for contingency/unsealed operations); the archived artifact shall be integrity-checked (hash on mirror, verified on read) — alteration of the signed structure is *lesiva al interés fiscal* and shall be flagged as a violation. (LB-004; LB-003)
- **SV-EINV-FR-153:** The SaaS shall incorporate the signed structure *íntegra* into the Archivo DTE — byte-stable assembly with no re-serialization drift between what was signed, what was transmitted and what is archived/delivered — so that the archived JSON is exactly the signed JSON plus the reception response fields. (LB-004; LB-013 D2)

### 3.7 Archive tiers & conservation (D3)

- **SV-EINV-FR-154:** The Odoo client shall mirror, at response time, every sealed Archivo DTE + rendered RG (and every sealed event file per `03_events.md` FR-090) into the Tier A local archive — the mirror is MANDATORY client-side behavior, not a tier option — so the CT 147 conservation duty is satisfied locally with zero dependence on the SaaS. (LB-013 D3; LB-002)
- **SV-EINV-FR-155:** The system shall conserve DTEs for 10 years counted from the GENERATION date (not the seal date), including untransmitted and rejected documents, preserving the exact structure and format (RG in its original format/medium); the client shall compute and enforce retention dates per document and shall refuse premature purges. (LB-002; LB-010)
- **SV-EINV-FR-156:** The system shall implement archive custody as tiers: Tier A (base, mandatory mirror — FR-154) and Tier B (paid SaaS hosting: long-term conservation, search, re-download, platform RG re-rendering, with a structured exit export while the account is in good standing); tier-down (B→A or cancellation) shall always leave the emitter compliant via the local mirror, and the product shall state plainly that SaaS hosting is a convenience on top of the emitter's own non-delegable duty — the AT is not the emitter's archive either. (LB-013 D3; LB-002)
- **SV-EINV-FR-157:** Read paths over the Tier A mirror (browse, search, print, export of the emitter's own archived DTEs/RGs) shall remain fully available regardless of subscription state — per D4, the entitlement hard wall blocks generation/signing/transmission but never the local archive. (LB-013 D3/D4)
- **SV-EINV-FR-158:** The system shall support backups of the conserved JSON + sello per the AT security guidance: client-side backup of the Tier A mirror (encrypted, restorable, retention-aligned), and SaaS-side backup as part of Tier B hosting. (LB-005; LB-002)

## 4. Data Model

GENERATION-TIME (pre-seal) scope: the client never generates or transforms
MH-format JSON — MH-shape data reaches the client only inside the signing
envelope (D2: private minimal protocol; the SaaS compiles and assembles).
Post-seal, the Archivo DTE (verbatim sealed MH JSON) and the JWS ARE
first-class client-side data as Tier A mirrored archive artifacts
(FR-152/154). This section documents the vault, the signing envelope,
entrega metadata and the Tier A mirror.

**Certificate vault** (odoo-side security surface):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.certificate | environment | selection | 00 pruebas / 01 producción (CAT-001) | FR-136 |
| l10n_sv_edi.certificate | nit | char(14) | emitter NIT bound to the cert | FR-136; LB-007 |
| l10n_sv_edi.certificate | public_cert | binary | AT-issued simple-signature certificate | FR-133 |
| l10n_sv_edi.certificate | private_key | binary (encrypted) | PKCS8-encoded, password-protected | FR-133, FR-139 |
| l10n_sv_edi.certificate | key_password | char (encrypted) | 13–25 chars, letters+numbers+special | FR-137 |
| l10n_sv_edi.certificate | valid_from / valid_to | date | MH-issued validity window | FR-138 |
| l10n_sv_edi.certificate | state | selection | draft / valid / expiring / expired / revoked | FR-135, FR-138 |
| l10n_sv_edi.certificate | accreditation_deadline | date | test env: 2-month window (Sistema de Transmisión) | FR-138 |

**Signing round-trip envelope** (shared protocol artifact; wire detail owned by `06_api-protocol.md`):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.sign_request | artifact | selection | dte / evento (invalidación, contingencia, retorno, eop) | FR-132, FR-134 |
| protocol.sign_request | ambiente | selection | 00 / 01 — must match the vault cert | FR-136 |
| protocol.sign_request | payload | bytes | exact bytes to sign (shape → OQ-001) | FR-132, FR-133 |
| protocol.sign_request | algorithm | const | RS512 (JWS) | FR-133 |
| protocol.sign_response | jws | char | JWS compact serialization (firmaElectronica) | FR-133 |
| protocol.sign_response | state | selection | signed / verify-failed / refused-env-mismatch | FR-132, FR-135 |

**Entrega / RG metadata**:

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (DTE) / l10n_sv_edi.event | rg_document | binary | rendered RG, original format conserved | FR-141, FR-146, FR-155 |
| (sidecar) | rg_categories | data | per tipoDte × field → A/B/C/D | FR-143; OQ-007 |
| account.move (DTE) | qr_url | char(200) | consultaPublica?ambiente=&codGen=&fechaEmi= | FR-147 |
| account.move (DTE) | delivery_modality | derived | sealed normal (CAT-004 1) / transitory normal-diferida / transitory contingency (CAT-004 2) | FR-145, FR-148 |
| account.move (DTE) | delivery_channel | selection | download_site / email | FR-149 |
| account.move (purchase) | seal_present | boolean | receiver-side demand check | FR-150 |

**Tier A archive mirror** (odoo):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_edi.archivo | archivo_dte | binary | verbatim JSON incl. firmaElectronica + selloRecibido (ex-contingency) | FR-152, FR-153 |
| l10n_sv_edi.archivo | sha256 | char(64) | integrity hash, verified on read | FR-152 |
| l10n_sv_edi.archivo | mirrored_at | datetime | reception-response time | FR-154 |
| l10n_sv_edi.archivo | conservation_until | date | generation date + 10 years | FR-155 |
| l10n_sv_edi.archivo | evidential_tier | metadata | AT copy > taxpayer copy > RG (CT 206) | FR-142 |

## 5. Odoo Mapping

Layer semantics: `saas` = generation/transformation/validation/transmission
logic in the Elixir core; `odoo` = the LGPL thin client's data-capture,
signing, mirroring and display surface; `shared` = private-protocol
contract items both sides must honor. Per D2 the SaaS never holds private
keys; per D3 the Tier A mirror is client-side and mandatory. Model names
are stable across Odoo 17/18/19/20; no version-specific behavior is
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-130 | shared | account.move, l10n_sv_edi.event | state chain | Chain orchestrated SaaS-side; the signature-before-transmission step is the client round-trip of FR-132 — both sides honor the ordering |
| FR-131 | odoo | l10n_sv_edi.signer (new) | — | Python JWS RS512 signer; no MH endpoint calls; no runtime dependency on MH firmador |
| FR-132 | shared | — | protocol envelope | Round-trip contract; exact envelope = `06_api-protocol.md` (OQ-001); client pre-validation runs before requesting a sign (D2 dual validation) |
| FR-133 | odoo | l10n_sv_edi.signer | firmaElectronica | JWS execution client-side; SaaS verifies against public cert before transmission |
| FR-134 | shared | l10n_sv_edi.event | — | Same round-trip for the 4 event types (03_events.md FR-090 amended S1 to orchestration wording; OQ-008 resolved) |
| FR-135 | saas | account.move, l10n_sv_edi.event | rejection family | Cert-error taxonomy surfaced through protocol state pushes; client renders vault-linked remediation |
| FR-136 | odoo | l10n_sv_edi.certificate | environment | Per-env vault rows; env binding enforced at sign time |
| FR-137 | odoo | l10n_sv_edi.certificate | key_password | Policy check at entry; SaaS API creds counterpart = 02 FR-057 |
| FR-138 | odoo | l10n_sv_edi.certificate | validity, state | Acreditamiento steps are manual (MH portal) — client tracks deadlines/alerts; test minimums owned by A11 onboarding file |
| FR-139 | odoo | l10n_sv_edi.certificate | private_key | Encrypted at rest (Odoo crypto util); excluded from logs/backups/protocol |
| FR-140 | shared | account.move | entrega flags | Package definition contract: Archivo DTE + RG together |
| FR-141 | saas | — | — | RG generated with the DTE in the same SaaS generation transaction |
| FR-142 | odoo | account.move, l10n_sv_edi.archivo | evidential_tier | Display + archive metadata; deduction logic never consults RG (02 FR-081/082) |
| FR-143 | saas | — | rg_categories sidecar | Category sidecar drives SaaS rendering; sidecar maintenance in catalogs pass (OQ-007) |
| FR-144 | saas | — | — | Sello merged into RG at seal time; sello never in outbound signed JSON |
| FR-145 | saas | account.move | delivery_modality | Estado transitorio for both deferred modalities; CAT-004 code 2 RG marking contingency-only; cleared on seal in current view, delivered copies immutable |
| FR-146 | saas | account.move | rg_document | SaaS renders (decision point recorded); client displays/prints from Tier A mirror and re-renders on demand |
| FR-147 | saas | — | qr_url | QR embedded in rendered RG from document data |
| FR-148 | shared | account.move | delivery_modality | Rides 02 FR-067–070 modality clocks; marking per FR-145 |
| FR-149 | saas | — | delivery_channel | SaaS hosts the download site; email triggered from odoo document flow using mirrored RG (content scope → OQ-005) |
| FR-150 | odoo | account.move (purchase) | seal_present | Receiver-demand surface on vendor bills + CT 206 warning chatter |
| FR-151 | shared | — | — | Module↔layer mapping recorded; AT reference architecture = SaaS deployment guidance (D1) |
| FR-152 | shared | l10n_sv_edi.archivo | archivo_dte, sha256 | SaaS assembles verbatim; client mirrors + verifies hash on read |
| FR-153 | saas | — | — | Byte-stable assembly (no re-serialization drift) |
| FR-154 | odoo | l10n_sv_edi.archivo | mirrored_at | Mandatory mirror at response time (incl. sealed events per 03 FR-090) |
| FR-155 | odoo | l10n_sv_edi.archivo | conservation_until | Generation-date anchored 10y; purge protection incl. untransmitted/rejected |
| FR-156 | shared | — | — | Tier B entitlement/export contract (06_api-protocol.md); ToS framing of non-delegable duty |
| FR-157 | odoo | l10n_sv_edi.archivo | — | Read paths exempt from D4 hard wall; local browse/search/export always on |
| FR-158 | odoo | l10n_sv_edi.archivo | backup surface | Encrypted client backups; SaaS-side backup only under Tier B |

## 6. Acceptance Criteria

- **AC-001:** Given a DTE ready for transmission, when the SaaS requests signing, then the private key never leaves the Odoo client (no key material in any request/response/webhook/log) and the returned artifact is a JWS compact serialization with alg RS512 over the conveyed payload, which the SaaS verifies against the public certificate before transmitting (FR-131/132/133).
- **AC-002:** Given a signing request whose ambiente is 00 while the vault's only valid certificate is ambiente 01, then the client refuses to sign and returns an environment-mismatch state (FR-136).
- **AC-003:** Given a vault or private-key password of 12 characters, of 26 characters, or of 13–25 characters missing any of letters/numbers/specials, then the vault rejects it; given 13–25 characters combining all three classes, then it is accepted (FR-137).
- **AC-004:** Given a certificate expiring in ≤ 30 days, then the client raises renewal alarms; given an expired certificate, then signing is blocked with the certificate error family, distinct from data-validation errors (FR-135/138).
- **AC-005:** Given a sealed FE, then the entrega package contains the Archivo DTE (full JSON incl. firmaElectronica and selloRecibido) plus the RG displaying the sello and the QR, and no category-C field appears on the RG (FR-140/143/144/147).
- **AC-006:** Given an RG where a category-D section/field is unused, then the RG prints that section/field name followed by a dash; given a category-B field relevant to the operation, then it is shown, and given it is irrelevant, then it may be omitted (FR-143).
- **AC-007:** Given a contingency-mode DTE delivered without seal, then its RG is marked tipo de transmisión contingencia (CAT-004 code 2); given the same document later sealed, then its current view shows the sello while the delivered transitory copy keeps the marking (FR-145).
- **AC-008:** Given the QR on any delivered RG, when decoded, then it equals `https://admin.factura.gob.sv/consultaPublica?ambiente={ambiente}&codGen={codigoGeneracion}&fechaEmi={fecEmi}` with the document's values (FR-147).
- **AC-009:** Given a reception response carrying a sello, then in the same response handling the Odoo Tier A mirror stores the verbatim Archivo DTE + rendered RG with sha256 and conservation_until = generation date + 10 years (FR-152/154/155).
- **AC-010:** Given a mirrored archivo whose stored bytes no longer match its sha256, then any read flags an integrity violation (alteración lesiva al interés fiscal) (FR-152).
- **AC-011:** Given a subscription in arrears (D4 hard wall active), then generation/signing/transmission are refused, while every previously mirrored DTE/RG remains browsable, printable and exportable locally (FR-157).
- **AC-012:** Given tier-down from Tier B to Tier A, then the emitter obtains a structured export of the SaaS-hosted archive before losing hosting and remains CT 147-compliant through the local mirror alone (FR-156).
- **AC-013:** Given a vendor bill recorded without a reception seal, then the purchase surface shows the missing-seal flag with the CT 206 deduction warning (FR-150).
- **AC-014:** Given an event (e.g. invalidación) ready for transmission, when the round-trip runs, then it is signed by the same client-side vault certificate and the SaaS transmits the signed event — the identical flow as DTEs (FR-134).
- **AC-015:** Given a rejected document whose codigoMsg family is certificate-related, then the client surfaces it as a certificate error linked to the vault record, not as a field-validation error (FR-135).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Signing envelope shape (FR-132): JWS must cover the exact bytes MH validates (full DTE/event JSON per Cuadro 10), but the private protocol is designed NOT to resemble the MH schema (D2). Decide: (a) opaque full-MH-JSON signing envelope (schema passes through the client for signing only), (b) server-side canonicalization with client-side digest signing (verify MH accepts the derived signature), or (c) hybrid. Cryptographic + IP design owned by `06_api-protocol.md`. | no | Takumi + SaaS team | resolved — Resolved by SV-PROT-FR-021..024 (envelope: opaque full MH JSON bytes; digest-signing rejected) |
| OQ-002 | Cuadro 10 OCR garbles (DG45 §5): "RSAS12" (likely RSASSA-PKCS1-v1_5), "CAGES" (2022 text read PKCS8EncodedKeySpec), "IWS" (= JWS). Confirm exact algorithm/key-encoding identifiers from 45_/46_ raw text; RS512 is taken from the firmador contract (22_). | no | Takumi (raw-text pass) | **resolved** (2026-08-17 pass) — 45_ p.40 re-OCR (PSM 6) prints "JSON Web Signature (JWS) … CAGES - PKCSBEncodedKeySpec … RSA512"; the twin Cuadro row in 18_ v1.2 (pypdf-native text) prints "**CAdES** - PKCS8ENCodedKeySpec … RSA512" → "CAGES" = CAdES misread. The `firmaElectronica` example header in BOTH normativas base64-decodes to `{"alg":"RS512"}` → the printed "RSA512" is the regulator's own typo for **RS512**. Operative identifiers: JWS / RS512 / PKCS8EncodedKeySpec (matches 22_ firmador contract) |
| OQ-003 | QR `fechaEmi` parameter format (DD-MM-YYYY vs YYYY-MM-DD) and URL-encoding rules are not stated in the extracts; confirm from 22_/46_ raw text or live consultaPublica behavior (FR-147). | no | Takumi (raw-text pass) | open |
| OQ-004 | Download-site minimum requirements (Cuadro 11 p. 43) not fully extracted (availability, retention, formats); obtain from 45_ raw text before the SaaS download portal is specified (FR-149). | no | SaaS team | open |
| OQ-005 | Email channel scope: Cuadro 11 says email carries "solo contenido de la entrega" — determine whether the Archivo DTE may be attached or only the RG/link; set the product default (FR-149). | no | Takumi + SaaS team | open |
| OQ-006 | Certificate renewal/revocation procedure post-acreditamiento (prod renewal cadence, test-cert re-issuance after the 2-month window, revocation notice channel) is not detailed in the 27_/46_ extracts; obtain before vault lifecycle FRs are implemented (FR-138). | no | Takumi (raw-text pass) | open |
| OQ-007 | Per-type Versión Legible A/B/C/D sidecar: the 2022 manual carries category columns per structure; v2.0 carries the Versión Legible column in Anexo II (per DG45 §4 concept note). Build the machine-readable per-type category sidecar during the catalogs pass and verify the v2.0 column exists for all 11 types (FR-143). | no | Takumi (catalogs pass) | open |
| OQ-008 | Cross-file conflict: `03_events.md` FR-090 states events are "generate[d], validate[d], sign[ed] and transmit[ted] exclusively in the SaaS core", which contradicts D2 (client-side signing; SaaS never holds private keys) and FR-131/134 here. This file governs; recommend amending 03 FR-090 wording ("orchestrate the signing round-trip") in a later pass. | no | Controller | resolved — `03_events.md` FR-090 amended (S1 controller pass) to orchestration wording: SaaS generates/validates/transmits, client signs; consistent with D2 and FR-131/134 here |
| OQ-009 | Normal-diferida entrega marking (FR-145): EVID-073 (18_ §11) ties the CAT-004 code 2 marking to contingency documents, and normal diferida is a normal modality held under AT resolution (`02_transmission.md` FR-068). Does 45_ §11.2 (v2.0 entrega framework) mandate any additional RG marking for normal-diferida entregas delivered in estado transitorio? Confirm from 45_ raw text. | no | Takumi (raw-text pass) | open |
