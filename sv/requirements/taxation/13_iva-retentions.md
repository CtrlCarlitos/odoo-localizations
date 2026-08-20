# SV — Taxation — IVA retentions and perceptions: the CT 161 non-domiciled self-liquidation, the CT 162 grandes/medianos retention matrix (1% ex-IVA ≥ $100, AT-designated agents, uniones de hecho, the 13% unregistered-natural-person regime, MH lottery prizes), the CT 162-A card 2% anticipo and the CT 162-B judgment-interest retention (Código Tributario Arts. 161, 162, 162-A, 162-B; Ley IVA Arts. 65, 94; Reglamento IVA Art. 23)

| Field   | Value |
|-------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the IVA
retention/perception matrix of El Salvador's *Código Tributario*
(D.L. 230-2000 consolidation, CT Title IV Chapter I Section IV): the
**Art. 161** non-domiciled regime — when the transferor of the good or the
prestador of the service has neither *domicilio ni residencia* in the
country, the LOCAL acquirer/prestatario/beneficiary is the *obligado al
pago* and self-liquidates, entering the pertinent retentions via a
*mandamiento de pago* issued by the Administración Tributaria (the
services-import venue per Ley Art. 94: liquidated before the DGII, paid
before the Dirección General de Tesorería); the **Art. 162** matrix —
grandes contribuyentes acquiring goods or receiving services from
contributors OUTSIDE that classification retain **1% ex-IVA as an
anticipo** on operations of **$100.00 or more**, entered *sin deducción
alguna* in the SAME período tributario within the Art. 94 plazo (the ten
first días hábiles of the following month); the AT's power to DESIGNATE
other retention agents (other contributors, state organs, government
dependencies, municipalities, official autonomous institutions — even
non-contribuyentes and non-acquirers) at the same 1%, designated agents
retaining regardless of the subject's category save reasoned limits in
the designation act; grandes (natural, jurídical, sucesión, fideicomiso)
acquiring from *uniones de personas, sociedades irregulares o de hecho*
retaining 1% *indistintamente* of the latter's classification; the **13%
FULL-TAX regime** — grandes or medianos contribuyentes acquiring *caña
de azúcar, café o leche en estado natural, carne en pie o en canal*, or
receiving financial services generating interest (*mutuos, préstamos u
otro tipo de financiamiento*), lease services, cargo-transport services
or *dietas*/similar emoluments from **natural persons NOT registered**
in the IVA registry retain the thirteen per cent — those providers being
excluded from the registration obligation unless they opt in (opt-in
flips the retention to 1%), the retained amounts constituting
*impuesto pagado* destined to the Fondo General del Estado; the retention
TIMING (at the causation moment per the Ley's general rules — the tax
point owned by the framework file) and the entero DESPITE the provider
remaining unpaid; the grand-contribuyente quality accredited by the AT's
distinguishable *tarjeta de contribuyente*; the NC/ND adjustment path for
retention increases/decreases (CT Art. 110 inciso primero circumstances);
and the Ministerio de Hacienda's 13% retention on goods destined as
prizes in the fiscal lottery (CT Art. 118); the **Art. 162-A** card
anticipo — the 2% *anticipo a cuenta* (ex-IVA) on credit/debit-card
operations, PERCEIVED by the card issuers/administrators (agent
perceptores) at the moment they pay, credit or place at disposal to
their *afiliados*, entered within the ten first días hábiles of the
following month at the Dirección General de Tesorería and MH-authorized
banks, and credited by the afiliado against the determined tax of the
period in which the anticipo was effected (the root of the DCLE
settlement document and the *ivaPercibido* fields — e-invoicing's, by
id); and the **Art. 162-B** retention on judgment interest — courts in
*juicios ejecutivos* ordering the pagador to retain 13% over the
interests paid to a natural-person creditor (registered or not) — the
same percentage for personas jurídicas regardless of classification,
save exempt interests — with the adjudicación/remate formality block and
the extrajudicial-agreement judge's inform within fifteen days.

The file also wires the **excluidos-purchases 13% applicability**
determination — the CT-119/162-side regime the F-07 Anexo 5 H column
consumes (closing the S3 `fiscal-reporting/03` OQ-004 by wiring) — the
**retention-credit release tie-in** (the Art. 65 declare+entero
same-period gate owned by this wave's credit file, cited by id), the
**reporting surfaces** (F-07 Anexos 9-12 and the F-930 monthly informe —
`fiscal-reporting/04`, by id, never re-derived), and the **ISR-track
separation statement** (the CT 154-160 ISR retention matrix stays in
`taxation/04_isr-withholding.md`, by id — the IVA track NEVER merges
with the ISR track).

It does **not** cover: the débito/crédito determination machinery and
the Art. 65 credit gates (Arts. 62-66 — `10_iva-credit-deductibility.md`
owns them; this file's retentions route INTO its release gate
SV-TAX-FR-256/257 by pointer); the tax-point/causation rules the
retention timing consumes (`07_iva-framework.md` SV-TAX-FR-180/189/194/
195, by id — never restated); the NCE/NDE adjustment windows of the
Art. 62-63 machinery and the lot registry (`12_iva-adjustments-assets.md`,
by id — this file routes retention adjustments into them); the DTE
emission surfaces — CRE (`SV-EINV-FR-034/035`), NCE/NDE adjusting a CRE
(`SV-EINV-FR-028/031/033`) and the DCLE card settlement
(`SV-EINV-FR-040`) — all `e-invoicing/01_dte-types.md` rows, by id; the
F-07 casilla wiring and the annex/F-930 builders (Anexos 9-12 =
SV-FREP-FR-104..107, F-930 = SV-FREP-FR-111..114, Anexo 5 H =
SV-FREP-FR-086/089/091 — `fiscal-reporting/` rows, by id); the ISR
retention matrix (CT 154-160 — `taxation/04_isr-withholding.md`
SV-TAX-FR-121..131, by id; the two tracks stay distinct); the LSI
1% IVA / 1.5% ISR anticipo pair (Ley de Servicios Internacionales Art. 8
— `special-regimes/05_tan-iva-interface.md` SV-SPE-FR-097/098, by id);
and the declaration/payment interfaces themselves (the future
`15_iva-declaration-interfaces.md`, pending — cited as a pending
pointer; the venue/timing rules consumed here are anchored directly on
Ley Art. 94, LB-014).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): the retention
matrix is **Código Tributario = 05_** (D.L. 230-2000, Índice Legislativo
consolidation) — Arts. 161/162/162-A/162-B, all live (none void or
derogated in the consolidation as printed). The entero timing/venue and
the credit-release gates are **Ley = 01_** (Art. 94) and **Reglamento =
02_** survivor (Art. 23) surfaces consumed by pointer. **CT-vintage
note (rides every 05_ LB in this file):** the 05_ copy is the Índice
Legislativo consolidation edition with reform stamps through (22) —
SOQ-21 kin: post-2017 CT reforms are possible and unverified against a
current official text; the matrix values (1%, 2%, 13%, the $100 floor)
print with stamps (1)/(3)/(5)/(9) as reproduced below — re-verify at
implementation. **SOQ-54 vintage note (rides every 01_/02_ LB in this
file):** the Ley/Reglamento consolidations end at D.L. 71-2015 and
D.E. 117-2001 — post-2015/post-2001 reforms unverified; corpus-internal
signals negative; re-verify at implementation. **V1 citation rule:**
every LB row below cites 05_ (or 01_/02_) with the EVID id and the txt
line/PAGE anchor of `05_Codigo_Tributario.pdf.txt` /
`01_Ley_IVA.pdf.txt` (verified this task); both vintage watches ride all
of them. D15 (binding): retention values and floors snapshot at the
payment/retention period of the operation; corrections use
original-period parameters; CT article text is implemented AS PRINTED
(post-2017 watch above).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código Tributario (D.L. 230-2000, texto consolidado), Art. 161 | "EL ADQUIRENTE DE LOS BIENES Y EL PRESTATARIO O BENEFICIARIO DE LOS SERVICIOS, CUANDO QUIEN TRANSFIERE EL BIEN O EL PRESTADOR DE LOS SERVICIOS NO TENGA DOMICILIO NI RESIDENCIA EN EL PAÍS ES EL OBLIGADO AL PAGO DEL IMPUESTO. PARA ESTE EFECTO DEBERÁN EFECTUAR LAS RETENCIONES PERTINENTES Y ENTERARLAS MEDIANTE MANDAMIENTO DE PAGO EMITIDO POR LA ADMINISTRACIÓN TRIBUTARIA. (1)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 161 p.90 (EVID-062; verified 05_ txt lines 3860-3864, before the PAGE-91 marker) |
| LB-002 | Código Tributario, Art. 162 inciso 1° | "TODOS LOS SUJETOS PASIVOS QUE CONFORME A LA CLASIFICACIÓN EFECTUADA POR LA ADMINISTRACIÓN TRIBUTARIA OSTENTEN LA CATEGORÍA DE GRANDES CONTRIBUYENTES Y QUE ADQUIERAN BIENES MUEBLES CORPORALES O SEAN PRESTATARIOS O BENEFICIARIOS DE SERVICIOS DE OTROS CONTRIBUYENTES QUE NO PERTENEZCAN A ESA CLASIFICACIÓN, DEBERÁN RETENER EN CONCEPTO DE ANTICIPO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS EL UNO POR CIENTO SOBRE EL PRECIO DE VENTA DE LOS BIENES TRANSFERIDOS O DE LA REMUNERACIÓN DE LOS SERVICIOS PRESTADOS, LA CUAL DEBERÁ SER ENTERADA SIN DEDUCCIÓN ALGUNA EN EL MISMO PERIODO TRIBUTARIO EN EL QUE SE EFECTÚE LA ADQUISICIÓN DE BIENES O DE SERVICIOS, DENTRO DEL PLAZO QUE ESTABLECE EL ARTÍCULO 94 DE LA LEY QUE REGULA DICHO IMPUESTO. (1)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-1° p.91 (EVID-062; verified 05_ txt lines 3874-3883) |
| LB-003 | Código Tributario, Art. 162 inciso 2° | "PARA EL CÁLCULO DE LA RETENCIÓN EN REFERENCIA, NO DEBERÁ INCLUIRSE EL VALOR QUE CORRESPONDA AL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS. LA RETENCIÓN A QUE SE REFIERE ESTE ARTÍCULO SERÁ APLICABLE EN OPERACIONES EN QUE EL PRECIO DE VENTA DE LOS BIENES TRANSFERIDOS O DE LOS SERVICIOS PRESTADOS SEA IGUAL O SUPERIOR A CIEN DÓLARES. LOS CONTRIBUYENTES QUE SEAN SUJETOS DE LA RETENCIÓN DEL IMPUESTO DEBERÁN CONSIGNAR EN LOS DOCUMENTOS LEGALES QUE EMITAN EL VALOR DEL IMPUESTO RETENIDO. (1) (3)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-2° p.91 (EVID-062; verified 05_ txt lines 3884-3890) |
| LB-004 | Código Tributario, Art. 162 incisos 3° y 4° | Inciso 3°: "LA ADMINISTRACIÓN TRIBUTARIA ESTÁ FACULTADA PARA DESIGNAR COMO RESPONSABLES, EN CARÁCTER DE AGENTES DE RETENCIÓN DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS A OTROS CONTRIBUYENTES DISTINTOS A LOS QUE SE REFIERE EL INCISO PRIMERO DE ESTE ARTÍCULO, ASÍ COMO A LOS ÓRGANOS DEL ESTADO, LAS DEPENDENCIAS DEL GOBIERNO, LAS MUNICIPALIDADES Y LAS INSTITUCIONES OFICIALES AUTÓNOMAS AUNQUE NO SEAN CONTRIBUYENTES DE DICHO IMPUESTO, O NO SEAN LOS ADQUIRENTES DE LOS BIENES O PRESTATARIOS DE LOS SERVICIOS. EN ESTE CASO, EL PORCENTAJE A RETENER CORRESPONDERÁ AL UNO POR CIENTO SOBRE EL PRECIO DE VENTA DE LOS BIENES TRANSFERIDOS O DE LOS SERVICIOS PRESTADOS. (1) (3)" Inciso 4°: "LOS SUJETOS DESIGNADOS COMO AGENTES DE RETENCIÓN POR LA ADMINISTRACIÓN TRIBUTARIA, DEBERÁN REALIZAR LA RESPECTIVA RETENCIÓN INDISTINTAMENTE LA CLASIFICACIÓN DE CATEGORÍA DE CONTRIBUYENTE QUE OSTENTE EL SUJETO DE RETENCIÓN; SALVO QUE EN EL ACTO DE DESIGNACIÓN LA ADMINISTRACIÓN TRIBUTARIA ESTABLEZCA DE FORMA RAZONADA LÍMITES AL AGENTE DE RETENCIÓN. (9)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-3°/4° p.91 (EVID-062; verified 05_ txt lines 3891-3904) |
| LB-005 | Código Tributario, Art. 162 inciso 5° | "AUTORICE AL MINISTERIO DE HACIENDA A RETENER EL TRECE POR CIENTO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS, APLICADO SOBRE EL PRECIO DE VENTA DE LOS BIENES TRANSFERIDOS CUANDO SEAN DESTINADOS COMO PREMIOS EN LA REALIZACIÓN DE LA LOTERÍA FISCAL A QUE SE REFIERE EL ARTÍCULO 118 DE ESTE CÓDIGO. (5)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-5° p.91 (EVID-062; verified 05_ txt lines 3905-3908) |
| LB-006 | Código Tributario, Art. 162 inciso 6° | "TODA PERSONA NATURAL O JURÍDICA, SUCESIÓN, FIDEICOMISO QUE OSTENTE LA CALIDAD DE GRAN CONTRIBUYENTE, QUE ADQUIERAN BIENES O RECIBAN SERVICIOS DE UNIONES DE PERSONAS, SOCIEDADES IRREGULARES O DE HECHO, DEBERÁN RETENER EL UNO POR CIENTO EN CONCEPTO DEL CITADO IMPUESTO, INDISTINTAMENTE DE LA CLASIFICACIÓN A QUE PERTENEZCAN ÉSTAS. (9)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-6° p.91 (EVID-062; verified 05_ txt lines 3909-3912) |
| LB-007 | Código Tributario, Art. 162 inciso 7° | "LOS SUJETOS CLASIFICADOS COMO GRANDES O MEDIANOS CONTRIBUYENTES QUE ADQUIERAN CAÑA DE AZÚCAR, CAFÉ O LECHE EN ESTADO NATURAL, CARNE EN PIE O EN CANAL, O SEAN PRESTATARIOS DE SERVICIOS FINANCIEROS QUE GENEREN INTERESES POR MUTUOS, PRÉSTAMOS U OTRO TIPO DE FINANCIAMIENTO, SERVICIOS DE ARRENDAMIENTO, SERVICIOS DE TRANSPORTE DE CARGA, ASÍ COMO POR DIETAS O CUALQUIER OTRO EMOLUMENTO DE IGUAL O SIMILAR NATURALEZA, PRESTADO POR PERSONAS NATURALES NO INSCRITOS EN EL REGISTRO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS, DEBERÁN RETENER EL TRECE POR CIENTO EN CONCEPTO DEL CITADO IMPUESTO. AQUELLAS PERSONAS NATURALES QUE SE DEDIQUEN EXCLUSIVAMENTE A LA TRANSFERENCIA DE BIENES O PRESTACIONES DE SERVICIOS DESCRITOS EN ESTE INCISO, ESTARÁN EXCLUIDOS DE LA OBLIGACIÓN DE INSCRIBIRSE PARA EL PRESENTE IMPUESTO, SALVO QUE OPTEN POR SOLICITAR SU INSCRIPCIÓN A LA ADMINISTRACIÓN TRIBUTARIA, EN CUYO CASO LA RETENCIÓN A APLICAR SERÁ DEL UNO POR CIENTO. (9)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-7° p.92 (EVID-062; verified 05_ txt lines 3920-3931) |
| LB-008 | Código Tributario, Art. 162 incisos 8° y 9° | Inciso 8°: "LAS CANTIDADES QUE HUBIEREN SIDO RETENIDAS A LAS PERSONAS NATURALES NO INSCRITAS EN EL REGISTRO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS, CONSTITUYEN IMPUESTO PAGADO Y PASARÁN AL FONDO GENERAL DEL ESTADO.(9)" Inciso 9°: "LAS RETENCIONES SE EFECTUARÁN EN EL MOMENTO EN QUE SEGÚN LAS REGLAS GENERALES QUE ESTIPULA LA LEY DE IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS SE CAUSA DICHO IMPUESTO Y DEBERÁN ENTERARSE AL FISCO DE LA REPÚBLICA AUNQUE NO SE HAYA REALIZADO EL PAGO RESPECTIVO AL PROVEEDOR DE LOS BIENES O DE LOS SERVICIOS. (1)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-8°/9° p.92 (EVID-062; verified 05_ txt lines 3932-3939) |
| LB-009 | Código Tributario, Art. 162 incisos 10° y 11° | Inciso 10°: "PARA EFECTOS DE LO DISPUESTO EN ESTE ARTÍCULO LA CALIDAD DE GRAN CONTRIBUYENTE SE ACREDITARÁ POR MEDIO DE LA TARJETA DE CONTRIBUYENTE QUE PROPORCIONE LA ADMINISTRACIÓN TRIBUTARIA, LA CUAL SE DISTINGUIRÁ DE LAS TARJETAS QUE SE EMITAN A LAS DEMÁS CATEGORÍAS DE CONTRIBUYENTES. (1)" Inciso 11°: "DEBERÁN DOCUMENTARSE MEDIANTE NOTAS DE DÉBITO O CRÉDITO, SEGÚN CORRESPONDA, LOS AJUSTES POR AUMENTOS O DISMINUCIONES A LAS RETENCIONES DEL IMPUESTO QUE HAYAN SIDO REALIZADAS EN SU OPORTUNIDAD, POR LAS MISMAS CIRCUNSTANCIAS A QUE SE REFIERE EL PRIMER INCISO DEL ARTÍCULO 110 DE ESTE CÓDIGO. (3)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-10°/11° p.92 (EVID-062; verified 05_ txt lines 3940-3947) |
| LB-010 | Código Tributario, Art. 162-A incisos 1°-3° (with the marginal heading) | Heading: "ANTICIPO A CUENTA DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS EN OPERACIONES CON TARJETA DE CRÉDITO O CON TARJETAS DE DÉBITO. (1)" Inciso 1°: "LOS CONTRIBUYENTES QUE REALICEN TRANSFERENCIAS DE BIENES O PRESTACIONES DE SERVICIOS Y RECIBAN PAGOS POR MEDIO DE TARJETAS DE CRÉDITO O DE DÉBITO ESTÁN OBLIGADOS A ENTERAR EN CONCEPTO DE ANTICIPO A CUENTA DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS EL DOS POR CIENTO DEL IMPORTE DEL VALOR DEL BIEN O DEL SERVICIO." Inciso 2°: "EL ANTICIPO A CUENTA A QUE SE REFIERE EL INCISO ANTERIOR SERÁ PERCIBIDO POR LOS SUJETOS PASIVOS EMISORES O ADMINISTRADORES DE TARJETAS DE CRÉDITO O DE DÉBITO." Inciso 3°: "PARA EFECTOS DE LO DISPUESTO EN LOS INCISOS PRECEDENTES, SE DESIGNAN COMO RESPONSABLES EN CARÁCTER DE AGENTES PERCEPTORES DE DICHO ANTICIPO A CUENTA A LOS SUJETOS PASIVOS EMISORES O ADMINISTRADORES DE TARJETAS DE CRÉDITO O DE DÉBITO." | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-A heading + 1°-3° pp.92-93 (EVID-062; verified 05_ txt lines 3948-3967) |
| LB-011 | Código Tributario, Art. 162-A incisos 4°-8° | Inciso 4°: "LA PERCEPCIÓN DEBERÁN REALIZARLA LOS EMISORES O ADMINISTRADORES DE TARJETAS DE CRÉDITO O DE DÉBITO AL MOMENTO QUE PAGUEN, ACREDITEN O PONGAN A DISPOSICIÓN POR CUALQUIER FORMA A SUS AFILIADOS, SUMAS POR LAS TRANSFERENCIAS DE BIENES O PRESTACIONES DE SERVICIOS GRAVADAS CON EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS REALIZADAS POR DICHOS AFILIADOS A LOS TARJETA HABIENTES EN EL PAÍS." Inciso 5°: "PARA EL CÁLCULO DEL ANTICIPO A CUENTA A QUE SE REFIERE ESTE ARTÍCULO, DEBERÁ EXCLUIRSE EL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS." Inciso 6°: "EL ANTICIPO A CUENTA CONSTITUIRÁ PARA LOS AFILIADOS UN PAGO PARCIAL DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS CAUSADO, EL CUAL DEBERÁN ACREDITAR CONTRA EL IMPUESTO DETERMINADO QUE CORRESPONDA AL PERÍODO TRIBUTARIO EN QUE SE EFECTUÓ EL ANTICIPO A CUENTA." Inciso 7°: "LAS SUMAS QUE PERCIBAN LOS EMISORES O ADMINISTRADORES DE TARJETAS DE CRÉDITO O DE DÉBITO CONFORME A LAS REGLAS DEL PRESENTE ARTÍCULO DEBERÁN ENTERARLAS SIN DEDUCCIÓN ALGUNA EN LA DIRECCIÓN GENERAL DE TESORERÍA, EN CUALQUIERA DE LAS OFICINAS QUE ESTA INSTITUCIÓN TENGA EN EL PAÍS Y EN LOS BANCOS AUTORIZADOS POR EL MINISTERIO DE HACIENDA, MEDIANTE LOS FORMULARIOS QUE DISPONGA LA ADMINISTRACIÓN, DENTRO DE LOS DIEZ PRIMEROS DÍAS HÁBILES DEL MES SIGUIENTE AL PERIODO TRIBUTARIO EN QUE SE HICIERON LAS PERCEPCIONES." Inciso 8°: "PARA EFECTOS DE ESTE ARTÍCULO SE ENTENDERÁ POR AFILIADO EL CONTRIBUYENTE DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS QUE ACEPTE PAGOS MEDIANTE EL SISTEMA DE TARJETAS DE CRÉDITO O DÉBITO. (1)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-A 4°-8° pp.92-93 (EVID-062; verified 05_ txt lines 3968-3989) |
| LB-012 | Código Tributario, Art. 162-B incisos 1° y 2° (with the marginal heading) | Heading: "RETENCIONES EN JUICIOS EJECUTIVOS. (9)" Inciso 1°: "EN TODOS LOS TRIBUNALES DE LA REPÚBLICA QUE EN RAZÓN DE SU COMPETENCIA CONOZCAN DE JUICIOS EJECUTIVOS, EN LA SENTENCIA DEFINITIVA DEBERÁN ORDENAR AL PAGADOR RESPECTIVO O A LA PERSONA ENCARGADA DE LOS FONDOS, QUE UNA VEZ EFECTUADA LA LIQUIDACIÓN CORRESPONDIENTE, SOBRE EL MONTO DE LOS INTERESES A PAGAR AL ACREEDOR, SIEMPRE QUE ÉSTE SEA UNA PERSONA NATURAL INSCRITA O NO EN EL REGISTRO DE CONTRIBUYENTES DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS, RETENGA EN CONCEPTO DE DICHO IMPUESTO EL TRECE POR CIENTO SOBRE LAS MISMAS." Inciso 2°: "IGUAL PORCENTAJE DE RETENCIÓN DEL IMPUESTO APLICARÁ PARA LAS PERSONAS JURÍDICAS, INDEPENDIENTEMENTE DE LA CLASIFICACIÓN DE CONTRIBUYENTE QUE LE HAYA SIDO ASIGNADA POR LA ADMINISTRACIÓN TRIBUTARIA, SALVO QUE LOS INTERESES SE ENCUENTREN EXENTOS DEL IMPUESTO." | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-B heading + 1°-2° p.93 (EVID-062; verified 05_ txt lines 3990-4001) |
| LB-013 | Código Tributario, Art. 162-B incisos 3° y 4° | Inciso 3°: "EN EL CASO QUE EL PAGO SEA MEDIANTE LA ADJUDICACIÓN O REMATE DE ALGÚN BIEN MUEBLE, INMUEBLE O DERECHO, LA TRANSFERENCIA O CESIÓN NO SE FORMALIZARÁ MIENTRAS EL BENEFICIARIO NO PAGUE A LA ADMINISTRACIÓN TRIBUTARIA LO QUE CORRESPONDE EN CONCEPTO DE IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS, EN LOS PORCENTAJES SEÑALADOS EN LOS INCISOS ANTERIORES EN ATENCIÓN A SU CALIDAD." Inciso 4°: "SÓLO EN AQUELLOS CASOS EN QUE EL ACREEDOR Y EL DEUDOR LLEGAREN A UN ACUERDO EXTRAJUDICIAL, EL JUEZ CUMPLIRÁ CON SU OBLIGACIÓN INFORMANDO A LA ADMINISTRACIÓN TRIBUTARIA SOBRE LAS GENERALES DE AMBOS, EL MONTO OBJETO DEL LITIGIO, Y EN SU CASO LOS EXTREMOS DE DICHO ACUERDO; LO ANTERIOR DEBERÁ SER INFORMADO DENTRO DE LOS QUINCE DÍAS POSTERIORES DEL ACUERDO REFERIDO. EL INFORME SE PRESENTARÁ MEDIANTE FORMULARIOS, CON LOS REQUISITOS Y ESPECIFICACIONES QUE DISPONGA LA ADMINISTRACIÓN TRIBUTARIA. (9)" | `sv/sources/05_Codigo_Tributario.pdf` | Art. 162-B 3°-4° pp.93-94 (EVID-062; verified 05_ txt lines 4002-4019) |
| LB-014 | Ley IVA (D.L. 296-1992, texto consolidado), Art. 94 | "LA DECLARACIÓN JURADA INCLUIRÁ EL PAGO Y DEBERÁ SER PRESENTADA EN LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS, EN LA DIRECCIÓN GENERAL DE TESORERÍA, EN LOS BANCOS Y OTRAS INSTITUCIONES FINANCIERAS AUTORIZADAS POR EL MINISTERIO DE HACIENDA, EN CUALQUIERA DE LAS OFICINAS QUE ESTAS INSTITUCIONES TENGAN EN EL PAÍS, DENTRO DE LOS DIEZ PRIMEROS DÍAS HÁBILES DEL MES SIGUIENTE AL PERIODO TRIBUTARIO CORRESPONDIENTE. EN ESTE MISMO LAPSO DEBEN INGRESARSE LOS IMPUESTOS RETENIDOS O PERCIBIDOS POR LOS AGENTES DE RETENCIÓN O DE PERCEPCIÓN." … "EL IMPUESTO SOBRE IMPORTACIONES E INTERNACIONES DE SERVICIOS SE LIQUIDARÁ ANTE LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS Y SE PAGARÁ ANTE LA DIRECCIÓN GENERAL DE TESORERÍA. LA COMPETENCIA PARA LIQUIDAR DE OFICIO EL IMPUESTO SOBRE LA IMPORTACIÓN E INTERNACIÓN DE SERVICIOS NO LIQUIDADO CORRESPONDERÁ A LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS. (8)" | `sv/sources/01_Ley_IVA.pdf` | Art. 94 p.43 (EVID-056; verified 01_ txt lines 1583-1602, PAGE 43) |
| LB-015 | Ley IVA, Art. 65 incisos finales + Reglamento IVA (D.E. 83-1992 consolidado), Art. 23 — **POINTER** | Art. 65: CT-162-retained IVA is crédito for the AGENT "EN EL MISMO PERÍODO QUE CORRESPONDA A LA FECHA DE EMISIÓN DEL COMPROBANTE DE RETENCIÓN (CT 112)" and CT-161 anticipo retentions are crédito "AMPARADOS POR EL MANDAMIENTO DE INGRESO" — both "SIEMPRE Y CUANDO SE DECLARE Y ENTERE ÍNTEGRAMENTE EN EL MISMO PERÍODO" (the post-entero credit route's Ley root). Rgto. Art. 23: agent-retained amounts are crédito "EN EL MISMO PERÍODO TRIBUTARIO, SIEMPRE QUE SE HAYAN INGRESADO ÍNTEGRAMENTE AL FISCO" (CT-162 side); CT-161-kin amounts via "MANDAMIENTO DE INGRESO Y EL RECIBO" (stale Ley-34 anchor re-anchored to CT 161) — credit-release machinery owned by `10_iva-credit-deductibility.md` (SV-TAX-FR-256/257); consumed here by pointer, never restated | `sv/sources/01_Ley_IVA.pdf` + `sv/sources/02_Reglamento_IVA.pdf` | Ley Art. 65 pp.30-32 (EVID-322; 01_ txt PAGE 30-32); Rgto. Art. 23 (EVID-336; Rgto. PAGE 6-7) |

Dead text and separation notes — never implementable as merged rows
(per wave constraints): the ISR retention matrix (CT Arts. 154-160 —
agents, 10%/20%/25%/5% values, courts' 10% on judgment interest,
non-residents) lives in `taxation/04_isr-withholding.md`
SV-TAX-FR-121..131 and is NEVER folded into this file — a single
operation may carry an ISR retention AND an IVA retention as separate
tax lines, each under its own matrix (the LSI 1.5% ISR / 1% IVA pair of
`special-regimes/05_tan-iva-interface.md` SV-SPE-FR-097/098 is the
worked example, by id). CT Art. 163 (grandes PERCEIVING 1% on transfers
to non-grand for the acquirer's activo realizable) is the
perception-side sibling OUTSIDE this file's scoped range (161/162/162-A/
162-B) — recorded here as a boundary note for the wave's index task,
not implemented by this file's FRs. The reform stamps printed on the CT
rows — (1)/(3)/(5)/(9) — are consolidation provenance, not behavior.
Both vintage watches (CT Índice Legislativo edition; SOQ-54) ride every
row above.

## 3. Functional Requirements

### 3.1 CT Art. 161 — non-domiciled transferors/prestadores: the acquirer as obligado al pago

- **SV-TAX-FR-303:** The system shall implement the Art. 161
  self-liquidation regime: whenever the transferor of the good or the
  prestador of the service has NO domicilio nor residencia in the
  country, the system shall radicate the IVA payment obligation on the
  LOCAL acquirer of the goods and the prestatario or beneficiary of the
  services (the buyer-side record carries the *obligado al pago* flag),
  shall compute the pertinent retention (self-withholding of the
  operation's IVA), and shall model the entero as effected MEDIANTE
  MANDAMIENTO DE PAGO EMITIDO POR LA ADMINISTRACIÓN TRIBUTARIA (the
  *mandamiento de ingreso* of the Art. 65 credit route — LB-015
  pointer), with the services-import venue per Ley Art. 94-IV: the tax
  LIQUIDATES before the DGII and PAYS before the Dirección General de
  Tesorería, oficio liquidation of unliquidated services imports
  belonging to the DGII (declaration/payment interface surfaces: future
  `15_iva-declaration-interfaces.md`, pending — this FR anchors the
  venue/timing rule directly on LB-014); the credit for the retained
  amount releases ONLY through this file's wave-sibling gate
  SV-TAX-FR-257 (`10_iva-credit-deductibility.md`, by id — declare +
  enter same period, mandamiento-referenced). The operation's
  import/tax-point classification consumes the framework file's surfaces
  (SV-TAX-FR-187/188/189, by id).
  (LB-001; LB-014; LB-015 pointer; EVID-062/056/322; TAX 07-file
  SV-TAX-FR-187/188/189; TAX 10-file SV-TAX-FR-257)

### 3.2 CT Art. 162 — the grandes/medianos retention matrix

- **SV-TAX-FR-304:** The system shall implement the Art. 162 inciso 1°
  core rule: every sujeto pasivo classified by the Administración
  Tributaria in the category of GRANDES CONTRIBUYENTES that acquires
  bienes muebles corporales or is prestatario/beneficiary of services
  from contributors NOT belonging to that classification shall retain,
  as ANTICIPO of the IVA, EL UNO POR CIENTO (1%) over the precio de
  venta of the goods transferred or the remuneración of the services —
  the retention base EXCLUDING the IVA itself (inciso 2°: no IVA value
  in the cálculo) — applicable ONLY on operations whose precio de
  venta/remuneración is IGUAL O SUPERIOR A CIEN DÓLARES ($100.00
  per-operation floor); the retained amount is entered SIN DEDUCCIÓN
  ALGUNA in the SAME período tributario as the acquisition, DENTRO DEL
  PLAZO of Ley Art. 94 (the ten first días hábiles of the month
  following the period — LB-014); values and floors snapshot at the
  retention period (D15).
  (LB-002; LB-003; LB-014; EVID-062/056)
- **SV-TAX-FR-305:** The system shall document every Art. 161/162
  retention with the CT-Art.-112 retention comprobante — the CRE
  electronic document (`e-invoicing/01_dte-types.md` SV-EINV-FR-034/
  035, by id: emisor = agente de retención, receptor = sujeto de
  retención, `codigoRetencionMH` CAT-006 — 22 = Retención IVA 1%, C4 =
  13%, C9 = otras; `ivaRetenido` = montoSujetoGrav × legal rate) — and
  shall require the RETAINED subject's own legal documents (the
  supplier's CCF/factura) to CONSIGN the retained tax value
  (inciso 2° final sentence), the retention records kept SEPARATE from
  the CCFs received (the separate-registration condition of the credit
  release gate — SV-TAX-FR-256 by id).
  (LB-003; EVID-062; EINV 01-file SV-EINV-FR-034/035; TAX 10-file
  SV-TAX-FR-256)
- **SV-TAX-FR-306:** The system shall implement the AT-designation
  surface: the Administración Tributaria is FACULTADA (empowered) to
  designate as RESPONSABLES, in the character of IVA retention agents,
  (a) other contributors distinct from the grandes of inciso 1°, and
  (b) the ÓRGANOS DEL ESTADO, the DEPENDENCIAS DEL GOBIERNO, the
  MUNICIPALIDADES and the INSTITUCIONES OFICIALES AUTÓNOMAS — even if they are NOT
  contributors of the tax nor the acquirers of the goods/services — in
  which case the retention percentage is EL UNO POR CIENTO over the
  precio de venta; a DESIGNATED agent shall retain INDISTINTAMENTE of
  the contribuyente-category the retained subject ostenta, SAVE that
  the designation act itself may establish REASONED LIMITS (límites al
  agente de retención), recorded as per-agent scope constraints. The
  designation LIST itself is administered practice absent from the
  corpus — a configuration surface with NO invented entries (OQ-3).
  (LB-004; EVID-062)
- **SV-TAX-FR-307:** The system shall implement the uniones rule: every
  persona natural o jurídica, sucesión or fideicomiso ostenting the
  quality of GRAN CONTRIBUYENTE that acquires goods or receives
  services from UNIONES DE PERSONAS, SOCIEDADES IRREGULARES O DE HECHO
  shall retain EL UNO POR CIENTO in concept of the tax, INDISTINTAMENTE
  of the classification those entities belong to (no category test on
  the supplier beyond its union/irregular/de-hecho kind — the
  supplier-kind classification consumes the framework file's
  SV-TAX-FR-197 subject taxonomy, by id).
  (LB-006; EVID-062; TAX 07-file SV-TAX-FR-197)
- **SV-TAX-FR-308:** The system shall implement the 13% full-tax
  regime: sujetos classified as GRANDES or MEDIANOS CONTRIBUYENTES that
  (a) acquire CAÑA DE AZÚCAR, CAFÉ O LECHE EN ESTADO NATURAL or CARNE EN
  PIE O EN CANAL, or (b) are prestatarios of SERVICIOS FINANCIEROS that
  generate interests (mutuos, préstamos u otro tipo de financiamiento),
  SERVICIOS DE ARRENDAMIENTO, SERVICIOS DE TRANSPORTE DE CARGA, or
  DIETAS or any other emolument of equal or similar nature, PRESTADO
  POR PERSONAS NATURALES NO INSCRITAS in the IVA registry, shall retain
  EL TRECE POR CIENTO (13%) EN CONCEPTO DEL CITADO IMPUESTO — the
  retention IS the full tax (the unregistered provider cannot trasladar
  it); the system shall flag those natural-person providers as EXCLUIDOS
  DE LA OBLIGACIÓN DE INSCRIBIRSE when exclusively dedicated to these
  transfers/services, SALVO they opt to request inscription — the opt-in
  flipping the retention to EL UNO POR CIENTO (registered-provider
  flip); and shall treat amounts retained from the unregistered natural
  persons as IMPUESTO PAGADO destined to the FONDO GENERAL DEL ESTADO —
  definitive for the provider, no credit flows back to them (their
  retention-credit surfaces never open).
  (LB-007; LB-008; EVID-062)
- **SV-TAX-FR-309:** The system shall fix the retention TIMING at the
  causation moment: retentions are effected EN EL MOMENTO the tax is
  caused per the general rules of the Ley IVA (the tax-point machinery
  of the framework file — SV-TAX-FR-180/189/194/195, by id; the resolved
  tax point snapshotted on the operation is the retention's D15 anchor),
  and the retained amounts shall be entered to the FISCO DE LA REPÚBLICA
  AUNQUE NO SE HAYA REALIZADO EL PAGO RESPECTIVO AL PROVEEDOR — the
  entero NEVER defers on the agent's own supplier-payment state (no
  payment-contingent blocking of the entero obligation or of the credit
  release gate).
  (LB-008; EVID-062; TAX 07-file SV-TAX-FR-180/189/194/195)
- **SV-TAX-FR-310:** The system shall source the GRAN CONTRIBUYENTE
  quality — for every matrix agent test — from the TARJETA DE
  CONTRIBUYENTE provided by the Administración Tributaria, which
  DISTINGUISHES itself from the cards emitted to the other categories:
  the partner's AT classification (grande · mediano · otra) is recorded
  with its tarjeta reference as the accreditation source feeding the
  retention-matrix agent resolution (config-gap: the classification
  itself is administered data — onboarding loads it; OQ-3 kin).
  (LB-009; EVID-062)
- **SV-TAX-FR-311:** The system shall document adjustments for
  AUMENTOS O DISMINUCIONES to retentions already realized — by the same
  circumstances of CT Art. 110 inciso primero — MEDIANTE NOTAS DE DÉBITO
  O CRÉDITO according to which corresponds: the retention-adjustment
  NCE/NDE relates the prior CRE (`e-invoicing/01_dte-types.md`
  SV-EINV-FR-028/031/033 — adjustment of 07-CR documents, by id) and
  routes into the Art. 62-63 adjustment windows owned by this wave's
  adjustments file (`12_iva-adjustments-assets.md`, by id — never
  restated here); the adjustment recomputes the retention delta at
  ORIGINAL-period parameters (D15).
  (LB-009; EVID-062; EINV 01-file SV-EINV-FR-028/031/033; TAX 12-file
  by id)
- **SV-TAX-FR-312:** The system shall model the Ministerio de Hacienda
  lottery retention: on the supply of goods DESTINADOS COMO PREMIOS in
  the realization of the LOTERÍA FISCAL (CT Art. 118), MH — as the
  acquirer — retains EL TRECE POR CIENTO of the IVA applied SOBRE EL
  PRECIO DE VENTA of the goods transferred (awareness-level event: the
  retention books on the prize-goods purchase with MH as agent, feeding
  the same entero/reporting surfaces; the lottery-operation registry
  itself is not this file's surface).
  (LB-005; EVID-062)
- **SV-TAX-FR-313:** The system shall determine the excluidos-purchases
  13% APPLICABILITY — the CT-119/162-side regime the F-07 Anexo 5
  column H consumes: for every purchase from a SUJETO EXCLUIDO
  (unregistered natural person, CT 119 zone), the 13% IVA retention
  applies when the buyer's classification is grande or mediano AND the
  operation falls in the Art. 162 inciso 7° catalog (caña/café/leche/
  carne or the financial-interest/lease/carga-transport/dietas services
  family) — the applicability flag resolving per FR-308's matrix and
  carried on the purchase record so that `fiscal-reporting/03`
  SV-FREP-FR-086 (Anexo 5 build) and SV-FREP-FR-089 (H = 0.13 × G
  validation) consume it by id; the post-entero credit re-entry into
  casilla 128 stays SV-FREP-FR-091 (by id). This wiring CLOSES
  `fiscal-reporting/03_f07-annexes-purchases.md` OQ-004 (the index task
  flips its status). Where the catalog does not reach, H resolves 0
  ("cuando aplique" — no invented 13% extension; boundary OQ-4).
  (LB-007; EVID-062; FREP 03-file SV-FREP-FR-086/089/091)

### 3.3 CT Art. 162-A — the card 2% anticipo (perception)

- **SV-TAX-FR-314:** The system shall implement the card anticipo
  root: contributors realizing transfers of goods or prestations of
  services that RECEIVE payments by credit or debit card are obliged to
  the ANTICIPO A CUENTA of EL DOS POR CIENTO (2%) of the importe of the
  value of the good or service — the calculation EXCLUDING the IVA
  (ex-IVA base) — PERCIBIDO by the sujetos pasivos EMISORES O
  ADMINISTRADORES of the cards (designated RESPONSABLES EN CARÁCTER DE
  AGENTES PERCEPTORES), the perception realized AT THE MOMENT they pay,
  credit or place at disposal IN ANY FORM to their AFILIADOS sums
  corresponding to taxed transfers/prestations realized by those
  afiliados to the TARJETA HABIENTES in the country; AFILIADO = the IVA
  contributor accepting payments through the card system (the affiliate
  flag on the partner). The settlement record's emission surface is the
  DCLE (`e-invoicing/01_dte-types.md` SV-EINV-FR-040, by id — the
  card-acquirer settlement document with `ivaPercibido` = 2% of the net
  subject amount; never restated here).
  (LB-010; LB-011; EVID-062; EINV 01-file SV-EINV-FR-040)
- **SV-TAX-FR-315:** The system shall implement the anticipo's credit
  and entero: the 2% anticipo constitutes for the AFILIADOS a PAGO
  PARCIAL of the caused tax, which they shall ACREDIT against the
  impuesto determinado of the PERÍODO TRIBUTARIO EN QUE SE EFECTUÓ EL
  ANTICIPO (the settlement period — practically the period following
  the card sale, the perception happening at the issuer's payment/
  crediting); the issuers/administrators enter the perceived sums SIN
  DEDUCCIÓN ALGUNA at the DIRECCIÓN GENERAL DE TESORERÍA (any of its
  in-country offices) and the MH-AUTHORIZED BANKS, via the AT's forms,
  DENTRO DE LOS DIEZ PRIMEROS DÍAS HÁBILES DEL MES SIGUIENTE to the
  period of the perceptions (LB-014's Art. 94 lapso kin — the agents'
  entero deadline); the afiliado's credit consumption posts on the
  settlement-linked ledger line, feeding the F-07 credit-side annex 6
  (Anticipo a Cuenta, casilla 161) and the payable-side Anexo 11 as
  reporting views only (`fiscal-reporting/04` SV-FREP-FR-100/106/110,
  by id — no re-derivation).
  (LB-011; LB-014; EVID-062/056; FREP 04-file SV-FREP-FR-100/106/110)

### 3.4 CT Art. 162-B — retentions in juicios ejecutivos

- **SV-TAX-FR-316:** The system shall model the judgment-interest
  retention: in ALL tribunals of the Republic that, by reason of their
  competence, know of JUICIOS EJECUTIVOS, the SENTENCIA DEFINITIVA
  orders the respective pagador or the person in charge of the funds
  that, once the corresponding LIQUIDACIÓN is effected, over the MONTO
  DE LOS INTERESES to pay the creditor — the creditor being a PERSONA
  NATURAL, inscrita o no in the IVA registry — the retention of EL
  TRECE POR CIENTO (13%) as the IVA on those interests; the IGUAL
  PORCENTAJE applies for PERSONAS JURÍDICAS, independently of the
  contribuyente classification assigned by the AT, SALVO the interests
  be EXEMPT from the tax (the exemption gate consuming the exemptions
  file's catalog, by id); where the payment is by ADJUDICACIÓN O REMATE
  of a bien mueble, inmueble o derecho, the transfer or cesión DOES NOT
  FORMALIZE while the beneficiary does not pay the AT the corresponding
  IVA in the percentages of the preceding incisos according to their
  quality (a formality-block state on the adjudication record); and in
  the ACUERDO EXTRAJUDICIAL case the judge informs the AT — generales
  of both parties, the litigio amount, the agreement's extremos —
  DENTRO DE LOS QUINCE DÍAS of the agreement, via the AT's forms (an
  inform event, awareness-level).
  (LB-012; LB-013; EVID-062; TAX 08-file by id for the exemption gate)

### 3.5 Credit-release tie-in, reporting surfaces and the ISR-track separation

- **SV-TAX-FR-317:** The system shall tie every retention/perception
  event of this file to the credit-release gate owned by this wave's
  credit file: the AGENT's crédito fiscal for CT-162 retentions
  releases only IN THE SAME PERIOD of the CRE's emission date when the
  retention is DECLARED and ENTERED ÍNTEGRAMENTE to the fisco in that
  same period with the retained tax registered SEPARATELY from the
  CCFs, and the CT-161 self-liquidation credit releases only via the
  MANDAMIENTO DE INGRESO plus receipt — both gates consumed by id
  (`10_iva-credit-deductibility.md` SV-TAX-FR-256/257; LB-015 pointer);
  this file's FR-304/FR-309 entero states (same-period, despite
  supplier-non-payment) are the ledger facts that gate consumes — the
  gate itself is never restated here.
  (LB-002; LB-008; LB-015 pointer; EVID-322/336; TAX 10-file
  SV-TAX-FR-256/257)
- **SV-TAX-FR-318:** The system shall expose every retention/
  perception event of this file to the fiscal-reporting surfaces as
  VIEWS, never re-deriving them: the payable-side F-07 Anexos 9-12 —
  Anexo 9 Percepción IVA 1% (SV-FREP-FR-104), Anexo 10 Retención IVA 1%
  Terceros Domiciliados (SV-FREP-FR-105), Anexo 11 Anticipo a Cuenta
  IVA 2% (SV-FREP-FR-106), Anexo 12 Retención IVA 13% Terceros
  Domiciliados (SV-FREP-FR-107), with the percent-column validation
  SV-FREP-FR-108 — and the F-930 v3 monthly retIVA informe
  (SV-FREP-FR-111..114), all `fiscal-reporting/04` rows cited by id;
  the credit-side surfaces (Anexo 5 H and the casilla-128 post-entero
  re-entry, Anexos 6-8, casillas 161-163) likewise by id
  (SV-FREP-FR-086/089/091; SV-FREP-FR-100/101/102/110).
  (LB-002; LB-007; LB-010; LB-011; EVID-062; FREP 04-file
  SV-FREP-FR-104..108/111..114; FREP 03-file SV-FREP-FR-086/089/091)
- **SV-TAX-FR-319:** The system shall keep the IVA retention track
  STRICTLY SEPARATE from the ISR retention track: the CT 154-160 ISR
  matrix (agents, the 10%/20%/25%/5% values, the courts' 10% on
  judgment interest, non-residents) lives in
  `taxation/04_isr-withholding.md` SV-TAX-FR-121..131 (by id) and shall
  never merge with this file's matrix — an operation carrying both
  retentions (e.g., a service with IVA 13% and ISR 10%) books them as
  SEPARATE tax lines under their own matrices and reporting surfaces;
  the LSI pair (1% IVA anticipo / 1.5% ISR anticipo on local-market
  services) remains special-regimes territory
  (`special-regimes/05_tan-iva-interface.md` SV-SPE-FR-097/098, by id —
  this file's CT matrix is NOT their source).
  (LB-001..LB-013; EVID-062; TAX 04-file SV-TAX-FR-121..131; SPE
  05-file SV-SPE-FR-097/098)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars): the retention matrix (1%/2%/13%, the $100
floor, the 10-hábiles deadlines) enters as legal-anchor config rows with
the CT-vintage watch (§2) riding them. Layer semantics: classification/
timing/subject computation living in the LGPL client (wave default
`odoo`; see §5) — nothing here touches DTE generation (the CRE/DCLE
emission rows are e-invoicing's, by id). **Interface entity for the
wave's index and the fiscal-reporting consumers:** the retention-rule
matrix + the retention/perception event ledger below.

**Retention matrix (config, D15-snapshotted):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.retention.rule (new) | code, legal_anchor | char / char | ct161_nodomiciliado · ct162_grandes_1pct · ct162_designated_1pct · ct162_uniones_1pct · ct162_agro_fin_13pct · ct162_lottery_mh_13pct · ct162a_card_2pct · ct162b_judgment_13pct — anchor string per row (CT article + inciso) | FR-303, FR-304, FR-306, FR-307, FR-308, FR-312, FR-314, FR-316 |
| l10n_sv.iva.retention.rule | rate, floor_amount, base_excludes_iva | decimal / monetary / boolean | 0.01 with 100.00 floor; 0.13 (no printed floor — OQ-4); 0.02 (no floor); base always ex-IVA | FR-304, FR-308, FR-314 |
| l10n_sv.iva.retention.rule | agent_basis, subject_scope | select / char | agent: grande · mediano · at_designated · card_issuer_administrator · mh · court_pagador · local_acquirer_nodomicile; subject: non_grand_contribuyente · any_category · uniones_hecho · unregistered_natural_person_agro_fin · afiliado · judgment_creditor | FR-303, FR-304, FR-306, FR-307, FR-308, FR-314, FR-316 |
| l10n_sv.iva.retention.rule | timing, enter_deadline | select / select | timing: causation_moment (tax point) · pay_credit_disposal (cards); deadline: art94_10_habiles_same_period · first_10_habiles_following_month | FR-304, FR-309, FR-315 |

**Agent/subject classification:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner (SV extension) | l10n_sv_at_category | select | grande · mediano · otra · none — accreditation source: tarjeta de contribuyente (LB-009) | FR-304, FR-306, FR-307, FR-308, FR-310 |
| res.partner (SV extension) | l10n_sv_at_retention_agent_designation | m2o / refs | AT designation act (date, act reference, reasoned limits — límites al agente); empty = not designated (config surface, OQ-3) | FR-306 |
| res.partner (SV extension) | l10n_sv_registration_exempt_provider, l10n_sv_opted_in | boolean / date | unregistered natural person exclusively in the inciso-7° catalog (excluded from registration); opt-in date flips retention 13%→1% | FR-308 |
| res.partner (SV extension) | l10n_sv_card_affiliate | boolean | afiliado: IVA contributor accepting card payments (162-A inciso 8° definition) | FR-314, FR-315 |
| res.partner (SV extension) | l10n_sv_non_domiciled | boolean | transferor/prestador without domicilio ni residencia in the country (CT 161 trigger) | FR-303 |

**Retention/perception events:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (SV extension) | l10n_sv_iva_retention_rule_id, l10n_sv_iva_retained_amount | m2o / monetary | resolved matrix row + computed retention (rate × ex-IVA base, floor-checked) | FR-304, FR-306, FR-307, FR-308 |
| account.move (SV extension) | l10n_sv_retention_tax_point_snapshot | date (stored) | the operation's resolved tax point = retention moment (D15 anchor; from the framework file's snapshot) | FR-309 |
| account.move (SV extension) | l10n_sv_retention_entero_state, l10n_sv_retention_entero_period | select / char | pending · declared · entered_integral (same-period gate facts consumed by SV-TAX-FR-256/257) | FR-304, FR-309, FR-317 |
| account.move (SV extension) | l10n_sv_mandamiento_ref | char | mandamiento de pago/ingreso reference for CT-161 self-liquidations | FR-303 |
| l10n_sv.iva.card.settlement (new) | affiliate, period, monto_sujeto, iva_percibido, dcle_ref | m2o / char / monetary / monetary / m2o | card 2% perception settlement record (issuer→affiliate); DCLE link (EINV 01-file by id); credit posts in the settlement period | FR-314, FR-315 |
| account.move (judgment/prize, SV extension) | l10n_sv_judgment_interest_retention, l10n_sv_formality_block | monetary / boolean | 162-B: 13% over liquidated interests (exempt-interest gate); adjudicación/remate blocked until AT payment; extrajudicial-inform event ref | FR-316 |
| account.move.line (purchase, SV extension) | l10n_sv_excluido_purchase_13pct_applies | boolean | FR-313 applicability flag consumed by Anexo 5 H (FREP 03-file by id) | FR-313 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = classification/timing/subject
computation logic living in the LGPL client. No SaaS rows are
introduced in this file: nothing here touches DTE generation or
transformation (the CRE/DCLE/NCE/NDE emission rows are e-invoicing's,
cited by id per `shared/docs/saas-thin-client-architecture.md` D2);
this file supplies the matrix resolution, the event ledger and the
applicability flags the client and the fiscal-reporting builders
consume. Model names are stable across Odoo 17/18/19/20 (`account.move`,
`account.move.line`, `res.partner`); version-specific behavior is
recorded per row where a legal vintage exists. D15 doctrine (binding):
retention values, floors and rates snapshot at the payment/retention
period; corrections use ORIGINAL-period parameters; CT article text is
implemented AS PRINTED (post-2017 watch, §2).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-303 | odoo | account.move + res.partner | obligado_al_pago flag + mandamiento_ref | CT 161: non-domiciled transferor/prestador ⇒ local acquirer owes the tax; mandamiento entero; venue DGII/Tesorería (Art. 94-IV); credit via SV-TAX-FR-257 gate |
| FR-304 | odoo | l10n_sv.iva.retention.rule + account.move.line | grandes 1% row | Ex-IVA base; $100.00 floor ("IGUAL O SUPERIOR A CIEN DÓLARES"); same-period entero within Art. 94's 10 first hábiles; D15 snapshot |
| FR-305 | odoo | account.move | CRE link + consign check | Retention documented per CT 112 → CRE (EINV 01-file SV-EINV-FR-034/035, CAT-006 22/C4/C9); supplier docs consign the retained value; separate registration (SV-TAX-FR-256 condition) |
| FR-306 | odoo | res.partner | agent_designation | AT-designated agents incl. state organs/municipalities/autonomous institutions (even non-contribuyentes); 1%; retain regardless of category save reasoned limits; list = config (OQ-3) |
| FR-307 | odoo | l10n_sv.iva.retention.rule | uniones 1% row | Grandes (natural/jurídica/sucesión/fideicomiso) buying from uniones/sociedades irregulares o de hecho ⇒ 1% indistintamente |
| FR-308 | odoo | l10n_sv.iva.retention.rule + res.partner | agro/finance 13% row | Grandes/medianos + inciso-7° catalog + unregistered natural person ⇒ 13% full tax; registration-exempt provider flag; opt-in flips to 1%; impuesto pagado → Fondo General (definitive, no provider credit) |
| FR-309 | odoo | account.move | tax_point_snapshot + entero_state | Retention at the causation moment (07-file tax points by id); entero although the provider is unpaid — never payment-contingent |
| FR-310 | odoo | res.partner | at_category + tarjeta ref | Grand quality accredited by the AT's distinguishable tarjeta de contribuyente; classification = administered data (onboarding load) |
| FR-311 | odoo | account.move | NC/ND adjustment path | Retention increases/decreases via NDE/NCE relating the CRE (EINV by id), per CT 110-1° circumstances; routes into 12-file Art. 62-63 windows; D15 original-period recompute |
| FR-312 | odoo | account.move | MH lottery retention event | 13% over the sale price of prize goods (Lotería Fiscal, CT 118) with MH as agent — awareness-level event feeding the entero/reporting surfaces |
| FR-313 | odoo | account.move.line | excluido_purchase_13pct_applies | The CT-119/162-side applicability the F-07 Anexo 5 H consumes (FREP 03-file SV-FREP-FR-086/089/091 by id); closes frep/03 OQ-004 (index task flips status); no invented extension (OQ-4) |
| FR-314 | odoo | l10n_sv.iva.card.settlement | 2% perception root | Card issuers/administrators (agent perceptores) retain 2% ex-IVA at pay/credit/disposal to afiliados; afiliado = contributor accepting cards; DCLE emission = EINV 01-file SV-EINV-FR-040 (by id) |
| FR-315 | odoo | l10n_sv.iva.card.settlement + account.move.line | affiliate credit + entero deadline | Anticipo = partial payment credited against the settlement period's determined tax; issuer enters sin deducción at DGT/MH banks within the 10 first hábiles; F-07 annex 6/11 reporting views by id |
| FR-316 | odoo | account.move | judgment-interest retention | Courts order 13% over liquidated interests (natural person inscrita o no; jurídicas salvo exempt); adjudicación/remate formality block; extrajudicial 15-day inform event |
| FR-317 | odoo | account.move | entero_state → credit gate | Declare+entero-same-period release gates consumed by id (TAX 10-file SV-TAX-FR-256/257; LB-015 pointer) — this file supplies the ledger facts, never restates the gate |
| FR-318 | odoo | reporting views | annex/F-930 feeds | F-07 Anexos 9-12 (SV-FREP-FR-104..108) + F-930 (SV-FREP-FR-111..114) + credit-side annexes (FR-086/089/091, FR-100/101/102/110) — all by id, no re-derivation |
| FR-319 | odoo | tax-line separation guard | IVA ≠ ISR lines | CT 154-160 matrix stays taxation/04 (SV-TAX-FR-121..131, by id); simultaneous retentions book as separate lines; LSI pair stays special-regimes (SV-SPE-FR-097/098) |

Version-regime notes (D12/D15): FR-304/308/314 carry the D15 snapshot
doctrine — retention values and floors resolve as-of the payment/
retention period with original-period correction parameters (the $100
floor and the 1%/2%/13% rates as printed in the 05_ consolidation).
The CT-vintage watch (§2) rides every CT-anchored row: the 05_ copy is
the Índice Legislativo edition with stamps through (22) — post-2017 CT
reforms possible; re-verify the matrix values against a current
official text at implementation. The SOQ-54 watch rides the 01_/02_
rows (LB-014/015).

## 6. Acceptance Criteria

- **AC-001:** Given a $150.00 ex-IVA purchase of goods by a GRANDE
  contribuyente from a small (non-grand) registered supplier, when the
  invoice posts, then the system books a 1% retention of $1.50 with a
  CRE comprobante referencing the operation, marks the entero due in
  the SAME period within the ten first hábiles of the following month,
  and the supplier's document consigns the retained value (FR-304,
  FR-305).
- **AC-002:** Given a purchase of $80.00 ex-IVA by a grande from a
  non-grand supplier, when the retention matrix resolves, then NO
  retention is booked (price under the $100.00 floor); given the same
  purchase at $100.00, then the 1% retention books (igual o superior a
  cien dólares) (FR-304).
- **AC-003:** Given a mediano contribuyente buying leche en estado
  natural from an UNREGISTERED natural person (sujeto excluido,
  registration-exempt provider), when the purchase posts, then the
  system retains 13% of the ex-IVA amount as the FULL tax, marks it
  impuesto pagado destined to the Fondo General del Estado, opens NO
  provider-side credit, and sets the excluido-purchase applicability
  flag consumed by the F-07 Anexo 5 H column (FR-308, FR-313).
- **AC-004:** Given the same leche seller OPTING to inscribe in the
  registry, when the retention matrix resolves post-inscription, then
  the retention flips to 1% (FR-308).
- **AC-005:** Given a grande's January card sales of $10,000.00
  (ex-IVA) with the issuer settling on 5-February (pay/credit to the
  afiliado), when the settlement posts, then the issuer perceives the
  2% anticipo ($200.00, ex-IVA base), enters it at the DGT/MH banks
  within the ten first hábiles of February, and the afiliado credits
  the $200.00 against the FEBRUARY determination — the period in which
  the anticipo was effected (FR-314, FR-315).
- **AC-006:** Given a foreign (non-domiciled) software provider billing
  a $5,000.00 service to a domiciled SV user utilizing it exclusively
  in-country, when the operation posts, then the ACQUIRER is obligado
  al pago, self-liquidates the IVA, enters it via the AT's mandamiento
  (DGII liquidation, Tesorería payment), and the credit releases ONLY
  through the mandamiento-referenced gate (FR-303; SV-TAX-FR-257 by
  id).
- **AC-007:** Given a grande's $500.00 service received from a UNION DE
  PERSONAS, when the matrix resolves, then the 1% retention books
  indistintamente of the union's classification (FR-307).
- **AC-008:** Given a grande's retained operation whose supplier
  remains UNPAID at period close, when the entero calendar runs, then
  the retention still enters (aunque no se haya realizado el pago
  respectivo al proveedor) and the credit-release gate sees the
  declared+entered state (FR-309, FR-317).
- **AC-009:** Given an ejecutivo-judgment sentence ordering payment of
  $2,000.00 interests to a natural-person creditor, when the liquidación
  executes, then the pagador retains 13% ($260.00) as the IVA on the
  interests; given the interests are exempt (juridical-creditor exempt
  gate), then NO retention books (FR-316).
- **AC-010:** Given judgment payment via remate of a good, when the
  adjudicación attempts to formalize before the beneficiary pays the
  AT the corresponding IVA, then the system holds the FORMALITY BLOCK
  (transfer/cesión not formalized) (FR-316).
- **AC-011:** Given a post-retention price increase of $200.00 on an
  AC-001 operation, when the adjustment posts, then an NDE relating
  the CRE documents the retention increase (CT 110-1° circumstances)
  at original-period parameters (FR-311).
- **AC-012:** Given goods destined as MH fiscal-lottery prizes
  purchased by the Ministerio de Hacienda, when the purchase posts,
  then MH retains 13% of the sale price as the IVA (FR-312).
- **AC-013:** Given one service carrying both an IVA 13% retention
  (this file) and an ISR 10% retention (taxation/04), when the
  retention lines book, then they remain SEPARATE tax lines under
  their own matrices and reporting surfaces — never a merged line
  (FR-319).
- **AC-014:** Given an AT designation act naming a MUNICIPALITY as
  retention agent with reasoned limits to operations above $5,000.00,
  when the designation loads, then the municipality retains 1% within
  its limits and skips operations outside them; given no designation
  loaded, then only the statutory grandes/medianos/CT-161 agents fire
  (FR-306).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage, 01_/02_): the Ley consolidation's last reform stamp is D.L. 71-2015 and the Reglamento's is D.E. 117-2001 — the Art. 94 plazo/venue and the Art. 65/Rgto. 23 pointer rows ride them; post-2015/post-2001 reforms unverified. Re-verify LB-014/LB-015 anchors at implementation. | no | Takumi S9 (sources registry) | open |
| OQ-2 | CT vintage (05_, SOQ-21 kin): the Código Tributario copy is the Índice Legislativo consolidation edition with reform stamps through (22) — post-2017 CT reforms are possible and unverified against a current official text; the Arts. 161/162/162-A/162-B matrix values (1%, 2%, 13%, $100 floor, 10-hábiles deadlines) print with stamps (1)/(3)/(5)/(9) as reproduced in §2. Re-verify the whole matrix at implementation (a later CT reform altering rates or the agent universe would rewrite FR-304..FR-319). | no | Takumi S9 (sources registry) | open |
| OQ-3 | AT-designation list config-gap: the inventory of designated retention agents (other contributors, state organs, dependencies, municipalities, autonomous institutions) and the grande/mediano classification itself are ADMINISTERED data absent from the corpus — FR-306/FR-310 ship them as configuration surfaces with no invented entries. Onboarding must load the real AT designation list and partner classifications before the matrix is trusted. | no | Takumi S9 + Odoo implementation | open |
| OQ-4 | Floor and family boundaries: (a) the $100 floor sentence sits in Art. 162 inciso 2° ("LA RETENCIÓN A QUE SE REFIERE ESTE ARTÍCULO…") — whether it governs ONLY the inciso-1° retention or the whole 1%-family (designated agents, uniones) is textual ambiguity; FR-304 applies it to the grande core rule and FR-307 to the uniones rule by reading, FR-306's designated agents pending confirmation; (b) the 13% inciso prints NO floor and NO ex-IVA clause — FR-308 applies 13% on the ex-IVA operation value by parity with inciso 2°; (c) the Anexo 5 H boundary — whether administered practice extends the 13% to excluded-subject purchases outside the inciso-7° catalog (FR-313 says no; corpus prints no other rule). Confirm all three with DGII practice/manual before final wiring. | no | Takumi S9 (CT re-anchor pass) + DGII practice | open |

Wiring note: FR-313 **closes frep/03 OQ-004** — the S3
`fiscal-reporting/03_f07-annexes-purchases.md` OQ register entry whose
applicability determination this file now owns (the S9/S3 index task
flips its status; OQ-4(c) above carries only the residual boundary
question, not the ownership gap).
