# sv/HANDOVER — El Salvador Session State & Continuation Guide

**For the next SV controller session.** Bootstrapped 2026-08-19 (first
worktree session; SV state moved here from the root HANDOVER per its §8.5b
directive — the root file is now integration-level memory only). Read this
fully before acting; it is the authoritative SV cross-session memory
(conversation context does not survive). **Update it at every session
boundary.**

**Bootstrap prompt for a fresh session:** `Read sv/HANDOVER.md and continue.`

---

## 1. Where you are

- **Worktree:** `.worktrees/sv`, branch `sv-research` (created 2026-08-19;
  all SV extraction/synthesis waves run there from now on). The main
  workspace is integration-only. Merge `sv-research` → `main` at milestones
  by owner decision (rebase-then-merge; never force-push; remote refs fixed
  via delete + re-push after rebase).
- **Mission:** SV requirements extraction for the Odoo localization per
  `shared/docs/requirements-extraction-procedure.md`; synthesis waves
  produce Takumi-contract requirements files in `sv/requirements/<topic>/`.
  Product architecture context: root `HANDOVER.md` §1 + `shared/docs/`
  (D1–D19 shared canon — binding on all waves).
- **Corpus status:** evidence phase COMPLETE through W14; synthesis
  delivered S1 (e-invoicing) + S2 (ISR) + S3 (fiscal reporting) + S4
  (payroll) + S5 (commercial-legal) + S6 (Quincena-25 fold-in) + S7
  (special-regimes, 2026-08-19). **W14 (2026-08-19, this session):
  NIIF/chart-of-accounts evidence pass COMPLETE** — 32_ (NIIF PYMES 3rd
  ed.) + 33_ (EY guide) read end-to-end, EVID-275..303, clusters N1-N8 +
  R29 + SOQ-46..53 in the master index (commits 421103b + 9f4effe).
  **NEXT WAVE: S8 chart-of-accounts synthesis — plan READY at
  `docs/superpowers/plans/2026-08-19-s8-chart-of-accounts-synthesis.md`
  (9 tasks, prefix SV-COA, tasks strictly sequential); execute the
  subagent loop in this worktree from the plan.** Then IVA-core taxation
  (01_/02_).

## 2. Read order for a new session

1. THIS file
2. `sv/EXTRACTION_PLAN.md` — wave log (W1–W13), reading order, risks
3. `sv/.extractions/00_MASTER_INDEX.md` — synthesis lookup: clusters
   (A1-A12, T1-T8, F1-F12, P1-P10, C1-C10, SR1-SR9), rulings R1–R28,
   MOQ/SOQ registers
4. `sv/requirements/COVERAGE.md` + the five topic `00_index.md` files
   (e-invoicing, taxation, fiscal-reporting, payroll, commercial-legal)
   + `sv/requirements/special-regimes/00_index.md` (wave-prep stub)
5. Root `HANDOVER.md` §5 (decisions D1–D19 + standing policies) +
   `shared/docs/` method docs (extraction procedure, requirements
   template, regulatory-change-management, odoo-localization-guide,
   go-live-readiness)
6. `sv/sources/README.md` — the registry (72 files, numbering 01–74,
   gaps 21/23/24/28; next numbering = 75)

## 3. Corpus & evidence state

- **EVID corpus 001..274** (gaps 109-127, 240 reserved-unused). W13 files
  (2026-08-19): `12_Ley_Zonas_Francas` (EVID-251..258),
  `14_17b_Servicios_Internacionales` (EVID-259..267),
  `13_42_43_74_Aduanas` (EVID-268..273), `31_Guia_FOVIAL_COTRANS`
  (EVID-274). W12: `71-73_AML_DL426_Instructivo380_CCverify` (EVID-241..250).
  W11: `66-70_Quincena25` (EVID-236..239). W10: `07_Codigo_Comercio`
  (EVID-211..227), `15_Ley_Lavado_Activos` (EVID-228..231, historical),
  `17_Reglamento_Lavado_Activos` (EVID-232..235, kept-mechanics citable).
  W9 payroll: EVID-191..210. W8 fiscal reporting: EVID-171..190. W7/W6.5/
  W6 ISR: EVID-088..108, 128..170. S1 foundations: EVID-001..087.
- **72 registered source files** (numbering 01–74, gaps 21/23/24/28).
  Registry carries title-vs-content amendments (29_ = F985 CNR mislabel;
  09_ = D.L. 614 misnomer; 15_ = D. 498 mislabel; 12_ = "Industriales y de
  Comercialización" content title fixed W13), supersession notes
  (10_ historical, 03_ historical, 65_ superseded-by-v19/v20, 15_/17_ AML
  historical/kept), and provenance markers (66_-70_ transparenciafiscal;
  71_-74_ uif.gob.sv).
- **Authority orders (binding):** DTE stack 44_/45_/46_/50_/51_/52_ (2026)
  > 18_/19_/22_ (2025) > 40_/41_/25_ (2022). ISR: 54_ + reform decrees
  55_/56_/57_/58_ > 03_; tables 53_ (+ 60_ gazette pin) > 10_. Payroll:
  09_ (D.L. 614) > SAP lore; ISSS 08_ + caps as F-14 dated data; SMM 16_.
  Commercial-legal: AML 71_ (D.L. 426, effective 2025-10-17) with kept
  72_/17_ (R28 chain); CC 07_ (verified vs 73_). Special-regimes: W13 set
  12_/13_/14_/17b_/42_/43_/74_/31_ (all consolidations end 2012-2013 —
  SOQ-30 verification watch).

## 4. Requirements corpus (delivered)

| Topic dir | Files | FRs | Prefix |
|---|---|---|---|
| `e-invoicing/` | 6 + index | 222 (incl. §3.11 FR-159..164) | SV-EINV-FR-001..164, SV-PROT-FR-001..040, SV-CAT-FR-001..018 |
| `taxation/` | 6 + index + 2 CSV | 175 | SV-TAX-FR-001..175 |
| `fiscal-reporting/` | 8 + index + CSV | 212 | SV-FREP-FR-001..212 |
| `payroll/` | 8 + index + 2 CSV | 143 | SV-PAY-FR-001..143 |
| `commercial-legal/` | 10 + index | 224 | SV-CML-FR-001..224 |
| `special-regimes/` | 8 + index | 175 | SV-SPE-FR-001..175 |

Totals: 1151 FRs (S7 = 175 FRs / 130 LBs / 80 ACs / 42 OQs). CSVs:
`withholding_tables.csv` + `isr_brackets.csv` (taxation),
`f14_income_codes.csv` (fiscal-reporting), `smm_2025.csv` +
`ss_contributions.csv` (payroll). FR numbering is wave-sequential within a
prefix; new topics take new prefixes per the `<CC>-<TOPIC>-FR-nnn`
contract (S8+ continues from a new topic prefix).

COVERAGE rollup after S7: 60 cited / 3 pending / 9 N/A / 1 superseded
(73 rows — 74_ was added as a row by S7; it had never been listed). The 3
pending = 02_ (IVA-core wave) + 32_/33_ (NIIF wave).

## 5. SV facts a new session must know (condensed; details in wave sections below)

- **Never-implement invariants:** pago mínimo (sent. 18-2012 family, R21);
  CT Art. 311 maternity tenure gate (sent. 105-2014); HN-kin dead-print
  guard for F-11/F-14 pago-mínimo casillas; 71_ Art. 24's 24h over 72_
  Art. 43's 5 días (law-wins, OQ-tracked); SAP-era pension rate lore.
- **D15 as-of doctrine (binding on all waves; §5 ruling 42 in root):**
  dated legal parameters = immutable dated rows resolved as-of the domain
  anchor date, snapshotted on the record; corrections use ORIGINAL-period
  parameters; no retro-transmission; history = read-only external records;
  payroll corrections hybrid by window. ZF/LSI/DPA exemption schedules are
  the canonical D15 consumers (per-acuerdo rows, never global constants).
- **D16/D18/D19 + go-live-readiness.md** bind every synthesis wave (dated
  mechanics canon; `is_historical` ingestion; posting tiers + verbatim
  rounding + `is_sequence_init` + TB routing).
- **D13/D14 (= D17 cross-country default):** `l10n_latam_invoice_document`
  — ONE journal, MANY document types; warehouses → establecimientos;
  caja/punto de venta first-class in numeroControl + codPuntoVentaMH.
- **Value-discipline:** caps/SMM-derived/threshold values enter as dated
  data with instrument provenance, never arithmetic-derived ([sic]
  fidelity for printed digits — D.E. 10-2025 precedent); config-gaps ship
  NO defaults with OQs (Economía rate, commission rates, SMM-mayor-cuantía
  sector).
- **Quote fidelity:** silent truncation of statutory catalogs = defect;
  verbatim sweeps against extraction txt are the norm; brief-vs-evidence
  conflicts resolve FOR the evidence.
- **Cross-file discipline:** consume sibling files BY FR ID (never
  restate): días-hábiles engine SV-FREP-FR-202..204; SMM feeds
  payroll/02; retention values taxation/04 + F-07 annexes 9-12; earnings
  register `l10n_sv.isr.earnings.register`; Quincena-25 credit ledger
  `l10n_sv.isr.quincena.credit` (SV-TAX-FR-174 = the S7 certificado
  consumer interface).

### Wave log summary (full detail in `sv/EXTRACTION_PLAN.md` §Extraction log)

- **W14 (2026-08-19, this session):** NIIF evidence pass — 32_ = Norma de
  Contabilidad NIIF para las PYMES **3ra edición (feb-2025; effective
  2027-01-01, early adoption permitted; Apéndice A Tabla A1 = the D12
  vintage artifact)** read in full (EVID-275..298); 33_ = EY full-NIIF
  guide (EVID-299..303) ruled SECONDARY-ONLY (R29(a) — version/horizon
  facts + contrast set, never sole LB). Master index: clusters N1-N8, R29
  (b: 32_ Prólogo P12 delegates applicability to jurisdictions — the SV
  adopting instrument is ABSENT = SOQ-46, the wave's gating acquisition;
  c: CC 443-444 "NIC"-covers-PYMES working reading), SOQ-46..53. Hard
  encodings for S8: ESF (a)-(r) + deferred tax ALWAYS non-current; LIFO
  banned; PPE revaluation per class; ALL internally generated intangibles
  incl. R&D expensed; leases dual financiero/operativo (NOT IFRS-16);
  borrowing costs all expensed; revenue = IFRS-15 five-step; no-NOL
  deferred-tax constraint (SOQ-50); dividend-WHT-to-equity (29.33);
  Pillar Two config-off; FX prepaid-rate 30.8A; Sec 35 deemed-cost = D18/
  D19 kin; NIIF 18/19 (2027) = full-NIIF-only watches; S1/S2 out of scope.

- **W1-W5.5 (2026-08-16/17):** foundations + catalogs sidecars + Ley/Regl
  IVA + CT + DTE stack + 2026 regulatory re-read; schemas 52_; DTE
  authority re-versioned (catalogs v1.1, Normativa v2.0, 4 events).
- **S1 (2026-08-17):** e-invoicing synthesis 222 FRs; schema pass closed
  10 OQs + 4 MOQs; §3.11 fiscal immutability addendum (FR-159..164).
- **W6/W6.5/W7 (2026-08-17):** ISR evidence + acquisitions 53_-58_;
  reform chain closed; pago mínimo void; tables operative NET base.
- **S2 (2026-08-18):** taxation 172 FRs + 2 CSVs; R17-R22; SOQ-01/03/04
  resolved; brackets two vintages.
- **W8 (2026-08-18):** F-07/F-14 evidence + 59_-64_ acquisitions; 29_
  mislabel found; DTE-identifier mapping canonical (FR-042/043).
- **S3 (2026-08-18):** fiscal-reporting 208 FRs; anulados code "D" closes
  02 OQ-008 F-07 side; casilla honesty rules (ruling 27).
- **W9 (2026-08-18):** payroll evidence; SMM Decreto 11-2025; D.L. 614
  identity find (16% = 7.25/8.75); CT payroll books; F-11 v18 acquired.
- **S4 (2026-08-18):** payroll 137 FRs + 2 CSVs; caps as dated data
  (SOQ-15/16/17); Art. 311 VOID invariant; R23/R24.
- **W10 (2026-08-18):** commercial-legal evidence (CC 07_ + AML 15_/17_);
  Art. 439 no-alteration kin to §3.11; prescription matrix Art. 995.
- **W11 (2026-08-18):** Quincena-25 package 66_-70_ (D.O. down;
  transparenciafiscal route); P10 unblocked; SOQ-09 resolved.
- **S6 (2026-08-18):** Quincena-25 fold-in — payroll 138..143, taxation
  173..175, fiscal-reporting 209..212; R27 in-file rulings.
- **W12 (2026-08-18):** AML regime replacement 71_/72_/73_ (uif.gob.sv
  route find); R28 threshold authority chain; 15_ historical.
- **S5 (2026-08-18):** commercial-legal 224 FRs; retention matrix §3.7
  (SOQ-28); CC↔CAT-031 auto-translation BANNED; SAS statute-pending.
- **W13 (2026-08-19):** special-regimes evidence EVID-251..274 + 74_
  acquisition; D15 decided; S7 unblocked.
- **S7 (2026-08-19, first worktree wave):** special-regimes synthesis
  COMPLETE per plan `docs/superpowers/plans/2026-08-19-s7-special-regimes-synthesis.md`
  — subagent-driven, 9 tasks (8 Approved clean + T1 one fix round + T9
  reviewer re-dispatch after a silent death; commits 2f33019..10a7cc0;
  final whole-wave review MERGE-READY, zero Critical/Important, all
  deferred minors triaged ride). Files: 01 regime-framework (SR1,
  FR-001..022) · 02 zf-exemption-schedules (SR2, 023..041) · 03
  lsi-regime (SR3, 042..063) · 04 customs-clocks (SR4, 064..081) · 05
  tan-iva-interface (SR5, 082..102) · 06 customs-declarations (SR6,
  103..129) · 07 obligations-reporting-sanctions (SR7, 130..165) · 08
  fovial-cotrans (SR8, 166..175). Key encodings: D15 per-beneficiary
  ladders (usuario 15/20y→60→40; DPA 10/15y; desarrollista flat;
  **administrador via 54-C ONLY — Arts. 14+15 derogated by D.L. 318-2013
  as printed, wave finding**); LSI indefinite-until-cessation rows +
  17b_ Art. 22 caps 50/40/30 (VENTAS basis, dictamen 58.e.9.iii); 12m-ZF
  vs 24m-LSI clock invariant (regime_family exclusivity); ZF 0%+76/77 vs
  LSI 75-77 route split; DUCA 62-field model (**field 14 = vencimiento
  per the 43_ print — master-index "33/56" was a prep error, fixed by
  wave-findings note**); $18 tasa + presumed flete/seguro 1.25/1.50/10%
  dated rows; SMM-mayor-cuantía = highest 16_ sector config default
  (SOQ-33; industria/comercio-y-servicios tie noted); FOVIAL $0.20/gal
  per-unit tax + IVA-exclusion guard (provenance chain via 31_ guide,
  law absent SOQ-39). SOQ-30..45 all carried as in-file OQs (42 open).

### S7-process rulings (2026-08-19, preserved from the SDD ledger before workspace deletion)

- **(a)** T1's implementer died pre-report — controller verified
  structure (contiguity, sections, mapping counts) and committed its
  file UNMODIFIED, review gate preserved (S5 ruling-41 precedent).
- **(b)** Extraction txts are git-ignored in this worktree —
  implementers/reviewers read them from the main checkout read-only
  (controller exception; §2 citations stay repo-relative).
- **(c)** One T9 reviewer dispatch died silently with no output —
  re-dispatched clean (read-only role, no state impact).
- **(d)** Harness exposes no per-subagent model parameter — dispatches
  inherit the session model (same as S1-S6).
- **(e)** Wave findings recorded upstream AND in-file: administrador
  Arts. 14+15 derogated as printed (54-C only; file 02 OQ-4); DUCA
  field-14 anchor (43_ print; master-index findings note).

## 6. Gotchas & verified lessons (SV-specific)

- Catalog versions NOT monotonic; CAT-013 re-assigned to 44-municipio
  model → dated catalog rows (SV-CAT-FR-007..010). CAT-008 = 263 rows.
- FE receptor threshold ≥3 SMM (D.L. 487) — old $200 superseded.
- Invalidación deadlines differentiated per type (1d/10háb/4d/3mo/2y-codes)
  — e-invoicing 03 FR-103 + DG45 §3.2.
- NCE contingency-eligible; CLE/DCLE/CDE excluded. Two new 2026 events
  (Retorno 18, OpEsp 17); FVS alive as physical regime via EOP.
- D.O. scans: PSM 6; D.O. TABLE pages PSM 4 at 400dpi. OCR quirk critical.
- factura.gob.sv wpdmdl IDs shuffled — verify page 1 with pypdf.
- D.O. `/seleccion/{Id}` route: **500 server-wide since 2026-08-18
  ~13:55** (API listing works). asamblea.gob.sv unreachable (000).
  Live official mirror: **uif.gob.sv Marco Legal** (plain GET + browser
  UA; Incapsula blocks HEAD). MH formularios page: direct wp-content
  URLs (verified 2026-08-18: no F-11 v19/v20, no F14 v17 manual).
- Title-vs-content incidents ×5 (29_, 09_, 15_, 12_, 31_-COTRANS) —
  trust content, amend registry, never trust catalog titles.
- Damaged-PDF recipes: qpdf auto-repair (17_, 74_); ghostscript pdfwrite
  rebuild for broken page trees (73_).
- Python venv `~/.venvs/localizations`; scripts
  `shared/scripts/extract_text.py` + `build_catalogs.py`.

## 7. Open-question highlights (full registers in master index + topic indexes)

- **MOQ-05** Retorno/OpEsp endpoints (externally blocked, schema-verified
  absent); **MOQ-04** FOVIAL/COTRANS instruments (FOVIAL half now anchored
  by 31_/D.L. 208 Art. 26; COTRANS + law texts still absent — SOQ-39).
- Taxation: SOQ-02 ($1,600 proration), 03-OQ-009 straddle, Quincena-25
  double-benefit 2026, IVA tercerización pointer (IVA-core wave).
- Fiscal-reporting: SOQ-08 (due-day windows), SOQ-13/14; 07 OQ-008 (v17
  apéndice code 73), 06 OQ-008 (MH validation depth).
- Commercial-legal: SOQ-23 SAS law, SOQ-24 quiebra vintage, SOQ-25 Ley
  Registro de Comercio, SOQ-26 Economía rate; AML new-reglamento watch
  (uif.gob.sv).
- F-11 v19/v20 + F14 v17 manual acquisitions (≥75 numbering; MH page
  watch). D.L. 598-2020 + EVID-167 tail laws (S7 SOQ-41).
- IVA-core taxation files still owed (01_/02_ full synthesis; R/S and
  IVA-retention cross-refs land there; FOVIAL chain design pass SOQ-40).

## 8. Next actions (ordered)

1. **NEXT WAVE: S8 chart-of-accounts synthesis** — plan READY
   (`docs/superpowers/plans/2026-08-19-s8-chart-of-accounts-synthesis.md`;
   9 tasks, prefix SV-COA, T1-T8 strictly sequential, T9 index/close).
   Execute the subagent loop in this worktree per the plan's protocol.
   LB = 32_ (cite section/párrafo); 33_ secondary-only (R29(a));
   SOQ-46 instrument gap rides every §2 preamble; accounting-vs-fiscal
   two-track invariant = the wave's spine (fiscal values consumed BY ID,
   bridges via Sec 29 deferred tax).
2. Then **IVA-core taxation wave** (01_/02_ full synthesis; folds the
   R/S and IVA-retention cross-refs from S3's 01/04 files, SOQ-40 FOVIAL
   chain design pass, LSI-tercerización FCF pointer from S6).
3. **Acquisition follow-ups (SOQ rides):** S8 — **SV NIIF-adopting
   instrument (Consejo de Vigilancia criteria per CC Arts. 443-444 or
   successor; SOQ-46 — the gating gap) + optional 2nd-edition NIIF
   PYMES text (SOQ-48)**; S7 — Reglamento General ZF (SOQ-31), LESIA
   (SOQ-32), DUCA user manual (SOQ-36), FOVIAL law D.L. 208-2000 +
   COTRANS instrument (SOQ-39), D.L. 598-2020 + EVID-167 tail laws
   (SOQ-41), current consolidations for 12_/13_/14_/17b_/74_ (SOQ-30),
   $18-tasa adjusting acuerdos (SOQ-34).
4. Registry note: numbering continues from **75** (32_/33_ were already
   registered; the S8 acquisition candidates above are the NEW numbering).
5. SOQ follow-ups per §7; periodic external checks (factura.gob.sv,
   uif.gob.sv/marco-legal, MH formularios, D.O. recovery).
6. Deferred cleanups (CAN-STAND): prior-wave deferred-minor lists (root
   HANDOVER §9 + per-task reviews; S7's triaged-ride list is in the
   final review record — AC-007 $1,100 Given-gap is the first-pick),
   boilerplate sweep (~11 files), COVERAGE regeneration script.
7. At wave closes: update THIS file + master index + COVERAGE + topic
   indexes; commit + push sv-research; record rulings here BEFORE
   deleting any SDD workspace. Owner decides sv-research → main merges
   at milestones (rebase-then-merge; never force-push).

## 9. Conventions

- Evidence: verbatim Spanish + gloss + loc + candidate-CR + topics +
  doubts→OQs; per-file OQ numbering; corpus-global EVID.
- `.gitignore`: `sv/.extractions/*` except `*.evidence.md` +
  `00_MASTER_INDEX.md`. `sv/sources/**` deliberately NOT under the
  byte-fidelity gitattributes rule (predates it; would need a migration
  pass — never "fix" casually).
- Commits: short imperative, no emojis; push after each wave.
- Registry additions continue numbering from 75; page-1 verify
  everything; record provenance + supersession.
- Synthesis waves: prep (master-index clusters + SOQs) → plan doc in
  `docs/superpowers/plans/` → subagent loop (fresh implementer per task;
  every FR cites LB; reviewer verifies vs master index; fix rounds;
  ledger) → final whole-wave review → ONE fix wave → push.
