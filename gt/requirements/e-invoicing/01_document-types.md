# GT — E-Invoicing — DTE document types & 26-type taxonomy

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-22 |

## 1. Purpose

This file defines the functional requirements for the Guatemala FEL
*Documento Tributario Electrónico* (DTE, electronic tax document) type
taxonomy: the 26 catalog codes in 11 families defined by Reglas y
Validaciones v2.0 §1.2 (legal identity, Spanish name, English gloss, printed
base legal per type); the taxonomy authority layers (Reglas §1.2 → XSD
`DatosGenerales/@Tipo` working set → acuerdo-level open category); the
v2.0/Decreto 31-2024 additions and the pre-v2.0 21-type history; the
known Reglas/XSD drift (six GH-disabled types, BIDP) under the R5 working
rule; per-type behavior hooks expressed as cross-references (CF Q2,500 cap
list, retention complements, FEPE natural-person receptor, origin caps,
afiliación × type eligibility); the legacy paper Código-Tipo codes accepted
as NC/ND referencia-origen; and the one-journal/many-document-types Odoo
model (D17/D-GT8).

It does **not** cover: the validation-rule detail behind the hooks (emission
windows, receptor canonicalization, totals arithmetic, frases matrix —
`03_validation-rules.md`, cluster E3), complement field structures beyond
the per-type required/allowed mapping (`03_validation-rules.md` §complemento
matrix), the XSD schema set and channel drift beyond the Tipo enumeration
(cluster E2 file; catalog sidecars in
[../catalogs/](_INDEX.md) from Task 1), establishment classification gating
(cluster E7 file), the mandate chronology (cluster E4 file), or tax rate
values (taxation wave). Those files reference this one for the type
taxonomy.

## 2. Legal Basis

Authority order (binding, per master evidence index): Reglas y Validaciones
**v2.0 (19/12/2024, vigencia abril 2025)** governs all validation behavior —
the "v1.7.10/Febrero 2025" cover footer is a stale stamp and is never cited
as content version (R1). XSD/JSON working authority = GitHub 961133c
(ratified-official, OQ1 ruling 2026-08-18); drift is recorded, never
silently resolved. Mandate instruments are cited as "Resolución de
Superintendencia SAT-DSI-nnn" and never for thresholds or sanctions.
Working rulings that bind this file: R5 (implement per Reglas matrices +
GH XSD active set; BIDP flagged XSD-only, never enabled), R16 (CF cap
applies to the 11-type list incl. FACP), R18 (18_'s "20 types" is a
mid-vintage display guide; Reglas §1.2 governs taxonomy).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Reglas y Validaciones v2.0, §1.2 "Tipos de DTE", tabla "No. NOMBRE CÓDIGO USO, CARACTERÍSTICAS Y BASE LEGAL", filas 1–26 (p.ej. "1 Factura FACT … Base legal: Decreto 27-92, Ley del IVA, artículo 29, literal a.") | Rulebook v2.0 §1.2: the 26-type catalog table with per-row use and base legal | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §1.2 pp. 10–14 (EVID-115) |
| LB-002 | Reglas v2.0, historial de ajustes, fila "2.0 19/12/2024": "Se agregan los tipos de DTE: Factura Especifica FEPE / Factura Contribuyente Régimen Primario FARP / Factura Cambiaria Contribuyente Régimen Primario FCRP / Factura Contribuyente Régimen Pecuario FPEC / Factura Cambiaria Contribuyente Régimen Pecuario FCPC … FECHA ENTRADA DE VIGENCIA Abril 2025" | v2.0 changelog (19/12/2024, effective April 2025): adds exactly FEPE/FARP/FCRP/FPEC/FCPC | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §6 changelog p. 146 (EVID-113; chain EVID-114) |
| LB-003 | Reglas v2.0, tabla duplicada pp. 15–17 (filas "5 … FESP" a "21 Factura provisional FACP"; sin FEPE/FARP/FCRP/FPEC/FCPC) | Duplicate legacy table pp. 15–17 = the pre-v2.0 21-type set left in the document (known defect; use the 26-row table) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | pp. 15–17 (EVID-116) |
| LB-004 | GT_Documento-0.2.1.xsd, DatosGenerales/@Tipo: activos en ambos canales "FACT" "FCAM" "FPEQ" "FCAP" "FESP" "NABN" "RDON" "RECI" "NDEB" "NCRE" "CIVA" "CAIS" "NEV" "RANT" "FACP"; GH agrega "FEPE" "FARP" "FCRP" "FPEC" "FCPC" "BIDP" (Boleta de despacho); GH comenta FACA/FCCA/FAPE/FCPE/FAAE/FCAE (activos en cat.desa) | DTE schema Tipo enumeration: 15 common active + 5 Decreto 31-2024 types + BIDP on GitHub; the six agro/electrónico types commented out on GH (active on cat.desa) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Documento-0.2.1.xsd` lines 37–73 + `gt/sources/30_FEL_XSD_cat_catdesa/GT_Documento-0.2.1.xsd` (diff hunk 47,52c54,59) | DatosGenerales@Tipo (EVID-002) |
| LB-005 | GT_Endoso-0.1.0.xsd, @TipoDTE doc "Únicamente puede ser uno de los cuatro tipos de Factura Cambiaria" enums "FCAM" "FCAP" "FCPC" "FCRP" (comentarios: Factura Cambiaria, Factura Cambiaria Pequeño Contribuyente, Factura Cambiaria Contribuyente Régimen Pecuario, Factura Cambiaria Contribuyente Régimen Primario) | Endorsement schema: the four endorsable cambiaria types; inline comments give the FCAP/FCPC/FCRP expansions (GH-only file) | `gt/sources/29_FEL_XSD_cat_github_961133c/GT_Endoso-0.1.0.xsd` | DatosDTEReferencia@TipoDTE (EVID-026) |
| LB-006 | AD 13-2018, Art. 3 (texto según 01_; reformado por Art. 2 del Acuerdo de Directorio 26-2019): "El Documento Tributario Electrónico o DTE … comprende facturas, nota de crédito, nota de débito, nota de abono, recibos y otros documentos autorizados por la SAT. Dichos documentos surtirán los efectos tributarios establecidos en las leyes específicas, según corresponda." | Acuerdo-level DTE taxonomy: invoices, credit note, debit note, abono note, receipts + open category "otros documentos autorizados por la SAT" (extensible by SAT); tax effects per the specific laws | `gt/sources/01_AD_13-2018_FEL.pdf` + `gt/sources/02_AD_26-2019_FEL_reformas.pdf` | 01_ p. 4 Art. 3; 02_ ARTÍCULO 2 (EVID-035) |
| LB-007 | Resoluciones de Superintendencia SAT-DSI 639-2020 / 640-2020 / 1240-2021 / 1350-2022 / 400-2023, Art. 1 ¶2, fórmula recurrente: "constituyendo el Régimen de Factura Electrónica en Línea (FEL) como el único medio para la emisión de los documentos tributarios que se encuentren disponibles dentro del mismo" | Mandate resolutions: FEL is the sole means for the tax documents available within it — no resolution restricts or enumerates DTE types per cohort (regime-level obligation) | `gt/sources/06_SAT-DSI-639-2020_fel_serv_tecnicos.pdf`, `07_SAT-DSI-640-2020_fel_emisores_face.pdf`, `12_SAT-DSI-1240-2021_fel_regimen_general.pdf`, `13_SAT-DSI-1350-2022_fel_pequenos.pdf`, `14_SAT-DSI-400-2023_fel_pequenos_ampliacion.pdf` | Art. 1 ¶2 in each (EVID-075) |
| LB-008 | 18_ (guía, sin fecha), p. 3: "El tipo de documento que corresponda según el régimen del contribuyente, actualmente existen [veinte] tipos: 1. Factura … 20. Nota de Envío" [sic: "existenveinte" run together in source] | Graphic-representation guide's twenty DTE types as of its unspecified date — mid-vintage display list; superseded for taxonomy by Reglas §1.2 (R18) | `gt/sources/18_FEL_guia_requisitos_minimos.pdf` | p. 3 "Tipo de documento" (EVID-082) |
| LB-009 | Reglas v2.0, reglas 2.2.4.11 y 2.2.5.6: "… el contenido de la casilla “Tipo de DTE” es: “FACT, FCAM, FPEQ, FCAP, FCCA, FACA, FAPE, FAAE, FCPE, FCAE, FACP”, y el contenido de la casilla “Gran total” es igual o superior a Q. 2,500.00" (2.19.1.2/2.19.2.4 listan 10 tipos, sin FACP) | CF (final-consumer) receptor cap Q2,500: the 11-type list incl. FACP (R16 conservative rule; 2.19.x prints 10 — GOQ-47) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §§2.2.4, 2.2.5, 2.19 (EVID-122/124/138) |
| LB-010 | Reglas v2.0, §2.5.1 matriz Afiliación IVA × Tipo DTE (p.ej. "1 Factura / 2 Factura Cambiaria: General only"; "27 Factura Especifica: Régimen Primario SI, Régimen Pecuario SI"; nota: "*Requiere contar con establecimiento habilitado para el efecto") + §2.5.3: "Cuando no exista información a consignar en el campo Afilicación del IVA … deberá de consignar la palabra EXE." | Regime → document-type eligibility matrix; EXE sentinel for sin afiliación; matrix row numbers unstable across matrices — key on codes | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §2.5.1 pp. 36–38 (EVID-128) |
| LB-011 | Reglas v2.0, §3.1 catálogo de complementos: "2 Retenciones de factura especial: 2 [Requerido] for FESP"; "14 Retenciones de factura especifica: 2 [Requerido] for FEPE"; "3 Abonos de factura cambiaria: 2 for FCAM/FCCA/FCPE/FCAE/FCRP/FCPC"; "12 Exportación provisional: 2 FACP" | Complement catalog: per-type required complements (0/1/2 semantics) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §3.1 pp. 97–98 (EVID-139) |
| LB-012 | Reglas v2.0, §3.7 fn. 10: "Referencia a un único DTE: Cada Nota de Crédito o de Débito solo puede hacer referencia a un único DTE" + 3.7.1.3: Código Tipo ∈ "1", "2", "7", "8", "9", "30", "32", "37", "38", "53", "57", "60", "62", "63", "66", "67", "68", "69", "72" (impreso idéntico en 3.10.2.5) | NC/ND single-origin rule + the paper "Régimen antiguo" Código-Tipo values accepted as referencia-origen | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §3.7 fn. 10 y 3.7.1.3 (EVID-141) |
| LB-013 | 17_ casos de prueba (Mayo 2018), "Validaciones Nota de Crédito y Nota de Débito": orígenes FACE con códigos 1,2,7,8,30,32,37,38,53,57,60,62,63,66,67,68,69,72; "Error. El número de Autorización del Documento Origen no coincide con ningún DTE registrado en la SAT." | 2018 test battery for NC/ND referencia-origen (historical reference data; FACE code list current per EV01e OQ-9) | `gt/sources/17_FEL_casos_de_prueba.zip` | Validaciones Nota de Crédito y Nota de Débito pp. 2–13 (EVID-110(e)) |
| LB-014 | Decreto 31-2024 (citado por la columna base legal de §1.2: "Factura Especifica FEPE … retendrá el impuesto respectivo por el uno punto cinco por ciento (1.5%) sobre el valor de la factura … Base legal: Artículo 4 Decreto 31-2024"; fila FARP "… Decreto 31 -2024"; fila FPEC "… Sector Pecuario, Hidrobiológico y Apícola"; y por la fila de changelog LB-002) | Decree 31-2024 — statutory origin of the five v2.0 DTE types and the FEPE 1.5% retention; NOW PRIMARY IN CORPUS (85_, read 2026-08-22): the LAW names NO DTE codes — FEPE/FARP/FCRP/FPEC/FCPC are SAT-side designations (Reglas v2.0 changelog + XSD); the law-level hooks are art. 7 a) "Estar inscritos en el Régimen de Factura Electrónica en Línea -FEL-" and art. 7 c) "Emitir en todas sus ventas, facturas de Régimen Primario o Régimen Pecuario, según corresponda, con las características que determine el reglamento." (EVID-808), plus art. 9's buyer-issued FEL factura with 1.5% retention and NIT/CUI identification (EVID-810); the Reglas' FEPE base-legal citation "Artículo 4" vs the law's purchaser-side art. 9 is a flagged source discrepancy (85_ OQ-5) | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` + `gt/sources/85_D31-2024_IntegracionPrimarioAgro.pdf` | §1.2 filas 9/18/20 + changelog p. 146 (EVID-115/113); 85_ arts. 7 y 9 (EVID-808, EVID-810; GOQ-13 resolved) |
| LB-015 | Reglas v2.0, §1.2 nota al pie 1: "En el proceso de Factura Electrónica en Línea, el Emisor que realice exportaciones, debe utilizar el DTE denominado Factura y debe colocar los datos que correspondan en el “Complemento Exportaciones”." | Exports use the FACTURA DTE plus the Exportaciones complement — no dedicated export DTE type | `gt/sources/15_FEL_Reglas_y_validaciones_v1.7.10_2025-02.pdf` | §1.2 fn. 1 (EVID-115) |
| LB-016 | Decisión compartida D17 / D-GT8: `l10n_latam_invoice_document` — un diario FEL, muchos tipos de documento; tipos = registros `l10n_latam.document.type` | Cross-country document-model default D17 and its GT instantiation D-GT8 (one journal, many document types) | `shared/docs/odoo-localization-guide.md` | D17 §"Document-type model" (master-index shared canon) |

## 3. Functional Requirements

### 3.1 Taxonomy & authority layers

- **GT-EINV-FR-001:** The system shall support generation of the 26 DTE
  types with their Reglas §1.2 codes and Spanish names — FACT, FCAM, FPEQ,
  FCAP, FESP, NABN, RDON, RECI, FEPE, NDEB, NCRE, FACA, FCCA, FAPE, FCPE,
  FAAE, FCAE, FARP, FCRP, FPEC, FCPC, CIVA, CAIS, NEV, RANT, FACP — grouped
  in the 11 families of §4 (facturas; pequeño; especiales/abono/recibos/
  específica; notas; agropecuario; electrónico pequeño; electrónico
  especial agropecuario; régimen primario; régimen pecuario; constancias;
  otros), and all type-keyed logic (matrices, catalogs, seeds) shall key on
  the codes, never on Reglas table row numbers (unstable: the duplicate
  pp.15–17 table and the 2.4.1/2.5.1 matrices number the same types
  differently). (LB-001; LB-003; EVID-115, EVID-116, EVID-127, EVID-128)
- **GT-EINV-FR-002:** Taxonomy authority shall be layered: (a) Reglas v2.0
  §1.2 defines the 26-type catalog (binding); (b) the XSD
  `DatosGenerales/@Tipo` GitHub working set (21 active incl. the five
  Decreto 31-2024 types, plus BIDP) constrains what can be emitted today,
  with drift against (a) recorded per FR-003/FR-004; (c) the acuerdo level
  (AD 13-2018 art. 3 as reformed by 26-2019) names only *facturas, nota de
  crédito, nota de débito, nota de abono, recibos* plus the open category
  "otros documentos autorizados por la SAT" — the extensibility hook by
  which new types arrive via SAT technical instruments rather than acuerdo
  reform. (LB-001; LB-004; LB-006)
- **GT-EINV-FR-003:** Per the R5 working rule, generation shall implement
  the Reglas v2.0 matrices for all 26 types AND emit only within the GH XSD
  active set: the six types active on cat.desa but commented out on GitHub
  (FACA, FCCA, FAPE, FCPE, FAAE, FCAE) shall be seeded as flagged,
  disabled-by-default document types — never silently dropped from the
  catalog and never enabled by default; enabling them before SAT answers
  the emittability question is blocked. Their status is an open question →
  OQ-001 (GOQ-16, umbrella GOQ-02). (LB-001; LB-004; R5)
- **GT-EINV-FR-004:** BIDP (*Boleta de despacho*, fuel-distribution
  dispatch docket) exists only in the GH XSD enumeration (IDP ecosystem,
  EVID-013) and is absent from Reglas v2.0; it shall be seeded as an
  XSD-only flagged type that is never enabled in product scope. Its status
  is part of OQ-001 (GOQ-16). (LB-004; EVID-002, EVID-013)
- **GT-EINV-FR-005:** The v2.0 history shall be recorded as dated taxonomy
  rows: FEPE, FARP, FCRP, FPEC, FCPC were added by Decreto 31-2024
  (Reglas changelog row "2.0 19/12/2024", *FECHA ENTRADA DE VIGENCIA Abril
  2025* — valid_from 2025-04); the pre-v2.0 active set was 21 types; the
  duplicate pp.15–17 table in the Reglas IS the stale 21-row set (known
  document defect) and shall not be implemented. The statutory layer is
  now primary in corpus (Decreto 31-2024 = 85_, read 2026-08-22): the LAW
  names NO DTE codes — FEPE/FARP/FCRP/FPEC/FCPC are SAT-side designations
  (Reglas v2.0 + XSD; this file keeps owning the type inventory); the
  law-level hook is art. 7 (FEL inscription + emission of "facturas de
  Régimen Primario o Régimen Pecuario" in ALL sales, characteristics
  deferred to the reglamento — EVID-808) → OQ-002 (GOQ-13, resolved).
  (LB-002; LB-003; LB-014; EVID-113, EVID-114, EVID-116, EVID-808)
- **GT-EINV-FR-006:** The undated 18_ guide's "actualmente existen
  [veinte] tipos" display list shall be treated as a mid-vintage display
  enumeration only (graphic-representation labeling): taxonomy, counts and
  codes shall come exclusively from Reglas §1.2 (26 types) per R18; no
  code path shall branch on the 20-type list. (LB-008; R18; EVID-082)
- **GT-EINV-FR-007:** Exports shall use the FACT DTE (or the régimen
  types carrying the Exp flag where the Reglas allow it) with the data
  placed in the *Complemento Exportaciones* — the system shall NOT model a
  dedicated export document type. (LB-015; LB-001 fn. 1)
- **GT-EINV-FR-008:** Document-type availability shall NOT be configured
  per mandate cohort: no incorporation resolution restricts DTE types per
  cohort (the obligation is regime-level — "los documentos tributarios que
  se encuentren disponibles dentro del mismo"); per-emitter availability
  shall be driven by the §2.5.1 afiliación × type matrix (FR-039) and the
  establishment classification gates (see 03_validation-rules.md and the
  E7 establishment file). (LB-007; LB-010; EVID-075)

### 3.2 The 26 DTE types

Each FR below fixes one type's identity: code, Spanish name, English gloss,
printed base legal, XSD working-set status, and its taxonomy-level hooks.
Validation-rule detail for every hook is cross-referenced, not re-derived
here.

- **GT-EINV-FR-009:** FACT — *Factura* (general invoice; the general-regime
  sales document and the export vehicle per FR-007). Base legal: "Decreto
  27-92, Ley del IVA, artículo 29, literal a." XSD active (both channels).
  Afiliación: General only. All 12 impuestos capable (EVID-127). CF-cap
  list member (FR-035). (LB-001; LB-010)
- **GT-EINV-FR-010:** FCAM — *Factura Cambiaria* (installment/credit
  invoice under the Código de Comercio). Base legal: "Decreto 2-70, Código
  de Comercio, art. 591". XSD active (both channels). Afiliación: General
  only. Carries the *Abonos de factura cambiaria* complement (required)
  for installment schedules; endorsable (LB-005 Endoso family). CF-cap list
  member. (LB-001; LB-005; LB-010; LB-011)
- **GT-EINV-FR-011:** FPEQ — *Factura Pequeño Contribuyente* (small-taxpayer
  invoice, definitive 5% regime; no IVA node). Base legal: "artículo 29,
  literal b." (D-27-92). XSD active (both channels). Afiliación: Pequeño
  Contribuyente only. CF-cap list member. (LB-001; LB-010)
- **GT-EINV-FR-012:** FCAP — *Factura Cambiaria Pequeño Contribuyente*
  (small-taxpayer credit invoice). No separate base legal printed in §1.2
  (cambiaria variant of FPEQ); the name expansion comes from the Endoso
  comments (LB-005) because the XSD Tipo enumeration carries no inline
  expansion (GOQ-16 records the unstated-expansion issue for FACP). XSD
  active (both channels). Afiliación: Pequeño Contribuyente only.
  Endorsable. CF-cap list member. (LB-001; LB-005; LB-010)
- **GT-EINV-FR-013:** FESP — *Factura Especial* (special invoice of
  D-27-92 arts. 52/52"A" special regimes; ISR 5% + IVA retention semantics
  via the *Retenciones de factura especial* complement, required — see
  03_validation-rules.md §complemento matrix). Base legal: "artículo 52 y
  52 A." XSD active (both channels). Afiliación: General, Pequeño, PEQ
  Electrónico, Agropecuario (SI\*), Agropecuario Electrónico Especial
  (SI\*). IVA only among impuestos (EVID-127). Never carries the Exp flag.
  (LB-001; LB-010; LB-011)
- **GT-EINV-FR-014:** NABN — *Nota de Abono* (rebate/abono note tied to the
  factura-especial intermediated regime). Base legal: "artículo 52 “A” …
  artículo 31 [AG 5-2013]". XSD active (both channels). Afiliación: SI in
  all five regimes. No impuestos. Never carries the Exp flag.
  (LB-001; LB-010)
- **GT-EINV-FR-015:** RDON — *Recibo por donación* (donation receipt).
  Base legal: "Decreto 27-92 … artículo 7 numeral 9". XSD active (both
  channels). Afiliación: General + Sin afiliación (EXE); personería-gated
  when EXE. No impuestos. LEPP complement optional. (LB-001; LB-010)
- **GT-EINV-FR-016:** RECI — *Recibo* (receipt issued by exempt entities
  for exempt operations). Base legal as printed: "art. 7 numeral 13 …
  art. 8 numeral 1 … art. 8 numeral 2 … Decreto 20-2018 … art. 35 …
  Artículo 29 literal e". XSD active (both channels). Afiliación: General +
  EXE; personería-gated when EXE. No impuestos. (LB-001; LB-010)
- **GT-EINV-FR-017:** FEPE — *Factura Específica* (specific-regime invoice;
  Reglas §1.2 base legal: "Artículo 4 Decreto 31-2024": "retendrá el
  impuesto respectivo por el uno punto cinco por ciento (1.5%) sobre el
  valor de la factura" — ICT
  retention via the *Retenciones factura específica* complement, required;
  "ICT" expansion resolved from the law: ICT = **"Impuesto a la Confianza
  Tributaria"** (D-31-2024 art. 2, EVID-803 — resolves the catalogs OQ
  29_30_ OQ-10 / GOQ-24 expansion half; label update in
  03_validation-rules.md pending); the law's purchaser-side 1.5% FEL
  retention with NIT/CUI identification is textually art. 9 (EVID-810 —
  the Reglas' art.-4 FEPE citation vs art. 9 discrepancy flagged, 85_
  OQ-5). GH XSD active (v2.0 type). Receptor must be a
  natural person (FR-037). Emitter eligibility: régimen primario/pecuario
  establishments; barred for emitters whose only ClasificacionEmisor is
  productor (1672). No impuestos. (LB-001; LB-002; LB-011; LB-014; LB-010;
  EVID-803, EVID-810)
- **GT-EINV-FR-018:** NDEB — *Nota de Débito* (debit note). Base legal:
  "art. 29, literal c." (D-27-92). XSD active (both channels). Afiliación:
  General only. Single FEL origin (FACT/FCAM) or accepted paper origin
  (FR-040); *Referencias de nota de crédito y débito* complement required.
  Inherits the origin's Exp flag and currency. (LB-001; LB-010; LB-011;
  LB-012)
- **GT-EINV-FR-019:** NCRE — *Nota de Crédito* (credit note). Base legal:
  "art. 29, literal d." (D-27-92). XSD active (both channels). Afiliación:
  General only. Same single-origin, referencias-complement, Exp/currency
  inheritance and origin-cap rules as NDEB (FR-038). (LB-001; LB-010;
  LB-011; LB-012)
- **GT-EINV-FR-020:** FACA — *Factura Contribuyente Agropecuario*
  (agricultural-regime invoice, 5% regime). Base legal: "artículo 54 “A”"
  (D-27-92). GH XSD commented out / cat.desa active → flagged,
  disabled-by-default per FR-003 (GOQ-16). Afiliación: Contribuyente
  Agropecuario. Goods-only (B/S = "B"). No impuestos. CF-cap list member.
  (LB-001; LB-004; LB-010)
- **GT-EINV-FR-021:** FCCA — *Factura Cambiaria Contribuyente
  Agropecuario* (agricultural-regime credit invoice). No separate base
  legal printed in §1.2 (cambiaria variant of FACA). GH commented out /
  cat.desa active → flagged, disabled by default (FR-003). Afiliación:
  Contribuyente Agropecuario. Abonos complement required; endorsable.
  CF-cap list member. (LB-001; LB-004; LB-005; LB-010; LB-011)
- **GT-EINV-FR-022:** FAPE — *Factura Pequeño Contribuyente Régimen
  Electrónico* (electronic small-taxpayer invoice). Base legal: "artículo
  54 “E”" (D-27-92). GH commented out / cat.desa active → flagged,
  disabled by default (FR-003). Afiliación: Pequeño Contribuyente Régimen
  Electrónico. CF-cap list member. (LB-001; LB-004; LB-010)
- **GT-EINV-FR-023:** FCPE — *Factura Cambiaria Pequeño Contribuyente
  Régimen Electrónico* (electronic small-taxpayer credit invoice). No
  separate base legal printed. GH commented out / cat.desa active →
  flagged, disabled by default (FR-003). Afiliación: Pequeño Contribuyente
  Régimen Electrónico. Abonos complement required; endorsable. CF-cap list
  member. (LB-001; LB-004; LB-005; LB-010; LB-011)
- **GT-EINV-FR-024:** FAAE — *Factura Contribuyente Agropecuario Régimen
  Electrónico Especial* (special electronic agricultural-regime invoice).
  No separate base legal printed. GH commented out / cat.desa active →
  flagged, disabled by default (FR-003). Afiliación: Agropecuario
  Electrónico Especial. Goods-only. CF-cap list member. (LB-001; LB-004;
  LB-010)
- **GT-EINV-FR-025:** FCAE — *Factura Cambiaria Contribuyente Agropecuario
  Régimen Electrónico Especial*. No separate base legal printed. GH
  commented out / cat.desa active → flagged, disabled by default (FR-003).
  Afiliación: Agropecuario Electrónico Especial. Abonos complement
  required; endorsable. CF-cap list member. (LB-001; LB-004; LB-005;
  LB-010; LB-011)
- **GT-EINV-FR-026:** FARP — *Factura Contribuyente Régimen Primario*
  (primary-sector regime invoice, Decreto 31-2024; 1.5%/2% regime via
  frase tipo 10). Base legal: "Decreto 31 -2024" (§1.2 row 18). GH XSD
  active (v2.0 type). Afiliación: Régimen Primario only. Carries
  *DestinodelaVenta* (7-value closed list). No impuestos. (LB-001; LB-002;
  LB-014; LB-010)
- **GT-EINV-FR-027:** FCRP — *Factura Cambiaria Contribuyente Régimen
  Primario* (primary-sector credit invoice). No separate base legal
  printed (cambiaria variant of FARP; expansion from Endoso comments).
  GH XSD active (v2.0 type). Afiliación: Régimen Primario only. Abonos
  complement required; endorsable. (LB-001; LB-002; LB-005; LB-011;
  LB-010)
- **GT-EINV-FR-028:** FPEC — *Factura Contribuyente Régimen Pecuario*
  (livestock/aquaculture/apiculture regime invoice, Decreto 31-2024; §1.2
  usage cites "Sector Pecuario, Hidrobiológico y Apícola"; 1.5%/10%/2%
  regime via frase tipo 11). GH XSD active (v2.0 type). Afiliación: Régimen
  Pecuario only. *DestinodelaVenta* value 5 = "Exportación en pie". No
  impuestos. (LB-001; LB-002; LB-014; LB-010)
- **GT-EINV-FR-029:** FCPC — *Factura Cambiaria Contribuyente Régimen
  Pecuario* (livestock-regime credit invoice; expansion from Endoso
  comments). GH XSD active (v2.0 type). Afiliación: Régimen Pecuario only.
  Abonos complement required; endorsable. (LB-001; LB-002; LB-005;
  LB-011; LB-010)
- **GT-EINV-FR-030:** CIVA — *Constancia de Exención de IVA* (IVA exemption
  certificate issued by constitutionally exempt sellers). Base legal:
  "Artículo 9 … Decreto 22-73 … Artículo 31 [Zolic]" (Ley IVA art. 9
  exempt persons; D-22-73 art. 31 Zolic). XSD active (both channels).
  Afiliación: General (SI\*) + EXE (SI\*); establishment-classification
  gated (Exento Constitucional 1703→1704). *Referencias de constancias*
  complement required; retroactive fecha rules (CIVA/CAIS exempt from the
  5-day back window); no frases allowed; origin-capped (FR-038).
  (LB-001; LB-010; LB-011)
- **GT-EINV-FR-031:** CAIS — *Constancia de Adquisición de Insumos y
  Servicios* (input/services acquisition certificate for maquila/ZF
  beneficiaries). Base legal: "Decreto 29-89 … artículo 36 bis …
  artículo 30 “B” [AG 533-89]". XSD active (both channels). Afiliación:
  General (SI\*); emitter must hold the "DECRETO 29-89" special trait in
  RTU; establishment-classification gated (Maquila 2204→2224).
  *Referencias de constancias* complement required; Gran Total capped by
  the origin document (FR-038); max 2 items. (LB-001; LB-010; LB-011)
- **GT-EINV-FR-032:** NEV — *Nota de Envío* (goods-transfer delivery note:
  "traslado de mercancías … no sustituye la obligación" of invoicing). No
  statutory base legal printed beyond the usage text. XSD active (both
  channels). Afiliación: General, Agropecuario, Agropecuario
  Electrónico Especial. *Traslado de mercancías* complement required
  (transportista/placa/origin/destination/motivo; FYDUCA-referenced
  goods). No impuestos; frase tipo 9 required (escenarios 8/9/10 —
  "no sustituye una factura" legends). (LB-001; LB-010; LB-011)
- **GT-EINV-FR-033:** RANT — *Recibo de anticipos* (advance-payment
  receipt). No base legal printed. XSD active (both channels). Afiliación:
  General + EXE (SI\*); personería-gated (barred categories in the §2.5.4
  rules). Services-only (B/S = "S"). Frase tipo 9 required; retention
  declarations may block anulación. (LB-001; LB-010)
- **GT-EINV-FR-034:** FACP — *Factura provisional* (provisional export
  invoice; added to the Reglas chain at v1.7.9 28/05/2024). §1.2 prints no
  expansion beyond "Factura provisional" (the FACP name expansion is
  unstated in both XSD and Reglas — GOQ-16 records it; by family pattern it
  is the provisional/export variant). XSD active (both channels).
  Afiliación: General (SI\* — emitter must be in the Aduanas exporters
  padrón). *Exportación provisional* complement required; finalized by a
  FACT referencing the FACP by UUID with currency/receptor consistency.
  CF-cap list member (R16 conservative rule — the one type whose presence
  differs between rule families). (LB-001; LB-002; LB-009; LB-010; LB-011)

### 3.3 Per-type behavior hooks (cross-referenced)

- **GT-EINV-FR-035:** The CF (consumidor-final) receptor cap — ID Receptor =
  "CF" with Gran Total ≥ Q2,500.00 is invalid — shall apply to the 11-type
  list "FACT, FCAM, FPEQ, FCAP, FCCA, FACA, FAPE, FAAE, FCPE, FCAE, FACP"
  including FACP (R16 conservative rule; the §2.19.x prints of the list
  omit FACP — which list is authoritative for FACP-CF is open → OQ-003
  (GOQ-47)). Enforcement detail (FX conversion, list semantics) →
  03_validation-rules.md. (LB-009)
- **GT-EINV-FR-036:** FESP shall carry the *Retenciones de factura
  especial* complement (ISR 5% + IVA retention arithmetic) and FEPE shall
  carry the *Retenciones factura específica* complement (ICT = Impuesto a
  la Confianza Tributaria, D-31-2024 art. 2 — EVID-803; 1.5% of Gran
  Total); both are "2 Requerido" in the §3.1 complement catalog — field
  structures and validation → 03_validation-rules.md §complemento matrix.
  (LB-011)
- **GT-EINV-FR-037:** FEPE shall accept only natural-person receptores: the
  ID Receptor shall not be an organización/empresa NIT ("El tipo de DTE es
  FEPE y el ID Receptor es un NIT de organización empresa." — Reglas
  2.2.4.12). (LB-009 §2.2.4 context; EVID-122)
- **GT-EINV-FR-038:** NCRE/NDEB shall reference exactly one origin DTE
  (single-origin rule, §3.7 fn. 10) and the CIVA/CAIS Gran Total shall not
  exceed the referenced origin's registered totals (§2.19.2.2/3 when no
  "Régimen antiguo") — amount-cap and cross-certificador detail →
  03_validation-rules.md. (LB-012)
- **GT-EINV-FR-039:** Per-emitter document-type availability shall follow
  the Reglas §2.5.1 afiliación × type matrix, keyed on type codes (matrix
  row numbers are unstable — the same five v2.0 types print as rows 22–26
  in §2.4.1 and 23–27 in §2.5.1), with empty AfiliacionIVA rendered as the
  sentinel "EXE"; footnoted SI\* cells additionally require the enabled
  establishment / payer-profile / exportadores padrón condition. The five
  v2.0 types' rows: FARP/FCRP only in Régimen Primario, FPEC/FCPC only in
  Régimen Pecuario, FEPE in both. (LB-010; EVID-128)

### 3.4 Legacy referencia-origen reference data

- **GT-EINV-FR-040:** The system shall carry the legacy paper Código-Tipo
  values accepted as NC/ND (and constancia) referencia-origen as historical
  reference data: the Reglas v2.0 §3.7.1.3 list — 1, 2, 7, 8, 9, 30, 32,
  37, 38, 53, 57, 60, 62, 63, 66, 67, 68, 69, 72 (printed identically in
  §3.10.2.5) — corroborated by the 2018 17_ test battery (EVID-110 lists
  the same codes minus "9" in the FACE-origin cases). The mapping from
  these codes to the legacy SAT resolution-type catalog is not evidenced →
  OQ-004 (GOQ-48). (LB-012; LB-013)

### 3.5 Journal model

- **GT-EINV-FR-041:** The Odoo model shall follow D17/D-GT8: ONE FEL
  journal carries MANY document types — the 26 types (plus flagged BIDP)
  instantiate `l10n_latam.document.type` records attached to the FEL
  journal, `account.move` selects the type via
  `l10n_latam_document_type_id`, and no per-type journal is created.
  Type-level behavior (availability, complements, caps) is configured on
  the document-type records per the FRs above. (LB-001; LB-004; LB-016)

## 4. Data Model

DTE type catalog (seed data; XSD status = GitHub working set per LB-004;
"flagged" rows are disabled by default per FR-003). Machine-readable
catalog sidecars for frases/unidades/mensajes live in
[../catalogs/](_INDEX.md) (Task 1) and are consumed per type via the
frase/complemento hooks cross-referenced in §3.

| Code | Family | Spanish name (§1.2) | English gloss | XSD active (GH) | Notes |
|------|--------|---------------------|---------------|-----------------|-------|
| FACT | Facturas | Factura | General invoice (export vehicle, FR-007) | yes (both channels) | D-27-92 art. 29 lit. a; 12 impuestos; CF-cap |
| FCAM | Facturas | Factura Cambiaria | Installment/credit invoice | yes (both) | CCom art. 591; Abonos compl.; endosable; CF-cap |
| FPEQ | Pequeño | Factura Pequeño Contribuyente | Small-taxpayer invoice | yes (both) | D-27-92 art. 29 lit. b; no IVA; CF-cap |
| FCAP | Pequeño | Factura Cambiaria Pequeño Contribuyente | Small-taxpayer credit invoice | yes (both) | expansion via Endoso comments; endosable; CF-cap |
| FESP | Especiales | Factura Especial | Special-regime invoice | yes (both) | D-27-92 arts. 52/52"A"; Retenciones compl. (FR-036) |
| NABN | Especiales | Nota de Abono | Abono/rebate note | yes (both) | art. 52"A" + AG 5-2013 art. 31; all 5 regimes |
| RDON | Especiales | Recibo por donación | Donation receipt | yes (both) | D-27-92 art. 7 num. 9 |
| RECI | Especiales | Recibo | Exempt-entity receipt | yes (both) | arts. 7.13/8.1/8.2 + D-20-2018 art. 35 + 29.e |
| FEPE | Especiales | Factura Específica | Specific-regime invoice (D-31-2024) | yes (GH) | v2.0; ICT 1.5%; natural-person receptor (FR-037) |
| NDEB | Notas | Nota de Débito | Debit note | yes (both) | D-27-92 art. 29 lit. c; single origin |
| NCRE | Notas | Nota de Crédito | Credit note | yes (both) | D-27-92 art. 29 lit. d; single origin |
| FACA | Agropecuario | Factura Contribuyente Agropecuario | Agricultural-regime invoice | no (commented GH / active CD) | flagged (FR-003, GOQ-16); art. 54"A"; CF-cap list |
| FCCA | Agropecuario | Factura Cambiaria Contribuyente Agropecuario | Agricultural credit invoice | no (commented) | flagged; Abonos compl.; endosable; CF-cap list |
| FAPE | Electrónico pequeño | Factura Pequeño Contribuyente Régimen Electrónico | Electronic small-taxpayer invoice | no (commented) | flagged; art. 54"E"; CF-cap list |
| FCPE | Electrónico pequeño | Factura Cambiaria Pequeño Contribuyente Régimen Electrónico | Electronic small-taxpayer credit invoice | no (commented) | flagged; Abonos compl.; endosable; CF-cap list |
| FAAE | Electrónico esp. agro | Factura Contribuyente Agropecuario Régimen Electrónico Especial | Special electronic agricultural invoice | no (commented) | flagged; CF-cap list |
| FCAE | Electrónico esp. agro | Factura Cambiaria Contribuyente Agropecuario Régimen Electrónico Especial | Special electronic agricultural credit invoice | no (commented) | flagged; Abonos compl.; endosable; CF-cap list |
| FARP | Régimen primario | Factura Contribuyente Régimen Primario | Primary-sector regime invoice | yes (GH) | v2.0; Decreto 31-2024; DestinodelaVenta |
| FCRP | Régimen primario | Factura Cambiaria Contribuyente Régimen Primario | Primary-sector credit invoice | yes (GH) | v2.0; Abonos compl.; endosable |
| FPEC | Régimen pecuario | Factura Contribuyente Régimen Pecuario | Livestock-regime invoice | yes (GH) | v2.0; "Sector Pecuario, Hidrobiológico y Apícola"; DestinodelaVenta 5 = "Exportación en pie" |
| FCPC | Régimen pecuario | Factura Cambiaria Contribuyente Régimen Pecuario | Livestock-regime credit invoice | yes (GH) | v2.0; Abonos compl.; endosable |
| CIVA | Constancias | Constancia de Exención de IVA | IVA exemption certificate | yes (both) | art. 9 + D-22-73 art. 31 (Zolic); origin-capped |
| CAIS | Constancias | Constancia de Adquisición de Insumos y Servicios | Maquila input-acquisition certificate | yes (both) | D-29-89 art. 36 bis + AG 533-89 art. 30"B"; max 2 items |
| NEV | Otros | Nota de Envío | Delivery note | yes (both) | traslado de mercancías; Traslado compl.; FYDUCA refs |
| RANT | Otros | Recibo de anticipos | Advance-payment receipt | yes (both) | services-only; frase tipo 9 |
| FACP | Otros | Factura provisional | Provisional export invoice | yes (both) | v1.7.9 addition; exportadores padrón; Exportación provisional compl.; CF-cap (R16) |
| BIDP | (IDP ecosystem) | Boleta de despacho | Fuel dispatch docket | yes (GH) | XSD-only, NOT in Reglas v2.0 — flagged, never enabled (FR-004, GOQ-16) |

**Type-registry fields** (seed on `l10n_latam.document.type` /
GT extension):

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.document.type | code | char(4) | the 27 codes above (26 + BIDP) | FR-001, FR-004 |
| l10n_gt.document.type | reglas_name / reglas_row | char / integer | §1.2 Spanish name; row 1–26 (display provenance only — never a logic key) | FR-001; EVID-115 |
| l10n_gt.document.type | xsd_active_gh / xsd_channel_status | boolean / selection | active · commented_gh_cd_active (six) · gh_only (BIDP, five v2.0) | FR-003, FR-004; EVID-002 |
| l10n_gt.document.type | enabled_by_default | boolean | false for the six flagged + BIDP; true otherwise | FR-003, FR-004 |
| l10n_gt.document.type | base_legal | char | §1.2 base-legal column verbatim (see LB-014 for the D-31-2024 rows) | FR-009..034 |
| l10n_gt.document.type | valid_from | date | 2025-04 for FEPE/FARP/FCRP/FPEC/FCPC; null otherwise (dated rows, D16) | FR-005 |
| l10n_gt.document.type | cf_cap_list | boolean | true: FACT, FCAM, FPEQ, FCAP, FCCA, FACA, FAPE, FAAE, FCPE, FCAE, FACP | FR-035 (R16) |
| l10n_gt.document.type | afiliacion_eligible | char list | §2.5.1 columns keyed on code: GEN/EXE/PEQ/ECA/EXI/PRI/PEC + SI\* footnote flags | FR-039 |
| l10n_gt.document.type | required_complement | char list | FESP→retenciones especial; FEPE→RETENC específica; FCAM/FCCA/FCPE/FCAE/FCRP/FCPC→abonos; NCRE/NDEB→referencias nota; CIVA/CAIS→referencias constancia; NEV→traslado; FACP→exportación provisional | FR-036; LB-011 |
| l10n_gt.document.type | endosable | boolean | true: FCAM, FCAP, FCRP, FCPC | LB-005; EVID-026 |
| l10n_gt.legacy.origen.code | codigo_tipo | integer | 1, 2, 7, 8, 9, 30, 32, 37, 38, 53, 57, 60, 62, 63, 66, 67, 68, 69, 72 (historical reference data; interpretation open GOQ-48) | FR-040 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = XML
emission, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Per the wave
brief: document-type configuration = `odoo`; XML emission = `saas`. Model
names are stable across Odoo 17/18/19/20; no version-specific behavior is
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | l10n_gt.document.type (extends l10n_latam.document.type) | code, reglas_name | 27 seed rows (26 + BIDP); all logic keys on code, never row number |
| FR-002 | shared | — | — | Authority-layering contract: both sides resolve the same (Reglas > XSD > acuerdo) order; extensibility hook for future SAT types |
| FR-003 | odoo | l10n_gt.document.type | xsd_channel_status, enabled_by_default | Six flagged types seeded disabled; SaaS refuses their emission while GOQ-16 open (R5); enable requires explicit config + drift re-check |
| FR-004 | odoo | l10n_gt.document.type | enabled_by_default = false (BIDP) | XSD-only row; no journal exposure; IDP annex out of scope |
| FR-005 | odoo | l10n_gt.document.type | valid_from | Dated rows per D16: v2.0 types valid_from 2025-04; duplicate pp.15–17 table never seeded |
| FR-006 | shared | — | — | Display guard: 18_ 20-type list never a taxonomy source; graphic-rep labeling reads the type registry |
| FR-007 | odoo | account.move (document-type selection) | l10n_latam_document_type_id | Export flow selects FACT + Exp; Exportaciones complement attached SaaS-side at XML build |
| FR-008 | odoo | l10n_gt.document.type | afiliacion_eligible | No cohort-keyed availability config exists; cohort calendar (E4 file) never gates type lists |
| FR-009..034 | odoo | l10n_gt.document.type + FEL journal availability | per-type fields of §4 | Type identity/config client-side; XML emission of every type = saas; per-type validation detail → 03_validation-rules.md |
| FR-035 | odoo | l10n_gt.document.type | cf_cap_list | List membership config (incl. FACP per R16); authoritative cap enforcement SaaS-side → 03_validation-rules.md |
| FR-036 | saas | — (complement builder) | — | Retention complements built into the XML at emission; arithmetic (ISR 5% / ICT 1.5%) → 03_validation-rules.md §complemento matrix |
| FR-037 | saas | res.partner (FEPE UX pre-check) | l10n_latam_identification_type_id | Natural-person guard authoritative SaaS-side; odoo partner form warns on organización NIT for FEPE journals |
| FR-038 | saas | account.move | ref/origin fields | Single-origin + constancia/CAIS caps validated at emission; detail → 03_validation-rules.md |
| FR-039 | odoo | l10n_gt.document.type | afiliacion_eligible | Matrix keyed on codes; emitter AfiliacionIVA arrives via certificador mini-RTU feed (E5/E7 files); EXE sentinel handling |
| FR-040 | odoo | l10n_gt.legacy.origen.code | codigo_tipo | Reference data consumed by the NC/ND origin picker for pre-FEL paper documents; GOQ-48 open |
| FR-041 | odoo | account.journal + l10n_latam.document.type | journal_id on types; l10n_latam_document_type_id on moves | D17/D-GT8: one FEL journal, many types; no per-type journals; l10n_latam_invoice_document pattern 17–20 |

## 6. Acceptance Criteria

- **AC-001:** Given the seeded type registry, when counted, then it holds
  exactly 27 rows (26 Reglas types + BIDP) whose codes match Reglas §1.2
  verbatim, and no code path branches on a Reglas table row number.
  (FR-001, FR-004)
- **AC-002:** Given any of FACA/FCCA/FAPE/FCPE/FAAE/FCAE or BIDP, when a
  user attempts to enable it (or emits it), then the action is blocked
  while GOQ-16 is open, and the row carries its drift flag (R5 working
  rule). (FR-003, FR-004)
- **AC-003:** Given the five Decreto 31-2024 types (FEPE, FARP, FCRP,
  FPEC, FCPC), when inspected, then each carries valid_from = 2025-04 and
  a base-legal pointer to D-31-2024 (GOQ-13 resolved: D-31-2024 = 85_
  primary-read; the law names no DTE codes — the law-level hook is art. 7,
  EVID-808), and no
  row from the duplicate pp.15–17 21-type table was seeded. (FR-005)
- **AC-004:** Given an export operation, when the DTE is generated, then
  the type is FACT (never a dedicated export type) and the Complemento
  Exportaciones is present. (FR-007)
- **AC-005:** Given a CF receptor and a Gran Total ≥ Q2,500.00 on any of
  the 11 cf_cap_list types — including FACP — when emission is attempted,
  then it is blocked (R16; FX-converted totals included per the 03 file).
  (FR-035)
- **AC-006:** Given an FEPE whose ID Receptor is an organización/empresa
  NIT, when emission is attempted, then it is rejected (2.2.4.12).
  (FR-037)
- **AC-007:** Given an NCRE or NDEB referencing more than one origin DTE,
  or a paper origin whose Código Tipo is outside the 19-value legacy list,
  then emission is blocked. (FR-038, FR-040)
- **AC-008:** Given an emitter affiliated only to Pequeño Contribuyente,
  when the available types are listed, then FPEQ/FCAP are offered and
  FACT/FCAM are not (matrix keyed on codes; EXE sentinel for sin
  afiliación). (FR-039)
- **AC-009:** Given a company's FEL setup, when document types are
  configured, then all in-scope types hang off ONE FEL journal and each
  account.move carries its own l10n_latam_document_type_id — no per-type
  journal exists. (FR-041)
- **AC-010:** Given any taxonomy-dependent surface (selection lists,
  seeds, display labels), when sourced, then it reads the type registry
  derived from Reglas §1.2 (26) — never 18_'s 20-type display list.
  (FR-006)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text copied verbatim from the register (abbreviations expanded
where noted). This file OWNS GOQ-16.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-16 (owned): "XSD-active-set vs Reglas: are FACA/FCCA/FAPE/FCPE/FAAE/FCAE (active CD, commented GH) still emittable? BIDP (GH-only) vs Reglas silence; FACP expansion unstated (FCAP = 'Factura Cambiaria Pequeño Contribuyente' per Endoso comments)." Blocks FR-003/FR-004 (and the six disabled type FRs); umbrella GOQ-02. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT/TotalDoc) | open |
| OQ-002 | GOQ-13 (kin): "D-31-2024 full text acquisition (added IVA 8-'A'; LAE changes; the 5 new DTE types FEPE/FARP/FCRP/FPEC/FCPC; ICT definition) + clean-DCA verification of D-10-2025's '8 A' reading (OCR 8/3 residue)." Blocks the statutory layer under FR-005/FR-017/FR-026..029 and GOQ-24 (ICT expansion). **RESOLVED in-corpus 2026-08-22: D-31-2024 = 85_ (6pp complete), primary-read end-to-end (EVID-801..819) — the LAW names NO DTE codes (FEPE/FARP/FCRP/FPEC/FCPC stay SAT-side per Reglas v2.0/XSD; law-level hook = art. 7 a)/c), EVID-808); art. 9 = buyer-issued FEL factura, 1.5% retention, NIT/CUI (EVID-810); ICT = "Impuesto a la Confianza Tributaria" (art. 2, EVID-803 — resolves 29_30_ OQ-10 and GOQ-24's expansion half); art. 13 adds IVA 8-"A" verbatim, no "3 'A'" anywhere (EVID-813); art. 18 corroborates LAE "16-2017" vs 74_ title's "168-2017" [sic] (EVID-815). Residual: Reglas' FEPE "Artículo 4" citation vs the law's art. 9 (85_ OQ-5) — kin to 03_validation-rules GOQ-24.** | no | GT synthesis wave S-GT1 (resolved in-corpus 2026-08-22; master-index annotation = controller's) | resolved (2026-08-22) |
| OQ-003 | GOQ-47: "CF Q2,500 DTE list: 11 types (incl. FACP, rules 2.2.4.11/2.2.5.6) vs 10 (2.19.1.2/2.19.2.4) — which authoritative for FACP-CF? Conservative: 11." Affects FR-035 (R16 working rule applied meanwhile). | no | GT synthesis wave S-GT1 → W6 partner ask | open |
| OQ-004 | GOQ-48: "'Régimen antiguo' paper Código-Tipo list (1,2,7,8,9,30,32,37,38,53,57,60,62,63,66,67,68,69,72) needs the SAT resolution-type catalog to interpret." Affects FR-040 (reference data recorded; mapping to legacy document identities unresolved). | no | GT synthesis wave S-GT1 → W6 partner ask | open |
