# SV — Special regimes — Regime framework: beneficiary model, roles, qualification and breach states

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | special-regimes |
| Status  | draft |
| Authors | Takumi synthesis wave 7 (S7 special-regimes) |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the special-regimes chassis every other file of this wave
builds on: the territorial-regime taxonomy of the Ley de Zonas Francas
Industriales y de Comercialización (Industrial and Commercial Free-Trade Zones
Law, 12_) — *zona franca* (free zone, ZF) as extra-territorial for
import/export tributes vs *depósito para perfeccionamiento activo* (active
perfecting deposit, DPA) as a suspensive perfeccionamiento regime, two DISTINCT
regimes never unified — and the Ley de Servicios Internacionales
(International Services Law, LSI, 14_) *parque de servicios* (services park,
multi-company) vs *centro de servicios* (services center, single company)
pair with its *usuario directo/indirecto/consignación/mercancías destinadas*
role definitions; the beneficiary profile that keys every D15 dated row of
the wave (regime × role × activity admission × location track × *acuerdo*
D.O. date); the authorization architecture (MINEC authorizes, MH through DGA
+ DGII watches; ONI capital registration) and the DGA institutional frame
(13_); the activity-admission catalogs (ZF SAC scope + Art. 6 negative list;
LSI letters a)-j) with per-letter scope predicates + co-located non-benefited
1)-11)); the qualification *requisitos* as dated config rows (ZF 17-A/19-A/
19-B; LSI 22/23 médico); the breach state machine (revocación vs suspensión
with tributes payable and the benefit clock running; LSI third-grave
revocation; inactivity loss); the MINEC procedure clocks; the customs
*declarante*-role config (*agente aduanero* vs *apoderado especial aduanero*
vs self-declaration); and the 13-municipio *área metropolitana* stale-static
dated list that selects the metro/fuera location track.

It does **not** cover: the ZF/DPA exemption ladders and exception-goods gates
(`02_zf-exemption-schedules.md`); the LSI exemption shapes, local-market caps
and auditor dictamen (`03_lsi-regime.md`); the customs clocks
(`04_customs-clocks.md`); the TAN/IVA interface (`05_tan-iva-interface.md`);
DUCA/teledespacho declarations (`06_customs-declarations.md`); obligations,
DGA-facing reporting and SMM-priced sanctions (`07_obligations-reporting-
sanctions.md`); FOVIAL/COTRANS (`08_fovial-cotrans.md`). Those files consume
this one's beneficiary-profile and benefit-state model by FR id.

## 2. Legal Basis

Authority order (binding, per master evidence index §S7-A): ZF = **12_**
(D.L. Nº 405, 3-sep-1998, D.O. N° 176 T.340 23-sep-1998; consolidated through
reform (8) D.L. 318-2013; content title "Ley de Zonas Francas Industriales y
de Comercialización" — the registry title "Ley de Zonas Francas y Recintos
Comerciales" is the D.L. 461-1990 law this decree replaces, fixed W13); LSI =
**14_** (D.L. Nº 431, 11-oct-2007, D.O. N° 199 T.377 25-oct-2007; 2007 print,
header "Reformas: S/R") + **17b_** (Reglamento D. Nº 131, 4-dic-2008, D.O.
N° 235 T.381 12-dic-2008; its Art. 22 local-market caps, dictamen regime and
inventory-register contract are consumed by `03_lsi-regime.md` — this file
cites the reglamento only where the framework itself needs it); DGA frame =
**13_** (D. Nº 903, 14-dic-2005, D.O.
Nº 8 T.370 12-ene-2006; consolidated through reform (2) D.L. 121-2012);
customs chassis = **74_** (D.L. Nº 529, 13-ene-1999, D.O. N° 23 T.342
3-feb-1999; consolidated through reform (4) D.L. 23-2012).

**SOQ-30 verification note (rides EVERY regime LB in this file and this
wave):** all regime consolidations end 2012-2013 (12_ → D.L. 318-2013;
13_ → D.L. 121-2012; 74_ → D.L. 23-2012; 14_ → 2007/2008 prints with no
reform block) — post-cutoff reforms are unverified until official routes
recover (SOQ-22 kin); article text is cited **as printed**. Verbatim text
below is copied from the W13 evidence files (EVID-251..269) and, where the
evidence abbreviates, from the extraction txts
`sv/.extractions/12_Ley_Zonas_Francas.pdf.txt`,
`sv/.extractions/14_Ley_Servicios_Internacionales.pdf.txt`,
`sv/.extractions/13_Ley_Organica_Aduanas.pdf.txt` and
`sv/.extractions/74_Ley_Simplificacion_Aduanera_D529.pdf.txt` (citable per
standing S3 ruling 25; page pointers = txt PAGE markers). D15 discipline:
every requisito value, threshold and list in this file is a dated config row
with instrument provenance — never a global constant.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley de Zonas Francas, Art. 2 r): "ZONA FRANCA: ES EL ÁREA DEL TERRITORIO NACIONAL EN LA QUE SE PERMITE INGRESAR MERCANCÍAS QUE SE CONSIDERAN COMO SI NO ESTUVIESEN EN EL TERRITORIO ADUANERO NACIONAL, CON RESPECTO A LOS TRIBUTOS DE IMPORTACIÓN Y DE EXPORTACIÓN, PARA SER DESTINADAS SEGÚN SU NATURALEZA, A LAS OPERACIONES O PROCESOS PERMITIDOS POR LA PRESENTE LEY." Art. 2 h): "DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO O DPA: ES EL ÁREA DEL TERRITORIO NACIONAL SUJETA A UN TRATAMIENTO ADUANERO ESPECIAL, EN EL CUAL LAS MERCANCÍAS PUEDEN INGRESAR CON SUSPENSIÓN DE LOS TRIBUTOS A LA IMPORTACIÓN, PARA SER SOMETIDAS A UN PROCESO DE TRANSFORMACIÓN, ELABORACIÓN, REPARACIÓN U OTRO LEGALMENTE AUTORIZADO, PARA SU POSTERIOR REEXPORTACIÓN Y EN EL CUAL LOS BIENES DE CAPITAL PUEDEN PERMANECER INDEFINIDAMENTE…" | Free zone: the area of the national territory into which goods may enter that are considered as if NOT within the national customs territory with respect to import and export tributes, destined per their nature to the operations or processes permitted by this law. DPA: the area of national territory under special customs treatment in which goods may enter with SUSPENSION of import tributes to undergo transformation, elaboration, repair or other legally authorized process for subsequent RE-EXPORT, and in which capital goods may remain INDEFINITELY | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 2 h)/r) pp.2-4 (EVID-251; txt PAGE 2-4; SOQ-30 print) |
| LB-002 | Ley de Zonas Francas, Art. 2 d): "ÁREA METROPOLITANA: LA CONSTITUYEN LOS SIGUIENTES MUNICIPIOS: ANTIGUO CUSCATLÁN, SANTA TECLA, APOPA, AYUTUXTEPEQUE, CUSCATANCINGO, CIUDAD DELGADO, ILOPANGO, MEJICANOS, NEJAPA, SAN MARCOS SAN MARTÍN [sic], TONACATEPEQUE, SAN SALVADOR Y SOYAPANGO" | Metropolitan area: constituted by the following municipalities: Antiguo Cuscatlán, Santa Tecla, Apopa, Ayutuxtepeque, Cuscatancingo, Ciudad Delgado, Ilopango, Mejicanos, Nejapa, San Marcos San Martín [sic], Tonacatepeque, San Salvador and Soyapango | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 2 d) p.2 (EVID-251; txt PAGE 2; SOQ-30 print) |
| LB-003 | Ley de Zonas Francas, Art. 4: "EL ESTABLECIMIENTO, ADMINISTRACIÓN Y FUNCIONAMIENTO DE ZONAS FRANCAS SERÁ AUTORIZADO POR EL MINISTERIO DE ECONOMÍA. LA VIGILANCIA Y EL CONTROL DEL RÉGIMEN FISCAL DE DICHAS ZONAS CORRESPONDERÁ AL MINISTERIO DE HACIENDA, POR MEDIO DE LAS DIRECCIONES GENERALES DE ADUANAS E IMPUESTOS INTERNOS…" | The establishment, administration and operation of free zones is authorized by the Ministry of Economy (MINEC). Surveillance and control of the fiscal regime of said zones corresponds to the Ministry of Finance (MH) through the General Directorates of Customs (DGA) and Internal Taxes (DGII) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 4 p.7 (EVID-251; txt PAGE 7; SOQ-30 print) |
| LB-004 | Ley de Zonas Francas, Art. 5: "PODRÁN AMPARARSE A LA PRESENTE LEY, LAS PERSONAS NATURALES O JURÍDICAS, TITULARES DE EMPRESAS: a) QUE DESARROLLEN ZONAS FRANCAS DENOMINADOS DESARROLLISTAS; b) QUE ADMINISTREN ZONAS FRANCAS DENOMINADOS ADMINISTRADORES; c) QUE SE ESTABLEZCAN EN ZONAS FRANCAS DENOMINADOS USUARIOS; d) CUYOS ESTABLECIMIENTOS SEAN DECLARADOS DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO." | May take cover under this law natural or legal persons, holders of enterprises: a) that develop free zones, called desarrollistas (developers); b) that administer free zones, called administradores (administrators); c) that establish themselves in free zones, called usuarios (users); d) whose establishments are declared deposits for active perfecting (DPA titularities) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 5 p.7 (EVID-251; txt PAGE 7; SOQ-30 print) |
| LB-005 | Ley de Zonas Francas, Art. 3 (inciso primero + segundo): "PODRÁN ESTABLECERSE Y FUNCIONAR EN ZONA FRANCA EMPRESAS… QUE SE DEDIQUEN A: I. LA PRODUCCIÓN, ENSAMBLE O MAQUILA, MANUFACTURA, PROCESAMIENTO, TRANSFORMACIÓN O COMERCIALIZACIÓN DE BIENES INDUSTRIALES, COMPRENDIDOS EN EL CAPÍTULO 3 Y EN LOS CAPÍTULOS DEL 25 EN ADELANTE DEL SISTEMA ARANCELARIO CENTROAMERICANO, SAC, CON EXCEPCIÓN DE AQUÉLLOS QUE SE ENCUENTREN COMPRENDIDOS EN EL ARTÍCULO 6…; II. PESCA DE ESPECIES MARÍTIMAS PARA SER SOMETIDAS A TRANSFORMACIÓN INDUSTRIAL…; III. CULTIVO, PROCESAMIENTO Y COMERCIALIZACIÓN DE ESPECIES DE FLORA PRODUCIDA BAJO ESTRUCTURAS PROTEGIDAS EN INVERNADEROS Y LABORATORIOS…; IV. CRIANZA Y COMERCIALIZACIÓN DE ESPECIES DE ANFIBIOS Y REPTILES EN CAUTIVERIO…; V. DESHIDRATACIÓN DE ALCOHOL ETÍLICO." "…AQUÉLLAS NECESARIAS PARA LA PRODUCCIÓN… TALES COMO: DISEÑO, PINTADO, CORTE, ESTAMPADO, ACABADOS, SERIGRAFÍA, BORDADO, LAVADO, PLANCHADO, CONTROL DE CALIDAD, RECICLAJE Y REPARACIÓN. DICHAS ACTIVIDADES DE SERVICIOS SÓLO PODRÁN SER PRESTADAS ENTRE LOS BENEFICIARIOS DE LA PRESENTE LEY." | Enterprises established and operating in a free zone may engage in: I. production, assembly or maquila, manufacture, processing, transformation or commercialization of industrial goods comprised in Chapter 3 and Chapters 25 onward of the SAC, except those in Art. 6; II. fishing of marine species for industrial transformation; III. cultivation, processing and commercialization of flora produced under protected greenhouse and laboratory structures; IV. raising and commercialization of amphibian and reptile species in captivity; V. dehydration of ethyl alcohol. The connected services (design, painting, cutting, stamping, finishing, serigraphy, embroidery, washing, ironing, quality control, recycling and repair) may ONLY be provided AMONG the beneficiaries of this law | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 3 I-V pp.5-6 (EVID-252; txt PAGE 5-6; SOQ-30 print) |
| LB-006 | Ley de Zonas Francas, Art. 6: "NO PODRÁN ACOGERSE A LO ESTABLECIDO EN ESTA LEY, LAS PERSONAS… QUE SE DEDIQUEN A LAS ACTIVIDADES SIGUIENTES: a) EXPLORACIÓN, EXPLOTACIÓN, PROCESAMIENTO Y COMERCIALIZACIÓN DE GAS NATURAL, PETRÓLEO Y SUS DERIVADOS COMBUSTIBLES…; b) PRODUCCIÓN Y COMERCIALIZACIÓN DE CEMENTO Y CLINKER; c) COMERCIALIZACIÓN DE CHATARRA…; d) PRODUCTOS MINERALES… PROVENIENTES DE LA EXPLOTACIÓN DEL SUBSUELO SALVADOREÑO; e)… EXPLOSIVOS Y MATERIALES RADIOACTIVOS; f) LA PRODUCCIÓN O ALMACENAMIENTO DE MERCANCÍAS… CAUSANTES DE CONTAMINACIÓN…; g) …AZÚCAR, SUS SUSTITUTOS, DERIVADOS Y SUBPRODUCTOS…; h) …ALCOHOL DE CUALQUIER ORIGEN…, SALVO LO ESTABLECIDO EN EL ROMANO V, DEL Art. 3 DE ESTA LEY; i) …SACOS O COSTALES, DE FIBRAS SINTÉTICAS O ARTIFICIALES; j) SUMINISTRO DE ALIMENTOS PREPARADOS O NO…; k) IMPORTACIÓN DE MAQUINARIA Y EQUIPO CON FINES DE ARRENDAMIENTO. TAMPOCO PODRÁN ACOGERSE…: 1) LAS PERSONAS… A QUIENES SE LES HAYA SUSPENDIDO O REVOCADO LOS BENEFICIOS…; 2) LAS SOCIEDADES EN LAS QUE FIGUREN COMO DIRECTORES, REPRESENTANTES LEGALES… SOCIOS O ACCIONISTAS… QUE FUNGIERON EN TALES CARGOS… EN OTRAS SOCIEDADES A LAS CUALES LES FUERON SUSPENDIDOS O REVOCADOS LOS BENEFICIOS…; 3) CUANDO LAS ACTIVIDADES… CONLLEVEN UN OBJETO ILÍCITO…; 4) LAS PERSONAS… QUE… TENGAN OBLIGACIONES ADUANERAS Y/O TRIBUTARIAS FIRMES EN SEDE ADMINISTRATIVA PENDIENTES DE CUMPLIR." (numerals 1) and 2) inapplicable when the suspension/revocation was voluntary and not for infringements) | May NOT take cover under this law persons dedicated to: a) exploration/exploitation/processing/sale of natural gas, petroleum and fuel derivatives; b) cement and clinker; c) ferrous/non-ferrous scrap; d) subsuelo minerals; e) explosives and radioactive materials; f) polluting/health-harmful goods; g) sugar, substitutes, derivatives and byproducts (and goods incorporating them); h) alcohol of any origin EXCEPT Art. 3 V dehydration; i) synthetic-fiber sacks; j) prepared-food supply to benefited employees/enterprises; k) machinery import for leasing. Nor: 1) persons whose benefits were suspended/revoked; 2) societies whose directors/legal representatives/partners held such roles in other societies whose benefits were suspended/revoked; 3) illicit-object activities; 4) persons with firm pending customs/tax obligations (1-2 inapplicable to voluntary suspensions) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 6 a)-k) + 1)-4) pp.7-9 (EVID-252; txt PAGE 7-9; SOQ-30 print) |
| LB-007 | Ley de Zonas Francas, Art. 17-A: "…DEBERÁN CUMPLIR AL MENOS, CON UNO DE LOS REQUISITOS SIGUIENTES: a) INVERSIÓN INICIAL EN ACTIVO FIJO POR UN MONTO IGUAL O MAYOR A QUINIENTOS MIL DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA (US$500,000.00), ALCANZABLE EN LOS PRIMEROS DOS AÑOS DE OPERACIONES; b) OPERAR CON UN NÚMERO IGUAL O MAYOR A CINCUENTA (50) PUESTOS DE TRABAJO PERMANENTES, DESDE EL PRIMER AÑO DE OPERACIONES; c) OPERAR CON UN NÚMERO IGUAL O MAYOR A CINCO (5) PUESTOS DE TRABAJO PERMANENTES, DESDE EL PRIMER AÑO DE OPERACIONES, EN EL CASO DE COMERCIALIZADORES." "CUANDO EL MINISTERIO DE ECONOMÍA DETERMINE QUE HA EXISTIDO INCUMPLIMIENTO DEL REQUISITO… LITERAL a)…, SE LE REVOCARÁ EL ACUERDO DE AUTORIZACIÓN AL USUARIO." "EN EL CASO DE INCUMPLIMIENTO DE LOS LITERALES b) Y c)…, SE LE SUSPENDERÁN LOS DERECHOS… HASTA QUE SUBSANE DICHO INCUMPLIMIENTO; POR TANTO, DEBERÁ PAGAR DURANTE DICHO PERÍODO LOS TRIBUTOS APLICABLES A LAS IMPORTACIONES QUE REALICE Y LOS DEMÁS IMPUESTOS RELACIONADOS." (invernaderos/laboratorios block: "…a) INVERSIÓN INICIAL… IGUAL O MAYOR A CIEN MIL DÓLARES… (US$100,000), EN EL PRIMER AÑO…; b) OPERAR CON UN NÚMERO IGUAL O MAYOR A QUINCE (15) PUESTOS…; c) DISPONER UN ÁREA MÍNIMA DE CINCO MIL (5,000) METROS CUADRADOS, EN EL CASO DE INVERNADEROS Y DE MIL (1,000) METROS CUADRADOS, EN EL CASO DE LABORATORIOS; d) ESTRUCTURA ADMINISTRATIVA Y FINANCIERA FORMAL." — with the same revocación a)/suspensión b)-d) split; suspension block adds: "EL PLAZO DE LA SUSPENSIÓN NO INTERRUMPE EL CÓMPUTO DEL PLAZO TOTAL DE LOS BENEFICIOS.") | ZF usuario applicants must meet at least ONE of: a) initial fixed-asset investment ≥ US$500,000.00, attainable within the first two years of operations; b) ≥50 permanent jobs from the first year; c) ≥5 permanent jobs from the first year in the case of comercializadores (marketers). Breach of a) ⇒ the authorization acuerdo is REVOKED; breach of b)/c) ⇒ rights SUSPENDED until cured, paying during that period the tributes applicable to imports made and other related taxes. Greenhouse/laboratorio usuarios: a) ≥US$100,000 first-year investment; b) ≥15 permanent jobs; c) minimum area 5,000 m² (greenhouses) / 1,000 m² (laboratories); d) formal administrative and financial structure — same split, and the suspension period does NOT interrupt the total benefit term | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 17-A pp.17-19 (EVID-255; txt PAGE 17-19; SOQ-30 print) |
| LB-008 | Ley de Zonas Francas, Art. 19-A: "…DPA… DEBERÁN CUMPLIR AL MENOS, UNO DE LOS REQUISITOS SIGUIENTES: a) INVERSIÓN INICIAL EN ACTIVO FIJO POR UN MONTO IGUAL O MAYOR A OCHOCIENTOS MIL DÓLARES DE LOS ESTADOS UNIDOS DE AMÉRICA (US$800,000), ALCANZABLE EN LOS PRIMEROS DOS AÑOS DE OPERACIONES. NO SE CONTABILIZARÁ COMO INVERSIÓN INICIAL LA ADQUISICIÓN DE INFRAESTRUCTURA EXISTENTE; b) OPERAR CON UN NÚMERO IGUAL O MAYOR A SETENTA Y CINCO (75) PUESTOS DE TRABAJO PERMANENTES, DESDE EL PRIMER AÑO…; c) OPERAR CON UN NÚMERO NO MENOR A QUINCE (15) PUESTOS DE TRABAJO PERMANENTES…, EN EL CASO DE COMERCIALIZADORES." (same a)-breach revocación / b)-c)-breach suspensión split as 17-A) | DPA applicants must meet at least ONE of: a) initial fixed-asset investment ≥US$800,000 attainable within the first two years — acquisition of EXISTING infrastructure does not count as initial investment; b) ≥75 permanent jobs from the first year; c) ≥15 permanent jobs in the case of comercializadores (same revocación/suspensión enforcement split) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19-A pp.24-25 (EVID-255; txt PAGE 24-25; SOQ-30 print) |
| LB-009 | Ley de Zonas Francas, Art. 19-B: "LAS PERSONAS JURÍDICAS QUE SOLICITEN SER CALIFICADOS COMO DPA PARA DEDICARSE A ACTIVIDADES VINCULADAS CON ESPECIES DE ANFIBIOS Y REPTILES EN CAUTIVERIO, DEBERÁN CUMPLIR CON LOS REQUISITOS SIGUIENTES: a) INVERSIÓN INICIAL EN ACTIVOS FIJOS POR UN MONTO NO MENOR A CIEN MIL DÓLARES… (US$100,000), EN EL PRIMER AÑO…; b) OPERAR CON UN NÚMERO NO MENOR A QUINCE (15) PUESTOS DE TRABAJO PERMANENTES DESDE EL PRIMER AÑO…; c) ESTRUCTURA ADMINISTRATIVA Y FINANCIERA FORMAL." | Legal persons seeking DPA qualification for amphibian/reptile-in-captivity activities must meet: a) fixed-asset investment ≥US$100,000 in the first year; b) ≥15 permanent jobs from the first year; c) formal administrative and financial structure (Art. 3 III greenhouse/flora activities follow the 17-A seventh-inciso requirements) | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 19-B pp.25-26 (EVID-255; txt PAGE 25-26; SOQ-30 print) |
| LB-010 | Ley de Zonas Francas, Art. 39: "LA PERSONA… BENEFICIADA POR ESTA LEY QUE DEJARE DE OPERAR LA EMPRESA…, POR CAUSAS IMPUTABLES A ÉSTE, DURANTE UN PERÍODO DE DOCE MESES CONTINUOS, PERDERÁ LA CATEGORÍA DE USUARIO DE ZONA FRANCA O DE DEPÓSITO PARA PERFECCIONAMIENTO ACTIVO, PREVIA AUDIENCIA AL INTERESADO POR EL TÉRMINO DE CINCO DÍAS HÁBILES… LA RESOLUCIÓN FINAL DEBERÁ PRONUNCIARSE DENTRO DE LOS DIEZ DÍAS POSTERIORES… LA DIRECCIÓN GENERAL DE ADUANAS DARÁ SEGUIMIENTO A TRAVÉS DE SU SISTEMA INFORMÁTICO, DEBIENDO DAR DE BAJA EN EL MISMO, A AQUELLAS EMPRESAS QUE INCURRIEREN EN TAL SITUACIÓN…" | A beneficiary that ceases operating its enterprise, for causes imputable to it, for a continuous TWELVE-MONTH period, loses its ZF-usuario or DPA category, after a five-días-hábiles hearing; final resolution within ten days thereafter. The DGA tracks this through its computer system and must deregister (dar de baja) affected companies in it | `sv/sources/12_Ley_Zonas_Francas.pdf` | Art. 39 p.39 (EVID-258; txt PAGE 39; SOQ-30 print) |
| LB-011 | Ley de Zonas Francas, Art. 45: "EL MINISTERIO DE ECONOMÍA DEBERÁ RESOLVER EN UN PLAZO DE 25 DÍAS HÁBILES LA SOLICITUD DE CALIFICACIÓN COMO USUARIO DE ZONA FRANCA Y EN UN PLAZO DE 35 DÍAS HÁBILES LA SOLICITUD PARA OPERAR COMO DPA… EL ACUERDO RESPECTIVO DEBERÁ EMITIRSE EN UN PLAZO NO MAYOR A DIEZ (10) DÍAS HÁBILES…" (same-zone amendments inciso: usuarios not modifying their authorized activity, solvent with social-security institutions, requiring expansions/diminutions or relocation WITHIN the same zona franca, file a notarized note; the acuerdo issues within 10 días hábiles). Art. 48: "…EL MINISTRO DE ECONOMÍA DARÁ AUDIENCIA AL PRESUNTO INFRACTOR PARA QUE EN EL TÉRMINO DE CINCO DÍAS HÁBILES, POSTERIORES AL DE LA NOTIFICACIÓN, SE PRONUNCIE… LA RESOLUCIÓN FINAL DEBERÁ SER PRONUNCIADA EN EL TÉRMINO DE DIEZ DÍAS." Art. 49: "…PROCEDERÁ EL RECURSO DE REVOCATORIA… EL CUAL DEBERÁ INTERPONERSE POR ESCRITO EN UN PLAZO DE TRES DÍAS HÁBILES CONTADOS A PARTIR DE LA NOTIFICACIÓN RESPECTIVA… RESOLVERÁ EN UN PLAZO DE QUINCE DÍAS HÁBILES…" | MINEC must resolve a ZF-usuario qualification application within 25 días hábiles and a DPA application within 35 días hábiles (the MH opinion period included); same-zone amendment acuerdos issue within 10 días hábiles. Infringement procedure: five-días-hábiles audiencia, final resolution within ten days. Revocatoria recourse filed within three días hábiles of notification, resolved within fifteen días hábiles | `sv/sources/12_Ley_Zonas_Francas.pdf` | Arts. 45/48/49 pp.40-42 (EVID-258; txt PAGE 40-42; SOQ-30 print) |
| LB-012 | Ley de Servicios Internacionales, Art. 2: a) "PARQUE DE SERVICIOS: ÁREA DELIMITADA QUE FORMANDO UN SOLO CUERPO, SE ENCUENTRA CERCADA Y AISLADA, SIN POBLACIÓN RESIDENTE, DONDE LOS BIENES QUE EN ELLA SE INTRODUZCAN Y LOS SERVICIOS QUE SE PRESTEN, SE CONSIDERAN FUERA DEL TERRITORIO ADUANERO NACIONAL…"; b) "CENTRO DE SERVICIOS: ÁREA DELIMITADA Y AISLADA… QUE SE CONSIDERA FUERA DEL TERRITORIO ADUANERO NACIONAL, EN VIRTUD DE CONSIDERARSE COMO UNA ZONA QUE GOZA DE EXTRATERRITORIALIDAD ADUANERA… DONDE… SE AUTORIZA EL ESTABLECIMIENTO DE UNA EMPRESA…"; c) "USUARIO DIRECTO: PERSONA… AUTORIZADA PARA PRESTAR SERVICIOS EN EL PARQUE O CENTRO DE SERVICIO…"; d) "USUARIO INDIRECTO: PERSONA…, ACREDITADO COMO PROPIETARIO DE LAS MERCANCÍAS… DESTINADA A SER INTERNADA EN UN PARQUE DE SERVICIOS PARA SOMETARSE A LAS OPERACIONES DE DISTRIBUCIÓN O LOGÍSTICA INTERNACIONAL, A CARGO DE UN USUARIO DIRECTO CALIFICADO…"; e) "CONSIGNACIÓN DE MERCANCÍAS: ACTO JURÍDICO… CONFÍA LA CUSTODIA, MANEJO Y DISTRIBUCIÓN DE SUS MERCANCÍAS A UN USUARIO DIRECTO…"; f) "MERCANCÍAS DESTINADAS: SON AQUELLAS MERCANCÍAS QUE UNA PERSONA… NOTIFICA, ENVÍA, ENTREGA Y/O CONSIGNA AL USUARIO DIRECTO CALIFICADO…" | Services park: a delimited, fenced and isolated single-body area without resident population where introduced goods and provided services are considered OUTSIDE the national customs territory. Services center: a delimited isolated area enjoying customs extraterritoriality where the establishment of ONE enterprise is authorized. Usuario directo: person authorized to provide services in the park or center. Usuario indirecto: person accredited as owner of goods to be entered into a park for international distribution/logistics operations in charge of a qualified usuario directo. Consignación: the legal act by which goods custody, handling and distribution are entrusted to a usuario directo. Mercancías destinadas: goods notified, sent, delivered and/or consigned to the qualified usuario directo | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 2 a)-f) pp.1-3 (EVID-259; txt PAGE 1-3; SOQ-30 print) |
| LB-013 | Ley de Servicios Internacionales, Art. 3: "PARA SER SUJETO A LOS BENEFICIOS…, LOS INVERSIONISTAS NACIONALES O EXTRANJEROS DEBERÁN REGISTRAR PREVIAMENTE EL CAPITAL, DE CONFORMIDAD A LA LEY DE INVERSIONES, EN LA OFICINA NACIONAL DE INVERSIONES, ONI, LA CUAL EMITIRÁ LA RESOLUCIÓN CORRESPONDIENTE EN UN PLAZO NO MAYOR A 5 DÍAS HÁBILES." Art. 7: "LA APLICACIÓN DE LA PRESENTE LEY CORRESPONDERÁ AL MINISTERIO DE ECONOMÍA. LA VIGILANCIA Y CONTROL EFECTIVO DEL RÉGIMEN ADUANERO Y FISCAL DE LOS PARQUES Y CENTROS DE SERVICIOS CORRESPONDERÁ AL MINISTERIO DE HACIENDA…" | To be subject to the benefits, national or foreign investors must PREVIOUSLY register capital per the Investment Law with the Oficina Nacional de Inversiones (National Investments Office, ONI), which issues the corresponding resolution within no more than 5 días hábiles. Application of the law corresponds to MINEC; effective surveillance and control of the customs and fiscal regime of parks and centers corresponds to MH | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Arts. 3/7 pp.3/5 (EVID-259; txt PAGE 3, 5; SOQ-30 print) |
| LB-014 | Ley de Servicios Internacionales, Art. 5 (letters, scope fragments): a) "DISTRIBUCIÓN INTERNACIONAL: …ALMACENAMIENTO, ACOPIO, CONSOLIDACIÓN Y DESCONSOLIDACIÓN DE MERCANCÍAS DE TERCEROS… SIN TRANSFORMAR LA NATURALEZA DE LAS MISMAS…"; b) "OPERACIONES INTERNACIONALES DE LOGÍSTICA: …PLANIFICACIÓN, CONTROL Y MANEJO DE INVENTARIOS, SELECCIÓN, EMPAQUE, EMBALAJE, FRACCIONAMIENTO, CLASIFICACIÓN, ENVIÑETADO, ETIQUETADO, ROTULADOS, FACTURACIÓN, INSPECCIÓN DE CARGA Y OTRAS ACTIVIDADES QUE NO TRANSFORMEN SUSTANCIALMENTE LA NATURALEZA…"; c) "CENTRO INTERNACIONAL DE LLAMADAS… call center…"; d) "TECNOLOGÍAS DE INFORMACIÓN: …SERVICIOS PRESTADOS… A PERSONAS JURÍDICAS DOMICILIADAS FUERA DEL TERRITORIO NACIONAL, EN DISEÑO Y DESARROLLO DE SOFTWARE…"; e) "INVESTIGACIÓN Y DESARROLLO…"; f) "REPARACIÓN Y MANTENIMIENTO DE EMBARCACIONES MARÍTIMAS…"; g) "REPARACIÓN Y MANTENIMIENTO DE AERONAVES…"; h) "PROCESOS EMPRESARIALES… BPO's…"; i) "SERVICIOS MÉDICO-HOSPITALARIOS: …PRESTADOS POR UNA ENTIDAD HOSPITALARIA A PACIENTES CON DOMICILIO PERMANENTE FUERA DEL ÁREA DE CENTROAMÉRICA, SE EXCEPTÚA… MEDICINA GENERAL Y ODONTOLÓGICOS"; j) "SERVICIOS FINANCIEROS INTERNACIONALES…". (final inciso) "…PODRÁN INSTALARSE EN PARQUES DE SERVICIOS, SIN GOZAR DE LOS BENEFICIOS… QUEDANDO OBLIGADOS AL CUMPLIMIENTO DE LAS NORMAS TRIBUTARIAS NACIONALES VIGENTES…: 1) HOTELES. 2) LÍNEAS AÉREAS: 3) GENERACIÓN, SUMINISTRO Y DISTRIBUCIÓN DE ENERGÍA ELÉCTRICA. 4) COMUNICACIONES Y TELECOMUNICACIONES; EXCEPTO… CALL CENTERS Y LAS EMPRESAS TELEFÓNICAS QUE NO POSEAN REDES FIJAS PROPIAS… TERMINACIÓN DE TRÁFICO INTERNACIONAL ENTRANTE; SIN EMBARGO ESTAS ÚLTIMAS NO GOZARÁN DE LOS BENEFICIOS QUE CONFIEREN LOS ARTÍCULOS 21 Y 25…; 5) BANCARIOS, FINANCIEROS Y DE SEGUROS…; 6) TRANSPORTE…; 7) TURÍSTICOS… COURIES. 8) PROFESIONALES Y TÉCNICOS…; 9) SUMINISTRO DE ALIMENTOS…; 10) CUALQUIER TIPO O MECANISMO DE SEGURIDAD PRIVADA. 11) ARRENDAMIENTO DE CUALQUIER NATURALEZA, EXCEPTO EL PRESTADO POR LOS ADMINISTRADORES A LOS USUARIOS DIRECTOS…" | Benefited international-services activities: a) international distribution (third-party storage, gathering, consolidation/deconsolidation without transforming nature); b) international logistics operations (inventory planning/control/handling, selection, packing, packaging, fractioning, classification, labeling, invoicing, cargo inspection — no substantial transformation); c) international call centers; d) information technologies (software design/development TO legal persons domiciled outside the national territory); e) research and development; f) ship repair/maintenance; g) aircraft repair/maintenance; h) business processes (BPO); i) medical-hospital services provided to patients PERMANENTLY DOMICILED OUTSIDE the Central America area (general medicine and dental excepted); j) international financial services. Co-located NON-benefited 1)-11) (hotels, airlines, energy, communications except call centers/no-network international-traffic terminators — which also lose Arts. 21/25 benefits, banking/insurance, transport, tourism/courier, professional/technical, food supply, private security, leasing except administrator-to-usuario) operate under ordinary national tax law | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 5 a)-j) + 1)-11) pp.3-5 (EVID-260; txt PAGE 3-5; SOQ-30 print) |
| LB-015 | Ley de Servicios Internacionales, Art. 6: "LAS PERSONAS… A LAS QUE SE REFIEREN LOS LITERALES: a), b), d), e), h), i), ASÍ COMO EL LITERAL j)…, SÓLO PODRÁN OPERAR EN PARQUES DE SERVICIOS… LOS SERVICIOS… f) Y g) QUE REQUIEREN CARACTERÍSTICAS FÍSICO-ESPACIALES PARTICULARES… PODRÁN OPTAR A DESARROLLAR SU ACTIVIDAD EN EL TERRITORIO ADUANERO NACIONAL, ASÍ COMO EN PUERTOS MARÍTIMOS Y AÉREOS, LOS CUALES DEBERÁN SER PREVIAMENTE CALIFICADOS COMO CENTRO DE SERVICIOS… EN EL CASO DEL LITERAL c), PODRÁN OPERAR EN PARQUES DE SERVICIOS O CENTROS DE SERVICIOS." | Letters a), b), d), e), h), i) and j) may operate ONLY in parques de servicios; f) (ships) and g) (aircraft), requiring particular physical-spatial characteristics, may operate in the national customs territory and in maritime/air ports previously qualified as centros de servicios; c) (call centers) may operate in parks or centers | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 6 p.5 (EVID-260; txt PAGE 5; SOQ-30 print) |
| LB-016 | Ley de Servicios Internacionales, Art. 8 (second inciso, aeronautical export rule): "…TAMBIÉN SE CONSIDERA EXPORTACIÓN EL SERVICIO… g)… DEL ARTÍCULO 5…, PRESTADO A UNA PERSONA… DEDICADA A LA OPERACIÓN DE LÍNEAS AÉREAS QUE REALICEN VUELOS INTERNACIONALES, INDEPENDIENTE DE SU DOMICILIO Y DONDE UTILICE EL SERVICIO." | It is also considered exportation: the Art. 5 g) aircraft service provided to a person operating airlines making international flights, REGARDLESS of its domicile and where the service is used (the general export test is owned by `05_tan-iva-interface.md` by id) | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 8 inc. 2 p.6 (EVID-261; txt PAGE 6; SOQ-30 print) |
| LB-017 | Ley de Servicios Internacionales, Art. 10: "GOZARÁN DE LOS BENEFICIOS… LAS PERSONAS… TITULARES DE EMPRESAS, QUE: a) DESARROLLEN PARQUES DE SERVICIOS O DESARROLLISTAS. b) ADMINISTREN PARQUES DE SERVICIOS O ADMINISTRADORES. c) SE ESTABLEZCAN Y OPEREN EN PARQUES DE SERVICIOS O USUARIOS DIRECTOS. d) SE ESTABLEZCAN Y OPEREN EN CENTROS DE SERVICIOS." | Benefit holders: enterprise holders that a) develop services parks (desarrollistas); b) administer services parks (administradores); c) establish and operate in services parks (usuarios directos); d) establish and operate in services centers | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 10 p.8 (EVID-259; txt PAGE 8; SOQ-30 print) |
| LB-018 | Ley de Servicios Internacionales, Art. 22: "LOS USUARIOS DIRECTOS, ACTUANDO COMO DISTRIBUIDORES INTERNACIONALES U OPERADORES LOGÍSTICOS, DEBERÁN CUMPLIR CON LOS REQUISITOS SIGUIENTES: a) DISPONER DE UN MÍNIMO DE 500 METROS CUADRADOS EN PROPIEDAD O ARRENDAMIENTO; EN CASO EXCEPCIONAL, LOS MINISTERIOS DE ECONOMÍA Y DE HACIENDA PODRÁN AUTORIZAR… MENOR CANTIDAD DE METROS CUADRADOS…; b) REGISTRAR ANTE LA DIRECCIÓN GENERAL DE ADUANAS, PARA EFECTO DE RECIBIR EL CÓDIGO DE ACCESO A LOS SISTEMAS INFORMÁTICOS DE SERVICIO DE ADUANAS. c) MANTENER UN REGISTRO ELECTRÓNICO DE INVENTARIOS Y UN SISTEMA EN LÍNEA A DISPOSICIÓN DEL SERVICIO DE ADUANAS…; d) CONSERVAR LAS COPIAS DE LOS MANIFIESTOS DE CARGA CONSOLIDADA… POR UN PLAZO DE 5 AÑOS. e) PRESENTAR ANTE LA AUTORIDAD ADUANERA LOS BULTOS…; f) RESPONDER… POR DIFERENCIAS DE LOS MÁRGENES… EN TÉRMINOS DE CANTIDAD, NATURALEZA Y VALOR DE LAS MERCANCÍAS DECLARADAS…; g) RESPONDER POR EL PAGO DE IMPUESTOS DE SUS CLIENTES USUARIOS INDIRECTOS, EN CASO DE FALTANTES DE INVENTARIOS, EXTRAVÍOS, PÉRDIDAS Y MERMAS." | Usuarios directos acting as international distributors or logistics operators must: a) hold a minimum of 500 square meters owned or leased (MINEC+MH may exceptionally authorize less); b) register with the DGA to receive the access code to customs computer systems; c) keep an electronic inventory register and online system at the customs service's disposal, issuing warehouse entry/exit documents; d) keep consolidated-cargo manifest copies for 5 years; e) present the transported bultos to the customs authority and assign loading/unloading equipment and personnel; f) answer for quantity/nature/value differences between declared and actually arrived goods (recourse against the carrier when proven); g) answer for their usuario-indirecto clients' taxes in case of inventory shortfalls, losses, misplacements and shrinkage | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 22 a)-g) pp.12-13 (EVID-262; txt PAGE 12-13; SOQ-30 print) |
| LB-019 | Ley de Servicios Internacionales, Art. 23: "…COMO USUARIOS DIRECTOS PARA PRESTAR SERVICIOS DE PROCESOS EMPRESARIALES…: a) NUEVA INVERSIÓN EN ACTIVOS POR UN MONTO NO MENOR A CIENTO CINCUENTA MIL DÓLARES… (US$150,000) EN EL PRIMER AÑO DE OPERACIONES; CORRESPONDIENTE A CAPITAL DE TRABAJO Y ACTIVOS FIJOS. b) OPERAR CON UN NÚMERO NO MENOR A DIEZ PUESTOS DE TRABAJO PERMANENTES. c) POSEER CONTRATO MÍNIMO ESCRITO DE UN AÑO. EN EL CASO DE NO CUMPLIR CON LOS LITERALES ANTERIORES, LA EMPRESA NO GOZARÁ DE LOS BENEFICIOS… CORRESPONDIENTE AL EJERCICIO FISCAL DEL INCUMPLIMIENTO." (médico-hospitalario block): "1) NUEVA INVERSIÓN EN ACTIVOS FIJOS POR UN MONTO MÍNIMO DE DIEZ MILLONES DE DÓLARES… ($10,000,000.00), CUANDO EL PROYECTO SE DESTINE A… ENFERMEDADES CON INTERVENCIÓN QUIRÚRGICA; O DE UN MÍNIMO DE TRES MILLONES DE DÓLARES… ($3,000.000,00 [sic]) CUANDO NO CONLLEVE INTERVENCIÓN QUIRÚRGICA. 2) QUE EL PROYECTO SE UBIQUE FUERA DEL ÁREA METROPOLITANA DE SAN SALVADOR Y DE LAS CABECERAS DEPARTAMENTALES… 3) EN LOS CASOS… CON INTERVENCIÓN QUIRÚRGICA DEBERÁ BRINDARSE ÚNICAMENTE A PACIENTES CON SEGUROS CONTRATADOS CON COMPAÑÍAS ASEGURADORAS NACIONALES O EXTRANJERAS." | BPO usuario-directo applicants: a) new asset investment ≥US$150,000 in the first year of operations (working capital and fixed assets); b) ≥10 permanent jobs; c) a written contract of at least one year — on breach, the enterprise does NOT enjoy the law's benefits for the fiscal year of the breach. Medical-hospital: 1) new fixed-asset investment ≥US$10,000,000.00 for surgical-treatment projects, or ≥US$3,000,000.00 [sic print] for non-surgical; 2) located OUTSIDE the San Salvador metropolitan area and departmental capitals; 3) surgical services only to patients holding insurance with national or foreign insurers | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 23 + médico block pp.13-14 (EVID-262; txt PAGE 13-14; SOQ-30 print) |
| LB-020 | Ley de Servicios Internacionales, Art. 52: "…a) LA INFRACCIÓN MENOS GRAVE SE SANCIONARÁ CON PREVENCIÓN ESCRITA… LA REINCIDENCIA… MULTA EQUIVALENTE A TRES SALARIOS MÍNIMOS MENSUALES DE MAYOR CUANTÍA. b) LA INFRACCIÓN GRAVE… MULTA EQUIVALENTE A TREINTA SALARIOS MÍNIMOS MENSUALES DE MAYOR CUANTÍA. EN CASO DE REINCIDENCIA… CUARENTA… AL PRESENTARSE UNA TERCERA INFRACCIÓN GRAVE SE DECRETARÁ LA REVOCATORIA DE LOS BENEFICIOS. c) LA INFRACCIÓN MUY GRAVE… SUSPENSIÓN TEMPORAL DE LOS BENEFICIOS, POR EL TÉRMINO DE TRES MESES. LA REINCIDENCIA… REVOCATORIA…" | Less-serious infringement: written prevención (warning); recidivism, a fine of three highest-amount monthly minimum wages (SMM de mayor cuantía). Serious: 30 SMM (40 on recidivism); upon a THIRD serious infringement the REVOCATION of benefits is decreed. Very serious: three-month temporary suspension of benefits; recidivism, revocation | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 52 p.25 (EVID-264; txt PAGE 25; SOQ-30 print) |
| LB-021 | Ley de Servicios Internacionales, Art. 62: "SI ALGUNA PERSONA… ACOGIDA A LOS BENEFICIOS DE ESTA LEY DEJARA DE OPERAR, DURANTE UN PERÍODO DE TRES MESES CONTINUOS, DEBERÁN REVOCARSE LOS BENEFICIOS OTORGADOS…, SALVO FUERZA MAYOR O CASO FORTUITO, PREVIA APLICACIÓN DEL PROCEDIMIENTO… SI LA RESOLUCIÓN DETERMINA LA CANCELACIÓN DE LOS BENEFICIOS, LA DIRECCIÓN GENERAL DE ADUANAS PROCEDERÁ A INHABILITAR LOS ACCESOS AL SISTEMA INFORMÁTICO." | A beneficiary ceasing to operate for a continuous THREE-MONTH period must have its benefits revoked, save force majeure or fortuitous case, after the sanction procedure; if the resolution cancels the benefits, the DGA proceeds to DISABLE its computer-system accesses | `sv/sources/14_Ley_Servicios_Internacionales.pdf` | Art. 62 p.26 (EVID-264; txt PAGE 26; SOQ-30 print) |
| LB-022 | Ley Orgánica de la DGA, Art. 3: "LA DIRECCIÓN GENERAL DE ADUANAS ES EL ÓRGANO SUPERIOR JERÁRQUICO NACIONAL EN MATERIA ADUANERA, ADSCRITA AL MINISTERIO DE HACIENDA… FISCALIZAR Y RECAUDAR LOS DERECHOS E IMPUESTOS… ASÍ COMO CONTROLAR Y FISCALIZAR EL SUBSIDIO DEL GAS LICUADO DE PETRÓLEO." Art. 11: "…FORMARÁN PARTE DEL SERVICIO ADUANERO, LOS DEPÓSITOS DE ADUANAS, DELEGACIONES DE ADUANAS, ZONAS FRANCAS, DEPÓSITOS PARA PERFECCIONAMIENTO ACTIVO Y OTROS SIMILARES…" Art. 14: "LA DIRECCIÓN GENERAL, PODRÁ ESTABLECER DELEGACIONES DE ADUANAS EN LOS DEPÓSITOS, RECINTOS, ZONAS FRANCAS, PARQUES DE SERVICIOS Y OTROS LUGARES LEGALMENTE HABILITADOS…" | The DGA is the national superior hierarchical organ in customs matters, attached to MH, empowered to verify and collect duties and taxes. The customs service comprises customs deposits, customs delegations, FREE ZONES, DPAs and other similar; the DGA may establish customs delegations in deposits, precincts, free zones, SERVICES PARKS and other legally enabled places | `sv/sources/13_Ley_Organica_Aduanas.pdf` | Arts. 3/11/14 pp.2-3, 7, 8 (EVID-268; txt PAGE 2-3, 7, 8; SOQ-30 print) |
| LB-023 | Ley Orgánica de la DGA, Art. 36-A: "LA PERSONA NATURAL QUE SOLICITE LA AUTORIZACIÓN PARA ACTUAR COMO AGENTE ADUANERO, DEBERÁ ACREDITAR, ENTRE OTROS, LOS SIGUIENTES REQUISITOS: a) SER NACIONAL DE CUALQUIERA DE LOS ESTADOS PARTES; b) POSEER EL GRADO ACADÉMICO EN LICENCIATURA EN MATERIA ADUANERA; c) POSEER GRADO ACADÉMICO EN OTRAS DISCIPLINAS DE ESTUDIO, EN CUYO CASO… ACREDITAR COMO MÍNIMO DOS AÑOS DE EXPERIENCIA EN MATERIA ADUANERA; EN LOS CASOS… b) Y c)… LAS AUTORIDADES DE ADUANA PODRÁN PRACTICAR AL INTERESADO UN EXAMEN PSICOMÉTRICO." | A natural person requesting authorization to act as agente aduanero (customs agent) must, among others, accredit: a) nationality of any of the (CAUCA) States Parties; b) a licenciatura degree in customs matters, or c) a degree in other disciplines plus at least two years of customs experience; for b)/c) the customs authorities may administer a psychometric examination | `sv/sources/13_Ley_Organica_Aduanas.pdf` | Art. 36-A p.17 (EVID-268; txt PAGE 17; SOQ-30 print) |
| LB-024 | Ley de Simplificación Aduanera, Art. 9: "…PARA GARANTIZAR EL ACCESO GENERALIZADO AL TELEDESPACHO, LA PARTICIPACIÓN DE LOS AGENTES DE ADUANA O AGENTES ADUANEROS EN LA GESTIÓN DE LOS TRÁMITES ADUANEROS… SERÁ OPTATIVA PARA EL USUARIO, SIEMPRE QUE ÉSTE SEA UNA PERSONA JURÍDICA, QUIEN PODRÁ OBTENER UNA AUTORIZACIÓN DE LA DIRECCIÓN GENERAL PARA EFECTUAR POR SI MISMA SUS DECLARACIONES ADUANERAS, PARA LO CUAL DEBERÁ OTORGAR PODER DE REPRESENTACIÓN EN ESCRITURA PÚBLICA A FAVOR DE CUALQUIERA DE SUS EMPLEADOS QUE LA REPRESENTARÁ EN CALIDAD DE APODERADO ESPECIAL ADUANERO ANTE LAS ADUANAS DE LA REPÚBLICA, QUIENES SERÁN SOMETIDOS A UN EXAMEN DE SUFICIENCIA QUE VERSARÁ SOBRE MATERIAS ADUANERAS Y QUE PODRÁ COMPRENDER ADEMÁS PRUEBAS PSICOTÉCNICAS… UNA VEZ AUTORIZADO EL APODERADO ESPECIAL ADUANERO, LA PERSONA JURÍDICA PODERDANTE DEBERÁ RENDIR UNA FIANZA QUE SERÁ FIJADA POR LA DIRECCIÓN GENERAL… EL APODERADO ESPECIAL ADUANERO QUEDARÁ SUJETO… A LAS MISMAS DISPOSICIONES LEGALES QUE REGULAN… LA SUSPENSIÓN Y REVOCATORIA DE LA AUTORIZACIÓN PARA OPERAR DE LOS AGENTES DE ADUANA." | To guarantee generalized teledespacho access, the participation of customs agents in customs procedures is OPTIONAL for the user when the user is a persona jurídica, which may obtain DGA authorization to make its own customs declarations, granting a representation power in public deed (escritura pública) to any of its employees, who will represent it as apoderado especial aduanero (special customs attorney-in-fact) before the Republic's customs offices; they undergo a sufficiency examination on customs matters (possibly including psychometric tests). Once authorized, the granting legal person must post a bond (fianza) fixed by the DGA; the apoderado especial aduanero is subject to the same suspension/revocation rules as customs agents | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Art. 9 pp.7-8 (EVID-269; txt PAGE 7-8; SOQ-30 print) |
| LB-025 | Ley de Simplificación Aduanera, Art. 5: "…DICHAS CONSULTAS SERÁN EVACUADAS POR LA AUTORIDAD ADUANERA A MÁS TARDAR DENTRO DE LOS QUINCE DÍAS HÁBILES SIGUIENTES A SU RECEPCIÓN, Y SÓLO SURTIRÁN EFECTO EN EL CASO CONCRETO ESPECÍFICAMENTE CONSULTADO; DICHO PLAZO PODRÁ SER AMPLIADO DE OFICIO POR UN PERÍODO IGUAL… LA PRESENTACIÓN DE LA CONSULTA NO SUSPENDE EL CUMPLIMIENTO DE LAS OBLIGACIONES TRIBUTARIAS Y NO TRIBUTARIAS ADUANERAS." Art. 5-A: "…LOS CRITERIOS O RESOLUCIONES ANTICIPADAS, SE ACEPTARÁN CUANDO SE PRESENTEN ANTES QUE SE REALICE LA IMPORTACIÓN DE LA MERCANCÍA EN CUESTIÓN, LOS CUALES CONSERVARÁN SU VALIDEZ POR TRES AÑOS, SIEMPRE Y CUANDO NO HAYAN CAMBIADO LAS CONDICIONES QUE FUNDAMENTARON SU EMISIÓN…" | Pre-declaration consultations by any person with legitimate interest are answered within fifteen días hábiles (extendable ex officio by an equal period), effective ONLY for the specific case consulted; filing does not suspend customs/tax obligations. Advance criteria or resolutions are accepted when presented before the importation of the goods in question and keep their validity for THREE YEARS provided the conditions underlying their issuance have not changed | `sv/sources/74_Ley_Simplificacion_Aduanera_D529.pdf` | Arts. 5/5-A pp.3-4 (EVID-269; txt PAGE 3-4; SOQ-30 print) |

## 3. Functional Requirements

### 3.1 Territorial-regime taxonomy (12_ Art. 2; 14_ Art. 2)

- **SV-SPE-FR-001:** The system shall model ZF and DPA as two DISTINCT
  territorial regimes, never unified: *zona franca* — goods entering are
  considered as if NOT within the national customs territory with respect to
  import and export tributes; *depósito para perfeccionamiento activo* — an
  area under special customs treatment where goods enter with SUSPENSION of
  import tributes for transformation, elaboration, repair or other legally
  authorized process for subsequent re-export, capital goods remaining
  INDEFINITELY — the regime kind is a first-class discriminator on every
  beneficiary, customs and exemption record of this wave (consumed by
  `02`/`04`/`05` by id; the ZF/DPA 12-month clock vs LSI 24-month clock
  invariant is owned by `04_customs-clocks.md`).
  (LB-001; EVID-251)
- **SV-SPE-FR-002:** The system shall model the LSI territorial pair —
  *parque de servicios* (multi-company fenced extra-aduanal area, no resident
  population) vs *centro de servicios* (single-company customs-extraterritorial
  area, including locations in the national customs territory such as maritime
  and air ports per FR-009) — plus the four custody-role definitions of
  Art. 2: *usuario directo* (authorized service provider in park/center),
  *usuario indirecto* (accredited owner of goods entered into a park for
  distribution/logistics by a qualified usuario directo), *consignación de
  mercancías* (the act entrusting custody/handling/distribution to a usuario
  directo) and *mercancías destinadas* (goods notified/sent/delivered/
  consigned to the usuario directo) — parque vs centro is a second
  discriminator that keeps LSI rows distinct from ZF/DPA rows everywhere.
  (LB-012; EVID-259)

### 3.2 Beneficiary profile — the D15 row key (12_ Art. 5; 14_ Art. 10)

- **SV-SPE-FR-003:** The system shall carry, per beneficiary company, one
  regime profile whose fields form the D15 row key of the whole wave:
  regime (ZF · DPA · parque de servicios · centro de servicios), role
  (ZF: desarrollista · administrador · usuario · DPA titular; LSI:
  desarrollista · administrador · usuario directo · centro de servicios),
  activity admission (FR-006..009 config), location track (área
  metropolitana vs fuera — FR-022, ZF family), and *acuerdo* authorization
  date (D.O. publication of the MINEC acuerdo) — every exemption,
  requisito and clock row of `02`..`07` resolves against this key as-of its
  domain anchor and is snapshotted on the record (D15; never global
  constants).
  (LB-004; LB-017; EVID-251/259)

### 3.3 Authorization architecture + DGA institutional frame (12_ Art. 4; 14_ Arts. 3/7; 13_ Arts. 3/11/14)

- **SV-SPE-FR-004:** The system shall record the authorization architecture
  as informational state on the regime profile: MINEC authorizes
  establishment/administration/operation (ZF) and grants park/center
  benefits (LSI); MH — through DGA and DGII — holds fiscal surveillance and
  control; for LSI the PRIOR ONI capital registration (Ley de Inversiones)
  with its ≤5-*días hábiles* resolution is a precondition flag on the
  profile (días-hábiles arithmetic consumed from the fiscal-reporting
  calendar engine SV-FREP-FR-202..204 by id, never restated).
  (LB-003; LB-013; EVID-251/259)
- **SV-SPE-FR-005:** The system shall anchor the compliance surfaces of this
  wave on the DGA institutional frame as an informational note (no
  automation surface): the DGA is the superior national customs organ
  attached to MH; zonas francas, DPAs and parques de servicios form part of
  the *servicio aduanero*, and the DGA may establish on-site customs
  delegations in them — this frame grounds the DGA-facing registers of
  `07_obligations-reporting-sanctions.md` (consumed there by id).
  (LB-022; EVID-268)

### 3.4 Activity-admission config (12_ Arts. 3/6; 14_ Arts. 5/6/8)

- **SV-SPE-FR-006:** The system shall implement the ZF permitted-activity
  admission as config keyed by SAC scope: production/ensamble/maquila/
  manufacture/processing/transformation/commercialization of industrial
  goods in SAC Chapter 3 and Chapters 25 onward EXCEPT the Art. 6 negative
  list; plus romanos II-V (marine-species fishing for industrial
  transformation; greenhouse/laboratory flora cultivation; captive
  amphibian/reptile raising; ethyl-alcohol dehydration, each with the
  corresponding-authority permit flag); connected production services
  (design, painting, cutting, stamping, finishing, serigraphy, embroidery,
  washing, ironing, quality control, recycling, repair) admitted ONLY
  between beneficiaries of the law.
  (LB-005; EVID-252)
- **SV-SPE-FR-007:** The system shall implement the ZF Art. 6 exclusion
  config as a negative admission gate with two tiers: activity exclusions
  a)-k) (hydrocarbons/fuels; cement and clinker; ferrous and non-ferrous
  scrap; subsuelo minerals; explosives/radioactive; polluting goods; sugar
  and incorporations; alcohol and incorporations SALVO Art. 3 V; synthetic-
  fiber sacks; prepared-food supply; machinery import for leasing) and
  personal exclusions 1)-4) (suspended/revoked beneficiaries; societies
  with directors/representatives/partners of suspended/revoked societies;
  illicit-object activities; firm pending customs/tax obligations — with the
  voluntary-suspension carve-out for 1)-2)), each exclusion recorded as a
  dated config row with the 12_ print provenance.
  (LB-006; EVID-252)
- **SV-SPE-FR-008:** The system shall implement the LSI benefited-activity
  admission as letters a)-j) config, each letter carrying its statutory
  scope predicate as an admission/monitoring rule: a) distribución
  internacional and b) logística internacional without transforming the
  nature of the goods; d) tecnologías de información TO legal persons
  domiciled outside the national territory; i) médico-hospitalario TO
  patients permanently domiciled outside the Centroamérica area (general
  medicine and dental excluded); g) aeronáutico export-grade when provided
  to international-flight airlines regardless of domicile (Art. 8 inc. 2);
  letters a), b), d), e), h), i), j) further carry the local-market and
  retention surfaces owned by `03`/`05` (cited by id, not restated here).
  (LB-014; LB-016; EVID-260/261)
- **SV-SPE-FR-009:** The system shall implement the LSI placement rule
  (Art. 6) as admission validation — letters a), b), d), e), h), i), j) only
  in parques de servicios; f) ships and g) aircraft also in national-
  territory/port locations previously qualified as centros de servicios; c)
  call centers in parks or centers — and shall flag the co-located
  NON-benefited categories 1)-11) (hotels; airlines; energy; communications
  except call centers and no-network international-traffic terminators,
  which also lose the Arts. 21/25 benefits; banking/insurance except c)/j);
  transport; tourism/courier; professional/technical except h)/j); food
  supply; private security; leasing except administrator-to-usuario) as
  operating under ordinary national tax law: full tax routing, no regime
  benefits, inside the same park.
  (LB-015; LB-014 final inciso; EVID-260)

### 3.5 Qualification requisitos — dated config rows (12_ Arts. 17-A/19-A/19-B; 14_ Arts. 22/23)

- **SV-SPE-FR-010:** The system shall implement the ZF usuario
  qualification requisitos (Art. 17-A) as dated config rows resolved
  per-beneficiary (valid_from = acuerdo D.O. date; instrument = 12_ as
  printed) with at-least-one-of semantics: a) initial fixed-asset
  investment ≥US$500,000.00 attainable within the first two years of
  operations; b) ≥50 permanent jobs from the first year; c) ≥5 permanent
  jobs from the first year for comercializadores — measured values
  (investment bookings against the row; headcount from payroll records,
  payroll/05-06 by id) log against the row with the operations-year anchor.
  (LB-007; EVID-255)
- **SV-SPE-FR-011:** The system shall implement the ZF invernadero/
  laboratorio requisitos as dated config rows: ≥US$100,000 first-year
  fixed-asset investment AND ≥15 permanent jobs AND minimum area 5,000 m²
  (invernaderos) / 1,000 m² (laboratorios) AND formal administrative and
  financial structure (criterion flag), with the same breach split of
  FR-016 (a)-breach revocación; b)-d)-breach suspensión with tributes
  payable and benefit clock running).
  (LB-007; EVID-255)
- **SV-SPE-FR-012:** The system shall implement the DPA qualification
  requisitos as dated config rows: Art. 19-A at-least-one-of — a) initial
  fixed-asset investment ≥US$800,000 attainable within the first two years,
  with acquisition of EXISTING infrastructure excluded from the investment
  computation (exclusion rule on the row); b) ≥75 permanent jobs from the
  first year; c) ≥15 permanent jobs for comercializadores — and Art. 19-B
  all-of for amphibian/reptile DPAs (≥US$100,000 first-year investment, ≥15
  permanent jobs, formal structure; Art. 3 III flora activities follow the
  17-A requisito set).
  (LB-008; LB-009; EVID-255)
- **SV-SPE-FR-013:** The system shall implement the LSI distributor/
  logistics-operator requisitos (Art. 22) as dated config rows on the
  usuario-directo profile: a) ≥500 m² owned or leased (exception flag for
  the MINEC+MH lesser-area authorization); b) DGA registration with system
  access code; c) electronic inventory register + online system with
  warehouse entry/exit documents (register contract owned by
  `07_obligations-reporting-sanctions.md` by id); d) 5-year consolidated-
  manifest copies retention; e) bulto presentation/equipment duty; f)
  answer for declared-vs-arrived quantity/nature/value differences (carrier
  recourse); g) answer for usuario-indirecto clients' taxes on shortfalls,
  losses, misplacements and shrinkage (liability ledger owned by
  `03_lsi-regime.md` by id).
  (LB-018; EVID-262)
- **SV-SPE-FR-014:** The system shall implement the LSI BPO and
  médico-hospitalario requisitos (Art. 23) as dated config rows: BPO — new
  asset investment ≥US$150,000 in the first operations year (working
  capital + fixed assets) AND ≥10 permanent jobs AND a written contract of
  at least one year, with breach-year semantics: failure in any year
  removes the law's benefits FOR THAT FISCAL YEAR ONLY (per-ejercicio
  benefit-loss state, not revocation); médico-hospitalario — new fixed-asset
  investment ≥US$10,000,000.00 (surgical projects) or ≥US$3,000,000.00
  (non-surgical; print value "$3,000.000,00" [sic]), location OUTSIDE the
  San Salvador metropolitan area and departmental capitals, and surgical
  services only to patients holding national-or-foreign insurer coverage.
  (LB-019; EVID-262)

### 3.6 Breach state machine (12_ Arts. 17-A/19-A/39; 14_ Arts. 52/62)

- **SV-SPE-FR-015:** The system shall maintain a benefit-state field on the
  regime profile — *activa* (active) · *suspendida* (suspended) ·
  *revocada* (revoked) · inactivity category-loss — that drives the
  exemption-row resolution of `02_zf-exemption-schedules.md` and
  `03_lsi-regime.md` and the routing of `05_tan-iva-interface.md` (consumed
  by id): suspension makes tributes payable during the period; revocation
  and category loss end the benefit rows; every state change records its
  statutory reason and resolution reference.
  (LB-007; LB-020; LB-021; EVID-255/264)
- **SV-SPE-FR-016:** The system shall implement the ZF/DPA breach split
  with its two invariants: investment-requisito breach (literal a) ⇒
  REVOCACIÓN of the authorization acuerdo; jobs/comercializador requisito
  breach (b)/c), and 17-A greenhouse b)-d)) ⇒ SUSPENSIÓN until cured, with
  the tributes applicable to imports made and related taxes PAYABLE during
  the suspension, AND the suspension period NOT interrupting the total
  benefit term (the ladder clock keeps running — consumed by `02` by id);
  both branches ride the Art. 48 procedure (FR-019).
  (LB-007; LB-008; EVID-255)
- **SV-SPE-FR-017:** The system shall implement the LSI breach escalations
  as state transitions only (SMM-priced sanction VALUES live in
  `07_obligations-reporting-sanctions.md`, which consumes payroll/02 SMM
  rows by id — nothing SMM-priced is encoded here): third serious
  infringement ⇒ REVOCATORIA; very-serious ⇒ three-month suspension,
  recidivism ⇒ revocation (Art. 52); the transitions stamp the
  benefit-state field of FR-015.
  (LB-020; EVID-264)
- **SV-SPE-FR-018:** The system shall implement inactivity category/benefit
  loss as dated monitors: ZF — 12 continuous months of not operating the
  incentivated activity (imports/exports under the regime), with the
  5-*días hábiles* audiencia and 10-day final resolution, DGA tracking and
  system deregistration recorded (Art. 39); LSI — 3 continuous months of
  not operating ⇒ benefits revoked (force majeure/casus fortuitus
  exception), with the DGA computer-system access disablement recorded as a
  regime-state side effect (Art. 62).
  (LB-010; LB-021; EVID-258/264)

### 3.7 MINEC procedure clocks (12_ Arts. 45/48/49)

- **SV-SPE-FR-019:** The system shall expose the MINEC procedure surfaces
  as workflow states with their statutory clocks (días-hábiles arithmetic
  consumed from SV-FREP-FR-202..204 by id): usuario qualification
  resolution 25 *días hábiles* / DPA 35 *días hábiles* (MH opinion period
  included); same-zone amendment acuerdos (no activity change, SS-solvent,
  expansions/diminutions/relocation within the same zona franca, notarized
  note) within 10 *días hábiles*; infringement audiencia 5 *días hábiles*
  with final resolution in ten days (Art. 48); revocatoria recourse filed
  within 3 *días hábiles* of notification and resolved within 15 *días
  hábiles* (Art. 49).
  (LB-011; EVID-258)

### 3.8 Customs declarante-role config (74_ Arts. 9/5/5-A; 13_ Art. 36-A)

- **SV-SPE-FR-020:** The system shall carry a declarante-role config per
  importing/exporting persona jurídica with three modes: *agente aduanero*
  (external customs agent — credential requirements recorded at evidence
  depth: Estado-Party national, licenciatura in customs matters OR other
  degree + 2 years customs experience, possible psychometric exam);
  *apoderado especial aduanero* — self-declaration route, optional for
  personas jurídicas, granted by DGA authorization: public-deed power to an
  employee, sufficiency examination on customs matters (possibly including
  psychometric tests), and the poderdante's fianza (amount fixed by the DGA
  — config-gap, no shipped default), the apoderado standing under the same
  suspension/revocation rules as agentes; and ordinary agency. Once the
  fianza is posted, the apoderado especial transmits the company's own
  declarations (transmission surface owned by `06_customs-declarations.md`
  by id).
  (LB-024; LB-023; EVID-269/268)
- **SV-SPE-FR-021:** The system shall record pre-declaration *consultas*
  and advance rulings as reference records with their statutory clocks and
  effects: consultas answered within 15 *días hábiles* extendable ex officio
  by an equal period, effective only for the specific case consulted, and
  NEVER suspending customs/tax obligations; advance criteria/resolutions
  accepted only before the importation of the goods concerned, valid for
  three years unless the underlying conditions change (validity window
  stamped on the record).
  (LB-025; EVID-269)

### 3.9 Área metropolitana — stale-static dated list (12_ Art. 2 d)

- **SV-SPE-FR-022:** The system shall implement the *área metropolitana* as
  a STALE-STATIC dated list of the 13 municipios as printed (Antiguo
  Cuscatlán, Santa Tecla, Apopa, Ayutuxtepeque, Cuscatancingo, Ciudad
  Delgado, Ilopango, Mejicanos, Nejapa, San Marcos San Martín [sic],
  Tonacatepeque, San Salvador, Soyapango) — one dated row set with the 12_
  print provenance, NO recompute against the 2023 municipal reorganization
  (SOQ-43) — and shall derive the location track of FR-003 (metro vs fuera)
  from it, feeding the shorter/longer exemption tracks of
  `02_zf-exemption-schedules.md` by id.
  (LB-002; EVID-251)

## 4. Data Model

Layer semantics: the regime framework is Odoo-native (res.company profile +
config rows) — all entities live in the client (wave default `odoo`; see
§5). MINEC/DGA/ONI are external authorities: the model records
authority-issued facts (acuerdos, resolutions, registrations), it does not
emulate them. No printed data table in this file warrants a CSV sidecar
(the 13-municipio list and the requisito values are small config sets;
default none per plan).

**Regime profile (on res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_spe_regime | select | zona_franca · dpa · parque_servicios · centro_servicios · none | FR-001, FR-002 |
| res.company | sv_spe_role | select | zf: desarrollista · administrador · usuario · titular_dpa; lsi: desarrollista · administrador · usuario_directo · centro_servicios | FR-003 |
| res.company | sv_spe_activity_admission | m2o config | ZF SAC-scope/negative-list row set (FR-006/007); LSI letter + predicate (FR-008/009) | FR-006..009 |
| res.company | sv_spe_location_track | select (computed) | metro · fuera — derived from the FR-022 municipio list (ZF family) | FR-003, FR-022 |
| res.company | sv_spe_acuerdo_do_date | date | MINEC acuerdo D.O. publication date = D15 row key member | FR-003 |
| res.company | sv_spe_benefit_state | select | activa · suspendida · revocada · perdida_inactividad | FR-015 |
| res.company | sv_spe_state_reason | select + char | art17a_a_investment · art17a_bc_jobs · art52_third_grave · art52_muy_grave · art39_inactivity_12m · art62_inactivity_3m · … (resolution ref) | FR-015..018 |
| res.company | sv_spe_oni_registration | char + date + boolean | ONI capital-registration resolution + ≤5-días-hábiles clock result (LSI precondition) | FR-004 |
| res.company | sv_spe_dga_access_enabled | boolean | DGA system-access state; set false on Art. 62 cancellation / Art. 39 baja | FR-018 |

**Activity-admission config (l10n_sv_special_regime.activity):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.activity | regime_scope | select | zf_sac_chapter (Ch. 3 + Ch. 25+, minus Art. 6) · zf_romano (II pesca · III invernadero · IV anfibios · V alcohol) · zf_connected_service (beneficiaries-only) · lsi_letter a)..j) · lsi_non_benefited 1)..11) | FR-006..009 |
| l10n_sv_special_regime.activity | scope_predicate | char/config | per-letter rule (d TI: foreign-domiciled PJ; i médical: non-Centroamérica patients; g aeronáutico: international airlines regardless of domicile) | FR-008 |
| l10n_sv_special_regime.activity | exclusion_tier | select | none · activity_art6_a_k · personal_art6_1_4 (voluntary-suspension carve-out flag) | FR-007, FR-009 |
| l10n_sv_special_regime.activity | valid_from · valid_to · provenance | date · date · char | instrument = 12_/14_ article as printed (SOQ-30); dated rows per D15 | FR-006..009 |

**Qualification-requisito rows (l10n_sv_special_regime.requisito):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.requisito | profile · kind | m2o · select | zf_usuario_17a · zf_invernadero_17a · dpa_19a · dpa_19b · lsi_distribuidor_22 · lsi_bpo_23 · lsi_medico_23 | FR-010..014 |
| l10n_sv_special_regime.requisito | threshold_type | select | investment_usd · permanent_jobs · area_m2 · contract_min_years · structure_flag · registration_flag | FR-010..014 |
| l10n_sv_special_regime.requisito | threshold_value · horizon | monetary/int · char | US$500,000/2y · 50 jobs/1y · 5 jobs (comercializadores) · US$100,000+15+5,000/1,000 m² · US$800,000/2y (existing-infrastructure exclusion) · 75/15 jobs · US$100,000+15 (19-B) · 500 m² · US$150,000/1y+10 jobs+1-y contract · US$10,000,000 quirúrgico / US$3,000,000 no-quirúrgico — as printed | FR-010..014 |
| l10n_sv_special_regime.requisito | logic · breach_effect | select | at_least_one · all_of ; revocacion · suspension_tributes_payable_clock_runs · ejercicio_benefit_loss | FR-010..016 |
| l10n_sv_special_regime.requisito | valid_from · valid_to · provenance | date · date · char | valid_from = beneficiary acuerdo D.O. date; instrument = law article as printed | FR-010..014 |
| l10n_sv_special_regime.requisito.log | measured_value · period | monetary/int · date/char | investment bookings and headcount (payroll/05-06 feed by id) logged per operations year against the row | FR-010, FR-014 |

**Área-metropolitana list (l10n_sv_special_regime.municipio):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_special_regime.municipio | name · ismetro | char · boolean (true) | the 13 municipios as printed (San Marcos San Martín [sic]) | FR-022 |
| l10n_sv_special_regime.municipio | valid_from · valid_to · provenance | date · date · char | stale-static 12_ print rows; NO 2023-reorganization recompute (SOQ-43) | FR-022 |

**Declarante-role config + rulings (res.company / l10n_sv_special_regime.ruling):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_spe_declarante_mode | select | agente_aduanero · apoderado_especial · ordinary_agency | FR-020 |
| res.company/res.partner (employee) | sv_spe_apoderado_data | fields | escritura pública ref · sufficiency-exam date/result (psychometric flag) · DACG requirements pending flag (OQ-004) | FR-020 |
| res.company | sv_spe_fianza_ref · sv_spe_fianza_amount | char · monetary slot | DGA-fixed fianza — config-gap, NO shipped default (OQ-004) | FR-020 |
| l10n_sv_special_regime.ruling | kind | select | consulta · advance_ruling | FR-021 |
| l10n_sv_special_regime.ruling | filed_on · due_on · answered_on · valid_until | date | consulta: 15 días hábiles + equal ex-officio extension, case-specific; advance ruling: pre-import only, 3-year validity window | FR-021 |

## 5. Odoo Mapping

Layer semantics for this wave: the regime framework is Odoo-native
(res.company profile + dated config rows) — every FR maps `odoo`; no SaaS
rows are introduced because none of these FRs touch DTE
generation/transmission (the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2); the teledespacho
transmission surface is `06_customs-declarations.md`'s. Model names are
stable across Odoo 17/18/19/20; no version-specific behavior is required by
this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | res.company + l10n_sv_special_regime.* | sv_spe_regime | ZF vs DPA distinct discriminators; feeds 02/04/05 by id |
| FR-002 | odoo | res.company | sv_spe_regime (parque/centro) + role defs | LSI custody roles ground 03's usuario-indirecto ledger |
| FR-003 | odoo | res.company | sv_spe_role, sv_spe_activity_admission, sv_spe_location_track, sv_spe_acuerdo_do_date | THE D15 row key; anchor = acuerdo D.O. date; snapshot-on-write per D15/D16 |
| FR-004 | odoo | res.company | sv_spe_oni_registration | ONI ≤5-días-hábiles clock via SV-FREP-FR-202..204 by id; MINEC/MH split informational |
| FR-005 | odoo | (informational) | — | 13_ frame note anchoring 07's DGA-facing registers; no automation surface |
| FR-006 | odoo | l10n_sv_special_regime.activity | regime_scope zf_* | SAC scope = product-catalog config; connected services beneficiaries-only gate |
| FR-007 | odoo | l10n_sv_special_regime.activity | exclusion_tier | Art. 6 a)-k)/1)-4) dated rows, 12_ print provenance; voluntary-suspension carve-out |
| FR-008 | odoo | l10n_sv_special_regime.activity | scope_predicate | per-letter predicates (d/i/g); local-market/retention surfaces owned by 03/05 by id |
| FR-009 | odoo | l10n_sv_special_regime.activity | regime_scope lsi_* | placement validation + co-located 1)-11) full-tax-routing flag |
| FR-010 | odoo | l10n_sv_special_regime.requisito(+.log) | kind zf_usuario_17a | US$500,000/2y · 50 · 5 jobs rows; valid_from = acuerdo D.O. date; headcount feed payroll/05-06 by id |
| FR-011 | odoo | l10n_sv_special_regime.requisito | kind zf_invernadero_17a | US$100,000 + 15 jobs + 5,000/1,000 m² + structure flag; breach split per FR-016 |
| FR-012 | odoo | l10n_sv_special_regime.requisito | kinds dpa_19a/19b | US$800,000 (existing-infrastructure exclusion rule) · 75 · 15; 19-B US$100,000/15; as printed |
| FR-013 | odoo | l10n_sv_special_regime.requisito | kind lsi_distribuidor_22 | 500 m² + DGA registration + register/manifest duties; ledgers owned by 03/07 by id |
| FR-014 | odoo | l10n_sv_special_regime.requisito | kinds lsi_bpo_23/lsi_medico_23 | US$150,000+10 jobs+1-y contract (breach year ⇒ ejercicio benefit loss); $10M/$3M [sic print] médico rows |
| FR-015 | odoo | res.company | sv_spe_benefit_state, sv_spe_state_reason | drives 02/03 exemption-row resolution + 05 routing by id; D16: imported regime history keeps prior states |
| FR-016 | odoo | res.company | benefit-state transitions | suspensión: tributes payable + ladder clock keeps running (consumed by 02); Art. 48 procedure link FR-019 |
| FR-017 | odoo | res.company | benefit-state transitions (LSI) | state transitions only; SMM-priced sanction values = 07's surface (payroll/02 by id) — nothing SMM here |
| FR-018 | odoo | res.company | inactivity monitors + sv_spe_dga_access_enabled | 12m ZF / 3m LSI dated monitors; DGA access disablement recorded as side effect |
| FR-019 | odoo | l10n_sv_special_regime.procedure (workflow states) | clocks 25/35/10/5/10-day/3/15 días hábiles | días-hábiles arithmetic via SV-FREP-FR-202..204 by id; Art. 48 resolution term printed as "DIEZ DÍAS" (calendar, as printed) |
| FR-020 | odoo | res.company/res.partner | sv_spe_declarante_mode, sv_spe_apoderado_data, fianza slots | fianza amount + exam/DACG detail = config-gaps (OQ-004); transmission surface = 06 by id |
| FR-021 | odoo | l10n_sv_special_regime.ruling | kind/filed_on/due_on/valid_until | consulta 15+15 días hábiles case-specific, no suspension; advance ruling 3-y validity stamped |
| FR-022 | odoo | l10n_sv_special_regime.municipio | name/valid_from/provenance | stale-static 13-municipio rows (SOQ-43 — no 2023 recompute); metro/fuera track feeds 02 by id |

Version-regime notes (D12/D15/D16/D18/D19): all statutory values in this
file (US$500,000/US$800,000/US$100,000/US$150,000/US$10,000,000/
US$3,000,000 [sic print], 50/75/15/10/5 jobs, 5,000/1,000/500 m², the
13-municipio list, the 25/35/10/5/3/15-day procedure clocks) are code-text
values cited as printed under the SOQ-30 verification watch (§2) and live
as dated config rows with instrument provenance — never constants; the
per-beneficiary anchor is the acuerdo D.O. date (FR-003). Mid-year go-live
(D18): a migrating regime company's requisito logs, benefit states and
ladder computations ingest as `is_historical` rows with original-period
semantics (tiered ingestion per D18; no re-derivation). No hard gates
beyond the statutory state machine (D16 no-override: regime validity is
never overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given an applicant qualified as ZF usuario under the Art. 17-A
  a) requisito (US$500,000 attainable in the first two years), when its
  fixed-asset investment bookings are recorded, then each booking logs
  against the beneficiary's dated requisito row (kind zf_usuario_17a,
  threshold_type investment_usd, valid_from = acuerdo D.O. date) with the
  operations-year anchor (FR-010).
- **AC-002:** Given a ZF usuario whose jobs requisito (50 permanent posts)
  is breached in year 3, when the breach determination is recorded, then
  the benefit state becomes suspendida with reason art17a_bc_jobs, the
  system marks import tributes and related taxes payable during the
  suspension, and the benefit-term computation continues accumulating
  (suspension does not interrupt the total benefit term) (FR-015, FR-016).
- **AC-003:** Given an LSI BPO usuario that fails to reach the US$150,000
  first-year investment in its second operations year, when the ejercicio
  closes, then the benefits for that fiscal year only are flagged lost
  (ejercicio_benefit_loss) with no revocation and no effect on other
  years' rows (FR-014).
- **AC-004:** Given a persona jurídica whose employee is authorized as
  apoderado especial aduanero (escritura pública + sufficiency exam
  recorded), when the poderdante's fianza is posted (DGA-fixed amount
  config slot), then the declarante mode apoderado_especial is active and
  the company's own customs declarations carry that declarante identity
  (transmission mechanics owned by `06` by id) (FR-020).
- **AC-005:** Given a ZF applicant located in Antiguo Cuscatlán, when its
  profile is saved, then its location track resolves to metro via the
  stale-static 13-municipio dated rows (no 2023-reorganization recompute),
  and the metro track is handed to `02`'s exemption-track resolution by id
  (FR-022, FR-003).
- **AC-006:** Given an LSI beneficiary with two recorded serious
  infringements, when a third serious infringement is recorded, then the
  benefit state becomes revocada per Art. 52 (third-grave rule) — with NO
  SMM-priced fine computed in this file (sanction values live in `07`)
  (FR-017).
- **AC-007:** Given a ZF beneficiary with 12 continuous months without
  regime operations (imports/exports), when the inactivity monitor fires,
  then the category-loss procedure opens with the 5-días-hábiles audiencia
  window (calendar engine by id) and, on final resolution, the state
  perdida_inactividad is stamped with the DGA deregistration recorded
  (FR-018, FR-019).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-30 carried: every regime consolidation ends 2012-2013 (12_ → D.L. 318-2013; 13_ → D.L. 121-2012; 74_ → D.L. 23-2012; 14_ → 2007 print "Reformas: S/R"); post-cutoff reforms unverified until official routes recover. All LBs in this file cite as printed; any post-2013 reform (e.g. D.L. 598-2020-era traffic) may move requisito values, the municipio list or procedure clocks — re-verify before implementation. | no | Takumi S7 (sources watch) | open |
| OQ-2 | SOQ-43 carried: the Art. 2 d) área-metropolitana 13-municipio list predates the 2023 municipal reorganization (CAT-013 kin); legal effect on membership unstated. FR-022 ships the list as stale-static dated rows with NO recompute; a future reform replacing the list lands as new dated rows. | no | Takumi S7 (config watch) | open |
| OQ-3 | SOQ-31 carried: the Reglamento General de la Ley de Zonas Francas (mandated by 12_ Art. 51) is NOT in the corpus — solicitud/informe formats and DACG structures are delegated there. FR-019 exposes the procedure clocks as printed; the format-level details ship as config slots with NO defaults. Acquisition candidate ≥75. | no | Takumi S7 (sources watch) | open |
| OQ-4 | 74_ declarante exam mechanics: the statute (Art. 9) delegates the sufficiency-exam requirements and the fianza amount to DGA disposiciones administrativas de carácter general (not in corpus, 13_ Art. 36-A similar); FR-020 records escritura/exam/fianza at evidence depth with the exam content and fianza value as config-gaps — no invented procedural detail. | no | Takumi S7 (sources watch) | open |
