# GT — Payroll — CT salary model: salario, salario completo and salary protection

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | payroll |
| Status  | draft |
| Authors | GT synthesis wave S-GT3 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the Guatemala Código de Trabajo (Labor Code, CT, Decreto
1441) salary-and-protection core every other GT payroll computation builds
on: the *salario o sueldo* (salary or wage) concept of Art. 88 with its three
statutory pay bases — *por unidad de tiempo* (unit of time: month,
*quincena* (fortnight), week, day, hour), *por unidad de obra* (unit of work:
*pieza* (piece), *tarea* (task), *precio alzado* (lump price), *destajo*
(piecework)) and *participación* (participation in the employer's profits,
sales or collections) — including mixed forms and the no-loss-risk-to-worker
rule; the *salario completo* (complete salary) of Art. 93 — ordinary +
extraordinary earnings — as THE integration basis for every indemnización
and prestación the Code grants; payment form and cadence (legal currency
only; ≤ quincena for manual workers, ≤ month for intellectual workers and
domestic service; participation advances with at-least-annual definitive
liquidation); the ≤30% in-kind ceiling for campesino workers; the
equal-salary-for-equal-work rule with its sex-discrimination burden shift
(Art. 89); statutory salary books keyed on headcount (*libro de salarios*
(salary ledger) ≥10 permanent workers / IGSS-model *planillas* (payroll
sheets) for 3–9) plus the annual MinTrabajo statistical report; salary
advances (no interest ever; ≥5-pay-period amortization) and the first-class
wage-credit privilege capped at six months of wages; the *inembargabilidad*
(unembargability) garnishment-protection ladder as a STRUCTURE-ONLY
requirement (1961-scale bracket numerics banned — GOQ-73) with the alimony
50% priority + 10% secondary carve-outs; the money-claims prescription
ladder (20 días hábiles / 30 días hábiles / 4 months / 2 years) with
partial-payment interruption; *intermediario* (intermediary) solidarity and
the pro-operario interpretive principles; the CT zero-bonus-articles
negative finding (EVID-299); and enforcement pointers (sanction values
never derived here).

It does **not** cover: jornada classification, overtime, descanso semanal
and asuetos (`02_working-time-overtime.md`); the salario mínimo chassis and
dated AG tables (`03_minimum-wage.md` + `salario_minimo.csv`); statutory
bonuses — bono 14, incentivo, and the corpus-absent December aguinaldo
regime (`04_statutory-bonuses.md`); vacaciones, maternidad and menores
(`05_vacaciones-maternidad.md`); contracts, despido and indemnización
(`06_contracts-termination.md`); IGSS contributions, planilla electrónica
and IGSS-planilla mechanics (`07_igss-contributions.md`); IRTRA/INTECAP
patronal charges (`08_irtra-intecap.md`); ISR/IVA payroll interfaces
(`09_isr-iva-interfaces.md`); or sanction values (owned by
`gt/requirements/taxation/06_ct-procedures.md` via the Código Tributario
art. 94 family — never re-derived here). Later S-GT3 payroll files consume
this file's salario-completo and pay-basis FRs by id (their FR ids are
assigned at their dispatch); the one exact external id cited is
GT-TAX-FR-146 (salaries off the IGSS planilla are employer-non-deductible).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): **CT labor
LBs cite 32_ as "CT art. N (texto según edición conmemorativa 2024,
MinTrabajo)" — no "current through" date claimable** (the edition is a
commemorative MinTrabajo print of indeterminate consolidation cutoff: latest
printed annotation D18-2001 with demonstrably later unannotated content —
GOQ-70/71; the qualifier carried on every CT row below IS the R44
mitigation; no dated-consolidation claim is ever made). **No CT article
exists for aguinaldo/bono/incentivo/propina or cesantía/doubling** (EVID-299
negative finding). Rejected myths never implemented (R33): no *auxilio de
cesantía*, no employer-side preaviso, no holiday-work 2×, and no 1961
inembargabilidad bracket numerics as implementable values (GOQ-73).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | CT art. 88 (texto según edición conmemorativa 2024, MinTrabajo): "Salario o sueldo es la retribución que el patrono debe pagar al trabajador en virtud del cumplimiento del contrato de trabajo o de la relación de trabajo vigente entre ambos." / "El cálculo de esta remuneración… puede pactarse: a) Por unidad de tiempo (por mes, quincena [sic spacing], semana, día u hora); b) Por unidad de obra (por pieza, tarea, precio alzado o a destajo), y c) Por participación en las utilidades, ventas o cobros que haga el patrono; pero en ningún caso el trabajador deberá asumir los riesgos de pérdidas que tenga el patrono." | Art. 88: salary or wage is the retribution the employer must pay the worker by virtue of the employment contract or prevailing work relationship; the remuneration may be pacted (a) per unit of time (month, fortnight, week, day, hour), (b) per unit of work (piece, task, lump price, piecework), (c) by participation in profits, sales or collections — but in no case may the worker assume the employer's loss risks | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 88 p.55 (EVID-280) |
| LB-002 | CT art. 89 (texto según edición conmemorativa 2024, MinTrabajo): "A trabajo igual, desempeñado en puesto y condiciones de eficiencia y antigüedad dentro de la misma empresa, también iguales, corresponderá salario igual…" / "En las demandas que entablen las trabajadoras relativas a la discriminación salarial por razón de sexo, queda el patrono obligado a demostrar que el trabajo que realiza la demandante es de inferior calidad y valor." | Art. 89: equal work performed in the same position and conditions of equal efficiency and seniority within the same enterprise corresponds to equal salary; in female workers' pay-discrimination claims the employer bears the burden of demonstrating the claimant's work is of inferior quality and value | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 89 p.55 (EVID-280) |
| LB-003 | CT art. 90 (texto según edición conmemorativa 2024, MinTrabajo): "El salario debe pagarse exclusivamente en moneda de curso legal." (+ prohibition of payment in mercadería, vales, fichas…; campesinos may receive "hasta en un treinta por ciento… en alimentos… a precio de costo o menos") | Art. 90: salary must be paid exclusively in legal-tender currency; payment in goods, vouchers, tokens… prohibited; campesino workers of agricultural/livestock operations may receive up to thirty percent of total salary in food and analogous articles supplied at cost price or less | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 90 pp.55-56 (EVID-281) |
| LB-004 | CT art. 92 (texto según edición conmemorativa 2024, MinTrabajo): "…sin que dicho plazo pueda ser mayor de una quincena para los trabajadores manuales, ni de un mes para los trabajadores intelectuales y los servicios domésticos." + participation pay: "se debe señalar una suma quincenal o mensual… La liquidación definitiva se debe hacer por lo menos cada año." | Art. 92: the pact payment term may not exceed one fortnight for manual workers nor one month for intellectual workers and domestic service; participation pay requires a fortnightly or monthly advance sum with definitive liquidation at least annually | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 92 p.56 (EVID-281) |
| LB-005 | CT art. 93 (texto según edición conmemorativa 2024, MinTrabajo): "…para el cómputo de todas las indemnizaciones o prestaciones que otorga el presente Código, se entiende por salario completo el devengado durante las jornadas ordinaria y extraordinaria o el equivalente de las mismas…" | Art. 93: for the computation of ALL indemnities or benefits this Code grants, "salario completo" (complete salary) = earnings accrued during the ordinary and extraordinary workdays, or their equivalent (unit-of-work pay); the salary must be liquidated complete each pay period; ¶2: where in-kind salary is legally pactable without stipulated proportion, a 30% in-kind share is presumed | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 93 p.56 (EVID-281) |
| LB-006 | CT arts. 96-97 (texto según edición conmemorativa 2024, MinTrabajo), art. 96: "Se declaran inembargables: a) Los salarios mínimos y los que sin serlo no excedan de treinta quetzales al mes; b) El no venta [sic] por ciento de los salarios mayores de treinta quetzales o más, pero menores de cien quetzales al mes; c) El ochenta y cinco por ciento de los salarios de cien quetzales o más, pero menores de doscientos quetzales al mes; d) El ochenta por ciento de los salarios de doscientos quetzales o más, pero menores de trescientos quetzales al mes; y e) El sesenta y cinco por ciento de los salarios mensuales de trescientos quetzales o más." / art. 97: "No obstante lo dispuesto en el artículo anterior, son embargables toda clase de salarios, hasta en un cincuenta por ciento, para satisfacer obligaciones de pagar alimentos presentes o los que se deben desde los seis meses anteriores al embargo." / "Los embargos por alimentos tendrán prioridad… en ningún caso podrán hacerse efectivos dos embargos simultáneamente… sólo podrá embargarse hasta el diez por ciento más para satisfacer las demás obligaciones." | Arts. 96-97: unembargable — minimum wages and sub-Q30 salaries (fully); 90%/85%/80%/65% of salaries by the Q30-100/100-200/200-300/≥300 monthly brackets (1961-scale numerics — GOQ-73: NEVER implementable values, structure only); alimony exception: any salary attachable up to 50% for present alimony or alimony owed from the six months before the garnishment; alimony garnishments have priority, two simultaneous garnishments may never be made effective, and only up to 10% more may be garnished for other obligations | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Arts. 96-97 p.57 (EVID-282) |
| LB-007 | CT art. 98 (texto según edición conmemorativa 2024, MinTrabajo): "…se declaran también inembargables los instrumentos, herramientas o útiles del trabajador que sean indispensables para ejercer su profesión u oficio…" | Art. 98: as additional salary protection, the worker's instruments, tools and implements indispensable for exercising the profession or trade are also unembargable (except debts from their own credit purchase) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 98 p.57 (EVID-283) |
| LB-008 | CT art. 99 (texto según edición conmemorativa 2024, MinTrabajo): "Los anticipos que haga el patrono al trabajador por cuenta de salarios en ningún caso deben devengar intereses." + debts "se deben amortizar hasta su extinción, en un mínimo de cinco períodos de pago, excepto cuando el trabajador, voluntariamente, pague en un plazo más corto." | Art. 99: salary advances must in no case bear interest; worker debts (from advances, excess payments, work-related civil liabilities) amortize over a MINIMUM of five pay periods unless the worker voluntarily pays faster; other debts amortize/compensate only in the proportion the respective salaries are garnishable; definitive liquidation permitted at contract end | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 99 pp.57-58 (EVID-283) |
| LB-009 | CT art. 101 (texto según edición conmemorativa 2024, MinTrabajo): wage credits and termination indemnizations "gozan en virtud de su carácter alimenticio de los siguientes privilegios…: a) Pueden ser cobrados por la vía especial que prevé el artículo 426; y b) Tienen carácter de créditos de primera clase… gozan de preferencia absoluta sobre cualesquiera otros, excepto…" / "Los privilegios… sólo comprenden un importe… equivalente a seis meses de salarios o menos." | Art. 101: unpaid wage credits and money termination indemnizations, by their alimentary character and once recognized by the labor courts, are (a) collectible via the art. 426 special path and (b) first-class credits with absolute preference over any others (except the Código Civil first-class exceptions); the privilege covers only up to six months of wages | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 101 p.58 (EVID-283) |
| LB-010 | CT art. 102 (texto según edición conmemorativa 2024, MinTrabajo): "Todo patrono que ocupe permanentemente a diez o más trabajadores, debe llevar un libro de salarios autorizado y sellado por el Departamento Administrativo del Ministerio de Trabajo y Previsión Social…" / "Todo patrono que ocupe permanentemente a tres o más trabajadores, sin llegar al límite de diez, debe llevar planillas de conformidad con los modelos que adopte el Instituto Guatemalteco de Seguridad Social." | Art. 102: employers permanently occupying ten or more workers keep a salary ledger authorized and stamped by MinTrabajo's administrative department; employers with three or more but fewer than ten keep IGSS-model planillas | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 102 p.59 (EVID-284) |
| LB-011 | CT art. 61 a) (texto según edición conmemorativa 2024, MinTrabajo) 1.: annual report to MinTrabajo within "el improrrogable plazo de los dos primeros meses de cada año" containing "Egresos totales que hayan tenido por concepto de salarios, bonificaciones y cualquier otra prestación económica durante el año anterior, con la debida separación de las salidas por jornadas ordinarias y extraordinarias." / 2.: names, ages, "número de días que haya trabajado cada uno y el salario que individualmente les haya correspondido durante dicho año." | Art. 61 a): annual employer report to MinTrabajo within the non-extendable first two months of each year: total prior-year outflows for salaries, bonificaciones and any other economic benefit with ordinary/extraordinary separation; per-worker names, ages, nationality, sex, occupation, days worked and individually corresponding salary | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 61 a) pp.37-38 (EVID-284) |
| LB-012 | CT arts. 259-264 (texto según edición conmemorativa 2024, MinTrabajo): art. 259: "Los derechos de los patronos para despedir justificadamente… o para disciplinar sus faltas, prescriben en veinte días hábiles…" / art. 260: "Los derechos de los trabajadores para reclamar, contra su patrono en los casos de despido…, prescriben en el plazo de treinta días hábiles contados a partir de la terminación del contrato…" / art. 261: worker's justa-cause termination right "prescriben en el término de veinte días hábiles" from the cause / art. 262: patrono claims vs unjustified quits "treinta días hábiles" / art. 263: rights from contracts, pactos, convenios, reglamentos "prescriben en el término de cuatro meses, contados desde la fecha de terminación de dichos contratos" / art. 264: "todos los derechos que provengan directamente de ese [sic] Código… o de las demás leyes de Trabajo y Previsión Social, prescriben en el término de dos años. Este plazo corre desde el acaecimiento del hecho u omisión respectivos." | Prescription ladder: 20 días hábiles — employer justified-dismissal/discipline rights (from the cause or knowledge) and worker justa-cause/indirect-termination rights (from the employer's cause); 30 días hábiles — worker dismissal/discipline claims (from termination or correction) and employer claims against unjustified quits (from separation); 4 months — rights from contracts, collective pacts, general-application convenios or interior reglamentos (from contract termination); 2 years — all rights directly derived from the Code, its reglamentos or the other labor and social-security laws (from the event or omission) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Arts. 259-264 pp.110-111 (EVID-297) |
| LB-013 | CT arts. 265-268 (texto según edición conmemorativa 2024, MinTrabajo): art. 265: prescription does not run against under-14s/incapables without legal representative / art. 266: interruption by "demanda o gestión ante autoridad competente", express/tacit recognition (incl. partial payment), or force majeure / art. 267: interruption vs one solidary debtor interrupts vs all / art. 268: interruption voids all time run before it | Tolling and interruption: the clock does not run against minors under 14 and incapables lacking a legal representative; interruption events — demand/proceeding before a competent authority, express or tacit recognition of the right (including any partial payment or performance in any form), force majeure; solidary-debtor extension; interruption resets all elapsed time | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Arts. 265-268 pp.111-112 (EVID-297) |
| LB-014 | CT art. 5 (texto según edición conmemorativa 2024, MinTrabajo): "Intermediario es toda persona que contrata en nombre propio los servicios de uno o más trabajadores para que ejecuten algún trabajo en beneficio de un patrono. Este último queda obligado solidariamente por la gestión de aquel para con el o los trabajadores…" / "No tiene carácter de intermediario y sí de patrono, el que se encargue por contrato, de trabajos que ejecute con equipos o capitales propios." | Art. 5: an intermediary contracts in his own name the services of one or more workers to execute work for the benefit of an employer — that beneficiary employer is solidarily (jointly and severally) liable for the intermediary's management toward the workers; whoever undertakes works with his own equipment or capital is not an intermediary but an employer himself | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 5 pp.16-17 (EVID-268) |
| LB-015 | CT arts. 17 y 20 (texto según edición conmemorativa 2024, MinTrabajo), art. 17: "…se debe tomar en cuenta, fundamentalmente, el Interés de los trabajadores en armonía con la conveniencia social." / art. 20: contrato obliga "a la observancia de las obligaciones y derechos que este Código o los convenios internacionales ratificados por Guatemala, determinen… cuando consignen beneficios superiores para los trabajadores que los que este Código crea" | Art. 17: labor norms applied with fundamental regard to the workers' interest in harmony with social convenience; art. 20: contracts bind to the obligations and rights determined by the Code and by Guatemala-ratified international (ILO) conventions whenever the latter consign superior worker benefits | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Art. 17 p.21; art. 20 p.23 (EVID-268) |
| LB-016 | NEGATIVE FINDING, CT whole text (texto según edición conmemorativa 2024, MinTrabajo): (no verbatim possible — terms absent; nearest: art. 61 a) 1. "…por concepto de salarios, bonificaciones y cualquier otra prestación económica…") | The CT as printed contains ZERO aguinaldo, bono/bonificación anual, incentivo and propina provisions (exhaustive search: 0 hits); those wage complements are governed exclusively by their specific laws (bono 14 = D-42-92; incentivo = D-78-89; December aguinaldo statutes absent from corpus); the CT contributes only the art. 93 salario-completo integration basis and the art. 89 equal-salary rule; "bonificaciones" appears in the CT only as the art. 61 a) annual-report category | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Whole text (exhaustive search: 0 hits); art. 61 a) 1. pp.37-38 (EVID-299) |
| LB-017 | CT arts. 422, 423 y 426 (texto según edición conmemorativa 2024, MinTrabajo), art. 422: "Las sanciones o multas que se impongan a los infractores deben hacerse efectivas inmediatamente…" / art. 423: insolvency → "prisión simple" / art. 426: "…el juez de oficio y dentro del plazo de tres días de notificada la ejecutoria o de aceptada la obligación, practicará la liquidación… Si dentro del tercero día… el obligado no hiciere efectivo el pago el juez ordenará… el embargo…" | Enforcement: imposed fines are effective immediately once firm; insolvency converts the sanction to simple prison per the Código Penal; recognized labor prestaciones execute via the art. 426 special path — ex-oficio liquidation within 3 days of the enforceable ruling or accepted obligation, then embargo on non-payment (ties the art. 101 privilege); the faltas chapter (arts. 269 ff.) defines infractions incl. violations of ratified ILO conventions and collective pacts — no workable administrative fine scale is printed (values external) | `gt/sources/32_Codigo_Trabajo_D1441.pdf` | Arts. 269+ p.112 ff. (skim); arts. 422-423 p.173; art. 426 p.175 (EVID-298) |

Dead print — never implementable as values (LB note, not an FR): the Art. 96
inembargabilidad bracket amounts (Q30/Q100/Q200/Q300 monthly) are 1961-scale
quetzals with no updating stamp — structure only; GOQ-73 bans the numerics
(OQ-001). Edition vintage (R44/GOQ-70/71): the 32_ source is the MinTrabajo
commemorative 2024 print with an indeterminate consolidation cutoff — cited
only with the edition qualifier, never as a dated consolidation.

## 3. Functional Requirements

### 3.1 Salary concept and pay-form taxonomy (CT Arts. 88-89)

- **GT-PAY-FR-001:** The system shall model *salario o sueldo* (salary or
  wage) as the *retribución* (remuneration) the *patrono* (employer) must
  pay the worker by virtue of the employment contract or the prevailing work
  relationship between them — and, save legal exceptions, every service
  rendered by a worker to the employer shall be remunerated.
  (LB-001; EVID-280)
- **GT-PAY-FR-002:** The system shall classify every worker's remuneration
  pact into the Art. 88 pay-basis taxonomy — (a) *por unidad de tiempo*
  (unit of time: month, quincena, week, day or hour), (b) *por unidad de
  obra* (unit of work: pieza, tarea, precio alzado or destajo), (c) *por
  participación* (participation in the employer's profits, sales or
  collections) — including contracts mixing bases (mixed contracts carry
  each basis on its own pact lines); for unit-of-work pay, Code averages use
  the ordinary+extraordinary equivalence of Art. 93 (FR-005). The pay-form
  choice shall never make remuneration less favorable: the no-disadvantage-
  by-form kin rule (CT art. 103, piecework/task/lump/destajo workers shall
  not come out disadvantaged by pay form) is owned by S-GT3 file
  `02_working-time-overtime.md` / `03_minimum-wage.md` (FR ids to be
  assigned at their dispatch) and consumed by cross-reference — never
  re-derived here. (LB-001; LB-005; EVID-280, EVID-281)
- **GT-PAY-FR-003:** The system shall implement the no-loss-risk rule:
  *en ningún caso el trabajador deberá asumir los riesgos de pérdidas que
  tenga el patrono* (in no case may the worker assume the employer's loss
  risks) — a participación or unidad-de-obra remuneration shall never be
  reduced by employer losses, and no salary rule may shift patrono loss risk
  onto the worker. (LB-001; EVID-280)
- **GT-PAY-FR-004:** The system shall provide an equal-salary audit surface
  implementing Art. 89: *a trabajo igual* (equal work), performed in the
  same *puesto* (position) and conditions of equal efficiency and
  *antigüedad* (seniority) within the same enterprise, corresponds equal
  salary (comprising payments made in exchange for ordinary labor); for
  *discriminación salarial por razón de sexo* (sex-based pay discrimination)
  claims by female workers, the record shall carry the reversed-burden
  marker — the patrono is obligated to demonstrate that the claimant's work
  is of inferior quality and value. Implemented as analytics metadata over
  salary data; no payslip computation is derived from it.
  (LB-002; EVID-280)

### 3.2 Salario completo — the integration basis (CT Art. 93)

- **GT-PAY-FR-005:** The system shall compute and stamp *salario completo*
  (complete salary) as THE single integration basis for the computation of
  ALL *indemnizaciones o prestaciones* (indemnities or statutory benefits)
  the Código de Trabajo grants: earnings accrued during the *jornadas
  ordinaria y extraordinaria* (ordinary and extraordinary workdays) — or
  their equivalent for unit-of-work pay (Art. 88 b) equivalence) — i.e.
  ordinary + extraordinary components, and shall liquidate the salary
  complete at each pay period. Every consuming computation of this wave
  references this FR id and never re-derives the basis: vacaciones prepaid
  averages (3-month agro / 12-month others, ordinary+extraordinary) and
  maternidad bases = S-GT3 file `05_vacaciones-maternidad.md`; indemnización
  6-month salario-completo average = `06_contracts-termination.md`; IGSS
  contributory-base interfaces = `07_igss-contributions.md` (FR ids to be
  assigned at their dispatch). R36 tension recorded: complementary bonus
  laws use NARROWER bases — bono 14 is 100% of one month's ORDINARY salary
  (D-42-92; R36) — while Art. 93 salario completo governs Code-derived
  prestaciones only; the per-concept base selection is owned by
  `04_statutory-bonuses.md` (FR ids to be assigned at its dispatch).
  (LB-005; EVID-281)

### 3.3 Payment form, cadence and in-kind component (CT Arts. 90, 92, 93)

- **GT-PAY-FR-006:** The system shall enforce the legal-currency rule: the
  salary must be paid exclusively in *moneda de curso legal* (legal-tender
  currency); payment totally or partially in mercadería (goods), vales,
  fichas, cupones or any other representative sign substituted for currency
  is prohibited — computation tokens (vales/fichas as mere salary-counting
  media) are admissible only when the employer exchanges their exact
  equivalent into legal currency at each pay-period end.
  (LB-003; EVID-281)
- **GT-PAY-FR-007:** The system shall enforce the in-kind ceiling:
  *trabajadores campesinos* (peasant workers) of agricultural or livestock
  operations may receive at most **30%** of total salary in food and
  analogous articles destined to the worker's or dependants' immediate
  personal consumption, supplied *a precio de costo o menos* (at cost price
  or less); where in-kind salary is legally pactable and no proportion was
  stipulated, a 30% in-kind share of total salary is presumed (Art. 93 ¶2).
  Any in-kind component above the 30% ceiling, or supplied above cost
  price, shall be rejected. (LB-003; LB-005; EVID-281)
- **GT-PAY-FR-008:** The system shall enforce the payment-cadence ceilings
  keyed on worker class: the pact payment term may not be greater than **one
  quincena** for *trabajadores manuales* (manual workers), nor **one month**
  for *trabajadores intelectuales* (intellectual workers) and *servicios
  domésticos* (domestic service); payroll-period configurations exceeding
  the worker-class ceiling shall be rejected. (LB-004; EVID-281)
- **GT-PAY-FR-009:** For *participación* pay (profits, sales or
  collections), the system shall model the mandatory rhythm: a quincenal or
  mensual advance sum proportionate to the worker's needs and the probable
  participation, plus a definitive liquidation at least once each year
  (*por lo menos cada año*). (LB-004; EVID-281)

### 3.4 Inembargabilidad — garnishment protection (CT Arts. 96-98)

- **GT-PAY-FR-010:** STRUCTURE-ONLY requirement: the system shall model the
  garnishment-protection ladder as structure — (a) a fully-protected floor:
  *salarios mínimos* (minimum-wage) earners are fully unembargable, and
  salaries below the statutory floor bracket likewise; (b) above the floor,
  percentage tiers protecting a share of salary by monthly-salary bracket —
  with ALL threshold data EXTERNALLY sourced (dated rows with
  valid_from/provenance per D15/D16). The printed Art. 96 bracket numerics
  (Q30/Q100/Q200/Q300 monthly — 1961-scale, unindexed) are BANNED as
  implementable values: no numeric bracket from this edition shall be
  seeded, and modern thresholds enter only when an external instrument
  supplies them (GOQ-73). (LB-006; EVID-282; GOQ-73 → OQ-001)
- **GT-PAY-FR-011:** The alimony carve-out shall be implemented with its
  printed percentages: any class of salary is attachable up to **50%** to
  satisfy *alimentos presentes* (present alimony) or alimony owed from the
  six months before the embargo (garnishment); alimony garnishments take
  priority over all others; two simultaneous garnishments may never be made
  effective; and only after the maximum alimony proportion is covered may up
  to **10% more** be garnished for the other obligations — the payslip
  deduction engine shall apply, in order: the unembargable-part protection,
  the alimony 50% priority cap, then the +10% secondary cap.
  (LB-006; EVID-282)
- **GT-PAY-FR-012:** The system shall flag as unembargable the worker's
  *instrumentos, herramientas o útiles* (instruments, tools and implements)
  indispensable for exercising the profession or trade — save debts arising
  solely from their own credit purchase (attachment metadata; no payslip
  computation attached). (LB-007; EVID-283)

### 3.5 Advances and worker-debt recovery (CT Art. 99)

- **GT-PAY-FR-013:** Salary advances (*anticipos* by the patrono on account
  of salaries) shall bear NO interest in any case (*en ningún caso deben
  devengar intereses*) — the Art. 99 prohibition is the only interest rule
  in the entire Code, and no interest, mora charge or financing cost shall
  ever be generated on a salary advance or labor debt (negative finding: no
  mora-interest-on-labor-debts article exists; delay compensation, where it
  exists at all, is the `06_contracts-termination.md` salarios-caídos
  regime, never interest). (LB-008; EVID-283)
- **GT-PAY-FR-014:** Recovery of worker debts to the employer — from salary
  advances, excess payments or work-related civil liabilities — shall
  amortize until extinction over a MINIMUM of **five pay periods** (*un
  mínimo de cinco períodos de pago*), except when the worker voluntarily
  pays in a shorter term; at contract end the employer may make the
  definitive liquidation that proceeds. (LB-008; EVID-283)
- **GT-PAY-FR-015:** All OTHER worker debts to the patrono or to his
  associates, family or dependants (contracted during or before the
  contract) may be amortized or compensated ONLY in the proportion in which
  the respective salaries are garnishable — the FR-010/FR-011 protection
  ladder gates every non-advance deduction. (LB-008; LB-006; EVID-283,
  EVID-282)

### 3.6 Privileged wage credits (CT Art. 101)

- **GT-PAY-FR-016:** Unpaid salary credits and money termination
  indemnizations shall carry privileged-credit metadata by virtue of their
  *carácter alimenticio* (alimentary character): once recognized by the
  labor courts, they (a) are collectible via the Art. 426 special execution
  path (ex-oficio 3-day liquidation → embargo) and (b) are *créditos de
  primera clase* (first-class credits) in universal proceedings, with
  absolute preference over any others except the Código Civil first-class
  exceptions; the privilege covers only an amount equivalent to **six
  months of wages or less**. Metadata for settlement ordering; no payslip
  computation attached. (LB-009; LB-017; EVID-283, EVID-298)

### 3.7 Salary books and the annual MinTrabajo report (CT Arts. 102, 61 a)

- **GT-PAY-FR-017:** Statutory payroll-record mode shall key on permanent
  headcount: employers permanently occupying **ten or more** workers shall
  keep a *libro de salarios* (salary ledger) authorized and stamped by the
  Departamento Administrativo del Ministerio de Trabajo y Previsión Social
  (MinTrabajo supplies printing models/norms); the ledger shall keep
  extraordinary-work payments separated from ordinary (feeds FR-019 and the
  FR-005 ordinary/extraordinary tagging). (LB-010; EVID-284)
- **GT-PAY-FR-018:** Employers permanently occupying **three or more
  workers without reaching ten** shall keep *planillas* (payroll sheets) per
  the models adopted by the Instituto Guatemalteco de Seguridad Social
  (IGSS) — the planilla MECHANICS are owned by S-GT3 file
  `07_igss-contributions.md` (FR ids to be assigned at its dispatch); this
  FR owns only the headcount-triggered mode selection. Taxation interface
  (consumed by id): salaries off the IGSS planilla are employer-non-
  deductible — GT-TAX-FR-146. (LB-010; EVID-284)
- **GT-PAY-FR-019:** The annual employer report to MinTrabajo shall be
  generated within the *improrrogable* (non-extendable) term of the **first
  two months of each year**, containing: (1) total prior-year outflows for
  salaries, *bonificaciones* (bonuses — a reporting category only, see
  FR-024) and any other economic benefit, with due separation of ordinary
  and extraordinary jornada outflows; and (2) per-worker name and surname,
  approximate age, nationality, sex, occupation, number of days worked and
  the salary individually corresponding during that year. (LB-011; EVID-284)

### 3.8 Prescription — money-claims ladder (CT Arts. 259-268)

- **GT-PAY-FR-020:** The labor money-claims clock table shall be stored as
  clock-rule data: **20 días hábiles** — employer justified-dismissal and
  discipline rights (Art. 259, from the cause or knowledge of the facts)
  and worker justa-cause / indirect-termination rights (Art. 261, from the
  patrono's cause); **30 días hábiles** — worker dismissal and
  disciplinary-correction claims (Art. 260, from contract termination or
  imposition) and employer claims against unjustified quits (Art. 262, from
  separation); **4 months** — rights from contracts, *pactos colectivos*
  (collective agreements), *convenios* de aplicación general or interior
  reglamentos (Art. 263, from contract termination); **2 years** — all
  rights directly derived from the Code, its reglamentos or the other labor
  and social-security laws (Art. 264, from the event or omission).
  (LB-012; EVID-297)
- **GT-PAY-FR-021:** Prescription computation: the clock does not run
  against minors under 14 and incapables without a legal representative
  (Art. 265); it is interrupted by (a) *demanda o gestión ante autoridad
  competente* (demand or proceeding before a competent authority), (b)
  express or tacit recognition of the right — INCLUDING any partial payment
  or performance of the obligation in any form (Art. 266 b)), and (c) force
  majeure; interruption against one solidary debtor interrupts against all
  (Art. 267) and voids all time run before it (Art. 268). Any payroll
  payment event against an aging labor debt shall emit the partial-payment
  interruption record (odoo surface; saas recomputes the clock).
  (LB-013; EVID-297)

### 3.9 Solidaridad and protective principles (CT Arts. 5, 17, 20)

- **GT-PAY-FR-022:** The multi-employer liability model shall implement
  Art. 5 solidarity: an *intermediario* (intermediary) is one who contracts
  in his own name the services of one or more workers to execute work for
  the benefit of a patrono — that beneficiary employer is *obligado
  solidariamente* (jointly and severally liable) for the intermediary's
  management toward those workers; by contrast, whoever undertakes by
  contract works executed with his OWN equipment or capital has the
  character of patrono, not intermediario. Payroll liability postings for
  outsourced/subcontracted workers shall carry the solidarity flag (true
  employer + beneficiary employer). (LB-014; EVID-268)
- **GT-PAY-FR-023:** Interpretive metadata (no computation): labor norms
  are applied taking fundamentally into account the *Interés de los
  trabajadores* (workers' interest) in harmony with social convenience
  (Art. 17), and contracts bind to the obligations and rights determined by
  the Code AND by ratified international (ILO) conventions whenever the
  latter consign *beneficios superiores* (superior benefits) for workers
  (Art. 20) — the pro-operario reading bias of this wave.
  (LB-015; EVID-268)

### 3.10 Negative finding and enforcement pointers (EVID-299, EVID-298)

- **GT-PAY-FR-024:** NEGATIVE FR (citation guard): the CT (as printed in
  this edition) contains ZERO aguinaldo, bono/bonificación anual, incentivo
  or propina provisions — no payroll rule for those concepts may cite the
  Código de Trabajo; their regimes live exclusively in their specific
  decrees, owned by S-GT3 file `04_statutory-bonuses.md` (FR ids to be
  assigned at their dispatch; the December aguinaldo statutes are absent
  from the corpus — never invented). The only CT occurrence of
  "bonificaciones" is the Art. 61 a) annual-report category (FR-019). The
  CT's sole contributions to the complementary-law bases are the Art. 93
  salario completo (FR-005) and the Art. 89 equal-salary rule (FR-004).
  (LB-016; LB-011; EVID-299, EVID-284)
- **GT-PAY-FR-025:** Enforcement hooks, POINTER ONLY: the CT faltas chapter
  (Arts. 269 ff.) defines labor infractions including violations of
  ratified ILO conventions and collective pacts; imposed fines are
  effective immediately (Art. 422), insolvency converts the sanction into
  simple prison (Art. 423), and recognized prestaciones execute via the
  Art. 426 special path (ex-oficio liquidation within 3 days → embargo).
  NO sanction value is defined or derived in this file — sanction amounts
  are owned by `gt/requirements/taxation/06_ct-procedures.md` via the
  Código Tributario art. 94 family cross-ref (GT-TAX-FR-140/146 hooks),
  never the CT labor text. (LB-017; EVID-298)

## 4. Data Model

Layer semantics: payroll is Odoo-native for computation and books; clock /
threshold / privilege data rows are `shared` (both sides resolve the same
row); prescription computation is `saas` with odoo surfaces (events emitted
from payroll). No dated values live in this file except via the external-
threshold regime below; the Art. 96 bracket NUMERICS are never seeded
(GOQ-73). Dated rows follow D15/D16: valid_from/valid_to + instrument
provenance; snapshot-on-write.

**Pay-basis, cadence & equal-salary metadata:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | gt_pay_pay_basis | select | tiempo · obra · participacion · mixto | FR-002 |
| hr.contract | gt_pay_pay_basis_detail | char | tiempo: mes/quincena/semana/día/hora; obra: pieza/tarea/precio_alzado/destajo; participación: utilidades/ventas/cobros | FR-002 |
| hr.contract | gt_pay_worker_class | select | manual · intellectual_domestic | FR-008 |
| hr.contract (participacion) | gt_pay_participacion_advance_freq / gt_pay_liquidation_floor | selection / integer | quincenal · mensual / annual (12m floor) | FR-009 |
| hr.payslip line | gt_pay_salary_component | select | ordinaria · extraordinaria · none (non-jornada items) | FR-005 |
| hr.payslip (aggregator) | gt_pay_salario_completo_period | monetary (computed) | sum of ordinaria+extraordinaria lines; read-only base consumed by files 04-07 | FR-005 |
| hr.payroll (analysis) | equal-salary audit view | view | same-puesto/efficiency/antigüedad cohorts; female-claim burden-shift marker | FR-004 |

**Payment form & in-kind:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.payslip (payment method) | gt_pay_legal_currency_only | constraint | reject mercadería/vales/fichas payment forms; token exception only with period-end exact exchange | FR-006 |
| hr.payslip line (in-kind) | gt_pay_inkind_pct / gt_pay_cost_price_or_less | monetary % / boolean | ≤ 0.30 of total salary (campesinos agro/ganadero); cost-price-or-less supply flag; unstipulated → 30% presumed | FR-007 |

**Garnishment ladder (structure-only) & advances:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.garnishment.tier | protected_pct / bracket_floor / bracket_ceiling / valid_from / provenance | decimal / dated rows | fully-protected floor (minimum-wage carve-out) + percentage tiers; thresholds EXTERNAL dated rows only — NO Q30/Q100/Q200/Q300 seeds (GOQ-73) | FR-010 |
| l10n_gt.pay.garnishment.rule | alimony_pct / secondary_pct / single_embargo | decimal / decimal / boolean | 0.50 alimony priority (present + 6-month arrears); +0.10 other obligations after the alimony cap; no two simultaneous embargoes | FR-011 |
| hr.employee (assets) | gt_pay_tools_unembargable | boolean | indispensable instruments/tools/implements (credit-purchase-debt exception) | FR-012 |
| hr.loan (salary advance) | interest (hard-coded none) / amortization_periods_min / voluntary_early_pay | constraint / integer / boolean | no interest ever; ≥5 pay periods; voluntary shorter term allowed; contract-end definitive liquidation | FR-013, FR-014 |
| hr.payslip (other-debt deduction) | gt_pay_embargable_proportion_gated | boolean | non-advance debts only in garnishable proportion | FR-015 |

**Privilege, books & report:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (payroll journal) | gt_pay_privileged_credit | tag | first_class_art101 · privilege_cap_6m_wages · via_especial_art426 | FR-016 |
| hr.payroll (company config) | gt_pay_book_mode | computed select | libro_salarios (≥10 permanent workers) · igss_planillas (3-9); mechanics owned by file 07 | FR-017, FR-018 |
| l10n_gt.pay.mintrabajo.annual.report | data set | report | prior-year totals with ordinary/extraordinary separation + per-worker days/salary; window: first 2 months of the year | FR-019 |

**Prescription, solidarity & guards:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pay.prescription.clock | claim_type / term / unit / habiles / anchor_event | char / int / selection / boolean / char | employer_justified_dismissal 20 días hábiles; worker_dismissal_claim 30 días hábiles; worker_justa_causa 20 días hábiles; employer_unjustified_quit 30 días hábiles; contractual_prestaciones 4 meses (from termination); general_statutory 2 años (from event/omission) | FR-020 |
| l10n_gt.pay.prescription.event | type / tolling / source | selection / boolean / ref | filing · recognition · partial_payment (any payroll payment move) · force_majeure; tolling: under-14 / incapable without representative | FR-021 |
| hr.contract (outsourcing) | gt_pay_intermediario / gt_pay_beneficiary_patrono | flags | solidarity pair (true employer + beneficiary) | FR-022 |
| l10n_gt.pay.guard | negative rows | char | aguinaldo · bono · incentivo · propina = NOT_IN_CT → cite 40_/41_ decrees only (file 04) | FR-024 |
| l10n_gt.pay.enforcement.pointer | note row | char | faltas arts. 269 ff.; arts. 422/423/426 execution path; sanction values external (taxation/06, Código Tributario art. 94 family) | FR-025 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and computation surface in the LGPL client; `saas` =
authoritative computation/validation in the Elixir core; `shared` =
contract items both sides must honor identically. Payroll-wave defaults
(binding): clock/threshold/privilege dated data = `shared`; payslip
salary-category computation + salary books = `odoo`; prescription
computation = `saas` with odoo surfaces. Model names stable across Odoo
17/18/19/20; no version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | hr.contract / hr.salary.rule | salary-structure anchor | Retribución-of-every-service principle; legal exceptions only |
| FR-002 | odoo | hr.contract | gt_pay_pay_basis (+detail) | Taxonomy incl. mixto; art. 103 kin rule consumed from files 02/03 |
| FR-003 | odoo | hr.salary.rule (guard) | no-loss-risk guard | No rule may net patrono losses against worker lines |
| FR-004 | odoo | hr.payroll (analysis view) | equal-salary audit | Analytics metadata; burden-shift marker; no payslip rule |
| FR-005 | odoo | hr.salary.rule / hr.payslip.line | gt_pay_salary_component + gt_pay_salario_completo_period | THE integration basis; consumers files 04-07 reference by FR id |
| FR-006 | odoo | hr.payslip (payment method) | legal-currency constraint | Token exception: exact period-end exchange |
| FR-007 | odoo | hr.payslip line | gt_pay_inkind_pct / cost-price flag | ≤30% campesinos; 30% presumption when unstipulated |
| FR-008 | odoo | hr.contract + payroll period config | gt_pay_worker_class + cadence validator | ≤quincena manual / ≤mes intellectual+domestic |
| FR-009 | odoo | hr.contract (participacion) | advance freq + annual liquidation floor | suma quincenal o mensual + liquidación ≥anual |
| FR-010 | shared | — (config data §4) | ladder tier rows, EXTERNAL thresholds | GOQ-73: numerics banned; structure only; both sides resolve same rows |
| FR-011 | odoo | hr.payslip (garnishment deductions) | 0.50 alimony priority + 0.10 secondary | Order: unembargable part → alimony cap → +10% |
| FR-012 | odoo | hr.employee / asset register | gt_pay_tools_unembargable | Metadata flag; credit-purchase exception |
| FR-013 | odoo | hr.loan | interest forbidden (hard) | Only interest rule in the Code is the prohibition |
| FR-014 | odoo | hr.loan | amortization ≥5 periods | Voluntary shorter term; contract-end liquidation |
| FR-015 | odoo | hr.payslip (deduction gate) | embargable-proportion gating | Ladder (FR-010/011) gates non-advance debts |
| FR-016 | shared | — (metadata contract §4) | first-class tag + 6-months cap data | Settlement-ordering consumers read the same rows |
| FR-017 | odoo | hr.payroll (book mode) | libro de salarios ≥10 | MinTrabajo-authorized ledger; ordinary/extra separation |
| FR-018 | odoo | hr.payroll (book mode) | IGSS planillas 3-9 | Mechanics = file 07; GT-TAX-FR-146 interface (no planilla → non-deductible) |
| FR-019 | odoo | l10n_gt.pay.mintrabajo.annual.report | report data set | First-2-months window; ordinary/extra split; per-worker days+salary |
| FR-020 | shared | — (config data §4) | prescription clock table | 20dh/30dh/4m/2y with anchors; both sides resolve same rows |
| FR-021 | saas | — (odoo emits events) | interruption event intake | Partial payment from any payroll move; odoo surfaces, saas recomputes; tolling under-14/incapable |
| FR-022 | odoo | hr.contract / res.partner | solidarity flag pair | Intermediario + beneficiary patrono jointly liable |
| FR-023 | odoo | hr.contract (metadata note) | pro-operario / ILO layering note | Interpretive only; no computation |
| FR-024 | shared | — (guard rows §4) | NOT_IN_CT negative rows | Both sides' catalogs carry the guard; bonuses cite 40_/41_ only |
| FR-025 | shared | — (pointer row §4) | enforcement pointer | Justification: procedural pointer honored identically by both sides; no data or computation either side may diverge on — sanction values external (taxation/06) |

## 6. Acceptance Criteria

- **AC-001:** Given a worker whose contract stipulates a mixed pact (60%
unit-of-time + 40% participación), when the pay basis is classified, then
the contract carries gt_pay_pay_basis = mixto with both basis details, and
the participación share follows the FR-009 advance+annual-liquidation
rhythm. (FR-002, FR-009)
- **AC-002:** Given a month in which the employer recorded losses and a
destajo/participación worker with agreed remuneration of Q2,000, when the
payslip computes, then the worker's remuneration is not reduced by the
patrono's losses (no loss-risk shift). (FR-003)
- **AC-003:** Given two workers in the same enterprise, same puesto, equal
efficiency and antigüedad, with salaries Q3,000 and Q4,000, when the
equal-salary audit runs, then the pair surfaces as a comparator gap; given
a female worker's pay-discrimination claim flag on the pair, then the
record carries the reversed-burden marker obligating the patrono to prove
inferior quality/value. (FR-004)
- **AC-004:** Given a worker with ordinary-jornada earnings of Q3,000 and
extraordinary-jornada (overtime) earnings of Q500 in the period, when the
salario completo is computed, then gt_pay_salario_completo_period = Q3,500
(ordinary + extraordinary only) and every Code indemnización/prestación
consumer (files 05/06) reads this aggregated value — never a re-derived
base; given the same worker's bono 14 computation, then its base selection
follows file 04's ordinary-salary rule (R36 tension), not this FR.
  (FR-005)
- **AC-005:** Given a manual worker whose payroll period is configured at
20 days, when validated, then the configuration is rejected (ceiling: one
quincena); given an intellectual worker at one month, then it is accepted.
  (FR-008)
- **AC-006:** Given a campesino worker of an agro/ganadero operation with
total salary Q2,000 receiving Q700 in food, when the payslip validates,
then the in-kind component is rejected (>30%); given Q500 of food supplied
at cost price, then it is accepted as the in-kind share (≤30%, cost-or-
less); given a legally-pactable in-kind salary with no stipulated
proportion, then a 30% in-kind share is presumed. (FR-006, FR-007)
- **AC-007:** Given any attempt to seed garnishment tiers with the printed
Art. 96 numerics (Q30/Q100/Q200/Q300 monthly), when the ladder registry is
inspected, then no such numeric row exists (GOQ-73: structure only,
thresholds external); given a minimum-wage earner, then the salary is fully
unembargable save the FR-011 alimony carve-out. (FR-010)
- **AC-008:** Given a Q4,000 salary with an alimony embargo and a second
non-alimony embargo, when deductions compute, then alimony takes at most
Q2,000 (50%, priority), the other obligation at most Q400 (+10% after the
alimony cap), and the two are never simultaneous; given a salary at or
below the protected floor, then no non-alimony deduction applies.
  (FR-011)
- **AC-009:** Given a Q1,000 salary advance recovered over the payroll,
when amortization schedules, then no interest line is ever generated and
recovery spreads over ≥5 payslip periods (e.g., Q200 × 5) unless the worker
voluntarily elects a shorter term; given contract termination, then the
definitive liquidation may clear the balance. (FR-013, FR-014)
- **AC-010:** Given a worker debt to the patrono's associate (not an
advance/excess/civil-liability debt), when a payroll deduction is
attempted, then it is admitted only up to the garnishable proportion of the
salary per the FR-010/FR-011 ladder. (FR-015)
- **AC-011:** Given a recognized termination indemnization credit at
employer insolvency, when settlement ordering runs, then the credit is
tagged first-class (art. 101) with the special art. 426 execution path and
the privilege amount capped at the equivalent of 6 months of wages.
  (FR-016)
- **AC-012:** Given a firm permanently occupying 12 workers, when payroll
books configure, then mode = libro de salarios (MinTrabajo-authorized);
given a 5-worker firm, then mode = IGSS planillas with mechanics deferred
to file 07; given year-end, when the annual report generates, then it
contains the prior-year ordinary/extraordinary split and per-worker
days+salary within the first-2-months window. (FR-017..019)
- **AC-013:** Given a worker dismissed on 1-March who files a dismissal
claim, when the clock resolves, then the claim type carries 30 días hábiles
from termination; given a contractual prestación claim after contract end,
then 4 months; given a general Code-derived claim, then 2 years from the
event; given a Q500 partial payment on that 2-year claim, when the payment
posts, then a partial-payment interruption event emits and the elapsed
clock resets (saas recompute). (FR-020, FR-021)
- **AC-014:** Given a worker engaged by an intermediario for the benefit of
patrono P, when payroll liability posts, then both the intermediario and P
carry the solidarity flag (jointly liable); given a contractor working with
own equipment/capital, then he is flagged patrono, not intermediario.
  (FR-022)
- **AC-015:** Given a search for aguinaldo, bono, incentivo or propina
statutory rows in this file's CT LB table, when inspected, then zero
implementable rows exist — only the LB-016 negative finding and the art. 61
reporting-category occurrence, with the regimes deferred to
`04_statutory-bonuses.md`. (FR-024)
- **AC-016:** Given any sanction surface citing this file, when inspected,
then it carries no monetary sanction value — only the arts. 269 ff./422/
423/426 pointers with sanction values external (taxation/06, Código
Tributario art. 94 family). (FR-025)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
allowed set for this file: GOQ-73 (owned). GOQ-70/71 (R44 edition
discipline) are discharged by the qualifier on every CT LB row (§2), not by
OQ rows. All rows Status open; GOQs are trace-pending, not blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-73 (owned): "Inembargabilidad brackets (Q30/100/200/300) = 1961-scale, unindexed — do NOT implement numerics from this text; modern garnishment thresholds elsewhere." Affects FR-010 (ladder structure-only; threshold rows pending an external modern garnishment instrument — acquisition queue; FR-011 percentages are structure, not bracket numerics, and stand). | no | GT synthesis wave S-GT3 → acquisition queue (modern garnishment-threshold instrument) | open |
