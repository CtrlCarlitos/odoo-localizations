# W26 — Rides + Hygiene Wave (deferred-minor consolidation) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (controller-direct mode — W21/W25 proportionate-scale precedent: ~20 pre-verified minor edits, no new FRs/LBs/sources). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute the accumulated deferred-minor ride ledger: the W23 cml minors, the W24 spe/taxation minors, the W25 spe/08 qualifier ride, the W19 straggler rides (verifiable subset), and the C1 §8.5 hygiene residuals (EV-bank nits, frep path fix, catalogs wipe-on-regen). **Zero FR additions, zero LB additions, zero registry changes, zero COVERAGE flips** — verified mechanically at close (`build_coverage.py sv --check`). This closes every open ride in sv/HANDOVER §8.1's residual list.

**Mode:** Controller-direct (no subagents; W21/W22/W25 precedent for proportionate scale). Every edit below was pre-verified against the evidence txts during prep (2026-08-24); line numbers are as-of prep and MUST be re-located by content grep at edit time.

**Spec:** sv/HANDOVER.md §5 (W19/W23/W24/W25 deferred-minor triages) + §8.1/§8.5 (residual rides + C1 first-picks); this plan's per-task evidence citations.

**Standing constraints:** quote fidelity (txt governs; `[sic]` = corpus-sanctioned in-quote editorial marker per C1 ruling (b)); by-id consumption unchanged; no rollup-prose hand-counts; commits short imperative; push at wave close only.

---

## Task 1 — cml rides (W23 deferred minors)

**Files:** `sv/requirements/commercial-legal/00_index.md`, `04_society-types.md`, `05_society-lifecycle.md`, `01_merchant-registration.md`, `02_accounting-books.md`, `03_financial-statements.md`, `06_commercial-agents.md`, `sv/.extractions/00_MASTER_INDEX.md`

- [ ] **T1-1 "225..246" range glosses → strict form "225..242 + 246"** (W23's own prescription: three descriptive surfaces attribute the whole tail range to cml/04, but 243..245 live in cml/05):
  - `00_index.md` 04-row (line ~40): `SV-CML-FR-042..071 + 225..246` → `SV-CML-FR-042..071 + 225..242 + 246` (the row's FR-count 49 stays correct: 30 + 18 + 1).
  - `00_index.md` numbering note (line ~54): `FR-225..246\nappended in \`04\`` → `FR-225..242 + FR-246\nappended in \`04\`` (the following sentence `FR-243..245 in\n\`05\`` already strict).
  - MASTER_INDEX C4 cluster row (line ~355): `FR-225..246 — formulario constitution` → `FR-225..242 + FR-246 — formulario constitution`.
  - MASTER_INDEX SOQ-23 row (line ~717): `the SAS profile FR-225..246 delivered (cml/04 §3.8)` → `the SAS profile FR-225..242 + FR-246 delivered (cml/04 §3.8)`.
  - MASTER_INDEX line ~801 (`SV-CML-FR-225..246 (SAS profile + acciones/fusión/escheat/domicilio…`) stays — corpus-level range across BOTH files is correct there.
- [ ] **T1-2 LB-034 [sic]** (cml/04:175, the 305-B IV quote): `una finalidad especifica se entenderá` → `una finalidad especifica [sic] se entenderá` — evidence: `111_` txt line 154 prints `finalidad especifica` (no accent).
- [ ] **T1-3 LB-018 paraphrase de-quote** (cml/05:166): the compressed gloss `the 07_-printed "acciones al portador: pago contra la entrega de los títulos" limb is DEAD` → de-quoted `the 07_-printed bearer-payment limb (acciones al portador → pago únicamente contra entrega de los títulos) is DEAD` — the quoted string was a compression, not verbatim (07_ txt PAGE 63 prints: "Cuando las acciones a ser liquidadas sean al portador, los pagos … únicamente se harán contra entrega de los títulos.").
- [ ] **T1-4 Art. 338 double-quote collapse** (cml/05): LB-018 and LB-033 both carry the FULL replaced-Art.-338 verbatim. Collapse in **LB-033** (line ~181): replace the two full Art. 338 verbatim paragraphs with a pointer+summary — `109_ Art. 7 (Art. 338 REPLACED — operative from 7-oct-2021; FULL VERBATIM at LB-018: 3-días-hábiles bank deposit a la orden del accionista + 5-year unclaimed escheat to the Fondo General del Estado) +` — keeping LB-033's 109_ Art. 8 derogatorias verbatim (short) and its existing gloss (already says "full operative reading at LB-018"). LB-018 keeps its copy (the mechanics owner).
- [ ] **T1-5 LB-039 transitorio numerals 3-4** (cml/04:180): extend the Art. 9 summary's post-deadline limb with the print's numerals 3 and 4 (after the SSF/RUC-block sentences, before the closing parenthesis): `; numeral 3 — surviving bearer portadores lose voto in juntas and utilidades/dividendos until the títulos are asentados as nominativos and informed to the AT; numeral 4 — unconverted bonos de fundador al portador are unusable by their poseedores for Arts. 210/211-II/213/215 purposes (awareness only)` — evidence: 109_ txt PAGE 3-4, Art. 9 numbered list.
- [ ] **T1-6 line-wrap** (the W23 "five files" ride, verified subset per C1 ruling (g)): rewrap prose (non-table) lines >80 chars to the files' ~72-76 convention — verified complete list: `01:66` (91), `01:113` (92), `02:225` (84), `03:75` (85), `03:324` (83), `06:92` (85). Post-edit grep proof: `awk 'length > 80 && !/^[|#]/ && NF' sv/requirements/commercial-legal/0[1-9]*.md` returns only pre-existing acceptable lines (04's bold label line 958 stays — single logical label).
- [ ] **T1-7 chapter-spine residual — RECORD ONLY** (no file edit): 305-C (accionista-not-employee), 305-I (proof-of-existence document), 305-T (arreglo directo/arbitraje) uncited by scoping — recorded in HANDOVER §8 at bookkeeping for the next 111_ touch.

## Task 2 — spe/taxation rides (W24 + W25 deferred minors)

**Files:** `sv/requirements/special-regimes/01_regime-framework.md`, `02_zf-exemption-schedules.md`, `08_fovial-cotrans.md`, `sv/requirements/taxation/01_isr-framework.md`, `03_isr-rates-gains.md`

- [ ] **T2-1 window_kind token reconcile** (W24 minor): canonical vocabulary = `fixed_15y_from_first_utilidades` · `event_bounded_recepcion` (97_) · `event_bounded_recepcion_within_vigencia` (108_) — the `6y` is a window_param, not a kind; `event_bounded` alone under-describes vs the sibling row:
  - spe/01:679: `event_bounded_recepcion_within_6y_vigencia (108_` → `event_bounded_recepcion_within_vigencia (108_`.
  - spe/02:690: `97_: event_bounded (anchor` → `97_: event_bounded_recepcion (anchor`.
  - spe/01:576 prose: `(the 97_ event_bounded_recepción kind` → ``(the 97_ `event_bounded_recepcion` kind`` (token in code form, no accent).
- [ ] **T2-2 spe/02 AC-015 whitespace**: lines 831-833 have 3-space continuation indents → normalize to the file's 2-space convention.
- [ ] **T2-3 FR-417 window-sketch tension** (taxation/01): FR-417 body (~line 157): `inside the per-contract event window (firma de contratos → recepción final / fin de la relación contractual con CEL; the vinculación and window inputs = SV-SPE-FR-204 by id, never restated here)` → `inside the TWO-LAYER 108_ window (per-contract event window — firma de contratos → recepción final / fin de la relación contractual con CEL — inside the decree-vigencia layer; the vinculación and window inputs = SV-SPE-FR-204 by id, never restated here)`; §5 mapping row (~489) sketch `inside the per-contract event window (SV-SPE-FR-204 by id)` → `inside the two-layer 108_ window (event layer inside decree vigencia — SV-SPE-FR-204 by id)`. Matches spe/02 LB/config "TWO layers … never collapsed" discipline.
- [ ] **T2-4 taxation/03 §5 stamp-name cells** (W24 minor): align §5 Field(s) cells to the §4 data-model vocabulary:
  - FR-418 row (~522): `isr_gain_track + aeropuerto_dl201_art29_1e stamp` → `isr_capital_gain_exoneration (+ aeropuerto_dl201_art29_1e)`.
  - FR-419 row (~523): `energia_dl411_art7 stamp + no_computation_form` → `isr_capital_gain_exoneration_window · no_computation_form (+ energia_dl411_art7)`.
  - Notes cells unchanged (already correct); §3 FR bodies and §4 rows unchanged (already correct).
- [ ] **T2-5 FR-189 chain provenance refresh** (W25 ride — 124_/125_/126_ now text-owned, EVID-413..415):
  - spe/08 FR-189 body (~379-399): `the earlier limbs are recital-pinned by 106_ considerando II; the 617/1000/307 texts themselves remain un-acquired — verification watch` → `the earlier limbs are now text-owned W25 (124_ = D.L. 307-2022 suspension; 125_ = D.L. 617-2022 → 30-abr-2024; 126_ = D.L. 1000-2024 → 31-ago-2025; EVID-413..415)`.
  - Same body, the 1000 limb: `**D.L. 1000-2024** (D.O. 77 T.443 25-abr-2024 — pinned W21 by 106_ cons. II recital) → 31-ago-2025` → `**D.L. 1000-2024** (D.O. 77 T.443 25-abr-2024 — text owned W25 as 126_) → 31-ago-2025`.
  - Same body, the 307 limb: `D.L. 307-2022 = a 3-month SUSPENSION interlude (2022 fuel-crisis measure) carried as a dated historical row` → append `(text owned W25 as 124_)`.
  - LB-012 gloss (~131): `(387 = owned text 106_ Art. 2; 617/1000 = recital-pinned by 106_ cons. II, texts un-acquired)` → `(387 = owned text 106_ Art. 2; 617/1000/307 = texts owned W25 as 125_/126_/124_, EVID-413..415 — with 617 = the Art. 17-A creator and 1000 its first reform)`.
  - LB-012 quote-side annotation: `(ambos recitados por 106_ considerando II)` → `(ambos textos propios W25: 125_/126_)`.
  - Config table row (~461): `D.L. 617-2022 → 30-abr-2024; D.L. 1000-2024 (D.O. 77 T.443 25-abr-2024, recital-pinned 106_ cons. II) → 31-ago-2025` → `D.L. 617-2022 (125_) → 30-abr-2024; D.L. 1000-2024 (126_; D.O. 77 T.443 25-abr-2024) → 31-ago-2025`.
  - LB-013 (106_'s own row) UNCHANGED — its cons. II description is what 106_ prints.
  - LB source columns UNCHANGED (89_/106_ remain the cited anchors; W25's deliberate pending-class choice for 115_-126_ stands) → no COVERAGE flip.

## Task 3 — W19 straggler rides (verifiable subset)

**Files:** `sv/requirements/special-regimes/04_customs-clocks.md`, `sv/requirements/chart-of-accounts/{01,02,03,04,05,07}_*.md`

- [ ] **T3-1 spe/04 OQ-1 stale gloss** (LESIA): row ~545 still says "LESIA … is NOT in the corpus though cited by 12_ Art. 26 … Acquisition candidate shared with 74_" — STALE since W18 (79_ acquired; SOQ-32 closed). Rewrite the row text to: `SOQ-32 carried — RESOLVED at sources level W18/W19: LESIA = 79_ (D.L. 551-2001, consolidated thru D.L. 588-2008 per its INDICE print; post-2008 traffic = watch). FR-066/068/072 stamp tribute-obligation states and pointers ONLY, zero sanction mechanics invented here; the sanction ladders and defraudación elements live in 07_obligations-reporting-sanctions.md (anchored to 79_).` Status cell `open` → `resolved (sources; mechanics homed in 07)`. Pointer lines 164/192/380/440 unchanged (they reference the OQ home, still valid as pointers).
- [ ] **T3-2 coa OQ rows stale "≥75" numbering** (6 rows: 01:602 OQ-1, 02:789 OQ-1, 03:901 OQ-3, 04:934 OQ-1, 05:905 OQ-3, 07:793 OQ-1): each ends `Acquisition candidate ≥75 (same instrument as commercial-legal/03 OQ-002).` → `Criteria-instrument hunt open (candidates Res. 175-2023 [derogated intermediate] / Res. 82-2024; authority chain 76_-78_ owned W18; registry numbering ≥127; same instrument as commercial-legal/03 OQ-002).` — aligns the OQ table rows with the W19-T6-refreshed per-file §2 notes (W24 ruling (d) lesson: legends don't propagate upward mechanically).
- [ ] **T3-3 rides verified moot/no-action (documented at bookkeeping):** "HANDOVER:645 AML phrasing" — the W19-era HANDOVER text no longer exists (multiple rewrites since; unrecoverable without the deleted SDD ledger — C1 ruling (g) class); "spe/08 historical misprint-notes" — verified PRESENT since W19 (LB-012's "registry's $200/$400 gloss is a misprint … OQ-7 note"; registry §89 corrected W19 T8); "payroll 05/08 trailing-newline" — verified CONSISTENT (all 9 payroll files end single `\n`, zero trailing spaces, zero triple-newlines) — non-reproducible, no action.

## Task 4 — hygiene (C1 §8.5 residuals + EV bank)

**Files:** `sv/requirements/fiscal-reporting/04_f07-annexes-retentions-events.md`, `sv/.extractions/32_NIIF_PYMES_2025.evidence.md`, `sv/requirements/chart-of-accounts/01_framework-policies.md`, `shared/scripts/build_catalogs.py`

- [ ] **T4-1 frep/04 truncated source path** (LB-009, line ~102): `sv/sources/63_F930v3.pdf` → `sv/sources/63_F930v3_informe_mensual_retIVA.pdf` (the registered filename; frep/07 already cites it correctly).
- [ ] **T4-2 EV-bank A1 estas→esas** (32_ evidence.md line 7, the Apéndice A1 effective-date quote): `"Una entidad aplicará estas modificaciones y revisiones a periodos anuales que comiencen a partir del **1 de enero de 2027**.` → `esas modificaciones` — the 32_ txt PAGE 315 prints `esas` (txt governs, W20 ruling (a); S9 ruling (g) EV-hygiene precedent). Requirements files checked: no downstream quote of this sentence exists (coa/01 LB rows quote other paragraphs — grep `aplicará estas` in requirements = 0).
- [ ] **T4-3 coa/01 LB-004 PAGE anchor** (line ~96): `(txt PAGE 46-53)` → `(txt PAGE 48-53)` — verified: Sección 3 heading + 3.3 on PAGE 48, 3.24 on PAGE 53, Sección 4 starts PAGE 54.
- [ ] **T4-4 catalogs _INDEX wipe-on-regen**: `shared/scripts/build_catalogs.py` — preserve hand-maintained trailing sections on regen: before writing `_INDEX.md`, read the existing file and carry over everything from the first `## Corrections log` heading to EOF verbatim (if present); append after the generated table. Add a one-line comment in the script. No behavior change otherwise; CSV output untouched.
- [ ] **T4-5 regen safety check**: after T4-4, run a dry sanity check on the script change (python -c compile + logic read-through; do NOT regen catalogs in this wave — the workbook txt parse path is untouched).

## Task 5 — bookkeeping & close

- [ ] **T5-1 COVERAGE gate:** `python3 shared/scripts/build_coverage.py sv --check` (workdir = repo root of the worktree) — expect NO drift (no LB source-column changes; frep/04 path fix resolves to the same 63_ instrument).
- [ ] **T5-2 grep proofs:** (a) `rg 'event_bounded_recepcion_within_6y|97_: event_bounded ' sv/requirements/` = 0; (b) `rg '225\.\.246' sv/requirements/commercial-legal sv/.extractions/00_MASTER_INDEX.md` = only the corpus-level MASTER:801 surface; (c) `rg 'recital-pinned by 106_ cons. II, texts un-acquired|recited por 106_|pinned W21 by 106_ cons. II' sv/requirements/` = 0; (d) `rg 'is NOT in the corpus' sv/requirements/special-regimes/04_customs-clocks.md` = 0; (e) `rg 'candidate ≥75' sv/requirements/chart-of-accounts/` = 0; (f) `rg '63_F930v3\.pdf' sv/requirements/` = 0; (g) `rg 'txt PAGE 46-53' sv/requirements/` = 0; (h) `rg 'aplicará estas modificaciones' sv/.extractions/32_NIIF_PYMES_2025.evidence.md` = 0.
- [ ] **T5-3 corpus-count invariants:** FR totals unchanged (1,730; cml 246, spe 204, taxation 421); LB/AC/OQ counts unchanged per file except: spe/04 OQ-1 open→resolved (index OQ legend recount if spe/00_index carries one — check and update), coa OQ rows stay `open` (SOQ-46 still open — only wording refreshed). Recount any per-file OQ legends touched.
- [ ] **T5-4 HANDOVER updates:** §1 W26 entry; §5 wave-log W26 entry (with the T3-3 moot/no-action documentation + T1-7 chapter-spine residual note); §8.1 residual list rewritten (rides EXECUTED; remaining = SOQ-46 hunt + external watches + census watch + go-live prep); §7 untouched (no SOQ status changes).
- [ ] **T5-5 EXTRACTION_PLAN.md** W26 wave-log entry.
- [ ] **T5-6 Commit + push** sv-research (commit per task group; push at close). Merge to main = owner decision (forty-seventh §4.6 run when directed).
