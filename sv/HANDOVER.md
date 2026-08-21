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
- **Corpus status:** evidence phase COMPLETE through W15; synthesis
  delivered S1 (e-invoicing) + S2 (ISR) + S3 (fiscal reporting) + S4
  (payroll) + S5 (commercial-legal) + S6 (Quincena-25 fold-in) + S7
  (special-regimes, 2026-08-19) + S8 (chart-of-accounts, 2026-08-20 —
  MERGED to main at aec9e5d via rebase-then-merge; pre-rebase SHAs
  d25ecd7..0eabbca superseded by eea1e5a..0ca6d29+) + **S9 (IVA-core,
  2026-08-20 — MERGED to main at 09847d0 via rebase-then-merge
  (fourteenth §4.6 run, zero conflicts; pre-rebase SHAs
  a021fc8..7147c5b superseded by b6fe41a..09847d0): taxation files 07-15
  + index/flips, 178 FRs SV-TAX-FR-176..353; final whole-wave review
  USABLE-WITH-FIXES → one fix wave PASS)**.
  W15 (2026-08-20): IVA deep pass EVID-304..338, clusters V1-V10 + R30
  + SOQ-54..58 in the master index. **W16 (2026-08-20): external-check
  sweep + 75_ (D.E. 117-2001 CT reglamento — the R17/R30(a) repeal
  authority) acquired/evidenced EVID-339..358; R30(a) survivor-set
  addendum; SOQ-54 Ley side RESOLVED; D.O. RECOVERED — see §5 wave log.**
  **W17 (2026-08-20): 75_ fold-in COMPLETE — taxation/16 new
  (SV-TAX-FR-354..396) + 01/04/13 edits (397..404; OQ-001 resolved),
  fiscal-reporting 213..214 + 06/07/08 notes, payroll 144..147 + 04 note
  — see §5 wave log.** COVERAGE after W17: 64 cited / 0 pending / 9 N/A /
  1 superseded (74 rows — zero pending again).
  The 8-topic synthesis program + W17 fold-in are COMPLETE (1,662 FRs
  total). Remaining
  program: acquisition follow-ups (§8.2), SOQ/external watches, deferred
  cleanups (§8.5), owner merge decisions.**

## 2. Read order for a new session

1. THIS file
2. `sv/EXTRACTION_PLAN.md` — wave log (W1–W17), reading order, risks
3. `sv/.extractions/00_MASTER_INDEX.md` — synthesis lookup: clusters
   (A1-A12, T1-T8, F1-F12, P1-P10, C1-C10, SR1-SR8, N1-N8, V1-V10),
   rulings R1–R30, MOQ/SOQ registers
4. `sv/requirements/COVERAGE.md` + the topic `00_index.md` files
   (e-invoicing, taxation, fiscal-reporting, payroll, commercial-legal,
   special-regimes, chart-of-accounts)
5. Root `HANDOVER.md` §5 (decisions D1–D19 + standing policies) +
   `shared/docs/` method docs (extraction procedure, requirements
   template, regulatory-change-management, odoo-localization-guide,
   go-live-readiness)
6. `sv/sources/README.md` — the registry (73 files, numbering 01–75,
    gaps 21/23/24/28; next numbering = 76)

## 3. Corpus & evidence state

- **EVID corpus 001..358** (gaps 109-127, 240 reserved-unused; W15 IVA deep
  pass EVID-304..338 in EV01's W15 section; W16 CT-reglamento EVID-339..358
  in EV75). W13 files
  (2026-08-19): `12_Ley_Zonas_Francas` (EVID-251..258),
  `14_17b_Servicios_Internacionales` (EVID-259..267),
  `13_42_43_74_Aduanas` (EVID-268..273), `31_Guia_FOVIAL_COTRANS`
  (EVID-274). W12: `71-73_AML_DL426_Instructivo380_CCverify` (EVID-241..250).
  W11: `66-70_Quincena25` (EVID-236..239). W10: `07_Codigo_Comercio`
  (EVID-211..227), `15_Ley_Lavado_Activos` (EVID-228..231, historical),
  `17_Reglamento_Lavado_Activos` (EVID-232..235, kept-mechanics citable).
  W9 payroll: EVID-191..210. W8 fiscal reporting: EVID-171..190. W7/W6.5/
  W6 ISR: EVID-088..108, 128..170. S1 foundations: EVID-001..087.
- **73 registered source files** (numbering 01–75, gaps 21/23/24/28; W16
  added 75_ = Reglamento de Aplicación del CT, D.E. 117-2001 — the R17/
  R30(a) mass-repeal authority instrument, EVID-339..358).
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
| `taxation/` | 16 + index + 2 CSV | 404 (S2: 001..175 ISR; S9: 176..353 IVA; W17: 354..404 CT procedures) | SV-TAX-FR-001..404 |
| `fiscal-reporting/` | 8 + index + CSV | 214 | SV-FREP-FR-001..214 |
| `payroll/` | 8 + index + 2 CSV | 147 | SV-PAY-FR-001..147 |
| `commercial-legal/` | 10 + index | 224 | SV-CML-FR-001..224 |
| `special-regimes/` | 8 + index | 175 | SV-SPE-FR-001..175 |
| `chart-of-accounts/` | 8 + index | 276 | SV-COA-FR-001..276 |

Totals: 1662 FRs (W17 fold-in = 57 new: taxation 354..404, fiscal-
reporting 213..214, payroll 144..147; taxation dir now 404 FRs / 295 LBs /
274 ACs / 87 OQs). CSVs:
`withholding_tables.csv` + `isr_brackets.csv` (taxation),
`f14_income_codes.csv` (fiscal-reporting), `smm_2025.csv` +
`ss_contributions.csv` (payroll). FR numbering is wave-sequential within a
prefix; **R30(b): one prefix per topic dir — the IVA-core files continued
`SV-TAX` at 176 rather than taking a new prefix**; genuinely new topics
take new prefixes per the `<CC>-<TOPIC>-FR-nnn` contract.

COVERAGE rollup after W17: 64 cited / 0 pending / 9 N/A / 1 superseded
(74 rows). S8 lesson (standing): registry flips
must grep ALL LB source columns of the new files.

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

- **W17 (2026-08-20):** 75_ reglamento-CT fold-in COMPLETE per plan
  `docs/superpowers/plans/2026-08-20-w17-75-reglamento-foldin.md` —
  subagent-driven, 5 tasks strictly sequential (per-task reviews all
  Approved clean, 0 Critical/Important; commits 562a3e3..03b05b9 + T5
  flips). Files: **taxation/16 ct-procedures NEW** (SV-TAX-FR-354..396:
  clocks vocabulary, representation/domicilio, registration, the
  Art. 31-35 declaration-state model + CT 103 amendment gate,
  payments/extinction, compensación, **the Art. 23/133 retention
  imprescriptibilidad/caducidad pair**, refunds, sanctions, books,
  fiscalización, print-era historical blocks per EV75 OQ-3/OQ-4 bars);
  04 **FR-397..400** + 13 **FR-401..404** (retention-agent layers,
  ISR/IVA tracks separate); 01 LB-027/036 — **OQ-001 RESOLVED**
  (75_ Arts. 99-100 corroborate Ley Art. 62 + monthly consolidation of
  sub-monthly cycles); frep 01 **FR-213/214** (declaration-state gate +
  delegated-reception contract) + 06/07/08 notes — **SOQ-08 anchor
  CONSUMED (Art. 100)**, by-NIT-digit windows still open; payroll 08
  **FR-144..147** + 04 LB-029 note. Registry corrective fold: 02_
  survivors = 1-10, 16-26, 29-30, 50-51 (+52 vigencia spent); 27-28 →
  147(b); 36/45 died via D.E. 60-1993 (1) — EVID-358/OQ-6, supersedes
  the "36/45 survive" gloss. Corpus 1,662 FRs (TAX 404 / FREP 214 / PAY
  147); COVERAGE 64/0/9/1. Process rulings: (a) T2's two beyond-brief
  edits upheld (FR-121 LB-anchor + 01 §5 stale-note refresh); (b) plan
  §3.6-pointer defect — payroll/04 note placed §3.3, reviewer-verified;
  (c) push deferred to post-final-review (S9 protocol). **Final whole-wave
  review: USABLE-WITH-FIXES → one fix wave PASS (c06ee79: LB-028 "de que
  se trata" restore, §2 R30(a) staleness reword, FR-372 by-pointer) =
  MERGE-READY**; deferred-minor triage: 3 RIDE (frep/01 enum style, FR-213
  dual-branch quote, FR-145 wording, LB-017 no-consumer row, HANDOVER
  rewrap) + parked residual (FR-372 trailing anchor map still reads "TAX
  13/15-files by id" — 13-file ids exist, 15 is pointer-only; fold at
  next 16 edit). Commits 562a3e3..c06ee79; pushed sv-research.**

- **W16 (2026-08-20):** external-check sweep + 75_ acquisition + SOQ-54
  Ley-side verification — **D.O. RECOVERED** (serves PDFs; API param shape
  unpinned — pin before the SOQ-41/34 hunts); asamblea still 000; MH
  formularios unchanged; factura.gob.sv no LB drift; no new AML reglamento.
  **75_ = Reglamento de Aplicación del CT (D.E. 117-2001**, D.O. 234 T.353
  11-dic-2001, effective 19-dic-2001; TF DC5854) — the R17/R30(a) repeal
  authority instrument finally owned; EVID-339..358 (EV75, 8 OQs). **R30(a)
  corrected by instrument audit: 02_ live survivors = 1-10, 16-26, 29-30,
  50-51** (old "16-30" over-included 27-28; 36/45 died via D.E. 60-1993,
  NOT 147(b)); all V1-V10 cites verified in-set; taxation 07/08/09/10/14
  preambles fixed. 147(a)→04_ survivors corroborate EV04 (04_ header
  "6-20" loose — Art. 8 repealed). Leads: 75_ Art. 100 = SOQ-08 anchor
  (EVID-351 payroll retention engine + F-14 annex root); imprescriptible
  retentions Art. 23 vs 2-y agent caducidad Art. 133; dictamen block
  historical (OQ-3). SOQ-54 Ley side RESOLVED (TF DC9226 ≡ 01_ through
  (14) D.L. 71-2015); Rgto side rides. **Pending: 75_ FR fold-ins at the
  next taxation/fiscal-reporting/payroll edit wave** (COVERAGE 74 rows,
  1 pending).

- **S9 (2026-08-20):** IVA-core synthesis COMPLETE per plan
  `docs/superpowers/plans/2026-08-20-s9-iva-core-synthesis.md` — W15 deep
  pass (EVID-304..338) first, then subagent-driven 10 tasks strictly
  sequential (per-task reviews: 8 Approved clean; T1 two fix rounds —
  quote fidelity + EVID-319 cite; T3 one fix round — two one-token
  restores; T6 implementer died pre-report, S8 ruling (b) applied) +
  final whole-wave review (USABLE-WITH-FIXES → one fix wave PASS =
  MERGE-READY: seven-field medicines registry, LB-table 6-column shape
  in 09/10/11/14, FR-216 [DESIGN] label, EVID-306 "se emite" evidence
  hygiene). Commits 0e20a28..04e6bfa. Files: 07 iva-framework (V1,
  176..205) · 08 iva-exemptions (V2, 206..224) · 09 iva-base-rate (V3,
  225..245) · 10 iva-credit-deductibility (V4, 246..268) ·
  11 iva-pro-rata-remanente (V5, 269..283) · 12 iva-adjustments-assets
  (V6+V7, 284..302) · 13 iva-retentions (V8, 303..319) ·
  14 iva-exports-refunds (V9, 320..337) · 15 iva-declaration-interfaces
  (V10, 338..353). Key encodings: R30 rulings (a) Rgto. survivors-only
  w/ stale-anchor notes; (b) SV-TAX-176+ continuation; (c) 67_'s
  tercerización "Art. 66 inciso sexto" maps to the CURRENT SIXTH inciso
  (prep gloss said fifth — corrected; FCF-exento no-pro-rata working
  reading OQ-tracked in 11); FOVIAL SOQ-40 design pass (09 §3.7
  [DESIGN] rows: 2001 chain → DTE D1-tributo mapping); CT retention
  matrix verbatim (13; floor prints "CIEN DÓLARES" — no colones issue);
  MOQ-03 closed as SOQ-55 (colones [sic] + config-gap); MOQ-04
  base-guard half closed (09 FR-242); fold-ins wired: taxation/02
  OQ-009 → resolved-by-pointer, frep/03 OQ-004 → ANSWERED (FR-313),
  frep/02 OQ-002 rate-anchor note (FR-240/241). RIDE list in the S9 SDD
  ledger copy (cosmetics; nothing load-bearing).

- **S8 (2026-08-20):** chart-of-accounts synthesis
  COMPLETE per plan `docs/superpowers/plans/2026-08-19-s8-chart-of-accounts-synthesis.md`
  — subagent-driven, 9 tasks strictly sequential (8 Approved clean + 2
  fix rounds: T3 CT-Art-62 by-id, T8 R29 co-cite) + final whole-wave
  review (MERGE-READY after one fix wave: COVERAGE 01_/54_ rows,
  sv_coa_ppe_class re-point, FR-163 pinned SV-PAY-FR-105..107, index
  bridge note). Commits d25ecd7..0eabbca; pushed sv-research. Files:
  01 framework-policies (N1, 001..021) · 02 coa-structure (N2,
  022..054) · 03 financial-instruments-fx (N3, 055..092) ·
  04 nonfinancial-assets (N4, 093..134) · 05 liabilities-equity-benefits
  (N5, 135..181) · 06 revenue (N6, 182..223) · 07 groups-related-parties
  (N7, 224..252) · 08 deferred-tax-adoption (N8, 253..276 — closes the
  wave; every 01-07 difference-route lands in FR-253..269). Key
  encodings: R29 authority (33_ never sole LB — 5 secondary rows in
  01/03/05/07/08, always co-cited); SOQ-46 note in every §2; two-clock
  CT Art. 62 = SV-TAX-FR-020 by id; SOQ-50 no-NOL constraint (only the
  capital-loss 5y ledger may ground loss-DTAs, 29.21-gated); Pillar Two
  + hyperinflation config-off; dividend-WHT-to-equity 29.33 ↔
  taxation/05; 32.11 dual encoding (05/FR-175 declaration half vs
  07/FR-251 reporting-date half — deliberate, index-noted). Wave
  findings: Sec 27 body actually at txt PAGE 239-248 (page-map hint was
  stale); e-invoicing §3.11 FRs live in 02_transmission.md. RIDE
  backlog from final review triage (glosses, locators, N1-N8 tags in
  index) — see SDD ledger copy in EXTRACTION_PLAN if needed; primary
  rides: T1 glosses ×2, T4 locator nits ×3, T6 AC-001 self-containment,
  T8 A1 sentence-final period.

- **W14 (2026-08-19):** NIIF evidence pass — 32_ = Norma de
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

### S8-process rulings (2026-08-20, preserved from the SDD ledger before workspace deletion)

- **(a)** Extraction txts exist WORKTREE-LOCAL since W14 (S7 ruling (b)
  superseded for S8+): implementers/reviewers read
  `sv/.extractions/*.pdf.txt` in the worktree; no cross-checkout reads.
- **(b)** T2's implementer died silently leaving a COMPLETE file —
  controller verified structure (33 FRs contiguous 022..054, 7 sections,
  layer rows, OQ table) and committed UNMODIFIED per S7 ruling (a);
  review gate preserved (S5 ruling-41 precedent).
- **(c)** T3 died twice with ZERO state — cause was dispatch context
  overload (2 exemplars ~140KB + full evidence). Fix: SCOPED dispatches
  (evidence read as line-ranges for the task's EVIDs; ONE exemplar;
  on-demand txt with grep+bounded-window). No further deaths in T3..T9.
  **This is the dispatch template for S9+.**
- **(d)** Thin-evidence citation form: where a 32_ evidence block lacks
  a specific párrafo, FRs cite `32_ + section/párrafo + txt PAGE
  anchor` + nearest governing EVID id (plan's evidence-inputs note, S3
  ruling 25 kin). Applied to Sec 16/27 (T4), 14/15 (T7), etc.
- **(e)** Final-review lesson recorded as §4 rollup note: registry
  flips must grep ALL LB source columns of the new files (01_/54_
  COVERAGE rows were stale until the final fix wave).

### S9-process rulings (2026-08-20, preserved from the SDD ledger before workspace deletion)

- **(a)** R30(b) numbering ruling (prep): IVA-core continues `SV-TAX`
  at 176 in `taxation/` files 07+ — one prefix per topic dir; corpus
  consistently said "01_/02_ owed to taxation/"; S6 append precedent.
- **(b)** T1 fix round 2 was a controller-verified one-liner
  (re-reviewer-prescribed LB-028 → EVID-319 cite; controller checked
  the line directly instead of a full re-review round — S1 ruling-2
  precedent).
- **(c)** T6's implementer died pre-report leaving a COMPLETE file
  (commit 9219c06 + full report on disk) — S8 ruling (b) applied:
  structure verified, committed UNMODIFIED, review gate preserved; the
  subsequent review corroborated the report fully.
- **(d)** R30(c) ordinal corrected IN-WAVE: the exclusion inciso of
  Art. 66 is the SIXTH as printed (T5 reviewer independent count) —
  67_'s "inciso sexto" citation maps DIRECTLY to the current print; the
  prep gloss ("fifth", pre-224-2009 renumbering theory) was wrong;
  master index amended by T10; the working-reading OQ stays open only
  for the numbering-history question.
- **(e)** T9's ⚠️ sibling-id items resolved by controller grep (all
  cited FREP/EINV ids exist in owning files) — reviewer-⚠️ resolution
  is the controller's job per the skill; logged.
- **(f)** T10 corrected the controller's rollup arithmetic (brief said
  "64 cited"; true = 63: 62 + 02_-flip − arithmetic check 63+9+1=73).
  Implementer-documented deviation from brief upheld.
- **(g)** Evidence hygiene folded into the final fix wave: EVID-306's
  "se emita" → "se emite" (Art. 8 txt line 148) — requirement files
  already quoted correctly; the evidence bank now matches.
- **(h)** Dispatch template (S8 ruling (c)) held for all 10 tasks +
  2 fix rounds + final review + fix wave: ZERO context-overload deaths
  (one implementer death (c) above was pre-report, not
  context-overload — its file was complete).

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
- D.O. `/seleccion/{Id}` route: **RECOVERED 2026-08-20** (serves PDFs
  again after the 500 outage since 08-18; API `/api/v1/diarios-disponibles`
  answers but the param shape 400'd on standard guesses — pin on next D.O.
  hunt from the W6.5 recipe). asamblea.gob.sv unreachable (000).
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
  double-benefit 2026 (tercerización pointer RESOLVED S9 → 11 §3.3);
  IVA-side: SOQ-54 (01_/02_ consolidation vintage watch), SOQ-55/56/57/
  58 carried in 07/08.
- Fiscal-reporting: SOQ-08 (due-day windows — **anchor consumed W17**:
  the statutory 10-hábiles layer is anchored by 75_ Art. 100 (frep/08
  LB-006, EVID-351); the by-NIT-digit window assignment remains dated
  config, still open), SOQ-13/14;
  07 OQ-008 (v17
  apéndice code 73), 06 OQ-008 (MH validation depth); 02 OQ-002 rate
  anchor ANSWERED S9 (SV-TAX-FR-240/241), 03 OQ-004 ANSWERED S9
  (SV-TAX-FR-313 zone).
- Commercial-legal: SOQ-23 SAS law, SOQ-24 quiebra vintage, SOQ-25 Ley
  Registro de Comercio, SOQ-26 Economía rate; AML new-reglamento watch
  (uif.gob.sv).
- F-11 v19/v20 + F14 v17 manual acquisitions (≥76 numbering; MH page
  watch). D.L. 598-2020 + EVID-167 tail laws (S7 SOQ-41).
- Ley IVA consolidation: **RESOLVED W16** (TF DC9226 second official
  print, reform list identical through (14) D.L. 71-2015 → 01_ current;
  registry §75-section note). Reglamento IVA: repeal instrument owned
  (75_); post-117-2001 consolidation watch continues, negative signals
  (SOQ-54 Rgto side).

## 8. Next actions (ordered)

 1. **No next synthesis wave is queued — the 8-topic program + the W17
     75_ fold-in are COMPLETE and the program MERGED (S9 → main at
     09847d0; root HANDOVER carries
     the fourteenth §4.6 run record).** Candidate follow-on work, owner's
     call: (a) consolidation/cleanup wave (CAN-STAND + S7/S8/S9 RIDE
     lists); (b) acquisitions below unlock small fold-in waves; (c)
     go-live/implementation prep per `shared/docs/go-live-readiness.md`.
 2. **Acquisition follow-ups (SOQ rides):** S8 — **SV NIIF-adopting
    instrument (Consejo de Vigilancia criteria per CC Arts. 443-444 or
    successor; SOQ-46 — the gating gap) + optional 2nd-edition NIIF
    PYMES text (SOQ-48)**; S7 — Reglamento General ZF (SOQ-31), LESIA
    (SOQ-32), DUCA user manual (SOQ-36), FOVIAL law D.L. 208-2000 +
    COTRANS instrument (SOQ-39 — also closes the 09 design rows'
    provenance), D.L. 598-2020 + EVID-167 tail laws (SOQ-41), current
    consolidations for 12_/13_/14_/17b_/74_ (SOQ-30), $18-tasa
    adjusting acuerdos (SOQ-34); S9 — current Ley IVA + Reglamento IVA
    consolidations (SOQ-54), Art. 46-f BCR instrument (SOQ-56), 167-A
    sectorial-politics instrument (SOQ-58).
  3. Registry note: numbering continues from **76** (32_/33_/75_ were already
     registered; the W16+ acquisition candidates above are the NEW numbering).
 4. SOQ follow-ups per §7; periodic external checks (factura.gob.sv,
    uif.gob.sv/marco-legal, MH formularios, D.O. recovery).
 5. Deferred cleanups (CAN-STAND): prior-wave deferred-minor lists (root
    HANDOVER §9 + per-task reviews; S7's triaged-ride list is in the
    final review record — AC-007 $1,100 Given-gap is the first-pick; S8
    and S9 RIDE lists are in their wave-log entries / SDD ledger
    copies), boilerplate sweep (~11 files + taxation 07-15 candidates),
    COVERAGE regeneration script.
 6. At wave closes: update THIS file + master index + COVERAGE + topic
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
