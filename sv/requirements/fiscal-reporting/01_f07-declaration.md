# SV — Fiscal reporting — F-07 IVA declaration: casilla engine & annex upload

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for the F-07 *Declaración y
Pago del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de
Servicios* (monthly IVA declaration and payment form), version v14, in two
layers: the **declaration casilla engine** — the complete 77-row *casilla*
(form box) graph of the v14 form, from the identification block and the
Art. 74-A *disminución* (balance reduction) flag through the sales and
purchase buckets, the verbatim SUMA DE VENTAS/DEBITOS/COMPRAS/CRÉDITOS
arithmetic, the remanente/impuesto-determinado split, the retention credits
effected on and by the declarant, the D.L. 764-2014
*control-de-liquidez* (liquidity-control withholding) and FOVIAL credits,
the multas/intereses block and TOTAL A PAGAR, all denominated exclusively
in US dollars; and the **annex upload engine** — the machine format of the
F-07 annex upload files (semicolon-delimited CSV, all-Text cells,
≤25-character filename, two-decimal amounts, negative-value gate for
*anulados* (voided documents) only, DD/MM/AAAA period consistency,
three-prior-period acceptance windows, annex-number column, per-annex
structure validation), the upload-response handling (success summary and
line-numbered inconsistencies) and the *declaración modificatoria* (amended
return) flow with its annex carryover and clean-replace semantics.

It does **not** cover: the per-annex row/column models, the DTE identifier
mapping and the R/S Renta pair (`02_f07-annexes-sales.md` §3 — annexes 1-2);
the purchase annexes 3/5 including the post-*entero* (remittance) credit
re-entry mechanics into casilla 128 (`03_f07-annexes-purchases.md` §3); the
retention/perception annexes 4/6-12, the anulados/emitidos annex and the
invalidation-event feed (`04_f07-annexes-retentions-events.md` §3); the
fuel and dated-regime annexes 13-17 (`05_f07-annexes-special.md` §3); the
F-14 ISR declaration family (`06_f14-declaration.md`); the income-code
catalog and the F-910/F-915/F-930/F-935 informs (`07_codes-and-informs.md`);
the filing calendar and due-day windows (`08_filing-calendar.md` — SOQ-08);
the IVA computation proper (taxable base, 13% rate, deductibility,
pro-rata — Ley IVA Arts. 54-66 territory of a future IVA taxation file,
cited here via LB only); the ISR retention matrix (SV-TAX-FR-102..131 in
`taxation/04_isr-withholding.md` — a different tax; the IVA-side
retention rates are anchored here only as form labels, see OQ-004); and the
FOVIAL/COTRANS quantity-tax computation (special-regimes/taxation
coordination — casilla 525 is consumed here as a credit input only).

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and upload manuals ARE the
primary authority for declaration mechanics — 39_ (F-07 v14 form, footer
"Actualizado al 15/08/2025") + 34_ (Manual de Usuario para Carga de
Archivo de los Anexos, F-07 V14, ENERO 2025). Legal anchors printed on the
form/manual (CT Arts. 74-A/111/162, Ley IVA Art. 63, D.L. 764-2014
Art. 10.7) are cited as printed; no article text is invented beyond what
the form/evidence quotes. Manual pages are printed pages (printed page N =
PDF page N+2).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Formulario F-07 v14, encabezado + A. Identificación del Contribuyente: "PERÍODO TRIBUTARIO MES AÑO"; "Marque con una X si está Disminuyendo Saldo por Aplicación de Art. 74-A del C.T." (casilla 495); "Número de declaración que Modifica" (casilla 55; a printed "0" sits adjacent — form-sample digit); fields "1 NIT" (14), "3 NRC", "2 Apellido(s), Nombre(s) / Razón Social o Denominación" (22), "3 Actividad Económica Principal" (14), "4 Nombre Comercial" (9), "7 Teléfono" (16) | F-07 v14 form header and taxpayer identification block: tax period month/year; Art. 74-A CT balance-reduction checkbox (casilla 495); amended-declaration number (casilla 55); NIT, NRC, name/trade name, main economic activity, telephone with printed field lengths | `sv/sources/39_F07_v14_form_visual.pdf` | p.1 (EVID-179) |
| LB-002 | F-07 v14, B. Ventas de Bienes y/o Servicios Débitos, rows 5-23: "5 Ventas Internas Exentas 85 / 6 Ventas Internas No Sujetas 86 / 7 Ventas Gravadas por Cuenta de Terceros No Domiciliados Comprobante de Liquidación con C.C.F. 88 (Débitos ... Comprobante Crédito Fiscal 141) / 8 ... Comprobante de Liquidación con Facturas 89 (Débito ... con Factura 142) / 9 Exportaciones de Bienes (Fuera de Región Centroamericana) 90 / 10 ... (Región Centroamericana) 91 / 11 Exportaciones de Servicios 94 / 12 Ventas Internas Exentas No Sujetas a Proporcionalidad 92 / 13 Ventas Efectuadas a Zonas Francas y D.P.A. (Tasa Cero) 93 / 14 Ventas Internas Gravadas con Comprobante de Crédito Fiscal 95 (Débito ... 135) / 15 ... con Factura 96 (Débito ... 140) / 16 Ventas Gravadas de Combustible con tasas diferenciadas de IVA 586 (Débito Fiscal ... 587) / 17 Devoluciones, Rebajas, Descuentos u otras Deducciones sobre Ventas 97− (Débito ... 143−) / 18 Operaciones Gravadas con Comprobante de Liquidación 98 (Débito ... 144) / 19 Operaciones con Comprobante de Liquidación gravadas tasa 0 y/o exentas 99 / 20 Débito Proveniente de Crédito Negativo 146− / 21 Devoluciones ... por precios máximos de combustibles 552− (Débito ... 553)"; "22 SUMA DE VENTAS (Casillas 85+86+88+89+90+91+92+93+94+95+96+98+99+586-97-552) 105"; "SUMA DE DÉBITOS (Casillas 141+142+135+140+144+587-143-553) 150"; "23 Ventas Gravadas por Cuenta de Terceros Domiciliados (No debe incluirse en sumatoria de casilla 105) 108" | F-07 v14 Section B sales/debit rows 5-23 with the verbatim SUMA DE VENTAS (casilla 105) and SUMA DE DÉBITOS (casilla 150) formulas, and the third-party domiciled sales casilla 108 explicitly excluded from casilla 105 | `sv/sources/39_F07_v14_form_visual.pdf` | p.1 (EVID-179) |
| LB-003 | F-07 v14, C. Compra de Bienes y/o Servicios Créditos, rows 24-44: "24 Compras Internas Exentas y/o No sujetas 65 / 25 Compras a sujetos excluidos 66 / 26 Importaciones Exentas y/o No Sujetas 70 / 27 Importaciones Gravadas de Servicios 77 (Crédito por Importación de Servicios 127) / 28 Importaciones Gravadas de Mercancías (Fuera de Región C.A.) 75 (Crédito ... 125) / 29 Internaciones Gravadas de Mercancías (Dentro Región C.A.) 76 (Crédito ... 126) / 30 Compras Internas Gravadas 80 (Crédito ... 130) / 31 Compras Gravadas de Combustible con tasas diferenciadas de IVA 588 (Crédito ... 589) / 32 Devoluciones ... sobre Compras 81− (Crédito ... 131−) / 33 ... por precios máximos de combustibles 550− (Crédito ... 551−)"; OTROS CRÉDITOS: "34 Remanente de Crédito del Período anterior 110+ / 35 Reintegro Crédito Fiscal IVA por Exportaciones (en el período que se Notificó Resolución) 115− / 36 Crédito por Retención 13% IVA a terceros domiciliados (Art. 162 C.T) 128+ / 37 Crédito IVA por Proporcionalidad mensual (No deducible del Débito) 132− / 38 Crédito IVA por Ajuste de Proporcionalidad Anual (si resulta Superior al efectivamente Deducido) 133+ / 39 ... (si resulta Inferior ...) 134− / 40 Disminución de Saldo a Favor (Remanente de Crédito Fiscal) por aplicación del Art 74-A del C.T. Resolución No. 201 ... 200− / 41 Crédito Proveniente de Débito Negativo 151−"; "42 SUMA DE COMPRAS (Casillas 65+66+70+77+75+76+80+588-81-550) 100"; "SUMA DE CRÉDITOS (Casillas 127+125+126+130-131+589-551+110-115+128-132+133-134-200) 145"; "43 REMANENTE CRÉDITO PRÓXIMO PERÍODO (Si la Suma de los Créditos 'Casilla 145' es Mayor que la Suma de los Débitos 'Casilla 150') 155"; "44 IMPUESTO DETERMINADO (Si la Suma de los Débitos 'Casilla 150' es Mayor que la Suma de los Créditos 'Casilla 145') 160" | F-07 v14 Section C purchase/credit rows 24-44 with the verbatim SUMA DE COMPRAS (casilla 100) and SUMA DE CRÉDITOS (casilla 145) formulas, the "Art. 162 C.T" anchor printed on casilla 128, the Art. 74-A resolution field (201) on casilla 200, and the conditional remanente (155) / tax-determined (160) split | `sv/sources/39_F07_v14_form_visual.pdf` | p.1 (EVID-179) |
| LB-004 | F-07 v14, D. Retención, Percepción y Anticipo a Cuenta Efectuadas al Declarante, rows 45-60: "45 Anticipo a Cuenta IVA del 2% efectuada al Declarante 161 / 46 Retención IVA del 1% Efectuada al Declarante 162 / 47 Percepción IVA del 1% efectuada al Declarante 163 / 48 Excedente de Impuesto Período Anterior 164 / 49 Impuesto IVA por Operaciones según Declaración que Modifica 165 / 50 TOTAL ... (Casillas 161+162+163+164+165) 166"; "51 Disminución de Saldo por Aplicación del Art. 74-A del C.T. Resolucion No. 202 / 52 Percepción IVA del 1% ... 491 / 53 Retención IVA del 1% ... 492 / 54 Anticipo a Cuenta IVA del 2% ... 493 / 55 TOTAL DISMINUCIÓN ... (Casillas 491+492+493) 203"; "56 EXCEDENTE DEL IMPUESTO PARA PRÓXIMO PERÍODO A FAVOR DEL DECLARANTE (Casillas 166-160-203, Si Resultado es Positivo) 167"; "57 TOTAL DE IMPUESTO POR OPERACIONES DEL PERÍODO (Casillas 160-166+203, Si Resultado es Positivo) 168"; "58 Acreditación de Retención del Impuesto por Control de Liquidez Conforme Constancias de Retención (Según Inciso 7 de Art. 10 Decreto Legislativo N° 764/2014) 520−"; "59 Acreditación por FOVIAL 525−"; "60 TOTAL ... MENOS ACREDITACIÓN ... MENOS ACREDITACIÓN POR FOVIAL (Casillas 168-520-525) 521" | F-07 v14 Section D rows 45-60: credits effected on the declarant (161-166), the Art. 74-A reduction block (resolution 202; 491-493 → 203), the conditional excedente (167) and period tax (168), the D.L. 764-2014 Art. 10.7 liquidity-control retention credit (520), the FOVIAL credit (525) and casilla 521 = 168 − 520 − 525 | `sv/sources/39_F07_v14_form_visual.pdf` | p.2 (EVID-179) |
| LB-005 | F-07 v14, E. Montos Retenidos y Percibidos por el Declarante, rows 61-70: "61 Percepción IVA del 1% efectuada por el Declarante ... Percepción 1% 401 ... 169 / 62 Retención IVA del 1% Terceros Domiciliados ... Retención 1% 403 ... 170 / 63 Retención IVA del 13% Terceros Domiciliados ... Retención 13% 404 ... 172 / 64 Anticipo a Cuenta IVA del 2% ... Percepción 2% 405 ... 171 [the form prints the sub-label 'Percepción 2%' against the anticipo-2% row — carried as printed]"; "65 TOTAL ... (Casillas 169+170+171+172) 187"; "66 Retenciones y/o Percepciones del Período según Declaración que Modifica (Casillas 401+403+404+405) 188−"; "67 TOTAL ... (Casillas 187-188 Si el Resultado es Positivo) 190"; "68 EXCEDENTE POR PAGO INDEBIDO O EN EXCESO (SOLICITAR POR ESCRITO) 189"; "69 Acreditación de Reintegro de IVA Exportador Autorizado 523−"; "70 TOTAL A PAGAR ... (Casillas 190-523) 524"; F. Multas e Intereses, rows 71-77: "71 Multa Impuesto 194 / 72 Multa Percepción 1% 192 / 73 Multa Anticipo a Cuenta del 2% 199 / 74 Multa Retención 193 / 75 TOTAL MULTAS (Casillas 194+192+199+193) 195 / 76 Intereses 196 / 77 TOTAL A PAGAR (Casillas 521+524+195+196) 198" | F-07 v14 Sections E-F rows 61-77: amounts retained/perceived by the declarant with the amended-return anchors 401/403/404/405, totals 187/188/190, the excess-payment excedente 189, the exporter-refund credit 523 → 524, and the fines/interest block 192-199 → TOTAL A PAGAR 198 | `sv/sources/39_F07_v14_form_visual.pdf` | p.2 (EVID-179) |
| LB-006 | F-07 v14, pie de página: "SEÑOR CONTRIBUYENTE LA DECLARACIÓN DEBE ELABORARSE EXCLUSIVAMENTE EN DOLARES DE LOS ESTADOS UNIDOS DE AMÉRICA US$" (both pages) | F-07 v14 form footer: the declaration must be elaborated exclusively in US dollars | `sv/sources/39_F07_v14_form_visual.pdf` | pp.1-2 footers (EVID-179; verified 39_ txt) |
| LB-007 | Manual F-07 v14 §II: "Todas las casillas del archivo deben contener formato de Texto"; el archivo "debe guardarse con un nombre que no exceda de 25 caracteres y en seguida debe guardarse como archivo del tipo CSV (delimitado por comas)" [with the list separator configured to semicolon — the heading keeps MH's stock "comas" wording while the operative delimiter is the semicolon; OQ-002]; montos: "Numérico de 10 caracteres, incluir punto decimal (máximo dos decimales) y sin separador de miles ... En caso de ingresar valores con más de 2 decimales, el Sistema tomará únicamente 2. Sino hay operación de este tipo, debe colocar 0.00. No debe ingresar valores negativos"; fechas: "10 caracteres con la siguiente estructura DD/MM/AAAA, debe coincidir con el mes y año seleccionado en la pantalla de carga de archivo"; columnas "no deben contener encabezados o títulos ... ni celdas combinadas" | F-07 v14 upload manual §II general file format rules: all-Text cell typing, ≤25-char filename saved as CSV, amount format (10-char numeric, decimal point, max two decimals with system-side truncation, no thousands separator, 0.00 for nil, no negatives), DD/MM/AAAA dates matching the selected period, no headers/titles/merged cells | `sv/sources/34_F07_v14_manual.pdf` | §II pp.2-4 (EVID-173) |
| LB-008 | Manual F-07 v14 §IV/§V/§XXII: "Se podrán ingresar valores negativos únicamente para los documentos anulados/invalidados, de acuerdo a lo establecido en el artículo 111 del Código Tributario"; compras: "de acuerdo a lo establecido en el artículo 63 de la Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios, se pueden ingresar documentos de 3 periodos anteriores al que está declarando"; anulados 3-period window likewise "de acuerdo a lo establecido en el artículo 111 del Código Tributario" | F-07 v14 upload manual negative-value gate (voided/invalidated documents only, CT Art. 111) and the three-prior-period acceptance windows for purchases (Ley IVA Art. 63) and voided documents (CT Art. 111) | `sv/sources/34_F07_v14_manual.pdf` | §IV, §V, §XXII (EVID-173) |
| LB-009 | Manual F-07 v14 §XVI "Inconsistencias en el Archivo Cargado": "Si el archivo cargado tiene inconsistencias, el sistema le enviará mensaje y le detallará las mismas, indicándole las líneas en que se encuentra cada inconsistencia"; mensajes: "Debe cerciorarse que el archivo que está cargando es de la extensión .CSV"; "Debe cerciorarse que no haya dejado en blanco ninguna de las columnas relacionadas a los montos de las operaciones"; "Debe cerciorarse que, en la última columna, todas las líneas tengan el número del anexo que corresponde"; "Debe cerciorarse que está cargando el archivo que corresponde al detalle correspondiente, ya que cada anexo posee una estructura diferente" | F-07 v14 upload manual §XVI: on inconsistencies the system sends a message detailing each one with its line number; validation catalog = .CSV extension, no blank amount columns, annex number on the last column of every line, per-annex structure | `sv/sources/34_F07_v14_manual.pdf` | §XVI pp.51-53 (EVID-178) |
| LB-010 | Manual F-07 v14 §XVII "Procedimiento para Declaraciones Modificatorias": "Cuando se trate de declaraciones modificatorias, el sistema le mostrará la información de los anexos 3 al 12 de la declaración inmediata anterior del mismo periodo tributario. En el caso de los anexos: 1 'Ventas a Contribuyentes' y 2 'Ventas a Consumidor Final' para la presentación de declaraciones modificatorias será necesario realizar la carga de estos" | F-07 v14 upload manual §XVII amended-return procedure: annexes 3-12 are shown from the immediately preceding declaration for the same tax period; annexes 1-2 must be re-uploaded | `sv/sources/34_F07_v14_manual.pdf` | §XVII p.54 (EVID-178) |
| LB-011 | Manual F-07 v14 §III y notas de totalización por anexo: al cargar "se mostrará mensaje en el cual se dice 'Archivo subido correctamente'"; "se mostrará un resumen de la información cargada"; "el sistema complementará automáticamente, las casillas de ventas con los valores cargados en el archivo"; "La casilla 108 será totalizada automáticamente según los registros previamente cargados"; "la casilla 161 [162, 163, 169, 170, 171, 172] será totalizada automáticamente según los registros previamente cargados"; "el sistema complementará automáticamente, las casillas de las compras y/o ventas" | F-07 v14 upload manual: success response ("file uploaded correctly") plus a summary of the loaded information, and automatic complementation/totalization of the declaration casillas from the uploaded annex records — no manual casilla fill | `sv/sources/34_F07_v14_manual.pdf` | §III pp.5-6; §V p.17; §VI p.19; §VIII-§XIV (EVID-173; EVID-174; EVID-177) |

## 3. Functional Requirements

### 3.1 F-07 declaration engine: casilla graph and payment computation

- **SV-FREP-FR-001:** The system shall implement the F-07 *Declaración y
  Pago del Impuesto a la Transferencia de Bienes Muebles y a la Prestación
  de Servicios* (monthly IVA declaration and payment form) as one
  declaration object per taxpayer per *período tributario* (tax period,
  month/year), following form version **v14** (form footer "Actualizado al
  15/08/2025"; upload manual ENERO 2025 — D12 version regime: v14 is the
  operative current version), and shall elaborate every casilla amount
  EXCLUSIVELY in US dollars per the form footer "LA DECLARACIÓN DEBE
  ELABORARSE EXCLUSIVAMENTE EN DOLARES DE LOS ESTADOS UNIDOS DE AMÉRICA
  US$" — no other currency unit is stored or emitted on the declaration.
  (LB-001; LB-006; EVID-179)
- **SV-FREP-FR-002:** The system shall populate the identification block
  of every F-07 declaration from the taxpayer master data: NIT (14),
  NRC, *Apellido(s), Nombre(s) / Razón Social o Denominación*
  (surname(s)/trade name, 22), *Actividad Económica Principal* (main
  economic activity, 14), *Nombre Comercial* (commercial name, 9) and
  *Teléfono* (telephone, 16), with the printed field lengths enforced as
  maximums. (LB-001; EVID-179)
- **SV-FREP-FR-003:** The system shall record the declaration header
  fields that condition the computation: the Art. 74-A CT
  *disminución* (balance reduction) checkbox — "Marque con una X si está
  Disminuyendo Saldo por Aplicación de Art. 74-A del C.T.", casilla 495 —
  and, for *declaraciones modificatorias* (amended returns), the *Número
  de declaración que Modifica* (number of the declaration being amended,
  casilla 55) referencing the prior declaration of the same tax period
  (modificatoria flow per SV-FREP-FR-040). (LB-001; LB-010; EVID-179)
- **SV-FREP-FR-004:** The system shall compute the Section B sales value
  buckets from the uploaded annex totals: casillas 85 (*ventas internas
  exentas*, exempt internal sales), 86 (no sujetas, non-subject), 88/89
  (sales for the account of non-domiciled third parties with CL + CCF /
  CL + factura), 90/91 (goods exports outside / inside the Central
  American region), 94 (service exports), 92 (exempt internal sales not
  subject to proportionality), 93 (sales to zonas francas and D.P.A. at
  zero rate), 95 (taxed with CCF), 96 (taxed with factura) — annexes 1-2
  feed these casillas (row models owned by `02_f07-annexes-sales.md` §3).
  (LB-002; EVID-179)
- **SV-FREP-FR-005:** The system shall compute the fuel-regime sales
  casillas 586 (sales of fuel taxed at differentiated IVA rates) and 587
  (its fiscal debit), and the fuel price-cap return casillas 552
  (devoluciones/rebajas/descuentos over sales by fuel maximum prices,
  negative) and 553 (its debit), wired from annexes 13/14 whose row models
  and D12 validity windows (Decreto 321 from Mar-2022; Ley Especial
  Transitoria de precios máximos from Abr-2022) are owned by
  `05_f07-annexes-special.md` §3. (LB-002; EVID-179)
- **SV-FREP-FR-006:** The system shall compute the Section B debit
  companions: 141/142 (debits on non-domiciled third-party CL sales with
  CCF/factura), 135 (debit on CCF sales), 140 (debit on factura sales),
  144 (debit on CL-taxed operations), 587 (fuel debit, FR-005), and the
  deduction 143 (debits on returns/rebajas/discounts over sales — a
  positive magnitude subtracted by the FR-008 formula); plus the
  value-only rows 98 (CL-taxed operations) and 99 (CL operations at 0%
  and/or exempt), and row 146 (*débito proveniente de crédito negativo*,
  debit arising from negative credit), which the v14 form prints as a
  row but which is NOT a term of the printed SUMA DE DÉBITOS formula
  (FR-008): the system records the 146 value with NO downstream
  computation — its casilla wiring is not printed on the form and is
  flagged OQ-005. (LB-002; EVID-179)
- **SV-FREP-FR-007:** The system shall compute SUMA DE VENTAS casilla
  105 with the verbatim form arithmetic: **105 = 85 + 86 + 88 + 89 + 90 +
  91 + 92 + 93 + 94 + 95 + 96 + 98 + 99 + 586 − 97 − 552**.
  (LB-002; EVID-179)
- **SV-FREP-FR-008:** The system shall compute SUMA DE DÉBITOS casilla
  150 with the verbatim form arithmetic: **150 = 141 + 142 + 135 + 140 +
  144 + 587 − 143 − 553**. (LB-002; EVID-179)
- **SV-FREP-FR-009:** The system shall total casilla 108 (sales for the
  account of DOMICILED third parties, annex 4) separately and shall NEVER
  include it in casilla 105, per the printed exclusion "(No debe
  incluirse en sumatoria de casilla 105)". (LB-002; EVID-179; EVID-177)
- **SV-FREP-FR-010:** The system shall compute the Section C purchase
  buckets and their credit companions from the annex 3/5 totals: values
  65 (internal exempt and/or non-subject purchases), 66 (purchases from
  *sujetos excluidos*, excluded subjects — annex 5), 70 (exempt
  imports), 77 (taxed service imports), 75/76 (taxed merchandise imports
  outside / internations inside the CA region), 80 (taxed internal
  purchases), 588 (fuel purchases at differentiated rates); credits 127,
  125, 126, 130, 589 (row models owned by
  `03_f07-annexes-purchases.md` §3). (LB-003; EVID-179)
- **SV-FREP-FR-011:** The system shall compute the purchase-return
  casillas 81 (devoluciones/rebajas/descuentos over purchases) with its
  credit companion 131, and 550/551 (the fuel price-cap equivalents —
  annex 14 wiring per `05_f07-annexes-special.md` §3): each casilla
  value is entered and stored as a POSITIVE magnitude and the minus
  signs of the FR-013/FR-014 formulas perform the subtraction (− 81 −
  550 in casilla 100; − 131 − 551 in casilla 145) — the same sign
  convention as FR-019/FR-020/FR-024. (LB-003; EVID-179)
- **SV-FREP-FR-012:** The system shall compute the OTROS CRÉDITOS block:
  110 (*remanente de crédito del período anterior*, prior-period credit
  balance — fed by the FR-026 carryforward); 115 (*reintegro de crédito
  fiscal IVA por exportaciones* — exporter credit refund in the period
  the resolution is notified; a positive magnitude subtracted by the
  FR-014 formula); 128 (credit for the 13% IVA retention on domiciled
  third parties, "Art. 162 C.T" as printed — its post-*entero* (after
  remittance) re-entry mechanics are owned by
  `03_f07-annexes-purchases.md` §3 per EVID-177); 132/133/134 (IVA
  proportionality monthly credit not deductible from the debit /
  annual-proportionality adjustment if higher / if lower — computed by
  the Ley IVA Art. 66 pro-rata regime of the future IVA taxation file
  and consumed here as dated inputs; 132 and 134 are magnitudes the
  FR-014 formula subtracts, 133 one it adds); 200 (Art. 74-A CT balance
  reduction, resolution number 201 recorded; a positive magnitude
  subtracted by the FR-014 formula); and 151 (*crédito proveniente de
  débito negativo*, credit arising from negative debit), which the v14
  form prints as a row but which is NOT a term of the printed SUMA DE
  CRÉDITOS formula (FR-014): the system records the 151 value with NO
  downstream computation — its casilla wiring is not printed on the form
  and is flagged OQ-005. (LB-003; EVID-179; EVID-177)
- **SV-FREP-FR-013:** The system shall compute SUMA DE COMPRAS casilla
  100 with the verbatim form arithmetic: **100 = 65 + 66 + 70 + 77 + 75 +
  76 + 80 + 588 − 81 − 550**. (LB-003; EVID-179)
- **SV-FREP-FR-014:** The system shall compute SUMA DE CRÉDITOS casilla
  145 with the verbatim form arithmetic: **145 = 127 + 125 + 126 + 130 −
  131 + 589 − 551 + 110 − 115 + 128 − 132 + 133 − 134 − 200**.
  (LB-003; EVID-179)
- **SV-FREP-FR-015:** The system shall apply the credit/debit split:
  if 145 > 150 then *REMANENTE CRÉDITO PRÓXIMO PERÍODO* 155 = 145 − 150
  and IMPUESTO DETERMINADO 160 = 0.00; if 150 > 145 then 160 = 150 − 145
  and 155 = 0.00 (equality → both 0.00). (LB-003; EVID-179)
- **SV-FREP-FR-016:** The system shall compute Section D (retentions,
  perceptions and anticipos effected ON the declarant): 161 (2% IVA
  *anticipo a cuenta*, advance payment — annex 6), 162 (1% IVA retention
  — annex 7), 163 (1% IVA perception — annex 8), 164 (*excedente de
  impuesto período anterior*, prior-period tax surplus — fed by the
  FR-026 carryforward), 165 (IVA tax per operations according to the
  amended declaration), and TOTAL 166 with the verbatim arithmetic:
  **166 = 161 + 162 + 163 + 164 + 165** (annex row models owned by
  `04_f07-annexes-retentions-events.md` §3). (LB-004; EVID-179; EVID-177)
- **SV-FREP-FR-017:** The system shall compute the Art. 74-A CT
  *disminución* block only when the header flag 495 is set: 491
  (perception 1%), 492 (retention 1%), 493 (anticipo 2%) reduced by the
  Art. 74-A resolution, with the resolution number (202) recorded, and
  TOTAL **203 = 491 + 492 + 493** — 203 enters the 167/168 formulas as
  an addition to the period tax side. (LB-001; LB-004; EVID-179)
- **SV-FREP-FR-018:** The system shall apply the conditional Section D
  outcomes with the verbatim arithmetic: **167 = 166 − 160 − 203 if
  positive** (*EXCEDENTE DEL IMPUESTO PARA PRÓXIMO PERÍODO*, tax surplus
  for the next period in the declarant's favor), else 0.00; **168 = 160 −
  166 + 203 if positive** (TOTAL DE IMPUESTO POR OPERACIONES DEL
  PERÍODO), else 0.00 — exactly one of 167/168 is non-zero.
  (LB-004; EVID-179)
- **SV-FREP-FR-019:** The system shall record casilla 520, *Acreditación
  de Retención del Impuesto por Control de Liquidez Conforme Constancias
  de Retención* (credit for liquidity-control tax withholding per
  retention certificates, D.L. 764-2014 Art. 10 inciso 7 as printed on
  the form), backed by the retention *constancias* (certificate
  references stored): the casilla value is entered and stored as a
  POSITIVE magnitude and the minus sign of the FR-021 formula performs
  the subtraction (521 = 168 − 520 − 525) — the same sign convention as
  FR-020 and FR-024. (LB-004; EVID-179)
- **SV-FREP-FR-020:** The system shall record casilla 525, *Acreditación
  por FOVIAL* (FOVIAL credit — road-maintenance fund tax credit) as a
  POSITIVE magnitude subtracted by the FR-021 formula (521 = 168 − 520 −
  525), under the same sign convention as FR-019 and FR-024; its
  quantity-based computation basis is NOT defined by the form and
  remains a cross-wave interface (OQ-003). (LB-004; EVID-179)
- **SV-FREP-FR-021:** The system shall compute casilla 521 with the
  verbatim arithmetic: **521 = 168 − 520 − 525** (TOTAL DE IMPUESTO POR
  OPERACIONES DEL PERÍODO MENOS ACREDITACIÓN DEL IMPUESTO POR CONTROL DE
  LIQUIDEZ MENOS ACREDITACIÓN POR FOVIAL). (LB-004; EVID-179)
- **SV-FREP-FR-022:** The system shall compute Section E (amounts
  retained/perceived BY the declarant) from the annex 9-12 totals:
  169 (perception 1% effected by the declarant — annex 9), 170
  (retention 1% on domiciled third parties — annex 10), 172 (retention
  13% on domiciled third parties — annex 12), 171 (anticipo 2% — annex
  11), each carrying its *declaración-que-modifica* anchor 401/403/404/405
  (the form prints the 405 sub-label "Percepción 2%" against the
  anticipo-2% row — carried as printed); row models owned by
  `04_f07-annexes-retentions-events.md` §3. (LB-005; EVID-179; EVID-177)
- **SV-FREP-FR-023:** The system shall compute the Section E totals with
  the verbatim arithmetic: **187 = 169 + 170 + 171 + 172**; **188 =
  401 + 403 + 404 + 405** (retentions/perceptions of the period per the
  amended declaration, deducted); **190 = 187 − 188 if positive**
  (TOTAL DE IMPUESTO POR RETENCIONES Y PERCEPCIONES DEL PERÍODO), else
  0.00; and casilla 189, *EXCEDENTE POR PAGO INDEBIDO O EN EXCESO
  (SOLICITAR POR ESCRITO)* (excess/undue payment surplus — request in
  writing), surfaced as the informational mirror row for the 187 < 188
  case with the written-request flag set. (LB-005; EVID-179)
- **SV-FREP-FR-024:** The system shall record casilla 523, *Acreditación
  de Reintegro de IVA Exportador Autorizado* (authorized exporter IVA
  refund credit) as a POSITIVE magnitude — the same sign convention as
  FR-019/FR-020: the casilla value is entered and stored positive and
  the formula's minus sign performs the subtraction — and compute
  **524 = 190 − 523** (TOTAL A PAGAR DE IMPUESTO POR RETENCIONES Y
  PERCEPCIONES DEL PERÍODO POR EL DECLARANTE). (LB-005; EVID-179)
- **SV-FREP-FR-025:** The system shall compute the fines/interest block
  and the payment total with the verbatim arithmetic: multas (fines)
  194 (impuesto), 192 (percepción 1%), 199 (anticipo 2%), 193
  (retención); **195 = 194 + 192 + 199 + 193**; intereses (interest)
  196; and **TOTAL A PAGAR 198 = 521 + 524 + 195 + 196**. (LB-005;
  EVID-179)
- **SV-FREP-FR-026:** The system shall carry prior-period balances
  forward per the printed labels: casilla 155 of period N becomes
  casilla 110 (*Remanente de Crédito del Período anterior*) of period
  N+1, and casilla 167 of period N becomes casilla 164 (*Excedente de
  Impuesto Período Anterior*) of period N+1; a *declaración modificatoria*
  of period N recomputes N's balances and re-feeds N+1 only from the
  amended values. (LB-003; LB-004; EVID-179)
- **SV-FREP-FR-027:** The system shall compute and store every casilla
  amount to two decimals, applying each verbatim formula to two-decimal
  operands; no intermediate value beyond two decimals is emitted, and at
  export time any amount carrying more than two decimals is truncated
  (not rounded) per SV-FREP-FR-030 ("el Sistema tomará únicamente 2").
  (LB-003; LB-004; LB-005; LB-007; EVID-179)

### 3.2 F-07 annex upload engine: file format, validations, modificatorias

- **SV-FREP-FR-028:** The system shall export every F-07 annex upload
  file in the machine format of manual §II: comma-type CSV saved with the
  list separator configured as SEMICOLON (operative delimiter ";",
  per OQ-002), filename of at most 25 characters, .CSV extension, and
  every cell typed as Text ("Todas las casillas del archivo deben
  contener formato de Texto"). (LB-007; EVID-173)
- **SV-FREP-FR-029:** The system shall emit upload files with NO header
  or title rows and NO merged cells ("no deben contener encabezados o
  títulos ... ni celdas combinadas") — one data row per
  document/aggregate, columns exactly in the per-annex order defined by
  each annex's row model (files 02-05). (LB-007; EVID-173)
- **SV-FREP-FR-030:** The system shall format every amount cell as
  10-character numeric including the decimal point, maximum two decimals,
  no thousands separator, with system-side truncation to two decimals
  when a value carries more ("el Sistema tomará únicamente 2"), and
  0.00 for every nil operation ("Sino hay operación de este tipo, debe
  colocar 0.00"). (LB-007; EVID-173)
- **SV-FREP-FR-031:** The system shall enforce the negative-value gate:
  NO negative amounts are emitted or accepted in any annex except for
  *documentos anulados/invalidados* (voided/invalidated documents),
  which may carry negatives per CT Art. 111 as printed in the manual.
  (LB-007; LB-008; EVID-173)
- **SV-FREP-FR-032:** The system shall format every date cell as
  DD/MM/AAAA (10 characters) and validate period consistency: each row's
  date must match the month and year selected on the upload screen,
  except where FR-033's three-prior-period windows apply.
  (LB-007; EVID-173)
- **SV-FREP-FR-033:** The system shall accept rows dated up to THREE
  prior periods before the declared period — for purchase documents
  (annex 3/5 territory, per Ley IVA Art. 63 as printed in the manual)
  and for voided/invalidated documents (anulados annex, per CT Art. 111)
  — and shall reject any row dated outside the current period and its
  three predecessors for those annexes, or outside the current period
  for every other annex. (LB-008; EVID-173)
- **SV-FREP-FR-034:** The system shall place the annex number in the
  LAST column of every row of every annex file and shall validate that
  every line carries the annex number that corresponds to the file being
  processed ("en la última columna, todas las líneas tengan el número del
  anexo que corresponde"). (LB-009; EVID-178)
- **SV-FREP-FR-035:** The system shall validate the per-annex structure
  of every uploaded file ("cada anexo posee una estructura diferente"):
  a file whose column structure does not match the target annex is
  rejected with the corresponding §XVI message, before any row-level
  processing. (LB-009; EVID-178)
- **SV-FREP-FR-036:** The system shall reject any file leaving blank an
  amount column related to the operation amounts ("no haya dejado en
  blanco ninguna de las columnas relacionadas a los montos de las
  operaciones") — nil amounts are expressed as 0.00 per FR-030, never as
  an empty cell. (LB-009; EVID-178)
- **SV-FREP-FR-037:** The system shall handle the upload response per
  manual §III: on success, surface the "Archivo subido correctamente"
  (file uploaded correctly) message and a *resumen* (summary) of the
  loaded information per annex. (LB-011; EVID-173; EVID-174)
- **SV-FREP-FR-038:** The system shall auto-total the declaration
  casillas from the uploaded annex records — the sales/purchase casillas
  (FR-004/FR-006/FR-010), casilla 108, casillas 161/162/163 and
  169/170/171/172 — with NO manual casilla fill ("el sistema
  complementará automáticamente, las casillas ... según los registros
  previamente cargados"). (LB-011; EVID-173; EVID-177)
- **SV-FREP-FR-039:** The system shall report file inconsistencies the
  way manual §XVI prescribes: a message detailing EACH inconsistency
  with the LINE number where it occurs, drawn from the validation
  catalog (extension .CSV — FR-028; blank amount columns — FR-036;
  missing/mismatched annex number — FR-034; wrong structure — FR-035;
  date/period mismatch — FR-032/FR-033; negative outside anulados —
  FR-031). (LB-009; EVID-178)
- **SV-FREP-FR-040:** The system shall implement the *declaración
  modificatoria* flow: when amending a period, the information of
  annexes 3 to 12 is carried over from the IMMEDIATELY PRIOR declaration
  of the same tax period, while annexes 1 (Ventas a Contribuyentes) and
  2 (Ventas a Consumidor Final) MUST be re-uploaded; the amendment
  records the *Número de declaración que Modifica* (FR-003) and feeds
  the modificatoria anchors 165, 188 (FR-016/FR-023) from the prior
  declaration's values. (LB-010; EVID-178)
- **SV-FREP-FR-041:** The system shall apply clean-replace (*limpiar y
  reemplazar*) semantics on every annex upload: a newly uploaded annex
  file fully REPLACES the previously loaded content of that annex for
  the period — rows are never merged or appended across uploads of the
  same annex; the modificatoria carryover of FR-040 is likewise
  superseded per annex by that annex's re-upload. (LB-010; LB-011;
  EVID-178)

## 4. Data Model

No CSV sidecars live next to this file: both seed tables below are
in-file §4 data (the casilla↔source map and the upload-format spec).
Layer semantics: Odoo-side computation/bookkeeping data only (wave
default `odoo`; see §5).

**Casilla graph — l10n_sv.f07.casilla.spec (seed data, v14; complete
row/casilla map with sign, role and source):**

| Form section / rows | Casilla (sign in formula) | Label (Spanish, abbreviated) | Role | Source | FR |
|---------------------|---------------------------|------------------------------|------|--------|----|
| Header | 495 · 55 | Art. 74-A flag X · nº declaración que modifica | input_flag · input_ref | res.partner/res.company + prior declaration | FR-003 |
| A. Identificación | NIT 14 · NRC · razón 22 · actividad 14 · n. comercial 9 · teléfono 16 | identification fields | input_master | taxpayer master data | FR-002 |
| B rows 5-6 | 85+ · 86+ | ventas internas exentas · no sujetas | annex_total | annexes 1-2 (file 02) | FR-004 |
| B rows 7-8 | 88+ · 89+ · 141+ · 142+ | terceros no domiciliados CL c/CCF · CL c/factura + débitos | annex_total | annexes 1-2 (file 02) | FR-004, FR-006 |
| B rows 9-13 | 90+ · 91+ · 94+ · 92+ · 93+ | exportaciones fuera/dentro CA · servicios · exentas no sujetas a proporcionalidad · ZF/DPA tasa cero | annex_total | annexes 1-2 (file 02) | FR-004 |
| B rows 14-15 | 95+ · 96+ · 135+ · 140+ | gravadas con CCF · con factura + débitos | annex_total | annexes 1-2 (file 02) | FR-004, FR-006 |
| B row 16 | 586+ · 587+ | combustible tasas diferenciadas + débito | annex_total | annex 13 wiring (file 05; D12 Decreto 321 Mar-2022+) | FR-005 |
| B row 17 | 97− · 143− | devoluciones sobre ventas + débito | annex_total | annexes 1-2 NC rows (file 02) | FR-006 |
| B rows 18-20 | 98+ · 99+ · 146− | operaciones CL gravadas · CL tasa 0/exentas · débito de crédito negativo | annex_total · input_unwired | annexes 1/4 · wiring not printed — OQ-005 | FR-006 |
| B row 21 | 552− · 553 | devoluciones precios máximos combustibles + débito | annex_total | annex 14 wiring (file 05; D12 Abr-2022+) | FR-005 |
| B row 22 | 105 · 150 | SUMA DE VENTAS · SUMA DE DÉBITOS | derived | verbatim formulas FR-007/FR-008 | FR-007, FR-008 |
| B row 23 | 108 | terceros domiciliados (EXCLUDED from 105) | annex_total | annex 4 (file 04) | FR-009 |
| C rows 24-31 | 65+ · 66+ · 70+ · 77+ · 75+ · 76+ · 80+ · 588+ · 127+ · 125+ · 126+ · 130+ · 589+ | compras/internaciones/importaciones buckets + créditos | annex_total | annexes 3/5 (file 03); 588/589 annex 13 (file 05) | FR-010 |
| C rows 32-33 | 81− · 131− · 550− · 551− | devoluciones sobre compras + precios-máximos pares | annex_total | annex 3 NC rows (file 03); 550/551 annex 14 (file 05) | FR-011 |
| Otros créditos 34 | 110+ | remanente período anterior | carryforward | 155 of prior period | FR-012, FR-026 |
| Otros créditos 35 | 115− | reintegro crédito IVA exportaciones | input_event | DGII resolution notification | FR-012 |
| Otros créditos 36 | 128+ | retención 13% IVA terceros domiciliados (Art. 162 C.T.) | input_event | annex 5 post-entero re-entry (file 03; EVID-177) | FR-012 |
| Otros créditos 37-39 | 132− · 133+ · 134− | proporcionalidad mensual · ajuste anual sup. · inf. | input_computed | Ley IVA Art. 66 pro-rata (future IVA taxation file) | FR-012 |
| Otros créditos 40-41 | 200− · 151− | disminución Art. 74-A (resolución 201) · crédito de débito negativo | input_event · input_unwired | Art. 74-A resolution · wiring not printed — OQ-005 | FR-012 |
| C row 42 | 100 · 145 | SUMA DE COMPRAS · SUMA DE CRÉDITOS | derived | verbatim formulas FR-013/FR-014 | FR-013, FR-014 |
| C rows 43-44 | 155 · 160 | remanente próximo período · impuesto determinado | derived_conditional | FR-015 | FR-015 |
| D rows 45-49 | 161+ · 162+ · 163+ · 164+ · 165+ | anticipo 2% · retención 1% · percepción 1% al declarante · excedente anterior · según declaración que modifica | annex_total · carryforward · input_ref | annexes 6-8 (file 04) · 167 prior period · prior declaration | FR-016 |
| D row 50 | 166 | TOTAL retención/percepción/anticipo a favor | derived | 161+162+163+164+165 | FR-016 |
| D rows 51-55 | 491+ · 492+ · 493+ · 203 | disminución Art. 74-A block (resolución 202) + total | input_event · derived | Art. 74-A resolutions; flag 495 required | FR-017 |
| D rows 56-57 | 167 · 168 | excedente próximo período · total impuesto operaciones del período | derived_conditional | 166−160−203 / 160−166+203 (positive) | FR-018 |
| D rows 58-60 | 520− · 525− · 521 | control de liquidez D.L. 764-2014 (constancias) · FOVIAL · total | input_event · derived | retention constancias · FOVIAL feed (OQ-003) · 168−520−525 | FR-019, FR-020, FR-021 |
| E rows 61-64 | 169+ · 170+ · 172+ · 171+ · 401 · 403 · 404 · 405 | percepción 1% · retención 1% · retención 13% · anticipo 2% por el declarante + anchors declaración-que-modifica | annex_total · input_ref | annexes 9-12 (file 04) · prior declaration | FR-022 |
| E rows 65-68 | 187 · 188− · 190 · 189 | total por el declarante · según declaración que modifica · total del período · excedente pago indebido (escrito) | derived · derived · derived_conditional · informational | 169+170+171+172 · 401+403+404+405 · 187−188 positive · mirror case | FR-023 |
| E rows 69-70 | 523− · 524 | reintegro IVA exportador autorizado · total a pagar retenciones | input_event · derived | DGII authorization · 190−523 | FR-024 |
| F rows 71-77 | 194+ · 192+ · 199+ · 193+ · 195 · 196+ · 198 | multas impuesto/percepción/anticipo/retención · total multas · intereses · TOTAL A PAGAR | input_event · derived | sanction/interest entries · 194+192+199+193 · 521+524+195+196 | FR-025 |

**Declaration and upload entities:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv.f07.declaration (new) | company_id, period_month, period_year, form_version, is_amendment, amends_declaration_id, flag_74a (495), declaration_no_modifies (55) | m2o/int/boolean/char | form_version default f07_v14; amends_declaration_id → prior declaration same period | FR-001, FR-003, FR-040 |
| l10n_sv.f07.casilla.value (new) | declaration_id, casilla_spec_id, amount | m2o/monetary(2dp) | one row per populated casilla; USD only | FR-001, FR-027 |
| l10n_sv.f07.casilla.spec (new) | form_version, section, row_no, casilla, label_es, sign, role, formula, source_ref | char/select | role: annex_total · derived · derived_conditional · carryforward · input_event · input_computed · input_master · input_flag · input_unwired · informational (input_unwired = printed row with no downstream formula term — OQ-005); seeded from the in-file table above | FR-004..FR-025 |
| l10n_sv.f07.annex.upload (new) | declaration_id, annex_no, filename, file, status, uploaded_at, response_summary | int/char(≤25)/binary/select | annex_no 1-14; status: draft · validated · rejected · accepted; response_summary = resumen per FR-037 | FR-028, FR-037, FR-041 |
| l10n_sv.f07.annex.upload.error (new) | upload_id, line_no, validation_code, message | int/select/text | validation_code: extension_csv · blank_amount · annex_number · structure · date_period · window_3periods · negative_gate | FR-039 |
| l10n_sv.f07.upload.format.spec (new) | annex_no, delimiter, cell_type, amount_rule, date_rule, negative_policy, period_window | char/select | seeded from the in-file format table below | FR-028..FR-036 |

**Upload-format spec — l10n_sv.f07.upload.format.spec (seed data; common
profile + per-annex windows):**

| Annex (no.) | Delimiter | Cell typing | Amounts | Dates | Negatives | Period window |
|-------------|-----------|-------------|---------|-------|-----------|---------------|
| 1, 2 (sales) | ; | Text | 10-char numeric, 2 decimals (truncate), 0.00 nil, no thousands sep | DD/MM/AAAA | anulados only (CT 111 — rows live in the anulados annex, file 04) | current period only |
| 3, 5 (purchases) | ; | Text | same | DD/MM/AAAA | no | current + 3 prior periods (Ley IVA Art. 63) |
| 4, 6-12 (retentions/perceptions) | ; | Text | same | DD/MM/AAAA | no | current period only |
| anulados/extraviados annex (file 04) | ; | Text | same | DD/MM/AAAA | YES — anulados/invalidados per CT 111 | current + 3 prior periods (CT 111) |
| 13-17 (special, file 05) | ; (13 = manual entry, no file) | Text | same | DD/MM/AAAA | per regime | per D12 regime window |

Every annex file: last column = annex number on every row (FR-034); no
headers/merged cells (FR-029); filename ≤ 25 characters + .CSV extension
(FR-028).

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these FRs
touch DTE generation/transformation (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`). Model names are
stable across Odoo 17/18/19/20; version-specific behavior is recorded per
row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | odoo | l10n_sv.f07.declaration | period, form_version, currency | Version regime (D12): v14 operative (39_ footer 15/08/2025; 34_ manual ENERO 2025); USD-only per LB-006 |
| FR-002 | odoo | l10n_sv.f07.declaration + res.partner/res.company | identification snapshot | Printed max lengths NIT 14/NRC/razón 22/actividad 14/nombre comercial 9/teléfono 16; actividad sourced from the fiscal actividad code |
| FR-003 | odoo | l10n_sv.f07.declaration | flag_74a, amends_declaration_id, declaration_no_modifies | Flag 495 gates FR-017; amendment number feeds FR-040 |
| FR-004 | odoo | l10n_sv.f07.casilla.value + l10n_sv.f07.annex.upload | casillas 85-96 | Annex totals from annexes 1-2 (02_f07-annexes-sales.md §3 owns row builders) |
| FR-005 | odoo | l10n_sv.f07.casilla.value | 586/587, 552/553 | D12: Decreto 321 Mar-2022+ and precios-máximos Abr-2022+ windows owned by 05_f07-annexes-special.md §3 |
| FR-006 | odoo | l10n_sv.f07.casilla.value | 141/142/135/140/144/587/143, 98/99/146 | 146 recorded as printed (row mark −); NOT a term of the 150 formula — role input_unwired, no downstream wiring (OQ-005) |
| FR-007 | odoo | l10n_sv.f07.casilla.value | 105 | Verbatim formula; AC-001 arithmetic spot-check |
| FR-008 | odoo | l10n_sv.f07.casilla.value | 150 | Verbatim formula; AC-002 |
| FR-009 | odoo | l10n_sv.f07.casilla.value | 108 | Hard exclusion from 105; annex 4 feed (04 file §3) |
| FR-010 | odoo | l10n_sv.f07.casilla.value | 65-80/588 + 127-130/589 | Annexes 3/5 feeds (03 file §3); 588/589 annex 13 (05 file §3) |
| FR-011 | odoo | l10n_sv.f07.casilla.value | 81/131, 550/551 | 550/551 annex 14 wiring (05 file §3) |
| FR-012 | odoo | l10n_sv.f07.casilla.value | 110/115/128/132-134/200/151 | 128 = post-entero re-entry (03 file §3; EVID-177); 132-134 = Ley IVA Art. 66 pro-rata inputs (future IVA taxation file — OQ-004 kin); 200 records resolución 201; 151 recorded as printed — NOT in the 145 formula, role input_unwired (OQ-005) |
| FR-013 | odoo | l10n_sv.f07.casilla.value | 100 | Verbatim formula; AC-003 |
| FR-014 | odoo | l10n_sv.f07.casilla.value | 145 | Verbatim formula; AC-003 |
| FR-015 | odoo | l10n_sv.f07.casilla.value | 155/160 | Conditional split; AC-004 |
| FR-016 | odoo | l10n_sv.f07.casilla.value | 161-166 | Annexes 6-8 feeds (04 file §3); 164 = prior 167 (FR-026); 165 from amended declaration |
| FR-017 | odoo | l10n_sv.f07.casilla.value + l10n_sv.f07.declaration | 491-493 → 203 | Gated by flag 495; resolución 202 stored; CT Art. 74-A anchor as printed |
| FR-018 | odoo | l10n_sv.f07.casilla.value | 167/168 | Exactly one non-zero; AC-005 |
| FR-019 | odoo | l10n_sv.f07.casilla.value | 520 + constancia refs | D.L. 764-2014 Art. 10.7 anchor as printed; certificate references required; positive-magnitude convention — FR-021's minus sign subtracts |
| FR-020 | odoo | l10n_sv.f07.casilla.value | 525 | Computation basis open — OQ-003 (FOVIAL quantity-tax interplay, 31_ pointer); positive-magnitude convention as FR-019 |
| FR-021 | odoo | l10n_sv.f07.casilla.value | 521 | Verbatim formula; AC-005 chain |
| FR-022 | odoo | l10n_sv.f07.casilla.value | 169-172 + 401/403/404/405 | Annexes 9-12 feeds (04 file §3); [405 sub-label "Percepción 2%" carried as printed] |
| FR-023 | odoo | l10n_sv.f07.casilla.value | 187/188/190/189 | 189 informational mirror with written-request flag |
| FR-024 | odoo | l10n_sv.f07.casilla.value | 523/524 | 523 positive magnitude (FR-019 sign convention); 524 = 190 − 523 |
| FR-025 | odoo | l10n_sv.f07.casilla.value | 192-196/198 | Payment total chain; AC-005 |
| FR-026 | odoo | l10n_sv.f07.declaration (compute) | carryforward job | 155→110, 167→164; amendment re-feeds from amended values |
| FR-027 | odoo | l10n_sv.f07.casilla.value | 2dp discipline | Consistent with FR-030 upload truncation |
| FR-028 | odoo | l10n_sv.f07.annex.upload + l10n_sv.f07.upload.format.spec | export/import codec | Semicolon delimiter operative (OQ-002); Text-typed cells; ≤25-char filename |
| FR-029 | odoo | l10n_sv.f07.upload.format.spec | row/column emission | Column order per annex row models (files 02-05) |
| FR-030 | odoo | l10n_sv.f07.upload.format.spec | amount formatter | Truncation (not rounding) beyond 2 decimals; 0.00 nil; AC-006/AC-013 |
| FR-031 | odoo | l10n_sv.f07.annex.upload.error (negative_gate) | validation | CT 111 exception; AC-010 |
| FR-032 | odoo | l10n_sv.f07.annex.upload.error (date_period) | validation | DD/MM/AAAA vs selected month/year; AC-009 |
| FR-033 | odoo | l10n_sv.f07.annex.upload.error (window_3periods) | validation | Ley IVA 63 (compras) / CT 111 (anulados) windows; AC-011 |
| FR-034 | odoo | l10n_sv.f07.annex.upload.error (annex_number) | validation | Last-column rule; AC-016 |
| FR-035 | odoo | l10n_sv.f07.annex.upload.error (structure) | validation | Per-annex structure pre-check |
| FR-036 | odoo | l10n_sv.f07.annex.upload.error (blank_amount) | validation | Nil = 0.00 never blank; AC-016 |
| FR-037 | odoo | l10n_sv.f07.annex.upload | status/response_summary | "Archivo subido correctamente" + resumen |
| FR-038 | odoo | l10n_sv.f07.casilla.value (compute) | auto-total | No manual fill for annex-fed casillas |
| FR-039 | odoo | l10n_sv.f07.annex.upload.error | line_no + catalog | Line-numbered inconsistencies |
| FR-040 | odoo | l10n_sv.f07.declaration (amendment wizard) | carryover + forced re-upload | Annexes 3-12 carryover; 1-2 mandatory upload; AC-014 |
| FR-041 | odoo | l10n_sv.f07.annex.upload (replace semantics) | full replace per annex | limpiar-replace; no merge across uploads |

Version-regime notes (D12): FR-001 records the F-07 v14 vintage (form
"Actualizado al 15/08/2025", manual ENERO 2025 — current); the casilla
spec is seeded per form_version so a future v15 re-seeds without code
change. FR-005/FR-011 fuel casillas (586-589, 550-553) are gated by the
fuel-regime validity windows owned by `05_f07-annexes-special.md` §3
(Decreto 321 from Mar-2022; Ley Especial Transitoria from Abr-2022).
FR-017's Art. 74-A and FR-019's D.L. 764-2014 Art. 10.7 mechanics carry
no in-corpus cutover dates — treated as standing rules as printed on the
v14 form; any future reform re-dates via the casilla spec. The R/S and
Q-T column period gates belong to files 02/03 (not this file). The
filing due-day windows are F12 territory (`08_filing-calendar.md`;
SOQ-08) — no deadline behavior is encoded here.

## 6. Acceptance Criteria

- **AC-001:** Given annex-fed sales casillas 85=1,000.00, 86=200.00,
  88=50.00, 89=0.00, 90=300.00, 91=150.00, 92=0.00, 93=0.00, 94=75.00,
  95=10,000.00, 96=500.00, 98=0.00, 99=0.00, 586=0.00, 97=100.00 and
  552=0.00, then 105 = 1,000+200+50+0+300+150+0+0+75+10,000+500+0+0+0−100−0
  = **12,175.00** (FR-007).
- **AC-002:** Given débito casillas 141=0.00, 142=0.00, 135=1,300.00,
  140=43.48, 144=0.00, 587=0.00, 143=13.00 and 553=0.00, then 150 =
  0+0+1,300+43.48+0+0−13−0 = **1,330.48**; given additionally 146=5.00,
  then 150 remains **1,330.48** — 146 is not a term of the printed
  formula (recorded, unwired — OQ-005) (FR-006, FR-008).
- **AC-003:** Given 65=500.00, 66=345.13, 70=0.00, 77=100.00, 75=200.00,
  76=0.00, 80=5,000.00, 588=0.00, 81=50.00, 550=0.00, then 100 =
  500+345.13+0+100+200+0+5,000+0−50−0 = **6,095.13**; and given
  127=13.00, 125=26.00, 126=0.00, 130=650.00, 131=6.50, 589=0.00,
  551=0.00, 110=1,000.00, 115=0.00, 128=130.00, 132=20.00, 133=0.00,
  134=0.00, 200=0.00, then 145 =
  13+26+0+650−6.50+0−0+1,000−0+130−20+0−0−0 = **1,792.50**; given
  additionally 151=8.00, then 145 remains **1,792.50** — 151 is not a
  term of the printed formula (recorded, unwired — OQ-005) (FR-012,
  FR-013, FR-014).
- **AC-004:** Given 145=2,000.00 and 150=1,330.48, then 155 = **669.52**
  and 160 = 0.00; given instead 150=2,500.00 and 145=1,792.50, then 160 =
  **707.50** and 155 = 0.00 (FR-015).
- **AC-005:** Given 161=20.00, 162=15.00, 163=5.00, 164=669.52, 165=0.00
  → 166 = **709.52**; given 203=0.00, 160=1,330.48 → 167 = max(0,
  709.52−1,330.48−0) = **0.00** and 168 = max(0, 1,330.48−709.52+0) =
  **620.96**; given 520=100.00, 525=0.00 → 521 = 620.96−100−0 =
  **520.96** (520 stored positive; the formula's minus sign subtracts);
  given 187=30.00, 188=0.00 → 190 = **30.00**; given 523=10.00 → 524 =
  30.00−10.00 = **20.00** (523 stored positive under the same
  convention as 520 — the formula's minus sign subtracts); given
  194=192=199=193=0.00 → 195=0.00, 196=5.00 → TOTAL A PAGAR 198 =
  520.96+20.00+0.00+5.00 = **545.96** (FR-016, FR-018, FR-019, FR-021,
  FR-023, FR-024, FR-025).
- **AC-006:** Given an annex row with amount 1,234.5 and three nil
  amount cells, when the upload file is exported, then the amount cell
  reads exactly `1234.50`, the nil cells read `0.00`, the delimiter is
  `;`, every cell is Text-typed, the filename is at most 25 characters
  with .CSV extension, and the byte sequence of the fixture row is
  reproduced exactly (FR-028, FR-030).
- **AC-007:** Given an amount computed as 10.126 at export time, then the
  emitted cell reads `10.12` (truncation to two decimals, not rounding to
  10.13) (FR-030, FR-027).
- **AC-008:** Given a sales-annex row dated 15/12/2025 uploaded against
  the 01/2026 period, then the row is rejected with a date/period
  inconsistency naming its line (sales annexes admit the current period
  only); given the same row in a purchase annex, then it is accepted
  (within the three-prior-period window) (FR-032, FR-033).
- **AC-009:** Given an anulados-annex row dated in N−3, then the row is
  accepted (CT 111 window); given a purchase document dated in N−4 or in
  any FUTURE month, then the row is rejected with a window inconsistency
  — the windows are backward-looking only (FR-033).
- **AC-010:** Given a sales row carrying −100.00, then the file is
  rejected with the negative-value inconsistency; given the same negative
  on a voided-document row (anulados annex), then it is accepted
  (FR-031).
- **AC-011:** Given an upload whose last column is empty on line 7 and
  whose amount column is blank on line 12, then the response lists two
  inconsistencies with line numbers 7 and 12 respectively, and no
  casillas are complemented from the rejected file (FR-034, FR-036,
  FR-039).
- **AC-012:** Given a file saved as .XLSX or named with 26+ characters,
  then the upload is rejected with the extension/filename message before
  structure processing (FR-028, FR-035).
- **AC-013:** Given an Anexo-3-shaped file uploaded to the Anexo-1 slot,
  then the per-annex structure validation rejects it with the "cada anexo
  posee una estructura diferente" message and no rows are ingested
  (FR-035).
- **AC-014:** Given a *declaración modificatoria* of period 04/2026
  whose prior same-period declaration carried annexes 1-12, when the
  amendment opens, then annexes 3-12 are prefilled from that prior
  declaration, annexes 1-2 are empty and REQUIRED before filing, the
  *Número de declaración que Modifica* is recorded, and casillas 165/188
  anchor to the prior declaration's values; given a re-upload of annex 5,
  then the carried annex-5 rows are fully replaced, not merged (FR-040,
  FR-041).
- **AC-015:** Given a validated upload of a sales annex, then the
  declaration's sales casillas (85-99, 586) re-total automatically
  without any manual casilla edit (FR-038).
- **AC-016:** Given casilla 108 = 500.00 alongside the AC-001 sales
  values, then 105 remains **12,175.00** — 108 never enters the 105
  arithmetic (FR-009).
- **AC-017:** Given the Art. 74-A flag 495 set with 491=10.00, 492=5.00,
  493=2.00, then 203 = **17.00** and 168 = 160−166+203 reflects the +17.00
  shift; given the flag unset, then 491-493/203 are not computable and
  the 167/168 formulas run with 203 = 0.00 (FR-017, FR-018).
- **AC-018:** Given period N closing with 155 = 669.52 and 167 = 0.00,
  when period N+1 opens, then casilla 110 of N+1 = **669.52** and 164 of
  N+1 = 0.00; given N amended so that 155 = 700.00, then N+1 re-feeds
  110 = 700.00 from the amended declaration (FR-026).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | SOQ-12 carried: the DGII resolution(s) modifying the F-07 annexes (the legal authority behind the v14 annex set and upload formats) are not in the corpus — the manual (34_) and form (39_) are the only authority for this file's mechanics. Non-blocking (manuals carry full structures); acquire opportunistically and re-verify the format/casilla spec. | no | Takumi S3 (sources registry) | open |
| OQ-002 | EVID-173 doubt: manual §II heading says "CSV (delimitado por comas)" while the operative configuration uses the semicolon list separator (the usual MH wording defect). Working assumption encoded in FR-028: semicolon is the delimiter. Confirm against a live MH upload (or the resolution of OQ-001) before certifying byte-exact exports. | no | Takumi S3 | open |
| OQ-003 | Casilla 525 (Acreditación por FOVIAL): the form prints no formula or source — the credit's quantity-based computation (FOVIAL per-gallon tax interplay; 31_ guide; F1 crossref "FOVIAL/COTRANS quantity-tax risk") is undefined here and coordinated with the special-regimes/taxation waves. FR-020 consumes it as an input only. | no | Takumi S3 + special-regimes/taxation waves | open |
| OQ-004 | IVA retention-rate cross-ref target: the 1%/2%/13% IVA retention/perception/anticipo rates printed on the F-07 rows are anchored here via the form labels (LB-004/LB-005) only, because no IVA taxation requirements file exists yet (the S2 taxation wave wrote ISR only — SV-TAX-FR-102..131 are the ISR CT matrix, a different tax). Nothing blocks: F-07 casillas consume annex totals (files 03/04). When the IVA taxation file lands, the index task must wire the rate cross-references (CT Arts. 161-162-A zone, EVID-062). | no | Takumi S3 (index task) + future IVA taxation wave | open |
| OQ-005 | F-07 v14 rows 20 (casilla 146, Débito Proveniente de Crédito Negativo) and 41 (casilla 151, Crédito Proveniente de Débito Negativo) are printed on the form (with row-sign marks "−") but appear in NO printed casilla formula: the verbatim SUMA DE DÉBITOS (150) and SUMA DE CRÉDITOS (145) sums exclude them. Downstream wiring is unknown (presumably prior-period negative-balance carriers inside MH's online system — the form does not print it, and inventing a wiring was rejected in review). Encoded as recorded-but-unwired (FR-006/FR-012; casilla-spec role input_unwired); resolve via MH system behavior or the annex-modification resolutions (OQ-001). | no | Takumi S3 | open |
