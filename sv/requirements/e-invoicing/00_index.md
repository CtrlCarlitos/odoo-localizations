# SV — e-Invoicing requirements index

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | e-invoicing |
| Status  | draft (S1 synthesis wave, in review) |
| Authors | Takumi synthesis wave 1 + controller |
| Updated | 2026-08-17 |

This directory holds the S1 (synthesis wave 1) e-invoicing requirements:
document types, transmission, events, signing/delivery/archive, and the
client↔SaaS private protocol contract. Catalog governance lives in
[../catalogs/05_governance.md](../catalogs/05_governance.md) (file number 05
of this wave; SV-CAT-FR-001..018). Source-to-requirements coverage:
[../COVERAGE.md](../COVERAGE.md).

## Files & FR ranges

| File | Scope | FR range | FRs | LBs | ACs | OQs |
|------|-------|----------|-----|-----|-----|-----|
| [01_document-types.md](01_document-types.md) | 11 DTE types: legal identity, v2.0 structures, per-type rules | SV-EINV-FR-001..052 | 52 | 16 | 18 | 8 |
| [02_transmission.md](02_transmission.md) | SaaS-side MH connector, modalities/clocks, state machine | SV-EINV-FR-053..086 | 34 | 11 | 15 | 7 |
| [03_events.md](03_events.md) | The four event types (invalidación, contingencia, retorno, OpEsp) | SV-EINV-FR-087..129 | 43 | 14 | 18 | 6 |
| [04_signing_delivery.md](04_signing_delivery.md) | JWS signing, certificates, RG/QR, entrega, archive tiers | SV-EINV-FR-130..158 | 29 | 13 | 15 | 9 |
| [06_api-protocol.md](06_api-protocol.md) | Client↔SaaS private protocol contract (D2/D6) | SV-PROT-FR-001..040 | 40 | 10 | 19 | 7 |
| [../catalogs/05_governance.md](../catalogs/05_governance.md) | Catalog machine-readable authority, versioning, dated storage | SV-CAT-FR-001..018 | 18 | 6 | 8 | 5 |
| **Total** | | | **216** | **70** | **93** | **42** |

Numbering note: A6 (signing) and A7 (delivery) merged into
`04_signing_delivery.md`; the state machine (A8) is owned by
`02_transmission.md` (§3.9); the protocol contract (A12) is file 06 — there
is no file 05 in this directory (it lives in `../catalogs/`).

## Open-questions rollup (ids + titles)

Status legend: `open` unless noted `resolved`. 39 open / 3 resolved.

### 01_document-types.md (8)

- OQ-001 — CT Art. 114 signature requirement vs v2.0's dropped Sección 10 EXTENSIÓN. open
- OQ-002 — MOQ-08: exact JSON key spellings (verify vs 52_ schemas). open
- OQ-003 — MOQ-08 (part): NCE/NDE allowed CAT-015 codes. open
- OQ-004 — MOQ-09: global-discount sign in resumen.subTotal. open
- OQ-005 — MOQ-12: DCLE cuerpo item-cap applicability. open
- OQ-006 — MOQ-11: CDE async seal 24–72h still true under v2.0? open
- OQ-007 — FE receptor SMM threshold: which salarios-mínimos figure applies. open
- OQ-008 — Type-code discrepancy: DG45 §3.3 parentheticals vs CAT-002 v1.1. open

### 02_transmission.md (7)

- OQ-001 — MOQ-07 residual: after-window correction behavior (re-read 45_ §10/§10.2). open
- OQ-002 — R16: 22_-era reception holgura status under v2.0. open
- OQ-003 — MOQ-05: Retorno/OpEsp event endpoint paths unpublished. open
- OQ-004 — Test-environment lot cap: 22_ 300 vs 46_ 400. open
- OQ-005 — Service-status consultation endpoint (Anexo I rule 3.5) URL/contract. open
- OQ-006 — Production base URL OCR variants in 46_. open
- OQ-007 — MOQ-11: CDE async seal 24–72h (state-machine timing). open

### 03_events.md (6)

- OQ-001 — Contingencia `version`: Anexo V prints 3 vs 52_ schema const 4 (R7 amendment). open
- OQ-002 — Anexo V N°9 scope: 2-year activity-code window and same-date correspondence. open
- OQ-003 — Anexo V N°48 `codigoGeneracionR` null-type list vs CAT-002. open
- OQ-004 — MOQ-06: FVS physical-document flow needed for AT-authorized emitters? open
- OQ-005 — Wire keys vs Anexo III unified names (schema-pass mapping table). open
- OQ-006 — MOQ-05 cross-ref: Retorno/OpEsp endpoint paths (blocks FR-090 completion). open

### 04_signing_delivery.md (9)

- OQ-001 — Signing envelope shape (a/b/c options). **resolved** — by SV-PROT-FR-021..024 (opaque full MH JSON bytes; digest-signing rejected).
- OQ-002 — Cuadro 10 OCR garbles (RSAS12/CAGES/IWS; RS512 identifier). open
- OQ-003 — QR `fechaEmi` parameter format and URL-encoding rules. open
- OQ-004 — Download-site minimum requirements (Cuadro 11) not fully extracted. open
- OQ-005 — Email channel scope: Archivo DTE attach vs RG/link only. open
- OQ-006 — Certificate renewal/revocation procedure post-acreditamiento. open
- OQ-007 — Per-type Versión Legible A/B/C/D sidecar (catalogs pass). open
- OQ-008 — 03 FR-090 "sign… in the SaaS core" wording conflict. **resolved** — FR-090 amended to orchestration wording (S1).
- OQ-009 — Normal-diferida entrega marking (CAT-004 code 2 scope). open

### ../catalogs/05_governance.md (5)

- OQ-001 — MOQ-01: CAT-019 actividad económica canonical source/count. open
- OQ-002 — Exact vigencia date of the v1.1 catalog set. open
- OQ-003 — Cross-version catalog references in events (Anexo IV behavior). open
- OQ-004 — Machine-readable MH catalog-change feed exists? open
- OQ-005 — CAT-008 distrito count: EVID-086 "~75" vs 263-row sidecar. open

### 06_api-protocol.md (7)

- OQ-001 — Deprecation-window default length for MAJOR versions. open
- OQ-002 — Rate-limit thresholds per API key (E-RATE fair-use numbers). open
- OQ-003 — Webhook reachability for on-prem Odoo behind NAT. open
- OQ-004 — Batch signing for lote flows (batch sign_request envelope). open
- OQ-005 — Cross-file controller pass (04 OQ-001, stale A12 pointers, 03 FR-090). **resolved** — executed in the S1 synthesis wave (task 7).
- OQ-006 — Abuse/anomaly telemetry decision (legal questions). open
- OQ-007 — Entitlement `features` map initial key set. open
