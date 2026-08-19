# Evidence — 17_-22_ + 31_ FEL manuals, test cases, certificador roster (W-GT1)

Source: `gt/.extractions/18_FEL_guia_requisitos_minimos.pdf.txt` (8pp), `19_FEL_contingencia.pdf.txt` (5pp), `20_FEL_anulacion_manual.pdf.txt` (5pp), `21_FEL_firma_electronica_manual.pdf.txt` (12pp), `22_FEL_autorizacion_certificador.pdf.txt` (42pp extracted; internal pagination "de 43"), `31_certificadores_dte_snapshot_2026-08-18.html`, `17_casos_de_prueba/*.txt` (25 files). Read: 2026-08-19. 17_/19_ read as 2018-vintage historical (supersession flags inline). PDF text extraction introduces spacing/line-break artifacts; verbatim quotes rejoin line-wraps silently, `[sic]` marks substantive defects.

---

## EVID-081 — 18_ identity: it is the graphic-representation requirements guide, NOT a software-certification requirements doc
- **Loc:** 18_FEL_guia_requisitos_minimos.pdf.txt, p. 1–2 (=== PAGE 1/2 ===), title + section head
- **Verbatim:** "Guía de requisitos (representación gráfica) / Documentos Tributarios Electrónicos (DTE) / Régimen de Factura Electrónica en Línea (FEL)" … "Requisitos que deben mostrarse en la representación gráfica de los Documentos Tributarios Electrónicos (DTE) 1. Tipo de documento 2. Datos del emisor 3. Datos del receptor 4. Datos de la autorización 5. Descripción de los bienes y servicios 6. Frases 7. Complementos 8. Datos del Certificador 9. Código QR"
- **Gloss:** The file labeled "guía requisitos mínimos (software certification requirements)" is in fact SAT's guide to what must be **displayed in the printed/graphic representation** of a DTE — 9 numbered requirement areas. It binds emisors' printed/PDF output, not certificador software approval (that is 22_).
- **Candidate CRs:** printed DTE representation must contain the 9 areas: document type; emitter data; receiver data; authorization data; goods/services description; frases; complementos; certificador name+NIT; QR code.
- **Topics:** e-invoicing; graphic representation; print/PDF output.
- **Doubts/xref:** No version/date string anywhere in 18_ (undated guide) — currency unknown; check current portal version and the 20-type count vs Reglas v1.7.10 catalogs (see EVID-082, OQ-2).

## EVID-082 — 18_ the twenty DTE types (as of the guide's unspecified date)
- **Loc:** 18_, p. 3, section "Tipo de documento"
- **Verbatim:** "El tipo de documento que corresponda según el régimen del contribuyente, actualmente existenveinte tipos: [sic: existenveinte] 1. Factura 2. Factura especial 3. Factura cambiaria 4. Factura de Pequeño Contribuyente 5. Factura cambiaria de Pequeño Contribuyente 6. Factura Contribuyente Agropecuario 7. Factura Cambiaria Contribuyente Agropecuario 8. Factura Pequeño Contribuyente Régimen Electrónico 9. Factura Cambiaria Pequeño Contribuyente Régimen Electrónico 10. Factura Contribuyente Agropecuario Régimen Electrónico Especial 11. Factura Cambiaria Contribuyente Agropecuario Régimen Electrónico Especial 12. Recibo 13. Recibo por Donación 14. Nota de crédito 15. Nota de débito 16. Nota de abono 17. Constancia de Exención de IVA 18. Constancia de Adquisición de Insumos y Servicios 19. Recibo de Anticipos 20. Nota de Envío"
- **Gloss:** Full enumeration of DTE types for display. Includes the Régimen Electrónico types (8–11), which post-date 2018 (small-taxpayer electronic regimes ~2021-2023) → guide is later than 2018 despite being undated.
- **Candidate CRs:** graphic representation must label the DTE with the correct one of the 20 document types.
- **Topics:** e-invoicing; document types; catalogs.
- **Doubts/xref:** "actualmente" with no date — anchor is dangling; cross-check count against Reglas v1.7.10 / catálogo de tipos de DTE (OQ-2).

## EVID-083 — 18_ mandatory authorization block; Número de Acceso shown only for contingencia "por casos fortuitos"; QR optional for third-party certificadores
- **Loc:** 18_, p. 4 ("Datos de la autorización", "Datos del receptor") and p. 6 ("Código QR", "Datos del Certificador")
- **Verbatim:** "a) Número de autorización b) Serie del documento c) Número del documento d) Número de acceso (aplica solo para documentos emitidos en contingencia por casos fortuitos) e) Fecha y hora de emisión (la hora es -Opcional-) f) Fecha y hora de certificación (autorizacióndel documento) -Opcional- g) Tipo de moneda aplicada al documento" … "Nombre y NIT de la entidad que certificóel documento (SAT o un certificador autorizado)" … "Direcciona al sitio web de la SAT,a efecto de comprobar que el documento es válido. -Opcional- para documentos generados con otros certificadores."
- **Gloss:** Authorization block on the printed DTE: auth number, series, document number, currency; emission date/time (time optional) and certification date/time optional. Número de Acceso appears **only** on contingency documents. Certificador name+NIT mandatory on print. QR points to SAT verification and is optional when another certificador (not SAT) generated the document.
- **Candidate CRs:** print auth block (número de autorización, serie, número, moneda; emisión date, hora optional); print Número de Acceso on contingency DTEs instead of auth number; print certificador name+NIT; QR optional for non-SAT certificadores.
- **Topics:** e-invoicing; graphic representation; contingencia; QR.
- **Doubts/xref:** 18_ says Número de Acceso is for "contingencia **por casos fortuitos**" while 19_ defines contingencia as connectivity problems (EVID-086) — SAT doctrine has both categories (conectividad vs casos fortuitos/SAT unavailability); 2018 19_ text covers only conectividad (OQ-4).

## EVID-084 — 18_ line-item content: unit price INCLUDES IVA; 8 taxes enumerated (IVA, IDP, ITH, ITP, TDP, IFB, MUN, TAP)
- **Loc:** 18_, p. 5, "Descripción de los bienes y servicios"
- **Verbatim:** "e) Precio unitario incluyendo el IVA (conlas excepciones correspondientes: pequeñocontribuyente, ventas exentas o no afectas). [sic spacing] f) Descuentos (si corresponde) g) Totalde ítem (cantidad de bienes o servicios multiplicado por el precio unitario) h) Impuestos cargados al documento: i. IVA … ii. IDP Impuesto a la Distribución de Petróleo … iii. ITH Impuesto al Turismo Hospedaje … iv. ITP Impuesto al Turismo Pasaje … v. TDP Impuesto alTimbre dePrensa … vi. IFB Impuesto a Favordel Cuerpo Voluntariode Bomberos … vii. MUN TasaMunicipal … viii.TAP Tarifa Portuaria."
- **Gloss:** Display rule: unit price shown **IVA-inclusive** (except pequeño contribuyente / exempt sales); item total = quantity × unit price; taxes charged are listed with their codes. Matches the 17_ per-tax test-case family (IVA/IDP/ITH/ITP/TDP/IFB/MUN).
- **Candidate CRs:** print unit prices IVA-inclusive by default; print per-item quantity, description, discounts, item total; show each tax charged with code.
- **Topics:** e-invoicing; graphic representation; taxes; pricing.
- **Doubts/xref:** none beyond 18_ being undated (OQ-2).

## EVID-085 — 18_ adendas allowed only via certificadores (not in free SAT app); complementos enumerated
- **Loc:** 18_, p. 6 "Complementos" and p. 7 "“Adendas“"
- **Verbatim:** "existen los siguientes complementos: a) Abonos de factura cambiaria y factura cambiara de pequeño contribuyente b) Retenciones de factura especial c) Exportaciones d) Referencia de notas de débito o crédito" … "Es importante aclarar que en los servicios de emisión gratuita FEL de la Agencia Virtual y App FEL, actualmente no es posible agregar “adendas” a los documentos, únicamente en el servicio que prestan los terceros autorizados (Certificadores)."
- **Gloss:** Complement types for display; adendas (non-fiscal commercial data — call detail, meter readings, internal refs, ads, customer codes) can only be attached when certifying through third-party certificadores.
- **Candidate CRs:** support printing complement data; if Odoo acts via a certificador, adendas are feasible; not a government constraint on Odoo itself but on the free SAT channel.
- **Topics:** e-invoicing; graphic representation; adendas; complements.
- **Doubts/xref:** whether adendas survive in XML (dAdenda) under Reglas v1.7.10 unchanged — xref 15_.

## EVID-086 — 19_ identity & vintage: Mayo 2018 contingency procedure under AD SAT 13-2018; contingencia defined as connectivity failure only
- **Loc:** 19_FEL_contingencia.pdf.txt, p. 1, 3 (headers "Mayo de 2018" on every page), §1.2
- **Verbatim:** "Procedimiento de Emisión de Documentos en Contingencia — Factura Electrónica en Línea (Acuerdo de Directorio SAT 13-2018)" … "Se define como contingencia la situación por la cual un Emisor no puede obtener de forma inmediata la certificación de sus documentos a que se refiere el Artículo 5 del Acuerdo de Directorio SAT No. 13-2018, por problemas de conectividad."
- **Gloss:** HISTORICAL (2018-05). Contingency = emitter cannot obtain immediate certification due to **connectivity problems**. Part of the FEL technical documentation ("El presente documento forma parte de la Documentación Técnica del Régimen FEL").
- **Candidate CRs:** none standalone; frames the contingency mechanics in EVID-087–090.
- **Topics:** e-invoicing; contingencia; historical.
- **Doubts/xref:** SUPERSESSION FLAG: current regime (Reglas y validaciones v1.7.10, Feb-2025) and later SAT doctrine distinguish contingencia por conectividad vs por casos fortuitos (SAT unavailability — see 18_ EVID-083) and may redefine windows/deadlines; every rule below must be checked against v1.7.10 before use (OQ-4).

## EVID-087 — 19_ alternatives before using contingency mode (free SAT app, self-certifier, second certificador, contingency emission)
- **Loc:** 19_, p. 3, §1.3 "ALTERNATIVAS"
- **Verbatim:** "a) Utilizar la aplicación web gratuita que la SAT pondrá a disposición a través de su Agencia Virtual, en la cual un contribuyente podrá emitir DTE sin restricciones … b) Solicitar su autorización para ser Certificador de sus propios documentos tributarios electrónicos … c) Acreditar más de un Certificador. d) Emitir los DTE en modalidad de contingencia, tomando en cuenta lo determinado en este documento."
- **Gloss:** SAT's stated fallback ladder; accrediting more than one certificador is an explicitly sanctioned mitigation (relevant to product default-provider risk, D-GT5/6).
- **Candidate CRs:** operational guidance only; support for multiple accredited certificadores is taxpayer-side behavior.
- **Topics:** e-invoicing; contingencia; certificador accreditation.
- **Doubts/xref:** none.

## EVID-088 — 19_ contingency emission mechanics: "Documento en Contingencia" text, Número de Acceso per Reglas/XSD GT_Documento, print replaces auth number, receiver retrieves on SAT site
- **Loc:** 19_, p. 4, §1.4
- **Verbatim:** "El Emisor deberá emitir y entregar sus Documentos con el texto “Documento en Contingencia”, adicionalmente a los datos obligatorios que debe incluir toda factura, deberá consignar un “Número de Acceso”, el cual se define como formarlo [sic] en el documento “Reglas y Validaciones”, debiendo cumplir con el formato que determina el esquema XSD: GT_Documento, en su versión vigente." … "El Emisor será directamente responsable de verificar que el nuevo documento creado cumpla con las reglas y características de un DTE, para evitar que el mismo sea rechazado por el Certificador cuando llegue el momento de transmitirlo para su Autorización." … "La representación gráfica de los documentos emitidos en contingencia no contendrá el número de autorización del Certificador, en su lugar deberá contener el “Número de Acceso” para que el receptor pueda obtener el DTE Certificado en el portal de la SAT, por lo que también deberá incluir el texto “Emisión en contingencia, obtenga el DTE Certificado en el sitio www.sat.gob.gt/efactura”."
- **Gloss:** Contingency DTE is issued without prior certification: emitter generates Número de Acceso (format defined in Reglas y validaciones / XSD GT_Documento), prints "Documento en Contingencia" + Número de Acceso + the retrieval notice instead of the certificador auth number. Emisor bears responsibility for pre-validity.
- **Candidate CRs:** contingency mode must: (1) mark document "Documento en Contingencia"; (2) generate/consign Número de Acceso; (3) print it in place of auth number with the SAT retrieval text; (4) not reject later when transmitting for certification.
- **Topics:** e-invoicing; contingencia; Número de Acceso; graphic representation.
- **Doubts/xref:** SUPERSESSION FLAGS: (a) Número de Acceso construction rules must come from **v1.7.10**, not the 2018 Reglas; (b) URL "www.sat.gob.gt/efactura" may be stale vs current portal; (c) whether the exact legend text changed (OQ-4, OQ-5).

## EVID-089 — 19_ post-contingency duties: Aviso de Contingencia in Agencia Virtual (5 fields), then immediately transmit XMLs including Número de Acceso
- **Loc:** 19_, p. 4, §1.4 (end)
- **Verbatim:** "Al finalizar la contingencia el Emisor deberá dar aviso a la SAT, haciendo el registro correspondiente a través del aplicativo disponible en su Agencia Virtual SAT, en el apartado de Factura Electrónica en Línea, Aviso de Contingencia; consignando la siguiente información: Fecha y hora de inicio de la contingencia; Fecha y hora en que finalizó la contingencia; Número de establecimiento; Motivo de la contingencia; Cantidad de documentos emitidos" … "Inmediatamente deberá enviar los documentos a su Certificador, incluyendo en los archivos XML el campo “Número de Acceso” que generó." … "La información de la contingencia servirá para que los servicios de la SAT no rechacen los documentos por llegar fuera del plazo establecido."
- **Gloss:** After the outage: (1) file "Aviso de Contingencia" in Agencia Virtual with the 5 fields; (2) immediately send the DTEs to the certificador with Número de Acceso embedded in XML. The notice prevents SAT rejecting the batch as late. **No numeric deadline is stated** — "el plazo establecido" is deferred to the Reglas.
- **Candidate CRs:** contingency workflow: queue DTEs offline; on reconnection file the Aviso (start/end timestamps, establecimiento no., motive, count) and retransmit XMLs carrying Número de Acceso.
- **Topics:** e-invoicing; contingencia; deadlines; Agencia Virtual.
- **Doubts/xref:** SUPERSESSION FLAG: the numeric regularization window (days after contingency end / vs certification date) is defined in Reglas — verify against v1.7.10 §validation of Fecha de emisión/contingencia; 2018 doc gives none (OQ-4).

## EVID-090 — 19_ restrictions: self-certifiers must use a third party for contingency docs; emitter e-signature must appear in the graphic representation
- **Loc:** 19_, p. 5, §1.5 "RESTRICCIONES"
- **Verbatim:** "Si el Emisor es a su vez Certificador de sus propios documentos, deberá utilizar el servicio de un tercero para la certificación de los documentos emitidos en contingencia." … "Debe incluirse la firma electrónica del Emisor en la representación gráfica."
- **Gloss:** A self-certifying emitter cannot certify its own contingency DTEs. Contingency prints must include the emitter's electronic signature (in the graphic representation).
- **Candidate CRs:** contingency print must include emisor firma electrónica.
- **Topics:** e-invoicing; contingencia; firma electrónica; graphic representation.
- **Doubts/xref:** whether "firma electrónica del Emisor en la representación gráfica" still required/current form (string? QR? image) — check v1.7.10 and current SAT guidance (OQ-4).

## EVID-091 — 20_ identity & anulación procedure: undated Agencia Virtual manual; search by full UUID + receptor NIT/CF, motivo, password, "Certificar DTE" button
- **Loc:** 20_FEL_anulacion_manual.pdf.txt, p. 1–5 ("MANUAL DE USUARIO FACTURA ELECTRÓNICA -FEL- Anular DTE")
- **Verbatim:** "Debes ingresar el número de autorización del documento que quieras anular. Debes de ingresar todo el número de autorización utilizando guiones (-). Ejemplo: 550e8400-e29b-41d4-a716-446655440000. Este campo es obligatorio para poder buscar tu documento." … "Ingresa el NIT del receptor (Cliente) o CF (en letras mayúsculas)." … "Ingresa tu contraseña asociada para autorizar la anulación del DTE. Luego presiona el botón “Certificar DTE”."
- **Gloss:** SAT-portal manual for the taxpayer-driven DTE annulment flow: portal.sat.gob.gt → Agencia Virtual → FEL → "Anular DTE"; lookup by full hyphenated UUID + receiver NIT (or literal CF); enter motivo; confirm warning; sign with the contraseña asociada; button is (oddly) labeled "Certificar DTE". Portal steps are SAT-operated — Odoo relevance is only that an annulment path exists outside the certificador channel and returns an anulación transaction (cf. 17_ "Validaciones Transacción de Anulación").
- **Candidate CRs:** none binding on Odoo (SAT portal UI); informational for annulment lifecycle.
- **Topics:** e-invoicing; anulación; Agencia Virtual.
- **Doubts/xref:** 20_ carries NO version/date string — undated screenshot manual (OQ-3).

## EVID-092 — 20_ annulment window: month of emission up to the IVA declaration due date; rectify if already declared
- **Loc:** 20_, p. 5, "IMPORTANTE"
- **Verbatim:** "Los documentos podrán ser anulados durante el mes en que fue emitido y como máximo hasta la fecha de vencimiento de la declaración del Impuesto al Valor Agregado." … "Si el DTE fue incluido en alguna declaración de impuestos, deberá realizar las rectificaciones respectivas."
- **Gloss:** DTE annulment deadline = through the end of the emission month, extended at most to the IVA return due date; declared DTEs require rectification of the return.
- **Candidate CRs:** annulment validation: block/flag annulment attempts beyond emission month + IVA due-date ceiling (taxpayer-side soft check).
- **Topics:** e-invoicing; anulación; deadlines; IVA.
- **Doubts/xref:** SUPERSESSION FLAG: current Reglas v1.7.10 define anulación windows in validation rules (incl. per-DTE-type and "mes siguiente" nuances); this manual's phrasing is the portal-era rule — verify against v1.7.10 (OQ-4, OQ-6).

## EVID-093 — 21_ identity & habilitación flow: undated manual; enable as emitter, password policy, three sub-modules
- **Loc:** 21_FEL_firma_electronica_manual.pdf.txt, p. 1–4 ("MANUAL DE USUARIO FACTURA ELECTRÓNICA -FEL- Habilitación como emisor")
- **Verbatim:** "Se integra de tres complementos “Habilitarse como emisor”, “Generación de firma electrónica interna para emisión” y “Términos y condiciones”." … "El sistema valida automáticamente que cumplas con los requisitos requeridos." … "Parámetros contraseña: debe tener más de 7 caracteres, teniendo al menos 1 mayúscula, 1 minúscula, 1 número y un carácter especial ($%&/()"
- **Gloss:** Actual subject = "Habilitación como emisor" (file label "firma_electronica" is only step 3). Enablement is self-service in Agencia Virtual with automatic requirement checks and a password policy (>7 chars, upper/lower/digit/special from $%&/() for the firma-associated password. Undated manual.
- **Candidate CRs:** none for Odoo (SAT portal onboarding); the associated-password policy matters only if the product stores/creates the emisor firma credentials.
- **Topics:** e-invoicing; onboarding; firma electrónica; Agencia Virtual.
- **Doubts/xref:** undated (OQ-3).

## EVID-094 — 21_ acreditación de certificadores: taxpayer accredits/de-accredits from the authorized list; SAT is certificador for the free app
- **Loc:** 21_, p. 5–6, Paso 2
- **Verbatim:** "Se te desplegará la lista de certificadores autorizados, para que acredites al que seleccionaste para que te preste el servicio de certificación de DTE, y en caso ya no desees los servicios, puedes cambiarle el estado a “No acreditado”." … "A partir de este paso ya puedes iniciar la emisión de DTE a través de esta aplicación gratuita en la Agencia Virtual, en la cual la Superintendencia de Administración Tributaria es tu Certificador"
- **Gloss:** Emitter→certificador relationship is established by **acreditación** in Agencia Virtual (list of authorized certificadores = the 31_ roster); revocable ("No acreditado"). SAT itself certifies only for its free app.
- **Candidate CRs:** informational; explains that switching providers (D-GT5/6) requires updating acreditación + regenerating the emisor signature for third parties (EVID-095).
- **Topics:** e-invoicing; certificador accreditation; onboarding.
- **Doubts/xref:** none.

## EVID-095 — 21_ emisor firma electrónica for third-party certificadores: select "Otros certificadores de DTE (terceros)", generate & download certificate, install in the emission system
- **Loc:** 21_, p. 8–9, Paso 3; p. 10–11 Paso 4 (reset for SAT free app)
- **Verbatim:** "Debes seleccionar a “Otros certificadores de DTE (terceros)”" … "Se descargará el certificado de firma electrónica con el cual se firmarán los DTE que emitas por medio de Certificadores. Dicha firma la debes instalar en tu sistema de emisión de documentos que tengas definido con tu Certificador." … "Utiliza esta opción si emitirás DTE a través de la aplicación gratuita de la Agencia Virtual y olvidaste tu contraseña asociada a tu firma electrónica interna para emisión" (entity = "Superintendencia de Administración Tributaria")
- **Gloss:** Two signature flavors: (1) SAT-internal firma for the free Agencia Virtual app; (2) a downloadable emisor signing certificate for use with third-party certificadores, installed in the emitter's billing system. Separate reset flows per flavor.
- **Candidate CRs:** product must be able to import/use the emisor's downloaded firma electrónica file + associated password to sign DTEs sent to a third-party certificador (TotalDoc flow), and allow re-generation when password is reset.
- **Topics:** e-invoicing; firma electrónica; provider integration (non-government, provider-interface).
- **Doubts/xref:** exact key format (PKCS#12?) is NOT stated in this manual — check 16_ DocTecnicoServicios / provider docs (OQ-7).

## EVID-096 — 22_ identity & version strings: "Procedimiento de Autorización del Certificador" v2.1 with MIXED footer dates (10-07-2024 vs 03-09-2018)
- **Loc:** 22_FEL_autorizacion_certificador.pdf.txt, running footer every page; e.g. p. 2 "Versión 2.1 10-07-2024 2 de 43"; p. 4 "Versión 2.1 03-09-2018 4 de 43"; last extracted page "42 de 43"
- **Verbatim:** "Procedimiento de Autorización del Certificador — Versión 2.1 10-07-2024" (pp. 2–3) and "Procedimiento de Autorización del Certificador — Versión 2.1 03-09-2018" (pp. 4–42)
- **Gloss:** The certificador-authorization manual, version 2.1. Footer dates alternate within the same PDF (10-07-2024 on the first pages, 03-09-2018 elsewhere) — likely a 2024 revision that only updated some headers. Internal pagination says "de 43" but extraction ends at page 42 (p. 43 missing/blank).
- **Candidate CRs:** none (certificador-side document); defines the regime whose roster is 31_.
- **Topics:** certificador authorization; document identity; dated instrument.
- **Doubts/xref:** which footer date governs the whole v2.1 text; whether a newer version exists on the portal (31_ links to `procedimiento-de-autorizacion-de-certificador.pdf`) (OQ-8).

## EVID-097 — 22_ who may be a certificador + application path (Intendencia de Recaudación, written request, third-party vs self)
- **Loc:** 22_, p. 3, §1.1–1.2
- **Verbatim:** "Un certificador es una persona individual, jurídica o entidad no lucrativa que solicita a la Superintendencia de Administración Tributaria, la autorización para realizar la certificación de Documentos Tributarios Electrónicos" … "a) Enviar solicitud escrita a la Intendencia de Recaudación de la SAT … Departamento de Sistemas de Recaudación … 7 avenida 3-73 Zona 9 – Edificio SAT Nivel 7, Ciudad de Guatemala" … "b) La solicitud debe especificar si se desea autorización para prestar el servicio de certificación a terceros, o bien, si desea autorización únicamente para certificar sus propios documentos."
- **Gloss:** Certification is a SAT authorization granted to individuals, companies, or non-profits, for third parties and/or own documents. Paper-based application to Intendencia de Recaudación.
- **Candidate CRs:** none for Odoo (defines who TotalDoc et al. are).
- **Topics:** certificador authorization.
- **Doubts/xref:** none.

## EVID-098 — 22_ administrative requirements: Q1M paid capital (Q5M assets non-profit), solvencia fiscal, declaración jurada, specialized staff, FACE solvency, seminario, ISO 27001 or SAT-audited security cert, Q1M surety insurance
- **Loc:** 22_, p. 5–9, §2.1 A "Requisitos administrativos" items 1–12
- **Verbatim:** "Verificar que la empresa cuenta con un capital pagado mínimo de un millón de quetzales." … "Certificación contable en la que conste que sus activos fijos netos equivalen como mínimo a un valor de cinco millones de quetzales (Q.5,000,000.00), en el caso de personas jurídicas no lucrativas." … "en la que se haga constar que la entidad cuenta como mínimo con diez (10) años de existencia jurídica" … declaración jurada items: "a. Morosidad: Ni la empresa ni sus representantes legales son deudores morosos del estado. b. Empleados del estado: Ninguno de los accionistas ni representantes legales de la empresa, son empleados de ningún organismo del estado … c. Carencia de sentencia condenatoria: No haber tenido ninguna sentencia por cualquier delito o falta contra el régimen tributario o aduanero en los últimos cinco años." … personal: "a. … gerente o asesor del área tributaria … b. … director o gerente del área informática … c. … área de auditoría interna o contratar los servicios de auditoría externa" … "a. Certificado de seguridad de la información vigente, bajo el estándar ISO/IEC 27001 en su versión más reciente." … "El certificador presenta un seguro de caución … por un valor de un millón de quetzales (Q1,000,000.00) a favor de la SAT … por el plazo de un año como mínimo"
- **Gloss:** Financial/administrative gate for certificadores (not Odoo). Security certificate must stay valid the whole service period ("El certificado de seguridad debe mantenerse vigente durante todo el tiempo en que se preste el servicio como certificador"); surety renewed annually.
- **Candidate CRs:** none for Odoo.
- **Topics:** certificador authorization; security certification.
- **Doubts/xref:** none.

## EVID-099 — 22_ mandatory contract clauses between certificador and its emitters (8 clauses a–h)
- **Loc:** 22_, p. 8–9, §2.1 A.10 "Contratos entre el certificador y sus emisores"
- **Verbatim:** minimum clauses: "a. Entrega de los DTE a la SAT … b. Aceptación de las disposiciones del Régimen de Factura Electrónica en Línea … c. Firma del emisor. … cada DTE que el emisor emita y entregue al certificador incluirá una firma electrónica de emisión … d. Autenticidad de los DTE … son irrefutables para fines legales, judiciales y tributarios respecto de los datos firmados. e. Seguridad de la información … f. Mesa de ayuda … de acuerdo al horario habitual de facturación del emisor, horario que debe quedar establecido en el contrato. g. Confidencialidad. … se compromete a no divulgar a terceros no autorizados … h. Relevo de responsabilidad. … cualquier acción u omisión del certificador que cause perjuicio a su emisor, puede derivar en responsabilidad civil y penal."
- **Gloss:** Every DTE must carry the **emisor's firma electrónica de emisión** (clause c) — this is the taxpayer-binding hook: Odoo's emitted DTEs must be signed with the emisor certificate before reaching the certificador. Helpdesk hours tied to the emitter's invoicing schedule.
- **Candidate CRs:** emisor-side: DTE must include firma electrónica de emisión; adenda-level awareness of clause set when contracting TotalDoc.
- **Topics:** e-invoicing; firma electrónica; provider contracts (provider-interface, non-government).
- **Doubts/xref:** clause (f) helpdesk SLA is contractual — capture from TotalDoc contract, not SAT.

## EVID-100 — 22_ performance requirements: ≤3 s to certify a 50-item DTE; ≥99.7% availability; helpdesk registry; no pending requirements/fines
- **Loc:** 22_, p. 9–10 & 13, §2.1 B.1–4 and E.2
- **Verbatim:** "Verificar que la certificación de un DTE que incluya en su detalle 50 ítems de por lo menos 10 caracteres demora 3 segundos o menos. La medición del tiempo inicia desde que el documento llega al certificador hasta que éste certifica el DTE, incluyendo las validaciones y demás procesos intermedios." … "Disponibilidad: verificar que los servicios de emisión, certificación, anulación y consulta de DTE del certificador brinda una disponibilidad igual o mayor al 99.7%." (renewal check, evidenced by "el reporte anual de incidencias del certificador")
- **Gloss:** Certificador-side SLAs; useful as expectations when integrating with TotalDoc (their certification latency and availability commitments), but these bind the certificador, not Odoo.
- **Candidate CRs:** none for Odoo (context for provider SLA expectations).
- **Topics:** certificador performance; provider-interface (non-government).
- **Doubts/xref:** whether v2.1 (2024 footer) tightened 99.7%/3 s — mixed-date doc (OQ-8).

## EVID-101 — 22_ certificador system functionality: emisor authentication, emission incl. anulación, graphic representation in PDF, QR content, HSM FIPS 140-2 L2+, NTP clock sync
- **Loc:** 22_, p. 11–12, §2.1 C.4–5 & D.1–4
- **Verbatim:** "Verificar que la llave privada de la firma electrónica del certificador sea custodiada en un módulo de seguridad criptográfico validado bajo el estándar FIPS-140-2 nivel 2 o superior." … "Verificar que los servidores utilizados por el sistema del certificador … esté sincronizado con un reloj de alta precisión (GPS o Atómico), un servicio registrado en ntp.org, o bien, el provisto por NIST." … representación gráfica cases: "b. El tipo de DTE, el identificador único del DTE (número de autorización), los datos del vendedor y los datos del comprador deben quedar claramente consignados en la parte superior. … f. Disponible en formato PDF. g. Si se incluye el QR, éste debe incluir el contenido que establezca la SAT. … i. Si el DTE está anulado, se debe agregar un texto que identifique ese estado." … emission functions: "a. Emitir documentos de cada tipo … b. Validar y certificar los documentos. c. Enviar a SAT los documentos. d. Almacenar los DTE y sus acuses de recibo. e. Anular DTE."
- **Gloss:** Confirms system-level obligations of the certificador channel (emit/validate/certify/send/store/annul; PDF representation; QR per SAT spec; "ANULADO" text on annulled DTE prints). Relevant to Odoo only as the interface contract expectations of a provider-side pipeline.
- **Candidate CRs:** (borrowable, taxpayer-side mirror) rendered PDF should mark annulled DTEs with state text; QR content per SAT spec when printed.
- **Topics:** certificador functionality; graphic representation; anulación; QR.
- **Doubts/xref:** QR exact content spec lives in Reglas/DocTecnico — xref 15_/16_.

## EVID-102 — 22_ production verification & normative test cases: 2 of each DTE type with SAT test NITs, anular one factura, clean acuses; SAT applies normative casos de prueba
- **Loc:** 22_, p. 12–13, §2.1 D.5 and E.5 "Verificar el sistema en producción"
- **Verbatim:** "a. Registrarse como emisor en su propio sistema informático de certificación de DTE y obtener la autorización de un DTE. b. Emitir y certificar por lo menos dos de cada uno de los tipos de DTE utilizando los NIT que la SAT establece para pruebas. c. Realizar la anulación de uno de los DTE de tipo factura. d. Generar la representación impresa en formato PDF para todos los documentos certificados. e. Obtener acuse de recibo sin errores de la SAT para todos los casos." … "Aprobar satisfactoriamente los casos de prueba normativos que la SAT aplique en el ambiente de pruebas del sistema del certificador."
- **Gloss:** The 17_ casos-de-prueba family is SAT's normative test battery applied to certificadores — this is the binding link between 17_ and 22_. Homologation-style flow (test NITs, all DTE types, anulación, acuses).
- **Candidate CRs:** none for Odoo directly; 17_ cases are the concrete validation examples per rule (see EVID-109/110).
- **Topics:** certificador authorization; test cases; homologation.
- **Doubts/xref:** whether SAT publishes current test NITs for emitter integration testing via TotalDoc (provider docs) (OQ-7).

## EVID-103 — 22_ security checklist (109 items) — highlights: 14-month backup retention until SAT conciliation; TLS 1.2+; RPSC-issued signing cert in FIPS 140-2 L2 HSM; cloud ISO 27018/27001 + CSA STAR; colocation 2-yr contract
- **Loc:** 22_, p. 16–37, §2.2 "Lista de revisión de seguridad del Certificador" items 1–109
- **Verbatim:** item 28: "La retención de los respaldos de información debe estar de acuerdo al Régimen de Factura Electrónica en Línea. Es decir, debe tener como plazo mínimo 14 meses y extenderse hasta que la SAT indique que se han conciliado los DTE certificados." … item 31: "La firma electrónica de certificación debe realizarse con un certificado de firma emitido por prestador de servicios de certificación autorizado por el RPSC. La firma debe resguardare [sic] en un módulo de seguridad criptográfico validado FIPS 140-2 nivel 2 o superior." … item 35: "Toda operación del sistema por Internet se debe realizar por protocolos seguros de acuerdo a las mejores prácticas recomendadas por SSL LABS (TLS 1.2 o superiores)." … item 78: "El proveedor de nube aplica el código de practica para la protección de información de identificación personal ISO/IEC 27018." … item 21: "… copia redundante electrónica diaria de todas las transacciones de la base de datos en un lugar físico alterno, o bien, por medio de servicios en la nube con durabilidad superior a 99.9999%."
- **Gloss:** Certificador-side security baseline (109 numbered controls across segmentation, perimeter, access, backups, crypto, logs, policies, personnel, vulnerability mgmt, risk, cloud/colocation/datacenter physical). Taxpayer-binding takeaway: **document retention floor is 14 months, extended until SAT declares DTE conciliation** — a defensible mirror requirement for Odoo-side DTE/acuse archiving.
- **Candidate CRs:** archive DTEs + SAT acuses ≥14 months (align to retention floor); everything else is certificador-side.
- **Topics:** certificador security; retention/archiving; cloud.
- **Doubts/xref:** emitter-side retention obligation is in AD 13-2018/LIBRO I VAT law (4 years) — reconcile 14-month floor vs statutory retention elsewhere (OQ-9).

## EVID-104 — 22_ authorization procedure & renewal: Resolución + contrato + surety + alta; authorization valid ONE YEAR; renewal duties incl. FEL-only emission
- **Loc:** 22_, p. 38, §2.3–2.4
- **Verbatim:** "a) La Intendencia de Recaudación de la SAT emite una Resolución de Autorización del Certificador … b) La entidad solicitante firma con la SAT el Contrato administrativo de Certificación de Documentos Tributarios Electrónicos. … d) La SAT da de alta al certificador en el sistema de Factura Electrónica en Línea. … f) La autorización brindada al certificador tiene una vigencia de un año." … "La autorización otorgada al certificador tiene una duración máxima de un año. El certificador es responsable de obtener de la SAT la correspondiente renovación de la autorización." … renewal duties: "c) Cumplir con la obligación de enviar a la SAT la totalidad de los DTE que certifique … d) Ser emisor de documentos tributarios únicamente bajo el Régimen de Factura Electrónica en Línea."
- **Gloss:** Authorization windows are annual — the "Fecha de Renovación" column in the 31_ roster is the end of the current annual window. Certificadores must transmit 100% of certified DTEs to SAT and may only invoice under FEL themselves.
- **Candidate CRs:** none for Odoo; interpretive key for roster validity windows (EVID-107).
- **Topics:** certificador authorization; renewal; dated instrument.
- **Doubts/xref:** none.

## EVID-105 — 22_ SAT data services to certificadores + catalogs; perfil form with change-notification duty
- **Loc:** 22_, p. 39–40, §2.5–2.6
- **Verbatim:** "La SAT comparte con los certificadores la información necesaria … 2.5.1 Datos del Registro Tributario Unificado de los emisores de DTE habilitados. 2.5.2 Datos generales de los contribuyentes. 2.5.3 Catálogos para el certificador" … "se establecen los catálogos que los emisores deben aplicar al momento de la emisión de documentos y que los certificadores deben validar al momento de la certificación de estos. La descripción detallada de los mismos estará disponible en el documento denominado “Documento Técnico de Servicios FEL”." … "Si existen cambios sustanciales en los elementos del perfil, tales como cambio de centros de datos, proveedores de nube o incorporación de nuevos servicios, el Certificador debe notificar a la SAT enviando el perfile [sic] actualizado."
- **Gloss:** Catalogs/RTU data flow SAT→certificador; emitters apply catalogs at emission, certificadores validate at certification (i.e., Odoo-side must encode the same catalogs to avoid certificador rejections; detailed in 16_ DocTecnicoServicios).
- **Candidate CRs:** Odoo must consume the same catalog versions the certificador validates (xref 16_).
- **Topics:** catalogs; certificador data services; provider-interface.
- **Doubts/xref:** catalog sync mechanism via TotalDoc — provider docs (OQ-7).

## EVID-106 — 31_ roster page identity & certificador definition; links to 22_; page last modified 2026-07-09
- **Loc:** 31_certificadores_dte_snapshot_2026-08-18.html, `<title>`/yoast schema (dateModified), body heading "Certificador de DTE"
- **Verbatim:** "Es la persona individual o jurídica autorizada por la SAT para encargarse de certificación de los Documentos Tributarios Electrónicos de los emisores que le hayan otorgado acreditación, o bien, de sus propios DTE, que no presenten errores en la validación, debiendo regresar los DTE certificados de inmediato al emisor, para su entrega al receptor y trasladarlo seguidamente a la SAT para su validez o rechazo según sea el caso." … link text: "Requisitos y procedimiento para autorizarse" → `https://portal.sat.gob.gt/portal/descarga/6524/factura-electronica-fel/80213/procedimiento-de-autorizacion-de-certificador.pdf` … schema: `"dateModified":"2026-07-09T21:16:28+00:00"` (page), snapshot taken 2026-08-18 (filename)
- **Gloss:** SAT portal page "Certificador de DTE" (canonical `https://portal.sat.gob.gt/portal/certificador-de-dte/`). Defines the certificador loop: accredit → validate → certify → return to emisor → forward to SAT (validity/rejection). Hosts the roster table below and the 22_ PDF.
- **Candidate CRs:** none (context; loop timing "de inmediato" is qualitative).
- **Topics:** certificador registry; dated data (D15/D16).
- **Doubts/xref:** emails in the HTML are obfuscated by the extractor ("[email protected]") — not captured verbatim (OQ-10).

## EVID-107 — 31_ roster mechanics: 18 authorized certificadores; columns "Fecha de Autorización" / "Fecha de Renovación" = annual validity window (per 22_ §2.3f)
- **Loc:** 31_, `<table class="certificadores">`, 19 `<tr>` (1 header + 18 data rows)
- **Verbatim:** header: "Certificador | Dirección | Contacto | Fecha de Autorización | Fecha de Renovación"; anchor row: "GRUPO CDS S.A. | NIT 107902281 www.grupocds.com.gt … 02/12/2021 | 02/12/2026"
- **Gloss:** Full dated roster as-of 2026-08-18 in the dedicated section below. GRUPO CDS (TotalDoc) renewal due 02/12/2026 — ~3.5 months after snapshot (global OQ7 watch: product default provider must renew; several others renew Nov–Dec 2026).
- **Candidate CRs:** provider-availability monitoring (product decision, not a CR from SAT).
- **Topics:** certificador registry; dated data (D15/D16); provider risk.
- **Doubts/xref:** "Fecha de Renovación" semantics (current window end vs next renewal due) inferred from 22_ annual validity — interpretation, flagged (OQ-11).

## EVID-108 — 31_ "empresas en proceso de autorización" table EMPTY as of 2026-08-18
- **Loc:** 31_, second table after roster
- **Verbatim:** "Lista de empresas en proceso de autorización como Certificador de Documentos Tributarios Electrónicos (DTE) en el Régimen de Factura Electrónica en Línea (FEL)" — columns "NIT | Contribuyente | Solicitud de autorización recibida | Requisitos generales verificados | Certificación de Seguridad aprobada | Desarrollo y pruebas iniciales | Pruebas funcionales en marcha | Autorización y firma de contrato"; single data row: "– | – | – | – | – | – | – | –"
- **Gloss:** Pipeline of candidate certificadores is empty at snapshot date (all cells dashes). Also reveals the authorization pipeline stages SAT publishes.
- **Candidate CRs:** none.
- **Topics:** certificador registry; dated data (D15/D16).
- **Doubts/xref:** an all-dash row could also mean "no data published" rather than "none in process" (OQ-11).

## EVID-109 — 17_ set characterization: uniform RE-GIN/DPI-TI-003 use-case template, v1.0, May-2018 elaboration, each annexed to a Reglas y Validaciones section; IDP near-duplicate with [sic] IVA objective
- **Loc:** 17_casos_de_prueba/*.txt, every file p. 1 header block + §4 Anexos; e.g. Validaciones Generales p.1: "RE-GIN/DPI-TI-003 001 01/03/2014 1 de 6 … Caso de Uso … Factura Electrónica en Línea Versión <1.0> Elaborado por Délmar Leonel Martínez Oliveros <Fecha Elaboración 28/05/2018>" … Anexos: "Documento Reglas y Validaciones. 2.14 Validaciones generales (Parte 3)" (Generales); "… 2.2. Validaciones Generales – 2.2.1 Validaciones Fecha de Emisión." (Fecha); "… 2.2.2 Validación: NIT del Emisor (XSD:NITEmisor)." (Establecimiento); "… 3.5 Complemento 4: REFERENCIAS NOTA DE CRÉDITO Y DÉBITO (XSD:ReferenciasNota)" (NCRE/NDEB); Frases annex: "Documento Reglas y Validaciones." (no section)
- **Gloss:** 25 txt files = 24 unique test-case documents + one near-duplicate IDP pair ("Validacion IDP.txt" vs "Validación IDP.txt" differ only in the objective line — one reads "Verificar la correcta validación del cálculo del IVA del DTE" under an IDP title [sic]). Uniform use-case template (actors: Emisor/Certificador/SAT[+Sistema RTU]; preconditions; numbered Flujo Normal Básico with per-step Resultado: OK/Error; Flujos Alternos; Poscondiciones; Anexos pointing at the Reglas section each case tests). Elaboration dates: 09/05/2018, 12/05/2018, 28/05/2018; header fecha 01/03/2014 is the template code date, not content date.
- **Candidate CRs:** cases are validation examples per rule — use as test-design input mirroring SAT's own battery (see EVID-110).
- **Topics:** test cases; historical (2018); validation rules.
- **Doubts/xref:** set may be incomplete ("Validaciones Generales parte 4" exists; partes 1–3 not in set); annexes cite 2018 Reglas numbering — all supersession checks vs v1.7.10 (OQ-12).

## EVID-110 — 17_ deep-read extracts: five representative cases — Total/Gran Total; establecimiento RTU status; fecha de emisión 5-day/month-end rules; frases type×scenario matrix; NCRE/NDEB referencia-origen validations
- **Loc:** 17_casos_de_prueba — (a) Validaciones Generales.txt pp. 2–6; (b) Validaciones de Código de establecimiento.txt pp. 2–4; (c) Validaciones de Fecha de Emisión.txt pp. 2–3; (d) Validación de Frases.txt pp. 2–12; (e) Validaciones Nota de Credito y Nota de Debito.txt pp. 2–13
- **Verbatim:**
  - (a) "Emitir una factura en la cual el contenido de la casilla total sea calculado erroneamente. Resultado: Error. Total calculado incorrectamente." (× DTE types FACT/FCAM/FESP/FPEQ/FCAP/REC/RDON/NCRE/NDEB/NABO, for Total and Gran Total; annex Reglas 2.14 Parte 3)
  - (b) preconditions: "Estar con Estatus Activo. / NIT Existe en el RTU. / No contar con la Marca de “No Localizado”. / No contar con la Marca de “Omiso”. / Afiliado a cualquier Regimen del IVA. / Contar con al menos un establecimiento Activo." ; "Resultado: Error. El establecimiento no está activo en la SAT (para la fecha de emision [sic]). Rechaza." (INACTIVO or nonexistent code → reject; ACTIVO → OK; annex Reglas 2.2.2)
  - (c) "Emitir un DTE en el cual la Fecha de Emisión tiene una antigüedad mayor a cinco días con respecto a la casilla “Fecha y hora de certificación”. Resultado: Error. La diferencia entre la fecha de emisión y de certificación excede los cinco días. SAT Informa." ; "igual a 5 dias [sic] hacia atrás … Resultado: OK." ; "Resultado: La fecha es mayor al último día del mes en el cual se está emitiendo. Error. La fecha de emisión es posterior al último día del mes de la fecha de certificación. SAT Informa." (annex Reglas 2.2.1)
  - (d) Frases matrix: frase 1 (ISR) required for FACT/FCAM ("Error. El tipo de frase: 1 y/o 2 debe estar presente para el tipo de DTE FACT."; scenarios 1=utilidades lucrativas, 2=opcional simplificado, 3=opcional simplificado con resolución pago directo); frase 2 only if Agente de Retención IVA ("Error. El tipo de frase “retención del IVA” debe estar presente para ese NIT emisor."; "El código de escenario para el “Tipo de Frase” 2 no corresponde a la afiliación del NIT del emisor."); frase 3 mandatory for FPEQ/FCAP, forbidden elsewhere ("El tipo de frase: 3 debe estar presente para el tipo de DTE FPEQ." / "El tipo de frase: 3 no debe estar presente para el tipo de DTE FACT."); frase 4 (exento/no afecto) scenarios 1–12 OK for exento-afiliación, scenario 9 or 12 for items sin IVA / exportación marca Exp=SI requires scenario 1 ("El tipo de frase “exento o no afecto al IVA” debe estar presente para una exportación."; "El código de escenario 10 para el tipo de frase “exento o no afecto al IVA” no corresponde para una exportación."); RDON accepts only 4
  - (e) NCRE/NDEB: "Resultado: Error. El número de Autorización del Documento Origen no coincide con ningún DTE registrado en la SAT." ; "… corresponde a un documento diferente a factura." (origen must be FACT/FCAM — FEL, or FACE with tipo FACT/FCAM codes; other FACE codes 1,2,7,8,30,32,37,38,53,57,60,62,63,66,67,68,69,72 → Error) ; "Error. El valor de la casilla NIT del Emisor no coincide con el registrado en el Documento Origen." (same for ID Receptor, NIT Certificador) ; "Error. La fecha de emisión del documento origen no coincide con la registrada en la SAT." ; "Error. La serie del documento origen no coincide con la registrada en la SAT para esa Resolución de Autorización." ; "Error. El número del documento origen no se encuentra dentro del rango registrado en la SAT para esa Resolución de Autorización." (FACE origens) ; "Error. El monto del impuesto XXX no puede ser mayor al del documento origen registrado en SAT." (annex Reglas 3.5 Complemento 4 XSD:ReferenciasNota)
- **Gloss:** Concrete per-rule acceptance/rejection behaviors: (a) totals arithmetic is validated; (b) establecimiento code must be an active RTU establishment at emission date; (c) emission date ≤ certification date, within same month or ≤5 days back, never past month-end; (d) frase type/scenario depends on emitter ISR/IVA affiliation, DTE type, Exp flag, items-sin-IVA; (e) credit/debit notes must reference an existing FACT/FCAM (FEL) or FACE factura of the same emisor/receptor/certificador, matching fecha/serie/número, with tax amounts not exceeding the origin.
- **Candidate CRs:** mirror validations emitter-side (totals; establecimiento active; date window; frase matrix; referencia-origen consistency) as pre-certification checks to avoid certificador rejections.
- **Topics:** e-invoicing; validation rules; frases; NCRE/NDEB; fechas; RTU; historical (2018).
- **Doubts/xref:** SUPERSESSION FLAGS vs Reglas v1.7.10: (1) 5-day window wording (v1.7.10 may state "no greater than the certification date and within the same month or max 5 days" — verify exact current rule); (2) frase scenario catalog (1–12; errors mention 13–15 as nonexistent — current catálogo may extend); (3) whether NCRE/NDEB origen may now include more FEL types (e.g., FCEL/FCAPE régimen electrónico); (4) FACE-origin codes list current (OQ-12, OQ-13).

---

## Certificador roster (31_, as-of 2026-08-18) — D15 dated data

Snapshot: `31_certificadores_dte_snapshot_2026-08-18.html` (page dateModified 2026-07-09; snapshot filename 2026-08-18). 18 authorized certificadores. "Renovación" = end of current annual authorization window per 22_ §2.3 f) (interpretation, see OQ-11). Addresses/phones/websites in source; emails obfuscated by extractor.

| # | Certificador | NIT | Sitio web | Fecha de Autorización | Fecha de Renovación | Sede (ciudad) |
|---|---|---|---|---|---|---|
| 1 | AINNOVA S.A. | 5640773-4 | www.guatefacturas.com | 23/11/2018 | 23/11/2026 | Guatemala |
| 2 | CÁMARA DE COMERCIO DE GUATEMALA | 351598 | www.ccg.gt | 24/02/2021 | 24/02/2027 | Guatemala |
| 3 | CARI LATINOAMÉRICA, S.A. | 96941243 | www.cari.lat | 22/11/2022 | 22/11/2026 | Quetzaltenango |
| 4 | COFIDI, S.A. | 62469045 | www.cofidi.com.gt | 03/07/2019 | 03/07/2027 | Guatemala |
| 5 | COMERCIALIZADORA GUATEMALTECA MAYORISTA DE ELECTRICIDAD, S.A. | 37156616 | portal.fel.guatemel.com.gt | 21/02/2020 | 21/02/2027 | Guatemala |
| 6 | CONTAP, S.A. | 98978802 | www.facturas.gt | 30/04/2020 | 30/04/2027 | Guatemala |
| 7 | CORPOSISTEMAS, S.A. | 108151654 | www.corposistemasgt.com | 06/04/2021 | 06/04/2027 | Cobán, Alta Verapaz |
| 8 | DIGIFACT SERVICIOS, S. A. | 77454820 | www.digifact.com.gt | 23/08/2019 | 23/08/2026 | Guatemala |
| 9 | FORMULARIOS CONTINUOS DE CENTRO AMERICA, S A. | 4150686 | www.eforcon.com | 20/11/2019 | 20/11/2026 | Guatemala |
| 10 | G4S DOCUMENTA, S. A. | 60010207 | www.documenta.com.gt | 11/03/2019 | 11/03/2027 | Guatemala |
| 11 | GOM SOLUTIONS, S.A. | 95189416 | www.gomsolutions.com | 12/03/2020 | 12/03/2027 | Mixco, Guatemala |
| 12 | **GRUPO CDS S.A. (= TotalDoc, product default provider)** | **107902281** | www.grupocds.com.gt | **02/12/2021** | **02/12/2026** | Quetzaltenango |
| 13 | INTEGRAL ADMINISTRADORA DE RECURSOS Y SERVICIOS EMPRESARIALES, S.A | 92721788 | www.indrese.com | 17/01/2020 | 17/01/2027 | Guatemala |
| 14 | INFILE, S. A. | 12521337 | www.infile.com | 29/10/2018 | 31/10/2026 | Guatemala |
| 15 | INFORUM CONSULTING, S. A. | 43430775 | www.edxsolutions.gt | 23/11/2018 | 23/11/2026 | Guatemala |
| 16 | MEGAPRINT, S. A. | 50510231 | www.megaprint.com.gt | 23/11/2018 | 23/11/2026 | Santa Catarina Pinula |
| 17 | OPERADORA ECONÓMICA, S.A. | 64281167 | www.ecofactura.com.gt | 13/02/2020 | 13/02/2027 | Guatemala |
| 18 | TEKRA, S. A. | 107346834 | www.tekra.com.gt | 21/12/2020 | 21/12/2026 | Guatemala |

Renewal-due cluster after snapshot: DIGIFACT 23/08/2026 (5 days post-snapshot), INFILE 31/10/2026, AINNOVA/INFORUM/MEGAPRINT 23/11/2026, CARI 22/11/2026, FELCON 20/11/2026, **GRUPO CDS (TotalDoc) 02/12/2026**, TEKRA 21/12/2026 — global OQ7 watch. In-process authorization table: empty (all dashes) as of snapshot.

---

## Casos-de-prueba set characterization (17_)

**Set:** 25 .txt extractions = 24 unique test-case documents + 1 near-duplicate (two IDP copies differing only in objective line IDP vs IVA [sic]). Uniform template: doc code RE-GIN/DPI-TI-003, Revisión 001, header date 01/03/2014 (template date), "Versión <1.0>", elaborador Délmar Leonel Martínez Oliveros, Fecha Elaboración 09|12|28/05/2018 → **HISTORICAL 2018-05 vintage** (task OQ9 note: may lag Reglas v1.7.10 and current catalogs). Structure: Actores (Emisor/Certificador/SAT[±Sistema RTU]) → Precondiciones → numbered Flujo Normal Básico with per-step "Resultado: OK/Error" → Poscondiciones → Anexo citing the Reglas y Validaciones section tested. Read as concrete validation examples per rule, not as current normative text.

**Deep-read (5):** Validaciones Generales; Validación de Frases; Validaciones de Código de establecimiento; Validaciones de Fecha de Emisión; Validaciones Nota de Credito y Nota de Debito → extracts in EVID-110.

**Rest (one-liners):**
1. Caso de Uso Validacion IDP / **Validación IDP (duplicate pair)** — IDP (petroleum distribution tax) computation/validation per DTE type; one copy's objective mis-prints "IVA" [sic].
2. Validacion de la Afiliación segun el NIT — emission admissibility per emitter-NIT affiliation (título interno: "Validaciones emisión de DTE según afiliación del NIT").
3. Validaciones Complemento Factura Especial — validations of the factura-especial complement (retenciones).
4. Validaciones Complementos — general complement presence/content rules.
5. Validaciones Generales parte 4 — part 4 of the general-validations battery (partes 1–3 absent from set).
6. Validaciones Transacción de Anulación — annulment-transaction validations.
7. Validaciones de Descuento — discount amount/consistency validations.
8. Validaciones de Esquema — XSD schema validation (título interno "Validaciones de Esquema XSD").
9. Validaciones de ID Exportación — export mark ("Marca Exportación") validations.
10. Validaciones de ID Receptor — receiver ID (NIT/CUI/CF) validations.
11. Validaciones de NIT del Emisor — emitter NIT validations (RTU existence/status).
12. Validaciones de Precio — price amount validations.
13. Validaciones especificas de los impuestos incluidos por tipo de DTE — which taxes may appear per DTE type (título interno "Validaciones de tipo de impuesto por DTE").
14. Validación IFB — Bomberos volunteer-fund tax validations.
15. Validación ITH — tourism lodging tax validations.
16. Validación ITP — air/sea departure ticket tax validations.
17. Validación IVA — IVA validations per DTE type.
18. Validación MUN — municipal rate validations.
19. Validación TDP — press-stamp tax validations.

---

## Open questions (file-level)

- **OQ-1 (18_ identity):** The workspace label says "guía requisitos mínimos (software certification requirements)" but the document is the **graphic-representation** requirements guide. Is there a separate SAT "requisitos mínimos" document for certificador software, or is 18_ the only guía? (Affects LB-citation naming.)
- **OQ-2 (18_ currency):** 18_ has no version/date string yet lists Régimen Electrónico DTE types (post-2021) — undated guide of uncertain vintage; confirm current portal version and whether the "20 tipos" count matches Reglas v1.7.10/catálogos.
- **OQ-3 (20_/21_ undated):** Both Agencia Virtual manuals carry no version/date; screenshot UIs may be stale. Confirm current portal flows (anulación and habilitación/firma) unchanged.
- **OQ-4 (19_ supersession):** 2018 contingency text vs current regime: (a) numeric deadline to regularize contingency DTEs is NOT stated ("fuera del plazo establecido" defers to Reglas — what does v1.7.10 say?); (b) 19_ defines contingencia as connectivity only, while 18_ mentions "contingencia por casos fortuitos" — does v1.7.10/ current SAT doctrine define both classes and different mechanics per class?; (c) is the legend "Emisión en contingencia, obtenga el DTE Certificado en el sitio www.sat.gob.gt/efactura" and URL still current?; (d) is emisor e-signature still required on the contingency print (EVID-090)?
- **OQ-5 (Número de Acceso format):** Current construction rule for Número de Acceso (2018: "definido en Reglas y Validaciones, XSD GT_Documento") — extract from v1.7.10 before implementing contingency mode.
- **OQ-6 (anulación window):** 20_ says anulación allowed through emission month, max until IVA declaration due date; verify against v1.7.10 anulación validation rules (incl. whether certificador-channel anulación has a different window and whether "hasta la fecha de vencimiento de la declaración del IVA" means the emitter's own periodicity).
- **OQ-7 (provider specifics, non-government):** Emisor firma key format for third-party certificadores (21_ says "descargar e instalar" but not the format), TotalDoc test NITs/homologation flow (22_ §E.5 mentions SAT test NITs), TotalDoc catalog sync (22_ §2.5) — pull from TotalDoc/provider docs (LB-citable only as provider-interface, non-government).
- **OQ-8 (22_ versioning):** v2.1 footers alternate 10-07-2024 (pp. 2–3) and 03-09-2018 (pp. 4–42); extraction ends "42 de 43" (p. 43 missing). Which date governs; is there a v2.2+ on the portal (the 31_ page links the PDF directly)?
- **OQ-9 (retention):** 22_ item 28 sets a 14-month minimum backup retention for certificadores "hasta que la SAT indique que se han conciliado los DTE"; reconcile with emitter-side retention duties (AD 13-2018 art.; LIBRO I IVA 4-year books/records) for the Odoo archiving requirement.
- **OQ-10 (31_ emails):** Roster emails obfuscated by extraction ("[email protected]") — re-fetch or accept loss; phones/addresses captured verbatim.
- **OQ-11 (31_ semantics):** Does "Fecha de Renovación" mean current-window expiry (interpretation used, per 22_ annual validity) or next renewal filing date? And is the all-dash "en proceso" row truly "none in process" vs "not published"?
- **OQ-12 (17_ completeness/vintage):** Set lacks "Validaciones Generales" partes 1–3 (only parte 4 present) — is the published set larger? All annexes cite 2018 Reglas numbering (2.2.1, 2.2.2, 2.14, 3.5) — map to v1.7.10 numbering before reuse; confirm whether SAT publishes a current test-case battery.
- **OQ-13 (17_ rule drift):** For deep-read cases, verify against v1.7.10: 5-day/month-end emission-date window; frase scenario catalog bounds (errors mention 13–15 as nonexistent for frase 4 — current catálogo?); NCRE/NDEB origen types (FACT/FCAM only? now also régimen-electrónico types?); FACE-origin código-tipo mapping list (1,2,7,8,30,32,37,38,53,57,60,62,63,66,67,68,69,72 rejected) currency.

## Superseded-by-Reglas-v1.7.10 watchlist (summary)
1. 19_ contingency mechanics: regularization deadline, contingency classes (conectividad vs casos fortuitos), legend/URL, Número de Acceso format (EVID-088/089/090 → OQ-4/5).
2. 20_ anulación window phrasing (EVID-092 → OQ-6).
3. 17_ all rule numbers/values: fecha-emisión 5-day rule, frase matrix/scenarios, NCRE/NDEB origen types, FACE code list, totals rules (EVID-109/110 → OQ-12/13).
4. 18_ 20-type count vs current catálogo; QR optionality wording (EVID-082/083 → OQ-2).
5. 22_ is current-ish (v2.1, 2024 partial footers) but its Reglas references and performance/security baselines should be spot-checked against v1.7.10-era SAT pages (OQ-8).
