# GT — Commercial-legal — RM surfaces: arancel fee catalog + the electronic edicto portal

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | commercial-legal |
| Status  | draft |
| Authors | GT synthesis wave S-GT5 |
| Updated | 2026-08-21 |

## 1. Purpose

This file is the THIRD of the S-GT5 chart-of-accounts/commercial-legal wave
and CREATES the commercial-legal topic directory: it owns cluster C3, the
*Registro Mercantil* (RM, Mercantile Registry) outward surfaces. It converts
into requirements: the RM fee catalog of the *arancel* (fee schedule) source
**73_** as dated-2022-label data with a re-verify flag on every row (R66 —
the print carries NO date or instrument number and its own "Ajuste por
vigencia de nuevo Arancel" rows presuppose wholesale supersession cycles);
the society-lifecycle *trámite* (procedure) fee rows and the NEGATIVE rows
(the *matrícula*/renovación fees are absent; the variable inscripción scale
is not printed); the edicto/publication fee classes ("Pago de edicto" Q30
plus per-event *publicaciones* Q200/Q100/Q25); the electronic publication
channel created by **D-18-2017 art. 12**, which reformed CC art. 343
("Mecanismo de publicación oficial", official publication mechanism) so ANY
*Código de Comercio*-mandated publication goes through the RM electronic
medium and displaces print (R64: the 66_ print's arts. 341/343 texts
pre-date the reform); the edicto content templates observable in the single
**83_** portal edition (edición 6022, Wednesday 19-Aug-2026: inscripción
grammar + field inventory, modificación kinds, disolución + liquidador
registration in Auxiliares de Comercio, the empresa-mercantil layer, balance
publication families, convocatoria STUBS whose content is never asserted);
the RM data model and the provisional → edicto → definitiva procedure of CC
arts. 333/335-343 as printed (pre-D18-2017 texts flagged per R64); the
MinEconomía instrument split (arancel/reglamento — no fees in the Code); and
the execution of the art. 380 balance-publication duty owned by
`../chart-of-accounts/01_books-anchor.md` GT-COA-FR-021 (consumed by exact
id).

It does **not** cover: the C1 books/PCGA anchor, entry invariants,
conservation and instrument identity
(`../chart-of-accounts/01_books-anchor.md`, GT-COA-FR-001..033); the
dual-track book-legalization model and the books-authorization fee row
(`../chart-of-accounts/02_dual-track-habilitacion.md`, GT-COA-FR-034..060 —
its Q0.20/hoja row GT-COA-FR-041 is cited as kin, never re-derived); the
comerciante/sociedades lifecycle itself — society types, capital, governance,
matrícula thresholds, liquidation waterfall (C4, the sociedades-lifecycle
file, unwritten — forward ref, file + cluster only: the lifecycle events are
the CONTENT this channel publishes, and that file consumes these FRs by id);
títulos valores and the prescription ladder (C5,
`03_titulos-valores-prescripcion.md` — forward ref, file + cluster only);
the AML chain (C6, unwritten — forward ref, cluster only); the consolidated
retention/destruction matrix (`../chart-of-accounts/03_retention-destruction-matrix.md`,
the GOQ-124 deliverable, Task 7 — forward ref, file + cluster only); and
tax-side sanction machinery (GT-TAX-FR-214/216/217 consumed by exact id —
this file owns only the RM-side cancellation surface).

## 2. Legal Basis

Authority order (binding, per master index preamble): CCom article text =
**66_** — *Código de Comercio, Decreto del Congreso 2-70* — as consolidated
inline through **Decreto 11-2006 (DCA 30-05-2006)**; the print carries NO
post-May-2006 reforms, so **every 66_-sourced row in this file carries the
GOQ-123 live-regime verification note** (kin — owned by
`01_books-anchor.md` GT-COA-FR-031), load-bearing here through **R64**: the
66_ print's arts. 341/343 still route publications to the Diario Oficial,
while **D-18-2017 art. 12 moved all CC publications to the RM electronic
portal** — current art. 343 mechanics are taken from the reform text as
printed by 83_ (EVID-598), and every 66_ procedural text below is cited
"as printed, pre-D18-2017". Instrument dated identity (vigencia 1971-01-01,
R45; D-2946 appendix guard, R65) is owned by `01_books-anchor.md`
GT-COA-FR-030..032 and consumed by id, never re-derived. **73_** = the RM
"ARANCEL" fee schedule — 1 page, ~46 numbered items, heavy OCR damage
(Q/O glyph confusion, mangled numerals — all rows quoted exactly as printed
from the committed evidence file, restorations bracketed); it **prints NO
date or instrument number** (the "2022" ascription is label-derived; OQ
discipline: R66) and its transition rows presuppose arancel supersession
cycles → every fee row is dated-2022-label + re-verify flag, no valid_to
asserted. **83_** = ONE daily edition of the RM electronic edicts portal
(edición 6022, MIÉRCOLES 19 DE AGOSTO DE 2026, Ministerio de Economía, 47
pp.) — a single-as-of snapshot (2026-08-19): it evidences CHANNEL SHAPE
only (sections, grammar, field inventories); publication cadence, lag and
volume norms are unknowable from one edition, and the convocatoria entries
are text-layer STUBS whose content is never asserted (GOQ-131). Quotation
sources: the committed evidence files `gt/.extractions/60_73_83_RM.evidence.md`
(EV05c; EVID-594..604) and `gt/.extractions/66_CCom_sociedades_comercial.evidence.md`
(EV05b; EVID-539/540/541), verified against the scan text layers
`gt/.extractions/73_RegistroMercantil_Aranceles_2022.pdf.txt`,
`gt/.extractions/83_RM_edictos_2026-08-19.pdf.txt` and
`gt/.extractions/66_Codigo_Comercio_D2-70.pdf.txt`.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 73_ (RM Arancel) identity + supersession rows: "ARANCEL / Registro / MERCANTIL" / "Ajuste por vigencia de nuevo Arancel 3/ Variable" / "Ajuste por CERTIFICACIONES según nuevo Arancel 38 Q 20.00" / footer: "O /a.Ave. 7-61, zona 4, Guatemala, C.A. www.registromercantil.gob.gt" / "(O consultasQregistromercantil.gob.gt a (502) 2317-3434" [all sic] | Fee schedule of the Registro Mercantil, one page, ~46 numbered trámite items. The document prints NO date or instrument number — the "2022" as-of is label-derived; rows 37-38 are transition items ("adjustment on entry into force of a new arancel"), evidencing that RM aranceles are replaced wholesale — this snapshot is likely superseded (re-verify, R66). Footer OCR-damaged | `gt/sources/73_RegistroMercantil_Aranceles_2022.pdf` | p.1 title block, rows 37-38, footer (EVID-594) |
| LB-002 | 73_ society-lifecycle trámite fee rows (as printed, numerals OCR-damaged): "Actas de Asambleas extraordinarias Q 150.00" / "Ampliación de capital * + arancel variable : Q 500.00" / "Cambio de direccion sociedad 5 Q 150.00" / "Cancelación de Empresa 9 Q 150.00" / "Inscripción de Comerciante 13 Q 100.00" / "Disolución de Sociedad (Provisional) 16 Q 300.00" / "Emisión de Acciones y titulos que generen obligaciones |7 Q 200.00" / "Inscripción de Empresas 18 Q 100.00" / "Inscripción de Sociedades * + arancel variable 2 | Variable" / "Modificacion de Escritura de Sociedad 23 O 300.00" [sic O=Q] / "Sociedad Extranjera * + arancel variable 26 Q 1500.00" / "Traspaso de Empresa 2/ Q 150.00" / "Nombramiento de Liquidador 3 | Q 150.00" / "Auxiliares de comercio 3 OQ 150.00" / "Cancelación de Auxiliares / OQ 150.00" [sic] / "Despacho Judicial Empresa 14 Q 150.00" / "Despacho Judicial Sociedad 15 Q 150.00" / "Inscripción de Mandatos 19 Q 150.00" / "Inscripción de Prendas 20 Q 150.00" / "Reposición de patente de empresa 24 Q 150.00" / "Reposición de patente de sociedad 25 Q 150.00" | Society-lifecycle fee map (2022-label snapshot): extraordinary-assembly minutes Q150; capital ampliation Q500 + variable; sociedad address change Q150; empresa cancellation Q150; comerciante/empresa inscripción Q100 each; (provisional) dissolution Q300; share/bond emissions Q200; sociedad inscripción = Variable + arancel variable; sociedad-deed modification Q300; foreign society Q1,500 + variable; empresa transfer (traspaso) Q150; liquidator appointment Q150; auxiliares de comercio (registration/cancellation) Q150; judicial dispatches Q150; mandates/prendas inscripción Q150; patente reissue (empresa/sociedad) Q150 each. NEGATIVE: the matrícula (patente) fee itself and renovación are NOT rows on this page (only reposición) — R66 | `gt/sources/73_RegistroMercantil_Aranceles_2022.pdf` | p.1, rows as numbered in the schedule (EVID-595) |
| LB-003 | 73_ books + edicto/publicación fee rows (as printed): "Autorización de Libros Pago Variable 29 Q 0.20 x Hoja" / "Certificaciones 30 O 50.00" [sic Q] / "Pago de edicto 33 Q 30.00" / "Multas 34 Q 25.00" / "Reingreso de documentos rechazados 28 Q 25.00" / "Publicacion Sociedades Nuevas 4 | Q 200.00" / "Publicacion Modificaciones (Transformación, fusión, disoluciones 472 Q 200.00 de sociedades Mercantiles, aumento o disminución de capital)" [sic 472 — likely 42] / "Publicación Otras Modificaciones (Cambios de dirección, objeto etc.) 43 O 100.00" [sic Q] / "Publicación Clausura o traspaso de Empresa 44 Q 100.00" / "Publicación de otros motivos 45 Q 100.00" / "Publicacion Fe de erratas 46 O 25.00" [sic Q] / "Consultas en linea (e-consultas) 35 Variable" | Books authorization Q0.20 per hoja (sheet) + variable payment; certifications Q50; edicto processing charge Q30; fines Q25; re-entry of rejected documents Q25. Publication classes: new sociedades Q200; major modifications (transformación, fusión, dissolutions, capital increase/decrease) Q200; other modifications (address, object) Q100; empresa closure or transfer Q100; other motives Q100; fe de erratas (errata notices) Q25; online consultations = Variable | `gt/sources/73_RegistroMercantil_Aranceles_2022.pdf` | p.1, rows 28-46 region (EVID-596) |
| LB-004 | 83_ masthead + section index: "MIÉRCOLES, 19 DE AGOSTO DE 2026 EDICIÓN: 6022 REGISTROMERCANTIL.GOB.GT / MINISTERIO DE ECONOMÍA / EN ESTA EDICIÓN ECONTRARÁ: [sic ENCONTRARÁ] / Inscripción de Sociedades - pag.1 / Modificación de Sociedades - pag.27 / Disolucion / Cancelacion de So-ciedades - pag.29 / Edictos Varios - pag.30 / Convocatoria - pag.46 / Balance - pag.47" | One daily edition of the RM electronic-edicts portal: edición no. 6022, Wednesday 19-Aug-2026, published at registromercantil.gob.gt under the Ministry of Economy; 47 pages; SIX fixed sections in fixed order (inscripción → modificación → disolución/cancelación → edictos varios → convocatoria → balance). Single as-of snapshot 2026-08-19; one edition shows weekday publication only — cadence/volume norms need more editions (GOQ-131) | `gt/sources/83_RM_edictos_2026-08-19.pdf` | p.1 masthead + index (EVID-597) |
| LB-005 | 83_ charter text: "Este portal de publicación electrónica nace a partir de las reformas realizadas al código de comercio de Guatemala a través del decreto 18-2017 en su artículo 12, como se detalla a continuación: / Artículo 12. Se reforma el artículo 343 del Código de Comercio de Guatemala, Decreto Número 2-70 del Congreso de la República, el cual queda así: / "Artículo 343. Mecanismo de publicación oficial. Cualquier publicación que el presente Código indique que debe realizarse en el Diario Oficial, deberá realizarse a través de un medio de comunicación electrónico del Registro Mercantil. Cuando la publicación se realice a través de un medio de comunicación electrónica del Registro Mercantil, no será necesario realizar ninguna publicación en medios escritos."" | This electronic-publication portal was born from the reforms to Guatemala's Commercial Code made by decree 18-2017 article 12, as detailed: Art. 12 reforms CC art. 343 (D-2-70), which reads: "Article 343. Official publication mechanism. Any publication that this Code indicates must be made in the Diario Oficial shall be made through an electronic communication medium of the Registro Mercantil. When the publication is made through an electronic medium of the Registro Mercantil, no publication in written media is necessary." — the channel's charter: RM-portal publication DISPLACES all print (R64: current art. 343 mechanics; text as printed by the portal) | `gt/sources/83_RM_edictos_2026-08-19.pdf` | p.1, below index (EVID-598) |
| LB-006 | 83_ inscripción-edicto exemplar (first entry of the edition; uniform grammar across the 121 openers): "EL REGISTRO MERCANTIL, CON BASE AL TESTIMONIO DE LA ESCRITURA NO. 18, AUTORIZADA EN LA CIUDAD DE GUATEMALA EL 1 DE JULIO DE 2026 POR EL NOTARIO EVEL YN JOHANA GARCÍA PERDOMO, PRESENTADO A ESTE REGISTRO EL 9 DE JULIO DE 2026 A LAS 19:5 HORAS [sic], INSCRIBE BAJO REGISTRO: 49653, FOLIO: 314, LIBRO ELECTRONICO: 29 DE SOCIEDADES MERCANTILES, EXPEDIENTE NO. 91434-2026 LA SOCIEDAD DENOMINADA CAPITAL VERDE SAGRADO, SOCIEDAD ANÓNIMA, DE NOMBRE COMERCIAL AGUA SAGRADA GROUP , DOMICILIO: DEPARTAMENTO DE GUATEMALA, SEDE: CARRETERA AL SALVADOR KILOMETRO 16.5 LOTE 4, COLONIA SAN MIGUEL, ZONA 0 OBJETO: A) OPERACIÓN, ADMINISTRACIÓN Y FUNCIONAMIENTO DE RESTAURANTES…; Y OTROS QUE CONSTAN EN LA ESCRITURA SOCIAL. PLAZO: INDEFINIDO; CAPITAL SOCIAL AUTORIZADO: Q.499999.00, SUSCRITO: Q.2000.00, PAGADO: Q.2000.00, DIVIDIDO EN: 499999 ACCIONES DE Q.1 CADA UNA. ÓRGANO DE ADMINISTRACIÓN: ADMINISTRADOR ÚNICO, CONSEJO DE ADMINISTRACIÓN; REPRESENTACIÓN LEGAL: ADMINISTRADOR ÚNICO, MIEMBRO(S) DEL CONSEJO DE ADMINISTRACIÓN, GERENTE; ÓRGANO DE VIGILANCIA: ACCIONISTA, AUDITOR, CONTADOR. GUATEMALA 30 DE JULIO DE 2026. ULTIMA LINEA." | The Registro Mercantil, on the testimony of escritura no. 18 authorized in Guatemala City on 1-July-2026 by notary …, presented on 9-July-2026 at 19:5 [sic] hours, inscribes under registro 49653, folio 314, ELECTRONIC BOOK 29 OF SOCIEDADES MERCANTILES, expediente 91434-2026 the society CAPITAL VERDE SAGRADO, S.A., trade name AGUA SAGRADA GROUP, domicile …, object … "AND OTHERS CONTAINED IN THE SOCIAL DEED", term: indefinite; authorized capital Q499,999.00, subscribed Q2,000.00, paid Q2,000.00, divided into 499,999 shares of Q1 each; administration/legal-representation/surveillance organs; Guatemala date; "LAST LINE." terminator — the standard inscripción-notice grammar: escritura → presentation → registro/folio/libro/expediente → identity → objeto → plazo → capital → órganos → date → terminator | `gt/sources/83_RM_edictos_2026-08-19.pdf` | pp.1-2, first entry; pattern count = 121 openers file-wide (EVID-599) |
| LB-007 | 83_ capital-cluster pattern (representative + counterexamples): "CAPITAL SOCIAL AUTORIZADO: Q.499999.00, SUSCRITO: Q.2000.00, PAGADO: Q.2000.00, DIVIDIDO EN: 499999 ACCIONES DE Q.1 CADA UNA." (Capital Verde Sagrado) / "CAPITAL SOCIAL AUTORIZADO: Q.499900.00, SUSCRITO: Q.200.00, PAGADO: Q.200.00, DIVIDIDO EN: 4999 ACCIONES DE Q.100 CADA UNA." (Avalanche Creek) / counterexamples: "CAPITAL SOCIAL AUTORIZADO: Q.5000.00, SUSCRITO: Q.5000.00, PAGADO: Q.5000.00, DIVIDIDO EN: 50 ACCIONES DE Q.100 CADA UNA." (Corporación Systec) / "CAPITAL SOCIAL AUTORIZADO: Q.20000000.00, SUSCRITO: Q.1500.00, PAGADO: Q.1500.00, DIVIDIDO EN: 20000000 ACCIONES DE Q.1 CADA UNA." (Transportes 24) | Dominant market pattern in this edition: authorize Q499,000-Q499,999 (just under Q500,000) while subscribing/paying only Q200-Q5,000 — 6+ of the ~27 sampled entries; NOT universal (Q5,000 and Q20,000,000 authorizations also appear). The Q500,000 boundary suggests a threshold in the "arancel variable" inscripción-fee scale (73_ prints the scale as "Variable" without brackets) — observed behavior; threshold inference flagged, NOT evidenced by either document (R66: inference only) | `gt/sources/83_RM_edictos_2026-08-19.pdf` | pp.1-7, capital clauses of inscripción entries (EVID-600) |
| LB-008 | 83_ modificación notices (kinds + electronic variant): capital increase: "…INSCRIBE LA MODIFICACIÓN NO. 1, DE AUMENTO DE CAPITAL, DE LA ENTIDAD: DISTRIBUIDORA LA PROVIDENCIA DEL 6-39, SOCIEDAD ANÓNIMA, INSCRITA CON REGISTRO NO. 131113 FOLIO 825 LIBRO 224 DE SOCIEDADES MERCANTILES… SE ACORDÓ AUMENTAR EL CAPITAL AUTORIZADO, SE MODIFICA LA CLÁUSULA SÉPTIMA, QUEDANDO DE LA SIGUIENTE MANERA: SÉPTIMA: CAPITAL SOCIAL AUTORIZADO: SE AUMENTA EL CAPITAL AUTORIZADO EN LA CANTIDAD ADICIONAL DE Q. 99,705,000.00 CON DICHO AUMENTO EL CAPITAL ASCIENDE A LA CANTIDAD DE Q. 100,000,000.00 REPRESENTADO Y DIVIDIDO POR 100,000,000 ACCIONES CON UN VALOR NOMINAL DE Q. 1.00 CADA UNA." / domicilio: "INSCRIBE LA MODIFICACIÓN #1 DE CAMBIO DE DOMICILIO DE LA ENTIDAD: DOMATERRA, SOCIEDAD ANONIMA INSCRITA CON REGISTRO 43234 FOLIO 411 LIBRO 28 DE SOCIEDADES MERCANTILES…" / denominación: "…CAMBIO DE DENOMINACIÓN SOCIAL Y NOMBRE COMERCIAL DE LA ENTIDAD: PREMAL HOLDINGS LA PATRIMONIAL… LA DENOMINACIÓN DE LA SOCIEDAD ES PREMAL HOLDINGS, SOCIEDAD ANÓNIMA QUE PODRÁ ABRVIARSE [as printed: PODRÁ ABRIVIARSE reads PODRÁ ABRVIARSE — see evidence] PREMAL HOLDINGS, S. A." / valor nominal: "INSCRIBE LA MODIFICACIÓN NO. 2, DE CAMBIO DEL VALOR NOMINAL DE ACCIONES… SE ACORDÓ MODIFICAR ERROR COMETIDO RELACIONADO AL VALOR NOMINAL DE LAS ACCIONES" / electronic tag: "SE INSCRIBE LA MODIFICACIÓN ELECTRÓNICA #2 DE AUMENTO DE CAPITAL DE LA ENTIDAD: ALMAVE, SOCIEDAD ANÓNIMA INSCRITA CON REGISTRO 169309 FOLIO 51 LIBRO 496 DE SOCIEDADES MERCANTILES" / closing: "…Y PARA LOS EFECTOS DE LEY , SE HACE LA PRESENTE PUBLICACIÓN. GUATEMALA [date]. EXP . [year-filed].- ULTIMA LINEA." | Modification notices share one grammar: escritura → prior registration coordinates (registro/folio/libro — spanning legacy books 22-496, evidencing the register's book migration) + expediente with original filing year → the assembly accord → the reforming clause "REMAINING AS FOLLOWS…". Observed kinds: capital increase (dominant, incl. Q100M cases), domicile change, denomination + trade-name change, share nominal-value change, clause modifications. "MODIFICACIÓN ELECTRÓNICA #N" = RM's electronic-filing variant of the same notice. Each modification = one edicto event priced by 73_ (Q200 major / Q100 other) | `gt/sources/83_RM_edictos_2026-08-19.pdf` | pp.27-28, section "MODIFICACIÓN DE SOCIEDADES" (EVID-601) |
| LB-009 | 83_ disolución template + liquidador registration: disolución: "EL REGISTRO MERCANTIL CON BASE EN EL TESTIMONIO DE LA ESCRITURA Nº 12 AUTORIZADA EN LA CIUDAD DE GUATEMALA EL 09 DE JUNIO DE 2026 POR EL NOTARIO JOSE DOMINGO PAREDES MORALES, SE INSCRIBE LA DISOLUCIÓN DE LA ENTIDAD: POC DX, SOCIEDAD ANÓNIMA, INSCRITA AL REGISTRO Nº 104378 FOLIO 64 LIBRO 198 DE SOCIEDADES MERCANTILES; LA DISOLUCIÓN SE EFECTÚA EN VIRTUD DE RESOLUCIÓN ACORDADA EN ASAMBLEA GENERAL EXTRAORDINARIA TOTALITARIA DE ACCIONISTAS. EN LA FORMA Y DEMÁS TÉRMINOS CONTENIDOS EN DICHO INSTRUMENTO LEGAL. Y PARA LOS EFECTOS DE LEY SE HACE LA PRESENTE PUBLICACIÓN. GUATEMALA, 29 DE JULIO DE 2026. EXP . 54798-2013. ULTIMA LINEA." / liquidador: "QUEDA INSCRIT(O/A) : RITA MARIA ACAJABON MARTINEZ BAJO NUMERO DE REGISTRO: 850479, FOLIO : 488, LIBRO : 864, DE AUXILIARES DE COMERCIO, COMO LIQUIDADORA DE INVERSIONES BIARRITZ (EN LIQUIDACIÓN), SOCIEDAD ANÓNIMA CON BASE EN NOMBRAMIENTO AUTORIZADO EL 23 DE JULIO DE 2026 POR EL NOTARIO RAFAEL ALFONSO ARCIA RODRIGUEZ. PLAZO: DEFINIDO: 1 AÑOS , CON VIGENCIA A PARTIR DEL: 03 DE JULIO DE 2026" / second form: "…SE INSCRIBE A JAIME SAUL BARRIOS PAR COMO LIQUIDADOR BAJO EL REGISTRO: 852785, FOLIO: 108, LIBRO: 865, DE AUXILIARES DE COMERCIO, DE LA ENTIDAD: INMOBILIARIA M.P .I. (EN LIQUIDACIÓN)… PLAZO 1 AÑO. SE HACE DEL CONOCIMIENTO PUBLICO QUE DICHA SOCIEDAD HA ENTRADO EN LIQUIDACION. … ARTOS. [sic ARTS.] 242, 243 Y 343 DEL CODIGO DE COMERCIO.---- ULTIMA LINEA." | Dissolution by resolution of an extraordinary (totalitaria) general shareholders' assembly; the liquidation phase adds: (i) liquidador appointment registered in the AUXILIARES DE COMERCIO register (own libro/folio numbering, ~libro 864-865 in 2026) with a defined term of 1 year and express notice that the society "HAS ENTERED LIQUIDATION", citing CC arts. 242, 243 y 343; (ii) the entity name then carries "(EN LIQUIDACIÓN)". Fees: disolución Q300 (provisional), liquidador Q150, auxiliares Q150 (LB-002) | `gt/sources/83_RM_edictos_2026-08-19.pdf` | p.29 section "DISOLUCIÓN/CANCELACIÓN"; pp.30/35 auxiliares entries (EVID-602) |
| LB-010 | 83_ empresa-mercantil layer (Edictos Varios): dirección: "AL REGISTRO MERCANTIL, SE PRESENTO ROLANDO OSIEL XILOJ REYES COMO ADMINISTRADOR ÚNICO Y REPRESENTANTE LEGAL DE IRC LA BENDICION, SOCIEDAD ANÓNIMA SOLICITANDO SE INSCRIBA CAMBIO DE DIRECCION COMERCIAL DE LA EMPRESA MERCANTIL DENOMINADA DISTRIBUIDORA LA BENDICIÓN DE OCCIDENTE REGISTRADA AL NUMERO 1074730 FOLIO 149 LIBRO 1216 DE EMPRESAS. A: CALZADA ROOSEVELT 32-27… Y PARA LOS EFECTOS DE LEY , SE HACE LA PRESENTE PUBLICACION EXP . 3882-2024 GUATEMALA 30 JULIO 2026 ULTIMA LINEA." / nombre comercial: "…SE INSCRIBA CAMBIO DE NOMBRE COMERCIAL DE LA EMPRESA MERCANTIL DENOMINADA LABORATORIO CLÍNICO XICAY REGISTRADA AL NUMERO 1238365 FOLIO 383 LIBRO 1284 DE EMPRESAS. A: XICAY…" / clausura: "…CHRYSTIAN ALBERTO LOPEZ RODAS QUIEN ACTÚA EN CALIDAD DE PRESIDENTE DEL CONSEJO DE ADMINISTRACION Y REPRESENTANTE LEGAL DE MEDIPRO, SOCIEDAD ANÓNIMA SOLICITANDO SE INSCRIBA CLAUSURA DE LA EMPRESA MERCANTIL DENOMINADA MEDIPRO REGISTRADA AL NUMERO 423913 FOLIO 849 LIBRO 385 DE EMPRESAS…" / registry-announced variant: "EL REGISTRO MERCANTIL GENERAL DE LA REPUBLICA HACE DEL CONOCIMIENTO PUBLICO QUE LA ENTIDAD …SOCIEDAD ANÓNIMA INSCRITA BAJO REGISTRO … DE SOCIEDADES MERCANTILES. CAMBIO DE DIRECCION A …" / traspaso (Balance section): "AL REGISTRO MERCANTIL SE PRESENTO ANDREA YOHANA CABRERA VELASQUEZ DANDO AVISO DEL TRASPASO POR APORTACION DE SU EMPRESA MERCANTIL DE NOMBRE COMERCIAL: ESTÁMPALO, INSCRITA BAJO REGISTRO: 1071954… SIENDO SU NUEVA PROPIETARIA LA ENTIDAD DENOMINADA: ÉLITE EVENTOS, SOCIEDAD ANONIMA…" | The bulk of the edition (16 of 47 pages) is the empresa mercantil register layer (establishments/business names — own LIBRO … DE EMPRESAS numbering, libro ~1179-1286 in 2026, vs sociedades libros ≤ ~496): commercial-address changes (dominant), trade-name changes, clausuras (~56 in this edition), address+object changes; two opener forms — promoter-filed ("THERE APPEARED BEFORE THE REGISTRAR … REQUESTING THE REGISTRATION OF …") and registry-announced ("THE REGISTRY MAKES PUBLICLY KNOWN THAT …"). Traspasos de empresa (by aportación/donación) appear with balance publication (LB-011) | `gt/sources/83_RM_edictos_2026-08-19.pdf` | pp.30-36 "EDICTOS VARIOS"; counts: 168 promoter-filed openers, ~56 clausuras file-wide (EVID-603) |
| LB-011 | 83_ convocatoria stubs + Balance publications: convocatoria stub (uniform): "GUATEMALA, 30 DE JULIO DE 2026. LA PUBLICACIÓN DE LA PRESENTE CONVOCATORIA SE REALIZA CON BASE AL ARTÍCULO 343 DEL CÓDIGO DE COMERCIO, LO QUE NO PREJUZGA SOBRE EL CONTENIDO NI VALIDEZ DE LA MISMA Y NO CONVALIDA HECHOS O ACTOS NULOS O ILÍCITOS. ULTIMA LINEA." (each preceded only by "EXPDIENTE: 12765-1999Ð" etc. [as printed: EXPEDIENTE]) / balance anual: "EL REGISTRO MERCANTIL HACE DEL CONOCIMIENTO PÚBLICO EL BALANCE GENERAL ANUAL, DE LA ENTIDAD: ROMALATTE, SOCIEDAD ANÓNIMA, INSCRITA CON REGISTRO NO. 69406 FOLIO 60 LIBRO 163 DE SOCIEDADES MERCANTILES Y PARA LOS EFECTOS DE LEY SE HACE LA PRESENTE PUBLICACIÓN. QUE LITERALMENTE SE LEE:. GUATEMALA 30 DE JULIO DEL 2026. EXP . 51770-2006.- ULTIMA LINEA." / balance final: "…EL BALANCE GENERAL FINAL DE LA ENTIDAD: POP MONITOR, SOCIEDAD ANONIMA (EN LIQUIDACION)… Y PARA QUE LA ASAMBLEA CONOZCA Y SE PRONUNCIE SOBRE EL PRESENTE BALANCE SEÑALA PLAZO ESTABLECIDO EN LA LEY , ARTICULO 251 CODIGO DE COMERCIO, EN LA SEDE SOCIAL." / fusión pair: "…INSCRIBE EL ACUERDO DE FUSIÓN POR ABSORCIÓN DE LA ENTIDAD: INMOBILIARIA CRISTAL, SOCIEDAD ANÓNIMA… CON LA ENTIDAD: IQ10, SOCIEDAD ANONIMA, FUSIÓN EN QUE LA PRIMERA ABSORBE A LA SEGUNDA, ADQUIRIENDO LOS ACTIVOS Y PASIVOS DE LA SOCIEDAD ABSORBIDA… Y PARA LOS EFECTOS DE LEY SE PUBLICA EL RESPECTIVO BALANCE QUE LITERALMENTE SE LEE." (mirror entry for IQ10 same date) / traspaso: "…DANDO AVISO DEL TRASPASO POR DONACION DE LA EMPRESA MERCANTIL… Y PARA LOS EFECTOS DE LEY SE PUBLICA EL RESPECTIVO BALANCE QUE LITERALMENTE SE LEE:" | Convocatoria entries in this text layer are STUBS: expediente + date + art.-343 boilerplate ("WHICH PREJUDGES NEITHER CONTENT NOR VALIDITY… NOR VALIDATES NULL OR UNLAWFUL FACTS OR ACTS") — the assembly-notice content itself is not extractable (GOQ-131: never asserted). Balance section carries: balance general anual (ordinary annual publication); balance general final for societies "(EN LIQUIDACIÓN)" with the assembly-pronouncement window of CC art. 251; fusión por absorción published as paired mirror entries (absorbing + absorbed each publish, with balance); traspasos de empresa (aportación/donación) with balance "WHICH LITERALLY READS" | `gt/sources/83_RM_edictos_2026-08-19.pdf` | pp.46-47, sections "CONVOCATORIA" and "BALANCE" (EVID-604) |
| LB-012 | CCom art. 333: "El Registro Mercantil será público y llevará los siguientes libros: 1º. De comerciantes individuales. 2º. De sociedades mercantiles. 3º. De empresas y establecimientos mercantiles. 4º. De auxiliares de comercio. 5º. De presentación de documentos. 6º. Los libros que sean necesarios para las demás inscripciones que requiere la ley. 7º. Indices y libros auxiliares. … Los libros del Registro Mercantil podrán ser reemplazados en cualquier momento y sin necesidad de trámite alguno, por otros sistemas más modernos." / art. 335: "La inscripción del comerciante individual se hará mediante declaración jurada del interesado, consignada en formulario con firma autenticada, que comprenderá: 1º. Nombres y apellidos completos, edad, estado civil, nacionalidad, domicilio y dirección. 2º. Actividad a que se dedique. 3º. Régimen económico de su matrimonio, si fuere casado o unido de hecho. 4º. Nombre de su empresa y sus establecimientos y sus direcciones. 5º. Fecha en que haya dado principio su actividad mercantil. El registrador razonará la cédula de vecindad del interesado." / art. 337: "La inscripción de las sociedades mercantiles se hará con base en el testimonio respectivo, que comprenderá: 1º. Forma de organización. 2º. Denominación o razón social y nombre comercial si lo hubiere. 3º. Domicilio y el de sus sucursales. 4º. Objeto. 5º. Plazo de duración. 6º. Capital social. 7º. Notario autorizante de la escritura de constitución, lugar y fecha. 8º. Organos de administración, facultades de los administradores. 9º. Organos de vigilancia si los tuviere. Siempre que se trate de sociedades cuyo objeto requiera concesión o licencia estatal, será indispensable adjuntar el acuerdo gubernativo o la autorización correspondiente y el término de inscripción principiará a contar a partir de la fecha del acuerdo o autorización." / art. 338 (selected literales): "1. El nombramiento de administradores de las sociedades, de factores y el otorgamiento de mandatos por cualquier comerciante… 5. Las modificaciones de la escritura constitutiva de las sociedades mercantiles, la prórroga de su plazo y la disolución o liquidación. … 8. Las emisiones de acciones y de otros títulos que entrañen obligaciones para las sociedades mercantiles, expresando su serie, valor y monto de la emisión, sus intereses, primas y amortizaciones… Las operaciones a que se refiere esta literal serán inscritas exclusivamente en el Registro Mercantil. 9. Los Agentes, Distribuidores y Representantes." + tag "*Reformado por el Artículo 18, del Decreto Del Congreso Número 11-2006 el 30-05-2006" | The RM is PUBLIC and keeps the listed book classes; its books may be replaced at any time without procedure by more modern systems (the electronic-book hook the 83_ portal realizes). Individual-merchant inscription via sworn form (identity, activity, marital property regime — including unión de hecho —, empresa names + addresses, activity start). Society inscription via testimonio comprising 9 fields (form, name + trade name, domicile + branches, object, term, capital, notary + place + date, administration organs, surveillance organs); a state concession/license gates the inscription window. Art. 338 ongoing acts: administrator appointments, mandates, deed modifications/prórroga/dissolution/liquidation, share and bond emissions (RM-EXCLUSIVE), and literal 9 (added by D-11-2006) agents/distributors/representatives | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.73 art. 333; p.74 arts. 335-337; p.75 art. 338 (EVID-539) |
| LB-013 | CCom arts. 339/341/342/343 (as printed, pre-D18-2017 — R64): art. 339: "Los actos y documentos que conforme la ley deben registrarse, sólo surtirán efecto contra terceros desde la fecha de su inscripción en el Registro Mercantil. Ninguna inscripción podrá hacerse alterando el orden de presentación." / art. 341: "Solicitada la inscripción de una sociedad o de cualquier modificación a su escritura social, el Registrador con vista del testimonio respectivo, si la escritura llena los requisitos legales… hará la inscripción provisional y la pondrá en conocimiento del público por medio de un aviso por cuenta del interesado publicado en el diario oficial. … Si se tratare de sociedades colectivas o de responsabilidad limitada, es forzoso publicar el nombre de todos los socios. Transcurridos sesenta días (60), desde la fecha de inscripción provisional sin que se hubiere presentado la publicación del edicto, el Registrador ordenará la cancelación de la inscripción provisional." / art. 342: "El registrador denegará la inscripción, en forma razonada, si del examen de la escritura y de la información registral aparece que: a) En su otorgamiento no se observaron los requisitos legales o sus estipulaciones contravienen la ley. b) La razón social o la denominación es idéntica a otra inscrita, o no es claramente distinguinble [sic] de cualquier otra." / art. 343: "Ocho días hábiles después de la fecha de la publicación, si no hubiere objeción de parte interesada o del Ministerio Público… el Registrador hará la inscripción definitiva, cuyos efectos se retrotraerán a la fecha de inscripción provisional, y devolverá razonado el testimonio respectivo." / art. 345: "…las firmas de los otorgantes de documentos privados, deberán ser legalizadas." | Registered acts bind third parties ONLY from their inscription date; no inscription may alter presentation order. Procedure: on request, the registrar makes the PROVISIONAL inscription and gives it public notice via an aviso published at the interested party's cost in the official daily [66_ text; current channel = RM electronic portal per D-18-2017 art. 12 — R64]; for colectivas and R.L. all partners' names must be published; if the edicto publication is not proved within 60 days the provisional inscription is cancelled. Denial (reasoned) if legal requirements unmet or the name is identical to / not clearly distinguishable from another. EIGHT business days after publication without objection → DEFINITIVE inscription, retroactive to the provisional date; testimonio returned endorsed. Private-document signatures must be legalized | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.75 arts. 339-340; p.76 arts. 341-343, 345 (EVID-540) |
| LB-014 | CCom art. 332 + transitorias VIII/II: art. 332: "El Registro Mercantil funcionará en la capital de la República y en los departamentos o zonas que el Ejecutivo determine. Los registradores deberán ser Abogados y Notarios, colegiados activos, guatemaltecos naturales, tener por lo menos cinco años de ejercicio profesional y su nombramiento lo hará el Ejecutivo por el órgano del Ministerio de Economía. … El Ejecutivo por intermedio del citado Ministerio, emitirá los aranceles y reglamentos que procedieren." / transitoria VIII: "El registro mercantil deberá estar organizado y funcionando a partir de la fecha en que entre en vigor esta ley. El Organismo Ejecutivo deberá emitir el Reglamento del Registro Mercantil, el cual será propuesto por el registrador mercantil, incluyendo el arancel respectivo." / transitoria II (fees carve-out for adaptation deeds): "…se formalizará en escritura pública, la que para efectos fiscales será de valor indeterminado… Los honorarios de registro, en ese caso, serán de una tercera parte de lo que correspondería, conforme al arancel respectivo." | The RM sits under MinEconomía; registrars must be Guatemalan abogados y notarios with 5 years' practice, appointed by the Executive through the Ministry, which issues the ARANCELES and REGLAMENTOS. NO fee amounts are enacted in the Code — the fee source is the MinEconomía arancel instrument (73_ evidence). Transitory VIII: the Reglamento del Registro Mercantil (proposed by the registrar) includes the arancel. Transitory II: adaptation-to-Code deeds pay one third of the arancel honorarios | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.73 art. 332; p.207 transitoria II; p.209 transitoria VIII (EVID-541) |

## 3. Functional Requirements

### 3.1 Channel charter and instrument split (D-18-2017 art. 12; CC arts. 332, 343)

- **GT-CML-FR-001:** The system shall implement the official publication
  channel charter: ANY publication the *Código de Comercio* indicates must
  be made "en el Diario Oficial" shall be effected through an RM electronic
  medium, and such publication makes NO print publication necessary — the
  RM electronic portal DISPLACES print for all CCom-mandated publications
  (convocatorias, edictos of constitution/modification/dissolution,
  balances). CHANNEL GUARD (R64): the 66_ print (consolidated to
  30-05-2006) still routes arts. 341/343 publications to the Diario
  Oficial — current art. 343 mechanics = D-18-2017 art. 12, text as printed
  by the portal (83_); every 66_ procedural row below carries this
  verification note (GOQ-123 kin). This FR OWNS publication-channel
  execution: the per-ejercicio balance-publication duty flag of
  `01_books-anchor.md` GT-COA-FR-021 is consumed here by exact id and
  discharged through this channel (FR-018). Rejected myth (wave set):
  treating any CCom-mandated publication as a newspaper/Diario-Oficial
  step after D-18-2017. (LB-005; EVID-598; GT-COA-FR-021; R64; GOQ-123)
- **GT-CML-FR-002:** The system shall enforce the MinEconomía
  instrument-split guard: the CCom enacts NO fee amounts — the fee source
  is the Executive/MinEconomía *arancel* (with the *Reglamento del Registro
  Mercantil* proposed by the registrar, transitoria VIII) — so no RM fee
  row shall ever be cited to the Code; every RM fee row stores its
  instrument provenance as the arancel (73_) with the no-date identity
  caveat (FR-003). The one statutory fee modifier — adaptation-to-Code
  deeds pay one third of the arancel *honorarios* (transitoria II) — is
  recorded as a dated provenance row, never applied by computation.
  (LB-014; EVID-541)
- **GT-CML-FR-003:** The system shall store the entire 73_ fee catalog as
  D16 dated-2022-label rows: the instrument prints NO date or instrument
  number (label-derived as-of 2022) and its own "Ajuste por vigencia de
  nuevo Arancel" / "Ajuste por CERTIFICACIONES según nuevo Arancel" rows
  presuppose wholesale arancel supersession cycles — EVERY fee row carries
  the re-verify flag (R66), no valid_to is asserted until re-verified
  against the current arancel, and no fee is auto-computed or auto-charged
  (recorded exposure only). Rejected myth (wave set): "RM arancel values
  are current". (LB-001; EVID-594; R66)

### 3.2 The RM fee catalog (73_ as dated data)

- **GT-CML-FR-004:** The system shall carry the society-lifecycle trámite
  fee rows as dated-2022-label config (all R66 re-verify-flagged):
  inscripción de comerciante Q100 and inscripción de empresas Q100;
  sociedad extranjera Q1,500 + arancel variable; actas de asambleas
  extraordinarias Q150; ampliación de capital Q500 + arancel variable;
  modificación de escritura de sociedad Q300; disolución de sociedad
  (provisional) Q300; nombramiento de liquidador Q150; cancelación de
  empresa Q150; auxiliares de comercio (inscripción/cancelación) Q150;
  despachos judiciales (empresa/sociedad) Q150; traspaso de empresa Q150;
  inscripción de mandatos Q150; inscripción de prendas Q150; emisión de
  acciones y títulos Q200; cambio de dirección sociedad Q150; reposición
  de patente (empresa/sociedad) Q150. OCR-damaged numerals are stored as
  printed with restoration brackets in provenance. (LB-002; EVID-595; R66)
- **GT-CML-FR-005:** The system shall implement the variable-scale
  NEGATIVE row: sociedad inscripción is priced "Variable + arancel
  variable" and the variable scale itself is NOT printed in 73_ (nor for
  extranjera/ampliación "+ arancel variable" rows) — NO computable
  inscripción fee shall be derived; the surface records "base Variable +
  unprinted variable scale" with the re-verify flag, and the Q500,000
  boundary is handled per FR-020 (inference only). (LB-002; EVID-595;
  R66)
- **GT-CML-FR-006:** The system shall implement the matrícula/renovación
  NEGATIVE row: the *matrícula* (patente) fee and its renovación are NOT
  rows of the 73_ schedule (only "Reposición de patente" Q150 appears) —
  no matrícula or renovación fee shall be modeled from 73_; the patente
  fee surface stays empty pending the current arancel/RTU (re-verify
  flag; C4 owns the matrícula/patente obligation model — this file owns
  only the fee-row absence). (LB-002; EVID-595; R66)
- **GT-CML-FR-007:** The system shall carry the edicto/publication fee
  classes as dated-2022-label config (R66 re-verify-flagged): "Pago de
  edicto" Q30 (per-edicto processing charge) plus the per-event
  publicación classes — sociedades nuevas Q200; modificaciones mayores
  (transformación, fusión, disoluciones, aumento o disminución de
  capital) Q200; otras modificaciones (cambios de dirección, objeto) Q100;
  clausura o traspaso de empresa Q100; otros motivos Q100; fe de erratas
  Q25. Each channel event type maps to exactly one publicación class plus
  the edicto charge (the per-event cost model of FR-024).
  (LB-003; EVID-596; R66)
- **GT-CML-FR-008:** The system shall carry the auxiliary-service fee rows
  as dated-2022-label config (R66 re-verify-flagged): certificaciones Q50;
  multas Q25; reingreso de documentos rechazados Q25; consultas en línea
  (e-consultas) = Variable (no amount derivable). The multa row is the RM
  administrative-fine exposure surface — recorded exposure, never computed
  sanctions (sanction-track separation per GT-COA-FR-020/FR-060, consumed
  by id). (LB-003; EVID-596; R66; GT-COA-FR-020)
- **GT-CML-FR-009:** The system shall NOT re-derive the RM
  books-authorization fee: "Autorización de Libros Pago Variable 29 Q 0.20
  x Hoja" is owned by `02_dual-track-habilitacion.md` GT-COA-FR-041
  (kin-cited here; the C3 catalog imports it by exact id into the same
  dated-2022-label regime — one row, one owner, no duplication).
  (LB-003; EVID-596; GT-COA-FR-041; R66)

### 3.3 RM registration coordinates and the provisional→definitiva procedure (arts. 333/335-343, as printed)

- **GT-CML-FR-010:** The system shall model RM registration coordinates as
  the record-addressing grammar of every edicto payload and RM-event
  record: *registro* (number) · *folio* · *libro* (with register class) ·
  *expediente* (with filing year) — across the register classes of art.
  333 (comerciantes individuales; sociedades mercantiles — currently LIBRO
  ELECTRONICO 29 per 83_; empresas y establecimientos mercantiles — LIBRO …
  DE EMPRESAS, ~1179-1286 in 2026; auxiliares de comercio — ~libro
  864-865; presentación de documentos; auxiliary books). The registry is
  PUBLIC; its books "podrán ser reemplazados… por otros sistemas más
  modernos" — the observed libro-number migration (legacy books 22-496 →
  electronic book 29) is recorded as provenance, never migrated by the
  system. (LB-006; LB-008; LB-012; EVID-599/601/539)
- **GT-CML-FR-011:** The system shall carry the RM inscription field
  inventory as the payload-source schema for edicto generation (the
  lifecycle-content owner is C4 — forward ref, cluster only; this file
  owns the schema the channel exposes): comerciante individual via sworn
  form (names, age, civil status, nationality, domicile + address;
  activity; marital property regime incl. *unido de hecho*; empresa +
  establecimiento names and addresses; activity start); sociedades via
  testimonio — 9 fields (forma de organización; denominación/razón social
  + nombre comercial; domicilio + sucursales; objeto; plazo; capital
  social; notario + place + date; órganos de administración +
  administradores' faculties; órganos de vigilancia); the state
  concession/license gate (inscription window runs from the governmental
  agreement/authorization); and the art. 338 ongoing-act classes
  (administrator appointments/factors/mandates; escritura modifications,
  prórroga, disolución, liquidación; RM-EXCLUSIVE share/bond emissions
  with serie/valor/monto/intereses/primas/amortizaciones; literal 9
  agentes/distribuidores/representantes — texto D-11-2006).
  (LB-012; EVID-539; GOQ-123 kin)
- **GT-CML-FR-012:** The system shall implement the provisional → edicto
  → definitiva lifecycle as tracked states on the RM-event record: on
  request the registrar makes the inscripción PROVISIONAL and gives it
  public notice via the edicto (published at the interested party's cost —
  channel per FR-001); if the edicto publication is not proved within 60
  days the provisional inscription lapses (cancellation ordered); EIGHT
  días hábiles after the publication date without objection of an
  interested party or the Ministerio Público → inscripción DEFINITIVA,
  whose effects RETROACT to the provisional date (the record stores both
  dates and derives the retroactivity as recorded fact, not as computed
  legal effect); denial grounds surface as checks — unmet legal
  requirements/unlawful stipulations, or a razón social/denominación
  identical to or not clearly distinguishable from another (colectivas and
  R.L. must publish ALL socios' names). R64 verification note: these
  66_-printed arts. 341/343 texts route the aviso to the diario oficial —
  the current publication step is the RM electronic portal (FR-001); the
  windows and the 60-day lapse rule are the pre-D18-2017 texts as printed
  and ride the GOQ-123 kin flag. (LB-013; EVID-540; R64; GOQ-123 kin)
- **GT-CML-FR-013:** The system shall record the effect/order rules of
  art. 339 as registry-side facts on the RM-event record: registered acts
  bind third parties ONLY from their inscription date, and no inscription
  may alter the order of presentation (presentation timestamp is an
  immutable ordering key). Legalized private-document signatures (art.
  345) are recorded as a provenance attribute. (LB-013; EVID-540)

### 3.4 Edicto payload templates (83_ snapshot — channel shape only)

- **GT-CML-FR-014:** The system shall carry the inscripción-edicto
  template as shared dated data (channel shape; snapshot 2026-08-19,
  edición 6022): escritura number + city + date + notary → RM presentation
  date/time → registro/folio/LIBRO ELECTRONICO 29 DE SOCIEDADES
  MERCANTILES/expediente → denominación + sociedad form + nombre comercial
  → domicilio (departamento + sede) → objeto (clause list, closing "Y
  OTROS QUE CONSTAN EN LA ESCRITURA SOCIAL") → PLAZO (typically
  INDEFINIDO) → capital social AUTORIZADO/SUSCRITO/PAGADO + share count
  and valor nominal → órganos (administración; representación legal;
  vigilancia) → Guatemala date → "ULTIMA LINEA." terminator; some entries
  add a second/clarification escritura. This is the observable public
  output shape of RM society registration — the fields an Odoo
  company-formation workflow feeds (via notary), never a form the company
  files itself. (LB-006; EVID-599; GOQ-131 kin)
- **GT-CML-FR-015:** The system shall carry the modificación-notice
  template and its observed kinds as shared dated data: escritura → prior
  registration coordinates (registro/folio/libro, legacy books 22-496) +
  expediente → the assembly accord (asamblea general extraordinaria
  [totalitaria]) → the reforming clause "QUEDANDO DE LA SIGUIENTE
  MANERA…"; kinds = aumento de capital (dominant), cambio de domicilio,
  cambio de denominación social y nombre comercial, cambio del valor
  nominal de acciones, modificación de cláusulas; the
  "MODIFICACIÓN ELECTRÓNICA #N" tag = the electronic-filing variant of the
  same notice; closing formula "…Y PARA LOS EFECTOS DE LEY, SE HACE LA
  PRESENTE PUBLICACIÓN. GUATEMALA [date]. EXP. [year-filed].- ULTIMA
  LINEA." Each kind is one channel event priced by FR-007 (Q200 major /
  Q100 other); the lifecycle-event model is C4's (forward ref, cluster
  only). (LB-008; EVID-601; GOQ-131 kin)
- **GT-CML-FR-016:** The system shall carry the disolución/liquidación
  templates as shared dated data: disolución notice (escritura → prior
  coordinates → "LA DISOLUCIÓN SE EFECTÚA EN VIRTUD DE RESOLUCIÓN
  ACORDADA EN ASAMBLEA GENERAL EXTRAORDINARIA [TOTALITARIA] DE
  ACCIONISTAS" → publication formula); liquidador appointment registered
  in the AUXILIARES DE COMERCIO register (own registro/folio/libro,
  ~864-865) with plazo definido (observed: 1 año) and the express notice
  that the society "HA ENTRADO EN LIQUIDACION", citing CC arts. 242, 243
  y 343; the entity name then carries "(EN LIQUIDACIÓN)" (status label
  consumed by C4's lifecycle model — forward ref, cluster only). Fees per
  FR-004 (disolución Q300 provisional; liquidador Q150; auxiliares Q150).
  (LB-009; EVID-602; GOQ-131 kin)
- **GT-CML-FR-017:** The system shall carry the empresa-mercantil layer
  templates as shared dated data (the Edictos Varios section — the bulk of
  the observed edition): promoter-filed opener ("AL REGISTRO MERCANTIL,
  SE PRESENTO [X] COMO [cargo] DE [sociedad] SOLICITANDO SE INSCRIBA…")
  and registry-announced opener ("EL REGISTRO MERCANTIL GENERAL DE LA
  REPUBLICA HACE DEL CONOCIMIENTO PUBLICO QUE…"); events = cambio de
  dirección comercial (dominant), cambio de nombre comercial, clausura
  (~56 in the observed edition), cambio de dirección y objeto, traspaso
  (por aportación/donación, with balance per FR-018); coordinates in
  LIBRO … DE EMPRESAS (own numbering, ~1179-1286 — distinct register
  layer from sociedades). The empresa mercantil / nombre comercial is a
  registerable asset distinct from the sociedad; its events are priced by
  FR-004/FR-007 (dirección/objeto Q150 + Q100 publicación; clausura Q150
  + Q100; traspaso Q150 + Q100). (LB-010; EVID-603; GOQ-131 kin)
- **GT-CML-FR-018:** The system shall implement the balance-publication
  families on this channel, discharging GT-COA-FR-021's per-ejercicio
  duty via FR-001: (i) *balance general anual* — the ordinary annual
  publication ("QUE LITERALMENTE SE LEE" — the balance text is reproduced
  in the edition); (ii) *balance general final* for sociedades "(EN
  LIQUIDACIÓN)", with the assembly-pronouncement window of CC art. 251 at
  the sede social; (iii) *fusión por absorción* agreements published as
  PAIRED MIRROR ENTRIES (absorbing and absorbed societies each publish,
  with the respective balance); (iv) *traspaso de empresa* (aportación/
  donación) with balance. The publication-obligation flag consumed from
  GT-COA-FR-021 keys the anual family; the final/fusión/traspaso
  families key on the liquidation/fusion/transfer events (C4 lifecycle
  content — forward ref, cluster only). (LB-011; EVID-604;
  GT-COA-FR-021; GOQ-131 kin)
- **GT-CML-FR-019:** The system shall implement the convocatoria STUB
  guard: convocatoria entries in the 83_ text layer are stubs — expediente
  + date + the art.-343 boilerplate ("LA PUBLICACIÓN DE LA PRESENTE
  CONVOCATORIA SE REALIZA CON BASE AL ARTÍCULO 343 DEL CÓDIGO DE
  COMERCIO, LO QUE NO PREJUZGA SOBRE EL CONTENIDO NI VALIDEZ DE LA MISMA
  Y NO CONVALIDA HECHOS O ACTOS NULOS O ILÍCITOS.") and NOTHING else —
  convocatoria CONTENT shall NEVER be asserted, extracted or modeled from
  83_ (rejected myth, wave set); the channel surface records the
  convocatoria event class (assembly notice → RM portal publication) with
  the non-prejudice boilerplate traveling as provenance metadata, content
  left open (GOQ-131). (LB-011; EVID-604; GOQ-131)
- **GT-CML-FR-020:** The system shall implement the Q500,000 inference
  guard: the observed just-under-Q500,000 capital-autorizado cluster
  (Q499,000-Q499,999 with minimal paid-in, 6+ of ~27 sampled entries,
  with counterexamples at Q5,000 and Q20,000,000) is recorded as observed
  market behavior ONLY — the Q500,000 boundary is an INFERENCE pointing
  at the unprinted arancel-variable scale (FR-005), never a configured
  threshold, validation or default; no amount, warning or nudge shall be
  derived from it (R66). (LB-007; EVID-600; R66)

### 3.5 Channel operations: generation, tracking, ingestion (single-snapshot discipline)

- **GT-CML-FR-021:** The system shall provide the edicto payload
  generation surface: from a company's RM-event data (FR-011 schema) and
  the applicable template (FR-014..018), render the edicto payload text
  in the observed grammar — a preparation/export surface for the notary/
  promoter workflow, which NEVER files to the RM portal itself (the RM
  files via notary or promoter; the system records facts, it does not
  emulate the registry). Generated payloads carry template version
  (snapshot 2026-08-19, edición 6022) and the GOQ-131 kin flag.
  (LB-006; LB-008; LB-009; EVID-599/601/602; GOQ-131 kin)
- **GT-CML-FR-022:** The system shall provide publication-event lifecycle
  tracking on the RM-event record: pending → edicto-published (edition
  reference/URL + publication date captured from the portal snapshot) →
  provisional/definitiva states per FR-012, with the 60-day proof window
  and the 8-días-hábiles definitive window surfaced as dated reminders/
  exposure (deadline computed from the recorded publication date; no
  legal effect is emulated — RM's own resolution is ingested, not
  generated). (LB-013; EVID-540/597; R64; GOQ-123 kin)
- **GT-CML-FR-023:** The system shall provide portal-snapshot ingestion
  and monitoring on the SaaS side: ingest RM portal editions (dated
  snapshots keyed by edición number + date, e.g. edición 6022 =
  2026-08-19) as evidence records; match published edictos against
  tracked publication events (FR-022) to confirm publication completion;
  and monitor for supersession of the 73_ arancel and channel changes —
  D2 dual-validation on the shared dated rows. Monitoring NEVER asserts
  norms a single edition cannot evidence (cadence, volumes, lag →
  GOQ-131). (LB-004; EVID-597; GOQ-131)
- **GT-CML-FR-024:** The system shall assemble the per-event cost-exposure
  row for each RM channel event: trámite fee (FR-004, where printed) +
  edicto Q30 + publicación class fee (FR-007) — e.g. sociedad-nueva
  inscripción = Q30 edicto + Q200 publicación + unprinted Variable
  inscripción (FR-005); dirección-type modificación = Q30 + Q100 + Q300
  modificación de escritura; clausura de empresa = Q30 + Q100 + Q150 —
  all as dated-2022-label recorded exposure (R66 re-verify flag), never
  invoiced, auto-charged or posted by the system.
  (LB-002; LB-003; EVID-595/596; R66)
- **GT-CML-FR-025:** The system shall record the RM-side cancellation
  exposure surface (taxation kin, consumed by id): CT art. 85 recidivism
  — reoffending in cierre temporal leads the RM to CANCEL the empresa's
  inscripción and patente — is owned by the taxation wave
  (GT-TAX-FR-216/217, consumed by exact id, never re-derived here); this
  file exposes only the RM-side fact slots (inscripción/patente
  cancellation state + provenance link to the taxation sanction row) on
  the RM-event record, with the RM multa track (GT-COA-FR-020) kept a
  separate, never-netted exposure (R62 sanction-track separation).
  (LB-002; EVID-595; GT-TAX-FR-216/217; GT-COA-FR-020; R62)

## 4. Data Model

Layer semantics: the fee catalog, publication classes, edicto templates
and RM data-model schema are dated config shared across the architecture;
edicto payload generation and the provisional→definitiva lifecycle
tracking live in the Odoo client; portal-snapshot ingestion/monitoring
lives on the SaaS side. The system records compliance facts and prepares
payloads — it never emulates the Registro Mercantil, never files to the
portal and never charges RM fees. No printed data table in this file
warrants a CSV sidecar: the 73_ rows are an OCR-damaged, no-date snapshot
whose verified transcription lives in the evidence file
(`gt/.extractions/60_73_83_RM.evidence.md`) and whose machine load awaits
the re-verified current arancel (R66) — seeding a sidecar now would
reify an unverified snapshot.

**RM fee catalog (l10n_gt_commerce.rm_fee — dated rows, D16):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.rm_fee | trámite | select | inscripcion_comerciante (Q100) · inscripcion_empresa (Q100) · inscripcion_sociedad (Variable + unprinted scale) · sociedad_extranjera (Q1,500 + variable) · actas_extraordinarias (Q150) · ampliacion_capital (Q500 + variable) · modificacion_escritura (Q300) · disolucion_provisional (Q300) · nombramiento_liquidador (Q150) · cancelacion_empresa (Q150) · auxiliares (Q150) · despacho_judicial (Q150) · traspaso (Q150) · reposicion_patente (Q150) · mandatos (Q150) · prendas (Q150) · emision_acciones (Q200) · cambio_direccion_sociedad (Q150) · certificaciones (Q50) · multas (Q25) · reingreso_rechazados (Q25) · e_consultas (Variable) | FR-004, FR-008 |
| l10n_gt_commerce.rm_fee | amount · basis | monetary + select | fixed Q-amount as printed · variable (scale unprinted — no computable amount) · per_hoja (books row, imported from GT-COA-FR-041 by id) | FR-004, FR-005, FR-008, FR-009 |
| l10n_gt_commerce.rm_fee | instrument · as_of · re_verify · valid_to | char + date + flags | instrument = "RM arancel (73_; prints NO date/instrument number)"; as_of = 2022 (label-derived); re_verify = true on EVERY row (R66); valid_to = never asserted until re-verified | FR-003 |
| l10n_gt_commerce.rm_fee | matricula_row · renovacion_row | NO ROW BY DESIGN | absence is the requirement — patente/renovación fee rows absent from 73_ (only reposición); guard comment in the seed (R66) | FR-006 |

**Publication classes (l10n_gt_commerce.rm_publication_class):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.rm_publication_class | class | select | sociedades_nuevas (Q200) · modificaciones_mayores: transformación/fusión/disoluciones/capital ± (Q200) · otras_modificaciones: dirección/objeto (Q100) · clausura_traspaso_empresa (Q100) · otros_motivos (Q100) · fe_erratas (Q25) | FR-007 |
| l10n_gt_commerce.rm_publication_class | edicto_charge | monetary | Q30 per edicto ("Pago de edicto") — rides every publication event | FR-007, FR-024 |

**RM event + edicto payload (l10n_gt_commerce.rm_event):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.rm_event | kind | select | inscripcion_sociedad · modificacion (kinds per FR-015) · disolucion · liquidador_auxiliares · empresa_direccion · empresa_nombre_comercial · clausura · traspaso · balance_anual · balance_final · fusion · convocatoria (stub class) · cancelacion | FR-012, FR-014..019 |
| l10n_gt_commerce.rm_event | coordinates | json | registro · folio · libro + register_class (sociedades/empresas/auxiliares/presentacion) · expediente + filing year | FR-010 |
| l10n_gt_commerce.rm_event | inscription_state | select + dates | solicitada · provisional (date) · definitiva (date; effects retroact to provisional — recorded fact) · provisional_lapsed (60-day window) · denegada (grounds: requisitos/estipulaciones · nombre no distinguible) | FR-012, FR-022 |
| l10n_gt_commerce.rm_event | publication_state | select + refs | pending · publicado (edición no. + date + URL from the ingested snapshot; capture timestamp = presentation-order key per art. 339) | FR-022, FR-023, FR-013 |
| l10n_gt_commerce.rm_event | payload_template · payload_text | m2o + text | template version keyed to the 83_ snapshot (2026-08-19, edición 6022); rendered per FR-014..018 grammar; convocatoria payloads = stub + boilerplate only | FR-021, FR-019 |
| l10n_gt_commerce.rm_event | cost_exposure | computed json | trámite fee + edicto Q30 + publicación class (FR-024 assembly); recorded exposure only — never invoiced/auto-charged | FR-024 |
| l10n_gt_commerce.rm_event | rm_cancellation_slots | fields | inscripción/patente cancellation state + link to the taxation sanction row (GT-TAX-FR-216/217 by id; R62 track separation) | FR-025 |

**RM data-model schema (payload-source fields, art. 335/337/338; consumed by C4):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| schema row (l10n_gt_commerce.rm_inscription_field) | party | select | comerciante_individual (art. 335 sworn-form 5 fields incl. marital regime) · sociedad (art. 337 nine testimonio fields) · ongoing_act (art. 338 classes; literal 8 = RM-exclusive emissions; literal 9 = texto D-11-2006) | FR-011 |
| schema row | concession_gate | boolean + date | objeto requiring state concession/license → inscription window runs from the acuerdo/autorización date | FR-011 |

**Portal snapshot (saas ingestion):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.rm_portal_snapshot | edición · date · sections | int + date + const set | e.g. edición 6022 = 2026-08-19; six fixed sections (inscripción · modificación · disolución/cancelación · edictos varios · convocatoria · balance); provenance = registromercantil.gob.gt / MinEconomía | FR-023 |
| l10n_gt_commerce.rm_portal_snapshot | matched_events · supersession_watch | o2m + flag | edicto→event matching for publication completion; arancel/channel supersession monitor (R66; GOQ-131 discipline: no cadence/volume/lag norms asserted) | FR-023 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2, wave defaults): `shared` =
the RM fee catalog, publication classes, edicto templates and the
inscription schema — dated config both sides must honor identically;
`odoo` = edicto payload generation and the provisional→definitiva
lifecycle tracking in the LGPL client; `saas` = RM-portal snapshot
ingestion and monitoring (D2 dual-validation on the shared dated rows).
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | shared | channel config row | art. 343 current mechanics | D-18-2017 art. 12 text (via 83_, R64); owns publication-channel execution; GT-COA-FR-021 consumed by id; GOQ-123 kin |
| FR-002 | shared | fee-instrument provenance | arancel = MinEconomía instrument | No fees in the Code (art. 332 + transitorias VIII/II); transitoria-II 1/3 row as provenance |
| FR-003 | shared | l10n_gt_commerce.rm_fee (all rows) | as_of=2022-label, re_verify | R66; no valid_to until re-verified; exposure only |
| FR-004 | shared | l10n_gt_commerce.rm_fee | trámite rows | Full 2022-label trámite set; OCR restorations bracketed in provenance |
| FR-005 | shared | l10n_gt_commerce.rm_fee | basis=variable | NEGATIVE row: scale unprinted — no computable inscripción fee |
| FR-006 | shared | rm_fee seed guard | matricula/renovación = no row | NEGATIVE row: only reposición Q150 printed (R66) |
| FR-007 | shared | l10n_gt_commerce.rm_publication_class | class + edicto Q30 | Q200/Q100/Q25 classes mapped to event types |
| FR-008 | shared | l10n_gt_commerce.rm_fee | certificaciones/multas/reingreso/e-consultas | Multa = recorded exposure; track separation R62 (GT-COA-FR-020 by id) |
| FR-009 | shared | rm_fee import | books row via GT-COA-FR-041 | Kin-cited, one owner (T2), no re-derivation |
| FR-010 | shared | rm_event.coordinates | registro/folio/libro/expediente | Register classes per art. 333; libro-migration provenance only |
| FR-011 | shared | rm_inscription_field schema | art. 335/337/338 inventories | Concession gate; literal 9 = texto D-11-2006; payload source for FR-021; C4 consumes |
| FR-012 | odoo | l10n_gt_commerce.rm_event | inscription_state + windows | 60-day lapse + 8 días hábiles + retroactivity as recorded facts; denial-ground checks; R64/GOQ-123 kin on the printed texts |
| FR-013 | odoo | l10n_gt_commerce.rm_event | presentation-order key | Art. 339 third-party effect + order immutability; art. 345 legalization attribute |
| FR-014 | shared | payload template config | inscripción grammar + "ULTIMA LINEA." | Snapshot 2026-08-19/edición 6022; GOQ-131 kin |
| FR-015 | shared | payload template config | modificación kinds + electronic variant | Kinds feed FR-007 fee classes; C4 owns the lifecycle events |
| FR-016 | shared | payload template config | disolución + liquidador auxiliares | "(EN LIQUIDACIÓN)" label consumed by C4; arts. 242/243/343 cite travels in the template |
| FR-017 | shared | payload template config | empresa-mercantil openers/events | DE EMPRESAS coordinates distinct from sociedades libros |
| FR-018 | shared | rm_event kinds + GT-COA-FR-021 flag | balance families | Anual keys on the T1 flag; final/fusión/traspaso on lifecycle events; art. 251 window noted |
| FR-019 | shared | stub guard | convocatoria = event class only | Content NEVER asserted from 83_ (GOQ-131); boilerplate as provenance |
| FR-020 | shared | inference guard | Q500,000 = observed pattern only | No threshold/validation/default derived (R66) |
| FR-021 | odoo | payload generation surface | template render + export | Preparation for notary/promoter workflow; never files to the portal |
| FR-022 | odoo | l10n_gt_commerce.rm_event | publication_state + deadlines | Reminders/exposure from recorded dates; RM resolution ingested, not generated |
| FR-023 | saas | rm_portal_snapshot ingestion | edición + matching + supersession watch | D2 dual-validation; no cadence/volume/lag norms (GOQ-131) |
| FR-024 | shared | rm_event.cost_exposure | per-event fee assembly | Trámite + Q30 + class fee; 2022-label exposure, never charged |
| FR-025 | shared | rm_event.rm_cancellation_slots | RM-side cancellation facts | Taxation kin (GT-TAX-FR-216/217 by id); R62 track separation |

Version-regime notes (D12/D15/D16): the CCom procedural rows resolve
as-of the domain anchor date with instrument provenance (D2-70 as
consolidated to 30-05-2006) and the R64/GOQ-123 verification note (art.
343 current mechanics = D-18-2017 art. 12 via 83_); the 73_ fee rows are
dated-2022-label rows (instrument prints no date; supersession-cycle
rows) with the re-verify flag — snapshot-on-write, no valid_to asserted
until re-verified (R66); the 83_ template/section rows are keyed to the
single snapshot 2026-08-19 (edición 6022) and assert channel shape only
(GOQ-131). Exposure rows are recorded, never charged; no legal effect
(inscription, retroactivity, cancellation) is computed — RM's own
resolutions are ingested as facts.

## 6. Acceptance Criteria

- **AC-001:** Given any CCom-mandated publication event configured in the
  system, when its channel is inspected, then it routes to the RM
  electronic portal (D-18-2017 art. 12 text with the R64 verification
  note against the 66_ print), no newspaper/Diario-Oficial step exists,
  and the art. 380 balance duty consumed from GT-COA-FR-021 discharges
  through this channel. (FR-001, FR-018)
- **AC-002:** Given the RM fee configuration, when inspected, then every
  73_-sourced row carries as_of = 2022 (label-derived), the re-verify
  flag and NO valid_to; the inscripción rows read "Variable + unprinted
  scale" with no computable amount; and NO matrícula or renovación fee
  row exists anywhere (only reposición Q150). (FR-003, FR-004, FR-005,
  FR-006)
- **AC-003:** Given a sociedad-nueva inscripción event, a dirección-type
  modificación and an empresa clausura, when cost exposure is assembled,
  then the rows read Q30+Q200(+Variable), Q30+Q100(+Q300 modificación de
  escritura) and Q30+Q100(+Q150) respectively — all marked recorded
  exposure, none invoiced or posted. (FR-007, FR-024)
- **AC-004:** Given an RM event in provisional state with its edicto
  published on a recorded date, when the lifecycle is evaluated, then
  the 60-day proof window and the 8-días-hábiles definitive window are
  surfaced as dated reminders, and a definitive resolution ingested
  later records effects retroactive to the provisional date without the
  system computing any legal effect. (FR-012, FR-022)
- **AC-005:** Given the inscripción-edicto template rendered from a
  sociedad's data, when the payload is generated, then it follows the
  observed grammar end-to-end — escritura → presentation →
  registro/folio/LIBRO ELECTRONICO 29/expediente → identity → objeto →
  plazo → capital autorizado/suscrito/pagado + acciones → órganos →
  date → "ULTIMA LINEA." — and carries the snapshot version
  (2026-08-19, edición 6022). (FR-014, FR-021)
- **AC-006:** Given any convocatoria record, when inspected, then it
  holds the event class, expediente, date and the art.-343 non-prejudice
  boilerplate ONLY — no convocatoria content asserted from 83_; and no
  configuration anywhere derives a cadence, volume or lag norm from the
  single edition. (FR-019, FR-023)
- **AC-007:** Given capital-autorizado values clustering just under
  Q500,000 in ingested snapshots, when the inference guard runs, then no
  threshold, validation, warning or default is produced — the pattern is
  stored as observed behavior with the R66 inference flag.
  (FR-020)
- **AC-008:** Given an ingested portal snapshot (edición + date), when
  matching runs, then tracked publication events transition to
  publicado with edition reference and URL, and the supersession watch
  flags — never clears — the 73_ fee rows pending re-verification.
  (FR-022, FR-023, FR-003)
- **AC-009:** Given the RM-side cancellation slots on an RM event, when
  the taxation recidivism sanction (GT-TAX-FR-216/217 by id) is
  consumed, then the inscripción/patente cancellation state records as
  an RM-side fact linked to the taxation row, and the RM multa track
  remains a separate, never-netted exposure. (FR-025; R62)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
this file owns GOQ-131 for the C3 rows, with GOQ-123 as kin on every 66_
citation family (owned by `01_books-anchor.md` GT-COA-FR-031 — the R64
verification note rides the arts. 341/343 procedural texts here).
GOQ-124 (retention/destruction matrix) is the Task 7 deliverable
(`../chart-of-accounts/03_retention-destruction-matrix.md`, forward ref —
file + cluster only). The 73_ no-date identity and the matrícula/variable
absences are handled by R66 flags (register rows), not new OQs — nothing
outside the register is treated as an open question.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-131 (owned): "RM publication SLA modeling from a single edition (6022): cadence, volumes, lag distributions unknowable; convocatoria entries = text-layer stubs (content model = payload)." FR-019 guards the stubs and FR-023 forbids norm assertion from one edition; any publication-cadence, volume or lag modeling requires more editions (acquisition queue), and convocatoria content requires a source with an extractable text layer. | no | GT synthesis wave S-GT5 (acquisition queue) | open |
| OQ-002 | GOQ-123 (kin): "CCom post-May-2006 reform watch: consolidation horizon D-11-2006; later reforms absent (known: art. 343 = D-18-2017) — verification note rides every 66_ citation." This file's arts. 333/335-343 procedural and data-model rows are the pre-D18-2017 print; FR-001/FR-012 carry the R64 note (current art. 343 mechanics = D-18-2017 art. 12 via 83_), and any further post-2006 reform of the RM title re-opens the affected FRs. | no | GT synthesis wave S-GT5 → W6 partner ask (owner: `01_books-anchor.md` FR-031; this file kin-cites) | open |
