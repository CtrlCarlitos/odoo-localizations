# HN — Payroll — 13th month (aguinaldo, D. 112-1982), 14th month (décimo cuarto mes) & bono educativo

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller; W5 wave (D. 112 unblock + bono reglamento) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for Honduras' annual bonus layer of
clusters P2/P3/P4: (a) the **13th month** — *décimo tercero mes en concepto de
aguinaldo* (13th-month statutory year-end bonus) — per its statutory home
**Decreto 112 of 1982 (Ley del Séptimo Día y Décimo Tercer Mes en Concepto de
Aguinaldo), acquired as `105_` at the W5 wave (R-H74)**: entitlement
(permanents + jubilados/pensionados), 31-dic 12-month same-employer gate,
December default + pacto, ordinary-salary-average base with the SMM-average
variant, the D. 178-86/D. 2-87 interpretation rules (100%-or-proportion, CBII
floor, 30-day base, obra ÷-days formula, convention/custom permanents), exit
proration + anticipo netting, and the instrument-chain dated rows (**W6: the
chain is now ORIGINAL-pinned end-to-end — `113_` = the G 23,848 original
print, `110_`/`111_`/`112_` = the reform/interp originals; OQ-008/OQ-009
RESOLVED; residual: the Art. 18 print variance ruled R-H80; the "Acuerdo
201-96" attribution voided — R-H75); the séptimo día chapter of the same law lives in
file `06_jornada-surcharges.md` (FR-234/235 + FR-248/249); (b)
the full mechanics of the **14th month** — *décimo cuarto mes de salario en
concepto de compensación social* (14th-month salary as social compensation,
Acuerdo 02-95 reglamento — G 27,587 23-feb-1995 — of D. 135-94 Cap. IX Art. 34
as interpreted by **D. 74-95** [re-attributed W7, R-H81] and extended to all
jubilados/pensionados by **D. 54-95**, G 27,639 28-abr-1995): entitlement year
1-jul→30-jun with the 100%-vs-proportional gate at
30-jun, permanent-employee eligibility, June payment default (pacto other date),
average-of-ordinary-salaries base with the SMM-average variant for small
industry/artesanías/small-scale agro, 30-day normalization for time and piece
workers, proportional payout on ANY exit, anticipo netting, better-terms
prevalence, integration into salario for all legal effects, and enforcement
metadata; and (c) the **bono educativo** (education bonus, Ley del Salario
Mínimo Art. 21-A as reformed by D. 43-97 — gazette original `106_`, R-H43
double-pinned): ≤2×SMM eligibility gate, dated rama×band amounts from the DGS
annual tables, once-a-year timing after the first trimestral exam, <1-year
pro-rata, ≤15-permanent-workers employer exemption, and its NON-salary
character (excluded from prestaciones AND from 13th/14th bases), now completed
by the **Reglamento STSS-154-2000** (also `106_`, OQ-004 resolved): calendar-
year 100% gate, post-exit claim, mid-year-entry forward proration, the 2×SMM
gate's exclusion list (OT/primas/bonificaciones/gratificaciones out), and the
family-allocation matrix.

It does **not** own: SMM values, promedio rows and the rama×band dated-row
sidecar — file `01_smm-chassis.md` (HN-PAYR-FR-001..040), consumed by range
only; the ISR plantilla/asalariados withholding engines including the
13th/14th-month 10×SMM-*promedio* EXCESS-ONLY caps and the December
settlement — taxation/04 (HN-TAX-FR-121..153), consumed by id; deduction
semantics / Art. 10 exclusions — taxation/02 (HN-TAX-FR-046..078); the DJIMR
export contract — fiscal-reporting/02 (HN-FREP-FR-054/055) on the
fiscal-reporting/01 chassis (HN-FREP-FR-001..032); comprobante de retención /
patronos-exempt-unless-requested — e-invoicing/03 (HN-EINV-FR-139/140);
IHSS contributions/incapacidad — `03_ihss-cotizaciones.md` (HN-PAYR-FR-101..135) and
`04_ihss-incapacidad.md` (HN-PAYR-FR-141..170); RAP/fondo — `05_rap-fondo.md`
(HN-PAYR-FR-181..215); jornada — `06_jornada-surcharges.md` (HN-PAYR-FR-221..247);
vacaciones — `07_vacaciones.md` (HN-PAYR-FR-261..280); cesantía/preaviso —
`08_cesantia-preaviso.md` (HN-PAYR-FR-291..325); suspension/maternity —
`09_suspension-maternity-special.md` (HN-PAYR-FR-331..357); salario/records —
`10_salario-concepts-records.md` (HN-PAYR-FR-371..405).

## 2. Legal Basis

Authority order (binding, per master evidence index): **13th month = `105_`
(D. 112-1982 + its in-print interpretation chain D. 178-86/D. 2-87/D. 36-90 +
reform D. 179-97; authentically interpreted 2021 by `89_`)** — R-H74; 14th
month = `102_` (Acuerdo 02-95 reglamento, 6-feb-1995; gazette G 27,587
23-feb-1995 per `119_`) with the embedded D. 135-94 Cap. IX Art. 34 quote,
the **D. 74-95** interpretation footnote (G 27,655 18-may-1995) and the
**D. 54-95** tacit-reform footnote (jubilados/pensionados extension,
G 27,639 28-abr-1995) — attribution decode R-H81 (W7, `119_` EVID-429);
bono educativo = `106_` (D. 43-97 Art. 21-A/21-B gazette original, G 28,271
29-may-1997 — R-H43 double-pinned) + the Reglamento STSS-154-2000 in the same
file (OQ-004 resolved) + the `92_` DGS annual bono table (amounts); CT
negative = `86_` (D. 189-1959 CEDIJ consolidation, R-H60). D-H1/D-H2/D-H3 bind
everything (dated rows, payslip-period resolution, never-guess rule, aggregate
ingestion depths).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Acuerdo 02-95 (Reglamento del Décimo Cuarto Mes de Salario en Concepto de Compensación Social), CONSIDERANDO 1º + quote embebido del Art. 34 del D. 135-94: "Establécese como un derecho a todos los empleados y trabajadores, el pago del Décimo Cuarto Mes de Salario, el que se hará efectivo en el mes de junio de cada año, en la misma modalidad y condiciones con que se hace efectivo el Décimo Tercer Mes en Concepto de Aguinaldo. El Poder Ejecutivo por medio de la Secretaría en los Despachos de Trabajo y Seguridad Social, reglamentará la presente disposición." | Acuerdo 02-95 (14th-Month Regulation), first recital + embedded Art. 34 of D. 135-94: "It is established as a right of all employees and workers, payment of the 14th Month of Salary, which shall be made effective in the month of June of each year, under the same modality and conditions with which the 13th Month in the Concept of Aguinaldo is made effective. The Executive through the Ministry of Labor and Social Security shall regulate this provision." | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-CONSIDERANDO 1º + Art. 34 quote (pp.1-2) (EV82:EVID-238) |
| LB-002 | Acuerdo 02-95, Art. 2 + pie de página de interpretación: Art. 2: "El pago del Décimo Cuarto Mes de Salario será del 100 por ciento (100%), si se cumple el año de trabajo continuo al 30 de junio, o la proporción del mismo, de conformidad al tiempo trabajado, si a dicha fecha no se cumplen 12 meses de servicios continuos con el mismo empleador." Pie: "Interpretado, según Decreto No. 74-95 … En el sentido: De que el pago del Décimo Cuarto mes de Salario, en concepto de Compensación Social a partir de 1995, deberá de hacerse efectivo en el mes de junio de cada año y será del cien por ciento (100%) del salario si al 30 de junio se ha cumplido el año de trabajo continuo con el mismo empleador o la proporción del mismo de conformidad al tiempo trabajado, si a dicha fecha no se cumplen los doce (12) meses servidos continuos." [interp footnote prints 74-95 — W7 dual-dpi fix, R-H81; the W4 LB read "54-95" was a transcription defect] | Acuerdo 02-95 Art. 2 + interpretation footnote (D. 74-95): payment is 100% if the continuous year of work with the same employer is completed by June 30, or the proportion thereof per time worked if 12 months are not served by that date; from 1995 payment is effective in June each year. (The two footnotes cite TWO different decrees — 74-95 interp / 54-95 extension — OQ-002 RESOLVED W7, R-H81; the rule itself is double-pinned by footnote + Art. 2 body.) | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Art. 2 (p.2) + Art. 34 interpretation footnote (p.1) (EV82:EVID-238) |
| LB-003 | Acuerdo 02-95, Arts. 1 y 4: Art. 1: "Todos los empleados y trabajadores permanentes, tendrán derecho al pago del Décimo Cuarto Mes de Salario en concepto de compensación social." Art. 4: "Para los efectos de este Reglamento, también se considerarán trabajadores y empleados permanentes, aquéllos a que se refiere el Artículo 347 del Código de Trabajo, así como aquellos trabajadores y empleados a quienes convencionalmente o por costumbre se les haya reconocido la calidad de permanentes en el servicio, sin consideración del número de días trabajados en el año, quienes también recibirán el pago proporcional." | Acuerdo 02-95 Arts. 1 and 4: all permanent employees and workers are entitled; also considered permanent are the workers of CT Art. 347 (irregular-work 200-day continuity) and those recognized as permanent by convention or custom regardless of days worked in the year — these receive the proportional payment. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 1 (pp.1-2) y 4 (p.2) (EV82:EVID-239) |
| LB-004 | Acuerdo 02-95, Arts. 3 y 5: Art. 3: "Si mediante negociación colectiva o contratación individual los empleados y trabajadores hubieren logrado un porcentaje mayor del que establece la ley, los empleadores estarán obligados a cumplir lo pactado." Art. 5: "El Décimo Cuarto Mes de Salario en concepto de compensación social, integrará para todos los efectos legales el concepto de salario, se pagará en el mes de junio de cada año. Sin embargo, las partes podrán pactar dicho pago en diferente fecha." | Acuerdo 02-95 Arts. 3 and 5: if collective bargaining or individual contracting achieved a greater percentage than the law, employers must honor what was agreed; the 14th Month integrates the concept of salario (salary) for all legal effects and is paid in June each year — however the parties may agree payment on a different date. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 3 (p.2) y 5 (p.2) (EV82:EVID-239) |
| LB-005 | Acuerdo 02-95, Arts. 6-8: Art. 6: "Cuando el salario se tase en forma mensual, el Décimo Cuarto Mes de Salario en concepto de compensación social … en base al promedio de los salarios ordinarios percibidos durante el tiempo trabajado en el año de que se trate. En la pequeña y mediana industria, artesanías, agricultura y ganadería en pequeña escala, el pago del Décimo Cuarto Mes de Salario se efectuará en base al promedio de los salarios mínimos percibidos durante el tiempo trabajado." Art. 7: "Para los trabajadores contratados por unidad de tiempo, cuyo salario sea diario, semanal, quincenal o mensual, el pago del Décimo Cuarto Mes de Salario, se hará en base a treinta (30) días, calculándose para ellos el promedio de los salarios ordinarios devengados durante el tiempo trabajado." Art. 8: "Para los trabajadores que laboran por unidad de obra (pieza, tarea, precio alzado o destajo), el pago del Décimo Cuarto Mes de Salario en base a treinta (30) días, calculado sobre el promedio de los salarios percibidos durante el período de que se trata." (Art. 6 dañado por run-on de impresión — reconstrucción entre paréntesis en la evidencia; cita recortada con …) | Acuerdo 02-95 Arts. 6-8: monthly-rated — computed on the average of the ORDINARY salaries received during the time worked in the year in question; for small and medium industry, artisanries, and small-scale agriculture and livestock, payment is made on the average of the MINIMUM salaries (SMM) received during the time worked; time-unit workers (daily/weekly/biweekly/monthly pay) — 30-day base computing the average of ordinary salaries earned; piece workers (pieza, tarea, precio alzado o destajo) — 30 days computed on the average of salaries received over the period. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 6-8 (p.2) (EV82:EVID-239) |
| LB-006 | Acuerdo 02-95, Arts. 9-10: Art. 9: "Si antes de cumplir el año, el trabajador renuncia o es despedido justificada o injustificadamente, el Décimo Cuarto Mes en concepto de compensación social, le será pagado proporcionalmente al tiempo trabajado." Art. 10: "Los anticipos que se hubieren dado al empleado o trabajador a cuenta del Décimo Cuarto Mes de Salario, serán deducibles al momento de hacer efectivo su pago." | Acuerdo 02-95 Arts. 9-10: if before completing the year the worker resigns or is dismissed with or without cause, the 14th Month is paid proportionally to time worked (no forfeiture); advances given on account of the 14th Month are deductible at the moment of payment. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 9 (p.2) y 10 (p.2) (EV82:EVID-239) |
| LB-007 | Acuerdo 02-95, Arts. 11-15: Art. 11: "Las personas naturales o jurídicas que al momento de entrar en vigencia el Decreto Legislativo Número 135-94 ya estuvieren pagando el Décimo Cuarto Mes, bajo ésta o cualquier otra denominación, no están obligadas más que a ajustarlo a las presentes disposiciones…"; Art. 13: "Los patronos que infrinjan, tergiversen o disminuyan lo prescrito en este Reglamento, serán sancionados con una multa que oscilará entre Cien a Cinco Mil Lempiras (L.100.00 a L.5,000.00)… La certificación que emita la indicada Secretaría de Estado tendrá carácter de título ejecutivo."; Art. 14: "Son nulos ipso-jure los actos o estipulaciones que impliquen renuncia, infracción, tergiversación o disminución de los derechos y obligaciones emanados del presente Reglamento."; Art. 15: "El primer pago del Décimo Cuarto Mes de Salario en concepto de compensación social se hará en forma proporcional, del veintiocho de octubre de mil novecientos noventa y cuatro, fecha en que entró en vigencia el Decreto Legislativo Número 135-94, al treinta de junio de mil novecientos noventa y cinco, sin perjuicio de lo establecido en el Artículo 5." | Acuerdo 02-95 Arts. 11-15: persons already paying a 14th month under this or any other name at vigencia need only align it to the regulation (subject to Art. 3 better terms); infringing/tergiversating/diminishing employers are fined L100.00-L5,000.00 and the STSS certification is an executive title; acts implying waiver or diminution are null ipso jure; the FIRST payment was proportional, from 28-oct-1994 (D. 135-94 vigencia) to 30-jun-1995. | `hn/sources/102_Acuerdo_02-95_Regl_14to_mes.pdf` | 02/95-Arts. 11-15 (pp.2-3) (EV82:EVID-240) |
| LB-008 | Ley del Salario Mínimo (D. 103), Art. 21-A (reformado por D. 43-97): "Se establece como un derecho a todos los empleados y trabajadores del sector público y privado que perciban hasta el equivalente de dos (2) salarios mínimos, el pago del BONO EDUCATIVO POR FAMILIA, el que hará efectivo una vez por año, después de la primera prueba trimestral de los educandos, como una compensación a los padres de los hijos en edad escolar, matriculados en los niveles de kínder, primaria y secundaria del país, consistirá en la cantidad de Quinientos Lempiras (L.500.00), incrementada en la misma proporción en que lo sea el salario mínimo y se pagará en la misma modalidad y condiciones en que se hace efectivo el Décimo Tercer Mes en concepto de Aguinaldo. En cuanto a la proporcionalidad para quienes no hubieren cumplido un (1) año de trabajar con el mismo patrono." + "El pago del bono no se computará como salario para el cálculo del pago de las prestaciones laborales ni para el pago del Décimo Tercer y Décimo Cuarto mes de salario." + "No se hará efectivo el pago del Bono, a los empleados y trabajadores que laboren en la pequeña y micro empresa, incluyendo las dedicadas a las actividades agropecuarias entendiéndose como tales aquellas en las que el número de trabajadores permanentes no exceda de quince (15)." | Minimum Wage Law (D. 103) Art. 21-A (reformed by D. 43-97, 28-abr-1997 per R-H43 — the print's "1977 [sic]" is a defect): all public- and private-sector employees earning up to the equivalent of 2 minimum wages have the right to the EDUCATION BONUS PER FAMILY, made effective once a year after the students' first trimestral exam, as compensation to parents of school-age children enrolled in kínder, primaria and secundaria; it consists of L500.00 (1997) increased in the same proportion as the minimum wage, and is paid in the same modality and conditions as the 13th Month (aguinaldo); proportionality applies to those with under 1 year with the same employer. The bonus is NOT computed as salary for severance (prestaciones) nor for the 13th/14th month; no bonus is payable to workers of small and micro enterprises, including agropecuary activities, i.e. those with no more than fifteen (15) permanent workers. | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` + `hn/sources/106_Gaceta_29320_D43-97_bono_educativo_Ac154-2000_reglamento_bono.pdf` | 103-Art. 21-A (pp.7-8); reforma D. 43-97 (R-H43); gazette original G 28,271 (EV82:EVID-218; EV106:EVID-375) |
| LB-009 | Ley del Salario Mínimo, Art. 21-B: "Durante el año de 1997, el Bono Educativo podrá hacer efectivo hasta en tres (3) cuotas mensuales." | Minimum Wage Law Art. 21-B: during 1997 only, the Education Bonus could be made effective in up to three (3) monthly installments — a 1997-only transition rule. | `hn/sources/104_Decreto_103_Ley_Salario_Minimo.pdf` | 103-Art. 21-B (p.8) (EV82:EVID-218) |
| LB-010 | DGS, "Tabla del Bono Educativo⅟ — Año 2026"; pie: "⅟En base a la Ley del Salario Mínimo y sus reformas, artículo 21-A del Decreto Número 43-97 de fecha 28 de abril de 1997, que establece el Bono Educativo." Bandas "De 16 a 20 / De 21 a 50 / De 51 a 150 / De 151 en adelante" × 11 ramas + "12 Empresas acogidas a la Ley de Zonas Libres — De 16 en adelante — 1,748.56" (matriz completa de 44 valores + fila ZL transcrita en §4; vigente Año 2026). | DGS (Dirección General de Salarios), "Education Bonus Table — Year 2026": amounts per rama × employer-size band (16-20 / 21-50 / 51-150 / 151 onward; the band floor 16 operationalizes the ≤15-workers exemption), plus a single zonas-libres row (L1,748.56); statutory basis footnote cites Art. 21-A of D. 43-97 dated 28-apr-1997 (the print supplying the correct year, R-H43). Full matrix transcribed in §4; amounts are present values of the L500-1997 × accumulated-SMM-increase formula — no per-cell derivation is published; values load as data. | `hn/sources/92_Tabla_Bono_Educativo_2026.pdf` | 92_ p.1 (EV82:EVID-229) |
| LB-011 | Código del Trabajo (D. 189-1959, impresión CEDIJ) — NEGATIVO: greps sobre todo el corpus del CT con 0 resultados para "aguinald*", "décimo tercer", "décimo cuarto"; CT-Art. 376: "Durante la vigencia del contrato el trabajador tiene derecho a percibir el salario, aún cuando no haya prestación del servicio por disposición o culpa del patrono." (Arts. 376-380 = reglas de salario, NO de aguinaldo.) | Labor Code negative finding: the CT contains NO aguinaldo, NO 13th/14th month, NO INVI, NO "salario integral", NO acoso provisions (R-H60) — Arts. 376-380 are salary rules, not bonus rules. The 13th month lives in special law only — **D. 112-1982 (105_, W5 — R-H74)**; the 14th month likewise (D. 135-94 Art. 34 / Acuerdo 02-95). [W4d's gloss "D. 135-94 (Ley del Aguinaldo)" was a CONFLATION — D. 135-94 = the 14th-month origin law; corrected R-H74/R-H75.] Never invent CT articles for these benefits. | `hn/sources/86_Codigo_del_Trabajo_TSC.pdf` | greps corpus-wide; CT-Arts. 376-380 (p.109) (EV85:EVID-327) |
| LB-012 | D. 117-2021 (interpretación auténtica del Art. 3 del D. 112-82, Ley del Séptimo Día y Décimo Tercer Mes en concepto de Aguinaldo), Art. 2: "cuando se hace referencia a que el pago del Séptimo Día y Décimo Tercer Mes en concepto de Aguinaldo, integran el concepto de salario para todos los efectos legales, es únicamente para efectos del cálculo y pago de prestaciones, derechos e indemnizaciones laborales, ésto quiero decir, que el Décimo Tercer Mes o Aguinaldo está exento del pago de todo impuesto, descuentos, cotizaciones y deducciones de cualquier naturaleza, salvo las relativas al cumplimiento de las obligaciones de prestar alimentos." ["ésto quiero decir" as printed] (vigencia = publication, 14-feb-2022) | Authentic interpretation (2022) of the 1982 aguinaldo law's salary clause: the séptimo día + 13th month integrate *salario* ONLY for computing labor benefits, rights and severances; the 13th month is exempt from EVERY tax, discount, social-security contribution and deduction of any nature EXCEPT alimony obligations. CONFLICT-flagged against Ley ISR Art. 10.h's 10-SMM-promedio cap (excess taxable — OQ-007, never resolved silently). [At V-HN1 this partially filled the D. 112-82 gap; the full text arrived as 105_ at W5 — the interp's dated rows now sit additively ON TOP of the 105_ originals (EVID-364).] | `hn/sources/89_Decreto_117-2021_interp_Art113_CT.pdf` | Art. 2 p.2 (EV89:EVID-335; vigencia EVID-336) |
| LB-013 | D. 112-1982 (Ley del Séptimo Día y Décimo Tercer Mes en Concepto de Aguinaldo), Arts. 1/3/9 + Art. 19 + cadena de fechas: Art. 3: "El pago del Séptimo Día y Décimo Tercer Mes integra el concepto de salario para todos los efectos legales." Art. 9: "Los trabajadores permanentes y jubilados y pensionados tendrán derecho al pago del décimo tercer mes, en concepto de aguinaldo." Art. 19: "La presente Ley entrará en vigencia a partir de la fecha de su publicación en el Diario Oficial 'La Gaceta'." (Dado 28-oct-1982; G 23,848 01-nov-1982 — **pin PRIMARY since W6: the gazette original is `113_`, masthead-confirmed; was secondary via 89_ cite**; fn.1: Art. 1 reformado por D. 179-97, G 28,441 17-dic-1997 — **reform content KNOWN since W6: `110_`, the jubilados/pensionados extension — OQ-008 resolved; see LB-020/LB-023**) | D. 112-1982 identity + 13th-month entitlement: permanent workers AND jubilados/pensionados are entitled — per the W6 originals: permanents ONLY 01-nov-1982→16-dic-1997 (original Arts. 1/9, `113_`), permanents + jubilados/pensionados from 17-dic-1997 (D. 179-97, `110_`); valid_from 1982-11-01 (primary gazette pin); Art. 3 = the salary-character clause D. 117-2021 authentically interpreted (pre-2022 wording = unlimited "para todos los efectos legales" — see LB-012/Fr-087 for the 2022 restriction rows). | `hn/sources/105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf` (+ `113_` original, `110_` reform) | 112-Arts. 1/3/9 (pp.1-2), Art. 19 + signatures (p.4), fn.1 (p.1) (EV105:EVID-362; EV105:EVID-363; EV105:EVID-364; EV110:EVID-394; EV110:EVID-396; EV110:EVID-397) |
| LB-014 | D. 112-1982, Arts. 10-11: Art. 10: "Los trabajadores permanentes que al 31 de diciembre de cada año no hayan cumplido 12 meses de servicios continuos con un mismo patrono, tendrán derecho al pago proporcional del décimo tercer mes en concepto de aguinaldo, de conformidad al tiempo trabajado. Para los efectos de esta Ley también se consideran trabajadores permanentes aquéllos a que se refiere el Artículo 347 del Código del Trabajo, quienes también recibirán el pago proporcional." Art. 11: "El décimo tercer mes en concepto de aguinaldo se pagará en el mes de diciembre de cada año; sin embargo, las partes podrán pactar dicha entrega en diferente fecha." ["proporcionar [sic]" corrected to "proporcional" in evidence] | 13th-month gate + timing: at each 31-december, workers with under 12 continuous months with the SAME employer take the proportional payment per time worked; CT-Art.-347-class permanents (irregular-work continuity) always get the proportional payment; default payment month = DECEMBER, displaced per-contract by pacto — the exact mirror of the 14th month's June gate (FR-056/057/059). | `hn/sources/105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf` | 112-Arts. 10-11 (pp.2-3) (EV105:EVID-368) |
| LB-015 | D. 112-1982, Art. 12 + fn.4 (interp D. 178-86 + re-interp D. 2-87; footnotes printed in near-spaceless run-on type — quotes normalize spacing, glyph-damaged words bracketed [?] in the evidence): Art. 12: "El décimo tercer mes en concepto de aguinaldo, se pagará calculando con base en el promedio de los salarios ordinarios percibidos durante el tiempo trabajado en el año de que se trate. En la pequeña y mediana industria, artesanía, agricultura y ganadería en pequeña y mediana escala, se pagará con base en el promedio de los salarios mínimos percibidos durante el tiempo trabajado." fn.4: "…Para los trabajadores que laboran por unidad de obra (pieza, tarea, precio alzado o destajo) el promedio del salario se obtendrá: a) Dividiendo la suma de los salarios devengados en el año de que se trate entre el total de días efectivamente trabajados… b) En el caso de que no hubiere trabajado todo el año, se aplicarán los Artículos 10 y 13… se exceptuarán a aquellos trabajadores a quienes convencionalmente o por costumbre se les haya reconocido la calidad de permanentes… Reinterpretado el inciso b) por Decreto 2-87… Gaceta No. 25,155 del 18 de febrero de 1987…" | 13th-month BASE: average of ORDINARY salaries over the time worked in the year; SMM-average variant for pequeña y mediana industria/artesanía/agricultura/ganadería (identical shape to the 14th-month FR-060/061; SMM rows imported from file 01 month-by-month across the calendar window); obra/piece workers = sum of salaries earned in the year ÷ days effectively worked; partial-year obra workers take Arts. 10/13 EXCEPT convention/custom permanents (full literal-a average). D. 178-86 interp of Art. 12 = G 25,077 17-nov-1986; its inciso b) re-interpreted by D. 2-87 (G 25,155 18-feb-1987; the print's given-date "30 de febrero de 1987" is impossible — OQ-009). | `hn/sources/105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf` | 112-Art. 12 + fn.4 (p.3) (EV105:EVID-369; EV105:EVID-370) |
| LB-016 | D. 112-1982, fn.3 (interp D. 178-86, G 25,077 17-nov-1986, sobre Arts. 9-10): "a) Todo Trabajador permanente tendrá derecho al 100 por ciento (100%) de pago de su aguinaldo si cumple el año de trabajo continuo o la proporción del mismo, si al 31 de diciembre no cumple 12 meses de servicios continuos con el mismo patrono. Es entendido que si mediante contratación colectiva los trabajadores hubieren logrado un porcentaje mayor del que establece la Ley, las empresas deberán cumplir lo pactado, pagando conforme lo negociado en el Contrato Colectivo; b) Para los trabajadores que laboran por unidad de tiempo, (semana, día u hora), cuyo salario sea semanal, quincenal o mensual, el décimo tercer mes en concepto de aguinaldo se hará en base a treinta (30) días. Tomándose como base el salario ordinario, entendiéndose como tal, el que se devenga en una jornada normal de trabajo…" | 100%-or-proportion rule (statutory interpretation with the same 31-dic same-employer gate); CBII better-percentage FLOOR (pay as negotiated where the collective contract achieved more); 30-day normalization for time-unit workers on ORDINARY salary = "el que se devenga en una jornada normal de trabajo" — identical to the 14th-month FR-062. | `hn/sources/105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf` | 112-fn.3 (p.2) (EV105:EVID-370) |
| LB-017 | D. 112-1982, Arts. 13-17: Art. 13: "El décimo tercer mes en concepto de aguinaldo, en casos de renuncia despido injustificado o justificado, será pagado proporcionalmente al tiempo que el trabajador haya laborado. Si se le hubiera dado un porcentaje anticipado se tomará en cuenta al momento del pago proporcional." Art. 16: "Los patronos que infrinjan, tergiversen o disminuyan el contenido de la presente Ley, serán sancionados con una multa que oscilará entre Cien Lempiras (L 100.00) a Cinco Mil Lempiras (L 5,000.00), tomando en consideración la capacidad económica de la empresa y la gravedad de la infracción…" | Exit proration for EVERY exit class (resignation, justified AND unjustified dismissal — no forfeiture); advances netted at the proportional settlement; closure metadata (STSS vigilance Art. 14; nullity of diminishing acts Art. 15; multa L100–L5,000 in 1982 nominals with no in-corpus adjustment — dated rows + never-guess; Art. 17 vivienda destination option). | `hn/sources/105_Decreto_112_Ley_Septimo_Dia_13er_Mes_Aguinaldo.pdf` | 112-Arts. 13-17 (pp.3-4) (EV105:EVID-371; EV105:EVID-372) |
| LB-018 | Reglamento STSS-154-2000 (Reglamento para el Pago del Bono Educativo; 5-oct-2000, gazette 6-nov-2000, vigencia = publicación): Art. 8: "Los empleados o trabajadores que laboren todo el año, comprendido del 01 de enero al 31 de diciembre con un mismo empleador, percibirán el CIEN POR CIENTO (100%) del Bono Educativo, y aquéllos que no laboren el año completo percibirán esta prestación en forma proporcional al tiempo trabajado." Art. 9: "Cuando un empleado o trabajador deje de laborar por cualquier causa con un empleador, sin haber percibido el pago del Bono Educativo por motivo de no haberse practicado la primera prueba bimestral o trimestral a los educandos, éste tendrá derecho a reclamarle con posterioridad su pago proporcional…" Art. 11 (ingreso posterior a la primera prueba): "…tendrá derecho a que se le pague el Bono Educativo en forma proporcional al tiempo que falte para concluir el año…" Art. 12: "Para computar el monto de los Salarios Mínimos… no se tomarán en cuenta las remuneraciones en concepto de horas extras trabajadas, primas, bonificaciones o gratificaciones." Art. 14 (ambos padres en el mismo centro de trabajo): "…se cumplirá la obligación otorgándole el pago de dicho bono [a] la madre si estuviere conviviendo, caso contrario… se le otorgará el Bono a quien tuviere los hijos…" Art. 15: "…más de una familia a su cargo, sólo tendrá derecho al [pago de un] Bono Educativo." Art. 16 (padres fallecidos → familiar/otra persona que labora, probando orfandad y manutención). [Restauraciones entre corchetes desde OCR;] | Bono reglamento mechanics (OQ-004 resolved): calendar-year 100% gate (01-01→31-12 same employer) with time-proportional fallback; post-exit claim right when the worker leaves before the first prueba; mid-year entrants AFTER the first prueba prorate FORWARD to year-end; the 2×SMM eligibility gate EXCLUDES OT, primas, bonificaciones and gratificaciones from the measured salary; family allocation (cohabiting → the mother; separated → whoever has the children; new-family right for the non-receiving parent; ONE bono per worker with multiple families; orphan-guardian right). | `hn/sources/106_Gaceta_29320_D43-97_bono_educativo_Ac154-2000_reglamento_bono.pdf` | 154/00-Arts. 8-12, 14-16 (pp.3-4); Arts. 3/5-7 (p.3); Arts. 17-21 (p.4) (EV106:EVID-376; EV106:EVID-377; EV106:EVID-378; EV106:EVID-379) |
| LB-019 | D. 43-97 (G 28,271, 29-may-1997; dado 28-abr-1997, vigencia = publicación), Art. 2 ( Arts. 21-A/21-B, original de gaceta): "…el pago del Bono Educativo por familia, el que se hará efectivo una vez por año, después de la primera prueba trimestral de los educandos… consistirá en la cantidad de QUINIENTOS LEMPIRAS (LPS. 500.00), incrementada en la misma proporción en que lo sea el salario mínimo y se pagará en la misma modalidad y condiciones en que se hace efectivo el Décimo Tercer Mes en concepto de Aguinaldo, en cuanto a la proporcionalidad para quienes no hubieren cumplido un año de trabajo con el mismo patrono…" + Reglamento Art. 3: "…sin considerar el número de hijos que se tengan estudiando."; Art. 5: "La cantidad de Quinientos Lempiras (Lps. 500.00)… se incrementa desde esa fecha [28-abr-1997], automáticamente, en la misma proporción en que se incrementa el salario mínimo de la respectiva actividad económica."; Art. 10 (pago en la fecha del sueldo o inmediato posterior a la primera prueba bimestral o trimestral, acreditado con documento del centro educativo). | Bono statutory ORIGINAL (gazette): the 21-A text as printed in G 28,271 ≡ the 104_ compilation print (R-H43 double-pinned; LB-008's source upgraded 104_ → 106_ with 104_ co-cite); the modality loan from the aguinaldo is scoped to PROPORTIONALITY ("en cuanto a la proporcionalidad…") — not the December timing; reglamento: one payment per family regardless of the number of children; L500-1997 auto-index from 28-abr-1997 (mechanism metadata only — amounts still load exclusively from the DGS tables per FR-076); payment timing = the payroll on/immediately after the first bimestral-or-trimestral prueba, school-documented. | `hn/sources/106_Gaceta_29320_D43-97_bono_educativo_Ac154-2000_reglamento_bono.pdf` | 43-97-Art. 2 (pp.1-2); 154/00-Arts. 3/5/10 (pp.3-4); fechas EVID-373 (EV106:EVID-375; EV106:EVID-376; EV106:EVID-377) |
| LB-020 | D. 179-97 (G 28,441, 17-dic-1997; Dado 16-oct-1997, Ejecútese 31-oct-1997, vigencia = publicación → 17-dic-1997), Art. 1: "Re[f]ormar los Artículos 1 y 9 del Decreto Número 112-82, que contiene la Ley del Séptimo Día y Décimo Tercer Mes en concepto de Aguinaldo, que en lo sucesivo se leerán así:" + reformed Art. 1: "Se reconoce el derecho de los trabajadores al pago del Séptimo Día. Los trabajadores permanentes y los jubilados y pensionados recibirán el pago del Décimo Tercer Mes en concepto de Aguinaldo. La presente Ley regula las modalidades y forma de aplicación de esta disposición." + reformed Art. 9 (same class extension); considerando: "…el beneficio del Treceavo Mes en concepto de aguinaldo navideño no se extiende en la misma forma hacia las personas en situación de jubilados tal como sucede con su similar el Catorceavo Mes…"; Art. 2: "Estas reformas no tendrán aplicación en aquellas instituciones donde tales beneficios se estén [o]torgando en iguales o mejores condiciones a las que establece la Ley en lo referente al pago del Décimo Tercer Mes en concepto de Aguinaldo," [Art. 2 as OCR-reconstructed, EVID-395] [OCR sidecar; accents normalized] | **THE 105_ OQ-1 RESOLVER (W6)**: D. 179-97's ONLY substantive change = adding "los jubilados y pensionados" to the 13th-month beneficiary class, in BOTH Arts. 1 and 9 (the chapter-placement quirk of Art. 1 is 1982 original drafting — EVID-397 — not a reform artifact). Considerandos corroborate: D. 135-94 Art. 34 Cap. IX = the 14th month already covering jubilados via D. 54-95 ("amplió la cobertura"). Art. 2 = non-regression floor (institutions/CBII already at equal-or-better keep their terms). Dating: beneficiary class = permanents 01-nov-1982→16-dic-1997; permanents + jubilados/pensionados from 17-dic-1997. | `hn/sources/110_Gaceta_28441_Decreto_179-97_reforma_Art1_aguinaldo.pdf` | 179-97-Art. 1 + reformed Arts. 1/9 + considerandos + Arts. 2-3 + date block (p.13) (EV110:EVID-392; EV110:EVID-393; EV110:EVID-394; EV110:EVID-395) |
| LB-021 | D. 178-86 (G 25,077, 17-nov-1986 masthead; Dado 31-oct-1986, vigencia = publicación → 17-nov-1986), Art. 1: "a) Todo trabajador permanente tendrá derecho al 100 por ciento del pago de su aguinaldo si cumple el año de trabajo contínuo o a la proporción del mismo, si al 31 de diciembre no cumple 12 meses de servicios contínuos con el mismo patrono… b) Para los trabajadores que laboran por unidad de tiempo, (semana, día u hora), cuyo salario sea semanal, quincenal o mensual, el décimo tercer mes en concepto de aguinaldo se hará en base a treinta días, tomándose como base el salario ordinario, entendiéndose como tal, el que se devenga en una jornada normal de trabajo; y, c) En la pequeña y mediana industria, artesanía, agricultura y ganadería en pequeña y mediana escala, el pago… se efectuará en base al salario mínimo establecido en la Zona, pagado durante el tiempo trabajado." + Art. 2 (obra ÷-days on SALARIO DIARIO) + Art. 3 (everything refers to Art.-1 permanents) [OCR sidecar; the a)-label print-damaged] | The interp ORIGINAL (W6, `111_`): content ≡ 105_ fn.3 transcription — now original-pinned; two structural upgrades: (i) Art. 2's formula computes the SALARIO DIARIO average (daily, then the 13th month builds on it); (ii) Art. 3 closes the whole interp to the Art.-1 permanents class. Refrendo quirk: Gobernación y Justicia (not Trabajo). | `hn/sources/111_Gaceta_25077_Decreto_178-86_interp_aguinaldo.pdf` | 178-86-Arts. 1-4 + date blocks (p.1) (EV110:EVID-401; EV110:EVID-402; EV110:EVID-403) |
| LB-022 | D. 2-87 (G 25,155, 18-feb-1987 masthead; **Dado 3-FEB-1987** — resolves 105_ OQ-3's impossible printed "30 de febrero de 1987"; Ejecútese 6-feb-1987; vigencia = publicación → 18-feb-1987), Art. 1: "Adicionar al Artículo 2, literal b) del Decreto Número 178-86, del 31 de octubre de 1986, que interpreta los Artículos 9, 10 y 12 del Decreto Número 112 del 28 de octubre de 1982, lo siguiente: …b) En el caso de que no se hubiere trabajado todo el año, se aplicarán los Artículos 10 y 13 del Decreto en referencia, pero en la aplicación del citado Artículo 10 se exceptuarán aquellos[g] trabajadores a quienes convencionalmente o por costumbres se les haya reconocido la calidad de permanentes, en el servicio sin consideración del número de días trabajados en el año, por lo que el Décimo Tercer Mes, en concepto de Aguinaldo se les pagará de conformidad a lo preceptuado en el literal a) de este Artículo…" + considerando: "las adiciones a la Ley tienen la misma vigencia que la Ley objeto de la adición" [OCR sidecar] | The re-interp ORIGINAL (W6, `112_`): the convention/custom-permanent class is EXCEPTED from Art. 10 proportionality → full literal-a average even in partial years. Adiciones-vigencia doctrine = same vigencia as the interpreted law. | `hn/sources/112_Gaceta_25155_Decreto_2-87_interp_aguinaldo.pdf` | 2-87-Art. 1 + considerandos + Art. 2 + date blocks (p.1; p.2 edition-mates out of scope) (EV110:EVID-404) |
| LB-023 | D. 112-1982 ORIGINAL gazette print (G 23,848, 01-nov-1982 masthead — the pin 89_ recited, now in-corpus PRIMARY; 2 pp complete; edition also carries Acuerdo 256-1982 Gobernación + Salud acuerdos 857-860): considerando: "…la Constitución de la República… dispone en el Artículo 128 numeral (10) que se reconoce el derecho de los trabajadores al pago del séptimo día y que los trabajadores permanentes recibirán además, el pago del décimo tercer mes en concepto de aguinaldo…" + ORIGINAL Art. 1: "Se reconoce el derecho de los trabajadores al pago del Séptimo Día. Los trabajadores permanentes recibirán además, el pago del Décimo Tercer Mes en concepto de aguinaldo. La presente Ley regula las modalidades y forma de aplicación de esta disposición." + ORIGINAL Art. 9 (permanents only) + Art. 18 TRANSITORIO: "En vista de la actual situación e[c]onómica del país, el pago del séptimo día se aplicará a partir del 1° de enero de 1983, y el pago del décimo tercer mes se hará del año en curso en adelante." [OCR sidecar; triple 300/400/600dpi-verified] | The ORIGINAL text (W6, `113_`) — pre-reform baseline: original Arts. 1/9 = permanentes ONLY (pins exactly what D. 179-97 changed in 1997); the compound Art. 1 (séptimo día + 13th month under "DEL PAGO DEL SÉPTIMO DÍA") existed from 1982; constitutional root = Constitución Art. 128 num. 10. **Art. 18 print variance (R-H80):** gazette reads "1° de enero de 1983" (ordinal primero — OCR "1+"/"1°" across three passes) vs the 105_ book extract's "10 de enero de 1983"; gazette = record per convention → séptimo-día transitory no-liability window 1982-11-01→1982-12-31 (was →1983-01-09); the book's "10" = typesetting slip of the ordinal "1°". 13th month owed from FY1982 ("del año en curso en adelante"). | `hn/sources/113_Gaceta_23848_Decreto_112-1982_aguinaldo_original.pdf` | 112-82-considerandos + Arts. 1/9/18-19 (pp.1-2) (EV110:EVID-396; EV110:EVID-397; EV110:EVID-399; EV110:EVID-400) |
| LB-024 | D. 135-94 ORIGINAL gazette print (La Gaceta 07-ene-1995, pp.10-23 of the issue; edition No. not printed in the file — 114_ OQ-1), Cap. IX "MEDIDAS DE COMPENSACION SOCIAL" Art. 34 (EVID-406 reconstruction, column-interleaved original — raw OCR in the evidence): "Establécese como un derecho a todos los empleados y trabajadores, el pago del Décimo Cuarto Mes de Salario, [el] que se [hará efecti]vo en [e]l mes de junio de [ca]da año, en [la misma modalidad y] [cond]iciones con [que se hace] efectivo [el] [Dé]cimo Tercer Mes en concepto de Aguinaldo. / El Poder Ejecutivo por medio de la Secretaría de Estado en [los D]espachos de **Trabajo y Previsión Social**, reglamentará [la presente disposición — object lost to column interleave]" + Art. 42 (vigencia): "El presente Decreto entrará en vigencia a partir de la fecha de su publicación en el Diario Oficial 'La Gaceta'…" [OCR sidecar; Art. 34 span column-interleaved — reconstruction cross-verified vs 102_'s embedded quote] | The 14th-month statutory ORIGINAL (W6, `114_`) — upgrades LB-005's source from quoted-in-102_ to the gazette original. Dado 12-oct-1994 pinned 4× (Anexo headers + Dado block) — 102_'s "1991 [sic]" finally closed with the original as direct LB. TWO divergences found, neither silently resolved: (i) delegation name = "Trabajo y **Previsión** Social" here vs 102_'s "Seguridad Social"; (ii) **vigencia CONFLICT (new OQ-012)**: Art. 42 = publication day (07-ene-1995) vs Acuerdo 02-95 Art. 15's "entró en vigencia 28-oct-1994" (the currently-encoded first-period anchor, FR-070). The law is also a major tax vehicle (ISV 7%/10% re-foundation, selectivo 20%, ISR interest 10% — all historical, EVID-405..414). | `hn/sources/114_Gaceta_1995-01-07_Decreto_135-94_Compensacion_Social.pdf` | 135-94-Cap. IX Art. 34 (p.9); Art. 42; Anexo headers; Dado block (EV114:EVID-406; EV114:EVID-414) |
| LB-025 | Congreso "Inventarios de Leyes" (official thematic law inventory, text-native PDF; Sub Sección 6.1 "Mapeo de la Legislación Nacional en Materia de Derecho Laboral"), entries 76-78 (p.281): "76. REGLAMENTO DEL DECIMO CUARTO MES DE SALARIO EN CONCEPTO DE COMPENSACIÓN SOCIAL. / 1995 Acuerdo No. 02-95. Gaceta No. 27,587 de 23/02/95 // 77. EXTENSIÓN DEL BENEFICIO DE PAGO DEL DECIMO CUARTO MES DE SALARIO A TODOS LOS JUBILADOS Y PENSIONADOS EN GENERAL. / 1995 Decreto Legislativo No. 54-95. Gaceta No. 27,639 de 28/04/95 // 78. INTERPRETACIÓN DEL ART. 34 DEL DECRETO No. 135-94 … EN EL SENTIDO DE QUE EL PAGO DEL DECIMO CUARTO MES DE SALARIO … A PARTIR DE 1995 DEBERA HACERSE EFECTIVO EN EL MES DE JUNIO DE CADA AÑO Y SERA DEL 100% DEL SALARIO SI A 30 DE JUNIO SE HA CUMPLIDO EL AÑO DE TRABAJO CONTINUO CON EL MISMO EMPLEADOR O LA PROPORCION DEL MISMO … / 1995 Decreto Legislativo No. 74-95. Gaceta No. 25,655 de 18/5/95" [inventory's "25,655" = digit slip for 27,655; gazette digits unreliable here — OQ-class caution] | **THE 102_ OQ-2 DECODER (W7, R-H81)**: pins the 1995 14th-month trio — Acuerdo 02-95 itself = G 27,587 23-feb-1995; **D. 54-95** = the jubilados/pensionados EXTENSION (G 27,639 28-abr-1995 — the book's "28,639" = digit-swap; monotonicity 27,587 < 27,639 < 27,655 arbitrates); **D. 74-95** = the Art.-34 INTERPRETATION (G 27,655 18-may-1995; the W4 extraction's "54-95" on this footnote = OCR misread, dual-dpi-fixed). Both decree texts remain unacquired (pre-ENAG gazettes) but their operative content is fully quoted in `102_`'s footnotes + here + `110_` considerandos (triple concordance). | `hn/sources/119_Congreso_Inventarios_de_Leyes.pdf` | Sub Sección 6.1 entries 76-78 (p.281) (EV119:EVID-429) |

## 3. Functional Requirements

### 3.1 P2 — 13th month (*aguinaldo*): statutory engine (D. 112-1982, `105_`)

**W5 UNBLOCK (R-H74):** the aguinaldo's statutory home was acquired as `105_`
(D. 112-1982 + its in-print interpretation chain D. 178-86 / D. 2-87 /
D. 36-90 + reform note D. 179-97). The former OQ-001 blocker is RESOLVED; the
W4d "D. 135-94 (Ley del Aguinaldo) + Acuerdo 201-96" framing was a CONFLATION
(D. 135-94 = the 14th-month origin law; the "Acuerdo 201-96" attribution was
unsourced — R-H75). Residual caveats carried as OQ-008/OQ-009: the D. 179-97
reform's content is unknown (Art. 1 rows reversible) and the gazette pin is
secondary (via 89_'s citation). FR-051/087 stand; FR-052..054 are REWRITTEN
from their config-gap form to the evidenced rules; FR-088..093 added from the
reserved range.

- **HN-PAYR-FR-051:** The system shall enforce the CT content-negative guard
  (R-H60): no aguinaldo/13th-month rule may be sourced from, or cited to, any
  Código del Trabajo article — the CT contains none, and CT Arts. 376-380 are
  salario rules — so the aguinaldo configuration surface shall expose NO
  CT-article source field for these benefits. (LB-011; EV85:EVID-327; R-H60)
- **HN-PAYR-FR-052:** The system shall model the aguinaldo entitlement per
  D. 112-1982 (valid_from 1982-11-01, **primary gazette pin — `113_` masthead,
  W6**) as DATED beneficiary-class rows: permanent workers (including the
  CT-Art.-347 irregular-work continuity class, who always receive the
  proportional payment) ONLY from 1982-11-01 through 1997-12-16 (original
  Arts. 1/9, `113_`); permanent workers AND jubilados y pensionados from
  1997-12-17 (D. 179-97, `110_` — the reform's entire substantive content;
  OQ-008 RESOLVED) — the jubilado/pensionado leg remaining a flagged
  pension-side edge class with no employer-contract context (OQ-010); the
  D. 179-97 Art. 2 non-regression floor (institutions already at
  equal-or-better conditions unaffected) rides as a config guard.
  (LB-013; LB-014; LB-020; LB-023; EV105:EVID-362; EV105:EVID-363;
  EV105:EVID-368; EV110:EVID-394; EV110:EVID-397)
- **HN-PAYR-FR-053:** The system shall implement the shared *modalidad del
  aguinaldo* parameter as ACTIVE with its borrowed-scope pinned from the
  gazette originals: the 14th month borrows the WHOLE modality ("en la misma
  modalidad y condiciones…"), while the bono educativo borrows it ONLY "en
  cuanto a la proporcionalidad para quienes no hubieren cumplido un año de
  trabajo" — the linkage surface is ONE parameter consumed by files 02 (P3/P4)
  with scope flags, never re-hardcoded per consumer.
  (LB-001; LB-008; LB-019; EV82:EVID-238; EV82:EVID-218; EV106:EVID-375)
- **HN-PAYR-FR-054:** The system shall default aguinaldo payment to the month
  of DECEMBER of each year (Art. 11), with an optional per-contract agreed
  payment date (*pacto en diferente fecha*) recorded as dated configuration
  displacing the December default for that contract only — mirroring FR-059;
  the ISR-side December settlement (taxation/04) is the tax feed, never the
  labor-law source. (LB-014; EV105:EVID-368)
- **HN-PAYR-FR-055:** The system shall expose the aguinaldo payment amount
  as a feed to the ISR plantilla engines of taxation/04 (annual gross
  HN-TAX-FR-126; 13th-month excess-only cap HN-TAX-FR-127) strictly by id
  consumption — this file supplies the amount, never the cap, the promedio,
  or any plantilla mechanics. (LB-013; EV105:EVID-364; EV82:EVID-238)
- **HN-PAYR-FR-087:** (added V-HN1 validation wave from the reserved
  087-100 range) The system shall encode the D. 117-2021 authentic
  interpretation of D. 112-82 Art. 3 as TWO dated interpretive rows
  (valid_from 2022-02-14, additive-only per D-H2): (a) *salary character* —
  the séptimo día and the 13th month integrate the concept of *salario*
  ONLY for the computation and payment of labor benefits, rights and
  severances (*prestaciones, derechos e indemnizaciones laborales*), never
  for other salary purposes; and (b) *aguinaldo immunity* — the 13th month
  is exempt from every tax, discount, social-security contribution
  (*cotización*) and deduction of any nature EXCEPT alimony
  (*prestación de alimentos*), which shall be the ONLY deduction line the
  aguinaldo payment surface accepts while the OQ-007 conflict is open; the
  ISR-side treatment is NOT changed by this row (the 10.h cap rows of
  taxation/02 + the plantilla caps of taxation/04 stand by id, conflict
  flag OQ-007), and the IHSS/RAP base leans ride their own files' OQs
  (payroll/03, payroll/05). (LB-012; EV89:EVID-335/336)
- **HN-PAYR-FR-088:** The system shall compute the aguinaldo base per
  Art. 12: the average of ORDINARY salaries (*salarios ordinarios*) received
  during the time worked in the calendar year of payment (ordinary-salary
  filter over the D-H3(b) monthly aggregates; non-ordinary items never enter
  the average), with the SMM-AVERAGE variant for *pequeña y mediana
  industria, artesanía, agricultura y ganadería en pequeña y mediana escala*
  — sourced exclusively as the imported dated SMM rows of file
  `01_smm-chassis.md` resolved month-by-month across the calendar window,
  never re-derived, never actual wages (shape-identical to FR-060/061).
  (LB-015; EV105:EVID-369)
- **HN-PAYR-FR-089:** The system shall normalize worker classes per the
  D. 178-86 interpretation block: time-unit workers (paid weekly, daily or
  hourly; weekly/quincenal/mensual salary) on a thirty (30)-day base over
  the ordinary-salary average ("el que se devenga en una jornada normal de
  trabajo"); obra/piece workers (*unidad de obra — pieza, tarea, precio
  alzado o destajo*) on the ÷-days formula (sum of salaries earned in the
  year ÷ days effectively worked), where partial-year obra workers take the
  Art. 10/13 proration EXCEPT convention/custom-recognized permanents, who
  receive the full literal-a average (their inciso-b) treatment itself
  re-interpreted by D. 2-87 — carried as an instrument-lineage row, content
  not in corpus, OQ-009). (LB-015; LB-016; EV105:EVID-369; EV105:EVID-370)
- **HN-PAYR-FR-090:** The system shall evaluate the 100%-vs-proportional
  gate at each 31-december: 100% when the worker has completed the
  continuous year of work with the same employer by that date, otherwise the
  proportion per time worked (Art. 10 + D. 178-86 a); and shall apply the
  CBII better-percentage floor — where collective contracting achieved a
  greater percentage, the negotiated percentage is paid (statutory
  computation = floor, never ceiling; same shape as FR-066).
  (LB-014; LB-016; EV105:EVID-368; EV105:EVID-370)
- **HN-PAYR-FR-091:** The system shall pay the aguinaldo PROPORTIONALLY to
  time worked on EVERY exit class — renuncia, despido justificado, despido
  injustificado (no exit class forfeits the accrued proportion) — and net
  any advances (*porcentaje anticipado*) against the exit settlement,
  recording gross, anticipos and net (shared ledger shape with FR-064/065).
  (LB-017; EV105:EVID-371)
- **HN-PAYR-FR-092:** The system shall record as informational legal-notes
  metadata (no sanction engine): STSS vigilance (Art. 14); ipso-nullity of
  diminishing acts/stipulations (Art. 15); the multa L100.00–L5,000.00 in
  1982-dated nominals with the adjustment-gap flag (never recomputed,
  never silently revalued — `105_ OQ-4`); and the Art. 17 fondo-social-de-
  la-vivienda destination option. (LB-017; EV105:EVID-372)
- **HN-PAYR-FR-093:** The system shall carry the aguinaldo instrument chain
  as dated provenance rows (additive-only, reversible): D. 112-1982
  (valid_from 1982-11-01, **PRIMARY gazette pin `113_` G 23,848 01-nov-1982 —
  was secondary via 89_**; séptimo-día transitory no-liability window
  1982-11-01→1982-12-31 per Art. 18 as gazette-read "1° de enero de 1983" —
  **R-H80**; the 105_ book print's "10 de enero" = typesetting slip of the
  ordinal "1°"); interp D. 178-86 (G 25,077, 17-nov-1986 — original `111_`);
  re-interp/adición D. 2-87 (G 25,155, 18-feb-1987; **Dado 3-feb-1987 —
  OQ-009(b) RESOLVED**; convention/custom-permanent exception); interp
  D. 36-90 (G 26,131, 11-may-1990 — séptimo-día side, consumed by file 06);
  reform D. 179-97 (G 28,441, 17-dic-1997 — **content KNOWN: the
  jubilados/pensionados extension to Arts. 1+9 + non-regression Art. 2,
  `110_` — OQ-008 RESOLVED**); D. 117-2021 (14-feb-2022, FR-087). The 14th
  month's origin D. 135-94 now also original-pinned (`114_`, gazetted
  07-ene-1995 — Dado 12-oct-1994 ×4; its vigencia-vs-Acuerdo-02-95-Art.-15
  conflict carried as OQ-012, never silently resolved).
  (LB-013; LB-020; LB-021; LB-022; LB-023; LB-024; EV105:EVID-362;
  EV105:EVID-365; EV105:EVID-370; EV110:EVID-392..EVID-404; EV114:EVID-406)

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
  (D. 74-95 interpretation — W7 re-attribution per R-H81; the instrument is
  D. 74-95 G 27,655 18-may-1995, NOT D. 54-95). (LB-002; LB-025;
  EV82:EVID-238; EV119:EVID-429)
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
  imported dated SMM rows of file `01_smm-chassis.md`
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
  vigencia per R-H44; the considerando's "1991 [sic]" is a print error —
  **now closed with the original: Dado 12-oct-1994 pinned 4× in `114_`,
  LB-024**) → 30-jun-1995, paid proportionally — as the
  proration-from-statutory-start pattern for any future regime cutover (new
  windows arise as dated rows, never in-place edits). **W6 FLAG (OQ-012,
  conflict carried):** `114_` Art. 42 sets D. 135-94 vigencia = publication
  day (07-ene-1995) vs Acuerdo 02-95 Art. 15's 28-oct-1994 — this row keeps
  the as-encoded 28-oct-1994 anchor until an instrument arbitrates; never a
  silent pick.
  (LB-007; LB-024; EV82:EVID-240; EV114:EVID-406; EV114:EVID-414; R-H44)
- **HN-PAYR-FR-071:** The system shall feed the June 14th-month payment to
  the ISR layer strictly as an amount consumed by id — the 14th enters the
  ISR annual gross only in the EXCESS above 10 × SMM *promedio*, per
  taxation/04 HN-TAX-FR-126 (annual gross) and HN-TAX-FR-128 (independent,
  excess-only cap, "en cada caso") — with the promedio feed owned by file
  `01_smm-chassis.md` (HN-PAYR-FR-001..040) and this file NEVER restating
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
- **HN-PAYR-FR-097:** (W7 gap-range 097-100) The system shall model the
  14th-month beneficiary class as DATED rows — all permanent employees and
  workers (Acuerdo 02-95 Art. 1, from the reglamento's vigencia) and, from
  28-abr-1995 (D. 54-95, G 27,639 — tacit reform of Art. 1), ALL
  jubilados y pensionados en general — mirroring FR-052's 13th-month
  structure; the jubilado/pensionado leg is a flagged pension-side edge class
  (same treatment as OQ-010: no employer-side computation is printed for it —
  the payer is the pension system unless the ex-employer voluntarily tops up).
  (LB-002; LB-025; EV82:EVID-238; EV119:EVID-429; R-H81)
### 3.3 P4 — *Bono educativo* (education bonus)

- **HN-PAYR-FR-073:** The system shall gate bono educativo eligibility on
  the worker perceiving up to the equivalent of two (2) applicable SMM —
  public and private sectors both — resolving the 2×SMM ceiling with the
  dated SMM rows of file `01_smm-chassis.md` (HN-PAYR-FR-001..040) as of
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
- **HN-PAYR-FR-094:** (W5, from the reserved range — Reglamento
  STSS-154-2000) The system shall evaluate the bono 100%-vs-proportional
  gate per the reglamento's CALENDAR-YEAR rule (its own instrument governs
  its gate — never the aguinaldo's 12-continuous-months formulation
  silently harmonized, OQ-011): 100% when the worker labors the whole year
  01-january→31-december with the same employer, else proportional to time
  worked; a worker who exits BEFORE the first prueba without receiving the
  bono retains a POST-EXIT CLAIM for the proportional amount against that
  employer; a worker entering AFTER the first prueba takes the proportional
  amount over the REMAINING year (forward proration), payable in the first
  payroll after that period on presentation of the school constancia.
  (LB-018; EV106:EVID-377)
- **HN-PAYR-FR-095:** (W5) The system shall compute the ≤2×SMM eligibility
  gate over a salary measure that EXCLUDES horas extras, primas,
  bonificaciones and gratificaciones (reglamento Art. 12 — a narrowing of
  FR-073's gate base, resolved with the same dated SMM rows), and shall
  implement the family-allocation matrix: both parents at the same
  obligated employer and cohabiting → the MOTHER is paid; separated →
  whoever has the children; a separated non-receiving parent forming a new
  family with studying children earns a bono at their own employer; ONE
  bono per worker even with multiple families at charge (per-worker
  singularity); deceased parents → the maintaining relative/person employed
  by an obligated employer, proving orphanhood and maintenance.
  (LB-018; EV106:EVID-378)
- **HN-PAYR-FR-096:** (W5) The system shall time bono payment to the
  payroll paid on or immediately after the first bimestral-or-trimestral
  prueba (the reglamento's widened trigger vs 21-A's "trimestral" — the
  procedural instrument governs), gated on the education-center document;
  and shall record as legal-notes metadata: the L500.00 base's
  auto-indexation from 28-abr-1997 per the respective activity's SMM
  increases (mechanism metadata only — amounts ALWAYS from the DGS rows,
  FR-076); the pre-existing-plan alignment duty with the CBII
  higher-amounts floor (reglamento Art. 13); Inspección General de Trabajo
  vigilance with the CT-625 multa reference (literal print-conflicted +
  prescription span damaged — informational only, never encoded,
  `106_ OQ-2`); nullity of waivers; and the reglamento provenance rows
  (valid_from 2000-11-06).
  (LB-018; LB-019; EV106:EVID-376; EV106:EVID-377; EV106:EVID-379)

## 4. Data Model

No CSV sidecar is allocated for this file: the bono 2026 matrix is transcribed
inline below (a future sidecar may be seeded from the DGS prints); all SMM /
promedio values are IMPORTED read-only from file
`01_smm-chassis.md` (HN-PAYR-FR-001..040).

**Aguinaldo engine (W5 unblock — D. 112-1982):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.payroll.aguinaldo.config (new, ACTIVE since 1982-11-01) | state, beneficiary_class, gate (31-dic 12m same-employer), payment_month (default december), pacto_date, base_variant (ordinary_average · smm_average), cbii_floor_flag, instrument_chain | char/select/date/boolean | beneficiary_class: permanent (+CT-347 class always proportional) · jubilado_pensionado (pension-side flag, OQ-010); base_variant class = pequeña y mediana industria · artesanía · agricultura y ganadería; chain rows: D.112-82 → D.178-86 → D.2-87 → D.36-90 → D.179-97(content OQ-008) → D.117-2021 | FR-052..FR-054, FR-088..FR-090, FR-093 |
| l10n_hn.payroll.aguinaldo.settlement (new) | employee, contract, year, gate_outcome (full · proportional), time_worked_factor, base (ordinary avg / 30-day / ÷-days obra), gross_amount, anticipos, net_amount, snapshot | m2o/int/select/monetary | December (or pacto) settlement trace; snapshot resolved SMM vintages/rows on write (D15) | FR-088..FR-091 |
| hr.payslip (termination run) | aguinaldo_exit_proportional line | monetary | proportional payout on any exit class + anticipo netting | FR-091 |
| hr.salary.rule (aguinaldo lines) | integrates_salario (prestaciones-only per FR-087), allowed_deductions = alimony-only (while OQ-007 open) | boolean | FR-087 consumption tags | FR-087 |
| l10n_hn.legal.note (metadata) | multa L100.00-L5,000 (1982 nominals, adjustment-gap) · STSS vigilance · nullity · vivienda option | char | informational only | FR-092 |

**14th-month engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.contract | 14m_entitlement_year_start/end (derived), 14m_payment_month (default june), 14m_pacto_date, smm_average_variant (boolean) | date/select/date/boolean | entitlement year 1-jul→30-jun per continuous contract; variant for pequeña y mediana industria · artesanías · agricultura y ganadería en pequeña escala | FR-056, FR-059, FR-061 |
| l10n_hn.payroll.14m.config (new, dated rows) | valid_from, beneficiary_class (permanent_all · +jubilados_pensionados), instrument (02-95 Art. 1 · D. 54-95 tacit reform) | date/select/char | 14th-month beneficiary class dated rows: permanents from the reglamento's vigencia; +jubilados/pensionados en general from 1995-04-28 (D. 54-95, G 27,639 — R-H81); pension-side leg flagged, no employer-side computation printed | FR-058, FR-097 |
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
| l10n_hn.payroll.bono.gate (new, W5) | calendar_year_gate (01-01→31-12 same employer), exit_claim_pending, midyear_entry_mode (forward proration), gate_salary_exclusions (OT · primas · bonificaciones · gratificaciones), family_allocation (cohabiting_mother · separated_custody · new_family · orphan_guardian), per_worker_cap | boolean/char/select | reglamento STSS-154-2000 mechanics; gate measure excludes the Art.-12 list | FR-094, FR-095 |
| l10n_hn.payroll.bono.claim (new, W5) | employee, employer, exit_date, proportional_amount, status (pending · paid) | m2o/date/monetary/select | post-exit claim ledger (exit before the first prueba) | FR-094 |
| l10n_hn.legal.note (metadata) | D. 43-97 28-abr-1997, G 28,271 29-may-1997 (R-H43) + Reglamento STSS-154-2000, gazette 6-nov-2000 (valid_from 2000-11-06) | char | provenance on bono config | FR-083, FR-096 |

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
| FR-051..FR-055 | odoo | l10n_hn.payroll.aguinaldo.config (new, ACTIVE W5) + hr.salary.rule | entitlement/gate/December+pacto + ISR feed | W5 unblock (R-H74): D. 112-1982 dated rows from 1982-11-01; D15/D16: chain instruments arrive as additive dated rows; CT-source field absent by design (R-H60); residual caveats OQ-008/OQ-009 |
| FR-088..FR-093 | odoo | l10n_hn.payroll.aguinaldo.settlement + hr.salary.rule + SMM import (file 01) + l10n_hn.legal.note | averages/30-day/÷-days bases, gate+CBII floor, exit+anticipo, chain provenance | D15: gate resolved at the December payslip period, snapshot on write; SMM vintages resolve month-by-month across the calendar window (FR-088 variant); corrections recompute with original-period rows; D12: D. 179-97 + D. 2-87 content leads (OQ-008/OQ-009) |
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
| FR-077 | odoo | shared modality parameter (FR-053 surface) | scope-pinned linkage (W5) | bono borrows the aguinaldo modality ONLY for proportionality (LB-019 scope note); aguinaldo side now ACTIVE per D. 112 |
| FR-094..FR-096 | odoo | l10n_hn.payroll.bono.gate + l10n_hn.payroll.bono.claim + l10n_hn.legal.note | calendar-year gate, exit claims, family allocation, timing | W5 (Reglamento STSS-154-2000): gate measure excludes OT/primas/bonificaciones/gratificaciones; CT-625 literal + prescription span left unencoded (106_ OQ-2) |
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

- **AC-001:** Given a December 2026 payroll run with the aguinaldo engine
  active (D. 112-1982 rows since 1982-11-01), then aguinaldo lines compute on
  the evidenced rules — and the aguinaldo rule's source dropdown offers no
  CT article (FR-051, FR-052; W5 rewrite of the former blocked-state AC).
- **AC-002:** Given the shared modality parameter ACTIVE with scope flags,
  then the June 14th-month settlement borrows the FULL aguinaldo modality
  while the bono borrows proportionality only — never the December timing
  (FR-053, FR-077; W5 rewrite of the former blocked-state AC).
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
- **AC-018:** Given an aguinaldo settlement for a worker hired 01-mar-2026
  (10 months at 31-dic-2026) with 30-day-base ordinary average L600.00/day,
  then the December 2026 payment = 10/12 × 30 × 600.00 = L15,000.00; given a
  worker with the full continuous year, then 100% = 30 × 600.00 = L18,000.00,
  raised to the CBII percentage where the collective pact grants more
  (FR-089, FR-090).
- **AC-019:** Given an obra worker who earned L72,000.00 over 240 days
  effectively worked in 2026, then the aguinaldo base = 72,000.00 ÷ 240 =
  L300.00/day → 30-day settlement L9,000.00 (FR-089).
- **AC-020:** Given a worker who exits 15-sep-2026 before the first prueba
  with 8.5 months worked, then a pending post-exit bono claim for the
  proportional amount (8.5/12 × the DGS row) registers against the employer;
  given a worker hired 01-aug-2026 (after the first prueba), then the bono
  prorates FORWARD over Sep-Dec (4/12), never over the elapsed year
  (FR-094).
- **AC-021:** Given a worker earning L13,500.00 monthly ordinary salary plus
  L2,000.00 OT and a L1,000.00 bonificación, then the bono ≤2×SMM gate
  measures L13,500.00 ONLY (exclusions applied); given both parents working
  at the same obligated employer and cohabiting, then the MOTHER's payroll
  carries the bono line (FR-095).
- **AC-022:** Given the 14m beneficiary-class config resolved for a
  settlement dated 1995-06-30, then the class row = +jubilados_pensionados
  (D. 54-95 in force since 28-abr-1995) with the pension-side leg flagged
  no-employer-computation; given a settlement dated 1994-06-30, then the row =
  permanent_all (extension not yet in force) — dated-row flip, never in-place
  edits (FR-097).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `EV85:86_ OQ-3` → **RESOLVED at W5 via R-H74/R-H75**: the aguinaldo's statutory home = **D. 112-1982, acquired as `105_`** (entitlement/gate/base/December/exit all LB'd — FR-052/054/088..091). The former framing ("D. 135-94 (Ley del Aguinaldo) + reglamento Acuerdo 201-96") was a CONFLATION: D. 135-94 = the 14th-month origin law (Cap. IX Art. 34); "Acuerdo 201-96" was an unsourced attribution — the REAL interpretation chain is D. 178-86/D. 2-87/D. 36-90 + reform D. 179-97 (105_ footnotes). Residuals carried as OQ-008/OQ-009. | was yes (P2) — RESOLVED | controller (W5) | resolved |
| OQ-002 | `EV82:102_ OQ-2` → **RESOLVED at W7 (R-H81, `119_` EVID-429 + dual-dpi re-read of 102_)**: the "two conflicting D. 54-95 citations" decode as **TWO different decrees** — the Art.-34 interp footnote prints **D. 74-95** (dado 25-abr-1995, G 27,655 18-may-1995; the W4 extraction misread 74→54 — fixed in LB-002/EVID-238), while the Art.-1 tacit-reform footnote's **D. 54-95** (dado 28-mar-1995) = the jubilados/pensionados extension, gazette **G 27,639 del 28-abr-1995** (congreso inventory; the book's "28,639" = digit-swap — monotonicity 27,587@23-feb < 27,639@28-abr < 27,655@18-may arbitrates; 28,6xx = 1997-class). FR-057 re-attributed to D. 74-95; FR-097 encodes the extension. Residual: both decree TEXTS unacquired (pre-ENAG gazettes) — operative content fully evidenced via triple-concordant official quotes. | no (rows as-encoded + FR-097) | controller (W7) | resolved |
| OQ-003 | `EV82:102_ OQ-3` — 102_ is a scanned compilation extract (pp. 247-249) with word run-ons; reconstructions bracketed/[?] in the evidence. Re-OCR at 400dpi/PSM 6 if verbatim-critical quoting is needed before freezing LB-005 text. | no | extraction queue | open |
| OQ-004 | `EV82:92_ OQ-1` → **RESOLVED at W5**: the bono reglamento = **Acuerdo STSS-154-2000, IN CORPUS as the second extract of `106_`** (gazette 6-nov-2000) — read end-to-end, mechanics encoded FR-094..096. Residual (kept open, non-blocking): no 2027 bono table in corpus (expected with the 2027 SMM cycle) — FR-084 still blocks that year's runs. | no | controller (W5) | resolved (2027-table residual open) |
| OQ-005 | `EV82:92_ OQ-2` — eligibility parameters live in Art. 21-A, NOT in the DGS table (amounts only); the 16-20 band floor is the table-side echo of the ≤15 exemption (16 = first non-excluded count) — consistent but unstated; encoded as the FR-085 source guard. | no | Takumi S-HN4 | open (encoded) |
| OQ-006 | `EV82:102_ OQ-1` → RESOLVED at synthesis via R-H44: the considerando's "12 de Octubre de 1991 [sic]" is a print error; D. 135-94 = 1994, vigencia 28-oct-1994 (per Art. 15; the 8-month first period is coherent only for 1994). Encoded in FR-070. No further action. | no | — | resolved |
| OQ-007 | `EV89:89_ OQ-1` (V-HN1) — CONFLICT, never resolve silently: D. 117-2021 Art. 2 ("el Décimo Tercer Mes o Aguinaldo está exento del pago de todo impuesto...") vs Ley ISR Art. 10.h (13th month exempt only up to 10 SMM promedio, excess taxable — `01_` EVID-006; plantilla `11_` implements the caps). Later-in-time authentic interpretation of a DIFFERENT statute (D. 112-82, 1982 — NOW IN CORPUS as 105_, W5) against the ISR's express cap regime. Current encoded rows STAND (FR-087(b) ships the immunity as a conflict-flagged interpretive row; the ISR-side caps of taxation/02/04 are untouched); resolution requires a hierarchy ruling, then a dated-row flip, never code. Related leans: IHSS base composition (payroll/03 OQ, statutory lean = 13th month OUT of cotización base), RAP/fondo "salario ordinario" base (payroll/05 OQ-1 lean), CT Art. 95.12-13/60-A mandatory union/coop deductions vs "deducciones de cualquier naturaleza, salvo... alimentos" (`EV89:89_ OQ-3`, payroll/10 flag). | no (ISR rows stand; immunity row conflict-flagged) | controller ruling | open |
| OQ-008 | `EV105:105_ OQ-1` (W5) → **RESOLVED at W6**: D. 179-97 acquired as `110_` (G 28,441 17-dic-1997) — the reform = Arts. 1 AND 9, adding "los jubilados y pensionados" to the beneficiary class, NOTHING else; the chapter-placement quirk is 1982 original drafting (`113_` original Art. 1 — compound text pre-reform, EVID-397); non-regression Art. 2. Beneficiary-class rows now DATED (permanents-only 1982-11-01→1997-12-16; +jubilados/pensionados from 1997-12-17 — FR-052, LB-020/LB-023); reversibility caveat LIFTED. | no | controller (W6) | resolved |
| OQ-009 | `EV105:105_ OQ-2/OQ-3` (W5) → **RESOLVED at W6**: (a) the gazette pin is now PRIMARY — `113_` = the G 23,848 original print, masthead-confirmed 01-nov-1982 (EVID-396); (b) D. 2-87 acquired as `112_` — Dado **3-feb-1987** (the book-print's "30-feb-1987" = print error), Ejecútese 6-feb-1987, and its content IS in corpus (the convention/custom-permanent adición, EVID-404). | no | controller (W6) | resolved |
| OQ-010 | `EV105:105_ OQ-5` (W5) — jubilados/pensionados 13th-month entitlement (Arts. 1/9): no payer-side mechanism in the print (pension system vs prior patrono); kept as a flagged pension-side edge class, no employer-side FR. | no | controller (parked) | open (parked) |
| OQ-011 | `EV106:106_ OQ-3` (W5) — bono gate formulation divergence: reglamento Art. 8 = CALENDAR year (01-01→31-12 same employer) vs the aguinaldo's 12-continuous-months-at-31-dic gate (D. 112 Art. 10) that Art. 21-A's modality loan references — coincident for full-year workers, different proration anchors for partial years. Encoded as the bono's own calendar-year rule (FR-094); flag stands so nobody "harmonizes" them silently. Also carried: reglamento Art. 18's CT-625 literal print conflict + Art. 19's damaged prescription span (`106_ OQ-2` — never encoded). | no | controller (encoded) | open (encoded) |
| OQ-012 | `EV114:114_ OQ-2` (W6, CONFLICT — never resolve silently): D. 135-94's OWN vigencia clause (Art. 42) = publication day → **07-ene-1995**, vs Acuerdo 02-95 Art. 15's assertion that D. 135-94 "entró en vigencia" **28-oct-1994** (the Ejecútese date — currently encoded as the 14th-month first-period anchor, FR-070/OQ-006). Corroborating anomaly: the decree's own 1994-dated windows (Arts. 21/30/35) were moot at 07-ene-1995 publication. Affects the 14th-month accrual-start row (valid_from 28-oct-1994 vs 07-ene-1995); rows stay as-encoded until another instrument arbitrates. **W7: D. 54-95's content is now pinned (extension-only, `119_` EVID-429) and does NOT recite D. 135-94's vigencia — no arbitration; conflict stands.** | no (rows as-encoded) | controller ruling | open |
| OQ-013 | `EV110:113_ OQ-1` (W6) → RESOLVED by ruling **R-H80**: Art. 18 transitory séptimo-día start — gazette `113_` reads "1° de enero de 1983" (ordinal primero; OCR "1+"/"1°" consistent across 300/400/600dpi passes) vs 105_ book extract's "10 de enero de 1983". Gazette = record → no-liability window ends 1982-12-31; the book's "10" = typesetting slip of "1°". Encoded in FR-093/LB-023. | no | controller (W6, R-H80) | resolved |
