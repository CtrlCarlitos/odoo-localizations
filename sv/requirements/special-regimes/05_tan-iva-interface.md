# SV — Special regimes — TAN/IVA interface: internaciones, 0% routing, cross-regime sales, retentions

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes); W19 T3 re-verification (80_) |
| Updated | 2026-08-22 |

## 1. Purpose

This file owns the fiscal ROUTING of regime transactions into the tax and
customs engines: the *internación* (entry for consumption) of ZF/DPA
production into the *territorio aduanero nacional* (national customs
territory, TAN) paying import duties ONLY on the non-national component,
with the verbatim cost rule (*valor en aduana* = materias primas + gastos
indirectos de fabricación), the comercializador full-value-minus-
demonstrated-national base, the NMF tariff with its TLC-origin exception,
and the minimum-value floor at the entry value/CIF (12_ Art. 3 final
block); the TAN→ZF/DPA sales route at 0% IVA + Ley IVA Arts. 76/77 —
12_ Art. 25, the F-07 annex-3 tipo-11 printed authority — with the
not-necessary-goods inversion to the full Art. 54 rate, the market-price
rule with DGII adjustment powers, the out-of-agreement full-tax guard and
the comercializador TAN-sale route; the B2B intra-regime no-tax route
(12_ Art. 3); the *materia-prima* TAN-consumption and
desperdicios/subproductos disposition paths (12_ Art. 27); the LSI export
test and local-market routing with the dual-retention pair **1.5% ISR
anticipo / 1% IVA anticipo** and the CT-anticipo suppression flag (14_
Art. 8); the cross-regime services FCF rule (LSI a)/b) services to ZF/DPA
beneficiaries, directly export-linked, documented via *factura de
consumidor final* naming the *prestatario*); the LSI goods interface
(TAN→parque/centro = *exportación definitiva* under Ley IVA Arts. 75-77 —
NEVER merged with ZF's 0% + Arts. 76/77 route; parque/centro→TAN goods =
*importación definitiva* with the importer as *sujeto pasivo*); and the
SS-solvency gate on every regime sale (prior-month ISSS/AFP solvency,
verified by electronic means per 12_ Art. 9-A). **THE invariant of this
file: ZF Art. 25 TAN-sales rule (0% IVA + Ley IVA Arts. 76/77) and LSI
Art. 26 (exportación definitiva, Ley IVA Arts. 75-77) are DISTINCT
fiscal-position families, never unified** (SV-SPE-FR-087 vs SV-SPE-FR-101).

It does **not** cover: the exemption ladders, exception-goods gates and
the comercializador incentive-exclusion/municipal-proration computation
(`02_zf-exemption-schedules.md` — FR-036/FR-041 by id); the LSI exemption
shapes, local-market caps and dictamen data pack (`03_lsi-regime.md` —
FR-048/FR-053/FR-054 by id); the customs clocks and DM/destinación record
surfaces (`04_customs-clocks.md` by id); the DUCA record model,
teledespacho chassis and the simplified-withdrawal PROCEDURE
(`06_customs-declarations.md` — T6 by id); the descargo/cost registers and
sanctions (`07_obligations-reporting-sanctions.md` — 12_ Art. 28 p/q cost
registers by id); FOVIAL/COTRANS (`08_fovial-cotrans.md`). The Ley IVA
Arts. 54/75/76/77 COMPUTATION mechanics (rate application, débito/crédito,
devolución) are the IVA-core taxation wave's by pointer — this file owns
the fiscal-position ROUTING that selects them, never the tax math; the
retention computation engine (moment-of-payment mechanics, remittance
deadlines) is `taxation/04_isr-withholding.md`'s by id (SV-TAX-FR-121..129
family); the FCF/FE and CRE document surfaces are e-invoicing's by id.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): ZF TAN
interface = **12_** (D.L. Nº 405, 3-sep-1998, D.O. N° 176 T.340 23-sep-1998;
consolidated through reform (8) D.L. 318-2013; content title "Ley de Zonas
Francas Industriales y de Comercialización"; W19 T3: ZF tail = 82_, D.L.
Nº 493-2025, vigencia ~31-dic-2025 — its Art. 17/18/19 extension changes
do not touch THIS file's routing surfaces; co-cite 12_+82_ where the ZF
tail matters); LSI interface = **80_**
(Ley de Servicios Internacionales, D.L. Nº 431, 11-oct-2007, as reformed
by D.L. Nº 277-2013, D.O. N° 28 T.398 11-feb-2013 → vigencia ~19-feb-2013
for the reformed articles — **W19 T3: supersedes 14_ thru D.L. 277-2013**;
LBs re-keyed 14_→80_; Art. 8's local-market/retention letter set drops h)
from ~19-feb-2013); customs-chassis kin = **74_** (D.L. Nº 529,
13-ene-1999, D.O. N° 23 T.342 3-feb-1999; consolidated through reform (4)
D.L. 23-2012) — cited here ONLY for the Art. 11-A h) SS-solvencia kin (the
withdrawal procedure itself is `06`'s). **Ley IVA anchors (pointer
authority):** Ley de Impuesto a la Transferencia de Bienes Muebles y a la
Prestación de Servicios (`sv/sources/01_Ley_IVA.pdf`) Arts. 54 (13% rate),
75 (exports), 76 and 77 (refund/credit regime) ride INSIDE the 12_/80_
prints below as the invoked articles — their computation mechanics are the
IVA-core taxation wave's by pointer (not yet written; consumed when it
lands), never restated here. Cross-topic pointers consumed by id:
fiscal-reporting/03 annex-3 tipo-11 gate SV-FREP-FR-073 (34_ manual kin);
taxation/04 withholding engine SV-TAX-FR-121..129; e-invoicing FCF/FE doc
rules SV-EINV-FR-019/020/021 + CRE retention document SV-EINV-FR-035;
payroll/05-06 SS cotización records SV-PAY-FR-066/072/093.

**SOQ-30 verification note (rides EVERY regime LB in this file):** the 12_
consolidation ends at D.L. 318-2013 (tail = 82_, D.L. 493-2025, W19 T3)
and 74_ at D.L. 23-2012 — post-cutoff traffic unverified beyond those
tails (SOQ-22 kin; D.L. 598-2020-era watch); **W19 T3: the LSI half
RESOLVED — 14_ superseded by 80_ (consolidated thru D.L. 277-2013; LBs
re-keyed)**; article text is cited **as printed** (12_ prints Arts. 21
onward in UPPERCASE; 80_/74_ print sentence case — casing preserved;
reformed incisos in 80_ print in CAPS). Verbatim text
below is copied from the W13 evidence files (EVID-252/257/261/263/270),
the W19 T3 evidence (EVID-383 of `80_82_LSI_ZF.evidence.md`) and, where
the evidence abbreviates, from the extraction txts
`sv/.extractions/12_Ley_Zonas_Francas.pdf.txt`,
`sv/.extractions/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf.txt`
(the LSI text of record; the superseded
`sv/.extractions/14_Ley_Servicios_Internacionales.pdf.txt` remains the
pre-277 provenance record) and
`sv/.extractions/74_Ley_Simplificacion_Aduanera_D529.pdf.txt` (citable per
standing S3 ruling 25; page pointers = txt PAGE markers). D15 discipline:
every rate, base rule and retention value in this file is a dated config
row with instrument provenance — never a global constant — resolved as-of
the transaction date and snapshotted on the record.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Zonas Francas, Art. 3 (final block): "CUANDO LOS BIENES PRODUCIDOS EN ZONAS FRANCAS O DPA SEAN VENDIDOS AL TERRITORIO ADUANERO NACIONAL POR UN PRODUCTOR AUTORIZADO AL EFECTO, ÉSTE DEBERÁ INTERNAR LOS BIENES, PAGANDO LOS DERECHOS E IMPUESTOS A LA IMPORTACIÓN SOBRE EL VALOR EN ADUANAS, ÚNICAMENTE POR EL COMPONENTE NO NACIONAL INCORPORADO AL PRODUCTO FINAL. LAS VENTAS AL MERCADO NACIONAL DE SUBPRODUCTOS TENDRÁN EL MISMO TRATAMIENTO." "LOS COMERCIALIZADORES AL REALIZAR VENTAS AL TERRITORIO ADUANERO NACIONAL, DEBERÁN INTERNAR LOS BIENES PAGANDO LOS DERECHOS E IMPUESTOS A LA IMPORTACIÓN SOBRE EL VALOR EN ADUANAS. EN EL CASO DE BIENES ADQUIRIDOS DE UN PRODUCTOR ESTABLECIDO DE CONFORMIDAD CON ESTA LEY, LOS DERECHOS E IMPUESTOS A LA IMPORTACIÓN SE CALCULARÁN SOBRE EL VALOR EN ADUANAS DEL BIEN, EXCLUYENDO DE DICHA BASE EL VALOR DEL COMPONENTE NACIONAL INCORPORADO AL PRODUCTO FINAL, SIEMPRE Y CUANDO EL COMERCIALIZADOR DEMUESTRE EL VALOR DE DICHOS COMPONENTES." "EL ARANCEL APLICABLE SERÁ EL DE LA NACIÓN MÁS FAVORECIDA (NMF). NO OBSTANTE, EN CASO QUE LOS COMERCIALIZADORES EFECTÚEN INTERNACIONES DE BIENES ORIGINARIOS DE TERCEROS PAÍSES CON LOS CUALES SE TIENE UN ACUERDO DE LIBRE COMERCIO, PODRÁN APLICAR AL TRATO PREFERENCIAL, SIEMPRE QUE DEMUESTREN LA AUTORIDAD ADUANERA QUE LAS MERCANCÍAS NO HAN SUFRIDO NINGUNA TRANSFORMACIÓN EN EL PAÍS, QUE HAN PERMANECIDO EN TODO MOMENTO BAJO CONTROL ADUANERO Y QUE CUMPLEN CON LOS DEMÁS REQUISITOS ESTABLECIDOS PARA GOZAR DE PREFERENCIAS ARANCELARIAS." "EN NINGÚN CASO EL VALOR DECLARADO DE LOS BIENES QUE SE INTERNEN AL PAÍS PODRÁ SER INFERIOR AL VALOR CON QUE LOS BIENES INGRESARON A LA ZONA FRANCA O DPA, EL QUE PARA EL CASO DE LAS MATERIAS PRIMAS E INSUMOS, NO PODRÁ SER MENOR AL VALOR EN ADUANAS ESTABLECIDO EN LA DECLARACIÓN DE MERCANCÍAS. EN LAS TRANSACCIONES EFECTUADAS, LOS DOCUMENTOS DE SOPORTE COMERCIAL, TRIBUTARIO Y CONTABLE DEBERÁN REFLEJAR EL VALOR AGREGADO NACIONAL POR LOS PROCESOS DE TRANSFORMACIÓN, ELABORACIÓN Y REPARACIÓN A LOS QUE FUERON SOMETIDOS DICHOS BIENES. PARA AQUELLAS MERCANCÍAS QUE HAN SUFRIDO TRANSFORMACIÓN, EL VALOR EN ADUANAS DEBERÁ CONTENER EL COSTO DE MATERIAS PRIMAS Y GASTOS INDIRECTOS DE FABRICACIÓN." "LAS VENTAS O COMPRAS DE BIENES NECESARIOS PARA LA ACTIVIDAD AUTORIZADA, EFECTUADAS ENTRE BENEFICIARIOS DEL RÉGIMEN ESTABLECIDO EN ESTA LEY, NO CAUSARÁN DERECHOS E IMPUESTOS, INCLUYENDO EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS; LO ANTERIOR, SERÁ APLICABLE EN EL CASO DEL DPA, SIEMPRE Y CUANDO SE REALICEN DENTRO DEL PLAZO LEGAL DEL RÉGIMEN ADUANERO CORRESPONDIENTE Y EN NINGÚN CASO LAS TRANSFERENCIAS DE MERCANCÍAS A CUALQUIER TÍTULO SE CONSIDERARÁN COMO MOTIVO PARA AMPLIAR DICHO PLAZO." "PARA REALIZAR LAS VENTAS DE LOS BIENES, LOS BENEFICIARIOS DE ESTA LEY TAMBIÉN DEBERÁN COMPROBAR A LA AUTORIDAD ADUANERA LA SOLVENCIA EN EL PAGO AL INSTITUTO SALVADOREÑO DEL SEGURO SOCIAL Y A LAS DIFERENTES ADMINISTRADORAS DE FONDOS DE PENSIONES, DE LAS COTIZACIONES Y RETENCIONES EFECTUADAS A SUS TRABAJADORES, ASÍ COMO DE LAS APORTACIONES EFECTUADAS POR EL PATRONO, CORRESPONDIENTES AL MES PRÓXIMO ANTERIOR A AQUÉL EN EL QUE SE LLEVE A CABO LA VENTA." | When goods produced in zonas francas or DPAs are sold into the national customs territory by a producer authorized for that purpose, the producer must intern the goods paying import duties and taxes on the customs value ONLY for the NON-NATIONAL component incorporated into the final product; national-market sales of byproducts take the SAME treatment. Comercializadores (marketers) making TAN sales intern the goods paying duties on the customs value; for goods acquired from a law-established producer, duties compute on the good's customs value EXCLUDING the value of the NATIONAL component incorporated into the final product, PROVIDED the comercializador demonstrates the value of those components. The applicable tariff is most-favoured-nation (NMF); comercializadores interning goods originating in third countries with a free-trade agreement may apply preferential treatment provided they demonstrate to the customs authority that the goods underwent NO transformation in-country, remained at all times under customs control, and meet the remaining preferential-tariff requirements. The declared value of interned goods may NEVER be below the value at which the goods entered the zona franca or DPA — for materias primas and insumos, never below the customs value established in the goods declaration; commercial, tax and accounting support documents must reflect the NATIONAL value added by the transformation, elaboration and repair processes; for goods that underwent transformation the customs value MUST contain the cost of raw materials and indirect manufacturing costs. Sales or purchases of goods necessary for the authorized activity between beneficiaries of the regime cause NO duties or taxes, INCLUDING IVA — applicable to DPA provided made within the legal term of the corresponding customs regime, and transfers of merchandise at any title are NEVER a reason to extend that term. To make sales of the goods, beneficiaries must also prove to the customs authority solvency in payment to the ISSS and the AFPs of the contributions and retentions effected on their workers and of the employer contributions, corresponding to the month next prior to that of the sale | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 3 final block pp.5-6 (EVID-252; txt PAGE 5-6; SOQ-30 print) |
| LB-002 | Ley de Zonas Francas, Art. 9-A: "LA COMPROBACIÓN DE LA SOLVENCIA EN EL PAGO A LAS INSTITUCIONES DE PREVISIÓN Y SEGURIDAD SOCIAL, ESTABLECIDAS PARA USUARIOS DE ZONAS FRANCAS Y DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO, SE REALIZARÁ MEDIANTE EL USO DE REDES DE COMUNICACIÓN ELECTRÓNICA, CUYAS ESPECIFICACIONES DE SEGURIDAD SERÁN ESTABLECIDAS POR LA DIRECCIÓN GENERAL DE ADUANAS. DICHA OFICINA ESTABLECERÁ MECANISMOS DE CONSULTA EN LÍNEA QUE FACILITEN LA VERIFICACIÓN DEL CUMPLIMIENTO DE LAS PRESENTES DISPOSICIONES. EN CASO DE FUERZA MAYOR O CASO FORTUITO, LA DIRECCIÓN GENERAL DE ADUANAS ADOPTARÁ LAS MEDIDAS DE CONTINGENCIA QUE GARANTICEN LA CONTINUIDAD DE LAS OPERACIONES, EN COORDINACIÓN CON DICHAS INSTITUCIONES. (5) (8)" | Proof of solvency in payment to the social-security and welfare institutions established for ZF usuarios and DPAs is made THROUGH ELECTRONIC COMMUNICATION NETWORKS whose security specifications the DGA establishes; that office establishes ONLINE CONSULTATION mechanisms facilitating verification of compliance; in case of force majeure or casus fortuitus the DGA adopts contingency measures guaranteeing operational continuity in coordination with those institutions | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 9-A p.9 (EVID-252; txt PAGE 9; SOQ-30 print) |
| LB-003 | Ley de Zonas Francas, Art. 25: "LAS VENTAS O TRANSFERENCIAS DE BIENES Y SERVICIOS QUE SEAN NECESARIOS PARA LA ACTIVIDAD AUTORIZADA, REALIZADAS POR PERSONAS NATURALES O JURÍDICAS ESTABLECIDAS EN EL TERRITORIO ADUANERO NACIONAL, A UN USUARIO DE ZONA FRANCA O A UN DPA, ESTARÁN AFECTAS A UNA TASA DEL CERO POR CIENTO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS Y ADEMÁS, LES SERÁN APLICABLES LOS ARTÍCULOS 76 Y 77 DE LA LEY DE IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS. EN NINGÚN CASO SERÁN CONSIDERADOS COMO NECESARIOS PARA SU ACTIVIDAD, LOS BIENES Y SERVICIOS REFERIDOS EN EL INCISO ÚLTIMO DE LOS ARTÍCULOS 17 Y 19 DE ESTA LEY, SALVO LA EXCEPCIÓN ESTABLECIDA EN DICHAS DISPOSICIONES; EN CONSECUENCIA, DICHOS BIENES ESTARÁN AFECTOS A LA TASA ESTABLECIDA EN EL ARTÍCULO 54 DE LA LEY DE IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS." "EN LAS TRANSFERENCIAS DE BIENES Y SERVICIOS U OTRAS OPERACIONES QUE SE REALICEN ENTRE UN BENEFICIARIO DE ESTA LEY Y PERSONAS NATURALES O JURÍDICAS ESTABLECIDAS EN EL TERRITORIO ADUANERO NACIONAL, DEBERÁN APLICARSE LOS PRECIOS DE MERCADO. PARA TAL EFECTO, EL MINISTERIO DE HACIENDA, A TRAVÉS DE LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS, EN EL EJERCICIO DE SUS FACULTADES DE FISCALIZACIÓN, PODRÁ SOLICITAR A LOS CONTRIBUYENTES… QUE PRESENTEN INFORMACIÓN DETALLADA DE LAS OPERACIONES REALIZADAS Y CON BASE A ELLO, EFECTUAR LOS AJUSTES PERTINENTES EN LOS COSTOS, DEDUCCIONES, INGRESOS, UTILIDADES, PÉRDIDAS Y CUALQUIER OTRO CONCEPTO… MEDIANTE LA DETERMINACIÓN FEHACIENTE DEL PRECIO O VALOR DE LAS OPERACIONES… PARA LO CUAL SE APLICARÁ EL PROCEDIMIENTO ESTABLECIDO EN EL CÓDIGO TRIBUTARIO." "AQUELLAS OPERACIONES QUE REALICEN LOS BENEFICIARIOS DE ESTA LEY, FUERA DE LOS ALCANCES AUTORIZADOS EN EL RESPECTIVO ACUERDO, CAUSARÁN LOS DERECHOS E IMPUESTOS A LA IMPORTACIÓN, EL IMPUESTO SOBRE LA RENTA, LOS IMPUESTOS MUNICIPALES Y EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS." "LAS OPERACIONES DE TRANSFERENCIA DE DOMINIO AL TERRITORIO ADUANERO NACIONAL DE BIENES REALIZADAS POR UN COMERCIALIZADOR, CAUSARÁN EL IMPUESTO A LA TRANSFERENCIA… Y NO LES SERÁ APLICABLE LOS INCENTIVOS ESTABLECIDOS EN EL Art. 17 LITERALES d) Y e) Y Art. 19 LITERALES d) Y e), AMBOS DE LA PRESENTE LEY. LOS IMPUESTOS MUNICIPALES SE PAGARÁN EN LA PROPORCIÓN QUE RESULTE DE DIVIDIR SUS VENTAS AL MERCADO LOCAL SOBRE SUS VENTAS TOTALES, EN RELACIÓN A SU ACTIVO. (1) (6) (8)" | Sales or transfers of goods and services NECESSARY for the authorized activity, made by persons established in the national customs territory to a ZF usuario or a DPA, are subject to a ZERO PERCENT rate of IVA, and Arts. 76 and 77 of the IVA Law are additionally applicable to them. Goods and services referred to in the final inciso of Arts. 17 and 19 are NEVER considered necessary for the activity, save the exception established in those provisions; consequently those goods are subject to the rate established in Art. 54 of the IVA Law. Transfers of goods and services or other operations between a beneficiary and TAN-established persons must apply MARKET PRICES; MH through the DGII, in exercise of its fiscalization powers, may require detailed operation information from the taxpayers and, based on it, effect the pertinent adjustments to costs, deductions, income, utilities, losses and any other concept through reliable determination of the price or value of the operations, applying the procedure established in the Tax Code. Operations by beneficiaries OUTSIDE the scope authorized in the respective acuerdo cause import duties and taxes, ISR, municipal taxes and IVA. Transfers of dominion of goods into the national customs territory made by a COMERCIALIZADOR cause the transfer tax; the Art. 17 d)/e) and Art. 19 d)/e) incentives are NOT applicable to them; municipal taxes are paid in the proportion resulting from dividing local-market sales over total sales, in relation to assets | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 25 pp.29-30 (EVID-257; txt PAGE 29-30; SOQ-30 print; 34_ F-07-manual tipo-11 kin) |
| LB-004 | Ley de Zonas Francas, Art. 27: "PREVIA AUTORIZACIÓN DEL MINISTERIO DE ECONOMÍA, LAS MATERIAS PRIMAS E INSUMOS PODRÁN SER DESTINADOS AL CONSUMO DEFINITIVO EN EL TERRITORIO ADUANERO NACIONAL, PAGANDO LOS DERECHOS E IMPUESTOS DE IMPORTACIÓN SOBRE EL VALOR FACTURADO, EL QUE PARA EL CASO DE LAS MATERIAS PRIMAS E INSUMOS NO PODRÁ SER MENOR AL VALOR DEL COSTO, SEGURO Y FLETE (CIF POR SUS SIGLAS EN INGLÉS) PROPORCIONAL CONSIGNADO EN LA DECLARACIÓN DE MERCANCÍAS EN LA QUE FUERON INTRODUCIDOS DICHOS BIENES." "CUANDO SE TRATE DE DONACIONES AL GOBIERNO DE LA REPÚBLICA Y A INSTITUCIONES PÚBLICAS O PRIVADAS, SIN FINES DE LUCRO, DE CARÁCTER HUMANITARIO, EDUCATIVAS U OTROS SERVICIOS A LA COMUNIDAD, PODRÁ CONCEDERSE LA EXONERACIÓN DE IMPUESTOS, PREVIA LA CALIFICACIÓN DEL MINISTERIO DE ECONOMÍA Y LA EXONERACIÓN APROBADA POR LA ASAMBLEA LEGISLATIVA." "EL BENEFICIARIO PODRÁ VENDER AL MERCADO NACIONAL LOS DESECHOS Y DESPERDICIOS PROVENIENTES DE SU ACTIVIDAD, PAGANDO LOS DERECHOS E IMPUESTOS CORRESPONDIENTES, SOBRE EL VALOR EN ADUANA. IGUAL TRATAMIENTO SE APLICARÁ A LOS SUBPRODUCTOS Y PRODUCTOS DEFECTUOSOS." "CUANDO LOS DESPERDICIOS Y DESECHOS SEAN DESTINADOS A BOTADEROS DE DESECHOS SÓLIDOS AUTORIZADOS O A UNA EMPRESA DEBIDAMENTE ACREDITADA POR LAS AUTORIDADES DE MEDIO AMBIENTE PARA SU DESTRUCCIÓN, NO PAGARÁN NINGÚN DERECHO E IMPUESTO. LA DIRECCIÓN GENERAL DE ADUANAS EJERCERÁ EL CONTROL RESPECTIVO." "EN EL CASO DE LAS MERCANCÍAS QUE POR SUS CONDICIONES O ESTADO NO SEAN SUSCEPTIBLES DE APROVECHAMIENTO INDUSTRIAL O COMERCIAL, TALES COMO SUBPRODUCTOS Y PRODUCTOS DEFECTUOSOS, PODRÁN SER DESTRUIDAS PREVIA SOLICITUD DEL INTERESADO A LA AUTORIDAD ADUANERA, SEGÚN LO DISPUESTO EN EL CAUCA Y SU REGLAMENTO. LA DESTRUCCIÓN SERÁ REALIZADA POR CUENTA Y COSTO DEL INTERESADO, EN PRESENCIA DE LA AUTORIDAD ADUANERA, BAJO LOS PROCEDIMIENTOS ESTABLECIDOS EN EL CAUCA Y SU REGLAMENTO. (8)" | With PRIOR MINEC authorization, raw materials and inputs may be destined to definitive consumption in the national customs territory, paying import duties and taxes on the INVOICED VALUE — which for raw materials and inputs may NOT be below the proportional CIF (cost, insurance and freight) consigned in the goods declaration through which those goods were introduced. Donations to the Government and to public or private non-profit institutions of humanitarian, educational or community-service character may be granted tax EXONERATION with prior MINEC qualification and the exoneración approved by the Legislative Assembly. The beneficiary may sell to the national market the wastes and scraps (desechos y desperdicios) coming from its activity, paying the corresponding duties and taxes on the customs value; the SAME treatment applies to byproducts (subproductos) and defective products. When wastes and scraps are destined to AUTHORIZED solid-waste dumps or to a company duly accredited by the environmental authorities for their destruction, they pay NO duty or tax; the DGA exercises the respective control. Merchandise that by its conditions or state is not susceptible of industrial or commercial use — such as byproducts and defective products — may be DESTROYED upon prior request of the interested party to the customs authority per CAUCA and its Reglamento; destruction is carried out at the interested party's account and cost, in the presence of the customs authority, under the CAUCA procedures | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 27 pp.31-32 (EVID-257; txt PAGE 31-32; SOQ-30 print) |
| LB-005 | Ley de Servicios Internacionales, Art. 8: "Los servicios… deberán ser destinados a la exportación… entendiéndose como exportación, el servicio utilizado exclusivamente en el exterior o territorio extra-aduanal y prestado a un cliente domiciliado en el extranjero o territorio extra-aduanal; también se considera exportación el servicio a que se refiere el literal g), inciso primero, del artículo 5 de esta Ley, prestado a una persona natural o jurídica dedicada a la operación de líneas aéreas que realicen vuelos internacionales, independiente de su domicilio y donde utilice el servicio." "Los servicios contenidos en los literales a) y b), inciso primero, del artículo 5 de esta Ley, prestados por beneficiarios de esta Ley a una empresa beneficiada bajo el régimen de Zonas Francas o Depósito para Perfeccionamiento Activo, no causarán los impuestos correspondientes, incluyendo el impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, siempre y cuando dichos servicios estén directamente vinculados con la exportación de bienes, para lo cual deberá emitir factura de consumidor final consignando el nombre del prestatario del servicio y demás requisitos establecidos en el Código Tributario." "La prestación de servicios al mercado nacional sólo podrá realizarse a contribuyentes debidamente inscritos en el Registro de Contribuyentes del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios. Dichas prestaciones causarán el Impuesto sobre la Renta, el de Transferencia de Bienes Muebles y a la Prestación de Servicios e impuestos municipales correspondientes; el prestador de servicios adquiere la calidad de sujeto pasivo respecto de todos los tributos que se generen por dichas transacciones." [W19 T3 — the following incisos are carried at their POST-277-2013 letter set (80_ Art. 8; the pre-reform set read "a), b), c), d), e), h) y j)" — h) REMOVED by D.L. 277-2013; EVID-383):] "En el caso de prestaciones de servicios al mercado nacional, el prestatario de los servicios, sea persona jurídica o natural, titular de empresas que paguen o acrediten sumas correspondientes a los servicios establecidos en los literales a), b), c), d), e) y j) del inciso primero del artículo 5 de esta ley, están obligados a retener el 1.5% en concepto de anticipo del impuesto sobre la renta, el cual deberá ser enterado dentro del plazo estipulado para las retenciones en la ley del impuesto sobre la renta; en consecuencia, dichas rentas no estarán sujetas al sistema de pago o anticipo a cuenta previsto en el Código Tributario. El incumplimiento a la retención establecida en este inciso, hará incurrir al sujeto pasivo en las sanciones establecidas en el Código Tributario.(1)" "En el caso de prestaciones de servicios al mercado nacional, todos los contribuyentes del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, independientemente de su clasificación, deberán retener el 1% sobre el valor del servicio recibido de los servicios contemplados en los literales a), b), c), d), e) y j) del inciso primero del artículo 5 de la presente ley, en concepto de anticipo de dicho impuesto. Lo no dispuesto en el presente inciso, se estará a lo establecido en el Código Tributario.(1)" "EN EL CASO DE LAS ACTIVIDADES CONTEMPLADAS EN LAS LETRAS a), b), c), d), e) y j) DEL INCISO PRIMERO DEL ARTÍCULO 5 DE LA PRESENTE LEY, PODRÁN DESTINAR PARTE DE SUS SERVICIOS AL MERCADO NACIONAL.(1)" "La introducción de bienes al mercado nacional derivada de las operaciones de distribución internacional y operaciones logísticas, se consideran importación definitiva, en la que el importador asume la calidad de sujeto pasivo respecto de todos los tributos que genere la misma, cuando proceda." | Services must be destined to exportation; exportation means the service used EXCLUSIVELY abroad or in extra-aduanal territory AND provided to a client domiciled abroad or in extra-aduanal territory; the Art. 5 g) aircraft service provided to a person operating international-flight airlines is ALSO exportation regardless of domicile and where the service is used. Art. 5 a) and b) services provided by LSI beneficiaries to an enterprise benefited under the zonas francas or DPA regime cause NO corresponding taxes, INCLUDING IVA, provided those services are DIRECTLY linked to the exportation of goods — for which a FACTURA DE CONSUMIDOR FINAL (final-consumer invoice) must be issued consigning the name of the prestatario (service recipient) and the other Tax Code requirements. National-market services may be provided ONLY to contribuyentes duly registered in the IVA Register; they cause ISR, IVA and the corresponding municipal taxes, the prestador (service provider) acquiring sujeto pasivo status for all tributes generated by those transactions. For national-market services, the prestatario — legal persons or natural-person enterprise holders paying or crediting sums for letters a), b), c), d), e), h) and j) services — is OBLIGED to retain 1.5% as ISR anticipo, remitted within the deadline stipulated for retentions in the ISR Law; consequently those rentas are NOT subject to the payment or anticipo-a-cuenta system provided in the Tax Code; breach of this retention incurs the Tax Code sanctions. For national-market services, ALL IVA contribuyentes regardless of classification must retain 1% of the value of the received service (letters a)-e), h), j)) as anticipo of that tax; matters not provided here follow the Tax Code. The introduction of goods into the national market derived from international distribution and logistics operations is considered DEFINITIVE IMPORTATION, in which the importer assumes sujeto pasivo status for all tributes it generates, when applicable | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 8 pp.7-8 (EVID-383; 80_ txt PAGE 7-8 — incisos 3º-6º reformed by 277-2013, re-verbatim W19) |
| LB-006 | Ley de Servicios Internacionales, Art. 9: "En las transferencias de bienes, servicios u otras operaciones que se realicen entre un beneficiario de la presente Ley y personas naturales o jurídicas establecidas en el territorio aduanero nacional, deberá aplicarse los precios de mercado. Para efecto del inciso anterior, el Ministerio de Hacienda, a través de la Dirección General de Impuestos Internos, en el ejercicio de sus facultades de fiscalización, podrá solicitar a los contribuyentes mencionados en este artículo, que presenten información detallada de las operaciones realizadas y con base a ello, efectuar los ajustes pertinentes en los costos, deducciones, ingresos, utilidades, pérdidas y cualquier otro concepto de las operaciones declaradas por los contribuyentes, mediante la determinación fehaciente del precio o valor de las operaciones en las cuales el contribuyente haya adquirido o enajenado bienes o servicios, para lo cual se aplicará el procedimiento establecido en el Código Tributario." | Transfers of goods, services or other operations between an LSI beneficiary and persons established in the national customs territory must apply MARKET PRICES; for that purpose MH through the DGII, in exercise of its fiscalization powers, may require those taxpayers to present detailed operation information and, based on it, effect the pertinent adjustments to costs, deductions, income, utilities, losses and any other declared concept, through reliable determination of the price or value of the operations, applying the procedure established in the Tax Code | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 9 p.8 (EVID-261; 80_ txt PAGE 8 — unchanged; 14_ re-keyed W19) |
| LB-007 | Ley de Servicios Internacionales, Art. 26 (final block): "Las ventas o transferencias de bienes y servicios que se utilicen en la actividad beneficiada, realizadas por personas naturales o jurídicas establecidas en el territorio aduanero nacional, a un usuario directo de parque de servicios o centro de servicios, se considerarán como operaciones de exportación definitiva, en consecuencia serán aplicables los artículos 75, 76 y 77 de la Ley de Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios. En ningún caso serán considerados como necesarios para el desarrollo de su actividad, los bienes y servicios contemplados en el inciso segundo del literal a), de los artículos 21 y 25 de la presente ley; en consecuencia, tales bienes y servicios estarán afectos con la tasa establecida en el artículo 54 de la Ley de Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios." "Para los efectos de lo establecido en el inciso anterior, se entenderá que un bien o servicio es utilizado en la actividad beneficiada cuando se destine a los fines propios de la actividad beneficiada." | Sales or transfers of goods and services USED in the benefited activity, made by persons established in the national customs territory to a usuario directo of a services park or a services center, are considered DEFINITIVE EXPORTATION operations — consequently Arts. 75, 76 and 77 of the IVA Law are applicable. Goods and services contemplated in the second inciso of literal a) of Arts. 21 and 25 are NEVER considered necessary for the development of the activity; consequently those goods and services are subject to the rate established in Art. 54 of the IVA Law. For the preceding effects, a good or service is USED IN THE BENEFITED ACTIVITY when destined to the own ends of the benefited activity | `sv/sources/80_Ley_Servicios_Internacionales_consolidada_DL431_DL277.pdf` | Art. 26 final block pp.18-19 (EVID-263; 80_ txt PAGE 18-19 — unchanged; 14_ re-keyed W19) |
| LB-008 | Ley de Simplificación Aduanera, Art. 11-A (requirement h) of the simplified-withdrawal authorization): "h) Presentar las respectivas solvencias de pago del Instituto Salvadoreño del Seguro Social y de las diferentes Administradoras de Fondos de Pensiones, de las cotizaciones correspondientes a los treinta días anteriores, a aquel en el que se presente la solicitud;" | h) Present the respective payment solvencies of the ISSS and the different Pension Fund Administrators (AFPs), for the contributions corresponding to the THIRTY DAYS prior to that in which the application is presented (the SS-solvencia kin of this file's gate; the simplified-withdrawal procedure itself is owned by `06_customs-declarations.md` by id) | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 11-A h) p.9 (EVID-270; txt PAGE 9; SOQ-30 print) |

## 3. Functional Requirements

### 3.1 Internación chassis — ZF/DPA production into TAN (12_ Art. 3 final block)

- **SV-SPE-FR-082:** The system shall route every sale of ZF/DPA-produced
  goods into the national customs territory by an authorized producer as an
  *internación* record: the producing beneficiary interns the goods paying
  import duties and taxes on the *valor en aduana* (customs value) ONLY for
  the NON-NATIONAL component incorporated into the final product, and
  national-market sales of SUBPRODUCTOS take the SAME treatment — the duty
  base is the non-national component, never the full product value; each
  internación links to the Task-1 regime profile (SV-SPE-FR-001/003 by id),
  rides the SS-solvency gate (FR-102) and declares through the customs
  surface of `06_customs-declarations.md` (by id). The METHOD to determine
  the non-national component beyond the FR-083 cost rule is corpus-silent
  (EVID-252 doubt) — no mechanics invented, OQ-2 config slots only.
  (LB-001; EVID-252)
- **SV-SPE-FR-083:** The system shall implement the verbatim cost rule for
  transformed goods: for merchandise that has undergone transformation, the
  *valor en aduana* MUST contain the COST of *materias primas* (raw
  materials) AND *gastos indirectos de fabricación* (indirect manufacturing
  costs); and the commercial, tax and accounting support documents of the
  transactions must REFLECT the national value added by the
  transformation, elaboration and repair processes — the value-composition
  check feeds the FR-082 base and consumes the cost registers of
  `07_obligations-reporting-sanctions.md` (12_ Art. 28 p kin, by id).
  (LB-001; EVID-252)
- **SV-SPE-FR-084:** The system shall split the comercializador internación
  base by goods origin: general rule — comercializadores making TAN sales
  intern the goods paying duties on the FULL *valor en aduana*; producer-
  sourced exception — for goods acquired from a producer established under
  the law, duties compute on the good's *valor en aduana* EXCLUDING the
  value of the NATIONAL component incorporated into the final product,
  ALWAYS AND ONLY WHEN the comercializador DEMONSTRATES the value of those
  components (demonstration-evidence link on the record; no demonstration
  ⇒ the full base stands).
  (LB-001; EVID-252)
- **SV-SPE-FR-085:** The system shall apply the NMF (Nación Más Favorecida,
  most-favoured-nation) tariff as the default internación tariff, with the
  TLC-origin exception: comercializadores interning goods originating in
  third countries with which a free-trade agreement exists may apply the
  PREFERENTIAL treatment provided they demonstrate to the customs authority
  that the goods (i) underwent NO transformation in the country, (ii)
  remained AT ALL TIMES under customs control, and (iii) meet the remaining
  preferential-tariff requirements — three evidence flags gating the
  preferential rate selection.
  (LB-001; EVID-252)
- **SV-SPE-FR-086:** The system shall enforce the minimum-value floor as an
  inverting validation gate on every internación: the declared value of the
  interned goods may NEVER be lower than the value at which the goods
  ENTERED the zona franca or DPA, and for *materias primas e insumos*
  (raw materials and inputs) it may NEVER be lower than the *valor en
  aduana* established in the introducing goods declaration (the DM value —
  consumed from `04`/`06` by id) — a declared value below either floor
  blocks the internación with a floor-mismatch flag (never silently
  corrected).
  (LB-001; EVID-252)

### 3.2 TAN→ZF/DPA sales — the 0% IVA route (12_ Art. 25)

- **SV-SPE-FR-087:** The system shall route sales or transfers of goods
  and services NECESSARY for the authorized activity, made by
  TAN-established persons to a ZF usuario or a DPA, at the 0% IVA rate
  with Ley IVA Arts. 76 and 77 applicable — a dedicated fiscal position
  (route `tan_to_zf_iva_0`) selecting a dated 0% *account.tax* row and
  stamping the Art. 76/77 applicability flag; the refund/credit
  COMPUTATION those articles govern is the IVA-core taxation wave's by
  pointer (never restated here); the purchase surfaces the F-07 annex-3
  tipo-11 bucket consumed BY ID from fiscal-reporting/03 (SV-FREP-FR-073 —
  12_ Art. 25 is its printed authority; 34_ manual kin); the route rides
  the benefit-state gate (SV-SPE-FR-015 by id — suspended/revoked profiles
  never resolve this route) and the SS-solvency gate (FR-102).
  (LB-003; EVID-257)
- **SV-SPE-FR-088:** The system shall implement the not-necessary
  inversion on the FR-087 fiscal position: goods and services of the
  exception lists in the final incisos of 12_ Arts. 17 and 19 (consumed
  from `02_zf-exemption-schedules.md` SV-SPE-FR-036 by id, including its
  acuerdo-recorded-exception escape) are NEVER considered necessary for
  the activity — consequently they route at the FULL rate of Ley IVA
  Art. 54 (13%, computation by pointer to the IVA-core wave), and no 0%
  row or annex-3 tipo-11 bucket may ever attach to them.
  (LB-003; EVID-257)
- **SV-SPE-FR-089:** The system shall record the market-price rule on
  every transfer of goods, services or other operations between a
  beneficiary and TAN-established persons: MARKET PRICES must be applied,
  and the DGII's fiscalization power — demanding detailed operation
  information and effecting adjustments to costs, deductions, income,
  utilities, losses and any other declared concept through reliable
  determination of price or value under the Código Tributario procedure —
  is mirrored as an informational price-reference and adjustment-record
  surface ONLY (zero transfer-pricing mechanics invented; the CT
  procedure is owned by the CT text, cross-topic).
  (LB-003; EVID-257)
- **SV-SPE-FR-090:** The system shall implement the out-of-agreement guard
  as a full-tax routing flag: operations by beneficiaries OUTSIDE the
  scope authorized in the respective *acuerdo* cause import duties and
  taxes, ISR, municipal taxes AND IVA — the flag derives from the
  activity-admission config of Task 1 (SV-SPE-FR-006..009 by id: goods or
  services outside the admitted SAC scope/letters route full-tax) and
  cooperates with the benefit-state gate (SV-SPE-FR-015 by id).
  (LB-003; EVID-257)
- **SV-SPE-FR-091:** The system shall route transfers of dominion of goods
  into the national customs territory by a *comercializador* through the
  full IVA route (the transfer tax IS caused — standard-rate fiscal
  position, no 0%/exempt row attachable), consuming the
  incentive-exclusion and municipal-proration computation BY ID from
  `02_zf-exemption-schedules.md` (SV-SPE-FR-041: TAN-sale income never
  enters the exemption rows; municipal taxes prorated local/total sales
  over assets) — never restated here.
  (LB-003; EVID-257)

### 3.3 B2B intra-regime route (12_ Art. 3)

- **SV-SPE-FR-092:** The system shall route sales and purchases of goods
  NECESSARY for the authorized activity between beneficiaries of the
  regime through the no-tax route: NO *derechos* (customs duties) and NO
  taxes whatsoever are caused, INCLUDING IVA (an exempt/no-tax fiscal
  position on both legs, both counterparties beneficiaries per their
  profiles — SV-SPE-FR-001/003 by id); the DPA condition rides the
  customs-clock invariant of `04_customs-clocks.md` by id
  (SV-SPE-FR-065/067): the route is valid only WITHIN the legal term of
  the corresponding customs regime, and NO transfer of merchandise at any
  title is ever a reason to extend that term.
  (LB-001; EVID-252)

### 3.4 Materia-prima TAN consumption + disposition paths (12_ Art. 27)

- **SV-SPE-FR-093:** The system shall route the definitive-consumption
  destination of *materias primas e insumos* into TAN (prior MINEC
  authorization recorded on the destination): import duties and taxes
  compute on the VALOR FACTURADO (invoiced value), which may NEVER be
  lower than the PROPORTIONAL CIF consigned in the goods declaration
  through which the goods were introduced — the proportional-CIF floor
  reconciles against the introducing DM consumed from `04`/`06` by id
  (mismatch blocks the destination).
  (LB-004; EVID-257)
- **SV-SPE-FR-094:** The system shall implement the ZF/DPA disposition
  paths for *desechos y desperdicios* (wastes and scraps), *subproductos*
  (byproducts) and *productos defectuosos* (defective products) as four
  recorded routes: i) SALE to the national market — duties and taxes on
  the VALOR EN ADUANA (same treatment for subproductos and defectuosos);
  ii) destination to AUTHORIZED solid-waste *botaderos* (dumps) or an
  environment-accredited destruction company — NO duty or tax, with the
  DGA-control note; iii) CAUCA DESTRUCTION for merchandise not
  susceptible of industrial or commercial use — prior request to the
  customs authority, executed at the interested party's account and cost
  in the authority's presence (procedure pointer to CAUCA, no invented
  mechanics); iv) DONATIONS to the Government or public/private non-profit
  humanitarian, educational or community-service institutions —
  exonerated with prior MINEC *calificación* AND the exoneración approved
  by the Asamblea Legislativa (both references required). These are the
  12_ Art. 27 ZF/DPA paths, DISTINCT from the LSI 80_ Art. 45 residuales
  paths owned by `04_customs-clocks.md` (SV-SPE-FR-079 by id — different
  instrument, different regime, never merged).
  (LB-004; EVID-257)

### 3.5 LSI export test + local-market routing (80_ Art. 8)

- **SV-SPE-FR-095:** The system shall implement the LSI export test as the
  routing predicate for every LSI service: a service is EXPORTATION when
  it is used EXCLUSIVELY abroad or in extra-aduanal territory AND is
  provided to a client DOMICILED abroad or in extra-aduanal territory —
  both limbs recorded (use-location + client-domicile stamps on the
  service move); the aeronáutico special grade of Art. 5 g) (international
  -flight airlines regardless of domicile and use) is consumed from Task
  1's letter predicates BY ID (SV-SPE-FR-008), never restated; passing the
  test routes the export treatment (the IVA export computation of Ley IVA
  Arts. 75-77 = IVA-core wave by pointer; the export document pairing =
  e-invoicing by id), while the local-market caps that operationalize the
  export destination are `03_lsi-regime.md`'s BY ID (SV-SPE-FR-048/050).
  (LB-005; EVID-261)
- **SV-SPE-FR-096:** The system shall route LSI local-market services with
  two gates: i) the RECEPTOR gate — national-market services may be
  provided ONLY to *contribuyentes* duly registered in the IVA Register
  (registration validation on the customer before the sale routes); and
  ii) the full-local-tax route — such services cause ISR, IVA and the
  corresponding municipal taxes, with the *prestador* acquiring SUJETO
  PASIVO status for ALL tributes generated by those transactions
  (full-tax fiscal position, distinct from every export route of
  FR-095/FR-099/FR-101).
  (LB-005; EVID-261)

### 3.6 LSI dual-retention pair (80_ Art. 8)

- **SV-SPE-FR-097:** The system shall carry the LSI 1.5% ISR-anticipo
  retention as applicability/trigger rows owned HERE with the computation
  engine consumed from `taxation/04_isr-withholding.md` BY ID
  (SV-TAX-FR-121 family: moment-of-payment/*acreditamiento* mechanics,
  remittance per the Ley ISR retention deadline): on national-market
  services of letters **a), b), c), d), e) and j)** (W19 T3: D.L. 277-2013
  REMOVED h) — pre-reform rows dated to ~19-feb-2013 carry a), b), c), d),
  e), h), j), retained as their own dated rows), the PRESTATARIO
  (service recipient — legal persons or natural-person enterprise holders)
  paying or crediting sums MUST retain 1.5% as ISR *anticipo*; and the
  SUPPRESSION FLAG rides the row: such rentas are NOT subject to the CT
  payment/anticipo-a-cuenta system (the CT anticipo rows are suppressed
  for this income — 03's CT-158-II carve-out kin SV-SPE-FR-059/060 by
  id); the 1.5% value is the dated print, provenance now 80_ Art. 8
  (reformed 277-2013; SOQ-37 cross-check OQ-1);
  the semestral dictamen verification of this retention is consumed BY ID
  from `03_lsi-regime.md` (SV-SPE-FR-053 item e.4 + FR-054 anexo b).
  (LB-005; EVID-261; EVID-383 W19 T3)
- **SV-SPE-FR-098:** The system shall carry the LSI 1% IVA-anticipo
  retention as applicability/trigger rows owned HERE with the same
  engine consumption (SV-TAX-FR-121..129 by id): on national-market
  services of letters **a), b), c), d), e) and j)** (W19 T3: h) REMOVED
  by D.L. 277-2013 — same dated-row split as FR-097), ALL IVA
  contribuyentes regardless of classification receiving the service MUST
  retain 1% of the VALUE OF THE SERVICE RECEIVED as IVA *anticipo* (this
  file owns the trigger predicate and the 1% dated row; the retention
  DOCUMENT is the e-invoicing CRE consumed BY ID — SV-EINV-FR-035,
  CAT-006 code 22 "Retención IVA 1%"); the 1% value is the dated print
  (provenance 80_ Art. 8 reformed 277-2013; SOQ-37 cross-check OQ-1);
  dictamen verification hook as in FR-097.
  (LB-005; EVID-261; EVID-383 W19 T3)

### 3.7 Cross-regime services — the FCF rule (80_ Art. 8 inc. 2)

- **SV-SPE-FR-099:** The system shall route Art. 5 a) (distribución
  internacional) and b) (logística internacional) services provided by LSI
  beneficiaries to an enterprise benefited under the zonas francas or DPA
  regime through the cross-regime no-tax route: NO corresponding taxes are
  caused, INCLUDING IVA, ALWAYS AND ONLY WHEN the services are DIRECTLY
  linked to the EXPORTATION of goods (export-link verification predicate
  on the service record — linking reference to the export operation);
  documentation is the FACTURA DE CONSUMIDOR FINAL consigning the NAME OF
  THE PRESTATARIO plus the other Código Tributario requirements — the
  FCF/FE document surface consumed BY ID from e-invoicing
  (SV-EINV-FR-001 type 01; SV-EINV-FR-019/020/021 FE rules: IVA-inclusive
  pricing model, receptor identification) with the prestatario-naming
  requirement as a routing-level stamp; this FR is the S6
  IVA-tercerización-FCF-exento pointer's authority (cross-wave note —
  consumed there by id when that wave lands).
  (LB-005; EVID-261)

### 3.8 LSI goods interface (80_ Arts. 8/26)

- **SV-SPE-FR-100:** The system shall route the introduction of goods into
  the national market derived from international-distribution and
  international-logistics operations as IMPORTACIÓN DEFINITIVA: the
  importer assumes SUJETO PASIVO status for all tributes the operation
  generates, when applicable — the route targets the importación-definitiva
  destinación of `04_customs-clocks.md` BY ID (SV-SPE-FR-075 menu) and the
  DUCA import surface of `06` by id.
  (LB-005; EVID-261)
- **SV-SPE-FR-101:** The system shall route sales or transfers of goods
  and services USED in the benefited activity, made by TAN-established
  persons to a usuario directo of a parque de servicios or a centro de
  servicios, as OPERACIONES DE EXPORTACIÓN DEFINITIVA with Ley IVA
  Arts. 75, 76 AND 77 applicable — a dedicated fiscal position (route
  `tan_to_lsi_export_definitiva`) that is a DISTINCT family from the ZF
  0%+Arts. 76/77 route of FR-087 (SV-SPE-FR-087): the config catalog
  enforces route-family exclusivity by regime (ZF/DPA profiles resolve
  FR-087's route; parque/centro profiles resolve this route; no shared or
  parameterized row between them — the file's governing
  regime-distinctness invariant; Art. 75 is in the LSI citation set and
  NOT in the ZF one, as printed). The not-necessary inversion applies:
  goods and services of the second incisos of Art. 21 a) and Art. 25 a)
  (the LSI exception lists — usuario-directo/centro kin of `02`'s
  exception-goods gate, SV-SPE-FR-036 pattern) are NEVER considered
  necessary and route at the Ley IVA Art. 54 rate; and the statutory
  definition is recorded verbatim: a good or service is USED IN THE
  BENEFITED ACTIVITY when destined to the own ends of the benefited
  activity.
  (LB-007; EVID-263)

### 3.9 SS-solvency gate (12_ Arts. 3/9-A; 74_ Art. 11-A kin)

- **SV-SPE-FR-102:** The system shall gate every regime sale of goods (the
  FR-082/FR-084 internaciones, the FR-087 TAN→ZF/DPA deliveries and the
  B2B route of FR-092) on the SS-solvency check: the beneficiary must
  PROVE to the customs authority solvency in payment to the ISSS and the
  AFPs — of the *cotizaciones* and retentions effected on its workers AND
  the employer (*patrono*) contributions — corresponding to the MONTH NEXT
  PRIOR to the sale month; the verification is by ELECTRONIC MEANS per
  Art. 9-A (DGA-established network specifications and online-consultation
  mechanisms — recorded as an external-interface assumption with the
  force-majeure contingency note); the solvency input consumes the payroll
  SS records BY ID (SV-PAY-FR-066/072 cotización computation;
  SV-PAY-FR-093 SIP payment states): an arrear month for the prior month
  blocks the sale routes with a cure path (the gate reopens when the
  payment records clear); the 74_ Art. 11-A h) kin is recorded —
  simplified-withdrawal solvencias cover the thirty days prior to the
  application (the withdrawal PROCEDURE itself is
  `06_customs-declarations.md`'s by id).
  (LB-001; LB-002; LB-008; EVID-252/270)

## 4. Data Model

Layer semantics: all entities are Odoo-native routing/config/ledger rows on
the Task-1 regime profile (fiscal positions, dated account.tax-selection
rows, internación records, retention-applicability rows, gate records) —
every entity lives in the client (wave default `odoo`; see §5). Rates and
base rules are code-text values as printed (SOQ-30 watch), stored as dated
rows with instrument provenance, never constants; the DGA/DGII electronic
verifications are external interfaces recorded as results. CSV sidecar
evaluated per plan: the route catalog (≈8 rows) and the retention
applicability set (7 letters × 2 retentions) are small config sets — §4
config rows suffice and NO sidecar ships (default none; judgment noted in
the task report).

**Internación record (l10n_sv_special_regime.internacion):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.internacion | profile · kind | m2o · select | T1 regime profile; productor_autorizado · comercializador (subproductos ride productor) | FR-082, FR-084 |
| l10n_sv_special_regime.internacion | valor_en_aduana · non_national_component · base | monetary ×3 | duty base = non-national component (productor) / full value minus demonstrated national (comercializador-producer-sourced) / full value | FR-082, FR-084 |
| l10n_sv_special_regime.internacion | cost_rule_conform | computed | transformed goods: valor en aduana contains materias primas + GIF (FR-083); national-value-added reflected on support docs (07 registers by id) | FR-083 |
| l10n_sv_special_regime.internacion | national_component_proof | char/m2o | demonstration evidence link (comercializador exception; absent ⇒ full base) | FR-084 |
| l10n_sv_special_regime.internacion | tariff · tlc_origin_flags | select · boolean ×3 | NMF default; preferential iff no-transformation + permanent-customs-control + other-requirements flags | FR-085 |
| l10n_sv_special_regime.internacion | entry_value_floor · dm_cif_floor · declared_value | monetary ×3 | declared ≥ entry value; materias primas ≥ DM valor en aduana (CIF) — mismatch flag blocks | FR-086 |
| l10n_sv_special_regime.internacion | ss_gate_ref · dm_ref | m2o ×2 | FR-102 gate record; declaring DM (06 by id) | FR-082, FR-102 |

**Routing config (l10n_sv_special_regime.fiscal_route):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.fiscal_route | route | select | tan_to_zf_iva_0 (0% + Ley IVA 76/77) · tan_to_lsi_export_definitiva (Arts. 75-77) · b2b_beneficiaries_no_tax · comercializador_tan_full_tax · lsi_local_market_full_tax · lsi_cross_regime_exempt (FCF) · lsi_goods_import_definitiva · out_of_agreement_full_tax | FR-087..101 |
| l10n_sv_special_regime.fiscal_route | regime_family | select | zf_dpa · lsi · cross_regime — route-family exclusivity enforced (zf_dpa profiles never resolve lsi routes and vice versa — FR-101 invariant) | FR-087, FR-101 |
| l10n_sv_special_regime.fiscal_route | necessity_gate | m2o config | exception-list check (02 FR-036 rows by id; LSI Arts. 21/25 a) inc. 2 kin) — fail ⇒ Art. 54 full rate | FR-088, FR-101 |
| l10n_sv_special_regime.fiscal_route | annex3_tipo_11 | boolean | TRUE only on tan_to_zf_iva_0 — feeds SV-FREP-FR-073 by id | FR-087 |
| l10n_sv_special_regime.fiscal_route | valid_from · valid_to · provenance | date · date · char | 12_/80_ article as printed (SOQ-30; W19 T3 14_→80_); snapshot-on-write per D15 | FR-087..101 |

**LSI retention applicability (l10n_sv_special_regime.retention_rule):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.retention_rule | kind · letters | select · m2m | isr_anticipo_1_5 · iva_anticipo_1 — letters a,b,c,d,e,j (80_ Art. 8 as reformed 277-2013, W19 T3); PRE-reform dated rows (to ~19-feb-2013): a,b,c,d,e,h,j; SOQ-37/OQ-1 | FR-097, FR-098 |
| l10n_sv_special_regime.retention_rule | ct_anticipo_suppressed | boolean | TRUE on isr rows — rentas outside the CT pago/anticipo-a-cuenta system | FR-097 |
| l10n_sv_special_regime.retention_rule | engine_ref · document_ref | char | SV-TAX-FR-121..129 (computation by id); CRE document SV-EINV-FR-035 (CAT-006 code 22) | FR-097, FR-098 |
| l10n_sv_special_regime.retention_rule | valid_from · valid_to · provenance | date · date · char | 80_ Art. 8 (values printed 2007; letter set reformed 277-2013 — W19 T3) | FR-097, FR-098 |

**Export-test stamp + market-price + solvency-gate records (l10n_sv_special_regime.\*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.export_test | use_location · client_domicile · result | select ×2 · computed | exclusively abroad/extra-aduanal + client abroad/extra-aduanal ⇒ export route (g) special grade via FR-008 by id | FR-095 |
| l10n_sv_special_regime.export_test | export_link_ref | m2o/char | cross-regime services: direct link to the goods-export operation | FR-099 |
| l10n_sv_special_regime.market_price_record | operation_ref · adjustment | m2o · fields | market-price reference + DGII adjustment record (informational; CT procedure pointer) | FR-089 |
| l10n_sv_special_regime.ss_solvency_gate | month · scope · result | date · select · computed | prior-month ISSS+AFP cotizaciones/retenciones + patronal aportaciones; source = payroll records by id (SV-PAY-FR-066/072/093); blocked/cured states | FR-102 |
| l10n_sv_special_regime.ss_solvency_gate | verification_means · contingency_note | char | electronic per Art. 9-A (DGA networks, online consultation — external interface); force-majeure contingency | FR-102 |
| l10n_sv_special_regime.materia_consumption | minec_authorization · valor_facturado · cif_floor | char · monetary ×2 | Art. 27 destination; proportional-CIF reconciliation vs introducing DM | FR-093 |
| l10n_sv_special_regime.disposition_path | kind · references | select · char | nacional_valor_en_aduana · botadero_autorizado_free · caucar_destruction · donacion (MINEC + Asamblea) — ZF/DPA Art. 27 paths, distinct from LSI FR-079 | FR-094 |

## 5. Odoo Mapping

Layer semantics for this wave: the TAN/IVA interface is Odoo-native
routing (fiscal positions + dated account.tax-selection rows on the regime
profile, internación/gate ledger records) — every FR maps `odoo`; no SaaS
rows are introduced (no DTE generation/transmission is owned here: the FCF
and CRE surfaces are consumed from the e-invoicing wave as read-only
document references, and the Ley IVA 54/75-77 computations are the
IVA-core wave's by pointer). The DGA online SS-solvency consultation
(Art. 9-A) and the DGII adjustment procedure are external authorities: the
model records results/references, it does not emulate them
(external-interface assumption noted on FR-102/FR-089). Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is required
by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-082 | odoo | l10n_sv_special_regime.internacion | kind/base/non_national_component | duty base = non-national component ONLY; method beyond cost rule = OQ-2 config slots; profile link FR-003 by id |
| FR-083 | odoo | l10n_sv_special_regime.internacion | cost_rule_conform | verbatim rule: valor en aduana ⊇ materias primas + GIF; support docs reflect national value added (07 registers by id) |
| FR-084 | odoo | l10n_sv_special_regime.internacion | national_component_proof | comercializador: full base default; producer-sourced exception only with demonstrated national component |
| FR-085 | odoo | l10n_sv_special_regime.internacion | tariff/tlc_origin_flags | NMF default; preferential gated on 3 demonstration flags |
| FR-086 | odoo | l10n_sv_special_regime.internacion | entry_value_floor/dm_cif_floor | two-floor gate; materias-primas floor = DM valor en aduana (04/06 by id); mismatch blocks, never corrects |
| FR-087 | odoo | account.fiscal.position + account.tax | route tan_to_zf_iva_0 (0% dated row + Art. 76/77 flag) | THE ZF route; annex-3 tipo-11 = SV-FREP-FR-073 by id (12_ Art. 25 = printed authority; 34_ kin); 76/77 computation = IVA-core pointer; benefit-state gate FR-015 by id |
| FR-088 | odoo | l10n_sv_special_regime.fiscal_route | necessity_gate | exception lists consumed from 02 FR-036 by id; fail ⇒ Ley IVA Art. 54 full rate (IVA-core pointer); no tipo-11 attachment |
| FR-089 | odoo | l10n_sv_special_regime.market_price_record | operation_ref/adjustment | informational surface; DGII adjustment powers + CT procedure pointer — zero TP mechanics invented |
| FR-090 | odoo | l10n_sv_special_regime.fiscal_route | out_of_agreement_full_tax | derives from admission config (FR-006..009 by id); full duties+ISR+municipal+IVA |
| FR-091 | odoo | account.fiscal.position | comercializador_tan_full_tax | transfer tax caused; incentive exclusion + municipal proration = 02 FR-041 by id (never restated) |
| FR-092 | odoo | account.fiscal.position | b2b_beneficiaries_no_tax | no derechos, no taxes incl. IVA; DPA condition rides 04 FR-065/067 by id (term never extended by transfer) |
| FR-093 | odoo | l10n_sv_special_regime.materia_consumption | minec_authorization/valor_facturado/cif_floor | prior-MINEC-auth destination; floor = proportional CIF of introducing DM (04/06 by id) |
| FR-094 | odoo | l10n_sv_special_regime.disposition_path | 4 ZF/DPA paths | valor en aduana / botaderos free / CAUCA destruction / donations MINEC+Asamblea; DISTINCT from LSI FR-079 (80_ Art. 45) — never merged |
| FR-095 | odoo | l10n_sv_special_regime.export_test | use_location/client_domicile/result | two-limb test; g) special grade via 01 FR-008 by id; caps = 03 FR-048/050 by id; export computation = IVA-core pointer |
| FR-096 | odoo | account.fiscal.position + res.partner gate | lsi_local_market_full_tax | receptor must be IVA-registered; prestador = sujeto pasivo of all tributes |
| FR-097 | odoo | l10n_sv_special_regime.retention_rule + account.tax | isr_anticipo_1_5 rows | applicability HERE; engine = SV-TAX-FR-121..129 by id; CT-anticipo suppression flag; value printed 2007, letters reformed 277-2013 (W19 T3; OQ-1); dictamen hook = 03 FR-053/054 by id |
| FR-098 | odoo | l10n_sv_special_regime.retention_rule + account.tax | iva_anticipo_1 rows | all IVA contribuyentes on receiving side; CRE doc = SV-EINV-FR-035 by id (CAT-006 22); value printed 2007, letters reformed 277-2013 (W19 T3; OQ-1) |
| FR-099 | odoo | account.fiscal.position | lsi_cross_regime_exempt | a)/b) to ZF/DPA, directly export-linked; FCF naming prestatario = SV-EINV-FR-019/020/021 by id; S6 pointer authority note |
| FR-100 | odoo | l10n_sv_special_regime.fiscal_route | lsi_goods_import_definitiva | importer = sujeto pasivo; destinación menu = 04 FR-075 by id; DUCA surface = 06 by id |
| FR-101 | odoo | account.fiscal.position | tan_to_lsi_export_definitiva | Arts. 75-77 (Art. 75 in LSI set, NOT in ZF's — as printed); route-family exclusivity vs FR-087 = THE invariant; LSI exception lists ⇒ Art. 54 rate; "utilizado en la actividad beneficiada" recorded |
| FR-102 | odoo | l10n_sv_special_regime.ss_solvency_gate | month/scope/result | prior-month ISSS+AFP incl. patronal; electronic per Art. 9-A (external interface — DGA networks/online consultation); payroll feed SV-PAY-FR-066/072/093 by id; cure path; 74_ 11-A h) 30-day kin (procedure = 06 by id) |

Version-regime notes (D12/D15/D16/D18/D19): all statutory values in this
file (the 0% rate and its Art. 76/77 flag, the Art. 54 full-rate
reference, the 1.5% ISR / 1% IVA retention values, the NMF/preferential
tariff selection, the two value floors, the prior-month solvency scope)
are code-text values cited as printed under the SOQ-30 verification watch
(§2) and live as dated config rows with instrument provenance — never
constants; each resolves as-of the transaction date with
snapshot-on-write (D15). The 1.5%/1% pair carries the explicit
dated-2007 provenance with the SOQ-37 re-verification watch (OQ-1). The
Ley IVA Arts. 54/75-77 computations are pointer-only (IVA-core wave —
consumed by id when written; SOQ-40-kin design-pass note for the route
families). Mid-year go-live (D18): a migrating regime company's open
internación bases, route resolutions and gate states ingest as
`is_historical` rows with original-period semantics (tiered ingestion; no
re-derivation of resolved rates). No hard gates beyond the statutory
blocks (D16 no-override: the value floors and the SS gate never resolve
around an unmet statutory condition by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a ZF producer selling goods produced in the zone into
  TAN with entry value US$10,000 and a demonstrated non-national component
  of US$6,000, when the internación records, then the duty base is
  US$6,000 only (never the full value), the declared value passes both
  floors (≥ entry value; materias-primas lines additionally ≥ the DM valor
  en aduana), and a declared value of US$9,000 against a US$10,000 entry
  value raises the floor-mismatch flag and blocks (FR-082, FR-086).
- **AC-002:** Given transformed goods whose cost ledger shows materias
  primas US$4,000 and gastos indirectos de fabricación US$1,500, when the
  internación's valor en aduana builds, then it CONTAINS both components
  (US$5,500 minimum content per the verbatim rule) and the support
  documents reflect the national value added (FR-083).
- **AC-003:** Given a TAN vendor delivering activity-necessary goods to a
  ZF usuario with an activa benefit state and a passing prior-month SS
  gate, when the invoice routes, then the FR-087 fiscal position applies
  the 0% IVA row with the Art. 76/77 flag stamped and the purchase feeds
  the F-07 annex-3 tipo-11 bucket (SV-FREP-FR-073 by id); the same goods
  on the Art. 17/19 exception list without an acuerdo-recorded exception
  route the full Art. 54 rate with NO tipo-11 row (FR-087, FR-088).
- **AC-004:** Given a sale of activity-necessary goods between two ZF
  beneficiaries, when both legs book, then NO IVA and no customs duties
  are caused (no-tax route), and under a DPA profile whose 12-month
  envelope expired, the same sale refuses the route — the transfer never
  extends the customs term (FR-092; 04 by id).
- **AC-005:** Given an LSI call center (letter c) billing a domestic bank
  registered in IVA, when the local-service invoice posts, then the
  receptor gate passes, the full local-tax route applies, and both
  retention triggers fire — the prestatario's 1.5% ISR anticipo row with
  the CT-anticipo suppression flag set, and the 1% IVA anticipo row
  documented through the CRE (CAT-006 code 22) — with the semestral
  dictamen e.4 verification consuming both ledgers by id (FR-096..098).
- **AC-006:** Given an LSI logistics usuario (letter b) providing a service
  directly linked to a ZF maquila's goods exportation, when the service
  bills, then the cross-regime no-tax route applies (no taxes including
  IVA) and the factura de consumidor final is issued consigning the
  prestatario's name per the FE doc rules by id; the same service without
  a demonstrable export link never takes this route (FR-099).
- **AC-007:** Given a TAN vendor delivering activity-necessary goods to a
  usuario directo of a parque de servicios, when the invoice routes, then
  it takes the exportación-definitiva position (Ley IVA Arts. 75-77) and
  NEVER the ZF 0%+76/77 position — the two route families are
  regime-exclusive by config, and a ZF profile can never resolve the LSI
  route nor vice versa (FR-087, FR-101).
- **AC-008:** Given a comercializador transferring dominion of goods into
  TAN, when the operation routes, then the transfer tax IS caused at the
  standard rate, the TAN-sale income stays OUT of the Art. 17 d)/e) and
  19 d)/e) exemption rows, and the municipal taxes compute on the
  local/total-sales-over-assets proration consumed from `02` by id
  (FR-091; SV-SPE-FR-041).
- **AC-009:** Given a ZF beneficiary whose prior-month ISSS/AFP records
  show an unpaid month, when it attempts an internación or a TAN sale,
  then the SS-solvency gate blocks the route (electronic-verification
  result recorded per Art. 9-A); when the payment records clear, then the
  gate reopens for the following sale month (cure path) (FR-102).
- **AC-010:** Given ZF desperdicios sold to the national market versus the
  same lot destined to an authorized botadero, when the dispositions
  record, then the sale computes duties on the valor en aduana while the
  botadero destination books zero duties with the DGA-control note; a
  donation records only with BOTH the MINEC calificación and the Asamblea
  exoneración references (FR-094).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-37 carried: the LSI retention VALUES 1.5% ISR anticipo / 1% IVA (80_ Art. 8 — values printed 2007, re-confirmed by the 277-2013 reform which only moved the LETTER set) — verify no later CT (Arts. 157/158 family) or Ley-ISR reform superseded the values; cross-check against the 54_ consolidated text and CT at the taxation cross-check (origin: EV14 OQ-2). FR-097/FR-098 ship them as dated rows (letters a,b,c,d,e,j post-~19-feb-2013; pre-reform rows keep h — W19 T3); a value reform lands as new dated rows. | no | Takumi S7 (taxation cross-check) | open |
| OQ-2 | EVID-252 doubt carried: the METHOD to determine the non-national component of an internación beyond the verbatim cost rule (valor en aduana ⊇ materias primas + GIF; comercializador demonstrated-national exclusion) is left to DGA practice — corpus-silent. FR-082/FR-084 encode the statutory base rules ONLY; the component-determination mechanics (cost-ledger basis, certification forms, DGA practice) ship as config slots with NO defaults. | no | Takumi S7 (DGA practice watch) | open |
| OQ-3 | SOQ-30 carried: the 12_ consolidation ends at D.L. 318-2013 (tail = 82_, D.L. 493-2025, folded W19 T3 for the extension surfaces; the routing rows of this file are untouched by 82_) and 74_ at D.L. 23-2012 — post-tail traffic unverified (D.L. 598-2020-era watch); **W19 T3: the LSI half RESOLVED — 14_ superseded by 80_ (thru D.L. 277-2013; LBs re-keyed; Art. 8 letters re-verified)**; every LB cites as printed — re-verify before implementation. The Ley IVA Art. 54/75-77 anchors additionally ride the future IVA-core wave's own verification. | no | Takumi S7 (sources watch) | open |
| OQ-4 | Art. 9-A electronic-solvency mechanics: the network security specifications and online-consultation mechanisms are DGA-established (DACG layer, not in corpus); FR-102 records the gate result and verification means with the external-interface assumption, and the force-majeure contingency route is a recorded note only — no interface emulation invented. | no | Takumi S7 (DACG watch) | open |
