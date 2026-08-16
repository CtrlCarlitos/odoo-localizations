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
| Topic   | e-invoicing / taxation / chart-of-accounts / payroll / fiscal-reporting |
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

How each functional requirement maps onto Odoo models and fields. Note
version-specific behavior for Odoo 17/18/19/20 wherever they differ.

| FR | Odoo model | Field(s) | Notes / version differences |
|----|------------|----------|------------------------------|
| | | | |

## 6. Acceptance Criteria

Given/When/Then criteria. These are what Takumi must satisfy; each must be
objectively verifiable.

- **AC-001:** Given ..., when ..., then ...

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | | yes / no | | open / resolved |
