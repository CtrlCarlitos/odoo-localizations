# GT — Fiscal reporting — Retenciones Web operating system (IVA + ISR) & agent population

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala
**Retenciones Web** (Retention Web system) OPERATIONAL surfaces — cluster F2:
the two SAT portal regimes (IVA variant 49_, ISR variant 50_), the ISR user
manual (51_, printed "noviembre 2024" — never "v3"), the IVA sector-público
manual (52_, undated), the official IVA-agent roster (53_, as-of 2025-10-01)
and the voluntary-inscription form SAT-0261 (54_). It carries: the portal
access model (login paths, SAT activation, RetenIVA sunset 31/07/2021); the
two IVA declaration surfaces **SAT-2340** (General + Pequeño Contribuyente,
first 15 días hábiles) vs **SAT-2320** (agropecuario, first 10 días hábiles —
R47 guard), both paid via boleta SAT 2000; the rate-matrix PRESENTATION
layer that renders the taxation rate catalog without ever re-deriving a
statutory value (IVA matrix incl. dualidad combos, PC 5% ≥ Q2,500.01, agro
5% total factura, sector público 25/5/5, card-fuel 1.5%); the "art. 54 B"
[sic] statutory-agent path; the ISR operating system (FEL-fed with 2022
phased onboarding, FEL legend routing, 10-días-hábiles declare-and-enter,
constancia dated = factura date, 5-días delivery as printed, DJ = SAT-1331 +
boleta SAT 2000, rectificación congelado + multa); the ~30-concepto ISR
retention catalog as a config surface; constancia machinery (prenumerada,
state machine impresa/asignada/pagada/anulada, per-contribuyente
consolidation, ZIP/PDF/Excel export); the LAT art. 48 and art. 15 declaration
anexos; and the carga-masiva engines (ISR 7/8-column CSV with the RECIBO
convention under CTI 03-2023; IVA 7-column paper path incl. monto agrícola
and monto exento; batch states + reversión; the neto/afecto/retención line
model with agent-vs-agent/minimums/exempt validations and Banguat FX at the
fecha de certificación).

This file is the OPERATIONAL half of a two-layer contract: every statutory
rate, threshold and deadline is owned by the S-GT2 taxation files
(`gt/requirements/taxation/03_iva-retenciones.md` GT-TAX-FR-069..110,
`gt/requirements/taxation/05_isr-lucrativas-capital.md`,
`gt/requirements/taxation/04_isr-trabajo.md` GT-TAX-FR-142) and their CSV
sidecars (`iva_retention_rates.csv`, `isr_rates.csv`) — consumed here by
exact FR id / CSV row, never re-derived, never frozen. Form REGISTRY
identities (2340/2320/2229/1331/2000/0261) are owned by Task 1
(`01_form-inventory-channels.md`, GT-FIN-FR-001..026) — cross-referenced,
never restated as registry rows.

It does **not** cover: the statutory retention regime itself (rates, bases,
de-minimis, dualidad, neutrality, seller-side netting — taxation/03, all
GT-TAX-FR ids); the ISR statutory deadlines and their "días"/"días hábiles"
qualifiers (taxation/04 GT-TAX-FR-142 owns the qualifier registry;
taxation/05 GT-TAX-FR-163/182/185/188/189 own the 10-day/5-day statutory
cycles); the form catalog and channel model (Task 1); the FEL DTE
emission/validation stack and the anulación blocker mechanics (e-invoicing
wave — GT-EINV-FR-210 is cited outcome-only); the RETENISR payroll outputs
and the Planilla IVA-FEL (`gt/requirements/payroll/09_isr-iva-interfaces.md`
GT-PAY-FR-213..222, cross-referenced by exact id); and sanctions/procedures
(taxation/06).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble — fiscal
reporting): **manuals and portal pages are PRIMARY for declaration
MECHANICS, SECONDARY for statutory parameters** — every rate/threshold/
deadline a manual or portal prints is a RESTATEMENT; statutory instruments
outrank them and live in the S-GT2 taxation files, consumed here by exact
FR id. Regime citations as printed by the sources themselves: 49_ cites
**D-20-2006 + AG 425-2006 + Ley del IVA (D-27-92)**; 50_/51_ cite
**D-10-2012 (LAT)**; 51_ additionally quotes **LAT arts. 48 and 15** verbatim
(the two anexo field sets) and **CTI 03-2023** for the carga-masiva utility
case; 52_ cites **D-27-92 "artículo 54 B" [sic — presumably 54 BIS, R59]**
for the statutory-agent population; 54_ cites **D-20-2006 art. 6**.
**R46 (binding): form numbers (SAT-2340/2320/2229/1331/2000/0261) are
RetWeb-layer prints — they NEVER cite D-20-2006/AG 425-2006, which print
none.** R47: the SAT-2320 10-día variant is a RetWeb-layer print whose
instrument is NOT in corpus — GOQ-01-context note, never frozen. Dated rows
follow D15/D16 (cite together): every deadline/rate row below carries
provenance + as-of qualifier (49_ content ≥ 2025-06-01; 50_ © 2025 only;
51_ nov-2024; 52_ portal-listed 2024-11-29, itself undated; 53_ as-of
2025-10-01). Source-file convention: 49_/50_ are HTML snapshots read through
their committed text layers (`gt/.extractions/49_…txt`, `50_…txt`); 51_/52_
are PDFs read through `.pdf.txt` layers (extraction spacing defects — e.g.
"noviembre2024" — are quoted as-is by the evidence file with `[sic]`; never
corrected). All quotes below verified verbatim against
`gt/.extractions/49-54_RetWeb_agentes.evidence.md` (EVID-386..417).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 49_/50_ portal identities: "Portal SAT \| Sistema Retenciones Web -IVA- Guatemala" / "Bienvenido al Sistema de Retenciones del IVA (Retenciones Web) de la Superintendencia de Administración Tributaria." / "Listado Agentes de Retención al 01/06/2025" / "© Superintendencia de Administración Tributaria 2025. Todos los Derechos Reservados." — 50_: "Portal SAT \| Sistema Retenciones Web -ISR- - Guatemala" / "Retenciones ISR con como insumo principal [sic]" / same © 2025 footer | Two sibling SAT portal regime pages (IVA and ISR variants of Retenciones Web). Only internal dating: © 2025 (both) + the 01/06/2025 roster link (49_, anchors its content to ≥ 01-Jun-2025); 50_ has no internal date anchor (GOQ-94 kin currency) | `gt/.extractions/49_SAT_RetWebIVA_page.txt`; `gt/.extractions/50_SAT_RetWebISR_page.txt` | 49_ p.1 lines 1, 17-18, 51, 71; 50_ p.1 lines 1, 17, 19, 71 (EVID-386) |
| LB-002 | 49_: "Es el Sistema que tienen a disposición todas las personas individuales o jurídicas designadas por la Ley y activadas por la Superintendencia de Administración Tributaria, para retener parte del Impuesto al Valor Agregado…, quienes actuarán como Agentes de Retención del IVA, conforme a lo establecido en el Decreto Número 20-2006…; su \"Reglamento\" Acuerdo Gubernativo Número 425-2006 y lo establecido en la Ley del Impuesto al Valor Agregado." / "Para poder tener acceso a este sistema, el contribuyente debe estar calificado y activado por la Superintendencia de Administración Tributaria, como Agente Retenedor del IVA y los designados por ley específica." | Regime ground truth as the page cites it: D-20-2006 + AG 425-2006 + Ley del IVA; agent status = designated by law AND activated by SAT (calificación + activación); access requires that status; two populations: SAT-activated agentes retenedores + "los designados por ley específica" | `gt/.extractions/49_SAT_RetWebIVA_page.txt` | 49_ p.1 lines 19-22 (EVID-387) |
| LB-003 | 49_: "Generar la Declaración Jurada de Retenciones del IVA con la totalidad del impuesto retenido, dentro de los primeros (15) días hábiles del mes inmediato siguiente, a aquel en el que se realice la retención." / "Entregar la constancia de retención prenumerada y autorizada por cada operación sujeta a retención (se emite cuando el vendedor del bien o prestador de servicios hace entrega de la factura)." / "Estar al día en el cumplimiento de sus obligaciones tributarias." | Agent duties as the portal prints them: monthly DJ with the totality of retained tax within the first 15 días hábiles of the following month; prenumerada y autorizada constancia PER retention-triggering operation, issued at invoice delivery; stay current | `gt/.extractions/49_SAT_RetWebIVA_page.txt` | 49_ p.1 lines 23-27 (EVID-388) |
| LB-004 | 49_: "El pago del impuesto por retenciones del IVA realizadas a facturas que correspondan al Régimen General y Pequeño Contribuyente, se deberá presentar por medio del formulario SAT-2340 Declaración Jurada de Retenciones del IVA de Declaraguate, el cual se pagará con la boleta SAT 2000 en cualquier banco del sistema o por Bancasat dentro de los primeros quince (15) días hábiles del mes inmediato siguiente en el que se realice la retención." / "…al Régimen Especial de Contribuyente Agropecuario, se deberá presentar por medio del formulario SAT-2320 Declaración Jurada IVA Retenciones Agropecuario de Declaraguate, el cual se pagará con la boleta SAT 2000 en cualquier banco del sistema o por Bancasat dentro de los primeros diez (10) días hábiles del mes inmediato siguiente en el que se realice la retención." | TWO IVA retention forms by provider regime: SAT-2340 (General + Pequeño; 15 días hábiles) and SAT-2320 (agropecuario; 10 días hábiles), both paid via boleta SAT 2000 (any bank or Bancasat), both via Declaraguate — the 10-day variant is a RetWeb-layer print whose instrument is NOT in corpus (R47; statutory = 15 días hábiles uniformly, GT-TAX-FR-106) | `gt/.extractions/49_SAT_RetWebIVA_page.txt` | 49_ p.1 lines 30-32 (EVID-389) |
| LB-005 | 49_ rate list: "Contribuyentes Especiales y Otros agentes de retención: 15%" / "Exportador (Decreto 29-89): 65%" / "Exportador (Decreto 29-89) con Dualidad: 15%, 65%" / "Exportador Habitual: 15%, 65%" / "Exportador Habitual con Dualidad: 15%, 15%, 65%" / "Sector Público: 25%" / "Operadora de Tarjetas de Crédito o Débito: 15%, 1.5%" | Portal rate matrix by agent type incl. the dualidad multi-rate prints (regimes unnamed on the page for the three-rate Habitual-con-Dualidad case); Sector Público 25%; card operators 15% + 1.5% — SECONDARY prints restating the statutory matrix (render layer only; GT-TAX-FR-070..079 + CSV rows) | `gt/.extractions/49_SAT_RetWebIVA_page.txt` | 49_ p.1 lines 33-40 (EVID-390; cross-check EVID-417) |
| LB-006 | 49_: "La retención para facturas del Régimen de Pequeño Contribuyente será del (5%) y el monto debe ser mayor o igual a dos mil quinientos quetzales con un centavo (Q 2,500.01)." / "Los Agentes de Retención no practicarán la retención que corresponda, cuando les presten servicios o hagan compras menores a dos mil quinientos quetzales (Q2,500.00), con excepción del Sector Público, las Operadoras de Tarjeta de Crédito o Débito y adquisición de combustibles pagada con tarjeta de crédito o débito." / "La retención para facturas del Régimen Especial de Contribuyente Agropecuario será del (5%). Para efectuar retenciones a este régimen el Agente de Retención deberá ingresar a su Agencia Virtual y realizarla en el sistema Retenciones Web." / "La retención será aplicada al monto total de la factura." | PC-provider 5% when monto ≥ Q2,500.01; Q2,500.00 de minimis excepting sector público, card operators and card-paid fuel; agro providers 5% processed in Retenciones Web (Agencia Virtual) applied to the total factura — all SECONDARY prints (R55/GOQ-06; CSV rows secondary-print-pending, never frozen) | `gt/.extractions/49_SAT_RetWebIVA_page.txt` | 49_ p.1 lines 41-48 (EVID-391) |
| LB-007 | 49_ manual roster: "Manual de usuario Delegación de Permisos - Sistema Retenciones Web -IVA- … 20-11-2024" / "…Exportadores Habituales … 14-11-2024" / "…Exportadores Decreto No. 29-89, Especiales y Otros Agentes de Retención … 14-11-2024" / "…Tesorería Nacional … 31-01-2025" / "…Usuarios Manuales … 29-11-2024" / "…Fondos Rotativos … 29-11-2024" / "…Unidades Ejecutoras … 29-11-2024" / "Formato carga de facturas en papel - con explicación … xlsx" / "Formato carga de facturas FEL (Terceros) -con explicación … xlsx" / "Instalación del Sistema RetenIVA (vigente hasta el 31/07/2021) podrá realizar consultas de las operaciones realizadas de la fecha indicada hacia años anteriores." / "RetenIVA 0.0.20" | Seven role-specific IVA manuals exist (only 52_ = usuarios manuales is in corpus — GOQ-96); two official xlsx carga-masiva templates (papel, FEL-Terceros); legacy desktop RetenIVA retired 31/07/2021 (v0.0.20 remains for historical queries only) | `gt/.extractions/49_SAT_RetWebIVA_page.txt` | 49_ p.1 lines 49-67 (EVID-392) |
| LB-008 | 50_: "El sistema está desarrollado a partir del insumo principal de Factura Electrónica en Línea -FEL-, de esta forma el agente de retención del ISR tiene a disposición las facturas electrónicas para practicar la retención desde el momento en que el proveedor las haya emitido, el mismo cuenta con la opción de carga masiva de los documentos tributarios en papel, conforme a lo establecido en el Decreto Número 10-2012, Ley de Actualización Tributaria." / "Contribuyentes Especiales Grandes deben incorporarse a partir del 1 de enero de 2022." / "…Especiales Medianos… 1 de febrero de 2022." / "Contribuyentes Normales… 1 de marzo de 2022." / "Sector Público… 1 de abril de 2022." / "…Especiales Regionales… 1 de mayo de 2022." | ISR system is FEL-fed: received e-invoices available to the agent from emission; paper documents enter via carga masiva; legal basis as cited by the page: D-10-2012 (LAT); mandatory onboarding phased Jan-May 2022 by taxpayer class (dated milestones) | `gt/.extractions/50_SAT_RetWebISR_page.txt` | 50_ p.1 lines 20-29 (EVID-393) |
| LB-009 | 50_: "Si el contribuyente es calificado como Agente de Retención del IVA puede ingresar con RNIT y la clave que utiliza para ingresar al Sistema Retenciones WEB, donde tendrá la opción de realizar retenciones del ISR y del IVA, respectivamente." / "Si es contribuyente normal, debe ingresar desde su Agencia Virtual>> Servicios>> Retenciones Web>> donde encuentra las opciones para realizar la generación de las constancias de retención del ISR." | Single credential plane: IVA-qualified agents use their RNIT Retenciones Web credentials for BOTH IVA and ISR; normal taxpayers enter via Agencia Virtual → Servicios → Retenciones Web (ISR constancia generation only) | `gt/.extractions/50_SAT_RetWebISR_page.txt` | 50_ p.1 lines 30-32 (EVID-394) |
| LB-010 | 50_: "Generar la Declaración Jurada del ISR con la totalidad del impuesto retenido, y enterarlo dentro del plazo de los primeros (10) días hábiles del mes siguiente a aquel en que se emitió la constancia de retención." / "Emitir la constancia de retención respectiva con la fecha de la factura." / "Entregar al contribuyente la constancia de retención dentro de los primeros (5) días del mes inmediato siguiente." / "¿Qué rentas puedo declarar en el Sistema Retenciones WEB para el ISR? Actividades Lucrativas / Rentas de Capital / Facturas Especiales" / (delegation:) "El titular puede delegar permisos a sus colaboradores para que realicen gestiones dentro del sistema… (Otras Rentas)." | ISR agent duties as printed: declare AND enter within the first 10 días hábiles of the month following constancia emission; constancia dated with the factura's date; delivery within the first (5) días — as printed, WITHOUT "hábiles" (R54/GOQ-99 mechanics half, transcribed exactly); declarable rentas = lucrativas / capital / facturas especiales; delegation supported | `gt/.extractions/50_SAT_RetWebISR_page.txt` | 50_ p.1 lines 33-42 (EVID-395) |
| LB-011 | 51_ cover/índice: "Guatemala, noviembre2024 [sic]" / "Manual de usuario Sistema Retenciones WEB-ISR" / "El presente manual de usuario es para dar soporte a los agentes de retención del Impuesto Sobre la Renta, según lo establecido en el Decreto Número 10-2012…, Ley de Actualización Tributaria." / índice: MENÚ DE INGRESO / CATEGORÍA DE RENTA / EMISIÓN CONSTANCIAS DE RETENCIÓN / CONSULTACONSTANCIAS [sic] DE RETENCIÓN / DECLARACIÓN JURADA / CONSULTADECLARACIÓN [sic] JURADA / CARGA MASIVA / "Ingresa desde el Portal SAT en Agencia Virtual." / "Si eres Agente de Retención del IVA, ingresa con el mismo usuario asignado -RNIT-." | SAT procedural manual for ISR agents under D-10-2012, dated noviembre 2024 (twice); the label's "v3" is NOT printed (GOQ-96); workflow skeleton: categoría de renta → emisión constancias → consulta → DJ → consulta DJ → carga masiva | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via `gt/.extractions/51_SAT_RetWebISR_Manual_v3.pdf.txt`) | 51_ pp.1-2 (EVID-396) |
| LB-012 | 51_ §2.1-2.2: "El sistema despliega los campos que deberá completar para realizar la búsqueda de Facturas Electrónicas recibidas, con estado vigente." (params "Período del / Período al / NIT Retenido… / Estado de Asignación… Todos / Sin Asignar / Asignados") / "Todas las facturas Electrónicas que contengan la leyenda Sujeto a retención definitiva se visualizarán automáticamente para la asignación de la Categoría de Renta, no obstante, aquellas que contengan la leyenda Sujeto a pagos trimestrales ISR y deban efectuarse la retención por Rentas de Capital, se utilizará la opción de Procesar FEL…" (manual entry: "1. Nit Emisor… / 2. Serie Dte… / 3. Número Dte… / 4. Clic Procesar FEL") / "Nota: es importante que previo a realizar el proceso del documento deberá verificar que no exista constancia de retención de IVA e ISR emitidas las cuales deberán ser anuladas." | FEL retention legends drive the feed: "Sujeto a retención definitiva" → auto-surfaced; "Sujeto a pagos trimestrales ISR" → rentas-de-capital path via manual Procesar FEL (NIT emisor + serie DTE + número DTE); cross-constancia guard: one document cannot carry two live IVA-and-ISR constancias (anular first) | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ pp.5-6 §2.1-2.2 (EVID-397) |
| LB-013 | 51_ p.9 §2.4 category/concept table: Category 1 "RÉGIMEN OPCIONAL SIMPLIFICADO SOBRE INGRESOS": "Renta Imponiblede [sic] Q0.01 a Q30,000.00 5% / Renta Imponiblede [sic] Q30,000.01 en adelante 7% + excedente de Q1,500.00" + conceptos 1-20 (Compras o Servicios Gravados de Entidades Exentas; Materias Primas; Productos Terminados; Transporte; Telecomunicaciones; Servicios Bancarios,Seguros [sic] y Financieros; Servicios Informáticos; Energía y Agua; Servicios Técnicos; Arrendamiento Bienes Muebles; Arrendamiento Bienes Inmuebles; Servicios Profesionales; Dietas a asistentes eventuales; Espectáculos; SubsidiosPúblicos [sic]; SubsidiosPrivados [sic]; Otros Bienes y/o Servicios; Películas Cinematográficas,TV [sic]; Dietas; Otras Remuneraciones) / Category 2 "RENTAS DE CAPITAL INMOBILIARIO": "Total, de factura dividido 1.12, se resta el 30% del gasto y se aplica el 10%" (conceptos 1-2: Arrendamiento y Subarrendamientos de Bienes Inmuebles; ConstituciónCesión [sic] de Derechos…) / Category 3 "RENTAS DE CAPITAL MOBILIARIO": "Base Imponible por el 10%" (conceptos 1-7) / "Base imponible por el 5% 8 Distribuciónde [sic] dividendos,ganancias [sic] y utilidades" | The SAT-side ISR retention taxonomy: 3 categories, ~30 conceptos, with embedded rate/base logic — Opcional 5% to Q30,000 / "7% + excedente de Q1,500.00" above (terse print); Inmobiliario (total ÷ 1.12 − 30% del gasto) × 10%; Mobiliario × 10% except dividendos (concepto 8) 5%; concept numbers = the carga-masiva codes. RATES ARE STATUTORY (LAT arts. 44/88/92/93) — rendered from `isr_rates.csv`, never re-derived here | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ p.9 §2.4 (EVID-398) |
| LB-014 | 51_ §3.1-3.3 emission params: "1. Emisión del: … 2. Emisión al: … 3. Retenciones que declara: ISR / 4. Retención a Declarar: Opcional Simplificado Sobre Ingresos / Rentas de Capital Inmobiliario / Rentas de Capital Mobiliario / Facturas Especiales / 5. Tipo Documento: FEL / Papel" / keys "6. NIT Retenido / 7. Número de Autorización FEL / 8. Serie de Factura / 9. Número de Factura / 10. Buscar" / "…selecciona Habilitar generación de Constancia y la factura a la que le emitirás la constancia de retención. Finalmente, clic en Generar retención. El sistema desplegará el detalle de la constancia generada, presiona el número de la constancia y esta se descargará en formato PDF." / "3.3 Emisión de Constancias de Retención Masiva: Selecciona las facturas a las cuales le emitirá la constancia de retención y presiona Generar Retención." | Constancia emission = search (period, retention category incl. Facturas Especiales, doc type FEL/Papel, optional NIT/autorización/serie/número) → select → Generar Retención (individual or masiva); constancia identified by número de constancia, downloaded as PDF | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ pp.10-12 §3.1-3.3 (EVID-399) |
| LB-015 | 51_ §4.1-4.3: "4. Estado: Todos / Impresa / Anulada / Impresa / Asignada / Impresa / Pagada" / "5. Retenciones que Declara: Opcional Simplificado Sobre Ingresos / Rentas de Capital Inmobiliario / Rentas de Capital Mobiliario / 6. Tipo Descarga Excel: Detallado" / "El sistema enviará una notificación a través del correo electrónico que se encuentre registrado en el Registro Tributario Unificado del Agente de Retención, en la que podrás realizar la descarga del Archivo ZIP, PDF o Excel." / "Anular: desde esta opción de Consulta de Constancias de Retención puedes anular las constancias seleccionadas, al confirmar la operación, puedes dirigirte a las opciones de Categoría de Renta o Emisión Constancias de Retención para realizar el proceso nuevamente." | Constancia state machine: Impresa → (Impresa/Asignada) → Impresa/Pagada, or Anulada (anulación re-opens categorización + emisión); batch export ZIP/PDF/Excel ("Detallado") delivered by email to the RTU-registered address | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ pp.13-15 §4.1-4.3 (EVID-400) |
| LB-016 | 51_ §4.4: "En cumplimiento a lo establecido en el Artículo 48 del Decreto Número 10-2012…, prescribe que debe acompañarse un anexo a la Declaración Jurada que indique los nombres y apellidos completos de cada uno de los contribuyentes residentes en el país o con establecimiento permanente, Número de Identificación Tributaria, el valor de lo efectivamente acreditado o pagado y el monto de la retención. Por lo anterior, en el menú Consulta de Declaración Jurada, al consultar la Declaración Jurada, podrás visualizar en la opción Ver detalle dicho anexo." | LAT art. 48 anexo (page's own citation): per-retained-taxpayer record {nombre y apellidos completos, NIT, valor efectivamente acreditado o pagado, monto de la retención} attached to the DJ; visible as "Ver detalle" — the minimum field set any retention-ledger export must carry | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ p.16 §4.4 (EVID-401) |
| LB-017 | 51_ §5.2-5.4, §6.1-6.2: "Se muestra el formulario SAT – 1331, si los datos consignados son correctos puede imprimir la Boleta SAT 2000 y presentarla en cualquier banco del sistema." / "5.3 Rectificación… aplicable a un formulario en estado pagado, cuando se realizan los siguientes cambios: Creación de nuevas constancias… / Anulación de constancias de retención…" / "Si rectificas una Declaración Jurada, el sistema generará un nuevo formulario SAT – 1331 en estado congelado con la multa por rectificación incluida." / "5.4 Liberar DeclaraciónJurada [sic]: Permite liberar la Declaración Jurada o la rectificación generada, cuando no se realizó ninguna modificación a constancias de retención…" / "Estado: Pendiente de pago / Pagada" / "Al realizar el pago de la Declaración Jurada, puede demorar algunos minutos en actualizar el estado de las constancias… cambiará el estado de la constancia de retención de Impresa/asignada a Impresa/pagada." / "Lo anterior permitirá que el sujeto de retención pueda consultar y visualizar sus constancias de retención recibidas desde su agencia virtual." | ISR declaration = SAT-1331 (R46) paid via boleta SAT 2000; rectification only from estado pagado (constancia create/annul) → new SAT-1331 estado congelado with multa por rectificación incluida; Liberar frees an unmodified frozen DJ; payment flips constancias to Impresa/pagada; the retained party then sees received constancias in their own Agencia Virtual | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ pp.17-22 §5.2-5.4, §6.1-6.2 (EVID-402) |
| LB-018 | 51_ §6.3: "En el Artículo 15 del Decreto Número 10-2012 … prescribe que debe acompañar a la Declaración Jurada, un anexo en el cual se especifique el nombre y apellido completos, domicilio fiscal y Número de Identificación Tributaria o número de identificación personal de cada una de las personas a las que le emitió la factura especial, el concepto de la misma, la renta acreditada o pagada y el monto de la retención, la cual se encuentra en el detalle de la Declaración Jurada, Detalle de Facturas Especiales." | Second anexo (facturas especiales, LAT art. 15 as cited): per-issued-special-invoice record {nombre y apellido completos, domicilio fiscal, NIT o número de identificación personal, concepto, renta acreditada o pagada, monto de la retención} | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ p.22 §6.3 (EVID-403) |
| LB-019 | 51_ §7.1-7.1.1: "La carga masiva se utiliza para la emisión de constancias de retención, en aquellos casos en los que las rentas no están respaldadas por facturas, como es el caso de los pagos por concepto de dietas o dividendos. Además, este proceso se aplica para realizar la carga de facturas electrónicas por servicios tales como: energía eléctrica, agua potable y teléfono de línea fija, emitidas a nombre y NIT de los arrendantes y no de los arrendatarios, cuando existe un contrato de arrendamiento previo. Este procedimiento se encuentra regulado por el Criterio Tributario Institucional Número 03-2023." / columns "NIT Proveedor \| Categoría de Renta \| Concepto de Renta \| Serie Documento \| Número Documento \| Fecha Documento \| Total Documento" / formats "GENERAL … FECHA … NÚMERO (2 decimales)" / "NIT del proveedor sin guión" / serie/número: "Colocar la palabra RECIBO o dejar la casilla en blanco" / total: "Monto total para Rentas de Capital Ingrese Renta Imponible" / examples: "237484379 1 19 RECIBO 100 03/09/2023 8000.00" / dividendos (extra column "Período de dividendos que declara"): "28619293 3 8 15/09/2023 5000.00 2023" | ISR carga masiva use cases: non-invoice-backed rents (dietas, dividendos — RECIBO convention) and arrendador-billed utility FELs under CTI 03-2023; file = 7 columns (8 for dividendos with período), NIT sin guión, 2-decimal amounts, renta-imponible override for capital categories | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ p.23 §7.1-7.1.1 (EVID-404) |
| LB-020 | 51_ §7.3-7.4: "2. Tipo Archivo: Papel / FEL (Terceros) / 3. Subir Archivo: selecciona Archivo Excel .csv (Delimitado por comas)." / FEL (Terceros) fields: "a. NIT retenido: NIT del emisor de la Factura Electrónica en Línea (sin guiones). b. Serie: serie de la FEL. c. Número de factura: número de la FEL." / "las facturas cargadas por la opción FEL (Terceros) se visualizarán en la pantalla de Categoría de Renta, el usuario le asigna categoría y concepto, continúa con el proceso de emisión de constancia de retención." / results "cantidad de documentos procesados (registros exitosos) y documentos no procesados (registros con errores)" / estados: "Todos / Revertidos / Error en reversión / Procesado / En Cola / En Cola Reversión / Error de Procesamiento" / "2. Anular: … revertir al archivo cargado previamente… se reflejará la anulación en Estado Carga Revertido y recibirás la notificación al correo electrónico registrado en el Registro TributarioUnificado [sic] Digital." | Upload contract: CSV comma-delimited; two templates — Papel (full 7-col) and FEL-Terceros (3-col pointer, categorized in-system); async processing with 7 file states and one-shot batch-level reversión; results/errors notified by email to the RTU-Digital address | `gt/sources/51_SAT_RetWebISR_Manual_v3.pdf` (via txt) | 51_ pp.24-27 §7.3-7.4 (EVID-405) |
| LB-021 | 52_ cover/footer: "INTENDENCIA DE RECAUDACÓN [sic] …" / "SISTEMA RETENCIONES WEB UTILIZANDO FEL COMO INSUMO PRINCIPAL" / "Manual de Uso / Usuarios manuales / Sector público (Entidades centralizadas y descentralizadas)" / footer "…Página N de 15" | Identity of 52_: the portal's "Usuarios Manuales" IVA manual (49_ listing, added 29-11-2024) whose audience is Sector Público manual users (centralized + decentralized State entities); NO date string printed anywhere (GOQ-96 kin) | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via `gt/.extractions/52_SAT_RetWebIVA_Manual_2024.pdf.txt`) | 52_ pp.1-2 (EVID-406) |
| LB-022 | 52_ p.3 intro + rate table: "El presente manual es para uso de los usuarios manuales, se utilizan en el sistema de Retenciones Web únicamente para la generar [sic] constancias de retención que se asocian al usuario principal de la unidad compradora, estas emiten sus constancias de retención por medio de los sistemas de Contabilidad del Estado, reteniendo los porcentajes que se describe a continuación:" / table "Tipo de Agente de Retención: Sector Público — Porcentajes de retención aplicables según régimen de afiliación del IVA del proveedor sujeto de retención: General 25% / Pequeño Contribuyente 5% / Especial de Contribuyente Agropecuario 5%" | Manual users (State purchasing units) ONLY generate constancias in Retenciones Web; their declarations flow through the Sistemas de Contabilidad del Estado; Sector Público agent rates by provider IVA regime: General 25% / PC 5% / Agropecuario 5% — the 5/5 rows are SECONDARY prints (R55/GOQ-06; CSV rows secondary-print-pending) | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via txt) | 52_ p.3 intro + rate table (EVID-407) |
| LB-023 | 52_ §1: "Para ingresar, deberá utilizar el usuario que le ha sido proporcionado para el uso de la herramienta RetenIVA2, si es Agente Retenedor activo. Si no posee usuario debe ingresar con su NIT, esta opción aplica únicamente para los Agentes de Retención establecidos en el primer párrafo del artículo 54 B del Decreto Número 27-92 del Congreso de la República de Guatemala, Ley del Impuesto al Valor Agregado, que llevan contabilidad completa y no han sido calificados por la Administración Tributaria como Agentes de Retención, sin embargo, actúan como Agentes de Retención cuando paguen, acreditan en cuenta ingresos a contribuyentes inscritos en el Régimen Especial de Contribuyente Agropecuario." / "Si es Agente Retenedor deberá ingresar con la contraseña asignada por la Administración Tributaria." | Two IVA login populations: active agentes retenedores with RetenIVA2 credentials; and statutory agents under D-27-92 art. "54 B" [printed as such; presumably 54 BIS — equating them needs the post-2018 text, R59/GOQ-01 kin] first paragraph — full accounting, NOT SAT-qualified, retaining only when paying/accrediting Agropecuario-regime suppliers, logging in with plain NIT | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via txt) | 52_ pp.3-4 §1 (EVID-408) |
| LB-024 | 52_ §2: "La estructura del archivo debe contener los siguientes campos: a. NIT retenido… (sin guiones). b. Serie… c. Número de factura… d. Fecha de factura… en formato dd/mm/aaaa. e. Total factura… en formato general. f. Monto agrícola: monto del valor por bienes agrícolas o pecuarios en formato general (aplica para agentes de retención calificados como exportadores). g. Monto exento u otros impuestos: monto exento o impuestos específicos según corresponda, por ejemplo: timbre de prensa, impuesto a la distribución de petróleo, hospedaje, bomberos, etc. (formato general)" / "los valores que se informen en las columnas e, f y g, deben ir en formato general, no debe ir separado por comas." / "Previo a guardar el archivo deberá verificar en configuración regional… que el separador de listas se encuentre con coma (,)." / "El archivo debe guardarse en formato CSV (delimitado por comas). No debe contener encabezado." / samples "19 A 123 31/10/2022 40040 40040" / "19 A 125 31/10/2022 33019.96 [blank] 15000" | IVA paper-invoice carga masiva = 7 columns (NIT, serie, número, fecha dd/mm/aaaa, total, monto agrícola — exportador agents only, monto exento u otros impuestos — timbre de prensa, distribución de petróleo, hospedaje, bomberos…), CSV comma-delimited, NO header, no thousand separators | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via txt) | 52_ pp.6-7 §2 (EVID-409) |
| LB-025 | 52_ §3 detail + NOTA: "a) NIT… b) Nombre retenido… c) Número autorización… d) Serie… e) Número factura… f) Fecha factura… g) Total factura… h) Importe neto: monto total sin el Impuesto al Valor Agregado (aplica únicamente para régimen General), para el régimen Pequeño Contribuyente y Régimen Especial de Contribuyente Agropecuario es el mismo monto total. i) Afecto retención: es el monto sujeto a retención. Para el Régimen de Pequeño Contribuyente y Régimen Especial de Contribuyente Agropecuario, en la casilla afecto a retención mostrará el mismo valor que el de total factura, debido a que la factura no incluye Impuesto al Valor Agregado. j) Retención: valor de retención aplicado a la factura. k) Opciones: muestra la opción para el registro de los pagos de las compras o servicios realizados con tarjeta de crédito o débito." / "NOTA: el monto de retención se deriva de la aplicación del porcentaje según el tipo de Agente de Retención y el régimen del proveedor, así mismo se realiza la validación de retención entre agentes, montos mínimos, montos exentos o no afectos. Si la factura electrónica en línea fue emitida en moneda distinta a Quetzal (Q), el cálculo de la retención es a partir del monto en quetzales al tipo de cambio publicado por el Banco de Guatemala con base a la fecha de certificación de la factura." | The SAT-side IVA retention line model: NIT, nombre, número de autorización (FEL), serie, número, fecha, total, importe neto (= total ex-IVA, General only; PC/Agro = total), afecto retención (base — total factura for PC/Agro), retención, card-payment option; system validations: retención entre agentes, montos mínimos, exentos/no afectos; FX: non-Quetzal FEL → Banguat rate at the factura's fecha de certificación | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via txt) | 52_ pp.10-11 §3 + NOTA (EVID-410) |
| LB-026 | 52_ §3.1-3.1.2: "3.1 Registrar pago realizado con tarjeta de crédito o débito — La opción muestra como disponibles todas las facturas en pantalla que son sujetas a retención del IVA y permite registrar el monto parcial o total que fue pagado con tarjeta de crédito y/o débito." / "3.1.1 Pago Total — …al realizar este registro la factura ya no estará disponible en la opción de emisión de constancia de retención del Impuesto al Valor Agregado, por lo que deberá documentar la factura con el voucher de la operación realizada." / "3.1.2 Pago Parcial — …la factura estará disponible en la opción de emisión de constancia de retención del Impuesto al Valor Agregado, con el valor que no fue pagado con tarjeta, toda vez supere el monto mínimo para retener el Impuesto al Valor Agregado." | Card-payment exit from the retention base: Pago Total removes the invoice from constancia emission (voucher = supporting doc); Pago Parcial leaves the non-card residual subject to retention iff it exceeds the applicable minimum | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via txt) | 52_ pp.11-13 §3.1-3.1.2 (EVID-411) |
| LB-027 | 52_ §3.2e, §4-6: "Nota: el sistema asigna como fecha de constancia la fecha asignada en el campo Emisión al ingresado en la búsqueda." / "e. Generar retención: … a) Si de la selección realizada existen facturas de un mismo contribuyente, el sistema le genera una sola retención. b) Si desea generar una retención para una sola factura deberá seleccionar de forma individual…" / "b. Clic en el número de constancia: genera un archivo en PDF que se descargará a su computadora…" / "5. Constancia de retención con una factura — …tales como: cantidad de facturas, serie y número de factura." / "6. Constancia de retención que contiene más de una factura — El sistema muestra una constancia con más de una factura, mostrando la cantidad de facturas incluidas en la misma y mostrando el detalle de las facturas que fueron sujetas a retención." | IVA constancia semantics: document date = the agent-chosen "Emisión al" search date (vs ISR's invoice-date rule — R54 intentional asymmetry, keep both); grouping = one constancia per retained contribuyente per emission batch (1..n facturas with count + detail); delivery = PDF via constancia number | `gt/sources/52_SAT_RetWebIVA_Manual_2024.pdf` (via txt) | 52_ pp.13-15 §3.2e, §4, §5, §6 (EVID-412) |
| LB-028 | 53_: "LISTADO DE AGENTES DE RETENCIÓN DEL IVA AL 01/10/2025" (title, once) / column header every page: "No. NIT NOMBRE FECHA INICIO" / footers "Página 1 de 127"…"Página 127 de 127" / last row "8447 117392960 DIRECCIÓN DEPARTAMENTAL DE EDUCACION PETEN SUR ORIENTE 1/07/2025" / first rows "1 3213501 CENTRAL DE ALIMENTOS SOCIEDAD ANONIMA 1/09/2006"… / OCR census: 8,422 clean-pattern rows; 25 concatenated-defect rows (e.g. "8379 93757794CUERPO DE INGENIEROS DEL EJERCITO … 1/02/2017" [sic]) | Official SAT roster as-of 2025-10-01: 127 pages, 8,447 numbered agents, four columns only (No., NIT, NOMBRE, FECHA INICIO — range 1/09/2006…1/07/2025); NO agent-type/category column, no totals, no notes; 25 OCR NIT/name/date concatenation defects (GOQ-97) | `gt/sources/53_SAT_Agentes_RetIVA_2025-10-01.pdf` | 53_ p.1 title/header, p.127 footer; full-file structural scan (EVID-413, EVID-414) |
| LB-029 | 54_ SAT-0261: "SOLICITUD DE INSCRIPCIÓN COMO AGENTE DE RETENCIÓN DEL IVA" / "SAT- 0261" / INFORMACIÓN — "\"Otros Agentes de Retención\" (Art.6. Disposiciones Legales para el Fortalecimiento de la Administración Tributaria): Especifique los motivos para solicitar ser Agente de Retención del IVA." / "A) Declaro conocer el contenido del Decreto 20-2006… y me comprometo a cumplir con las obligaciones establecidas en ella." / "B) Declaro y juro que son verdaderos los datos contenidos en este formulario…" / field inventory: "1 Número de formulario 2 Número de Identificación Tributaria" / "3 Apellidos y nombres, razón o denominación social:" / domicilio fiscal block (4-14) / "16 Número de Identificación Tributaria 17 Nombre del Representante Legal" / "18 Fecha de nombramiento… 19 Fecha de inscripción… 20 Fecha de vencimiento (dd/mm/aaaa)" / signature blocks + "Firma y sello de recepción SAT" | SAT-0261 = the voluntary-inscription instrument under D-20-2006 art. 6 (form's own citation): motive statement + two declarations + 20-field layout (identity, domicilio fiscal, representante legal with fecha de inscripción); confirms the tri-partite agent provenance (SAT-calificado / por ley específica / voluntario SAT-0261) | `gt/sources/54_SAT-0261_form.pdf` (via `gt/.extractions/54_SAT-0261_form.pdf.txt`) | 54_ p.1 INFORMACIÓN block + declarations + field lines (EVID-415, EVID-416) |
## 3. Functional Requirements

### 3.1 Portal identity, access model & agent population

- **GT-FIN-FR-027:** The system shall model the two Retenciones Web portal
  regimes as one product surface pair with per-variant identity rows stamped
  with their internal dating only: Sistema Retenciones Web -IVA- (49_) and
  -ISR- (50_), both © 2025; the 49_ variant carries the in-page anchor
  "Listado Agentes de Retención al 01/06/2025" (content ≥ 2025-06-01) while
  50_ carries no internal date anchor — every read surface keeps the
  as-of qualifier and never presents either page as undated current law
  (GOQ-94 kin currency discipline, consumption side of T1's registry
  freshness model). (LB-001; EVID-386)
- **GT-FIN-FR-028:** RetWeb access shall require SAT agent status exactly as
  the portal states it: the taxpayer must be **calificado y activado** by SAT
  as Agente Retenedor del IVA (or be a statutory agent "designado por ley
  específica") — the partner-level agent flag is SAT-activation-driven dated
  data consumed from GT-TAX-FR-101, never self-declared; the regime basis
  rows (D-20-2006 + AG 425-2006 + Ley del IVA, as cited by the page itself)
  are taxation-owned (GT-TAX-FR-069) and are never re-derived here.
  (LB-002; EVID-387; cross-ref GT-TAX-FR-101, GT-TAX-FR-069)
- **GT-FIN-FR-029:** The login-path model shall encode the single credential
  plane: (i) IVA-qualified agents enter with **RNIT** + their Retenciones
  Web key and reach BOTH the IVA and ISR options; (ii) normal taxpayers
  enter via Agencia Virtual → Servicios → Retenciones Web and reach ISR
  constancia generation only; (iii) on the IVA side, active agentes
  retenedores use their **RetenIVA2** credentials while statutory agents
  (FR-048) log in with plain NIT. Product-side this maps to user/role
  gating, not credential replication of SAT's plane. (LB-009; LB-023;
  EVID-394, EVID-408)
- **GT-FIN-FR-030:** Legacy guard: the desktop system **RetenIVA** was
  retired ("vigente hasta el 31/07/2021", v0.0.20 retained for historical
  queries only) — the system shall never route any current obligation to a
  RetenIVA surface and shall record the sunset as a dated negative row;
  Retenciones Web is the sole successor surface. (LB-007; EVID-392)
- **GT-FIN-FR-031:** The system shall carry the RetWeb manual/template
  inventory as provenance rows: seven role-specific IVA manuals (delegación
  de permisos 20-11-2024; exportadores habituales 14-11-2024; exportadores
  D-29-89/especiales/otros 14-11-2024; Tesorería Nacional 31-01-2025;
  usuarios manuales 29-11-2024 — this corpus's 52_; fondos rotativos
  29-11-2024; unidades ejecutoras 29-11-2024) and the two official xlsx
  carga-masiva templates (papel; FEL-Terceros) — mechanics from a manual
  outside the corpus (all but 52_) shall never be asserted (GOQ-96).
  (LB-007; LB-011; LB-021; EVID-392, EVID-396, EVID-406; GOQ-96 → OQ-001)
- **GT-FIN-FR-032:** Agent master-data seeding shall ingest the official
  roster 53_ as a **dated saas-side seed (as-of 2025-10-01)**: 8,447
  numbered agents carrying only No./NIT/NOMBRE/FECHA INICIO (per-agent
  fecha-inicio range 2006-09-01…2025-07-01); the roster carries NO
  agent-type column (type attributes come from RTU/SAT calificación, never
  from this file) and 25 rows carry OCR NIT/name/date concatenation
  defects — every ingested NIT is verified (checksum/RTU) before use, and
  a fresh roster download supersedes the seed as a new dated vintage
  (consumption side of GT-TAX-FR-108). (LB-028; EVID-413, EVID-414;
  GOQ-97 → OQ-002; cross-ref GT-TAX-FR-108)
- **GT-FIN-FR-033:** The voluntary-inscription surface shall model form
  **SAT-0261** (Solicitud de Inscripción como Agente de Retención del IVA,
  "Otros Agentes de Retención" under D-20-2006 art. 6 as cited by the form):
  motive statement (free text) + the two sworn declarations + the 20-field
  layout (identity, domicilio fiscal 4-14, representante legal block with
  fecha de inscripción) with the SAT reception signature/stamp as the
  completion evidence — completing the tri-partite agent provenance
  (SAT-calificado / por ley / voluntario SAT-0261) recorded on the agent
  flag (statutory channels GT-TAX-FR-079; registry identity is
  RetWeb-owned, R46). (LB-029; EVID-415, EVID-416; cross-ref
  GT-TAX-FR-079)

### 3.2 IVA declaration surfaces (SAT-2340 / SAT-2320)

- **GT-FIN-FR-034:** The IVA retention declaration surface shall generate
  **SAT-2340** (Declaración Jurada de Retenciones del IVA) for retentions on
  invoices of **Régimen General and Pequeño Contribuyente** providers, due
  within the **first 15 días hábiles** of the month following the retention,
  paid via **boleta SAT 2000** at any bank or Bancasat (Declaraguate rails) —
  this FR is the OPERATIONAL surface OF GT-TAX-FR-105/106 (chassis +
  single-window deadline) and GT-TAX-FR-107 (form identity); the deadline
  value is consumed as a dated row, never re-derived. Form identity is
  RetWeb-owned (R46: never cited to D-20-2006/AG 425-2006); registry row
  cross-ref GT-FIN-FR-011. (LB-003; LB-004; EVID-388, EVID-389; R46;
  cross-ref GT-TAX-FR-105, GT-TAX-FR-106, GT-TAX-FR-107, GT-FIN-FR-011)
- **GT-FIN-FR-035:** The agropecuario surface shall generate **SAT-2320**
  (Declaración Jurada IVA Retenciones Agropecuario) for retentions on
  Régimen Especial de Contribuyente Agropecuario provider invoices, paid via
  boleta SAT 2000 — with the **R47 guard transcribed exactly**: the portal
  prints "dentro de los primeros diez (10) días hábiles del mes inmediato
  siguiente", a RetWeb-layer value whose instrument is NOT in the corpus;
  the statutory deadline remains **15 días hábiles uniformly**
  (GT-TAX-FR-106, R26). The 10-day print is stored as a dated
  GOQ-01-context note (provenance 49_, as-of ≥ 2025-06-01), NEVER frozen as
  a deadline constant, and the deadline engine resolves the statutory window
  unless a deployment explicitly binds the printed variant with its
  provenance. (LB-004; EVID-389; R47, R46; GOQ-01 kin → OQ-005; cross-ref
  GT-TAX-FR-106, GT-TAX-FR-107)
- **GT-FIN-FR-036:** The declaration content assembly shall carry "la
  totalidad del impuesto retenido" for the retention month from the
  registro-auxiliar surface (GT-TAX-FR-109 owns the ledger; even-zero duty
  and per-provider fields {NIT, nombre, %, valor, fecha} are
  GT-TAX-FR-105's chassis, consumed here, never re-stated as this file's
  rules). (LB-003; EVID-388; cross-ref GT-TAX-FR-105, GT-TAX-FR-109)
- **GT-FIN-FR-037:** Role boundary for Sector Público manual users (52_
  audience): in Retenciones Web they **only generate constancias**
  associated to the purchasing unit's main user; their declarations flow
  through the **Sistemas de Contabilidad del Estado** — the product shall
  model this boundary (constancia-emitting unit without its own RetWeb
  declaration duty) and never force a SAT-2340 filing for a manual-user
  configuration whose declaration lane is the State accounting system.
  (LB-022; EVID-407)

### 3.3 Rate-matrix presentation (renders the taxation CSV — never re-derives)

- **GT-FIN-FR-038:** The IVA rate-matrix presentation surface shall RENDER
  the rows of `gt/requirements/taxation/iva_retention_rates.csv` keyed on
  (agent class × provider context): Especiales/Otros 15%; Exportador
  D-29-89 65%; dualidad multi-rate prints "15%, 65%" and "15%, 15%, 65%"
  (regimes unnamed on the page — per-activity resolution is the Sistema
  model, GT-TAX-FR-084/085); Sector Público 25%; operadoras 15% + fuel
  1.5%. Every rendered value carries its CSV row status (statutory vs
  secondary-print-pending) and instrument provenance; the presentation layer
  shall contain NO rate constant of its own — statutory authority
  GT-TAX-FR-070..079 by exact id. (LB-005; EVID-390, EVID-417; cross-ref
  GT-TAX-FR-070..079, GT-TAX-FR-084, GT-TAX-FR-085)
- **GT-FIN-FR-039:** The pequeño-contribuyente presentation rows shall
  render the CSV secondary-print-pending rows exactly as flagged: **5% when
  the invoice monto ≥ Q2,500.01**, with the Q2,500.00 de minimis and its
  exceptions (Sector Público, operadoras de tarjeta, fuel paid by card) —
  all values consumed from GT-TAX-FR-080/FR-086 and the CSV rows (status
  secondary-print-pending, provenance 49_ ≥ 2025-06-01); never frozen,
  never re-keyed as statutory (GOQ-06/R55). (LB-006; EVID-391; GOQ-06 kin →
  OQ-006; cross-ref GT-TAX-FR-080, GT-TAX-FR-086)
- **GT-FIN-FR-040:** The agropecuario presentation rows shall render the
  CSV secondary-print-pending row **5% applied to the monto total de la
  factura** (invoice carries no separable IVA), processed through
  Retenciones Web (Agencia Virtual) — consumed from GT-TAX-FR-081 and the
  CSV row; statutory basis pending (GOQ-06/R55), never frozen.
  (LB-006; EVID-391; GOQ-06 kin → OQ-006; cross-ref GT-TAX-FR-081)
- **GT-FIN-FR-041:** The sector-público presentation rows shall render the
  provider-regime split **General 25% / Pequeño Contribuyente 5% / Especial
  de Contribuyente Agropecuario 5%** from the CSV rows (GT-TAX-FR-082): the
  25% row is statutory (art. 2); the 5/5 rows are secondary-print-pending
  (52_, 2024-11-29) and the floor-interplay flag (which Q-floor governs
  pequeño/agro providers of a sector-público agent) stays config-resolved,
  never hard-coded (GOQ-66 discipline via GT-TAX-FR-082).
  (LB-022; EVID-407; GOQ-06 kin → OQ-006; cross-ref GT-TAX-FR-082)
- **GT-FIN-FR-042:** The card-fuel presentation row shall render the
  **1.5% sobre el valor total** rate (the sole non-IVA base) from the CSV
  statutory row, consumed from GT-TAX-FR-077 with its GOQ-67 edge guards
  (GT-TAX-FR-110: petroleum-tax base composition unverifiable post-2006; no
  import-side retention) intact — the presentation adds no qualifier the
  taxation layer has not frozen. (LB-005; EVID-390; cross-ref
  GT-TAX-FR-077, GT-TAX-FR-110)

### 3.4 RetWeb IVA line model & card-payment mechanics

- **GT-FIN-FR-043:** The IVA retention line model shall carry the manual's
  field set: NIT proveedor, nombre retenido, número de autorización (FEL),
  serie, número, fecha factura, total factura, **importe neto** (= total
  ex-IVA for Régimen General only; for Pequeño Contribuyente and
  Agropecuario the same monto total — their invoices carry no separable
  IVA), **afecto retención** (the retention base; = total factura for
  PC/Agro), **retención** (applied value), and the card-payment registration
  option. Base semantics are data rules of the render/compute layer; rates
  resolve via GT-TAX-FR-085 (Sistema model). (LB-025; EVID-410; cross-ref
  GT-TAX-FR-085, GT-TAX-FR-091)
- **GT-FIN-FR-044:** The line-validation engine shall implement the printed
  validation set — **retención entre agentes** (agent-to-agent abstention),
  **montos mínimos** (de-minimis floors), **montos exentos o no afectos** —
  consuming the statutory rules from GT-TAX-FR-086 (Q2,500/Q30,000 floors),
  GT-TAX-FR-087 (agent-vs-agent via carné + Web list) and GT-TAX-FR-089
  (exempt pre-identification); this FR owns only the operational wiring of
  those checks on the retention line. (LB-025; EVID-410; cross-ref
  GT-TAX-FR-086, GT-TAX-FR-087, GT-TAX-FR-089)
- **GT-FIN-FR-045:** For FEL invoices issued in a currency other than
  quetzales, the retention computation shall use the quetzal amount at the
  **Banco de Guatemala exchange rate of the factura's fecha de
  certificación** — rate FETCH is a saas-side service (Banguat published
  rates), applied on the odoo-side retention line; rule consumed from
  GT-TAX-FR-094 (mechanics this file, statutory anchor taxation).
  (LB-025; EVID-410; cross-ref GT-TAX-FR-094)
- **GT-FIN-FR-046:** **Pago Total** card registration: when an invoice is
  fully paid by credit/debit card, it shall leave the constancia-emission
  pool entirely (no agent constancia; the card voucher documents the
  factura) — the operator retains instead (GT-TAX-FR-076 exclusivity);
  consumed jointly with GT-TAX-FR-088. (LB-026; EVID-411; cross-ref
  GT-TAX-FR-088, GT-TAX-FR-076)
- **GT-FIN-FR-047:** **Pago Parcial** card registration: the non-card
  residual shall remain available for constancia emission **iff it exceeds
  the applicable retention minimum** — mixed card/invoice settlements split
  the retention base this way; consumed jointly with GT-TAX-FR-088.
  (LB-026; EVID-411; cross-ref GT-TAX-FR-088)
- **GT-FIN-FR-048:** The statutory-agent path shall be modeled per the 52_
  print with the **R59 guard verbatim**: entities under **D-27-92 "artículo
  54 B" [printed as such; presumably 54 BIS — equating them requires the
  post-2018 D-27-92 text, GOQ-01 kin]**, first paragraph, that carry full
  accounting and are NOT SAT-calified, act as retention agents **only when
  paying or accrediting income to Agropecuario-regime suppliers**,
  accessing the system by plain NIT (no RetenIVA2 credentials) — subtype
  consumed from GT-TAX-FR-083 (secondary print, never frozen); the path
  stands regardless of the B/BIS nomenclature resolution. (LB-023;
  EVID-408; R59; GOQ-01 kin → OQ-005; cross-ref GT-TAX-FR-083)
### 3.5 ISR RetWeb operating system (50_/51_)

- **GT-FIN-FR-049:** The ISR feed contract shall be **FEL-first**: received
  e-invoices (estado vigente) are available to the agent from the moment
  the provider emits them, and paper documents enter exclusively via carga
  masiva (FR-072/073) — legal basis as cited by the page: D-10-2012 (LAT;
  statutory ISR regime taxation/05, never re-derived here). Received-DTE
  search params: Período del/al, NIT Retenido, Estado de Asignación
  (Todos/Sin Asignar/Asignados). (LB-008; LB-012; EVID-393, EVID-397)
- **GT-FIN-FR-050:** The 2022 phased onboarding shall be recorded as dated
  milestone rows (print of 50_, © 2025): Especiales Grandes 2022-01-01;
  Especiales Medianos 2022-02-01; Normales 2022-03-01; Sector Público
  2022-04-01; Especiales Regionales 2022-05-01 — all classes incorporated
  by 1-May-2022; no product behavior may key on these historical milestones
  except historical-scope qualification of pre-2022 data. (LB-008;
  EVID-393)
- **GT-FIN-FR-051:** ISR retention candidate lines shall be keyed on the
  FEL retention legends: invoices carrying **"Sujeto a retención
  definitiva"** are surfaced automatically for rent-category assignment;
  invoices carrying **"Sujeto a pagos trimestrales ISR"** (rentas-de-capital
  path) enter via the manual **Procesar FEL** operation (NIT Emisor + Serie
  DTE + Número DTE) — legend strings are the FEL document's own
  (e-invoicing wave owns the emission side; suppression rules GT-TAX-FR-165
  consumed). (LB-012; EVID-397; cross-ref GT-TAX-FR-165)
- **GT-FIN-FR-052:** The cross-constancia guard shall block processing a
  document for a new retention while a live IVA-or-ISR constancia for it
  exists — existing constancias must be anuladas first (FR-066); the
  e-invoicing anulación blocker is consumed outcome-only: a FEL DTE with a
  registered Retenciones Web retention is not anulable (GT-EINV-FR-210).
  (LB-012; EVID-397; cross-ref GT-EINV-FR-210)
- **GT-FIN-FR-053:** The ISR declaration deadline engine shall implement
  the mechanics exactly as printed: declare the DJ with the totality of
  retained tax AND enter it **within the first 10 días hábiles of the month
  following the month the constancia was emitted** (keyed to
  constancia-emission month — distinct from the IVA retention-month key).
  Qualifier discipline (GOQ-99 mechanics half): the engine stores the
  qualifier verbatim per source; the statutory qualifier registry is
  GT-TAX-FR-142 (taxation/04) and the statutory cycles are GT-TAX-FR-163
  (Opcional), GT-TAX-FR-182 (capital), GT-TAX-FR-185 (non-resident payers),
  GT-TAX-FR-188/189 (facturas especiales) — consumed by exact id, never
  re-derived. Día-hábil resolution consumes the external calendar
  ingestion surface (GT-FIN-FR-024; GOQ-14 kin). (LB-010; EVID-395;
  GOQ-99 → OQ-004; cross-ref GT-TAX-FR-142, GT-TAX-FR-163, GT-TAX-FR-182,
  GT-TAX-FR-185, GT-TAX-FR-189, GT-FIN-FR-024)
- **GT-FIN-FR-054:** The ISR constancia document date shall be **the
  factura's date** ("Emitir la constancia de retención respectiva con la
  fecha de la factura") — kept ASYMMETRIC to the IVA rule (FR-068:
  "Emisión al" search date) per R54 (intentional, both rules kept); the
  declaration clock (FR-053) keys on constancia EMISSION, not on this
  document date. (LB-010; EVID-395; R54)
- **GT-FIN-FR-055:** The ISR constancia delivery obligation shall be
  transcribed EXACTLY as printed: deliver to the retained taxpayer "dentro
  de los primeros (5) días del mes inmediato siguiente" — **WITHOUT the
  "hábiles" qualifier** (the 10-day rule carries it; this one does not, as
  printed — R54/GOQ-99 mechanics half). The deadline row stores the print
  verbatim with provenance 50_ (© 2025) and defers the legal qualifier to
  the statutory registry (GT-TAX-FR-142: taxation-side transcription per
  instrument); the engine must not silently add "hábiles". (LB-010;
  EVID-395; R54; GOQ-99 → OQ-004; cross-ref GT-TAX-FR-142, GT-TAX-FR-163)
- **GT-FIN-FR-056:** The declarable rentas surface shall offer exactly the
  three categories as printed — **Actividades Lucrativas / Rentas de
  Capital / Facturas Especiales** — mapped onto the retention catalog
  (FR-060..064); and the permission-delegation model (titular delegates
  gestiones to collaborators, "(Otras Rentas)" scope) shall be a supported
  role configuration. (LB-010; LB-014; EVID-395, EVID-399)
- **GT-FIN-FR-057:** The ISR declaration surface shall generate the DJ on
  **formulario SAT-1331** (R46 spine: ISR retenciones; registry identity
  T1's GT-FIN-FR-004 — never restated) paid by printing the **boleta SAT
  2000** for any bank; declaration states {**pendiente de pago, pagada**}.
  (LB-017; EVID-402; R46; cross-ref GT-FIN-FR-004)
- **GT-FIN-FR-058:** Rectification mechanics: applicable only to a DJ in
  **estado pagado**, and only for constancia-level changes (creation of new
  constancias; anulación of constancias); rectifying generates a NEW
  SAT-1331 in **estado congelado** with the **multa por rectificación
  incluida** (multa amounts are taxation/06 territory — never derived
  here); **Liberar** releases a frozen DJ/rectification when no constancia
  modification actually occurred. (LB-017; EVID-402)
- **GT-FIN-FR-059:** Payment state refresh: on payment of the DJ, the
  associated constancias flip **Impresa/Asignada → Impresa/Pagada** (refresh
  may lag minutes), after which the **retained party** can query and view
  their received constancias from their own Agencia Virtual — the
  seller-side visibility contract. (LB-017; EVID-402; cross-ref
  GT-TAX-FR-095 seller-side netting)

### 3.6 ISR retention catalog (config surface rendering isr_rates.csv)

- **GT-FIN-FR-060:** The ISR retention catalog shall be a configuration
  surface mirroring the manual's 3-category taxonomy with numbered
  conceptos as SAT codes (used by carga masiva, FR-072): Category 1
  Régimen Opcional Simplificado Sobre Ingresos (conceptos 1-20, incl.
  dietas 13 and otras remuneraciones 20); Category 2 Rentas de Capital
  Inmobiliario (conceptos 1-2); Category 3 Rentas de Capital Mobiliario
  (conceptos 1-8, concepto 8 = dividendos). The catalog carries codes +
  labels ONLY — every rate/base formula resolves from
  `gt/requirements/taxation/isr_rates.csv` rows and the GT-TAX-FR ids
  below. (LB-013; EVID-398)
- **GT-FIN-FR-061:** Category 1 rate logic shall render `isr_rates.csv`
  opcional_simplificado_monthly bracket rows (bracket_1 5% Q0.01-30,000.00;
  bracket_2 7% + fixed Q1,500.00 over the Q30,000.00 excess, valid ≥
  2014-01-01): the manual's terse print "7% + excedente de Q1,500.00"
  [sic] is the same structure — the CSV/LAT rows are the authority
  (GT-TAX-FR-159/160); the config surface never re-states the numbers.
  (LB-013; EVID-398; cross-ref GT-TAX-FR-159, GT-TAX-FR-160)
- **GT-FIN-FR-062:** Category 2 base formula shall render the print
  "Total, de factura dividido 1.12, se resta el 30% del gasto y se aplica
  el 10%" as the operationalization of the statutory capital-inmobiliario
  base (GT-TAX-FR-177: 70% presumed-expense base; `isr_rates.csv` capital
  mobiliarias_inmobiliarias_ganancias 10% row) — formula executed, values
  consumed. (LB-013; EVID-398; cross-ref GT-TAX-FR-177)
- **GT-FIN-FR-063:** Category 3 rates shall render `isr_rates.csv` capital
  rows: mobiliario conceptos 1-7 at 10% (GT-TAX-FR-179); **concepto 8
  dividendos/ganancias/utilidades at 5%** (GT-TAX-FR-180; CSV
  dividendos_utilidades row). (LB-013; EVID-398; cross-ref GT-TAX-FR-179,
  GT-TAX-FR-180)
- **GT-FIN-FR-064:** The Facturas Especiales declarable category (LB-014
  option list) shall resolve its retention to the statutory
  facturas-especiales rows (GT-TAX-FR-188: **5% definitive on the factura
  value excluding IVA**, valid_from 2019-05-08; pre-reform historical row
  in the CSV) and its constancia semantics to GT-TAX-FR-189 (copy of the
  factura especial = constancia); this file renders the category surface
  only. (LB-013; LB-014; EVID-398, EVID-399; cross-ref GT-TAX-FR-188,
  GT-TAX-FR-189)

### 3.7 Constancia machinery (both taxes)

- **GT-FIN-FR-065:** The constancia emission flow shall implement: search
  (Emisión del/al period, Retenciones que declara ISR, Retención a Declarar
  category, Tipo Documento FEL/Papel, optional NIT Retenido / Número de
  Autorización FEL / Serie / Número) → Habilitar generación → **Generar
  Retención** per selected factura or **masiva** over the selection; the
  constancia is identified by its **número de constancia** and downloads as
  **PDF**. (LB-014; EVID-399)
- **GT-FIN-FR-066:** The constancia state machine shall implement
  **Impresa → Impresa/Asignada → Impresa/Pagada** plus terminal
  **Anulada**; anulación (single or selected batch from the Consulta
  screen) re-opens categorización + emisión for the underlying document —
  wiring the cross-constancia guard (FR-052) and the rectification
  triggers (FR-058). (LB-015; EVID-400)
- **GT-FIN-FR-067:** Constancia batch export shall support **ZIP, PDF and
  Excel ("Tipo Descarga Excel: Detallado")** delivered by email
  notification to the RTU-registered address of the agent (RTU-Digital for
  carga-masiva results) — export job + notification surfaces; the email
  address is RTU data, never locally re-keyed. (LB-015; LB-020; EVID-400,
  EVID-405)
- **GT-FIN-FR-068:** The IVA constancia semantics shall implement the R54
  IVA half: **document date = the agent-chosen "Emisión al" search date**
  (asymmetric to ISR's factura-date rule, FR-054 — both kept); **grouping =
  one constancia per retained contribuyente per emission batch**
  (same-contribuyente selection → "una sola retención"; single-factura
  selection → individual), with multi-factura constancias carrying the
  invoice count and detail. Operational surface OF GT-TAX-FR-100.
  (LB-027; EVID-412; R54; cross-ref GT-TAX-FR-100)
- **GT-FIN-FR-069:** The constancia document class shall be the
  **prenumerada y autorizada** certificate, one per retention-triggering
  operation (issued at invoice delivery), whose 10-field minimum content
  contract and per-operation/monthly-consolidated granularity are OWNED by
  GT-TAX-FR-098/099 (reglamento arts. 6/20) — this FR renders the emission
  surface only; the registry's form code for the IVA constancia (SAT-2229,
  RetWeb app-generated) is consumed from T1 (GT-FIN-FR-011), and whether
  constancias are themselves a FEL DTE family member stays OPEN (GOQ-98 —
  no DTE-type code appears anywhere in this corpus; the system shall not
  assume one). (LB-003; EVID-388; GOQ-98 → OQ-003; cross-ref
  GT-TAX-FR-098, GT-TAX-FR-099, GT-FIN-FR-011)

### 3.8 Declaration anexos (LAT arts. 48 / 15)

- **GT-FIN-FR-070:** The DJ anexo surface shall carry, per retained
  taxpayer per declaration, the LAT **art. 48** field set quoted by the
  manual: nombres y apellidos completos, NIT, valor de lo efectivamente
  acreditado o pagado, monto de la retención — surfaced as the
  declaration's "Ver detalle" view; the field set is statutory (LB quotes
  art. 48 verbatim); this FR owns only the assembly surface reading the
  registro auxiliar. (LB-016; EVID-401; cross-ref GT-TAX-FR-105,
  GT-TAX-FR-109)
- **GT-FIN-FR-071:** The facturas especiales anexo (LAT **art. 15**) shall
  carry, per issued factura especial: nombre y apellido completos,
  domicilio fiscal, NIT o número de identificación personal, concepto,
  renta acreditada o pagada, monto de la retención — attached to the DJ
  ("Detalle de Facturas Especiales"); statutory anchor LB-018; ISR
  semantics GT-TAX-FR-188/189 (cross-ref only). (LB-018; EVID-403;
  cross-ref GT-TAX-FR-188, GT-TAX-FR-189)

### 3.9 Carga masiva engines

- **GT-FIN-FR-072:** The ISR carga-masiva file schema shall implement the
  7-column contract — NIT Proveedor (sin guión), Categoría de Renta,
  Concepto de Renta (codes of FR-060), Serie Documento, Número Documento,
  Fecha Documento (GENERAL/FECHA formats), Total Documento (NÚMERO, 2
  decimals) — with the **RECIBO convention** ("Colocar la palabra RECIBO o
  dejar la casilla en blanco") for non-invoice-backed rents (dietas,
  dividendos) and the **renta imponible override** for capital categories;
  dividendos rows add the 8th column **Período de dividendos que declara**.
  Use cases governed by **CTI 03-2023** (arrendador-billed utility FELs
  under a prior lease contract) are recorded with the criterion citation.
  (LB-019; EVID-404)
- **GT-FIN-FR-073:** The ISR batch engine shall implement the upload
  contract: CSV comma-delimited; two templates — **Papel** (full 7-col) and
  **FEL (Terceros)** (3-column pointer NIT retenido/Serie/Número; loaded
  FELs then appear in Categoría de Renta for in-system assignment) — with
  the seven batch states {En Cola, Procesado, Error de Procesamiento,
  Revertidos, Error en reversión, En Cola Reversión, Todos} and one-shot
  batch-level **reversión** (Anular reverts a previously loaded file; state
  Carga Revertido); results (processed count + error records) notified by
  email to the RTU-Digital address. (LB-020; EVID-405)
- **GT-FIN-FR-074:** The IVA paper carga-masiva schema shall implement the
  7-column contract of 52_ §2: NIT retenido (sin guiones), Serie, Número de
  factura, Fecha de factura (dd/mm/aaaa), Total factura, **Monto
  agrícola** (agricultural/livestock value — exportador-calified agents
  only, feeding the dualidad/agro base decomposition of GT-TAX-FR-085),
  **Monto exento u otros impuestos** (exempt amounts or specific taxes:
  timbre de prensa, impuesto a la distribución de petróleo, hospedaje,
  bomberos…) — CSV comma-delimited, **no header**, no thousand separators
  (columns e/f/g formato general), with the list-separator comma
  configuration note carried for users; batch reversal runs on the saas
  engine (FR-073 states) and only over rows without an emitted constancia
  (annul the constancia first), once per batch. (LB-024; EVID-409;
  cross-ref GT-TAX-FR-085, FR-073)
## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + provenance
+ as-of qualifier; snapshot-on-write. Rate/threshold rows are
taxation-owned (CSV sidecars) — this file stores NO statutory constants,
only operational surfaces, print-provenance rows and state machines. R46:
form-number rows carry RetWeb provenance (49_/50_/51_/52_/54_ prints),
never D-20-2006/AG 425-2006. R47: the SAT-2320 10-day print and every
secondary-print rate reference carry status flags — never frozen.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.retweb.portal | variant / identity_es / as_of / anchor | selection iva-isr / char / date / char | IVA (49_, anchored ≥ 2025-06-01 via roster link) / ISR (50_, no anchor, © 2025 only) | FR-027 |
| l10n_gt.retweb.access | population / credential_plane / entry_path | selection / selection / char | rnit_dual (IVA+ISR) / agencia_virtual (ISR constancias only) / reteniva2_active / nit_statutory | FR-028, FR-029, FR-048 |
| l10n_gt.retweb.agent.roster | no / nit / nombre / fecha_inicio / as_of / ocr_defect | int / char / char / date / date=2025-10-01 / boolean | seed 53_: 8,447 rows; fecha-inicio range 2006-09-01…2025-07-01; NO agent-type column; 25 defect rows flagged; NIT checksum/RTU-verified on import | FR-032 |
| l10n_gt.retweb.inscription | form / motive / declarations / rep_legal / fecha_inscripcion | char=SAT-0261 / text / boolean×2 / char / date | D-20-2006 art. 6 hook (form's own citation); 20-field layout | FR-033 |
| l10n_gt.retweb.declaration.surface | form / provider_scope / deadline_row / payment | char / selection / m2o dated row / char | SAT-2340 (general+pequeño, 15 dh statutory) / SAT-2320 (agro; 10-dh print = GOQ-01-context note, never frozen) / boleta SAT 2000 (bank/Bancasat) | FR-034, FR-035 |
| l10n_gt.retweb.rate.presentation | csv_row_ref / status / instrument | char (iva_retention_rates.csv row key) / selection statutory-secondary-print-pending / char | render-only rows keyed (agent_class, provider_context, rate_pct); no local constants | FR-038..FR-042 |
| l10n_gt.retweb.line | doc keys (nit, nombre, autorizacion, serie, numero, fecha) / total / importe_neto / afecto / retencion / card_option | char×6 / decimal / decimal / decimal / decimal / boolean | neto = total ex-IVA (General only); afecto = base (total for PC/Agro); validations entre-agentes/mínimos/exentos (GT-TAX-FR-086..089) | FR-043, FR-044 |
| l10n_gt.retweb.line.fx | currency / rate_source / rate_date | m2o currency / selection=banguat / date | rate at fecha de certificación; fetch = saas service | FR-045 |
| l10n_gt.retweb.card.payment | mode / residual / over_minimum | selection pago_total-pago_parcial / decimal / boolean | total → invoice leaves pool (voucher documents); parcial → residual retains iff > minimum | FR-046, FR-047 |
| l10n_gt.retweb.isr.feed | legend / routing / search_params | selection sujeto-a-retencion-definitiva / sujeto-a-pagos-trimestrales-isr / selection auto-procesar_fel / json | procesar FEL keys: NIT emisor + serie DTE + número DTE; estado-vigente filter | FR-049, FR-051 |
| l10n_gt.retweb.onboarding | taxpayer_class / valid_from | selection / date | 2022 milestones: grandes 01-01 / medianos 02-01 / normales 03-01 / público 04-01 / regionales 05-01 | FR-050 |
| l10n_gt.retweb.isr.catalog | category_no / concepto_no / label_es / rate_ref | int 1-3 / int / char / char (isr_rates.csv row key) | 3 categories, ~30 conceptos; rates/bases resolve from CSV + GT-TAX-FR ids (159/160/177/179/180/188) | FR-060..FR-064 |
| l10n_gt.retweb.constancia | numero / doc_type fel-papel / date_rule / group_key / state | char (prenumerada) / selection / selection factura_date-iva-emision_al / char (contribuyente+batch) / selection impresa-asignada-pagada-anulada | date asymmetry R54 kept; per-contribuyente consolidation 1..n facturas with count+detail; anulación re-opens | FR-054, FR-065..FR-069 |
| l10n_gt.retweb.constancia.export | formats / email_target | multi-selection zip-pdf-excel_detallado / char (RTU) | notification to RTU-registered address | FR-067 |
| l10n_gt.retweb.declaration.isr | form=SAT-1331 / payment=boleta SAT 2000 / state / rectification | char / char / selection pendiente_de_pago-pagada-congelado / json | rectificación only from pagada (constancia create/annul) → new SAT-1331 congelado + multa incluida; Liberar on no-change | FR-057, FR-058 |
| l10n_gt.retweb.anexo | type / fields | selection art48-art15 / json | art. 48: {nombre completo, NIT, valor acreditado/pagado, monto retención}; art. 15: + domicilio fiscal, NIT o ID personal, concepto, renta | FR-070, FR-071 |
| l10n_gt.retweb.cargamasiva.batch | template / state / reversión / email_ack | selection papel-fel_terceros / selection en_cola-procesado-error_procesamiento-revertidos-error_reversión-en_cola_reversión / boolean one-shot / char | ISR 7/8-col + RECIBO + período dividendos; IVA 7-col (monto agrícola + monto exento; no header); IVA reversal only constancia-free rows | FR-072, FR-073, FR-074 |
| l10n_gt.retweb.guard | key | char | reteniva_never_routed (sunset 2021-07-31); sat2320_10day_never_frozen (R47); no_constancia_dte_type_assumed (GOQ-98); manual_users_no_dj (State accounting lane); no_form_number_to_D20-2006 (R46) | FR-030, FR-035, FR-037, FR-069 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = ingestion,
transformation and authoritative validation in the Elixir core; `shared` =
contract items both sides must honor identically. Wave defaults for this
file (binding): constancia emission data + registro-auxiliar reads =
`odoo`; carga-masiva batch state machines + roster ingestion + FX rate
fetch = `saas`; rate rendering + deadline engines + catalogs = `shared`.
Model names stable across Odoo 17/18/19/20; no version-specific behavior
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-027 | shared | — (config data §4) | retweb.portal identity/as-of rows | GOQ-94 kin currency qualifier on every read surface |
| FR-028 | odoo | res.partner | agent flag (SAT-activation-driven) | Consumes GT-TAX-FR-101 dated data; never self-declared |
| FR-029 | odoo | res.users / res.groups | retweb role gating (rnit_dual / agencia_virtual / statutory-nit) | Product maps roles, never replicates SAT credentials |
| FR-030 | shared | — (guard) | reteniva_never_routed | Sunset dated row 2021-07-31; v0.0.20 historical queries only |
| FR-031 | shared | — (config data §4) | manual/template inventory provenance rows | 7 manuals (dates 2024-11-14…2025-01-31); only 52_ in corpus (GOQ-96) |
| FR-032 | saas | roster ingestion service | retweb.agent.roster seed (as-of 2025-10-01) | 8,447 rows; NIT checksum/RTU verification; no category column (GOQ-97); new vintage per re-download |
| FR-033 | odoo | retweb.inscription record | SAT-0261 capture surface | Motive + declarations + 20 fields; art. 6 hook; tri-partite provenance |
| FR-034 | odoo | account.move (declaration skeleton) + registro-auxiliar read | SAT-2340 generation + boleta SAT 2000 | Deadline row consumed (GT-TAX-FR-105/106); form identity GT-TAX-FR-107 + GT-FIN-FR-011 |
| FR-035 | shared | — (dated print row + guard) | SAT-2320 surface + 10-dh GOQ-01-context note | R47: never frozen; statutory 15 dh (GT-TAX-FR-106); agro provider routing |
| FR-036 | odoo | account.move (declaration assembly) | totality-of-retained-tax read from registro auxiliar | Even-zero + per-provider fields = GT-TAX-FR-105 (consumed) |
| FR-037 | shared | — (config row) | manual_users_no_dj boundary | Declarations via Sistemas de Contabilidad del Estado |
| FR-038 | shared | — (render layer) | rate.presentation rows → iva_retention_rates.csv | No local rate constants; CSV row status surfaced (statutory / secondary-print-pending) |
| FR-039 | shared | — (render layer) | PC 5% ≥ Q2,500.01 + de-minimis render | GOQ-06; GT-TAX-FR-080/086 consumption |
| FR-040 | shared | — (render layer) | agro 5% total-factura render | GT-TAX-FR-081; Agencia Virtual processing note |
| FR-041 | shared | — (render layer) | sector público 25/5/5 render | GT-TAX-FR-082; floor interplay stays config (GOQ-66 discipline) |
| FR-042 | shared | — (render layer) | fuel 1.5% valor-total render | GT-TAX-FR-077 + GOQ-67 guards (GT-TAX-FR-110) intact |
| FR-043 | odoo | account.move.line (retention line) | neto/afecto/retención + doc keys | PC/Agro base semantics = data rule; % via GT-TAX-FR-085 |
| FR-044 | odoo | account.move.line (validators) | entre-agentes / mínimos / exentos checks | Statutory rules GT-TAX-FR-086/087/089 — wiring only |
| FR-045 | saas | Banguat FX fetch service | rate at fecha de certificación | Applied on odoo line; saas owns the fetch/cache (wave default) |
| FR-046 | odoo | account.payment.register (card flag) | pago_total → pool exit | Voucher documents; operator retains (GT-TAX-FR-076/088) |
| FR-047 | odoo | account.payment.register (card flag) | pago_parcial → residual over minimum | GT-TAX-FR-088 consumption |
| FR-048 | shared | — (config data §4) | statutory-agent subtype row | R59 "54 B" [sic] guard; GT-TAX-FR-083 (never frozen); NIT-login population |
| FR-049 | shared | — (feed contract) | FEL-first ISR feed + paper-via-carga-masiva | Received-DTE search params contract; D-10-2012 as cited by page |
| FR-050 | shared | — (config data §4) | 2022 onboarding milestones | Historical-scope qualification only |
| FR-051 | odoo | account.move.line (received DTE candidates) | legend-keyed routing (auto / Procesar FEL) | Legend strings = FEL document's own; GT-TAX-FR-165 suppression consumed |
| FR-052 | odoo | constancia emission guard | no second live constancia per document | GT-EINV-FR-210 anulación blocker cited outcome-only |
| FR-053 | shared | — (deadline engine) | ISR 10-días-hábiles declare+enter (constancia-emission key) | Qualifier registry = GT-TAX-FR-142; cycles GT-TAX-FR-163/182/185/189; día-hábil calendar via GT-FIN-FR-024 (GOQ-14 kin) |
| FR-054 | odoo | constancia record | ISR date = factura date | R54 asymmetry vs FR-068 kept |
| FR-055 | shared | — (deadline engine row) | 5-días delivery, verbatim WITHOUT "hábiles" | GOQ-99 mechanics half; engine must not add the qualifier |
| FR-056 | shared | — (config data §4) | 3 declarable rentas + delegation roles | Categories map onto FR-060 catalog |
| FR-057 | odoo | account.move (DJ skeleton) + payment slip print | SAT-1331 + boleta SAT 2000 | R46 spine; registry identity T1 GT-FIN-FR-004; states pendiente/pagada |
| FR-058 | odoo | retweb.declaration.isr (rectification flow) | congelado + multa + Liberar | Multa amounts taxation/06 — never derived here |
| FR-059 | odoo | constancia state refresh + partner visibility | Impresa/Pagada flip; seller Agencia Virtual view | Refresh lag tolerated; GT-TAX-FR-095 seller side |
| FR-060 | shared | — (config data §4) | ISR catalog codes (3 categories, ~30 conceptos) | Codes + labels only; rates from isr_rates.csv |
| FR-061 | shared | — (render layer) | OS bracket render (5% / 7%+Q1,500) | GT-TAX-FR-159/160; terse manual print noted [sic] |
| FR-062 | shared | — (render layer) | inmobiliario (÷1.12 −30%) ×10% formula | GT-TAX-FR-177 operationalization |
| FR-063 | shared | — (render layer) | mobiliario 10% / dividendos 5% | GT-TAX-FR-179/180 |
| FR-064 | shared | — (render layer) | facturas especiales 5% (≥2019-05-08) | GT-TAX-FR-188/189; CSV historical pre-reform row |
| FR-065 | odoo | constancia emission flow | search → Habilitar → Generar (individual/masiva) → PDF by número | Search keys incl. autorización FEL / serie / número |
| FR-066 | odoo | constancia record state machine | impresa/asignada/pagada/anulada | Anulación re-opens categorización + emisión |
| FR-067 | odoo | export job + notification | ZIP/PDF/Excel detallado → RTU email | RTU address is external data |
| FR-068 | odoo | constancia record (IVA variant) | date = "Emisión al"; per-contribuyente grouping | Operational surface of GT-TAX-FR-100; R54 |
| FR-069 | odoo | constancia document class surface | prenumerada per-operation emission | Field contract GT-TAX-FR-098/099; SAT-2229 identity T1; GOQ-98 no DTE-type assumption |
| FR-070 | odoo | declaration anexo assembly (art. 48) | per-taxpayer 4-field set, Ver detalle | Reads registro auxiliar (GT-TAX-FR-109) |
| FR-071 | odoo | declaration anexo assembly (art. 15) | facturas especiales 7-field set | GT-TAX-FR-188/189 cross-ref |
| FR-072 | shared | — (file-format contract §4) | ISR 7/8-col schema + RECIBO + período dividendos | CTI 03-2023 use case recorded with citation |
| FR-073 | saas | carga-masiva batch engine | states ×7 + one-shot reversión + email ack | Papel vs FEL (Terceros) 3-col pointer template |
| FR-074 | shared | — (file-format contract §4) | IVA 7-col paper schema (monto agrícola + monto exento; no header) | Batch execution + constancia-free reversal guard ride the saas engine (FR-073); exportador dualidad feeds |

## 6. Acceptance Criteria

- **AC-001:** Given the portal identity rows, when any RetWeb surface is
  read, then the IVA variant carries as-of ≥ 2025-06-01 (roster-link
  anchor) and the ISR variant carries © 2025 with NO date anchor, and
  neither is presented as undated current law. (FR-027)
- **AC-002:** Given a partner flagged as retention agent, when the flag is
  inspected, then its provenance is one of {SAT calificado y activado,
  statutory art. 54 B [BIS] path, SAT-0261 voluntary inscription} with
  dated evidence — never self-declaration; and a statutory-agent entity
  retains ONLY against Agropecuario-regime suppliers. (FR-028, FR-048,
  FR-033)
- **AC-003:** Given an IVA retention month on General/Pequeño provider
  invoices, then the generated declaration is SAT-2340 due the first 15
  días hábiles of the following month with boleta SAT 2000; given
  agropecuario provider invoices, then the form is SAT-2320 whose deadline
  surface shows the 10-días-hábiles print ONLY as a provenance-flagged
  GOQ-01-context note while the engine resolves the statutory 15-días
  window (R47), and no form number anywhere cites D-20-2006 or AG 425-2006
  (R46). (FR-034, FR-035)
- **AC-004:** Given the rate presentation layer, when any rate value is
  rendered, then it resolves from `iva_retention_rates.csv` /
  `isr_rates.csv` rows carrying status and instrument — the layer contains
  zero local rate constants; the PC 5% ≥ Q2,500.01, agro 5%
  total-factura and sector-público 5/5 rows render as
  secondary-print-pending (GOQ-06) and the fuel 1.5% renders as
  %-of-valor-total (sole base exception). (FR-038..FR-042, FR-061..FR-064)
- **AC-005:** Given an ISR constancia-emission month, then the DJ
  (SAT-1331) + enterar deadline computes as the first 10 días hábiles of
  the following month; given the constancia delivery duty, then the
  deadline row reads "primeros (5) días" verbatim WITHOUT "hábiles" and
  the engine has not silently added the qualifier. (FR-053, FR-055)
- **AC-006:** Given an ISR constancia, then its document date equals the
  factura date; given an IVA constancia, then its document date equals the
  "Emisión al" search date and same-contribuyente invoices in one batch
  consolidate into one constancia with invoice count + detail — both rules
  coexist (R54). (FR-054, FR-068)
- **AC-007:** Given a received FEL carrying "Sujeto a retención
  definitiva", then it auto-surfaces for category assignment; given one
  carrying "Sujeto a pagos trimestrales ISR", then it enters only via
  Procesar FEL (NIT emisor + serie + número); given a document with a live
  IVA-or-ISR constancia, then processing is blocked until the constancia
  is anulada — and the FEL itself is not anulable while a RetWeb retention
  is registered (GT-EINV-FR-210 outcome). (FR-051, FR-052)
- **AC-008:** Given a paid ISR DJ with constancia-level changes, then
  rectification produces a new SAT-1331 in estado congelado with the
  multa por rectificación included; given no actual constancia
  modification, then Liberar releases it; given DJ payment, then
  constancias flip to Impresa/Pagada and the retained party can view them
  in their Agencia Virtual. (FR-058, FR-059)
- **AC-009:** Given the constancia state machine, then the reachable
  states are exactly {Impresa, Impresa/Asignada, Impresa/Pagada, Anulada},
  anulación re-opens categorización + emisión, and batch export offers
  ZIP/PDF/Excel detallado delivered to the RTU-registered email.
  (FR-066, FR-067)
- **AC-010:** Given the ISR carga-masiva file, then it validates against
  the 7-column schema (8 for dividendos with período), accepts RECIBO or
  blank in serie, applies the renta-imponible override for capital
  categories and references concept codes 1-20/1-2/1-8 of the catalog;
  given a batch, then it traverses the seven states with one-shot
  reversión and email results. (FR-072, FR-073)
- **AC-011:** Given the IVA paper carga file, then it is a headerless
  comma-delimited CSV whose 7 columns include monto agrícola (exportador
  agents) and monto exento u otros impuestos, with no thousand
  separators; given a reversal request over rows with emitted
  constancias, then the reversal is rejected until those constancias are
  anuladas. (FR-074)
- **AC-012:** Given a card Pago Total registration, then the invoice
  leaves the constancia-emission pool (voucher documents it); given Pago
  Parcial, then only the non-card residual over the applicable minimum
  retains. (FR-046, FR-047)
- **AC-013:** Given a non-Quetzal FEL retention line, then the retention
  computes from the quetzal amount at the Banguat rate of the factura's
  fecha de certificación (saas-fetched rate). (FR-045)
- **AC-014:** Given the roster seed, then it holds 8,447 rows as-of
  2025-10-01 with fecha-inicio 2006-09-01…2025-07-01, the 25 OCR-defect
  rows are flagged and NIT-verified before use, no agent-type attribute is
  seeded from it, and no obligation ever routes to RetenIVA (sunset
  2021-07-31). (FR-030, FR-032)
- **AC-015:** Given the DJ anexos, then the art. 48 anexo carries per
  retained taxpayer {nombre completo, NIT, valor acreditado o pagado,
  monto de la retención} and the art. 15 anexo adds {domicilio fiscal,
  NIT o ID personal, concepto, renta} for facturas especiales — both
  visible as declaration detail. (FR-070, FR-071)
## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.4 +
§C); question text verbatim from the register (abbreviated where noted).
This file owns GOQ-96/97/98/99 (mechanics half) and cites kin GOQ-01/06/14
plus the S-GT2-resolved GOQ-118/119/120 — never re-opening the resolved
findings. Nothing outside this register is treated as an open question;
new gaps are flagged to the controller as non-OQ notes (no invented ids).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-96 (owned): "RetWeb manual provenance: 51_ prints 'noviembre 2024' not 'v3'; 52_ undated; 54_ no form version." Affects FR-031 (inventory rows: only 52_ of the seven IVA manuals is in corpus — mechanics never asserted from out-of-corpus manuals) and every 51_/52_-sourced mechanics row (secondary-provenance discipline; the 49_ portal listing dates 2024-11-14…2025-01-31 carried as the only manual dating). | no | GT synthesis wave S-GT4 → acquisition queue (six remaining role manuals + fresh portal listing) | open |
| OQ-002 | GOQ-97 (owned): "53_ roster: verify 8,447 count + 25 OCR-concat rows vs fresh download; NO agent-type column — type attribute must come from RTU/SAT calificación." Affects FR-032 (saas seed: defect-flagged, NIT-verified, category-less; agent-type attribute external). | no | GT synthesis wave S-GT4 → fresh roster download + RTU/SAT calificación source (acquisition queue) | open |
| OQ-003 | GOQ-98 (owned; E1-kin): "Constancia document-type mapping: no DTE-type code for retention constancias anywhere; are constancias a FEL DTE family member? (W-GT1 kin — E1/E2.)" Affects FR-069 (emission renders PDFs by número de constancia; the system assumes NO DTE type). In-file note: the 48_ catalog prints a Constancia de Retención del IVA code SAT-2229 (T1 LB-005) while 51_ shows ISR constancias only as system-generated PDFs — whether the ISR constancia has any form code at all is likewise unprinted; both questions ride this GOQ. | no | GT synthesis wave S-GT4 ↔ e-invoicing wave (E1/E2 DTE taxonomy) | open |
| OQ-004 | GOQ-99 (owned; mechanics half): "Deadline qualifiers: 50_ constancia delivery 'primeros (5) días' WITHOUT 'hábiles' (vs the 10-day ISR rule's 'hábiles') — legal qualifier needs LAT." Statutory half ANSWERED in taxation/04 §7 (GT-TAX-FR-142 qualifier registry: LAT/28_ qualifiers transcribed exactly per instrument) — this file owns the mechanics half only: FR-053/FR-055 store the 50_ prints verbatim and the engine never adds or removes a qualifier. | no | GT synthesis wave S-GT4 (mechanics half; statutory half resolved S-GT2) | open |
| OQ-005 | GOQ-01 (kin; register lists TX1/TX2/TX3 freeze): "Post-2018 consolidated Ley IVA 27-92 text: … art. 54 B/BIS nomenclature …". Affects FR-048 (statutory-agent path — 52_ prints "54 B" [sic]; the path stands either way per R59) and the FR-035 SAT-2320 10-día variant (R47 GOQ-01-context note riding GT-TAX-FR-107; statutory = 15 días hábiles uniformly per R26/GT-TAX-FR-106 — never frozen here). Register row cited kin; acquisition unchanged (DCA Edición Legal / accountant). | no | GT synthesis wave S-GT2 → acquisition queue (shared; this file consumes the kin rows only) | open |
| OQ-006 | GOQ-06 (kin; register lists TX3, F2 rate catalog): "5% IVA-retention additions (Pequeño suppliers ≥ Q2,500.01; Agropecuario on total factura) + 1.5% 'valor total' qualifier vs the D-20-2006/AG 425-2006 matrix — reconcile vs LIVA art. 54-bis text (GOQ-01 kin) before freezing the retention-rate catalog." Affects FR-039/FR-040/FR-041 (render-only consumption of the secondary-print-pending CSV rows — never frozen, never re-keyed as statutory here). | no | GT synthesis wave S-GT2 → acquisition queue (LIVA art. 54-bis text; this file renders only) | open |
| OQ-007 | GOQ-14 (kin; register lists F-cluster deadline CRs): "Accountant asks pending: calendario perpetuo vencimiento windows per NIT last-digit (JSF transcription, owner browser; atlas.com.gt cross-check only)…". Affects FR-053/FR-055/FR-034/FR-035 deadline engines: día-hábil/vencimiento resolution consumes the T1 ingestion surface (GT-FIN-FR-024); with no ingested vintage, no deadline object is generated and the gap is flagged — never invented. | no | GT synthesis wave S-GT4 → accountant track / owner-browser JSF transcription (W6; T1 owns the surface) | open |
| OQ-008 | GOQ-118 (S-GT2-resolved kin; register lists F6, TX3): "AG 425-2006 art. 4 vs 'art. 9' (64_ analysis) for the multi-group retention rule — instrument IS in corpus (79_); re-verify article contents at synthesis." RESOLVED S-GT2 (taxation/03 §7): art. 4 = Sistema-de-Retenciones procedure, art. 9 = dualidad rule — both citations correct, R52 dissolved. Cited here kin-only (FR-038's per-activity dualidad rendering rides the resolved finding); never re-opened. | no | GT synthesis wave S-GT2 (resolved; register annotation) | resolved |
| OQ-009 | GOQ-119 (S-GT2 modeling-call kin; register lists F6, TX3): "Dualidad same-invoice co-application: Criterios 1-2 state 65% (exporter quality) + 15% (second quality) on the same object without reconciling co-application; operative % per factura = SAT's Sistema de Retenciones — modeling call at synthesis." Modeling call MADE S-GT2 (taxation/03 FR-084/085): per-quality retention at per-activity statutory rates, configuration-driven dated data, per-factura % via the Sistema model with prorrateo; FR-038 renders the dualidad CSV rows (status secondary-print-pending, "regimes unnamed on the page") under that call — textual tension remains a deployment-configuration decision. | no | GT synthesis wave S-GT2 (modeling call recorded; textual tension open) | open |
| OQ-010 | GOQ-120 (S-GT2-recorded kin; register lists F6, TX6): "Retención-omission multa basis: CT art. 91 (65_) vs CT art. 94 num. 7 (64_) — verify vs current consolidated CT." Recorded UNRESOLVED S-GT2 (taxation/06 LB-026, both texts verbatim, no winner; evaluation keys on the infraction committed). Cited here because FR-058's rectificación multa is a distinct (procedural) multa — the system shall never source a multa amount from this file's corpus; sanction rows remain taxation/06 property pending the consolidation. | no | GT synthesis wave S-GT2 → record standing; resolve only with a newer CT consolidation | open |
