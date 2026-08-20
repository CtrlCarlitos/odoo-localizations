# GT — E-Invoicing — FEL legal chain, mandate chronology & emisor onboarding

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | e-invoicing |
| Status  | draft |
| Authors | GT synthesis wave S-GT1 |
| Updated | 2026-08-19 |

## 1. Purpose

This file defines the functional requirements for the Guatemala FEL legal
chain and onboarding: the statutory ladder that grounds the electronic
invoicing obligation (Código Tributario arts. 98.5/98"A".2 → Ley IVA
D-27-92 arts. 29-30 → IVA art. 29-"A" added by Decreto 4-2019 art. 6 →
Acuerdo de Directorio 13-2018 as reformed by AD 26-2019 and AD 15-2020 →
the eleven *Resoluciones de Superintendencia* SAT-DSI incorporation
instruments); the mandate chronology modeled as D16 dated rows keyed by
incorporation resolution/cohort (243-2019 → 400-2023, including the
1240-2021 mass mandate and the reglamento-layer AG 222-2019 rules); the
legacy-authorization lapse semantics (deadline clauses, blank-NIT death,
6-month reglamento cap); and the emisor onboarding operational flow from
the 21_ *habilitación* manual (Agencia Virtual enablement, password
policy, *acreditación* of certificadores, downloadable *firma
electrónica*). It also carries the instrument-naming and citation-guard
rules for the mandate corpus.

It does **not** cover: the DTE taxonomy and per-type structure
(`01_document-types.md`, cluster E1), the XSD schema set
(`02_dte-schema.md`, cluster E2), the Reglas v2.0 validation universe
(`03_validation-rules.md`, cluster E3), the certificador authorization
regime and provider interface (`05_certificador-interface.md`, clusters
E5/E7 — AD 13-2018 arts. 14-20 certificador requirements live there), the
anulación/contingencia models (`06_anulacion-contingencia.md`, cluster
E6), or the graphic representation (`07_display-representation.md`,
cluster E8). Those files reference this one for the mandate calendar and
onboarding prerequisites.

## 2. Legal Basis

Authority guards (binding, verbatim from the master index): mandate
instruments are cited as "Resolución de Superintendencia SAT-DSI-nnn-nnnn"
(never "Directorio Superior" — EVID-072); they are NEVER cited for
thresholds (D-27-92 owns them) or for sanctions (none contained —
EVID-074). `01_` is the consolidated edition of AD 13-2018 and is the
operative text (R10); the original 2018 wordings of reformed articles are
not in corpus → OQ-002 (GOQ-28). IVA art. 29-"A" provenance = Decreto
4-2019 art. 6, verbatim in `02_` (EVID-049/050). The SAT-DSI publication
dates come from the gazette headers inventoried in EVID-076; where no
publication date is printed the dated row stays undated (GOQ-33) and
computed dates are marked ≈. Binding rulings for this file: R8 (639/640
dual DCA print = cross-verification asset), R9 (12_ = digest-verified real
1240-2021 text), R10 (01_ consolidated = operative), R21 (FEL-suspension
cites go to CT 98"A".2, never the struck art. 120 ¶).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Código Tributario, Decreto número 6-91, arts. 98 numeral 5. y 98 "A" numeral 2., as quoted in AD 13-2018: "es atribución de la Superintendencia de Administración Tributaria, organizar el sistema de recaudación … y establecer procedimientos para la elaboración, transmisión y conservación de facturas, libros, registros y documentos por medios electrónicos, cuya impresión puede hacer prueba en juicio" / "el numeral 2) del artículo 98 “A” … podrá establecer procedimientos para la elaboración, transmisión y conservación de facturas, recibos, libros, registros y documentos por medios electrónicos" | Tax Code arts. 98.5 and 98"A".2: SAT's faculty to organize collection and to establish procedures for elaboration, transmission and conservation of invoices, books, registers and documents by electronic means — the top statutory rung of the FEL chain | `gt/sources/01_AD_13-2018_FEL.pdf` | p. 1 considerandos (EVID-032); 98"A".2 as quoted in `gt/sources/06_SAT-DSI-639-2020_fel_serv_tecnicos.pdf` considerandos (EVID-073) |
| LB-002 | Ley del Impuesto al Valor Agregado, Decreto número 27-92, arts. 29 y 30, and Acuerdo Gubernativo 5-2013 (Reglamento IVA) art. 29, as quoted in AD 13-2018: "la SAT está facultada para establecer las características de las facturas electrónicas" | IVA Law arts. 29-30 (+ IVA Reglamento art. 29): SAT is empowered to establish the characteristics of electronic invoices — the 2018-vintage IVA hook (before art. 29-"A" existed); D-27-92 also owns every régimen threshold the cohorts reference by registration | `gt/sources/01_AD_13-2018_FEL.pdf` | p. 1 considerandos (EVID-032) |
| LB-003 | Ley IVA art. 29 "A", added by Decreto número 4-2019 (Ley para la Reactivación Económica del Café) art. 6 — provenance verbatim in AD 26-2019: "el Decreto Número 4-2019 …, en su artículo 6 adiciona el artículo 29 “A” al Decreto Número 27-92 …, el cual faculta a la Administración Tributaria para calificar y habilitar de oficio a personas individuales o jurídicas para utilizar el Régimen de Factura Electrónica (FEL)"; content per SAT-DSI-639-2020: "la Administración Tributaria tiene la facultad de calificar … ya sea por el volumen de facturas emitidas, nivel de ingresos brutos facturados, vinculación económica, inscripción a regímenes especiales u otro criterio … y que la resolución … cobrará vigencia tres meses posteriores a su notificación" | IVA art. 29-"A" (added by Decree 4-2019, Coffee Economic Reactivation Law, art. 6): empowers SAT to qualify and compulsorily enable taxpayers into FEL by invoice volume, gross invoiced income, economic linkage, special-regime enrollment or any other SAT-defined criterion, with resolutions taking effect 3 months after notification | `gt/sources/02_AD_26-2019_FEL_reformas.pdf` + `gt/sources/06_SAT-DSI-639-2020_fel_serv_tecnicos.pdf` | 02_ p. 1 considerandos (EVID-049); content quote 06_ considerandos (EVID-073); cited as incorporation basis in 03_ (EVID-050) |
| LB-004 | Acuerdo de Directorio 13-2018 (consolidated edition = operative text, R10): Art. 1 objeto FEL; Art. 11 (texto 26-2019): "La resolución que emita la SAT al contribuyente para su incorporación obligatoria al Régimen FEL, cobrará vigencia tres meses posteriores a su notificación … quedarán sin efecto dichas autorizaciones; el Régimen FEL constituirá el único medio …"; Art. 12 (texto 26-2019): "plazo máximo de seis meses para el uso de las autorizaciones vigentes" (voluntary adoption); Art. 13 (texto 26-2019): "Estar inscrito, actualizado y ratificado en el Registro Tributario Unificado (RTU)"; Art. 13 "A" (adicionado 26-2019): "1. Acreditar el o los certificadores … 3. Utilizar las herramientas electrónicas …"; Art. 25 FACE sunset; Art. 29: "entrará en vigencia quince días después de su publicación en el Diario Oficial" | AD 13-2018 (FEL Regime Agreement): regime scope; compulsory incorporation resolutions effective 3 months after notification with lapse of prior emission authorizations (art. 11); voluntary adoption with 6-month sunset (art. 12); enablement prerequisites RTU registered/updated/ratified + SAT e-means (art. 13); operating conditions incl. certificador accreditation and CT-art.-120 suspension interlock (art. 13"A"); FACE migration programming (art. 25); vigencia 15 days after DCA publication (art. 29 — DCA date not in corpus, GOQ-27) | `gt/sources/01_AD_13-2018_FEL.pdf` | Arts. 1, 11-13 "A", 25, 29 pp. 2-12 (EVID-031, EVID-033, EVID-039, EVID-040, EVID-041, EVID-047, EVID-048) |
| LB-005 | Acuerdo de Directorio 26-2019 (DCA No. 54, 27-Nov-2019; "entrará en vigencia el día siguiente al de su publicación" → 28-Nov-2019): reforms AD 13-2018 arts. 2.b, 3, 11, 12, 13 and adds art. 13 "A" — the post-reform wordings printed in consolidated 01_ | AD 26-2019 (in force 28-Nov-2019): aligns AD 13-2018 with IVA art. 29-"A"; source of the operative arts. 11/12/13/13"A" texts used by this file (original 2018 wordings not in corpus — GOQ-28) | `gt/sources/02_AD_26-2019_FEL_reformas.pdf` | p. 1-2 reform articles + vigencia (EVID-049; reform map EV01b; garbles GOQ-32) |
| LB-006 | Acuerdo de Directorio 15-2020 (DCA "NÚMERO 6", 25-Nov-2020 [edition anomaly GOQ-30]; vigencia next day → 26-Nov-2020): reforms AD 13-2018 art. 15 — "las personas individuales, jurídicas y no lucrativas" eligible as certificador; capital tiers "un millón de quetzales, (Q. 1,000,000.00)" (individual) / "capital autorizado y pagado mínimo de un millón de quetzales" (jurídica) / "activos fijos netos equivalen como mínimo a un valor de cinco millones de quetzales (Q.5,000,000.00)" + 10 años de existencia jurídica (no lucrativas) | AD 15-2020 (in force 26-Nov-2020): widens certificador eligibility to include non-profit legal entities with tiered capital requirements Q1M/Q1M/Q5M and 10-year existence — certificador-market context for the onboarding flow (requirements themselves are certificador-side; file 05_) | `gt/sources/03_AD_15-2020_FEL.pdf` | p. 1-2 ARTÍCULO 1 + vigencia (EVID-050, EVID-042) |
| LB-007 | Resolución de Superintendencia SAT-DSI-243-2019 (11-Mar-2019): "Incorporar al Régimen de Factura Electrónica en Línea FEL, a los contribuyentes que provean bienes, obras, servicios y suministros a las entidades del Estado y sus dependencias, bajo las modalidades de adquisición de, contrato abierto; cotización; licitación; y, subasta electrónica inversa"; "empezará a regir un día después de la fecha de su publicación" (publication date not printed anywhere — GOQ-33) | SAT-DSI-243-2019: first cohort — State suppliers under the 4 contract-level procurement modalities; no incorporation deadline printed; effective the day after publication (undatable from corpus) | `gt/sources/04_SAT-DSI-243-2019_fel_proveedores_estado.pdf` | Artículos 1 y 3; date block (EVID-051, EVID-052) |
| LB-008 | Resolución de Superintendencia SAT-DSI-838-2019 (21-Aug-2019; DCA 11-Sep-2019): cohort "Servicios Profesionales Individuales en General" (definition per AG 122-2016 art. 2 q): "servicios prestados por una persona individual que acredita un grado académico a través de un título universitario y ha cumplido con … la Ley de Colegiación Profesional Obligatoria, Decreto 72-2001") serving "los organismos del estado, entidades descentralizadas y autónomas incluyendo las Municipalidades … establecidas en el artículo 1 del Decreto número 57-92" | SAT-DSI-838-2019 (effective 12-Sep-2019 computed): individual professionals (university degree + active colegiación) rendering services to the whole D57-92 art. 1 state sector; no lapse deadline printed (GOQ-34) | `gt/sources/05_SAT-DSI-838-2019_fel_serv_prof.pdf` | Artículos 1 y 3; DCA header p. 1 (EVID-053, EVID-054) |
| LB-009 | Resolución de Superintendencia SAT-DSI-639-2020 (16-Jul-2020; DCA 30-Jul-2020): cohort Servicios Técnicos to the D57-92 state sector; "El plazo máximo para el uso de las autorizaciones vigentes de otros medios o formas de emisión … será hasta el 31 de diciembre de 2020; transcurrido el plazo referido quedarán sin efecto dichas autorizaciones, constituyendo el Régimen de Factura Electrónica en Línea (FEL) como el único medio …"; "entrará en vigencia tres meses después de su publicación" (≈30-Oct-2020) | SAT-DSI-639-2020 (vigencia ≈30-Oct-2020 computed): technical-services providers to the State; first hard lapse date — all legacy emission authorizations void 31-Dec-2020, FEL the only means thereafter | `gt/sources/06_SAT-DSI-639-2020_fel_serv_tecnicos.pdf` | Artículo 1 both paragraphs + Artículo 3 (EVID-055, EVID-056; DCA data EVID-076) |
| LB-010 | Resolución de Superintendencia SAT-DSI-640-2020 (16-Jul-2020; DCA 30-Jul-2020, same issue as 639 — R8): "Incorporar … a todos los Emisores establecidos dentro del Acuerdo de Directorio número 024-2007, Régimen de Factura Electrónica “FACE”"; "El plazo máximo para el uso de las autorizaciones vigentes establecidas en el Acuerdo de Directorio número 024-2007, será el 31 de diciembre de 2020"; vigencia 3 months post-publication (≈30-Oct-2020) | SAT-DSI-640-2020: regime abolition — ALL FACE emisors migrate to FEL; FACE authorizations die 31-Dec-2020; implements AD 13-2018 art. 25 (FACE sunset) | `gt/sources/07_SAT-DSI-640-2020_fel_emisores_face.pdf` | considerando IV, Artículos 1-2 (EVID-057; dual-print cross-check R8) |
| LB-011 | Resolución de Superintendencia SAT-DSI-887-2020 (8-Oct-2020; DCA 19-Oct-2020): cohort State suppliers under "Compra Directa y Compra de Baja Cuantía" (D57-92 art. 43 a-b); "Se exceptúan … bajo la modalidad de compra de baja cuantia [sic] por un valor menor a dos mil quinientos quetzales (Q.2,500.00)"; "entrará en vigor a partir del uno de abril del año dos mil veintiuno" | SAT-DSI-887-2020: Compra Directa/Baja Cuantía cohort with FIXED vigencia 1-Apr-2021; the only monetary exception in the 11 instruments — baja-cuantía operations under Q2,500.00 per operation are exempt from this mandate | `gt/sources/08_SAT-DSI-887-2020_fel_baja_cuantia.pdf` | considerando IV, Artículos 1, 2 y 4 (EVID-058) |
| LB-012 | Resolución de Superintendencia SAT-DSI-398-2021 (29-Apr-2021; DCA 10-May-2021): cohort State suppliers under "Adquisición con proveedor único, Arrendamientos, Arrendamiento y adquisición de bienes inmuebles y Dragado" (D57-92 art. 43 c-f); "entrará en vigor a los tres meses siguientes contados a partir de la fecha de su publicación" (≈10-Aug-2021); article sequence prints 1, 2, 4 with no Artículo 3 (GOQ-35) | SAT-DSI-398-2021: completes the D57-92 art. 43 modality sweep; COMPLEMENTS (does not extend) 243-2019 — parallel cohort, not an amendment | `gt/sources/09_SAT-DSI-398-2021_fel_proveedores_estado.pdf` | Artículo 1 + vigencia article (EVID-059, EVID-060) |
| LB-013 | Resolución de Superintendencia SAT-DSI-1074-2021 (11-Oct-2021; DCA 19-Oct-2021): market-wide "salud y asistencia social" cohort in 6 categories a)-f) (establecimientos de salud/farmacias y similares; prevención/recuperación/rehabilitación; laboratorios y diagnóstico; bancos de sangre; "Profesionales universitarios, técnicos y auxiliares"; importers/manufacturers/sellers of equipos … y cualquier otro producto farmacéutico y afín); "Se exceptúan … a las entidades del Sector Público"; vigencia 3 months (≈19-Jan-2022) | SAT-DSI-1074-2021: first activity-defined market-wide cohort (not State-procurement-tied), six inclusive verbal categories; Sector Público entities excepted; MSPAS notified | `gt/sources/10_SAT-DSI-1074-2021_fel_salud.pdf` | Artículos 1-4 (EVID-061, EVID-062) |
| LB-014 | Resolución de Superintendencia SAT-DSI-1218-2021 (15-Nov-2021; DCA 24-Nov-2021): market-wide cohort "servicios en materia contable, financiera, tributaria y de auditoría": "a) Peritos Contadores. b) Profesionales de la Contaduría Pública y Auditoría. c) Personas Jurídicas constituidas bajo la figura de firmas contables y de auditoría"; "Se exceptúan … a las personas individuales que presten sus servicios únicamente en relación de dependencia"; vigencia 3 months (≈24-Feb-2022) | SAT-DSI-1218-2021: accountants/auditors (3 categories, any clientele); only natural persons working EXCLUSIVELY as employees are excepted | `gt/sources/11_SAT-DSI-1218-2021_fel_contadores.pdf` | Artículos 1-3 (EVID-063, EVID-064) |
| LB-015 | Resolución de Superintendencia SAT-DSI-1240-2021 (17-Nov-2021; DCA 24-Nov-2021 same page as 1218; 12_ = digest-verified real text, R9): "Incorporar … a las personas individuales y jurídicas que se encuentren registradas en el Régimen General del Impuesto al Valor Agregado conforme el Decreto número 27-92 …, quienes deberán iniciar con la emisión de sus Documentos Tributarios Electrónicos (DTE) a más tardar el 01 de julio de 2022"; "las autorizaciones vigentes de otros medios o formas de emisión de documentos tributarios y las autorizaciones para emitir facturas u otros documentos con NIT y nombre del receptor en blanco, quedarán sin efecto, constituyendo el Régimen FEL el único medio …"; vigencia 3 months (≈24-Feb-2022) | SAT-DSI-1240-2021 — THE mass mandate: every taxpayer registered in the IVA General Régimen (registration fact, no codes/thresholds) must start DTE emission by 01-Jul-2022; on that date ALL legacy and blank-NIT emission authorizations die; no per-cohort DTE-type restriction (EVID-075) | `gt/sources/12_SAT-DSI-1240-2021_fel_regimen_general.pdf` | Artículo 1 both paragraphs + Artículo 2; identity dual-print (EVID-065, EVID-066, EVID-067, EVID-075) |
| LB-016 | Resolución de Superintendencia SAT-DSI-1350-2022 (3-Oct-2022; DCA 17-Oct-2022, issue number garbled "NUMERO as" [sic] — GOQ-35; heavy OCR cross-verified via 400-2023's clean quotation): cohort "registradas en el Régimen de Pequeño Contribuyente conforme el Decreto número 27-92" (as printed "27-42" [sic]); DTE start "a más tardar el 31 de marzo de 2023"; vigencia 3 months (≈17-Jan-2023); no thresholds stated (EVID-069) | SAT-DSI-1350-2022: pequeño-contribuyente cohort defined purely by régime registration; original deadline 31-Mar-2023 (moved by 400-2023); threshold values live in D-27-92, never here | `gt/sources/13_SAT-DSI-1350-2022_fel_pequenos.pdf` | Articulo 1 [sic] + Articulo 2 [sic] (EVID-068, EVID-069) |
| LB-017 | Resolución de Superintendencia SAT-DSI-400-2023 (28-Mar-2023; DCA 31-Mar-2023): "Ampliar el plazo de incorporación … a las personas … registradas en el Régimen de Pequeño Contribuyente …, quienes deberán iniciar con la emisión de sus Documentos Tributarios Electrónicos (DTE) a más tardar el 1 de julio de 2023"; "A partir del 1 de julio de 2023, las autorizaciones … y las autorizaciones para emitir facturas u otros documentos con Número de Identificación Tributaria -NIT- y nombre del receptor en blanco, quedarán sin efecto …"; "empezará a regir a partir de su publicación" (31-Mar-2023) | SAT-DSI-400-2023: pure deadline EXTENSION of 1350-2022 (cohort unchanged) to 01-Jul-2023; effective on publication the very day the old deadline expired — no lapse gap; blank-NIT lapse restated with full NIT expansion | `gt/sources/14_SAT-DSI-400-2023_fel_pequenos_ampliacion.pdf` | Artículo 1 both paragraphs + Artículo 2 (EVID-070, EVID-071) |
| LB-018 | Reglamento de la Ley del IVA, AG 5-2013, reformado por AG 222-2019 (the reglamento's only reform — EV02a): Art. 28 bis: "A partir del 1 de julio de 2021, el Régimen FEL será el único medio que la Administración Tributaria autorizará para la emisión de documentos tributarios, a las personas que se inscriban por primera vez para realizar una actividad económica"; Art. 29 ¶4: "Los documentos que se autoricen en medios distintos del Régimen FEL tendrán seis meses como plazo máximo de vigencia contados a partir de la fecha de la resolución de autorización"; Art. 36 bis: onboarding prerequisites (RTU inscrito/actualizado/ratificado + medios electrónicos + AD-defined conditions) | IVA Reglamento (AG 222-2019 layer): from 1-Jul-2021 FEL is the only emission means SAT will authorize for FIRST-TIME registrants; non-FEL document authorizations are capped at 6 months' validity from the authorization resolution; reglamento-level onboarding prerequisites | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | Arts. 28 bis, 29 ¶4, 36 bis (EVID-180, EVID-181) |
| LB-019 | Manual "FACTURA ELECTRÓNICA -FEL- Habilitación como emisor" (21_, undated — currency watch GOQ-37): "Se integra de tres complementos “Habilitarse como emisor”, “Generación de firma electrónica interna para emisión” y “Términos y condiciones”" / "El sistema valida automáticamente que cumplas con los requisitos requeridos" / "Parámetros contraseña: debe tener más de 7 caracteres, teniendo al menos 1 mayúscula, 1 minúscula, 1 número y un carácter especial ($%&/()" / acreditación: "Se te desplegará la lista de certificadores autorizados, para que acredites al que seleccionaste … puedes cambiarle el estado a “No acreditado”" / firma: "Debes seleccionar a “Otros certificadores de DTE (terceros)” … Se descargará el certificado de firma electrónica con el cual se firmarán los DTE que emitas por medio de Certificadores. Dicha firma la debes instalar en tu sistema de emisión" | SAT user manual for emisor enablement (Agencia Virtual): self-service habilitación with automatic prerequisite checks; password policy (>7 chars, ≥1 upper/lower/digit/special from $%&/()); taxpayer accredits/de-accredits certificadores from the authorized list (SAT itself certifies only its free app); for third-party certificadores a downloadable emisor signing certificate is generated and installed in the emission system | `gt/sources/21_FEL_firma_electronica_manual.pdf` | pp. 1-11, Pasos 1-4 (EVID-093, EVID-094, EVID-095) |
| LB-020 | Instrument type of the 11 mandate instruments: every file headed "RESOLUCIÓN DE SUPERINTENDENCIA NÚMERO SAT-DSI-…" issued by "EL SUPERINTENDENTE DE ADMINISTRACIÓN TRIBUTARIA" (footers "Despacho del Superintendente") — never "Directorio Superior" | Citation-hygiene authority: the mandate instruments are Superintendent resolutions of the SAT-DSI series; the label "Resolución de Directorio Superior" is inaccurate and must not propagate | `gt/sources/04_SAT-DSI-243-2019_fel_proveedores_estado.pdf` … `14_SAT-DSI-400-2023_fel_pequenos_ampliacion.pdf` | all 11 title blocks (EVID-072) |
| LB-021 | Sanctions absence in the 11 instruments: the only CT references are faculty hooks (e.g. 10_: "conforme lo establecen los artículos 19 y 98 “A” numeral 2 del Código Tributario"); the operative teeth are lapse clauses, e.g. 12_: "quedarán sin efecto, constituyendo el Régimen FEL el único medio …" | None of the 11 resolutions contains sanctions articles; enforcement = administrative death of emission authorizations on the deadline; sanctions for unauthorized issuance would attach via the Código Tributario generally — outside these instruments (GOQ-31) | `gt/sources/12_SAT-DSI-1240-2021_fel_regimen_general.pdf` | POR TANTO + RESUELVE of all 11 (EVID-074) |
| LB-022 | Decisiones compartidas D15/D16 (+ D-GT10 instantiation): dated rows keyed by instrument; changes add rows; no past-dated transmission; hard no-override emission block; snapshot-on-write of resolved legal parameters (here: mandate deadlines and lapse dates resolved as-of the taxpayer's anchor dates) | Shared canon for the mandate registry: cohort/deadline rows carry valid_from/provenance and are append-only; a taxpayer's mandate status and legacy-authorization lapse are resolved and snapshotted on write | `shared/docs/regulatory-change-management.md` | D15-D16, D-GT10 (canon compartido del master index) |

## 3. Functional Requirements

### 3.1 Statutory ladder & citation discipline

- **GT-EINV-FR-140:** The system shall represent the FEL statutory ladder
  as a provenance chain in its legal-reference registry: CT D-6-91 arts.
  98.5/98"A".2 (electronic-documents faculty) → Ley IVA D-27-92 arts. 29-30
  (invoice characteristics) → IVA art. 29-"A", added by Decreto 4-2019
  art. 6 (Ley para la Reactivación Económica del Café; SAT qualifies and
  compulsorily enables cohorts, 3-month vacatio legis) → AD 13-2018
  (operative text = consolidated 01_, R10) as reformed by AD 26-2019
  (in force 28-Nov-2019) and AD 15-2020 (in force 26-Nov-2020) → the
  eleven Resoluciones de Superintendencia SAT-DSI (mandate chronology,
  FR-150). Every mandate-related requirement shall trace to a rung of this
  chain. (LB-001; LB-002; LB-003; LB-004; LB-005; LB-006; EVID-032,
  EVID-049, EVID-050, EVID-073)
- **GT-EINV-FR-141:** Every user-facing and persisted citation of a
  mandate instrument shall use the form "Resolución de Superintendencia
  SAT-DSI-nnn-nnnn"; the strings "Directorio Superior" or "Resolución de
  Directorio" shall never be attached to these instruments (they are
  Superintendent acts of the DSI series). The AD-layer instruments are
  cited as "Acuerdo de Directorio". (LB-020; EVID-072)
- **GT-EINV-FR-142:** The system shall never cite a SAT-DSI incorporation
  resolution as the source of a fiscal threshold or régime boundary: the
  Régimen General / Régimen de Pequeño Contribuyente boundary and all
  monetary limits live in D-27-92 and its reforms (the resolutions define
  cohorts purely as registration facts). The Q2,500.00 figure of
  SAT-DSI-887-2020 art. 2 is that instrument's own cohort exception
  (FR-156), not a tax threshold. → OQ-007 (GOQ-33/34/35 minors recorded;
  threshold sourcing guard). (LB-015; LB-016; LB-017; EVID-069)
- **GT-EINV-FR-143:** The system shall treat mandate enforcement as
  authorization lapse, not penalty: none of the 11 SAT-DSI instruments
  contains sanctions articles, and no requirement or message may cite them
  for sanctions. On a cohort's lapse date the legacy emission
  authorizations die administratively (including blank-NIT invoice
  tolerances); any FEL-infraction sanction semantics belong to the Código
  Tributario layer, whose location is open → OQ-005 (GOQ-31).
  (LB-021; EVID-074)

### 3.2 Regime-level mandate mechanics (AD 13-2018 as reformed by 26-2019)

- **GT-EINV-FR-144:** The system shall model compulsory incorporation per
  AD 13-2018 art. 11 (26-2019 wording): SAT defines taxpayer segments and
  deadlines by notified resolutions; each incorporation resolution takes
  effect 3 months after notification; the resolution itself states the
  maximum deadline for the taxpayer's legacy emission authorizations
  (including blank-NIT authorizations), which lapse upon expiry, FEL then
  being the only authorized means. Per-taxpayer mandate state shall
  record: notification/incorporation anchor, 3-month vigencia clock
  (resolution texts operationalize publication as trigger — EVID-073),
  deadline and lapse date. (LB-003; LB-004; LB-005; EVID-039, EVID-073)
- **GT-EINV-FR-145:** The system shall support the voluntary-adoption
  path per AD 13-2018 art. 12 (26-2019 wording): a taxpayer who qualifies
  may enable as FEL emisor voluntarily via SAT's virtual platform, with a
  maximum 6-month window for its legacy emission authorizations
  (including blank-NIT), after which FEL is the only means. The voluntary
  adoption date shall be captured and shall start the 6-month lapse clock.
  (LB-004; LB-005; EVID-040)
- **GT-EINV-FR-146:** The emisor-onboarding surface shall enforce the
  AD 13-2018 art. 13 prerequisites (26-2019 wording): RTU status
  inscrito/actualizado/ratificado, and access to the SAT electronic means
  (Agencia Virtual); it shall record that SAT issues the emission
  signature certificate and that the emisor is directly responsible for
  its custody. The "inscrito" element of the 26-2019 text carries an OCR
  reservation → OQ-003 (GOQ-29). (LB-004; EVID-041)
- **GT-EINV-FR-147:** The system shall implement the AD 13-2018 art. 13"A
  operating conditions: an emisor accredits one or more certificadores of
  its choosing (see FR-166), adapts its emission systems to the FEL
  operational model, and uses the SAT electronic tools; and it shall deny
  authorization of NEW documents in FEL while the taxpayer's IVA
  affiliation is suspended (the art. 13"A hook cites CT art. 120; per
  ruling R21 the suspension citation channel is CT 98"A".2 — the struck
  art. 120 eleventh paragraph is never cited). (LB-004; LB-005;
  EVID-041)

### 3.3 Reglamento-layer mandate rules (AG 5-2013, reformado por AG 222-2019)

- **GT-EINV-FR-148:** The entitlement/onboarding evaluation shall classify
  every taxpayer that registers for an economic activity for the first
  time on or after 2021-07-01 as FEL-only per Reglamento IVA art. 28 bis:
  FEL is the only emission means SAT will authorize for first-time
  registrants from that date; no non-FEL emission-authorization path
  shall be offered or modeled for such taxpayers. (LB-018; EVID-181)
- **GT-EINV-FR-149:** Every non-FEL document authorization recorded for a
  legacy taxpayer shall carry a computed expiry of at most 6 months from
  its authorization resolution date per Reglamento IVA art. 29 ¶4,
  reconciled against (and superseded by) any earlier cohort lapse date
  from FR-150's registry; the earlier of the two governs. (LB-018;
  EVID-181)

### 3.4 Mandate chronology — dated rows keyed by incorporation resolution (D16)

- **GT-EINV-FR-150:** The mandate chronology shall be stored as append-only
  dated rows (D16/D-GT10) keyed by incorporation resolution, one row per
  instrument, each carrying: instrument id (FR-141 naming), given date,
  DCA publication date (from gazette headers, EVID-076), vigencia rule +
  resolved vigencia date (computed dates marked ≈), cohort predicate,
  DTE-start deadline / legacy-lapse date where printed, exceptions, and
  EVID provenance. A later instrument that changes a deadline (e.g.
  400-2023) adds a new row superseding the prior row's deadline without
  mutating it. (LB-022; LB-007..LB-017; EVID-051..071, EVID-076)
- **GT-EINV-FR-151:** The system shall provide a who-must-emit-FEL-by-when
  evaluation: given a taxpayer's RTU régime registration(s), registration
  date(s), activity and client predicates, it shall evaluate the cohort
  predicates of all rows in the FR-150 registry, select the earliest
  applicable mandate (and, for régimens with deadline rows, the operative
  deadline after supersession), and return the taxpayer's FEL obligation
  date and legacy-authorization lapse date. Taxpayers matching no cohort
  predicate return not-mandated (voluntary path FR-145 available).
  (LB-007..LB-017; EVID-052..071)
- **GT-EINV-FR-152:** The registry shall carry the SAT-DSI-243-2019 row:
  cohort = suppliers of bienes/obras/servicios/suministros to State
  entities under contrato abierto, cotización, licitación, subasta
  electrónica inversa; no deadline printed; vigencia = day after
  publication, which is undatable from the corpus → OQ-001 (GOQ-27
  analog) and OQ-007 (GOQ-33); whether the obligation was later subsumed
  by 1240-2021's blanket is not determinable → OQ-008 (GOQ-34).
  (LB-007; EVID-051, EVID-052)
- **GT-EINV-FR-153:** The registry shall carry the SAT-DSI-838-2019 row:
  cohort = individual professionals (university degree + colegiación
  activa per D-72-2001; statutory definition per AG 122-2016 art. 2 q))
  rendering services to the D57-92 art. 1 state sector; given 21-Aug-2019,
  DCA 11-Sep-2019, effective 12-Sep-2019 (computed); no lapse deadline
  printed → OQ-008 (GOQ-34). (LB-008; EVID-053, EVID-054)
- **GT-EINV-FR-154:** The registry shall carry the SAT-DSI-639-2020 row:
  cohort = Servicios Técnicos providers to the state sector; given
  16-Jul-2020, DCA 30-Jul-2020, vigencia 3 months post-publication
  (≈30-Oct-2020); legacy emission authorizations void 2020-12-31. Any
  COVID-era prórroga of that lapse is outside the corpus → OQ-009
  (GOQ-35). (LB-009; EVID-055, EVID-056)
- **GT-EINV-FR-155:** The registry shall carry the SAT-DSI-640-2020 row:
  cohort = ALL emisors under AD 024-2007 (FACE); FACE authorizations void
  2020-12-31, FEL the only means thereafter; no new FACE emisors are
  admitted after the established deadline (AD 13-2018 art. 25
  programming). Prior-FACE taxpayers are FEL-mandatory regardless of
  régime. Prórroga caveat as FR-154 → OQ-009 (GOQ-35). (LB-004; LB-010;
  EVID-047, EVID-057)
- **GT-EINV-FR-156:** The registry shall carry the SAT-DSI-887-2020 row:
  cohort = State suppliers under Compra Directa and Compra de Baja
  Cuantía (D57-92 art. 43 a-b); FIXED vigencia 2021-04-01; exception —
  baja-cuantía operations "por un valor menor a" Q2,500.00 (per-operation,
  exclusive boundary) are exempt from this instrument's mandate. No other
  monetary exception exists in the 11 instruments. (LB-011; EVID-058)
- **GT-EINV-FR-157:** The registry shall carry the SAT-DSI-398-2021 row:
  cohort = State suppliers under Adquisición con proveedor único,
  Arrendamientos, Arrendamiento y adquisición de bienes inmuebles, Dragado
  (D57-92 art. 43 c-f); given 29-Apr-2021, DCA 10-May-2021, vigencia
  3 months (≈10-Aug-2021). The row shall record the relationship verdict:
  398-2021 COMPLEMENTS (does not extend or amend) 243-2019; together with
  243-2019 (contract-level modalities) and 887-2020 (a-b) the D57-92
  modality sweep is complete. Article-sequence defect (no printed
  Artículo 3) → OQ-009 (GOQ-35). (LB-012; EVID-059, EVID-060)
- **GT-EINV-FR-158:** The registry shall carry the SAT-DSI-1074-2021 row:
  cohort = market-wide salud y asistencia social providers in the six
  printed categories a)-f) (including ALL university professionals,
  technicians and auxiliaries of the sector, and
  importers/manufacturers/sellers of medical equipment and
  pharmaceutical-affine products); exception = entidades del Sector
  Público; given 11-Oct-2021, DCA 19-Oct-2021, vigencia 3 months
  (≈19-Jan-2022). The categories are verbal (no activity codes printed);
  mapping to SAT activity codes is a product-side concern, never cited to
  the instrument. (LB-013; EVID-061, EVID-062)
- **GT-EINV-FR-159:** The registry shall carry the SAT-DSI-1218-2021 row:
  cohort = market-wide providers of contable/financiera/tributaria/auditoría
  services — Peritos Contadores, CPA professionals, and contable/audit
  firms; exception = natural persons rendering services "únicamente en
  relación de dependencia" (mixed practice is not exempt); given
  15-Nov-2021, DCA 24-Nov-2021, vigencia 3 months (≈24-Feb-2022).
  (LB-014; EVID-063, EVID-064)
- **GT-EINV-FR-160:** The registry shall carry the SAT-DSI-1240-2021 row —
  THE mass mandate: cohort = ALL personas individuales y jurídicas
  registered in the Régimen General del IVA (pure registration fact per
  D-27-92; no activity codes, no turnover thresholds); compliance act =
  start DTE emission no later than 2022-07-01; on that date all legacy
  AND blank-NIT emission authorizations die and FEL is the only means.
  Source discipline: cite 12_ (digest-verified real text, R9); the 11_
  DCA twin is a cross-check. No per-cohort DTE-type restriction exists at
  this instrument layer (regime-level obligation). (LB-015; EVID-065,
  EVID-066, EVID-067, EVID-075)
- **GT-EINV-FR-161:** The registry shall carry the SAT-DSI-1350-2022 row:
  cohort = ALL taxpayers registered in the Régimen de Pequeño
  Contribuyente (D-27-92; no thresholds stated — EVID-069); original DTE
  start deadline 2023-03-31, superseded by FR-162's row; given 3-Oct-2022,
  DCA 17-Oct-2022 (issue number garbled → OQ-009/GOQ-35), vigencia 3
  months (≈17-Jan-2023). (LB-016; EVID-068, EVID-069)
- **GT-EINV-FR-162:** The registry shall carry the SAT-DSI-400-2023 row as
  the operative deadline instrument for the pequeño cohort: it EXTENDS
  ("Ampliar el plazo") 1350-2022's deadline only — cohort unchanged — to
  DTE start ≤ 2023-07-01, with legacy + blank-NIT authorizations void from
  that date; it takes effect on publication (DCA 31-Mar-2023), the same
  day the original 31-Mar-2023 deadline expired, so no lapse gap exists
  between the two instruments. (LB-017; EVID-070, EVID-071)
- **GT-EINV-FR-163:** Cohort predicates shall be evaluated as registration
  facts and instrument-printed verbal categories only: none of the 11
  resolutions carries per-cohort DTE-type restrictions (the obligation is
  regime-level — "todos los documentos tributarios disponibles dentro del
  mismo"), and none carries thresholds. DTE-type requirements cite the
  taxonomy layer (`01_document-types.md`, AD 13-2018 art. 3 + Reglas
  v2.0), never these resolutions. (LB-015; LB-021; EVID-069, EVID-075)

### 3.5 Emisor onboarding operational flow (21_ manual; 2018-vintage, supersession-checked)

- **GT-EINV-FR-164:** The onboarding wizard shall mirror the SAT
  Agencia Virtual *habilitación* flow as its informational backbone:
  self-service enablement ("Habilitarse como emisor", "Generación de firma
  electrónica interna para emisión", "Términos y condiciones"
  sub-modules) with automatic prerequisite validation, so the Odoo-side
  configuration checklist tracks the SAT-side steps and their completion
  state. The 21_ manual is undated — portal-flow currency is watched
  jointly with file 07/08 → OQ-010 (GOQ-37 kin, owned by
  `07_display-representation.md`). (LB-019; EVID-093)
- **GT-EINV-FR-165:** Wherever the product stores or creates the
  *contraseña asociada a la firma electrónica* (the password associated
  with the emisor electronic signature), it shall enforce the SAT policy
  printed in 21_: more than 7 characters with at least 1 uppercase, 1
  lowercase, 1 digit and 1 special character from the set $%&/(). The
  policy is validated at capture; it does not apply to unrelated Odoo
  user passwords. (LB-019; EVID-093)
- **GT-EINV-FR-166:** The onboarding surface shall support *acreditación*
  of certificadores: selection from the SAT-published list of authorized
  certificadores (roster data owned by `05_certificador-interface.md` /
  cluster E5), state changes to "No acreditado" (de-accreditation), and
  the fact that SAT itself acts as certificador only for its free Agencia
  Virtual app. Switching certificador requires updating the acreditación
  and, for third parties, regenerating the emisor signature (FR-167).
  (LB-019; EVID-094)
- **GT-EINV-FR-167:** The system shall support the third-party-certificador
  signature flavor: the taxpayer selects "Otros certificadores de DTE
  (terceros)", generates and downloads the emisor *certificado de firma
  electrónica* from Agencia Virtual, and installs it in the emission
  system; the product shall import and use that downloadable certificate
  (with its FR-165 password) to sign DTEs submitted through the
  third-party certificador, and shall support re-generation/reset flows
  (separate reset paths exist for the SAT-internal flavor). Key-format
  specifics are provider-boundary questions → `05_certificador-interface.md`
  (GOQ-39 kin); manual currency → OQ-010 (GOQ-37 kin). (LB-019; EVID-095)

### 3.6 Legacy-authorization lapse semantics

- **GT-EINV-FR-168:** Given a legacy (non-FEL) emission authorization on a
  taxpayer record, the system shall resolve and display its lapse date as
  the earliest of: the applicable cohort lapse date from the FR-150
  registry (e.g. 2020-12-31, 2022-07-01, 2023-07-01), the voluntary
  6-month window expiry (FR-145), and the reglamento 6-month cap
  (FR-149); the resolved value is snapshotted on write (D15/D16) with its
  provenance row. Blank-NIT invoice authorizations lapse on the same date
  as the instrument's lapse clause states. (LB-009; LB-015; LB-017;
  LB-018; EVID-056, EVID-067, EVID-071, EVID-181)
- **GT-EINV-FR-169:** After a taxpayer's lapse date, the system shall
  block all non-FEL emission paths for that taxpayer (hard no-override
  emission block per D16): post-deadline legacy-authority invoicing is
  not offerable, and the block is lifted only by a superseding instrument
  row (as 400-2023 lifted nothing but moved the pequeño deadline before
  it took effect). (LB-015; LB-017; EVID-067, EVID-071, EVID-075)
- **GT-EINV-FR-170:** The Odoo company record shall surface the
  taxpayer's mandate status derived from FR-151: applicable cohort(s) and
  instrument citations (FR-141 form), obligation/deadline date,
  legacy-authorization lapse date(s), voluntary-adoption state, and
  onboarding checklist state (FR-144..FR-147, FR-164..FR-167), each with
  its dated-row provenance. (LB-022; LB-007..LB-017; EVID-051..071)

## 4. Data Model

**Mandate-cohort registry** (dated rows, D16/D-GT10 seed — append-only;
computed dates marked ≈; publication data from gazette headers per
EVID-076). Machine-readable sidecar: `../catalogs/` mandate rows
(future); this table is the authoritative seed.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.fel.mandate.cohort | resolution | char | SAT-DSI-243-2019 · 838-2019 · 639-2020 · 640-2020 · 887-2020 · 398-2021 · 1074-2021 · 1218-2021 · 1240-2021 · 1350-2022 · 400-2023 | FR-141, FR-150; EVID-072 |
| l10n_gt.fel.mandate.cohort | given / dca_publication | date / date null | 243-2019 DCA = null (GOQ-33); 1350-2022 issue no. garbled (GOQ-35) | FR-150; EVID-051..076 |
| l10n_gt.fel.mandate.cohort | vigencia_rule / valid_from | select + date | next-day · 3-months-post-publication · fixed-date (887: 2021-04-01) · on-publication (400-2023) | FR-150..FR-162; EVID-073 |
| l10n_gt.fel.mandate.cohort | cohort_predicate | text (structured) | state-supplier modality set · professional-to-state · technical-to-state · FACE-emisor · health 6-cat · accountant 3-cat · régimen=General · régimen=Pequeño | FR-152..FR-162; EVID-052..071 |
| l10n_gt.fel.mandate.cohort | dte_start_deadline | date null | 1240-2021: 2022-07-01 · 1350-2022: 2023-03-31 (superseded) · 400-2023: 2023-07-01 · others: null | FR-160..FR-162; EVID-066/068/070 |
| l10n_gt.fel.mandate.cohort | legacy_lapse_date | date null | 639/640-2020: 2020-12-31 · 1240-2021: 2022-07-01 · 400-2023: 2023-07-01 | FR-154/155/160/162; EVID-056/057/067/071 |
| l10n_gt.fel.mandate.cohort | exceptions | text | 887: baja-cuantía op < Q2,500.00 · 1074: Sector Público · 1218: dependencia-only individuals · others: none | FR-156/158/159; EVID-058/062/064 |
| l10n_gt.fel.mandate.cohort | supersedes | many2one null | 400-2023 → 1350-2022 (deadline only) | FR-162; EVID-070 |
| res.company | l10n_gt_fel_mandate_state | select | not_mandated · voluntary · mandated · lapsed | FR-145, FR-151, FR-170 |
| res.company | l10n_gt_fel_obligation_date / lapse_date | date | snapshot-on-write + provenance row id | FR-151, FR-168; D15/D16 |
| res.company | l10n_gt_fel_first_registration_date | date | input to FR-148 first-time-registrant test (cutoff 2021-07-01) | FR-148; EVID-181 |
| res.company | l10n_gt_fel_voluntary_adoption_date | date | starts FR-145 6-month clock | FR-145; EVID-040 |
| l10n_gt.emission.authorization | type / resolution_date / valid_to | select + date | type = non-FEL legacy; valid_to = min(cohort lapse, resolution_date + 6 months, voluntary window) | FR-149, FR-168; EVID-181 |
| res.company (firma credentials) | l10n_gt_fel_firma_file / password metadata | binary + policy flag | downloadable third-party certificador certificate; password policy FR-165 (>7 chars, 1 upper/lower/digit/special $%&/()) | FR-165, FR-167; EVID-093/095 |

**Chronology quick table** (human-facing mirror of the registry; all rows
also in FR-152..FR-162):

| Resolution | Given | DCA | Vigencia | Deadline / lapse | Exceptions |
|---|---|---|---|---|---|
| SAT-DSI-243-2019 | 11-Mar-2019 | not printed (GOQ-33) | day after publication (undatable) | none printed | none |
| SAT-DSI-838-2019 | 21-Aug-2019 | 11-Sep-2019 | 12-Sep-2019 ≈ | none printed | none |
| SAT-DSI-639-2020 | 16-Jul-2020 | 30-Jul-2020 | ≈30-Oct-2020 | legacy void 2020-12-31 | none |
| SAT-DSI-640-2020 | 16-Jul-2020 | 30-Jul-2020 | ≈30-Oct-2020 | FACE void 2020-12-31 | none |
| SAT-DSI-887-2020 | 8-Oct-2020 | 19-Oct-2020 | fixed 2021-04-01 | none printed | baja cuantía < Q2,500.00 |
| SAT-DSI-398-2021 | 29-Apr-2021 | 10-May-2021 | ≈10-Aug-2021 | none printed | none |
| SAT-DSI-1074-2021 | 11-Oct-2021 | 19-Oct-2021 | ≈19-Jan-2022 | none printed | Sector Público |
| SAT-DSI-1218-2021 | 15-Nov-2021 | 24-Nov-2021 | ≈24-Feb-2022 | none printed | dependencia-only |
| SAT-DSI-1240-2021 | 17-Nov-2021 | 24-Nov-2021 | ≈24-Feb-2022 | DTE start ≤ 2022-07-01; legacy + blank-NIT void | none |
| SAT-DSI-1350-2022 | 3-Oct-2022 | 17-Oct-2022 | ≈17-Jan-2023 | DTE start ≤ 2023-03-31 (superseded) | none |
| SAT-DSI-400-2023 | 28-Mar-2023 | 31-Mar-2023 | on publication 2023-03-31 | DTE start ≤ 2023-07-01; legacy + blank-NIT void from 2023-07-01 | none |

## 5. Odoo Mapping

Layer semantics per the architecture split: `odoo` = onboarding
configuration/wizard and status surfaces in the LGPL client; `saas` =
the who-must-emit-by-when entitlement/config evaluation and emission
blocking; `shared` = the dated-row registry and lapse-date contract both
sides must honor. Model names are stable across Odoo 17/18/19/20; no
version-specific behavior is required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-140 | shared | — (legal-reference registry) | provenance chain rows | Registry content shared odoo↔saas; both surfaces render the ladder citations identically |
| FR-141 | shared | — | citation strings | Naming rule applies to every generated citation on both surfaces; single shared formatter |
| FR-142 | shared | — | citation guard metadata | Guard rides the shared LB/registry layer; threshold values themselves live in the taxation files (D-27-92) |
| FR-143 | shared | — | lapse-semantics metadata | Guard: no sanctions semantics attach to SAT-DSI rows; enforcement = lapse only |
| FR-144 | shared | l10n_gt.fel.mandate.state | notification anchor, vigencia clock, deadline, lapse | State machine contract; odoo displays, saas evaluates deadlines |
| FR-145 | shared | res.company | l10n_gt_fel_voluntary_adoption_date | Adoption date captured in odoo wizard; 6-month clock resolved per contract |
| FR-146 | odoo | res.company | RTU status checklist fields | Onboarding wizard prerequisites; SAT-side validation acknowledged (EVID-093 automatic checks) |
| FR-147 | saas | — | new-document authorization gate | Deny-new-docs interlock evaluated at emission authorization time (IVA-affiliation suspension feed = mini-RTU, `05_certificador-interface.md`) |
| FR-148 | saas | res.company | l10n_gt_fel_first_registration_date | First-time-registrant cutoff 2021-07-01 evaluated in the entitlement core |
| FR-149 | saas | l10n_gt.emission.authorization | resolution_date, valid_to | 6-month cap computed authoritative saas-side; odoo displays |
| FR-150 | shared | l10n_gt.fel.mandate.cohort | all registry fields | Dated rows are the shared contract artifact (append-only, provenance per row) |
| FR-151 | saas | — | cohort evaluation service | Who-must-emit-by-when entitlement evaluation; result mirrored to odoo for display (FR-170) |
| FR-152 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-243-2019 | Undated vigencia kept null + GOQ-33 caveat; never date-math'd |
| FR-153 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-838-2019 | Effective 12-Sep-2019 computed from printed DCA header |
| FR-154 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-639-2020 | ≈ dates marked computed; GOQ-35 prorroga caveat |
| FR-155 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-640-2020 | FACE cohort predicate = historical regime membership; historical import must classify pre-2021 FACE emisors |
| FR-156 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-887-2020 | Q2,500 exception = per-operation exclusive bound; not a tax threshold (FR-142) |
| FR-157 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-398-2021 | complements-not-extends relation recorded on the row |
| FR-158 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-1074-2021 | 6 verbal categories; product-side activity-code mapping never cited to the instrument |
| FR-159 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-1218-2021 | "únicamente" qualifier drives the exception test |
| FR-160 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-1240-2021 | Anchor row of the registry; cite 12_ (R9); blank-NIT lapse recorded |
| FR-161 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-1350-2022 | Deadline superseded via `supersedes` link |
| FR-162 | shared | l10n_gt.fel.mandate.cohort | row SAT-DSI-400-2023 | Operative pequeño deadline row; no-lapse-gap continuity note |
| FR-163 | shared | l10n_gt.fel.mandate.cohort | predicate metadata | Guard: no per-cohort DTE-type data on registry rows |
| FR-164 | odoo | res.company + onboarding wizard | checklist steps | Informational mirror of Agencia Virtual flow; GOQ-37 currency watch shared with file 07/08 |
| FR-165 | odoo | res.company (firma credentials) | password policy validation | Only for the firma-associated password; policy constants from 21_ (GOQ-37 kin currency) |
| FR-166 | odoo | res.partner (certificador) / res.company | acreditacion state | Roster feed owned by 05_certificador-interface.md (31_ snapshot); forward ref |
| FR-167 | odoo | res.company (firma credentials) | certificate import/export | Credential import odoo-side; signing usage crosses the provider boundary — 05_ owns interface (GOQ-39 kin) |
| FR-168 | shared | l10n_gt.emission.authorization | valid_to | Lapse-resolution contract: min(cohort lapse, +6m cap, voluntary window); snapshot-on-write |
| FR-169 | saas | — | emission-path gate | Hard no-override block evaluated at emission authorization; only a superseding instrument row lifts it |
| FR-170 | odoo | res.company | mandate status surface | Display-only aggregation of FR-151 results + onboarding checklist state |

## 6. Acceptance Criteria

- **AC-001:** Given a taxpayer registered in the Régimen General del IVA
  with first registration 2021-06-15, when the mandate evaluation runs,
  then the SAT-DSI-1240-2021 row applies, the FEL obligation date
  displayed is DTE emission start ≤ 2022-07-01, and the legacy
  authorization lapse date displayed is 2022-07-01 (FR-151, FR-160,
  FR-168).
- **AC-002:** Given a taxpayer whose first registration for an economic
  activity is 2021-07-01 or later, when onboarding is configured, then no
  non-FEL emission-authorization path exists (Reglamento art. 28 bis);
  given a first registration 2021-06-30, then legacy paths remain
  available subject to cohort rules (FR-148).
- **AC-003:** Given a non-FEL emission authorization resolved on
  2022-09-01 for a taxpayer not matching any lapse-deadline cohort, when
  its valid_to is computed, then it displays 2023-03-01 (6-month cap);
  given the same authorization on a Régimen General taxpayer, then
  valid_to = 2022-07-01 (cohort lapse governs as the earlier date)
  (FR-149, FR-168).
- **AC-004:** Given a taxpayer registered in the Régimen de Pequeño
  Contribuyente, when the registry is queried, then the operative
  deadline row is SAT-DSI-400-2023 (DTE start ≤ 2023-07-01) with the
  1350-2022 row retained unchanged as superseded, and no lapse gap exists
  between 2023-03-31 and 2023-07-01 (FR-161, FR-162).
- **AC-005:** Given a private-sector pharmacy and a hospital that is an
  entidad del Sector Público, when the 1074-2021 predicate is evaluated,
  then the pharmacy is mandated (from ≈2022-01-19) and the Sector Público
  entity is excepted (FR-158).
- **AC-006:** Given a State supplier whose only operations are
  baja-cuantía purchases of Q2,499.99, then the 887-2020 mandate does not
  apply; given one operation of exactly Q2,500.00, then it applies
  ("menor a" = exclusive bound) (FR-156).
- **AC-007:** Given the SAT-DSI-243-2019 registry row, when rendered, then
  its vigencia date is null with the undatable-publication caveat
  displayed, and no computed effective date is asserted (FR-152; GOQ-33).
- **AC-008:** Given any citation string generated for any of the 11
  instruments, when inspected, then it reads "Resolución de
  Superintendencia SAT-DSI-nnn-nnnn" and the corpus contains no
  "Directorio Superior" attribution to them (FR-141; EVID-072).
- **AC-009:** Given the requirements corpus, when searched, then no FR or
  LB row cites a SAT-DSI instrument for sanctions or for a fiscal
  threshold; the 1240-2021 deadline semantics render as authorization
  expiry, not penalty (FR-142, FR-143).
- **AC-010:** Given the statutory-ladder registry entry for IVA art.
  29-"A", when rendered, then its provenance displays "added by Decreto
  4-2019 art. 6 (Ley para la Reactivación Económica del Café)" verbatim
  from the AD 26-2019 considerando (FR-140; EVID-049).
- **AC-011:** Given an onboarding password capture for the firma
  credential with "abcdefg1A" (no special), then it is rejected; given
  "abcdefg$1A", then it passes (FR-165).
- **AC-012:** Given a certificador switch from SAT free app to a
  third-party certificador, then the acreditación state updates, the
  downloadable third-party certificate flow (generate, download, install)
  is presented, and re-generation after password reset is supported
  (FR-166, FR-167).
- **AC-013:** Given a former FACE emisor, then its FACE authorizations
  display as void since 2020-12-31 and FEL is the only emission path
  (FR-155, FR-169).
- **AC-014:** Given a taxpayer under the 1218-2021 cohort who renders
  accounting services both as an employee and independently, when the
  exception is evaluated, then the taxpayer is mandated ("únicamente en
  relación de dependencia" not met) (FR-159).

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.1);
question text verbatim from the register where printed. This file OWNS
GOQ-27, GOQ-28, GOQ-29, GOQ-30, GOQ-31, GOQ-32, GOQ-33, GOQ-34 and
GOQ-35. Kin ids referenced inline only: GOQ-37 (undated-manuals currency,
owned by `07_display-representation.md`, Task 8), GOQ-39 (provider
key-format specifics, owned by `05_certificador-interface.md`).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-27 (owned): "01_ prints no DCA publication date; AD 13-2018 vigencia = 'quince días después de su publicación' — the 23-May-2018 effective date is NOT evidenced; verify against DCA before date math." Affects any AD 13-2018-level date computation (none required by current FRs; FR-144 uses resolution dates instead). | no | GT synthesis wave S-GT1 → W6 partner ask (DCA gazette) | open |
| OQ-002 | GOQ-28 (owned): "Original 2018 wordings of reformed AD articles (2.b, 3, 11, 12, 13, 15) not in corpus — obtain 2018 DCA print if diffs matter." FR-144..FR-147 implement the consolidated (operative) texts. | no | GT synthesis wave S-GT1 → W6 partner ask (DCA gazette) | open |
| OQ-003 | GOQ-29 (owned): "02_ art. 5 OCR: cannot resolve whether 26-2019 dropped 'inscrito' (consolidated treated operative)." Affects only the provenance note of FR-146's RTU prerequisite; consolidated wording ships. | no | GT synthesis wave S-GT1 → W6 partner ask (clean gazette re-OCR) | open |
| OQ-004 | GOQ-30 (owned): "03_ DCA edition 'NÚMERO 6' for 25-Nov-2020 anomalous vs 2019's 'NÚMERO 54' (tomo reset?) — verify edition/tomo." Gazette-citation hygiene for AD 15-2020 (LB-006). | no | GT synthesis wave S-GT1 → W6 partner ask (DCA gazette) | open |
| OQ-005 | GOQ-31 (owned): "Where do FEL infractions/sanctions live? Neither the AD reforms nor any of the 11 resolutions contains sanctions articles (only hooks art. 6/13"A/15 k/20)." Sanctions-absence finding recorded as FR-143 (FR-note) — never cite these instruments for sanctions; CT-layer location open. | no | GT synthesis wave S-GT1 (recorded) → W6 partner ask (SAT) | open |
| OQ-006 | GOQ-32 (owned): "02_ considerando-2 sentence incomplete; 03_ POR TANTO legal basis garbled — gazette re-OCR if verbatim needed." No FR depends on the garbled fragments. | no | GT synthesis wave S-GT1 → W6 partner ask (clean gazette re-OCR) | open |
| OQ-007 | GOQ-33 (owned): "243-2019 publication date not printed anywhere (effective date = publication + 1 day) — undatable from corpus." FR-152 keeps the vigencia date null. | no | GT synthesis wave S-GT1 → W6 partner ask (DCA gazette) | open |
| OQ-008 | GOQ-34 (owned): "243-2019 and 838-2019 cohorts carry no lapse deadline — superseded by or coexisting with 1240-2021's blanket? Not determinable from texts." FR-152/FR-153 rows carry no lapse; FR-151 evaluates 1240 independently. | no | GT synthesis wave S-GT1 → W6 partner ask (SAT) | open |
| OQ-009 | GOQ-35 (owned): "Print-numbering minors: 398-2021 Art. 3 missing (sequence 1,2,4); 1350-2022 DCA issue garbled ('NUMERO as'); COVID-era prorroga instruments for the 31-dic-2020/01-jul-2022 lapse dates, if any, outside corpus." Prórroga leg guards FR-154/FR-155/FR-160 lapse assertions. | no | GT synthesis wave S-GT1 → W6 partner ask (DCA/SAT) | open |
| OQ-010 | GOQ-37 (kin; owned by `07_display-representation.md`): "20_/21_ undated Agencia Virtual manuals — confirm current portal flows unchanged." Guards FR-164..FR-167 (habilitación flow, password policy, acreditación, downloadable firma) as 2018-vintage operational content. | no | GT synthesis wave S-GT1 → 07_display-representation.md (Task 8) | open (kin) |
