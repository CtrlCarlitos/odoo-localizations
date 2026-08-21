# SV — Payroll — ISR interfaces: retention-base input contract, F-14/F-910/F-11 value feeds, voluntary pension savings and the Quincena-25 income treatment

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave 4 (S4 payroll) |
| Updated | 2026-08-20 |

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
the *deducción fija* (fixed deduction) 722 pointer to
`taxation/04_isr-withholding.md` SV-TAX-FR-103); the
voluntary pension savings regime of Ley Integral del Sistema de
Pensiones (D.L. 614) Art. 138 — the ≤10% IBC deductibility of employer
and employee *ahorro previsional voluntario* (voluntary pension
savings), tax-free transfers, the <5-year withdrawal *renta gravable*
reversal flag and the non-affiliated variant; and the Quincena-25
income treatment (P10 — law acquired as 66_, D.L. 499, D.O. N° 8
T.450 14-ene-2026): the renta-no-gravada/no-retention/no-cotización
classification and the per-worker ledger + 417/418 aggregate feeds
into the F-14 v17 January annex (SV-FREP-FR-209..211) and the F-910
code-73 surface (SV-FREP-FR-212); and the ISR retention-cycle layer
of the Reglamento de Aplicación del Código Tributario (D.E. N°
117-2001, source `75_`, Arts. 95-101 — EVID-351): the retention
period as the ORDINARY PAYMENT MONTH (*mes calendario*) into which
daily/special-period/weekly/quincenal pay cycles consolidate with the
10-*días-hábiles* entero and its per-subject detail annex (Arts. 99-100),
the *constancia de retención* (retention certificate) issuance
surface per retained subject (Art. 101 + CT 145 anchor), the in-specie
remuneration market-valuation RUN-SURFACE inside payroll runs (Art. 96
— the valuation rule itself is taxation-owned by FR id), and the
aguinaldo no-retention print of Art. 95's final inciso carried as
HISTORICAL CORROBORATION ONLY (R22 governs current periods — co-cite
by id, never restated).

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
the ISR retention constancia's CT 145 intake semantics (taxation-owned,
SV-TAX-FR-113 — this file owns only the payroll-side issuance surface
of the document type, FR-145); and the F-07 R/S rentas-matrix S-wiring (65_ OQ-1,
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

W17 75_ fold-in (Arts. 95-101, EVID-351): the LB-015..019 rows below
cite the Reglamento de Aplicación del Código Tributario (D.E. N°
117-2001, D.O. N° 234 T.353 11-dic-2001, effective 19-dic-2001;
source `75_`) — the CT (05_) governs substance and 75_ develops
procedure: each row cites 75_ primary for procedure with a co-cite
note to its CT/Ley anchor, and substantive rules already encoded in
sibling files are cited BY FR ID, never restated (S9 rides).
**Vintage-note rule (rides every 75_ LB row in this file, not
repeated per row):** the 75_ print carries NO REFORMAS block (EV75
OQ-1) and post-2001 repeal by CT Art. 344 ff is print-unresolvable
(OQ-8, SOQ-06-kin) — cite as printed with the watch note; the
current-law layer is always consumed by FR id from the S2/S3 files,
never re-derived from the 2001 print.

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
| LB-009 | Formulario F-14 v17: section "INGRESOS NO GRAVADOS LEY ESPECIAL QUINCENA VEINTICINCO" inserted after row 58 — row 61 *Ingresos No Gravados Pagados por el Agente de Retención Quincena 25*, casilla 417 (número de sujetos) and casilla 418 (monto) — the declaration surface of the Ley Especial Quincena Veinticinco (D.L. 499, D.O. 14-ene-2026 vol. 31679 — **acquired 2026-08-18 as `66_`** (official DGII copy `700-DGII-LY-2025-008` via transparenciafiscal; D.O. `/seleccion` outage workaround); current authority for the Quincena-25) | F-14 v17 casillas 417/418: subject count and amount of Quincena-25 no-gravado payments — the form-level pointer this file cites by FREP FR id; the law is in corpus as `66_` and the payroll income treatment lands as FR-137/142/143 below | `sv/sources/59_F14_v17_form_visual.pdf` | v17 vs v16 diff, row 61 / casillas 417-418 (EVID-184) |
| LB-010 | D.E. 10-2025, Art. 1 d) — interface anchor only: retention base considers only remuneraciones gravadas, determined by deducting from TOTAL period remunerations the remuneraciones no gravadas and the cotizaciones laborales a la Seguridad Social; cotizaciones previsionales to the AFPs and public pension institutes are comprised within the no-gravadas concept — the base FORMULA is OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-104 and consumed by reference; this file states only the payroll-side input contract | Retention-base interface: worker SS/pension cotizaciones excluded from the gravadas base — payroll supplies the stamped aggregates; the computation is taxation's by FR id, never restated | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 d) p.3 (EVID-156; via taxation/04 LB-008 / SV-TAX-FR-104) |
| LB-011 | Ley ISR, Art. 4 num. 16 + D.E. 10-2025, Arts. 1 f)/g) — interface anchors only: the aguinaldo exento/gravado split, retention vintages and recálculo aggregation are OWNED by `taxation/04_isr-withholding.md` (SV-TAX-FR-120 split; SV-TAX-FR-116 aggregation; SV-TAX-FR-110/111 recálculo) with the gross-prima supply OWNED by `04_statutory-benefits.md` (SV-PAY-FR-060/061/062) — consumed by reference into this file's F-14 J-K feed | Aguinaldo interface by reference: the split computation is taxation's and the gross prima file 04's; this file wires only the J-K declared values | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` + `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 4.16 p.7 (EVID-165); Arts. 1 f)/g) (EVID-158/159; via taxation/04 and payroll/04 by FR id) |
| LB-012 | Ley Especial Quincena Veinticinco (D.L. 499), Art. 4: "se declara como rentas no gravables, y en consecuencia excluidos del cómputo de la renta obtenida, el monto que reciban los trabajadores en concepto de Quincena Veinticinco. Asimismo, estos ingresos... no estarán afectos a la Retención del Impuesto sobre la Renta, y gozarán del beneficio de la inembargablilidad [sic]. Para efectos tributarios, los montos pagados en concepto de Quincena Veinticinco constituliran [sic] gasto deducible para el patrono, siempre que hayan sido efectivamente pagados y debidamente documentados, conforme a lo dispuesto en la Ley de Impuesto sobre la Renta." | Quincena-25 fiscal treatment (worker side): amounts received as Quincena Veinticinco are declared rentas no gravables and excluded from the computation of renta obtenida; not subject to ISR Retention; unseizable (inembargabilidad); (employer side) amounts paid are a deductible employer expense provided they were effectively paid and duly documented per the Ley ISR | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 4 p.4 (EVID-237) |
| LB-013 | Ley Especial Quincena Veinticinco (D.L. 499), Art. 1 (payment invariants): "debe ser pagado de forma integra [sic] y sin ningún descuento a los sujetos beneficiados, independiente del salario ordinario, aguinaldo, compensación adicional en efectivo y de otras prestaciones laborales... y no formará parte de la base de cálculo de otras prestaciones, por lo que no sera [sic] objeto de ninguna clase de retención. Consecuentemente, el ingreso complementario Quincena Veinticinco... en ningún caso deberá ser objeto de retención ni descuento alguno por concepto de aportes u otras obligaciones de Seguridad Social o del Régimen Previsional." | The benefit must be paid in full and without any deduction, independent of ordinary salary, aguinaldo, cash compensación adicional and other labor benefits; it does not form part of the calculation base of other benefits, hence is not subject to any kind of retention; in no case may it be subject to retention or deduction for contributions or other Social Security or Pension-Regime obligations | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 1 p.2 (EVID-236) |
| LB-014 | Guía de Orientación Quincena Veinticinco (67_), §3.f: "En el Informe Anual de Retenciones (F-910), el monto pagado en concepto de Quincena Veinticinco, se verá reflejado en la columna de NO GRAVADOS, el cual se identificará de conformidad al Código 73 Ingresos No Gravados Pagados Quincena Veinticinco, generado de forma automática... de acuerdo a los datos cargados en anexo... (F-14)"; §3.g: renta-en-línea shows it as an ingreso no gravado (Anexo 6 rentas-no-gravadas row gains "Quincena Veinticinco" — *casilla 724 operative, 734 = guía typo [sic] (in-file resolution, evidence OQ-3)*); Anexo 3: "El anexo de planilla Quincena Veinticinco, solo podrá ser informado en el mes de enero de cada ejercicio fiscal" | Reporting chain: the F-910 NO GRAVADOS column auto-populates with Código 73 "Ingresos No Gravados Pagados Quincena Veinticinco" from the F-14 annex data; the employee's renta-en-línea shows it as an ingreso no gravado (casilla 724); the planilla annex is January-only per ejercicio fiscal | `sv/sources/67_Guia_Orientacion_Quincena25.pdf` | §§3.f/3.g + Anexos 3/6 (EVID-238) |
| LB-015 | Reglamento de Aplicación del Código Tributario (D.E. N° 117-2001), Art. 95 (develops CT 155): permanent services = "aquellos cuya prestación es regulada por la Ley Laboral y su remuneración es el devengo de salarios, sueldos, sobresueldos, horas extras, primas, comisiones, gratificaciones, bonificaciones, aguinaldos y cualquier otra compensación por servicios personales, ya sean que estos se paguen en efectivo o en especie… la prestación de servicios es por tiempo indefinido o bien cuando dichos servicios se contraten por un plazo determinado sea a tiempo completo, medio tiempo o tiempo parcial con carácter de subordinación o dependencia, considerándose como parcial los medios tiempos, horas clase, horas médicos, y similares"; final inciso: "No obstante que los aguinaldos constituyen remuneraciones de carácter permanente gravados con el Impuesto sobre la Renta, no serán sujetos a retención toda vez que mediante Decreto Legislativo gocen de tal prerrogativa." — the final inciso restates CT 155-II's blanket no-retention AS OF THE 2001 PRINT; R22 GOVERNS current periods (Ley ISR Art. 4.16 standing 2-SMM split, D.L. 458-2019 floor-deducted excess — SV-TAX-FR-120 by id) | Permanent (dependent) services sweep: salaries, sueldos, sobresueldos, horas extras, primas, comisiones, gratificaciones, bonificaciones, aguinaldos and any other personal-services compensation, cash or in-specie, indefinite or fixed term, full/half/part-time (medios tiempos, horas clase, horas médicos included) — the payroll population this file's feeds cover; the final inciso = historical corroboration only (FR-147), never a current no-retention rule | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 95 p.60 (EVID-351; verified 75_ txt lines 3110-3123) |
| LB-016 | Reglamento de Aplicación del CT, Art. 96: "Están sujetas a retención toda clase de remuneraciones, incluyendo por tanto salarios, sueldos de tiempo completo o de tiempo parcial, compensaciones adicionales como sobresueldos, horas extras, dietas, gratificaciones, primas, comisiones, aguinaldos, bonificaciones, gastos de representación y cualquier otra compensación por servicios personales sea que se paguen en efectivo, en especie o mediante operaciones contables"; no labor dependency → "sujetas a los porcentajes de retención establecidos en el artículo 156 del Código Tributario"; sickness-license remunerations "sujetas a retención de acuerdo a las tablas respectivas"; in-specie: "se computarán al precio de mercado a la fecha en que se entregue como valor de la remuneración"; fully-in-specie: the agent "deberá retener el impuesto que corresponda y enterarlo dentro del plazo establecido" — the valuation RULE and CT 156 matrix are OWNED by `taxation/04_isr-withholding.md` (SV-TAX-FR-397; SV-TAX-FR-128 zone) and consumed by reference | All-remunerations retention sweep (cash, in-specie, operaciones contables); independents take the CT 156 percentages (taxation-owned); in-specie remuneration values at DELIVERY-DATE market price; a fully-in-specie payment still withholds and enters — no cash-payment escape | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 96 pp.60-61 (EVID-351; verified 75_ txt lines 3131-3157) |
| LB-017 | Reglamento de Aplicación del CT, Arts. 97-98: Art. 97 — no retention on "los productos o utilidades excluidos del concepto de renta y las rentas no gravables, a que se refieren los artículos 3 y 4 de la Ley de Impuesto sobre la Renta respectivamente, así como las remuneraciones de carácter temporal que obtengan las personas naturales por la recolección de productos agrícolas de temporada"; Art. 98 (CT 154 inc. 2º) — AT written designation of retention agents against morosos, in which "se expresará el nombre completo, número de Identificación Tributaria, monto del adeudo principal y multas por infracciones cometidas y la cantidad que deberá retener y desde cuando" — awareness only: the exclusion gates ride the matrix and the Ley ISR Art. 3-4 anchors already encoded (`taxation/04_isr-withholding.md` SV-TAX-FR-121/398, cited by id; the temporal-agro exclusion is SV-TAX-FR-398's); Art. 98 is AT-side only — no payroll FR attaches | Exclusions from retention (Ley ISR Arts. 3-4 no-renta/no-gravada items + temporal-agricultural harvest labor) and the AT's moroso-collection agent designation — both consumed by id elsewhere; recorded here for article-range completeness of the 75_ retention block | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 97-98 p.61 (EVID-351; verified 75_ txt lines 3164-3186) |
| LB-018 | Reglamento de Aplicación del CT, Arts. 99-100: Art. 99 — "Por período de pago para efectos de retenciones del Impuesto sobre la Renta, se entiende el mes calendario en el que el agente de retención paga ordinariamente la remuneración sea ésta total o parcial". Art. 100 — "Las cantidades retenidas deberán ser enteradas al colector respectivo, dentro de los diez días hábiles que inmediatamente sigan al vencimiento del mes calendario en que se efectúa la retención"; "Cuando se trate de remuneraciones pagadas por día, por período especial, semana o quincena, el agente de retención deberá consolidar en períodos mensuales, las respectivas retenciones, debiendo proceder a su entero obligatoriamente dentro del término general establecido en el inciso precedente"; entero with declaración jurada; annex to the agent's copy: "un detalle de las personas naturales o jurídicas que hayan sido objeto de retención, especificando el nombre, denominación o razón social y número de identificación tributaria del sujeto de retención, así como el monto devengado e impuesto retenido" — the 10-hábiles window corroborates the current-law deadline owner `taxation/01_isr-framework.md` SV-TAX-FR-032 (Ley ISR Art. 62, by id) | Retention period = the ORDINARY PAYMENT MONTH (mes calendario); sub-monthly cycles (day/special/week/quincena) consolidate monthly; entero within the ten días hábiles after month-end with declaración jurada + per-subject detail annex (name · NIT · devengado · retenido — the paper ancestor of the F-14 annex) | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 99-100 p.62 (EVID-351; verified 75_ txt lines 3193-3221) |
| LB-019 | Reglamento de Aplicación del CT, Art. 101 (+ CT 145 anchor): "Todo agente de retención está obligado a extender constancia al contribuyente, por las cantidades retenidas… en el que se exprese lo establecido en el artículo 145 del Código"; for Órganos del Estado, government dependencies, Municipalidades and official autonomous institutions, the constancia "deberá ser firmada por la persona responsable del pago de las remuneraciones" — the certificate's CT 145 CONTENT and intake semantics (prior-employer constancia within 15 días hábiles of retirement) are OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-113 (by id); this file owns only the payroll-side issuance surface (FR-145) | Constancia de retención duty: every retention agent must issue the certificate for retained amounts, signed by agent retenedor / representante legal / apoderado (State: the payment responsible), expressing the CT 145 content | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Art. 101 p.62 (EVID-351; verified 75_ txt lines 3222-3228) |

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
F-11 version discovery (67_ Anexos 1/8, EVID-238): the 65_ F-11 v18
print is SUPERSEDED AS CURRENT PRINT by v19 — a new casilla 319
"Crédito Tributario Quincena Veinticinco" inside the IMPUESTO
DETERMINADO subtraction (the casilla-330 formula includes 319) — and
the v19 print STILL prints the dead pago-mínimo rows (R21 extends to
v19: never feed, kin of LB-006); v20 ("Versión 20 — Declaración de
Impuesto sobre la Renta para Sujetos con Régimen Especial", renamed,
Certificado de Crédito Tributario anexo) covers special-regime
subjects; both prints are acquisition candidates (numbering ≥71 —
OQ-004 sharpened, stays open).

Version regime (D12): no dated VALUES are owned by this file — the SS
cap values re-date through `05_social-security-contributions.md`'s
`ss_contributions.csv` (its SV-PAY-FR-081, re-dated per instrument
acquisition per its SV-PAY-FR-084); the SMM feed belongs to
`02_minimum-wage.md`; the form vintages consumed (F-11 v18 page date
27-02-2025 — 65_ OQ-2 watch; F-910 v9; F-14 v16 annex + v17 form gate
per SV-FREP-FR-165) are owned by the fiscal-reporting files. The 65_
F-11 v18 print is superseded as current print by v19 (casilla 319
Quincena credit; still prints the dead pago-mínimo rows — R21
extends) and v20 (special-regime subjects) — acquisition candidates
≥71 (OQ-004 sharpened, stays open). The Quincena-25 surface is
version-gated from period 2026-06 by
SV-FREP-FR-165 (cited, never restated); the January-annex reporting
window is SV-FREP-FR-210's (cited, never restated).

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
  The `min()` expression is the interface formulation of Art. 4.3's
  conditional exemption ("SIEMPRE QUE NO EXCEDAN", LB-003) — the law
  prints a conditional exemption, not a split arithmetic; the bend is
  in-mandate per cluster P9 (the exempt/excess stamps require it).
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
  death/incapacity INDEMNITIES, not leave-replacing remuneration; sick
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
  touched here); the casillas 718-720/738 silence is evidence-faithful —
  718-720 carry no extracted label in EVID-210 and 738
  ("Indemnizaciones No Gravadas") rides the FR-123 no_gravada stamps
  with NO dedicated payroll feed, both re-verifying at the v19/v20
  acquisition (OQ-004). (LB-004; EVID-210; cross-ref SV-TAX-FR-105,
  SV-PAY-FR-123)
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

### 3.7 Quincena Veinticinco income treatment and feeds (P10 — 66_ acquired)

- **SV-PAY-FR-137:** The system shall classify every Quincena-25
  payment as *renta no gravada* per D.L. 499 Art. 4 (the special-law
  declaration prevailing per its Art. 8; `taxation/01` SV-TAX-FR-173
  owns the ISR-side rule — cited by id): stamped no_gravada by the
  matrix (FR-004 row), EXCLUDED from the retention base and from the
  June/December recálculo aggregation (never in the SV-TAX-FR-104
  inputs of FR-121), generating NO ISR retention line, NO worker
  SS/pension cotización (out of IBC per `05` and FR-141) and NO entry
  in any benefit base — replacing this file's former absence invariant
  (the law was acquired as 66_ on 2026-08-18; the invariant is
  withdrawn). (LB-012 Art. 4; LB-013 Art. 1; EVID-236/237; cross-ref
  SV-TAX-FR-173, SV-PAY-FR-121, SV-PAY-FR-141)
- **SV-PAY-FR-142:** The system shall maintain, per worker and
  ejercicio, the Quincena-25 ledger record carrying EXACTLY the seven
  annex fields of the F-14 v17 January annex (consumed by
  SV-FREP-FR-209): A *apellidos y nombres* (≤100 chars, uppercase, no
  commas/quotes) · B *NIT* (≤14 digits, no hyphens/plecas) XOR C *DUI*
  (≤9 digits) · D *fecha de pago* dd/mm/aaaa · E *salario nominal*
  (4 enteros + 2 decimales, no thousands separator) · F *quincena
  veinticinco* amount (3+2) · G *período* mmaaaa — the payroll-owned
  value source; amounts from FR-138; the XOR rule validated
  payroll-side before export. (EVID-239; cross-ref SV-FREP-FR-209)
- **SV-PAY-FR-143:** The system shall produce the declaration
  aggregates consumed by SV-FREP-FR-166: casilla **417** = count of
  workers paid and casilla **418** = total amount, per declaración
  period — reporting-only, never in retention arithmetic
  (SV-FREP-FR-166's isolation by id); reporting window January-only
  per SV-FREP-FR-210. (EVID-238; cross-ref SV-FREP-FR-166,
  SV-FREP-FR-210)

### 3.8 ISR retention cycle — 75_ layer (retention-month consolidation, entero annex, constancia, in-specie surface)

- **SV-PAY-FR-144:** The system shall consolidate ISR retentions on
  the ORDINARY PAYMENT MONTH (*mes calendario*): the retention period
  is the calendar month in which the retention agent ordinarily pays
  the remuneration, in whole or in part (Art. 99), and payslips of
  sub-monthly cycles — paid *por día, por período especial, semana o
  quincena* — consolidate their retentions into ONE retention-month
  record per employee and month (Art. 100: the agent "deberá
  consolidar en períodos mensuales, las respectivas retenciones");
  the entero of the consolidated sums falls within the TEN *días
  hábiles* immediately following month-end — the deadline SCHEDULING
  is owned by `taxation/01_isr-framework.md` SV-TAX-FR-032 (by id;
  75_ Arts. 99-100 as the corroborated anchor) and the business-day
  arithmetic is the días-hábiles engine
  `fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-202..204
  (first_n_habiles(month, 10), by id — never re-implemented here);
  each retention-month record carries the per-subject entero annex
  detail of Art. 100 (name, *denominación o razón social* and NIT of
  the retained subject, plus *monto devengado* and *impuesto
  retenido* — the paper ancestor of the F-14 annex, whose electronic
  value source is the FR-126 f14.feed record, consumed by id).
  (LB-018; EVID-351; cross-ref SV-TAX-FR-032, SV-FREP-FR-202,
  SV-FREP-FR-203, SV-FREP-FR-204, SV-PAY-FR-126)
- **SV-PAY-FR-145:** The system shall maintain a *constancia de
  retención* (retention certificate) document type per retained
  subject, issued on request or per period (Art. 101 + the CT 145
  anchor): the certificate states the retained amounts and is signed
  by the agent retenedor, *representante legal* or *apoderado* — for
  State organs, government dependencies, Municipalidades and official
  autonomous institutions, by "la persona responsable del pago de las
  remuneraciones"; its VALUES are sourced exclusively from this
  file's feed records — the FR-126 f14.feed (monthly detail), the
  FR-129 f910.feed (annual consolidation) and the FR-130
  f11.deduction rows — never recomputed (the F-14/F-910/F-11 surfaces
  own their layouts, cited by id through those FRs); the CT 145
  content and intake semantics (the prior employer's constancia
  within 15 días hábiles of retirement, consumed by the June/December
  recap) are OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-113
  — cited by id, never restated here. (LB-019; EVID-351; cross-ref
  SV-TAX-FR-113, SV-PAY-FR-126, SV-PAY-FR-129, SV-PAY-FR-130)
- **SV-PAY-FR-146:** The system shall encode the in-specie
  remuneration RUN-SURFACE only: payslip lines paid in species
  (*productos, frutos, alojamiento, alimentación o cualquier otra
  compensación en especie*) enter the FR-144 retention-month ledger
  at their market value on the DELIVERY date, with the valuation rule
  OWNED by `taxation/04_isr-withholding.md` SV-TAX-FR-397 (by id —
  "se computarán al precio de mercado a la fecha en que se entregue
  como valor de la remuneración"; the market-price-factors root is
  `16_ct-procedures.md` SV-TAX-FR-357, by id) and NEVER recomputed
  payroll-side; a payment made TOTALLY in species still withholds
  (Art. 96: the agent "deberá retener el impuesto que corresponda y
  enterarlo dentro del plazo establecido" — the no-cash-escape rule
  rides SV-TAX-FR-397 by id), the retention entering the FR-144
  consolidation like any cash retention. (LB-016; EVID-351;
  cross-ref SV-TAX-FR-397, SV-TAX-FR-357, SV-PAY-FR-144)
- **SV-PAY-FR-147:** The system shall treat the 75_ Art. 95
  final-inciso print (2001) as HISTORICAL CORROBORATION ONLY of the
  aguinaldo no-retention prerogative ("No obstante que los aguinaldos
  constituyen remuneraciones de carácter permanente gravados con el
  Impuesto sobre la Renta, no serán sujetos a retención…"): R22
  GOVERNS current periods — the live rule is the Ley ISR Art. 4.16
  standing 2-SMM exemption split with the D.L. 458-2019
  floor-deducted excess, OWNED by `taxation/04_isr-withholding.md`
  §3.6 (SV-TAX-FR-120 vintage rows) and consumed BY ID into the
  FR-126 J/K feed — no blanket no-retention invariant, no vintage row
  and no exemption value is restated or encoded here; payroll/04's
  own 75_ row (its LB-029) carries the same historical layer for the
  aguinaldo engine (co-cite only). (LB-015; EVID-351; R22; cross-ref
  SV-TAX-FR-120, SV-PAY-FR-126)

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

**Quincena-25 per-worker ledger (per worker-ejercicio)** — fields
string-typed to mirror the export contract (SV-FREP-FR-209 truncation
discipline):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.quincena.feed (new) | a_apellidos_nombres | char(100) | A *apellidos y nombres*: uppercase, no commas/quotes (≤100 chars) | FR-142 |
| l10n_sv.pay.quincena.feed | b_nit XOR c_dui | char(14)/char(9) | B *NIT* ≤14 digits no hyphens/plecas XOR C *DUI* ≤9 digits — XOR validated payroll-side before export | FR-142 |
| l10n_sv.pay.quincena.feed | d_fecha_pago | date-format char | D *fecha de pago* dd/mm/aaaa | FR-142 |
| l10n_sv.pay.quincena.feed | e_salario_nominal · f_quincena_veinticinco | monetary-string | E *salario nominal* 4 enteros + 2 decimales, no thousands separator; F *quincena veinticinco* 3+2 — amounts from FR-138 | FR-142 |
| l10n_sv.pay.quincena.feed | g_periodo · ejercicio | char(6)/char(4) | G *período* mmaaaa; ejercicio = the annual grouping key of FR-143's aggregates | FR-142, FR-143 |

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

**ISR retention-month ledger and constancia (75_ layer):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.pay.retention.month (new) | employee_id · period · cycle_sources | m2o/char(6)/m2m | ONE record per employee × retention month (mes calendario, Art. 99); sub-monthly cycles (día / período especial / semana / quincena) consolidate here (Art. 100) | FR-144 |
| l10n_sv.pay.retention.month | consolidated_retention · annex_detail | monetary(2dp)/related | consolidated monthly retentions; annex fields per Art. 100: nombre / denominación o razón social · NIT · monto devengado · impuesto retenido (value provenance = the FR-126 f14.feed records, by id) | FR-144 |
| l10n_sv.pay.retention.month | entero_deadline | date (computed) | the 10 días hábiles after month-end — scheduled per SV-TAX-FR-032 (by id) over the SV-FREP-FR-202..204 engine (by id); never computed locally | FR-144 |
| l10n_sv.pay.retention.month | in_specie_value_source | pointer (char) | fixed pointer `taxation/04 SV-TAX-FR-397` — in-specie lines enter at delivery-date market value; the valuation is never computed payroll-side | FR-146 |
| l10n_sv.pay.retention.constancia (new) | subject_id · period_from · period_to · issued_on_request · signatory_role | m2o/date/date/boolean/select | per-subject constancia document type (Art. 101 + CT 145 anchor); signatory_role: agent_retenedor · representante_legal · apoderado · state_payment_responsible; values sourced exclusively from the FR-126/129/130 records | FR-145 |
| l10n_sv.pay.retention.month | unentered_exposure_flag | boolean (surfaced) | perpetual-exposure surfacing of `taxation/16_ct-procedures.md` SV-TAX-FR-375 (by id — taxation/16 owns the Art. 23 invariant): activates when the entero deadline lapses unmet and NEVER time-expires; payroll owns the payroll-ledger surfacing only — NO payroll FR attaches | AC-022; SV-TAX-FR-375 by id |
| l10n_sv.pay.retention.month | erroneous_refund_window_end | date (surfaced) | 2-year refund-claim window of `taxation/16` SV-TAX-FR-378 (by id — taxation/16 owns the Art. 133 caducidad): ends two years from the pago indebido date of an erroneous retention; surfaced for exposure tracking only — NO payroll FR attaches | AC-022; SV-TAX-FR-378 by id |

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
| FR-137 | odoo | l10n_sv.pay.quincena feed stamps | renta no gravada; no retention/cotización/base entry | 66_ Art. 4 declaration + Art. 1 invariants (LB-012/013; EVID-236/237); ISR rule = SV-TAX-FR-173 by id; never in the SV-TAX-FR-104 inputs; former absence invariant withdrawn (law acquired as 66_) |
| FR-142 | odoo | l10n_sv.pay.quincena.feed | seven annex fields A..G + ejercicio | string-typed export contract (SV-FREP-FR-209 truncation discipline); XOR NIT/DUI validated payroll-side; amounts from FR-138 |
| FR-143 | odoo | l10n_sv.pay.quincena.feed aggregate | casillas 417/418 | count of workers paid + total amount per declaración period; consumed by SV-FREP-FR-166 (isolation by id); January-only window per SV-FREP-FR-210 |
| FR-144 | odoo | l10n_sv.pay.retention.month | consolidation + annex + deadline | Retention period = mes calendario (Art. 99); día/período especial/semana/quincena cycles consolidate monthly (Art. 100); entero deadline = SV-TAX-FR-032 by id over the SV-FREP-FR-202..204 engine; annex detail values from the FR-126 records; exposure-pair fields (§4) surface on this ledger by id to SV-TAX-FR-375/378 — no payroll FR for the pair |
| FR-145 | odoo | l10n_sv.pay.retention.constancia | constancia issuance surface | Art. 101 + CT 145 anchor; values exclusively from FR-126/129/130 records (by id); CT 145 intake semantics = SV-TAX-FR-113 (by id, never restated) |
| FR-146 | odoo | l10n_sv.pay.retention.month + hr.payslip.line (in-specie) | in-specie run-surface | Delivery-date market value per SV-TAX-FR-397 (by id; factors root SV-TAX-FR-357); fully-in-specie still retains and enters the FR-144 consolidation |
| FR-147 | odoo | (pointer only) | historical corroboration | 75_ Art. 95 final inciso = 2001-print layer (LB-015); R22 current rule = taxation/04 §3.6 SV-TAX-FR-120 by id; nothing encoded — no invariant, no vintage, no value |

Version-regime notes (D12): no dated values live in this file. The SS
cap values consumed re-seed through `ss_contributions.csv`
(`05_social-security-contributions.md` SV-PAY-FR-081/084); the F-14
v16/v17 and F-11 v18/F-910 v9 vintages are owned by the
fiscal-reporting files (F-11 v19/v20 confirmed to exist — feed keys
re-verify on acquisition, this file's OQ-004); the Quincena-25 gate
date (2026-06) is cited from
SV-FREP-FR-165 and the January-annex engine, code-73 auto-population
and renta-en-línea feed from SV-FREP-FR-209..212 (all cited by id,
never restated as local configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a monthly payslip with devengado-family lines
  US$1,000.00, worker ISSS US$30.00 (clamped, 05 FR-070) and worker
  AFP US$72.50 on IBC US$1,000.00, then the retention-input aggregates
  expose total US$1,000.00 / no-gravadas US$0.00 / worker cotizaciones
  US$102.50, and the retention base computed by SV-TAX-FR-104 over
  them = 1,000.00 − 102.50 = US$897.50 — this file supplies the
  aggregates only; the employer's 8.75% + 7.5% legs never appear in any
  input (FR-121).
- **AC-002:** Given a settlement of indemnización US$2,400.00
  (60 day-credits = 30 days × 2 years of service at daily básico
  US$40.00, below the 4×SMM clamp) PLUS a voluntary-retirement bonus
  of US$1,000.00 — total US$3,400.00 — and a twelve-month average of
  salaries subject to retention of US$35.00/day, then the Art. 4.3
  exempt cap = 30 days × 2 years × min(US$40.00, US$35.00) =
  US$2,100.00: US$2,100.00 stamps no_gravada and the excess
  US$1,300.00 stamps gravada, routed to SV-TAX-FR-116 as an
  extraordinary remuneration — the matrix crosscheck_oq flag is gone
  (FR-123).
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
  carries G = US$1,000.00 — the full gross devengado per the matrix
  families, with the AFP/SS cotizaciones INSIDE G per the plantilla
  note (never netted at the G level; the netting lives only in the
  FR-121 retention inputs) — H = 0.00 (no bonus lines), the seven SS
  columns L=72.50 · M=30.00 · N..R=0.00 (regime isss_sip) and
  W=MMYYYY — consumed by SV-FREP-FR-143/145 and passing the
  SV-FREP-FR-150 cap validation unchanged (FR-126).
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
- **AC-015:** Given a January-2027 payroll with Quincena payments to 10
  workers totalling US$5,000.00 (all gates passed), then each payment
  line stamps no_gravada with no retention line and no IBC/base
  effect, and the ledger yields 10 feed records + aggregates 417=10 /
  418=5,000.00 consumed by SV-FREP-FR-166/209 — the by-id pointers
  replace the former absence invariant (FR-137, FR-142, FR-143).
- **AC-016:** Given the F-11 value export, then casillas 630-648 carry
  NO value under any configuration (dead pago-mínimo block, R21) and
  casilla 722 resolves through the SV-TAX-FR-103 pointer with no
  payroll-side computation — a deliberately-fed 630-648 value raises a
  blocking validation (FR-132).
- **AC-017:** Given a worker with NIT 22222222222222 and DUI both
  present, the feed record fails payroll-side validation (XOR) and is
  not exported; given name "Prueba Persona", the export field renders
  `PRUEBA PERSONA` uppercase with the amount `250.00` and período
  `012027` — mirroring the 70_ example-row contract (FR-142).
- **AC-018:** Given a quincenal employee with March-2027 retentions
  US$25.00 and US$30.00 on the two quincena payslips plus a
  daily-cycle settlement retention of US$5.00 in the same month, then
  ONE retention.month record consolidates US$60.00 listing the three
  cycle sources, its annex detail (name + NIT + devengado + retenido)
  is drawn from the FR-126 f14.feed records, and entero_deadline
  resolves to the 10th día hábil of April 2027 scheduled per
  SV-TAX-FR-032 over the SV-FREP-FR-202..204 engine — never by local
  business-day arithmetic (FR-144).
- **AC-019:** Given a worker requesting a constancia for ejercicio
  2026, then the document issues from the f910.feed/f14.feed values
  (per-month and annual retained sums, never recomputed) with
  signatory role agent/representante-legal/apoderado — and given a
  State-organ employer, signatory_role = state_payment_responsible;
  the CT 145 15-días-hábiles intake flow of the June/December recap
  never triggers payroll-side (SV-TAX-FR-113 by id) (FR-145).
- **AC-020:** Given a December payslip whose lodging benefit is valued
  at its delivery-date market price US$300.00 (in-specie), then the
  line enters the retention.month at US$300.00 with the
  in_specie_value_source pointer to SV-TAX-FR-397 (no payroll-side
  price computation exists), and a FULLY in-specie payment still
  produces its retention line inside the month's consolidation
  (FR-146).
- **AC-021:** Given any aguinaldo line of a current period, then NO
  blanket no-retention applies from the 75_ Art. 95 print — the
  exento/gravado split resolves solely through SV-TAX-FR-120's
  vintages (2025+: standing 2-SMM exemption, floor-deducted excess)
  into the FR-126 J/K feed; the 75_ LB-015 row surfaces only as the
  historical corroborating layer (FR-147; R22).
- **AC-022:** Given a retention.month whose entero deadline lapses
  unmet, then unentered_exposure_flag activates and NEVER
  time-expires — the perpetual-exposure invariant is SV-TAX-FR-375's
  (by id; payroll surfaces it on the ledger, no payroll FR owns it);
  and given an erroneous retention with pago indebido date
  1-March-2025, then erroneous_refund_window_end surfaces
  1-March-2027 (the Art. 133 2-year caducidad of SV-TAX-FR-378, by
  id) after which the agent's refund claim is time-barred — surfacing
  only, never an enforced cutoff. (§4 exposure-pair fields;
  SV-TAX-FR-375/378 by id — no payroll FR)

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | F-14 quartet stamped values for SALARIED rows: the S/T/U/V code lists are printed for the F-07 purchases annex (LB-003 of `03_f07-annexes-purchases.md`) and mirrored onto the F-14 annex; which exact codes apply to payroll code-01/60 rows (Q=1 gravada for retained rows? T=7 mano de obra?) is label-inference only (kin of 02-file OQ-003). FR-127 ships the stamped values as configuration with the documented default set; MH guidance or a plantilla example pins it. | no | Takumi S4 (MH guidance watch) | open |
| OQ-002 | Ley Especial Quincena Veinticinco (D.L. 499, D.O. 14-ene-2026 vol. 31679) NOT in corpus — D.O. /seleccion route down at acquisition time 2026-08-18; law-firm mirrors not registrable. BLOCKS all payroll income-treatment FRs (FR-137's absence invariant stands; kin of SOQ-09); acquisition queued as source 66. When acquired: earning category, retention/no-gravada classification and the 417/418 ledger feed land here + `fiscal-reporting/06` FR-167's annex-format assumption resolves. **RESOLVED 2026-08-18 (acquisition): the law was acquired as `66_` (official DGII copy `700-DGII-LY-2025-008` via transparenciafiscal — D.O. `/seleccion` outage workaround; EVID-236..239); FR-137 rewritten + FR-142/143 landed (this wave); the `fiscal-reporting/06` OQ kin resolves through SV-FREP-FR-209..211.** | no (was yes — Quincena-25 features only; resolved) | Takumi S6 (acquisition) | resolved (acquisition) |
| OQ-003 | Non-affiliated voluntary-savings cap input: Art. 138's "renta imponible declarada en el ejercicio fiscal inmediato anterior" is the worker's OWN prior-year declared renta — employer/payroll has no source record; FR-136 ships it as a worker-supplied input with provenance; confirm acceptance of worker-declared provenance (and any DGII cross-check surface) at implementation. | no | Takumi S4 | open |
| OQ-004 | F-11 v18 currency (65_ OQ-2 kin): page footer stamp 27-02-2025 with no later "Actualizado"; v18 assumed current (MH page checked 2026-08-18). **SHARPENED 2026-08-18 (67_ Anexos 1/8, EVID-238): v19 and v20 CONFIRMED to exist — v19 adds casilla 319 "Crédito Tributario Quincena Veinticinco" (IMPUESTO DETERMINADO subtraction; the casilla-330 formula includes 319) and STILL prints the dead pago-mínimo rows (R21 extends to v19 — never feed); v20 = special-regime subjects ("Versión 20 — Declaración de Impuesto sobre la Renta para Sujetos con Régimen Especial", renamed, Certificado de Crédito Tributario anexo); the 65_ v18 print is superseded as current print.** The FR-130..132 feed keys are casilla-numbered (713-725/734) and re-verify on acquisition of the v19/v20 prints (numbering ≥71; watch with the fiscal-reporting F-11-side acquisition). | no | Takumi S6 (sources watch — numbering ≥71) | open |
