# Regulatory Change Management — Working Note

**Status: DECIDED (Q1–Q7, socratic session 2026-08-17; D15 applicability
session 2026-08-19).** The framing below is retained verbatim; the decision
log (D7–D15) at the end of this document is binding for S2+ synthesis,
alongside D1–D6 in
[saas-thin-client-architecture.md](saas-thin-client-architecture.md).

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

## Session output (filled 2026-08-17)

- Decision per Q1–Q7 recorded below as D7–D12, continuing the D-numbering
  from the S0.5 architecture session. Binding for S2+ synthesis.
- Template/localization-guide updates flowing from the decisions: done
  (template §5 version-regime note; guide pointer).

---

## DECISION LOG (Q1–Q7 socratic session, 2026-08-17)

### D7 — SaaS MH-spec runtime: replace-in-place + switchover dates (Q1)

The SaaS always implements the CURRENT MH spec; switchover dates (Cuadro 4
adaptation windows) are configuration, not code paths. MH itself enforces
the spec version at seal time and refuses non-compliant documents after the
adaptation deadline, so an old-spec engine has a regulator-enforced death
date. History is immutable, self-describing artifacts (each DTE carries its
own `version`), never a live engine. The Odoo client never sees MH versions
at all — only private-protocol semver (D6).

### D8 — Catalogs: immutable releases via SaaS feed (Q3)

The Odoo client stores catalog RELEASES (set + version label + publication/
effective date + rows) as atomic immutable units delivered through the
private protocol. Lookup "code X at date D" = latest release effective ≤ D;
emission pickers use the latest release. Catalog changes become DATA events,
never module upgrades; the Tier A mirror stays self-sufficient for rendering
historical documents (CAT-013 code re-assignment lesson; reinforces
SV-CAT-FR-007..010).

### D9 — Reporting: freeze at filing + post-time amounts; correction corollary (Q5)

Move lines freeze tax amounts at posting (Odoo-native); the declaration
record (F-07/F-14) snapshots its computed report lines AT FILING — the
snapshot is the legal artifact. Unfiled periods recompute freely.
Rectificativas derive from the frozen original + explicit adjustment moves,
never from re-running reports over old periods with new config. Tax/rule
changes ship as ADDITIVE dated data (new templates, cutover dates); existing
records are never edited in place — the same discipline as D8 catalogs.

**Correction corollary (binding):** fiscal corrections ALWAYS post as new
entries in the correction period; originals are immutable. Specifically:
invalidation ⇒ auto-generated non-editable full-mirror reversal entry dated
in the event's period (credit-note treatment cross-month); retorno ⇒ credit
entry in the retorno period; window-expired CCF/CR ⇒ NCE/NDE. Where the
commercial currency ≠ USD, corrections derive their USD amounts from the
ORIGIN document's conversion rate — never the correction-date rate — so
correction can never create currency gain/loss. Operational FRs:
`sv/requirements/e-invoicing/02_transmission.md` §3.11 (FR-159..164).

### D10 — Dual-version disposition + protocol version guarantee (Q2)

(a) Rectificativas for pre-change periods ⇒ D9 artifacts (legal obligation,
CT 280 transition principle). (b) Audits/fiscalización of old periods ⇒ D9
artifacts + Tier A mirror (obligation). (c) Transition-window operation ⇒
D7 (each period freezes at its own filing; windows are configuration).
(d) Cross-version adjustments (e.g. NCE v4 referencing a CCF v3) ⇒ the
SaaS generation engine (D2) — schemas are self-describing and generation is
central. NEW protocol guarantee: every document/event record the SaaS
returns carries its MH schema version (06_api-protocol OQ-008 formalizes
the FR wording) so the Odoo mirror renders history without knowing MH
schemas. No live old-spec engine exists anywhere.

### D11 — Normative packs + wizard; the SaaS absorbs urgency (Q4/Q6)

Odoo-side law changes ship as additive dated data ("normative packs": new
tax templates, report lines, fiscal-position flips keyed by cutover date)
applied by a lightweight "cambio de normativa" wizard per branch (l10n_es
precedent; CoA templates never touch live taxes). MH adaptation deadlines
bind the SaaS (central deploy, days), NOT the client — a client release is
needed only when its own surface changes (booking-affecting taxes, report
layout) or the private protocol MAJORs. Support policy: develop newest
branch first; backport additive packs to every supported branch (17–20) —
packs are additive, so backports are cheap.

### D12 — Repo conventions: version-regime as first-class requirements data (Q7)

(1) The requirements template §5 requires any FR whose behavior depends on
a spec version to record version + effective date + adaptation window in
the version-notes column. (2) The W5.5 supersession-map pattern (delta +
effective date + adaptation window captured BEFORE synthesis) is standing
policy for every extraction wave. (3) D7–D12 join D1–D6 as binding
citations for synthesis Layer/version assignments.

### D15 — Applicability windows: as-of resolution + snapshot-on-write; no retro-transmission; history-import contract (decided 2026-08-19)

Extends D7–D12 from *spec* versioning to **legal applicability windows for
every dated parameter** (tax rates, brackets, caps, SMM-indexed thresholds,
regime schedules, sanction scales). Binding for all remaining synthesis
waves (special-regimes, IVA-core, NIIF/COA) and retroactively consistent
with S1–S6 output (no existing FR contradicts it; the S4/S6 dated-config
disciplines are its precursors).

**(a) Mechanics — snapshot-on-write over dated rows.** Every legal parameter
lives as a **dated row** (`valid_from`, open-ended `valid_to`; immutable once
cited by a posted/validated record; a change = a NEW row, never an edit —
same discipline as D8 catalog releases). At creation time Odoo resolves each
parameter **as-of the domain's anchor date** (table below) and **stores the
resolved values on the record** (move-line tax amounts, payslip line amounts,
DTE payload fields, report-line figures). Already-posted documents never
re-resolve; corrections compute with the ORIGINAL-period parameters (D9
corollary kin). Rejected alternative: resolve-at-read (documents store only
inputs; every view recomputes) — silent retroactive drift, breaks D9
freeze-at-filing and §3.11 immutability. Layering: transactional taxes ALSO
version the `account.tax`/template record itself (Odoo-native snapshot
carrier; deactivate-old-at-cutover per D7/D11 normative packs), while the
dated-row layer carries the numeric lookups (brackets, caps, SMM-derived
values, thresholds). The CSV sidecars with `valid_from` columns
(`isr_brackets.csv`, `smm_2025.csv`, `ss_contributions.csv`, catalog
sidecars) are the seed data for these rows.

**(b) Anchor-date table** (what "as-of" means per domain; the instrument's
own language always wins; corpus-silent straddles become OQs with disclosed
working assumptions — never invented formulas):

| Domain | Anchor date |
|---|---|
| IVA on a document | invoice/credit-note date (hecho generador; Ley IVA Art. 4, W3) |
| ISR wage retention | the payment period per D.E. 10-2025 (June/Dec recálculo tables carry their own rules) |
| ISR annual liquidation (F-11) | the fiscal year; mid-year bracket straddle stays OQ until MH guidance (taxation 03 OQ-009) |
| SS caps + SMM-derived values (4×SMM indemnización cap, 3×SMM FE threshold, 25-SMM cash ban, AML SMM sanctions) | the payroll/transaction period; effective-date straddle within a period = period-start working assumption (SOQ-02/SOQ-18 kin, OQ-tracked) |
| DTE schema/catalog version | emission moment (D10/D8) |
| Declarations F-07/F-14/F-910/F-930/F-935/F-11 | rules in force for the DECLARED period, frozen at filing (D9) |
| ZF/LSI/DPA exemptions | the beneficiary's per-acuerdo dated schedule: acuerdo D.O. publication + N-year window by location + 60%/40% phase-down ladder (ZF Arts. 11/17/19; LSI Arts. 14/17/21/25) — per-company config rows, never global constants |
| AML regime | transaction/report date against the 2025-10-17 cutover rows (CML/10) |
| Quincena-25 | payment window (15–25 Jan) + year-based mandate flags (2026 voluntary-private/2027+ all-mandatory) |

**(c) No retro-transmission.** Odoo/the SaaS never emit a DTE or filing
dated in the past; regulators' clocks are unidirectional. History enters as
**read-only external records** (history-import contract):

- **Historical DTEs** (pre-go-live, emitted by another system): imported
  read-only with original numbering, flagged `emitted-externally`, no
  re-transmission/no re-numbering, rendered from their own stored payload
  (D10 version guarantee). Import is **validated against MH consulta
  endpoints** (22_/46_ surface) producing a non-blocking exceptions report
  (mismatches flagged for follow-up, import proceeds) — needed so F-07
  annexes/emitidos derive a complete period. Physical pre-e-invoicing
  invoices (facturas pre-DTE): config-gap OQ — optional import as deduction
  evidence, never the default path.
- **Payroll history**: per-employee **monthly aggregates** (devengado/
  bonificaciones/retención/SS per month) + **contract tenure records**
  (start/end dates) — sufficient for indemnización (30d/year), vacaciones
  (200-day gate), aguinaldo (10/15-25 Dec tiers; Art. 4.16 split) and the
  F-910/F-11 annual surfaces; full historical payslips are NOT imported.
- **Ledger / stock / banks**: opening balances only — no movement-level
  history import.

**(d) Payroll corrections — hybrid by window.** Declaration period still
open → recompute + replace in place (always with original-period rules).
Period already filed → original slip immutable + **delta/refund slip in the
correction period computed with the ORIGINAL-period parameters** (D9/§3.11
mirror; SS declaration corrections follow the same split).

## Q → D mapping

| Question | Decision |
|---|---|
| Q1 module runtime | D7 |
| Q2 dual-version calculation | D10 (disposition matrix) |
| Q3 data model | D8 |
| Q4 migration mechanics | D11 |
| Q5 reporting | D9 (+ correction corollary) |
| Q6 maintenance model | D11 |
| Q7 this repo | D12 |
| Applicability windows (session 2026-08-19) | D15 |
