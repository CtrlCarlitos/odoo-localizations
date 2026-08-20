# GT — E-Invoicing — Certificador interface, provider model & establishment model (D-GT9)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the Guatemala FEL
certificador/provider interface and the establishment model: the provider
architecture (SAT owns the standard, validates and pushes registry data;
taxpayers integrate via *certificadores* (certifiers); TotalDoc = GRUPO CDS
S.A., NIT 107902281, is the product default provider); the SAT↔certificador
boundary semantics of the *Documento Técnico Informático para certificadores*
v1.2 (technical specification for certifiers) — certification lifecycle,
UUID/Serie/Numero numbering authority, the two XAdES signatures, anulación
transport immutability, adenda/complemento treatment, result-code vocabulary
and the mini-RTU registry feed — cited ONLY as boundary semantics, never as
the product's own API contract (R11); the certificador authorization regime
(AD 13-2018 arts. 14–20 developed by the 22_ v2.1 procedure) with the 31_
roster as D15/D16 dated data; and the establishment / *dispositivo* (device)
model D-GT9: `CodigoEstablecimiento` + `NombreComercial` as the only
establishment identity, the SAT-apps-exclusive dispositivo enum, the
contingencia NumeroAcceso accessor, and the RTU validation teeth delivered
through this interface.

The establishment subsection (§3.7) is **pre-flagged for product-owner
visibility** (gt/HANDOVER.md §5a/§9): D-GT9 records that no taxpayer
punto-de-emisión field exists, that sucursal/warehouse maps to
CodigoEstablecimiento, and that a POS/cash-register or dispositivo mapping is
rejected — a material product-scope decision, not an implementation detail.

It does **not** cover: the DTE taxonomy (`01_document-types.md`, E1), the XSD
schema structure (`02_dte-schema.md`, E2 — including the Certificacion block
fields, FR-045), the Reglas v2.0 validation-rule universe
(`03_validation-rules.md`, E3 — the establishment gates FR-087..FR-091 live
there), the legal chain and mandate chronology (`04_mandate-onboarding.md`,
E4 — onboarding/acreditación FR-164..FR-167 live there), anulación windows,
blockers and contingencia behavior (`06_anulacion-contingencia.md`, cluster
E6), or the graphic representation (`07_display-representation.md`, cluster
E8). Those files reference this one for the provider contract, the roster and
the establishment model.

## 2. Legal Basis

Authority guards (binding, from the master index): **16_ Documento Técnico
v1.2 = SAT↔certificador boundary SEMANTICS only** — never cited for current
schema structure (it references -0.1.0 filenames while the live repo serves
GT_Documento-0.2.1 — R11) or production URLs (none printed; every URL in it
is `desa`/dev). The product integrates via the certificador's own API
(TotalDoc provider docs = W6 partner access, GOQ-39); SAT is never called
directly by the product. Reglas cited as "v2.0 (19/12/2024, vigencia abril
2025)" only (stale "v1.7.10/Febrero 2025" cover footer never cited; filename
encodes it). 22_ cited as v2.1 with the mixed-footer caveat (R14/GOQ-40).
Rulings applied: R11, R12, R13, R14.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 16_ DTI v1.2: "Documento Técnico Informático para certificadores del Régimen FEL" / "Versión 1.2" / "Nota de la versión 1.2: Se actualizaron URL hacia el nuevo ambiente para desarrollo y pruebas." / alcance: "Este documento describe los aspectos técnicos-informáticos de los servicios desarrollados por la SAT para nuevo sistema de factura electrónica en línea, que deben ser empleados por los CERTIFICADORES" | Technical specification for certifiers v1.2 (undated; change-without-notice clause); v1.2 note = URLs updated to the new dev/test environment; scope = the SAT↔certificador web-service contract only (DTE reception + P/S catalog propagation) — the emisor is never a direct consumer | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | pp. 1–4 (EVID-146, EVID-147) |
| LB-002 | 16_ §I.B ciclo: "1. Cada emisor o contribuyente construye un XML con firma de emisión y lo envía al CERTIFICADOR, quien debe aplicar todas las reglas de validación proporcionadas por la SAT…" "2. … asigna número de autorización de forma automatizada e incorpora la firma electrónica avanzada a la certificación." "4. La SAT devuelve un acuse de recibo con un código de mensaje de respuesta…" y rechazos: "Cuando un documento es rechazado o recibido con errores no imputables al certificador, el certificador tiene la obligación de informar al emisor…; si el rechazo o error es imputable al certificador, este debe corregirlo y enviar de nuevo el documento." | Certification lifecycle in 5 steps (emisor XML + emisión signature → certificador validates SAT rules → certificador assigns authorization number + advanced signature → SAT reception → catalog-coded acuse stored by certificador); rejection responsibility split emisor-vs-certificador | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | pp. 5–6 (EVID-148, EVID-149) |
| LB-003 | 16_ §II: firma de emisión "se realiza sobre el elemento DatosEmision"; "El elemento NumeroAutorización contiene el identificador único que el CERTIFICADOR debe asignar … es de tipo aleatorio, es decir, versión 4 de acuerdo con la especificación de UUID"; "ambas son incorporadas al XML por medio de un elemento Signature con un ID diferente … empleando las extensiones Xades-Bes y firmas tipo RSA con algoritmo SHA-256"; complementos "forman parte de los nodos firmados por el EMISOR" y "deben ser enviados a la SAT"; adenda "no forma parte de los elementos DatosEmision ni DTE … no debe ser enviado a la SAT … la SAT rechazará el mismo"; pruebas "Certificados RSA con llaves de 2048 … https://www.pkicloud.com/" | Emisión signature covers DatosEmision; NumeroAutorización = random UUID v4 assigned by the certificador (numbering authority); both signatures XAdES-BES/RSA/SHA-256 with distinct Signature IDs; complementos signed + mandatory when required and always sent to SAT; adenda outside the DTE, unsigned, must never reach SAT (rejection if present); dev-test certs self-generated RSA-2048 | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | pp. 8–13 (EVID-151..154) |
| LB-004 | 16_ §III API recepción: "https://api.desa.sat.gob.gt/getToken" con "Autenticación Básica" … "un token … tiempo de vida (60 minutos), al vencer el token se debe de volver a generar uno nuevo"; "El API de recepción de DTE se encuentra publicado en la dirección siguiente: https://api.desa.sat.gob.gt /postFactura"; "en el Header se debe de incluir el token … con el nombre de "Access _Token"" [sic spacing; illustrations print "Access_Token"]; "dichos códigos se encuentran detallados en el catálogo de Errores"; acuse + nota 6 "En una siguiente versión este mensaje de acuse de recibo incorporará una firma electrónica simple" | SAT reception API (REST, certificador-facing): GET /getToken basic-auth with 60-minute token; POST /postFactura single DTE XML in body with Access_Token header [sic]; response codes from the mensajes catalog; acuse returned on success — signature deferred to a future version (R13: assume v1.2 unsigned) | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | pp. 15–18 (EVID-155) |
| LB-005 | 16_ §IV anulación: "La anulación se realiza por una operación externa al DTE y no modificará en ningún caso un DTE ya certificado, únicamente consiste en una anotación lógica vinculada al DTE que sea anulado."; "La operación de anulación … debe ser firmada por el EMISOR … y también debe ser firmada por el CERTIFICADOR para su validez"; "https://api.desa.sat.gob.gt /postAnulacionDTE"; "Esta firma se realiza sobre el elemento DatosGenerales"; esquema "GT_AnulacionDocumento-0.1.0.xsd" | Anulación = external logical annotation, never modifies a certified DTE; the anulación operation is double-signed (emisor over DatosGenerales + certificador); same token/header/response pattern; AnulacionDocumento schema | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | pp. 19–23 (EVID-156, EVID-157) |
| LB-006 | 16_ §V.A mini-RTU: "Datos del Registro Tributario Unificado de los Emisores de DTE habilitados: • Nombre del EMISOR … • Nodo ESTABLECIMIENTOS o Número de establecimiento o Nombre del establecimiento (nombre comercial) o Dirección … ▪ Zona … o Estatus (activo o no activo) • Nodo AFILIACIONES o Impuesto o Régimen • Nodo MARCAS o Código o Fecha o Valor"; "2. Datos generales de los contribuyentes … NIT, nombre o razón social y CUI cuando corresponda" | Mini-RTU feed content: emitter master data (name, ESTABLECIMIENTOS node with number/commercial-name/address/status, AFILIACIONES regime, MARCAS traits) + general taxpayer data (NIT/nombre/CUI) shared with certificadores | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | p. 24 (EVID-158) |
| LB-007 | 16_ §V.B–E + §VI: "el certificador debe de contar con un Uri … al momento de darse de alta esto permitirá realizar los envíos de información de cambios de los contribuyentes" (delta JSON: "Nit":"800000000011" ,"afiliacionIVA":"PEQ","marcas":[],"establecimientos":[{…}],"frases":[{…}]); anexo: "3. Catálogo de Mensajes Contiene la información de los errores tanto de rechazo, como informativos y secundarios … Adicional a esto se tienen mensajes definidos para autenticación, anulaciones, éxito y errores genéricos" | SAT→certificador PUSH model (webhook URI, email fallback) for registry deltas with JSON keys Nit/afiliacionIVA/marcas[]/establecimientos[]/nombre/frases[]; the response vocabulary = Catálogo de Mensajes with dedicated groups (rechazo/informativos/secundarios/autenticación/anulaciones/éxito/genéricos) | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | pp. 25–27 (EVID-159, EVID-160) |
| LB-008 | AD 13-2018 (texto consolidado 01_) arts. 14–20: "El emisor puede operar con más de un certificador simultáneamente." (14); art. 15 (reformado por 15-2020) requisitos y umbrales "capital en giro … un millón de quetzales … persona individual" / "capital autorizado y pagado mínimo de un millón de quetzales … personas jurídicas" / "activos fijos netos … cinco millones de quetzales … no lucrativas"; "La autorización para operar como certificador deberá ser renovada anualmente"; "La SAT podrá ejercer la función de certificador … sin cumplir con presentar la documentación requerida"; autogenerados "únicamente … para emitir sus propios DTE"; (17) "contrato administrativo con la SAT"; (18) "seguro de caución … por un millón de quetzales (Q1,000,000.00)"; (19) "La SAT mantendrá publicada y actualizada … El listado de certificadores autorizados"; (20) retiro "al menos tres meses de anticipación" | Certificador regime: multiple simultaneous per emisor; eligibility tiers Q1M/Q1M/Q5M (15-2020 widened to non-profits); annual renewal; SAT-as-certificador for the free app; self-certifiers for own DTEs; administrative contract + Q1M surety; SAT-published roster; 3-month withdrawal notice | `gt/sources/01_AD_13-2018_FEL.pdf` | Arts. 14–20 pp. 7–10 (EVID-042..045) |
| LB-009 | 22_ v2.1 (pies de página mixtos 10-07-2024/03-09-2018 — R14): "la certificación de un DTE que incluya en su detalle 50 ítems de por lo menos 10 caracteres demora 3 segundos o menos"; "Disponibilidad: … una disponibilidad igual o mayor al 99.7%"; "módulo de seguridad criptográfico validado bajo el estándar FIPS-140-2 nivel 2 o superior"; "Certificado de seguridad de la información vigente, bajo el estándar ISO/IEC 27001"; lista de seguridad ítem 28: "La retención de los respaldos de información … debe tener como plazo mínimo 14 meses y extenderse hasta que la SAT indique que se han conciliado los DTE certificados"; "La autorización brindada al certificador tiene una vigencia de un año" | Certificador authorization procedure v2.1: performance SLAs (3 s / 50-item DTE, ≥99.7% availability), HSM FIPS 140-2 L2+, ISO 27001 security certificate, 109-item security checklist incl. 14-month backup retention until SAT conciliation, one-year authorization windows | `gt/sources/22_FEL_autorizacion_certificador.pdf` | §§2.1–2.4 pp. 5–38 (EVID-096..105) |
| LB-010 | 31_ roster (captura 2026-08-18; página dateModified 2026-07-09): encabezado "Certificador | Dirección | Contacto | Fecha de Autorización | Fecha de Renovación"; fila ancla "GRUPO CDS S.A. | NIT 107902281 www.grupocds.com.gt … 02/12/2021 | 02/12/2026"; 18 filas; tabla "empresas en proceso de autorización" con fila única "– | – | – | – | – | – | – | –" | SAT's authorized-certificador roster as-of 2026-08-18: 18 authorized; GRUPO CDS (TotalDoc) window 02/12/2021→02/12/2026; empty authorization pipeline (all-dash row, semantics open) | `gt/sources/31_certificadores_dte_snapshot_2026-08-18.html` | tabla de certificadores (EVID-106..108) |
| LB-011 | GT_Documento-0.2.1.xsd: `CodigoEstablecimiento` doc "Número del establecimiento donde se emite el documento. Es el que aparece asignado por SAT en sus registros." restricción `xs:positiveInteger` minInclusive 1, maxInclusive 9999; `NombreComercial` (1..255) doc "nombre comercial del establecimiento (de acuerdo a los registros tributarios)"; `Dispositivo` doc "Campo de uso para identificar del dispositivo donde se realizó. Uso exclusivo para aplicación de SAT AV y SAT móvil (App)" enums "APP" "AV" "APPVOZ"; `NumeroAcceso` doc "Es un número generado por el Emisor en caso de contingencia, que va desde 100000000 hasta 999999999"; `EmisionUbicacionTemporal` enum "SI" doc "Indica si el establecimiento se encuentra en una ubicación temporal"; @Serie doc "Se forma con los primeros 8 dígitos hexadecimales del UUID, de izquierda a derecha… De un UUID Original: dbb51ae2-3a62-4437-b8e9-42ecfb761156, el valor resultante será: dbb51ae2"; @Numero doc "Se forma con el equivalente en números decimales de los dígitos hexadecimales del UUID, a partir de la posición 9 hasta la posición 16 (excluyendo los guiones "-" )… el valor resultante será: 979518519" | DTE establishment identity = SAT-assigned CodigoEstablecimiento (1–9999) + NombreComercial only; @Dispositivo is a SAT-apps-exclusive enum; NumeroAcceso = 9-digit contingencia accessor; EmisionUbicacionTemporal=SI marks temporary location; Serie = first 8 UUID hex (example dbb51ae2), Numero = decimal of UUID hex positions 9–16 (example 979518519) — both post-certificación only | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` | Emisor lines 154–258; DatosGenerales lines 117–151; Certificacion lines 741–775 (EVID-003, EVID-004) |
| LB-012 | Reglas v2.0 §2.2.3: "El establecimiento no aparece activo en la SAT para ese NIT en esa fecha de emisión." + tablas de clasificación ("Exento Constitucional 1703 → Centros educativos privados 1704 …; Beneficio Fiscal Temporal 2204 → Maquila Decreto 29-89 … 2224; Persona jurídica … 887 → 963/1084/964; Entidad del Estado 886 → 899/965/966") + tabla regímenes ("3696 1696 Régimen Primario … / 3694 885 … / 3695 1696 Régimen Pecuario … / 3689 885 …") | Establishment RTU teeth: active at emission date; classification tables gate CIVA/CAIS/RECI/FESP; régimen primario/pecuario establishment pairs (3696/1696, 3694/885 primario; 3695/1696, 3689/885 pecuario), all FEPE-capable | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §2.2.3 pp. 24–26 + tablas (EVID-121) |
| LB-013 | catalogoMensajes-0.3.0.json ("Ultima Actualizacion": "02/12/2024"; 211 códigos, 7 familias): familias `FEL_RCP` 154, `FEL_AUT` 3, `FEL_ASO` 1, `FEL_GEN` 10, `FEL_INF` 6, `FEL_ANU` 22, `FEL_SEC` 15; éxito `FEL_RCP000` "Se Devuelve un FaceId"; establecimiento: `FEL_RCP305` "El establecimiento no existe en los registros de la SAT para ese NIT."; `FEL_RCP306` "El establecimiento no aparece activo en la SAT para ese NIT en esa fecha de emisión."; `FEL_RCP460` "Error. La clasificación o tipo del establecimiento no le permite el tipo de DTE."; `FEL_RCP485` "…DTE de tipo RANT y no corresponde el establecimiento para la actividad comercial según la tabla 2.2.3.2"; `FEL_RCP497` "Se envía un DTE que no corresponde según el establecimiento." | Runtime result-code dictionary (211 codes, 7 families) with the establishment teeth: 305 not-in-registry, 306 not-active-on-date, 460 classification incompatible, 485 RANT activity mismatch, 497 regime mismatch | `gt/sources/29_FEL_XSD_cat_github_961133c/catalogoMensajes-0.3.0.json` | catalog file (EVID-029; sidecar per GT-CAT-FR-013) |
| LB-014 | 17_ caso "Validaciones de Código de establecimiento" (vintage Mayo-2018; anexo Reglas 2.2.2): precondiciones "Estar con Estatus Activo. / NIT Existe en el RTU. / … / Contar con al menos un establecimiento Activo."; "Resultado: Error. El establecimiento no está activo en la SAT (para la fecha de emision [sic]). Rechaza." | 2018 SAT test case corroborating the establishment gate (active RTU establishment preconditions; INACTIVO/nonexistent code → reject) — historical, cited only as corroboration of LB-012 | `gt/sources/17_FEL_casos_de_prueba.zip` | caso file pp. 2–4 (EVID-110(b)) |
| LB-015 | AD 13-2018 art. 21: "El emisor debe conservar los archivos en formato XML de los DTE certificados mientras no haya transcurrido el plazo de prescripción que establece el Código Tributario, de igual forma el receptor, cuando corresponda." / certificador: "…hasta la renovación de su autorización como certificador…" | Emitter-side XML retention duty runs to the CT prescription period (not the certificador's 14-month backup floor) — the two retention clocks must not be conflated (GOQ-41) | `gt/sources/01_AD_13-2018_FEL.pdf` | Art. 21 p. 10 (EVID-046) |
| LB-016 | Reglas v2.0 §2.2.2 MARCAS: "1 Marca de domicilio no localizado … 0 = Domicilio OK / 1 = Domicilio no localizado"; "2 Marca de Omiso … 0 = No está omiso en IVA / 1 = Omiso en IVA" ("Esta información es provista a través del Mini RTU") | Emitter marcas traits (domicilio-no-localizado, omiso) are mini-RTU-fed non-blocking data — the registry feed drives emitter-eligibility context (rules owned by `03_validation-rules.md` FR-084) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §2.2.2 pp. 22–23 (EVID-120) |

## 3. Functional Requirements

### 3.1 Provider model & product integration boundary

- **GT-EINV-FR-171:** The system shall implement the FEL provider model
  (D-GT5/D-GT6): SAT owns the standard, validates each certified DTE and
  distributes registry/catalog data; taxpayers integrate exclusively through
  certificadores; the product shall never call a SAT API endpoint directly —
  every SAT interaction travels through the accredited certificador.
  (LB-001; LB-004; EVID-147, EVID-155)
- **GT-EINV-FR-172:** The system shall ship TotalDoc (GRUPO CDS S.A., NIT
  107902281) as the default certificador, configurable per company; an
  emisor may operate with more than one certificador simultaneously
  (acreditación lifecycle per GT-EINV-FR-166 in
  `04_mandate-onboarding.md`), and the provider selection shall be validated
  against the SAT-published roster (FR-201). (LB-008; LB-010; EVID-042,
  EVID-045, EVID-107)
- **GT-EINV-FR-173:** The product's operative API contract shall be the
  certificador's own interface documentation (TotalDoc provider docs — W6
  partner access), NOT the 16_ SAT-side specification; endpoint names,
  credential formats, homologation flow and catalog-sync mechanism are
  provider-boundary specifics → OQ-003 (GOQ-39). (LB-001; EVID-147;
  16_-file integration-boundary verdict)
- **GT-EINV-FR-174:** The 16_ v1.2 document shall be treated as boundary
  semantics only: it shall never be cited for current schema structure (its
  XSD inventory references -0.1.0 filenames vs the live GT_Documento-0.2.1
  repo — R11; structure is owned by `02_dte-schema.md`) nor for production
  URLs (none printed; all URLs are `desa`/dev). Semantics the provider must
  relay (numbering authority, dual signatures, result-code vocabulary,
  acuse evidence, anulación immutability, adenda exclusion) are the
  LB-citable content. (LB-001; LB-003; EVID-150; R11)

### 3.2 SAT↔certificador boundary operations (NOT product endpoints)

- **GT-EINV-FR-175:** The system shall record the 16_ v1.2 SAT-side
  operation inventory as boundary reference data, explicitly flagged
  dev-only and non-product: `GET /test` (availability), `GET /getToken`
  (basic auth → 60-minute token), `POST /postFactura` (one certified DTE
  XML per POST), `POST /postAnulacionDTE` (AnulacionDocumento XML), all
  under base `https://api.desa.sat.gob.gt` with header "Access_Token" [sic —
  body text prints "Access _Token", illustrations print "Access_Token"];
  whether op names, header spelling and the production base URL still hold
  → OQ-007 (GOQ-51). (LB-004; LB-005; EVID-155, EVID-157)
- **GT-EINV-FR-176:** The system shall assume NO batch, consulta/status or
  reversion operation exists at the SAT tier in v1.2 (single-DTE-per-POST
  granularity only; the ReversionDocumento schema exists but no v1.2 API
  operation is printed — structure owned by `02_dte-schema.md` FR-066,
  behavior by `06_anulacion-contingencia.md`); existence of later
  reversion/batch operations → OQ-007 (GOQ-51). (LB-004; LB-005; EVID-155,
  EVID-157)
- **GT-EINV-FR-177:** The provider adapter (saas) shall isolate every
  transport-specific concern — base URL, credentials, token
  acquisition/refresh cadence (boundary reference: 60-minute TTL), request
  serialization — behind a per-provider configuration profile, so that
  TotalDoc's actual contract (GOQ-39) can be wired without touching the
  certification pipeline; dev/test environment availability constraints
  (SAT dev environment business-hours only, 7:00–16:00 Mon–Fri) shall be
  surfaced in test-planning metadata. (LB-004; EVID-155)

### 3.3 Certification lifecycle, numbering authority & signatures

- **GT-EINV-FR-178:** The certification pipeline shall implement the 5-step
  lifecycle semantics: (1) emisor-built XML with firma de emisión → (2)
  certificador applies the SAT-provided validation rules (pre-certification
  rejection to emisor on failure) and assigns the authorization number +
  advanced certification signature → (3) certificador posts to SAT → (4)
  SAT returns a catalog-coded acuse (success/reject/with-errors) → (5) the
  acuse/reference is stored with the document as registration evidence.
  (LB-002; EVID-148)
- **GT-EINV-FR-179:** Rejection handling shall implement the responsibility
  split: reject/error NOT imputable to the certificador → surfaced to the
  emisor for correction and re-emission; reject/error imputable to the
  certificador → provider corrects and re-posts the SAME document (no
  re-numbering); the product shall map provider-returned codes onto these
  two handling paths and never regenerate a new document identity for
  provider-fault rejections. (LB-002; EVID-149)
- **GT-EINV-FR-180:** The *número de autorización* (authorization number)
  shall be a random UUID v4 assigned by the certificador — never by the
  emisor and never by the product; the pipeline shall only ingest and store
  the UUID returned via the provider (schema owned by
  `02_dte-schema.md` FR-045). (LB-003; EVID-153)
- **GT-EINV-FR-181:** Serie and Numero are post-certificación derivatives of
  the certificador-assigned UUID and shall be computed only from the
  returned UUID, never pre-assigned: Serie = the first 8 hexadecimal digits
  of the UUID left-to-right (worked example: UUID
  dbb51ae2-3a62-4437-b8e9-42ecfb761156 → Serie dbb51ae2, ≤20 chars);
  Numero = the decimal equivalent of the UUID's hex positions 9–16
  excluding hyphens (same example → 979518519, ≤15 digits). (LB-011;
  EVID-004)
- **GT-EINV-FR-182:** Both signatures follow one technical profile —
  XAdES-BES, RSA, SHA-256, two Signature elements with distinct IDs — with
  scopes: firma de emisión signs the DatosEmision element; firma de
  certificación (advanced, RPSC-provider cert) covers the DTE node;
  §II.G's "firma electrónica de emisión se aplica sobre el nodo de DTE"
  is read as a typo for firma de certificación (R12). The product shall
  verify both signatures on received certified DTEs and treat a DTE with
  either signature invalid as not certifiable/valid. (LB-003; EVID-152..154;
  R12)
- **GT-EINV-FR-183:** Emisor signing shall use the SAT-issued emitter
  certificate in production (per the third-party-certificador flavor,
  GT-EINV-FR-167 in `04_mandate-onboarding.md`); in dev/test the pipeline
  shall support self-generated RSA-2048 certificates (pkicloud service) so
  connector testing does not depend on SAT issuance; certificate validity
  is evaluated against the document's emission date (not reception date).
  (LB-003; EVID-152)
- **GT-EINV-FR-184:** Until OQ-007 (GOQ-51) resolves the acuse-signature
  ambiguity, the system shall assume the v1.2 SAT acuse is UNSIGNED
  (footnotes 6/9 defer the "firma electrónica simple" to a future version;
  p. 6 step 5's "irá firmado" read as forward-looking — R13) and shall
  store the acuse payload verbatim regardless of signature presence.
  (LB-004; EVID-155, EVID-157, EVID-148; R13)

### 3.4 Anulación transport, adenda & complementos

- **GT-EINV-FR-185:** Anulación transport semantics: an anulación is an
  operation EXTERNAL to the DTE — a logical annotation linked to the target
  DTE that never modifies a certified DTE in any case; the product shall
  never mutate a certified document (corrections are NC/ND or anulación),
  shall originate the anulación request with the emisor's signature over
  DatosGenerales plus the certificador's counter-signature, and shall store
  the anulación acuse alongside the original DTE. Windows, blockers and
  contingencia behavior: `06_anulacion-contingencia.md`. (LB-005; EVID-156,
  EVID-157)
- **GT-EINV-FR-186:** The *adenda* (addendum — emitter↔receiver private
  payload) is not part of DatosEmision nor the DTE, is unsigned, and MUST
  NOT reach SAT: submitting a DTE containing an Adenda element causes SAT
  rejection and requires resending without it. The certification pipeline
  shall strip/withhold adenda content from the document handed to the
  provider for SAT submission (or flag it for emitter/receiver-only
  delivery), and the provider-side stripping behavior is a GOQ-39 contract
  question. Adenda-side dispositivo carriage is explicitly open → OQ-002
  (GOQ-17). (LB-003; EVID-151)
- **GT-EINV-FR-187:** Complementos (complements) are part of the
  emisor-signed nodes, are mandatory whenever the Reglas scenario requires
  them, and are always sent to SAT (which may reject or report error when a
  required complement is missing — trigger matrix owned by
  `03_validation-rules.md` FR-134). (LB-003; EVID-151)

### 3.5 Result codes & error groups

- **GT-EINV-FR-188:** Every provider-relayed SAT result code shall be
  interpreted through the mensajes vocabulary: the 16_ error-group names
  (rechazo / informativos / secundarios / autenticación / anulaciones /
  éxito / genéricos) map onto catalogoMensajes 0.3.0 families (FEL_RCP 154,
  FEL_AUT 3, FEL_ASO 1, FEL_GEN 10, FEL_INF 6, FEL_ANU 22, FEL_SEC 15 —
  sidecar per GT-CAT-FR-013); the concrete name↔code mapping is open →
  OQ-008 (GOQ-52). Establishment-family codes FEL_RCP305/306/460/485/497
  are the runtime teeth of §3.7 (delivery contract per GT-EINV-FR-091 in
  `03_validation-rules.md`). (LB-007; LB-013; EVID-160, EVID-029)

### 3.6 Mini-RTU registry feed

- **GT-EINV-FR-189:** Registry data reaches the product through the
  provider via the SAT→certificador publish/subscribe mini-RTU feed: SAT
  PUSHES JSON deltas (Nit, afiliacionIVA, marcas[], establecimientos[],
  nombre, frases[]) to a certificador-provided URI (email fallback in an
  unspecified format); push cadence and the full delta schema are
  unspecified → OQ-007 (GOQ-51). The product shall consume this data as
  provider-delivered reference data, never fetch SAT directly.
  (LB-006; LB-007; EVID-158, EVID-159)
- **GT-EINV-FR-190:** Emitter master data shall be modeled as
  registry-driven, mutable configuration: afiliación transitions (e.g.
  GEN↔PEQ), establishment status changes and marcas traits arrive as delta
  updates and must take effect without re-deployment (marcas = non-blocking
  warnings per `03_validation-rules.md` FR-084; deny-new-docs interlock
  feed per GT-EINV-FR-147 in `04_mandate-onboarding.md`); receiver NIT/
  name/CUI validation semantics ultimately derive from the general
  taxpayer-data feed delivered via the provider; marcas traits
  (domicilio-no-localizado, omiso) are mini-RTU-fed non-blocking data.
  (LB-006; LB-007; LB-016; EVID-158, EVID-159, EVID-120)

### 3.7 Establishment model (D-GT9) — §establishment

*This subsection is the `05_certificador-interface.md §establishment`
anchor referenced by `02_dte-schema.md` and `03_validation-rules.md`.*
Pre-flagged for product-owner visibility (HANDOVER §5a/§9): the granularity
decision below is a product-scope ruling.

- **GT-EINV-FR-191:** Establishment identity in the DTE shall be exactly
  two fields: `Emisor/CodigoEstablecimiento` — an xs:positiveInteger
  1–9999, "el que aparece asignado por SAT en sus registros" (the number
  assigned by SAT in its records) — and `NombreComercial` (1..255, per
  tax records). There is NO taxpayer punto-de-emisión (point of emission)
  field in the FEL schema; the product shall not represent one.
  (LB-011; EVID-003)
- **GT-EINV-FR-192:** Odoo establishment mapping (D-GT9): sucursal /
  warehouse → CodigoEstablecimiento — each emission point resolves to one
  SAT-assigned active establishment code captured on the company
  establishment record (value capture per GT-EINV-FR-046 in
  `02_dte-schema.md`); the emitted DTE always carries the resolved code
  and its NombreComercial. (LB-011; EVID-003)
- **GT-EINV-FR-193:** POS / cash-register identity has NO FEL schema slot:
  the product shall not synthesize a punto-de-emisión or dispositivo code
  from POS session or cash-register data; POS-origin documents carry the
  establishment code of their configured sucursal/warehouse and nothing
  finer. (LB-011; EVID-004)
- **GT-EINV-FR-194:** `DatosGenerales/@Dispositivo` (enums APP / AV /
  APPVOZ) is "uso exclusivo para aplicación de SAT AV y SAT móvil (App)"
  (exclusive use of SAT's own AV/mobile apps): the dispositivo mapping is
  REJECTED as out of product scope — the product shall never emit @Dispositivo;
  whether TotalDoc would even accept an emitter-side dispositivo via adenda
  is open → OQ-002 (GOQ-17). (LB-011; EVID-004)
- **GT-EINV-FR-195:** `NumeroAcceso` (range 100000000–999999999) is an
  emisor-generated CONTINGENCIA accessor only — never a numbering
  substitute, never emitted on regular documents; contingencia mechanics
  (generation, aviso, re-send) are owned by `06_anulacion-contingencia.md`.
  (LB-011; EVID-004)
- **GT-EINV-FR-196:** `EmisionUbicacionTemporal` = SI (temporary-location
  emission flag) shall pair with frase tipo 9 escenario 14 — "Facturación
  en ubicación temporal (art. 30 Reglamento Ley del IVA)" (billing from a
  temporary location, IVA Law Regulation art. 30); the product shall offer
  the flag on the establishment/emission surface and drive the paired
  frase selection (frases matrix owned by `03_validation-rules.md`
  FR-105..FR-108). (LB-011; EVID-004, EVID-027)
- **GT-EINV-FR-197:** Establishment RTU teeth (validation semantics —
  rules owned by `03_validation-rules.md`): the establishment must be
  active in SAT's registry at the emission date (GT-EINV-FR-087; runtime
  FEL_RCP305 not-in-registry / FEL_RCP306 not-active), classification
  tables gate CIVA/CAIS/RECI/FESP emission (1703→1704, 2204→2224 maquila,
  887→963/1084/964, 886→899/965/966 — GT-EINV-FR-088/089; runtime
  FEL_RCP460), régimen primario/pecuario establishment pairs 3696/1696 +
  3694/885 (primario) and 3695/1696 + 3689/885 (pecuario), all
  FEPE-capable (GT-EINV-FR-090; runtime FEL_RCP485 RANT activity mismatch,
  FEL_RCP497 regime mismatch); runtime codes surface through this file's
  delivery contract per GT-EINV-FR-091. (LB-012; LB-013; LB-014; EVID-121,
  EVID-029, EVID-110(b))
- **GT-EINV-FR-198:** The establishment validation surface shall be fed by
  the mini-RTU establecimientos[] node — field set (JSON keys verbatim):
  zona, estado (activo/no activo), numero (the establishment number matching
  CodigoEstablecimiento), municipio, numeroCasa, apto, departamento, letra,
  nombre, calleAvenida, colonia — consumed via the provider feed
  (FR-189) and cached as dated reference data. (LB-006; LB-011; EVID-158)

### 3.8 Certificador authorization regime & roster (context, dated data)

- **GT-EINV-FR-199:** The authorization-regime context shall be modeled as
  reference data (certificador-side duties, not product duties): multiple
  simultaneous certificadores per emisor (AD art. 14); eligibility tiers
  Q1M working capital (individual) / Q1M paid-in capital (jurídica) / Q5M
  net fixed assets + 10 years existence (non-profit) (art. 15, 15-2020
  reform); ANNUAL renewal of authorization + security certificate (art. 15
  tail; 22_ §2.3f one-year validity); SAT-as-certificador for the free app
  and self-certifiers for own DTEs (art. 15); administrative contract +
  Q1M surety (arts. 17–18); SAT-published list (art. 19); 3-month
  withdrawal notice with no new emisors during wind-down (art. 20).
  (LB-008; EVID-042..045)
- **GT-EINV-FR-200:** The 22_ v2.1 regime development
  shall be recorded as provider-evaluation context with the versioning
  caveat (R14/GOQ-40): ISO/IEC 27001 security certificate, FIPS 140-2
  Level 2+ HSM key custody, ≤3 s certification of a 50-item DTE, ≥99.7%
  availability, 109-item security checklist, 14-month backup retention
  until SAT conciliation; these bind the certificador, not the product —
  they inform provider SLA expectations and the FR-203 retention
  reconciliation. (LB-009; EVID-096..104; R14)
- **GT-EINV-FR-201:** The certificador roster shall be stored as D15/D16
  dated data (snapshot-provenance rows, never silently overwritten): 18
  authorized certificadores as-of the 2026-08-18 snapshot (page dateModified
  2026-07-09); each row = certificador, NIT, website, Fecha de
  Autorización, Fecha de Renovación (annual-window semantics per 22_
  §2.3f — interpretation flagged); the empty "en proceso" pipeline table is
  recorded as all-dash (semantics open) → OQ-006 (GOQ-42). Provider
  selection (FR-172) and acreditación (GT-EINV-FR-166) validate against
  this registry. (LB-009; LB-010; EVID-104, EVID-106..108)
- **GT-EINV-FR-202:** The product shall carry a provider-continuity watch
  on the Aug–Dec 2026 renewal cluster — DIGIFACT 23/08/2026, INFILE
  31/10/2026, FELCON (FORMULARIOS CONTINUOS DE CENTRO AMERICA) 20/11/2026,
  CARI 22/11/2026, AINNOVA / INFORUM / MEGAPRINT 23/11/2026, **TotalDoc
  (GRUPO CDS, product default) 02/12/2026**, TEKRA 21/12/2026 — surfacing
  the default provider's renewal date on the provider config, and requiring
  a roster re-check at the milestone → OQ-001 (GOQ-03). (LB-010; EVID-107)
- **GT-EINV-FR-203:** Retention reconciliation (cross-topic pointer):
  the certificador's 14-month backup floor ("hasta conciliación" — until
  SAT declares conciliation) is PROVIDER-side and shall not be modeled as
  the emitter's duty; emitter-side retention of certified XML + acuses
  runs to the Código Tributario prescription period (AD art. 21) with the
  LIBRO I books/records duties owned by the taxation wave — full
  reconciliation → OQ-005 (GOQ-41). (LB-009; LB-015; EVID-103, EVID-046)

## 4. Data Model

**Establishment entity** (D-GT9; value capture per `02_dte-schema.md`
FR-046 — this file owns the model and the registry feed):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.establishment | codigo_establecimiento | integer 1–9999 | SAT-assigned (RTU/Agencia Virtual), unique per company | FR-191, FR-192; EVID-003 |
| l10n_gt.establishment | nombre_comercial | char(255) | per tax records | FR-191; EVID-003 |
| l10n_gt.establishment | estado | char | A / inactive (mini-RTU establecimientos[].estado) | FR-198, FR-197; EVID-158 |
| l10n_gt.establishment | ubicacion_temporal | boolean | drives EmisionUbicacionTemporal=SI + frase 9-esc-14 pairing | FR-196; EVID-004, EVID-027 |
| l10n_gt.establishment | mini-RTU address cache | char fields | zona, municipio, numeroCasa, apto, departamento, letra, nombre, calleAvenida, colonia (dated cache) | FR-198; EVID-158/159 |
| l10n_gt.establishment | sucursal/warehouse mapping | many2one stock.warehouse / res.company branch | D-GT9: sucursal/warehouse → CodigoEstablecimiento; POS/cash-register → none | FR-192, FR-193; EVID-003/004 |
| account.move (certified DTE) | numero_autorizacion (UUID v4) / serie / numero / numero_acceso | char(36) / char(8) / char(15) / integer 9-digit | UUID+derivatives certificador-assigned post-certificación; NumeroAcceso contingencia-only | FR-180, FR-181, FR-195; EVID-153/004 |
| account.move (certified DTE) | acuse_ref / adenda_ref | binary + boolean | SAT acuse stored verbatim; adenda held out of the SAT-bound document | FR-178, FR-184, FR-186; EVID-148/155/151 |

**Mini-RTU delta payload** (SAT→certificador push; product consumes via
provider — reference keys verbatim from the printed example):

| Node | Keys | Type | Notes |
|------|------|------|-------|
| Cabecera.minirtu[] | Nit | string | emitter NIT (example "800000000011") |
| | afiliacionIVA | enum string | e.g. "PEQ" — AfiliacionIVA regimes |
| | marcas[] | array | {código, fecha, valor} — non-blocking warnings |
| | establecimientos[] | array | {zona, estado, numero, municipio, numeroCasa, apto, departamento, letra, nombre, calleAvenida, colonia} — feeds FR-197/198 |
| | nombre | string | [sic — example concatenates the NIT into nombre] |
| | frases[] | array | {escenario, tipo, fechaResolucion, numeroResolucion} — registry-driven frases |

**Certificador roster** (31_ snapshot 2026-08-18 — D15 dated data; seed
rows; "Renovación" = annual-window end per 22_ §2.3f, interpretation
flagged GOQ-42):

| Certificador | NIT | Sitio web | Autorización | Renovación |
|---|---|---|---|---|
| AINNOVA S.A. | 5640773-4 | www.guatefacturas.com | 23/11/2018 | 23/11/2026 |
| CÁMARA DE COMERCIO DE GUATEMALA | 351598 | www.ccg.gt | 24/02/2021 | 24/02/2027 |
| CARI LATINOAMÉRICA, S.A. | 96941243 | www.cari.lat | 22/11/2022 | 22/11/2026 |
| COFIDI, S.A. | 62469045 | www.cofidi.com.gt | 03/07/2019 | 03/07/2027 |
| COMERCIALIZADORA GUATEMALTECA MAYORISTA DE ELECTRICIDAD, S.A. | 37156616 | portal.fel.guatemel.com.gt | 21/02/2020 | 21/02/2027 |
| CONTAP, S.A. | 98978802 | www.facturas.gt | 30/04/2020 | 30/04/2027 |
| CORPOSISTEMAS, S.A. | 108151654 | www.corposistemasgt.com | 06/04/2021 | 06/04/2027 |
| DIGIFACT SERVICIOS, S. A. | 77454820 | www.digifact.com.gt | 23/08/2019 | 23/08/2026 |
| FORMULARIOS CONTINUOS DE CENTRO AMERICA, S A. (FELCON) | 4150686 | www.eforcon.com | 20/11/2019 | 20/11/2026 |
| G4S DOCUMENTA, S. A. | 60010207 | www.documenta.com.gt | 11/03/2019 | 11/03/2027 |
| GOM SOLUTIONS, S.A. | 95189416 | www.gomsolutions.com | 12/03/2020 | 12/03/2027 |
| **GRUPO CDS S.A. (= TotalDoc, product default)** | **107902281** | www.grupocds.com.gt | **02/12/2021** | **02/12/2026** |
| INTEGRAL ADMINISTRADORA DE RECURSOS Y SERVICIOS EMPRESARIALES, S.A | 92721788 | www.indrese.com | 17/01/2020 | 17/01/2027 |
| INFILE, S. A. | 12521337 | www.infile.com | 29/10/2018 | 31/10/2026 |
| INFORUM CONSULTING, S. A. | 43430775 | www.edxsolutions.gt | 23/11/2018 | 23/11/2026 |
| MEGAPRINT, S. A. | 50510231 | www.megaprint.com.gt | 23/11/2018 | 23/11/2026 |
| OPERADORA ECONÓMICA, S.A. | 64281167 | www.ecofactura.com.gt | 13/02/2020 | 13/02/2027 |
| TEKRA, S. A. | 107346834 | www.tekra.com.gt | 21/12/2020 | 21/12/2026 |

**16_ v1.2 SAT-side operation inventory** (boundary reference data —
dev/desa only, NOT product endpoints; production base URL not printed):

| Operation (verbatim) | Direction | Purpose | Notes |
|---|---|---|---|
| GET https://api.desa.sat.gob.gt/test | certificador → SAT | availability check | page returns "OK" |
| GET https://api.desa.sat.gob.gt/getToken | certificador → SAT | basic-auth → token | TTL 60 minutes |
| POST https://api.desa.sat.gob.gt/postFactura | certificador → SAT | submit one certified DTE XML | header "Access_Token" [sic]; single DTE per POST |
| POST https://api.desa.sat.gob.gt/postAnulacionDTE | certificador → SAT | submit AnulacionDocumento XML | same auth pattern; acuse fn. 9 |
| Delta push (mini-RTU) | SAT → certificador URI | registry deltas (JSON above) | webhook or email fallback |
| https://cat.desa.sat.gob.gt/xsd/alfa + /catalogos/alfa | SAT → all (pull) | XSD + catalog distribution | alfa = dev; prod channel per fn. 3 |

**Error-group mapping** (16_ names ↔ catalogoMensajes 0.3.0 families;
concrete code mapping open — GOQ-52):

| 16_ group name | catalogoMensajes family | Count | Established anchor codes |
|---|---|---|---|
| rechazo | FEL_RCP | 154 | 000 success ("Se Devuelve un FaceId"); 305/306/460/485/497 establishment |
| informativos | FEL_INF | 6 | — |
| secundarios | FEL_SEC | 15 | 500/502 calculation |
| autenticación | FEL_AUT | 3 | — |
| anulaciones | FEL_ANU | 22 | 368–371 anulación mismatches |
| éxito | FEL_RCP000 (within FEL_RCP) | 1 | — |
| genéricos | FEL_GEN | 10 | 100/102 XSD schema |
| (no 16_ name printed) | FEL_ASO | 1 | unmapped family — GOQ-52 |

## 5. Odoo Mapping

Layer split for this file: `saas` = certificador API client + XML
certification pipeline (submission, signature verification, UUID/Serie/
Numero ingestion, result-code mapping, mini-RTU consumption); `odoo` =
establishment/journal configuration and document-state surfaces (acuse
display, Serie/Numero fields, acreditación wizard); `shared` = roster and
authorization dated data + the mensajes code table both sides must honor.
Model names are stable across Odoo 17/18/19/20; no version-specific
behavior is required by this file. Dated rows (roster, registry cache)
follow D15/D16: append-only, snapshot-on-write, provenance per row.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-171 | saas | — | provider adapter boundary | Architecture rule D-GT5/D-GT6: SAT-facing traffic only through certificador adapter |
| FR-172 | odoo | res.company | certificador provider profile (default TotalDoc) | Selection UI on company; roster validation shared (FR-201); multi-certificador per FR-166 (04 file) |
| FR-173 | saas | — | provider config profile | TotalDoc contract wired at W6 (GOQ-39); 16_ kept as reference data only |
| FR-174 | shared | — | LB-citation guard metadata | Guard rides shared citation layer: 16_ never cited for schema structure/URLs (R11) |
| FR-175 | shared | — | op-inventory reference table | §4 table seeds the reference data; dev-only flag; GOQ-51 watch |
| FR-176 | shared | — | op-inventory reference table | No batch/consulta/reversion assumption recorded with the inventory |
| FR-177 | saas | — | base URL, credentials, token TTL config | Per-provider profile; 60-min boundary reference; dev-hours surfaced in test metadata |
| FR-178 | saas | account.move | acuse_ref, state transitions | Lifecycle orchestration saas-side; odoo displays acuse + state |
| FR-179 | saas | account.move | rejection-handling path | Two-path mapping; emisor-fix path surfaced odoo-side as correction wizard |
| FR-180 | saas | account.move | numero_autorizacion | Ingest-only; never generated client-side (mirror of FR-045 schema) |
| FR-181 | saas | account.move | serie, numero | Derived from returned UUID only (post-certificación); stored + displayed |
| FR-182 | saas | — | signature verification | Both signatures verified core-side; canonical Signature IDs from XSD (02 file) |
| FR-183 | saas | res.company (firma credentials) | signing cert profile | Prod = SAT-issued (FR-167, 04 file); dev = self-generated RSA-2048; validity vs emission date |
| FR-184 | saas | account.move | acuse payload | Unsigned-assumption (R13) recorded; verbatim storage either way |
| FR-185 | saas | account.move | anulación request/acuse | Immutability enforced core-side; odoo void-flow UI originates request; behavior = 06 file |
| FR-186 | saas | account.move | adenda_ref | Strip/withhold before SAT-bound submission; provider stripping = GOQ-39; adenda dispositivo = GOQ-17 |
| FR-187 | saas | account.move | complement attachments | Mandatory-complement check rides the 03-file matrix (FR-134) |
| FR-188 | shared | — | mensajes code table | Family mapping table (§4) shared; concrete mapping GOQ-52; sidecar GT-CAT-FR-013 |
| FR-189 | saas | — | mini-RTU consumer | Feed consumed core-side via provider; cadence/schema open (GOQ-51) |
| FR-190 | shared | res.company | afiliacion/marcas config | Registry-driven dated config; odoo surfaces transitions; feed also drives FR-147 (04 file) |
| FR-191 | odoo | l10n_gt.establishment | codigo, nombre_comercial | The only establishment identity; no punto-de-emisión field exists (D-GT9) |
| FR-192 | odoo | l10n_gt.establishment + stock.warehouse | sucursal/warehouse mapping | D-GT9 mapping rule; value capture per FR-046 (02 file) |
| FR-193 | odoo | pos.session / cash register | — (no mapping) | Explicit non-mapping recorded; POS docs inherit establishment code |
| FR-194 | odoo | — | — (mapping rejected) | @Dispositivo SAT-apps-exclusive; product never emits it; GOQ-17 open |
| FR-195 | odoo | account.move | numero_acceso (contingencia-only) | Range 100000000–999999999; mechanics owned by 06 file |
| FR-196 | odoo | l10n_gt.establishment + account.move | ubicacion_temporal flag | Pairs with frase tipo 9 esc 14; frase matrix saas-side (03 file FR-105..108) |
| FR-197 | shared | establishment registry cache | estado, classification pairs | Gate rules owned by 03 file (FR-087..091); runtime codes delivered via FR-091 |
| FR-198 | shared | establishment registry cache | mini-RTU establecimientos[] fields | Dated cache rows; keys verbatim §4 |
| FR-199 | shared | l10n_gt.certificador (regime reference) | eligibility/renewal metadata | Context data; certificador-side duties |
| FR-200 | shared | l10n_gt.certificador | SLA/security metadata | Provider-evaluation context; R14/GOQ-40 versioning caveat recorded |
| FR-201 | shared | l10n_gt.certificador | roster dated rows | 18 rows snapshot 2026-08-18; D15/D16 append-only; acreditación UI odoo-side (FR-166) |
| FR-202 | odoo | res.company (provider profile) | renewal watch flag | Default-provider renewal 02/12/2026 surfaced; roster re-check at milestone (GOQ-03) |
| FR-203 | shared | — | retention metadata | 14-month = provider-side; emitter retention = CT prescription (LB-015); GOQ-41 reconcile |

## 6. Acceptance Criteria

- **AC-001:** Given a certified DTE returned via the provider with UUID
  dbb51ae2-3a62-4437-b8e9-42ecfb761156, when parsed, then Serie =
  dbb51ae2 and Numero = 979518519, both stored read-only and never
  regenerated (FR-180, FR-181).
- **AC-002:** Given a document submitted for certification with adenda
  content inside the SAT-bound XML, when the pipeline runs, then the
  adenda is withheld/stripped before provider submission and no Adenda
  element is present in the certified DTE (FR-186).
- **AC-003:** Given a provider rejection classified as
  certificador-imputable, when handled, then the same document (same
  UUID/identity) is re-posted after provider correction and no new
  document identity is created (FR-179).
- **AC-004:** Given an establishment record with codigo 0 or 10000, when
  saved, then validation rejects it (bounds 1–9999); given codigo 47 with
  nombre_comercial "EL AGAVE", then the emitted DTE carries
  CodigoEstablecimiento 47 and that NombreComercial (FR-191, FR-192).
- **AC-005:** Given a POS-session-originated invoice, when compiled, then
  the DTE carries only the sucursal's establishment code and no
  dispositivo or punto-de-emisión attribute appears anywhere in the XML
  (FR-193, FR-194).
- **AC-006:** Given a configuration attempt to map a cash register to a
  @Dispositivo value, when saved, then the mapping is rejected with the
  SAT-apps-exclusive explanation (FR-194; GOQ-17 recorded open).
- **AC-007:** Given an establishment flagged ubicacion_temporal, when a
  document is emitted, then EmisionUbicacionTemporal=SI and the frase
  selection includes tipo 9 escenario 14 "Facturación en ubicación
  temporal (art. 30 Reglamento Ley del IVA)" (FR-196).
- **AC-008:** Given an establishment inactive at the emission date in the
  registry cache, when certification is attempted, then the surfaced
  runtime mensaje is FEL_RCP306 (delivered through this interface;
  gate per GT-EINV-FR-087/091 in the 03 file) (FR-197, FR-188).
- **AC-009:** Given the provider profile rendered for TotalDoc, when
  inspected, then the roster row shows GRUPO CDS S.A., NIT 107902281,
  window 02/12/2021 → 02/12/2026 with a renewal-watch flag dated
  2026-12-02 and the Aug–Dec 2026 cluster visible (FR-201, FR-202).
- **AC-010:** Given the roster registry, when a future snapshot is
  imported, then prior rows are retained as dated history (append-only)
  and no earlier snapshot is overwritten (FR-201).
- **AC-011:** Given the operation-inventory reference data, when
  inspected, then every URL is flagged dev/desa-only and no production
  endpoint is asserted anywhere in the product (FR-175, FR-174).
- **AC-012:** Given a token older than the configured TTL, when the next
  submission runs, then the adapter refreshes the token transparently and
  the document is submitted exactly once (FR-177).
- **AC-013:** Given any SAT interaction path in the codebase, when
  audited, then none calls api.desa.sat.gob.gt (or any SAT endpoint)
  directly — all traffic passes the provider adapter (FR-171).
- **AC-014:** Given a certified DTE, when either signature (emisión or
  certificación) verifies as invalid, then the document is treated as not
  valid and the failure surfaces through the result-code path (FR-182).
- **AC-015:** Given a contingencia-mode document, then it carries
  NumeroAcceso in 100000000–999999999 and no Serie/Numero until
  post-certificación re-submission assigns them (FR-195, FR-181).

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C /
§C.1); question text verbatim from the register where printed. This file
OWNS GOQ-03, GOQ-17, GOQ-39, GOQ-40, GOQ-41, GOQ-42, GOQ-51 and GOQ-52.
Kin ids referenced inline only: GOQ-02 (channel umbrella, catalogs-owned)
for schema-drift reads of LB-011.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-03 (owned): "TotalDoc/GRUPO CDS authorization renewal 02/12/2026 (Aug-Dec 2026 renewal cluster: DIGIFACT 23/08, INFILE 31/10, FELCON 20/11, CARI 22/11, AINNOVA/INFORUM/MEGAPRINT 23/11, TEKRA 21/12) — re-check roster 31_ at milestone." Guards FR-172/FR-202 and the default-provider continuity of every FR in §3. | no | GT synthesis wave S-GT1 → W6 partner ask (roster re-check at milestone) | open |
| OQ-002 | GOQ-17 (owned): "Does TotalDoc accept an emitter-side dispositivo/punto-de-emisión identifier (e.g. via adenda), or is CodigoEstablecimiento the only establishment granularity?" FR-193/FR-194 ship the schema-grounded ruling (no slot; mapping rejected); the adenda-side question stays open. | no | GT synthesis wave S-GT1 → W6 partner ask (TotalDoc) | open |
| OQ-003 | GOQ-39 (owned): "Provider specifics (non-government): emisor firma key format for third-party certificadores, TotalDoc test NITs/homologation flow, catalog sync — pull from TotalDoc docs at W6 partner access." Blocks the concrete adapter profile of FR-173/FR-177 and the FR-186 provider-stripping question. | no | GT synthesis wave S-GT1 → W6 partner access (TotalDoc docs) | open |
| OQ-004 | GOQ-40 (owned): "22_ versioning: v2.1 footers alternate 10-07-2024 / 03-09-2018; p.43 of 43 missing; v2.2+ on portal?" Affects the confidence of the FR-200 context rows (SLA/security baselines) — R14 working rule: treat v2.1 as current. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT portal) | open |
| OQ-005 | GOQ-41 (owned): "Certificador 14-month backup retention ("hasta conciliación") vs emitter-side retention duties (CT/LIBRO I) — reconcile for the Odoo archiving requirement." FR-203 records the separation; the archiving requirement itself lands with the taxation wave (CT/LIBRO I retention). | no | GT synthesis wave S-GT1 → S-GT2 taxation wave + W6 partner ask | open |
| OQ-006 | GOQ-42 (owned): "Roster 31_ hygiene: emails obfuscated by extraction; "Fecha de Renovación" semantics (window-end vs filing date); all-dash "en proceso" row meaning." FR-201 ships the window-end interpretation flagged. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT portal re-fetch) | open |
| OQ-007 | GOQ-51 (owned): "16_ API currency: are getToken/postFactura/postAnulacionDTE still the operative op names; production base URL (none printed); acuse signed? + field structure (images only); Access_Token spelling; shared-token credential model; reversion/batch ops existence; pub/sub cadence + full delta schema." Guards FR-175..FR-177, FR-184, FR-189; working assumptions shipped (v1.2 ops as boundary reference; acuse assumed unsigned per R13). | no | GT synthesis wave S-GT1 → W6 partner ask (TotalDoc/SAT) | open |
| OQ-008 | GOQ-52 (owned): "Map 16_ error-group names (rechazo/informativos/secundarios/autenticación/anulaciones/éxito/genéricos) to concrete catalogoMensajes codes (families captured in EVID-029)." FR-188 ships the family-level table (§4); concrete code mapping open. | no | GT synthesis wave S-GT1 → W6 partner ask (TotalDoc) | open |
