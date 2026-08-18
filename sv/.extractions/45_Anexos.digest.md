# DIGEST — Anexos of Normativa de Cumplimiento DTE v2.0 (2026-05-25)

Source: `45_Normativa_Cumplimiento_DTE_v2.0_2026-05-25.pdf.txt` (OCR). Page citations use `=== PAGE n ===` markers.
Anexo page map: Anexo I pp.36–47 · Anexo II pp.48–80 · Anexo III pp.81–101 · Anexo IV pp.102–122 · Anexo V pp.123–135 · Anexo VI (MODIFICACIONES, changelog) pp.136–137.
Anexo II is ONE unified table, fields N° 1–174 + N° 175 `selloRecibido`; each row lists which DTE types use the field ("Documento" column). Anexo III same pattern for events, fields 1–120 + 121 sello. "Per-type field count" below = tally of rows whose Documento column includes that type (best effort from garbled OCR — treat all counts as approximate [?]).

---

## 1. Per-DTE-type structure deltas (ANEXO II, pp.48–80)

### 1.0 Authoritative version numbers (Anexo IV field 1, p.102 — use this, Anexo II OCR of field 1 is ambiguous)

| DTE | versión JSON (v2.0 normativa) | 2022-era |
|---|---|---|
| FE | **2** | 1 |
| CRE | **2** | 1 |
| CLE | **2** | 1/2 |
| DCLE | **2** | 1 |
| FSEE | **2** | 1 |
| CDE | **2** | 1 |
| FEXE | **3** | 1 |
| CCFE | **4** | 3 |
| NRE | **4** | 3 |
| NCE | **4** | 3/4 |
| NDE | **4** | 3/4 |

- Anexo II field 1 (p.48) OCR groups FEXE with the "valor 2" list — **contradicted by Anexo IV field 1 (p.102): "Se ingresará 3 para: FEXE"**. Anexo IV is explicit; Anexo II reading likely garbled.
- All 11 types get the version bump (Anexo VI row "2.0 / ANEXOS II": "Se actualiza campo 1 'Versión' para todos los DTE", p.136).

### 1.1 Section layout (Anexo II)

Sección 1 IDENTIFICACIÓN (fields 1–13) · 2 DOCUMENTOS RELACIONADOS (14–17) · 3 EMISOR (18–37) · 4 RECEPTOR (38–57) · 5 DOCUMENTOS ASOCIADOS (58–68) · 6 VENTAS POR CUENTA DE TERCEROS (69–71) · 7 COMPRA POR CUENTA DE TERCEROS (72–73, FEXE only) · 8 CUERPO (74–122) · 9 RESUMEN (123–168) · 10 EXTENSIÓN (169–171, DCLE only) · 11 APÉNDICE (172–174) · 12 SELLO DE RECEPCIÓN (175).
Emisor roles (p.38 & p.51): CRE emisor = Agente de Retención, receptor = Sujeto de Retención; CLE emisor = Comisionista, receptor = Mandante; DCLE emisor = Agente Perceptor, receptor = Afiliado; FEXE emisor = Exportador; FSEE receptor = Sujeto Excluido; CDE emisor = Donatario, receptor = Donante.

### 1.2 Best-effort per-type field tallies (rows including the type; ±1–2 due to OCR) [?]

| Type | ~fields v2.0 (incl. sello 175) | 2022 baseline | Delta notes |
|---|---|---|---|
| FE | ~102 [?] | 107 | -Extensión, -reteRenta; +28/49 distrito, +71 domicilioFiscal ventaTercero, +84 tributoSujetoIVA |
| CCFE | ~100 [?] | ~106 | -Extensión, -reteRenta; +28/49, +71, +84 |
| NRE | ~83 [?] | n/a | +28/49, +71, +84 |
| NCE | ~87 [?] | n/a | +13 fusiones, +98–101, +143–146, +151, +153, -40 NIT receptor, -global discounts/subTotal |
| NDE | ~88 [?] | n/a | same pattern as NCE |
| CRE | ~58 [?] | 61 | +13 fusiones, +157 IVA 13%, +168 observaciones |
| CLE | ~70 [?] | n/a | +13 fusiones, +53 domicilioFiscal receptor |
| DCLE | **64** (tally matches baseline exactly) | 64 | -emisor/receptor MH establecimiento codes, -tipoEstablecimiento emisor |
| FEXE | ~96 [?] | 85 | +Secc.2 doc.relacionados, +Secc.7 (72–73), +36, +38/39, +49, +75, +80, +84, +96, +136–138, +152 |
| FSEE | ~66 [?] | 64 | -142 ivaRetenido (removed for FSEE), +28/49 |
| CDE | ~61 [?] | 60 | +28/49 distrito |

### 1.3 NEW fields / keys in v2.0 (per Anexo VI changelog p.136–137, cross-checked against Anexo II rows)

- `identificacion.fusiones` (N°13, p.49; applies NCE, NDE, CRE y CLE) — NIT del fusionado, art. 69 inc. 1 LST; 9 o 14 dígitos; null si no aplica; NIT must be in "lista de contribuyentes fusionados" (Anexo IV N°13, p.103). **NEW**.
- Sección 2 DOCUMENTOS RELACIONADOS **now applies to FEXE** (fields 14–17) — NEW for FEXE.
- Sección 7 COMPRA POR CUENTA DE TERCEROS, N°72 `compraTercero.numDocumento`, N°73 `compraTercero.nombre` (pp.60–61, FEXE only) — the known Nov-2025 v1.2 addition; retained in v2.0. Receptor must be "enlistado como operador logístico por la AT" when 72 is filled (Anexo IV N°72, p.109).
- N°28 `emisor.direccion.distrito` (CAT-008) and N°49 `receptor.direccion.distrito` — changelog lists both as additions; must correspond with Departamento/Municipio.
- N°36 `emisor.tipoRegimen` (CAT-033 "Tipo de Régimen", FEXE; required when Tipo de exportación = 1, null when 2) — NEW.
- N°38 `receptor.tipoDocumento` / N°39 `receptor.numDocumento` extended coverage (changelog lists them as additions; FEXE context) [?].
- N°53 `receptor.domicilioFiscal` (CAT-032, applies CDE y CLE) and N°71 `ventaTercero.domicilioFiscal` (CAT-032, applies FE, CCFE, NRE, NCE, NDE y FEXE) — NEW pair. CLE must copy the code from "FE V2, CCFE V4, NCE V4, NDE V4 o FEXE V3" being liquidated (Anexo IV N°53, p.107).
- N°84 "Tributo sujeto a cálculo de IVA" — JSON key OCR-garbled (fragments `...¿Tribal` / `codTr...`, pp.63, 108–109; Anexo V N°76 fragment `cuerpoDocumento.codTr…`); applies FE, CCFE, NRE, NCE, NDE y FEXE; codes A8, 57, 90, A6 (sección 2 CAT-015); requires Tipo de item = 4, cantidad = 1, precioUnitario = valor del tributo. NEW key — exact spelling unresolvable from OCR [?].
- N°83 `cuerpoDocumento.codigo` (F-983 inventory code) listed as addition [? changelog]; N°86 `descripcion` length extended to **1500** ("Se amplía longitud de campo 83 'Descripción'" — changelog numbering differs from table numbering [?]).
- NCE/NDE item-level: N°98 `noGravado` (Cargos/Abonos que no afectan la base imponible), N°99 `ivaPerci`, N°100 `iva13` (ajuste IVA 13% de CR por personas naturales inscritas IVA), N°101 `ivaRete`; summary: N°143 `totalIvaPercibido`, N°144 `codigoRetencionMH`, N°145 `totalIvaRetenido`, N°146 `totalIva13`, N°151 `totalNoGravado`, N°153 `totalPagar` — NEW for NCE/NDE.
- FEXE: N°75 tipoItem (codes 1/2 only; 4 with authorization; 3 forbidden), N°80 numeroDocumento relacionado, N°96 tributos, N°136–138 resumen tributos, N°152 `resumen.totalNoOnerosa` ("Transferencias de bienes no onerosas", art. 77 LST; FEXE only) — NEW for FEXE.
- N°157 `resumen.iva13` **para CRE** — NEW for CRE (calculated on monto sujeto a retención, no effect on Total IVA retenido, art. 162 inc. 7° CT).
- N°168 `resumen.observaciones` (max 3000) — NEW (FE, CCFE, NRE, NCE, NDE, CRE, CLE, FEXE, FSEE).

### 1.4 REMOVED fields (Anexo VI, pp.136–137)

- "Tipo de establecimiento (Emisor)", "Código del establecimiento asignado por el MH (Emisor)", "Código del Punto de Venta (Emisor) asignado por el MH", "Código del establecimiento asignado por el MH (Receptor)", "Código del Punto de Venta (Receptor) asignado por el MH" — **eliminados para DCLE**. (N°32/33 `codEstablecimiento`/`codPuntoVenta` remain as *internal, optional* codes for most types; N°46 tipoEstablecimiento receptor remains DCLE-only.)
- `receptor.nit` (N°40) **eliminado para NCE, NDE y CLE** — Anexo II N°40 now applies **CCFE y DCLE** only (p.54).
- "IVA Retenido" **eliminado para FSEE** (summary N°142 not in FSEE's column).
- Para NCE y NDE: "Monto global de Descuento, Bonificación, Rebajas y otros a ventas no sujetas/exentas/gravadas" (N°130–132 not in NCE/NDE columns), "Porcentaje de descuento" (N°134), "Sub Total" (N°139), resumen "IVA percibido" (N°141) e "IVA retenido" (N°142) — eliminated; replaced by N°143–146 totals.
- "Retención renta" para **FE, CCFE, NCE y NDE** eliminated (N°147 is FSEE-only).
- **Sección 10 EXTENSIÓN eliminada para FE, CCFE, NRE, NCE, NDE, CRE, CLE, FEXE, FSEE y CDE** — now DCLE-only (N°169–171).

### 1.5 Required vs conditional highlights (Anexo II)

- N°8 `identificacion.tipoContingencia` / N°9 `motivoContingencia`: only when tipoTransmisión = 2; N°9 required only if tipoContingencia = 5, else null. Aplican FE, CCFE, NRE, NCE, NDE, CRE, FEXE y FSEE (i.e., **contingency-allowed types; CLE, DCLE, CDE excluded**).
- N°38/39/42 (FE): "Requerido por tipo de operación" — null allowed when "Monto Total de la Operación" < monto legalmente establecido (the $200 figure is NOT restated in the Anexos).
- N°41 NRC receptor: null when receptor has no NRC / when related doc also null.
- N°78–81 (CRE/CLE cuerpo): tipoDocRelacionado/tipoGeneracion/numeroDocRelacionado/fechaGeneracion — CRE = requerido; CLE = requerido por tipo de operación.
- N°93 `exportaciones` (CLE only): negative values when informed FEX is invalidado/anulado; FEXE V3 formula "Total gravadas − descuento global + seguro + flete"; Evento de retorno uses "Suma de operaciones".
- N°103–105 (CRE cuerpo): montoSujetoGrav[?] (OCR key fragment `montoSujet…oGrav`, p.69 [?]) sin IVA; codigoRetencion CAT-006; ivaRetenido = monto × % legal.
- N°106–122 (DCLE cuerpo): periodo liquidación fechas, codigoLiquidacion, cantidadDocumentos, valorOperaciones, valoresSinPercepcion, descripcionSinPercepcion, observaciones, subTotal, montoSujetoPercepcion, ivaOperacionesLiquidar [? `ivaO…`], ivaPercibido (2%), comision, porcentajeComision, ivaComision, valorLiquidoPagar [? `…idoApagar`], totalLetras.
- Item limits: cuerpo max **2000** ítems (CRE y CLE **500**) — p.61 & Anexo IV N°74; documentos relacionados max **50** docs / **2000** ítems; otrosDocumentos **1–10** (FEXE **1–20**); apéndice max **10**.

---

## 2. Event structures (ANEXO III, pp.81–101)

One unified table (fields 1–120 + 121 sello) covering 4 events: **Invalidación, Contingencia, Retorno (18), Operaciones Especiales (17)**. Versions (Anexo V N°1, p.123): **Invalidación y Contingencia = 3; Retorno y Operaciones Especiales = 1**. (Anexo II-equivalent Anexo III N°1 OCR was contradictory; Anexo V is explicit.)

### 2.1 Sección map & per-event fields

- **Sección 1 IDENTIFICACIÓN DEL EVENTO** (1–14): `version` (1), `ambiente` (2), `tipoModelo` (3 — código 1 previo for Retorno/OpEsp; código 2 en contingencia para Retorno), `tipoTransmision` (4 — normal solo con modelo previo), `tipoContingencia` (5, CAT-005, Retorno only), `motivoContingencia` (6, only code 5), `codigoGeneracion` (7, UUID v4 uppercase), `tipoEvento` (8, CAT-002: **18 = Retorno, 17 = Operaciones especiales**; NOT present for Invalidación/Contingencia), `fecEmiEvento` (9 — Retorno y OpEsp), `fecEvento` (10 — Contingencia), `horEmiEvento` (11 — Invalidación, Retorno y OpEsp), `horEvento` (12 — Contingencia), `fusiones` (13 — Invalidación y Retorno; NEW), `tipoMoneda` (14 — "Debe ser USD"; Retorno y OpEsp; NEW).
- **Sección 2 DOCUMENTOS RELACIONADOS** (15–17, Retorno only): `documentoRelacionado.tipoDte` (solo códigos **01 FE, 11 FEXE, 14 FSEE**), `.codigoGeneracion` (max 50 docs, mismo tipo, con Sello), `.fechaEmision`.
- **Sección 3 IDENTIFICACIÓN DEL EMISOR** (18–33): `nit` (18), `nombre` (19), `nombreResponsable` (20, Contingencia), `tipoDocResponsable` (21), `numeroDocResponsable` (22), `tipoEstablecimiento` (23, Contingencia), `codEstablecimientoMH` (24 — Invalidación, Contingencia y Retorno; MH structure "(M000, S000, B000, P000)" per Anexo V N°24 [OCR: "MO00, $000, 8000, PO00"]), `codEstablecimiento` (25, interno, opcional), `codPuntoVentaMH` (26 — Invalidación, Contingencia y Retorno), `codPuntoVenta` (27, interno), `recintoFiscal` (28, CAT-027, FEXE), `tipoRegimen` (29, CAT-033), `regimen` (30, CAT-028 "Régimen de exportación"), `tipoItemExpor[?]` (31 — "Tipo de exportación" para FEXE, códigos 1 o 2; key OCR `emisor.ti…poltemExpor` [?]), `telefono` (32), `correo` (33).
- **Sección 4 INFORMACIÓN DEL DOCUMENTO/EVENTO EN CONTINGENCIA** (34–36, Contingencia): `detalleDTE.numeroItem` (34, max **1000 ítems** — "más de 1000 documentos ⇒ nuevo evento de contingencia"), `detalleDTE.tipoDteContingencia` (35), `detalleDTE.codigoGeneracion` (36). Allowed types in contingency (Anexo III p.86 line "Se podrán emitir en contingencia…"; identical in Anexo V N°35, p.126): **01-FE, 03-CCFE, 04-NRE, 05-NCE, 06-NDE, 07-CRE, 11-FEXE, 14-FSEE y 18-Evento de retorno**.
- **Sección 5 MOTIVO DE LA CONTINGENCIA** (37–42, Contingencia): `motivo.fInicio` (37), `motivo.fFin` (38), `motivo.hInicio` (39), `motivo.hFin` (40), `motivo.tipoContingencia` (41, CAT-005), `motivo.motivoContingencia` (42, solo código 5).
- **Sección 6 DETALLE DE APLICACIÓN DEL EVENTO** (43–55, Invalidación + some Retorno): `documento.tipoDte` (43), `documento.codigoGeneracion` (44, **un código por evento**), `documento.selloRecibido` (45), `documento.numeroControl` (46 — null si tipoDTE 16/17/18), `documento.fecGeneracion` (47), `documento.codigoGeneracionR[?]` (48 — DTE que reemplaza, solo tipoInvalidación 1 o 3), `documento.tipoDocumento` (49, receptor, Retorno too), `.numDocumento` (50), `.nombre` (51), `.codPais` (52, Retorno/FEXE), `.nombrePais` (53), `.telefono` (54), `.correo` (55).
- **Sección 7 VENTAS POR CUENTA DE TERCEROS** (56–58, Retorno): `ventaTercero.nit` (56), `.nombre` (57), `.domicilioFiscal` (58, CAT-032 — NEW).
- **Sección 8 COMPRA POR CUENTA DE TERCEROS** (59–60, Retorno): `compraTercero.numDocumento` (59), `.nombre` (60) — NEW section in events.
- **Sección 9 CUERPO** (61–88, Retorno y OpEsp; max 2000): `numeroItem` (61), `codigoGeneracionRef` (62, OpEsp — refiere Evento de Operaciones Especiales activo), `tipoDocumento` (63, **CAT-023 "Operaciones especiales"**, códigos 02 y 97 [?]), `numDocumento` (64, solo código 97), `fechaEmision` (65), `tipoItem` (66, CAT-011, Retorno; FEXE sin código 3), `codigoGeneracion` (67, Retorno — todos los códigos de la Sección 2 en los ítems), `cantidad` (68 — enteros > 0 en OpEsp; 1 para cargos/abonos o tipoItem 4), `codigo` (69, F-983), `uniMedida` (70, 99 en cargos/abonos o tipoItem 4), `descripcion` (71, max 1500), `precioUni` (72), `DocDel` (73 — inicio de rango, código 02), `DocAl` (74 — fin de rango, código 02), `montoDescu` (75), `codTributo[SujetoIVA?]` (76 — same garbled key as DTE N°84 [?]; null si FSEE, o FE/FEXE con tipoItem ≠ 4), `ventaNoSuj` (77), `ventaExenta` (78), `ventaGravada` (79), `compra` (80 — "Compras a sujetos excluidos", FSEE), `tributos` (81, CAT-015 secciones 1 y 3; FEXE excepto 20), `psv` (82, FE), `ivaItem` (83, FE), `noGravado` (84), `ivaRetenido` (85, FE), `reteRenta` (86, FSEE × 10%), `seguro` (87, FEXE), `flete` (88, FEXE).
- **Sección 10 RESUMEN** (89–109): `totalNoSuj` (89), `totalExenta` (90), `totalGravada` (91), `totalCompraExc[luidos]` (92 [? key OCR `totalCompraExc…`], Retorno), `subTotalVentas` (93, Retorno = NoSuj+Exe+Grav+CompraExcl), `subTotal` (94, OpEsp), `totalNoGravado` (95), `totalSeguro` (96), `totalFlete` (97), `montoTotalOperacion` (98, Retorno = Suma + tributos + seguro + flete), `totalIvaRetenido` (99), `totalRetencionRenta` (100), `tributos.codigo` (101), `tributos.descripcion` (102), `tributos.valor` (103 — $0.00 si código C3), `total` (104, OpEsp = subTotal + valor tributo), `totalPagar` (105, Retorno = montoTotal − IVA retenido − reteRenta ± cargos; $0.00 si cargos > monto), `totalLetras` (106), `totalNoOnerosa` (107, FEXE/Retorno), `iva13` (108, informativo, FE), `saldoFavor` (109, opcional).
- **Sección 11 MOTIVO DEL EVENTO** (110–117, Invalidación): `motivo.tipoInvalidacion` (110, CAT-024), `motivo.motivoInvalidacion` (111, 1–200), `nombreResponsable` (112), `tipDocResponsable` (113), `numDocResponsable` (114), `nombreSolicita` (115), `tipDocSolicita` (116), `numDocSolicita` (117).
- **Sección 12 APÉNDICE** (118–120, **Retorno y Operaciones Especiales only** — per Evento column pp.100–101; apéndice NOT available for Invalidación/Contingencia in v2.0 table [? differs from 2022 invalidación which had apéndice]).
- **Sección 13 SELLO DE RECEPCIÓN** (121, all events).

### 2.2 Field-count estimates per event [?]

- Invalidación ≈ 33 (+sello): Sec1 {1,2,7,11,13} + Sec3 {18,19,24,25,26,27,32,33} + Sec6 {43–48,49,50,51,54,55} + Sec11 {110–117}. 2022 baseline = 36. Removed per Anexo VI: "Tipo de establecimiento (Emisor)", "Nombre de casa matriz, sucursal/agencia, predio/patio, bodega (Emisor)", "Monto Total de la Operación (del DTE a invalidar)". Added: fusiones (13) [y N°8 tipoEvento no aplica a invalidación].
- Contingencia ≈ 24 (+sello): Sec1 {1,2,10,12} + Sec3 {18–24,26,32,33} + Sec4 {34,35,36} + Sec5 {37–42}. 2022 baseline = 25. Delta: detalleDTE cap now **1000** (2022 era 500 [? not restated here]); emisor gained codEstablecimientoMH/codPuntoVentaMH.
- Retorno (not in 2022) ≈ 80 fields incl. Secciones 2, 6–10, 12.
- Operaciones Especiales (NEW event) ≈ 37 fields; **emitted only by "contribuyentes designados por la A.T."** (Anexo V N°18, p.125); body/resumen designed for informing internal-control documents (CAT-023 codes 02 rango / 97 individual [?]).

### 2.3 New JSON keys in events vs 2022 invalidación/contingencia (per Anexo VI, p.137 + table)

Added: 3 `tipoModelo`, 4 `tipoTransmision`, 5 `tipoContingencia`, 6 `motivoContingencia`, 8 `tipoEvento`, 13 `fusiones` [changelog numbering "16"], 15/16/18/19/20 documento-relacionado trio (Retorno), 28 `recintoFiscal`, 29 `tipoRegimen`, 30 `regimen`, 31 `tipoItemExpor[?]`, 47/48 tipoGeneracion/numeroDocRelacionado, 52/53 codPais/nombrePais, 56–58 ventaTercero trio (incl. NEW `domicilioFiscal`), 59–60 compraTercero (NEW), entire Sección 9 CUERPO, entire Sección 10 RESUMEN, Sección 12 APÉNDICE. (Changelog's own field numbers — "del 67 al 96", "97 al 122", "131 al 133" — do not match the table's 61–88 / 89–109 / 118–120 numbering [?]; both quoted.)

---

## 3. Validation rules (ANEXO IV pp.102–122, ANEXO V pp.123–135)

### 3.1 Anexo IV — DTE (field → rule, compact)

**Identificación**
- 1 Versión → 2 (FE, CRE, CLE, DCLE, FSEE, CDE); 3 (FEXE); 4 (CCFE, NRE, NCE, NDE). Entero sin cero/punto a la derecha [sic — "a la derecha" is OCR; means leading zeros/decimal point].
- 2 Ambiente → CAT-001; 00 pruebas / 01 producción.
- 3 tipoDte → CAT-002.
- 4 codigoGeneracion → único por documento, 36 chars incl. guiones, UUID v4, **solo números y letras MAYÚSCULAS**.
- 5 numeroControl → 31 chars (DTE + 2 tipo + 8 estab/PV + 15 consecutivo); posiciones 1–4 de sección 3: "M"/"B"/"S"/"P" + 3 números; posiciones 5–8: "P" + 3 números; **no repetirse del 01 enero al 31 diciembre; el consecutivo se REINICIA a partir del primer DTE de cada ejercicio impositivo (year-reset)**.
- 6 Modelo facturación → CAT-003; código 1 = previo con transmisión normal; **código 2 en contingencia** (doc column: FE, CCFE, NRE, NCE, NDE, CRE, FEXE y FSEE — CLE/DCLE/CDE solo reglas 1–2, i.e., sin modelo 2).
- 7 Tipo transmisión → CAT-004; código 1 normal con modelo previo; **código 2 en contingencia** (mismos 8 tipos).
- 8 tipoContingencia → null si transmisión = 1; CAT-005 (1–5) si transmisión = 2 (mismos 8 tipos).
- 9 motivoContingencia → requerido si tipoContingencia = 5; null en los demás casos.
- 10 fecEmi → YYYY-MM-DD; puede anteceder a transmisión (FEXE y CDE: casos especiales; FSEE: período anterior); **hasta 5 días posteriores a transmisión en casos excepcionales, sin sobrepasar el siguiente período tributario** (ej.: transmitido 27-jun ⇒ fecEmi 28/29/30-jun ok, 01/02-jul no).
- 11 horEmi → HH:MM:SS; holgura 30 min el último día del mes.
- 12 tipoMoneda → USD.
- 13 fusiones → null si no hay fusión; NIT 9 o 14 dígitos; debe estar en lista de contribuyentes fusionados de la AT.

**Documentos relacionados (14–17)** — NCE/NDE obligatoria; máx 50; mismo tipo en un mismo DTE; no relacionar electrónicos invalidados/rechazados; el mismo número puede referenciarse en varios DTE una sola vez cada uno; correspondencia emisor/receptor. tipoDoc: FEXE puede 04-NR; FE/CCFE pueden 04-NR, 08-CL, 09-DCL; NCE/NDE requieren 03-CCF o 07-CR; NRE solo 01-FE, 03-CCFE o 11-FEXE. Plazos (N°17): FE/CCFE/FEXE que relaciona NR ⇒ mismo período o máx 3 días siguientes; FE/CCFE relacionando DCL ⇒ mismo período; NCE/NDE relacionando CCF/CR ⇒ máx 3 meses.

**Emisor (18–37)** — NIT registrado como contribuyente IVA activo (RUC) + autorizado emisor DTE; 9 o 14 dígitos sin guiones; NCE/NDE ajustando CR validan agentes retenedores no inscritos; NRC con correspondencia NIT, null cuando aplique; actividad económica CAT-019 y su nombre; distrito (CAT-008) corresponde a depto/municipio; teléfono 8–30; correo con dominio de nivel superior válido; FEXE: tipo exportación CAT-011 sin códigos 3 y 4; recinto CAT-027 y tipoRégimen CAT-033 solo exportación = 1; régimen CAT-028 requerido si tipoItem 1 o 3, null si 2 (Servicios).

**Receptor (38–57)** — DUI = 9 dígitos; NIT receptor (CCFE/DCLE) debe poseer NRC activo; 40 nit solo CCFE y DCLE (ver remociones); CLE: numDocumento = NIT del tercero, no informar DTE con ventaTercero null; CRE electrónico: emisor del CR = receptor del doc informado y viceversa; distrito opcional en FE pero codificado si se llena; complemento null si departamento null; codPais CAT-020 (FEXE destino exportación / CDE nacionalidad donante); domicilioFiscal CAT-032 (CDE y CLE); bienTitular CAT-025 (NRE); tipoPersona CAT-029 (FEXE).

**Documentos asociados (58–68)** — 1–10 (FEXE 1–20); código 3 médico solo FE y CCFE (CAT-010 servicio médico, NIT médico null si usa doc de identificación de médico no domiciliado); código 4 transporte solo FEXE (CAT-030 modo y placa); CDE: código 1 + resolución donatario art. 6 LISR obligatorio.

**Venta/Compra por cuenta de terceros (69–73)** — emisor ≠ tercero; correspondencias NIT con documento relacionado; null si doc relacionado 08-CL/09-DCL o 07-CR; domicilioFiscal código 1 "Domiciliado" ⇒ NIT inscrito en IVA; copiar domicilioFiscal del doc relacionado FE V2 / CCFE-NCE-NDE V4 / FEXE V3; compraTercero (FEXE): receptor debe estar enlistado como **operador logístico** por la AT.

**Cuerpo (74–122)** — ítems: consecutivos > 0; máx 2000 (CRE y CLE 500); tipoItem 4 solo con justificación/autorización (FEXE, NRE-relacionando-FEXE); NRE relacionando FEXE: solo códigos 1 o 2; FSEE sin código 4; cantidad = 1 en cargos/abonos, tipoItem 4, NCE/NDE ajustando CRE, donación en efectivo; descuento ≤ monto del ítem; NCE/NDE ajustando CRE: ventaNoSuj/Exenta/Gravada = $0.00, la suma de ajustes no puede exceder "Total de operaciones X − descuento global" del CCFE, y (código 07) los ajustes no exceden "Total monto sujeto a retención" del CRE; CLE: positivos F/CCF/ND ok, negativos si anulados; NC/Evento de retorno al revés; un doc activo- luego-invalidado dentro del período ⇒ 2 ítems con signos opuestos; DTE con sello solo una vez en CLE (2 veces si positivo+negativo mismo período); mismo emisor y receptor; tributos (96): FE excluye 20 y C3; FEXE solo C3 (o null con tipoItem 4); CLE solo sección 1 (20, C3, 59, 71, D1, C8, D5); NRE con doc relacionado: FE/CCFE ⇒ 20, 59, 71, D1, C8, D5, D4; FEXE ⇒ C3; FOVIAL/COFRANS (D1 y C8) en FEXE requieren solicitud/autorización; PSV informativo ≥ 0; ivaItem FE = (ventasGravadas/1.13)×13%; CRE montoSujetoRet: CCFE = TotalGravadas − descGlobal; FE = (TotalGravadas − descGlobal)/1.13; DCLE: fechaFin ≥ fechaInicio; subTotal = valorOperaciones − noSujetosPercibo; ivaComision = comisión × 13%; valorLiquido = valorOperaciones − comisión − ivaPercibido(2%) − ivaComision.

**Resumen (123–168)** — sumatorias con holgura **+ $0.01** en todos los campos calculados; descuentos globales ≤ su total; totalPagar: FSEE = subTotal − reteRenta; NCE/NDE = monto + totalIvaPercibido − totalIvaRetenido ± cargos; si abonos > monto ⇒ $0.00; condición operación CAT-016 (código 3 mixto; código 1 si total $0.00 o saldo a favor); forma pago CAT-017 (n formas, código 99 con saldo a favor; CDE null si tipoDonación 2 o 3); montoPago suma = totalPagar (CDE: = totalDonación); plazo CAT-018 requerido si condición = 2; NPE opcional (FE, CCFE, NDE, FEXE); INCOTERMS CAT-031 requerido si exportación = 1.

**Extensión (169–171)** / **Apéndice (172–174)** / **Sello (175)** — DCLE-only extensión; apéndice 1–10; selloRecibido incorporado al Archivo DTE salvo operaciones en contingencia.

### 3.2 Anexo V — Events (field → rule, compact)

- 1 Versión → **1** Retorno y OpEsp; **3** Invalidación y Contingencia.
- 2 Ambiente → CAT-001 (00/01).
- 3 Modelo → código 1 (OpEsp únicamente 1); Retorno código 2 en contingencia. 4 Transmisión → 1 normal con modelo previo; Retorno 2 en contingencia. 5/6 tipoContingencia/motivo (Retorno en contingencia).
- 7 codigoGeneracion → UUID v4, único, mayúsculas.
- **8 tipoEvento → código 18 Retorno; código 17 Operaciones especiales** (CAT-002).
- 9 fecEmiEvento → hasta 5 días posteriores (no cruzar período tributario; último día del mes ⇒ solo 30 min); cualquier fecha anterior; **invalidando DTE ≠ FE/FEXE/FSEE/Evento ⇒ misma fecha que fecEmi/fecEvento del DTE invalidado**; FE/FEXE/FSEE ⇒ máx 3 meses posteriores a la generación; transmisión ≤ 3 meses desde el sello del DTE; **2 años** si código de actividad del emisor ∈ {21001, 21008, 46482, 46484, 46491, 47721}; otros DTE ⇒ transmisión ≤ 10 días hábiles posteriores al período del sello.
- 10 fecEvento (Contingencia) → no fechas anteriores; transmisión ≤ 24 h tras fin del cese de fuerza mayor.
- 11/12 horas → HH:MM:SS, holgura 30 min fin de mes. 13 fusiones → null o NIT. 14 tipoMoneda → USD.
- 15–17 (Retorno docsrel) → solo 01/11/14; máx 50 mismo tipo; con Sello; un código por evento por documento (eventos múltiples permitidos por documento).
- 18–27 emisor → autorizado emisor DTE; NIT = del DTE; **OpEsp solo contribuyentes designados por la AT**; codEstablecimientoMH estructura M000/S000/B000/P000 [?].
- 28–31 (Retorno/FEXE) → recinto CAT-027 / tipoRégimen CAT-033 / régimen CAT-028 solo exportación 1; tipoItemExpor[?] códigos 1 o 2 (no 3 ni 4).
- 34–36 (Contingencia detalle) → correlativos > 0, **máx 1000**; tipos permitidos **01, 03, 04, 05, 06, 07, 11, 14 y 18**; sin Sello ni invalidados; pueden mezclarse tipos distintos en un mismo evento; un código por ítem.
- 37–42 (motivo contingencia) → fFin ≥ fInicio; hFin > hInicio; CAT-005; texto solo código 5.
- 43–48 (invalidación detalle) → doc con Sello; **CCFE/CRE no deben tener NCE/NDE de ajuste (invalidar primero la NC/ND)**; **FE/FEXE/FSEE no deben tener Evento de retorno aplicado (invalidar primero el evento)**; **plazos de invalidación: CCFE/CRE/NCE/NDE ⇒ 1 día tras el sello; CLE/DCLE ⇒ 10 días hábiles del mes siguiente al período; NRE/CDE/Evento de retorno/Evento de OpEsp ⇒ 4 días calendario; FE/FEXE/FSEE ⇒ 3 meses**; codigoGeneracionR solo tipoInvalidación 1 o 3, con Sello previo, null para tipos 05[? OCR "053"], 08, 16, 17 y 18, y null si tipoInvalidación = 2.
- 49–55 → copiar exacto del DTE (tipoDoc/numDoc/nombre del receptor; null si null en la FE); codPais/nombrePais solo FEXE.
- 56–58 → ventaTercero copiado del DTE; null si FSEE; domicilioFiscal igual al de la FE/FEXE (FE V1 / FEXE V1-V2 ⇒ cualquiera de CAT-032).
- 59–60 → compraTercero igual al de la FEXE; null si FE o FSEE.
- 61–88 (cuerpo Retorno/OpEsp) → 2000 ítems; codigoGeneracionRef debe ser OpEsp **activo**; docs 02/97 admiten referencia si fecha origen ≤ 3 meses del evento; anulaciones de lo reportado ⇒ valores positivos referenciando el código del EOE; un mismo código de generación en todos los ítems que lo usen; DocDel/DocAl requeridos para tipoDocumento 02 (máx 36 dígitos), null para 97 con documento origen; cantidad = 1 con documento origen o cargos/abonos o tipoItem 4; valores no pueden exceder los del DTE origen (noSuj/exentas/gravadas/compras/ivaRetenido (VG/1.13)×1%/reteRenta 10%); FEXE ⇒ ventaNoSuj y ventaExenta = $0.00; FSEE ⇒ gravadas = $0.00 y usar compras; seguro/flete solo FEXE.
- 89–109 (resumen) → sumatorias + holgura $0.01; montoTotalOperacion (Retorno) = suma + tributos + seguro + flete; totalPagar = monto − ivaRetenido − reteRenta ± cargos (≥ $0.00).
- 110–117 → CAT-024; descripción del error; responsable y solicitante con doc de identidad.
- 121 sello → todos los eventos; "exceptuando las operaciones generadas en Contingencia del Evento de Retorno".

### 3.3 Contingency-allowed DTE types — resolution of the NCE (05) contradiction

Every Anexo list that touches the question **INCLUDES NCE (05)**:
- Anexo II N°8/N°9 doc column (p.49): "FE, CCFE, NRE, NCE, NDE, CRE, FEXE y FSEE".
- Anexo IV N°6/7/8/9 rules 3 (pp.102–103): "En contingencia deberá ingresar el código 2 … FE, CCFE, NRE, NCE, NDE, CRE, FEXE y FSEE".
- Anexo III Sección 4 (p.86) and Anexo V N°35 (p.126): "01-FE, 03-CCFE, 04-NRE, **05-NCE**, 06-NDE, 07-CRE, 11-FEXE, 14-FSEE y 18-Evento de retorno".
Excluded from contingency everywhere: **CLE (15), DCLE (16), CDE (17)**. Additionally **Evento de retorno (18) itself may be generated en contingencia** (modelo 2 / transmisión 2 per Anexo V N°3/4). If the main body (secs 1–19) lists differ, the Anexos are unanimous as above.

---

## 4. Technical specs (ANEXO I, pp.36–47)

- **No HTTP endpoints, URLs, retry policy, or QR-code byte format are specified in Anexo I.** Auth details, reception (uno-a-uno / lote), and service-status endpoints are deferred: "Las Guías y Manuales emitidos por la Administración Tributaria contienen los detalles tecnológicos" (rules 3.2, 3.3, 3.5). QR appears only as an Entrega requirement: the download site must show "Código QR que enlace a la dirección del sitio y/o ruta de descarga del receptor" (p.43). No Retorno/OpEsp-specific endpoints appear.
- Código de Generación: UUID **v4**, 32 hex + 4 guiones = 36 chars, **mayúsculas**; filename = código + extensión (p.36).
- Número de Control (p.36–37): `DTE-00-00000000-000000000000000`; 4 secciones; sección 3 = 4 chars establecimiento + 4 chars punto de venta (codificación AT); sección 4 consecutivo 15 dígitos, "iniciará en 1 y finalizará en 9999999999999909" [OCR garbled — 15 dígitos ⇒ 999999999999999].
- Formato: JSON-schema provisto por la AT; estándar **ECMA-404**; columnas de estructura: N°, Campo JSON, Representación Gráfica (A/B/C/D), Nombre, Descripción, Condición (Requerido para su transmisión / Requerido por tipo de operación / Opcional), Tipo de dato, Longitud/precisión, Documento/Evento (pp.37–39, 47).
- **Firma** (Cuadro 10, p.40): firma electrónica simple con certificados de la AT; "JSON Web Signature (IWS)" [OCR: JWS], "Estándar de Firmado CAGES - PKCS8EncodedKeySpec" [? OCR — 2022 text read "PKCS8EncodedKeySpec"; CAGES likely garbled], algoritmo "RSAS12" [? OCR — likely RSASSA-PKCS / similar]. Llaves asimétricas privada/pública; `firmaElectronica` = JWS compact serialization over the full DTE/Evento JSON (garbled base64 example pp.40–41). AT validates the certificate on every document/event. No firmador changes beyond this are stated.
- **Sello de Recepción**: 40 caracteres alfanuméricos sin guiones, mayúsculas; atributo base `selloRecibido` (p.42).
- **Transmisión** (p.41): ambientes Pruebas (00, sin efectos tributarios) y Productivo (01); recepción uno a uno / en lote; regla 3.5 consulta de estado del servicio (NEW per changelog "Se incorpora la Consulta del Estado del Servicio de Recepción").
- **Archivo DTE** (Cuadro 11, pp.43–44): partes = llave de apertura `{`, estructura de datos, firma electrónica, sello de recepción, llave de cierre `}`; objetos base: `identificacion`, `emisor`, `receptor`, `otrosDocumentos`, `documentoRelacionado`, `ventaTercero`, `compraTercero`, `cuerpoDocumento`, `resumen`, `apendice`, `firmaElectronica`, `selloRecibido`. Estructura firmada debe incorporarse íntegra (alteración = lesiva al interés fiscal). Entrega: RG fiel; sitio de descarga (requisitos mínimos p.43) o correo electrónico (solo contenido de la entrega).
- **Módulos** (NEW per changelog: "Se incorpora el Módulo de Entrega"): 1 Generación, 2 Firmado, 3 Transmisión, 4 Entrega; arquitectura sugerida: alta disponibilidad, DRP, balanceadores, seguridad, auto-escalado, respaldo, trazabilidad, monitoreo, reportes (p.44).
- **Seguridad** (pp.44–45): JWS, ECMA-404, UUIDv4; copias de respaldo de los JSON + sello (Sistema de Transmisión) o medio electrónico (Sistema de Facturación); SADEs deben garantizar disponibilidad.
- Flujo (diagram p.46): Genera JSON → Firma → Transmisión (uno a uno / lote) → AT valida token/firma → sello o error; incluye "Retoma [Retorno] datos de consulta".
- Glosario (p.47): Representación Gráfica A/B/C/D; 11 siglas DTE (incluye FCE→FE typo).

---

## 5. OCR-quality warnings

1. **Rotated table headers**: every Anexo II/III/V table page begins with 2–3 lines of rotated-column gibberish (e.g. p.48 "el a 3 cl a E] 25…"). Column values sometimes interleave; JSON keys are broken across lines (e.g. `otrosDo cument os.codD ocAsoci ado`). Keys were reconstructed from fragments — treat any key not cross-confirmed in ≥2 places as [?].
2. **Garbled keys [?] (unresolvable from this OCR)**: DTE N°84 "Tributo sujeto a cálculo de IVA" (`…¿Tribal` / `codTr…`, pp.63/108/129); DTE N°103 CRE `montoSujeto…oGrav…` (p.69); event N°31 `emisor.tipoItemExpor…` (p.85); event resumen N°92 `totalCompraExc…` (p.96); DCLE N°116/117/121 key fragments. Also `identificacion.tipoOperacion` (N°7) vs. older `tipoTransmision` — Anexo I p.43 example shows `"tipoOperacion"` but Anexo III N°4 shows `tipo…cion` [?] — the DTE field 7 JSON key should be verified against the official JSON-schemas.
3. **Version lists**: Anexo II field 1 (p.48) vs Anexo IV field 1 (p.102) disagree on FEXE (2 vs 3). Anexo IV taken as authoritative. Anexo III field 1 (p.81) internally contradictory ("Máximo: 2 … deberá ingresar 3"); resolved by Anexo V N°1.
4. **Digits inside words**: "MO00, $000, 8000, PO00" → (M000, S000, B000, P000); "9999999999999909" → 15-digit cap; "053" in Anexo V N°48 → likely "05"; "IWS/RSAS12/CAGES" in Cuadro 10 → JWS/RSASSA[?]/[?]. "Di - Modo producción" → 01.
5. **Page 57 (N°58–60)**: table header repeated mid-page; condition column values for codDocAsociado (CDE=Requerido / otros=por tipo de operación) partially interleaved — confident but column order reconstructed.
6. **Anexo VI (pp.136–137)** itself is partially garbled (e.g. "11 Y Campo 21: Se modifica el máximo de ítems", "PATA", "2.0 iy IV IVA retenido") — changelog field numbering for Anexo III additions does not match Anexo III's own table numbering; quoted as-is.
7. **TOC (pp.4–6)** is heavily garbled but confirms the section skeleton only; no content lost that matters.
8. Missing entirely from OCR: none of the six Anexos is absent; however no page shows an explicit dollar value for the FE receptor threshold ("monto legalmente establecido" everywhere), and no QR payload spec / endpoint list exists anywhere in the Anexos (they are deferred to Manuales) — a requirement writer must NOT expect them here.
