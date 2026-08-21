# SV — Taxation — IVA exports: 0% exportación, Art. 76 credits/offsets and the Art. 77 reintegro (Ley IVA Arts. 74-77; Rgto. Arts. 2, 29-30)

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | taxation |
| Status  | draft (S9 IVA-core wave, in review) |
| Authors | Takumi synthesis wave 9 + controller |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the export and refund
edge of El Salvador's IVA (D.L. 296-1992): the Art. 74 export definition —
definitive transfers of dominion of *bienes muebles corporales* destined to
use and consumption abroad, and services rendered in the country to users
without domicile or residence in it, destined to be utilized EXCLUSIVELY
abroad (Rgto. Art. 2 num. 10 vocabulary: the *envío legal* of mercancías in
libre circulación for definitive foreign use/consumption) — with the stamp-11
carve-out that the CONNECTION, CONTINUATION OR TERMINATION of services
originated abroad is NOT exclusive-foreign utilization and rates at the
Art. 54 13% (never 0%); the Art. 75 zero rate (a *tasa del cero por
ciento* — gravadas, never exempt: no débito, full credit rights), which is
the Ley-side routing authority consumed BY ID by the special-regimes TAN
sales to ZF/DPA (12_ Art. 25 co-cite) and the LSI export-definitiva route
(Arts. 75-77); the Art. 76 credit regime — export-activity credits netted
against the internal gravada débito of the same period, with the excess
carried to following periods until total extinction OR accredited, on the
taxpayer's request, against retained/perceived/import-generated IVA, other
direct taxes and fiscal obligations; the Art. 77 + Rgto. Art. 30 *reintegro*
(refund) workflow — request only after the period declaration, the
complete-file rule under DGII *Instructivos*, the 30-day resolution clock
with fiscalización suspension and *sin-lugar*-then-refile mechanics, the
omiso and zero-declaration-modification gates, *fehaciente* proof plus the
full purchases/credits and sales/débitos/exports detail in magnetic or
printed media, the mixed-exporter proportion (exports ÷ total gravadas
ventas) and pure-exporter rules with the 13%-of-export-value cap per
customs documents, the accumulation of unrefunded excess, the
export-period-only refund rule, the three-way export/local/common purchase
ledger with monthly percentage distribution by ventas and the Art. 66
adequacy for local exempt ventas, and the *reintegro* that never constitutes
*renta gravable*; and the Rgto. Art. 29 ZF/recintos export-equivalence
(transfers destined to the use and consumption of zona-franca and
recinto-fiscal companies deemed exportación, documented via *póliza de
exportación* or *declaración de mercancías* — with the D.L. 461-1990 anchor
stale-as-printed and the substance carried by 12_ Art. 25).

It does **not** cover: the 13% rate value and rate rows (Art. 54 — the
base/rate file of this wave owns them; the carve-out here only routes to
the standard rate, by pointer); credit eligibility and its gates (Arts.
62-65 — the credit file of this wave owns them; Art. 76 consumes the
eligible credit, by id); the Art. 66 pro-rata engine and the remanente
carryforward ledger (Arts. 66-67 — the pro-rata/remanente file of this
wave; FR-335 adequacy and FR-326 carryforward route INTO it, by id); the
retention/perception machinery that Art. 76 offsets consume (Arts. 161/162
CT — the retentions file of this wave, by id); the period determination row
(`l10n_sv.iva.period.determination`, adjustments/assets file of this wave,
by id — never restated here); the ZF/DPA/LSI fiscal-position routing
configuration (special-regimes SR5/SR3 files own it — SV-SPE-FR-087/095/
048/050/101 by id); the DUCA mechanics and FAUCA validity (SR6 by id);
the F-07 declaration engine and its casilla formulas (fiscal-reporting
files — casillas 90-94/93, 115 and 523/524 consumed by id); and FEXE
emission itself (`e-invoicing/01_document-types.md` SV-EINV-FR-001 — the
export invoice document type is cited by id, never restated).

## 2. Legal Basis

Authority order (binding, per master evidence index S9): **Ley = 01_**
(D.L. 296-1992, Asamblea Índice Legislativo consolidation through reform
(14) D.L. 71-2015, D.O. 146 T.408 14-Aug-2015; vigencia 1-sep-1992 per
Art. 175). **SOQ-54 vintage note (rides every 01_/02_ LB in this file):**
the consolidation's last reform stamp is D.L. 71-2015 — post-2015 reforms
unverified; corpus-internal signals negative (DTE stack 44_/45_,
Quincena-25 package 66_/67_, F-07 v14 manual silent); re-verify at
implementation. **Reglamento = 02_ survivors only** (D.E. 83-1992
consolidated through D.E. 60-1993/10-1996/**117-2001**; the mass repeal =
D.E. 117-2001 stamp (3) — ruling R30(a): repeal authority is the D.E., not
the Código Tributario); survivor articles = 1-10, 16-26, 29-30, 50-51 (+ 52
vigencia; corrected set per R30(a) addendum, 75_ Art. 147(b) audit
2026-08-20); this file cites Rgto. Arts. 2, 29, 30 — all survivors. **Stale
anchor (R30(a) kin):** Rgto. Art. 29 prints its ZF/recintos
export-equivalence "de conformidad con el Art. 26 del Decreto Legislativo
No. 461" of 1990 — superseded as law by D.L. 405-1998 (12_); the anchor is
carried as printed with note, the operative SUBSTANCE (deemed export +
documentary form) surviving via 12_ Art. 25 and Ley IVA Arts. 76/77 (SR5
by id). **CT re-anchor (live):** Art. 77 inciso 3º cites Art. 215 del
Código Tributario — a CURRENT cross-reference (verification faculty), not a
derogated anchor. **V1 citation rule:** every LB row below cites 01_, 02_
or the 12_ co-cite with the EVID id and the txt page anchor (`=== PAGE n
===` markers of `01_Ley_IVA.pdf.txt` / `02_Reglamento_IVA.pdf.txt`,
verified this task); the SOQ-54 watch rides all of them.

| LB | ID | Citation (Spanish) | English translation | Source file | Location |
|----|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley IVA, Art. 74 inciso 1º + Reglamento IVA, Art. 2 num. 10 | Art. 74: "ESTÁN AFECTAS A ESTAS NORMAS ESPECIALES, LAS EXPORTACIONES CONSISTENTES EN TRANSFERENCIAS DE DOMINIO DEFINITIVAS DE BIENES MUEBLES CORPORALES, DESTINADAS AL USO Y CONSUMO EN EL EXTERIOR Y LAS PRESTACIONES DE SERVICIOS REALIZADAS EN EL PAÍS, A USUARIOS QUE NO TIENEN DOMICILIO NI RESIDENCIA EN ÉL Y LOS SERVICIOS ESTÉN DESTINADOS A SER UTILIZADOS EXCLUSIVAMENTE EN EL EXTRANJERO. (1)" Rgto. Art. 2-10): "Exportación: El envío legal de mercancías que se encuentran en libre circulación, para su uso o consumo definitivo en el exterior y la prestación de servicios en el país a usuarios que no tienen domicilio ni residencia en él y que estén destinados a ser utilizados exclusivamente en el exterior." | Art. 74 (as incorporated): exports are the definitive transfers of dominion of corporal movable goods destined to use and consumption abroad, and the services rendered in the country to users without domicile or residence in it, the services destined to be utilized exclusively abroad. Reglamento: exportation is the legal shipment of goods in free circulation for their definitive use or consumption abroad, and the rendition of in-country services to users without domicile or residence in it, destined to be used exclusively abroad | `sv/sources/01_Ley_IVA.pdf` + `sv/sources/02_Reglamento_IVA.pdf` | Ley Art. 74 pp.37-38 (EVID-327; verified 01_ txt lines 1383-1394, PAGE 37-38); Rgto. Art. 2 num. 10 p.2 (EVID-333; verified 02_ txt lines 46-49, PAGE 2) |
| LB-002 | Ley IVA, Art. 74 inciso final (stamp 11) | "NO SE ENTENDERÁN UTILIZADOS EXCLUSIVAMENTE EN EL EXTRANJERO, LAS PRESTACIONES DE SERVICIOS REALIZADAS EN EL PAÍS, A USUARIOS QUE NO TIENEN NI DOMICILIO NI RESIDENCIA EN ÉL, CONSISTENTES EN LA CONEXIÓN, CONTINUACIÓN O TERMINACIÓN DE SERVICIOS ORIGINADOS EN EL EXTERIOR, EN CUYO CASO DEBE APLICARSE LA TASA ESTIPULADA EN EL ARTÍCULO 54 DE LA PRESENTE LEY. (11)" | Services rendered in the country to users without domicile or residence in it, consisting of the connection, continuation or termination of services originated abroad, shall NOT be understood as utilized exclusively abroad — in which case the rate stipulated in Art. 54 of this law (13%) must apply | `sv/sources/01_Ley_IVA.pdf` | Art. 74 final p.38 (EVID-327; verified 01_ txt lines 1395-1399, PAGE 38) |
| LB-003 | Ley IVA, Art. 75 | "Las exportaciones estarán afectas a una tasa del cero por ciento." | Exports are affected at a zero percent rate | `sv/sources/01_Ley_IVA.pdf` | Art. 75 p.38 (EVID-327; verified 01_ txt line 1401, PAGE 38) |
| LB-004 | Ley IVA, Art. 76 | "EL CRÉDITO FISCAL GENERADO AL ADQUIRIR BIENES Y AL UTILIZAR SERVICIOS NECESARIOS PARA REALIZAR LA ACTIVIDAD EXPORTADORA, PODRÁ DEDUCIRSE DEL DÉBITO FISCAL QUE SE ORIGINE POR LAS OPERACIONES INTERNAS GRAVADAS EN EL IMPUESTO, QUE TAMBIÉN PUDIERAN HABERSE REALIZADO EN EL MISMO PERÍODO TRIBUTARIO DE LA EXPORTACIÓN. (3)" "SI EL CRÉDITO FISCAL EXCEDIERE AL DÉBITO FISCAL DE DICHO PERÍODO, EL REMANENTE PODRÁ DEDUCIRSE EN LOS PERÍODOS TRIBUTARIOS SIGUIENTES HASTA SU TOTAL EXTINCIÓN, O TAMBIÉN PODRÁ ACREDITARSE CONTRA EL IMPUESTO QUE REGULA LA PRESENTE LEY, RETENIDO, PERCIBIDO O GENERADO EN LAS IMPORTACIONES DE BIENES, OTROS IMPUESTOS DIRECTOS U OBLIGACIONES FISCALES, SIEMPRE QUE ASÍ LO SOLICITARE EL INTERESADO. (3) (14)" | The fiscal credit generated on acquiring goods and utilizing services necessary to realize the exporting activity may be deducted from the débito fiscal originated by the internal taxed operations of the same period. If the credit exceeds that period's débito, the remanente may be deducted in following periods until its total extinction, or may also be accredited against the tax this law regulates — retained, perceived or generated at goods imports — other direct taxes or fiscal obligations, provided the interested party so requests | `sv/sources/01_Ley_IVA.pdf` | Art. 76 p.38 (EVID-328; verified 01_ txt lines 1402-1411, PAGE 38) |
| LB-005 | Ley IVA, Art. 77 incisos 1º-2º | "EN CASO DE QUE LOS CRÉDITOS FISCALES NO PUDIERAN DEDUCIRSE ÍNTEGRAMENTE DE LOS DÉBITOS FISCALES DURANTE EL PERÍODO TRIBUTARIO, EL EXPORTADOR QUE NO TUVIERE DEUDAS TRIBUTARIAS LÍQUIDAS, FIRMES Y EXIGIBLES COMPENSABLES CON DICHO CRÉDITO FISCAL, PODRÁ SOLICITAR A LA DIRECCIÓN GENERAL DE IMPUESTOS INTERNOS EL REINTEGRO DE DICHO SALDO REMANENTE. LA DIRECCIÓN GENERAL DEBERÁ ORDENAR MEDIANTE RESOLUCIÓN EL REINTEGRO EN UN PLAZO NO MAYOR DE TREINTA DÍAS CONTADOS A PARTIR DE LA FECHA DE PRESENTACIÓN DE LA SOLICITUD DE REINTEGRO. PARA EMITIR LA RESPECTIVA RESOLUCIÓN, NO SERÁ NECESARIA LA FISCALIZACIÓN PREVIA. EL CONTRIBUYENTE QUE SOLICITARE REINTEGROS INDEBIDOS SE SUJETARÁ A LAS ACCIONES PENALES CORRESPONDIENTES. EL REINTEGRO NO CONSTITUYE RENTA GRAVABLE.(1) (3) (11)" "EL PLAZO A QUE ALUDE EL INCISO ANTERIOR SE SUSPENDE CON LA NOTIFICACIÓN DE LA ADMINISTRACIÓN TRIBUTARIA DEL INICIO DE UNA FISCALIZACIÓN QUE COMPRENDA LOS PERÍODOS TRIBUTARIOS DE LOS CUALES SE HUBIERA SOLICITADO EL REINTEGRO DEL CRÉDITO FISCAL. EN CONSECUENCIA EL CÓMPUTO DEL PLAZO SE REANUDARÁ O CONTINUARÁ CORRIENDO A PARTIR DE LA FECHA EN QUE LA RESOLUCIÓN RESPECTIVA ADQUIERA ESTADO DE FIRMEZA. (11)" | Where the credits cannot be integrally deducted from the débitos during the period, the exporter holding no liquid, firm and enforceable tax debts compensable with that credit may request from DGII the refund of that remanente balance. DGII must order the refund by resolution within no more than THIRTY DAYS from the request's presentation date; prior fiscalización is not necessary to issue the resolution; improper refund claims subject the taxpayer to the corresponding penal actions; the refund does not constitute taxable income. The 30-day term SUSPENDS with the tax administration's notification of a fiscalización covering the periods whose credit refund was requested; the computation resumes or continues running from the date the respective resolution acquires firmness | `sv/sources/01_Ley_IVA.pdf` | Art. 77 incisos 1º-2º p.38 (EVID-329; verified 01_ txt lines 1412-1427, PAGE 38) |
| LB-006 | Ley IVA, Art. 77 inciso 3º (CT-215 verification) | "CUANDO LA ADMINISTRACIÓN TRIBUTARIA EJERZA SU FACULTAD DE VERIFICACIÓN DE SOLICITUD DE REINTEGRO, DE ACUERDO A LO ESTABLECIDO EN EL ARTÍCULO 215 DEL CÓDIGO TRIBUTARIO Y EL CONTRIBUYENTE NO PROPORCIONE LA INFORMACIÓN REQUERIDA POR LA ADMINISTRACIÓN TRIBUTARIA DENTRO DEL PLAZO QUE LA MISMA LE HUBIERE CONFERIDO PARA TAL EFECTO, DEBERÁ DECLARARSE SIN LUGAR LA SOLICITUD. EL CONTRIBUYENTE PODRÁ PRESENTAR NUEVAMENTE LA SOLICITUD DE REINTEGRO UNA VEZ TENGA DISPONIBLE LA INFORMACIÓN PARA CONTINUAR CON EL TRÁMITE DEL PROCEDIMIENTO. (11)" | When the tax administration exercises its verification faculty over a refund request per Art. 215 of the Tax Code and the taxpayer does not provide the required information within the term conferred, the request must be declared WITHOUT MERIT (*sin lugar*); the taxpayer may file the refund request anew once the information is available to continue the procedure | `sv/sources/01_Ley_IVA.pdf` | Art. 77 inciso 3º p.39 (EVID-329; verified 01_ txt lines 1435-1441, PAGE 39) |
| LB-007 | Ley IVA, Art. 77 procedure a)-b) | "EL PROCEDIMIENTO PARA LA VERIFICACIÓN DE REINTEGRO Y SU CÁLCULO, SE EFECTUARÁ DE ACUERDO A LO SIGUIENTE:(11)" "a) EL CONTRIBUYENTE PETICIONARIO, EN LOS CASOS QUE LA ADMINISTRACIÓN TRIBUTARIA LO REQUIERA, ESTARÁ OBLIGADO A COMPROBAR EN FORMA FEHACIENTE LAS OPERACIONES DE EXPORTACIÓN REALIZADAS Y LOS CRÉDITOS FISCALES, APORTANDO LA DOCUMENTACIÓN LEGAL CORRESPONDIENTE. (11)" "ASIMISMO, LOS CONTRIBUYENTES ESTARÁN OBLIGADOS AL MOMENTO DE PRESENTAR LA SOLICITUD RESPECTIVA, A PROPORCIONAR EL DETALLE DE TODAS LAS OPERACIONES DE COMPRAS Y CRÉDITOS FISCALES Y DE VENTAS Y DÉBITOS FISCALES Y EXPORTACIONES, EFECTUADAS EN EL PERÍODO A QUE CORRESPONDE LA SOLICITUD; EN MEDIOS MAGNÉTICOS O IMPRESOS; LOS MONTOS DE DICHO DETALLE DEBERÁN ESTAR CONFORMES A LOS REGISTROS Y A LA DOCUMENTACIÓN DE SOPORTE CORRESPONDIENTE. (11)" "b) HABER PRESENTADO PREVIO A LA SOLICITUD RESPECTIVA, LA DECLARACIÓN DEL PERÍODO TRIBUTARIO CORRESPONDIENTE DEL CUAL SOLICITA EL REINTEGRO DE CRÉDITO FISCAL Y NO ENCONTRARSE OMISO EN LA PRESENTACIÓN DE DECLARACIONES QUE POR LEY ESTÉ OBLIGADO. (11)" "EN AQUELLOS CASOS QUE EL CONTRIBUYENTE HUBIERE PRESENTADO DECLARACIONES CON CERO VALORES DE CUALQUIER TRIBUTO, PERO QUE COMO PRODUCTO DE LAS VERIFICACIONES QUE EFECTÚE LA ADMINISTRACIÓN TRIBUTARIA, SE DETERMINE LA REALIZACIÓN DE HECHOS GENERADORES, EL REINTEGRO SOLICITADO NO TENDRÁ LUGAR HASTA QUE DICHAS DECLARACIONES NO HAYAN SIDO MODIFICADAS. (11)" | The refund verification and calculation procedure: a) the petitioning taxpayer, where the administration so requires, must reliably (*fehaciente*) prove the export operations performed and the fiscal credits, furnishing the corresponding legal documentation; taxpayers must also, at the moment of filing, provide the detail of ALL purchases and fiscal credits and of sales and fiscal debits and exports effected in the period of the request, in magnetic or printed media, the amounts conforming to the records and support documentation; b) having presented, prior to the request, the declaration of the corresponding period, and not being OMISO (in default) in the presentation of declarations owed by law; where zero-value declarations were filed for any tax but the verifications determine hechos generadores, the requested refund shall not proceed until those declarations are modified | `sv/sources/01_Ley_IVA.pdf` | Art. 77 a)-b) p.39 (EVID-329; verified 01_ txt lines 1442-1464, PAGE 39) |
| LB-008 | Ley IVA, Art. 77 procedure c)-e) + inciso final | "c) EL EXPORTADOR QUE EFECTUARE TAMBIÉN TRANSFERENCIAS DE BIENES MUEBLES CORPORALES O PRESTACIONES DE SERVICIOS INTERNOS, SÓLO TENDRÁ DERECHO A REINTEGRO, SOBRE LA PARTE PROPORCIONAL DEL REMANENTE DE CRÉDITO FISCAL DEL PERÍODO TRIBUTARIO, VINCULADO A LA EXPORTACIÓN, PARA LO CUAL APLICARÁ EL PORCENTAJE QUE RESULTE DE DIVIDIR EL VALOR DE LAS EXPORTACIONES ENTRE LAS VENTAS TOTALES GRAVADAS DEL PERÍODO TRIBUTARIO CORRESPONDIENTE, EL CUAL NO PODRÁ EXCEDER DEL TRECE POR CIENTO (13%) DEL VALOR DE EXPORTACIÓN QUE CONSTE EN LOS DOCUMENTOS ADUANEROS RESPECTIVOS REALIZADA EN EL PERÍODO QUE CORRESPONDE; (11)" "d) EL EXPORTADOR QUE SÓLO EFECTUARE EXPORTACIONES, PODRÁ SOLICITAR COMO REINTEGRO EL TOTAL DE CRÉDITOS FISCALES DEL PERÍODO TRIBUTARIO, SIN QUE ÉSTOS EXCEDAN DEL TRECE POR CIENTO (13%) DEL VALOR DE EXPORTACIÓN QUE CONSTE EN LOS DOCUMENTOS ADUANEROS RESPECTIVOS; y, (11)" "e) [01_ prints a duplicated 'e)e)' marker — carried as note] LOS VALORES DE CRÉDITO FISCAL QUE NO FUEREN REINTEGRADOS EN UN PERÍODO TRIBUTARIO, POR EXCEDER DEL LÍMITE DEL TRECE POR CIENTO (13%) DEL VALOR DE EXPORTACIÓN QUE CONSTE EN LOS DOCUMENTOS ADUANEROS RESPECTIVOS, PODRÁN ACUMULARSE A LOS CRÉDITOS FISCALES DE LOS SIGUIENTES PERÍODOS TRIBUTARIOS, Y SER SUJETOS AL PROCEDIMIENTO DE CÁLCULO DE REINTEGRO ESTABLECIDO EN LOS LITERALES c) Y d) DE ESTE ARTÍCULO SEGÚN EL CASO.(11)" "EL REGLAMENTO ESTABLECERÁ LOS REQUISITOS, DOCUMENTACIÓN, PLAZOS, FORMAS Y PROCEDIMIENTOS PARA EFECTUAR LOS REINTEGROS A QUE SE REFIERE EL INCISO PRIMERO DE ESTE ARTÍCULO. (1) (3)" | c) the exporter who ALSO effects internal transfers of goods or service prestations is entitled to refund only over the PROPORTIONAL PART of the period's credit remanente LINKED TO EXPORTATION, applying the percentage resulting from dividing the value of exports by the TOTAL TAXED SALES of the corresponding period — which may not exceed THIRTEEN PERCENT (13%) of the export value appearing in the respective customs documents; d) the exporter who ONLY exports may request as refund the TOTAL fiscal credits of the period, provided they do not exceed the same 13%-of-export-value cap; e) credit values not refunded in a period for exceeding the 13% cap may ACCUMULATE to the fiscal credits of following periods and be subject to the c)/d) calculation procedure as corresponds [the 01_ txt prints a duplicated 'e)e)' marker — carried as note]; the Reglamento will establish the requirements, documentation, terms, forms and procedures for the refunds | `sv/sources/01_Ley_IVA.pdf` | Art. 77 c)-e) pp.39-40 (EVID-329; verified 01_ txt lines 1465-1493, PAGE 39-40) |
| LB-009 | Reglamento IVA, Art. 29 (stamp 1) + Ley de Zonas Francas (12_), Art. 25 co-cite | Rgto. Art. 29: "Para los efectos del Capítulo II del Título V de la Ley, de conformidad con el Art. 26 del Decreto Legislativo No. 461, del 15 de marzo de 1990, publicado en el Diario Oficial No. 88, Tomo 307 del 18 de abril del mismo año, se considerará como exportación la transferencia de dominio definitivo de bienes muebles corporales y la prestación de servicios destinados al uso y consumo de las empresas acogidas al Régimen de Zonas Francas y Recintos Fiscales." "Dicha exportación será documentada como tal, mediante la Póliza de Exportación o Declaración de Mercancías y los documentos de acompañamiento previstos en la legislación aduanera pertinente. Sin perjuicio de otras obligaciones que establezca la Dirección General. (1)" 12_ Art. 25 (first inciso, co-cite as the CURRENT authority via SR5 LB-003): "LAS VENTAS O TRANSFERENCIAS DE BIENES Y SERVICIOS QUE SEAN NECESARIOS PARA LA ACTIVIDAD AUTORIZADA, REALIZADAS POR PERSONAS NATURALES O JURÍDICAS ESTABLECIDAS EN EL TERRITORIO ADUANERO NACIONAL, A UN USUARIO DE ZONA FRANCA O A UN DPA, ESTARÁN AFECTAS A UNA TASA DEL CERO POR CIENTO DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS Y ADEMÁS, LES SERÁN APLICABLES LOS ARTÍCULOS 76 Y 77 DE LA LEY DE IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS." | Reglamento: for the purposes of Chapter II of Title V of the Law, per Art. 26 of D.L. 461 of 15-March-1990, the definitive transfer of dominion of corporal movable goods and the rendition of services destined to the use and consumption of companies under the Zonas Francas and Recintos Fiscales regime shall be considered EXPORTATION; said exportation is documented as such by the Export Permit (póliza de exportación) or Goods Declaration (declaración de mercancías) and the accompaniment documents foreseen in the pertinent customs legislation, without prejudice to other obligations the Dirección General establishes. 12_ Art. 25: sales or transfers of goods and services necessary for the authorized activity, made by persons established in the national customs territory to a ZF usuario or a DPA, are affected at the ZERO PERCENT rate of IVA, and Arts. 76 and 77 of the IVA Law are additionally applicable to them | `sv/sources/02_Reglamento_IVA.pdf` + `sv/sources/12_Ley_Zonas_Francas.pdf` | Rgto. Art. 29 p.8 (EVID-337; verified 02_ txt lines 270-279, PAGE 8); 12_ Art. 25 pp.29-30 (EVID-257 via SR5 LB-003; 12_ txt PAGE 29-30; SOQ-30 print) |
| LB-010 | Reglamento IVA, Art. 30 (stamps 1/2) | "Para los efectos del reintegro del crédito fiscal que regulan los Arts. 76 y 77 de la Ley, el contribuyente que realice la actividad exportadora, deberá presentar ante la Dirección General, la solicitud de devolución del remanente, previa presentación de la declaración del período correspondiente." "Se tendrá por presentada, toda solicitud de reintegro que reúna los requisitos acompañada de la documentación e información que establezca la Dirección General, por medio de Instructivos." "Para efectos de establecer el monto del crédito fiscal que corresponda reintegrar a aquellos contribuyentes que efectúan exportaciones y transfieren bienes o prestan servicios localmente, en su libro de compras deberán registrar separadamente, aquellas erogaciones que generen los créditos fiscales necesarios para realizar la actividad exportadora, de los identificados con las actividades locales. Los créditos fiscales que no sean plenamente identificables con ninguna de las actividades, también se registrarán separadamente, los cuales al final de cada período tributario, se distribuirán porcentualmente entre ambas actividades en relación a las ventas que cada una haya generado. En el caso que dichos contribuyentes también realicen ventas exentas localmente, deberán adecuar sus registros a los que establece el Art. 66 de la Ley." "De acuerdo al Art. 76 de la Ley, únicamente procederá la devolución respecto al período tributario de la exportación." "Cuando la Dirección General lo requiera, el contribuyente estará obligado a demostrar y comprobar en forma fehaciente la veracidad de los datos consignados en la solicitud de devolución. (1)(2)" | For the purposes of the credit refund regulated by Law Arts. 76 and 77, the exporting taxpayer must present to the Dirección General the remanente refund request, AFTER presentation of the corresponding period's declaration. A refund request is deemed filed only when it meets the requirements, accompanied by the documentation and information the Dirección General establishes through Instructivos. To establish the credit amount to refund taxpayers who export AND transfer goods or render services locally, the purchase ledger must separately register the outlays generating the credits necessary for the exporting activity and those identified with local activities; credits not plainly identifiable with either activity are also registered separately, and at the end of each period are distributed PERCENTUALLY between both activities in relation to the sales each generated; where such taxpayers also make local EXEMPT sales, they must adequate their records to those Art. 66 of the Law establishes. Per Art. 76 of the Law, the refund proceeds ONLY with respect to the tax period of the exportation. When the Dirección General requires it, the taxpayer must demonstrate and reliably prove the veracity of the data entered in the refund request | `sv/sources/02_Reglamento_IVA.pdf` | Rgto. Art. 30 p.8 (EVID-337; verified 02_ txt lines 280-301, PAGE 8) |

Dead text — never implementable as current law (recorded as notes, not FRs,
per wave constraints): the Rgto. Art. 29 anchor "Art. 26 del Decreto
Legislativo No. 461" (1990) is STALE as printed — that ZF/recintos law was
superseded by D.L. 405-1998 (12_); the anchor is never cited as live
authority, the export-equivalence substance surviving via 12_ Art. 25 +
Ley IVA Arts. 76/77 (SR5 by id; R30(a) note). The Art. 77-A/B/C zone and
everything Arts. 78-141 sit outside this file; the ~60 Ley articles
derogated by D.L. 230/00 are the CT re-anchor belt (only the LIVE CT-215
cross-reference of Art. 77-3º is used here). Rgto. non-survivors
(everything outside 1-10, 16-26, 29-30, 50-51 — corrected set, R30(a)
addendum) are per R30(a) derogated and never
cited. The 01_ txt prints a duplicated "e)e)" literal marker at Art. 77-e)
— a typographical defect carried as note, not law. The SOQ-54 vintage
watch (§2 preamble) applies to every row above.

## 3. Functional Requirements

### 3.1 The export definition and the zero rate (Arts. 74-75; Rgto. Art. 2-10)

- **SV-TAX-FR-320:** The system shall classify as *exportación* (Art. 74,
  with the Rgto. Art. 2 num. 10 vocabulary) exactly two operation families:
  (a) TRANSFERS OF DOMINION DEFINITIVE of *bienes muebles corporales*
  destined to use and consumption abroad — the reglamento test: *envío
  legal* of mercancías in *libre circulación* for definitive foreign
  use/consumption; and (b) SERVICES RENDERED IN THE COUNTRY to users who
  have NO domicile or residence in El Salvador, the services destined to be
  utilized EXCLUSIVELY abroad — recording on the operation BOTH limbs:
  the destination/use stamp (use_consumption_abroad ·
  exclusive_use_abroad) AND the user domicile/residence flags
  (non-domiciled, non-resident), each with its evidence source; the
  classification resolves AT THE TAX POINT (D15: the export/0% status is a
  tax-point-date snapshot on the record; corrections keep original-period
  parameters); the special-regimes consumers (LSI export test
  SV-SPE-FR-095; ZF/DPA routing SV-SPE-FR-087 — both by id) feed from this
  classification, never restated.
  (LB-001; EVID-327/333)
- **SV-TAX-FR-321:** The system shall implement the Art. 74 final-inciso
  carve-out as a BLOCKING classification: services rendered in the country
  to non-domiciled/non-resident users consisting of the *conexión,
  continuación o terminación de servicios originados en el extranjero*
  (connection, continuation or termination of foreign-originated services)
  are NOT utilized-exclusively-abroad — the export classification is
  refused and the Art. 54 rate applies (13%, rate row owned by the
  base/rate file of this wave, by pointer — this file only routes; a
  connected-services invoice NEVER resolves at 0%).
  (LB-002; EVID-327)
- **SV-TAX-FR-322:** The system shall apply to every classified export the
  Art. 75 ZERO PERCENT rate — a zero-rated GRAVADA status, never an
  exemption: no débito fiscal is generated, and credit rights survive
  intact (the Art. 76 machinery below); Art. 75 is the Ley-side routing
  authority consumed BY ID by the special-regimes routes: the TAN→ZF/DPA
  sale (12_ Art. 25 co-cite — necessary-for-activity goods/services at 0%
  with Arts. 76/77 applicable; exception lists route full 13%:
  `special-regimes/05_tan-iva-interface.md` SV-SPE-FR-087/088, by id) and
  the LSI export-definitiva route (Arts. 75-77 set:
  SV-SPE-FR-101 + export test SV-SPE-FR-095 + local-market caps
  SV-SPE-FR-048/050 — SR5/SR3 by id); the 0% *account.tax* row itself is
  the base/rate file's dated row (by id), selected here only through the
  export classifier.
  (LB-003; LB-009; EVID-327/257)
- **SV-TAX-FR-323:** The system shall emit every goods/services export
  invoice as the export document type — FEXE (factura electrónica de
  exportación, DTE type 11), never a consumer FE — with the export-0%
  tribute code (CAT-015 code C3), the emission surface owned by the
  e-invoicing file (`e-invoicing/01_document-types.md` SV-EINV-FR-001 and
  the per-type tributo restrictions SV-EINV-FR-017 — by id); this file
  supplies only the export classification that drives the type selection.
  (LB-001; LB-003; EVID-327)

### 3.2 ZF/recintos export-equivalence (Rgto. Art. 29)

- **SV-TAX-FR-324:** The system shall treat as exportación (deemed) the
  definitive transfer of dominion of bienes muebles corporales and the
  rendition of services destined to the use and consumption of companies
  under the Régimen de Zonas Francas y Recintos Fiscales — documented AS
  SUCH via the *póliza de exportación* or *declaración de mercancías* plus
  the accompaniment documents the customs legislation foresees (customs
  document reference recorded on the operation; other DGII obligations
  reserved) — with the D.L. 461-1990 anchor carried as STALE-as-printed
  (superseded by 12_ D.L. 405-1998; R30(a) note) and the operative
  substance resolved through the CURRENT authority: 12_ Art. 25 (0% +
  Arts. 76/77 for necessary goods/services) as encoded by SR5
  (SV-SPE-FR-087 by id — the necessity gate and exception lists live
  there); the DUCA/póliza terminology drift is carried as note (the modern
  DUCA-F/DM surface is SR6's, by id — OQ-2); the F-07 ZF/DPA tasa-cero
  sales casilla 93 is a consumer by id (SV-FREP-FR-004).
  (LB-009; EVID-337/257)

### 3.3 Export credits, carryforward and on-request offsets (Art. 76)

- **SV-TAX-FR-325:** The system shall net the export-activity crédito
  fiscal — the credit generated on acquiring goods and utilizing services
  NECESSARY to realize the exporting activity — against the débito fiscal
  originated by the internal gravadas operations that may also have been
  realized in the SAME period as the export (the same-period netting rides
  the period determination row `l10n_sv.iva.period.determination`
  introduced by the adjustments/assets file of this wave, by id — never a
  competing period model); the credit ELIGIBILITY machinery (formal
  requirements, gates, proportionalities) is the credit file's (by id);
  the export necessity of each purchase is a recorded destination
  classification feeding the three-way ledger of FR-335.
  (LB-004; EVID-328)
- **SV-TAX-FR-326:** Where the export-activity credit exceeds the period's
  internal débito, the system shall carry the remanente to following
  periods HASTA SU TOTAL EXTINCIÓN (indefinite carryforward on the
  remanente ledger owned by the pro-rata/remanente file of this wave,
  SV-TAX-FR-278 by id) — OR, exclusively upon the interested party's
  recorded request, credit it against: the IVA RETAINED, the IVA
  PERCEIVED, or the IVA GENERATED AT GOODS IMPORTS, plus OTHER DIRECT
  TAXES and FISCAL OBLIGATIONS — the offset election stored per request
  with its target-kind enumeration (iva_retenido · iva_percibido ·
  iva_import_generated · otro_impuesto_directo · obligacion_fiscal), never
  applied without the request; the retention/perception balances consumed
  are the retentions file's surfaces (by id).
  (LB-004; EVID-328)

### 3.4 The reintegro workflow (Art. 77; Rgto. Art. 30)

- **SV-TAX-FR-327:** The system shall implement the reintegro (refund)
  request: available only where the créditos fiscales could not be
  deducted ÍNTEGRAMENTE from the débitos during the period AND the
  exporter holds NO deudas tributarias líquidas, firmes y exigibles
  compensable with that credit (solvency precondition checked at filing);
  the request is addressed to DGII and the system shall track the
  statutory clock — resolution ordering the reintegro due within NO MORE
  THAN THIRTY DAYS counted from the request's PRESENTATION date — with
  the two printed riders: NO prior fiscalización is required to emit the
  resolution, and improper refund claims expose the claimant to PENAL
  actions (an improper-claim warning surface on the request, never a
  sanctioned-state engine); the refunded amount NEVER constitutes renta
  gravable (ISR-excluded posting on settlement — ISR file consumes, by
  pointer).
  (LB-005; EVID-329)
- **SV-TAX-FR-328:** The system shall suspend the 30-day resolution clock
  upon the notification of a fiscalización covering ANY of the periods
  whose credit refund was requested — a suspension event (fiscalización
  reference + notification date) freezing the clock — and shall resume or
  continue the computation from the date the respective resolution acquires
  ESTADO DE FIRMEZA (firmness date recorded; the deadline recomputes as
  elapsed-running-days + suspension interval, never extended de novo).
  (LB-005; EVID-329)
- **SV-TAX-FR-329:** The system shall implement the CT-215 verification
  gate: where DGII exercises its verification faculty and the taxpayer
  does NOT provide the required information within the conferred term, the
  request is declared SIN LUGAR (without merit) — a terminal-for-now
  state, NOT a denial on the merits — and the taxpayer may file the
  refund request NUEVAMENTE once the information is available, the refiled
  request linking to the sin-lugar original (lineage preserved; the new
  presentation date restarts the 30-day clock).
  (LB-006; EVID-329)
- **SV-TAX-FR-330:** The system shall enforce the Art. 77 a)-b)
  procedure gates on every refund request: (a) FEHACIENTE proof duty —
  where the administration requires it, the petitioning taxpayer must
  reliably prove the export operations performed and the fiscal credits,
  furnishing the corresponding LEGAL documentation (evidence attachments
  checklist on the request), plus the AT-FILING detail duty: the detail of
  ALL operations of compras y créditos fiscales AND ventas y débitos
  fiscales AND exportaciones of the request's period, EN MEDIOS MAGNÉTICOS
  O IMPRESOS, the amounts conforming to the books and the support
  documentation (a generated detail pack reconciled against the ledgers —
  mismatch blocks filing); and (b) the DECLARATION gates — the period's
  declaration must have been presented PRIOR to the request, the taxpayer
  must NOT be omiso in any declarations owed by law, and where zero-value
  declarations were filed for any tribute but verifications determine
  hechos generadores, the refund does NOT proceed until those declarations
  are MODIFIED (blocked-with-remediation state, re-evaluated on the
  modification event).
  (LB-007; EVID-329)
- **SV-TAX-FR-331:** The system shall enforce the Rgto. Art. 30
  procedural frame: the refund request is presentable only PREVIA
  presentación de la declaración del período correspondiente
  (declaration-first precondition — a January export cannot be refunded
  before January's declaration exists); under the COMPLETE-FILE rule a
  request is deemed FILED only when it meets the requirements and is
  accompanied by the documentation and information the DGII establishes
  por medio de Instructivos (the instructivo formats are a configuration
  surface — config-gap OQ-3, no formats invented); the refund proceeds
  ÚNICAMENTE respecto al período tributario de la exportación
  (per-period-only — a request never mints refunds attributable to other
  periods); and the taxpayer must demonstrate and prove FEHACIENTEMENTE
  the veracity of the data consigned in the request whenever the Dirección
  General requires it (on-demand verification surface).
  (LB-010; EVID-337)

### 3.5 The 13% cap computation — mixed and pure exporters (Art. 77 c)-e))

- **SV-TAX-FR-332:** For the MIXED exporter (one who ALSO effects internal
  transfers of bienes muebles corporales or internal service
  prestations), the system shall compute the refundable amount as the
  PROPORTIONAL PART of the period's remanente VINCULADO A LA
  EXPORTACIÓN: proportion = value of exports ÷ VENTAS TOTALES GRAVADAS of
  the corresponding period (snapshot from the frozen period values), and
  the resulting refund SHALL NOT EXCEED THE TRECE POR CIENTO (13%) OF THE
  EXPORT VALUE appearing in the respective CUSTOMS DOCUMENTS of the period
  — the customs-document export value (póliza/DM per FR-324; DUCA-F
  terminology-drift note OQ-2) is the cap base, never the invoiced value
  alone.
  (LB-008; EVID-329)
- **SV-TAX-FR-333:** For the PURE exporter (one who ONLY effects
  exports), the system shall compute the refundable amount as the TOTAL
  créditos fiscales of the period, under the SAME cap — never exceeding
  13% of the export value appearing in the respective customs documents.
  (LB-008; EVID-329)
- **SV-TAX-FR-334:** The system shall ACCUMULATE every credit value not
  refunded in a period for exceeding the 13% cap: the unrefunded excess
  carries into the créditos fiscales of the FOLLOWING periods and re-enters
  the same reintegro calculation procedure of FR-332/FR-333 as corresponds
  (mixed or pure, per the later period's own exporter profile) — an
  accumulation ledger distinct from the Art. 76 carryforward election of
  FR-326 (statutory post-cap continuation, not a taxpayer election).
  (LB-008; EVID-329)

### 3.6 Three-way purchase ledger and reporting consumers (Rgto. Art. 30; F-07)

- **SV-TAX-FR-335:** The system shall maintain the THREE-WAY purchase
  ledger for every exporting taxpayer: credits from outlays generating the
  créditos necessary for the EXPORTING activity registered SEPARATELY from
  those identified with the LOCAL activities, and credits not plainly
  identifiable with either activity (COMMON) registered separately too —
  the commons distributed PERCENTUALLY between both activities at the end
  of each period EN RELACIÓN A LAS VENTAS QUE CADA UNA HAYA GENERADO
  (monthly distribution run: export ventas ÷ (export + local) ventas, the
  split factors snapshotted per period); where the taxpayer ALSO makes
  local EXEMPT ventas, the records shall be ADEQUATED to those Art. 66 of
  the Ley establishes (the pro-rata engine of the pro-rata/remanente file
  of this wave, by id — never restated).
  (LB-010; EVID-337)
- **SV-TAX-FR-336:** The system shall feed the F-07 declaration surfaces
  by id (`fiscal-reporting/01_f07-declaration.md`): the export sales
  casillas — 90 (goods exports outside the Central American region), 91
  (within region), 94 (service exports) and 93 (ventas a Zonas Francas y
  D.P.A., tasa cero) — SV-FREP-FR-004 by id; casilla 115, reintegro de
  crédito fiscal IVA por exportaciones recorded in the period the
  resolution was NOTIFIED — SV-FREP-FR-012 by id; and the casilla 523/524
  pair, acreditación de reintegro de IVA exportador autorizado against
  the retentions block — SV-FREP-FR-024 by id; this file owns the amounts
  (classification, cap math, notification event), the F-07 engine owns
  the formulas.
  (LB-008; LB-010; EVID-329/337)
- **SV-TAX-FR-337:** The system shall compute every refund against the
  CLOSED period's FROZEN declaration values (D9 interplay: the
  proportion, the remanente and the customs-document export value are the
  period's declaration-time figures; later corrections require the
  declaration-modification event before any recomputation — kin to the
  FR-330 zero-declaration gate), and shall post the granted reintegro
  settlement EXCLUSIVELY on the credit/refund surfaces — never into
  renta gravable (FR-327 rider) and never as an offset absent the
  FR-326 request election.
  (LB-005; LB-008; LB-010; EVID-329/337)

## 4. Data Model

No dated legal TABLE vintages ship as CSV sidecars for this file (wave
constraint: NO CSV sidecars). The only dated parameters are the 0% and 13%
RATE rows (owned by the base/rate file, by id) and the 13% refund CAP — a
statutory constant printed inside Art. 77 c)/d)/e) (not an administered
row; SOQ-54 watch rides it). Layer semantics: this file introduces
Odoo-side classification/workflow data only (wave default `odoo`; see §5);
it REUSES `l10n_sv.iva.period.determination` (adjustments/assets file) as
the period row and the remanente ledger of the pro-rata/remanente file —
no competing period/ledger model is introduced.

**Export classification (stamps on the operation):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (SV extension) | l10n_sv_iva_export_kind | select (computed, stored) | goods_transfer_abroad · service_nondomiciled_exclusive · connected_services_13 (carve-out) · zf_recinto_deemed (Rgto. 29) | FR-320, FR-321, FR-324 |
| account.move (SV extension) | l10n_sv_iva_export_destination | select | uso_consumo_exterior (goods) · utilizacion_exclusiva_extranjero (services) — the destination limb | FR-320 |
| account.move (SV extension) | l10n_sv_iva_user_nondomiciled_nonresident | boolean (validated) | user without domicile or residence in SV — the user limb; both limbs required for export | FR-320 |
| account.move (export) | l10n_sv_iva_export_customs_doc_ref | char / m2o ref | póliza de exportación / declaración de mercancías / DUCA-F reference + accompaniment-doc links (cap base; SR6 terminology note) | FR-324, FR-332, FR-333 |
| account.move (SV extension) | l10n_sv_iva_export_status_snapshot | date + json | D15: export/0% status resolved at the tax point; snapshot of classifier inputs (destination, domicile, regime profile) | FR-320 |

**Export credit ledger (three-way):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move.line (purchase, SV extension) | l10n_sv_iva_export_ledger_bucket | select | export · local · common — common = not plainly identifiable with either activity | FR-325, FR-335 |
| l10n_sv.iva.common.distribution (new) | period, export_ventas, local_ventas, pct_export | char / monetary ×2 / float | monthly percentage distribution of commons EN RELACIÓN A LAS VENTAS generated by each activity; factors snapshotted per period | FR-335 |
| l10n_sv.iva.common.distribution | exempt_local_flag, art66_adequacy_ref | boolean / m2o | local exempt ventas ⇒ records adequated to Art. 66 (pro-rata engine of the remanente file, by id) | FR-335 |

**Offset and refund workflow:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.iva.export.offset.request (new) | kind, target_debt_ref, amount, requested_on | select / char / monetary / datetime | iva_retenido · iva_percibido · iva_import_generated · otro_impuesto_directo · obligacion_fiscal — Art. 76-2 on-request offset election | FR-326 |
| l10n_sv.iva.reintegro.request (new) | period, remanente_base, exporter_kind | char / monetary / select | exporter_kind: mixed · pure (per the period's own operations) | FR-327, FR-332, FR-333 |
| l10n_sv.iva.reintegro.request | export_value_customs_docs, proportion_pct, cap_13pct, requested_amount | monetary / float / monetary / monetary | proportion = exports ÷ ventas totales gravadas; cap = 13% × customs-doc export value; requested = min(proportional remanente or total credits, cap) | FR-332, FR-333, FR-337 |
| l10n_sv.iva.reintegro.request | state, filed_date, resolution_deadline, resolution_date, notification_period | select / date ×2 + datetime / date / char | draft · filed · in_verification · suspended_fiscalizacion · sin_lugar · blocked_omiso · blocked_zero_declaration · resolved · refiled; deadline = filed + 30 running days − suspension; notification_period feeds F-07 casilla 115 (SV-FREP-FR-012 by id) | FR-327, FR-328, FR-329, FR-330, FR-336 |
| l10n_sv.iva.reintegro.request | solvency_check, penal_exposure_warning, refiling_of | boolean / boolean / m2o | no líquidas-firmes-exigibles compensable debts at filing; improper-claim warning surface; refile links to the sin-lugar original | FR-327, FR-329 |
| l10n_sv.iva.reintegro.request | detail_pack_ref, detail_pack_reconciled | m2o / boolean (validated) | compras/créditos + ventas/débitos/exportaciones detail in magnetic-or-printed media form, reconciled to books (mismatch blocks filing) | FR-330 |
| l10n_sv.iva.reintegro.suspension (new) | request_id, fiscalizacion_ref, notified_date, firmeza_date | m2o / char / date / date | clock-suspension event; computation resumes/continues from firmeza | FR-328 |
| l10n_sv.iva.reintegro.accumulation (new) | period, unrefunded_excess, carried_to | char / monetary / char | post-cap excess accumulating to following periods' credits; re-enters c)/d) math per the later period's exporter profile | FR-334 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = classification/workflow/computation
logic living in the LGPL client. No SaaS rows are introduced in this file:
nothing here touches DTE generation/transformation (the FEXE emission is
the e-invoicing file's row, SV-EINV-FR-001/017 by id — this file supplies
the export classification that drives type selection); the DGII portal
transmission of the refund request is an external procedure — the system
models the request record, clock and gates, and exports the detail pack.
Model names are stable across Odoo 17/18/19/20 (`account.move`,
`account.move.line`; new light models `l10n_sv.iva.reintegro.*`,
`l10n_sv.iva.export.offset.request`, `l10n_sv.iva.common.distribution`);
the period row is REUSED from the adjustments/assets file
(`l10n_sv.iva.period.determination`, by id). D15 doctrine (binding): the
export/0% status and every refund input resolve as-of the tax point /
closed period and are snapshotted; D9: refund math runs against the frozen
declaration values.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-320 | odoo | account.move | export_kind + destination + user flags | Both limbs recorded; D15 tax-point snapshot; SR5 FR-095/087 consume by id |
| FR-321 | odoo | account.move | connected_services_13 carve-out | Connection/continuation/termination of foreign-originated services → Art. 54 rate (rate row = base/rate file, by pointer); NEVER 0% |
| FR-322 | odoo | account.move + account.tax (selection only) | 0% gravada status | Zero-rated ≠ exempt: credits survive; ZF/DPA route = SR5 FR-087/088 (12_ Art. 25); LSI route = SR5 FR-101 + FR-095 + SR3 FR-048/050 — all by id |
| FR-323 | odoo | account.move → DTE type selection | FEXE type 11 | Emission = EINV 01-file SV-EINV-FR-001; CAT-015 C3 restriction = SV-EINV-FR-017 (by id) |
| FR-324 | odoo | account.move | zf_recinto_deemed + customs_doc_ref | Rgto. 29; D.L. 461 anchor stale-as-printed (R30(a)); substance via 12_ Art. 25 = SR5 FR-087 by id; DUCA-F drift = SR6 by id (OQ-2); casilla 93 = SV-FREP-FR-004 by id |
| FR-325 | odoo | account.move.line + l10n_sv.iva.period.determination (reuse) | export_ledger_bucket + same-period netting | Credit eligibility = credit file (by id); necessity recorded; period row REUSED from adjustments/assets file — no competing model |
| FR-326 | odoo | l10n_sv.iva.export.offset.request | offset election | Carryforward = remanente file SV-TAX-FR-278 by id; offsets (retained/perceived/import IVA, direct taxes, fiscal obligations) ONLY on recorded request; retention balances = retentions file by id |
| FR-327 | odoo | l10n_sv.iva.reintegro.request | eligibility + 30-day clock + solvency | No prior fiscalización required (rider recorded); penal-exposure warning surface; reintegro ≠ renta gravable (ISR posting exclusion, by pointer) |
| FR-328 | odoo | l10n_sv.iva.reintegro.suspension | notified_date → firmeza_date | Clock recomputes elapsed-days + suspension interval; never restarted de novo |
| FR-329 | odoo | l10n_sv.iva.reintegro.request | sin_lugar → refiled lineage | CT-215 gate; refile links to original; new presentation date restarts the clock |
| FR-330 | odoo | l10n_sv.iva.reintegro.request | detail_pack + declaration gates | Fehaciente checklist; magnetic/printed detail reconciled to books; declaration-first, no-omiso, zero-declaration-modification blocks |
| FR-331 | odoo | l10n_sv.iva.reintegro.request | declaration-precondition + complete-file + per-period-only | Instructivo formats = config surface (OQ-3); refund only for the export's period |
| FR-332 | odoo | l10n_sv.iva.reintegro.request | proportion + 13% cap (mixed) | exports ÷ ventas totales gravadas; cap = 13% × customs-doc export value; frozen-period inputs (D9) |
| FR-333 | odoo | l10n_sv.iva.reintegro.request | total credits + 13% cap (pure) | Pure exporter = only exports in the period |
| FR-334 | odoo | l10n_sv.iva.reintegro.accumulation | post-cap excess carry | Statutory continuation into following periods; re-enters FR-332/333 math per later exporter profile; distinct from FR-326 election |
| FR-335 | odoo | account.move.line + l10n_sv.iva.common.distribution | three-way ledger + monthly split | Commons distributed by ventas percentages; Art. 66 adequacy = pro-rata/remanente file by id |
| FR-336 | odoo | l10n_sv.iva.reintegro.request → l10n_sv.f07.casilla.value | casilla feeds | 90/91/94/93 = SV-FREP-FR-004; 115 = SV-FREP-FR-012 (notification period); 523/524 = SV-FREP-FR-024 — all by id; F-07 engine owns formulas |
| FR-337 | odoo | l10n_sv.iva.reintegro.request | frozen-values computation + settlement | D9: frozen declaration values; recomputation only on declaration-modification event; settlement never into renta gravable |

Version-regime notes (D12/D15/D9): FR-320 snapshots the export/0% status
at the tax point (original-period parameters on correction); FR-332/333/
337 compute against the closed period's frozen values (declaration-time
figures; later corrections route through the declaration-modification
event). The 13% cap is a statutory constant as printed (SOQ-54 watch
rides the 01_ print); the instructivo-driven request formats are a
configuration surface (OQ-3). The SOQ-54 consolidation watch rides every
LB (§2 preamble) — re-verify against a current official consolidation at
implementation.

## 6. Acceptance Criteria

- **AC-001:** Given a mixed exporter whose period ventas totales gravadas
  are $250,000.00 with exports of $100,000.00 (40%) and a remanente of
  $100.00 linked to exportation, when the refund computes, then the
  refundable proportional part is 40% × $100.00 = $40.00, further capped
  at 13% × $100,000.00 = $13,000.00 (cap not binding) — and any excess
  over the cap would accumulate per AC-008 (FR-332, FR-334).
- **AC-002:** Given an invoice for connection/continuation/termination
  services originated abroad (foreign telecom) rendered in-country to a
  non-domiciled, non-resident user, when classification runs, then the
  export classification is REFUSED and the Art. 54 rate of 13% applies —
  the invoice never resolves at 0% and never emits as FEXE on the 0%
  tribute code (FR-321, FR-323).
- **AC-003:** Given an exporter who is OMISO in the presentation of any
  declaration owed by law, when a refund request is attempted, then the
  request is BLOCKED with the omiso gate until the default is cured
  (FR-330).
- **AC-004:** Given a January export with January's declaration not yet
  presented, when the refund request is attempted, then filing is refused
  (Rgto. Art. 30 declaration-first precondition); once January's
  declaration exists, the same request files and its 30-day clock starts
  at the presentation date (FR-331, FR-327).
- **AC-005:** Given a refund request filed 1-March with a fiscalización
  covering the requested periods notified 10-March and its resolution
  firm 20-April, when the deadline resolves, then the clock ran 1-9 March
  (9 days), suspended 10-March→19-April, and resumed 20-April for the
  remaining 21 days — deadline 11-May, never a de-novo 30 days (FR-328).
- **AC-006:** Given a verification requirement whose conferred term
  expires without the information provided, when the gate evaluates, then
  the request is declared SIN LUGAR and a refiled request (once the
  information is available) links to the original with a fresh
  presentation date and clock (FR-329).
- **AC-007:** Given a taxpayer who filed zero-value declarations for any
  tribute where verifications determine hechos generadores, when the
  refund evaluates, then it does NOT proceed until those declarations are
  modified — the block re-evaluates on the modification event (FR-330).
- **AC-008:** Given a pure exporter with period credits of $2,000.00 and
  a customs-document export value of $10,000.00 (cap $1,300.00), when the
  refund computes, then $1,300.00 is refundable and the $700.00 excess
  ACCUMULATES to the following periods' credits, re-entering the same
  c)/d) math of that later period's exporter profile (FR-333, FR-334).
- **AC-009:** Given a period with export ventas $60,000.00, local ventas
  $40,000.00 and common credits $500.00, when the monthly distribution
  runs, then $300.00 of the commons is distributed to the export bucket
  (60%) and $200.00 to the local bucket (40%), the factors snapshotted
  for the period (FR-335).
- **AC-010:** Given an exporting taxpayer also making local EXEMPT
  ventas, when the records resolve, then the purchase-ledger records are
  ADEQUATED to the Art. 66 surfaces of the pro-rata engine (by id) — the
  three-way split and the Art. 66 pro-rata coexist (FR-335).
- **AC-011:** Given a granted reintegro of $1,300.00, when the
  settlement posts, then the amount NEVER enters renta gravable (ISR
  exclusion rider) and is recorded in the notification period feeding F-07
  casilla 115 (SV-FREP-FR-012 by id) (FR-327, FR-336).
- **AC-012:** Given a TAN sale of necessary goods to a ZF usuario
  documented by DUCA-F/DM, when the operation resolves, then it is the
  deemed export of Rgto. Art. 29 via the CURRENT 12_ Art. 25 authority
  (SR5 SV-SPE-FR-087 by id — 0% with Arts. 76/77), the customs document
  reference is recorded as cap base, and the sale feeds F-07 casilla 93
  (SV-FREP-FR-004 by id) (FR-324, FR-322).
- **AC-013:** Given a refund request whose computed amounts would draw on
  a period OTHER than the export's own period, when validation runs, then
  the request is rejected — the refund proceeds ÚNICAMENTE respecto al
  período tributario de la exportación (FR-331, FR-337).
- **AC-014:** Given a goods export outside the Central American region
  and a service export in the same period, when the F-07 feeds resolve,
  then the sales enter casillas 90 and 94 respectively (casilla 91 for
  within-region goods; all SV-FREP-FR-004 by id) with the amounts from
  the frozen period values (FR-336, FR-337).
- **AC-015:** Given an export-activity credit exceeding the same period's
  internal gravada débito with no refund or offset request filed, when
  the period closes, then the remanente carries to the following periods
  on the remanente ledger (SV-TAX-FR-278 by id) until total extinction;
  given instead a recorded offset request against IVA percibido, then
  only the requested amount offsets that target (FR-325, FR-326).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-54 (vintage): the 01_ consolidation's last reform stamp is D.L. 71-2015 and the 02_ Reglamento's is D.E. 117-2001 — post-2015/post-2001 reforms unverified until an official current consolidation is acquired; corpus-internal signals negative (DTE stack 44_/45_, Quincena-25 package 66_/67_, F-07 v14 manual all silent on later IVA-core reforms). Re-verify Arts. 74-77 + Rgto. Arts. 2/29/30 (and the 13% cap constant) at implementation; the watch rides every LB of this file (§2). | no | Takumi S9 (sources registry) | open |
| OQ-2 | Terminology drift — customs documents: Rgto. Arts. 29/30 print "Póliza de Exportación o Declaración de Mercancías" (1992 vocabulary); the modern operative surface is the DUCA family (DUCA-F for Central-American-origin goods — SR6 `06_duca-customs-docs.md` by id; the Rgto. Art. 18 FX-rate anchor already rides the "aceptación de la póliza o formulario aduanero" print, SOQ-45 kin). Confirm the DGII-accepted document set feeding the 13% cap's "valor de exportación que conste en los documentos aduaneros" (DM field of the DUCA-F?) before wiring the cap base extraction. | no | Takumi S9 + Odoo implementation | open |
| OQ-3 | DGII Instructivo formats (config-gap): Rgto. Art. 30's complete-file rule conditions "presented" status on the documentation/information the DGII establishes "por medio de Instructivos" — the refund-request formats (media, layouts, magnetic-file specifications) are outside the corpus. The request model ships the checklist and the detail-pack reconciliation as a CONFIGURATION surface; onboarding must load the real instructivo formats before the complete-file gate is trusted. | no | Takumi S9 + Odoo implementation | open |
| OQ-4 | Offset mechanics detail: Art. 76-2 allows accrediting the remanente against IVA retenido/percibido/import-generated, "otros impuestos directos u obligaciones fiscales ... siempre que así lo solicitare el interesado" — the application PROCEDURE (whether via CT compensation rules Art. 74-A zone, per-debt applications, or a DGII determination) is not in the corpus; FR-326 records the election and targets, but the settlement mechanics against each target kind need CT-practice confirmation at implementation. | no | Takumi S9 (CT re-anchor pass) | open |
