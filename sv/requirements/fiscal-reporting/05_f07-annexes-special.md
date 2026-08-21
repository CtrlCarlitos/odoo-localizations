# SV — Fiscal reporting — F-07 fuel & dated-regime annexes 13-17: tasas diferenciadas, precios máximos & informativos

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | Takumi synthesis wave 3 (S3) |
| Updated | 2026-08-18 |

## 1. Purpose

This file defines the functional requirements for the five special-regime
annexes of the F-07 annex upload manual (*Manual de Usuario para Carga de
Archivo de los Anexos*, F-07 V14, ENERO 2025 §XX-§XXIV), all of them D12
DATED regimes: **Anexo 13** (*tasas diferenciadas* — differentiated IVA
rates on fuel, Decreto 321, enabled from the Mar-2022 tax period): a
MANUAL-ENTRY grid of global, IVA-net values by fuel grade
SUPERIOR/REGULAR/DIÉSEL — the only F-07 annex WITHOUT an upload file —
wired to casillas 586/587 (sales) and 588/589 (purchases), with
general-13%-rate fuel operations staying in annexes 1-3; **Anexo 14**
(the price-cap discount detail of the *Ley Especial Transitoria para
Fijar Precios Máximos de los Combustibles* — Transitory Special Law to
Set Maximum Fuel Prices — from Abr-2022): a credit-note-ONLY detail
(tipo 05, issued and/or received) with the A-P column model including
the fuel-grade column J (1 SUPERIOR / 2 REGULAR / 3 DIÉSEL) and the
*galones* (gallons) column at 11 integer + 8 decimal digits and the
*sin IVA* (without IVA) convention on price/value/discount/
IVA-of-the-discount, wired by *tipo de operación* 1 COMPRAS / 2 VENTAS
into casillas 550/551 and 552/553; **Anexos 15/16** (the Decreto No. 357
*informativo* (informational) pair over casillas 92/65, window Mayo-2022
→ *finalización de la obra* — completion of the works); **Anexo 17**
(the fuel-importers price-cap detail: informativo, CCF-only, CLOSED
window Junio-Agosto 2022, no casilla); and the **dated-regime engine**
that gates all five surfaces by regime-validity windows stored as data
with a regime-active flag derived from decree status (closed windows
never re-activate).

It does **not** cover: the declaration casillas this file feeds — 586-589
and 550-553 are owned by `01_f07-declaration.md` SV-FREP-FR-005/FR-010/
FR-011, casillas 92/65 by SV-FREP-FR-004/FR-010 (cross-referenced, never
restated); the generic annex upload engine and its format/validations/
modificatoria flow (SV-FREP-FR-028..041, inherited here by reference);
the canonical document-identifier mapping (`02_f07-annexes-sales.md`
SV-FREP-FR-042/043 — this file references it by id and never restates
it); the purchase annexes 3/5 (`03_f07-annexes-purchases.md` §3 — its
§1 records the F4→F7 hand-off of Anexo 16 to this file); the retention/
perception annexes and the anulados annex
(`04_f07-annexes-retentions-events.md` §3); the F-14 family, income
codes and informs (`06_f14-declaration.md`, `07_codes-and-informs.md`);
the filing calendar (`08_filing-calendar.md` — SOQ-08); the general-13%
fuel operations themselves (annexes 1-3 territory, files 02/03); the
differentiated RATE VALUES per fuel grade and the regime substance of
Decreto 321 / the Ley Especial Transitoria / Decreto 357 (special-regimes
and taxation wave territory — consumed here as dated configuration
data, OQ-001); and the FOVIAL/COTRANS quantity-tax interplay of casilla
525 (open pointer to the taxation/special-regimes waves — 01 §7 OQ-003
kin — NOT an FR here, see OQ-003).

## 2. Legal Basis

Authority rule (S3, binding): the MH forms and upload manuals ARE the
primary authority for declaration mechanics — 34_ (Manual de Usuario
para Carga de Archivo de los Anexos, F-07 V14, ENERO 2025) §XX-§XXIV is
the governing source for annexes 13-17; the form 39_ (F-07 v14, footer
"Actualizado al 15/08/2025") anchors the casilla wiring labels (owned by
`01_f07-declaration.md`). The plantilla workbook 36_ carries NO sheets
for annexes 13-17 (12 annex sheets + ÍNDICE only — consistent with
Anexo 13's manual-entry nature). Decree names are cited as printed in
the manual; no decree text is in the corpus and none is invented. Manual
pages are printed pages (printed page N = PDF page N+2).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Manual F-07 v14 §XX, "Anexo de Tasas Diferenciadas por Compras y Ventas Gravadas de Combustibles": "A partir del periodo tributario de marzo 2022 y durante la vigencia del Decreto 321 'DISPOSICIONES TRANSITORIAS RELATIVAS A LA REDUCCIÓN DE TASAS DEL IMPUESTO A LA TRANSFERENCIA DE BIENES MUEBLES Y A LA PRESTACIÓN DE SERVICIOS APLICABLES A LOS COMBUSTIBLES' sus prórrogas o similares decretos, se habilita el anexo 13 mediante el cual se deberán ingresar los valores de las ventas y compras gravadas realizadas de combustibles"; "Las ventas y compras de combustibles (incluyendo importaciones e internaciones) que han sido afectas con la tasa del 13% de IVA, se seguirán registrando en cada uno de los anexos de Ventas a Contribuyentes, Ventas a Consumidor Final y Compras a Contribuyentes"; las afectas a tasas diferenciadas "se deberán registrar de forma manual en el anexo que para tal efecto se ha puesto a disposición en el Formulario del referido impuesto, tomando en cuenta que los valores a ingresar deben ser globales y netos (es decir, sin las devoluciones, rebajas, descuentos u otras deducciones sobre ventas y/o compras) y los mismos no deben incluir IVA"; "de acuerdo al tipo de combustible: SUPERIOR, REGULAR y DIÉSEL"; "el sistema complementará automáticamente, las casillas de las compras y/o ventas gravadas de combustible con tasa diferenciada de IVA y su correspondiente débito y crédito fiscal, con los valores del anexo 13" | F-07 v14 upload manual §XX, differentiated-rates fuel annex: from the Mar-2022 tax period and during the validity of Decreto 321 (transitory provisions on the reduction of IVA rates applicable to fuels) — its extensions or similar decrees — annex 13 is enabled for the values of taxed fuel sales and purchases; fuel operations (including imports and CA-region internations) at the general 13% rate keep registering in annexes 1/2/3; differentiated-rate operations register MANUALLY in the form's annex with GLOBAL and NET values — without returns, rebates, discounts or other deductions over sales and/or purchases — not including IVA, by fuel type SUPERIOR, REGULAR and DIÉSEL; the system auto-complements the differentiated-rate casillas and their debit/credit companions with the annex-13 values | `sv/sources/34_F07_v14_manual.pdf` | §XX p.59 (EVID-178; txt `sv/.extractions/34_F07_v14_manual.pdf.txt` PAGE 65) |
| LB-002 | Manual F-07 v14 §XXI, "Anexo Descuento por Precio Máximo de Combustibles", tabla de estructura: "A FECHA EMISIÓN 10 / B TIPO DE OPERACIÓN 1 / C TIPO DE DOCUMENTO (EMITIDO/RECIBIDO) 2 / D NÚMERO DE RESOLUCIÓN/CÓDIGO DE GENERACIÓN mín. 19 máx. 50 / E SERIE DE DOCUMENTO/SELLO DE VALIDACIÓN mín. 8 máx. 50 / F NÚMERO DE DOCUMENTO/NÚMERO DE CONTROL mín. 1 máx. 50 / G NIT O NRC (CLIENTE/PROVEEDOR) mín. 2 máx. 14 / H DUI (CLIENTE/PROVEEDOR) 9 / I NOMBRE O RAZÓN SOCIAL (CLIENTE/PROVEEDOR) mín. 10 máx. 100 / J TIPO DE COMBUSTIBLE 1 / K CANTIDAD DE GALONES (VENDIDOS/COMPRADOS) 10 / L PRECIO DEL GALÓN ANTES DEL DESCUENTO (SIN IVA) 4 / M VALOR TOTAL DE OPERACIÓN ANTES DE DESCUENTO (SIN IVA) (VENTAS/COMPRAS) 11 / N VALOR TOTAL DE DESCUENTO POR PRECIO MÁXIMO (SIN IVA) (VENTAS/COMPRAS) 9 / O IVA DEL DESCUENTO (VENTAS/COMPRAS) 9 / P NÚMERO DE ANEXO 2"; semántica: A "Corresponde al documento emitido a sus clientes en caso que sean ventas o al documento recibido de su proveedor en caso sean compras"; B "1 COMPRAS / 2 VENTAS" y "Dependiendo del tipo de operación ingresado, los siguientes datos de las columnas D a la O, deben estar relacionados ya sea a las compras o ventas de combustible"; C "únicamente puede ser: 05 NOTA DE CRÉDITO"; D DTE = "número de control del DTE sin guiones (28 caracteres)"; pre-Nov-2022 "Código de Generación del DTE sin guiones (32 caracteres)"; E DTE = "sello de recepción del DTE (40 caracteres)"; F DTE = "código de generación del DTE sin guiones (32 caracteres)"; pre-Nov-2022 "número de control del DTE sin guiones (28 caracteres)"; G/H personas naturales DUI-vs-NIT XOR; J "1 SUPERIOR / 2 REGULAR / 3 DIÉSEL"; K "Máximo 11 enteros y 8 decimales ... No debe ingresar valores negativos" [la celda "10" de la tabla de estructura es defecto de impresión — gobierna la regla semántica 11+8; ídem N/O: tabla "9" vs semántica "Máximo 11 enteros y 2 decimales"]; L "Máximo de 4 caracteres (2 enteros y 2 decimales) ... el valor ingresado no debe incluir IVA"; M/N sin IVA; O "Corresponde al total del débito o crédito fiscal del descuento"; P = 14; "(sin incluir anulados y/o extraviados)"; alcance: "las devoluciones, descuentos u otras deducciones sobre compras y/o ventas que no tengan relación con los precios máximos de combustibles se seguirán registrando en cada uno de los anexos de Ventas a Contribuyentes y Compras a Contribuyentes"; totalización: "el sistema complementará automáticamente, las casillas de los descuentos de compras y/o ventas de combustibles con su correspondiente crédito y/o débito fiscal, con los valores del anexo cargado" | F-07 v14 upload manual §XXI, price-cap discount annex: verbatim A-P structure table with printed character counts; date = the document issued to clients (sales) or received from the supplier (purchases); operation type 1 purchases / 2 sales conditioning columns D-O; document type 05 credit note ONLY; the canonical DTE identifier fills printed for D/E/F (control number 28 / generation code 32 with the Nov-2022 swap; reception seal 40); client/supplier NIT-NRC vs DUI exclusive-or for natural persons; fuel type 1 SUPERIOR / 2 REGULAR / 3 DIÉSEL; gallons max 11 integer + 8 decimals (the structure table's "10" is a printing defect — the semantic rule governs; likewise N/O "9" vs 11+2); price per gallon before discount 2+2 without IVA; operation value and discount without IVA; IVA of the discount = the total fiscal debit/credit of the discount; annex number 14; voided/lost documents excluded; returns/discounts UNRELATED to price caps stay in annexes 1/3; the system auto-complements the purchase and/or sale discount casillas with their credit and/or debit companions from the loaded annex | `sv/sources/34_F07_v14_manual.pdf` | §XXI pp.59-63 (EVID-178; txt PAGES 65-69: tabla p.60, semántica pp.61-62, alcance p.59, totalización p.63) |
| LB-003 | Manual F-07 v14 §XXII, "Detalle de Ventas Internas Exentas No Sujetas a Proporcionalidad Decreto No. 357", tabla de estructura: "A FECHA DE EMISIÓN 10 / B CLASE DE DOCUMENTO 1 / C NÚMERO DE RESOLUCIÓN 100 / D SERIE DE DOCUMENTO 100 / E NÚMERO DE CONTROL INTERNO 100 / F NÚMERO DE DOCUMENTO 100 / G VENTAS INTERNAS EXENTAS NO SUJETAS A PROPORCIONALIDAD DECRETO No. 357 10 / H TOTAL VENTAS 10 / I NÚMERO DE ANEXO 2"; semántica: "La presentación de este anexo es informativa. Los datos a incorporar ... serán deducibles durante los períodos tributarios de mayo 2022 hasta la finalización de la obra"; A "debe coincidir con el mes y año seleccionado ... (a excepción de los documentos anulados, de acuerdo a lo establecido en el artículo 111 del Código Tributario, se pueden ingresar documentos de 3 periodos anteriores al que está declarando). Corresponde al documento emitido a sus clientes"; B clase 1/2/4; C DTE = "número de control del DTE sin guiones"; pre-Nov-2022 "Código de Generación del DTE sin guiones"; D DTE = "sello de recepción del DTE"; E formulario único = correlativo; DTE = blanco [las reglas de igualdad impresas de E ("igual al de la columna H") y F ("igual al de la columna F", autorreferencia) son defectos de transcripción]; F DTE = "código de generación del DTE sin guiones (32 dígitos)"; pre-Nov-2022 "número de control (28 dígitos)"; G/H numérico 10, dos decimales, sin negativos; I = 15; carga: "debe dar clic en el lapicito de la casilla 92" | F-07 v14 upload manual §XXII, Decreto 357 exempt-internal-sales annex: verbatim A-I structure table (date, document class 1/2/4, resolution, series, internal control number, document number, the Decreto 357 exempt-non-subject value, total sales, annex number 15); presentation is informational, data deductible from May 2022 until completion of the works; date = the document issued to clients, current-period with the CT Art. 111 three-prior-period exception for voided documents; canonical DTE identifier fills for C/D/F (control number / generation code Nov-2022 swap; reception seal; DTE blanks E); the printed equality cross-references of E (cites H) and F (self-citing) are transcription defects; amounts 10-char two-decimal no-negatives; upload entry via the casilla-92 pencil | `sv/sources/34_F07_v14_manual.pdf` | §XXII pp.64-66 (EVID-178; txt PAGES 70-72) |
| LB-004 | Manual F-07 v14 §XXIII, "Detalle de Compras Internas Exentas Decreto No. 357", tabla de estructura: "A FECHA DE EMISIÓN 10 / B CLASE DE DOCUMENTO 1 / C TIPO DE DOCUMENTO 2 / D NÚMERO DE DOCUMENTO 100 / E NIT O NRC DEL PROVEEDOR 14 / F NOMBRE DEL PROVEEDOR SIN LÍMITE / G COMPRAS INTERNAS EXENTAS DECRETO No. 357 10 / H INTERNACIONES EXENTAS Y/O NO SUJETAS 10 / I IMPORTACIONES EXENTAS Y/O NO SUJETAS 10 / J TOTAL DE COMPRAS 10 / K DUI DEL PROVEEDOR 9 / L NÚMERO DE ANEXO 2"; semántica: "para efectos informativos ... las compras y créditos fiscales detallados sean deducibles durante los períodos tributarios de mayo 2022 hasta finalización de la obra"; A: ventana de 3 periodos anteriores "de acuerdo al artículo 63 de la Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestación de Servicios"; B "1 Impreso por Imprenta o Tiquetes (aplica para el tipo de documento 01) / 2 Formulario Único (aplica para el tipo de documento 01) / 3 Otros (aplica para el tipo de documento 12)" [la lista de C repite el catálogo de clase 1/2/4 — defecto de copia; los tipos operativos por los paréntesis de B: 01 y 12]; D DTE = "código de generación del DTE sin guiones"; pre-Nov-2022 "número de control"; E/K personas naturales DUI-vs-NIT XOR [E imprime el corte "enero 2022", K "MAYO 2022" — coincidentes dentro de la ventana del anexo (≥ mayo 2022)]; "Si es un proveedor del exterior, para los tipos de documento 12 puede colocar el NIT de la Dirección General de Tesorería 06140108140066 e independientemente del periodo a declarar, el campo de DUI debe quedar completamente vacío"; F tipo 12 = "el Nombre de la Dirección General de Tesorería"; H/I "debe colocar el valor de la operación detallada en la Declaración de Mercancías"; J "total de las operaciones detalladas en las columnas comprendidas de la G a la I (sumando las Notas de Débito y restando las Notas de Crédito)"; L = 16; nota Aduanas: importaciones/internaciones "se compararán con los valores reportados por la Dirección General de Aduanas, de acuerdo al levante de las mercancías"; carga: "lapicito de la casilla 65" | F-07 v14 upload manual §XXIII, Decreto 357 exempt-internal-purchases annex: verbatim A-L structure table (date, document class, document type, document number, supplier NIT/NRC and name, the Decreto 357 exempt internal purchases bucket, exempt/non-subject internations and imports buckets, purchase total, supplier DUI, annex number 16); informational, deductible May 2022 until completion of the works; Ley IVA Art. 63 three-prior-period window on dates; class list with its tipo parentheticals (imprenta/tiquetes and formulario único apply to tipo 01; Otros to tipo 12 — the type column's printed 1/2/4 list is a copy defect of the class catalog); DTE generation-code/control-number fills on D; natural-person DUI-vs-NIT exclusive-or (printed cuts Enero-2022 and Mayo-2022 coincide inside the annex window); foreign suppliers of tipo 12 carry Treasury's NIT 06140108140066 with DUI empty and Treasury's name; internations/imports valued from the merchandise declaration; total J = G..I adding debit notes, subtracting credit notes; customs levante cross-check note; upload entry via the casilla-65 pencil | `sv/sources/34_F07_v14_manual.pdf` | §XXIII pp.66-69 (EVID-178; txt PAGES 72-75) |
| LB-005 | Manual F-07 v14 §XXIV, "Anexo 17 Descuento Precios Máximos para Importadores de Combustible", tabla de estructura (como se imprime): "A FECHA DE EMISIÓN 10 / B TIPO DE DOCUMENTO 2 / C SERIE DE DOCUMENTO/SELLO DE VALIDACIÓN 50 / D NÚMERO DE DOCUMENTO/NÚMERO DE CONTROL 50 / E NIT O NRC (CLIENTE) 14 / F DUI (CLIENTE) 9 / G NOMBRE O RAZÓN SOCIAL (CLIENTE) 100 / H TIPO DE COMBUSTIBLE 1 / I CANTIDAD DE GALONES (VENDIDOS) 10 / J PRECIO DEL GALÓN ANTES DEL DESCUENTO (SIN IVA) 4 / K VALOR DESCUENTO MÁXIMO (SIN IVA) (VENTAS) 11 / L VALOR TOTAL DE DESCUENTO POR PRECIO MÁXIMO (SIN IVA) (VENTAS) 9 / M IVA DEL DESCUENTO (VENTAS) 9 / L NÚMERO DE ANEXO 2" [la segunda "L" está duplicada tal como se imprime — la semántica la letra "N. Número de anexo ... 17"]; semántica: "La presentación de este anexo es para efectos informativos, no afecta el cálculo de la declaración ... deducibles durante los períodos tributarios de junio 2022 a agosto 2022"; B "03 Comprobante de crédito fiscal"; C DTE = "Sello de Validación del DTE. Ejemplo: 2021DC0000A000DD000090BB00DB00000000BR0WT"; D DTE = "código de generación del DTE sin guiones"; pre-Nov-2022 "número de control"; E/F personas naturales XOR desde junio 2022 [E imprime "junio 2022 en adelante" y F "enero 2022" — coincidentes dentro de la ventana (≥ junio 2022)]; H "1 SUPERIOR / 2 REGULAR / 3 DIESEL"; I/J/K/L/M numéricos con DOS decimales [galones a 2 decimales, a diferencia del 11+8 del Anexo 14]; N = 17 | F-07 v14 upload manual §XXIV, fuel-importers price-cap discount annex: verbatim structure table as printed — including the duplicated "L" letter of the annex-number row (lettered N by its semantics, value 17); informational, does not affect the declaration's computation, deductible June 2022 through August 2022; document type 03 tax-credit document only; DTE fills: validation seal in C (example printed), generation code in D with the Nov-2022 control-number swap; client NIT-NRC vs DUI exclusive-or (printed cuts Jun-2022 and Ene-2022 coincide inside the window); fuel type 1/2/3; ALL amount columns including gallons at two decimals — unlike Anexo 14's 11+8 gallons exception | `sv/sources/34_F07_v14_manual.pdf` | §XXIV pp.70-72 (EVID-178; txt PAGES 76-78) |
| LB-006 | Formulario F-07 v14, etiquetas de cableado (39_/EVID-179): B fila 16 "Ventas Gravadas de Combustible con tasas diferenciadas de IVA 586 (Débito Fiscal ... 587)"; B fila 21 "Devoluciones ... por precios máximos de combustibles 552− (Débito ... 553)"; B fila 12 "Ventas Internas Exentas No Sujetas a Proporcionalidad 92"; C fila 31 "Compras Gravadas de Combustible con tasas diferenciadas de IVA 588 (Crédito ... 589)"; C fila 33 "... por precios máximos de combustibles 550− (Crédito ... 551−)"; C fila 24 "Compras Internas Exentas y/o No sujetas 65" | F-07 v14 form wiring labels: casillas 586/587 (differentiated-rate fuel sales + debit), 552/553 (price-cap sales returns + debit), 92 (exempt internal sales not subject to proportionality), 588/589 (differentiated-rate fuel purchases + credit), 550/551 (price-cap purchase returns + credit), 65 (exempt and/or non-subject internal purchases) — all owned by `01_f07-declaration.md` FR-004/FR-005/FR-010/FR-011 | `sv/sources/39_F07_v14_form_visual.pdf` | p.1 (EVID-179) |

## 3. Functional Requirements

### 3.1 Anexo 13 — tasas diferenciadas (manual-entry regime; casillas 586-589)

- **SV-FREP-FR-124:** The system shall enable Anexo 13 (fuel sales and
  purchases at *tasas diferenciadas* — differentiated IVA rates) as a
  DATED regime — "A partir del periodo tributario de marzo 2022 y durante
  la vigencia del Decreto 321 ... sus prórrogas o similares decretos"
  (from the Mar-2022 tax period, during the validity of Decreto 321
  "Disposiciones Transitorias Relativas a la Reducción de Tasas del
  IVA ... Aplicables a los Combustibles", its extensions or similar
  decrees): the annex exists only for tax periods from Mar-2022 while
  Decreto 321 or its printed extensions/similar decrees are in force —
  and shall capture it as a MANUAL-ENTRY grid: NO upload file exists or
  is produced for Anexo 13, the only F-07 annex without a file (the
  generic export engine of SV-FREP-FR-028..041 is bypassed; the grid is
  entered and stored on the declaration object itself).
  (LB-001; EVID-178)
- **SV-FREP-FR-125:** The system shall capture the Anexo 13 values as
  GLOBAL aggregates (one value per direction and fuel grade, NOT
  per-document rows) NET in the manual's printed sense — "globales y
  netos (es decir, sin las devoluciones, rebajas, descuentos u otras
  deducciones sobre ventas y/o compras) y los mismos no deben incluir
  IVA" (global and net: without returns, rebates, discounts or other
  deductions over sales and/or purchases, and not including IVA) —
  split by direction (ventas/compras, INCLUDING importaciones e
  internaciones of fuel) and by fuel grade SUPERIOR, REGULAR and
  DIÉSEL; fuel operations taxed at the GENERAL 13% rate (including
  imports and internations) shall NOT enter Anexo 13 — they stay in
  the general annexes 1/2/3 per the manual's printed exclusion.
  (LB-001; EVID-178)
- **SV-FREP-FR-126:** The system shall wire the Anexo 13 grid into the
  Task 1 fuel casillas by auto-complementation as printed — "el sistema
  complementará automáticamente, las casillas de las compras y/o
  ventas gravadas de combustible con tasa diferenciada de IVA y su
  correspondiente débito y crédito fiscal, con los valores del anexo
  13": the net venta bases total casilla 586 with its fiscal debit
  587, and the net compra bases total casilla 588 with its fiscal
  credit 589 (casillas owned by SV-FREP-FR-005/FR-010); the
  debit/credit companions compute as the applicable differentiated rate
  of each fuel grade × that grade's net base — the rate VALUES per
  grade are not printed in the manual and are consumed as dated regime
  configuration (OQ-001) — under the two-decimal discipline of
  SV-FREP-FR-027. (LB-001; LB-006; EVID-178; EVID-179; cross-ref
  SV-FREP-FR-005/010/027)

### 3.2 Anexo 14 — descuentos por precios máximos (NC-only detail; casillas 550-553)

- **SV-FREP-FR-127:** The system shall build Anexo 14 (the detail of
  the discounts from the application of fuel *precios máximos* —
  maximum prices) as a DATED regime from Abr-2022 under the *Ley
  Especial Transitoria para Fijar Precios Máximos de los Combustibles*
  (Transitory Special Law to Set Maximum Fuel Prices), admitting ONLY
  credit notes — "únicamente ... las Notas de Crédito emitidas y/o
  recibidas relacionadas a los descuentos ... por los precios máximos
  de combustibles": every row is a tipo 05 *Nota de Crédito* (credit
  note), and any non-05 document row is REJECTED before export; the
  A FECHA EMISIÓN is that of the document ISSUED to clients on venta
  rows and of the document RECEIVED from the supplier on compra rows
  ("Corresponde al documento emitido a sus clientes en caso que sean
  ventas o al documento recibido de su proveedor en caso sean
  compras"), with columns D-O related to compras or ventas per the
  B tipo de operación; returns, discounts and other deductions NOT
  related to fuel price caps are EXCLUDED from this annex — they keep
  registering in annexes 1 and 3 per the printed scope rule; and
  voided/lost documents are excluded ("sin incluir anulados y/o
  extraviados"). (LB-002; EVID-178)
- **SV-FREP-FR-128:** The system shall emit every Anexo 14 row with
  the verbatim manual §XXI column model A-P — A FECHA EMISIÓN (10) ·
  B TIPO DE OPERACIÓN (1: 1 COMPRAS / 2 VENTAS) · C TIPO DE DOCUMENTO
  EMITIDO/RECIBIDO (2: 05 only, FR-127) · D NÚMERO DE RESOLUCIÓN /
  CÓDIGO DE GENERACIÓN (min 19 max 50) · E SERIE DE DOCUMENTO / SELLO
  DE VALIDACIÓN (min 8 max 50) · F NÚMERO DE DOCUMENTO / NÚMERO DE
  CONTROL (min 1 max 50) · G NIT O NRC CLIENTE/PROVEEDOR (min 2 max
  14) · H DUI CLIENTE/PROVEEDOR (9) · I NOMBRE O RAZÓN SOCIAL (min 10
  max 100) · **J TIPO DE COMBUSTIBLE (1: 1 SUPERIOR / 2 REGULAR /
  3 DIÉSEL)** · K CANTIDAD DE GALONES VENDIDOS/COMPRADOS ("Máximo 11
  enteros y 8 decimales", no negatives — an annex-specific EXCEPTION
  to the §II two-decimal discipline of SV-FREP-FR-030; the structure
  table's "10" is a printing defect, the semantic rule governs) ·
  L PRECIO DEL GALÓN ANTES DEL DESCUENTO SIN IVA (4: 2 enteros + 2
  decimales) · M VALOR TOTAL DE OPERACIÓN ANTES DE DESCUENTO SIN IVA
  · N VALOR TOTAL DE DESCUENTO POR PRECIO MÁXIMO SIN IVA · O IVA DEL
  DESCUENTO (= the total fiscal débito/crédito of the discount; M/N/O
  at 11 enteros + 2 decimales, sin IVA, no negatives) · P NÚMERO DE
  ANEXO = 14 — in exactly this order; D/E/F DTE rows fill under the
  CANONICAL mapping of SV-FREP-FR-042/043, which §XXI prints in full
  (D = *número de control* 28 / pre-Nov-2022 *código de generación*
  32; E = *sello de recepción* 40; F = *código de generación* 32 /
  pre-Nov-2022 *número de control* 28 — a printed confirmation, never
  restated beyond this); G/H enforce the natural-person DUI-vs-NIT
  exclusive-or (H filled ⇒ G empty, and vice versa).
  (LB-002; EVID-178; cross-ref SV-FREP-FR-042/043)
- **SV-FREP-FR-129:** The system shall wire Anexo 14 rows into the
  Task 1 price-cap casillas by their TIPO DE OPERACIÓN: tipo 1 COMPRAS
  rows (NCs received) feed the purchase pair 550 (devoluciones por
  precios máximos, subtracted by the casilla-100 formula) with its
  credit companion 551, and tipo 2 VENTAS rows (NCs issued) feed the
  sales pair 552 with its debit companion 553 (casillas owned by
  SV-FREP-FR-005/FR-011); the column basis follows the label match
  (descuento → 550/552; IVA del descuento → 551/553 — unprinted, OQ-002)
  and the casilla values are stored as POSITIVE magnitudes under the
  sign convention of SV-FREP-FR-019 (the printed formulas' minus signs
  perform the subtraction). (LB-002; LB-006; EVID-178; EVID-179;
  cross-ref SV-FREP-FR-005/011/019)

### 3.3 Anexos 15/16 — Decreto 357 informativos (casillas 92/65)

- **SV-FREP-FR-130:** The system shall build Anexo 15 (detail of the
  *ventas internas exentas no sujetas a proporcionalidad* — exempt
  internal sales not subject to proportionality — under Decreto No. 357)
  as a DATED-regime INFORMATIVO annex — "La presentación de este anexo
  es informativa", its data deductible "durante los períodos
  tributarios de mayo 2022 hasta la finalización de la obra" (until
  completion of the works — an end consumed as dated data, semantics
  OQ-005) — with the verbatim column model A-I: A FECHA DE EMISIÓN
  (10; DD/MM/AAAA current-period, with the CT Art. 111
  three-prior-period exception for anulados as printed; the document
  issued to clients) · B CLASE DE DOCUMENTO (1/2/4) · C NÚMERO DE
  RESOLUCIÓN (100; DTE = *número de control*, pre-Nov-2022 *código de
  generación*) · D SERIE DE DOCUMENTO (100; DTE = *sello de
  recepción*) · E NÚMERO DE CONTROL INTERNO (100; formulario único
  correlativo; DTE blank — the printed equality cross-references of E
  to H and of F to itself are transcription defects, not encoded) ·
  F NÚMERO DE DOCUMENTO (100; DTE = *código de generación* 32,
  pre-Nov-2022 *número de control* 28) · G VENTAS INTERNAS EXENTAS NO
  SUJETAS A PROPORCIONALIDAD DECRETO No. 357 (10) · H TOTAL VENTAS
  (10) · I NÚMERO DE ANEXO = 15; C/D/F DTE fills follow the canonical
  SV-FREP-FR-042/043 mapping (printed confirmation); the annex details
  the operations behind casilla 92 (upload entry: the casilla-92
  pencil), computes NO débito/crédito companion of its own, and rows
  dated outside the window are rejected under FR-133's gating (the
  casilla-92 value itself is owned by SV-FREP-FR-004; auto-total basis
  unprinted — OQ-002). (LB-003; LB-006; EVID-178)
- **SV-FREP-FR-131:** The system shall build Anexo 16 (detail of the
  *compras internas exentas* — exempt internal purchases — under
  Decreto 357) as the purchase-side twin of FR-130's regime — the same
  Mayo-2022 → fin-de-obra window, informational status ("para efectos
  informativos"), no credit companion — with the verbatim column model
  A-L: A FECHA DE EMISIÓN (10; Ley IVA Art. 63 three-prior-period
  window as printed; the supplier-issued document's date) · B CLASE DE
  DOCUMENTO (1 imprenta/tiquetes → tipo 01 · 2 formulario único →
  tipo 01 · 3 Otros → tipo 12, per the printed parentheticals; the
  C column's own printed 1/2/4 list is a copy defect of the clase
  catalog — the operative tipos are 01 and 12) · C TIPO DE DOCUMENTO ·
  D NÚMERO DE DOCUMENTO (100; DTE = *código de generación*, pre-Nov-
  2022 *número de control*) · E NIT O NRC DEL PROVEEDOR (14) ·
  F NOMBRE DEL PROVEEDOR · G COMPRAS INTERNAS EXENTAS DECRETO No. 357
  (10) · H INTERNACIONES EXENTAS Y/O NO SUJETAS (10; valued from the
  *Declaración de Mercancías*) · I IMPORTACIONES EXENTAS Y/O NO
  SUJETAS (10; likewise) · J TOTAL DE COMPRAS (10; = G..I "sumando
  las Notas de Débito y restando las Notas de Crédito") · K DUI DEL
  PROVEEDOR (9) · L NÚMERO DE ANEXO = 16; natural-person suppliers
  enforce the DUI-vs-NIT exclusive-or (the printed Enero-2022 cut of
  E and Mayo-2022 cut of K coincide inside the annex window ≥
  Mayo-2022); FOREIGN suppliers of tipo 12 carry the Tesorería
  pseudo-NIT 06140108140066 in E with K DUI EMPTY "independientemente
  del periodo a declarar" and the Tesorería's name in F — the twin of
  SV-FREP-FR-074's rule; the Aduanas levante cross-check note applies
  to H/I (awareness only, cf. SV-FREP-FR-094 kin); the annex details
  the operations behind casilla 65 (upload entry: the casilla-65
  pencil); master-index cluster F4 lists it among the purchase
  annexes but this wave's file split assigns it to this file (the
  hand-off is recorded in `03_f07-annexes-purchases.md` §1).
  (LB-004; LB-006; EVID-178; cross-ref SV-FREP-FR-074)

### 3.4 Anexo 17 — importadores (closed window, informativo)

- **SV-FREP-FR-132:** The system shall build Anexo 17 (informativo
  detail of the price-cap discounts of fuel *importadores* —
  importers) as a CLOSED-VINTAGE regime: its window is fixed at
  "períodos tributarios de junio 2022 a agosto 2022" (tax periods June
  2022 through August 2022 — CLOSED), the annex is "para efectos
  informativos, no afecta el cálculo de la declaración" (informational;
  it does not affect the declaration's computation) and feeds NO
  casilla; its column model as printed: A FECHA DE EMISIÓN (10) ·
  B TIPO DE DOCUMENTO (2: 03 *Comprobante de Crédito Fiscal* ONLY —
  the only admissible type) · C SERIE DE DOCUMENTO / SELLO DE
  VALIDACIÓN (50; DTE = *sello de validación*, printed example
  "2021DC0000A000DD000090BB00DB00000000BR0WT") · D NÚMERO DE
  DOCUMENTO / NÚMERO DE CONTROL (50; DTE = *código de generación*,
  pre-Nov-2022 *número de control*) · E NIT O NRC CLIENTE (14) ·
  F DUI CLIENTE (9) · G NOMBRE O RAZÓN SOCIAL CLIENTE (100) ·
  H TIPO DE COMBUSTIBLE (1: 1 SUPERIOR / 2 REGULAR / 3 DIESEL) ·
  I CANTIDAD DE GALONES VENDIDOS (10) · J PRECIO DEL GALÓN ANTES DEL
  DESCUENTO SIN IVA (4: 2+2) · K VALOR DESCUENTO MÁXIMO SIN IVA
  VENTAS (11) · L VALOR TOTAL DE DESCUENTO POR PRECIO MÁXIMO SIN IVA
  VENTAS (9) · M IVA DEL DESCUENTO VENTAS (9) · N NÚMERO DE ANEXO =
  17 (the structure table prints the annex-number row with a
  DUPLICATED "L" letter — carried as printed; the semantics letter it
  N); every amount column INCLUDING galones carries the standard
  TWO-decimal discipline — unlike Anexo 14's 11+8 exception (FR-128);
  client natural persons enforce the E/F DUI-vs-NIT exclusive-or (the
  printed Jun-2022 and Ene-2022 cuts coincide inside the window);
  DTE identifier fills follow the canonical SV-FREP-FR-042/043
  mapping (printed confirmation). (LB-005; EVID-178; cross-ref
  SV-FREP-FR-042/043)

### 3.5 Dated-regime engine (D12)

- **SV-FREP-FR-133:** The system shall gate every annex 13-17 surface
  by a regime-validity window stored as DATED DATA — annex 13: Mar-2022
  → end of Decreto 321's *vigencia* (validity); annex 14: Abr-2022 →
  end of the Ley Especial Transitoria's validity; annexes 15/16:
  Mayo-2022 → fin-de-obra; annex 17: Jun-2022 → Ago-2022 (fixed) — with
  a
  regime-active flag DERIVED from the decree status: a period inside
  the window accepts rows; a period before the window start or after
  the window end rejects them and leaves the surface unavailable.
  (LB-001; LB-002; LB-003; LB-004; LB-005; EVID-178)
- **SV-FREP-FR-134:** The system shall encode Anexo 17's window as
  CLOSED — the regime-active flag is permanently false for periods
  after Ago-2022 — while the annex remains available for declarations
  of periods INSIDE the window (historical and amended filings):
  closed-vintage regimes never re-activate, and the open-ended regimes
  (13/14/15/16) close only by decree-status update, never by
  hard-coded dates. (LB-005; EVID-178)

### 3.6 Export, declaration integration and regime interplay

- **SV-FREP-FR-135:** The system shall export annexes 14-17 under the
  generic upload engine of SV-FREP-FR-028..041 (semicolon CSV, Text
  cells, ≤25-character filename, clean-replace semantics), with each
  annex's number in its printed trailing column — P = 14, I = 15,
  L = 16 and N = 17 (the §XXIV table's duplicated-L lettering carried
  as printed) — and the Anexo 14 galones column as the printed
  exception to the two-decimal discipline (FR-128; Anexo 17's gallons
  stay two-decimal, FR-132); Anexo 13 produces NO file under any
  condition (FR-124); the *declaración modificatoria* (amended return)
  carryover of SV-FREP-FR-040 prints
  "anexos 3 al 12" only — the 13-17 carryover behavior is unprinted and
  not asserted (OQ-004). (LB-002; LB-003; LB-004; LB-005; EVID-178;
  EVID-173; cross-ref SV-FREP-FR-028..041/040)
- **SV-FREP-FR-136:** The system shall expose this file's feeds as the
  §4 wiring interface into the Task 1 casilla engine — Anexo 13 →
  586/587 and 588/589 (FR-126); Anexo 14 → 550/551 and 552/553
  (FR-129); Anexos 15/16 → the informativo detail of casillas 92/65
  (owned by SV-FREP-FR-004/FR-010); Anexo 17 → no casilla — with no
  manual casilla fill anywhere (SV-FREP-FR-038); the FOVIAL/COTRANS
  quantity-tax interplay of casilla 525 stays OPEN with the
  taxation/special-regimes waves (OQ-003; 01 §7 OQ-003 kin — its
  per-gallon design decision is NOT encoded here). (LB-006; EVID-179;
  cross-ref SV-FREP-FR-004/005/010/011/038)

## 4. Data Model

No CSV sidecars live next to this file: the regime windows, row models
and wiring below are in-file §4 seed data. Layer semantics: Odoo-side
computation/bookkeeping data only (wave default `odoo`; see §5).

**Regime window seed — l10n_sv.f07.fuel.regime (D12 dated data):**

| Annex | Instrument (as printed) | Window start | Window end | End kind | Status |
|-------|--------------------------|--------------|------------|----------|--------|
| 13 | Decreto 321 (tasas diferenciadas) | 2022-03 | null | decree vigencia (regime-active from decree status) | open — OQ-001 (2026 successor status unpinned) |
| 14 | Ley Especial Transitoria para Fijar Precios Máximos de los Combustibles | 2022-04 | null | decree vigencia | open — OQ-001 kin |
| 15 | Decreto No. 357 (ventas exentas no sujetas a proporcionalidad) | 2022-05 | fin de la obra | dated data | open — OQ-005 (end semantics unpinned) |
| 16 | Decreto No. 357 (compras internas exentas) | 2022-05 | fin de la obra | dated data | open — OQ-005 (end semantics unpinned) |
| 17 | precios máximos importadores | 2022-06 | 2022-08 | fixed | CLOSED (FR-134 — never re-activates) |

**Anexo 13 manual grid — l10n_sv.f07.annex13.entry (no file surface):**

| Field | Type | Catalog / values | Reference |
|-------|------|------------------|-----------|
| declaration_id, fuel_grade, direction, base_neto | m2o/select/select/monetary(2dp) | grade: SUPERIOR · REGULAR · DIÉSEL; direction: venta → 586/587 · compra → 588/589; base_neto = global net-of-IVA aggregate | FR-124, FR-125 |
| debit_credit_computed | monetary(2dp) | grade rate × base_neto; rate values from regime configuration (not in corpus — OQ-001) | FR-126 |

**Anexo 14 row model — l10n_sv.f07.annex14.row (seed structure; verbatim
from manual §XXI structure table + semantics):**

| Col | Header (Spanish, verbatim, abbreviated) | Length | Semantics | FR |
|-----|------------------------------------------|--------|-----------|----|
| A | FECHA EMISIÓN | 10 | DD/MM/AAAA current period; document issued (ventas) / received (compras) | FR-127 |
| B | TIPO DE OPERACIÓN | 1 | 1 COMPRAS · 2 VENTAS — conditions columns D-O | FR-127, FR-129 |
| C | TIPO DE DOCUMENTO (EMITIDO/RECIBIDO) | 2 | 05 NOTA DE CRÉDITO only (non-05 rejected) | FR-127 |
| D | NÚMERO DE RESOLUCIÓN/CÓDIGO DE GENERACIÓN | 19-50 | canonical RESOLUCIÓN slot (FR-043): número de control 28 / pre-Nov-2022 código de generación 32 | FR-128 |
| E | SERIE DE DOCUMENTO/SELLO DE VALIDACIÓN | 8-50 | canonical SERIE slot: sello de recepción 40 (DTE) | FR-128 |
| F | NÚMERO DE DOCUMENTO/NÚMERO DE CONTROL | 1-50 | canonical NÚMERO slot: código de generación 32 / pre-Nov-2022 número de control 28 | FR-128 |
| G | NIT O NRC (CLIENTE/PROVEEDOR) | 2-14 | XOR with H for natural persons (H filled ⇒ G empty) | FR-128 |
| H | DUI (CLIENTE/PROVEEDOR) | 9 | natural persons only; XOR with G | FR-128 |
| I | NOMBRE O RAZÓN SOCIAL (CLIENTE/PROVEEDOR) | 10-100 | counterparty name | FR-128 |
| J | TIPO DE COMBUSTIBLE | 1 | 1 SUPERIOR · 2 REGULAR · 3 DIÉSEL | FR-128 |
| K | CANTIDAD DE GALONES (VENDIDOS/COMPRADOS) | 11+8 | exception to FR-030's 2dp; no negatives (structure-table "10" = print defect; semantics govern) | FR-128, FR-135 |
| L | PRECIO DEL GALÓN ANTES DEL DESCUENTO (SIN IVA) | 4 (2+2) | sin IVA; no negatives | FR-128 |
| M | VALOR TOTAL DE OPERACIÓN ANTES DE DESCUENTO (SIN IVA) | 11+2 | sin IVA (structure-table "11") | FR-128 |
| N | VALOR TOTAL DE DESCUENTO POR PRECIO MÁXIMO (SIN IVA) | 11+2 | sin IVA (structure-table "9" = print defect; semantics govern) | FR-128, FR-129 |
| O | IVA DEL DESCUENTO (VENTAS/COMPRAS) | 11+2 | total fiscal débito/crédito of the discount (structure-table "9" = print defect) | FR-128, FR-129 |
| P | NÚMERO DE ANEXO | 2 | literal 14 on every row | FR-135 |

Voided/lost documents excluded (FR-127); non-price-cap returns/discounts
excluded — annexes 1/3 territory (FR-127).

**Anexo 15 row model — l10n_sv.f07.annex15.row (A-I verbatim from §XXII):
** A FECHA (10; current period, CT 111 anulados 3-prior-period exception
printed; the document issued to clients) · B CLASE (1/2/4) · C NÚMERO DE
RESOLUCIÓN (100; DTE = número de control, pre-Nov-2022 código de
generación) · D SERIE (100; DTE = sello de recepción) · E NÚMERO DE
CONTROL INTERNO (100; formulario único correlativo, DTE blank — the
printed E→H and F→F equality cross-references are transcription defects,
not encoded) · F NÚMERO DE DOCUMENTO (100; DTE = código de generación 32,
pre-Nov-2022 número de control 28) · G VENTAS INTERNAS EXENTAS NO SUJETAS
A PROPORCIONALIDAD D-357 (10) · H TOTAL VENTAS (10) · I NÚMERO DE ANEXO =
15. Informativo; no companion; upload entry via the casilla-92 pencil.
(FR-130)

**Anexo 16 row model — l10n_sv.f07.annex16.row (A-L verbatim from
§XXIII):** A FECHA (10; Ley IVA Art. 63 3-prior-period window) ·
B CLASE (1 imprenta/tiquetes → tipo 01 · 2 formulario único → tipo 01 ·
3 Otros → tipo 12) · C TIPO DE DOCUMENTO (2; the printed 1/2/4 list is a
copy defect of the clase catalog — operative tipos 01 and 12) ·
D NÚMERO DE DOCUMENTO (100; DTE = código de generación, pre-Nov-2022
número de control) · E NIT O NRC DEL PROVEEDOR (14; Tesorería
06140108140066 for foreign tipo-12 suppliers, DUI empty; XOR with K for
natural persons) · F NOMBRE DEL PROVEEDOR (Tesorería's name for tipo 12)
· G COMPRAS INTERNAS EXENTAS D-357 (10) · H INTERNACIONES EXENTAS Y/O NO
SUJETAS (10; valued from the Declaración de Mercancías) ·
I IMPORTACIONES EXENTAS Y/O NO SUJETAS (10; likewise) · J TOTAL DE
COMPRAS (10; = G..I, ND+ / NC−) · K DUI DEL PROVEEDOR (9; from
Mayo-2022) · L NÚMERO DE ANEXO = 16. Informativo; Aduanas levante
cross-check awareness on H/I; upload entry via the casilla-65 pencil.
(FR-131)

**Anexo 17 row model — l10n_sv.f07.annex17.row (as printed from §XXIV):
** A FECHA (10) · B TIPO DE DOCUMENTO (2; 03 CCF only) · C SERIE DE
DOCUMENTO/SELLO DE VALIDACIÓN (50; DTE = sello de validación, example
2021DC0000A000DD000090BB00DB00000000BR0WT) · D NÚMERO DE DOCUMENTO/
NÚMERO DE CONTROL (50; DTE = código de generación, pre-Nov-2022 número
de control) · E NIT O NRC CLIENTE (14; XOR with F) · F DUI CLIENTE (9)
· G NOMBRE O RAZÓN SOCIAL CLIENTE (100) · H TIPO DE COMBUSTIBLE (1/2/3)
· I CANTIDAD DE GALONES VENDIDOS (10; standard 2dp — NOT Anexo 14's
11+8) · J PRECIO DEL GALÓN SIN IVA (4; 2+2) · K VALOR DESCUENTO MÁXIMO
SIN IVA VENTAS (11) · L VALOR TOTAL DE DESCUENTO POR PRECIO MÁXIMO SIN
IVA VENTAS (9) · M IVA DEL DESCUENTO VENTAS (9) · N NÚMERO DE ANEXO = 17
(structure table prints the annex-number row with a duplicated "L" —
carried as printed). Informativo; no casilla feed. (FR-132)

**Wiring interface into 01 §3.1 (casillas owned by Task 1):**

| Feed | Casilla(s) | Notes |
|------|-----------|-------|
| Anexo 13 venta bases (net, by grade) | 586 + débito 587 | companions = grade rate × base (rates = regime config, OQ-001); AC-002/AC-003 |
| Anexo 13 compra bases | 588 + crédito 589 | same |
| Anexo 14 tipo 1 (compras) descuento / IVA del descuento | 550 / 551 | label-match basis (OQ-002); positive magnitude — the 100/145 formulas' minus signs subtract (01 FR-013/FR-014) |
| Anexo 14 tipo 2 (ventas) | 552 / 553 | same; the 105/150 formulas subtract (01 FR-007/FR-008) |
| Anexo 15 | 92 (informativo detail) | casilla owned by 01 FR-004; auto-total basis unprinted (OQ-002) |
| Anexo 16 | 65 (informativo detail) | casilla owned by 01 FR-010; F4→F7 hand-off per 03 §1 |
| Anexo 17 | — (no casilla) | informativo, closed window |

Integration note: the generic upload entity of 01 §4
(l10n_sv.f07.annex.upload) serves annexes 14-17 here — its annex_no
domain extends to 17; Anexo 13 never appears in it (manual grid,
FR-124).

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic
living in the LGPL client. No SaaS rows are introduced: none of these
FRs touch DTE generation/transformation (an architecture-split
surface per `shared/docs/saas-thin-client-architecture.md`). Model
names are stable across Odoo 17/18/19/20; version-specific behavior is
recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-124 | odoo | l10n_sv.f07.annex13.entry + l10n_sv.f07.fuel.regime | manual-grid enablement | D12: window Mar-2022 + Decreto 321 vigencia; NO file surface (01 upload engine bypassed); successor status for 2026 unpinned — OQ-001; AC-001 |
| FR-125 | odoo | l10n_sv.f07.annex13.entry | direction/grade/net base | Global aggregates net of IVA; 13%-rate ops excluded (files 02/03 territory); AC-002 |
| FR-126 | odoo | l10n_sv.f07.annex13.entry + l10n_sv.f07.casilla.value (01 file) | 586/587, 588/589 | Companions = grade rate × base; rate values = regime configuration (OQ-001); 2dp per 01 FR-027; AC-001/AC-003 |
| FR-127 | odoo | l10n_sv.f07.annex14.row + l10n_sv.f07.fuel.regime | NC-only gate + window | D12: Abr-2022 + Ley Especial Transitoria vigencia; tipo 05 only, issued and/or received; AC-004 |
| FR-128 | odoo | l10n_sv.f07.annex14.row | full A-P column model | J tipo de combustible 1/2/3 encoded; K 11+8 exception (K/N/O structure-table counts = print defects — semantics govern); D/E/F identifier fills = canonical mapping (printed confirmation); G/H XOR; AC-005/AC-010 |
| FR-129 | odoo | l10n_sv.f07.annex14.row + l10n_sv.f07.casilla.value (01 file) | 550-553 wiring | Tipo 1 → 550/551; tipo 2 → 552/553; positive-magnitude convention (01 FR-019); label-match basis — OQ-002; AC-004 |
| FR-130 | odoo | l10n_sv.f07.annex15.row + l10n_sv.f07.fuel.regime | informativo + window | A-I map encoded (LB-003); E/F equality cross-refs = print defects; CT 111 anulados window printed on dates; casilla 92 owned by 01 FR-004; no companion; fin-de-obra end semantics — OQ-005; AC-006 |
| FR-131 | odoo | l10n_sv.f07.annex16.row + l10n_sv.f07.fuel.regime | informativo + window | A-L map encoded (LB-004); Tesorería pseudo-NIT 06140108140066 for foreign tipo-12 (twin of 03's FR-074); C-list copy defect — tipos 01/12 operative; casilla 65 owned by 01 FR-010; F4→F7 hand-off recorded in 03 §1; AC-006/AC-010 |
| FR-132 | odoo | l10n_sv.f07.annex17.row + l10n_sv.f07.fuel.regime | closed window + CCF-only | A-N map as printed (duplicated-L noted); galones standard 2dp (vs 14's 11+8); no casilla feed; informativo; AC-007/AC-010 |
| FR-133 | odoo | l10n_sv.f07.fuel.regime | window-gating engine | Windows as dated data; regime-active flag from decree status; AC-001/AC-006/AC-007 |
| FR-134 | odoo | l10n_sv.f07.fuel.regime | closed-vintage semantics | Anexo 17 permanently closed post-Ago-2022; historical-window filings still served; open regimes close by decree-status update only; AC-007 |
| FR-135 | odoo | l10n_sv.f07.annex.upload (01 engine) + annex14-17 rows | export inheritance | 01 FR-028..041 apply unchanged; galones 8-decimal exception; 13-17 modificatoria carryover unprinted — OQ-004; AC-008 |
| FR-136 | odoo | l10n_sv.f07.casilla.value (01 file) + §4 wiring | wiring interface | No manual casilla fill (01 FR-038); FOVIAL/COTRANS pointer open — OQ-003; AC-009 |

Version-regime notes (D12): this file is entirely dated-regime
territory — every surface's availability is governed by the
l10n_sv.f07.fuel.regime seed (FR-133), so a decree change re-dates the
behavior by data, not code. Anexo 13's force status for 2026 (Decreto
321 successor) and the differentiated-rate values per grade are unpinned
(OQ-001). Anexo 17 is the one fixed closed vintage (Jun-Ago 2022). The
v14 manual vintage governs the row models (a future manual revision
re-seeds them). The filing due-day windows remain F12 territory
(`08_filing-calendar.md`; SOQ-08) — no deadline behavior is encoded
here. Cross-file canonicality: SV-FREP-FR-042/043 (02) own the
identifier mapping; SV-FREP-FR-004/005/010/011 (01) own every casilla
this file feeds.

## 6. Acceptance Criteria

- **AC-001:** Given the Decreto 321 regime-active flag true with window
  start Mar-2022, when an Anexo 13 grid is saved for period 03/2022,
  then the values are accepted; for period 02/2022 the grid is
  unavailable (pre-window); and given the decree status turns inactive
  with end month E, then periods after E leave the annex unavailable
  and casillas 586-589 read 0.00 (FR-124, FR-133).
- **AC-002:** Given June sales of SUPERIOR fuel at differentiated rates
  with net base 1,000.00 and DIÉSEL purchases with net base 500.00,
  then casilla 586 = **1,000.00** and casilla 588 = **500.00**, neither
  including IVA; and given a fuel sale at the general 13% rate, then it
  produces NO Anexo 13 entry and lands in the annex 1/2 rows (casillas
  95/96) per the printed exclusion (FR-125).
- **AC-003:** Given a SUPERIOR rate configuration of 0.05, then casilla
  587 = 0.05 × 1,000.00 = **50.00** rounded to two decimals (rate
  values consumed as configuration — OQ-001) (FR-126).
- **AC-004:** Given an Anexo 14 row whose document is a CCF (03), then
  the row is rejected — only tipo 05 NC rows are admitted; given a
  received NC (tipo operación 1 COMPRAS) with descuento 100.00 and IVA
  del descuento 13.00, then casilla 550 = **100.00** and 551 =
  **13.00** (positive magnitudes; the 100/145 formulas' minus signs
  subtract); and given an issued NC (tipo 2 VENTAS) with the same
  values, then 552 = **100.00** and 553 = **13.00** (FR-127, FR-129).
- **AC-005:** Given an Anexo 14 row with galones 150.12345678 and
  precio 4.56, when the row is exported, then the galones cell reads
  exactly `150.12345678` (the 8-decimal exception) while every monetary
  cell keeps the two-decimal discipline (FR-128, FR-135).
- **AC-006:** Given a Decreto 357 exempt-internal-sale row dated
  06/2022, then the Anexo 15 row is accepted as informativo detail of
  casilla 92 with NO débito companion; given the same row dated 04/2022,
  then it is rejected (pre-window); and given an exempt purchase row
  dated 07/2023 with the obra still open, then the Anexo 16 row is
  accepted as informativo detail of casilla 65 (FR-130, FR-131,
  FR-133).
- **AC-007:** Given an Anexo 17 CCF row dated 07/2022, then it is
  accepted (informativo, no casilla); given the same row dated 09/2022
  or 05/2026, then it is rejected — the closed vintage never
  re-activates; and given a non-CCF row dated 07/2022, then it is
  rejected (FR-132, FR-134).
- **AC-008:** Given a validated Anexo 14 export, then the file follows
  the generic engine (semicolon delimiter, Text cells, filename ≤25
  characters + .CSV, last column = 14, full replace on re-upload) with
  the galones cell as the only 8-decimal exception; and no file is ever
  produced for Anexo 13 (FR-124, FR-135).
- **AC-009:** Given Anexo 13/14 feeds for a period, then casillas
  586/587/588/589 and 550-553 re-total automatically with no manual
  casilla edit (SV-FREP-FR-038), and Anexos 15/16/17 add no term to any
  SUMA formula beyond their informativo detail (FR-136).
- **AC-010:** Given an Anexo 14 row with J = 2 and K = 150.12345678,
  then the row exports as tipo de combustible REGULAR with the
  8-decimal gallons cell; given an Anexo 17 row carrying the same
  gallons value, then its export writes `150.12` (standard two-decimal
  discipline — the 11+8 exception is Anexo 14 only); and given an
  Anexo 16 row from a foreign tipo-12 supplier, then E reads exactly
  `06140108140066`, F reads the Tesorería's name and K (DUI) is empty
  (FR-128, FR-131, FR-132).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | Decreto 321 dated-regime status and rates (34_-file OQ-4 carried): (a) is Decreto 321 (or a successor) still in force for 2026 — the regime-active flag of FR-133 and the Mar-2022+ availability of Anexo 13 depend on it; (b) the differentiated IVA rate VALUES per fuel grade (SUPERIOR/REGULAR/DIÉSEL) are not in the corpus — FR-126 consumes them as dated regime configuration, and 587/589   cannot compute until seeded. Acquire Decreto 321 (and the Ley Especial
  Transitoria's duration text for the Anexo 14 window) via the
  special-regimes wave / sources registry. | no | Takumi S3 (sources registry) + special-regimes/taxation waves | open |
| OQ-002 | Auto-complement column bases (trimmed 2026-08-18 after the full §XXI-§XXIV column maps were encoded from the manual txt — LB-002..005; the former A-P letter-map and trailing-annex-number items are dissolved: P=14, I=15, L=16, N=17 are printed, and the issued/received → tipo-operación mapping is printed verbatim): (a) casillas 550-553 — §XXI prints only the generic sentence "el sistema complementará automáticamente, las casillas de los descuentos de compras y/o ventas de combustibles con su correspondiente crédito y/o débito fiscal, con los valores del anexo cargado"; WHICH columns total into each casilla (N descuento vs M valor-operación; the O companion basis) is unprinted — FR-129 encodes the label match (descuento → 550/552; IVA del descuento → 551/553). (b) Anexos 15/16 — whether G (and the 65-side buckets) auto-total casillas 92/65 or the annexes only detail them is unprinted (both are marked informativa; upload entry via the casilla pencils). Confirm both bases against MH auto-complement behavior. | no | Takumi S3 | open |
| OQ-003 | FOVIAL/COTRANS interplay (casilla 525; 31_ guide pointer): the per-gallon quantity-tax credit design decision stays OPEN with the taxation/special-regimes waves (01 §7 OQ-003 kin). This file's fuel surfaces record the pointer only — no FR encodes the interplay. | no | special-regimes/taxation waves (pointer recorded by Takumi S3) | open |
| OQ-004 | Annexes 13-17 modificatoria carryover: manual §XVII prints the carryover for "anexos 3 al 12" only — the fate of annexes 13-17 (and the Anexo 13 manual grid) in amended returns is unprinted. FR-135 does not assert it (kin to `04_f07-annexes-retentions-events.md` OQ-004 for §XIX). Confirm against MH system behavior. | no | Takumi S3 | open |
| OQ-005 | "Fin de la obra" window-end semantics for Anexos 15/16: whether the Decreto 357 window ends per-taxpayer/per-project (an obra-completion fact Odoo must store per company) or by a global decree-level end date is not elaborated in the manual extract. FR-133/FR-130 encode the end as dated data; the seed table leaves end_kind open. Confirm from Decreto 357 text (acquisition candidate; special-regimes wave kin). | no | Takumi S3 (sources registry) + special-regimes wave | open |
