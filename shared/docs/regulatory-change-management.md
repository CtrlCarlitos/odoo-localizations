# Regulatory Change Management — Working Note

**Status: OPEN — framing note for a dedicated socratic discussion. Not a decision record.**

## The problem

Laws and technical specifications are versioned by *effective date* (vigencia),
with transition windows. Software ships as *releases*. A live Odoo instance must
simultaneously:

1. Emit documents that satisfy the spec in force **at each document's date**;
2. Keep already-emitted documents valid and readable **forever**;
3. Recalculate and report **past periods under the rules that governed them**
   (declaraciones modificatorias, fiscalización, audits).

Our El Salvador extraction proved this is not occasional — it is the operating
rhythm:

- Normativa v1.2 (Nov-2025) → **v2.0 (May-2026)**: two new event types
  (Retorno, Operaciones Especiales), new transmission modes for events,
  invalidation taxonomy rebuilt on the new CT articles.
- **Catalogs re-versioned downward** v1.2 → v1.1 (2026): version numbers are
  NOT monotonic; only dates are trustworthy. CAT-013 municipios restructured to
  the 44-municipio model (codes re-assigned); CAT-023 repurposed entirely;
  CAT-008 un-deleted (now Distrito); CAT-002 absorbed event codes 17/18.
- JSON schemas bumped per document type (CCF v4, FEX v3, F v2...), twice.
- FE receptor-name threshold changed **$200 → 3 salarios mínimos** (a
  floating index, not a constant!).
- Adaptation SLAs are defined by the regulator (Cuadro 4: structural changes →
  10 primeros días hábiles of the 3rd month; minor → next month; **seal is
  refused to non-compliant documents after the deadline**).

## Constraints any solution must respect (SV facts; verify per country)

1. Every DTE JSON carries its own per-type schema `version` — documents are
   self-describing.
2. Emitted DTEs are immutable legal artifacts (Archivo DTE + seal + RG in
   original format). History is never recomputed at the document level.
3. MH enforces spec versions at seal time with adaptation deadlines → there is
   a **switchover date**, and during windows both behavior and deadline logic
   matter.
4. Period reports (débito/crédito, F-07/F-14) recompute from posted data in
   Odoo; if taxes/rules change in place, past periods' reports silently
   change — but fiscal declarations must follow the rules in force for *their*
   period (transition principle, cf. CT Art. 280).
5. Catalogs are referenced **by code** from stored documents (municipio codes,
  tributo codes). The 2026 CAT-013 re-assignment proves codes get reused —
  replacing catalog rows in place corrupts the meaning of stored documents.
6. Cross-version operations exist: events (invalidación/retorno) and NC/ND can
   relate to documents emitted under an older schema version. (Whether MH
   allows cross-version relations is an open question — Anexo IV validations.)

## The questions (agenda for the socratic session)

- **Q1 — Module runtime:** replace-in-place vs effective-dated rule sets vs
  hybrid?
- **Q2 — Dual-version calculation:** when must BOTH versions be calculable
  simultaneously? Known cases: (a) rectificativas for pre-change periods;
  (b) audits of old periods; (c) transition-window operation (closing an old
  period while emitting under the new spec); (d) cross-version adjustments
  (NC v4 referencing a CCF v3). Which are legal obligations vs conveniences,
  per country?
- **Q3 — Data model:** catalogs as immutable dated rows (code, value,
  valid_from, valid_to)? Spec parameters as date-keyed feature sets?
- **Q4 — Migration mechanics:** on module update in a live DB, what changes?
  (Odoo precedent: CoA templates don't touch live taxes; l10n_es ships
  version-change wizards.) Do we ship "cambio de normativa" wizards?
- **Q5 — Reporting:** which figures are frozen at period close vs derived on
  demand? (Odoo tax reports recompute — a known hazard for retro periods.)
- **Q6 — Maintenance model:** spec changes must be backported to every
  supported Odoo branch (17–20), while the deployment's real date selects the
  applicable spec. Branch × spec-date matrix; who backports, how fast (MH
  deadlines are 1–3 months)?
- **Q7 — This repo:** capture effective dates and change deltas as first-class
  requirements data (the W5.5 supersession map becomes standing policy); the
  Takumi template's Odoo Mapping should record the version regime per FR where
  relevant.

## Candidate strategies (to be debated, not decided here)

**A. Replace-in-place + immutable artifacts.** Module always implements the
current spec; emitted documents stored immutably with their version; period
summaries stored at close (not derived). Simplest runtime; retro correctness
depends entirely on stored summaries.

**B. Effective-dated everything.** Rule engine keyed by vigencia date; catalogs
as dated rows; emission and period computation select rule sets by date.
Strongest correctness (rectificativas just work); most complex, highest
maintenance cost, foreign to Odoo's stock patterns.

**C. Hybrid.** Current-spec emission selected by switchover dates (config or
data-driven), immutable DTE storage, catalogs as dated data, period summaries
frozen at close, wizards/migrations for rule changes.

## Precedents to study before the session

- `l10n_mx_edi`: CFDI 3.3 → 4.0 transition (parallel operation by date) —
  the closest analog in the Odoo ecosystem.
- `l10n_cl` (SII), `l10n_ar` (AFIP RG changes), `l10n_co` (DIAN resolution
  bumps) — how LatAm localizations ship spec changes.
- Odoo core: `account.edi.format` version handling; tax-report recomputation
  semantics; `l10n_es` version wizards.
- MH's own behavior: Manual Tecnológico v2.0 notes platform-side configurable
  parameters — the regulator itself runs versioned services; watch how it
  communicates cutover dates.

## Already-adopted answers for THIS repo (low-risk, standing policy)

- Superseded sources are retained; every supersession is recorded with
  authority order, dates, and the delta (see sv W5.5 evidence).
- When a newer source supersedes one already read, the evidence pass MUST
  capture: what changed, effective date, adaptation window — before
  synthesis proceeds against it.
- Catalog sidecars regenerate to current version; the v1.1 lesson (code
  re-assignment) is the argument for dated catalog storage in the modules.

## Session output (to fill after discussion)

- Decision per Q1–Q7, with rationale, recorded as a decision log entry.
- Template/localization-guide updates flowing from the decisions.
