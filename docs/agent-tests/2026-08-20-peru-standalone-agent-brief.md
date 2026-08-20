# Peru standalone-agent benchmark brief (2026-08-20)

Benchmark experiment (owner): second instance of the Colombia test —
hand THIS brief alone to a different coding agent in a clean environment.
Intent, scope, deliverables and quality bars only; deliberately NO
method, tooling, file conventions, or process hints from this repo.
Purpose: compare that agent's output against our process-driven result
to evaluate what the method contributes. Everything below the line is
the brief as handed to the other agent.

---

# Mission: Odoo Localization Requirements for Peru

You are producing the complete requirements foundation for an Odoo
localization for Peru. This is a documents deliverable, NOT a coding
task: you will not build the module. A development team will later
implement an Odoo module (target versions 17–20) directly from your
requirements, without access to you.

## Deliverables

1. **Source corpus** — acquire the official source documents (laws,
   legislative decrees, urgent decrees, SUNAT resolutions/superintendencia
   rules, technical manuals, catalogs, XSD/UBL schemas, official guides)
   for every domain in scope. Each document
   must be precisely identified: instrument number, emission date,
   publication/gazette reference, official URL, acquisition date.
   Preserve files as acquired.
2. **Evidence record** — for every requirement, the exact legal or
   technical basis: instrument + article/clause, with the verbatim
   source-language quote plus a short English gloss. Conflicts between
   sources are recorded as such. Anything unclear, ambiguous, or
   unobtainable becomes an open question — never a guess.
3. **Requirements files** — structured, referenceable requirements
   (unique IDs per requirement; each with legal-basis citation and
   acceptance criteria) detailed enough that an Odoo developer could
   implement from them without asking questions.
4. **Coverage map** — per source: fully read / partially read / pending;
   and per requirement: traceability to its evidence.

## Domains in scope

- **Electronic invoicing** (SUNAT regime: comprobantes de pago family —
  facturas, boletas de venta, notas de crédito/débito, tickets;
  authorization/verification mechanisms, XML/UBL structure, CDR
  acceptance, contingencies, resúmenes y comunicaciones, retention
  document "retención electrónica" and percepción documents as evidenced)
- **Indirect tax**: IGV (rates, base rules, exclusions, exonerations),
  ISC (selective consumption tax) mechanics, percepciones y retenciones
  del IGV (agent regimes)
- **Direct tax company-side**: Impuesto a la Renta (general regime),
  retenciones de renta (withholding-agent obligations), pagos a cuenta,
  temporary/mobility taxes only as evidenced
- **Municipal/regional taxes**: Impuesto de Promoción Municipal as part
  of the IGV mechanics; municipal arbitrios/operaciones if evidenced as
  system-relevant
- **Payroll**: salary regime, gratificaciones (July/December),
  CTS (compensación por tiempo de servicio), vacations, social security
  (EsSalud, EPS), AFP/SNP pension,   retención de quinta categoría, RMV (minimum living wage) as salary
  configuration drivers
- **Fiscal books & reporting**: libros electrónicos (electronic books
  regime — ventas, compras, caja), PLE/SLE-PLE formats, IGV monthly
  return (PDT 621) context, PCGA/IFRS context that drives
  chart-of-accounts configuration (PCGE)
- **Company compliance essentials** that affect system configuration
  (RUC identity data, bajas/registration changes, reporting obligations
  calendar, tax calendar cronograma)

Out of scope: consumer-facing storefronts, non-fiscal CRM, HR recruiting.
Borderline items: record as open questions with your recommendation.

## Rules

- **Official sources only** for legal basis (SUNAT, MEF, Presidencia del
  Consejo de Ministros, Diario Oficial El Peruano, INEI, MTPE, SBS,
  ministry resolutions). Third-party accounting blogs/firms may
  help you FIND the instrument; they are never citable as basis.
- **Dated values are configuration, never constants**: tax rates, UIT
  values, minimum living wage, thresholds, caps, coefficient/depreciation
  tables — each captured with its value, effective period, and the
  instrument that sets it, including supersession history (what replaced
  what, when).
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
