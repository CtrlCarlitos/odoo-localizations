# W29 — SV Go-Live Readiness Assessment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Verify the SV go-live instantiation register and deliver `sv/requirements/GO_LIVE_READINESS.md` — the universal-catalog walk against the 1,732-FR corpus with graded statuses (VERIFIED / CONFIG-GAP / WATCH / BLOCKER) and an explicit gate statement.

**Architecture:** Hybrid wave (owner-approved process A): controller-direct authoring from a pre-mapped citation table, then one independent reviewer dispatch reproducing every citation and status (W24 ruling (g): resolution-carrying verifications get reproduced, not trusted). One register edit in `shared/docs/go-live-readiness.md`. No FR minting, no requirements-file edits.

**Tech Stack:** Markdown corpus, `rg` grep verification, `shared/scripts/build_coverage.py sv --check`, git on branch `sv-research`.

**Spec:** `docs/superpowers/specs/2026-08-24-w29-sv-go-live-readiness-design.md`

## Global Constraints

- Work in `.worktrees/sv` on branch `sv-research`; commits short imperative, no emojis; push at wave close.
- Every assessment row: concern → SV instantiation → status → citations (FR/LB ids, by id never restated) → notes/gaps.
- Status semantics (verbatim from spec §4): VERIFIED = surface exists in corpus, cited by id, implementation-ready · CONFIG-GAP = documented requirement, ships no default (config slot + OQ), non-blocking · WATCH = external dependency with re-probe cadence/deadline · BLOCKER = must close before production go-live, never softened.
- No requirements-file edits; no FR minting; citation defects found during the walk surface as ride notes in the wave log only.
- Citations must be grep-reproducible: every id cited must exist verbatim in the named file.
- Counts derive from script/README parse (standing off-by-one lesson); COVERAGE gate must stay green (no source changes).
- HEAD at wave start: b102b1c (W29 design commit).

## Prep research findings (authoritative row map — Task 1 assembles from this)

Corpus basis: 1,732 FRs; registry 126 file rows; COVERAGE 92/9/2/24 of 127 gate green (W28).

### §1 Bootstrap master data — row map

| # | Concern | SV instantiation | Status | Citations (verified to exist) | Notes |
|---|---|---|---|---|---|
| 1 | Legal identity & tax registrations | NIT/DUI/CAT-022 identification; NIT+NRC active contributor profile; foreign-receptor registry IDs | VERIFIED | `SV-EINV-FR-021` (01: CAT-022: 13 DUI / 36 NIT / 02 / 37 / 03 passport), `SV-EINV-FR-023` (01: CCFE NIT 9/14 + active NRC), `SV-EINV-FR-042` (01: FEXE foreign receptor), `SV-EINV-FR-009` (01: fusion NIT AT merged list) | Emitter-side NIT/NRC ride the A11 gap row (§3.1) |
| 2 | Establishments & points of sale | numeroControl carries estab/PV; warehouses ↔ establecimientos, caja ↔ punto de venta (D17/D14) | VERIFIED | `SV-EINV-FR-004` (01: `DTE-{tipoDte:2}-{estab/PV:8}-{consecutivo:15}`, sections M/B/S/P + P-prefix PV), coa/02 template config sets | D14 canon; EVID-077 all-types-all-establishments rides §3 A11 |
| 3 | Authorization ranges | SV: NONE — MH assigns; Art. 115-A correlative authorization lifted for DTEs | VERIFIED | `SV-EINV-FR-004` (01: "no AT correlative authorization — Art. 115-A is lifted"), contrast: go-live-readiness.md §4 HN CAI row | Sequence-init still applies (row 5) |
| 4 | Chart of accounts | sv_coa template + opening balances | VERIFIED | coa/02 (`l10n_sv_chart` template surfaces, ~L589 "account template… Odoo-native"), coa/08 `SV-COA-FR-270` (adoption_transition: transition_date + adjustment_account, ganancias acumuladas) | Opening balances = §2 posting-tier rows |
| 5 | Legal sequences | D19(c): from imported last-legacy documents, `is_sequence_init`, never user-typed | VERIFIED | `SV-EINV-FR-004` (year-reset consecutive), coa/08 L521 (`is_sequence_init` follows D19 canon) | Corpus-thin: implementation rows are canon-level (shared docs); recorded as such |

### §2 Cut-over mechanics — row map

| # | Concern | SV instantiation | Status | Citations | Notes |
|---|---|---|---|---|---|
| 1 | Tiered ingestion (D18) | T1–T4; `is_historical` | VERIFIED | coa/08 L325-328 (D18 canon: is_historical, suppress/reallow, straddle-FY), taxation/15 (is_historical IVA surfaces), spe/02+spe/07 (is_historical files) | Canon + corpus consumers |
| 2 | Posting tiers (D19a) | GL-neutral closed / real open; control accounts | VERIFIED | coa/08 L317-321 (D19 posting-tier canon cited in-file), `SV-COA-FR-270` | |
| 3 | Config, never hardcode (D19a+) | migration/clearing + control accounts = config fields | VERIFIED | coa/08 FR-270 map row (adjustment_account m2o) | |
| 4 | Rounding (D19b) | legacy verbatim; residuals absorb | VERIFIED | frep/01 F-07 verbatim SUMA arithmetic family (casilla engine) | canon-cited |
| 5 | Sequence initialization (D19c) | canceled GL-neutral init records in LIVE journals | VERIFIED | (same as §1 row 5) | |
| 6 | Straddle-filing checkpoint (D19d) | F-07/F-14 monthly; F-11 annual | VERIFIED + WATCH limb | frep/01 `SV-FREP-FR-213/214` (declaration-state gate + delegated reception), frep/00_index scope rows | F-11 v19/v20 prints pending (MH landing watch) = the WATCH limb |

### §3 Regulator onboarding — row map

| # | Concern | SV instantiation | Status | Citations | Notes |
|---|---|---|---|---|---|
| 1 | Regime enrollment | MH DTE emitter registration; acreditamiento once per environment | VERIFIED (mechanics) + BLOCKER limb | `SV-EINV-FR-138` (04: portal info.dtes.mh.gob.sv → verification → cert generation → API user), LB-008 (04: 27_ manual) | AT authorization program (groups/dates) = A11 gap (below) |
| 2 | Credentials & certificates | JWS RS512/PKCS8; per-env vault; env separation | VERIFIED + WATCH limb | `SV-EINV-FR-136` (04: one ACTIVE cert per ambiente, cross-env refused), `SV-PROT-FR-021` (06: const RS512 opaque full-bytes), `SV-EINV-FR-054` (02: pruebas/producción separation), `SV-PROT-FR-013/023` (06: signing round-trip) | WATCH limb: 04 OQ-006 renewal/revocation procedure unobtained |
| 3 | Test/homologation pass | minimum tests per DTE type + event; test-env windows | **BLOCKER** | Gap: master-index A11 (8 governing EVIDs: 001/036/045/080/081/077/074/083) has NO requirements file — every e-invoicing file scopes "(A11)" out to a file never synthesized (S1 plan file list 01/02/03/04/05-cat/06 has no A11; FR-138's own citation dangles: "owned by the A11 onboarding file") | Closing condition: mint the A11 onboarding requirements file (S-wave; evidence owned; GT S-GT1 Task 5 `04_mandate-onboarding.md` = pattern) |
| 4 | Phased mandates | AT sets groups/dates; early adoption | **BLOCKER** (same root) | Gap: EVID-077 rows unsynthesized (A11) | Same closing condition as row 3 — ONE §5 inventory entry |
| 5 | Provider contracts | SV model = MH-direct; no certified intermediary | VERIFIED (negative) | `SV-EINV-FR-138` (portal-direct acquisition flow; no certificador surface anywhere in corpus) | Contrast GT (18 certificadores) |
| 6 | Contingency authorization | contingencia CAT-005 tipos 1-5; clocks; invalidación deadlines | VERIFIED | `SV-EINV-FR-103` (03: 1d/10háb/4d/3mo/2y differentiated), `SV-EINV-FR-111/112` (03: contingencia 24h/72h clocks), 03 §4 map rows (event.contingencia) | NCE contingency-eligible; CLE/DCLE/CDE excluded |

### §4 Register verification (shared-docs §4 SV rows)

| Row | Disposition |
|---|---|
| Enrollment | Verified w/ A11 caveat (mechanics VERIFIED; program rows = BLOCKER §3.3/3.4) |
| Credentials | Verified (JWS RS512/PKCS8; OQ-006 renewal watch) |
| Sequences/ranges | Verified (no ranges — MH assigns; sequence-init applies) |
| Straddle filings | Verified (F-07/F-14 monthly, F-11 annual; v19/v20 prints WATCH) |

### §5 Blocking-gaps inventory (authoritative list)

1. **BLOCKER — A11 onboarding/authorization never synthesized.** Surfaces: acreditamiento minimum tests (EVID-081 consola mandatory-starred; EVID-036/045 per-event), AT authorization groups/dates + early adoption (EVID-077), no physical/DTE coexistence + stock destruction + range reporting (EVID-074/083), 7-step onboarding (EVID-001 carried). Closing: one S-wave minting `sv/requirements/e-invoicing/05_onboarding.md` (or next free number — controller decides at mint; numbering per R30(b) SV-EINV continuation), evidence already in bank. Dangling in-corpus pointers to "(A11)": 01:201, 02:38, 03:42/211, 04:77, 06:36.
2. **WATCH items** (each: pointer + cadence/deadline): F-11 v19/v20 prints (MH landing; §6 recipe); cert renewal/revocation procedure (04 OQ-006; 27_/46_ gap); AML reglamento D.L. 426 (deadline 2026-10-17; uif WAF; 128_ corroboration no-lineamientos); SOQ-46 criteria instrument (negative at full-enumeration strength; cvpcpa + D.O. re-probe); D.O. gazette-feed stall (re-probe before any 2026-instrument hunt).
3. **CONFIG-GAP items** (non-blocking by value-discipline canon; cite canonical instances, reference per-file OQ registers for the long tail): RAEX reglamento (96_; SOQ-41 residual), Economía commission rate (SOQ-26), Ley Registro de Comercio + reglamento (SOQ-25), quiebra vintage (SOQ-24), 108_ operative format (spe/02 OQ-10), FE receptor ≥3 SMM amount (FR-020 → OQ-007), SMM-mayor-cuantía sector, BCR Tasa Máxima Legal (cml/08).

### Gate statement (rollup)

1 BLOCKER (A11 synthesis gap; single root, one closing wave) → **NOT go-live-ready until closed**; all other rows VERIFIED / CONFIG-GAP / WATCH. Expected post-A11: gate green for planning.

---

### Task 1: Author the assessment file

**Files:**
- Create: `sv/requirements/GO_LIVE_READINESS.md`

**Interfaces:**
- Consumes: the authoritative row map above (prep research, grep-verified 2026-08-24).
- Produces: the assessment doc — Task 2 verifies it, Task 3 reviews it, Task 4's register edit points to it.

- [ ] **Step 1: Write `sv/requirements/GO_LIVE_READINESS.md`** with sections: header (status/as-of 2026-08-24/corpus basis 1,732 FRs, registry 126 rows, COVERAGE gate green, gate summary: 15 VERIFIED rows + 4 VERIFIED-with-limb rows / 0 standalone CONFIG-GAP rows [§5.3 carries the canonical list] / 6 WATCH limbs / 1 BLOCKER) · §1 Bootstrap (5 rows) · §2 Cut-over (6 rows) · §3 Onboarding (6 rows) · §4 Register verification (4 rows) · §5 Blocking-gaps inventory (3 blocks per above) · §6 Gate statement. Assemble every row from the row map tables verbatim — concern, instantiation, status, citations, notes.
- [ ] **Step 2: Self-check structure** — Run: `rg -c "Status|VERIFIED|WATCH|CONFIG-GAP|BLOCKER" sv/requirements/GO_LIVE_READINESS.md`; verify 21 content rows + gate statement present; verify header counts match actual row statuses (recount by hand).
- [ ] **Step 3: Commit**

```bash
git add sv/requirements/GO_LIVE_READINESS.md
git commit -m "W29: SV go-live readiness assessment (catalog walk, graded statuses; A11 synthesis gap = the blocker)"
```

### Task 2: Mechanical citation verification

**Files:**
- Verify: `sv/requirements/GO_LIVE_READINESS.md` (no edits unless a citation fails)

**Interfaces:**
- Consumes: Task 1 file.
- Produces: verification evidence quoted in the Task 3 dispatch brief; any failed citation → corrected in this task, re-committed.

- [ ] **Step 1: Reproduce every FR/LB id citation.** For each id cited in the assessment, grep its owning file, e.g.: `rg -n "SV-EINV-FR-004\b" sv/requirements/e-invoicing/01_document-types.md`, `rg -n "SV-PROT-FR-021\b" sv/requirements/e-invoicing/06_api-protocol.md`, `rg -n "SV-FREP-FR-213\b" sv/requirements/fiscal-reporting/01_f07-declaration.md`, `rg -n "SV-COA-FR-270\b" sv/requirements/chart-of-accounts/08_deferred-tax-adoption.md`, `rg -n "SV-EINV-FR-103\b|SV-EINV-FR-111\b|SV-EINV-FR-112\b" sv/requirements/e-invoicing/03_events.md`, `rg -n "SV-EINV-FR-136\b|SV-EINV-FR-138\b" sv/requirements/e-invoicing/04_signing_delivery.md`. Expected: every id matches exactly once as a row definition (bold list item or table row).
- [ ] **Step 2: Verify line-anchor citations** — `rg -n "is_sequence_init" sv/requirements/chart-of-accounts/08_deferred-tax-adoption.md` (expect L521-area), `rg -n "D19|posting-tier" sv/requirements/chart-of-accounts/08_deferred-tax-adoption.md` (expect L317-328-area), `rg -n "Odoo-native" sv/requirements/chart-of-accounts/02_coa-structure.md` (expect L589-area). If a line number drifted, the assessment cites content (not line numbers) — confirm the content matches.
- [ ] **Step 3: Verify the A11-gap claim at full strength.** `rg -c "A11" sv/requirements/e-invoicing/*.md` (expect dangling refs in 01/02/03/04/06); `rg -rn "EVID-081" sv/requirements/` (expect ZERO hits — the evidence is unsynthesized); `rg -n "A11" docs/superpowers/plans/2026-08-17-s1-synthesis.md` (expect zero — never planned). Record outputs; these anchor the BLOCKER status.
- [ ] **Step 4: Verify status honesty against open-surface registers** — cross-check every WATCH/CONFIG-GAP item against sv/HANDOVER §7 + the master-index SOQ register (e.g. SOQ-24/25/26/41/46, OQ-006, OQ-007, spe/02 OQ-10 all present-and-open as claimed; nothing open-and-material omitted: sweep `rg -n "SOQ-" sv/.extractions/00_MASTER_INDEX.md | rg -i "open"` equivalent — the §5.3 list must cover every SOQ the HANDOVER §7 carries as open).
- [ ] **Step 5: Confirm no source drift** — Run: `source ~/.venvs/localizations/bin/activate && python shared/scripts/build_coverage.py sv --check`. Expected: `COVERAGE.md: no drift`.
- [ ] **Step 6: Fix any failed citation and amend/commit** — only if failures found: `git add -A sv/requirements/GO_LIVE_READINESS.md && git commit -m "W29: citation fixes from mechanical verification"`.

### Task 3: Independent reviewer dispatch

**Interfaces:**
- Consumes: Task 1+2 outputs.
- Produces: verdict APPROVED or FIX-REQUIRED with prescribed edits (drives Task 4).

- [ ] **Step 1: Dispatch one reviewer** (read-only role) with the brief: reproduce every citation and status in `sv/requirements/GO_LIVE_READINESS.md` against the corpus (the W24 ruling (g) standard — grep evidence per row); audit the gate rollup arithmetic; audit §5 completeness against the open-surface registers; check status-assignment honesty (nothing softened from BLOCKER, nothing inflated); verdict + prescribed edits. Include the Task 2 evidence in the brief; require independent re-runs, not trust.
- [ ] **Step 2: Record verdict** in the wave log (SDD ledger or controller notes; rulings preserved to sv/HANDOVER at Task 5 per W19 ruling (b)).

### Task 4: Fix round + register flip (conditional on Task 3)

**Files:**
- Modify: `sv/requirements/GO_LIVE_READINESS.md` (fixes, if any)
- Modify: `shared/docs/go-live-readiness.md` §4 SV header

**Interfaces:**
- Consumes: Task 3 verdict.
- Produces: final assessment + flipped register (Task 5 records).

- [ ] **Step 1 (if FIX-REQUIRED): apply prescribed fixes**, controller-verifying one-liners directly (S9 ruling (b) form); re-dispatch review only for substantive changes.
- [ ] **Step 2: Flip the register header** in `shared/docs/go-live-readiness.md` §4: `### SV (seeded 2026-08-19 — verify at special-regimes synthesis close)` → `### SV (verified 2026-08-24 — see sv/requirements/GO_LIVE_READINESS.md; one blocker: A11 onboarding synthesis gap)` — keep the existing four rows and the F-11 v19/v20 pending note intact (append `; verified W29` to the straddle-filings row's parenthetical if cleaner).
- [ ] **Step 3: Commit**

```bash
git add shared/docs/go-live-readiness.md sv/requirements/GO_LIVE_READINESS.md
git commit -m "W29: register flip + review fixes (go-live-readiness SV verified)"
```

### Task 5: Bookkeeping + push

**Files:**
- Modify: `sv/HANDOVER.md` (§1 wave log W29 entry, §8 next-actions), `sv/EXTRACTION_PLAN.md` (W29 log entry)

**Interfaces:**
- Consumes: all prior tasks + any Task 3 rulings.
- Produces: pushed sv-research; merge to main = owner decision (fiftieth §4.6 run when directed).

- [ ] **Step 1: sv/HANDOVER.md** — §1 W29 entry (scale: hybrid per approved design; deliverables; the A11 finding with its evidence chain; gate rollup; commits) + §8: add the A11 synthesis wave as the top acquisition-follow-up-class item (owner's call), note register flipped.
- [ ] **Step 2: sv/EXTRACTION_PLAN.md** — W29 wave-log entry (short form: pointer to HANDOVER §1).
- [ ] **Step 3: Final gate re-check** — `python shared/scripts/build_coverage.py sv --check` (expect no drift) + `git status` clean after commit.
- [ ] **Step 4: Commit + push**

```bash
git add sv/HANDOVER.md sv/EXTRACTION_PLAN.md
git commit -m "W29 bookkeeping: HANDOVER + EXTRACTION_PLAN wave log (A11 gap recorded; register verified)"
git push origin sv-research
```

## Self-review record (writing-plans checklist)

1. **Spec coverage:** deliverable 1 = Task 1 (+2/3/4 gates); deliverable 2 (register flip) = Task 4; deliverable 3 (bookkeeping) = Task 5; spec §3 structure = Task 1 Step 1; §6 process = Tasks 1–5 in order; §8 success criteria = Tasks 2/3/4/5 verification steps. §7 out-of-scope honored (no FR minting anywhere; A11 closure is recorded, not executed).
2. **Placeholder scan:** all statuses/citations concrete from prep research; grep commands given verbatim; no TBD/TODO.
3. **Consistency:** row-map statuses match §5 inventory (1 BLOCKER, root A11, rows 3.3/3.4); gate rollup matches header counts; register-flip text given verbatim.
