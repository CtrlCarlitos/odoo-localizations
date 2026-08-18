# SV — Fiscal reporting — Filing calendar & deadline engine: obligation inventory, asuetos, días hábiles

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for El Salvador's filing
calendar and deadline engine (cluster F12) in four layers: the
*Calendario Tributario* (tax calendar — the MH annual publication)
**obligation inventory as DATED DATA** — form → period type →
due-window month, versioned by calendar year and carrying the printed
*Asamblea Legislativa* (Legislative Assembly) modification disclaimer
on every row, with third-party registry reports marked informational;
the **due-day window mechanism as configuration data** — the window
values are UNPINNED (the 2026 calendar's due-day windows are a visual
highlighted-cell layer with no normative anchor in the corpus: SOQ-08),
so the FRs state the config-driven mechanism without hard dates; the
***asueto* (public holiday) table** (2026 legend verbatim) feeding the
shared ***días hábiles* (business days) computation engine** — the
single engine also consumed by the e-invoicing invalidation and OpEsp
deadlines and by the taxation retention-remittance deadline, cited by
FR id and never duplicated here; and the **per-company deadline and
reminder model** keyed to the inventory (period-open generation, asueto
shifting, annual versioning swap, overdue surfacing).

It does **not** cover: the declaration and inform builders themselves
(`01_f07-declaration.md`..`05_f07-annexes-special.md`,
`06_f14-declaration.md`, `07_codes-and-informs.md` — deadline objects
link to those outputs by form code; every other file of this wave
forward-references THIS file for deadlines); the DTE-event deadline
VALUES (`e-invoicing/03_events.md` SV-EINV-FR-103 differentiated
invalidation deadlines and SV-EINV-FR-126 OpEsp first-10-hábiles —
this file supplies only their business-day engine); the
retention-remittance RULE (`taxation/01_isr-framework.md`
SV-TAX-FR-032, routed by `taxation/05_isr-distributions.md`
SV-TAX-FR-149 — same engine, rule owned there); sanction computation
for late filing (CT sanctions territory, not in this wave's evidence —
overdue is flagged, never fined here); and payment processing.

## 2. Legal Basis

Authority rule (S3, binding): the MH *Calendario Tributario 2026*
(30_) IS the primary authority for the obligation inventory and the
asueto legend — a dated annual publication whose every page prints the
Asamblea-modification disclaimer; the due-day WINDOWS are its visual
layer and stay unpinned (SOQ-08 → OQ-001). The engine consumers'
deadlines are anchored in their own files' sources and are cited here
by pointer only (LB-004/LB-005), never restated. Calendar pages are
printed month pages (pp.2-13 = Enero..Diciembre; p.1 = legend).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Calendario Tributario 2026, inventario de obligaciones (verbat): MENSUAL (todos los meses, incl. Enero p.2): "IVA: Declaración y Pago del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios (F-07). RENTA Y OPERACIONES FINANCIERAS: Declaración Mensual de Pago a Cuenta e Impuestos Retenidos de Renta y Agentes Extranjeros (F-14). ESPECÍFICOS Y AD-VALOREM: Declaración de Impuestos Específicos, Ad-Valorem y Contribución Especial (F-06). OTRAS OBLIGACIONES: Estado de Origen y Aplicación de Fondos (F-950) [patrón Enero/Abril/Julio(+Octubre)]. Informe sobre Donaciones (F-960) ... IVA: Informe Mensual de Retención, Percepción o Anticipo a Cuenta de IVA (F-930). IMPRENTAS: Informe Mensual de Documentos Impresos a Contribuyentes Inscritos en IVA (F-945). OTRAS OBLIGACIONES: Informe Mensual de Retención sobre Agentes Extranjeros (F-935)". FEBRERO (p.3): "Informe Anual de Retención del Impuesto sobre la Renta, Ejercicio 2025 (F-910)" + "Informe sobre Distribución o Capitalización de Utilidades, Dividendos o Excedentes y/o Lista de Socios, Accionistas o Cooperados 2025 (F-915)" + "Informe de Notarios por Otorgamiento de Instrumentos que hayan comparecido ante sus Oficios (F-986)" + "Informe Semestral de Proveedores, Clientes, Acreedores y Deudores (F-987)" + F-947/F-948/F-958. MARZO (p.4): F-957 (ventas anuales de licores), F-972 (instituciones financieras), F-983 (inventario), "Dictamen e Informe Fiscal Código Tributario, de las sociedades que tomaron acuerdo de Fusión (Sociedad Absorbente) ... (Art. 134 literal a) Código Tributario) (F-455)" + inscripción de fusión (134 b) + disolución/liquidación (134 c). ABRIL (p.5): "Declaración de Impuesto sobre la Renta y de la Contribución Especial a los Grandes Contribuyentes para el Plan de Seguridad Ciudadana del Ejercicio 2025 (F-11)" + F-971 (Balance General y Estado de Resultados / contabilidad formal) + F-944 (Ganancias y/o Pérdidas de Capital 2025) + F-30 (Bienes Inmuebles 2025) + F-40 (Activos y Pasivos 2025) + F-982 (operaciones paraísos fiscales). MAYO (p.6): "Nombramiento de Auditor Fiscal, según lo establecido en el Art. 131 inciso segundo del Código Tributario para el Ejercicio 2026" + nombramientos de auditor Ley de Servicios Internacionales (nota de ventana MINEC). JULIO (p.7): F-987 segundo semestre. AGOSTO (p.8): auditor-fiscal kin + F-950. CNR/terceros (p.2): "Registro de Propiedad Raíz e Hipotecas: Informe Semestral sobre el Registro de Inmuebles (F-985)" + "REGISTRO DE COMERCIO: Informe Semestral sobre la Constitución, Transformación, Fusión, Disolución o Liquidación de Sociedades (F-975)" + "ALCALDÍAS MUNICIPALES: Informe de Alcaldías (F-995)" + F-990 (importadores de vehículos) | Tax Calendar 2026 obligations inventory (verbatim): MONTHLY core F-07/F-14/F-06/F-930/F-935/F-945 (+F-960 donations; F-950 Jan/Apr/Jul pattern); ANNUAL/SEMIANNUAL anchors — February: F-910 (annual ISR retentions, ejercicio 2025) + F-915 (distributions/shareholder list) + F-986 (notaries) + F-987 (first half) + F-947/F-948/F-958; March: F-957/F-972/F-983 + the F-455 fusión dictamen (CT Art. 134 a) + fusión inscription (b) + disolución/liquidación (c); April: F-11 (ISR + grandes contribuyentes security contribution) + F-971 (balance/income statement) + F-944 (capital gains) + F-30 (real property) + F-40 (assets & liabilities) + F-982 (tax-haven operations); May: auditor-fiscal appointments for ejercicio 2026 (CT Art. 131 second inciso) + LSI auditor appointments (MINEC window); July: F-987 second half; August: auditor kin + F-950; THIRD-PARTY (CNR/alcaldías/importers): F-985/F-975/F-995/F-990 — registry-side informational reports, not taxpayer obligations | `sv/sources/30_Calendario_Tributario_2026.pdf` | pp.1-13 (EVID-185) |
| LB-002 | Calendario Tributario 2026, advertencia (verbat, en cada página): "Estimado Contribuyente, tome en cuenta que las fechas señaladas pueden ser modificadas por la Honorable Asamblea Legislativa" | Tax Calendar 2026 disclaimer (verbatim, every page): "Dear Taxpayer, note that the dates indicated may be modified by the Honorable Legislative Assembly" — the annual-publication + modification disclaimer behind the dated-data versioning of FR-196/FR-207 | `sv/sources/30_Calendario_Tributario_2026.pdf` | every page (EVID-185) |
| LB-003 | Calendario Tributario 2026, p.1 leyenda "Días de asueto" (verbat): "Año Nuevo (1 y 2 Enero) / Semana Santa / Día del Trabajo / Día del Padre / Fiestas Patronales del Salvador del Mundo / Día de la Independencia / Día de los Difuntos / Fiestas Navideñas y Fin de Año"; las cuadrículas mensuales marcan días como asueto por la leyenda; las ventanas de días de presentación (celdas resaltadas) NO extraen como texto | Tax Calendar 2026 p.1 "Días de asueto" (public holidays) legend (verbatim): New Year (1-2 January) / Holy Week / Labor Day / Father's Day / Patron Saint Festivities of El Salvador del Mundo / Independence Day / Day of the Dead / Christmas and Year-End Festivities; month grids mark days as asueto per the legend; the due-day windows (highlighted cells) do NOT extract as text — the asueto set feeding the días-hábiles engine, with exact-date pinning open (OQ-003) | `sv/sources/30_Calendario_Tributario_2026.pdf` | p.1 legend + month grids (EVID-186) |
| LB-004 | Ley ISR, Art. 62 (por referencia, vía `taxation/01_isr-framework.md` LB-027 — el consumidor de remesa): los agentes de retención enteran lo retenido dentro de los diez días hábiles siguientes al cierre del período de la retención | ISR Law Art. 62 (by pointer via the taxation file's LB-027 — the remittance consumer): retention agents remit withheld sums within the ten business days following the end of the retention period — the SV-TAX-FR-032 deadline whose business-day arithmetic runs on THIS file's engine; the rule itself is owned by the taxation file | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 62 p.43 (EVID-104; via taxation/01 LB-027) |
| LB-005 | Normativa de Cumplimiento DTE v2.0, Anexo V + §13.4 (por referencia, vía `e-invoicing/03_events.md` LB-007/LB-005 — los consumidores de eventos): plazos diferenciados de invalidación (CLE/DCLE = primeros 10 días hábiles del mes siguiente al período; NRE/CDE/retorno/OpEsp = 4 días calendario, etc.) y OpEsp dentro de los primeros 10 días hábiles del mes siguiente | DTE Regulation v2.0, Annex V + §13.4 (by pointer via the e-invoicing file's LBs — the event consumers): differentiated invalidation deadlines (CLE/DCLE = first 10 business days of the month following the period; NRE/CDE/retorno/OpEsp = 4 calendar days, etc.) and OpEsp transmission within the first 10 business days of the following month — the SV-EINV-FR-103/SV-EINV-FR-126 deadlines whose hábil-window arithmetic runs on THIS file's engine; the deadline tables are owned by the e-invoicing file | `sv/sources/45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf` | Anexo V pp.123-135 + §13.4 (via e-invoicing/03 LB-007/LB-005; EVID-084/085) |

## 3. Functional Requirements

### 3.1 Obligation inventory (dated data)

- **SV-FREP-FR-195:** The system shall maintain the filing obligation
  inventory as DATED DATA keyed form code → period type → due-window
  month, seeded from the 2026 *Calendario Tributario*: monthly core —
  F-07, F-14, F-06, F-930, F-935, F-945 and the F-960 donations
  inform (every month; the period-to-window-month offset — window
  month follows the period close, as the February annuals listing
  *ejercicio*-2025 reports show — is an inference carried as per-row
  configuration, re-verified in the OQ-001 window pass);
  quarterly-pattern F-950 (Enero/Abril/Julio appearances — FR-197);
  semiannual F-987 (first half due-window February, second half
  July); annual anchors — F-910, F-915, F-986 (+F-947/F-948/F-958)
  due-window February of the year after the *ejercicio* (fiscal
  year); F-455 fusión dictámenes (CT Art. 134 a/b/c) and the
  F-957/F-972/F-983 annuals due-window March; F-11, F-971, F-944,
  F-30, F-40, F-982 due-window April; auditor-fiscal appointments
  (CT Art. 131 second inciso) and LSI auditor appointments (MINEC
  window) due-window May — each row carrying its calendar vintage and
  verbatim source name; annual due-window months are the calendar's
  listing months for the prior ejercicio's reports, never
  recomputed. (LB-001; EVID-185)
- **SV-FREP-FR-196:** The system shall carry the Asamblea disclaimer
  on the inventory as a whole — every dated calendar row is
  contingent on the printed warning "las fechas señaladas pueden ser
  modificadas por la Honorable Asamblea Legislativa" — and shall
  re-date the inventory only from a published calendar/modification:
  a refresh lands as a new vintage (FR-207), never as a silent edit
  of live rows; a calendar year with no loaded vintage is flagged
  stale on every deadline computation of that year.
  (LB-002; EVID-185)
- **SV-FREP-FR-197:** The system shall carry F-950 *Estado de Origen
  y Aplicación de Fondos* (statement of origin and application of
  funds) as an inventory row with period_type = quarterly pattern
  (Enero/Abril/Julio calendar appearances, with an Agosto listing
  kin), its frequency and applicability (whose obligation) left OPEN
  — the row is data with an OQ flag, and no deadline generation
  occurs for it until SOQ-14 resolves (OQ-002).
  (LB-001; EVID-185; SOQ-14)
- **SV-FREP-FR-198:** The system shall mark the third-party registry
  reports of the calendar's CNR/alcaldías block — F-985 (*Registro de
  Propiedad Raíz e Hipotecas* semestral inmuebles inform), F-975
  (*Registro de Comercio* semestral societies inform), F-995
  (alcaldías inform) and F-990 (vehicle importers) — as
  third_party_informational inventory rows: they are carried for
  completeness of the published calendar and generate NO taxpayer
  deadline, reminder or overdue object (they are obligations of the
  registries, not of the taxpayer). (LB-001; EVID-185)

### 3.2 Due-day windows (config-driven mechanism; values unpinned — SOQ-08)

- **SV-FREP-FR-199:** The system shall implement every due-day WINDOW
  as configuration data resolved against the inventory row — the
  window month comes from the inventory (FR-195) and the day rule
  from window configuration — with NO window values hardcoded: the
  2026 calendar's highlighted-cell due-day layer does not extract as
  text and no normative schedule instrument (calendario resolution or
  reglamento) exists in the corpus, so the system states the
  mechanism and ships no dates (SOQ-08 → OQ-001, which owns the
  06-file OQ-005 pointer). (LB-001; LB-003; EVID-186)
- **SV-FREP-FR-200:** The system shall define the window
  configuration schema per obligation × period type with three day
  rules — fixed_day (a day-of-month), day_range (an inclusive
  from-to range within the window month) and first_n_habiles (the
  first N business days of the window month) — plus an OPTIONAL
  taxpayer-segment rule slot for the by-NIT-digit day-assignment
  practice of F-07/F-14: the segment rule is a configuration object
  that is NEVER assumed (no normative anchor in the corpus — SOQ-08);
  an obligation without loaded window configuration computes no due
  date and surfaces a configuration-missing flag instead.
  (LB-001; EVID-186; SOQ-08)
- **SV-FREP-FR-201:** The system shall compute a deadline from a
  loaded window configuration as follows: fixed_day ⇒ due date = that
  day of the window month, shifted per FR-204; day_range ⇒ due date =
  the last day of the range (any day within the range is on time),
  shifted per FR-204; first_n_habiles ⇒ due date = the Nth *día
  hábil* of the window month per the shared engine (FR-203); the
  taxpayer-segment rule, when configured, selects the subject's
  window within the rule's segmentation without changing the
  computation. (LB-001; LB-003; EVID-186)

### 3.3 Asuetos & the shared días-hábiles engine

- **SV-FREP-FR-202:** The system shall maintain the *asueto* table as
  DATED DATA seeded from the calendar's p.1 legend — the 2026 set:
  Año Nuevo (1 y 2 Enero), Semana Santa, Día del Trabajo, Día del
  Padre, Fiestas Patronales del Salvador del Mundo, Día de la
  Independencia, Día de los Difuntos, Fiestas Navideñas y Fin de Año
  — year-keyed with weekends as non-business days by rule, re-seeded
  annually from the published calendar; the legend names the holidays
  but only pins Año Nuevo's exact dates in text, so each year's
  exact-date pinning (which days of that year each named holiday
  occupies, read from the month grids) is an explicit annual data
  load, flagged until completed (OQ-003). (LB-003; EVID-186)
- **SV-FREP-FR-203:** The system shall expose ONE shared días-hábiles
  engine over the asueto table — is_habil(date), next_habil(date),
  add_habiles(date, n) and first_n_habiles(month, n) — as the single
  business-day arithmetic of the localization, consumed by: the
  window computations of FR-201; the e-invoicing invalidation and
  OpEsp deadlines (`e-invoicing/03_events.md` SV-EINV-FR-103 — incl.
  its CLE/DCLE first-10-hábiles rule — and SV-EINV-FR-126); and the
  taxation retention-remittance deadline
  (`taxation/01_isr-framework.md` SV-TAX-FR-032, routed by
  `taxation/05_isr-distributions.md` SV-TAX-FR-149) — the deadline
  VALUES are owned by those FRs and cited by id; no consumer
  re-implements business-day logic and this file never restates
  their deadline tables. (LB-003; LB-004; LB-005; EVID-186;
  cross-ref SV-EINV-FR-103, SV-EINV-FR-126, SV-TAX-FR-032,
  SV-TAX-FR-149)
- **SV-FREP-FR-204:** The system shall shift a computed fixed-day or
  day-range-end due date that falls on an asueto or a weekend to the
  NEXT *día hábil* (next business day), recording the shift on the
  deadline object; *días-hábiles* windows (first_n_habiles,
  add_habiles) exclude asuetos and weekends by construction and are
  never themselves shifted; the shift convention's normative anchor
  (CT general deadline rules) is not in this wave's evidence and
  stays open (OQ-003). (LB-003; EVID-186)

### 3.4 Deadline & reminder model

- **SV-FREP-FR-205:** The system shall generate, per company, one
  deadline object per applicable obligation × period when the period
  opens (monthly core periods open at month start; annual/semiannual
  obligations open at their inventory due-window year; appointment
  obligations open at the appointment year), the due date computed
  per FR-201/FR-204 and the object linking to the matching
  declaration/inform output of files 01-07 by form code (F-07/F-14
  declarations, F-910/F-915/F-930/F-935 informs) when one exists;
  F-950 generates none (FR-197) and third-party rows generate none
  (FR-198). (LB-001; EVID-185)
- **SV-FREP-FR-206:** The system shall surface each deadline with a
  configurable reminder lead (a number of *días hábiles* before the
  due date, computed on the shared engine) and shall flag a deadline
  OVERDUE when its due date passes without a linked filed output —
  the flag is informational with a pointer to the CT sanction regime;
  no sanction amount is computed in this file.
  (LB-001; LB-002; EVID-185)
- **SV-FREP-FR-207:** The system shall swap calendar vintages
  additively: a new-year inventory and asueto table load with
  valid_from = the new calendar year, existing deadlines of prior
  years keep their computed dates (no retroactive rewrite), and the
  year-over-year diff (obligations added/removed, window months
  moved, asuetos changed) is surfaced for review before activation —
  implementing the Asamblea-modification disclaimer of FR-196 as a
  controlled re-dating path rather than an edit.
  (LB-001; LB-002; LB-003; EVID-185; EVID-186)
- **SV-FREP-FR-208:** The system shall scope obligation applicability
  per taxpayer from the calendar's own section classes — *IVA*,
  *renta y operaciones financieras*, *específicos y ad-valorem*,
  *imprentas* (printing houses, F-945), *otras obligaciones*, grandes
  contribuyentes (the F-11 contribution pair), notaries (F-986) —
  as configuration keyed to taxpayer attributes (IVA taxpayer,
  retention agent, printer, grande contribuyente, notario), with the
  calendar's headers as the seed vocabulary and any finer scoping
  rule left to configuration (the calendar prints classes, not
  eligibility rules). (LB-001; EVID-185)

## 4. Data Model

Machine-readable sidecar: DEFERRED until OQ-001 (window values) and
OQ-003 (asueto exact dates) pin data — the seed CSVs
(`filing_obligations_2026.csv`, `asuetos_2026.csv`) ship when those
pin, so no unpinned values masquerade as catalog data. Layer
semantics: Odoo-side computation/bookkeeping data only (wave default
`odoo`; see §5).

**Obligation inventory — l10n_sv.filing.obligation (new; the DATED
DATA home):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| form_code, name_es | char/char | verbatim names of LB-001 | FR-195 |
| period_type | select | monthly · quarterly · semiannual · annual · appointment | FR-195, FR-197 |
| due_window_months | integer list | following-month (monthly core; inferred offset — OQ-001 pass); 2 (F-910/F-915/F-986/F-987-1H); 3 (F-455 + F-957/F-972/F-983); 4 (F-11/F-971/F-944/F-30/F-40/F-982); 5 (auditor appointments); 7 (F-987-2H) | FR-195 |
| applicability_class | char | calendar header class (iva · renta · especificos · imprentas · otras · grandes_contribuyentes · notarios) | FR-195, FR-208 |
| taxpayer_scope | select | taxpayer · third_party_informational (F-985/F-975/F-995/F-990) | FR-198 |
| calendar_vintage, valid_from, source, oq_flag | char/date/char/char | e.g. 2026 · 2026-01-01 · 30_ pp.2-13; F-950 row carries SOQ-14 flag | FR-195, FR-196, FR-197 |

**Window configuration — l10n_sv.filing.window.config:**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| obligation, window_month | m2o/integer | resolved month per inventory row | FR-199 |
| day_rule | select | fixed_day · day_range · first_n_habiles | FR-200 |
| day_params | json | {day} / {from, to} / {n} — values UNPINNED (SOQ-08), loaded as config, never code | FR-200 |
| segment_rule | json, optional | taxpayer-segment rule object (by-NIT-digit practice — unpinned, never assumed) | FR-200, FR-201 |

**Asueto table — l10n_sv.fiscal.asueto (new; the shared engine's data):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| date, name_es | date/char | the LB-003 legend set; exact dates pinned annually from the grids (OQ-003); 2026 pins Año Nuevo = Jan 1-2 in text | FR-202 |
| scope | select | national | FR-202 |
| vintage, source, pinned | char/char/boolean | year-keyed · 30_ p.1 + grids · false until the annual exact-date load completes | FR-202, FR-207 |

**Deadline model — l10n_sv.filing.deadline:**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| company, obligation, period | m2o/m2o/char | monthly M/YYYY · annual ejercicio · appointment year | FR-205 |
| due_date, reminder_at | date/datetime | computed per FR-201; reminder = lead días hábiles before due (FR-206) | FR-205, FR-206 |
| status | select | pending · filed · overdue | FR-205, FR-206 |
| linked_output | m2o (form-code keyed) | F-07/F-14 declarations (files 01/06), F-910/F-915/F-930/F-935 informs (files 04/07) | FR-205 |
| shift_log | char | asueto/weekend shift record when FR-204 applied | FR-204 |

**Shared engine — l10n_sv.fiscal.calendar (service over the asueto
table; single implementation):**

| Method | Semantics | Consumers (by FR id) |
|--------|-----------|----------------------|
| is_habil(date) / next_habil(date) | weekend + asueto exclusion; next business day | FR-201, FR-204 |
| add_habiles(date, n) | n días hábiles forward from basis date | SV-TAX-FR-032 (ten-hábiles remittance; routed by SV-TAX-FR-149) |
| first_n_habiles(month, n) | the Nth día hábil of a month | SV-EINV-FR-103 (CLE/DCLE first-10-hábiles invalidation), SV-EINV-FR-126 (OpEsp), FR-201 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows: none of these FRs touch DTE
generation/transmission (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`); the engine merely
serves the e-invoicing deadlines that DO split, on the client side.
Model names are stable across Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-195 | odoo | l10n_sv.filing.obligation | inventory seed | D12: 2026 calendar vintage (30_); CSV sidecar deferred until OQ-001/OQ-003 pin data; AC-001 |
| FR-196 | odoo | l10n_sv.filing.obligation | vintage + disclaimer flag | Disclaimer printed every page (LB-002); refresh = new vintage only; stale-year flag; AC-004 |
| FR-197 | odoo | l10n_sv.filing.obligation (F-950 row) | period_type=quarterly + oq_flag | SOQ-14 (OQ-002): no deadline generation until resolved; AC-001 |
| FR-198 | odoo | l10n_sv.filing.obligation (third-party rows) | taxpayer_scope | F-985/F-975/F-995/F-990 informational — no deadline/reminder objects; AC-001 |
| FR-199 | odoo | l10n_sv.filing.window.config | mechanism only | SOQ-08 (OQ-001; owns 06-file OQ-005 pointer): no hardcoded dates; config-missing flag; AC-002 |
| FR-200 | odoo | l10n_sv.filing.window.config | day_rule + day_params + segment_rule | Three day rules; by-NIT-digit segment slot never assumed; AC-002 |
| FR-201 | odoo | l10n_sv.filing.deadline (compute) | due_date | fixed_day/day_range shift per FR-204; first_n_habiles via engine; AC-002 |
| FR-202 | odoo | l10n_sv.fiscal.asueto | dated legend set | 2026 legend verbatim (LB-003); annual exact-date load pinned=false until done (OQ-003); AC-003/AC-004 |
| FR-203 | odoo | l10n_sv.fiscal.calendar | is_habil/next_habil/add_habiles/first_n_habiles | THE single engine; consumers cited by id: SV-EINV-FR-103/126, SV-TAX-FR-032 (via SV-TAX-FR-149); no duplication; AC-005 |
| FR-204 | odoo | l10n_sv.filing.deadline | shift_log | Next-día-habil shift for fixed days/range ends; hábil windows never shifted; shift anchor open (OQ-003); AC-003 |
| FR-205 | odoo | l10n_sv.filing.deadline | generation + linked_output | Period-open generation; links files 01-07 outputs by form code; F-950/third-party excluded (FR-197/198); AC-006 |
| FR-206 | odoo | l10n_sv.filing.deadline | reminder_at + status=overdue | Lead in días hábiles (engine-computed); informational sanction pointer, no amounts; AC-006 |
| FR-207 | odoo | l10n_sv.filing.obligation + l10n_sv.fiscal.asueto | vintage swap | Additive valid_from loads; no retroactive rewrite; diff review before activation; AC-004 |
| FR-208 | odoo | l10n_sv.filing.obligation ↔ company profile | applicability_class config | Calendar header classes as seed vocabulary; finer scoping = configuration; AC-001 |

Version-regime notes (D12): the inventory and the asueto table are
DATED annual publications (2026 vintage, 30_) with the
Asamblea-modification disclaimer (FR-196/207); due-day window VALUES
are unpinned configuration (SOQ-08 — OQ-001); exact asueto dates are
an annual load (OQ-003).

## 6. Acceptance Criteria

- **AC-001:** Given the 2026 inventory seed, then the monthly core
  forms (F-07, F-14, F-06, F-930, F-935, F-945, F-960) appear with
  due_window_months = following-month for every month including
  Enero; F-910/F-915/F-986/F-987-1H appear with window month 2,
  F-455 (+F-957/F-972/F-983) with 3, F-11/F-971/F-944/F-30/F-40/
  F-982 with 4, the CT-131 auditor appointments with 5, F-987-2H with
  7; the F-950 row carries the SOQ-14 flag and generates no deadline;
  the F-985/F-975/F-995/F-990 rows carry taxpayer_scope =
  third_party_informational and generate no taxpayer deadline,
  reminder or overdue object (FR-195, FR-197, FR-198, FR-208).
- **AC-002:** Given a PLACEHOLDER window configuration for a monthly
  obligation — window_month = M, day_rule = first_n_habiles,
  day_params = {n: 10} — and an asueto table where two named holidays
  fall inside M on weekdays (placeholder dates), when the deadline is
  computed, then due_date = the 10th día hábil of M counting only
  days that are neither weekend nor asueto (FR-199, FR-200, FR-201,
  FR-203); and given an obligation with NO loaded window
  configuration, then no due date is computed and the
  configuration-missing flag is raised (FR-199, FR-200). No real
  2026 calendar dates are asserted (SOQ-08).
- **AC-003:** Given a placeholder fixed_day window with day_params =
  {day: D} where D falls on an asueto (placeholder date), when the
  deadline is computed, then due_date = the next día hábil after D
  and the shift is recorded in shift_log; and given the same D
  falling on a normal weekday, then due_date = D with no shift
  (FR-204, FR-202, FR-201).
- **AC-004:** Given an active 2026 vintage with computed deadlines
  for June-2026 periods, when a 2027 inventory and asueto table load
  with valid_from = 2027-01-01 (including a moved due-window month
  and a changed asueto in the diff), then every 2026 deadline keeps
  its already-computed date, the 2027 deadlines compute from the new
  vintage, the diff is surfaced for review before activation, and a
  deadline computed for a year with no loaded vintage raises the
  stale-year flag (FR-196, FR-207, FR-202).
- **AC-005:** Given a placeholder asueto falling inside the relevant
  month, when (a) the CLE/DCLE invalidation window of
  SV-EINV-FR-103, (b) the OpEsp window of SV-EINV-FR-126 and (c) the
  ten-días-hábiles remittance due date of SV-TAX-FR-032 are each
  resolved, then all three exclude that asueto through the SAME
  engine instance (l10n_sv.fiscal.calendar) — no consumer ships its
  own business-day table — and this file's deadline values for those
  consumers are nowhere restated (FR-203).
- **AC-006:** Given a deadline with reminder lead = 5 días hábiles
  and due_date D, then reminder_at = the date 5 días hábiles before
  D; and given due_date D passing with no linked filed output, then
  status flips to overdue with the informational CT-sanction pointer
  and no sanction amount (FR-205, FR-206).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-08 (OWNS the 06-file OQ-005 pointer): due-day windows unpinned — the 2026 calendar's windows are a visual highlighted-cell layer (EVID-186) and the by-NIT-digit day-assignment rule for F-07/F-14 has no normative anchor in the corpus. Extract the visual layer (pdfplumber rects / manual read) or acquire the schedule instrument (calendario resolution / reglamento) before deadline FRs get AC-grade dates; until then FR-199/200 ship the config mechanism with placeholder-only ACs (AC-002). | no | Takumi S3 (sources registry) | open |
| OQ-002 | SOQ-14: F-950 *Estado de Origen y Aplicación de Fondos* frequency (quarterly Ene/Abr/Jul? an Agosto appearance exists) and applicability (whose obligation) — FR-197 carries the row as flagged data with no deadline generation until resolved. | no | Takumi S3 (sources registry) | open |
| OQ-003 | Asueto data + shift anchor: (a) exact-date pinning — the p.1 legend names the 2026 holidays but only pins Año Nuevo (1 y 2 Enero) in text; each year's exact dates must be read from the month grids (annual manual load, FR-202 pinned=false until done); (b) the fixed-day next-día-hábil shift convention (FR-204) lacks a corpus anchor — pin against the CT's general deadline rules during the CT matrix re-check before certification. | no | Takumi S3 (CT matrix re-check) | open |
| OQ-004 | Calendar provenance for years ≠ 2026: the 30_ source covers tax year 2026 only; every future vintage (and any mid-year Asamblea modification, per the LB-002 disclaimer) requires acquiring the MH publication — add to the sources-registry watch cadence feeding FR-196/207. | no | Takumi S3 (sources registry) | open |
