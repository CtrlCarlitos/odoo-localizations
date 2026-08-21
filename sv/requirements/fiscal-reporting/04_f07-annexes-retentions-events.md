# SV — Fiscal reporting — F-07 retention/perception/event annexes 4/6-12, anulados/emitidos & F-930 view

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for the retention/perception
family of the F-07 annex upload manual (*Manual de Usuario para Carga de
Archivo de los Anexos*, F-07 V14, ENERO 2025) and its two satellite
surfaces: **Anexo 4** (*ventas por cuenta de terceros domiciliados*, sales
for the account of domiciled third parties — the *mandante* (principal)
identification, the CCF/factura row with its *monto sin IVA* (amount
without IVA) convention for consumer-final facturas, and the
*comprobante de liquidación* (liquidation document, CL) linkage columns,
feeding casilla 108); **Anexos 6-8** (the retentions/perceptions/anticipos
effected ON the declarant — *al declarante*: anticipo 2% → casilla 161,
retención 1% → 162, percepción 1% → 163, including document types 07
*Comprobante de Retención* (retention document, CRE) and 12 *Declaración
de Mercancías* (merchandise declaration)); **Anexos 9-12** (the same
family effected BY the declarant — *por el declarante*: percepción 1% →
169, retención 1% → 170, anticipo 2% → 171, retención 13% → 172 — with
the 1/2/13 percent validations that mirror the MH-side upload validator);
the **F-930 v3** *Informe Mensual de Retención/Percepción/Anticipo IVA*
(monthly IVA retention/perception/anticipo inform) implemented as a VIEW
over the same retention ledger — no second ledger; and the **§XIX
anulados/extraviados annex** (*Documentos Anulados, Extraviados o
DTE Invalidados* — voided/lost/invalidated documents) with its A-J column
model, the A/X/D detail codes, the full 12-type document list (the only
place types 04/08/09/14 appear in the F-07), the SOQ-10 defect ruling
(the manual's "36 caracteres" and inverted Sept/Oct cutover are
transcription defects — the annexes-1-12 convention is operative), the
system-derived **Documentos Emitidos** (issued documents) detail of §XVIII,
and the **invalidation-event feed interface** from the e-invoicing module
(sealed invalidation events enter this annex as detail code D — closing
the F-07 side of e-invoicing 02 OQ-008).

It does **not** cover: the declaration casilla engine and the generic
annex upload format/validations/modificatoria flow
(`01_f07-declaration.md` §3.1/§3.2 — SV-FREP-FR-001..041 own the casillas
including FR-009 (108), FR-016 (161-166), FR-022/023 (169-172/187-190) and
FR-028..041 (the semicolon-CSV engine, negative gate, windows,
clean-replace, modificatoria carryover), which this file inherits by
reference); the sales annexes and the CANONICAL document-identifier
mapping (`02_f07-annexes-sales.md` §3 — SV-FREP-FR-042/043 own the slot
model and the DTE mapping; this file references them by id and never
restates); the purchase annexes 3/5 including the post-*entero* (after
remittance) re-entry into casilla 128
(`03_f07-annexes-purchases.md` §3 — the 13% CREDIT side of CT Art. 162
lives THERE as FR-091; Anexo 12 here is the 13% PAYABLE side, a distinct
matrix per the F-cluster crossref); the fuel and dated-regime annexes
13-17 (`05_f07-annexes-special.md` §3); the F-14 family, income codes and
the F-910/F-915/F-935 informs (`06_f14-declaration.md`,
`07_codes-and-informs.md` — the F-935 donantes-locales anchor is Task 7's
SOQ-13, not this file's); the filing calendar (`08_filing-calendar.md` —
SOQ-08); the invalidation-event lifecycle itself
(`e-invoicing/03_events.md` — SV-EINV-FR-103/104/117 own deadlines, date
correspondence and retorno; this file only CONSUMES sealed events as the
source of D-code rows); and the IVA retention-rate legal regime (the
1%/2%/13% rates are anchored here via the manual/form labels only —
future IVA taxation file territory, 01 §7 OQ-004 kin).

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and upload manuals ARE the
primary authority for declaration mechanics — 34_ (Manual de Usuario
para Carga de Archivo de los Anexos, F-07 V14, ENERO 2025) is the
governing source for every annex structure here; the plantilla workbook
36_ (sheets "4", "6"-"12") is the structural conformance reference; the
form 39_ (F-07 v14, footer "Actualizado al 15/08/2025") anchors the
casilla wiring labels; the F-930 v3 form 63_ anchors the inform view.
Legal anchors printed in the manual/form (CT Art. 111 for anulados
values/windows; CT Art. 162 on casilla 128 via 01's LB) are cited as
printed; no article text is invented beyond what the form/evidence
quotes. Manual pages are printed pages (printed page N = PDF page N+2).

**SOQ-10 LB note (binding S3 ruling, recorded here as LB-007):** manual
§XIX carries two defects — column J instructs *código de generación*
"con longitud de 36 caracteres" (32 characters everywhere else and in
the DTE schema), and column A's cutover instruction ("desde septiembre
hacia atrás agregar 'Código de Generación' y ... octubre 2022 en
adelante 'Número de control'") INVERTS the Noviembre-2022 cutover used
by annexes 1-12. Ruling: both are manual transcription defects; the
annexes-1-12 convention (32 characters; Nov-2022 cutover per
SV-FREP-FR-043) is operative; the inverted cutover is NEVER encoded.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-07 v14 §VI, Anexo 4 "Ventas por Cuenta de Terceros Domiciliados" (casilla 108), tabla de columnas: "A NIT/NRC MANDANTE / B NOMBRE MANDANTE / C FECHA / D TIPO ('01 Factura, 03 CCF, 05 NC, 06 ND, 11 Factura de Exportación') / E SERIE / F RESOLUCIÓN / G NÚMERO / H MONTO ('Si declara operaciones de venta con factura de consumidor final, deberá detallarlas sin IVA') / I IVA / J-L COMPROBANTE DE LIQUIDACIÓN (serie/resolución/número) / M FECHA CL / N DUI MANDANTE / O NÚMERO DE ANEXO 4"; DTE: Serie = "sello de recepción" (ejemplo "2022F2041F1DCE1A4CE4B10B6AABFD344125QTZS"); Resolución = número de control (pre-Nov-2022 código de generación); Número = "código de generación del DTE sin guiones (32 caracteres)" / pre-Nov-2022 "número de control del DTE sin guiones (28 caracteres)" | F-07 v14 upload manual §VI, Anexo 4 column table A-O: principal's NIT/NRC and name, date, document type (invoice, tax-credit document, credit note, debit note, export invoice), series, resolution, number, amount — "if you declare sale operations with a consumer-final invoice, you must detail them without IVA" — IVA, the liquidation-document linkage triplet (series/resolution/number) with the CL date, the principal's DUI, annex number 4; DTE identifier fills as printed (reception seal series; control number / pre-Nov-2022 generation code in the resolution slot; 32-char generation code / pre-Nov-2022 28-char control number in the number slot) | `sv/sources/34_F07_v14_manual.pdf` | §VI pp.19-21 (EVID-177; plantilla sheet "4" in `sv/sources/36_F07_v14_plantilla.xls`) |
| LB-002 | Manual F-07 v14 §VIII-§X, Anexos 6-8 (efectuadas AL declarante): Anexo 6 (anticipo 2%, casilla 161): "NIT AGENTE / FECHA / SERIE / NÚMERO / MONTO SUJETO / MONTO ANTICIPO 2% / DUI / anexo 6"; DTE serie = "Sello de recepción del DTE (40 dígitos)". Anexo 7 (retención 1%, casilla 162): el modelo del Anexo 6 "+ TIPO DOC ('05 NC / 06 ND / 07 Comprobante de Retención')". Anexo 8 (percepción 1%, casilla 163): TIPO "03 CCF / 06 ND / 05 NC / 12 Declaración de Mercancía" | F-07 v14 upload manual §§VIII-X, the retention/perception/anticipo annexes effected on the declarant: Anexo 6 column set (agent NIT, date, series, number, subject amount, 2% advance amount, DUI, annex 6) with the DTE series = reception seal (40 digits); Anexo 7 adds the document-type column (credit note, debit note, retention document CRE); Anexo 8 carries the type list CCF, debit note, credit note, merchandise declaration | `sv/sources/34_F07_v14_manual.pdf` | §VIII pp.28-30; §IX pp.31-33; §X pp.34-36 (EVID-177; plantilla sheets "6"-"8") |
| LB-003 | Manual F-07 v14 §XI-§XIV, Anexos 9-12 (efectuadas POR el declarante): Anexo 9 (percepción 1%, casilla 169): "NIT SUJETO / FECHA / TIPO (03/05/06) / RESOLUCIÓN / SERIE / NÚMERO / MONTO SUJETO / PERCEPCIÓN 1% / DUI / anexo 9". Anexo 10 (retención 1%, casilla 170): TIPO 05/06/07. Anexo 11 (anticipo 2%, casilla 171): sin columna de tipo de documento. Anexo 12 (retención 13%, casilla 172): TIPO 05/06/07, "Corresponde al 13% del monto sujeto de la operación" | F-07 v14 upload manual §§XI-XIV, the retention/perception/anticipo annexes effected by the declarant: Anexo 9 column set (subject NIT, date, type CCF/NC/ND, resolution, series, number, subject amount, 1% perception, DUI, annex 9); Anexo 10 type list credit/debit note and retention document; Anexo 11 with NO document-type column; Anexo 12 type list as Anexo 10 with the retention amount = 13% of the operation's subject amount | `sv/sources/34_F07_v14_manual.pdf` | §XI pp.37-39; §XII pp.41-43; §XIII pp.45-47; §XIV pp.48-50 (EVID-177; plantilla sheets "9"-"12") |
| LB-004 | Manual F-07 v14 §VI-§XIV (glosa familiar EVID-177), reglas de familia de los Anexos 4-12: "DUI-vs-NIT XOR from enero 2022 (natural persons), no negatives, anulados excluded"; totalización: "La casilla 108/161/162/163/169/170/171/172 será totalizada automáticamente según los registros cargados" | F-07 v14 upload manual family rules for annexes 4-12: from Enero-2022 natural-person counterparties state either DUI or NIT/NRC, never both; no negative values; voided documents are excluded from the detail annexes; casillas 108, 161, 162, 163, 169, 170, 171 and 172 are totalized automatically from the loaded records | `sv/sources/34_F07_v14_manual.pdf` | §VI-§XIV pp.19-50 (EVID-177; EVID-173) |
| LB-005 | Manual F-07 v14 §XVIII "Detalle de Documentos Emitidos, Anulados o Extraviados": "Con la información cargada de los anexos de Detalle de Ventas a Contribuyentes, Detalle de Ventas a Consumidor Final, Percepciones (casilla 169), Retenciones 1% (casilla 170), Anticipo a Cuenta (casilla 171) y Retención 13% (casilla 172) efectuados por el declarante, podrá visualizar en el apartado de los Documentos Emitidos, Anulados o Extraviados, en la pestaña de 'Automáticos', que se genera el detalle de los Documentos Emitidos. Es decir, que ya no será necesario que se cargue un archivo para los documentos emitidos, sino que solo para los Anulados y/o Extraviados" | F-07 v14 upload manual §XVIII: with the information loaded from annexes 1 (sales to taxpayers), 2 (consumer-final sales), 9 (perceptions, casilla 169), 10 (1% retentions, casilla 170), 11 (2% anticipos, casilla 171) and 12 (13% retentions, casilla 172) effected by the declarant, the "Issued, Voided or Lost Documents" section's "Automáticos" (automatic) tab generates the issued-documents detail — no file upload is needed for issued documents anymore, only for the voided and/or lost ones | `sv/sources/34_F07_v14_manual.pdf` | §XVIII p.54 (EVID-178) |
| LB-006 | Manual F-07 v14 §XIX, anexo de Documentos Anulados/Extraviados, columnas A-J: "A NÚMERO DE RESOLUCIÓN 100 ('Cuando se refiera a una resolución de Documento Tributario Electrónico DTE debe colocar dato alfanumérico ... Si se trata de declaraciones desde septiembre hacia atrás agregar "Código de Generación" y si corresponden a octubre 2022 en adelante "Número de control"') / B CLASE (1/2/4) / C-D DESDE-HASTA (PREIMPRESO; DTE = 'cero') / E TIPO DE DOCUMENTO ('01 FACTURA DE CONSUMIDOR FINAL / 02 FACTURA DE VENTA SIMPLIFICADA / 03 CCF / 04 NOTA DE REMISIÓN / 05 NOTA DE CRÉDITO / 06 NOTA DE DÉBITO / 07 COMPROBANTE DE RETENCIÓN / 08 COMPROBANTE DE LIQUIDACIÓN / 09 DOCUMENTO CONTABLE DE LIQUIDACIÓN / 10 TIQUETES / 11 FACTURA DE EXPORTACIÓN / 14 FACTURA DE SUJETO EXCLUIDO') / F TIPO DE DETALLE ('Documentos Anulados/Invalidados: "A" / Documentos Extraviados: "X" / Documento DTE Invalidado: "D"') / G SERIE (DTE = 'sello de recepción de 40 caracteres, ejemplo: 2116A00512396DCF4A4F9W9429HF171C58134TTG') / H-I DESDE-HASTA (DTE = 0) / J CÓDIGO DE GENERACIÓN: 'Esta columna es exclusiva para documentos DTE Clase 4, deberá colocar Código de Generación con longitud de 36 caracteres' (clases 1/2 vacío)" | F-07 v14 upload manual §XIX, the voided/lost-documents annex column model A-J: resolution number (with the DTE cutover instruction quoted verbatim — defective per LB-007), class 1/2/4, pre-printed from/to ranges (DTE = "zero"), the twelve-type document list (consumer-final invoice, simplified sales invoice, tax-credit document, remission note, credit note, debit note, retention document, liquidation document, accounting liquidation document, tickets, export invoice, excluded-subject invoice), detail type (voided/invalidated "A", lost "X", invalidated DTE "D"), series (DTE = 40-character reception seal, example quoted), from/to (DTE = 0), generation code (exclusively for class-4 DTE documents; classes 1/2 empty) | `sv/sources/34_F07_v14_manual.pdf` | §XIX pp.55-58 (EVID-178) |
| LB-007 | Manual F-07 v14 §XIX, defectos de transcripción + ruling SOQ-10 (S3): col J "Código de Generación con longitud de 36 caracteres" (32 en todas las demás secciones y en el esquema DTE); col A "desde septiembre hacia atrás ... Código de Generación; octubre 2022 en adelante ... Número de control" INVIERTE el cutover de Noviembre-2022 de los Anexos 1-12. **Ruling aplicado (SOQ-10):** defectos de transcripción del manual — la convención de los Anexos 1-12 (32 caracteres; cutover Nov-2022 según SV-FREP-FR-043) es la operativa; el cutover invertido jamás se codifica | F-07 v14 upload manual §XIX transcription defects and the binding SOQ-10 ruling: the J-column "36 characters" contradicts the 32-character generation code used everywhere else; the A-column September/October instruction inverts the November-2022 cutover used by annexes 1-12. Ruling: manual transcription defects — the annexes-1-12 convention (32 chars; Nov-2022 cutover per SV-FREP-FR-043) is operative; the inverted cutover is never encoded (master-index S3 OQ register, SOQ-10; EVID-178 doubt) | `sv/sources/34_F07_v14_manual.pdf` | §XIX pp.55-58 (EVID-178 doubt; 00_MASTER_INDEX SOQ-10) |
| LB-008 | Manual F-07 v14 §IV/§XXII: "Se podrán ingresar valores negativos únicamente para los documentos anulados/invalidados, de acuerdo a lo establecido en el artículo 111 del Código Tributario"; ventana de 3 periodos anteriores para anulados igualmente "de acuerdo a lo establecido en el artículo 111 del Código Tributario" | F-07 v14 upload manual: negative values are admitted ONLY for voided/invalidated documents per CT Art. 111 as printed, and the anulados annex accepts documents dated up to three prior periods under the same CT Art. 111 anchor (the generic negative gate and window rules owned by `01_f07-declaration.md` FR-031/FR-033) | `sv/sources/34_F07_v14_manual.pdf` | §IV; §XXII pp.63-65 (EVID-173; EVID-178) |
| LB-009 | Formulario F-930 v3 "Informe Mensual de Retención/Percepción/Anticipo IVA", §B "DOCUMENTOS × TOTAL DE DOCUMENTOS / MONTO SUJETO / MONTO DE LA RETENCIÓN, PERCEPCIÓN O ANTICIPO A CUENTA": "1. Comprobante de Crédito Fiscal / 2. Documento Contable de Liquidación / 3. Comprobante de Retención / 4. Nota de Débito / 5. Nota de Crédito / 6. Factura / 7. Documento Emitido por Sujeto Excluido"; §C filas por contribuyente: "Correl / NIT / Apellidos y Nombres, Razón Social o Denominación / Calidad en que Actúa / Modalidad / Código / DATOS DOCUMENTOS RECIBIDOS: Fecha / Serie / Número / Monto Sujeto / Monto Retención, Percepción o Anticipo IVA"; codificación: "CALIDAD EN LA QUE ACTÚA" (categorías agente/perceptor) | F-930 v3 form, monthly IVA retention/perception/anticipo inform: Section B document-typed summary — seven document classes (tax-credit document, accounting liquidation document, retention document, debit note, credit note, invoice, excluded-subject issued document) each with total documents, subject amount and the retention/perception/anticipo amount; Section C per-taxpayer rows with correlative, NIT, name, the quality-in-which-the-declarant-acts and modality classifiers, code, and the received documents' date/series/number/subject amount/retention-perception-anticipo amount; the coding appendix carries the CALIDAD EN QUE ACTÚA agent/perceiver categories | `sv/sources/63_F930v3.pdf` | §A-§C + codificación (EVID-189) |
| LB-010 | Formulario F-07 v39_ v14 (EVID-179), etiquetas de cableado: B fila 23 "Ventas Gravadas por Cuenta de Terceros Domiciliados (No debe incluirse en sumatoria de casilla 105) 108"; D filas 45-47 "Anticipo a Cuenta IVA del 2% efectuada al Declarante 161 / Retención IVA del 1% Efectuada al Declarante 162 / Percepción IVA del 1% efectuada al Declarante 163" (→ TOTAL 166); E filas 61-65 "Percepción IVA del 1% efectuada por el Declarante 169 / Retención IVA del 1% Terceros Domiciliados 170 / Anticipo a Cuenta IVA del 2% 171 / Retención IVA del 13% Terceros Domiciliados 172" (→ TOTAL 187) | F-07 v14 form wiring labels: casilla 108 (domiciled third-party sales, excluded from 105) fed by Anexo 4; casillas 161/162/163 (2% anticipo, 1% retention, 1% perception effected on the declarant) fed by annexes 6/7/8 into total 166; casillas 169/170/171/172 (1% perception, 1% retention, 2% anticipo, 13% retention effected by the declarant) fed by annexes 9/10/11/12 into total 187 (casillas owned by `01_f07-declaration.md` FR-009/FR-016/FR-022/FR-023) | `sv/sources/39_F07_v14_form_visual.pdf` | pp.1-2 (EVID-179) |

## 3. Functional Requirements

### 3.1 Anexo 4 — Ventas por Cuenta de Terceros Domiciliados (casilla 108)

- **SV-FREP-FR-095:** The system shall build Anexo 4 (*Ventas por Cuenta
  de Terceros Domiciliados*, sales for the account of DOMICILED third
  parties) with ONE ROW PER EMITTED DOCUMENT sold on behalf of a
  *mandante* (principal), admitting only TIPO DE DOCUMENTO 01 (*Factura*,
  invoice), 03 (*Comprobante de Crédito Fiscal*, tax-credit document),
  05 (*Nota de Crédito*, credit note), 06 (*Nota de Débito*, debit note)
  and 11 (*Factura de Exportación*, export invoice); each row identifies
  the mandante in A (NIT/NRC) and B (name) — and N (DUI) for
  natural-person mandantes under the family DUI-vs-NIT exclusive-or with
  its Enero-2022 gate (mirroring SV-FREP-FR-050); voided and lost
  documents are EXCLUDED and route to the §XIX annex of §3.6; the
  annex's records total casilla 108 automatically (LB-004), which
  `01_f07-declaration.md` FR-009 keeps OUT of the casilla-105 arithmetic.
  (LB-001; LB-004; LB-010; EVID-177; cross-ref SV-FREP-FR-009/050)
- **SV-FREP-FR-096:** The system shall emit every Anexo 4 row with the
  verbatim column model A-O of manual §VI — A NIT/NRC MANDANTE ·
  B NOMBRE MANDANTE · C FECHA · D TIPO DE DOCUMENTO · E SERIE ·
  F RESOLUCIÓN · G NÚMERO · H MONTO · I IVA · J SERIE COMPROBANTE DE
  LIQUIDACIÓN · K RESOLUCIÓN COMPROBANTE DE LIQUIDACIÓN · L NÚMERO
  COMPROBANTE DE LIQUIDACIÓN · M FECHA COMPROBANTE DE LIQUIDACIÓN ·
  N DUI MANDANTE · O NÚMERO DE ANEXO = 4 — in exactly this order,
  conforming to plantilla sheet "4"; amount columns follow the generic
  §II format (SV-FREP-FR-030) and C the DD/MM/AAAA current-period rule
  (SV-FREP-FR-032). (LB-001; EVID-177; cross-ref SV-FREP-FR-030/032)
- **SV-FREP-FR-097:** The system shall apply the *monto sin IVA*
  convention verbatim — "Si declara operaciones de venta con factura de
  consumidor final, deberá detallarlas sin IVA" (if you declare sale
  operations with a consumer-final invoice, you must detail them without
  IVA): on TIPO 01 rows the H MONTO column carries the operation value
  NET of IVA and the I IVA column carries the tax separately (the
  manual prints the rule for consumer-final facturas; for CCF/NC/ND
  rows the same H/I base-vs-tax split is applied by family convention
  — both inferences are recorded in OQ-002). (LB-001; EVID-177)
- **SV-FREP-FR-098:** The system shall fill the
  *comprobante-de-liquidación* linkage block J/K/L + M on every Anexo 4
  row: the series, resolution and number of the CL (*comprobante de
  liquidación*, liquidation document) through which the third-party
  operation is liquidated, plus its date — blank only when the manual's
  fill rules leave the slots blank (the CL slots follow the clase-based
  slot model of SV-FREP-FR-042; DTE-class CLs fill per SV-FREP-FR-043);
  the linkage is stored on the row so the domiciled-third-party channel
  reconciles against the CL record. (LB-001; EVID-177; cross-ref
  SV-FREP-FR-042/043)
- **SV-FREP-FR-099:** The system shall fill the document identifier
  columns E SERIE / F RESOLUCIÓN / G NÚMERO of Anexo 4 under the
  CANONICAL slot model and DTE mapping of
  `02_f07-annexes-sales.md` SV-FREP-FR-042/043 — manual §VI prints the
  twin mapping for this annex (Serie = *sello de recepción*, example
  "2022F2041F1DCE1A4CE4B10B6AABFD344125QTZS"; Resolución = *número de
  control*, pre-Nov-2022 *código de generación*; Número = *código de
  generación* hyphenless 32, pre-Nov-2022 *número de control*
  hyphenless 28), which CONFIRMS the canonical mapping and is never
  restated beyond this printed confirmation. (LB-001; EVID-177;
  cross-ref SV-FREP-FR-042/043)

### 3.2 Annexes 6-8 — retentions/perceptions/anticipos AL declarante (casillas 161-163)

- **SV-FREP-FR-100:** The system shall build Anexo 6 (*Anticipo a Cuenta
  IVA del 2% efectuada al Declarante*, 2% IVA advance effected on the
  declarant) with one row per document on which an AGENT applied a 2%
  anticipo to the declarant, with the verbatim column set of manual
  §VIII — NIT AGENTE · FECHA · SERIE · NÚMERO · MONTO SUJETO · MONTO
  ANTICIPO 2% · DUI · NÚMERO DE ANEXO = 6 — conforming to plantilla
  sheet "6" (the manual prints an ordered list, not column letters —
  letters are assigned by printed position, OQ-005); DTE rows fill SERIE
  with the *sello de recepción* "del DTE (40 dígitos)" per the canonical
  SERIE-slot rule of SV-FREP-FR-043; the records total casilla 161
  automatically (LB-004). (LB-002; LB-004; EVID-177; cross-ref
  SV-FREP-FR-042/043)
- **SV-FREP-FR-101:** The system shall build Anexo 7 (*Retención IVA del
  1% Efectuada al Declarante*, 1% IVA retention effected on the
  declarant) with the Anexo 6 column set PLUS a TIPO DE DOCUMENTO
  column admitting only 05 (*Nota de Crédito*), 06 (*Nota de Débito*)
  and 07 (*Comprobante de Retención*, retention document — CRE: the
  document type through which IVA retentions enter the DTE world),
  conforming to plantilla sheet "7" (column position per the plantilla,
  OQ-005); the records total casilla 162 automatically (LB-004).
  (LB-002; LB-004; EVID-177; cross-ref SV-FREP-FR-042/043)
- **SV-FREP-FR-102:** The system shall build Anexo 8 (*Percepción IVA
  del 1% efectuada al Declarante*, 1% IVA perception effected on the
  declarant) with the Anexo 6 column set plus its TIPO DE DOCUMENTO
  column admitting only 03 (*Comprobante de Crédito Fiscal*), 05
  (*Nota de Crédito*), 06 (*Nota de Débito*) and 12 (*Declaración de
  Mercancías*, merchandise/customs declaration — the DUA channel through
  which import-side perceptions arrive), conforming to plantilla sheet
  "8" (OQ-005); the records total casilla 163 automatically (LB-004).
  (LB-002; LB-004; EVID-177)
- **SV-FREP-FR-103:** The system shall fill the counterparty
  identification of annexes 6-8 (the retention/perception/anticipo
  AGENT) and 9-12 (the SUBJECT on whom the declarant acted) from the
  counterparty master data of the row's source document: the NIT/NRC
  column (NIT AGENTE / NIT SUJETO) and the DUI column — enforcing the
  family DUI-vs-NIT exclusive-or with its Enero-2022 gate (LB-004;
  mirrored from SV-FREP-FR-050: from Enero-2022 natural-person
  counterparties state EITHER the DUI OR the NIT/NRC, never both or
  neither; before Enero-2022 the NIT/NRC is mandatory; juridical persons
  always carry the NIT/NRC). (LB-002; LB-003; LB-004; EVID-177;
  cross-ref SV-FREP-FR-050)

### 3.3 Annexes 9-12 — retentions/perceptions/anticipos POR el declarante (casillas 169-172)

- **SV-FREP-FR-104:** The system shall build Anexo 9 (*Percepción IVA
  del 1% efectuada por el Declarante*, 1% IVA perception effected by the
  declarant) with one row per document on which the declarant applied a
  1% perception, with the verbatim column set of manual §XI — NIT
  SUJETO · FECHA · TIPO (03/05/06 only) · RESOLUCIÓN · SERIE · NÚMERO ·
  MONTO SUJETO · PERCEPCIÓN 1% · DUI · NÚMERO DE ANEXO = 9 — conforming
  to plantilla sheet "9" (letters by printed position, OQ-005); the
  records total casilla 169 automatically (LB-004). (LB-003; LB-004;
  EVID-177)
- **SV-FREP-FR-105:** The system shall build Anexo 10 (*Retención IVA
  del 1% Terceros Domiciliados*, 1% IVA retention on domiciled third
  parties) with the Anexo 9 column set, its TIPO DE DOCUMENTO column
  admitting only 05, 06 and 07 (CRE), conforming to plantilla sheet
  "10"; the records total casilla 170 automatically (LB-004).
  (LB-003; LB-004; EVID-177)
- **SV-FREP-FR-106:** The system shall build Anexo 11 (*Anticipo a
  Cuenta IVA del 2%*, 2% IVA advance) with the Anexo 9 column set
  MINUS the document-type column — manual §XIII prints NO tipo-doc
  column for this annex — conforming to plantilla sheet "11"; the
  records total casilla 171 automatically (LB-004). (LB-003; LB-004;
  EVID-177)
- **SV-FREP-FR-107:** The system shall build Anexo 12 (*Retención IVA
  del 13% Terceros Domiciliados*, 13% IVA retention on domiciled third
  parties) with the Anexo 9 column set, its TIPO DE DOCUMENTO column
  admitting only 05, 06 and 07, and its retention column validated as
  exactly "el 13% del monto sujeto de la operación" (13% of the
  operation's subject amount); the records total casilla 172
  automatically (LB-004). DISTINCTION (binding, per the F-cluster
  crossref): this is the PAYABLE side — retentions the declarant
  EFFECTED and must remit; the 13% CREDIT side of CT Art. 162 (casilla
  128, post-*entero* re-entry) belongs to
  `03_f07-annexes-purchases.md` SV-FREP-FR-091, and the ISR retention
  matrix of `taxation/04_isr-withholding.md` is a different tax — the
  two matrices stay distinct. (LB-003; LB-004; LB-010; EVID-177;
  cross-ref SV-FREP-FR-091)
- **SV-FREP-FR-108:** The system shall validate the percent column of
  every retention/perception/anticipo row as exactly the annex's rate
  applied to the row's MONTO SUJETO — 2% on annexes 6/11 (MONTO
  ANTICIPO 2%), 1% on annexes 7/8/9/10, 13% on annex 12 — under the
  two-decimal discipline of SV-FREP-FR-027, surfacing any row whose
  percent column differs from rate × MONTO SUJETO as a validation
  inconsistency before export (MH-side upload validator parity: the
  MH system rejects such files; the Odoo builder performs the same
  check pre-emptively). (LB-002; LB-003; EVID-177; cross-ref
  SV-FREP-FR-027)
- **SV-FREP-FR-109:** The system shall apply the family row rules of
  LB-004 to every annex 4/6-12 row: voided/lost documents are EXCLUDED
  from the detail rows and route to the §XIX annex (§3.6); NO negative
  values are emitted (negative gate inherited from SV-FREP-FR-031 —
  negatives live only in the anulados annex); date cells follow the
  DD/MM/AAAA current-period rule (SV-FREP-FR-032 — the three-prior-
  period window of SV-FREP-FR-033 does NOT extend to these annexes);
  and the fed casillas 108/161/162/163/169/170/171/172 are totalized
  automatically from the loaded records — "será totalizada
  automáticamente según los registros cargados" — with no manual
  casilla fill (SV-FREP-FR-038). (LB-004; LB-008; EVID-177; EVID-173;
  cross-ref SV-FREP-FR-031/032/038)

### 3.4 Aggregation into the declaration casillas

- **SV-FREP-FR-110:** The system shall aggregate the retention-family
  annex totals into the Task 1 casillas per the §4 wiring table: the
  CREDIT side — annex 6 MONTO ANTICIPO 2% → casilla 161, annex 7
  retention column → 162, annex 8 perception column → 163, entering
  Section D's total 166 = 161+162+163+164+165 owned by
  SV-FREP-FR-016; and the PAYABLE side — annex 9 → 169, annex 10 →
  170, annex 11 → 171, annex 12 → 172, entering Section E's total 187
  = 169+170+171+172 with its modificatoria anchor 188 and result 190
  owned by SV-FREP-FR-022/023; the percent columns are the wired
  amounts (MONTO SUJETO columns feed NO casilla of Sections D/E).
  (LB-002; LB-003; LB-004; LB-010; EVID-177; EVID-179; cross-ref
  SV-FREP-FR-016/022/023)

### 3.5 F-930 — Informe Mensual de Retención/Percepción/Anticipo IVA (view over the retention ledger)

- **SV-FREP-FR-111:** The system shall implement the F-930 v3 (*Informe
  Mensual de Retención/Percepción/Anticipo IVA*, monthly IVA
  retention/perception/anticipo inform) as a VIEW over the SAME
  retention ledger that builds annexes 9-12 — one ledger model
  (§4 l10n_sv.iva.retention.ledger, side = effected) feeding BOTH the
  F-07 annex exports and the F-930 report — and shall NOT create a
  second ledger, entry surface or posting path for the F-930: a
  retention row edited once reflects identically in the annex 9-12
  exports and the F-930 lines (EVID-189 gloss: data source identical
  to F-07 annexes 9-12). (LB-009; EVID-189; EVID-177)
- **SV-FREP-FR-112:** The system shall render the F-930 §B summary as
  the document-typed matrix "DOCUMENTOS × TOTAL DE DOCUMENTOS / MONTO
  SUJETO / MONTO DE LA RETENCIÓN, PERCEPCIÓN O ANTICIPO A CUENTA"
  grouped by the seven printed document classes — 1 Comprobante de
  Crédito Fiscal · 2 Documento Contable de Liquidación · 3
  Comprobante de Retención · 4 Nota de Débito · 5 Nota de Crédito ·
  6 Factura · 7 Documento Emitido por Sujeto Excluido — each row
  counting the ledger rows of its class and summing their MONTO SUJETO
  and retention/perception/anticipo amounts (the class grouping is
  label-matched to the annex tipo catalog — 1↔03, 2↔09, 3↔07, 4↔06,
  5↔05, 6↔01, 7↔14 — OQ-007 confirms the mapping). (LB-009; EVID-189)
- **SV-FREP-FR-113:** The system shall render the F-930 §C
  per-contribuyente detail from the same ledger rows: Correl · NIT ·
  name (*Apellidos y Nombres, Razón Social o Denominación*) · *Calidad
  en que Actúa* (quality in which the declarant acts) · *Modalidad* ·
  Código · and the received-document block Fecha / Serie / Número /
  Monto Sujeto / Monto Retención, Percepción o Anticipo IVA — with
  the calidad and modalidad classifiers taken from the form's
  codificación (agent/perceiver categories); the codificación's code
  VALUES are not in the corpus and are consumed as configuration data
  (OQ-001). (LB-009; EVID-189)
- **SV-FREP-FR-114:** The system shall scope the F-930 as the monthly
  inform per taxpayer per *período tributario* (tax period) — a
  reporting surface SEPARATE from the F-07 declaration (its own
  filing obligation), sourced exclusively from the effected-side
  ledger (annexes 9-12 territory); version regime (D12): form v3 is a
  2017-era print still listed by MH as of 2026-08-18 (EVID-189 doubt)
  — the layout is seeded per form_version so a v4 re-seeds without
  code change (OQ-006); due-day scheduling belongs to
  `08_filing-calendar.md` (SOQ-08) and is not encoded here.
  (LB-009; EVID-189)

### 3.6 §XIX annex — Documentos Anulados/Extraviados/DTE Invalidados + auto-emitidos + invalidation feed

- **SV-FREP-FR-115:** The system shall build the §XIX annex
  (*Documentos Anulados, Extraviados o DTE Invalidados* — voided, lost
  or invalidated documents) with ONE ROW PER voided/lost/invalidated
  document (or DEL/AL range for pre-printed physical ranges), with the
  verbatim column model A-J of manual §XIX — A NÚMERO DE RESOLUCIÓN
  (100) · B CLASE DE DOCUMENTO (1/2/4) · C DESDE (PREIMPRESO) ·
  D HASTA (PREIMPRESO) · E TIPO DE DOCUMENTO · F TIPO DE DETALLE ·
  G SERIE · H DESDE · I HASTA · J CÓDIGO DE GENERACIÓN — in exactly
  this order; §XIX prints NO trailing annex-number column and NO
  date/amount column in the A-J model (the annex-number gap vs the
  generic last-column rule of SV-FREP-FR-034 and the date gap vs the
  §II DD/MM/AAAA discipline — which the CT 111 window of FR-119
  presupposes — are recorded in OQ-003; the row STORES its underlying
  document date as the window-validation field even though A-J does
  not print it). (LB-006; EVID-178)
- **SV-FREP-FR-116:** The system shall fill the F TIPO DE DETALLE
  column with the verbatim detail codes — **A** for *Documentos
  Anulados/Invalidados* (voided documents, physical/business
  annulment), **X** for *Documentos Extraviados* (lost documents),
  **D** for *Documento DTE Invalidado* (a DTE invalidated by sealed
  invalidation event) — and the clase-dependent fills: clase 1/2 rows
  carry the physical document ranges in the two DESDE/HASTA pairs —
  C/D (the PREIMPRESO pre-printed range) and H/I (the document-number
  range) — with G = the physical series and J EMPTY; clase 4 rows
  carry "cero" (0) in C/D
  and H/I ("PREIMPRESO; DTE = 'cero'", "DTE = 0"), G = the *sello de
  recepción* (reception seal) of 40 characters (example printed:
  "2116A00512396DCF4A4F9W9429HF171C58134TTG"), and J = the *código
  de generación* (generation code) — J is "exclusiva para documentos
  DTE Clase 4". (LB-006; EVID-178)
- **SV-FREP-FR-117:** The system shall admit on the §XIX annex the
  FULL twelve-type document list verbatim — 01 FACTURA DE CONSUMIDOR
  FINAL · 02 FACTURA DE VENTA SIMPLIFICADA · 03 CCF · 04 NOTA DE
  REMISIÓN · 05 NOTA DE CRÉDITO · 06 NOTA DE DÉBITO · 07 COMPROBANTE
  DE RETENCIÓN · 08 COMPROBANTE DE LIQUIDACIÓN · 09 DOCUMENTO
  CONTABLE DE LIQUIDACIÓN · 10 TIQUETES · 11 FACTURA DE EXPORTACIÓN ·
  14 FACTURA DE SUJETO EXCLUIDO — the ONLY place in the F-07 where
  types 04 (*nota de remisión*, remission note — NRE), 08 (CLE), 09
  (DCL) and 14 (*factura de sujeto excluido*, excluded-subject invoice
  — FSE) appear as admissible codes. (LB-006; EVID-178)
- **SV-FREP-FR-118:** The system shall apply the SOQ-10 ruling as the
  operative convention on the §XIX annex and shall NEVER encode the
  manual's defective instructions: column J carries the *código de
  generación* hyphenless at **32** characters (not the printed "36" —
  transcription defect), and column A carries the canonical
  RESOLUCIÓN-slot value of SV-FREP-FR-043 — the *número de control*
  hyphenless (28) from the Noviembre-2022 period forward and the
  *código de generación* hyphenless (32) before it (NOT the printed
  inverted September/October instruction) — for DTE rows; the defects
  and the ruling are recorded as LB-007 for traceability.
  (LB-006; LB-007; EVID-178; cross-ref SV-FREP-FR-043)
- **SV-FREP-FR-119:** The system shall apply the anulados value and
  window rules: the §XIX annex is the ONLY annex whose rows may carry
  negative values (CT Art. 111 as printed — the negative gate of
  SV-FREP-FR-031 opens here), and it accepts documents dated up to
  THREE prior periods before the declared period under the same CT
  Art. 111 anchor (SV-FREP-FR-033's anulados window); every other
  annex of this file remains current-period-only and negative-free
  (FR-109). (LB-008; EVID-173; EVID-178; cross-ref
  SV-FREP-FR-031/033)
- **SV-FREP-FR-120:** The system shall DERIVE the *Documentos
  Emitidos* (issued documents) detail automatically from the loaded
  annex rows — annexes 1 (*Detalle de Ventas a Contribuyentes*), 2
  (*Detalle de Ventas a Consumidor Final*), 9 (perceptions, casilla
  169), 10 (1% retentions, casilla 170), 11 (anticipos, casilla 171)
  and 12 (13% retentions, casilla 172) — replicating manual §XVIII:
  the "Automáticos" tab of the *Documentos Emitidos, Anulados o
  Extraviados* section "se genera el detalle de los Documentos
  Emitidos" from those uploads, so that NO upload file is produced or
  required for issued documents — only the anulados/extraviados rows
  are uploaded; the derived emitidos view is read-only and recomputed
  from its source annexes (never independently editable).
  (LB-005; EVID-178)
- **SV-FREP-FR-121:** The system shall build D-code rows of the §XIX
  annex from the e-invoicing invalidation-event feed: the SOURCE of
  *Documento DTE Invalidado* rows is the sealed invalidation events
  owned by `e-invoicing/03_events.md` — SV-EINV-FR-103 (differentiated
  invalidation deadlines), SV-EINV-FR-104 (event-date correspondence)
  and SV-EINV-FR-117 (retorno windows, cited to bound the interface) —
  read from the client event mirror (l10n_sv_edi.event /
  l10n_sv_edi.event.invalidacion: tipoDte, codigoGeneracion,
  selloRecibido, numeroControl, fecEmi); a DTE with a SEALED
  invalidation event enters the §XIX annex of the applicable period
  (its window per FR-119) as TIPO DE DETALLE **D** with its clase-4
  fills per FR-116 — this CLOSES the F-07 side of
  `e-invoicing/02_transmission.md` OQ-008 (invalidated DTEs present
  as detail code D); retorno events do NOT produce D rows (a retorno
  never invalidates its origin document, SV-EINV-FR-119), and the
  F-14/retorno presentation side of that OQ remains OPEN with
  e-invoicing (the retorno gap stays there — not encoded here).
  (LB-006; EVID-178; cross-ref SV-EINV-FR-103/104/117/119;
  e-invoicing 02 OQ-008)
- **SV-FREP-FR-122:** The system shall build this file's annex rows
  from POSTED documents and events: Anexo 4 from posted third-party
  sale documents (customer invoices/CCF/NC/ND issued on behalf of a
  mandante, Odoo `account.move`); annexes 6-8 from posted documents
  where a counterparty agent retained/perceived/advanced on the
  declarant (vendor-side documents and bank/cash entries carrying the
  retention); annexes 9-12 from posted documents where the declarant
  acted as agent/perceptor (customer-side and payment entries posting
  the retention accrual) — all landing in the single retention ledger
  of FR-111; §XIX A/X rows from locally voided/lost physical
  documents and D rows from FR-121's event feed; export runs under
  the generic engine of SV-FREP-FR-028..041 (clean-replace per
  annex), and the *declaración modificatoria* carryover of
  SV-FREP-FR-040 carries annexes 4/6-12 (within the printed "anexos 3
  al 12") from the prior same-period declaration — the §XIX annex's
  own carryover is not printed (OQ-004). (LB-001; LB-002; LB-003;
  LB-005; EVID-177; EVID-178; EVID-173; cross-ref SV-FREP-FR-028..041,
  SV-FREP-FR-040)
- **SV-FREP-FR-123:** The system shall expose this file's feeds as the
  §4 wiring interface into the Task 1 casilla engine — annex 4 → 108
  (kept out of 105 by SV-FREP-FR-009); annexes 6/7/8 → 161/162/163
  (into 166 per SV-FREP-FR-016); annexes 9/10/11/12 → 169/170/171/172
  (into 187/188/190 per SV-FREP-FR-022/023) — with casilla 108 fed by
  the Anexo 4 H MONTO column (the sin-IVA base, per FR-097 — H-only
  basis, OQ-002); no casilla is filled manually (SV-FREP-FR-038) and
  the §XIX/emitidos surfaces feed NO casilla (they are informational
  detail of the declaration). (LB-004; LB-010; EVID-177; EVID-179;
  cross-ref SV-FREP-FR-009/016/022/023/038)

## 4. Data Model

No CSV sidecars live next to this file: the column models, code lists,
wiring and catalogs below are in-file §4 seed data. Layer semantics:
Odoo-side computation/bookkeeping data only (wave default `odoo`; see
§5). The retention ledger is THE single bookkeeping model for the whole
IVA retention/perception/anticipo family (F-07 annexes 9-12 exports +
the F-930 view; annexes 6-8 rows share the model with side =
'received').

**Anexo 4 row model — l10n_sv.f07.annex4.row (seed structure; verbatim
from manual §VI / plantilla sheet "4"):**

| Col | Header (Spanish, verbatim) | Length | Semantics | FR |
|-----|----------------------------|--------|-----------|----|
| A | NIT/NRC MANDANTE | 14 (family) | principal's NIT/NRC; XOR with N (Enero-2022 gate) | FR-095 |
| B | NOMBRE MANDANTE | sin límite impreso | principal's name | FR-095 |
| C | FECHA | 10 | DD/MM/AAAA; current period only | FR-096, FR-109 |
| D | TIPO | 2 | 01 factura · 03 CCF · 05 NC · 06 ND · 11 factura de exportación | FR-095 |
| E | SERIE | plantilla | slot per FR-042; DTE = sello de recepción (40) per FR-043 (printed §VI) | FR-099 |
| F | RESOLUCIÓN | plantilla | slot per FR-042; DTE = número de control (28; pre-Nov-2022 código de generación 32) per FR-043 (printed §VI) | FR-099 |
| G | NÚMERO | plantilla | slot per FR-042; DTE = código de generación (32; pre-Nov-2022 número de control 28) per FR-043 (printed §VI) | FR-099 |
| H | MONTO | 10 (§II) | operation value NET of IVA on tipo-01 rows (sin-IVA convention) → casilla 108 basis (OQ-002) | FR-097 |
| I | IVA | 10 (§II) | the IVA of the operation | FR-097 |
| J | SERIE COMPROBANTE DE LIQUIDACIÓN | plantilla | CL series (clase-based slot per FR-042) | FR-098 |
| K | RESOLUCIÓN COMPROBANTE DE LIQUIDACIÓN | plantilla | CL resolution | FR-098 |
| L | NÚMERO COMPROBANTE DE LIQUIDACIÓN | plantilla | CL number | FR-098 |
| M | FECHA COMPROBANTE DE LIQUIDACIÓN | 10 | CL date | FR-098 |
| N | DUI MANDANTE | 9 (family) | principal's DUI; XOR with A (Enero-2022 gate) | FR-095 |
| O | NÚMERO DE ANEXO | 1 | literal 4 on every row | FR-096 |

**Retention ledger — l10n_sv.iva.retention.ledger (THE single model;
annexes 6-12 rows are projections; the F-930 is a view over it):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| company_id, period_month, period_year | m2o/int | one row per retention/perception/anticipo document | FR-111, FR-122 |
| side | select | effected (annexes 9-12 + F-930) · received (annexes 6-8) | FR-111, FR-122 |
| kind | select | anticipo_2 · retencion_1 · percepcion_1 · retencion_13 | FR-100..FR-107 |
| rate | float | 0.02 · 0.01 · 0.13 (annex-determined) | FR-108 |
| counterparty_partner_id / counterparty_nit_nrc / counterparty_dui | m2o/char(14)/char(9) | agent (6-8) or subject (9-12); DUI-vs-NIT XOR gate | FR-103 |
| date | date | current period only | FR-109 |
| clase / tipo | select | per-annex lists (see catalog below); annex 11 carries no tipo | FR-100..FR-107 |
| resolucion / serie / numero | char | canonical FR-042/043 slot fills (sello 40 / número de control 28 / código 32; Nov-2022 swap) | FR-099..FR-107 |
| monto_sujeto / monto_retencion | monetary(2dp) | subject amount and the rate × subject retention (FR-108 validation) | FR-108 |
| annex_no | computed | 6/7/8 (side received) · 9/10/11/12 (side effected) per kind | FR-110 |
| source_move_id / source_event_id | m2o | posted account.move (FR-122); null for manual rows | FR-122 |

Per-annex row shapes (letters by printed position — OQ-005; amounts and
dates under the §II discipline of 01 §3.2): annex 6 = NIT AGENTE ·
FECHA · SERIE · NÚMERO · MONTO SUJETO · MONTO ANTICIPO 2% · DUI ·
anexo 6; annex 7 = annex 6 + TIPO DOC (05/06/07); annex 8 = annex 6 +
TIPO DOC (03/05/06/12); annex 9 = NIT SUJETO · FECHA · TIPO (03/05/06)
· RESOLUCIÓN · SERIE · NÚMERO · MONTO SUJETO · PERCEPCIÓN 1% · DUI ·
anexo 9; annex 10 = annex 9 shape with TIPO (05/06/07); annex 11 =
annex 9 shape WITHOUT the tipo column; annex 12 = annex 9 shape with
TIPO (05/06/07) and the 13% column. Annexes 6-8 print NO resolución
column; annexes 9-12 print the full triplet (FR-100..FR-107).

**§XIX anulados row model — l10n_sv.f07.anulados.row (seed structure;
verbatim from manual §XIX):**

| Col | Header (Spanish, verbatim) | Length | Semantics | FR |
|-----|----------------------------|--------|-----------|----|
| A | NÚMERO DE RESOLUCIÓN | 100 | physical: MH resolution of the printed range; DTE: canonical RESOLUCIÓN-slot value (número de control 28 post-Nov-2022 / código de generación 32 pre) — SOQ-10 ruling, never the inverted instruction | FR-118 |
| B | CLASE DE DOCUMENTO | 1 | 1 · 2 · 4 | FR-116 |
| C | DESDE (PREIMPRESO) | plantilla | pre-printed range start; DTE = 0 ("cero") | FR-116 |
| D | HASTA (PREIMPRESO) | plantilla | pre-printed range end; DTE = 0 | FR-116 |
| E | TIPO DE DOCUMENTO | 2 | the 12-type list (catalog below) | FR-117 |
| F | TIPO DE DETALLE | 1 | A anulados · X extraviados · D DTE invalidado | FR-116, FR-121 |
| G | SERIE | 40 (DTE) | physical series; DTE = sello de recepción (example 2116A00512396DCF4A4F9W9429HF171C58134TTG) | FR-116 |
| H | DESDE | plantilla | physical range start; DTE = 0 | FR-116 |
| I | HASTA | plantilla | physical range end; DTE = 0 | FR-116 |
| J | CÓDIGO DE GENERACIÓN | 32 (operative — SOQ-10; manual prints "36" = defect) | exclusively clase 4; hyphenless; empty for clases 1/2 | FR-116, FR-118 |

Additional fields: source (select: manual_row · invalidation_event),
invalidation_event_id (m2o l10n_sv_edi.event — FR-121), declaration_id,
window check fields (3-prior-period, CT 111 — FR-119). The §XIX file
prints NO trailing annex-number column (OQ-003).

**Emitidos derived view — l10n_sv.f07.emitidos.row (read-only,
computed):** declaration_id · source_annex (1/2/9/10/11/12) ·
source_row_id · clase · tipo · date · identifier slots — recomputed
from the source annexes, never edited (FR-120).

**F-930 view — l10n_sv.f930.report + lines (view over the ledger):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.f930.report (new) | company_id, period_month, period_year, form_version | m2o/int/char | form_version default f930_v3 (D12 seed; OQ-006) | FR-114 |
| l10n_sv.f930.summary.line (new) | report_id, doc_class, total_documentos, monto_sujeto, monto_retencion | select/int/monetary(2dp) | doc_class: 1 CCF · 2 DCL · 3 CR · 4 ND · 5 NC · 6 factura · 7 FSEE (label-matched to tipos 03/09/07/06/05/01/14 — OQ-007) | FR-112 |
| l10n_sv.f930.detail.line (new) | report_id, correl, partner_nit, partner_name, calidad, modalidad, codigo, doc_fecha, doc_serie, doc_numero, monto_sujeto, monto_retencion | int/char/date/monetary(2dp) | calidad/modalidad from the form codificación (values absent from corpus — configuration data, OQ-001) | FR-113 |

**Column→casilla wiring (interface into 01 §3.1; casillas owned by
Task 1):**

| Annex column | Casilla (label match) | Notes |
|--------------|----------------------|-------|
| Anexo 4 H (+I?) | 108 terceros domiciliados | EXCLUDED from 105 (01 FR-009); column basis H vs H+I unprinted — OQ-002; CL-side débito wiring (98/99/144) recorded-unwired per 01 OQ-005 |
| Anexo 6 MONTO ANTICIPO 2% | 161 | → 166 (01 FR-016) |
| Anexo 7 retención column | 162 | → 166 |
| Anexo 8 percepción column | 163 | → 166 |
| Anexo 9 PERCEPCIÓN 1% | 169 | → 187 (01 FR-022/023) |
| Anexo 10 retención column | 170 | → 187 |
| Anexo 11 MONTO ANTICIPO 2% | 171 | → 187 |
| Anexo 12 retención 13% | 172 | → 187; credit side of CT 162 = 03's FR-091, distinct |
| MONTO SUJETO columns | — (no casilla) | Section D/E wire only the percent columns |
| §XIX / emitidos | — (no casilla) | informational detail |

**Code lists (seed data):**

| List | Values |
|------|--------|
| Anexo 4 tipos | 01 factura · 03 CCF · 05 NC · 06 ND · 11 factura de exportación |
| Anexo 7 tipos | 05 NC · 06 ND · 07 comprobante de retención (CRE) |
| Anexo 8 tipos | 03 CCF · 05 NC · 06 ND · 12 declaración de mercancías |
| Anexo 9 tipos | 03 CCF · 05 NC · 06 ND |
| Anexo 10 tipos | 05 NC · 06 ND · 07 CRE |
| Anexo 11 tipos | — (no tipo column) |
| Anexo 12 tipos | 05 NC · 06 ND · 07 CRE |
| §XIX detail codes | A anulados/invalidados (physical) · X extraviados · D DTE invalidado (event-fed) |
| §XIX document types | 01 · 02 · 03 · 04 NRE · 05 · 06 · 07 · 08 CLE · 09 DCL · 10 · 11 · 14 FSE (only place 04/08/09/14 appear in F-07) |
| §XIX clases | 1 · 2 · 4 (DTE zeros/blank rules per FR-116) |
| F-930 §B classes | 1 CCF · 2 documento contable de liquidación · 3 comprobante de retención · 4 nota de débito · 5 nota de crédito · 6 factura · 7 documento emitido por sujeto excluido |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these
FRs touch DTE generation/transformation (an architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`); FR-121
READS the sealed-event client mirror (l10n_sv_edi.event) that the
e-invoicing module owns. Model names are stable across Odoo
17/18/19/20; version-specific behavior is recorded per row where a
legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-095 | odoo | l10n_sv.f07.annex4.row | granularity + tipo gate + mandante id | Tipos 01/03/05/06/11; XOR Enero-2022 gate (mirror of 02 FR-050); anulados routing to §XIX; 108 auto-total (01 FR-038/FR-009) |
| FR-096 | odoo | l10n_sv.f07.annex4.row | column order A-O | Plantilla sheet "4" conformance; O = 4 on every row |
| FR-097 | odoo | l10n_sv.f07.annex4.row | monto/iva split | Sin-IVA detail on tipo-01 rows (verbatim convention); CCF counterpart by family convention — OQ-002 |
| FR-098 | odoo | l10n_sv.f07.annex4.row | CL linkage J-M | Slots per canonical FR-042 (clase-based); reconciliation against the CL record |
| FR-099 | odoo | l10n_sv.f07.annex4.row + l10n_sv.f07.idmap (02 file, read) | E/F/G fills | §VI prints the twin mapping (sello example; 32/28 swap) — printed confirmation of FR-042/043, never restated |
| FR-100 | odoo | l10n_sv.iva.retention.ledger | kind=anticipo_2, side=received | Annex 6 projection; sello 40 SERIE fill per FR-043; → 161 |
| FR-101 | odoo | l10n_sv.iva.retention.ledger | kind=retencion_1, side=received + tipo | Tipos 05/06/07 (CRE); → 162 |
| FR-102 | odoo | l10n_sv.iva.retention.ledger | kind=percepcion_1, side=received + tipo | Tipos 03/05/06/12 (DUA channel); → 163 |
| FR-103 | odoo | l10n_sv.iva.retention.ledger + res.partner | counterparty id + XOR | NIT AGENTE/NIT SUJETO + DUI; Enero-2022 gate; juridical → NIT always |
| FR-104 | odoo | l10n_sv.iva.retention.ledger | kind=percepcion_1, side=effected | Annex 9 projection; tipos 03/05/06; → 169 |
| FR-105 | odoo | l10n_sv.iva.retention.ledger | kind=retencion_1, side=effected | Tipos 05/06/07; → 170 |
| FR-106 | odoo | l10n_sv.iva.retention.ledger | kind=anticipo_2, side=effected | NO tipo column printed (§XIII); → 171 |
| FR-107 | odoo | l10n_sv.iva.retention.ledger | kind=retencion_13, side=effected | 13% of monto sujeto; PAYABLE side — CT 162 credit side = 03's FR-091; ISR matrix distinct |
| FR-108 | odoo | l10n_sv.iva.retention.ledger | rate validation | 2%/1%/1%/1%/1%/13%/13% per annex × monto_sujeto, 2dp (01 FR-027); MH validator parity; AC-001 |
| FR-109 | odoo | l10n_sv.iva.retention.ledger + l10n_sv.f07.annex4.row | family row rules | Anulados excluded → XIX; no negatives (01 FR-031); current-period dates (01 FR-032); auto-total (01 FR-038) |
| FR-110 | odoo | l10n_sv.f07.casilla.value (01 file) + §4 wiring | totals interface | 161-163 → 166 (01 FR-016); 169-172 → 187 (01 FR-022/023); MONTO SUJETO unwired; AC-007 |
| FR-111 | odoo | l10n_sv.iva.retention.ledger + l10n_sv.f930.report | one-ledger view | F-930 = VIEW over the annex 9-12 ledger — no second ledger/entry surface; AC-011 |
| FR-112 | odoo | l10n_sv.f930.summary.line | §B matrix | 7 doc classes × totals; label-matched tipo mapping — OQ-007; AC-006 |
| FR-113 | odoo | l10n_sv.f930.detail.line | §C rows | Calidad/modalidad from codificación (values absent — configuration data, OQ-001) |
| FR-114 | odoo | l10n_sv.f930.report | scope + version | D12: v3 2017-era print still listed (OQ-006); form_version-seeded; due days = file 08 (SOQ-08) |
| FR-115 | odoo | l10n_sv.f07.anulados.row | column order A-J | §XIX prints NO annex-number column — OQ-003 (vs 01 FR-034) |
| FR-116 | odoo | l10n_sv.f07.anulados.row | detail codes + clase fills | A/X/D; clase 4 zeros in C/D/H/I, sello 40 in G, código in J; clases 1/2 J empty |
| FR-117 | odoo | l10n_sv.f07.anulados.row + l10n_latam.document.type | 12-type list | Only F-07 surface for 04 NRE / 08 CLE / 09 DCL / 14 FSE |
| FR-118 | odoo | l10n_sv.f07.anulados.row + l10n_sv.f07.idmap (02 file, read) | SOQ-10 ruling fills | J = 32 chars (not "36"); A = canonical RESOLUCIÓN-slot (número de control post-Nov-2022 / código before) — inverted instruction never encoded; AC-004/AC-008 |
| FR-119 | odoo | l10n_sv.f07.anulados.row | negatives + window | CT 111 negative exception (01 FR-031) and 3-prior-period window (01 FR-033); AC-009 |
| FR-120 | odoo | l10n_sv.f07.emitidos.row (derived) | auto-emitidos | Derived from annexes 1/2/9/10/11/12 (§XVIII); read-only recompute; no upload surface; AC-005 |
| FR-121 | odoo | l10n_sv.f07.anulados.row + l10n_sv_edi.event (e-invoicing mirror, read) | invalidation feed | Sealed invalidation events → D rows; SV-EINV-FR-103/104/117 cited, never restated; closes e-invoicing 02 OQ-008's F-07 side; retorno gap stays with e-invoicing; AC-004 |
| FR-122 | odoo | account.move + l10n_sv.iva.retention.ledger + l10n_sv.f07.annex.upload (01 engine) | builders + export | Posted moves only; export under 01 FR-028..041; modificatoria carryover covers 4/6-12 (01 FR-040); §XIX carryover unprinted — OQ-004; AC-010/AC-012 |
| FR-123 | odoo | l10n_sv.f07.casilla.value (01 file) + §4 wiring | full wiring interface | 108/161-163/169-172 feeds; §XIX/emitidos informational; AC-007 |

Version-regime notes (D12): four dated elements touch this file — the
Enero-2022 DUI-vs-NIT XOR gate (FR-095/FR-103, defined as dated data in
02's FR-050), the Noviembre-2022 DTE identifier cutover (FR-099/FR-118,
dated data owned by 02's FR-043), the v14 manual vintage (annex
structures; a future manual revision re-seeds the row models), and the
F-930 v3 2017-era print (FR-114, OQ-006 — layout seeded per
form_version). The §XVIII auto-emitidos behavior and the D detail code
are v14-manual features (no earlier-vintage rows needed). The filing
due-day windows remain F12 territory (`08_filing-calendar.md`; SOQ-08) —
no deadline behavior is encoded here. Cross-file canonicality:
SV-FREP-FR-042/043 (02) own the identifier mapping; SV-FREP-FR-091 (03)
owns the CT 162 credit side; SV-EINV-FR-103/104/117 (e-invoicing 03)
own the event lifecycle this file consumes.

## 6. Acceptance Criteria

- **AC-001:** Given an Anexo 9 row with MONTO SUJETO = 1,000.00, then
  its PERCEPCIÓN 1% column reads **10.00**; given an Anexo 12 row with
  MONTO SUJETO = 2,000.00, then its retention column reads **260.00**;
  given an Anexo 6 row with MONTO SUJETO = 500.00 whose MONTO ANTICIPO
  2% cell reads 9.00, then the export surfaces a validation
  inconsistency on that row before any file is written (FR-108).
- **AC-002:** Given an Anexo 4 tipo-01 row (consumer-final factura) for
  a 113.00 gross operation with 13.00 IVA, then H reads **100.00** and
  I reads **13.00** (sin-IVA detail convention) (FR-097).
- **AC-003:** Given a natural-person retention agent on an Anexo 7 row
  in period 05/2025, then the row carries either the NIT AGENTE or the
  DUI — never both; given a row carrying both (or neither), then it is
  rejected by the XOR gate; given the same agent in a pre-2022 period,
  then the NIT/NRC is mandatory (FR-103).
- **AC-004:** Given a sealed invalidation event for an FE emitted
  10/2025, when the 11/2025 §XIX annex is built, then one D-code row
  appears with B=4, E=01, F=D, G=the 40-character sello, C/D/H/I = 0,
  J = the 32-character código de generación, and A = the hyphenless
  28-character número de control (canonical slot — NOT the manual's
  inverted instruction); and given a candidate J value of 36
  characters, then the row is rejected/flagged per the SOQ-10 ruling
  (32 operative) (FR-116, FR-118, FR-121).
- **AC-005:** Given validated uploads of annexes 1, 2, 9, 10, 11 and 12
  for a period, then the *Documentos Emitidos* view lists exactly the
  documents of those annexes recomputed from their rows, no upload
  surface exists for emitidos, and editing an annex-10 row changes the
  emitidos view accordingly on recompute (FR-120).
- **AC-006:** Given effected-side ledger rows of one CCF perception
  (1,000.00/10.00) and one CRE retention (500.00/5.00), then the F-930
  §B summary reads class 1 (CCF): 1 document, 1,000.00, 10.00 and
  class 3 (CR): 1 document, 500.00, 5.00, and the §C lines carry the
  counterparties' NIT/name with their calidad/modalidad classifiers
  (FR-111, FR-112, FR-113).
- **AC-007:** Given annex 6/7/8 totals 20.00/15.00/5.00 and annex
  9/10/11/12 totals 30.00/10.00/8.00/26.00, then casillas 161/162/163
  read 20.00/15.00/5.00 (entering 166 per 01 FR-016) and 169/170/171/
  172 read 30.00/10.00/8.00/26.00 (entering 187 = 74.00 per 01
  FR-022/023), with every MONTO SUJETO column absent from the casilla
  feeds and no manual casilla edit anywhere (FR-110, FR-123).
- **AC-008:** Given a §XIX row for a DTE dated 08/2022, then A carries
  the *código de generación* hyphenless (32); given the DISCRIMINATING
  boundary case — a DTE dated 10/2022 — then A carries the *código de
  generación* hyphenless (32) per the canonical pre-Nov-2022 rule, NOT
  the *número de control* the manual's inverted instruction would
  require; given a DTE dated 12/2022, then A carries the *número de
  control* hyphenless (28) — the annexes-1-12 Nov-2022 convention
  applied throughout, the inverted September/October wording never
  encoded (FR-118).
- **AC-009:** Given an anulados row carrying −100.00, then it is
  accepted (CT 111 exception — the only annex admitting negatives);
  given an Anexo 10 row carrying −100.00, then it is rejected; given an
  anulado document dated N−3, then its §XIX row is accepted; and given
  an anulado dated N−4 or a future month, then its §XIX row is
  rejected (FR-109, FR-119).
- **AC-010:** Given a *declaración modificatoria* (amended return) of
  period 04/2026 whose prior same-period declaration carried annexes
  4/6-12, then those annexes are prefilled from the prior declaration
  per 01 FR-040 ("anexos 3 al 12"); given a re-upload of annex 10, then
  the carried rows are fully replaced, not merged (01 FR-041); the §XIX
  carryover behavior is not asserted (OQ-004) (FR-122).
- **AC-011:** Given one effected-side retention row edited to correct
  its subject amount, then both the Anexo 10 export for the period and
  the F-930 §B/§C lines reflect the corrected value after recompute —
  one ledger, no second entry surface (FR-111).
- **AC-012:** Given a voided retention document (an anulled CRE), then
  it produces NO annex 10 row and one §XIX A-code row instead (routing
  per FR-109/FR-116); given a lost physical factura, then its §XIX row
  carries F=X with the pre-printed C/D and H/I ranges and J empty
  (FR-116).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | F-930 codificación values: the form's coding appendix (CALIDAD EN LA QUE ACTÚA agent/perceiver categories, Modalidad, Código) is not in the corpus — only its existence is printed (EVID-189). FR-113 consumes calidad/modalidad as configuration data. Acquire the appendix (or a newer form print) and seed the code lists. | no | Takumi S3 (sources registry) | open |
| OQ-002 | Anexo 4 amount inferences: (a) casilla 108 basis — the manual prints the 108 auto-total but not which columns total into it: H only (sin-IVA base, consistent with FR-097) vs H+I; (b) the H/I base-vs-tax split on CCF/NC/ND rows (the sin-IVA rule is printed for tipo-01 rows only). Encoded: H-only basis and the same split on all tipos (family convention; FR-123 wires 108 = H). Likewise the CL-side débito wiring (casillas 98/99/144 from annex 4) stays recorded-unwired per `01_f07-declaration.md` OQ-005 — not asserted here. Confirm against MH auto-totalization behavior. | no | Takumi S3 | open |
| OQ-003 | §XIX printed-model gaps: manual §XIX prints the A-J model with (a) NO trailing annex-number column, while the generic rule (SV-FREP-FR-034 / manual §XVI) requires the annex number on the last column of every line; and (b) NO date column, while the §II DD/MM/AAAA discipline and the CT 111 three-prior-period window (FR-119) presuppose one — FR-115 stores the document date as the window-validation field without printing it. Encoded: A-J as printed, no annex-number/date column emitted for the §XIX file. Confirm against a live MH upload or plantilla validation (the plantilla sheets 1-12 do not include the anulados section). | no | Takumi S3 | open |
| OQ-004 | §XIX modificatoria carryover: manual §XVII lists the carryover for "anexos 3 al 12" only — the anulados/emitidos section's fate in amended returns is unprinted (emitidos auto-recompute from carried annexes; anulados carryover or re-upload unknown). FR-122 does not assert it. Confirm against MH system behavior. | no | Takumi S3 | open |
| OQ-005 | Annexes 6-12 column letters and lengths: the manual prints ordered column lists without letters (letters here assigned by printed position, per-annex TIPO positions per the plantilla), and without lengths — NIT/NRC 14, DUI 9, sello 40, código 32, número de control 28 follow the family conventions; amount/date columns the §II discipline (01 §3.2). Confirm letters/positions against the plantilla sheets 6-12 before certifying byte-exact exports. | no | Takumi S3 | open |
| OQ-006 | F-930 v3 vintage: 63_ is a 2017-era print still listed by MH as of 2026-08-18 (EVID-189 doubt; 61-64 addendum OQ-2's F-930 half — the F-915 half belongs to `07_codes-and-informs.md`). FR-114 seeds the layout per form_version. Re-verify if a calendar year rolls or a v4 appears. | no | Takumi S3 | open |
| OQ-007 | F-930 §B class↔tipo mapping: the seven summary classes are label-matched to the annex tipo catalog (1↔03, 2↔09, 3↔07, 4↔06, 5↔05, 6↔01, 7↔14) — the form prints names, not codes; grouping of e.g. FSE (14) rows that never appear in annexes 9-12 as tipos is by ledger doc_class. Confirm against the codificación (with OQ-001). | no | Takumi S3 | open |
