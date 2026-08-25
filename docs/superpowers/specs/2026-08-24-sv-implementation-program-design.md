# SV Implementation Program Design — 2026-08-24

**Status: APPROVED (all four sections approved in-session 2026-08-24).**
Turns the SV requirements corpus (1,747 FRs @ `c0b4ace`, GO_LIVE gate
GREEN FOR PLANNING) into a build program. Inputs:
`sv/CORPUS_DIGEST.md` (scoping digest), `shared/docs/saas-thin-client-
architecture.md` (D1–D6), `shared/docs/odoo-localization-guide.md`
(D13/D14/D17 + anatomy + testing rules), `shared/docs/regulatory-change-
management.md` (D7–D12/D15–D19), `sv/requirements/GO_LIVE_READINESS.md`.

## 0. Decisions from the brainstorming session (all owner-approved)

| Decision | Choice |
|---|---|
| Scope | Whole program (Odoo thin client + Elixir SaaS + private protocol), one spec |
| Code home | NEW private monorepo `CtrlCarlitos/sv-implementation`; split out the LGPL client later via subtree-split |
| Canon repo role | This repo stays requirements canon + process controller (wave plans, SHA bookkeeping, protocol spec authorship) |
| Odoo version | 19.0 first (newest stable); porting per the guide's rules |
| First milestone | One FE accepted by the REAL MH test ambiente |
| MH strategy | Simulator inner loop (CI oracle) + real-MH acceptance gate; credentials pursued in parallel from Wave 0 |
| Signing | Python JWS/RS512 signer inside the Odoo client (D2); NO firmador container |
| Decomposition | A: slice-then-breadth, wave boundaries = corpus file boundaries |

## 1. Program architecture & repo topology

```
CtrlCarlitos/odoo-localizations  (THIS repo — canon/controller, unchanged)
  sv/requirements/...            1,747 FRs + GO_LIVE + CORPUS_DIGEST
  shared/docs/...                D1–D19 decision log, guides
  docs/superpowers/plans+specs   wave plans + this design
  + gains: implementation wave records (code-repo SHA bookkeeping, §4.6-style)

CtrlCarlitos/sv-implementation   (NEW private monorepo — all code)
  client/odoo/                   LGPL-3 BOUNDARY — publishable via subtree-split later
    l10n_sv/                     fiscal core (COA, taxes, fiscal positions, tax report)
    l10n_sv_edi/                 thin-client EDI (D13/D14 model, vault, Python JWS signer,
                                 protocol client, archive mirror, entitlement banners)
    l10n_sv_reports/             F-07/F-14 casilla engine + filing calendar
    l10n_sv_hr/                  payroll (later wave)
  saas/elixir/                   PROPRIETARY — Phoenix umbrella (core + sv namespace per D6)
  protocol/                      pinned mirror of the protocol version in force
                                 (authoritative spec lives in the canon repo)
  sim/mh/                        MH simulator (schemas 52_ + Normativa v2.0 semantics)
  ci/                            contract tests, FR-traceability checks, LGPL-boundary guard
```

**Interaction rules:**
- Protocol spec is authored in the canon repo (D2 made it a requirements
  artifact: `sv/requirements/e-invoicing/06_api-protocol.md` + a versioned
  spec doc); `protocol/` in the monorepo is a pinned mirror updated by an
  explicit sync step.
- Code cites the canon by FR id (tests, docstrings); CI consumes catalog/
  parameter CSVs from the canon (fixture tag) as test data.
- Canon wave ledger records monorepo SHAs at wave closes (§4.6 bookkeeping
  style). No submodules anywhere.
- **LGPL boundary guard (CI):** `client/` must not reference `saas/`, must
  not import/link anything outside `client/` + Odoo + public PyPI; marker
  grep + import lint keep the subtree-split clean from day one.

## 2. Wave plan (slice-then-breadth)

| Wave | Delivers | Consumes (corpus) | Exit gate |
|---|---|---|---|
| 0 — Scaffold | Monorepo boot: Odoo 19.0 addon skeletons, Elixir umbrella, protocol mirror + sync, sim skeleton (schema harness), CI (tests, LGPL guard, FR-traceability lint) | EINV 06 (protocol v0.1: auth, entitlement fields, FE generate/response, state sync) | CI green on trivial round-trip; protocol v0.1 spec committed in canon |
| 1 — Vertical slice | Odoo invoice (stub fiscal) → protocol → SaaS builds FE → client signs → simulator validates → sello/estado mirrored | EINV 01/02/04/06 slices: FR-054/057, PROT-FR-013/021/023, CAT subset | FE passes simulator E2E; FR-cited tests green |
| 2 — Real-MH gate | Point stack at MH test ambiente (owner creds from Wave 0): transmission, rejection handling, 24h clock surfaced | EINV 02 transmission FRs; FR-166..168 counters as config rows | **One FE accepted by real MH test ambiente** = milestone 1 |
| 3 — Fiscal core | Full COA template, tax templates/grids, fiscal positions, tax report; replaces slice stubs | COA 01/02 (N1/N2) + TAX 07/08/09 frameworks | Chart installable; tax report computes; file-closure gate |
| 4 — EDI breadth | All 11 DTE types, 4 events, invalidación classes, contingency, full numeroControl sequencing (D13/D14), onboarding state machine + consola mirror | EINV 01..07 + PROT (~237 FRs) | Per-file FR-coverage gate; simulator regression complete |
| 5 — Fiscal reporting | F-07/F-14 casilla engine + annexes + días-hábiles engine + filing calendar | FREP 01..08 (214; consumes TAX-202..204 by id) | Casilla honesty rules tested; export flows |
| 6 — Payroll | SMM/ISSS/IPSFA/aguinaldo/indemnización, D15 correction windows | PAY 01..08 (147) | Dated-row machinery + invariants tested |
| 7 — Special regimes + COA depth | ZF/LSI D15 ladders, DUCA, FOVIAL/COTRANS; deferred-tax adoption | SPE (204) + COA 03..08 (222) | Full-corpus FR ledger closes; go-live register flips |

**Standing rules:** every wave = plan doc (canon repo) → subagent tasks →
per-task reviews → FR-coverage gate → one fix wave (the S-wave
methodology, applied to code). CONFIG-GAP classes (AT groups/dates,
test-count rows, Economía rates) stay config-empty by value-discipline.
Watch-triggered corpus amendments (F-11 v19/v20, AML reglamento,
aguinaldo-cap decree) ride as plan addenda, never mid-wave.

Wave 2→3 ordering is soft: if credentials lag, Wave 3 starts and Wave 2
slides (config-switched hookup, not a redesign).

## 3. Protocol v0.1 & slice data flow

**Endpoints (private minimal protocol — deliberately unlike MH JSON, D2):**

```
POST /v1/sv/dte/prepare     Odoo → SaaS: {common: {company, ambiente, doc_type, refs},
                                           sv: {partner, lines, totals, establishment, caja}}
  ← 201 {dte_id, canon_json, mh_schema_valid?, warnings[], plan: {sign_payload}}
POST /v1/sv/dte/{id}/signed Odoo → SaaS: {jws}   (client Python-signs sign_payload)
  ← 200 {estado, sello, codigo_generacion, mh_response}
GET  /v1/sv/dte/{id}        state poll / mirror resync
GET  /v1/sv/state           batch state sync (cron pull + webhook push)
```

Every response carries `entitlement: {status, expiry, grace}` (D4) and
`protocol_version` (semver per namespace, D6). Error taxonomy:
`validation` (client-fixable, field-level) / `regulator` (MH rejection,
corpus-typed codes) / `system` (retryable) / `entitlement`.

**Slice flow:** (1) `account.move` posts with FE doc type → EDI layer
builds the private payload (no MH schema knowledge client-side — SaaS IP).
(2) SaaS `prepare`: validates against its compiled schema matrix +
Normativa rules, assigns numeroControl (server-side single sequencing
store, D2), returns canon_json + exact sign_payload. (3) Odoo vault
(test-ambiente cert/key), Python JWS/RS512 signature. (4) SaaS verifies
JWS + (sim mode) full schema/crypto validation; returns estado + sello +
codigoGeneración. (5) Odoo writes the Tier-A archive mirror (sealed DTE +
RG per D3; §3.11 immutability) and updates move state.

**Error handling:** pre-validation failures block posting with field-level
errors; regulator rejections enter the 24h-fix clock (deadline via
FREP-202..204 días-hábiles engine by id); transmission failures queue with
8s/2-retry, then surface for contingency decision (FR-129 no-coexistence —
contingency is a separate emission path, Wave 4).

**Testing:** every test names FR ids; simulator = CI oracle;
real-MH suite separately tagged, credential-gated, never in CI.

## 4. Wave-0 engineering details

- `client/odoo/` — Odoo 19.0 addons; `l10n_sv` + `l10n_sv_edi` skeletons
  (`__manifest__.py`, dep `l10n_latam_invoice_document`), one minimal
  passing test each.
- `saas/elixir/` — Phoenix umbrella: `core` (auth, entitlement, protocol
  plumbing, state machine) + `sv` (FE namespace, schema matrix);
  Ecto/Postgres; `ex_json_schema` with schemas compiled from the canon's
  52_ set (pinned).
- `sim/mh/` — Elixir app, sibling of the SaaS umbrella in one mix
  workspace (own endpoint set, shared deps) exposing MH-shaped
  endpoints: validation, JWS verify, sello/codigoGeneración recomputation,
  Normativa v2.0 state transitions; deterministic mode via seeded fixtures.
- `ci/` — GitHub Actions: Odoo tests, Elixir tests, contract tests (both
  sides vs the same protocol fixtures), LGPL guard, FR-traceability lint
  (`# FR: SV-XXX-FR-nnn` citations must resolve to real corpus ids; the
  wave gate prints per-file coverage vs declared wave scope).
- Libraries: Odoo — `jwcrypto` only; SaaS/sim — Phoenix/Ecto/ex_json_schema.
- Secrets: dev fixture creds committed; real vault (per-env certs, FR-136
  single-ACTIVE-cert) stubbed Wave 0, implemented Wave 1.
- NOT in Wave 0: fiscal data, events, contingency, real MH calls,
  reports/payroll/spe/coa modules.

**Risks & mitigations:** (a) Odoo 19 API drift → minimal slice API
surface, port notes per file; (b) MH undocumented validation depth →
OQ-linked simulator divergence log; (c) year-one protocol churn → semver +
changelog from v0.1, one-command mirror sync; (d) single-controller
bandwidth → subagent waves with per-task reviews.

## 5. Post-program notes

- Each wave gets its implementation plan via the writing-plans skill
  (first: Wave 0), stored in this repo's `docs/superpowers/plans/`.
- The canon's sv/HANDOVER gains an "implementation program" section at
  Wave 0 close; wave records carry monorepo SHAs.
- Go-live surfaces stay governed by `sv/requirements/GO_LIVE_READINESS.md`
  — this program closes its WATCH items as waves land (F-11 prints → Wave
  5; AML reglamento → watch; MOQ-05 endpoints → Wave 2/4 as published).
