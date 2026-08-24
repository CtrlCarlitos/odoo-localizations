# W29 — SV Go-Live Readiness Assessment (Design)

**Date:** 2026-08-24
**Status:** approved design (owner, 2026-08-24)
**Wave class:** W29, hybrid — controller-direct authoring + one independent
reviewer dispatch (W24 ruling (g): resolution-carrying verifications get
reproduced, not trusted)
**Branch:** `sv-research` (`.worktrees/sv`)

## 1. Context & motivation

The SV requirements program is complete: 8 topics, 1,732 FRs, COVERAGE gate
green (92/9/2/24 of 127), registry 126 file rows, all waves through W28
merged to main (912cdde). `shared/docs/go-live-readiness.md` (D19 session)
mandates: "Country waves MUST verify their register before synthesis
sign-off; no go-live with an unverified row." The SV instantiation register
(§4 of that doc) is still marked "seeded 2026-08-19 — verify at
special-regimes synthesis close"; that synthesis closed long ago and the
full corpus is now available. The owner directed: verify the register AND
produce a full SV readiness assessment walking the universal catalog
against the corpus, with graded statuses and explicit gate semantics.

## 2. Deliverables

1. **NEW `sv/requirements/GO_LIVE_READINESS.md`** — the SV go-live
   readiness assessment (operational artifact, sits alongside
   `COVERAGE.md`; NOT a Takumi-template requirements file; mints no FRs).
2. **EDIT `shared/docs/go-live-readiness.md` §4** — SV register header
   flips from "seeded 2026-08-19 — verify at special-regimes synthesis
   close" to "verified 2026-08-24 — see
   `sv/requirements/GO_LIVE_READINESS.md`". The F-11 v19/v20
   pending-acquisition note stays (acquisition watch continues).
3. **Bookkeeping** — sv/HANDOVER.md §1/§5 wave log + §8 next-actions;
   sv/EXTRACTION_PLAN.md wave-log entry; commit + push sv-research.
   Merge to main = owner decision (fiftieth §4.6 run when directed).

## 3. Assessment doc structure

1. **Header** — status, as-of date, corpus basis (1,732 FRs; registry 126
   file rows; COVERAGE gate green), gate summary up top (counts per
   status).
2. **§1 Bootstrap master data** — the five universal rows instantiated
   for SV:
   - Legal identity & tax registrations (NIT/DUI + regime classification
     as company data with instrument provenance).
   - Establishments & points of sale (D17/D14 kin: warehouses ↔
     establecimientos, caja ↔ punto de venta, numeroControl per
     (type, establecimiento, punto de venta)).
   - Authorization ranges (SV: none — MH assigns; sequence-init still
     applies; contrast HN CAI as the canonical range case).
   - Chart of accounts (country CoA template + opening balances).
   - Legal sequences (D19(c): initialized from imported last-legacy
     documents, `is_sequence_init`, never user-typed).
3. **§2 Cut-over mechanics** — D18 tiered ingestion (T1–T4,
   `is_historical`), D19 posting tiers, config-never-hardcode, verbatim
   rounding, sequence initialization, straddle-filing checkpoint
   (F-07/F-14 monthly; F-11 annual).
4. **§3 Regulator onboarding** — the six universal rows instantiated:
   MH DTE emitter enrollment (Normativa v2.0; 27_ certificate-obtainment
   manual), credentials & certificates (JWS RS512/PKCS8 per ruling 9,
   per-environment, vault-stored), test/homologation pass, phased
   mandates (FE receptor threshold ≥3 SMM, D.L. 487), provider contracts
   (verify whether any certified intermediary is required in the SV
   model — expected: none), contingency authorization (contingencia
   regime, invalidación deadlines 1d/10háb/4d/3mo/2y-codes).
5. **§4 Register verification result** — the four shared-docs §4 SV rows
   (Enrollment, Credentials, Sequences/ranges, Straddle filings)
   re-stated with their disposition.
6. **§5 Blocking-gaps inventory** — every non-VERIFIED row enumerated
   with OQ/FR pointers, closing condition, and re-probe cadence
   (deadline where known).
7. **Gate statement** — statuses roll up: no BLOCKERs =
   gate-passing-for-planning; every BLOCKER must close before production
   go-live.

Every row carries: concern → SV instantiation → status → citations
(FR/LB ids) → notes/gaps. Citations consume corpus rows BY ID (never
restate).

## 4. Status vocabulary (exact semantics)

| Status | Meaning |
|---|---|
| **VERIFIED** | Requirement surface exists in corpus, cited by FR/LB id; implementation-ready |
| **CONFIG-GAP** | Corpus documents the requirement; implementation ships no default (config slot + OQ) — documented, non-blocking per the value-discipline canon |
| **WATCH** | External dependency (pending instrument/acquisition/regulator action) with a re-probe cadence and, where known, a deadline |
| **BLOCKER** | Unresolved absence/contradiction that must close before go-live — expected few or none; candidates evaluated honestly, never softened into WATCH |

## 5. Corpus surfaces the walk consumes

- **§1:** e-invoicing (DTE emitter registration, numeroControl /
  codPuntoVenta / establecimiento surfaces), `coa/02` (sv_coa template),
  D19(c) `is_sequence_init` FRs, regime classification (taxation/01).
- **§2:** `coa/08` FR-253..276 (the D18/D19 difference-route close-out),
  `is_historical` ingestion surfaces, fiscal-reporting F-07/F-14/F-11
  straddle rows.
- **§3:** 27_ certificate-obtainment anchors, JWS RS512/PKCS8 (ruling 9),
  contingencia + invalidación deadlines (e-invoicing 03), FE receptor
  ≥3 SMM threshold (D.L. 487).
- **Known open surfaces dispositioned honestly, each landing in its
  actual status:** F-11 v19/v20 pending prints (WATCH), RAEX reglamento
  config-gap (96_), AML reglamento (WATCH, deadline 2026-10-17),
  Economía rate (SOQ-26), Ley Registro de Comercio (SOQ-25), quiebra
  vintage (SOQ-24), 108_ operative-format config-gap (spe/02 OQ-10),
  SOQ-46 criteria-instrument negative watch.

## 6. Process (W29, hybrid)

1. **Prep** — controller grep-maps corpus surfaces per catalog concern
   (explore dispatches for breadth as needed).
2. **Authoring** — controller-direct write of the assessment.
3. **Independent review** — one reviewer dispatch reproduces every
   citation and status against the corpus (grep evidence required per
   row); verdict APPROVED / FIX-REQUIRED.
4. **Fix round** — if FIX-REQUIRED, controller applies prescribed fixes,
   re-review only if substantive.
5. **Register flip + bookkeeping** — shared-docs §4 edit, HANDOVER +
   EXTRACTION_PLAN records, commit + push.

## 7. Out of scope (recorded, not forgotten)

- Parallel-run tooling & reconciliation dashboards beyond residual
  clearing (D19(e)) — per go-live-readiness.md §5.
- Predecessor-system decommissioning & data-retention duties.
- Rollback doctrine for failed cut-overs.
- No FR minting; no requirements-file edits (a citation defect found
  during the walk surfaces as a ride note in the wave log, not an
  in-wave fix).
- Actual Odoo module implementation (Takumi/SaaS-team side; this repo is
  requirements-only).

## 8. Success criteria

- Every catalog row (§1 five + §2 six + §3 six) AND every register row
  (§4 four) dispositioned with a status and FR/LB citations where the
  corpus provides them.
- Reviewer reproduces all citations/statuses; zero unresolved findings.
- shared-docs register flipped to verified-with-pointer.
- COVERAGE gate still green (no source changes); registry unchanged.
- Bookkeeping complete; sv-research pushed.
