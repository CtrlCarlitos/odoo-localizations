# SV — Fiscal reporting — F-07 purchase annexes 3/5: IVA buckets, ISR cost/gasto quartet & excluded subjects

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for the two F-07 purchase
annexes of the *Manual de Usuario para Carga de Archivo de los Anexos*
(annex upload user manual), F-07 V14, ENERO 2025: **Anexo 3 Compras**
(purchases — THE purchase annex: one row per purchase document, document
types 03/05/06/11/12/13 with the ZF/DPA-only tipo 11 and the customs
documents 12/13, the IVA base buckets G-M crossing acquisition channel
(*compras internas* / *internaciones* / *importaciones*: internal
purchases / CA-region internations / imports) with tax status (exempt
and/or non-subject vs taxed), the *crédito fiscal* (fiscal credit)
column N = 13% of the taxed bucket sum J..M as a row-level validation,
the total column O with its ND+/NC− semantics, the DUI-vs-NIT
exclusive-or for natural-person suppliers, the Tesorería pseudo-NIT for
foreign suppliers of customs documents, and — since Febrero-2024 — the
ISR cost/gasto classification quartet Q/R/S/T (*Tipo de Operación /
Clasificación / Sector / Tipo de Costo-Gasto*) that this file owns
CANONICALLY for the whole localization: the code lists, the
Febrero-2024 gate, the multi-annex deduplication code 8 and the
public-institutions/non-deductibles code 9 are stated ONCE here, and
`06_f14-declaration.md` (the F-14 annex's twin S-V columns) references
SV-FREP-FR-079..085 instead of restating them) and **Anexo 5 Compras a
Sujetos Excluidos** (purchases from excluded subjects — the CT Art. 119
anchor as printed, the supplier document-type triplet NIT/DUI/OTRO, the
13% IVA retention column "cuando aplique" (when applicable), its own
I-L quartet under the canonical lists, and the post-*entero*
(after-remittance) credit re-entry path: the retained 13% becomes
*crédito fiscal* only after its remittance is recorded, then feeds
casilla 128 of the F-07).

It does **not** cover: the declaration casilla engine and the generic
annex upload format/validations/modificatoria flow
(`01_f07-declaration.md` §3.1/§3.2 — SV-FREP-FR-001..041; the
semicolon-CSV, Text-cell, two-decimal, negative-gate, date/period,
three-prior-period, annex-number and clean-replace rules live THERE and
are inherited here by reference); the sales annexes and the canonical
document-identifier mapping (`02_f07-annexes-sales.md` §3 —
SV-FREP-FR-042/043 own the slot model and the DTE mapping; this file
references them by id and never restates); the retention/perception
annexes 4/6-12, the anulados/extraviados annex and the
invalidation-event feed (`04_f07-annexes-retentions-events.md` §3); the
fuel and dated-regime annexes 13-17 (`05_f07-annexes-special.md` §3 —
including Anexo 16, the Decreto 357 informativo over casilla 65, which
cluster F4 lists among the purchase annexes but which this wave's file
split assigns to the dated-regime file, F7); the F-14 declaration
family and income-code catalog
(`06_f14-declaration.md`, `07_codes-and-informs.md` — consumers of the
canonical quartet); the filing calendar (`08_filing-calendar.md` —
SOQ-08); the IVA computation proper (13% rate base, deductibility Arts.
65/65-A, Ley IVA Art. 66 pro-rata feeding casillas 132-134 — future IVA
taxation file territory, cf. 01 §7 OQ-004; the Q-T quartet here only
CLASSIFIES rows for the ISR side); and the ISR deduction machinery
itself (`taxation/02_isr-deductions.md` — SV-TAX-FR-035/036/052 own the
necessary-cost gate, the pro-rata allocator and the Art. 29-A
non-deductible classifier that the Q codes and code 9 cross-reference
by id). Task 1's casilla FRs (SV-FREP-FR-010/011/012) consume this
file's annex totals; Task 4's annex family references this file's row
models and quartet FRs.

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and upload manuals ARE the
primary authority for declaration mechanics — 34_ (Manual de Usuario
para Carga de Archivo de los Anexos, F-07 V14, ENERO 2025) is the
governing source for both annex structures; the plantilla workbook 36_
(sheets "3" and "5") is the structural conformance reference; the form
39_ (F-07 v14, footer "Actualizado al 15/08/2025") anchors the casilla
wiring labels. Legal anchors printed in the manual (CT Art. 119 for the
excluidos purchases, Ley ZF Art. 25 inside the tipo-11 wording, CT Art.
162 on casilla 128 via 01's LB-003) are cited as printed; no article
text is invented beyond what the form/evidence quotes. Manual pages are
printed pages (printed page N = PDF page N+2).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-07 v14 §V, Anexo 3 "Compras", tabla de columnas: "A FECHA / B CLASE 1/2/3 Otros/4 DTE / C TIPO: 03 CCF / 05 NC / 06 ND / 11 Factura de Exportación: éste deberán utilizarlo los usuarios de Zona Franca o DPA únicamente por la compra de bienes o servicios en el territorio nacional, de acuerdo a lo establecido en el Artículo 25 de la Ley de Zonas Francas Industriales y de Comercialización / 12 Declaración de Mercancías / 13 Mandamiento de Ingreso / D NÚMERO DE DOCUMENTO 100 / E NIT/NRC PROVEEDOR 14 / F NOMBRE / G COMPRAS INTERNAS EXENTAS Y/O NO SUJETAS / H INTERNACIONES EXENTAS Y/O NO SUJETAS / I IMPORTACIONES EXENTAS Y/O NO SUJETAS / J COMPRAS INTERNAS GRAVADAS / K INTERNACIONES GRAVADAS DE BIENES / L IMPORTACIONES GRAVADAS DE BIENES / M IMPORTACIONES GRAVADAS DE SERVICIOS / N CRÉDITO FISCAL / O TOTAL DE COMPRAS / P DUI / Q TIPO DE OPERACIÓN / R CLASIFICACIÓN / S SECTOR / T TIPO DE COSTO / GASTO / U NÚMERO DE ANEXO 3" | F-07 v14 upload manual §V, Anexo 3 column table A-U with the printed field lengths (document number 100, supplier NIT/NRC 14) and the annex's own document-class list (1, 2, 3 Otros, 4 DTE — clase 3 admitted here) and type list: CCF, credit note, debit note, export invoice (ZF/DPA users only, for national-territory purchases of goods or services, per Art. 25 of the Free Zones Law as printed in the manual), merchandise declaration, payment deposit warrant | `sv/sources/34_F07_v14_manual.pdf` | §V pp.12-17 (EVID-176; plantilla sheet "3" in `sv/sources/36_F07_v14_plantilla.xls`) |
| LB-002 | Manual F-07 v14 §V, Anexo 3: "Si es un proveedor del exterior, para los tipos de documento 12 y 13 puede colocar el NIT de la Dirección General de Tesorería 06140108140066"; N (CRÉDITO FISCAL): "Corresponde al 13% del total de las operaciones gravadas detalladas en las columnas comprendidas de la J a la M"; O (TOTAL DE COMPRAS): total G..M "sumando las Notas de Débito y restando las Notas de Crédito" | F-07 v14 upload manual §V: for a foreign supplier on document types 12/13 the Treasury Directorate's NIT 06140108140066 may be placed in the supplier column; the fiscal-credit column N = 13% of the total taxed operations detailed in columns J through M; the purchase total O sums G..M adding debit notes and subtracting credit notes | `sv/sources/34_F07_v14_manual.pdf` | §V pp.12-17 (EVID-176) |
| LB-003 | Manual F-07 v14 §V, Anexo 3: "Las nuevas columnas 'Q, R, S, T' aplica a partir del periodo de Febrero 2024"; Q TIPO DE OPERACIÓN: "1 Gravada / 2 No Gravada / 3 Excluido o no Constituye Renta / 4 Mixta (... costos y gastos que inciden en la actividad generadora de rentas gravadas, así como aquellos que afectan las rentas no gravadas ... Aplica también para los contribuyentes que gozan de Regímenes Especiales o beneficio fiscal)"; R CLASIFICACIÓN: "1 Costo / 2 Gasto"; S SECTOR: "1 Industria / 2 Comercio / 3 Agropecuaria / 4 Servicios, Profesiones, Artes y Oficios"; T TIPO DE COSTO/GASTO: "1 Gastos de Venta sin Donación / 2 Gastos de Administración sin Donación / 3 Gastos Financieros sin Donación / 4 Costo Artículos Producidos/Comprados Importaciones/Internaciones / 5 Costo Artículos Producidos/Comprados Interno / 6 Costos Indirectos de Fabricación / 7 Mano de obra" | F-07 v14 upload manual §V ISR cost/gasto quartet: Q/R/S/T apply from the Febrero-2024 period; Q operation-type codes 1 taxed / 2 not taxed / 3 excluded or not constituting income / 4 mixed (costs and expenses affecting both taxed and non-taxed income-generating activity — also for special-regime or fiscal-benefit taxpayers); R cost-vs-expense classification 1/2; S sector 1 industry / 2 commerce / 3 agriculture-and-livestock / 4 services-professions-arts-trades; T cost/expense type: sales expenses without donation / administration expenses without donation / financial expenses without donation / cost of articles produced or purchased imports-internations / cost of articles produced or purchased internal / indirect manufacturing costs / labor | `sv/sources/34_F07_v14_manual.pdf` | §V pp.12-17 (EVID-176) |
| LB-004 | Manual F-07 v14 §V, Anexo 3, notas de códigos 8/9: "Cuando una misma operación es informada en diferentes anexos, ésta debe ser clasificada con el código 8 'Operaciones informadas en más de 1 anexo', a efecto de identificar y no considerar en la suma de costos y gastos de la Declaración del Impuesto sobre la Renta, los valores reportados con dicho código." + "Para las Instituciones Públicas, Municipalidades y contribuyentes con operaciones no deducibles para Renta vía costo o gasto, las 4 columnas anteriores (Q, R, S, T) deberán ser completadas con el código '9'." | F-07 v14 upload manual §V: an operation reported in more than one annex is classified with code 8 "operations reported in more than 1 annex", so that the values reported with that code are identified and NOT considered in the ISR declaration's cost-and-expense sums; for public institutions, municipalities and taxpayers with operations non-deductible for ISR via cost or expense, all four columns Q/R/S/T are completed with code 9 | `sv/sources/34_F07_v14_manual.pdf` | §V pp.12-17 (EVID-176) |
| LB-005 | Manual F-07 v14 §V, Anexo 3, cruce Aduanas: los valores de importaciones/internaciones "se compararán con los valores reportados por la Dirección General de Aduanas, de acuerdo al levante de las mercancías" | F-07 v14 upload manual §V: import/internation values declared in Anexo 3 are compared by MH against the values reported by the Dirección General de Aduanas (customs), on the basis of the merchandise release (*levante*) | `sv/sources/34_F07_v14_manual.pdf` | §V pp.12-17 (EVID-176) |
| LB-006 | Manual F-07 v14 §VII, Anexo 5 "Compras a Sujetos Excluidos" (casilla 66), tabla de columnas: "A TIPO DOC 1 ('1 NIT / 2 DUI / 3 OTRO DOCUMENTO') / B NIT/DUI/OTRO 14 / C NOMBRE / D FECHA / E SERIE (DTE = sello recepción) / F NÚMERO (DTE = código generación) / G MONTO / H MONTO DE LA RETENCIÓN IVA 13% ('Corresponde al 13% del monto de la operación cuando aplique') / I-L cuarteto Renta (Feb-2024) / M NÚMERO DE ANEXO 5"; ancla: "documentos de compra a sujetos excluidos de acuerdo con lo establecido en el artículo 119 el Código Tributario" | F-07 v14 upload manual §VII, Anexo 5 column table A-M: supplier document type (NIT / DUI / other document) and number (14), name, date, series (DTE = reception seal), number (DTE = generation code), amount, "AMOUNT OF THE 13% IVA RETENTION" (= 13% of the operation amount when applicable), the I-L ISR quartet under the Febrero-2024 gate, annex number 5; anchor: purchase documents from excluded subjects per Article 119 of the Tax Code (as printed) | `sv/sources/34_F07_v14_manual.pdf` | §VII pp.22-27 (EVID-177; plantilla sheet "5" in `sv/sources/36_F07_v14_plantilla.xls`) |
| LB-007 | Manual F-07 v14 §VII, Anexo 5, ruta del crédito: "por las retenciones de 13% de IVA donde se genera crédito fiscal, posterior al entero de dichas retenciones IVA, dicho crédito fiscal se incorporará en la casilla 128 del formulario F-07" | F-07 v14 upload manual §VII credit path: for the 13% IVA retentions where fiscal credit arises, AFTER the remittance (*entero*) of those IVA retentions the fiscal credit is incorporated into casilla 128 of the F-07 form | `sv/sources/34_F07_v14_manual.pdf` | §VII pp.22-27 (EVID-177; casilla 128 owned by `01_f07-declaration.md` SV-FREP-FR-012, label "Crédito por Retención 13% IVA a terceros domiciliados (Art. 162 C.T)" per EVID-179) |
| LB-008 | Manual F-07 v14 §V/§VII (glosa familiar EVID-176/177): DUI-vs-NIT XOR desde enero 2022 para personas naturales; documentos anulados excluidos de los anexos de detalle; sin valores negativos; compras: "de acuerdo a lo establecido en el artículo 63 de la Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, se pueden ingresar documentos de 3 periodos anteriores al que está declarando" | F-07 v14 upload manual family rules for the purchase annexes: from Enero-2022 natural-person suppliers state either DUI or NIT/NRC, never both (before Enero-2022 the NIT/NRC is mandatory); voided documents are excluded from the detail annexes; no negative values; purchase documents dated up to three prior periods are admitted per Ley IVA Art. 63 as printed in the manual | `sv/sources/34_F07_v14_manual.pdf` | §V pp.12-17; §VII pp.22-27 (EVID-176; EVID-177; EVID-173 §V) |
| LB-009 | Formulario F-07 v14, C. Compra de Bienes y/o Servicios Créditos, filas 24-33: "24 Compras Internas Exentas y/o No sujetas 65 / 25 Compras a sujetos excluidos 66 / 26 Importaciones Exentas y/o No Sujetas 70 / 27 Importaciones Gravadas de Servicios 77 (Crédito por Importación de Servicios 127) / 28 Importaciones Gravadas de Mercancías (Fuera de Región C.A.) 75 (Crédito ... 125) / 29 Internaciones Gravadas de Mercancías (Dentro Región C.A.) 76 (Crédito ... 126) / 30 Compras Internas Gravadas 80 (Crédito ... 130) / 32 Devoluciones ... sobre Compras 81− (Crédito ... 131−)" | F-07 v14 form Section C purchase rows 24-33: the casilla labels that the Anexo 3/5 columns wire into by label match — 65 internal exempt/non-subject purchases, 66 excluded-subject purchases, 70 exempt imports, 77 taxed service imports (credit 127), 75 taxed merchandise imports OUTSIDE the CA region (credit 125), 76 taxed merchandise internations INSIDE the CA region (credit 126), 80 taxed internal purchases (credit 130), 81 returns over purchases (credit 131, negative) | `sv/sources/39_F07_v14_form_visual.pdf` | p.1 (EVID-179; wiring consumed by `01_f07-declaration.md` FR-010/FR-011) |

## 3. Functional Requirements

### 3.1 Anexo 3 — Compras: row model, document routing and IVA buckets

- **SV-FREP-FR-067:** The system shall build Anexo 3 (*Compras*,
  purchases) with ONE ROW PER PURCHASE DOCUMENT, admitting only TIPO DE
  DOCUMENTO 03 (*Comprobante de Crédito Fiscal*, tax-credit document),
  05 (*Nota de Crédito*, credit note), 06 (*Nota de Débito*, debit
  note), 11 (*Factura de Exportación* — ZF/DPA users only, FR-073), 12
  (*Declaración de Mercancías*, merchandise/customs declaration) and 13
  (*Mandamiento de Ingreso*, treasury payment deposit warrant); voided
  and lost documents (*anulados y/o extraviados*) are EXCLUDED and
  route to the anulados annex owned by
  `04_f07-annexes-retentions-events.md` §3; purchase documents dated
  up to THREE prior periods before the declared period are admitted
  (three-prior-period window inherited from SV-FREP-FR-033, Ley IVA
  Art. 63 as printed). (LB-001; LB-008; EVID-176; EVID-173; cross-ref
  SV-FREP-FR-033)
- **SV-FREP-FR-068:** The system shall emit every Anexo 3 row with the
  verbatim column model A-U of manual §V — A FECHA (10) · B CLASE DE
  DOCUMENTO (1) · C TIPO DE DOCUMENTO (2) · D NÚMERO DE DOCUMENTO
  (100) · E NIT/NRC PROVEEDOR (14) · F NOMBRE (no printed limit) ·
  G COMPRAS INTERNAS EXENTAS Y/O NO SUJETAS · H INTERNACIONES EXENTAS
  Y/O NO SUJETAS · I IMPORTACIONES EXENTAS Y/O NO SUJETAS · J COMPRAS
  INTERNAS GRAVADAS · K INTERNACIONES GRAVADAS DE BIENES ·
  L IMPORTACIONES GRAVADAS DE BIENES · M IMPORTACIONES GRAVADAS DE
  SERVICIOS · N CRÉDITO FISCAL · O TOTAL DE COMPRAS · P DUI · Q TIPO
  DE OPERACIÓN · R CLASIFICACIÓN · S SECTOR · T TIPO DE COSTO / GASTO
  · U NÚMERO DE ANEXO = 3 — in exactly this order, conforming to
  plantilla sheet "3"; amount columns G-O follow the generic
  10-character two-decimal format (SV-FREP-FR-030) and the date column
  the DD/MM/AAAA period rule (SV-FREP-FR-032/FR-033).
  (LB-001; EVID-176; cross-ref SV-FREP-FR-030/032/033)
- **SV-FREP-FR-069:** The system shall apply Anexo 3's OWN
  document-class list — CLASE 1, 2, 3 *Otros* (other) or 4 DTE —
  recording that clase 3 is admitted on this annex (the §V list prints
  "1/2/3 Otros/4 DTE", whereas Anexo 1 admits 1/2/4,
  `02_f07-annexes-sales.md` FR-042): the class selects the identifier
  fill of FR-070 and no other annex's class list is affected.
  (LB-001; EVID-176)
- **SV-FREP-FR-070:** The system shall fill the single identifier
  column D (NÚMERO DE DOCUMENTO) per class: clase 1/2/3 rows carry the
  physical/other document number (customs documents 12/13: the
  declaration/warrant number); clase 4 rows carry the canonical
  NÚMERO-slot value of SV-FREP-FR-043 — the *código de generación*
  (generation code) hyphenless (32) from the Noviembre-2022 period
  forward, the *número de control* (control number) hyphenless (28)
  before it — as the label-matched extension of the canonical mapping
  to this annex's single NÚMERO-named slot (manual §V prints NO
  per-column DTE mapping for Anexo 3, unlike §VII for Anexo 5 — the
  extension is recorded in OQ-001; the mapping itself is NEVER
  restated here). (LB-001; EVID-176; cross-ref SV-FREP-FR-042/043)
- **SV-FREP-FR-071:** The system shall fill the
  supplier-identification columns from the supplier master data of the
  row's source document: E = the supplier's NIT or NRC (14), F = the
  supplier's name with no printed limit, P = the supplier's DUI — and
  shall enforce the DUI-vs-NIT exclusive-or with its period gate,
  mirroring SV-FREP-FR-050: from the Enero-2022 period, natural-person
  suppliers state EITHER the DUI (P filled, E empty) OR the NIT/NRC
  (E filled, P empty) — a row carrying both, or neither, is rejected;
  before Enero-2022 the NIT/NRC (E) is mandatory and P stays empty;
  juridical persons always carry the NIT/NRC and never a DUI.
  (LB-001; LB-008; EVID-176; EVID-177; EVID-174; cross-ref
  SV-FREP-FR-050)
- **SV-FREP-FR-072:** The system shall substitute the supplier NIT on
  foreign-supplier customs rows: when the supplier of a tipo 12 or
  tipo 13 row is a foreign supplier (*proveedor del exterior*), the
  system fills E with the NIT of the *Dirección General de Tesorería*
  (Treasury Directorate) **06140108140066** per the printed allowance
  "para los tipos de documento 12 y 13 puede colocar el NIT de la
  Dirección General de Tesorería 06140108140066" — implemented as a
  seeded Tesorería pseudo-supplier record, with the foreign supplier's
  real name kept in F; the manual words the substitution as an
  allowance ("puede colocar") — the system applies it BY DEFAULT for
  foreign suppliers without a Salvadoran NIT, and the substitution
  applies ONLY to tipos 12/13. (LB-002; EVID-176)
- **SV-FREP-FR-073:** The system shall admit TIPO 11 (*Factura de
  Exportación*, export invoice) on Anexo 3 ONLY for users of *Zona
  Franca* (free zone) or *DPA* (*depósito de perfeccionamiento
  activo*, active perfection deposit) and only for the purchase of
  goods or services in the national territory, per the printed rule
  "éste deberán utilizarlo los usuarios de Zona Franca o DPA
  únicamente por la compra de bienes o servicios en el territorio
  nacional, de acuerdo a lo establecido en el Artículo 25 de la Ley de
  Zonas Francas Industriales y de Comercialización" (Ley ZF Art. 25
  anchor AS PRINTED in the manual — the regime mechanics belong to the
  special-regimes wave, not this file); a tipo-11 row whose buyer is
  not a ZF/DPA user is rejected. (LB-001; EVID-176)
- **SV-FREP-FR-074:** The system shall route the customs document
  channels: TIPO 12 (*Declaración de Mercancías*) is the SINGLE
  goods-customs channel — its taxed values land in L (IMPORTACIONES
  GRAVADAS DE BIENES) for imports from OUTSIDE the CA region or in K
  (INTERNACIONES GRAVADAS DE BIENES) for internations from WITHIN it
  (dentro Región C.A., per the casilla-76 label), and its exempt
  values in I or H under the same origin split; TIPO 13 (*Mandamiento
  de Ingreso*) is the channel through which taxed SERVICE imports are
  reported — its taxed values land in M (IMPORTACIONES GRAVADAS DE
  SERVICIOS) — services having no merchandise declaration
  (channel/bucket association is label-matched from the column names
  and the dentro/fuera Región C.A. casilla labels — OQ-006).
  (LB-001; LB-009; EVID-176; EVID-179)
- **SV-FREP-FR-075:** The system shall fill the IVA base buckets G-M
  per column semantics — G *compras internas exentas y/o no sujetas*
  (internal exempt and/or non-subject purchases), H *internaciones
  exentas y/o no sujetas* (CA-region internations, exempt/non-subject),
  I *importaciones exentas y/o no sujetas* (imports,
  exempt/non-subject), J *compras internas gravadas* (internal taxed
  purchases), K *internaciones gravadas de bienes* (taxed goods
  internations), L *importaciones gravadas de bienes* (taxed goods
  imports), M *importaciones gravadas de servicios* (taxed service
  imports) — one row places each acquisition in the bucket crossing
  its acquisition channel with its tax status, with 0.00 in every
  non-applicable bucket (SV-FREP-FR-030 nil rule); credit and debit
  notes (tipos 05/06) are emitted as rows of their own with POSITIVE
  magnitudes in the same buckets as the documents they adjust — never
  as negatives (negative gate inherited from SV-FREP-FR-031).
  (LB-001; LB-008; EVID-176; cross-ref SV-FREP-FR-031)
- **SV-FREP-FR-076:** The system shall validate the *crédito fiscal*
  column N as exactly **N = 13% of the sum J + K + L + M** of the row
  — "Corresponde al 13% del total de las operaciones gravadas
  detalladas en las columnas comprendidas de la J a la M" — computed
  on the row's taxed buckets only (G/H/I never enter the credit
  base), rounded to two decimals under the FR-027 discipline; a row
  whose N differs from 13% × (J+K+L+M) is surfaced as a validation
  inconsistency before export. (LB-002; EVID-176; cross-ref
  SV-FREP-FR-027)
- **SV-FREP-FR-077:** The system shall compute the row total O (TOTAL
  DE COMPRAS) as the sum of the row's value buckets G through M under
  the printed ND+/NC− semantics "sumando las Notas de Débito y
  restando las Notas de Crédito": a CCF or ND row's O =
  G+H+I+J+K+L+M (additive); an NC row's magnitudes are recorded
  POSITIVE on its own row per the negative gate (SV-FREP-FR-031) but
  its totalization contribution is SUBTRACTIVE — the row-level
  reading is forced by the no-negatives rule, and the subtraction is
  realized at the declaration level where NC totals feed casillas
  81/131 per SV-FREP-FR-011 (FR-093 wiring); the crédito column N is
  a tax column and NEVER a term of O. (LB-002; EVID-176; cross-ref
  SV-FREP-FR-011/031)
- **SV-FREP-FR-078:** The system shall surface the IMPORT-side
  Aduanas cross-check AWARENESS flags — informational only, no
  computation: because the import/internation values "se compararán
  con los valores reportados por la Dirección General de Aduanas, de
  acuerdo al levante de las mercancías", the system shall flag (i)
  import/internation rows (buckets H/I/K/L) whose values rest on
  documents without customs *levante* (release) linkage and (ii)
  period totals of H/I/K/L whose levante-date basis differs from the
  document-date basis of the annex rows — the export-side counterpart
  is SV-FREP-FR-063. (LB-005; EVID-176; cross-ref SV-FREP-FR-063)

### 3.2 Canonical ISR cost/gasto quartet (Q/R/S/T) — owned here for the whole localization

- **SV-FREP-FR-079:** The system shall apply the Q/R/S/T period gate:
  the columns Q (*Tipo de Operación*, operation type), R
  (*Clasificación*, cost/expense classification), S (*Sector*) and T
  (*Tipo de Costo / Gasto*, cost/expense type) apply from the
  **Febrero-2024** period ("Las nuevas columnas 'Q, R, S, T' aplica a
  partir del periodo de Febrero 2024"); for periods before
  Febrero-2024 all four columns are emitted as "0" (the pre-gate "0"
  fill is inferred by parity with the R/S rule of
  `02_f07-annexes-sales.md` FR-051 — §V prints the gate but no
  explicit "0" instruction, OQ-002). This quartet — its gate, code
  lists (FR-080..083) and codes 8/9 (FR-084/085) — is the CANONICAL
  taxonomy for the whole localization: `06_f14-declaration.md` (the
  F-14 annex's S-V columns) references SV-FREP-FR-079..085 and shall
  not restate any of it. (LB-003; EVID-176; cross-ref
  SV-FREP-FR-051)
- **SV-FREP-FR-080:** The system shall classify every post-gate row's
  Q (TIPO DE OPERACIÓN) with the verbatim code list: **1 Gravada**
  (taxed) · **2 No Gravada** (not taxed) · **3 Excluido o no
  Constituye Renta** (excluded or not constituting income) ·
  **4 Mixta** (mixed — "costos y gastos que inciden en la actividad
  generadora de rentas gravadas, así como aquellos que afectan las
  rentas no gravadas ... Aplica también para los contribuyentes que
  gozan de Regímenes Especiales o beneficio fiscal": costs and
  expenses affecting both the taxed and non-taxed income-generating
  activity, also for special-regime or fiscal-benefit taxpayers) —
  the gravada/no-gravada/mixed semantics interface with the ISR
  necessary-cost gate and pro-rata allocator of
  `taxation/02_isr-deductions.md` (SV-TAX-FR-035/SV-TAX-FR-036) by
  classification id only; no ISR computation happens here.
  (LB-003; EVID-176; cross-ref SV-TAX-FR-035/036)
- **SV-FREP-FR-081:** The system shall classify every post-gate row's
  R (CLASIFICACIÓN) with the verbatim two-code list: **1 Costo**
  (cost) · **2 Gasto** (expense). (LB-003; EVID-176)
- **SV-FREP-FR-082:** The system shall classify every post-gate row's
  S (SECTOR) with the verbatim four-code list: **1 Industria**
  (industry) · **2 Comercio** (commerce) · **3 Agropecuaria**
  (agriculture-and-livestock) · **4 Servicios, Profesiones, Artes y
  Oficios** (services, professions, arts and trades).
  (LB-003; EVID-176)
- **SV-FREP-FR-083:** The system shall classify every post-gate row's
  T (TIPO DE COSTO / GASTO) with the verbatim seven-code list: **1
  Gastos de Venta sin Donación** (sales expenses without donation) ·
  **2 Gastos de Administración sin Donación** (administration
  expenses without donation) · **3 Gastos Financieros sin Donación**
  (financial expenses without donation) · **4 Costo Artículos
  Producidos/Comprados Importaciones/Internaciones** (cost of
  articles produced/purchased, imports/internations) · **5 Costo
  Artículos Producidos/Comprados Interno** (cost of articles
  produced/purchased, internal) · **6 Costos Indirectos de
  Fabricación** (indirect manufacturing costs) · **7 Mano de obra**
  (labor). (LB-003; EVID-176)
- **SV-FREP-FR-084:** The system shall apply the multi-annex
  deduplication code 8: when one and the same operation is reported
  in different annexes ("Cuando una misma operación es informada en
  diferentes anexos"), every row of that operation is classified
  with code **8 "Operaciones informadas en más de 1 anexo"**
  (operations reported in more than 1 annex) in the quartet columns —
  by parity with code 9's explicit all-four-columns rule (FR-085; the
  parity inference — OQ-007) —
  so that the values reported with that code are identified and NOT
  considered in the ISR declaration's cost-and-expense sums ("a
  efecto de identificar y no considerar en la suma de costos y gastos
  de la Declaración del Impuesto sobre la Renta"): the exclusion is a
  flag consumed by the F-14/F-910 family (`06_f14-declaration.md`,
  `07_codes-and-informs.md`); no ISR sum is computed here.
  (LB-004; EVID-176)
- **SV-FREP-FR-085:** The system shall apply code 9 for the
  non-deductible track: for *Instituciones Públicas* (public
  institutions), *Municipalidades* (municipalities) and taxpayers
  with operations non-deductible for ISR via cost or expense, ALL
  FOUR quartet columns Q/R/S/T are completed with the code **9**
  ("las 4 columnas anteriores (Q, R, S, T) deberán ser completadas
  con el código '9'") — the non-deductible determination interfaces
  with the Art. 29-A classifier of `taxation/02_isr-deductions.md`
  (SV-TAX-FR-052) by classification id only. (LB-004; EVID-176;
  cross-ref SV-TAX-FR-052)

### 3.3 Anexo 5 — Compras a Sujetos Excluidos (excluded-subject purchases)

- **SV-FREP-FR-086:** The system shall build Anexo 5 (*Compras a
  Sujetos Excluidos*, purchases from excluded subjects) with ONE ROW
  PER purchase document from an excluded subject — "documentos de
  compra a sujetos excluidos de acuerdo con lo establecido en el
  artículo 119 el Código Tributario" (CT Art. 119 anchor as printed;
  the excluded-subject definition and the retention-applicability
  rule are IVA-side matter of the future IVA taxation file, OQ-004)
  — whose totals feed casilla 66 (*Compras a sujetos excluidos*) per
  SV-FREP-FR-010; voided documents are excluded (anulados annex, 04
  file) and the purchase three-prior-period window applies
  (SV-FREP-FR-033). (LB-006; LB-008; LB-009; EVID-177; cross-ref
  SV-FREP-FR-010/033)
- **SV-FREP-FR-087:** The system shall emit every Anexo 5 row with
  the verbatim column model A-M of manual §VII — A TIPO DOC (1: "1
  NIT / 2 DUI / 3 OTRO DOCUMENTO") · B NIT/DUI/OTRO (14) · C NOMBRE
  · D FECHA · E SERIE · F NÚMERO · G MONTO · H MONTO DE LA RETENCIÓN
  IVA 13% · I TIPO DE OPERACIÓN · J CLASIFICACIÓN · K SECTOR ·
  L TIPO DE COSTO / GASTO · M NÚMERO DE ANEXO = 5 — in exactly this
  order, conforming to plantilla sheet "5". (LB-006; EVID-177)
- **SV-FREP-FR-088:** The system shall fill the supplier
  identification of Anexo 5 rows as: A = the supplier document type
  (1 NIT, 2 DUI, 3 OTRO DOCUMENTO), B = the supplier document number
  (14), C = the supplier name; the DUI-vs-NIT exclusive-or applies
  with its Enero-2022 gate (natural-person suppliers state either
  the DUI — A=2 — or the NIT — A=1 — never both; before Enero-2022
  the NIT is mandatory); the document identifier columns follow the
  canonical slot mapping of SV-FREP-FR-042/043 as PRINTED for this
  annex: E SERIE = the *sello de recepción* (reception seal) for DTE
  rows, F NÚMERO = the *código de generación* (generation code) for
  DTE rows — never restated beyond this printed confirmation.
  (LB-006; LB-008; EVID-177; cross-ref SV-FREP-FR-042/043/050)
- **SV-FREP-FR-089:** The system shall fill G (MONTO) with the
  operation amount and validate H (MONTO DE LA RETENCIÓN IVA 13%) as
  **13% of the operation amount when applicable** — "Corresponde al
  13% del monto de la operación cuando aplique": on rows where the
  13% IVA retention applies, H = 0.13 × G under the FR-027
  two-decimal discipline; the retention-applicability rule itself
  ("cuando aplique") is not printed in §VII and belongs to the
  IVA-side retention regime of the future IVA taxation file
  (OQ-004, 01 §7 OQ-004 kin — the F-07 side consumes the
  applicability determination, it does not define it).
  (LB-006; EVID-177; cross-ref SV-FREP-FR-027)
- **SV-FREP-FR-090:** The system shall apply the I-L quartet on
  Anexo 5 under the CANONICAL gate and code lists of FR-079..085
  (Febrero-2024 gate, "0" before; the Q/R/S/T lists verbatim, codes
  8/9 included) — manual §VII prints the quartet columns I-L under
  the same gate but NO separate code lists for this annex, so the
  same-lists assumption is recorded in OQ-003 (the twin of
  `02_f07-annexes-sales.md` OQ-004); the lists are referenced, never
  restated. (LB-006; EVID-177; cross-ref SV-FREP-FR-079..085)
- **SV-FREP-FR-091:** The system shall implement the post-*entero*
  credit re-entry path: the 13% IVA retentions recorded in column H
  generate *crédito fiscal* ONLY after the *entero* (remittance) of
  those retentions is recorded — "por las retenciones de 13% de IVA
  donde se genera crédito fiscal, posterior al entero de dichas
  retenciones IVA, dicho crédito fiscal se incorporará en la
  casilla 128 del formulario F-07" — implemented as a per-retention
  ledger linking each Anexo 5 row's H amount to its entero
  reference: the credit is incorporated into casilla 128 (*Crédito
  por Retención 13% IVA a terceros domiciliados (Art. 162 C.T)*,
  owned by SV-FREP-FR-012) in the declaration of the period in
  which the entero is recorded, and NEVER before — Anexo 5 feeds
  casilla 66 directly (FR-093) but casilla 128 ONLY through this
  re-entry gate (the strict period attribution — same period as the
  entero vs the following one — is not printed and is flagged
  OQ-005). (LB-007; EVID-177; cross-ref SV-FREP-FR-012)

### 3.4 Builder interfaces

- **SV-FREP-FR-092:** The system shall export and validate the Anexo
  3 and Anexo 5 files under the generic upload-format engine of
  `01_f07-declaration.md` §3.2 — every format and validation rule is
  owned by SV-FREP-FR-028..041 and consumed BY ID here (the
  purchase-side specializations: the THREE-prior-period window per
  Ley IVA Art. 63 — SV-FREP-FR-033 — and the last-column annex number
  = 3 / 5 — SV-FREP-FR-034), with the *declaración modificatoria*
  carryover of SV-FREP-FR-040 and the re-upload replace semantics of
  SV-FREP-FR-041 likewise consumed by id — no format rule is
  duplicated in this file. (LB-008; EVID-176; EVID-177; EVID-173;
  cross-ref SV-FREP-FR-028..041)
- **SV-FREP-FR-093:** The system shall feed the declaration casillas
  from the annex totals per the §4 wiring table (label-matched
  columns → casillas of `01_f07-declaration.md` FR-010/FR-011):
  Anexo 3 G → 65, H/I → 70, J → 80 with its crédito share of N →
  130, K → 76 with N-share → 126, L → 75 with N-share → 125, M → 77
  with N-share → 127, NC-row totals → 81/131; Anexo 5 G → 66; H
  enters NO purchase casilla — it reaches the declaration only
  through the FR-091 re-entry into casilla 128; no casilla is filled
  manually (SV-FREP-FR-038). (LB-009; EVID-176; EVID-177; EVID-179;
  cross-ref SV-FREP-FR-010/011/038)
- **SV-FREP-FR-094:** The system shall build both annexes' rows from
  POSTED purchase-side documents (vendor bills, vendor credit notes,
  vendor debit notes, customs/import entries — Odoo `account.move`),
  routing by document type and acquisition channel: local CCF/NC/ND
  purchase documents feed Anexo 3 (tipos 03/05/06), ZF/DPA-user
  local purchases through export invoices feed Anexo 3 tipo 11
  (FR-073), customs declarations and payment warrants feed Anexo 3
  tipos 12/13 (FR-074), and purchases from suppliers flagged as
  *sujetos excluidos* (excluded subjects) feed Anexo 5 (FR-086) — a
  document never feeds both annexes except when genuinely reported
  in more than one annex, in which case the code-8 rule of FR-084
  marks the duplication. (LB-001; LB-006; EVID-176; EVID-177)

## 4. Data Model

No CSV sidecars live next to this file: the column models, code lists
and wiring below are in-file §4 seed data. Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**Anexo 3 row model — l10n_sv.f07.annex3.row (seed structure; verbatim
from manual §V / plantilla sheet "3"):**

| Col | Header (Spanish, verbatim) | Length | Semantics | FR |
|-----|----------------------------|--------|-----------|----|
| A | FECHA | 10 | DD/MM/AAAA; current period or 3 prior periods (Ley IVA Art. 63) | FR-067, FR-068 |
| B | CLASE DE DOCUMENTO | 1 | 1 · 2 · 3 Otros · 4 DTE (annex-specific list) | FR-069 |
| C | TIPO DE DOCUMENTO | 2 | 03 CCF · 05 NC · 06 ND · 11 factura de exportación (ZF/DPA only) · 12 declaración de mercancías · 13 mandamiento de ingreso | FR-067, FR-073, FR-074 |
| D | NÚMERO DE DOCUMENTO | 100 | physical/other document number; DTE = código de generación (32; pre-Nov-2022 número de control 28) per FR-043 slot rule — OQ-001 | FR-070 |
| E | NIT/NRC PROVEEDOR | 14 | supplier NIT/NRC; Tesorería 06140108140066 for foreign 12/13; XOR with P (Enero-2022 gate) | FR-071, FR-072 |
| F | NOMBRE | sin límite impreso | supplier name (real foreign name kept on Tesorería rows) | FR-071, FR-072 |
| G | COMPRAS INTERNAS EXENTAS Y/O NO SUJETAS | 10 (§II) | exempt/non-subject internal purchases → casilla 65 | FR-075, FR-093 |
| H | INTERNACIONES EXENTAS Y/O NO SUJETAS | 10 (§II) | exempt/non-subject CA-region internations → casilla 70 (label-merged, OQ-006) | FR-075, FR-093 |
| I | IMPORTACIONES EXENTAS Y/O NO SUJETAS | 10 (§II) | exempt/non-subject imports → casilla 70 | FR-075, FR-093 |
| J | COMPRAS INTERNAS GRAVADAS | 10 (§II) | taxed internal purchases → casillas 80 + 130 | FR-075, FR-093 |
| K | INTERNACIONES GRAVADAS DE BIENES | 10 (§II) | taxed goods internations (dentro Región C.A.) → casillas 76 + 126 | FR-074, FR-075, FR-093 |
| L | IMPORTACIONES GRAVADAS DE BIENES | 10 (§II) | taxed goods imports (fuera Región C.A.) → casillas 75 + 125 | FR-074, FR-075, FR-093 |
| M | IMPORTACIONES GRAVADAS DE SERVICIOS | 10 (§II) | taxed service imports (tipo-13 mandamiento channel) → casillas 77 + 127 | FR-074, FR-075, FR-093 |
| N | CRÉDITO FISCAL | 10 (§II) | 13% × (J+K+L+M) validation; credit split by bucket → 125/126/127/130 | FR-076, FR-093 |
| O | TOTAL DE COMPRAS | 10 (§II) | G..M sum, ND+ / NC− semantics; not a casilla source (casilla 100 sums casillas) | FR-077 |
| P | DUI | 9 (family convention — not printed in §V, OQ-002) | supplier DUI; XOR with E (Enero-2022 gate) | FR-071 |
| Q | TIPO DE OPERACIÓN | 2 (by analogy, OQ-002) | canonical Q codes; "0" pre-Febrero-2024 | FR-079, FR-080 |
| R | CLASIFICACIÓN | 2 (as Q) | 1 costo · 2 gasto; "0" pre-gate | FR-079, FR-081 |
| S | SECTOR | 2 (as Q) | 1-4 sector codes; "0" pre-gate | FR-079, FR-082 |
| T | TIPO DE COSTO / GASTO | 2 (as Q) | 1-7 cost/expense types; "0" pre-gate | FR-079, FR-083 |
| U | NÚMERO DE ANEXO | 1 | literal 3 on every row | FR-068, FR-092 |

Length note: manual §V prints the lengths only for D (100) and E
(14); the A/B/C lengths (10/1/2) follow the Anexo 1 family convention
(02 §4), amount columns the generic §II 10-character format (01 §3.2);
P/Q/R/S/T lengths are not printed in §V — recorded by family
convention and analogy (OQ-002).

**Anexo 5 row model — l10n_sv.f07.annex5.row (seed structure; verbatim
from manual §VII / plantilla sheet "5"):**

| Col | Header (Spanish, verbatim) | Length | Semantics | FR |
|-----|----------------------------|--------|-----------|----|
| A | TIPO DOC | 1 | 1 NIT · 2 DUI · 3 otro documento | FR-087, FR-088 |
| B | NIT/DUI/OTRO | 14 | supplier document number; DUI-vs-NIT XOR (Enero-2022 gate) | FR-088 |
| C | NOMBRE | sin límite impreso | supplier (excluded subject) name | FR-087 |
| D | FECHA | 10 | DD/MM/AAAA; 3-prior-period window | FR-086, FR-092 |
| E | SERIE | plantilla | DTE = sello de recepción (40) per FR-043 | FR-088 |
| F | NÚMERO | plantilla | DTE = código de generación (32) per FR-043 | FR-088 |
| G | MONTO | 10 (§II) | operation amount → casilla 66 | FR-089, FR-093 |
| H | MONTO DE LA RETENCIÓN IVA 13% | 10 (§II) | 13% × G cuando aplique; enters the declaration only via FR-091 re-entry → casilla 128 | FR-089, FR-091 |
| I | TIPO DE OPERACIÓN | 2 | canonical Q codes (same-lists assumption — OQ-003); "0" pre-Febrero-2024 | FR-090 |
| J | CLASIFICACIÓN | 2 | canonical R codes | FR-090 |
| K | SECTOR | 2 | canonical S codes | FR-090 |
| L | TIPO DE COSTO / GASTO | 2 | canonical T codes | FR-090 |
| M | NÚMERO DE ANEXO | 1 | literal 5 on every row | FR-087, FR-092 |

**Canonical ISR cost/gasto quartet — l10n_sv.isr.costgasto.classification
(seed data; the ONE canonical statement — `06_f14-declaration.md` S-V
columns reference this table, never restate):**

| List | Values |
|------|--------|
| Q / I tipo de operación | 1 gravada · 2 no gravada · 3 excluido o no constituye renta · 4 mixta (costs/expenses affecting taxed and non-taxed activity; also special-regime/fiscal-benefit taxpayers) · **8** operaciones informadas en más de 1 anexo (dedup — excluded from ISR cost/gasto sums) · **9** instituciones públicas, municipalidades, operaciones no deducibles (all-four-columns fill) |
| R / J clasificación | 1 costo · 2 gasto (codes 8/9 override per FR-084/085) |
| S / K sector | 1 industria · 2 comercio · 3 agropecuaria · 4 servicios, profesiones, artes y oficios (codes 8/9 override) |
| T / L tipo de costo/gasto | 1 gastos de venta sin donación · 2 gastos de administración sin donación · 3 gastos financieros sin donación · 4 costo artículos producidos/comprados importaciones/internaciones · 5 costo artículos producidos/comprados interno · 6 costos indirectos de fabricación · 7 mano de obra (codes 8/9 override) |
| Gate | applies from Febrero-2024; "0" in all four columns for earlier periods |

**Column→casilla wiring (builder interface into 01 §3.1; label-matched
per FR-093):**

| Annex column | Casilla (label match) | Notes |
|--------------|----------------------|-------|
| Anexo 3 G | 65 compras internas exentas y/o no sujetas | |
| Anexo 3 H | 70 importaciones exentas y/o no sujetas | internaciones-exentas merged into 70 — one form casilla for both exempt channels (label-inferred, OQ-006) |
| Anexo 3 I | 70 | |
| Anexo 3 J | 80 compras internas gravadas + crédito 130 | crédito = N share on J |
| Anexo 3 K | 76 internaciones gravadas (dentro Región C.A.) + crédito 126 | |
| Anexo 3 L | 75 importaciones gravadas (fuera Región C.A.) + crédito 125 | |
| Anexo 3 M | 77 importaciones gravadas de servicios + crédito 127 | tipo-13 channel (OQ-006) |
| Anexo 3 N | 125/126/127/130 split by gravadas bucket | label-inferred split (OQ-006) |
| Anexo 3 NC rows (05) | 81 devoluciones sobre compras + crédito 131 | netting per 01 FR-011; ND rows add per FR-077 |
| Anexo 3 O | — (no casilla) | annex-side row total; casilla 100 sums casillas (01 FR-013) |
| Anexo 5 G | 66 compras a sujetos excluidos | |
| Anexo 5 H | — until entero → 128 | only via FR-091 re-entry; 128 owned by 01 FR-012 |

**Entities:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.f07.annex3.row (new) | declaration_id, source_move_id, date, clase, tipo, numero_documento, supplier_nit_nrc, supplier_name, supplier_dui, compras_int_exentas, internaciones_exentas, importaciones_exentas, compras_int_gravadas, internaciones_gravadas, importaciones_gravadas_bienes, importaciones_gravadas_servicios, credito_fiscal, total_compras, tipo_operacion, clasificacion, sector, tipo_costo_gasto, is_tesoreria_nit | m2o/char/monetary(2dp)/boolean | one row per purchase document (FR-067); buckets per FR-075; quartet = canonical codes or "0" per gate | FR-067..FR-083 |
| l10n_sv.f07.annex5.row (new) | declaration_id, source_move_id, supplier_tipo_doc, supplier_doc_number, supplier_name, date, serie, numero, monto, retencion_iva_13, tipo_operacion, clasificacion, sector, tipo_costo_gasto | m2o/char/monetary(2dp) | one row per excluido purchase; quartet per FR-090 | FR-086..FR-090 |
| l10n_sv.isr.costgasto.classification (new) | move_id, tipo_operacion, clasificacion, sector, tipo_costo_gasto, period_gate | char/select | the CANONICAL quartet defaults per move (product/account mapping), consumed by annex3/annex5 row builders AND by `06_f14-declaration.md` S-V — single source of truth | FR-079..FR-085 |
| l10n_sv.f07.retention.credit (new) | annex5_row_id, entero_ref, entero_date, credit_period, casilla_128_fed | m2o/char/date/boolean | per-retention re-entry ledger: H amount → entero reference → credit period → casilla 128 feed | FR-091 |
| res.partner (seed) | vat = 06140108140066 | char | Tesorería pseudo-supplier for foreign tipo-12/13 rows | FR-072 |
| l10n_sv.f07.aduanas.flag (01/02-file entity, reused) | kind: import_no_levante_link · import_levante_date_mismatch | select/text | import-side counterparts of the 02-file export flags | FR-078 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these
FRs touch DTE generation/transformation (the only architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`); FR-070/088
READ the sealed-DTE identifiers via the canonical mapping that file 02
owns. Model names are stable across Odoo 17/18/19/20; version-specific
behavior is recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-067 | odoo | l10n_sv.f07.annex3.row | granularity + tipo gate | Tipos 03/05/06/11/12/13 only; anulados routing to 04 file §3; 3-prior-period window (01 FR-033, Ley IVA 63) |
| FR-068 | odoo | l10n_sv.f07.annex3.row | column order A-U | Plantilla sheet "3" conformance; U = 3 on every row |
| FR-069 | odoo | l10n_sv.f07.annex3.row + l10n_latam.document.type | clase catalog | Clase 3 "Otros" admitted HERE only (§V prints 1/2/3 Otros/4 DTE; Anexo 1 = 1/2/4) |
| FR-070 | odoo | l10n_sv.f07.annex3.row + l10n_sv.f07.idmap (02 file, read) | D column fill | DTE = código de generación (32; pre-Nov-2022 número de control 28) per FR-043 slot rule — label-matched extension, OQ-001 |
| FR-071 | odoo | l10n_sv.f07.annex3.row + res.partner | supplier identification + XOR | D12: Enero-2022 gate; pre-2022 NIT/NRC mandatory; juridical → NIT always (mirror of 02 FR-050) |
| FR-072 | odoo | l10n_sv.f07.annex3.row + res.partner (seed) | Tesorería substitution | NIT 06140108140066 on tipos 12/13 only; real name kept in F |
| FR-073 | odoo | l10n_sv.f07.annex3.row + res.company | tipo-11 gate | ZF/DPA users only; Ley ZF Art. 25 anchor as printed; regime mechanics = special-regimes wave |
| FR-074 | odoo | l10n_sv.f07.annex3.row | customs channel routing | 12 → L/I (+K internations); 13 → M; label-matched (OQ-006) |
| FR-075 | odoo | l10n_sv.f07.annex3.row | G-M buckets | Channel × status routing; NC/ND positive rows; nils 0.00 (01 FR-030) |
| FR-076 | odoo | l10n_sv.f07.annex3.row | credito_fiscal validation | N = 0.13 × (J+K+L+M), 2dp; AC-001 |
| FR-077 | odoo | l10n_sv.f07.annex3.row | total_compras | G..M sum; ND+ / NC− totalization semantics; N excluded; AC-002 |
| FR-078 | odoo | l10n_sv.f07.aduanas.flag | import flags | Informational only (levante basis); no computation; mirror of 02 FR-063 |
| FR-079 | odoo | l10n_sv.isr.costgasto.classification | period gate | D12: Febrero-2024 gate, else "0" (inference flagged — OQ-002); CANONICAL — file 06 references SV-FREP-FR-079..085 |
| FR-080 | odoo | l10n_sv.isr.costgasto.classification | tipo_operacion (Q) | Codes 1/2/3/4 verbatim; 4 mixta ↔ SV-TAX-FR-036 pro-rata interface |
| FR-081 | odoo | l10n_sv.isr.costgasto.classification | clasificacion (R) | 1 costo · 2 gasto |
| FR-082 | odoo | l10n_sv.isr.costgasto.classification | sector (S) | 1 industria · 2 comercio · 3 agropecuaria · 4 servicios/profesiones/artes/oficios |
| FR-083 | odoo | l10n_sv.isr.costgasto.classification | tipo_costo_gasto (T) | Codes 1-7 verbatim (donation split on 1-3; T4 imports vs T5 internal) |
| FR-084 | odoo | l10n_sv.isr.costgasto.classification | code 8 dedup | Multi-annex duplication → 8 in all four columns (parity with 9); ISR sums exclude — consumed by file 06/07 |
| FR-085 | odoo | l10n_sv.isr.costgasto.classification | code 9 fill | Public institutions/municipalities/non-deductibles → 9 in all four columns; ↔ SV-TAX-FR-052 |
| FR-086 | odoo | l10n_sv.f07.annex5.row | granularity + anchor | CT 119 anchor as printed; excluido definition = future IVA file (OQ-004); feeds casilla 66 |
| FR-087 | odoo | l10n_sv.f07.annex5.row | column order A-M | Plantilla sheet "5" conformance; M = 5 on every row |
| FR-088 | odoo | l10n_sv.f07.annex5.row + res.partner | supplier identification | A tipo doc 1/2/3; XOR Enero-2022 gate; E/F = printed DTE mapping (sello/código) per FR-042/043 |
| FR-089 | odoo | l10n_sv.f07.annex5.row | G/H validation | H = 0.13 × G cuando aplique; applicability = future IVA file (OQ-004) |
| FR-090 | odoo | l10n_sv.f07.annex5.row | I-L quartet | Canonical lists via l10n_sv.isr.costgasto.classification; same-lists assumption (OQ-003) |
| FR-091 | odoo | l10n_sv.f07.retention.credit + l10n_sv.f07.casilla.value (01 file) | entero-gated re-entry | Credit → casilla 128 (01 FR-012) only after recorded entero; period attribution flagged — OQ-005; AC-007 |
| FR-092 | odoo | l10n_sv.f07.annex.upload (01 file's engine) | format inheritance | 01 FR-028..041 apply unchanged; purchase window = current + 3 prior (01 FR-033); modificatoria carryover annexes 3-12 (01 FR-040) |
| FR-093 | odoo | l10n_sv.f07.casilla.value (01 file) + §4 wiring table | totals interface | Bucket→casilla + N-split label-matched (OQ-006); no manual casilla fill (01 FR-038); AC-008 |
| FR-094 | odoo | account.move (purchase-side builder) | routing | Posted moves only; tipo + channel + excluido flag route Anexo 3 vs 5; code-8 marks genuine duplication |

Version-regime notes (D12): four dated gates live in or are referenced
by this file — the Febrero-2024 Q/R/S/T (and I-L) quartet gate
(FR-079/FR-090), the Enero-2022 DUI-vs-NIT XOR gate (FR-071/FR-088),
the Noviembre-2022 DTE identifier cutover (FR-070/FR-088, defined as
dated data in 02's FR-043) and the v14 annex vintage (manual ENERO
2025, plantilla v14 — operative structure; a future manual revision
re-seeds the column models). Each gate is stored as period-keyed
configuration so a future regime change re-dates without code change.
The canonical quartet FRs (SV-FREP-FR-079..085) are the single
statement of the ISR cost/gasto taxonomy: `06_f14-declaration.md`
(F-14 annex columns S-V) references them and must not restate the
lists, the gate, or codes 8/9. The filing due-day windows remain F12
territory (`08_filing-calendar.md`; SOQ-08) — no deadline behavior is
encoded here.

## 6. Acceptance Criteria

- **AC-001:** Given an Anexo 3 row with J=1,000.00, K=200.00, L=0.00,
  M=0.00 and G=100.00, H=0.00, I=0.00, then N reads **156.00**
  (13% × (1,000+200+0+0) — G/H/I never enter the base); given a row
  with J=100.55 only, then N reads **13.07** (two-decimal discipline);
  given a row whose stored N reads 150.00 against J=1,000.00, K=200.00,
  L=0.00, M=0.00, then the export surfaces a validation inconsistency
  on that row before any file is written (FR-076).
- **AC-002:** Given a CCF row with G=100.00 and J=1,000.00, then O =
  **1,100.00** (N excluded); given an ND row adjusting that purchase
  with J=50.00, then its O=50.00 and its totalization contribution is
  +50.00; given an NC row with J=30.00, then its own O reads 30.00
  (positive, no-negatives gate) while its contribution to the
  declaration is −30.00 through casillas 81/131 per 01 FR-011
  (FR-075, FR-077; cross-ref SV-FREP-FR-011/031).
- **AC-003:** Given a tipo-13 mandamiento row whose supplier is a
  foreign entity without a Salvadoran NIT, then E reads
  **06140108140066** (Tesorería pseudo-supplier) and F keeps the
  foreign supplier's real name; given a local CCF row (tipo 03) from
  the same foreign entity, then NO substitution occurs — the rule is
  tipo-12/13-only (FR-072).
- **AC-004:** Given Anexo 3 generated for period 01/2024, then every
  row's Q/R/S/T columns read `0`; given the same supplier documents in
  period 02/2024 with classification Q=4, R=1, S=2, T=5, then the
  columns read `4`, `1`, `2`, `5` (FR-079; OQ-002 inference).
- **AC-005:** Given one purchase reported both in Anexo 3 and in
  Anexo 5 of the same declaration, then BOTH rows carry `8` in all
  four quartet columns and the ISR-side cost/gasto sums exclude their
  values; given a purchase from a municipality, then its quartet
  reads `9`/`9`/`9`/`9` (FR-084, FR-085; OQ-007).
- **AC-006:** Given an Anexo 5 row for a 1,000.00 excluido purchase
  with the 13% retention applicable, then G=1,000.00 and H=**130.00**;
  given a DUI-carrying natural-person excluido supplier in period
  05/2025, then A=2 with B carrying the DUI; given a row whose
  supplier carries both DUI and NIT, then it is rejected by the XOR
  (FR-088, FR-089).
- **AC-007:** Given the 130.00 retention of AC-006 recorded in period
  03/2026 with its *entero* recorded on 10/04/2026, then casilla 128
  of the 03/2026 declaration reads 0.00 for that retention and
  casilla 128 of the 04/2026 declaration receives **130.00** (01
  FR-012 consumes the FR-091 ledger; strict attribution flagged —
  OQ-005); at no point does H enter casilla 66 (FR-091, FR-093).
- **AC-008:** Given annex 3 rows G=500.00, I=120.00, J=5,000.00,
  K=200.00, M=100.00 with their N shares, and an NC row J=50.00, then
  the declaration totals read 65=**500.00**, 70=**120.00**,
  80=**5,000.00**, 76=**200.00**, 77=**100.00**, credits
  130=**650.00**, 126=**26.00**, 127=**13.00**, 125=**0.00**, and
  81=**50.00** with 131=**6.50**; given Anexo 5 rows G=345.13 total,
  then casilla 66 = **345.13** with no manual casilla edit anywhere
  (FR-093; cross-ref SV-FREP-FR-010/011).
- **AC-009:** Given a tipo-11 row (Factura de Exportación) whose
  declarant is not a ZF/DPA user, then the row is rejected; given the
  same row under a ZF-flagged company, then it is accepted with its
  values classified into the local buckets J or G (national-territory
  purchase) — never into the import buckets (FR-073, FR-074).
- **AC-010:** Given import rows (buckets K/L) whose source documents
  carry no customs levante linkage, then the declaration surfaces
  Aduanas-awareness flags naming those rows, and NO casilla value is
  altered by the flag (informational only) (FR-078).
- **AC-011:** Given a *declaración modificatoria* (amended return) of
  period 04/2026 whose prior same-period declaration carried annexes
  3/5, then both annexes are prefilled from that prior declaration
  per 01 FR-040; given a re-upload of annex 3, then the carried rows
  are fully replaced, not merged (01 FR-041); and given a purchase
  document dated in N−3, then it is accepted, in N−4 or a future
  month rejected (01 FR-033) (FR-092).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Anexo 3 D-column DTE fill: manual §V prints a single NÚMERO DE DOCUMENTO column and NO per-column DTE mapping (unlike §VII, which prints SERIE=sello / NÚMERO=código for Anexo 5). FR-070 extends SV-FREP-FR-043's canonical NÚMERO-slot rule (código de generación post-Nov-2022; número de control before) to the single slot by label match. Confirm against a live MH upload or plantilla validation before certifying exports. | no | Takumi S3 | open |
| OQ-002 | Q/R/S/T pre-gate fill and lengths: §V prints the Febrero-2024 gate but, unlike §III's R/S rule, no explicit "deberá colocar '0'" instruction, and no column lengths. FR-079 encodes the "0" fill by parity with 02's FR-051 and 2-character codes by analogy (Anexo 1's R/S "máximo dos caracteres" text; its table's "10" was ruled a typo — 02 OQ-003 kin). P (DUI) length likewise unprinted in §V — 9 by the family convention (Anexo 1 Q). Confirm all three. | no | Takumi S3 | open |
| OQ-003 | Anexo 5 I-L code lists: manual §VII prints the quartet columns under the Feb-2024 gate but no separate code lists for this annex — FR-090 applies the canonical Q/R/S/T lists of FR-079..085 (same-lists assumption, the twin of 02's OQ-004 for Anexo 2 U/V). Confirm whether §VII carries its own lists in a manual revision. | no | Takumi S3 | open |
| OQ-004 | Anexo 5 H retention applicability ("Corresponde al 13% del monto de la operación cuando aplique"): WHEN the 13% IVA retention applies on an excluded-subject purchase (and the sujeto-excluido definition itself, CT 119 zone) is not printed in §VII — IVA-side retention-regime matter for the future IVA taxation file (01 §7 OQ-004 kin). FR-089 consumes the applicability determination; it does not define it. When the IVA file lands, the index task wires the cross-references. | no | Takumi S3 (index task) + future IVA taxation wave | open — ANSWERED by S9 13_iva-retentions (excluido 13% regime defined; SV-TAX-FR-313 zone) |
| OQ-005 | Post-entero re-entry period attribution: "posterior al entero ... se incorporará en la casilla 128" does not print whether the credit enters the declaration of the entero's OWN period or the FOLLOWING one. FR-091 encodes the entero's own period. Confirm against MH system behavior (or the annex-modification resolutions — 01 §7 OQ-001 kin). | no | Takumi S3 | open |
| OQ-006 | Wiring label-inferences: (a) H (internaciones exentas) and I (importaciones exentas) merge into the single casilla 70; (b) the N crédito splits into casillas 125/126/127/130 by gravadas bucket (K→126, L→125, M→127, J→130) — the manual prints one N column, the form four credit casillas; (c) the tipo-12→L/I and tipo-13→M channel associations (services have no merchandise declaration); (d) O is not wired to any casilla (casilla 100 sums casillas per 01 FR-013). All label-matched from LB-009's form labels; confirm against MH auto-totalization behavior. | no | Takumi S3 | open |
| OQ-007 | Code-8 all-four-columns fill: §V's code-8 note ("Cuando una misma operación es informada en diferentes anexos, ésta debe ser clasificada con el código 8 ...") prints no per-column fill rule — the explicit all-four-columns wording ("las 4 columnas anteriores (Q, R, S, T) deberán ser completadas con el código '9'") is printed for code 9 only (LB-004). FR-084 encodes code 8's fill in all four quartet columns by parity with code 9 (FR-085); AC-005 asserts it. Confirm against a live MH upload or the annex-modification resolutions (01 §7 OQ-001 kin). | no | Takumi S3 | open |
