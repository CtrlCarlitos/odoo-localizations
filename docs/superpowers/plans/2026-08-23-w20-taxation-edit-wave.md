# W20 — Taxation Edit Wave (SR8 rewire + 96_ Chapter V fold-in + 2025+ standing-rule mirror) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fold the three W19 follow-up debts into `sv/requirements/taxation/`: (a) the SR8 COTRANS rewire in taxation/09 (instrument 89_ now owned), (b) the 96_ Chapter V 30% foreign-agents levy as a NEW taxation file (SV-TAX-FR-405+), (c) the aguinaldo-vintage instrument mirror in taxation/04 (91_-94_ chain) — plus the pointer flips, index/COVERAGE regen, and wave bookkeeping.

**Architecture:** Edit wave per the standing synthesis conventions (sv/HANDOVER.md §9): controller prep (master index) → sequential per-task dispatches (fresh implementer + reviewer each, fix rounds, SDD ledger) → final whole-wave review → ONE fix wave → bookkeeping → push `sv-research`. Work happens ONLY in `.worktrees/sv` (branch `sv-research`). No new source acquisitions; registry UNCHANGED (numbering stays next=106).

**Tech Stack:** Markdown requirements files (Takumi contract: §1 scope, §2 Legal-basis LB table with verbatim Spanish + gloss + locator, §3 FRs, §4 data model, §5 Odoo mapping, §6 acceptance criteria, §7 OQ table), master index, COVERAGE regen script `shared/scripts/build_coverage.py`.

**Spec:** `sv/HANDOVER.md` §5 (W19 follow-up debts), §8.1(a)(b)(c); `sv/.extractions/00_MASTER_INDEX.md` (SOQ-41 row, cluster sections); `shared/docs/requirements-extraction-procedure.md`.

## Global Constraints (binding on every task)

- **Every FR cites an LB row** in its own file's §2 (by LB id), statutory verbatim quoted with `[sic]` markers where the print is defective (OCR quirks cleaned only where the EV header declares the cleaning discipline; "sin dedcción" in 96_ Art. 13 = quote WITH `[sic]`).
- **By-ID sibling consumption, never restatement:** sibling-topic/sibling-file mechanics are consumed by FR id (e.g. spe/01 `SV-SPE-FR-201`; taxation/16 sanction rows; taxation/04/13 tracks). R30(b): numbering continues the ONE `SV-TAX` prefix — new FRs start at **405** (no gaps, no renumbering).
- **D15 doctrine:** dated legal parameters = immutable dated rows resolved as-of the domain anchor date, snapshotted on the record; instrument provenance on every dated row.
- **Value-discipline:** config-gaps ship NO defaults, only OQs (AT forms, RAEX reglamento, RAES in-kind determinations, Art. 5 exclusion determinations).
- **Fiscal-value fidelity:** values enter as printed (30% rate; $0.10/gal; caps $1,100/$1,500) — never arithmetic-derived.
- **Corpus count discipline:** the ONLY FR additions this wave are taxation/17's contiguous block starting at 405. taxation/09 and taxation/04 are EDIT-ONLY (LB re-anchors, wording, OQ statuses — no FR/LB row count changes). spe/ edits are pointer/status flips only.
- **Commits:** short imperative, no emojis, one per task (+ plan commit + fix-wave commits). Push only at wave close (S9 ruling (c): push deferred to post-final-review).
- **Extraction txts are worktree-local** (`sv/.extractions/*.pdf.txt`) — implementers/reviewers read them there (S8 ruling (a)).
- **Dispatch template (S8 ruling (c), binding):** scoped evidence — the task's EVID ids as line-ranges, ONE exemplar file, on-demand txt via grep + bounded window. Harness exposes no per-subagent model parameter (S7 ruling (d)); Model-Selection framing only.
- **SDD ledger:** `.superpowers/sdd/2026-08-23-w20-taxation-edit-wave/` — per-task implementer reports, reviewer verdicts, fix rounds, rulings. Before ANY workspace deletion, preserve rulings into `sv/HANDOVER.md` §5 (W19 ruling (b), repo convention overrides silent deletion).
- **Reviewer gates:** every task gets a fresh reviewer vs the master index + the EV bank; fix rounds until Approved (0 Critical/Important). Controller commits died-mid-task COMPLETE work UNMODIFIED after structure verification (S7 ruling (a)) and re-dispatches zero-state deaths clean (S7 ruling (c)).

---

## Pre-loop prep (controller, before Task 1 dispatch)

- [ ] **P-1: Master index W20 prep** — in `sv/.extractions/00_MASTER_INDEX.md`:
  - Mint **Section W20-A — Taxation (special levy) topic cluster (synthesis worklist)** after Section S9-A, cluster **L1** (single cluster): covers 96_ D.L. 308-2025 Chapter V (Arts. 10-17): the 30% levy on mandante-financed transactions (incl. RAEX-determined in-kind imports), the two-limb Agentes de Retención Especial scope (SSF general limb + NPO-qualified catch-all limb), DGT enteros (10 first días hábiles), electronic reports (15 días hábiles), monthly domestic-donation self-entero, Art. 14 own-informe to DGII, CT 246/247/241 sanction routing + CT supletorio, Art. 16 MH/DGII/DGT administrative-instrument delegation, Art. 25 vigencia (7-jun-2025). Citation rule: LB cites 96_ as printed (EVID-396/397 anchors); siblings consumed BY ID (spe/01 FR-201; taxation/16 sanction rows; 04/13 track-separation invariants). FR numbering continues `SV-TAX` at 405 (R30(b)).
  - Append to the **SOQ-41** row (§C register, currently ends with the W19 T4 verdict): "**W20 (2026-08-23): the 96_ Chapter V taxation fold-in EXECUTED — SV-TAX-FR-405+ in `taxation/17_foreign-agents-levy.md` (cluster L1); spe/01 OQ-6 resolved-by-pointer. Residuals unchanged: D.L. 201-2025 + 411-2025 dated negatives stand; 96_ reglamento not acquired (config-gap).**"
  - Update the master index Build note (header) with a one-line W20 entry.
- [ ] **P-2: Commit plan + prep** — `git add docs/superpowers/plans/2026-08-23-w20-taxation-edit-wave.md sv/.extractions/00_MASTER_INDEX.md && git commit -m "W20 plan + master-index prep: L1 cluster, SOQ-41 W20 verdict"`.

---

## Task 1: NEW file taxation/17 — the 96_ Chapter V foreign-agents levy (SV-TAX-FR-405..416)

**Files:**
- Create: `sv/requirements/taxation/17_foreign-agents-levy.md`
- Modify (Task 4, not here): none. This task touches ONLY the new file.

**Interfaces:**
- Consumes (BY ID, never restated): `SV-SPE-FR-201` (spe/01 RAEX registration-state identity row); taxation/16 sanction rows (`SV-TAX-FR-380..382` kin — sanction base/reincidencia; CT catalog 226-262 is 05_-encoded, by pointer); taxation/04 ISR retention tables + taxation/13 IVA retention matrix (track-separation invariant only); 16's declaration-state/payments/prescription vocabulary (supletorio).
- Produces: `SV-TAX-FR-405..416` (12 FRs, contiguous from 405) — spe/01 FR-201/OQ-6, spe/00_index, taxation/00_index and COVERAGE flip to these ids in Task 4.

**Evidence inputs (scoped, per dispatch template):**
- EV bank: `sv/.extractions/95_96_97_SpecialIncentives.evidence.md` — EVID-396 (lines ~48-66: identity/scope/RAEX/obligations/vigencia) and EVID-397 (lines ~67-75: Chapter V verbatim + gloss) + the file OQ table (OQ-2 = this wave's routing root).
- Primary txt: `sv/.extractions/96_Ley_Agentes_Extranjeros_DL308_DO_2025-05-30_pp3-18.pdf.txt` — bounded windows: considerandos from line 10 (considerando IV = Ley ISR Art. 3 num. 4 no-prejudice); Art. 10 lines 296-304; Arts. 11-15 lines 305-419; Art. 16 (MH facultades) lines 420-429; Art. 17 + exclusiones clause lines 430-435; Art. 25 (vigencia, "ocho días después de su publicación", publication 30-may-2025 → 7-jun-2025) line 538.
- Exemplar (ONE): `sv/requirements/taxation/13_iva-retentions.md` — the retention-file shape (LB table style, FR density, track-separation precedent, AC/OQ registers).
- Cluster contract: master index Section W20-A / L1 (prep P-1).

**Required file structure (Takumi contract, same as all taxation files):** §1 scope summary (what the file owns / does NOT own); §2 LB table; §3 FRs (each cites LB ids); §4 data model; §5 Odoo mapping; §6 ACs; §7 OQ table.

**LB table (~10 rows, quote verbatim Spanish + gloss + locator `sv/sources/96_...pdf` + txt/EVID anchor):**
- LB-001 Art. 10 (hecho generador: mandante-financed transactions obligate the levy)
- LB-002 Art. 11 (30% on each transacción financiera/desembolso/transferencia/importación en especie/cualquier otro from mandante funds; in-kind = hecho generador when RAEX determines)
- LB-003 Art. 12 (collection by retención directly by financial-system institutions + any other intervening entity/mechanism/person)
- LB-004 Art. 13 first block (Agentes de Retención Especial: SSF-supervised institutions + reception/canalization/transfer interveners for funds desde el exterior a favor de organizaciones sin fines de lucro; enteros "sin dedcción [sic] alguna" a la Dirección General de Tesorería within 10 primeros días hábiles del mes siguiente; electronic report within 15)
- LB-005 Art. 13 donations ¶ (domestic donations: the Agentes Extranjeros themselves enter the 30% on gross donations, monthly periods, within 10 días hábiles after month close)
- LB-006 Art. 14 (retention-subject agents' own electronic informe — NIT + names + amounts + donations + enteros — to DGII within 15 primeros días hábiles)
- LB-007 Art. 15 (sanction routing: CT 246 non-retention/non-entero · CT 247 entero breaches · CT 241 reporting breaches)
- LB-008 Art. 16 (MH/DGII/DGT facultades to emit acuerdos/instructivos/circulares/resoluciones/guías for Chapter V application)
- LB-009 Art. 17 (CT supletorio + "Se aplicarán de igual forma … las exclusiones que se establezcan de conformidad con lo dispuesto en esta Ley")
- LB-010 Art. 25 + considerando IV (vigencia 8 días after publication → 7-jun-2025; levy "sin perjuicio" of Ley ISR Art. 3 num. 4)

**FR list (titles; implementer mints exact shall-statements, 405..416 contiguous):**
1. FR-405 levy establishment + dated 30% rate row (valid_from 2025-06-07, provenance 96_ Art. 11 + Art. 25) on every mandante-financed transaction to Agentes Extranjeros (LB-001/002/010)
2. FR-406 taxable-event breadth: in-kind imports = hecho generador only when RAEX so determines (config-dependent, no default); "cualquier otro" concepto catch-all as printed (LB-002)
3. FR-407 collection = retention at source by the Art. 12 institutions/entities; retention documentation surface = AT-provided forms (config-gap → OQ-2) (LB-003)
4. FR-408 two-limb agent scope: limb A SSF-supervised financial-system institutions (general); limb B any other reception/canalization/transfer intervenor, retaining ONLY funds desde el exterior a favor de organizaciones sin fines de lucro (the NPO qualifier rides limb B, never limb A) (LB-004)
5. FR-409 entero: full retained sum ("sin deducción alguna" — print "sin dedcción" [sic]) to la Dirección General de Tesorería within the 10 first días hábiles of the following month (LB-004)
6. FR-410 retained agents' electronic report of retained-upon Agentes Extranjeros within 15 first días hábiles of the following month (LB-004)
7. FR-411 monthly domestic-donation self-entero: 30% of gross donations received, per monthly period, within 10 días hábiles after the monthly close (LB-005)
8. FR-412 retention-subject agents' own electronic informe to DGII (NIT + names + amounts + donations + enteros) within 15 first días hábiles (LB-006)
9. FR-413 sanctions + supletorio: CT 246/247/241 routing consumed by id from the 05_-encoded CT catalog + 16's sanction-BASE rows; CT general law supletorio per Art. 17 → 16's declaration-state/payments/prescription vocabulary by id; the law's Art. 5 exclusion determinations apply to the chapter (config slots) (LB-007/009)
10. FR-414 subject-identification interface: RAEX registration state consumed from SV-SPE-FR-201 by id; MIGOB-side freeze/prohibitions informational only — no tax machinery duplicated (LB via EVID-396 pointer; spe/01 by id)
11. FR-415 ISR no-prejudice: the levy applies without prejudice to Ley ISR Art. 3 num. 4 (awareness row; levy and ISR obligations independent) (LB-010)
12. FR-416 track-separation invariant: this levy's retention/entero/report engine is a THIRD track, never merged with the ISR retention tables (taxation/04) nor the IVA retention matrix (taxation/13) — the 16-file ISR/IVA separation invariant extended (LB-001..009 as a chapter)

**§4 data model sketch:** `l10n_sv.special_levy.rate` (valid_from · rate · provenance — one row 2025-06-07/30%/96_ Art. 11); retention move-line fields (levy base, 30% computed, agent-limb select `ssf_general` / `npo_catchall`, RAEX determination flag for in-kind); entero register (period · amount · due-window 10-hábiles); report register (15-hábiles); donation self-entero monthly aggregate; all clocks computed on the días-hábiles engine consumed by id (SV-FREP-FR-202..204).

**§6 ACs (~9):** limb-scope gating (an SSF institution retains on a for-profit agent transaction; a non-SSF money-transfer entity retains ONLY on an NPO-destined exterior funds transfer); entero 10-hábiles deadline computed on the hábiles engine; donation monthly self-entero window; sanction routing resolves by id into the CT catalog; separation invariant (a levy retention never lands in the ISR or IVA retention ledgers); in-kind import triggers ONLY with a RAEX determination row present; [sic] fidelity checks in quotes; RAEX state read from the spe/01 field; ISR independence (levy posts do not alter ISR retention bases).

**§7 OQ table (4 rows, all open):**
- OQ-1 RAEX reglamento not acquired (formats/directrices config-gap; acquisition candidate ≥106)
- OQ-2 AT-provided forms (Arts. 13/14) absent — retention document + report formats ship NO defaults; Art. 16 delegation = the statutory root for the acquisition watch
- OQ-3 RAES in-kind import determination mechanics unknown (RAEX "cuando así lo determine" — config rows, no default enumeration)
- OQ-4 fiscal-reporting declaration surface unknown (no F-form/declaration instrument in corpus for the levy enteros/reports — future fiscal-reporting wave ride; pointer only)

**Steps:**
- [ ] **1.1** Dispatch implementer (scoped template: evidence inputs above, ONE exemplar, L1 cluster contract, global constraints). Verify: file exists, 12 FRs contiguous 405-416, 10 LB rows, ~9 ACs, 4 OQs, sections §1-§7 present.
- [ ] **1.2** Dispatch reviewer (fresh) vs master-index L1 + EV bank verbatim checks + by-id existence checks (grep every cited sibling id exists in its owning file). Fix rounds until Approved (0 Critical/Important).
- [ ] **1.3** Commit: `W20 T1: taxation/17 foreign-agents levy (SV-TAX-FR-405..416) — 96_ Chapter V fold-in, cluster L1`.

**Verification:**
```bash
rg -c "SV-TAX-FR-4(0[5-9]|1[0-6])" sv/requirements/taxation/17_foreign-agents-levy.md   # each id present
rg -n "sin dedcción" sv/requirements/taxation/17_foreign-agents-levy.md                 # [sic] fidelity present
rg -n "SV-SPE-FR-201|SV-TAX-FR-38[0-2]" sv/requirements/taxation/17_foreign-agents-levy.md  # by-id cites present
```

---

## Task 2: taxation/09 — SR8/COTRANS rewire (debt a)

**Files:**
- Modify: `sv/requirements/taxation/09_iva-base-rate.md` (~lines 79-80, 474-482, 530, 568, 662-663, 674)
- Modify: `sv/requirements/taxation/00_index.md` (file-09 scope cell only — NO count changes)

**Interfaces:**
- Consumes: 89_ instrument facts (D.L. 257-2021, $0.10/gal Art. 3, passenger-tariff identity, vigencia through 31-dic-2026 per the registry prorroga chain — texts not acquired) via spe/08 LB-011/SV-SPE-FR-174 by id; this file's own OQ-3 (resolved W19).
- Produces: FR-245 with an 89_-satisfiable activation gate; OQ-3 note updated "rewire landed W20". No FR/LB/OQ count changes (EDIT-ONLY).

**Prescribed edits (reviewer verifies each):**
- [ ] **2.1** Preamble (~line 79-80): "with COTRANS rows config-gated behind its absent instrument" → "with the COTRANS rows config-gated on the 89_ instrument (D.L. 257-2021, owned W18; vigencia through 31-dic-2026 per the registry prorroga chain)".
- [ ] **2.2** FR-245 (~474-482): label `[DESIGN — SOQ-40/SOQ-39]` → `[DESIGN — SOQ-40]`; body: "value-flagged print-anchor, instrument absent" → "instrument-anchored via 89_ (spe/08 LB-011 by id)"; final sentence "ACTIVATE only upon instrument acquisition (SOQ-39: zero shipped chain mechanics for COTRANS; …)" → "the chain/config rows ship ANCHORED to 89_ (activation satisfiable since W19; the C8 row activates inside the 89_ vigencia window, valid_from 23-dic-2021 through 31-dic-2026 per the registry prorroga chain — texts not acquired, spe/08 OQ-8 watch) while the never-in-base guard stays instrument-independent per FR-242". The DESIGN character of the chain mapping itself is UNCHANGED (OQ-2/SOQ-40 still open).
- [ ] **2.3** §4 row (~530): "design: C8 chain/config rows activate on instrument acquisition (SOQ-39; SR8 SV-SPE-FR-174 by id)" → "design: C8 chain/config rows anchored to 89_ (satisfiable since W19; SOQ-39 consumed; SR8 SV-SPE-FR-174 by id)".
- [ ] **2.4** §5 row (~568): "SOQ-39: activates on instrument acquisition" → "anchored to 89_ (SOQ-39 consumed W19)".
- [ ] **2.5** AC-017 (~662-663): "given COTRANS unconfigured (instrument absent), then no C8 chain rows activate while the never-in-base guard already covers the family (FR-245)" → "given COTRANS outside the 89_ vigencia window (or the C8 row disabled), then no C8 chain rows activate while the never-in-base guard already covers the family (FR-245)".
- [ ] **2.6** OQ-3 (~674): append to the resolved note: "**Rewire landed W20: FR-245/§4/§5/AC-017 now anchor to 89_ (vigencia window through 31-dic-2026).**" (status stays resolved).
- [ ] **2.7** `sv/requirements/taxation/00_index.md` file-09 scope cell: append "; COTRANS rows anchored to 89_ (W20 — SOQ-39 consumed, gate satisfiable)". No other index change here.
- [ ] **2.8** Reviewer (fresh): verify every edit vs 89_/spe/08 LB-011 + the OQ-3 W19 note; grep 09 for residual staleness: `rg -n "instrument absent|upon instrument acquisition|behind its absent" sv/requirements/taxation/09_iva-base-rate.md` → expect 0 hits (except quotes of repealed-era text if any — must be none here). Fix rounds to Approved.
- [ ] **2.9** Commit: `W20 T2: taxation/09 SR8 rewire — COTRANS rows anchored to 89_, FR-245 gate satisfiable`.

---

## Task 3: taxation/04 — aguinaldo-vintage instrument mirror (debt c)

**Files:**
- Modify: `sv/requirements/taxation/04_isr-withholding.md` (LB-021 ~line 104; §3.4 narrative ~354-355; FR-120 mapping row ~574; §3 note ~599; OQ-003 ~713)
- Modify: `sv/.extractions/00_MASTER_INDEX.md` (R22 row ~646; SOQ-05 row ~679 — append verdicts)

**Interfaces:**
- Consumes: the W19 T5 anchor chain — 91_ D.L. 229-2021 ($1,100, 2021) · 92_ D.L. 596-2022 ($1,500, 2022) · 93_ D.L. 900-2023 ($1,500, 2023) · 94_ D.L. 159-2024 ($1,500, 2024), each single-fiscal-year spent; EVID-398..401 + chain verification EVID-403; standing rule = Ley ISR Art. 4.16 (EVID-165). Payroll/04 LB-023 already carries this chain and defers the vintages interface HERE (SV-TAX-FR-120 owns split/vintages).
- Produces: OQ-003 → **resolved** (W20) with a standing annual re-check note; master-index R22/SOQ-05 appended verdicts. Values/FR behavior UNCHANGED (anchors only). No FR/LB/OQ count changes (EDIT-ONLY).

**Prescribed edits:**
- [ ] **3.1** LB-021 (~104): locator/provenance column → co-cite the four primary instruments `sv/sources/91_...pdf` + `92_...` + `93_...` + `94_...` (W19 T5 primary instruments of the vintage limb) + `54_...` (standing-rule text + consolidation-tail navigation co-cite) — MIRROR the payroll/04 LB-023 locator shape (that file's row is the template); gloss column: append "; vintages instrument-anchored since W19 T5 (EVID-398..401 + chain verification EVID-403)".
- [ ] **3.2** §3.4 vintage narrative (~354-355): after the vintage enumeration, add "(vintage limbs instrument-anchored to 91_-94_ since W19 T5; 2025+ standing row chain-verified — EVID-403)".
- [ ] **3.3** FR-120 mapping row (~574): reference cell append "; 91_-94_ instruments co-anchored W20 (EVID-398..401/403)".
- [ ] **3.4** §3 note (~599): "unindexed amounts in the current text (same class as 03-file OQ-003)" — leave; but the adjacent SOQ-05/OQ-003 assumption sentence (~599-600) gains "(verified: no 2025 transitory — EVID-403 chain verification + 54_ print 2025-04-30 tail; annual Diciembre-window re-check at encoding)".
- [ ] **3.5** OQ-003 (~713): status → `**resolved** (W20; EVID-403 + 91_-94_ anchored)`; question text append the verification basis + the standing note: annual Diciembre-transitory re-check rides the SMM/aguinaldo encoding pass (SOQ-05 kin).
- [ ] **3.6** Master index: R22 row (~646) verdict cell append "; 2025 leg instrument-verified W19/W20 (EVID-403; taxation/04 OQ-003 resolved)"; SOQ-05 row (~679) append "; W20: taxation-side mirror landed, OQ-003 resolved — annual Diciembre re-check at encoding".
- [ ] **3.7** Reviewer (fresh): verify LB-021 locator == payroll/04 LB-023 shape (no value drift: $1,100/$1,500/2-SMM unchanged); verify R22/SOQ-05 appends vs EVID-403; grep `rg -n "159-2024" sv/requirements/taxation/04_isr-withholding.md` shows the new instrument co-cites. Fix rounds to Approved.
- [ ] **3.8** Commit: `W20 T3: taxation/04 aguinaldo vintages mirrored to 91-94_ instruments; OQ-003 resolved`.

---

## Task 4: pointer flips + taxation/00_index + COVERAGE regen

**Files:**
- Modify: `sv/requirements/special-regimes/01_regime-framework.md` (FR-201 ~554-570; §4 row ~644; §5 row ~697; OQ-6 ~789)
- Modify: `sv/requirements/special-regimes/00_index.md` (file-01 row tail ~line 30; per-file OQ listing row ~line 100)
- Modify: `sv/.extractions/95_96_97_SpecialIncentives.evidence.md` (file OQ table: OQ-2 status annotate — append-only)
- Modify: `sv/requirements/taxation/00_index.md` (new 17 row; totals; numbering note; Status/Updated fields)
- Modify: `sv/requirements/COVERAGE.md` (script regen)

**Prescribed edits:**
- [ ] **4.1** spe/01 FR-201 body (~567-570): "The Chapter V 30% special levy … future taxation pass (OQ-6; no retention FRs here)" → point to the owning file by id: "the Chapter V 30% special levy = taxation-owned since W20 (`17_foreign-agents-levy.md`, SV-TAX-FR-405..416 by id; OQ-6 resolved-by-pointer)". Same flip in the §4 data-model row (~644: "Chapter V levy = out-of-wave pointer OQ-6" → "= taxation-owned (SV-TAX-FR-405..416 by id)") and the §5 mapping row (~697: "Chapter V 30% levy = out-of-wave pointer (OQ-6)" → by-id pointer).
- [ ] **4.2** spe/01 OQ-6 (~789): status → `**resolved-by-pointer** (W20: taxation/17 SV-TAX-FR-405..416 owns the retention engine)` — keep the descriptive text.
- [ ] **4.3** spe/00_index: file-01 row tail (~30) "96_ Chapter V = out-of-wave taxation pointer" phrasing (if the FR-201 gloss repeats it) → by-id pointer; per-file OQ listing (~100): `OQ-6 96_ Chapter V 30%-withholding surface = out-of-wave taxation pointer (W19 T4, EVID-397)` → append `— **resolved W20 via taxation/17 (SV-TAX-FR-405..416)**`.
- [ ] **4.4** EV file `95_96_97_SpecialIncentives.evidence.md` OQ table: append to OQ-2 status: "**RESOLVED-BY-POINTER W20: taxation/17_foreign-agents-levy.md (SV-TAX-FR-405..416) owns the Chapter V engine.**" (append-only; no text deletion).
- [ ] **4.5** taxation/00_index: add file-17 row to the Files & FR ranges table (scope: "96_ D.L. 308-2025 Chapter V foreign-agents special levy: 30% on mandante-financed transactions (RAES-determined in-kind), two-limb Agentes de Retención Especial scope (SSF general + NPO-qualified catch-all), DGT enteros 10 días hábiles, electronic reports 15, monthly donation self-entero, Art. 14 own-informe, CT 246/247/241 sanctions + supletorio, Art. 16 MH delegation — cluster L1"; FR range `SV-TAX-FR-405..416`; counts from T1's reviewed file); recompute the Total row (FRs 404→416+actual, LBs/ACs/OQs +17's counts); numbering note append "**405-416 = the W20 foreign-agents-levy fold-in (2026-08-23): file 17, one prefix per R30(b).**"; Status field → `draft (S2 + S9 + W17 CT fold-in + W19 identity notes + W20 levy fold-in, in review)`; Updated → `2026-08-23 (W20: file 17 + 09 rewire + 04 mirror)`.
- [ ] **4.6** COVERAGE regen: `python shared/scripts/build_coverage.py` (venv `~/.venvs/localizations`) from the worktree root, then `--check` gate must be green; inspect the 96_ row (expect cited — spe/01 + taxation/17 LB cites; pending-set count may drop only if the script re-keys 96_; any COVERAGE_NOTES rationale changes ride the script output — no manual row edits).
- [ ] **4.7** Reviewer (fresh): verify every flipped pointer's target id exists (`rg -n "SV-TAX-FR-405" sv/requirements/special-regimes/01_regime-framework.md` etc.); totals arithmetic (FR/LB/AC/OQ sums = per-file rows); COVERAGE gate output. Fix rounds to Approved.
- [ ] **4.8** Commit: `W20 T4: spe/EV pointer flips to taxation/17; taxation index + COVERAGE regen`.

---

## Task 5: wave bookkeeping (W19 T8 pattern)

**Files:**
- Modify: `sv/EXTRACTION_PLAN.md` (W20 wave-log entry, dated 2026-08-23)
- Modify: `sv/HANDOVER.md` (§1 corpus status line; §4 table taxation row 404→new count + totals 1,690→1,702; §5 wave-log summary entry + W20-process rulings; §7 SOQ highlights — 96_ Chapter V resolved-by-pointer, OQ-003 resolved; §8 next-actions refresh)
- Modify: `sv/.extractions/00_MASTER_INDEX.md` Build note (if not already current from P-1/T3/T4 edits — one-line W20 close)

**Steps:**
- [ ] **5.1** Write the W20 EXTRACTION_PLAN log entry (per-task record, commits, deltas: +12 FRs → corpus 1,702; COVERAGE verdict; deviations + rulings).
- [ ] **5.2** HANDOVER refresh: §1 (append W20 COMPLETE line with commit range + merge-pending marker); §4 taxation row `404` → `416` + FRs cell + Totals `1,690` → `1,702 FRs`; §5 wave-log summary W20 entry + a W20-process rulings block (preserved from the SDD ledger); §7 (SOQ-41 Chapter-V half consumed; spe OQ-6/taxation OQ-003 resolved); §8 item 1 (debts (a)(b)(c) executed; remaining: residual acquisitions + external watches + go-live prep).
- [ ] **5.3** Reviewer (fresh, read-only): consistency sweep — corpus totals vs `rg -c` per file, HANDOVER §4 numbers vs index totals, wave-log vs commit log, no stale "out-of-wave" phrasing left (`rg -n "out-of-wave" sv/requirements/ sv/HANDOVER.md` — every survivor must be a historical W19 record, not a live pointer).
- [ ] **5.4** Commit: `W20 T5: wave-close bookkeeping — EXTRACTION_PLAN log, HANDOVER refresh`.

---

## Final whole-wave review + fix wave + close (controller)

- [ ] **F-1** Dispatch final whole-wave reviewer (read-only): full diff `git diff <W19-merge>..HEAD` vs this plan + master index + EV bank; verdict MERGE-READY | USABLE-WITH-FIXES | NOT-USABLE. Mechanical checks: FR contiguity 405-416; corpus arithmetic 1,690+12; CSVs untouched ( taxation CSVs must be byte-identical); coverage gate green.
- [ ] **F-2** If USABLE-WITH-FIXES: ONE fix wave dispatch (prescribed edits from F-1) + re-verify. If MERGE-READY: proceed.
- [ ] **F-3** Preserve W20 rulings from the SDD ledger into sv/HANDOVER.md §5 (W19 ruling (b)) BEFORE any workspace cleanup; record the close.
- [ ] **F-4** Push: `git push origin sv-research`. Owner decides the §4.6 rebase-then-merge to main (thirty-eighth run).

## Self-review notes

- Spec coverage: debts (a) T2, (b) T1+T4, (c) T3 — all three §8.1 candidates covered; bookkeeping T5; prep P-1. No orphan requirements.
- Placeholder scan: all edits carry exact loci + prescribed replacement text shapes; FR list enumerated with anchors; OQ/AC registers enumerated.
- Type consistency: SV-TAX-FR-405..416 used consistently; spe/01 FR-201 id stable; counts recomputed in T4/T5 from the reviewed file (never hardcoded past T1).
