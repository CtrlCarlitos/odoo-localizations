# SV — Payroll — Social-security contributions: ISSS and SIP rates, IBC, caps and regime routing

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the Salvadoran social-security contribution engine:
the ISSS (*Instituto Salvadoreño del Seguro Social*) side of Ley del
Seguro Social (D.L. 1263) — mandatory affiliation of ALL dependent
workers whatever the contract type or remuneration form (Art. 3) with
the high-income exclusion threshold as reglementary dated data
(SOQ-15), the general *régimen de salud y riesgos profesionales* rates
of 7.50% *patrono* / 3.00% *trabajador* (employer / worker) over the
*remuneración afecta* (remuneration subject to social security) with
the Art. 99 public-sector special health regime at 6.68%/2.67%
(medical-only), voluntary insurance at both shares, the Art. 34 base
fallbacks for variable/part-in-kind earners, the Art. 33
employer-share no-deduction invariant, and the worker-share $-cap as
F-14-print dated data; and the SIP (*Sistema Integral de Pensiones*)
side of Ley Integral del Sistema de Pensiones (D.L. 614, effective
2022-12-29 — registry title is a misnomer per R24; SAP-era rate lore
is dead text) — the 16% *cotización* (contribution) split 7.25%
*trabajador* / 8.75% *empleador* with the 9.0/6.0/1.0 destination
split and the never-pass-through invariant (Art. 16), the
*ingreso base de cotización* (IBC, contribution base) of Art. 14
consuming Task 1's canonical matrix by id, the SMM floor with
sector-associated exceptions, calendar-day months, multi-job
per-salary cotización, subsidy months and the pensioner
riesgos-profesionales base, the independent-worker full-share
declared-income mode (Art. 15), affiliation/routing (Art. 8 AFP
choice + 20-day default; Art. 11 instituto exclusions), the
pensioner-side adjacent config (7.80% health per R23; 7% solidarity
above 6× *pensión mínima*), and the caps as DATED DATA from the F-14
v16 print (Oct-2025) with their instrument OQs — carried in the CSV
sidecar `ss_contributions.csv` that is the wave's single SS parameter
feed (SOQ-11: payroll owns the values; the F-14 side mirrors them as
validation parameters).

It does **not** cover: the *salario*/*salario básico* model and the
canonical earning-category matrix (`01_salary-model.md` — SV-PAY-FR-004
is consumed by id for every IBC inclusion/exclusion; the stored rates
of its FR-005 are never re-derived); the SMM chassis and dated tariff
tables (`02_minimum-wage.md` — its sidecar `smm_2025.csv` owns every
sector SMM row feeding the IBC floor); jornada, surcharges and
asuetos (`03_working-time-surcharges.md`); vacaciones and aguinaldo
computation (`04_statutory-benefits.md`); SS declaration, remittance,
planillas and sanctions (`06_ss-declaration-remittance.md` — owns the
10-*días-hábiles* window, the electronic planilla and the fine/mora
regime); contracts, termination and *indemnización*
(`07_contracts-termination.md`); the ISR retention-base netting of
worker-side cotizaciones (owned by `taxation/04_isr-withholding.md`
SV-TAX-FR-104, wired payroll-side by `08_isr-interfaces.md`); and the
F-14 column model (owned by `fiscal-reporting/06_f14-declaration.md`).

## 2. Legal Basis

Authority order (binding, per master evidence index S4): pensions =
09_ (Ley Integral del Sistema de Pensiones, **D.L. 614**, effective
2022-12-29 — derogates D.L. 927-1996/SAP per its Art. 162; the
registry title "Ley del Sistema de Ahorro para Pensiones" is a
misnomer, R24; SAP-era rates are NEVER cited) over any SAP-era lore;
ISSS = 08_ (Ley del Seguro Social, D.L. 1263 — law-level rates; caps
live in the Reglamento, absent from corpus, SOQ-15) with 09_ Art. 154
governing pensioner-health (ruling R23); caps as dated data from the
F-14 v16 print Oct-2025 (SOQ-11/15/16/17); SMM rows consumed from
`02_minimum-wage.md`'s sidecar by FR id; F-14 column semantics
consumed from the S3 files by FR id.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley del Seguro Social (D.L. 1263), Art. 3: "El régimen del Seguro Social obligatorio se aplicará originalmente a todos los trabajadores que dependan de un patrono, sea cual fuere el tipo de relación laboral que los vincule y la forma en que se haya establecido la remuneración. ... Podrá exceptuarse únicamente la aplicación obligatoria del régimen del Seguro, a los trabajadores que obtengan un ingreso superior a una suma que determinarán los reglamentos respectivos." | The obligatory social-security regime applies to ALL workers depending on an employer, whatever the type of labor relation and the form in which the remuneration is established; the ONLY permissible exception is workers earning above a sum that the respective REGULATIONS determine (high-income exclusion = reglementary dated data; instrument absent, SOQ-15) | `sv/sources/08_Ley_ISSS.pdf` | Art. 3 p.2 (EVID-194) |
| LB-002 | Ley del Seguro Social, Art. 29: "Las cuotas que aportarán los patronos, los trabajadores y el Estado ... se determinarán con base a la remuneración afecta al Seguro Social." "Para la cobertura del régimen general de salud y riesgos profesionales, el patrono aportará el siete punto cincuenta por ciento (7.50%) y el trabajador el tres por ciento (3%), de la referida remuneración." "Para la cobertura del régimen especial de salud a que se refiere el Art. 99 de esta Ley, el patrono aportará el seis punto sesenta y ocho por ciento (6.68%) y el trabajador el dos punto sesenta y siete por ciento (2.67%), de la remuneración antes mencionada." "En caso de seguro voluntario autorizado por los reglamentos, el asegurado pagará en su totalidad las aportaciones que correspondieren al trabajador y al patrono; en los mismos porcentajes establecidos para el régimen obligatorio de que se trate." | Quotas are determined over the remuneración afecta; general health + riesgos profesionales regime = employer 7.50% / worker 3.00%; the Art. 99 special health regime = 6.68% / 2.67%; voluntary insurance = the assured pays BOTH shares in full, in the same percentages of the obligatory regime in question. (The same article's IVM 3.50% "primas escalonadas" seed and pensioner 6% are DEAD print for current periods — see the dead-text note below) | `sv/sources/08_Ley_ISSS.pdf` | Art. 29 p.11 (EVID-193) |
| LB-003 | Ley del Seguro Social, Art. 99: the Régimen Especial (public-sector workers indicated by reglamento) covers only letters a), b), c) of Art. 2; "En ningún caso el Régimen Especial incluirá prestaciones en dinero." — valid_from caveat: the CSV `isss_art99_public` rate row's 1953-12-11 is the shared Art. 29 law-print date, NOT a per-inciso verified date (reform-tail stability watch 08_ OQ-2, as the general row carries; the regime's applicability is itself reglementary — SOQ-15) | The public-sector special health regime covers only the listed contingencies and in NO case includes money (cash) benefits — medical-only | `sv/sources/08_Ley_ISSS.pdf` | Art. 99 p.24 (EVID-193) |
| LB-004 | Ley del Seguro Social, Art. 34: "El Instituto podrá agrupar en sus reglamentos a los asegurados que no tengan ingresos fijos, a efecto de establecer un salario de base ... Los reglamentos también fijarán las normas para establecer la base para el cómputo de las cotizaciones y beneficios en dinero, de los asegurados que perciban sus ingresos parcialmente en especie. La determinación de las cotizaciones y de los beneficios podrá hacerse en base a salarios mínimos y salarios presuntos que establecerán los Reglamentos." | The Institute may group non-fixed-income insured persons in its regulations to establish a base salary; the regulations also fix the base-computation rules for earners paid partly in kind, and cotizaciones/benefits may be determined on minimum-wage (SMM) and presumed salaries that the Regulations establish — reglementary fallbacks (instrument absent, SOQ-15) | `sv/sources/08_Ley_ISSS.pdf` | Art. 34 p.12 (EVID-194) |
| LB-005 | Ley del Seguro Social, Art. 33: "Las cuotas de los patronos no podrán ser deducidas en forma alguna de los salarios de los asegurados. El patrono que infringiere esta disposición será sancionado con una multa de cien a quinientos colones, sin perjuicio de la restitución..." "El patrono deberá deducir a todas las personas que emplee y que deben contribuir al régimen del Seguro Social, las cuotas correspondientes a los salarios que les pague, y será responsable por la no percepción y entrega de tales cuotas al Instituto..." | The employer's own quotas may NEVER be deducted from the insured workers' salaries in any form (violation = fine plus restitution); the employer MUST withhold the worker quotas of every contributing person it employs, is responsible for their perception and delivery to the Institute, and remits both shares within the Reglamento's terms (timing mechanics owned by `06_ss-declaration-remittance.md`) | `sv/sources/08_Ley_ISSS.pdf` | Art. 33 p.12 (EVID-195) |
| LB-006 | Ley Integral del Sistema de Pensiones (D.L. 614), Art. 16: "La tasa de cotización del Sistema será del dieciséis por ciento (16%) sobre el ingreso base de cotización, correspondiendo el siete punto veinticinco por ciento (7.25%) al trabajador y el ocho punto setenta y cinco por ciento (8.75%) al empleador. Esta tasa se distribuirá así: a) El nueve punto cero por ciento (9.0%) ... acreditado en la cuenta individual de ahorro para pensiones. De este total siete punto veinticinco por ciento (7.25%) ... aportado por el trabajador y uno punto setenta y cinco por ciento (1.75%) por el empleador. b) El seis punto cero por ciento (6.0%) ..., será acreditado a la Cuenta de Garantía Solidaria; y, c) Uno punto cero por ciento (1.0%) ..., se destinará como comisión para las Administradoras." Final inciso: "En ningún caso, el incremento del 1% en la cotización que le corresponde al empleador, deberá ser trasladado bajo ninguna figura al trabajador." | SIP cotización = 16% of the IBC: 7.25% worker + 8.75% employer; destination split: 9.0% to the individual pension-savings account (the worker's 7.25% + 1.75% employer), 6.0% to the Garantía Solidaria account, 1.0% as Administradora (AFP) commission; and the employer's 1-point increment may NEVER be shifted to the worker under any figure | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 16 pp.7-8 (EVID-197) |
| LB-007 | Ley Integral del Sistema de Pensiones, Art. 14: "El ingreso base para calcular las cotizaciones obligatorias de los trabajadores dependientes será el salario mensual que devenguen o el subsidio respectivo de incapacidad por enfermedad, accidente o maternidad. Dicha base no podrá ser inferior al salario mínimo legal mensual en vigencia, excepto en los casos tales como aprendices, trabajadores agrícolas, domésticos y otros cuyos ingresos sean inferiores a dicho mínimo, considerando los salarios mínimos de los sectores asociados... se entenderá por salario mensual la suma de las retribuciones en dinero que el trabajador reciba por los servicios ordinarios que preste durante un mes. Considérese integrante del salario, todo lo que reciba el trabajador en dinero y que implique retribución de servicios, incluido el período de vacaciones, comisiones y porcentajes sobre ventas. No forman parte del Ingreso Base de Cotización los siguientes conceptos: a) Las gratificaciones y bonificaciones ocasionales. b) El aguinaldo. c) Viáticos, gastos de representación y prestaciones sociales establecidas por la ley." (continues: calendar-day month denominator, per-salary treatment of multiple employers, and the pensioner riesgos-profesionales base — extract truncated in evidence; see OQ-006) | IBC for dependent workers = the monthly salary earned OR the respective illness/accident/maternity subsidy; floor = the current legal monthly SMM EXCEPT apprentices, agricultural and domestic workers and others earning below it, considering the sector-associated SMMs; monthly salary = money retributions for ORDINARY services in a month; included: the vacation period, commissions, sales percentages; excluded: occasional gratuities/bonuses, the aguinaldo, viáticos/representation allowances/legal social benefits — the inclusion/exclusion CLASSIFICATION MATRIX is OWNED by `01_salary-model.md` SV-PAY-FR-004 and consumed by reference | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 14 pp.6-7 (EVID-197) |
| LB-008 | Ley Integral del Sistema de Pensiones, Art. 15 (gloss-level; no verbatim extracted): independent workers' obligatory-affiliation cotización mode — the affiliated independent pays the FULL share (both the worker's and the employer's side) over the income he declares to the Sistema | Independent workers: full-share declared-income mode (the self-paying affiliated bears the whole cotización over declared income) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 15 p.7 (EVID-197) |
| LB-009 | Ley Integral del Sistema de Pensiones, Arts. 8 and 11 (gloss-level per master index P6): Art. 8 — worker's free choice of Administradora (AFP), with employer obligatory registration within TWENTY days when the worker does not choose; Art. 11 — exclusions from obligatory affiliation: workers covered by IPSFA/IvD and the institutos case | Routing anchors: the worker chooses the AFP (employer registers within 20 days by default when no choice is exercised); workers covered by IPSFA/IvD are excluded from SIP obligatory affiliation (the institutos case) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Arts. 8, 11 pp.4-5 (EVID-197; EVID-200) |
| LB-010 | Ley Integral del Sistema de Pensiones, Art. 154: "Las cotizaciones al programa de salud del Instituto Salvadoreño del Seguro Social, para la cobertura de los pensionados y su cónyuge o conviviente, será a cargo del pensionado ... con una tasa de cotización del siete punto ochenta por ciento (7.80%) de su pensión mensual." | Pensioner-side ISSS health cotización = 7.80% of the monthly pension, borne by the pensioner, covering pensioner and spouse/concubine — SUPERSEDES the 6% of 08_ Art. 29 (ruling R23: D.L. 614 is later in time and specifically regulates this cotización) | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 154 p.62 (EVID-199) |
| LB-011 | Ley Integral del Sistema de Pensiones, Art. 121 (gloss-level): old-age pensioners whose pension exceeds SIX times the pensión mínima cotize 7% to the Cuenta de Garantía Solidaria (counterpart: +10% raise from age 85) | Pensioner solidarity cotización: 7% over the pensión when it exceeds 6× the pensión mínima | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 121 p.50 (EVID-199) |
| LB-012 | Manual F-14 v16 (Oct-2025), §2, columns L-R with printed maxima (via `fiscal-reporting/06_f14-declaration.md` LB-002): "AFP: ... siendo el monto máximo de cotización $472.93, de acuerdo a la Ley" / "ISSS: ... monto máximo de cotización 30.00" / "INPEP: ... porcentaje máximo de cotización del 7.5% del monto devengado" / "IPSFA: ... 9.5%" / "CEFAFA: ... 5%" / "Bienestar Magisterial: ... 5.58%" / "ISSS/IVM: ... 7.5%" — dated VALUE anchor only; the caps' own instruments are ABSENT from the corpus (SOQ-15/16/17) and the values enter as dated data owned by THIS file's sidecar (SOQ-11: the F-14 side mirrors them as validation parameters per SV-FREP-FR-145/150) | The seven F-14 SS columns carry legal maxima — amount caps AFP US$472.93 and ISSS US$30.00; percentage maxima INPEP 7.5%, IPSFA 9.5%, CEFAFA 5%, Bienestar Magisterial 5.58%, ISSS-IVM 7.5% — a dated Oct-2025 print snapshot, NEVER a derivation base: no implied base ceiling may be asserted from a cap value | `sv/sources/35_F14_v16_manual.pdf` | §2 pp.2-5 zone (EVID-180; via fiscal-reporting/06 LB-002) |

Dead text — never implementable as current law (LB note, not an FR):
(i) 08_ Art. 29's IVM seed "cuotas iniciales ... 3.50% (patronos 2%,
trabajadores 1%, Estado 0.50%)" is the 1953 *primas escalonadas*
public-pension seed — superseded for private-sector pensions by the
SIP (09_) and for the public side by the institutos; it is NEVER an
operative rate, and the F-14's ISSS-IVM 7.5% print (SOQ-17 dated
data) governs that column instead. (ii) 08_ Art. 29's pensioner 6%
health rate is superseded by 09_ Art. 154's 7.80% (ruling R23) — cite
the ruling, never the 6%. (iii) Any SAP-era rate lore (e.g. 6.25%/
6.75% splits of D.L. 927-1996) is dead per D.L. 614 Art. 162 (R24) —
only Art. 16's 16% (7.25/8.75) may be cited for current periods.
Version regime (D12): the ONLY dated values owned by this file live in
the sidecar `ss_contributions.csv` (rates are law-anchored with their
articles; caps are print-anchored Oct-2025 with SOQ-15/16/17
instrument OQs); the ISSS Reglamento de Aplicación is absent from the
corpus (SOQ-15) — until acquired, every reglementary value (high-income
exclusion threshold, base ceiling, presumed/SMM base tables) stays
unencoded configuration.

## 3. Functional Requirements

### 3.1 Affiliation scope and regime routing

- **SV-PAY-FR-063:** The system shall affiliate in the ISSS obligatory
  regime EVERY worker depending on an employer, whatever the type of
  labor relation linking them and the form in which the remuneration
  is established, and shall apply the high-income EXCLUSION only as
  dated configuration data carrying its instrument OQ (SOQ-15): the
  exclusion threshold is fixed exclusively by the ISSS Reglamento
  (absent from corpus) — no threshold value is invented, and a worker
  is never excluded by default. (LB-001; EVID-194)
- **SV-PAY-FR-064:** The system shall route every worker's pension
  cotización to the AFP of the worker's CHOICE, registering the worker
  with an Administradora; when a worker exercises no choice, the
  employer shall register the worker within TWENTY days under the
  default-assignment rule, recording the assignment date and AFP on
  the employee's SS routing record. (LB-009; EVID-197; EVID-200)
- **SV-PAY-FR-065:** The system shall exclude from SIP obligatory
  affiliation the workers covered by the instituto regimes that Art. 11
  excludes (IPSFA/IvD), carrying the exclusion as an employee-level
  SS-regime routing dimension (instituto code) that determines which
  contribution parameter rows apply (§4); instituto rates themselves
  enter ONLY as F-14-print dated data (FR-083) with their instrument
  OQ. (LB-009; EVID-200)

### 3.2 ISSS contributions: rates, base, cap and the no-deduction invariant

- **SV-PAY-FR-066:** The system shall compute the ISSS general-regime
  cotización over the *remuneración afecta* at 7.50% employer / 3.00%
  worker (salud + riesgos profesionales folded — no separate employer
  accident rate exists in the law; watch OQ-004), posting the worker
  share as a payslip deduction and the employer share as employer
  cost, monthly per worker, from the `ss_contributions.csv` law-anchored
  rate rows. (LB-002; EVID-193)
- **SV-PAY-FR-067:** The system shall compute, for workers routed to
  the Art. 99 public-sector special health regime, the cotización at
  6.68% employer / 2.67% worker, and shall NEVER generate money-benefit
  accruals under that regime (medical-only invariant); the routing is
  employer/reglementary configuration carrying its instrument OQ
  (SOQ-15). (LB-002; LB-003; EVID-193)
- **SV-PAY-FR-068:** The system shall support the voluntary-insurance
  mode in which the assured bears BOTH shares in full — the worker
  percentages plus the employer percentages of the applicable
  obligatory regime, computed over the same remuneración afecta — as
  an employee-level configuration with no employer-share cost line.
  (LB-002; EVID-193)
- **SV-PAY-FR-069:** The system shall determine the ISSS cotizable
  base per worker as the *remuneración afecta*, operationally built
  from the canonical matrix flags of `01_salary-model.md`
  SV-PAY-FR-004 (sv_pay_ibc_included — consumed by id, never
  restated) as the corpus proxy, and shall support the Art. 34
  reglementary fallbacks for variable earners, part-in-kind earners
  and presumed/SMM bases ONLY as dated configuration data with its
  instrument OQ (SOQ-15) — no fallback table value is invented
  (divergence between the ISSS reglamento list and SIP Art. 14 stays
  under OQ-005). (LB-002; LB-004; EVID-193/194; cross-ref
  SV-PAY-FR-004)
- **SV-PAY-FR-070:** The system shall clamp the ISSS WORKER-share
  monthly cotización at the amount-cap value loaded from the
  `ss_contributions.csv` print-anchored cap row (US$30.00, F-14 v16
  Oct-2025 print, SOQ-15 instrument OQ) — a VALUE-LEVEL clamp only:
  the base-ceiling instrument is absent, and the system shall never
  assert, derive or encode any implied base ceiling by arithmetic
  (whether/how the ceiling binds the employer 7.50% share is unknown —
  OQ-007; the employer share computes over the unclamped
  remuneración afecta unless the acquired instrument says otherwise).
  (LB-002; LB-012; EVID-193/180)
- **SV-PAY-FR-071:** The system shall enforce the employer-share
  no-deduction invariant: the patronal ISSS quotas may NEVER be
  deducted from the insured workers' salaries in any form — any
  salary-rule configuration that charges the employer share (or any
  part of it) to the worker is rejected, and the worker-share
  withholding happens at payment of the affected salaries (the
  remittance terms, planillas and the 1%/month recargo of the same
  article are owned by `06_ss-declaration-remittance.md`).
  (LB-005; EVID-195)

### 3.3 SIP contributions: the 16% split and its invariants

- **SV-PAY-FR-072:** The system shall compute the SIP cotización at
  16% over the IBC, split 7.25% trabajador (payslip deduction) /
  8.75% empleador (employer cost), and shall post it with the Art. 16
  destination legs: 9.0% to the individual pension-savings account
  (the worker's 7.25% PLUS 1.75% of the employer's share), 6.0% to
  the Cuenta de Garantía Solidaria (employer) and 1.0% as AFP
  commission (employer) — each leg a tagged accounting line so the
  per-AFP declaration can be built without recomputation (declaration
  mechanics owned by `06_ss-declaration-remittance.md`).
  (LB-006; EVID-197)
- **SV-PAY-FR-073:** The system shall enforce the never-pass-through
  invariant: the worker-side deduction is EXACTLY 7.25% of the IBC —
  the employer's 1-point increment embedded in the 8.75% share may
  never be shifted to the worker under ANY figure — implemented as a
  validation on every SIP salary-rule configuration and a computed
  invariant check on each payslip (violation blocks posting).
  (LB-006; EVID-197)
- **SV-PAY-FR-074:** The system shall support the independent-worker
  mode: an affiliated independent worker bears the FULL cotización
  (both shares, 16% total under the Art. 16 rate) over the income he
  declares, with no employer-share cost line — computed from the
  `ss_contributions.csv` independent row over the declared-income base
  recorded per period. (LB-008; LB-006; EVID-197)

### 3.4 Ingreso base de cotización (Art. 14 — matrix consumed by id)

- **SV-PAY-FR-075:** The system shall compute the monthly IBC for
  every dependent worker as the money retributions received for
  ORDINARY services in the month, taking the inclusion/exclusion
  classification EXCLUSIVELY from the canonical matrix of
  `01_salary-model.md` SV-PAY-FR-004 (sv_pay_ibc_included flags
  stamped on payslip lines — the vacation period, commissions and
  sales percentages are IN; occasional gratuities/bonuses, the
  aguinaldo, viáticos/representation allowances and legal social
  benefits are OUT, and the Quincena-25 — 66_ Art. 1; SV-PAY-FR-141;
  LB-kin of this row's LB-007 exclusion list via
  `04_statutory-benefits.md` LB-025, arriving through the matrix row,
  never restated here): the IBC builder sums the flagged lines and
  RESTATES none of the matrix. (LB-007; EVID-197; cross-ref
  SV-PAY-FR-004, SV-PAY-FR-141)
- **SV-PAY-FR-076:** The system shall floor the IBC at the worker's
  current legal monthly SMM — the dated sector row loaded from
  `02_minimum-wage.md`'s sidecar `smm_2025.csv` per its SV-PAY-FR-011
  (sector association per its SV-PAY-FR-022 config) — and shall apply
  the sector-associated exception for apprentices, agricultural and
  domestic workers and other below-minimum earners (their
  sector-associated SMM governs) ONLY as configuration carrying the
  Normativa Técnica OQ (the surviving SAP-era normas are the likely
  instrument — unacquired, OQ-004). (LB-007; EVID-197)
- **SV-PAY-FR-077:** The system shall measure the monthly salary over
  CALENDAR-day months: the salario mensual and any month proration use
  the month's calendar days (30/31) as the denominator — a mid-month
  entry/exit prorates the monthly salary by calendar days of the
  month, before any SMM floor evaluation. (LB-007; EVID-197)
- **SV-PAY-FR-078:** The system shall cotize EACH salary separately
  for workers with multiple employers: every employer computes and
  declares the cotización over the salary IT pays, with no
  cross-employer aggregation or offset of IBCs, floors or caps.
  (LB-007; EVID-197)
- **SV-PAY-FR-079:** The system shall compute the IBC of a
  subsidy-month as the respective subsidy: in months of illness,
  accident or maternity leave the cotizable base is the
  *subsidio respectivo* in place of the monthly salary (the subsidy
  values themselves are benefit-engine data owned by
  `07_contracts-termination.md`; the license-month devengo timing for
  remittance belongs to `06_ss-declaration-remittance.md`).
  (LB-007; EVID-197)
- **SV-PAY-FR-080:** The system shall carry the Art. 14
  pensioner-side riesgos-profesionales IBC rule as a dedicated config
  slot with NO encoded mechanics pending source pinning: the evidence
  extract truncates the article's final provisions, so the exact
  base rule for the riesgos-profesionales pension situation is
  recorded as OQ-006 and no computation ships until the article text
  is re-read. (LB-007; EVID-197)

### 3.5 Caps and the dated-data feed (ss_contributions.csv)

- **SV-PAY-FR-081:** The system shall load ALL social-security
  contribution parameters from the CSV sidecar `ss_contributions.csv`
  as the single dated SS parameter feed of the wave — schema:
  regime/institution × worker%/employer% × cap-type × cap-value ×
  valid_from × instrument-OQ — with law-anchored RATE rows (article
  refs; ISSS rows 08_ Art. 29, SIP rows 09_ Art. 16, pensioner rows
  Art. 154/121) and print-anchored CAP rows (F-14 v16 Oct-2025
  provenance + SOQ ids), versioned by valid_from/valid_to and
  re-dated per instrument acquisition; no SS rate or cap lives as a
  code constant. (LB-002; LB-006; LB-010; LB-011; LB-012;
  EVID-193/197/199/180)
- **SV-PAY-FR-082:** The system shall clamp the AFP cotización that
  feeds F-14 column L at the amount-cap value loaded from the
  `ss_contributions.csv` print-anchored cap row (US$472.93, F-14 v16
  Oct-2025 print, SOQ-16 instrument OQ) — a VALUE-LEVEL clamp only:
  the ceiling instrument (BCR Norma Técnica? SIP transitory?) is
  absent from the corpus, and the system shall never assert, derive
  or encode any implied IBC ceiling by arithmetic from the cap.
  (LB-012; EVID-180)
- **SV-PAY-FR-083:** The system shall carry the instituto
  percentage-maxima — INPEP 7.5%, IPSFA 9.5%, CEFAFA 5%, Bienestar
  Magisterial 5.58%, ISSS-IVM 7.5% — ONLY as print-anchored cap rows
  from `ss_contributions.csv` (F-14 v16 Oct-2025, SOQ-17 instrument
  OQ): the institutos' rate laws are absent from the corpus, so NO
  worker/employer split is invented and no instituto rate row is
  encoded beyond the printed maxima (public-sector employer
  configuration only). (LB-012; EVID-180; EVID-200)
- **SV-PAY-FR-084:** The system shall remain the single OWNER of the
  cap VALUES (SOQ-11): the F-14 declaration surface
  (`fiscal-reporting/06_f14-declaration.md` SV-FREP-FR-145, validated
  per its SV-FREP-FR-150 and parameter-mirrored in its
  l10n_sv.f14.ss.cap) consumes this file's sidecar values by
  reference — when an instrument is acquired (SOQ-15/16/17), the sidecar
  rows are re-dated here and the mirror follows; the ISR retention
  base netting of the worker-side cotizaciones is consumed by id from
  `taxation/04_isr-withholding.md` SV-TAX-FR-104 (wired by
  `08_isr-interfaces.md`; never re-derived here). (LB-012; EVID-180;
  cross-ref SV-FREP-FR-145, SV-FREP-FR-150, SV-TAX-FR-104)

### 3.6 Pensioner-side adjacent configuration

- **SV-PAY-FR-085:** The system shall carry the pensioner-side
  cotizaciones as ADJACENT configuration rows (no employer-payroll
  computation attached): ISSS pensioner health at 7.80% of the
  monthly pension borne by the pensioner and covering spouse/
  concubine — cited per 09_ Art. 154 with ruling R23 (SUPERSEDES the
  6% of 08_ Art. 29; the 6% is never encoded) — and the SIP solidarity
  cotización of 7% for old-age pensioners whose pension exceeds 6×
  the pensión mínima (Art. 121); both rows live in
  `ss_contributions.csv` under the pensioner regime for the
  pension-paying institution's processes. (LB-010; LB-011; EVID-199)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in
the client (wave default `odoo`; see §5). The ONLY dated data owned by
this file is the sidecar `ss_contributions.csv` (rates + caps,
versioned); the SMM floor rows belong to `02_minimum-wage.md`'s
`smm_2025.csv` and are consumed by FR id.

**SS parameter feed (single dated source):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.ss.parameter (new) | regime · institution · row_type | select | regime: isss_general · isss_art99_public · isss_voluntary · sip · sip_independent · pensioner · instituto; row_type: rate · cap | FR-081 |
| l10n_sv.pay.ss.parameter | worker_pct · employer_pct | float (%) | rate rows only; voluntary/independent rows carry the full share worker-side | FR-066..068, FR-072, FR-074, FR-085 |
| l10n_sv.pay.ss.parameter | cap_type · cap_value · valid_from · valid_to | select/date/monetary | cap_type: amount · percent; print-anchored cap rows (Oct-2025 vintage) | FR-070, FR-082, FR-083 |
| l10n_sv.pay.ss.parameter | source · instrument_oq | char | law article ref (rate rows) / F-14 print provenance + SOQ id (cap rows) | FR-081 |

**Routing and affiliation:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.employee | sv_pay_ss_regime | select | isss_sip (default) · isss_art99_public · instituto_inpep · instituto_ipsfa · instituto_cefafa · instituto_bienestar_magisterial · instituto_isss_ivm · sip_excluded_art11 | FR-064, FR-065, FR-067 |
| hr.employee | sv_pay_afp_id · sv_pay_afp_choice_date · sv_pay_afp_default_flag | m2o/date/boolean | worker AFP choice; default assignment when no choice, with the 20-day registration watchdate | FR-064 |
| hr.employee (ISSS gate) | sv_pay_isss_excluded | boolean (config, dated) | high-income exclusion ONLY as dated config carrying SOQ-15 — no default value ships | FR-063 |
| hr.employee (voluntary) | sv_pay_isss_voluntary | boolean | gates the both-shares mode | FR-068 |
| res.partner (independent) | sv_pay_sip_independent · declared income per period | boolean/monetary | full-share declared-income mode | FR-074 |

**IBC and contribution lines:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip | sv_pay_ibc | monetary (computed) | Σ payslip lines with sv_pay_ibc_included (01 FR-004 flags); floor per FR-076; calendar-day proration per FR-077 | FR-075..077 |
| hr.payslip | sv_pay_isss_base | monetary (computed) | remuneración afecta per FR-069 (matrix proxy; fallback config slots) | FR-069 |
| hr.payslip.line (SS) | sv_pay_ss_share | select | worker · employer | FR-066..068, FR-072 |
| hr.payslip.line (SIP legs) | sv_pay_sip_destination | select | individual_account · garantia_solidaria · afp_commission | FR-072 |
| hr.payslip.line (SS) | sv_pay_ss_cap_applied | monetary/boolean | clamp provenance: value-level cap row id when a clamp fired (never a base assertion) | FR-070, FR-082 |
| l10n_sv.pay.ss.fallback (new) | fallback_type · sector · value · instrument_oq | select/monetary/char | Art. 34 presumed/SMM base tables — EMPTY until the Reglamento is acquired (SOQ-15) | FR-069 |
| config slot | sv_pay_art14_riskpensioner_base | char (OQ placeholder) | no mechanics encoded pending OQ-006 | FR-080 |

**Pensioner adjacent config (no employer payroll):** pensioner-regime
rate rows on l10n_sv.pay.ss.parameter (7.80% health per R23; 7%
solidarity >6×PM) — consumed by pension-paying processes only
(FR-085).

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr /
hr_payroll module family) — every FR maps `odoo`; no SaaS rows are
introduced because none of these FRs touch DTE generation/transformation
(the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is
required beyond the dated-data regime below.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-063 | odoo | hr.employee | sv_pay_isss_excluded | Art. 3 universal affiliation; exclusion = dated config with SOQ-15 OQ; no default threshold ships |
| FR-064 | odoo | hr.employee | sv_pay_afp_id + choice/default dates | Art. 8: choice or 20-day employer default registration |
| FR-065 | odoo | hr.employee | sv_pay_ss_regime | Art. 11 instituto exclusions; regime feeds which ss.parameter rows and F-14 SS columns apply |
| FR-066 | odoo | hr.payslip.line (SS rules) | worker 3.0 / employer 7.5 legs | From ss_contributions.csv isss_general rate row; riesgos folded (OQ-004 watch) |
| FR-067 | odoo | hr.payslip.line (SS rules) | 2.67 / 6.68 legs | Art. 99 medical-only invariant; routing is config with SOQ-15 OQ |
| FR-068 | odoo | hr.payslip.line (SS rules) | both-shares mode | Voluntary = worker pays 3.00 + 7.50; no employer cost line |
| FR-069 | odoo | hr.payslip | sv_pay_isss_base | Matrix proxy via 01 FR-004 flags; l10n_sv.pay.ss.fallback EMPTY until Reglamento (SOQ-15) |
| FR-070 | odoo | hr.payslip.line (SS worker leg) | cap clamp | min(3% × base, 30.00); value-level only; never derive base; employer share unclamped pending OQ-007 |
| FR-071 | odoo | salary-rule constraint + payslip check | no-deduction invariant | Art. 33; rejection of any employer-share pass-through; remittance/recargo owned by 06 |
| FR-072 | odoo | hr.payslip.line (SIP rules) | 7.25/8.75 legs + sv_pay_sip_destination | 9.0 = 7.25w + 1.75e; 6.0 solidarity e; 1.0 commission e |
| FR-073 | odoo | rule constraint + payslip invariant | worker leg = exactly 7.25% × IBC | Art. 16 final inciso; blocks posting on violation |
| FR-074 | odoo | res.partner / hr.payslip.line | independent full-share row | Art. 15; 16% over declared income, no employer line |
| FR-075 | odoo | hr.payslip | sv_pay_ibc = Σ sv_pay_ibc_included lines | 01 FR-004 matrix consumed by id; no matrix restated |
| FR-076 | odoo | hr.payslip | floor = sector SMM row | 02 smm_2025.csv via SV-PAY-FR-011/FR-022; Normativa Técnica exceptions OQ-004 |
| FR-077 | odoo | hr.payslip (computation) | calendar-day denominators 30/31 | Art. 14; mid-month proration by calendar days |
| FR-078 | odoo | hr.payslip (per employer) | per-salary cotización | No cross-employer aggregation of IBC/floors/caps |
| FR-079 | odoo | hr.payslip | subsidy-month base | IBC = subsidio respectivo; subsidy values owned by 07; license-month remittance timing owned by 06 |
| FR-080 | odoo | config slot only | sv_pay_art14_riskpensioner_base | No mechanics until OQ-006 pins the truncated article text |
| FR-081 | odoo | l10n_sv.pay.ss.parameter | CSV seeding | Version regime (D12): law-anchored rates (1953-12-11 / 2022-12-29 vintages) + print-anchored caps (2025-10-01) with SOQ-15/16/17 OQ refs |
| FR-082 | odoo | hr.payslip.line (SIP worker leg) | cap clamp | min(7.25% × IBC, 472.93); value-level only; never derive IBC ceiling (SOQ-16) |
| FR-083 | odoo | l10n_sv.pay.ss.parameter (instituto cap rows) | %-maxima only | INPEP 7.5 / IPSFA 9.5 / CEFAFA 5 / Bien.Mag. 5.58 / ISSS-IVM 7.5; no invented splits (SOQ-17) |
| FR-084 | odoo | l10n_sv.pay.ss.parameter → l10n_sv.f14.ss.cap mirror | provenance chain | SOQ-11: payroll owns values; SV-FREP-FR-145/150 mirror; netting = SV-TAX-FR-104 by id |
| FR-085 | odoo | l10n_sv.pay.ss.parameter (pensioner rows) | adjacent config | 7.80% health (R23; never the 6%) + 7% solidarity >6×PM; no employer-payroll rule attached |

Version-regime notes (D12): the sidecar carries two vintages of
provenance — law-anchored rate rows (ISSS: D.L. 1263 print, rates
stable per the reform tail through D.L. 45-1994, 08_ OQ-2 watch; SIP:
D.L. 614 effective 2022-12-29) and print-anchored cap rows (F-14 v16
manual, Oct-2025 print, values dated 2025-10-01 with SOQ-15/16/17
instrument OQs — the caps' operative-since dates are unknown until the
instruments are acquired, and the rows re-date on acquisition). The
SMM floor rows re-seed per SMM decree (owned by 02's sidecar).

## 6. Acceptance Criteria

- **AC-001:** Given a sip-regime worker with monthly IBC US$1,000.00,
  then the SIP posting carries: worker deduction 7.25% = US$72.50
  (destination: individual account) and employer cost 8.75% =
  US$87.50 split into legs individual account 1.75% = US$17.50 ·
  garantía solidaria 6.0% = US$60.00 · AFP commission 1.0% =
  US$10.00 — the individual account totals 9.0% = US$90.00
  (FR-072).
- **AC-002:** Given the same worker, any salary-rule configuration
  producing a worker-side SIP deduction ≠ 7.25% of IBC (e.g. 8.25%,
  shifting the employer's 1-point increment) is REJECTED at
  configuration time and, if it reaches a payslip, blocks posting
  (FR-073).
- **AC-003:** Given a December payslip with ordinary pay US$500.00,
  commissions US$200.00 and aguinaldo US$400.00, then the IBC =
  500 + 200 = US$700.00 — the commissions are IN and the aguinaldo
  OUT, taken exclusively from the sv_pay_ibc_included flags of
  `01_salary-model.md` SV-PAY-FR-004 (FR-075).
- **AC-004:** Given an ISSS general-regime worker with monthly
  remuneración afecta US$1,500.00, then the worker share computes
  3% = US$45.00 and CLAMPS to US$30.00 (the F-14 print cap), while
  the employer share posts 7.5% = US$112.50 over the unclamped base
  — and no implied base ceiling is asserted anywhere in the record
  (FR-066, FR-070).
- **AC-005:** Given a sip-regime worker with monthly IBC US$7,000.00,
  then the AFP worker-share cotización computes 7.25% = US$507.50
  and CLAMPS to US$472.93 as the value feeding F-14 column L —
  value-level clamp only, with the cap-provenance row recorded
  (FR-082).
- **AC-006:** Given three employees of one employer — (a) an
  AFP-affiliated private worker, (b) an IPSFA-covered worker
  (Art. 11 exclusion), (c) a worker routed to the Art. 99 public
  special regime — then (a) applies the sip + isss_general parameter
  rows, (b) carries sv_pay_ss_regime = instituto_ipsfa with NO SIP
  cotización lines, and (c) applies 6.68%/2.67% with no money-benefit
  accruals (FR-064, FR-065, FR-067).
- **AC-007:** Given a comercio-y-servicios worker whose calendar-month
  ordinary pay is US$350.00 (below the sector SMM row US$408.80
  loaded from `smm_2025.csv` per SV-PAY-FR-011), then the IBC floors
  at US$408.80 and the SIP shares compute worker 7.25% = US$29.64 /
  employer 8.75% = US$35.77; for an aprendiz flagged under the
  sector-exception config, the sector-associated SMM row selected by
  that config governs instead (FR-076).
- **AC-008:** Given a worker hired 12-March with monthly salary
  US$620.00 (a 31-day month, 20 calendar days employed), then the
  IBC = 620 × 20/31 = US$400.00 before any floor evaluation (FR-077).
- **AC-009:** Given a worker employed by two employers at US$400.00
  and US$300.00 in the same month, then each employer cotizes on its
  own salary (e.g. SIP worker shares US$29.00 and US$21.75) with no
  aggregation, floor offset or cap sharing across employers (FR-078).
- **AC-010:** Given a worker on an illness license whose subsidy for
  the month is US$306.00, then that month's IBC = US$306.00 (the
  subsidio respectivo in place of the salary); the license-month
  remittance timing is asserted by id against
  `06_ss-declaration-remittance.md`, never here (FR-079).
- **AC-011:** Given a voluntarily insured worker with remuneración
  afecta US$500.00, then the ISSS deduction is BOTH shares
  3.00% + 7.50% = US$52.50 with zero employer cost line (FR-068).
- **AC-012:** Given a pensioner with monthly pensión US$1,500.00 and
  a pensión mínima of US$400.00, then the adjacent config computes
  health 7.80% = US$117.00 (per Art. 154/R23 — the 6% of 08_ Art. 29
  is never applied) and NO solidarity 7% row fires (1,500 ≤
  6 × 400 = 2,400); at pensión US$2,500.00 the 7% solidarity row
  would fire — both as pensioner-regime rows with no employer-payroll
  computation (FR-085).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-15 carried: the ISSS **Reglamento de Aplicación is absent** — it alone fixes the Art. 3 high-income exclusion threshold, the cotizable-base CAP behind the F-14 ISSS $30.00 print, the Art. 34 variable-income/in-kind/presumed-SMM base tables, and the remittance/planilla mechanics. Until acquired: exclusion = config only (FR-063), cap = value-level print clamp (FR-070), fallback tables EMPTY (FR-069). Acquisition candidate (≥66). | no | Takumi S4 (sources watch) | open |
| OQ-002 | SOQ-16 carried: the SIP **IBC-ceiling instrument is absent** — no base cap appears in D.L. 614; the F-14 v16 print caps AFP at US$472.93. The instrument (BCR Norma Técnica? SIP transitory?) is unacquired; the value stands as print-anchored dated data (FR-082) and NO implied IBC ceiling is ever derived from it. | no | Takumi S4 (sources watch) | open |
| OQ-003 | SOQ-17 carried: the **D.L. 614 Reglamento + BCR Normas Técnicas + the institutos' rate laws are absent** (INPEP/IPSFA/CEFAFA/Bienestar Magisterial/ISSS-IVM; planilla-única spec; acreditación windows) — the institutos' worker/employer splits are unknown, so only the F-14 %-maxima print rows ship (FR-083); never invent a split. Acquisition optional (public-sector employers only). | no | Takumi S4 (sources watch) | open |
| OQ-004 | SMM floor exceptions (SIP Art. 14): the floor excepts "aprendices, trabajadores agrícolas, domésticos y otros" considering the "salarios mínimos de los sectores asociados" per the **Normativa Técnica** (likely the SAP-era BCR normas surviving per Art. 159 unless contrary — unacquired). FR-076 ships config slots; the association rule (which sector SMM for each exception class) needs the Normativa. Kin of 02's OQ-002 sector-mapping question. | no | Takumi S4 (payroll config) | open |
| OQ-005 | ISSS remuneración afecta vs SIP IBC divergence: 08_ gives no statutory in/out list (reglementary, absent) while 09_ Art. 14 does; FR-069 uses the 01 FR-004 matrix flags as the operational proxy for BOTH. If the acquired ISSS Reglamento's list diverges from Art. 14 (e.g. on a category the matrix marks), the ISSS base builder forks to its own list — re-key on acquisition (SOQ-15 kin). | no | Takumi S4 (sources watch) | open |
| OQ-006 | Art. 14 final provisions truncated in the evidence extract (EVID-197 verbatim cut mid-article): the **pensioner riesgos-profesionales IBC base rule** and the calendar-day/multi-job clauses' exact wording need a source re-read. FR-077/FR-078 implement the master-index gloss; FR-080 ships NO mechanics until pinned. | no | Takumi S4 (evidence re-read) | open |
| OQ-007 | ISSS cap applicability to the employer share: the F-14 prints $30.00 as the ISSS column (worker cotización) maximum; whether the absent reglamento ceiling binds the employer 7.50% share too is unknown — FR-070 leaves the employer share over the unclamped base pending the instrument (SOQ-15 kin). | no | Takumi S4 (sources watch) | open |
| OQ-008 | Riesgos profesionales rate fold (08_ OQ-3 carried): Art. 29 folds riesgos profesionales into the general 7.5%/3% with no separate employer accident rate; any later decree splitting it out would supersede — watch during Reglamento acquisition and at re-dating of the ss_contributions.csv rate rows. | no | Takumi S4 (sources watch) | open |
