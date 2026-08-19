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

> **Country-scope note (added 2026-08-19 at the cross-country convergence,
> GT session):** D7–D12 were decided from the El Salvador corpus — the
> regulator nouns in their bodies (MH = Ministerio de Hacienda, Cuadro 4
> adaptation windows, F-07/F-14 forms, CT 280, CCF/CR/NCE/NDE document
> taxonomy) are **SV illustrations, not normative across borders**. The
> mechanics themselves are binding for every country in scope; each country
> instantiates them with its own regulator and instruments (GT: SAT, FEL
> Reglas y validaciones/XSD-catalog versions, SAT-2237-family forms, Código
> Tributario 6-91; HN: SAR/DEI, SAR formats, Código Tributario). Same rule
> as D15's instantiation register: no country's citation is normative for
> another country. D15/D16/D18/D19 below were written universal from the
> start.

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

### D15 — Applicability windows: as-of resolution + snapshot-on-write; no retro-transmission; history-import contract (decided 2026-08-19; universalized same day)

Extends D7–D12 from *spec* versioning to **legal applicability windows for
every dated parameter** (tax rates, brackets, caps, wage-indexed thresholds,
regime schedules, sanction scales, authorization ranges). Binding for every
country's synthesis. **D16 is the cross-country mechanics canon of this same
doctrine — cite D15+D16 together.** Country instantiations (anchor tables +
concrete surfaces): see the instantiation register at the end of this
decision — the canon below is country-neutral; examples live ONLY in the
register, and no country's citation is normative for another country.

**(a) Mechanics — snapshot-on-write over dated rows.** Every legal parameter
lives as a **dated row** (`valid_from`, open-ended `valid_to`; immutable once
cited by a posted/validated record; a change = a NEW row, never an edit —
same discipline as D8 catalog releases). At creation time Odoo resolves each
parameter **as-of the domain's anchor date** (see (b)) and **stores the
resolved values on the record** (move-line tax amounts, payslip line amounts,
e-document payload fields, report-line figures). Already-posted documents
never re-resolve; corrections compute with the ORIGINAL-period parameters
(D9 corollary kin). Rejected alternative: resolve-at-read (documents store
only inputs; every view recomputes) — silent retroactive drift, breaks D9
freeze-at-filing and correction immutability. Layering: transactional taxes
ALSO version the `account.tax`/template record itself (Odoo-native snapshot
carrier; deactivate-old-at-cutover per D7/D11 normative packs), while the
dated-row layer carries the numeric lookups (brackets, caps, indexed values,
thresholds). Extraction sidecars with `valid_from` columns are the seed data
for these rows.

**(b) Anchor-date selection (universal pattern).** What "as-of" means per
domain; two rules override everything: (1) the instrument's own language
always wins (a law that pins its anchor differently is followed literally);
(2) corpus-silent straddles (a parameter changing inside a period) become
OQs with disclosed working assumptions — never invented formulas.

| Domain (universal) | Anchor date |
|---|---|
| Transactional taxes on a document | document/emission date (the hecho generador / taxable event date per each country's law) |
| Wage withholding / payroll statutory values | the wage or payment period; recalculation windows carry their own rules |
| Annual liquidations | the fiscal year; mid-year parameter straddles = OQ until regulator guidance |
| Index-derived values (multiples of minimum wage, indexed caps, sanctions in wage units) | the payroll/transaction period; straddle assumption = period start (OQ-tracked) |
| E-document schema/catalog version | emission moment (D10/D8) |
| Declarations/reports | rules in force for the DECLARED period, frozen at filing (D9) |
| Special-regime incentives (free zones, services parks, sector regimes) | the beneficiary's per-instrument dated schedule (grant date + N-year window + phase-down ladders) — per-company config rows, never global constants |
| Regime cutovers (new laws replacing old) | transaction/report date against dated cutover rows |
| Time-boxed benefits/transitories | the instrument's own window + year-based mandate flags |

**(c) No retro-transmission; history-import contract.** Odoo/the SaaS never
emit an e-document or filing dated in the past; regulators' clocks are
unidirectional. History enters as **read-only external records**:

- **Historical e-documents** (pre-go-live, emitted by another system):
  imported read-only with original numbering, flagged `emitted-externally`,
  no re-transmission/no re-numbering, rendered from their own stored payload
  (D10 version guarantee); import **validated against the regulator's
  consultation endpoint** producing a NON-BLOCKING exceptions report
  (mismatches flagged, import proceeds) so period declarations derive
  complete totals. Paper-era pre-e-invoicing documents: config-gap OQ —
  optional import as deduction evidence, never the default path.
- **Payroll history**: per-employee **monthly aggregates** + **contract
  tenure records** (start/end dates) — sufficient for every tenure-based
  statutory benefit (severance, vacation, year-end bonuses) and the annual
  reporting surfaces; full historical payslips are NOT imported.
- **Ledger / stock / banks balances**: opening entries only. (AMENDED by
  D18: the straddle fiscal year's TRANSACTIONAL detail is additionally
  imported under `is_historical` — tiered contract in D18(b).)
- **Reconciliation against FILED history**: see D16 ¶7.

**(d) Payroll corrections — hybrid by window.** Declaration period still
open → recompute + replace in place (always with original-period rules).
Period already filed → original slip immutable + **delta/refund slip in the
correction period computed with the ORIGINAL-period parameters** (D9 kin;
social-security declaration corrections follow the same split).

**Country instantiation register (D15).** Each country records its concrete
anchor mapping (instruments + citations) at synthesis time; the register is
illustrative for other countries, never normative across borders:

- **SV (decided 2026-08-19):** anchor table — IVA → invoice/credit-note date
  (Ley IVA Art. 4); wage retention → payment period per D.E. 10-2025;
  F-11 annual → fiscal year (straddle OQ taxation 03 OQ-009); SMM-derived
  values → payroll/transaction period (SOQ-02/SOQ-18 kin); DTE
  schema/catalog → emission moment; declarations F-07/F-14/F-910/F-930/
  F-935/F-11 → declared period frozen at filing; ZF/LSI/DPA exemptions →
  per-acuerdo schedule (D.L. 405 Arts. 11/17/19; D.L. 431/131); AML →
  transaction date vs 2025-10-17 cutover; Quincena-25 → payment window +
  year flags. History-import surfaces: F-07 annexes/emitidos derivation,
  F-910/F-11 feeds, pre-DTE invoices = config-gap OQ; seeds
  `isr_brackets.csv`/`smm_2025.csv`/`ss_contributions.csv`.
- **GT:** D-GT10 (spec `docs/superpowers/specs/2026-08-18-gt-source-research-design.md`).
- **HN:** D-H2/D-H3 (`hn/EXTRACTION_PLAN.md`; hecho-generador/period keys,
  CAI-range hard block, SAR-filing reconciliation).
- *(Future countries append their instantiation here at synthesis time.)*

### D16 — Date-driven compliance mechanics (cross-country; proposed as "D13" on gt-research 2026-08-19, approved by product owner same day; renumbered at the 2026-08-19 merge — D13/D14 already taken by the journal/establishment-model decisions in [odoo-localization-guide.md](odoo-localization-guide.md))

Taxes, e-invoicing, filings, and payroll all carry dated applicability
(vigencia). Odoo mechanics — binding for every country's synthesis.
**Complements D15** (D16 = mechanics canon; D15 = SV-anchored as-of doctrine
with the anchor-date table, snapshot-on-write, history-import contract).
Country instantiations: GT = D-GT10 (spec
`docs/superpowers/specs/2026-08-18-gt-source-research-design.md`); HN =
D-H2/D-H3 (`hn/EXTRACTION_PLAN.md`, `hn/HANDOVER.md`):

1. **Dated rule rows.** Every externally-sourced normative datum — tax
   rates, retention tables/percentages, salario mínimo / wage tables, social
   security cuotas, ISR brackets, FEL/DTE Reglas-XSD-catalog versions, form
   validities, authorization ranges (HN: CAI) — is stored with `valid_from` (required), `valid_to`
   (nullable), and instrument provenance. Rate changes ADD rows; they never
   mutate history. Extraction sidecars carry these columns from day one.
2. **Rule selection key.** The document's fecha de emisión (payslip período;
   declaration periodo) selects the in-force rule set ("rules at date D"
   lookup = D15 anchor-date resolution). Unposted drafts re-resolve freely;
   POSTED records carry D15 snapshots — recomputation of anything posted
   (corrections, retro runs) always selects the ORIGIN period's rules.
3. **E-invoicing: emission = certification timestamp.** No past-dated
   transmission (the DTE's legal timestamp is the certification moment).
   Drafts dated ≠ today are BLOCKED from transmission with guidance to the
   corrective path (current-dated NC/ND referencing the original, or
   anulación within its window). Emission outside an authorization range's
   vigencia (HN CAI kin) = HARD BLOCK, no override — the supervisor-override
   variant was considered and rejected (HN D-H2, adopted cross-country).
   History reconstruction (migration, paper era) = accounting-only entries
   under a historical/non-transmittable document class — never a DTE
   (D15(c)).
4. **Payroll: fully retro-capable.** The payslip period selects wage floor,
   cuotas, retention tables, statutory-benefit parameters. Retroactive runs
   recompute with the ORIGINAL period's rates; corrections post in the
   current period (SV adds hybrid-by-window: replace in place while the
   declaration period is still open — D15(d)).
5. **Filings: period rules + freeze-at-filing** (extends D9): a declaration
   for period P uses P's forms and windows; rectificativas file from the
   frozen snapshot plus adjustment moves. Filed periods are write-protected
   (HN D-H2 kin).
6. **Backdating UX.** Past date → period rules auto-selected;
   transmission-required actions blocked with explanation; accounting-only
   actions allowed with historical rates and an immutable audit note.
7. **Go-live ingestion reconciles against FILED history** (HN D-H3,
   adopted cross-country): imported historical detail/aggregates are
   reconciled against the declarations actually FILED with the country's
   authority (SAR in HN; MH in SV; SAT in GT) — discrepancies surface as
   exceptions, never silently absorbed (extends D15(c)).

### D18 — Mid-year go-live ingestion mechanics: `is_historical` flag + tiered import + correction paths (decided 2026-08-19)

**Driver (named):** an Odoo go-live rarely lands on January 1 — mid-year
go-lives mean the straddle fiscal year's filings (and filings that use
prior-year data) must compute COMPLETE from partially-imported history,
without Odoo re-processing what the predecessor system already handled.
Universal for every country in scope; refines D15(c) for the ledger tier.

**(b) Tiered ingestion contract (amends D15(c)):**

- **T1 — Straddle-FY transactional detail**: imported into the proper
  transactional models (account.move + e-document payload records, payroll
  aggregates, retentions), `is_historical = True`, in historical journals
  (see (d)). Covers emitted + received documents and tax-relevant
  transactions of the pre-go-live part of the fiscal year.
- **T2 — Prior-FY filings**: imported as FROZEN DECLARATION-SNAPSHOT
  records (the D9 legal-artifact model), `is_historical` — comparatives
  and carryover derivation without any prior-year account.moves.
- **T3 — Balances**: opening entries for ledger/stock/banks (unchanged
  from D15(c)).
- **T4 — Carryover ledgers**: dated rows per D15 (IVA saldo arrastre,
  capital-loss carryforwards, benefit-remanents, etc.).

**(c) `is_historical` semantics.** Set only by import tooling; posted
historical records are immutable (filed-period protection kin).
**Suppresses:** legal sequence assignment (original external numbering
preserved), e-document transmission (hard block — no retro-transmission,
D16 ¶3), payment matching / dunning / workflow automations, and
RECOMPUTATION (amounts fixed from the source payload / predecessor
values). **Allows:** validation + confirmation (posting) so records are
complete and report-visible — with the D15 subtlety that tax-grid
resolution still happens ONCE at import, resolved as-of the ORIGINAL date
(snapshot-on-write): the flag suppresses recompute, not resolution.
Distinct number sequences make imported vs Odoo-processed data visually
separable.

**(d) Journal grouper + integrity invariant.** `is_historical` exists on
records AND journals. Historical journals are the RECOMMENDED T1 pattern:
they keep their natural journal TYPE (sale/purchase/bank) so type-keyed
reports stay correct, while giving users a grouper that identifies what
was imported vs what Odoo processed. Where a journal exists: a record in
an `is_historical=True` journal MUST be `is_historical=True`, and
historical records are rejected in non-historical journals
(cross-check validation on save/post). **Flag-flip lock:** a journal
cannot switch its flag while it contains transactions contradicting the
target state (either direction). Journal-less models (e.g. some payroll or
statement surfaces): the record flag alone is the control.

**(e) Correction/deletion of mistaken imports.** Historical records never
fired Odoo sequences or transmissions (no external footprint) and were
already filed by the predecessor system — so deletion changes only LOCAL
completeness, never regulator truth. Two paths:

- **Primary: import-batch reversal.** Every import run registers a batch;
  "reverse import" deletes that batch's records atomically — wholesale
  mistakes (wrong file/period, duplicates) are batch mistakes, and the
  batch is the safe unit.
- **Surgical: config-gated delete.** A single global `res.config.settings`
  gate ("allow historical record management"), NOT per-type flags (per-type
  multiplies config surface without adding safety); explicit, off by
  default; every deletion under it writes an immutable audit entry
  (who/when/what).
- **Guard:** deletion by either path is BLOCKED when a live (non-historical)
  posted record or a filed declaration snapshot references the record.

### D19 — Cut-over mechanics: posting tiers, config accounts, sequence-init records, straddle-filing checkpoint (decided 2026-08-19)

Complements D18; operational catalog + country registers in
[go-live-readiness.md](go-live-readiness.md). Scope ruling: parallel-run
tooling, predecessor decommission/retention, and rollback doctrine are
explicitly OUT of scope (logged there §5).

**(a) Posting tiers at cut-over + config accounts.**
- **Closed historical items** (paid/settled): GL-NEUTRAL report fuel —
  posted net-zero against a single migration/clearing account with
  tax-grid lines attached (report derivation: tax grids, annexes, annual
  surfaces); P&L untouched; line granularity = full lines OR summary
  lines, whatever the legacy export provides.
- **Open items** (uncollected AR, unpaid AP, stock, bank): posted FOR
  REAL — actual subledger account ↔ `00/ZZ`-style control-account pair;
  matching stays suppressed (D18) — post-go-live payments on predecessor
  items route to the control account.
- **Opening trial balance**: dated AT CUT-OVER (not FY start), carrying
  everything cumulative; closed history exists alongside it purely as
  report fuel.
- **Config, never hardcode (D19(a+)):** the migration/clearing account
  and the control-account set are `res.config.settings` fields, each
  defaulting to a module-data account created with a **stable XML ID**
  (upgrade-safe): one clearing account + one control account per
  subledger (AR/AP/Stock/Bank).

**(b) Rounding.** Legacy amounts stored VERBATIM — never recomputed with
Odoo rounding; Odoo matches the legacy system, not the reverse; the
residual surface absorbs drift.

**(c) Sequence initialization via import.** The last legacy document per
(document type × establishment × point of sale) imports as a CANCELED,
GL-NEUTRAL move in the LIVE journal carrying an **`is_sequence_init`**
flag — NOT `is_historical` (those records live in live journals; D18's
journal invariant forbids the historical flag there). `is_sequence_init`
is READ-ONLY, settable ONLY by a server action or special import
procedure (never by hand). Sequences AND authorization-range
consumed-to counters (HN CAI kin) derive from these records; users never
type first numbers. Mid-range continuation is the automatic outcome;
fresh-range start remains a deployment choice.

**(d) Straddle-filing checkpoint.** Both paths supported —
predecessor-already-filed (declaration imports as a D18-T2 frozen
snapshot; Odoo's first live filing = the next period) or unfiled (Odoo
files the period complete from `is_historical` + live records). The
choice is an EXPLICIT go-live checklist item, never implicit.

**(f) Trial-balance ROUTING (not restriction).** A trial balance is
complete by nature: every line posts to its own REAL account,
unrestricted (assets, loans, equity, P&L — no allowlist, no import
blocking). The **control-treatment set** (defaults: AR/AP/Inventory/Bank;
extensible per company/customer) is the only special case: lines for
those accounts ROUTE to their configured control accounts instead of the
real subledger accounts, because their detail arrives separately via the
open-items import. Residual detection falls out naturally: each control
account nets trial-balance total against open-item imports; nonzero
balance = drift (rounding/omissions) → surfaced and cleared per
accountant instructions. The only validation is CONSISTENCY of
treatment: a control-set line that posted direct to the real subledger
account (bypassing the control account) would double-count once open
items land — that is blocked/flagged.

**D18 amendments flowing from D19:** T3 elaborated to the
control-account pattern; `is_historical` gains the two posting modes
(neutral report-fuel / open-item-real); matching stays suppressed for
open items; sequence-init records are `is_sequence_init`, not
`is_historical`.

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
| Date-driven compliance (dated rates/forms/regimes, retro payroll, no past-dated transmission; GT-proposed, HN-amended) | D16 |
| Mid-year go-live ingestion (is_historical, tiers, journal grouper, correction paths) | D18 |
| Cut-over mechanics (posting tiers, config accounts w/ XML IDs, is_sequence_init, straddle checkpoint, TB routing) | D19 |
