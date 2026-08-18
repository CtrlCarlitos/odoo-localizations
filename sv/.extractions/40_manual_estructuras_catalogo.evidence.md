# Evidence — 40_manual_estructuras_catalogo.md (pilot)

Source: `sv/sources/40_manual_estructuras_catalogo.md`
Read: 2026-08-16 (pilot) + 2026-08-16 wave 2. Sections read: intro, I–IV, Anexos 1–12, §V structures for **FE, CCFE, CRE**.
**Not yet read: §V remaining 8 structures (NRE 663-810, NCE 811-952, NDE 953-1100, CLE 1215-1340, DCLE 1341-1452, FEXE 1453-1592, FSEE 1593-1704, CDE 1705-1817) — next wave.**
Citation form: section/annex + markdown line numbers of the source file.

---

## EVID-001 Onboarding steps for DTE emitters

- **Loc:** §I (md 120-128). Verbatim: "Paso 1: Complete los requisitos mínimos... Paso 2: Envío de solicitud de ingreso al ambiente para pruebas. Paso 3: Obtener el Certificado de Firma Electrónica y la contraseña de acceso a la API. Paso 4: Ejecutar las pruebas mínimas requeridas. (en esta plataforma se otorgan 2 meses para realizar las pruebas desde el ingreso a la consola...) Paso 5: Presentar la solicitud de Autorización... Paso 6: DGII emitirá la Resolución de autorización... Paso 7: Inicia operaciones emitiendo los tipos de DTE que se hayan autorizado."
- **Gloss:** 7-step emitter onboarding: test-environment request → certificate + API credentials → minimum tests (2-month window from console access) → authorization request/resolution (pre-mandate opt-in only) → operate.
- **Candidate CR:** system must support the emitter onboarding workflow incl. test credentials and the minimum transmission tests (Anexo 1 defines them).
- **Topics:** e-invoicing

## EVID-002 Reception model — seal before delivery

- **Loc:** §II (md 132-136). Verbatim: "el emisor en su sistema interno de facturación, genera el documento electrónico en formato JSON incorporándole su firma electrónica; posteriormente deberá enviarlo a la Administración Tributaria... en caso que el documento electrónico cumpla con las validaciones, dicha Administración le otorgará el 'sello de recepción', que le brinda la calidad de Documento Tributario Electrónico (DTE), siendo hasta este momento, cuando el emisor debe entregar al receptor el DTE."
- **Gloss:** generate JSON → sign → transmit to MH → MH validates → reception seal granted → ONLY THEN deliver to customer. Rejection returns field-level errors for correction and resending.
- **Candidate CR:** the DTE only becomes legally valid with the sello de recepción; delivery to receiver must not precede the seal. Rejected documents return error details per field.
- **Also:** MH stores DTE content and offers public status lookup by código de generación or sello (md 136).
- **Topics:** e-invoicing
- **Xref:** transmission flow detail lives in 22_Manual_Tecnologico; events in 41_manual_eventos_invalidacion.

## EVID-003 Electronic signature — simple cert, issuer = MH, per-emitter infra

- **Loc:** §III (md 150-181). Verbatim: "la Administración Tributaria ha puesto a disposición de los emisores un certificado de firma electrónica simple... Será el Ministerio de Hacienda el responsable de la emisión y resguardo... Es responsabilidad del emisor administrar y desarrollar su propia infraestructura y software que le permita incorporar la firma electrónica."
- **Gloss:** MH issues simple (not advanced) signing certificates; each emitter builds/admins its own signing infrastructure; MH also offers an optional signing service. Signature applies to all 11 DTE types + contingency and invalidation events.
- **Candidate CR:** signing architecture must support MH-issued certificate; JSON signed per JWS standard (md 165-169: "se enviará el documento encriptado como parámetro dentro del cuerpo de la petición"); certificate obtainment flow (contract acceptance → API credentials → public key/private key/CR file, md 173-177).
- **Topics:** e-invoicing
- **Xref:** 27_Manual_Obtencion_Certificado.pdf (certificate flow detail); reference firmadores in tuky-workspace (Go/Java).

## EVID-004 Catalog registry — 32 catalogs with DTE applicability matrix

- **Loc:** §IV Catálogo General table (md 190-223).
- **Gloss:** 31 live catalogs (CAT-008 deleted) mapping codes used across DTE fields, each with the DTE types/events it applies to. Notables:
  - CAT-001 Ambiente (Prueba/Producción); CAT-002 Tipo de Documento; CAT-003 Modelo Facturación; CAT-004 Tipo Transmisión (normal/contingencia); CAT-005 Tipo Contingencia; CAT-006 Retención IVA MH (only CRE, FSEE); CAT-007 Tipo Generación (físico/electrónico); CAT-009 Tipo establecimiento; CAT-010 Servicio Médico; CAT-011 Tipo Ítem (bien/servicio/ambos/otros tributos); CAT-012/013 Departamento/Municipio; CAT-014 Unidad de Medida; CAT-015 Tributos; CAT-016 Condición Operación; CAT-017 Forma Pago; CAT-018 Plazo; CAT-019 Actividad Económica; CAT-020 País; CAT-021 Otros Documentos Asociados; CAT-022 Tipo documento receptor; CAT-023 Tipo Documento Contingencia; CAT-024 Tipo Invalidación; CAT-025 Título traslado bienes (NRE); CAT-026 Tipo Donación; CAT-027 Recinto Fiscal (FEXE); CAT-028 Régimen (FEXE); CAT-029 Tipo Persona (FEXE); CAT-030 Transporte (FEXE); CAT-031 INCOTERMS (FEXE); CAT-032 Domicilio Fiscal (CDE).
- **Candidate CR:** all 31 catalogs must be loaded as reference data (machine-readable in catalogs XLSX v1.2, sheet Hoja1); deleted CAT-008 must NOT be loaded.
- **Note:** CAT-019 activity codes are published on MH web (link in source is broken/google-redirect — needs the real URL).
- **Topics:** catalogs, e-invoicing

## EVID-005 Número de Control structure (31 chars)

- **Loc:** Anexo 3 (md 3662-3685). Verbatim: "dividido en 4 Secciones... 'DTE'... Código de Tipo de Documento según CAT-002... 8 dígitos Alfanuméricos... código de Casa Matriz, sucursal o Agencia, Bodega y/o Predio o Patio (4 dígitos) seguido del código de punto venta (4 dígitos)... 15 dígitos numéricos... secuenciales y se reiniciarán cada año... 31 caracteres contando los guiones... no debe de repetirse en un año calendario."
- **Gloss:** `DTE-{type:2}-{branch/POS:8}-{seq:15}`; sequence resets yearly; uniqueness per calendar year; transition-period note: 3rd section currently numeric-only.
- **Candidate CR:** control-number generator per format + yearly reset + uniqueness constraint.
- **Topics:** e-invoicing
- **Doubt:** "por periodo de transición" — is alphanumeric already allowed? Confirm in 19/22 manuals.

## EVID-006 Cargos/Abonos que no afectan la base imponible

- **Loc:** Anexo 4 (md 3687-3716). Verbatim: "no están sujetos a impuestos y serán sumados o restados... hasta el campo 'Total a Pagar'... se ingresarán en el cuerpo del documento como un ítem más... valores positivos y negativos..." with the item-filling table (qty=1, unidad medida=99, all sale fields $0.00, tributo=Null).
- **Gloss:** non-taxable charges/credits are transmitted as body items with a fixed fill pattern (UM 99, zeros elsewhere, signed amount only in that field); consolidated total must appear in resumen field "Total Cargos/Abonos...". Applies FE, CCFE, FEXE (FEXE: "ventas afectas" wording, no exentas/no sujetas).
- **Candidate CR:** support non-taxable charge/credit lines with exact fill rules + summary consolidation.
- **Topics:** e-invoicing, taxation

## EVID-007 CAT-015 Tributos — three sections with distinct mechanics

- **Loc:** Anexo 5 (md 3718-3831).
  - **Sección 1 (per-item, consolidated in resumen):** IVA 13% (20), IVA exportaciones 0% (C3), Turismo alojamiento 5% (59), Turismo aéreo $7.00 (71), FOVIAL D1 $0.20/gal, COTRANS C8 $0.10/gal, otros D4/D5. Multiple codes per item, comma-separated; resumen shows consolidated code/name/value per tax type. C3 only for FEXE (and CLE when required), value $0.00 still detailed.
  - **Sección 2 (own body item, tipo ítem=4):** cemento 57, primera matrícula 90, combustible A8, armas A6, D4/D5. Filled as an independent item: qty 1, UM 99, precio unitario = tax value, ventas gravadas = tax value, código tributo "20-IVA" (i.e., the special tax line itself carries IVA!). Cement example: 100 bags $8 → gravadas $800 + item 2 (tax $32) → total gravadas $832.
  - **Sección 3 (informative only):** bebidas alcohólicas C5 8%, tabaco cigarrillos C6 39%, tabaco cigarros C7 100%. Reflected in resumen but NO effect on total a pagar.
- **Candidate CRs:** (a) per-item multi-tax with summary consolidation; (b) special taxes as separate line items that themselves carry IVA; (c) ad-valorem informative taxes excluded from totals; (d) C3 mandatory $0.00 detail on FEXE.
- **Topics:** e-invoicing, taxation (FOVIAL/COTRANS quantity-based challenge confirmed here)
- **Xref:** 31_Guia_FOVIAL_COTRANS; Ley IVA for legal basis of each tax.

## EVID-008 Documentos Relacionados — max 50 docs / 2000 items, same-type only

- **Loc:** Anexo 6 (md 3833-3928). Verbatim: "un máximo de 50 documentos que entre sí, podrían sumar hasta un máximo de 2000 ítems o líneas... deberán ser del mismo tipo... obligatorio para NCE y NDE... cuando la operación no lo requiera... deberá completar la sección con la palabra Null."
- **Gloss:** related-documents section: mandatory for NC/ND (they adjust prior docs), conditional elsewhere (Null when N/A); same document type within one DTE; physical (correlative) and electronic (código generación) docs can mix; 4 fields (tipo documento, tipo generación 1-físico/2-electrónico, número, fecha). Worked example: one NCE adjusting 3 CCFs (mixed physical/electronic) with per-item adjustments mapped to each doc.
- **Also (md 3925-3928):** related docs must be ACTIVE with reception seal; DCLs referenced without seal must be transmitted within their deadlines by the issuer.
- **Candidate CRs:** related-document section model + validation rules (same type, active, sealed) + NC/ND mandatory linkage + per-line doc attribution in body items ("Número de documento relacionado" column).
- **Topics:** e-invoicing
- **Xref:** invalidation interplay in EVID-009; NC/ND "only for CCF" rule from hint layer needs confirmation from legal sources (Código Tributario), NOT stated here.

## EVID-009 Otros Documentos Asociados

- **Loc:** Anexo 7 (md 3930-3992). FE/CCFE/FEXE/CDE; CAT-021 codes 1=emisor, 2=receptor, 3=médico, 4=transportista. Max 10 lines (FE/CCFE), 20 lines (FEXE). Field sets differ per code (1/2: doc id + description; 3: médico name/NIT/foreign-id/CAT-010 service; 4: transporte CAT-030 + vehicle + conductor). CDE: only 1/2, at least one Donatario record mandatory.
- **Topics:** e-invoicing

## EVID-010 Discounts — per-item and global, with FEXE/FSEE naming variants

- **Loc:** Anexo 8 (md 3994-4052). Two mechanisms: per-item field (consolidated per line, subtracted from qty×price before sale-type totals) and three global summary fields by sale type (no sujetas/exentas/gravadas) + optional global percentage field (no % symbol, e.g. "10") + informative total-discount field (sum of both). When unused: $0.00 mandatory. FEXE: "gravadas"→"afectas"; FSEE: single "ventas" field.
- **Topics:** e-invoicing, taxation

## EVID-011 Payment fields — condition drives shape

- **Loc:** Anexo 10 (md 4082-4180). Condición (CAT-016): 1 Contado (1..n payment methods, no plazo), 2 Crédito (forma + plazo CAT-018 [01 días/02 meses/03 años] + periodo number), 3 Otro (mixed; plazo fields only on the credit portion). Reference required except "billetes y monedas" (Null). Worked examples for each.
- **Topics:** e-invoicing

## EVID-012 Donación items

- **Loc:** Anexo 11 (md 4182-4213). CAT-026: 1 Efectivo (qty 1, UM 99, dep $0), 2 Bien (real UM from CAT-014, depreciation allowed for used goods), 3 Servicio (UM 99, dep $0). Valor Donado = unitario × cantidad − depreciación. Multiple/mixed donation types per document, one item each.
- **Topics:** e-invoicing

## EVID-013 Rounding and tolerance rules

- **Loc:** Anexo 12 (md 4215-4280). Body fields: 11.8 (8 decimals); round 9th decimal up if ≥5, else keep. Resumen: 2 decimals, round 3rd up if ≥5. Tolerance (holgura): resumen fields accept ±$0.01 vs computed. Worked examples confirm MH runs arithmetic validation on reception — mismatches cause rejection.
- **Candidate CR:** enforce rounding at JSON generation; totals within ±0.01 of rounded line sums.
- **Topics:** e-invoicing

## EVID-014 Invalidación — type-driven replacement rules per DTE

- **Loc:** Anexo 9 (md 4054-4080). Tipo invalidación (CAT-024): 1 = error in DTE info, 2 = rescind operation, 3 = otro. Types 1/3: must FIRST transmit + seal the correcting document, then invalidate, referencing both codes. Type 2: Null in replacement field. NCE/CLE exception: even for 1/3, replacement field is Null; invalidate first, then re-issue. Full matrix per DTE type (FE, CCFE, NCE, NDE, NRE, CRE, CLE, DCLE, FEXE, FSEE, CDE) including: CCFE linked to active NC/ND cannot be invalidated until the NC/ND is invalidated; CCFE referenced by CRE can be invalidated without touching CRE (CRE adjusts via NCE); related docs don't need co-invalidation (with the DCL-transmission obligation from EVID-008).
- **Candidate CRs:** invalidation workflow state machine per DTE type + precondition checks (active NC/ND block) + replacement-doc sequencing.
- **Topics:** e-invoicing
- **Xref:** 41_manual_eventos_invalidacion.md (event structure); deadlines table from hint layer (1 day / 3 months) — confirm there.

## EVID-015 Anexo 1 — minimum transmission tests

- **Loc:** Anexo 1 (md 1859-1876, not read in detail). Placeholder for next pass — needed for the onboarding test requirement (EVID-001).

---

## Open questions from this pass

1. **OQ:** Is the 3rd section of Número de Control alphanumeric now, or still numeric-only in transition? (EVID-005)
2. **OQ:** Real URL for CAT-019 activity codes (source link broken). (EVID-004)
3. **OQ:** NC/ND applicability rules (hint: "only CCF") — not in this document; needs Código Tributario/06 guide confirmation. (EVID-008)
4. **OQ:** Invalidation deadlines (1 day vs 3 months) — confirm in 41_manual_eventos_invalidacion. (EVID-014)

## Topic tag summary

e-invoicing: EVID-001..003, 005..014 · catalogs: EVID-004 · taxation: EVID-006, 007, 010

---

## EVID-016 FE v1 — identification & baseline structure

- **Loc:** §V.1a Identificación (md 291-306). Fields: version=`1`, ambiente (CAT-001), tipoDTE=`01`, numeroControl 31ch, codigoGeneracion UUID v4 UPPERCASE, tipoModelo (CAT-003; deferred only in contingency), tipoOperacion (CAT-004; contingency only with deferred model), tipoContingencia (Null unless transm. 02; CAT-005), motivoContin (required iff contingency type 5; ≤500), fecEmi `YYYY-MM-DD`, horEmi `HH:MM:SS` 24h, tipoMoneda `USD` default.
- **Gloss:** FE is the B2C document. UUID must be uppercase. Transition note repeated: 3rd numeroControl section = 8 alphanumerics ("durante la transición deberá completar los 8 espacios alfanuméricos").
- **Topics:** e-invoicing

## EVID-017 FE v1 — receptor rules (B2C)

- **Loc:** §V.1a Receptor (md 342-352). tipoDocumento CAT-022: `13` DUI for natural persons NOT registered in IVA; `36` NIT with DUI accepted when taxpayer homologated DUI as NIT. receptor.nombre REQUIRED only when operation ≥ $200 (else Null). NRC optional no-leading-zeros. Address/phone/email optional.
- **Candidate CR:** partner identification type mapping (CAT-022), conditional name requirement at $200 threshold.
- **Topics:** e-invoicing

## EVID-018 FE v1 — IVA-INCLUSIVE pricing

- **Loc:** §V.1a Cuerpo (md 385, 389). Verbatim: precioUni "(precios con inclusión del impuesto IVA)"; ventaGravada "(ventas con inclusión de IVA)... resultado de: [(precio unitario * cantidad) - 'Descuento, Bonificación, Rebajas por ítem']".
- **Gloss:** in FE, unit prices and gravadas INCLUDE IVA. IVA is NOT added to totals; resumen.totalIva and cuerpo.ivaItem are informative-only for MH (md 393, 418). venteGravada formula: (price × qty) − discount.
- **Candidate CR:** FE tax computation = tax-included price extraction (Odoo price-incl tax mode); totals exclude added IVA.
- **Topics:** e-invoicing, taxation

## EVID-019 FE v1 — resumen formulas

- **Loc:** §V.1a Resumen (md 399-426). subTotalVentas = NoSuj + Exenta + Gravada. subTotal = sumatoria − global discounts. montoTotalOperacion = subTotal + tributo values (excluding informative C5/C6/C7; worked example $177+$10+$5=$192). totalPagar = montoTotal ± (ivaRete1, reteRenta, totalNoGravado); floor at $0.00. totalLetras required (8-200 chars). saldoFavor negative. condicionOperacion CAT-016 drives pagos block (1-contado: n payment rows; 2-crédito: montoPago=$0.00 + plazo CAT-018 + periodo; 3-otro: mixed). saldo a favor → condición 1 + forma pago 99-otros. numPagoElectronico (NPE) optional.
- **Topics:** e-invoicing

## EVID-020 FE v1 — extension/apéndice thresholds

- **Loc:** §V.1a Extensión/Apéndice (md 432-445, 451). FE: entrega/recibe responsible fields all optional (unlike CCFE — see EVID-025). placaVehiculo for fuel stations. Apéndice: 1-10 custom field triplets. Sello NOT part of outbound JSON — MH response only; must appear in Versión Legible (except contingency docs).
- **Versión Legible categories** (md 455-462): A=must show, B=show if applicable, C=never show, D=if unused print name + dash. Layout is suggested, categories are binding.
- **Topics:** e-invoicing

## EVID-021 FE v1 — other sections

- **Loc:** §V.1a. documentoRelacionado: FE may relate ONLY 04 (NR) or 09 (DCL) (md 312). ventaTercero (NIT + nombre) for third-party sales (md 370-371). otrosDocumentos per CAT-021 (médico etc., md 358-364). cuerpo: numItem 1-2000; tipoItem=4 → tax-as-item (codTributo from CAT-015 §2; then código tributo must be Null for FE; value → ventas gravadas, qty 1, precio=tax value, UM 99); numeroDocumento per-item related-doc attribution (repeats ≤2000, only docs from related section); tributos array syntax "[20,D1]" comma-separated in brackets; PSV informative (tobacco/alcohol, never in readable version).
- **Topics:** e-invoicing

## EVID-022 CCFE v3 — B2B receptor mandatory

- **Loc:** §V.2a Receptor (md 531-541). receptor.nit (9-14, no dashes) REQUIRED, nrc REQUIRED, nombre REQUIRED, codActividad + descActividad REQUIRED (from NRC card primary/secondary/tertiary), full address (depto+muni+complemento) REQUIRED, correo REQUIRED, teléfono optional, nombreComercial optional. Version field = `3`, tipoDTE=`03`.
- **Gloss:** CCFE demands the full contributor profile — Odoo partner validation must enforce it.
- **Topics:** e-invoicing

## EVID-023 CCFE v3 — IVA ADDED (contradicts FE wording)

- **Loc:** §V.2a (md 574-578, 587-604). precioUni (md 574) has NO IVA-inclusion clause (unlike FE md 385). subTotalVentas (md 590) = "Suma de operaciones sin impuestos". Worked example (md 603): subtotal $177 + IVA(20) $23 + FOVIAL $10 + COTRANS $5 = **$215** — IVA is ADDED. Resumen includes ivaPercib1 (IVA percibido/perception, md 600) which FE lacks.
- **Doubt:** md 578 ventaGravada still says "(ventas con inclusión de IVA)" — likely copy-paste from FE. The resumen formula + worked example prove net-of-IVA for CCFE. **Arbitrate with fe-ccf-v3.json schema + Ley IVA Art. 62.**
- **Also:** md 599 CCFE subTotal described as sumatoria **+** global discounts (FE md 411 says −). Formula conflict in source; schema + FE pattern suggest minus. Flag.
- **Candidate CR:** CCFE = net prices + IVA débito fiscal added (Odoo tax-excluded mode).
- **Topics:** e-invoicing, taxation

## EVID-024 CCFE v3 — related docs & tipoItem-4 tax line

- **Loc:** §V.2a (md 501, 571, 579). Related docs: ONLY 04 (NR), 08 (CL), 09 (DCL). codTributo §2 note (md 571b): when a §2 special-tax item is used, its código tributo may contain ONLY `20`-IVA (FE: Null instead — md 582b. Difference recorded; schema arbitrates).
- **Topics:** e-invoicing

## EVID-025 CCFE v3 — responsible parties required ≥ $11,428.57

- **Loc:** §V.2a Extensión (md 621-624). nombEntrega/docuEntrega/nombRecibe/docuRecibe REQUIRED when montoTotalOperacion ≥ $11,428.57 ("requisitos de ley"), else Null. (FE: optional; CRE: same threshold on totalSujetoRetencion.)
- **Candidate CR:** legal threshold trigger for delivery/reception responsible identification.
- **Topics:** e-invoicing
- **Xref:** legal basis in Código de Comercio/CT — confirm during those passes.

## EVID-026 CCFE v3 — source-quality defect (shifted rows)

- **Loc:** §V.2a Resumen (md 606-608). Rows mislabeled: totalPagar described as "en letras"; totalLetras carries saldoFavor's description; saldoFavor carries condición's. Duplicate pagos.codigo rows (609/610); montoTotalOperacion duplicated (603/604). **The JSON schema (fe-ccf-v3.json) is the field-mapping authority** — cross-check during synthesis.
- **Topics:** e-invoicing (process note)

## EVID-027 CRE v1 — retention document structure

- **Loc:** §V.6a (md 1101-1214). tipoDTE=`07`. **NO contingency**: tipoModelo must be 1 (previo), tipoOperacion normal only, tipoContingencia/motivoContin always Null (md 1113-1116). numeroControl 3rd section "8 espacios numéricos" BUT example `DTE-07-W123M456-...` is alphanumeric — internal contradiction (transition rule: numeric; example shows letters). OQ stands.
- **Emisor** = Agente de Retención: NRC may be Null if retention agent has no active NRC (md 1125). **Receptor** = Sujeto de Retención: tipoDocumento (CAT-022) + nit + nombre + address REQUIRED; NRC Null allowed if inactive (md 1144-1153).
- **Cuerpo** (max **500** items, not 2000): per item = related-doc quad (tipoDte, tipoDoc-gen, numDocumento, fechaEmision) + montoSujetoGrav (11,2 — TWO decimals, unlike sales docs' 8) + CodigoRetencionMH from CAT-006 **restricted to codes 22, C4, C9** (md 1166) + ivaRetenido (= montoSujeto × code rate) + descripcion. Cannot mix document types within one CR (md 1161).
- **Resumen:** totalSujetoRetencion, totalIVAretenido, totalIVAretenidoLetras (must append "USD", md 1175). No pagos/ventaTercero/otrosDocumentos sections. Extensión responsible fields required when totalSujetoRetencion ≥ $11,428.57 (md 1180-1183).
- **Doubt/OQ:** structure is IVA-retention-only (ivaRetenido field; no renta field). Hint layer claimed CR covers ISR retentions — the DTE structure doesn't show it. How are income-tax retentions reported electronically (if at all)? Check CAT-006 codes + Código Tributario + F-14.
- **Topics:** e-invoicing, taxation

## EVID-028 NRE v3 — goods-transfer document

- **Loc:** §V.3a (md 663-800). tipoDTE=`04`. Related docs: ONLY 01 (F) or 03 (CCF) — reversed direction: NR relates the SALE docs it precedes; related F/CCF must be active with seal (md 688). Receptor: tipoDocumento CAT-022 required + **bienTitulo CAT-025 (título a que se remiten los bienes) REQUIRED** (md 726) — the consignment/transfer concept field. Receptor name/ID/address required like CCFE. Cuerpo ≤2000 items, same sale-type fields; NR summary tributes allowed: codes 20, 59, 71, D1, C8, D5, D4 (§1 only; md 765). No pagos block in resumen, no ivaRete/reteRenta. Extensión ≥$11,428.57 rule applies (md 774-777). ventaTercero present.
- **Candidate CR:** NR as delivery/transfer document tied to future/past F/CCF, with CAT-025 title concept.
- **Topics:** e-invoicing

## EVID-029 NCE v3 — credit note, CCF/CR adjustments

- **Loc:** §V.4a (md 811-944). tipoDTE=`05`. **documentoRelacionado REQUIRED** (unlike F/CCF): allowed types **03 (CCF) or 07 (CR)** only, 1-50 same-type, active+sealed (md 834-837). Related docs to NCE also include 05/06 per NDE table (see EVID-030 note: NDE relates 03/05/06/07). Receptor = full B2B profile (NIT/NRC/address required). Body: adjustment items reference numeroDocumento per item; ajustes only for sale types the original CCF possesses (md 889-891). Resumen: ivaPerci1 + ivaRete1 present (adjustments to perceptions/retentions); montoTotalOperacion = subTotal + tributos + ivaPercibido − ivaretenido (md 911). NO pagos block. Extensión ≥$11,428.57.
- **Candidate CR:** NC adjusts CCF (or CR) — never F; per-item doc attribution; perception/retention adjustment fields.
- **Topics:** e-invoicing
- **Note:** confirms hint-layer "NC only for CCF" — and extends it: NC also adjusts CR (per md 834 + invalidation matrix EVID-014).

## EVID-030 NDE v3 — debit note

- **Loc:** §V.5a (md 953-1099). tipoDTE=`06`. Related docs: **03 (CCF), 05 (NC), 06 (ND) or 07 (CR)** (md 977) — ND can adjust a prior NC/ND. Same B2B receptor, adjustment body, ivaPercibido/ivaRete1 resumen, montoTotalOperacion = subTotal + tributos + IVA percibido − IVA retenido (md 1060). No pagos block. ≥$11,428.57 rule. Source-quality note: md 1041 ND tributos lists "(20, 59, T1, D1, D8, C5 y D4)" — codes T1/D8/C5 don't match CAT-015 §1 as read in Anexo 5 (should be 71/C8); schema arbitrates.
- **Topics:** e-invoicing

## EVID-031 CLE v1 — liquidation (consignment sales)

- **Loc:** §V.7a (md 1215-1339). tipoDTE=`08`. **No contingency** (normal transmission only, md 1228). Emisor = Comisionista (commission agent), Receptor = Mandante (principal) (md 1233, 1253). Cuerpo ≤**500** items, each item = ONE document being liquidated (F/CCF/FEX/NC/ND allowed, mixed types OK — md 1272); values NET of IVA (md 1276-1278); **invalidated docs entered as NEGATIVE values** — same-period annulments appear twice (+ then −); cross-period only once negative (md 1274). Exportaciones separate field (FEX values only). Resumen: subTotalVentas includes exports; total = montoTotalOperacion + ivaPerci (floor $0.00); NO pagos. CL invalidation releases its documents for re-inclusion in a new CL (md 429 invalidation matrix crossref).
- **Candidate CR:** period liquidation doc aggregating sales docs net-of-IVA with negative re-entry of annulled docs.
- **Topics:** e-invoicing

## EVID-032 DCLE v1 — card-acquirer settlement

- **Loc:** §V.8a (md 1341-1451). tipoDTE=`09`. **No contingency**; normal only. Emisor = Agente Perceptor (card issuer/acquirer), Receptor = Afiliado (merchant) (md 1359, 1379). **Not item-based**: single "cuerpo" = settlement summary: periodoLiquidacionFechaInicio/Fin, codLiquidacion, cantidadDOC, valorOperaciones (gross incl. IVA/tips), montoSinPercepcion + descripSinPercepcion, subTotal, IVA, montoSujetoPercepcion (net), **IVAPercibido = 2% of net** (worked example md 1410), comision + porcentComision + IVAcomision, liquidoApagar, totalLetras. Extensión: nombEntrega/docuEntrega REQUIRED always (liquidation responsible). No related-docs section.
- **Candidate CR:** acquiring-settlement document: 2% IVA perception on card sales; commission + IVA on commission; net payable to merchant.
- **Topics:** e-invoicing, taxation

## EVID-033 FEXE v1 — export invoice

- **Loc:** §V.9a (md 1453-1591). tipoDTE=`11`. Emisor = Exportador + **tipoItemExpor (CAT-011: only 1/2/3), recintoFiscal (CAT-027) & regimen (CAT-028) required when tipo ítem = 1 or 3 (goods), Null for 2 (services)** (md 1492-1494). Receptor = FOREIGN: no NIT/NRC; name, tipoDocumento/numDocumento (CAT-022, up to 30 chars, keep leading zeros), descActividad (free text ≤300), codPais+nombrePais (CAT-020), complemento (full foreign address ≤300), tipoPersona (CAT-029) (md 1499-1509). Body: no ventaNoSuj/ventaExenta; **ventaGravada = "Ventas Afectas"** (exports); **tributos = C3 ONLY** (IVA exportaciones 0%, mandatory even $0.00 — md 1538); noGravado charges allowed. Resumen: seguro + flete fields (md 1549-1550); montoTotalOperacion = afectas − descuento + seguro + flete; totalPagar = montoTotalOperacion ± noGravado − **reteRenta** (md 1553); INCOTERMS (CAT-031) required for goods (tipo 1/3, md 1561-1562). otrosDocumentos: 1/2/4 (transporte: modoTransp CAT-030, placa, conductor) up to 20 lines (md 1514-1520).
- **Candidate CR:** export flow: foreign receiver profile, CAT-027/028/029/031 usage, C3 0% mandatory, seguro/flete in totals, renta retention on exports.
- **Topics:** e-invoicing, special-regimes, taxation

## EVID-034 FSEE v1 — non-IVA-taxpayer invoice

- **Loc:** §V.10a (md 1593-1703). tipoDTE=`14`. Emisor NRC **optional** (sujeto excluido may lack NRC, md 1617). Receptor section = **sujetoexcluido.** prefix: tipoDocumento/numDocumento (CAT-022, DUI for natural persons), name, address required; actividad optional. Body: tipoItem 1-3 only (no tax-items); single "Compra" (sales) amount field — no gravada/exenta/noSuj split (md 1656); precioUni no IVA-inclusion note. Resumen: total operations − global discount = subtotal; **ivaRete1 + reteRenta present** (retentions ON FSEE); totalPagar = subtotal − ivaRete1 − reteRenta (md 1667); pagos block full (condición/formas/plazo/periodo, incl. NPE). Note: FSEE participates in contingencies (per contingency event manual: types 01/03/04/05/06/11/14 — EVID-037) AND CAT-006 Retención IVA MH applies to CRE & FSEE (EVID-004).
- **Candidate CR:** simplified invoice for non-registered receivers with retention fields.
- **Topics:** e-invoicing, taxation

## EVID-035 CDE v1 — donation receipt

- **Loc:** §V.11a (md 1705-1815). tipoDTE=`15`. Normal transmission only (md 1718). Emisor = **Donatario** (recipient of donation) with **receptor.tipoDocumento = 36-NIT ONLY** (md 1726 — mislabeled prefix in source; field sits in Emisor section but names donatario NIT). Receptor = **Donante**: CAT-022 ID, NRC optional, **codDomiciliado (CAT-032: 1 Domiciliado / 2 No Domiciliado)**, codPais (CAT-020); address NOT required when No Domiciliado (md 1753-1757). OtrosDocumentos: codes 1/2 only; **MANDATORY: resolución de calificación como sujeto excluido del donatario** (md 1764). Body: tipoDonacion (CAT-026: 1 efectivo/2 bien/3 servicio), cantidad (1 if cash), depreciación (bienes usados), valorUni, **valor = (valorUni × cantidad) − depreciación** (md 1779). Resumen: valorTotal + totalLetras + pagos (cash-delivery forms CAT-017, only when tipo=1). **Sello arrives 24-72h after transmission** (md 1800) — async seal for CDE.
- **Candidate CR:** donation receipt with mandatory qualification resolution, domiciled-flag-driven address rules, per-type valuation.
- **Topics:** e-invoicing

> **ARBITRATION UPDATE (W3, 2026-08-16):** EVID-023 doubt RESOLVED by Ley IVA Art. 57 (EVID-048): CCF must state IVA **separate from price** → CCFE prices are NET + IVA added. The manual's CCF ventaGravada "(con inclusión de IVA)" wording is a copy-paste defect from the FE structure. FE (consumer) IVA-inclusive stands. Schema cross-check in synthesis to close fully.
