# SV — Payroll — Salary model: salario, salario básico and the earning-category matrix

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador salary model every other payroll
computation builds on: the Código de Trabajo (Labor Code, CT) *salario*
(salary) concept of Art. 119 — money retribution with its *integrantes*
(included components: habitual bonuses, overtime pay, rest/*asueto*-day
pay, profit participation) and its exclusions (occasional gratuities,
function reimbursements, CT *prestaciones sociales*, statutory social
benefits); the *salario básico* (basic salary) of Arts. 140-143 as the
normalized daily/hourly rate that serves as universal base for ANY
employer money obligation, with the seven Art. 142 derivation rules, the
weekly-excess hourly-base rule and the complete-the-week day; the
equal-remuneration rule (Art. 123) and the privileged-credit ordering of
salary/social-benefit credits (Art. 121, ISSS Art. 36, SIP Art. 25) as
metadata; and the CANONICAL earning-category mapping matrix — category →
IBC inclusion, ISR *gravada* (taxable) input, F-14 column family — that
the social-security, interface and fiscal-reporting files consume by FR
id.

It does **not** cover: the salario mínimo chassis and dated tables
(`02_minimum-wage.md`); jornada limits, surcharges, *descanso semanal*
(weekly rest) and *asueto* pay mechanics (`03_working-time-surcharges.md`);
the vacaciones and aguinaldo computation engines
(`04_statutory-benefits.md`); social-security rates, caps and the IBC
computation itself (`05_social-security-contributions.md`); SS
declaration/remittance (`06_ss-declaration-remittance.md`); contracts,
termination and indemnización (`07_contracts-termination.md`); ISR/F-14/F-11
interfaces (`08_isr-interfaces.md`); ISR retention computation (owned by
`taxation/04_isr-withholding.md`); or the F-14 column model (owned by
`fiscal-reporting/06_f14-declaration.md`). Those files consume this one for
the two salary bases and the category matrix.

## 2. Legal Basis

Authority order (binding, per master evidence index S4): labor =
11_ (Código de Trabajo, D.L. 15-1972, Índice Legislativo edition, reform
stamps (1)-(22)); pensions = 09_ (Ley Integral del Sistema de Pensiones,
D.L. 614, effective 2022-12-29 — registry title is a misnomer per R24;
SAP-era lore is dead text); ISSS = 08_ (Ley del Seguro Social, D.L. 1263);
ISR retention-base anchors consumed from the S2 files by FR id (53_
D.E. 10-2025); F-14 column semantics consumed from the S3 files by FR id.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Trabajo, Art. 119: "Salario es la retribución en dinero que el patrono está obligado a pagar al trabajador por los servicios que le presta en virtud de un contrato de trabajo. Considérase integrante del salario, todo lo que recibe el trabajador en dinero y que implique retribución de servicios, cualquiera que sea la forma o denominación que se adopte, como los sobresueldos y bonificaciones habituales; remuneración del trabajo extraordinario, remuneración del trabajo en días de descanso semanal o de asueto, participación de utilidades. No constituyen salario las sumas que ocasionalmente y por mera liberalidad recibe el trabajador ... como las bonificaciones y gratificaciones ocasionales y lo que recibe en dinero, no para su beneficio ... sino para desempeñar a cabalidad sus funciones, como los gastos de representación, medios de transporte, elementos de trabajo u otros semejantes, ni tampoco las prestaciones sociales de que trata este Código." | Salary is the money retribution the employer must pay the worker for services under an employment contract. Everything the worker receives in money implying retribution of services is a salary component whatever its form or name — customary supplements and habitual bonuses; overtime pay; pay for work on weekly-rest or public-holiday days; profit participation. NOT salary: sums received occasionally by mere liberality (occasional bonuses and gratuities); money received not for the worker's benefit but to perform the functions properly (representation allowances, transport means, work tools and similar); and the statutory social benefits of this Code | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 119 p.31 (EVID-201) |
| LB-002 | Código de Trabajo, Art. 121: salary and social benefits are "créditos privilegiados ... ocuparán el primer lugar, excluyendo ... a los demás, aunque estos últimos sean de carácter mercantil" | Privileged credits: salaries and social benefits occupy the first place, excluding all other credits even when the latter are mercantile in character | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 121 p.32 (EVID-201) |
| LB-003 | Código de Trabajo, Art. 123: equal remuneration for equal labor regardless of "sexo, edad, raza, color, o condición de discapacidad, nacionalidad, opinión política o creencia religiosa" (fine scaled to employer capacity) | Equal pay for equal work regardless of sex, age, race, color, disability status, nationality, political opinion or religious belief (with a fine proportionate to the employer's capacity) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 123 p.32 (EVID-201) |
| LB-004 | Código de Trabajo, Art. 140: "Salario básico es la retribución que le corresponde al trabajador de conformidad con lo dispuesto en el inciso primero del Art. 119, el cual servirá de base para calcular cualquier obligación pecuniaria del patrono a favor del trabajador, motivada por la prestación de sus servicios." | Basic salary is the retribution corresponding to the worker per Art. 119 first paragraph, and it serves as the base to calculate ANY pecuniary (money) obligation of the employer in favor of the worker motivated by the rendering of services | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 140 p.34 (EVID-201) |
| LB-005 | Código de Trabajo, Art. 141: salario básico per day or hour = the contract sums | Where the basic salary is stipulated by day or by hour, it corresponds to the sums fixed in the contract | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 141 p.34 (EVID-201) |
| LB-006 | Código de Trabajo, Art. 142: derivation rules A)1-7 (hourly pay × jornada; period total ÷ period days; mixed forms six-day average; unidad de obra six-day total; destajo ÷ days used; a domicilio; commission/other = last-six-months ordinary salaries ÷ días laborables) and B) hourly variants (a domicilio hourly = daily ÷ 8); final inciso: the hourly básico remunerating the excess-day hours "será también el que se tomará en cuenta para remunerar las horas extras que se trabajen excediendo a la semana laboral"; discontinuous-work básico cap printed as "treinta colones" (thirty colons) | Art. 142 A: seven básico derivation rules by pay form; B: hourly variants for home work (daily ÷ 8); final paragraph: the hourly basic salary that remunerates hours of a day in excess of the ordinary workday is ALSO the rate used to remunerate overtime hours worked in excess of the working week; the thirty-colon discontinuous-work cap is a colon-era remnant — dead print, day counts govern (LB note, never a value) | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 142 pp.34-35 (EVID-201; 11_ OQ-2) |
| LB-007 | Código de Trabajo, Art. 143: a day on which the worker worked only the hours needed to complete the week counts as a full day of salario básico | A day containing only complete-the-week hours is remunerated as a full day of basic salary | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 143 p.35 (EVID-201) |
| LB-008 | Ley del Seguro Social (D.L. 1263), Art. 36: ISSS credits carry "privilegio de créditos de primera clase, con preferencia absoluta sobre cualesquiera otros, excepto ... salarios" | ISSS credits are first-class privileged credits with absolute preference over any others, EXCEPT salary credits | `sv/sources/08_Ley_ISSS.pdf` | Art. 36 pp.12-13 (EVID-195) |
| LB-009 | Ley Integral del Sistema de Pensiones (D.L. 614), Art. 25: "Las cotizaciones constituyen créditos privilegiados de conformidad con el artículo 121 del Código de Trabajo." | The (pension) contributions constitute privileged credits in conformity with Art. 121 of the Labor Code | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 25 p.14 (EVID-198) |
| LB-010 | Ley Integral del Sistema de Pensiones, Art. 14: IBC = "la suma de las retribuciones en dinero que el trabajador reciba por los servicios ordinarios que preste durante un mes"; "Considérese integrante del salario, todo lo que reciba el trabajador en dinero y que implique retribución de servicios, incluido el período de vacaciones, comisiones y porcentajes sobre ventas. No forman parte del Ingreso Base de Cotización los siguientes conceptos: a) Las gratificaciones y bonificaciones ocasionales. b) El aguinaldo. c) Viáticos, gastos de representación y prestaciones sociales establecidas por la ley." | Contribution base (IBC) = the sum of money retributions the worker receives for ORDINARY services in a month; salary integrant is everything received in money implying retribution of services, INCLUDING the vacation period, commissions and sales percentages; NOT part of the IBC: a) occasional gratuities and bonuses; b) the aguinaldo (statutory Christmas bonus); c) travel per-diems, representation allowances and social benefits established by law | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 14 pp.6-7 (EVID-197) |
| LB-011 | D.E. 10-2025 (tablas de retención), Art. 1 d): retention base = period remunerations minus *remuneraciones no gravadas* (non-taxable remunerations, comprising the *cotizaciones previsionales*, pension contributions) minus *cotizaciones laborales a la Seguridad Social* (employee social-security contributions) — interface anchor only; the base computation is OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-104 and consumed by reference | Retention-base netting rule: non-taxable remunerations and employee SS/pension contributions leave the ISR retention base before any table application | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 d) (EVID-156, via taxation/04 LB-008) |
| LB-012 | Manual F-14 v16, §2 payroll columns + plantilla header note: G (MONTO DEVENGADO) includes AFP and social-security contributions and EXCLUDES "Aguinaldos, Bonificaciones y Gratificaciones"; H carries *bonificaciones y gratificaciones* separately; J/K = AGUINALDO EXENTO/GRAVADO pair — column semantics OWNED by `fiscal-reporting/06_f14-declaration.md` SV-FREP-FR-143/144 and consumed by reference | F-14 annex column family for payroll rows: accrued-amount column G (excluding bonuses/aguinaldo), separate bonus column H, and the exempt/taxable aguinaldo pair J/K | `sv/sources/35_F14_v16_manual.pdf` | §2 pp.2-5 (EVID-180; EVID-181) |

Dead text — never implementable as current law (LB note, not an FR): CT
Art. 142's discontinuous-work básico cap expressed in "treinta colones"
(thirty colons) is a colon-era remnant of pre-dollarization text,
unenforceable as printed; the Art. 142 day-count derivations govern
(11_ OQ-2 ruling; day counts, never the ¢ figure). CT vintage note
(SOQ-21): the 11_ copy is the Índice Legislativo edition with reform
stamps (1)-(22) and no as-of date; the stamped articles cited here
(Arts. 119-123, 140-143) cross-check consistent with the post-2017
consolidation — re-verify if a later CT reform lands (OQ-001).

## 3. Functional Requirements

### 3.1 Salario and the earning-category model (CT Art. 119)

- **SV-PAY-FR-001:** The system shall classify every payroll earning
  line into exactly one *earning category*: (a) *salario integrante*
  (salary component — money retribution for services, whatever the form
  or denomination adopted), (b) *non-salario* item (an occasional sum
  received by mere liberality, or money received not for the worker's
  benefit but to perform the assigned functions), or (c) *prestación
  social* (statutory social benefit regulated by the Código de Trabajo);
  only money retribution constitutes *salario*. (LB-001; EVID-201)
- **SV-PAY-FR-002:** The system shall recognize as *salario integrante*:
  habitual *sobresueldos y bonificaciones* (customary supplements and
  habitual bonuses), remuneration of *trabajo extraordinario* (overtime
  work), remuneration of work performed on *días de descanso semanal o de
  asueto* (weekly-rest or public-holiday days), and *participación de
  utilidades* (profit participation). (LB-001; EVID-201)
- **SV-PAY-FR-003:** The system shall recognize as NOT *salario*: sums
  received occasionally and by mere liberality (*bonificaciones y
  gratificaciones ocasionales*, occasional bonuses and gratuities); sums
  received in money not for the worker's benefit but to perform the
  functions properly — *gastos de representación* (representation
  allowances), *medios de transporte* (transport means), *elementos de
  trabajo* (work tools) and similar; and the *prestaciones sociales*
  regulated by the Código de Trabajo itself. (LB-001; EVID-201)
- **SV-PAY-FR-004:** The system shall implement the canonical
  earning-category mapping matrix (§4) as the single wave-wide
  classification authority: every earning category/class shall carry the
  three flag families — IBC (*ingreso base de cotización*, contribution
  base) inclusion per SIP Art. 14, ISR *gravada* (taxable) input consumed
  by `taxation/04_isr-withholding.md` SV-TAX-FR-104, and F-14 column
  family (*devengado* G / *bonificaciones* H / *aguinaldo* J-K pair)
  consumed by `fiscal-reporting/06_f14-declaration.md`
  SV-FREP-FR-143/144 — and every consumer file (`05_social-security-
  contributions.md`, `08_isr-interfaces.md`, fiscal-reporting/06-07)
  shall reference this FR id instead of restating the mapping; the
  Quincena Veinticinco row (class `quincena_25`, D.L. 499) is consumed
  by id by `SV-PAY-FR-138..143` (payroll/04 benefit mechanics +
  payroll/08 income treatment and feeds) and `SV-FREP-FR-209..212` (the
  F-14 January-annex engine and the F-910 code-73 surface). The
  quincena_25 earning class carries its matrix flags directly and maps
  to NO sv_pay_earning_category — the category field stays empty for
  Quincena-25 rules (outside FR-001's three categories per 66_ Art. 1;
  EVID-236).
  (LB-001; LB-010; LB-011; LB-012; EVID-201/197/236)

### 3.2 Salario básico: the universal derivation base (CT Arts. 140-143)

- **SV-PAY-FR-005:** The system shall compute and store for every worker
  a *salario básico* (basic salary — the normalized daily and hourly
  rate, stipulated per day/hour as the contract sums for time pay) that
  serves as the base for ANY *obligación pecuniaria* (money obligation)
  of the employer in the worker's favor motivated by the rendering of
  services; every consuming computation of this wave — SMM floors
  (`02_minimum-wage.md`), surcharges and rest/holiday pay
  (`03_working-time-surcharges.md`), vacaciones and aguinaldo
  (`04_statutory-benefits.md`), indemnización and subsidies
  (`07_contracts-termination.md`) — shall read the stored rate and never
  re-derive it independently. (LB-004; LB-005; EVID-201)
- **SV-PAY-FR-006:** The system shall derive the *salario básico* by
  applying exactly one of the seven Art. 142-A derivation rules selected
  by the worker's pay form (catalog in §4): SB-R1 hourly pay — hourly
  rate × hours of the ordinary *jornada* (workday); SB-R2 period pay
  (week, *quincena* (fortnight), month or longer) — period total ÷
  days of the
  period; SB-R3 mixed remuneration forms — six-day average; SB-R4
  *unidad de obra* (unit of work) — six-day total; SB-R5 *destajo*
  (piecework) — total ÷ days used; SB-R6 *a domicilio* (home work) — per
  the Art. 142-B variants, hourly básico = daily ÷ 8; SB-R7 commission or
  other forms — sum of the ordinary salaries received in the last six
  months ÷ *días laborables* (working days) of that window (SB-R7
  is the variable-pay rule that CT Arts. 183/199, anchored at
  `04_statutory-benefits.md` LB-007/LB-016, invoke for benefit
  bases — consumed by `04_statutory-benefits.md`). (LB-006; EVID-201)
- **SV-PAY-FR-007:** The system shall apply the hourly *salario básico*
  that remunerates the hours of a day worked in excess of the ordinary
  *jornada* ALSO as the base hourly rate for overtime hours worked in
  excess of the *semana laboral* (working week) — the Art. 142 final
  *inciso* rule, consumed by `03_working-time-surcharges.md` for the
  Art. 169 overtime recargo. (LB-006; EVID-201)
- **SV-PAY-FR-008:** The system shall remunerate as a FULL day of
  *salario básico* any day on which the worker worked only the hours
  needed to complete the working week. (LB-007; EVID-201)

### 3.3 Equal pay and privileged credits (metadata)

- **SV-PAY-FR-009:** The system shall provide an equal-remuneration
  audit surface comparing the pay of workers performing equal labor
  under equal conditions, regardless of *sexo, edad, raza, color, o
  condición de discapacidad, nacionalidad, opinión política o creencia
  religiosa* (sex, age, race, color, disability status, nationality,
  political opinion or religious belief) — implemented as analytics
  metadata over salary data; no payslip computation is derived from it.
  (LB-003; EVID-201)
- **SV-PAY-FR-010:** The system shall tag worker credits with
  privileged-credit metadata for settlement ordering: salary and CT
  social-benefit credits occupy the FIRST place, excluding all other
  credits even mercantile ones (CT Art. 121); ISSS credits are
  first-class with absolute preference over any others EXCEPT salary
  credits (08_ Art. 36); SIP *cotizaciones* (contributions) are
  privileged credits per CT Art. 121 (09_ Art. 25) — recorded as
  metadata only, with no computation attached. (LB-002; LB-008; LB-009;
  EVID-201/195/198)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in the
client (wave default `odoo`; see §5). No dated values live in this file
except the §5 version-regime notes; the SMM and SS-cap sidecars belong to
`02_minimum-wage.md` and `05_social-security-contributions.md`
respectively.

**Earning-category model (on salary rules, stamped onto payslip lines):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.salary.rule → hr.payslip.line | sv_pay_earning_category | select | salario_integrante · non_salario · prestacion_social | FR-001 |
| hr.salary.rule | sv_pay_earning_class | select | ordinary_pay · habitual_bonus · overtime_pay · rest_asueto_day_pay · profit_participation · occasional_gratuity · reimbursement · vacation_pay · aguinaldo · other_ct_benefit · quincena_25 | FR-002, FR-003, FR-004 |
| hr.salary.rule | sv_pay_ibc_included | boolean | per matrix below; consumed by `05_social-security-contributions.md` | FR-004 |
| hr.salary.rule | sv_pay_isr_gravada_input | select | gravada · no_gravada · split_exento_gravado · crosscheck_oq | consumed by SV-TAX-FR-104 and `08_isr-interfaces.md` | FR-004 |
| hr.salary.rule | sv_pay_f14_column_family | select | devengado_g · bonificaciones_h · aguinaldo_jk · none | consumed by SV-FREP-FR-143/144 | FR-004 |

**CANONICAL EARNING-CATEGORY MAPPING MATRIX (SV-PAY-FR-004 — the
wave-wide authority; consumers reference the FR id, never restate):**

| Earning class (anchor) | Category | In salario (CT 119) | In IBC (SIP 14) | ISR gravada input (53_ 1.d) | F-14 column family (35_ §2) |
|------------------------|----------|--------------------|-----------------|------------------------------|------------------------------|
| Ordinary pay — money retribution for ordinary services (time, unit-of-work, commission ordinary salaries; carries the presumed séptimo-día/asueto components of period salaries, decomposed by file 03) | salario_integrante | yes | yes | gravada | G (codes 01/60/80 — totality rule; code semantics owned by `fiscal-reporting/07_codes-and-informs.md` SV-FREP-FR-171, EVID-182) |
| Habitual sobresueldos y bonificaciones | salario_integrante | yes | yes | gravada | H |
| Overtime remuneration (trabajo extraordinario) | salario_integrante | yes | yes | gravada | G |
| Rest-day / asueto-day work remuneration | salario_integrante | yes | yes | gravada | G |
| Participación de utilidades (profit participation) | salario_integrante | yes | yes | gravada | G |
| Occasional bonuses and gratuities (bonificaciones y gratificaciones ocasionales) | non_salario | no | no (14.a) | gravada — no corpus exclusion (OQ-002) | H |
| Representation allowances, transport means, work tools, viáticos-type reimbursements | non_salario | no | no (14.c) | no_gravada when reasonable and documented (SV-TAX-FR-004) | none (not remuneration) |
| Vacation pay (prestación with express IBC inclusion "incluido el período de vacaciones") | prestacion_social | no | yes (express inclusion) | gravada (EVID-204 mapping note) | G |
| Aguinaldo | prestacion_social | no | no (14.b) | split_exento_gravado — floor and vintages taxation-owned (SV-TAX-FR-120) | J / K pair |
| Other CT statutory benefits (indemnización, illness/maternity subsidies, sepelio; séptimo día decomposes into ordinary pay per Art. 174 — `03_working-time-surcharges.md` LB-011) | prestacion_social | no | no (14.c prestaciones sociales) | crosscheck_oq (Ley ISR Art. 4 cross-check — OQ-003) | value feed via `08_isr-interfaces.md` |
| Quincena Veinticinco annual complement (D.L. 499; paid 15–25 Jan; 50% of monthly salario básico o nominal, gate ≤ US$1,500.00) | none — special-law benefit outside the CT categories (66_ Art. 1 independence declaration; EVID-236) | no — ingreso complementario independiente del salario ordinario, aguinaldo y otras prestaciones (66_ Art. 1) | no — never in any benefit-calculation base nor SS/pension cotización (66_ Art. 1) | no_gravada (66_ Art. 4) | none — surfaces ONLY in the separate January-only Quincena annex (SV-FREP-FR-209), never in the G/H/J-K retention-annex families |

Matrix resolution note: the crosscheck_oq cells above are resolved by
`08_isr-interfaces.md` §3.2 (FR-123..125), 2026-08-18 — indemnización
split_exento_gravado, sepelio no_gravada, illness/maternity subsidies
gravada (OQ-002/OQ-003 below).

**Salario básico engine (per contract):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | sv_pay_pay_form | select | hourly · period · mixed · unit_of_work · destajo · home_worker · commission_other | FR-006 |
| hr.contract | sv_pay_basico_rule | select (computed) | SB-R1 .. SB-R7 (derivation catalog below) | FR-006 |
| hr.contract | sv_pay_salario_basico_day / sv_pay_salario_basico_hour | monetary (computed, stored) | the universal base; read-only for consumer files 02-07 | FR-005, FR-006 |
| hr.contract (commission_other and mixed) | sv_pay_ordinary_salaries_6mo / sv_pay_dias_laborables_6mo | monetary / integer (rolling) | six-month ordinary-salary feed for SB-R7 | FR-006 |

**Art. 142 derivation-rule catalog:**

| Rule | Pay form | Derivation | Anchor |
|------|----------|------------|--------|
| SB-R1 | Hourly pay | hourly rate × hours of the ordinary jornada | Art. 142 A.1 |
| SB-R2 | Period pay (week/quincena/month/longer) | period total ÷ days of the period | Art. 142 A.2 |
| SB-R3 | Mixed remuneration forms | six-day average | Art. 142 A.3 |
| SB-R4 | Unidad de obra | six-day total | Art. 142 A.4 |
| SB-R5 | Destajo | total ÷ days used | Art. 142 A.5 |
| SB-R6 | A domicilio | per Art. 142 B variants; hourly básico = daily ÷ 8 | Art. 142 A.6 + B |
| SB-R7 | Commission and other forms | last-six-months ordinary salaries ÷ días laborables | Art. 142 A.7 |
| — | Weekly-excess overtime base | the excess-day hourly básico is also the rate for overtime hours exceeding the working week | Art. 142 final inciso (FR-007) |
| — | Complete-the-week day | full day of salario básico | Art. 143 (FR-008) |

**Metadata (equal pay + privileged credits):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (payroll journal) | sv_pay_privileged_credit | tag | ct_art121_first · isss_art36_first_class_except_salaries · sip_art25_privileged | FR-010 |
| hr.payroll (analysis) | equal-pay audit view | view | same-labor cohorts across the Art. 123 protected dimensions | FR-009 |

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr / hr_payroll
module family) — every FR maps `odoo`; no SaaS rows are introduced
because none of these FRs touch DTE generation/transformation (the only
architecture-split surface per `shared/docs/saas-thin-client-architecture.md`
D2). Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | hr.salary.rule / hr.payslip.line | sv_pay_earning_category | Category set on the rule, stamped on each line at computation; drives all matrix flags |
| FR-002 | odoo | hr.salary.rule | sv_pay_earning_class | Integrante subclasses (habitual bonus, overtime, rest/asueto-day pay, profit participation) |
| FR-003 | odoo | hr.salary.rule | sv_pay_earning_class | Non-salary/reimbursement and prestación classes; non-salary rules never feed básico or IBC |
| FR-004 | odoo | hr.salary.rule + §4 matrix | sv_pay_ibc_included, sv_pay_isr_gravada_input, sv_pay_f14_column_family | Canonical matrix as rule-level flags; consumers: file 05, file 08, SV-FREP-FR-143/144, SV-TAX-FR-104 — reference by FR id; quincena_25 row added S6 (D.L. 499; EVID-236) |
| FR-005 | odoo | hr.contract | sv_pay_salario_basico_day/_hour | Computed stored rate; consumer files 02-07 read it, never re-derive |
| FR-006 | odoo | hr.contract | sv_pay_pay_form, sv_pay_basico_rule | Pay-form → SB-rule selection; rolling six-month feeds maintained for commission/mixed forms |
| FR-007 | odoo | hr.contract | sv_pay_salario_basico_hour | Hourly base reused for weekly-excess overtime; file 03 applies the Art. 169 recargo on it |
| FR-008 | odoo | hr.attendance / work-calendar flag | complete-the-week day detection | Full-day básico; feeds file 03 séptimo-día accrual |
| FR-009 | odoo | hr.payroll (analysis view) | equal-pay audit | Analytics surface over the Art. 123 dimensions; no payslip rule attached |
| FR-010 | odoo | account.move.line (payroll journal) | sv_pay_privileged_credit | Metadata tag only; settlement-ordering consumers read it |

Version-regime notes (D12): no dated values live in this file. The CT
text basis is the Índice Legislativo edition (stamps through (22), no
as-of date — SOQ-21/OQ-001 watch); the ISR and F-14 anchors are consumed
by reference and carry the version regimes recorded in their owning
files (D.E. 10-2025 effective 2025-05-08; F-14 v16 print Oct-2025).
Exception: the Quincena-25 row's 15–25 January window and US$1,500.00
gate are D.L. 499's printed constants, cited from 66_ (EVID-236), not
locally owned dated data.

## 6. Acceptance Criteria

- **AC-001:** Given a commission-only worker whose ordinary salaries
  received over the last six months total US$10,920.00 and whose *días
  laborables* in that window total 156, when the *salario básico* is
  derived, then the daily básico = 10,920.00 ÷ 156 = US$70.00 (FR-006,
  SB-R7).
- **AC-002:** Given a worker paid US$480.00 over a 30-day period with an
  8-hour ordinary *jornada*, then the daily *salario básico* =
  US$16.00 and the hourly básico = US$2.00; and when overtime hours are
  worked in excess of the *semana laboral*, then the US$2.00 hourly base
  (not any other rate) is the input handed to
  `03_working-time-surcharges.md` for the Art. 169 recargo (FR-006
  SB-R2, FR-007).
- **AC-003:** Given a payslip carrying (i) a habitual productivity bonus
  of US$50.00, (ii) an occasional gratuity paid by mere liberality of
  US$100.00, (iii) a work-tools reimbursement of US$40.00 and (iv)
  aguinaldo of US$400.00, when classified per the canonical matrix, then
  (i) salario_integrante/habitual — IBC in, gravada, F-14 H; (ii)
  non_salario/occasional — IBC out (14.a), gravada per OQ-002, F-14 H;
  (iii) non_salario/reimbursement — IBC out (14.c), no_gravada when
  reasonable and documented, no F-14 column; (iv)
  prestacion_social/aguinaldo — IBC out (14.b), split_exento_gravado per
  SV-TAX-FR-120, F-14 J/K (FR-001..004).
- **AC-004:** Given a *destajo* worker who earned US$120.00 over 4 days
  used, when the *salario básico* is derived, then the daily básico =
  US$30.00 (FR-006, SB-R5).
- **AC-005:** Given a worker who on a given day worked only the hours
  needed to complete the working week, then that day is remunerated as a
  FULL day of *salario básico* (FR-008).
- **AC-006:** Given vacation pay of US$650.00 and aguinaldo of
  US$500.00 on a worker's annual payslips, when the IBC feed is built,
  then the vacation pay carries sv_pay_ibc_included = true (express
  Art. 14 inclusion "incluido el período de vacaciones") while the
  aguinaldo carries sv_pay_ibc_included = false (Art. 14.b) (FR-004).
- **AC-007:** Given a January payslip with an ordinary salary line and a
  Quincena-25 line of US$750.00, then the Quincena line classifies
  quincena_25 with ibc_included=false, isr=no_gravada and
  f14_column_family=none, and it appears in NO retention-annex export
  column (only in the Quincena annex feed of SV-PAY-FR-142) (FR-004;
  EVID-236).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-21 carried: CT copy vintage — the 11_ source is the Índice Legislativo edition with reform stamps (1)-(22) and no as-of date; the articles cited here (119-123, 140-143) cross-check consistent with a post-2017 consolidation. Re-verify stamped articles if a later CT reform lands (D.O. watch). | no | Takumi S4 (sources watch) | open |
| OQ-002 | Occasional gratuities ISR treatment: CT Art. 119 excludes them from *salario* and SIP Art. 14.a excludes them from IBC, but no corpus norm excludes them from the ISR *remuneraciones gravadas* concept; the matrix marks gravada = yes pending confirmation in the interfaces file (`08_isr-interfaces.md`, taxation cross-check). | no | Takumi S4 (task 8) | resolved 2026-08-18 — `08` §3.2 FR-125 confirms gravada (no exclusion in the Ley ISR Art. 3-4 lists); crosscheck flag cleared |
| OQ-003 | ISR gravada classification of the non-vacation/aguinaldo *prestaciones* (indemnización, illness/maternity subsidies, sepelio): the Ley ISR Art. 4 exemption-list cross-check belongs to `08_isr-interfaces.md` + taxation; the matrix cell carries crosscheck_oq until then (EVID-204/209 mapping notes). | no | Takumi S4 (task 8) | resolved 2026-08-18 — `08` §3.2 FR-123 (indemnización split_exento_gravado per Art. 4.3), FR-124 (sepelio no_gravada), FR-125 (subsidies gravada); crosscheck_oq cells resolved |
