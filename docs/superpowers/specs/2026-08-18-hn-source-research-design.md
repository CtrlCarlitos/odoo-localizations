# Honduras — Source Research & Corpus Acquisition Design

**Date:** 2026-08-18
**Status:** Approved in session — pending spec review
**Branch:** `hn-research` (worktree `.worktrees/hn-research`); merge to `main` at milestone

## Purpose

Bootstrap the Honduras (HN) localization from scratch: deep research across
official websites to locate, evaluate, acquire, and register every relevant
source document (PDF, XLS/XLSX, CSV, DOC/DOCX, etc.) into `hn/sources/`, then
write the country execution plan (`hn/EXTRACTION_PLAN.md`, Stage 0 of the
[shared extraction procedure](../../../shared/docs/requirements-extraction-procedure.md)).

For El Salvador this stage never happened as a deliberate pass — the corpus was
imported from a prior project (tuky-workspace) and gaps were patched wave by
wave (ISR retention tables, D.O. reform extracts, F-14 v17, Quincena-25
package, AML replacement law). For HN we invert that: research first, so the
extraction waves start from a complete, currency-checked corpus.

## Decisions (this session, binding)

1. **E-invoicing IS in scope for Honduras.** The 2026-08-16 repo-structure
   spec's scope table ("HN electronic invoicing: No") is superseded by this
   spec. Rationale: SAR has been phasing in mandatory facturación electrónica;
   by 2026 it is in advanced mandatory stages and an HN localization without
   it would be incomplete. `hn/README.md` gets an e-invoicing topic row.
2. **Acquire + register immediately** (no download gate): clearly-relevant
   official documents are downloaded into `hn/sources/` and registered with
   full provenance as they are found and verified. Borderline cases
   (third-party mirrors, possibly-superseded versions) are still flagged in
   the dossier; mirrors are used only when the official source is
   unreachable, and are recorded as mirrors.
3. **Merge milestone = corpus + plan**: acquired/registered source corpus +
   research dossier + updated `hn/README.md` + `hn/EXTRACTION_PLAN.md`. No
   evidence passes, no requirements files in this phase.

## Research scope (topics and what we hunt)

Registry sections in `hn/sources/README.md` mirror the SV pattern. Topics:

| Topic | Hunt list (starter — refined during research) |
|-------|-----------------------------------------------|
| **e-invoicing** | SAR facturación electrónica stack: legal framework (resoluciones/acuerdos/circulars), technical specs (XML structure, catalogs de datos / catálogos de documentos, validation rules), onboarding/registration manuals, portal docs, contingency rules |
| **taxation** | Ley del Impuesto sobre la Renta (D. 25-1966 + reform chain, esp. D. 170-2020 and later) + Reglamento; Ley del Impuesto sobre Ventas (ISV, D. 24-2001) + Reglamento; Código Tributario (D. 51-2003) + reforms; retenciones (anexos/resoluciones, DTI-AI forms); DAI/aportes if SAR-published |
| **fiscal-reporting** | Declaración Jurada Determinativa (Formulario 1000 series) + all anexos (retenciones ISR, ISV crédito/retención, RTI etc.), rates/tables, calendario tributario/calendario de agentes, SAR guides |
| **payroll** | Código del Trabajo (D. 189-1959 + reforms); salarios mínimos (STSS decretos, sector tables); IHSS law + reglamento + rates/caps (and resolution updates); RAP/IVM pension law + administrators' rates; INPREMA; vales de alimentación rules; aguinaldo + bono fin de año (double December bonus); finiquito rules |
| **chart-of-accounts** | What governs Honduran books: Código de Comercio accounting articles + NIF/NIIF adoption instruments (TSC/CPMCP) — expected thinner than SV; only statutory instruments, not textbooks |
| **commercial-legal / special-regimes (net-cast)** | Código de Comercio (books/retention/registry duties), Ley de Lavado de Activos (threshold reporting), ZOLI/ZIP/RIT regimes, ZEDE status post-2022 repeal — tag candidates in the dossier; don't force completeness in this phase |

## Source universe (dig order)

1. **sar.gob.hn** — legislación section, formularios, resoluciones,
   facturación electrónica section. Same WordPress/download-manager (wpdmdl)
   stack as factura.gob.sv → SV fetch lessons apply: download-manager labels
   do not always match content; verify page 1 of every file before
   registering; record the resolved wpdmdl URL.
2. **Congreso Nacional** (congresonacional.hn) — consolidated laws; prefer
   the newest consolidation available.
3. **La Gaceta** (official gazette) — publication dates + reform texts when
   consolidations lag behind.
4. **Payroll-side authorities** — STSS (salarios mínimos), IHSS, INPREMA,
   SEP (reglamento código trabajo) — rate instruments.
5. **TSC / CPMCP** — accounting norms; **SEFIN / BCH / ONCAE-DGA** —
   official mirrors and customs if needed.
6. Law-firm or portal copies only when official is down — labeled
   non-official mirror in provenance, never as primary.

## Evaluation & registry discipline

Per document:

- **Relevance**: maps to ≥1 topic above. Rejected candidates are logged in
  the dossier (`hn/RESEARCH.md`) with reason — stale, superseded,
  out-of-scope, duplicate, unofficial-only.
- **Currency**: check consolidation date / reform chain / "actualizado"
  markers; newest authority wins; superseded files retained as historical
  LB only when they carry evidence value (SV pattern).
- **Official provenance required**; registry rows carry File / Topic / Title
  / Issued / Retrieved / Provenance URL filled from day one (no "pending"
  debt — SV's registry needed a later provenance-backfill wave).
- **Download verification**: read page 1 (pypdf) of every file — title must
  match the registry title; note scan quality/OCR expectation in the row.
  SV quirks may transfer (D.O.-style scans; the extraction script handles
  qpdf repair/OCR flags).
- Numbering `NN_name.ext` continues sequentially within `hn/sources/`;
  never renumber.

## Deliverables at milestone

1. `hn/sources/` — acquired corpus, unmodified originals.
2. `hn/sources/README.md` — registry, sections per topic, full provenance,
   supersession notes.
3. `hn/RESEARCH.md` — dossier: sites visited, search queries used,
   rejected/stale documents + reasons, open leads (things to watch:
   announced reforms, pending publications), per-topic assessment, fetch
   recipes (SV HANDOVER §6 style).
4. `hn/README.md` — e-invoicing topic added; statuses updated.
5. `hn/EXTRACTION_PLAN.md` — Stage 0: source inventory & decomposition,
   dependency-aware reading order, topic map, known risks — informed by what
   the corpus actually contains.

## Out of scope for this phase

- Evidence passes (Stage 2) and `.extractions/` content beyond throwaway
  page-1 verification
- Requirements files / Takumi templates (Stages 3-5)
- NotebookLM notebook creation (corpus too young; revisit at first synthesis)
- GT and SV work (other sessions own them; main stays untouched until merge)

## Risks / unknowns to resolve during research

- **E-invoicing instrument inventory unknown**: which resolución governs the
  current mandatory stages, where the technical specs live, whether there's
  a public XSD/catalog set — first research question.
- **Consolidation lag**: Honduran consolidations may lag years behind
  reforms (SV lesson: 03_ consolidation was 2012-vintage); identify the
  newest per law and its gap vs. La Gaceta.
- **Gazette accessibility**: La Gaceta's site reliability is unknown; if
  down, log it and use official mirrors labeled as such.
- **Payroll rates fragmentation**: IHSS/RAP caps and salarios mínimos are
  decree/resolution-driven and scattered; expected to need multiple small
  instruments rather than one law print.
- **ZEDE regime**: repealed/reformed in 2022+; flag whatever the current
  situation is rather than assuming either way.

## Success criteria

- Every registry row verified (page-1 read), provenance-complete.
- Dossier explains why each corpus document is there and what was rejected.
- `hn/EXTRACTION_PLAN.md` is executable by a fresh session without
  re-doing the research (reading units derivable from inventory).
- No changes outside `hn/` and this spec; merge is conflict-free by
  construction (other sessions don't touch `hn/`).
