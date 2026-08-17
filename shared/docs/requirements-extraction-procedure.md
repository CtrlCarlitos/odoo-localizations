# Requirements Extraction Procedure

The method spine for extracting Odoo localization requirements from source
documents. Invariant across countries. **How** it executes (reading order,
decomposition, topics that exist) is decided per country in that country's
execution plan — each country is a different legal world; only this spine
repeats.

## Core principles

1. **Direct reading.** Requirements are derived from the source text itself,
   read end-to-end. Retrieval tools (search, NotebookLM) never substitute for
   reading; they point and validate.
2. **Traceability.** Every requirement cites a Legal Basis (LB): file in
   `<cc>/sources/`, article, and page/section. No trace → not a requirement
   (an open question at best).
3. **Two layers.** Extraction produces evidence; synthesis produces the
   Takumi-template requirements. Never write requirements directly from a
   single pass over a single document.
4. **Repeal-aware.** Laws, reglamentos, and codes overlap; procedural
   articles are frequently repealed by later codes. The merge pass decides
   what is current — the newest authority wins, and repeals are recorded,
   not silently dropped.

## Layers

| Layer | Location | Nature | Content |
|-------|----------|--------|---------|
| Sources | `<cc>/sources/` | Committed, read-only | Official documents + registry |
| Extracted text | `<cc>/.extractions/` | Git-ignored scratch | Plain-text renderings with page markers |
| Evidence bank | `<cc>/.extractions/<doc>.evidence.md` | Git-ignored scratch | Per-document: LB citations, verbatim Spanish quotes + English gloss, candidate requirements, topic tags, doubts |
| Hint layer | Prior-work repositories (external links) | Read-only reference | Old AI-generated requirements — pointers for where to read, never sources |
| Requirements | `<cc>/requirements/<topic>/` | Committed deliverable | Takumi-template files |

Evidence and extracted text are scratch: regenerable, not reviewed, not
published. If context is lost, re-extract; the requirements and the coverage
matrix are the durable record.

## Pipeline

### Stage 0 — Country execution plan (`<cc>/EXTRACTION_PLAN.md`)

Written before any reading. Contains:

- Source inventory: each document, what it governs, expected topics
- Decomposition: multi-topic documents split into reading units (book/title/
  chapter/article ranges per topic)
- Reading order: dependency-aware (foundational catalogs and core tax law
  first; reporting and special regimes later)
- Topic map: source units → requirement topics
- Risks: known repeals, wrong-document incidents, incomplete sources

### Stage 1 — Text extraction

- `shared/scripts/extract_text.py` converts each source to text with page
  markers (`=== PAGE n ===`), so citations carry `p. N`.
- XLSX/XLS/JSON/MD sources need no conversion.
- Output to `<cc>/.extractions/`. Verify extraction quality per document
  (scanned PDFs may need OCR — flag, don't guess through).

### Stage 2 — Per-document reading (evidence pass)

One document (or reading unit) at a time, batched. For each:

1. Read the extracted text end-to-end.
2. Record LB candidates: article/page + verbatim Spanish + English gloss.
3. Record candidate requirements, tagged with **every** applicable topic —
   filing decisions happen in synthesis, not here.
4. Record doubts and cross-references (to other articles/documents) as-is.
5. Pre-load hint-layer pointers before reading (they say *where* to pay
   attention, and are confirmed or refuted by actually reading).

Rules: quote verbatim, never paraphrase into the record. A candidate
requirement without an LB candidate is discarded on the spot.

### Stage 3 — Merge and dedup pass

Across documents, per topic cluster:

- Merge duplicates (same rule stated by law + reglamento + code → one FR,
  multi-LB citation; prefer the most authoritative/current wording).
- Detect conflicts (documents disagreeing) → open questions, not silent picks.
- Detect repeals (old wording superseded) → record in the requirements file's
  Legal Basis notes; the FR cites current authority.
- Produce the authoritative candidate list per topic.

### Stage 4 — Topic synthesis (Takumi template)

For each topic, write `<cc>/requirements/<topic>/<nn>_<scope>.md` following
`shared/docs/requirements-template.md`:

- FRs numbered with globally unique, stable IDs: `<CC>-<TOPIC>-FR-<nnn>`
  (e.g. `SV-EINV-FR-001`). Cross-topic references cite IDs, never duplicate
  content.
- Data Model: entities/fields/catalogs; machine-readable sidecars (CSV/JSON)
  live next to the markdown.
- Odoo Mapping: model/field mapping with version notes (17/18/19/20). Validated
  architecture decisions from prior work may be imported here — as decisions,
  with their rationale, subject to review.
- Acceptance Criteria: Given/When/Then, objectively verifiable.

### Stage 5 — Validation wave

All three gates must pass before a topic is `approved`:

1. **Coverage matrix** (script-checked): every source-registry row maps to
   ≥1 LB citation *or* an explicit not-applicable note; every FR cites ≥1 LB;
   every LB resolves to a real file/article. Stored per country as
   `<cc>/requirements/COVERAGE.md`, generated by script, committed.
2. **NotebookLM gap probing** (optional, where a notebook exists): ask what
   the corpus says that the requirements don't cover; hunt contradictions
   across documents. Any finding enters requirements only after tracing to
   the real source file — no trace → open question. The notebook is a
   validator, never the source of truth.
3. **Adversarial review**: fresh reviewer attacks the requirements files
   (ambiguity, contradiction, untestable ACs, missing versions notes).
   Findings fixed or parked with rulings before approval.

## Topic taxonomy

Starter set: `e-invoicing`, `taxation`, `chart-of-accounts`, `payroll`,
`fiscal-reporting`, `commercial-legal`, `special-regimes`, plus a shared
`catalogs` topic where a country's authority catalogs live (machine-readable
sidecars). Countries extend per their execution plan; the template's Topic
row lists the current set.

Cross-cutting concerns (catalogs, ID types) get their own requirement files
in `catalogs/`; topic files reference by FR ID.

## NotebookLM usage policy

- **Allowed:** post-synthesis gap probing, contradiction hunting, spot-check
  summaries of sections already read.
- **Forbidden:** generating requirements, answering "what does the law say
  about X" during extraction, citing the notebook as LB.
- **Incomplete-corpus rule:** absence of evidence in the notebook is evidence
  of nothing; only positive, traced findings count.

## Cross-country patterns

Do not pre-build. When ≥2 countries exhibit the same concept (operation
types, retention documents, credit notes), record it in
`shared/docs/patterns.md` with citations to both countries' FR IDs. One
country is a data point, not a pattern.
