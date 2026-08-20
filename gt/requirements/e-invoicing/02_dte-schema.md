# GT — E-Invoicing — DTE XML schema contract (GT_Documento & transaction family)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the Guatemala FEL XML
schema contract — the machine-readable *esquema* (schema) set both the Odoo
client and the SaaS core serialize against: the GT_Documento-0.2.1 envelope
(GTDocumento > SAT > DTE > DatosEmision + Certificacion) with its dual
`ds:Signature` slots; the emisor/receptor/items/totales field constraints;
the four coexisting version strings recorded as data (GOQ-15); the
21-file complement schema inventory including the Endoso family; the
AnulacionDocumento/ReversionDocumento transaction schemas (namespace
fel/0.1.0); the edge validations carried by the schema itself (NIT/ID
patterns, per-item Impuesto cap, closed currency enum); the
publication-channel authority rule for the XSD set (GitHub 961133c working
authority; MediosdePago → cat.desa per R2; drift recorded, never silently
resolved); and the adenda exclusion rule (DTE-external, unsigned, never to
SAT).

It does **not** cover: the DTE-type taxonomy and the `DatosGenerales/@Tipo`
enumeration drift (01_document-types.md, GT-EINV-FR-001..004), the
validation-rule behavior keyed on schema fields — emission windows, receptor
canonicalization, totals arithmetic, the Reglas §3.1 14×26 complemento
applicability matrix (03_validation-rules.md §complemento matrix), catalog
data governance and sidecars ([../catalogs/01_governance.md](../catalogs/01_governance.md),
GT-CAT FRs), the certificador interface, mini-RTU feed and the establishment
model detail (05_certificador-interface.md §establishment, D-GT9),
anulación/contingencia behavior and windows (06_anulacion-contingencia.md),
or graphic representation (07_display-representation.md). Those files
reference this one for the schema contract.

## 2. Legal Basis

Authority order (binding, per master evidence index): XSD/JSON working
authority = GitHub 961133c (ratified-official, OQ1 ruling 2026-08-18)
EXCEPT `GT_Complemento_MediosdePago-0.1.0.xsd` → cat.desa (R2); all drift
recorded, never silently resolved (GOQ-02 umbrella). The 16_ Documento
Técnico v1.2 is cited ONLY for provider-boundary semantics (XSD-compliance
duty, signature scopes, adenda exclusion) — never for current schema
structure: its §II.A inventory references -0.1.0 filenames and only 4
complements against the live 25-XSD set (R11). Rulings that bind this
file: R2 (MediosdePago channel override), R6 (frases pairing 12/88), R11
(16_ vintage), R12 (emisión signature scope = DatosEmision).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | GT_Documento-0.2.1.xsd: `<xs:schema … xmlns:dte="http://www.sat.gob.gt/dte/fel/0.2.0" … targetNamespace="http://www.sat.gob.gt/dte/fel/0.2.0" elementFormDefault="qualified" version="2.0">`; raíz `GTDocumento` > `SAT` > `DTE` doc `"Agrupa la estructura para un DTE. Fecha de inicio de aplicacion: 2019-03-01"`; `GTDocumento` `@Version type="xs:decimal" use="required" fixed="0.1"`; `SAT@ClaseDocumento` enumeración `"dte"`; `<xs:element ref="ds:Signature" id="FirmaEmisor"/>` + `<xs:element ref="ds:Signature" id="FirmaCertificador" minOccurs="0"/>`; import `"http://www.w3.org/TR/2002/REC-xmldsig-core-20020212/xmldsig-core-schema.xsd"` | Main DTE schema: envelope chain, four coexisting version identifiers (filename 0.2.1 / NS fel/0.2.0 / schema@version 2.0 / GTDocumento@Version 0.1), two xmldsig Signature slots (emitter required, certificador optional), W3C xmldsig import; structure in force since 2019-03-01 | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 2–19, 810 | root chain + version soup (EVID-001) |
| LB-002 | GT_Documento-0.2.1.xsd, Emisor: `NITEmisor` tipo `dte:tipoNITDelEFACE` doc `"Indica el NIT del Emisor del DTE (sin guión)."`; `NombreEmisor` (1..400); `CodigoEstablecimiento` doc `"Número del establecimiento donde se emite el documento. Es el que aparece asignado por SAT en sus registros."` restricción `xs:positiveInteger`, `minInclusive 1`, `maxInclusive 9999`; `NombreComercial` (1..255); `AfiliacionIVA` enums GH `"GEN" "EXE" "PEQ" "ECA" "EXI" "PRI" "PEC" "OMI" "IDP"` (con `"PEE" "AGR" "AGE"` comentados, activos en CD) doc `"(EXE queda por compatibilidad para DTE hasta 29/feb/2020)"`; GH agrega `AfiliacionOmiso` (GEN/PEQ) y `ClasificacionEmisor` enumeración `1674` | Emisor block: NIT (classic format only), name, SAT-assigned establishment code 1–9999, commercial name, IVA-regime enum (9 GH-active; EXE compatibility anchor 29/feb/2020); GH-only omiso/classification additions | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 154–258 (idéntico en CD salvo enums comentados) | Emisor block (EVID-003) |
| LB-003 | GT_Documento-0.2.1.xsd, DatosGenerales: `NumeroAcceso` doc `"Es un número generado por el Emisor en caso de contingencia, que va desde 100000000 hasta 999999999"`; `Dispositivo` doc `"Campo de uso para identificar del dispositivo donde se realizó. Uso exclusivo para aplicación de SAT AV y SAT móvil (App) "` enums `"APP" "AV" "APPVOZ"`; `EmisionUbicacionTemporal` enumeración `"SI"`; Certificacion/NumeroAutorizacion `@Serie` doc `"Se forma con los primeros 8 dígitos hexadecimales del UUID, de izquierda a derecha…"` y `@Numero` doc `"Se forma con el equivalente en números decimales de los dígitos hexadecimales del UUID, a partir de la posición 9 hasta la posición 16…"` | DatosGenerales emission fields: 9-digit contingencia access number; dispositivo enum reserved for SAT's own apps (not a taxpayer point-of-emission code); temporary-location flag; Serie/Numero derived from the certificador UUID post-certificación | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 117–151, 741–775 | NumeroAcceso/Dispositivo + Serie/Numero derivation (EVID-004) |
| LB-004 | GT_Documento-0.2.1.xsd, Receptor: `IDReceptor` doc `"Indica el NIT o CUI del RECEPTOR, CF."`; `TipoEspecial` doc `"Cuando la casilla está llena debe contener el valor “CUI”…"` enums `"CUI" "EXT"`; `NombreReceptor` (1..400) doc `"Si la casilla “IDReceptor” contiene un NIT valido el nombre indicado debe corresponder a los registros tributarios. Caso contrario el contenido puede ser cualquiera que solicite el RECEPTOR."`; GH cambia `DireccionReceptor` a `tipoDireccionReceptor` (Direccion 1..200 requerida; CodigoPostal/Municipio/Departamento/Pais todos opcionales); `DestinodelaVenta` (GH) union Primario/Pecuario/Condición | Receptor block: polymorphic ID (NIT/CUI/CF/foreign) + TipoEspecial discriminator; name must match SAT registry when the ID is a valid NIT; GH relaxes the receiver address to street-only; destination-of-sale union for the primario/pecuario regimes | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 260–327 + tipoDireccionReceptor lines 914–966 (GH) | Receptor block (EVID-005; union EVID-014) |
| LB-005 | GT_Documento-0.2.1.xsd, tipos: `tipoNITReceptor` patrón GH `"((([1-9])+([0-9])*([0-9]|K))|(([1-9]+[0-9]){12,13})|(CF)|^([A-Z0-9&amp;%-/#=]{3,18}))$"` vs CD `…^([A-Z0-9]{3,18}))$"` [sic: `^` a mitad de alternativa en ambos]; `tipoNITDelEFACE` (emisor) patrón `"(([1-9])+([0-9])*([0-9]|K))$"` maxLength 13; `NITCertificador` patrón `"([1-9])+([0-9])*([0-9]|K)"`; GH-new `tipoNITTransportista` (sin alternativa CF) | NIT/ID validation patterns: four receiver alternatives (classic NIT ending digit/K; 12–13 digit CUI; literal CF; 3–18 char foreign token with GH-widened charset `[A-Z0-9&%-/#=]`, fuente `&amp;` = `&` literal); emitter/certificador NITs classic-format only; mid-alternative `^(` recorded verbatim | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 839–860, 716–727 + CD (diff hunk 741c843) | NIT patterns (EVID-006) |
| LB-006 | GT_Documento-0.2.1.xsd, Frases/Frase `maxOccurs="100"` doc `"En esta sección deberá indicarse los regímenes y textos especiales que son requeridos en los DTE, de acuerdo a la afiliación del contribuyente y tipo de operación."`; `TipoFrase` `xs:positiveInteger` minInclusive 1 maxInclusive 12 (GH) / 9 (CD); `CodigoEscenario` 1..99; `NumeroResolucion` (4..50)?; `FechaResolucion` (`xs:date`)? | Frases container: up to 100 (TipoFrase, CodigoEscenario) reference pairs into CatalogoFrases, with optional resolution number/date when the escenario flags demand them; TipoFrase domain differs per channel (R6 pairing) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 328–391 + CD (diff hunk 274c350) | Frases container (EVID-007) |
| LB-007 | GT_Documento-0.2.1.xsd, Items: `Item maxOccurs="9999"` @`NumeroLinea` 1..9999 @`BienOServicio` enums `"B" "S"`; `CodigoProducto` (GH, doc `" Según el Decreto número 15-2021 se establece un subsidio al gas propano con base al peso en libras de cada cilindro"`); `UnidadMedida` (1..3)? doc `"...puede utilizar la nomenclatura definida por la Intendencia de Aduanas de la SAT en su tabla SAT-IA-008."`; `Descripcion` 1..10000; `Precio` doc `"PrecioUnitario multiplicado por CantidadItem."`; `Impuestos/Impuesto` maxOccurs="2" (GH) / "20" (CD): `NombreCorto` (TipoImpuesto), `CodigoUnidadGravable` totalDigits 7, `MontoGravable`?, `CantidadUnidadesGravables`?, `MontoImpuesto`; GH agrega `Afecto` (Si/No) y `Idp`; `ComplementosItem/ComplementoItem` con `xs:any` + `NombreComplementoItem`/`URIComplementoItem` requeridos | Items block: line field set and caps; per-item tax structure with the GH 2-tax cap vs CD 20 (GOQ-20); GH-only IDP fields; item-level complement wrapper | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 392–625 | Items block (EVID-008) |
| LB-008 | GT_Documento-0.2.1.xsd, Totales/Complementos: `TotalImpuestos/TotalImpuesto maxOccurs="20"` @`NombreCorto` @`TotalMontoImpuesto` doc `"Sumatoria de MontoImpuesto de cada uno de los ítems con el mismo impuesto…"`; `GranTotal` doc `"Sumatoria de los elementos Total de cada uno de los ítems del DTE."`; `Complementos/Complemento` (secuencia, maxOccurs unbounded) con `xs:any` + `IDComplemento`? + `NombreComplemento` y `URIComplemento` requeridos (doc `"Indica el URI del XSD del complemento."`) | Totales (tax-total groups capped 20, GranTotal) and the document-level Complementos wrapper: any-namespaced XML plug-in mechanism identified by complement name + XSD URI | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 627–705 | Totales + Complementos wrappers (EVID-009) |
| LB-009 | GT_Documento-0.2.1.xsd, Certificación: `NITCertificador` (patrón LB-005); `NombreCertificador` 1..400; `NumeroAutorizacion` base `dte:tipoUUID` = `xs:token` patrón `"[0-9A-F]{8}-([0-9A-F]{4}-){3}[0-9A-F]{12}"` con @Serie/@Numero (LB-003); `FechaHoraCertificacion` `xs:dateTime` patrón `"((\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(.(\d{3}))?(-06:00)?)"`; DatosGenerales@FechaHoraEmision doc `"Formato aaaa-mm-ddThh:mm:ss.000-06:00 (Milisegundos opcionales, zona horaria especificada o interpretada como hora de Guatemala.)"` | Certification block (produced by the certificador): identity, uppercase UUID authorization number, timestamp pattern with optional Guatemala -06:00 offset; emission timestamp documented as Guatemala time | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 710–788, 833–837 | Certificación + UUID/dateTime types (EVID-010) |
| LB-010 | GT_Documento-0.2.1.xsd, tipos auxiliares: `TipoImpuesto` enums `"IVA" "PETROLEO" "TURISMO HOSPEDAJE" "TURISMO PASAJES" "TIMBRE DE PRENSA" "BOMBEROS" "TASA MUNICIPAL" "BEBIDAS ALCOHOLICAS" "TABACO" "CEMENTO" "BEBIDAS NO ALCOHOLICAS" "TARIFA PORTUARIA"`; `CodigoProducto` enums GH `"GALDIESEL" "GALSUPER" "GALREGULAR"` vs CD `"CGP10LBS"… "GALDIESEL"`; `tipoMoneda` doc `"ISO 4217"`, 28 enums + GH-new `<xs:enumeration value="PLN"/> <!-- esloti Polaco - Requerimiento 06052026 -->` [sic "esloti"] | Auxiliary types: the 12 tax short names joining lines/totales to the unidades gravables catalog; fuel product enum differs per channel; closed 28-currency list with PLN added per an internal SAT tracker id (GOQ-22) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 1120–1155, 1458–1480 + CD (diff hunk 1159,1164c1476) | TipoImpuesto/CodigoProducto/tipoMoneda (EVID-011) |
| LB-011 | GT_Documento-0.2.1.xsd, tipos base: `TipoCorreoElectronico` patrón `"((\w[-+._\w]+@\w[-.\w]+\.\w[-.\w]+)(;?))*"` (acepta listas separadas por punto y coma; anotación `"Validador de correos electronicos DISCUTIR…"` [sic]); `NumeroNDecimales` doc `"Acepta cantidades mayores a 0"` [sic: permite 0] = `xs:decimal` minInclusive 0, fractionDigits 10, totalDigits 22; `tipoCodigoPais` ~240 enums doc `"Código de País ISO 3166-1"` con entradas legadas (p.ej. "AN") | Base types: semicolon-separated e-mail lists; non-negative decimals up to 22 total / 10 fractional digits; mostly-ISO country enum with legacy entries | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 1164–1457 | Country/e-mail/decimal types (EVID-012) |
| LB-012 | GT_Documento-0.2.1.xsd, bloque IDP (GH únicamente, dentro de marcadores `<!-- IDP -->`): `DatosGenerales/Idp` tipo `datosGeneralesIDPType` doc `"Agrupa los datos para emitir la boleta de despacho IDP."` con atributos requeridos `Litoral` ("Norte"/"Sur"/"Central"), `Placa` (≤10), `Numerodeviaje` (1..50), `Direcciondeentrega` (1..500), `Origendespacho`, `Destinodespacho`, `Procedencia` + elementos `Terminal`/`Transportista` | IDP (petroleum-distribution) annex block powering the BIDP boleta de despacho — exists only on the GH channel | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 31–35, 542–557, 967–1119 | IDP block (EVID-013) |
| LB-013 | GT_AnulacionDocumento-0.1.0.xsd: `targetNamespace="http://www.sat.gob.gt/dte/fel/0.1.0"` `version="0.1.0"`; raíz `GTAnulacionDocumento` > SAT > `AnulacionDTE` > `DatosGenerales@ID fixed="DatosAnulacion"` con atributos requeridos `NumeroDocumentoAAnular` (tipoUUID), `NITEmisor` (tipoNITDelEFACE), `IDReceptor` (doc `"Indica el NIT, CUI o Identificacion Extranjera del RECEPTOR, CF."`), `FechaEmisionDocumentoAnular` (dateTime), `FechaHoraAnulacion` (dateTime), `MotivoAnulacion` (1..255); `Certificacion` opcional; `GTAnulacionDocumento@Version fixed="0.1"`; mismos dos slots ds:Signature; comentario de cabecera `<!-- editado con XMLSpy … por Eduardo Guillen (personal) -->` | Anulación transaction schema (NS fel/0.1.0): identifies the target by UUID + emitter NIT + receiver ID + original timestamp + reason (1–255); optional certification block; double signature slots; XMLSpy editorial header recorded as provenance quirk | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_AnulacionDocumento-0.1.0.xsd` (211 líneas; CD difiere en una línea — patrón tipoNITReceptor, diff hunk 173) | AnulacionDocumento structure (EVID-015) |
| LB-014 | GT_ReversionDocumento-0.1.0.xsd: raíz `GTReversionDocumento` > SAT > `ReversionDTE`; anotación `"Transacción de anulación de un Documento Tributario Electrónico del Régimen FEL."` [sic copy-paste — es la reversión]; atributos requeridos `NumeroDocumentoAReversar` (tipoUUID), `Serie` + `Numero` (derivados del UUID), `NITEmisor`, `IDReceptor`, `FechaEmisionDocumentoReversar`, `FechaHoraReversion`, `MotivoReversion` (1..255), `UsuarioSolicitud` (1..100, doc `"Indica el nombre del usuario que registra la transaccion."`) | Reversion transaction schema (undoes an anulación): UUID plus its Serie/Numero decomposition and a named requesting user; byte-identical on both channels | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_ReversionDocumento-0.1.0.xsd` lines 1–289 (idéntico en CD) | ReversionDocumento structure (EVID-016) |
| LB-015 | GT_Complemento_Cambiaria-0.1.0.xsd: NS `http://www.sat.gob.gt/dte/fel/CompCambiaria/0.1.0`; `AbonosFacturaCambiaria` doc `"Definición Global de abonos de factura cambiaria"`; `Abono maxOccurs="unbounded"`: `NumeroAbono` (`xs:int` totalDigits 3), `FechaVencimiento` (`xs:date`, requerido), `MontoAbono` (NonNegativeFloat); `@Version` fixed `"1"` | Cambiaria complement: unbounded installment rows (number, due date, amount) for the FCAM-family credit invoices | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Complemento_Cambiaria-0.1.0.xsd` (idéntico en CD) | Abonos structure (EVID-017) |
| LB-016 | GT_Complemento_Referencia_Nota-0.1.0.xsd: `RegimenAntiguo` enumeración `"Antiguo"` doc `"Debe incluirse solamente cuando el documento original corresponde al regimen de papel o FACE1."`; `NumeroAutorizacionDocumentoOrigen` (requerido) patrón UUID-o-papel `"[0-9A-F]{8}-([0-9A-F]{4}-){3}[0-9A-F]{12}|([1-2]{1}[0-9]{3}-[1-9]{1}[0-9]{0,2}-[1-9]{1}[0-9]{0,6}-[1-9]{1}[0-9]{0,6})|([0-9]{4}-[0-9]{1}-[0-9]{1,6}-[0-9]{1,6})"`; `FechaEmisionDocumentoOrigen` doc `"Se utiliza para verificar que pasados los 2 meses una Nota de Crédito no incluya el IVA."`; `MotivoAjuste` 1..200. ReferenciaConstancia: variante de patrón + `MontoIVAExento` doc `"El monto total del IVA que ampara el documento, cuando el complemento corresponde a una Constancia de Exención del IVA (CIVA). Dicho monto debe ser igual al total de IVA del DTE al que hace referencia."`. ReferenciaBoletaDespacho (GH): doc `"Agrupa la informacion del documento original BIDP al cual hace referencia esta factura."` | Reference complements: NC/ND origin (FEL UUID or legacy paper/FACE1 authorization numbers; the 2-month NC IVA rule embedded in schema documentation), CIVA/CAIS constancia origin (echoes the origin's total IVA), BIDP origin (GH-only) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Complemento_Referencia_Nota-0.1.0.xsd` + `GT_Complemento_ReferenciaConstancia-0.1.0.xsd` (idénticos en CD); `GT_Complemento_ReferenciaBoletaDespacho-0.1.0.xsd` (GH únicamente) | Reference complements (EVID-018) |
| LB-017 | GT_Complemento_Exportaciones-0.1.0.xsd (GH, copia rica): `Nombre/DireccionConsignatarioODestinatario` 1..300 (CD 1..70); bloque comprador dentro de comentarios `"<!-- Campos agregados de ultimo -->"`; `INCOTERM` type INCOTERMType = `"EXW" "FCA" "FAS" "FOB" "CFR" "CIF" "CPT" "CIP" "DDP" "DAP" "DAT" "DPU" "ZZZ"` doc `"Catálogo Edifact"` [sic: DAT y DPU coexisten]; `fechaExportacion`? patrón `"\d{2}[/]\d{2}[/]\d{4}"` [sic nombre minúsculo]; `viaTransporte`? enums `"Aérea" "Marítima" "Terrestre"`; `aduanaSalida`?. GT_Complemento_ExportacionProvisional-0.1.0.xsd: CD `<xs:element name="OtraSReferencia"…>` vs GH `name="OtraReferencia"` (renombral de un token) | Export complements: GH extends consignee/buyer blocks, INCOTERM enum (mixed Incoterms vintage), export date (dd/mm/yyyy string), transport mode, exit customs; provisional-export drift = one element rename OtraSReferencia→OtraReferencia | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Complemento_Exportaciones-0.1.0.xsd` (209 líneas; CD = variante 5,359 B); diff 29_ vs 30_ `GT_Complemento_ExportacionProvisional-0.1.0.xsd` línea 25 | Exportaciones + ExportacionProvisional (EVID-019, EVID-020) |
| LB-018 | GT_Complemento_MediosdePago-0.1.0.xsd — CD: `MediosDePago` doc `"El presente complemento, debe incluirse únicamente en los documentos del tipo: Factura, Factura Cambiaria, Factura de Pequeño Contribuyente y Factura Cambiaria de Pequeño Contribuyente."`; `TipoFormaPago` type `cmdp:TipoFormaPagoLista` doc `"…Medio de Pago Sigla: * Tarjeta de Crédito - TC, * Tarjeta de Débito - TD, * Efectivo - EF, * Cheque - CH."` enums `"TC" "TD" "EF" "CH"`; `NumeroTransaccion`? ≤36, `FechaTransaccion`?, `Monto`?. GH: sobrescritura TurismoPasaje — `TipoFormaPago` cadena libre ≤13 con doc `"Nit del receptor del DTE."` [doc erróneo]; `@Version type="ctup:VersionType"` con prefijo `ctup` **no declarado** en el esquema (no compilable tal como publicado) | Payment-means complement: the cat.desa copy is coherent (TC/TD/EF/CH enum, optional transaction number/date/amount); the GitHub copy is a defective TurismoPasaje overwrite with an undeclared prefix — R2 working rule: model from cat.desa | `gt/sources/30_FEL_XSD_cat_catdesa/GT_Complemento_MediosdePago-0.1.0.xsd` (autoridad) vs `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Complemento_MediosdePago-0.1.0.xsd` (defectuoso) | MediosdePago + R2 (EVID-021) |
| LB-019 | Complementos idénticos en ambos canales: PartidosPoliticos (LEPP) doc `"El presente complemento, debe incluirse únicamente en los documentos del tipo: Recibo por donación y Recibo"` attrs `CalidadAportante` ("Afiliado"/"Simpatizante"), `TipoAporte` ("Dineraria"/"No dineraria o en especie"), `DeclaracionProcedencia` ≤500, `Aporte`; Fac_Especial `RetencionesFacturaEspecial`: `RetencionISR`, `RetencionIVA`?, `TotalMenosRetenciones`; Espectaculos (`CodigoEvento`/`NombreEvento`/`NombreLocalidad`/`PrecioAdmision`/`NumeroBoleto`); TurismoPasaje doc `"Aplica para los DTE que incluyen exención de IVA e Impuesto de Turismo Pasajes derivado del Decreto 31-2022."`; CobroXCuentaAjena `ItemCuentaAjena` repetible (DAI = `"Derechos Arancelarios a la Importación"`) | Miscellaneous complements: political-party donations (LEPP), special-invoice retentions (Fac_Especial), event ticketing, tourism-passage exemption (Decree 31-2022), third-party collection | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Complemento_PartidosPoliticos-0.1.0.xsd` (drift cosmético), `GT_Complemento_Fac_Especial-0.1.0.xsd`, `GT_Complemento_Espectaculos-0.1.0.xsd`, `GT_Complemento_TurismoPasaje-0.1.0.xsd`, `GT_Complemento_CobroXCuentaAjena-0.1.0.xsd` | LEPP + Fac_Especial (EVID-022, EVID-023); Espectaculos/Turismo/Cobro (EVID-024) |
| LB-020 | GT_Complemento_RetencionesFacturaEspecifica.xsd (GH): doc `"…deben incluirse únicamente en los documentos del tipo: Factura Específica."`, elementos `RetencionICT`? doc `"Monto de retención de ICT."`, `TotalMenosRetenciones`? | FEPE retention complement (GH-only): ICT retention + net total — "ICT" expansion unprinted (GOQ-24 kin, Task 4 file) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Complemento_RetencionesFacturaEspecifica.xsd` | RetencionesFacturaEspecifica (EVID-023) |
| LB-021 | Complementos sectoriales GH-only: ComplementoAlItem @`CodArancelario` doc `"Codificación del listado provisto por la SAT"` (@`NoItem` totalDigits 999999 [sic defecto]); DetalleProductos `ItemDetalleProductos` (`CodigoUnidadGravable` doc `"para bebidas alcoholicas"`, `ClaseDeBebida`, `CapacidadEnvase`, `PrecioVentaSugerido`…); TrasladoMercancias doc `"…Aplica para los documentos electrónicos no tributarios Notas de Envío."` attrs requeridos IDTransportista/TipoDocumentoIdentificacion/NombreTransportista/Placa/DireccionProcedencia/NITCUIConsignatario/NombreConsignatario/DireccionDestino/Motivo; GasLicuadoPetroleo per-item `PesoTara/PesoBruto/PesoNeto/…/CantidadGalones60F/Duca`; AlmacenajeGalonaje per-item `Compartimiento/CapacidadGalones/…` | GH-only sector complements: item tariff code, alcoholic-beverage excise detail, NEV waybill data, GLP/fuel-terminal measurements (IDP ecosystem) — capability exists only on the GH channel | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_ComplementoAlItem.xsd`, `GT_ComplementoDetalleProductos-0.1.0.xsd`, `GT_ComplementoTrasladoMercancias-0.1.0.xsd`, `GT_Complemento_GasLicuadoPetroleo.xsd`, `GT_Complemento_AlmacenajeGalonaje-0.1.0.xsd` (ninguno en cat.desa) | GH-only sector set (EVID-025) |
| LB-022 | GT_Endoso-0.1.0.xsd (GH): `targetNamespace="http://www.sat.gob.gt/dte/fel/0.2.0"`, raíz `GTEndoso` doc `"Definición Global de Endoso de Factura Cambiaria para Guatemala"`; `Contrato`? @`TipoContrato` doc `"Únicamente puede ser Factoraje o Descuento"`; `Cedente`/`Cesionario`; `DatosDTEReferencia` @`TipoDTE` doc `"Únicamente puede ser uno de los cuatro tipos de Factura Cambiaria"` enums `"FCAM" "FCAP" "FCPC" "FCRP"`; evento `"CreacionEndoso"`; GT_AnulacionEndoso doc `"Definición Global de Anulación de Endoso…"`, GT_PagoEndoso doc `"…confirmación de Pago de un Endoso…"` | Endoso (endorsement/factoring) transaction family, GH-only, NS fel/0.2.0: create/annul/pay lifecycle over the four endorsable cambiaria types (Factoraje or Descuento) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Endoso-0.1.0.xsd`, `GT_AnulacionEndoso-0.1.0.xsd`, `GT_PagoEndoso-0.1.0.xsd` (ausentes en cat.desa) | Endoso family (EVID-026) |
| LB-023 | Inventario de versiones/fechas: NS de transacción DTE+Endoso `http://www.sat.gob.gt/dte/fel/0.2.0`; Anulacion/Reversion `…/dte/fel/0.1.0`; complementos `http://www.sat.gob.gt/face2/<Name>/0.1.0` (con desajustes registrados [sic]: NS "ComplementoPartidosPolitico", "ComplementoAlmacenamientoGalonaje" vs archivo "AlmacenajeGalonaje", "ComplementoDetalleDeProductos" vs archivo "DetalleProductos"); xs:schema@version: GT_Documento `2.0`, Anulacion/Reversion `0.1.0`; @Version de documento fijo `"0.1"`; complementos `@Version fixed "1"` o xs:decimal libre; anclas fechadas: DTE `"Fecha de inicio de aplicacion: 2019-03-01"`, EXE `"hasta 29/feb/2020"`, `<!-- esloti Polaco - Requerimiento 06052026 -->`; matriz de deriva: 17 archivos compartidos (9 idénticos, 8 difieren), 11 GH-only, 1 CD-only | Version/date metadata inventory across the whole set (transaction-family namespaces, per-file version attributes, dated anchors) plus the md5-level channel drift matrix — the provenance substrate for D-GT10 dated rows | `gt/sources/29_FEL_XSD_cat_github_961133c/` + `gt/sources/30_FEL_XSD_cat_catdesa/` (inventario completo, ambos canales) | Version/date metadata + drift matrix (EVID-030) |
| LB-024 | 16_ Documento Técnico v1.2, §II.A: `"La observancia del cumplimiento del XSD aplica para la emisión, certificación y recepción de los DTE. Para este efecto el emisor, certificador, receptor y la SAT tienen disponible los archivos XSD oficiales"` — tabla con `"GT_documento.xsd"` [sic] y 4 complementos, URLs `https://cat.desa.sat.gob.gt/xsd/alfa/` con nombres `-0.1.0` | Provider-boundary semantics: XSD conformance binds emisión, certificación AND recepción; the doc's own inventory is stale (-0.1.0 filenames, 4 complements vs the live 25-XSD set) — R11: cite 29_/30_ for current structure, 16_ only for these semantics | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | §II.A p. 7 (EVID-150; R11) |
| LB-025 | 16_ §II.C: `"En el nodo Signature, el EMISOR incorporará un nodo conteniendo la firma de emisión, la cual se realiza sobre el elemento DatosEmision"`; §II.F/G: `"El certificador agrega un segundo elemento Signature, el cual firma los datos del nodo DTE. Ambas firmas deben ser válidas para que el DTE sea válido."`; §II.G `"La firma electrónica de emisión se aplica sobre el nodo de DTE, SAT debe validarla…"` [sic — leído como errata de firma de certificación, R12]; §II.I: ambas `"empleando las extensiones Xades-Bes y firmas tipo RSA con algoritmo SHA-256"` con IDs distintos | Signature contract: emisión signs DatosEmision (R12 — the §II.G variant is a typo for the certificación signature, which covers the DTE node); both signatures XAdES-BES / RSA / SHA-256 with distinct Signature IDs | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | §II.C pp. 8–9, §II.F–G pp. 10–11, §II.I p. 13 (EVID-152, EVID-153, EVID-154; R12) |
| LB-026 | 16_ §II.D/E: `"Los complementos deben incorporse conforme con las disposiciones del Régimen FEL y forman parte de los nodos firmados por el EMISOR."` [sic "incorporse"] `"Cuando existan, los complementos deben ser enviado a la SAT, la SAT verificará y puede rechazar o informar error si un complemento requerido no es enviado."` [sic]; `"El elemento Adenda no forma parte de los elementos DatosEmision ni DTE, motivo por el cual no se encuentra firmado por el EMISOR ni por el RECEPTOR y no altera la validez de un DTE."` `"El elemento Adenda no debe ser enviado a la SAT, si un DTE es enviado a la SAT conteniendo el elemento Adenda la SAT rechazará el mismo y deberá enviarse de nuevo sin el mismo."` | Complementos ride inside the signed DatosEmision area and are mandatory when required (SAT rejects/errors when a required complement is missing); Adenda is DTE-external, unsigned, and must never reach SAT (rejection if present) | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | §II.B/D/E pp. 8–9 (EVID-151) |
| LB-027 | Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025), §3.1 catálogo de complementos (filas 1–14, p.ej. `"2 Retenciones de factura especial: 2 [Requerido] for FESP"`, `"14 Retenciones de factura especifica: 2 [Requerido] for FEPE"`, `"3 Abonos de factura cambiaria: 2 for FCAM/FCCA/FCPE/FCAE/FCRP/FCPC"`) | Complement applicability catalog: the 14 × 26 complemento matrix (0/1/2 semantics) — the only printed source of canonical complement names; URIs not captured anywhere (GOQ-21); applicability numbers owned by the Task 4 file | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §3.1 pp. 97–98 (EVID-139) |

## 3. Functional Requirements

### 3.1 Envelope, version strings, signatures

- **GT-EINV-FR-042:** The DTE XML envelope shall follow the
  working-authority GT_Documento structure exactly:
  `GTDocumento@Version="0.1"` > `SAT@ClaseDocumento="dte"` > `DTE` >
  `DatosEmision` (the emitter-side payload) with `Certificacion` optional
  (filled by the certificador), `elementFormDefault="qualified"`, and the
  `DatosGenerales/@Tipo` value drawn from the taxonomy registry of
  01_document-types.md (GT-EINV-FR-001..004). The DTE structure dates from
  its printed *inicio de aplicación* 2019-03-01, recorded as a dated
  anchor. (LB-001; EVID-001)
- **GT-EINV-FR-043:** The four coexisting version strings shall be recorded
  as data, never reconciled: filename `GT_Documento-0.2.1`,
  targetNamespace `fel/0.2.0`, `xs:schema@version 2.0`, `GTDocumento@Version
  fixed "0.1"`. Serialization shall reproduce the working-authority copy's
  values (NS fel/0.2.0; GTDocumento@Version "0.1"); validation logic shall
  key on document content, never on a single version string. Which string
  production validation keys on is open → OQ-001 (GOQ-15).
  (LB-001; LB-023; EVID-001, EVID-030)
- **GT-EINV-FR-044:** The envelope shall carry two `ds:Signature` slots per
  the XSD ids: `FirmaEmisor` (required, emitter) and `FirmaCertificador`
  (optional, certificador). The emisión signature covers `DatosEmision`
  only and the certificación signature covers the whole `DTE` node — both
  valid being a condition of DTE validity (R12: the 16_ §II.G "sobre el
  nodo de DTE" wording applied to the firma de *emisión* is a typo for the
  firma de certificación) — and both use XAdES-BES, RSA, SHA-256 with
  distinct Signature IDs. The xmldsig import resolves to a W3C network
  URL: the shipped local `xmldsig-core-schema.xsd` shall be used so
  validation never depends on a network fetch. (LB-001; LB-025; EVID-001,
  EVID-152, EVID-153, EVID-154; R12)
- **GT-EINV-FR-045:** The `Certificacion` block is certificador-produced
  data the system ingests, never generates: NITCertificador
  (classic-NIT format), NombreCertificador, NumeroAutorizacion (uppercase
  UUID v4 pattern) with Serie/Numero derived from that UUID (first-8-hex /
  hex-positions-9..16 decimal), and FechaHoraCertificacion in the
  Guatemala (-06:00) dateTime pattern; the emitter-side FechaHoraEmision
  shall serialize per the same ISO pattern with Guatemala-time semantics.
  (LB-003; LB-009; EVID-004, EVID-010)

### 3.2 Parties & DatosGenerales

- **GT-EINV-FR-046:** The Emisor block shall carry: NITEmisor in classic
  NIT format only (no CF/foreign), NombreEmisor (1..400),
  CodigoEstablecimiento (`xs:positiveInteger` 1–9999, "el que aparece
  asignado por SAT en sus registros"), NombreComercial (1..255), the strict
  tipoDireccion address, CorreoEmisor, and AfiliacionIVA drawn from the
  GH-active enum set (GEN, EXE, PEQ, ECA, EXI, PRI, PEC, OMI, IDP — with
  PEE/AGR/AGE recorded as CD-active/GH-commented drift); the EXE
  compatibility note ("hasta 29/feb/2020") is a dated anchor, and the
  GH-only AfiliacionOmiso/ClasificacionEmisor additions are recorded as
  channel data. Establishment identity in the DTE is CodigoEstablecimiento
  + NombreComercial ONLY — the establishment model detail (sucursal
  mapping, RTU validation, mini-RTU feed) lives in
  05_certificador-interface.md §establishment (D-GT9) and is not
  duplicated here. (LB-002; LB-023; EVID-003, EVID-030; GOQ-02 umbrella
  for the enum drift)
- **GT-EINV-FR-047:** The Receptor block shall carry: IDReceptor validating
  against tipoNITReceptor (FR-054), the TipoEspecial discriminator ("CUI"
  or "EXT") when the ID is not a NIT, NombreReceptor (1..400 — must
  correspond to the tax registry when the ID is a valid NIT, free
  otherwise), the GH-relaxed address (street required, remaining fields
  optional), and — for the Primario/Pecuario regime types —
  DestinodelaVenta from the closed union enum (the duplicated
  "Comercializador" enum value recorded [sic]). (LB-004; EVID-005,
  EVID-014)
- **GT-EINV-FR-048:** DatosGenerales emission fields shall follow:
  NumeroAcceso only for contingencia documents (9 digits, range
  100000000–999999999); Dispositivo reserved for SAT's own apps
  (APP/AV/APPVOZ) and never populated by taxpayer flows — taxpayers have no
  punto-de-emisión/dispositivo field (whether TotalDoc accepts an
  adenda-side dispositivo is GOQ-17, owned by the E7/05 file);
  EmisionUbicacionTemporal="SI" marking temporary-location emission; the
  optional Servicio="Residencial" field. (LB-003; EVID-004)

### 3.3 Items, taxes, totals, currency

- **GT-EINV-FR-049:** Each Item (max 9999 per DTE) shall carry NumeroLinea
  (1..9999), BienOServicio ("B"/"S"), Cantidad, UnidadMedida (optional
  1–3 chars, SAT-IA-008 nomenclature recommended), Descripcion
  (1..10000), PrecioUnitario with Precio = PrecioUnitario × Cantidad, and
  Descuento/OtrosDescuento; all amounts serialize as non-negative decimals
  with ≤ 10 fractional digits and ≤ 22 total digits; e-mail fields accept
  semicolon-separated lists; country codes come from the closed ~240-enum
  list. (LB-007; LB-011; EVID-008, EVID-012)
- **GT-EINV-FR-050:** Each per-item Impuesto shall carry NombreCorto (one
  of the 12 TipoImpuesto names), CodigoUnidadGravable (the catalog join
  key), the base/units fields per the ad-valorem vs per-unit formula rule
  ([../catalogs/01_governance.md](../catalogs/01_governance.md)
  GT-CAT-FR-011), and MontoImpuesto. The GH schema caps Impuesto at
  maxOccurs 2 per item while CD allows 20; per the conservative working
  rule the system shall emit at most 2 taxes per line (splitting the line
  when a scenario genuinely needs more) until the production behavior for
  real multi-tax lines is answered → OQ-003 (GOQ-20). IVA lines never
  carry CantidadUnidadesGravables (FEL_SEC502 anchor; enforcement detail
  owned by 03_validation-rules.md). (LB-007; LB-010; EVID-008, EVID-011,
  EVID-029)
- **GT-EINV-FR-051:** The GH-only IDP/fuel extensions shall be treated as
  channel-dependent capability: the DatosGenerales/Idp annex block, the
  item-level Afecto (Si/No) + Idp fields, and the CodigoProducto closed
  enum — whose values drift per channel (GH: GALDIESEL/GALSUPER/
  GALREGULAR; CD: CGP*LBS set + GALDIESEL) — shall be emitted per the
  working-authority (GH) reading with the CD reading recorded as drift;
  CodigoProducto is the fuel-subsidy control enum (Decreto 15-2021 doc
  anchor), never an Odoo product default_code. (LB-010; LB-012; EVID-011,
  EVID-013; GOQ-02 umbrella)
- **GT-EINV-FR-052:** Totales shall group TotalImpuesto rows per
  NombreCorto (cap 20 groups — unchanged on both channels even though the
  per-item cap tightened on GH), each summing the MontoImpuesto of
  same-tax items, with GranTotal = sum of item totals; grouping
  arithmetic and validation tolerances are owned by
  03_validation-rules.md. (LB-008; EVID-009)
- **GT-EINV-FR-053:** Document currency shall be restricted to the closed
  28-enum tipoMoneda list (not free ISO 4217), including the GH-added PLN
  row whose sole provenance is the inline comment "esloti Polaco -
  Requerimiento 06052026" [sic] — an internal SAT tracker id, not a
  published norm, recorded as a dated anchor → OQ-005 (GOQ-22, minor).
  (LB-010; EVID-011)

### 3.4 Identifier patterns & frases container

- **GT-EINV-FR-054:** Receiver/transportista ID validation shall implement
  the tipoNITReceptor alternatives verbatim from the working-authority
  copy: (a) classic NIT ending in digit or K; (b) 12–13 digit CUI-style
  ID; (c) literal "CF"; (d) 3–18 char foreign-ID token with the GH-widened
  charset `[A-Z0-9&%-/#=]` (source `&amp;` = literal `&`); emitter and
  certificador NITs accept the classic format only. The mid-alternative
  `^(` and the widened charset shall be carried exactly as published —
  never "fixed" locally — with the pattern held as configuration so the
  CD/GH charset drift can be switched by ruling; practical production
  handling is open → OQ-002 (GOQ-18). (LB-005; EVID-006)
- **GT-EINV-FR-055:** The Frases container shall serialize up to 100 Frase
  elements, each with TipoFrase (1..12 GH / 1..9 CD — emitted per the GH
  domain), CodigoEscenario (1..99), and the optional
  NumeroResolucion/FechaResolucion demanded by the catalog's
  contieneResolucion/contieneFechaResolucion flags. The pairing rule is
  R6: the GH schema's TipoFrase ≤ 12 pairs with CatalogoFrases 0.6.0 (12
  tipos / 88 frases, 25/03/2025) — implemented by
  [../catalogs/01_governance.md](../catalogs/01_governance.md)
  GT-CAT-FR-009 — and the CD-internal inconsistency (schema 1..9 vs
  catalog 5 tipos) is recorded drift (GOQ-19, owned by the catalogs file);
  frase selection logic is owned by 03_validation-rules.md.
  (LB-006; EVID-007, EVID-027; R6)

### 3.5 Complement schemas

- **GT-EINV-FR-056:** A complement shall ride inside the signed DatosEmision
  area as `Complementos/Complemento` (unbounded; `xs:any` payload +
  optional IDComplemento) carrying the required `NombreComplemento` and
  `URIComplemento` ("Indica el URI del XSD del complemento."), with
  `ComplementosItem/ComplementoItem` as the item-level twin; canonical
  per-complement name/URI values are NOT enumerated in the schemas (names
  are printed only in Reglas §3.1; URIs nowhere) → OQ-004 (GOQ-21).
  Complementos are mandatory when the scenario requires them and reach
  SAT (SAT may reject or inform error when a required complement is
  missing). Per-complement applicability (0/1/2) is owned by
  03_validation-rules.md §complemento matrix. (LB-008; LB-026; LB-027;
  EVID-009, EVID-151, EVID-139)
- **GT-EINV-FR-057:** The system shall carry a complement-schema registry
  seeded from §4 Table B — 18 complement XSDs plus the 3-file Endoso
  family, each row recording XSD file name, transaction namespace
  (face2/0.1.0 family, with the recorded [sic] NS/filename mismatches),
  @Version regime (fixed "1" vs free decimal), and channel availability
  (identical / differs / GH-only) — and shall treat the committed
  `gt/sources/29_…` + `30_…` XSD files as the machine-readable contract
  of record. (LB-023; EVID-030 + drift matrix)
- **GT-EINV-FR-058:** The Abonos de factura cambiaria complement shall
  serialize unbounded Abono rows (NumeroAbono ≤ 3 digits, required
  FechaVencimiento, MontoAbono ≥ 0) on the cambiaria types, fed from the
  installment schedule (required-type list →
  03_validation-rules.md §complemento matrix). (LB-015; EVID-017)
- **GT-EINV-FR-059:** The reference complements shall serialize: for
  NCRE/NDEB, the origin's NumeroAutorizacionDocumentoOrigen matching the
  3-alternative UUID-or-paper pattern (FEL UUID, or legacy
  YYYY-E-…/YYYY-N-… authorization numbers under RegimenAntiguo="Antiguo")
  plus FechaEmisionDocumentoOrigen and MotivoAjuste (1..200); for
  CIVA/CAIS, the constancia variant with MontoIVAExento equal to the
  referenced DTE's total IVA; for BIDP-origin invoices, the GH-only
  ReferenciaBoletaDespacho. The 2-month NC IVA rule embedded in the
  FechaEmisionDocumentoOrigen documentation is recorded as schema-borne
  business-rule provenance; its computation detail is owned by
  03_validation-rules.md. (LB-016; EVID-018)
- **GT-EINV-FR-060:** The export complements shall serialize per the GH
  (working-authority, richer) copy: consignee name/address (1..300), the
  buyer and exporter blocks, INCOTERM from the 13-value enum (DAT and DPU
  coexist — mixed Incoterms vintage recorded [sic]), customs declaration
  (1..50), fechaExportacion (dd/mm/yyyy string pattern), viaTransporte
  (Aérea/Marítima/Terrestre), aduanaSalida, and the UUID-derived origin
  references; the provisional-export complement shall emit the GH element
  name `OtraReferencia` (CD's `OtraSReferencia` [sic] recorded as drift).
  Export applicability (FACT + Exp flag) per 01_document-types.md
  GT-EINV-FR-007. (LB-017; EVID-019, EVID-020)
- **GT-EINV-FR-061:** The retention complements shall serialize: for FESP,
  `RetencionesFacturaEspecial` with RetencionISR, optional RetencionIVA
  and TotalMenosRetenciones (Fac_Especial XSD, identical both channels);
  for FEPE, the GH-only `RetencionesFacturaEspecifica` with optional
  RetencionICT ("ICT" expansion unprinted — GOQ-24 kin, Task 4 file) and
  TotalMenosRetenciones. Retention arithmetic is owned by
  03_validation-rules.md. (LB-019; LB-020; EVID-023)
- **GT-EINV-FR-062:** The remaining shared complements shall serialize per
  their identical-both-channel XSDs: LEPP (political-party donations:
  CalidadAportante, TipoAporte, DeclaracionProcedencia, Aporte —
  RDON/RECI applicability per its doc string), Espectaculos (event
  code/name/locale/admission price/ticket number), TurismoPasaje
  (Decreto 31-2022 air-exit tourism exemption fields), and
  CobroXCuentaAjena (repeatable ItemCuentaAjena with taxable base +
  DAI/IVA/otros split). (LB-019; EVID-022, EVID-024)
- **GT-EINV-FR-063:** The GH-only sector complement set (ComplementoAlItem
  tariff code, DetalleProductos beverage excise detail, TrasladoMercancias
  NEV waybill data, GasLicuadoPetroleo and AlmacenajeGalonaje
  fuel-terminal measurements) shall be registered with a
  GH-channel-dependency flag: the entire sector capability (NEV transport
  data, beverage excise, IDP ecosystem) exists only on the GitHub channel,
  and its emission config shall surface that dependency (GOQ-02 umbrella).
  Structural defects are recorded, never fixed in place: @NoItem
  totalDigits 999999 [sic], NS/filename mismatches [sic].
  (LB-021; LB-023; EVID-025, EVID-030)
- **GT-EINV-FR-064:** The Endoso family (GT_Endoso / GT_AnulacionEndoso /
  GT_PagoEndoso, NS fel/0.2.0, GH-only) shall be recorded as registry
  data — the create/annul/pay endorsement lifecycle over the four
  endorsable cambiaria types (FCAM/FCAP/FCPC/FCRP) with Contrato
  TipoContrato Factoraje|Descuento — and is out of core product scope
  (factoring): no emission flow is built for it in this wave; its
  existence and the FCAP name expansion it evidences are consumed by
  01_document-types.md GT-EINV-FR-012. (LB-022; EVID-026)

### 3.6 Anulación & reversion schemas (structure only)

- **GT-EINV-FR-065:** The anulación transaction shall serialize
  GT_AnulacionDocumento (NS fel/0.1.0, @Version fixed "0.1"):
  GTAnulacionDocumento > SAT > AnulacionDTE > DatosGenerales@ID
  "DatosAnulacion" with the six required attributes —
  NumeroDocumentoAAnular (tipoUUID), NITEmisor (classic NIT), IDReceptor
  (widened tipoNITReceptor — the sole CD/GH drift in this file),
  FechaEmisionDocumentoAnular, FechaHoraAnulacion, MotivoAnulacion
  (1..255) — plus optional Certificacion and the same two ds:Signature
  slots; the XMLSpy editorial header comment is provenance trivia, never
  a requirement. Anulación behavior (windows, blockers, transport) is
  owned by 06_anulacion-contingencia.md. (LB-005; LB-013; EVID-006,
  EVID-015)
- **GT-EINV-FR-066:** The reversion transaction (undo of an anulación)
  shall serialize GT_ReversionDocumento (byte-identical both channels):
  NumeroDocumentoAReversar (tipoUUID) plus its Serie/Numero decomposition,
  NITEmisor, IDReceptor, both timestamps, MotivoReversion (1..255) and
  UsuarioSolicitud (1..100); the [sic] copy-paste annotation
  ("Transacción de anulación…") is recorded as a defect. No v1.2
  provider-boundary API operation exists for reversion (16_ prints none —
  R11 scope note); reversion behavior is owned by
  06_anulacion-contingencia.md. (LB-014; EVID-016)

### 3.7 Channel authority, drift & conformance

- **GT-EINV-FR-067:** XSD-set channel authority shall follow the
  master-index rule: GitHub 961133c is the working authority for every XSD
  EXCEPT `GT_Complemento_MediosdePago-0.1.0.xsd`, which is modeled from
  cat.desa because the GitHub copy is an uncompilable TurismoPasaje
  overwrite (undeclared `ctup:` prefix, lost TC/TD/EF/CH enum, wrong
  docs) — R2 working rule; payment TipoFormaPago ∈ {TC, TD, EF, CH} with
  optional transaction number/date/amount. Every inter-channel difference
  (8 differing shared files, 11 GH-only, 1 CD-only) is recorded — via the
  Task-1 drift surfaces ([../catalogs/_DRIFT.md](../catalogs/_DRIFT.md)
  for catalogs; the EVID-030 md5 drift matrix for XSDs) — and never
  silently resolved; whether SAT/GH will fix the defective copy is open →
  OQ-006 (GOQ-23; GOQ-02 umbrella). (LB-018; LB-023; EVID-021, EVID-030;
  R2)
- **GT-EINV-FR-068:** XSD conformance shall be the first validation gate:
  every generated DTE/anulación/reversion XML shall validate against the
  working-authority XSD set (with the local xmldsig copy) BEFORE any
  business-rule validation or submission, because XSD observance binds
  emisión, certificación and recepción (16_ §II.A) and the Reglas
  pipeline rejects non-conformant XML outright (rule 2.1 — pipeline
  detail owned by 03_validation-rules.md §validation pipeline).
  (LB-001; LB-024; EVID-001, EVID-150)
- **GT-EINV-FR-069:** Every schema vintage shall be stored as dated rows
  keyed by (channel, file, version string, date): the transaction-family
  namespace matrix (DTE+Endoso fel/0.2.0; Anulacion/Reversion fel/0.1.0;
  complements face2/0.1.0), the per-file @Version regimes, and the
  in-file dated anchors (DTE "Fecha de inicio de aplicacion: 2019-03-01";
  EXE "hasta 29/feb/2020"; PLN "Requerimiento 06052026"); a new published
  vintage appends rows, never overwrites (D16). The 16_ v1.2 document is
  never cited for current schema structure — its -0.1.0 inventory is the
  R11 drift record itself. (LB-023; LB-024; EVID-030, EVID-150; R11)
- **GT-EINV-FR-070:** Adenda (emitter↔receiver private payload) shall be
  kept strictly DTE-external: it forms no part of DatosEmision or DTE, is
  unsigned by both parties, does not alter DTE validity, and shall never
  be included in any XML submitted toward SAT — a DTE containing an
  Adenda element is rejected and must be re-sent without it; adenda
  content shall be stored and delivered through emitter↔receiver channels
  outside the certification payload. (LB-026; EVID-151)

## 4. Data Model

The machine-readable contract of record = the committed XSD sources
(`gt/sources/29_FEL_XSD_cat_github_961133c/` + `gt/sources/30_FEL_XSD_cat_catdesa/`,
md5-fingerprinted in the EVID-030 drift matrix); JSON catalog data lives in
the Task-1 sidecars ([../catalogs/_INDEX.md](../catalogs/_INDEX.md)). The
tables below are the seed registry both sides derive their
serializers/validators from.

**Table A — GT_Documento element/attribute inventory** (working authority
GH; channel drift noted):

| Element / attribute | Type / facets | Notes | EVID |
|---------------------|---------------|-------|------|
| GTDocumento @Version | xs:decimal, required, fixed "0.1" | version string 4 of 4 (GOQ-15) | 001 |
| SAT @ClaseDocumento | enum "dte" | — | 001 |
| DTE (doc "Agrupa la estructura para un DTE…") | container | since 2019-03-01 | 001 |
| DatosGenerales @FechaHoraEmision | dateTime, Guatemala -06:00 semantics | — | 010 |
| DatosGenerales @Tipo | 21 GH-active enums (15 common + 5 v2.0 + BIDP); 6 commented (CD-active) | owned by 01_document-types.md FR-001..004 | 002 |
| DatosGenerales @NumeroAcceso | integer 100000000–999999999 | contingencia only | 004 |
| DatosGenerales @Dispositivo | enum APP/AV/APPVOZ | SAT apps only (D-GT9) | 004 |
| DatosGenerales @EmisionUbicacionTemporal | enum "SI" | pairs frase tipo 9 esc 14 | 004 |
| DatosGenerales /Idp | datosGeneralesIDPType (8 required attrs) | GH only (BIDP/IDP) | 013 |
| ds:Signature id=FirmaEmisor | required | XAdES-BES/RSA/SHA-256 over DatosEmision (R12) | 001 |
| ds:Signature id=FirmaCertificador | minOccurs 0 | covers DTE node | 001 |
| Emisor/NITEmisor | tipoNITDelEFACE (≤13, classic NIT) | no CF/foreign | 003, 006 |
| Emisor/NombreEmisor | 1..400 | — | 003 |
| Emisor/CodigoEstablecimiento | xs:positiveInteger 1–9999 | SAT-assigned; the only establishment slot (D-GT9) | 003 |
| Emisor/NombreComercial | 1..255 | — | 003 |
| Emisor/CorreoEmisor | TipoCorreoElectronico (semicolon list) | — | 003, 012 |
| Emisor/DireccionEmisor | tipoDireccion (all fields required) | strict, unlike receptor | 005 |
| Emisor/AfiliacionIVA | GH: GEN EXE PEQ ECA EXI PRI PEC OMI IDP; CD adds PEE AGR AGE | EXE anchor 29/feb/2020 | 003 |
| Emisor/AfiliacionOmiso · ClasificacionEmisor (1674) | GH only | — | 003 |
| Receptor/IDReceptor + @TipoEspecial | tipoNITReceptor (4 alternatives); TipoEspecial CUI/EXT | charset drift GOQ-18 | 005, 006 |
| Receptor/NombreReceptor | 1..400 | registry-match when valid NIT | 005 |
| Receptor/DireccionReceptor | tipoDireccionReceptor (street only required) | GH relaxation | 005 |
| Receptor/DestinodelaVenta | union Primario/Pecuario/Condición enums | GH; "Comercializador" ×2 [sic] | 005, 014 |
| Frases/Frase (≤100) | TipoFrase 1..12 (GH) / 1..9 (CD); CodigoEscenario 1..99; NumeroResolucion?; FechaResolucion? | R6 pairing with CatalogoFrases 0.6.0 | 007 |
| Items/Item (≤9999) | @NumeroLinea 1..9999; @BienOServicio B/S; CodigoProducto?; Cantidad; UnidadMedida? (1..3); Descripcion 1..10000; PrecioUnitario/Precio/Descuento/OtrosDescuento; Observaciones? (GH, ≤50) | Precio = PrecioUnitario × Cantidad | 008 |
| Item/Impuestos/Impuesto | ≤2 (GH) / ≤20 (CD): NombreCorto (TipoImpuesto); CodigoUnidadGravable (≤7 digits); MontoGravable?; CantidadUnidadesGravables?; MontoImpuesto; Afecto?/Idp? (GH) | cap GOQ-20 | 008 |
| Item/ComplementosItem/ComplementoItem | xs:any + NombreComplementoItem + URIComplementoItem (required) | item-level twin | 008 |
| Totales/TotalImpuestos/TotalImpuesto (≤20) | @NombreCorto; TotalMontoImpuesto | groups per tax | 009 |
| Totales/GranTotal | NumeroNDecimales | sum of item totals | 009 |
| Complementos/Complemento (unbounded) | xs:any + IDComplemento? + NombreComplemento + URIComplemento (required) | values GOQ-21 | 009 |
| Certificacion/* | NITCertificador; NombreCertificador 1..400; NumeroAutorizacion tipoUUID + @Serie/@Numero; FechaHoraCertificacion | certificador-produced | 010 |
| TipoImpuesto | 12 names (IVA … TARIFA PORTUARIA) | catalog join key | 011 |
| tipoMoneda | closed 28 enums + PLN (GH) | GOQ-22 | 011 |
| CodigoProducto | GH: GALDIESEL/GALSUPER/GALREGULAR; CD: CGP*LBS set + GALDIESEL | fuel subsidy enum | 011 |
| NumeroNDecimales | decimal ≥ 0, ≤10 fractional, ≤22 total digits | amounts | 012 |

**Table B — complement & transaction schema inventory** (GH = GitHub
961133c; CD = cat.desa; SAME/DIFF per the drift matrix; structure = this
file, applicability = 03_validation-rules.md §complemento matrix):

| XSD file | Namespace (version) | @Version | Channel | Scope |
|----------|---------------------|----------|---------|-------|
| GT_Complemento_Cambiaria-0.1.0.xsd | fel/CompCambiaria/0.1.0 | fixed 1 | SAME | FCAM-family installment abonos (FR-058) |
| GT_Complemento_Referencia_Nota-0.1.0.xsd | face2/ComplementoReferenciaNota/0.1.0 | free decimal | SAME | NCRE/NDEB origin reference (FR-059) |
| GT_Complemento_ReferenciaConstancia-0.1.0.xsd | face2/ComplementoReferenciaConstancia/0.1.0 | free decimal | SAME | CIVA/CAIS origin reference (FR-059) |
| GT_Complemento_ReferenciaBoletaDespacho-0.1.0.xsd | face2/ComplementoReferenciaBoletaDespacho/0.1.0 | free decimal | GH-only | BIDP origin reference (FR-059) |
| GT_Complemento_Exportaciones-0.1.0.xsd | face2/ComplementoExportaciones/0.1.0 | fixed 1 | DIFF (GH richer) | export annex (FR-060) |
| GT_Complemento_ExportacionProvisional-0.1.0.xsd | face2/ComplementoExportacionProvisional/0.1.0 | fixed 1 | DIFF (one token) | provisional export (FR-060) |
| GT_Complemento_MediosdePago-0.1.0.xsd | face2/ComplementoMediosDePago/0.1.0 | required decimal (CD copy) | DIFF — cat.desa governs (R2) | payment means TC/TD/EF/CH (FR-067) |
| GT_Complemento_PartidosPoliticos-0.1.0.xsd | face2/ComplementoPartidosPolitico/0.1.0 [sic] | free decimal | DIFF (cosmetic) | LEPP donations (FR-062) |
| GT_Complemento_Fac_Especial-0.1.0.xsd | face2/ComplementoFacturaEspecial/0.1.0 | fixed 1 | SAME | FESP retentions (FR-061) |
| GT_Complemento_RetencionesFacturaEspecifica.xsd | face2/ComplementoRetencionesFacturaEspecifica/0.1.0 | free decimal | GH-only | FEPE ICT retention (FR-061) |
| GT_Complemento_Espectaculos-0.1.0.xsd | face2/ComplementoEspectaculos/0.1.0 | fixed 1 | SAME | event ticketing (FR-062) |
| GT_Complemento_TurismoPasaje-0.1.0.xsd | face2/ComplementoTurismoPasaje/0.1.0 | fixed 1 | SAME | air-exit tourism exemption, Dec. 31-2022 (FR-062) |
| GT_Complemento_CobroXCuentaAjena-0.1.0.xsd | face2/CobroXCuentaAjena/0.1.0 | fixed 1 | SAME | third-party collection (FR-062) |
| GT_ComplementoAlItem.xsd | face2/ComplementoAlItem/0.1.0 | free decimal | GH-only | item tariff code (FR-063) |
| GT_ComplementoDetalleProductos-0.1.0.xsd | face2/ComplementoDetalleDeProductos/0.1.0 [sic] | free decimal | GH-only | beverage excise detail (FR-063) |
| GT_ComplementoTrasladoMercancias-0.1.0.xsd | face2/TrasladoMercancias/0.1.0 | free decimal | GH-only | NEV waybill data (FR-063) |
| GT_Complemento_GasLicuadoPetroleo.xsd | face2/ComplementoGasLicuadoPetroleo/0.1.0 | fixed 1 | GH-only | GLP measurements (FR-063) |
| GT_Complemento_AlmacenajeGalonaje-0.1.0.xsd | face2/ComplementoAlmacenamientoGalonaje/0.1.0 [sic] | fixed 1 | GH-only | fuel-terminal gallonage (FR-063) |
| GT_Endoso-0.1.0.xsd · GT_AnulacionEndoso-0.1.0.xsd · GT_PagoEndoso-0.1.0.xsd | fel/0.2.0 | fixed 1 | GH-only | endorsement lifecycle, out of core scope (FR-064) |
| GT_AnulacionDocumento-0.1.0.xsd | fel/0.1.0 (schema version 0.1.0) | @Version fixed 0.1 | DIFF (one pattern line) | anulación transaction (FR-065) |
| GT_ReversionDocumento-0.1.0.xsd | fel/0.1.0 (schema version 0.1.0) | @Version fixed 0.1 | SAME | reversion transaction (FR-066) |
| xmldsig-core-schema.xsd | W3C xmldsig core | — | SAME | local copy for the network-URL import (FR-044) |

**Table C — version-string & dated-anchor registry** (D-GT10/D16 rows;
stored as (channel, file, version string, date), append-only):

| Artifact | Version strings / anchors (verbatim) | EVID |
|----------|--------------------------------------|------|
| GT_Documento | filename 0.2.1 · NS fel/0.2.0 · schema@version 2.0 · GTDocumento@Version 0.1 · "Fecha de inicio de aplicacion: 2019-03-01" | 001, 030 |
| GT_AnulacionDocumento / GT_ReversionDocumento | filename 0.1.0 · NS fel/0.1.0 · schema@version 0.1.0 · @Version 0.1 | 015, 016, 030 |
| Endoso family | NS fel/0.2.0 (filename 0.1.0) | 026, 030 |
| Complements (family) | NS face2/Name/0.1.0 · @Version fixed "1" or free decimal · XMLSpy editorial comments (provenance trivia, never requirements) | 030 |
| AfiliacionIVA EXE anchor | "(EXE queda por compatibilidad para DTE hasta 29/feb/2020)" | 003 |
| tipoMoneda PLN anchor | "esloti Polaco - Requerimiento 06052026" [sic] | 011 |
| CodigoProducto anchor | "Decreto número 15-2021" (gas propano subsidy doc) | 008 |
| 16_ Documento Técnico | "Versión 1.2"; XSD inventory at -0.1.0 filenames / 4 complements = the R11 drift record | 150 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2): `odoo` = configuration and
registry surface in the LGPL client; `saas` = XML emission, signing and
authoritative validation in the Elixir core; `shared` = contract items
both sides must honor identically — per the wave brief, the schema itself
is a `shared` contract (both sides serialize against the same XSD set).
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-042 | shared | — | — | Envelope contract: both sides serialize GTDocumento/SAT/DTE/DatosEmision identically; Tipo value from the 01-file registry |
| FR-043 | shared | l10n_gt.schema.version (new, config data) | version strings ×4 | Recorded as data both sides log; no code path keys on one string while GOQ-15 open |
| FR-044 | saas | — | — | XAdES-BES/RSA/SHA-256 signing + verification in the core; local xmldsig copy bundled; FirmaEmisor/FirmaCertificador IDs per XSD |
| FR-045 | saas | account.move (mirror fields) | auth UUID, Serie/Numero, FechaHoraCertificacion | Ingested from provider response, mirrored to client archive (D3); never generated |
| FR-046 | shared | res.company + l10n_gt.establishment | CodigoEstablecimiento (1–9999), NombreComercial, AfiliacionIVA | Value capture client-side, serialization core-side; establishment mapping detail = 05 file (D-GT9) |
| FR-047 | shared | res.partner | vat/l10n_gt ID + TipoEspecial + DestinodelaVenta | Partner capture client-side; registry-match rule core-side |
| FR-048 | shared | account.move | contingencia NumeroAcceso, ubicacion-temporal flag | Contingencia flow itself = 06 file |
| FR-049 | shared | account.move.line | line fields → Item mapping | Contract for both serializers; rounding/tolerance detail = 03 file |
| FR-050 | shared | account.move.line, account.tax | tax_ids → Impuesto (≤2/line) | Cap enforced at emission; line-splitting UX surfaced client-side |
| FR-051 | saas | product.template (fuel flag) | CodigoProducto enum | Fuel-sector only; channel drift config carried with the registry |
| FR-052 | shared | account.move | amount totals → Totales | Grouping contract; arithmetic authority = 03 file |
| FR-053 | shared | res.currency (GT whitelist) | name in 28-enum list | Closed-list check both sides; PLN row carries GOQ-22 flag |
| FR-054 | shared | res.partner | vat validation pattern | Pattern held as switchable config (CD/GH charset); odoo partner form pre-checks, SaaS validates |
| FR-055 | shared | — | — | Container contract; pairing per GT-CAT-FR-009; selection logic = 03 file |
| FR-056 | shared | — | — | Wrapper contract + name/URI strings = contract items (values pending GOQ-21) |
| FR-057 | odoo | l10n_gt.complement.schema (new registry) | file, ns, version, channel, scope | Seed rows = §4 Table B; feeds emission config |
| FR-058 | saas | account.move (payment terms → abonos) | installment schedule | Schedule captured client-side (payment terms), complement built core-side |
| FR-059 | saas | account.move (ref/origin) | origin UUID or legacy auth number | Legacy paper/FACE1 origin picker = 01-file FR-040 reference data |
| FR-060 | saas | account.move + sale (export data) | consignee/buyer/INCOTERM/vía/aduana | Export capture client-side; GH copy serialized |
| FR-061 | saas | account.move | retention staging lines | FESP/FEPE retention complements; arithmetic = 03 file |
| FR-062 | saas | account.move | scope-conditional annex inputs | LEPP/Espectaculos/TurismoPasaje/Cobro ajena flows |
| FR-063 | saas | product/stock (sector fields) | NEV waybill, beverage, fuel inputs | GH-channel-dependency flag surfaces in config (GOQ-02) |
| FR-064 | odoo | l10n_gt.complement.schema | Endoso rows | Registry-only; no emission flow (out of core scope) |
| FR-065 | saas | account.move (cancel flow) | anulación payload fields | Request origination client-UX, XML build core-side; behavior = 06 file |
| FR-066 | saas | — | — | Structure recorded; no v1.2 API operation (R11); behavior = 06 file |
| FR-067 | shared | l10n_gt.schema.version / registry | channel authority column | R2 override stamped on the MediosdePago row; drift surfaces consumed from Task-1 artifacts |
| FR-068 | saas | — | — | Authoritative XSD gate core-side pre-submission; client pre-validates for early UX |
| FR-069 | shared | l10n_gt.schema.version | dated rows (channel, file, version, date) | Append-only vintage registry both sides read |
| FR-070 | shared | account.move (adenda staging) | adenda payload (never in DTE XML) | Both sides responsible: stripping at submission core-side; storage/delivery client-side |

## 6. Acceptance Criteria

- **AC-001:** Given any generated DTE (and any anulación/reversion XML),
  when validated against the working-authority XSD set with the local
  xmldsig copy, then it conforms with zero network fetches and zero
  schema-side errors. (FR-042, FR-068)
- **AC-002:** Given the schema registry, when inspected, then the
  GT_Documento row records all four version strings verbatim (filename
  0.2.1 / NS fel/0.2.0 / schema@version 2.0 / GTDocumento@Version 0.1)
  and no validation code path branches on any single one. (FR-043)
- **AC-003:** Given a certified DTE received back from the provider, when
  its signatures are checked, then the emisión signature covers
  DatosEmision and the certificación signature covers the DTE node, both
  XAdES-BES/RSA/SHA-256 with distinct IDs. (FR-044)
- **AC-004:** Given an invoice line carrying three taxes (e.g. IVA + TASA
  MUNICIPAL + TIMBRE DE PRENSA), when emission is prepared under the
  conservative cap, then the line is split so no Item carries more than 2
  Impuesto elements (GOQ-20 pending). (FR-050)
- **AC-005:** Given a receiver ID "CF", a 13-digit CUI, a classic NIT
  ending in K, and a foreign token containing "&", when each is validated
  against the GH working-authority pattern, then all four pass; given the
  same foreign token validated against a CF/foreign value in NITEmisor,
  then it is rejected. (FR-054)
- **AC-006:** Given any emitted complement, when serialized, then it
  carries NombreComplemento and URIComplemento values drawn from the
  canonical table once captured (GOQ-21) and validates against its own
  complement XSD. (FR-056, FR-057)
- **AC-007:** Given a MediosdePago complement, when built, then
  TipoFormaPago ∈ {TC, TD, EF, CH} per the cat.desa copy and the GitHub
  copy is never loaded as schema authority. (FR-067)
- **AC-008:** Given an XML payload submitted toward SAT, when inspected,
  then it contains no Adenda element — adenda content is delivered only
  via emitter↔receiver channels. (FR-070)
- **AC-009:** Given an anulación request, when serialized, then the
  DatosGenerales element carries all six required attributes with
  MotivoAnulacion ≤ 255 chars and IDReceptor in the widened charset.
  (FR-065)
- **AC-010:** Given the complement registry, when counted, then it holds
  18 complement XSDs + 3 Endoso files + AnulacionDocumento +
  ReversionDocumento + xmldsig core, each row carrying namespace,
  @Version regime and channel status per §4 Table B. (FR-057)
- **AC-011:** Given a DTE with frases, when serialized, then every
  TipoFrase ≤ 12 pairs with a CatalogoFrases 0.6.0 row (GT-CAT-FR-009) and
  escenario-flagged frases carry NumeroResolucion/FechaResolucion.
  (FR-055)
- **AC-012:** Given the Odoo Mapping table, when checked, then every FR
  row carries a Layer value (odoo/saas/shared) and the schema-contract
  FRs are `shared`. (§5)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.1);
question text copied verbatim from the register. This file OWNS GOQ-15,
GOQ-18, GOQ-20, GOQ-21, GOQ-22, GOQ-23. Kin ids referenced inline only:
GOQ-02 (channel umbrella, catalog-owned), GOQ-19 (frases runtime, catalogs
file), GOQ-17 (dispositivo via adenda, E7 file), GOQ-24 (ICT expansion,
Task 4 file).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-15 (owned): "Which version string does production validation key on — filename 0.2.1 / NS 0.2.0 / schema@version 2.0 / GTDocumento@Version 0.1 (four coexist)?" Blocks FR-043's keying decision; umbrella GOQ-02. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT/TotalDoc) | open |
| OQ-002 | GOQ-18 (owned): "Practical handling of the NIT-pattern mid-alternative `^(` and widened charset `[A-Z0-9&%-/#=]` by the production validator." Blocks FR-054's charset freeze. | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-003 | GOQ-20 (owned): "Per-item Impuesto cap: GH caps at 2 (IVA+1), CD allows 20 — are real multi-tax lines (IVA + TASA MUNICIPAL + TIMBRE DE PRENSA) rejected on the GH rule set?" Blocks FR-050's conservative cap (line-splitting stays until answered). | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-004 | GOQ-21 (owned): "Canonical NombreComplemento/URIComplemento values per complement (names known from EVID-139; URIs not captured)." Blocks FR-056's canonical name/URI table. | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-005 | GOQ-22 (owned, minor): "Basis of 'Requerimiento 06052026' (PLN currency addition) — internal SAT tracker, not a published norm." Affects FR-053's PLN provenance row only. | no | GT synthesis wave S-GT1 | open |
| OQ-006 | GOQ-23 (owned): "MediosdePago: will SAT/GH fix the defective GitHub copy; cat.desa governs meanwhile (R2 working rule)." Blocks FR-067's channel-override removal. | no | GT synthesis wave S-GT1 → W6 partner ask | open |
