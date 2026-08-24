# SV — Taxation — IVA pro-rata and remanente: the Art. 66 proportionality engine, the Arts. 67-70 credit-excess regime and the Quincena-25 tercerización closure (Ley IVA Arts. 66-70; Rgto. Arts. 24-25; D.L. 499-2026 + MH guía 67_)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller; W24 T3 fold-in (108_ proveedores-locales Art. 66 exception) |
| Updated | 2026-08-24 |

## 1. Purpose

This file defines the functional requirements for the proportionality and
credit-excess tail of El Salvador's IVA (D.L. 296-1992): the Art. 66
*proporcionalidad* engine — the monthly factor (gravadas operations ÷ the
sum of gravadas + exentas + no sujetas) that scales the deductible crédito
fiscal of a mixed period; the ACCUMULATED base of following periods
(operations accumulated from the FIRST period in which the proportionality
was applied through the *término del ejercicio comercial* — fiscal-year end
— even where only gravadas operations follow); the NEXT-JANUARY
redistribution — in the first month of the following commercial exercise a
recalculation with the cumulative values of the PRIOR exercise's gravadas/
exentas/no-sujetas operations, redistributing the crédito fiscal so that a
superior recalculated credit SUMS its difference to the crédito of the
first period of the following exercise and an inferior one SUBTRACTS from
it; the record-conservation/exhibition duty (CT term, DGII on requirement);
the denominator EXCLUSIONS (no-sujeta operations of NON-HABITUAL activities
lacking attributable credits; donations of goods/services per the final
incisos of Arts. 11/16 to the ISR-Art.-6 institutions; sales to misiones
diplomáticas, consulares, international organizations and their accredited
members when declared exentas or no sujetas under international instruments
subscribed AND RATIFIED by El Salvador — stamp 13); the statutory
*operaciones no sujetas* definition (operations not expressly previsto as
exenciones that fall outside the hechos generadores, plus operations the
law expressly declares no sujetas); and the costo-o-gasto tail — the
crédito proportion corresponding to exentas and no-sujetas operations forms
part of the COST OR EXPENSE as corresponds (the F-07 pro-rata casillas
132/133/134 feed's legal root, cited by id). It also carries the
QUINCENA-25 TERCERIZACIÓN closure: the D.L. 499 (66_) pass-through
obligation — the *tercerizador* contractor emits the separate documento
fiscal as a *Factura de Consumidor Final, con valor exento* and presents
the planilla copy — and the guía 67_ ruling that per "la parte primera del
inciso sexto del artículo 66" the crédito-fiscal proportionality is NOT
applied for that operation (pre-D.L.-224-2009 inciso numbering; current
print mapping = the no-habitual exclusion — R30(c) working reading,
OQ-tracked; closes `taxation/02_isr-deductions.md` OQ-009 by pointer). And
it owns the Arts. 67-70 remanente regime: the indefinite carryforward of
the credit excess (summed to the crédito of the following or successive
periods *hasta su deducción total*, with the Rgto. Art. 24 remanente
definition); the Art. 68 cessation lock (no devolución, no reintegro, no
offset against other tax debts, no transfer — save Art. 69); the Art. 69
non-transferability of the credit-deduction right (proper to each
contribuyente) with its TWO exceptions — the continuador de otro por
mandato legal and the fusión/absorción where the nueva or subsistente
society CONTINUES the giro of the primitives, inheriting their remanente —
and the four hard bars (liquidation: no refund; universal
activo-y-pasivo aport: no right for the receptora; vinculados
económicamente: no traspaso; herederos: no use); and the Art. 70
never-cost rule (the tax paid or caused is never a cost of goods/services
acquired, imported or used — SAVE final use or consumption, exempt
operations or excluded subjects — and never an ISR-deductible gasto),
mirrored by Rgto. Art. 25 (credit-forming IVA out of cost save
exempt/no-gravada destinations; credit unusable by the Art. 66
proportionality or by the término/cese de actividades passes to constitute
a GASTO GENERAL).

It does **not** cover: the débito/crédito determination arithmetic and the
Arts. 62-63 adjustment machinery (Arts. 62-64 — the adjustments/assets
file of this wave owns them; this file consumes the period's crédito and
débito totals as inputs); the credit-eligibility gates and blocked states
that feed the pro-rata base (`10_iva-credit-deductibility.md`
SV-TAX-FR-251..268 — the eligible crédito of the period is T4's engine
output, consumed by id; FR-268's blocked→cost reclassification is the
mirror this file's Art. 66/70 rows co-cite); the operation classification
itself (gravada/exenta/no-sujeta tagging — `07_iva-framework.md`
SV-TAX-FR-176 operation taxonomy and `08_iva-exemptions.md`
SV-TAX-FR-206/224 exemption classification, consumed by id); the rate rows
(`09_iva-base-rate.md` — never needed here: the factor is a ratio of
operation VALUES, never of tax amounts); the F-07 casilla graph
(`fiscal-reporting/01_f07-declaration.md` SV-FREP-FR-012/014/015/026 own
casillas 132-134, the 145 formula, the 155/160 split and the 155→110
carryforward — this file is the named producer of the 132-134 inputs,
cited by id); the export-credit offsets and the reintegro regime (Arts.
76-77 — the exports/refunds file of this wave); the Quincena-25 payroll
and ISR surfaces (`payroll/08_isr-interfaces.md` SV-PAY-FR-142 seven-field
ledger consumed by id; `taxation/02_isr-deductions.md` SV-TAX-FR-173..175
own the ISR side); DTE emission mechanics (the e-invoicing stack — the
type-01 FE consumer document is cited by id via SV-EINV-FR-001); and the
CT prescription/conservation term books (the CT term the record duty
references is a fiscal-books surface, consumed by id when it exists).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). **SOQ-54 vintage note (rides every 01_/02_ LB in this
file):** the consolidation's last reform stamp is D.L. 71-2015 —
post-2015 reforms unverified; corpus-internal signals negative (DTE
stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual silent);
re-verify at implementation. **Reglamento = 02_ survivors only** (D.E.
83-1992 consolidated through D.E. 60-1993/10-1996/**117-2001**; the mass
repeal = D.E. 117-2001 stamp (3) — R30(a)); survivor articles = 1-10,
16-30, 50-51 (+ 52 vigencia); this file cites Rgto. Arts. 24 and 25 —
both survivors. **Third source class (tercerización rows only):** D.L.
499 (Ley Especial Quincena Veinticinco, 66_; 14-ene-2026, D.O. N° 8
T.450 same day, effective on publication) and the DGII guía 67_
(MH.UVI.DGII/006.001/2026, 21-ene-2026) — both official-DGII OCR'd scans
(quote fidelity is to the extraction, not to a text layer; the 66_ OCR
misses accents, e.g. "debera" [sic]). **R30(c) ruling (binding on
LB-008):** the guía's citation "la parte primera del inciso sexto del
artículo 66" uses PRE-D.L.-224-2009 inciso numbering; in the current
print of Art. 66 the corresponding exclusion is the "SI NO EXISTEN
CRÉDITOS FISCALES ATRIBUIBLES..." inciso — no-sujeta operations of
non-habitual activities without attributable credits (LB-002; R30(c)
calls it the fifth printed inciso, this file counts it sixth — ordinal
noted in OQ-2, substance identical); the mapping is a working reading,
OQ-tracked (OQ-2).
**CT re-anchor:** the record-conservation duty's "PLAZO QUE ESTABLECE EL
CÓDIGO TRIBUTARIO" anchors on the CT books/preservation regime (D.L.
230/00 re-anchor family) — the term itself is never restated here.
**V1 citation rule:** every LB row below cites its source with the EVID
id and the locator (txt page anchors `=== PAGE n ===` of
`01_Ley_IVA.pdf.txt` / `02_Reglamento_IVA.pdf.txt` verified this task;
the 66_/67_ rows cite the extraction EVID ids — no txt layer exists);
the SOQ-54 watch rides all of them.

| LB | ID | Citation (Spanish) | English translation | Source file | Location |
|----|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA, Art. 66, incisos 1º-4º (factor; accumulated base; January recalc; redistribution) | "SI LAS OPERACIONES REALIZADAS EN UN PERIODO TRIBUTARIO SON EN PARTE GRAVADAS, EN PARTE EXENTAS O EN PARTE NO SUJETAS; EL CRÉDITO FISCAL A DEDUCIRSE DEL DÉBITO FISCAL, SE ESTABLECERÁ CON BASE A UN FACTOR QUE SE DETERMINARÁ DIVIDIENDO LAS OPERACIONES GRAVADAS REALIZADAS EN EL PERÍODO TRIBUTARIO ENTRE LA SUMATORIA DE LAS OPERACIONES GRAVADAS, EXENTAS Y LAS NO SUJETAS REALIZADAS EN DICHO PERÍODO, DEBIENDO DEDUCIRSE ÚNICAMENTE LA PROPORCIÓN RESULTANTE DE APLICAR DICHO FACTOR AL CRÉDITO FISCAL DEL PERÍODO TRIBUTARIO. (8)" — "EN LOS PERÍODOS TRIBUTARIOS SIGUIENTES LA PROPORCIÓN DEL CRÉDITO FISCAL SE DETERMINARÁ APLICANDO EL PROCEDIMIENTO ANTERIOR SOBRE LA BASE DE LAS OPERACIONES ACUMULADAS DESDE EL PRIMER PERÍODO EN QUE SE APLICÓ LA PROPORCIONALIDAD, AÚN CUANDO SÓLO TUVIERE OPERACIONES GRAVADAS, Y HASTA EL TÉRMINO DEL EJERCICIO COMERCIAL. (8)" — "CUANDO ESTA NORMA SE HAYA APLICADO DURANTE UN EJERCICIO COMERCIAL, EN EL PRIMER MES DEL EJERCICIO COMERCIAL SIGUIENTE, SE DEBERÁ HACER UN RECÁLCULO DE LA PROPORCIONALIDAD CON LOS VALORES ACUMULATIVOS DE LAS OPERACIONES GRAVADAS, EXENTAS Y NO SUJETAS REALIZADAS EN EL EJERCICIO COMERCIAL ANTERIOR, Y SE REDISTRIBUIRÁ EL CRÉDITO FISCAL. (8)" — "SI EL CRÉDITO FISCAL QUE DEBIÓ DEDUCIRSE RESULTA SER SUPERIOR AL EFECTIVAMENTE DEDUCIDO, LA DIFERENCIA SE SUMARÁ AL CRÉDITO FISCAL CORRESPONDIENTE AL PRIMER PERÍODO TRIBUTARIO DEL EJERCICIO COMERCIAL SIGUIENTE Y SI RESULTARE INFERIOR, SE RESTARÁ DEL CRÉDITO FISCAL DE ESE PERÍODO. (8)" | Where the operations of a tax period are in part gravadas, in part exentas or in part no sujetas, the crédito fiscal deductible from the débito fiscal is established by a FACTOR determined by dividing the gravadas operations of the period by the SUM of the gravadas, exentas and no sujetas operations of that period, deducting ONLY the proportion resulting from applying that factor to the period's crédito fiscal; in FOLLOWING periods the proportion is determined by the same procedure over the ACCUMULATED operations from the first period in which the proportionality was applied — even if it had only gravadas operations — until the end of the commercial exercise; once the norm has applied during a commercial exercise, in the FIRST MONTH of the following exercise a RECALCULATION is made with the cumulative values of the gravadas/exentas/no-sujetas operations of the PRIOR exercise and the crédito fiscal is REDISTRIBUTED; if the credit that should have been deducted turns out SUPERIOR to that effectively deducted, the difference is SUMMED to the crédito of the first period of the following exercise, and if INFERIOR, it is SUBTRACTED from that period's credit | `sv/sources/01_Ley_IVA.pdf` | Art. 66 incisos 1º-4º pp.34-35 (EVID-324; verified 01_ txt lines 1258-1283, PAGE 34-35) |
| LB-002 | Ley IVA, Art. 66, incisos 5º-6º (record conservation; denominator exclusions) | "EL CONTRIBUYENTE DEBERÁ CONSERVAR DURANTE EL PLAZO QUE ESTABLECE EL CÓDIGO TRIBUTARIO, LOS REGISTROS QUE SIRVIERON DE BASE PARA REALIZAR EL RECÁLCULO DE LA PROPORCIONALIDAD, LOS CUALES DEBERÁN EXHIBIRSE O PRESENTARSE A LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS CUANDO ESTA LO REQUIERA. (8)" — "SI NO EXISTEN CRÉDITOS FISCALES ATRIBUIBLES A LAS OPERACIONES NO SUJETAS AL PAGO DEL IMPUESTO Y ÉSTAS PROVIENEN DE ACTIVIDADES NO HABITUALES DEL CONTRIBUYENTE, NO SE INCLUIRÁN TALES OPERACIONES EN EL CÁLCULO DE LA PROPORCIONALIDAD. TAMPOCO SE INCLUIRÁN EN EL CÁLCULO DE LA PROPORCIONALIDAD, LAS OPERACIONES CONSISTENTES EN DONACIONES DE BIENES O DE SERVICIOS EFECTUADAS POR EL CONTRIBUYENTE EN LOS TÉRMINOS PREVISTOS EN LOS INCISOS FINALES DE LOS ARTÍCULOS 11 Y 16 DE ESTA LEY, A LAS INSTITUCIONES A QUE SE REFIERE EL ARTÍCULO 6 DE LA LEY DE IMPUESTO SOBRE LA RENTA; ASÍ COMO TAMBIÉN, LAS OPERACIONES DE VENTAS DE BIENES Y SERVICIOS QUE REALICEN LOS CONTRIBUYENTES A LAS MISIONES DIPLOMÁTICAS, CONSULARES, ORGANISMOS INTERNACIONALES Y A SUS MIEMBROS ACREDITADOS ANTE EL GOBIERNO DE LA REPÚBLICA DE EL SALVADOR, CUANDO ÉSTAS HAYAN SIDO DECLARADAS COMO EXENTAS O NO SUJETAS AL PAGO DEL IMPUESTO QUE REGULA ESTA LEY, CONFORME A LOS RESPECTIVOS INSTRUMENTOS INTERNACIONALES SUSCRITOS Y RATIFICADOS POR EL SALVADOR. LO ANTERIOR, SIN PERJUICIO DEL CUMPLIMIENTO DE OTRAS OBLIGACIONES TRIBUTARIAS QUE ESTA LEY O EL CÓDIGO TRIBUTARIO ESTABLEZCAN RESPECTO DE LAS OPERACIONES NO SUJETAS. (8) (9) (13)" | The contribuyente shall CONSERVE during the term the Código Tributario establishes the records that served as base for the proportionality recalculation, which shall be EXHIBITED or PRESENTED to the Dirección General de Impuestos Internos when it requires; operations NOT INCLUDED in the proportionality calculation: no-sujeta operations where NO credits fiscal are attributable to them AND they come from NON-HABITUAL activities of the contribuyente; donation operations of goods or services effected in the terms of the FINAL INCISOS of Arts. 11 and 16 to the institutions of ISR Art. 6; and sales of goods and services to diplomatic missions, consulates, international organizations and their members accredited before the Government of El Salvador when declared exentas or no sujetas under the respective international instruments SUBSCRIBED AND RATIFIED by El Salvador — all without prejudice to other tax obligations the law or the CT establish regarding no-sujeta operations | `sv/sources/01_Ley_IVA.pdf` | Art. 66 incisos 5º-6º p.35 (EVID-324; verified 01_ txt lines 1285-1303, PAGE 35) |
| LB-003 | Ley IVA, Art. 66, incisos 7º-8º (no-sujetas definition; costo o gasto) | "SE CONSIDERAN OPERACIONES NO SUJETAS AL PAGO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS, AQUELLAS QUE, NO ESTANDO EXPRESAMENTE PREVISTAS EN LA LEY COMO EXENCIONES, NO SE ENMARCAN DENTRO DE LOS HECHOS GENERADORES ESTABLECIDOS EN ESTA LEY, ASÍ COMO AQUELLAS QUE DICHA LEY LES ATRIBUYA EXPRESAMENTE EL CARÁCTER DE NO SUJETAS. (8)" — "LA PROPORCIÓN DEL CRÉDITO FISCAL QUE CORRESPONDA A LAS OPERACIONES EXENTAS Y NO SUJETAS FORMARÁ PARTE DEL COSTO O GASTO, SEGÚN CORRESPONDA. (8)" | Operations no sujetas to the tax are those which, NOT being expressly foreseen in the law as exemptions, do not frame within the hechos generadores established in it, as well as those to which the law expressly attributes the character of no sujetas; the proportion of the crédito fiscal corresponding to EXENTAS and NO SUJETAS operations forms part of the COST OR EXPENSE, as corresponds | `sv/sources/01_Ley_IVA.pdf` | Art. 66 incisos 7º-8º pp.35-36 (EVID-324; verified 01_ txt lines 1304-1317, PAGE 35-36) |
| LB-004 | Ley IVA, Art. 67 + Reglamento IVA, Art. 24 | Ley Art. 67: "Si el monto del crédito fiscal fuere superior al total del débito fiscal del período tributario, el excedente de aquél se sumará al crédito fiscal del período tributario siguiente o sucesivos hasta su deducción total." Rgto. Art. 24: "Se entenderá por excedente o remanente de Crédito Fiscal, aquel saldo o cantidad del mismo, que por ser superior al monto del Débito Fiscal generado en el período tributario, no fuere posible utilizarlo en el mismo período; en consecuencia, podrá hacerse uso de él en los períodos tributarios siguientes hasta su total deducción." | If the crédito fiscal exceeds the total débito fiscal of the period, the excess is summed to the crédito fiscal of the following or successive periods UNTIL ITS TOTAL DEDUCTION; Rgto. Art. 24: excedente or remanente de Crédito Fiscal = the balance or quantity which, being superior to the Débito Fiscal generated in the period, cannot be used in that same period — consequently usable in the FOLLOWING tax periods until its total deduction | `sv/sources/01_Ley_IVA.pdf` + `sv/sources/02_Reglamento_IVA.pdf` | Ley Art. 67 p.36 (EVID-325; verified 01_ txt lines 1319-1322, PAGE 36); Rgto. Art. 24 p.7 (EVID-336; verified 02_ txt lines 245-248, PAGE 7) |
| LB-005 | Ley IVA, Art. 68 | "El contribuyente que cese en el objeto o giro de sus actividades, no podrá solicitar devolución ni reintegro del remanente del crédito fiscal que quedare con motivo de dicho término de actividades. Este remanente, no será imputable a otras deudas tributarias ni tampoco transferible a terceros, salvo el caso señalado en el artículo siguiente." | The contribuyente that CEASES in the object or giro of its activities may not request devolución nor reintegro of the remanente crédito fiscal remaining by reason of that termination; that remanente is not imputable to other tax debts nor transferable to third parties — save the case the following article señala | `sv/sources/01_Ley_IVA.pdf` | Art. 68 p.36 (EVID-325; verified 01_ txt lines 1323-1327, PAGE 36) |
| LB-006 | Ley IVA, Art. 69 (incisos 1º-5º) | "El derecho a deducir el crédito fiscal del débito fiscal es propio de cada contribuyente, y no podrá ser transferido a terceros, excepto cuando un contribuyente sea el continuador de otro por mandato legal o cuando se trate de la fusión o absorción de sociedades y en que la sociedad nueva o la subsistente continúa el giro o actividad de las primitivas, en cuyo caso la nueva sociedad gozará del remanente del crédito fiscal que les correspondía a las sociedades fusionadas o absorbidas." — "En el caso de liquidación de sociedades, no procede la devolución o reintegro del remanente del crédito fiscal." — "El aporte de todo el activo y pasivo de una sociedad a otra, no le da derecho a la sociedad receptora para usar el crédito fiscal de la aportante." — "Asimismo, no procede traspasar el remanente del crédito fiscal entre contribuyentes vinculados económicamente." — "Tampoco tienen derecho los herederos a utilizar el remanente del crédito fiscal resultante del término de actividades de un contribuyente fallecido." | The right to deduct the crédito fiscal from the débito fiscal is PROPER to each contribuyente and not transferable to third parties, EXCEPT where a contribuyente is the continuador of another by legal mandate, or in the fusión or absorción of societies where the new or subsisting society CONTINUES the giro or activity of the primitives — in which case the new society enjoys the remanente crédito fiscal that corresponded to the fused or absorbed societies; in society LIQUIDATION no devolution or reinstatement of the remanente proceeds; the aport of ALL the activo and pasivo of one society to another gives the receiving society NO right to use the aportante's crédito fiscal; no traspaso of the remanente between economically LINKED contribuyentes proceeds; and HEIRS have no right to use the remanente crédito fiscal resulting from the termination of activities of a deceased contribuyente | `sv/sources/01_Ley_IVA.pdf` | Art. 69 p.36 (EVID-325; verified 01_ txt lines 1328-1341, PAGE 36) |
| LB-007 | Ley IVA, Art. 70 + Reglamento IVA, Art. 25 | Ley Art. 70: "El presente impuesto pagado o causado no constituye un costo de los bienes y servicios adquiridos, importados o utilizados, respectivamente, salvo cuando los bienes o servicios estén destinados al uso o consumo final, a operaciones exentas o sujetos excluidos del presente impuesto. Tampoco es un gasto deducible para los efectos del impuesto sobre la renta." Rgto. Art. 25: "El impuesto pagado o causado por las compras o adquisiciones de bienes y utilización de servicios por parte del contribuyente, al constituir Crédito Fiscal, no debe formar parte del costo de los mismos, salvo que estén destinados a operaciones exentas o no gravadas. Por otra parte, si el impuesto no pudiere utilizarse totalmente, por aplicación de la proporcionalidad del Crédito Fiscal a que se refiere el artículo 66 de la ley o por el término o cese de actividades, pasará a constituir un gasto general." | This tax paid or caused is NOT a cost of the goods and services acquired, imported or used — SAVE when the goods or services are destined to final use or consumption, to exempt operations, or to subjects excluded from this tax — nor is it a deductible expense for ISR purposes; Rgto. Art. 25: IVA paid or caused on purchases/acquisitions and service use which constitutes Crédito Fiscal must not form part of their cost — SAVE destinations to exempt or non-gravada operations — and if the tax cannot be totally used, whether by application of the Art. 66 crédito-fiscal proportionality or by the término or cese de actividades, it passes to constitute a GENERAL EXPENSE | `sv/sources/01_Ley_IVA.pdf` + `sv/sources/02_Reglamento_IVA.pdf` | Ley Art. 70 p.36 (EVID-325; verified 01_ txt lines 1342-1346, PAGE 36); Rgto. Art. 25 p.7 (EVID-336; verified 02_ txt lines 249-256, PAGE 7) |
| LB-008 | D.L. 499 (Ley Quincena Veinticinco, 66_), Art. 6 pasaje de tercerización + Guía DGII 67_ (tratamiento documental e IVA) — **OCR QUOTE-FIDELITY NOTE** | 66_ Art. 6: el tercerizador que pague el íntegro de la Quincena Veinticinco "debera emitir al contratante, por separado, el correspondiente documento fiscal en el que conste el monto pagado en concepto de Quincena Veinticinco y, oportunamente, presentar la copia de la planilla" ["debera" sic — OCR]. 67_: el documento fiscal del tercerizador = "**Factura de Consumidor Final, con valor exento**" + "de conformidad con la parte primera del inciso sexto del artículo 66 de la Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, **no se aplicará la proporcionalidad del Crédito Fiscal por dicha operación**" | The tercerización contractor paying the full Quincena-25 amount must emit to the contracting party, SEPARATELY, the corresponding fiscal document stating the amount paid as Quincena Veinticinco and opportunely PRESENT THE PLANILLA COPY; the guía: that document is a Factura de Consumidor Final WITH EXEMPT VALUE, and per "the first part of the sixth inciso of Art. 66" of the IVA law the crédito-fiscal PROPORTIONALITY IS NOT APPLIED for that operation | `sv/sources/66_Ley_Quincena25_DL499.pdf` + `sv/sources/67_Guia_Orientacion_Quincena25.pdf` | 66_ Art. 6 p.5-6 + 67_ §4 (EVID-237; OCR extraction — no txt layer; R30(c) inciso-mapping note applies) |
| LB-009 | Disposiciones Especiales y Transitorias de Apoyo al "Programa de Acceso Universal a la Energía en El Salvador" (108_), Art. 2, párrafo final: "Los proveedores locales que realicen ventas de bienes o prestaciones de servicios a favor de los beneficiarios de las exenciones detalladas no aplicarán la proporcionalidad del crédito fiscal a que se refiere el artículo 66 de la Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios." | Local suppliers making sales of goods or prestations of services in favor of the beneficiaries of the detailed (108_ Art. 2) exemptions do NOT apply the Art. 66 crédito-fiscal proportionality — a SELLER-SIDE (proveedor local) relief printed on EXPRESS STATUTORY text (a law-printed no-proporcionalidad command — contrast LB-008/FR-277, where the Quincena-25 no-pro-rata rule rests on the DGII guía 67_ reading of a pre-D.L.-224-2009 inciso under the R30(c) working reading). KIN NOTE: 97_ Art. 1-b prints the identical proveedores-locales relief (spe/02 LB-023 — the in-corpus precedent; 97_'s window is project-spent, so W19 minted no separate taxation/11 row — recorded here as kin, not re-quoted). Operative FR = FR-421; the beneficiaries' vinculación and exemption windows resolve per spe/02 SV-SPE-FR-204 by id (identity row = spe/01 LB-034) | `sv/sources/108_EnergiaElectrica_AccesoUniversal_DL411_2025_Asamblea.pdf` | 108_ Art. 2 final ¶ p.2 (EVID-406; 108_ txt PAGE 2, lines 111-114; native asamblea text layer — intra-word cleaning per EV header; W24 T3) |

Dead text — never implementable as current law (recorded as notes, not
FRs): nothing in this file's article range is derogated or void — Arts.
66-70 are all live in the 01_ consolidation and Rgto. Arts. 24-25 are
survivors; the only vintage caveats are the SOQ-54 watch (§2 preamble,
every row) and the 67_ guía's PRE-D.L.-224-2009 inciso numbering on the
tercerización citation (R30(c) working reading, OQ-2 — the guía is an
administrative guide, not law; the operative rule is encoded against the
current print's own exclusion inciso). The 66_ Art. 6 transitory credit
regime (2026-only ISR sweetener) is the ISR files' surface
(`taxation/02` SV-TAX-FR-173..175, by id) — never restated here. The
SOQ-54 vintage watch applies to every row above.

## 3. Functional Requirements

### 3.1 The Art. 66 proportionality engine (factor, accumulated base, January redistribution)

- **SV-TAX-FR-269:** The system shall apply the Art. 66
  proportionality when a período tributario's operations are mixed — in
  part gravadas, in part exentas or in part no sujetas (mixed-period
  trigger evaluated on the period's classified operation values, buckets
  from the T1/T2 classification feeds by id) — computing the deductible
  crédito fiscal as: **factor = gravadas operations of the period ÷
  (gravadas + exentas + no sujetas operations of the same period)**,
  with ONLY the resulting proportion of the period's crédito fiscal
  (the T4 credit engine's eligible total, SV-TAX-FR-251..267 output
  consumed by id) deductible against the débito fiscal; the factor, the
  three bucket values and the split amounts are snapshotted on the
  period's pro-rata run record (D15: the factor resolves as-of each
  period over that period's data).
  (LB-001; EVID-324; cross-ref SV-TAX-FR-176, SV-TAX-FR-206/224,
  SV-TAX-FR-251..267)
- **SV-TAX-FR-270:** For períodos tributarios FOLLOWING the first
  pro-rata period, the system shall compute the proportion over the
  ACCUMULATED base: operations accumulated FROM THE FIRST PERIOD IN
  WHICH THE PROPORTIONALITY WAS APPLIED through the término del
  ejercicio comercial (fiscal-year end) — even where the contribuyente
  had ONLY gravadas operations afterwards — each period's factor
  applying to that period's own crédito fiscal; the accumulated
  accumulator (per ejercicio, per bucket) is a first-class ledger
  object opening at the first pro-rata period and closing at
  fiscal-year end, and no later-only-gravadas stretch may restart or
  reset it.
  (LB-001; EVID-324)
- **SV-TAX-FR-271:** When the norm has applied during an ejercicio
  comercial, the system shall — in the FIRST MONTH of the following
  ejercicio — recompute the proportionality with the CUMULATIVE values
  of the prior ejercicio's gravadas, exentas and no-sujetas operations
  (the closed-year accumulator totals; original-year parameters, D15)
  and REDISTRIBUTE the crédito fiscal: where the crédito that SHOULD
  have been deducted is SUPERIOR to that effectively deducted, the
  difference shall be SUMMED to the crédito fiscal corresponding to
  the FIRST período tributario of the following ejercicio (a dated
  true-up entry posting to that period's credit); where INFERIOR, it
  shall be SUBTRACTED from the crédito fiscal of that same first
  period; the redistribution entry records the closed ejercicio, the
  recalculated factor, both credit figures and the difference with its
  sign — a computation against the CLOSED fiscal year whose parameters
  never re-resolve.
  (LB-001; EVID-324)
- **SV-TAX-FR-272:** The system shall conserve the records that served
  as base for the proportionality recalculation — the per-period bucket
  ledgers, run records and the January redistribution entries — during
  the term the Código Tributario establishes (CT books-preservation
  term consumed as configuration, never hardcoded), and shall surface
  them for EXHIBITION or PRESENTATION to the Dirección General de
  Impuestos Internos on requirement (an exportable recalculation-base
  dossier per ejercicio: buckets, factors, credits, true-up).
  (LB-002; EVID-324)

### 3.2 Denominator composition: no-sujetas definition, exclusions and the costo-o-gasto tail

- **SV-TAX-FR-273:** The system shall classify *operaciones no
  sujetas* per the Art. 66 statutory definition — operations NOT
  expressly foreseen in the law as exenciones that do not frame within
  the hechos generadores it establishes, PLUS operations to which the
  law expressly attributes the character of no sujetas — as a bucket
  DISTINCT from exentas (exemption classification owned by
  `08_iva-exemptions.md` SV-TAX-FR-206/224 and hecho-generador framing
  by `07_iva-framework.md` SV-TAX-FR-176, both consumed by id: a
  no-sujeta line never resolves through the exemption registry, and an
  exemption never resolves as no-sujeta).
  (LB-003; EVID-324; cross-ref SV-TAX-FR-176, SV-TAX-FR-206/224)
- **SV-TAX-FR-274:** The system shall EXCLUDE from the proportionality
  calculation's denominator three operation classes, each with its
  recorded exclusion ground: (a) no-sujeta operations where NO créditos
  fiscales are attributable to them AND they come from NON-HABITUAL
  activities of the contribuyente (both limbs required — attribution
  test per the OQ-3 configuration note; habitualidad sources consumed
  from `07_iva-framework.md` SV-TAX-FR-199, by id); (b) donations of
  goods or services effected in the terms of the FINAL INCISOS of
  Arts. 11 and 16 to the ISR-Art.-6 institutions (the donation
  carve-outs owned by `07_iva-framework.md` SV-TAX-FR-185/191, by id);
  and (c) sales of goods and services to misiones diplomáticas,
  consulares, organismos internacionales and their members accredited
  before the Government of El Salvador when declared exentas or no
  sujetas under the respective international instruments SUBSCRIBED
  AND RATIFIED by El Salvador (stamp 13) — the exclusions carry NO
  waiver of the other tax obligations the law or the CT establish
  regarding no-sujeta operations (the without-prejudice clause is a
  recorded note on each exclusion).
  (LB-002; EVID-324; cross-ref SV-TAX-FR-185, SV-TAX-FR-191,
  SV-TAX-FR-199)
- **SV-TAX-FR-275:** The system shall post the crédito-fiscal
  proportion corresponding to EXENTAS and NO SUJETAS operations as
  PART OF THE COST OR EXPENSE, as corresponds (the non-deducted tail of
  each period's factor split): the reclassification entry
  (IVA crédito → costo o gasto) fires at each pro-rata run, feeds the
  F-07 pro-rata block — casilla 132 (*crédito IVA por proporcionalidad
  mensual*, the monthly non-deductible magnitude), casilla 133 (annual
  adjustment, superior) and casilla 134 (annual adjustment, inferior)
  — as the named producer of the inputs consumed by
  `fiscal-reporting/01_f07-declaration.md` SV-FREP-FR-012 (by id; the
  v14 print attests exactly casillas 132/133/134 for this block — the
  extraction gloss's "137-138" has no form anchor, OQ-3), mirrors the
  T4 blocked→cost row (SV-TAX-FR-268, by id) and the Rgto. Art. 25
  unusable-credit rule (FR-283).
  (LB-003; LB-007; EVID-324/336; cross-ref SV-TAX-FR-268,
  SV-FREP-FR-012)

### 3.3 Quincena-25 tercerización closure (D.L. 499 Art. 6; guía 67_; R30(c))

- **SV-TAX-FR-276:** For a tercerización contractor paying the full
  Quincena-25 amount, the system shall emit the pass-through to the
  contratante as a SEPARATE fiscal document stating the amount paid in
  concepto de Quincena Veinticinco — a *Factura de Consumidor Final,
  con valor exento* (consumer-final document with exempt value: the FE
  type-01 electronic consumer invoice of
  `e-invoicing/01_document-types.md` SV-EINV-FR-001, by id, carrying
  the exempt classification — never a CCF/CCFE, which would shift
  credit) — and shall enforce the planilla duty: the OPPORTUNE
  PRESENTATION OF THE PLANILLA COPY to the contratante, sourced from
  the per-worker Quincena-25 ledger (`payroll/08_isr-interfaces.md`
  SV-PAY-FR-142, by id — the seven-field annex ledger is the planilla
  value source; attachment recorded on the emission).
  (LB-008; EVID-237; cross-ref SV-EINV-FR-001, SV-PAY-FR-142)
- **SV-TAX-FR-277:** The system shall NOT apply the Art. 66
  crédito-fiscal proportionality to the Quincena-25 tercerización
  pass-through operation — per the guía 67_ reading of "la parte
  primera del inciso sexto del artículo 66" (pre-D.L.-224-2009 inciso
  numbering; R30(c) working reading maps it to the CURRENT print's
  no-habitual/no-attributable-credit no-sujetas exclusion, LB-002) —
  so the FCF-exento Quincena-25 operation is tagged OUT of the
  pro-rata denominator as an excluded operation (exclusion ground
  `quincena25_tercerizacion`, regime-dated: D.L. 499 effective
  14-ene-2026, the 2026 voluntary payment and every January from 2027
  mandatory), and no pro-rata true-up, monthly or annual, ever draws
  on it; this row CLOSES `taxation/02_isr-deductions.md` OQ-009 by
  pointer (the index task wires the status flip).
  (LB-008; EVID-237; R30(c) — OQ-2)
- **SV-TAX-FR-421:** The system shall NOT apply the Art. 66
  proportionality (FR-269) to a LOCAL SUPPLIER's ventas de bienes or
  prestaciones de servicios made in favor of 108_-exemption
  beneficiaries: the operation is tagged OUT of the seller's pro-rata
  base as an excluded operation — the FR-277 chassis, but anchored on
  EXPRESS STATUTORY text (108_ Art. 2 final paragraph: "no aplicarán
  la proporcionalidad del crédito fiscal" — versus FR-277's guía-67_
  anchor) — with exclusion ground `energia_dl411_proveedor_local`
  keyed to the instrument (dl411_2025): the beneficiary vinculación
  and the exemption window resolve per spe/02 SV-SPE-FR-204 by id, and
  the exclusion window FOLLOWS THE BENEFICIARY'S exemption window
  (dated, per-contract event window inside the decree vigencia
  27-sep-2025 → 26-sep-2031; D15 as-of the operation date — a sale
  outside the beneficiary's window stays IN the seller's
  proportionality base). DENOMINATOR-SIDE reading (recorded in-row per
  the printed text, not an OQ): the printed command relieves the
  proportionality CALCULATION only — the seller's crédito fiscal
  attributable to those operations is NOT blocked and remains
  creditable under the engine's other rules (FR-269 consumes the T4
  credit output unchanged); no monthly factor and no annual true-up
  ever draws on the excluded operation.
  (LB-009; EVID-406 W24 T3; cross-ref FR-269, FR-277, SV-SPE-FR-204)

### 3.4 Remanente — definition, indefinite carryforward and the cessation lock (Art. 67-68; Rgto. 24)

- **SV-TAX-FR-278:** The system shall compute the *excedente o
  remanente de Crédito Fiscal* per period as the crédito balance that,
  being superior to the débito fiscal generated in the período
  tributario, cannot be used in that same period (Rgto. Art. 24
  definition) — and shall carry it forward by summing it to the crédito
  fiscal of the FOLLOWING or SUCCESSIVE periods *HASTA SU DEDUCCIÓN
  TOTAL*: an INDEFINITE carryforward ledger with no expiry, no
  prescription-driven write-off inside this file (CT prescription is
  procedural, never encoded here) and no refund conversion (the F-07
  consumer surfaces — casilla 155 computation and the 155→110
  next-period re-entry — are `fiscal-reporting/01_f07-declaration.md`
  SV-FREP-FR-015/026, cited by id; this file is the ledger they read).
  (LB-004; EVID-325/336; cross-ref SV-FREP-FR-015, SV-FREP-FR-026)
- **SV-TAX-FR-279:** When a contribuyente CEASES in the objeto or giro
  of its activities (cessation event recorded with its date), the
  system shall LOCK the remanente crédito fiscal remaining by reason of
  that termination: NO devolución (refund) and NO reintegro may be
  requested or generated from it; it shall NOT be imputable to other
  tax debts (no cross-tax offset path); and it shall NOT be
  transferable to third parties — SAVE the Art. 69 exceptions (FR-280);
  the locked remanente keeps its ledger record in an unusable
  `cessation_locked` state and routes to gasto general per Rgto. Art.
  25 (FR-283).
  (LB-005; LB-007; EVID-325/336)

### 3.5 Non-transferability of the credit right (Art. 69)

- **SV-TAX-FR-280:** The system shall treat the right to deduct the
  crédito fiscal from the débito fiscal as PROPER TO EACH
  CONTRIBUYENTE — never transferable to third parties — with EXACTLY
  two inheritance exceptions, each recorded with its legal ground and
  evidence: (a) a contribuyente that is the CONTINUADOR of another POR
  MANDATO LEGAL (the mandate-of-law continuation instrument recorded on
  the transfer record); and (b) FUSIÓN or ABSORCIÓN of societies where
  the nueva or subsistente society CONTINUES the giro or activity of
  the primitives — in which case the successor inherits the remanente
  crédito fiscal that corresponded to the fused or absorbed societies
  (giro-continuity attested against the registered giro, the
  tarjeta-de-contribuyente identity of SV-TAX-FR-258's kin); any
  transfer path outside these two is rejected at validation.
  (LB-006; EVID-325)
- **SV-TAX-FR-281:** In LIQUIDATION of societies the system shall
  generate NO devolución or reintegro of the remanente crédito fiscal
  (the liquidation event produces no refund path — the remanente dies
  with the liquidated entity, recorded as a terminal ledger state).
  (LB-006; EVID-325)
- **SV-TAX-FR-282:** The system shall enforce the three residual Art.
  69 bars: (a) the aport of ALL the activo and pasivo of one society
  to another gives the RECEPTORA society NO right to use the
  aportante's crédito fiscal (a universal aport is not a fusión — the
  succession exception of FR-280 does not fire); (b) NO traspaso of
  the remanente between contribuyentes VINCULADOS ECONÓMICAMENTE
  (related parties — the economic-link flag blocks the transfer); and
  (c) HEREDEROS have no right to use the remanente crédito fiscal
  resulting from the termination of a deceased contribuyente's
  activities (estate succession ≠ contribuyente succession).
  (LB-006; EVID-325)

### 3.6 IVA never cost nor gasto (Art. 70; Rgto. 25)

- **SV-TAX-FR-283:** The system shall treat IVA paid or caused as NOT
  constituting a cost of the goods and services acquired, imported or
  used — and NOT an ISR-deductible gasto — SAVE in the three carved-out
  destinations: final use or consumption (*uso o consumo final*);
  exempt operations (*operaciones exentas*); and subjects excluded
  from the tax (*sujetos excluidos*, the Art.-28 excluidos of
  `07_iva-framework.md` SV-TAX-FR-202..205, by id); and, per Rgto.
  Art. 25, where the tax cannot be totally used — whether by
  application of the Art. 66 crédito-fiscal proportionality (FR-269's
  non-deducted tail) or by the término or cese de actividades
  (FR-279's lock) — it shall PASS TO CONSTITUTE A GASTO GENERAL (a
  general-expense reclassification, the operating mirror of T4's
  blocked→cost row SV-TAX-FR-268 and of FR-275's exenta/no-sujeta
  proportion; ISR-side deductibility is owned by
  `taxation/02_isr-deductions.md` SV-TAX-FR-045, by id — never decided
  here).
  (LB-007; EVID-325/336; cross-ref SV-TAX-FR-202..205, SV-TAX-FR-268,
  SV-TAX-FR-045)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the factor is computed, never tabulated;
the only dated regimes are the D.L. 499 Quincena-25 window (effective
14-ene-2026; 2026 voluntary private-sector payment, every January from
2027 mandatory — a behavior flag on the tercerización exclusion, values
owned by the Quincena-25 payroll files by id) and the D15 as-of
resolution of every factor/true-up computation. Layer semantics: this
file introduces Odoo-side proportionality/carryforward computation data
only (wave default `odoo`; see §5).

**Pro-rata engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.prorata.run (new) | company_id, period, first_prorata_period | m2o / char / char | per períodos tributarios; the first period the proportionality applied (accumulator opener) | FR-269, FR-270 |
| l10n_sv.iva.prorata.run | gravadas, exentas, no_sujetas (period) + accum_gravadas, accum_exentas, accum_no_sujetas | monetary ×6 | period buckets from classification feeds; accumulated base from first pro-rata period through fiscal-year end | FR-269, FR-270 |
| l10n_sv.iva.prorata.run | factor, credito_total, credito_deducible, credito_exento_cost | monetary-ratio / monetary ×3 | factor = gravadas ÷ (gravadas+exentas+no_sujetas); deducible = factor × crédito_total; tail → costo o gasto (snapshot, D15) | FR-269, FR-275 |
| l10n_sv.iva.prorata.redistribution (new) | prior_ejercicio, recalc_factor, credit_should, credit_effective, difference, sign | char / ratio / monetary ×3 / select | January true-up: superior ⇒ sum to following ejercicio's first period (+); inferior ⇒ subtract (−); original-year parameters, never re-resolved | FR-271 |
| l10n_sv.iva.prorata.run (links) | casilla_132_feed, casilla_133_feed, casilla_134_feed | monetary | named producer outputs consumed by SV-FREP-FR-012 (by id) | FR-275 |
| account.move.line (sale, SV extension) | l10n_sv_iva_prorata_bucket | select (computed) | gravada · exenta · no_sujeta · excluded | FR-269, FR-273 |
| account.move.line (sale, SV extension) | l10n_sv_iva_prorata_exclusion | select | none · no_habitual_no_credit · donation_11_16_isr6 · diplomatic_instrument · quincena25_tercerizacion · energia_dl411_proveedor_local (W24 T3) | FR-274, FR-277, FR-421 |
| account.move.line (sale, SV extension) | l10n_sv_iva_exclusion_instrument (108_ limb) | m2o (instrument config) + date fields | instrument-keyed dated window for energia_dl411_proveedor_local: follows the BENEFICIARY's exemption window (per-contract event window per SV-SPE-FR-204 by id, inside decree vigencia 27-sep-2025 → 26-sep-2031); D15 as-of operation date; DENOMINATOR-SIDE only — the seller's credit on the operation is NOT blocked | FR-421 |
| l10n_sv.iva.prorata.dossier (new) | ejercicio, records refs | char / refs | conservation/exhibition dossier (CT term config; DGII on requirement) | FR-272 |

**Remanente and succession:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.remanente.ledger (new) | company_id, period, opening, generated, used, closing | m2o / char / monetary ×4 | opening = prior closing (F-07 155→110 kin, SV-FREP-FR-026 by id); indefinite carryforward, no expiry | FR-278 |
| l10n_sv.iva.remanente.ledger | state | select | active · cessation_locked · liquidated_terminal · inherited | FR-278, FR-279, FR-281, FR-280 |
| res.company (SV extension) | l10n_sv_iva_cese_date | date | cessation in objeto/giro → remanente lock (no refund, no offset, no transfer save Art. 69) | FR-279 |
| l10n_sv.iva.remanente.transfer (new) | kind, instrument_ref, giro_continuity_evidence, amount | select / char / ref / monetary | continuador_mandato_legal · fusion · absorcion (ONLY these inherit; related-party/universal-aport/heir paths rejected) | FR-280, FR-282 |
| l10n_res.partner (SV extension) | l10n_sv_iva_vinculado_economico | boolean + link | economic-link flag blocking remanente traspaso | FR-282 |

**Cost tails:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (auto, SV extension) | l10n_sv_iva_prorata_cost_entry, l10n_sv_iva_gasto_general_entry | boolean / select | exenta-no-sujeta proportion → costo o gasto (FR-275); unusable crédito (pro-rata/cese) → gasto general (Rgto. 25) | FR-275, FR-283 |
| account.move (tercerización emission, SV extension) | l10n_sv_quincena25_passthrough | boolean | FCF-exento pass-through doc (FE type-01 by id) + planilla-copy attachment (SV-PAY-FR-142 by id); pro-rata denominator exclusion | FR-276, FR-277 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = proportionality/carryforward
computation logic living in the LGPL client. No SaaS rows are
introduced in this file: nothing here touches DTE generation (the
tercerización FCF emission rides the e-invoicing stack's type-01 FE —
SV-EINV-FR-001, cited by id; this file supplies the exempt-value
pass-through rule and the pro-rata exclusion the client consumes).
Model names are stable across Odoo 17/18/19/20 (`account.move`,
`account.move.line`, `res.partner`, `res.company`; the pro-rata run,
redistribution, remanente-ledger and transfer objects are new
`l10n_sv.*` models). D15 doctrine (binding): every factor resolves
as-of its period over accumulated data; the January redistribution is
a DATED computation against the CLOSED fiscal year — original-year
parameters snapshotted on the redistribution record, corrections to
the closed year re-derive it, never re-resolve it.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-269 | odoo | l10n_sv.iva.prorata.run | factor + buckets + split | Mixed-period trigger; factor = gravadas ÷ (gravadas+exentas+no sujetas) of the period; crédito input = T4 engine output (SV-TAX-FR-251..267, by id); D15 snapshot |
| FR-270 | odoo | l10n_sv.iva.prorata.run | accumulated base fields | Accumulator opens at FIRST pro-rata period, closes at fiscal-year end; only-gravadas stretch never resets it |
| FR-271 | odoo | l10n_sv.iva.prorata.redistribution + account.move (auto) | January true-up | First month of following ejercicio; superior ⇒ + to first period's crédito, inferior ⇒ −; closed-year original parameters (D15) |
| FR-272 | odoo | l10n_sv.iva.prorata.dossier | conservation/exhibition | CT term consumed as config (never hardcoded); DGII-on-requirement export surface |
| FR-273 | odoo | account.move.line (sale) | prorata_bucket = no_sujeta | Statutory no-sujetas definition; distinct from exentas (T2 registry SV-TAX-FR-206/224 by id; framing SV-TAX-FR-176 by id) |
| FR-274 | odoo | account.move.line (sale) | prorata_exclusion enum | (a) no-habitual + no-attributable-credit (both limbs; habitualidad per SV-TAX-FR-199 by id); (b) donations 11/16-finals (FR-185/191 by id); (c) diplomatic under RATIFIED instruments (stamp 13); without-prejudice note rides each |
| FR-275 | odoo | l10n_sv.iva.prorata.run + account.move (auto) | costo-o-gasto entry + 132/133/134 feeds | Named producer for SV-FREP-FR-012 (by id); v14 attests only 132/133/134 (OQ-3: gloss's "137-138" unanchored); mirrors SV-TAX-FR-268 |
| FR-276 | odoo | account.move (emission) | quincena25_passthrough doc | FCF con valor exento = FE type-01 (SV-EINV-FR-001 by id; never CCF/CCFE); planilla copy from SV-PAY-FR-142 ledger (by id) |
| FR-277 | odoo | account.move.line (sale) | exclusion = quincena25_tercerizacion | No pro-rata for the pass-through (67_ "inciso sexto parte primera" = pre-224-2009 numbering → current no-habitual exclusion, R30(c)/OQ-2); regime-dated 14-ene-2026+; closes taxation/02 OQ-009 by pointer |
| FR-421 | odoo | account.move.line (sale) | exclusion = energia_dl411_proveedor_local | 108_ Art. 2 final ¶: local suppliers selling to 108_ beneficiaries do not apply the Art. 66 proportionality — EXPRESS statutory anchor (vs FR-277's guía/R30(c) reading); window follows the beneficiary's exemption window (SV-SPE-FR-204 by id); DENOMINATOR-SIDE relief — the seller's credit remains creditable |
| FR-278 | odoo | l10n_sv.iva.remanente.ledger | opening/generated/used/closing | Indefinite carryforward hasta su deducción total; F-07 consumers SV-FREP-FR-015/026 (by id); no prescription write-off encoded |
| FR-279 | odoo | l10n_sv.iva.remanente.ledger + res.company | cese_date + cessation_locked | No devolución/reintegro, no other-debt offset, no transfer save Art. 69; tail → gasto general (FR-283) |
| FR-280 | odoo | l10n_sv.iva.remanente.transfer | continuador_mandato_legal / fusion / absorcion | ONLY these inherit (giro continuity attested vs registered giro); all other transfer paths rejected at validation |
| FR-281 | odoo | l10n_sv.iva.remanente.ledger | liquidated_terminal | Society liquidation ⇒ no refund path; terminal state |
| FR-282 | odoo | l10n_sv.iva.remanente.transfer + res.partner | universal-aport bar + vinculado flag + heirs bar | Universal activo-y-pasivo aport ≠ fusión; vinculados económicamente traspaso banned; herederos banned |
| FR-283 | odoo | account.move (auto) | gasto_general entry | Never cost/gasto save final-use/exempt/excluded destinations (excluidos SV-TAX-FR-202..205 by id); Rgto. 25 unusable → gasto general; ISR deductibility owned by SV-TAX-FR-045 (by id) |

Version-regime notes (D12/D15/D18): FR-277's tercerización exclusion is
regime-dated (D.L. 499 effective 14-ene-2026 — voluntary private-sector
Quincena-25 in 2026, mandatory every January from 2027; periods before
2026-01-14 never carry the exclusion, D18 historical-import kin). FR-421's
exclusion is instrument-dated (108_ dl411_2025: operations from 27-sep-2025
inside a declared beneficiary's per-contract event window, inside decree
vigencia through 26-sep-2031 — SV-SPE-FR-204 by id; periods before the
decree vigencia never carry the exclusion, D18 kin). FR-269/
270/271 carry the D15 doctrine (per-period as-of resolution; January
redistribution against closed-year original parameters). The SOQ-54
consolidation watch rides every LB (§2 preamble) — re-verify against a
current official consolidation at implementation.

## 6. Acceptance Criteria

- **AC-001:** Given March as the FIRST mixed month (gravadas $90,000,
  exentas $10,000, no sujetas $0, crédito $2,600), when the pro-rata
  run executes, then factor = 90,000/100,000 = 0.9000, deductible
  crédito = $2,340.00 and the $260.00 tail posts to costo o gasto
  (FR-269, FR-275).
- **AC-002:** Given April with only gravadas operations ($40,000) and
  crédito $1,300, when April's run executes, then the factor computes
  over the ACCUMULATED base (90,000+40,000)/(100,000+40,000) = 0.9286 —
  April's own crédito applies it — and the accumulator does not reset
  (FR-270).
- **AC-003:** Given an ejercicio that applied the norm with an
  effective-year deduced credit of $30,000 where the closed-year
  recalculation yields $32,000, when next January's redistribution
  runs, then a +$2,000.00 true-up posts TO THE FIRST PERIOD'S crédito
  of the new ejercicio (casilla-133 kin feed); given instead a
  recalculation of $29,000, then −$1,000.00 subtracts from that same
  period (casilla-134 kin) (FR-271, FR-275).
- **AC-004:** Given a contribuyente ceding activities in July with a
  $12,000.00 remanente, when the cessation event records, then the
  remanente enters `cessation_locked`: no refund, no offset against
  other tax debts, no transfer — and the unusable credit routes to
  gasto general per Rgto. Art. 25 (FR-279, FR-283).
- **AC-005:** Given a fusión where the absorbente society continues the
  absorbed society's registered giro, when the succession processes,
  then the absorbente INHERITS the absorbed company's $8,500.00
  remanente; given a fusión where the giro is NOT continued, or an
  aport of todo el activo y pasivo, then NO inheritance (FR-280,
  FR-282).
- **AC-006:** Given a deceased contribuyente's $5,000.00 remanente,
  when the heirs request its use, then the request is REJECTED
  (herederos bar); given the same request between economically linked
  contribuyentes, likewise REJECTED (FR-282).
- **AC-007:** Given a sociedad in liquidation holding remanente, when
  liquidation closes, then NO devolución or reintegro path exists —
  terminal state, no refund document can be generated (FR-281).
- **AC-008:** Given an occasional (non-habitual) no-sujeta operation
  with no créditos fiscales attributable to it, when the denominator
  composes, then the operation is EXCLUDED from the proportionality
  calculation (ground `no_habitual_no_credit`); given a no-sujeta
  operation of a HABITUAL activity, then it stays IN the denominator
  (FR-274; attribution test per OQ-3).
- **AC-009:** Given a donation of goods to an ISR-Art.-6 institution
  under the Art. 11 final inciso, and a sale to an accredited
  diplomatic mission declared exempt under a RATIFIED instrument, when
  the denominator composes, then BOTH operations are excluded
  (grounds `donation_11_16_isr6` / `diplomatic_instrument`) with the
  without-prejudice note recorded (FR-274).
- **AC-010:** Given a tercerización contractor paying the full
  Quincena-25 amount in January 2027, when the pass-through bills, then
  the document resolves as Factura de Consumidor Final CON VALOR EXENTO
  (FE type-01, never a CCF), the planilla copy attaches from the
  SV-PAY-FR-142 ledger, and the operation is tagged OUT of the
  pro-rata denominator (ground `quincena25_tercerizacion`) — no
  monthly factor and no annual true-up ever draws on it (FR-276,
  FR-277).
- **AC-011:** Given a period whose exentas proportion of the crédito is
  $410.00, when the run posts, then the reclassification entry moves
  $410.00 IVA crédito → costo o gasto and the monthly magnitude feeds
  casilla 132 of the F-07 block (by id through SV-FREP-FR-012's
  inputs) (FR-275).
- **AC-012:** Given a DGII exhibition requirement over the 2027
  ejercicio's recalculation base, when the requirement is served, then
  the dossier exports the per-period bucket ledgers, factors, credit
  splits and the January redistribution entries conserved for the CT
  term (FR-272).
- **AC-013:** Given a local supplier with mixed gravadas/exentas
  operations that sells $50,000 of goods to a DGII-declared 108_
  beneficiary inside the beneficiary's per-contract event window, when
  the period's denominator composes, then that sale's amount LEAVES
  the proportionality calculation (ground `energia_dl411_proveedor_local`
  — no monthly factor and no annual true-up draws on it), while the
  supplier's créditos fiscales on that operation REMAIN CREDITABLE per
  the engine's other rules (denominator-side relief as printed)
  (FR-421).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Re-verify Arts. 66-70 + the Rgto. 24-25 survivors cited here at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | R30(c) inciso mapping (tercerización): the guía 67_ anchors the no-pro-rata rule on "la parte primera del inciso sexto del artículo 66" — PRE-D.L.-224-2009 inciso numbering (the reform that restructured Art. 66); in the current print the working reading (R30(c)) maps it to the "SI NO EXISTEN CRÉDITOS FISCALES ATRIBUIBLES..." exclusion inciso — no-habitual/no-attributable-credit no-sujetas operations (LB-002; R30(c) counts it the fifth printed inciso, this file's §2 counts it sixth — ordinal discrepancy recorded, substance identical) — making the Quincena-25 FCF-exento pass-through a denominator-excluded operation (FR-277). Confirm the mapping against the pre-224-2009 text of Art. 66 (or DGII criteria) at implementation; **this row closes taxation/02 OQ-009 by pointer — the index task (T10) wires the status flip.** | no | Takumi S9 (R30(c) working reading) | open |
| OQ-3 | No-sujeta denominator attribution test (config): the LB-002 exclusion limb (a) requires that NO créditos fiscales be "attributable" to the no-sujeta operations AND that they come from non-habitual activities — the corpus states no attribution methodology (per-operation tracing vs activity-level allocation); FR-274 ships the exclusion with a configurable attribution test (never a hardcoded guess). Also re-verify the F-07 pro-rata casilla set: the extraction gloss (EVID-324) mentions "casillas 132-134/137-138" but the v14 form print attests ONLY 132/133/134 for the block (EVID-179 — no 137/138 anchor exists in 39_/34_/36_); FR-275 produces exactly the three attested inputs; confirm at implementation whether a later form version wires 137-138. | no | Takumi S9 + Odoo implementation | open |
