# HANDOVER — Session State & Continuation Guide

**For the next controller session.** Written 2026-08-17 at the close of the
S1 synthesis wave. Read this document fully before acting; it is the
authoritative cross-session memory (conversation context does not survive).
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
5. `shared/docs/regulatory-change-management.md` — version-regime framing; **Q1–Q7 socratic session still pending**
6. `shared/docs/odoo-localization-guide.md` — module anatomy (with thin-client caveat)
7. `sv/.extractions/00_MASTER_INDEX.md` — synthesis lookup: 12 topic clusters (A1–A12), 16 resolved contradictions (R1–R16), 12 MOQs
8. `sv/requirements/e-invoicing/00_index.md` + `sv/requirements/COVERAGE.md` — S1 corpus index + source coverage matrix (authoritative for source→wave mapping)
9. `HANDOVER.md` (this file)

## 3. Current state (2026-08-17)

### Git / repo
- Branch `main` only; remote `origin` = `git@github-CtrlCarlitos:CtrlCarlitos/odoo-localizations.git` (SSH alias `github-CtrlCarlitos` from `~/.ssh/config`); push after each wave; never force-push. `gh` CLI at `~/.local/bin/gh`, authenticated as CtrlCarlitos.
- Commits are SSH-signed; local `%G?=N` is a verification-only artifact (`gpg.ssh.allowedSignersFile` unset) — signatures ARE present; don't chase it.
- `.gitattributes`: `*.csv text eol=lf`.
- Last S1 commit: `72e06b0`; evidence tracking added `58b8b81`.

### El Salvador — extraction (COMPLETE for S1 scope)
- **87 EVID entries** across 7 evidence files + the 45_Anexos digest, all
  committed under `sv/.extractions/` (`.evidence.md`, `00_MASTER_INDEX.md`,
  `45_Anexos.digest.md` are tracked; `.txt` dumps + `schemas_2026/` remain
  ignored — regenerable via `shared/scripts/extract_text.py` and the 52_ zip).
- Waves done: W1 foundations (11 DTE structures + events manual), W2 catalogs
  sidecars, W3 Ley IVA + Reglamento, W4 Código Tributario, W5 DTE stack, W5.5
  2026-regulatory-update re-read. Sources refreshed mid-project: files 44–52
  fetched from factura.gob.sv (D.L. 487 CT reform, Normativa v2.0 25-May-2026,
  Manual Tecnológico v2.0, catalogs v1.1 2026 re-versioning, JSON schemas
  2026-08-11). **Authority order: 44_/45_/46_/50_/51_/52_ (2026) > 18_/19_/22_
  (2025) > 40_/41_/25_ (2022).** Superseded sources retained as historical LB.
- 50 source files (numbering 01–52; gaps 21/23/24/28 unused; next file = 53)
  + superseded 2022 `schemas/` dir + current 15 schemas inside the 52_ zip.

### El Salvador — synthesis S1 (COMPLETE, pushed)
Six Takumi files + index + coverage, **216 FRs / 70 LBs / 93 ACs / 42 OQs
(39 open, 3 resolved)**:

| File | FRs | Prefix range |
|---|---|---|
| `sv/requirements/e-invoicing/01_document-types.md` | 52 | SV-EINV-FR-001..052 |
| `sv/requirements/e-invoicing/02_transmission.md` | 34 | SV-EINV-FR-053..086 |
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

### GT / HN
Scaffolded only (READMEs, sources/scripts/requirements dirs, topic sets; hn
has no e-invoicing). No sources collected yet. GT gets FEL (SAT), HN fiscal
reporting only. Extractions begin after sv S2 or in parallel by decision.

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

### Standing policies
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
- **Fetching from factura.gob.sv**: wpdmdl download-manager LABELS DO NOT
  MATCH CONTENT (IDs were shuffled). Always verify by reading page 1 with
  pypdf. Known IDs as of 2026-08-16: 4388=Manual Tecnológico v2.0,
  4728=Normativa v2.0, 4725=catalogs XLSX-as-pdf, 5353=catalogs XLSX,
  4399=schemas zip, 4726=Manual Funcional, 4397=eventos manual,
  4398=estructuras manual v1.6 (237pp). Re-verify before reuse.

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

## 8. Next actions (ordered)

1. **DTE schema pass** (highest value, in-repo evidence): close the
   schema-verifiable OQs by reading `sv/sources/52_Json_Schemas_DTE_...zip`
   (extract to scratch) against the OQ sections of the S1 files. Final
   review flagged: 01 OQ-002/003/004/005/008, 02 OQ-003, 03 OQ-003/005 —
   confirm each against in-file OQ tables before resolving; record
   resolutions in-file AND in `00_MASTER_INDEX.md` Section C.
2. **Regulatory-change socratic session** (Q1–Q7 in
   regulatory-change-management.md) — BEFORE S2 Odoo Mappings; S2 (taxes/
   reporting) hits recomputation/version issues hardest (Q5). Some
   complexity already resolved by D2 (central SaaS spec upgrades).
3. **S2 waves** (each: extraction → evidence → synthesis, same patterns;
   source mapping authoritative in COVERAGE.md): ISR (03_/04_/10_) →
   F-07/F-14 reporting (29_/30_/34_–39_) → payroll (08_/09_/11_/16_) →
   commercial-legal (07_/15_/17_) → special-regimes (12_/13_/14_/17b_/42_/
   43_) → NIIF/chart-of-accounts (32_/33_). F-14 manual (35_) is OCR'd.
4. **Externally-blocked OQs** (check factura.gob.sv periodically): Retorno/
   OpEsp endpoints (MOQ-05; 03 OQ-006, 02 OQ-005-adjacent); CAT-024 vs
   Cuadro-2 taxonomy confirmation. When new docs appear: continue source
   numbering from 53, register with provenance, capture supersession.
5. **Deferred cleanups** (§9 below, batch them).
6. **GT/HN bootstrap** when sv is sufficiently far along (GT sources first:
  SAT/FEL normative; HN: SAR fiscal reporting).

## 9. Deliberately deferred (CAN-STAND list)

- `catalogs/README.md` + `_INDEX.md` still say "PDF overlay"; and
  `build_catalogs.py` keeps a `--pdf` overlay path — contradicts SV-CAT
  FR-002 (workbook = sole parse source). Align at next sidecar regeneration.
- T3 wording: 03_events FR-094 5-day anchor (generation vs transmission —
  add verify note to 03 OQ-002); UUID "uppercase hexadecimal digits"
  tightening (M-1).
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

## 10. Session-protocol checklist for the next controller

1. Read §1–§8 of this file; read the documents in §2 in order.
2. Confirm state: `git log --oneline -20`, `git status` (expect clean),
   `ls sv/requirements/e-invoicing/`.
3. Follow skills (brainstorming gate for new design work; SDD for plan
   execution; systematic-debugging for any investigation).
4. Before ANY source citation: check authority order (§3) and COVERAGE.md.
5. At session end: update THIS file (state, rulings, next actions), commit,
   push. Copy any SDD-ledger rulings here BEFORE deleting the workspace.
