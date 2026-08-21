# Thailand standalone-agent benchmark brief (2026-08-20)

Benchmark experiment (owner): third instance of the standalone-agent
test (after Colombia, Peru) — hand THIS brief alone to a different
coding agent in a clean environment. Intent, scope, deliverables and
quality bars only; deliberately NO method, tooling, file conventions,
or process hints from this repo. First NON-Latam target (Thailand is
not on the owner roadmap): also a stress test of whether the brief's
quality bars hold outside the Spanish civil-law world. Purpose:
compare that agent's output against our process-driven result to
evaluate what the method contributes. Everything below the line is
the brief as handed to the other agent.

---

# Mission: Odoo Localization Requirements for Thailand

You are producing the complete requirements foundation for an Odoo
localization for Thailand. This is a documents deliverable, NOT a coding
task: you will not build the module. A development team will later
implement an Odoo module (target versions 17–20) directly from your
requirements, without access to you.

## Deliverables

1. **Source corpus** — acquire the official source documents (acts,
   royal decrees, ministerial regulations/notices, Revenue Department
   rules and return-form instructions, departmental guides, published
   technical specifications) for every domain in scope. Each document
   must be precisely identified: instrument number, emission date,
   publication/Royal Gazette reference, official URL, acquisition date.
   Preserve files as acquired.
2. **Evidence record** — for every requirement, the exact legal or
   technical basis: instrument + section/section number, with the
   verbatim quote in the official language of the instrument (Thai, or
   the official English version where the authority publishes one) plus
   a short English gloss. Where you rely on an official English
   translation of a Thai-language instrument, record that fact.
   Conflicts between sources are recorded as such. Anything unclear,
   ambiguous, or unobtainable becomes an open question — never a guess.
3. **Requirements files** — structured, referenceable requirements
   (unique IDs per requirement; each with legal-basis citation and
   acceptance criteria) detailed enough that an Odoo developer could
   implement from them without asking questions.
4. **Coverage map** — per source: fully read / partially read / pending;
   and per requirement: traceability to its evidence.

## Domains in scope

- **Electronic invoicing / tax invoices** (Revenue Department regime:
  tax invoice and receipt formatting/content rules, e-Tax Invoice &
  e-Receipt scheme conditions incl. digital-signature requirements,
  abridged tax invoices as evidenced, credit notes /
  debit notes / tax refund forms, reporting of invoice data to the
  authority, contingencies)
- **Indirect tax**: VAT (rates, base rules, zero-rated/exempt classes,
  input-tax credit conditions), Specific Business Tax mechanics,
  excise/other levies only as evidenced
- **Direct tax company-side**: Corporate Income Tax (rates, filing
  cadence, half-year and year-end returns), withholding tax regimes
  (payments for services, rent, interest, dividends; agent obligations)
- **Payroll**: salary regime under labour law (daily/periodic wages,
  working-time-driven payments), minimum wage (regional daily rates as
  dated configuration), Social Security Fund contributions (employer +
  employee), Workmen's Compensation Fund, provident fund (voluntary
  regime as evidenced), severance and termination payments, Personal
  Income Tax withholding on salaries (progressive bands, allowances as
  evidenced)
- **Fiscal books & reporting**: statutory accounting/books obligations
  incl. Thai accounting standards (TFRS) context that drives
  chart-of-accounts configuration, VAT and withholding return forms and
  their data fields, supporting-document schedules the returns imply
- **Company compliance essentials** that affect system configuration
  (company registration/DBD identity data, 13-digit tax identification
  number, VAT and other registrations incl. thresholds, filing
  obligations calendar)

Out of scope: consumer-facing storefronts, non-fiscal CRM, HR recruiting.
Borderline items: record as open questions with your recommendation.

## Rules

- **Official sources only** for legal basis (Thai Revenue Department,
  Ministry of Finance, Department of Business Development, Ministry of
  Labour, Social Security Office, Royal Gazette, ministry regulations).
  Third-party accounting firms/summaries may help you FIND the
  instrument; they are never citable as basis.
- **Dated values are configuration, never constants**: tax rates, wage
  floors by region, contribution caps, PIT bands, WHT rates,
  registration thresholds — each captured with its value, effective
  period, and the instrument that sets it, including supersession
  history (what replaced what, when). Amounts are in THB unless the
  instrument states otherwise.
- **As-of discipline**: requirements state the law in force at your
  work date; where an instrument is known to be scheduled to change,
  record both regimes with their windows.
- **No hallucinated citations**: every quote must exist in a source file
  you hold; a reviewer with your corpus must be able to verify every
  citation mechanically.
- **Uncertainty is explicit**: open-questions register, referenced from
  the requirements that depend on them.

## Output structure

Plain text/markdown, organized at your discretion, but it must include:
the four deliverables above, an index/entry-point document, and the
open-questions register.

## Success criteria

1. An Odoo dev team can build the module from your requirements alone.
2. Every requirement traces to verbatim official evidence in the corpus.
3. Zero guessed values; all dated data carries effective dates +
   instrument.
4. Coverage map honestly reflects what was read vs pending.
