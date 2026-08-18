# SV — Fiscal reporting — F-07 sales annexes 1-2: row models, DTE identifier mapping & Renta pair

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for the two F-07 sales annexes
of the *Manual de Usuario para Carga de Archivo de los Anexos* (annex upload
user manual), F-07 V14, ENERO 2025: **Anexo 1 Ventas a Contribuyentes**
(sales to taxpayers — the B2B annex: one row per EMITTED document, document
types CCF/NC/ND only, classes 1/2/4, with the DUI-vs-NIT exclusive-or gate
for natural-person clients and, since Enero-2025, the cross-tax ISR
classification pair R *Tipo de Operación* / S *Tipo de Ingreso* that feeds
the F-14/F-910/F-11 rentas family) and **Anexo 2 Ventas a Consumidor Final**
(sales to final consumers — the B2C annex: AGGREGATED rows, physical
documents in authorized pre-printed DEL/AL ranges with cash-register numbers
for tiquetes, DTE documents grouped BY DAY with the first/last *código de
generación* as range endpoints, gravadas locales detailed IVA-INCLUSIVE,
export buckets split inside/outside the Central American region plus service
exports and zonas francas/DPA at zero rate, and the U/V Renta pair under the
same Enero-2025 gate as R/S). This file also owns THE canonical
document-identifier mapping FR for the whole F-07 annex family — the column
semantics per document class (physical *resolución/serie/preimpreso* ranges;
*formulario único* control interno; the DTE mapping of sello de
recepción/número de control/código de generación with the November-2022
cutover as dated data) — which files 03/04 reference instead of restating.

It does **not** cover: the declaration casilla engine and the generic annex
upload format/validations/modificatoria flow (`01_f07-declaration.md`
§3.1/§3.2 — SV-FREP-FR-001..041; the semicolon-CSV, Text-cell, two-decimal,
negative-gate, date/period, annex-number and clean-replace rules live THERE
and are inherited here by reference); the purchase annexes 3/5 with the
post-*entero* (after-remittance) credit re-entry
(`03_f07-annexes-purchases.md` §3 — which references this file's
identifier-mapping FR); the retention/perception annexes 4/6-12, the
anulados/extraviados annex and the invalidation-event feed
(`04_f07-annexes-retentions-events.md` §3 — voided documents are ROUTED
there from this file's exclusion rules); the fuel and dated-regime annexes
13-17 (`05_f07-annexes-special.md` §3); the F-14 declaration family and
income-code catalog (`06_f14-declaration.md`, `07_codes-and-informs.md`);
the filing calendar (`08_filing-calendar.md` — SOQ-08); the IVA computation
proper (13% rate, taxable base, deductibility — future IVA taxation file;
the débito columns here consume its output, cf. 01 §7 OQ-004); and the ISR
retention matrix (SV-TAX-FR-102..131 in `taxation/04_isr-withholding.md` —
a different tax; the R/S pair only CLASSIFIES rows for the ISR side). Task
1's casilla FRs consume this file's annex totals; Task 4's anulados annex
references this file's row models.

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and upload manuals ARE the
primary authority for declaration mechanics — 34_ (Manual de Usuario para
Carga de Archivo de los Anexos, F-07 V14, ENERO 2025) is the governing
source for both annex structures; the plantilla workbook 36_ (sheets "1"
and "2") is the structural conformance reference. Legal anchors printed in
the manual (CT Art. 111 for the anulados negative exception) are cited as
printed. The IVA-inclusive convention's legal root (Ley IVA Art. 57 via
ruling R1) is cited for the cross-file consistency requirement with the
e-invoicing wave. Manual pages are printed pages (printed page N = PDF page
N+2).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-07 v14 §III, Anexo 1 "Ventas a Contribuyentes", tabla de columnas: "A FECHA DE EMISIÓN DEL DOCUMENTO 10 / B CLASE DE DOCUMENTO 1 / C TIPO DE DOCUMENTO 2 / D NÚMERO DE RESOLUCIÓN 100 / E NÚMERO DE SERIE DE DOCUMENTO 100 / F NÚMERO DE DOCUMENTO 100 / G NÚMERO DE CONTROL INTERNO 100 / H NIT O NRC DEL CLIENTE 14 / I NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN SIN LÍMITE / J VENTAS EXENTAS 10 / K VENTAS NO SUJETAS 10 / L VENTAS GRAVADAS LOCALES 10 / M DÉBITO FISCAL 10 / N VENTAS A CUENTA DE TERCEROS NO DOMICILIADOS 10 / O DÉBITO FISCAL POR VENTA A CUENTA DE TERCEROS 10 / P TOTAL VENTAS 10 / Q DUI DEL CLIENTE 9 / R TIPO DE OPERACIÓN (Renta) 10 / S TIPO DE INGRESO (Renta) 10 / T NÚMERO DE ANEXO 1"; CLASE DE DOCUMENTO: "1 IMPRESO POR IMPRENTA O TIQUETES / 2 FORMULARIO ÚNICO / 4 DOCUMENTO TRIBUTARIO ELECTRÓNICO DTE"; TIPO DE DOCUMENTO: "03 COMPROBANTE DE CRÉDITO FISCAL / 05 NOTA DE CRÉDITO / 06 NOTA DE DÉBITO" | F-07 v14 upload manual §III, Anexo 1 column table A-T with printed field lengths (date 10, clase 1, tipo 2, identifier columns 100, NIT/NRC 14, DUI 9, amounts 10, unlimited name, annex number 1), the three document classes (printer-issued or tiquetes / formulario único / DTE) and the three admitted document types (CCF / credit note / debit note) | `sv/sources/34_F07_v14_manual.pdf` | §III pp.1-6 (EVID-174; plantilla sheet "1" in `sv/sources/36_F07_v14_plantilla.xls`) |
| LB-002 | Manual F-07 v14 §III, Anexo 1, mapeo de identificadores DTE: D (Resolución) "deberá colocar el número de control del DTE sin guiones. Cuando se ingresen documentos que antecedan al periodo noviembre 2022 debe ingresar Código de Generación del DTE sin guiones"; E (Serie) "debe ingresar el sello de recepción del DTE"; F (Número) "debe ingresar el código de generación del DTE sin guiones. Cuando se ingresen documentos que antecedan al periodo noviembre 2022 debe ingresar el número de control del DTE sin guiones"; G (Control interno) "Para los documentos Tributarios Electrónicos debe dejar en blanco" | F-07 v14 upload manual §III DTE identifier mapping: Resolución slot = número de control hyphenless (pre-Nov-2022: código de generación hyphenless); Serie slot = sello de recepción; Número slot = código de generación hyphenless (pre-Nov-2022: número de control hyphenless); control interno blank for DTEs | `sv/sources/34_F07_v14_manual.pdf` | §III pp.1-6 (EVID-174; the Anexo 4 twin mapping §VI pp.19-21 prints the 40/32/28 character lengths, EVID-177) |
| LB-003 | Manual F-07 v14 §III, Anexo 1, columnas R/S: "Las nuevas columnas 'R, S' aplica a partir del periodo de Enero 2025; para periodos anteriores al referido deberá colocar '0'"; códigos R TIPO DE OPERACIÓN: "1 Gravada / 2 No Gravada o Exento / 3 Excluido o no Constituye Renta / 4 Mixta / 12 Ingresos que ya fueron sujetos de retención informados en el F14 y consolidados en F910 / 13 Sujetos pasivos excluidos (art. 6 LISR)"; códigos S TIPO DE INGRESO: "1 Profesiones, Artes y Oficios / 2 Actividades de Servicios / 3 Actividades Comerciales / 4 Actividades Industriales / 5 Actividades Agropecuarias / 6 Utilidades y Dividendos / 7 Exportaciones de bienes / 8 Servicios Realizados en el Exterior y Utilizados en El Salvador / 9 Exportaciones de servicios / 10 Otras Rentas Gravables / 12, 13 (as R)" | F-07 v14 upload manual §III Renta pair: R/S apply from the Enero-2025 period, "0" for earlier periods; R operation-type codes 1/2/3/4/12/13 verbatim (12 = income already subject to retention, reported in F-14 and consolidated in F-910; 13 = sujetos pasivos excluidos per Art. 6 LISR); S income-type codes 1-10 with 12/13 as in R | `sv/sources/34_F07_v14_manual.pdf` | §III pp.1-6 (EVID-174) |
| LB-004 | Manual F-07 v14 §III, Anexo 1: regla DUI vs NIT (glosa EVID-174): desde enero 2022 los clientes personas naturales pueden consignar DUI (entonces NIT/NRC vacío) o NIT/NRC (entonces DUI vacío); antes de 2022 el NIT/NRC es obligatorio; alcance: "Los datos cargados deben corresponder a los documentos emitidos (sin incluir anulados y/o extraviados)" | F-07 v14 upload manual §III: from Enero-2022 natural-person clients state either DUI (Q, 9 — NIT/NRC empty) or NIT/NRC (H, 14 — DUI empty), never both; before Enero-2022 the NIT/NRC is mandatory; loaded data corresponds to EMITTED documents only, excluding voided and lost documents | `sv/sources/34_F07_v14_manual.pdf` | §III pp.1-6 (EVID-174) |
| LB-005 | Manual F-07 v14 §IV, Anexo 2 "Ventas a Consumidor Final", tabla de columnas A-W: "A FECHA EMISIÓN / B CLASE / C TIPO: 01 FACTURA DE CONSUMIDOR FINAL / 02 FACTURA DE VENTA SIMPLIFICADA / 10 TIQUETES DE MÁQUINAS REGISTRADORA / 11 FACTURA DE EXPORTACION"; bloque de identificadores D-J incl. "J N° DE MAQUINA REGISTRADORA 14"; valores: "K VENTAS EXENTAS / L VENTAS INTERNAS EXENTAS NO SUJETAS A PROPORCIONALIDAD / M VENTAS NO SUJETAS / N VENTAS GRAVADAS LOCALES / O EXPORTACIONES DENTRO DEL ÁREA CENTROAMERICANA / P EXPORTACIONES FUERA DEL ÁREA CENTROAMERICANA / Q EXPORTACIONES DE SERVICIOS / R VENTAS A ZONAS FRANCAS Y DPA (TASA CERO) / S VENTAS A CUENTA DE TERCEROS NO DOMICILIADOS / T TOTAL"; par U/V (Renta); W número de anexo 2; DTE: "Para el caso de Documento Tributario Electrónico deberá colocar: N/A (Esto debido a que los documentos se agruparán por día)" (D y E); F/G/H/I: "Para el caso de los DTE se deberá agrupar por día los documentos emitidos y deberá colocar el Código de Generación del primer DTE emitido" / "del último DTE emitido" | F-07 v14 upload manual §IV, Anexo 2 column table A-W: date; clase; type (consumer-final invoice / simplified sales invoice / cash-register tiquetes / export invoice); identifier block D-J incl. the 14-char cash-register number J; value buckets K exentas, L internal exempt not subject to proportionality, M no sujetas, N gravadas locales, O/P goods exports inside/outside the Central American region, Q service exports, R zonas francas and DPA at zero rate, S sales for the account of non-domiciled third parties, T total; U/V Renta pair; W annex number 2; DTE rows: N/A in the resolución/serie columns because documents are grouped by day, with the código de generación of the first and last DTE emitted as range endpoints | `sv/sources/34_F07_v14_manual.pdf` | §IV pp.7-11 (EVID-175; plantilla sheet "2" in `sv/sources/36_F07_v14_plantilla.xls`) |
| LB-006 | Manual F-07 v14 §IV, Anexo 2: N (VENTAS GRAVADAS LOCALES) "Deberá detallarlas con IVA incluido"; Área Centroamericana = "Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica" | F-07 v14 upload manual §IV: Anexo 2 gravadas locales are detailed IVA-INCLUSIVE; the Central American region for the export split = Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica | `sv/sources/34_F07_v14_manual.pdf` | §IV pp.7-11 (EVID-175) |
| LB-007 | Manual F-07 v14 §IV, Anexo 2: cruce Aduanas: "los valores declarados ... en concepto de Exportaciones de Bienes Dentro y Fuera del Área Centroamericana, se compararán con los valores reportados por la Dirección General de Aduanas"; regla de negativos (glosa EVID-175): valores negativos únicamente para documentos anulados, de acuerdo al artículo 111 del Código Tributario; par U/V (glosa EVID-175): aplica a partir de Enero 2025, antes "0" | F-07 v14 upload manual §IV: goods-export values inside and outside the CA region are compared by MH against the values reported by the Dirección General de Aduanas (customs); negative values only for voided documents per CT Art. 111; U/V apply from Enero-2025, "0" before | `sv/sources/34_F07_v14_manual.pdf` | §IV pp.7-11 (EVID-175; CT 111 anchor per EVID-173 §IV) |
| LB-008 | Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios (Ley IVA), Art. 57 | IVA Law Art. 57: the IVA must appear in the CCF separate from the price — the legal root of ruling R1 (factura prices include IVA, CCF prices exclude it), mirrored on the sales annexes: Anexo 1 gravadas net with a separate débito column, Anexo 2 gravadas IVA-inclusive | `sv/sources/01_Ley_IVA.pdf` | Art. 57 p.27 (EVID-048 via `sv/.extractions/01_Ley_IVA.evidence.md`; R1; cross-file consistency with SV-EINV-FR-019/024) |

## 3. Functional Requirements

### 3.1 Canonical document-identifier mapping (shared across the F-07 annex family)

- **SV-FREP-FR-042:** The system shall implement ONE canonical
  document-identifier slot model for every F-07 annex row, keyed by CLASE
  DE DOCUMENTO (document class): **clase 1** (*impreso por imprenta o
  tiquetes*, printer-issued or cash-register documents) fills the
  RESOLUCIÓN slot with the MH authorization resolution number of the
  printed range, the SERIE slot with the document series, and the NÚMERO
  slot(s) with the pre-printed document number — one row per document, or
  a DEL/AL (*desde/hasta*, from/to) range on annexes whose row model
  aggregates (Anexo 2, FR-055); **clase 2** (*formulario único*, single
  form) routes the emitter's internal control number to the CONTROL
  INTERNO slot; **clase 4** (*Documento Tributario Electrónico*, DTE)
  fills the slots per FR-043 only. This slot model is CANONICAL: files
  03/04/05 (`03_f07-annexes-purchases.md`,
  `04_f07-annexes-retentions-events.md`, `05_f07-annexes-special.md`)
  reference SV-FREP-FR-042/043 and shall not restate the mapping.
  (LB-001; LB-002; EVID-174)
- **SV-FREP-FR-043:** THE shared DTE-identifier-mapping requirement: for
  clase 4 rows the system shall fill the identifier slots as follows —
  SERIE = the *sello de recepción* (MH reception seal) of the DTE, 40
  characters; RESOLUCIÓN = the *número de control* (control number) of
  the DTE without hyphens, 28 characters; NÚMERO = the *código de
  generación* (generation code) of the DTE without hyphens, 32
  characters; CONTROL INTERNO = blank ("debe dejar en blanco"); with the
  November-2022 cutover as dated data (D12): for documents preceding the
  Noviembre-2022 period the RESOLUCIÓN slot carries the *código de
  generación* without hyphens (32) and the NÚMERO slot carries the
  *número de control* without hyphens (28) — the two slots swap sources
  across the cutover, the SERIE slot does not. (LB-002; EVID-174;
  EVID-177 §VI twin mapping for the 40/32/28 lengths)
- **SV-FREP-FR-044:** The system shall source every clase-4 identifier
  value from the archived sealed DTE record — *sello de recepción* only
  for sealed documents (cross-ref `e-invoicing/01_document-types.md`
  SV-EINV-FR-003 *código de generación* format, SV-EINV-FR-004 *número de
  control* format, and `e-invoicing/03_events.md` SV-EINV-FR-092 sello
  archival) — and shall validate the hyphenless emission lengths
  (40/32/28) on every exported row, rejecting a row whose identifier
  values do not match the stored DTE identifiers of its source document
  (documents corrected under the 24-hour same-code rule keep their
  *código de generación*, `e-invoicing/02_transmission.md` FR-078).
  (LB-002; EVID-174; EVID-177)

### 3.2 Anexo 1 — Ventas a Contribuyentes (per-document B2B rows)

- **SV-FREP-FR-045:** The system shall build Anexo 1 (*Ventas a
  Contribuyentes*, sales to taxpayers) with ONE ROW PER EMITTED DOCUMENT,
  admitting only TIPO DE DOCUMENTO 03 (*Comprobante de Crédito Fiscal*,
  tax-credit document), 05 (*Nota de Crédito*, credit note) and 06 (*Nota
  de Débito*, debit note), for CLASE 1, 2 or 4; voided and lost documents
  (*anulados y/o extraviados*) are EXCLUDED from this annex ("Los datos
  cargados deben corresponder a los documentos emitidos (sin incluir
  anulados y/o extraviados)") and route to the anulados annex owned by
  `04_f07-annexes-retentions-events.md` §3. (LB-001; LB-004; EVID-174)
- **SV-FREP-FR-046:** The system shall emit every Anexo 1 row with the
  verbatim column model A-T of manual §III — A FECHA DE EMISIÓN DEL
  DOCUMENTO (10) · B CLASE DE DOCUMENTO (1) · C TIPO DE DOCUMENTO (2) ·
  D NÚMERO DE RESOLUCIÓN (100) · E NÚMERO DE SERIE DE DOCUMENTO (100) ·
  F NÚMERO DE DOCUMENTO (100) · G NÚMERO DE CONTROL INTERNO (100) ·
  H NIT O NRC DEL CLIENTE (14) · I NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN
  (sin límite) · J VENTAS EXENTAS (10) · K VENTAS NO SUJETAS (10) ·
  L VENTAS GRAVADAS LOCALES (10) · M DÉBITO FISCAL (10) · N VENTAS A
  CUENTA DE TERCEROS NO DOMICILIADOS (10) · O DÉBITO FISCAL POR VENTA A
  CUENTA DE TERCEROS (10) · P TOTAL VENTAS (10) · Q DUI DEL CLIENTE (9) ·
  R TIPO DE OPERACIÓN (Renta) · S TIPO DE INGRESO (Renta) · T NÚMERO DE
  ANEXO = 1 — in exactly this order, conforming to plantilla sheet "1".
  (LB-001; EVID-174)
- **SV-FREP-FR-047:** The system shall fill the client-identification
  columns from the customer master data of the row's source document:
  H = the client's NIT or NRC (14), I = the client's name/trade name with
  no length limit, Q = the client's DUI (9) — subject to the FR-050
  exclusive-or; the identifier columns D-G follow the canonical slot
  model of FR-042/043. (LB-001; LB-002; EVID-174)
- **SV-FREP-FR-048:** The system shall fill the Anexo 1 value buckets per
  column semantics: J *ventas exentas* (exempt sales), K *ventas no
  sujetas* (non-subject sales), L *ventas gravadas locales* (locally
  taxed sales) NET of IVA with its M *débito fiscal* (fiscal debit)
  companion in a separate column — the CCF net convention of ruling R1 /
  SV-EINV-FR-024 (L carries the tax base; M carries the IVA computed on
  it by the IVA engine; the manual prints no explicit wording for L —
  OQ-002), N *ventas a cuenta de terceros no domiciliados* (sales for the
  account of non-domiciled third parties) with its O débito companion,
  and P *total ventas* = J + K + L + N (the row's sale-value columns; the
  débito companions M/O are tax columns, not sale values).
  (LB-001; LB-008; EVID-174)
- **SV-FREP-FR-049:** The system shall emit credit and debit notes
  (tipos 05/06) as rows of their own with POSITIVE magnitudes classified
  into the same value buckets as the documents they adjust — never as
  negatives (negative gate inherited from SV-FREP-FR-031) — and the
  sale-reduction netting happens at the declaration level: NC totals feed
  casillas 97/143 (*devoluciones/rebajas/descuentos sobre ventas*,
  returns/rebajas/discounts over sales) per
  `01_f07-declaration.md` FR-004/FR-006, which consume this annex's
  totals. (LB-001; EVID-174; cross-ref SV-FREP-FR-004/006)
- **SV-FREP-FR-050:** The system shall enforce the DUI-vs-NIT
  exclusive-or on Anexo 1 client identification with its period gate:
  from the Enero-2022 period, natural-person clients state EITHER the DUI
  (Q filled, H empty) OR the NIT/NRC (H filled, Q empty) — a row carrying
  both, or neither, is rejected; before Enero-2022 the NIT/NRC (H) is
  mandatory and Q stays empty; juridical persons always carry the NIT/NRC
  and never a DUI. (LB-004; EVID-174)
- **SV-FREP-FR-051:** The system shall apply the R/S Renta-pair period
  gate: columns R (*Tipo de Operación*, operation type) and S (*Tipo de
  Ingreso*, income type) apply from the Enero-2025 period; for periods
  before Enero-2025 both columns are emitted as "0" ("para periodos
  anteriores al referido deberá colocar '0'"); codes are at most TWO
  characters (the column table's printed "10" is the manual's own typo
  against its "máximo dos caracteres" text — OQ-003). (LB-003; EVID-174)
- **SV-FREP-FR-052:** The system shall classify every post-gate Anexo 1
  row with the verbatim R/S code lists — R TIPO DE OPERACIÓN (Renta):
  1 Gravada · 2 No Gravada o Exento · 3 Excluido o no Constituye Renta ·
  4 Mixta · 12 Ingresos que ya fueron sujetos de retención informados en
  el F14 y consolidados en F910 (income already subject to retention,
  reported in F-14 and consolidated in F-910 — excluded from double
  counting) · 13 Sujetos pasivos excluidos (art. 6 LISR) (excluded
  subjects per Art. 6 of the ISR Law); S TIPO DE INGRESO (Renta): 1
  Profesiones, Artes y Oficios · 2 Actividades de Servicios · 3
  Actividades Comerciales · 4 Actividades Industriales · 5 Actividades
  Agropecuarias · 6 Utilidades y Dividendos · 7 Exportaciones de bienes ·
  8 Servicios Realizados en el Exterior y Utilizados en El Salvador · 9
  Exportaciones de servicios · 10 Otras Rentas Gravables · 12, 13 as in R
  — stored on the row as the ISR-side classification consumed by the
  F-14/F-910/F-11 family (`06_f14-declaration.md`,
  `07_codes-and-informs.md`; cross-tax interface only: no ISR computation
  happens here). (LB-003; EVID-174)

### 3.3 Anexo 2 — Ventas a Consumidor Final (aggregated B2C rows)

- **SV-FREP-FR-053:** The system shall build Anexo 2 (*Ventas a
  Consumidor Final*, sales to final consumers) as an AGGREGATED annex —
  never one row per DTE — with two row modes: physical-document rows
  (clase 1/2) aggregated per authorized range (FR-055) and DTE rows
  (clase 4) aggregated per DAY (FR-056), admitting only TIPO DE DOCUMENTO
  01 (*Factura de Consumidor Final*, consumer-final invoice), 02
  (*Factura de Venta Simplificada*, simplified sales invoice), 10
  (*Tiquetes de Máquinas Registradora*, cash-register tickets) and 11
  (*Factura de Exportación*, export invoice). (LB-005; EVID-175)
- **SV-FREP-FR-054:** The system shall emit every Anexo 2 row with the
  verbatim column model A-W of manual §IV — A FECHA EMISIÓN · B CLASE ·
  C TIPO · D-J identifier block (D resolución · E serie · F/G número
  DEL/AL · H/I control interno DEL/AL · J N° DE MÁQUINA REGISTRADORA 14)
  · K VENTAS EXENTAS · L VENTAS INTERNAS EXENTAS NO SUJETAS A
  PROPORCIONALIDAD · M VENTAS NO SUJETAS · N VENTAS GRAVADAS LOCALES ·
  O EXPORTACIONES DENTRO DEL ÁREA CENTROAMERICANA · P EXPORTACIONES
  FUERA DEL ÁREA CENTROAMERICANA · Q EXPORTACIONES DE SERVICIOS ·
  R VENTAS A ZONAS FRANCAS Y DPA (TASA CERO) · S VENTAS A CUENTA DE
  TERCEROS NO DOMICILIADOS · T TOTAL · U/V Renta pair · W = 2 — in
  exactly this order, conforming to plantilla sheet "2". (LB-005;
  EVID-175)
- **SV-FREP-FR-055:** The system shall build physical-document rows
  (clase 1/2) per authorized range: D = the MH authorization resolution
  of the printed range, E = the series, F/G = the document-number range
  DEL/AL (F = G for a single document — the identity rule), H/I = the
  internal-control-number range DEL/AL where the emitter keeps internal
  control (H = I identity; formulario único emitters route their control
  number here per FR-042 clase 2), and for tipo 10 tiquetes J = the
  cash-register number (14) identifying the issuing machine; every value
  bucket of the row aggregates the documents of the range.
  (LB-005; EVID-175)
- **SV-FREP-FR-056:** The system shall build clase-4 DTE rows grouped BY
  DAY: all DTEs of the same tipo emitted on the same date form ONE row
  whose A = that date, D and E = the literal text "N/A" ("Para el caso de
  Documento Tributario Electrónico deberá colocar: N/A (Esto debido a que
  los documentos se agruparán por día)"), F = the *código de generación*
  of the FIRST DTE emitted that day, G = the *código de generación* of
  the LAST DTE emitted that day (both hyphenless, 32), H/I = blank
  (control interno is blank for DTE per FR-043), J = blank, and whose
  value buckets aggregate all documents of the day-group; the required
  ordering of the daily groups in the file is not printed by the manual
  (OQ-001). (LB-005; EVID-175)
- **SV-FREP-FR-057:** The system shall admit tipos 02 and 10 on Anexo 2
  as VALID codes for the physical regimes only, carrying the regime note:
  *tiquetes* are banned for DTE emitters since 01-January-2025 and the
  FVS (*factura de venta simplificada*) survives only as a physical
  document for authorized emitters reported via the Evento de Operaciones
  Especiales (ruling R12; cross-ref
  `e-invoicing/03_events.md` SV-EINV-FR-129) — post-2025 DTE
  emitters generate no tipo-02/10 rows, non-DTE emitters keep them; the
  codes stay in the catalog for historical compatibility.
  (LB-005; EVID-175 doubt note)
- **SV-FREP-FR-058:** The system shall fill the Anexo 2 value buckets per
  column semantics: K *ventas exentas*, L *ventas internas exentas no
  sujetas a proporcionalidad* (internal exempt sales not subject to the
  proportionality proration — the casilla-92 track), M *ventas no
  sujetas*, N *ventas gravadas locales*, O/P goods exports inside/outside
  the CA region, Q service exports, R zonas francas/DPA zero-rate sales,
  S sales for the account of non-domiciled third parties, and T TOTAL =
  K + L + M + N + O + P + Q + R + S (Anexo 2 has no débito columns: its
  gravadas are IVA-inclusive per FR-059 and its exports are zero-rated).
  (LB-005; EVID-175)
- **SV-FREP-FR-059:** The system shall detail Anexo 2 gravadas locales
  (N) WITH IVA INCLUDED ("Deberá detallarlas con IVA incluido") — the
  consumer-invoice convention of ruling R1 / SV-EINV-FR-019 — so the
  row-builder operates a CONVENTION SWITCH against Anexo 1: Anexo 2 N
  aggregates tax-included totals of consumer documents, while Anexo 1 L
  carries the net base with its débito in M (FR-048); both annexes must
  agree with the e-invoicing tax configuration (price_include=True for FE
  taxes, False for CCFE — SV-EINV-FR-019/024 §5 rows). (LB-006; LB-008;
  EVID-175)
- **SV-FREP-FR-060:** The system shall route export and special-regime
  B2C sales by destination: O for goods exports to the *área
  centroamericana* = Guatemala, Honduras, El Salvador, Nicaragua, Costa
  Rica; P for goods exports outside it; Q for service exports; R for
  sales to *zonas francas* (free zones) and *depósitos de
  perfeccionamiento activo* (active perfection deposits, DPA) at zero
  rate; the destination country of the source document decides the O/P
  split. (LB-006; EVID-175)
- **SV-FREP-FR-061:** The system shall NEVER emit a negative amount on
  Anexo 2 rows: voided consumer documents carry their negative magnitudes
  ONLY in the anulados annex per CT Art. 111 (negative gate inherited
  from SV-FREP-FR-031; routing to
  `04_f07-annexes-retentions-events.md` §3 per FR-045's exclusion
  principle). (LB-007; EVID-175; EVID-173)
- **SV-FREP-FR-062:** The system shall apply the U/V Renta pair on Anexo
  2 under the SAME gate and code lists as Anexo 1's R/S: from the
  Enero-2025 period the U (*Tipo de Operación*) and V (*Tipo de Ingreso*)
  columns carry the FR-052 code lists verbatim; for earlier periods both
  are emitted as "0" (the manual §IV prints the gate but no separate U/V
  code lists — same-lists assumption, OQ-004). (LB-007; LB-005;
  EVID-175)
- **SV-FREP-FR-063:** The system shall surface Aduanas cross-check
  AWARENESS flags — informational only, no computation: because "los
  valores declarados ... en concepto de Exportaciones de Bienes Dentro y
  Fuera del Área Centroamericana, se compararán con los valores
  reportados por la Dirección General de Aduanas", the system shall flag
  (i) export rows whose values rest on documents without DUA/levante
  linkage and (ii) period totals of O/P whose DUA-registration-date basis
  differs from the emission-date basis of the annex rows; the import-side
  counterpart belongs to `03_f07-annexes-purchases.md` §3. (LB-007;
  EVID-175; EV34 OQ-5)

### 3.4 Builder interfaces

- **SV-FREP-FR-064:** The system shall export and validate the Anexo 1
  and Anexo 2 files under the generic upload-format engine of
  `01_f07-declaration.md` §3.2 — SV-FREP-FR-028..041 (semicolon CSV, Text
  cells, ≤25-char filename, two-decimal truncation, 0.00 nils,
  DD/MM/AAAA period consistency with the CURRENT-period-only window for
  sales annexes, last-column annex number = 1 / 2, clean-replace
  semantics, modificatoria forced re-upload of annexes 1-2) — restated
  here only as the interface: no format rule is duplicated in this file.
  (LB-001; LB-005; EVID-173; EVID-174; EVID-175; cross-ref
  SV-FREP-FR-028..041)
- **SV-FREP-FR-065:** The system shall build both annexes' rows from
  POSTED sale-side documents (customer invoices, credit notes, debit
  notes — Odoo `account.move`), routing by receiver fiscal category and
  document type: customers with NIT/NRC invoiced through CCF/NC/ND
  documents feed Anexo 1 rows (per-document mode); final-consumer
  documents (factura de consumidor final, simplified invoices, tiquetes,
  export invoices) feed Anexo 2 rows (per-range or per-day aggregation
  mode per FR-055/056); a document never feeds both annexes.
  (LB-001; LB-005; EVID-174; EVID-175)
- **SV-FREP-FR-066:** The system shall feed the declaration casillas
  from the annex totals per the §4 wiring table (label-matched columns →
  casillas of `01_f07-declaration.md` FR-004/FR-006/FR-038), with the
  third-party channel routed by document family: Anexo 1 N/O (CCF-family
  documents) → casillas 88/141, Anexo 2 S (factura-family documents) →
  casilla 89 (débito 142 computed by the IVA engine — Anexo 2 has no
  débito column); no casilla is filled manually. (LB-001; LB-005;
  EVID-174; EVID-175; cross-ref SV-FREP-FR-004/006/038)

## 4. Data Model

No CSV sidecars live next to this file: the column models, code lists and
identifier mapping below are in-file §4 seed data. Layer semantics:
Odoo-side computation/bookkeeping data only (wave default `odoo`; see §5).

**Anexo 1 row model — l10n_sv.f07.annex1.row (seed structure; verbatim from
manual §III / plantilla sheet "1"):**

| Col | Header (Spanish, verbatim) | Length | Semantics | FR |
|-----|----------------------------|--------|-----------|----|
| A | FECHA DE EMISIÓN DEL DOCUMENTO | 10 | DD/MM/AAAA, current period only | FR-046, FR-064 |
| B | CLASE DE DOCUMENTO | 1 | 1 impreso por imprenta o tiquetes · 2 formulario único · 4 DTE | FR-042, FR-046 |
| C | TIPO DE DOCUMENTO | 2 | 03 CCF · 05 NC · 06 ND | FR-045, FR-046 |
| D | NÚMERO DE RESOLUCIÓN | 100 | slot per FR-042; DTE = número de control (28; pre-Nov-2022 código de generación 32) | FR-043 |
| E | NÚMERO DE SERIE DE DOCUMENTO | 100 | slot per FR-042; DTE = sello de recepción (40) | FR-043 |
| F | NÚMERO DE DOCUMENTO | 100 | slot per FR-042; DTE = código de generación (32; pre-Nov-2022 número de control 28) | FR-043 |
| G | NÚMERO DE CONTROL INTERNO | 100 | clase 2 control number; blank for DTE | FR-042, FR-043 |
| H | NIT O NRC DEL CLIENTE | 14 | client NIT/NRC; XOR with Q (Enero-2022 gate) | FR-047, FR-050 |
| I | NOMBRE, RAZÓN SOCIAL O DENOMINACIÓN | sin límite | client name | FR-047 |
| J | VENTAS EXENTAS | 10 | exempt sales → casilla 85 | FR-048, FR-066 |
| K | VENTAS NO SUJETAS | 10 | non-subject sales → casilla 86 | FR-048, FR-066 |
| L | VENTAS GRAVADAS LOCALES | 10 | taxed sales NET of IVA → casilla 95 (OQ-002) | FR-048, FR-066 |
| M | DÉBITO FISCAL | 10 | IVA debit on L → casilla 135 | FR-048, FR-066 |
| N | VENTAS A CUENTA DE TERCEROS NO DOMICILIADOS | 10 | third-party non-domiciled sales → casilla 88 | FR-048, FR-066 |
| O | DÉBITO FISCAL POR VENTA A CUENTA DE TERCEROS | 10 | IVA debit on N → casilla 141 | FR-048, FR-066 |
| P | TOTAL VENTAS | 10 | J + K + L + N | FR-048 |
| Q | DUI DEL CLIENTE | 9 | client DUI; XOR with H (Enero-2022 gate) | FR-050 |
| R | TIPO DE OPERACIÓN (Renta) | 2 (table's "10" = typo, OQ-003) | R codes; "0" pre-Enero-2025 | FR-051, FR-052 |
| S | TIPO DE INGRESO (Renta) | 2 (as R) | S codes; "0" pre-Enero-2025 | FR-051, FR-052 |
| T | NÚMERO DE ANEXO | 1 | literal 1 on every row | FR-046, FR-064 |

**Anexo 2 row model — l10n_sv.f07.annex2.row (seed structure; verbatim from
manual §IV / plantilla sheet "2"):**

| Col | Header (Spanish, verbatim) | Length | Semantics | FR |
|-----|----------------------------|--------|-----------|----|
| A | FECHA EMISIÓN | 10 | DD/MM/AAAA; DTE rows = the group's day | FR-054, FR-056 |
| B | CLASE | 1 | 1 · 2 · 4 | FR-053, FR-054 |
| C | TIPO | 2 | 01 factura de consumidor final · 02 factura de venta simplificada · 10 tiquetes de máquinas registradora · 11 factura de exportación | FR-053, FR-057 |
| D | NÚMERO DE RESOLUCIÓN | plantilla | physical: range resolution; DTE = "N/A" | FR-055, FR-056 |
| E | NÚMERO DE SERIE | plantilla | physical: series; DTE = "N/A" | FR-055, FR-056 |
| F | NÚMERO DE DOCUMENTO (DEL) | plantilla | physical: range start; DTE = first código de generación (32) | FR-055, FR-056 |
| G | NÚMERO DE DOCUMENTO (AL) | plantilla | physical: range end (identity F = G single doc); DTE = last código de generación (32) | FR-055, FR-056 |
| H | NÚMERO DE CONTROL INTERNO (DEL) | plantilla | physical: internal-control range start; DTE = blank | FR-055, FR-056 |
| I | NÚMERO DE CONTROL INTERNO (AL) | plantilla | physical: internal-control range end (identity H = I); DTE = blank | FR-055, FR-056 |
| J | N° DE MÁQUINA REGISTRADORA | 14 | cash-register number (tipo 10) | FR-055 |
| K | VENTAS EXENTAS | 10 | exempt sales → casilla 85 | FR-058, FR-066 |
| L | VENTAS INTERNAS EXENTAS NO SUJETAS A PROPORCIONALIDAD | 10 | exempt not subject to proportionality → casilla 92 | FR-058, FR-066 |
| M | VENTAS NO SUJETAS | 10 | non-subject sales → casilla 86 | FR-058, FR-066 |
| N | VENTAS GRAVADAS LOCALES | 10 | taxed sales IVA-INCLUSIVE → casilla 96 | FR-058, FR-059, FR-066 |
| O | EXPORTACIONES DENTRO DEL ÁREA CENTROAMERICANA | 10 | goods exports GT/HN/SV/NI/CR → casilla 91 | FR-058, FR-060, FR-066 |
| P | EXPORTACIONES FUERA DEL ÁREA CENTROAMERICANA | 10 | goods exports outside CA → casilla 90 | FR-058, FR-060, FR-066 |
| Q | EXPORTACIONES DE SERVICIOS | 10 | service exports → casilla 94 | FR-058, FR-060, FR-066 |
| R | VENTAS A ZONAS FRANCAS Y DPA (TASA CERO) | 10 | ZF/DPA zero-rate sales → casilla 93 | FR-058, FR-060, FR-066 |
| S | VENTAS A CUENTA DE TERCEROS NO DOMICILIADOS | 10 | third-party non-domiciled (factura family) → casilla 89 | FR-058, FR-066 |
| T | TOTAL | 10 | K + L + M + N + O + P + Q + R + S | FR-058 |
| U | TIPO DE OPERACIÓN (Renta) | 2 | R code list; "0" pre-Enero-2025 | FR-062 |
| V | TIPO DE INGRESO (Renta) | 2 | S code list; "0" pre-Enero-2025 | FR-062 |
| W | NÚMERO DE ANEXO | 1 | literal 2 on every row | FR-054, FR-064 |

Length note: manual §IV prints the length only for J (14) within the D-J
identifier block; the other identifier lengths follow plantilla sheet "2"
(recorded as `plantilla` — structural conformance, not a printed manual
rule).

**Canonical identifier-slot mapping — l10n_sv.f07.idmap (seed data; the
table files 03/04 reference as SV-FREP-FR-042/043):**

| Slot | Clase 1 (imprenta/tiquetes) | Clase 2 (formulario único) | Clase 4 DTE ≥ Nov-2022 | Clase 4 DTE < Nov-2022 |
|------|------------------------------|----------------------------|------------------------|------------------------|
| RESOLUCIÓN | MH authorization of the printed range | per emitter authorization | número de control, hyphenless (28) | código de generación, hyphenless (32) |
| SERIE | printed series | — | sello de recepción (40) | sello de recepción (40) |
| NÚMERO (DEL/AL or single) | pre-printed number (range endpoints) | — | código de generación, hyphenless (32) | número de control, hyphenless (28) |
| CONTROL INTERNO | emitter's internal control (books) | formulario único control number | BLANK | BLANK |
| MÁQUINA REGISTRADORA (Anexo 2 J) | cash-register number (tiquetes) | — | blank | blank |

**Code lists (seed data):**

| List | Values |
|------|--------|
| clase de documento | 1 impreso por imprenta o tiquetes · 2 formulario único · 4 documento tributario electrónico DTE |
| Anexo 1 tipo | 03 comprobante de crédito fiscal · 05 nota de crédito · 06 nota de débito |
| Anexo 2 tipo | 01 factura de consumidor final · 02 factura de venta simplificada · 10 tiquetes de máquinas registradora · 11 factura de exportación |
| R / U tipo de operación (Renta) | 1 gravada · 2 no gravada o exento · 3 excluido o no constituye renta · 4 mixta · 12 ingresos ya sujetos de retención informados en el F14 y consolidados en F910 · 13 sujetos pasivos excluidos (art. 6 LISR) |
| S / V tipo de ingreso (Renta) | 1 profesiones, artes y oficios · 2 actividades de servicios · 3 actividades comerciales · 4 actividades industriales · 5 actividades agropecuarias · 6 utilidades y dividendos · 7 exportaciones de bienes · 8 servicios realizados en el exterior y utilizados en El Salvador · 9 exportaciones de servicios · 10 otras rentas gravables · 12/13 as in R |
| área centroamericana | Guatemala · Honduras · El Salvador · Nicaragua · Costa Rica |

**Entities:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.f07.annex1.row (new) | declaration_id, source_move_id, date, clase, tipo, slot_resolucion, slot_serie, slot_numero, slot_control_interno, client_nit_nrc, client_name, client_dui, ventas_exentas, ventas_no_sujetas, gravadas_netas, debito_fiscal, terceros_no_dom, debito_terceros, total_ventas, renta_op, renta_ingreso | m2o/char/monetary(2dp) | one row per emitted document (FR-045); renta_* = R/S codes or "0" per gate | FR-045..FR-052 |
| l10n_sv.f07.annex2.row (new) | declaration_id, date, clase, tipo, slot_resolucion, slot_serie, numero_del, numero_al, control_del, control_al, maquina_registradora, ventas_exentas, exentas_no_proporc, no_sujetas, gravadas_inclusive, expo_dentro_ca, expo_fuera_ca, expo_servicios, zf_dpa_tasa_cero, terceros_no_dom, total, renta_op, renta_ingreso, aggregation_mode | m2o/char/monetary(2dp)/select | aggregation_mode: range · day_group | FR-053..FR-062 |
| l10n_sv.f07.annex2.row.source (new) | annex2_row_id, move_id | m2o | membership of a posted move in an aggregated row (day-group or range) | FR-056, FR-065 |
| l10n_sv.f07.renta.classification (new) | move_id, renta_op, renta_ingreso, period_gate | char/select | defaults per fiscal classification; code 12/13 semantics of FR-052 | FR-052, FR-062 |
| l10n_sv.f07.aduanas.flag (new) | declaration_id, kind, row_ref, detail | select/text | kind: export_no_dua_link · export_dua_date_mismatch | FR-063 |

**Column→casilla wiring (builder interface into 01 §3.1; label-matched per
FR-066; 88/89 routed by document family):**

| Annex column | Casilla (label match) | Notes |
|--------------|----------------------|-------|
| Anexo 1 J / Anexo 2 K | 85 ventas internas exentas | |
| Anexo 1 K / Anexo 2 M | 86 ventas internas no sujetas | |
| Anexo 1 L + M | 95 / 135 gravadas con CCF + débito | CCF family |
| Anexo 2 N | 96 gravadas con factura | IVA-inclusive value; débito 140 computed by the IVA engine |
| Anexo 1 N + O | 88 / 141 terceros no domiciliados CL con CCF + débito | CCF family (OQ-005) |
| Anexo 2 S | 89 terceros no domiciliados CL con facturas | factura family; débito 142 computed (OQ-005) |
| Anexo 2 O | 91 exportaciones dentro región CA | Aduanas cross-check (FR-063) |
| Anexo 2 P | 90 exportaciones fuera región CA | Aduanas cross-check (FR-063) |
| Anexo 2 Q | 94 exportaciones de servicios | |
| Anexo 2 R | 93 zonas francas y D.P.A. tasa cero | |
| Anexo 2 L | 92 exentas no sujetas a proporcionalidad | |
| Anexo 1 NC rows (05) | 97 / 143 devoluciones sobre ventas + débito | netting per 01 FR-006 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these FRs
touch DTE generation/transformation (the only architecture-split surface
per `shared/docs/saas-thin-client-architecture.md`); FR-044 READS the
sealed-DTE archive that the e-invoicing wave owns. Model names are stable
across Odoo 17/18/19/20; version-specific behavior is recorded per row
where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-042 | odoo | l10n_sv.f07.idmap (seed) + l10n_latam.document.type | clase routing | Canonical slot model; files 03/04/05 reference SV-FREP-FR-042/043 — no restatement |
| FR-043 | odoo | l10n_sv.f07.idmap (seed) | DTE slot fills | D12 dated data: Nov-2022 cutover — pre-Nov-2022 DTEs swap RESOLUCIÓN/NÚMERO sources (código 32 / número de control 28); SERIE (sello 40) never swaps |
| FR-044 | odoo | account.move (read) + l10n_sv.f07.annex1.row/annex2.row | identifier validation | Sources the sealed DTE identifiers (SV-EINV-FR-003/004/092 kin); hyphenless 40/32/28 length checks; 24h same-code corrections keep the código (02 FR-078) |
| FR-045 | odoo | l10n_sv.f07.annex1.row | granularity + exclusion | Voided/lost docs route to the anulados annex (04 file §3); the emitidos annex auto-derivation consumes Anexo 1/2 (EVID-178 §XVIII — 04 file's FR) |
| FR-046 | odoo | l10n_sv.f07.annex1.row | column order A-T | Plantilla sheet "1" conformance; T = 1 on every row |
| FR-047 | odoo | l10n_sv.f07.annex1.row + res.partner | client identification | NIT/NRC 14 max; name unlimited; DUI per XOR |
| FR-048 | odoo | l10n_sv.f07.annex1.row | J..P buckets | L NET convention (R1/SV-EINV-FR-024 — OQ-002); M/O débito companions computed by the IVA engine (rate anchor = future IVA taxation file, cf. 01 OQ-004); P = J+K+L+N |
| FR-049 | odoo | l10n_sv.f07.annex1.row (move type routing) | NC/ND positive rows | Netting to 97/143 consumed by 01 FR-004/FR-006 |
| FR-050 | odoo | l10n_sv.f07.annex1.row | XOR validation | D12: Enero-2022 gate; pre-2022 NIT/NRC mandatory; juridical → NIT always |
| FR-051 | odoo | l10n_sv.f07.annex1.row | renta_op/renta_ingreso | D12: Enero-2025 gate else "0"; 2-char codes (printed "10" = manual typo, OQ-003) |
| FR-052 | odoo | l10n_sv.f07.renta.classification | R/S codes | Code 12 = F14/F910-consolidated (F9 crossref); 13 = Art. 6 LISR excluidos; ISR-side consumption only |
| FR-053 | odoo | l10n_sv.f07.annex2.row | aggregation_mode | Modes: range (physical) · day_group (DTE); never per-document for DTE |
| FR-054 | odoo | l10n_sv.f07.annex2.row | column order A-W | Plantilla sheet "2" conformance; W = 2 on every row |
| FR-055 | odoo | l10n_sv.f07.annex2.row | range rows | DEL/AL endpoints; F=G / H=I identity rules per clase; J máquina registradora for tipo 10 |
| FR-056 | odoo | l10n_sv.f07.annex2.row + .source | day groups | D/E = "N/A"; F/G = first/last código de generación (hyphenless 32); H/I/J blank; row ordering → OQ-001 |
| FR-057 | odoo | l10n_latam.document.type | tipo catalog note | 02/10 = non-DTE-emitter codes only (R12; SV-EINV-FR-129); historical compatibility rows |
| FR-058 | odoo | l10n_sv.f07.annex2.row | K..T buckets | T = K+L+M+N+O+P+Q+R+S; no débito columns on this annex |
| FR-059 | odoo | account.tax + l10n_sv.f07.annex2.row | convention switch | N IVA-INCLUSIVE (R1/SV-EINV-FR-019) vs Anexo 1 L net (FR-024); must mirror the e-invoicing price_include configuration (SV-EINV §5 FR-019/024 rows) |
| FR-060 | odoo | l10n_sv.f07.annex2.row + res.partner (destination) | export routing | CA = GT/HN/SV/NI/CR (LB-006); ZF/DPA tasa 0; destination country decides O/P |
| FR-061 | odoo | l10n_sv.f07.annex2.row | negative gate | Inherits 01 FR-031; anulados routing per CT 111 (04 file §3) |
| FR-062 | odoo | l10n_sv.f07.annex2.row | renta_op/renta_ingreso (U/V) | D12: Enero-2025 gate else "0"; same lists as R/S (OQ-004) |
| FR-063 | odoo | l10n_sv.f07.aduanas.flag | awareness flags | Informational only (EV34 OQ-5); no computation; import side = 03 file |
| FR-064 | odoo | l10n_sv.f07.annex.upload (01 file's engine) | format inheritance | 01 FR-028..041 apply unchanged; sales annexes = current-period-only window (01 FR-033) |
| FR-065 | odoo | account.move (sale-side builder) | routing + modes | Posted moves only; receiver fiscal category + document type route 1 vs 2; a move never feeds both annexes |
| FR-066 | odoo | l10n_sv.f07.casilla.value (01 file) + §4 wiring table | totals interface | 88/141 vs 89/142 routed by document family (OQ-005); no manual casilla fill (01 FR-038) |

Version-regime notes (D12): three dated gates live in this file — the
Nov-2022 DTE identifier cutover (FR-043), the Enero-2022 DUI-vs-NIT XOR
gate (FR-050) and the Enero-2025 R/S/U/V gates (FR-051/FR-062) — each
stored as period-keyed configuration so a future regime change re-dates
without code change. The F-07 v14 annex vintage (manual ENERO 2025,
plantilla v14) is the operative structure; a future manual revision
re-seeds the column models. The tipo-02/10 regime note (FR-057) tracks
ruling R12's 01-Jan-2025 tiquete ban for DTE emitters.

## 6. Acceptance Criteria

- **AC-001:** Given a sealed CCFE dated 15/03/2025 with número de control
  "DTE-03-P0050001-000000000000123", sello
  "2025F2041F1DCE1A4CE4B10B6AABFD344125QTZS" and código de generación
  "8f5e2a1b-c4d9-4e6f-9a2b-1c3d5e7f9a0b", when its Anexo 1 row is
  exported, then D reads `DTE03P0050001000000000000123` (28, hyphenless),
  E reads the 40-char sello, F reads
  `8f5e2a1bc4d94e6f9a2b1c3d5e7f9a0b` (32, hyphenless) and G is empty;
  given the same document dated 15/09/2022 (pre-cutover), then D reads
  the hyphenless código (32) and F reads the hyphenless número de control
  (28) — the slots swap, E does not (FR-042, FR-043, FR-044).
- **AC-002:** Given a posted CCF invoice to an NIT-registered customer
  with exempt 100.00, non-subject 50.00 and taxed base 1,000.00 + IVA
  130.00, when Anexo 1 is generated, then exactly ONE row exists with
  J=100.00, K=50.00, L=1000.00, M=130.00, P=1150.00, T=1, and no Anexo 2
  row exists for that move (FR-045, FR-046, FR-048, FR-065).
- **AC-003:** Given an Anexo 1 row for period 03/2025 whose client states
  both a DUI and a NIT, then the row is rejected by the XOR validation;
  given a DUI-only natural-person row in period 03/2025, then it is
  accepted (H empty); given a DUI-only row in period 12/2021, then it is
  rejected — pre-Enero-2022 requires the NIT/NRC (FR-050).
- **AC-004:** Given Anexo 1 generated for period 12/2024, then every row's
  R and S columns read `0`; given the same customer documents in period
  01/2025 with renta classification R=4, S=3, then the columns read `4`
  and `3`; given a retained-then-consolidated income row, then R reads
  `12` (F-14-reported, F-910-consolidated) (FR-051, FR-052).
- **AC-005:** Given four sealed consumer FEs emitted 07/07/2025 and two
  emitted 08/07/2025, when Anexo 2 is generated, then exactly TWO clase-4
  rows exist: the 07/07 row with D=`N/A`, E=`N/A`, F=the first emitted
  código (hyphenless 32), G=the last emitted código of that day, H/I/J
  empty, and buckets aggregating all four documents; ditto the 08/07 row
  for the two documents; no per-document DTE row exists (FR-053,
  FR-056).
- **AC-006:** Given an FE with IVA-inclusive gravadas total 113.00 and
  its CCF counterpart with net base 100.00 + IVA 13.00, then the Anexo 2
  N bucket for the FE reads `113.00` while the Anexo 1 L column for the
  CCF reads `100.00` with M=`13.00` — the convention switch holds
  (FR-048, FR-059).
- **AC-007:** Given B2C export invoices to Guatemala and to the United
  States plus a service export and a zona-franca sale, then the GT value
  lands in O, the US value in P, the service value in Q and the ZF value
  in R; T equals the sum of K through S of the row (FR-058, FR-060).
- **AC-008:** Given a voided consumer document of the period, then NO
  Anexo 2 row carries a negative amount: the document is excluded from
  Anexo 2 and its negative magnitude appears only in the anulados annex
  of `04_f07-annexes-retentions-events.md` §3 (CT 111) (FR-045,
  FR-061).
- **AC-009:** Given Anexo 2 generated for period 06/2024, then every U
  and V column reads `0`; for period 01/2025 forward they carry the
  FR-052 code lists (FR-062).
- **AC-010:** Given a cash-register tiquete range of machine registered
  as `00000000000005` for 10/05/2024, then the row reads B=1, C=10, the
  J column carries the 14-character machine number, F/G carry the range
  DEL/AL endpoints, and F=G only when the range covers one document
  (FR-055).
- **AC-011:** Given a period whose Anexo 2 O/P totals include export
  documents without DUA linkage, then the declaration surfaces
  Aduanas-awareness flags naming those rows, and NO casilla value is
  altered by the flag (informational only) (FR-063).
- **AC-012:** Given validated Anexo 1/2 uploads for a declaration, then
  the last column of every row reads 1 (Anexo 1) / 2 (Anexo 2), the
  files conform to the 01 §3.2 format engine (semicolon, Text, ≤25-char
  filename, 0.00 nils), and the sales casillas re-total per the §4 wiring
  table with no manual fill — e.g., the sum of Anexo 1 J lands in casilla
  85 and Anexo 1 N in casilla 88 (FR-064, FR-066).
- **AC-013:** Given a *declaración modificatoria* (amended return), then
  annexes 1 and 2 are regenerated and re-uploaded (never carried over)
  per 01 FR-040, and the regenerated rows fully replace the prior upload
  per 01 FR-041 (FR-064).
- **AC-014:** Given an Anexo 2 file whose DTE day-group rows are ordered
  by emission date, the system accepts it; given the same rows reordered
  by código de generación, the system likewise accepts it — no ordering
  rule is enforced pending OQ-001 (FR-056; OQ-001).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | EV34 OQ-3 carried: Anexo 2 DTE daily grouping — "Código de Generación del primer/último DTE emitido" per day — the required ROW ORDERING of the daily groups (by day? by code?) is unstated and the validations beyond the generic §XVI set are unknown. FR-056 encodes no ordering rule; AC-014 accepts both orderings. Confirm against a live MH upload or the annex-modification resolutions (01 §7 OQ-001 kin). | no | Takumi S3 | open |
| OQ-002 | Anexo 1 L (VENTAS GRAVADAS LOCALES) net-of-IVA convention: manual §III prints no explicit "sin IVA" wording for L (unlike Anexo 2 N's explicit "Deberá detallarlas con IVA incluido"). Net encoding rests on the separate M DÉBITO FISCAL column + ruling R1 / SV-EINV-FR-024 (Ley IVA Art. 57, LB-008). Confirm before certifying exports. | no | Takumi S3 | open |
| OQ-003 | R/S column lengths: the §III column table prints "Total de caracteres 10" for R/S while its own text says "máximo dos caracteres" — the table's "10" is the manual's typo (EVID-174 doubt). FR-051 encodes 2-character codes. | no | Takumi S3 | open |
| OQ-004 | Anexo 2 U/V code lists: manual §IV prints the U/V gate (from Enero-2025, else "0") but no separate U/V code lists — FR-062 assumes the same lists as Anexo 1's R/S (EVID-175 prints only "U/V Renta pair"). Confirm whether §IV carries its own lists in a manual revision. | no | Takumi S3 | open |
| OQ-005 | Terceros-casilla wiring: routing Anexo 1 N/O → casillas 88/141 and Anexo 2 S → casilla 89 (débito 142 computed, no column) rests on the document-family reading of the casilla labels ("Comprobante de Liquidación con C.C.F." / "con Facturas" — LB-002 of 01). Label-matched inference; confirm against MH auto-totalization behavior. | no | Takumi S3 | open |
| OQ-006 | Anexo 2 H/I treatment on DTE day-group rows: the manual's grouping instruction covers F/G (first/last código de generación); FR-056 leaves H/I blank by extension of the control-interno-blank rule (FR-043/LB-002), but §IV does not print H/I's DTE value explicitly (N/A vs blank unstated). | no | Takumi S3 | open |

