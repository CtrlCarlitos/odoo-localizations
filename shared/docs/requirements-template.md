# Requirements Template (Takumi Input Contract)

Every requirements file in `<cc>/requirements/<topic>/` follows this template
exactly. Copy it, rename it to match its topic scope, and fill in every
section. If a section genuinely does not apply, write "Not applicable" with
one line explaining why — never delete a section.

Requirements are written in **English**. Spanish legal and technical terms
are kept inline with an English translation on first use, e.g.
*factura electrónica* (electronic invoice).

---

# [Country] — [Topic] — [Specific scope]

| Field   | Value |
|---------|-------|
| Country | sv / gt / hn |
| Topic   | e-invoicing / taxation / chart-of-accounts / payroll / fiscal-reporting / commercial-legal / special-regimes / catalogs |
| Status  | draft / in-review / approved |
| Authors | name(s) |
| Updated | YYYY-MM-DD |

## 1. Purpose

One paragraph: what this requirement covers and what it does not.

## 2. Legal Basis

Every requirement must be traceable to an official source document in
`<cc>/sources/`.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | *Ley ...* | Law ... | `sv/sources/....pdf` | Art. 12 |

## 3. Functional Requirements

Numbered, testable statements. One requirement per line — no compound
requirements.

- **FR-001:** The system shall ...

## 4. Data Model

Entities, fields, catalogs, and code lists. Machine-readable versions
(CSV/JSON) live next to this markdown file.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| | | | | |

## 5. Odoo Mapping

How each functional requirement maps onto the solution, with version notes
where 17/18/19/20 differ. The **Layer** column records where the logic lives
when the product architecture splits the Odoo module (thin client) from a
SaaS core — see [saas-thin-client-architecture.md](saas-thin-client-architecture.md);
use `odoo` / `saas` / `shared`; write `n/a` only with a justification line.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| | | | | |

Version-regime note (D12): any FR whose behavior depends on a spec version
must record version + effective date + adaptation window in the Notes
column — see [regulatory-change-management.md](regulatory-change-management.md) D7–D12.
Applicability note (D15/D16): any FR whose value/behavior depends on a dated
legal parameter (rate, bracket, cap, SMM-derived threshold, regime schedule,
authorization range) must resolve it as-of the domain's anchor date, store
the resolved value on the record (snapshot-on-write), and carry
`valid_from/valid_to` rows for the parameter — see D15 (anchor-date
pattern + country instantiation register + history-import contract) and
D16 (cross-country mechanics: dated rows,
retro payroll with original-period rules, hard no-override emission block,
filed-period protection, ingestion reconciliation). Mid-year go-live FRs
(historical import surfaces) must follow D18: `is_historical` records in
historical journals (natural journal type), suppress/reallow semantics,
tiered ingestion (straddle-FY detail / prior-FY declaration snapshots /
balances / carryover rows), batch-reversal or config-gated deletion.
Go-live/cut-over FRs must follow D19 + go-live-readiness.md: posting
tiers (GL-neutral closed items / real open items via configurable
control accounts with XML-ID defaults), verbatim legacy rounding,
`is_sequence_init` sequence initialization, trial-balance routing, and
the explicit straddle-filing checkpoint.
## 6. Acceptance Criteria

Given/When/Then criteria. These are what Takumi must satisfy; each must be
objectively verifiable.

- **AC-001:** Given ..., when ..., then ...

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | | yes / no | | open / resolved |
