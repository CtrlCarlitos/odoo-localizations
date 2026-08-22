# HN — Taxation — ISR deductions: renta neta chassis, non-deductibles, personal & senior deductions, NOL

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN1 + controller |
| Updated | 2026-08-20 (V-HN1 validation fixes) |

## 1. Purpose

This file defines the functional requirements for Honduras' ISR
(*Impuesto sobre la Renta*, income tax; Decreto-Ley 25 of 1963, consolidated
through Acuerdo SAR-07-2025) *renta neta* (net taxable income) determination —
cluster T2. Covered: the Art. 11 ordinary-and-necessary deduction chassis
(*gastos ordinarios y necesarios… debidamente comprobados y pagados o
incurridos*) with its itemized heads (salaries, insurance with the
75%-reserves in-country condition, productive interest, AT-approved
depreciation, non-ISR taxes and contributions, documented property losses);
the Art. 11.g bad-debt provision engine (1% of credit sales accrual, 10%-of-AR
year-end cap excluding related-party receivables, the 24-month
*incobrabilidad* (uncollectibility) presumption ledger and the
recovery-is-taxable rule); the worker-benefit amortizations (worker housing
10%/year × 10 years; social/hygienic/cultural works 20%/year × 5 years),
gratuities within the 6-month-salary cap, depletion, donations,
social-security quotas and the representation-expense regime; the Art. 12
non-deductible catalog (depreciated-wear repairs, *inversiones* (capital
investments), personal/family expenses, partner gifts, owner/partner capital
interest, capital and luxury/recreation losses); the personal deductions of
Arts. 13/16/17 — the L40,000 no-receipt education+medical allowance, the
senior tiers (L80,000 at 65+ per D. 59-2020; +L30,000 at 60+ cited to the
D. 199-2006 — in corpus as `95_`/`96_`, evidence pass pending; the 65+ ≤
L350,000 *de pleno derecho* exemption
reforming D. 194-2002 Art. 14) — and the donation 10%-of-*renta neta gravable*
cap; the Eficiencia effective-service gate (E-Art 12); the boleta-de-compra
cost-support caps (R-Art. 22); the revaluation-tax non-deductibility
interface (D. 17-2010 L-Arts 8-12, substance owned by file 05); the payroll
prestaciones/IHSS deductibility and non-grossability interfaces (rates owned
by the payroll wave and `04_isr-withholding.md`); and the Art. 20
net-operating-loss carryforward (3-year window, 50% annual cap,
same-activity gate, AT authorization + certified-P&L attachment).

It does **not** cover: the subject/scope/rate-routing chassis
(`01_isr-framework.md`, T1/T11 — cited by id); the plantilla (withholding)
computation STACK mechanics — annualize → deduct → annual table → ÷ months —
the 13th/14th-month 10×SMM *promedio* cap amounts, scale vintages and the
senior-stack cells as consumed per payslip (`04_isr-withholding.md`,
HN-TAX-FR-121..153; this file owns the declaration-side semantics those
cells consume); ganancias de capital mechanics, the non-resident schedule
and the capital-loss ledger (`03_isr-rates-gains-minimum.md`, cluster T5,
HN-TAX-FR-081..104 — capital-loss netting at its FR-095); the
Art. 22-A minimum tax and the D. 17-2010 family (dividends, cédulas,
revaluación computation, selectivo — `05_d17-2010-family.md`,
HN-TAX-FR-166..207, revaluación FRs 184..186); ISV (`06_isv.md`,
HN-TAX-FR-211..255); payroll rates/SMM/IHSS/CT mechanics (S-HN4 wave,
`../payroll/`); and the annual-declaration filing surfaces (S-HN3 F6/F7).

## 2. Legal Basis

Authority order (binding, per master evidence index): ISR = `01_` (D.L. 25
consolidation SAR-07-2025 — current article text) with reform decree `79_`
(D. 59-2020) for the senior tiers; Eficiencia = `05_` (Enero-2022 print —
vintage caveat, 05_ OQ-2) for E-Art 12; facturación Reglamento 481-2017 =
`24_` for the boleta-de-compra caps (deduction-side interface; document
mechanics = S-HN2); D. 17-2010 = `04_` for the revaluación note (computation
owned by file 05); Ley IHSS `87_` and D. 47-2024 `27_` for worker-side
non-grossability (rates = payroll wave). D-H1/D-H2/D-H3 bind all rows:
every threshold ships as dated config resolved by the period date,
additive-only.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR, Art. 11 (encabezado y literales a-f): renta neta gravable de una empresa mercantil = renta bruta menos "gastos ordinarios y necesarios en la generación de la renta gravable... debidamente comprobados y pagados o incurridos": a) sueldos razonables y gastos normales del negocio; b) primas de seguros (la aseguradora debe mantener "por lo menos el 75% de sus reservas matemáticas... invertidas en el país"); c) intereses sobre deudas contraídas para producir la renta; d) depreciación según método aprobado por la AT; e) impuestos y contribuciones "con excepción del impuesto sobre la renta"; f) pérdidas documentadas de bienes productores de renta | Net taxable income of a mercantile enterprise = gross income minus ordinary and necessary expenses in generating the taxable renta, duly evidenced and paid or incurred: reasonable salaries and normal business expenses; insurance premiums (insurer must keep at least 75% of its mathematical reserves invested in-country); interest on debt contracted to produce the income; depreciation under an AT-approved method; taxes and contributions except the income tax itself; documented losses of income-producing property | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 11 pp.10-13 (EV01:EVID-007) |
| LB-002 | Ley ISR, Art. 11.g (deudas incobrables): provisión de "El uno por ciento (1%) del valor de las ventas de bienes o servicios al crédito" por período, con tope que "nunca será superior al diez por ciento (10%) del importe de las cuentas por cobrar a clientes al cierre" (excluyendo CxC de relacionados); se presume incobrabilidad a ">24 meses desde la fecha de su vencimiento"; las recuperaciones de castigos de años anteriores = renta gravable; no deducibles: cuentas entre familiares (cónyuges, 4º grado de consanguinidad / 2º de afinidad), socios o directores | Bad-debt provision: 1% of the value of credit sales of goods or services per period, capped at never more than 10% of client accounts receivable at close (related-party AR excluded); uncollectibility presumed at more than 24 months from the due date; recoveries of prior-year write-offs are taxable income; not deductible: receivables between family members (spouses, 4th degree blood / 2nd affinity), partners or directors | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 11.g pp.12-13 (EV01:EVID-007) |
| LB-003 | Ley ISR, Art. 11.h-k: h) amortización "del diez por ciento (10%) anual durante diez (10) años" de viviendas obreras gratuitas (condiciones higiénicas); i) amortización "del veinte por ciento (20%) anual durante cinco (5) años" de obras de carácter social, higiénico o cultural para trabajadores; j) gratificaciones al personal "siempre que no excedan del total del sueldo devengado por el beneficiario durante el período de seis meses"; k) amortización por agotamiento (depletion) | Amortization at 10% per year for 10 years of free worker housing (hygiene conditions); 20% per year for 5 years of social/hygienic/cultural works for workers; employee gratuities provided they do not exceed the total salary earned by the beneficiary over a six-month period; depletion amortization | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 11.h-k p.13 (EV01:EVID-007) |
| LB-004 | Ley ISR, Art. 11.l-n: l) donaciones al Estado, Distrito Central, municipalidades, instituciones de educación, beneficencia y deportivas legalmente reconocidas; m) cuotas de seguridad social a fondos autónomos (sin beneficio empresarial, aprobados por la AT, instituciones nacionales); n) gastos de representación y bonificaciones que formen parte del salario de propietarios, socios o ejecutivos — deducibles "únicamente para transacciones específicas... relacionadas con empresas no vinculadas"; gravables para la persona natural beneficiaria (excepto gastos de representación documentados); activos personales/educación pagados por la empresa a ejecutivos = renta gravable de éstos | Donations to the State, Central District, municipalities, legally-recognized education/charity/sports institutions; social-security quotas to autonomous funds (no enterprise benefit, AT-approved, national institutions); representation expenses and bonuses that are part of the salary of owners/partners/executives — deductible only for specific transactions related to non-related enterprises; taxable to the recipient natural person (except documented representation expenses); company-paid personal assets/education for executives are taxable income to them | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 11.l-n p.13 (EV01:EVID-007) |
| LB-005 | Ley ISR, Art. 12 (gastos no deducibles): a) reparaciones de desgaste ya depreciado; b) "Las inversiones"; c) gastos personales/familiares (salvo el artículo siguiente); d) obsequios o participaciones a socios o sus parientes hasta el 4º grado (sueldos de socios deducibles sólo como retribución real, necesaria y proporcional — a juicio de la AT); e) intereses sobre el capital invertido o prestado por propietarios, parientes o socios; f) pérdidas de capital (salvo Art. 21 [derogado]) y pérdidas por lujos o recreaciones | Non-deductible: repairs of already-depreciated wear; investments (capitalized); personal/family expenses (except the next article); gifts or participations to partners or their relatives up to 4th degree (partner salaries deductible only as real, necessary and proportionate retribution — AT judgment); interest on capital invested or lent by owners, relatives or partners; capital losses (except repealed Art. 21) and luxury/recreation losses | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 12 p.13 (EV01:EVID-008) |
| LB-006 | Ley ISR, Arts. 13, 16 y 17 (deducciones personales): a) "La suma anual hasta de CUARENTA MIL LEMPIRAS (L.40,000.00)" por educación y gastos médicos "sin necesidad de presentar comprobante alguno"; ≥65 años: L.80,000; b) gastos documentados de profesión, oficina o taller; c) agricultores/ganaderos: producción y conservación, intereses de crédito, depreciación; d) donaciones (mismos beneficiarios que 11.l) "hasta por un monto que no exceda al diez por ciento (10%) de la Renta Neta Gravable"; Art. 16: sólo residentes; Art. 17: prorrateo mensual | Personal deductions: an annual sum up to forty thousand lempiras for education and medical expenses with no voucher requirement; age 65+: L80,000; documented profession/office/workshop expenses; farmers/ranchers: production and maintenance, credit interest, depreciation; donations capped at 10% of net taxable income; residents only; monthly proration | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 13 pp.13-14; Arts. 16-17 p.14 (EV01:EVID-008) |
| LB-007 | Ley ISR, Art. 20 (arrastre de pérdidas): actividades agropecuarias, agroindustriales, manufactureras, mineras y turísticas pueden arrastrar pérdidas operativas "en los tres años de ejercicio siguiente", con amortización anual "que no exceda de CINCUENTA POR CIENTO (50%) de la renta neta gravable del año impositivo"; contribuyentes multi-actividad: "el arrastre y compensación de la pérdida sólo se hará contra las utilidades de la misma actividad que la originó"; requiere autorización de la AT + DJ anual adjuntando PyG "certificado por un Perito Mercantil y Contador Público, debidamente colegiado"; del quebranto se excluyen los gastos no deducibles del Art. 12 | Agropecuary, agro-industrial, manufacturing, mining and tourism activities may carry operating losses forward through the three following fiscal years, with each year's amortization capped at 50% of that year's net taxable renta; multi-activity taxpayers may carry and offset the loss only against profits of the same activity that generated it; requires AT authorization plus an annual DJ attaching a P&L certified by a duly colegiado mercantile expert and public accountant; Art. 12 non-deductible expenses are excluded from the loss | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 20 p.15 (EV01:EVID-009) |
| LB-008 | Ley de Eficiencia (D. 113-2011, consolidado Enero-2022), E-Art 12: los pagos por los conceptos del Artículo 5 de la Ley del ISR son deducibles "en la medida que se demuestre la prestación efectiva de los servicios recibidos" | Payments for the concepts of ISR Art. 5 are deductible only to the extent the effective provision of the services received is demonstrated (vintage caveat 05_ OQ-2) | `hn/sources/05_Ley_Eficiencia_D113-2011_actualizada.pdf` | E-Art 12 p.7 (EV05:EVID-061) |
| LB-009 | D. 59-2020 (79_), Arts. 1-3: Art. 1 añade al ISR Art. 13.a: "En el caso de las personas mayores de sesenta y cinco (65) años... la suma es de hasta OCHENTA MIL LEMPIRAS (L 80,000.00)"; Art. 2 reforma el Art. 14 del D. 194-2002: mayores de 65 "con una renta bruta hasta de TRESCIENTOS CINCUENTA MIL LEMPIRAS (L. 350,000.00), quedan exentos del pago de este impuesto... sin la necesidad de presentar comprobante alguno ni someterse a procedimientos administrativos autorizantes o trámite adicional... pudiendo los contribuyentes aplicar el beneficio de exención de pleno derecho, a partir del período fiscal en que cumplan los sesenta y cinco (65) años"; excluidas de la renta bruta de prueba: intereses y ganancias de capital (Art. 10 párr. 2 y D. 110-93 Art. 9); la AT adecuará sus sistemas; las retenciones sufridas "se les devolverán siguiendo el procedimiento que establezca SEFIN"; Art. 3: vigencia desde la publicación (La Gaceta 35,273, 4-jun-2020) | D. 59-2020: the Art. 13.a personal deduction becomes L80,000 for persons over 65; and persons over 65 with gross renta up to L350,000 are exempt from the tax — with no voucher, no authorizing administrative procedure, applying the exemption de pleno derecho from the fiscal year they turn 65; interest and capital gains are excluded from the test renta bruta; the AT must adapt its systems; wrongly-retained amounts are returned following the SEFIN procedure; effective from publication 4-Jun-2020 | `hn/sources/79_Decreto_59-2020_reforma_ISR.pdf` | D59-Arts 1-3 pp.1-2 (EV05:EVID-069) |
| LB-010 | Plantilla de Retención sobre Renta 2026 (`11_`), Instrucciones: citan D. 199-2006 (deducción adicional L30,000 ≥60 años — texto legal en corpus como `95_`/`96_`/`109_`, evidenced V-HN1b+W5c), D. 194-2002 Art. 14 (exención 65+ ≤L350,000, texto reformado en 79_), D. 59-2020 (L80,000) y el "Art. 51 del Reglamento de la Ley de ISR" (deducción de aportes de pensión — reglamento no adquirido) | SAR's official withholding workbook instructions citing the senior-tier instruments: D. 199-2006 (extra L30,000 deduction at age 60+ — statute in corpus as 95_/96_/109_, evidenced V-HN1b+W5c), D. 194-2002 Art. 14 (65+ ≤L350,000 exemption, reformed text in 79_), D. 59-2020 (L80,000) and ISR-Reglamento Art. 51 (pension-contribution deduction — regulation unacquired) | `hn/sources/11_Plantilla_Retencion_Fuente_2026.xlsx` | Instrucciones cols C/D (EV07:EVID-056) |
| LB-011 | Ley ISR, Art. 10.f/h (rentas no gravadas + deducibilidad de aportes): f) "Las indemnizaciones percibidas por riesgos profesionales y las prestaciones que otorgue el Instituto Hondureño de Seguridad Social"; h) "El valor de las prestaciones laborales, bonificación por vacaciones ordinarias de conformidad con el Código del Trabajo hasta con un pago adicional de treinta (30) días, jubilaciones, pensiones y montepíos" — con las contribuciones a su favor deducibles; "El décimo tercer mes en concepto de aguinaldo, así como el décimo cuarto mes de salario, hasta por el monto de diez (10) salarios mínimos promedio, en cada caso, a partir de cuyo monto serán gravables" | Non-grossable: occupational-risk indemnities and IHSS benefits; labor prestaciones, the ordinary vacation bonus up to one additional 30-day payment, retirements, pensions and death benefits — with employer contributions to them DEDUCTIBLE; 13th (aguinaldo) and 14th month each exempt up to 10 average minimum wages, taxable from that amount (cap computations owned by `04_isr-withholding.md` FR-127/128) | `hn/sources/01_Ley_ISR_DL25_consoliada_SAR07-2025.pdf` | Art. 10 pp.9-10 (EV01:EVID-006) |
| LB-012 | Ley IHSS (87_), Art. 92: las prestaciones en dinero "no serán gravables por impuesto alguno"; D. 47-2024 (27_), Art. 14: "Los aportes efectuados a las cuentas individuales del Fondo de Reserva Laboral de Capitalización Individual, realizadas por el patrono, no formarán parte de la renta neta gravable para el Impuesto Sobre la Renta. Adicionalmente, los valores recibidos por los (las) trabajadores(as) en concepto de prestaciones derivados de los fondos establecidos en esta Ley no formarán parte de la renta bruta para efectos del cálculo del Impuesto Sobre la Renta" | IHSS Law Art. 92: cash benefits are not taxable by any tax; D. 47-2024 Art. 14: employer contributions to individual fondo-de-reserva accounts do not form part of net taxable renta, and prestación payouts received by workers do not form part of gross renta for ISR purposes (rates/mechanics = payroll wave P5/P7) | `hn/sources/87_Ley_IHSS_TSC.pdf`, `hn/sources/27_Decreto_47-2024_Fondo_Reserva_Laboral.pdf` | LI-Art. 92 p.16 (EV81:EVID-263); 27_ Art. 14 pp.6-7 (EV27:EVID-283) |
| LB-013 | D. 17-2010 (04_), L-Arts 8-12 (revaluación voluntaria de activos): 6% "pago único y definitivo" sobre (valor de la revaluación − valor depreciado en libros); base a precio de mercado peritada por peritos colegiados; contabilizada en la cuenta de reserva "Superávit de Capital por Revaluación de Activos"; el impuesto de revaluación no es deducible ni acreditable contra el ISR (la mecánica completa es del archivo 05) | Optional asset revaluation: a one-time definitive 6% payment on the revaluation increment over depreciated book value; market basis via colegiado experts; booked to the Superávit de Capital por Revaluación reserve account; the revaluation tax is neither deductible nor creditable against ISR (computation owned by file 05, HN-TAX-FR-184..186) | `hn/sources/04_Decreto_17-2010_Ley_Fortalecimiento.pdf` | L-Arts 8-12 pp.4-5 (EV04:EVID-044) |
| LB-014 | Reglamento de Facturación (Acuerdo 481-2017, `24_`), R-Art. 22 (boleta de compra): "1. La boleta de compra debe ser utilizada única y exclusivamente para respaldar los costos y gastos... por las compras de bienes y/o prestación de servicios de mano de obra no calificada... 2. El monto total de las transacciones sustentadas mediante la boleta de compra no podrán exceder del cinco por ciento (5%) del total de gastos operativos deducibles de la Renta Bruta Gravable, excluyendo los gastos financieros. 3. Se sustentará con Boleta de Compra las compras... a una misma persona natural hondureña cuando no exceda del monto que constituye la base exenta del Impuesto Sobre la Renta en un mismo período fiscal. En caso de exceder el monto antes citado, el proveedor debe emitir factura"; R-Arts 23-24: constancia de donación emitida por el beneficiario (original al donante) | Buyer-issued purchase slip supports ONLY unskilled-labor goods/services costs; the total of boleta-supported transactions may not exceed 5% of total deductible operating expenses of gross taxable renta (financial expenses excluded); purchases from the same natural person are boleta-supported only up to the ISR exempt-base amount per fiscal year — beyond it the provider must issue a factura; the donation constancia is beneficiary-issued with the original going to the donor (document mechanics = S-HN2 wave, cluster E6) | `hn/sources/24_Reglamento_Facturacion_Ac481-2017_consolidado.pdf` | R-Art. 22 pp.28-31; R-Arts 23-24 pp.31-33 (EV24:EVID-196/197) |
| LB-015 | D. 199-2006 (95_), Art. 30 num. 14 (raw OCR, reconstruction [?]): "los beneficiarios de la presente Ley gozarán de un crédito adicional de TREINTA MIL LEMPIRAS (Lps.30,000.00) para compra de medicamentos, materiales médicos, prótesis [...]" (damaged tail — OQ-009(d)); Art. 50 vigencia: "entrará en vigencia a los veinte (20) días de su publicación" (G 31,361, 21-jul-2007 → 10-ago-2007) | THE senior-tier basis (V-HN1b read): an own-law crédito adicional of L30,000 for the law's beneficiaries (60+ or any-age jubilado per Art. 3), effective 10-ago-2007; not an ISR amendment — stacking is plantilla practice (OQ-009(c)) | `hn/sources/95_Decreto_199-2006_Ley_Adulto_Mayor.pdf` | Art. 30.14 p.8; Art. 50 p.11 (EV95:EVID-337/338) |
| LB-016 | D. 194-2002 (97_), Art. 14 ORIGINAL: 65+ exemption on renta bruta ≤ L350,000 conditioned on "[haber] pagado" Art. 22-b) ISR for 5 consecutive periods (reconstructed from scanned original; the corpus `79_` print carries only the reformed text) | Historical regime row (V-HN1b read): 2002-06-05 → 2020-06-03 the L350k/65+ exemption required 5 consecutive prior periods of Art. 22-b payment; D. 59-2020 deleted the condition and made the exemption de pleno derecho (EVID-356) — FR-068's current row cites the reformed text; this original is the pre-2020 history anchor | `hn/sources/97_Decreto_194-2002_Ley_Equilibrio_Financiero.pdf` | Art. 14 pp.7-8 (EV97:EVID-355/356) |
| LB-018 | D. 278-2013 (`130_`), Art. 5 num. 11 (survival catalogue) + D. 74-2014 (`132_`, G 33,617 27-dic-2014; Dado 10-sep-2014, Ejecútese 10-oct-2014) Art. 1 (authentic interpretation): the Ordenamiento derogated all special-law ISR exonerations EXCEPT num. 11 "Las Leyes del Adulto Mayor en cuanto a las deducciones concedidas por beneficios otorgados"; D. 74-2014 interprets num. 11: "en el sentido que éste no deroga y al contrario, conserva íntegra la vigencia de la exoneración a las personas naturales mayores de sesenta y cinco (65) años dispuesta en el Artículo 14 del Decreto Legislativo No. 194-2002" ("deducciones" reads as "exoneraciones", Constitution Art. 205-1) | The 65+ chain is CONTINUOUS across the 2013-14 Ordenamiento wave: the L350k exemption window runs 194-2002 → D. 59-2020 with NO gap (valid_from 1-ene-2014 survival row + the 27-dic-2014 authentic-interp confirmation); the print's own "164-2002" slip for 194-2002 flagged at `132_` OQ-1; also D. 278-2013 Art. 49.2 derogated D. 194-2002 Art. 48 (a different article — the Art. 14 exemption untouched) | `hn/sources/132_Gaceta_33617_Decreto_74-2014_interp_Art5_278-2013.pdf` | D74-Art. 1 (p.1; EV130:EVID-484; EV132:EVID-499) |
| LB-017 | La Gaceta 36,460 (109_), D. 59-2023 (14-feb-2024), Art. 1 reformed D. 199-2006 Art. 30, tercera-edad list: "Los adultos mayores de la tercera edad, jubilados o no jubilados y pensionados, gozarán de los descuentos siguientes: 1) Cincuenta por ciento… 2) Veinticinco por ciento… […] 13) Descuento de dos…;y, 14) Cualquiera que fuere…" (ellipses IN the gazette print — the 2007 fourteen-numeral catalogue reprinted summarized = unchanged); Art. 4: "entrará en vigencia a partir de la fecha de su publicación en el Diario Oficial 'La Gaceta'" | W5c read: the L30,000 credit (numeral 14) SURVIVES D. 59-2023 untouched — addition-only reform (Arts. 3 y 30 por adición); FR-067's row needs NO mid-life cutover; reformed BENEFICIARIOS now reads "los jubilados que cumplan con la edad" (vs 2007 "sin importar su edad" — age-bounded jubilado leg from 14-feb-2024, two readings open, OQ-009(b)); cuarta edad = 80+ defined (EVID-386, resolves 96_ OQ-2) | `hn/sources/109_Gaceta_36460_Decreto_59-2023_Adulto_Mayor.pdf` | D59-Art. 1/4 pp.1, 4; reformed Art. 30 p.3 (EV109:EVID-385/387/388) |

Dead text: none newly recorded in this cluster. Repealed ISR Art. 21 (cited
by Art. 12.f as excepted) was derogated by D. 18-90 (EV01 Cuadros 1-2) — the
capital-loss exception is inert; its treatment lives with the file-03 ledger.

## 3. Functional Requirements

### 3.1 Deduction chassis and the Art. 11 catalog

- **HN-TAX-FR-046:** The system shall determine *renta neta gravable* (net
  taxable income) as renta bruta minus *gastos ordinarios y necesarios*
  (ordinary and necessary expenses) incurred in generating the taxable renta
  that are *debidamente comprobados y pagados o incurridos* (duly evidenced
  and paid or incurred), stamping every expense line with a deductibility
  status resolved by the period date of the computation (D-H2; status
  catalog per §4). (LB-001; EV01:EVID-007)
- **HN-TAX-FR-047:** The system shall admit as deductible reasonable salaries
  and normal business expenses (Art. 11.a), consuming the payroll expense
  classification of the payroll wave (rates never restated; prestaciones
  interfaces = FR-074/075). (LB-001; EV01:EVID-007)
- **HN-TAX-FR-048:** The system shall admit insurance-premium deductions
  (Art. 11.b) flagged with the statutory insurer condition — at least 75%
  of its *reservas matemáticas* (mathematical reserves) invested in the
  country — recorded as a data attribute on the insurer partner.
  (LB-001; EV01:EVID-007)
- **HN-TAX-FR-049:** The system shall admit interest on debt contracted to
  produce the taxable renta (Art. 11.c); interest on capital invested or lent
  by owners, relatives or partners is blocked by the Art. 12.e head
  (FR-064). (LB-001; LB-005; EV01:EVID-007/008)
- **HN-TAX-FR-050:** The system shall admit depreciation only under an
  AT-approved method (Art. 11.d) carried as dated configuration — no method
  or table invented in corpus silence (Reglamento Ley ISR unacquired;
  OQ-006); the only statutory rate schedules here are FR-056/057.
  (LB-001; EV01:EVID-007)
- **HN-TAX-FR-051:** The system shall admit taxes and contributions levied on
  the taxpayer as deductible (Art. 11.e) EXCEPT the ISR itself — and except
  the revaluation tax, which is never deductible nor creditable (FR-073);
  ISV treatment is owned by `06_isv.md` and never re-derived here.
  (LB-001; LB-013; EV01:EVID-007)
- **HN-TAX-FR-052:** The system shall admit documented losses of
  income-producing property as deductible (Art. 11.f), requiring the loss
  documentation flag before the deduction is admitted. (LB-001; EV01:EVID-007)

### 3.2 Bad-debt provision engine (Art. 11.g)

- **HN-TAX-FR-053:** The system shall compute the bad-debt provision
  (*provisión para deudas incobrables*) per period as 1% of the value of
  credit sales of goods or services of the period, capped at never more
  than 10% of the balance of client accounts receivable at period close,
  with related-party receivables EXCLUDED from the cap base; admitted
  provision = min(1% × credit sales, 10% × eligible AR at close).
  (LB-002; EV01:EVID-007)
- **HN-TAX-FR-054:** The system shall maintain the 24-month receivables
  ledger: a receivable is presumed *incobrable* (uncollectible) when more
  than 24 months have elapsed from its *vencimiento* (due date); receivables
  from spouses, relatives within the 4th degree of consanguinity or 2nd of
  affinity, partners and directors are INELIGIBLE for the provision in all
  cases. (LB-002; EV01:EVID-007)
- **HN-TAX-FR-055:** The system shall recognize recoveries of amounts
  deducted as bad debts (or provisioned) in prior years as taxable income of
  the fiscal year in which the recovery is received, to the previously
  deducted amount. (LB-002; EV01:EVID-007)

### 3.3 Worker-benefit amortizations, gratuities, donations and social-security quotas (Arts. 11.h-11.n, 13.d)

- **HN-TAX-FR-056:** The system shall amortize the cost of free worker
  housing meeting the statutory hygiene conditions at 10% per year over ten
  (10) years (Art. 11.h) — a fixed statutory schedule, not configurable.
  (LB-003; EV01:EVID-007)
- **HN-TAX-FR-057:** The system shall amortize social/hygienic/cultural
  works for workers at 20% per year over five (5) years (Art. 11.i).
  (LB-003; EV01:EVID-007)
- **HN-TAX-FR-058:** The system shall admit employee gratuities
  (*gratificaciones al personal*) as deductible only up to the total salary
  earned by the beneficiary employee over the preceding six-month period
  (Art. 11.j), rejecting the excess. (LB-003; EV01:EVID-007)
- **HN-TAX-FR-059:** The system shall admit depletion amortization of
  exhaustible natural-resource assets (Art. 11.k) as a statutory
  amortization class alongside FR-056/057. (LB-003; EV01:EVID-007)
- **HN-TAX-FR-060:** The system shall admit donations (Art. 11.l) only to
  the statutory beneficiary classes — the State, the Distrito Central,
  municipalities, and legally-recognized education, charity and sports
  institutions — validating the beneficiary class on the donee partner, and
  shall link the deduction to the donee-issued *constancia de donación*
  (donation certificate, code 12; emission = S-HN2 cluster E6; the donor's
  original is the deduction support).
  (LB-004; LB-014; EV01:EVID-007; EV24:EVID-197)
- **HN-TAX-FR-061:** The system shall cap deductible donations of natural
  persons at 10% of the *renta neta gravable* (Art. 13.d), rejecting the
  excess; the RNG cap basis (before or after the donation deduction itself)
  and whether the cap extends to juridical-person donations under Art. 11.l
  are carried as OQ-005 markers on the computation. (LB-006; EV01:EVID-008)
- **HN-TAX-FR-062:** The system shall admit social-security quotas to
  autonomous funds (Art. 11.m) as deductible when the fund grants no
  enterprise benefit, is AT-approved and is a national institution —
  consuming the rate rows of the payroll wave (IHSS/RAP mechanics = S-HN4,
  never restated here). (LB-004; EV01:EVID-007)
- **HN-TAX-FR-063:** The system shall apply the representation-expense regime
  (Art. 11.n): representation expenses and bonuses forming part of the salary
  of owners, partners or executives are deductible only for specific
  transactions with non-related (*no vinculadas*) enterprises; such amounts
  are flagged taxable to the recipient natural person (except documented
  representation expenses); company-paid personal assets/education for
  executives are flagged taxable income of the executive.
  (LB-004; EV01:EVID-007)

### 3.4 Non-deductible catalog (Art. 12)

- **HN-TAX-FR-064:** The system shall classify every cost or expense against
  the Art. 12 non-deductible catalog and tag the applicable head(s):
  repairs of wear already depreciated (a); *inversiones* (capital
  investments — capitalized, recovering only via Art. 11.d depreciation,
  b); personal/family expenses except Art. 13 (c); gifts and participations
  to partners or their relatives up to the 4th degree (d) — partner salaries
  admitted only as real, necessary and proportionate retribution, subject to
  AT judgment; interest on capital invested or lent by owners, relatives or
  partners (e); and capital losses (f — routed to the ganancias-de-capital
  ledger of `03_isr-rates-gains-minimum.md` FR-095, never deducted against
  ordinary income) and luxury/recreation losses (f). (LB-005; EV01:EVID-008)

### 3.5 Personal deductions and the senior tiers (Arts. 13, 16-17; D. 59-2020)

- **HN-TAX-FR-065:** The system shall apply personal deductions only to
  residents (Art. 16), exposing the Art. 17 monthly proration for
  withholding-side consumption while the annual declaration consumes the
  annual amounts (plantilla-side = `04_isr-withholding.md` FR-131).
  (LB-006; EV01:EVID-008)
- **HN-TAX-FR-066:** The system shall compute the education+medical personal
  deduction as DATED CONFIG: an annual sum up to L40,000 with no voucher
  requirement (*sin necesidad de presentar comprobante alguno*) for
  taxpayers up to 64 years, and L80,000 from the fiscal year the taxpayer
  turns 65 (D. 59-2020, valid_from 4-jun-2020 publication; birthday-year
  activation per the D-H2 payroll resolution key); no IPC clause (OQ-001).
  (LB-006; LB-009; EV01:EVID-008; EV05:EVID-069)
- **HN-TAX-FR-067:** The system shall apply the additional senior deduction
  of L30,000 from the fiscal year the taxpayer turns 60, stacking on
  FR-066 — statutory basis **PINNED V-HN1b: D. 199-2006 Art. 30 numeral
  14** (the Adulto Mayor law's own "crédito adicional de TREINTA MIL
  LEMPIRAS", EVID-338; NOT an ISR Art. 13 amendment — the law reforms
  nothing external), **valid_from 10-ago-2007** (Art. 50: 20 days after
  publication in G 31,361 of 21-jul-2007, EVID-337) and confirmed
  WHOLE-LIFE by the W5c read of the intermediate reform D. 59-2023
  (`109_`, EVID-388: the 2007 catalogue including numeral 14 is reprinted
  summarized-unchanged — the credit SURVIVES; no mid-life cutover row);
  the row is ACTIVE on the plantilla computation contract (SAR operates
  the tier; stacking is plantilla practice — the statute itself contains
  no stacking bridge, OQ-009). Carried caveats: the beneficiary class is
  the law's "beneficiarios" — 60+ OR any-age jubilado per the 2007 Art. 3
  (EVID-347), with the reformed D. 59-2023 text (from 14-feb-2024)
  reading "los jubilados que cumplan con la edad" (age-bounded leg, two
  readings open — broader than/diverging from the plantilla's 60-turn
  gate either way; encoded per the plantilla, flag OQ-009(b)).
  (LB-010; LB-015; LB-017; EV07:EVID-056; EV95:EVID-337/338/347;
  EV109:EVID-385/388)
- **HN-TAX-FR-068:** The system shall apply the 65+ exemption *de pleno
  derecho* (of full right) on the declaration side: a taxpayer over 65 whose
  renta bruta — excluding interest and ganancias de capital, which remain on
  their own tracks — does not exceed L350,000 is exempt with no voucher and
  no authorizing administrative procedure, from the fiscal year the
  taxpayer turns 65 (D. 59-2020 reforming D. 194-2002 Art. 14; valid_from
  4-jun-2020; fixed lempiras — OQ-001 kin); wrongly-retained amounts are
  returned per the SEFIN procedure (unacquired — OQ-003; devolution-request
  flag only). W9 continuity pin: the exemption SURVIVED the 2013-14
  Ordenamiento derogation wave (D. 278-2013 Art. 5 num. 11 + D. 74-2014
  authentic interpretation — LB-018; no FY2014 gap exists).
  (LB-009; LB-017; EV05:EVID-069; EV130:EVID-484; EV132:EVID-499)
- **HN-TAX-FR-069:** The system shall admit documented expenses of the
  taxpayer's profession, office or workshop as a personal deduction
  (Art. 13.b), requiring document linkage before admission.
  (LB-006; EV01:EVID-008)
- **HN-TAX-FR-070:** The system shall admit the farmer/rancher personal
  deductions (Art. 13.c): production/maintenance expenses, credit interest
  and depreciation of the agricultural activity. (LB-006; EV01:EVID-008)

### 3.6 Cross-cutting gates: effective service, boleta caps, revaluation

- **HN-TAX-FR-071:** The system shall gate the deductibility of payments for
  the concepts of ISR Art. 5 (the services/fees categories) on proof of the
  *prestación efectiva* (effective provision) of the services received —
  payments without such proof are non-deductible until evidenced (Eficiencia
  E-Art 12; consolidation-vintage caveat OQ-004).
  (LB-008; EV05:EVID-061)
- **HN-TAX-FR-072:** The system shall enforce the boleta-de-compra
  cost-support caps on the deduction side (R-Art. 22): (a) boleta-supported
  transactions support only unskilled-labor (*mano de obra no calificada*)
  goods/services costs; (b) their total per fiscal year may not exceed 5% of
  total deductible operating expenses of the renta bruta gravable
  (financial expenses excluded) — excess amounts unsupported by other
  documents are non-deductible; (c) purchases from the same natural-person
  provider are boleta-supported only up to the ISR exempt-base amount of the
  fiscal year (resolved from the dated scale rows of
  `04_isr-withholding.md` FR-121; snapshot-on-write per D-H2), beyond it a
  *factura* is required; boletas never support ISV *crédito fiscal*
  (ISV = `06_isv.md`; emission = S-HN2 cluster E6).
  (LB-014; EV24:EVID-196)
- **HN-TAX-FR-073:** The system shall exclude the D. 17-2010 revaluation tax
  (6% *pago único y definitivo* on the revaluation increment) from every
  deductible-expense class and from every ISR credit surface — it is neither
  deductible nor creditable; the revaluation computation, expert-appraisal
  basis and the *Superávit de Capital por Revaluación* reserve account are
  owned by `05_d17-2010-family.md` (HN-TAX-FR-184..186).
  (LB-013; EV04:EVID-044)

### 3.7 Payroll deductibility interfaces (rates owned elsewhere)

- **HN-TAX-FR-074:** The system shall admit employer contributions to
  pension and *previsión* funds — public systems (INJUPEMP/INPREUNAH/IPM)
  and private (RAP/AFP) — as deductible per Art. 10.h ("contributions in
  their favor are deductible") together with Art. 11.m, consuming the
  contribution amounts from the payroll wave and `04_isr-withholding.md`
  FR-132 (plantilla-side worker-contribution deduction; the unacquired
  "Reglamento Art. 51" citation rides its OQ-003).
  (LB-011; LB-004; EV01:EVID-006/007)
- **HN-TAX-FR-075:** The system shall stamp the worker-side non-grossable
  payroll classifications as a deduction-file interface: IHSS benefits and
  occupational-risk indemnities (Art. 10.f); labor *prestaciones*, the
  vacation bonus up to the additional 30-day payment, jubilaciones,
  pensiones and *montepíos* (Art. 10.h); IHSS cash benefits — never taxable
  by any tax (LI Art. 92); RAP fondo aportes/prestaciones — outside renta
  (D. 47-2024 Art. 14); rates, ceilings and payout mechanics = payroll wave
  (P5/P7), never restated. (LB-011; LB-012; EV01:EVID-006; EV81:EVID-263;
  EV27:EVID-283)

### 3.8 Net-operating-loss carryforward (Art. 20)

- **HN-TAX-FR-076:** The system shall restrict NOL carryforward eligibility
  to losses from agropecuary, agro-industrial, manufacturing, mining and
  tourism activities, requiring (a) AT authorization on the loss, (b) the
  annual DJ attaching a P&L certified by a *Perito Mercantil y Contador
  Público debidamente colegiado* (collegiated mercantile-expert public
  accountant), and (c) loss composition EXCLUDING Art. 12 non-deductible
  expenses (FR-064 heads added back out of the loss).
  (LB-007; EV01:EVID-009)
- **HN-TAX-FR-077:** The system shall carry an eligible operating loss
  forward only through the three (3) fiscal years following the loss year,
  expiring the remainder at the third year's close. (LB-007; EV01:EVID-009)
- **HN-TAX-FR-078:** The system shall apply each year's NOL amortization
  with both statutory limits: the applied amount may not exceed 50% of the
  renta neta gravable of the offsetting fiscal year, and — for
  multi-activity taxpayers — the loss offsets only against profits of the
  SAME activity that generated it (activity dimension required on loss and
  income sides; taxonomy = OQ-007). (LB-007; EV01:EVID-009)

## 4. Data Model

Machine-readable sidecars (non-deductible head catalog, senior-tier dated
rows) live next to this markdown file when produced. Dated statutory values
are additive `valid_from`/`valid_to` rows resolved by the period date
(D-H2); amounts never hardcode into code.

**Deduction classification (chassis + Art. 12 catalog):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line | hn_isr_deductibility_status | select | deductible · non_deductible · partially_deductible · pending_evidence | FR-046, FR-064 |
| account.move.line | hn_isr_nondeductible_head | m2o catalog | depreciated_wear_repair · investment_capitalized · personal_family · partner_gift_participation · owner_partner_interest · capital_loss · luxury_recreation · related_party_baddebt · gratuity_excess · donation_cap_excess · boleta_cap_excess · effective_service_unproven | FR-054, FR-058, FR-061..064, FR-071, FR-072 |
| account.move.line | hn_isr_loss_documented | boolean | Art. 11.f loss-documentation gate | FR-052 |

**Bad-debt engine:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isr.baddebt.provision (new) | period, credit_sales, accrued_1pct, ar_close_total, ar_related, cap_10pct, admitted | monetary/computed | admitted = min(1% × credit sales, 10% × (AR_close − related AR)) | FR-053 |
| account.move.line (receivable) | hn_isr_vencimiento, hn_isr_months_overdue, hn_isr_incobrable_presumed | date/computed/boolean | presumption at >24 months from vencimiento | FR-054 |
| res.partner | hn_isr_baddebt_related | boolean | spouses / ≤4th-degree consanguinity / ≤2nd affinity / partners / directors → receivables ineligible | FR-054 |
| account.move.line | hn_isr_baddebt_recovery | boolean (posted) | recovery of prior-year write-off → taxable income line | FR-055 |

**Amortizations, gratuities, donations, social security:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset | hn_isr_amortization_scheme | select | worker_housing_10pct_10y · social_works_20pct_5y · depletion (statutory fixed schedules) | FR-056, FR-057, FR-059 |
| account.move.line (gratuity) | hn_isr_gratuity_cap | computed | ≤ total 6-month beneficiary salary | FR-058 |
| res.partner (donee) | hn_isr_donation_class | select | state · distrito_central · municipality · education · charity · sports (legalmente reconocidas) | FR-060 |
| l10n_hn.isr.donation.cap (new) | fiscal_year, rng_basis, cap_10pct, donations_total, admissible | computed | cap = 10% × RNG (basis per OQ-005); PN-side | FR-061 |
| res.partner (insurer) | hn_isr_reserves_75pct_incountry | boolean | Art. 11.b insurer condition | FR-048 |
| account.move.line (payroll) | hn_isr_pension_contrib_deductible | boolean | employer pension/previsión contributions | FR-074 |
| account.move.line | hn_boleta_supported, hn_isr_effective_service_proof | boolean/select | boleta cost support (unskilled labor only); effective-service proof: proven · unproven · not_applicable | FR-071, FR-072 |
| l10n_hn.isr.boleta.cap (new) | fiscal_year, deductible_opex_ex_financial, cap_5pct, boleta_total, per_provider_aggregates, exempt_base_snapshot | computed | aggregate 5% guard; per-provider ≤ exempt base (snapshot from the FR-121 scale row; D-H2) | FR-072 |

**Personal deductions and senior tiers (dated config):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isr.parameter (dated rows) | parameter, value, valid_from, valid_to, instrument | monetary/dates | personal_deduction_general = 40,000 (1963 text, no IPC clause); personal_deduction_65plus = 80,000 (D. 59-2020, valid_from 2020-06-04); senior_extra_60plus = 30,000 (D. 199-2006, valid_from 2007-08-10 — survives D. 59-2023 unchanged, EVID-388); senior_exempt_bruta_65plus = 350,000 (79_ Art. 2 re D. 194-2002 Art. 14, valid_from 2020-06-04) | FR-066..068 |
| res.partner / res.users (taxpayer) | birthdate, hn_isr_senior_tier (computed) | date/select | none · extra_30k_from_60 · deduction_80k_from_65 · exempt_350k_from_65 (birthday-year rule, D-H2) | FR-066..068 |
| l10n_hn.isr.devolution.request (new) | taxpayer, period, amount, basis | m2o/monetary | 65+ wrongly-retained flag; SEFIN procedure unacquired (OQ-003) | FR-068 |

**NOL ledger:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.isr.nol.ledger (new) | origin_fy, activity, sector, loss_amount, expires_fy, at_authorized, certified_pl_attachment | dates/amounts/flags | sectors: agropecuaria · agroindustrial · manufacturing · mining · tourism; activity taxonomy = OQ-007 | FR-076, FR-077 |
| l10n_hn.isr.nol.application (new) | fy, nol_id, rng, cap_50pct, same_activity_utilidades, applied | computed | applied = min(remaining, 50% × RNG, same-activity profits) | FR-078 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic in
the LGPL client. No `saas`/`shared` rows: none of these FRs touch a
transmission/DTE surface (HN's facturación channel is paper-CAI; SEE blocked
on unpublished docs — W3 lead 1); constancia/boleta emission = S-HN2
surfaces consumed by id. Models stable across Odoo 17/18/19/20;
version-specific behavior recorded where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-046 | odoo | account.move.line | hn_isr_deductibility_status | Master gate evaluated at period close; feeds the annual-declaration adjustment bridge (S-HN3 F7) |
| FR-047 | odoo | account.move.line (payroll journals) | salary-expense classification | Consumes hr.expense/hr.salary-rule postings; rates never restated (W4) |
| FR-048 | odoo | res.partner (insurer) + account.move.line | hn_isr_reserves_75pct_incountry | Data-entry flag; default true for national insurers, editable with audit trail |
| FR-049 | odoo | account.move.line | interest classification | Productive-debt tag; owner/partner/relative-lender lines auto-tagged head owner_partner_interest (FR-064) |
| FR-050 | odoo | account.asset + l10n_hn.isr.parameter | depreciation method config | AT-approved method as dated config; no schedule invented (OQ-006); depreciation engine = Odoo native asset model |
| FR-051 | odoo | account.move.line (tax expense accounts) | tax-kind resolver | ISR accounts excluded by account mapping; revaluation accounts hard-excluded (FR-073) |
| FR-052 | odoo | account.move.line | hn_isr_loss_documented | Documentation attachment required before admission |
| FR-053 | odoo | l10n_hn.isr.baddebt.provision | period computation | Runs at FY close; related-AR exclusion from cap base via partner flag |
| FR-054 | odoo | account.move.line (receivables) + res.partner | 24-month ledger | Months-overdue computed from vencimiento (invoice due_date); kinship/partner flags drive ineligibility |
| FR-055 | odoo | account.move.line | recovery posting | Recovery payments post taxable-income line referencing the write-off year |
| FR-056, FR-057, FR-059 | odoo | account.asset | hn_isr_amortization_scheme | Fixed statutory schedules seeded as scheme rows (10×10%, 5×20%, depletion class); not user-rate-editable |
| FR-058 | odoo | account.move.line + hr.employee | gratuity cap | 6-month beneficiary salary resolved from payroll history (W4 feed) |
| FR-060 | odoo | res.partner (donee) + account.move.line | donation_class | Constancia linkage field references S-HN2 document type 12 by id |
| FR-061 | odoo | l10n_hn.isr.donation.cap | cap computation | RNG basis configurable pending OQ-005 (default RNG-before-donations); PN-side cap |
| FR-062 | odoo | account.move.line (SS contributions) | fund validation | AT-approved national fund flags on res.partner; rates from W4 rows |
| FR-063 | odoo | account.move.line | representation regime | Non-vinculada transaction link required; recipient-taxable flag feeds payroll/informative surfaces |
| FR-064 | odoo | account.move.line | hn_isr_nondeductible_head catalog | Head catalog seeded from Art. 12; capital-loss head routes to the 03-file GC ledger (FR-095), never ordinary deduction |
| FR-065 | odoo | res.partner (taxpayer) | residency gate | Resident flag consumed from the 01-file subject profile (HN-TAX-FR-003) |
| FR-066 | odoo | l10n_hn.isr.parameter + birthdate | dated rows | D. 59-2020 cutover valid_from 2020-06-04; birthday-year activation (D-H2); snapshot-on-write |
| FR-067 | odoo | l10n_hn.isr.parameter | pinned dated row | valid_from 2007-08-10 (V-HN1b); row ACTIVE on the plantilla contract; survives D. 59-2023 unchanged (W5c, EVID-388); <60-jubilado edge = flag-only (OQ-009(b)) |
| FR-068 | odoo | l10n_hn.isr.parameter + computation | 65+ exemption | Test base excludes interest/GC lines (rate-track routing per 01-file FR-013); devolution-request flag (OQ-003) |
| FR-069, FR-070 | odoo | account.move.line | documented-expense gates | Document linkage mandatory; farmer/rancher activity dimension consumed from activity coding |
| FR-071 | odoo | account.move.line | hn_isr_effective_service_proof | Applies to Art. 5-concept payments; evidence attachment flips unproven→proven |
| FR-072 | odoo | l10n_hn.isr.boleta.cap + account.move.line | caps | Aggregate 5% guard at FY close; per-provider aggregation job; exempt-base snapshot from FR-121 vintage rows (04 file) |
| FR-073 | odoo | account.account (revaluation accounts) + exclusion rule | never-deduct/credit | Cross-file invariant vs `05_d17-2010-family.md` HN-TAX-FR-184..186 (its l10n_hn.asset.revaluation feeds the non-deductible flag); blocked at account level |
| FR-074 | odoo | account.move.line (payroll) | pension-contribution deduction | Amounts from W4 payslip engine; plantilla-side counterpart = 04 FR-132 |
| FR-075 | odoo | hr.salary.rule / account.move.line stamps | non-grossable classes | Classification only; IHSS/RAP mechanics and rates = W4 P5/P7 |
| FR-076 | odoo | l10n_hn.isr.nol.ledger | eligibility + gates | Sector list as config; certified-P&L attachment requirement; AT-authorization workflow flag |
| FR-077 | odoo | l10n_hn.isr.nol.ledger | expires_fy | origin_fy + 3; expiry sweep at FY close |
| FR-078 | odoo | l10n_hn.isr.nol.application | dual-cap application | min(remaining, 50% RNG, same-activity profits); activity dimension required (OQ-007) |

Version-regime notes (D-H2/D12): FR-066/FR-068 record the D. 59-2020
cutover (valid_from 4-jun-2020 publication = vigencia; birthday-year
activation of the 65+ tiers); FR-067's row = valid_from 10-ago-2007,
whole-life (the D. 59-2023 intermediate reform leaves numeral 14
untouched — W5c null-with-proof), with the beneficiary-class divergence
carried as OQ-009(b). FR-061/FR-072
parameters (donation-cap RNG basis; exempt-base snapshots) resolve as-of the
computation's period date with snapshot-on-write (D15). All other rules were
verified stable in the SAR-07-2025 consolidation (no post-reform touching
Arts. 11-13/20 beyond D. 59-2020 and the repealed Art. 21 exception — EV01
Cuadros 1-2).

## 6. Acceptance Criteria

- **AC-001:** Given an expense line without documentary support at period
  close, when deductibility resolves, then hn_isr_deductibility_status =
  pending_evidence and no deduction enters renta neta gravable (FR-046).
- **AC-002:** Given FY2026 credit sales of L2,000,000 and client AR at close
  of L150,000 including L30,000 of director receivables, when the bad-debt
  provision computes, then accrual = 1% × 2,000,000 = L20,000, cap = 10% ×
  (150,000 − 30,000) = L12,000, and the admitted provision = L12,000
  (FR-053).
- **AC-003:** Given a client receivable with vencimiento 1-June-2024
  evaluated at the FY2026 close, then months-overdue = 31 and
  hn_isr_incobrable_presumed = true; given the same age receivable from a
  partner, then it is ineligible for the provision regardless of age
  (FR-054).
- **AC-004:** Given L5,000 recovered in 2026 on a receivable written off in
  2023, then a L5,000 taxable-income line posts to FY2026 (FR-055).
- **AC-005:** Given worker housing costing L800,000 meeting the hygiene
  conditions, then L80,000 deducts per year for 10 years; given social works
  of L250,000, then L50,000 per year for 5 years (FR-056, FR-057).
- **AC-006:** Given a gratuity of L120,000 to an employee whose preceding
  6-month salary totals L90,000, then the deductible amount = L90,000 and
  the L30,000 excess is tagged gratuity_excess (FR-058, FR-064).
- **AC-007:** Given a resident PN with RNG before donations of L300,000 and
  donations of L45,000 to a municipal education foundation, then the cap =
  10% × 300,000 = L30,000, the admissible donation = L30,000, and the
  OQ-005 basis marker rides the computation (FR-060, FR-061).
- **AC-008:** Given interest paid on capital lent by a shareholder, a repair
  of fully-depreciated wear, and a capital loss on share disposal, then the
  lines resolve to heads owner_partner_interest, depreciated_wear_repair and
  capital_loss — the first two non-deductible, the third routed to the
  03-file ganancias-de-capital ledger (FR-095), never against ordinary
  income (FR-049, FR-064).
- **AC-009:** Given a resident PN aged 63, then the deduction stack =
  L40,000 + L30,000 (FR-067 row pinned) = L70,000; given age 67 with renta
  bruta L380,000 (no interest/GC), then the deduction = L80,000 and no
  L350,000 exemption; given age 67 with test renta bruta L300,000, then the
  exemption de pleno derecho applies and the ordinary base = L0 (FR-066..068).
- **AC-010:** Given a 68-year-old with salary L300,000 and bank interest
  L80,000, when the 65+ exemption test runs, then the test base = L300,000
  (interest excluded) → exemption applies; the L80,000 interest remains on
  its own rate track (FR-068).
- **AC-011:** Given a L200,000 payment for an ISR Art. 5-concept service
  with no prestación-efectiva evidence on file, then the line is
  non-deductible (head effective_service_unproven) until evidence attaches
  (FR-071).
- **AC-012:** Given FY2026 deductible operating expenses (ex-financial) of
  L1,000,000 and boleta-compra-supported transactions totaling L60,000, then
  the aggregate cap = 5% × 1,000,000 = L50,000 and L10,000 is
  non-deductible unless otherwise documented; given FY-total boleta
  purchases from one provider of L230,000 vs the FY2026 exempt base
  L228,324.32 (snapshot), then a factura is required for the excess
  (FR-072).
- **AC-013:** Given a revaluation increment of L1,000,000 taxed at 6%
  (L60,000, per `05_d17-2010-family.md` FR-184..186), then the L60,000
  appears in no deductible-expense class and no ISR credit ledger of this
  file (FR-051, FR-073).
- **AC-014:** Given a FY2024 tourism operating loss of L100,000
  (AT-authorized, certified P&L attached, Art. 12 addbacks excluded), then
  FY2025 tourism RNG of L60,000 absorbs at most L30,000 (50% cap) leaving
  L70,000 carried, FY2025 manufacturing profit L200,000 absorbs L0
  (same-activity gate), and any remainder expires at the FY2027 close
  (FR-076..078).
- **AC-015:** Given an employer RAP contribution posted by the payroll
  engine and an IHSS sickness subsidy paid to a worker, then the employer
  contribution is deductible (FR-074) and the subsidy is stamped
  non-grossable to the worker (FR-075; LI Art. 92).
- **AC-016:** Given a municipal contribution caused and paid in FY2026 and
  the FY2026 ISR liability itself, then the first is deductible and the
  second rejected by the tax-kind resolver (FR-051).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | L40,000/L80,000 personal-deduction and L350,000 65+ exemption vintages (origin `01_ OQ-5`, register C1): fixed lempiras, NO IPC clause (last reformed D. 59-2020; the Art. 22.b propagation sentence arguably reaches only scale-referencing values, not Art. 13) — Cuadro 2 shows no post-2020 reform; FR-066/068 ship fixed dated rows; verify SAR/Ayuda-102 practice does not index them before freezing. | no | Takumi S-HN3 (Ayuda 102 check) | open |
| OQ-002 | 13th/14th-month excess semantics (origin `01_ OQ-4`, register C1) — RESOLVED at synthesis: "hasta por el monto de diez (10) salarios mínimos promedio, en cada caso, a partir de cuyo monto serán gravables" = EXCESS-ONLY (never a cliff), proven by the plantilla computation contract (EV07:EVID-055 IF-semantics = FR-127/128 of `04_isr-withholding.md`); SMM measure = the single national *promedio* (R-H47; 04-file OQ-007: FY2026 = L14,917.20 → cap L149,172.00). Residual: missing promedio vintages remain payroll P1 leads. | no | Takumi S-HN1 | resolved |
| OQ-003 | SEFIN devolution procedure for 65+ ≤L350,000 wrongly-retained amounts (origin `05_ OQ-5`, register C1): D59-Art 2 mandates return "siguiendo el procedimiento que establezca SEFIN" but the procedure is not in corpus; FR-068 records the mandate and the devolution-request flag only — LEAD. | no | acquisition queue | open |
| OQ-004 | Eficiencia consolidation vintage for E-Art 12 (origin `05_ OQ-2`, register C1; kin of 04-file OQ-009 which carries it for E-Arts 35/52): print = Enero-2022, reforms footnoted only through D. 7-2017 — FR-071 stands on the 2022 print; re-verify if any post-2022 Eficiencia reform surfaces. | no | Takumi S-HN1 | open (verify) |
| OQ-005 | NEW (synthesis finding): donation-cap basis — Art. 13.d caps PN donations at 10% "de la Renta Neta Gravable" without stating whether RNG is computed before or after the donation deduction (no SV-style explicit formula); and Art. 11.l (business donations) states no cap — whether the 10% cap extends to juridical persons is corpus-silent. FR-061 defaults to RNG-before-donations, PN-side, marker attached; pin vs Ayuda 102/103 practice (S-HN3). | no | Takumi S-HN3 | open |
| OQ-006 | Depreciation "según método aprobado por la AT" (Art. 11.d) — approved methods/tables live in the unacquired Reglamento Ley ISR ("Acuerdo N°799"; kin `07_ OQ-3`/`13_ OQ-2`): FR-050 carries method as dated config; no schedule invented. **W8/R-H83:** the instrument is IDENTITY-DECODED via the official congreso inventory (`119_` entry 324, EV119:EVID-479): Reglamento Ley ISR = **Acuerdo 799, G 19,972 (13-ene-1970)**, derogating the 1955 reglamento, its Art. 33 reformed by Acuerdo 6-B (G 21,505 4-feb-1975); the "799-1963"-style year suffixes in manual citations = slips (1963 = the LEY's year). TEXT still unacquired (1970 gazette, pre-ENAG) — citations remain print-based, never asserted as acquired text. | no | acquisition queue (identity pinned) | open (LEAD kin) |
| OQ-007 | NEW (synthesis finding): NOL same-activity taxonomy — "la misma actividad que la originó" requires an activity classification register (beyond the five eligibility sectors) and the AT-authorization instrument/procedure is unpinned; FR-076/078 encode activity as a mandatory ledger dimension with the catalog open. | no | Takumi S-HN1 + acquisition queue | open (config) |
| OQ-008 | Senior L30,000 @60+ statutory basis → **RESOLVED V-HN1b (2026-08-20, `95_`+`96_` evidence read, EVID-337..348):** basis = D. 199-2006 Art. 30.14 (own-text crédito, not an ISR amendment), valid_from 10-ago-2007; FR-067 row PINNED + ACTIVE. `96_` (D. 45-2025) verified NOT to touch deductions (services-discount side only). Residual carries moved to OQ-009. | no | — | resolved |
| OQ-009 | (a) intermediate reform D. 59-2023 scope → **RESOLVED W5c (2026-08-20, `109_` evidence read, EVID-385..388):** "Reformar por adición los artículos 3 y 30" — the L30,000 credit (Art. 30.14) SURVIVES unchanged (tercera-edad list reprinted summarized 1)-14) with gazette ellipses); vigencia = publication day 14-feb-2024; FR-067 needs NO mid-life cutover row. (b) beneficiary-class mismatch — UPDATED with the reformed text: 2007 wording (60+ OR any-age jubilado, "sin importar su edad") valid 10-ago-2007→13-feb-2024; reformed wording from 14-feb-2024 reads "los jubilados que cumplan con la edad" (age-bounded leg — narrowing vs drafting-slip readings both open, `109_` OQ-1; affects only the <60-jubilado edge, which flags rather than computes under the encoded plantilla gate either way); (c) STACKING CONFLICT — unchanged: the L30k "adicional" has NO statutory bridge to the L40k/L80k Art. 13 stack in 95_, 109_, 79_ or 01_ (plantilla-only practice; never resolve silently); (d) "crédito" vs "deducción" mechanics + the 95_ OCR-damaged expense-tail (flat vs expense-limited — plantilla implements flat); residual lead = clean/consolidated D. 199-2006 text (`109_` OQ-2 — the gazette ellipses point at the still-damaged 2007 print). | no (row active on plantilla contract) | controller ruling (b) + consolidation lead (d) | open |
