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
5. `shared/docs/regulatory-change-management.md` — version-regime framing + **D7–D12 decision log (decided 2026-08-17)**
6. `shared/docs/odoo-localization-guide.md` — module anatomy (with thin-client caveat)
7. `sv/.extractions/00_MASTER_INDEX.md` — synthesis lookup: 12 topic clusters (A1–A12), 16 resolved contradictions (R1–R16), 12 MOQs
8. `sv/requirements/e-invoicing/00_index.md` + `sv/requirements/COVERAGE.md` — S1 corpus index + source coverage matrix (authoritative for source→wave mapping)
9. `HANDOVER.md` (this file)

## 3. Current state (2026-08-17)

### Git / repo
- Branch `main` only; remote `origin` = `git@github-CtrlCarlitos:CtrlCarlitos/odoo-localizations.git` (SSH alias `github-CtrlCarlitos` from `~/.ssh/config`); push after each wave; never force-push. `gh` CLI at `~/.local/bin/gh`, authenticated as CtrlCarlitos.
- Commits are SSH-signed; local `%G?=N` is a verification-only artifact (`gpg.ssh.allowedSignersFile` unset) — signatures ARE present; don't chase it.
- `.gitattributes`: `*.csv text eol=lf`.
- Commits through `81c0bd6` (2026-08-17 session: W6.5 acquisition `a26f4b6`,
  W7 evidence `8a1599e`, W7 addendum `81c0bd6`).

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
- **Diario Oficial volumes (recipe, verified 2026-08-17)**:
  `POST https://www.diariooficial.gob.sv/api/v1/diarios-disponibles`
  (form data `year`, `month`) → JSON rows with `Id`/`NombreArchivo` →
  `https://www.diariooficial.gob.sv/seleccion/{Id}` serves the full volume
  PDF (opens with EMPTY password in pypdf). Online copies are watermarked
  "SOLO PARA CONSULTA — NO TIENE VALIDEZ LEGAL" (fine for extraction).
  D.O. scans OCR only under tesseract PSM 6 (same quirk as 44_).
- **Asamblea consolidations**: asamblea.gob.sv was network-unreachable
  2026-08-17; the official-mirror route that worked is the DGA (Aduanas)
  WordPress download-manager: fetch the `/download/<slug>/` page, parse the
  embedded `?wpdmdl=<id>` href, download that (plain URL of the file 404s —
  the degree-sign `°` in filenames gets mangled).

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

1. ~~**DTE schema pass**~~ **DONE 2026-08-17** — 10 OQs + 4 MOQs closed;
   rulings 5–10 above; resolutions recorded in-file and in master-index
   Section C.
2. ~~**Regulatory-change socratic session**~~ **DONE 2026-08-17** — D7–D12
   decided and recorded (see §5 register + regulatory-change-management.md);
   template/guide updated; correction corollary → 02 §3.11 FR-159..164.
3. **S2 waves** (each: extraction → evidence → synthesis, same patterns;
    source mapping authoritative in COVERAGE.md): ISR (03_/04_/10_) —
    **extraction + evidence DONE (W6); blockers CLOSED + new-source evidence
    DONE (W6.5/W7: EVID-153..170; gating OQs resolved)** → next = **S2
    prep**: digest/merge W6+W7 evidence into the
    ISR cluster (master-index extension; fold the 54_-file OQ-4 reglamento
    provenance check into the merge) → plan doc → subagent synthesis
    into `sv/requirements/taxation/` (citations: 54_/53_ current authority,
    03_/10_ historical; Art. 37 = TWO dated vintages; Art. 3.4/4.16/14-A
    deltas folded) → F-07/F-14 reporting (29_/30_/34_–39_; **check F14 v17
    2026-06 vs our v16 manual — acquire if the layout moved**) → payroll
    (08_/09_/11_/16_) → commercial-legal (07_/15_/17_) → special-regimes
    (12_/13_/14_/17b_/42_/43_; D.L. 598-2020 + EVID-167 tail laws feed it)
    → NIIF/chart-of-accounts (32_/33_). F-14 manual (35_) is OCR'd.
4. **Externally-blocked OQs** (check factura.gob.sv periodically): Retorno/
   OpEsp endpoints (MOQ-05 — 52_-schema absence verified 2026-08-17; 03
   OQ-006, 02 OQ-003); CAT-024 vs Cuadro-2 taxonomy confirmation. When new
   docs appear: continue source numbering from 53, register with provenance,
   capture supersession.
5. **Remaining S1 OQs** (34 open): most are business decisions (FVS flow,
   email scope) or AT-publication dependencies; 45_ §10 re-read for MOQ-07
   (02 OQ-001/002) can ride along with the S2 transmission-adjacent work.
   Addendum follow-ups: 02 OQ-011 (line-level move↔picking design pass —
   product owner's prior implementation as input) before FR-162/163
   implementation; 02 OQ-009 (NRE fate — watch AT/45_ revisions); 06
   OQ-008 (D10 protocol guarantee FR wording, next 06 edit).
6. **Deferred cleanups** (§9 below, batch them).
7. **GT/HN bootstrap** when sv is sufficiently far along (GT sources first:
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

## 10. Session-protocol checklist for the next controller

1. Read §1–§8 of this file; read the documents in §2 in order.
2. Confirm state: `git log --oneline -20`, `git status` (expect clean),
   `ls sv/requirements/e-invoicing/`.
3. Follow skills (brainstorming gate for new design work; SDD for plan
   execution; systematic-debugging for any investigation).
4. Before ANY source citation: check authority order (§3) and COVERAGE.md.
5. At session end: update THIS file (state, rulings, next actions), commit,
   push. Copy any SDD-ledger rulings here BEFORE deleting the workspace.
