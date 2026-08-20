# GT — E-Invoicing — Anulación, contingencia & the fecha-emisión regime (cluster E6)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the Guatemala FEL
*anulación* (cancellation) regime, the *contingencia* (contingency) local
emission procedure, the CF-replacement model, and the document-state
consequences of the fecha-emisión (emission-date) regime: the anulación
window bounded by the IVA monthly-declaration due date of the emission
period (never a fixed N-day window) plus the prescription ceiling; the
anulación blocker set (vigente NC/ND and constancia associations;
SAT-exclusive checks against Retenciones Web / Asiste Libros / LET /
Planilla del IVA FEL); emisor-only origination and cross-certificador
anulación; the GT_AnulacionDocumento transport (double-signed, never
mutating a certified DTE) with the ReversionDocumento schema recorded but
NOT implemented; contingencia emission (full local XML per the current
XSD, "Documento en contingencia" title, 9-digit Número de Acceso,
verifier footer URL, Aviso de Contingencia, immediate re-send); the
CF-replacement model (5-calendar-day NIT-ization with automatic
annul-and-reissue); and the correct-vs-annul document-state routing that
instantiates D16's no-past-dated-transmission rule.

It does **not** cover: the DTE taxonomy (`01_document-types.md`, E1), the
XSD schema structure — the anulación/reversion schemas are anchored at
`02_dte-schema.md` GT-EINV-FR-065/066 and the certification block at
FR-045 (E2), the Reglas validation universe including the fecha-emisión
rule trio GT-EINV-FR-077..079 and their D16 mechanics FR-080
(`03_validation-rules.md`, E3 — referenced here, never duplicated), the
legal chain and mandate chronology (`04_mandate-onboarding.md`, E4), the
certificador provider contract — anulación transport semantics are
anchored at `05_certificador-interface.md` GT-EINV-FR-175..177 and
FR-180..FR-185 (E5), the graphic representation layout
(`07_display-representation.md`, E8 — forward anchor), or retention and
archive duties (`08_archive-retention.md` — forward anchor).

## 2. Legal Basis

Authority guards (binding, from the master index): **Reglas y
Validaciones v2.0 (19/12/2024, vigencia abril 2025) governs EVERY
divergence vs the 2018-vintage manuals 19_/20_ (ruling R7)** — 2018 items
are retained below only as historical/test-design input, each with an
explicit supersession note, and the supersession ledger in §3.7 records
every known divergence. Reglas is cited as "v2.0 (19/12/2024, vigencia
abril 2025)" only (the stale "v1.7.10/Febrero 2025" cover footer is never
cited; the source filename encodes it). 16_ Documento Técnico v1.2 is
cited for anulación transport boundary semantics only (R11 discipline —
never for current schema structure or production URLs). Rulings applied:
R7, R11, R13 (context), D1/D15/D16/D-GT10.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglas v2.0 §3.16.7.1: "La casilla “Fecha de anulación” excede la fecha de vencimiento de la declaración mensual del IVA del período impositivo al que corresponde el documento a anular (Fecha de Emisión del DTE a Anular)." | Anulación window rule: the cancellation date may not exceed the due date of the IVA monthly declaration for the tax period to which the document to be cancelled belongs (the emission date of the DTE to cancel) — a period-based ceiling, not a fixed N-day window | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §3.16.7.1 pp. 122–124 (EVID-143) |
| LB-002 | Reglas v2.0 §3.16.2.2–3: no se puede anular un DTE que cuente con Nota de Débito o Nota de Crédito vigente asociada, ni un DTE con Constancia (CIVA/CAIS) asociada vigente. | Anulación blockers: a DTE with a live (vigente) NDEB/NCRE associated, or with a live associated CIVA/CAIS, cannot be cancelled | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §3.16.2 pp. 122–124 (EVID-143) |
| LB-003 | Reglas v2.0 §3.17.2 (validaciones exclusivas de la SAT — anulación): retención de IVA/ISR registrada en "Retenciones Web" (cotejo NIT Emisor/ID Receptor[/Monto Total/Fecha y Hora de Emisión]), "Asiste Libros", "LET", "Planilla del IVA FEL" → rechaza. | SAT-exclusive anulación checks: if an IVA/ISR retention touching the document exists in Retenciones Web, or it appears in Asiste Libros, LET or the Planilla del IVA FEL, SAT rejects the anulación — checks only SAT can run | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §3.17.2 p. 123 (EVID-143) |
| LB-004 | Reglas v2.0 §5.5.1: "a) La anulación únicamente la puede solicitar el emisor … b) No se puede anular un DTE que corresponda a un período mensual del Impuesto al Valor Agregado ya prescrito. … d) [aplica] exclusivamente a los DTE emitidos dentro del régimen FEL. e) Es responsabilidad del Certificador … validar que el documento a anular cuenta con acuse de recibo de la SAT, aun cuando el DTE a anular no haya sido certificado por él." §5.5.2 datos de la solicitud: UUID, NIT emisor, ID receptor, fecha emisión, fecha anulación, motivo, firma. | Anulación annex conditions: only the emitter may request; a DTE in an already-prescribed IVA monthly period can never be cancelled; the regime covers FEL DTEs exclusively; the certificador must verify the SAT acknowledgment (acuse de recibo) exists even for DTEs it did not certify; request data set = UUID + emitter NIT + receiver ID + both dates + reason + signature | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §5.5 p. 136 (EVID-143) |
| LB-005 | Reglas v2.0 §3.16.5.1 nota: "Se deja sin efecto la presente validación, para permitir que un Certificador pueda autorizar la anulación de un DTE autorizado por otro Certificador." (misma liberación para NC/ND desde v1.6: changelog "3.5.1.6 Se deja sin efecto la limitación de autorizar nota de débito o crédito para DTE de un mismo Certificador") | Cross-certificador anulación explicitly allowed (validation left without effect); the same liberation applies to NC/ND since Reglas v1.6 (14/12/2020) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §3.16.5 p. 123 + changelog pp. 139–146 (EVID-143, EVID-114) |
| LB-006 | Reglas changelog: v1.5 (20/12/2019) "Se agrega validación a la fecha de anulación, para que no se pueda anular más allá de 5 días en el pasado"; v1.5.4 Rev.1 (07/12/2020) "se acepte la anulación, siempre que el periodo en el que haya sido emitido el DTE, no esté prescrito" | The 5-day-past anulación window was ADDED at v1.5 (20/12/2019) and REPLACED at v1.5.4 Rev.1 (07/12/2020) by the non-prescribed-period rule — the changelog is the supersession proof (D-GT10 dated rows) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | Sección 6 changelog pp. 139–146 (EVID-114) |
| LB-007 | GT_AnulacionDocumento-0.1.0.xsd (NS fel/0.1.0): root GTAnulacionDocumento > SAT > AnulacionDTE > DatosGenerales@ID "DatosAnulacion", atributos requeridos NumeroDocumentoAAnular (tipoUUID), NITEmisor, IDReceptor, FechaEmisionDocumentoAnular (dateTime), FechaHoraAnulacion (dateTime), MotivoAnulacion (1..255); Certificacion opcional; mismos dos slots ds:Signature. | The anulación transaction document: six required attributes (target UUID, emitter NIT, receiver ID, original emission timestamp, cancellation timestamp, reason 1–255 chars), optional Certificacion, two signature slots (structure owned by `02_dte-schema.md` FR-065) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_AnulacionDocumento-0.1.0.xsd` | full file (EVID-015) |
| LB-008 | GT_ReversionDocumento-0.1.0.xsd (NS fel/0.1.0, idéntico en ambos canales): NumeroDocumentoAReversar (tipoUUID), Serie + Numero (derivadas del UUID), NITEmisor, IDReceptor, FechaEmisionDocumentoReversar, FechaHoraReversion, MotivoReversion (1..255), UsuarioSolicitud (1..100, "Indica el nombre del usuario que registra la transaccion."). | The reversion transaction (undo of an anulación): target UUID plus its Serie/Numero decomposition, both NITs/IDs, both timestamps, reason 1..255 and the name of the requesting user — schema exists, no v1.2 API operation is printed for it (structure owned by `02_dte-schema.md` FR-066) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_ReversionDocumento-0.1.0.xsd` | full file (EVID-016) |
| LB-009 | Reglas v2.0 §4.1 (contingencia): "a. El documento debe generarse en el formato electrónico (XML) que determina el esquema XSD: GT_Documento, en su versión vigente. b. La representación gráfica debe identificarse con el título “Documento en contingencia”. … d. Debe contener un “Número de Acceso”, definido en el anexo 5.4 … e. Al pie del documento debe colocar el texto: Emisión en contingencia, obtenga su DTE certificado en el sitio https://portal.sat.gob.gt/portal/verificador-integrado/." + "Los documentos emitidos en contingencia, en ningún caso serán formularios “preimpresos”…" + Aviso de Contingencia (Agencia Virtual): "Fecha y hora de inicio …; Fecha y hora en que finalizó …; Número de establecimiento; Motivo; Cantidad de documentos emitidos"; "En su defecto, el aviso puede enviarse al correo electrónico efactura@sat.gob.gt."; "… al obtener conexión con su Certificador, de forma inmediata deberá enviar todos los documentos que generó en contingencia …". | Contingency procedure: generate the full DTE XML locally per the current GT_Documento XSD; title the graphic representation "Documento en contingencia"; carry a Número de Acceso (annex 5.4); print the footer with the SAT integrated-verifier URL; never preprinted forms; after the outage file the Aviso de Contingencia (five fields) via Agencia Virtual or the efactura@sat.gob.gt fallback; upon reconnecting with the certificador, IMMEDIATELY send every contingency document (no numeric deadline stated) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §4.1 pp. 125–131 (EVID-144) |
| LB-010 | Reglas v2.0 §4.2 (modelo de emisión CF): "… como máximo en los 5 días calendario siguientes a la fecha de emisión … de forma automática el emisor anula el documento CF y le emite el nuevo DTE (el cual conservará los mismos datos de la operación, con excepción del número de autorización, serie y número de documento)." + texto al pie: "Para obtener el Documento Tributario Electrónico (DTE) certificado con su NIT y NOMBRE debe ingresar en un plazo máximo de 5 días calendario al sitio web: …" + "Este modelo solo estará disponible con servicio de un Certificador (tercero autorizado …)". | CF-replacement model: the customer obtains a NIT-bearing certified DTE within at most 5 calendar days of emission; the emitter then AUTOMATICALLY cancels the CF document and reissues the DTE preserving all operational data except authorization number/serie/número; the CF print carries the 5-day retrieval footer; the model is available only with a (paid) certificador service | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §4.2 pp. 125–131 (EVID-144) |
| LB-011 | Reglas v2.0 §5.4: "Número de Acceso … generado por el sistema de facturación del Emisor en forma aleatoria, que va desde 100000000 hasta 999999999 (9 dígitos) … para obtener un DTE … en contingencia … sin necesidad de utilizar una contraseña". | Número de Acceso: generated randomly by the emitter's billing system, in the range 100000000–999999999 (9 digits); lets the receiver retrieve the contingency DTE on SAT's portal without a password | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §5.4 pp. 135–138 (EVID-142) |
| LB-012 | Reglas v2.0 §2.2.1.1–5 + "Aclaración sobre la validación 2.2.1.1 (fecha futura)": "El día, mes y año de la casilla “Fecha y hora de emisión” tiene una antigüedad mayor a cinco días … y el tipo de DTE es diferente de “CIVA” y “CAIS”." (Se cuenta a partir del siguiente día de la emisión); "La casilla “Fecha y hora de emisión” es posterior al último día del mes de la “Fecha y hora de certificación”."; afiliación: tras un cambio, DTE con fecha del mes anterior (5 días calendario) "deberá mostrar la afiliación con la que contaba anteriormente". | The fecha-emisión regime (rules owned by `03_validation-rules.md` FR-077..079): ≤5 days back counted from the day after emission with CIVA/CAIS exempt; future dates only within the same calendar month; 5-day affiliation-change lookback showing the OLD affiliation — cited here only for the document-state consequences this file owns | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` (cited as v2.0 per authority order) | §2.2.1 pp. 20–21 (EVID-119) |
| LB-013 | 19_ (Mayo 2018, HISTORICAL — supersesión R7): "Se define como contingencia la situación por la cual un Emisor no puede obtener de forma inmediata la certificación de sus documentos … por problemas de conectividad." (§1.2); alternativas: aplicación web gratuita / certificador de sus propios documentos / "Acreditar más de un Certificador" / emisión en contingencia (§1.3); "El Emisor deberá emitir y entregar sus Documentos con el texto “Documento en Contingencia” … La representación gráfica … no contendrá el número de autorización del Certificador, en su lugar deberá contener el “Número de Acceso” … “Emisión en contingencia, obtenga el DTE Certificado en el sitio www.sat.gob.gt/efactura”" (§1.4); Aviso 5 campos + "Inmediatamente deberá enviar los documentos a su Certificador, incluyendo en los archivos XML el campo “Número de Acceso”…" + "La información de la contingencia servirá para que los servicios de la SAT no rechacen los documentos por llegar fuera del plazo establecido." (§1.4 fin); "Si el Emisor es a su vez Certificador … deberá utilizar el servicio de un tercero para la certificación de los documentos emitidos en contingencia." + "Debe incluirse la firma electrónica del Emisor en la representación gráfica." (§1.5) | The 2018 contingency manual: connectivity-only definition; the four-alternative ladder; emission mechanics (contingency title; Número de Acceso printed in place of the authorization number; retrieval legend with the now-stale www.sat.gob.gt/efactura URL); the aviso + immediate retransmission with "plazo establecido" deferral; self-certifier third-party restriction and the emisor e-signature-on-print duty — historical input under Reglas v2.0 supersession | `gt/sources/19_FEL_contingencia.pdf.txt` | §1.2–1.5 pp. 1–5 (EVID-086..090) |
| LB-014 | 20_ (HISTORICAL — supersesión R7, moneda GOQ-37): flujo portal "Debes ingresar el número de autorización del documento que quieras anular … utilizando guiones (-) … Ingresa el NIT del receptor (Cliente) o CF … Ingresa tu contraseña asociada para autorizar la anulación del DTE. Luego presiona el botón “Certificar DTE”." + ventana: "Los documentos podrán ser anulados durante el mes en que fue emitido y como máximo hasta la fecha de vencimiento de la declaración del Impuesto al Valor Agregado." + "Si el DTE fue incluido en alguna declaración de impuestos, deberá realizar las rectificaciones respectivas." | The undated Agencia Virtual anulación manual: taxpayer portal flow (full hyphenated UUID + receiver NIT/CF lookup, reason, password signature, "Certificar DTE" button [sic]) and the portal-era window phrasing (emission month extended at most to the IVA declaration due date) plus the rectify-if-declared duty — historical illustration; the current window rule is LB-001 | `gt/sources/20_FEL_anulacion_manual.pdf.txt` | pp. 1–5 (EVID-091, EVID-092) |
| LB-015 | 16_ §IV (anulación — semántica de frontera, R11): "La anulación se realiza por una operación externa al DTE y no modificará en ningún caso un DTE ya certificado, únicamente consiste en una anotación lógica vinculada al DTE que sea anulado."; "La operación de anulación … debe ser firmada por el EMISOR … y también debe ser firmada por el CERTIFICADOR para su validez"; "https://api.desa.sat.gob.gt /postAnulacionDTE"; firma "sobre el elemento DatosGenerales"; esquema "GT_AnulacionDocumento-0.1.0.xsd". | Anulación transport boundary semantics: external logical annotation that never modifies a certified DTE; double-signed (emisor over DatosGenerales + certificador counter-signature); SAT-side operation postAnulacionDTE (dev/desa reference only — the product integrates via the provider's own API) | `gt/sources/16_FEL_DocTecnico_Servicios.pdf` | §IV pp. 19–23 (EVID-156, EVID-157) |

## 3. Functional Requirements

### 3.1 Anulación window (current authority)

- **GT-EINV-FR-204:** The anulación window shall be computed as a
  period-based ceiling: an anulación is admissible while its
  *Fecha de anulación* (cancellation date) does not exceed the due date
  of the IVA monthly declaration for the *período impositivo* (tax
  period) of the cancelled DTE's emission date. The IVA-declaration due
  date is EXTERNAL calendar data — the product shall consume it from a
  configurable IVA-calendar input (per-period, per-NIT-last-digit rows,
  D15/D16 dated rows) and shall never hardcode a due date or a fixed
  N-day window; calendar sourcing → GOQ-14 kin (cross-topic note to the
  fiscal-reporting wave). (LB-001; EVID-143; D15/D16)
- **GT-EINV-FR-205:** Independently of the calendar ceiling, an anulación
  shall be refused when the DTE belongs to an IVA monthly period that is
  already *prescrito* (prescribed / statute-barred): the window is never
  a prescribed period — this is a hard legal ceiling no configuration can
  extend. (LB-004; EVID-143)
- **GT-EINV-FR-206:** The window-rule evolution shall be recorded as
  D-GT10 dated rows and the product shall implement ONLY the current
  rule: v1.5 (20/12/2019) added a "no anular más allá de 5 días en el
  pasado" validation (former §3.7.6.3); v1.5.4 Rev.1 (07/12/2020)
  replaced it with the non-prescribed-period rule; Reglas v2.0
  (19/12/2024, vigencia abril 2025) carries the period rule as §3.16.7.1
  + §5.5.1.b. No 5-day anulación check shall ship; the superseded row is
  retained as test-design/history only. (LB-006; EVID-114; R7)
- **GT-EINV-FR-207:** When an anulación targets a DTE already included in
  a filed IVA declaration, the product shall surface the rectification
  advisory — "deberá realizar las rectificaciones respectivas" (the
  respective rectifications must be made) — without mutating any filed
  declaration (D16 freeze-at-filing: filed-period data is never
  rewritten by the anulación flow). Historical-source duty, retained
  because the current authority does not contradict it (GOQ-37 kin on
  the undated manual). (LB-014; EVID-092; D16)

### 3.2 Anulación blockers & eligibility

- **GT-EINV-FR-208:** A DTE with a *vigente* (live) NDEB or NCRE
  associated shall be blocked from anulación, with the blocker reason
  surfaced on the cancel surface. (LB-002; EVID-143)
- **GT-EINV-FR-209:** A DTE with a live associated CIVA/CAIS (constancia)
  shall be blocked from anulación, with the blocker reason surfaced.
  (LB-002; EVID-143)
- **GT-EINV-FR-210:** The §3.17.2 SAT-exclusive checks shall be modeled
  as OUTCOME-ONLY blockers: the product can neither pre-verify nor
  override them — if SAT finds an IVA/ISR retention touching the document
  in Retenciones Web (match on NIT Emisor / ID Receptor [, Monto Total /
  Fecha y Hora de Emisión]), or the document appears in Asiste Libros,
  LET or the Planilla del IVA FEL, SAT rejects the anulación and the
  product shall surface the rejection with its blocker family. The
  product shall not promise pre-verification of these systems
  (cross-topic note: the retention/book feeds are owned by the
  fiscal-reporting and payroll waves). (LB-003; EVID-143)
- **GT-EINV-FR-211:** An anulación request shall originate only from the
  emisor of the DTE ("La anulación únicamente la puede solicitar el
  emisor"): the cancel action shall be restricted to users acting for the
  emitting company of the target document — receiver-side or third-party
  cancellation is out of scope (the SAT-portal taxpayer flow of LB-014
  is the emisor's own portal session, recorded as historical
  illustration, GOQ-37 kin). (LB-004; LB-014; EVID-143, EVID-091)
- **GT-EINV-FR-212:** The anulación regime applies exclusively to DTEs
  emitted within the FEL regime: the cancel flow shall be offered only
  for FEL documents (legacy paper/FACE-era documents follow their own
  regimes and are out of this flow's scope). (LB-004; EVID-143)
- **GT-EINV-FR-213:** Cross-certificador anulación shall be allowed: a
  certificador may authorize the anulación of a DTE certified by another
  certificador (the restriction is explicitly "sin efecto"), and the
  certificador — not the product — carries the duty to verify the SAT
  *acuse de recibo* (acknowledgment of receipt) exists even for DTEs it
  did not certify; the product shall not restrict anulación to the
  original provider and shall pass the acuse-verification expectation
  through the provider profile (transport per
  `05_certificador-interface.md` GT-EINV-FR-185). (LB-004; LB-005;
  EVID-143, EVID-114)

### 3.3 Anulación transport & reversion

- **GT-EINV-FR-214:** The anulación request shall serialize
  GT_AnulacionDocumento exactly as anchored at `02_dte-schema.md`
  GT-EINV-FR-065 (NS fel/0.1.0; DatosGenerales@ID "DatosAnulacion") with
  the six required attributes — NumeroDocumentoAAnular (the target UUID),
  NITEmisor, IDReceptor, FechaEmisionDocumentoAnular, FechaHoraAnulacion,
  MotivoAnulacion (1..255 chars, local-validation bounded) — and the
  §5.5.2 data set (UUID, NIT emisor, ID receptor, fecha emisión, fecha
  anulación, motivo, firma); the request is doubly signed (emisor
  signature over DatosGenerales + certificador counter-signature) and is
  an EXTERNAL logical annotation that never modifies the certified DTE —
  the original UUID/Serie/Numero and content stay immutable in the
  ledger. (LB-004; LB-007; LB-015; EVID-143, EVID-015, EVID-156)
- **GT-EINV-FR-215:** The reversion transaction (undo of an anulación)
  shall be RECORDED, NOT IMPLEMENTED: the GT_ReversionDocumento schema
  exists (NumeroDocumentoAReversar + its Serie/Numero decomposition +
  NITEmisor + IDReceptor + both timestamps + MotivoReversion 1..255 +
  UsuarioSolicitud 1..100 — structure anchored at FR-066) but no v1.2
  provider-boundary API operation is printed for it; the product shall
  ship no reversion surface, and any future reversion capability waits
  on the API-currency question → GOQ-51 kin (owned by
  `05_certificador-interface.md` OQ-007; no-reversion assumption per
  GT-EINV-FR-176). (LB-008; EVID-016)

### 3.4 Fecha-emisión regime: document-state consequences (rules owned by the 03 file)

- **GT-EINV-FR-216:** The FEL document state machine shall expose:
  draft → certified (número de autorización assigned —
  `05_certificador-interface.md` FR-180/FR-181) → anulado (via the
  anulación acuse; the document stays immutable with the anulación
  annotation linked); and contingencia → certified (via re-send,
  FR-224). Corrections are ALWAYS new NCRE/NDEB documents referencing
  the origin — never edits to a certified DTE and never mutations of an
  anulado one; state transitions are saas-authoritative with odoo
  display surfaces. (LB-015; EVID-156; back-ref GT-EINV-FR-185)
- **GT-EINV-FR-217:** The correct-vs-annul routing shall follow the
  fecha-emisión regime (window rules GT-EINV-FR-077..079 owned by the 03
  file, cited not duplicated): a certified DTE with wrong data is
  corrected via NCRE/NDEB (single-origin rules, 03-file FR-137) or
  cancelled via this file's window+blocker flow; the surface shall make
  the consequence explicit — anulación is available only within the
  FR-204/FR-205 window and with no FR-208..FR-210 blocker, while NC/ND
  follow their own 03-file rules (2-month IVA-credit advisory included
  there). (LB-001; LB-012; EVID-143, EVID-119)
- **GT-EINV-FR-218:** D16 instantiation — no past-dated transmission: a
  replacement DTE issued after an anulación (or a corrected NC/ND flow)
  shall carry an emission date inside the permitted window (≤5 días back
  counted from the day after emission, CIVA/CAIS exempt; future only
  within the same calendar month); the product shall never offer
  "re-issue with the original past date", and documents dated beyond the
  window are the historical, NON-TRANSMITTABLE class (hard no-override
  emission block per GT-EINV-FR-080 in the 03 file — instantiation
  here: the anulación/reissue path cannot be used to smuggle a
  past-dated document into certification). (LB-012; EVID-119; D16;
  back-ref GT-EINV-FR-080)

### 3.5 Contingencia (Reglas v2.0 §4.1; 19_ historical input)

- **GT-EINV-FR-219:** Contingencia mode shall be available when
  certification cannot be obtained (certificador/SAT unreachable): the
  emitter generates and delivers documents WITHOUT prior certification,
  following the mechanics of FR-220..FR-225. The current authority
  states one mechanics set and NO doctrine classes; the 19_ (Mayo 2018)
  connectivity-only definition ("por problemas de conectividad") vs the
  "casos fortuitos" (fortuitous events) category mentioned by 18_ is an
  unresolved doctrine gap → GOQ-38 (owned, OQ-001); the product shall
  key the mode on "certification unobtainable" and shall not encode
  per-class mechanics until the doctrine resolves. (LB-009; LB-013;
  EVID-144, EVID-086; R7)
- **GT-EINV-FR-220:** In contingencia mode the product shall generate
  the FULL DTE XML locally per the current GT_Documento XSD ("en su
  versión vigente" — channel authority per `02_dte-schema.md` FR-067),
  offline-capable at the odoo layer (D1 resilience-posture flag: D1
  records "no local-fallback generation in the client" as the product
  posture; the contingencia duty is a legally-mandated local-generation
  case — this FR flags the tension for an explicit architecture ruling
  rather than silently assuming either side). The emitter bears
  responsibility for pre-validity: the local XML shall be checked
  against the XSD (and the locally-mirrorable business rules) BEFORE
  delivery so the later re-send is not rejected. (LB-009; LB-013;
  EVID-144, EVID-088; D1)
- **GT-EINV-FR-221:** Every contingencia document shall carry a
  *Número de Acceso* (access number) generated by the emitter's billing
  system at random within 100000000–999999999 (9 digits), consigned in
  the XML and printed so the receiver can retrieve the certified DTE on
  SAT's portal without a password; it is a contingencia-only accessor —
  never a numbering substitute (back-ref GT-EINV-FR-195 in the 05
  file). (LB-011; LB-009; EVID-142, EVID-144)
- **GT-EINV-FR-222:** The contingencia graphic representation shall be
  identified with the title "Documento en contingencia" and carry at the
  foot the verbatim text "Emisión en contingencia, obtenga su DTE
  certificado en el sitio https://portal.sat.gob.gt/portal/verificador-integrado/"
  with the Número de Acceso printed in place of the certificador's
  authorization number; contingencia documents shall never be
  "formularios preimpresos" (preprinted forms). The 19_ legend URL
  www.sat.gob.gt/efactura is STALE and shall appear nowhere (R7; layout
  ownership: `07_display-representation.md`, forward anchor). (LB-009;
  LB-013; EVID-144, EVID-088; R7)
- **GT-EINV-FR-223:** On contingency end, the emitter shall file the
  *Aviso de Contingencia* (contingency notice) via Agencia Virtual
  (apartado Factura Electrónica en Línea) — or, in its absence, email it
  to efactura@sat.gob.gt — capturing exactly five fields: Fecha y hora
  de inicio; Fecha y hora en que finalizó; Número de establecimiento;
  Motivo; Cantidad de documentos emitidos. Filing happens outside the
  product (SAT portal/email): the product shall capture the five fields,
  track the notice as a pending/filed checklist item on the contingency
  batch, and never pretend to file it automatically. (LB-009; LB-013;
  EVID-144, EVID-089)
- **GT-EINV-FR-224:** Upon reconnection with the certificador, ALL
  contingencia documents shall be re-sent "de forma inmediata"
  (immediately): the product shall queue contingencia DTEs and
  auto-flush the queue as soon as connectivity returns, with the
  Número de Acceso embedded in each XML. NO numeric re-send deadline
  (days/hours) shall be encoded anywhere — none is printed in the
  current authority nor in 19_ ("fuera del plazo establecido" defers
  without a number); the aviso is what protects the batch from
  late-arrival rejection (FR-223); any regularization-deadline doctrine
  → GOQ-38 (OQ-001). (LB-009; LB-013; EVID-144, EVID-089)
- **GT-EINV-FR-225:** Re-sent contingencia documents re-enter the normal
  certification pipeline: the certificador assigns the número de
  autorización (UUID v4), Serie and Numero only then (never
  emitter-assigned), while the Número de Acceso is retained on the
  record as the contingencia accessor; a contingencia document rejected
  on re-send follows the normal rejection paths
  (`05_certificador-interface.md` FR-179). (LB-009; LB-011; EVID-144,
  EVID-142; back-ref GT-EINV-FR-180/FR-181)

### 3.6 CF-replacement model (Reglas v2.0 §4.2)

- **GT-EINV-FR-226:** The CF-replacement flow shall implement: a DTE
  emitted to *CF* (consumidor final — final consumer) under this model
  lets the customer obtain a NIT-bearing certified DTE within at most
  5 calendar days of the emission date; upon the customer's NIT request
  inside that window, the system AUTOMATICALLY cancels (anula) the CF
  document through this file's anulación flow and reissues the DTE
  preserving the same operational data — lines, amounts, dates, parties
  — with ONLY the número de autorización, serie and número changing.
  Day 6 onward the replacement window is expired and the surface shall
  say so (the customer's retrieval right lapses; no silent extension).
  (LB-010; EVID-144)
- **GT-EINV-FR-227:** The CF-replacement model shall be gated on the
  certificador service ("solo estará disponible con servicio de un
  Certificador — tercero autorizado"): the feature is offered only when
  the company's provider profile is a third-party certificador (never
  on SAT free-channel emulation), and the CF document in this model
  shall carry the verbatim footer "Para obtener el Documento Tributario
  Electrónico (DTE) certificado con su NIT y NOMBRE debe ingresar en un
  plazo máximo de 5 días calendario al sitio web: …" completed with the
  current verifier site (FR-222 URL; layout anchor: 07 file).
  (LB-010; LB-009; EVID-144)

### 3.7 Supersession ledger (R7): 2018 manuals vs Reglas v2.0

Reglas y Validaciones v2.0 (19/12/2024, vigencia abril 2025) governs
EVERY divergence below (R7); the 2018 items are retained only as
historical/test-design input. Behavior ownership column keeps FRs
single-homed.

| # | 2018 item (source) | Current authority (Reglas v2.0) | Resolution / owner |
|---|--------------------|--------------------------------|--------------------|
| 1 | Anulación 5-day window: v1.5 20/12/2019 "no anular más allá de 5 días en el pasado" (changelog); 20_ portal phrasing "durante el mes en que fue emitido y como máximo hasta la fecha de vencimiento de la declaración del IVA" (EVID-092) | §3.16.7.1: IVA-declaration due date of the emission period + §5.5.1.b prescription ceiling (EVID-143; changelog evolution EVID-114) | Reglas v2.0 governs; FR-204..FR-206. 20_ phrasing = same substance, portal-era wording — historical illustration (GOQ-37 kin) |
| 2 | 19_ contingencia retrieval legend URL "www.sat.gob.gt/efactura" (EVID-088) | §4.1.e footer: "https://portal.sat.gob.gt/portal/verificador-integrado/" (EVID-144) | Reglas v2.0 governs; FR-222; stale URL appears nowhere |
| 3 | 19_ re-send deadline wording: "fuera del plazo establecido" — defers, prints no number (EVID-089) | §4.1: "de forma inmediata deberá enviar todos los documentos que generó en contingencia" — immediate, no numeric deadline (EVID-144) | Reglas v2.0 governs; FR-224; no numeric deadline encoded; doctrine gap → GOQ-38 |
| 4 | 19_ contingencia defined as connectivity failure only, §1.2 (EVID-086); 18_ mentions "contingencia por casos fortuitos" (EVID-083 xref) | §4.1 states one mechanics set, no class taxonomy (EVID-144) | Unresolved doctrine (both classes? different mechanics?) → GOQ-38 (OQ-001); product keys on "certification unobtainable" (FR-219) |
| 5 | 19_ §1.5: self-certifiers must use a third party for contingency documents (EVID-090) | §4.1 does not reprint the restriction | Reglas v2.0 governs the mechanics; restriction retained as historical input — product posture unaffected: contingencia flow always travels via a third-party provider profile (FR-220, FR-224); GOQ-38 adjacent |
| 6 | 19_ §1.5: "Debe incluirse la firma electrónica del Emisor en la representación gráfica" — emisor e-signature on the contingency print (EVID-090) | §4.1 lists title/Número de Acceso/footer only; print-signature duty not restated (EVID-144) | Open → GOQ-38 (OQ-001); current-authority list ships as-is (FR-222); the XML emisión signature itself is FR-214/05-file territory |
| 7 | 17_ 2018 casos treated frase tipo 4 scenarios >12 as error (bounds 1–12) | Frase tipo 4 catalog runs escenarios 1–35 (34 absent) + 36 cited in 2.6.1.27 (EVID-131/132) | Reglas v2.0 governs; behavior owned by `03_validation-rules.md` (frases FRs); recorded here for R7 completeness |
| 8 | 20_ portal anulación flow: UUID + receptor NIT/CF + contraseña + button "Certificar DTE" [sic] (EVID-091) | Current anulación path = emisor request through a certificador (§5.5; cross-certificador allowed §3.16.5) | Reglas v2.0 governs; FR-211/FR-213/FR-214; portal flow = historical illustration; manual is undated (GOQ-37 kin, owned by the 08-task file) |

## 4. Data Model

**Anulación window inputs (external calendar — D15/D16 dated rows; never
hardcoded; sourcing → GOQ-14 kin):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.iva_calendar | período impositivo | char(7) YYYY-MM | emission period of the DTE | FR-204; EVID-143 |
| l10n_gt.iva_calendar | fecha_vencimiento | date | IVA monthly-declaration due date for the period (per NIT-last-digit row where applicable) | FR-204; EVID-143; GOQ-14 kin |
| l10n_gt.iva_calendar | nit_last_digit (optional) | char(1)/null | calendario perpetuo split when the calendar is per-digit | FR-204; GOQ-14 kin |
| l10n_gt.anulacion_rule (dated rows, D-GT10) | rule / valid_from / valid_to | char / date / date | "5_day_window" 2019-12-20→2020-12-07 (superseded, history-only); "period_iva_due_date" 2020-12-07→open; Reglas v2.0 row 2024-12-19 (vigencia abril 2025) | FR-204..FR-206; EVID-114 |

**Anulación state on the document (account.move):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (FEL DTE) | anulado state | state/flag | certified → anulado via anulación acuse (immutable original) | FR-216; EVID-156 |
| account.move (FEL DTE) | motivo_anulacion | char(255) | 1..255, local-bounded | FR-214; EVID-015/143 |
| account.move (FEL DTE) | fecha_hora_anulacion | datetime | request timestamp | FR-214; EVID-015 |
| account.move (FEL DTE) | anulacion_acuse_ref | binary | certificador/SAT anulación acknowledgment stored verbatim | FR-213, FR-214; EVID-143/156 |
| account.move (FEL DTE) | anulacion_certificador | m2o provider | may differ from the certifying provider (cross-certificador) | FR-213; EVID-143 |

**Contingencia batch & aviso:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.contingencia.aviso | fecha_hora_inicio / fecha_hora_fin | datetime | Aviso fields 1–2 | FR-223; EVID-144/089 |
| l10n_gt.contingencia.aviso | numero_establecimiento | integer | Aviso field 3 (the emission establishment) | FR-223; EVID-144 |
| l10n_gt.contingencia.aviso | motivo | char | Aviso field 4 | FR-223; EVID-144 |
| l10n_gt.contingencia.aviso | cantidad_documentos | integer | Aviso field 5 (auto-counted from the batch) | FR-223; EVID-144 |
| l10n_gt.contingencia.aviso | canal / estado | selection | agencia_virtual / email-fallback; pendiente / presentado | FR-223; EVID-144 |
| account.move (contingencia DTE) | contingencia flag / numero_acceso | boolean / integer 9-digit | queued offline; 100000000–999999999 | FR-220, FR-221; EVID-142/144 |

**CF-replacement:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.move (CF DTE under model) | cf_replacement_eligible | boolean | model active only with third-party certificador profile | FR-227; EVID-144 |
| account.move (CF DTE under model) | replacement_deadline | date (computed) | fecha emisión + 5 días calendario | FR-226; EVID-144 |
| account.move (reissued DTE) | reissue_of | m2o account.move | operational data preserved; authorization/serie/número new | FR-226; EVID-144 |

**Reversion (reference data only — not implemented):** the
GT_ReversionDocumento field set (UUID + Serie/Numero + UsuarioSolicitud,
EVID-016) is recorded as schema reference data via
`02_dte-schema.md` FR-066; no product entity.

## 5. Odoo Mapping

Layer split for this file: `saas` = the anulación document state machine,
window computation against the IVA-calendar input, blocker evaluation and
reject-code ingestion, transport orchestration (double-signed
GT_AnulacionDocumento build, acuse storage) — authoritative, with odoo
display surfaces (cancel-flow UI, blocker reasons, advisory texts);
`odoo` = contingencia LOCAL emission — offline-capable XML generation,
Número de Acceso generation, contingencia queue and aviso wizard, the
CF-replacement wizard (D1 resilience-posture flag: contingencia is the
legally-mandated local-generation exception to D1's "no local-fallback
generation in the client" posture — flagged for architecture ruling);
`shared` = the IVA-calendar dated rows, the anulación-rule dated rows and
the supersession ledger reference data. Model names are stable across
Odoo 17/18/19/20; no version-specific behavior is required by this file.
Version-regime note (D12): the anulación-rule rows carry version +
effective window in §4 (v1.5 20/12/2019 → v1.5.4 Rev.1 07/12/2020 →
v2.0 19/12/2024, vigencia abril 2025).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-204 | saas | l10n_gt.iva_calendar + account.move | window computation | Configurable calendar input; no N-day constant; GOQ-14 kin (calendar external) |
| FR-205 | saas | l10n_gt.iva_calendar | prescription ceiling | Hard ceiling; config cannot extend |
| FR-206 | shared | l10n_gt.anulacion_rule | dated rows | D-GT10 ledger rows; 5-day row history-only |
| FR-207 | odoo | account.move | rectification advisory | Advisory surfaced odoo-side; D16 freeze-at-filing honored saas-side |
| FR-208 | saas | account.move | NDEB/NCRE blocker | Blocker reason surfaced odoo-side |
| FR-209 | saas | account.move | CIVA/CAIS blocker | Blocker reason surfaced odoo-side |
| FR-210 | saas | account.move | reject-code ingestion | Outcome-only modeling; no pre-verification claim; cross-topic feeds fiscal-reporting/payroll |
| FR-211 | odoo | account.move (cancel action) | emisor-only ACL | Action restricted to emitting-company users |
| FR-212 | saas | account.move | FEL-only gate | Legacy documents excluded from the flow |
| FR-213 | saas | provider profile + account.move | cross-certificador anulación | Acuse-verification expectation passed to provider; no provider lock-in |
| FR-214 | saas | account.move | anulación payload + acuse | XML build core-side; double signature; immutability enforced; odoo cancel-flow UI originates |
| FR-215 | shared | — | reversion reference row | Record-only; no surface; GOQ-51 kin (05-file OQ-007) |
| FR-216 | saas | account.move | state machine | draft→certified→anulado; contingencia→certified; odoo surfaces states |
| FR-217 | odoo | account.move / wizard | correct-vs-annul routing | Routing surfaced odoo-side; rules authoritative saas-side (03-file FR-137) |
| FR-218 | saas | account.move | emission-date guard | Hard no-override block instantiation (03-file FR-080); odoo shows the historical-class explanation |
| FR-219 | odoo | res.company / emission config | contingencia mode toggle | Keyed on certification-unobtainable; no per-class mechanics (GOQ-38) |
| FR-220 | odoo | account.move (contingencia generation) | local XML builder | Offline-capable; D1 posture flag recorded; XSD authority per 02-file FR-067 |
| FR-221 | odoo | account.move | numero_acceso | Random 9-digit 100000000–999999999 generated client-side; range check shared |
| FR-222 | odoo | report layout (contingencia) | title + footer + accessor | Verbatim title/URL; layout ownership 07 file (forward anchor) |
| FR-223 | odoo | l10n_gt.contingencia.aviso | 5 fields + estado | Manual filing tracked as checklist; never auto-filed |
| FR-224 | odoo | contingencia queue | auto-flush on reconnect | Immediate; NO numeric deadline config exists (GOQ-38) |
| FR-225 | saas | account.move | post-re-send ingestion | UUID/Serie/Numero assigned by provider (05-file FR-180/181); numero_acceso retained |
| FR-226 | odoo | account.move wizard | CF replacement | Auto-annul + reissue preserving operational data; deadline = +5 días calendario |
| FR-227 | odoo | res.company (provider profile) + report | gating + footer | Third-party-certificador-only; verbatim footer text |

## 6. Acceptance Criteria

- **AC-001:** Given an IVA-calendar input row mapping period 2026-07 →
  due date 2026-08-17 and a DTE emitted 2026-07-09, when an anulación is
  requested on 2026-08-15, then it is admissible; when requested on
  2026-08-18, then it is blocked with the window reason — and changing
  ONLY the calendar input row (no code, no N-day constant) changes the
  boundary (FR-204).
- **AC-002:** Given a DTE whose emission period is flagged prescribed in
  the calendar/rule data, when an anulación is requested on any date,
  then it is blocked with the prescription reason (FR-205).
- **AC-003:** Given a certified FACT with a vigente NCRE (or a live
  associated CIVA/CAIS), when an anulación is requested, then it is
  blocked with the respective blocker reason; given the same document
  with no blockers and an open window, then the request is admissible
  (FR-208, FR-209).
- **AC-004:** Given an anulación that SAT rejects because a matching
  retention exists in Retenciones Web (or the document appears in Asiste
  Libros, LET or the Planilla del IVA FEL), when the rejection returns,
  then the surface shows the anulación as rejected with the
  SAT-exclusive blocker family and the product never claimed to
  pre-verify those systems (FR-210).
- **AC-005:** Given a DTE certified through provider A, when the emisor
  requests its anulación through provider B, then the request is
  admitted (cross-certificador) and the provider profile records the
  SAT-acuse verification expectation (FR-213).
- **AC-006:** Given an anulación request with motivo of 256 characters,
  when submitted, then local validation rejects it (1..255); given a
  valid motivo, then the payload is a doubly-signed GT_AnulacionDocumento
  carrying the six required attributes and, after the acuse, the
  original DTE still shows its original UUID/Serie/Numero and content
  unchanged with the anulación annotation linked (FR-214, FR-216).
- **AC-007:** Given the full product surface, when audited, then no
  reversion action/button/API exists — the ReversionDocumento field set
  appears only as schema reference data (FR-215).
- **AC-008 (contingencia round-trip):** Given the certificador
  unreachable, when a document is emitted in contingencia mode, then the
  local XML validates against the current GT_Documento XSD, the print
  shows title "Documento en contingencia" and a Número de Acceso drawn
  at random from 100000000–999999999 in place of the authorization
  number; when the outage ends, then the aviso wizard captures the five
  fields (start, end, establecimiento, motivo, cantidad auto-counted)
  and tracks filing; when connectivity returns, then the queue
  auto-flushes immediately with each XML carrying its Número de Acceso,
  and after certification the record shows the provider-assigned
  UUID/Serie/Numero with the Número de Acceso retained (FR-220..FR-225).
- **AC-009:** Given any contingencia print or PDF in the product, when
  inspected, then the footer URL is
  https://portal.sat.gob.gt/portal/verificador-integrado/ and the string
  www.sat.gob.gt/efactura appears nowhere in the product's outputs
  (FR-222; R7).
- **AC-010 (CF replacement timeline):** Given a CF document emitted under
  the replacement model on day D, when the customer presents a NIT on
  day D+3, then the system auto-annuls the CF DTE through the anulación
  flow and reissues a DTE with identical lines/amounts/dates/parties and
  a new authorization number/serie/número; when the NIT arrives on day
  D+6, then the flow reports the 5-calendar-day window expired; when the
  company's provider profile is a SAT free channel, then the model is
  not offered (FR-226, FR-227).
- **AC-011:** Given the contingencia queue configuration surface and
  codebase, when audited, then no configurable day/hour value gates the
  contingencia re-send — the only behavior is immediate flush on
  reconnection (FR-224; GOQ-38).
- **AC-012:** Given an anulado DTE originally emitted 9 days ago, when a
  replacement is drafted, then any emission date older than the 5-day
  window is refused (hard block, D16) and the surface explains the
  historical non-transmittable class (FR-218).

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C /
§C.1); question text verbatim from the register. This file OWNS GOQ-38.
Kin ids referenced inline only: GOQ-14 (IVA vencimiento calendar —
fiscal-reporting wave), GOQ-37 (20_/21_ undated manuals — owned by the
08-task file), GOQ-51 (16_ API currency incl. reversion ops — owned by
`05_certificador-interface.md` OQ-007).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-38 (owned): "Contingencia doctrine gaps: does current doctrine define both classes (connectivity 19_ vs "casos fortuitos" 18_) with different mechanics; numeric regularization deadline absent; emisor e-signature still required on contingency print?" Guards FR-219 (doctrine classes), FR-224 (no numeric deadline encoded), FR-222 (print content shipped per current-authority list only) and supersession ledger rows 3/4/6; working assumptions shipped (single mechanics set keyed on certification-unobtainable; immediate re-send; current-authority print list). | no | GT synthesis wave S-GT1 → W6 partner ask (SAT doctrine/TotalDoc) | open |
