# W23 — cml Fold-in Wave (SAS statute + post-2008 CC reform set 109_-114_) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fold the W22 acquisitions (EVID-405..412) into `sv/requirements/commercial-legal/`: (a) the SAS statute (111_ D.L. 905-2023) as a full society-type profile — FR-044 statute_pending flip + SAS profile FRs + LB-032 retirement, (b) the 109_ D.L. 153-2021 acciones re-anchors (nominative-absolute regime), (c) the 111_ Arts. 4-8 fusión transnacional + Art. 358 foreign-domicile rows and the 109_ Art. 338 escheat re-anchor in cml/05, (d) the 110_ usura + 112_ cheque-truncation awareness notes in cml/08, (e) the SOQ-22 falsification verification-note flips across cml files, plus index/COVERAGE regen and wave bookkeeping. **107_/108_ (D.L. 201/411-2025) are OUT OF SCOPE** — they are the spe/taxation wave (§8.1(b)).

**Architecture:** Edit wave per the standing synthesis conventions (sv/HANDOVER.md §9): controller prep (master index citation-rule flip) → sequential per-task dispatches (fresh implementer + reviewer each, fix rounds, SDD ledger) → final whole-wave review → ONE fix wave → bookkeeping → push `sv-research`. Work happens ONLY in `.worktrees/sv` (branch `sv-research`). No new source acquisitions; registry UNCHANGED (numbering stays next=115).

**Tech Stack:** Markdown requirements files (Takumi contract: §1 scope, §2 Legal-basis LB table with verbatim Spanish + gloss + locator, §3 FRs, §4 data model, §5 Odoo mapping, §6 acceptance criteria, §7 OQ table), master index, COVERAGE regen script `shared/scripts/build_coverage.py`.

**Spec:** `sv/HANDOVER.md` §5 W22 wave log + §8.1(a) (the fold-in debt register); `sv/.extractions/00_MASTER_INDEX.md` (SOQ-22/SOQ-23 rows, S5-A citation rule, C-clusters); `sv/.extractions/109-114_Reformas_CodigoComercio.evidence.md` (EVID-407..412 + file OQ-1 routing); `shared/docs/requirements-extraction-procedure.md`.

## Global Constraints (binding on every task)

- **Every FR cites an LB row** in its own file's §2 (by LB id); statutory verbatim quoted with `[sic]` markers where the print is defective. The 111_ asamblea print is a CONSOLIDATED REPRINT (Art. 10 text already carries both gratuidad reforms — quote the terminal text and note the chain per 113_/114_ recitals); intra-word spacing artifacts cleaned only per the EV header discipline ("comerc io"→"comercio", "o stente"→"ostente", "305 -C"→"305-C"); the zero-glyph article prints as "**305-0** [sic, read 305-O]".
- **Routing corrections (W23 plan rulings, evidence-based — corpus greps over the HANDOVER/EVID-409 glosses):** (i) fusión transnacional + Art. 358 + Art. 338 escheat fold into **cml/05** (the file whose LB-005..LB-008/LB-018/LB-028 own Arts. 315-319/337-338/358) — the "cml/02/03" gloss in EVID-409/§8.1(a) is a mis-route, files 02/03 carry no fusión/foreign-society LBs; (ii) cml/08 gets ONLY the 960/960-A + 838-A..E awareness rows. Record both in the wave log at bookkeeping.
- **By-ID sibling consumption, never restatement:** society-type/profile mechanics live in cml/04; fusión/transformación/liquidation/foreign-society mechanics live in cml/05; SAS lifecycle exceptions (formulario-instead-of-escritura) are encoded ONCE in cml/05's rewrites with the SAS profile cross-referenced by FR id, and 305-Q/R (any society may transform/fuse into SAS; parent-SAS >90% absorption) encodes the SAS-eligibility rows in cml/04 §3.8 consuming 05's chassis by id. Matrícula machinery = SV-CML-FR-008/013/016/017 by id; book model = cml/02 FR-022/FR-025 by id; EF cycle = cml/03 by id; taxation distributions/earnings register = SV-TAX-FR-132..149 by id (the CT-124 duty row is the interface pointer ONLY — no tax mechanics restated).
- **Numbering (R30(b) kin):** new FRs continue the ONE `SV-CML` prefix contiguously from **225** (no gaps, no renumbering). Allocation: T1 = FR-225..240 (cml/04 §3.8 SAS profile), T2 = FR-241..242 (cml/04 acciones), T3 = FR-243..246 (cml/05). T4 mints NO FRs (awareness LBs only). In-place amendments to existing FRs (FR-042/044/066/068/077/078/079/086/097) keep their ids.
- **D15 doctrine:** dated legal parameters = immutable dated rows resolved as-of the domain anchor date; instrument provenance on every dated row. The SAS gratuidad window = dated rows (11-feb-2024→11-feb-2025 original; 31-dic-2025 limb 113_; terminal 31-dic-2026 limb 114_), post-2026 reversion = config watch. The $12,000 activo accounting-mode threshold (305-Z) is a D15-kin dated value with 111_ provenance — do NOT conflate with cml/02's Art. 437 keeper threshold (same figure, different instrument/rule).
- **Value-discipline:** config-gaps ship NO defaults (Ley de Competencia values in the reshaped Art. 319 checkpoint; CNR formulario current shape = the 111_ disposición transitoria gradual note; BCR 838-B norms ≤90 días not acquired). Interest/usura rates stay SOQ-26-governed (Tasa Máxima Legal = external BCR series, never shipped).
- **Awareness-only surfaces (no FR mechanics invented):** 110_ usura judicial nullity (960-A); 112_ truncation bank-participant duties + multas 100-1000 SMM (BCR/SSF-side); 109_ RUC-block enforcement + spent 1-year conversion transitorio. LB rows + gloss notes only.
- **Quote fidelity for stale 07_ prints:** the superseded Art. 134/155/315-319/337/338/358/960 texts stay in the corpus ONLY as historical provenance inside LB re-anchor notes (or are replaced in-row with the reformed text as the operative quote + the 07_ print noted as superseded); the reformed text is ALWAYS quoted from the reform instrument txt (109_/110_/111_/112_), verbatim.
- **Corpus count discipline:** the ONLY FR additions are the contiguous blocks 225..240 (T1), 241..242 (T2), 243..246 (T3) — 22 new FRs → corpus 1,724. cml/01/02/03/06/07/09 are ONE-PARAGRAPH edits (verification-note flips, no LB/FR/AC/OQ count changes). cml/08 = LB additions + notes + OQ-004 narrowing (no FR additions).
- **Commits:** short imperative, no emojis, one per task (+ plan/prep commit + fix-wave commits). Push only at wave close (S9 ruling (c)).
- **Extraction txts are worktree-local** (`sv/.extractions/*.pdf.txt`) — implementers/reviewers read them there (S8 ruling (a)).
- **Dispatch template (S8 ruling (c), binding):** scoped evidence — the task's EVID ids as line-ranges, ONE exemplar, on-demand txt via grep + bounded window. Harness exposes no per-subagent model parameter (S7 ruling (d)).
- **SDD ledger:** `.superpowers/sdd/2026-08-23-w23-cml-sas-foldin/` — per-task implementer reports, reviewer verdicts, fix rounds, rulings. Before ANY workspace deletion, preserve rulings into `sv/HANDOVER.md` §5 (W19 ruling (b)).
- **Reviewer gates:** every task gets a fresh reviewer vs the master index + the EV bank + the reform txts; fix rounds until Approved (0 Critical/Important). Controller commits died-mid-task COMPLETE work UNMODIFIED after structure verification (S7 ruling (a)); re-dispatches zero-state deaths clean (S7 ruling (c)).

---

## Pre-loop prep (controller, before Task 1 dispatch)

- [ ] **P-1: Master index W23 prep** — in `sv/.extractions/00_MASTER_INDEX.md`:
  - **S5-A citation rule flip** (the paragraph starting "Citation rule for synthesis: mercantile-registry and accounting LBs cite 07_ (D.L. 671 — post-2008 reforms verified-absent in TWO official copies…"): replace the parenthetical with "**07_ = consolidated base print, SOQ-22 FALSIFIED W22 (EVID-407..412): the post-2008 reform set 109_-114_ is OWNED — LBs citing articles in the reformed set (Arts. 17/18/134/153/155/158/164/212/219/315-319/337/338/358/960 + new 305-A..Z/838-A..E/960-A) cite the REFORM INSTRUMENT (109_/110_/111_/112_) as the operative LB, co-citing 07_ as the base print; article sets outside the reformed set keep citing 07_ (text stands current, W23 sweep)**". Keep the AML half of the rule unchanged; replace "society type menu may be incomplete without the SAS law (SOQ-23)" with "SAS = 111_ Chapter VIII-Bis (SOQ-23 resolved; W23 fold-in)".
  - **C4 cluster row** — append to Covers: "W23: SAS profile (111_ Capítulo VIII-Bis 305-A..Z + Art. 18-II-c; FR-225..242 — formulario constitution, S.A.S. suffix, $1 capital, free reserve, ≤180-day dividends, $12,000 accounting-mode threshold, auditor gate, gratuidad → 31-dic-2026) + 109_ acciones re-anchors (nominative-absolute)".
  - **C5 cluster row** — append to Covers: "W23: fusión transnacional (111_ Arts. 4-8 → CC 315/316/317/319/358; FR-243..246) + 109_ Art. 338 escheat → Fondo General del Estado (FR-086 re-anchor)".
  - **C8 cluster row** — append to Covers: "W23: 110_ usura 960/960-A + 112_ truncation 838-A..E awareness LBs (no FR mechanics)".
  - Header **Build note**: append one line " **W23 prep 2026-08-23:** S5-A citation rule flipped for the owned post-2008 reform set; C4/C5/C8 W23 scope annotations (fold-in wave per plan `docs/superpowers/plans/2026-08-23-w23-cml-sas-foldin.md`)."
- [ ] **P-2: Commit plan + prep** — `git add docs/superpowers/plans/2026-08-23-w23-cml-sas-foldin.md sv/.extractions/00_MASTER_INDEX.md && git commit -m "W23 plan + master-index prep: S5-A citation-rule flip, C4/C5/C8 annotations"`.

---

## Task 1: cml/04 §3.8 SAS profile (FR-044 flip + FR-225..240 + LB-032 retirement)

**Files:**
- Modify: `sv/requirements/commercial-legal/04_society-types.md` (§2 preamble + LB table + §3.1 + NEW §3.8 + §4 + §5 + §6 + §7). This task does NOT touch §3.7 (that is Task 2).

**Interfaces:**
- Consumes (BY ID): SV-CML-FR-008/013/016/017 (matrícula/registry-entry/presentation/publication machinery, cml/01); cml/02 book model (FR-022 legalization, FR-025 Art. 440 discipline, FR-028 retention row a); cml/03 FY-close/EF cycle; SV-TAX-FR-132..149 (distributions + earnings register — interface pointer only); SV-PAY-FR-011/022 (SMM units — NOT needed here, no SMM values in 111_).
- Produces: `SV-CML-FR-225..240` (16 FRs, contiguous) + the FR-044 in-place flip + new LB rows LB-033..LB-038 (approx.; renumber-free appends after LB-032). Task 2 builds on this file state; Tasks 3-6 cross-reference these ids.

**Evidence inputs (scoped, per dispatch template):**
- EV bank: `sv/.extractions/109-114_Reformas_CodigoComercio.evidence.md` — EVID-409 (the SAS statute: identity, verbatim spine, gloss, gratuidad chain) + EVID-411/EVID-412 (chain limbs) + file OQ-1 routing (whole file = 70 lines, read all).
- Primary txt: `sv/.extractions/111_Reforma_CodigoComercio_DL905_2023_Asamblea.pdf.txt` (722 lines) — bounded windows: header/D.O. lines 1-30; Art. 1 (new Art. 17 — sociedad by manifestación de UNA voluntad or acuerdo) lines 33-63; Art. 2 (new Art. 18 taxonomy + unipersonal exception) lines 64-97; Art. 3 Chapter VIII-Bis lines 98-530 (305-A 104-135 · 305-B 136-233 · 305-C 234-237 · 305-D 238-254 · 305-E 255-266 · 305-F 267-269 · 305-G 270-273 · 305-H 274-278 · 305-I 279-282 · 305-J 283-324 · 305-K 325-335 · 305-L 336-350 · 305-M 351-360 · 305-N 361-370 · 305-0 [O] 371-377 · 305-P 378-385 · 305-Q 386-406 · 305-R 407-413 · 305-S 414-421 · 305-T 422-434 · 305-U 435-467 · 305-V 468-474 · 305-W 475-487 · 305-X 488-497 · 305-Y 498-505 · 305-Z 506-530); Art. 10 gratuidad (consolidated terminal text) + vigencia Art. 11 lines 640-680 (grep `gratuidad\|GRATUIDAD\|Art. 10`).
- Chain txts (gratuidad provenance): `113_Reforma_DL905_CodigoComercio_DL203_2025_Asamblea.pdf.txt` + `114_Reforma_DL905_GratuidadSAS_DL468_2025_Asamblea.pdf.txt` (2 pp each, read whole).
- Exemplar (ONE): the file itself (cml/04 shape) + `sv/requirements/taxation/17_foreign-agents-levy.md` as the W20 new-block exemplar (LB-table + FR density + AC/OQ registers).

**§2 edits:**
- Flip the SOQ-22 verification paragraph (lines ~67-75) per the falsification (see Task 5 for the canonical replacement text — use the file-04 variant listing Arts. 17/18/134/155 as REFORMED-in-file).
- Replace the "SAS extensible design (SOQ-23, open)" paragraph (lines ~83-92) with the resolved statement: statute = 111_ D.L. 905-2023 (D.O. 234 T.441 13-dic-2023, vigencia 11-feb-2024), CC reform not separate law; LB-032 retired (see below); profile rows now statutory.
- **LB-032 retirement:** rewrite the row as historical (keep the id): mark "RETIRED W23 — superseded by LB-033..035 (111_ statutory rows); retained as the pre-statute provenance record (EVID-250 pointer)". Do NOT delete.
- New LB rows (append after LB-032, source `sv/sources/111_Reforma_CodigoComercio_DL905_2023_Asamblea.pdf`, locator = "111_ Art. N (txt PAGE n; EVID-409)"):
  - **LB-033** Art. 17 (new inciso 1: sociedad mercantile by manifestación de UNA voluntad or acuerdo of two+; personality/patrimony distinct) + Art. 18 as replaced (full taxonomy I.a-c personas incl. SRL under personas; II.a-c capitales incl. **c) SAS**; the two-socio minimum + SAS unipersonal exception).
  - **LB-034** Chapter VIII-Bis operative spine: 305-A (definition, mercantil nature always, responsibility limited to aportes, unipersonal, personality at Registro inscription, ALL acts via formularios, no escritura pública ever exigible, governance cascade pacto→capítulo→S.A. supletorio) + 305-B (denomination + "Sociedad por Acciones Simplificada"/"S.A.S." suffix; omission → administrators/representatives unlimited solidary liability; defaults: duración indeterminada, domicilio San Salvador Centro, finalidad any lawful activity, capital 100% suscrito, acciones múltiplos de un dólar, Firma Electrónica Certificada signing).
  - **LB-035** capital + reserves + listing: 305-D (capital from US$1, íntegramente suscrito at constitution; payment ≤2 años; means: efectivo, transferencia bancaria, billeteras electrónicas) + 305-E/F (classes/series; capital-variable regime adoptable) + 305-G (reserva legal FREE — "se regulará libremente") + 305-H (no Registro Público Bursátil inscription, no bolsa negotiation).
  - **LB-036** governance + minorities + exclusion + fraud: 305-J (junta/accionista-único defaults; meetings via any tech ensuring identification; books ≥1 actas-de-administración + contables, physical OR electronic) + 305-K (representación legal = ONE natural person, may be the único accionista) + 305-L/M (≥5% sesión/agenda; ≥10% designate 1/3 of ≥3-member junta) + 305-N (exclusión 3/4 of capital; reintegro ≥ valor contable) + 305-0 [O] (fraud → personal solidary liability).
  - **LB-037** auditor gate + dividends + dissolution/liquidation: 305-P (no auditor interno/externo/consejo while microempresario; obligation on exceeding → dictamen included in deposited EF) + 305-S (dividend rules free; once approved, payable ≤180 días from acuerdo) + 305-U (dissolution causes incl. falta total de pago del capital suscrito; partial-past-2-years → capital diminution unless below legal minimum) + 305-V..305-X (simplified dissolution/liquidation: no-pending-payments certified by contador público/auditor externo; liquidadores; 15 días hábiles post-inscription; reparto ≤30 días hábiles; "se tendrá por disuelta").
  - **LB-038** accounting + EF + gratuidad: 305-Z (comerciante-social obligations apply; activo < US$12,000 → contabilidad por sí mismos or appointees; ≥ US$12,000 → contadores públicos autorizados; EF suscribed by Representante Legal + contador público (auditor additionally when obligated); approved by Junta General or accionista único; deposited at Registro de Comercio VIA FORMULARIO with EF attached) + 305-Y (EF + informes de gestión approved by junta/único; actas físico o digital) + Art. 10 as consolidated (inscription of constitution formularios + first matrícula de empresa/local/sucursal/agencia = NO derechos o aranceles, terminal 31-dic-2026) + the chain provenance note (original 1-year from vigencia; 113_ D.L. 203-2025 → 31-dic-2025; 114_ D.L. 468-2025 → 31-dic-2026 CURRENT terminal, D.O. 226 T.449 28-nov-2025; 114_ cons. III = SAS "el tipo societario de mayor uso") + Art. 11 vigencia (60 days post-publication → 11-feb-2024) + disposición transitoria (Registro gradual formulario implementation).

**§3.1 edits (in-place amendments, ids unchanged):**
- **FR-042:** amend the taxonomy sentence — capitales class now = S.A. · comandita por acciones · **SAS (Art. 18-II-c per 111_)**; and the Art. 17 basis now reads "manifestación de una sola voluntad (SAS unipersonal) or contrato between two+ persons" (the two-person contrato sole basis is the superseded 07_ print; cite LB-033).
- **FR-044 full rewrite (flip):** statute_status `statute_pending` → `in_corpus`; the SAS profile fields are now REAL and populated per §3.8 (no more config-gap rendering); LB-032 → LB-033..038; SOQ-23 resolved.

**NEW §3.8 "SAS profile (Arts. 305-A..305-Z; Arts. 17-18)" — FR-225..240 (16 FRs; implementer mints exact shall-statements, each citing LB ids):**
1. **FR-225** constitution-by-FORMULARIO: all SAS social acts (constitución, modificación, transformación, disolución, liquidación) via Registro-de-Comercio formularios; escritura pública NEVER exigible; Firma Electrónica Certificada signing; personality ONLY at inscription (Art. 25 kin — FR-048 chassis consumed by id). (LB-034)
2. **FR-226** suffix "S.A.S." (or full form) immediately after the denominación; omission → administrators/representatives UNLIMITED SOLIDARY liability flag. (LB-034)
3. **FR-227** statutory defaults on constitution: duración indeterminada, domicilio San Salvador Centro, finalidad any lawful activity — overridable pacto fields with these as shipped default rows. (LB-034)
4. **FR-228** unipersonal constitution: sole accionista = natural person OR a capital society; declaración unilateral de voluntad; the Art. 18 two-socio minimum does not apply. (LB-033)
5. **FR-229** capital: minimum US$1 (dated value, 111_ provenance), íntegramente suscrito at constitution; unpaid balance ≤2 años; payment means incl. efectivo/transferencia bancaria/billeteras electrónicas recorded. (LB-035)
6. **FR-230** acciones múltiplos de un dólar + classes/series freedom + capital-variable regime adoptable (305-F mechanics chassis consumed from cml/05 FR-072 by id). (LB-035)
7. **FR-231** reserva legal FREE: no mandatory rate/limit — profile row = free/0 with the 305-G quote; NO Art. 39 restoration machinery applies (FR-054 chassis noted as inapplicable-by-statute). (LB-035)
8. **FR-232** no bolsa/Registro Bursátil: listing-blocked flag on SAS acciones (kin of FR-068 ledger; no market-listing states). (LB-035)
9. **FR-233** governance: junta functions → junta general or accionista único; administración → representante legal (one natural person, may be the único accionista; broad default powers); meetings via any tech ensuring attendee identification; cascade pacto → VIII-Bis → S.A. supletorio (S.A. profile rows FR-063..071 consumed as the fallback layer, never restated). (LB-034/036)
10. **FR-234** minority rights: ≥5% sesión/agenda; ≥10% designate 1/3 of a ≥3-member junta directiva. (LB-036)
11. **FR-235** exclusion of accionistas: pacto causales; 3/4-of-capital agreement; reintegro ≥ valor contable; 305-O fraud → personal solidary liability exposure flag. (LB-036)
12. **FR-236** auditor gate: NO auditor interno/externo/consejo de vigilancia while microempresario-classified; crossing the classification → appointment obligation + dictamen in deposited EF (classification source = external config slot, microempresario criteria NOT in corpus — config-gap, no default; OQ note). (LB-037)
13. **FR-237** dividends: rules free per pacto; once approved, payment deadline ≤180 días from the acuerdo date (clock on the distribution record; expiry = overdue flag). (LB-037)
14. **FR-238** accounting-mode threshold (D15-kin dated row): activo < US$12,000 → self-kept or appointee; ≥ US$12,000 → contadores públicos autorizados; EF signed Representante Legal + contador (+ auditor when obligated); approved by junta/único; deposited at Registro via FORMULARIO (cml/02 book model + cml/03 EF cycle consumed by id; NOT the Art. 437 keeper threshold — different instrument). (LB-038)
15. **FR-239** books: ≥1 actas-de-órganos-de-administración book + libros contables; physical OR electronic per 305-J (cml/02 legalization + Art. 440 discipline flags by id; electronic = first-class option, no 24-month gate — Art. 455 does not govern SAS statutory books per 305-J print; record the reading). (LB-036)
16. **FR-240** gratuidad window (dated rows): $0 constitution-formulario inscription + first matrícula (empresa/local/sucursal/agencia) — window rows 11-feb-2024→11-feb-2025 (111_ original), →31-dic-2025 (113_), →31-dic-2026 (114_ terminal, current); post-2026 reversion watch; fee surface consumed from cml/01 machinery by id. (LB-038)

**§4 Data Model additions (the SAS profile rows + formulario objects):** `l10n_sv_commerce.society.type` (sas row): statute_status=in_corpus, suffix_rule="S.A.S.", min_capital_usd=1 (dated), reserve_rate=free, auditor_required=conditional(microempresario), accounting_mode_threshold_usd=12000 (dated), constitution_channel=formulario, unipersonal=true, bolsa_blocked=true; new entity `l10n_sv_commerce.sas.formulario` (act_kind, e-signature ref, inscription state — kin of escritura but formulario-based); `l10n_sv_commerce.dividend.distribution` sas payment-deadline field (≤180 días); gratuidad window rows on the fee/matricula surface. Update the FR-044 row values.

**§5 Odoo Mapping:** update FR-042/FR-044 rows; add rows FR-225..240 (res.company + l10n_sv_commerce.* — all `odoo` layer; no saas rows); version-regime note: delete the "SAS statute-pending flag is a version-regime slot" sentence, replace with the gratuidad-window + $1/$12,000 dated-values note.

**§6 ACs:** REWRITE **AC-004** (sas chosen → record saves with statute_status=in_corpus, suffix/capital/reserve/dividend/auditor profile fields POPULATED, gratuidad window applied — no more config-gap rendering); ADD ~4 ACs: (a) SAS constitution via formulario without escritura → valid + personality pending-until-inscription; (b) capital $1 fully subscribed → passes; dividends agreement → 180-day deadline computed; (c) activo $11,999 vs $12,000 → accounting-mode switch + EF signature set changes; (d) gratuidad: constitution dated 2026 → $0 fee row; dated 2027-01-02 → reversion watch flag.

**§7 OQs:** flip OQ-001 → **resolved** (statute owned as 111_; status "resolved (W23)"; residual watch = CNR formulario current shape per the disposición transitoria — recorded in the LB-038 gloss, not a new OQ).

**Review gate:** fresh reviewer verifies vs EVID-409/411/412 + 111_/113_/114_ txts: verbatim fidelity (incl. the 305-0 [sic] and the consolidated-Art.-10 note), LB coverage of the chapter spine, FR contiguity 225..240, by-id discipline, no invented mechanics (microempresario criteria stay config-gap).

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W23 T1: cml/04 SAS profile fold-in — FR-044 flip, FR-225..240, LB-033..038, LB-032 retirement (111_ D.L. 905-2023)"`

---

## Task 2: cml/04 acciones re-anchors (109_ D.L. 153-2021) — FR-066/068 rewrites + FR-241..242

**Files:**
- Modify: `sv/requirements/commercial-legal/04_society-types.md` (§2 LB-026/LB-028 re-anchors + new LB-039; §3.7 FR-066/FR-068 rewrites + new FR-241..242; §4 entry_kind/title rows; §5 rows; §6 AC-002-kin additions; §7 no new OQs). Sequenced AFTER Task 1 (same file).

**Interfaces:**
- Consumes: Task 1's §2 preamble state; the share-ledger model (FR-068, `l10n_sv_commerce.share.register.entry`).
- Produces: `SV-CML-FR-241..242`; the re-anchored Art. 134/155 operative quotes (109_); the CT-124 tax-interface pointer consumed by taxation at the next taxation wave.

**Evidence inputs:**
- EV bank: EVID-407 (109_ full: verbatim of Arts. 1-8 + transitorio; staleness map; gloss).
- Primary txt: `sv/.extractions/109_Reforma_CodigoComercio_DL153_2021_Asamblea.pdf.txt` (219 lines — read whole; exact reform-text shapes: Art. 1 replaces ONLY Art. 134 inciso 1; Art. 8 derogates Art. 134 inciso 2, Art. 154 inciso final, Art. 155 romano IV, Art. 219 inciso 2, Art. 337 inciso 4; Art. 134 incisos 3-4 SURVIVE).
- 07_ txt contrast windows: `07_Codigo_Comercio.pdf.txt` Arts. 134/149/153/155/158/164 (txt PAGE 26-30).

**§2 edits:**
- **LB-026 re-anchor:** keep the 07_ historical print in a provenance note; the OPERATIVE quote becomes 109_ Art. 1: "Art. 134. Las acciones serán siempre nominativas." + the surviving incisos 3-4 (provisional titles ≤1 year + mandatory exchange + administrator liability) + the Art. 8 derogation of inciso 2 (bearer-conversion demand DEAD). Source column: `sv/sources/109_Reforma_CodigoComercio_DL153_2021_Asamblea.pdf` (co-cite 07_ as base print). Effective date: vigencia +8 días after D.O. 185 T.432 29-sep-2021 → **7-oct-2021** (per EVID-407 gloss).
- **LB-028 re-anchor:** Art. 155 inciso 1 parte primera as replaced by 109_ Art. 3 ("debidamente actualizado" registry of acciones nominativas) + romano IV (nominative→bearer conversions) DEROGATED (registry content = ordinals I-III, V-VIII) + the NEW final inciso: "Estas sociedades deberán dar cumplimiento a las obligaciones de informar sobre sus accionistas y sobre la distribución de dividendos o utilidades, según lo previsto en el Art. 124 del Código Tributario." Art. 149 title profile unchanged.
- **New LB-039** (109_ Arts. 2/4/5/6 + transitorio): Art. 153 "Los títulos deberán ser siempre nominativos." + Art. 158 inciso 2 (totally-paid nominative acciones traspasables WITHOUT society consent, even against express contrary pact) + Art. 164 (society considers accionista the registered titular) + Art. 212 (bonos de fundador nominativos; numeral IV replaced) + transitorio summary (1-year conversion window; bearer-dividend payers inform AT within 3 months; post-deadline DGII RUC-block + SSF-supervised-entity bar — historical/enforcement awareness).

**§3.7 edits:**
- **FR-066 rewrite:** acciones ALWAYS NOMINATIVE (absolute, no payment-state condition); bearer-conversion gate REMOVED entirely (the option ceases to exist — data model + UI); provisional-title ≤1-year exchange clock SURVIVES (incisos 3-4); cite LB-026 re-anchored.
- **FR-068 amend:** Art. 155 registry content = 7 kinds (numeral IV nominative_to_bearer gone); registry must be "debidamente actualizado" (currency duty); the CT-124 information duty hook added as the tax-interface pointer (by-id to SV-TAX-FR-132..149 zone, no restatement).
- **FR-241 (new):** nominative-title mechanics per 109_: titles always nominative (Art. 153); totally-paid acciones traspasable without society consent even contra pacto (Art. 158-II — the share-ledger traspaso flow carries NO consent gate); the REGISTERED titular is the accionista of record (Art. 164 — ledger = register of record, sharpened). (LB-039)
- **FR-242 (new):** CT-124 shareholder/dividend information-duty interface: capital societies' registro + dividend distributions feed the CT Art. 124 reporting duty (interface pointer to taxation; the duty's filing mechanics = taxation-owned); RUC-block + SSF bar + conversion transitorio = awareness gloss only (no Odoo enforcement mechanics). (LB-039 + LB-028 final inciso)

**§4 edits:** `share.register.entry.entry_kind` — retire the `nominative_to_bearer` value (migration note: value leaves the catalog; historical rows read-only per D15); `share.holding` — add no-consent-traspaso flag for paid acciones; `share.title` — nominative-only profile.

**§6:** ADD one AC: given a fully-paid acción traspaso recorded without society consent, then the ledger posts it (no consent gate exists); given any bearer-title creation attempt post-7-oct-2021, then blocked with the Art. 134 reason.

**Review gate:** reviewer verifies the Art. 134 inciso-survival split (incisos 3-4 alive), the 155 numeral-IV derogation, effective dating 7-oct-2021, and that no bearer machinery survives anywhere in §3.7/§4.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W23 T2: cml/04 acciones re-anchors — FR-066/068 rewrites, FR-241..242, LB-026/028/039 (109_ D.L. 153-2021)"`

---

## Task 3: cml/05 fusión transnacional + Art. 358 + escheat (111_ Arts. 4-8; 109_ Arts. 7-8) — FR-243..246 + amends

**Files:**
- Modify: `sv/requirements/commercial-legal/05_society-lifecycle.md` (§2 preamble flip + LB-005/006/008/018 annotations + new LB-031..LB-033; §3.2 FR-077/078/079 amends + new FR-243..245; §3.4 FR-086 amend; §3.6 FR-097 amend + FR-246; §4; §5; §6; §7 OQ-002 reshape).

**Interfaces:**
- Consumes: Task 1/2's cml/04 SAS profile ids (FR-225 formulario chassis; FR-228 unipersonal) by id; FR-017 publication engine; FR-048 personality regime; FR-013 registry-entry model.
- Produces: `SV-CML-FR-243..246`; re-anchored Arts. 315-319/337-338/358 operative quotes.

**Evidence inputs:**
- EV bank: EVID-409 (Arts. 4-8 verbatim + gloss) + EVID-407 (Art. 7/8: the Art. 338 replacement + Art. 337 inciso-4 derogation).
- Primary txts: `111_...txt` lines 531-650 (Arts. 4-8 exact texts: 315 +incisos 2-3; 316 +inciso final; 317 REPLACED wholesale — NOTE: the marginal-notes clause and the per-domicile clause are GONE from the new text; 319 REPLACED wholesale — SAS formulario exception, notary foreign-doc relation duty, SC comprobar-or-declarar, foreign-registration-cancellation duty + failure → personality persists; 358 inciso 1 replaced + incisos 4-5 added); `109_...txt` lines 93-105 (Art. 7: new Art. 338 — 3 días hábiles deposit, 5 years unclaimed → Fondo General del Estado, NO bearer limb) + lines 106-110 (Art. 8 derogations incl. Art. 337 inciso 4).
- 07_ txt contrast: Arts. 315-319 (PAGE 58-59), 337-338 (PAGE 62-63), 358-359 (PAGE 67-68).

**§2 edits:**
- Flip the SOQ-22 verification paragraph (file-05 variant: Arts. 315-319/337/338/358 REFORMED-in-file).
- **LB-005 annotate:** Art. 315 as printed + NEW incisos 2-3 per 111_ Art. 4 (cross-border fusión enablement); Art. 316 + final inciso (111_ Art. 5).
- **LB-006 re-anchor:** Art. 317 REPLACED by 111_ Art. 6 — new operative text: agreement per pacto social; inscription in the Registro de Comercio; publication of agreement + último balance; cross-border: ONLY the salvadoreñas inscribe. The old marginal-annotation + per-domicile clauses are superseded (historical note).
- **LB-008 re-anchor:** Art. 319 REPLACED by 111_ Art. 7 — designados draft pacto; approved per fusión-agreement requisites; escritura matriz EXCEPT SAS (formulario); testimonio inscribed, effects from inscription; cross-border notary duty (relate foreign-law compliance documentation); SAS-absorbente formulario route + suscriptor responsibility; SC approval/resolución comprobar OR declaration of non-requirement (notary/suscriptor administratively responsible for veracity); personality extinguished at inscription; SV-society-absorbed-into-foreign cancellation duty (foreign-authority documentation attached; registrar records the asiento data) + failure → personality + merchant obligations subsist.
- **LB-018 annotate:** Art. 337 inciso 4 (bearer-actions payment limb) DEROGATED (109_ Art. 8) — the summarized incisos 3-5 gloss drops the bearer limb; Art. 338 REPLACED by 109_ Art. 7 (3-días-hábiles bank deposit a la orden del accionista; 5 years unclaimed → **Fondo General del Estado** — the 07_ print's centro-de-beneficencia limb is superseded; no bearer limb).
- **New LB rows:** LB-031 (111_ Arts. 4-6: the 315/316/317 reform texts verbatim); LB-032 (111_ Art. 7: the new 319 verbatim); LB-033 (111_ Art. 8 + 109_ Arts. 7-8: the 358 replacement/additions + 338 replacement + derogation set). Sources: `sv/sources/111_...pdf` / `sv/sources/109_...pdf`.

**§3 edits:**
- **FR-077 amend:** agreement-registration limb per the NEW 317 (inscription in the Registro de Comercio; publication of agreement + last balance stands; marginal-notes duty dropped as superseded); cross-border split → FR-243.
- **FR-078:** Art. 318/320 untouched — STANDS (verify no 111_/109_ touch: none).
- **FR-079 rewrite:** per the new 319 — escritura matriz EXCEPT SAS (formulario instead; SAS profile FR-225 chassis by id); the Ley-de-Competencia checkpoint becomes the notary/suscriptor comprobar-or-declarar duty (registry-side state simplified); personality-extinguished-at-inscription stands; the foreign-absorption cancellation duty → FR-244.
- **FR-243 (new):** fusión transnacional enablement: SV societies may fuse with national or FOREIGN societies (315-II); governing-law split — each society's applicable legislation incl. its decision process, SV societies per this Code (315-III); resulting/incorporating salvadoreña → pacto governed by the CC, content/form per the national ordenamiento (316-final). (LB-031)
- **FR-244 (new):** cross-border mechanics: ONLY the salvadoreñas inscribe the fusión agreement (317-II); notary relates the foreign societies' home-law compliance documentation (319); SV societies incorporated into a foreign society (or new foreign-law society) MUST request cancellation of their Registro registration, attaching foreign-authorship proof of the foreign inscription; the registrar records the cancellation-as-fusión asiento (foreign registry number, razón social, forma jurídica); FAILURE to cancel → personality persists + merchant obligations subsist (state machine: absorbed-abroad-until-cancelled). (LB-031/032)
- **FR-245 (new):** foreign-society SV-domicile fixing (Art. 358 as reformed): acts of commerce permitted unless home law prohibits (inciso 1); the society fixing SV domicile CONSERVES its legal personality (continuity — no new personality) and presents for inscription the testimonio of the adecuación escritura matriz (salvadoreño notary) stating the clauses of the CC society class it assumes, requesting the domicile-fixing inscription (inciso 4); notary/suscriptor relates home-law compliance for the domicile change (inciso 5). (LB-033)
- **FR-086 amend (escheat):** Art. 338 limbs — deposit within 3 DÍAS HÁBILES of final-balance approval (clock via the días-hábiles engine); beneficiary of 5-year unclaimed sums = **Fondo General del Estado** (supersedes the charity limb); bearer-acción payment limbs DEAD (109_ Art. 8 + nominative-absolute regime FR-066 by id). (LB-018 re-anchored)
- **FR-097 amend:** add the 358-inciso-1 home-law-permission gate + the domicilio-fixing continuity/adecuación route (cross-ref FR-245); the sucursal limbs unchanged.

**§4/§5/§6:** `l10n_sv_commerce.fusion` — add cross-border fields (foreign_participant flag/refs, governing_law split, sv_inscription_only rule, cancellation_duty state); foreign.registration — domicile_fixing route + personality_continuity; FR rows for 243..246; ACs: (a) SV+foreign fusión → only the SV society's agreement inscribes; (b) absorbed-abroad SV society without cancellation request → personality-persists state; (c) unclaimed liquidation sum at 5 years → Fondo General del Estado payee (not charity); (d) SAS absorbente → formulario route (no escritura matriz).

**§7 OQ-002 reshape:** the Ley de Competencia thresholds remain un-acquired BUT the checkpoint is now the notary/suscriptor comprobar-or-declarar duty — keep open, reworded (values still config-gaps).

**Review gate:** reviewer verifies the 317/319 wholesale-replacement deltas (marginal-notes clause gone; SC-checkpoint re-shape), the 338 escheat flip, and FR-078's untouched status.

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W23 T3: cml/05 fusión transnacional + Art. 358 + Art. 338 escheat re-anchors — FR-243..246, FR-077/079/086/097 amends (111_ Arts. 4-8, 109_ Art. 7)"`

---

## Task 4: cml/08 usura + truncation awareness (110_/112_) — LB rows + OQ-004 narrowing, NO new FRs

**Files:**
- Modify: `sv/requirements/commercial-legal/08_payment-instruments.md` (§2 preamble flip + two awareness LB rows + §3.6 FR-158 note + §7 OQ-004 narrowing).

**Interfaces:** Consumes: none new. Produces: awareness LBs citing 110_/112_ (COVERAGE flip); no FRs.

**Evidence inputs:** EV bank EVID-408 (110_: Art. 960-III BCR consultation + 960-A nullity of the usurious-interest slice + Tasa Máxima Legal base at contract celebration) + EVID-410 (112_: 838-A..E truncation; image-presentation = physical presentation; BCR compensation administration; multas 100-1000 SMM comercio/servicios/industria; Ley de Procedimientos Administrativos governs; 90-day format substitution transitorio; vigencia 19-abr-2024). Txts: `110_...txt` + `112_...txt` (2 pp / 5 pp — read whole).

**Edits:**
- §2 preamble: SOQ-22 flip (file-08 variant: Art. 960 reformed-in-file + new 838-A..E).
- **LB row (awareness class, cite 110_):** Art. 960 inciso tercero as added (judge consults BCR to determine whether the effective rate exceeds the Ley Contra la Usura maxima) + Art. 960-A (usurious-interest obligations NULL DE PLENO DERECHO as to the usurious slice; judicial calculation bases on the Tasa Máxima Legal published and in force at contract celebration). Gloss: judicial-mechanics layer; NO Odoo posting surface; the Economía rate config (FR-158/SOQ-26) unchanged; Tasa Máxima Legal = BCR external series (never shipped).
- **LB row (awareness class, cite 112_):** Arts. 838-A..E as added: truncation procedure (physical exchange reduced/eliminated; electronic records incl. cheque image); presentation by images = physical presentation effects; BCR reglamenta y administra compensation (Consejo Directivo norms ≤90 días — Art. 7-b Ley de Mejora Regulatoria excluded); administrative infractions a)-l); multas 100-1000 SMM (SMM = 30 days of the comercio/servicios/industria ordinary-diurnal-day minimum); Ley de Procedimientos Administrativos governs; 90-day cheque-format substitution transitorio; vigencia 19-abr-2024. Gloss: bank-participant/BCR-side duties — informational for Odoo; the cml/08 CC clocks (Art. 995 prescription etc.) untouched.
- **FR-158 note (in-place, one sentence):** the Art. 960 base text cited is the pre-110_ print for the pactado/legal ladder limbs — the 110_ inciso tercero + 960-A nullity layer ride the awareness LB (no computation mechanics).
- **OQ-004 reword/narrow:** truncation NOW evidenced (112_ 838-A..E — awareness row; BCR norms ≤90 días + current interbank rules still un-acquired); electronic clearing beyond truncation still watch. Keep open, narrowed.

**Review gate:** reviewer verifies verbatim fidelity + that NO FR mechanics were invented (awareness-only discipline).

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W23 T4: cml/08 usura + cheque-truncation awareness LBs + OQ-004 narrowing (110_ D.L. 295-2022, 112_ D.L. 972-2024)"`

---

## Task 5: verification-note flips — cml/01/02/03/06/07/09 (one paragraph each)

**Files:**
- Modify: `sv/requirements/commercial-legal/01_merchant-registration.md`, `02_accounting-books.md`, `03_financial-statements.md`, `06_commercial-agents.md`, `07_empresa-mercantil-eirl.md`, `09_sales-contracts.md` — §2 SOQ-22 verification paragraph replacement ONLY (no other edits).

**Interfaces:** none. Produces: the corpus-wide C1-C9 flip (SOQ-22 falsification sweep).

**Canonical replacement text** (single paragraph replacing each file's "SOQ-22 verification (resolved-with-residual, W12 2026-08-18)" sentence — keep each file's surrounding sentences about txt provenance/reform ticks intact):

> **SOQ-22 verification (FALSIFIED-AND-RE-RESOLVED W22 2026-08-23; W23 sweep)**: the W12 verdict ("no post-2008 CC structural reform is evidenced in two official consolidations") is FALSIFIED — the asamblea por-anios census found the post-2008 reform set: 109_ D.L. 153-2021 (Arts. 134/153/155/158/164/212/219/337/338), 110_ D.L. 295-2022 (Art. 960-III + 960-A), 111_ D.L. 905-2023 (Arts. 17/18 + Capítulo VIII-Bis 305-A..Z + 315-319 + 358 + SAS gratuidad chain 113_/114_), 112_ D.L. 972-2024 (838-A..E) — EVID-407..412. NO article of this file's LB set is in the reformed set: the 07_ text quoted here STANDS CURRENT for this article range (W23 grep-verified). Census caveat rides the SOQ-22 residual (por-anios carries no cards for 2010/2012-2015; 2019 partial).

**Steps:** per file — locate the paragraph (grep `SOQ-22 verification`), replace the W12 sentence run (from "the second official copy 73_" through "rides every 07_ LB in this file") with the canonical text, verify no LB/FR/AC/OQ row touched. Commit once for all six files.

- [ ] Implement → [ ] Review (light gate: diff-only review) → [ ] Commit: `git commit -m "W23 T5: SOQ-22 falsification verification-note flips — cml/01/02/03/06/07/09 (no article-set overlap)"`

---

## Task 6: cml/00_index + master-index rollups + COVERAGE regen

**Files:**
- Modify: `sv/requirements/commercial-legal/00_index.md`; `sv/.extractions/00_MASTER_INDEX.md` (rollup lines); regenerate `sv/requirements/COVERAGE.md` via `shared/scripts/build_coverage.py sv` (gate: `python3 shared/scripts/build_coverage.py sv --check` → "no drift"); `sv/requirements/COVERAGE_NOTES.md` curated refresh for the flipped rows (W20 ruling (d) precedent — scanner half + stale-gloss reconciliation).

**Edits:**
- **00_index:** header note (07_ base + 109_-114_ reform instruments; SOQ-22 falsified; SOQ-23 resolved W23); 04 row FR range → `SV-CML-FR-042..071 + 225..242` + scope gloss (SAS profile + acciones re-anchors) + LB/AC/OQ recount; 05 row → `SV-CML-FR-072..097 + 243..246` + gloss (fusión transnacional + escheat + 358) + recount; 08 row gloss (usura/truncation awareness LBs) + LB recount; 01/02/03/06/07/09 rows LB counts unchanged (verify); Total row → FRs **246**, LBs/ACs/OQs recounted; numbering note → W23 tails (225-240/241-242 in 04; 243-246 in 05); OQ rollup — 04 OQ-001 resolved (35 → recount); ruling-notes section — SOQ-22 paragraph updated (falsified; per-file re-anchor map), add W23 note (routing corrections + SAS fold-in).
- **Master index:** S5-A section closing line (§798 kin) — W23 delivered annotation; §3 Build note — W23 fold-in line; SOQ-22 row — append the W23 sweep verdict (C1-C9 notes flipped; per-file re-anchors landed); SOQ-23 row — append "fold-in EXECUTED W23 (FR-044 flip + FR-225..240; OQ-001 resolved)".
- **COVERAGE:** regen — expected flips: 109_/110_/111_/112_/113_/114_ pending → cited-as-LB (citing files cml/04/05/08); rollup 81 cited / 20 pending → **87 cited / 14 pending** (107_/108_ stay pending — spe/taxation wave; verify with the script output); COVERAGE_NOTES: retire the W22 pending-set rationale for 109_-114_, add the 107_/108_ residual line.

**Review gate:** reviewer verifies counts mechanically (grep FR/LB/OQ counts per file vs index; contiguity 001..246; `build_coverage.py sv --check` green).

- [ ] Implement → [ ] Review → fix rounds to Approved → [ ] Commit: `git commit -m "W23 T6: cml index + master-index rollups + COVERAGE regen (109_-114_ cited; 87/14 pending)"`

---

## Final whole-wave review + ONE fix wave (controller)

- [ ] **F-1:** Dispatch a fresh whole-wave reviewer (read-only): all six task diffs vs the plan + EV bank + reform txts; verdict MERGE-READY / USABLE-WITH-FIXES; log to SDD ledger.
- [ ] **F-2:** If USABLE-WITH-FIXES: execute ONE fix wave addressing all Critical/Important findings (deferred minors triaged ride/ignore per house convention); re-verify; commit.
- [ ] **F-3:** Bookkeeping (Task 7): update `sv/HANDOVER.md` (§1 wave log entry + §3 EVID/registry state + §4 corpus table + §5 W23 log + §7 SOQ register + §8 next-actions) and `sv/EXTRACTION_PLAN.md` (W23 extraction-log entry); preserve W23 process rulings into HANDOVER §5 BEFORE any SDD workspace deletion (W19 ruling (b)); commit: `git commit -m "W23 close: HANDOVER + EXTRACTION_PLAN bookkeeping"`.
- [ ] **F-4:** Push `sv-research`. Merge to main = owner decision (rebase-then-merge per §8.6; never force-push).

## Expected end state

- cml corpus: 224 → **246 FRs** (FR-225..242 in 04; FR-243..246 in 05); total SV corpus **1,724**.
- SOQ-23 fully closed (statute + profile delivered); SOQ-22 falsification swept (C1-C9 notes flipped; re-anchors landed in 04/05/08); OQ-001 (cml/04) resolved; OQ-002 (cml/05) reshaped-open; OQ-004 (cml/08) narrowed-open.
- COVERAGE: 109_-114_ cited-as-LB; rollup 87/9/2/14 of 112 — gate green. Registry unchanged (next=115).
- Remaining program after W23: spe/taxation wave (107_/108_ surfaces + SOQ-40/OQ-2 rides), external watches, owner merge decisions.
