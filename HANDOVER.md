# HANDOVER — Session State & Continuation Guide

**For the next controller session.** Written 2026-08-17, updated 2026-08-18 (S3 close),
2026-08-18 twice more (W9/S4 closes), 2026-08-18 twice more again (W10+S5 prep, then W11 Quincena-25 package),
2026-08-18 once more (S6 Quincena-25 fold-in close), and 2026-08-18 twice more
(W12 AML-regime replacement + S5 commercial-legal synthesis close). Read this
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

## 3. Current state (2026-08-19)

### Git / repo
- Branch `main` only; remote `origin` = `git@github-CtrlCarlitos:CtrlCarlitos/odoo-localizations.git` (SSH alias `github-CtrlCarlitos` from `~/.ssh/config`); push after each wave; never force-push. `gh` CLI at `~/.local/bin/gh`, authenticated as CtrlCarlitos.
- Commits are SSH-signed; local `%G?=N` is a verification-only artifact (`gpg.ssh.allowedSignersFile` unset) — signatures ARE present; don't chase it.
- `.gitattributes`: `*.csv text eol=lf`.
- Commits through `cc7a307` (2026-08-19 6th session: D15 as-of doctrine;
  before that `3929470` GT/HN worktree note and the W12+S5 close `260d039`/
  `9bb37e9` per §3).

### El Salvador — sources & evidence state
- **EVID corpus 001..274** (gaps 109-127, 240 reserved-unused). W13 files (2026-08-19):
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

### GT / HN — SEPARATE WORKTREES (do not work them here)

**GT and HN run in dedicated git worktrees/branches, NOT in this main
workspace** (2026-08-18 note):

- `git worktree list` shows: `.worktrees/gt-research` (branch `gt-research`)
  and `.worktrees/hn-research` (branch `hn-research`).
- Each worktree keeps its OWN wave logs/registers/HANDOVER state — their
  in-progress status is NOT tracked in this file. Before any GT/HN work (or
  merge decisions), read their state with:
  `git log --oneline main..gt-research` / `main..hn-research` plus the files
  in the worktree (their own HANDOVER sections/logs).
- As of 2026-08-18 both are FAR past scaffolding: gt-research ≈ W1-W5
  complete (source acquisition engine: 36+ sources across payroll/fiscal
  reporting/COA/special regimes; DCA/Wayback/SAT-portal queue discipline);
  hn-research ≈ W1e (EVID-056+; Código Tributario + D.17-2010 family +
  ISR tabla vintages evidence passes).
- This main workspace stays sv-focused: no GT/HN edits land on `main` from
  here. Worktree branches sync/merge to `main` by explicit decision when
  their waves close (rebase-then-merge; never force-push).
- Original scope note stands: GT gets FEL (SAT), HN fiscal reporting only
  (no e-invoicing).

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


- Evidence-based answers only; RAG (NotebookLM) is validator, never source
  (notebook `c7ca0391-4822-4d3c-8090-b0d8c147ba94`, owner
  c20260202@gmail.com; MCP: github.com/jacob-bd/gemini-notebook-mcp-cli).
- Hint layer = tuky-workspace repo (github.com:CtrlCarlitos/tuky-workspace,
  `projects/odoo-localization-el-salvador`) — pointers only, never LB.
- Takumi builds thin clients only (D2); SaaS is Elixir, separate codebase.

## 6. Environment & tooling (this machine)

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
      subagent wave).**
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
10. **GT/HN bootstrap** when sv is sufficiently far along (GT sources first:
    SAT/FEL normative; HN: SAR fiscal reporting).

## 9. Deliberately deferred (CAN-STAND list)

- `catalogs/README.md` + `_INDEX.md` still say "PDF overlay"; and
  `build_catalogs.py` keeps a `--pdf` overlay path — contradicts SV-CAT
  FR-002 (workbook = sole parse source). Align at next sidecar regeneration.
- T3 wording: 03_events FR-094 5-day anchor — RESOLVED 2026-08-17 (raw 45_
  p.123 quote folded into FR-094 with the anchor-noun ambiguity note);
  UUID "uppercase hexadecimal digits" tightening (M-1) still open.
- 06_api-protocol OQ-005 is resolved-but-noisy (used as work-log) — fold
  into next 06 edit.
- 02_transmission AC-011 over-broad ("no *.dtes.mh.gob.sv reference" vs
  legitimate portal URLs) — scope to API code paths.
- FR-136 renewal-staging wording fixed (final review), but 04 OQ-006
  (renewal procedure) remains open legitimately.
- sv/README count phrasing nit (50 = 48 used numbers + 17/17b pair + 25_
  pdf/xlsx pair).
- D4 email-escalation channel ownership → ToS/onboarding backlog (not a
  requirements file yet).
- COVERAGE regeneration script (currently hand-built matrix).
- **"Only architecture-split surface" boilerplate** exists in ~11 requirements files
  across waves (S3 final-fix found 01's instance; 02:467 + taxation files untouched) —
  one sweep to soften all instances.
- S3 deferred minors (final review, deferrable): 01 FR-005 missing EVID-178 cite; 01
  FR-023 else-branch phrasing; 01 §4 sign-header wording; 01 Art. 66 attribution
  looseness; 02 FR-064 compressed inventory; 02 §5 FR-048 row missing P-formula pointer;
  03 AC-005 code-8 parity un-OQ'd; 03 FR-071 could name EVID-174; 03 FR-092 glosses 01's
  upload rules; 04/06 Given/then style; 06 FR-162 antecedent + FR-168 FR-106 gloss; 08
  LB-005 gloss restates consumer values (verified correct);   index §7 pointer wording;
    taxation 05-OQ-002 pointer's "F-910/F-915" phrasing (F-910 marginally irrelevant there).
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
- S5 deferred minors (final review "can-ride", deferrable): 09:75 id
  SV-CML-FR-162 line-wrapped mid-id (grep-artifact source); 03 page-pointer
  over-broads + §2 abbreviation overlap; 04 Art. 121 final-sentence marker +
  Art. 149 parenthetical skip; 06 EOF blanks; 08 inner-quote normalizations
  ×5 + "626-787" over-bread; 10 FR-209 paren scar; index 07-scope labels;
  marker-vocabulary variance across files; T1-M3 A11 cluster-pointer
  normalization when A11 lands.

## 10. Session-protocol checklist for the next controller

1. Read §1–§8 of this file; read the documents in §2 in order.
2. Confirm state: `git log --oneline -20`, `git status` (expect clean),
   `ls sv/requirements/e-invoicing/` and `ls sv/requirements/commercial-legal/`
   (10 files + index).
3. Follow skills (brainstorming gate for new design work; SDD for plan
   execution; systematic-debugging for any investigation).
4. Before ANY source citation: check authority order (§3) and COVERAGE.md.
5. At session end: update THIS file (state, rulings, next actions), commit,
   push. Copy any SDD-ledger rulings here BEFORE deleting the workspace.
