# HANDOVER — Session State & Continuation Guide

**For the next controller session.** Written 2026-08-17, updated 2026-08-18 (S3 close),
2026-08-18 twice more (W9/S4 closes), 2026-08-18 twice more again (W10+S5 prep, then W11 Quincena-25 package),
2026-08-18 once more (S6 Quincena-25 fold-in close), and 2026-08-18 twice more
(W12 AML-regime replacement + S5 commercial-legal synthesis close), and
2026-08-19 once more (§4.6 standard session-close & merge protocol). Read this
document fully before acting; it is the authoritative cross-session memory
(conversation context does not survive).
**Update it at every session boundary** — replace stale sections, append new
rulings, refresh "Next actions".

---

## 1. Project in one paragraph

`odoo-localizations` is a requirements-extraction workspace (NOT a code
repo) for Odoo localizations of El Salvador (sv), Guatemala (gt), Honduras
(hn). Source documents (laws, MH manuals, catalogs, JSON schemas) are
extracted to text, read end-to-end in evidence passes, then synthesized into
Takumi-contract requirements files (fixed 7-section template, FR/LB/AC/OQ
traceability). Takumi — the in-house AI agent platform for building Odoo
modules — and an Elixir/Phoenix SaaS team consume the requirements. Product
architecture (decided): **open-source LGPL-3 Odoo thin client + proprietary
SaaS core** (see decisions D1–D6 below). Target Odoo versions: 17–20.
**Method (owner 2026-08-20):** SV was the deliberate pilot — learn by
doing; it validated the approach and produced most of the shared canon.
The goal is to keep the extraction of requirements as UNIFORM as possible
across all localizations: `shared/docs/` + `shared/scripts/` are the
common base, expected to keep evolving as each country teaches us
something new; per-country drift (sources, formats, availability) is
expected and absorbed by instantiating the canon, never by forking it.

## 2. Authoritative documents (read order for a new session)

1. `sv/EXTRACTION_PLAN.md` — wave log, risks, reading order; the state of sv extraction
2. `shared/docs/saas-thin-client-architecture.md` — D1–D6 decision log (S0.5 socratic session output)
3. `shared/docs/requirements-extraction-procedure.md` — the method spine (pipeline, NotebookLM policy, evidence format)
4. `shared/docs/requirements-template.md` — 7-section format authority; Topic row now includes `catalogs`
5. `shared/docs/regulatory-change-management.md` — version-regime framing + **D7–D12 decision log (decided 2026-08-17)**
6. `shared/docs/odoo-localization-guide.md` — module anatomy (thin-client caveat) + **D13/D14 module-design decisions (journal/establishment models, 2026-08-18)**
7. `sv/.extractions/00_MASTER_INDEX.md` — synthesis lookup: topic clusters (A1–A12, T1-T8, F1-F12, P1-P10, C1-C10), 28 resolved contradictions (R1–R28), 12 MOQs + SOQ registers
8. `sv/requirements/e-invoicing/00_index.md` +
   `sv/requirements/taxation/00_index.md` +
   `sv/requirements/fiscal-reporting/00_index.md` +
   `sv/requirements/payroll/00_index.md` +
   `sv/requirements/commercial-legal/00_index.md` +
   `sv/requirements/COVERAGE.md` —
   S1+S2+S3+S4+S5 corpus indexes + source coverage matrix (authoritative for
   source→wave mapping)
9. `HANDOVER.md` (this file)

## 3. Current state (2026-08-20)

### Git / repo
- Branch `main` only; remote `origin` = `git@github-CtrlCarlitos:CtrlCarlitos/odoo-localizations.git` (SSH alias `github-CtrlCarlitos` from `~/.ssh/config`); push after each wave; never force-push. `gh` CLI at `~/.local/bin/gh`, authenticated as CtrlCarlitos.
- Commits are SSH-signed; local `%G?=N` is a verification-only artifact (`gpg.ssh.allowedSignersFile` unset) — signatures ARE present; don't chase it.
- `.gitattributes`: `*.csv text eol=lf`.
- Commits through `8ac5d6a` (2026-08-22: HN W12 merge — see §3
  thirty-fifth run; `c1e740a` 2026-08-22: GT W-GT7 merge — see §3
  thirty-fourth run; `ba98ac7` 2026-08-22: HN R-H91 merge — see §3
  thirty-third run; `3250ffa` 2026-08-22: GT S-GT6/S-GT7 merge — see §3
  thirty-second run; earlier `d37f89f` 2026-08-22: HN W11 merge —
  thirty-first run, `56ee669` 2026-08-22: SV W18 merge — thirtieth run,
  `23ad21e` 2026-08-21: GT S-GT5 merge — see §3
  twenty-sixth run; earlier: `b881f87` 2026-08-20 SV W17, `ac7184b`
  2026-08-20: GT S-GT1 merge — see §3 ninth
  run; earlier: `53edd55` 2026-08-19 6th session, multi-part: D15 as-of
  doctrine `cc7a307` → W13 evidence pass `94b4142` → GT/HN merges + D16
  unification `5eb6d6b` → universalization + D17 + roadmap `b67dfa0` →
  D18 `4cd719a` → D19 + go-live-readiness.md `53edd55`; all pushed). **HN
  wave-2 merge 2026-08-20:** `hn-research` fast-forward-merged (`7fdacba` +
  `92f35dd`, W1+W2 evidence EVID-001..185). **HN wave-3 merge 2026-08-20
  (§4.6 protocol, first run):** `hn-research` rebased onto `c077455` (2
  commits rewritten: `78082e3` HANDOVER-pointer + `c1f9fa8` W3 facturación
  evidence EVID-186..214, D-H1 inputs evidence-complete) then
  fast-forward-merged; remote branch ref updated via delete + re-push. HN =
  taxation + fiscal-reporting + facturación evidence complete; next W4
  payroll. **GT wave-1..3 merge 2026-08-20 (§4.6 protocol, second run):**
  `gt-research` rebased onto `de420c2` (6 commits rewritten:
  `ae78891` convergence residue + `4249ea5` EXTRACTION_PLAN Stage 0 +
  `00830f1` W-GT1 FEL stack EVID-001..160 + `8f5fbaf` W-GT2 taxation core
  EVID-161..265 + `12faa93` W-GT3 payroll EVID-266..370 + `58055c2`
  HANDOVER addenda; one HANDOVER conflict resolved — GT state paragraph vs
  main's HN-paragraph restructure) then fast-forward-merged; remote ref
  updated via delete + re-push. GT = EXTRACTION_PLAN approved + W-GT1/W-GT2/
  W-GT3 evidence complete (14 files, EVID-001..370; Reglas = v2.0;
  OQ5/OQ6/OQ13 resolved, OQ12 disproven, OQ17 resolved-as-myth, OQ11 open;
  see `gt/HANDOVER.md` §5a-5c); next W-GT4 fiscal reporting. **HN wave-4
  merge 2026-08-20 (§4.6 protocol, third run):** `hn-research` rebased onto
  `7007695` (1 commit rewritten: `63e854b`→`d5a2f4b` W4 payroll evidence
  EVID-215..333) then fast-forward-merged; remote branch ref updated via
  delete + re-push. HN = ALL FOUR evidence waves complete (taxation +
  fiscal-reporting + facturación + payroll; 17 evidence files,
  EVID-001..333, ~227 open OQs, corpus 103 files); next synthesis prep
  (master index + OQ registers) then S-waves. W4 keys: IHSS matrix IVM
  3.5/2.5/0.5 + EM 5/2.5/0.5 (worker 5% / employer 8.5%), TWO regime
  ceilings (post-2025 = JD actuarial rows); RAP fondo 4% + 1.5+1.5 stacked,
  coexists-with-offset vs CT cesantía (CT Art. 120 lit. f hook); SMM
  promedio printed ONLY in DGS companion tables (2026 L14,917.20 → 10×SMM
  cap L149,172; never recompute); aguinaldo NOT in the CT (D.135-94 +
  Acuerdo 201-96 = TOP acquisition leads; D.112 SAR routes exhausted);
   85_ = 9th title-vs-content incident (D.93-2021 derogates Penal-only, ZERO
   CT articles — guard table EVID-333). **HN synthesis-prep merge 2026-08-19
   (§4.6 protocol, fourth run):** `hn-research` rebased onto `7cc9dd3` (1
   commit rewritten: `e4fa9e8`→`e106b1f` synthesis prep — one HANDOVER
   conflict resolved vs main's W4 merge record) then fast-forward-merged;
   remote branch ref updated via delete + re-push. HN master index BUILT
   (`hn/.extractions/00_MASTER_INDEX.md`: 43 clusters T1-T12/F1-F11/E1-E8/
   P1-P12, R-H1..65 ledger, OQ registers C1-C4 ~227 open, authority orders,
    S-wave plan); next S-HN1 taxation synthesis (S-HN2 e-invoicing
    parallel-able; SEE/CAEE sub-cluster blocked on lead 1). **SV S7 merge
    2026-08-19 (§4.6 protocol, fifth run):** `sv-research` rebased onto
    `d1b59ed` (14 commits rewritten: `bf87179` sv/HANDOVER bootstrap →
    `f4a1076` S7 prep → `fe819ac` S7 plan → `2f33019..10a7cc0` T1-T9
    wave → `ebf76c6` session close; zero conflicts — all sv/-scoped or
    new files) then fast-forward-merged; remote branch ref updated via
    delete + re-push. SV = S7 special-regimes synthesis COMPLETE (8
    files + index, 175 FRs / 130 LBs / 80 ACs / 42 OQs, SV-SPE-FR-
    001..175; final whole-wave review MERGE-READY; see §3 S7 section +
    `sv/HANDOVER.md`); `sv/HANDOVER.md` now the authoritative SV memory;
     next NIIF/COA wave (32_/33_) then IVA-core taxation. This HANDOVER
     update commits on main directly (integration branch). **GT wave-4..6
     merge 2026-08-20 (§4.6 protocol, sixth run):** `gt-research` rebased
     onto `7dc31e1` (3 commits rewritten: `2a60011`→`cf83e67` W-GT4
     fiscal reporting EVID-371..500 + `3e449ab`→`da5829c` W-GT5 COA/
     commercial-legal EVID-501..645 + `356c21b`→`716c00b` W-GT6 special
     regimes EVID-646..745; zero conflicts) then fast-forward-merged;
     remote branch ref updated via delete + re-push. **GT = ALL SIX
     evidence waves complete** (26 evidence files, EVID-001..745, ~195
     per-file OQs; session resolved OQ14 (D-15-2026 derogates D-67-2001 +
     D-58-2005, vigencia 17-sep-2026, reglamento ≈17-mar-2027, no Q
     threshold in law) + OQ15 (AG 65-2022 = the AG 242-90 ZF-reglamento
     reform — W5 ZOLIC-only verdict wrong, registry corrected) + added
     OQ18 (5% pequeño/agro retention rates); two registry identity
     corrections: 48_ form map (ISR anual = SAT-1411, asalariados =
     SAT-1431, 1371 = no-residentes, retenciones = SAT-1331) + 81_; see
      `gt/HANDOVER.md` §5a-5f); next master-index/MOQ prep
      (00_MASTER_INDEX.md) then S-GT1 e-invoicing synthesis; D-19-2016 =
      top-ranked acquisition (blocks special-regimes synthesis quality).
      **GT synthesis-prep merge 2026-08-20 (§4.6 protocol, seventh run):**
      `gt-research` rebased onto `5bdd97f` (1 commit rewritten:
      `4227af8`→`d1ba16c` master-index build; zero conflicts) then
      fast-forward-merged; remote branch ref updated via delete + re-push.
      **GT master index BUILT** (`gt/.extractions/00_MASTER_INDEX.md`:
      40 clusters E1-E8/TX1-TX7/P1-P7/F1-F6/C1-C6/SR1-SR6, 81-row R ledger,
      140-GOQ register rolled from all 250 per-file OQs + struck audit,
      authority orders, OQ1-OQ18 mapping; 8 controller-verified quotes).
      Three index-level resolutions: **R20** Q150,000 = D-4-2012 reforming
      LIVA arts. 45/46 ("LAT attribution" was research-era error); **R45**
      CCom vigencia = 1971-01-01 (01-07-1970 = D-43-70 tag date — corrected
      gt/HANDOVER §5e); **R81** maquila art. 12 bis ADDED by D-19-2016
      art. 7 (corrects §5f "born D-38-04").       DOWNLOAD_QUEUE rev 7. **Next:
      S-GT1 e-invoicing synthesis plan → subagent wave** (master index =
      the gate, closed); see `gt/HANDOVER.md` §5g. **GT S-GT1 merge
      2026-08-20 (§4.6 protocol, ninth run):** `gt-research` rebased onto
      `8282ae6` (14 commits rewritten `7bea5c4`→`ac7184b`: plan + 8 task
      waves + T9 + fixes; zero conflicts) then fast-forward-merged; remote
      ref updated via force-with-lease re-push. **GT = S-GT1 E-INVOICING
      SYNTHESIS COMPLETE** — first requirements wave: 8 files + 00_index +
      COVERAGE (GT-EINV-FR-001..243 + GT-CAT-FR-001..015; 139 LBs / 99 ACs
      / 45 OQ rows consuming GOQ-15..52 + 02/03/07/13/14; catalog CSV
      sidecars 88/43/211 GH-authority + _DRIFT; master-index write-back 43
      rows; all task reviews Approved + final whole-wave MERGE-READY).
      Evidence corrections vs briefs: 19-code legacy FACE list; 18+3
      complements; Reglas 3.5.1.6. **OPEN architecture item: D1
      no-local-fallback vs GT contingencia local-XML requirement (FR-220)
      — needs product-owner ruling before implementation.** Next: S-GT2
      taxation plan; see `gt/HANDOVER.md` §5h + §10. **SV W14/S8-prep merge
      2026-08-19 (§4.6 protocol, eighth run):** `sv-research` rebased onto
      `8282ae6` (3 commits rewritten: `290364c` W14 NIIF evidence +
      S8-prep, `673c981` S8 plan, `f3dae2f` session close; zero conflicts)
      then fast-forward-merged; remote branch ref updated via delete +
      re-push. **SV W14 COMPLETE** (32_ NIIF-PYMES 3rd ed. + 33_ EY guide
      read end-to-end, EVID-275..303; master-index clusters N1-N8 + R29
      authority rulings + SOQ-46..53; the SV adopting-instrument gap =
      SOQ-46 gates S8 eligibility config). **S8 synthesis plan READY**
      (`docs/superpowers/plans/2026-08-19-s8-chart-of-accounts-synthesis.md`,
      9 tasks, prefix SV-COA) — next SV session bootstraps
      `Read sv/HANDOVER.md and continue.` and runs the subagent wave in
      `.worktrees/sv`; see `sv/HANDOVER.md` §1/§8. **HN S-HN1+S-HN2 merge
      2026-08-20 (§4.6 protocol, ninth run):** `hn-research` rebased onto
      `ca83157` (1 commit rewritten: `ea8bc40`→`6d1cfc3` S-HN1 taxation +
      S-HN2 e-invoicing synthesis; one hn/HANDOVER conflict resolved vs
      main's synthesis-prep merge record `07a4069`) then
      fast-forward-merged; remote branch ref updated via delete + re-push.
      **HN FIRST TWO SYNTHESIS WAVES COMPLETE** (`hn/requirements/taxation/`
      7 files + index, HN-TAX-FR-001..281 = 248 FRs/109 LBs/135 ACs/54 OQs
      + `isr_brackets.csv` FY2022-2026 vintages; `hn/requirements/
      e-invoicing/` 4 files + index, HN-EINV-FR-001..175 = 155 FRs/68 LBs/
      67 ACs/26 OQs + `document_types.csv`; D-H1/D-H2/D-H3 encoded — D-H2.2
      hard CAI-vigencia emission gate; SEE/CAEE config-gapped on lead 1;
      controller-verified 11/11 + 5/5 verbatim spot-checks). Synthesis
      rulings: 10-SMM caps excess-only; FY2026 promedio cap L149,172
      (R-H47); DAR→DJIMR (R-H31); bad-debt cap 10%-of-AR; L30k@60 tier →
      D. 199-2006 (activation-blocked). **Proposed R-H66 territoriality
      ruling (worldwide pre-2017 / territorial 2017+) encoded reversibly —
      OPEN for owner confirmation.** New top LEAD: Reglamento Ley ISR
      ("Acuerdo N°799"). Next per `hn/HANDOVER.md`: S-HN3 fiscal-reporting
      → S-HN4 payroll → validation wave (COVERAGE + adversarial review).
      **HN S-HN3 + R-H66 merge 2026-08-20 (§4.6 protocol, tenth run):**
      `hn-research` rebased onto `b98dae1` (3 commits rewritten:
      `3c54832`→`e79afef` hn/HANDOVER ninth-run record, `e3f9eb2`→`4847630`
      S-HN3 fiscal-reporting synthesis, `9af3972`→`00caef9` R-H66 adoption;
      zero conflicts) then fast-forward-merged; remote branch ref updated
      via delete + re-push. **HN THIRD SYNTHESIS WAVE COMPLETE**
      (`hn/requirements/fiscal-reporting/` 11 files + index,
      HN-FREP-FR-001..393 = 362 FRs/154 LBs/188 ACs/169 OQs +
      `djimr_retention_codes.csv` 25 codes; F1-F11 all clusters; S-HN1/
      S-HN2 ids consumed throughout; controller-verified 11/11 + 5/5
      verbatim spot-checks; one sanctioned direct-cite exception = F9 IPC
      chain 98_/99_/100_ page-1-verified, values re-verified vs raw txt).
      **R-H66 territoriality ADOPTED by product owner 2026-08-20**
      (worldwide pre-2017 / territorial 2017+; taxation/01 FR-004 reversible
      dated rows; master-index R ledger now 66 rows). Only yes-blocking
      S-HN3 OQ = 506-vs-509 boundary (LSP statutes unacquired). Next per
      `hn/HANDOVER.md`: S-HN4 payroll → validation wave at S-HN4 close
      (COVERAGE + adversarial review).
      **HN S-HN4 merge 2026-08-20 (§4.6 protocol, eleventh run):**
      `hn-research` rebased onto `daa8a10` (2 commits rewritten: `087e94f`→
      `3ee60c0` hn/HANDOVER tenth-run record, `9890bda`→`d05f2c1` S-HN4
      payroll synthesis; zero conflicts) then fast-forward-merged; remote
      branch ref updated via delete + re-push. **HN FOURTH AND FINAL
      S-WAVE COMPLETE — ALL FOUR SYNTHESIS TOPICS DRAFTED**
      (`hn/requirements/payroll/` 10 files + index,
      HN-PAYR-FR-001..398 = 313 FRs/146 LBs/163 ACs/73 OQs +
      `smm_tables.csv` 199 rows w/ print_status discipline — never a
      derived amount in an amount cell; P1 owns the SMM/promedio rows
      feeding taxation/04 FR-134 per R-H47; controller-verified 10/10
      structural + STRICT FULL verbatim bank-check — every quote-bounded
      Spanish span in every file vs the evidence bank, 372 PASS, 5 one-word
      LB defects found+fixed; the strict bank-check supersedes 5-sample
      spot-checks for future waves; 10/10 dispatches delivered, zero
      empty-return anomalies). Only yes-blocking S-HN4 OQ = aguinaldo P2
      sub-cluster (D. 135-94 + Acuerdo 201-96 unacquired — top of the
      acquisition queue). Evidence-over-brief corrections kept: feriado
      collision = two-holidays-one-day; Art. 349 ¶2 proportional leg
      employer-imputable-only; cesantía fraction = Art. 120 lit. c; Art.
      104 rule-4 no half-salary qualifier. Next per `hn/HANDOVER.md`:
      validation wave (COVERAGE.md all four topics + adversarial review,
      template Stage 5) + S-HN5 thin-close decision at milestone.
      **GT S-GT2 merge 2026-08-20 (§4.6 protocol, twelfth run):**
      `gt-research` rebased onto `7a40433` (12 commits rewritten
      `8505725`→`4a17961`: S-GT2 plan + 7 taxation task files + T8
      index/COVERAGE/write-back + final-review fixes + session close; zero
      conflicts — all gt/-scoped or new files) then fast-forward-merged;
      remote branch ref updated via delete + re-push. **GT = S-GT2
      TAXATION SYNTHESIS COMPLETE** (`gt/requirements/taxation/` 7 files +
      00_index, GT-TAX-FR-001..261 = 261 FRs/136 LBs/93 ACs/38 OQ rows +
      `iva_retention_rates.csv` 16 rows [8 statutory + 8
      secondary-print-pending, R55 never frozen] + `isr_rates.csv` 17 rows
      [4 transitional valid_to]; TX1-TX7 all clusters; GOQ-53..69 +
      GOQ-01/06 consumed with master-index write-back incl. 5-column GOQ
      table headers register-wide; **two in-corpus GOQ resolutions:
      GOQ-118 [AG 425-2006 art. 4 = Sistema procedure AND art. 9 =
      dualidad — R52 dissolved, source-verified] + GOQ-68 resolved-negative
      [24_ art. 29 ¶6 = electronic-invoice exception, NOT AG 125-2022 —
      acquisition stands]**; GOQ-119 dualidad modeling call made
      [config-driven + saas Sistema-% resolution]; R20 full footnote
      mapping 45←12/46←13/50←18; GOQ-99 statutory half answered; COVERAGE
      42 cited/40 N-A/0 pending — EV04b/c manuals + digest/criterios cited
      ONLY as dated-as-of secondary/interpretive anchors; 7 task reviews
      [6 first-pass Approved, 1 fix round] + final whole-branch review [1
      Important: FESP IVA-side cross-lock mispointed at FR-080..085 →
      repointed to FR-097/GT-EINV-FR-036/LB-021; fixed + re-review PASS];
      ~30 verbatim quote checks, zero fabrications; rulings: evidence files
      are frozen wave artifacts — LB backfill rejected; cross-file handoffs
      must terminate at a resolving FR id, never a family-range guess).
      **HN V-HN1 merge 2026-08-20 (§4.6 protocol, thirteenth run):**
      `hn-research` rebased onto `7b89224` (2 commits rewritten
      `49f57d5`→`47593f2` HANDOVER eleventh-note + `cc5444d`→`960df34`
      V-HN1 validation wave; zero conflicts — all hn/-scoped or new
      files) then fast-forward-merged; remote branch ref updated via
      delete + re-push. **HN = VALIDATION WAVE COMPLETE — ALL FOUR TOPICS
      APPROVED** (`hn/requirements/COVERAGE.md` generated by committed
      `hn/scripts/build_coverage.py`: 103 rows = 98 cited-as-LB + 5
      annotated N/A; script gates = every FR cites an own-file LB (1082
      FRs), every LB token resolves to registry+disk (480 LBs), per-topic
      totals match indexes [248/157/363/314 FRs; 566 ACs; 317 OQ rows];
      gate 2 skipped — no notebook; gate 3 = four fresh adversarial
      reviewers, findings adjudicated in hn/EXTRACTION_PLAN V-HN1 log).
      Keys: **`89_` D. 117-2021 had NO evidence pass = 10th
      title-vs-content incident** — Art. 2 = authentic interp of D.
      112-82 Art. 3 (séptimo día + 13th month = salario ONLY for labor
      prestaciones; aguinaldo exempt from ALL taxes/cotizaciones/
      deductions except alimony) → payroll/02 FR-087 + OQ-007 CONFLICT
      vs ISR Art. 10.h 10-SMM caps carried as R-H67 (ISR rows stand);
      IHSS-base lean payroll/03, RAP-base lean payroll/05; Art. 1 CT-
      113.1 TP-scope interp → F10 OQ-004 RESOLVED (TP reaches only
      related parties, never regime entities). Evidence fixes R-H68..70:
      selectivo vehicles WHOLE-BASE brackets (not marginal); 65+ L350k
      exemption CLIFF (not cap); feriados = ELEVEN (8 + Semana Santa 3).
      95_/96_ were in-corpus-unread pre-S-HN1 ("unacquired" claims
      fixed; FR-067 senior tier stays activation-blocked pending their
      read). Gap closures: EINV FR-085 filed-period freeze + FR-086
      go-live reconciliation (D-H2.5/D-H3.2 implementations), FREP
      FR-076 111-split, PAYR FR-087; ~12 AC additions; sibling cite
      repairs payroll-wide. Next per `hn/HANDOVER.md`: acquisition wave
      (D. 135-94 + Acuerdo 201-96 TOP) + 93_-97_ in-corpus reads + S-HN5
      thin-close scoping at milestone.
      **HN V-HN1b merge 2026-08-20 (§4.6 protocol, fifteenth run):**
      `hn-research` rebased onto `074c6eb` (1 commit rewritten
      `436dc90`→`cf7dfe9` V-HN1b; zero conflicts — SV's fourteenth-run
      record touched only the root HANDOVER) then fast-forward-merged;
      remote branch ref updated via delete + re-push. **HN = VALIDATION
      FOLLOW-UPS + ACQUISITION ROUND 6**: in-corpus evidence reads of
      95_/96_ (EVID-337..348) and 93_/94_/97_ (EVID-350..361) — **FR-067
      senior L30k tier PINNED + ACTIVATED** (D. 199-2006 Art. 30 num. 14
      own-law "crédito adicional", NOT an ISR amendment; valid_from
      10-ago-2007; R-H71; OQ-008 resolved, OQ-009 carries: D. 59-2023
      intermediate reform UNACQUIRED = new top lead, beneficiarios-class
      mismatch, stacking = plantilla-only practice); 22-A FR-082 gains
      regime 0 FY2017 (original D. 278-2013 Art. 9 rules per D. 31-2019
      authentic interpretation, R-H72; gazette pin G 34,932 — catalog
      34,934 in error); 97_ Art. 14 original 5-consecutive-periods
      condition recorded as FR-068 history rows (R-H73). **Acquisition
      wave: D. 112 — the aguinaldo law — FOUND** via Wayback snapshot of
      the official STSS upload (live link stale-404; corrects round-5's
      "routes exhausted"), + Acuerdo STSS-154-2000 bono reglamento (the
      payroll/02 OQ-004 lead) + D. 150-2008 + Acuerdo 345 = corpus 107
      files (105-108; duplicate D. 103 upload discarded md5-identical).
      S-HN5 scoping: DEFERRED pending Código de Comercio + Ley RAP.
      Coverage 107 rows = 101 cited + 6 N/A (evidence passes pending for
      105-108). Next per `hn/HANDOVER.md`: evidence passes 105-108 (105_
      unblocks the P2 aguinaldo sub-cluster), D. 59-2023 fetch via ENAG
      Feb-2024, then D. 135-94/201-96 + Acuerdo 799 + Reglamento General
      IHSS + Ley RAP.
      Next per `gt/HANDOVER.md` §5i/§9: S-GT3 payroll plan (GOQ-70..91 +
      GOQ-04/09/10/11; consumes taxation/04 art. 70/72 FRs; carry
      R30/R36/R41 bonus-law corrections).
      **SV branch reconcile 2026-08-20 (§4.6 protocol, sixteenth run):**
      one-commit close-out — `8e3ee84` (the `sv/HANDOVER.md` S9 merge
      record) had landed only on `sv-research` while the fourteenth
      run's record went only to main, leaving main's `sv/HANDOVER.md`
      stale ("MERGE-READY", §8.1(a) merge listed as pending). Rebased
      twice (`8e3ee84`→`ace2838` onto `074c6eb`, then →`a340d54` onto
      `22c4607` after the concurrent HN fifteenth-run close advanced
      main mid-run; zero conflicts both times — disjoint files) then
      fast-forward-merged; remote ref updated via delete + re-push.
      No requirements changes; SV state unchanged per
      `sv/HANDOVER.md` §8 (no queued wave — owner picks).
      **SV W16 merge 2026-08-20 (§4.6 protocol, eighteenth run):**
      `sv-research` rebased onto `e8e558b` (1 commit rewritten:
      `b3e63b6`→`1c40560` W16; zero conflicts — sv/-scoped only)
      then fast-forward-merged; remote ref updated via delete +
      re-push. **SV = W16 EXTERNAL-CHECK + ACQUISITION WAVE:**
      **D.O. `/seleccion` RECOVERED** (serves PDFs again after the
      08-18 outage; API param shape unpinned — pin before the
      SOQ-41/34 hunts); asamblea still 000; MH formularios unchanged
      (no F-11 v19/v20, no F14 v17 manual); factura.gob.sv no LB
      drift; no new AML reglamento (watch to 2026-10-17). **75_ =
      Reglamento de Aplicación del CT, D.E. 117-2001** (TF DC5854) —
      the R17/R30(a) mass-repeal authority instrument finally owned;
      EVID-339..358 (EV75, 8 OQs). **R30(a) corrected by instrument
      audit: 02_ live survivors = Arts. 1-10, 16-26, 29-30, 50-51**
      (old "16-30" over-included 27-28; 36/45 died via D.E. 60-1993,
      not 147(b); all V1-V10 cites verified in-set; taxation
      07/08/09/10/14 preambles fixed in-wave). **SOQ-54 Ley side
      RESOLVED** (TF DC9226 second official print ≡ 01_ through (14)
      D.L. 71-2015). Leads banked: 75_ Art. 100 = SOQ-08 anchor
      (EVID-351); imprescriptible retentions (Art. 23) vs 2-y agent
       caducidad (Art. 133); 75_ FR fold-ins queued at the next
       edit wave. Next per `sv/HANDOVER.md` §8: fold-ins, SOQ-46/
       SOQ-54-Rgto acquisitions, CAN-STAND/RIDE cleanups, or go-live
       prep — owner's call.
       **HN W5+W5b merge 2026-08-20 (§4.6 protocol, nineteenth run):**
       `hn-research` rebased onto `20c517d` (3 commits rewritten
       `51be444..6f37179`→`9a8dc2f..cd01045`: W5 acquisition-reads +
       W5b 109_ fetch + HANDOVER consistency pass; zero conflicts —
       hn/-scoped only) then fast-forward-merged; remote branch ref
       updated via force-with-lease re-push. **HN = W5 ACQUISITION
       -READS WAVE COMPLETE** (105_-108_ evidence passes EVID-362..384:
       **P2 aguinaldo UNBLOCKED** — D. 112-1982 = the 13th-month law
       (R-H74), "D. 135-94/201-96" framing voided (R-H75); bono
       reglamento STSS-154-2000 encoded (R-H76, OQ-004 resolved);
       séptimo día statutory layer (payroll/06 FR-248/249); payroll
       314→326 FRs, COVERAGE 108 rows = 105 cited + 3 N/A; plus 109_ =
       D. 59-2023 Adulto Mayor intermediate reform acquired via ENAG G
        36,460 14-feb-2024, evidence pass PENDING). Next per
        `hn/HANDOVER.md`: 109_ evidence pass + the R-H75 interp/reform
        chain — bootstrap `Read hn/HANDOVER.md and continue.`
       **HN W5c merge 2026-08-20 (§4.6 protocol, twentieth run):**
       `hn-research` rebased onto `5c7185b` (2 commits rewritten
       `014b758..cbad485`→`47d56f8..9d1aac4`: nineteenth-merge branch
       record + W5c 109_ evidence pass; zero conflicts — hn/-scoped only)
       then fast-forward-merged; remote branch ref updated via delete +
       re-push. **HN = 109_ EVIDENCE PASS COMPLETE — CORPUS FULLY
       EVIDENCED (108/108 files, EVID-001..391)**: R-H78 — D. 59-2023 =
       adición-only reform of D. 199-2006 Arts. 3/30, the L30,000 senior
       credit (Art. 30.14) SURVIVES unchanged (tercera list reprinted
       summarized 1)-14) with GAZETTE-print ellipses, dual-OCR-pass
       confirmed; taxation/02 OQ-009(a) resolved, FR-067 =
       10-ago-2007 whole-life row, vigencia 14-feb-2024; R-H79 — cuarta
       edad = 80+ DEFINED (resolves 96_ OQ-2; D.45-2025 utility-tier
       predicate pinned; cuarta catalogue banked for S-HN5); reformed
       BENEFICIARIOS jubilado-leg flag (OQ-009(b)); edition decrees
       identified (D. 63-2023 promotions / D. 5-2024 municipal amnistía,
       expired / D. 6-2024 migration); taxation index 248/113/140/56;
       COVERAGE 108 rows = 106 cited + 2 N/A, gates PASS; R-H1..R-H79.
       Next per `hn/HANDOVER.md`: R-H75 interp/reform chain (D. 179-97
       top) + 95_ clean-consolidation lead — bootstrap
       `Read hn/HANDOVER.md and continue.`
       **HN W6 merge 2026-08-20 (§4.6 protocol, twenty-first run):**
       `hn-research` rebased onto `36df87c` (3 commits rewritten
       `804a98c..7b1e597`→`1124e23..24391b6`: twentieth-merge branch
       record + W6 acquisition + W6 evidence pass; zero conflicts —
       hn/-scoped only) then fast-forward-merged; remote branch ref
       updated via delete + re-push. **HN = W6 R-H75-CHAIN WAVE
       COMPLETE (acquisition + evidence pass same session; corpus
       117 files, evidence through EVID-428):** route = Wayback of the
       old official `congreso.gob.hn/leyesdehonduras/` library (512
       PDFs, CDX-catalogued, `id_` fetch — the pre-2015 decree source;
       NATLEX/Mojeek/DDG hard-blocked from this network, recorded).
       Nine files `110_`..`118_`: **D. 179-97** (reforms D. 112 Arts.
       1+9 = the jubilados/pensionados 13th-month extension — payroll/02
       OQ-008 RESOLVED, dated beneficiary rows permanents-only
       1982-11-01→1997-12-16 / +jubilados from 1997-12-17, FR-052),
       **D. 178-86** (interp original), **D. 2-87** (dado 3-feb-1987 —
       the "30-feb" print error resolved; convention/custom-permanent
       adición; OQ-009 RESOLVED), **D. 112-1982 ORIGINAL gazette print**
       (G 23,848 — gazette pin now PRIMARY; original Art. 1 =
       permanentes-only "recibirán además"), **D. 135-94** (14th-month
       origin Cap. IX Art. 34; NEW vigencia conflict OQ-012 carried),
       **D. 58-1982** (selectivo código-203 origin — 1982 cc-tier
       canasta + 1995 20% states; FREP/09 OQ-001 narrowed),
       **D. 131-98** (Art. 43 = the 4% turística/código-259 origin;
       FREP/09 OQ-010 RESOLVED; operadora anti-cascading exclusion
       encoded FR-321), **D. 110-93** (Art. 9 intereses = código-115
       core; FREP/02 Art. 12 L50,000 savings monto ACTIVATED, excess-
       only), **D. 54-96** (FIRST Ley Equidad Tributaria; FREP/07
       job-credit statute + OQ-014 narrowed). **R-H80**: Art. 18
       transitory = "1° de enero de 1983" per the gazette (triple-OCR
       300/400/600dpi convergence; no in-session image input) vs the
       105_ book's "10 de enero" — gazette = record, no-liability
       window ends 1982-12-31. Rulings R-H1..R-H80; payroll index
       326/163/170/83, FREP 363/157/189/169; COVERAGE 117 rows = 115
       cited + 2 N/A, gates PASS (1094/502/573/325). Residual chain
       (D. 36-90 / D. 54-95 / D. 247-89 — verified ABSENT from the
       congreso library) + post-W6 queue (Acuerdo 799, Reglamento
       General IHSS, Ley RAP, D. 314-98 watch, post-1995 selectivo
       chain, D. 99-93) + 95_ clean-consolidation lead — bootstrap
       `Read hn/HANDOVER.md and continue.`
       **GT S-GT3 merge 2026-08-20 (§4.6 protocol, seventeenth run):**
      `gt-research` rebased onto `7bf2e86` (14 commits rewritten
      `da0f374..57c6be0`: plan + T1..T11 + close + final-review fixes;
      zero conflicts) then fast-forward-merged; remote branch ref updated
      via force-with-lease re-push. **GT = S-GT3 PAYROLL SYNTHESIS
      COMPLETE** — third requirements wave: 10 files + 00_index +
      salario_minimo.csv 82 rows (GT-PAY-FR-001..236; 159 LBs / 151 ACs /
      29 OQ rows consuming GOQ-70..91 + GOQ-04/09/10/11 + kin
      58/61/99/121; master-index write-back 26 GOQ annotations; all 10
      task reviews Approved first-pass + final whole-wave MERGE-READY +
      fix-wave re-review PASS). Discipline shipped: IGSS rates ALL
      external (GOQ-04 — 12.67/4.83 rejected priors only); 2026
      salario-mínimo six cells [sic]-faithful words-govern (GOQ-77/78) +
      2022-2025 ABSENT rows never interpolated (GOQ-11); December
      aguinaldo = ABSENCE-FR (GOQ-09); no cesantía/doubling/employer
      -preaviso/holiday-2×/IRTRA-brackets (R33/R37/R38/R32); ISR consumed
      by exact FR id via payroll/09 (31 external ids verified).
      Trust-evidence rule caught FOUR controller-brief errors (art. 103
      ¶2; precio-de-costo; 50%-of-indemnización; INTECAP ladder dates).
      Next per `gt/HANDOVER.md` §5j/§9: S-GT4 fiscal-reporting plan
      (F1-F6 + GOQ-92..121; consumes taxation + payroll FR ids).
      **GT S-GT4 merge 2026-08-20 (§4.6 protocol, twenty-second run):**
      `gt-research` rebased onto `8513e49` (13 commits rewritten
      `fa2152d..88cb6e8`→`68cd873..4be704d`: S-GT4 plan + T1..T6 topic
      files + T7 index/COVERAGE/write-back + session close +
      final-review fixes; zero conflicts — gt/-scoped or new files only)
      then fast-forward-merged; remote branch ref updated via
      force-with-lease re-push. **GT = S-GT4 FISCAL-REPORTING SYNTHESIS
      COMPLETE** — fourth requirements wave: 6 files + 00_index
      (GT-FIN-FR-001..185; 111 LBs / 79 ACs / 40 OQ rows consuming
      GOQ-92..121 + GOQ-14 owned + kin 01/06/09/66/67/94/101/105 and
      resolved kin 118/119/120 never re-opened; master-index write-back
      31 annotations + synthesis-order line). Discipline shipped: R46 ISR
      identities on every form-naming row (1411/1431/1371/1331/1321);
      R47 SAT-2320 10-dh = RetWeb print never frozen; statutory
      non-re-derivation held wave-wide (GT-TAX-FR-105..110 + 025/031..037
      + both rate CSVs consumed by exact id; payroll via
      GT-PAY-FR-213..222; GT-EINV-FR-210 outcome-only); GOQ-105
      LET-layouts-images negative-FR = export-layout hard blocker; the
      63_ CSV spec column-letter-faithful (16/11-col; >Q2,500 NIT+ID from
      2023-01 dated row); criterios confirm-only (GOQ-116 clause-citation
      ban; GOQ-121 negative-FR — no GOQ-09 backfill). All 6 task reviews
      Approved first-pass + final whole-wave review (2 minors, one fix
      wave, re-review PASS). COVERAGE 67 cited / 15 N-A / 0 pending (9
      rows flipped; 49_/50_ cited as `gt/sources/…html (read via txt
      layer)` — extraction-dump paths alone don't count for the grep).
      New gap reports for register triage: ISR-constancia form code
      (rides GOQ-98), D27-92 Cap. VIII/IX primary texts, informe
      periodicity, 63_ rule-6c col-D omission, 51_ slash normalization.
      Next per `gt/HANDOVER.md` §5k/§9: S-GT5 COA/commercial plan
      (C1-C6 + GOQ-122..134; GOQ-124 retention/destruction matrix = an
      S-GT5 deliverable; D-19-2016 still blocks S-GT6/S-GT7).

      **HN W11 merge 2026-08-22 (§4.6 protocol, thirty-first run):**
      `hn-research` rebased onto `56ee669` (1 commit rewritten
      `0143500`→`20d10fd`: the W11 wave+session-state commit; zero
      conflicts — hn/-scoped only) then fast-forward-merged; remote
      branch ref updated via delete + re-push. **HN = W11 AMNISTÍA +
      NEGATIVES WAVE COMPLETE (corpus 164 files, evidence through
      EVID-664):** FIVE files `161_`..`165_` registered + evidenced
      (21 EVIDs, controller-executed; the ihss.hn
      "Reglamento-Incapacidad-para-reformas" upload caught as a
      content-identical re-render of `88_` [40/40 pages same text,
      different md5] — discarded unregistered): **THE IHSS AMNISTÍA
      FAMILY BOTH GENERATIONS** — `161_` the Reglamento Especial
      (CI-IHSS print 11-nov-2016, ihss.hn Wayback) + `162_` D.L.
      112-2016 statute-original (G 34,170 26-oct-2016, ENAG) =
      HISTORICAL closed window 25-oct-2017 (flat-12% convenio
      economics, prima/plazo table, débito claw-back, FSA-01,
      RTN-unificación origin); `163_` **D.L. 44-2025** (G 36,861
      11-jun-2025 — the seven-amnistía package) + `164_` **D.L.
      78-2026** (G 37,166 12-jun-2026 — the AMPLIACIÓN: Art. 1 =
      the CURRENT SAR general amnistía window 12-jun→12-oct-2026 on
      obligations ≤31-dic-2025 with principal surviving, **and D.
      7-2026 Art. 7 (06_) DEROGATED same-day**; Art. 2 = the IHSS
      re-grant, intereses restored) + `165_` **Res.
      SOJD-IHSS-016-2026-XIII** (certified G 37,189 9-jul-2026 =
      the REFORMED reglamento: convenio gate principal > L15,000;
      0% ≤12m / 12% longer; prima mínima 10/15/25% sin- and
      20/30/35% con-refinanciamiento; exceptions 120m ≥5% / 96m
      ≥10%; terminal 12-oct-2026 + 6-month processing tail; Art. 24
      continuity + judicial/MP enforcement) — payroll/03
      LB-021/LB-022 + OQ-012; taxation/07 LB-013 + LB-010
      derogation annotation. **W11 NEGATIVES (all scan-verified
      2026-08-22):** NO 2026 JD ceiling act through the NEW ENAG
      full-text scan recipe (218 issues dic-2025→ago-2026,
      grep-all-pages; payroll/03 AC-006's blocking config gap = the
      LIVE state; IHSS JD acts publish as Sección-A certificaciones
      = the techo/rate watch route) · CbCR TRANSITORIO restatement
      comunicado NOT published (FREP/10 OQ-024 stands) · Oficio
      SETRASS-DGS-014-2025 + DGS 2025 print unpublished · ihss.hn
      full-domain CDX (8,000 URLs) negative for RP cuadros/JD
      ceilings/REAP rates · D. 96-2012 re-grep negative. **PLUS THE
      W5 LOST-FILE RECOVERY: the committed
      `106+107+108_*.evidence.md` had been an md5-IDENTICAL
      duplicate of the 105_ pass since the W5 commit (a shape-(b)
      subagent anomaly undetected at W5 verification) — EVID-373..384
      RECONSTRUCTED controller-side (OCR sidecars survived; 600dpi
      re-passes; one own-reconstruction error caught+fixed at 600dpi
      — Art. 10 "extremo que deberá constar"); corpus-global EVID
      structural sweep now an EVERY-WAVE convention.** COVERAGE
      regen: 164 rows = 162 cited + 2 N/A; gates PASS
      (1099/535/574/332); payroll 330/174/172/86, taxation
      249/121/140/56; rulings R-H1..R-H90 (none new); next EVID =
      665. Next per `hn/HANDOVER.md` §6: the residual watch queue
      (2026 JD ceiling act watch via the certificaciones route,
      D. 96-2012 watch, CbCR comunicado watch, "Acuerdo 799" TEXT,
      D. 247-89, Código de Comercio, SEE docs, DGS 2027 promedio
      print; the 506-vs-509 legal reading = OWNER DECISION; S-HN5
      DEFERRED).

       **HN W13 merge 2026-08-23 (§4.6 protocol, thirty-sixth
       run):** `hn-research` already on main tip `a34747b` + 1
       commit `0fc2cbe` (the W13 watch-tick close-out; no rebase
       rewrite needed, zero conflicts — hn/-scoped only) then
       fast-forward-merged; plain push (no ref rewrite). **HN =
       W13 WATCH-TICK SESSION ONLY: NO corpus change (166 files,
       EVID-680, R-H1..R-H91 — all unchanged from the W12 merge).
       The residual watch queue re-ticked, ALL CLEAN/NEGATIVE:**
       (a) **2026 JD ceiling act watch (TOP)** — ENAG ago-2026
       month listing re-enumerated (start=0..72): still ends at
       `20260821-37226` (G 37,226, Fri 21-ago-2026; 22/23-ago =
       weekend, no weekday issues since the W12 tick; septiembre
       listing absent; the year index links months only) → no JD
       ceiling act through 23-ago-2026; payroll/03 AC-006 blocking
       config gap = the LIVE state; next meaningful tick = Mon
       24-ago-2026. (b) **CbCR restatement comunicado**
       (FREP/10 OQ-024) — SAR wp-json negative ("comunicado país
       por país"/"653-2023" empty; only hits = FYDUCA FAQ noise);
       suspended row stands. (c) **D. 96-2012 / "Acuerdo 799" /
       D. 247-89 watch class** — Wayback CDX delta vs the W11/W12
       re-greps: zero new captures of congreso.gob.hn (from
       21-ago), zero new ihss.hn PDFs (from 1-ago), zero new
       trabajo.gob.hn → nothing to re-grep (trigger = a new
       enumeration landing, per the W8 recipe). (d) DGS SMM 2027
       promedio: not due until early-2027. (e) SEE docs: no route
       (lead 1). Fold-ins: EXTRACTION_PLAN wave-log W13 entry +
       RESEARCH §5 dated WATCH TICK line + hn/HANDOVER header/
       session-state. Next per `hn/HANDOVER.md` §6: the residual
       watch queue unchanged (TOP: the 2026 JD ceiling act watch
       via the Sección-A certificaciones route, next tick Mon
       24-ago; D. 96-2012; CbCR restatement comunicado;
       "Acuerdo 799" TEXT + D. 247-89 [the OQ-008 cap-window key];
       SEE docs; DGS SMM 2027 promedio print early-2027; S-HN5
       DEFERRED).

       **HN W12 merge 2026-08-22 (§4.6 protocol, thirty-fifth
       run):** `hn-research` rebased onto `d4937f3` (1 commit
       rewritten `c83c157`→`8ac5d6a`: the W12 GLIN re-grep wave;
       zero conflicts — hn/-scoped only) then fast-forward-merged;
       remote branch ref updated via delete + re-push. **HN = W12
      ACQUISITION WAVE (TWO files, corpus 164→166; EVID-665..680,
      next EVID 681): the Código de Comercio + CT-original pair,
      both from the GLIN archive of the old official
      congreso.gob.hn via Wayback `id_` fetches — surfaced by
      re-grepping the SAVED W7 full-domain CDX for
      comercio/codigos (the W8-recipe lesson executed).** `166_`
      = **Código de Comercio, DECRETO No. 73 de 1950**
      (attribution CORRECTED from "D. 4-1950" — 12th
      lead-attribution fix; Dado 16-feb-1950, Ejecútese
      17-feb-1950, vigor +20 días after publication concludes —
      gazette pin open; official consolidated print post-May-1959
      + the 1940-Libro-III Comercio Marítimo APÉNDICE per
      transitory Art. 1º, truncated at CdC-APX-Art. 1038; **Art.
      143 VERBATIM = the FREP/10 LB-008 541 dividend anchor —
      now instrument-backed**; Art. 13-VI cooperativa + fn(1)
      D. 158-1954 special-law carve-out = R-H91 context only).
      `167_` = **the CT D. 189-1959 ORIGINAL print (complete)**:
      **THE CT PROMULGATION PIN — G 16,827-16,834 of 15→23-jul-
      1959 → vigencia 15-jul-1959**; **THE HEADLINE DELTA:
      original Art. 120 lit. d) caps cesantía at 8 MESES** (the
      25/15 caps arrive with D. 150-2008; the 1990-2008 window
      after D. 247-89 = payroll/08 OQ-008, unpinned,
      prescription-muted); original preaviso ladder ≡ current
      (whole-life rows); original 95.13 coop/cajas deductions =
      sindicalizados-ONLY (non-union 60-A lane wholly post-1973);
      **the 8+3 feriado list = VERBATIM the 1959 original — the
      D.L. 116/275-1960 pair reformed MECHANICS only**; Art. 874
      = the full pre-1959 derogation genealogy. Fold-ins:
      payroll/08 +LB-015 +OQ-008 + FR-302 dated-row note;
      payroll/06 OQ-002 refined; payroll/10 LB-005/LB-015
      annotations; FREP/10 LB-008 annotation; payroll totals
      330/175/172/87. Verification: corpus-global EVID sweep
      654/zero-dup + 3-gram bank-check adjudicated (13/13
      load-bearing tokens; LOWs = OCR-noise/º-glyph classes) +
      COVERAGE regen 166 rows = 164 cited + 2 N/A, gates PASS
      (1099/536/574/333). No new ruling (R-H1..R-H91 — deltas are
      dated-row history). Next per `hn/HANDOVER.md` §6: the
      residual watch queue (TOP: the 2026 JD ceiling act watch
      via the Sección-A certificaciones route [2026 payroll =
      blocking config gap AC-006]; D. 96-2012; CbCR restatement
      comunicado; "Acuerdo 799" TEXT + D. 247-89 [now also the
      OQ-008 cap-window key]; ~~Código de Comercio~~ CLOSED W12;
      SEE docs; DGS SMM 2027 promedio print early-2027; S-HN5
      DEFERRED).

      **HN R-H91 merge 2026-08-22 (§4.6 protocol, thirty-third
      run):** `hn-research` rebased onto `0c45282` (1 commit
      rewritten `052329c`→`ba98ac7`: the R-H91 ruling fold-in;
      zero conflicts — hn/-scoped only) then fast-forward-merged;
      remote branch ref updated via delete + re-push. **HN =
      R-H91 RULING SESSION (no acquisition, no corpus change —
      164 files / EVID-664 / next EVID 665 all unchanged): the
      product owner ruled THE 506-vs-509 cooperative boundary =
      Reading B, CONSUCOOP-gated** — CONSUCOOP-recognized
      cooperativas → código 509 (D. 53-2015/92-2015 world, 15% +
      0.5% floor + exemptions); non-recognized → código 506 (LSP
      Art. 44-A 3.6%). Basis: every other operative article of
      both decrees is CONSUCOOP-gated (reformed Art. 7 sanctions,
      Art. 3-92 liberation window, D. 46-2016/D. 131-2018
      siblings) + the manuals' own 511 test keys on CONSUCOOP
      recognition. Fold-ins: FREP/11 **FR-382 rewritten** (explicit
      selector keeps no-auto-assign/no-silent-dual-filing,
      recognition-guided default, rows REVERSIBLE — legal reading,
      not statute) + AC-011 + config/mapping rows + **OQ-009
      RESOLVED** (the last unqualified yes-blocking OQ); FREP
      00_index wave-noted; master index +R-H91 ledger row + C2
      `60_ OQ-1` resolved + Section-C delta; EXTRACTION_PLAN
      wave-log entry. COVERAGE regen: counts UNCHANGED
      (1099/535/574/332, 164 rows = 162 cited + 2 N/A — status
      flip only); rulings R-H1..R-H91. Next per `hn/HANDOVER.md`
      §6: the residual watch queue unchanged (TOP: 2026 JD
      ceiling act via the Sección-A certificaciones route;
      D. 96-2012; CbCR restatement comunicado; "Acuerdo 799"
      TEXT; D. 247-89; Código de Comercio; SEE docs; DGS SMM 2027
       promedio print early-2027; S-HN5 DEFERRED).

       **SV W21 merge 2026-08-23 (§4.6 protocol, thirty-ninth run):**
       `sv-research` rebased onto `15f2147` (2 commits rewritten
       `a5f5ea3..8a32e93`→`f4a861d..3627bd3`: W21 acquisition + SHA
       bookkeeping; TWO textual conflicts on the W21 commit vs the
       main-side re-probe record `15f2147` — §1 W20-merge-record +
       W21 blurb resolved keep-both; §8.2/8.3 triplicate resolved
       keep-theirs (the W21 version subsumes the re-probe edit)) then
       fast-forward-merged at `3627bd3`; remote branch ref fixed via
       delete + re-push. **SV = W21 COTRANS PRORROGA MINI WAVE
       COMPLETE (corpus UNCHANGED 1,702 FRs; registry 103→104):**
       asamblea.gob.sv recovered same session (A-records restored;
       TLS chain incomplete → `curl -k`; working route = by-year
       decree enumeration, keyword search useless) → **106_ = D.L.
       387-2025 acquired** (the spe/08 OQ-8 target: Art. 2 extends
       COTRANS efectos → 31-dic-2026, D.O. 157 T.448 22-ago-2025;
       vigencia = publication day; EVID-404; junk-prefix trimmed +
       qpdf-repaired) + **D.L. 1000-2024 pinned by recital** (106_
       cons. II = the numberless →31-ago-2025 limb; 617/1000/307
       texts stay un-acquired, verification watch). spe/08 LB-013 +
       FR-189/LB-012 re-stamps + OQ-8 RESOLVED; taxation/09 gate
       note; master index SR8/SOQ-39 closure; COVERAGE 82/9/2/12 of
       105 gate green. Newly unblocked (§8.2): SAS statute hunt
       (SOQ-23) + D.L. 201-2025 text via the asamblea route. SV
       worktree clean at the merge point; no wave queued.

       **SV W22 merge 2026-08-23 (§4.6 protocol, forty-first run):**
       `sv-research` rebased onto `7ee18c7` (2 commits rewritten total:
       `10963bb`→`8fe7854` the W22 acquisition wave — ONE textual
       conflict on sv/HANDOVER §1 — the W22 status block vs the
       main-side W21 merge-record parenthetical, resolved keep-both —
       and the post-merge SHA-bookkeeping commit `4319603`→`15b48a4`,
       rebased clean onto the parallel GT forty-second-run `854cc47`
       at session close) then fast-forward-merged (`8fe7854`, record
       `c4eda40`; bookkeeping follow-up `15b48a4`); remote branch ref
       fixed via delete + re-push. **SV = W22 SOQ-41-RESIDUALS + SAS-HUNT
       ACQUISITION WAVE COMPLETE (corpus UNCHANGED 1,702 FRs; registry
       104→111 files, numbering 01-114, next 115):** asamblea up second
       day (D.O. degraded further to NXDOMAIN; uif still DNS-absent;
       MH formularios path 302→home) → **8 acquisitions = 107_-114_**
       (all asamblea prints, D.O. stamps on face, 8-byte junk prefix
       systemic — trimmed + qpdf ×8): 107_ D.L. 201-2025 Aeropuerto
       del Pacífico (ganancia-de-capital exoneration for CEPA/MOPT
       sellers, efectos from 8-may-2022; D.O. 21 T.446 30-ene-2025 —
       the W18-unpinned issue now stamped) + 108_ D.L. 411-2025
       energía eléctrica acceso-universal (BID/CEL package, vigencia →
       26-sep-2031: IVA exención total, Art. 66 pro-rata NOT applied
       by local suppliers, ISR 4.1 rentas no gravables, CT 260 abuso,
       registros especiales, CEL-seller exemption + no formulario
       duty; D.O. 181 T.448 26-sep-2025) + **the SAS-hunt discovery:
       the post-2008 Código de Comercio reform set** — 109_ D.L.
       153-2021 (bearer shares BANNED from 7-oct-2021; RUC-blocking),
       110_ D.L. 295-2022 (usura 960-A nullity), **111_ D.L. 905-2023
       = THE SAS STATUTE** (SOQ-23 RESOLVED at sources level:
       Capítulo VIII-Bis Arts. 305-A..Z — formulario constitution,
       unipersonal, $1 capital, free reserve, ≤180-día dividends,
       $12,000 accounting threshold; consolidated-reprint print with
       the 203/468 reform stamps), 112_ D.L. 972-2024 (cheque
       truncation), 113_ D.L. 203-2025 + 114_ D.L. 468-2025
       (SAS-gratuidad → 31-dic-2026). **SOQ-22 FALSIFIED-AND-
       RE-RESOLVED** (the W12 "no post-2008 CC reform" verdict dead —
       07_/73_ stale for Arts. 17/18/134/153/155/158/164/212/219/
       315-319/337/338/358/960 + new articles; census caveat: por-anios
       no cards 2010/2012-2015, 2019 partial); **SOQ-41 negatives
       OWNED** (EVID-167 named set 10-of-10). EVID-405..412 (two EV
       files); cml/04 OQ-001 sources-resolved; COVERAGE 81/9/2/20 of
       112 gate green (+8 pending, rationale in COVERAGE_NOTES; the
       pre-W22 "104 files" glosses corrected off-by-one). Fold-in
       debts registered sv/HANDOVER §8.1: cml edit wave (FR-044 SAS
       flip + acciones re-anchors + fusión transnacional + usura/
       truncation notes) + spe/taxation wave (107/108 exemption
       surfaces). SV worktree clean at the merge point.

       **GT idle-close merge 2026-08-23 (§4.6 protocol, forty-third
       run):** bootstrap session (`Read gt/HANDOVER.md and continue.`)
       found the forty-second run already landed and recorded; state
       verified clean (main `854cc47` at open, both checkouts clean,
       remotes synced, both GT inboxes EMPTY, no core.editor
       leftover). No controller-actionable work — queue rev 13 = all
       owner-side/future-dated (DCA-archive SEM/accidentes rate hunt ·
       D-1633 art.-11 montos · AG 52-2017 low watch · 1556-window
       expiry ≈25-sep-2026 · TotalDoc roster 02-dic-2026 · AML
       reglamento ≈17-mar-2027 · accountant · TotalDoc W6); owner
       chose idle close. Single gt/HANDOVER.md addendum commit
       (idle-verification note + next-session bootstrap = inbox check
       for W-GT11) rebased onto the advanced main tip `beef5e1`
       (parallel SV bookkeeping; zero conflicts — gt/-scoped) and
       fast-forward-merged at `ffde2c5`; remote gt-research updated
       via delete + re-push; core.editor unset at close. Corpus
        unchanged 115/0/0; no wave queued.

        **SV W23 merge 2026-08-23 (§4.6 protocol, forty-fourth run):**
        `sv-research` rebased onto `bf9d475` (10 commits rewritten
        `688b4c4..5dcbda9` → `b816b8f..b793f59`, zero conflicts — the
        advance was GT idle-close gt/-scoped bookkeeping only) then
        fast-forward-merged at the rewritten W23 close `b793f59`;
        remote sv-research updated via delete + re-push.
        **SV W23 = the W22 cml fold-in EXECUTED:** the SAS statute
        (111_ D.L. 905-2023) delivered as a full society-type profile
        (FR-044 statute_pending→in_corpus; §3.8 FR-225..240 + FR-246:
        formulario constitution, S.A.S. suffix, $1 capital, free
        reserve, ≤180-day dividends, $12,000 accounting-mode threshold,
        gratuidad → 31-dic-2026, 305-Q/R transform/fuse-into-SAS routes)
        + the 109_ acciones re-anchors (nominative-ABSOLUTE from
        7-oct-2021; FR-066/068 rewrites + FR-241..242 + CT-124 duty
        interface) + cml/05 fusión transnacional + Art. 358 + Art. 338
        escheat→Fondo General del Estado (FR-243..245 + four amends;
        Arts. 317/319 REPLACED wholesale) + cml/08 usura/truncation
        awareness LBs + the SOQ-22 falsification sweep across all nine
        cml files. **Corpus 1,702→1,724 (cml 246/256/142/35); SOQ-23
        FULLY CLOSED; SOQ-22 swept (census-watch residual only);
        COVERAGE 88/9/2/14 of 113 gate green** (109_-114_ cited; W22
        rollup off-by-one corrected; 107_/108_ pending = the next SV
        wave, spe/taxation). Registry unchanged (111 files, next 115).
        Process: subagent-driven 6 tasks (T4 one fix round = quote-tail
         discipline; T1 first dispatch died zero-state, re-dispatched
         clean), final whole-wave review USABLE-WITH-FIXES → one fix
         wave PASS (FR-246 restored); W23-process rulings (a)-(i)
         preserved in sv/HANDOVER.md §5. sv worktree converged to main
         at close.

         **SV W24 merge 2026-08-24 (§4.6 protocol, forty-fifth run):**
         `sv-research` rebased onto `dbe2306` (a NO-OP — main unmoved
         since the W23 merge, so the 11 session commits `eab7604..
         4a4613a` stand UNREWRITTEN) then fast-forward-merged at the
         W24 close `4a4613a`; plain fast-forward push, no remote
         re-pin needed. **SV W24 = the W22 spe/taxation fold-in EXECUTED
         (program item §8.1 CLOSED):** the two SOQ-41 residual
         instruments consumed — 107_ D.L. 201-2025 (CEPA/MOPT
         perimeter-seller ganancia exoneración, efectos from 8-may-2022
         as printed — SV-TAX-FR-418 + spe/01 LB-035) + 108_ D.L.
         411-2025 contractor package (spe/01 FR-200 class-member
         amendment + spe/02 SV-SPE-FR-204 family + taxation FR-417
         rentas-no-gravables chassis + FR-419 CEL-seller exoneración
         with express no-formulario + FR-224 third-channel amendment
         [Art. 174 genéricas working reading recorded, rejection limb
         intact] + FR-420 IVA exemption registry with import no-cascade
         + FR-421 proveedores-locales Art.-66-proportionality
         exception) + **SOQ-40/OQ-2 RESOLVED** (FOVIAL/COTRANS
         instruments independently grep-verified rule-negative;
         FR-244/245 confirmed as labeled product design, config-gated;
         spe/08 OQ-3 resolved-by-pointer). **Corpus 1,724→1,730 (spe
         204/165/100/60; taxation 421/310/290/91); SOQ-41 residual =
         the RAEX reglamento config-gap ONLY — the EVID-167 named set
         fully dispositioned; COVERAGE 90/9/2/12 of 113 gate green**
         (107_/108_ cited). Registry unchanged — count CORRECTED to
         112 file rows (the "111" prose forgot the 17b key; third
         off-by-one-prose incident). Process: subagent-driven 5 tasks
         (T3 one fix round; T5 two; T1 dispatch 1 died mid-work →
         fresh implementer finished), final whole-wave review
         MERGE-READY 0 C/I (4 minors riding); W24-process rulings
         (a)-(h) preserved in sv/HANDOVER.md §5. External sweep: D.O.
         still down (day 3); uif back to 403-WAF. sv worktree converged
         to main at close.

         **SV W25 merge 2026-08-24 (§4.6 protocol, forty-sixth run):**
         `sv-research` rebased onto `812bd84` (a NO-OP — main unmoved
         since the W24 merge, so the 2 session commits `fd54f03..
         f53af59` stand UNREWRITTEN) then fast-forward-merged at the
         W25 close `f53af59`; plain fast-forward push, no remote
         re-pin needed. **SV W25 = the D.O. original-print wave
         (controller-direct, owner-directed full sweep after D.O. www
         recovered same day):** 12 acquisitions `115_-126_` — the D.O.
         original gazette prints of the nine W21/W22 instruments
         106_-114_ (8 issues; 120_ preserves the AS-ENACTED 2023
         Art.-10 gratuidad vintage vs 111_'s consolidated reprint) +
         the COTRANS chain limbs D.L. 307/617/1000 TEXT-OWNED as
         124_/125_/126_ (EVID-413..415; **Art. 17-A provenance
         RESOLVED — 617 is the creator**; chain fully instrument-text
         end-to-end 89_→124_→125_→126_→106_) + **SOQ-31 CLOSED
         negative-CONFIRMED** (the full D.O. window scan 23-sep→
         23-dic-1998 — 65 issues, two OCR passes each, no Reglamento
         General Ley-ZF ever printed; MINEC-practice corroboration).
         **FR corpus UNCHANGED at 1,730 (sources wave); registry 124
         file rows, next 127; COVERAGE 90/9/2/24 of 125 gate green**
         (+12 provenance-class pending rows, rationale in
         COVERAGE_NOTES). MH formularios re-pinned same sweep (new
         landing `/servicios/formularios-tributarios-para-descarga/`,
         NO drift — F-11 v18/F-14 v17 current). D.O. route intel:
         web prints are body-raster (headers-only text layer) — locate
         instruments by single-page OCR probes; sumario p.1-2 as
         index; use the www base (apex still 000). sv worktree
         converged to main at close.

       **SV W26 merge 2026-08-24 (§4.6 protocol, forty-seventh
         run):** `sv-research` rebased onto `6121d42` (a NO-OP — main
         unmoved since the W25 merge, so the 9 session commits
         `a56c2a1..c74770c` stand UNREWRITTEN) then
         fast-forward-merged at the W26 close `c74770c`; plain
         fast-forward push, no remote re-pin needed. **SV W26 = the
         rides + hygiene wave (controller-direct, owner-directed
         consolidation per plan
         `docs/superpowers/plans/2026-08-24-w26-rides-hygiene-wave.md`):
         every open ride in sv/HANDOVER §8.1's residual list
         EXECUTED with ZERO corpus deltas** — W23 cml minors (strict
         "225..242 + 246" glosses ×3 surfaces; LB-034 [sic]; LB-018
         de-quote; Art.-338 double-verbatim collapsed at LB-033;
         LB-039 transitorio numerals 3-4; six >80-char rewraps) + W24
         spe/taxation minors (window_kind canonical tokens
         spe-corpus-wide; AC-015 ws; FR-417 two-layer window sketch;
         taxation/03 §5 cells → §4 field vocabulary) + the W25 spe/08
         ride (FR-189/LB-012/config-row/preamble/OQ-8 chain provenance
         → text-owned 124_/125_/126_, all recital hedges dropped) +
         W19 stragglers (spe/04 OQ-1 flipped resolved — LESIA 79_;
         spe/01 OQ-3 + spe/07 OQ-4 flipped resolved-negative — SOQ-31
         W25 propagation, caught by the proof grep; six coa OQ rows'
         stale "≥75" refreshed; spe OQ legend 48 open/12 resolved) +
         C1 hygiene (frep/04 LB-009 full registered source stem +
         COVERAGE_NOTES retirement + regen; EV-bank A1 estas→esas +
         the coa/01 LB-002 kin; coa/01 LB-004 PAGE 48-53;
         build_catalogs.py preserves the _INDEX corrections-log on
         regen). **Corpus 1,730 FRs UNCHANGED / same LB-AC counts;
         COVERAGE 90/9/2/24 of 125 gate green (no drift); registry
         UNCHANGED (124 file rows, next 127).** No-action rides
         documented (verify-or-document); 111_-touch chapter-spine
         residual recorded (305-C/305-I/305-T). SV program residual =
         SOQ-46 criteria hunt + external watches (uif AML deadline
         2026-10-17) + census watch + go-live prep. sv worktree
         converged to main at close.

       **SV W29 merge 2026-08-24 (§4.6 protocol, fiftieth
         run):** `sv-research` rebased onto `912cdde` (a NO-OP — main
         unmoved since the W28 merge-record close, so the 7 session
         commits `b102b1c..04ed7fa` stand UNREWRITTEN — design spec
         → plan → assessment → citation fixes → review fixes +
         register flip → bookkeeping → whitespace fix) then
         fast-forward-merged at `04ed7fa`; plain fast-forward push,
         no remote re-pin needed. **SV W29 = the SV go-live readiness
         assessment wave (first wave of the post-program
         implementation-prep phase, owner-directed per
         `shared/docs/go-live-readiness.md`'s register-verification
         mandate; hybrid process per the approved design
         `docs/superpowers/specs/2026-08-24-w29-sv-go-live-readiness-design.md`
         + plan, subagent-driven T1-T5 with per-task reviews + a
         Task-3 independent reviewer + final whole-branch review
         MERGE-READY zero findings): (1) NEW
         `sv/requirements/GO_LIVE_READINESS.md` = the universal-catalog
         walk against the corpus — 21 rows (bootstrap 5 + cut-over 6 +
         onboarding 6 + register 4), graded statuses
         VERIFIED/CONFIG-GAP/WATCH/BLOCKER, gate rollup 13 VERIFIED ·
         6 with-limb · 2 BLOCKER rows = ONE root; (2) the shared-docs
         §4 SV instantiation register FLIPPED "seeded 2026-08-19" →
         "verified 2026-08-24" with pointer to the assessment;
         (3) HEADLINE FINDING: the S1 synthesis wave NEVER
         synthesized master-index cluster A11 (onboarding/
         authorization — acreditamiento minimum tests, AT
         authorization groups/dates + early adoption, physical-stock
         destruction, no-coexistence; 8 governing EVIDs
         001/036/045/080/081/077/074/083 owned-but-unsynthesized;
         EVID-081 grep-zero in requirements; the S1 plan's file list
         records NO deferral — silent omission, not a decision; 9
         exhaustive dangling "(A11)" pointers + cml cross-topic
         notes + COVERAGE/COVERAGE_NOTES 26_ rows; GT S-GT1 Task 5
         04_mandate-onboarding.md = the precedent) ⇒ **gate verdict:
         NOT go-live-ready until the A11 onboarding file is minted
         (single closing wave; numbering per R30(b) SV-EINV
         continuation; recorded as the TOP owner's-call follow-up in
         sv/HANDOVER §8)** — everything else VERIFIED / CONFIG-GAP /
         WATCH (6 WATCH limbs incl. F-11 v19/v20 + F-14 v17 manual,
         cert renewal OQ-006, AML reglamento 2026-10-17, MOQ-05
         endpoints promoted at review; canonical CONFIG-GAP list
         RAEX/SOQ-26/SOQ-25/SOQ-24/OQ-10/OQ-007/SOQ-33/usos-del-lugar).**
         W29-process rulings (a)-(e) preserved in sv/HANDOVER (brief-
         arithmetic matrix-lesson; curated-canonical WATCH list;
         W24-(g) sampled-reproduction standard; controller one-liners
         per S9 (b); verify-or-document minor). **ZERO corpus deltas:
         FR corpus 1,732 UNCHANGED; registry 126 file rows next 129;
         COVERAGE 92/9/2/24 of 127 gate green (no drift, re-verified
         post-merge).** SV residual = the A11 synthesis wave (owner's
         call) + external watches (uif AML deadline 2026-10-17; D.O.
         feed stall; MH formularios; cvpcpa cadence) + census watch.
         sv worktree converged to main at close.

       **SV W28 merge 2026-08-24 (§4.6 protocol, forty-ninth
         run):** `sv-research` rebased onto `647faa0` (a NO-OP — main
         unmoved since the W27 merge-record close, so the single
         session commit `f7c2f71` stands UNREWRITTEN) then
         fast-forward-merged at the W28 close `f7c2f71`; plain
         fast-forward push, no remote re-pin needed. **SV W28 = the
         SOQ-46 re-probe sweep + 128_ acquisition mini wave
         (controller-direct, owner-directed hunt re-probe): (1) the
         SOQ-46 hunt re-probed at FULL-ENUMERATION strength — the
         entire cvpcpa publication record triaged (media library
         1,082 items / 11 pages, all 32 PDFs; all 13 resolución
         posts; keyword searches pymes/niif/norma contable/umbral/
         criterio = ZERO hits); every resolution 2021-2026
         dispositioned criteria-negative (Res. 111-2025 aranceles +
         159-2025 ethics = the D.O.-published Aug-2025 pair; Res.
         83/84-2024 fees/services; Res. 275/237-2023 AML, 237 now
         derogated by 128_; the site's LREC Reglamento PDF = an
         UN-ENACTED DRAFT with zero framework content) ⇒ SOQ-46
         negative at full-enumeration strength on the primary
         surface, watch rides cadence unchanged (fallback surface =
         the transparencia.gob.sv LAIP deposit, JS app, route
         undiscovered); (2) 128_ = Resolución CVPCPA 111-2026
         ACQUIRED (27-feb-2026, Acta 10/2026; sha256-verified;
         EVID-419..420) — the D.L. 426 supervisor-side Art.-58
         diagnostic requirement + the EXPRESS no-lineamientos
         statement (strongest supervisor-side OQ-001 datum) + the
         12-month window re-cited (⇒ 2026-10-17 corroborated) + Res.
         237-2023 derogation; cml/10 LB-031 minted ON ARRIVAL (zero
         fold-in debt).** Same-session D.O. re-probe: gazette feed
         STILL stalls at 10-ago-2026 (Ids 31815/31816 unchanged —
         the successor-legislation + AML-reglamento D.O.-sumario
         routes gated on the stall clearing). **Corpus 1,732 FRs
         UNCHANGED / cml 248-260-144-35 (LB-031 only); COVERAGE
         92/9/2/24 of 127 gate green (128_ cited on arrival);
         registry 126 file rows, next 129.** SV program residual =
         external watches (uif AML deadline 2026-10-17, now
         instrument-evidenced by 128_; D.O. feed stall; MH
         formularios; F-11 v19/v20) + census watch + go-live prep.
         sv worktree converged to main at close.

        **SV W27 merge 2026-08-24 (§4.6 protocol, forty-eighth
         run):** `sv-research` rebased onto `f3e66ab` (a NO-OP — main
         unmoved since the W26 merge, so the 3 session commits
         `ec149e0..1b43569` stand UNREWRITTEN) then
         fast-forward-merged at the W27 close `1b43569`; plain
         fast-forward push, no remote re-pin needed. **SV W27 = the
         chapter-spine mini wave (controller-direct, owner-approved
         bounded design): (1) the W26-recorded 111_ residual EXECUTED —
         cml/04 LB-041..043 (305-C accionista-not-employee / 305-I
         Registro-issued inscription-certificate proof / 305-T
         awareness) + SV-CML-FR-247 (contract-gated accionista→employee
         link, payroll consumes by id) + FR-248 (the inscription
         document = the SAS documentary-proof interface) + AC-021/022 —
         the 305-A..Z citation spine COMPLETE; (2) the SOQ-46 hunt
         DISPOSITIONED — Res. 175-2023 closed-negative (text not
         acquirable; successor 76_ has no criteria content); Res.
         82-2024 ACQUIRED as 127_ (cvpcpa wp-json, EVID-416..418) = the
         NIIF S1/S2 voluntary window (1-ene-2025) + the NIIF-PYMES
         S1/S2 bar — PRESUMES the classification, so SOQ-46 residual =
         negative watch only; coa/01 LB-008 awareness/config-off.**
         Same-session external sweeps (commits ec149e0/8eceda1):
         factura NO drift (schemas zip byte-identical to 52_); MH NO
         drift; D.O. www+API serving but the gazette feed STALLS at
         10-ago-2026 (partial recovery — re-probe before any
         2026-instrument hunt); uif WAF blocks human browsers too — no
         2026 AML reglamento evidenced (deadline 2026-10-17 stands).
         **Corpus 1,732 FRs (+2) / cml 248-259-144-35 / coa LBs 58;
         COVERAGE 91/9/2/24 of 126 gate green (127_ cited on arrival);
         registry 125 file rows, next 128 (stale sv/README W22 count
         fixed).** SV program residual = external watches (uif AML,
         D.O. feed, MH formularios, F-11 v19/v20) + census watch +
         go-live prep. sv worktree converged to main at close.


       **GT W-GT10 merge 2026-08-23 (§4.6 protocol, forty-second
       run):** `gt-research` rebased onto the SV-W22 tip `8fe7854`
       (4 commits rewritten `051a276..026df77`→`9758f59..c259fc1`,
       one clean pass, zero conflicts — gt/-scoped) then
       fast-forward-merged at the rewritten W-GT10 close; remote
       gt-research updated via delete + re-push. **GT = JD-LIBRARY
       HUNT + RECAUDACIÓN-REFORM/EXONERACIÓN WAVE COMPLETE (corpus
       113→115 rows, COVERAGE re-closed 115/0/0):** hunt for the
       queue-rev-12 top item (SEM/accidentes operative-rate
       instruments) executed controller-side over the full
       igssgt.org JD-library listing — **VERDICT NEGATIVE (EVID-1329):
       no Acuerdo 475, no rate-setting title among ~500; library
       "1243" = 2010 SEM extension (W-GT9 rejection stands);
       /cuotas/ login-gated; residue → owner-browser DCA-archive
       route only (queue rev 13)**. Two bonus acquisitions
       (controller direct fetches): **116_ = JD Acuerdo 1520 + AG
       239-2022 — THE 2022 REFORM of recaudación reglamento Acuerdo
       1421 (= 87_, now layer-dated): arts. 4/5 reformed + art. 9 ¶3
       added; floor redefined as monto base = OE SMM (jornada diurna,
       ≥8h/día, by activity) × 243.3333/30.4167/1.00 with
       patrono-borne top-up; the FIRST printed program-distribution
       proportions table (EMA/Acc/IVS + non-IVS variant) recorded
       CORROBORATION-ONLY (×15.50% ⇒ EMA 4/2 + Acc 3/1, IVS 3.67/1.83
       exact — the folk "12.67" mechanically explained yet the
       12.67/4.83 rejected-prior verdicts STAND; percentages remain
       delegated to "normativa institucional" — GOQ-04 rate residue
       UNCHANGED, base-floor half now FORMULA-ANCHORED); effective
       29-sep-2022** + **117_ = JD Acuerdo 1556 + AG 17-2026 — the
       standing 100% recargo-exoneración window (lineage
       1200→1504/1519→1556; ≈25-mar→25-sep-2026 computed, OPEN at
       session date; planilla-electrónica preconditions; oficio
       annulment of recargo-only cobros; dación en pago) modeled as a
       D15/D16 dated-regime overlay (payroll/07 FR-182), never a
       fifth reglementary waiver case**. EV10 = EVID-1306..1329
       (controller-written); backfills payroll/07 LB-028/029 +
       FR-165/169/182/183 + payroll/10 LB-011 addendum + payroll index
       totals 167→169 (stale W-GT8-era 07-row cell fixed). Tooling
       gap recorded: build_coverage.py --check RED for GT by
       construction (SOURCE_RE expects SV-style backticked registry
       cells) — GT COVERAGE stays hand-maintained; fix parked for the
       next maintenance pass. GT worktree clean at the merge point; no
       wave queued — next inputs owner-side (DCA-archive rate hunt,
       D-1633 art.-11 montos, AG 52-2017 low watch, accountant,
       TotalDoc W6, 1556-window expiry ≈25-sep-2026). **Note: this
       commit also carries the SV W22 forty-first-run record above,
       which the parallel SV session left UNCOMMITTED in the main
       checkout at its close (their merged commit 8fe7854 rides this
       push).**

       **GT W-GT8 + W-GT9 merge 2026-08-23 (§4.6 protocol, fortieth
       run):** `gt-research` rebased onto `4be5347` (12 commits
       rewritten `ff027bc..895e452`→one clean pass, zero conflicts —
       gt/-scoped) then fast-forward-merged at the rewritten W-GT9
       close; remote gt-research updated via delete + re-push.
       **GT = BATCH-3/4/5 + IGSS-JD-LIBRARY WAVES COMPLETE (corpus
       94→113 rows, COVERAGE re-closed 113/0/0):** W-GT8 (96_–101_ +
       103_–108_: AML reglamento AG 118-2002 primary, US$10,000 sole
       threshold, AG 75-2006=SINAS hypothesis DEAD; D-1633 standing
       public aguinaldo with art.-11 quantum external; D-37-2001
       incentivo primary; IVA 27-92 consolidated ~2019 → GOQ-01
       resolved-composite; Cap. VIII/IX = D-7-2019 RECA/electrónico,
       sunset 2025-08-09 → GOQ-146/107 resolved; SAT Calendario 2026
       ×8 FLAT, no NIT-digit windows → GOQ-14/145 re-scoped; SEM 410
       set rateless). W-GT9 (owner found the IGSS JD library
       igssgt.org/acuerdos-y-resoluciones — fetches direct; 109_–115_:
       **GOQ-04 IVS-rate half RESOLVED — Acuerdo 1124 art. 40 =
       3.67% patronal + 1.83% laboral = 5.50% payroll pair, Estado
       25% = of benefits**; program-family map pinned
       410/468/466/1002/1124/1118/1135-staff-excluded; residue =
       SEM/accidentes operative rates via the 410 art.-85 chain
       475→1243, queue rev 12). GT worktree clean at the merge
       point; no wave queued — next inputs owner-side (JD-library
       SEM/accidentes hunt, D-1633 art.-11 montos, AG 52-2017 low
       watch, accountant, TotalDoc W6).

       **SV W20 merge 2026-08-23 (§4.6 protocol, thirty-eighth run):**
       `sv-research` rebased onto `eb59e17` (11 commits rewritten
       `81e0906..1cce46d`→`bcd4a4f..1912d6a`: W20 plan + prep + T1..T5
       + T1/T4 fix rounds + fix-wave/close commits; TWO textual
       conflicts on the T5 bookkeeping + W20-close commits vs the
       main-side W19 merge record `eb59e17`, both resolved keep-both)
       then fast-forward-merged; remote branch ref fixed via delete +
       re-push. **SV = W20 TAXATION EDIT WAVE COMPLETE (corpus
       1,690→1,702 FRs):** the three W19 follow-up debts executed —
       **96_ D.L. 308-2025 Chapter V fold-in** (NEW
       `taxation/17_foreign-agents-levy.md`, cluster L1, SV-TAX-FR-
       405..416: 30% levy on mandante-financed transactions, two-limb
       Agentes de Retención Especial scope — SSF general + NPO-qualified
       catch-all —, DGT enteros 10 días hábiles, reports 15, monthly
       donation self-entero, CT 246/247/241 sanctions + supletorio;
       spe/01 OQ-6 + EV OQ-2 resolved-by-pointer; SOQ-41 Chapter-V half
       consumed); **SR8 rewire** (taxation/09 COTRANS rows anchored to
       89_, FR-245 gate satisfiable — SOQ-39/MOQ-04 chain closed);
       **2025+ standing-rule mirror** (taxation/04 aguinaldo vintages
       instrument-anchored to 91_-94_ per payroll/04 LB-023; OQ-003
       resolved — 2025+ standing 2-SMM chain-verified EVID-403; R22 +
       SOQ-05 verdicts appended). Corpus: taxation dir 416 FRs / 305
       LBs / 283 ACs / 91 OQs; COVERAGE 81/9/2/12 of 104, gate green
       (96_ curated note refreshed to W20 ownership); registry
       UNCHANGED (103 files, next 106). Process: T1 quote-fidelity
       ruling (txt-normalized "sin deducción" governs over the EV
       artifact; EVID-397 hygiene landed per S9 ruling (g)); T1
       implementer rejected 2 reviewer prescriptions on txt evidence
       (upheld); T4 curated-note refresh reviewer-sanctioned; 8 W20
       rulings preserved in sv/HANDOVER §5. Final whole-wave review
       USABLE-WITH-FIXES → one fix wave PASS = MERGE-READY. **SV
       remaining: residual acquisitions (SOQ-46 criteria instrument;
       D.L. 201-2025 + 411-2025 anchors; COTRANS Aug-2025 prorroga
       decree), external watches (D.O./uif DNS-down since 08-22; AML
       2026-10-17), SR8 residual (taxation/09 OQ-2 design
       confirmation), go-live prep.**

       **SV W19 merge 2026-08-23 (§4.6 protocol, thirty-seventh run):**
       `sv-research` rebased onto `bde7cfa` (15 commits rewritten
       `e86e100..c188c6c`→`6ab5a6a..33deaaa`: W19 plan + T1..T8 +
       T1/T3/T4 fix rounds + T3-fix2/close/fix-wave commits; ONE
       textual conflict on T8's sv/HANDOVER §1/§8 edits vs the
       main-side `56ee669` (W18 merge record), resolved keep-both) then
       fast-forward-merged; remote branch ref fixed via delete +
       re-push. **SV = W18 FOLD-IN/EVIDENCE WAVE COMPLETE (corpus
       1,662→1,690 FRs):** the 16-file evidence backlog consumed —
       **five EV files, EVID-359..403 gapless** (LESIA+124-2015 tasa /
       FOVIAL-COTRANS instruments / LSI-277+ZF-493 / 95_+96_+97_
       incentives / 90_-94_ transitories); **SV-SPE-FR-176..203 (+28)**
       across spe/01/02/06/07/08; **14_→80_ LSI re-key = 38 LB columns
       + 47 inline, 0 survivors** (12m-ZF vs 24m-LSI clock invariant
       re-verified HOLDS); ZF 493-2025 tail folded (Arts.
       2/10/11/17/18/19/28/44/46-A/54-B/54-I + 2-yr grace); COTRANS
       passenger-identity + $0.20=D.L. 597-2001-Art.26 provenance
       landed in SR8 + e-invoicing FR-046/CAT-015 glosses (**MOQ-04
       CLOSED**); aguinaldo-cap vintages re-anchored to 91_-94_
       (values byte-identical); **95_ horizon TEXT-PINNED 15 años**
       (Art. 3 inc. 2); **SOQ-32/34/39/56 consumed, 36/46/58 refreshed
       (stay open), 30 narrowed; SOQ-56 = BCR-list membership (OQ-2
       resolved)**; **96_ Chapter V = REAL 30%-withholding surface
       discovered (plan hypothesis refuted) — routed out-of-wave to a
       future taxation wave** (spe/01 OQ-6 + SOQ-41 + FR-201 pointers).
       COVERAGE regen: **81 cited / 9 N-A / 2 superseded / 12 pending
       of 104** (18 flips + 14_→superseded, gate PASS). External
       checks: factura 200 / MH unchanged / **D.O. + uif.gob.sv
       DNS-level outage since 2026-08-22** (no A record, DoH-verified;
       AML watch deadline 2026-10-17 = 71_ 12-month adaptation).
       Registry fix: §89 compensation figures $250/$500 per the print.
       Final whole-wave review USABLE-WITH-FIXES → one fix wave PASS
       (master-index stale authority claims cleared) = MERGE-READY.
       Next per `sv/HANDOVER.md` §8: SR8 rewire backlog, 96_ Chapter V
       taxation fold-in, taxation-side 2025+ standing-rule mirror,
       residual acquisitions + external watches.


      **SV W18 merge 2026-08-22 (§4.6 protocol, thirtieth run):**
      `sv-research` rebased onto `adcd528` (13 commits rewritten
      `6d0875c..dbf0cc5`→`87b4b4e..f7fb42a`: W18 plan + T1..T8 +
      T4/T6 fix rounds + close/COVERAGE commits; ONE textual conflict
      on T8's sv/HANDOVER §1 edit vs the main-side-only `27b5d0a`
      (C1 merge parenthetical), resolved keep-both) then
      fast-forward-merged; remote branch ref fixed via delete +
      re-push. **SV = W18 ACQUISITION FOLLOW-UPS WAVE COMPLETE
      (sources only — 1,662 FRs unchanged; registry 73→103 files,
      30 acquisitions `76_`..`105_`, next numbering 106):** CVPCPA
      NIIF authority chain `76_`-`78_` (Res. 154-2024 + Res. 462-2021
      + Ley Reguladora D.L. 828/646 — **SOQ-46 PARTIAL**: chain owned,
      PYMES-vs-full criteria instrument still hunted); customs/regime
      set `79_`-`85_`: **LESIA D.L. 551-2001 (SOQ-32 CLOSED)**, LSI
      consolidation thru D.L. 277-2013 `80_` (**supersedes `14_`**,
      Arts. 5/6/8/23/24 changed), MH Recopilación `81_`, **ZF reform
      D.L. 493-2025 `82_`** (post-`12_`-consolidation), FYDUCA
      res/format/glossary `83_`-`85_` (SOQ-36 partial: manual
      Portal-internal; Res. 409-2018 NOT superseded); fuel set
      `86_`-`89_`: FOVIAL law consolidation + D.O. prints ($0.20/gal
      = the D.L. 597-2001 Art. 26 REFORM, not the 2000 original) +
      **COTRANS = D.L. 257-2021 passenger-tariff contribution
      $0.10/gal thru 31-dic-2026 (IDENTITY CORRECTION vs the
      transportistas-de-carga gloss — SOQ-39 RESOLVED, MOQ-04
      instruments half closed)**; ISR-tail set `90_`-`100_`: D.L.
      598-2020 (**SOQ-41 CLOSED**), aguinaldo-cap chain D.L.
      229-2021→159-2024 ($1,100→$1,500), D.L. 95-2024/308-2025/386-
      2025, **DACG tasa prints 2015+2025 both $18.00 (SOQ-34 RESOLVED
      — never adjusted, documentary supersession)**, D.L. 124-2015
      (**74_ Art. 12-B parity break — SOQ-30 annotated W18**); Art.
      46-f BCR set `101_`-`105_` (DGII+BCR joint Instructivo
      CD-39/2021→CD-24/2023 + live qualification lists — **SOQ-56
      RESOLVED**: exemption flag = BCR-list membership). **SOQ-54
      Rgto RESOLVED-AS-PARITY** (TF DC5855 ≡ `02_`, two-official-copy
      pattern); SOQ-31 Rgto-ZF NEGATIVE (never-issued hypothesis);
      48/58 negative-refreshed. T1 external checks: no factura/MH
      drift; **uif.gob.sv WAF-blocked from 2026-08-21** (AML watch
      interrupted, 2026-10-17 deadline); **D.O. API recipe PINNED**
      (form-encoded year/month). Route recipes proven in-wave: TF DC
      catalog via Wayback CDX; SIECA S3 presigned URLs. COVERAGE
      regen: 64/30/9/1 of 104 rows (30 pending-S2+ until their
      evidence/fold-in waves cite them — W16 `75_` precedent); gates
      PASS. Final whole-wave review MERGE-READY (zero C/I; deferred
      minors triaged ride/ignore — SOQ-30:705/SOQ-39:714 rendering
      nits + 95_ reads ride to W19). Next per `sv/HANDOVER.md` §8:
      W19 fold-in/evidence wave (`82_`+`80_`+`79_`+`89_`/`86_`
      special-regimes/taxation edits + 16-file evidence backlog),
      residual acquisitions (SOQ-46 criteria instrument), external
      watches.

      **SV C1 merge 2026-08-21 (§4.6 protocol, twenty-seventh run):**
      `sv-research` rebased onto `d29c226` (15 commits rewritten
      `70f86f9..71d2f6d`→`89879bd..289017e`: C1 plan + T1..T11 + fix
      wave + HANDOVER verdict; zero conflicts) then fast-forward-merged;
      remote branch ref fixed via delete + re-push. **SV = C1
      consolidation/cleanup wave COMPLETE** — the CAN-STAND/rides
      burn-down with ZERO substance changes: per-wave deferred minors
      (S3 13/15 fixed, S4 9/11, S5 9/9, S7 AC-007 Given-gap, S8 rides
      w/ one fix round — PAGE 162 anchor; W17 rides incl. FR-213 by-id
      to taxation/16 **LB-013** (brief's LB-012 = plan defect) + FR-372
      anchor-map fold + LB-017 "awareness only"), **43-instance
      "only architecture-split surface" boilerplate sweep** (taxation 8
      + non-taxation 35; spe/08:295 file-scoped variant correctly left),
      **T9 catalogs workbook-sole-source alignment** (SV-CAT-FR-002;
      overlay path removed; 33 CSVs byte-identical), **T10
      `shared/scripts/build_coverage.py`** + COVERAGE_NOTES sidecar
      (`--check` gate; 13 under-listed citing sources corrected;
      statuses 64/9/1/0 exact), e-invoicing UUID/AC-011/OQ-005 rides,
      root §9 per-item RESOLVED-C1 annotations (stays: D4 ToS backlog,
      04 OQ-006 legitimately open). Corpus delta verified mechanically
      by final review: **+OQ-007 (frep/03) only; 1,662 FRs unchanged**.
      10 content-task reviews Approved (T6 after one fix round) + final
      whole-wave USABLE-WITH-FIXES + one fix wave PASS (re-review
      APPROVED). S9 RIDE ledger unrecoverable (workspace deleted;
      recorded verdict "nothing load-bearing"). Next per
      `sv/HANDOVER.md` §8: owner's call — acquisition follow-ups
      (SOQ-46 NIIF instrument = gating), external watches, or go-live
      prep.

      **SV W17 merge 2026-08-20 (§4.6 protocol, twenty-third run):**
      `sv-research` rebased onto `c297853` (7 commits rewritten
      `562a3e3..f528181`→`37778b3..c42a600`: W17 plan + T1..T5 + fix
      wave + HANDOVER verdict; zero conflicts — sv/-scoped or new files
      only) then fast-forward-merged; remote branch ref fixed via delete
      + re-push. **SV = W17 75_ (D.E. 117-2001 CT application reglamento)
      FOLD-IN COMPLETE** — the queued W16 follow-up: NEW
      `taxation/16_ct-procedures.md` (SV-TAX-FR-354..396; 43 FRs/41 LBs:
      clocks vocabulary, representation/domicilio, registration, the
      Art. 31-35 declaration-state model + CT 103 amendment gate,
      payments/extinction, compensación, **the Art. 23/133 retention
      imprescriptibilidad/caducidad pair**, refunds, sanctions, books,
      fiscalización, print-era historical blocks per EV75 OQ-3/OQ-4
      bars) + taxation/04 397..400 + 13 401..404 + 01 OQ-001 RESOLVED
      (75_ Arts. 99-100 corroborate Ley Art. 62) + fiscal-reporting/01
      213..214 + 06/07/08 notes (SOQ-08 Art. 100 anchor CONSUMED;
      dictamen historical) + payroll/08 144..147 + 04 note. Registry
      corrective fold: 02_ survivors = 1-10, 16-26, 29-30, 50-51 (+52
      spent) — EVID-358 audit supersedes the "36/45 survive" gloss.
      Corpus 1,662 FRs (TAX 404 / FREP 214 / PAY 147); COVERAGE 64
      cited / 0 pending / 9 N/A / 1 superseded — **all 74 rows
      terminal-state, zero pending**. All 5 task reviews Approved
      first-pass + final whole-wave USABLE-WITH-FIXES + one fix wave
      (re-review PASS). Next per `sv/HANDOVER.md` §8: owner's call —
      consolidation/cleanup wave (CAN-STAND + S7/S8/S9 RIDE lists),
      acquisition follow-ups (SOQ-46 NIIF instrument = gating), or
      go-live prep.

      **HN W7 merge 2026-08-21 (§4.6 protocol, twenty-fourth run):**
      `hn-research` rebased onto `b881f87` (2 commits rewritten
      `18aea5c..f0b0e92`→`c0d4049..d4b2a49`: W6-merge branch record +
      W7 residual-chain decode; zero conflicts — hn/-scoped only)
      then fast-forward-merged; remote branch ref updated via delete +
      re-push. **HN = W7 RESIDUAL-CHAIN DECODE COMPLETE (corpus 118
      files, evidence through EVID-433):** the four 1990-1995 TEXTS
      (D. 36-90 / D. 54-95 / D. 74-95 / D. 247-89) remain unacquired
      (routes A-D exhausted: congreso CDX full-domain incl. a SECOND
      library `leyes nacionales/` + GLIN date-coded archive + `Codigos/`;
      TSC live 2026-redesign + CDX 12k PDFs; STSS/trabajo CDX 2,411
      PDFs — two fetches md5-identical to 102_/105_, discarded; SAR
      wp-search posts-only) — but the chain DECODED via **`119_` = the
      official congreso "Inventarios de Leyes"** (text-native 559-pp
      thematic inventory, Wayback of congreso.gob.hn/decretos/;
      EVID-429..433): **R-H81** — the W4 102_/payroll OQ-002 "conflicting
      D. 54-95 citations" = TWO decrees: the Art.-34 interp = **D. 74-95**
      (G 27,655 18-may-1995; the W4 footnote read "54-95" was an OCR
      misread — EVID-238/LB-002 fixed with dual-dpi 300/600 proof) and
      the jubilados/pensionados extension = **D. 54-95** (G 27,639
      28-abr-1995; the book's "28,639" = digit-swap; monotonicity
      27,587 (Acuerdo 02-95's own NEW pin) < 27,639 < 27,655 arbitrates)
      → payroll/02 FR-057 re-attributed + FR-097 dated beneficiary row
      (gap range 097-100) + LB-025 + AC-022 + 14m.config dated rows,
      OQ-002 RESOLVED (OQ-012 unchanged — D. 54-95 content is
      extension-only, does not arbitrate the D. 135-94 vigencia
      conflict); **R-H82** — D. 36-90 = G 26,131 11-MAY-1990 (the
      inventory's "11-abril" = its own slip; payroll/06 LB-014 +
      FR-248/249 pinned) and D. 247-89 = G 26,028 6-ene-1990 (CT-120
      cesantía amplification — the ONE text still quote-nowhere = live
      residual, genealogical since 86_ integrates its effect;
      payroll/08 LB-007). Bonus: RIT ancestor identified (Acuerdo
      166-JD-76 + reform 003-82JD, both G 25,013 30-ago-1986); D.
      215-92/D. 40-89 genealogy banked; standing caution = inventory
      gazette digits slip (discovery source only). Verification:
      bank-check 23/23 Spanish legs vs the text layer + 5/5 glyph
      probes vs 600dpi; structural payroll/02 47/25/22/13 = index.
      Payroll 327/164/171/83; rulings R-H1..R-H82; COVERAGE 118 rows =
      116 cited + 2 N/A, gates PASS (1095/503/574/325). Next per
      `hn/HANDOVER.md`: post-W6 queue (TOP: Acuerdo 799 Reglamento Ley
      ISR, Reglamento General IHSS, Ley RAP D.L. 107-2013, D. 51-2003;
      then D. 314-98 watch, post-1995 selectivo chain, D. 99-93, 95_
      clean-consolidation lead, D. 247-89 text watch); S-HN5 DEFERRED —
      bootstrap `Read hn/HANDOVER.md and continue.`

      **HN W8 merge 2026-08-21 (§4.6 protocol, twenty-fifth run; branch
      record completed 2026-08-21 same-day sweep at `261b27b` — the
      branch-side hn/HANDOVER record commit `98cb5b1` was rebased onto
      `c1aefe1` post-GT-S-GT5-merge and fast-forward-merged in):**
      `hn-research` rebased onto `380f044` (2 commits rewritten
      `7a47fe8..221ce4a`→`2012b6a..2006f04`: W7-merge branch record +
      W8 acquisition wave; zero conflicts — hn/-scoped only) then
      fast-forward-merged; remote branch ref updated via delete +
      re-push. **HN = W8 POST-W6 ACQUISITION WAVE COMPLETE (corpus 128
      files, evidence through EVID-481):** TEN files `120_`..`129_`
      registered + evidenced (48 EVIDs across 6 dispatched/controller
      files + a 119_ addendum): `120_` **Ley RAP D.L. 107-2013 ORIGINAL**
      (G 33,222 6-sep-2013, recovered via the Wayback of rap.hn's own
      dead pdf/leyrap1.pdf — the doubly-load-bearing lead CLOSED;
      R-H85: original Art. 42 = 10-empleado/FOSOVI-unregistered gate,
      Art. 43 = "El Patrono aportante" 1.5+1.5=3% on FULL salario
      mensual ordinario ≤15 días — the IVM-excess base + ceiling = 2024
      inserts, pre-reform percentages identical, D. 167-91 exception
      deleted by the reform, and 47_'s transcription ellipsis = the
      original's exact end → COMPLETE → payroll/05 OQ-003/OQ-006
      RESOLVED, FR-216/LB-016/AC-019 dated rows across the 2013→2024
      boundary); `121_` **D. 51-2003 LET** (G 30,059 10-abr-2003;
      R-H84: ATN = Cap. II Arts. 5-16 — 1% Art. 7, PJ-comerciantes
      Art. 5, L3M EXCESS-ONLY Art. 14.1, ATN-as-ISR-credit Art. 15 →
      FREP/07 OQ-010 RESOLVED, FR-257 statute-anchored; **AS Art. 22 =
      "temporal"… "hasta el año 2005"** → the CURRENT FY2014+ AS needs
      its re-establisher — refined lead D. 278-2013, shared with the
      devolución-8% Arts. 20-21 residual; Art. 18 = ISV-tarjetas
      retention-agent origin; Art. 28 = Registro Fiscal de Imprentas;
      Art. 44 = cooperative-mercantile origin (506/509-boundary
      bookend); D. 54-96 NOT among the Art. 56 derogations — negative
      finding) + `122_` Acuerdo 0948-2003 (the LET reglamento = the
      67_-cited "reglamento del ATN", gazette 28-jun-2003) + `123_`
      D. 52-2004 (Art.-49 interp); `124_/125_/126_` **turismo family**
      (314-98 G 28,847; 135-2006 cruise class; **68-2017 G 34,419
      17-ago-2017 = CURRENT statute, DEROGATES 314-98**; Art. 21 = the
      tasa-turística cobrar-retener-enterar ≤10-primeros-días
      procedure — creation/rate stay D. 131-98 Art. 43 untouched,
      grep-verified negative; taxation/07 FR-282/LB-011);
      `127_` **Acuerdo 005-2017** (selectivo/production-consumption
      reglamento, G 34,282 6-mar-2017, TEXT-NATIVE; import formula
      ISV=(CIF+DAI+ISC+IPC)t; image-only rates cuadro + an Arts.
      18/20-vs-19 ISC contradiction = OQs; FREP/09 LB-013/014, OQ-001
      procedure leg closed); `128_` D. 99-93 (FX-repatriation, gazette
      9-jul-1993 = the código-115 exclusion mechanism; FREP/02 FR-073/
      LB-019, OQ-009 mechanism pinned); `129_` **D. 74-95 TEXT** (G
      27,655 May-1995 — found in the W6 leyesdir.cdx the W7 hunt never
      re-grepped: standing lesson = re-check EVERY saved CDX
      enumeration before declaring exhaustion; the Art.-34 interp
      verbatim = exactly the R-H81 decode; payroll/02 FR-057/LB-026
      statute-anchored). **R-H83** — the five-times-cited "Acuerdo
      N°799" identity-DECODED via 119_ entry 324 (EVID-479): = the ISR
      reglamento of **1970**, G 19,972 13-ene-1970 (+6-B Art. 33 patch
      G 21,505 4-feb-1975; 31_'s "799-1963" = manual slip; text stays
      unacquired — 1970 gazette, pre-ENAG; five consumer OQs
      annotated); NEW lead Acuerdo 1515-2003 (second LET reglamento,
      119_ entry 1035); the 119_ IHSS block carries NO Reglamento
      General (one more route exhausted for that TOP lead).
      Verification: EVID structural 48/48 contiguous + accent-
      insensitive 3-gram bank-check (LOWs adjudicated: English-gloss
      artifacts, interleave boundaries, one correctly-attracted delta
      quote) + requirements bank-check vs the evidence corpus.
      Totals: payroll 328/165/172/83, taxation 249/114/140/56, FREP
      363/160/189/170; rulings R-H1..R-H85; COVERAGE 128 rows = 126
      cited + 2 N/A, gates PASS (1097/511/574/326). Next per
      `hn/HANDOVER.md`: residual queue (TOP: Reglamento General IHSS,
      "Acuerdo 799" TEXT (1970), D. 278-2013 [AS re-establisher +
      devolución-8% suspension — one instrument, three questions];
      then D. 247-89 text watch, D. 54-95/36-90 completeness,
      D. 96-2012, LSP/contribuciones statutes, Código de Comercio, SEE
      docs); S-HN5 DEFERRED — bootstrap `Read hn/HANDOVER.md and
      continue.`

      **HN W9 merge 2026-08-21 (§4.6 protocol, twenty-eighth run):**
      `hn-research` rebased onto `27b5d0a` (2 commits rewritten
      `71223da..43b7733`→`fa57aa1..64183e4`: W9 acquisition wave + W9
      session-state HANDOVER; zero conflicts — hn/-scoped only) then
      fast-forward-merged; remote branch ref updated via delete +
      re-push. **HN = W9 RESIDUAL-QUEUE ACQUISITION WAVE COMPLETE
      (corpus 147 files, evidence through EVID-565):** NINETEEN files
      `130_`..`148_` registered + evidenced (84 EVIDs across 8
      dispatched/controller files; SAR-240-2024 fetch discarded
      md5-identical to `19_`): the SAR-catalog family
      `130_`-`144_` + **the Reglamento General IHSS triple
      `145_`/`146_`/`147_` + `148_` via the NEW ihss.hn Wayback-CDX
      recipe** (`cdx?url=ihss.hn*&filter=mimetype:application/pdf` =
      246 PDFs, the whole reglamento family). **R-H86 — D. 278-2013
      CAPÍTULO V Art. 15 "Restablecimiento de la Aportación Solidaria"
      = the AS FY2014+ RE-ESTABLISHER** (re-reads LET Art. 22: 5% on
      the EXCESS of RNG > L1M, PJ except export/tourism, sobretasa del
      ISR non-deductible, ISR calendar — FREP/07 FR-255/256 + LB-018
      statute-anchored). **130_'s other legs:** Art. 9 = the 22-A
      ORIGINAL (regime 0 extended FY2014-17; five 0.75% sectors =
      ORIGINAL list; exclusion b) keeps <L10M inside the ATN; losses →
      D. 96-2012 dado 20-jun-2012 NEW pin; taxation/03 FR-082/LB-019 +
      the corpus "D. 273-2013" misprint corrected to 278-2013);
      Art. 20 = the devolución-8% SIX-MONTH SELF-EXPIRING suspension
      (01-ene-2014→30-jun-2014 outer bound; `41_ OQ-3` resolved as
      temporal — NOT a repeal; Art. 21 = OTCD 50% at 2013 → D. 7-2017
      → SAR-240 chain); Arts. 1-2/5/22-27/49 = the exonerations RESET
      (24+17-numeral survival catalogues; 12-year default cap; DGCFIA
      registration; Adulto Mayor #13/#11 alive — the D. 74-2014
      `132_` authentic-interp 65+ continuity pin, taxation/02 LB-018;
      derogations incl. D. 194-2002 Art. 48 + CT Art. 464);
      Arts. 16-19+Anexo I = the CURRENT 15/18 ISV home + the canasta
      DESCRIPTION-PREVAILS NOTA + Simplificado 31-ene; vigencia
      EXPLICIT 01-ene-2014 (Art. 51). **SAR-256-2024 = the DMC
      due-day bomb** (`134_`, G 36,580 8-jul-2024: may/jun/jul-2024 at
      20 días transitional, from aug-2024 **8 días calendario
      CURRENT** — FREP/03 FR-091/092/OQ-004 re-seeded, R-H18's
      manuals-stale reading SUPERSEDED; OVI monopoly operative
      28-jun-2024; SAR-236 `133_` owns the 535 approval + deroga the
      whole e-filing ancestry incl. SAR-007-2017 — FREP/01
      OQ-006/008/009). **LSP statutes** `135_`-`139_` (the CETF
      códigos 501/524 = LSP's own contribución, tarifa L2.00/millar
      (a/b/d/e/f) / L1.50 (c) / tramos (g); reglamento exemptions
      L120k/L20k + enteros 20th/5th; telefonía 1% transitorio;
      comidas Art. 23 permanente per 31-2018 now in-corpus via the
      texto actualizado; 506-vs-509 NARROWED — **D. 92-2015 (G 33,883
      14-nov-2015) = the closer lead**). **TP triple** `140_`-`142_`
      (vinculación criteria Arts. 11-13; the 545 ancestor Arts. 29-32
      with the threshold DELEGATION — the ≤USD-1M pequeño gate's true
      instrument = **DEI-SG-004-2016, still unacquired**; 62-2019's
      gazette = G 35,077 19-oct-2019 — the catalog's "34,224" was the
      CT's own edition, registry corrected). **THE Reglamento General
      IHSS (the W4b TOP lead RESOLVED):** `145_` Acuerdo 003-JD-2005
      "última versión" + `147_` its GAZETTE ORIGINAL (G 30,735
      29-jun-2005, full Art. 1-194; the "188-vs-143" count premise =
      regex artifact) + `146_` the 1971 Reglamento de Aplicación
      ancestor + `148_` G 33,879 interventora extract. **Art. 135 =
      the contribution-BASE resolver — payroll/03 OQ-005 RESOLVED,
      FR-115 rewritten:** OT/horas extras + rest-day value +
      commissions + profit participation + HABITUAL bonificaciones IN;
      ocasional-y-por-mera-liberalidad primas/bonos/gratificaciones
      OUT; in-kind ≤30%; aguinaldo OUT per D. 117-2021 (89_); the
      14th = config flag (new OQ-010). Art. 134 = minimum base =
      category SMM (FR-137); Arts. 136/151 = ceiling/review powers;
      Arts. 43/67 = subsidio 66% + patrono complement (RIT kin);
      **Arts. 88-97 = the RP chapter (0.2% new-entrant entry on
      nominal-at-techo, five classes, January siniestralidad filing,
      ≥1-year stability — OQ-006 narrowed, class cuadros still
      absent)**; Art. 144 = EMPLOYER 10-day payment (FR-136);
      Art. 161 = 10%-monthly multa class. Verification: EVID
      structural 84/84 contiguous + 3-gram bank-check (LOWs
      adjudicated) + COVERAGE regen. Totals: payroll 330/170/172/84,
      taxation 249/118/140/56, FREP 363/164/189/170; rulings
      R-H1..R-H86; COVERAGE **147 rows = 145 cited + 2 N/A, gates
      PASS (1099/523/574/327)**. Next per `hn/HANDOVER.md`: the
      sharpened residual queue (TOP: D. 92-2015 the 506-vs-509 closer,
      DEI-SG-004-2016 TP gate, SAR-653-2023 CbCR, D. 7-2017 OTCD
      drift, D. 96-2012 loss regimes; then "Acuerdo 799" TEXT (1970)
      + D. 247-89 watch, Código de Comercio, SEE docs, RP class
      cuadros, JD ceilings, DGS SMM promedio prints); S-HN5 DEFERRED —
      bootstrap `Read hn/HANDOVER.md and continue.`

      **HN W10 merge 2026-08-21 (§4.6 protocol, twenty-ninth run):**
      `hn-research` rebased onto `53bf391` (1 commit rewritten
      `bef10b2`→`9e600db`: the W10 wave+session-state commit; zero
      conflicts — hn/-scoped only) then fast-forward-merged; remote
      branch ref updated via delete + re-push. **HN = W10
      SHARPENED-RESIDUAL CLOSERS COMPLETE (corpus 159 files, evidence
      through EVID-643):** TWELVE files `149_`..`160_` registered +
      evidenced (78 EVIDs across 7 dispatched files, 3 shape-(b)
      re-dispatches; the ihss.hn `AJ-RIESGOS-PROFESIONALES` filename
      caught at page-1 = juramentación memo, discarded unregistered):
      `149_` **D. 92-2015** (G 33,883 14-nov-2015, ENAG route) + `150_`
      **DEI-SG-004-2016** (G 34,018 27-abr-2016 — located via the NEW
      ENAG 49-issue SUMARIO batch-scan recipe) + `151_` SAR-653-2023
      CbCR + `152_` D. 7-2017 + `153_` SAR-239-2024 + `154_`
      SAR-283-2024 (SAR catalog) + `155_` Acuerdo 006-JD-2008 REAP
      domésticos (ihss.hn Wayback) + `156_`/`157_`/`158_` the DGS
      promedio prints 2022/2023/2024 (trabajo.gob.hn uploads Wayback
      CDX recipe) + `159_`/`160_` the SAR-43-2026/SAR-125-2024 CT-131
      descargo anchors (ENAG — the SAR catalog slug login-walls).
      **R-H87 — D. 92-2015 reforms D. 53-2015 Arts. 3/4/7 ONLY**
      (grep-negative on LSP/44-A — the 506 side untouched): the
      reservas/fondos tail in the 509 base = REFORM TEXT (FREP/11
      FR-378 statute-anchored; α/β staging flagged OQ-022); reformed
      Art. 7 = the 509 sanction chassis with a THIRD promedio
      resolution semantics (hecho-generador time — never conflate);
      **the 506-vs-509 boundary instruments COMPLETE — readings A
      (all coops) vs B (CONSUCOOP) both textually open, B with more
      witnesses; FREP/11 FR-382 selector stays BLOCKED pending OWNER
      RULING.** **R-H88 — DEI-SG-004-2016 = the USD-1M TP pequeño-gate
      instrument** (FREP/10 OQ-006 resolved; FR-326/327
      statute-anchored; the 31-dic/BCH rate-day = 63_-manual
      elaboration — the acuerdo prints bare "paridad cambiaria") +
      **NEGATIVE RULING: NO safe-harbour regime exists in HN TP law**
      (OQ-005 resolved flag-only). **SAR-653-2023 = the CbCR/Informe
      País por País regime** (threshold Def.-3 = prior-FY consolidated
      < EUR 750M `o` L19,000M words-only, never derive; SEGUNDO
      Num.I UPE duty LIVE / **Num.II local filing SUSPENDED from the
      outset by the TRANSITORIO until a Director-Ejecutivo
      comunicado** — encode suspended; 31-dic digital notification;
      FY-close+12m XML; first reportable FY2025; OQ-024/025 new).
      **R-H89 — D. 7-2017 = the OTCD chain middle instrument**
      (ISV-Art.-8 ¶6: 50%→10% automatic + the 15% NO-DISCRIMINATION
      fallback on the monto total; Art. 3 deroga 278-2013-Art.-21 —
      FREP/04 OQ-003 RESOLVED, FR-147 toggle statute-dated; zero drift
      vs `05_`'s consolidation). **SAR-239-2024 = the QUINCENCAL CETF
      retenciones/percepciones informativa** (replaces
      DEI-SG-110-2012; a new cadence class in FREP/01's due-day
      engine) + SAR-283-2024 the June-2024 prorroga (HISTORICAL).
      **Acuerdo 006-JD-2008 REAP = the domésticos health-only lane**
      (annual prepaid cotización, JD-delegated rates unacquired =
      OQ-011, incapacidad subsidies EXCLUDED, optional IVM bridge —
      payroll/03 FR-126 segment gate). **R-H90 — THE PROMEDIO FAMILY
      5-OF-6 YEARS printed/anchored:** 2022 L11,278.75 / 2023
      L12,377.73 (jornada cell triple-pass 600dpi-closed; two-print
      validated vs SAR-125-2024's SETRASS-411-2023 recital) / 2024
      L13,156.53 / 2025 L13,985.16 (SAR-43-2026 official anchor — no
      DGS 2025 print exists; Oficio SETRASS-DGS-014-2025 = fixer
      lead) / 2026 L14,917.20 — smm_tables.csv rows flipped; the
      FY2022-FY2025 10×SMM caps unblocked for taxation/04 FR-134;
      **THREE promedio resolution semantics separated** (FY-cap /
      CT-131 emission-time umbral — demonstrated twice by the descargo
      pair / hecho-generador-time sanctions); 2027 = the only gap
      (early-2027 watch). **D. 96-2012 routes exhausted W10** (SAR
      live re-crawl, saved CDXs, DEI sitioleyes = 2007-era, engines;
      refined pin = gazetted 20-jul-2012 per `80_`'s recital).
      Verification: EVID structural 78/78 + 3-gram bank-check (LOWs
      adjudicated) + COVERAGE regen. Totals: payroll 330/172/172/85,
      taxation 249/120/140/56, FREP 363/169/189/174; rulings
      R-H1..R-H90; COVERAGE **159 rows = 157 cited + 2 N/A, gates
      PASS (1099/532/574/331)**. Next per `hn/HANDOVER.md`: the
      residual queue (D. 96-2012 watch, CbCR TRANSITORIO restatement
      comunicado, Oficio SETRASS-DGS-014-2025 + DGS 2025 print, RP
      class cuadros + JD ceilings, REAP JD-rates, "Acuerdo 799" TEXT
      + D. 247-89 watch, Código de Comercio, SEE docs, DGS SMM 2027
      print early-2027; **the 506-vs-509 legal reading = OWNER
      DECISION**); S-HN5 DEFERRED — bootstrap `Read hn/HANDOVER.md
      and continue.`

      **GT W-GT7 merge 2026-08-22 (§4.6 protocol, thirty-fourth
      run):** `gt-research` rebased onto `da47a38` (HN's thirty-third
      run had advanced main; 4 commits rewritten
      `5d2afd0..b96b71c`→`d1e0964..be6e89c`; zero conflicts —
      gt/-scoped only) then fast-forward-merged; remote branch ref
      updated via delete + re-push. **GT = W-GT7 BATCH-2 EVIDENCE
      PASS + TARGETED BACKFILLS COMPLETE — CORPUS RE-CLOSED
      94/0/0** (see `gt/HANDOVER.md` §5n): 5 evidence files
      (EVID-746..951, 164 entries) over 84_–95_ incl. the D-19-2016
      blocker; 85_ force-OCR'd (footer-layer heuristic trap).
      **GOQ-08/09(mora)/10/13/24/68/132/134/147 RESOLVED into the
      corpus** (D-19-2016 primary-read: ZF art. 23 keeps
      10-años-from-notificación; 12-bis/8-bis asymmetry verbatim-real;
      2005-state trio recovered via D-38-2004 — AT holiday was art.
      12 c); ICT = Impuesto a la Confianza Tributaria; AG 125-2022
      pointer = own footnote; D-76-78 = SECTOR PRIVADO only (R82 —
      payroll/04 ABSENCE-FR → private engine; public D-1633 absent);
      1421 art. 9 day-20 deadline + art. 38 JM-floating mora cap-100%;
      D-62-2001 = pure IVA adjacency artifact; FT pair primary +
      **AG 118-2002 = AML reglamento named at 2-mar-2006 (NOT
      AG 75-2006)**; Código Civil art. 1508 5-y fallback closes
      FR-110). Backfills: 20 requirements files, 7 new LB rows, zero
      FR renumbering.       GOQ-04 refined (IGSS program reglamentos);
      queue rev 9. No synthesis work remains — next inputs are
      owner-side (AG 52-2017 top acquisition, GOQ-149; TotalDoc
      renewal 02/12/2026, OQ7; AML reglamento ≈17-mar-2027, GOQ-12);
      bootstrap `Read gt/HANDOVER.md and continue.`

      **GT S-GT6/S-GT7 merge 2026-08-22 (§4.6 protocol, thirty-second
      run):** `gt-research` rebased onto `d37f89f` (15 commits rewritten
      `d9b34a3..c446df3`→`37a1a65..3250ffa` in two rebase passes — main
      advanced mid-close as the parallel SV W18 + HN W11 §4.6 runs landed;
      zero conflicts — gt/-scoped + one new plan file) then
      fast-forward-merged; remote ref updated via delete + re-push.
      **GT = S-GT6/S-GT7 SPECIAL-REGIMES SYNTHESIS COMPLETE — ALL SEVEN
      WAVES DONE, CORPUS CLOSED 82/0/0** (see `gt/HANDOVER.md` §5m):
      7 files (`gt/requirements/special-regimes/` GT-SPR-FR-001..193;
      102 LBs / 79 ACs / 20 OQ rows; GOQ-08 + GOQ-135..140 consumed;
      R72..R81 guards; 4 stale master-index preamble R-cites fixed
      R49→R72/R50→R73/R52→R75/R55→R81; final whole-branch review
      APPROVED + one editorial fix wave + re-review PASS). Same session,
      post-wave: register-triage pass GOQ-141..149 (register 149 rows)
      + **acquisition batch 2 = 12 instruments 84_–95_** (incl.
      **D-19-2016 = the GOQ-08 blocker IN HAND** — art. 7 adds maquila
      12 bis verified against primary; D-76-78 aguinaldo; Código Civil;
      FT pair D-58-2005 + AG 86-2006; AG 125-2022; IGSS Acuerdo
      1421-2018; maquila leads AG 3-2017/D-38-04/AG 4-2005; D-31-2024;
      D-62-2001) — COVERAGE 82 cited + 12 pending evidence passes.
      Next per `gt/HANDOVER.md` §5m/§9: W-GT7 evidence pass over
      84_–95_ (EVID-746+) + targeted backfills (GOQ-08 fences,
      payroll/04 aguinaldo ABSENCE-FR, payroll/07 mora, AML FT-lineage,
      cml03 fallback clocks, maquila supersession); watches: TotalDoc
      renewal 02/12/2026 (OQ7), AML reglamento ≈17-mar-2027 (GOQ-12);
      AG 52-2017 = top remaining acquisition (GOQ-149).

      **GT S-GT5 merge 2026-08-21 (§4.6 protocol, twenty-sixth run):**
      `gt-research` rebased onto `1308644` (16 commits rewritten
      `89375f2..c8645a7`→`c739e09..23ad21e`: S-GT5 plan + 7 task waves +
      T1/T4 fix rounds + T8 close + final-review fix + record; zero
      conflicts — gt/-scoped + one new plan file) then
      fast-forward-merged; remote ref updated via delete + re-push.
      **GT = S-GT5 COA/COMMERCIAL-LEGAL SYNTHESIS COMPLETE — FIVE OF SIX
      TOPIC WAVES DONE** (see `gt/HANDOVER.md` §5l): 7 files + 2 indexes
      (`gt/requirements/chart-of-accounts/` GT-COA-FR-001..074 ·
      `gt/requirements/commercial-legal/` GT-CML-FR-001..163 = 237
      FRs / 118 LBs / 78 ACs / 27 OQ rows). **GOQ-124
      RESOLVED-DELIVERED** (retention/destruction max-per-object matrix =
      coa03; closes GT-EINV OQ-005 + GOQ-41 kin — emitter XML retention =
      CT prescription, certificador 14-month = provider-side excluded);
      GOQ-122..134 + GOQ-05/12 all consumed (16 register annotations);
      R70 GOQ-133→132 off-by-one fixed. Negative anchors: NO statutory
      plan de cuentas (PCGA-governed), no copiador, RM-autorización vs
      SAT-habilitación never merged (no SAT fee), AML cutover
      17-sep-2026 (never 17-jun), no Q-threshold AML trigger. COVERAGE
      74 cited / 8 N-A (special-regimes only) / 0 pending — stale
      S-GT6 labels fixed. Final whole-branch review APPROVED (all
      cross-file invariants PASS; one kin-inventory index fix). Next:
      S-GT6/S-GT7 special-regimes plan (D-19-2016 still blocking,
      GOQ-08); bootstrap `Read gt/HANDOVER.md and continue.`

      **SV S9 merge 2026-08-20 (§4.6 protocol, fourteenth run):**
      `sv-research` rebased onto `f2eccbc` (19 commits rewritten:
      `6d01c1e`→`8fe51cc` S8 merge-record fix + `558ed94`→`f67658f`
      range fix + `a021fc8`→`b6fe41a` W15 IVA deep pass +
      `96e136a`→`0098dff` S9 plan + `0e20a28..7147c5b`→`0e7141e..09847d0`
      S9 wave; zero conflicts — all sv/-scoped or new files) then
      fast-forward-merged; remote branch ref updated via delete +
      re-push. **SV = S9 IVA-CORE SYNTHESIS COMPLETE — THE 8-TOPIC
      SYNTHESIS PROGRAM IS DONE** (1,605 FRs total; see the refreshed SV
      section below + `sv/HANDOVER.md`): `sv/requirements/taxation/`
      files 07-15 (SV-TAX-FR-176..353 = 178 FRs / 127 LBs / 134 ACs /
      35 OQs; R30(b) one-prefix continuation; CT retention matrix
      verbatim; FOVIAL SOQ-40 design pass; MOQ-03/04 closed; tercerización
      + frep OQ-002/004 fold-ins wired). **COVERAGE final 63 cited / 0
      pending / 9 N/A / 1 superseded — corpus FULLY cited.** Next per
      `sv/HANDOVER.md` §8: no queued wave — owner picks merge cleanups
      (CAN-STAND + RIDE lists), SOQ-46 acquisition, or go-live work.

### El Salvador — sources & evidence state
- **EVID corpus 001..338** (gaps 109-127, 240 reserved-unused; W15 IVA deep
  pass EVID-304..338 appended 2026-08-20; W14 NIIF files EVID-275..303
  appended 2026-08-19 — country detail now lives in
  `sv/HANDOVER.md`). W13 files (2026-08-19):
  `12_Ley_Zonas_Francas` (EVID-251..258), `14_17b_Servicios_Internacionales`
  (EVID-259..267), `13_42_43_74_Aduanas` (EVID-268..273),
  `31_Guia_FOVIAL_COTRANS` (EVID-274). W12 file:
  `71-73_AML_DL426_Instructivo380_CCverify` (EVID-241..250). W11 file:
  `66-70_Quincena25` (EVID-236..239). W10 files:
  `07_Codigo_Comercio` (EVID-211..227), `15_Ley_Lavado_Activos` (EVID-228..231,
  **historical since W12**), `17_Reglamento_Lavado_Activos` (EVID-232..235,
  kept-mechanics citable). W9 files:
  `16_Salarios_Minimos_2025` (EVID-191..192), `08_Ley_ISSS` (EVID-193..196),
  `09_Ley_Sistema_Pensiones` (EVID-197..200), `11_Codigo_Trabajo`
  (EVID-201..209), `65_F11_v18_form_visual` (EVID-210). W8 files:
  `29_F985_CNR_RegComercio` (EVID-172), `34_36_39_F07_v14` (EVID-173..179),
  `35_37_38_59_F14_v16_v17` (EVID-180..184), `30_Calendario_Tributario_2026`
  (EVID-185..186), `61-64_report_forms` (EVID-187..190); `60_DE10_...` (EVID-171).
  **72 registered source files, numbering 01-74** (gaps 21/23/24/28;
  66_-70_ = Quincena-25 (W11); 71_ = D.L. 426 AML law, 72_ = UIF Instructivo 380,
  73_ = CC verification copy (W12); 74_ = Ley Simplificación Aduanera D. 529,
  acquired W13 from uif.gob.sv; next numbering = 75).
- Source registry carries: 29_ mislabel note; 38_/39_ current-form notes; 59_
  (F14 v17), 60_ (D.E. 10 gazette print), 61_-64_ (F910v9/F915v4/F930v3/F935v1)
  with provenance; 08_ law-level-rates-only note; 09_ D.L. 614 identity
  note (registry misnomer); 65_ (F-11 v18 + **superseded-by-v19/v20 note**);
  **07_ consolidation-≤2008 note; 15_ title-mislabel amendment (R25); 17_
  PRE-REFORM note (R26); 66_-70_ with transparenciafiscal provenance**.

### El Salvador — extraction (S1 scope COMPLETE; W6/ISR COMPLETE 2026-08-17)
- **EVID corpus now 001..152** (gap 109–127 reserved-unused): S1 = 87 entries
  across 7 evidence files + the 45_Anexos digest (committed under
  `sv/.extractions/`; `.txt` dumps + `schemas_2026/` stay ignored —
  regenerable). **W6 ISR**: `03_Ley_ISR.evidence.md` (EVID-088..108),
  `04_Reglamento_ISR.evidence.md` (EVID-128..146),
  `10_Tablas_Retencion_ISR.evidence.md` (EVID-148..152); 23 new OQs
  (per-file OQ-1.. numbering; not yet MOQ-rolled).
- Waves done: W1 foundations (11 DTE structures + events manual), W2 catalogs
  sidecars, W3 Ley IVA + Reglamento, W4 Código Tributario, W5 DTE stack, W5.5
  2026-regulatory-update re-read, W6 ISR (Ley + Reglamento + retention tables).
  Sources refreshed mid-project: files 44–52
  fetched from factura.gob.sv (D.L. 487 CT reform, Normativa v2.0 25-May-2026,
  Manual Tecnológico v2.0, catalogs v1.1 2026 re-versioning, JSON schemas
  2026-08-11). **Authority order: 44_/45_/46_/50_/51_/52_ (2026) > 18_/19_/22_
  (2025) > 40_/41_/25_ (2022).** Superseded sources retained as historical LB.
- **W6 rulings (see EXTRACTION_PLAN W6 entry for detail):** (1) 10_ tables
  are 1992 colones-era (D.E. 75/25) — superseded in practice; the operative
  retention tables decree is MISSING → acquire from MH (next-file numbering
  continues from 53); (2) Reglamento ISR carries a self-documented repeal map
  (D.E. 117-2001) — only substantive computation articles survive; (3) pago
  mínimo declared UNCONSTITUTIONAL (sent. 18-2012) — do not implement;
  (4) Ley ISR copy consolidated only through D.L. 233-2012 — verify post-2012
  reforms (Art. 37 brackets / 41 rates / 72 5% / 29-A limits) before
  synthesis trusts them.
- 50 source files (numbering 01–52; gaps 21/23/24/28 unused) + superseded 2022
  `schemas/` dir + current 15 schemas inside the 52_ zip.

### El Salvador — W6.5 ISR source acquisition (COMPLETE 2026-08-17, same day)
Both ISR synthesis blockers closed; sources 53_/54_/55_ registered:
- **53_ = D.E. 10-2025** (certified copy via transparenciafiscal): the CURRENT
  retention tables — monthly $550 exempt / quincenal $275 / semanal $137.50,
  June/December recálculo tables, base definition (closes 10_ OQ-4 for the
  current regime), multi-employer rule, repeals D.E. 95-2015, effective
  May-2025. Supersedes 10_ (1992 colones-era) as operative authority.
- **54_ = Ley ISR Asamblea consolidation** (title: D.O. 79 T.447 30-abr-2025;
  content refs through Jan-2026): current authority superseding 03_. Tail
  block = authoritative reform history: post-2012 = D.L. 762-2014
  (unconstitutional, sent. 96-2014), D.L. 458-2019, D.L. 969-2024, D.L.
  293-2025 + interpretaciones D.L. 192-2018/345-2019 + related transitories.
- **55_ = D.L. 293-2025** (D.O. extract pp. 21-23): Art. 37 Tramos I/II only —
  exempt $4,064 → $6,600 (10% bracket $6,600.01–$9,142.86 + $212.12; III/IV +
  cuotas unchanged); effective 2025-05-08.
- Verified against 54_: Art. 41 (30%/25%), Art. 72 (5%), Art. 29-A limits
  unchanged → 03_ OQ-8 substantively resolved (Art. 3 changed — movimientos
  de dinero; exact D.L. attribution 458-2019 vs 969-2024 pending W7 read).
- Also spotted (not yet acquired): **F14 v17** form (2026-06-03) newer than
  our 35_F14_v16 manual — matters for the fiscal-reporting wave.

### El Salvador — W7 evidence pass (COMPLETE 2026-08-17, same day)
Evidence on the new sources committed (EVID-153..167):
- **53_ evidence** (EVID-153..161): D.E. 10-2025 fully transcribed — tables
  a)-c), June/December recálculo (derived as Art. 37 shifted +$1,600),
  NET base definition (closes the old OQ-4 for the current regime),
  multi-employer rules, proration for special periods. 9 OQs incl. the
  printed-digit fidelity set and the $1,600-proration ambiguity.
- **54_/55_ delta evidence** (EVID-162..167): post-2012 reform set CLOSED —
  D.L. 762-2014 void; **458-2019 = Art. 4.16** (aguinaldo-excess retention
  now deducts the 2-SMM floor); **969-2024 = Art. 3.4** foreign-source
  exclusion + Art. 28 pro-rata carve-out + **Art. 14-A incisos 6-8
  derogated** (W6 EVID-094 foreign-securities text is DEAD); 293-2025 =
  Art. 37. Art. 41/72/29-A/33 verified unchanged (03_ OQ-8 closed; W6
  citations transfer to 54_ as current authority).   4 OQs: interpretaciones
  192-2018/345-2019 scope, D.L. 969 vigencia, reglamento provenance chain
  (101-1992 vs 117-2001), consolidation dating.
- **W7 addendum (same day):** sources 56_/57_/58_ acquired (D.O. extracts);
  gating OQs CLOSED — D.L. 969-2024 full text (EVID-168: Art. 2 derogates
  Art. 14-A 6º-8º + Art. 16 4ºc)/5º/7º + Art. 27 2º-4º; effective
  2024-03-22), D.L. 192-2018 (EVID-169: Art. 30.1 seasonal depreciation —
  full annual quota for café/caña-type activities), D.L. 345-2019 (EVID-170:
  Art. 28 mermas/pérdidas deductibility + zero-base guard). ISR evidence
  base COMPLETE for S2 synthesis (EVID-088..170).

### El Salvador — synthesis S1 (COMPLETE, pushed) + schema pass + §3.11 addendum (2026-08-17)
Six Takumi files + index + coverage, **222 FRs / 70 LBs / 99 ACs / 47 OQs
(34 open, 13 resolved)**:

| File | FRs | Prefix range |
|---|---|---|
| `sv/requirements/e-invoicing/01_document-types.md` | 52 | SV-EINV-FR-001..052 |
| `sv/requirements/e-invoicing/02_transmission.md` | 40 | SV-EINV-FR-053..086 + 159..164 (§3.11 addendum) |
| `sv/requirements/e-invoicing/03_events.md` | 43 | SV-EINV-FR-087..129 |
| `sv/requirements/e-invoicing/04_signing_delivery.md` | 29 | SV-EINV-FR-130..158 |
| `sv/requirements/e-invoicing/06_api-protocol.md` | 40 | SV-PROT-FR-001..040 |
| `sv/requirements/catalogs/05_governance.md` | 18 | SV-CAT-FR-001..018 |

FR numbering is wave-sequential within a prefix across files (EINV restarts
never; PROT/CAT are separate prefixes). New waves pick new topic prefixes
(e.g. taxation, fiscal-reporting) per the `<CC>-<TOPIC>-FR-nnn` contract.
Executed subagent-driven: per-task implementer + reviewer + scoped
re-reviews; two fix rounds (T4, T6); final whole-wave review ("usable with
fixes") + one fix wave — all findings closed. Coverage matrix: 51 rows, no
orphans (14 cited / 1 superseded-not-cited / 8 N/A / 28 pending-S2+).

**Schema pass 2026-08-17 (controller-executed, committed):** the 15 schemas
inside the 52_ zip (`sv/.extractions/schemas_2026/svfe-json-schemas/`,
regenerable) + 45_/18_ raw text closed 10 OQs — 01 OQ-002/003/004/005/008,
03 OQ-001/002/003/005, 04 OQ-002 — plus master-index MOQ-02/08/09/12
(struck); MOQ-05 endpoint-absence schema-verified (still AT-blocked).
FR updates: FR-012/018/022/035 (01), FR-103/104/117 (03), FR-133 (04);
Data Model codTributo row (01). OQ rollup in `00_index.md` = 29 open /
13 resolved.

**§3.11 addendum (user-driven design session, same day):** fiscal
immutability & correction accounting — FR-159..164 in `02_transmission.md`:
account.move lifecycle lock keyed to transmission state (no reset-to-draft/
cancel/delete past seal); invalidation ⇒ auto-generated NON-EDITABLE
full-mirror reversal entry in the event's period (credit-note treatment
cross-month; replacement nets in its own period); window-expired CCF/CR ⇒
NCE/NDE; retorno ⇒ credit entry + goods-vs-price-only traceability
invariants; cross-type reissue inherits sale order + pickings (supersede,
never delete); corrections derive USD from the ORIGIN rate (multi-currency
books; DTE layer stays USD-only). New OQs 02 OQ-008..011 (F-07/F-14 annex
presentation → S2; NRE fate on origin invalidation — evidence silent,
working assumption NRE survives; declaration FX → S2; line-level
move↔picking linkage design pass — product owner has prior-implementation
mechanics to import).

### El Salvador — synthesis S2 (ISR) (COMPLETE 2026-08-18, pushed)
Prep (controller-executed): master index extended with clusters T1-T8 + rulings
R17-R22 + SOQ-01..07; CT Art. 62 FX rule captured from raw txt (closes 03_ OQ-2);
54_-file OQ-4 reglamento provenance RESOLVED (R17: 04_ = D.E. 101-1992
consolidated incl. reform D.E. 117-2001 — the 54_ tail listing is editorially
partial). Wave plan `docs/superpowers/plans/2026-08-17-s2-isr-synthesis.md`;
executed subagent-driven (7 tasks, per-task reviews, 3 fix rounds, final
whole-wave review "usable with fixes" + one fix wave). Deliverables in
`sv/requirements/taxation/`:

| File | FRs | Prefix range |
|---|---|---|
| `01_isr-framework.md` | 33 | SV-TAX-FR-001..033 |
| `02_isr-deductions.md` | 40 | SV-TAX-FR-034..073 (payroll gate = FR-040) |
| `03_isr-rates-gains.md` | 28 | SV-TAX-FR-074..101 |
| `04_isr-withholding.md` | 30 | SV-TAX-FR-102..131 + 2 CSV sidecars |
| `05_isr-distributions.md` | 18 | SV-TAX-FR-132..149 (register: `l10n_sv.isr.earnings.register`) |
| `06_isr-assets.md` | 23 | SV-TAX-FR-150..172 |

Totals: **172 FRs / 111 LBs / 118 ACs / 44 OQs (42 open, 2 resolved)**.
CSVs: `withholding_tables.csv` (20 rows, D.E. 10-2025 exact-as-printed with
[sic] flags — fidelity rule) + `isr_brackets.csv` (23 rows: both Art. 37
vintages + 3×1992 tables; dl_957_2011 valid_from unpinned → OQ-005 chain gap).
In-wave resolutions: SOQ-01 (Art. 42 stamp (14)=D.L. 496-2004 governs; Art. 17
media-tasa historical), SOQ-04 (NO general NOL; CT scan negative). Open notables:
SOQ-02 ($1,600 proration quincenal/semanal), SOQ-03 (D.E. 10 D.O. pin + digit
anomalies — extra finds 1,731.42, semanal III 509.52), SOQ-05 (2025+ aguinaldo
transitory), 03 OQ-009 (mid-2025 vintage straddle for one annual liquidation).
COVERAGE rollup now 23 cited / 25 pending / 8 N/A / 1 superseded.

### El Salvador — synthesis S3 (fiscal reporting F-07/F-14) (COMPLETE 2026-08-18, pushed)
W8 evidence (EVID-172..190) + acquisitions 59_-64_ + master-index clusters F1-F12 + SOQ-08..14
fed a subagent-driven wave (9 tasks, per-task reviews, 6 fix rounds, final whole-wave review
"usable with fixes" + one fix wave 9/9 addressed; commits 334497f..d2e5e4a). Deliverables in
`sv/requirements/fiscal-reporting/`:

| File | FRs | Prefix range |
|---|---|---|
| `01_f07-declaration.md` | 41 | SV-FREP-FR-001..041 (casilla engine + upload engine) |
| `02_f07-annexes-sales.md` | 25 | SV-FREP-FR-042..066 (canonical DTE-identifier mapping FR-042/043) |
| `03_f07-annexes-purchases.md` | 28 | SV-FREP-FR-067..094 (canonical ISR quartet FR-079..085) |
| `04_f07-annexes-retentions-events.md` | 29 | SV-FREP-FR-095..123 (F-930 view; SOQ-10 ruling LB-007) |
| `05_f07-annexes-special.md` | 13 | SV-FREP-FR-124..136 (fuel/357 dated regimes) |
| `06_f14-declaration.md` | 34 | SV-FREP-FR-137..170 (SS caps; dead pago-mínimo FR-163; Quincena-25 v17 FR-165/166) |
| `07_codes-and-informs.md` | 24 | SV-FREP-FR-171..194 + `f14_income_codes.csv` (48 codes) |
| `08_filing-calendar.md` | 14 | SV-FREP-FR-195..208 (SOQ-08 windows as config) |

Totals: **208 FRs / 66 LBs / 94 ACs / 47 OQs**. In-wave answers: F-910 = the CT 123 ISR
retention surface (taxation 04 OQ-007 answered ISR-side); F-915 = the Art. 74-C inform
format (taxation 05 OQ-002 partially answered); F-07 anulados detail code "D" closes
e-invoicing 02 OQ-008's F-07 side (retorno gap open with e-invoicing). COVERAGE now
36 cited / 17 pending / 9 N/A / 1 superseded (63 rows). Key session finds recorded in
W8 log: **29_ is MISLABELED** (actual content = F985/F-975 CNR manual — CT 121 a)2
third-party report; the intended annex-modification resolutions are NOT in the corpus);
**F-14 v17 = Quincena-25 section only** (casillas 417/418; no v17 manual yet — SOQ-09
blocks the annex-level FR); F-07/F-14 manuals are the primary authority for declaration
mechanics; DTE-identifier mapping (Serie=sello 40c / Resolución=NC-28 pre-Nov-2022 CG-32 /
Número=CG-32 pre-Nov-2022 NC-28) is now FR-042/043 canonical.

### El Salvador — W9 payroll evidence pass (COMPLETE 2026-08-18, same day)
Sources read end-to-end + evidence EVID-191..210 (5 files, 16 file-level OQs):
- **16_ = Decreto 11-2025 SMM** (D.O. 95 T.447 23-May-2025, effective 1-Jun-2025;
  repeals D.E. 9/10-2021): Agrícola $305.23 / Industria $408.80 / Comercio y
  servicios $408.80 / Maquila $402.32; piece-rate caña $5.018/t + $2.007/arroba,
  café $0.080/lb + Art. 6 descanso prestación table; 3-decimal daily/hourly prints
  transcribed [sic]. Feeds: aguinaldo floor $817.60 (2× comercio y servicios),
  FE-receptor 3×SMM, 25-SMM ban (sector selection = 16_ OQ-2 open).
- **08_ = Ley Seguro Social D.L. 1263** (1953 consolidation, last reform 1994):
  law-level rates only — salud 7.5%/3%, Art. 99 public 6.68%/2.67%, pensioner
  health 6% (superseded by 09_ 7.80%). **CAPS live in the Reglamento — NOT in
  corpus** (08_ OQ-1 acquisition candidate); withholding/remittance duty,
  1%/month late recargo, first-class credits, 48h accident reports,
  Art. 100 benefit-substitution rule.
- **09_ = IDENTITY FIND: Ley INTEGRAL del Sistema de Pensiones, D.L. 614**
  (D.O. 241 T.437 21-dic-2022 → effective 2022-12-29; **derogates D.L. 927-1996
  SAP** — the registry title "Ley del Sistema de Ahorro para Pensiones" is a
  MISNOMER, registry row amended). Cotización **16% = 7.25% trabajador +
  8.75% empleador** (9.0/6.0/1.0 split); IBC = ordinary-services money
  remuneration (aguinaldo/viáticos/ocasionales OUT, SMM floor, calendar-day
  months, multi-job per-salary); **declare+pay first 10 días hábiles**,
  electronic planilla (AFP + ISSS); sanctions 5/10/15% + 20%+2%/mo +
  10%+5%/mo; privileged imprescriptible credits; ISR hooks (cotizaciones no
  gravadas; **voluntary savings ≤10% IBC deductible, 5-y withdrawal clawback**);
  IPSFA excluded; IBC ceiling instrument ABSENT (F-14's AFP $472.93 value is
  the only corpus anchor — 09_ OQ-1).
- **11_ = Código de Trabajo** (Índice Legislativo edition, payroll books read
  full): salario vs **salario básico** (7 derivation rules — the universal
  employer-obligation base); jornada 8/44 (+nocturno 7/39; +25% nocturnal,
  **+100% overtime**); séptimo día per complete week (presumed in period
  salaries); **vacaciones 15d+30%** (200-day gate, no cash-out except
  termination); asuetos static list + 2× pay (CT list vs Calendario-2026
  legend divergence → dated data, 11_ OQ-1); **aguinaldo tiers 15/19/21 días,
  window 12-20 Dec, no disciplinary forfeiture**; **indemnización 30d/year
  min 15d, salary cap 4× daily SMM**; contract taxonomy (indefinido/plazo/
  obra/interino/30-day trial); SMM chassis (5-8h full SMM; triennial);
  illness 75% seniority tiers; **maternity 16w @75% básico (10 post-partum),
  Art. 311 tenure gate VOID per sent. 105-2014**; lactancia 1h/d paid.
- **65_ = F-11 v18 acquired** (ISR annual declaration, Feb-2025): rentas
  matrix 105-145 = the F-07 R/S consumer surface (closes 07 OQ-006's
  acquisition half); personal deductions 711-725 incl. SS rows (form label
  still cites dead Ley SAP Art. 22 — print-vs-law defect); **pago-mínimo
  casillas 630-648 printed but DEAD (R21 — never feed)**; devolución ≤$5,000.
- **Quincena-25 acquisition BLOCKED (pinned)**: law = **D.L. 499, D.O.
  14-ene-2026, volume Id 31679**; the D.O. `/seleccion/{Id}` route 500s
  server-wide since 2026-08-18 ~13:55 (worked that morning for 60_). Retry
  when up; law-firm PDF mirrors exist but are NOT official (do not register).
- Resolution candidates recorded in evidence (formalize at S4 prep):
  pensioner-health 6% → **7.80%** (later-in-time, 09_ Art. 154);
  11_ OQ-1 asueto dual-layer design; 16_ OQ-1 fidelity discipline.

### El Salvador — synthesis S4 (payroll) (COMPLETE 2026-08-18, pushed)
Prep (controller-executed): master index extended with clusters P1-P10 + rulings
R23-R24 + SOQ-15..21 (commit 87df6b5). Wave plan
`docs/superpowers/plans/2026-08-18-s4-payroll-synthesis.md`; executed
subagent-driven (9 tasks, per-task reviews, fix rounds T1/T4, final whole-wave
review "usable with fixes" + one fix wave 10/10 addressed; commits
87df6b5..33edf2d). Deliverables in `sv/requirements/payroll/`:

| File | FRs | Prefix range |
|---|---|---|
| `01_salary-model.md` | 10 | SV-PAY-FR-001..010 (canonical category matrix FR-004) |
| `02_minimum-wage.md` | 13 | SV-PAY-FR-011..023 + `smm_2025.csv` (18 rows [sic]-faithful) |
| `03_working-time-surcharges.md` | 20 | SV-PAY-FR-024..043 (asueto dual-layer SOQ-19) |
| `04_statutory-benefits.md` | 19 | SV-PAY-FR-044..062 (vacaciones/aguinaldo labor side) |
| `05_social-security-contributions.md` | 23 | SV-PAY-FR-063..085 + `ss_contributions.csv` (14 rows) |
| `06_ss-declaration-remittance.md` | 15 | SV-PAY-FR-086..100 |
| `07_contracts-termination.md` | 20 | SV-PAY-FR-101..120 (Art. 311 VOID invariant) |
| `08_isr-interfaces.md` | 17 | SV-PAY-FR-121..137 (by-id feeds; Quincena-25 BLOCKED) |

Totals: **137 FRs / 126 LBs / 94 ACs / 41 OQs (39 open, 2 resolved)**.
Key encodings: SIP = D.L. 614 16% = 7.25/8.75 (R24 — SAP lore dead); ISSS
7.5/3 law-level; ALL cap values = F-14-print dated data with instrument-OQs
(SOQ-15/16/17) — never arithmetic-derived; 4×SMM cap $53.76 = config-default
(comercio y servicios row ×4, SOQ-18 kin); indemnización 30d/yr min 15d;
vacaciones 15d+30%; aguinaldo tiers 15/19/21 window 12-20 Dec no-forfeiture;
+25% nocturnal / +100% overtime; first-10-días-hábiles SS remittance (consumes
FREP FR-203 engine); ISSS 1%/mo vs SIP sanction scales kept distinct;
voluntary pension savings ≤10% IBC + 5-y clawback; F-11 711-725 feeds with
stale-717-label guard; pago-mínimo dead-print guards (R21). COVERAGE rollup
now 41 cited / 13 pending / 9 N/A / 1 superseded (64 rows incl. 65_).
Cross-refs: taxation/00_index F-11-feed pointer; fiscal-reporting/00_index
SOQ-11 values-owned-by-payroll/05 pointer.

### El Salvador — W11 Quincena-25 acquisition + evidence (COMPLETE 2026-08-18, same session)
User supplied a transparenciafiscal search (D.O. `/seleccion` still 500 server-wide —
also confirmed via the D.O. website UI by the user). Acquired + registered + read:
- **66_ = D.L. 499 Ley Especial Quincena Veinticinco** (D.O. N° 8 T.450 14-ene-2026,
  effective same day; official DGII copy). **67_** = Guía de Orientación
  MH.UVI.DGII/006.001/2026 (+8 anexos). **68_/69_** = upload instructions/manual
  (annex-CSV spec). **70_** = plantilla macro (semicolon-delimiter confirmation).
- Evidence EVID-236..239 (`66-70_Quincena25.evidence.md`): benefit = 50% salario
  básico/nominal, gate ≤$1,500, 15–25 Jan; 2026 public-mandatory/private-VOLUNTARY
  + 100% ISR credit (ZF/DPA/LSI → transferable Certificado de Crédito Tributario);
  2027+ mandatory all; renta no gravada + zero retention/SS + not-in-benefit-bases
  + inembargable; employer gasto deducible; tercerización FCF-exento + no Art.-66
  pro-rata; reporting chain F-14 v17 January-only annex (7-col `;` CSV; NIT XOR DUI)
  → 417/418 → F-910 code 73 → casilla 724 → **F-11 v19 casilla 319**; **F-11 v20**
  special-regime (NEW FORMS — acquisition candidates ≥71; 65_ = v18 superseded).
- **P10 UNBLOCKED; SOQ-09 RESOLVED; payroll/08 OQ-002 + FREP 06 OQ-001 flipped
  resolved-acquisition; COVERAGE = 69 rows (5 pending-S2+ added).** FR fold-ins
  into payroll/01+08, fiscal-reporting/06+07, taxation, special-regimes = QUEUED
  edit wave (S6-fix candidate).

### El Salvador — synthesis S6 (Quincena-25 FR fold-in) (COMPLETE 2026-08-18, pushed; commits d757ae6..db82601)
Executed subagent-driven per plan `docs/superpowers/plans/2026-08-18-s6-quincena25-foldin.md`
(7 tasks, per-task reviews, 2 fix rounds T1/T6, final whole-wave review "usable with
fixes" + one fix wave 7/7 + controller one-line residual; numbering contract
SV-PAY-FR-138..143 / SV-FREP-FR-209..212 / SV-TAX-FR-173..175):
- **payroll/01:** matrix quincena_25 row — Category cell = "none — special-law
  benefit outside the CT categories" (66_ Art. 1 independence; sv_pay_earning_category
  stays empty for Quincena rules — Ruling 33).
- **payroll/04:** §3.4 FR-138..141 (50% salario básico o nominal, ≤$1,500 gate,
  15–25 Jan; aguinaldo-eligibility mirroring + Art. 3 [sic] proportional right;
  dated 2026-public-mandatory/private-voluntary → 2027-all-mandatory flag;
  no-retention/no-cotización/not-in-any-base/inembargable invariants). 05 FR-075
  IBC-exclusion note appended.
- **payroll/08:** FR-137 rewritten (absence invariant WITHDRAWN → renta no gravada
  treatment) + FR-142 (7-field ledger = annex value source) + FR-143 (417/418
  aggregates); OQ-002 resolved-acquisition; OQ-004 sharpened (v19/v20 confirmed).
- **fiscal-reporting/06:** FR-166 amended, FR-167 rewritten (separate January-only
  planilla upload — old working assumption WITHDRAWN) + FR-209..211 (7-col `;` CSV
  export contract; January-window gate + clear-then-reupload + line-numbered
  validation; 417/418 auto-sum + code-73 wiring + warning-only F=0.5×E/E>$1,500
  cross-check). OQ-009 resolved (`;` operative).
- **fiscal-reporting/07:** FR-212 code 73 + CSV row 73 (dated 2026-01, catalog_version
  `f17_kin` = MH-package authority NOT v16 apéndice); FR-177/178/179/181 amended;
  AC-001 count updated (49 rows).
- **taxation/01+02:** FR-173 (renta no gravada, Art. 8 prevalence), FR-174 (FY-2026-only
  employer credit ledger `l10n_sv.isr.quincena.credit` + remanent + tercerización +
  ZF/DPA/LSI certificado + F-11 v19 casilla-319 feed key; R21 dead-rows extend to v19),
  FR-175 (gasto deducible on payment+documentation; double-benefit OQ; IVA tercerización
  deferred pointer).
- **Corpus state:** payroll 143 FRs (133 LB/100 AC/42 OQ), fiscal-reporting 212
  (71/98/50 — 48 open/2 resolved), taxation 175 (117/122/47); COVERAGE 46 cited /
  13 pending / 9 N/A / 1 superseded (69 rows); master index F10 resolved + P10 folded +
  Section-B R27; special-regimes/00_index.md wave-prep stub created (no FRs).
- Open notables: 07 OQ-008 (v17-apéndice inclusion of code 73 unverified — v17
  manual/F-910 v10 watch); 06 OQ-008 (MH validation depth — warning-only cross-check);
  taxation OQs double-benefit 2026, F-11 v19/v20 acquisition ≥71, IVA tercerización
  pointer.

### El Salvador — W10 commercial-legal evidence pass + S5 prep (COMPLETE 2026-08-18, pushed; commits 3cd4ad4/c75610c)
Sources read end-to-end + evidence EVID-211..235 (3 files, 11 file-level OQs → SOQ-22..29):
- **07_ = Código de Comercio D.L. 671/1970** (consolidation through reform (29)
  D.L. 641-2008 — post-2008 reforms UNVERIFIED, SOQ-22; 260pp; commercial-legal
  books full, quiebra skimmed, seguros/transporte/bancarios N/A). Key: matrícula =
  registro único + ANNUAL renewal; contabilidad electronic-legal/castellano/USD/
  in-country + **no-alteration + immediate-rectification-asiento regime (Art. 439)**
  = §3.11 kin; annual statements 3 months IMPRORROGABLE + auditor + **Registro
  deposit = third-party effect** ($12k/$34k thresholds; sociedades/EIRL always);
  **retention 10y books + issued/received facturas anexas + 5y post-liquidation**;
  microfilm/optical ≥24 months; reserva legal 5%→1/6 (colectiva) / 7%→1/5
  (SRL/S.A./EIRL); SRL $2,000/Ltda.; S.A. share-ledger + no self-acquisition;
  fusión 90-day window + Competencia checkpoint; liquidación suffix + 2y cap +
  10y post-liquidation paper deposit; single-socio 3-month collapse; extranjeras
  package; auxiliares authority defaults (factor registry powers, dependiente
  caja/outside rules, distribuidor indemnity scale); cheque 15d/1m/3m + protest
  15d + 1y + 20% indemnity; **prescription matrix 6m/1y/2y/5y-from-last-recognition
  (Art. 995)**; mora interest pactado→legal (Economía rate, SOQ-26); facturas +
  registros contables = statutory proof (999/1002); compraventa defect/warranty
  clocks (8d/15d/1y; 30d/6m/3y) + CSF/CF/FOB in-code; estimatorio/suministro/
  comisión no-credit-default.
- **15_ = Ley Contra el Lavado de Dinero y de Activos D. 498/1998** (reforms (1)-(6)
  through D.L. 104-2015; registry title was a MISLABEL — row amended, R25).
  **Sujetos obligados include ANY mercantile society (Art. 2.20)**; unsupervised
  exempt only from Oficialía; threshold reporting **$10,000 cash per client
  same-day/rolling-month / $25,000 other media, 5 días hábiles**; suspicion
  reports amount-irrelevant (≤15+15d analysis); PEP enhanced DD; retention 5y
  docs / 15y transaction registers; Art. 13 8-field capture; safe harbor 26-A;
  tip-off crimes 26-B.
- **17_ = Reglamento D. 2-2000** — complete 6pp (the "partial document" suspicion
  CLOSED) but **PRE-REFORM**: colones ¢500k threshold + 3-day clock superseded by
  15_ Art. 9 post D.L. 568-2013 (R26); citable for window mechanics (30 continuous
  days back from last transaction), no-tip-off (4j), liaison 15-day notice (4g),
  red-flag catalogs (12-18, case-creation never auto-report). Current reglamento
  + UIF forms = SOQ-27 acquisition.
- **S5 prep (controller-executed, c75610c):** master index extended with clusters
  **C1-C10** + rulings **R25/R26** + **SOQ-22..29** (incl. SOQ-28 retention-matrix
  reconciliation CC vs AML vs DTE = S5 synthesis deliverable; SOQ-23 SAS law;
  SOQ-25 Ley Registro de Comercio).
- **Quincena-25 retry (same session): D.O. `/seleccion` route STILL 500 server-wide**
  (all Ids; API listing works; Id 31679 = 14-01-2026 volume confirmed). Keep retrying.
- Periodic checks: MH formularios unchanged (F14-V17-1 2026/06; no v17 manual —
  SOQ-09 open); factura.gob.sv /downloads no longer exposes wpdmdl links in raw
  HTML (JS-driven) — re-verify IDs before reuse.

### El Salvador — W12 AML-regime-replacement acquisition + evidence pass (COMPLETE 2026-08-18, same session; commit b4cd790)
**Route find: uif.gob.sv Marco Legal** (official FGR/UIF library — the one live official mirror;
asamblea.gob.sv unreachable (000), D.O. /seleccion still 500 server-wide, transparenciafiscal
JS-opaque, search engines bot-blocked). Acquired + registered + read (sources 71_/72_/73_):
- **71_ = D.L. 426 Ley Contra el Lavado de Dinero y de Activos** (7-oct-2025, D.O. N° 190
  T.449 9-oct-2025, effective 2025-10-17) — **WHOLESALE REPLACEMENT of D. 498-1998 (15_)**
  per Art. 61: sujetos obligados restructured to 10 named categories (**the "any mercantile
  society" catch-all is GONE**; digital-asset/bitcoin providers + political parties in);
  ROS = 15 días hábiles analysis + ONE same-length extension + **24h transmit**; regulated-ops
  thresholds DELEGATED to a future reglamento (Art. 25); **retention UNIFORM ≥15 años**
  (old 5y/15y split dead); border declaration $15,000 (was $10k); sanctions in SMM
  sector-comercio units (50-500/501-1000; officers + inhabilitación 5y/10y); 10y sanction
  prescription; supervision split SSF/SOM/CSJ/CNAD/TSE; adaptation clocks 6/9/12 months.
- **72_ = UIF Instructivo Acuerdo 380** (22-oct-2021, D.O. 205 T.433 27-oct-2021; reformed
  Acuerdo 266-2023 + 476-2023; 93 arts + Anexo 1) — **kept in force by 71_ Art. 61** → the
  OPERATIVE $10k-cash/$25k-other-media regime (Art. 51: single + monthly-cumulative +
  mixed-payment decomposition, 5 días hábiles) + institutions' $1,000-wire/$200-remesa
  monthly aggregates (Art. 52) + APNFD GAFI triggers ($3k casino/$10k metals-cash/$10k
  lawyer-office, Art. 77) + Encargado de Cumplimiento + beneficiario-final DD.
- **73_ = Código de Comercio Índice Legislativo edition (UIF copy)** — verification-grade:
  its reform list ALSO ends at D.L. 641-2008 → **SOQ-22 RESOLVED-WITH-RESIDUAL** (decree-date
  print conflict 12-vs-26-jun-2008 [sic]; same D.O. 120 T.379 27-jun-2008). Structurally
  damaged PDF (page tree); text via ghostscript pdfwrite rebuild (regenerable .txt).
- Evidence EVID-241..250 (`71-73_AML_DL426_Instructivo380_CCverify.evidence.md`, 6 OQs).
  Rulings: **R26 addendum** (no post-568-2013 reglamento ever issued — 17_ is
  operative-by-transitory), **R28** (threshold authority chain: 71_ Art. 25 delegation +
  72_ Art. 51 operative values as dated config + pending-reglamento watch). SOQ-27
  RESOLVED-BY-RESTRUCTURE; SOQ-23 SAS-existence confirmed via creaempresa.cnr.gob.sv
  (statute identity still unpinned — open); SOQ-25 still open (not on the UIF library).
  W10 AML evidence EVID-228..231 now HISTORICAL. Numbering next = 74. Registry 15_/17_
  supersession notes amended.

### El Salvador — synthesis S5 (commercial-legal) (COMPLETE 2026-08-18, pushed; commits 6c09db7..9bb37e9)
Executed subagent-driven per plan `docs/superpowers/plans/2026-08-18-s5-commercial-legal-synthesis.md`
(11 tasks, per-task reviews, fix rounds T1/T2/T5/T9/T10 + final-fix wave + controller one-line
residual; final whole-wave review "usable with fixes" 5/5 + 4 mechanics addressed, rulings
audit 5/5 upheld; re-review PASS merge-ready). Deliverables in `sv/requirements/commercial-legal/`:

| File | FRs | Prefix range |
|---|---|---|
| `01_merchant-registration.md` | 17 | SV-CML-FR-001..017 (C1; SOQ-25 config-slots) |
| `02_accounting-books.md` | 13 | SV-CML-FR-018..030 (**§3.7 = SOQ-28 retention matrix**) |
| `03_financial-statements.md` | 11 | SV-CML-FR-031..041 (C3; NIIF hook pointer) |
| `04_society-types.md` | 30 | SV-CML-FR-042..071 (C4; SAS = statute_pending, zero invented mechanics) |
| `05_society-lifecycle.md` | 26 | SV-CML-FR-072..097 (C5; quiebra = SOQ-24 terminology-only) |
| `06_commercial-agents.md` | 22 | SV-CML-FR-098..119 (C6; Art. 397 indemnity scale verbatim) |
| `07_empresa-mercantil-eirl.md` | 22 | SV-CML-FR-120..141 (C7) |
| `08_payment-instruments.md` | 23 | SV-CML-FR-142..164 (C8; Art. 995 prescription matrix verbatim; SOQ-26 config) |
| `09_sales-contracts.md` | 28 | SV-CML-FR-165..192 (C9; CC↔CAT-031 auto-translation BANNED) |
| `10_aml-compliance.md` | 32 | SV-CML-FR-193..224 (C10 rebased on 71_/72_/17_; R28 chain in every threshold FR) |

Totals: **224 FRs / 243 LBs / 132 ACs / 35 OQs**. Key encodings: 02 §3.7 =
the SOQ-28 longest-per-object retention matrix (CC 10y+5y-post-liquidation / facturas anexas /
24-month media migration / AML uniform 15y / DTE row by id to SV-EINV-FR-152..158+D3); CC
Art. 439-440 no-alteration cites e-invoicing §3.11 FR-159..164 as kin BY ID; ISR-vs-CC
reserva-legal disambiguation pointers (SV-TAX-FR-063/101); días-hábiles engine consumed by
id (SV-FREP-FR-202..204); AML sanctions in SMM units consuming payroll/02 by id; AML
regime cutover 2025-10-17 dated rows + adaptation windows (2026-04-09/07-09/10-17); law-wins
rulings ×2 (71_ Art. 24's 24h over 72_ Art. 43's 5-días; ≥25% beneficiario-final over 72_'s
10%) OQ-tracked. COVERAGE now 52 cited / 10 pending / 9 N/A / 1 superseded (72 rows);
README commercial-legal → In review (draft, S5); master-index S5 DELIVERED + SOQ-28 closed.
### El Salvador — W13 special-regimes evidence pass + D15 (COMPLETE 2026-08-19, pushed; see §5 ruling 42)
Sources read end-to-end + evidence **EVID-251..274** (4 files, 17 file-level OQs):
12_ ZF (title mislabel fixed — content = "Ley de Zonas Francas Industriales y de
Comercialización" D.L. 405-1998, consolidated through D.L. 318-2013) · 13_ LOA
D. 903 (through 121-2012) · 14_ LSI D.L. 431 (2007) + 17b_ Reglamento D. 131
(2008) · 31_ FOVIAL guide DG-002/2001 (COTRANS NOT covered — title defect,
MOQ-04 half-open) · 42_ Panamá DUCA-F (SIECA 03-mar-2025) · 43_ DUCA Res.
409-2018 · **74_ Ley de Simplificación Aduanera D. 529 ACQUIRED** (uif.gob.sv;
through D.L. 23-2012; damaged PDF qpdf-repaired). Key encodings for S7:
ZF ladders (usuario ISR 15/20y→60%→40%; municipal 100→90→75%; DPA 10/15y;
dividends taxed from 13th ejercicio; requisitos 17-A/19-A; breach split);
ZF aduanero clocks (12m improrrogable per DM; traslados 12/6/2m; TAN→ZF 0%
IVA + Ley IVA 76/77 = Art. 25); LSI (indefinite ISR exemption; 1.5% ISR + 1%
IVA local retentions Art. 8; **17b_ Art. 22 caps 50/40/30%**; 24m admisión
temporal ≠ ZF; semestral auditor dictamen; 90% Salvadoran staffing);
74_ (teledespacho chassis; presumed flete/seguro 1.25/1.50/10% FOB; **$18
inspection tasa** + biennial ≤10%; courier $200/$3,000; 5y records +
5y caducidad); DUCA 62-field contract (F = 30 días hábiles); FOVIAL
$0.20/gal outside IVA base + B2B control-account chain. **Numbering next =
75.** Acquisition gaps queued: Reglamento General ZF, **LESIA**, DUCA user
manual, Ley Fondo Vial + COTRANS instrument, current consolidations for
12_/13_/14_/17b_/74_, $18-tasa acuerdos. **Special-regimes synthesis (S7) is
NEXT**: master-index clusters + SOQ register → plan → subagent wave; D15
binding (per-acuerdo exemption rows; never global constants). External checks
this session: D.O. /seleccion still 500; MH formularios unchanged (no F-11
v19/v20, no F14 v17 manual); **UIF marco-legal hosts 74_ + "36-Ley-de-
Simplificacion-Aduanera" — its AML "Reglamento" PDF = D. 2-2000 verbatim
(duplicate of 17_; new D.L.-426 reglamento still absent — watch continues)**.

### El Salvador — SYNTHESIS PROGRAM COMPLETE (S1-S9 all merged; in `.worktrees/sv`, branch `sv-research`; S8 merged at aec9e5d 2026-08-20, S9 merged at 09847d0 2026-08-20)
**`sv/HANDOVER.md` was bootstrapped this session (bf87179) and is now the
authoritative SV cross-session memory — per-wave SV state lives THERE;
this root section stays integration-level.** **S8 (chart-of-accounts,
276 FRs SV-COA-FR-001..276) and S9 (IVA-core, taxation files 07-15,
178 FRs SV-TAX-FR-176..353) both landed 2026-08-20 — the 8-topic
program is COMPLETE: 1,605 FRs; COVERAGE 63 cited / 0 pending / 9 N/A /
1 superseded (73 rows, corpus FULLY cited).** Remaining SV program =
acquisition follow-ups (SOQ-46 NIIF-adopting instrument is the gating
gap), SOQ/external watches, deferred cleanups — owner's call per
`sv/HANDOVER.md` §8. Historical S7 detail follows. S7 = first worktree wave:
plan `docs/superpowers/plans/2026-08-19-s7-special-regimes-synthesis.md`,
subagent-driven 9 tasks (8 Approved clean + T1 one fix round), final
whole-wave review **MERGE-READY** (zero Critical/Important). Deliverables
in `sv/requirements/special-regimes/`: 8 files + index — **175 FRs /
130 LBs / 80 ACs / 42 OQs (SV-SPE-FR-001..175)**. Key encodings: D15
per-beneficiary exemption ladders (usuario 15/20y→60→40; DPA 10/15y;
desarrollista flat; administrador via 54-C ONLY — Arts. 14+15 derogated
by D.L. 318-2013 as printed); LSI indefinite-until-cessation rows +
17b_ Art. 22 caps 50/40/30; 12m-ZF vs 24m-LSI clock invariant; ZF
0%+76/77 vs LSI 75-77 route split; DUCA 62-field model (field 14 =
vencimiento per the 43_ print — master-index "33/56" was a prep error,
flagged); $18 tasa + presumed flete/seguro dated rows;
SMM-mayor-cuantía config default (SOQ-33); FOVIAL $0.20/gal per-unit tax
+ IVA-exclusion guard (31_ provenance chain, SOQ-39). S7 COVERAGE was
**60 cited / 3 pending / 9 N/A / 1 superseded (73 rows; 74_ row added)**
— the pending trio (02_/32_/33_) all closed by S8/S9.

### GT / HN — merged to main; branch-based country workflow (2026-08-19)

**Both `gt-research` and `hn-research` were rebased onto main and
fast-forward-merged 2026-08-19** (owner decision; policy honored: rebase
then merge, no force-push — hn-research's rewritten remote ref was updated
by delete + re-push, gt-research pushed for the first time). The
cross-country decision sets were unified the same day (see §5 rulings
42-43): **D15 (SV as-of doctrine) + D16 (GT-proposed date-driven
mechanics, HN-amended) are the shared canon**; country instantiations GT
D-GT10 / HN D-H2/D-H3 stay in their country docs.

**Country work model (binding from now on):**
- **Every country works in its own branch + worktree; `main` is the
  integration branch.** Worktrees: `.worktrees/gt-research`,
  `.worktrees/hn-research`, `.worktrees/sv` (branch `sv-research`,
  created 2026-08-19 — SV synthesis waves run there from now on; this
  main workspace is used for integration/merges only).
- Each country keeps its own cross-session memory INSIDE its tree:
  `gt/HANDOVER.md`, `hn/HANDOVER.md`, and (for SV) this root HANDOVER
  until SV work moves fully into the worktree. **Read the country
  HANDOVER before any country work.** Their in-progress state is NOT
  duplicated here.
- Merge country branches to main at milestones by owner decision
  (rebase-then-merge; never force-push; remote refs updated via
  delete + re-push when history was rebased). Milestones are normally
  session closes — standard protocol in §4.6.
- **Future countries: Chile, Colombia, Peru, Nicaragua, Costa Rica,
   Belize, Panama, Dominican Republic** (owner roadmap 2026-08-19; Chile
  added 2026-08-20; none started). All countries — sv/gt/hn and every
  future one — share the same base: `shared/docs/` + cross-country
  decisions D15–D19 (this file §5) are the binding canon; per-country
  rules are instantiations on top (D-H2/D-H3 model). "Bootstrap per the
  GT/HN pattern" refers ONLY to the mechanical scaffold for a new country
  (dir + research spec in `docs/superpowers/specs/` + own HANDOVER +
  worktree) — SV predates the recipe (pilot on main; `sv-research`
  worktree since 2026-08-19), not an exclusion from the shared base.
  **New-country bootstrap prompt (owner magic words):**
  `Bootstrap <Country> (<cc>): start the Odoo localization.` →
  controller runs the brainstorming/design session for the
  research spec, scaffolds the country dir, writes its HANDOVER, creates
  branch `<cc>-research` + worktree `.worktrees/<cc>-research`; from then
  on the standard loop applies (`Read <cc>/HANDOVER.md and continue.`).

**State at merge (updated 2026-08-19 W-GT3 close, branch-side):** GT =
source research COMPLETE (82 entries + 2 schema dirs; decisions D-GT1..10)
**+ EXTRACTION_PLAN approved + W-GT1 (FEL stack) + W-GT2 (taxation core) +
W-GT3 (payroll) evidence COMPLETE** — 14 evidence files committed
(EVID-001..370; Reglas = v2.0; OQ5/OQ6/OQ13 resolved; OQ12 disproven (IRTRA
flat 1%, D-1528/1962); OQ17 resolved-as-myth (D-10-2025 derogates IVA
8-"A" added D-31-2024); OQ11 still open (IGSS rates not in corpus);
40_/41_ bonus-law identities corrected — December aguinaldo D-76-78 =
missing acquisition candidate; Dto. 4-2019 = IVA Art. 29-"A" provenance;
D-GT9 establishment-field refinement — see `gt/HANDOVER.md` §5a/§5b/§5c);
next = W-GT4 fiscal-reporting evidence. Queue rev 6 in
`gt/DOWNLOAD_QUEUE.md`. HN = research + taxation
core COMPLETE (decisions D-H1..D-H3). Shared docs adopted: D16 canon,
`.gitattributes` byte-fidelity for gt/+hn/ sources (sv/ deliberately
exempt — predates the rule), `.gitignore` evidence exceptions pattern for
all countries.

**HN wave-2 merge (2026-08-20, fast-forward):** HN evidence now = taxation
core + **fiscal reporting COMPLETE** (EVID-001..185, ~160 open OQs; 103
registered files 01-104 gap 103; decisions D-H1..D-H3 = D16/D18/D17
instantiations). Round-5 acquisitions: STSS-308-2022 (SMM tables 2022/23),
Acuerdo 02-95 (14th-month reglamento, D.135-94 Art. 34 origin), D. 103 Ley
SMM. Key W2 encodings: Form 535 EEFF-prior gate (FY2024+); DJIMR 25-code
catalog; DMC = form 527, deadline 10d→20d→5d chain; tarjetas 523/215 outside
DJIMR; AS 5% RNG>L1M + ATN minimum tax (D.51-2003 = top acquisition lead);
selectivo 203 = separate D.58-1982 tax; 8 title-vs-content incidents total
(20_/52_ corrected this wave). Next per `hn/HANDOVER.md`: W3 facturación →
W4 payroll → synthesis (master index + S-waves).

## 4. How work is done here (process that has proven itself)

1. **Skills discipline**: superpowers skills are mandatory gates —
   brainstorming before design, systematic-debugging before fixes,
   subagent-driven-development for plan execution. Use them.
2. **Extraction waves** (per `requirements-extraction-procedure.md`):
   extract text → per-document evidence pass (verbatim quotes, EVID-nnn,
   loc/gloss/candidate-CR/topics/doubts, OQs at file end) → plan-log entry →
   commit. Evidence NEVER paraphrases; doubts become OQs, never guesses.
3. **Synthesis waves** (S1 pattern): prep (digest reads + master-index merge)
   → plan doc with tasks/global constraints → subagent loop (fresh
   implementer per task; every FR cites LB; reviewer verifies against master
   index + schemas; fix rounds; ledger with rulings) → final whole-wave
   review → ONE fix wave → push → delete workspace. Preserve rulings by
   copying them into THIS file at wave close (the SDD workspace is deleted).
4. **Supersession discipline**: when a newer source arrives, capture
   delta/effective-date/adaptation-window BEFORE synthesis; mark superseded
   files in the registry; old EVIDs stay as history.
5. **Commit style**: short imperative, no emojis. Push after waves.
6. **Session close & merge protocol** (standard from 2026-08-19; applies to
   every country branch — currently `hn-research`, later `sv-research` /
   `gt-research`):
   - At session start (any country work): `git config core.editor nvim`
     (repo-local agent override; see §6 — unset again at close).
   - At session end the owner asks: *"So `Read <cc>/HANDOVER.md and
     continue.`? Want to merge before we nuke this session?"* — the country
     named in the prompt is the branch being closed (e.g. hn →
     `hn-research` in `.worktrees/hn-research`).
   - Controller closes out: refresh the country HANDOVER (state-at-stop +
     next actions), commit + push the branch; then
     `git config --unset core.editor` to restore the owner's VS Code git
     editor (§6).
   - Owner forks: request changes (session continues) OR nuke (end
     session).
   - **Before nuking, merge the branch back to main:** (1) review what
     happened last on the branch (`git log main..<branch>` — session
     commits feed the merge record); (2) rebase the branch onto main's tip
     — this also picks up any procedure/policy changes committed to main
     since the last merge, so the close follows current procedures; (3)
     merge into main (fast-forward after rebase), write the merge record
     into THIS file §3, commit + push. Never force-push; rewritten remote
     branch refs are updated via delete + re-push.
   - A fresh session bootstraps with the prompt: `Read <cc>/HANDOVER.md and
     continue.`

## 5. Decisions & rulings register

### S0.5 product decisions (binding, in saas-thin-client-architecture.md)
- **D1** Fly.io multi-region SaaS; NO local generation fallback; residual
  partition risk framed as force majeure (CT 119-F logic).
- **D2** SaaS generates/sequences/transmits; **Odoo signs** (cert vault,
  JWS RS512, per-environment certs); **private minimal protocol** (wire
  format deliberately unlike MH JSON); dual validation both ends.
- **D3** Archive tiers: mandatory client mirror (Tier A, legal baseline) +
  paid SaaS hosting (Tier B, export guarantee).
- **D4** Hard entitlement wall on generation; escalating email + Odoo
  banners; entitlement state in EVERY protocol response.
- **D5** LGPL-3 client + trademark reserved; SaaS proprietary; AGPL/OPL
  rejected (reasons in doc).
- **D6** Hybrid multi-country protocol: shared core (auth/entitlement/
  archive/state/webhooks) + namespaced payloads (`sv:`, future `gt:`),
  semver per namespace.

### S1 wave rulings (ledger deleted; preserved here)
1. Master index/evidence were scratch → **SUPERSEDED 2026-08-17**: user
   decided to commit them (gitignore exceptions). The committed index
   already contains the EVID-013 addition and the R7 erratum fix.
2. Controller applied 4 review-specified mechanical fixes directly (T5
   LB-002 path + corrections log; T7 44_ filename; README count) — each was
   a one-line review finding; documented, no review bypass of substance.
3. **Contingencia schema version = 4** (schema const in 52_ zip beats the
   digest's "3"); master-index R7 amended accordingly; 03_events FR-088
   asserts 4 with OQ-001 recording the erratum.
4. CAN-STAND minors deferred (logged below in §9).

### Schema-pass rulings (2026-08-17; recorded in-file + master index)
5. **Wire keys beat the digest**: DTE N°84 = `codTributo` ("Tributo sujeto a
   cálculo de IVA"); N°7 = `tipoOperacion`; CRE = `montoSujetoGrav`; eret
   `emisor.tipoItemExpor`, `resumen.totalCompraExcluidos`; eop cuerpo
   `docDel`/`docAl`; identificacion `fusion` (singular, NC/ND/CR/CL + eret +
   invalidación); domicilio fiscal = `codDomiciliado` on BOTH surfaces
   (receptor CDE/CLE and ventaTercero — not "domicilioFiscal"). DG45's
   divergent names are OCR/digest artifacts, not the wire.
6. **Type codes**: schema `tipoDte` consts pin CAT-002 v1.1 exactly
   (F=01, CCF=03, NR=04, NC=05, ND=06, CR=07, CL=08, DCL=09, FEX=11,
   FSE=14, CD=15). DG45 §3.3 parentheticals (15/16/17) = errata; Anexo V
   N°48's "16" = ghost code (no catalog referent) — codigoGeneracionR
   null-set = {05, 08, 17, 18}.
7. **subTotal sign**: Anexo IV N°139 (raw) = sumatoria − global discounts,
   uniformly (FE/CCFE/NRE; FSEE variant) — 2022 CCFE "+" was the copy-paste
   defect. FR-022 stands.
8. **2-year invalidation window** (Anexo V N°9 rule 7): binds invalidación
   AND retorno, FE/FEXE only (not FSEE), from the target DTE's seal date,
   conditional on the target's emisor activity code ∈ {21001, 21008, 46482,
   46484, 46491, 47721}. FR-103/104/117 amended.
9. **Signing identifiers**: both normativas' example `firmaElectronica`
   header base64-decodes to `{"alg":"RS512"}` — the printed "RSA512" is the
   regulator's typo; "CAGES" = CAdES (18_ v1.2 twin row prints it clean).
   Operative: JWS / RS512 / PKCS8EncodedKeySpec.
10. **DCLE cuerpo** = single object (no array) — item caps inapplicable;
    motivoContingencia/motivoContin maxLength 500 (both schemas);
    event apéndice exists only on eret/eop among events.

### Regulatory-change session rulings (D7–D12, 2026-08-17 — in regulatory-change-management.md)
11. **D7** SaaS MH-spec runtime = replace-in-place + switchover dates
    (Cuadro 4 windows are configuration; no old-spec engine; Odoo sees only
    private-protocol semver).
12. **D8** Catalogs = immutable releases via SaaS feed (set-level atomic
    units; "code X at date D" lookup; catalog changes are data events, not
    module upgrades).
13. **D9** Reporting = freeze at filing + post-time amounts; rectificativas
    from frozen snapshot + adjustment moves; tax changes additive-with-
    cutover. **Correction corollary:** corrections always post as new
    entries in the correction period; originals immutable; invalidation
    reversal non-editable full mirror; retorno credit; origin-rate FX reuse
    (→ 02 §3.11 FR-159..164).
14. **D10** Dual-version disposition matrix accepted; protocol carries MH
    schema version per document record (06 OQ-008 formalizes).
15. **D11** Normative packs + "cambio de normativa" wizard Odoo-side; MH
    deadlines bind the SaaS, not the client; newest branch first, additive
    backports 17–20.
16. **D12** Repo conventions: template §5 version-regime note; W5.5
    supersession-map pattern standing for every wave; D7–D12 binding for
    synthesis.

### S2 wave rulings (2026-08-18; preserved from the deleted SDD ledger + master index)
17. **R17 (master index):** Reglamento provenance — 04_ = D.E. 101-1992
    consolidated incl. reform D.E. 117-2001 (self-printed REFORMAS block);
    54_ tail's listing is editorially partial. Repeal authority = D.E.
    117-2001, NOT the CT.
18. **R18:** foreign-source income tracks DEAD per D.L. 969-2024 (effective
    2024-03-22): Art. 3.4 exclusion + Art. 14-A 6º-8º / Art. 16 4ºc)/5º/7º /
    Art. 27 2º-4º derogated; domestic 10% tracks survive; EVID-092 gross-up
    dead for foreign rents.
19. **R19/R20/R21/R22:** 53_ tables operative (NET base per literal d)) over
    10_ historical; Art. 37 = two dated vintages (957-2011 ≤2025-05-07;
    293-2025 from 2025-05-08); pago mínimo never implement (void 3 ways);
    aguinaldo Ley 4.16 governs over CT 155-II (vintage rows 2014-24).
20. **SOQ-01 verdict:** capital gains = Ley Art. 42 flat 10% (>12mo) current
    law; Reglamento Art. 17 media-tasa = historical method only (stale rate
    anchors; stamp (14) = D.L. 496-2004 on Art. 42).
21. **SOQ-04 verdict:** NO general NOL carryforward exists in the corpus
    (CT "pérdida" hits are all document-loss/sanction contexts); only the
    capital-loss 5y ledger (Art. 14/14-A).
22. **CT Art. 62** = the FX conversion rule (hecho-generador-day rate;
    installment FX deltas into base; payment-date FX difference never in
    base) — read from 05_ raw txt lines 840-844 (controller, 2026-08-17).
23. **SDD-process rulings:** execute on `main` per repo policy (no
    worktree); "tests" = structural verification commands (no suite in
    repo); forward cross-file refs cite file+§ (resolved into ids at final
    review — all verified); Task 7 carried the master-index SOQ strikes
    (plan gap, controller-added interface).

### S3 wave rulings (2026-08-18; preserved from the deleted SDD ledger)
24. **Forward file+§ refs allowed** (S2 precedent reused): 06→07 §3 catalog
    forward-reference; all resolved/verified at final review.
25. **Extraction .txt counts as LB-citable source**: evidence files summarize the
    extraction txts; when the evidence file abbreviates a verbatim table (e.g. F-07
    §XXI-XXIV column maps), implementers cite the txt with page anchors — OQs only for
    data absent from every corpus file.
26. **Taxation 04 OQ-007 answered (ISR side)**: F-910 = the CT 123 annual retention
    report (pointer wired in taxation 00_index + 07 §3.3); 05 OQ-002 partially answered
    (F-915 format published; norms resolution still absent); 05 OQ-006 answered-kin
    (F-14 codes 43-46 + F-910 + F-915). IVA-side surface = F-930 (04 file owns the view).
27. **Casilla semantics honesty rules** (from fix rounds): unprinted wirings
    (146/151, 155→110, 167→164) recorded-but-unwired with OQs — never invented into
    formulas; sign convention = positive magnitude entered, formula subtracts
    (520/523/81/131/550/551 harmonized); two-decimal discipline = computation rounds
    never, export truncates (FR-027/030 aligned).
28. **README source-count fix**: registry recount = 62 files (the S2-era "50" +
    53-64); controller's interim 56 was a miscount — corrected in 595eec1.

### S4 wave rulings (2026-08-18; preserved from the deleted SDD ledger)
29. **R23/R24 (master index):** pensioner-health cotización = **7.80%**
    (09_ Art. 154, later-in-time — supersedes 08_ Art. 29's 6%); 09_'s
    registry title is a MISNOMER — content = Ley INTEGRAL del Sistema de
    Pensiones D.L. 614 (effective 2022-12-29), which DEROGATES the SAP
    (D.L. 927-1996): only Art. 16's 16% (7.25/8.75) is citable; SAP-era
    rate lore is dead text.
30. **S4-process rulings:** execute on main (S2/S3 precedent); tasks strictly
    sequential (FR-numbering chain — worked cleanly 001..137); caps discipline
    = value-level-only from the F-14 print with instrument-OQs (never
    arithmetic-derived — e.g. "$30 ÷ 3% = $1,000" is NOT corpus fact);
    caña-floor→agrícola + tail-week + 4×SMM-sector readings ship as disclosed
    working assumptions with OQs (SOQ-18 family); Art. 311 VOID = never-
    implement invariant with negative AC; 01's crosscheck-OQ family resolved
    in-wave by 08 §3.2.

### W10/S5-prep rulings (2026-08-18; recorded in master index Section B)
31. **R25/R26:** 15_'s registry title was a mislabel — content = **Ley Contra el
    Lavado de Dinero y de Activos, D. 498/1998** (third title-vs-content incident
    after 29_/09_; row amended). 17_ reglamento (D. 2-2000) is PRE-REFORM: its
    colones ¢500k threshold + 3-días-hábiles clock are superseded by 15_ Art. 9
    ($10k/$25k + 5 días hábiles, post D.L. 568-2013); 17_ citable ONLY for window
    mechanics (rolling 30-continuous-days-back-from-last-transaction anchor),
    no-tip-off, liaison notice, and red-flag catalogs; current reglamento
    acquisition queued (SOQ-27).

### S6 wave rulings (2026-08-18; preserved from the deleted SDD ledger)
32. **R27 (master index, recorded by the wave):** the four in-file Quincena-25
    rulings carried corpus-wide — casilla **724 operative** (734 = guía typo
    [sic]); annex-CSV delimiter = **semicolon** (70_ header beats the "comas"
    type-label); January-window = **every January from 2026** (68_'s
    "exclusivamente Enero 2026" = publication-moment phrasing); 66_ Condición
    especial = **Art. 3 positional [sic]** ("Art. 5" prints twice).
33. **Ruling (T1 fix):** quincena_25 sits OUTSIDE FR-001's three CT categories
    per 66_ Art. 1's independence declaration — matrix Category cell = "none —
    special-law benefit outside the CT categories"; `sv_pay_earning_category`
    stays empty for Quincena rules; FR-001 select NOT extended.
34. **Ruling (T6 fix):** credit entity = `l10n_sv.isr.quincena.credit` (repo's
    uniform `l10n_sv.isr.*` taxonomy overruled the plan-pinned
    `l10n_sv.tax.*` name).
35. **S6-process rulings:** index tables are authoritative over plan arithmetic
    (T7); CSV `catalog_version` enum extension `f17_kin` = deliberate
    dated-authority marker (code 73's authority = MH package 67_/68_, not a
    v17 apéndice that doesn't exist); gloss-only LBs marked as gloss (66_ Art. 8,
    69_ §H — no verbatim exists; never fabricated); controller applied ONE
    one-line residual fix directly (frep index OQ-009 status sync — S1
    precedent ruling 2).

### S5 wave rulings (2026-08-18; preserved from the deleted SDD ledger)
36. **Module-design decisions D13/D14 (user, mid-wave; recorded in
     `shared/docs/odoo-localization-guide.md` §EDI, binding on all future
     Odoo Mapping rows):** **D13** journal model = `l10n_latam_invoice_document`
     — ONE journal, MANY document types (`l10n_latam.document.type` per DTE;
     move-level `l10n_latam_document_type_id`/`_number`; per-type journals
     REJECTED; same pattern as official latam localizations). **D14**
     establishment model = Odoo warehouses → establecimientos (M/B/S/P+3 →
     numeroControl sección 3 + `codEstablecimientoMH` M000/S000/B000/P000);
     caja/punto de venta = first-class concept in numeroControl positions 5-8
     (P+3) + `codPuntoVentaMH`; sequence space = (type, establecimiento,
     punto de venta) with year-reset consecutive — per-(establishment,PV)
     partition = DISCLOSED WORKING ASSUMPTION (corpus pins only year-reset +
     calendar-year uniqueness). D13/D14 orthogonal (journal×doctype ×
     warehouse×establishment × caja×PV). No existing file assumed the
     per-type-journal model → no retroactive amendments needed.
37. **Quote-fidelity rulings (wave-wide):** silent truncation of a statutory
     catalog = Important-grade defect (T1: Art. 422 a)-j) completed);
     single-word deviations = defects (T5 "Dichos"→"Dicho"; T9
     "indubitable"→"indudable" ×2 — Critical-grade); truncation-marker
     convention = "(first N…; X omitted — topic)"; omission markers must
     describe what is ACTUALLY omitted (T9 I-1: Art. 1043 marker mis-scoped
     the matrícula rule into Art. 1044-III); full-file programmatic
     verbatim sweeps against the extraction txt are the norm.
38. **Interpretive working readings (labeled in-file, OQ-tracked where
     corpus-silent):** Arts. 282-286 read as the sociedad/EIRL-cycle
     statements regime (they sit in the S.A. title; Art. 474-grounded);
     Art. 442 = Art. 459 one-register reading; Art. 15-vs-452 simplified-book
     coexistence; Art. 451 retention anchor = register-close working anchor;
     Art. 469 matrícula-gate non-binding on constitutive inscription;
     estatuto contradiction check = warning-only; Art. 313 last-trimester
     boundary. Brief-vs-evidence conflicts resolve FOR the evidence (T7: the
     plan's "≥3/4 paid at constitution" AC example had no statutory basis —
     AC encodes Art. 609's actual 1/4-of-paid-capital rule).
39. **Config-gap disciplines:** commission rates ("usos del lugar") +
     distribuidor-indemnity inputs ship NO defaults (worksheet only);
     Economía legal-interest rate = SOQ-26 dated config never hardcoded;
     colones remnants ("un mil colones" Art. 1038) = config-gap OQ with NO
     invented USD conversion; **CC↔CAT-031 Incoterms auto-translation
     FORBIDDEN** (OQ — mapping must come from evidence); Ley de Competencia
     checkpoint states + MINEC registry interface + Ley Registro de Comercio
     epochs/fees = acquisition/config OQs; SAS = statute_pending with ZERO
     invented mechanics (populate from the statute when acquired ≥74).
40. **AML law-wins rulings (T10, OQ-003-tracked):** where the kept
     instructivo diverges from the new law, the LAW wins — 71_ Art. 24's
     24h transmit clock over 72_ Art. 43's 5-días; 71_'s ≥25%
     beneficiario-final threshold over 72_'s 10%. Re-verify both when the
     new instructivo issues (EV71 OQ-1 watch).
41. **S5-process rulings:** same SDD pattern as S2-S4 (main-branch execution,
     structural verifications as tests, per-task reviews + one final fix
     wave, push at close); controller applied ONE one-line residual directly
     (05 LB-020 gloss typo — S1 precedent ruling 2); the final-fix subagent
     died pre-report — controller verified its diff item-by-item (incl. the
     LB-027 source-check at txt:7998) before committing; ledger preserved
     here before workspace deletion.

### Applicability-windows session rulings (D15, 2026-08-19 — in regulatory-change-management.md)
42. **D15 as-of doctrine (user session, binding on all remaining waves):**
    dated legal parameters = immutable dated rows (`valid_from/valid_to`),
    resolved **as-of the domain's anchor date** and **snapshotted onto the
    record at creation** (never re-resolved; corrections use ORIGINAL-period
    parameters). Anchor table per domain in the decision doc (IVA=invoice
    date; retención=payment period; declarations=declared period frozen at
    filing; SMM-derived=period with OQ-tracked straddle assumptions;
    ZF/LSI/DPA=per-acuerdo company schedule; AML=transaction date vs
    2025-10-17; Quincena-25=window+year flags). Transactional taxes also
    version the `account.tax` record (Odoo-native snapshot; D7/D11 packs);
    CSV sidecars = seed rows. **No retro-transmission ever**; history =
    read-only external records (historical DTEs imported emitted-externally +
    non-blocking MH-consulta validation; payroll monthly aggregates + tenure
    records, not payslips; ledger/stock/banks = opening balances; physical
    pre-DTE invoices = config-gap OQ). **Payroll corrections hybrid by
    window:** period open → replace in place; filed → immutable original +
    delta slip in correction period under original rules. Retro-consistent
    with S1–S6 (S4/S6 dated-config disciplines were its precursors); template
     §5 + guide updated; new OQ families recorded (straddle anchors;
     pre-DTE import; physical-invoice gap).

### Cross-country unification rulings (2026-08-19 merge session)
43. **D16 canon + branch workflow (owner decisions at the gt/hn merge):**
    (a) GT's branch-proposed "shared D13" (date-driven compliance mechanics)
    became **D16** — renumbered (D13/D14 taken by journal/establishment
    models), reconciled with D15 (D15 = anchor table + snapshot-on-write +
    history contract; D16 = mechanics canon), and AMENDED with HN's
    contributions promoted cross-country: hard no-override emission block
    outside authorization-range vigencia (D-H2) + ingestion reconciliation
    against previously-FILED declarations (D-H3, D16 ¶7). Template §5 +
    guide cite D15+D16 jointly. (b) **Branch-based country workflow**: all
    countries (incl. SV from now on — `.worktrees/sv`, branch
    `sv-research`) work in branches/worktrees; main = integration; merges
    at milestones, rebase-then-merge, never force-push; remote refs fixed
    via delete + re-push after rebase. (c) `.gitattributes` byte-fidelity
    extended to hn/ (sv/ deliberately exempt — predates the rule; needs a
    byte-fidelity migration pass first). (d) Colombia + Peru planned as
    future countries (not started). (e) gt-research + hn-research MERGED to
    main 2026-08-19 (18 + 22 commits rebased; conflict surface: root
    HANDOVER GT/HN section, shared decision doc D13-vs-D15, .gitignore EOF
    union + one stale-line fix).

### Universality + D17 rulings (2026-08-19, second merge-session commit)
44. **Shared docs are country-neutral; examples live in instantiation
    registers.** D15 rewritten universal (generic anchor-date pattern
    table; SV citations moved into a labeled "Country instantiation
    register" — illustrative for other countries, never normative across
    borders; GT/HN pointers already there; future countries append at
    synthesis time). Template §5 + guide scrubbed to match.
45. **D17 — document-type model cross-country default** (guide, binding):
    `l10n_latam_invoice_document`, ONE journal / MANY document types, is
    the default for every country in scope — the official Odoo pattern for
    regulator-defined document-type families (l10n_ar/cl/co/ec/pe/uy;
    **Colombia uses it** — Factura de Venta/NC/ND; Peru too — owner
    confirmed; Mexico = the known single-document exception shape,
    deviations need explicit rulings). Countries verify dependency +
    document-type catalog at bootstrap. SV D13/D14 relabeled as SV
    instantiations of D17 (numbers unchanged); establishment/point-of-sale
    mapping stays per-country (D14/D-GT9/D-H1).
46. **Country roadmap expanded (owner 2026-08-19):** planned after the
    current three — **Colombia, Peru, Nicaragua, Costa Rica, Belize,
    Panama, Dominican Republic** (none started; bootstrap per the GT/HN
    pattern — scaffold + research spec + own HANDOVER + worktree). Note
    Belize is English-speaking/common-law (GST world) — expect the Spanish-
    Latam extraction template to need adaptation there.
    **Chile added to the roadmap (owner 2026-08-20):** intent recorded,
    not started — SII e-invoicing (folio/CEDN environment), IVA 19%,
    Spanish civil-law; fits the existing extraction template; strong
    upstream `l10n_cl` ecosystem to verify against at bootstrap.

### D18 mid-year go-live rulings (2026-08-19, owner session)
47. **D18 ingestion mechanics (owner-approved with two amendments):**
    driver = mid-year go-lives (straddle-FY + prior-FY filings must compute
    complete without re-processing). Tiered contract T1-T4 (T1 straddle-FY
    transactional detail as `is_historical` records in HISTORICAL journals
    keeping their natural journal TYPE — owner's grouper pattern;
    T2 prior-FY filings as frozen D9 declaration snapshots; T3 opening
    balances; T4 carryover dated rows). Flag semantics: set only by import
    tooling; posted ⇒ immutable; suppresses legal sequences/transmission/
    matching/recompute, allows validation+posting with ORIGINAL-date
    tax-grid resolution (snapshot-on-write; suppress recompute ≠ suppress
    resolution). Journal-record bidirectional cross-check + flag-flip lock
    while contradicting transactions exist; journal-less models = record
    flag alone. Corrections: PRIMARY = import-batch atomic reversal;
    surgical = ONE global res.config.settings gate (per-type flags
    rejected) + immutable audit entries; deletion blocked when referenced
    by live posted records or filed snapshots. D15(c) ledger line amended
    accordingly; guide + template §5 cite D18.

### D19 go-live/cut-over rulings (2026-08-19, owner brainstorm session)
48. **D19 cut-over mechanics + go-live-readiness doc (owner-approved after
    3 amendment rounds):** (a) posting tiers — closed items GL-neutral via
    config migration/clearing account (XML-ID default), open items real
    (subledger ↔ `00/ZZ` control accounts, config w/ XML-ID defaults,
    matching suppressed, payments route to control); (b) legacy amounts
    VERBATIM (Odoo matches legacy rounding; residuals absorb drift);
    (c) sequence init via canceled GL-neutral **`is_sequence_init`**
    records in LIVE journals (owner correction: NOT is_historical —
    journal invariant forbids it; read-only flag, set only by server
    action/special import) — sequences + range counters (CAI kin) derive
    from imports, users never type first numbers; (d) straddle-filing
    checkpoint = explicit deployment choice (predecessor-filed T2
    snapshot vs Odoo-files-complete); (f) trial-balance ROUTING not
    restriction (owner correction: TB lines post to real accounts
    unrestricted; only control-set lines route to control accounts;
    residual detection via control-account netting; consistency
    validation only). Scope OUT: parallel-run tooling, decommission/
    retention, rollback (logged). NEW shared/doc `go-live-readiness.md`
    (universal concern catalog + SV/GT/HN registers seeded — verify at
    each synthesis close). D18 amended (T3 elaborated; posting modes).
    Guide + template §5 cite D19.

### Standing policies

- Evidence-based answers only; RAG (NotebookLM) is validator, never source
  (notebook `c7ca0391-4822-4d3c-8090-b0d8c147ba94`, owner
  c20260202@gmail.com; MCP: github.com/jacob-bd/gemini-notebook-mcp-cli).
- Hint layer = tuky-workspace repo (github.com:CtrlCarlitos/tuky-workspace,
  `projects/odoo-localization-el-salvador`) — pointers only, never LB.
- Takumi builds thin clients only (D2); SaaS is Elixir, separate codebase.
- **Canon evolution (owner 2026-08-20):** `shared/docs/` and
  `shared/scripts/` evolve with every country — when a localization's
  documentation drifts from what existing tools/procedures handle, first
  modify or extend the SHARED asset (new script, amended procedure), not
  the country tree alone; rulings worth generalizing get promoted from
  country decisions to cross-country D-numbers (D16/D18 promotion
  pattern). Uniform requirements extraction across countries is the
  standing objective.

## 6. Environment & tooling (this machine)

- **Git editor (repo-local override):** global `~/.gitconfig` sets
  `core.editor = code --wait` (VS Code popup — owner wants it for manual
  work). That popup blocks/aborts agent-driven commits, so agent sessions
  run `git config core.editor nvim` (repo-local `.git/config`, shared by
  all worktrees) **at session start**, and
  `git config --unset core.editor` **at session close** (§4.6) to restore
  the VS Code behavior. Owner never edits `~/.gitconfig` for this.
- **Python**: 3.14, NO system pip. Venv `~/.venvs/localizations`
  (pypdf, openpyxl, ocrmypdf, xlrd, python-docx). Run scripts as
  `~/.venvs/localizations/bin/python shared/scripts/...`. Setup documented
  in root README "Development environment".
- **System packages** (installed): tesseract-ocr + tesseract-ocr-spa,
  ghostscript, qpdf, unpaper. No passwordless sudo.
- **Scripts**: `shared/scripts/extract_text.py` (PDF/XLSX/XLS/DOCX/MD →
  `sv/.extractions/` with `=== PAGE n ===` markers; `--check`; `--ocr`;
  auto qpdf-repair for damaged PDFs), `build_catalogs.py` (catalogs → 33
  CSV sidecars; v1.1-aware; `--pdf` overlay path is legacy-2022 — see §9).
- **OCR quirk (critical)**: Diario Oficial scans (watermarked pages) need
  `--tesseract-pageseg 6`; default PSM returns near-empty text (hit on 44_).
  **D.O. TABLE pages need PSM 4 at 400dpi** (PSM 6 merges table rows into
  digit soup; hit on the D.E. 10-2025 tables 2026-08-18 — considerandos stay
  PSM 6). MH form PDFs and manual scans OCR fine under the script's defaults.
- **Fetching from factura.gob.sv**: wpdmdl download-manager LABELS DO NOT
  MATCH CONTENT (IDs were shuffled). Always verify by reading page 1 with
  pypdf. Known IDs as of 2026-08-16: 4388=Manual Tecnológico v2.0,
  4728=Normativa v2.0, 4725=catalogs XLSX-as-pdf, 5353=catalogs XLSX,
  4399=schemas zip, 4726=Manual Funcional, 4397=eventos manual,
  4398=estructuras manual v1.6 (237pp). Re-verify before reuse.
- **Diario Oficial volumes (recipe, verified 2026-08-17; OUTAGE 2026-08-18 ≥13:55)**:
  `POST https://www.diariooficial.gob.sv/api/v1/diarios-disponibles`
  (form data `year`, `month`) → JSON rows with `Id`/`NombreArchivo` →
  `https://www.diariooficial.gob.sv/seleccion/{Id}` serves the full volume
  PDF (opens with EMPTY password in pypdf). **The `/seleccion/{Id}` route
  returned HTTP 500 server-wide (all Ids, both UAs) from 2026-08-18 ~13:55 —
  retry on next session; the API listing route still works.** Online copies
  are watermarked "SOLO PARA CONSULTA — NO TIENE VALIDEZ LEGAL" (fine for
  extraction). D.O. scans OCR only under tesseract PSM 6 (same quirk as 44_);
  **D.O. TABLE pages need PSM 4 at 400dpi** (PSM 6 merges table rows into
  digit soup; verified again on 16_ — gs rasterize + `tesseract --psm 4`
  recovers labels/values PSM 6 loses).
- **Asamblea consolidations**: asamblea.gob.sv was network-unreachable
  2026-08-17 AND 2026-08-18; the official-mirror route that worked is the DGA (Aduanas)
  WordPress download-manager: fetch the `/download/<slug>/` page, parse the
  embedded `?wpdmdl=<id>` href, download that (plain URL of the file 404s —
  the degree-sign `°` in filenames gets mangled).
- **UIF Marco Legal (verified 2026-08-18 — the W12 route find)**:
  `https://www.uif.gob.sv/marco-legal/` hosts direct wp-content PDFs of current
  laws (D.L. 426 AML law, kept Instructivo 380, D.E. 2-2000 reglamento, Código
  de Comercio, Código Tributario, Ley Bitcoin set). Watch it for the pending
  new AML reglamento/instructivo (71_ Art. 56 deadlines already past as of
  2026-08-18). Its Código-de-Comercio PDF is structurally damaged server-side
  (broken page tree; qpdf fails) — rebuild with `gs -o out.pdf -sDEVICE=pdfwrite
  in.pdf` then extract. Its PDFs sit behind Incapsula: HEAD requests return
  500-with-HTML; plain GET with a browser UA works and returns the full file.
  Related UIF pages: /guias-y-manuales/ (goAML registration manuals,
  ROS buenas prácticas, compliance-manual guide), /senales-de-alerta/,
  /tipologias/. CNR creaempresa (creaempresa.cnr.gob.sv) confirms SAS
  constitution services ("Asesoría virtual SAS") — society-creation flows are
  behind eCNR login.

## 7. Gotchas & verified lessons

- Catalog version numbers are NOT monotonic (2022 v1.2 → 2026 v1.1
  re-versioning). Trust publication dates only. CAT-013 was restructured to
  the 44-municipio model (codes RE-ASSIGNED) → modules must store dated
  catalog rows, never replace in place (SV-CAT-FR-007..010).
- CAT-008 (Distrito) has 263 rows; EVID-086's "~75" estimate is wrong
  (sidecar is authoritative; already handled as OQ-005 in catalogs file).
- FE receptor threshold is **≥3 salarios mínimos** (D.L. 487 CT 119-G VII);
  the old $200 is superseded but appears in 2022 manuals.
- FE prices IVA-inclusive vs CCFE net+IVA (Ley IVA Art. 57) — resolved R1.
- Invalidación deadlines are differentiated per type (1d / 10 háb / 4d /
  3mo / special 2y codes) — see 03_events FR-103 + DG45 §2.2/§3.2.
- Two NEW 2026 event types: **Evento de Retorno (18)** and **Evento de
  Operaciones Especiales (17)** — FVS (physical simplificada) is alive as a
  paid-tier reporting regime via EOP, not an electronic DTE.
- NCE IS contingency-eligible (contradiction resolved: only CLE/DCLE/CDE
  excluded).
- `17_Reglamento_Lavado_Activos.pdf` is structurally damaged (renders in
  pdf.js, fails strict parsers) — auto-repaired via qpdf in the script.
- `docs/superpowers/` holds process artifacts (specs/plans) — keep using it.
- **MH formularios page** (mh.gob.sv/servicios/formularios-tributarios-para-descarga/):
  direct wp-content URLs (no wpdmdl shuffling); forms verified 2026-08-18: F14-V17-1.pdf
  (2026-06, still NO v17 manual/plantilla — SOQ-09 open), F07_V14_COMPLE.pdf (= our 39_,
  updated 15-08-2025), F910=PMHDC8240, F915=PMHDC8241, F-930=PMHDC8242, F935v1.pdf
  (2025-10), **F11-V18.pdf = acquired as 65_ (2026-08-18)**. Watch for F14 v17 manual +
  newer F910/F915/F930 prints + **F-11 v19/v20** (v19 = casilla 319 Quincena-25 credit,
  still printing dead pago-mínimo rows; v20 = "Sujetos con Régimen Especial" + certificado
  anexo — discovered via 67_ Anexos 1/8, 2026-08-18; acquisition candidates ≥71).
- **29_ mislabel**: `29_Modificacion_Anexos_F07_F14.pdf` is actually the F985/F-975 CNR
  Registro de Comercio manual (CT 121 a)2) — the annex-modification resolutions
  are NOT in the corpus (SOQ-12).
- **09_ misnomer** (W9): registry title says "Ley del Sistema de Ahorro para
  Pensiones" but the content is the NEWER **Ley Integral del Sistema de
  Pensiones D.L. 614 (2022)** which derogated the SAP — row amended; trust
  content, not old titles (same lesson as 29_, opposite direction).
- **CT Art. 311 is VOID** (sent. 105-2014, D.O. 225 T.417 1-dic-2017):
  maternity-benefit tenure gate produces no legal effect — never implement.
- **F-11 v18 + F-14 v17 both still PRINT dead pago-mínimo casillas** (Dec.
  762/2015 references) — R21 discipline: never feed, flag as print-vs-law
  defects.

## 8. Next actions (ordered)

1. ~~**DTE schema pass**~~ **DONE 2026-08-17** — 10 OQs + 4 MOQs closed;
   rulings 5–10 above; resolutions recorded in-file and in master-index
   Section C.
2. ~~**Regulatory-change socratic session**~~ **DONE 2026-08-17** — D7–D12
   decided and recorded (see §5 register + regulatory-change-management.md);
   template/guide updated; correction corollary → 02 §3.11 FR-159..164.
3. ~~**S2 ISR wave**~~ **DONE 2026-08-18** — extraction/evidence (W6/W6.5/W7),
   prep (master-index T1-T8 + R17-R22 + SOQs), synthesis (172 FRs, 6 files +
   index + CSVs), final review clean. See §3 S2 section.
4. ~~**S2 next wave — F-07/F-14 fiscal reporting**~~ **DONE 2026-08-18** — W8 evidence +
    acquisitions 59_-64_ + S3 synthesis (208 FRs, 8 files + index + CSV). See §3 S3 section.
5. **S2 remaining waves** (each: extraction → evidence → synthesis):
     (a) ~~Quincena-25~~ + ~~S6 fold-in~~ + ~~S5 commercial-legal~~ **ALL DONE
      2026-08-18** (§3 sections above); (b) **NEXT = special-regimes synthesis**
      (12_/13_/14_/17b_/42_/43_; D.L. 598-2020 + EVID-167 tail laws; consumes the
      W11 certificado — `special-regimes/00_index.md` stub exists; extraction +
      evidence pass FIRST (none of these sources read yet), then master-index
      clusters + synthesis; hunt D.L. 598-2020 + Ley ZF reforms when official
      routes recover). **Binding: D15 as-of doctrine (§5 ruling 42) — the ZF/
      LSI/DPA exemption schedules are the canonical D15 consumers (per-acuerdo
      dated rows + 60/40 phase-down ladders, never global constants). **W13
      evidence pass + 74_ acquisition COMPLETE 2026-08-19 (see §3 W13 section)
      — S7 synthesis is the next concrete step (master-index clusters → plan →
      subagent wave). RUN S7 IN `.worktrees/sv` (branch `sv-research`) —
      D15/D16/D18/D19 + go-live-readiness.md are binding synthesis
      constraints (ZF/LSI schedules = the canonical D15 consumers). FIRST
      worktree session: bootstrap `sv/HANDOVER.md` per the gt/hn country
      pattern and move per-wave SV state there — root HANDOVER becomes
      integration-level memory only (this avoids repeating the root-HANDOVER
      merge conflicts the GT/HN merge just had to resolve by hand).**
      Then NIIF/chart-of-accounts (32_/33_; consumes 06's
      register interface + C3 NIC anchor + T3's Consejo-criteria OQ); (c) IVA-core
     taxation files still owed (01_ cited in S1; 02_ Reglamento unread; the R/S
     and IVA-retention cross-refs from S3's 01/04 files land there; IVA
     tercerización FCF-exento pointer from S6) — fold into a later taxation wave.
6. **SOQ follow-ups**: taxation — SOQ-02 ($1,600 proration quincenal/semanal; MH
   guidance), 03 OQ-009 (vintage straddle; watch MH guidance), S6 OQs
   (double-benefit 2026 deduction+credit; IVA tercerización → IVA-core wave);
   fiscal-reporting — SOQ-08 (due-day windows), SOQ-13 (F-935 donantes-locales
   CT anchor), SOQ-14 (F-950 frequency); commercial-legal (S5 residue) —
   **SOQ-23 SAS law** (acquire ≥74; statute_pending mechanics in CML/04),
   **SOQ-24 quiebra vintage** (verify modern insolvency law before citing
   beyond terminology), **SOQ-25 Ley Registro de Comercio + Reglamento**
   (CML/01 config-slots empty until acquired), **SOQ-26 Economía rate**
   (dated config; acquire current instrument opportunistically), SOQ-29
   colones flags (ride); **AML watch (new)** — the pending reglamento +
   instructivo under D.L. 426 (EV71 OQ-1; uif.gob.sv/marco-legal watch; when
   issued: re-anchor CML/10 thresholds, revisit OQ-003 law-wins pair and the
   Art. 7 dynamic-inclusion feed); W11/Quincena-25 — F-11 v19/v20 prints
   (≥74; MH formularios page watch — verified unchanged 2026-08-18);
   2026 double-benefit OQ (taxation-side).
7. **Externally-blocked OQs** (check factura.gob.sv + uif.gob.sv/marco-legal
    periodically): Retorno/OpEsp endpoints (MOQ-05 — 52_-schema absence
    verified 2026-08-17; 03 OQ-006, 02 OQ-003); CAT-024 vs Cuadro-2 taxonomy
    confirmation; the pending D.L.-426 reglamento + instructivo (EV71 OQ-1);
    D.O. `/seleccion` + asamblea recovery (still down 2026-08-18). When new
    docs appear: continue source numbering from 74, register with provenance,
    capture supersession.
8. **Remaining S1 OQs** (34 open): most are business decisions (FVS flow,
    email scope) or AT-publication dependencies; 45_ §10 re-read for MOQ-07
    (02 OQ-001/002) can ride along with the payroll or IVA-core wave.
    Addendum follow-ups: 02 OQ-011 (line-level move↔picking design pass —
    product owner's prior implementation as input) before FR-162/163
    implementation; 02 OQ-009 (NRE fate — watch AT/45_ revisions); 06
    OQ-008 (D10 protocol guarantee FR wording, next 06 edit).
9. **Deferred cleanups** (§9 below, batch them).
10. **GT/HN continuation — now branch-merged (2026-08-19):** research phases
    are ON main; continue per `gt/HANDOVER.md` / `hn/HANDOVER.md` inside
    their worktrees (GT: close queue rev 5 → EXTRACTION_PLAN → W1 evidence;
    HN: per its HANDOVER next-actions). SV work moves to
    `.worktrees/sv` (branch `sv-research`). **Roadmap: Colombia, Peru,
    Nicaragua, Costa Rica, Belize, Panama, Dominican Republic follow**
    (ruling 46; bootstrap per the GT/HN pattern when started).

## 9. Deliberately deferred (CAN-STAND list)

- `catalogs/README.md` + `_INDEX.md` still say "PDF overlay"; and
  `build_catalogs.py` keeps a `--pdf` overlay path — contradicts SV-CAT
  FR-002 (workbook = sole parse source). Align at next sidecar regeneration.
  — RESOLVED C1 2026-08-21 (T9: overlay path removed, docs aligned, 33 CSVs
  byte-identical after workbook-only regen).
- T3 wording: 03_events FR-094 5-day anchor — RESOLVED 2026-08-17 (raw 45_
  p.123 quote folded into FR-094 with the anchor-noun ambiguity note);
  UUID "uppercase hexadecimal digits" tightening (M-1) still open.
  — M-1 RESOLVED C1 2026-08-21 (T1: schemas pin `^[A-F0-9]{8}-…-{12}$`;
  §4 rows tightened).
- 06_api-protocol OQ-005 is resolved-but-noisy (used as work-log) — fold
  into next 06 edit. — RESOLVED C1 2026-08-21 (T1: folded to a one-row
  summary).
- 02_transmission AC-011 over-broad ("no *.dtes.mh.gob.sv reference" vs
  legitimate portal URLs) — scope to API code paths. — RESOLVED C1
  2026-08-21 (T1: scoped to API endpoints, portal URLs excluded).
- FR-136 renewal-staging wording fixed (final review), but 04 OQ-006
  (renewal procedure) remains open legitimately. — OQ-006 STAYS OPEN
  (deliberate; verified C1 2026-08-21).
- sv/README count phrasing nit (50 = 48 used numbers + 17/17b pair + 25_
  pdf/xlsx pair). — RESOLVED C1 2026-08-21 (T11: 73 files / 01-75 / next
  76, registry-verified).
- D4 email-escalation channel ownership → ToS/onboarding backlog (not a
  requirements file yet). — STAYS (ToS backlog, out of requirements scope).
- COVERAGE regeneration script (currently hand-built matrix). — RESOLVED
  C1 2026-08-21 (T10: `shared/scripts/build_coverage.py` + COVERAGE_NOTES
  sidecar; `--check` gate green; 13 under-listed citing sources corrected).
- **"Only architecture-split surface" boilerplate** exists in ~11 requirements files
  across waves (S3 final-fix found 01's instance; 02:467 + taxation files untouched) —
  one sweep to soften all instances. — RESOLVED C1 2026-08-21 (T7+T8: 43
  instances softened corpus-wide — taxation 8 + non-taxation 35; canonical
  form = frep/01; corpus grep now empty).
- S3 deferred minors (final review, deferrable): 01 FR-005 missing EVID-178 cite; 01
  FR-023 else-branch phrasing; 01 §4 sign-header wording; 01 Art. 66 attribution
  looseness; 02 FR-064 compressed inventory; 02 §5 FR-048 row missing P-formula pointer;
  03 AC-005 code-8 parity un-OQ'd; 03 FR-071 could name EVID-174; 03 FR-092 glosses 01's
  upload rules; 04/06 Given/then style; 06 FR-162 antecedent + FR-168 FR-106 gloss; 08
  LB-005 gloss restates consumer values (verified correct);   index §7 pointer wording;
    taxation 05-OQ-002 pointer's "F-910/F-915" phrasing (F-910 marginally irrelevant there).
  — RESOLVED C1 2026-08-21 (T2: 13/15 fixed incl. W17 rides FR-213 by-id +
  enum style; Art. 66 attribution + enum style verified already-conformant;
  frep/03 OQ-007 added as the sanctioned code-8-parity OQ).
- S4 deferred minors (final review, deferrable): 06 AC-001 placeholder
  composition "weekend pair + two asuetos" → "two weekend pairs" at next
  touch; T1 ISR-cell 2×SMM restatement + unanchored Art. 174/183/199
  navigational mentions; T2 CSV row-level EVID provenance; T3 FR-029
  two-resolution compression + navigational glosses; T4 FR-051/058 negative
  asymmetry implicit + LB-023 vintage restatement (verified zero-drift vs
  taxation/04); T5 voluntary-ISSS 10.50 regime-dependence (CSV note covers) +
  art99 valid_from caveat + LB-009 gloss-kin; T6 FR-089 kin phrasing + LB-004
  page-pin; T7 LB-018 chamber attribution + FR-107 floor-exclusion inference +
  AC-002 boundary convention; T8 FR-123 min() arithmetic bend (in-mandate per
  P9) + casillas 718-720/738 silence (evidence-faithful); T9 taxation-pointer
  placement.
  — RESOLVED C1 2026-08-21 (T3: 9/11 fixed incl. W17 rides FR-145 wording +
  LB-017 awareness marker; voluntary-ISSS regime-dependence verified
  already-covered; `(navigational)` marker documented nonexistent — anchor
  branch taken).
- S5 deferred minors (final review "can-ride", deferrable): 09:75 id
  SV-CML-FR-162 line-wrapped mid-id (grep-artifact source); 03 page-pointer
  over-broads + §2 abbreviation overlap; 04 Art. 121 final-sentence marker +
  Art. 149 parenthetical skip; 06 EOF blanks; 08 inner-quote normalizations
  ×5 + "626-787" over-bread; 10 FR-209 paren scar; index 07-scope labels;
  marker-vocabulary variance across files; T1-M3 A11 cluster-pointer
  normalization when A11 lands.
  — RESOLVED C1 2026-08-21 (T4: all 9 steps addressed — 6 fully fixed,
  3 partial with documented not-reproducible sub-items; A11 normalized;
  626-787→702-787 source-verified).

## 10. Session-protocol checklist for the next controller

1. Read §1–§8 of this file; read the documents in §2 in order.
2. Confirm state: `git log --oneline -20`, `git status` (expect clean),
   `git worktree list`, `ls sv/requirements/e-invoicing/` and
   `ls sv/requirements/commercial-legal/` (10 files + index). SV synthesis
   work happens in `.worktrees/sv` (branch `sv-research`); this workspace
   is integration-only. For GT/HN: read `gt/HANDOVER.md` / `hn/HANDOVER.md`
   in their worktrees first.
3. Follow skills (brainstorming gate for new design work; SDD for plan
   execution; systematic-debugging for any investigation).
4. Before ANY source citation: check authority order (§3) and COVERAGE.md.
5. At session end: update THIS file (state, rulings, next actions), commit,
   push. Copy any SDD-ledger rulings here BEFORE deleting the workspace.
