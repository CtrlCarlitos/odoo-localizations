# GT — Fiscal reporting — SAT-2390 devolución de crédito fiscal (régimen general, ventas a exentas)

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster F5: the SAT-2390
electronic **Solicitud de Devolución de Crédito Fiscal del IVA, Régimen
General para contribuyentes que venden a entidades exentas** (electronic
IVA fiscal-credit refund request, general regime, for taxpayers selling to
exempt entities) — `62_` the Agencia Virtual filing walkthrough, and `63_`
the companion CSV-annex format spec. It owns: the channel identity and
eligibility surface (statutory entitlement consumed from taxation by exact
id); the request-object header model (RTU-fed data, per-form
domicilio/correo overrides, single *producto principal*); the CARTERA
lifecycle states; the claim-window engine (periods claimable only from the
IVA-declaration due date, up to 4 years later, aggregated exclusively
trimestral/semestral — dated rows); the per-period amount determination
against registered SAT-2237 IVA declarations ("Crédito Sujeto a Devolución
del Período" + default-0.00 "Crédito no Solicitado"); the Congelar freeze
gate; **THE cross-validation gate** (SAT compares the uploaded Libro de
Compras/Ventas CSV values against the declared crédito/débito fiscal of
the SAT-2237 declarations and rejects on mismatch — the verbatim error is
captured; this gate drives the export pipeline); the full CSV annex spec
authoritative from `63_` itself (naming, 2 header rows skipped, no totals
rows, compras 16 columns A-P with the mandatory payment block L-P and the
closed 17-value column-B document-type catalog, ventas 11 columns A-K with
explicit DEBITO FISCAL column I and the never-blank column K vocabulary);
the cross-cutting cell-format contract (all-TEXT cells, dd/MM/yyyy dates,
zero-fill, NC negative/ND positive, SERIE the only blank allowed, comma
ban, and the dated > Q2,500 NIT+ID rule from enero 2023); and the guard
rows (undated prints, no legal basis printed, container unknowns,
doc-type catalog oddities kept verbatim).

It does **not** cover: the statutory refund entitlement, channel matrix,
Q10,000 minimum, electronic 100% regime or export evidence pack — all owned
by S-GT2 taxation (`01_iva-core.md` GT-TAX-FR-025/031..037, consumed here
by exact id, never re-derived); the LET electronic books surfaces (Task 4,
`04_let-electronic-books.md` — cross-referenced by FR id; the "libros" the
cross-validation gate compares against); the form registry and the R58
outside-catalog marker (Task 1, GT-FIN-FR-017); the FEL DTE emission stack
and W-GT1 document-type taxonomy (`e-invoicing/01_document-types.md` —
GOQ-115 verification pointer only); the books data layer itself (future
S-GT5 — dependency noted on the export FRs); and the saldo/traslado
accounting mechanics (GT-TAX-FR-025).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble — fiscal
reporting): manuals are PRIMARY for MECHANICS, SECONDARY for statutory
parameters; and for the CSV annex spec **the authority is `63_` itself**
(the instructions document). `62_` cites **NO legal basis** anywhere
(GOQ-111) — the entitlement, the 4-year window and the
trimestral/semestral granularity are statutory matters owned by taxation
(`GT-TAX-FR-031/032/025`, consumed by exact id; the 4-year window mirrors
the statute of limitations per W-GT2 xref — never restated as law here).
Neither `62_` nor `63_` prints a date/version in its text layer (GOQ-110);
internal terminus: `63_` post-2023-01 (rule 4's "a partir de enero 2023").
`63_` pp.1/3 embed the two template tables as images whose text layers
extract interleaved: the clean **column-letter list is the authoritative
part; group-header spans are never transcribed** (GOQ-105 kin — register
row owned by Task 4's OQ-002, whose 63_/F5 half is discharged here by that
rule). OCR defects are kept verbatim with [sic], never corrected. All
quotes verified against `gt/.extractions/62-63_SAT-2390.evidence.md`
(EVID-481..490) and the `62_`/`63_` committed text layers. Dated rows
follow D15/D16 (cite together).

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 62_ identity + service label: "GUIA DEL USUARIO PARA LA UTILIZACIÓN DEL FORMULARIO ELECTRÓNICO SAT-2390" / "Formulario Electrónico, Solicitud de Devolución de Crédito Fiscal del IVA, Régimen General para contribuyentes que venden a entidades exentas" / "1. Ingresar al Portal de SAT https://portal.sat.gob.gt/portal/ ingresar al apartado de Agencia Virtual…" / "2. En “Agencia Virtual”, ingresar en el apartado de “Servicios” en la opción “Solicitud Dev. CF Reg Gral contribuyentes que venden a entes exentos”" / NO legal-basis citation printed anywhere (GOQ-111); NO version/date string (GOQ-110) | SAT-2390 = the electronic IVA fiscal-credit refund request under the general regime, addressed to taxpayers who sell to exempt entities; filed in Agencia Virtual under a service whose own label confirms the target population; undated procedural manual printing no legal basis | `gt/sources/62_SAT-2390_guia.pdf` (via `gt/.extractions/62_SAT-2390_guia.pdf.txt`) | p.1 title block + steps 1-2 (EVID-481) |
| LB-002 | 62_ CARTERA + attachments: "3. Le aparecerá la pantalla “CARTERA”, en donde se le proporciona información sobre las solicitudes de de volución [sic devolución] de crédito fiscal ingresadas por medio electrónico , mostrando el número de Solicitud, No. D ocumento [sic Documento] SAT, el período solicitado y el estado en el cual se encuentra cada solicitud; en el momento de la consulta, dicho estado puede ser; CONGELADO, EN PROCESO, RECIBIDO (GUARDADO), ADMITIDO, NO ADMITIDO, ASIGNADO Y RESUELTO, y por último la columna de Opciones, que muestra dos botones, uno de solicitud enviada y da la opción de imprimir, y otro botón que es el que se utiliza para adjuntar los archivos qu e [sic que] contienen el Libro de Compras y Libro de Ventas en formato CSV (delimitado por comas)." / "4. En el botón “Nueva Solicitud”, dar clic para indicar el llenado de un nuevo formulario SAT-2390." | Request portfolio screen (CARTERA) with columns request no., SAT document no., requested period, state; lifecycle states as printed: CONGELADO, EN PROCESO, RECIBIDO (GUARDADO), ADMITIDO, NO ADMITIDO, ASIGNADO Y RESUELTO (cardinality of the last entry ambiguous as printed — GOQ-112); per-request options: print sent request + attach the two CSV files (purchases book and sales book, comma-delimited) | `gt/sources/62_SAT-2390_guia.pdf` (via txt) | p.2 steps 3-4 (EVID-482) |
| LB-003 | 62_ header apartados a-d: "El formulario se divide en 6 apartados" / "a. Datos del Contribuyente: En este apartado el sistema mostrará la información que se encuentra registrada en el Registro Tributario Unificado, como: • NIT • Nombre del Contribuyente • Domicilio Fiscal (Puede ser modificado para este formulario, permite la opción de utilizar un domicilio fiscal diferente al registrado) • Correo Electrónico (Puede ser modificado para este formulario…) • Número de Teléfono y Extensión…" / "b. Datos del Representante Legal (Sí [sic Si] es persona Jurídica): …se mostrarán los representantes legales activos a la fecha… se deberá seleccionar el dato del Representante Legal que firmará la solicitud." / "c. Datos del Contador: El sistema mostrará datos según el Registro Tributario Unificado del contador que se encuentra registrado." / "d. Datos de la Solicitud: Deberá ingresar el producto principal que vende (solamente el nombre de un producto ejemplo Alcohol Medicinal, Med icamentos [sic Medicamentos], Servicios Médicos, etc.), dato que es importante para la realización de la auditoría." | Request header data model: taxpayer NIT/name auto-fed from the RTU (Registro Tributario Unificado — Unified Tax Registry); fiscal address and e-mail overridable for this form only; legal-entity filers must select the active legal representative who signs; accountant data auto-fed from RTU; exactly one main product name in free text — flagged as audit-relevant | `gt/sources/62_SAT-2390_guia.pdf` (via txt) | pp.2-3 step 5 literaras a-d (EVID-483) |
| LB-004 | 62_ period window: "En este mismo apartado el sistema muestra los campos para que el contribuyente elija los períodos que solicitará Devolución de Crédito Fiscal, dicha solicitud podrá solicitarse a partir del vencimiento de la presentación de las Declaraciones del IVA, es decir a partir de ese momento hasta 4 años después; la solicitud podrá presentarse únicamente en forma trimestral o semestral." | Period mechanics: a period becomes claimable only after its IVA declaration due date has passed; claims run up to 4 years after that point; aggregation granularity exclusively quarterly (trimestral) or semiannual (semestral) — no monthly or annual requests; the guide cites no statutory basis (GOQ-111; statutory mirror consumed from taxation) | `gt/sources/62_SAT-2390_guia.pdf` (via txt) | p.4 step 5d continuation (EVID-484) |
| LB-005 | 62_ determinación + freeze gate: "e. Determinación del monto de devolución de crédito fiscal solicitado: • La información de la columna “Número de Declaración SAT -2237 [sic SAT-2237]” y “Períodos Impo sitivos [sic Impositivos]”, se obtendrá d el [sic del] sistema las Declaraciones del Impuesto al Valor Agregado que se encuentren registradas en el Registro Tributario Unificado. • La información de la columna “Crédito Sujeto a Devolución del Período ” será ingresado por el contribuyente con el lápiz… y grabará cada valor hasta totalizar el monto solicitado. • “El Crédito no Solicitado” será utilizado solamente cuando el contribuyente considere rebajar al monto del Crédito Sujeto a Devolución del Período, de lo contrario debe quedar con valor 0.00." / "f. Declaración del Contribuyente: …declara y jura que los datos ingresados son verdaderos. / Tienes la opción de elegir dos botones : “Congelar” y “Cancelar”, si la información ingresada es correcta, al elegir Congelar la solicitud pasará a estado CONGELADO, y si el sistema detecta inconsistencias con el Representante Legal y el Contador, no permitirá congelar el formulario debiend o [sic debiendo] el contribuyente elegir el botón Cancelar y deberá iniciar nuevamente el proceso." | Amount determination per declared period: declaration numbers (form SAT-2237, IVA) and taxed periods pulled from the RTU's registered IVA declarations; the taxpayer manually enters Crédito Sujeto a Devolución del Período per row until totalling the requested amount; Crédito no Solicitado exists only to reduce the claim (default 0.00); sworn declaration; Congelar (freeze) fails on inconsistencies vs RTU legal-representative/accountant records → only option is Cancel and restart | `gt/sources/62_SAT-2390_guia.pdf` (via txt) | p.4 step 5 literaras e-f (EVID-485) |
| LB-006 | 62_ upload, cross-validation, ENVIAR, e-mail: "6. Al dar clic en el botón congelar el formulario cambiará a estado congelado, habilitando la opción de cargar los Libros de compras y Libro de Ventas (Ver Instrucciones previo a cargar los anexos del formulario electrónico, SAT -2390 [sic SAT-2390])…" / "7. El contribuyente selecciona archivo en formato CSV, si el archivo plano esta [sic está] guardado según las instrucciones, automáticamente le muestra la opción de CARGAR archivo." / "8. Al elegir cargar archivo, el sistema hace una comparación de los valores incluidos en Libros y Declaraciones. / Si los valores no coinciden, muestra el mensaje siguiente: “Los valores declarados como crédito y débito fiscales, no coinciden con los valores registrados en el Libro de Compras y Libro de Ventas”." / "9. Después de haber completado la carga de los Libros, debe elegir el botón ENVIAR…" / "10. El formulario queda registrado en la Administración Tributaria para su análisis , posteriormente el contribuyente recibirá mediante correo electrónico previamente registrado, la Notificación de que su solicitud ha sido recibida o no recibida…" | THE cross-validation gate: on upload, the system compares the values included in the uploaded books against the declarations and rejects on mismatch with the quoted message (declared crédito/débito fiscal vs Libro de Compras/Ventas values); sequence freeze → upload CSVs → ENVIAR → registered for analysis → e-mail notification (received / not received) to the previously registered address; step 6's parenthetical ties 62_ to 63_ (same-form annex instructions) | `gt/sources/62_SAT-2390_guia.pdf` (via txt) | pp.5-8 steps 6-10 (EVID-486) |
| LB-007 | 63_ identity + file mechanics: "INSTRUCCIONES, PREVIO A CARGAR LOS ANEXOS DEL FORMULARIO ELECTRÓNICO, SAT-2390, ARCHIVOS EN FORMATO CSV (Delimitados por Comas)." / rule 7: "Si solo se tiene una línea en el encabezado del libro , la línea 2 dejarla en blanco, tanto el Libro de Compras y Libro de Ventas. La línea 1 y 2 no se toman en cuenta en la carga del archivo ya que estas se han dejado para el encabezado, el sistema carga el archivo a partir de la línea 3 en adelante." / rule 8: "El Libro no debe llevar: Línea de SUBTOTAL o TOTAL, tanto el Libro de Compras y Libro de Ventas." / rule 11: "Guardar el archivo en formato .CSV, identificar los archivos con el nombre: SAT_MESAÑO_VENTAS.csv o SAT_MESAÑO_COMPRAS.csv. a) Libro de Compras: SAT_102017_COMPRAS.csv b) Libro de Ventas: SAT_102017_VENTAS.csv" / rule 12: "Previo a cargar los archivos en formato CSV… abrir el archivo con BLOC DE NOTAS, para cerciorarse que las columnas estén separadas por el signo coma (,)." / NO date/version printed in the text layer (GOQ-110); internal terminus post-2023-01 | Annex container contract: comma-delimited .CSV; rows 1-2 are headers and always skipped (system loads from row 3); one-line header ⇒ row 2 left blank; no SUBTOTAL/TOTAL rows anywhere; file name = SAT_<MM><AÑO>_COMPRAS.csv / _VENTAS.csv (example 102017 = month 10 of 2017 — one file per month per book); Notepad check confirms the comma delimiter | `gt/sources/63_SAT-2390_instrucciones_csv.pdf` (via `gt/.extractions/63_SAT-2390_instrucciones_csv.pdf.txt`) | pp.1-3 title + rules 7, 8, 11 y 12 (EVID-487) |
| LB-008 | 63_ compras layout + doc-type catalog (column-letter list = authoritative part; pp.1/3 template tables are images — group-header spans never transcribed, GOQ-105 kin): "NOMBRE DE COLUMNA COLUMNA / FECHA A / TIPO B / SERIE C / NUMERO D / NIT E / NOMBRE F / COMPRA(Q) G / SERVICIO (Q) H / IMPORTACIONES(Q) I / LOCAL(Q) J / EXENTO / EXPORTACIÓN (Q) K / FORMA DE PAGO L / NÚMERO DE DOCUMENTO M / NOMBRE DEL BANCO N / No. DE CUENTA O / MONEDA P" / rule 10: "En Libro de Compras, las columnas L, M, N, O y P; (INFORMACIÓN DEL MEDIO DE PAGO), no dejar espacios en blanco." / rule 13: "En el Libro de Compras, para la columna “B” tipo de documento, se deben identificar los documentos de acuerdo con la siguiente nomenclatura:" + table: "1 FACTURA FACTURA / 2 FACTURA DE PEQUEÑO CONTRIBUYENTE FPC / 3 FACTURA ELECTRÓNICA FACE FCE / 4 FACTURA ELECTRÓNICA FEL / 5 FACTURA ESPECIAL FE / 6 DECLARACIÓN ADUANERA DA / 7 FYDUCA FYDUCA / 8 NOTA DE CRÉDITO NC / 9 NOTA DE DÉBITO ND / 10 FACTURA ESPECIAL SOLICITA CRÉDITO FISCAL FESC / 11 ESCRITURA PÚBLICA EP / 12 FACTURA CAMBIARIA FCAM / 13 FACTURA CAMBIARIA ELECTRÓNICA FELCAM / 14 FACTURA ELECTRÓNICA PEQUEÑO CONTRIBUYENTE FELPC / 15 RECIBO RECI / 16 NOTA DE ABONO NABN / 17 FACTURA CONTRIBUYENTE AGROPECUARIO FACA" / Nota 1: "Los contribuyentes que no se encuentren inscritos en el Régimen Especial de Devolución al Banco de Guatemala o en el Régimen Optativo de Devolución de Crédito Fiscal, y/o en el padrón de Exportador de Productos Agropecuarios, Artesanales o Productos Reciclados , pueden utilizar el tipo de documento “FESC” para solicitar Crédito Fiscal de Facturas Especial." / Nota 2 (in part): "…el contribuyente podrá registrar en el Libro de Compras y Servicios Recibidos, en la columna “B” del formato CSV, como tipo de documento “FPC”, documentos recibidos que no generan derecho a crédito fiscal…: • Las Factura y /o Facturas cambiarias de contribuyente agropecuario… • Las Factura y/o Facturas cambiarias de contribuyente agropecuario Régimen Electrónico Especial… • Las Facturas y/o Facturas Cambiarios [sic] pequeño Contribuyente Régimen Electrónico…" | 16-column purchase-ledger layout A-P: A fecha, B tipo, C serie, D número, E NIT proveedor, F nombre proveedor, G compra Q, H servicio Q, I importaciones Q, J local Q, K exento/exportación Q, L-P payment block (forma de pago / no. documento / banco / no. cuenta / moneda) never blank; column B closed 17-value doc-type catalog — R49 defects kept verbatim: row 3 names "FACTURA ELECTRÓNICA FACE" but codes it FCE [sic]; row 12 FCAM lacks the ELECTRÓNICA qualifier of row 13 FELCAM; FESC = crédito vehicle on Facturas Especiales only for taxpayers NOT enrolled in the BANGUAT special-refund/optativo/agro-exporter rosters; FPC also covers no-credit agropecuario/régimen-electrónico/pequeño docs | `gt/sources/63_SAT-2390_instrucciones_csv.pdf` (via txt) | p.1 column list; pp.3-4 rules 10, 13 + Notas 1-2 (EVID-488) |
| LB-009 | 63_ ventas layout (column-letter list = authoritative part): "NOMBRE DE COLUMNA COLUMNA / FECHA A / TIPO B / SERIE C / NUMERO D / NIT E / NOMBRE F / VENTAS GRAVADAS(Q) G / SERVICIOS GRAVADOS (Q) H / DEBITO FISCAL(Q) I / EXPORTACIONES(Q) J / No. CONSTANCIA DE EXENCIÓN / No. DECLARACIÓN ADUANERA K" / rule 9: "En la columna de N o [sic No.] CONSTANCIA DE EXENCIÓN / No. DECLARACIÓN ADUANERA , del libro de ventas consignar lo que corresponda: Número de Constancia de Exención, DUA, FAUCA. Si la factura corresponde a VENTA LOCAL o ANULADA… consignar en la columna correspondiente, LOCAL o ANULADA, o “N/A”, de no aplica [sic]. No dejar en blanco el espacio, (Los números consignados en esta columna deben ir sin guion (-)). a) Libro de ventas, Columna (K)" | 11-column sales-ledger layout A-K: A fecha, B tipo, C serie, D número, E NIT cliente, F nombre cliente, G ventas gravadas Q, H servicios gravados Q, I débito fiscal Q (explicit — the value the cross-validation gate checks), J exportaciones Q, K constancia de exención / declaración aduanera — never blank: Constancia de Exención number, DUA or FAUCA without guion, or literal LOCAL / ANULADA / N/A | `gt/sources/63_SAT-2390_instrucciones_csv.pdf` (via txt) | p.1 column list; pp.1, 3 rules 1b, 2, 9 (EVID-489) |
| LB-010 | 63_ cell-format contract (rules 1-6): rule 1: "Si la casilla no contiene valor y corresponde a un valor numérico colocar cero (0) (Si es una factura, nota de crédito anulada, colocar cero (0)). a) Libro de compras, Columnas (G, H, I, J y K) b) Libro de ventas, Columnas (G, H, I y J)" / rule 2: "Las NOTAS DE CRÉDITO, se identificarán (NC), el valor de las notas de crédito NC se registran con valor negativo, y las NOTAS DE DÉBITO, se identificarán (ND), el valor… con valor positivo. Para las notas de crédito: a) Se coloca “NC” en la Columna B… b) Los valores de las Columnas (G, H, I, J y K) del libro de compras deben ser negativos. c) Los valores de las Columnas (G, H, I y J) del libro de ventas deben ser negativos. Para las notas de débito: d)… “ND”… e)… (G, H, I, J y K) del libro de compras deben ser positivos. f)… (G, H, I y J) del libro de ventas deben ser positivos." / rule 3: "Ninguna columna de los libros debe ir en blanco, excepto la columna serie, si el documento no tiene serie, la casilla serie debe quedar en blanco. a) Libro de compras, Columnas C b) Libro de ventas, Columnas C" / rule 4: "En el NIT, evitar utilizar guion (-), ni (_). Utilizar (-), (_) si y solo si es parte de un NIT, Ejemplo 45856-7 o 45856_7… En el caso de importaciones colocar el NIT del contribuyente que solicita la devolución de crédito fiscal. Y en el caso del libro de ventas el NIT e ID (NIT internacional), deberán incluirse en las operaciones mayores a Q2,500.00 de forma obligatoria a partir de enero 2023. c) Libro de compras, Columnas E (Nota: En columna F consignar el nombre o razón social del proveedor) d) Libro de ventas, Columnas E (Nota: En columna F consignar el nombre o razón social del cliente)" / rule 5: "En ninguna de las columnas utilizar comas (,). a) Libro de compras, Columnas (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O y P) b) Libro de ventas, Columnas (A, B, C, D, E, F, G, H, I, J y K)" / rule 6: "Todas las columnas consignar en formato TEXTO, excepto la columna de la fecha… b) Libro de compras, Columna (A) consignar formato FECHA CORTA. El formato debe ser “dd/MM/yyyy”, ejemplo 01/01/2016." (rule 6c's ventas list omits D by typo — column D NUMERO is intended TEXT with all non-A columns; flagged, not corrected) | Full cell contract: numeric buckets zero-filled (0) when empty, voided invoices/credit notes also 0; NC rows negative / ND rows positive across all value columns (compras G-K, ventas G-J) with NC/ND in column B; no blank cells anywhere except SERIE (C) without series; NIT without dash/underscore unless intrinsic; imports rows carry the requesting taxpayer's own NIT; ventas NIT + ID (NIT internacional) mandatory for operations > Q2,500.00 from enero 2023 (dated row — instrument external, GOQ-113); comma ban in every column; all cells TEXT format except date column A = FECHA CORTA dd/MM/yyyy | `gt/sources/63_SAT-2390_instrucciones_csv.pdf` (via txt) | p.2 rules 1-6; pp.3-4 rule 13 NC/ND values (EVID-490) |
| LB-011 | NEGATIVE (both documents): no date/version string anywhere in either text layer — 62_ footers print only "Página N de 8"; 63_'s only internal dating is rule 4's "a partir de enero 2023" (business rule), while its illustrative examples still use 2016/2017 dates ("01/01/2016", "SAT_102017_COMPRAS.csv"), consistent with a legacy layout carried forward; 62_ prints NO base-legal citation (contrast the 56_ Planilla IVA-FEL manual, which cites art. 72 D10-2012) | Both sources are undated procedural documents: currency unverifiable from the documents (GOQ-110); internal terminus post-2023-01; entitlement/window/granularity statutory anchors live in taxation (GOQ-111) — this file evidences mechanics only | `gt/sources/62_…/63_…` (via txt layers) | throughout both documents (EVID-481, EVID-487 identity verdicts) |

## 3. Functional Requirements

### 3.1 Channel identity, eligibility & provenance guards

- **GT-FIN-FR-131:** The system shall record the SAT-2390 channel identity
  as printed: the electronic *Solicitud de Devolución de Crédito Fiscal del
  IVA, Régimen General para contribuyentes que venden a entidades exentas*
  (electronic IVA fiscal-credit refund request, general regime, taxpayers
  selling to exempt entities), filed in Agencia Virtual under the service
  label "Solicitud Dev. CF Reg Gral contribuyentes que venden a entes
  exentos". The statutory eligibility surface is CONSUMED from taxation by
  exact id — entitlement for taxpayers rendering services or selling goods
  to exempt persons = **GT-TAX-FR-031**; Channel A (general, Arts. 23/23-A)
  = **GT-TAX-FR-032** — 62_ itself prints NO legal basis (GOQ-111 →
  OQ-002). The channel's registry position is the outside-catalog marker of
  Task 1 (cross-ref GT-FIN-FR-017, R58). (LB-001; EVID-481; cross-ref
  GT-TAX-FR-031, GT-TAX-FR-032, GT-FIN-FR-017; GOQ-111 → OQ-002)
- **GT-FIN-FR-132:** The provenance model shall record (GOQ-110 → OQ-001)
  that neither `62_` nor `63_` prints a date/version in its text layer:
  currency of both documents is unverifiable from the sources, the internal
  terminus is post-2023-01 (`63_` rule 4's "a partir de enero 2023"), and
  `63_`'s illustrative examples still carry 2016/2017 dates (legacy layout
  carried forward). Every practice row sourced from 62_/63_ carries this
  caveat and none is asserted as the verified current procedure without
  live verification. (LB-011; EVID-481, EVID-487; GOQ-110 → OQ-001;
  D15/D16)
- **GT-FIN-FR-133:** The statutory-consumption guard shall encode
  (GOQ-111 → OQ-002): `62_` cites no legal instrument, therefore the
  entitlement test (GT-TAX-FR-031), the refund channels (GT-TAX-FR-032
  Channel A quarterly/semiannual; GT-TAX-FR-033/034 kin), the saldo rule
  (refund forbidden except through the statutory channels — GT-TAX-FR-025),
  the Q10,000 application minimum (GT-TAX-FR-035) and the electronic 100%
  regime (GT-TAX-FR-036) are consumed from `taxation/01_iva-core.md` by
  exact id and NEVER re-derived or restated as law from this file's
  sources; this file owns only the filing mechanics. (LB-001; LB-011;
  EVID-481; cross-ref GT-TAX-FR-025, GT-TAX-FR-031..036)

### 3.2 Request object: header model & CARTERA lifecycle

- **GT-FIN-FR-134:** The request-header model shall implement the six
  apartados as printed: (a) *Datos del Contribuyente* auto-fed from the RTU
  — NIT, nombre, with **domicilio fiscal and correo electrónico
  overridable for this form only** (a different address than registered may
  be used), plus teléfono/extensión; (b) *Datos del Representante Legal*
  (persona jurídica only) — selection from the **active legal
  representatives as of the request date**, the selected one being the
  signer; (c) *Datos del Contador* auto-fed from the contador's RTU record;
  (d) *Datos de la Solicitud* — **exactly one producto principal** in free
  text ("solamente el nombre de un producto"), flagged as audit-relevant.
  (LB-003; EVID-483)
- **GT-FIN-FR-135:** The CARTERA portfolio surface shall implement: per
  request — número de Solicitud, No. Documento SAT, período solicitado,
  estado, and the Opciones column with the two buttons (print the sent
  request; attach the CSV annex files), plus the Nueva Solicitud action
  that starts a fresh SAT-2390. (LB-002; EVID-482)
- **GT-FIN-FR-136:** The request state machine shall carry the CARTERA
  states exactly as printed: **CONGELADO, EN PROCESO, RECIBIDO (GUARDADO),
  ADMITIDO, NO ADMITIDO, ASIGNADO Y RESUELTO** — the cardinality of
  "ASIGNADO Y RESUELTO" (one combined state vs. the last two of the list)
  is ambiguous as printed and shall be modeled as a single received-state
  label with the ambiguity recorded (GOQ-112 → OQ-003), never resolved by
  guess. (LB-002; EVID-482; GOQ-112 → OQ-003)
- **GT-FIN-FR-137:** The annex contract shall require exactly two CSV
  attachments per request — **Libro de Compras + Libro de Ventas, both
  comma-delimited** (formats per FR-146..160); no request is submittable
  (ENVIAR) without both annexes loaded and accepted. (LB-002; LB-006;
  EVID-482, EVID-486)

### 3.3 Claim window & aggregation (dated rows)

- **GT-FIN-FR-138:** The claim-window engine shall implement the dated row
  as printed: a period becomes claimable **only from the vencimiento de la
  presentación de las Declaraciones del IVA** (the IVA declaration filing
  due date) and claims run **up to 4 years after** that moment. The 4-year
  duration is the printed mechanics of `62_` — its statutory mirror
  (prescription window) is taxation-owned and consumed by cross-ref, never
  restated as law here (GOQ-111). Dated row per D16/D-GT10 with provenance
  "62_ p.4 mechanics; statutory basis not printed". (LB-004; EVID-484;
  cross-ref GT-TAX-FR-032; GOQ-111 → OQ-002; D15/D16)
- **GT-FIN-FR-139:** The aggregation rule shall implement: claim periods
  are aggregated **exclusively trimestral or semestral** ("únicamente en
  forma trimestral o semestral") — monthly and annual request shapes do not
  exist on this channel; the quarterly/semiannual granularity mirrors
  Channel A (GT-TAX-FR-032, consumed by exact id — GOQ-111). (LB-004;
  EVID-484; cross-ref GT-TAX-FR-032)

### 3.4 Amount determination & freeze gate

- **GT-FIN-FR-140:** The determination model shall key every claim row to a
  registered IVA declaration: the columns **Número de Declaración SAT-2237**
  and **Períodos Impositivos** are fed from the IVA declarations registered
  in the RTU — the taxpayer does not type declaration numbers; the claim
  amount is determined per declared period against those registered
  SAT-2237 declarations. (LB-005; EVID-485)
- **GT-FIN-FR-141:** The per-period amount entry shall implement: the
  taxpayer enters **"Crédito Sujeto a Devolución del Período"** per row
  (the pencil-editable value), recording each value **until totalling the
  requested amount**; **"Crédito no Solicitado"** exists only to reduce the
  claim and defaults to **0.00** — the reconciliation invariant is:
  crédito sujeto a devolución + crédito no solicitado = the period's credit.
  (LB-005; EVID-485)
- **GT-FIN-FR-142:** The freeze gate shall implement the sworn-declaration
  flow with the two buttons **Congelar / Cancelar**: Congelar moves the
  request to state CONGELADO and unlocks the annex upload; if inconsistencies
  with the **Representante Legal and Contador** records (vs RTU) are
  detected, the system **does not allow freezing** and the only printed
  path is Cancel and restart the whole process — no in-place edit of a
  frozen request. (LB-005; LB-006; EVID-485, EVID-486)

### 3.5 THE cross-validation gate & submission flow

- **GT-FIN-FR-143:** THE cross-validation gate shall be modeled exactly as
  printed: on CARGAR of an annex, the system "hace una comparación de los
  valores incluidos en Libros y Declaraciones" — it compares the uploaded
  **Libro de Compras / Libro de Ventas CSV values against the declared
  crédito and débito fiscal of the SAT-2237 IVA declarations** — and
  rejects on mismatch with the verbatim error: **"Los valores declarados
  como crédito y débito fiscales, no coinciden con los valores registrados
  en el Libro de Compras y Libro de Ventas"**. The values at stake are the
  ventas column I DEBITO FISCAL and the compras credit base buckets feeding
  the declared crédito (FR-153/154); whether the exportaciones column also
  feeds the check is not printed (recorded, never invented). This SAT-side
  gate is THE constraint the export pipeline must satisfy (FR-145).
  (LB-006; LB-008; LB-009; EVID-486, EVID-488, EVID-489)
- **GT-FIN-FR-144:** The submission flow shall implement: after the libros
  load completes, the **ENVIAR** button registers the request with the
  Administración Tributaria for analysis, and the taxpayer later receives
  the **Notificación by e-mail** (solicitud recibida / no recibida) at the
  previously registered address — which may be the per-form correo override
  of FR-134. (LB-006; EVID-486; cross-ref FR-134)
- **GT-FIN-FR-145:** The export pipeline shall pre-validate the
  reconciliation locally BEFORE upload: for every claimed period, the
  generated CSV book values (ventas débito fiscal; compras credit bases)
  must tie out with the SAT-2237-declared crédito/débito fiscal of the
  corresponding registered declarations, and a mismatch shall block the
  upload attempt with the SAT reject message mirrored — because the SAT
  gate (FR-143) rejects the annex at load otherwise. This FR is the
  export-pipeline requirement the cross-validation gate drives; the book
  data source is the Odoo books layer (S-GT5 dependency noted — the CSVs
  are a flat monthly render of the same book data LET surfaces, Task 4
  GT-FIN-FR-103..119, never a second bookkeeping). (LB-006; EVID-486;
  cross-ref FR-143, GT-FIN-FR-103)

### 3.6 CSV annex spec (authoritative from 63_)

- **GT-FIN-FR-146:** The file-generation contract shall produce **one CSV
  per month per book**, named exactly `SAT_<MES><AÑO>_COMPRAS.csv` /
  `SAT_<MES><AÑO>_VENTAS.csv` (printed examples
  `SAT_102017_COMPRAS.csv` / `SAT_102017_VENTAS.csv` = month 10 of 2017),
  saved in .CSV format. (LB-007; EVID-487)
- **GT-FIN-FR-147:** The row contract shall implement: **rows 1-2 are
  header rows and are always skipped** ("el sistema carga el archivo a
  partir de la línea 3 en adelante"); if the header fits on one line, row 2
  is left blank; and **no SUBTOTAL or TOTAL line may appear anywhere** in
  either book file. (LB-007; EVID-487)
- **GT-FIN-FR-148:** The compras CSV layout shall be **exactly 16 columns
  A-P** as printed in the authoritative column-letter list: **A** FECHA ·
  **B** TIPO · **C** SERIE · **D** NUMERO · **E** NIT (proveedor) · **F**
  NOMBRE (proveedor/razón social) · **G** COMPRA (Q) · **H** SERVICIO (Q) ·
  **I** IMPORTACIONES (Q) · **J** LOCAL (Q) · **K** EXENTO/EXPORTACIÓN (Q)
  · **L** FORMA DE PAGO · **M** NÚMERO DE DOCUMENTO · **N** NOMBRE DEL
  BANCO · **O** No. DE CUENTA · **P** MONEDA. The 63_ template
  group-header spans (e.g. "VALOR BASE" vs "VALOR CRÉDITO FISCAL" over
  G-K) are images and shall NEVER be transcribed or asserted (GOQ-105 kin
  — Task 4 OQ-002's 63_ half; the column-letter list is the authoritative
  part); notably compras carries NO explicit crédito-fiscal column — only
  the base buckets G-K. (LB-008; EVID-488; GOQ-105 kin via Task 4 OQ-002)
- **GT-FIN-FR-149:** The compras payment block shall implement rule 10:
  columns **L, M, N, O and P (INFORMACIÓN DEL MEDIO DE PAGO)** — forma de
  pago, número de documento, nombre del banco, No. de cuenta, moneda —
  shall **never be left blank** on any compras row. (LB-008; EVID-488)
- **GT-FIN-FR-150:** The compras column-B document-type catalog shall be
  the **closed 17-value nomenclature transcribed verbatim** (rule 13):
  FACTURA, FPC, FCE, FEL, FE, DA, FYDUCA, NC, ND, FESC, EP, FCAM, FELCAM,
  FELPC, RECI, NABN, FACA — with the R49 print defects kept exactly as
  printed: row 3 "**FACTURA ELECTRÓNICA FACE**" coded **FCE** [sic], and
  row 12 "FACTURA CAMBIARIA FCAM" lacking the "ELECTRÓNICA" qualifier
  that row 13 "FACTURA CAMBIARIA ELECTRÓNICA FELCAM" carries. The codes
  shall be verified against SAT's current catalog + the W-GT1 FEL document
  types (`e-invoicing/01_document-types.md`) before any mapping is frozen
  (GOQ-115 → OQ-006) — pointer only, never resolved here. (LB-008;
  EVID-488; R49; GOQ-115 → OQ-006)
- **GT-FIN-FR-151:** The FESC rule shall implement Nota 1: taxpayers **NOT
  enrolled** in the Régimen Especial de Devolución al Banco de Guatemala,
  the Régimen Optativo de Devolución de Crédito Fiscal, or the padrón de
  Exportador de Productos Agropecuarios, Artesanales o Productos
  Reciclados, may use document type **FESC** to claim crédito fiscal on
  Facturas Especiales — enrollment in any of those rosters removes the FESC
  vehicle (those taxpayers refund through their own regimes — GT-TAX-FR-034
  kin, consumed not re-derived). (LB-008; EVID-488; cross-ref
  GT-TAX-FR-034)
- **GT-FIN-FR-152:** The FPC rule shall implement Nota 2: received
  documents that generate **no right to crédito fiscal** for the buyer are
  recorded in compras column B as **FPC** — covering (i) facturas y
  facturas cambiarias of the Régimen Especial de Contribuyente
  Agropecuario, (ii) of the Régimen Electrónico Especial de Contribuyente
  Agropecuario, and (iii) facturas/facturas cambiarias [sic "Facturas
  Cambiarios"] of the Régimen Electrónico de Pequeño Contribuyente — FPC
  therefore covers both the pequeño-contribuyente factura itself and these
  no-credit docs. (LB-008; EVID-488)
- **GT-FIN-FR-153:** The compras base-bucket mapping shall map each Odoo
  supplier-invoice/journal line to exactly one value bucket — **G COMPRA
  (Q) · H SERVICIO (Q) · I IMPORTACIONES (Q) · J LOCAL (Q) · K
  EXENTO/EXPORTACIÓN (Q)** — with the signed-amount rules of FR-157; no
  crédito-fiscal column exists on the compras CSV (FR-148), so the
  declared-credit reconciliation of FR-143/145 derives from these bases.
  (LB-008; EVID-488; cross-ref FR-143, FR-145)
- **GT-FIN-FR-154:** The ventas CSV layout shall be **exactly 11 columns
  A-K** as printed in the authoritative column-letter list: **A** FECHA ·
  **B** TIPO · **C** SERIE · **D** NUMERO · **E** NIT (cliente) · **F**
  NOMBRE (cliente/razón social) · **G** VENTAS GRAVADAS (Q) · **H**
  SERVICIOS GRAVADOS (Q) · **I** DEBITO FISCAL (Q) — explicit, the value
  the cross-validation gate checks (FR-143) · **J** EXPORTACIONES (Q) ·
  **K** No. CONSTANCIA DE EXENCIÓN / No. DECLARACIÓN ADUANERA. Group-header
  spans are images — never transcribed (GOQ-105 kin). (LB-009; EVID-489;
  cross-ref FR-143)
- **GT-FIN-FR-155:** The ventas column-K contract shall implement rule 9:
  column K is **never blank**, with the closed vocabulary — **número de
  Constancia de Exención** (exempt-sale certificate), **DUA** or **FAUCA**
  customs declaration number for exports, written **sin guion** (no
  hyphen); or the literal **LOCAL** (local sale), **ANULADA** (voided
  invoice), or **N/A** when neither applies. The constancia number is the
  operational trace of the exempt-entity sale — the population marker of
  this channel (ventas a entidades exentas). (LB-009; EVID-489)

### 3.7 Cell-format contract (both books)

- **GT-FIN-FR-156:** The cell typing shall implement rule 6: **every
  column is format TEXTO except the date column A**, which is FECHA CORTA
  `dd/MM/yyyy` (printed example 01/01/2016) — amounts are text cells.
  (Rule 6c's ventas list omits column D by typo; D NUMERO is intended TEXT
  with all non-A columns — flagged, not corrected.) Empty numeric cells are
  **zero-filled (0)** in compras columns G-K and ventas columns G-J —
  including voided facturas/notas de crédito (rule 1). (LB-010; EVID-490)
- **GT-FIN-FR-157:** The sign convention shall implement rule 2: rows with
  **NC** in column B carry **negative** values and rows with **ND** carry
  **positive** values across all value columns — compras G-K and ventas
  G-J — with the NC/ND marker in column B of both books. (LB-010; EVID-490)
- **GT-FIN-FR-158:** The blank/NIT rules shall implement rules 3-4: **no
  column may be blank except SERIE (C)** when the document has no series;
  the NIT columns (E) carry **no guion (-) or underscore (_) unless
  genuinely part of the NIT** (printed example 45856-7 / 45856_7), and
  **importaciones rows carry the requesting taxpayer's own NIT**; column F
  always carries the proveedor/cliente nombre o razón social. (LB-010;
  EVID-490)
- **GT-FIN-FR-159:** DATED ROW (D16/D-GT10, valid from **2023-01**,
  provenance "63_ rule 4; instrument external"): in the ventas book, **the
  client NIT and ID (NIT internacional) shall be included, mandatorily,
  for operations greater than Q2,500.00 from enero 2023**. The external
  instrument is not in the corpus, and how "ID (NIT internacional)" renders
  in the single NIT column (E) for foreign clients without a Guatemalan
  NIT is open — transcribed exactly, never resolved by guess (GOQ-113 →
  OQ-004). (LB-010; EVID-490; GOQ-113 → OQ-004; D15/D16)
- **GT-FIN-FR-160:** The comma ban shall implement rule 5: **no commas in
  any column** — rule 5 enumerates all 16 compras columns (A-P) and all 11
  ventas columns (A-K) — therefore amounts carry no thousands separators;
  the decimal separator is only implied "." by the printed "Q2,500.00"/
  "0.00" examples and is never stated (container matter — GOQ-114).
  (LB-010; EVID-490; GOQ-114 → OQ-005)
- **GT-FIN-FR-161:** The container guard shall record (GOQ-114 → OQ-005):
  file **encoding (ANSI vs UTF-8), BOM, line endings, quoting/escaping
  (moot given the comma ban), maximum rows/file size, decimal separator and
  negative-number rendering are unspecified** by 63_ (the Notepad check of
  rule 12 only hints plain single-file text). These parameters shall be
  fixed by testing against the real SAT loader — recorded as an open
  question, never invented. (LB-007; LB-010; EVID-487, EVID-490;
  GOQ-114 → OQ-005)

### 3.8 Pairing & register rows

- **GT-FIN-FR-162:** The books pairing shall record: the "Libro de
  Compras / Libro de Ventas" the cross-validation gate compares are the
  taxpayer's IVA books — the same statutory book obligations Task 4 models
  on the LET surfaces (GT-FIN-FR-103..119: General = two books per month
  per establecimiento); the SAT-2390 CSVs are a SAT-2390-specific flat
  monthly render of that book data, generated from the Odoo books layer
  (S-GT5 dependency noted) — two surfaces of one bookkeeping, never a
  second data set. (LB-002; LB-006; EVID-482, EVID-486; cross-ref
  GT-FIN-FR-103..119)
- **GT-FIN-FR-163:** The channel-matrix consumption row shall bind this
  file's mechanics to the taxation channel matrix by exact id only:
  entitlement = **GT-TAX-FR-031**; Channel A general Arts. 23/23-A
  (accumulated expired periods, **quarterly or semiannual** — the statutory
  mirror of FR-139) = **GT-TAX-FR-032**; saldo carries forward and refund
  is forbidden except through the statutory channels = **GT-TAX-FR-025**;
  Channel B/C kin = GT-TAX-FR-033/034; Q10,000 minimum = GT-TAX-FR-035;
  electronic 100% regime = GT-TAX-FR-036; export evidence pack =
  GT-TAX-FR-037. None of these is restated from 62_/63_ (which print no
  legal basis — GOQ-111). (LB-001; LB-004; EVID-481, EVID-484; cross-ref
  GT-TAX-FR-025, GT-TAX-FR-031..037; GOQ-111 → OQ-002)
- **GT-FIN-FR-164:** The R58 register pairing shall record: SAT-2390 is
  absent from the 48_ 4-table form catalog yet fully documented as a
  Formulario Electrónico in Agencia Virtual by 62_/63_ — 48_-absence ≠
  nonexistence; the channel links to Task 1's outside-catalog marker
  (GT-FIN-FR-017) and this file discharges the "Task 5 owns SAT-2390" note
  of that row. (LB-001; EVID-481; cross-ref GT-FIN-FR-017; R58)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + provenance
+ as-of qualifier; snapshot-on-write. This file stores NO statutory
constants — entitlement/channels/minimums are taxation-owned and consumed
by FR id (FR-133/163 anchors). What is stored here: the channel identity
row, the provenance caveats, the request-header model, the CARTERA state
row, the window/aggregation dated rows, the determination model, the gate
contract, the two column-letter layouts (authoritative part only), the
17-value doc-type catalog (verbatim incl. defects), the cell contract and
the container-unknown row.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.devolucion.channel | form / population / service_label / legal_basis_printed | char=SAT-2390 / char / char / selection none | entitlement + channels consumed: GT-TAX-FR-031/032/025 (GOQ-111) | FR-131, FR-163 |
| l10n_gt.devolucion.provenance | file / version_date_printed / internal_terminus / caveat | selection 62_-63_ / char=none / char=post-2023-01 / char | GOQ-110 caveat rides every practice row | FR-132 |
| l10n_gt.devolucion.request.header | nit / nombre / domicilio_override / correo_override / tel_ext / rep_legal_selection / contador_rtu / producto_principal | char (RTU-fed) / char / char / char / char / selection active-as-of-request-date / char (RTU-fed) / char single-product free text | per-form overrides; producto = audit-relevant | FR-134 |
| l10n_gt.devolucion.cartera | no_solicitud / no_documento_sat / periodo / estado / opciones | char / char / char / char label as printed / list print-attach | states verbatim CONGELADO…ASIGNADO Y RESUELTO; GOQ-112 ambiguity flag | FR-135, FR-136 |
| l10n_gt.devolucion.annex | book / filename_pattern / month / year | selection compras-ventas / char=SAT_<MM><YYYY>_<BOOK>.csv / integer / integer | one CSV per month per book; rows 1-2 headers skipped; no SUBTOTAL/TOTAL | FR-137, FR-146, FR-147 |
| l10n_gt.devolucion.window | from_event / duration / granularity / valid_from / provenance | char=vencimiento IVA declaration / char=4 años / selection trimestral-semestral / date / char=62_ p.4 mechanics (statutory mirror = taxation) | dated row; GOQ-111 (no basis printed) | FR-138, FR-139 |
| l10n_gt.devolucion.determination | sat2237_decl_no / periodo_impositivo / credito_sujeto / credito_no_solicitado | char (RTU-fed) / char / decimal user-entered / decimal default 0.00 | invariant: sujeto + no_solicitado = period credit | FR-140, FR-141 |
| l10n_gt.devolucion.congelar | gate / failure_action / unlocks | rep_legal + contador vs RTU consistency / cancel-and-restart / annex upload | freeze → CONGELADO state | FR-142 |
| l10n_gt.devolucion.gate.crossval | comparison / reject_message / values_in_scope / exportaciones_in_check | libros CSV values vs SAT-2237 declared crédito/débito / verbatim LB-006 message / compras bases G-K + ventas col I / selection unspecified | THE gate; drives FR-145 pre-flight | FR-143, FR-145 |
| l10n_gt.devolucion.csv.compras.layout | col_letter A-P / field / group_spans | char / char list (16, verbatim LB-008) / selection never_asserted (GOQ-105 kin) | column-letter list = authoritative part; no crédito column (bases only) | FR-148, FR-149, FR-153 |
| l10n_gt.devolucion.csv.ventas.layout | col_letter A-K / field / group_spans | char / char list (11, verbatim LB-009) / selection never_asserted | col I = DEBITO FISCAL (gate value); col K vocabulary | FR-154, FR-155 |
| l10n_gt.devolucion.csv.cellcontract | text_all / date_format / zero_fill_cols / nc_negative_nd_positive / blank_only_serie / nit_rules / imports_own_nit / comma_ban / nit_id_q2500 | boolean / char=dd/MM/yyyy / list compras-G..K ventas-G..J / boolean / char=C / char no-guion-unless-intrinsic / boolean / boolean all-columns / dated row valid_from=2023-01 (GOQ-113) | rule 6c typo on col D flagged not corrected | FR-156..FR-160 |
| l10n_gt.devolucion.doctype | no / nombre / tipo_doc | integer 1-17 / char verbatim (incl. "FACTURA ELECTRÓNICA FACE" + FCE [sic]; FCAM/FELCAM asymmetry) / char | closed catalog; FESC/FPC notas; GOQ-115 verification vs W-GT1 | FR-150, FR-151, FR-152 |
| l10n_gt.devolucion.container | encoding / bom / eol / quoting / row_caps / decimal_sep / negative_render | all selection unspecified | GOQ-114 — fixed by testing against the real loader | FR-161 |
| l10n_gt.devolucion.guard | key | char list | undated_prints (GOQ-110); no_legal_basis (GOQ-111); estado_cardinality (GOQ-112); nit_id_external (GOQ-113); container_unspecified (GOQ-114); doctype_oddities (GOQ-115); spans_never_transcribed (GOQ-105 kin); r58_outside_catalog | FR-132, FR-133, FR-136, FR-159, FR-161, FR-164 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration, generation and selection surface in the LGPL client; `saas`
= authoritative validation, SAT-side state modeling and transmission in
the Elixir core; `shared` = contract items both sides must honor
identically. Wave defaults for this file (binding): CSV generation from
Odoo books = `odoo` (S-GT5 books-layer dependency noted); cross-validation
gate + CARTERA states + RTU consistency checks = `saas`;
window/aggregation dated rows + column-letter schemas = `shared`. Model
names stable across Odoo 17/18/19/20; no version-specific behavior required
by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-131 | shared | — (config data §4) | channel row | Entitlement/channels consumed GT-TAX-FR-031/032; R58 pairing to T1 FR-017 |
| FR-132 | shared | — (config data §4) | provenance rows | GOQ-110 caveat rides every 62_/63_-sourced row |
| FR-133 | shared | — (guard) | no_legal_basis | Statutory anchors taxation-only; grep-able guard |
| FR-134 | odoo | devolución request model | header fields + overrides + rep-legal selection + producto | RTU-fed fields rendered read-only; per-form domicilio/correo overrides |
| FR-135 | saas | CARTERA state model (rendered in odoo) | cartera row | States are SAT-side received data; odoo renders the portfolio |
| FR-136 | saas | CARTERA state model | estado label | GOQ-112 ambiguity: single label, never split by guess |
| FR-137 | shared | — (contract) | annex pair requirement | ENVIAR blocked without both accepted annexes |
| FR-138 | shared | — (config data §4 / CSV) | window dated rows | From-event = IVA due date; 4 años; statutory mirror taxation cross-ref |
| FR-139 | shared | — (config data §4) | granularity row | Trimestral/semestral only; mirrors GT-TAX-FR-032 |
| FR-140 | saas | SAT-2237 declaration feed ingestion | decl-no + período rows | RTU-registered declarations; odoo renders read-only pick list |
| FR-141 | odoo | devolución determination line | credito_sujeto / credito_no_solicitado | Pencil-edit entry until total; default 0.00 reduction |
| FR-142 | saas | freeze gate service | rep-legal/contador consistency check | Congelar/Cancelar semantics; failure = restart |
| FR-143 | saas | cross-validation gate service | libros-vs-declaraciones comparison + verbatim reject | THE authoritative gate (D2); exportaciones scope unspecified |
| FR-144 | saas | transmission + notification service | ENVIAR + e-mail notice | Notice address honors per-form correo override |
| FR-145 | odoo | annex export wizard + pre-flight check | per-period reconciliation vs declared crédito/débito | S-GT5 books-layer dependency; mirrors FR-143 before upload |
| FR-146 | odoo | CSV export wizard | filename pattern + month/year split | SAT_<MM><YYYY>_<BOOK>.csv |
| FR-147 | odoo | CSV export wizard | 2 header rows + no totals lines | Loader reads row 3+; one-line header ⇒ blank row 2 |
| FR-148 | shared | — (config data §4 / CSV) | compras column-letter schema A-P | Authoritative part only; spans never asserted (GOQ-105 kin) |
| FR-149 | odoo | CSV export wizard (compras) | L-P payment block completeness validation | Never blank on any row |
| FR-150 | shared | — (config data §4 / CSV) | 17-value doc-type catalog (verbatim) | R49 defects kept; GOQ-115 verification vs W-GT1 pending |
| FR-151 | odoo | supplier-doc tagging rule | FESC eligibility test | Roster enrollment removes FESC; GT-TAX-FR-034 kin |
| FR-152 | odoo | supplier-doc tagging rule | FPC no-credit mapping | Agro / electrónico-agro / electrónico-PC docs → FPC |
| FR-153 | odoo | CSV export wizard (compras) | G-K base bucket mapping | From books/journal data; no crédito column exists |
| FR-154 | shared | — (config data §4 / CSV) | ventas column-letter schema A-K | Col I DEBITO FISCAL = gate value; spans never asserted |
| FR-155 | odoo | CSV export wizard (ventas) | column K vocabulary + sin-guion rule | Constancia/DUA/FAUCA/LOCAL/ANULADA/N/A; never blank |
| FR-156 | odoo | CSV export wizard (both) | TEXT cells + dd/MM/yyyy + zero-fill | Rule 6c col-D typo flagged, not corrected |
| FR-157 | odoo | CSV export wizard (both) | NC− / ND+ sign convention | Marker in col B both books |
| FR-158 | odoo | CSV export wizard (both) | SERIE-only blank + NIT rules | Imports rows = requesting taxpayer's NIT |
| FR-159 | shared | — (dated row §4) | nit_id_q2500 valid_from 2023-01 | GOQ-113: instrument external; foreign-client rendering open |
| FR-160 | odoo | CSV export wizard (both) | comma ban (all columns) | Decimal separator implied "." only (GOQ-114) |
| FR-161 | shared | — (guard) | container unspecified row | GOQ-114: fixed by testing against real loader |
| FR-162 | shared | — (provenance ledger) | LET/books pairing row | T4 GT-FIN-FR-103..119 = same bookkeeping; S-GT5 dependency |
| FR-163 | shared | — (config data §4) | channel-matrix consumption anchors | GT-TAX-FR-025/031..037 by exact id only |
| FR-164 | shared | — (register row) | r58_outside_catalog | Discharges T1 FR-017's "Task 5 owns SAT-2390" note |

## 6. Acceptance Criteria

- **AC-001:** Given the channel identity row, then SAT-2390 resolves as the
  electronic refund request for régimen-general taxpayers selling to
  exempt entities with the Agencia Virtual service label as printed, and
  its eligibility/entitlement resolves ONLY through GT-TAX-FR-031/032 by
  exact id — grep finds no statutory restatement sourced from 62_/63_.
  (FR-131, FR-133, FR-163)
- **AC-002:** Given any practice row sourced from 62_/63_, then it carries
  the undated-print caveat (GOQ-110) and none is asserted as verified
  current procedure. (FR-132)
- **AC-003:** Given a new request, then the header auto-fills NIT/nombre/
  contador from RTU, accepts per-form domicilio/correo overrides, requires
  selection of an active legal representative for personas jurídicas, and
  accepts exactly one producto principal; the e-mail notice after ENVIAR
  goes to the effective (possibly overridden) address. (FR-134, FR-144)
- **AC-004:** Given the CARTERA, then each request shows número de
  solicitud, documento SAT, período, estado and the two option buttons;
  the state list is exactly CONGELADO, EN PROCESO, RECIBIDO (GUARDADO),
  ADMITIDO, NO ADMITIDO, ASIGNADO Y RESUELTO as printed, with the
  ASIGNADO-Y-RESUELTO cardinality ambiguity flagged, never split by guess.
  (FR-135, FR-136)
- **AC-005:** Given period selection, then a period is offerable only
  after its IVA declaration due date and only within 4 years of it, and
  requests aggregate exclusively in trimestral or semestral blocks — no
  monthly/annual request shape exists. (FR-138, FR-139)
- **AC-006:** Given the determination step, then declaration numbers and
  períodos impositivos come only from the RTU-registered SAT-2237
  declarations; the taxpayer enters Crédito Sujeto a Devolución per period
  until totalling the requested amount, Crédito no Solicitado defaults to
  0.00 and only reduces; and Congelar fails on rep-legal/contador
  inconsistencies vs RTU leaving Cancel-and-restart as the only path.
  (FR-140, FR-141, FR-142)
- **AC-007:** Given an uploaded annex whose book values do not match the
  declared crédito/débito fiscal of the SAT-2237 declarations, then the
  load is rejected with the verbatim message "Los valores declarados como
  crédito y débito fiscales, no coinciden con los valores registrados en
  el Libro de Compras y Libro de Ventas"; and the export wizard blocks
  locally beforehand on the same reconciliation (FR-143 gate; FR-145
  pre-flight). (FR-143, FR-145)
- **AC-008:** Given the CSV export, then one file per month per book is
  produced, named SAT_<MM><YYYY>_COMPRAS.csv / _VENTAS.csv, with rows 1-2
  as skipped headers (blank row 2 on one-line headers) and zero
  SUBTOTAL/TOTAL lines. (FR-146, FR-147)
- **AC-009:** Given a compras CSV, then it has exactly the 16 columns A-P
  in the printed order; the payment block L-P contains no blank cell; the
  column-B value belongs to the 17-value catalog transcribed verbatim
  ("FACTURA ELECTRÓNICA FACE"→FCE [sic] and the FCAM/FELCAM asymmetry kept
  as printed); and no group-header span is asserted anywhere (grep: no
  layout-span entity). (FR-148, FR-149, FR-150)
- **AC-010:** Given a supplier document, then FESC applies only when the
  taxpayer is enrolled in none of the BANGUAT-special/optativo/agro-export
  rosters, and no-credit agropecuario/régimen-electrónico docs tag as FPC.
  (FR-151, FR-152)
- **AC-011:** Given a ventas CSV, then it has exactly the 11 columns A-K;
  column I carries DEBITO FISCAL (the gate value); column K is never blank
  with only Constancia de Exención / DUA / FAUCA (sin guion) / LOCAL /
  ANULADA / N/A. (FR-154, FR-155)
- **AC-012:** Given any generated row, then all cells are TEXT except date
  column A in dd/MM/yyyy; empty numeric buckets print 0; NC rows are
  negative and ND rows positive across the value columns; only SERIE (C)
  may be blank; NITs carry no guion/underscore unless intrinsic and
  importaciones rows carry the requester's own NIT; no comma appears in
  any cell; and ventas rows for operations > Q2,500.00 dated on/after
  2023-01 carry the client NIT/ID (dated row visible with its GOQ-113
  flag). (FR-156..FR-160)
- **AC-013:** Given any container question (encoding/BOM/EOL/quoting/row
  caps/decimal separator/negative rendering), then the system asserts no
  value from the corpus — the container row stays "unspecified" until
  fixed by testing against the real loader. (FR-161)
- **AC-014:** Given the pairing rows, then the annex CSVs resolve as a
  flat render of the same bookkeeping Task 4's LET surfaces model (no
  second data set), the statutory anchors resolve only by taxation id,
  and the channel links to T1's outside-catalog marker GT-FIN-FR-017
  (R58). (FR-162, FR-163, FR-164)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.4);
question text verbatim from the register. This file OWNS GOQ-110/111/112/
113/114/115 (F5 rows). The 63_ group-header-span half of GOQ-105 is
discharged by the never-transcribe rule (FR-148/154) with the register row
owned by Task 4's OQ-002. Nothing outside this register is treated as an
open question; new gaps are flagged to the controller as non-OQ notes (no
invented ids).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-110 (owned): "SAT-2390 (62_/63_): neither prints a date/version in the text layer (internal terminus: post-2023-01) — provenance rows." Affects every practice row of this file (FR-131..162): values verified against the live Agencia Virtual/loader before any current-procedure assertion. | no | GT synthesis wave S-GT4 → acquisition queue (live portal verification) | open |
| OQ-002 | GOQ-111 (owned): "SAT-2390 statutory basis: 62_ cites NO legal basis — entitlement, 4-year window, trimestral/semestral granularity sourced from W-GT2/25_; mechanics only here." Affects FR-131/133/138/139/163 — statutory anchors consumed by taxation id (GT-TAX-FR-025/031/032..037); nothing restated as law from 62_/63_. | no | GT synthesis wave S-GT4 → S-GT2 taxation files (anchors already consumed; no re-derivation) | open |
| OQ-003 | GOQ-112 (owned): "SAT-2390 state list '…ASIGNADO Y RESUELTO' — combined state or last-two cardinality ambiguous." Affects FR-136 (single received-state label; never split by guess). | no | GT synthesis wave S-GT4 → acquisition queue (live CARTERA observation) | open |
| OQ-004 | GOQ-113 (owned): "Ventas NIT+ID rule (> Q2,500 from enero-2023): its instrument is external; how 'ID (NIT internacional)' renders in the single NIT column for foreign clients?" Affects FR-159 (dated row transcribed exactly; foreign-client rendering open — never resolved by guess). | no | GT synthesis wave S-GT4 → acquisition queue (external instrument + loader behavior) | open |
| OQ-005 | GOQ-114 (owned): "CSV container details unspecified: encoding/BOM/EOL/quoting/row caps/decimal separator/negative rendering — fix by testing against the real loader." Affects FR-146..160 (generation parameters) and FR-161 (container guard). | yes (file generation only) | GT synthesis wave S-GT4 → implementation phase (test against real loader) | open |
| OQ-006 | GOQ-115 (owned): "63_ doc-type catalog oddities (FCE [sic] for FACE; FCAM vs FELCAM qualifier asymmetry) — verify codes vs SAT current catalog + W-GT1 FEL catalogs." Affects FR-150 (catalog stored verbatim with defects; verification pointer to `e-invoicing/01_document-types.md` before mapping freeze). | no | GT synthesis wave S-GT4 → W-GT1 catalogs cross-check | open |
