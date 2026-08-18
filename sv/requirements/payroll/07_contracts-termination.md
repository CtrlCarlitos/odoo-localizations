# SV — Payroll — Contracts, termination and indemnización: contract taxonomy, severance, constancia, illness and maternity benefits

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the El Salvador contract and termination layer of the
Código de Trabajo (Labor Code, CT): the contract taxonomy of Arts. 25-28 —
the INDEFINITE presumption (a *plazo* / fixed-term stipulation is valid
only for transitory, temporary or eventual labors; permanent labor
contracts are indefinite despite any written term), *obra* (specific-work)
contracts with the 7-day termination notice or 7 days' pay in lieu,
*interinos* (substitute workers) with return-termination and the >15-day
post-return permanence presumption, and the 30-day trial period with the
no-second-trial-within-a-year rule — every type ROUTING its termination
outcomes; the unjustified-dismissal *indemnización* (severance) of Arts.
58-59 — 30 days' *salario básico* per year of services plus prorated
fractions, minimum 15 days, with the countable salary CAPPED at 4× the
daily legal *salario mínimo* (SMM, minimum wage — the cap arithmetic this
file owns, resolving `02_minimum-wage.md` SV-PAY-FR-023's forward
reference), and the fixed-term variant capped at the indefinite
equivalent; the termination *constancia* (certificate) content model of
Art. 60 and the *despacho de hecho* (de-facto dismissal) presumption of
Art. 55; the employer-side illness subsidies of Arts. 307-308-B (75% of
básico with the 60/40/20 seniority-tier day caps, the grave-fault
exception, and chronic-illness stability with full ISSS subsidy); the
maternity engine of Arts. 309-312 (16 weeks at 75% of básico with 10
mandatory post-partum weeks, prenatal supplement and late-birth
extension, the deductible ISSS money subsidy, the no-pay-beyond-limits
rule, the VOID Art. 311 tenure gate — never implementable per sent.
105-2014 — the post-licencia sickness continuation and the paid
*lactancia* (breastfeeding) breaks) and the *sepelio* (burial) help of
Art. 313 (60 days of básico); and the termination-settlement wiring where
the vacation and aguinaldo termination prorations of
`04_statutory-benefits.md` (its SV-PAY-FR-051/SV-PAY-FR-058) plug in by
id.

It does **not** cover: the *salario* / *salario básico* model and the
canonical earning-category matrix (`01_salary-model.md` — the stored rates
of SV-PAY-FR-005 and the classification flags of SV-PAY-FR-004 are
consumed by id, never restated); the SMM chassis, dated tariff tables and
the SMM sector-mapping configuration (`02_minimum-wage.md` — this file
consumes its SV-PAY-FR-011 sidecar rows, its SV-PAY-FR-021 benefit-base
max rule and its SV-PAY-FR-022/FR-023 cap feed, and owns only the 4×SMM
cap ARITHMETIC); jornada, surcharges and descanso/asueto pay
(`03_working-time-surcharges.md`); the vacaciones and aguinaldo
computation engines (`04_statutory-benefits.md` — its prorations
SV-PAY-FR-051/SV-PAY-FR-058 land in this file's settlement surface);
social-security rates, caps, IBC and declaration/remittance
(`05_social-security-contributions.md`, `06_ss-declaration-remittance.md`
— the ISSS subsidy interface is consumed as the money-subsidy record,
never re-derived); ISR/F-14 interfaces (`08_isr-interfaces.md`, task 8);
the ISR retention constancia of CT Art. 145 (owned by
`taxation/04_isr-withholding.md`); and the riesgos-profesionales
(work-accident) indemnización of Arts. 336-366 (insurer-side, deferred —
11_ OQ-4). Those files consume this one for contract typing, severance
and the illness/maternity/sepelio prestaciones.

## 2. Legal Basis

Authority order (binding, per master evidence index S4): labor = 11_
(Código de Trabajo, D.L. 15-1972, Índice Legislativo edition, reform
stamps (1)-(22) — SOQ-21 watch); SMM feed = 16_ (Decreto 11-2025) as
dated data OWNED by `02_minimum-wage.md`'s `smm_2025.csv` sidecar and
consumed by FR id; the salary/básico model and category matrix are
consumed from `01_salary-model.md` by FR id.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código de Trabajo, Art. 25: contracts for permanent labor are INDEFINITE despite any stipulated *plazo* (term); a plazo stipulation is valid only when the labor is by nature transitory, temporary or eventual; in doubt the contract is presumed indefinite | Indefinite-presumption rule: fixed terms bind only for transitory/temporary/eventual work; permanent-labor contracts are indefinite whatever the paper says | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 25, Arts. 25-28 pp.6-7 (EVID-207) |
| LB-002 | Código de Trabajo, Art. 26: *obra* (specific-work) contracts are plazo contracts; once the work extends beyond fifteen days, termination requires seven days' advance notice, or the payment of seven days' salary in its place | Obra contracts: after >15 days of work the employer must give 7-day termination notice or pay 7 days' salary in lieu | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 26, Arts. 25-28 pp.6-7 (EVID-207) |
| LB-003 | Código de Trabajo, Art. 27: *interinos* (substitute workers) terminate without employer responsibility upon the return of the substituted titular; if the interim remains in the post more than fifteen days after the titular's return, permanence is presumed | Interinos: return-termination without responsibility; >15 days of post-return permanence converts the contract by presumption | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 27, Arts. 25-28 pp.6-7 (EVID-207) |
| LB-004 | Código de Trabajo, Art. 28: a thirty-day trial period applies (no-cause termination by either party); no second trial period may be stipulated within one year for the same labor | 30-day trial: termination without cause inside the window; a repeat trial for the same labor within a year is prohibited | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 28, Arts. 25-28 pp.6-7 (EVID-207) |
| LB-005 | Código de Trabajo, Art. 55: when the worker is denied entry to the workplace, the dismissal (*despacho*) is presumed | De-facto dismissal presumption: denial of entry raises the presumption of dismissal, shifting the burden to the employer | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 55, Arts. 55-60 pp.20-21 (EVID-207) |
| LB-006 | Código de Trabajo, Art. 58 (stamps (6)(8)): "Cuando un trabajador contratado por tiempo indefinido, fuere despedido de sus labores sin causa justificada, tendrá derecho a que el patrono le indemnice con una cantidad equivalente al salario básico de treinta días por cada año de servicios y proporcionalmente por fracciones de año. En ningún caso la indemnización será menor del equivalente al salario básico de quince días. PARA LOS EFECTOS DEL CALCULO ... NINGUN SALARIO PODRA SER SUPERIOR A CUATRO VECES EL SALARIO MINIMO DIARIO LEGAL VIGENTE." | An indefinite-contract worker dismissed without just cause is owed a severance equal to 30 days' basic salary per year of services and proportionally for year fractions, never below 15 days' basic salary; for the calculation NO salary may exceed four times the current legal daily minimum wage | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 58, Arts. 55-60 pp.20-21 (EVID-207) |
| LB-007 | Código de Trabajo, Art. 59: unjustified dismissal of a fixed-term (plazo) worker = the salario básico of the REMAINING term, capped at the indefinite-contract indemnización of Art. 58 | Fixed-term variant: severance equals the básico of the unexpired term, but never more than the Art. 58 indefinite-equivalent amount | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 59, Arts. 55-60 pp.20-21 (EVID-207) |
| LB-008 | Código de Trabajo, Art. 60: on termination the employer must issue a constancia stating the service dates, the class of work performed and the salary of the last period; efficiency/behavior and termination causes may optionally be included | Termination constancia: mandatory content = entry/exit dates, work class, last-period salary; optional content = efficiency/behavior and termination causes | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 60, Arts. 55-60 pp.20-21 (EVID-207) |
| LB-009 | Código de Trabajo, Art. 187: proportional vacation pay on termination with employer responsibility or despacho de hecho; completed qualifying year ⇒ full pay regardless of responsibility — interface anchor only; the proration computation is OWNED by `04_statutory-benefits.md` SV-PAY-FR-051 and consumed by reference | Vacation-proration interface: this file supplies only the termination-responsibility routing; the quantum is file 04's | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 187 pp.41-42 (EVID-204; via 04 FR-051) |
| LB-010 | Código de Trabajo, Art. 202: proportional aguinaldo on termination with employer responsibility / despacho de hecho before 12-December — interface anchor only; the proration computation is OWNED by `04_statutory-benefits.md` SV-PAY-FR-058 and consumed by reference | Aguinaldo-proration interface: same routing supply; the quantum is file 04's | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 202 pp.43-44 (EVID-206; via 04 FR-058) |
| LB-011 | Decreto 11-2025, Art. 7: "El pago de las prestaciones que establece el Código de Trabajo ... como día de asueto, vacaciones, aguinaldo, indemnizaciones y otras, se hará con base al salario mínimo diario establecido, excepto cuando el salario estipulado sea mayor." — interface anchor only; the base rule is OWNED by `02_minimum-wage.md` SV-PAY-FR-021 (benefit base = max(actual daily salary, sector daily SMM)) and consumed by reference | Benefit-base interface: indemnización and the illness/maternity/sepelio prestaciones compute on max(actual daily salary, sector daily SMM) — the max rule and the dated rows are file 02's | `sv/sources/16_Salarios_Minimos_2025.pdf` | Art. 7 p.20 (EVID-192; via 02 FR-021) |
| LB-012 | `smm_2025.csv` daily tariff rows (Decreto 11-2025 Art. 2, dated data OWNED by `02_minimum-wage.md` SV-PAY-FR-011, sector selection per its SV-PAY-FR-022 `indemnizacion_cap_4x` mapping row, feed duty per its SV-PAY-FR-023) — interface anchor only: line 3 (agricola · day · $10.035), line 6 (industria · day · $13.440), line 9 (comercio_y_servicios · day · $13.440), line 12 (maquila_textil_y_confeccion · day · $13.227), all valid_from 2025-06-01 | The 4×SMM cap reads the DAILY tariff row selected by the FR-022 mapping from the sidecar — e.g. the documented comercio_y_servicios default ⇒ cap 4 × $13.440 = US$53.76/day; the rows are file 02's dated data, never restated as constants of this file | `sv/requirements/payroll/smm_2025.csv` | lines 3/6/9/12 (EVID-191; via 02 FR-011/FR-022/FR-023) |
| LB-013 | Código de Trabajo, Art. 307: common illness or accident suspension → the patrono pays 75% of the salario básico by seniority tiers: PRIMERA (≥1 year of service): 60 days/year; SEGUNDA (5 months to 1 year): 40 days; TERCERA (1 to 5 months): 20 days; promotion between tiers nets the days already enjoyed; tier dates run from service start (reset if the contract dissolves and is re-contracted) | Illness subsidy: 75% of básico with seniority-tier day caps 60/40/20; tier promotion nets already-used days; tier clocks from hire date, reset on dissolve-and-recontract | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 307, Arts. 307-313 pp.67-69 (EVID-209) |
| LB-014 | Código de Trabajo, Art. 308: no subsidy payment when the illness proceeds from the worker's grave fault (requires a judicial finding; restitution if paid) | Grave-fault exception: subsidy denial needs a judicial grave-fault finding; amounts paid are restitutable | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 308, Arts. 307-313 pp.67-69 (EVID-209) |
| LB-015 | Código de Trabajo, Art. 308-A (stamp (19)): chronic-incapacitating illness → no dismissal and no salary discounts; job stability runs from diagnosis to three months after the end of treatment (the Art. 50 termination causes excepted) | Chronic-illness stability: dismissal ban + no salary discounts from diagnosis to 3 months post-treatment, excepting the CT Art. 50 legal termination causes | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 308-A, Arts. 307-313 pp.67-69 (EVID-209) |
| LB-016 | Código de Trabajo, Art. 308-B (stamp (19)): the ISSS covers the FULL daily subsidy for the Art. 308-A chronic cases | Full-subsidy displacement: for chronic cases ISSS pays the whole daily subsidy — the employer-side 75% engine does not apply | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 308-B, Arts. 307-313 pp.67-69 (EVID-209) |
| LB-017 | Código de Trabajo, Art. 309 (stamp (15)): "EL PATRONO ESTÁ OBLIGADO A DAR A LA TRABAJADORA EMBARAZADA, EN CONCEPTO DE DESCANSO POR MATERNIDAD, DIECISÉIS SEMANAS DE LICENCIA, DIEZ DE LAS CUALES SE TOMARÁN OBLIGATORIAMENTE DESPUÉS DEL PARTO; Y ADEMÁS, A PAGARLE ANTICIPADAMENTE UNA PRESTACIÓN EQUIVALENTE AL SETENTA Y CINCO POR CIENTO DEL SALARIO BÁSICO DURANTE DICHA LICENCIA."; prenatal supplementary rest (per reglamento); late birth → the prenatal rest is extended and the puerperal ten weeks remain uncut; no payment obligation beyond the 16-week limits; "EL PATRONO PODRÁ DEDUCIR ... EL EQUIVALENTE DE LO QUE LA TRABAJADORA HUBIESE RECIBIDO A TÍTULO DE SUBSIDIO EN DINERO EN VIRTUD DE LA LEY DEL SEGURO SOCIAL" (stamp (8)); Art. 310: a medical constancia on simple paper suffices | Maternity: 16 weeks of licencia, 10 mandatorily post-partum, paid IN ADVANCE at 75% of básico during the licencia; prenatal supplement and late-birth extension (puerperal 10 weeks uncut); employer payment never exceeds the 16-week quantum; the ISSS money subsidy received is deductible; a simple-paper medical certificate suffices | `sv/sources/11_Codigo_Trabajo.pdf` | Arts. 309-310, Arts. 307-313 pp.67-69 (EVID-209) |
| LB-018 | Código de Trabajo, Art. 311 — VOID: the six-month prior-employment requirement "QUEDÓ DEROGADA TÁCITAMENTE ... NO PUEDE PRODUCIR EFECTO JURÍDICO ALGUNO" per Sala de lo Constitucional sentencia 105-2014 (D.O. No. 225, Tomo 417, 1-dic-2017); the benefit has NO tenure gate — the licencia is always owed | Dead text: any prior-employment minimum for the maternity benefit is unconstitutional-by-derogation; the system may never condition Art. 309 on tenure | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 311 + notes block pp.140-141 (EVID-209) |
| LB-019 | Código de Trabajo, Art. 312: post-licencia medical continuation (suspension with the illness benefits and the job kept); lactancia: "INTERRUPCION DEL TRABAJO DE HASTA UNA HORA DIARIA ... SE PODRÁ FRACCIONAR EN DOS PAUSAS DE TREINTA MINUTOS ... CONTADAS COMO HORAS DE TRABAJO Y REMUNERADAS COMO TALES" (stamp (8)) | A worker still medically unfit at licencia end continues under suspension with illness benefits and job retention; lactancia = up to one hour's daily work interruption, fractionable into two 30-minute pauses, counted and remunerated as work time | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 312, Arts. 307-313 pp.67-69 (EVID-209) |
| LB-020 | Código de Trabajo, Art. 313: on the worker's death the employer gives immediate sepelio (burial) help of sixty days of salario básico; the printed "doscientos cincuenta colones" floor is a colon-era remnant (11_ OQ-2 — day count governs, never the ¢ figure) | Death benefit: immediate payment of 60 days of básico; the 250-colon floor is dead print recorded as an LB note only | `sv/sources/11_Codigo_Trabajo.pdf` | Art. 313, Arts. 307-313 pp.67-69 + notes (EVID-209) |
| LB-021 | Código de Trabajo, Art. 119 final clause ("ni tampoco las prestaciones sociales de que trata este Código") + Ley Integral del Sistema de Pensiones (D.L. 614) Art. 14 c) — interface anchors only; the classification matrix is OWNED by `01_salary-model.md` SV-PAY-FR-004 and consumed by reference | Interface: the indemnización, illness/maternity subsidies and sepelio are prestaciones sociales — NOT salario, NOT IBC (14.c); ISR gravada classification carries crosscheck_oq per the 01-matrix row (its OQ-003, resolved in `08_isr-interfaces.md`) | `sv/sources/11_Codigo_Trabajo.pdf` + `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 119 p.31 (EVID-201); Art. 14 pp.6-7 (EVID-197; via 01 FR-004) |

Dead text — never implementable as current law (LB notes, not FRs): CT
Art. 311's six-month prior-employment requirement is VOID (tacitly
derogated; sent. 105-2014, D.O. 225 T.417 1-dic-2017 — LB-018; FR-115
turns it into a NEVER-implement invariant). Art. 313's "doscientos
cincuenta colones" (¢250) sepelio floor is a colon-era remnant of
pre-dollarization print — the 60-day count governs and no ¢/$ conversion
is ever applied (LB-020; kin of the Art. 142 "treinta colones" note in
`01_salary-model.md` — 11_ OQ-2). CT vintage note (SOQ-21): the 11_ copy
is the Índice Legislativo edition with reform stamps (1)-(22) and no
as-of date; the articles cited here (25-28, 55-60, 307-313) cross-check
consistent with the post-2017 consolidation — re-verify if a later CT
reform lands (kin of file 01's OQ-001).

Version regime (D12): NO dated data is owned by this file — the only
dated values consumed are the SMM daily tariff rows of `smm_2025.csv`
(owned by `02_minimum-wage.md` SV-PAY-FR-011, re-seeded per SMM decree)
selected through its SV-PAY-FR-022 mapping; every other value cited here
(30/15 days, 4× multiplier, 75%, 60/40/20 caps, 16 weeks, 10 weeks, 1
hour/2×30 minutes, 60 days) is STATIC law (CT Arts. 25-28, 55-60,
307-313).

## 3. Functional Requirements

### 3.1 Contract taxonomy — routing termination outcomes (CT Arts. 25-28)

- **SV-PAY-FR-101:** The system shall classify every employment contract
  into exactly one taxonomy type — *indefinido* (indefinite), *plazo*
  (fixed-term), *obra* (specific work) or *interino* (substitute) — and
  shall enforce the Art. 25 indefinite presumption as a VALIDATION GATE:
  a plazo stipulation is accepted ONLY when the recorded labor nature is
  transitory, temporary or eventual; a contract whose labor nature is
  permanent classifies INDEFINITE regardless of any written term, and the
  plazo gate failure is recorded on the contract (the classification
  drives every termination-outcome route of FR-102..FR-110: only
  indefinite-contract unjustified dismissals take the Art. 58
  indemnización of FR-105). (LB-001; EVID-207)
- **SV-PAY-FR-102:** The system shall treat obra contracts as
  term-limited by the work itself and shall enforce the Art. 26 exit
  protocol once the work has extended beyond FIFTEEN days: termination
  requires a SEVEN-DAY advance notice, or the payment of SEVEN DAYS'
  salary in lieu (a 7 × daily salario básico line emitted when notice is
  not given); completion of the obra terminates without employer
  responsibility (no indemnización route). (LB-002; EVID-207)
- **SV-PAY-FR-103:** The system shall terminate interino contracts
  WITHOUT employer responsibility upon the recorded return of the
  substituted titular (no indemnización route), and shall apply the
  Art. 27 permanence presumption: an interim who remains in the post
  MORE THAN FIFTEEN DAYS after the titular's return is presumed
  permanent — the contract reclassifies to indefinite with effect from
  the day following the fifteenth, opening the FR-105 indemnización
  route for any later dismissal. (LB-003; EVID-207)
- **SV-PAY-FR-104:** The system shall support a THIRTY-DAY trial period
  per Art. 28 during which either party may terminate WITHOUT cause (no
  indemnización, no proration gate beyond earned balances), and shall
  enforce the no-second-trial rule as a validation: a trial period may
  not be stipulated for a worker re-hired for the SAME labor within one
  year of a prior trial (lookup across the worker's prior contracts;
  violation raises a blocking validation, never a silent accept).
  (LB-004; EVID-207)

### 3.2 Indemnización engine (CT Arts. 58-59)

- **SV-PAY-FR-105:** The system shall compute the unjustified-dismissal
  indemnización for INDEFINITE-contract workers (Art. 58) as
  countable_base × day_credit where day_credit = 30 × years of services
  + 30 × fraction-of-year (fractions prorated; denominator defaulted to
  365 days — corpus-silent, OQ-001), subject to the FIFTEEN-DAY MINIMUM
  (day_credit floor = 15 regardless of tenure); the countable_base is
  the daily salario básico selected per the benefit-base max rule of
  `02_minimum-wage.md` SV-PAY-FR-021 — max(stored daily básico per
  `01_salary-model.md` SV-PAY-FR-005, sector daily SMM) — and then
  CAPPED per FR-106; eligibility routes: unjustified dismissal of an
  indefinite contract only (trial-period FR-104, interino-return
  FR-103, obra-completion FR-102 and justified dismissals never open
  this FR). (LB-006; LB-011; EVID-207/192)
- **SV-PAY-FR-106:** The system shall own and apply the 4×SMM cap
  arithmetic of Art. 58 (resolving the forward reference of
  `02_minimum-wage.md` SV-PAY-FR-023): the countable daily salary for
  the indemnización computation shall be
  countable_base = min(benefit_base (FR-105 selection), 4 × daily SMM),
  where the daily SMM is the dated row read from the `smm_2025.csv`
  sidecar of `02_minimum-wage.md` (loaded per its SV-PAY-FR-011) at the
  row selected by its SV-PAY-FR-022 `indemnizacion_cap_4x` sector
  mapping — documented default: the comercio_y_servicios daily row
  (`smm_2025.csv` line 9, $13.440 valid_from 2025-06-01 ⇒ cap
  US$53.76/day), alternates when configured: agricola line 3 ($10.035),
  industria line 6 ($13.440), maquila_textil_y_confeccion line 12
  ($13.227); the article names NO sector ("salario mínimo diario legal
  vigente" — EVID-207 doubt), so the selection stays configurable and
  the pinning question rides `02_minimum-wage.md` OQ-002 (SOQ-18 kin —
  this file's OQ-002); the cap value is NEVER hardcoded — it re-seeds
  per SMM decree through the sidecar rows. (LB-006; LB-012; LB-011;
  EVID-207/191)
- **SV-PAY-FR-107:** The system shall compute the fixed-term (plazo)
  variant of Art. 59 for unjustified dismissals of valid plazo contracts
  (FR-101 gate passed): quantum = the salario básico of the REMAINING
  TERM, computed on the same capped countable_base of FR-106, and
  CAPPED at the indefinite-contract equivalent —
  min(remaining_term_days × countable_base, FR-105 quantum for the same
  worker); the Art. 58 minimum-15-days floor does not extend the
  remaining-term pay (the cap only lowers it). (LB-007; LB-006;
  EVID-207)
- **SV-PAY-FR-108:** The system shall record a *despacho de hecho*
  (de-facto dismissal) event per Art. 55: a worker whose entry to the
  workplace is denied is presumed DISMISSED — the event carries the
  denial date and shifts the burden to the employer record; the
  presumption routes the termination as employer-responsibility for
  every consumer: the Art. 58 indemnización (FR-105), the vacation
  proration of `04_statutory-benefits.md` SV-PAY-FR-051 and the
  aguinaldo proration of its SV-PAY-FR-058 (both gate on "employer
  responsibility or despacho de hecho" — this FR owns the presumption
  event they consume). (LB-005; LB-009; LB-010; EVID-207)

### 3.3 Termination flow: constancia and settlement wiring (CT Arts. 60, 187, 202)

- **SV-PAY-FR-109:** The system shall issue on every termination the
  Art. 60 *constancia de trabajo* (work certificate) with MANDATORY
  content — service entry and exit dates, the class of work performed,
  and the salary of the last period — plus OPTIONAL content emitted only
  when flagged (efficiency/behavior report; termination causes); the
  document is generated from the termination record and the last
  payslip, and is DISTINCT from the ISR retention-credits constancia of
  CT Art. 145 (owned by `taxation/04_isr-withholding.md` — different
  duty, never merged). (LB-008; EVID-207)
- **SV-PAY-FR-110:** The system shall assemble the termination
  settlement as the single surface where every termination-driven
  payment wires in BY ID, never restated: (a) the indemnización of
  FR-105/FR-107 (indefinite/plazo variants, despacho-presumed or
  declared unjustified); (b) the vacation termination proration of
  `04_statutory-benefits.md` SV-PAY-FR-051 (proportional on employer
  responsibility/despacho de hecho; completed qualifying year ⇒ full
  pay — all arithmetic owned there); (c) the aguinaldo termination
  proration of `04_statutory-benefits.md` SV-PAY-FR-058 (pre-12-December
  employer-responsibility terminations — mechanics owned there); the
  settlement emits the constancia of FR-109 and pays sepelio per FR-119
  when the termination is the worker's death. (LB-009; LB-010; EVID-204/
  206/207)

### 3.4 Illness subsidies (CT Arts. 307-308-B)

- **SV-PAY-FR-111:** The system shall pay the common-illness/accident
  suspension subsidy at SEVENTY-FIVE PERCENT of the salario básico
  (base selected per `02_minimum-wage.md` SV-PAY-FR-021 max rule) with
  the Art. 307 seniority-tier day caps: TERCERA tier (1-5 months of
  service) = 20 days; SEGUNDA tier (5 months-1 year) = 40 days; PRIMERA
  tier (≥1 year) = 60 days per anniversary year — tier windows measured
  from service start (anniversary years; OQ-005), reset when a dissolved
  contract is re-contracted; on promotion between tiers the cap nets the
  days ALREADY ENJOYED under the lower tier (head-room = new cap − used
  days); days beyond the cap accrue no employer subsidy (unpaid
  suspension, continuity preserved per the Art. 181 family recorded in
  `04_statutory-benefits.md` SV-PAY-FR-046). (LB-013; LB-011;
  EVID-209/192)
- **SV-PAY-FR-112:** The system shall deny the illness subsidy ONLY on
  a recorded JUDICIAL grave-fault finding that the illness proceeds from
  the worker's *grave culpa* (Art. 308): the denial requires the finding
  reference; subsidies already paid against a later finding are flagged
  for restitution — no discretionary, employer-unilateral denial path
  exists. (LB-014; EVID-209)
- **SV-PAY-FR-113:** The system shall implement the chronic-illness
  stability regime of Arts. 308-A/308-B: from the recorded diagnosis of
  a chronic-incapacitating illness until THREE MONTHS after the end of
  treatment, the worker may NOT be dismissed and suffers NO salary
  discounts (the CT Art. 50 legal termination causes excepted — the
  dismissal block raises a blocking validation except for recorded
  Art. 50 causes), and the employer-side 75% engine of FR-111 is
  DISPLACED: the ISSS covers the FULL daily subsidy for these cases, so
  no employer subsidy line is emitted while the case is active.
  (LB-015; LB-016; EVID-209)

### 3.5 Maternity and lactancia (CT Arts. 309-312)

- **SV-PAY-FR-114:** The system shall schedule the maternity *descanso*
  (rest) as SIXTEEN weeks of licencia with TEN weeks mandatorily
  post-partum: default split 6 weeks prenatal + 10 weeks post-partum
  (the 10 post-partum weeks are statutory and immovable; the prenatal
  portion is the residual, configurable up to 6 weeks); a LATE birth
  extends the prenatal rest day-by-day while the puerperal 10 weeks
  remain UNCUT; prenatal supplementary rest beyond the default split is
  a medical-certification-driven extension (reglamento mechanics not in
  corpus — OQ-004); the 75% prestación of FR-116 pays over this
  schedule, and a simple-paper medical constancia (Art. 310) suffices
  as the licencia evidence — no special form may be demanded.
  (LB-017; EVID-209)
- **SV-PAY-FR-115:** The system shall implement the Art. 311 VOID
  ruling as a NEVER-implement invariant: the maternity licencia and its
  75% prestación shall NEVER be conditioned on any prior-employment or
  tenure minimum — the six-month gate of Art. 311 is dead text per
  sent. 105-2014 (D.O. No. 225 T.417, 1-dic-2017: "QUEDÓ DEROGADA
  TÁCITAMENTE ... NO PUEDE PRODUCIR EFECTO JURÍDICO ALGUNO"); any
  configuration, rule or gate introducing a tenure condition on
  Art. 309 benefits is rejected as a validation error (the invariant is
  tested, not merely documented). (LB-018; LB-017; EVID-209)
- **SV-PAY-FR-116:** The system shall pay the maternity prestación
  ANTICIPADAMENTE (in advance) at SEVENTY-FIVE PERCENT of the salario
  básico (base per `02_minimum-wage.md` SV-PAY-FR-021) during the
  licencia, with TWO statutory boundaries: (a) the employer may DEDUCT
  the equivalent of the money subsidy the worker received or will
  receive from the ISSS by virtue of the Social Security Law (netting
  line: prestación − documented ISSS money subsidy, never below zero);
  and (b) NO payment obligation exists beyond the SIXTEEN-WEEK quantum
  — a late-birth extension (FR-114) lengthens the licencia, never the
  employer's paid weeks. (LB-017; EVID-209)
- **SV-PAY-FR-117:** The system shall continue a worker still medically
  unfit at the end of the maternity licencia under the Art. 312 first
  rule: the contract enters suspension with the ILLNESS benefits and
  the JOB KEPT — the case routes into the Art. 307 engine of FR-111
  (tier caps, 75%, netting; grave-fault exception) from the licencia's
  end date, with no dismissal route while suspended. (LB-019; LB-013;
  EVID-209)
- **SV-PAY-FR-118:** The system shall grant the *lactancia*
  (breastfeeding) break as an interruption of work of up to ONE HOUR
  DAILY, fractionable into TWO pauses of THIRTY MINUTES each, COUNTED
  AS HOURS OF WORK AND REMUNERATED AS SUCH (paid at the ordinary rate,
  inside the jornada — never an unpaid or discounted break); the
  eligibility window (child-age span) is corpus-silent in the 11_
  evidence and ships as a REQUIRED configuration parameter with no
  invented default (OQ-003). (LB-019; EVID-209)

### 3.6 Sepelio and classification interfaces (CT Art. 313; by-reference)

- **SV-PAY-FR-119:** The system shall pay, on the termination caused by
  the worker's death, the IMMEDIATE sepelio help of SIXTY DAYS of
  salario básico (60 × daily base per `02_minimum-wage.md`
  SV-PAY-FR-021; the payment is emitted on the death-termination event
  of FR-110 without probate or waiting); the printed "doscientos
  cincuenta colones" floor is a colon-era remnant recorded as an LB
  note ONLY — no colon figure, conversion or floor value is ever
  implemented (11_ OQ-2). (LB-020; LB-011; EVID-209)
- **SV-PAY-FR-120:** The system shall classify the indemnización,
  illness/maternity subsidy, lactancia-break and sepelio lines
  exclusively through the canonical mapping matrix of
  `01_salary-model.md` SV-PAY-FR-004 (consumed by id, never re-derived):
  each is *prestación social* — NOT salario (CT Art. 119 final clause),
  IBC EXCLUDED (SIP Art. 14 c), ISR gravada classification carrying the
  matrix's crosscheck_oq flag (its OQ-003, to be resolved in
  `08_isr-interfaces.md` against the Ley ISR Art. 4 exemption list),
  F-14 value feed via `08_isr-interfaces.md` when that file lands; no
  matrix row is restated here. (LB-021; EVID-201/197/209)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in the
client (wave default `odoo`; see §5). No sidecar lives next to this
file: the only dated data consumed is the SMM daily-row feed owned by
`02_minimum-wage.md` (`smm_2025.csv` lines 3/6/9/12 via its FR-011,
selected per its FR-022 mapping) — consumed by FR id.

**Contract taxonomy and termination routing:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | sv_pay_contract_type | select | indefinite · plazo · obra · interino | FR-101 |
| hr.contract (plazo) | sv_pay_labor_nature | select | transitory · temporary · eventual (Art. 25 validity gate; permanent → validation error, contract classifies indefinite) | FR-101 |
| hr.contract (obra) | sv_pay_obra_notice_due · sv_pay_obra_pay_in_lieu | date / monetary (computed) | >15 days of work ⇒ 7-day notice or 7 × daily básico in-lieu line | FR-102 |
| hr.contract (interino) | sv_pay_titular_return_date · sv_pay_permanence_date | date (computed) | return-termination; permanence presumed at >15 days post-return → reclassify indefinite from day 16 | FR-103 |
| hr.contract | sv_pay_trial_start · sv_pay_trial_end · sv_pay_trial_blocked | date/boolean (computed) | 30-day window; second-trial-within-a-year lookup across prior contracts (same labor) | FR-104 |
| hr.departure (termination) | sv_pay_termination_kind · sv_pay_unjustified · sv_pay_despacho_presumed | select/boolean | resignation · justified_dismissal · unjustified_dismissal · despacho_de_hecho (Art. 55 event: entry-denial date) · death · completion (obra/return/trial) | FR-105, FR-108, FR-110 |

**Indemnización engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.indemnizacion (new) | years · fraction_days · denominator · day_credit | numeric (computed) | 30 × years + 30 × fraction; denominator 365 default (OQ-001); day_credit floor 15 | FR-105 |
| l10n_sv.pay.indemnizacion | benefit_base · countable_base · cap_applied | monetary (computed) | benefit_base per 02 FR-021 max rule; countable_base = min(benefit_base, 4 × daily SMM row) | FR-105, FR-106 |
| l10n_sv.pay.indemnizacion | quantum · variant | monetary/select | indefinite = countable_base × day_credit; plazo = min(remaining_term_days × countable_base, indefinite quantum) | FR-105, FR-107 |
| l10n_sv.pay.indemnizacion | smm_cap_row | m2o (dated data) | the smm_2025.csv daily row via 02 FR-011 + FR-022 `indemnizacion_cap_4x` mapping (default comercio_y_servicios line 9); provenance recorded, value never hardcoded | FR-106 |

**Illness / chronic cases:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.illness.subsidy (new) | seniority_tier · tier_cap_days · days_used · days_netted | select/integer (computed) | tercera (1-5mo) 20 · segunda (5mo-1y) 40 · primera (≥1y) 60/anniversary-year; promotion nets days_used; clocks from service start, reset on re-contract | FR-111 |
| l10n_sv.pay.illness.subsidy | rate · base | %/monetary | 75% of básico; base per 02 FR-021 | FR-111 |
| l10n_sv.pay.illness.subsidy | grave_fault_finding · restitution_due | char/boolean | judicial finding reference required for denial; restitution flag on later findings | FR-112 |
| l10n_sv.pay.chronic.case (new) | diagnosis_date · treatment_end · stability_until · active | date/boolean | stability window = diagnosis → treatment end + 3 months; dismissal-block validation except recorded CT Art. 50 causes; no employer subsidy line while active (ISSS full subsidy, 308-B) | FR-113 |

**Maternity / lactancia / sepelio:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.maternity.leave (new) | licencia_start · birth_date · prenatal_weeks · postpartum_weeks | date/integer (computed) | 16 weeks total; 10 post-partum mandatory; default split 6+10 (prenatal configurable ≤6); late birth extends prenatal day-by-day, postpartum uncut | FR-114 |
| l10n_sv.pay.maternity.leave | prestacion_75 · isss_subsidy_deducted · net_employer_pay | monetary (computed) | 75% of básico × paid days (≤16 weeks); net = prestación − documented ISSS money subsidy (floor zero) | FR-116 |
| l10n_sv.pay.maternity.leave | continuation_case_id | m2o | still-unfit at end → Art. 312 suspension routing into the FR-111 engine | FR-117 |
| hr.leave.type (lactancia) | sv_pay_lactancia_break | boolean/config | up to 1h daily, 2 × 30-minute pauses, PAID work time; eligibility window = required config (OQ-003, no invented default) | FR-118 |
| hr.departure (death) | sv_pay_sepelio_pay | monetary (computed) | 60 × daily base, immediate; ¢250 floor never implemented (LB note) | FR-119 |

**Constancia + settlement + classification provenance:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| constancia document (report/mail.template) | mandatory fields: entry/exit dates, work class, last-period salary; optional: efficiency/behavior, termination causes | template | distinct from CT Art. 145 ISR constancia (taxation/04-owned) | FR-109 |
| hr.departure (settlement) | sv_pay_settlement_lines | one2many (by-id refs) | indemnización (FR-105/107) + 04's FR-051 vacation proration + 04's FR-058 aguinaldo proration + sepelio (FR-119) — ids only, no restated arithmetic | FR-110 |
| hr.payslip.line (this file's prestaciones) | matrix flags | stamped (from 01 FR-004) | prestación_social · IBC out (SIP 14.c) · ISR crosscheck_oq · F-14 feed via 08 | FR-120 |

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr / hr_payroll /
hr_holidays / hr_contract module family) — every FR maps `odoo`; no SaaS
rows are introduced because none of these FRs touch DTE
generation/transformation (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is required
beyond the dated-data regime below.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-101 | odoo | hr.contract | sv_pay_contract_type, sv_pay_labor_nature | Indefinite presumption as validation gate; classification routes FR-102..110 outcomes |
| FR-102 | odoo | hr.contract + hr.payslip.line | obra notice / in-lieu line | >15 days ⇒ 7-day notice or 7 × daily básico; completion = no-responsibility termination |
| FR-103 | odoo | hr.contract | titular_return_date / permanence | Return-termination without responsibility; >15-day post-return permanence reclassifies indefinite (day 16) |
| FR-104 | odoo | hr.contract | trial dates + prior-contract lookup | 30-day no-cause window; second trial for same labor within a year = blocking validation |
| FR-105 | odoo | l10n_sv.pay.indemnizacion | day_credit / quantum | 30d per year + prorated fractions; floor 15 days; base per 02 FR-021; denominator 365 default (OQ-001) |
| FR-106 | odoo | l10n_sv.pay.indemnizacion + l10n_sv.smm.tariff + l10n_sv.smm.sector.mapping | countable_base / smm_cap_row | Cap = 4 × daily SMM row via 02's `indemnizacion_cap_4x` mapping (default comercio_y_servicios, smm_2025.csv line 9 ⇒ $53.76; OQ-002/SOQ-18 kin); resolves 02 FR-023 forward reference; value never hardcoded |
| FR-107 | odoo | l10n_sv.pay.indemnizacion | plazo variant | min(remaining-term pay, indefinite equivalent) on the same capped base |
| FR-108 | odoo | hr.departure | sv_pay_despacho_presumed | Art. 55 entry-denial event; routes FR-105 + 04's FR-051/FR-058 (responsibility gate they consume) |
| FR-109 | odoo | report/mail.template (constancia) | content model | Mandatory: dates, work class, last-period salary; optional sections flagged; distinct from CT 145 (taxation/04) |
| FR-110 | odoo | hr.departure (settlement) | sv_pay_settlement_lines | Wires FR-105/107 + 04 FR-051 + 04 FR-058 + FR-119 by id; emits FR-109 constancia |
| FR-111 | odoo | l10n_sv.pay.illness.subsidy | tier caps 20/40/60 | 75% of básico (02 FR-021 base); promotion netting; anniversary clocks from hire, reset on re-contract (OQ-005) |
| FR-112 | odoo | l10n_sv.pay.illness.subsidy | grave-fault fields | Denial only with judicial finding reference; restitution flag |
| FR-113 | odoo | l10n_sv.pay.chronic.case | stability window | Dismissal block (except CT Art. 50 causes) + no salary discounts; ISSS full subsidy displaces the 75% line |
| FR-114 | odoo | l10n_sv.pay.maternity.leave | scheduling | 16w total, 10 post-partum mandatory, default 6+10; late birth extends prenatal only; supplement = OQ-004; Art. 310 simple-paper constancia |
| FR-115 | odoo | constraint (invariant) | tenure-gate rejection | Art. 311 VOID per sent. 105-2014 (D.O. 225 T.417 1-dic-2017) — no tenure condition may attach to Art. 309; tested invariant |
| FR-116 | odoo | l10n_sv.pay.maternity.leave | prestación + deduction | 75% paid in advance; ISSS money-subsidy netting (floor zero); never beyond 16 weeks |
| FR-117 | odoo | l10n_sv.pay.maternity.leave → suspension | continuation case | Still-unfit at end → Art. 312 suspension, FR-111 engine, job kept |
| FR-118 | odoo | hr.leave.type + work entries | lactancia breaks | 1h/d fractionable 2 × 30m, PAID work time; eligibility window = required config (OQ-003) |
| FR-119 | odoo | hr.departure (death) + payslip line | sepelio | 60 × daily base, immediate; ¢250 colon floor never implemented (LB note, 11_ OQ-2) |
| FR-120 | odoo | hr.payslip.line (stamped flags) | matrix consumption | prestación_social · IBC out (14.c) · crosscheck_oq (01 OQ-003 → 08) — flags from 01 FR-004, never restated |

Version-regime notes (D12): no dated values live in this file. The 4×SMM
cap re-seeds per SMM decree through `02_minimum-wage.md`'s sidecar rows
(selected by its FR-022 mapping; pre-2025-06-01 lookups flag its
OQ-001); the CT taxonomy/severance/benefit values are STATIC law
(SOQ-21 vintage watch, kin of file 01's OQ-001).

## 6. Acceptance Criteria

- **AC-001:** Given a contract stipulating a 12-month plazo whose
  recorded labor nature is permanent, then the Art. 25 gate REJECTS the
  plazo classification and the contract stores indefinite — a later
  unjustified dismissal routes to the Art. 58 indemnización; the same
  12-month plazo on a recorded eventual labor keeps the plazo type and
  routes to FR-107 instead (FR-101).
- **AC-002:** Given an interino whose titular returns on 1-March and
  who remains in the post through 17-March (>15 days), then the
  contract reclassifies to INDEFINITE with effect 17-March (day 16);
  had the interino exited by 16-March, the termination carries no
  responsibility and no indemnización (FR-103).
- **AC-003:** Given a worker terminated on trial-day 25 without cause,
  then no indemnización accrues; and given the same worker re-hired for
  the same labor 3 months later, then any second trial stipulation is
  BLOCKED by validation (no second trial within a year) (FR-104).
- **AC-004:** Given an obra contract with 40 days of work terminated
  without the 7-day notice, then the settlement pays SEVEN DAYS'
  salario básico in lieu (7 × US$16.00 = US$112.00) alongside earned
  balances; with notice given, no in-lieu line exists (FR-102).
- **AC-005:** Given an indefinite worker unjustified-dismissed after 3
  years and 2 months with daily benefit base US$100.00 and the default
  cap mapping (comercio_y_servicios, `smm_2025.csv` line 9 ⇒
  4 × US$13.440 = US$53.76), then countable_base = US$53.76 and the
  indemnización = (30 × 3 + 30 × 62/365) days × 53.76 = 95.10 days ×
  53.76 = US$5,112.58 [day credit 95.10 = 90 + 5.10 prorated fraction;
  denominator 365 per OQ-001] — the 4×SMM clamp having replaced the
  US$100 base (FR-105, FR-106).
- **AC-006:** Given a worker unjustified-dismissed after 4 months of
  service (fraction credit 30 × 4/12 = 10 days < 15), then the
  day_credit floor applies: 15 days × countable_base — never the bare
  10-day fraction (FR-105).
- **AC-007:** Given a valid plazo worker (eventual labor) with 10
  months remaining, unjustified-dismissed after 2 years of service at
  countable_base US$53.76, then the Art. 59 variant pays
  min(remaining-term pay ≈ 304 × 53.76 = US$16,343.04, indefinite
  equivalent 60 × 53.76 = US$3,225.60) = US$3,225.60 — the
  indefinite-equivalent cap governs (FR-107).
- **AC-008:** Given a worker whose entry is denied on 5-May (recorded
  despacho de hecho event), then the termination is presumed an
  unjustified dismissal: the Art. 58 indemnización computes AND the
  prorations of `04_statutory-benefits.md` SV-PAY-FR-051/SV-PAY-FR-058
  attach by id — this file supplying only the presumption and routing
  (FR-108, FR-110).
- **AC-009:** Given any termination, then the issued constancia carries
  the four mandatory fields (entry date, exit date, work class,
  last-period salary) and includes efficiency/behavior or termination
  causes ONLY when flagged; the ISR CT-Art.-145 retention constancia is
  a different document owned by taxation/04 and is never conflated
  (FR-109).
- **AC-010:** Given a PRIMERA-tier worker (≥1 year) with 75 illness
  days in the anniversary year at daily base US$16.00, then 60 days
  pay at 75% (60 × 12.00 = US$720.00) and the remaining 15 days accrue
  no employer subsidy; and given a worker promoted TERCERA→SEGUNDA
  having already used 12 days, then the new head-room is 40 − 12 = 28
  days (promotion netting) (FR-111).
- **AC-011:** Given a worker with a recorded chronic-incapacitating
  illness diagnosis and treatment ended 10-June, then dismissal
  attempts are blocked until 10-September (3 months post-treatment)
  except recorded CT Art. 50 causes, no salary-discount line may
  attach, and NO employer 75% subsidy line is emitted (ISSS covers the
  full daily subsidy) (FR-113).
- **AC-012:** Given an expected-birth schedule of 6 prenatal + 10
  post-partum weeks with the birth occurring ONE WEEK LATE, then the
  prenatal rest extends by the week while the 10 post-partum weeks
  remain uncut — and the employer's 75% payment stays capped at the
  16-week quantum; and given a worker hired ONE MONTH before the
  birth, then the full 16-week entitlement applies with NO tenure
  gate, and any configured six-month (or other) tenure condition is
  rejected by the Art. 311 VOID invariant (FR-114, FR-115, FR-116).
- **AC-013:** Given a maternity prestación of 16 weeks × 7 days × 75% ×
  US$16.00 = US$1,344.00 and a documented ISSS money subsidy of
  US$500.00, then the net employer payment = US$844.00 (deduction
  applied, floor zero); no payment line exists beyond the 16 weeks
  (FR-116).
- **AC-014:** Given a lactancia-eligible worker, then each day grants
  up to one hour of interruption remunerated as work time, taken as
  two 30-minute paid pauses; no payslip discount or unpaid-break line
  may attach (FR-118).
- **AC-015:** Given a termination caused by the worker's death with
  daily base US$16.00, then the settlement pays the immediate sepelio
  of 60 × 16.00 = US$960.00; the "doscientos cincuenta colones" print
  is never converted, floored or implemented in any way (FR-119).
- **AC-016:** Given payslip lines for indemnización (US$5,112.58),
  illness subsidy (US$720.00) and sepelio (US$960.00), then each
  carries the matrix flags of `01_salary-model.md` SV-PAY-FR-004:
  prestación_social · IBC excluded (SIP 14.c) · ISR crosscheck_oq —
  consumed by id, never restated (FR-120).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Indemnización fraction denominator: Art. 58 says "proporcionalmente por fracciones de año" without a denominator (365 calendar days? días laborables?); FR-105 defaults to 365 (kin of `04_statutory-benefits.md` OQ-004 for the aguinaldo proration). Consistent with the 30-days-per-year credit being calendar-based; no corpus norm pins it. | no | Takumi S4 (labor ruling watch) | open |
| OQ-002 | 4×SMM cap sector (SOQ-18 kin; `02_minimum-wage.md` OQ-002): CT Art. 58 caps the countable salary at 4× the "salario mínimo diario legal vigente" naming NO sector (EVID-207 doubt). FR-106 documents the comercio_y_servicios default (`smm_2025.csv` line 9 ⇒ US$53.76) via 02's `indemnizacion_cap_4x` mapping; alternatives (worker's own contract sector — `sv_pay_smm_sector`; highest/lowest sector row) pending MTP/labor guidance; rides 02 OQ-002's MH guidance hunt. | no | Takumi S4 + 02 consumers | open |
| OQ-003 | Lactancia eligibility window: Art. 312's verbatim grants the 1h/2×30m paid breaks without stating the child-age span (doctrinal "first year" is NOT in the 11_ evidence); FR-118 ships a REQUIRED config parameter and never invents a default. Acquisition watch for the reform stamp (8) context or a reglamento. | no | Takumi S4 (sources watch) | open |
| OQ-004 | Prenatal supplementary rest: Art. 309 delegates the prenatal supplement to a reglamento not in corpus; FR-114 implements the medical-certification-driven extension as the default mechanism with the 6+10 default split and late-birth rule (both corpus-express or residual). Reglamento acquisition optional (numbering ≥66). | no | Takumi S4 (sources watch) | open |
| OQ-005 | Illness-tier window cadence: Art. 307's PRIMERA tier grants "60 days/year" with tier dates from service start — anniversary-year windows (FR-111 default) vs calendar-year reading; also whether netted days carry across the SEGUNDA→PRIMERA promotion boundary the same way (EVID-209 states netting generally). Default: anniversary windows from hire, full netting. | no | Takumi S4 (labor ruling watch) | open |
