# GT — Fiscal reporting — Form inventory & channel model (SAT lista general de formularios)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala master form
registry and filing-channel model (cluster F1): SAT's own authoritative
*form ↔ obligation ↔ channel* mapping as published on the *Lista general de
formularios (trámites y pago de impuestos)* (general list of forms — tax
procedures and payment) page, captured as a Wayback snapshot dated
**2025-10-06** — an **administrative catalog, not a legal instrument**. It
carries: the four source tables (Vigentes 82 rows, VigentesAnexo 24,
NoVigentes 54, NoVigentesAnexo 9); the page's own four channel definitions
(**Papel** (paper), **AsiseLight**, **AsiseWeb**, **Declaraguate**) plus the
application-generated *Anexo* forms as a **fifth filing surface**; the
corrected ISR form-identity spine (R46, binding: ISR anual lucrativas =
**SAT-1411**; asalariados anual = **SAT-1431**; **SAT-1371** = no-residentes
pago directo mensual; ISR retenciones = **SAT-1331**; **1321** = ISR capital
mensual); the same-code/channel-split version dimension (GOQ-93); the
dated-validity ledger of 18 printed validity strings under the dated-instrument
regime (D15/D16), including the R53 Sep/Oct-2013 both-windows rule and the
Dic-2012 LAT cliff; the R58 negative finding that electronic devolución-CF
forms, DUCA/SAT-2901 customs forms and the LAT dividendos successors of
7061/7101 live **outside** the 4-table catalog (GOQ-92); the GOQ-95 negative
finding (no maquila/ISA-specific declaration family); the GOQ-94 as-of
stamping and registry-freshness regime; the *calendario perpetuo* (perpetual
filing calendar) ingestion surface for per-NIT-last-digit *vencimiento*
(deadline) windows (GOQ-14); and existence-capture catalog-echo rows for the
customs family, the specific-tax families and the compliance/admin surface
without re-deriving their mechanics.

It does **not** cover: the operational declaration surfaces themselves — the
RetWeb agent population and 2340/2320 operational mechanics (Task 2 file,
`02_retenciones-web.md`), the pequeño-contribuyente forms 2046/2241 in
operation (Task 3, `03_pequeno-libro-regime.md`; statutory regime owned by
`gt/requirements/taxation/02_iva-pequeno.md` GT-TAX-FR-046..068), SAT-2390 and
the electronic dev.CF spec (Task 5, `05_devolucion-credito-fiscal.md`); the
SAT-1111 *mechanics* (payroll-owned: `gt/requirements/payroll/09_isr-iva-interfaces.md`
GT-PAY-FR-213..222, cross-referenced here by exact id); form-identity
ownership for the retention matrix (`gt/requirements/taxation/03_iva-retenciones.md`
GT-TAX-FR-107); customs-form mechanics (DUCA/SAT-2901 field specs — customs
out of scope); the statutory windows/rates behind each obligation (taxation
and payroll waves, cross-referenced); and deadline computation beyond the
external-calendar ingestion contract (F-cluster deadline files).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble — fiscal
reporting): **48_ = dated registry data (as-of 2025-10-06 Wayback),
SAT-published but not exhaustive**. The catalog is SAT's own authoritative
form↔obligation↔channel mapping; where a row prints its legal basis
(Decreto 73-2008 at 1609; Decreto 37-92 at 7061; Decretos 21-04 y 9-02 at
3035; "art.44 y 44A Ley del ISR" at 1241/1249), that printed citation is the
LB candidate for the row. Manuals outrank it only for declaration MECHANICS;
statutory instruments outrank both for parameters. Stage-1 quirk: 48_ is an
HTML snapshot whose tables live inside an escaped JS payload — quotes below
are verified against the recovered dump
`gt/.extractions/48_SAT_Lista_Formularios.txt` (line numbers cited), never
the raw HTML. Form identities follow R46 (corrected, binding) on every
ISR-form-naming row; R53 (both printed windows) and R58 (absence ≠
nonexistence) govern the ledger and outside-catalog rows. Dated rows follow
D15/D16 (cite together): valid_from/valid_to + provenance + as-of qualifier.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 48_ page head + channel definitions: "Lista general de formularios (trámites y pago de impuestos)" / "El guión que aparece en algunas casillas significa que el formulario no está disponible en ese formato." / "Formularios en Papel: Estos formularios los puede adquirir en cualquier Oficina o Agencia Tributaria en las diferentes regiones del país." / "AsiseLight: Puede descargar de Internet la edición para el formulario específico que desea llenar, y generar el archivo electrónico para utilizarse en BancaSAT." / "AsiseWeb: Es la versión en línea del Asiste, que encuentra en los sitios de Internet de los bancos que ofrecen el servicio BancaSAT." / "Declaraguate: Es un sistema por medio del cual pueden llenar vía Internet diferentes formularios electrónicos para la declaración y el pago de impuestos." + headers " | Descripción | Impreso | Electrónico – Asiste" / " | Papel | Web: | Light: | DG:" | Page identity and the page's own channel model: general list of forms (tax procedures and payment); the dash in a cell means the form is not available in that format; Paper forms acquirable at any Oficina or Agencia Tributaria nationwide; AsiseLight = download the form edition offline and generate the electronic file for BancaSAT; AsiseWeb = the online Asiste hosted at banks offering BancaSAT; Declaraguate = SAT's internet system for filling electronic forms for declaration AND payment of taxes (EVID-371) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 4-17 (EVID-371) |
| LB-002 | 48_ FormulariosVigentes, ISR monthly family: "ISR Opcional Mensual | – | – | – | 1311" / "ISR Capital Mensual | – | – | – | 1321" / "ISR Retenciones | – | – | – | 1331" / "ISR Sorteos | – | – | – | 1341" / "ISR No Residentes Retenciones | – | – | – | 1352" | Vigente monthly ISR set, all Declaraguate-only: optional monthly 1311; capital monthly 1321; ISR retenciones (general withholding declaration) 1331; sorteos 1341; non-resident retentions 1352. Plan-mapping correction (R46): ISR retenciones = 1331, NOT 1321 (1321 = ISR Capital Mensual) (EVID-372) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 32-36 (EVID-372) |
| LB-003 | 48_ FormulariosVigentes: "ISR Trimestral. Impuesto Sobre la Renta. Régimen Sobre Utilidades de Actividades Lucrativas. Declaración Jurada y Pago Trimestral. | – | – | – | 1361" / "ISR No Residentes. Pago Directo. Impuesto Sobre la Renta. Pagos en Forma Directa por No Residentes sin Establecimiento Permanente que no fueron objeto de retención. Declaración Jurada y Pago Mensual. | – | – | – | 1371" / "ISR Anual. Impuesto Sobre la Renta. Para los Regímenes Sobre las Utilidades de Actividades Lucrativas, Opcional Simplificado, Sobre Ingresos de Actividades Lucrativas y Contribuyentes Exentos. | – | – | – | 1411" / "ISR Relación de Dependencia. Impuesto Sobre la Renta. Rentas del Trabajo en Relación de Dependencia, Declaración Jurada y Pago Anual. | – | – | – | 1431" / "Impuesto de Solidaridad. Recibo de pago Trimestral. | – | – | – | 1608" | Plan-mapping corrections (R46): SAT-1371 is NOT "ISR anual" — it is the monthly non-resident direct-payment declaration (income not subject to retention, no permanent establishment); SAT-1411 is NOT "asalariados" — it is the annual ISR for the lucrativas family (Utilidades + Opcional Simplificado + Sobre Ingresos + Exentos); the rentas-del-trabajo annual declaration is SAT-1431 (Relación de Dependencia); quarterly lucrativas = 1361; ISO quarterly receipt = 1608. All DG-only (EVID-373) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 37-41 (EVID-373) |
| LB-004 | 48_ FormulariosVigentes: "Declaración Jurada y Pago Mensual del Impuesto al Valor Agregado para contribuyentes que realicen operaciones locales y de exportación. Válido para períodos de Imposición Septiembre 2013 en adelante. | – | – | – | 2237" / "Impuesto al Valor Agregado. Régimen de Pequeño Contribuyente. Declaración Jurada Simplificada y Pago Mensual. Válido para períodos de Imposición Septiembre 2013 en adelante | – | – | – | 2046" / "IVA-Régimen Electrónico de Pequeño Contribuyente | – | – | – | 2241" | IVA monthly general declaration = SAT-2237 (one form for taxpayers doing local AND export operations), DG-only, valid for tax periods September 2013 onwards; pequeño contribuyente simplified monthly = SAT-2046, DG-only, same 2013-09 valid_from; electronic pequeño regime = SAT-2241, DG-only, no printed validity (EVID-374) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 44, 53-54 (EVID-374) |
| LB-005 | 48_ FormulariosVigentesAnexo (RETENCIONES WEB) + dated receipts + 2302 split: "RETENCIONES WEB | Constancia de Retención del IVA | 2229" / "RETENCIONES WEB | Declaración Jurada de IVA Retenciones Agropecuario | 2320" / "RETENCIONES WEB | Declaración Jurada de Retenciones del IVA | 2340" / "Impuesto al Valor Agregado. Retenciones efectuadas al emitir Facturas Especiales. Recibo de pago. Válido para períodos de Imposición Septiembre 2013 en adelante. | – | – | – | 2085" / "Recibo de Pago, Compra-venta de Bienes Inmuebles, Retención a Facturas Especiales. Válido para períodos de imposición desde enero – 1999 hasta septiembre – 2013. | – | – | – | 2086" / "Solicitud de acreditamiento en cuenta de remanentes por retenciones de IVA | 2302 | – | – | –" (Vigentes, papel) / "Solicitud de acreditamientos en cuenta de remanentes por retenciones del IVA | – | 2302 | – | –" (No Vigentes, web) | The IVA-withholding declarations are generated in the RETENCIONES WEB application, not Declaraguate: general 2340, agropecuario 2320, retention certificate 2229; facturas-especiales retention receipts 2085 (valid ≥ 2013-09) and 2086 (bounded 1999-01 → 2013-09, yet listed among Vigentes — usable for old-period filings); remanentes accreditation 2302: paper version vigente, web version no vigente (same code, channel-dependent validity) (EVID-375) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 48-49, 57, 102-104, 172 (EVID-375) |
| LB-006 | 48_ FormulariosVigentesAnexo (RETENISR) + superseded: "RETENISR | Impuesto Sobre la Renta del Trabajo. Informe Anual de Liquidación y Devolución de lo Retenido en Exceso | 1481" / "RETENISR | Declaración Jurada ante el Patrono del ISR. | 1901" / "RETENISR | Constancia de Retención del ISR. Régimen Opcional Sobre Ingresos de Actividades Lucrativas y Rentas de Capital | 1911" / "RETENISR | Constancia de Retención del ISR del Trabajo. | 1921" / "RETENISR | Anexo a Retenciones ISR – IPF | 1219" / (no vigentes:) "RETENISR | Declaración Jurada Anual de Conciliación de Retenciones Efectuadas a Empleados en Relación de Dependencia | 1078" / "RETENISR | Conciliación Anual de Retenciones Practicadas a Empleados en Relación de Dependencia | 1088" | The wage-ISR (payroll) instruments live in the RETENISR application: annual declaration before the employer 1901; annual liquidation/devolución informe 1481; retention certificates 1921 (trabajo) and 1911 (opcional + rentas de capital); ISR-IPF annex 1219 (also printed among no-vigentes); superseded annual reconciliation forms 1078/1088 (EVID-376) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 105-109, 186-188 (EVID-376) |
| LB-007 | 48_ SAT-1111 dual rows: "PLANILLA IVA-FEL | Planilla para el Crédito por Impuesto al Valor Agregado | 1111" (VigentesAnexo) / "Impuesto Sobre la Renta Planilla para el Crédito por Impuesto al Valor Agregado IVA | 1111 | – | – | –" (No Vigentes, papel) | Code 1111 carries two instruments in two tables: the vigente, application-generated PLANILLA IVA-FEL form (employee IVA-credit planilla) and the retired no-vigente PAPER ISR-law planilla; the 56_ manual identifies the current one as the January-window output "Formulario SAT-1111" + Constancia, statutory anchor LAT art. 72 (D10-2012) — mechanics owned by payroll/09 (EVID-377) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 118, 149 (EVID-377) |
| LB-008 | 48_ exportadores trio + general devolución + superseded: "Solicitud de Registro al Régimen Especial de Devolución de Crédito Fiscal a Exportadores | 2053 | – | – | –" / "Declaración Jurada y Solicitud de Devolución Régimen Especial de Crédito Fiscal a Exportadores, ante el Banco de Guatemala | 2062 | – | – | –" / "Actualización Registro Especial de Devolución a Exportadores | 2073 | – | – | –" / "Solicitud de Devolución de Crédito Fiscal del IVA, o Restitución de Pagos Indebidos o en Exceso de Otros Impuestos, Impuestos Pagados por Importación de Combustibles o Depósitos por Garantías Aduanales | 2124 | – | – | –" / (no vigentes:) "Solicitud de Registro al Régimen Especial de Devolución de Crédito Fiscal a Exportadores. | – | 2052 | – | –" / "Solicitud de Devolución de Crédito Fiscal del IVA o de Pagos Indebidos o en Exceso de Otros Impuestos. | – | 2123 | – | –" | Exportadores special regime serviced by a paper-only trio: registration 2053, devolución application 2062 filed before the Banco de Guatemala, registro update 2073; superseded web versions 2052/2123; general devolución/restitución = 2124 (paper): IVA crédito fiscal, undue/excess payments, fuel-import taxes, customs guarantee deposits. NO form 2390 appears anywhere in the dump (EVID-378) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 45-47, 50, 165, 167 (EVID-378) |
| LB-009 | 48_ agro + EXENIVA: "Régimen Especial de Contribuyente Agropecuario | – | – | – | 2280" / "IVA Electrónico Especial de Contribuyente Agropecuario | – | – | – | 2290" / "Solicitud de habilitación en el sistema de ExenIVA (gratuito) | 351 | – | – | –" / "EXENIVA | Constancia de Exención IVA | 2093" / "EXENIVA | Informe Trimestral de uso de Constancias de Exención | 2118" | Agropecuario special regime has two DG-only declaration forms (2280 regime; 2290 IVA electrónico), plus agro IVA-retention declaration 2320 via Retenciones Web (LB-005); IVA-exemption certificates run through the EXENIVA system: habilitación 351 (paper, free of charge), constancia 2093, quarterly usage informe 2118 (app-generated) (EVID-379) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 25, 55-56, 110-111 (EVID-379) |
| LB-010 | 48_ FormulariosNoVigentes ISR-law ledger (anchors): "Declaración Jurada y Recibo de Pago Trimestral del ISR. Válido para períodos de imposición desde Enero 2004 hasta Abril 2012 | – | – | – | 1025" / "Declaración Jurada y Recibo de Pago Mensual de Retenciones del ISR e Impuesto Sobre Productos Financieros. Válido para períodos de imposición desde Enero 1999 hasta Diciembre 2012 | – | – | – | 1055" / "Declaración Jurada Anual y Recibo de Pago ISR Asalariados. Válido para períodos de Imposición desde 2004 hasta el 2012 | – | – | – | 1179" / "Declaración Jurada Anual y Recibo de Pago ISR Régimen General. Válido para períodos de Imposición desde 2004 hasta el 2012 | – | – | – | 1189" / "ISR Retenciones No Residentes Pago Retenciones. Válido para períodos de Imposición desde Enero 2013 hasta Abril 2013 | – | – | – | 1351" / "Declaración Jurada y Recibo de Pago Mensual, Art. 44 y 44 “A” de la Ley del ISR (con reformas). Válido para períodos de Imposición desde Enero 2004 hasta Diciembre 2012 | – | – | – | 1249" | Dated-validity ledger for the old-law ISR family (R46 discipline on every ISR-form-naming row): annual asalariados 1179 and régimen general 1189 valid 2004→2012; monthly retenciones+IPF 1055 1999-01→2012-12; art. 44/44-A monthly 1249 2004-01→2012-12 (LB printed: "Art. 44 y 44 A de la Ley del ISR"); quarterly 1025 2004-01→2012-04; transitional no-resident retención 1351 only 2013-01→2013-04; also no-resident retención 1096 2001-01→2012-12 and revaluación 1128 1999-01→2012-12; undated superseded 1024/1193/1197/1241/1121; one-off regimes IETAAP 1169, IEMA 1037. The Dic-2012 cliff = the LAT (D10-2012) replacing the old ISR law from 2013 (EVID-380) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 144-159 (EVID-380) |
| LB-011 | 48_ FormulariosNoVigentes IVA/ISO predecessors (anchors): "Formulario de Pago del Impuesto de Solidaridad (Decreto 73-2008 del Congreso de la República). Válido para períodos de imposición desde enero – 2009 hasta septiembre – 2013. | – | – | – | 1609" / "Declaración Jurada Simplificada y Pago Mensual del IVA para Pequeños Contribuyentes. Válido para períodos de imposición desde febrero -2012 hasta septiembre – 2013 | – | – | – | 2047" / "Declaración Jurada Simplificada y Pago Trimestral del IVA para Pequeños Contribuyentes. Válido para períodos de imposición desde 3-2001 hasta 1-2012. | – | – | – | 2049" / "Declaración y Recibo de Pago Mensual del IVA y Anexo. Válido para períodos de Imposición desde Enero 2001 hasta Octubre 2013. | – | – | – | 2157" / "Declaración y Recibo de pago mensual del Impuesto al Valor Agregado (Para contribuyentes que realicen exclusivamente operaciones locales). Válido para períodos de Imposición desde Enero 2001 hasta Octubre 2013. | – | – | – | 2238" / "Factura y Declaración Única Centroamericana | – | 2291 | – | –" | Predecessor chains: 2237 ← 2157 (IVA monthly + anexo) / 2238 (locals-only), both valid 2001-01→2013-10 (2232 undated); 2046 ← 2047 (2012-02→2013-09 [sic formats]) ← 2049 (quarterly, 2001-03→2012-01 [sic]) ← 2043 (undated); 1608 ← 1609 (ISO, LB printed Decreto 73-2008, 2009-01→2013-09). Printed overlap flagged, not corrected (R53): successors say "Septiembre 2013 en adelante" while 2157/2238 say "hasta Octubre 2013" — one overlapping month as printed. Also superseded 2028 (Declaración Anual del IVA, Régimen Simplificado) and FYDUCA 2291 (web) (EVID-381) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 160-164, 168-171 (EVID-381) |
| LB-012 | 48_ channel row-data anchors: "Recibo de Cobranza y Control de Multas | – | – | – | 811" / "Aviso Anulación de Documentos | – | 511 | – | –" / "Boleta para presentar y pagar formulario previamente llenado a través de Declaraguate | – | 2000 | – | 2000" / "Formulario para Pago Ramo Aduanas | – | 8008 | – | 8008" / "Recibo de pago de Ingresos Privativos por Gestiones de Vehículos Terrestres | – | 8209 | – | –" / "AGENCIA VIRTUAL | Anexo y Formulario del Impuesto a la Distribución de Bebidas Alcohólicas y No Alcohólicas de Declaraguate en la Agencia Virtual | 3109" | Channel matrix read as data (vigentes, main table): every tax declaration/payment form is DG-only (the 1311…9911 set); 27 forms paper-only (26, 27, 45, 62, 72, 73, 251, 351, 362, 411, 2033, 2053, 2062, 2073, 2124, 2175, 2192, 4053, 5011, 5021, 5031, 5041, 5064, 7001, 7012, 7016, 9001); Light column empty for every vigente row (Light values only among no-vigentes: 81, 149, 229, 1151, 3035, 5056, 5079, 7069, 7109 + ASISTELIGHT app rows 6017/6021/6049, 3081/3091) → AsiseLight is a legacy channel; Web-only survivors 511, 8209; dual Web+DG 2000 (boleta) and 8008; the 24 Anexo forms are generated inside named applications — a fifth filing surface beyond the 4 channel columns (EVID-382) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 18-125 read as data; anchors lines 28-29, 42, 81, 83, 123 (EVID-382) |
| LB-013 | 48_ libros/protocolos + timbres-dividendos: "Habilitación de Libros. Impuesto de Timbres Fiscales y de Papel Sellado Especial para Protocolos. Habilitación y autorización de libros. | – | – | – | 7121" / "Impuesto de Timbres Fiscales y Papel Sellado Especial para Protocolos. Recibo de Pago. Vigente a partir del 25 de agosto 2015. | – | – | – | 7130" / "Impuesto Sobre Títulos Universitarios y de Carreras Técnicas | – | – | – | 7190" / "Herencia, Legados y Donaciones | – | – | – | 8490" / (no vigentes:) "Constancia de Retención por pago de dividendos o utilidades según Decreto 37-92 del Congreso de la República y sus reformas. Ley del Impuesto de Timbres y de Papel Sellado Especial para Protocolo | 7061 | – | 7069 | –" / "Retenciones sobre Dividendos o Utilidades – Declaración Jurada de Retenciones del Impuesto de Timbres Fiscales y de Papel Especial para Protocolo | 7101 | 7109 | 7109 | –" | Books/protocolos: habilitación y autorización de libros = 7121 (DG), page-scoped to Protocolos timbres; protocolos payment receipt 7130 is dated — "Vigente a partir del 25 de agosto 2015" (valid_from 2015-08-25); títulos universitarios 7190; herencias/legados/donaciones 8490; superseded timbres-dividendos withholding pair 7061 (constancia) / 7101-7109 (DJ retenciones), LB printed Decreto 37-92 (pre-LAT timbres regime) (EVID-383) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 77-79, 88, 178-179 (EVID-383) |
| LB-014 | 48_ customs + specific taxes (existence anchors): "Formulario para Pago Declaración Aduanera | – | – | – | 8560" / "Aduana ATC | – | – | – | 8540" / "Aduanas Específicos y Otros | – | – | – | 8530" / "Formulario para Pago Ramo Aduanas | – | 8008 | – | 8008" / "Declaración jurada y pago semanal del Impuesto a la Distribución de Petróleo Crudo y Combustibles Derivados del Petróleo | – | – | – | 6051" / "Impuesto Único Sobre Inmuebles. Impuesto sobre el valor de los bienes inmuebles situados en el territorio de la República. Recibo de pago trimestral. | – | – | – | 9050" / "Recibo de Impuesto Único Sobre Inmuebles. | 9001 | – | – | –" / "Declaración Jurada y Recibo de Pago del Impuesto a la Distribución del Cemento. | – | – | – | 9208" / "Impuesto a la Distribución de Señales por Cable. Declaración Jurada y Pago Mensual. | – | – | – | 9031" / (no vigente:) "Declaración Jurada y Recibo de Pago del Impuesto a la Distribución de Bebidas Alcohólicas y Otras. Decretos No. 21-04 y 9-02 del Congreso de la República de Guatemala | – | – | 3035 | –" | Existence capture per family: customs (8560 pago declaración aduanera; 8008 ramo aduanas Web+DG; 8530 específicos y otros; 8540 ATC; 8028 ingresos privativos; superseded 8005/8021/2291 FYDUCA); specific taxes: petróleo (6051 weekly; 6080 monthly informative; 6090 annual exempt-products cuenta corriente), IUSI (9050 quarterly DG; 9001 paper receipt), cemento 9208, señales por cable 9031, tabaco (5011/5021/5031/5041/5064/7200; superseded 5056/5071-5079), bebidas (26, 611, 621, 3109-3120; superseded 3035 — LB printed Decretos 21-04 y 9-02 — /3061/3081/3091), vehículos (IPRIMA 4041/4081; circulación 4091/4121/4131/4170; plates/records 8611/8620/8933/4053/4015; superseded 4001). DUCA/SAT-2901 not itemized here (EVID-384) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 18-124 family rows; anchors lines 81, 89-91, 71, 95-98, 173 (EVID-384) |
| LB-015 | 48_ compliance/admin surface + as-of: "Formulario Solicitud de Convenio de pago | – | – | – | 821" / "Facilidades de Pago | – | – | – | 891" / "Certificación de Cumplimiento. Solicitud de Certificación de estar al día en el cumplimiento de obligaciones tributarias | – | – | – | 8421" / "Cese de actividades definitivo | 2175 | – | – | –" / "Cese temporal o habilitación de actividades económicas | 2192 | – | – | –" / "RECIBO COBRANZA FISCALIZACIÓN | Recibo de ingresos por pago de sanciones y ajustes de fiscalización | 860" / (no vigente:) "Formulario de actualización por Depuración del Registro Tributario Unificado. | FAD 02 | – | – | –" / header: "=== SOURCE: gt/sources/48_SAT_Lista_Formularios_2025-10-06.html (Wayback snapshot 2025-10-06 of portal.sat.gob.gt/portal/lista-general-de-formularios/) ===" | Compliance-adjacent surface: payment boleta 2000 (Web+DG, LB-012) for Declaraguate-pre-filled forms; multas receipt 811; convenio de pago 821 + facilidades de pago 891; fiscalización sanciones/ajustes receipt 860 (app-generated); solvencia/certificación de cumplimiento 8421; cease-of-activity notices 2175 (definitivo) and 2192 (temporal) are paper-only — no electronic channel for the registry-exit workflow on this page; deprecated RTU-depuration form "FAD 02" (non-SAT-prefixed code). As-of evidence = Wayback snapshot 2025-10-06 only; no dateModified in the dump (GOQ-94) (EVID-385) | `gt/sources/48_SAT_Lista_Formularios_2025-10-06.html` (read via dump) | dump lines 1, 29-31, 51-52, 86, 125, 182 (EVID-385) |
| LB-016 | Master-index register GOQ-14 (via `gt/HANDOVER.md` §8, accountant track, asked 2026-08-19): "calendario perpetuo vencimiento windows per NIT last-digit (monthly/quarterly/annual)" + plan B: "calendar windows → transcribe from SAT's JSF app in owner browser with atlas.com.gt as cross-check only" | The per-NIT-last-digit deadline (vencimiento) windows of SAT's perpetual filing calendar are EXTERNAL DATA: a pending accountant-delivered acquisition, plan-B transcribed from SAT's JSF application with atlas.com.gt as cross-check ONLY — never invented. Register trace, no 48_ EVID (the catalog prints no deadline data) | `gt/.extractions/00_MASTER_INDEX.md` §C (GOQ-14) via `gt/HANDOVER.md` | §8 accountant track (EVID: none — register trace GOQ-14) |

## 3. Functional Requirements

### 3.1 Form registry core (the 48_ catalog as data)

- **GT-FIN-FR-001:** The system shall maintain the GT form registry as a
  four-table seed mirroring the 48_ catalog exactly as printed:
  FormulariosVigentes (82 rows), FormulariosVigentesAnexo (24 rows, heading
  "FORMULARIOS QUE SE GENERAN EN APLICACIONES ELECTRÓNICAS"),
  FormulariosNoVigentes (54 rows) and FormulariosNoVigentesAnexo (9 rows),
  each row carrying the printed description, channel cells ("–" = form not
  available in that format), table membership and vigencia status — the
  registry is SAT-published administrative data (not a legal instrument),
  stamped as-of 2025-10-06 with the Wayback provenance and the
  SAT-published-not-exhaustive qualifier on every read surface.
  (LB-001; LB-015; EVID-371, EVID-385)
- **GT-FIN-FR-002:** The system shall model form availability as a per-form
  channel matrix {papel, asiste-web, asiste-light, declaraguate} seeded from
  the four page-defined channels with their definitions carried verbatim:
  Papel (acquirable at any Oficina o Agencia Tributaria), AsiseLight
  (offline download, electronic file for BancaSAT), AsiseWeb (online Asiste
  hosted at BancaSAT-offering banks), Declaraguate (SAT internet system for
  filling e-forms for declaration and payment); a dash cell = not available.
  Reading rule (page-legend doubt resolved as data): although the flattened
  header groups DG under "Electrónico – Asiste", the page's own definitions
  make Declaraguate a separate system — DG is modelled as its own channel.
  Spellings "AsiseLight"/"AsiseWeb" preserved as printed (SAT styles the app
  "Asiste" elsewhere). (LB-001; EVID-371)
- **GT-FIN-FR-003:** ISR form identities shall follow the R46 corrected
  spine, binding on every ISR-form-naming row in the product: **ISR anual
  (lucrativas family) = SAT-1411; asalariados/relación de dependencia anual
  = SAT-1431; SAT-1371 = ISR No Residentes Pago Directo (mensual); ISR
  retenciones = SAT-1331; SAT-1321 = ISR Capital Mensual**. The W4-era plan
  map ("1371 = ISR anual", "1411 = asalariados", "1321 = retenciones") is
  contradicted by the catalog's own row descriptions and shall fail
  validation wherever it appears. (LB-002; LB-003; EVID-372, EVID-373; R46)
- **GT-FIN-FR-004:** The registry shall carry the ISR monthly family
  (R46): SAT-1311 ISR Opcional Mensual, SAT-1321 ISR Capital Mensual,
  SAT-1331 ISR Retenciones, SAT-1341 ISR Sorteos, SAT-1352 ISR No
  Residentes Retenciones — all Declaraguate-only. (LB-002; EVID-372; R46)
- **GT-FIN-FR-005:** The registry shall carry the ISR periodic/annual set
  and ISO (R46): SAT-1361 ISR Trimestral (Régimen Sobre Utilidades de
  Actividades Lucrativas), SAT-1371 ISR No Residentes Pago Directo
  (declaración jurada y pago mensual, non-retained income of non-residents
  without permanent establishment), SAT-1411 ISR Anual (Utilidades /
  Opcional Simplificado / Sobre Ingresos / Exentos), SAT-1431 ISR Relación
  de Dependencia (rentas del trabajo, declaración jurada y pago anual),
  SAT-1608 Impuesto de Solidaridad recibo trimestral — all
  Declaraguate-only. (LB-003; EVID-373; R46)
- **GT-FIN-FR-006:** The registry shall carry the IVA declaration
  identities: SAT-2237 (declaración jurada y pago mensual del IVA,
  contribuyentes doing local AND export operations in one form, valid for
  períodos de imposición September 2013 onwards), SAT-2046 (Régimen de
  Pequeño Contribuyente, declaración jurada simplificada y pago mensual,
  valid ≥ 2013-09) and SAT-2241 (IVA-Régimen Electrónico de Pequeño
  Contribuyente, no printed validity) — all Declaraguate-only; the
  statutory regimes behind them are taxation-owned (cross-ref
  GT-TAX-FR-046..068), never re-derived here. (LB-004; EVID-374)
- **GT-FIN-FR-007:** The registry shall carry the RETENISR wage-ISR family
  (R46) as application-generated forms: SAT-1901 (declaración jurada anual
  ante el patrono del ISR), SAT-1481 (informe anual de liquidación y
  devolución de lo retenido en exceso), SAT-1911 (constancia de retención
  del ISR — Régimen Opcional y Rentas de Capital), SAT-1921 (constancia de
  retención del ISR del Trabajo), SAT-1219 (Anexo a Retenciones ISR – IPF);
  superseded annual reconciliation forms SAT-1078/SAT-1088 are no-vigente
  rows. These are the employer-side outputs of the LAT rentas-del-trabajo
  withholding — payroll-owned mechanics (cross-ref GT-PAY-FR-207..222
  wave), catalog-echoed here only. (LB-006; EVID-376; R46)

### 3.2 Channel model (row-data findings)

- **GT-FIN-FR-008:** The channel model shall encode the row-data findings
  of the vigentes main table as registry data: (i) every tax
  declaration/payment form is **Declaraguate-only** (the 1311…9911 set);
  (ii) **27 forms are paper-only**: 26, 27, 45, 62, 72, 73, 251, 351, 362,
  411, 2033, 2053, 2062, 2073, 2124, 2175, 2192, 4053, 5011, 5021, 5031,
  5041, 5064, 7001, 7012, 7016, 9001; (iii) Web-only survivors: 511, 8209;
  dual Web+DG: 2000 (boleta) and 8008 (ramo aduanas). (LB-012; EVID-382)
- **GT-FIN-FR-009:** Registry-driven filing-surface routing: the system
  shall route each obligation to its surface from the channel matrix — tax
  declarations to Declaraguate, paper-only admin forms to a paper workflow
  (print/track, no electronic emission), app-generated forms to their named
  application surface — and shall never route anything to AsiseLight or
  AsiseWeb (FR-010 guard). (LB-012; EVID-382)
- **GT-FIN-FR-010:** AsiseLight legacy guard: the Light column carries ZERO
  vigente forms (Light values exist only among no-vigentes: 81, 149, 229,
  1151, 3035, 5056, 5079, 7069, 7109, plus ASISTELIGHT/ASISTELIGHT-ASISTEWEB
  app rows 6017/6021/6049, 3081/3091); AsiseLight and AsiseWeb are BancaSAT-era
  legacy channels and shall never be modelled as current filing surfaces —
  the page's channel definitions may lag SAT's current portal (e.g. Agencia
  Virtual "Mis Declaraciones"), treat the channel model as SAT-published,
  not exhaustive (GOQ-94 → OQ-003). (LB-001; LB-012; EVID-371, EVID-382;
  GOQ-94 kin → OQ-003)
- **GT-FIN-FR-011:** The 24 Vigentes-Anexo forms generated inside SAT
  applications shall be modelled as a **fifth filing surface** beyond the
  four channel columns — the Anexo tables print no channel columns because
  the application IS the channel: RETENCIONES WEB (2229, 2320, 2340),
  RETENISR (1481, 1901, 1911, 1921, 1219), EXENIVA (2093, 2118), E-CAI
  (9021), AUTORIZACIÓN DOCUMENTOS / MÁQUINAS REGISTRADORAS (511, 521, 531,
  157), RFV (4015), PLANILLA IVA-FEL (1111), SISTEMA DE BEBIDAS ALCOHÓLICAS
  Y NO ALCOHÓLICAS (621, 611, 3110, 3120), AGENCIA VIRTUAL (3109), SISTEMA
  DE REGISTRO FISCAL DE VEHÍCULOS (4170), RECIBO COBRANZA FISCALIZACIÓN
  (860). The IVA-withholding declarations are NOT Declaraguate forms:
  general SAT-2340, agropecuario SAT-2320 and the constancia SAT-2229 via
  RETENCIONES WEB (operational mechanics owned by Task 2,
  `02_retenciones-web.md` — cross-referenced, never re-derived).
  (LB-005; LB-012; EVID-375, EVID-382)

### 3.3 Same-code / channel-split version dimension (GOQ-93)

- **GT-FIN-FR-012:** The registry key shall be the tuple
  (code, source-table, channel) — never the bare code — because the page
  prints same-code rows whose validity differs by table and/or channel:
  **1219** (Anexo a Retenciones ISR – IPF) in BOTH VigentesAnexo and
  NoVigentesAnexo; **2302** (solicitud de acreditamiento en cuenta de
  remanentes por retenciones de IVA) papel-vigente vs web-no-vigente —
  operationally paper-channel only; **1111** app-vigente vs
  paper-no-vigente (FR-013); **511** (aviso anulación de documentos) in
  the Vigentes main table (Web) AND in VigentesAnexo (app). The page does
  not explain the version semantics; the model stores each printed row as
  its own version, flagged, semantics unmerged (GOQ-93 → OQ-002).
  (LB-005; LB-006; LB-007; LB-012; EVID-375, EVID-376, EVID-377, EVID-382;
  GOQ-93 → OQ-002)
- **GT-FIN-FR-013:** SAT-1111 dual identity (R46 guard): the registry shall
  keep code 1111 as two distinct instruments — the vigente,
  application-generated **PLANILLA IVA-FEL** form (planilla para el crédito
  por IVA, employee annual IVA-credit planilla, LAT art. 72 regime) and the
  superseded no-vigente PAPER "Impuesto Sobre la Renta Planilla para el
  Crédito por Impuesto al Valor Agregado IVA" (old ISR-law planilla). The
  current surface is the app form; its mechanics are owned by payroll/09 —
  cross-referenced by exact id: GT-PAY-FR-213..218 (app identity, filing
  window, deliverables) and GT-PAY-FR-221 (planilla disambiguation guard).
  No surface may resolve bare "1111" to the paper instrument.
  (LB-007; EVID-377; cross-ref GT-PAY-FR-213..218, GT-PAY-FR-221; R46)

### 3.4 Dated-validity ledger (D15/D16)

- **GT-FIN-FR-014:** The registry shall store every printed
  dated-validity string as a dated row (valid_from/valid_to + provenance =
  the printed string + as-of qualifier 2025-10-06) — the 18-string ledger,
  as printed: 7130 (2015-08-25 →); 2237, 2046, 2085 (2013-09 →); 2086
  (1999-01 → 2013-09, bounded yet listed among Vigentes — retained for
  old-period filings); NoVigentes: 1025 (2004-01 → 2012-04), 1055
  (1999-01 → 2012-12), 1096 (2001-01 → 2012-12), 1128 (1999-01 → 2012-12),
  1179 (2004 → 2012), 1189 (2004 → 2012), 1249 (2004-01 → 2012-12), 1351
  (2013-01 → 2013-04), 1609 (2009-01 → 2013-09, LB printed Decreto
  73-2008), 2047 (2012-02 → 2013-09), 2049 (2001-03 → 2012-01), 2157
  (2001-01 → 2013-10), 2238 (2001-01 → 2013-10). Printed date formats vary
  ("3-2001", "febrero -2012", "enero – 2009" [sic]) — normalised into the
  dated fields with the [sic] string preserved in provenance; ISR-form
  rows of the ledger carry R46 discipline. (LB-004; LB-005; LB-010;
  LB-011; LB-013; EVID-374, EVID-375, EVID-380, EVID-381, EVID-383; R46)
- **GT-FIN-FR-015:** Form-version selection shall key on the período de
  imposición (tax period), and the printed Sep/Oct-2013 overlap shall be
  modelled as printed (R53: BOTH windows stored, flagged, never corrected):
  successors 2237/2046/2085 print "Septiembre 2013 en adelante" while
  predecessors 2157/2238 print "hasta Octubre 2013" — one overlapping month
  as printed. Old-period filings keep the predecessor codes: IVA monthly
  2001-01–2013-10 → 2157 (general + anexo) or 2238 (exclusively local
  operations); pequeño monthly 2012-02–2013-09 → 2047, quarterly
  2001-03–2012-01 → 2049; ISO 2009-01–2013-09 → 1609; old-law ISR
  (Dic-2012 LAT cliff): annual asalariados 2004–2012 → 1179, anual régimen
  general 2004–2012 → 1189, monthly retenciones+IPF 1999-01–2012-12 →
  1055, art. 44/44-A monthly 2004-01–2012-12 → 1249, no-resident
  retenciones 2001-01–2012-12 → 1096, revaluación 1999-01–2012-12 → 1128,
  quarterly 2004-01–2012-04 → 1025; transitional no-resident retención
  1351 only for 2013-01–2013-04; facturas especiales receipts 2085 (≥
  2013-09) / 2086 (1999-01–2013-09). Historical rows are non-transmittable
  class (D16). (LB-005; LB-010; LB-011; EVID-374, EVID-375, EVID-380,
  EVID-381; R53, R46)

### 3.5 Devolución/exportadores surfaces & outside-catalog negative rows

- **GT-FIN-FR-016:** The exportadores devolución de crédito fiscal workflow
  shall be routed as a paper-only trio — SAT-2053 (solicitud de registro al
  régimen especial) → SAT-2062 (declaración jurada y solicitud de
  devolución, filed **ante el Banco de Guatemala**) → SAT-2073
  (actualización del registro) — plus the general devolución SAT-2124
  (paper; scope: IVA crédito fiscal, pagos indebidos o en exceso, fuel-
  import taxes, customs guarantee deposits); the superseded web versions
  2052/2123 shall never be routed. Electronic successors live outside this
  catalog (FR-017); the dev.CF regime mechanics are Task 5 property.
  (LB-008; EVID-378)
- **GT-FIN-FR-017:** NEGATIVE FR (R58): SAT-2390 does not appear anywhere
  in the 48_ dump, and absence from the 4-table catalog ≠ nonexistence.
  The registry shall carry an **outside-catalog surface marker** family for
  instruments that live outside the catalog's 4 tables: the electronic
  devolución-CF forms (nav chrome names "Formularios Electrónicos Solicitud
  Dev. C.F. Régimen Especial Electrónico y Régimen General"), the customs
  DUCA/SAT-2901 forms, and the LAT dividendos-withholding successors of
  7061/7101 (cross-ref GT-TAX-FR-180 for the current dividendos regime).
  The enumeration of that family from the portal remains open (GOQ-92 →
  OQ-001; Task 5 owns SAT-2390). (LB-008; LB-013; EVID-378, EVID-383;
  cross-ref GT-TAX-FR-180; R58; GOQ-92 → OQ-001)
- **GT-FIN-FR-018:** NEGATIVE FR (GOQ-95): NO maquila- or ISA-specific
  declaration family exists in the 48_ catalog — the exportadores/maquila
  kin surface exists only via the devolución de crédito fiscal trio
  (2053/2062/2073, FR-016), and ISO (1608 vigente / 1609 superseded) is
  the only solidarity-tax form. Any expectation of an ISR-exportadores or
  maquila declaration form family shall resolve to "not in catalog" — the
  registry shall never synthesise one. (LB-003; LB-008; LB-011; EVID-373,
  EVID-378, EVID-381; GOQ-95 → OQ-004)
- **GT-FIN-FR-019:** The timbres-dividendos withholding pair SAT-7061
  (constancia de retención por pago de dividendos o utilidades) and
  SAT-7101/7109 (declaración jurada de retenciones) shall be stored as
  no-vigente rows with their printed legal basis **Decreto 37-92** (Ley del
  Impuesto de Timbres y de Papel Sellado Especial para Protocolo) — valid
  only pre-LAT; the current dividendos withholding regime is the LAT's
  (taxation-owned, cross-ref GT-TAX-FR-180); the LAT successors' form
  identities live outside this catalog (FR-017). (LB-013; EVID-383;
  cross-ref GT-TAX-FR-180)

### 3.6 Books/protocolos, agro/EXENIVA — catalog-echo rows

- **GT-FIN-FR-020:** The registry shall carry the books/protocolos and
  ISR-adjacent rows: SAT-7121 (habilitación y autorización de libros —
  page-scoped to Impuesto de Timbres Fiscales y de Papel Sellado Especial
  para Protocolos; DG), SAT-7130 (protocolos timbres recibo de pago, dated
  valid_from 2015-08-25; DG), SAT-7190 (impuesto sobre títulos
  universitarios y de carreras técnicas; DG), SAT-8490 (herencia, legados y
  donaciones; DG). The general libros/LEDGER habilitation flow is F-cluster
  property (Task 4) — echoed here as registry rows only.
  (LB-013; EVID-383)
- **GT-FIN-FR-021:** The registry shall carry the agropecuario and
  EXENIVA surfaces: SAT-2280 (Régimen Especial de Contribuyente
  Agropecuario, DG) and SAT-2290 (IVA Electrónico Especial de
  Contribuyente Agropecuario, DG) as the agro declarations, with the agro
  IVA-retention declaration SAT-2320 via RETENCIONES WEB (FR-011); the
  IVA-exemption certificate workflow through the EXENIVA system — SAT-351
  (solicitud de habilitación, paper, gratuito), SAT-2093 (constancia de
  exención IVA, app), SAT-2118 (informe trimestral de uso de constancias,
  app). (LB-005; LB-009; EVID-375, EVID-379)

### 3.7 As-of stamping & registry freshness (GOQ-94)

- **GT-FIN-FR-022:** As-of stamping: every registry row and every derived
  surface shall carry the qualifier that the registry is **SAT-published,
  not exhaustive, as-of 2025-10-06 (Wayback; no page dateModified)**, and
  that the channel definitions describe the BancaSAT-era stack (GOQ-94 →
  OQ-003); no surface may present catalog absence as legal nonexistence
  (R58, FR-017). (LB-001; LB-015; EVID-371, EVID-385; GOQ-94 → OQ-003)
- **GT-FIN-FR-023:** Registry freshness ingestion: a re-capture of the 48_
  catalog (or a successor publication) shall land as a NEW DATED VINTAGE —
  never a silent edit of live rows; vintage diffing surfaces added forms,
  retired forms, channel changes and validity-string changes; deadline
  computations and routing read the vintage effective for the período de
  imposición being filed. (LB-015; EVID-385)

### 3.8 Calendario perpetuo ingestion (GOQ-14)

- **GT-FIN-FR-024:** The per-NIT-last-digit *vencimiento* (deadline)
  windows of SAT's *calendario perpetuo* (monthly/quarterly/annual) shall
  be modelled strictly as EXTERNAL INGESTED DATA: acquired via the
  accountant track or transcribed from SAT's JSF application, with
  atlas.com.gt as cross-check provenance ONLY — the system shall never
  invent, extrapolate or hardcode a vencimiento window; absent data means
  no deadline object is generated and the gap is flagged (GOQ-14 → OQ-005;
  deadline consumers in the F-cluster read this ingestion surface).
  (LB-016; register trace GOQ-14; GOQ-14 → OQ-005)

### 3.9 Existence-capture catalog echoes (customs, specific taxes, compliance/admin)

- **GT-FIN-FR-025:** The registry shall include existence-capture rows —
  codes, descriptions, channels, superseded kin — for the customs family
  (SAT-8560 pago declaración aduanera; SAT-8008 ramo aduanas Web+DG;
  SAT-8530 aduanas específicos y otros; SAT-8540 aduana ATC; SAT-8028
  ingresos privativos "Gestiones Varias"; superseded 8005/8021 and FYDUCA
  2291) and the specific-tax families: petróleo (6051 weekly, 6080 monthly
  informative, 6090 annual exempt-products cuenta corriente), IUSI (9050
  quarterly DG; 9001 paper receipt), cemento 9208, señales por cable 9031,
  tabaco (5011/5021/5031/5041/5064/7200; superseded 5056/5071-5079),
  bebidas alcohólicas (26, 611, 621, 3109-3120; superseded 3035 — printed
  LB Decretos 21-04 y 9-02 — /3061/3081/3091), vehículos (IPRIMA
  4041/4081; circulación 4091/4121/4131/4170; plates/records
  8611/8620/8933/4053/4015; superseded 4001) — WITHOUT field-level
  modeling: mechanics are owned by other waves; customs (DUCA/SAT-2901) is
  out of scope and outside the catalog (FR-017). (LB-014; EVID-384)
- **GT-FIN-FR-026:** The registry shall include the compliance/admin
  surface as catalog-echo rows: SAT-811 (recibo de cobranza y control de
  multas, DG), SAT-821 (solicitud de convenio de pago, DG), SAT-891
  (facilidades de pago, DG), SAT-860 (recibo de ingresos por pago de
  sanciones y ajustes de fiscalización, RECIBO COBRANZA FISCALIZACIÓN
  app), SAT-8421 (certificación de cumplimiento / solvencia, DG), boleta
  SAT-2000 (pay a Declaraguate-pre-filled form; dual Web+DG), and the
  PAPER-ONLY cease-of-activity notices SAT-2175 (cese definitivo) and
  SAT-2192 (cese temporal o habilitación) — the registry-exit workflow has
  no electronic channel in this catalog; deprecated RTU-depuration form
  "FAD 02" (non-SAT-prefixed code) carried as a no-vigente oddity. No
  compliance mechanics (sanctions, installments) are derived here.
  (LB-012; LB-015; EVID-382, EVID-385)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + provenance
(the printed validity string, [sic] preserved) + as-of qualifier
(2025-10-06); snapshot-on-write; historical rows are non-transmittable
class. The registry is configuration data shared by every filing surface.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.form.registry | code / description_es / table / status / as_of / provenance | char / text / selection / selection / date / char | tables: vigentes (82) / vigentes_anexo (24) / no_vigentes (54) / no_vigentes_anexo (9); status: vigente / no_vigente as per table + printed exceptions; as_of = 2025-10-06 (Wayback; SAT-published, not exhaustive) | FR-001 |
| l10n_gt.form.registry | channels | boolean×4 | papel / web / light / declaraguate; dash = false; DG modelled as own channel (header-grouping quirk) | FR-002, FR-008 |
| l10n_gt.form.registry | app_surface | char, nullable | RETENCIONES WEB / RETENISR / EXENIVA / E-CAI / AUTORIZACIÓN DOCUMENTOS / RFV / PLANILLA IVA-FEL / SISTEMA DE BEBIDAS / AGENCIA VIRTUAL / SISTEMA DE REGISTRO FISCAL DE VEHÍCULOS / RECIBO COBRANZA FISCALIZACIÓN (Anexo rows: application IS the channel) | FR-011 |
| l10n_gt.form.registry | version_key | tuple | (code, table, channel) — never bare code; printed split instances: 1219 both anexo tables; 2302 papel-vigente/web-no-vigente; 1111 app-vigente/paper-no-vigente; 511 main+anexo | FR-012, FR-013 |
| l10n_gt.form.channel.def | channel / definition_es | selection / text | papel, asise_light, asise_web, declaraguate — definitions verbatim; legend: dash = not available in that format; asise_light + asise_web flagged legacy (0 vigente Light rows) | FR-002, FR-010 |
| l10n_gt.form.isr.spine | obligation / form_code | char / char | R46 binding set: ISR anual lucrativas = 1411; asalariados anual (relación de dependencia) = 1431; no-residentes pago directo mensual = 1371; ISR retenciones = 1331; ISR capital mensual = 1321 | FR-003..FR-005, FR-007 |
| l10n_gt.form.validity | form_code / valid_from / valid_to / printed_string / class | char / date / date / char / char | the 18-string ledger (FR-014 values); printed_string preserves [sic] formats; bounded-yet-vigente 2086; overlap flag for 2013-09/2013-10 (R53 both windows); historical = non-transmittable class | FR-014, FR-015 |
| l10n_gt.form.version.selection | periodo / resolved_form | date / char | selection keyed on período de imposición: old-period → predecessor codes (2157/2238/2047/2049/1609/1179/1189/1055/1249/1096/1128/1025/1351-window/2086); ≥ 2013-09 (IVA) → 2237/2046/2085 | FR-015 |
| l10n_gt.form.surface.routing | obligation / surface | char / selection | declaraguate / app:<name> / paper; declarations DG-only; 27 paper-only codes (FR-008 list); asise_light/asise_web never routed | FR-008, FR-009 |
| l10n_gt.form.outside.catalog | family / note | selection / char | electronic_dev_cf (SAT-2390 kin); customs_duca_2901; lat_dividendos_successors (of 7061/7101); marker only — enumeration open (GOQ-92); absence ≠ nonexistence (R58) | FR-017, FR-019 |
| l10n_gt.form.negative | finding | char | no maquila/ISA declaration family in 48_ (exportadores surface = dev.CF trio only; ISO 1608 only solidarity form) — GOQ-95 | FR-018 |
| l10n_gt.form.exportadores | sequence | char | 2053 registro → 2062 DJ+solicitud (ante el Banco de Guatemala) → 2073 actualización; paper-only; 2124 general; superseded 2052/2123 never routed | FR-016 |
| l10n_gt.form.registry.vintage | as_of / diff | date / json | v2025-10-06 baseline; refresh = new vintage, never silent edit; diff = added/retired/channel-change/validity-change | FR-001, FR-022, FR-023 |
| l10n_gt.filing.calendar.external | nit_last_digit / period_type / window / provenance | int / selection / char / char | per-NIT-last-digit vencimiento windows (calendario perpetuo); provenance = JSF transcription (accountant track) + atlas.com.gt cross-check ONLY; never invented; absent → flagged, no deadline object | FR-024 |
| l10n_gt.form.family.echo | family / rows | selection / char | customs (8560/8008/8530/8540/8028; sup. 8005/8021/2291); petróleo/IUSI/cemento/señales/tabaco/bebidas/vehículos code sets; compliance/admin (811/821/891/860/8421/2000/2175/2192/FAD 02); existence capture only, no field mechanics | FR-025, FR-026 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = ingestion,
transformation and authoritative validation in the Elixir core; `shared` =
contract items both sides must honor identically. Wave defaults for this
file: form registry + validity ledger + calendar ingestion contract =
`shared`; registry-driven filing-surface routing = `odoo`; registry
freshness ingestion = `saas`. Model names stable across Odoo 17/18/19/20;
no version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-001 | shared | — (config data §4) | l10n_gt.form.registry seed | 4-table mirror, row counts 82/24/54/9; as-of + provenance on every row; SAT-published-not-exhaustive qualifier |
| FR-002 | shared | — (config data §4) | l10n_gt.form.channel.def | Definitions verbatim; DG own-channel reading rule; [sic] spellings preserved |
| FR-003 | shared | — (config data §4) | l10n_gt.form.isr.spine | R46 binding identity set; wrong-map validation guard (grep-able) |
| FR-004 | shared | — (config data §4) | registry rows 1311/1321/1331/1341/1352 | DG-only channel flags; R46 |
| FR-005 | shared | — (config data §4) | registry rows 1361/1371/1411/1431/1608 | DG-only; R46 descriptions verbatim |
| FR-006 | shared | — (config data §4) | registry rows 2237/2046/2241 | Validity rows via FR-014; statutory regime = GT-TAX-FR-046..068 cross-ref |
| FR-007 | shared | — (config data §4) | registry rows 1901/1481/1911/1921/1219 (+1078/1088 sup.) | App surface RETENISR; payroll cross-ref; R46 |
| FR-008 | shared | — (config data §4) | channel row-data findings | DG-only declaration set; 27 paper-only codes; web survivors 511/8209; dual 2000/8008 |
| FR-009 | odoo | filing-surface routing config + account.move (declaration skeletons) | surface per obligation | Declarations → Declaraguate; paper-only → paper workflow; app forms → app surface; legacy channels never routed |
| FR-010 | shared | — (config data §4) | channel.def legacy flags | Light = 0 vigente rows; no-vigente Light code list carried; GOQ-94 qualifier |
| FR-011 | shared | — (config data §4) | app_surface on Anexo rows | 24 Anexo forms; RetWeb 2340/2320/2229 identities; Task 2 owns mechanics |
| FR-012 | shared | — (config data §4) | version_key tuple | Same-code/channel-split rows stored unmerged; GOQ-93 flag |
| FR-013 | shared | — (config data §4) | 1111 dual rows | Current = PLANILLA IVA-FEL app; payroll GT-PAY-FR-213..218 + GT-PAY-FR-221 own mechanics/guard; bare-1111→paper refused |
| FR-014 | shared | — (config data §4) | l10n_gt.form.validity | 18 dated rows; [sic] strings in provenance; as-of qualifier; D15/D16 |
| FR-015 | shared | — (config data §4) | l10n_gt.form.version.selection | R53 both-windows overlap flag; predecessor selection by período; non-transmittable historical class |
| FR-016 | odoo | devolución workflow config (paper) | 2053→2062 (Banco de Guatemala)→2073; 2124 | Paper-only routing; 2052/2123 blocked; electronic successors = Task 5 |
| FR-017 | shared | — (config data §4) | outside.catalog markers | R58 negative FR; GOQ-92 enumeration open; GT-TAX-FR-180 cross-ref for LAT dividendos |
| FR-018 | shared | — (config data §4) | negative finding rows | GOQ-95; "not in catalog" resolution; never synthesise a maquila/ISA family |
| FR-019 | shared | — (config data §4) | 7061/7101 no-vigente rows | Printed LB D-37-92; pre-LAT only; GT-TAX-FR-180 owns current regime |
| FR-020 | shared | — (config data §4) | libros/protocolos echo rows | 7121/7130 (≥2015-08-25)/7190/8490; ledger flow = Task 4 |
| FR-021 | shared | — (config data §4) | agro + EXENIVA rows | 2280/2290 DG; 351 paper/2093/2118 app; 2320 via FR-011 |
| FR-022 | shared | — (config data §4) | as-of qualifier on all rows | GOQ-94; absence ≠ nonexistence presentation guard |
| FR-023 | saas | registry freshness ingestion service | vintage rows + diff | New dated vintage per re-capture; no silent edits; effective-vintage reads |
| FR-024 | shared | — (ingestion contract §4) | filing.calendar.external | External data only (JSF transcription / accountant; atlas.com.gt cross-check); never invented; GOQ-14 |
| FR-025 | shared | — (config data §4) | family.echo rows (customs + specific) | Existence capture; codes/channels/superseded kin only; DUCA out of scope |
| FR-026 | shared | — (config data §4) | family.echo rows (compliance/admin) | 811/821/891/860/8421/2000; cese 2175/2192 paper-only; FAD 02 oddity; no mechanics |

## 6. Acceptance Criteria

- **AC-001:** Given the registry seed, when counted per table, then it holds
  82 vigentes / 24 vigentes-anexo / 54 no-vigentes / 9 no-vigentes-anexo
  rows, each stamped as-of 2025-10-06 with Wayback provenance and the
  SAT-published-not-exhaustive qualifier. (FR-001, FR-022)
- **AC-002:** Given ISR identity lookups, then ISR retenciones resolves
  SAT-1331, ISR capital mensual SAT-1321, ISR anual lucrativas SAT-1411,
  asalariados/relación de dependencia anual SAT-1431, and SAT-1371
  resolves to no-residentes pago directo mensual; and a surface asserting
  the W4-era map (1371=anual / 1411=asalariados / 1321=retenciones) fails
  validation. (FR-003, FR-004, FR-005)
- **AC-003:** Given the channel matrix, then SAT-2237 reads
  declaraguate-only (papel/web/light unavailable); SAT-511 reads web+app;
  SAT-2124 reads paper-only; boleta SAT-2000 reads dual Web+DG; and the
  dash legend is carried so "–" never renders as unknown.
  (FR-002, FR-008, FR-026)
- **AC-004:** Given filing-surface routing, then a declaration obligation
  (e.g. SAT-2237) routes to Declaraguate, a paper-only admin form (e.g.
  SAT-2124) routes to the paper workflow, an app form (e.g. SAT-2340)
  routes to the RETENCIONES WEB surface, and no obligation ever routes to
  AsiseLight or AsiseWeb. (FR-009, FR-010, FR-011)
- **AC-005:** Given code 2302, then the registry resolves two versions
  (papel-vigente / web-no-vigente) and the operational surface is paper
  only; given code 1111, then the vigente instrument is the PLANILLA
  IVA-FEL app form (mechanics GT-PAY-FR-213..218; guard GT-PAY-FR-221) and
  bare-1111 never resolves to the paper planilla; the bare code alone is
  never a registry key. (FR-012, FR-013)
- **AC-006:** Given the validity ledger and a período de imposición of
  2013-09, then BOTH the successor window (2237/2046/2085, from 2013-09)
  and the predecessor window (2157/2238, until 2013-10) resolve as printed
  with an overlap flag (R53); given período 2011-11 (IVA, general+anexo),
  the resolved form is 2157; given 2012-05 ISR quarterly, 1025; given
  2013-03 no-resident retención, 1351 (window 2013-01–2013-04 only); given
  2011 ISR anual asalariados, 1179; all historical rows carry the
  non-transmittable class marker. (FR-014, FR-015)
- **AC-007:** Given a registry search for SAT-2390, then the catalog
  returns absent AND the outside-catalog marker family exists (electronic
  dev.CF forms, DUCA/SAT-2901, LAT dividendos successors of 7061/7101) so
  no surface presents absence as nonexistence. (FR-017)
- **AC-008:** Given a query for a maquila- or ISA-specific declaration
  family, then it resolves "not in catalog" (exportadores surface = the
  paper dev.CF trio only; ISO = 1608/1609), and the registry synthesises
  no such family. (FR-016, FR-018)
- **AC-009:** Given SAT-7061/7101, then they resolve as no-vigente with
  printed legal basis Decreto 37-92 (pre-LAT) and a pointer to the current
  dividendos regime GT-TAX-FR-180. (FR-019)
- **AC-010:** Given a registry re-capture, then it lands as a new dated
  vintage with a diff (added/retired/channel/validity changes) and live
  rows are never silently edited; routing reads the vintage effective for
  the período being filed. (FR-023)
- **AC-011:** Given the calendario perpetuo ingestion surface with no
  ingested vintage for a period type, then no vencimiento/deadline object
  is generated and the gap is flagged; given ingested windows, every row
  carries JSF-transcription provenance with atlas.com.gt cross-check noted
  and nothing else. (FR-024)
- **AC-012:** Given the family-echo rows, then the customs codes
  (8560/8008/8530/8540/8028, superseded 8005/8021/2291), specific-tax
  families (petróleo/IUSI/cemento/señales/tabaco/bebidas/vehículos) and
  compliance/admin codes (811/821/891/860/8421/2000; cese 2175/2192
  paper-only; FAD 02 deprecated) are present with codes, channels and
  superseded kin — and no field-level mechanics derive from this file.
  (FR-025, FR-026)
- **AC-013:** Given the exportadores workflow, then routing sequences
  2053 → 2062 (ante el Banco de Guatemala) → 2073 on the paper channel
  with 2124 available for general devolución, and the superseded 2052/2123
  are never routable. (FR-016)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text verbatim from the register (abbreviated where noted). All
rows Status open; GOQs are trace-pending, not blockers. This file owns
GOQ-92/93/94/95 and the GOQ-14 calendar-ingestion surface; nothing outside
this register is treated as an open question.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-92: "Electronic devolución-CF forms itemization (nav chrome names the family; 48_ tables carry only paper 2124/2053/2062/2073) + DUCA/SAT-2901 customs forms + LAT dividendos successors of 7061/7101 — all live outside the 4-table catalog; enumerate from portal." Affects FR-017 (outside-catalog markers exist; enumeration pending — Task 5 owns SAT-2390). | no | GT synthesis wave S-GT4 → Task 5 file + portal enumeration (acquisition queue) | open |
| OQ-002 | GOQ-93: "Same-code/channel-split rows (1219 both tables; 2302 papel-vigente/web-no-vigente; 1111 app/paper; 511 main+anexo) — registry versioning semantics unexplained; model needs version-dimension." Modelled in FR-012/FR-013 as unmerged version rows keyed (code, table, channel); SAT-side semantics unexplained. | no | GT synthesis wave S-GT4 | open |
| OQ-003 | GOQ-94: "As-of stamping: 48_ = Wayback 2025-10-06 (no dateModified; channel definitions BancaSAT-era); 49_/50_ © 2025 only … — treat channel model as SAT-published, not exhaustive." Affects FR-001/FR-010/FR-022/FR-023 (as-of qualifiers, legacy-channel guard, vintage refresh). | no | GT synthesis wave S-GT4 → registry freshness ingestion (saas) + re-capture queue | open |
| OQ-004 | GOQ-95: "Negative finding: NO maquila/ISA-specific declaration family in 48_ (exportadores surface only via dev.CF trio; ISO 1608/1609 only solidarity form)." Encoded as negative FR-018; revisit only if a special-regimes wave (S-GT6/S-GT7) surfaces a dedicated family elsewhere. | no | GT synthesis wave S-GT4 (register to S-GT6/S-GT7 expectations) | open |
| OQ-005 | GOQ-14: "Accountant asks pending: calendario perpetuo vencimiento windows per NIT last-digit (JSF transcription, owner browser; atlas.com.gt cross-check only)…" Ingestion surface FR-024; window VALUES are external data — never invented; back-fill on acquisition (HANDOVER §8 plan B). | no | GT synthesis wave S-GT4 → accountant track / owner-browser JSF transcription (W6) | open |
