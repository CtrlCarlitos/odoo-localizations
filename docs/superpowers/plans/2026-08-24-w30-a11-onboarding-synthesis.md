# W30 — A11 Onboarding/Authorization Synthesis Wave (go-live BLOCKER closing) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Mint the never-synthesized master-index cluster **A11 (onboarding/authorization)** as `sv/requirements/e-invoicing/07_onboarding.md` — the W29 go-live BLOCKER (GO_LIVE_READINESS.md §5.1) — from evidence already in bank (EVID-001/036/045/074/077/080/081/083), then resolve every dangling "(A11)" pointer, flip the COVERAGE row for 26_ (not-applicable → cited-as-LB), and flip the go-live gate to green (GO_LIVE_READINESS.md + shared/docs/go-live-readiness.md §4 SV register).

**Architecture:** Synthesis wave per the standing conventions (sv/HANDOVER.md §9): sequential per-task dispatches (fresh implementer + reviewer each, fix rounds, SDD ledger) → final whole-wave review → ONE fix wave → bookkeeping → push `sv-research`. Work happens ONLY in `.worktrees/sv` (branch `sv-research`). No new source acquisitions; registry UNCHANGED (126 file rows, next=129). R30(b): the new FRs continue the ONE `SV-EINV` prefix at **165** (current tail = FR-164 in 02_transmission.md §3.11). File number: **07** (next free in `e-invoicing/`; 05 deliberately belongs to `../catalogs/05_governance.md` — do not reuse).

**Tech Stack:** Markdown requirements files (Takumi contract: §1 scope, §2 LB table with verbatim Spanish + gloss + locator, §3 FRs, §4 data model, §5 Odoo mapping, §6 acceptance criteria, §7 OQ table), master index, COVERAGE regen script `shared/scripts/build_coverage.py`.

**Spec:** `sv/requirements/GO_LIVE_READINESS.md` §3.3/§3.4/§5.1 (the gap definition + closing condition); `sv/.extractions/00_MASTER_INDEX.md` §A11 (cluster definition: emitter acreditamiento, minimum tests per DTE type and per event, authorization resolution, implementation program, physical-stock destruction); `sv/HANDOVER.md` §8.2 TOP; `shared/docs/requirements-extraction-procedure.md`; GT structural precedent `gt/requirements/e-invoicing/04_mandate-onboarding.md` (W29-named pattern).

## Global Constraints (binding on every task)

- **Every FR cites an LB row** in the file's own §2 (by LB id); statutory verbatim quoted from the primary source where a text layer exists (40_/41_ are `.md` sources — quote them exactly, incl. the parenthetical qualifiers in the Paso list; 18_/26_/27_/44_ are raster PDFs with NO txt — the EV-bank rows are the citable extraction and LB rows take gloss-form quotes with `pp./§` locators per the standing `04_signing_delivery.md` LB-008 precedent for 27_). **Quote-tail self-checks are mandatory** (W23 ruling (e)).
- **By-ID sibling consumption, never restatement:** the coexistence rule incl. the tiquete ban = `SV-EINV-FR-129` (03_events, owns the FVS/Art.-113-OpEsp exception limb); the certificate vault/acreditamiento lifecycle + 2-month deadline tracking = `SV-EINV-FR-136..138` (04_signing_delivery); environment separation + API-user credentials = `SV-EINV-FR-054/057` (02_transmission); numeroControl estab/PV = `SV-EINV-FR-004` (01); the event-type registry = `SV-EINV-FR-087` (03); the catalog adaptation SLA (Cuadro 4) = `SV-CAT-FR-006` (../catalogs/05); días-hábiles arithmetic = `SV-FREP-FR-202..204` (fiscal-reporting) by id.
- **Numbering (R30(b)):** the new file mints **SV-EINV-FR-165..179** (15 FRs — allocation below is binding; any implementer-deemed addition must be disclosed as a deviation and lands only with reviewer approval, W23 ruling (d)). No other file mints EINV FRs in this wave. **Corpus: 1,732 → 1,747.**
- **D16/D15 doctrine:** mandate/obligation/report-liberation dates and authorization resolutions = append-only dated rows keyed by instrument, snapshotted on write. The AT program (groups/dates) has NO instrument in corpus → dated rows are config-gated slots with provenance, never invented values (value-discipline: config-gaps ship NO defaults, OQ-tracked).
- **The 2022-era manuals vs the 2026 regime:** 40_/26_/27_/41_ are 2022-vintage practice manuals; the 7-step flow's steps 5-6 (solicitud + Resolución de autorización) are printed as early-adopter-only ("solo para contribuyentes que opten por iniciar a emitir DTE previo a la fecha designada"); the current obligation route = AT program (EVID-077/083 transitorias). Encode both vintages with the qualifier; authority order 44_ > 45_/18_ > manuals.
- **Counts discipline:** the 26_ consola minimum-tests per doc type (counts per type) were NOT extracted (EVID-081 records only the table's existence + starred-mandatory semantics) → config rows with NO defaults (OQ-001). The 41_ Anexo 1 event minimums (5 invalidación + 5 contingencia) ARE in corpus verbatim — quote the table. Retorno/OpEsp test minimums are not evidenced (2026 events postdate 41_ v1.1) → OQ.
- **Corpus count discipline:** the ONLY FR additions are SV-EINV-FR-165..179 in the new file. T2/T3/T4 mint NO FRs. GO_LIVE_READINESS.md / shared-docs / index updates change ZERO existing FR texts.
- **Commits:** short imperative, no emojis, one per task (+ plan commit + fix-wave commits). Push only at wave close (S9 ruling (c)).
- **Dispatch template (S8 ruling (c), binding):** scoped evidence — the task's EVID ids with file/line windows + the two small `.md` source windows + ONE exemplar + target-file line windows; on-demand additional source via grep + bounded window. Harness exposes no per-subagent model parameter (S7 ruling (d)).
- **SDD ledger:** `.superpowers/sdd/2026-08-24-w30-a11-onboarding-synthesis/` — per-task implementer reports, reviewer verdicts, fix rounds, rulings. Before ANY workspace deletion, preserve rulings into `sv/HANDOVER.md` §5 (W19 ruling (b)).
- **Reviewer gates:** every task gets a fresh reviewer vs the master index A11 cluster + the EV bank rows + the `.md` sources; fix rounds until Approved (0 Critical/Important). Controller commits died-mid-task COMPLETE work UNMODIFIED after structure verification (S7 ruling (a)); re-dispatches zero-state deaths clean (S7 ruling (c)). **Rollup prose derives from the matrix** (W22/W23 ruling — no hand-computed counts in prose).

---

## Pre-loop prep (controller, before Task 1 dispatch)

- [ ] **P-1:** Verify branch state clean on `sv-research` at `956c41c` (post-W29 convergence); no external-check sweep needed (W27/W28 same-day sweeps recorded; D.O. stall + uif WAF rides unchanged; no acquisition depends on this wave).
- [ ] **P-2: Commit plan** — `git add docs/superpowers/plans/2026-08-24-w30-a11-onboarding-synthesis.md && git commit -m "W30 plan: A11 onboarding/authorization synthesis (go-live blocker closing)"`.

---

## Task 1: Mint `sv/requirements/e-invoicing/07_onboarding.md` (cluster A11 — SV-EINV-FR-165..179)

**Files:**
- Create: `sv/requirements/e-invoicing/07_onboarding.md`

**Interfaces:**
- Consumes (BY ID, pointer-only): SV-EINV-FR-129 (03; coexistence + tiquete ban + FVS/113 exception), SV-EINV-FR-136..138 (04; per-env vault, password policy, acreditamiento lifecycle + 2-month deadline), SV-EINV-FR-054/057 (02; env separation, API credentials), SV-EINV-FR-004 (01; numeroControl estab/PV), SV-EINV-FR-087 (03; event-type registry), SV-CAT-FR-006 (catalogs; Cuadro 4 SLA), SV-FREP-FR-202..204 (fiscal-reporting; días-hábiles engine), D14/D15/D16/D19 canons.
- Produces: `07_onboarding.md` with **SV-EINV-FR-165..179**, ~8 LB rows, ~6 ACs, ~4 OQs; the FR ids T2/T3 pointers cite.

**Evidence inputs (scoped, per dispatch template):**
- EV bank windows: `sv/.extractions/40_manual_estructuras_catalogo.evidence.md` lines 10-15 (EVID-001) + line 112 (the EVID-015 Anexo-1 placeholder note — superseded per master-index A11 History); `sv/.extractions/41_manual_eventos_invalidacion.evidence.md` lines 9-13 (EVID-036) + 63-66 (EVID-045); `sv/.extractions/18_Normativa_DTE_W5.evidence.md` lines 38-42 (EVID-074) + 60-64 (EVID-077) + 77-85 (EVID-080/081); `sv/.extractions/44-52_RegulatoryUpdate2026.evidence.md` lines 8-25 (EVID-083 — esp. line 11 [119-A faculties incl. obligation dates + report-liberation dates] and line 24 [transitorias]).
- Primary `.md` source windows (verbatim zones): `sv/sources/40_manual_estructuras_catalogo.md` lines 118-130 (the Paso 1-7 list); `sv/sources/41_manual_eventos_invalidacion.md` lines 69-75 (§1) + 394-399 (Anexo 1 table).
- Exemplar (ONE): `sv/requirements/e-invoicing/04_signing_delivery.md` (whole file, 241 lines — the same-directory house shape: header table, §1 scope prose with by-file boundary, §2 LB table, §3 FR sections, §4/§5/§6/§7). Pattern kin (read-only, structure reference only): `gt/requirements/e-invoicing/04_mandate-onboarding.md` lines 282-341 (§3.5 onboarding operational flow) + 319-341 (§3.6 lapse semantics) — GT content is NOT citable; only the section arrangement is the pattern.

**Content allocation (binding; implementer mints the shall-statements):**

- **§1 Purpose/scope:** the A11 cluster = the emitter-side onboarding and authorization regime: the 7-step onboarding flow, acreditamiento windows and the minimum-test regime (per DTE type + per event), the authorization program (AT groups/dates, early adoption, all-types-all-establishments discipline, report liberation), and the physical-stock cut-over (destruction + correlative-range reporting + no-coexistence). Does NOT cover (by-file boundary prose, house style): per-type structures (01), transmission/state machine + env separation (02), event semantics/deadlines + the coexistence rule itself (03 owns FR-129), certificate vault + acreditamiento portal lifecycle (04 owns FR-136..138), catalogs (../catalogs/05), the private protocol (06). Those files reference this one.
- **§2 LB rows (~8):**
  - **LB-001** — 44_ D.L. 487, Art. 119-A (AT faculties: normativa, structures, events, **obligation dates**, **report-liberation dates** — lit per EVID-083 gloss; loc Art. 1 p.3).
  - **LB-002** — 44_ D.L. 487, **transitorias** (obligation dates per AT program; physical stock: inform + present for destruction within **15 días hábiles** of becoming obligated; Art. 113/115 systems coexistence only where AT allows — regulated by Normativa §15).
  - **LB-003** — 18_ Normativa §15-16 (tiquetes banned for DTE emitters from 01-ene-2025; implementation program: **AT sets groups/dates**; emitter implements **ALL doc types it is authorized for across ALL establishments**; **may adopt early**; report-liberation dates per 119-A lit i; pp.22-24, EVID-077). Note: 45_ v2.0 §15 restates the tiquete ban (EVID-084 — FR-129 owns that limb by id).
  - **LB-004** — 18_ Normativa §12 (physical documents replaced by DTE presented to AT for **anulación/destrucción + correlative ranges reported**; **NO coexistence** — exception: Sistema de Facturación users; "Documentos impresos" includes PDF-emission systems lacking the official structure; p.18, EVID-074). Cross-note: the conservation limb of §12 is owned by 04 LB-010 — distinct slices.
  - **LB-005** — 40_ §I (the Paso 1-7 list verbatim incl. both "(solo para contribuyentes que opten por iniciar a emitir DTE previo a la fecha designada…)" qualifiers + the 2-month parenthetical in Paso 4; md 120-128, EVID-001).
  - **LB-006** — 26_ Consola manual (Sitio Emisores DTE sections: Inicio [onboarding state], Detalle de Emisor [authorized doc types], Certificado, Sistema de Facturación, **Solicitar Autorización** [test→prod], Consultas, Gestión de Usuario API; **minimum-tests table per doc type, starred = mandatory before requesting additional types**; TOC + pp.6-9, EVID-081).
  - **LB-007** — 41_ §1 + Anexo 1 (verbatim: "deberá realizar el proceso de pruebas para cada uno de los eventos… Las pruebas de dichos eventos serán consideradas al momento de realizar las verificaciones para el otorgamiento de la resolución"; the Anexo 1 table: Evento de Invalidación → 5, Evento de Contingencia → 5; md 69-75 + 394-399, EVID-036/045).
  - **LB-008** — 27_ Certificado manual (acreditamiento once per environment; test credentials valid **2 months** Sistema de Transmisión / **15 days** Sistema de Facturación; pp.5-10, EVID-080). Cross-note: 04 LB-008 is the same-instrument kin; the cert-side lifecycle is FR-136..138 by id — this row anchors the window semantics for the test regime.
- **§3 FRs (SV-EINV-FR-165..179 — allocation):**
  - §3.1 Onboarding workflow: **FR-165** (the 7-step flow as a tracked, per-environment onboarding state/checklist; steps 5-6 early-adopter-qualified as printed; consumes FR-136..138 by id for the cert steps); **FR-166** (per-DTE-type minimum-test completion tracking: counters + window binding against the 2-month/15-day deadlines — the deadline tracking itself is FR-138's; per-type required counts = config rows, NO defaults → OQ-001); **FR-167** (starred-mandatory gate: additional doc types requestable only after the starred types' minimums pass — LB-006).
  - §3.2 Event tests: **FR-168** (per-event minimums: 5 invalidación + 5 contingencia verbatim counts; the 2026 events Retorno/OpEsp have no evidenced test minimums → OQ-002); **FR-169** (event tests count toward the authorization verifications — LB-007 verbatim limb); **FR-170** (test environment reusable for AT-mandated updates — EVID-045 md 159; ties to SV-CAT-FR-006 adaptation deadlines by id).
  - §3.3 Authorization program: **FR-171** (early-adopter authorization: solicitud + DGII Resolución as dated rows with instrument provenance; post-2026 route = obligation by AT program, the resolución flow is the early/voluntary limb); **FR-172** (mandate-state model: AT groups/dates as append-only dated config rows — who-must-emit-by-when evaluation; NO cohort instrument in corpus → config-gated + watch → OQ-003); **FR-173** (early adoption path: a taxpayer may adopt before its group date → routes to FR-171); **FR-174** (implementation-program discipline: upon authorization/obligation the emitter implements ALL authorized doc types across ALL establishments — consumes FR-004 estab/PV by id + D14 warehouses↔establecimientos); **FR-175** (report-liberation dates per 119-A lit i as dated config rows, provenance-gated, no corpus instrument → rides OQ-003).
  - §3.4 Physical-stock cut-over: **FR-176** (inform AT + present physical stock for anulación/destrucción within 15 días hábiles of the obligation date — días-hábiles arithmetic SV-FREP-FR-202..204 by id); **FR-177** (correlative-range reporting of the destroyed/voided stock — the ranges record, D15 snapshot); **FR-178** (no-coexistence invariant for DTE emitters — consumes FR-129 by id for the FVS/Art.-113-OpEsp exception; the Sistema de Facturación exception limb recorded as the 119-H free-AT-solution awareness note).
  - §3.5 Status surface: **FR-179** (company-level onboarding/authorization status surface: authorized doc types [consola Detalle de Emisor mirror], checklist state, per-type/per-event test counters, mandate state + obligation date, stock-destruction state — each with dated-row provenance).
- **§4 Data model:** `l10n_sv_edi.onboarding.state` (company, environment, checklist steps); `l10n_sv_edi.onboarding.test` (scope: doc_type | event_type; required_count [config], passed_count, window deadline); `l10n_sv_edi.mandate.group` dated rows (group, obligation_date, provenance — config-gated); `l10n_sv_edi.authorization.resolution` (dated rows); `l10n_sv_edi.stock.destruction` (ranges, inform/present dates, state); res.company status fields (FR-179).
- **§5 Odoo mapping:** layer rows per FR (odoo = checklist/status/config surfaces; saas = gates consuming the dated rows; shared = the dated-row registries). Version note per house style.
- **§6 ACs (~6):** e.g. an emitter completing 5+5 event tests before requesting authorization; a starred-type gate blocking an additional-type request; a group-date row flipping a company to obligated with the 15-día-hábile stock clock computed via the días-hábiles engine; a destruction-range record snapshotted; an early adopter path; the no-coexistence block for a non-exception system.
- **§7 OQs (~4):** OQ-001 (26_ per-type test counts not extracted — config rows, no defaults); OQ-002 (Retorno/OpEsp test minimums not evidenced — 2026 events postdate 41_ v1.1); OQ-003 (AT program instruments [groups/dates] + report-liberation acts not in corpus — dated rows config-gated; watch kin MOQ-05 class, re-probe rides the D.O./factura cadence); OQ-004 (26_/27_ manuals are 2022-vintage portal flows — currency watch shared with 04 OQ-006 kin; portal-flow drift re-probe at cadence).

**Review gate:** fresh reviewer verifies vs the master-index A11 cluster + all eight EVID rows + both `.md` source windows: verbatim fidelity INCL. QUOTE TAILS (the Paso list qualifiers; the Anexo 1 table; the 41_ §1 sentence); FR contiguity 165..179 (EINV tail 164 → 165); by-id discipline (FR-129/136..138/054/057/004/087/CAT-FR-006/FREP-202..204 never restated); config-gap discipline (no invented counts/dates); the 2022-vs-2026 vintage qualifiers present; LB gloss-form quotes only where no text layer exists (26_/27_/18_/44_); §1 boundary prose consistent with the six sibling files.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W30 T1: mint e-invoicing/07_onboarding.md — cluster A11 synthesized (SV-EINV-FR-165..179)"`

---

## Task 2: Dangling-pointer resolution + e-invoicing 00_index (NO new FRs)

**Files:**
- Modify: `sv/requirements/e-invoicing/01_document-types.md` (§1 line ~30 zone + §5 FR-001 row note)
- Modify: `sv/requirements/e-invoicing/02_transmission.md` (§1 line ~38 zone)
- Modify: `sv/requirements/e-invoicing/03_events.md` (§1 line ~42 zone + §5 FR-087 row note)
- Modify: `sv/requirements/e-invoicing/04_signing_delivery.md` (§1 lines ~34-35 zone + FR-138 body tail + §5 FR-138 row note)
- Modify: `sv/requirements/e-invoicing/06_api-protocol.md` (§1 line ~36 zone)
- Modify: `sv/requirements/e-invoicing/00_index.md` (file table row, numbering note, OQ rollup, status/Updated lines)
- Verify-only: `sv/requirements/commercial-legal/01:354 · 04:136,1006 · 05:82,134,213,411,750,816,823,835 · 07:88,693` (the W29 §5.1 cross-topic inventory — NO text edits; record that the cluster refs now resolve via the A11→file mapping T3 records)

**Edits:**
- **01** §1: "onboarding/authorization (A11)" → "onboarding/authorization (A11, `07_onboarding.md`)". §5 FR-001 note: "per-company enablement gated by AT authorization (A11 file)" → "…gated by AT authorization (`07_onboarding.md` FR-172/174/179 by id)".
- **02** §1: same file-pointer insertion for the A11 clause.
- **03** §1: same insertion. §5 FR-087 note: "per-event enablement gated by acreditamiento (A11)" → "…gated by acreditamiento (`07_onboarding.md` FR-166..168 by id)".
- **04** §1: same insertion ("onboarding/authorization beyond certificate acquisition (A11)" → "(A11, `07_onboarding.md`)"). FR-138 body tail: "(onboarding test regime owned by the A11 onboarding file)" → "(onboarding test regime owned by `07_onboarding.md` FR-166..170, by id)". §5 FR-138 note cell: "test minimums owned by A11 onboarding file" → "test minimums owned by `07_onboarding.md` (FR-166..170)".
- **06** §1: same insertion for "onboarding/authorization (A11)".
- **00_index:** file table gains the 07 row (scope "A11 onboarding/authorization: 7-step flow, minimum tests, AT program, physical-stock cut-over"; FR range `SV-EINV-FR-165..179`; 15 FRs + counted LBs/ACs/OQs from T1's delivered file); Total row → **237 FRs** + recounted LB/AC/OQ (derive from grep counts of the delivered file — never hand-computed); numbering note gains "07 = the A11 onboarding file (W30); there is still no file 05 here (it lives in ../catalogs/)"; OQ rollup gains the 07 section (4 OQs per T1); header Status/Updated lines note the W30 mint.
- **cml verification:** grep the 13 inventoried anchors; confirm each references the A11 cluster (now resolvable); NO edits (cluster-id language is house convention); the verification note lands in the implementer report.

**Review gate:** reviewer re-greps `grep -rn "(A11" sv/requirements/` — every hit either carries the file pointer or is a cml cluster ref inventoried in W29 §5.1; index counts reproduce from grep; ZERO FR-text changes outside the FR-001/FR-087/FR-138 note cells named above (those cells are pointers, not FR bodies — the FR body edit is limited to 04 FR-138's trailing parenthetical).

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W30 T2: resolve dangling A11 pointers (01/02/03/04/06 + index) — 07_by-id wiring"`

---

## Task 3: Master-index A11 closure + COVERAGE regen + go-live gate flip

**Files:**
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (A11 section closure note + Build-note header append)
- Modify: `sv/requirements/COVERAGE_NOTES.md` (retire the 26_ N/A rationale lines — curated refresh, W20 ruling (d) precedent)
- Regenerate: `sv/requirements/COVERAGE.md` via `python3 shared/scripts/build_coverage.py sv` (gate: `python3 shared/scripts/build_coverage.py sv --check` → no drift; bare `--check` misparses — country arg required, W20 ruling (g))
- Modify: `sv/requirements/GO_LIVE_READINESS.md` (gate flip)
- Modify: `shared/docs/go-live-readiness.md:59` (SV register row — blocker note resolved)

**Edits:**
- **Master index:** A11 section gains a closing line: "**W30 (2026-08-24): SYNTHESIZED — `sv/requirements/e-invoicing/07_onboarding.md` (SV-EINV-FR-165..179); the S1 silent omission closed; dangling pointer sweep executed.**" Header Build note gains the W30 one-liner (corpus 1,732 → 1,747; 26_ cited).
- **COVERAGE:** expected flips — `26_Manual_Consola_Administrativa.pdf` not-applicable-this-wave → cited-as-LB (`e-invoicing/07_onboarding.md` LB row); the already-cited 18_/40_/41_/44_ rows gain `07_onboarding.md` in their citing-file columns (LB source columns — S8 lesson: grep ALL LB source columns of the new file); rollup expected **93 cited / 8 N-A / 2 superseded / 24 pending of 127** — VERIFY FROM THE SCRIPT OUTPUT (matrix-derived prose only). COVERAGE_NOTES: retire the two 26_ lines (19 + 51 zones).
- **GO_LIVE_READINESS.md:** header (Corpus basis 1,747; COVERAGE line per script; Updated + W30 note); §3.1 → `VERIFIED (mechanics)` (BLOCKER limb resolved — drop the limb; mechanics citations stand + add 07 by-id citations); §3.3 → `VERIFIED` with citations to the 07 FR ids (test regime: FR-166..170) + closing-condition note "closed W30"; §3.4 → `VERIFIED` (FR-171..175); §4 Enrollment row → `VERIFIED (mechanics)` (drop the limb); §1 row 2 note — the EVID-077 rides-A11 tail now resolves (07 FR-174); **Gate summary §-rollup recounted from the 21 rows: expect 17 VERIFIED · 4 WATCH-limb rows (§2.6, §3.2, §4.2, §4.4) · 0 BLOCKER** (recount from the matrix, W23 ruling (f)); §5.1 → heading "**5.1 BLOCKER — CLOSED (W30)**" + body note (mint record + pointer sweep + gate flip); §6 gate statement → green for planning.
- **shared/docs/go-live-readiness.md:59:** "one blocker: A11 onboarding synthesis gap" → "blocker closed 2026-08-24 — A11 synthesized (`sv/requirements/e-invoicing/07_onboarding.md`, W30); gate green for planning".

**Review gate:** reviewer re-runs the coverage script (--check green) + re-greps the rollup arithmetic from the GO_LIVE matrix (17/4/0); master-index append consistent with T1/T2 diffs; shared-docs row verified; ZERO requirement-file FR edits.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W30 T3: master-index A11 closure + COVERAGE regen (26_ cited) + go-live gate flip"`

---

## Final whole-wave review + ONE fix wave (controller)

- [ ] **F-1:** Dispatch a fresh whole-wave reviewer (read-only): all three task diffs vs the plan + EV bank + source windows + GO_LIVE §5.1 closing condition; verdict MERGE-READY / USABLE-WITH-FIXES; log to SDD ledger.
- [ ] **F-2:** If USABLE-WITH-FIXES: execute ONE fix wave addressing all Critical/Important findings (deferred minors triaged ride/ignore per house convention); re-verify; commit.
- [ ] **F-3:** Bookkeeping (Task 4): update `sv/HANDOVER.md` (§1 wave-log entry; §3 EVID state unchanged; §4 corpus table e-invoicing row 222→237 + totals 1,732→1,747 + COVERAGE rollup 93/8/2/24; §5 W30 log + W30-process rulings; §8 next-actions — item 2 TOP struck, go-live blocker closed, remaining = watches + owner merges) and `sv/EXTRACTION_PLAN.md` (W30 extraction-log entry); preserve W30 process rulings into HANDOVER §5 BEFORE any SDD workspace deletion (W19 ruling (b)); commit: `git commit -m "W30 close: HANDOVER + EXTRACTION_PLAN bookkeeping"`.
- [ ] **F-4:** Push `sv-research`. Merge to main = owner decision (rebase-then-merge per §4.6; never force-push).

## Expected end state

- `sv/requirements/e-invoicing/07_onboarding.md` delivered (A11 cluster: SV-EINV-FR-165..179, ~8 LBs, ~6 ACs, ~4 OQs); e-invoicing corpus 222 → **237 FRs**; total SV corpus **1,747**.
- Every dangling "(A11)" pointer resolves (9 e-invoicing anchors flipped to by-id pointers; 13 cml cluster refs verified resolvable); the W29 §5.1 inventory closes.
- COVERAGE: 26_ cited-as-LB; rollup **93/8/2/24 of 127 — gate green** (from the script). Registry unchanged (126 file rows, next=129).
- GO_LIVE_READINESS gate: **17 VERIFIED · 4 WATCH · 0 BLOCKER — green for planning**; shared-docs §4 SV register blocker note closed.
- Remaining program after W30: external watches (uif 403-WAF AML deadline 2026-10-17; D.O. gazette-feed stall; F-11 v19/v20 + F14 v17 manual; MOQ-05 endpoints; SOQ-46 negative watch; asamblea census negative watch), optional residual acquisitions, owner merge decisions.
