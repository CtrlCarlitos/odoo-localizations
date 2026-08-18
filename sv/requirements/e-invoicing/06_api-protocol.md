# SV — E-Invoicing — Client↔SaaS private protocol contract (API)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | Takumi synthesis wave 1 |
| Updated | 2026-08-17 |

## 1. Purpose

This file defines the functional requirements for the PRIVATE MINIMAL PROTOCOL
between the Odoo thin client and the Elixir/Phoenix SaaS core (master-index
cluster A12; architecture decisions D1–D6): the hybrid request/response
envelope with namespaced country payloads, per-namespace semantic versioning
with deprecation windows, transport and per-company API-key authentication
with rotation, the document/event generation operation lifecycle and its
idempotency contract, dual validation with the shared error/warning model,
the signing envelope (RESOLVING `04_signing_delivery.md` OQ-001 — the
SaaS sends the exact MH-format pre-seal JSON bytes and the client signs
them), entitlement state as a standing field in every response (D4 banners),
the state-change webhook/callback contract with delivery guarantees and
retry, archive mirror synchronization and Tier B surfaces (D3), and the
degradation/resilience posture (D1 hard wall; local read paths). It is the
contract BOTH Takumi's thin client and the SaaS team build against; its FR
prefix is `SV-PROT-FR-nnn` (fresh sequence — this file does not continue the
`SV-EINV-FR` numbering of files 01–04).

It does **not** cover: the MH-facing connector endpoints, retry-to-MH and
transmission modalities (`02_transmission.md`, A2/A8), per-type document
structures (`01_document-types.md`), event semantics and deadlines
(`03_events.md`), the JWS signing standard, certificate vault and delivery
mechanics (`04_signing_delivery.md` — this file owns only the wire envelope
of the signing round-trip), catalog governance (`../catalogs/05_governance.md`),
tax computation (A10), or onboarding/authorization (A11). Where an FR here
restates a decision from the architecture doc, that doc governs the
rationale; this file governs the contract detail.

## 2. Legal Basis

This is a product-contract file: its primary source is the S0.5 architecture
decision log; the regulatory anchors below bind the contract to legal duties
the protocol exists to satisfy. Authority order as per master index.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Product architecture decision log D1–D6 | S0.5 decisions: D1 Fly.io multi-region, no local fallback; D2 SaaS generation + client signing + private minimal protocol + dual validation; D3 tiered archive (Tier A mandatory mirror); D4 entitlement hard wall with read-path exemption; D6 hybrid multi-country protocol core + namespaced payloads | `shared/docs/saas-thin-client-architecture.md` | §S0.5 D1–D6 |
| LB-002 | D.L. 487-2022, Art. 119-F (CT 119-F) | Art. 119-F: contingency/force-majeure logic — basis for contractually framing the residual customer↔SaaS partition risk (D1) | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 119-F (EVID-083) |
| LB-003 | D.L. 487-2022, Art. 3 (CT 147 reformado) | CT 147 as reformed: 10-year conservation counted from generation, emitter's non-delegable duty — the duty the Tier A mirror sync exists to satisfy locally | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Art. 3 (EVID-083) |
| LB-004 | D.L. 487-2022, Arts. 119-B y 119-D | Art. 119-B: DTE exists once generated, signed, transmitted and sealed; 119-D: transmission rules and seal effects — the lifecycle the protocol's operation states and state-change pushes mirror | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Arts. 119-B/119-D (EVID-083) |
| LB-005 | Normativa de Cumplimiento DTE v2.0, Anexo I, Cuadro 10 (firma electrónica) | Annex I Table 10: `firmaElectronica` = JWS over the FULL DTE/event JSON — the cryptographic fact that decides the signing envelope (FR-021..024) | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I Cuadro 10 pp. 40–41 (via DG45 §4) |
| LB-006 | Normativa v2.0, Anexo I, Cuadro 11 (Archivo DTE y entrega) | Annex I Table 11: Archivo DTE = signed JSON structure + `firmaElectronica` + `selloRecibido`, conserved *íntegra* — the sealed artifact the mirror-sync responses carry | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo I Cuadro 11 pp. 43–44 (via DG45 §4) |
| LB-007 | Esquemas JSON DTE/Eventos, 11-ago-2026 | Official MH JSON schema set: PUBLIC artifact — basis of the no-IP-leak finding in FR-024 (the schema itself is not the SaaS's IP; the private→MH compilation logic is) | `sv/sources/52_Json_Schemas_DTE_Eventos_2026-08-11.zip` | schema files (EVID-087) |
| LB-008 | Manual Tecnológico (22_), §§2–5 | MH reference *firmador* pattern: local-only signer proves the client-side signing topology the protocol's sign round-trip implements | `sv/sources/22_Manual_Tecnologico_Transmision.pdf` | §§2–5 pp. 5–32 (EVID-079) |
| LB-009 | Manual Tecnológico para la Integración v2.0 (46_) | Technology Integration Manual v2.0: the 8s/2-retry MH posture and service windows — design reference for the webhook retry/delivery contract | `sv/sources/46_Manual_Tecnologico_Integracion_v2.0_2026-05-25.pdf` | §5.5 (EVID-085) |
| LB-010 | Código Tributario Arts. 199 y 206 (reformados) | CT 199/206: seal-dependent deductions, presumed income — the legal stakes the state-change pushes make visible to the client (cross-ref `02_transmission.md` FR-081) | `sv/sources/44_Reforma_CT_DTE_DL487_DO_2022-09-20.pdf` | Arts. 9–10 (EVID-083) |

## 3. Functional Requirements

### 3.1 Hybrid protocol envelope & namespaces (D6)

- **SV-PROT-FR-001:** Every protocol request and response shall use the hybrid envelope: a `common` core object — protocol (core) version, namespace version map, country code, environment (CAT-001: 00 *pruebas* / 01 *producción*), artifact kind (dte / event / control), correlation identifiers (`client_request_id`: client-generated UUID and idempotency key; `saas_operation_id`: server-assigned, stable across the whole operation lifecycle) and `occurred_at` — plus exactly ONE country namespace payload object (`"sv": {...}` today; a future `"gt"` joins alongside, never inside `sv`). (LB-001 D6)
- **SV-PROT-FR-002:** The private protocol shall not resemble the government JSON at generation time: request payloads use the private minimal vocabulary, and MH-format data shall cross the wire ONLY inside (a) the opaque signing envelope payload bytes (FR-021) and (b) sealed archive artifacts delivered for the Tier A mirror (FR-033) — the client shall never generate, business-parse, or structurally depend on MH-shape data outside those two channels. (LB-001 D2; LB-007)
- **SV-PROT-FR-003:** The SaaS shall implement the shared protocol CORE — authentication, entitlement/subscription state, archive sync surfaces, the transmission state machine and webhooks — as country-agnostic operations that reference no namespace internals; document/event payload semantics shall live exclusively in the `sv` namespace (and later siblings). (LB-001 D6)
- **SV-PROT-FR-004:** The system shall confine every namespace change to its namespace: a breaking change or defect in `sv` shall never alter the contract behavior of the core or of any other namespace, and core changes shall be regression-tested against every served namespace before release. (LB-001 D6)

### 3.2 Versioning & compatibility (D2/D6)

- **SV-PROT-FR-005:** The system shall version the protocol core and each country namespace INDEPENDENTLY with semantic versioning (MAJOR.MINOR.PATCH: MAJOR = breaking, MINOR = additive, PATCH = fix), declared in every request (client side) and every response (server side), with a published changelog maintained as a versioned artifact in this repository's requirements. (LB-001 D2/D6)
- **SV-PROT-FR-006:** The system shall perform a version handshake: on connect and on module upgrade the client announces its core + namespace versions and the SaaS replies with the supported set, deprecation state and sunset dates per component; if the client's namespace MAJOR is unsupported, the client shall block protocol calls for that namespace and surface a distinct version error (family `E-VERSION`), never a generic failure. (LB-001 D2/D6)
- **SV-PROT-FR-007:** The SaaS shall run every deprecation through an announced window: a MAJOR version, once deprecated, keeps serving until its published sunset date (default window ≥ 6 months, ToS-configurable — → OQ-001), and every response served on a deprecated version shall carry a deprecation notice with that sunset date which the client shall surface to the administrator. (LB-001 D2)
- **SV-PROT-FR-008:** Both sides shall be tolerant readers within a MAJOR: unknown response/request fields (MINOR/PATCH additions) shall be ignored without error, and no field shall ever be removed or retyped within a MAJOR version of any component. (LB-001 D2/D6)

### 3.3 Transport, authentication & API keys

- **SV-PROT-FR-009:** The protocol shall run exclusively over authenticated TLS, authorizing per-COMPANY API keys scoped per environment (one key set for 00, another for 01, mirroring the MH per-environment model), transmitted only in the authorization header — never in URLs, query strings, logs, error messages or webhook payloads. (LB-001 D2; cross-ref `02_transmission.md` FR-054)
- **SV-PROT-FR-010:** The SaaS shall support key ROTATION without downtime: at least two concurrently active keys per company+environment, with an explicit create → dual-active → revoke lifecycle, immediate revocation effect, and a visible fingerprint (prefix + last characters) with last-used timestamp for each key so the client administrator can identify and retire stale keys. (LB-001)
- **SV-PROT-FR-011:** The system shall distinguish transport/auth failures semantically: invalid/revoked key → authentication error family (`E-AUTH`) that the client shall NOT auto-retry; throttling → rate-limit family (`E-RATE`) with a machine-readable retry-after that the client shall honor with backoff. (LB-001; LB-009 as design reference)

### 3.4 Operation lifecycle & idempotency

- **SV-PROT-FR-012:** The system shall expose a generation operation over the protocol: the client submits a private-protocol document/event payload (individually or as a client-side batch with one correlation id per item); the SaaS compiles it to MH format, assigns `codigoGeneracion`/`numeroControl` from the single server-side sequencer (D2), validates authoritatively, and responds with either complete findings (FR-018) or a `pending_sign` state carrying the signing envelope (FR-021) — MH *lote* assembly is a SaaS-internal concern the client never addresses. (LB-001 D2; cross-ref `01_document-types.md` FR-003/004; `02_transmission.md` FR-059)
- **SV-PROT-FR-013:** The SaaS shall make every mutating operation idempotent by `client_request_id`: a resubmission with the same id and the same payload hash returns the SAME `saas_operation_id` and current operation state, consumes no additional sequence numbers and never creates a duplicate document — after any timeout or crash the client may safely retry with the identical id. A resubmission with the same `client_request_id` but a DIFFERENT payload hash shall be REJECTED with a dedicated idempotency-conflict error (family `E-IDEM`, FR-019): the SaaS shall neither serve, resume nor disclose the original operation's state or result on such a conflict — a genuinely new payload requires a freshly generated `client_request_id` from the client. The `sign_response` submission is idempotent by the composite retry key (`saas_operation_id` + `payload_sha256`), NOT by response-bytes equality: RS512 (RSASSA-PKCS1-v1_5) signing is randomized, so a crash between local signing and acknowledgment (FR-039) produces on resume a second, distinct-but-valid JWS over the same bytes — the SaaS shall accept ANY JWS that verifies against the emitter's public certificate over exactly those bytes (FR-023) as a redelivery of the same signing round-trip, with no duplicate operation or sequence consumption. (LB-001 D2; LB-009 dedup posture)
- **SV-PROT-FR-014:** The system shall expose the full operation state machine over the protocol — received → validating → pending_sign → signed → verify_failed / transmitting → transitorio → procesado [observado/ajustado] / rechazado / invalidado / not_emitted (mirroring `02_transmission.md` FR-076) — with the current state returned in every operation response AND pollable at any time by `saas_operation_id`. (LB-004; cross-ref 02 FR-076)
- **SV-PROT-FR-015:** Operations held by the affected-before-affecting ordering rule shall surface a `blocked` state identifying the dependency's `saas_operation_id`/`codigoGeneracion` in responses and state pushes, so the client renders exactly what the SaaS queue holds (cross-ref `02_transmission.md` FR-074/075). (LB-004; LB-001 D2)

### 3.5 Dual validation & the error/warning model (D2)

- **SV-PROT-FR-016:** The SaaS shall publish, per namespace version, a machine-readable PRE-VALIDATION PACK (the cheap subset: required fields, formats, caps, thresholds) that the Odoo client caches and runs before submission for early UX rejection; the pack refreshes on namespace version change, and a stale or missing pack shall never block submission — pre-validation is advisory only. (LB-001 D2)
- **SV-PROT-FR-017:** The SaaS shall ALWAYS run authoritative validation regardless of any client-side pre-validation (a client that skips or bugs its pre-check must still receive correct authoritative findings), and shall return the complete result set on every operation response. (LB-001 D2)
- **SV-PROT-FR-018:** The system shall use one finding object model for ALL validation results in both directions of the round-trip: `{code}` (stable, namespaced, dotted string — e.g. `sv.business.related_doc_not_sealed` — never renamed within a MAJOR), `{severity}` (`error` blocks the operation; `warning` surfaces but proceeds, mirroring MH observaciones), `{field_pointer}` (RFC 6901 JSON pointer into the namespace payload), `{message}` (human-readable, localizable) and optional evidence reference. (LB-001 D2; cross-ref `02_transmission.md` FR-077)
- **SV-PROT-FR-019:** The system shall classify every failure into exactly one contract family: `E-AUTH` (key invalid/revoked), `E-ENTITLEMENT` (D4 wall), `E-VERSION` (unsupported/deprecated-sunset component), `E-SCHEMA` (envelope/namespace shape), `E-BUSINESS` (fiscal rule violation), `E-ENV` (environment mismatch), `E-ORDER` (dependency/ordering), `E-SIGN` (signature verification/certificate), `E-MH` (relayed MH rejection, carrying the verbatim MH estado/clasificaMsg/codigoMsg/observaciones per `02_transmission.md` FR-086), `E-IDEM` (idempotency conflict: `client_request_id` reused with a different payload hash — FR-013), `E-RATE` (throttle/transient, retryable), and the warning families `W-BUSINESS`/`W-MH` (non-blocking observaciones). MH-originated findings (`E-MH`/`W-MH`) carry MH's own field names VERBATIM and define NO `field_pointer` mapping from MH vocabulary into the private namespace — RFC 6901 pointers (FR-018) exist only for SaaS-generated findings over the namespace payload. (LB-001 D2; cross-ref 02 FR-076/086, `04_signing_delivery.md` FR-135)
- **SV-PROT-FR-020:** The system shall deliver finding arrays COMPLETE — never truncated or summarized — attached to the operation's correlation ids, and the client shall render them on the document record with field-level placement driven by `field_pointer`. (LB-001 D2)

### 3.6 Signing envelope — resolution of `04_signing_delivery.md` OQ-001

- **SV-PROT-FR-021:** The system shall define the signing envelope as OPAQUE FULL-BYTES: the SaaS's `sign_request` (delivered inside the generation response or a state push) shall carry — artifact kind (dte / event type), ambiente, algorithm (const RS512), `payload_b64` = the EXACT MH-format pre-seal JSON bytes (no `firmaElectronica` field), `payload_sha256` of those bytes, and the operation correlation ids; the client's JWS shall cover exactly these bytes. (LB-005 Cuadro 10; cross-ref `04_signing_delivery.md` FR-132/133)
- **SV-PROT-FR-022:** The client shall treat `payload_b64` as opaque bytes: no parsing, no business use, no persistence beyond the operation lifetime; it shall check the request's ambiente against the vault certificate (refusing cross-environment signing per `04_signing_delivery.md` FR-136), sign locally, and return `sign_response` = the JWS compact serialization whose payload segment is the base64url of the received bytes, plus the round-trip state (signed / refused-env-mismatch). (LB-005; LB-008; cross-ref 04 FR-131/136)
- **SV-PROT-FR-023:** The SaaS shall, before any transmission, verify the returned JWS against the emitter's PUBLIC certificate AND verify that the payload segment decodes to bytes matching `payload_sha256`; on success it shall assemble the signed artifact byte-stably from the SAME bytes it sent (`04_signing_delivery.md` FR-153 — no re-serialization drift); a retried `sign_response` presenting a DIFFERENT but valid JWS under the same retry key (`saas_operation_id` + `payload_sha256`, FR-013) is an accepted redelivery, not a conflict; on failure it shall mark the operation `verify_failed` with an `E-SIGN` finding and transmit nothing. (LB-005; LB-006; cross-ref 04 FR-132/133/153)
- **SV-PROT-FR-024:** Decision record (resolves `04_signing_delivery.md` OQ-001): option (a) opaque full-MH-JSON-bytes envelope is adopted; server-side canonicalization with client-side digest signing is REJECTED because the MH validates `firmaElectronica` as a JWS over the full document JSON (Cuadro 10) — a digest-only signature would not verify at MH; there is no IP leak because the MH schema set is a public artifact (LB-007) and the sealed Archivo DTE already transits and persists client-side under Tier A (D3) — the SaaS's IP is the private→MH compilation and validation logic, which still never crosses the wire at generation time (FR-002). (LB-005; LB-007; LB-001 D2/D3)

### 3.7 Entitlement state in every response (D4)

- **SV-PROT-FR-025:** EVERY protocol response — success or error, any operation, including webhook envelopes — shall carry a standing entitlement object: subscription `status` (`active` / `grace` / `suspended`), `expires_at`, `grace_until` (nullable), a server-computed `banner` level (`none` / `warning` / `urgent` / `final`), and a `features` map of entitlement flags with additive, versioned keys (e.g. `archive_tier_b`, enabled doc-type bundles). (LB-001 D4)
- **SV-PROT-FR-026:** The SaaS shall enforce the D4 hard wall server-side ONLY: with `status` = suspended (or past grace), all generation, signing-relay and transmission operations are refused with an `E-ENTITLEMENT` finding; the client shall never be trusted to enforce entitlement and a tampered client gains nothing. (LB-001 D4)
- **SV-PROT-FR-027:** The client shall render escalating Odoo banners from the server-reported `banner` level (warning → urgent → final) on every protocol exchange, with grace/dunning windows configurable per ToS and rendered as communicated — the client renders state, it never decides it; the final level shall state plainly that electronic invoicing stops at expiry. (LB-001 D4)
- **SV-PROT-FR-028:** Read paths shall be exempt from the entitlement wall per D4/D3: browse, search, print and export over the local Tier A mirror shall remain fully available regardless of subscription state and shall function with zero SaaS connectivity; Tier B SaaS-hosted archive services (FR-035) require an account in good standing. (LB-001 D3/D4; cross-ref 04 FR-157)

### 3.8 Webhooks & state-change push (D6 core)

- **SV-PROT-FR-029:** The SaaS shall push state changes to registered client endpoints via the webhook catalog: transmission results (uno-a-uno and per-DTE lote results), seal arrival, rejection (with the 24-hour correction deadline), sub-condition changes (observado/ajustado), invalidation flips, overdue/not-emitted flags, event results, entitlement changes, mirror artifacts (FR-033) and version-deprecation notices. (LB-001 D6; cross-ref `02_transmission.md` FR-080, `03_events.md` FR-095)
- **SV-PROT-FR-030:** Every webhook shall use the signed envelope: `event_id` (globally unique UUID), `event_type` (catalog value), `occurred_at`, per-document/operation `state_version` (monotonic integer), correlation ids, namespace payload — authenticated with HMAC-SHA256 over body+timestamp using a registered endpoint secret (write-only, rotatable, never echoed) and a timestamp check against replay. (LB-001 D6)
- **SV-PROT-FR-031:** Webhook delivery shall be AT-LEAST-ONCE: the client shall apply every event idempotently (dedup by `event_id`; discard stale events whose `state_version` is not newer than locally recorded; any 2xx acknowledges), since cross-document ordering is not guaranteed. (LB-001 D6)
- **SV-PROT-FR-032:** The SaaS shall retry undelivered webhooks with exponential backoff for a configurable window (default ≥ 24h) and then dead-letter them; because push is never the only path, the client shall always be able to reconcile by PULL: current-state query per `saas_operation_id`, an event replay endpoint for a time range, and the mirror delta scan (FR-034) — pull is the fallback of record after outages (deployment shapes without a reachable HTTPS endpoint run poll-only — → OQ-003). (LB-001 D6; LB-009 as design reference)

### 3.9 Archive mirror sync & Tier B surfaces (D3)

- **SV-PROT-FR-033:** Every seal-carrying response and webhook shall carry the FULL archive artifact set for immediate Tier A mirroring at response time: the verbatim sealed Archivo DTE (MH JSON incl. `firmaElectronica` + `selloRecibido`), the rendered *Representación Gráfica*, and its sha256 — mandatory carriage, not a tier option (cross-ref `04_signing_delivery.md` FR-152/154). (LB-006; LB-003; LB-001 D3)
- **SV-PROT-FR-034:** The SaaS shall expose mirror reconciliation: a delta endpoint (by date range/period: sealed `codigoGeneración` list + sha256 + state per document/event) and a fetch-by-id backfill endpoint; the client shall run scheduled completeness checks against it and flag any gap between the SaaS record and the local Tier A mirror. (LB-001 D3; LB-003)
- **SV-PROT-FR-035:** The SaaS shall expose Tier B (paid) archive services behind the entitlement flags of FR-025: hosted long-term conservation with search, re-download and platform RG re-rendering, plus a structured exit export delivered while the account is in good standing (tier-down or cancellation) so the emitter stays CT 147-compliant via the local mirror alone. (LB-001 D3; LB-003; cross-ref 04 FR-156)

### 3.10 Resilience, degradation & SLA posture (D1)

- **SV-PROT-FR-036:** The client shall implement NO local fallback generation: when the SaaS is unreachable or refuses the call, confirming an invoice leaves the document as a draft with an explicit connectivity/entitlement notice, no MH-format JSON is produced locally, and the document submits automatically once the SaaS returns — MH-outage contingency is handled centrally by the SaaS in deferred mode (D1), never by offline client generation. (LB-001 D1; LB-002)
- **SV-PROT-FR-037:** The SaaS shall publish an unauthenticated health/status endpoint distinguishing service health from client-network failure, which the client shall consult (rate-limited) to render its connectivity surface: last-known operation states, SaaS reachability, and active incident/degradation state. (LB-001 D1)
- **SV-PROT-FR-038:** The ToS shall state the D1 service posture explicitly: multi-region deployment with an availability target at or above the MH platform's own, and the residual customer↔SaaS partition risk framed as force majeure per CT 119-F logic; the client's help surface shall state the no-local-fallback posture plainly. (LB-001 D1; LB-002)

### 3.11 Client-side operation safety (odoo)

- **SV-PROT-FR-039:** The client shall persist every pending protocol operation (submission, awaited sign_response, awaited seal) in a durable queue encrypted at rest BEFORE acknowledgment, surviving Odoo crashes/restarts and resuming automatically with the original `client_request_id` — no document may be lost or double-submitted across a crash. (LB-001 D2; LB-004)
- **SV-PROT-FR-040:** Both sides shall log every protocol exchange for support and audit under the correlation ids (`client_request_id`, `saas_operation_id`, `event_id`), with a guaranteed exclusion set: API keys, vault key material and endpoint secrets shall never appear in any log, diagnostic, support bundle or webhook. (LB-001; cross-ref `04_signing_delivery.md` FR-139; `02_transmission.md` FR-057)

## 4. Data Model

The wire contract itself is the data model: this section documents the
contract objects both sides must agree on. Catalog sidecars live in
[../catalogs/](../catalogs/); vault-side signing fields in
`04_signing_delivery.md` §4; MH response mirror fields in
`02_transmission.md` §4.

**Protocol envelope (`common`) — every request/response:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.envelope | protocol_version | semver | core contract version | FR-001, FR-005 |
| protocol.envelope | namespaces | map | {"sv": "1.0.0"} (future "gt") | FR-001, FR-005 |
| protocol.envelope | country / environment | char(2) / char(2) | sv · 00 pruebas / 01 producción (CAT-001) | FR-001, FR-009 |
| protocol.envelope | artifact | enum | dte · event (invalidación/contingencia/retorno/eop) · control | FR-001 |
| protocol.envelope | client_request_id | char(36) | UUID, client-generated, idempotency key | FR-001, FR-013 |
| protocol.envelope | saas_operation_id | char(36) | UUID, server-assigned, lifecycle-stable | FR-001, FR-014 |

**Entitlement object (standing in every response/webhook):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.entitlement | status | enum | active · grace · suspended | FR-025, FR-026 |
| protocol.entitlement | expires_at / grace_until | date / date-null | grace per ToS windows | FR-025, FR-027 |
| protocol.entitlement | banner | enum | none · warning · urgent · final (server-computed) | FR-027 |
| protocol.entitlement | features | map (additive keys) | e.g. archive_tier_b: bool · doc_type_bundles: [01,03,…] | FR-025, FR-035 |

**Finding object (error/warning model):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.finding | code | char (dotted, namespaced) | stable within a MAJOR, e.g. sv.business.related_doc_not_sealed | FR-018 |
| protocol.finding | severity | enum | error · warning | FR-018 |
| protocol.finding | field_pointer | char (RFC 6901) | pointer into the namespace payload | FR-018, FR-020 |
| protocol.finding | family | enum | E-AUTH · E-ENTITLEMENT · E-VERSION · E-SCHEMA · E-BUSINESS · E-ENV · E-ORDER · E-SIGN · E-MH · E-IDEM · E-RATE · W-* | FR-019, FR-013 |
| protocol.finding | message / evidence | text / ref | localizable · optional rule/source reference | FR-018 |

**API key & rotation (saas-side registry; client shows fingerprints):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| saas.api_key | company / environment | m2o / char(2) | one subscriber identity; keys per 00/01 | FR-009 |
| saas.api_key | fingerprint | char | prefix + last 4 (full value never returned) | FR-010 |
| saas.api_key | state / created_at / last_used_at | enum / datetime | active · revoked; immediate revocation | FR-010 |
| saas.api_key | rotation_pair | m2o self | ≥2 concurrently active during rotation | FR-010 |

**Operation state (mirrors `02_transmission.md` FR-076):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.operation | state | enum | received · validating · pending_sign · signed · verify_failed · blocked · transmitting · transitorio · procesado [observado/ajustado] · rechazado · invalidado · not_emitted | FR-014 |
| protocol.operation | blocked_by | char(36) / char(36) | dependency saas_operation_id / codigoGeneracion | FR-015 |
| protocol.operation | state_version | integer | monotonic per operation; stale-event discriminator | FR-031 |

**Signing envelope (wire owned here; vault fields in 04 §4):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.sign_request | artifact_kind / ambiente / algorithm | enum / char(2) / const | dte·event kinds · 00/01 · RS512 | FR-021 |
| protocol.sign_request | payload_b64 / payload_sha256 | base64 / char(64) | exact MH-format pre-seal bytes + digest | FR-021, FR-024 |
| protocol.sign_response | jws / state | char / enum | JWS compact serialization · signed · refused-env-mismatch (verify_failed returns as E-SIGN finding) | FR-022, FR-023 |
| protocol.sign_response | retry_key | composite | (saas_operation_id, payload_sha256) — randomized RS512 ⇒ JWS bytes are never the dedup basis; any valid JWS over the key's bytes is accepted | FR-013, FR-022, FR-023 |

**Webhook envelope & event catalog:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.webhook | event_id / event_type / occurred_at | char(36) / enum / datetime | globally unique · catalog value | FR-030 |
| protocol.webhook | event_type values | enum | dte.state_changed · event.state_changed · operation.verify_failed · entitlement.changed · mirror.artifact_available · version.deprecated | FR-029 |
| protocol.webhook | state_version | integer | monotonic per target document/operation | FR-031 |
| protocol.webhook | auth | hmac-sha256 + timestamp | body signature with write-only endpoint secret | FR-030 |

**Mirror sync:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| protocol.mirror_delta | range | date range / period | query window | FR-034 |
| protocol.mirror_delta | items | list | {codigoGeneracion, sha256, state} per sealed artifact | FR-034, FR-033 |

## 5. Odoo Mapping

Layer semantics: `shared` = the private-protocol contract both sides must
honor (this file IS the contract); `saas` = authoritative behavior in the
Elixir core; `odoo` = client-side behavior in the LGPL thin client. Model
names are stable across Odoo 17/18/19/20; nothing here requires
version-specific behavior.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | shared | — | envelope | Hybrid common+namespace envelope; client builds/validates envelope, never the MH shape |
| FR-002 | shared | — | — | IP posture: MH bytes only in sign envelope + sealed archive artifacts |
| FR-003 | saas | — | — | Country-agnostic core design duty (Elixir umbrella boundaries) |
| FR-004 | saas | — | — | Namespace isolation + cross-namespace regression duty |
| FR-005 | shared | — | — | Semver per component; changelog artifact lives in this repo |
| FR-006 | shared | l10n_sv_edi.protocol.session (new) | announced versions | Handshake on connect/upgrade; E-VERSION blocks per namespace |
| FR-007 | shared | res.company | l10n_sv_edi_sunset_notice | Deprecated-version notice surfaced to admin |
| FR-008 | shared | — | — | Tolerant reader both directions; no in-major removals |
| FR-009 | shared | res.company | l10n_sv_edi_api_key (new, encrypted) | Key stored encrypted client-side only for sending; per env 00/01 |
| FR-010 | saas | l10n_sv_edi.api.key | fingerprint, last_used | Rotation UI client-side; dual-active lifecycle server-side |
| FR-011 | shared | — | — | E-AUTH no-retry; E-RATE honors retry-after |
| FR-012 | saas | account.move | l10n_sv_edi_operation_id | Compile + server ids + validate + sign_request; batches carry per-item correlation |
| FR-013 | saas | — | — | Idempotency by client_request_id; E-IDEM conflict on same id + different payload hash; sign_response retry key (saas_operation_id + payload_sha256) tolerates randomized RS512 |
| FR-014 | shared | l10n_sv_edi.operation (new) | state | State machine mirrors 02 FR-076; pollable anytime |
| FR-015 | shared | l10n_sv_edi.operation | blocked_by | Rendered in the outbox (02 FR-084) |
| FR-016 | odoo | l10n_sv_edi.prevalidation.pack (new) | cached ruleset | Pack published per namespace version; advisory only |
| FR-017 | saas | — | — | Authoritative validation always runs, complete results returned |
| FR-018 | shared | — | finding object | Stable codes within a MAJOR; RFC 6901 pointers |
| FR-019 | shared | — | family enum | Taxonomy incl. E-IDEM conflict + E-MH relay carrying verbatim MH response fields (no pointer mapping) |
| FR-020 | shared | account.move | l10n_sv_edi_findings (new) | No truncation; field-level rendering via pointer |
| FR-021 | shared | — | sign_request | Opaque full-bytes envelope; resolves 04 OQ-001 |
| FR-022 | odoo | l10n_sv_edi.signer | — | Opaque handling; vault ambiente binding (04 FR-136); returns JWS |
| FR-023 | saas | — | — | Public-cert verify + sha256 match + byte-stable assembly (04 FR-153) |
| FR-024 | shared | — | — | Decision record; cross-file update of 04 OQ-001 → resolved (OQ-005) |
| FR-025 | shared | — | entitlement object | Standing in EVERY response incl. webhooks |
| FR-026 | saas | — | — | Hard wall server-side only; E-ENTITLEMENT |
| FR-027 | odoo | res.company UI | banner state | Escalating warning→urgent→final from server field |
| FR-028 | odoo | l10n_sv_edi.archivo | — | Local reads exempt; Tier B requires standing account |
| FR-029 | shared | l10n_sv_edi.state.event | event_type | Push catalog per D6 core |
| FR-030 | shared | — | webhook envelope | HMAC + timestamp; write-only secret |
| FR-031 | shared | l10n_sv_edi.state.event | event_id, state_version | Idempotent apply; stale discard; 2xx ack |
| FR-032 | saas | — | — | Backoff retry window → dead-letter; pull fallback always available |
| FR-033 | shared | l10n_sv_edi.archivo | archivo_dte, rg, sha256 | Artifact carriage mandatory at response time (04 FR-154) |
| FR-034 | saas | l10n_sv_edi.mirror.check (new) | delta, gaps | Client-side scheduled completeness checks + backfill |
| FR-035 | saas | — | — | Tier B endpoints behind entitlement flags; exit export |
| FR-036 | odoo | account.move | state + connectivity notice | No local fallback; drafts resubmit on recovery |
| FR-037 | saas | l10n_sv_edi.status.surface | — | Unauthenticated health endpoint; client connectivity UI |
| FR-038 | n/a | — | — | ToS/documentation requirement (D1 posture + CT 119-F framing) — no runtime layer |
| FR-039 | odoo | l10n_sv_edi.queue (new) | encrypted pending ops | Persist-before-ack; crash-safe resume; original request ids |
| FR-040 | shared | — | — | Correlation-id logging both sides; secret exclusion set |

## 6. Acceptance Criteria

- **AC-001:** Given any protocol exchange, when the payload is inspected, then it decomposes into `common` + exactly one namespace object (`sv`); and given a response carrying an unknown additive field, then both sides process it without error (FR-001, FR-008).
- **AC-002:** Given a client announcing `sv` MAJOR 2 while the SaaS supports {1}, when the handshake runs, then every `sv` call is blocked client-side with an `E-VERSION` finding and upgrade guidance — never a generic 500 (FR-006, FR-019).
- **AC-003:** Given a client operating on a deprecated MAJOR with sunset date D, when any response arrives, then it carries the deprecation notice and the client surfaces it to the administrator (FR-007).
- **AC-004:** Given two active API keys during rotation, when traffic runs across the overlap, then both keys work; given the old key is revoked, then it fails with `E-AUTH` and the client does not auto-retry it (FR-010, FR-011).
- **AC-005:** Given a submit that timed out client-side, when it is resubmitted with the identical `client_request_id` and payload, then the same `saas_operation_id` and state return, exactly one `numeroControl` is consumed, and no duplicate document exists (FR-013).
- **AC-006:** Given a client whose cached pre-validation pack is stale, when a document is submitted, then the SaaS authoritative findings still return complete, and a client-side pre-check error never reaches the wire (FR-016, FR-017).
- **AC-007:** Given an `E-BUSINESS` finding with `field_pointer` `/sv/lines/3/unit_price`, when the client renders it, then the message attaches to that invoice line in the UI and to the document's findings record (FR-018, FR-020).
- **AC-008:** Given a `sign_request` with payload bytes B, when the client returns the JWS, then the JWS payload segment base64url-decodes to exactly B and sha256(B) equals `payload_sha256`; given a tampered JWS, then the SaaS marks `verify_failed` with an `E-SIGN` finding and transmits nothing (FR-021, FR-022, FR-023).
- **AC-009:** Given a completed signing round-trip, when the client database is inspected, then no parsed or persisted MH-format business data exists outside the operation's opaque bytes and the sealed archive artifacts (FR-002, FR-022).
- **AC-010:** Given a suspended subscription, when ANY call is made, then the response carries the entitlement object with `banner: final`, generation is refused with `E-ENTITLEMENT`, and local archive browse/print/export still work (FR-025, FR-026, FR-028).
- **AC-011:** Given entitlement `banner` values warning → urgent → final over successive responses, then the Odoo banner escalates accordingly and the final banner states that electronic invoicing stops at expiry (FR-027).
- **AC-012:** Given duplicate delivery of the same `event_id`, then the client applies it once; given an event whose `state_version` is lower than locally recorded, then it is discarded; given a webhook with an invalid HMAC, then it is rejected and logged (FR-030, FR-031).
- **AC-013:** Given an endpoint down for the full retry window, when retries exhaust into dead-letter, then pull reconciliation (state query + event replay + mirror delta) reconstructs the identical final states and the mirror matches the SaaS record (FR-032, FR-034).
- **AC-014:** Given a seal-carrying response, then it contains the verbatim Archivo DTE (incl. `firmaElectronica` + `selloRecibido`), the rendered RG and sha256, and the client stores them in the Tier A mirror before acknowledging (FR-033).
- **AC-015:** Given the SaaS unreachable, when a user confirms an invoice, then it remains a draft with a connectivity notice, no MH-format JSON is generated locally, and it submits automatically once connectivity returns (FR-036).
- **AC-016:** Given a client-side network failure while the SaaS status endpoint reports healthy service, then the client displays a local-network indication (vs. a SaaS-degraded indication when the status endpoint reports an incident) (FR-037).
- **AC-017:** Given Odoo restarted mid-operation (kill before sign-response), when the client resumes, then the pending operation continues with its original `client_request_id` and is neither lost nor double-submitted (FR-039, FR-013).
- **AC-018:** Given any support log bundle from either side, when scanned, then it contains correlation ids but no API key, private key material or webhook secret (FR-040).
- **AC-019:** Given a client crash after local signing but before the `sign_response` is acknowledged, when the client resumes and re-signs the same payload bytes, then it produces a second JWS DISTINCT from the first and the SaaS accepts it for the SAME `saas_operation_id` (public-certificate verification + `payload_sha256` match per FR-023; retry key per FR-013) with no duplicate document and no additional sequence consumption (FR-013, FR-022, FR-039).
- **AC-020:** Given a mutating request reusing an existing `client_request_id` with a different payload hash, when the SaaS receives it, then it responds with an `E-IDEM` finding, does not serve, resume or disclose the original operation, and the client retries with a newly generated `client_request_id` (FR-013, FR-019).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Deprecation-window default length for MAJOR namespace/core versions (FR-007 assumes ≥ 6 months): product/ToS decision — confirm the shipped default and whether core and country namespaces differ. | no | Takumi + SaaS team | open |
| OQ-002 | Rate-limit thresholds per API key (`E-RATE`, FR-011): numeric fair-use values (req/s, burst, batch size) need ToS definition before enforcement ships. | no | SaaS team | open |
| OQ-003 | Webhook reachability for on-prem Odoo behind NAT (FR-032): confirm poll-only mode is a fully supported deployment shape (not merely a fallback), and whether long-poll/WebSocket is offered as an alternative push transport. | no | Takumi + SaaS team | open |
| OQ-004 | Batch signing for lote flows (FR-021): a 100-DTE lot implies up to 100 sign round-trips; decide whether the protocol adds a batch `sign_request` envelope (array of payloads) as a MINOR addition, and what per-item failure semantics apply. | no | Takumi + SaaS team | open |
| OQ-005 | Cross-file controller pass demanded by this file (executed in the S1 synthesis wave, task 7): (a) `04_signing_delivery.md` OQ-001 → `resolved`, pointing to FR-021..024 here — done; (b) the stale A12 pointer filename used by `01_document-types.md`, `02_transmission.md` and `03_events.md` corrected to this file's actual name — done; (c) `03_events.md` FR-090 amended to orchestration wording and `04_signing_delivery.md` OQ-008 → `resolved` — done. | no | Controller | resolved |
| OQ-006 | Abuse/anomaly telemetry (key-sharing detection): architecture doc lists it as a candidate mechanic with open legal questions (opt-in, privacy law) — decide before any telemetry crosses the protocol; until then the contract carries none. | no | Takumi + SaaS team | open |
| OQ-007 | Entitlement `features` map initial key set (FR-025): which flags ship in v1 (archive_tier_b confirmed per D3; doc-type bundles per the monetization note?) — freeze the initial additive key list before namespace v1.0.0 is cut. | no | Takumi + SaaS team | open |
