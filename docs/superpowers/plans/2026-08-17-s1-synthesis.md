# S1 Synthesis Implementation Plan — sv e-invoicing + catalogs Takumi files

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert the W1–W5.5 evidence base into the first Takumi-contract requirements files for El Salvador e-invoicing + catalogs, with FR numbering, LB citations, layer split (odoo/saas/shared per S0.5 decisions D1–D6), ACs, and coverage tracking.

**Architecture:** Requirements follow the template (7 fixed sections); Odoo Mapping carries a Layer column; the client↔SaaS private protocol is a first-class requirements artifact (D2/D6); catalogs ship as CSV sidecars (done) + a requirements file governing them (A9). Synthesis cites the master index, not raw evidence.

**Tech Stack:** Markdown; CSV sidecars (generated); FR IDs `SV-EINV-FR-nnn` / `SV-CAT-FR-nnn` / `SV-PROT-FR-nnn` (protocol).

**Spec:** `sv/.extractions/00_MASTER_INDEX.md` (governing lookup) + `shared/docs/requirements-template.md` (format authority) + `shared/docs/saas-thin-client-architecture.md` (D1–D6) + `shared/docs/regulatory-change-management.md` (version-regime policy).

## Global Constraints

- Every FR cites ≥1 LB (EVID id + source file + article/section/page). No trace → OQ, not FR.
- Authority order binding: 44_/45_/46_/50_/51_/52_ (2026) > 18_/19_/22_ (2025) > 40_/41_/25_ (2022). Old-EVID detail is history; cite as LB only where current authority is silent (mark "historical LB, verified vs 52_ schemas" — MOQ-08).
- Layer column required per FR row: `odoo` | `saas` | `shared` (never blank; `n/a` needs justification line).
- Version regime: where an FR depends on spec versions (schema version numbers, deadlines changed by v2.0), the Odoo Mapping notes record the version + effective date (per regulatory-change-management standing policy).
- English prose, Spanish legal terms inline with translation on first use.
- Open questions recorded as OQ rows in-file AND in the file's OQ section; never silently dropped.
- Files land in `sv/requirements/e-invoicing/` and `sv/requirements/catalogs/`; follow the template exactly (7 sections, none deleted).
- 12 open MOQs (Section C of master index): FR writers must check which MOQs affect their cluster; affected FRs get the OQ recorded in-file; synthesis proceeds (MOQs are trace-pending, not blockers) EXCEPT MOQ-07 (states/24h rule) — for it, write the FR from 18_ v1.2 evidence and mark "pending 45_ §10 verify".

---

### Task 1: `sv/requirements/e-invoicing/01_document-types.md`

**Files:** Create `sv/requirements/e-invoicing/01_document-types.md`
**Covers master cluster:** A1 (+ A10 tax-treatment hooks where they define per-type behavior)
**Content requirements:** Per-DTE-type FRs for all 11 types: legal identity (CT 107/119-G), authoritative JSON versions (DG45 §1.0), per-type receptor rules & thresholds (3-SMM for FE per D.L. 487 119-G VII — replaces $200), per-type structural constraints (item caps, related-doc rules, contingencia eligibility per DG45 §3.3 — CLE/DCLE/CDE excluded), FE-inclusive vs CCFE-net tax treatment (R1), distrito/domicilioFiscal new fields. Odoo Mapping: document types as l10n_latam pattern, per-type Layer split (generation=saas, display/posting=odoo).
**FR numbering:** SV-EINV-FR-001..0NN sequential.

### Task 2: `sv/requirements/e-invoicing/02_transmission.md`

**Files:** Create `sv/requirements/e-invoicing/02_transmission.md`
**Covers:** A2 (+ A8 state machine merged here: states, observaciones, 24h same-code rule MOQ-07-flagged, ordering rule)
**Content:** Auth/token lifecycle (saas), endpoints inventory (saas-side, client calls private protocol), retry 8s/2x, lote ≤100 + windows, holgura de transmisión (1 day + 30-min month-end), fecEmi ≤5 days rule (DG45 §3.1 N°10), transmission states (PROCESADO/RECHAZADO/observado/ajustado), affected-before-affecting ordering. Layer: mostly saas with odoo queue surface.

### Task 3: `sv/requirements/e-invoicing/03_events.md`

**Files:** Create `sv/requirements/e-invoicing/03_events.md`
**Covers:** A3 + A4 + A5 (all four events in one file)
**Content:** Invalidación (taxonomy, differentiated deadlines table from DG45 §2.2/§3.2, preconditions, codigoGeneracionR rules, CAT-024 semantics); Contingencia (allowed types incl. NCE per DG45 §3.3, 24h/72h clocks, 1000-item detail cap, batch 24/7); Retorno (3-month window, cases, no-receptor-crédito effects, FE/FEXE/FSEE targets); Operaciones Especiales (FVS reporting, control-interno comprobantes, AT-designated emitters, monthly 10-hábiles). Event schema versions (invalidación 3, contingencia 3, retorno 1, opEsp 1).

### Task 4: `sv/requirements/e-invoicing/04_signing_delivery.md`

**Files:** Create `sv/requirements/e-invoicing/04_signing_delivery.md`
**Covers:** A6 + A7
**Content:** Client-side signer (JWS RS512, cert vault, per-environment certs, password policy 13-25), MH firmador reference pattern; RG requirements (A/B/C/D categories, simultaneous generation, electronic delivery both modalities), QR (URL format, params), Archivo DTE composition, archive mirror (D3 Tier A: mandatory client-side mirror; Tier B upsell noted). Layer: signer+mirror=odoo, RG-render=saas(shared decision point).

### Task 5: `sv/requirements/e-invoicing/05_catalogs-governance.md` + catalogs README update

**Files:** Create `sv/requirements/catalogs/05_governance.md`; update `sv/requirements/catalogs/README.md` link
**Covers:** A9
**Content:** Catalog-as-data governance FRs: 33 sidecars as the machine-readable LB, dated-version policy (v1.1 lesson: codes re-assigned — modules must store dated rows, never replace), regeneration procedure, new-scope catalogs (CAT-008 distrito, CAT-033 régimen), CAT-002 event codes, corrections log. FR prefix SV-CAT-FR-nnn.

### Task 6: `sv/requirements/e-invoicing/06_api-protocol.md`

**Files:** Create `sv/requirements/e-invoicing/06_api-protocol.md`
**Covers:** A12 (D1–D6 as requirements)
**Content:** Private minimal protocol FRs: hybrid shape (common core + sv namespace), versioning policy (semver per namespace), dual validation contract (client pre-validation + saas authoritative; error/warning taxonomy surfaced fully), entitlement state in every response (D4 banners), archive mirror sync (D3), auth/keys, webhooks/callback contract (state changes push), degradation behavior (hard wall D4; read paths local). FR prefix SV-PROT-FR-nnn. This file is the contract Takumi's thin client builds against.

### Task 7: `sv/requirements/e-invoicing/00_index.md` + `sv/requirements/COVERAGE.md` + README updates

**Files:** Create `sv/requirements/e-invoicing/00_index.md`, `sv/requirements/COVERAGE.md`; update `sv/README.md` + `sv/requirements/README.md` topic status (e-invoicing → In review; catalogs → In review)
**Content:** Index file (FR id ranges per file, OQ rollup); COVERAGE.md: source-registry rows (44 files + schemas dir) × LB-citation status, generated by hand this wave (script later), every source mapped or not-applicable-noted; README status flips.
