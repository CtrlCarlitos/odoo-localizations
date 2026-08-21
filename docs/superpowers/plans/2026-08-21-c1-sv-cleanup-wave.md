# C1 — SV Consolidation/Cleanup Wave Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Burn down the accumulated deferred-minor backlog (root `HANDOVER.md` §9 CAN-STAND + S7/S8/W17 RIDE lists + boilerplate sweep + COVERAGE regeneration script) without touching any requirement's substance.

**Architecture:** Mechanical-fidelity cleanup wave. Ten content tasks bundled by topic directory (fresh implementer + fresh reviewer per task, strictly sequential), one controller bookkeeping task. No new FRs, no renumbering, no restated sibling content — every edit is a wording/anchor/marker/infra fix already sanctioned by a recorded review verdict. The COVERAGE script is the only new code artifact.

**Tech Stack:** Markdown requirements files (Takumi contract), Python 3 stdlib script (`shared/scripts/build_coverage.py`), git worktree `.worktrees/sv` on branch `sv-research`.

**Spec:** root `HANDOVER.md` §9 (CAN-STAND list) + `sv/HANDOVER.md` §5 (S7/S8/S9/W17 wave-log ride entries) + §8.5 (deferred cleanups scope). The plan argues from those records; read them before executing.

## Global Constraints

- **Workspace:** ALL work in `.worktrees/sv` (branch `sv-research`). The main checkout is integration-only. Never force-push; remote refs fixed by delete + re-push (owner protocol).
- **Id immutability:** FR/LB/AC/OQ ids and per-file counts NEVER change. A cleanup edit must not renumber, insert, or delete any requirement row. The per-file totals in each `00_index.md` must remain true after every task (verify with grep counts before commit).
- **Quote fidelity:** verbatim Spanish quotes stay verbatim; `[sic]` rows untouched. If a fix would alter a verbatim quote, STOP — it is out of scope.
- **Cross-file discipline:** sibling content is cited BY FR ID, never restated. Several cleanup items exist precisely to enforce this (FR-213 dual-branch, frep/03 FR-092, frep/08 LB-005).
- **Verify-or-document protocol** (rides whose precise review notes died with the deleted SDD ledgers — S8 T1/T4/T6/T8 rides, W17 "enum style"/"FR-145 wording"): locate the described defect class in the named file; fix ONLY what is verifiable against file content or the evidence bank; otherwise record "not reproducible from surviving records" in the task report. NEVER guess-edit.
- **Evidence bank:** worktree-local `sv/.extractions/*.evidence.md` (+ `*.pdf.txt`, git-ignored). EVID ids are corpus-global.
- **Markdown hygiene:** match each file's existing wrap width (~76-80 cols) and table style. No emojis. No comment-only churn.
- **Commits:** per task, short imperative, e.g. `C1 T3: payroll S4 deferred minors + W17 rides`. No push until the wave closes (S9 protocol: push post-final-review).
- **Dispatch template (S8 ruling (c)):** one exemplar file max in the dispatch prompt; evidence read as grep + bounded line-ranges (`sed -n 'A,Bp'`) for the task's EVIDs only; no full-corpus dumps.

---

### Task 1: e-invoicing deferred minors (UUID tightening, AC-011 scope, OQ-005 fold)

**Files:**
- Modify: `sv/requirements/e-invoicing/01_document-types.md` (§4 field table, ~line 171)
- Modify: `sv/requirements/e-invoicing/02_transmission.md` (AC-011 ~line 251; §4 rows ~lines 170-173; FR-059 ~line 79)
- Modify: `sv/requirements/e-invoicing/06_api-protocol.md` (OQ-005 row ~line 296)

**Interfaces:**
- Consumes: `sv/sources/schemas/*.json` (52_ schema patterns for `codigoGeneracion`/`idEnvio`/`codigoLote`), `sv/requirements/e-invoicing/02_transmission.md` FR-053.
- Produces: none (leaf task).

- [ ] **Step 1 — UUID M-1 tightening.** Grep the 52_ schemas for the UUID field patterns:

```bash
grep -rn 'codigoGeneracion\|idEnvio\|codigoLote' sv/sources/schemas/ | head -20
grep -rni 'pattern' sv/sources/schemas/ | grep -i '0-9A-F\|a-f' | head -10
```

Expected: a regex pattern like `"^[0-9A-Fa-f]{8}-..."` or format `uuid`. If the schema pins uppercase hex, tighten the §4 field rows in `01_document-types.md:171` and `02_transmission.md:170,173` from `UUID v4 uppercase` to `UUID v4 — 36 chars, uppercase hexadecimal digits [0-9A-F], 8-4-4-4-12 hyphen groups (52_ schema)`. If the schema permits lowercase, instead write the schema's exact constraint and add nothing else. Do not touch FR prose beyond the §4 Notes cells; do not change the `Field(s)`/type columns.

- [ ] **Step 2 — AC-011 scope fix.** In `02_transmission.md`, replace the AC-011 body (line ~251) with:

```
- **AC-011:** Given the Odoo client codebase, when statically scanned, then no reference to `*.dtes.mh.gob.sv` API endpoints exists in client code paths outside SaaS configuration test fixtures — MH portal URLs (human documentation/validation pages, not API surfaces) are out of scope (FR-053).
```

Keep the FR-053 row (~line 198) as is (it only names AC-011).

- [ ] **Step 3 — OQ-005 work-log fold.** In `06_api-protocol.md`, compress the OQ-005 row body (line ~296) to:

```
| OQ-005 | S1-wave cross-file controller pass, executed and closed: `04_signing_delivery.md` OQ-001 → resolved via FR-021..024 here; stale A12 pointer filename corrected in `01_document-types.md`/`02_transmission.md`/`03_events.md`; `03_events.md` FR-090 reworded to orchestration; `04_signing_delivery.md` OQ-008 → resolved. | no | Controller | resolved |
```

(One row, no work-log detail beyond this summary; keep the id `OQ-005` and the resolved status.)

- [ ] **Step 4 — Verify invariants.**

```bash
grep -c 'SV-EINV-FR-\|SV-PROT-FR-\|SV-CAT-FR-' sv/requirements/e-invoicing/0*.md   # per-file FR counts unchanged
grep -n 'OQ-005' sv/requirements/e-invoicing/06_api-protocol.md                     # exactly one row
```

- [ ] **Step 5 — Commit.** `git add -A sv/requirements/e-invoicing/ && git commit -m "C1 T1: e-invoicing deferred minors (UUID M-1, AC-011 scope, OQ-005 fold)"`

---

### Task 2: fiscal-reporting S3 deferred minors + W17 frep rides

**Files:**
- Modify: `sv/requirements/fiscal-reporting/01_f07-declaration.md`, `02_f07-annexes-sales.md`, `03_f07-annexes-purchases.md`, `04_retention-event-annexes.md`, `06_f14-declaration-annex.md`, `08_filing-calendar.md`, `00_index.md`

**Interfaces:**
- Consumes: EV bank (`sv/.extractions/*f07*`, `*F14*`, `30_Calendario*`) for EVID-178/174 anchors; `sv/requirements/taxation/04_isr-withholding.md` (by-id cite targets).
- Produces: none.

S3 minors (root HANDOVER §9), each with the verify-or-document protocol:

- [ ] **Step 1 — 01 FR-005:** add the missing `EVID-178` to the FR-005 trailing anchor (locate the FR; append `; EVID-178` in its citation tail, matching sibling FR anchor style).
- [ ] **Step 2 — 01 FR-023:** inspect the else-branch; if its phrasing drops the subject or compresses two outcomes into one clause, rewrite the else clause so Given/When/Then map 1:1 to the two states. Minimal edit only.
- [ ] **Step 3 — 01 §4 sign-header:** locate the sign/sello header row in §4; fix wording so it names the field it describes (selloRecibido vs firma) unambiguously.
- [ ] **Step 4 — 01 Art. 66 attribution:** find the gloss citing "Art. 66" loosely; tighten to name instrument + article as printed (e.g. "Ley IVA Art. 66" vs a Rgto. gloss) per the LB it rides.
- [ ] **Step 5 — 02 FR-064:** decompress the compressed inventory enumeration (the FR inventories annex/doc types in a run-on); split into the same enumeration shape sibling FRs use.
- [ ] **Step 6 — 02 §5 FR-048 row:** the §5 row referencing FR-048 lacks the P-formula pointer its siblings carry; add the pointer in the sibling format.
- [ ] **Step 7 — 03 AC-005:** the code-8 dedup parity rule rides AC-005 without an OQ or an LB anchor; add an OQ row (next free per-file OQ id — verify with grep) OR an LB-anchor note in the AC, whichever matches file convention. This is the ONLY task in the wave allowed to append a row (an OQ); it must not renumber anything.
- [ ] **Step 8 — 03 FR-071:** add `EVID-174` to its anchor tail.
- [ ] **Step 9 — 03 FR-092:** the FR glosses 01's upload rules — replace the restated rules with a by-id cite to the owning FRs in `01_f07-declaration.md` (keep one clause of context).
- [ ] **Step 10 — 04 + 06 Given/then style:** normalize AC Given/When/Then phrasing to the file-family style (04 and 06 flagged); align commas/dashes only.
- [ ] **Step 11 — 06 FR-162 antecedent + FR-168 gloss:** fix FR-162's dangling antecedent; in FR-168 replace the FR-106 restating gloss with a by-id cite.
- [ ] **Step 12 — 08 LB-005:** the LB gloss restates consumer values (verified correct) — replace the restated values with the consumer FR ids, keeping the verbatim quote column untouched.
- [ ] **Step 13 — 00_index §7 pointer wording:** fix the §7 pointer wording flagged by the S3 final review (locate §7; make pointers name their target files unambiguously).
- [ ] **Step 14 — W17 ride: 01 enum style.** In `01_f07-declaration.md` §4, the FR-213/214 row uses `value_a · value_b` enum notation; compare against the file's other enum rows (e.g. line ~466 upload.error row) and the dominant convention across `02`/`03`; align if inconsistent, else document.
- [ ] **Step 15 — W17 ride: FR-213 dual-branch quote.** FR-213 (~lines 377-393) restates BOTH CT 103 branches with full Spanish quotes. The verbatim matrix is owned by `taxation/16` LB-012. Keep the first branch's key phrase quoted; reduce the second branch's quote to its operative key phrase (`lugar al pago original o complementario del impuesto`) with gloss, and add `verbatim matrix: taxation/16 LB-012` to the anchor tail. Do NOT touch the §4 enum row or FR-214.
- [ ] **Step 16 — Verify invariants:** per-file FR counts unchanged (`grep -c 'SV-FREP-FR-' each file`); only the Task-2 Step-7 OQ row was added.
- [ ] **Step 17 — Commit.** `git commit -m "C1 T2: fiscal-reporting S3 minors + W17 rides (FR-213 by-id, enum style)"`

---

### Task 3: payroll S4 deferred minors + W17 rides

**Files:**
- Modify: `sv/requirements/payroll/01_salary-model.md`, `02_minimum-wage.md` (+ `smm_2025.csv` notes if the CSV carries a provenance header), `03_working-time-surcharges.md`, `04_statutory-benefits.md`, `05_social-security-contributions.md` (+ `ss_contributions.csv`), `06_ss-declaration-remittance.md`, `07_contracts-termination.md`, `08_isr-interfaces.md`

**Interfaces:**
- Consumes: `sv/requirements/taxation/04_isr-withholding.md` (by-id cites), EV bank payroll files.
- Produces: none.

S4 minors (root HANDOVER §9), verify-or-document each:

- [ ] **Step 1 — 06 AC-001 placeholder composition:** change "weekend pair + two asuetos" to "two weekend pairs" (verify against CT asueto/pago de salario rules in the EV bank first — the S4 reviewer verified the correct composition is two weekend pairs).
- [ ] **Step 2 — 01 (T1 rides):** (a) remove the 2×SMM restatement in the ISR cell — replace with a by-id cite to the owning taxation FR; (b) the unanchored Art. 174/183/199 navigational mentions — either anchor each to its LB row or mark `(navigational)` per file convention.
- [ ] **Step 3 — 02 CSV (T2 ride):** add row-level EVID provenance to `smm_2025.csv` (a `evid` column or a provenance note row — match `withholding_tables.csv` conventions in taxation).
- [ ] **Step 4 — 03 FR-029 (T3 ride):** decompress the two-resolution compression; keep both resolutions as distinct clauses; mark navigational glosses `(navigational)`.
- [ ] **Step 5 — 05 (T5 rides):** voluntary-ISSS 10.50 regime-dependence — add the regime-dependence note if absent (CSV note may already cover; then document); `art99` valid_from caveat — add the caveat note to the LB row; LB-009 gloss-kin — align gloss phrasing with the LB verbatim column.
- [ ] **Step 6 — 06 (T6 rides):** FR-089 kin phrasing fix; LB-004 page-pin — add the exact page anchor to the LB location cell.
- [ ] **Step 7 — 07 (T7 rides):** LB-018 chamber attribution fix; FR-107 floor-exclusion inference — mark the inference as inference (or OQ it per convention); AC-002 boundary convention note.
- [ ] **Step 8 — 08 (T8 rides):** FR-123 `min()` arithmetic bend — add the in-mandate note (P9 ruling) if absent; casillas 718-720/738 silence — add the evidence-faithful silence note.
- [ ] **Step 9 — 08 (T9 ride):** taxation-pointer placement — move/consolidate the pointer so it sits with the file's other cross-file pointers.
- [ ] **Step 10 — W17 ride: FR-145 wording.** Inspect FR-145 (08, ~line 442) for wording defects (dangling clauses, restated sibling layout); fix minimally. If no defect is verifiable, document.
- [ ] **Step 11 — W17 ride: LB-017 no-consumer marker.** Payroll/08 LB-017 (Art. 97-98 awareness row, ~line 128) — ensure it carries the standard awareness-row marker used elsewhere in the corpus for no-consumer LB rows (grep `awareness` across `sv/requirements/**` for the convention; align wording, keep all citations).
- [ ] **Step 12 — Verify invariants:** per-file FR counts unchanged (`grep -c 'SV-PAY-FR-'`); 147 total.
- [ ] **Step 13 — Commit.** `git commit -m "C1 T3: payroll S4 minors + W17 rides (FR-145, LB-017 marker)"`

---

### Task 4: commercial-legal S5 deferred minors

**Files:**
- Modify: `sv/requirements/commercial-legal/01_merchant-registration.md`, `03_financial-statements.md`, `04_society-types.md`, `06_commercial-agents.md`, `08_payment-instruments.md`, `09_secured-transactions.md`, `10_*.md` (per-file name via `ls`), `00_index.md`, plus marker-vocabulary normalization across all 10 files.

**Interfaces:**
- Consumes: master index (`sv/.extractions/00_MASTER_INDEX.md`) cluster A11 ("Onboarding/authorization").
- Produces: none.

S5 minors (root HANDOVER §9 "can-ride" list), verify-or-document each:

- [ ] **Step 1 — 09:75 id line-wrap:** find the line where `SV-CML-FR-162` is wrapped mid-id (grep `FR-16$` / `FR-1$` artifacts); rewrap so the id is never split.
- [ ] **Step 2 — 03 page-pointer over-broads + §2 abbreviation overlap:** narrow page-pointer locators that span more than the cited content; deduplicate the §2 abbreviation definitions.
- [ ] **Step 3 — 04 Art. 121 final-sentence marker + Art. 149 parenthetical:** add the `[final sentence]` marker convention where the LB quote stops before the article's last sentence; handle the Art. 149 parenthetical skip with the file's `[…]` convention.
- [ ] **Step 4 — 06 EOF blanks:** strip trailing blank lines (file should end with a single newline).
- [ ] **Step 5 — 08 inner-quote normalizations ×5 + "626-787" over-bread:** normalize guillemet/quote nesting to the corpus convention; narrow the "626-787" page/article range to the actual cited span.
- [ ] **Step 6 — 10 FR-209 paren scar:** fix the unbalanced/stray parenthesis in FR-209.
- [ ] **Step 7 — 00_index 07-scope labels:** fix the file-07 row's scope label(s).
- [ ] **Step 8 — marker-vocabulary variance:** normalize §-marker vocabulary (e.g. `[sic]`, `(navigational)`, `awareness`) to the dominant corpus convention across the 10 files.
- [ ] **Step 9 — A11 cluster-pointer normalization:** `01_merchant-registration.md` ~line 344 references the "authorization cluster (A11)"; A11 exists in the master index — normalize the pointer to the master-index citation form used elsewhere in the corpus (grep other files for `master index` / `A11` forms; align).
- [ ] **Step 10 — Verify invariants:** per-file FR counts unchanged; 224 total.
- [ ] **Step 11 — Commit.** `git commit -m "C1 T4: commercial-legal S5 minors + A11 pointer normalization"`

---

### Task 5: special-regimes S7 ride — AC-007 Given-gap

**Files:**
- Modify: `sv/requirements/special-regimes/06_customs-declarations.md` (AC-007, ~line 681)

**Interfaces:**
- Consumes: FR-125 (same file, the $3,000 per-operator consolidation cap contract).
- Produces: none.

- [ ] **Step 1 — Fix the Given list.** AC-007's Then branch consumes `$1,800+$1,100 ($2,900)` but the Given enumerates `$150, $2,500, $1,800 and $1,500` — `$1,100` is not Given. Change the Given to:

```
- **AC-007:** Given courier shipments of FOB $150, $2,500, $1,800, $1,100 and
  $1,500, when routed, then the $150 shipment withdraws on guía aérea +
  factura, the $2,500 on its DM, the pair $1,800+$1,100 ($2,900)
  consolidates under the US$3,000 per-operator cap — and a $1,800+
  $1,500 ($3,300) consolidation is rejected naming the band breach
  (FR-125).
```

(Only the Given enumeration changes; then-branch text identical.)

- [ ] **Step 2 — Cross-check FR-125** (`grep -n 'FR-125' sv/requirements/special-regimes/06_customs-declarations.md`) to confirm the $3,000 cap and band semantics match the AC as amended. If FR-125 says otherwise, STOP and report — do not edit FR-125 in this wave.
- [ ] **Step 3 — Verify invariants:** FR count unchanged (175 total across dir); no other line touched.
- [ ] **Step 4 — Commit.** `git commit -m "C1 T5: special-regimes AC-007 Given-gap ($1,100 added to Given)"`

---

### Task 6: chart-of-accounts S8 rides + index cluster tags

**Files:**
- Modify: `sv/requirements/chart-of-accounts/01_framework-policies.md`, `04_nonfinancial-assets.md`, `06_revenue.md` (AC-001 ~line 670), `08_deferred-tax-adoption.md`, `00_index.md`

**Interfaces:**
- Consumes: EV bank `sv/.extractions/32_NIIF_PYMES_2025.evidence.md` (EVID-275..298; txt `sv/.extractions/32_*.pdf.txt` for PAGE anchors).
- Produces: none.

All four S8 rides are verify-or-document (ledger lost; names survive):

- [ ] **Step 1 — T1 ride (glosses ×2, 01):** scan `01_framework-policies.md` glosses (the English gloss column/parentheticals of §2 LB rows and FR bodies) for the two flagged gloss defects — gloss diverging from the verbatim quote, or gloss restating a sibling's rule. Fix the two clearest instances; document if fewer than two are verifiable.
- [ ] **Step 2 — T4 ride (locator nits ×3, 04):** audit `04_nonfinancial-assets.md` §2 LB location cells for wrong/missing txt PAGE anchors (compare against the EV bank's 32_ locators for the same EVID ids); fix the three clearest.
- [ ] **Step 3 — T6 ride (AC-001 self-containment, 06):** AC-001 (~line 670) references "guide-verified pattern, 32_ 23A.9-23A.13" and depends on the reader knowing the allocation; inline the allocation arithmetic into the Given so the AC stands alone (keep all ids/anchors).
- [ ] **Step 4 — T8 ride (A1 sentence-final period, 08):** find the sentence quoting Apéndice A A1 in `08_deferred-tax-adoption.md` (§3.7 FR-275 region and the LB-002 row) whose final punctuation is missing/misplaced; restore the sentence-final period without altering the verbatim quote characters.
- [ ] **Step 5 — Index N-tags:** in `00_index.md`'s "Files & FR ranges" table, append the master-index cluster tag to each file row's Scope cell: 01→`(N1)`, 02→`(N2)`, 03→`(N3)`, 04→`(N4)`, 05→`(N5)`, 06→`(N6)`, 07→`(N7)`, 08→`(N8)`. Minimal-diff edit (one insertion per row).
- [ ] **Step 6 — Verify invariants:** per-file FR counts unchanged; 276 total.
- [ ] **Step 7 — Commit.** `git commit -m "C1 T6: chart-of-accounts S8 rides + index N1-N8 tags"`

---

### Task 7: taxation W17 rides + S3 pointer + taxation boilerplate sweep

**Files:**
- Modify: `sv/requirements/taxation/16_ct-procedures.md` (FR-372 anchor tail ~line 394), `05_isr-distributions.md` (OQ-002 pointer), all taxation files carrying the "only architecture-split surface" claim (01-08, 15 per sweep grep).
- Consumes: `13_iva-retentions.md` SV-TAX-FR-303; `15_iva-declaration-interfaces.md`.

- [ ] **Step 1 — FR-372 trailing anchor map fold.** In `16_ct-procedures.md` (~line 394), replace the tail `(LB-016; LB-018; EVID-344; TAX 13/15-files by id)` with `(LB-016; LB-018; EVID-344; SV-TAX-FR-303 by id; 15_iva-declaration-interfaces.md by pointer)`. Nothing else in the FR changes.
- [ ] **Step 2 — 05 OQ-002 pointer phrasing.** Locate `taxation/05_isr-distributions.md` OQ-002's pointer whose phrasing says "F-910/F-915"; F-910 is marginally irrelevant there — narrow to the F-915 kin (or the precise form the pointer's target actually names). Minimal edit.
- [ ] **Step 3 — Boilerplate sweep (taxation dir).** Find every instance of the "only" claim, including line-wrapped ones:

```bash
grep -rn -B1 -A1 'architecture-split surface' sv/requirements/taxation/
```

For each instance still reading "the only architecture-split surface per `shared/docs/saas-thin-client-architecture.md` [D2])", soften to the canonical S3-fixed form (see `fiscal-reporting/01_f07-declaration.md:488-490`): `an architecture-split surface per \`shared/docs/saas-thin-client-architecture.md\`)` — drop `only` and the `D2` suffix, adjusting sentence case (`The only` → `An`). Preserve each file's wrap width; no other wording changes.
- [ ] **Step 4 — Verify:** `grep -rn 'only' sv/requirements/taxation/*.md | grep 'architecture-split'` returns nothing; FR counts unchanged (404 total; per-file counts match `00_index.md`).
- [ ] **Step 5 — Commit.** `git commit -m "C1 T7: taxation W17 rides (FR-372 anchor map) + boilerplate sweep"`

---

### Task 8: boilerplate sweep — non-taxation directories

**Files:**
- Modify: every file in `fiscal-reporting/` (except `01`, already softened), `payroll/`, `commercial-legal/`, `special-regimes/`, `chart-of-accounts/` still carrying the "only" claim (expect ~23 files; discover with the grep below).

**Interfaces:**
- Consumes: canonical softened form from `sv/requirements/fiscal-reporting/01_f07-declaration.md:488-490`.

- [ ] **Step 1 — Discover instances (wrapped lines included):**

```bash
for d in fiscal-reporting payroll commercial-legal special-regimes chart-of-accounts; do
  grep -rn -B1 'architecture-split surface' sv/requirements/$d/ ; done
```

- [ ] **Step 2 — Soften each:** same canonical replacement as Task 7 Step 3 (`the only … D2)` → `an …)`), preserving wrap and sentence flow. Files with the phrase but no `only` (already softened) are left untouched.
- [ ] **Step 3 — Verify:** `grep -rn 'only' sv/requirements/ | grep 'architecture-split'` returns nothing corpus-wide; `git diff --stat` shows only the expected files.
- [ ] **Step 4 — Commit.** `git commit -m "C1 T8: boilerplate sweep — soften architecture-split 'only' claims (non-taxation)"`

---

### Task 9: catalogs sidecar authority alignment (SV-CAT-FR-002)

**Files:**
- Modify: `sv/requirements/catalogs/README.md` (~line 6), `_INDEX.md` (generated — fix the GENERATOR, then regenerate), `shared/scripts/build_catalogs.py` (docstring + `--pdf` path + `_INDEX` template).
- Consumes: SV-CAT-FR-002 (`05_governance.md:48`) — workbook = sole parse source; gt/hn usage of the script.

- [ ] **Step 1 — Check other consumers:** `grep -rn 'build_catalogs\|--pdf' gt/ hn/ shared/ docs/ --include='*.md' | grep -v sv/`. If GT/HN still use `--pdf`, keep the flag with a docstring note "overlay retained for <cc>; SV bound by SV-CAT-FR-002 (workbook sole source)" and skip Step 2's removal.
- [ ] **Step 2 — Remove the overlay path** (if SV-only): delete `parse_pdf`, the `--pdf` arg handling, and the overlay merge block (~lines 104, 133-135, 150, 165-170); update the usage docstring to `build_catalogs.py <country> <catalogs_xlsx>`. Also update the `_INDEX.md` generation template so it no longer emits "(overlay: PDF text)".
- [ ] **Step 3 — Regenerate SV sidecars workbook-only and diff:**

```bash
~/.venvs/localizations/bin/python shared/scripts/build_catalogs.py sv sv/sources/51_Catalogos_Facturacion_Electronica_v1.1_2026-07.xlsx
git diff --stat sv/requirements/catalogs/
```

Expected: CSVs byte-identical (no diff); `_INDEX.md` wording updated. **If any CSV drifts** (e.g. a CAT-032-style workbook gap), revert the regeneration, restore the overlay code with the docstring note instead, and record the drift in the task report — do NOT ship changed CSVs in this wave.
- [ ] **Step 4 — Fix README.md line 6** to state the workbook is the sole parse source per SV-CAT-FR-002 (PDF = human-reference fallback).
- [ ] **Step 5 — Verify:** `grep -rn 'overlay' sv/requirements/catalogs/` returns only historical-context sentences if any; CSV diff clean.
- [ ] **Step 6 — Commit.** `git commit -m "C1 T9: catalogs workbook-sole-source alignment (SV-CAT-FR-002)"`

---

### Task 10: COVERAGE regeneration script

**Files:**
- Create: `shared/scripts/build_coverage.py`
- Create: `sv/requirements/COVERAGE_NOTES.md` (curated status overrides + note fragments migrated from the current matrix)
- Modify: `sv/requirements/COVERAGE.md` (matrix section regenerated between the `## Matrix` heading and EOF; header block hand-updated: Authors line → "Controller + `shared/scripts/build_coverage.py`")

**Interfaces:**
- Consumes: `sv/sources/README.md` registry table (File/Topic/Title columns), LB citation scan of `sv/requirements/{topic}/[0-9]*.md` + `catalogs/*.md`.
- Produces: `build_coverage.py --check` exit code (0 = no drift) — T11 and future wave-close gates consume it.

- [ ] **Step 1 — Write the script** (complete implementation; adjust only if the registry parse fails on a row — extend `SOURCE_RE`, never special-case a source):

```python
#!/usr/bin/env python3
"""Regenerate <country>/requirements/COVERAGE.md from the sources registry
and an LB-citation scan of the requirements corpus.

Curated content (status overrides + note fragments) lives in
<country>/requirements/COVERAGE_NOTES.md and is merged into the matrix.
Usage:
    build_coverage.py <country> [--check]
--check regenerates to memory and diffs against the committed matrix;
exit 1 with a unified diff on drift (wave-close gate).
"""
from __future__ import annotations
import sys, re, subprocess
from pathlib import Path

SOURCE_RE = re.compile(r"^\| `([^`]+\.(?:pdf|xlsx|xls|docx|zip))` \|")
LBROW_RE = re.compile(r"^\|\s*(?:\d+_)?LB-\d+")
TOPIC_FILE_RE = re.compile(r"^\d{2}_.*\.md$")

def parse_registry(registry: Path):
    rows = []
    for line in registry.read_text(encoding="utf-8").splitlines():
        m = SOURCE_RE.match(line)
        if m:
            rows.append(m.group(1))
    return rows

def parse_notes(notes: Path):
    overrides, fragments, section = {}, {}, None
    for line in notes.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("## "):
            section = s[3:].strip().lower()
        elif s.startswith("|") and not set(s) <= set("|- ~\t "):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 2 and cells[0] and not cells[0].startswith("Source"):
                if section and section.startswith("status"):
                    overrides[cells[0]] = cells[1]
                elif section and section.startswith("note"):
                    fragments[cells[0]] = cells[1]
    return overrides, fragments

def scan_citations(req_dir: Path):
    # {source: {topic_file_dir/file.md: lb_row_count}}
    hits = {}
    for topic in sorted(req_dir.iterdir()):
        if not topic.is_dir() or topic.name in {"catalogs"}:
            continue
        for f in sorted(topic.glob("*.md")):
            if not TOPIC_FILE_RE.match(f.name):
                continue
            for line in f.read_text(encoding="utf-8").splitlines():
                for src in re.findall(r"`sv/sources/([^`]+)`", line):
                    if LBROW_RE.match(line) or "`sv/sources/" in line and line.startswith("|") and "LB-" in line:
                        hits.setdefault(src, {}).setdefault(
                            f"{topic.name}/{f.name}", 0)
                        if LBROW_RE.match(line):
                            hits[src][f"{topic.name}/{f.name}"] += 1
    return hits

def build_matrix(sources, hits, overrides, fragments, req_dir: Path):
    lines = ["| Source | Status | Cited in / note |",
             "|--------|--------|-----------------|"]
    for src in sources:
        per_file = hits.get(src, {})
        cited = [f"`{k}` ({v} LB rows)" if v else f"`{k}`"
                 for k, v in sorted(per_file.items())]
        status = overrides.get(src, "cited-as-LB" if per_file else "pending")
        note = fragments.get(src, "")
        cell = "; ".join(cited)
        if note:
            cell = (cell + " — " + note) if cell else note
        lines.append(f"| {src} | {status} | {cell} |")
    # synthetic schemas row (kept from the hand-built matrix)
    lines.append("| schemas/ (dir) | cited-as-LB | direct JSON schema reads "
                 "(e-invoicing waves) — see `sv/sources/schemas/` |")
    return "\n".join(lines) + "\n"

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    country = sys.argv[1]
    check = "--check" in sys.argv
    root = Path(__file__).resolve().parent.parent
    req_dir = root / country / "requirements"
    cov = req_dir / "COVERAGE.md"
    sources = parse_registry(root / country / "sources" / "README.md")
    overrides, fragments = ({}, {})
    notes = req_dir / "COVERAGE_NOTES.md"
    if notes.exists():
        overrides, fragments = parse_notes(notes)
    matrix = build_matrix(sources, scan_citations(req_dir),
                          overrides, fragments, req_dir)
    text = cov.read_text(encoding="utf-8")
    marker = "## Matrix"
    idx = text.index(marker)
    head = text[:idx + len(marker)]
    new = head + "\n" + matrix
    if check:
        import difflib
        diff = list(difflib.unified_diff(
            text.splitlines(True), new.splitlines(True),
            fromfile="COVERAGE.md", tofile="regenerated"))
        if diff:
            sys.stdout.writelines(diff)
            sys.exit(1)
        print("COVERAGE.md: no drift")
        sys.exit(0)
    cov.write_text(new, encoding="utf-8")
    print(f"COVERAGE.md matrix regenerated ({len(sources)} sources)")

if __name__ == "__main__":
    main()
```

- [ ] **Step 2 — Migrate curated notes.** Create `sv/requirements/COVERAGE_NOTES.md`: under `## Status overrides` move every non-cited row's status + reason (N/A rows, superseded rows, pending rows); under `## Note fragments` move the per-source curated prose that must survive regeneration (vintage watches, survivor-set notes, flip records). Table format `| <file> | <text> |`. Split long existing cells into short fragments — the citing-file lists are now auto-generated and must NOT be duplicated in fragments.
- [ ] **Step 3 — Regenerate + reconcile:**

```bash
python3 shared/scripts/build_coverage.py sv
git diff sv/requirements/COVERAGE.md | head -100
python3 shared/scripts/build_coverage.py sv --check && echo GATE-OK
```

Reconcile until the regenerated matrix is truthful vs the hand-built one: every status flip or citing-file change the script produces must be either (a) a real drift the hand-matrix missed — keep the script's version and note it, or (b) a scan defect — fix the script (never hand-edit the matrix back without fixing the scanner). The rollup line in the header (counts by status) is updated by hand from the regenerated matrix.
- [ ] **Step 4 — Commit.** `git commit -m "C1 T10: build_coverage.py + COVERAGE_NOTES migration; regenerate matrix"`

---

### Task 11: controller bookkeeping (no subagent)

**Files:**
- Modify: `sv/HANDOVER.md`, root `HANDOVER.md`, `sv/EXTRACTION_PLAN.md`, `sv/README.md` (count phrasing check only)

- [ ] **Step 1 — sv/README count check:** verify the file-count phrasing matches the registry (73 files, numbering 01-75, gaps 21/23/24/28, next = 76); fix if stale (CAN-STAND nit).
- [ ] **Step 2 — HANDOVER rewrap ride:** rewrap the `sv/HANDOVER.md` §5 W17 entry to the file's wrap width (no text changes).
- [ ] **Step 3 — S9 RIDE record:** add one line to the W17/C1 area of `sv/HANDOVER.md`: S9 RIDE ledger unrecoverable (SDD workspace deleted; recorded verdict was "cosmetics; nothing load-bearing") — no action possible.
- [ ] **Step 4 — Prune root HANDOVER §9:** mark resolved every CAN-STAND item this wave burned down (strikethrough or `RESOLVED C1 (2026-08-21)` annotation, matching the file's existing resolution style — see the T3 wording item). Items intentionally left: D4 email-escalation (ToS backlog, not requirements), `06 OQ-006` renewal-procedure OQ (legitimately open), UUID M-1 if unverifiable.
- [ ] **Step 5 — Wave log:** add the C1 entry to `sv/EXTRACTION_PLAN.md` §Extraction log + `sv/HANDOVER.md` §5 wave log (scope, tasks, findings, unrecoverable-ride record, commit range).
- [ ] **Step 6 — Final review gate:** dispatch the whole-wave reviewer over `git diff main...sv-research` (read-only): verdict categories per conventions (MERGE-READY / USABLE-WITH-FIXES). Run ONE fix wave if needed. Then `git push origin sv-research`.
- [ ] **Step 7 — Session close:** update both HANDOVERs' §8/next-actions (acquisition follow-ups and go-live prep remain the owner's queued options), commit, push.

---

## Self-review record

- Spec coverage: root §9 CAN-STAND items 1 (T9), 3 (T1), 4 (T1), 5 (T7), 6 (T11), 7 (T7+T8), 8 S3 list (T2), 9 S4 list (T3), 10 S5 list (T4); sv HANDOVER S7 ride (T5), S8 rides + N-tags (T6), W17 rides (T2/T3/T5-adjacent/T7/T11), FR-372 parked residual (T7), boilerplate taxation candidates (T7), COVERAGE script (T10), HANDOVER rewrap (T11). S9 RIDE = unrecoverable, recorded (T11 Step 3). Not covered by design: D4 email-escalation, F-11/F-14 acquisitions, go-live prep (owner's other queued options).
- Placeholder scan: none — every step names files, ids, and the edit shape; rides without surviving detail carry the verify-or-document protocol instead of invented content.
- Interface consistency: T7/T8 share the canonical softened form (frep/01:488-490); T10's `--check` gate consumed by T11 Step 6; no FR id changes anywhere except the single allowed OQ append (T2 Step 7).
