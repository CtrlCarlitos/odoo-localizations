# SV — Special regimes — Customs clocks: admisión temporal, traslados, destinación, expedición

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes) |
| Updated | 2026-08-19 |

## 1. Purpose

This file times the goods: it owns the customs clocks of the three regimes —
the ZF/DPA *admisión temporal para perfeccionamiento activo* (temporary
admission for active perfecting) tracker of DOCE (12) MESES IMPRORROGABLES
(twelve months non-extendable) per *declaración de mercancías* (goods
declaration, DM) acceptance (12_ Art. 22), with its *traslado* (inter-site
goods transfer) sub-clocks (definitive ≤12m from first admisión; temporales
≤6m within the 12m envelope; ZF→DPA ≤12m from the ZF-cancelling DM
liquidación; ZF/DPA→TAN temporales 2 meses; *formalización* formalization
≤3 días hábiles after ingreso; NOTA DE REMISIÓN on non-dominion traslados);
the TAN→ZF/DPA passive-processing reimport clock (≤6 months, duties only on
the non-national value-added aggregate, NMF tariff); and the LSI clock
family — parque permanencia INDEFINITE (liberatorio character), centros
materias-primas/insumos 1 year, capital goods *liquidados a franquicia
definitiva*, **admisión temporal 24 MESES CALENDARIO (veinticuatro meses
calendario, twenty-four calendar months) prorrogable in +1-year periods with
prior DGA authorization** (14_ Art. 33), the 20-días-hábiles *destinación*
(customs-destination election) window post-discharge whose expiry ⇒
*abandono* (abandonment), the regímenes-optables menu (14_ Art. 34), the
*expedición* (dispatch) status window ≤20 días hábiles post-DM with its
information duty, the storage/conservation customs-value exclusion,
Certificados de Control Aduanero records, the residuales disposition paths
(valor facturado + DM simplificada; botaderos free; donations MINEC +
Asamblea), and the DUCA linkage (the "fecha de vencimiento del régimen"
field feeding these clocks; DUCA-F 30-días-hábiles validity in its FAUCA
role, export-country only). **THE invariant of this file: the ZF/DPA
12-MONTH IMPRORROGABLE clock and the LSI 24-MONTH PRORROGABLE clock are
DISTINCT regime clock rows, NEVER unified** (SV-SPE-FR-065).

It does **not** cover: the exemption ladders and exception-goods gates
(`02_zf-exemption-schedules.md`); the LSI exemption shapes, caps and
dictamen (`03_lsi-regime.md`); the TAN internación duty bases, 0%-IVA
routing, market-price rules and retention values (`05_tan-iva-interface.md`
— incl. 12_ Art. 27 materia-prima TAN consumption and 14_ Art. 26 TAN→
parque/centro exportación-definitiva routing); the DUCA record model,
teledespacho chassis, $18 tasa and presumed valuation
(`06_customs-declarations.md` — T6, cited by id/forward reference); the
descargo/cancellation registers and sanction ladders
(`07_obligations-reporting-sanctions.md`); FOVIAL/COTRANS
(`08_fovial-cotrans.md`). This file consumes Task 1's regime discriminators
and profile (SV-SPE-FR-001/002/003 by id), the fiscal-reporting días-hábiles
engine (SV-FREP-FR-202..204 by id) and the e-invoicing NRE document types
(SV-EINV-FR-001/026 by id) — never restating any of them.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): ZF/DPA clocks =
**12_** (D.L. Nº 405, 3-sep-1998, D.O. N° 176 T.340 23-sep-1998; consolidated
through reform (8) D.L. 318-2013; content title "Ley de Zonas Francas
Industriales y de Comercialización"); LSI clocks = **14_** (D.L. Nº 431,
11-oct-2007, D.O. N° 199 T.377 25-oct-2007; 2007 print, header "Reformas:
S/R"); DUCA field anchors = **43_** (Anexo II de la Resolución No. 409-2018
(COMIECO-LXXXV), Instructivo de llenado DUCA; 2018 print assumed current —
SOQ-36). Pointer LBs of this file: the NRE document surface = e-invoicing by
id (SV-EINV-FR-001 doc type 04 / SV-EINV-FR-026 goods-transfer document);
días-hábiles arithmetic = SV-FREP-FR-202..204 by id; the DUCA record model
owning the mirrored fields = `06_customs-declarations.md` (T6 forward
reference, resolved at final review per S2/S3 precedent ruling 24); the
per-DM descargo/cancellation registers consuming these clocks =
`07_obligations-reporting-sanctions.md` by id.

**SOQ-30 verification note (rides EVERY regime LB in this file):** the 12_
consolidation ends at D.L. 318-2013 and 14_ is the 2007 print with no reform
block ("Reformas: S/R") — post-cutoff reforms are unverified until official
routes recover (SOQ-22 kin; D.L. 598-2020-era traffic may have touched the
regimes); article text is cited **as printed** (12_ prints Arts. 22 onward
in UPPERCASE; 14_ prints sentence case — casing preserved). Verbatim text
below is copied from the W13 evidence files (EVID-257/263/272) and, where
the evidence abbreviates, from the extraction txts
`sv/.extractions/12_Ley_Zonas_Francas.pdf.txt`,
`sv/.extractions/14_Ley_Servicios_Internacionales.pdf.txt` and
`sv/.extractions/43_DUCA_Instructivo_COMIECO.pdf.txt` (citable per standing
S3 ruling 25; page pointers = txt PAGE markers). D15 discipline: every clock
duration, window and unit in this file is a dated config row keyed by clock
kind with instrument provenance — never a global constant; each running
clock resolves as-of its own anchor (DM acceptance, DM liquidación,
traslado date, ingreso, discharge, DM registration or emission) and
snapshots on the record.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Zonas Francas, Art. 21: "El Régimen de Zona Franca será el régimen aduanero que normará el ingreso de todos los bienes señalados en el artículo 17 de esta Ley, introducidos por los Usuarios de Zona Franca y por tiempo de permanencia indefinido en la misma. … las empresas Usuarias deberán presentar una Declaración de Mercancías de Zona Franca. En lo que respecta a los Depósitos para Perfeccionamiento Activo, el régimen aduanero que normará la admisión de los bienes señalados en el literal b) del art. 19 de esta Ley, será el de Admisión Temporal para Perfeccionamiento Activo. La importación definitiva de los bienes señalados en los literales a) y c) del art. 19 de esta Ley, se autorizarán mediante la presentación de una Declaración de Importación Definitiva a Franquicia, con excepción de aquellos bienes que se hubieren internado bajo la modalidad de arrendamiento o cualquier otra que no implique transferencia de dominio, los cuales deberán declararse bajo el Régimen de Admisión Temporal para Perfeccionamiento Activo." | The ZF regime governs the entry of all Art. 17 goods introduced by ZF usuarios with INDEFINITE permanence — a ZF goods declaration (DM) is presented. For DPAs, the customs regime governing admission of the Art. 19 b) goods (raw materials, parts, packaging under suspension) is Admisión Temporal para Perfeccionamiento Activo; the definitive importation of Art. 19 a)/c) goods (capital goods; lubricants/catalysts/fuels) is authorized by a Declaración de Importación Definitiva a Franquicia (definitive-import declaration under franchise) — EXCEPT goods introduced under leasing or any other modality NOT implying transfer of dominion, which must be declared under the admisión-temporal-perfeccionamiento-activo regime (i.e. they take the Art. 22 clock) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 21 p.27 (EVID-257; txt PAGE 27; SOQ-30 print) |
| LB-002 | Ley de Zonas Francas, Art. 22: "EL PLAZO DE PERMANENCIA DE LOS BIENES INTRODUCIDOS PARA SU PERFECCIONAMIENTO AL AMPARO DEL RÉGIMEN DE ADMISIÓN TEMPORAL PARA PERFECCIONAMIENTO ACTIVO, SERÁ DE HASTA DOCE (12) MESES IMPRORROGABLES, CONTADOS A PARTIR DE LA ACEPTACIÓN DE LA DECLARACIÓN DE MERCANCÍAS. EL PLAZO DE LOS TRASLADOS SE DEFINE DE LA SIGUIENTE MANERA: a) PARA LOS TRASLADOS DEFINITIVOS: HASTA DOCE (12) MESES CONTADOS A PARTIR DE LA FECHA EN QUE LAS MERCANCÍAS INGRESARON POR PRIMERA VEZ AL RÉGIMEN DE ADMISIÓN TEMPORAL, POR MEDIO DE LA ACEPTACIÓN DE LA DECLARACIÓN DE MERCANCÍAS; b) PARA LOS TRASLADOS TEMPORALES: HASTA SEIS (6) MESES CONTADOS A PARTIR DE LA FECHA DEL TRASLADO DE LAS MERCANCÍAS QUE CONSTE EN EL DOCUMENTO EMITIDO PARA TAL FIN; SIEMPRE QUE DICHO PLAZO NO EXCEDA EL CÓMPUTO TOTAL DEL PLAZO DE LOS DOCE MESES EN EL CASO DE LOS DPA; c) PARA LOS TRASLADOS DEFINITIVOS DE UNA ZONA FRANCA A UN DPA: HASTA DOCE (12) MESES CONTADOS A PARTIR DE LA FECHA DE LIQUIDACIÓN DE LA DECLARACIÓN DE MERCANCÍAS QUE CANCELA EL RÉGIMEN DE ZONAS FRANCAS, PARA LO CUAL EL DPA DEBERÁ DE TRANSMITIR LA DECLARACIÓN DE MERCANCÍAS CORRESPONDIENTE A LA DELEGACIÓN DE ZONA FRANCA PARA LA SALIDA DE LAS MISMAS. LO DISPUESTO EN EL LITERAL b) DEL INCISO ANTERIOR ES TAMBIÉN APLICABLE A LOS TRASLADOS REALIZADOS POR USUARIOS DE ZONAS FRANCAS. EL INCUMPLIMIENTO DE LOS PLAZOS ANTERIORES DARÁ COMO CONSECUENCIA LA OBLIGACIÓN DEL PAGO DE LOS TRIBUTOS CORRESPONDIENTES Y LAS SANCIONES QUE DE CONFORMIDAD A LA LEGISLACIÓN CORRESPONDIENTE LES SEAN APLICABLES." | The permanence term of goods introduced for perfecting under the admisión-temporal-perfeccionamiento-activo regime is UP TO (de hasta) TWELVE (12) MONTHS NON-EXTENDABLE (improrrogables), counted from the ACCEPTANCE of the goods declaration (DM). Traslado terms: a) definitive traslados — up to 12 months from the date the goods first entered the admisión-temporal regime via DM acceptance; b) temporary traslados — up to SIX (6) months from the traslado date recorded in the document emitted for that purpose, PROVIDED the term does not exceed the total computation of the twelve months in the case of DPAs; c) definitive traslados from a zona franca to a DPA — up to 12 months from the LIQUIDATION date of the DM that cancels the zonas-francas regime (the DPA transmits the corresponding DM to the zona-franca delegation for the goods' exit); literal b) also applies to traslados by ZF usuarios. Breach of these terms results in the OBLIGATION TO PAY the corresponding tributes and the sanctions applicable under the corresponding legislation | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 22 incs. 1-2 pp.27-28 (EVID-257; txt PAGE 27-28; SOQ-30 print) |
| LB-003 | Ley de Zonas Francas, Art. 22 (continuation): "LOS TRASLADOS SE REALIZARÁN UTILIZANDO LOS FORMATOS Y MEDIOS FÍSICOS Y ELECTRÓNICOS QUE AL EFECTO ESTABLEZCA LA DIRECCIÓN GENERAL DE ADUANAS, MEDIANTE DISPOSICIONES ADMINISTRATIVAS DE CARÁCTER GENERAL. PARA AQUELLOS TRASLADOS QUE NO IMPLIQUEN TRANSFERENCIA DE DOMINIO, DEBERÁ EMITIRSE ADEMÁS UNA NOTA DE REMISIÓN. CONSTITUYE CASO ESPECIAL EN EL CUAL NO HAY TRANSFERENCIA DE DOMINIO, CUANDO EL TRASLADO A OTRO BENEFICIARIO SE REALIZA POR ORDEN DEL CONTRATISTA DEBIDAMENTE COMPROBADA. PARA AQUELLOS BIENES QUE SE HUBIEREN ADMITIDO TEMPORALMENTE Y QUE NO IMPLIQUE TRANSFERENCIA DE DOMINIO, LOS CONTRATOS RESPECTIVOS DETERMINARÁN SU PERMANENCIA BAJO EL RÉGIMEN DE ADMISIÓN TEMPORAL PARA PERFECCIONAMIENTO ACTIVO, EL CUAL NO PODRÁ SER MAYOR A DOCE MESES. EL PLAZO PARA REALIZAR LAS FORMALIZACIONES Y/O CONFIRMACIONES A LOS BENEFICIARIOS DE LA LEY SERÁ DE HASTA TRES DÍAS HÁBILES DESPUÉS DEL INGRESO DE LAS MERCANCÍAS, LAS CUALES DEBERÁN PERMANECER A DISPOSICIÓN DE LA ADUANA HASTA QUE SEA OTORGADO EL LEVANTE CONFORME LO DISPUESTO EN EL CÓDIGO ADUANERO UNIFORME CENTROAMERICANO, CAUCA Y SU REGLAMENTO. CUANDO LOS TRASLADOS TEMPORALES SE GENEREN DE EMPRESAS CALIFICADAS COMO USUARIAS DE ZONAS FRANCAS O DE DPA, A EMPRESAS UBICADAS DENTRO DEL TERRITORIO ADUANERO NACIONAL, EL PLAZO DE PERMANENCIA DE ESTAS MERCANCÍAS SERÁ DE DOS MESES. LA DIRECCIÓN GENERAL DE ADUANAS PODRÁ AUTORIZAR PREVIAMENTE QUE LOS USUARIOS DE UNA MISMA ZONA FRANCA FORMALICEN SUS TRASLADOS DEFINITIVOS DE MANERA ACUMULADA, CUANDO LA NATURALEZA Y EL VOLUMEN DE OPERACIONES LO JUSTIFIQUEN. (6) (8)" | Traslados use the physical/electronic formats the DGA establishes by general administrative provisions. For traslados NOT implying transfer of dominion, a NOTA DE REMISIÓN (remission note) must ADDITIONALLY be issued; it is a special case of no-dominion transfer when the traslado to another beneficiary is made by order of the contractor (contratista), duly proven. For goods admitted temporarily without dominion transfer, the respective contracts determine their permanence under the regime, which may NOT exceed twelve months. Formalizations/confirmations are due within up to THREE días hábiles AFTER the goods' ingreso (entry), the goods remaining at the customs office's disposal until levante (release) per CAUCA and its Reglamento. Temporary traslados from ZF-usuario or DPA companies to companies located in the national customs territory (TAN): permanence term of these goods is TWO MONTHS. The DGA may previously authorize usuarios of the same zona franca to formalize their definitive traslados in accumulated form when the nature and volume of operations justify it | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 22 incs. 3-6 p.28 (EVID-257; txt PAGE 28; SOQ-30 print) |
| LB-004 | Ley de Zonas Francas, Art. 23: "EL TITULAR DE UNA EMPRESA CALIFICADA COMO USUARIA DE ZONA FRANCA, PODRÁ TRASLADAR TEMPORALMENTE MERCANCÍAS AL TERRITORIO ADUANERO NACIONAL, CON EL OBJETO QUE TERCERAS PERSONAS POR ÉL SUBCONTRATADAS, REALICEN PROCESOS QUE AGREGUEN VALOR A LOS BIENES, COMPLETEN LOS PROCESOS DE TRANSFORMACIÓN, ELABORACIÓN O REPARACIÓN DE LAS MERCANCÍAS. LAS EMPRESAS CALIFICADAS COMO DPA PODRÁN REALIZAR TRASLADOS TEMPORALES DE MAQUINARIA Y EQUIPO AL TERRITORIO ADUANERO NACIONAL PARA SER REPARADAS. ÚNICAMENTE LAS EMPRESAS CALIFICADAS COMO DPA DEDICADAS A ACTIVIDADES RELACIONADAS A LAS ARTESANÍAS, INDUSTRIA TEXTIL, MAQUILA O CONFECCIÓN DE ROPA, PODRÁN SER AUTORIZADAS PARA REALIZAR LOS DEMÁS PROCESOS ESTABLECIDOS EN EL INCISO ANTERIOR. EN AMBOS CASOS, DICHO TITULAR SERÁ EL RESPONSABLE POR EL PAGO DE LOS DERECHOS E IMPUESTOS CORRESPONDIENTES, SI TALES BIENES NO INGRESARAN NUEVAMENTE AL USUARIO O DPA QUE LOS REMITIÓ. … LOS TRASLADOS NO IMPLICARÁN PRÓRROGA DEL PLAZO ESTABLECIDO EN EL ARTÍCULO 22 DE ESTA LEY. TODO TRASLADO SE EFECTUARÁ UTILIZANDO LOS FORMATOS Y MEDIOS FÍSICOS Y ELECTRÓNICOS QUE AL EFECTO ESTABLEZCA LA DIRECCIÓN GENERAL DE ADUANAS. PARA PODER REALIZAR TRASLADOS TEMPORALES AL TERRITORIO ADUANERO NACIONAL A LOS QUE SE REFIERE ESTE ARTÍCULO, EL USUARIO DEBERÁ NOTIFICAR POR UNA SOLA VEZ A LA DELEGACIÓN ADUANERA CORRESPONDIENTE Y EL DPA A LA DIRECCIÓN GENERAL DE ADUANAS, QUE REALIZARÁ O QUE DEJARÁ DE REALIZAR ESTE TIPO DE OPERACIONES. (6) (8)" | A ZF-usuario company holder may temporarily transfer goods to the national customs territory (TAN) so that third persons subcontracted by it perform processes that add value to the goods or complete the transformation, elaboration or repair processes. DPA companies may make temporary traslados of machinery and equipment to TAN for REPAIR; ONLY DPAs dedicated to artesanías (handicrafts), textile industry, maquila or clothing manufacture may be authorized for the other processes of the preceding inciso. In both cases the holder is RESPONSIBLE for payment of the corresponding duties and taxes if the goods do not re-enter the usuario or DPA that sent them. Traslados do NOT extend the Art. 22 term. Every traslado uses DGA-established formats. To perform such temporary TAN traslados, the usuario notifies the corresponding customs delegation ONCE, and the DPA the DGA, whether it will or will not perform this type of operations | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 23 pp.28-29 (EVID-257; txt PAGE 28-29; SOQ-30 print) |
| LB-005 | Ley de Zonas Francas, Art. 24: "PODRÁN EXPORTARSE TEMPORALMENTE BIENES DEL TERRITORIO ADUANERO NACIONAL A UNA ZONA FRANCA O DPA, CON EL PROPÓSITO QUE PUEDAN SER SOMETIDAS A OPERACIONES DE PERFECCIONAMIENTO, TRANSFORMACIÓN, ELABORACIÓN, REPARACIÓN O CUALQUIER OTRO SERVICIO QUE SEA REQUERIDO. EL PLAZO MÁXIMO PARA SU REIMPORTACIÓN AL TERRITORIO ADUANERO NACIONAL SERÁ DE SEIS MESES CONTADOS A PARTIR DE LA FECHA DE INGRESO A LA ZONA FRANCA O DPA. DICHOS BIENES AL SER REIMPORTADOS AL TERRITORIO ADUANERO NACIONAL, DEBERÁN PAGAR LOS DERECHOS E IMPUESTOS QUE CORRESPONDAN ÚNICAMENTE A LA PARTE DEL VALOR AGREGADO NO NACIONAL INCORPORADO EN DICHO PROCESO. PARA EFECTOS DE ESTA OPERACIÓN, SE APLICARÁ EL ARANCEL DE LA NACIÓN MÁS FAVORECIDA (NMF). EL ENVÍO DE BIENES A QUE SE REFIEREN LOS SERVICIOS ANTERIORES, SE ASIMILARÁ PARA LOS EFECTOS IMPOSITIVOS A EXPORTACIÓN TEMPORAL PARA PERFECCIONAMIENTO PASIVO; NO OBSTANTE, LOS MISMOS SE REALIZARÁN AL AMPARO DEL FORMULARIO QUE AL EFECTO DEBERÁ ESTABLECER LA DIRECCIÓN GENERAL DE ADUANAS. (1) (8)" | Goods may be TEMPORARILY EXPORTED from the national customs territory to a zona franca or DPA to undergo perfecting, transformation, elaboration, repair or any other required service. The MAXIMUM term for their REIMPORTATION into the national customs territory is SIX MONTHS counted from the date of entry into the zona franca or DPA. Upon reimportation the goods pay the corresponding duties and taxes ONLY on the part of the NON-NATIONAL VALUE-ADDED incorporated in the process; for this operation the most-favoured-nation tariff (NMF) applies. The sending of goods under these services is ASSIMILATED, for tax effects, to temporary exportation for passive perfecting; it is carried out under the form the DGA must establish | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 24 p.29 (EVID-257; txt PAGE 29; SOQ-30 print) |
| LB-006 | Ley de Zonas Francas, Art. 26: "LOS PRODUCTOS INTRODUCIDOS AL PAÍS DE CONFORMIDAD CON ESTA LEY PODRÁN MOVILIZARSE EN EL TERRITORIO ADUANERO NACIONAL, SIN EL PAGO DE LOS RESPECTIVOS DERECHOS E IMPUESTOS, CUANDO SE TRATE DEL TRASLADO ENTRE USUARIOS DEL RÉGIMEN DE ZONAS FRANCAS; DPA; USUARIOS DEL RÉGIMEN DE ZONAS FRANCAS Y DPA O CON TERCEROS SUBCONTRATADOS PARA LAS OPERACIONES REFERIDAS EN EL ARTÍCULO 23 DE ESTA LEY. EN EL CASO DE TRASLADOS ENTRE DPA O DE ZONAS FRANCAS A DPA Y DE DPA A ZONAS FRANCAS, DEBERÁN HACERSE DENTRO DEL PLAZO QUE SEÑALA EL ARTÍCULO 22 DE ESTA LEY. … CUANDO SE TRATE DE TRASLADOS TEMPORALES, SERÁ EL TITULAR DE LA EMPRESA AUTORIZADA QUE GENERA EL TRASLADO O SU REPRESENTANTE LEGAL, EL RESPONSABLE DEL PAGO DE DERECHOS E IMPUESTOS A LA IMPORTACIÓN Y DEMÁS GRAVÁMENES CONEXOS, UNA VEZ VENCIDO EL PLAZO ESTABLECIDO POR LA LEY. SU INCUMPLIMIENTO SERÁ SANCIONADO DE CONFORMIDAD A LO ESTABLECIDO EN EL ARTÍCULO 5, LITERAL q) DE LA LEY ESPECIAL PARA SANCIONAR INFRACCIONES ADUANERAS. EN CASO QUE INGRESE LA MERCANCÍA FUERA DEL PLAZO O QUE ÉSTA NO RETORNE, DEBERÁ PRESENTAR LA DECLARACIÓN DE MERCANCÍAS A PAGO Y SE PROCEDERÁ CON EL PROCESO SANCIONADOR CUANDO CORRESPONDA. SI AL MOMENTO DEL RETORNO DE LAS MERCANCÍAS, EL USUARIO RECEPTOR HUBIERE CERRADO OPERACIONES, LAS MISMAS DEBERÁN PONERSE A DISPOSICIÓN DE LA DIRECCIÓN GENERAL DE ADUANAS, PARA LOS EFECTOS CORRESPONDIENTES, LA QUE CONSIDERARÁ LO DISPUESTO EN EL ARTÍCULO 40 DE ESTA LEY." | Products introduced under this law may move within the national customs territory WITHOUT payment of duties and taxes for traslados between ZF usuarios, DPAs, ZF usuarios and DPAs, or with third parties subcontracted for the Art. 23 operations; traslados between DPAs, from zonas francas to DPAs and from DPAs to zonas francas must be made within the Art. 22 term. For TEMPORARY traslados, the holder of the authorized company generating the traslado (or its legal representative) is RESPONSIBLE for payment of import duties and other connected levies once the statutory term has expired. Breach is sanctioned per Art. 5 literal q) of the Ley Especial para Sancionar Infracciones Aduaneras (LESIA). If the goods enter outside the term or do not return, a DM for payment must be presented and the sanctioning process proceeds when applicable; if the receiving usuario has closed operations at return time, the goods are placed at the DGA's disposal, which considers Art. 40 of this law | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 26 pp.30-31 (EVID-257; txt PAGE 30-31; SOQ-30 print) |
| LB-007 | Ley de Servicios Internacionales, Art. 26: "El Régimen que normará el ingreso y permanencia de todos los bienes introducidos por los usuarios directos de un parque de servicios para la prestación de sus servicios, tendrá carácter liberatorio y su plazo de permanencia será indefinido. Dichos bienes no estarán sujetos a ningún impuesto ni caución mientras permanezcan dentro del parque de servicios. No obstante, las operaciones de distribución u operaciones logísticas internacionales, deberán regirse de conformidad a lo dispuesto en la sección segunda de este Capítulo. En el caso de los centros de servicios, las materias primas, insumos y demás bienes introducidos, tendrán un plazo de permanencia de un año, contado a partir de la fecha de aceptación de la declaración de mercancías correspondiente; asimismo, los bienes de capital serán liquidados a franquicia definitiva. Para aquellos centros de servicios que operen en zonas aduaneras primarias donde exista delegación aduanera, las materias primas, insumos, bienes de capital y demás bienes introducidos, podrán permanecer el tiempo que sea necesario para sus operaciones, debiendo cumplir las disposiciones contenidas en el reglamento de la presente Ley." | The regime governing entry and permanence of all goods introduced by usuarios directos of a services park has a LIBERATORY (liberatorio) character and its permanence term is INDEFINITE; those goods are subject to no tax or bond while they remain inside the park — though distribución/logística operations follow the chapter's second section (the Arts. 27-45 clocks below). For centros de servicios, raw materials, inputs and other goods introduced have a permanence term of ONE YEAR counted from the acceptance date of the corresponding DM; capital goods are liquidated under DEFINITIVE FRANCHISE (franquicia definitiva). For centros operating in primary customs zones with a customs delegation, goods may remain the time necessary for their operations, subject to the reglamento's provisions (the TAN→parque/centro exportación-definitiva paragraph of this article is owned by `05_tan-iva-interface.md` by id) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 26 incs. 1/3/4 p.15 (EVID-263; txt PAGE 15; SOQ-30 print) |
| LB-008 | Ley de Servicios Internacionales, Art. 33: "Una vez descargadas las mercancías en las instalaciones del usuario directo, éste tendrá un plazo de veinte días hábiles para proceder a destinarlas al régimen de Admisión Temporal por un plazo de veinticuatro meses calendario, prorrogables por períodos adicionales de un año, previa autorización de la Dirección General de Aduanas, tiempo durante el cual las mercancías no estarán sujetas a ningún impuesto ni caución; o dentro de los mismos veinte días hábiles, a solicitud de su cliente, podrá destinadas a los regímenes aduaneros aplicables. Vencido el plazo de los veinte días hábiles sin haberse destinado las mercancías a un determinado régimen, las mismas se considerarán en abandono." | Once the goods are discharged at the usuario directo's installations, it has a term of TWENTY días hábiles to proceed to destine them to the admisión-temporal regime for a term of TWENTY-FOUR CALENDAR MONTHS (veinticuatro meses calendario), EXTENDABLE by additional ONE-YEAR periods with PRIOR DGA authorization — during which the goods are subject to no tax or bond; or, within the same twenty días hábiles, at its client's request, they may be destined to the applicable customs regimes. Upon expiry of the twenty días hábiles without destinación to a determined regime, the goods are considered in ABANDONMENT (abandono) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 33 p.18 (EVID-263; txt PAGE 18; SOQ-30 print) |
| LB-009 | Ley de Servicios Internacionales, Art. 34: "Los usuarios directos o indirectos, podrán optar a declarar sus mercancías a cualquiera de los siguientes regímenes, de conformidad a las regulaciones legales: a) Importación definitiva. b) Exportación definitiva. c) Importación Temporal con reexportación en el mismo estado. d) Tránsito Aduanero. e) Reexportación. Los usuarios deberán solicitar la autorización para la declaración de mercancías en tránsito interno, al Depósito o lugar autorizado, cuando requieran someter sus mercancías a cualquiera de los siguientes regímenes: 1) Zonas Francas. 2) Depósito Perfeccionamiento Activo. 3) Régimen de Depósito Aduanero. En caso de ejecutar las operaciones siguientes, deberán ser trasladadas a la aduana interna que corresponda: I) Reimportación. II) Exportación temporal con reimportación en el mismo estado. III) Exportación temporal para perfeccionamiento pasivo. IV) Envíos postales. V) Envíos urgentes o courier. VI) Equipaje. VII) Menaje de Casa. VIII) Pequeños envíos de carácter comercial." | Usuarios directos or indirectos may opt to declare their goods to any of: a) definitive importation; b) definitive exportation; c) temporary importation with re-export in the same state; d) customs transit; e) re-exportation. Users must request authorization for the internal-transit goods declaration, to the deposit or authorized place, when they need to subject goods to: 1) zonas francas; 2) depósito perfeccionamiento activo (DPA); 3) régimen de depósito aduanero. For the listed operations the goods must be transferred to the corresponding internal customs office: I) reimportation; II) temporary exportation with reimportation in the same state; III) temporary exportation for passive perfecting; IV) postal shipments; V) urgent shipments or courier; VI) baggage; VII) household goods (menaje de casa); VIII) small commercial shipments | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 34 pp.18-19 (EVID-263; txt PAGE 18-19; SOQ-30 print) |
| LB-010 | Ley de Servicios Internacionales, Art. 38 (final inciso of the acopio article): "La remisión de mercancías en libre circulación hacia el parque de servicios será documentada ante la Delegación Aduanera y Fiscal del parque de servicios, a través de la nota de remisión. Para realizar las operaciones a que se refiere el presente artículo, el beneficiario deberá estar previamente autorizado por la Dirección General de Aduanas…" | The remission of goods in free circulation (libre circulación) toward the services park is documented before the park's customs and fiscal delegation THROUGH A NOTA DE REMISIÓN; the beneficiary must be previously authorized by the DGA for those acopio-para-exportación operations (LSI kin of the ZF non-dominion nota-de-remisión duty — LB-003) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 38 inc. 2 p.20 (EVID-263; txt PAGE 20; SOQ-30 print) |
| LB-011 | Ley de Servicios Internacionales, Art. 41: "Una vez legalizada la declaración de mercancías a cualquier régimen aduanero, según lo dispuesto en el artículo 34 de la presente Ley, las mismas podrán permanecer en el estatus de expedición, dentro de las instalaciones del usuario directo, hasta un plazo máximo de veinte días hábiles a partir del día siguiente al registro de la correspondiente declaración de mercancías en el sistema informático de la Dirección General de Aduanas. El usuario directo o indirecto deberá informar dentro del plazo antes señalado la razón y las acciones legales a seguir." | Once the goods declaration to any customs regime is legalized (per Art. 34), the goods may remain in EXPEDICIÓN (dispatch) status inside the usuario directo's installations for a MAXIMUM term of twenty días hábiles counted from the DAY AFTER the registration of the corresponding DM in the DGA's computer system. The usuario directo or indirecto must INFORM within that term the reason (razón) and the legal actions to be followed | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 41 p.20 (EVID-263; txt PAGE 20; SOQ-30 print) |
| LB-012 | Ley de Servicios Internacionales, Art. 43: "Para efecto de la determinación de la base imponible de las mercancías que se destinen al mercado nacional, de conformidad al precio pagado o por pagar, no se incluirán en el valor en aduana, los gastos de almacenaje y de conservación de las mercancías durante su estancia en el parque de servicios, siempre que éstos se expresen por separado del precio pagado o por pagar por la misma." | For determining the taxable base of goods destinated to the national market per the price paid or payable, the STORAGE (almacenaje) and CONSERVATION costs of the goods during their stay in the services park are NOT included in the customs value (valor en aduana), PROVIDED they are expressed SEPARATELY from the price paid or payable for the goods themselves | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 43 p.21 (EVID-263; txt PAGE 21; SOQ-30 print) |
| LB-013 | Ley de Servicios Internacionales, Art. 44: "La Delegación de Aduanas del parque de servicios, a requerimiento de parte interesada, podrá emitir Certificados de Control Aduanero de las Mercancías que se reexporten desde el parque a otros destinos, a efecto que las mismas conserven los beneficios inherentes a su origen en el marco de los Tratados de Libre Comercio o de la Integración Económica Centroamericana, suscritos por el Gobierno de El Salvador. La Dirección General de Aduanas emitirá a través de disposiciones administrativas de carácter general, las regulaciones, formatos y procedimientos relativos a dicho certificado." | The park's customs delegation, at an interested party's request, may issue Customs Control Certificates (Certificados de Control Aduanero) for goods RE-EXPORTED from the park to other destinations, so that they preserve the benefits inherent to their origin under the free-trade treaties or Central American economic integration signed by El Salvador. The DGA issues the certificate's regulations, formats and procedures through general administrative provisions (DACG — not in corpus) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 44 p.21 (EVID-263; txt PAGE 21; SOQ-30 print) |
| LB-014 | Ley de Servicios Internacionales, Art. 45: "Previa autorización de la Delegación de Aduanas del parque de servicios, los productos residuales provenientes del embalaje o empaque de las mercancías tales como: paletas de madera o plástico, bidones y similares, podrán ser destinadas a consumo definitivo al territorio nacional pagando los derechos e impuestos de importación sobre el valor facturado a precios de mercado, a través de la declaración de mercancías simplificada. No pagarán ningún impuesto, cuando sean destinados a botaderos de desechos sólidos autorizados para su destrucción o podrán ser exonerados de derechos e impuestos cuando se trate de donaciones a instituciones sin fines de lucro de carácter humanitario, educativas u otros servicios a la comunidad, previa calificación del Ministerio de Economía y la exoneración del Órgano Legislativo. En ambos casos, se realizarán bajo la coordinación y supervisión de la Dirección General de Aduanas. El reglamento de esta Ley establecerá los procedimientos para la aplicación de esta disposición." | With prior authorization of the park's customs delegation, residual products from the packing or packaging of goods — such as wooden or plastic pallets (paletas), drums (bidones) and the like — may be destined to definitive consumption in the national territory PAYING import duties and taxes on the invoiced value at market prices (valor facturado a precios de mercado), through the simplified goods declaration (declaración de mercancías simplificada). They pay NO tax when destined to AUTHORIZED solid-waste dumps (botaderos) for destruction, and may be EXONERATED for DONATIONS to non-profit humanitarian, educational or community-service institutions, with prior MINEC qualification and the exoneración of the Legislative Organ (Órgano Legislativo/Asamblea); both cases under DGA coordination and supervision. The law's reglamento establishes the application procedures | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 45 p.21 (EVID-263; txt PAGE 21; SOQ-30 print) |
| LB-015 | Instructivo de llenado DUCA (43_), field 14: "Fecha de vencimiento del régimen: En este campo se consigna la fecha en la que se vence el plazo autorizado al régimen al que se están sometiendo las mercancías." Field 56: "Válida hasta: Cuando la Declaración haga las veces de Formulario Aduanero Único Centroamericano, tendrá validez de treinta días hábiles a partir de su emisión. Esta Vigencia aplica únicamente en el país de exportación de las mercancías." (types frame: "3. DUCA-F: para las mercancías originarias de la región centroamericana"; the DUCA "está conformada por el conjunto de datos que integran las funciones asignadas al [FAUCA], la Declaración de Mercancías (DM) y la [DUT]") | Field 14 — regime expiry date: the date on which the authorized term of the regime to which the goods are subjected expires. Field 56 — valid until: when the declaration serves as the Formulario Aduanero Único Centroamericano (FAUCA, Central American Single Customs Form), it has a validity of THIRTY días hábiles from its emission; this validity applies ONLY in the country of exportation of the goods. DUCA-F = the variant for goods originating in the Central American region (the DUCA record model mirroring these fields is owned by `06_customs-declarations.md` — cited here at field-anchor depth only) | `sv/sources/43_DUCA_Instructivo_COMIECO.pdf` | Fields 14/56 pp.3, 9 (EVID-272; txt PAGE 3, 9; 2018 print assumed current — SOQ-36) |

## 3. Functional Requirements

### 3.1 The clock chassis + the regime-distinctness invariant (12_ Arts. 21/22; 14_ Arts. 26/33)

- **SV-SPE-FR-064:** The system shall carry every regime-goods time limit as a
  per-DM clock row on `l10n_sv_special_regime.customs_clock`, linked to the
  goods-declaration record (DUCA surface consumed from
  `06_customs-declarations.md` by id) and to the Task-1 regime profile
  (SV-SPE-FR-001/002/003 by id — ZF · DPA · parque · centro), each row
  carrying: clock kind (the §4 catalog), anchor kind and anchor date (DM
  acceptance · DM liquidación · traslado-document date · ingreso · discharge
  · DM system registration · emission), the duration resolved from its
  dated clock-kind config row (value · unit · day kind, snapshot-on-write —
  D15: never a global constant), the computed expiry, the running state and
  the expiry effect; the DUCA "fecha de vencimiento del régimen" linkage
  rides FR-080.
  (LB-002; LB-008; EVID-257/263)
- **SV-SPE-FR-065:** The system shall encode the ZF/DPA and LSI
  admisión-temporal clocks as DISTINCT clock kinds that are NEVER unified:
  ZF/DPA — UP TO 12 MESES IMPRORROGABLES per DM acceptance (12_ Art. 22,
  uppercase as printed), hard-capped, no extension row ever attachable; LSI
  — 24 MESES CALENDARIO (veinticuatro meses calendario, 14_ Art. 33)
  prorrogable by additional one-year periods with PRIOR DGA authorization;
  the config catalog enforces regime-exclusive kinds (a 12m row can never
  resolve against an LSI profile; a prorrogable row can never resolve
  against a ZF/DPA profile), and no shared row or parameterized shortcut
  between the two families is offered — this is the file's governing
  invariant (EVID-263 doubt: "12-month (ZF) vs 24-month (LSI) admisión
  temporal for the same goods concept — regime-specific rows, never shared
  config").
  (LB-002; LB-008; EVID-257/263)
- **SV-SPE-FR-066:** The system shall run the ZF/DPA perfeccionamiento
  clock per DM: goods introduced for perfecting under the
  admisión-temporal-para-perfeccionamiento-activo regime — DPA Art. 19 b)
  goods by nature, and ZF entries under non-dominion modalities
  (arrendamiento, comodato or any form not implying transfer of dominion,
  which per Art. 21 declare under that regime) — carry a clock of UP TO
  ("DE HASTA") 12 MESES IMPRORROGABLES counted from DM acceptance, where
  the per-goods contract may set a shorter permanence never exceeding
  twelve months; ZF dominion goods under Art. 17 carry NO clock (indefinite
  permanence) and DPA capital goods enter via Declaración de Importación
  Definitiva a Franquicia (no clock); on expiry the system stamps the
  tribute-obligation state ("LA OBLIGACIÓN DEL PAGO DE LOS TRIBUTOS
  CORRESPONDIENTES") and records that sanctions under the applicable
  legislation follow — ZERO sanction mechanics invented (LESIA absent —
  OQ-1/SOQ-32 pointer; the sanction ladders live in `07` by id); a
  pre-expiry warning window is an operational default (30 days,
  configurable — non-statutory, OQ-5).
  (LB-001; LB-002; LB-003; EVID-257)
### 3.2 Traslado sub-clocks (12_ Arts. 22/23/26)

- **SV-SPE-FR-067:** The system shall implement the traslado sub-clocks of
  Art. 22 as clock rows of their own kind, each anchored per the print:
  definitive traslados — up to 12 months from the date the goods FIRST
  entered the admisión-temporal regime (first DM acceptance); temporary
  traslados — up to 6 months from the traslado date recorded in the
  document emitted for that purpose, ALWAYS capped inside the 12-month
  envelope computation (the cap is printed for DPA and literal b) is
  extended to ZF-usuario traslados); definitive ZF→DPA traslados — up to 12
  months from the LIQUIDACIÓN date of the DM that cancels the
  zonas-francas regime (with the DPA-transmits-the-DM-to-the-ZF-delegation
  procedural note); and NO traslado ever extends the Art. 22 term ("LOS
  TRASLADOS NO IMPLICARÁN PRÓRROGA DEL PLAZO" — Art. 23); the DGA's
  same-zone accumulated-formalization authorization is recorded as a config
  flag with no shipped default (DACG matter).
  (LB-002; LB-004; EVID-257)
- **SV-SPE-FR-068:** The system shall run the ZF/DPA→TAN temporary-traslado
  clock at TWO MONTHS permanence for goods moved from ZF-usuario or DPA
  companies to companies located in the national customs territory, with
  the responsibility rule attached: the holder of the generating company
  (or its legal representative) is responsible for import duties and
  connected levies once the term expires; goods entering out of term or not
  returning trigger the DM-A-PAGO state plus the sanctioning-process
  pointer (LESIA Art. 5 q) — OQ-1), and goods whose receiving usuario has
  closed operations are flagged for DGA disposal per Art. 40 (the
  closure-with-open-DMs defraudación surface lives in `07` by id).
  (LB-003; LB-006; EVID-257)
- **SV-SPE-FR-069:** The system shall run the formalización clock at up to
  3 días hábiles after the goods' ingreso to the receiving beneficiary —
  the goods remaining at the customs office's disposal until levante per
  CAUCA and its Reglamento — with días-hábiles arithmetic consumed from
  SV-FREP-FR-202..204 by id (never restated).
  (LB-003; EVID-257)
- **SV-SPE-FR-070:** The system shall require, on every traslado that does
  NOT imply transfer of dominion, the emission of a NOTA DE REMISIÓN in
  addition to the DGA-established traslado format — the document surface
  being the e-invoicing NRE doc type consumed by id (SV-EINV-FR-001 type
  04; SV-EINV-FR-026 goods-transfer document rules), with the statutory
  no-dominion special case recorded: a traslado to another beneficiary made
  by order of the CONTRATISTA, duly proven, is a no-dominion transfer
  (proof-reference field); the LSI twin rides the same surface: remissions
  of libre-circulación goods toward a parque de servicios for acopio are
  documented before the park's Delegación Aduanera y Fiscal through a nota
  de remisión (14_ Art. 38, prior-DGA-authorization flag). A non-dominion
  traslado without its NRE reference stays in pending-document state.
  (LB-003; LB-010; EVID-257/263)
- **SV-SPE-FR-071:** The system shall enforce the Art. 23 scope predicates
  on temporary traslados to TAN before the FR-068 clock opens: ZF usuarios
  — goods moved for third persons SUBCONTRACTED by the holder to add value
  or complete transformation/elaboration/repair processes; DPAs — machinery
  and equipment moved for REPAIR only, EXCEPT DPAs in artesanías, textile
  industry, maquila or clothing manufacture, which may be authorized for
  the other processes (authorization flag); the holder's responsibility for
  duties if the goods do not re-enter; and the one-time standing notice
  (usuario → delegación aduanera; DPA → DGA) that it will or will not
  perform this type of operations, recorded as a regime-profile flag.
  (LB-004; EVID-257)

### 3.3 TAN→ZF/DPA passive processing (12_ Art. 24)

- **SV-SPE-FR-072:** The system shall model the temporary exportation of
  TAN goods into a zona franca or DPA for perfeccionamiento,
  transformation, elaboration, repair or any other required service as a
  passive-processing clock of its own kind: reimportation into the national
  customs territory due within a MAXIMUM of 6 months counted from the date
  of INGRESO to the zona franca or DPA (a clock DISTINCT from the 2-month
  ZF/DPA→TAN traslado of FR-068 — never merged, per the EVID-257
  do-not-merge note); on reimportation within term, duties and taxes apply
  ONLY to the part of the NON-NATIONAL VALUE-ADDED incorporated in the
  process, under the NMF tariff; the operation is assimilated for tax
  effects to EXPORTACIÓN TEMPORAL PARA PERFECCIONAMIENTO PASIVO (temporary
  exportation for passive perfecting) and runs under the DGA-established
  formulario (config slot, no default — DACG); out-of-term entry or
  non-return follows the FR-068 DM-a-pago state.
  (LB-005; LB-006; EVID-257)

### 3.4 LSI clock family — parque/centros, destinación, regímenes optables (14_ Arts. 26/33/34)

- **SV-SPE-FR-073:** The system shall run the LSI parque/centro permanence
  clocks per Art. 26, all as clock kinds DISTINCT from every ZF/DPA row:
  parque de servicios — liberatorio character, INDEFINITE permanence (no
  expiry row; no tax nor bond while the goods remain in the park; the
  distribución/logística operations route to the Arts. 27-45 clocks);
  centro de servicios — materias primas, insumos and other goods introduced
  carry a ONE-YEAR clock from the DM acceptance date, and capital goods are
  recorded as liquidated under FRANQUICIA DEFINITIVA (terminal state, no
  clock); centros operating in primary customs zones with a customs
  delegation — indefinite ("el tiempo que sea necesario"), reglamento-bound
  (the TAN→parque/centro exportación-definitiva tax routing of this article
  is owned by `05_tan-iva-interface.md` by id).
  (LB-007; EVID-263)
- **SV-SPE-FR-074:** The system shall run the two-stage LSI destinación
  machinery of Art. 33: stage 1 — from the DISCHARGE of the goods at the
  usuario directo's installations (the recepción-efectiva document date per
  Art. 32 kin), a 20-días-hábiles window (días-hábiles engine by id) to
  destine the goods, whose expiry without destinación stamps the ABANDONO
  state (a terminal goods state feeding the register surfaces of `07` by
  id); stage 2 — the admisión-temporal clock opened by that destinación:
  24 MESES CALENDARIO prorrogable by additional ONE-YEAR periods, EACH
  extension requiring and recording PRIOR DGA authorization (authorization
  reference + date stamped per extension; extension rows exist ONLY on
  this clock kind per FR-065); alternatively, within the same 20 días
  hábiles and at the client's request (flag), the goods destine to the
  Art. 34 regimes (FR-075).
  (LB-008; EVID-263)
- **SV-SPE-FR-075:** The system shall carry the regímenes optables menu of
  Art. 34 as the destinación target catalog: a) importación definitiva;
  b) exportación definitiva; c) importación temporal con reexportación en
  el mismo estado; d) tránsito aduanero; e) reexportación — plus the
  internal-transit route: destining toward zonas francas, DPA or depósito
  aduanero requires the internal-transit DM to the deposit or authorized
  place; and the aduana-interna operations list (reimportación; exportación
  temporal con reimportación en el mismo estado; exportación temporal para
  perfeccionamiento pasivo; envíos postales; envíos urgentes/courier;
  equipaje; menaje de casa; pequeños envíos de carácter comercial)
  requiring transfer to the corresponding internal customs office — the
  menu is config (as printed), stamped on the destinación record.
  (LB-009; EVID-263)

### 3.5 Expedición, customs-value edge, Certificados de Control Aduanero (14_ Arts. 41/43/44)

- **SV-SPE-FR-076:** The system shall run the expedición clock: once the DM
  to any customs regime is legalized (per Art. 34), goods may remain in
  EXPEDICIÓN status inside the usuario directo's installations for a
  maximum of 20 días hábiles counted from the DAY AFTER the DM's
  registration in the DGA computer system (días-hábiles engine by id), with
  the information duty attached: the usuario directo or indirecto must
  inform within the same term the RAZÓN and the legal actions to be
  followed — an inform record (reason + actions + date) on the expedición
  state, pending-flagged at expiry.
  (LB-011; EVID-263)
- **SV-SPE-FR-077:** The system shall exclude, from the customs value
  (valor en aduana) of goods destinated to the national market from a
  parque de servicios, the storage (almacenaje) and conservation costs
  incurred during the goods' stay in the park WHEN — and only when — those
  costs are expressed SEPARATELY from the price paid or payable for the
  goods; costs embedded in the price remain in the base (inverting gate on
  the value line; the DUCA value block it feeds is owned by `06` by id).
  (LB-012; EVID-263)
- **SV-SPE-FR-078:** The system shall record Certificados de Control
  Aduanero as reexport-linked certificate records: issued by the park's
  customs delegation at an interested party's request for goods re-exported
  from the parque to other destinations, so the goods PRESERVE the benefits
  inherent to their origin under the TLCs or Central American economic
  integration signed by El Salvador — each record carrying the reexport DM
  reference, the requesting party and the origin-benefit instrument; the
  DGA's DACG formatos/procedimientos are config slots with NO defaults
  (SOQ-44 kin — living administrative layer).
  (LB-013; EVID-263)
### 3.6 Residuales disposition paths (14_ Art. 45)

- **SV-SPE-FR-079:** The system shall implement the residual-products
  disposition paths (paletas de madera o plástico, bidones y similares from
  embalaje/empaque) as three recorded paths, each prior-authorized by the
  park's customs delegation: i) consumo definitivo into the national
  territory — import duties and taxes computed on the VALOR FACTURADO A
  PRECIOS DE MERCADO (invoiced value at market prices), declared through
  the DECLARACIÓN DE MERCANCÍAS SIMPLIFICADA (simplified DM — record
  reference required); ii) destination to authorized solid-waste BOTADEROS
  for destruction — NO tax, DGA control note; iii) DONATIONS to non-profit
  humanitarian, educational or community-service institutions — exonerated
  with prior MINEC calificación AND the exoneración of the Órgano
  Legislativo (Asamblea), both references required on the record; all paths
  under DGA coordination/supervision, with the reglamento's application
  procedures as a config-slot note (17b_ pointer, no invented detail).
  (LB-014; EVID-263)

### 3.7 DUCA linkage (43_; `06_customs-declarations.md` by id)

- **SV-SPE-FR-080:** The system shall feed the clock rows from the DUCA
  "fecha de vencimiento del régimen" field (43_ field 14: the date on which
  the authorized term of the regime to which the goods are subjected
  expires), consumed BY ID from the DUCA record model of
  `06_customs-declarations.md` (forward reference resolved at final
  review): each clock row reconciles its computed expiry against the
  declaration's regime-expiry field and raises a mismatch flag on
  divergence (never silently overwriting either side); whether the field is
  mandatory per operation lives in the absent Comité Aduanero user manual
  (OQ-2).
  (LB-015; EVID-272)
- **SV-SPE-FR-081:** The system shall run the DUCA-F FAUCA-validity clock:
  when a DUCA-F (regional-origin variant) serves as Formulario Aduanero
  Único Centroamericano (FAUCA), it is valid for 30 días hábiles from its
  EMISSION, and that validity applies ONLY in the country of exportation of
  the goods — an export-country scope flag on the clock row (an in-country
  expiry event never fires from this clock); días-hábiles arithmetic via
  SV-FREP-FR-202..204 by id; this file owns the CLOCK view; the
  declaration-record field surface is `06_customs-declarations.md`'s by id
  (ownership split noted — OQ-6).
  (LB-015; EVID-272)

## 4. Data Model

Layer semantics: all entities are Odoo-native config/ledger rows on the
Task-1 regime profile, keyed to the DUCA record surface that
`06_customs-declarations.md` owns (consumed by id) — every entity lives in
the client (wave default `odoo`; see §5). Clock durations are code-text
values as printed (SOQ-30 watch), stored as dated clock-kind rows with
instrument provenance, never constants. CSV sidecar evaluated per plan: the
clock-kind catalog is ≈14 template rows — §4 config rows suffice and NO
sidecar ships (default none; judgment noted in the task report).

**Clock chassis (l10n_sv_special_regime.customs_clock):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.customs_clock | dm_ref · profile | m2o · m2o | DUCA record (06 by id); T1 regime profile (SV-SPE-FR-003 by id) | FR-064 |
| l10n_sv_special_regime.customs_clock | clock_kind | m2o config | zf_dpa_admision_12m · traslado_definitivo_12m · traslado_temporal_6m · traslado_zf_a_dpa_12m · traslado_zf_dpa_a_tan_2m · formalizacion_3dh · reimport_pasivo_6m · lsi_admision_temporal_24m · centros_materias_1y · parque_indefinido · centros_primaria_indefinido · destinacion_20dh · expedicion_20dh · duca_f_fauca_30dh | FR-064..081 |
| l10n_sv_special_regime.customs_clock | anchor_kind · anchor_date | select · date | dm_acceptance · dm_liquidacion · traslado_doc_date · ingreso_date · discharge_date · dm_registration · emission_date (D15 anchor per clock kind) | FR-064, FR-066..081 |
| l10n_sv_special_regime.customs_clock | duration_value · duration_unit · day_kind | int · select · select | resolved from the clock-kind config row; mes_calendario · dia_habil (snapshot-on-write) | FR-064 |
| l10n_sv_special_regime.customs_clock | expiry_date · state | computed · select | running · expired · closed · abandoned · dm_a_pago — expiry effects per kind (tributes due · abandono · DM a pago) | FR-064, FR-066, FR-068, FR-074 |
| l10n_sv_special_regime.customs_clock | expiry_effect · lesia_pointer | select · flag | tribute_obligation (12_/14_ expiry) — sanction consequences NOT modeled (SOQ-32/OQ-1) | FR-066, FR-068 |
| l10n_sv_special_regime.customs_clock | warning_days | int (default 30) | operational pre-expiry alert — NON-statutory default, configurable (OQ-5) | FR-066 |
| l10n_sv_special_regime.customs_clock | duca_vencimiento_reconciled | computed | vs DUCA field 14 by id (06) — mismatch flag | FR-080 |

**Clock-kind config (l10n_sv_special_regime.clock_kind — dated rows, instrument provenance):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.clock_kind | kind · duration | select · int+unit+day_kind | values as printed: 12 MESES IMPRORROGABLES (zf_dpa_admision_12m — extendable FALSE by design) · 12 meses (traslado_definitivo_12m · traslado_zf_a_dpa_12m) · 6 meses (traslado_temporal_6m · reimport_pasivo_6m) · 2 meses (traslado_zf_dpa_a_tan_2m) · 3 días hábiles (formalizacion_3dh) · 24 MESES CALENDARIO (lsi_admision_temporal_24m — extendable +1y periods) · 1 año (centros_materias_1y) · 20 días hábiles (destinacion_20dh · expedicion_20dh) · 30 días hábiles (duca_f_fauca_30dh) · indefinite (parque_indefinido · centros_primaria_indefinido — no expiry) | FR-064..081 |
| l10n_sv_special_regime.clock_kind | extendable · envelope_rule | boolean · char | TRUE only on lsi_admision_temporal_24m (prior DGA authorization per extension); traslado_temporal_6m capped inside the 12m envelope | FR-065, FR-067, FR-074 |
| l10n_sv_special_regime.clock_kind | regime_family | select | zf_dpa · lsi — regime-exclusive resolution (a kind never resolves against the other family; the invariant encoded) | FR-065 |
| l10n_sv_special_regime.clock_kind | valid_from · valid_to · provenance | date · date · char | 12_/14_/43_ article as printed (SOQ-30); duca_f_fauca_30dh = 43_ field 56 (2018 print assumed current — SOQ-36) | FR-064..081 |

**Clock extensions (l10n_sv_special_regime.customs_clock.extension):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.customs_clock.extension | period_years · dga_authorization_ref · granted_on | int · char · date | +1-year periods; ONLY valid on lsi_admision_temporal_24m (constraint per FR-065); prior DGA authorization required per period | FR-074 |

**Traslados (l10n_sv_special_regime.traslado):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.traslado | kind · source/target | select · m2o×2 | definitivo · temporal · zf_a_dpa · zf_dpa_a_tan; regime profiles (intra-regime vs TAN companies — Art. 23 scope predicate FR-071) | FR-067, FR-068, FR-071 |
| l10n_sv_special_regime.traslado | dominion_transfer · nre_ref | boolean · m2o | non-dominion ⇒ NRE required (SV-EINV-FR-001/026 by id); pending-document state until attached | FR-070 |
| l10n_sv_special_regime.traslado | contratista_order_proof | char | no-dominion special case: traslado by order of the contratista, duly proven | FR-070 |
| l10n_sv_special_regime.traslado | sub_clock · return_state | m2o · select | the traslado clock row; out-of-time/non-return ⇒ dm_a_pago (Art. 26) | FR-067, FR-068 |
**LSI destinación + expedición (l10n_sv_special_regime.destinacion):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.destinacion | recepcion_efectiva_ref · discharge_date | char · date | stage-1 anchor (20-días-hábiles window; días hábiles via SV-FREP-FR-202..204 by id) | FR-074 |
| l10n_sv_special_regime.destinacion | regimen_optable | select | admision_temporal_24m · a) importación definitiva · b) exportación definitiva · c) importación temporal mismo estado · d) tránsito aduanero · e) reexportación · transito_interno (zf · dpa · deposito_aduanero) · aduana_interna ops I-VIII | FR-074, FR-075 |
| l10n_sv_special_regime.destinacion | client_request · abandono_state | boolean · select | destinación at client's request; window expiry ⇒ abandono (feeds `07`'s registers by id) | FR-074 |
| l10n_sv_special_regime.destinacion | expedicion_state · expedicion_deadline · inform_record | select · date · fields | en_expedición · exited · expired; deadline = 20 días hábiles from day after DM registration; inform = razón + acciones legales + date | FR-076 |

**Residuales + certificates + value edge (l10n_sv_special_regime.\*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.residual_disposition | kind · goods | select · char | tan_consumo_definitivo · botadero_autorizado · donacion; paletas de madera/plástico, bidones y similares | FR-079 |
| l10n_sv_special_regime.residual_disposition | valor_facturado · dm_simplificada_ref · delegacion_authorization | monetary · char · char | TAN path: duties on valor facturado a precios de mercado via DM simplificada; prior Delegación authorization on every path | FR-079 |
| l10n_sv_special_regime.residual_disposition | donation_minec_ref · donation_asamblea_ref | char · char | donation path: MINEC calificación + Órgano Legislativo exoneración (both required) | FR-079 |
| l10n_sv_special_regime.customs_control_certificate | reexport_dm_ref · requesting_party · tlc_instrument | m2o · char · char | issued by the park Delegación for reexports preserving TLC/integration origin benefits; DACG formatos = config slots, NO defaults | FR-078 |
| l10n_sv_special_regime.customs_value_exclusion | kind · separately_expressed · excluded_amount | select · boolean · monetary | almacenaje_conservacion_parque — excluded from valor en aduana ONLY when expressed separately from the price (feeds the DUCA value block, 06 by id) | FR-077 |

## 5. Odoo Mapping

Layer semantics for this wave: the customs clocks are Odoo-native dated
config/ledger rows (per-DM clock records on the regime profile, linked to
stock moves for goods tracking and to the DUCA mirroring surface owned by
`06`) — every FR maps `odoo`; no SaaS rows (no DTE generation/transmission
introduced; the NRE consumed by FR-070 is READ as a document reference, its
generation owned by the e-invoicing wave). Model names are stable across
Odoo 17/18/19/20; no version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-064 | odoo | l10n_sv_special_regime.customs_clock | dm_ref/clock_kind/anchor/duration/expiry/state | THE per-DM chassis; durations from dated clock_kind rows (D15); DM surface = 06 by id; profile link FR-003 by id |
| FR-065 | odoo | l10n_sv_special_regime.clock_kind | regime_family/extendable | THE invariant encoded: zf_dpa vs lsi families regime-exclusive; 12m improrrogable vs 24m prorrogable never share a row |
| FR-066 | odoo | l10n_sv_special_regime.customs_clock | kind zf_dpa_admision_12m | "DE HASTA" 12m cap (contract may shorten, never exceed); ZF Art.-17 goods/DPA capital goods carry no clock (Art. 21 frame); expiry ⇒ tribute obligations; LESIA = OQ-1 pointer, zero mechanics; warning_days default 30 = operational (OQ-5) |
| FR-067 | odoo | l10n_sv_special_regime.customs_clock (+.traslado link) | kinds traslado_* | anchors per print: first-admisión DM acceptance / traslado doc date (envelope-capped) / ZF-cancelling DM liquidación; no traslado extends Art. 22 (Art. 23) |
| FR-068 | odoo | l10n_sv_special_regime.customs_clock + .traslado | kind traslado_zf_dpa_a_tan_2m | DOS MESES; responsibility on the generating holder; out-of-time/non-return ⇒ dm_a_pago; receptor-cerrado ⇒ DGA disposal flag (Art. 40 kin = 07 by id) |
| FR-069 | odoo | l10n_sv_special_regime.customs_clock | kind formalizacion_3dh | días hábiles via SV-FREP-FR-202..204 by id; levante state per CAUCA note |
| FR-070 | odoo | l10n_sv_special_regime.traslado | dominion_transfer/nre_ref/contratista_order_proof | NRE = SV-EINV-FR-001 (04) + SV-EINV-FR-026 by id — read-only reference; LSI Art. 38 libre-circulación twin on the same surface; pending-document state when missing |
| FR-071 | odoo | l10n_sv_special_regime.traslado + res.company flag | scope predicates | ZF subcontracted processes; DPA repair-only + artesanías/textil/maquila/confección exception flag; one-time standing notice |
| FR-072 | odoo | l10n_sv_special_regime.customs_clock | kind reimport_pasivo_6m | distinct from FR-068 2m (do-not-merge); duties on non-national value-added only, NMF; asimilación perfeccionamiento pasivo; DGA formulario = config slot |
| FR-073 | odoo | l10n_sv_special_regime.customs_clock | kinds parque_indefinido/centros_materias_1y/centros_primaria_indefinido | liberatorio/indefinite = no expiry row; centros 1y from DM acceptance; capital goods = franquicia-definitiva terminal state; tax routing = 05 by id |
| FR-074 | odoo | l10n_sv_special_regime.destinacion + customs_clock | two-stage: destinacion_20dh + lsi_admision_temporal_24m | discharge anchor (recepción efectiva, Art. 32 kin); expiry ⇒ abandono; +1y extensions ONLY here (DGA authorization ref per period; FR-065 constraint) |
| FR-075 | odoo | l10n_sv_special_regime.destinacion | regimen_optable | a)-e) + tránsito interno (zf/dpa/depósito) + aduana-interna ops I-VIII, as printed |
| FR-076 | odoo | l10n_sv_special_regime.destinacion | expedicion_state/deadline/inform_record | 20 días hábiles from day after DM registration; inform = razón + acciones legales, pending-flagged at expiry |
| FR-077 | odoo | l10n_sv_special_regime.customs_value_exclusion | separately_expressed gate | almacenaje/conservación excluded ONLY when expressed separately; feeds the DUCA value block (06 by id) |
| FR-078 | odoo | l10n_sv_special_regime.customs_control_certificate | reexport refs | origin-benefit preservation records; DACG formatos = config slots, NO defaults (SOQ-44 kin) |
| FR-079 | odoo | l10n_sv_special_regime.residual_disposition | 3 paths | valor facturado + DM simplificada / botaderos free / donations MINEC+Asamblea; delegación authorization on every path; 17b_ procedures = pointer |
| FR-080 | odoo | l10n_sv_special_regime.customs_clock | duca_vencimiento_reconciled | consumes DUCA field 14 BY ID from 06 (forward ref, final review resolves); mismatch flag, never auto-overwrite; mandatory-vs-optional = OQ-2 |
| FR-081 | odoo | l10n_sv_special_regime.customs_clock | kind duca_f_fauca_30dh | 30 días hábiles from emission; export-country-only scope flag; clock view here, declaration-record surface = 06 by id (OQ-6 split note) |

Version-regime notes (D12/D15/D16/D18/D19): all clock durations, windows and
units in this file (12 MESES IMPRORROGABLES, 12m/6m/2m traslado clocks,
3-días-hábiles formalización, 6-month passive reimport, 24 MESES CALENDARIO
+ 1-year extensions, 1-year centros clock, 20-días-hábiles destinación and
expedición windows, 30-días-hábiles DUCA-F FAUCA validity) are code-text
values cited as printed under the SOQ-30 verification watch (§2) and live as
dated clock-kind rows with instrument provenance — never constants; each
running clock resolves as-of its own anchor (DM acceptance / liquidación /
traslado date / ingreso / discharge / DM registration / emission) with
snapshot-on-write. Mid-year go-live (D18): a migrating regime company
ingests its open clocks, extensions and states as `is_historical` rows with
original-period semantics (tiered ingestion; no re-derivation — the ZF 12m
and LSI 24m family split is preserved on imported rows). No hard gates
beyond the statutory expiry states (D16 no-override: a regime clock is
never extended by configuration; LSI extensions exist only through the
DGA-authorization event).

## 6. Acceptance Criteria

- **AC-001:** Given a ZF/DPA DM accepted 2026-03-10 covering
  perfeccionamiento goods, when the clock row opens, then the computed
  expiry is 2027-03-10, marked IMPRORROGABLE — an extension attempt on this
  kind is rejected by config (no extension row attachable), the
  pre-expiry warning fires 30 days before expiry (operational default),
  and at expiry the tribute-obligation state stamps with the LESIA
  pointer recorded and NO sanction mechanics applied (FR-064..066).
- **AC-002:** Given the same goods destined under the LSI regime
  (destinación to admisión temporal, DM accepted 2026-03-10), when the
  clock row opens, then the expiry computes 2028-03-10 with the extension
  surface available, and a DGA-authorized +1-year extension granted
  2028-02-01 moves the expiry to 2029-03-10 — the row and the ZF row of
  AC-001 never share a clock kind (FR-065, FR-074).
- **AC-003:** Given a DPA with a 12m envelope opened 2026-01-10 and a
  temporary traslado out on 2026-02-01, when the goods return 2026-07-01
  (5 months), then the 6-month sub-clock passes inside the envelope; when
  another lot returns 2026-09-01 (7 months), then the sub-clock breach
  flags with the tribute-obligation state and the envelope computation is
  unchanged by either traslado (FR-067).
- **AC-004:** Given a non-dominion traslado between two beneficiaries
  recorded without an NRE reference, when the traslado saves, then it
  stays in pending-document state until the nota de remisión (e-invoicing
  doc type by id) is attached — and a traslado documented as by order of
  the contratista with proof passes the same gate (FR-070).
- **AC-005:** Given goods discharged at a usuario directo's installations
  on 2026-05-04 with no destinación recorded, when the 20th día hábil
  after discharge elapses, then the goods stamp the abandono state (day-21
  recording arrives too late) and the state feeds the register surfaces of
  `07` by id (FR-074).
- **AC-006:** Given TAN goods entered into a zona franca 2026-01-15 for
  passive processing, when they reimport 2026-06-10, then the duty base is
  ONLY the non-national value-added aggregate at the NMF tariff; when
  another lot reimports 2026-08-01, then the out-of-term entry stamps the
  DM-a-pago state — and neither lot's clock is the 2-month traslado kind
  (FR-068, FR-072).
- **AC-007:** Given a DM registered in the DGA system on 2026-02-02, when
  the expedición deadline computes, then it resolves 20 días hábiles from
  2026-02-03 (the day after); goods still in expedición status at day 21
  flag expired with the información-duty record (razón + acciones legales)
  pending (FR-076).
- **AC-008:** Given a centro de servicios DM accepted 2026-04-01 for
  materias primas, when the clock opens, then the expiry is 2027-04-01;
  the same goods under a parque profile carry NO expiry row, and the
  centro's capital goods record the franquicia-definitiva terminal state
  (FR-073).
- **AC-009:** Given residual palets disposed to TAN, when the disposition
  records, then duties compute on the valor facturado a precios de mercado
  with the DM-simplificada reference stored; the same palets to an
  authorized botadero record zero duties; a donation records only with
  BOTH the MINEC calificación and the Asamblea exoneración references
  (FR-079).
- **AC-010:** Given a clock row computing expiry 2027-03-10 whose DUCA
  field-14 value (consumed from `06` by id) reads 2027-03-10, when the
  reconciliation runs, then the row passes; a DUCA value of 2027-05-10
  raises the mismatch flag without overwriting either side (FR-080).
- **AC-011:** Given a DUCA-F serving as FAUCA emitted 2026-06-01, when the
  validity computes, then it expires 30 días hábiles after emission with
  the export-country-only scope flag set — an in-country use at día hábil
  31 never consumes this clock (FR-081).
- **AC-012:** Given a parque destine-to-national-market operation with
  US$500 of almacenaje/conservación costs expressed separately from the
  price, when the customs value builds, then those costs are excluded from
  valor en aduana; the same US$500 embedded in the price stays in the base
  (FR-077).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-32 carried: the Ley Especial para Sancionar Infracciones Aduaneras (LESIA) is NOT in the corpus though cited by 12_ Art. 26 (Art. 5 literal q) for traslado-term breaches and by Arts. 26/40-A generally for expiry consequences — FR-066/FR-068/FR-072 stamp tribute obligations and state pointers ONLY, zero sanction mechanics invented; the sanction ladders and the defraudación crime elements live in `07_obligations-reporting-sanctions.md` (same SOQ-32 pointer). Acquisition candidate shared with 74_. | no | Takumi S7 (sources watch) | open |
| OQ-2 | SOQ-36 kin + DUCA field-number anchor: the master-index SR4 LB anchor prints "43_ (DUCA fields 33/56)", but the instructivo as printed numbers the regime-expiry field 14 ("Fecha de vencimiento del régimen") and the FAUCA-validity field 56 ("Válida hasta") — field 33 is "Peso neto total". This file cites fields 14/56 as printed; reconcile the master-index anchor at T9 final review. Additionally the Comité Aduanero user manual (mandatory-vs-optional fields per operation) is absent — whether field 14 must be consigned for every regime declaration is unverified; FR-080 reconciles whenever present. Res. 409-2018 supersession status also unverified (2018 text assumed current). | no | Takumi S7 (crossfile with T6; sources watch) | open |
| OQ-3 | SOQ-45 kin (crossfile with T6): DUCA field 31 "tasa de cambio" (peso centroamericano vs import-country currency at acceptance) — operational meaning post-dollarization is corpus-silent; NOT consumed by this file's clocks, recorded here as DUCA-fields family kin so the register maps it to `06_customs-declarations.md`. | no | Takumi S7 (crossfile with T6) | open |
| OQ-4 | SOQ-30 carried: the 12_ consolidation ends at D.L. 318-2013 and 14_/43_ are the 2007/2018 prints — post-cutoff reforms unverified until official routes recover; every LB in this file cites as printed; a post-cutoff reform may move clock durations, the 24-month/+1y structure, the destinación/expedición windows or the DUCA field layout — re-verify before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-5 | Pre-expiry warning window: the 30-day warning on clock expiry (AC-001) is an OPERATIONAL DEFAULT, not a statutory value — no corpus text prescribes any warning lead time; FR-066 ships warning_days = 30 as a labeled system default, configurable per deployment. | no | Takumi S7 (config watch) | open |
| OQ-6 | T4/T6 DUCA-F-FAUCA ownership split: the S7 plan assigns T6 a "DUCA-F validity FR" on the declaration record AND T4 this file's clock view (both briefs list the 30-días-hábiles FAUCA validity) — FR-081 owns the CLOCK row (expiry computation + export-country scope); `06_customs-declarations.md` owns the declaration-record field surface. Final wave review confirms the two FRs reference each other by id and duplicate nothing. | no | Takumi S7 (crossfile with T6) | open |
