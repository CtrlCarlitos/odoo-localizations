# HN — Payroll — 13th month (aguinaldo, config-gapped), 14th month (décimo cuarto mes) & bono educativo

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for Honduras' annual bonus layer of
clusters P2/P3/P4: (a) the **13th month** — *décimo tercer mes en concepto de
aguinaldo* (13th-month statutory year-end bonus) — as a CONFIG-GAPPED surface:
the aguinaldo's own instruments (D. 135-94 + reglamento Acuerdo 201-96) are
NOT in the corpus (negative CT finding R-H60; `86_ OQ-3` = TOP acquisition
lead), so this file encodes only what IS evidenced — the modality linkage that
the 14th-month and bono statutes print verbatim, and the ISR-side December
settlement interface — with every entitlement/pro-rata/base/deadline parameter
held as visibly blocked configuration (pattern per e-invoicing/04 SEE FRs); (b)
the full mechanics of the **14th month** — *décimo cuarto mes de salario en
concepto de compensación social* (14th-month salary as social compensation,
Acuerdo 02-95 reglamento of D. 135-94 Cap. IX Art. 34 as interpreted by
D. 54-95): entitlement year 1-jul→30-jun with the 100%-vs-proportional gate at
30-jun, permanent-employee eligibility, June payment default (pacto other date),
average-of-ordinary-salaries base with the SMM-average variant for small
industry/artesanías/small-scale agro, 30-day normalization for time and piece
workers, proportional payout on ANY exit, anticipo netting, better-terms
prevalence, integration into salario for all legal effects, and enforcement
metadata; and (c) the **bono educativo** (education bonus, Ley del Salario
Mínimo Art. 21-A as reformed by D. 43-97): ≤2×SMM eligibility gate, dated
rama×band amounts from the DGS annual tables, once-a-year timing after the
first trimestral exam, <1-year pro-rata, ≤15-permanent-workers employer
exemption, and its NON-salary character (excluded from prestaciones AND from
13th/14th bases).

It does **not** own: SMM values, promedio rows and the rama×band dated-row
sidecar — file `01_salario-minimo.md` (HN-PAYR-FR-001..040), consumed by range
only; the ISR plantilla/asalariados withholding engines including the
13th/14th-month 10×SMM-*promedio* EXCESS-ONLY caps and the December
settlement — taxation/04 (HN-TAX-FR-121..153), consumed by id; deduction
semantics / Art. 10 exclusions — taxation/02 (HN-TAX-FR-046..078); the DJIMR
export contract — fiscal-reporting/02 (HN-FREP-FR-054/055) on the
fiscal-reporting/01 chassis (HN-FREP-FR-001..032); comprobante de retención /
patronos-exempt-unless-requested — e-invoicing/03 (HN-EINV-FR-139/140);
IHSS contributions/incapacidad — `03_ihss.md` (HN-PAYR-FR-101..135) and
`04_ihss-incapacidad.md` (HN-PAYR-FR-141..170); RAP/fondo — `05_rap-fondo.md`
(HN-PAYR-FR-181..215); jornada — `06_jornada.md` (HN-PAYR-FR-221..250);
vacaciones — `07_vacaciones.md` (HN-PAYR-FR-261..280); cesantía/preaviso —
`08_cesantia-preaviso.md` (HN-PAYR-FR-291..325); suspension/maternity —
`09_suspension-maternity.md` (HN-PAYR-FR-331..360); salario/records —
`10_salario-records.md` (HN-PAYR-FR-371..405).

## 2. Legal Basis

Authority order (binding, per master evidence index): 14th month = `102_`
(Acuerdo 02-95 reglamento, 6-feb-1995) with the embedded D. 135-94 Cap. IX
Art. 34 quote and the D. 54-95 interpretation footnote; bono educativo =
`104_` (Ley del Salario Mínimo, D. 103) Arts. 21-A/21-B as reformed by
D. 43-97 (R-H43) + the `92_` DGS annual bono table (amounts); CT negative =
`86_` (D. 189-1959 CEDIJ consolidation). D-H1/D-H2/D-H3 bind everything
(dated rows, payslip-period resolution, never-guess rule, aggregate
ingestion depths).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo 02-95 (Reglamento del Décimo Cuarto Mes de Salario en Concepto de Compensación Social), CONSIDERANDO 1º + quote embebido del Art. 34 del D. 135-94: "Establécese como un derecho a todos los empleados y trabajadores, el pago del Décimo Cuarto Mes de Salario, el que se hará efectivo en el mes de junio de cada año, en la misma modalidad y condiciones con que se hace efectivo el Décimo Tercer Mes en Concepto de Aguinaldo. El Poder Ejecutivo por medio de la Secretaría en los Despachos de Trabajo y Seguridad Social, reglamentará la presente disposición." | Acuerdo 02-95 (14th-Month Regulation), first recital + embedded Art. 34 of D. 135-94: "It is established as a right of all employees and workers, payment of the 14th Month of Salary, which shall be made effective in the month of June of each year, under the same modality and conditions with which the 13th Month in the Concept of Aguinaldo is made effective. The Executive through the Ministry of Labor and Social Security shall regulate this provision." | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-CONSIDERANDO 1º + Art. 34 quote (pp.1-2) (EV82:EVID-238) |
| LB-002 | Acuerdo 02-95, Art. 2 + pie de página de interpretación: Art. 2: "El pago del Décimo Cuarto Mes de Salario será del 100 por ciento (100%), si se cumple el año de trabajo continuo al 30 de junio, o la proporción del mismo, de conformidad al tiempo trabajado, si a dicha fecha no se cumplen 12 meses de servicios continuos con el mismo empleador." Pie: "Interpretado, según Decreto No. 54-95 … En el sentido: De que el pago del Décimo Cuarto mes de Salario, en concepto de Compensación Social a partir de 1995, deberá de hacerse efectivo en el mes de junio de cada año y será del cien por ciento (100%) del salario si al 30 de junio se ha cumplido el año de trabajo continuo con el mismo empleador o la proporción del mismo de conformidad al tiempo trabajado, si a dicha fecha no se cumplen los doce (12) meses servidos continuos." | Acuerdo 02-95 Art. 2 + interpretation footnote (D. 54-95): payment is 100% if the continuous year of work with the same employer is completed by June 30, or the proportion thereof per time worked if 12 months are not served by that date; from 1995 payment is effective in June each year. (Two conflicting D. 54-95 gazette cites inside the footnotes — OQ-002; the rule itself is double-pinned by footnote + Art. 2 body.) | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Art. 2 (p.2) + Art. 34 interpretation footnote (p.1) (EV82:EVID-238) |
| LB-003 | Acuerdo 02-95, Arts. 1 y 4: Art. 1: "Todos los empleados y trabajadores permanentes, tendrán derecho al pago del Décimo Cuarto Mes de Salario en concepto de compensación social." Art. 4: "Para los efectos de este Reglamento, también se considerarán trabajadores y empleados permanentes, aquéllos a que se refiere el Artículo 347 del Código de Trabajo, así como aquellos trabajadores y empleados a quienes convencionalmente o por costumbre se les haya reconocido la calidad de permanentes en el servicio, sin consideración del número de días trabajados en el año, quienes también recibirán el pago proporcional." | Acuerdo 02-95 Arts. 1 and 4: all permanent employees and workers are entitled; also considered permanent are the workers of CT Art. 347 (irregular-work 200-day continuity) and those recognized as permanent by convention or custom regardless of days worked in the year — these receive the proportional payment. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 1 (pp.1-2) y 4 (p.2) (EV82:EVID-239) |
| LB-004 | Acuerdo 02-95, Arts. 3 y 5: Art. 3: "Si mediante negociación colectiva o contratación individual los empleados y trabajadores hubieren logrado un porcentaje mayor del que establece la ley, los empleadores estarán obligados a cumplir lo pactado." Art. 5: "El Décimo Cuarto Mes de Salario en concepto de compensación social, integrará para todos los efectos legales el concepto de salario, se pagará en el mes de junio de cada año. Sin embargo, las partes podrán pactar dicho pago en diferente fecha." | Acuerdo 02-95 Arts. 3 and 5: if collective bargaining or individual contracting achieved a greater percentage than the law, employers must honor what was agreed; the 14th Month integrates the concept of salario (salary) for all legal effects and is paid in June each year — however the parties may agree payment on a different date. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 3 (p.2) y 5 (p.2) (EV82:EVID-239) |
| LB-005 | Acuerdo 02-95, Arts. 6-8: Art. 6: "Cuando el salario se tase en forma mensual, el Décimo Cuarto Mes de Salario en concepto de compensación social … en base al promedio de los salarios ordinarios percibidos durante el tiempo trabajado en el año de que se trate. En la pequeña y mediana industria, artesanías, agricultura y ganadería en pequeña escala, el pago del Décimo Cuarto Mes de Salario se efectuará en base al promedio de los salarios mínimos percibidos durante el tiempo trabajado." Art. 7: "Para los trabajadores contratados por unidad de tiempo, cuyo salario sea diario, semanal, quincenal o mensual, el pago del Décimo Cuarto Mes de Salario, se hará en base a treinta (30) días, calculándose para ellos el promedio de los salarios ordinarios devengados durante el tiempo trabajado." Art. 8: "Para los trabajadores que laboran por unidad de obra (pieza, tarea, precio alzado o destajo), el pago del Décimo Cuarto Mes de Salario en base a treinta (30) días, calculado sobre el promedio de los salarios percibidos durante el período de que se trata." (Art. 6 dañado por run-on de impresión — reconstrucción entre paréntesis en la evidencia; cita recortada con …) | Acuerdo 02-95 Arts. 6-8: monthly-rated — computed on the average of the ORDINARY salaries received during the time worked in the year in question; for small and medium industry, artisanries, and small-scale agriculture and livestock, payment is made on the average of the MINIMUM salaries (SMM) received during the time worked; time-unit workers (daily/weekly/biweekly/monthly pay) — 30-day base computing the average of ordinary salaries earned; piece workers (pieza, tarea, precio alzado o destajo) — 30 days computed on the average of salaries received over the period. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 6-8 (p.2) (EV82:EVID-239) |
| LB-006 | Acuerdo 02-95, Arts. 9-10: Art. 9: "Si antes de cumplir el año, el trabajador renuncia o es despedido justificada o injustificadamente, el Décimo Cuarto Mes en concepto de compensación social, le será pagado proporcionalmente al tiempo trabajado." Art. 10: "Los anticipos que se hubieren dado al empleado o trabajador a cuenta del Décimo Cuarto Mes de Salario, serán deducibles al momento de hacer efectivo su pago." | Acuerdo 02-95 Arts. 9-10: if before completing the year the worker resigns or is dismissed with or without cause, the 14th Month is paid proportionally to time worked (no forfeiture); advances given on account of the 14th Month are deductible at the moment of payment. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 9 (p.2) y 10 (p.2) (EV82:EVID-239) |
| LB-007 | Acuerdo 02-95, Arts. 11-15: Art. 11: "Las personas naturales o jurídicas que al momento de entrar en vigencia el Decreto Legislativo Número 135-94 ya estuvieren pagando el Décimo Cuarto Mes, bajo ésta o cualquier otra denominación, no están obligadas más que a ajustarlo a las presentes disposiciones…"; Art. 13: "Los patronos que infrinjan, tergiversen o disminuyan lo prescrito en este Reglamento, serán sancionados con una multa que oscilará entre Cien a Cinco Mil Lempiras (L.100.00 a L.5,000.00)… La certificación que emita la indicada Secretaría de Estado tendrá carácter de título ejecutivo."; Art. 14: "Son nulos ipso-jure los actos o estipulaciones que impliquen renuncia, infracción, tergiversación o disminución de los derechos y obligaciones emanados del presente Reglamento."; Art. 15: "El primer pago del Décimo Cuarto Mes de Salario en concepto de compensación social se hará en forma proporcional, del veintiocho de octubre de mil novecientos noventa y cuatro, fecha en que entró en vigencia el Decreto Legislativo Número 135-94, al treinta de junio de mil novecientos noventa y cinco, sin perjuicio de lo establecido en el Artículo 5." | Acuerdo 02-95 Arts. 11-15: persons already paying a 14th month under this or any other name at vigencia need only align it to the regulation (subject to Art. 3 better terms); infringing/tergiversating/diminishing employers are fined L100.00-L5,000.00 and the STSS certification is an executive title; acts implying waiver or diminution are null ipso jure; the FIRST payment was proportional, from 28-oct-1994 (D. 135-94 vigencia) to 30-jun-1995. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 11-15 (pp.2-3) (EV82:EVID-240) |
| LB-008 | Ley del Salario Mínimo (D. 103), Art. 21-A (reformado por D. 43-97): "Se establece como un derecho a todos los empleados y trabajadores del sector público y privado que perciban hasta el equivalente de dos (2) salarios mínimos, el pago del BONO EDUCATIVO POR FAMILIA, el que hará efectivo una vez por año, después de la primera prueba trimestral de los educandos, como una compensación a los padres de los hijos en edad escolar, matriculados en los niveles de kínder, primaria y secundaria del país, consistirá en la cantidad de Quinientos Lempiras (L.500.00), incrementada en la misma proporción en que lo sea el salario mínimo y se pagará en la misma modalidad y condiciones en que se hace efectivo el Décimo Tercer Mes en concepto de Aguinaldo. En cuanto a la proporcionalidad para quienes no hubieren cumplido un (1) año de trabajar con el mismo patrono." + "El pago del bono no se computará como salario para el cálculo del pago de las prestaciones laborales ni para el pago del Décimo Tercer y Décimo Cuarto mes de salario." + "No se hará efectivo el pago del Bono, a los empleados y trabajadores que laboren en la pequeña y micro empresa, incluyendo las dedicadas a las actividades agropecuarias entendiéndose como tales aquellas en las que el número de trabajadores permanentes no exceda de quince (15)." | Minimum Wage Law (D. 103) Art. 21-A (reformed by D. 43-97, 28-abr-1997 per R-H43 — the print's "1977 [sic]" is a defect): all public- and private-sector employees earning up to the equivalent of 2 minimum wages have the right to the EDUCATION BONUS PER FAMILY, made effective once a year after the students' first trimestral exam, as compensation to parents of school-age children enrolled in kínder, primaria and secundaria; it consists of L500.00 (1997) increased in the same proportion as the minimum wage, and is paid in the same modality and conditions as the 13th Month (aguinaldo); proportionality applies to those with under 1 year with the same employer. The bonus is NOT computed as salary for severance (prestaciones) nor for the 13th/14th month; no bonus is payable to workers of small and micro enterprises, including agropecuary activities, i.e. those with no more than fifteen (15) permanent workers. | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Art. 21-A (pp.7-8); reforma D. 43-97 (R-H43) (EV82:EVID-218) |
| LB-009 | Ley del Salario Mínimo, Art. 21-B: "Durante el año de 1997, el Bono Educativo podrá hacer efectivo hasta en tres (3) cuotas mensuales." | Minimum Wage Law Art. 21-B: during 1997 only, the Education Bonus could be made effective in up to three (3) monthly installments — a 1997-only transition rule. | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Art. 21-B (p.8) (EV82:EVID-218) |
| LB-010 | DGS, "Tabla del Bono Educativo⅟ — Año 2026"; pie: "⅟En base a la Ley del Salario Mínimo y sus reformas, artículo 21-A del Decreto Número 43-97 de fecha 28 de abril de 1997, que establece el Bono Educativo." Bandas "De 16 a 20 / De 21 a 50 / De 51 a 150 / De 151 en adelante" × 11 ramas + "12 Empresas acogidas a la Ley de Zonas Libres — De 16 en adelante — 1,748.56" (matriz completa de 44 valores + fila ZL transcrita en §4; vigente Año 2026). | DGS (Dirección General de Salarios), "Education Bonus Table — Year 2026": amounts per rama × employer-size band (16-20 / 21-50 / 51-150 / 151 onward; the band floor 16 operationalizes the ≤15-workers exemption), plus a single zonas-libres row (L1,748.56); statutory basis footnote cites Art. 21-A of D. 43-97 dated 28-apr-1997 (the print supplying the correct year, R-H43). Full matrix transcribed in §4; amounts are present values of the L500-1997 × accumulated-SMM-increase formula — no per-cell derivation is published; values load as data. | `hn/sources/92_Tabla_Bono_Educativo_2026.pdf` | 92_ p.1 (EV82:EVID-229) |
| LB-011 | Código del Trabajo (D. 189-1959, impresión CEDIJ) — NEGATIVO: greps sobre todo el corpus del CT con 0 resultados para "aguinald*", "décimo tercer", "décimo cuarto"; CT-Art. 376: "Durante la vigencia del contrato el trabajador tiene derecho a percibir el salario, aún cuando no haya prestación del servicio por disposición o culpa del patrono." (Arts. 376-380 = reglas de salario, NO de aguinaldo.) | Labor Code negative finding: the CT contains NO aguinaldo, NO 13th/14th month, NO INVI, NO "salario integral", NO acoso provisions (R-H60) — Arts. 376-380 are salary rules, not bonus rules. The 13th month exists only in special law (D. 135-94 + reglamento Acuerdo 201-96, UNACQUIRED — `86_ OQ-3`); the 14th month likewise (D. 135-94 Art. 34 / Acuerdo 02-95). Never invent CT articles for these benefits. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | greps corpus-wide; CT-Arts. 376-380 (p.109) (EV85:EVID-327) |

## 3. Functional Requirements

### 3.1 P2 — 13th month (*aguinaldo*): statutory placeholder contract — CONFIG-GAPPED, BLOCKED

The P2 sub-cluster is BLOCKED on `EV85:86_ OQ-3` (TOP acquisition lead): the
aguinaldo's own instruments — D. 135-94 (Ley del Aguinaldo) and its reglamento
Acuerdo 201-96 — are unacquired (this lead subsumes D. 112, whose acquisition
routes are exhausted). The FRs below implement ONLY what the corpus evidences;
every entitlement, pro-rata, base, deadline and termination-payout parameter is
unresolved blocked configuration (pattern per e-invoicing/04 §3.8 SEE FRs).

- **HN-PAYR-FR-051:** The system shall enforce the CT content-negative guard
  (R-H60): no aguinaldo/13th-month rule may be sourced from, or cited to, any
  Código del Trabajo article — the CT contains none, and CT Arts. 376-380 are
  salario rules — so the aguinaldo configuration surface shall expose NO
  CT-article source field for these benefits. (LB-011; EV85:EVID-327; R-H60)
- **HN-PAYR-FR-052:** The system shall implement the aguinaldo entitlement
  surface as a CONFIG-GAPPED placeholder with five visibly blocked parameter
  slots — entitlement basis, pro-rata rule, computation base, payment
  deadline (December or otherwise) and termination payout — gated on
  acquiring D. 135-94 + Acuerdo 201-96; while blocked, no aguinaldo amount is
  computed, defaulted or guessed on any payslip (D-H2 never-guess rule), and
  the blocked state cites the missing instruments.
  (LB-011; EV85:EVID-327; EV85:86_ OQ-3)
- **HN-PAYR-FR-053:** The system shall model the *modalidad del aguinaldo*
  (aguinaldo modality) as ONE shared, config-gapped linkage parameter
  evidenced by the statutes that reference it: the 14th month is payable "en
  la misma modalidad y condiciones con que se hace efectivo el Décimo Tercer
  Mes en Concepto de Aguinaldo" (embedded D. 135-94 Art. 34 quote) and the
  bono educativo "se pagará en la misma modalidad y condiciones en que se
  hace efectivo el Décimo Tercer Mes en concepto de Aguinaldo" (Art. 21-A) —
  the aguinaldo is presumed to mirror the 14th-month modality, but that
  presumption shall NEVER be hardcoded: the parameter stays blocked until the
  aguinaldo instruments are acquired (OQ-001).
  (LB-001; LB-008; EV82:EVID-238; EV82:EVID-218)
- **HN-PAYR-FR-054:** The system shall hold the aguinaldo payment timing as
  a blocked parameter recording that ONLY the ISR side is evidenced in this
  corpus — the plantilla settles the 13th-month excess in December
  (taxation/04 HN-TAX-FR-127 + the December settlement of HN-TAX-FR-133,
  consumed by id) — while the labor-law payment month/deadline is NOT in the
  corpus and shall never be assumed to be "December" as law.
  (LB-001; EV82:EVID-238)
- **HN-PAYR-FR-055:** The system shall expose the aguinaldo payment amount
  as a feed to the ISR plantilla engines of taxation/04 (annual gross
  HN-TAX-FR-126; 13th-month excess-only cap HN-TAX-FR-127) strictly by id
  consumption — this file supplies the amount (once FR-052 unblocks), never
  the cap, the promedio, or any plantilla mechanics.
  (LB-001; EV82:EVID-238)

### 3.2 P3 — 14th month (*décimo cuarto mes*): full mechanics (Acuerdo 02-95)

- **HN-PAYR-FR-056:** The system shall model the 14th-month entitlement year
  as the continuous-work year ending at each 30-jun gate (accrual window
  1-jul→30-jun), tracked per contract from hire date (D-H3 depth: monthly
  aggregates per contract, no payslip-level import), with the resolution
  anchor = the June payslip period of the settlement.
  (LB-002; EV82:EVID-238)
- **HN-PAYR-FR-057:** The system shall evaluate the 100%-vs-proportional gate
  at each 30-jun: 100% of the computed amount when the worker has completed
  the continuous year of work with the same employer by that date; otherwise
  the proportion corresponding to the time worked in the entitlement year
  (D. 54-95 interpretation). (LB-002; EV82:EVID-238)
- **HN-PAYR-FR-058:** The system shall extend 14th-month eligibility to all
  permanent employees and workers, including the workers of CT Art. 347
  (irregular-work continuity) and workers recognized as permanent by
  convention or custom regardless of the number of days worked in the year —
  these receive the proportional payment.
  (LB-003; EV82:EVID-239)
- **HN-PAYR-FR-059:** The system shall default 14th-month payment to the
  month of June of each year, with an optional per-contract agreed payment
  date (*pacto en diferente fecha*) recorded as dated configuration that
  displaces the June default for that contract only.
  (LB-004; EV82:EVID-239)
- **HN-PAYR-FR-060:** The system shall compute the 14th-month base for
  monthly-rated workers as the average of ORDINARY salaries (*salarios
  ordinarios*) received during the time worked in the entitlement year — an
  ordinary-salary filter over monthly aggregates per contract (D-H3(b)), with
  non-ordinary items (and the 14th/13th/bono payments themselves) never
  entering the average.
  (LB-005; EV82:EVID-239)
- **HN-PAYR-FR-061:** The system shall apply the SMM-average variant: for
  workers of *pequeña y mediana industria, artesanías, agricultura y
  ganadería en pequeña escala*, the base is the average of the SALARIOS
  MÍNIMOS applicable during the time worked — sourced exclusively as the
  imported dated SMM rows of file `01_salario-minimo.md`
  (HN-PAYR-FR-001..040) resolved month-by-month across the entitlement
  window (a jul→jun window straddles SMM vintages), never re-derived and
  never actual wages.
  (LB-005; EV82:EVID-239)
- **HN-PAYR-FR-062:** The system shall normalize time-unit workers (paid
  daily, weekly, biweekly or monthly) to a thirty (30)-day base, computing
  for them the average of ordinary salaries earned during the time worked
  and expressing the payment over 30 days.
  (LB-005; EV82:EVID-239)
- **HN-PAYR-FR-063:** The system shall compute piece-rate workers — *unidad
  de obra (pieza, tarea, precio alzado o destajo)* — on the same 30-day
  base, calculated over the average of the salaries received during the
  period in question (no ordinary-salary filter is printed for this class —
  average of salaries received).
  (LB-005; EV82:EVID-239)
- **HN-PAYR-FR-064:** The system shall pay the 14th month PROPORTIONALLY to
  time worked when, before completing the year, the worker resigns or is
  dismissed with or without just cause — no exit class forfeits the accrued
  proportion. (LB-006; EV82:EVID-239)
- **HN-PAYR-FR-065:** The system shall net advances (*anticipos*) given on
  account of the 14th month against the settlement at the moment of payment,
  recording the gross, the anticipos and the net.
  (LB-006; EV82:EVID-239)
- **HN-PAYR-FR-066:** The system shall let negotiated better terms prevail:
  where collective bargaining or individual contracting achieved a
  percentage greater than the law, the employer obligation is what was
  agreed — the statutory computation is a floor, never a ceiling.
  (LB-004; EV82:EVID-239)
- **HN-PAYR-FR-067:** The system shall flag the 14th-month payment as
  INTEGRATING salario for all legal effects — consumption pointer for the
  sibling average/prestaciones bases (RAP/fondo `05_rap-fondo.md`
  HN-PAYR-FR-181..215; vacaciones `07_vacaciones.md` HN-PAYR-FR-261..280;
  cesantía/preaviso `08_cesantia-preaviso.md` HN-PAYR-FR-291..325), which
  take 14th-month amounts into their bases by id — the OPPOSITE of the bono
  educativo (FR-080). (LB-004; EV82:EVID-239)
- **HN-PAYR-FR-068:** The system shall support the prior-equivalent-payment
  alignment: employers already paying a 14th-month equivalent under this or
  any other denomination at the reglamento's vigencia are obliged only to
  align it to these provisions (subject to the FR-066 better-terms floor).
  (LB-007; EV82:EVID-240)
- **HN-PAYR-FR-069:** The system shall record as informational legal-notes
  metadata (no sanction engine): STSS/Inspección General del Trabajo
  vigilance; fines of L100.00 to L5,000.00 for infringing/tergiversating/
  diminishing the reglamento; the STSS certification's executive-title
  character; and the ipso-jure nullity of any act or stipulation implying
  waiver or diminution of 14th-month rights.
  (LB-007; EV82:EVID-240)
- **HN-PAYR-FR-070:** The system shall encode the first-period precedent as
  a dated historical entitlement-window row — 28-oct-1994 (D. 135-94
  vigencia per R-H44; the considerando's "1991 [sic]" is a print error) →
  30-jun-1995, paid proportionally — as the proration-from-statutory-start
  pattern for any future regime cutover (new windows arise as dated rows,
  never in-place edits).
  (LB-007; EV82:EVID-240; R-H44)
- **HN-PAYR-FR-071:** The system shall feed the June 14th-month payment to
  the ISR layer strictly as an amount consumed by id — the 14th enters the
  ISR annual gross only in the EXCESS above 10 × SMM *promedio*, per
  taxation/04 HN-TAX-FR-126 (annual gross) and HN-TAX-FR-128 (independent,
  excess-only cap, "en cada caso") — with the promedio feed owned by file
  `01_salario-minimo.md` (HN-PAYR-FR-001..040) and this file NEVER restating
  the plantilla or implying a cliff (amounts at or below the cap contribute
  zero, not a forfeit).
  (LB-001; LB-005; EV82:EVID-238; EV82:EVID-239)
- **HN-PAYR-FR-072:** The system shall apply the D-H2 payroll resolution
  discipline to every 14th-month computation: resolution key = (payslip
  period, worker attributes); paid slips frozen; corrections recompute with
  the ORIGINAL entitlement-year rows (original SMM vintages where FR-061
  applies); filed periods write-protected; and the resolved values (gate
  outcome, averages, applicable SMM rows) snapshotted on write.
  (LB-002; LB-005; EV82:EVID-238; EV82:EVID-239)

### 3.3 P4 — *Bono educativo* (education bonus)

- **HN-PAYR-FR-073:** The system shall gate bono educativo eligibility on
  the worker perceiving up to the equivalent of two (2) applicable SMM —
  public and private sectors both — resolving the 2×SMM ceiling with the
  dated SMM rows of file `01_salario-minimo.md` (HN-PAYR-FR-001..040) as of
  the bono computation period (D-H2: dated, never hardcoded; re-resolves
  when SMM vintages change). (LB-008; EV82:EVID-218)
- **HN-PAYR-FR-074:** The system shall register the *educandos* (students)
  per worker's family — school-age children matriculated in kínder, primaria
  or secundaria — and pay the BONO EDUCATIVO POR FAMILIA once a year, after
  the first trimestral exam of the educandos, as ONE payment per family
  (independent of the number of educandos); no matriculated educando → no
  bono. (LB-008; EV82:EVID-218)
- **HN-PAYR-FR-075:** The system shall load bono amounts as DATED rama×band
  rows seeded from the DGS annual bono tables (the 2026 print: 44 values +
  the zonas-libres single band, valid 2026-01-01→2026-12-31, transcribed in
  §4) — additive-only per year, never replaced in place; amounts load as
  data from the DGS prints.
  (LB-010; EV82:EVID-229)
- **HN-PAYR-FR-076:** The system shall record the indexation MECHANISM as
  metadata only — base L500.00 (1997) "incrementada en la misma proporción
  en que lo sea el salario mínimo" — and shall NEVER derive a bono amount
  from L500 × accumulated SMM increase: present values are unpublished
  per-cell derivations; the operative amount is always the DGS table row
  (D-H2 never-guess rule). (LB-008; LB-010; EV82:EVID-218; EV82:EVID-229)
- **HN-PAYR-FR-077:** The system shall tie bono payment form to the shared
  aguinaldo-modality parameter of FR-053 ("en la misma modalidad y
  condiciones en que se hace efectivo el Décimo Tercer Mes en concepto de
  Aguinaldo") — a config-gapped linkage: the bono's own statutory timing and
  amount mechanics (FR-073..076) are NOT blocked, only modality-derived
  conditions are. (LB-008; EV82:EVID-218)
- **HN-PAYR-FR-078:** The system shall pay the bono proportionally to
  workers who have not completed one (1) year of work with the same
  employer. (LB-008; EV82:EVID-218)
- **HN-PAYR-FR-079:** The system shall exempt from bono payment employers
  of *pequeña y micro empresa* — including agropecuary activities — with no
  more than fifteen (15) permanent workers, via a company-level permanent-
  headcount flag (dated, resolved as of the bono period); the DGS table's
  16-20 band floor is the table-side echo of this exemption (16 = first
  non-excluded count). (LB-008; LB-010; EV82:EVID-218; EV82:EVID-229)
- **HN-PAYR-FR-080:** The system shall tag the bono as a NON-salary payroll
  input: excluded from salario for the computation of *prestaciones
  laborales* (labor severance) AND from the 13th/14th-month computation
  bases — the sibling bases of files 05/07/08 and the FR-060/061 averages
  never include bono amounts (the exact opposite of FR-067).
  (LB-008; EV82:EVID-218)
- **HN-PAYR-FR-081:** The system shall flag the statutory bono as
  non-taxable-salary for ISR — kept out of the plantilla annual gross by id
  consumption of taxation/04 HN-TAX-FR-130 (Art. 10 exclusions as consumed
  by the plantilla; ISR Art. 10.h family semantics owned by the taxation
  files) — distinct from non-statutory employer school bonuses, which the
  plantilla lists among other gross income.
  (LB-008; EV82:EVID-218)
- **HN-PAYR-FR-082:** The system shall encode Art. 21-B as a historical
  transition row valid only within calendar 1997 (up to three monthly
  *cuotas*); no post-1997 computation may ever select it.
  (LB-009; EV82:EVID-218)
- **HN-PAYR-FR-083:** The system shall record the bono statute's provenance
  per R-H43: Art. 21-A/21-B as reformed by D. 43-97 of 28-abr-1997 (La
  Gaceta 28,271, 29-may-1997) — the 104_ print's "1977 [sic]" footnote year
  is a defect, corrected by the 92_ statutory-basis footnote — as source
  metadata on the bono configuration.
  (LB-008; LB-010; EV82:EVID-218; EV82:EVID-229; R-H43)
- **HN-PAYR-FR-084:** The system shall treat a year with no loaded DGS bono
  table (e.g. 2027 — no table in corpus, expected with the 2027 SMM cycle)
  as a BLOCKED configuration gap for that year's bono runs — never the
  prior-year row silently reused, never an indexed derivation.
  (LB-010; EV82:EVID-229; EV82:92_ OQ-1)
- **HN-PAYR-FR-085:** The system shall source bono eligibility parameters
  exclusively from Art. 21-A (FR-073/074/077/078/079/080) — the DGS table
  carries AMOUNTS ONLY; no eligibility, timing or character rule may be
  inferred from the table (guard for `92_ OQ-2`).
  (LB-008; LB-010; EV82:EVID-218; EV82:EVID-229)
- **HN-PAYR-FR-086:** The system shall carry the zonas-libres employers as
  their own single-band dated row ("Empresas acogidas a la Ley de Zonas
  Libres — De 16 en adelante"; 2026: L1,748.56) mirroring the row-12 family
  of the SMM tables (file 01), inside the same bono row model.
  (LB-010; EV82:EVID-229)

## 4. Data Model

No CSV sidecar is allocated for this file: the bono 2026 matrix is transcribed
inline below (a future sidecar may be seeded from the DGS prints); all SMM /
promedio values are IMPORTED read-only from file
`01_salario-minimo.md` (HN-PAYR-FR-001..040).

**Aguinaldo placeholder (blocked):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.payroll.aguinaldo.config (new, BLOCKED) | state, entitlement_basis, prorata_rule, base_formula, payment_deadline, termination_payout, modality_parameter | char (empty-blocked) | state: blocked · active; all parameter slots empty while D. 135-94 + Acuerdo 201-96 unacquired (OQ-001); modality_parameter SHARED with the 14th month and bono (FR-053/077) | FR-051..FR-055 |
| hr.salary.rule (aguinaldo lines) | l10n_hn_config_gap_flag | boolean | renders visibly blocked; never a computed/guessed amount | FR-052 |

**14th-month engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | 14m_entitlement_year_start/end (derived), 14m_payment_month (default june), 14m_pacto_date, smm_average_variant (boolean) | date/select/date/boolean | entitlement year 1-jul→30-jun per continuous contract; variant for pequeña y mediana industria · artesanías · agricultura y ganadería en pequeña escala | FR-056, FR-059, FR-061 |
| l10n_hn.payroll.14m.settlement (new) | employee, contract, entitlement_year, gate_outcome (full · proportional), time_worked_factor, average_ordinary_salary, base_days (30), gross_amount, anticipos, net_amount, smm_rows_snapshot | m2o/date/select/monetary | June (or pacto) settlement trace; snapshots resolved SMM vintages on write (D15) | FR-057..FR-065, FR-072 |
| hr.payslip (termination run) | 14m_exit_proportional line | monetary | proportional payout on any exit class (resignation · justified/unjustified dismissal) | FR-064 |
| l10n_hn.payroll.14m.anticipo (new) | settlement_id, date, amount | m2o/date/monetary | advance ledger netted at payment | FR-065 |
| l10n_hn.legal.note (metadata) | fines L100.00-L5,000.00 · executive-title certification · ipso-jure nullity | char | informational only | FR-069 |
| l10n_hn.payroll.window (dated config) | first period 1994-10-28→1995-06-30 (proportional) | date rows | proration-from-statutory-start precedent (R-H44) | FR-070 |
| hr.payslip | isr_14m_feed | monetary | amount consumed by taxation/04 HN-TAX-FR-126/128 by id | FR-071 |

**Bono educativo:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.bono.educativo.amount (new) | rama, band, amount, valid_from, valid_to, source_print | char/select/monetary/date | bands: 16_20 · 21_50 · 51_150 · 151_onward · zl_16_onward; one row set per DGS annual print; missing year = blocked gap | FR-075, FR-076, FR-084, FR-086 |
| hr.employee | bono_eligibility (computed ≤2×SMM, dated SMM import), children/educandos registry | boolean + child rows | educando: school_level kinder · primaria · secundaria, matriculated flag | FR-073, FR-074, FR-078 |
| res.company | permanent_workers_count, bono_exempt (≤15) | integer/boolean | resolved as of the bono period (dated) | FR-079 |
| hr.salary.rule (bono line) | is_salary = false; isr_non_taxable_flag = true | boolean | excluded from prestaciones + 13th/14th bases; ISR exclusion via taxation/04 FR-130 consumption | FR-080, FR-081 |
| l10n_hn.payroll.window (dated config) | Art. 21-B row valid 1997-01-01→1997-12-31 (≤3 cuotas) | date rows | historical transition, never selectable post-1997 | FR-082 |
| l10n_hn.legal.note (metadata) | D. 43-97 28-abr-1997, G 28,271 29-may-1997 (R-H43) | char | provenance on bono config | FR-083 |

**Bono educativo 2026 matrix (DGS print, EVID-229; valid 2026-01-01→2026-12-31):**

| Rama | De 16 a 20 | De 21 a 50 | De 51 a 150 | De 151 en adelante |
|------|-----------|-----------|------------|-------------------|
| 1 Agricultura, silvicultura, caza y pesca | 1,764.14 | 1,780.04 | 1,858.19 | 1,905.04 |
| 2 Explotación de minas y canteras | 1,948.63 | 1,964.53 | 2,061.08 | 2,131.18 |
| 3 Industria manufacturera | 1,956.13 | 1,972.03 | 2,068.58 | 2,138.68 |
| 4 Electricidad, gas y agua | 1,803.06 | 1,818.96 | 1,915.51 | 1,985.61 |
| 5 Construcción | 1,956.13 | 1,972.03 | 2,068.58 | 2,138.68 |
| 6 Comercio al por mayor y menor | 1,956.13 | 1,972.03 | 2,068.58 | 2,138.68 |
| 7 Restaurantes y hoteles | 1,956.13 | 1,972.03 | 2,063.63 | 2,118.73 |
| 8 Transporte, almacenamiento y comunicaciones | 1,953.60 | 1,969.50 | 2,066.05 | 2,136.15 |
| 9 Establecimientos financieros, bienes inmuebles y servicios prestados a las empresas | 1,857.20 | 1,873.10 | 1,969.65 | 2,039.75 |
| 10 Servicios comunales, sociales y personales, seguridad y limpieza | 1,963.60 | 1,979.50 | 2,076.05 | 2,146.15 |
| 11 Actividades de hospitales | 1,946.13 | 1,962.03 | 2,058.58 | 2,128.68 |
| 12 Empresas acogidas a la Ley de Zonas Libres — De 16 en adelante | 1,748.56 | — | — | — |

## 5. Odoo Mapping

Layer semantics for this file: `odoo` for every row — all logic is
computation/bookkeeping inside the LGPL client (hr module family); no
thin-client/SaaS split surface and no DTE-like transmission surface exists for
payroll in the corpus. Model names stable across Odoo 17/18/19/20; no
version-specific behavior arises beyond the dated-legal-parameter notes below.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-051..FR-055 | odoo | l10n_hn.payroll.aguinaldo.config (new) + hr.salary.rule block | blocked slots + shared modality param | Config-gap pattern per e-invoicing/04 FR-166..169; D15/D16: regime arrives as dated config rows on acquisition (never in-place edits); D12: re-check acquisition lead quarterly (OQ-001); CT-source field absent by design (R-H60) |
| FR-056..FR-059 | odoo | hr.contract + hr.payslip (June run) | entitlement-year, payment-month/pacto | D15: gate resolved at the June payslip period, snapshot on write; D18: mid-year go-live ingests straddle-window monthly aggregates for the open entitlement year (jul→jun straddles calendar FYs), no payslip-level import (D-H3) |
| FR-060..FR-063, FR-072 | odoo | l10n_hn.payroll.14m.settlement + hr.salary.rule + SMM import (file 01) | averages, 30-day base, snapshots | D15/D16: SMM vintages resolve month-by-month across the window (jul→jun straddle); corrections recompute with original-period rows; filed periods write-protected; paid slips frozen |
| FR-064, FR-065 | odoo | hr.payslip termination run + l10n_hn.payroll.14m.anticipo | exit pro-rata, advance netting | Termination-date anchor (not "today") for the proration factor |
| FR-066, FR-068 | odoo | hr.contract (pact/CBII fields) | better-terms floor | upward-only override; alignment path for pre-existing equivalents |
| FR-067 | odoo | hr.salary.rule tagging | integrates_salario = true | consumption flag for sibling files 05/07/08 bases |
| FR-069 | odoo | l10n_hn.legal.note | fines/executor-title/nullity | informational metadata only |
| FR-070 | odoo | l10n_hn.payroll.window (dated row) | 1994-10-28→1995-06-30 | R-H44 vigencia pin; regime-cutover pattern |
| FR-071 | odoo | hr.payslip | isr_14m_feed | amount only; caps/plantilla = taxation/04 HN-TAX-FR-126/128 by id; excess-only, no cliff |
| FR-073, FR-074, FR-078 | odoo | hr.employee + educando registry + hr.salary.rule (bono) | ≤2×SMM gate (SMM import), per-family timing | D15: gate value dated (rides SMM vintages of file 01); re-resolves on new bienio rows |
| FR-075, FR-076, FR-084, FR-086 | odoo | l10n_hn.bono.educativo.amount | dated rama×band rows, ZL row | D12: annual DGS-print cycle (2026 seeded inline §4); missing year = blocked flag (OQ-004); never L500×index derivation |
| FR-077 | odoo | shared modality parameter (FR-053 surface) | blocked linkage | bono's own mechanics unblocked; only modality-derived conditions blocked |
| FR-079 | odoo | res.company | permanent headcount + exemption flag | dated resolution as of the bono period; 16-20 band floor echo |
| FR-080, FR-081 | odoo | hr.salary.rule tagging | is_salary = false; isr_non_taxable_flag | sibling-base exclusion + taxation/04 FR-130 consumption by id |
| FR-082, FR-083 | odoo | l10n_hn.payroll.window + l10n_hn.legal.note | 1997-only row; R-H43 provenance | historical row never selectable post-1997 |

Version-regime notes (D12): the dated legal parameters of this file are (a)
the annual DGS bono tables (Jan-1 effectivity per year, additive rows), (b)
the SMM vintages consumed from file 01 (including mid-year maquila splits —
resolve by each month of the entitlement window), and (c) the 1994-1995
first-period window and the 1997 Art. 21-B transition (historical rows). No
adaptation windows exist in the instruments. D18: June-settlement go-lives
ingest the straddle-window monthly aggregates (prior-FY detail tier) without
payslip-level import. D19: no special posting tiers — settlements post
through standard payroll journals.

## 6. Acceptance Criteria

- **AC-001:** Given a December 2026 payroll run with the aguinaldo config
  surface empty (D. 135-94 + Acuerdo 201-96 unacquired), then aguinaldo lines
  are visibly blocked citing the missing instruments — no amount computed,
  defaulted or guessed — and the aguinaldo rule's source dropdown offers no
  CT article (FR-051, FR-052).
- **AC-002:** Given the shared modality parameter in blocked state, then the
  June 14th-month settlement computes normally on its own statutory base
  while the aguinaldo/bono modality-linkage fields render blocked (FR-053,
  FR-077).
- **AC-003:** Given a worker hired 01-jul-2024, then at the 30-jun-2025 gate
  the continuous year is complete and the 2024-2025 settlement pays 100%;
  given a worker hired 01-oct-2024, then at 30-jun-2025 the factor is 9/12 =
  0.75 (22.5 of the 30 base days) (FR-056, FR-057).
- **AC-004:** Given a daily-rated time worker whose ordinary salaries over
  the window average L450.00/day, then the 14th = 30 × 450.00 =
  L13,500.00; given a monthly-rated worker averaging L20,000.00 ordinary
  monthly salary, then the 30-day normalization yields L20,000.00 (FR-060,
  FR-062).
- **AC-005:** Given a pequeña-industria worker (manufacturera rama, 1-10
  band) with entitlement window jul-2025→jun-2026 and SMM rows 12,140.69
  (6 months of 2025) and 12,869.14 (6 months of 2026), then the variant base
  = (12,140.69×6 + 12,869.14×6) ÷ 12 = L12,504.92 (print 2dp) — and the
  worker's higher actual wages never enter the computation (FR-061).
- **AC-006:** Given a worker who resigns effective 28-feb-2026 with window
  start 01-jul-2025 (8 months) and average daily salary L500.00, then the
  exit settlement pays 8/12 × 30 × 500.00 = L10,000.00 — the same outcome as
  for unjustified dismissal (FR-064).
- **AC-007:** Given a computed 14th of L13,500.00 with recorded anticipos of
  L4,000.00, then the net paid at settlement = L9,500.00 (FR-065).
- **AC-008:** Given a collective pact granting a 14th equal to 1.5× the
  average month, then the settlement applies the pact; given no pact, the
  statutory 1.0× computes — the statute never lowers a pact (FR-066).
- **AC-009:** Given a 14th payment of L20,000.00 and a bono of L1,972.03,
  then the 14th enters the sibling average bases (vacaciones, cesantía,
  fondo — files 07/08/05) while the bono enters none of them NOR the
  13th/14th bases (FR-067, FR-080).
- **AC-010:** Given a June-2026 14th of L160,000.00 with the promedio feed
  at L14,917.20 (cap L149,172.00), then the ISR annual-gross feed =
  L10,828.00 (excess only, via HN-TAX-FR-128); given a 14th of exactly
  L149,172.00, then the feed = L0.00 — no cliff (FR-071).
- **AC-011:** Given a worker employed since before 28-oct-1994, then the
  first-period settlement row 1994-10-28→1995-06-30 computes a PRORATED
  (not 100%) 14th (FR-070).
- **AC-012:** Given a worker with monthly salary L20,000.00 and applicable
  SMM L12,869.14 (2×SMM = L25,738.28), then the bono eligibility gate
  passes; given L26,000.00, then it fails — and the gate re-resolves when
  the SMM vintage changes (FR-073).
- **AC-013:** Given a comercio rama employer with 45 permanent workers, then
  the 2026 bono = band 21-50 = L1,972.03; given 15 permanent workers, then
  no bono line arises; given 16, then band 16-20 = L1,956.13 (FR-075,
  FR-079).
- **AC-014:** Given a worker with two matriculated primaria educandos, then
  ONE bono payment per family issues after the first trimestral exam; given
  no matriculated educando, then no bono accrues (FR-074).
- **AC-015:** Given any 2026 bono computation, then the Art. 21-B row
  (valid 1997 only) is never selectable (FR-082).
- **AC-016:** Given a January 2027 bono run with no 2027 DGS table loaded,
  then the run is blocked with a missing-table flag — never the 2026 row
  reused, never L500 × accumulated index derived (FR-084).
- **AC-017:** Given a paid June-2025 14th slip corrected in August 2025,
  then the correction recomputes with the original 2024-2025 entitlement-year
  rows and original SMM vintages, and the filed June period stays
  write-protected (adjustment lines only) (FR-072).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `EV85:86_ OQ-3` — aguinaldo instruments UNACQUIRED: D. 135-94 (Ley del Aguinaldo) + reglamento Acuerdo 201-96 (TOP acquisition lead; subsumes D. 112, routes exhausted). Entitlement/pro-rata/base/December-deadline/termination-payout cannot be LB'd; FR-051..055 are config-gapped placeholders on the corpus's modality-linkage + ISR-interface evidence only. | yes (P2 sub-cluster only) | acquisition queue / controller | open |
| OQ-002 | `EV82:102_ OQ-2` — two conflicting D. 54-95 citations inside 102_'s footnotes (Art. 34 footnote: 25-abr-1995, G 27,655 18-may-1995; Art. 1 footnote: 28-mar-1995, G 28,639 28-abr-1995 — gazette numbering must increase with date, so at least one is corrupt). The 30-jun rule is double-pinned (footnote + Art. 2 body) so the FRs stand; acquire D. 54-95 to pin the interpretation instrument. | no | acquisition queue | open |
| OQ-003 | `EV82:102_ OQ-3` — 102_ is a scanned compilation extract (pp. 247-249) with word run-ons; reconstructions bracketed/[?] in the evidence. Re-OCR at 400dpi/PSM 6 if verbatim-critical quoting is needed before freezing LB-005 text. | no | extraction queue | open |
| OQ-004 | `EV82:92_ OQ-1` — suspected bono reglamento ("Acuerdo 154-2000" family) appears in NO corpus document — unverified lead; acquire before asserting any bono procedural rule beyond Art. 21-A's own text. Also: no 2027 bono table in corpus (expected with the 2027 SMM cycle) — FR-084 blocks. | no | acquisition queue | open |
| OQ-005 | `EV82:92_ OQ-2` — eligibility parameters live in Art. 21-A, NOT in the DGS table (amounts only); the 16-20 band floor is the table-side echo of the ≤15 exemption (16 = first non-excluded count) — consistent but unstated; encoded as the FR-085 source guard. | no | Takumi S-HN4 | open (encoded) |
| OQ-006 | `EV82:102_ OQ-1` → RESOLVED at synthesis via R-H44: the considerando's "12 de Octubre de 1991 [sic]" is a print error; D. 135-94 = 1994, vigencia 28-oct-1994 (per Art. 15; the 8-month first period is coherent only for 1994). Encoded in FR-070. No further action. | no | — | resolved |
