# SV — Taxation — ISR framework: subjects, renta obtenida, territoriality & filing

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft |
| Authors | Takumi synthesis wave 2 (S2 ISR) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional framework for El Salvador's *Impuesto sobre la
Renta* (ISR, income tax): the *renta obtenida* (obtained income) concept and its
four categories plus the catch-all inclusions; the ISR subject registry
(including *sucesiones*, estates, *fideicomisos*, trusts, *conjuntos*, visiting
artistic/sports ensembles, and *sociedades irregulares o de hecho*, de-facto or
irregular societies); the Art. 6 exclusions with the *utilidad pública* (public
utility) qualification cycle; the fiscal-year calendar and cash/accrual
computation methods per taxpayer type (including the irrevocable accrual
election for natural persons); estate/trust period splits; branch consolidation;
foreign-currency conversion per Código Tributario (Tax Code, CT) Art. 62; the
territorial source classifier with the D.L. 969-2024 foreign-source exclusion
and the Art. 127 partial-territory apportionment; and the annual
declaration/payment framework with the Art. 92 filing-duty catalog, conjunto
event returns, online-only filing and the retention-remittance deadline.

It does **not** cover: rates, brackets and special computations including the
10% separate liquidations and capital gains (`03_isr-rates-gains.md`,
clusters T4); deductions, non-deductibles and the Art. 28 pro-rata allocator
itself (`02_isr-deductions.md`, T3); payroll withholding tables and
retention mechanics (`04_isr-withholding.md`, T5); the 5% distributions regime
(`05_isr-distributions.md`, T6); fixed-asset depreciation and software
amortization (`06_isr-assets.md`, T7); IVA (`e-invoicing/` A10); or sanctions
and administrative procedure, which route to the Código Tributario (CT). Those
files reference this one for the subject/period/territoriality framework.

## 2. Legal Basis

Authority order (binding, per master evidence index S2): 54_ (consolidated Ley
ISR, current article text) with reform decrees 55_ (Art. 37), 56_ (D.L. 969-2024
— Art. 3.4 + derogations), 57_/58_ (interpretaciones auténticas) for changed
articles > 03_ (historical consolidation through D.L. 233-2012; supplies
analysis via EVID ids). Reglamento: 04_ = D.E. 101-1992 as consolidated with
reforms D.E. 8-1993 / 39-1993 / **117-2001** (self-documented repeal map — R17);
only survivor articles are cited. Retention-tables decree 53_ cited only for
the filing/threshold bits. Every Ley article below was re-verified in the 54_
consolidation text (54_-verify rule; EVID-166 residual-risk note). **75_
vintage watch (rides the 75_ row below):** the D.E. 117-2001 print carries NO
REFORMAS block and post-2001 repeal by CT Art. 344 ff is print-unresolvable
(EV75 OQ-1/OQ-8, SOQ-06-kin) — cited as printed.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley ISR (D.L. 134-1991, texto consolidado), Art. 1 | Taxable event: obtaining renta by subjects in the fiscal period generates the ISR obligation | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 1 p.1 (EVID-088) |
| LB-002 | Ley ISR, Art. 2 + interpretación auténtica D.L. 629-1993 | Renta obtenida: products/utilities received or accrued in cash or in kind from any source; categories a) trabajo, b) actividad empresarial, c) capital, d) catch-all (condoned debts, undocumented liabilities, excess provisions, unjustified patrimony increments per CT Art. 195); D.L. 629: public officials' gastos de representación are not remuneration | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 2 pp.2-3 + D.L. 629 reproduced pp.2-3 (EVID-088) |
| LB-003 | Ley ISR, Art. 3 nums. 1-3 | Not renta: reasonable viáticos/work tools/uniforms/office equipment necessary for the employer's income production (documented per CT Arts. 107/119); legacies and inheritances; donations between ascendants/descendants within 2nd degree and spouses (antecesor's value/date carries over) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 3.1-3.3 pp.3-4 (EVID-088/089 carried) |
| LB-004 | Ley ISR, Art. 3 num. 4 (heading + numeral added by D.L. 969-2024, stamp (24)) | Foreign-source exclusion: ALL values obtained abroad in any concept, money or kind, by any subject domiciled or not, are excluded from the renta concept; subjects with gravadas rents AND these excluded concepts are excluded from the Art. 28-final pro-rata mechanism | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 3.4 p.4 (EVID-164) |
| LB-005 | Ley ISR, Art. 5 | Subjects: natural/juridical persons domiciled or not; sucesiones and fideicomisos; artists/sportsmen individually or in conjuntos (non-domiciled temporary groups = one subject); sociedades irregulares o de hecho y uniones de personas; related subjects & preferential-regime jurisdictions per CT | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 5 p.7 (EVID-090) |
| LB-006 | Ley ISR, Art. 6 | Exclusions: Estado, municipalidades, public-law and utilidad-pública corporations/foundations (non-profit, exclusive destination of income/assets, no distributions); DGII must qualify in advance and may revoke | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 6 pp.7-8 (EVID-090) |
| LB-007 | Reglamento ISR (D.E. 101-1992 consolidado), Arts. 2, 6-7 | Reglamento subjects mirror Art. 5; exclusion never lifts formal duties; utilidad-pública qualification dossier (D.O. statutes, member roster, board certificate) and 12-month qualification periods aligned to the fiscal year, auto-renewed absent official revocation | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 2, 6-7 pp.2-4 (EVID-129) |
| LB-008 | Ley ISR, Arts. 12-13 | Determination = sum of products/utilities of all income sources; 12-month ejercicios Jan 1-Dec 31 for natural and juridical persons; liquidation on cessation/definitive departure; rent presumed obtained at midnight of period end; each period liquidated independently, save legal exceptions | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Arts. 12-13 p.9 (EVID-091) |
| LB-009 | Ley ISR, Art. 17 | Natural persons compute on the cash method (constructive receipt: availability); accounting-obligated natural persons must use accrual; non-obligated may elect accrual (auxiliary records; inform DGII in Nov-Dec of the prior ejercicio); once adopted, accrual is irrevocable | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 17 p.12 (EVID-091) |
| LB-010 | Ley ISR, Arts. 18-23 | Usufructo legal of unemancipated children attributed to parents (halves or per common law); deceased's final period Jan 1 to date of death; sucesiones compute from day after apertura to acceptance (with multi-year splits); herederos add proportional succession rents after acceptance; fideicomisos computed like natural persons (constitution to period end; final period to extinction); non-domiciled conjuntos use the cash method as a single subject | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Arts. 18-23 pp.12-13 (EVID-091) |
| LB-011 | Ley ISR, Art. 24 | Juridical persons use the accrual system: rents accrued though uncollected; costs/expenses incurred though unpaid (subject to deductibility rules) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 24 p.14 (EVID-091) |
| LB-012 | Reglamento ISR, Arts. 9-10 | Renta obtained = all income received or accrued, gross, money or kind, even if later excluded/non-taxable (income is renta obtenida first); cash method = income when received/available (reinvested, accumulated, capitalized, credited, reserved = received), expenses when paid; accrual = accrued/incurred regardless of collection | `sv/sources/04_Reglamento_ISR.pdf` | Arts. 9-10 pp.4-5 (EVID-130) |
| LB-013 | Reglamento ISR, Art. 20 | Natural persons owning branches/agencies consolidate matriz + sucursales income wherever located; domestic juridical persons likewise consolidate their Salvadoran branches/agencies | `sv/sources/04_Reglamento_ISR.pdf` | Art. 20 p.8 (EVID-131) |
| LB-014 | Código Tributario, Art. 62 | Tax base is the economic quantification of the taxable event in legal-tender currency; a foreign-currency base converts at the exchange rate of the day the taxable event occurred; the exchange difference between that date and payment never forms part of the base, but exchange-rate differences on foreign-currency installment sales between contract date and payment of the balance/installments are added to the base | `sv/sources/05_Codigo_Tributario.pdf` | Art. 62 p.21 (txt lines 840-844; T1 LB row, master index) |
| LB-015 | Ley ISR, Art. 16 | SV-source rents: goods situated in-country; activities performed or capital invested in-country; services provided or used in national territory even if paid/received abroad (services used in-country are SV-source to the provider regardless of where performed); industrial/intellectual property registered or used in SV; securities/derivatives results when the emitter is national/domiciled (a) or the capital is invested/placed in-country (b) — literal c) and incisos 5º/7º DEROGATED by D.L. 969-2024; government/municipal remunerations paid abroad to Salvadoran officials | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 16 pp.11-12 (EVID-092; R18 dead-track note) |
| LB-016 | Ley ISR, Art. 127 | Partial-territory method (absent treaties): per activity, ratio = SV gross income ÷ total gross income of that activity; ratio × verified expenses = deductible expenses; SV gross − deductible = SV net income from partially-in-country activities, added to fully-domestic net income | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 127 p.56 (EVID-092) |
| LB-017 | Ley ISR, Art. 27 | Domestic deposits: natural persons' interest/prizes/utilities from deposits in SSF-supervised institutions, savings-credit cooperatives and federations domiciled in-country bear ISR at 10% liquidated separately; with CT Art. 159 retentions the retention is definitive payment (no declaration); incisos 2º-4º (foreign deposits) DEROGATED by D.L. 969-2024 | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 27 pp.14-15 (EVID-094; EVID-168) |
| LB-018 | Ley ISR, Art. 14-A | Domestic securities: utilities, dividends, prizes, interest, net capital gains of domiciled natural persons from títulos valores and financial instruments bear 10% liquidated separately (payment with the annual declaration + DGII calculation form; retained rents need not be declared — definitive); incisos 6º-8º (foreign securities) DEROGATED by D.L. 969-2024 | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 14-A pp.10-11 (EVID-094; EVID-168) |
| LB-019 | D.L. 969-2024 (reforma Ley ISR), Arts. 1-3 | Full derogation scope: Art. 14-A incisos 6º/7º/8º (foreign-securities rents); Art. 16 4º c), 5º and 7º in part (foreign-securities rendimientos; foreign exempt rents from credits abroad — the anti-exemption gross-up); Art. 27 2º/3º/4º (deposits in foreign financial institutions); effective 8 days after D.O. publication of 14-III-2024 → 2024-03-22 | `sv/sources/56_Reforma_Ley_ISR_DL969_DO_2024-03-14.pdf` | Arts. 1-3 pp.1-3 (EVID-168; R18) |
| LB-020 | Ley ISR, Art. 28 inciso final | Mixed costs must be apportioned by the factor gravadas ÷ (gravadas + no gravadas + no renta), deducting only the gravadas proportion (allocator itself specified in `02_isr-deductions.md`; cited here as the mechanism the Art. 3.4 carve-out excludes subjects from) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 28 p.15 (EVID-097) |
| LB-021 | Ley ISR, Art. 48 | Annual liquidation by sworn declaration on DGII form, filed within the four months following the end of the ejercicio or period | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 48 p.41 (EVID-107) |
| LB-022 | Ley ISR, Art. 49 | Non-domiciliated conjuntos: the local contractor and the ensemble's representative are solidarily obliged to formulate and present the ensemble's liquidation on the first business day (*día hábil siguiente*) after each event | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 49 p.41 (EVID-107) |
| LB-023 | Ley ISR, Art. 51 | Payment of the self-assessed tax within the same four-month window via mandamiento de ingreso (DGII form), at tesorería colecturías or authorized places | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 51 p.41 (EVID-107) |
| LB-024 | Ley ISR, Art. 53 | Non-domiciled subjects with withheld amounts: presumed taxes paid, no declaration due; non-domiciled obtaining SV rents without retention (agent failure, dispensing norm, or no obligation) must present the declaration within the legal term liquidating those rents and tax | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 53 pp.41-42 (EVID-104) |
| LB-025 | Ley ISR, Art. 92 | Filing-duty catalog: every ISR subject (registered or not) files per ejercicio; also obliged even with no tax due: natural persons with taxable income above the Art. 37 exempt base; personas jurídicas; formal-accounting subjects; anyone partially/totally withheld upon; prior-year declarants; sucesiones; fideicomisos; foreign conjuntos; "impuesto de timbres" subjects (obsolete tax — see OQ-002); and ALL subjects registered as IVA taxpayers; Art. 38 salaried persons excepted | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 92 p.52 (EVID-107) |
| LB-026 | Ley ISR, Arts. 38 and 29 num. 7 | Salaried natural persons with retentions are not obliged to declare, EXCEPT rents above US$60,000.00 annual, or no retention effected, or retentions not consonant with the Art. 37 table (then declare or request refund); tax = sum of retentions per CT Art. 155 tables; salaried ≤ US$9,100.00 not obliged to liquidate and entitled to the US$1,600.00 fixed deduction (embedded in the retention quota; mechanics in `04_isr-withholding.md`) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 38 pp.38-39; Art. 29.7 p.20 (EVID-096) |
| LB-027 | Ley ISR, Art. 62 | Retention agents remit withheld sums within the ten business days (*diez días hábiles*) immediately following the end of the period in which the retention was effected; December-cost retention values are remitted within the legal term in the December declaration of the year the cost/expense was incurred (corroborated by 75_ Art. 100 — OQ-001 resolved; Art. 100 adds the monthly consolidation of sub-monthly pay cycles — LB-036, EVID-351) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 62 p.43 (EVID-104) |
| LB-028 | D.E. 10-2025 (tablas de retención), Art. 1 i) and Art. 2 | Withheld subjects whose retentions do not match the Art. 37 liquidation declare/pay or request refund; in any case subjects with rents > US$60,000.00 MUST file the ISR declaration; domiciled natural persons subject to retention present their declarations ONLINE via the Ministerio de Hacienda website aplicativos | `sv/sources/53_Tablas_Retencion_ISR_DE10_2025.pdf` | Art. 1 i), Art. 2 pp.7-8 (EVID-161) |
| LB-029 | Ley ISR, Art. 105-A | Stale sanction: 50% fine on unentered anticipos/pagos a cuenta, minimum "mil colones" (colon-era), citing the repealed "inciso 6º del Art. 72"; self-liquidated in the declaration; no appeal but 30-day pago indebido claim — superseded in practice by the CT sanctions regime (CT Arts. 226-247 zone; see OQ-003) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | Art. 105-A pp.54-55 (EVID-107; EV05:EVID-065) |
| LB-030 | Ley ISR, derogation map + final provisions (Arts. 7-11, 15, 26, 43-125 passim, 128-129) | Procedure routing: ~70 articles repealed (domicile, determination-officio, staged payment, retention machinery Arts. 58-59/61/63/66-71, administration/fiscalización/sanctions/procedures) — procedures live in the Código Tributario; substance survives in the Ley. Legal-basis note only, not FRs (EVID-108) | `sv/sources/54_Ley_ISR_consolidada_DO79_T447_2025-04-30.pdf` | repealed articles passim pp.8-56 (EVID-108) |
| LB-031 | Reglamento ISR, REFORMAS block (p.20): D.E. 8-1993, D.E. 39-1993, D.E. 117-2001 | Reglamento procedure routing: D.E. 117-2001 is the mass-repeal instrument (declaración/pago, retention machinery, devoluciones, prescripción, cobro coactivo, information duties, books — Art. 84 survives — sanctions, administration, procedures); cite survivors only. Repeal authority is D.E. 117-2001, NOT the CT (R17). Legal-basis note only, not FRs | `sv/sources/04_Reglamento_ISR.pdf` | REFORMAS p.20 (EVID-128; R17) |
| LB-032 | Ley Especial Quincena Veinticinco (D.L. 499, D.O. N° 8 T.450 14-ene-2026; effective on publication; **acquired 2026-08-18 as `66_`** — official DGII copy, OCR), Art. 4: "se declara como rentas no gravables, y en consecuencia excluidos del cómputo de la renta obtenida, el monto que reciban los trabajadores en concepto de Quincena Veinticinco. Asimismo, estos ingresos... no estarán afectos a la Retención del Impuesto sobre la Renta, y gozarán del beneficio de la inembargablilidad [sic]. Para efectos tributarios, los montos pagados en concepto de Quincena Veinticinco constituliran [sic] gasto deducible para el patrono, siempre que hayan sido efectivamente pagados y debidamente documentados, conforme a lo dispuesto en la Ley de Impuesto sobre la Renta." | Quincena-25 fiscal treatment: amounts received by workers as Quincena Veinticinco are declared rentas no gravables and excluded from the computation of renta obtenida; not subject to ISR Retention; unseizable (inembargabilidad); employer side — amounts paid constitute gasto deducible for the patrono provided effectively paid and duly documented per the Ley ISR (deduction FR owned by `02_isr-deductions.md` SV-TAX-FR-175) | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 4 p.4 (EVID-237) |
| LB-033 | Ley Especial Quincena Veinticinco (D.L. 499), Art. 6 (transitory): private-sector 2026 payment "tendrá carácter voluntario para los patronos, debiendo realizarse en su caso, a mas tardar el veinticinco de enero de dos mil veintiséis"; paying employers "tendrán derecho a un crédito tributario acreditable contra el pago del Impuesto sobre la Renta del ejercicio fiscal dos mil veintiséis, por el monto total pagado"; tercerización contractors paying the full amount get the same credit (tercerizador "debera [sic] emitir al contratante, por separado, el correspondiente documento fiscal en el que conste el monto pagado en concepto de Quincena Veinticinco y, oportunamente, presentar la copia de la planilla"); credit > ISR payable → remanent "podrá utilizarse para atender el cumplimiento de otras obligaciones sustantivas relacionadas con el Impuesto sobre la Renta"; ZF/DPA/LSI users: excess → "Certificado de Crédito Tributario emitido por el Ministerio de Hacienda... el cual se obtendrá al momento de presentar su declaración del Impuesto sobre la Renta para el ejercicio fiscal dos mil veintiséis"; certificado usage "no representa la aplicación de un régimen especial tributario" | FY-2026-only employer tax credit = 100% of amounts actually paid, creditable against the FY-2026 ISR payment (public sector 2026 = mandatory, private = voluntary); remanent applicable to other substantive ISR obligations; ZF/DPA/LSI excess routed to the Certificado de Crédito Tributario auto-generated at FY-2026 declaration presentation (uses: negotiable at any financial-system institution; transferible intra-grupo or to third parties; creditable against ISR of prior/later ejercicios, pagos a cuenta and retenciones; redeemable at MH); tercerización contractors record the same credit with a separate documento fiscal to the contratante + planilla copy | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 6 pp.4-6 (EVID-237) |
| LB-034 | Ley Especial Quincena Veinticinco (D.L. 499), Art. 8 — special-law character of public order: the Quincena-25 rules prevail over any contrary norm (EVID-237 gloss; verbatim text not extracted in evidence) | The Quincena-25 special law is of public order (orden público) and prevails over contrary norms — anchoring the Art. 4 renta-no-gravada declaration's precedence in the ISR computation without amending the Ley ISR exemption list | `sv/sources/66_Ley_Quincena25_DL499.pdf` | Art. 8 pp.4-6 (EVID-237) |
| LB-035 | Guía de Orientación Quincena Veinticinco (MH.UVI.DGII/006.001/2026; **acquired 2026-08-18 as `67_`**), §§3-4 + Anexos 1/7/8: credit documentation = "planilla en original... y la suscripción de la misma por beneficiarios" + the F-14 annex; Anexo 1: "Se genera una nueva versión del Formulario F-11 versión 19" with the credit in "casilla 319 denominada 'Crédito Tributario Quincena Veinticinco'" inside the IMPUESTO DETERMINADO subtraction (casilla-330 formula includes 319), the v19 print still carrying the dead pago-mínimo rows (R21); Anexo 7: ZF/DPA/LSI checkbox "Marque si es usuario de Zona Franca, DPA o Usuario regulado en la Ley de Servicios Internacionales" on the Renta-2026 screen; Anexo 8: "Versión 20 — Declaración de Impuesto sobre la Renta para Sujetos con Régimen Especial... la que tendrá como anexo el Certificado de Crédito Tributario" | Credit documentation = original planilla subscribed (signed) by the beneficiaries + the F-14 annex; declaration surface = F-11 v19 casilla 319 inside the casilla-330 subtraction; ZF/DPA/LSI certificado seekers identified by the renta-en-línea checkbox; F-11 v20 (special-regime subjects, renamed) carries the Certificado as anexo (prints not yet acquired — OQ-007) | `sv/sources/67_Guia_Orientacion_Quincena25.pdf` | §§3-4 + Anexos 1/7/8 pp.2-13 (EVID-237; EVID-238) |
| LB-036 | Reglamento de Aplicación del Código Tributario (D.E. N° 117-2001), Arts. 99-100 | Retention payment period and entero deadline: Art. 99: "Por período de pago para efectos de retenciones del Impuesto sobre la Renta, se entiende el mes calendario en el que el agente de retención paga ordinariamente la remuneración sea ésta total o parcial"; Art. 100: "Las cantidades retenidas deberán ser enteradas al colector respectivo, dentro de los diez días hábiles que inmediatamente sigan al vencimiento del mes calendario en que se efectúa la retención", and for remunerations paid "por día, por período especial, semana o quincena" the agent "deberá consolidar en períodos mensuales, las respectivas retenciones" — corroborating Ley Art. 62's ten-días-hábiles remittance (OQ-001 resolved; no divergence) and adding the monthly consolidation of sub-monthly pay cycles; the by-NIT-digit window question stays fiscal-reporting's SOQ-08 | `sv/sources/75_Reglamento_Codigo_Tributario_DE117.pdf` | Arts. 99-100 p.62 (EVID-351; verified 75_ txt lines 3193-3210) |

Dead text — never implementable as current law (recorded here as LB notes, not
FRs, per wave constraint): pago mínimo Arts. 76-81 (declared unconstitutional,
sentencias 18-2012/98-2014/96-2014 — R21; EV03:EVID-105, EV54:EVID-162);
EVID-094's foreign-securities/deposit paragraphs and EVID-092's
anti-exemption gross-up for foreign rents (dead per D.L. 969-2024 — R18;
LB-019).

## 3. Functional Requirements

### 3.1 Renta obtenida and its categories (T1)

- **SV-TAX-FR-001:** The system shall classify every recognized income item of
  an ISR subject into exactly one of the four *renta obtenida* categories:
  a) *del trabajo* (from work: salaries, wages, fees, commissions and any
  remuneration or compensation for personal services), b) *de la actividad
  empresarial* (from business activity: commercial, agricultural, industrial,
  service or any other nature), c) *del capital* (from capital: rents, interest,
  dividends or participations), or d) the catch-all (any class of products,
  gains, benefits or utilities whatever their origin) — the classification
  being the first step of the Art. 1 taxable-event obligation. (LB-001;
  LB-002; EVID-088)
- **SV-TAX-FR-002:** The system shall recognize as catch-all renta obtained:
  condoned debts (*deudas condonadas*), undocumented liabilities (*pasivos no
  documentados*), excess provisions of liabilities (*provisiones de pasivos en
  exceso*) — the latter two imputed to the respective imposition period — and
  unjustified patrimony increments plus expenditures whose resource origin is
  unjustified per CT Art. 195. (LB-002; EVID-088)
- **SV-TAX-FR-003:** The system shall exclude *gastos de representación*
  (representation allowances) of public officials from category-a remuneration
  income, per the interpretación auténtica D.L. 629-1993 incorporated in
  Art. 2.a. (LB-002; EVID-088)
- **SV-TAX-FR-004:** The system shall treat employer deliveries of
  *viáticos* (travel per-diems for transport, food and lodging) in a reasonable
  amount, work tools, uniforms and office equipment as NOT renta obtained by
  the worker, provided they are necessary for the employer's income production
  or source conservation and are backed by the documents established in CT
  Arts. 107 or 119 (electronic document types per
  `e-invoicing/01_document-types.md`, SV-EINV-FR-001); deliveries with other
  purposes constitute renta obtained subject to retention with the remuneration.
  (LB-003; EVID-088/089)
- **SV-TAX-FR-005:** The system shall treat the value of goods received by
  legacies or inheritances, and donations between ascendants and descendants
  within the second degree of consanguinity and between spouses, as NOT renta
  obtained, recording as acquisition value and date the goods' value to the
  predecessor (*antecesor*) at the date they entered the recipient's patrimony
  (market price if undeterminable, verifiable by DGII). (LB-003; EVID-089)
- **SV-TAX-FR-173:** The system shall classify amounts received by
  workers as Quincena-25 as *rentas no gravadas* excluded from the
  renta computation per D.L. 499 Art. 4 — a special-law declaration
  that prevails over contrary norms per its Art. 8 (public-order),
  operating alongside (not amending) the Ley ISR Art. 4 exemption
  list; consequently the amounts never enter the retention base (the
  SV-TAX-FR-104 exclusion input is fed by SV-PAY-FR-137), never appear
  in the annual liquidation renta, and surface only as no-gravado
  reporting (F-910 code 73 / renta-en-línea 724-kin — SV-FREP-FR-212).
  (LB-032; LB-034; EVID-237; cross-ref SV-PAY-FR-137, SV-FREP-FR-212,
  SV-TAX-FR-104)

### 3.2 Subjects and exclusions (T1)

- **SV-TAX-FR-006:** The system shall support ISR-subject registration for all
  Art. 5 subject types: natural and juridical persons (domiciled or not),
  *sucesiones* (estates), *fideicomisos* (trusts), artists/sportsmen and
  similar individually or as *conjuntos* (any non-domiciled group of natural
  persons entering the country temporarily, whatever its organization, treated
  as ONE subject), and *sociedades irregulares o de hecho* and *uniones de
  personas* (de-facto/irregular societies and unions of persons). (LB-005;
  LB-007; EVID-090/129)
- **SV-TAX-FR-007:** The system shall flag as excluded ISR subjects (no
  substantive obligation) the Estado, municipalidades, and public-law or
  *utilidad pública* corporations/foundations, the latter only where
  non-profit, with income and patrimony exclusively destined to the
  institution's purposes and never distributed directly or indirectly to
  members; the exclusion shall never lift formal duties. (LB-006; LB-007;
  EVID-090/129)
- **SV-TAX-FR-008:** The system shall model the *utilidad pública* exclusion
  as a DGII qualification held for 12-month periods that coincide with the
  fiscal year and are automatically renewed unless DGII officially communicates
  revocation (qualification dossier: D.O.-published statutes, member roster,
  board-election certificate; DGII verification right). (LB-006; LB-007;
  EVID-129)

### 3.3 Fiscal year, methods and period splits (T1)

- **SV-TAX-FR-009:** The system shall compute ISR per *ejercicio de
  imposición* (imposition period) of twelve months running 1-January through
  31-December for natural and juridical persons, aggregating the products or
  utilities of ALL income sources of the subject, with income presumed
  obtained at midnight of the last day of the period. (LB-008; EVID-091)
- **SV-TAX-FR-010:** The system shall trigger a short-period liquidation when
  the subject ceases to exist or definitively leaves the country ending its
  economic activity before the ejercicio closes, computing the rent of that
  partial period. (LB-008; EVID-091)
- **SV-TAX-FR-011:** The system shall liquidate each ejercicio or period
  independently of the preceding and following one (gains/losses of one period
  not affecting others), except where a legal exception applies (capital-loss
  carryforward and securities-loss netting — `03_isr-rates-gains.md` §3
  losses; no general NOL exists). (LB-008; EVID-091/106)
- **SV-TAX-FR-012:** The system shall compute natural persons' ISR on the
  cash method by default: income when actually received in cash, securities or
  kind, including constructive receipt (amounts available, or reinvested,
  accumulated, capitalized, credited to account or placed in reserve =
  received); expenses when actually paid. (LB-009; LB-012; EVID-091/130)
- **SV-TAX-FR-013:** The system shall enforce the accrual-method rules for
  natural persons: accounting-obligated natural persons MUST compute on
  accrual; non-obligated natural persons may elect accrual by recording
  operations in auxiliary accounting records and informing DGII in
  November-December of the ejercicio prior to adoption; once adopted, the
  accrual election shall be blocked from being changed (irrevocable).
  (LB-009; EVID-091)
- **SV-TAX-FR-014:** The system shall compute juridical persons' ISR on the
  accrual system: rents accrued in the ejercicio though not collected, and
  costs/expenses incurred though unpaid (always subject to the deductibility
  rules of `02_isr-deductions.md`). (LB-011; EVID-091)
- **SV-TAX-FR-015:** The system shall attribute the *usufructo legal* (legal
  usufruct) income of an unemancipated minor to the parents in equal parts or
  as common law indicates; a minor under testamentary or judicial
  tutela/curatela computes individually; a verified renunciation by the
  usufructuary disables parental attribution. (LB-010; EVID-091)
- **SV-TAX-FR-016:** The system shall split periods on death and succession:
  the deceased's final period runs from 1-January to the date of death; the
  *sucesión* computes from the day after its apertura (opening) until
  acceptance of the inheritance, respecting ejercicio boundaries (periods
  closing without acceptance computed to year-end; full ejercicios for each
  year un-accepted; final stub to the acceptance date); once accepted,
  herederos and legatarios add their proportional share of succession rents
  from the day after acceptance to their own rents. (LB-010; EVID-091)
- **SV-TAX-FR-017:** The system shall compute *fideicomiso* (trust) rent as
  for natural persons (cash-method rules), splitting periods from constitution
  to the close of the ordinary ejercicio and, on extinction, computing the
  final period from the ejercicio's start to the extinction date. (LB-010;
  EVID-091)
- **SV-TAX-FR-018:** The system shall compute non-domiciled *conjuntos* as a
  single subject on the cash method, summing the total rents obtained by all
  members per event. (LB-010; EVID-091)
- **SV-TAX-FR-019:** The system shall consolidate for ISR determination the
  income of natural persons owning branches/agencies (matriz + sucursales,
  wherever located) and of domestic juridical persons for their Salvadoran
  branches/agencies. (LB-013; EVID-131)
- **SV-TAX-FR-020:** The system shall convert foreign-currency tax bases to
  the legal-tender currency (USD) at the exchange rate of the day the taxable
  event (*hecho generador*) occurred; exchange differences arising between
  that date and the payment of the tax shall never enter the tax base;
  exchange-rate differences on foreign-currency installment sales arising
  between contract date and payment of the balance or installments SHALL be
  added to the tax base. (LB-014; T1 LB row, master index)

### 3.4 Territoriality and foreign-source exclusion (T2)

- **SV-TAX-FR-021:** The system shall classify income as Salvadoran-source
  when it derives from: goods situated in the country; activities performed or
  capitals invested in it; services provided OR used in national territory even
  if received or paid abroad (services used in-country are SV-source to the
  provider regardless of where the underlying activity is performed);
  industrial or intellectual property and analogous economic rights registered
  officially in SV or used in it; and results/utilities/interests from
  securities, financial instruments and derivatives when the issuing entity is
  national or domiciled in SV (literal a) or the capital is invested/placed in
  the country (literal b) — literal c) and incisos 5º/7º are dead text per
  D.L. 969-2024); and remunerations of the Government, municipalidades and
  official entities paid to their Salvadoran officials abroad. (LB-015;
  EVID-092/168; R18)
- **SV-TAX-FR-022:** The system shall exclude from the ISR renta concept ALL
  values obtained abroad in any concept — including any movement of capital,
  remuneration or emolument, in money or kind, generated or not by investment
  of national or foreign capital, nominally obtained by natural persons,
  juridical persons or entities without legal personality, domiciled or not —
  per Art. 3.4, effective 2024-03-22. Version note (D12): for periods before
  the 2024-03-22 cutover, the pre-969 foreign tracks (EVID-094 foreign
  paragraphs; EVID-092 anti-exemption gross-up) remain historical data and
  shall not be applied to current periods. (LB-004; LB-019; EVID-164/168; R18)
- **SV-TAX-FR-023:** The system shall mark subjects that obtain gravadas
  rents AND any Art. 3.4 foreign-excluded concept as OUTSIDE the Art. 28-final
  pro-rata mechanism for cost/expense apportionment (the carve-out added by
  D.L. 969-2024); the allocator itself is specified in
  `02_isr-deductions.md` §3. (LB-004; LB-020; EVID-164)
- **SV-TAX-FR-024:** The system shall provide an Art. 127
  partial-territory apportionment worksheet for activities performed partly in
  El Salvador (absent applicable treaties): per activity, ratio = SV gross
  income ÷ total gross income of that activity; deductible expenses = ratio ×
  total verified expenses of the activity; SV net income = SV gross income −
  deductible expenses, added to fully-domestic net income. (LB-016; EVID-092)
- **SV-TAX-FR-025:** The system shall route DOMESTIC deposit income (Art. 27:
  deposits in SSF-supervised institutions and in savings-credit cooperatives
  and their federations domiciled in-country) and domestic securities income
  (Art. 14-A) of domiciled natural persons to the surviving 10%
  separate-liquidation track (definitive when retained — no declaration), and
  shall NOT route foreign deposits/securities to that track (dead per D.L.
  969-2024); computation detail lives in `03_isr-rates-gains.md` §3.
  (LB-017; LB-018; LB-019; EVID-094/168; R18)

### 3.5 Filing and payment framework (T8)

- **SV-TAX-FR-026:** The system shall present the annual ISR liquidation duty
  with a filing window ending four months after the close of the ejercicio or
  imposition period (declaration on DGII form). (LB-021; EVID-107)
- **SV-TAX-FR-027:** The system shall present the payment duty for
  self-assessed tax with the same four-month deadline after period close,
  via *mandamiento de ingreso* (payment order on DGII form). (LB-023;
  EVID-107)
- **SV-TAX-FR-028:** The system shall evaluate the Art. 92 filing-duty
  catalog per ejercicio and flag must-file status even when no tax is due,
  for: natural persons with renta imponible above the Art. 37 exempt base;
  personas jurídicas; subjects obliged to keep formal accounting; anyone
  partially or totally withheld upon; prior-year declarants; sucesiones;
  fideicomisos; non-domiciled conjuntos; and ALL subjects registered as IVA
  taxpayers (VAT registration drives an ISR filing duty); the "impuesto de
  timbres" numeral (obsolete tax) shall be disabled (OQ-002). (LB-025;
  EVID-107)
- **SV-TAX-FR-029:** The system shall apply the salaried exception: domiciled
  natural persons whose rents come exclusively from salaries and similar
  remunerations and who were subject to retention are NOT obliged to file,
  except (a) annual rents above US$60,000.00, (b) no retention effected, or
  (c) retentions not consonant with the Art. 37 table (then must declare or
  may request refund); salaried persons at or below US$9,100.00 are not
  obliged to liquidate (fixed-deduction mechanics in
  `04_isr-withholding.md` §3). (LB-026; LB-028; EVID-096/161)
- **SV-TAX-FR-030:** The system shall present, for each event of a
  non-domiciled conjunto, an event liquidation duty due on the first business
  day (*día hábil siguiente*) after the event, with the local contractor and
  the ensemble's representative flagged as solidarily responsible for filing.
  (LB-022; EVID-107)
- **SV-TAX-FR-031:** The system shall assume online-only ISR filing for
  domiciled natural persons subject to retention (declarations presented
  online via the Ministerio de Hacienda website aplicativos — informational;
  no paper filing path shall be assumed or offered by the system).
  (LB-028; EVID-161)
- **SV-TAX-FR-032:** The system shall schedule retention remittances (when
  acting as retention agent) for remission of withheld ISR within the ten
  business days (*diez días hábiles*) immediately following the end of the
  retention period, and shall schedule December-cost retention values in the
  December declaration of the year the cost or expense was incurred. Anchor
  corroborated by 75_ Reglamento CT Arts. 99-100 (LB-036; EVID-351 — OQ-001
  resolved): retention period = the ordinary-payment *mes calendario*, entero
  within the ten días hábiles after month end, sub-monthly pay cycles
  (día/período especial/semana/quincena) consolidated monthly; no mechanic
  change. (LB-027; LB-036; EVID-104/351)
- **SV-TAX-FR-033:** The system shall treat withheld amounts of
  non-domiciled subjects as taxes paid (presumed payment, no declaration duty
  generated), and shall flag a self-declaration duty for non-domiciled
  subjects who obtained Salvadoran rents without any retention having been
  effected (agent failure, dispensing norm, or no retention obligation), to be
  liquidated within the legal term. (LB-024; EVID-104)
- **SV-TAX-FR-174:** The system shall maintain, for FY-2026 only, the
  employer Quincena-25 tax CREDIT ledger: employers who paid the
  (voluntary private / mandatory public) Quincena-25 record a credit
  of 100% of amounts actually paid, creditable against the FY-2026 ISR
  payment; a remanent after crediting is applicable to OTHER
  substantive ISR obligations; tercerización contractors that paid the
  full amount record the same credit (with the separate documento
  fiscal to the contratante + planilla copy — 66_ Art. 6); ZF/DPA/LSI
  users route the excess to the transferable Certificado de Crédito
  Tributario issued by MH (auto-generated at the FY-2026 declaration
  presentation; "no representa la aplicación de un régimen especial
  tributario" — special-regimes wave consumes this by id); the credit's
  declaration surface is F-11 v19 casilla 319 'Crédito Tributario
  Quincena Veinticinco' inside the casilla-330 IMPUESTO DETERMINADO
  subtraction (v19/v20 prints = acquisition candidates ≥71; layout
  builder future); documentation = original signed planilla + the
  F-14 annex (67_ §4); the renta-en-línea ZF/DPA/LSI checkbox routes
  certificado seekers (67_ Anexo 7). Dated regime: valid for ejercicio
  2026 payments only (no continuation in 2027+ — the credit is Art. 6
  transitory). (LB-033; LB-035; EVID-237/238)

## 4. Data Model

Machine-readable sidecars (e.g. filing-duty reason codes) live next to this
markdown file when produced. Layer semantics: this file introduces Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**ISR subject profile (per company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | isr_subject_type | select | natural_person · legal_person · succession · trust · conjunto · irregular_society · persons_union | FR-006 |
| res.company | isr_domiciled | boolean | drives 54_ Art. 37/41 rate selection (03 file) | FR-006 |
| res.company | isr_computation_method | select | cash · accrual | FR-012, FR-014 |
| res.company | isr_accrual_elected_on | date null | set once; election irrevocable — UI blocks change | FR-013 |
| res.company | isr_accrual_informing_period | char | Nov-Dec ejercicio prior to adoption (DGII informing) | FR-013 |
| res.company | isr_excluded_art6 | boolean | Estado/municipalidad/public-law/utilidad pública | FR-007 |
| res.company | isr_utilidad_publica_qualified_on | date null | DGII qualification start | FR-008 |
| res.company | isr_qualification_revoked_on | date null | DGII official revocation ends auto-renewal | FR-008 |
| res.company | isr_cessation_date | date null | triggers short-period liquidation | FR-010 |
| res.company | isr_foreign_excluded_concepts | boolean (computed) | true → subject outside Art. 28-final pro-rata | FR-023 |
| res.company | isr_consolidates_branches | boolean default true | matriz + sucursales consolidation scope | FR-019 |

**Income classification (on journal items):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line | isr_income_category | select | trabajo · empresarial · capital · catch_all | FR-001 |
| account.move.line | isr_catch_all_rule | select | condoned_debt · undocumented_liability · excess_provision · unjustified_patrimony_ct195 · other_benefit | FR-002 |
| account.move.line | isr_representation_allowance | boolean | true → excluded from trabajo remuneration (D.L. 629) | FR-003 |
| account.move.line | isr_no_renta_rule | select null | work_tools_viaticos · legacy_inheritance · family_donation · quincena_25_art4_66_ (renta NO GRAVADA by special law — excluded from the cómputo; reporting-only code-73/724 surface) | FR-004, FR-005, FR-173 |
| account.move.line | isr_territorial_status | select | domestic · foreign_excluded · partial_apportioned | FR-021, FR-022, FR-024 |
| account.move.line | isr_sv_source_rule | select | goods_situated · activity_performed · capital_invested · service_provided_or_used · ip_registered_or_used · securities_emitter_domiciled · securities_capital_in_country · govt_remuneration_abroad | FR-021 |

**Period-split bookkeeping (estates/trusts/conjuntos):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner / res.company (sucesión) | isr_apertura_date / isr_acceptance_date | date null | drives sucesión period splits and heredero attribution start | FR-016 |
| res.company (fideicomiso) | isr_constitution_date / isr_extinction_date | date null | trust period splits (cash-method rules) | FR-017 |
| res.company (conjunto) | isr_event_dates | date list | one liquidation duty per event (día hábil siguiente) | FR-018, FR-030 |

**Territoriality worksheet and FX:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.territorial.apportionment (new) | activity, fiscal_year, sv_gross_income, total_gross_income, ratio, verified_expenses, deductible_expenses, sv_net_income | monetary/computed | ratio = SV gross ÷ total gross; deductible = ratio × verified expenses; net = SV gross − deductible | FR-024 |
| account.move | isr_fx_anchor | date (defaults to invoice date) | hecho-generador day rate for foreign-currency base; payment-date FX deltas excluded from base; installment FX deltas added | FR-020 |

**Filing framework:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.filing.duty (new) | company, fiscal_year, must_file, duty_reasons, salaried_exception | boolean · m2m catalog | duty_reasons: above_exempt_base · legal_person · formal_accounting · withheld · prior_declarant · succession · trust · foreign_conjunto · iva_registered · over_60k · retention_mismatch · non_domiciled_unretained | FR-028, FR-029, FR-033 |
| l10n_sv.isr.filing.duty | declaration_due_date / payment_due_date | date | period end + 4 months | FR-026, FR-027 |
| l10n_sv.isr.remittance.period (new; mechanics in 04 file) | period, due_date, december_rule | date · boolean | 10 días hábiles after period end; December costs in December declaration | FR-032 |

**FY-2026 Quincena-25 employer credit ledger (dated regime — 66_ Art. 6
transitory; no 2027+ continuation):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.isr.quincena.credit (new) | ejercicio | year | 2026 only — dated regime; no rows for 2027+ | FR-174 |
| l10n_sv.isr.quincena.credit | amount_paid | monetary | amounts actually paid (voluntary private / mandatory public) | FR-174 |
| l10n_sv.isr.quincena.credit | credit_amount | monetary (computed) | = 100% × amount_paid ("por el monto total pagado") | FR-174 |
| l10n_sv.isr.quincena.credit | applied_against · remanent | monetary (computed) | crediting against the FY-2026 ISR payment; remanent → other substantive ISR obligations | FR-174 |
| l10n_sv.isr.quincena.credit | route | select | isr_payment · other_isr_obligations · certificado_zf_dpa_lsi | FR-174 |
| l10n_sv.isr.quincena.credit | certificado_ref | char null | MH Certificado de Crédito Tributario reference (issuance = MH external, at FY-2026 declaration presentation) | FR-174 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living in
the LGPL client. No SaaS rows are introduced in this file: none of these FRs
touch DTE generation/transformation (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are stable
across Odoo 17/18/19/20; no version-specific behavior is required by this
file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | account.move.line | isr_income_category | Category defaulting by account/product; user-overridable at line |
| FR-002 | odoo | account.move.line | isr_catch_all_rule | Feeds misc-income journals (debt condonation, provision excess); CT 195 increments entered via adjustment entries |
| FR-003 | odoo | account.move.line | isr_representation_allowance | Exclusion applied on payroll/feed lines of public officials |
| FR-004 | odoo | hr.expense / account.move.line | isr_no_renta_rule | Viáticos reasonableness is a payroll-side check (`04_isr-withholding.md`); document backing cross-checks DTE types (SV-EINV-FR-001) |
| FR-005 | odoo | account.move.line | isr_no_renta_rule | Basis carryover recorded on the asset/income line (donation/inheritance) |
| FR-006 | odoo | res.company | isr_subject_type, isr_domiciled | Partner/company fiscal category; drives method, splits, rate file (03) |
| FR-007 | odoo | res.company | isr_excluded_art6 | Formal duties remain active even when excluded (tax grid obligations) |
| FR-008 | odoo | res.company | qualification dates | Auto-renewal per fiscal year computed; revocation date cuts qualification |
| FR-009 | odoo | account.fiscal.year / date.range | — | Jan-Dec fixed for ISR; aggregation over all income accounts |
| FR-010 | odoo | res.company | isr_cessation_date | Short-period liquidation run trigger |
| FR-011 | odoo | account.move | fiscal period binding | Period independence enforced by per-period computation; exceptions only via loss ledgers (03 file) |
| FR-012 | odoo | res.company | isr_computation_method | Cash-method recognition engine incl. constructive-receipt flags |
| FR-013 | odoo | res.company | isr_accrual_elected_on | UI blocks method change once set; Nov-Dec informing recorded |
| FR-014 | odoo | account.move | accrual defaults | Native Odoo accrual; unpaid costs gated by deductibility (02 file) |
| FR-015 | odoo | res.partner (dependents) | usufruct attribution | Awareness-level: attribution split on guardian partners |
| FR-016 | odoo | res.partner/res.company | apertura/acceptance dates | Estate period-split computation on death event |
| FR-017 | odoo | res.company | constitution/extinction dates | Trust period splits; cash-method rules |
| FR-018 | odoo | res.company | conjunto flag | Single-subject aggregation per event |
| FR-019 | odoo | res.company | isr_consolidates_branches | Branches as analytic/operating units consolidated in determination |
| FR-020 | odoo | account.move | currency_id, isr_fx_anchor | Native multi-currency converts at invoice date; rule keeps FX payment deltas out of tax base (fiscal layer adjustment) |
| FR-021 | odoo | account.move.line | isr_sv_source_rule | Source-rule classifier defaults by partner/product/currency |
| FR-022 | odoo | account.move.line | isr_territorial_status | Version regime: cutover 2024-03-22 (D.L. 969-2024); periods before keep dated foreign tracks as historical data |
| FR-023 | odoo | res.company | isr_foreign_excluded_concepts | Computed flag consumed by the 02 file's pro-rata allocator |
| FR-024 | odoo | l10n_sv.isr.territorial.apportionment | all | Art. 127 worksheet model; ratio + deductible + net computed |
| FR-025 | odoo | account.move.line | isr_territorial_status | Domestic 10% routing tag; computation in 03 file |
| FR-026 | odoo | l10n_sv.isr.filing.duty | declaration_due_date | Calendar/duty surface; e-filing itself out of scope (online-only, FR-031) |
| FR-027 | odoo | l10n_sv.isr.filing.duty | payment_due_date | Payment order (mandamiento de ingreso) generated as report |
| FR-028 | odoo | l10n_sv.isr.filing.duty | must_file, duty_reasons | IVA registration read from company tax IDs (l10n_latam) — cross-topic: SV-EINV registration feeds this duty |
| FR-029 | odoo | l10n_sv.isr.filing.duty | salaried_exception | $60,000/$9,100 thresholds as parameters; retention-mismatch check consumes 04 file data |
| FR-030 | odoo | l10n_sv.isr.filing.duty / event model | event dates | Día hábil siguiente deadline; solidarity flag on contractor + representative |
| FR-031 | odoo | — (informational) | — | Informational notice only: system assumes MH online aplicativos; no paper path modeled |
| FR-032 | odoo | l10n_sv.isr.remittance.period | due_date, december_rule | 10 días hábiles computation (business-day calendar); OQ-001 resolved — 75_ Arts. 99-100 corroborate (mes-calendario period + monthly consolidation), no re-anchor |
| FR-033 | odoo | l10n_sv.isr.filing.duty | duty_reasons | Presumed-paid vs unretained self-declaration flags on non-domiciled partners |
| FR-173 | odoo | account.move.line | isr_no_renta_rule (+ quincena_25_art4_66_) | Special-law no-gravada stamp fed by SV-PAY-FR-137 (payroll matrix): never in the SV-TAX-FR-104 retention base nor the annual liquidation renta; only surface = no-gravado reporting (F-910 code 73 / 724-kin, SV-FREP-FR-212) |
| FR-174 | odoo | l10n_sv.isr.quincena.credit | all | FY-2026-only dated regime (Art. 6 transitory); F-11 v19 casilla-319 feed key inside the casilla-330 subtraction; v19's dead pago-mínimo rows never fed (R21 extends — AC-020); ZF/DPA/LSI certificado entitlement recorded, issuance external to MH; special-regimes wave consumes the certificado by id |

Version-regime notes (D12): FR-022/FR-025 record the D.L. 969-2024 cutover
(2024-03-22) — any computation on pre-cutover periods must select the dated
foreign-track data instead. FR-029 thresholds ($60,000 / $9,100) are stable
in current text; the D.E. 10-2025 vintage date (2025-05-08 CONFIRMED:
published D.O. N° 79 T.447 30-abr-2025, gazette print 60_, EVID-171 —
SOQ-03 resolved) affects the tables decree, tracked in
`04_isr-withholding.md`. FR-174 records the FY-2026-only Quincena-25
credit (66_ Art. 6 transitory, D.O. 14-ene-2026): no continuation in
2027+ — the ledger accepts ejercicio 2026 rows only.

## 6. Acceptance Criteria

- **AC-001:** Given a journal line recognized as a director's salary and
  another as warehouse-lease rent, when classified, then the first line is
  isr_income_category = trabajo and the second = capital (FR-001).
- **AC-002:** Given a condoned supplier debt of $1,000 booked in March and an
  excess liability provision of $500 booked in July, when the ejercicio is
  computed, then both are recognized as catch-all renta obtained imputed to
  their respective periods (March / July) (FR-002).
- **AC-003:** Given an employer delivery of work tools to an employee, backed
  by a CCF-type DTE and flagged necessary for production, then the delivery is
  not renta obtained; given a cash delivery outside the Art. 3.1 concepts,
  then it is renta subject to retention with the remuneration (FR-004).
- **AC-004:** Given goods received by inheritance from a parent, then no renta
  is recognized and the acquisition value/date recorded equals the goods' value
  to the predecessor at patrimony-entry date (FR-005).
- **AC-005:** Given a taxpayer dying on 15-May with rents Jan 1-May 15, then
  the final period liquidates Jan 1-May 15; given the sucesión opened 16-May
  of year 1 and accepted 20-September of year 3, then the estate computes
  16-May→31-Dec of year 1, a full ejercicio for year 2, and 1-Jan→20-Sep of
  year 3 (the acceptance year) (FR-016).
- **AC-006:** Given a non-accounting natural person who elected accrual
  informing DGII in Nov-Dec 2024, then the system computes 2025 on accrual and
  any subsequent attempt to switch the method back to cash is blocked
  (FR-013).
- **AC-007:** Given an accounting-obligated natural person, then the
  computation method is forced to accrual with no cash option (FR-013).
- **AC-008:** Given a $10,000 foreign-currency receivable with hecho
  generador on 10-March (rate applied at that date) settled on 30-April at a
  different rate, then the tax base keeps the 10-March conversion and the
  payment-date FX difference never enters the base (FR-020).
- **AC-009:** Given a domiciled company receiving $5,000 of foreign-source
  dividends in 2025, then the amount is excluded from renta obtenida; given
  the same facts in a 2023 exercise, then the pre-cutover foreign-track data
  applies instead (FR-022).
- **AC-010:** Given a subject with both $100,000 gravadas rents and $20,000
  Art. 3.4-excluded concepts, then isr_foreign_excluded_concepts = true and
  the subject is excluded from the Art. 28-final pro-rata mechanism (FR-023).
- **AC-011:** Given an activity with SV gross $30,000, total gross $120,000
  and verified expenses $40,000, then ratio = 0.25, deductible = $10,000 and
  SV net from the partial activity = $20,000, added to fully-domestic net
  (FR-024).
- **AC-012:** Given a taxpayer whose only tie to ISR is active IVA
  registration and zero ISR tax due, then must_file = true with duty_reasons
  containing iva_registered (FR-028).
- **AC-013:** Given a salaried person with $50,000 rents fully retained per
  the tables, then no filing duty; given a salaried person with $65,000 rents,
  then must_file = true (over_60k) (FR-029).
- **AC-014:** Given a non-domiciled conjunto event performed on Friday
  12-June, then the event liquidation due date is the next business day
  (Monday 15-June if unimpeded) with contractor and representative flagged
  solidary (FR-030).
- **AC-015:** Given retentions effected in June, then the remittance due date
  is the tenth business day after 30-June; given a December-cost retention,
  then it is scheduled in the December declaration of that year (FR-032).
- **AC-016:** Given ejercicio 2025 of a domiciled juridical person, then the
  declaration and payment due dates both compute to 30-April-2026 (FR-026,
  FR-027).
- **AC-017:** Given a non-domiciled service provider whose SV rents were fully
  retained, then no declaration duty is generated; given the same provider with
  an unretained SV rent, then a self-declaration duty is flagged (FR-033).
- **AC-018:** Given an employer that paid US$5,000.00 voluntarily in
  January-2026 and has FY-2026 ISR payable of US$4,000.00, then
  credit_amount = US$5,000.00, applied_against = US$4,000.00 and
  remanent = US$1,000.00 routed to other ISR obligations (FR-174).
- **AC-019:** Given a ZF user whose credit exceeds its FY-2026 ISR payable,
  then route = certificado_zf_dpa_lsi and the entitlement is recorded with
  certificado_ref pending (issuance = MH external, at declaration
  presentation) (FR-174).
- **AC-020:** Given the F-11 v19 feed for the credit of AC-018, then casilla
  319 = 5,000.00 inside the casilla-330 IMPUESTO DETERMINADO subtraction, and
  casillas 630-648 still carry no value under any configuration (dead
  pago-mínimo rows — R21 extends to v19) (FR-174).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Ley Art. 62 retention-remittance deadline (10 días hábiles) and December rule: is it superseded/complemented by the CT retention-agent regime (CT Arts. 154-160 zone) and CT payment/deadline rules? FR-032 implemented on the Ley text; re-anchor to CT if verification shows divergence (EV05 EVID-063 zone; 03_ EVID-104 doubt). **RESOLVED 2026-08-20 (EVID-351, source 75_): 75_ Art. 100 corroborates Ley Art. 62 — retained sums enter "dentro de los diez días hábiles que inmediatamente sigan al vencimiento del mes calendario en que se efectúa la retención", adding the monthly consolidation of sub-monthly pay cycles (día/período especial/semana/quincena; LB-036); no divergence found — FR-032/LB-027 stand on the Ley text with the anchor corroborated, no re-anchor. The by-NIT-digit window question remains fiscal-reporting's SOQ-08 (`fiscal-reporting/08_filing-calendar.md` OQ-001, by pointer — Art. 100's 10-hábiles is the by-NIT-independent statutory anchor it hunted).** | no | Takumi S2 (CT pass) | resolved |
| OQ-002 | Art. 92 numeral 9 obliges subjects of the "impuesto de timbres" (obsolete stamp tax) and the whole declaration-duty list may be restated by CT declaration articles (03_ OQ-9 carried). Confirm CT-era restatement; numeral disabled in FR-028 meanwhile. | no | Takumi S2 (CT pass) | open |
| OQ-003 | Art. 105-A sanction cites the repealed "inciso 6º del Art. 72" and a 1,000-colon minimum — superseded by the CT sanctions regime (CT Arts. 226-247 zone, EV05 EVID-065). Recorded as informational LB only; no sanction FR written. Confirm final disposition in the fiscal-reporting wave. | no | Takumi S2 (fiscal-reporting wave) | open |
| OQ-004 | SOQ-06 carried: D.E. 117-2001 (the Reglamento mass-repeal instrument) predates the CT — whether any additional 04_ survivor article was later repealed by CT Art. 344 ff. Non-blocking; survivors cited as printed (LB-031; R17). | no | Takumi S2 | open |
| OQ-005 | SOQ-03 (partial): the publishing D.O. issue of D.E. 10-2025 is not pinned in the certified copy — vigencia 2025-05-08 is assumed per MH dating. Affects LB-028 vintage dating and `04_isr-withholding.md` table data. **RESOLVED 2026-08-18 (EVID-171, source 60_): published D.O. N° 79, T. 447, 30-abr-2025, pp. 25-32 → effective 2025-05-08 confirmed; digit fidelity verified in the same pass (see 04 §7 OQ-002).** | no | Takumi S2 (sources registry) | resolved |
| OQ-006 | CT Art. 62 governs FX conversion ("tipo de cambio que corresponda al día" of the hecho generador) but the operational rate source/feed (BCCR/AT-published rate vs. bank rate) is outside the corpus; the Odoo currency-rate feed for the fiscal layer needs selection. | no | Takumi + Odoo implementation | open |
| OQ-007 | F-11 v19/v20 prints not acquired (65_ = v18, superseded as current print): v19 adds casilla 319 "Crédito Tributario Quincena Veinticinco" inside the casilla-330 IMPUESTO DETERMINADO subtraction and STILL prints the dead pago-mínimo rows (R21 extends to v19 — casillas 630-648 stay unfed per FR-174/AC-020); v20 = special-regime subjects with the Certificado de Crédito Tributario anexo. Acquisition candidates (numbering ≥71; MH formularios page watch — kin of payroll/08 OQ-004 and evidence OQ-5; layout builder future). | no | Takumi S6 (sources watch — numbering ≥71) | open |
