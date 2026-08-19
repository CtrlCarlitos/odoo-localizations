# Evidence — 48_ SAT Lista general de formularios (master form catalog: code ↔ declaration type ↔ channel)

Source: 1 document: `48_SAT_Lista_Formularios.txt` = text dump of `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` — Wayback snapshot **2025-10-06** of portal.sat.gob.gt/portal/lista-general-de-formularios/. Read: 2026-08-19, end-to-end. Dump/extraction defects flagged `[sic]`, never corrected.

**Extraction-method notes (this file only):**
- Page body + tables were recovered from the snapshot's embedded JS payload (wpfd/vc markup); the raw HTML's visible DOM carries only page chrome. Tables (data-row counts): FormulariosVigentes **82**, FormulariosVigentesAnexo **24** ("FORMULARIOS QUE SE GENERAN EN APLICACIONES ELECTRÓNICAS"), FormulariosNoVigentes **54**, FormulariosNoVigentesAnexo **9** (same heading, no-vigente side).
- The dump prints form codes bare ("2237"); the "SAT-" prefix is SAT's convention, printed by SAT itself elsewhere (e.g. `56_` manual: "Formulario SAT-1111", EVID-377). "–" in a channel cell = form not available in that format (page's own legend, EVID-371).
- Main-table headers are flattened onto two dump lines: " | Descripción | Impreso | Electrónico – Asiste" / " | Papel | Web: | Light: | DG:". The Anexo tables instead use " | Aplicación Electrónica | Descripcción [sic] | Formulario" — no channel columns: the application IS the channel.
- Dump lines 194-241 are site-navigation chrome (trámite link labels: "Cita Controlada", "Inscripción RTU", "Planilla de IVA", "Agentes de Retención del IVA", "Cambio de Regímenes", "Aduanas", "Documento Compromisorio"…), not table data; used only as context (EVID-378, OQ-2).
- No page dateModified is present in the dump; the only as-of evidence is the Wayback snapshot date 2025-10-06.

**Identity verdict (checked first):** CONFIRMED — SAT's "Lista general de formularios (trámites y pago de impuestos)" page (title lines 4-5; source URL in the dump header), carrying the 4 announced tables. It is an **administrative catalog, not a legal instrument**: its LB value = SAT's own authoritative form↔obligation↔channel mapping; where a row prints its legal basis (Decreto 73-2008 at 1609; Decreto 37-92 at 7061; Decretos 21-04 y 9-02 at 3035; "art.44 y 44A Ley del ISR" at 1241/1249), that printed citation is the LB candidate for the row.

---

## EVID-371 — Identity + the page's own channel model: Papel / AsiseLight / AsiseWeb / Declaraguate
- **Loc:** dump lines 1-17 (page head + legend + channel definitions + FormulariosVigentes header rows)
- **Verbatim:** "Lista general de formularios" / "Lista general de formularios (trámites y pago de impuestos)" / "El guión que aparece en algunas casillas significa que el formulario no está disponible en ese formato." / "Formularios en Papel: Estos formularios los puede adquirir en cualquier Oficina o Agencia Tributaria en las diferentes regiones del país." / "AsiseLight: Puede descargar de Internet la edición para el formulario específico que desea llenar, y generar el archivo electrónico para utilizarse en BancaSAT." / "AsiseWeb: Es la versión en línea del Asiste, que encuentra en los sitios de Internet de los bancos que ofrecen el servicio BancaSAT." / "Declaraguate: Es un sistema por medio del cual pueden llenar vía Internet diferentes formularios electrónicos para la declaración y el pago de impuestos." / header: " | Descripción | Impreso | Electrónico – Asiste" + " | Papel | Web: | Light: | DG:"
- **Gloss:** Four channels, defined by the page itself: **Papel** (physical forms, any Oficina/Agencia Tributaria); **AsiseLight** (offline: download the form edition, generate an electronic file **for BancaSAT**); **AsiseWeb** (online Asiste **hosted at banks** offering BancaSAT); **Declaraguate** (SAT internet system to fill e-forms for declaration AND payment). Dash = unavailable in that format. Spellings "AsiseLight"/"AsiseWeb" as printed (SAT elsewhere styles the app "Asiste"; OQ-7). Per row-data (EVID-382), Declaraguate is the only channel carrying the tax declarations, and Light carries zero vigente forms.
- **Candidate CRs:** filing-surface CR: model GT form availability as a per-form channel matrix {papel, asiste-web, asiste-light, declaraguate} plus app-generated surfaces (Anexo), "–" = not available. LB: this catalog (definitions + row data).
- **Topics:** catalogs; fiscal-reporting (filing surfaces)
- **Doubts/xref:** OQ-6 (header grouping), OQ-7 (spellings), EVID-382

## EVID-372 — Vigentes ISR monthly family 1311/1321/1331/1341/1352 — plan correction: ISR retenciones = 1331, NOT 1321
- **Loc:** FormulariosVigentes, rows SAT-1311…SAT-1352, dump lines 32-36
- **Verbatim:** "ISR Opcional Mensual | – | – | – | 1311" / "ISR Capital Mensual | – | – | – | 1321" / "ISR Retenciones | – | – | – | 1331" / "ISR Sorteos | – | – | – | 1341" / "ISR No Residentes Retenciones | – | – | – | 1352"
- **Gloss:** Monthly ISR set, all **DG-only**: opcional mensual 1311; **capital mensual 1321**; **ISR retenciones (general) 1331**; sorteos 1341; no-resident retenciones 1352. **Plan-mapping correction:** the extraction plan's "SAT-1321 (retenciones)" is contradicted by the page — 1321 = ISR Capital Mensual; the ISR-withholding declaration is **SAT-1331**.
- **Candidate CRs:** catalog CRs: ISR retenciones declaration = SAT-1331 (DG only); ISR capital mensual = SAT-1321 (DG); ISR opcional mensual = SAT-1311; ISR sorteos = SAT-1341; ISR no-resident retenciones = SAT-1352. LB: this catalog + LAT (D10-2012) retenciones/rentas provisions (W-GT2 unit).
- **Topics:** fiscal-reporting; taxation (ISR); catalogs
- **Doubts/xref:** OQ-1

## EVID-373 — Vigentes ISR periodic/annual 1361/1371/1411/1431 + ISO 1608 — plan corrections: "1371 = ISR anual" and "1411 = asalariados" both wrong
- **Loc:** FormulariosVigentes, rows SAT-1361, SAT-1371, SAT-1411, SAT-1431, SAT-1608, dump lines 37-41
- **Verbatim:** "ISR Trimestral. Impuesto Sobre la Renta. Régimen Sobre Utilidades de Actividades Lucrativas. Declaración Jurada y Pago Trimestral. | – | – | – | 1361" / "ISR No Residentes. Pago Directo. Impuesto Sobre la Renta. Pagos en Forma Directa por No Residentes sin Establecimiento Permanente que no fueron objeto de retención. Declaración Jurada y Pago Mensual. | – | – | – | 1371" / "ISR Anual. Impuesto Sobre la Renta. Para los Regímenes Sobre las Utilidades de Actividades Lucrativas, Opcional Simplificado, Sobre Ingresos de Actividades Lucrativas y Contribuyentes Exentos. | – | – | – | 1411" / "ISR Relación de Dependencia. Impuesto Sobre la Renta. Rentas del Trabajo en Relación de Dependencia, Declaración Jurada y Pago Anual. | – | – | – | 1431" / "Impuesto de Solidaridad. Recibo de pago Trimestral. | – | – | – | 1608"
- **Gloss:** **Plan-mapping corrections:** SAT-1371 is NOT "ISR anual" — it is the monthly **No Residentes Pago Directo** (direct payment by non-residents without permanent establishment on income not subject to retención); SAT-1411 is NOT "asalariados" — it is the **annual ISR for the lucrativas family** (Utilidades + Opcional Simplificado + Sobre Ingresos + Exentos); the rentas-del-trabajo annual declaration is **SAT-1431 (Relación de Dependencia)**. Trimestral lucrativas = 1361; ISO quarterly receipt = 1608. All DG-only.
- **Candidate CRs:** catalog CRs: annual ISR (lucrativas family) = SAT-1411; annual ISR rentas del trabajo (relación de dependencia) = SAT-1431; quarterly ISR utilidades = SAT-1361; no-resident direct payment = SAT-1371 (monthly); ISO = SAT-1608 (quarterly). LB: this catalog + LAT (D10-2012) regime structure (W-GT2 unit).
- **Topics:** fiscal-reporting; taxation (ISR); payroll (1431); catalogs
- **Doubts/xref:** OQ-1

## EVID-374 — IVA declarations: 2237 general (valid from Sep-2013), 2046 pequeño contribuyente (valid from Sep-2013), 2241 electronic peq. regime
- **Loc:** FormulariosVigentes, rows SAT-2046, SAT-2237, SAT-2241, dump lines 44, 53, 54
- **Verbatim:** "Impuesto al Valor Agregado. Régimen de Pequeño Contribuyente. Declaración Jurada Simplificada y Pago Mensual. Válido para períodos de Imposición Septiembre 2013 en adelante | – | – | – | 2046" / "Declaración Jurada y Pago Mensual del Impuesto al Valor Agregado para contribuyentes que realicen operaciones locales y de exportación. Válido para períodos de Imposición Septiembre 2013 en adelante. | – | – | – | 2237" / "IVA-Régimen Electrónico de Pequeño Contribuyente | – | – | – | 2241"
- **Gloss:** **IVA monthly general declaration = SAT-2237** (single form for taxpayers doing local AND export operations — the page's own wording), DG-only, **valid for períodos de imposición Septiembre 2013 en adelante** (dated row, valid_from 2013-09). **Pequeño contribuyente simplified monthly = SAT-2046**, DG-only, same 2013-09 valid_from. **Régimen Electrónico de Pequeño Contribuyente = SAT-2241**, DG-only, no printed validity. The plan's priority mapping for 2046/2241 is confirmed.
- **Candidate CRs:** catalog CRs: IVA monthly filing = SAT-2237 (locals + exporters in one form), DG only, periods ≥ 2013-09; peq. contribuyente monthly = SAT-2046 (DG, ≥ 2013-09); electronic peq. regime = SAT-2241 (DG). Dated CR: form-version selection by período de imposición. LB: this catalog + LIVA (D27-92)/LAT (units W-GT2 ff.).
- **Topics:** fiscal-reporting; taxation (IVA); special regimes (pequeño contribuyente); catalogs
- **Doubts/xref:** OQ-4 (predecessor overlap), EVID-381

## EVID-375 — IVA retenciones family: 2340 / 2320 / 2229 via RETENCIONES WEB; 2085 / 2086 facturas especiales (dated); 2302 remanentes (paper vigente / web superseded)
- **Loc:** FormulariosVigentesAnexo rows (RETENCIONES WEB), dump lines 102-104; FormulariosVigentes rows SAT-2085, SAT-2086, SAT-2302, dump lines 48, 49, 57; FormulariosNoVigentes row SAT-2302, dump line 172
- **Verbatim:** "RETENCIONES WEB | Constancia de Retención del IVA | 2229" / "RETENCIONES WEB | Declaración Jurada de IVA Retenciones Agropecuario | 2320" / "RETENCIONES WEB | Declaración Jurada de Retenciones del IVA | 2340" / "Impuesto al Valor Agregado. Retenciones efectuadas al emitir Facturas Especiales. Recibo de pago. Válido para períodos de Imposición Septiembre 2013 en adelante. | – | – | – | 2085" / "Recibo de Pago, Compra-venta de Bienes Inmuebles, Retención a Facturas Especiales. Válido para períodos de imposición desde enero – 1999 hasta septiembre – 2013. | – | – | – | 2086" / "Solicitud de acreditamiento en cuenta de remanentes por retenciones de IVA | 2302 | – | – | –" (Vigentes, papel) / "Solicitud de acreditamientos en cuenta de remanentes por retenciones del IVA | – | 2302 | – | –" (No Vigentes, web)
- **Gloss:** The IVA-withholding declarations are **not Declaraguate forms**: they are generated in the **RETENCIONES WEB application** — general 2340, agropecuario 2320, plus the retention certificate 2229. Facturas-especiales retention receipts: 2085 (valid ≥ 2013-09) and 2086 (bounded window 1999-01 → 2013-09, yet listed among **Vigentes** — usable for old-period filings, OQ-4). Remanentes accreditation 2302: **paper version vigente, web version no vigente** (same code, channel-dependent validity).
- **Candidate CRs:** filing-surface CRs: IVA retention declaration = SAT-2340 via Retenciones Web app (agro variant 2320; constancia 2229); facturas especiales retention receipt = 2085 (≥2013-09), 2086 for 1999-01–2013-09 periods; remanentes acreditamiento = 2302 (paper channel only). LB: this catalog + LIVA (D27-92) retención regime (units cross-ref).
- **Topics:** fiscal-reporting; taxation (IVA retenciones); special regimes (agropecuario); catalogs
- **Doubts/xref:** OQ-3 (2302 dual row), OQ-4 (2086 in Vigentes), EVID-379

## EVID-376 — RETENISR family (patrono-side ISR wage instruments): 1901, 1481, 1911, 1921, 1219 (+ superseded 1078/1088)
- **Loc:** FormulariosVigentesAnexo rows (RETENISR), dump lines 105-109; FormulariosNoVigentesAnexo rows (RETENISR), dump lines 186-188
- **Verbatim:** "RETENISR | Impuesto Sobre la Renta del Trabajo. Informe Anual de Liquidación y Devolución de lo Retenido en Exceso | 1481" / "RETENISR | Declaración Jurada ante el Patrono del ISR. | 1901" / "RETENISR | Constancia de Retención del ISR. Régimen Opcional Sobre Ingresos de Actividades Lucrativas y Rentas de Capital | 1911" / "RETENISR | Constancia de Retención del ISR del Trabajo. | 1921" / "RETENISR | Anexo a Retenciones ISR – IPF | 1219" / (no vigentes:) "RETENISR | Declaración Jurada Anual de Conciliación de Retenciones Efectuadas a Empleados en Relación de Dependencia | 1078" / "RETENISR | Conciliación Anual de Retenciones Practicadas a Empleados en Relación de Dependencia | 1088"
- **Gloss:** The wage-ISR (payroll) instruments live in the **RETENISR application**: annual declaration before the employer (**1901**), annual liquidation/devolución informe (**1481**), retention certificates — trabajo **1921**, opcional/rentas de capital **1911** — and the ISR-IPF annex **1219**. Superseded: annual reconciliation forms 1078/1088. These are the employer-side outputs of the LAT rentas-del-trabajo withholding (xref `56_` unit EVID-368: asalariado regime, Agencia Virtual).
- **Candidate CRs:** payroll CRs: employer-side annual ISR declaration for dependents = SAT-1901 (RETENISR app); annual informe de liquidación/devolución = SAT-1481; retention constancias = SAT-1921 (trabajo) and SAT-1911 (opcional + rentas de capital). LB: this catalog + LAT (D10-2012) rentas-del-trabajo retención provisions (W-GT2; `56_` unit).
- **Topics:** payroll; fiscal-reporting; taxation (ISR); catalogs
- **Doubts/xref:** OQ-3 (1219 also in NoVigentesAnexo)

## EVID-377 — SAT-1111 dual: current PLANILLA IVA-FEL (app) vs superseded paper ISR-law Planilla IVA
- **Loc:** FormulariosVigentesAnexo row (PLANILLA IVA-FEL), dump line 118; FormulariosNoVigentes row SAT-1111 (papel), dump line 149
- **Verbatim:** "PLANILLA IVA-FEL | Planilla para el Crédito por Impuesto al Valor Agregado | 1111" / "Impuesto Sobre la Renta Planilla para el Crédito por Impuesto al Valor Agregado IVA | 1111 | – | – | –"
- **Gloss:** Code **1111** carries two different instruments in two tables: the **no-vigente PAPER** planilla ("Impuesto Sobre la Renta Planilla para el Crédito por IVA" — the old ISR-law annual employee IVA planilla) and the **vigente, application-generated** PLANILLA IVA-FEL form. The `56_` manual (EVID-368/370) identifies the current one: output of the January filing window, "Formulario SAT-1111" + Constancia, statutory anchor art. 72 D10-2012. The catalog confirms the FEL planilla is a distinct, current surface and the paper planilla is retired.
- **Candidate CRs:** catalog CR: annual employee IVA-credit planilla = SAT-1111 generated in the PLANILLA IVA-FEL app (paper 1111 superseded). LB: this catalog + LAT art. 72 (D10-2012, per `56_` unit EVID-368).
- **Topics:** payroll (asalariados); taxation (IVA); annual filing; catalogs
- **Doubts/xref:** OQ-3 (same-code reuse pattern)

## EVID-378 — Exportadores devolución de crédito fiscal: 2053 / 2062 (ante el Banco de Guatemala) / 2073, paper-only; general devolución 2124; SAT-2390 ABSENT
- **Loc:** FormulariosVigentes rows SAT-2053, SAT-2062, SAT-2073, SAT-2124, dump lines 45-47, 50; FormulariosNoVigentes rows SAT-2052, SAT-2123, dump lines 165, 167
- **Verbatim:** "Solicitud de Registro al Régimen Especial de Devolución de Crédito Fiscal a Exportadores | 2053 | – | – | –" / "Declaración Jurada y Solicitud de Devolución Régimen Especial de Crédito Fiscal a Exportadores, ante el Banco de Guatemala | 2062 | – | – | –" / "Actualización Registro Especial de Devolución a Exportadores | 2073 | – | – | –" / "Solicitud de Devolución de Crédito Fiscal del IVA, o Restitución de Pagos Indebidos o en Exceso de Otros Impuestos, Impuestos Pagados por Importación de Combustibles o Depósitos por Garantías Aduanales | 2124 | – | – | –" / (no vigentes:) "Solicitud de Registro al Régimen Especial de Devolución de Crédito Fiscal a Exportadores. | – | 2052 | – | –" / "Solicitud de Devolución de Crédito Fiscal del IVA o de Pagos Indebidos o en Exceso de Otros Impuestos. | – | 2123 | – | –"
- **Gloss:** The exportadores special regime (maquila/export kin) is serviced by a **paper-only trio**: registration 2053, devolución application 2062 **filed before the Banco de Guatemala**, registro update 2073; superseded web versions 2052/2123. General devolución/restitución = **2124 (paper)**: IVA crédito fiscal, pagos indebidos/en exceso, fuel-import taxes, customs guarantee deposits. **No form 2390 appears anywhere in this dump** — the plan's "SAT-2390 kin" is NOT confirmed by this page (OQ-2); nav chrome ("Formularios Electrónicos Solicitud Dev. C.F. Régimen Especial Electrónico y Régimen General") hints current electronic devolución forms live outside these 4 tables.
- **Candidate CRs:** filing-surface CRs: export-devolution workflow = SAT-2053 (registro) → SAT-2062 (DJ + solicitud, Banco de Guatemala) → SAT-2073 (actualización), paper channel; general devolución = SAT-2124 (paper), scope incl. combustibles-import taxes + customs guarantee deposits. LB: this catalog + LIVA/LAT devolución regime (units cross-ref).
- **Topics:** special regimes (exportadores); taxation (IVA crédito fiscal); fiscal-reporting; catalogs
- **Doubts/xref:** OQ-2 (2390 absent; electronic dev.CF forms not itemized)

## EVID-379 — Special IVA regimes: agropecuario 2280 / 2290 (+2320 xref) and EXENIVA 2093 / 2118 / 351
- **Loc:** FormulariosVigentes rows SAT-2280, SAT-2290, dump lines 55-56; SAT-351 dump line 25; FormulariosVigentesAnexo rows (EXENIVA), dump lines 110-111
- **Verbatim:** "Régimen Especial de Contribuyente Agropecuario | – | – | – | 2280" / "IVA Electrónico Especial de Contribuyente Agropecuario | – | – | – | 2290" / "Solicitud de habilitación en el sistema de ExenIVA (gratuito) | 351 | – | – | –" / "EXENIVA | Constancia de Exención IVA | 2093" / "EXENIVA | Informe Trimestral de uso de Constancias de Exención | 2118"
- **Gloss:** Agropecuario special regime has two DG-only declaration forms: **2280** (Régimen Especial de Contribuyente Agropecuario) and **2290** (IVA Electrónico Especial de Contribuyente Agropecuario), plus the agro IVA-retention declaration 2320 via Retenciones Web (EVID-375). IVA-exemption certificates run through the **EXENIVA system**: habilitación 351 (paper, gratuito), constancia 2093, quarterly usage informe 2118 (app-generated).
- **Candidate CRs:** catalog CRs: agro regime filing surfaces = SAT-2280/SAT-2290 (DG) + SAT-2320 (Retenciones Web); exención-certificate workflow = 351 (habilitación, paper) + 2093 (constancia) + 2118 (quarterly informe, EXENIVA app). LB: this catalog + LAT/LIVA special-regime provisions (units cross-ref).
- **Topics:** special regimes (agropecuario); taxation (IVA exemptions); fiscal-reporting; catalogs
- **Doubts/xref:** EVID-375

## EVID-380 — No-Vigentes dated ledger A (ISR-law cluster): printed valid_from→valid_to windows of the superseded ISR forms
- **Loc:** FormulariosNoVigentes, rows SAT-1024/1025/1037/1055/1096/1121/1128/1169/1179/1189/1193/1197/1241/1249/1351, dump lines 144-159
- **Verbatim (anchors):** "Declaración Jurada y Recibo de Pago Trimestral del ISR. Válido para períodos de imposición desde Enero 2004 hasta Abril 2012 | – | – | – | 1025" / "Declaración Jurada y Recibo de Pago Mensual de Retenciones del ISR e Impuesto Sobre Productos Financieros. Válido para períodos de imposición desde Enero 1999 hasta Diciembre 2012 | – | – | – | 1055" / "Declaración Jurada Anual y Recibo de Pago ISR Asalariados. Válido para períodos de Imposición desde 2004 hasta el 2012 | – | – | – | 1179" / "Declaración Jurada Anual y Recibo de Pago ISR Régimen General. Válido para períodos de Imposición desde 2004 hasta el 2012 | – | – | – | 1189" / "ISR Retenciones No Residentes Pago Retenciones. Válido para períodos de Imposición desde Enero 2013 hasta Abril 2013 | – | – | – | 1351" / "Declaración Jurada y Recibo de Pago Mensual, Art. 44 y 44 “A” de la Ley del ISR (con reformas). Válido para períodos de Imposición desde Enero 2004 hasta Diciembre 2012 | – | – | – | 1249"
- **Gloss:** Dated-validity ledger (D16) for the old-law ISR family: annual **asalariados 1179** and **régimen general 1189** valid 2004→2012; monthly retenciones+IPF **1055** 1999-01→2012-12; no-resident retención **1096** 2001-01→2012-12; revaluación **1128** 1999-01→2012-12; art. 44/44-A monthly **1249** 2004-01→2012-12 (LB printed: "Art. 44 y 44 “A” de la Ley del ISR"); quarterly **1025** 2004-01→2012-04; transitional no-resident retención **1351** 2013-01→2013-04 only. Undated superseded: 1024, 1193, 1197, 1241, 1121 (revaluación), plus one-off regimes **IETAAP 1169** and **IEMA 1037**. The Dic-2012 cliff = the LAT (D10-2012) replacing the old ISR law from 2013.
- **Candidate CRs:** dated CR: form-version selection by período de imposición — filings for old ISR periods must use the superseded codes (1179/1189/1055/1096/1128/1249/1025; 1351 only for 2013-01–2013-04); the form registry must carry these as valid_to-dated rows. LB: this catalog (printed windows) + LAT vigencia (W-GT2 unit).
- **Topics:** catalogs; fiscal-reporting; taxation (ISR)
- **Doubts/xref:** OQ-4, ledger table below

## EVID-381 — No-Vigentes dated ledger B (IVA/ISO cluster): predecessors of 2237 / 2046 / 1608 and the printed Sep-vs-Oct-2013 overlap
- **Loc:** FormulariosNoVigentes, rows SAT-1609/2028/2043/2047/2049/2157/2232/2238/2291, dump lines 160-164, 168-171
- **Verbatim (anchors):** "Formulario de Pago del Impuesto de Solidaridad (Decreto 73-2008 del Congreso de la República). Válido para períodos de imposición desde enero – 2009 hasta septiembre – 2013. | – | – | – | 1609" / "Declaración Jurada Simplificada y Pago Mensual del IVA para Pequeños Contribuyentes. Válido para períodos de imposición desde febrero -2012 hasta septiembre – 2013 | – | – | – | 2047" / "Declaración Jurada Simplificada y Pago Trimestral del IVA para Pequeños Contribuyentes. Válido para períodos de imposición desde 3-2001 hasta 1-2012. | – | – | – | 2049" / "Declaración y Recibo de Pago Mensual del IVA y Anexo. Válido para períodos de Imposición desde Enero 2001 hasta Octubre 2013. | – | – | – | 2157" / "Declaración y Recibo de pago mensual del Impuesto al Valor Agregado (Para contribuyentes que realicen exclusivamente operaciones locales). Válido para períodos de Imposición desde Enero 2001 hasta Octubre 2013. | – | – | – | 2238" / "Factura y Declaración Única Centroamericana | – | 2291 | – | –"
- **Gloss:** Predecessor chains: **2237 ← 2157/2238/2232** (IVA monthly: general+anexo and locals-only both valid 2001-01→**2013-10**; 2232 undated); **2046 ← 2047** (peq. contribuyente monthly, 2012-02 [sic]→2013-09) **← 2049** (quarterly, 2001-03→2012-01 [sic]) **← 2043** (undated); **1608 ← 1609** (ISO, LB printed **Decreto 73-2008**, 2009-01→2013-09). **Printed overlap, flagged not corrected:** successors 2237/2046/2085 say "Septiembre 2013 en adelante" while predecessors 2157/2238 say "hasta Octubre 2013" — one overlapping month as printed (OQ-4). Also superseded: 2028 (Declaración Anual del IVA, Régimen Simplificado) and FYDUCA 2291 (web; see EVID-384).
- **Candidate CRs:** dated CR: IVA/peq-contribuyente/ISO form-version chains with printed windows (data above + ledger table); old-period IVA filings 2001-01–2013-10 use 2157 (general+anexo) or 2238 (locals-only), peq. 2012-02–2013-09 = 2047, quarterly peq. 2001-03–2012-01 = 2049. LB: this catalog + Decreto 73-2008 (printed at 1609) + LIVA/LAT (units cross-ref).
- **Topics:** catalogs; fiscal-reporting; taxation (IVA, ISO)
- **Doubts/xref:** OQ-4 (overlap + [sic] date formats), EVID-374

## EVID-382 — Channel row-data findings: declarations DG-only; 27 paper-only admin forms; AsiseLight legacy (0 vigente rows); Web remnants; dual-channel 2000/8008; Anexo apps = 5th surface
- **Loc:** FormulariosVigentes (whole table, dump lines 18-99) + FormulariosVigentesAnexo (dump lines 100-125), read as data
- **Verbatim (anchors):** "Recibo de Cobranza y Control de Multas | – | – | – | 811" / "Aviso Anulación de Documentos | – | 511 | – | –" / "Boleta para presentar y pagar formulario previamente llenado a través de Declaraguate | – | 2000 | – | 2000" / "Formulario para Pago Ramo Aduanas | – | 8008 | – | 8008" / "Recibo de pago de Ingresos Privativos por Gestiones de Vehículos Terrestres | – | 8209 | – | –" / "AGENCIA VIRTUAL | Anexo y Formulario del Impuesto a la Distribución de Bebidas Alcohólicas y No Alcohólicas de Declaraguate en la Agencia Virtual | 3109"
- **Gloss:** Channel matrix (vigentes, main table): (i) **every tax declaration/payment form is DG-only** (the 1311…9911 set); (ii) **27 forms are paper-only**: 26, 27, 45, 62, 72, 73, 251, 351, 362, 411, 2033, 2053, 2062, 2073, 2124, 2175, 2192, 4053, 5011, 5021, 5031, 5041, 5064, 7001, 7012, 7016, 9001; (iii) **the Light column is empty for every vigente row** — Light values exist only among no-vigentes (81, 149, 229, 1151, 3035, 5056, 5079, 7069, 7109 + ASISTELIGHT/ASISTELIGHT-ASISTEWEB app rows 6017/6021/6049, 3081/3091) → AsiseLight is a legacy channel; (iv) Web-only survivors: 511, 8209; dual Web+DG: **2000** (boleta) and **8008**; (v) the 24 Anexo forms are generated inside named applications (RETENCIONES WEB, RETENISR, EXENIVA, E-CAI, PLANILLA IVA-FEL, AGENCIA VIRTUAL, …) — a **fifth filing surface** beyond the 4 channel columns.
- **Candidate CRs:** filing-surface CRs: GT filing surfaces = Declaraguate (the universal e-channel) + app-specific surfaces (Retenciones Web, RETENISR, EXENIVA, PLANILLA IVA-FEL, Agencia Virtual) + paper (the 27 listed admin forms, incl. all devolución/exportador solicitudes); guard CR: do not model AsiseLight/AsiseWeb as current channels (0 vigente Light forms; Web only 511/2000/8008/8209). LB: this catalog (channel columns read as data).
- **Topics:** catalogs; fiscal-reporting (filing surfaces)
- **Doubts/xref:** OQ-5, EVID-371

## EVID-383 — Libros/protocolos + timbres + misc. ISR-adjacent: 7121, 7130 (dated 25-ago-2015), 7190, 8490; superseded timbres-dividendos 7061/7101 (D37-92 printed)
- **Loc:** FormulariosVigentes rows SAT-7121, SAT-7130, SAT-7190, SAT-8490, dump lines 77-79, 88; FormulariosNoVigentes rows SAT-7061, SAT-7101, dump lines 178-179
- **Verbatim:** "Habilitación de Libros. Impuesto de Timbres Fiscales y de Papel Sellado Especial para Protocolos. Habilitación y autorización de libros. | – | – | – | 7121" / "Impuesto de Timbres Fiscales y Papel Sellado Especial para Protocolos. Recibo de Pago. Vigente a partir del 25 de agosto 2015. | – | – | – | 7130" / "Impuesto Sobre Títulos Universitarios y de Carreras Técnicas | – | – | – | 7190" / "Herencia, Legados y Donaciones | – | – | – | 8490" / (no vigentes:) "Constancia de Retención por pago de dividendos o utilidades según Decreto 37-92 del Congreso de la República y sus reformas. Ley del Impuesto de Timbres y de Papel Sellado Especial para Protocolo | 7061 | – | 7069 | –" / "Retenciones sobre Dividendos o Utilidades – Declaración Jurada de Retenciones del Impuesto de Timbres Fiscales y de Papel Especial para Protocolo | 7101 | 7109 | 7109 | –"
- **Gloss:** Books/registros: **habilitación y autorización de libros = 7121** (DG), scoped on the page to Protocolos timbres; protocolos payment receipt **7130** is a dated row — "Vigente a partir del 25 de agosto 2015" (valid_from 2015-08-25). Títulos universitarios 7190; herencias/legados/donaciones 8490 (ISR-adjacent). Superseded timbres-dividendos withholding pair 7061 (constancia) / 7101-7109 (DJ retenciones), LB printed **Decreto 37-92** (the pre-LAT timbres regime; cf. current dividendos withholding under LAT, units cross-ref).
- **Candidate CRs:** catalog CRs: books/protocolos habilitación = SAT-7121 (DG); protocolos timbre receipt = SAT-7130 (valid ≥ 2015-08-25); timbres-dividendos forms 7061/7101 valid only pre-LAT (dated supersession). LB: this catalog + Decreto 37-92 (printed at 7061).
- **Topics:** catalogs; fiscal-reporting; taxation (timbres/protocolos; herencias)
- **Doubts/xref:** OQ-2 (LAT dividendos successors not on this page)

## EVID-384 — Customs & specific-tax families: existence capture (not exhaustive itemization)
- **Loc:** FormulariosVigentes rows SAT-8008/8028/8530/8540/8560, dump lines 81-91; petróleo 6051/6080/6090 lines 71-73; IUSI 9001/9050 lines 95, 97; cemento 9208 line 98; señales 9031 line 96; tabaco lines 66-70, 80; bebidas lines 18, 119-123; vehículos lines 60-65, 92-94, 117, 124; FormulariosNoVigentes row SAT-2291 line 171, 8005/8021 lines 180-181
- **Verbatim (anchors):** "Formulario para Pago Declaración Aduanera | – | – | – | 8560" / "Aduana ATC | – | – | – | 8540" / "Aduanas Específicos y Otros | – | – | – | 8530" / "Formulario para Pago Ramo Aduanas | – | 8008 | – | 8008" / "Declaración jurada y pago semanal del Impuesto a la Distribución de Petróleo Crudo y Combustibles Derivados del Petróleo | – | – | – | 6051" / "Impuesto Único Sobre Inmuebles. Impuesto sobre el valor de los bienes inmuebles situados en el territorio de la República. Recibo de pago trimestral. | – | – | – | 9050" / "Recibo de Impuesto Único Sobre Inmuebles. | 9001 | – | – | –" / "Declaración Jurada y Recibo de Pago del Impuesto a la Distribución del Cemento. | – | – | – | 9208" / "Impuesto a la Distribución de Señales por Cable. Declaración Jurada y Pago Mensual. | – | – | – | 9031"
- **Gloss:** Existence-as-category per plan: **customs family** (8560 pago declaración aduanera, 8008 ramo aduanas Web+DG, 8530, 8540 ATC, 8028 ingresos privativos; superseded 8005/8021/2291 FYDUCA; DUCA/SAT-2901 not itemized here — the `56_` manual, EVID-369, names FYDUCA = SAT-2901); **specific taxes**: petróleo (6051 weekly, 6080 monthly informative, 6090 annual exempt-products cuenta corriente), IUSI (9050 quarterly DG; 9001 paper receipt), cemento 9208, señales por cable 9031, tabaco family (5011/5021/5031/5041/5064/7200; superseded 5056/5071-5079), bebidas alcohólicas family (26, 611, 621, 3109-3120; superseded 3035/3061/3081/3091), vehicles taxes (IPRIMA 4041/4081; circulación 4091/4121/4131/4170; plates/records 8611/8620/8933/4053/4015; superseded 4001). All DG-only except noted.
- **Candidate CRs:** category CRs: registry must include the customs-form family (8560/8008/8530/8540/8028) and the specific-tax declaration set (petróleo/IUSI/cemento/señales/tabaco/bebidas/vehículos) with codes+channels as above, without deep field modeling at this stage. LB: this catalog.
- **Topics:** catalogs; customs (existence only); fiscal-reporting
- **Doubts/xref:** OQ-2 (DUCA forms outside this page), `56_` unit EVID-369

## EVID-385 — Compliance/admin surface + as-of: boleta 2000; 811/821/891/860; 8421 solvencia; cese 2175/2192 (paper-only); FAD 02; snapshot 2025-10-06
- **Loc:** FormulariosVigentes rows SAT-811/821/891/8421, dump lines 29-31, 86; SAT-2175/2192 dump lines 51-52; FormulariosVigentesAnexo row 860, dump line 125; FormulariosNoVigentes row "FAD 02", dump line 182; dump header line 1
- **Verbatim:** "Formulario Solicitud de Convenio de pago | – | – | – | 821" / "Facilidades de Pago | – | – | – | 891" / "Certificación de Cumplimiento. Solicitud de Certificación de estar al día en el cumplimiento de obligaciones tributarias | – | – | – | 8421" / "Cese de actividades definitivo | 2175 | – | – | –" / "Cese temporal o habilitación de actividades económicas | 2192 | – | – | –" / "RECIBO COBRANZA FISCALIZACIÓN | Recibo de ingresos por pago de sanciones y ajustes de fiscalización | 860" / (no vigente:) "Formulario de actualización por Depuración del Registro Tributario Unificado. | FAD 02 | – | – | –" / header: "=== SOURCE: gt/sources/48_SAT_Lista_Formularios_2025-10-06.html (Wayback snapshot 2025-10-06 of portal.sat.gob.gt/portal/lista-general-de-formularios/) ==="
- **Gloss:** Compliance-adjacent surface: payment-slip **boleta 2000** (Web+DG, EVID-382) for Declaraguate-pre-filled forms; multas receipt 811; convenio de pago 821 + facilidades de pago 891 (installment hardship); fiscalización sanciones/ajustes receipt 860 (app-generated); solvencia/certificación de cumplimiento 8421; **cease-of-activity notices 2175 (definitivo) and 2192 (temporal) are paper-only** — the registry-exit workflow has no electronic channel on this page; deprecated RTU-depuration form "FAD 02" (a non-SAT-prefixed code, superseded). **As-of evidence:** content = Wayback snapshot 2025-10-06 only; no dateModified in the dump (OQ-5).
- **Candidate CRs:** catalog CRs: compliance/admin registry rows (811/821/891/860/8421; cese 2175/2192 paper-only; boleta 2000 dual-channel). LB: this catalog.
- **Topics:** catalogs; fiscal-reporting; compliance
- **Doubts/xref:** OQ-5

---

## Vigentes form-family map (DATA, from FormulariosVigentes + Anexo)

| Form | Declaration / obligation (page's own scope) | Channel | Validity (as printed) |
|---|---|---|---|
| 1311 | ISR Opcional Mensual | DG | — |
| 1321 | ISR Capital Mensual | DG | — |
| 1331 | ISR Retenciones (general) | DG | — |
| 1341 | ISR Sorteos | DG | — |
| 1352 | ISR No Residentes Retenciones | DG | — |
| 1361 | ISR Trimestral (Utilidades de Actividades Lucrativas) | DG | — |
| 1371 | ISR No Residentes Pago Directo (mensual) | DG | — |
| 1411 | ISR Anual (Utilidades / Opcional Simplificado / Ingresos / Exentos) | DG | — |
| 1431 | ISR Relación de Dependencia (anual, rentas del trabajo) | DG | — |
| 1608 | Impuesto de Solidaridad, trimestral | DG | — |
| 8490 | Herencia, Legados y Donaciones | DG | — |
| 1901 | DJ anual ante el Patrono del ISR | RETENISR | — |
| 1481 | ISR Trabajo: informe anual de liquidación y devolución | RETENISR | — |
| 1911 / 1921 | Constancias retención ISR (opcional+capital / trabajo) | RETENISR | — |
| 1219 | Anexo a Retenciones ISR – IPF | RETENISR | (also in NoVigentesAnexo, OQ-3) |
| 1111 | Planilla IVA-FEL (crédito IVA asalariados) | PLANILLA IVA-FEL app | — (paper 1111 = no vigente) |
| 2237 | IVA mensual, locales y exportación | DG | ≥ Sep-2013 |
| 2046 | IVA peq. contribuyente, DJ simplificada mensual | DG | ≥ Sep-2013 |
| 2241 | IVA-Régimen Electrónico de Pequeño Contribuyente | DG | — |
| 2280 / 2290 | Régimen Especial Agropecuario / IVA Electrónico Agropecuario | DG | — |
| 2340 | DJ Retenciones del IVA | RETENCIONES WEB | — |
| 2320 | DJ IVA Retenciones Agropecuario | RETENCIONES WEB | — |
| 2229 | Constancia de Retención del IVA | RETENCIONES WEB | — |
| 2085 | IVA retenciones Facturas Especiales, recibo | DG | ≥ Sep-2013 |
| 2086 | Inmuebles/Facturas Especiales, recibo | DG | 1999-01 → 2013-09 (in Vigentes) |
| 2311 | Vehículos traspasos: declaración y pago IVA | DG | — |
| 2799 | IVA contratos en Escritura Pública, pago directo | DG | — |
| 2302 | Acreditamiento remanentes por retenciones IVA | Papel | (web 2302 = no vigente) |
| 2093 / 2118 | EXENIVA: constancia exención / informe trimestral | EXENIVA app | — |
| 351 | Habilitación sistema ExenIVA (gratuito) | Papel | — |
| 2053 / 2062 / 2073 | Exportadores devolución CF: registro / DJ+solicitud (Banco de Guatemala) / actualización | Papel | — |
| 2124 | Devolución CF IVA / restitución pagos indebidos-exceso, combustibles, garantías aduanales | Papel | — |
| 2000 | Boleta para pagar formulario previamente llenado vía Declaraguate | Web + DG | — |
| 7121 | Habilitación de libros (timbres/protocolos) | DG | — |
| 7130 | Timbres protocolos, recibo de pago | DG | ≥ 25-ago-2015 |
| 811 / 821 / 891 | Multas / convenio de pago / facilidades de pago | DG | — |
| 860 | Sanciones y ajustes de fiscalización | RECIBO COBRANZA FISCALIZACIÓN app | — |
| 8421 | Certificación de cumplimiento (solvencia) | DG | — |
| 2175 / 2192 | Cese definitivo / cese temporal-habilitación | Papel | — |
| Customs: 8008 / 8028 / 8530 / 8540 / 8560 | Ramo Aduanas (Web+DG) / ingresos privativos / específicos y otros / ATC / pago declaración aduanera | see EVID-384 | — |
| Specific: 6051 / 6080 / 6090 / 9031 / 9050 / 9001 / 9208; tabaco 5011-5064, 7200; bebidas 26, 611-621, 3109-3120; vehículos 4041/4081/4091/4121/4131/4170, 8611/8620/8933, 4015/4053 | petróleo semanal/informativo/cuenta corriente; señales; IUSI trimestral/papel; cemento; tabaco; bebidas; vehículos | mostly DG | — |

## Dated-validity ledger (D16; all printed validity strings in the dump)

| Form | Table | valid_from | valid_to (as printed) |
|---|---|---|---|
| 7130 | Vigentes | 2015-08-25 | — ("Vigente a partir del 25 de agosto 2015.") |
| 2237 | Vigentes | 2013-09 | — ("Septiembre 2013 en adelante") |
| 2046 | Vigentes | 2013-09 | — ("Septiembre 2013 en adelante") |
| 2085 | Vigentes | 2013-09 | — ("Septiembre 2013 en adelante") |
| 2086 | Vigentes | 1999-01 | 2013-09 (bounded, yet vigente) |
| 1025 | NoVigentes | 2004-01 | 2012-04 |
| 1055 | NoVigentes | 1999-01 | 2012-12 |
| 1096 | NoVigentes | 2001-01 | 2012-12 |
| 1128 | NoVigentes | 1999-01 | 2012-12 |
| 1179 | NoVigentes | 2004 | 2012 |
| 1189 | NoVigentes | 2004 | 2012 |
| 1249 | NoVigentes | 2004-01 | 2012-12 |
| 1351 | NoVigentes | 2013-01 | 2013-04 |
| 1609 | NoVigentes | 2009-01 | 2013-09 (LB printed: D73-2008) |
| 2047 | NoVigentes | 2012-02 | 2013-09 |
| 2049 | NoVigentes | 2001-03 | 2012-01 |
| 2157 | NoVigentes | 2001-01 | 2013-10 |
| 2238 | NoVigentes | 2001-01 | 2013-10 |

---

## Open questions (file-level, numbered OQ-1..)

- **OQ-1 (controller attention — plan-mapping corrections):** the unit-19 plan's priority map is wrong on three codes, per the page's own descriptions: ISR retenciones = **1331** (1321 = ISR Capital Mensual); ISR anual (lucrativas family) = **1411** (1371 = ISR No Residentes Pago Directo, monthly); asalariados/relación de dependencia annual = **1431** (1411 is NOT asalariados). 2046/2241/1361/2340/2320/2000 confirmed as planned.
- **OQ-2:** **SAT-2390 does not appear anywhere in the dump.** The devolución-crédito-fiscal family here = 2124 (general, paper) / 2053-2062-2073 (exportadores, paper) with superseded 2052/2123. Nav chrome ("Formularios Electrónicos Solicitud Dev. C.F. Régimen Especial Electrónico y Régimen General") indicates current ELECTRONIC dev.CF forms exist but are not itemized in these 4 tables; likewise DUCA/SAT-2901 customs forms and the LAT dividendos-withholding successors of 7061/7101.
- **OQ-3:** same-code / duplicate rows as printed: 1219 (Anexo ISR–IPF) in BOTH VigentesAnexo and NoVigentesAnexo; 2302 papel-vigente vs web-no-vigente; 1111 app-vigente vs papel-no-vigente; 511 in both Vigentes main table (Web) and VigentesAnexo (app). Version semantics not explained by the page.
- **OQ-4:** printed period overlap: successors 2237/2046/2085 ("Septiembre 2013 en adelante") vs predecessors 2157/2238 ("hasta Octubre 2013") — one overlapping month as printed, flagged not corrected. Also 2086 sits in the Vigentes table with a CLOSED 1999-01→2013-09 window (presumably retained for old-period filings); and date formats vary ("3-2001", "1-2012", "febrero -2012", "enero – 2009" [sic spacing/dash]).
- **OQ-5:** as-of = Wayback snapshot 2025-10-06 only; no page dateModified in the dump. Channel definitions still describe the BancaSAT-era Asiste/AsiseWeb/AsiseLight stack even though row data shows those channels carry (almost) nothing vigente — the page may lag SAT's current portal (e.g., Agencia Virtual "Mis Declaraciones"); treat the channel model as SAT-published, not exhaustive.
- **OQ-6:** main-table column headers as flattened ("Impreso" / "Electrónico – Asiste" over "Papel | Web: | Light: | DG:") group DG ambiguously under "Electrónico – Asiste", yet the page's own definitions make Declaraguate a separate system from Asiste — read DG as its own channel.
- **OQ-7:** typos as printed, never corrected: "Descripcción" [sic] (Anexo header); "AsiseLight"/"AsiseWeb" spellings (vs "Asiste" elsewhere); stray spacing in dated strings (OQ-4).
- **OQ-8:** no maquila/ISA-specific declaration forms appear: the exportador presence is only via the devolución de crédito fiscal trio (2053/2062/2073); ISO (1608/1609) is the only solidarity-tax form. If the plan expected an ISR-exportadores/maquila declaration family, it is not in this catalog.
