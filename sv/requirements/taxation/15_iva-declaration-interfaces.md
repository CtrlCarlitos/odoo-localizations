# SV — Taxation — IVA declaration & interfaces: the Art. 93-94 monthly declaración jurada, import liquidation venues and the operation-classification feeds (Ley IVA Arts. 81, 93-94, 165, 167-175)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the DECLARATION CHASSIS of
El Salvador's IVA (D.L. 296-1992) and for the operation-classification
interface that feeds every declaration surface — the synthesis fold-in of the
S9 IVA-core wave: the Art. 93 *período tributario* (ONE calendar month) and
its monthly *declaración jurada* (sworn declaration) content — the gravadas,
exentas and no sujetas operations realized in the period, the monthly
*débito fiscal*, the same-period *crédito fiscal* and the remanentes
traspasados from prior periods, plus the liquidation of the tax payable or of
the undeducted credit remanente — presented in the formularios the Dirección
General provides (the F-07 v14 chassis, by id); the Art. 94 filing-and-payment
mechanics — the declaration INCLUDES the payment, presented at DGII, the
Dirección General de Tesorería or the Ministerio-de-Hacienda-authorized banks
and financial institutions, DENTRO DE LOS DIEZ PRIMEROS DÍAS HÁBILES del mes
siguiente (within the first ten business days of the following month —
computed on the shared días-hábiles engine, by id), with the agents'
same-lap rule (retained/perceived taxes of agentes de retención o de
percepción entered in the SAME lap); the Art. 94 import-liquidation venues —
goods imports liquidated ANTE LA DIRECCIÓN GENERAL DE LA RENTA DE ADUANAS in
the SAME ACT as the customs taxes, where the payment constancy itself
CONSTITUTES the *comprobante de crédito fiscal* (the credit document), the
oficio liquidation of goods imports at Aduanas with payment at Tesorería, and
services imports liquidated at DGII and paid at Tesorería; the Art. 81
payment-discipline pair — oficio liquidations payable within two months of
the firme resolution, and the ABSOLUTE rule that this tax admits NO
*prórrogas ni facilidades o plazos diferidos* (no extensions, facilities or
deferred terms); the per-operation DECLARATION CLASSIFICATION (gravada-local /
exenta / no-sujeta / 0%-export / ZF-DPA-0 / differentiated-fuel) as the single
classification source that feeds the F-07 annexes 1/2/3 buckets, the R/S
Renta pair (*Tipo de Operación* / *Tipo de Ingreso* — codes 12/13 ISR-side
kin), the débito/crédito casilla graph and the DTE tributo/CAT-015 fields,
with the MOQ-04 closure note (FOVIAL/COTRANS never in the base nor charged as
IVA); and the version-regime closure — the Art. 175 vigencia root
(1-sep-1992), the Art. 165 incorporation note (the 7-m)/17-p/q/final and
65-A-c)/fourth regulations incorporated for facilitation only, never new
hechos generadores), the transitorios 167-172 as D18-*is_historical* notes
(zero operative FRs) and the unconstitutional-arts note (113/123/124/161,
sentencia 17-dic-1992 — already repealed, historical note only).

It does **not** cover: the F-07 casilla formulas, row models, upload formats
and modificatoria flow themselves (fiscal-reporting files — the declaration
chassis SV-FREP-FR-001, the casilla graph FR-004..027, annexes 1/2
FR-045..066 and annex 3 FR-067..078 are cited by id, never restated); the
días-hábiles arithmetic and window-configuration schema
(`fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-200..204 — by id); the
débito/crédito determination machinery (Arts. 62-66 — the determination row
`l10n_sv.iva.period.determination` is REUSED from the adjustments/assets file
of this wave, SV-TAX-FR-295, never duplicated here); the remanente
carryforward ledger (Arts. 67-70 — pro-rata/remanente file, SV-TAX-FR-278 by
id); credit eligibility and its gates (credit file, by id); the
retention/perception machinery itself (retentions file, SV-TAX-FR-303..319 —
only the same-lap entero tie is wired here); the export/reintegro regime
(exports file, SV-TAX-FR-320..337 — only the F-07 feed interplay, by id);
the exempt-operation catalogs (exemptions file, by id — including the
Art. 167-A kill-switch); the fuel differentiated-RATE values and Decreto 321
regime windows (`fiscal-reporting/05_f07-annexes-special.md`
SV-FREP-FR-124..126/133 — by id; this file only tags the classification);
DTE emission itself (`e-invoicing/01_document-types.md` SV-EINV-FR-017/018 —
the CAT-015 tributo matrix is cited by id); and the special-regimes ZF/DPA
routing (SR5 SV-SPE-FR-087 — by id). The filing-calendar obligation schema
(FREP 08-file) owns the window machinery; this file binds the IVA obligation
to it.

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). **SOQ-54 vintage note (rides every 01_/02_ LB in this file):** the
consolidation's last reform stamp is D.L. 71-2015 — post-2015 reforms
unverified; corpus-internal signals negative (DTE stack 44_/45_,
Quincena-25 package 66_/67_, F-07 v14 manual silent); re-verify at
implementation — nowhere more load-bearing than here, since Arts. 93-94 are
the procedure articles the modern online filing stack (F-07 v14) overlays.
**CT re-anchor for procedure:** the Arts. 78-92 belt around Art. 81 and the
Arts. 95-96 followers of Art. 94 are DEROGADO (D.L. 230/00) — filing
procedure, sanctions and administration live in the Código Tributario;
Arts. 93-94 themselves SURVIVE as the operative declaration rule (stamps
(7)/(8)/(D.L. 230/00) touch only their repealed incisos, carried as notes).
**Reglamento = 02_ survivors only** (D.E. 83-1992 consolidated through D.E.
60-1993/10-1996/**117-2001**; mass-repeal stamp (3)); this file cites no
Reglamento article — nothing in the 02_ survivors governs the declaration
chassis. **V1 citation rule:** every LB row below cites 01_ with the EVID id
and the txt page anchor (`=== PAGE n ===` markers of `01_Ley_IVA.pdf.txt`,
verified this task); the SOQ-54 watch rides all of them.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA, Art. 93 incisos 1º-2º y 4º: "PARA EFECTOS DE ESTA LEY, EL PERÍODO TRIBUTARIO SERÁ DE UN MES CALENDARIO. EN CONSECUENCIA, LOS CONTRIBUYENTES Y, EN SU CASO, LOS RESPONSABLES DEL IMPUESTO, DEBERÁN PRESENTAR MENSUALMENTE UNA DECLARACIÓN JURADA SOBRE LAS OPERACIONES GRAVADAS, EXENTAS Y NO SUJETAS REALIZADAS EN EL PERÍODO TRIBUTARIO, EN LA CUAL DEJARÁN CONSTANCIA TANTO DEL DÉBITO FISCAL MENSUAL COMO DEL CRÉDITO FISCAL DEL MISMO PERÍODO, ASÍ COMO DE LOS REMANENTES DE ÉSTE TRASPASADOS DE PERÍODOS TRIBUTARIOS ANTERIORES. (8)" "Igualmente liquidarán el impuesto a pagar o, si correspondiere, liquidarán el remanente del crédito fiscal no deducido del débito fiscal del respectivo período." Incisos 3º/5º/6º DEROGADO (D.L. No. 230/00; (7)). "La declaración deberá presentarse en los formularios que proporcione la Dirección General." | For the purposes of this law the tax period is ONE CALENDAR MONTH. Consequently, taxpayers and, where applicable, responsible parties must MONTHLY present a sworn declaration over the taxed, exempt and non-subject operations realized in the tax period, recording both the monthly fiscal DEBIT and the fiscal CREDIT of the same period, as well as the REMANENTES of the latter transferred from prior tax periods. They likewise liquidate the tax payable or, where applicable, the remanente of fiscal credit not deducted from the respective period's fiscal debit. The declaration must be presented in the forms the Dirección General provides | `sv/sources/01_Ley_IVA.pdf` | Art. 93 p.42 (EVID-330; verified 01_ txt lines 1562-1573, PAGE 42) |
| LB-002 | Ley IVA, Art. 94 incisos 1º-2º: "LA DECLARACIÓN JURADA INCLUIRÁ EL PAGO Y DEBERÁ SER PRESENTADA EN LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS, EN LA DIRECCIÓN GENERAL DE TESORERÍA, EN LOS BANCOS Y OTRAS INSTITUCIONES FINANCIERAS AUTORIZADAS POR EL MINISTERIO DE HACIENDA, EN CUALQUIERA DE LAS OFICINAS QUE ESTAS INSTITUCIONES TENGAN EN EL PAÍS, DENTRO DE LOS DIEZ PRIMEROS DÍAS HÁBILES DEL MES SIGUIENTE AL PERIODO TRIBUTARIO CORRESPONDIENTE. EN ESTE MISMO LAPSO DEBEN INGRESARSE LOS IMPUESTOS RETENIDOS O PERCIBIDOS POR LOS AGENTES DE RETENCIÓN O DE PERCEPCIÓN." | The sworn declaration INCLUDES the payment and must be presented at DGII, at the Dirección General de Tesorería, at the banks and other financial institutions authorized by the Ministerio de Hacienda, at any of the offices these institutions hold in the country, WITHIN THE FIRST TEN BUSINESS DAYS of the month following the corresponding tax period. In this SAME LAPSE the taxes retained or perceived by the retention or perception agents must be entered | `sv/sources/01_Ley_IVA.pdf` | Art. 94 incisos 1º-2º p.43 (EVID-330; verified 01_ txt lines 1583-1592, PAGE 43) |
| LB-003 | Ley IVA, Art. 94 incisos 3º-6º (stamp 8): "EL IMPUESTO SOBRE LAS IMPORTACIONES E INTERNACIONES DE BIENES SERÁ LIQUIDADO ANTE LA DIRECCIÓN GENERAL DE LA RENTA DE ADUANAS, EN EL MISMO ACTO EN QUE SE LIQUIDEN LOS IMPUESTOS ADUANEROS. LA CONSTANCIA DEL PAGO DE ESTE IMPUESTO CONSTITUIRÁ EL COMPROBANTE DE CRÉDITO FISCAL." "LA LIQUIDACIÓN DE OFICIO DEL IMPUESTO SOBRE LAS IMPORTACIONES E INTERNACIONES DE BIENES CORRESPONDERÁ EFECTUARLA A LA DIRECCIÓN GENERAL DE LA RENTA DE ADUANAS." "EN LOS CASOS, PREVISTOS EN LOS INCISOS ANTERIORES EL IMPUESTO DEBERÁ PAGARSE ANTE LA DIRECCIÓN GENERAL DE TESORERÍA." "EL IMPUESTO SOBRE IMPORTACIONES E INTERNACIONES DE SERVICIOS SE LIQUIDARÁ ANTE LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS Y SE PAGARÁ ANTE LA DIRECCIÓN GENERAL DE TESORERÍA. LA COMPETENCIA PARA LIQUIDAR DE OFICIO EL IMPUESTO SOBRE LA IMPORTACIÓN E INTERNACIÓN DE SERVICIOS NO LIQUIDADO CORRESPONDERÁ A LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS. (8)" | The tax on IMPORTATIONS AND INTERNATIONS OF GOODS is liquidated before the Dirección General de la Renta de Aduanas, in the SAME ACT in which the customs taxes are liquidated. The CONSTANCY OF PAYMENT of this tax CONSTITUTES THE COMPROBANTE DE CRÉDITO FISCAL (tax-credit document). The oficio liquidation of the tax on goods importations/internations falls to the Dirección General de la Renta de Aduanas; in the cases of the preceding incisos the tax is paid before the Dirección General de Tesorería. The tax on importations and internations of SERVICES is liquidated before DGII and paid before the Dirección General de Tesorería; the competence to liquidate oficio the tax on unliquidated service importations/internations falls to DGII | `sv/sources/01_Ley_IVA.pdf` | Art. 94 incisos 3º-6º p.43 (EVID-330; verified 01_ txt lines 1593-1600, PAGE 43) |
| LB-004 | Ley IVA, Art. 81 incisos I-II: "Los impuestos liquidados de oficio por la Dirección General o la Dirección General de la Renta de Aduanas, deberán pagarse dentro del plazo de dos meses, contados a partir de la fecha en que quede firme la resolución liquidatoria del impuesto; sin perjuicio que los efectos de la mora en el pago del impuesto se produzcan desde que el mismo debió haber sido legalmente pagado en su totalidad, de conformidad al artículo 94 de esta ley." "Respecto del presente impuesto no proceden prórrogas ni facilidades o plazos diferidos para su pago." | Taxes liquidated oficio by the Dirección General or the Dirección General de la Renta de Aduanas must be paid within a term of TWO MONTHS counted from the date the liquidatory resolution becomes FIRME; without prejudice that the effects of mora in payment are produced from when the tax should have been legally paid in its totality, per Art. 94 of this law. Regarding this tax NO EXTENSIONS, FACILITIES OR DEFERRED TERMS proceed for its payment | `sv/sources/01_Ley_IVA.pdf` | Art. 81 pp.40-41 (EVID-330; verified 01_ txt lines 1505-1511, PAGE 40-41) |
| LB-005 | Ley IVA, Art. 165: "LAS REGULACIONES RESPECTO DE HECHOS GENERADORES CONTENIDAS EN LOS ARTÍCULOS 7 LITERAL m), 17 LITERALES p) Y q) E INCISO FINAL; ASÍ COMO LAS RELACIONADAS CON LAS NO DEDUCCIONES CONTENIDAS EN EL ARTÍCULO 65-A, LITERAL c) E INCISO CUARTO, TODOS DE LA PRESENTE LEY; SE INCORPORAN PARA EFECTOS DE FACILITAR LA APLICACIÓN DE LAS NORMAS Y NO CONSTITUYEN NUEVOS HECHOS GENERADORES O NUEVAS REGLAS DE NO DEDUCCIÓN.(D.L. No. 230/00) (11)" | The regulations regarding hechos generadores contained in Arts. 7-m), 17-p) and q) and final inciso, as well as those related to the non-deductions contained in Art. 65-A-c) and fourth inciso, all of this law, are INCORPORATED to facilitate the application of the norms and DO NOT CONSTITUTE NEW HECHOS GENERADORES OR NEW NON-DEDUCTION RULES | `sv/sources/01_Ley_IVA.pdf` | Art. 165 p.51 (EVID-331; verified 01_ txt lines 1845-1852, PAGE 51) |
| LB-006 | Ley IVA, Arts. 167-172 (Disposiciones Transitorias) — HISTORICAL — Art. 167: "No estarán afectas al impuesto establecido en el artículo 1 de esta ley, la importación o internación de mercaderías exentas del impuesto de timbres, que a la fecha de vigencia de esta ley, se encontraren en las situaciones siguientes: a) Embarcadas en el puerto de origen y que ingresen al país dentro del plazo de sesenta días contados a partir de tal vigencia; y b) Dentro de las Aduanas de la República o Recintos Fiscales, siempre que el registro definitivo de las mismas se verifique en el plazo de treinta días hábiles siguientes a la vigencia de esta ley." Art. 168: "Los contribuyentes del impuesto establecido en el artículo 1 de esta ley, podrán deducir de él un crédito equivalente al cinco por ciento del valor de inventario de los bienes del activo realizable existentes a la fecha de entrada en vigencia de esta ley, por concepto del impuesto de timbres generado en la adquisición, importación o internación de ellas." "La deducción del crédito deberá efectuarse por duodécimas partes en los primeros doce períodos tributarios del impuesto, pero se dará por extinguido el excedente del crédito que no pudiere deducirse." Art. 169: "el impuesto se aplicará a partir de la primera medición posterior a la entrada en vigencia de la ley." Art. 170: "Los precios, valores o coeficientes estipulados en los contratos suscritos con anterioridad a la vigencia de esta ley, se entenderán modificados en lo que corresponda, considerando la incidencia en ellos del presente impuesto y la eliminación del impuesto de timbres." Art. 171: "La ley especial a que se refiere el inciso segundo del Art. 73 de esta ley, deberá emitirse a más tardar dentro de los sesenta días hábiles siguientes a la vigencia de la misma." Art. 172: "Lo dispuesto en el inciso segundo del artículo 77 de esta ley se aplicará después de transcurrido un plazo de seis meses, contados a partir de la fecha de vigencia de la misma." | Transitory regime of the 1-sep-1992 cutover from the stamp-tax system: 167 — pre-vigencia stamp-exempt merchandise imported/interned within 60 days (embarked at origin) or registered within 30 días hábiles (already at Aduanas/Recintos Fiscales) not affected; 168 — 5% inventory credit over the activo realizable existing at vigencia, deducted by TWELFTH PARTS over the first twelve tax periods, excess extinguished; 169 — metered periodic supplies taxed from the first post-vigencia measurement; 170 — pre-vigencia contract prices/values/coefficients understood modified by the IVA incidence and the stamp-tax elimination (parties may agree otherwise); 171 — the Art. 73-2º difierimiento special law to be emitted within 60 días hábiles of vigencia; 172 — the Art. 77-2º certificate-based refund applicable only after six months from vigencia. ALL LAPSED (1992-1993 windows; the 60-day and 12-period clocks ran out decades ago) | `sv/sources/01_Ley_IVA.pdf` | Arts. 167-172 pp.52-53 (EVID-331 range; verified 01_ txt lines 1863-1888, 1890-1894, 1903-1907, PAGE 52-53) |
| LB-007 | Ley IVA, Art. 175: "La presente ley entrará en vigencia el uno de septiembre de mil novecientos noventa y dos, previa publicación en el Diario Oficial." | This law enters into force the first of September of nineteen ninety-two, prior publication in the Diario Oficial | `sv/sources/01_Ley_IVA.pdf` | Art. 175 p.55 (EVID-331; verified 01_ txt lines 1985-1986, PAGE 55) |
| LB-008 | Ley IVA, title block — DECLARATORIA DE INCONSTITUCIONALIDAD: "DECLARATORIA DE INCONSTITUCIONALIDAD: LA SALA DE LO CONSTITUCIONAL DE LA CORTE SUPREMA DE JUSTICIA, DECLARO LOS ARTICULOS 113, 123, 124 Y 161 INCONSTITUCIONALES EN SU CONTENIDO DE UN MODO GENERAL Y OBLIGATORIO, SEGUN RESOLUCION DEL DIA 17 DE DICIEMBRE DE 1992, CONTENIDA EN EXPEDIENTES NUMEROS 3-92 Y 6-92." | Declaration of unconstitutionality: the Constitutional Chamber of the Supreme Court of Justice declared articles 113, 123, 124 and 161 unconstitutional in their content in a general and obligatory manner, per resolution of 17-December-1992, contained in expedientes 3-92 and 6-92 | `sv/sources/01_Ley_IVA.pdf` | Title block pp.56-58 (EVID-304; verified 01_ txt lines 2088-2093, PAGE 58) |

Dead text — never implementable as current law (recorded as notes, not FRs,
per wave constraints): the transitorios 167-172 are EXHAUSTED 1992-cutover
windows (LB-006 — historical notes only, FR-352); Art. 167-A is a LIVE
kill-switch owned by the exemptions file (SV-TAX-FR-206 zone LB — cited by
id, not restated); Art. 173 (stamp-tax family repeal) and the embedded
D.L. 634-1993 interpretación auténtica of it touch pre-vigencia sanctions of
a repealed system — consolidation provenance only; Art. 174 (generic-exemption
nullity) is the exemptions file's gate (by id); the unconstitutional
Arts. 113/123/124/161 (LB-008) were void from the start and are anyway
inside the D.L. 230/00-repealed belt — historical note only; Arts. 78-92 and
95-96 (the procedural belt around the survivors) are DEROGADO — CT re-anchor;
Art. 93 incisos 3º/5º/6º are repealed stamps inside a survivor article
(carried as notes on LB-001). Rgto. non-survivors are per R30(a) derogated
and never cited. The SOQ-54 vintage watch (§2 preamble) applies to every row
above.

## 3. Functional Requirements

### 3.1 The monthly declaration chassis (Arts. 93-94; Art. 81)

- **SV-TAX-FR-338:** The system shall fix the IVA *período tributario* at
  ONE CALENDAR MONTH and shall build, per taxpayer per month, the declaración
  jurada content of Art. 93 inciso 1º as a pure READ of the wave's
  determination machinery: the operations gravadas, exentas and no sujetas
  realized in the period (the operation-classification feed of FR-345), the
  monthly débito fiscal and the same-period crédito fiscal (REUSING the
  period determination row `l10n_sv.iva.period.determination` — the
  Art. 64 row owned by `12_iva-adjustments-assets.md` SV-TAX-FR-295, by id —
  NO competing period model is introduced), and the remanentes traspasados
  de períodos anteriores (the carryforward ledger `l10n_sv.iva.remanente.ledger`
  opening balance, `11_iva-pro-rata-remanente.md` SV-TAX-FR-278, by id); and
  shall liquidate per inciso 2º the impuesto a pagar or, where applicable,
  the remanente del crédito fiscal no deducido — both outcomes recorded on
  the period row handed to the declaration surface.
  (LB-001; EVID-330; TAX 12-file SV-TAX-FR-295; TAX 11-file SV-TAX-FR-278)
- **SV-TAX-FR-339:** The system shall derive the monthly declaration 100%
  from the ledgers and period rows — NO casilla of the declaration surface
  is manually enterable from the IVA side — and shall present it exclusively
  through the DGII-provided formulario (Art. 93 inciso 4º), implemented as
  the F-07 v14 chassis (`fiscal-reporting/01_f07-declaration.md`
  SV-FREP-FR-001, by id): the declaration object, its casilla graph
  (SV-FREP-FR-004..027, by id — never restated here) and the remanente
  balance rows (SV-FREP-FR-026) are consumed as THE surface; under the D9
  freeze-at-filing doctrine the filed declaration is a frozen snapshot —
  corrections route exclusively through the modificatoria flow
  (SV-FREP-FR-040, by id), never silent in-place mutation.
  (LB-001; EVID-330; FREP 01-file SV-FREP-FR-001/004..027/026/040; D9)
- **SV-TAX-FR-340:** The system shall fix the filing-and-payment deadline of
  the monthly declaration — which INCLUDES the payment (la declaración
  jurada incluirá el pago) — at the FIRST TEN DÍAS HÁBILES of the month
  following the tax period, computed as a `first_n_habiles(10)` window over
  the shared días-hábiles engine and window-configuration schema
  (`fiscal-reporting/08_filing-calendar.md` SV-FREP-FR-200..204, by id —
  this file binds the IVA obligation to that machinery and never
  re-implements business-day arithmetic); the due date is recorded on the
  filing object with the payment venue (DGII · Dirección General de
  Tesorería · Ministerio-de-Hacienda-authorized banks/financial institutions,
  any of their in-country offices) as channel metadata.
  (LB-002; EVID-330; FREP 08-file SV-FREP-FR-200..204)
- **SV-TAX-FR-341:** The system shall enter the IVA retained or perceived
  by agentes de retención o de percepción in the SAME ten-días-hábiles lap
  as the declaration (EN ESTE MISMO LAPSO): the retention/perception
  remittance feed of `13_iva-retentions.md` (SV-TAX-FR-317/318, by id —
  the same-period ÍNTEGRAMENTE-entered states and their F-07 Section D
  surfaces) binds to the same window object of FR-340, one lap for both the
  own-tax declaration and the agents' entero; the retention machinery itself
  is never restated here.
  (LB-002; EVID-330; TAX 13-file SV-TAX-FR-317/318)
- **SV-TAX-FR-342:** For the importación/internación of GOODS the system
  shall liquidate the IVA at the Aduanas venue IN THE SAME ACT as the
  customs taxes (the customs-liquidation event carries the IVA line), and
  shall accept the CONSTANCIA DEL PAGO of that IVA as the COMPROBANTE DE
  CRÉDITO FISCAL — the customs payment constancy IS the credit document: the
  import credit of `10_iva-credit-deductibility.md` (import-side gates, by
  id) and the annex 3 customs rows (`03_f07-annexes-purchases.md`
  SV-FREP-FR-074/078, by id) are backed by the constancy, whose acceptance
  anchor (D15) is the customs-liquidation acceptance date snapshotted on the
  import record; the OFICIO liquidation of goods imports falls to Aduanas
  with payment at the Dirección General de Tesorería (venue pair recorded on
  the import object).
  (LB-003; EVID-330; D15; TAX 10-file import gates; FREP 03-file
  SV-FREP-FR-074/078)
- **SV-TAX-FR-343:** For the importación/internación of SERVICES the system
  shall liquidate the IVA at DGII with payment at the Dirección General de
  Tesorería — the self-liquidated service-import IVA posts to the period's
  determination as import-generated tax (the Art. 64 row's import term,
  `12_iva-adjustments-assets.md` SV-TAX-FR-295, by id) and its declaration
  surface is the F-07 import casillas (SV-FREP-FR-010 zone, by id); the
  OFICIO liquidation of unliquidated service imports is DGII's competence —
  recorded as the venue pair of the assessment surface, never as an Odoo-side
  computation.
  (LB-003; EVID-330; TAX 12-file SV-TAX-FR-295; FREP 01-file
  SV-FREP-FR-010)
- **SV-TAX-FR-344:** The system shall enforce the Art. 81 payment
  discipline: (a) NO prórrogas, facilidades or plazos diferidos exist for
  the IVA payment — the monthly liability of FR-340 admits no
  installment/deferral surface, and any payment-plan request on it is
  rejected with ground `art81_ii_no_facilities`; and (b) oficio liquidations
  (DGII or Aduanas) are payable within TWO MONTHS counted from the date the
  liquidatory resolution becomes firme, with mora effects running from when
  the tax was legally payable in its totality per Art. 94 — the two-month
  window recorded on the assessment object as its payment deadline, distinct
  from the monthly-declaration deadline.
  (LB-004; LB-002; EVID-330)

### 3.2 The operation-classification interface (the R/S + feeds fold-in)

- **SV-TAX-FR-345:** The system shall expose ONE per-operation DECLARATION
  CLASSIFICATION, resolved on every IVA-relevant operation line as the
  closed enum: *gravada_local* (locally taxed) · *exenta* (exempt) ·
  *no_sujeta* (non-subject) · *cero_exportacion* (0% export) · *zf_dpa_cero*
  (zona-franca/DPA zero-rate sale) · *combustible_diferenciado*
  (differentiated-rate fuel) — DERIVED exclusively from the wave's
  classifiers, never re-classified: the operation-kind taxonomy
  (`07_iva-framework.md` SV-TAX-FR-176), the exemption-reason registry
  (`08_iva-exemptions.md` SV-TAX-FR-206), the export/0% tests
  (`14_iva-exports-refunds.md` SV-TAX-FR-320/322), the ZF/DPA routing
  (`special-regimes/05_tan-iva-interface.md` SV-SPE-FR-087) and the
  fuel-rate regime (`09_iva-base-rate.md` SV-TAX-FR-240/241) — all by id;
  the enum is the single classification source consumed by every feed of
  FR-346..FR-350.
  (LB-001; EVID-330; TAX 07-file FR-176; TAX 08-file FR-206; TAX 14-file
  FR-320/322; TAX 09-file FR-240/241; SPE 05-file SV-SPE-FR-087)
- **SV-TAX-FR-346:** The system shall route every classified SALE into the
  F-07 annex 1/2 buckets and every classified PURCHASE into the annex 3
  buckets, by id and never restated: annex 1 *Ventas a Contribuyentes*
  rows with their exentas/no sujetas/gravadas locales/third-party columns
  (`02_f07-annexes-sales.md` SV-FREP-FR-045..052), annex 2 *Ventas a
  Consumidor Final* (SV-FREP-FR-053..066 zone) and annex 3 *Compras*
  (`03_f07-annexes-purchases.md` SV-FREP-FR-067..078) — every annex row
  derives from a classified operation and its period; the ONLY manual-entry
  exception is the annex 13 fuel grid
  (`05_f07-annexes-special.md` SV-FREP-FR-124..126, by id), whose global
  net values are captured on the declaration object per its own regime.
  (LB-001; EVID-330; FREP 02-file SV-FREP-FR-045..066; FREP 03-file
  SV-FREP-FR-067..078; FREP 05-file SV-FREP-FR-124..126)
- **SV-TAX-FR-347:** The system shall feed the R/S Renta pair — columns R
  (*Tipo de Operación*) and S (*Tipo de Ingreso*) of annex 1 and the U/V
  twins of annex 2 — from the FR-345 classification, as a FEED and never as
  the owner: the Enero-2025 period gate, the code lists and the column
  models are `02_f07-annexes-sales.md` SV-FREP-FR-051/052 (U/V: FR-062),
  by id; the IVA classification supplies the R selection basis
  (*gravada_local* → R-1 Gravada; *exenta*/*no_sujeta* → R-2 No Gravada o
  Exento / non-subject kin; mixed rows → R-4 Mixta), while codes 12/13
  (F-14/F-910 retention-consolidated income; Art. 6 LISR excluidos) are
  ISR-side routing keys — kin to this classification but NEVER IVA outputs:
  the IVA engine computes no retention consolidation and no excluido status
  from them.
  (LB-001; EVID-330; FREP 02-file SV-FREP-FR-051/052/062)
- **SV-TAX-FR-348:** The system shall aggregate the classified operation
  bases and their computed IVA into the F-07 débito/crédito casilla graph
  exclusively through the annex totals (the graph
  `01_f07-declaration.md` SV-FREP-FR-004..008 sales side and
  SV-FREP-FR-010..015 purchases side, by id — formulas never restated
  here): *gravada_local* bases → the taxed-sales casillas with their débito
  companions; *exenta*/*no_sujeta* → the exempt/non-subject casillas;
  *cero_exportacion* → the export casillas and *zf_dpa_cero* → casilla 93
  (the exports-file feed SV-TAX-FR-336, by id);
  *combustible_diferenciado* → casillas 586-589 (FREP 05-file, by id); no
  casilla ever computes from an unclassified operation, and no
  classification ever writes a casilla outside its bucket.
  (LB-001; EVID-330; FREP 01-file SV-FREP-FR-004..015; TAX 14-file
  SV-TAX-FR-336; FREP 05-file SV-FREP-FR-126)
- **SV-TAX-FR-349:** The system shall keep the DTE tributo emission and the
  declaration feed on the SAME classification source: the FR-345 enum and
  the computed IVA per operation are what the DTE stack emits as its
  tributo fields over the CAT-015 catalog (`e-invoicing/01_document-types.md`
  SV-EINV-FR-017 per-type tributo restrictions — 20 IVA 13%, C3 export 0%
  — and SV-EINV-FR-018 non-taxable *cargos/abonos*, by id); a
  reclassification of an operation propagates to BOTH the annex/casilla
  feed and the DTE tributo lines — the system shall never hold divergent
  IVA classification surfaces between invoicing and declaration.
  (LB-001; EVID-330; EINV 01-file SV-EINV-FR-017/018)
- **SV-TAX-FR-350:** The system shall enforce the MOQ-04 closure on every
  declaration-side surface: FOVIAL and COTRANS contributions are NEVER part
  of the IVA base, NEVER charged or recargado as IVA, and NEVER surface as
  IVA débito or crédito in any casilla — the base/rate file's guard
  (`09_iva-base-rate.md` SV-TAX-FR-242/245, by id) is inherited by this
  interface: the *combustible_diferenciado* classification carries a base
  NET of the FOVIAL tributo, routes its values to the annex 13 grid
  (SV-FREP-FR-124..126, by id) with its own débito/crédito companions at
  the differentiated rate, and the per-gallon contributions ride their own
  contribution rows outside the IVA casilla graph entirely.
  (LB-001; EVID-330; TAX 09-file SV-TAX-FR-242/245; FREP 05-file
  SV-FREP-FR-124..126)

### 3.3 Version regime and historical notes (Arts. 165, 167-172, 175)

- **SV-TAX-FR-351:** The system shall key every IVA dated row of the
  localization to the Art. 175 vigencia root — the law in force since
  1-sep-1992 (D12 version-regime discipline): the rate vintages
  (10% → 13%, D.L. 370-1995), the D.L. 645-2005 import-service
  interpretation cutover (2005-03-26), the reform stamps (1)-(14) and every
  regime window of the S9 files resolve against this root; no IVA parameter
  may carry a valid-from earlier than 1992-09-01, and the consolidation
  itself is pinned through reform (14) D.L. 71-2015 under the SOQ-54 watch.
  (LB-007; EVID-331/304)
- **SV-TAX-FR-352:** The system shall record the transitorios 167-172 as
  HISTORICAL NOTE rows ONLY — zero operative FRs, D18 *is_historical* kin
  (exhausted 1992-1993 cutover windows, never implementable as current
  law): Art. 167 (pre-vigencia stamp-exempt merchandise: 60-day embarkation
  / 30-días-hábiles registration windows), Art. 168 (5% inventory credit by
  duodécimas over the first twelve periods, excess extinguished), Art. 169
  (metered supplies from the first post-vigencia measurement), Art. 170
  (pre-vigencia contract-price modification by IVA incidence), Art. 171
  (Art. 73-2º difierimiento special law, 60 días hábiles to emit) and
  Art. 172 (Art. 77-2º certificate refund deferred six months) — each
  carried as a dated historical note on the version regime, with NO
  computation, NO window monitor and NO credit ledger entry ever generated
  from them; Art. 167-A is excluded from this note (a LIVE kill-switch
  owned by the exemptions file, by id).
  (LB-006; EVID-331; D18 kin)
- **SV-TAX-FR-353:** The system shall record two provenance notes of the
  consolidation and nothing more: (a) the Art. 165 incorporation note — the
  hechos-generadores regulations of Arts. 7-m), 17-p)/q)/final and the
  non-deduction regulations of Art. 65-A-c)/fourth inciso are INCORPORATED
  into the law for facilitation only and constitute NO new hechos
  generadores nor new non-deduction rules: the corresponding catalog rows
  of the framework/services/credit files carry their single classification,
  never a double-counted "incorporated" twin; and (b) the
  unconstitutional-arts note — Arts. 113/123/124/161 are void per the Sala
  de lo Constitucional resolution of 17-dic-1992 (expedientes 3-92/6-92)
  and in any case sit inside the D.L. 230/00-repealed belt: historical
  note only, no row, no guard, no dead-text FR beyond this note.
  (LB-005; LB-008; EVID-331/304)

## 4. Data Model

No CSV sidecars live next to this file (wave constraint: NO CSV sidecars);
the only dated data is the version-regime root constant and the historical
notes (in-file §4 rows, never seed tables). Layer semantics: Odoo-side
classification/filing-interface data only (wave default `odoo`; see §5).
**Interface entity for the wave's index and the fiscal-reporting
consumers:** the declaration-classification field + the filing-window binding
below — the period determination row itself is REUSED
(`l10n_sv.iva.period.determination`, adjustments/assets file — no competing
model is created here).

**Declaration classification (per operation line):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (SV extension) | l10n_sv_iva_declaration_class | select (computed, stored) | gravada_local · exenta · no_sujeta · cero_exportacion · zf_dpa_cero · combustible_diferenciado — derived from T1/T2/T3/T4/SR5 classifiers; D15: resolved as-of the tax-point snapshot, never recomputed for a filed period | FR-345 |
| account.move.line (SV extension) | l10n_sv_iva_declaration_class_source | m2o / char | the owning classifier row (exemption reason · export test · ZF/DPA fiscal position · fuel regime) + its file/FR anchor string | FR-345 |
| account.move.line (fuel) | l10n_sv_iva_base_net_of_fovial | monetary (computed) | base net of the FOVIAL/COTRANS tributos (T3 guard SV-TAX-FR-242) — the only base the declaration feed may read for combustible_diferenciado | FR-350 |

**Filing chassis (window binding + freeze):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.declaration.filing (new) | company_id, period, state | m2o / char / select | state: draft · due · filed · modificatoria_pending; one per taxpayer per período tributario | FR-338, FR-339 |
| l10n_sv.iva.declaration.filing | window_rule_ref, due_date | m2o / date | window_rule → FREP 08-file config as first_n_habiles(10); due_date computed by SV-FREP-FR-201/203 — never local arithmetic | FR-340 |
| l10n_sv.iva.declaration.filing | payment_venue, filed_at, frozen_snapshot_id | select / datetime / m2o | venue: dgii · tesoreria · authorized_bank; D9 freeze: filed values immutable, corrections via modificatoria (FREP FR-040 by id) | FR-339, FR-340 |
| l10n_sv.iva.declaration.filing | agents_lap_link | m2m | retention/perception remittances of the same lap (T7 feed SV-TAX-FR-317/318) | FR-341 |
| l10n_sv.iva.declaration.filing | determination_row_id, remanente_opening_id | m2o / m2o | → l10n_sv.iva.period.determination (REUSE — T6) and l10n_sv.iva.remanente.ledger (T5): the Art. 93 content is a read of these rows | FR-338 |

**Import venues and constancy anchor:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (goods import) | l10n_sv_iva_customs_liquidation_venue, payment_venue | select | liquidation: aduana (same act as customs taxes); payment: tesoreria; oficio-liquidation venue pair aduana/tesoreria | FR-342 |
| account.move (goods import) | l10n_sv_iva_constancy_credit_doc | boolean + ref | the payment constancy IS the comprobante de crédito fiscal — the credit-document reference of the import credit (T10 gates consume); acceptance anchor D15 below | FR-342 |
| account.move (goods import) | l10n_sv_iva_constancy_acceptance_date | date (snapshotted) | customs-liquidation acceptance anchor — the D15 as-of date for the constancy-backed credit | FR-342 |
| account.move (services import) | l10n_sv_iva_service_import_venue | select | liquidation: dgii; payment: tesoreria; oficio competence: dgii | FR-343 |

**Version regime (note rows, not seed data):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.version.regime (config constant) | vigencia_root | date | 1992-09-01 (Art. 175) — the valid-from floor of every IVA dated row | FR-351 |
| l10n_sv.iva.version.regime | historical_notes | text (note rows, is_historical kin) | transitorios 167-172 exhausted windows (167: 60d/30-hábiles; 168: 5% duodécimas; 169: first measurement; 170: contract adaptation; 171: 60-hábiles special law; 172: 6-month deferral); unconstitutional 113/123/124/161 (sent. 17-dic-1992); Art. 165 incorporation provenance — ZERO computation attached | FR-352, FR-353 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = classification/filing-interface
computation logic living in the LGPL client; `shared` = logic whose data
lives on Odoo models but whose enforcement spans the SaaS DTE layer (the one
architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are stable
across Odoo 17/18/19/20 (`account.move`, `account.move.line`; the new
`l10n_sv.iva.declaration.filing` is localization-side). D15 doctrine
(binding): every parameter resolves as-of the tax-point/acceptance snapshot;
D9: filed declarations are frozen artifacts corrected only via
modificatoria. **Version-regime note (binding, rides every row):** the 01_
print is the consolidation through D.L. 71-2015 and the 02_ print through
D.E. 117-2001 — SOQ-54 vintage watch on every legal parameter above; the
DIFFERENTIATED-FUEL regime windows and rate values are dated-regime rows
owned by `fiscal-reporting/05_f07-annexes-special.md` (SV-FREP-FR-124..126/
133, by id — Decreto 321 kin: from Mar-2022, its prórrogas or similar
decretos; this file only tags *combustible_diferenciado* and consumes their
config, never re-dating it).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-338 | odoo | l10n_sv.iva.declaration.filing → determination/remanente rows | period content read | REUSES l10n_sv.iva.period.determination (T6 SV-TAX-FR-295) + remanente ledger (T5 SV-TAX-FR-278) — no competing period model |
| FR-339 | odoo | l10n_sv.iva.declaration.filing + FREP F-07 object | frozen_snapshot + surface binding | 100% ledger-derived; D9 freeze; modificatoria = SV-FREP-FR-040 by id |
| FR-340 | odoo | l10n_sv.iva.declaration.filing | window_rule_ref + due_date | first_n_habiles(10) via SV-FREP-FR-200..204; declaration includes payment; venues as metadata |
| FR-341 | odoo | l10n_sv.iva.declaration.filing | agents_lap_link | Same lap for agentes' entero; retention machinery = T7 SV-TAX-FR-317/318 by id |
| FR-342 | odoo | account.move (goods import) | constancy_credit_doc + acceptance_date | Constancy = comprobante de crédito fiscal; D15 acceptance anchor; oficio venue pair aduana/tesorería |
| FR-343 | odoo | account.move (services import) | service_import_venue | DGII liquidation / Tesorería payment; oficio competence DGII; posts to the Art. 64 import term (T6 by id) |
| FR-344 | odoo | computation guard + assessment object | art81_ii ground + two-month window | No deferral surface ever on the monthly liability; oficio deadline = firme + 2 months |
| FR-345 | odoo | account.move.line | declaration_class enum | Derived from T1/T2/T3/T4/SR5 classifiers by id; single source for FR-346..350 |
| FR-346 | odoo | account.move.line → FREP annex rows | bucket routing | Annex 1/2/3 row models owned by FREP 02/03 files by id; annex 13 manual grid = FREP 05-file by id |
| FR-347 | odoo | account.move.line → FREP R/S columns | R/S feed | Gate + lists = SV-FREP-FR-051/052 (U/V FR-062) by id; codes 12/13 ISR-side kin — never IVA outputs |
| FR-348 | odoo | computation (annex totals → casillas) | casilla graph feed | Graph = SV-FREP-FR-004..015 by id; export/ZF feed = SV-TAX-FR-336 by id; no casilla from unclassified ops |
| FR-349 | shared | account.move.line + account.tax | tributo consistency | Odoo tax templates carry the CAT-015 codes (EINV FR-017 mapping); SaaS validates per-type (SV-EINV-FR-017/018 by id) — one classification source for both surfaces |
| FR-350 | odoo | account.move.line (fuel) | base_net_of_fovial | MOQ-04 closure: FOVIAL/COTRANS never in base nor charged (T3 SV-TAX-FR-242/245 by id); annex 13 routing = FREP 05-file by id |
| FR-351 | odoo | l10n_sv.iva.version.regime | vigencia_root 1992-09-01 | D12 root of every IVA dated row; consolidation pinned D.L. 71-2015 (SOQ-54) |
| FR-352 | odoo | l10n_sv.iva.version.regime | historical_notes | Transitorios 167-172 note rows, is_historical kin, ZERO computation; 167-A excluded (exemptions file owns) |
| FR-353 | odoo | l10n_sv.iva.version.regime | incorporation + void-arts notes | Art. 165 facilitation-only (no double-counted catalog twins); 113/123/124/161 void since 17-dic-1992 — note only |

Version-regime notes (D12/D15/D9): FR-351 carries the Art. 175 root; FR-340
carries the window-vintage discipline (asueto tables are year-keyed data
owned by the FREP 08-file); FR-342 carries the D15 acceptance anchor; FR-339
carries the D9 freeze. The SOQ-54 consolidation watch rides every LB (§2
preamble) — re-verify against a current official consolidation at
implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a March period with gravadas $50,000.00, exentas
  $10,000.00, no sujetas $2,000.00, débito $6,500.00, crédito $4,100.00 and
  a remanente traspasado of $300.00, when the monthly declaration is built,
  then every content element derives from the period determination row and
  the remanente ledger (no manual casilla exists) and the liquidation shows
  impuesto a pagar $2,100.00 (FR-338, FR-339).
- **AC-002:** Given a period whose following month starts with two asuetos
  in its first two weekdays, when the filing deadline computes, then the due
  date is the 10th DÍA HÁBIL of that month per the shared engine
  (first_n_habiles(10), asuetos skipped) — never the 10th calendar day
  (FR-340).
- **AC-003:** Given an agent's March retentions entered ÍNTEGRAMENTE within
  the same ten-hábiles lap, when the lap closes, then both the own-tax
  declaration and the agents' entero carry the same window object and due
  date (FR-341).
- **AC-004:** Given a goods import liquidated at Aduanas in the same act as
  the customs duties with its IVA paid there, when the import posts, then
  the payment CONSTANCIA is accepted as the credit document backing the
  crédito fiscal (annex 3 customs row), anchored at the
  customs-liquidation acceptance date — no CCF is demanded for that credit
  (FR-342).
- **AC-005:** Given a services import from a foreign provider utilized
  exclusively in El Salvador, when its IVA self-liquidates, then the venue
  pair is DGII (liquidation) / Tesorería (payment) and the tax posts to the
  period determination's import term (FR-343).
- **AC-006:** Given a user requesting a payment plan or deferred term on the
  monthly IVA liability, when the request is submitted, then it is REJECTED
  with ground `art81_ii_no_facilities`; given an oficio liquidation that
  became firme on 10-May, then its payment deadline records 10-July (two
  months) with mora effects from the original Art. 94 due date (FR-344).
- **AC-007:** Given a sale to a zona franca user (ZF/DPA 0% route) and an
  export of goods in the same period, when classification resolves, then the
  two lines carry *zf_dpa_cero* and *cero_exportacion* respectively and feed
  casilla 93 and the export casillas — never the gravada-local buckets
  (FR-345, FR-348).
- **AC-008:** Given a post-Enero-2025 annex 1 row over a gravada-local
  sale, when the R/S pair fills, then R = 1 (Gravada) derived from the
  classification; given a row whose income was already F-14-retained, then
  R = 12 is applied as ISR-side routing — the IVA classification is unchanged
  by it (FR-347).
- **AC-009:** Given a fuel sale at a differentiated rate with $0.20/galón
  FOVIAL inside the gross charge, when the declaration feed runs, then the
  operation classifies *combustible_diferenciado*, its base enters the
  annex 13 routing NET of the FOVIAL tributo, and no FOVIAL amount ever
  appears as IVA débito/crédito in any casilla (FR-350).
- **AC-010:** Given an operation reclassified from exenta to gravada-local
  before filing, when the change posts, then both the annex 1 bucket and
  the DTE tributo line (CAT-015 code 20) reflect gravada-local — no
  divergent surfaces survive (FR-349).
- **AC-011:** Given any IVA dated row with valid_from before 1-sep-1992,
  when the version regime validates, then the row is rejected (vigencia
  root floor); given the transitorios notes, then no computation, window
  monitor or ledger entry ever generates from them (FR-351, FR-352).
- **AC-012:** Given the Art. 7-m)/17-p)/65-A-c) catalog rows, when the
  incorporation note applies, then each carries exactly ONE classification —
  no duplicated "incorporated" twin row exists anywhere (FR-353).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 — post-2015 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Arts. 93-94 are the procedure articles most exposed to post-2015 administrative overlay (online filing, payment channels, agent laps) — re-verify them and the Art. 81 pair at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | Pre-DTE physical-invoice ingestion (D15/D18 history contract): periods before the DTE mandate are declared over physical CCFs/facturas — FR-346's "every annex row derives from a classified operation" must hold for ingested pre-DTE periods too, where no sealed DTE record exists (clase 1/2/3 documents). The D18(b) tiered-import contract (T1 transactional detail imported `is_historical`, T2 frozen declaration snapshots, T4 carryover ledgers) is the ingestion path; confirm the physical-document → classified-line mapping (identifier slots per SV-FREP-FR-042/043, no DTE seals) at implementation so the declaration feed stays 100%-derived for historical filings. | no | Takumi S9 + Odoo implementation | open |
| OQ-3 | Decreto 321 kin pointer: the *combustible_diferenciado* classification of FR-345/350 depends on the differentiated-rate regime windows and per-grade rate VALUES owned by `fiscal-reporting/05_f07-annexes-special.md` (SV-FREP-FR-124..126/133, by id — from Mar-2022 during Decreto 321's validity, its prórrogas or similar decretos; rate values themselves that file's OQ-001 config gap). This file consumes their config and never re-dates it; when the decree lapses or is extended, only the 05-file regime rows change — verify the config load at implementation (MOQ-04/SOQ-39 kin: the decree text is not in the corpus). | no | Takumi S9 + Odoo implementation | open |
