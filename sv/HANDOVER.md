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
  (MERGED to main at c42a600 via rebase-then-merge, twenty-third §4.6
  run in root HANDOVER, zero conflicts; pre-rebase SHAs
  562a3e3..f528181 superseded by 37778b3..c42a600)
  (SV-TAX-FR-354..396) + 01/04/13 edits (397..404; OQ-001 resolved),
  fiscal-reporting 213..214 + 06/07/08 notes, payroll 144..147 + 04 note
  — see §5 wave log.** COVERAGE after W17: 64 cited / 0 pending / 9 N/A /
  1 superseded (74 rows — zero pending again).
  The 8-topic synthesis program + W17 fold-in are COMPLETE (1,662 FRs
  total). **C1 consolidation/cleanup wave (2026-08-21): CAN-STAND
  burn-down + S3-S8/W17 rides + 43-instance boilerplate sweep + catalogs
  authority alignment + COVERAGE regen script — see §5 wave log.
  (MERGED to main at 289017e via rebase-then-merge, twenty-seventh §4.6
  run in root HANDOVER, zero conflicts; pre-rebase SHAs
  70f86f9..71d2f6d superseded by 89879bd..289017e.)**
  **W18 acquisition wave (2026-08-21/22): COMPLETE — 30 acquisitions
  76_-105_ (registry 103 files, next 106); SOQ-32/34/39/41/54-Rgto/56
  resolved, 36/46 partial, 48/58 negative-refreshed, SOQ-31 negative;
   sources only, no FR changes (1,662 FRs unchanged) — MERGED to main
   at f7fb42a via rebase-then-merge (thirtieth §4.6 run in root
   HANDOVER; one textual conflict on the T8 bookkeeping commit vs the
   main-side C1 merge record, resolved keep-both; pre-rebase SHAs
   6d0875c..dbf0cc5 superseded by 87b4b4e..f7fb42a); see §5 wave log.**
   **W19 fold-in wave (2026-08-23): COMPLETE — the W18 16-file evidence
   backlog consumed (five EV files, EVID-359..403); SV-SPE-FR-176..203
   (+28) = corpus 1,690 FRs; 14_→80_ re-key (0 survivors); COVERAGE
   81/9/2/12 of 104, gate green — MERGED to main at 33deaaa via
   rebase-then-merge (thirty-seventh §4.6 run in root HANDOVER; one
   textual conflict on the T8 bookkeeping commit vs the main-side W18
   merge record 56ee669, resolved keep-both; pre-rebase SHAs
   e86e100..c188c6c superseded by 6ab5a6a..33deaaa); see §5 wave log.**
    **W20 taxation edit wave (2026-08-23): COMPLETE — 96_ D.L. 308-2025
    Chapter V foreign-agents levy fold-in: NEW taxation/17
    (SV-TAX-FR-405..416) + taxation/09 SR8 rewire (COTRANS rows → 89_,
    FR-245 gate satisfiable) + taxation/04 vintages mirrored to 91_-94_
    (OQ-003 resolved) + spe/01 pointer flips; +12 FRs = corpus 1,702;
    COVERAGE 81/9/2/12 gate green (96_ curated note only); the W19 §8
    debts (a)(b)(c) all EXECUTED; **final whole-wave review
    USABLE-WITH-FIXES → one fix wave PASS (efa4370: index OQ-003 flip +
    per-file 17 OQ section, 09 OQ-2 phrasing reword, EXECUTED typo ×4,
    EVID-397 hygiene per S9 ruling (g)) = MERGE-READY; commits
    81e0906..efa4370 (pre-rebase; superseded by bcd4a4f..d3a9b11 —
    fix-wave SHA d3a9b11); pushed sv-research; **MERGED to main at
    1912d6a via rebase-then-merge (thirty-eighth §4.6 run in root
    HANDOVER; two textual conflicts on the T5/close commits vs the
    main-side W19 merge record eb59e17, resolved keep-both)**; see §5
    wave log.**
     **W21 COTRANS prorroga mini wave (2026-08-23): COMPLETE —
     asamblea recovered same day (`curl -k`, §6 recipe on main);
     106_ = D.L. 387-2025 acquired (the Aug-2025 prorroga: efectos →
     31-dic-2026, Art. 2; D.O. 157 T.448 22-ago-2025) + the
     previously-numberless →31-ago-2025 limb recital-pinned as
     D.L. 1000-2024 (106_ cons. II); EVID-404; spe/08 LB-013 +
     FR-189 re-stamps + **OQ-8 RESOLVED**; taxation/09 gate note;
     master-index SOQ-39 residual closure; COVERAGE 82/9/2/12 of 105
     gate green; FR corpus UNCHANGED at 1,702; registry 104 files,
     next 107 — see §5 wave log. (MERGED to main at 3627bd3 via
     rebase-then-merge — thirty-ninth §4.6 run in root HANDOVER; two
     textual conflicts vs the main-side re-probe record 15f2147,
     resolved keep-both / keep-theirs-subsumed; pre-rebase SHAs
     a5f5ea3..8a32e93 superseded by f4a861d..3627bd3.)**
    Remaining program: acquisition follow-ups (§8.2), SOQ/external watches,
    owner merge decisions.**
     **W22 acquisition wave (2026-08-23): COMPLETE — controller-direct
      (proportionate scale, asamblea-recovered route): the two SOQ-41 dated
      negatives OWNED (107_ = D.L. 201-2025 Aeropuerto del Pacífico
      capital-gains exemption, D.O. 21 T.446 30-ene-2025 stamp on face,
      efectos from 8-may-2022; 108_ = D.L. 411-2025 energía eléctrica
      acceso-universal contractor package, D.O. 181 T.448 26-sep-2025 stamp
      on face, vigencia through 26-sep-2031 — IVA exención + Art. 66
      pro-rata exception + ISR rentas no gravables + registros especiales +
      CEL-seller ganancia-de-capital exemption) + THE SAS-HUNT DISCOVERY:
      the post-2008 Código de Comercio reform set 109_-114_ (D.L. 153-2021
      bearer-share suppression; 295-2022 usura; **905-2023 = THE SAS
      STATUTE (Capítulo VIII-Bis Arts. 305-A..Z — SOQ-23 RESOLVED at
      sources level)**; 972-2024 cheque truncation; 203-2025 + 468-2025
      SAS-gratuidad chain → 31-dic-2026) — **SOQ-22's W12 "no post-2008 CC
      reform" verdict FALSIFIED (07_/73_ stale for the reformed article
      set)**. EVID-405..412 (two EV files); registry 111 numbered files,
      next 115; FR corpus UNCHANGED at 1,702 (sources wave; fold-in debts
      registered §8.1); COVERAGE 81/9/2/20 of 112 — gate green (see §5
      wave log). (MERGED to main at 8fe7854 via rebase-then-merge —
      forty-first §4.6 run in root HANDOVER; one textual conflict on
      sv/HANDOVER §1 vs the main-side W21 merge record, resolved
      keep-both; pre-rebase SHA 10963bb superseded by 8fe7854.)**
      **W23 cml fold-in wave (2026-08-23): COMPLETE — the W22 fold-in
      debt (a) EXECUTED per plan
      `docs/superpowers/plans/2026-08-23-w23-cml-sas-foldin.md` —
      subagent-driven, 6 tasks + fix rounds (T1 dispatch died zero-state
      once → re-dispatched clean; T4 one fix round = LB-029 quote-tails;
      final whole-wave review USABLE-WITH-FIXES → one fix wave PASS
      f9ab4e5: FR-246 305-Q/R SAS-eligibility routes restored — the
      plan-mandated rows the T1 brief's enumeration dropped; commits
      688b4c4..f9ab4e5). Delivered: cml/04 SAS profile (111_: FR-044
      statute_pending→in_corpus, FR-225..240 + FR-246 = formulario
      constitution, S.A.S. suffix + omission liability, $1 capital ≤2-y
      payment incl. e-wallets, free reserve, no bolsa, S.A.-supletorio
      cascade, minorities 5/10, exclusión 3/4, auditor-gate-while-
      microempresario, dividends ≤180 días, $12,000 accounting-mode
      threshold, books physical-or-electronic, simplified dissolution,
      gratuidad → 31-dic-2026, transform/fuse-into-SAS routes; LB-032
      retired in place; LB-033..038 + LB-040) + 109_ acciones re-anchors
      (FR-066/068 rewrites + FR-241..242: nominative-ABSOLUTE from
      7-oct-2021, bearer machinery dead, Art. 155 7-kind registry + CT-124
      information-duty interface, 158 no-consent traspasos, 164
      registered-titular; LB-026/028 re-anchored + LB-039) + cml/05
      fusión transnacional + Art. 358 + Art. 338 escheat (111_ Arts. 4-8:
      FR-243..245 + FR-077/079/086/097 amends + LB-031..033; Arts. 317/319
      REPLACED wholesale — marginal-notes clause gone, SAS formulario
      exception, SC comprobar-or-declarar, absorbed-abroad cancellation
      duty; escheat → Fondo General del Estado; domicilio-fixing
      continuity/adecuación) + cml/08 awareness LBs (110_ usura 960/960-A;
      112_ truncation 838-A..E; OQ-004 narrowed) + the SOQ-22
      falsification sweep (§2 verification-note flips in ALL nine 01-09
      files; six no-overlap files grep-verified). **+22 FRs → corpus
      1,724 (cml 246 FRs / 256 LBs / 142 ACs / 35 OQs); SOQ-23 FULLY
      CLOSED (OQ-001 resolved); SOQ-22 swept (residual = census negative
      watch only); COVERAGE 88/9/2/14 of 113 — gate green (109_-114_
      cited; the W22 rollup gloss was off-by-one vs its own matrix,
      corrected; 107_/108_ pending = the spe/taxation wave). Registry
      UNCHANGED (111 files, next 115).** Pushed sv-research; merge to
      main = owner decision. See §5 wave log + W23-process rulings.**
     **(MERGED to main at b793f59 same day via rebase-then-merge —
       forty-fourth §4.6 run in root HANDOVER, zero conflicts; pre-rebase
       SHAs 688b4c4..5dcbda9 superseded by b816b8f..b793f59; remote
       sv-research re-pinned via delete + re-push; both branches
       converged.)**
     **W24 spe/taxation fold-in wave (2026-08-24): COMPLETE — the W22
     fold-in debt (b) EXECUTED per plan
     `docs/superpowers/plans/2026-08-24-w24-spe-taxation-foldin.md` —
     subagent-driven, 5 tasks + fix rounds (T3 one fix round = 08-§1
     channel contradiction; T5 two fix rounds = taxation OQ-legend
     recount 81/10 + spe-index bold rebalance; T1 dispatch 1 died
     mid-work → fresh implementer finished per W18 ruling (a); commits
     44e71ac..76364f8 after plan eab7604; final whole-wave review
     MERGE-READY, 0 Critical/Important, 4 minors riding). Delivered:
     107_ D.L. 201-2025 (spe/01 LB-035 identity + taxation/03 LB-020 +
     SV-TAX-FR-418 CEPA/MOPT perimeter-seller ganancia exoneración,
     efectos from 8-may-2022 as printed) + 108_ D.L. 411-2025 (spe/01
     LB-034 + FR-200 class-member amendment [dl411_2025, admission
     dgii_escrito_vinculacion, two-layer window] + spe/02 LB-024 +
     SV-SPE-FR-204 package family + taxation/01 LB-037 + FR-417
     rentas-no-gravables chassis extension + taxation/03 LB-021 +
     FR-419 CEL-seller exoneración + express no-formulario +
     taxation/08 LB-016 + FR-224 THIRD-CHANNEL amendment [registered
     specific special-law instruments with expresada especialidad —
     Art. 174 genéricas working reading recorded] + FR-420 IVA
     exemption registry [transfers/services + import no-cascade] +
     taxation/11 LB-009 + FR-421 proveedores-locales Art.-66-proportionality
     exception) + **SOQ-40/OQ-2 RESOLVED** (T4: instruments 86_-89_/106_
     independently grep-verified rule-negative — no statutory DTE-chain
     rule; FR-244/245 confirmed as labeled product design, config-gated;
     spe/08 OQ-3 resolved-by-pointer; stale-gloss sweep) + spe/02 OQ-10
     (108_ operative-format config-gap). **+6 FRs → corpus 1,730 (spe
     204 / 256 LBs / 100 ACs / 60 OQs; taxation 421 / 310 / 290 / 91);
     SOQ-41 residual = the RAEX reglamento config-gap only — the
     EVID-167 named set fully dispositioned; COVERAGE 90/9/2/12 of 113 —
     gate green (107_/108_ cited). Registry UNCHANGED — and the count
     CORRECTED: sources/README carries 112 file rows (110 plain numbers
     01-114-minus-gaps + 17b + 25_×2), not 111; the script/README agree
     (third off-by-one-prose incident — the W22 "111" recount forgot
     17b).** Pushed sv-research; merge = owner decision. See §5 wave
     log + W24-process rulings.**


## 2. Read order for a new session

1. THIS file
2. `sv/EXTRACTION_PLAN.md` — wave log (W1–W23), reading order, risks
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
6. `sv/sources/README.md` — the registry (112 file rows, numbering
   01–114 + 17b, gaps 21/23/24/28, 25_ double vintage; next numbering =
   115)

## 3. Corpus & evidence state

- **EVID corpus 001..412** (gaps 109-127, 240 reserved-unused; W22 adds
  EVID-405..412 across two EV files: `107_108_Aeropuerto_Energia`
  (SOQ-41 residuals — D.L. 201-2025 ganancia-de-capital exoneration with
  8-may-2022 retroactivity + D.L. 411-2025 contractor package: IVA
  exención, Art. 66 pro-rata exception for local suppliers, ISR Art. 4.1
  rentas no gravables, CT 260 abuso, registros especiales, CEL-seller
  exemption) and `109-114_Reformas_CodigoComercio` (the post-2008 CC
  reform set: bearer-share suppression, usura, THE SAS STATUTE D.L.
  905-2023 Capítulo VIII-Bis, cheque truncation, the SAS-gratuidad
  chain → 31-dic-2026); W21 adds
  EVID-404 in `106_Reforma_COTRANS_DL387` — the D.L. 387-2025 COTRANS
  prorroga; W15 IVA deep
  pass EVID-304..338 in EV01's W15 section; W16 CT-reglamento EVID-339..358
  in EV75; W19 fold-in EVID-359..403 across five EV files:
  `79_100_AduanasSancciones` (T1), `86-89_FOVIAL_COTRANS` (T2),
  `80_82_LSI_ZF` (T3), `95_96_97_SpecialIncentives` (T4),
  `90-94_Transitorias` (T5)). W13 files
  (2026-08-19): `12_Ley_Zonas_Francas` (EVID-251..258),
  `14_17b_Servicios_Internacionales` (EVID-259..267),
  `13_42_43_74_Aduanas` (EVID-268..273), `31_Guia_FOVIAL_COTRANS`
  (EVID-274). W12: `71-73_AML_DL426_Instructivo380_CCverify` (EVID-241..250).
  W11: `66-70_Quincena25` (EVID-236..239). W10: `07_Codigo_Comercio`
  (EVID-211..227), `15_Ley_Lavado_Activos` (EVID-228..231, historical),
  `17_Reglamento_Lavado_Activos` (EVID-232..235, kept-mechanics citable).
  W9 payroll: EVID-191..210. W8 fiscal reporting: EVID-171..190. W7/W6.5/
  W6 ISR: EVID-088..108, 128..170. S1 foundations: EVID-001..087.
- **112 registered source file rows** (numbering 01–114 + **17b**, gaps
   21/23/24/28 = 110 plain numbers + 17b + the 25_ double vintage (pdf+xlsx)
   = 112 files — W24 bookkeeping correction: the W22 "111 files" recount
   forgot the 17b registry key; sources/README and the COVERAGE script
   parse agree on 112; historical wave-log glosses that say 111 stand
   uncorrected as history. The pre-W22 "104 files" glosses were the
   first off-by-one class; W16
   added 75_ = Reglamento de Aplicación del CT, D.E. 117-2001 — the R17/
   R30(a) mass-repeal authority instrument, EVID-339..358; W18 added
   76_-105_ = new authority instruments: CVPCPA NIIF chain 76_-78_,
   LESIA 79_, LSI consolidation 80_ (supersedes 14_), MH Recopilación
   81_, ZF reform 82_, FYDUCA 83_-85_, FOVIAL/COTRANS 86_-89_, ISR/
   customs transitories + tasas 90_-100_, Art. 46-f qualification set
   101_-105_ — W19 (2026-08-22/23) consumed the 16-file evidence-pass
   backlog (79_/80_/82_/86_-89_/90_-94_/95_/96_/97_/100_; the identity-only
   remainder is dispositioned in the registry + COVERAGE_NOTES pending-set
   rationale); W21 (2026-08-23) added 106_ = D.L. 387-2025 COTRANS
   Aug-2025 prorroga (EVID-404; asamblea print); W22 (2026-08-23) added
   107_-114_ (asamblea prints, all D.O.-stamped on face): 107_ = D.L.
   201-2025 Aeropuerto del Pacífico + 108_ = D.L. 411-2025 energía
   eléctrica (the SOQ-41 residuals) + 109_-114_ = the post-2008 CC
   reform set (D.L. 153-2021/295-2022/905-2023/972-2024/203-2025/
   468-2025 — SAS statute + bearer-share suppression + usura + cheque
   truncation + gratuidad chain).
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
  72_/17_ (R28 chain); CC 07_ (verified vs 73_). Special-regimes: 12_ (+82_
  2025 tail) / 13_ / 80_ (supersedes 14_, W19 T3 re-key) / 17b_ / 42_ / 43_ /
  74_ / 31_ + 86_-89_ FOVIAL/COTRANS (W19; consolidations end 2012-2013
  plus the 82_ tail — SOQ-30 verification watch; COTRANS prorroga chain
  W21: terminal limb instrument-owned 106_ D.L. 387-2025).

## 4. Requirements corpus (delivered)

| Topic dir | Files | FRs | Prefix |
|---|---|---|---|
| `e-invoicing/` | 6 + index | 222 (incl. §3.11 FR-159..164) | SV-EINV-FR-001..164, SV-PROT-FR-001..040, SV-CAT-FR-001..018 |
| `taxation/` | 17 + index + 2 CSV | 421 (S2: 001..175 ISR; S9: 176..353 IVA; W17: 354..404 CT procedures; W20: 405..416 foreign-agents levy; W24: 417 no-gravables chassis [01] + 418..419 ganancia exonerations [03] + 420 IVA exemption channel [08] + 421 pro-rata exception [11]) | SV-TAX-FR-001..421 |
| `fiscal-reporting/` | 8 + index + CSV | 214 | SV-FREP-FR-001..214 |
| `payroll/` | 8 + index + 2 CSV | 147 | SV-PAY-FR-001..147 |
| `commercial-legal/` | 10 + index | 246 (W23: 225..246 tails — 04 carries 225..242+246, 05 carries 243..245) | SV-CML-FR-001..246 |
| `special-regimes/` | 8 + index | 204 (W24: 204 = the 108_ package family in 02; FR-200 amended in place) | SV-SPE-FR-001..204 |
| `chart-of-accounts/` | 8 + index | 276 | SV-COA-FR-001..276 |

Totals: 1730 FRs (W17 fold-in = 57 new: taxation 354..404, fiscal-
reporting 213..214, payroll 144..147; W19 fold-in = +28: special-regimes
176..203, all other dirs unchanged; W20 fold-in = +12: taxation 405..416,
all other dirs unchanged; W23 fold-in = +22: commercial-legal 225..246,
all other dirs unchanged; W24 fold-in = +6: spe FR-204 + taxation
FR-417..421, all other dirs unchanged; taxation dir 421 FRs / 310 LBs /
290 ACs / 91 OQs; spe dir 204 FRs / 165 LBs / 100 ACs / 60 OQs). CSVs:
`withholding_tables.csv` + `isr_brackets.csv` (taxation),
`f14_income_codes.csv` (fiscal-reporting), `smm_2025.csv` +
`ss_contributions.csv` (payroll). FR numbering is wave-sequential within a
prefix; **R30(b): one prefix per topic dir — the IVA-core files continued
`SV-TAX` at 176 rather than taking a new prefix**; genuinely new topics
take new prefixes per the `<CC>-<TOPIC>-FR-nnn` contract.

COVERAGE rollup after W24 (2026-08-24 regen, gate green): 90 cited /
9 N-A / 2 superseded / 12 pending (113 rows = 112 registry file rows +
the schemas/ dir row; W24 flips: 107_/108_ pending → cited [spe/01+02 +
taxation/01/03/08/11 LB columns]. The 12 pending = the W18 identity-only
set, rationale in COVERAGE_NOTES. Registry-count correction W24: the
W22-onward "111 files" prose forgot the 17b registry key — README/script
parse = 112 file rows (third off-by-one-prose incident; standing lesson
re-confirmed: counts derive from the README/script parse, never from
gap arithmetic). S8
lesson (standing): registry flips
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

- **W24 (2026-08-24):** spe/taxation fold-in wave COMPLETE per plan
  `docs/superpowers/plans/2026-08-24-w24-spe-taxation-foldin.md` —
  subagent-driven, 5 tasks + per-task reviews (T1/T2/T4 Approved clean;
  T3 one fix round = taxation/08 §1 channel-sentence contradiction with
  the amended FR-224(c) + 11 §1 FR-421 note + LB-009 kin reword; T5 two
  fix rounds = taxation OQ-legend recount 81/10 [books three pre-W24
  resolutions: 04 OQ-003 W20, 08 OQ-2 W18, 09 OQ-3 W19] + spe-index
  bold rebalance; T1 dispatch 1 died mid-work leaving conformant spe/01
  preamble edits → fresh implementer finished per W18 ruling (a);
  commits 44e71ac..76364f8). Delivered: **(1) 107_ D.L. 201-2025** —
  spe/01 LB-035 identity row (base law D.L. 361-2022 un-acquired;
  perimeter = external config) + taxation/03 LB-020 + **SV-TAX-FR-418**
  (CEPA/MOPT perimeter-seller ganancia-de-capital exoneración, efectos
  retrotraídos al 8-may-2022 per the substituted Art. 35 as printed —
  the [as printed] 8-may-vs-7-may note in the LB gloss; vigencia
  7-feb-2025); **(2) 108_ D.L. 411-2025** — spe/01 LB-034 identity +
  **FR-200 class-member amendment** (instrument dl411_2025; admission
  dgii_escrito_vinculacion, resolución ≤10 días hábiles; TWO-layer
  window: decree vigencia 27-sep-2025→26-sep-2031 + per-benefit
  firma→recepción/fin-relación-CEL; Art. 11 especialidad prevalence
  flag) + spe/02 LB-024 + **SV-SPE-FR-204** package family (Art. 2
  literals a/b/c incl. the no-cascade import guard + the
  proveedores-locales/Art.-66 paragraph; ISR no-gravada until completa
  recepción; registros especiales + CT-147 conservation + vinculación
  annotation; CT-260 abuso revocation + liquidar-from-ejercicio;
  personal-use/activo-corriente carve-outs; CEL-seller + CNR-arancel
  limbs; OQ-10 = operative-format config-gap [DGII escrito/resolución
  format + MH Art. 12 directrices + documental presentation — EV file
  OQ-1 rides]) + taxation/01 LB-037 + **FR-417** (isr_no_renta_rule
  value `programa_energia_dl411_art3` on the FR-173 chassis; no-
  retention consequence per the 97_/spe-02-OQ-9 working reading) +
  taxation/03 LB-021 + **FR-419** (propietarios O POSEEDORES voluntary
  sellers to CEL; EXPRESS no-formulario lift — the class distinction vs
  FR-418 encoded, not blurred) + taxation/08 LB-016 + **FR-224
  THIRD-CHANNEL amendment** (registered specific special-law instruments
  with expresada especialidad + vigencia, config-gated — the Art. 174
  "genéricas" working reading recorded in-row [specific
  instrument-bounded grant + Art. 11 prevalence + CT 6-b recital;
  in-corpus precedent 97_/LB-023]; the rejection limb for GENERIC
  foreign-law claims INTACT) + **FR-420** IVA exemption registry
  (transfers/services rows + import DAI/IVA/gravámenes rows, no-cascade
  flag, exemption reason cites the instrument channel) + taxation/11
  LB-009 + **FR-421** (local suppliers selling to 108_ beneficiaries:
  Art. 66 proportionality NOT applied on those operations — FR-277
  chassis with an express-statutory anchor; denominator-side relief
  reading recorded; 97_ same-substance kin noted). **(3) SOQ-40/OQ-2
  RESOLVED (T4)** — the four owned FOVIAL/COTRANS instruments
  (86_/87_/88_/89_) independently grep-verified RULE-NEGATIVE (no DTE/
  chain prescription; nearest-miss classes dispositioned); the 2001
  control-account chain = 31_-guide practice vintage; FR-244/245
  CONFIRMED as labeled product design (D1-line-per-operation echo,
  config-gated; re-validation trigger = any future MH/DGII chain rule);
  spe/08 OQ-3 resolved-by-pointer; stale-gloss sweep (master index +
  spe/08 + taxation/09 prose tails; FR-244/245 row bodies untouched).
  **+6 FRs → corpus 1,730** (spe 204/165/100/60; taxation 421/310/290/
  91); SOQ-41 residual = the RAEX reglamento config-gap (96_) only —
  the EVID-167 10-instrument named set fully dispositioned; COVERAGE
  90/9/2/12 of 113 gate green; registry UNCHANGED (112-file-row count
  corrected — see §3/§4). **Final whole-wave review: MERGE-READY, 0
  Critical/Important, 4 minors riding** (window_kind token split
  spe/01-vs-spe/02 — reconcile at next spe touch; AC-015 whitespace;
  FR-417 window-sketch tension; 03 §5 stamp-name cells). Pushed
  sv-research; merge = owner decision.

- **W23 (2026-08-23):** cml fold-in wave COMPLETE per plan
  `docs/superpowers/plans/2026-08-23-w23-cml-sas-foldin.md` —
  subagent-driven, 6 tasks + per-task reviews (T1-T3/T5/T6 Approved
  clean; T4 one fix round = two LB-029 silent quote-TAIL truncations
  extended per the omission-marker discipline; T1's first dispatch died
  zero-state → re-dispatched clean; commits 688b4c4..024a1de + fix wave
  f9ab4e5). **T1** cml/04 SAS profile: §2 SOQ-22 stale-print flip +
  SAS-design resolution; LB-032 retired in place; LB-033..038 (111_
  verbatim spine incl. the consolidated Art. 10 gratuidad terminal text
  + chain; "305-0" [sic, read 305-O] discipline); FR-042 amended (Art.
  17 one-will-or-agreement basis; Art. 18-II-c sixth type); FR-044
  flipped to in_corpus; NEW §3.8 FR-225..240 (formulario constitution,
  S.A.S. suffix + unlimited-solidary omission liability, statutory
  defaults, unipersonal, $1 capital + ≤2-y payment incl. e-wallets,
  free reserve, bolsa-blocked, governance cascade + tech meetings,
  minorities 5/10, exclusión 3/4 + reintegro ≥ valor contable, 305-O
  fraud liability, auditor-gate-while-microempresario [criteria =
  config-gap], dividends ≤180 días, $12,000 accounting-mode threshold
  [≠ Art. 437 keeper threshold — different instrument], books
  physical-or-electronic [Art. 455 24-month gate read not to govern SAS
  statutory books per 305-J print — recorded as reading], simplified
  dissolution clocks, gratuidad window rows → 31-dic-2026); §4
  society.type sas profile + `sas.formulario` entity; AC-004 rewrite +
  AC-015..018; OQ-001 resolved. **T2** 109_ acciones re-anchors:
  LB-026/028 re-anchored (operative quotes from 109_; effective
  7-oct-2021; Art. 134 survivors = incisos 3-5 as printed — the brief's
  "3-4" was a miscount) + LB-039 (Arts. 153/158-II/164/212 +
  transitorio awareness incl. RUC-block); FR-066 rewritten
  (nominative-ABSOLUTE, bearer-conversion gate removed, provisional-
  title ≤1-y clock survives) + FR-068 amended (7-kind registry,
  debidamente-actualizado duty, CT-124 pointer) + NEW FR-241
  (nominative-title mechanics: no-consent traspasos of paid acciones
  even contra pacto; registered-titular rule) + FR-242 (CT-124
  shareholder/dividend information-duty interface → taxation by id;
  RUC-block/SSF-bar/conversion-window = awareness gloss);
  `nominative_to_bearer` entry_kind retired with D15 migration note;
  AC-019. **T3** cml/05: §2 flip + LB-005/018 annotations + LB-006/008
  re-anchors + LB-031..033 (111_ Arts. 4-8 + 109_ Arts. 7-8 verbatim);
  FR-077 amended (new-317 registration limb — marginal-notes duty
  superseded), FR-078 verified untouched (Arts. 318/320 un-reformed),
  FR-079 rewritten (SAS formulario exception, SC comprobar-or-declarar,
  absorbed-abroad cancellation duty + failure → personality persists),
  FR-086 amended (3-días-hábiles deposit clock; 5-y escheat → Fondo
  General del Estado; bearer limbs dead), FR-097 amended (home-law
  permission gate + domicilio-fixing route); NEW FR-243 (fusión
  transnacional enablement + governing-law split), FR-244 (SV-only
  inscription; notary foreign-doc duty; cancellation-duty state
  machine), FR-245 (SV-domicile fixing: personality continuity +
  adecuación escritura); AC-017..020; OQ-002 reshaped-open. **T4**
  cml/08: §2 flip + awareness LB-028 (110_ usura: 960-III BCR
  consultation + 960-A nullity of the usurious slice; Tasa Máxima
  Legal = BCR external series, never shipped; vigencia 4-may-2022) +
  LB-029 (112_ truncation 838-A..E incl. multas 100-1000 SMM
  comercio/servicios/industria + the cross-capítulo SMM-extension
  sentence; vigencia 19-abr-2024); FR-158 pre-110_-print note; OQ-004
  narrowed-open (BCR norms ≤90 días + interbank rules still
  un-acquired). **T5** the six no-overlap files (01/02/03/06/07/09)
  §2 verification-note flips (per-file grep-verified zero
  reformed-article citations; Art. 1582 C. Civil-code false positive
  handled). **T6** cml/00_index + master-index rollups + COVERAGE
  regen. **Final whole-wave review: USABLE-WITH-FIXES → one fix wave
  PASS (f9ab4e5): I-1 = FR-246 305-Q/R SAS-eligibility routes restored
  (any society → SAS transformación quorums incl. 3/4-títulos
  SAS→other; parent-SAS >90% simplified absorption — SAS-absorbing-SAS
  only per the 305-R print, acciones only; consuming FR-080..082/
  077..079/225 by id) + LB-040 + §3.8 tail scope note + recount
  246/256/142 / corpus 1,724 + COVERAGE regen = MERGE-READY.** Deferred
  minors riding (next cml touch): "225..246" range glosses spanning
  05's 243..245 in three descriptive surfaces (00_index 04-row,
  numbering note, MASTER C4/SOQ-23 annotations — strict form "225..242 +
  246"); LB-034 "finalidad especifica" [sic]; §3.8 heading note landed
  in the fix wave; LB-018 paraphrase-in-quotes de-quote; Art. 338
  double-quoted (LB-018 + LB-033) collapse; LB-039 transitorio
  numerals 3-4; five files' line-wrap. Chapter-spine residual: 305-C
  (accionista-not-employee), 305-I (proof-of-existence document),
  305-T (arreglo directo/arbitraje) uncited by scoping — record for the
  next 111_ touch.

### W24-process rulings (2026-08-24, preserved from the SDD ledger before workspace deletion)

- **(a)** T1's first dispatch died mid-work (truncated return) leaving
  CONFORMANT uncommitted spe/01 preamble edits — controller verified the
  partial diff against the brief, then a FRESH implementer finished
  (W18 ruling (a) kin; dispatch fatality remains the standing
  first-failure mode — third consecutive wave).
- **(b)** Controller routing: spe/08 §7 OQ-3 (the SOQ-40 pointer OQ) was
  not in T4's brief — its resolution flip was routed into T5's dispatch
  with PRESCRIBED text rather than a controller hand-edit (keeps the
  review gate; S9 ruling (b) kin for the prescribed-text form).
- **(c)** T5 fix round 2 = the re-reviewer's exact one-line prescription
  (bold-span rebalance); controller verified the line directly instead
  of a third re-review dispatch (S9 ruling (b) precedent — one-liner,
  no full round).
- **(d)** T5 fix round 1 lesson: the taxation/00_index OQ legend was
  stale by THREE pre-W24 resolutions (04 OQ-003 W20, 08 OQ-2 W18,
  09 OQ-3 W19) that WERE recorded in the per-file bullets — legends and
  rollups need MECHANICAL recounts at every index touch; per-file
  bullets do not propagate upward by themselves (same class as the
  rollup-prose-from-matrix lesson).
- **(e)** T5's two W21 booking catch-ups (spe/08 LB count 12→13; spe OQ
  legend) ruled benign index bookkeeping — the wave that adds an LB row
  owns the count it can see is stale; disclosed in the implementer
  report, verified by the reviewer.
- **(f)** Registry count corrected at bookkeeping: sources/README parses
  to 112 file rows (110 plain numbers + **17b** + 25_×2) — every
  "111 files" gloss since W22 forgot the 17b registry key. Third
  off-by-one-prose incident; counts derive from the README/script parse,
  never from gap arithmetic.
- **(g)** T4's rule-negative verification (the OQ-2 resolution basis)
  was independently RE-RUN by the task reviewer (grep reproduction, hit
  classes dispositioned) — resolution-carrying verifications get
  reproduced, not trusted.

### W23-process rulings (2026-08-23, preserved from the SDD ledger before workspace deletion)

- **(a)** T1's first dispatch died with ZERO state — re-dispatched clean
  (S7 ruling (c); recurring — dispatch fatality remains the standing
  first-failure mode).
- **(b)** The T2 brief's "incisos 3-4" was a MISCOUNT: the 07_ print of
  Art. 134 has five incisos (1 replaced, 2 derogated, survivors 3-5) —
  the implementer's as-printed reading upheld (evidence-based
  implementer override of a plan pointer defect, W17 ruling (a) kin).
- **(c)** FR-241/242 placement at the §3.8 tail: numbering contiguity +
  the file's ascending-FR reading order beat the brief's zone planning;
  a heading scope note was added in the fix wave (T2-M-1).
- **(d)** FR-246 saga: the T3 brief's header said "FR-243..246" but its
  allocation text defined three FRs — allocation governed (T3-a);
  SUPERSEDED at the final review: the plan's Global Constraints had
  mandated 305-Q/R SAS-eligibility rows which the T1 brief's 16-FR
  enumeration silently dropped — I-1, fixed in the one fix wave by
  minting FR-246 per the plan. **Lesson: per-task review gates must
  check the plan's Global-Constraints deliverables against the brief
  enumerations, not only the brief's own list.**
- **(e)** T4 process note: verbatim self-checks must check quote TAILS,
  not only intra-word spacing (two silent tail truncations escaped);
  fix = quote extension preferred over omission markers when the
  dropped text carries substance.
- **(f)** T6 rollup arithmetic: the W22 rollup prose was off-by-one vs
  its own committed matrix (81/112 vs actual 82/113) — the regen
  flipped exactly 6 rows; actuals + a correction note recorded, matrix
  never hand-forced (W20 ruling (d) precedent; second off-by-one-prose
  incident — standing lesson: rollup prose derives from the matrix).
- **(g)** Routing corrections (pre-flight R-1): fusión transnacional +
  Art. 358 + Art. 338 escheat folded into cml/05, NOT cml/02/03/08 as
  the W22 EVID-409 gloss routed — corpus LB ownership governs; the EV
  file's OQ-1 row rides untouched as the historical acquisition-time
  routing.
- **(h)** The 07_ extraction txt (pre-W14, main-checkout-only) was
  regenerated worktree-local, byte-identical — closes the S8 ruling (a)
  gap for any pre-worktree txt a future wave needs.
- **(i)** Fix wave: 305-R's simplified absorption is SAS-absorbing-SAS
  only ("de otra sociedad por acciones simplificada", acciones only) —
  the controller dispatch's looser "acciones/participaciones of any
  sociedad" was tightened by the implementer for verbatim fidelity
  (upheld; proofread controller-authored fact strings, W20 ruling (h)
  kin).

- **W22 (2026-08-23):** SOQ-41 residuals + SAS hunt acquisition wave
  COMPLETE — controller-direct (no subagents; proportionate scale, W21
  precedent). Trigger: §8.2 follow-ups newly unblocked by the asamblea
  recovery. External state: asamblea UP (second day); **D.O. degraded
  further to NXDOMAIN**; uif still SOA-only no-A; factura 200; MH
  formularios path 302→home (wp-content re-pin at the next watch).
  Route: by-year enumeration → card → view/<id> → PDF (W21 recipe);
  all eight decree PDFs carried the 8-byte junk prefix (now proven
  systemic to the asamblea document server); the 111_ print is a
  CONSOLIDATED REPRINT carrying later-reform stamps (living-document
  pattern — expect on future reform-chain acquisitions). **8
  acquisitions = 107_-114_:** 107_ D.L. 201-2025 (ganancia-de-capital
  exoneration for CEPA/MOPT airport-perimeter sellers; new Art. 35
  retrotrae efectos al 8-may-2022; D.O. 21 T.446 30-ene-2025 — the
  unpinned issue now stamped) + 108_ D.L. 411-2025 (BID/CEL electrification
  package, vigencia → 26-sep-2031: IVA exención total, **Art. 66 pro-rata
  NOT applied by local suppliers**, ISR 4.1 rentas no gravables until
  reception, CT 260 abuso revocation, registros especiales, CEL-seller
  exemption + no formulario duty; D.O. 181 T.448 26-sep-2025) + the
  SAS-hunt discovery: a full por-anios census 2016-2026 found the
  **post-2008 CC reform set** — 109_ D.L. 153-2021 (bearer shares banned
  from 7-oct-2021; "Las acciones serán siempre nominativas"; RUC-blocking
  transitorio; staleness hit on every cml LB quoting 07_'s
  Arts. 134/153/155/158/164/212/219/337/338), 110_ D.L. 295-2022 (usura
  960-III + 960-A nullity), **111_ D.L. 905-2023 = THE SAS STATUTE**
  (SOQ-23 RESOLVED at sources level: sixth society type via Art. 18-II-c
  + Capítulo VIII-Bis 305-A..Z — formulario constitution, unipersonal,
  $1 capital, free reserve, ≤180-day dividends, $12,000 accounting
  threshold, no-auditor-while-microempresario, simplified dissolution;
  fusión transnacional + foreign domicilio; vigencia 11-feb-2024), 112_
  D.L. 972-2024 (cheque truncation 838-A..E, multas 100-1000 SMM), 113_
  D.L. 203-2025 + 114_ D.L. 468-2025 (SAS-gratuidad → 31-dic-2026
  terminal; 114_ cons. III: SAS = "el tipo societario de mayor uso").
  **SOQ verdicts: SOQ-22 FALSIFIED-AND-RE-RESOLVED** (W12 two-stale-
  consolidations verdict dead; census caveat: por-anios has no cards for
  2010/2012-2015, 2019 partial — negative watch rides), **SOQ-23
  RESOLVED at sources level** (cml/04 OQ-001 sources-resolved, fold-in
  pending), **SOQ-41 both negatives OWNED** (EVID-167 named set
  10-of-10; residual = RAEX reglamento config-gap). EVID-405..412.
  Corpus edits at index/status level only (cml/04 OQ-001 + cml/00 + spe/00
  + spe/01 + master index + registry + COVERAGE). **FR corpus UNCHANGED
  at 1,702; registry 111 files, next 115; COVERAGE 81/9/2/20 of 112 —
  gate green** (+8 pending rows with COVERAGE_NOTES rationale; the
  pre-W22 "104 files" glosses corrected). **Fold-in debts born: (a) cml
   edit wave — FR-044 SAS flip + profile rows, acciones re-anchors,
   usura/truncation/338 notes, gratuidad window; (b) spe/taxation wave —
   107/108 exemption surfaces.** Commits: 10963bb pre-rebase → 8fe7854
   post-rebase (main merge + record c4eda40 — forty-first §4.6 run);
   the W22 bookkeeping commit (SHAs recorded) rode to main afterwards as
   4319603 → 15b48a4 (rebase onto the parallel GT forty-second-run
   854cc47, clean) — both branches converged; session closed.

- **W21 (2026-08-23):** COTRANS Aug-2025 prorroga mini acquisition wave
  COMPLETE — controller-direct (no subagents; proportionate scale —
  one instrument, one OQ target). Trigger: the wave-cadence external
  re-probe found **asamblea.gob.sv RECOVERED** (A-records restored;
  TLS 1.3 answers but chain incomplete → `curl -k` REQUIRED; keyword
  search useless — the working route is `/leyes-y-decretos/decretos-
  por-anios/<year>/0` card enumeration → view/<id> → document PDF).
  **106_ = D.L. N° 387 (2025) acquired** (DADO 19-ago-2025; D.O. 157
  T.448 22-ago-2025 stamp on face; 2 pp; served with 8 junk prefix
  bytes — trimmed + qpdf-relinearized; EVID-404): Art. 2 extends
  D.L. 257-2021 efectos → **31-dic-2026** (direct instrument
  provenance for spe/08 FR-189's terminal row); Art. 3 vigencia =
  publication day 22-ago-2025; Art. 17-A cajas-únicas reform
  (authority-side). **Considerando II recital-pins the numberless
  limbs: D.L. 617-2022 + D.L. 1000-2024 (D.O. 77 T.443 25-abr-2024)
  = the →31-ago-2025 prorroga** (617/1000/307 texts stay un-acquired
  — verification watch; official-recital provenance class). Corpus:
  spe/08 LB-013 minted + FR-189/LB-012 re-stamps + **OQ-8 RESOLVED**;
  spe/00_index + taxation/09 gate note; master index SR8/SOQ-39
  closure; registry 104 files (next 107). **FR corpus UNCHANGED at
  1,702** (provenance wave). **COVERAGE 82/9/2/12 of 105 — gate
  green.** Same-day external state: D.O. + uif still DNS-absent;
  factura 200. Follow-ups born: none (SOQ-40/OQ-2 unchanged-open);
  optional D.O. print of D.L. 387 when D.O. recovers. Commits:
  a5f5ea3 (sv-research). Merge to main = owner decision.

- **W20 (2026-08-23):** taxation edit wave COMPLETE per plan
  `docs/superpowers/plans/2026-08-23-w20-taxation-edit-wave.md` —
  subagent-driven, tasks T1-T4 + controller prep (T2/T3 Approved clean;
  T1 one fix round = quote fidelity — txt-normalized "sin deducción"
  variant noted, two reviewer prescriptions rejected on txt evidence +
  re-review upheld; T4 one fix round = curated 96_ COVERAGE note;
  commits 81e0906..89443fe). **T1** NEW `taxation/17_foreign-agents-levy.md`
  (SV-TAX-FR-405..416; 12 FRs / 10 LBs / 9 ACs / 4 OQs) = the 96_ D.L.
  308-2025 Chapter V 30% levy fold-in, cluster L1 · **T2** taxation/09
  SR8 rewire (COTRANS rows anchored to 89_; FR-245 gate satisfiable) ·
  **T3** taxation/04 aguinaldo vintages mirrored to 91_-94_ + **OQ-003
  RESOLVED** + master-index R22/SOQ-05 appends · **T4** spe/01 + spe
  index + EV95/96/97 OQ-2 pointer flips, taxation/00_index 17-row +
  totals 416/305/283/91, COVERAGE regen. **SV-TAX-FR-405..416 (+12) →
  corpus 1,702 FRs**; registry unchanged (103 files, next 106); COVERAGE
  81/9/2/12 of 104 stands, gate green (96_ curated note only). SOQ
  verdicts: **SOQ-41 96_-Chapter-V half consumed** (residuals = D.L.
  201-2025 + 411-2025 dated negatives + RAEX reglamento config-gap);
  spe/01 OQ-6 + taxation/04 OQ-003 resolved; MOQ-04 stays closed;
  **SOQ-40/OQ-2 (taxation/09) still open — the D1-mapping design
  confirmation, now unblocked by the rewire**. The W19 §8 debts (a)(b)(c)
  ALL EXECUTED. Follow-ups: EV-bank hygiene queue (EVID-397 "sin
  dedcción [sic OCR]" + dropped "se" — S9 ruling (g) precedent; rides
  this wave's final fix wave) + FR-244 OQ-2 phrasing (deferred minor).
  **Final whole-wave review + fix wave pending; merge-pending at edit
  time. Merge to main = owner decision (thirty-eighth §4.6 run).**

- **W19 (2026-08-22/23):** W18 fold-in/evidence wave COMPLETE per plan
  `docs/superpowers/plans/2026-08-22-w19-w18-foldin.md` — subagent-driven,
  8 tasks (T1 fix round; T3 two fix rounds; T4 fix round; T5 first
  dispatch died zero-state → re-dispatched clean; T2/T5/T6/T7 Approved;
  commits ecd553d..3047745). Five EV files, **EVID-359..403 gapless**:
  T1 `79_100_AduanasSancciones` (LESIA + 100_/D.L. 124-2015 +
  98_/99_ $18 chain; **SOQ-32/34 consumed**) · T2 `86-89_FOVIAL_COTRANS`
  (SR8 provenance/identity/vigencia; **SOQ-39 consumed; MOQ-04 CLOSED**)
  · T3 `80_82_LSI_ZF` (**14_→80_ re-key = 38 LB columns + 47 inline,
  0 survivors**; 12m/24m clock invariant HOLDS; ZF 82_ tail folded;
  SOQ-30 watch narrowed) · T4 `95_96_97_SpecialIncentives` (**95_
  horizon TEXT-PINNED 15 años**; 96_ Chapter V routed out-of-wave) ·
  T5 `90-94_Transitorias` (aguinaldo-cap vintages re-anchored to
  91_-94_; D.L. 598-2020 historical note) · T6 identity-notes sweep
  (SOQ-46 coa refresh; **SOQ-56 OQ-2 resolved** = BCR-list membership;
  SOQ-36/58 refreshed, stay open) · T7 indexes + COVERAGE regen
  (**81/9/2/12 of 104, gate green**) + external-check note · T8
  bookkeeping + registry §89 figures fix ($250/$500). **SV-SPE-FR-176..203
  (+28) → corpus 1,690 FRs**; SOQ-41 96_ pointer dispositioned. External
  checks: factura/MH no drift; **D.O. + uif DNS-level outage since
  2026-08-22** (§6). Follow-up debts: SR8 rewire backlog, 96_ Chapter V
  taxation-wave fold-in, taxation-side 2025+ standing-rule mirror (§8).
  **Final whole-wave review: USABLE-WITH-FIXES → one fix wave PASS
  (67f75bc: master-index stale pre-W19 authority claims cleared — SR8
  re-anchored to instruments 86_-89_ w/ EVID-374..379 + MOQ-04 closed,
  SR6 LB line + SOQ-34 resolution, SR7 LESIA consumed, preamble 31_
  demoted; final-review I-1, prescribed edits) = MERGE-READY.** Deferred
  minors triaged: 2 ignore (COVERAGE.md:18 "zero pending" aside; EVID
  cosmetic nits), rest ride (HANDOVER:645 AML phrasing, spe/08
  historical misprint-notes, spe/04 OQ-1 pointer, coa OQ wording,
   taxation/09 rewords = SR8 backlog). Commits ecd553d..67f75bc;
   pushed sv-research. **Merged to main at 33deaaa same day —
   thirty-seventh §4.6 run; see §1 record.**

### W20-process rulings (2026-08-23, preserved from the SDD ledger before workspace deletion)

- **(a)** T1 quote-fidelity ruling: where the EV bank and the primary
  extraction txt diverge on an unambiguous OCR artifact (EVID-397's
  "sin dedcción [sic OCR]" vs the txt's normalized "sin deducción
  alguna"), the TXT governs the LB/FR quotes; the variant survives only
  in non-quote notes. EV-bank transcription fixes ride fix waves per the
  S9 ruling (g) precedent (EVID-397 hygiene landed in the W20 fix wave).
- **(b)** T1 fix round: TWO reviewer-prescribed edits were rejected by
  the implementer on direct txt evidence (txt L48 prints `de lo
  "dispuesto`; L50 is blank) — re-review UPHELD both rejections (W17
  ruling (a) kin: evidence-based implementer override of a review
  pointer defect, grep-evidenced).
- **(c)** Controller applied the W20-A citation-rule amendment as a
  verified one-liner post-T1 (S9 ruling (b) precedent).
- **(d)** T4: a curated COVERAGE_NOTES refresh was sanctioned by the
  reviewer's prescription (supersedes the wave's no-manual-edit default
  for the 96_ row — the scanner half already listed taxation/17's LB
  cites, so the stale curated gloss self-contradicted).
- **(e)** T5 review routed the taxation/00_index per-file OQ-003 stale
  "open" marker (a T3/T4 edit-set split) to the final fix wave — the
  wave owns index consistency; the fix wave added the per-file 17 OQ
  section on the same precedent (W17 pattern).
- **(f)** Final-review triage stands: the indexes' prose "85 open /
  6 resolved" watch-flavor totals = house convention (registers are the
  record); narrative reflow + report token-count minors = ignore.
- **(g)** Mechanical: `build_coverage.py --check` REQUIRES the country
  arg (`sv --check`); bare `--check` misparses as the country and
  errors.
- **(h)** The "EXECUTATED" ×4 typo originated in a controller dispatch
  and was faithfully carried into files — fixed in the fix wave; lesson:
  proofread controller-authored fact strings before dispatch.

### W19-process rulings (2026-08-23, preserved from the SDD ledger before workspace deletion)

- **(a)** Pre-flight (standing): harness exposes no per-subagent model
  parameter (S7 ruling (d)) — dispatches inherit the session model;
  Model-Selection sections honored only in dispatch complexity framing.
- **(b)** Pre-flight (standing): SDD workspace deletion at wave close
  MUST be preceded by rulings preservation into sv/HANDOVER.md §5 (repo
  convention overrides the skill default of silent deletion).
- **(c)** T3's spe/04 touch beyond the brief file list UPHELD (binding
  S8 re-key rule — the 12m-clock rows cite 80_ where LSI-side).
- **(d)** T3's SOQ-33/SOQ-42 two-token locator flips were
  controller-applied per the S9 ruling-(b) precedent (re-review had
  prescribed the exact edits).
- **(e)** T4's 96_ Chapter V ruling: the plan's "no-real-surface"
  hypothesis was REFUTED by reading — Chapter V is a REAL
  30%-withholding surface; out-of-wave OQ routing upheld by the reviewer
  (SOQ-40 precedent; scope bars left no in-wave home; three durable loci
  + FR-201 pointer).
- **(f)** T5's first dispatch died with ZERO state — re-dispatched
  clean (S7 ruling (c)).
- **(g)** Controller routing: T2's deferred taxation/09 FOVIAL-staleness
  spots rode the T6 dispatch (same SOQ-39-consumed class; T6 owns
  taxation identity notes); T2's registry §89 compensation misprint
  ($200/$400 vs the printed $250/$500) was verified-then-fixed inside
  T8 (89_ txt checked first).

- **W18 (2026-08-21/22):** acquisition follow-ups wave COMPLETE per plan
  `docs/superpowers/plans/2026-08-21-w18-acquisition-followups.md` —
  subagent-driven, 8 tasks (per-task reviews Approved; T4 + T6 one fix
  round each; T2 + T6 first dispatches died silently — T2 left state,
  re-dispatched to finish; T6 zero-state, re-dispatched clean; commits
  6d0875c + 9c98e5c..4cccb24). **30 acquisitions 76_-105_** (registry
  103 files, next 106): CVPCPA NIIF chain 76_-78_ (**SOQ-46 PARTIAL** —
  authority owned, PYMES-vs-full criteria unfound; candidates Res.
  175-2023 / 82-2024); LESIA 79_ (**SOQ-32 closed**); LSI consolidation
  80_ thru D.L. 277-2013 (**SUPERSEDES 14_**); MH Recopilación 81_; ZF
  reform D.L. 493-2025 = 82_; FYDUCA 83_-85_ (**SOQ-36 partial** —
  manual Portal-internal, Res. 409-2018 current); FOVIAL/COTRANS 86_-89_
  (**SOQ-39 RESOLVED** — $0.20/gal = the D.L. 597-2001 Art. 26 REFORM;
  COTRANS = D.L. 257-2021 PASSENGER-tariff $0.10/gal Art. 3 to
  31-dic-2026, IDENTITY CORRECTION vs "transportistas de carga");
  90_-100_ ISR/customs set (**SOQ-41 closed** — D.L. 598-2020 spent,
  aguinaldo caps $1,100→$1,500, **SOQ-34 RESOLVED** $18.00 never
  adjusted; 100_ = D.L. 124-2015 → **74_ Art. 12-B parity break**,
  SOQ-30 annotated); 101_-105_ Art. 46-f set (**SOQ-56 RESOLVED** —
  flag = BCR-list membership; **SOQ-54 Rgto RESOLVED-AS-PARITY** DC5855
  ≡ 02_; **SOQ-58** negative refreshed; **SOQ-48** optional-negative).
  **SOQ-31 Rgto-ZF NEGATIVE** (never-issued hypothesis; D.O. Oct-Dic
  1998 micro-scan optional). T1 external checks: no factura/MH drift;
  uif WAF-blocked (403 all routes); D.O. API recipe PINNED (§6). Route
   intel in §6; per-task detail in the SDD ledger + EXTRACTION_PLAN W18
   entry (incl. next-wave fold-in debt). **Sources only, no FR changes —
   final whole-wave review MERGE-READY (zero Critical/Important; deferred
   minors all triaged ride/ignore: SOQ-30:705 + SOQ-39:714 nested-bold
   rendering nits ride to W19 which re-edits both rows; 95_ junk-prefix
   trim + vigencia/horizon read ride with its evidence pass).**
   **MERGED to main at f7fb42a (thirtieth §4.6 run in root HANDOVER;
   pre-rebase SHAs 6d0875c..dbf0cc5 superseded by 87b4b4e..f7fb42a).**

### W18-process rulings (2026-08-22, preserved from the SDD ledger before workspace deletion)

- **(a)** T2's first dispatch died silently leaving 3 COMPLETE downloads
  uncommitted (76_/77_/78_) — controller verified integrity, then a FRESH
  implementer finished (registration/verdict/commit). NOT the
  commit-unmodified path (S7 (a)/S8 (b)/S9 (c) apply to COMPLETE work;
  here the task itself was incomplete).
- **(b)** T6's first dispatch died with ZERO state — re-dispatched clean
  (S7 ruling (c)).
- **(c)** Plan's T2 file list said "Modify HANDOVER §7"; deferred to T8's
  wholesale §7 refresh (master index = register of record meanwhile);
  T7's stale-count Important finding (§3 "73 files") routed to T8 the
  same way.
- **(d)** T4's COTRANS D.O. window re-bounded to Dec-2021 by the identity
  correction (plan's 2001-2002 era was wrong); T5's tasa hunt skipped
  D.O. via documentary supersession (2015+2025 DACG prints both $18) —
  both deviations upheld by the final review.
- **(e)** Registration ownership: each task registers its own
  acquisitions; T7 = consolidated verification only (found+fixed 14
  cross-task defects: stale counts, missing CTG/no-D.O. notes).
- **(f)** T8's §9 numbering→106 edit beyond brief upheld (contradicted
  §2/§3/§8 otherwise; C1 ruling (c) precedent).
- **(g)** Controller pinned the D.O. API param shape pre-wave
  (form-encoded `year`/`month`; JSON+query fail) — T1 recorded it in §6;
  TF-catalog-via-Wayback-CDX + SIECA-S3-presigned recipes proven in-wave
  (§6). uif.gob.sv WAF-block began 2026-08-21 (re-probe next sweep; AML
  watch deadline 2026-10-17 stands).

- **C1 (2026-08-21):** consolidation/cleanup wave COMPLETE per plan
  `docs/superpowers/plans/2026-08-21-c1-sv-cleanup-wave.md` — subagent-driven,
  10 content tasks + controller bookkeeping (T3 dispatch died silently once,
  re-dispatched clean per S7 ruling (c); T6 one fix round — PAGE 162 anchor
  block-boundary misread; all other reviews Approved clean 0 C/I). Scope:
  CAN-STAND burn-down + S3/S4/S5 wave minors + S7 AC-007 Given-gap ($1,100
  added) + S8 rides (LB-001 gloss, LB-004 PAGE 162, AC-001 arithmetic
  inlined; A1 period correctly ZERO-diff — inside the EV-governed verbatim
  quote) + W17 rides (FR-213 by-id + verbatim-matrix pointer to
  taxation/16 **LB-013** (brief's LB-012 was a plan defect — LB-012 = Art.
  32 reception, LB-013 = CT 103 matrix), FR-145 wording, LB-017 "awareness
  only" marker, FR-372 trailing anchor map folded to
  `SV-TAX-FR-303 by id; 15_iva-declaration-interfaces.md by pointer`,
  OQ-002 pointer narrowed F-915-only at taxation/00_index:192, enum style
  verified consistent, HANDOVER rewrap) + **boilerplate sweep: 43 instances
  softened corpus-wide** (taxation 8 + non-taxation 35; spe/08:295
  file-scoped variant correctly left) + **T9 catalogs workbook-sole-source
  alignment** (overlay path removed; 33 CSVs byte-identical; shared/scripts
  README usage row updated — beyond-brief edit upheld) + **T10
  `shared/scripts/build_coverage.py`** (COVERAGE_NOTES sidecar; `--check`
  gate; 13 under-listed citing sources corrected; 3 scanner
  generalizations; catalogs/ scan included) + frep/03 OQ-007 added (the
  wave's only sanctioned row addition). In-wave finds: 01 §4 sign-header
  defect was casilla-vs-formula ambiguity (sello/firma not found);
  626-787→702-787 (CC letra-de-cambio chapter source-verified); sv/README
  count fixed 73/01-75/next-76. **S9 RIDE ledger unrecoverable** (SDD
  workspace deleted; recorded verdict was "cosmetics; nothing
  load-bearing") — no action possible. Deferred minors from C1 reviews are
  in the C1 SDD ledger copy below. Commits 70f86f9 (plan) +
  3f6f5ed..3c925ac. **Final whole-wave review: USABLE-WITH-FIXES → one
  fix wave PASS (c696025: coverage default status token `pending-S2+`
  aligned to legend; HANDOVER C1-END placeholder resolved; EXTRACTION_
  PLAN commit record) = MERGE-READY.** Deferred-minor triage: ALL RIDE
  (T1-T4/T6/T9/T10 sub-items; first-picks already in §8.5 — frep/04
  truncated source path, _INDEX corrections-log wipe-on-regen, EV-bank
  hygiene nits, payroll trailing-newline sweep). Corpus delta verified
  mechanically by the final review: +OQ-007 (frep/03) only; 1,662 FRs;
  CSVs byte-identical; coverage gate green.
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

- **S8 (2026-08-20):** chart-of-accounts synthesis COMPLETE per plan
  `docs/superpowers/plans/2026-08-19-s8-chart-of-accounts-synthesis.md`
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
  COMPLETE per plan
  `docs/superpowers/plans/2026-08-19-s7-special-regimes-synthesis.md`
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

### C1-process rulings (2026-08-21, preserved from the SDD ledger before workspace deletion)

- **(a)** T2's LB-013 substitution upheld: the plan brief said FR-213's
  verbatim-matrix pointer → taxation/16 "LB-012", but LB-012 is the
  Art. 32 reception row; LB-013 (FR-367-anchored) is the Arts. 33-34
  CT 103 matrix. Evidence-based implementer override of a plan pointer
  defect — reviewer line-verified.
- **(b)** T4's in-quote `[sic]` insertions (cml/03 LB-010, cml/06
  LB-017) ruled corpus-sanctioned editorial markers (precedents 06:362,
  09:640/700): bracketed annotation replacing out-of-band parentheticals
  of the same fact; quoted characters unchanged.
- **(c)** T9's beyond-brief edit (shared/scripts/README usage row)
  upheld: stale `--pdf` docs post-removal would be actively wrong.
- **(d)** T8's boundary case: spe/08:295 "the only split surface this
  file touches" = file-scoped verifiable claim, NOT the corpus-wide
  exclusivity boilerplate — correctly left unswept.
- **(e)** T7's 13:559 `D2` = substantive decision-id citation, not an
  only-claim — out of sweep scope. OQ-002 pointer target adapted
  05 → taxation/00_index:192 (no F-910/F-915 text exists in 05).
- **(f)** T5 count convention: 175 = defined FRs (SV-SPE-FR-001..175);
  183 = grep bullet-rows incl. index/cross-refs. Final review verified
  contiguity.
- **(g)** Verify-or-document protocol worked as designed on lost-ledger
  rides (S8 T1/T4/T6/T8, W17 wording rides): fixes landed only where
  the defect was verifiable; A1 period correctly ZERO-diff (inside the
  EV-governed verbatim quote); Art. 66 attribution + frep enum style
  verified already-conformant.

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
  again after the 500 outage since 08-18). API recipe **PINNED 2026-08-21**:
  POST `/api/v1/diarios-disponibles` form-encoded `year=YYYY&month=MM`
  (English keys only — JSON body 400s incl. `anio`/`mes`; query-string
  404s) → `[{Id, FechaInicio, FechaInexacta, NombreArchivo}]`; PDF at
  `/seleccion/{Id}` (serves `application/pdf`). asamblea.gob.sv:
  **RECOVERED 2026-08-23** (DNS A-records restored — 168.90.109.76 +
  138.255.154.12; serves 200/74KB on both apex + www, but TLS chain
  incomplete → `curl -k` REQUIRED; unblocks the COTRANS Aug-2025
  prorroga decree hunt §8.2). **W22 route intel (2026-08-23): the
  by-year pages are full-calendar-year single pages, newest-first**
  (pages 1+ return 2-4 cards or empty — pagination broken server-side,
  page 0 is complete per year; year straddling a legislature seating
  carries BOTH numbering families on its page); ALL decree PDFs carry
  the 8-byte junk prefix before `%PDF` (systemic); the document server
  serves some decrees as CONSOLIDATED REPRINTS with REFORMAS blocks
  (111_ = the pattern's first observation); NO cards exist for
  2010/2012-2015 and 2019 looks partial (73 cards) — the por-anios
  archive is NOT a complete pre-2016 census instrument; one 504-retry
  needed on the 2021 page.
  Live official mirror: **uif.gob.sv Marco Legal** (plain GET + browser
  UA; Incapsula blocks HEAD) — WAF-blocked since 2026-08-21 (403 all
  routes),   **degraded further to DNS-ABSENT since 2026-08-22** (D.O. +
  uif.gob.sv both in a DNS-level outage: hosts resolve to NO A record,
  Cloudflare DoH-verified; **still absent at the 2026-08-23 W22
  re-probe — D.O. apex now NXDOMAIN (was SOA-only no-A); recovery =
  A-record restoration on the registrar/host side; all pinned
   recipes stand unchanged; factura.gob.sv alive 200**. **W24 re-probe
   (2026-08-24): D.O. STILL unreachable (HTTP 000 — outage day 3);
   uif.gob.sv answers 403 at the HTTP layer (the Incapsula WAF block —
   no longer DNS-absent; AML reglamento watch resumes via the WAF-block
   re-probes); factura 200; asamblea 200 (`-k` route stands).** AML
   reglamento watch interrupted; the live date is **2026-10-17 = the 71_
   12-month adaptation deadline (publication 9-oct-2025 + 12 months; 71_
   effective 2025-10-17)**; re-probe at wave cadence. MH formularios
  page: direct wp-content URLs (re-verified 2026-08-22: no F-11
  v19/v20, no F14 v17 manual; **W22 2026-08-23: the
  `/formularios-e-instructivos/` path now 302s to the mh.gob.sv home —
  page moved/removed, re-pin the wp-content route at the next F-11/F14
  watch**).
- W18 route intel (2026-08-21/22): **TF DC catalog enumerable via
  Wayback CDX** (`web.archive.org/cdx/search/cdx?url=transparenciafiscal.
  gob.sv*`) → live `downloads/pdf/DC<id>_<ExactCase_Slug>.pdf` URLs
  (UPPERCASE DC serves the PDF; lowercase dc slugs 302 — recipe +
  precedent rows in sv/sources/README). **SIECA downloads gated but S3
  presigned URLs work** (POST the product page → presigned S3 link; used
  for 83_-85_). cvpcpa.gob.sv wpdm table incomplete — WP media REST API
  surfaces the unlisted PDFs (76_). jurisprudencia.gob.sv bóveda D.O.
  archive = the ZF-family negative-check route (SOQ-31).
- Title-vs-content incidents ×5 (29_, 09_, 15_, 12_, 31_-COTRANS) —
  trust content, amend registry, never trust catalog titles.
- Damaged-PDF recipes: qpdf auto-repair (17_, 74_); ghostscript pdfwrite
  rebuild for broken page trees (73_).
- Python venv `~/.venvs/localizations`; scripts
  `shared/scripts/extract_text.py` + `build_catalogs.py`.

## 7. Open-question highlights (full registers in master index + topic indexes)

- **MOQ-05** Retorno/OpEsp endpoints (externally blocked, schema-verified
  absent); **MOQ-04 FOVIAL/COTRANS — CLOSED W19** (SOQ-39 consumed by the
  T2 fold-in: law texts owned 86_-89_ — $0.20 = D.L. 597-2001 Art. 26
  reform; COTRANS = D.L. 257-2021 passenger-tariff $0.10/gal, identity
  corrected — and spe/08 SR8 provenance/identity/vigencia rows now
  instrument-anchored).
- Special-regimes W19: **SOQ-32 consumed** (LESIA anchored — INDICE print
  thru D.L. 588-2008, post-2008 watch), **SOQ-34 consumed** ($18.00
  never adjusted; the FR-176 revision watch closed as a no-change
  verdict), **SOQ-39 consumed** (MOQ-04 closed), SOQ-30 watch NARROWED
  (LSI half resolved by the 80_ re-key; ZF 82_ tail folded; residual =
  post-tail traffic), **95_ horizon TEXT-PINNED 15 años** (Art. 3 inc. 2,
  no OQ), **96_ Chapter V CONSUMED W20** — the real 30%-withholding
  surface on remittances to foreign agents now owned by `taxation/17`
  (SV-TAX-FR-405..416; spe/01 OQ-6 resolved-by-pointer; SOQ-41 96_ half
  consumed — residuals: D.L. 201-2025 + 411-2025 dated negatives, RAEX
  reglamento config-gap).
- Taxation: SOQ-02 ($1,600 proration), 03-OQ-009 straddle, Quincena-25
  double-benefit 2026 (tercerización pointer RESOLVED S9 → 11 §3.3);
  **04 OQ-003 RESOLVED W20** (2025+ standing 2-SMM rule chain-verified —
  EVID-403 + 91_-94_ anchored; the annual December re-check rides the
  encoding pass); **SOQ-40/OQ-2 (09 §3.7 D1-tributo-mapping design
  confirmation) RESOLVED W24** — instruments 86_-89_/106_ independently
  grep-verified rule-negative (no statutory DTE-chain rule; the 2001
  control-account chain = 31_-guide practice vintage); FR-244/245
  confirmed as labeled product design, config-gated; spe/08 OQ-3
  resolved-by-pointer; re-validation trigger = any future MH/DGII chain
  rule;
  IVA-side: SOQ-54 **FULLY RESOLVED** (Ley W16 DC9226; **Rgto W18
  RESOLVED-AS-PARITY** — DC5855 text-identical to 02_; 01_/02_ both
  current consolidations; cadence watch only), SOQ-55/57 carried in
  07/08, **SOQ-56 RESOLVED W18** (Art. 46-f = 101_-105_; exemption flag
  = BCR-list membership), SOQ-58 negative-refreshed W18 (167-A
  kill-switch instrument not yet issued — watch).
- Fiscal-reporting: SOQ-08 (due-day windows — **anchor consumed W17**:
  the statutory 10-hábiles layer is anchored by 75_ Art. 100 (frep/08
  LB-006, EVID-351); the by-NIT-digit window assignment remains dated
  config, still open), SOQ-13/14;
  07 OQ-008 (v17
  apéndice code 73), 06 OQ-008 (MH validation depth); 02 OQ-002 rate
  anchor ANSWERED S9 (SV-TAX-FR-240/241), 03 OQ-004 ANSWERED S9
  (SV-TAX-FR-313 zone).
- Commercial-legal: **SOQ-23 SAS statute FULLY CLOSED W23** (sources
  W22: D.L. 905-2023 = 111_ CC reform, Capítulo VIII-Bis 305-A..Z +
  Art. 18-II-c; fold-in EXECUTED W23: FR-044 in_corpus + FR-225..240 +
  FR-246 + LB-032 retired, OQ-001 resolved; gratuidad chain 113_/114_ →
  31-dic-2026; SAS = "el tipo societario de mayor uso" per 114_ cons.
  III); **SOQ-22 FALSIFIED-AND-RE-SWEPT W22/W23** (the post-2008 CC
  reform set 109_-114_ owned + folded: 04 Arts. 17/18/134/155
  re-anchored, 05 Arts. 315-319/337/338/358 re-anchored, 08 Art. 960 +
  838-A..E awareness; the six no-overlap files' verification notes
  flipped; residual = the asamblea census negative watch only — no
  cards for 2010/2012-2015, 2019 partial); SOQ-24 quiebra vintage,
  SOQ-25 Ley
  Registro de Comercio, SOQ-26 Economía rate; 05 OQ-002 reshaped-open
  (Ley de Competencia values still config-gap; checkpoint now
  notary/suscriptor comprobar-or-declarar per the new Art. 319); 08
  OQ-004 narrowed-open (truncation evidenced; BCR norms/interbank
  rules un-acquired); **SOQ-46 PARTIAL W18** —
  NIIF authority chain acquired 76_-78_ (CVPCPA Res. 154-2024 current +
  Res. 462-2021 adoption + Ley Reguladora D.L. 828/646), both frameworks
  SV-ratified, but the PYMES-vs-full criteria instrument is still
  unfound (hunt open; candidates Res. 175-2023 [derogated intermediate] /
  Res. 82-2024, low value per SOQ-52 boundary); AML new-reglamento watch
  (uif.gob.sv — WAF-blocked since 2026-08-21, re-probe pending;
  2026-10-17 deadline).
- F-11 v19/v20 + F14 v17 manual acquisitions (MH page watch; numbering
  now ≥115). **SOQ-41 CLOSED W18** (90_-97_ acquired; D.L. 201-2025 +
  411-2025 dated negatives) — W19: the 96_ transitory limb
  dispositioned via the Chapter V pointer, **CONSUMED W20 by
  taxation/17 (SV-TAX-FR-405..416) — W22: the two dated negatives OWNED
  as 107_/108_ (EVID-405/406; D.O. anchors stamped on face); **W24: the
  107_/108_ FR fold-ins EXECUTED (SV-SPE-FR-204 + SV-TAX-FR-417..421) —
  SOQ-41 residual = the RAEX reglamento config-gap (96_) ONLY; the
  EVID-167 10-instrument named set fully dispositioned** · **SOQ-34
  RESOLVED W18 + consumed W19** ($18.00 never adjusted — 98_/99_ DACG
  prints; 74_ Art. 12-B tail owned as 100_; spe/06 LB-022 chain
  anchored).
- Ley IVA consolidation: **RESOLVED W16** (TF DC9226 second official
  print, reform list identical through (14) D.L. 71-2015 → 01_ current;
  registry §75-section note). Reglamento IVA: **RESOLVED-AS-PARITY W18**
  (TF DC5855 text-identical to 02_, ratio 1.0; transparencia.mh.gob.sv
  links the same DC5855 → two-institution parity; no post-117-2001
  consolidated print exists — SOQ-54 Rgto side closed).

## 8. Next actions (ordered)

  1. **Fold-in edit waves: ALL EXECUTED (program item CLOSED W24).**
       ~~(a) cml edit wave~~ COMPLETE W23; ~~(b) spe/taxation wave~~
       **COMPLETE W24 (2026-08-24)** — 107_/108_ folded (spe FR-204 +
       taxation FR-417..421; corpus 1,730; COVERAGE 90/9/2/12 gate
       green; see §1/§5); ~~(c) SOQ-40/OQ-2 ride~~ RESOLVED W24. The
       8-topic program + W17 + C1 + W18-W24 are
       COMPLETE (W20/W21/W22/W23 MERGED; W24 push/merge per item 6).
       Remaining, owner's call: residual acquisitions (item 2) + external
       watches (D.O. down since 2026-08-22, uif 403-WAF — §6) + EV-bank
       hygiene queue + the W23 cml deferred-minor rides + the W24
       spe/taxation deferred minors (window_kind token split + three
       cosmetics — §5 wave log) +
       go-live/implementation prep per
       `shared/docs/go-live-readiness.md`.
  2. **Acquisition follow-ups (residual after W22):** SOQ-46 criteria
      instrument (candidates Res. 175-2023 [derogated intermediate] /
      Res. 82-2024 — low value per SOQ-52 boundary); SOQ-31 D.O.
      Oct-Dic-1998 micro-scan (optional — never-issued negative
      hypothesis stands); F-11 v19/v20 + F14 v17 manual MH-page watches
      (re-pin the wp-content route — the formularios path 302s to home
      since 2026-08-23); ~~COTRANS Aug-2025 prorroga~~ RESOLVED W21
      (106_; 617/1000/307 texts optional at the D.O. recovery watch);
      ~~SAS statute hunt~~ **RESOLVED W22 (D.L. 905-2023 = 111_ + the
      gratuidad chain 113_/114_)**; ~~D.L. 201-2025 + 411-2025 anchors~~
      **RESOLVED W22 (107_/108_, D.O. stamps on face)**; uif.gob.sv
      re-probe (AML reglamento watch — 2026-10-17 adaptation deadline;
      DNS-level outage since 2026-08-22); optional D.O. original prints
      of 106_-114_ when D.O. recovers; asamblea por-anios residual
      census (2010/2012-2015 no cards, 2019 partial — the SOQ-22
      negative watch).
   3. Registry note: numbering continues from **115** (W22 registered
       107_-114_; sv/sources/README is the count of record — **112 file
       rows** = 110 plain numbers + 17b + 25_×2 [W24 correction; the
       "111" prose forgot 17b], gaps 21/23/24/28).
 4. SOQ follow-ups per §7; periodic external checks (factura.gob.sv,
    uif.gob.sv/marco-legal, MH formularios, D.O. recovery).
  5. Deferred cleanups (CAN-STAND): **RESOLVED by C1 (2026-08-21)** — root
     HANDOVER §9 items annotated per-item; S7 AC-007 fixed, S8 rides fixed
     (T6), S9 RIDE ledger unrecoverable (workspace deleted; recorded
     verdict "cosmetics; nothing load-bearing"); boilerplate swept (43
     instances); COVERAGE regen script shipped. Residual deferred minors
     from C1 per-task reviews (all Minor, non-blocking) live in the C1
     wave-log entry / EXTRACTION_PLAN record; first-picks: frep/04
     truncated source path `63_F930v3.pdf` latent fix, catalogs _INDEX
     corrections-log wipe-on-regen, EV-bank hygiene nits (A1 estas/esas,
     01 LB-004 PAGE 46-53 vs 48-53), payroll 05/08 trailing-newline
     inconsistency sweep.
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
- Registry additions continue numbering from the current tail (115
  after W22); page-1 verify everything; record provenance +
  supersession.
- Synthesis waves: prep (master-index clusters + SOQs) → plan doc in
  `docs/superpowers/plans/` → subagent loop (fresh implementer per task;
  every FR cites LB; reviewer verifies vs master index; fix rounds;
  ledger) → final whole-wave review → ONE fix wave → push.
