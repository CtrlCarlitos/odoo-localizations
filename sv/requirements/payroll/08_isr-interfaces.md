# SV — Payroll — ISR interfaces: retention-base input contract, F-14/F-910/F-11 value feeds, voluntary pension savings and the Quincena-25 pointer

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-18 |

## 1. Purpose

This file is the payroll↔ISR/reporting INTERFACES file: everything here
is a POINTER or a VALUE-FEED contract. It defines the payroll-side input
contract behind the ISR retention base — the payslip aggregates that
`taxation/04_isr-withholding.md` SV-TAX-FR-104 consumes (worker-side
social-security and pension *cotizaciones* (contributions) and
*remuneraciones no gravadas* (non-taxable remunerations) netted from the
gravadas base per D.E. 10-2025 Art. 1 d) — the base FORMULA is
taxation-owned and never restated here); the Ley ISR Art. 4 exemption
cross-check that resolves the `01_salary-model.md` matrix's crosscheck_oq
cells (OQ-002/OQ-003 of that file — the *indemnización* severance split
of Art. 4.3, the death-indemnity character of *sepelio*, the
remuneration character of the illness/maternity subsidies); the F-14
value-feed contract (SOQ-11): the per-employee-period record whose 7
social-security column values, *devengado* (accrued) G /
*bonificaciones* (bonuses) H split, aguinaldo J-K pair, Renta quartet
S-V stamps, country/haven flag and period W are PRODUCED by payroll and
consumed by `fiscal-reporting/06_f14-declaration.md`
(SV-FREP-FR-143..150 own the column model and validations — cited by id);
the F-910 annual feed: the 12-month consolidation inputs and the
retained-at-least-once classification input flag consumed by
`fiscal-reporting/07_codes-and-informs.md` SV-FREP-FR-179/180; the F-11
personal-deduction value feeds of form 65_ (the SS rows 713/714/716/
721/724, the AFP voluntary quota 717 with its stale-label warning, and
the *deducción fija* (fixed deduction) 722 pointer to taxation); the
voluntary pension savings regime of Ley Integral del Sistema de
Pensiones (D.L. 614) Art. 138 — the ≤10% IBC deductibility of employer
and employee *ahorro previsional voluntario* (voluntary pension
savings), tax-free transfers, the <5-year withdrawal *renta gravable*
reversal flag and the non-affiliated variant; and the Quincena-25
pointer — BLOCKED: the Ley Especial Quincena Veinticinco (D.L. 499,
D.O. 14-ene-2026) is not in the corpus, so this file carries only the
form-surface pointer to F-14 v17 casillas 417/418 (by FREP FR id) and
NO payroll income-treatment FRs.

It does **not** cover: the retention computation itself — base formula,
tables, June/December *recálculo* (recalculation), aguinaldo split,
CT 154-160 matrix (`taxation/04_isr-withholding.md` — SV-TAX-FR-102..
131, consumed by id); the F-14 column model, validations, declaration
projection and v17 vintage (`fiscal-reporting/06_f14-declaration.md`
— SV-FREP-FR-137..170, by id); the income-code catalog, F-910 inform
and F-11 layout ownership (`fiscal-reporting/07_codes-and-informs.md`
— the F-11 layout is taxation-side; this file only feeds values); the
SS contribution VALUES — rates, IBC, caps and regime routing
(`05_social-security-contributions.md` — SV-PAY-FR-063..085 compute the
lines whose declared values this file wires; its `ss_contributions.csv`
sidecar is the single dated SS parameter feed); the aguinaldo gross
prima and payment-window mechanics (`04_statutory-benefits.md`
SV-PAY-FR-053..062); the severance quantum, subsidy schedules and
sepelio computation (`07_contracts-termination.md` SV-PAY-FR-105..120);
the ISR retention constancia of CT Art. 145 (taxation-owned,
SV-TAX-FR-113); and the F-07 R/S rentas-matrix S-wiring (65_ OQ-1,
taxation/fiscal-reporting side — SV-FREP-FR-051/052/178 own it). Those
files consume this one for the interface stamps and value records
defined here.

## 2. Legal Basis

Authority order (binding, per master evidence index S4): pensions =
09_ (Ley Integral del Sistema de Pensiones, D.L. 614, effective
2022-12-29 — registry title is a misnomer per R24) for Arts. 26 and
138; ISR exemption semantics = 54_ (consolidated Ley ISR) with the S2
citation rule (cite 54_ as current authority; EVID-089 carries the
Art. 3-4 read); forms = 65_ (F-11 v18, page date 27-02-2025), 35_
(F-14 v16 manual, Oct-2025 print), 61_ (F-910 v9), 59_ (F-14 v17 form)
— the forms ARE the primary authority for their casilla surfaces; all
computation semantics consumed from the S2/S3 files by FR id (no
re-derivation). The SMM feed is `02_minimum-wage.md`'s sidecar
(consumed by id through file 04's aguinaldo interface).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley Integral del Sistema de Pensiones (D.L. 614), Art. 26: "Los rendimientos por inversiones de los Fondos de Pensiones, las cotizaciones obligatorias de los afiliados al Sistema, el excedente de libre disponibilidad ... así como los ingresos provenientes de los incentivos por permanencia serán considerados rentas no gravables para efectos de Impuesto sobre la Renta." | Pension-fund investment yields, the affiliates' mandatory cotizaciones, the free-availability surplus and permanence-incentive income are rentas no gravadas (non-taxable income) for ISR purposes | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 26 p.14 (EVID-199) |
| LB-002 | Ley Integral del Sistema de Pensiones, Art. 138: voluntary-savings fund rendimientos = rentas no gravadas; "los aportes que los empleadores y afiliados realicen a dichos Fondos en concepto de ahorro previsional voluntario, serán considerados como gastos deducibles de la renta imponible **hasta por el diez por ciento del ingreso base de cotización del afiliado**. Otras personas naturales no afiliadas ... podrán deducir hasta un diez por ciento de la renta imponible declarada en el ejercicio fiscal inmediato anterior."; transfers between own voluntary accounts (or employer→employee voluntary accounts) tax-free; "En caso que se realicen retiros ... antes de cumplir cinco años de haberse hecho el aporte respectivo, éstos serán considerados rentas gravables del ejercicio en el que el retiro se haga efectivo, siempre y cuando el afiliado se los haya deducido..." | Voluntary pension savings: employer and employee contributions deductible up to 10% of the affiliate's IBC; non-affiliated natural persons up to 10% of the renta imponible declared in the immediately prior ejercicio; voluntary-account transfers tax-free; withdrawals before five years from the contribution become rentas gravables of the withdrawal year IF they had been deducted | `sv/sources/09_Ley_Sistema_Pensiones.pdf` | Art. 138 p.57 (EVID-199) |
| LB-003 | Ley ISR, Art. 4 num. 3: "LAS INDEMNIZACIONES POR DESPIDO Y BONIFICACIONES POR RETIRO VOLUNTARIO, SIEMPRE QUE NO EXCEDAN DE UN SALARIO BÁSICO DE TREINTA DÍAS POR CADA AÑO DE SERVICIOS. PARA ESTOS EFECTOS, NINGÚN SALARIO PODRÁ SER SUPERIOR AL SALARIO PROMEDIO DE LO DEVENGADO EN LOS ÚLTIMOS DOCE MESES, SIEMPRE Y CUANDO ESTOS SALARIOS HAYAN SIDO SUJETOS DE RETENCIÓN"; the same numeral exempts death/incapacity indemnities and jubilaciones/pensiones/montepíos, while ordinary remunerations during sick leave remain taxable | Severance exemption: dismissal indemnizations and voluntary-retirement bonuses are not renta up to thirty days' salario básico per year of service, with no countable salary above the twelve-month average of salaries subject to retention; death/incapacity indemnities and pensions are exempt; sick-leave remunerations are taxable | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 4.3 pp.4-5 (EVID-089) |
| LB-004 | Formulario F-11 v18, p.2 DEDUCCIONES PERSONAS NATURALES: "ISSS (Salud) + 713 / Bienestar Magisterial + 714 / IPSFA + 716 / AFP Cuota Voluntaria (hasta límite legal, Inc. 2º de Art. 22 Ley SAP) + 717 / Cuota Patronal Pagada al I.S.S.S. por Trabajador Doméstico + 721 / Deducción Fija + 722 / CEFAFA + 724 / TOTAL ... casillas 711 a 722 = 725" | F-11 v18 personal-deduction block: the SS rows 713 ISSS (health), 714 Bienestar Magisterial, 716 IPSFA, 717 AFP voluntary quota "up to the legal limit", 721 patronal quota paid to the ISSS for a domestic worker, 722 fixed deduction, 724 CEFAFA; total 725 sums casillas 711-722 (711 medical and 712 schooling are NOT payroll values) | `sv/sources/65_F11_v18_form_visual.pdf` | p.2 deduction block (EVID-210) |
| LB-005 | Formulario F-11 v18, p.2 rentas no gravadas block: "Rentas No Gravadas AFP (Cuota legal y porción cuota voluntaria no deducible), ISSS e INPEP + 734" | F-11 casilla 734 carries as rentas no gravadas the AFP legal quota AND the non-deductible portion of the voluntary quota, plus ISSS and INPEP cotizaciones | `sv/sources/65_F11_v18_form_visual.pdf` | p.2 no-gravadas block, casilla 734 (EVID-210) |
| LB-006 | Formulario F-11 v18, p.2 pago-mínimo block: "DETERMINACIÓN DE LA BASE IMPONIBLE DEL ACTIVO NETO PARA CALCULAR EL IMPUESTO DEL PAGO MINIMO (Dec. Nº 762/2015)" casillas 630-646 and "Impuesto por Pago Mínimo (Casilla No 646 * 1%) 647" — PRINTED BUT DEAD (R21: sent. 18-2012/98-2014; D.L. 762-2014 void per sent. 96-2014); casilla 717's label cites "Ley SAP Art. 22 Inc. 2º" — a DEROGATED law (D.L. 927-1996 repealed by D.L. 614 per R24; live rule = D.L. 614 Art. 138) | F-11 print-vs-law defects: the pago-mínimo block 630-648 (and its liquidation consumers 314/647/648) is never fed; the 717 label's SAP citation is stale — never encode from the form label alone | `sv/sources/65_F11_v18_form_visual.pdf` | p.2 blocks (EVID-210; R21/R24) |
| LB-007 | Manual F-14 v16 §2, Anexo (Retenciones) payroll columns: G MONTO DEVENGADO / H BONIFICACIONES Y GRATIFICACIONES / I IMPUESTO RETENIDO / J AGUINALDO EXENTO / K AGUINALDO GRAVADO / L AFP / M ISSS / N INPEP / O IPSFA / P CEFAFA / Q BIENESTAR MAGISTERIAL / R ISSS IVM / W PERÍODO MMYYYY, with the plantilla note "Para código de ingreso 01, 60 y 80: incluir AFP y Cotizaciones Sociales si aplican, No Incluir Aguinaldos, Bonificaciones y Gratificaciones" — the VALUE-FEED surface this file produces into; the column MODEL and validations are OWNED by `fiscal-reporting/06_f14-declaration.md` (SV-FREP-FR-143..150) | F-14 v16 annex payroll zone: the G devengado / H bonuses split, I retained tax, J-K aguinaldo pair, the seven SS columns L-R and period W — payroll produces the values; the collection-side column semantics, caps mirror and export validations are file 06's by FR id | `sv/sources/35_F14_v16_manual.pdf` | §2 annex column table + plantilla note (EVID-180; via fiscal-reporting/06 LB-001/LB-002) |
| LB-008 | Formulario F-910 v9 §C, estructura de filas "CÓDIGO INGRESO / MONTO DEVENGADO / MONTO DEVENGADO ANUAL POR BONIFICACIONES Y GRATIFICACIONES / IMPUESTO RETENIDO / Aguinaldo (Aplica solo para código 01 y 60) Exento Gravado / ISSS ANUAL / AFP ANUAL / IPSFA ANUAL / CEFAFA ANUAL / INPEP ANUAL / BIENESTAR MAGISTERIAL ANUAL"; regla de nómina: "1. En el código 01, si se le retuvo en al menos un mes del ejercicio fiscal. 2. En el código 60, si no se le retuvo en todo el ejercicio fiscal" — the annual consolidation SURFACE; the inform mechanics are OWNED by `fiscal-reporting/07_codes-and-informs.md` (SV-FREP-FR-179..183) | F-910 v9 §C: per-contribuyente annual rows = income code + accrued + annual bonuses + retained tax + the aguinaldo pair (codes 01/60 only) + SIX annual SS columns (ISSS, AFP, IPSFA, CEFAFA, INPEP, BIENESTAR MAGISTERIAL — no ISSS-IVM annual column); payroll rule: code 01 if retained in at least one month, code 60 if never retained | `sv/sources/61_F910v9_informe_anual_retenciones.pdf` | §A-§C (EVID-187; via fiscal-reporting/07 LB-003) |
| LB-009 | Formulario F-14 v17: section "INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO" inserted after row 58 — row 61 *Ingresos No Gravados Pagados por el Agente de Retención Quincena 25*, casilla 417 (número de sujetos) and casilla 418 (monto) — the ONLY known surface of the Ley Especial Quincena Veinticinco (D.L. 499, D.O. 14-ene-2026 vol. 31679 — NOT in corpus, P10 BLOCKED; acquisition queued as source 66) | F-14 v17 casillas 417/418: subject count and amount of Quincena-25 no-gravado payments — the form-level pointer this file cites by FREP FR id; no payroll income-treatment FR exists until the law is acquired | `sv/sources/59_F14_v17_form_visual.pdf` | v17 vs v16 diff, row 61 / casillas 417-418 (EVID-184) |
| LB-010 | D.E. 10-2025, Art. 1 d) — interface anchor only: retention base considers only remuneraciones gravadas, determined by deducting from TOTAL period remunerations the remuneraciones no gravadas and the cotizaciones laborales a la Seguridad Social; cotizaciones previsionales to the AFPs and public pension institutes are comprised within the no-gravadas concept — the base FORMULA is OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-104 and consumed by reference; this file states only the payroll-side input contract | Retention-base interface: worker SS/pension cotizaciones excluded from the gravadas base — payroll supplies the stamped aggregates; the computation is taxation's by FR id, never restated | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 d) p.3 (EVID-156; via taxation/04 LB-008 / SV-TAX-FR-104) |
| LB-011 | Ley ISR, Art. 4 num. 16 + D.E. 10-2025, Arts. 1 f)/g) — interface anchors only: the aguinaldo exento/gravado split, retention vintages and recálculo aggregation are OWNED by `taxation/04_isr-withholding.md` (SV-TAX-FR-120 split; SV-TAX-FR-116 aggregation; SV-TAX-FR-110/111 recálculo) with the gross-prima supply OWNED by `04_statutory-benefits.md` (SV-PAY-FR-060/061/062) — consumed by reference into this file's F-14 J-K feed | Aguinaldo interface by reference: the split computation is taxation's and the gross prima file 04's; this file wires only the J-K declared values | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` + `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 4.16 p.7 (EVID-165); Arts. 1 f)/g) (EVID-158/159; via taxation/04 and payroll/04 by FR id) |

Dead text and print-vs-law rulings (LB notes, tested where an FR says
so): the F-11 pago-mínimo block casillas 630-648 and its liquidation
consumers (314/647/648) are PRINTED BUT DEAD (R21 — sent. 18-2012,
D.O. 216 T.401 19-XI-2013; sent. 98-2014; D.L. 762-2014 void per sent.
96-2014 — LB-006; never fed, mirroring the F-14 pago-mínimo discipline
of SV-FREP-FR-163). Casilla 717's printed citation "Inc. 2º de Art. 22
Ley SAP" is a STALE LABEL: D.L. 927-1996 (Ley SAP) is derogated by
D.L. 614 (R24) — the live rule is Art. 138's 10%-of-IBC limit (LB-002;
LB-006; FR-131 encodes the live rule, never the label). Harmonization
ruling (resolves the EVID-199 doubt): the Ley ISR Art. 4 exemption
list (EVID-089) does NOT expressly name SS cotizaciones or pension-fund
rendimientos — D.L. 614 Art. 26 is the operative declaration making
them rentas no gravadas (LB-001), consistent with, not contrary to, the
Ley ISR; both layers classify them no-gravadas and no conflict exists.

Version regime (D12): no dated VALUES are owned by this file — the SS
cap values re-date through `05_social-security-contributions.md`'s
`ss_contributions.csv` (its SV-PAY-FR-081, re-dated per instrument
acquisition per its SV-PAY-FR-084); the SMM feed belongs to
`02_minimum-wage.md`; the form vintages consumed (F-11 v18 page date
27-02-2025 — 65_ OQ-2 watch; F-910 v9; F-14 v16 annex + v17 form gate
per SV-FREP-FR-165) are owned by the fiscal-reporting files. The
Quincena-25 surface is version-gated from period 2026-06 by
SV-FREP-FR-165 (cited, never restated).

## 3. Functional Requirements

### 3.1 ISR retention-base input contract (the payroll side of SV-TAX-FR-104)

- **SV-PAY-FR-121:** The system shall expose, for every employee and
  pay period, the three stamped aggregates that
  `taxation/04_isr-withholding.md` SV-TAX-FR-104 consumes as retention
  inputs — (a) TOTAL period remunerations: the sum of payslip lines
  classified by the canonical matrix of `01_salary-model.md`
  SV-PAY-FR-004 (G/H column families plus the aguinaldo line); (b)
  *remuneraciones no gravadas*: the lines stamped no_gravada by the
  matrix (including FR-123/FR-124 exempt components and the Art. 26
  items of FR-122 where they are remunerations) — the netting of the
  previsional cotizaciones happens through the no-gravadas concept per
  LB-010; and (c) WORKER-side cotizaciones of the period: the ISSS
  laboral line and the AFP/instituto previsional line computed by
  `05_social-security-contributions.md` (its SV-PAY-FR-066/072 and the
  instituto rows, with the clamps of its SV-PAY-FR-070/082) —
  EMPLOYER-side legs shall never enter any input (the base arithmetic,
  ordering and table application are SV-TAX-FR-104/109 territory,
  consumed by id). (LB-010; LB-001; EVID-156/199; cross-ref
  SV-TAX-FR-104, SV-PAY-FR-004, SV-PAY-FR-066/070/072/082)
- **SV-PAY-FR-122:** The system shall classify the worker's mandatory
  SS/pension cotizaciones, the pension funds' investment rendimientos,
  the free-availability surplus and the permanence-incentive income as
  *rentas no gravadas* per D.L. 614 Art. 26 — stamping them
  no-gravadas wherever they surface as worker income — and shall
  produce the annual no-gravadas value for F-11 casilla 734 as the sum
  of (i) the worker's legal AFP/ISSS/INPEP cotizaciones and (ii) the
  NON-deductible portion of the voluntary quota per FR-131 (the
  casilla label's own composition — LB-005); the harmonized reading
  (no express Ley ISR Art. 4 numeral needed; Art. 26 is the operative
  declaration) is recorded in §2 and re-derived nowhere.
  (LB-001; LB-005; EVID-199/210)

### 3.2 Ley ISR Art. 4 cross-check — resolving the matrix crosscheck_oq cells

- **SV-PAY-FR-123:** The system shall split the unjustified-dismissal
  *indemnización* (and any voluntary-retirement bonus) into its
  exempt/gravable components per Ley ISR Art. 4.3: the EXEMPT portion =
  min(settlement quantum computed by `07_contracts-termination.md`
  SV-PAY-FR-105/107, 30 days' salario básico × years of service, with
  NO countable salary above the worker's twelve-month average of
  salaries SUBJECT TO RETENTION) and the EXCESS = gravada, routed to
  the ISR layer as an extraordinary remuneration through
  `taxation/04_isr-withholding.md` SV-TAX-FR-116 (aggregation mechanics
  owned there); the split resolves the indemnización crosscheck_oq cell
  of the `01_salary-model.md` SV-PAY-FR-004 matrix (its OQ-003) — the
  no_gravada/gravada stamps replace the flag from the settlement date.
  (LB-003; EVID-089; cross-ref SV-PAY-FR-105/107, SV-TAX-FR-116)
- **SV-PAY-FR-124:** The system shall classify the *sepelio* (burial)
  help of `07_contracts-termination.md` SV-PAY-FR-119 as a death
  indemnity EXEMPT per Ley ISR Art. 4.3 — no_gravada in FULL, no
  split, no retention line — resolving that matrix crosscheck_oq cell
  (its OQ-003). (LB-003; EVID-089; cross-ref SV-PAY-FR-119)
- **SV-PAY-FR-125:** The system shall classify the illness and
  maternity subsidy prestaciones of `07_contracts-termination.md`
  SV-PAY-FR-111/SV-PAY-FR-116 as GRAVADA remunerations — they replace
  ordinary remuneration during leave (the Art. 4.3 exemption covers
  death/inapacity INDEMNITIES, not leave-replacing remuneration; sick
  leave ordinary remunerations are taxable per EVID-089, and D.L. 614
  Art. 14 itself cotizes the illness/accident/maternity subsidy as IBC
  via `05_social-security-contributions.md` SV-PAY-FR-079) — and shall
  CONFIRM the matrix's gravada stamps for occasional
  bonuses/gratuities (no exclusion exists in the Ley ISR Art. 3-4
  lists, closing `01_salary-model.md` OQ-002) and for vacation pay
  (per its EVID-204 mapping note); these resolutions close the
  crosscheck_oq family (its OQ-003) — the flags are replaced by
  definitive stamps, never left pending. (LB-003; LB-001; EVID-089/
  197; cross-ref SV-PAY-FR-111/116, SV-PAY-FR-079, SV-PAY-FR-004)

### 3.3 F-14 value-feed contract (SOQ-11 — payroll owns the values, file 06 mirrors)

- **SV-PAY-FR-126:** The system shall produce, for every employee and
  monthly period, the F-14 annex VALUE record as a single payroll-owned
  feed consumed by `fiscal-reporting/06_f14-declaration.md`: G
  (devengado) and H (bonificaciones y gratificaciones) split per the
  `01_salary-model.md` SV-PAY-FR-004 column families (G includes the
  AFP/SS cotizaciones and excludes aguinaldos/bonificaciones — the
  plantilla note, LB-007); the aguinaldo pair J (exento) / K (gravado)
  carrying the split computed by `taxation/04_isr-withholding.md`
  SV-TAX-FR-120 over the gross prima supplied by
  `04_statutory-benefits.md` SV-PAY-FR-060/061 (split owned there,
  wired here); I (impuesto retenido) sourced EXCLUSIVELY from the
  retention postings of SV-TAX-FR-102 (provenance pointer, never
  recomputed); the SEVEN social-security column values L AFP · M ISSS ·
  N INPEP · O IPSFA · P CEFAFA · Q BIENESTAR MAGISTERIAL · R ISSS IVM —
  produced from the `05_social-security-contributions.md` lines with
  the clamps of its SV-PAY-FR-070/082/083 over its sidecar values (its
  SV-PAY-FR-081) — and W (período) as MMYYYY; the column MODEL, legal
  caps mirror and export validations are OWNED by the consumer
  (SV-FREP-FR-143/144/145/147, validated per SV-FREP-FR-148/149/150)
  and any cap mismatch is flagged to this file's provenance chain, not
  adjusted here. (LB-007; LB-011; EVID-180; cross-ref SV-FREP-FR-143,
  SV-FREP-FR-144, SV-FREP-FR-145, SV-FREP-FR-147, SV-FREP-FR-148,
  SV-FREP-FR-149, SV-FREP-FR-150, SV-TAX-FR-102/120, SV-PAY-FR-060/
  061, SV-PAY-FR-081/082/083/084)
- **SV-PAY-FR-127:** The system shall stamp the Renta quartet
  S (tipo de operación) / T (clasificación) / U (sector) / V (tipo de
  costo/gasto) on every F-14 value record from the CANONICAL code
  lists and Febrero-2024 period gate OWNED by
  `fiscal-reporting/03_f07-annexes-purchases.md` SV-FREP-FR-079..085
  (codes 8/9 included; "0" before the gate) and mirrored by
  `fiscal-reporting/06_f14-declaration.md` SV-FREP-FR-146 — no code
  list is restated here; the stamped values for salaried payroll rows
  ship as CONFIGURATION with a documented default set (tipo de
  operación 1 gravada for retained rows; clasificación/sector from the
  employer's activity; tipo de costo/gasto 7 mano de obra) carrying
  OQ-001 (label-inference: the lists are printed for the purchases
  annex, not the payroll rows). (LB-007; EVID-180; cross-ref
  SV-FREP-FR-079..085, SV-FREP-FR-146)
- **SV-PAY-FR-128:** The system shall stamp on every F-14 value record
  the employee's country classification (non-domiciliados) from the MH
  country-code table loaded per `fiscal-reporting/06_f14-declaration.md`
  SV-FREP-FR-139, including its *paraíso fiscal* (tax-haven) flag: a
  haven-flagged record routes to the 25% exactness validation
  SV-FREP-FR-141 and the haven retention rule
  `taxation/04_isr-withholding.md` SV-TAX-FR-127 — this file supplies
  ONLY the country code and flag (partner-master data), never the
  rate or the check. (LB-007; EVID-180; cross-ref SV-FREP-FR-139,
  SV-FREP-FR-141, SV-TAX-FR-127)

### 3.4 F-910 annual feed (fiscal-reporting/07 by id)

- **SV-PAY-FR-129:** The system shall produce, for every employee and
  *ejercicio* (fiscal year), the annual consolidation INPUTS consumed
  by `fiscal-reporting/07_codes-and-informs.md`: the 12-month sums per
  income code over the FR-126 records — devengado, bonificaciones y
  gratificaciones, impuesto retenido, the aguinaldo exento/gravado pair
  (codes 01/60 only) and the SIX annual SS columns (ISSS, AFP, IPSFA,
  CEFAFA, INPEP, BIENESTAR MAGISTERIAL — the F-910 prints NO annual
  ISSS-IVM column, so the R value is consolidated nowhere on that
  surface) — plus the retained_at_least_once input FLAG computed from
  the twelve monthly records (≥1 month with a retention ⇒ flag true);
  the 01-vs-60 classification RULE (flag true → code 01; false → 60)
  and the inform builder are OWNED by SV-FREP-FR-179/180 (the monthly
  threshold selection behind them is SV-TAX-FR-106), and the
  FOLIO-modifica full-recompute parity is SV-FREP-FR-182 — consumed by
  id. (LB-008; EVID-187; cross-ref SV-FREP-FR-179, SV-FREP-FR-180,
  SV-FREP-FR-182, SV-TAX-FR-106)

### 3.5 F-11 personal-deduction value feeds (65_/EVID-210)

- **SV-PAY-FR-130:** The system shall produce, for every worker and
  ejercicio, the F-11 SS deduction VALUES: casilla 713 (ISSS Salud),
  714 (Bienestar Magisterial), 716 (IPSFA) and 724 (CEFAFA) = the
  annual worker-side cotizaciones per institution (sums of the FR-121
  inputs over the ejercicio), and casilla 721 = the PATRONAL ISSS
  quota paid by a natural-person employer for a domestic worker (the
  employer leg of `05_social-security-contributions.md` in the
  domestic-worker case); values ONLY — the deduction caps and the F-11
  layout/liquidation are taxation-owned (the Art. 33 regime of
  SV-TAX-FR-105; rows 711/712/715 are not payroll values and are never
  touched here). (LB-004; EVID-210; cross-ref SV-TAX-FR-105)
- **SV-PAY-FR-131:** The system shall produce the F-11 casilla 717 AFP
  *cuota voluntaria* (voluntary quota) value as the annual sum of
  DEDUCTIBLE voluntary-savings contributions capped at 10% of the
  affiliate's IBC per FR-133 — and shall surface the NON-deductible
  excess (contributions above the cap, when retained in the account)
  into the FR-122 casilla-734 no-gravadas value instead (LB-005: legal
  quota + non-deductible voluntary portion), so no amount is ever both
  deducted and declared no-gravada; STALE-LABEL GUARD: the v18 form
  label cites "Inc. 2º de Art. 22 Ley SAP" — a DEROGATED instrument
  (R24) — and shall never be encoded; the live limit is D.L. 614
  Art. 138's 10%-of-IBC (LB-002), tested against the cap computation.
  (LB-004; LB-005; LB-006; LB-002; EVID-210/199)
- **SV-PAY-FR-132:** The system shall treat F-11 casilla 722
  (*deducción fija*) as a POINTER ONLY: the US$1,600.00 fixed deduction
  of Ley ISR Art. 29.7 is OWNED by `taxation/04_isr-withholding.md`
  SV-TAX-FR-103 (with its annual-renta ≤ US$9,100.00 mode selection of
  SV-TAX-FR-106) — payroll supplies no 722 value beyond the FR-121
  aggregates and the FR-130/131 deduction rows; and it shall NEVER
  feed the printed-but-dead pago-mínimo block casillas 630-648 (R21 —
  LB-006; a dead-cell guard mirroring SV-FREP-FR-163: no payroll or
  ISR value may enter those casillas under any configuration).
  (LB-004; LB-006; EVID-210; cross-ref SV-TAX-FR-103, SV-FREP-FR-163)

### 3.6 Voluntary pension savings — D.L. 614 Art. 138

- **SV-PAY-FR-133:** The system shall maintain a per-contribution
  voluntary-savings ledger (employer and employee contributions to the
  voluntary pension funds) and shall compute the deductibility CAP for
  each affiliate and ejercicio as 10% of the affiliate's IBC (the IBC
  computed by `05_social-security-contributions.md` SV-PAY-FR-075) —
  contributions up to the cap carry the deductible stamp feeding
  FR-131's casilla 717 (worker side) and the employer's
  cost-deductibility provenance (the *gasto deducible* character is
  Art. 138's own; nothing here re-derives the taxation deduction
  rules); amounts and dates per contribution are retained for the
  FR-135 clock. (LB-002; EVID-199; cross-ref SV-PAY-FR-075)
- **SV-PAY-FR-134:** The system shall record transfers between the
  affiliate's own voluntary accounts (and employer→employee voluntary
  account transfers) with a TAX-FREE stamp — no renta event, no
  reversal, no deduction undo — per Art. 138; the stamp is a ledger
  record only (no computation attaches). (LB-002; EVID-199)
- **SV-PAY-FR-135:** The system shall flag, for every withdrawal of a
  DEDUCTED voluntary contribution made BEFORE the fifth anniversary of
  its contribution date, the *renta gravable* (taxable income)
  REVERSAL: the withdrawn amount becomes rentas gravables of the
  ejercicio in which the withdrawal takes effect — emitted as a
  reversal flag + amount on the worker's annual record for the ISR
  layer (the incorporation into the annual liquidation is
  taxation-owned; non-deducted contributions never reverse); the
  ledger keeps the per-contribution five-year clock from the FR-133
  dates. (LB-002; EVID-199)
- **SV-PAY-FR-136:** The system shall support the NON-affiliated
  natural-person variant as ADJACENT worker-side configuration (no
  employer computation attached, kin of file 05's pensioner rows): the
  deductible cap = 10% of the *renta imponible declarada en el
  ejercicio fiscal inmediato anterior* (the renta imponible declared in
  the immediately prior ejercicio), read from the worker's own prior
  annual declaration input — provenance recorded, no default invented
  (OQ-003). (LB-002; EVID-199)

### 3.7 Quincena Veinticinco pointer (P10 — BLOCKED)

- **SV-PAY-FR-137:** The system shall implement NO payroll
  income-treatment rules for the Ley Especial Quincena Veinticinco
  (D.L. 499, D.O. 14-ene-2026, volume Id 31679 — NOT in the corpus;
  acquisition queued as source 66, OQ-002): the ONLY known surface is
  the F-14 v17 section "INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA
  VEINTICINCO" casillas 417 (número de sujetos) / 418 (monto) —
  consumed by reference from `fiscal-reporting/06_f14-declaration.md`
  SV-FREP-FR-165 (layout gate from period 2026-06) and SV-FREP-FR-166
  (the reporting-only projection with its FR-167 annex-format working
  assumption) — and until the law is acquired NO quincena-25 earning
  category, payslip line, F-14 value-record field or ledger
  classification shall exist (absent law ⇒ absent rows everywhere; the
  payment mechanics stay with that future acquisition, never invented
  here). (LB-009; EVID-184; cross-ref SV-FREP-FR-165, SV-FREP-FR-166,
  SV-FREP-FR-167)

## 4. Data Model

Layer semantics: payroll is Odoo-native — all entities below live in
the client (wave default `odoo`; see §5). No sidecar lives next to this
file: every dated value consumed (SS caps, SMM rows) belongs to files
05/02 and enters by FR id; the form vintages are fiscal-reporting
property.

**Retention-input and F-14 value-feed record (per employee-period):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip | sv_pay_total_remunerations · sv_pay_no_gravada_remunerations · sv_pay_worker_cotizaciones | monetary (computed) | the three SV-TAX-FR-104 input aggregates: total matrix remunerations / no-gravada lines (incl. FR-123/124 exempt components) / worker ISSS + previsional lines; employer legs never enter | FR-121 |
| l10n_sv.pay.f14.feed (new) | employee_id · period_mmyyyy · income_code_family | m2o/char(6)/char | one record per employee-period; code family per `fiscal-reporting/07` catalog semantics | FR-126 |
| l10n_sv.pay.f14.feed | g_devengado · h_bonificaciones · i_retained_source · j_aguinaldo_exento · k_aguinaldo_gravado | monetary(2dp)/pointer | G/H per 01 FR-004 families; I = provenance pointer to the SV-TAX-FR-102 posting, never a recomputation; J/K from SV-TAX-FR-120 via 04's FR-060/061 | FR-126 |
| l10n_sv.pay.f14.feed | ss_afp · ss_isss · ss_inpep · ss_ipsfa · ss_cefafa · ss_bienestar_mag · ss_isss_ivm | monetary(2dp) | the SEVEN column values from 05's lines (clamps FR-070/082/083; sidecar FR-081; provenance FR-084) | FR-126 |
| l10n_sv.pay.f14.feed | s_tipo_operacion · t_clasificacion · u_sector · v_tipo_costo_gasto | char(1) | stamped from the SV-FREP-FR-079..085 canonical lists; "0" pre-Feb-2024; salaried defaults = configuration (OQ-001) | FR-127 |
| l10n_sv.pay.f14.feed | country_code_id · haven_flag | m2o/boolean | from the MH country table (SV-FREP-FR-139); routes to SV-FREP-FR-141/SV-TAX-FR-127 | FR-128 |
| l10n_sv.pay.f910.feed (new) | employee_id · ejercicio · devengado_anual · bonificaciones_anual · retenido_anual · aguinaldo_exento_anual · aguinaldo_gravado_anual · ss_annual[6] · retained_at_least_once | monetary(2dp)/boolean | 12-month sums over f14.feed; SIX annual SS columns (no ISSS-IVM); the 01-vs-60 input flag (rule owned by SV-FREP-FR-180) | FR-129 |

**Annual F-11 deduction values (per worker-ejercicio):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.f11.deduction (new) | casilla_713 · casilla_714 · casilla_716 · casilla_724 | monetary(2dp) | annual worker-side cotizaciones per institution (ISSS salud / Bien. Mag. / IPSFA / CEFAFA) | FR-130 |
| l10n_sv.pay.f11.deduction | casilla_721 | monetary(2dp) | patronal ISSS quota paid for a domestic worker (natural-person employer) | FR-130 |
| l10n_sv.pay.f11.deduction | casilla_717 · casilla_734_components | monetary(2dp) | deductible voluntary quota (≤ FR-133 cap; live rule Art. 138, never the SAP label) + non-deductible excess into the 734 no-gravadas value | FR-131, FR-122 |
| l10n_sv.pay.f11.deduction | casilla_722 | pointer (char) | fixed pointer `taxation/04 SV-TAX-FR-103` — no payroll value; dead cells 630-648 carry no field at all (R21 guard) | FR-132 |

**Voluntary pension savings ledger:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.voluntary.savings (new) | affiliate_id · contributor | m2o/select | worker · employer (deductibility character per Art. 138) | FR-133 |
| l10n_sv.pay.voluntary.savings | contribution_date · amount · deducted · cap_provenance | date/monetary/boolean | per-contribution record; deductible ≤ 10% × IBC (IBC per 05 FR-075); dates retained for the 5-year clock | FR-133 |
| l10n_sv.pay.voluntary.savings | transfer_tax_free | boolean | own-account and employer→employee transfers: ledger stamp, no computation | FR-134 |
| l10n_sv.pay.voluntary.withdrawal (new) | contribution_id · effective_date · before_5y · reversal_amount | m2o/date/boolean/monetary | before-5y + deducted ⇒ renta gravable reversal flag/amount of the effective year (annual-ISR consumption) | FR-135 |
| config (worker-side) | sv_pay_voluntary_nonaffiliated_cap | monetary (input) | non-affiliated variant: 10% × prior-ejercicio declared renta imponible; worker-supplied input, provenance recorded (OQ-003) | FR-136 |

**Matrix resolution stamps (on payslip lines):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip.line | sv_pay_isr_gravada_input (resolved) | select | the 01 FR-004 cell values now DEFINITIVE: indemnización = split_exento_gravado (FR-123 Art. 4.3 split) · sepelio = no_gravada (FR-124) · illness/maternity subsidies = gravada (FR-125) — crosscheck_oq eliminated | FR-123, FR-124, FR-125 |

## 5. Odoo Mapping

Layer semantics for this wave: payroll is Odoo-native (hr / hr_payroll
module family) — every FR maps `odoo`; no SaaS rows are introduced
because none of these FRs touch DTE generation/transformation (the only
architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is
required beyond the dated-data regime noted in §2.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-121 | odoo | hr.payslip | sv_pay retention-input aggregates | THE input contract of SV-TAX-FR-104 (by id): total − no-gravadas − worker cotizaciones; employer legs never netted |
| FR-122 | odoo | hr.payslip.line + l10n_sv.pay.f11.deduction | no-gravada stamps + 734 value | Art. 26 items no-gravadas; 734 = legal quotas + non-deductible voluntary portion |
| FR-123 | odoo | hr.payslip.line + hr.departure (settlement) | indemnización split stamps | Art. 4.3: exempt ≤ 30d básico × years, 12-month retained-salary average cap; excess → SV-TAX-FR-116; closes 01 OQ-003 (indemnización) |
| FR-124 | odoo | hr.payslip.line (sepelio) | no_gravada stamp | Death indemnity exempt (Art. 4.3); closes 01 OQ-003 (sepelio) |
| FR-125 | odoo | hr.payslip.line (subsidies) | gravada stamps | Illness/maternity = leave-replacing remuneration (EVID-089; cotizable per SIP Art. 14 via 05 FR-079); closes 01 OQ-002/OQ-003 |
| FR-126 | odoo | l10n_sv.pay.f14.feed | G/H/I/J-K + 7 SS columns + W | Values payroll-owned (SOQ-11); column model/validations = SV-FREP-FR-143..150 by id; caps provenance chain = 05 FR-084 |
| FR-127 | odoo | l10n_sv.pay.f14.feed | S/T/U/V stamps | Canonical lists SV-FREP-FR-079..085 by id; Feb-2024 gate; salaried defaults = config (OQ-001) |
| FR-128 | odoo | l10n_sv.pay.f14.feed + res.partner | country + haven flag | Flag-only feed → SV-FREP-FR-141 / SV-TAX-FR-127 (rate never here) |
| FR-129 | odoo | l10n_sv.pay.f910.feed | annual sums + retained flag | SIX annual SS columns (no ISSS-IVM); 01-vs-60 rule = SV-FREP-FR-180 by id |
| FR-130 | odoo | l10n_sv.pay.f11.deduction | 713/714/716/721/724 | Annual per-institution worker cotizaciones + domestic-worker patronal ISSS; deduction regime = SV-TAX-FR-105 |
| FR-131 | odoo | l10n_sv.pay.f11.deduction | 717 + 734 excess | Live rule Art. 138 ≤10% IBC; SAP label never encoded (R24); excess → 734, never double-counted |
| FR-132 | odoo | pointer + dead-cell guard | 722 → SV-TAX-FR-103 | No payroll value; pago-mínimo 630-648 never fed (R21; kin SV-FREP-FR-163) |
| FR-133 | odoo | l10n_sv.pay.voluntary.savings | ledger + 10% IBC cap | Cap over 05 FR-075 IBC; feeds FR-131 and employer deductibility provenance |
| FR-134 | odoo | l10n_sv.pay.voluntary.savings | transfer_tax_free | Ledger stamp only |
| FR-135 | odoo | l10n_sv.pay.voluntary.withdrawal | before_5y reversal flag | Withdrawal year renta gravable IF deducted; per-contribution clock |
| FR-136 | odoo | config (worker-side) | non-affiliated cap | 10% × prior-year declared renta; adjacent config, input provenance (OQ-003) |
| FR-137 | odoo | none (absence invariant) | no quincena-25 surface | D.L. 499 NOT in corpus (source 66 queued); only pointers SV-FREP-FR-165/166 by id; absent law ⇒ absent rows |

Version-regime notes (D12): no dated values live in this file. The SS
cap values consumed re-seed through `ss_contributions.csv`
(`05_social-security-contributions.md` SV-PAY-FR-081/084); the F-14
v16/v17 and F-11 v18/F-910 v9 vintages are owned by the
fiscal-reporting files (65_ OQ-2 watch for an F-11 v19 — this file's
OQ-003 kin); the Quincena-25 gate date (2026-06) is cited from
SV-FREP-FR-165 and never restated as local configuration.

## 6. Acceptance Criteria

- **AC-001:** Given a monthly payslip with devengado-family lines
  US$1,000.00, worker ISSS US$30.00 (clamped, 05 FR-070) and worker
  AFP US$72.50 on IBC US$1,000.00, then the retention-input aggregates
  expose total US$1,000.00 / no-gravadas US$0.00 / worker cotizaciones
  US$102.50, and the retention base computed by SV-TAX-FR-104 over
  them = 1,000.00 − 102.50 = US$897.50 — this file supplies the
  aggregates only; the employer's 8.75% + 7.5% legs never appear in any
  input (FR-121).
- **AC-002:** Given an indemnización quantum of US$3,225.60 (the
  `07_contracts-termination.md` AC-007 worker) after 2 years of
  service with a twelve-month average retained salary of US$14.00/day
  (US$4,480.00/year retained ≈ cap), then the Art. 4.3 exempt cap =
  30 days × 2 years × min(básico, US$14.00) and the split stamps the
  exempt portion no_gravada with the excess (if any) gravada and routed
  to SV-TAX-FR-116 — the matrix crosscheck_oq flag is gone (FR-123).
- **AC-003:** Given a death-termination settlement paying sepelio of
  US$960.00 (07 AC-015), then the sepelio line stamps no_gravada in
  full — no retention line, no split, no F-14 gravadas contribution
  (FR-124).
- **AC-004:** Given an illness-subsidy line of US$720.00 and a
  maternity prestación line of US$844.00 (07 AC-010/013 values), then
  both stamp GRAVADA (leave-replacing remuneration; cotizable as IBC
  per 05 FR-079) — and the occasional-gratuity and vacation rows of the
  01 matrix keep gravada with the crosscheck flags cleared (FR-125).
- **AC-005:** Given the FR-121 worker's f14.feed record, then it
  carries G = US$1,102.50-equivalent devengado split per the matrix
  families (AFP/SS cotizaciones INCLUDED in G per the plantilla note),
  H for any bonus lines, the seven SS columns L=72.50 · M=30.00 ·
  N..R=0.00 (regime isss_sip) and W=MMYYYY — consumed by
  SV-FREP-FR-143/145 and passing the SV-FREP-FR-150 cap validation
  unchanged (FR-126).
- **AC-006:** Given an SIP worker with IBC US$8,000.00 whose AFP
  worker share 7.25% = US$580.00, then column L carries the FR-082
  clamp US$472.93 (the f14.feed value already clamped payroll-side;
  the F-14 mirror validates, never adjusts) (FR-126).
- **AC-007:** Given a Febrero-2024-or-later payroll row, then its
  S/T/U/V stamps come from the SV-FREP-FR-079..085 canonical lists
  (documented default 1 gravada / employer clasificación+sector /
  7 mano de obra, OQ-001); and given an Enero-2024 row, then all four
  read "0" (pre-gate) (FR-127).
- **AC-008:** Given a non-domiciliado employee whose country code
  carries the haven flag (SV-FREP-FR-139 table), then the f14.feed
  record surfaces country + haven_flag and the row routes to the
  SV-FREP-FR-141 exactness check with SV-TAX-FR-127's 25% — no rate is
  ever computed payroll-side (FR-128).
- **AC-009:** Given an employee retained in March but never otherwise
  (11 months with zero retention), then the f910.feed
  retained_at_least_once = true ⇒ the SV-FREP-FR-180 rule reports the
  whole year under code 01; given a never-retained employee, the flag
  is false ⇒ code 60 — and in both cases the annual SS block carries
  exactly SIX columns with no ISSS-IVM value (FR-129).
- **AC-010:** Given a worker with annual worker cotizaciones ISSS
  US$360.00, AFP US$870.00 and instituto IPSFA US$500.00, then the
  f11.deduction record carries 713=360.00, 716=500.00, 717 per FR-133,
  and 714/724 = 0.00 (regime) — rows 711/712/715 carry no payroll
  value ever (FR-130).
- **AC-011:** Given voluntary pension contributions of US$150.00 in a
  year whose 10% IBC cap = US$100.00 (IBC US$1,000.00), then casilla
  717 carries US$100.00 (the Art. 138 live rule — the v18 label's "Ley
  SAP Art. 22" citation is never encoded) and the non-deductible
  US$50.00 excess surfaces in the casilla-734 no-gravadas value
  (FR-131, FR-133).
- **AC-012:** Given a deductible US$100.00 contribution dated
  15-March-2025 withdrawn 1-June-2027 (before 15-March-2030), then the
  withdrawal record flags before_5y=true and emits the reversal amount
  US$100.00 as rentas gravables of ejercicio 2027; the same withdrawal
  on 1-July-2030 emits nothing; and a NON-deducted contribution
  withdrawn early never reverses (FR-135).
- **AC-013:** Given a transfer of US$200.00 between the worker's own
  voluntary accounts, then the ledger stamps transfer_tax_free and no
  renta event, deduction undo or reversal flag arises (FR-134).
- **AC-014:** Given a non-affiliated natural person declaring US$30,000
  renta imponible in the prior ejercicio, then the adjacent cap input =
  US$3,000.00 (10%) with provenance recorded — no employer computation
  attaches (FR-136).
- **AC-015:** Given ANY period (including ≥ 2026-06), then no
  quincena-25 earning category, payslip line, f14.feed field or ledger
  classification exists — the only quincena-25 surface is the by-id
  pointer to SV-FREP-FR-165/166 (casillas 417/418), and absent law ⇒
  absent rows (FR-137).
- **AC-016:** Given the F-11 value export, then casillas 630-648 carry
  NO value under any configuration (dead pago-mínimo block, R21) and
  casilla 722 resolves through the SV-TAX-FR-103 pointer with no
  payroll-side computation — a deliberately-fed 630-648 value raises a
  blocking validation (FR-132).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | F-14 quartet stamped values for SALARIED rows: the S/T/U/V code lists are printed for the F-07 purchases annex (LB-003 of `03_f07-annexes-purchases.md`) and mirrored onto the F-14 annex; which exact codes apply to payroll code-01/60 rows (Q=1 gravada for retained rows? T=7 mano de obra?) is label-inference only (kin of 02-file OQ-003). FR-127 ships the stamped values as configuration with the documented default set; MH guidance or a plantilla example pins it. | no | Takumi S4 (MH guidance watch) | open |
| OQ-002 | Ley Especial Quincena Veinticinco (D.L. 499, D.O. 14-ene-2026 vol. 31679) NOT in corpus — D.O. /seleccion route down at acquisition time 2026-08-18; law-firm mirrors not registrable. BLOCKS all payroll income-treatment FRs (FR-137's absence invariant stands; kin of SOQ-09); acquisition queued as source 66. When acquired: earning category, retention/no-gravada classification and the 417/418 ledger feed land here + `fiscal-reporting/06` FR-167's annex-format assumption resolves. | yes (Quincena-25 features only) | Takumi S4 (sources watch — source 66) | open |
| OQ-003 | Non-affiliated voluntary-savings cap input: Art. 138's "renta imponible declarada en el ejercicio fiscal inmediato anterior" is the worker's OWN prior-year declared renta — employer/payroll has no source record; FR-136 ships it as a worker-supplied input with provenance; confirm acceptance of worker-declared provenance (and any DGII cross-check surface) at implementation. | no | Takumi S4 | open |
| OQ-004 | F-11 v18 currency (65_ OQ-2 kin): page footer stamp 27-02-2025 with no later "Actualizado"; v18 assumed current (MH page checked 2026-08-18). A v19 would renumber/move casillas 711-725/734 — the FR-130..132 feed keys are casilla-numbered and re-verify on any F-11 revision (watch with the fiscal-reporting F-11-side acquisition). | no | Takumi S4 (sources watch) | open |
