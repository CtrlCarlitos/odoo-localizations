# GT — Fiscal reporting — LET electronic books & Informe Electrónico de Compras y Ventas

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster F4: the SAT **Sistema
de Libros Electrónicos Tributarios —LET—** (electronic tax books system) user
manuals — `57_` (Régimen de Pequeño Contribuyente), `58_` (IVA General) and
`82_` (Regímenes Especiales del IVA) — plus `59_`, the **Informe Electrónico
de Compras y Ventas** (Electronic Purchase/Sales Report) manual for
contribuyentes Especiales. It owns: the book-architecture map per regime (one
combined *libro de compras y ventas* (purchases-and-sales book) for Pequeño
Contribuyente and each of the three especial/electrónico regimes; TWO separate
books per *establecimiento* (establishment) for IVA General, which generates
NO declaration — its *resumen* (summary) is only "insumo" (input) for the
external monthly IVA filing); the feed model (immutable FEL ventas feed,
inclusion-by-selection compras feed closable empty, FYDUCA Transferencia/
Adquisición with the rectified-discard anti-duplication rule, DUCA
Importaciones, the paper-document modules and their scoping, auto-detected
*constancias de retención* (retention certificates)); the cierre/resumen/folio
surfaces including the one-time immutable *último folio* (last folio) capture;
the in-system declaration generation (SAT-2046 for PC; masked form numbers for
the especial/electrónico regimes); the report inventories; the
  electrónico-regime 4%-within-10-*días hábiles*/5% tariff rule (a rate rule,
  NOT a filing deadline; statute-anchored to D-27-92 art. 54 "E" and
  time-boxed 2019 → 2025-08-09 — LB-026); the Informe Electrónico attestation flow (auto DTE
search, two FEL-coverage questions, *carga masiva* (mass upload) with its
100%-processed gate, PDF *constancia*, SAT-side *en/fuera de tiempo*
(on/over time), full-flow rectificación); and the cross-cutting guards (all
record-level layouts are images — never guessed; no LET-creating resolution
number printed anywhere; the R48 RTN/Honduras glossary defect; the undated
manuals).

It is the F4 half of the fiscal-reporting contract. Statutory regime
parameters are owned by the S-GT2 taxation files and consumed here by exact
FR id (12% → GT-TAX-FR-006; art. 57 "D" statutory ancestor → GT-TAX-FR-045;
PC Q150,000/5% → GT-TAX-FR-046/051; ROS 5%/7% → GT-TAX-FR-159; Utilidades 25%
→ GT-TAX-FR-152) — never re-derived. The earlier-era PC book procedure `61_`
is owned by Task 3 (`03_pequeno-libro-regime.md`) — paired here by FR id, two
dated layers never merged. Form REGISTRY identities are owned by Task 1
(`01_form-inventory-channels.md`). The RetWeb operating system is Task 2's;
the FEL DTE emission stack and the anulación blocker semantics are the
e-invoicing wave's (GT-EINV-FR-210 cited outcome-only).

It does **not** cover: statutory regime parameters or sanction values
(taxation/01/02/05/06 — all GT-TAX-FR ids); the 55_/61_ PC chain and its
form-drift ledger (Task 3); the form registry itself (Task 1); the SAT-2390
devolución channel (Task 5); the Criterios interpretive layer (Task 6); the
Código de Comercio books model and the dual-track habilitación model (future
S-GT5 C2 — this file records only the printed LET-side bridge with a
cross-ref pointer); and any LET record-level field layout (all images —
GOQ-105 hard blocker; layout acquisition is a pending task, never guessed
here).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble — fiscal
reporting): **manuals are PRIMARY for MECHANICS, SECONDARY for statutory
parameters**. **LET record-level layouts are ALL images — NEVER guess a field
layout** (GOQ-105/EVID-473 = hard blocker for any export-layout FR; layout
re-capture is an acquisition task, already fed to DOWNLOAD_QUEUE rev 7).
`57_`/`58_`/`82_` print **no version/date string** (GOQ-104) — every practice
row below carries that provenance caveat; `59_` is dated **diciembre 2023**.
**No LET-creating/regulating SAT resolution is printed anywhere** (GOQ-106) —
hooks only. R48 (binding): the 58_ glossary "RTN" = Honduras registry [sic]
entry is a print defect — ignore it; model NIT only. Statutory values live in
the S-GT2 taxation files — consumed by exact id. All quotes verified verbatim
against `gt/.extractions/57-59_82_LET_informe.evidence.md` (EVID-451..475)
and the 57_/58_/82_/59_ committed text layers. Dated rows follow D15/D16
(cite together); deadline surfaces carry GOQ-14 kin.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 57_ identity/scope: "Manual — Sistema de Libros Electrónicos Tributarios —LET— — Elaborado por Departamento de Normatividad de Atención al Contribuyente. Intendencia de Atención al Contribuyente" / "…afiliados al Impuesto al Valor Agregado —IVA— Régimen de Pequeño Contribuyente… facilitar el registro de los documentos tributarios emitidos y recibidos por los contribuyentes en el libro de compras y ventas, así como la generación del formulario SAT-2046 «IVA Pequeño Contribuyente»" / NO version/date string printed anywhere (GOQ-104) | LET for Pequeño Contribuyente = a single combined compras-y-ventas book with in-system generation of the SAT-2046 declaration; no other book type exists for this regime; undated print | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via `gt/.extractions/57_SAT_LET_Pequeno_Manual.pdf.txt`) | pp.1-2 cover + Introducción (EVID-451) |
| LB-002 | 57_ Requisitos + Aclaraciones: "1 Contar como mínimo con un establecimiento en estado Activo. 2 Contar con habilitación de libros computarizados de compras y de ventas para Pequeño Contribuyente en estado Activo.…" / "Todos los campos con (*) dentro del sistema son obligatorios (se debe ingresar información)." / "En la parte de las ventas y/o servicios prestados, visualizaras [sic] reportadas todas las facturas electrónicas que hayas emitido durante el mes, por lo que, no podrás realizar ningún cambio." / "En la parte de compras y/o servicios adquiridos, se te muestran las facturas electrónicas emitidas a tu nombre, por lo que, debes seleccionar los documentos que quieres incluir. El cierre del libro lo puedes realizar sin haber seleccionado ninguna factura de compras." | Entry gate = active establecimiento + active computerized-books habilitación; ventas feed read-only/immutable (all month's FEL pre-reported); compras feed inclusion-by-selection, closable empty; (*) = the only printed field-level validation | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via txt) | pp.3, 6 (EVID-452) |
| LB-003 | 57_ period/feed/papel: "Selecciona Año, Mes y Aceptar." / "Si al seleccionar el período este corresponde a uno generado previamente, el sistema te mostrará un mensaje indicando si deseas modificar el registro de este período…" / "El sistema te muestra todas las FEL emitidas en el período seleccionado. En caso de que no te las muestre, selecciona el botón Refrescar…" / "Si cuentas con resoluciones de documentos en papel en estado activo en el período seleccionado, el sistema te muestra el apartado Detalle de Documentos en Papel Emitidos…" / "…apartado Detalle de Documentos en Papel Recibidos y se desplegará el botón Ingresar Documento…" | Monthly (Año+Mes) periods, re-generable/reopenable by prompt; FEL feed auto-shown and refreshable; parallel manual paper modules (emitidos + recibidos) shown only while paper resolutions are active in the period | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via txt) | pp.9-14 (EVID-453) |
| LB-004 | 57_ cierre sequence: "Si realizas el cierre sin movimiento, se te consultará: Usted no ha registrado ventas, ¿Desea cerrar ventas y/o servicios prestados sin movimiento?…" / "En caso de no reportar compras para el período, el sistema muestra el mensaje «Usted no ha registrado compras, ¿Desea cerrar compras y/o servicios recibidos sin movimiento?»…" / "Se muestra en la pantalla el Resumen del Libro de Compras y Ventas para el Pequeño Contribuyente" / "NOTAS: Si cuentas con la declaración del período presentada y solo necesitas tu libro de compras y ventas para tener el registro al día, no debes de generar otro formulario, tu proceso termina con la generación del resumen." / "El sistema detecta las constancias de retención que has recibido en el período y te muestra el rubro…" / "Si es la primera vez que usas el libro, el sistema te solicitará que ingreses el número del último folio utilizado, no podrás modificar este datos [sic] posterior a su resguardo." | Fixed sequence cierre ventas → cierre compras → resumen, each side closable sin movimiento; resumen-only (bookkeeping without new declaration) is a valid terminal state; constancias de retención auto-detected as a resumen rubro; first use captures último folio immutably | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via txt) | pp.12-15 (EVID-454) |
| LB-005 | 57_ SAT-2046 generation: "Para generar la declaración presiona el botón GENERAR FORMULARIO SAT-2046." / "Se te mostrará el número de Formulario y Acceso que el sistema te generó." / "El sistema te solicitará que ingreses la fecha en que realizarás la presentación del formulario…" / "Si el valor a pagar es igual a cero «0», el sistema te solicitará la fecha de nacimiento o constitución para que puedas presentarlo desde el LET." / "Puedes hacer la presentación en la banca en línea o dirigirte a Declaraguate e imprimir la Boleta SAT-2000 y presentarlo en ventanillas bancarias." | In-system SAT-2046 generation with system-assigned formulario+acceso numbers, user-declared presentation date, zero-pay identity check (birth/incorporation date), payment via banca en línea or boleta SAT-2000; NO deadline rule printed (GOQ-107) | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via txt) | p.16 (EVID-455) |
| LB-006 | 57_ reports: "Encontrarás las opciones Reporte de Libro de Compras y Ventas para Pequeño Contribuyente, Reporte de Compras por Proveedores Pequeño Contribuyente y Reporte de Ventas por Cliente Pequeño Contribuyente…" / "NOTA: Únicamente te muestra los años y meses en los que realizaste el cierre y generación del resumen del libro." | Three reports (libro + compras-por-proveedor + ventas-por-cliente), restricted to closed periods; download via printer icon (format unprinted — images, GOQ-105) | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via txt) | pp.17-20 (EVID-456) |
| LB-007 | 57_ glosario: "Asignación de folios: Función automática que realiza el sistema LET, reconociendo el número de hojas habilitadas por el contribuyente, de conformidad con el artículo 5 numeral 4 de la ley de Timbres Fiscales y de Papel Sellado Especial para Protocolos." / "Régimen de Pequeño Contribuyente: Persona individual o jurídica cuyo monto de venta de bienes o prestación de servicios no exceda de ciento cincuenta mil Quetzales (Q.150,000.00) en un año calendario, cuya tarifa aplicable… es del 5% de forma mensual. Sus facturas no generan derecho a crédito fiscal y únicamente debe llevar el libro de compras y ventas habilitado… Capítulos V y VI del Decreto 27-92…" | Secondary regime print: Q150,000 calendar-year cap, 5% monthly, no crédito fiscal, single habilitated book, Capítulos V-VI D27-92; folio assignment automatic against hojas habilitadas under Ley de Timbres Fiscales art. 5 num. 4 | `gt/sources/57_SAT_LET_Pequeno_Manual.pdf` (via txt) | p.22 Glosario (EVID-457) |
| LB-008 | 58_ identity/scope: "…contribuyentes… afiliados al… IVA— en el Régimen General, exceptuado [sic] aquellos inscritos con tipo de contribuyente Profesional Liberal… la generación del libro de compras y servicios adquiridos y del libro de ventas y servicios prestados." / Objetivos: "Mostrar como generar el resumen de compras y ventas que sirve de insumo para el llenado de la declaración mensual del IVA General." / NO version/date string (GOQ-104) | LET-IVA General = TWO separate books (ventas/servicios prestados + compras/servicios adquiridos), Profesional Liberal excluded; generates NO declaration — the resumen is only insumo for the monthly IVA General filing made elsewhere | `gt/sources/58_SAT_LET_IVAGeneral_Manual.pdf` (via `gt/.extractions/58_SAT_LET_IVAGeneral_Manual.pdf.txt`) | pp.1-2, 5 (EVID-458) |
| LB-009 | 58_ Requisitos: "1 Contar como mínimo con un establecimiento en estado Activo. 2 Contar con libros habilitados de forma computarizada de compras y de ventas en estado Activo. 3 Aplica para personas individuales o jurídicas afiliadas al… IVA— Régimen general e Impuesto Sobre la Renta —ISR— Régimen Opcional Simplificado Sobre Ingresos de Actividades Lucrativas (exceptuando… Profesional Liberal) o Régimen de las Actividades Lucrativas." | LET-General eligibility couples IVA General with ISR Opcional Simplificado (5%/7%) or Utilidades de Actividades Lucrativas (25%); same habilitación + establecimiento preconditions | `gt/sources/58_SAT_LET_IVAGeneral_Manual.pdf` (via txt) | p.6 (EVID-459) |
| LB-010 | 58_ ventas book: "En el libro de ventas y/o servicios prestados, debes seleccionar los campos que se te piden, de lo contario [sic contrario] no te permitirá que realices el cierre del libro." / "5 Selecciona Tipo de Libro, Año, Mes e Ingresar." / "El sistema te muestra el apartado Transferencia con FYDUCAS." / "NOTAS: El botón Selección Múltiple te permite seleccionar por bloques las FEL." / "El sistema te muestra todas las FYDUCAS emitidas en el período seleccionado… selecciona el botón Refrescar…" / "El botón te permite descartar las FYDUCAS que han sido rectificadas y no se duplique la información." | Ventas = FEL emitidas (block-selectable) + FYDUCAS emitidas (Transferencia con FYDUCAS) with an explicit discard-rectified-FYDUCAS anti-duplication control; cierre de ventas BLOCKED until requested fields are complete (stricter than PC) | `gt/sources/58_SAT_LET_IVAGeneral_Manual.pdf` (via txt) | pp.3, 10-12 (EVID-460) |
| LB-011 | 58_ compras book: "El sistema te muestra el apartado Adquisición con FYDUCAS." / "…todas las FYDUCAS recibidas en el período… Refrescar…" / "El sistema te muestra el apartado Importaciones." / "…todas las DUCAS recibidas en el período… Refrescar…" / "Si deseas reportar una compra de un vehículo del modelo de 2 años anteriores al año en curso, selecciona el botón Ingresar Documento del apartado Documentos en Papel." | Compras book aggregates FOUR feeds: FEL recibidas + FYDUCAS recibidas (Adquisición) + DUCAS (Importaciones, auto-loaded) + Documentos en Papel scoped to vehicle purchases of model year up to 2 years before the current year | `gt/sources/58_SAT_LET_IVAGeneral_Manual.pdf` (via txt) | pp.15-17 (EVID-461) |
| LB-012 | 58_ cierres/folio/reports/establecimiento: "Si realizas el cierre sin movimiento… «¿Desea realizar cierre de ventas sin movimiento?»…" / "Si es la primera vez que usas el libro, el sistema te solicitará que ingreses el número del último folio utilizado, no podrás modificar este datos [sic]…" / "Encontrarás las opciones Libros de Ventas y/o Servicios Prestados para IVA General, Libros de Compras y/o Servicios Adquiridos para IVA General, Reporte de Clientes del Libro de Ventas… y Reporte de Proveedores del Libro de Compras…" / "Selecciona Año, Mes, Establecimiento y Buscar." / "La opción Establecimiento se te solicitará únicamente para el reporte de Libro de Compras… y Libro de Ventas…" | Same sin-movimiento/último-folio mechanics as PC; FOUR reports; the two book reports are queried per Establecimiento — General book records carry an establecimiento dimension | `gt/sources/58_SAT_LET_IVAGeneral_Manual.pdf` (via txt) | pp.12, 17, 20-21 (EVID-462) |
| LB-013 | 58_ glosario: "Régimen General del IVA: …período de liquidación mensual, gravado con una tasa del 12% con base al Decreto Número 27-92…" / "Régimen Opcional Simplificado…: …período de liquidación mensual… los tipos impositivos establecidos son el 5% y 7% con base al Decreto 10-2012…" / "Régimen Sobre las Utilidades…: …período de liquidación trimestral… una de las opciones establecidas en el artículo 38 del Decreto 10-2012…, el tipo impositivo es del 25%. Artículos del 14 al 42 del Decreto 10-2012…" / "RTN: Registro tributario nacional, sirve para identificar contribuyentes tanto personas naturales como jurídicas en el territorio de Honduras." / "VE: Ventas por exportación." / "FYDUCA: Factura y Declaración Única Centroamericana." | Cross-regime secondary prints: 12% mensual (D27-92); ROS 5%/7% mensual (D10-2012); Utilidades trimestral 25% with art. 38 option fixed per annual period (arts. 14-42). DEFECT (R48): "RTN" defined as the Honduras registry [sic] — ignore; Guatemala's identifier is the NIT | `gt/sources/58_SAT_LET_IVAGeneral_Manual.pdf` (via txt) | p.23 Glosario (EVID-463) |
| LB-014 | 82_ identity/scope: "…pone a disposición de los contribuyentes afiliados al… IVA—, en alguno de los regímenes siguientes: Especial de Contribuyente Agropecuario, Electrónico de Pequeño Contribuyente y Electrónico Especial de Contribuyente Agropecuario; …registro de los documentos tributarios… en el libro de compras y ventas, así como la generación de la declaración que corresponda." / NO version/date string (GOQ-104); generated form number masked "00000000" (GOQ-109) | LET-Regímenes Especiales serves THREE regimes with a single combined compras-y-ventas book each and in-system generation of the regime-appropriate declaration (form number NOT printed — masked) | `gt/sources/82_SAT_LET_RegEspeciales_Manual.pdf` (via `gt/.extractions/82_SAT_LET_RegEspeciales_Manual.pdf.txt`) | pp.1-2, 8 (EVID-464) |
| LB-015 | 82_ Requisitos + Aclaraciones: "1 Contar como mínimo con un establecimiento en estado Activo. 2 Contar con habilitación de libros computarizados de compras y ventas en estado Activo. 3 Aplica para los contribuyentes afiliados al… IVA— en alguno de los regímenes siguientes: ➢ Especial de Contribuyente Agropecuario, ➢ Electrónico de Pequeño Contribuyente y ➢ Electrónico Especial de Contribuyente Agropecuario." / same Aclaraciones as 57_: ventas "no podrás realizar ningún cambio" / compras by selection, cierre emptiable / "(*)" obligatorios | Identical eligibility gate and identical data asymmetry as 57_: the two combined-book populations (PC + RegEspeciales) share ONE LET interaction model — one engine, regime flavors | `gt/sources/82_SAT_LET_RegEspeciales_Manual.pdf` (via txt) | pp.3, 6 (EVID-465) |
| LB-016 | 82_ flow-to-declaration (PC-mirror): "…Si al seleccionar el período este corresponde a uno generado previamente…" / "…todas las FEL emitidas/recibidas en el período… Refrescar…" / "Si cuentas con documentos en papel que requieras reportar, selecciona el apartado Detalle de Documentos en Papel Recibidos…" / "El sistema detecta las constancias de retención… te muestra el rubro…" / "Si es la primera vez que usas el libro… el número del último folio utilizado…" / "Para generar la declaración presiona el botón Generar Formulario." / "Se te mostrará el número de formulario y acceso que el sistema te generó." (masked "00000000") / "Si el valor a pagar es igual a cero «0»… fecha de nacimiento o constitución…" / "…Declaraguate e imprimir la Boleta SAT-2000…" | Full PC-mirror flow (periods, FEL feeds, constancias, folio, zero-pay, SAT-2000/banca) with ONE printed difference: paper module described for Recibidos only (electronic regimes issue FEL by definition); form number masked | `gt/sources/82_SAT_LET_RegEspeciales_Manual.pdf` (via txt) | pp.10-15 (EVID-466) |
| LB-017 | 82_ glosario (Especial Agropecuario): "Régimen Especial de Contribuyente Agropecuario: Persona individual que desarrolle actividades de producción y comercialización en el sector agropecuario, cuyo monto de ventas no exceda los tres millones de Quetzales (Q.3,000,000.00) dentro del año fiscal…, cuya tarifa… es del 5% de forma mensual. Sus facturas no generan derecho a crédito fiscal y únicamente debe llevar el libro de compras y ventas habilitado… Capítulo VIII del Decreto 27-92…" | Secondary print of the (non-electrónico) Especial Agropecuario regime: persona individual, agro producción/comercialización, ≤ Q3,000,000 per año fiscal, 5% mensual, no crédito fiscal, single book; statutory cite Cap. VIII D27-92 | `gt/sources/82_SAT_LET_RegEspeciales_Manual.pdf` (via txt) | p.21 Glosario (EVID-467) |
| LB-018 | 82_ glosario (electrónico regimes): "Régimen Electrónico de Pequeño Contribuyente y Régimen Electrónico Especial de Contribuyente Agropecuario: Persona individual para el caso de los que desarrolle [sic] actividades… agropecuario y persona individual o jurídica para los contribuyentes que se acojan al Régimen Electrónico de Pequeño Contribuyente, quienes deben registrar una cuenta bancaria ante SAT, emitir facturas electrónicas en todas sus ventas y por las cuales no generaran [sic] derecho a crédito fiscal. La tarifa aplicable… es del 4% de forma mensual si presenta la declaración dentro de los primeros 10 días hábiles del mes inmediato siguiente al mes vencido, posterior a esos días deben de tributar por el 5%. Capítulo IX del Decreto 27-92…" | THE deadline-linked tariff rule of the electrónico regimes: 4% monthly if the declaración is filed within the first 10 días hábiles of the following month, else 5%; preconditions: bank account registered with SAT, FEL-mandatory sales, no crédito fiscal; Electrónico PC = individual o jurídica, Electrónico Agro = individual; Cap. IX D27-92 — a RATE rule, not a LET filing deadline (GOQ-107); statute-anchored by LB-026: D-27-92 art. 54 "E" (added D-7-2019 art. 8), time-boxed 2019 → 2025-08-09 (derogated by D-31-2024 art. 25) | `gt/sources/82_SAT_LET_RegEspeciales_Manual.pdf` (via txt) | p.21 Glosario (EVID-468) |
| LB-019 | 59_ identity + hook: "Manual del Usuario — Informe Electrónico de Compras y Ventas — Guatemala, diciembre 2023" / "El presente manual brinda soporte al contribuyente catalogado como Especial para el cumplimiento de la obligación establecida en el artículo 57 “D” del Decreto Número 27-92 del Congreso de la República de Guatemala." / "Requerimientos Básicos…: Contar con acceso a la Agencia Virtual; Estar actualizado en RTU Digital; Aplica a contribuyentes clasificados como Especiales" / "Ingresa tu usuario: NIT del Contribuyente Especial" | The Informe Electrónico = a Contribuyente Especial obligation hung on art. 57 "D" D27-92 (only printed hook); dated diciembre 2023; prerequisites Agencia Virtual + RTU Digital current; login user = the Especial's NIT; the reform instrument adding literal D is not in the corpus (GOQ-108) | `gt/sources/59_SAT_InformeComprasVentas_Manual.pdf` (via `gt/.extractions/59_SAT_InformeComprasVentas_Manual.pdf.txt`) | pp.1-3 (EVID-469) |
| LB-020 | 59_ attestation flow: "…los campos para ingresar los parámetros de consulta del período a presentar. a. Mes… b. Año… c. Consultar…" / "Al seleccionar la opción Consultar, el sistema busca de forma automática que existan registros de Documentos Tributarios Electrónicos (DTE) emitidos y/o recibidos, al encontrar registros mostrará la pregunta siguiente ¿Todas sus ventas las factura a través del Régimen de Factura Electrónica en Línea –FEL-? Selecciona la opción SI para continuar…" / "…¿Todas sus compras locales reciben DTE generados a través del Régimen de Factura Electrónica en Línea –FEL-? Selecciona la opción SI… Si posee compras realizadas por medio de documentos pre impresos, realice lo indicado en el numeral 3.2" | The informe is a monthly (Mes+Año) attestation flow, not a data upload: SAT auto-searches the period's DTE and the taxpayer answers two FEL-coverage questions (all sales FEL?; all local purchases FEL-DTE?); SI/SI = 100%-FEL direct path; NO on purchases diverts to the paper-upload path (LB-021) | `gt/sources/59_SAT_InformeComprasVentas_Manual.pdf` (via txt) | pp.3-6 §§1-3.1 (EVID-470) |
| LB-021 | 59_ carga masiva: "3.2.3. …selecciona la opción Carga Masiva de Documentos Tributarios en papel para cargar los documentos pre impresos." / "3.2.4. …debes ingresar los parámetros siguientes: a. Mes al que corresponde la carga… b. Año…" / "3.2.5. …cargar el archivo seleccionando la opción a. Subir Archivo" / "3.2.6. Elige el botón Cargar…" / "3.2.8. El sistema te enviará la notificación sobre el resultado de la carga realizada al correo electrónico registrado en la Agencia Virtual." / "3.2.9. …puedes consultar el resultado… “Consulta Archivos de Carga Masiva”" / "a. Si los registros fueron procesados con éxito en su totalidad puedes continuar con la presentación del Informe. b. Si los registros no fueron procesados debes volver a realizar la carga corrigiendo los errores." | Non-FEL local purchases reconciled via period-scoped mass upload; result by e-mail + queryable; HARD GATE: ALL records must process successfully before the informe proceeds — partial success forces corrected re-upload; file format/extension/layout NOT printed (GOQ-108) | `gt/sources/59_SAT_InformeComprasVentas_Manual.pdf` (via txt) | pp.7-12 §§3.2.1-3.2.12 (EVID-471) |
| LB-022 | 59_ sin-registros/outputs/rectificación: "3.3.1 Al seleccionar la opción Consultar el sistema busca de forma automática que existan registros de DTE…, al no encontrar registro de documentos se mostrará en pantalla el mensaje siguiente:" / "4.1. El sistema muestra el siguiente mensaje de confirmación de la presentación del Informe en tiempo o fuera de tiempo según corresponda." / "4.2. …Éxito de presentación… opciones: a. Rectificar Informe b. Descargar Constancia (En formato PDF.)" / "4.4. El sistema enviará al correo registrado… una notificación con la confirmación de la presentación del Informe…" / "5.2. Al seleccionar la opción Rectificar Informe, el sistema muestra en pantalla el mensaje siguiente y seleccionarás aceptar para continuar con la rectificación." / "5.4. Con la acción anterior, iniciarás el proceso a partir del numeral 2 de este manual." | Sin-registros month = valid informe (confirm + proceed); the SYSTEM classifies the filing en tiempo / fuera de tiempo (rule not printed — GOQ-107); outputs = PDF constancia + e-mail confirmation; Rectificar Informe restarts the whole flow from the parameters step | `gt/sources/59_SAT_InformeComprasVentas_Manual.pdf` (via txt) | pp.13-17 §§3.3, 4, 5 (EVID-472) |
| LB-023 | NEGATIVE (all four manuals): the only field-level strings reaching the text layer: "Todos los campos con (*) dentro del sistema son obligatorios" (57_/82_ p.3; 58_ p.3 "de llenado obligatorio") / "NIT:" "Nombre:" (login bars) / "completa las casillas que se te piden" (57_ p.14, 82_ p.13) / resumen captions only — book grids, resumen totals, papel-entry forms, carga-masiva template and report column sets are ALL images | No column-by-column book layout (field name, type, format, required flag) exists in any text layer — layouts must NEVER be guessed; export-layout surfaces stay blocked until a layout source is acquired (GOQ-105/EVID-473) | `gt/sources/57_…/58_…/82_…/59_…` (via txt layers) | throughout, e.g. 57_ pp.10-16; 58_ pp.11-17; 82_ pp.10-15; 59_ pp.4-15 (EVID-473) |
| LB-024 | Printed-citation inventory (complete, all four manuals): "Capítulos V y VI del Decreto 27-92…" (57_ glosario) / "Capítulo VIII del Decreto 27-92" + "Capítulo IX del Decreto 27-92" (82_ glosario) / "artículo 57 “D” del Decreto Número 27-92…" (59_ p.2) / "Decreto Número 27-92 … y sus reformas" (58_ glosario) / "el artículo 5 numeral 4 de la ley de Timbres Fiscales y de Papel Sellado Especial para Protocolos" (three glosarios, idéntico) / "Decreto 10-2012…" + "artículo 38" + "Artículos del 14 al 42" (58_ glosario) / forms: "SAT-2046 «IVA Pequeño Contribuyente»" (57_), "Boleta SAT-2000" (57_ p.16, 82_ p.15) | The hunting map: EVERY instrument cited across the four manuals; NO SAT resolution number creating/regulating LET is printed anywhere — hooks only (GOQ-106); never assert a resolution number | `gt/sources/57_…/58_…/82_…/59_…` (via txt) | 57_ pp.16, 22; 58_ pp.5, 23; 82_ p.21; 59_ p.2 (EVID-474) |
| LB-025 | Paper-books bridge (three manuals): "Contar con habilitación de libros computarizados de compras y de ventas … en estado Activo" (Requisitos) / "Si es la primera vez que usas el libro, el sistema te solicitará que ingreses el número del último folio utilizado, no podrás modificar este datos posterior a su resguardo." / "Asignación de folios: Función automática que realiza el sistema LET, reconociendo el número de hojas habilitadas por el contribuyente, de conformidad con el artículo 5 numeral 4 de la ley de Timbres Fiscales…" (glosarios, identical) | LET is the electronic continuation of the authorized computerized-books regime: entry requires an active habilitación; LET assigns folios automatically against the hojas habilitadas (Timbres art. 5 num. 4); first use imports the último folio irreversibly — the flow as printed here, S-GT5 C2 cross-ref pointer only | `gt/sources/57_…/58_…/82_…` (via txt) | 57_ pp.6, 15, 22; 58_ pp.6, 12, 17, 23; 82_ pp.6, 14, 21-22 (EVID-475) |
| LB-026 | 99_ D-27-92 consolidated print, Cap. IX — art. 54 "E", the statute behind the electrónico 4%/5% rule: "ARTÍCULO 54 "E". Régimen Electrónico de Pequeño Contribuyente y Régimen Electrónico Especial de Contribuyente Agropecuario. *" / "Los contribuyentes que soliciten su incorporación a este régimen, en todas sus ventas están obligados a emitir factura electrónica de pequeño contribuyente o contribuyente agropecuario, según corresponda, y estarán afectos a un tipo impositivo reducido del cuatro por ciento (4%) en sustitución del cinco por ciento (5%) establecido en los artículos 47 y 54 "A"." / "El contribuyente deberá registrar ante la Administración Tributaria una cuenta bancaria y autorizar a esta para que el décimo día hábil de cada mes calendario, debite automáticamente de dicha cuenta el monto equivalente a aplicar el tipo impositivo del cuatro por ciento (4%) sobre el total de ingresos reportados en el mes inmediato anterior, de conformidad con las facturas electrónicas emitidas para tal efecto." / "El contribuyente que no tenga los fondos suficientes para cubrir el impuesto de este régimen en la fecha establecida, presentará la declaración dentro de los días que faltan para finalizar el mes calendario, pagando un tipo impositivo del cinco por ciento (5%) sobre el valor de los ingresos reportados en el mes inmediato anterior, de conformidad con las facturas electrónicas emitidas para tal efecto, sin que ello implique su exclusión del Régimen Electrónico de Pequeño Contribuyente y Régimen Especial de Contribuyente Agropecuario." / footnote: "*Adicionado por el Artículo 8 del Decreto Número 7-2019 del Congreso de la República." | Interpretation: (i) the 4%-within-10-días-hábiles rule = D-27-92 art. 54 "E" (added D-7-2019 art. 8) — NOT a LET deadline: GOQ-107's TARIFF-not-LET ruling is now statute-anchored (4% EN SUSTITUCIÓN del 5% of arts. 47/54 "A", collected by automatic bank debit on the décimo día hábil; 5% fallback only on insufficient funds, declared within the days remaining in the month, no exclusion); (ii) the whole 54 "E"/"F" electrónico pair was TIME-BOXED 2019 → 2025-08-09, derogated by D-31-2024 art. 25 (cross-ref 85_/W-GT7 EVID-819 — registry cross-note, NOT printed in 99_): every 4%/5% tariff row in this file carries valid_from 2019 / valid_to 2025-08-09 (D15 discipline) and must NOT be modeled as a current live rate; (iii) post-derogation electronic-filing incentive state = corpus-silent (OQ-008). GOQ-146 resolved: the Cap. VIII/IX primary texts are now in the corpus via 99_ (cap. VIII verbatim at EVID-1047) | `gt/sources/99_IVA_27-92_Consolidado_2019.pdf` (via `gt/.extractions/99_100_IVA_Consolidado2019_D4-2012.evidence.md`) | 99_ pp.42-43 (EVID-1051; GOQ-146 verdict EVID-1053; consolidation horizon EVID-1032; derogation cross-ref 85_ EVID-819) |

## 3. Functional Requirements

### 3.1 Book architecture per regime & provenance guards (shared map)

- **GT-FIN-FR-103:** The system shall implement the LET **regime-architecture
  map** as shared configuration: **Régimen de Pequeño Contribuyente** and each
  of the three **Regímenes Especiales** — *Especial de Contribuyente
  Agropecuario*, *Electrónico de Pequeño Contribuyente*, *Electrónico
  Especial de Contribuyente Agropecuario* — keep **ONE combined libro de
  compras y ventas** per month with in-system declaration generation; **IVA
  General** keeps **TWO separate books** — *Libro de Ventas y/o Servicios
  Prestados* and *Libro de Compras y/o Servicios Adquiridos* — per month per
  establecimiento and generates **NO declaration form**: its resumen is only
  the "insumo" for the external monthly IVA General filing. The PC combined
  book is the SAME statutory obligation Task 3 models from `61_`
  (GT-FIN-FR-086/090 — paired, never duplicated). (LB-001; LB-008; LB-014;
  EVID-451, EVID-458, EVID-464; cross-ref GT-FIN-FR-086, GT-FIN-FR-090;
  D15/D16)
- **GT-FIN-FR-104:** The eligibility gate shall be modeled per population as
  printed: (i) all three manuals require **at least one establecimiento in
  estado Activo** AND an **active habilitación de libros computarizados de
  compras y de ventas**; (ii) LET-IVA General additionally couples the IVA
  regime with the ISR dimension — **Régimen Opcional Simplificado Sobre
  Ingresos de Actividades Lucrativas or Régimen de las Actividades
  Lucrativas (Utilidades)** — and **excludes** the *Profesional Liberal*
  taxpayer type; (iii) LET-Regímenes Especiales requires affiliation in one
  of the three named regimes. The fiscal-regime matrix shall therefore carry
  both IVA and ISR regime dimensions for the General gate. (LB-002; LB-009;
  LB-015; EVID-452, EVID-459, EVID-465)
- **GT-FIN-FR-105:** The provenance model shall record that `57_`, `58_` and
  `82_` print **no version/date string** (unlike `56_` enero-2024 and `59_`
  diciembre-2023): currency of all three LET manuals is unverifiable from the
  documents and later UI/flow changes are invisible to this corpus — every
  practice row sourced from them carries this caveat (GOQ-104), and no 57_/
  58_/82_-sourced mechanic is asserted as the verified current procedure
  without live verification. (LB-001; LB-008; LB-014; EVID-451, EVID-458,
  EVID-464; GOQ-104 → OQ-001; D15/D16)
- **GT-FIN-FR-106:** NEGATIVE FR (hard blocker): all LET record-level
  layouts — book grid columns, resumen totals, papel-entry form casillas,
  carga-masiva file template, report column sets — are **images with no text
  layer**; the system shall **not assert any field layout** for any LET book,
  resumen, paper-entry form, carga-masiva template or report, and shall keep
  every export-layout surface blocked until a layout source is re-captured
  (acquisition watcher already queued). Only the printed mechanics (buttons,
  sequences, feeds, gates) are modeled here. (LB-023; EVID-473;
  GOQ-105 → OQ-002)
- **GT-FIN-FR-107:** The normative-basis guard shall encode that **no
  LET-creating/regulating SAT resolution number is printed anywhere** in the
  four manuals: the system shall never assert a LET resolution number, and
  the printed-citation inventory (D27-92 Capítulos V/VI/VIII/IX + art. 57
  "D"; D10-2012 arts. 14-42 and 38; Ley de Timbres Fiscales art. 5 num. 4;
  forms SAT-2046 and Boleta SAT-2000) shall be stored as the hunting map for
  the resolution acquisition (GOQ-106). (LB-024; EVID-474;
  GOQ-106 → OQ-003)
- **GT-FIN-FR-108:** R48 guard: the 58_ glossary entry defining "RTN" as the
  **Honduras** registry [sic] is a SAT print defect — the system shall ignore
  the RTN entry entirely and model the **NIT** only; no RTN concept shall
  enter the model from this source. (LB-013; EVID-463; R48)

### 3.2 Feed model (book data assembly & ingestion)

- **GT-FIN-FR-109:** The ventas feed shall be **immutable/read-only** for the
  combined-book populations: all FEL issued during the month are auto-loaded
  and pre-reported with **no edit and no delete** ("no podrás realizar ningún
  cambio"); the feed is refreshable ("Refrescar"). The same immutability
  applies to the General ventas FEL feed (block-selectable via Selección
  Múltiple). Pairing note: a document's appearance in LET is a SAT-exclusive
  **anulación blocker** per GT-EINV-FR-210 — modeled outcome-only, with no
  pre-verification promised. (LB-002; LB-003; LB-010; LB-015; EVID-452,
  EVID-453, EVID-460, EVID-465; cross-ref GT-EINV-FR-210)
- **GT-FIN-FR-110:** The compras feed shall be **inclusion-by-selection**:
  FEL recibidas (issued to the taxpayer's name) are surfaced for the user to
  select which documents to include, and the cierre may be completed **with
  zero purchase documents selected** ("El cierre del libro lo puedes
  realizar sin haber seleccionado ninguna factura de compras"). (LB-002;
  LB-015; EVID-452, EVID-465)
- **GT-FIN-FR-111:** The book period model shall key sessions to **calendar
  month (Año + Mes)**; selecting a previously generated period prompts
  whether to **modify/reopen** that period's record — periods are
  re-generable/rectifiable by prompt, in all three LET manuals. (LB-003;
  LB-016; EVID-453, EVID-466)
- **GT-FIN-FR-112:** The paper-document modules shall be scoped as printed:
  (i) PC — **Detalle de Documentos en Papel Emitidos** and **Recibidos**,
  shown only while the taxpayer's paper-document resolutions remain active in
  the period (manual entry via Ingresar Documento); (ii) Regímenes
  Especiales — **Recibidos only** (the electronic regimes issue FEL by
  definition; no Papel Emitidos apartado is printed); (iii) IVA General —
  the Documentos en Papel module scoped to **vehicle purchases of model
  year up to 2 years before the current year** ("compra de un vehículo del
  modelo de 2 años anteriores al año en curso"). (LB-003; LB-011; LB-016;
  EVID-453, EVID-461, EVID-466)
- **GT-FIN-FR-113:** The IVA General feed set shall add customs feeds on top
  of FEL: **ventas** = FEL emitidas (Selección Múltiple block selection) +
  **FYDUCAS emitidas** (*Transferencia con FYDUCAS* apartado); **compras** =
  FEL recibidas + **FYDUCAS recibidas** (*Adquisición con FYDUCAS*) +
  **DUCAS** (*Importaciones* apartado, auto-loaded) — every auto-feed
  refreshable. (FYDUCA = Factura y Declaración Única Centroamericana;
  DUCA = Declaración Única Centroamericana.) (LB-010; LB-011; EVID-460,
  EVID-461)
- **GT-FIN-FR-114:** The anti-duplication control shall implement the
  printed rectified-FYDUCA discard: the user shall be able to **discard
  rectified FYDUCAS** so that rectified originals do not double-count
  ("descartar las FYDUCAS que han sido rectificadas y no se duplique la
  información") on both the Transferencia and Adquisición feeds. (LB-010;
  EVID-460)
- **GT-FIN-FR-115:** The field-completion gate shall implement BOTH printed
  strictness levels: (i) universal — fields marked "(*)" are required; (ii)
  IVA General — the **cierre de ventas is blocked** until all requested
  fields are selected/completed ("de lo contario [sic contrario] no te permitirá que
  realices el cierre del libro") — a hard validation stricter than the PC/
  especiales closable-empty rule (FR-110). (LB-002; LB-010; LB-015;
  EVID-452, EVID-460, EVID-465)
- **GT-FIN-FR-116:** The constancias surface shall record **SAT-side
  auto-detection**: the system detects the *constancias de retención*
  received in the period and surfaces them as a rubro in the resumen
  (verifiable via the "Constancias de retención recibidas en este período"
  link) — for PC and the Regímenes Especiales; no equivalent General print
  exists (recorded as a documented absence, never invented). (LB-004; LB-016;
  EVID-454, EVID-466)

### 3.3 Cierre, folio bridge & reports

- **GT-FIN-FR-117:** The monthly cycle shall implement the fixed sequence
  **cierre de ventas → cierre de compras → resumen**, with each side
  closable **sin movimiento** (explicit confirm prompt per side); a
  **resumen-only terminal state** is valid when the period's declaration was
  already presented elsewhere — book and declaration are separable
  ("tu proceso termina con la generación del resumen"). (LB-004; LB-012;
  EVID-454, EVID-462)
- **GT-FIN-FR-118:** The folio-continuity bridge shall implement the printed
  flow: first use of a book captures the **número del último folio
  utilizado**, immutable after saving ("no podrás modificar este datos [sic]
  posterior a su resguardo"); folio assignment is automatic against the
  **hojas habilitadas** (*enabled sheets*) under **Ley de Timbres Fiscales y
  de Papel Sellado Especial para Protocolos art. 5 num. 4**; the **active
  computerized-books habilitación is the adoption precondition** (FR-104).
  The dual-track habilitación model (RM autorización vs SAT habilitación) is
  owned by the future S-GT5 COA wave (cluster C2) — **cross-ref pointer
  only**, never modeled here. (LB-002; LB-007; LB-025; EVID-452, EVID-457,
  EVID-475; S-GT5 C2 cross-ref pointer)
- **GT-FIN-FR-119:** The report inventory shall implement: PC and
  Regímenes Especiales — **three reports** (Reporte de Libro de Compras y
  Ventas + Compras por Proveedores + Ventas por Cliente); IVA General —
  **four reports** (Libros de Ventas y/o Servicios Prestados + Libros de
  Compras y/o Servicios Adquiridos + Reporte de Clientes + Reporte de
  Proveedores), the two book reports queried **Año + Mes + Establecimiento**
  — hence General book records shall carry an **establecimiento dimension**.
  All reports are restricted to **closed periods only** (cierre + resumen
  completed). Output column layouts are images — blocked per FR-106.
  (LB-006; LB-012; EVID-456, EVID-462)

### 3.4 Declaration generation, tariff rule & deadline surface

- **GT-FIN-FR-120:** The PC declaration surface shall implement in-system
  **SAT-2046** generation: "GENERAR FORMULARIO SAT-2046" from the resumen;
  system-assigned **número de Formulario + número de Acceso**; user-declared
  **fecha de presentación**; **zero-pay path** requiring fecha de
  nacimiento (individual) or constitución (jurídica) as identity check;
  payment via **banca en línea** or **Declaraguate → Boleta SAT-2000** at
  bank windows. Form identity and validity are consumed from Task 1
  (GT-FIN-FR-006/015); the era ledger is Task 3's (GT-FIN-FR-093) — this FR
  owns the 57_-era generation mechanics. (LB-005; EVID-455; cross-ref
  GT-FIN-FR-006, GT-FIN-FR-015, GT-FIN-FR-093, GT-FIN-FR-097)
- **GT-FIN-FR-121:** The Regímenes Especiales declaration surface shall
  implement the identical in-system mechanics ("Generar Formulario",
  form+acceso numbers, user date, zero-pay identity flow, SAT-2000/banca
  rails) — but the generated form number is **MASKED in the manual**
  ("la declaración que corresponda"; "00000000"): the system shall assert NO
  form number from 82_ itself. Form identities resolve only from the Task 1
  registry: **Electrónico de Pequeño Contribuyente = SAT-2241**
  (GT-FIN-FR-006, 48_ registry row "IVA-Régimen Electrónico de Pequeño
  Contribuyente"); Especial de Contribuyente Agropecuario and Electrónico
  Especial de Contribuyente Agropecuario remain unresolved (GOQ-109).
  (LB-014; LB-016; EVID-464, EVID-466; GOQ-109 → OQ-006; cross-ref
  GT-FIN-FR-006)
- **GT-FIN-FR-122:** The electrónico-regime tariff shall be stored as dated
  rows implementing the deadline-driven effective rate: **4% monthly if the
  declaración is presented within the first 10 días hábiles of the month
  immediately following the taxed month; 5% thereafter** (Capítulo IX
  D27-92 as printed in the 82_ glossary). ANCHORED + SUNSET (W-GT8,
  LB-026): the primary text is now in the corpus — the rule = **D-27-92
  art. 54 "E"** (added D-7-2019 art. 8; `99_`): 4% EN SUSTITUCIÓN del 5%
  of arts. 47/54 "A", collected by automatic bank debit on the **décimo
  día hábil**, with the 5% fallback on insufficient funds — a TARIFF,
  never a LET deadline (GOQ-107 statute-anchored). The whole 54 "E"/"F"
  electrónico pair was TIME-BOXED **2019 → 2025-08-09**, derogated by
  D-31-2024 art. 25 (85_ cross-ref): every 4%/5% tariff row carries
  valid_from 2019 / valid_to 2025-08-09 (D15) and shall NEVER be modeled
  as a current live rate; the post-derogation electronic-tariff state is
  corpus-silent (OQ-008). The declaration engine shall resolve the
  effective rate as-of the filing date (snapshot-on-write per D15/D16;
  the GOQ-104 currency caveat still applies to the 82_ print).
  (LB-018; LB-026; EVID-468, EVID-1051, EVID-1053; D15/D16)
- **GT-FIN-FR-123:** The deadline surface shall encode GOQ-107 exactly:
  `57_` and `58_` print **no** cierre/declaration deadline; the ONLY
  printed deadline anywhere is the electrónico-regime 4%/5% rule of
  FR-122 — **a rate rule, NOT a LET filing deadline**; the informe's
  en/fuera de tiempo classification (FR-128) is SAT-side with the rule
  unprinted. The system shall create **no LET/informe deadline object**
  from these manuals; actual deadlines are external (GOQ-14 kin — consumed
  via Task 1's calendar ingestion surface GT-FIN-FR-024 when a calendar
  vintage arrives, never invented). (LB-005; LB-018; LB-022; EVID-455,
  EVID-468, EVID-472; GOQ-107 → OQ-004; cross-ref GT-FIN-FR-024)
- **GT-FIN-FR-124:** The glossary statutory prints shall be stored as
  secondary rows anchored by exact taxation id, never re-derived: PC
  **Q150,000** cap (GT-TAX-FR-046), PC **5% mensual** (GT-TAX-FR-051),
  facturas **no generan crédito fiscal** (GT-TAX-FR-064), single book
  (GT-TAX-FR-066); General **12% mensual** (GT-TAX-FR-006); ROS **5% y 7%
  mensual** (GT-TAX-FR-159); Utilidades **trimestral 25%** with the art. 38
  option fixed per annual period (GT-TAX-FR-152, GT-TAX-FR-150 regime
  lifecycle). The Especial Agropecuario print (**persona individual; ≤
  Q3,000,000 año fiscal; 5% mensual; no crédito fiscal; Cap. VIII D27-92**)
  keeps its anchor-pending flag (no taxation id yet), while the
  electrónico-regime prints (**cuenta bancaria ante SAT; FEL-only
  sales; 4%/5% — FR-122**) are statute-anchored (W-GT8, LB-026): the
  D27-92 Cap. VIII/IX primary texts are now in the corpus via the `99_`
  consolidated print (54 "E"/"F" EVID-1051/1052; cap. VIII EVID-1047) —
  the 4%/5% rows anchor to art. 54 "E" with valid_from 2019 /
  valid_to 2025-08-09 (derogated by D-31-2024 art. 25), historical-only,
  never asserted as verified current law. (LB-007; LB-009; LB-013; LB-017; LB-018; EVID-457, EVID-459,
  EVID-463, EVID-467, EVID-468; cross-ref GT-TAX-FR-006, GT-TAX-FR-046,
  GT-TAX-FR-051, GT-TAX-FR-064, GT-TAX-FR-066, GT-TAX-FR-150,
  GT-TAX-FR-152, GT-TAX-FR-159)

### 3.5 Informe Electrónico de Compras y Ventas (59_, contribuyentes Especiales)

- **GT-FIN-FR-125:** The informe obligation surface shall record: actor =
  **contribuyente Especial**; legal hook as printed = **art. 57 "D" del
  Decreto Número 27-92**; prerequisites = Agencia Virtual access + RTU
  Digital current + Especial classification; login user = the Especial's
  **NIT**. The statutory ancestor is consumed from GT-TAX-FR-045 (23_
  texto ≤ D-10-2012: semi-annual "cada seis meses, como máximo", per-
  counterparty NIT/name/amount/date) — the manual instead shows a MONTHLY
  flow (FR-126): this periodicity tension is recorded, not reconciled; the
  reform instrument adding/modifying literal D is not in the corpus
  (GOQ-108). The informe's relation to LET books/declarations is NOT
  printed — no connection shall be asserted. (LB-019; EVID-469;
  GOQ-108 → OQ-005; cross-ref GT-TAX-FR-045)
- **GT-FIN-FR-126:** The informe presentation flow shall implement the
  monthly (Mes + Año) attestation state machine: on Consultar, the system
  **auto-searches the period's DTE (emitidos y/o recibidos)**; with records
  found, exactly two FEL-coverage questions gate progression — (1) "¿Todas
  sus ventas las factura a través del Régimen de Factura Electrónica en
  Línea –FEL-?" and (2) "¿Todas sus compras locales reciben DTE generados a
  través del Régimen de Factura Electrónica en Línea –FEL-?" — SI/SI
  continues to presentation; a NO on question (2) diverts to the carga
  masiva path (FR-127). The **sin-registros path is valid**: no DTE found →
  confirmation message → the informe proceeds (nil-month attestation).
  (LB-020; LB-022; EVID-470, EVID-472)
- **GT-FIN-FR-127:** The carga masiva de documentos en papel shall
  implement: period-scoped upload (Mes + Año → Subir Archivo → Cargar);
  result notified by **e-mail to the Agencia Virtual registered address**
  and queryable via **Consulta Archivos de Carga Masiva**; and the HARD
  GATE: presentation may continue **only when records were processed
  successfully in their entirety** — any errored record blocks the informe
  and forces a corrected re-upload ("debes volver a realizar la carga
  corrigiendo los errores"). The upload file format/extension/layout is
  NOT printed (GOQ-108; layout blocker FR-106 applies — no template
  asserted). (LB-021; EVID-471; GOQ-108 → OQ-005)
- **GT-FIN-FR-128:** The informe outputs shall implement: success screen
  with **Rectificar Informe** and **Descargar Constancia** actions; the
  **constancia de presentación in PDF format**; an **e-mail confirmation
  notice**; and the SAT-side timeliness classification **"en tiempo o
  fuera de tiempo según corresponda"** surfaced as a received state — the
  underlying deadline rule is not printed and shall not be modeled
  (FR-123/GOQ-107). (LB-022; EVID-472)
- **GT-FIN-FR-129:** The rectification flow shall implement full-flow
  re-run: selecting **Rectificar Informe** (with its acceptance prompt)
  restarts the process **from the parameters step** for the period — the
  prior filing is replaced by the re-executed flow, including the DTE
  search, both coverage questions and any carga-masiva gate. (LB-022;
  EVID-472)

### 3.6 Era pairing with Task 3

- **GT-FIN-FR-130:** The era-pairing ledger shall record that `61_` (Task 3,
  GT-FIN-FR-090/091: the ≥ ~2018-11 procedure — Ingreso de Factura, FEL
  auto-load both sides, cierre order, 20-line folios) and `57_` (this file:
  the undated LET-manual mechanics — Refrescar feeds, sin-movimiento
  prompts, constancias rubro, SAT-2046 generation) are **two dated layers
  of the SAME obligation**, never silently merged; drift between them
  (e.g. 61_'s 20-lines-per-folio rule unprinted in 57_; 57_'s constancias
  rubro unprinted in 61_) is recorded as layer differences, and any
  current-procedure claim requires live verification (GOQ-101/GOQ-104
  kin). (LB-001; LB-004; EVID-451, EVID-454; cross-ref GT-FIN-FR-090,
  GT-FIN-FR-091; D15/D16)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + provenance +
as-of qualifier; snapshot-on-write. This file stores NO statutory constants —
regime parameters are taxation-owned and consumed by FR id (FR-124 anchors);
what is stored here is the regime-architecture map, the feed/cierre/folio
operational surfaces, the form-mask rows, the tariff dated row (anchored,
historical 2019 → 2025-08-09 — LB-026), the informe state machine and the guard rows. No field-layout
entity exists (FR-106 blocker — layouts stay unasserted).

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.let.regime.architecture | regime_key / book_count / book_scope / declaration_mode / establecimiento_dimension / isr_coupling / pl_excluded | selection pc-general-especial_agro-electronico_pc-electronico_agro / integer 1-2 / char / selection in_system-none_insumo / boolean / selection ros-utilidades-none / boolean | PC + 3 especiales = 1 combined book + in-system declaration; General = 2 books + NO declaration (resumen = insumo) | FR-103, FR-104 |
| l10n_gt.let.gate | establecimiento_activo / habilitacion_activa / regime_test | boolean / boolean / char | tripartite gate printed identically in 57_/58_/82_ | FR-104, FR-118 |
| l10n_gt.let.manual.provenance | file / version_date_printed / caveat | selection 57_-58_-82_-59_ / char (none·diciembre 2023) / char | GOQ-104: 57_/58_/82_ undated — caveat on every practice row; 59_ dated | FR-105 |
| l10n_gt.let.feed | side / source / load_mode / selectable / immutable / refresh / discard_rectified | selection ventas-compras / selection fel-fyduca-duca-papel / selection auto-manual / boolean / boolean / boolean / boolean | ventas FEL immutable; compras FEL by selection; FYDUCA Transferencia/Adquisición; DUCA Importaciones; papel scoped | FR-109, FR-110, FR-112, FR-113, FR-114 |
| l10n_gt.let.period | key=año+mes / regenerable / reopen_prompt | char / boolean / boolean | monthly sessions; previously generated period reopenable by prompt | FR-111 |
| l10n_gt.let.papel.scope | population / modules / condition | selection pc-especiales-general / list emitidos-recibidos / char | PC both; especiales recibidos only; General vehicle model ≤ 2 years prior | FR-112 |
| l10n_gt.let.cierre | sequence / sin_movimiento / fields_gate / constancias_rubro / resumen_only_terminal | char=ventas→compras→resumen / boolean per side / selection asterisk-general_hard / boolean / boolean | constancias = PC + especiales print only | FR-115, FR-116, FR-117 |
| l10n_gt.let.folio | first_use_capture / ultimo_folio / immutable / hojas_habilitadas / timbres_art | boolean / char / boolean=true / char / char=art. 5 num. 4 | paper-book continuity lock; S-GT5 C2 pointer only | FR-118 |
| l10n_gt.let.report | set / params / closed_periods_only / establecimiento_param | selection pc_especiales-3-general-4 / char list / boolean / boolean | book reports queried Año+Mes+Establecimiento (General) | FR-119 |
| l10n_gt.let.declaration | generate / form_ref / acceso_number / presentation_date / zero_pay_id_check / rails | boolean / char / char / date / selection nacimiento-constitucion / list banca_en_linea-sat_2000 | PC = SAT-2046 (T1 GT-FIN-FR-006/015); General = NONE | FR-120, FR-121 |
| l10n_gt.let.form.mask | regime / form_identity / source / status | selection especial_agro-electronico_pc-electronico_agro / char / char / selection resolved-masked | electrónico PC = SAT-2241 (48_ via T1); agro pair masked (GOQ-109) | FR-121 |
| l10n_gt.let.tariff.electronico | rate_early / window / rate_late / valid_from / valid_to / provenance / anchor_status | decimal=0.04 / char=4% via automatic bank debit on the décimo día hábil (art. 54 "E") / decimal=0.05 / date=2019 (D-7-2019 art. 8) / date=2025-08-09 (D-31-2024 art. 25) / char=99_ art. 54 "E" (EVID-1051) + 82_ glosario / selection anchored_historical | deadline-driven effective rate while the regime lived; snapshot-on-write at filing date; HISTORICAL — never a current live rate (LB-026) | FR-122 |
| l10n_gt.let.glossary.print | term / printed_value / anchor_ref / status | char / char / char (GT-TAX-FR id) / selection anchored-pending | Q150k→046; 5%→051; 12%→006; ROS→159; Utilidades→152; electrónico 4%/5% → anchored art. 54 "E" (LB-026; 2019→2025-08-09); Q3M·agro 5% = pending | FR-124 |
| l10n_gt.informe | actor / hook / prerequisites / login_user / periodicity_printed / statutory_ancestor_ref | char=Especial / char=art. 57 "D" D27-92 / list agencia_virtual-rtu_digital / char=NIT / char=monthly flow (manual) / char (GT-TAX-FR-045: semi-annual ≤ D-10-2012) | periodicity tension recorded, not reconciled | FR-125 |
| l10n_gt.informe.attestation | period / auto_dte_search / q_ventas_fel / q_compras_fel / sin_registros_path | char=mes+año / boolean / boolean / boolean / boolean | SI/SI direct; NO compras → carga masiva; nil month valid | FR-126 |
| l10n_gt.informe.carga | period / upload / result_email / consulta / gate_pct / format_status | char / char=Subir Archivo→Cargar / boolean / boolean / integer=100 / selection unprinted | 100%-processed hard gate; format = GOQ-108 + FR-106 blocker | FR-127 |
| l10n_gt.informe.output | constancia_pdf / email_notice / timeliness | boolean / boolean / selection sat_side_en-fuera | deadline rule unprinted (GOQ-107) | FR-128 |
| l10n_gt.informe.rectificacion | restart_step / replaces | char=numeral 2 (parameters) / char=last filing | full-flow re-run | FR-129 |
| l10n_gt.let.guard | key | char list | layouts_all_images (GOQ-105); no_let_resolution (GOQ-106); r48_no_rtn; rate_not_deadline (GOQ-107); undated_manuals (GOQ-104); masked_forms (GOQ-109); 61_57_layer_split; deadline_external_goq14_kin | FR-105..FR-108, FR-121..FR-123, FR-130 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = feed
ingestion, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Wave defaults
for this file (binding): book data assembly + feed selection + folio/
último-folio capture = `odoo`; carga-masiva 100% gate + informe state
machine + FEL-feed ingestion = `saas`; regime-architecture map + tariff
dated rows = `shared`. Model names stable across Odoo 17/18/19/20; no
version-specific behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-103 | shared | — (config data §4) | regime.architecture rows | One engine, regime flavors; PC book = same obligation as T3's 61_ layer |
| FR-104 | shared | — (config data §4) | gate rows | General gate reads both IVA + ISR regime dimensions (ROS/Utilidades); PL excluded |
| FR-105 | shared | — (config data §4) | manual.provenance rows | GOQ-104 caveat rides every 57_/58_/82_-sourced row |
| FR-106 | shared | — (guard/blocker) | layouts_all_images | Export-layout surfaces disabled until layout acquisition (DOWNLOAD_QUEUE rev 7) |
| FR-107 | shared | — (guard) | no_let_resolution | EVID-474 hunting map stored as provenance data |
| FR-108 | shared | — (guard) | r48_no_rtn | NIT-only; grep-able guard |
| FR-109 | saas | LET feed ingestion service | FEL emitidas feed + refresh | Immutable downstream (odoo renders read-only); anulación blocker = GT-EINV-FR-210 outcome-only |
| FR-110 | odoo | libro line model (compras selection surface) | include flag per FEL recibida | Cierre allowed with zero selections |
| FR-111 | odoo | libro session model | año/mes key + reopen prompt | Reopen = modify flow for generated periods |
| FR-112 | odoo | papel document entry surface | scope flags per population | PC emitidos+recibidos; especiales recibidos; General vehicle model ≤ 2 yrs |
| FR-113 | saas | LET feed ingestion service | FYDUCA Transferencia/Adquisición + DUCA Importaciones feeds | Refreshable; odoo renders selection surface |
| FR-114 | odoo | libro line model (FYDUCA discard action) | rectified-discard control | Anti-duplication over saas-ingested FYDUCA feed |
| FR-115 | odoo | libro cierre flow | (*) required fields + General cierre block | Two strictness levels per population |
| FR-116 | saas | constancias detection ingestion | constancias rubro data | Odoo renders the resumen rubro; General absence recorded |
| FR-117 | odoo | libro cierre/resumen flow | sequence + sin-movimiento prompts + resumen-only terminal | Book and declaration separable |
| FR-118 | odoo | folio register | último folio capture (immutable) + hojas habilitadas | Timbres art. 5.4 hook; S-GT5 C2 = pointer only |
| FR-119 | odoo | libro report actions | report set + params + closed-periods filter | Establecimiento dimension on General book records |
| FR-120 | odoo | declaration generation flow + saas transmission | SAT-2046 assembly + numbers + zero-pay + rails | Form identity from T1; era ledger from T3 (FR-093) |
| FR-121 | shared | — (config data §4) | form.mask rows | Electrónico PC = SAT-2241 (48_ via T1); agro pair never asserted (GOQ-109) |
| FR-122 | shared | — (config data §4 / CSV) | tariff.electronico dated rows | Effective rate resolved as-of filing date (D15/D16 snapshot); anchored art. 54 "E" (99_, LB-026); valid 2019→2025-08-09 — historical, never a current live rate |
| FR-123 | shared | — (guard) | deadline_external_goq14_kin | No deadline object from these manuals; calendar via T1 GT-FIN-FR-024 |
| FR-124 | shared | — (config data §4) | glossary.print rows | Anchored rows consume taxation ids; pending rows flagged (Cap. VIII/IX primary texts to acquire) |
| FR-125 | shared | — (config data §4) | informe obligation row | GT-TAX-FR-045 statutory ancestor; periodicity tension recorded |
| FR-126 | saas | informe state machine | DTE auto-search + coverage questions + paths | Nil-month attestation path included |
| FR-127 | saas | carga masiva service | upload + result notice + 100% gate | Gate = authoritative validation in core; template blocked (FR-106) |
| FR-128 | saas | informe output service | constancia PDF + e-mail + timeliness state | en/fuera de tiempo surfaced as received state only |
| FR-129 | saas | informe rectification flow | restart-from-parameters | Replaces the last filing for the period |
| FR-130 | shared | — (provenance ledger) | 61_/57_ layer rows | Drift recorded as layer differences; live verification pending |

## 6. Acceptance Criteria

- **AC-001:** Given the regime-architecture map, then Pequeño Contribuyente
  and each of the three especial/electrónico regimes resolve ONE combined
  compras-y-ventas book with in-system declaration generation, while IVA
  General resolves TWO books per establecimiento with NO declaration and a
  resumen marked "insumo" for the external monthly IVA filing; Profesional
  Liberal fails the General gate; the General gate passes only under ISR
  Opcional Simplificado or Utilidades. (FR-103, FR-104)
- **AC-002:** Given any practice row sourced from 57_/58_/82_, then it
  carries the undated-print caveat (GOQ-104) and none is asserted as
  verified current procedure; the 59_ rows carry "diciembre 2023".
  (FR-105, FR-125)
- **AC-003:** NEGATIVE — given every LET book/resumen/papel-form/carga-
  masiva/report surface, then no field layout, column set or file template
  is asserted anywhere in the product data (grep: no layout entity exists);
  export-layout actions are blocked pending layout acquisition. (FR-106,
  FR-119, FR-127)
- **AC-004:** Given the normative-basis guard, then no LET resolution number
  is asserted anywhere; the stored citation inventory contains exactly the
  printed hooks (D27-92 caps. V/VI/VIII/IX + art. 57 "D"; D10-2012 arts.
  14-42/38; Timbres art. 5 num. 4; SAT-2046; SAT-2000). (FR-107)
- **AC-005:** Given the 58_ glossary import, then no RTN field or Honduras
  registry concept enters the model — NIT only (R48). (FR-108)
- **AC-006:** Given a month's feeds, then ventas FEL are auto-loaded
  read-only (no edit/delete) and refreshable; compras FEL are
  inclusion-by-selection and the cierre completes with zero selections; in
  the General population, cierre de ventas is blocked until all requested
  fields are complete and rectified FYDUCAS are discardable without
  double-counting. (FR-109, FR-110, FR-113, FR-114, FR-115)
- **AC-007:** Given the papel modules, then PC shows Emitidos + Recibidos
  only while paper resolutions are active, the especiales population shows
  Recibidos only, and the General population accepts paper vehicle
  purchases of model year ≤ (current year − 2) and rejects older/other
  paper entries. (FR-112)
- **AC-008:** Given a first-use cierre, then the sequence runs ventas →
  compras → resumen with per-side sin-movimiento prompts; a resumen-only
  terminal state is accepted; constancias surface as a resumen rubro for
  PC/especiales; and the último folio is captured once and immutable
  thereafter. (FR-116, FR-117, FR-118)
- **AC-009:** Given the reports, then PC/especiales expose 3 and General 4
  report actions; only closed periods are selectable; the General book
  reports require Año + Mes + Establecimiento. (FR-119)
- **AC-010:** Given declaration generation, then PC generates the SAT-2046
  with system-assigned form/acceso numbers, user-declared presentation
  date, the zero-pay identity check and the banca/SAT-2000 rails; the
  especial/electrónico surface asserts NO form number from 82_ — the
  Electrónico PC row resolves SAT-2241 only via the Task 1 registry and
  the agro pair stays masked (GOQ-109). (FR-120, FR-121)
- **AC-011:** Given an electrónico-regime declaration filed within the
  first 10 días hábiles of the following month, then the effective rate
  resolves 4%; filed later, 5% (snapshot-on-write; anchored to art. 54 "E"
  per LB-026, dated valid_from 2019 / valid_to 2025-08-09 — historical
  only, never a current live rate); and given any deadline question, then
  no LET/informe deadline object exists beyond the external calendar
  surface — the 4%/5% row is labeled a rate rule, never a filing
  deadline. (FR-122, FR-123)
- **AC-012:** Given the glossary prints, then Q150k/5%/12%/ROS 5-7%/
  Utilidades 25% resolve their taxation anchors by exact id, the agro
  Q3,000,000/5% rows keep anchor-pending flags, and the electrónico rows
  resolve their statutory anchor (art. 54 "E", LB-026) with valid_from
  2019 / valid_to 2025-08-09 dating — never surfaced as current
  law. (FR-124)
- **AC-013:** Given an Especial running the informe, then Consultar
  triggers the DTE auto-search; SI/SI on both FEL-coverage questions
  proceeds; a NO on compras routes to carga masiva where presentation is
  blocked until 100% of records process successfully; the outputs are the
  PDF constancia + e-mail notice with en/fuera de tiempo surfaced as a
  SAT-side state; and Rectificar Informe re-runs the whole flow from the
  parameters step. (FR-126..FR-129)
- **AC-014:** Given the era ledger, then the 61_ layer (T3) and the 57_
  layer (this file) remain distinct dated rows with their differences
  recorded — never merged into a single "current" procedure. (FR-130)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.4);
question text verbatim from the register. This file OWNS GOQ-104/105/106/
107/108/109 (F4 rows) and GOQ-146 (electrónico-tariff anchor — row OQ-007,
resolved W-GT8). GOQ-14 (calendar ingestion) is consumed as kin via
Task 1's GT-FIN-FR-024. Nothing outside this register is treated as an open
question; new gaps are flagged to the controller as non-OQ notes (no
invented ids), except controller-directed OQ rows (OQ-008, W-GT8).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-104 (owned): "57_/58_/82_ print NO version/date (unlike 56_/59_) — LET manual currency unverifiable; later UI/flow changes invisible." Affects every mechanics row of this file (FR-103..FR-124, FR-130): values verified against the live LET portal before any current-procedure assertion; rides the same acquisition pass as the layout re-capture. | no | GT synthesis wave S-GT4 → acquisition queue (live LET portal verification) | open |
| OQ-002 | GOQ-105 (owned): "LET record-level layouts = ALL images (book grids, resumen totals, papel forms, carga-masiva templates, report columns) — layout acquisition REQUIRED before any export-layout CR; never guess. Same for 63_ group-header spans (column-letter list is the authoritative part)." This file owns the F4 half (FR-106 hard blocker; FR-119/FR-127 blocked surfaces); the 63_/F5 half of the register row is Task 5's. Layout re-capture already queued (DOWNLOAD_QUEUE rev 7). | yes (export-layout FRs only) | GT synthesis wave S-GT4 → acquisition queue (LET field-layout re-capture) | open |
| OQ-003 | GOQ-106 (owned): "No LET-creating/regulating SAT resolution printed anywhere (hooks only: D27-92 caps. V/VI/VIII/IX + art. 57 'D'; D10-2012 arts. 14-42; Timbres art. 5.4; EVID-474 hunting map) — normative basis hunt (normativa listing AJAX-gated). Carries the CT '69-kin' residual (R29)." Affects FR-107 (never assert a resolution number) and the file's LB provenance generally. | no | GT synthesis wave S-GT4 → acquisition queue (normativa listing; AJAX-gated) | open |
| OQ-004 | GOQ-107 (owned): "LET/informe deadlines: 57_/58_ print none; 82_ only the electrónico 4%-within-10-hábiles/5% tariff rule; 59_ marks en/fuera de tiempo without printing the rule — actual deadlines live outside these manuals." Affects FR-123 (no deadline object; GOQ-14 kin via GT-FIN-FR-024), FR-122 (rate-rule labeling), FR-128 (timeliness as received state). RESOLVED (W-GT8): the 4%/5% rule is statute-anchored as a TARIFF — D-27-92 art. 54 "E" (99_, LB-026) — never a LET deadline, sunset 2025-08-09 (D-31-2024 art. 25); actual deadlines = SAT Calendario flat per-obligation dates (103_ → 01/LB-017, consumed via GT-FIN-FR-024); the informe's en/fuera rule stays unprinted (received state per FR-128). | no | GT synthesis wave S-GT4 → resolved W-GT8 (99_ + 103_ acquisitions) | resolved (W-GT8) |
| OQ-005 | GOQ-108 (owned): "Informe (59_): the instrument adding art. 57 'D' + its obligation text (periodicity/deadline/sanction) not in corpus; carga-masiva file format/extension unspecified." Affects FR-125 (monthly-manual vs semi-annual statutory print GT-TAX-FR-045 tension unresolved), FR-127 (no upload template — also FR-106). | no | GT synthesis wave S-GT4 → acquisition queue (art. 57 "D" reform instrument) | open |
| OQ-006 | GOQ-109 (owned): "82_ masks the generated declaration number — which formulario per especial/electrónico regime (PC = SAT-2046 per 57_)?" Partially resolved from within the corpus: Electrónico PC = SAT-2241 per the 48_ registry (Task 1 GT-FIN-FR-006); the Especial Agropecuario and Electrónico Especial Agropecuario forms remain unknown — never asserted (FR-121). | no | GT synthesis wave S-GT4 → acquisition queue (form registry check / live portal) | open |
| OQ-007 | GOQ-146 (owned): "D-27-92 Cap. VIII/IX primary texts absent from corpus — fiscal-reporting/04's electrónico-tariff rows (4%/5% within 10 días hábiles) are anchor-pending on the tariff chapter itself (currently anchored to 82_ glossary print only)." RESOLVED (W-GT8, LB-026): the 99_ consolidated print carries Cap. IX arts. 54 "E"/"F" verbatim (EVID-1051/1052; cap. VIII at EVID-1047) — the 4%/5% tariff = art. 54 "E" (added D-7-2019 art. 8); FR-122 rows re-anchored and dated 2019 → 2025-08-09 (derogated by D-31-2024 art. 25, 85_ cross-ref). | no | GT synthesis wave S-GT4 → resolved W-GT8 (99_ acquisition) | resolved (W-GT8) |
| OQ-008 | Post-2025-08-09 electronic-tariff state: D-31-2024 art. 25 derogated the whole D-27-92 art. 54 "E"/"F" electrónico pair — whether any successor electronic-filing tariff/incentive exists after the D-31-2024 ICT cutover is corpus-silent; the 4%/5% rows are modeled historical-only (FR-122, LB-026) until an instrument is acquired. | no | GT synthesis wave S-GT4 → acquisition queue (post-D-31-2024 electronics regime) | open |
