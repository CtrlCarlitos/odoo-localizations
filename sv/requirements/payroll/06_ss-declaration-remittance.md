# SV — Payroll — Social-security declaration & remittance: planillas, deadline engine, sanctions, cure workflow, accident reports, record duties

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the Salvadoran social-security declaration and
remittance cycle (cluster P7): the monthly declare-and-pay duty — the
employer declares and pays every cotización (contribution) within the
FIRST TEN días hábiles (business days) of the month following the
devengo (accrual) month or, for subsidy-based cotizaciones, the month
in which the medical license was authorized (09_ Art. 21), with the
due date computed EXCLUSIVELY on the shared días-hábiles engine
consumed by FR id; the ELECTRONIC planilla (declaration sheet) that
one flow must carry BOTH the AFP previsional declaration routed per
Administradora (AFP — the worker-chosen pension-fund administrator)
AND the ISSS obrero-patronal (worker-employer shares) planilla — the
planilla única (unified declaration mechanism) of Art. 27 carried as
a POINTER with its absent spec as an OQ; the sanction architecture as
DISTINCT regimes — the ISSS late-payment recargo (surcharge) of 1%
per month-or-fraction (08_ Art. 33), the SIP late-declaration multa
(fine) ladder 5%/10% plus the 15% non-enrollment multa, the
US$600 → US$1,200 incomplete-declaration escalation, and the
non-payment 20% + 2%/month versus underpayment 10% + 5%/month tracks
(09_ Arts. 143-145) — modeled as exposure records imposed by the SSF
on Administradora notice (Art. 146), with the privileged and
imprescriptible (never-prescribing) credit character of cotizaciones
(09_ Arts. 24-25) as payable notes; the omisión/inconsistencia
(omission/inconsistency) discrepancy-response workflow of Art. 22
(Administradora notice ≤ 20 días hábiles from acréditación — the
crediting of cotizaciones to the affiliate's account — employer cure
≤ 10 días hábiles, MTP inspection/certification, determination and
payment windows); the work-accident report within 48 hours on
Institute forms (08_ Art. 75); and the employer record duties —
planillas, attendance controls, recibos (receipts) — as the
retention/inspection surface (16_ Art. 11 + CT Art. 160).

It does **not** cover: the contribution VALUES themselves — rates,
IBC, caps and regime routing (`05_social-security-contributions.md`:
SV-PAY-FR-066/072 compute the lines this file declares;
SV-PAY-FR-064 owns the AFP routing dimension; SV-PAY-FR-079 owns the
subsidy-month IBC; SV-PAY-FR-071 owns the no-deduction invariant and
the withholding-at-payment mechanic — every value is consumed by id,
never recomputed or restated here); the salary model and earning
matrix (`01_salary-model.md`); minimum wage, jornada/surcharges and
benefits (`02`..`04`); the días-hábiles engine itself
(`fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-203 — one
engine, this file a consumer); the ISR retention-remittance deadline
and its December rule (`taxation/01_isr-framework.md` SV-TAX-FR-032 —
same window family, rule owned there); the F-14 declaration surface
(`fiscal-reporting/06_f14-declaration.md` — a different form; the SS
planilla is not the F-14); contracts, termination and subsidy VALUES
(`07_contracts-termination.md`); and the payroll↔ISR interfaces
(`08_isr-interfaces.md`).

## 2. Legal Basis

Authority order (binding, per master evidence index S4): pensions =
09_ (Ley Integral del Sistema de Pensiones, **D.L. 614**, effective
2022-12-29 — registry title is a misnomer per R24; SAP-era sanction
lore is never cited) for the declaration window, planillas, cure
procedure, sanctions and credit character; ISSS = 08_ (Ley del Seguro
Social, D.L. 1263 — the 1% recargo, the restitution/fine of the
no-deduction violation, the first-class credit privilege and the
48-hour accident report; remittance TIMING is reglementary and the
Reglamento is absent — 08_ OQ-1, carried here as OQ-002); records =
16_ (Decreto 11-2025, Art. 11) + CT Art. 160 (11_); engine and
December-rule cross-anchors consumed by FR id (SV-FREP-FR-203,
SV-TAX-FR-032); sanction parameters are law-text values seeded in a
catalog with article refs (no dated sidecar owned by this file).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley Integral del Sistema de Pensiones (D.L. 614), Art. 21: "Las cotizaciones ... deberán ser declaradas y pagadas por el empleador ... en la Administradora en que se encuentre afiliado cada trabajador. ... el empleador descontará del ingreso base de cotización de cada afiliado, al momento de su pago, el monto de las cotizaciones, y trasladará dichos importes, junto con la correspondiente a su aporte, a las Administradoras respectivas. La declaración y pago deberán efectuarse dentro de los diez primeros días hábiles del mes siguiente a aquél en que se devengaron los ingresos afectos, o a aquél en que se autorizó la licencia médica...". "Todos los empleadores deberán elaborar y remitir la planilla de declaración de cotizaciones previsionales y la planilla de cotización obrero-patronales del Régimen de Enfermedad, Maternidad y Riesgos Profesionales del ISSS por medios electrónicos..." | Cotizaciones are declared AND paid by the employer at the Administradora where each worker is affiliated; the employer withholds each affiliate's cotizaciones at payment of the IBC and transfers them, together with its own share, to the respective Administradoras; declaration and payment fall within the FIRST TEN días hábiles of the month following the month the affected income was accrued, OR the month the medical license was authorized; ALL employers must elaborate and remit electronically BOTH the pension (previsional) declaration planilla and the ISSS obrero-patronal planilla of the Enfermedad/Maternidad/Riesgos Profesionales regime | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 21 pp.10-11 (EVID-198) |
| LB-002 | Ley Integral del Sistema de Pensiones, Art. 27 (gloss-level; verbatim truncated in the evidence extract — "deberá crearse un..."): the law orders the creation of a unified planilla mechanism (planilla única) for the declaration/payment of cotizaciones; its layout, format and channels are NOT in the corpus (Reglamento del D.L. 614 + BCR Normas Técnicas unacquired — 09_ OQ-2 kin) | A unified declaration mechanism (planilla única) shall be created — carried as a POINTER only: no layout, file format or submission channel is invented (OQ-001) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 27 p.14 (EVID-198) |
| LB-003 | Ley Integral del Sistema de Pensiones, Art. 22 (gloss-level per evidence; windows as extracted): omission/inconsistency procedure — the Administradora notices the employer within TWENTY días hábiles after acréditación; the employer cures within TEN días hábiles; uncured cases go to MTP (Ministerio de Trabajo y Previsión Social) inspection and certification; debt determination within the twenty-plus-ten días hábiles window; payment of the determined debt within TEN días hábiles | The omission/inconsistency cure chain: Administradora notice ≤ 20 días hábiles post-acréditación → employer cure ≤ 10 días hábiles → MTP inspection → certification → determination (20+10 días hábiles) → payment (10 días hábiles) — the discrepancy-response workflow's stage windows (anchor composition as-extract, OQ-003) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 22 pp.11-12 (EVID-198) |
| LB-004 | Ley Integral del Sistema de Pensiones, Arts. 23-25 (gloss/verbatim mix): Art. 23 — cobro administrativo starts ≤ 30 days, exhausted at 90 days without payment or a broken two-month commitment, then cobro judicial; Art. 24 — the deuda (debt) is supported by título ejecutivo (executory instrument) and is "irrenunciable e imprescriptible"; Art. 25 (verbatim): "Las cotizaciones constituyen créditos privilegiados de conformidad con el artículo 121 del Código de Trabajo." | The collection chain (administrative → judicial, ejecutive instrument); the cotización debt may NOT be waived and NEVER prescribes; cotizaciones are privileged credits per CT Art. 121 — carried as payable classifications/notes, the collection actions belonging to the Administradora | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 23 p.12 · Art. 25 p.14; Art. 24 within the span, not separately pinned (EVID-198) |
| LB-005 | Ley Integral del Sistema de Pensiones, Art. 143 (late declaration; per evidence extract): declaration of cotizaciones after the deadline — multa 5% de las cotizaciones dejadas de percibir when made up to twenty days late; 10% beyond twenty days; non-inscription of workers (Art. 8 inc. 3º registration duty) — multa 15% | SIP late-DECLARATION fines: 5% of the cotizaciones the Administradora failed to receive (dejadas de percibir) if declared ≤ 20 days late, 10% if > 20 days; 15% for workers never enrolled — a DECLARATION-ladder regime kept distinct from payment sanctions and from the ISSS recargo (day-type as-extract: plain días, OQ-003) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 143 p.58 (EVID-198) |
| LB-006 | Ley Integral del Sistema de Pensiones, Art. 144 (per evidence extract): incomplete or erroneous declaration gravely prejudicing an affiliate's account — multa US$600; escalating if not cured within fifteen days (extract "+$1,200"; wave binding reading: the fine becomes US$1,200 — OQ-003 re-verification) | Incomplete/erroneous declaration fine: US$600, escalating to US$1,200 when the defect is not cured within 15 days | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 144 p.58 (EVID-198) |
| LB-007 | Ley Integral del Sistema de Pensiones, Art. 145 (non-payment; per evidence extract): absolute omission of payment — multa 20% + recargo moratorio 2% per month-or-fraction, plus lost rentabilidad (foregone yield) and the employer-side Art. 16-inc. 2º cotización; underpayment (pago parcial/inferior) — multa 10% + recargo 5% per month-or-fraction | SIP payment sanctions: non-payment = 20% fine + 2%/month-or-fraction surcharge (+ flagged non-computed legs: lost yield, the Art. 16 inc. 2º employer leg); underpayment = 10% fine + 5%/month-or-fraction surcharge — two distinct tracks never blended | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 145 p.59 (EVID-198) |
| LB-008 | Ley Integral del Sistema de Pensiones, Art. 146 (gloss-level per evidence): the sanctions of Arts. 143-145 are imposed by the SSF (Superintendencia del Sistema Financiero — the financial-system superintendent) on notice of the Administradora | Sanctions are imposed by the SSF upon Administradora notice — the system's sanction records are EXPOSURE (estimates) until an imposition notice is recorded; appeal/payment-channel mechanics are absent from the corpus (OQ-003) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 146 p.59 (EVID-198) |
| LB-009 | Ley del Seguro Social (D.L. 1263), Art. 33, incisos 1º/3º/4º: "Las cuotas de los patronos no podrán ser deducidas en forma alguna de los salarios de los asegurados. El patrono que infringiere esta disposición será sancionado con una multa de cien a quinientos colones, sin perjuicio de la restitución..." "El patrono estará obligado a enterar al Instituto las cuotas de sus trabajadores y las propias, en el plazo y condiciones que señalen los Reglamentos. El pago de cuotas en mora se hará con un recargo del uno por ciento, por cada mes o fracción de mes de atraso." (4º, Art. 99 public payers): "estarán obligados a retener las respectivas cotizaciones y remitirlas al Instituto con las planillas correspondientes..." | The employer's own quotas may never be deducted from insured salaries — violation = fine ("cien a quinientos colones" — a COLON-ERA historical print, never converted to USD) PLUS RESTITUTION of the deducted amounts; the employer must remit both share sets to the Institute within the Reglamento's terms (reglementary timing — absent, OQ-002); late cuotas carry a recargo of 1% per month-OR-FRACTION of delay; public Art.-99 payers withhold and remit with the corresponding planillas | `sv/sources/08_Ley_ISSS.pdf` | Art. 33 p.12 (EVID-195) |
| LB-010 | Ley del Seguro Social, Art. 36: a) "Las certificaciones del Director sobre sumas adeudadas al Instituto constituyen título ejecutivo"; b) ISSS credits = "privilegio de créditos de primera clase, con preferencia absoluta sobre cualesquiera otros, excepto ... salarios" | ISSS credits are FIRST-CLASS privileged with absolute preference over all others EXCEPT salary credits; Director certifications are executory instruments — the ISSS-side privilege note beside 09_ Art. 25's CT-121 incorporation | `sv/sources/08_Ley_ISSS.pdf` | Art. 36 pp.12-13 (EVID-195) |
| LB-011 | Ley del Seguro Social, Art. 75 (per evidence): patronos "obligados a informar al Instituto los accidentes de trabajo ... dentro de las cuarenta y ocho horas siguientes de acaecido el hecho", on Institute forms, filable at the Alcaldía (municipal office) where no ISSS office exists | Employers must report work accidents to the Institute within FORTY-EIGHT HOURS of the event, on Institute forms (form templates absent from the corpus — OQ-006), filable at the Alcaldía where the locality has no ISSS office | `sv/sources/08_Ley_ISSS.pdf` | Art. 75 p.21 (EVID-195) |
| LB-012 | Decreto 11-2025 (Tarifas de Salarios Mínimos), Art. 11: employers "deberán llevar y exhibir registros, planillas de pago de salarios, controles de asistencia, recibos, documentos o constancias necesarias para comprobar que pagan a sus trabajadores los salarios mínimos y prestaciones" | Employers must keep and EXHIBIT records, salary-payment planillas, attendance controls, recibos and the documents/constancias necessary to prove they pay the SMM and prestaciones — the payroll record-retention/audit duty (no retention period stated — OQ-007) | `sv/sources/16_Salarios_Minimos_2025.pdf` | Art. 11 p.20 (EVID-192) |
| LB-013 | Código de Trabajo, Art. 160 (gloss-level per evidence, with the Arts. 149-158 Consejo context): employer obligations regarding Consejo Nacional de Salario Mínimo access — the Consejo's inspection powers include FREE ACCESS to workplaces and the right to examine and copy planillas y recibos | Labor-authority inspection access: the record set of LB-012 must be produced for examination/copying — the audit surface's export/read path (CT-side anchor of the inspection duty) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 160 p.38; Arts. 149-158 context (EVID-208) |

Notes (LB-level, not FRs): (i) the "cien a quinientos colones" fine
of 08_ Art. 33 inc. 1º is a colon-era historical print — it is
recorded as reference text only and is NEVER converted, indexed or
posted as a USD amount (OQ-005). (ii) 08_ Art. 33 inc. 3º defers the
ISSS remittance TIMING to the Reglamento (absent — 08_ OQ-1); the
operative reading here is the unified window of 09_ Art. 21 read with
its own electronic-planilla mandate and the Art. 27 planilla única
(OQ-002 owns the re-anchor). Version regime (D12): sanction
percentages and the recargo rate are law-text values (D.L. 614
effective 2022-12-29; D.L. 1263 stable per its reform tail through
D.L. 45-1994 — 08_ OQ-2 watch); the US$600/US$1,200 amounts are
statutory text values; none is a dated print needing a sidecar —
they seed the sanction-type catalog with article refs (FR-094).

## 3. Functional Requirements

### 3.1 Declaration, window and the electronic planilla

- **SV-PAY-FR-086:** The system shall schedule, for every month in
  which the employer has cotizaciones devengadas, ONE social-security
  declaration-and-payment obligation covering the SIP cotizaciones
  and the ISSS cuotas, due within the FIRST TEN días hábiles of the
  following month — the due date computed EXCLUSIVELY as
  first_n_habiles(following_month, 10) on the shared engine
  SV-FREP-FR-203 (consumed by id; this file never restates or
  re-implements business-day arithmetic), with the per-worker values
  and the withholding-at-payment mechanic consumed by id from
  `05_social-security-contributions.md` (SV-PAY-FR-066/071/072 —
  never recomputed here). (LB-001; EVID-198; cross-ref SV-FREP-FR-203,
  SV-PAY-FR-066, SV-PAY-FR-071, SV-PAY-FR-072)
- **SV-PAY-FR-087:** The system shall generate the monthly
  declaration as an ELECTRONIC remittance carrying BOTH regimes in
  one flow — the planilla de declaración de cotizaciones
  previsionales (SIP pension declaration) AND the planilla de
  cotización obrero-patronal of the ISSS
  Enfermedad/Maternidad/Riesgos Profesionales regime — with SIP lines
  ROUTED per Administradora: each worker's cotización lines group
  under the AFP of the worker's affiliation record (the routing
  dimension of SV-PAY-FR-064), while the ISSS leg carries the
  obrero-patronal cuotas of the ISSS-regime workers; the single-flow
  mechanism is the planilla única of Art. 27, carried as a POINTER
  ONLY — its spec is absent from the corpus (OQ-001), so the system
  exports the structured declaration data (per-worker per-regime
  lines with bases and both shares) and invents NO layout, file
  format or submission channel. (LB-001; LB-002; EVID-198; cross-ref
  SV-PAY-FR-064)
- **SV-PAY-FR-088:** For cotizaciones whose base is a subsidy (the
  subsidy-month IBC of SV-PAY-FR-079, consumed by id), the system
  shall anchor the declare-and-pay window to the month in which the
  medical license was AUTHORIZED (the "mes ... en que se autorizó la
  licencia médica" anchor of Art. 21): the affected lines join the
  declaration cohort of that month and their due date is the first
  ten días hábiles of the FOLLOWING month, computed on the same
  engine — never the devengo month when the two differ.
  (LB-001; EVID-198; cross-ref SV-PAY-FR-079, SV-FREP-FR-203)
- **SV-PAY-FR-089:** The system shall apply the first-ten-hábiles
  window UNIFORMLY to every period — December cotizaciones are due
  within the first ten días hábiles of January — and shall implement
  NO December-specific deferral or special rule for social security
  (none exists in the corpus); the ISR retention-remittance deadline
  of the same ten-hábiles window family and its December rule (Ley
  ISR Art. 62) are OWNED by `taxation/01_isr-framework.md`
  SV-TAX-FR-032 and are cited by id here, never restated or
  imported. (LB-001; EVID-198; cross-ref SV-TAX-FR-032,
  SV-FREP-FR-203)

### 3.2 Sanctions and mora (distinct regimes)

- **SV-PAY-FR-090:** The system shall accrue the ISSS late-payment
  recargo of ONE PERCENT per month-or-fraction of delay on cuotas
  paid after the applicable window — a distinct ISSS-regime charge,
  never merged with SIP sanctions: the accrual runs from the window
  close to the payment date, each started month counts as a full
  month, and the charge posts per declaration on the total late
  cuotas. (LB-009; EVID-195)
- **SV-PAY-FR-091:** The system shall compute the SIP
  late-DECLARATION multa on cotizaciones declared after the window
  close: 5% of the cotizaciones dejadas de percibir when the
  declaration is made up to twenty days late, 10% beyond twenty days
  — plus the 15% multa for non-inscription of workers (breach of the
  SV-PAY-FR-064 registration duty) — each on its own basis and
  recorded as a DECLARATION-ladder exposure, kept distinct from the
  payment tracks and from the ISSS recargo (day-type of the ladders
  as-extract — OQ-003). (LB-005; EVID-198; cross-ref SV-PAY-FR-064)
- **SV-PAY-FR-092:** The system shall flag an incomplete or
  erroneous declaration that gravely prejudices an affiliate's
  account and open a cure-window exposure: multa US$600 from notice,
  ESCALATING to US$1,200 when the defect is not cured within FIFTEEN
  days (wave binding reading of the "+$1,200" escalation;
  re-verification OQ-003), with the cure tracked on the same case
  record. (LB-006; EVID-198)
- **SV-PAY-FR-093:** The system shall compute the two SIP PAYMENT
  tracks, never blended: absolute non-payment of cotizaciones =
  multa 20% of the omitted cotizaciones PLUS recargo 2% per
  month-or-fraction, together with the lost-rentabilidad and the
  employer-side Art. 16-inc. 2º cotización legs carried as FLAGGED
  NON-COMPUTED exposure components (formulas absent — OQ-004);
  underpayment = multa 10% of the underpaid amount PLUS recargo 5%
  per month-or-fraction. (LB-007; EVID-198)
- **SV-PAY-FR-094:** The system shall model every sanction of
  FR-090..093 as an EXPOSURE record with regime-tagged accrual legs
  (ISSS recargo vs SIP multa+recargo), month-or-fraction semantics
  (any started month counts in full — 3.5 months accrue 4), and
  sanction parameters loaded from a seeded sanction-type catalog
  carrying its article refs (no code constants); status is
  `estimated` at detection and becomes `imposed` ONLY when an
  Administradora/SSF notice is recorded (the Art. 146 imposition on
  notice) — an estimate is never presented as an imposed sanction,
  and the lost-rentabilidad leg is never computed (OQ-004).
  (LB-005; LB-006; LB-007; LB-008; LB-009; EVID-198; EVID-195)
- **SV-PAY-FR-095:** The system shall classify every cotización
  payable as a PRIVILEGED credit (CT Art. 121 as incorporated by
  09_ Art. 25; ISSS cuotas additionally first-class per 08_ Art. 36,
  behind salary credits only) and as irrenunciable e
  imprescriptible (09_ Art. 24 — the debt may not be waived and
  NEVER prescribes): no automatic prescription, aging write-off or
  cancellation job may ever clear an SS payable — only an explicit
  case resolution can; the cobro administrativo → judicial chain
  (Art. 23: start ≤ 30 days; exhaustion at 90 days without payment
  or a broken two-month commitment; ejecutive instrument) is mirrored
  as collection-stage data on the payable, the collection actions
  belonging to the Administradora/Institute, never the payroll
  system. (LB-004; LB-010; EVID-198; EVID-195)
- **SV-PAY-FR-096:** When a violation of the employer-share
  no-deduction invariant (OWNED by SV-PAY-FR-071) is detected —
  employer quotas charged to workers under any figure — the system
  shall open a restitution case computing the FULL restitution of
  every deducted employer-share amount to the affected workers, per
  affected payslip, with no prescription bar (FR-095); the
  accompanying "cien a quinientos colones" fine is recorded ONLY as
  a historical-print reference — never converted, indexed or posted
  as a USD amount (OQ-005). (LB-009; EVID-195; cross-ref
  SV-PAY-FR-071)

### 3.3 Omisión/inconsistencia discrepancy-response workflow (Art. 22)

- **SV-PAY-FR-097:** The system shall implement the
  discrepancy-response intake: a recorded Administradora notice
  (omission or inconsistency in a declaration) carries the
  acréditación date, validates the notice window (a notice is due
  within TWENTY días hábiles of acréditación — later notices are
  flagged, not rejected), and opens an employer CURE task due within
  TEN días hábiles of the notice (both windows computed on
  SV-FREP-FR-203), tracking the corrected declaration/payment that
  cures the case. (LB-003; EVID-198; cross-ref SV-FREP-FR-203)
- **SV-PAY-FR-098:** On an uncured discrepancy, the system shall
  advance the case through the Art. 22 chain — MTP inspection,
  certification, debt determination within the twenty-plus-ten
  días-hábiles window and payment of the determined debt within TEN
  días hábiles — as staged case data with engine-computed stage
  deadlines (the 20+10 anchor composition carried as-extract,
  OQ-003) and the determination amount recorded from the
  certification; the inspection and certification acts are external
  and only mirrored, never generated. (LB-003; EVID-198)

### 3.4 Work-accident reporting (08_ Art. 75)

- **SV-PAY-FR-099:** The system shall flag every registered work
  accident for INSTITUTE reporting within FORTY-EIGHT HOURS of the
  event: one report record per accident with due_at = accident
  datetime + 48h, prepared on Institute forms (form templates absent
  from the corpus — OQ-006), filable at the Alcaldía where the
  locality has no ISSS office (channel selection), and a late flag
  when the filing timestamp exceeds due_at.
  (LB-011; EVID-195)

### 3.5 Employer records and inspection surface

- **SV-PAY-FR-100:** The system shall maintain the employer record
  duties as an audit surface linked to each payslip run: salary
  payment planillas, attendance controls, recibos and the
  documents/constancias necessary to prove SMM and prestaciones
  compliance (kept AND exhibited per 16_ Art. 11), with an
  inspection-export view exposing the full set for labor-authority
  access (Consejo/inspection free access, examine and copy planillas
  y recibos per CT Art. 160); NO retention period is invented — none
  appears in the corpus (OQ-007) — so no auto-purge path ships.
  (LB-012; LB-013; EVID-192; EVID-208)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in
the client (wave default `odoo`; see §5). This file owns NO dated
sidecar: sanction parameters are law-text values seeded in the
sanction-type catalog with article refs; every consumed value
(bases, shares, routing, engine) arrives by FR id.

**Declaration — l10n_sv.pay.ss.declaration (new) + lines:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.ss.declaration (new) | company · period | m2o · char (M/YYYY) | one per devengo month | FR-086 |
| l10n_sv.pay.ss.declaration | due_date · status | date (computed) · select | due = first_n_habiles(month+1, 10) via SV-FREP-FR-203 (l10n_sv.fiscal.calendar); status: draft · declared · paid · overdue | FR-086, FR-089 |
| l10n_sv.pay.ss.declaration.line (new) | worker · regime · afp | m2o · select · m2o | regime: sip · isss; afp on SIP lines = the sv_pay_afp_id routing of SV-PAY-FR-064 | FR-087 |
| l10n_sv.pay.ss.declaration.line | base · worker_share · employer_share | monetary (consumed) | consumed from payslip lines per SV-PAY-FR-066/072 — never recomputed | FR-086 |
| l10n_sv.pay.ss.declaration.line | window_anchor · window_month · line_due_date | select · char · date | anchor: devengo_month · license_month; cohort + due of the anchor month | FR-088 |

**Sanctions — l10n_sv.pay.ss.sanction (new) + catalog:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.ss.sanction.type (new catalog) | type · multa_pct · recargo_pct · fixed_amounts · source_article | char · float · monetary · char | isss_recargo (1%) · sip_late_decl (5/10) · sip_nonenrollment (15) · sip_incomplete (600→1200) · sip_nonpayment (20+2) · sip_underpay (10+5) · nodeduction_case — article-ref seeded, no code constants | FR-090..094, FR-096 |
| l10n_sv.pay.ss.sanction (new) | declaration · regime_tag · basis_amount | m2o · select · monetary | regime_tag: isss · sip; basis per type (late cuotas / cotizaciones dejadas de percibir / omitted / underpaid amount) | FR-090..093 |
| l10n_sv.pay.ss.sanction | months_or_fraction · recargo_amount · multa_amount · fixed_amount | integer (computed) · monetary | month-or-fraction: any started month counts in full | FR-090, FR-092..094 |
| l10n_sv.pay.ss.sanction | extra_legs | boolean flags | lost_rentabilidad · art16_inc2_leg (non-computed, OQ-004); restitution lines on nodeduction_case | FR-093, FR-096 |
| l10n_sv.pay.ss.sanction | status · imposition_ref · cure_due | select · char · date | estimated · imposed · paid; Administradora/SSF notice (Art. 146); cure_due = notice + 15 días (incomplete type) | FR-092, FR-094 |

**Discrepancy workflow — l10n_sv.pay.ss.discrepancy (new):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.ss.discrepancy (new) | administradora · declaration · worker | m2o | the noticed declaration/affiliate | FR-097 |
| l10n_sv.pay.ss.discrepancy | acreditacion_date · notice_date · notice_window_ok | date · date · boolean (computed) | notice ≤ 20 días hábiles post-acréditación (engine) | FR-097 |
| l10n_sv.pay.ss.discrepancy | cure_due · stage | date (computed) · select | notice + 10 días hábiles; stage: noticed · cured · inspection · certified · determined · paid | FR-097, FR-098 |
| l10n_sv.pay.ss.discrepancy | determination_due · payment_due · determined_amount | date · date · monetary | 20+10 días hábiles window (as-extract, OQ-003); determination + 10 días hábiles; amount from certification | FR-098 |

**Accident reporting — l10n_sv.pay.accident.report (new):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.accident.report (new) | worker · accident_at · due_at | m2o · datetime · datetime (computed) | due_at = accident_at + 48h | FR-099 |
| l10n_sv.pay.accident.report | channel · form_ref · status | select · char · select | channel: isss_office · alcaldia; status: pending · filed · late | FR-099 |

**Records / payable character:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.record.doc (new) | run · doc_type · attachment | m2o (hr.payslip.run) · select · m2o | doc_type: planilla · asistencia · recibo · constancia | FR-100 |
| hr.payslip.run | record_docs (o2m) + inspection export action | — | the CT-Art.-160 access surface; no retention period (OQ-007) | FR-100 |
| SS payable (account.move) | sv_pay_ss_privileged · sv_pay_ss_no_prescribe | boolean (defaults true on SS payables) | privileged (CT 121 / first-class) + irrenunciable/imprescriptible; cobro-chain stage char | FR-095 |

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native — every FR maps
`odoo`; no SaaS rows are introduced because none of these FRs touch
DTE generation/transformation (the only architecture-split surface
per `shared/docs/saas-thin-client-architecture.md` D2). Model names
are stable across Odoo 17/18/19/20; the only external service
consumed is the shared business-day engine, read by id.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-086 | odoo | l10n_sv.pay.ss.declaration | due_date via l10n_sv.fiscal.calendar | Art. 21 first-10-hábiles; engine = SV-FREP-FR-203 by id; values consumed from 05 FR-066/071/072 |
| FR-087 | odoo | l10n_sv.pay.ss.declaration.line | regime + afp grouping; structured export | Art. 21 electronic both-regime planilla; Art. 27 planilla única = pointer only (OQ-001); routing from sv_pay_afp_id (05 FR-064) |
| FR-088 | odoo | l10n_sv.pay.ss.declaration.line | window_anchor = license_month | Art. 21 license clause; subsidy IBC consumed from 05 FR-079 |
| FR-089 | odoo | l10n_sv.pay.ss.declaration (window compute) | uniform window every month | No SS December rule exists; ISR December kin = SV-TAX-FR-032 by id, never restated |
| FR-090 | odoo | l10n_sv.pay.ss.sanction (isss_recargo) | 1% × months-or-fraction | 08_ Art. 33; ISSS regime — never blended with SIP tracks |
| FR-091 | odoo | l10n_sv.pay.ss.sanction (sip_late_decl / sip_nonenrollment) | 5/10% ladder + 15% | Art. 143; declaration ladder ≠ payment tracks; day-type as-extract (OQ-003) |
| FR-092 | odoo | l10n_sv.pay.ss.sanction (sip_incomplete) | fixed 600 → 1200 + cure_due 15 días | Art. 144; escalation reading bound to OQ-003 re-verification |
| FR-093 | odoo | l10n_sv.pay.ss.sanction (sip_nonpayment / sip_underpay) | 20+2 / 10+5 tracks | Art. 145; rentabilidad + Art. 16-inc.2º legs flagged non-computed (OQ-004) |
| FR-094 | odoo | l10n_sv.pay.ss.sanction + .type catalog | estimated → imposed lifecycle | Art. 146 (SSF on notice); month-or-fraction semantics; parameters catalog-seeded with article refs |
| FR-095 | odoo | account.move (SS payables) | sv_pay_ss_privileged · sv_pay_ss_no_prescribe + stage | 09_ Arts. 23-25; 08_ Art. 36; write-off/prescription jobs excluded by flag |
| FR-096 | odoo | l10n_sv.pay.ss.sanction (nodeduction_case) | restitution computation | 08_ Art. 33 inc. 1º; invariant owned by 05 FR-071; colones fine historical-print only (OQ-005) |
| FR-097 | odoo | l10n_sv.pay.ss.discrepancy | notice intake + cure_due | Art. 22; 20-hábiles notice window check + 10-hábiles cure on SV-FREP-FR-203 |
| FR-098 | odoo | l10n_sv.pay.ss.discrepancy (stages) | inspection → certified → determined → paid | Art. 22 chain; external acts mirrored only; 20+10 anchors as-extract (OQ-003) |
| FR-099 | odoo | l10n_sv.pay.accident.report | due_at = accident_at + 48h; channel | 08_ Art. 75; Institute forms absent (OQ-006); Alcaldía channel where no ISSS office |
| FR-100 | odoo | l10n_sv.pay.record.doc + hr.payslip.run | doc_type set + inspection export | 16_ Art. 11; CT Art. 160; no retention period invented (OQ-007) |

Version-regime notes (D12): the sanction catalog seeds law-text
values — D.L. 614 vintages (Arts. 143-145, effective 2022-12-29) and
the D.L. 1263 recargo (stable per the reform tail through
D.L. 45-1994 — 08_ OQ-2 watch); the US$600/US$1,200 amounts are
statutory text, not prints; the colon-era fine stays
historical-reference text only (OQ-005). Re-dating happens only on
instrument acquisition via the catalog's source_article re-seed.

## 6. Acceptance Criteria

- **AC-001:** Given a declaration month whose following month M+1
  opens with four non-business days among its first thirteen
  calendar days (two weekend pairs — placeholder dates) so that
  only nine días hábiles elapse by calendar day 13 (13 − 4 = 9),
  then due_date = the 10th día hábil = the 14th calendar day of
  M+1 — the deadline lands beyond calendar day 13, pushed past
  the 10th calendar day by the non-business days, computed
  exclusively by SV-FREP-FR-203's first_n_habiles(M+1, 10), and
  the payroll module ships no business-day table of its own
  (FR-086; cross-ref SV-FREP-FR-203).
- **AC-002:** Given a March declaration with five workers — three
  affiliated to AFP-1, one to AFP-2 (routing per SV-PAY-FR-064) and
  one Art.-99 public-regime worker — then ONE declaration object
  carries BOTH regimes: SIP lines grouped into two per-AFP
  previsional-planilla blocks and the ISSS obrero-patronal leg for
  the ISSS-regime workers; the export emits the structured
  per-worker lines (bases, both shares) and invents no layout
  (planilla-única spec absent — OQ-001) (FR-087).
- **AC-003:** Given a worker whose May subsidy IBC (per
  SV-PAY-FR-079) rests on a medical license authorized 3-June, then
  the cotización lines on that subsidy join the JUNE cohort (anchor
  = license-authorization month) and are due within the first ten
  días hábiles of JULY — not June's window — while the ordinary May
  devengo lines stay in the May cohort (FR-088).
- **AC-004:** Given December-2026 cotizaciones, then due_date = the
  10th día hábil of January-2027 (uniform window; no December
  deferral exists for social security), and the ISR retention
  December rule (Ley ISR Art. 62) is nowhere replicated here — it is
  consumed by id from SV-TAX-FR-032 only (FR-089).
- **AC-005:** Given ISSS cuotas US$1,000.00 paid three and a half
  months after the window close, then the recargo accrues 1% × 4
  (month-or-fraction: the half month counts in full) = US$40.00,
  recorded as an ISSS-regime exposure leg never blended with SIP
  sanctions (FR-090, FR-094).
- **AC-006:** Given SIP cotizaciones US$5,000.00 never paid, at
  three and a half months, then the non-payment exposure shows
  multa 20% = US$1,000.00 plus recargo 2% × 4 = US$400.00, with the
  lost-rentabilidad and Art. 16-inc. 2º legs as flagged
  non-computed components (OQ-004) — computed exposure
  US$1,400.00, status `estimated` (FR-093, FR-094).
- **AC-007:** Given the same US$5,000.00 obligation with
  US$4,000.00 paid on time and US$1,000.00 omitted
  (underpayment) at two months and ten days, then the UNDERPAYMENT
  track applies: multa 10% of US$1,000.00 = US$100.00 plus recargo
  5% × 3 = US$150.00 — the 20%+2% non-payment track is never applied
  to an underpayment (FR-093).
- **AC-008:** Given cotizaciones US$8,000.00 declared (a) fifteen
  days and (b) twenty-five days after the window close, then multa =
  5% = US$400.00 and 10% = US$800.00 respectively; and a
  never-enrolled worker (SV-PAY-FR-064 duty breached) with
  cotizaciones US$500.00 → 15% = US$75.00 — the declaration ladder
  never merges with the payment tracks or the ISSS recargo
  (FR-091).
- **AC-009:** Given an erroneous declaration gravely prejudicing an
  affiliate's account, then the exposure opens at US$600.00 with
  cure_due = notice + 15 days; cured on day 10 → it stays
  US$600.00; uncured on day 16 → US$1,200.00 (FR-092; escalation
  reading per OQ-003).
- **AC-010:** Given the AC-006 exposure detected at window close,
  then its status is `estimated` with the statutory formulas and no
  imposition claim; when an SSF/Administradora notice is recorded
  (Art. 146), status flips to `imposed` with the notice reference
  and the accrual recomputes to the imposition date (FR-094).
- **AC-011:** Given acréditación 2026-07-01 (placeholder) and an
  Administradora notice received 2026-07-08 (inside the
  twenty-días-hábiles notice window, engine-checked), then cure_due
  = 2026-07-08 + 10 días hábiles; a cure (corrected declaration +
  payment) filed in time closes the case at stage `cured`, otherwise
  it advances `inspection → certified → determined` with
  determination_due = acréditación + 20 + 10 días hábiles
  (as-extract composition, OQ-003) and payment_due = determination
  + 10 días hábiles (FR-097, FR-098).
- **AC-012:** Given a detected pass-through of US$100.00 of the
  employer ISSS share into a worker's salary (violation of the
  SV-PAY-FR-071 invariant), then a restitution case opens for
  US$100.00 repayable to the worker with no prescription bar
  (FR-095), and the "cien a quinientos colones" fine is recorded as
  historical print only — never converted or posted in USD (FR-096).
- **AC-013:** Given a work accident at 2026-06-05 14:30, then the
  report record's due_at = 2026-06-07 14:30 (48 hours), channel =
  Institute form (template absent — OQ-006) with the Alcaldía option
  where the locality has no ISSS office; a filing recorded at
  2026-06-08 08:00 raises the late flag (FR-099).
- **AC-014:** Given a February payslip run, then the audit surface
  exposes the linked planilla de pago, attendance-control and recibo
  documents per worker, and the inspection export returns the full
  set for CT-Art.-160 authority access — with no retention-period
  auto-purge anywhere (OQ-007) (FR-100).
- **AC-015:** Given an SS payable from January-2023 still open in
  2026, then it carries the privileged + no-prescribe flags and every
  prescription/write-off job skips it; only an explicit case
  resolution may clear it, with the cobro-chain stage mirrored on
  the record (FR-095).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Planilla única spec absent: 09_ Art. 27's verbatim truncates at "deberá crearse un..." and neither the Reglamento del D.L. 614 nor the BCR Normas Técnicas (planilla layout, acreditación windows, submission channels) are in the corpus (09_ OQ-2 kin; the Reglamento acquisition is already carried by `05`'s OQ-003). FR-087 exports structured declaration data only — no layout/format is invented; the export binds to the spec when acquired. | no | Takumi S4 (sources watch) | open |
| OQ-002 | ISSS-side statutory window: 08_ Art. 33 inc. 3º defers remittance timing to the Reglamento (absent — 08_ OQ-1). The unified first-10-hábiles window carrying the ISSS planilla is the operative reading of 09_ Art. 21 (its own electronic-planilla mandate) + Art. 27 (planilla única); re-anchor the ISSS leg if the acquired Reglamento diverges. | no | Takumi S4 (sources watch) | open |
| OQ-003 | Sanction-procedure details needing a source re-read: (a) day-type of the 20-day (Art. 143) and 15-day (Art. 144) ladders — the extract says plain días, not días hábiles; (b) the "+$1,200" escalation of Art. 144 (wave reading: total becomes US$1,200); (c) the anchor composition of the Art. 22 "20+10 días hábiles" determination window; (d) Art. 146 imposition/appeal/payment-channel mechanics. FR-091/092/098 implement the as-extract readings; FR-094 keeps estimates pre-imposition. | no | Takumi S4 (evidence re-read) | open |
| OQ-004 | Non-computed sanction legs of Art. 145: the lost-rentabilidad formula (foregone yield on unpaid cotizaciones) and the mechanics of the employer-side Art. 16-inc. 2º cotización leg — no instrument in corpus (BCR Normas candidate). FR-093/094 carry them as flagged exposure components only. | no | Takumi S4 (sources watch) | open |
| OQ-005 | The 08_ Art. 33 inc. 1º fine "cien a quinientos colones" is a colon-era print (1953 law, stable per the reform tail — 08_ OQ-2 watch): never converted/indexed to USD; any successor instrument re-dating the fine is an acquisition candidate feeding FR-096. | no | Takumi S4 (sources watch) | open |
| OQ-006 | Institute accident-report forms absent: the 08_ Art. 75 form templates/codes and the Alcaldía-channel registry (which localities) are not in the corpus; FR-099 ships the 48h clock, the record and the channel flag — no form layout. | no | Takumi S4 (sources watch) | open |
| OQ-007 | Retention period for the 16_ Art. 11 records (planillas/asistencia/recibos): no period appears in the corpus (16_/11_/CT zones read); FR-100 ships no auto-purge, and a retention rule loads only when an instrument pins one. | no | Takumi S4 (sources watch) | open |
