# gt/HANDOVER — Guatemala Session State & Continuation Guide

**For the next controller session.** Written 2026-08-19 at close of the GT
source-research sessions (W1–W5 + owner DCA batches); updated 2026-08-19
(convergence-audit session: shared-rules D16 reconciliation +
EXTRACTION_PLAN draft). Read this fully before
acting; it is the authoritative cross-session memory. **Update it at every
session boundary.**

Session bootstrap command: `Read gt/HANDOVER.md and continue.`

## 1. What this work is

GT requirements-extraction for the Odoo localization, per
`shared/docs/requirements-extraction-procedure.md` (method spine) and the SV
corpus as precedent. Currently in **Stage 0→1 transition**: source research
is COMPLETE (corpus assembled); extraction/evidence/synthesis waves are next.
Product architecture context: root `HANDOVER.md` §1 (SaaS thin-client + Odoo;
Takumi consumes requirements).

## 2. Read order for a new session

1. This file
2. `docs/superpowers/specs/2026-08-18-gt-source-research-design.md` —
   decisions D-GT1..D-GT10 (scope, policies, FEL provider model, journal/
   document-type design, dated-instrument regime)
3. `gt/SOURCE_RESEARCH.md` — research record: wave log, candidates, verdicts,
   OQ register (OQ1–OQ17 with statuses), acquisition log
4. `gt/sources/README.md` — the registry (provenance + re-verify flags)
5. `gt/DOWNLOAD_QUEUE.md` — remaining owner-browser items (rev 5; most closed
   by the 2026-08-19 batch)
6. Root `HANDOVER.md` §GT (cross-session) + `shared/docs/` method docs

## 3. Repo/session mechanics

- **Branch `gt-research`, worktree `.worktrees/gt-research`** (same convention
  as HN; `.worktrees/` git-ignored via main commit f6f5415). Main is being
  actively committed by the SV session — never work outside the worktree;
  merge `gt-research` → `main` at milestone by owner decision.
- Commit style: short imperative, no emojis; commit per batch (precedent in
  `git log gt-research`).
- **`.gitattributes` carries `gt/sources/** -text`** — global
  `core.autocrlf=input` must never normalize source bytes (incident fixed
  2026-08-18: 24 blobs were silently CRLF-normalized; re-committed pristine).
  HN worktree should adopt the same line at merge time.
- Python: `~/.venvs/localizations/bin/python` (shared, absolute path — works
  from the worktree). Scripts in `shared/scripts/` (extract_text.py etc.).

## 4. Corpus state (2026-08-19)

**82 registered entries** (`gt/sources/`, numbering 01–83; gap 27 unused):
FEL e-invoicing stack (acuerdos 13-2018/26-2019/15-2020, incorporation
resolutions SAT-DSI 04_–14_, Reglas y validaciones **v1.7.10 Feb-2025**, Doc.
Técnico Servicios, 26 XSDs + 3 JSON catalogs × 2 channels (29_ GitHub pinned
961133c; 30_ cat.desa), manuals, casos-de-prueba 2018, contingencia 2018);
taxation core (IVA 27-92 **pre-FEL vintage — OQ10**, Reglamento IVA AG
5-2013, Código Tributario 6-91, LAT 10-2012 + AG 213-2013, **D-10-2025 IVA
reform — derogates Art. 3-"A"**, D-20-2006 + AG 425-2006 retenciones basis);
payroll (Código de Trabajo D-1441, IGSS set incl. Res. 08-SGF/2026, IRTRA
D-15-1928, INTECAP **D-17-72**, aguinaldo D-42-92, bono 14 D-78-89, salario
AG 250-2020 + **AG 256-2025 (2026 rates)** + Historia); fiscal reporting
(form inventory snapshot 2025-10-06, retenciones Web pages+manuals, LET
manuals ×3, agentes roster 2025-10, criterios 6-2018/2-2019, SAT-2390 set);
COA anchor (Código de Comercio D-2-70, 301pp); special regimes (ZF D-65-89
chain **D-65-89 → D-19-2016 → D-6-2021**, maquila D-29-89 set, ZOLIC AG
65-2022); commercial-legal (AML **D-67-2001 + D-51-2001 + D-15-2026 Ley
Integral (17-jun-2026)**, RM edictos + aranceles).

**Known-stale instruments retained deliberately** (supersession discipline):
23_ (IVA pre-FEL), 68_ (ZF reglamento pre-check), 75_ (AML, likely
superseded by 77_ D-15-2026 — derogation inventory pending), 17_/19_ (2018
vintage FEL docs). Reform chains are recorded in SOURCE_RESEARCH.md.

## 5. GT facts a new session must know

- **FEL model**: SAT owns XML standard + validates; taxpayers integrate via
  **certificadores de DTE** (18 authorized; NOT "instaladores"). **TotalDoc =
  GRUPO CDS S.A., NIT 107902281**, authorized 02/12/2021 → **02/12/2026
  (OQ7 renewal watch)**. Product default provider = TotalDoc (D-GT5/D-GT6);
  public docs only so far; partner-access list in SOURCE_RESEARCH W1-C.
- **No "Anexo técnico" exists** — equivalents: Reglas y validaciones +
  Documento Técnico Servicios + XSDs + JSON catalogs.
- **Schema drift (OQ3, material)**: cat.desa vs GitHub differ in 8/17 shared
  files; GitHub main = "versión 2" actively maintained. Ask TotalDoc/SAT
  which set production validates against.
- **ISR today = LAT D-10-2012** (26-92 superseded). **ISR anual = SAT-1371**
  ("2236" = legacy, rejected). **IVA retenciones = D-20-2006 + AG 425-2006**
  ("resolución 2-2010" = rejected myth).
- **FEL legal chain**: AD 13-2018 → 26-2019 → 15-2020 + SAT-DSI incorporations
  243-2019…400-2023 (04_–14_). Ley IVA Art. 29-"A" is the law-level hook
  (cited by AD 15-2020) — post-2018 consolidated IVA still missing (OQ10,
  now joined by OQ17: which decree added Art. 3-"A" that D-10-2025
  derogated).
- **D-GT8/D-GT9/D-GT10 bind synthesis**: `l10n_latam_invoice_document`
  (one journal, multi document types — now also shared default **D17** in
  `shared/docs/odoo-localization-guide.md`; D-GT8 = its GT instantiation);
  sucursales/warehouses/cash-registers → FEL establishment/dispositivo codes;
  **dated-instrument regime** — D-GT10 instantiates **shared D16**
  (`shared/docs/regulatory-change-management.md`): dated rule rows
  (valid_from/to + provenance; changes add rows), fecha-emisión rule
  selection, no past-dated transmission (certification timestamp;
  historical = non-transmittable accounting class), retro payroll with
  original-period rates, freeze-at-filing, backdating UX. **Naming note
  (2026-08-19 merge session): GT's "shared D13" proposal was renumbered
  D16** (D13/D14 = SV journal/establishment instantiations of D17); D16 was
  reconciled with D15 (as-of doctrine) and amended with HN's D-H2/D-H3
  (hard no-override emission block outside authorization-range vigencia;
  ingestion reconciliation against filed declarations). Cite D15+D16
  together; D18/D19 + `shared/docs/go-live-readiness.md` also bind
  synthesis (GT register already seeded there).

## 6. Access realities & gotchas (verified)

- `portal.sat.gob.gt`/`www.sat.gob.gt` = **Cloudflare 403 to ALL non-browser
  clients** (browser-UA curl too). Acquisition: owner browser downloads
  (ruling OQ2) or Wayback-of-official-URL with provenance + re-verify flags
  (follow-up ruling). Wayback quirks: rate-limits after bursts (sequential +
  sleep); some `id_` captures truncate at exact 1/5 MiB boundaries — try
  alternate captures (65_ fixed via 2022 capture; 66_ via 2024-06-12).
- **SAT label ≠ content**: id 17662 "639-2020" serves a 639-**2011** PDF; id
  57855 "1240-2021" serves a 1218-duplicate post-2023 (real 1240 = digest-
  verified 2022 captures, 12_). wpfd re-ids/re-categories files (manuals
  6524→15747; LAT →78389). **Verify every download by reading it.**
- `legal.dca.gob.gt` search = JS app — owner's browser works well there
  (19 docs found 2026-08-19); CDX `filter=` regex must be lowercase.
- igssgt.org / irtra.org.gt (needs browser UA + referer) / intecap.edu.gt /
  mineco.gob.gt (`mineco.gob.gt`, not mineconomia) fetch directly.
  mintrabajo 403 (use Wayback; site rebuilt ~2024 — check capture mimetypes).
  congreso + registromercantil unusable (empty/maintenance).
- Non-official leads (never registrable): atlas.com.gt calendario
  (back-years; cross-check only), corporacionbi.com calendario,
  diamantecontador forum, capacitacionessat.page Google Sites (SAT-branded,
  non-gov domain — ratify before use).
- OCR: DCA gazette prints need `--psm 6`; **table pages need PSM 4 at
  300–400dpi** (SV D.O. lesson carries over). Several corpus PDFs are scans
  (02/03, 33–35, 38, 64–65, 71, 73, 74, 76–77, 81, 83) — Stage 1 extraction
  must OCR-verify page 1 identity before reading.

## 7. Open questions register (live ones; full list in SOURCE_RESEARCH.md)

- **OQ3** schema drift cat.desa vs GitHub → ask TotalDoc/SAT.
- **OQ10/OQ17** post-2018 consolidated Ley IVA 27-92 (Art. 29-"A"); which
  decree added Art. 3-"A"; D-10-2025 full inventory.
- **OQ11** IGSS cuota split (12.67/4.83 priors) — inside 35_/36_ (evidence
  pass resolves; accountant can confirm).
- **OQ12** IRTRA cuota brackets — inside 42_/43_/44_.
- **OQ13** IVA-retention % + ISR retention rates — inside 78_/79_/26_/28_.
- **OQ14** D-15-2026 derogation inventory; AML reglamento status; Q2,000
  threshold wording.
- **OQ15** ZF reglamento (AG 242-90) current-reform status.
- **OQ16** does a numbered Reglamento del Código de Comercio exist?

## 8. Accountant track (asked 2026-08-19; assume yes, plan B ready)

Asks: (1) current consolidated Ley IVA 27-92 print (≥2018 reforms, ideally
through D-10-2025); (2) calendario perpetuo vencimiento windows per NIT
last-digit (monthly/quarterly/annual); (3) D-15-2026 AML reglamento status +
what happens to AG 75-2006 / Q2,000 cash-documentation rule.

**Plan B (no accountant)**: proceed with corpus-as-is using the SV
gaps discipline — record missing values as OQs with instrument-provenance
notes, never guess (SV precedent: F-14 SS caps shipped as dated data with
instrument-OQs); keep owner-driven DCA browser hunts (they outperformed
every automated route); calendar windows → transcribe from SAT's JSF app in
owner browser with atlas.com.gt as cross-check only; OQ3/dated data →
surface to TotalDoc when partner access opens (W6). Requirements can be
synthesized with these as flagged open questions and back-filled later.

## 9. Next actions (ordered)

1. ~~Draft `gt/EXTRACTION_PLAN.md` (Stage 0)~~ **DRAFTED 2026-08-19
   (convergence session) — awaiting owner review**; adjust wave
   decomposition/reading order per review before W-GT1 starts.
2. Opportunistic gap closure: queue rev-5 leftovers (instructivos cat
   15812, calendario transcription via SAT JSF app); **D-19-2016 (Ley
   Emergente ZF — the missing middle link of D-65-89 → D-19-2016 →
   D-6-2021)** flagged as an acquisition candidate in the plan's gap set;
   accountant answers fold in when they arrive.
3. **W-GT1 evidence pass** (FEL stack: 15_ Reglas v1.7.10 → 29_/30_ XSDs →
   16_ Doc Técnico Servicios → 01_–03_ acuerdos → 04_–14_ resolutions →
   manuals 18_–22_ + 17_ casos + 31_ registry) per the procedure's Stage 2;
   evidence to `gt/.extractions/` (gitignore already excludes; commit
   exceptions only if owner rules so, SV-style).
4. Milestone: owner decides `gt-research` → `main` merge (EXTRACTION_PLAN
   now exists; owner also owns the pending merge of this branch's
   convergence commits).
5. W6 partner follow-up when TotalDoc access exists (API manuals, sandbox,
   OQ3 question). **OQ7 watch: TotalDoc/Grupo CDS authorization expires
   02/12/2026 — re-check the certificador registry at next milestone.**

## 10. Owner notes (2026-08-19, session close; updated same day by the
convergence session)

- **Owner will handle the `gt-research` → `main` merge personally** — next
  controller does NOT merge; verify branch state only.
- ~~NEXT SESSION PRIORITY: uniform shared rules for all 3 countries
  (SV/GT/HN)~~ **EXECUTED on main 2026-08-19** by the merge/unification
  session (commits `5eb6d6b..53edd55`, root HANDOVER rulings 43–48): GT's
  "shared D13" became the **D16 canon** (renumbered; reconciled with D15;
  HN D-H2/D-H3 amended in); D15 universalized with country instantiation
  registers; **D17** = `l10n_latam_invoice_document` cross-country default
  (D-GT8 = GT instantiation); **D18** (mid-year go-live ingestion) and
  **D19** (cut-over mechanics) added; `shared/docs/go-live-readiness.md`
  created with SV/GT/HN registers. **Residue closed by the 2026-08-19 GT
  convergence session** (this branch): D7–D12 country-scope note added to
  `shared/docs/regulatory-change-management.md` (SV nouns = illustrations,
  mechanics binding cross-country); GT spec D-GT10 row now cites D16; this
  HANDOVER de-staled. Remaining convergence surface for future sessions:
  keep country instantiations current at each synthesis close
  (go-live-readiness registers + D15/D16 registers), and converge any
  variant texts the SV/HN sessions write in parallel via root HANDOVER.md.
