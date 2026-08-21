# GT — Chart of accounts — Dual-track book legalization: RM autorización + SAT habilitación + the electronic-books bridge

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | GT synthesis wave S-GT5 |
| Updated | 2026-08-21 |

## 1. Purpose

This file is the SECOND of the S-GT5 chart-of-accounts/commercial-legal wave:
it owns the **dual-track, two-authority book-legalization model** (cluster C2).
Guatemalan legal books are legalized on two PARALLEL tracks that are never
merged (R62): the four *Código de Comercio* books (Commercial Code, CCom —
the set anchored by `01_books-anchor.md` GT-COA-FR-002) need **RM
autorización** (authorization by the *Registro Mercantil*, Mercantile
Registry — CC art. 372) **AND SAT habilitación** (legalization/enablement by
the tax administration — *formulario SAT-7121*, at any *agencia u oficina
tributaria* or the *Agencia Virtual*); tax-law books (IVA art. 37 two books
for *Régimen Normal/General*; IVA art. 49 the single *pequeño contribuyente*
book; the ISR backing registros of LAT arts. 40/42/53) need **SAT habilitación
only**; books may be manual or computerized at the taxpayer's choice. On that
model this file fixes: the RM autorización mechanics (art. 372 + the Q0.20
per *hoja* (sheet) + "pago variable" arancel row as dated-2022-label data —
R66); the SAT habilitación mechanics (SAT-7121 → *resolución de habilitación
de libros*, no SAT-side fee evidenced anywhere — never model one); the
bookkeeping-surface specs this cluster owns from the 60_ restatement
(*libro de inventarios* bank-account and investment detail registers; LAT
art. 53's guard that *Opcional Simplificado* taxpayers also owe CC-based
*contabilidad*; the ISR backing statements; the AG 213-2013 six-field
inventory detail; the "para efectos fiscales" cap); the RLIVA arts. 38-39
field-level IVA book specs (crédito/débito split by local/export/exempt,
monthly summary, daily consolidation, PC net = invoice total); the
electronic-books bridge of IVA art. 29-"A" (added by D-4-2019 art. 6, in
force 30-oct-2019: Régimen de Factura Electrónica taxpayers run an
electronic system subsuming the FIVE book categories; SAT supplies the
tools; Agencia Virtual *libros electrónicos* with DTE auto-load) with
pointer-only cross-refs to the fin-wave surfaces that instantiate it; and
the sanction gates this model feeds (missing either track → *cierre
temporal*; books not *al día* or in wrong form → Q5,000 per fiscalización —
machinery consumed from taxation by exact FR id; this file owns only the
legalization-status predicates).

It does **not** cover: the C1 anchor itself — the four-book registry,
entry invariants, conservation and instrument identity
(`01_books-anchor.md`, GT-COA-FR-001..033, consumed by id); the RM arancel
fee catalog and the edicto/publication channel execution
(`../../commercial-legal/01_rm-surfaces.md`, C3 — forward ref, file +
cluster only; this file states only the books-authorization fee row); the
comerciante/sociedades lifecycle (C4); títulos valores and the prescription
ladder (C5); the AML chain (C6); the consolidated retention/destruction
matrix (`03_retention-destruction-matrix.md`, the GOQ-124 deliverable, Task
7 — which consumes this file's legalization-status rows as matrix inputs);
tax-side books duties (owned by the taxation wave — GT-TAX-FR-066 statutory
hook, GT-TAX-FR-214/216/217/230/231 sanction and books-family rows,
consumed by exact id, never re-derived); the pequeño libro operational
surface (fin03 — GT-FIN-FR-086, GT-FIN-FR-089 consumed by id); LET
mechanics (fin04 — GT-FIN-FR-104/118, pointer-only); and FEL/DTE archive
duties (GT-EINV wave — outcome-only cross-refs).

## 2. Legal Basis

Authority order (binding, per master index preamble): CCom article text =
**66_** — *Código de Comercio, Decreto del Congreso 2-70* — as consolidated
inline through **Decreto 11-2006 (DCA 30-05-2006)**; the GOQ-123
live-regime verification note rides every 66_ citation family (owned by
`01_books-anchor.md` FR-031; kin-cited here — T1's §2 carries the dated
identity rows: vigencia 1971-01-01, R45). **Books LBs cite 66_ + 60_
jointly** per the wave authority order: **60_ is an UNDATED ILLUSTRATIVE
SAT orientation** (Unidad de Orientación Legal — "Este material solo puede
ser utilizado con fines ilustrativos…", no version/date string printed;
terminus post quem = its D-4-2019 art. 6 citation "el cual entró en vigencia
el 30 de octubre 2019" → snapshot ≥ 2019-10-30), **never law** — all legal
force resides in the instruments it cites (CCom D-2-70 arts. 2, 368, 371,
372, 377; Ley IVA D-27-92 arts. 37, 49, 29-"A"; Reglamento IVA AG 5-2013
arts. 38-39; LAT D-10-2012 arts. 40, 42, 53; Reglamento del Libro I de la
LAT AG 213-2013; Ley ONG D-2-2003 art. 13; Código Tributario arts. 85,
94.4; D-4-2019 art. 6). **73_** (RM arancel) = dated-2022-label fee data —
the print carries NO date or instrument number (label-derived as-of; its
own "Ajuste por vigencia de nuevo Arancel" rows presuppose supersession
cycles) and is a 1-page scan with heavy OCR damage (fee rows quoted from
the committed evidence file only); re-verify before any operative use
(R66). Vocabulary (R62): *autorización* = the Registro Mercantil track
(the CCom's word — "habilitación" NEVER appears in the CCom, EVID-521);
*habilitación* = the SAT/CT track; both needed per CC book, never merged.
1970-nominal amounts restated by 60_ (Q25,000 omission floor; Q20,000
contador floor) are never indexed — dated rows under D16, GOQ-126
verify-before-config kin (R67). The statutory text of IVA art. 29-"A" and
its D-4-2019 art. 6 provenance are owned by the e-invoicing wave
(`../e-invoicing/04_mandate-onboarding.md` LB-003) — cited by pointer,
never restated here; this file quotes 60_'s rendition (EVID-592).
Quotation source: the committed evidence files
`gt/.extractions/60_73_83_RM.evidence.md` (EV05c; EVID-586..605) and
`gt/.extractions/66_CCom_libros_contabilidad.evidence.md` (EV05a;
EVID-501..522), verified against the scan text layers in `gt/.extractions/`.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 60_ (SAT orientation), dual-track rule: "Para ese efecto deberán solicitar en cualquier agencia u oficina tributaria del país, la habilitación de los siguientes libros o registros:" / "Asimismo el artículo 372 del Código de Comerc io [sic Comercio] de Guatemala preceptúa que los libros de inventarios, de primera entrada o diario, el mayor o centralizador y el de estados financieros, deberán ser autorizados por el Registro Mercantil." / "Los libros contables podrán ser manuales o computarizados, a conveniencia del contribuyente o responsable tributario, dichos libros deben ser habilitados por la Administración Tributaria. Para realizar la habilitación de libros por agencia virtual deberá utilizar el formulario SAT-7121 Habilitación y autorización de libros y seguir los siguientes pasos: https://portal.sat.gob.gt/portal /requisitos-tramites-agencias/habilitación-de-libros/" / "Debe considerarse que los libros contables referidos en el mencionado Código deben estar autorizados por el Registro Mercantil y habilitados po r [sic por] la Administración Tributaria, para el caso de los libros contables establecidos en leyes de materia tributaria, únicamente deben estar habilitados por la Administración Tributaria." | For that purpose they shall request, at any tax agency or office in the country, the legalization of the following books or registers. Likewise article 372 of the Commercial Code of Guatemala provides that the inventarios, daybook, mayor/centralizador and estados-financieros books must be authorized by the Registro Mercantil. Accounting books may be manual or computerized, at the taxpayer's or responsible party's convenience; said books must be legalized (habilitados) by the Tax Administration. To legalize books via Agencia Virtual, use formulario SAT-7121 "Habilitación y autorización de libros" and follow the printed steps (portal URL). It must be considered that the books referred to in said Code must be authorized by the Registro Mercantil AND legalized by the Tax Administration; in the case of the books established in tax-law matter, they only must be legalized by the Tax Administration | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | pp.5, 10, 12 (EVID-587) |
| LB-002 | CCom art. 372 + Disposiciones Transitorias art. IX: "Los libros de inventarios y de primera entrada o diario, el mayor o centralizador y el de estados financieros, deberán ser autorizados por el Registro Mercantil." / "La autorización de libros y de registros establecida en el artículo 372 comenzará a hacerse por el Registro Mercantil de la capital a partir de la fecha de vigencia de esta ley. En los demás registros se hará desde la fecha que el Ministerio de Economía determine." | The inventarios and first-entry/daybook, the mayor/centralizador and the estados-financieros books must be authorized by the Registro Mercantil. (Transitory IX: this authorization began at the RM of the capital from the law's vigencia; at other registries from the date the Ministry of the Economy set) | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | p.83 art. 372; p.209 transitorio IX (EVID-507) |
| LB-003 | 66_ NEGATIVE findings (full-file term sweeps): "habilita" → only quiebra/seguro "rehabilitación" senses (no libros-habilitación anywhere in the code); the mandatory list (art. 368, raw lines 4288-4289) contains no copiador de correspondencia; the only medium clause is art. 368 ¶3 "También podrán llevar la contabilidad por procedimientos mecanizados, en hojas sueltas, fichas o por cualquier otro sistema, siempre que permita su análisis y fiscalización." | "Habilitación" is NOT Código de Comercio vocabulary — RM "autorización" (art. 372) is the CCom word; "habilitación" is SAT/CT vocabulary. The split authority (RM vs SAT) is real, not superseded | `gt/sources/66_Codigo_Comercio_D2-70.pdf` | full-file sweeps (EVID-521; supersession ledger EVID-522) |
| LB-004 | 60_, book contents: "Los comerciantes obligados a llevar contabilidad deberán registrar en su contabilidad todas las cuentas bancarias que utilicen para realizar sus transacciones mercantiles e inversiones que se originen del capital o de los recursos financieros de la entidad, independientemente si se aperturan o realizan dentro o fuera de Guatemala. Dichas cuentas bancari as [sic bancarias] deberán aparecer detalladas en el libro de inventarios, especificando en el mismo, el número de la cuenta, la institución bancaria en la que se encuentra, el tipo de cuenta, y el monto al cierre del ejercicio contable." / "En el caso de las inversiones, se deberá detallar el monto de la inversión, la clase de inversión, la institución en la que se encuentra, especificando si es nacional o extranjera, y si es extranjera, se indicará el país en el que se encuentra." / estados financieros contents (fn7 = CC art. 377): "Cabe indicar que en el libro o Registro de Estados Financieros, contendrá: 1. El balance general de apertura y los ordinarios y extraordinarios 2. Los estados de pérdidas y ganancias 3. Cualquier otro estado que a juicio del comerciante sea necesario para mostrar su situación financiera." / "En todos los casos anteriores, las partidas contables del libro Diario, deberán estar soportadas por los documentos que originan la transacción." | Merchants obliged to keep accounting must record in it ALL bank accounts used for their mercantile transactions and for investments arising from the entity's capital or financial resources, whether opened or made inside or outside Guatemala; said bank accounts must appear detailed in the libro de inventarios, specifying the account number, the banking institution, the account type, and the amount at the accounting period's close. For investments: the amount, the class of investment, the institution, whether national or foreign, and if foreign, the country. (Estados-financieros contents = art. 377; Diario entries document-supported) | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | pp.5-6 (EVID-588) |
| LB-005 | 60_, thresholds + fiscal cap: "El Código de Comercio de Guatemala, establece que los comerciantes que tengan un activo total que no exceda de Q. 25,000.00, pueden omitir en su contabilidad los lib ros [sic libros] o registros enumerados anteriormente a excepción de aquellos que obliguen las leyes especiales." / "…aquellos comerciantes individuales cuyo activo total exceda de Q.20,000.00 y toda sociedad mercantil, están obligados a llevar su contabilidad por medio de cont adores.8 [sic contadores] Para efectos fiscales solo están obligados a habilitar y autorizar los anteriormente descritos." | The Commercial Code establishes that merchants whose total assets do not exceed Q25,000.00 may omit the books/registers enumerated above, except those compelled by special laws. Individual merchants whose total assets exceed Q20,000.00 and every mercantile society must keep their accounting through accountants. For tax purposes they are only obliged to legalize and authorize those previously described | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | p.6 (EVID-589) |
| LB-006 | 60_, IVA book matrix + field specs: "siempre que sean contribuyentes del Impuesto al Valor Agregado en el Régimen Normal o General, deberán llevar los libros siguientes: Libro de compras y servicios recibidos / Libro de ventas y servicios prestados.9" (fn9 = IVA art. 37) / "Para los contribuyentes del referido impuesto, inscritos en el Régimen de Pequeño Contribuyente, deberán solicitar la habilitación del siguiente libro: Libro de Compras y Ventas de Pequeño Contribuyente.10" (fn10 = IVA art. 49) / compras fields: "Serie, número y fecha de las facturas, facturas de pequeño contribuyente, notas de crédito, declaración aduanera de importación, escrituras públicas o facturas especiales, que respalden las adquisiciones de bienes y servicios. / Número de Identificación Tributaria y nombre completo del vendedor o prestador del servicio. / En los casos de facturas especiales si el vendedor no tuviere NIT, se consignará el número del documento de identificación personal. / Precio neto (sin incluir el impuesto), conforme a la separación efectuada de las compras e importaciones de bienes y de l a [sic la] adquisición de los servicios de acuerdo con cada una de las actividades de ventas realizadas. / IVA (crédito fiscal) conforme a la separación efectuada… / Asimismo, en cada período mensual, deberán efectuar un resumen en el libro de compras y servicios recibidos, separando las compras e importaciones de bienes y adquisición de servicios que correspondan a operaciones de ventas locales de exportación y a personas exentas." / ventas fields: "Serie, número y fecha de la factura, facturas de pequeño contribuyente, nota de débito, facturas especiales o escritura pública que respalden las ventas efectuadas y los servicios prestados. / NIT y nombre completo del comprador. / Valor total de las exportaciones y de las ventas exentas. / Precio neto, sin incluir el impuesto, de las ventas de bienes y de los servicios prestados. En el caso de pequeños contribuyentes, el precio neto es equivalente al monto total de la factura. / IVA, débito fiscal, correspondiente a las ventas y las prestaciones de servicios, excepto en el caso de los pequeños contribuyentes conforme lo establece el numeral anterior. / Cuando el contribuyente consolide sus ventas diarias debe utilizar un renglón para cada tipo de documento, indicando la serie y el primer y último número emitido. 11" (fn11 = RLIVA AG 5-2013 art. 39) | Whenever they are IVA taxpayers in the Régimen Normal or General, they must keep the following books: purchases-and-services-received book; sales-and-services-rendered book (IVA art. 37). Pequeño Contribuyente registrants must request the legalization of one book: Libro de Compras y Ventas de Pequeño Contribuyente (IVA art. 49). Purchases fields: serie, number and date of the supporting documents (facturas, pequeño-contribuyente facturas, credit notes, import customs declaration, public deeds, facturas especiales); seller's NIT and full name (DPI number if the facturas-especiales seller has no NIT); net price (tax excluded) per the separation made by sales activity; IVA (crédito fiscal) per the same separation; PLUS a monthly summary separating purchases/importations/services corresponding to local sales, export sales and exempt persons. Sales fields: document serie/number/date; buyer's NIT and full name; total value of exports and exempt sales; net price (tax excluded); for pequeño contribuyentes the net price equals the invoice's total amount; IVA débito fiscal except for pequeño contribuyentes per the prior numeral; daily sales consolidation uses one row per document type, stating the serie and the first and last numbers issued (RLIVA arts. 38-39) | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | pp.7-8 (EVID-590) |
| LB-007 | 60_, ISR side: "Conforme lo regulado en los artículos 40 numeral 1 y 3, del 42 numeral 3 y 4 de la Ley de Actualización Tributaria, los contribuyentes del Impuesto Sobre la Renta, inscritos en el Régimen Sobre las Utilidades de Actividades Lucrativas, deben respaldar la Declaración Jurada de Renta, con los siguientes documentos: Cuando se trate de contribuyente obligado a llevar contabilidad completa: Con los registros de balance general, estado de resultados, flujo de efectivo y estado de costo de producción, cuando corresponda. Los contribuyentes no obligados a llevar contabilidad completa: Deberán proporcionar información detallada del período de liquidación de sus ingresos, costos y gastos deducibles." / inventory fields: "1. Código del bien si lo tuviere 2. Nombre o denominación 3. Cantidad total 4. Unidad que se toma como medida 5. Precio de cada unidad 6. Valor total" (fn12 = Reglamento del Libro I de la LAT, D10-2012, contenido en AG 213-2013) / "Conforme lo regulado en el artículo 53 de la ley en mención, los contribuyentes del referido impuesto independientemente al régimen bajo el que se encuentren inscritos, (Régimen Sobre las Utilidades de Actividades Lucrativas o Régimen Opcional Simplificado Sobre Ingresos de Actividades Lucrativas) están obligados a llevar contabilidad de acuerdo con el Código de Comercio de Guatemala, asimismo, deberán cumplir con las obligaciones en materia de llevar libros, registros y estados financieros." | Per LAT arts. 40 (numerals 1 and 3) and 42 (numerals 3 and 4), ISR taxpayers enrolled in the Régimen Sobre las Utilidades de Actividades Lucrativas must back the sworn renta declaration with: full-accounting taxpayers — the registros of balance general, estado de resultados, flujo de efectivo and estado de costo de producción, when applicable; taxpayers not obliged to keep full accounting — detailed period information of income, costs and deductible expenses. Inventory of goods for sale carries 6 detail fields (code, name/denomination, total quantity, unit of measure, unit price, total value) per AG 213-2013. Per LAT art. 53, ISR taxpayers regardless of regime (Utilidades or Opcional Simplificado) must keep accounting per the Commercial Code of Guatemala and comply with the books, registers and financial-statements duties | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | pp.9-10 (EVID-591) |
| LB-008 | 60_, electronic books: "El artículo 29 "A" segundo párrafo, de la Ley del Impuesto al Valor Agregado, el cual fue adicionado por el artículo 6, del decreto del Congreso Número 4-2019 el cual entró en vigencia el 30 de octubre 2019, regula que los contribuyentes registrados en el Régimen de Factura Electrónica deberán utilizar un sistema electrónico de registro de operaciones y de documentación de soporte de todas las operaciones del giro normal del negocio del contribuyente. En este sistema se incluirán, según corresponda: 1. Libro de Inventarios; 2. Libro de primera entrada o diario; 3. Libro mayor o centralizador; 4. Libros de Estados Financieros; 5. Libros de compras y ventas y otros auxiliares que determinen las leyes específicas. Para tal efecto, la Administración Tributaria po [sic pondrá] a disposición de los contribuyentes, todas las herramientas electrónicas correspondientes para dar cumplimiento a lo establecido en el presente artículo." / "La resolución que emita la Administración cobrará [sic — tomará/adquirirá] vigencia tres meses posteriores a su notificación. La Administración Tributaria desarrollará y pondrá a disposición de los contribuyentes, por los medios que considere necesarios, el reglamento que regule la incorporación, requisitos y condiciones para operar en este régimen." / "¿Qué es el sistema de libros electrónicos? Es una herramienta web que se encuentra en la Agencia Virtual, la misma permite facilitar el registro de los documentos en el Libro de Compras y Ventas de Pequeño Contribuyente en forma electr ónica [sic electrónica], para el cumplimiento voluntario de sus obligaciones. La herramienta tiene la peculiaridad que permite facilitar a los pequeños contribuyentes inscritos en el Régimen FEL, cargar automáticamente los documentos tributarios electrónicos –DTE- de ventas o servicios prestados y los documentos generados de forma manual." | Article 29-"A" second paragraph of the IVA Law, added by article 6 of Congressional Decree 4-2019 (in force 30 October 2019), provides that taxpayers registered in the Régimen de Factura Electrónica must use an electronic system of operations registration and supporting documentation for all operations of the business's normal giro. Included in this system, as applicable: 1. Inventarios book; 2. first-entry/daybook; 3. mayor/centralizador; 4. Estados Financieros books; 5. purchases-and-sales books and other auxiliaries determined by specific laws. For that purpose the Tax Administration will make all corresponding electronic tools available to taxpayers. The resolution the Administration issues takes [printed "cobrará", sic] effect three months after its notification; the Administration will develop and make available the regulation governing incorporation, requirements and conditions to operate in this regime. The "sistema de libros electrónicos" is an Agencia Virtual web tool easing electronic recording in the PC Libro de Compras y Ventas for voluntary compliance; it lets pequeño contribuyentes enrolled in FEL automatically load the electronic tax documents (DTE) of sales/services rendered plus manually generated documents | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | p.11 (EVID-592) |
| LB-009 | 60_, sanctions: "Conforme el artículo 85 del Código Tributario, constituye infracción tributaria, no contar con la autorización y habilitación de los libros contables establecidos en el Código de Comercio de Guatemala y habilitados los libros que establecen las leyes tributarias específicas, dicha infracción es sancionada con cierre temporal de empresas, establecimientos o negocios." / procedure: "…la Administración Tributaria presenta memorial de solicitud para la aplicación del cierre temporal ante Juez competente, quien emite resolución señalando día y hora para celebración de audiencia oral, la cual también es notificada al contribuyente para que éste ejerza su derecho de defensa, inmediatamente de finalizada la audiencia, el Juez dicta la resolución que en derecho corresponda y notifica a las partes. Una vez firme la sentencia que de ser condenatoria, procederá la ejecución del cierre temporal." / "No llevar al día los libros u otros registros obligatorios establecidos, en el Código de Comercio de Guatemala y las leyes tributarias específicas, dicha infracción es sancionada con multa de Q.5,000.00 cada vez que se fiscalice.13" / "Llevar los libros y registros contables en forma distinta a la que obliga el Código de Comercio de Guatemala y las leyes tributarias específicas, dicha infracción es sancionada con multa de Q.5,000.00 cada vez que se fiscalice." (fn13 = "Ibídem, artículo 94 numeral 4") | Per Tax Code art. 85, it is a tax infraction not to have the authorization and legalization of the accounting books established in the Commercial Code and the legalization of the books established by specific tax laws; said infraction is sanctioned with temporary closure of businesses. Procedure: the Tax Administration files a memorial requesting the closure before the competent Judge, who issues a resolution setting date and hour for an oral hearing (also notified to the taxpayer for defense); immediately after the hearing the Judge rules and notifies the parties; once the judgment is firm, if condemnatory, the temporary closure is executed. Not keeping the obligatory books/registers up to date, and keeping the books in a form different from that required, are each sanctioned with a Q5,000.00 fine every time an inspection occurs (CT art. 94 numeral 4) | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | pp.12-13 (EVID-593) |
| LB-010 | 73_ (RM arancel), books-authorization fee row: "Autorización de Libros Pago Variable 29 Q 0.20 x Hoja" | Books authorization — variable payment; item 29, Q0.20 per hoja (sheet). The RM-side fee of the dual legalization only; 73_ prints NO date or instrument number (2022-label as-of, re-verify — R66); the numerals are OCR-damaged and the row is quoted exactly as printed | `gt/sources/73_RegistroMercantil_Aranceles_2022.pdf` | p.1, row 29 region (rows 28-46) (EVID-596; no-date identity EVID-594) |
| LB-011 | 60_ identity banner: "Intendencia de Asuntos Jurídicos — Departamento de Consultas — Unidad de Orientación Legal y Derechos del Contribuyente" / "OBLIGACIÓN DE SOLICITAR A LA ADMINISTRACIÓN TRIBUTARIA LA HABILITACIÓN DE LIBROS CONTABLES U OTROS REGISTROS, CONFORME EL CÓDIGO DE COMERCIO DE GUATEMALA Y LEYES TRIBUTARIAS ESPECÍFICAS, CUYO INCUMPLIMIENTO, ES SANCIONADO CON EL CIERRE TEMPORAL" / footer, every page: "Este material solo puede ser utilizado con fines ilustrativos y no sustituye la consulta de leyes y reglamentos correspondientes." | SAT Legal-Orientation Unit orientation paper (13 pp): obligation to request the Tax Administration's legalization of accounting books and other registers per the Commercial Code and specific tax laws, whose breach is sanctioned with temporary closure. Running footer: this material may be used for illustrative purposes only and does not substitute consultation of the corresponding laws and regulations. No version/date string printed; bounded below by the D-4-2019 citation (≥ 2019-10-30) | `gt/sources/60_SAT_Habilitacion_Libros.pdf` | p.1 title + footers passim (EVID-586) |

## 3. Functional Requirements

### 3.1 The dual-track status model (R62)

- **GT-COA-FR-034:** The system shall implement the per-book legalization
  status as TWO independent state dimensions on the legal-book registry:
  `rm_authorization_state` (the RM *autorización* track — registry facts
  surface owned by `01_books-anchor.md` GT-COA-FR-007) and
  `sat_habilitation_state` (the SAT *habilitación* track) — the CC books
  "deben estar autorizados por el Registro Mercantil y habilitados por la
  Administración Tributaria", tax-law books "únicamente deben estar
  habilitados por la Administración Tributaria". NO code path shall merge
  them into a single "legalization" status or fee (rejected myth, wave set —
  R62). Vocabulary guard: *autorización* = RM; *habilitación* = SAT — the
  word "habilitación" never appears in the CCom (EVID-521) and shall only
  ever be cited to the SAT corpus. (LB-001; LB-002; LB-003; EVID-587/507/
  521/522; R62)
- **GT-COA-FR-035:** The system shall carry the per-book REQUIRED-TRACK
  matrix as shared dated config, implementing the book-legalization map
  (EVID-605): (i) the four CC books (GT-COA-FR-002 set) → BOTH tracks;
  (ii) IVA books (art. 37 two books; art. 49 single PC book) → SAT
  habilitación only, never RM; (iii) ISR backing registros (LAT arts.
  40/42/53) → via the CC books (no separate legalization); plus an
  electronic-variant column ("subsumed in the REF electronic system" for
  FEL taxpayers — FR-054). The matrix row for "who must have it" follows
  the map as printed (comerciantes with contabilidad completa above the
  Q25,000 dated floor; NGOs per D-2-2003 art. 13 noted as map data).
  (LB-001; LB-006; EVID-587/590/591/605; R62)
- **GT-COA-FR-036:** The system shall seed the tax-law book rows of the
  registry per the IVA matrix: *Régimen Normal o General* → TWO books —
  *Libro de compras y servicios recibidos* and *Libro de ventas y
  servicios prestados* (IVA art. 37); *Régimen de Pequeño Contribuyente* →
  ONE book — *Libro de Compras y Ventas de Pequeño Contribuyente* (IVA
  art. 49; statutory hook = GT-TAX-FR-066 by exact id; operational book
  surface = GT-FIN-FR-086 by id — never re-derived). Applicability keys on
  the company's IVA regime dimension. (LB-006; EVID-587/590; GT-TAX-FR-066;
  GT-FIN-FR-086)
- **GT-COA-FR-037:** The system shall enforce the RM-scope guard: art. 372
  enumerates EXACTLY the four CC books for RM autorización — auxiliary
  books (GT-COA-FR-004) and tax-law books (FR-036) NEVER receive RM
  authorization, and no surface shall offer it for them.
  (LB-002; EVID-507/521)
- **GT-COA-FR-038:** The system shall record the per-book medium choice:
  "Los libros contables podrán ser manuales o computarizados, a
  conveniencia del contribuyente o responsable tributario" — a manual/
  computerized flag on the book record, taxpayer's choice, both media
  equally legal for the habilitación surface (legality basis of
  computerized medium in the CCom = GT-COA-FR-005, consumed by id).
  (LB-001; EVID-587)
- **GT-COA-FR-039:** The system shall implement the fee-split guard:
  the RM authorization fee is the RM-side charge only (FR-041), and NO
  SAT-side habilitation fee is evidenced anywhere in the corpus — the
  SAT-7121 flow prints no fee (GT-FIN-FR-089 consumed by id). No single
  "book legalization fee" shall ever be modeled; no fee row shall be
  attached to the SAT track. Rejected myth (wave set): "RM autorización
  and SAT habilitación are one track / one fee" — R62.
  (LB-001; LB-010; EVID-587/596; GT-FIN-FR-089; R62)

### 3.2 RM autorización mechanics (art. 372; 73_ fee row; GOQ-125)

- **GT-COA-FR-040:** The system shall provide the RM autorización surface
  for the four CC books: registry facts (authorization date, hojas/folios
  authorized, book identity, RM office) recorded per book, plus the
  transitorio-IX rollout note as provenance (RM of the capital from
  vigencia; other registries per MinEconomía). The present-day procedure
  for RM authorization of COMPUTERIZED books is outside the corpus (art.
  333's "sistemas más modernos" hook) — the surface is shipped with the
  re-verify flag and GOQ-125 rides it (OQ-001); the physical act is
  external, the system records facts only. (LB-002; EVID-507/587; GOQ-125)
- **GT-COA-FR-041:** The system shall store the RM books-authorization
  fee as D16 dated-2022-label rows: "Autorización de Libros Pago Variable
  29 Q 0.20 x Hoja" — Q0.20 per hoja plus a "pago variable" component;
  instrument = the RM arancel (73_), which prints NO date or number
  (label-derived 2022 as-of; the arancel's own supersession-cycle rows
  make the snapshot likely stale) — every row carries the re-verify flag
  (R66) and no valid_to is asserted until re-verified. The per-sheet basis
  makes the charge book-thickness-dependent: it is recorded as exposure on
  the authorization surface, never auto-computed or auto-charged. The RM
  fee rail (full arancel catalog, collection mechanics) is owned by the C3
  file (`../../commercial-legal/01_rm-surfaces.md`, forward ref — file +
  cluster only). (LB-010; EVID-596/594; R66)

### 3.3 SAT habilitación mechanics (SAT-7121; GOQ-129)

- **GT-COA-FR-042:** The system shall record the SAT habilitación channel
  facts per book: habilitación requested "en cualquier agencia u oficina
  tributaria del país", or via Agencia Virtual using *formulario SAT-7121
  "Habilitación y autorización de libros"* following the portal steps —
  the wizard surface captures channel (in-person office / Agencia
  Virtual), form number and request facts. The SAT-7121 registry-echo row
  is owned by fin01 (GT-FIN-FR-020, consumed by id); the form's own
  page-scoping note (Impuesto de Timbres Fiscales) travels with that row,
  not re-derived here. (LB-001; EVID-587; GT-FIN-FR-020)
- **GT-COA-FR-043:** The system shall ingest the SAT-track output: the
  *resolución de habilitación de libros* (resolution reference, date,
  hojas habilitadas) recorded as the `sat_habilitation_state = habilitado`
  fact per book; the Agencia-Virtual portal flow states are ingested on
  the SaaS side (solicitud → processing → resolución), with fin03's
  GT-FIN-FR-089 consumed by id as the printed pequeño instantiation
  (SAT-7121 in Declaraguate → boleta SAT 2000 → re-enter → print the
  resolución — again, NO fee amount printed anywhere in that flow). The
  hojas-habilitadas fact feeds fin04's folio-continuity bridge
  (GT-FIN-FR-118) — pointer-only, never re-modeled.
  (LB-001; EVID-587; GT-FIN-FR-089/118/020)
- **GT-COA-FR-044:** The system shall carry the 60_ banner discipline on
  every 60_-derived row: the illustrative-only footer ("Este material solo
  puede ser utilizado con fines ilustrativos y no sustituye la consulta de
  leyes y reglamentos correspondientes.") plus the undated-snapshot bound
  (no version/date printed; ≥ 2019-10-30 via the D-4-2019 citation) ride
  as a provenance flag; legal force is attributed ONLY to the instruments
  60_ cites (§2), never to 60_ itself; and the SAT-7121 flow, steps and
  URLs are re-verified against the current SAT portal BEFORE the
  habilitación wizard is built (GOQ-129 → OQ-002).
  (LB-011; EVID-586; GOQ-129)

### 3.4 Book contents owned by this cluster from the 60_ restatement (EVID-588/589/591)

- **GT-COA-FR-045:** The system shall implement the bank-accounts register
  inside the *libro de inventarios*: ALL bank accounts used for mercantile
  transactions and for investments arising from the entity's capital or
  financial resources — including accounts opened or maintained outside
  Guatemala — detailed with account number, banking institution, account
  type, and the amount at the accounting period's close (one2many detail
  rows on the inventarios book record, exercised at each cierre).
  (LB-004; EVID-588)
- **GT-COA-FR-046:** The system shall implement the investments register
  inside the *libro de inventarios*: each investment detailed with amount,
  class of investment, institution, whether national or foreign, and — if
  foreign — the country in which it is located.
  (LB-004; EVID-588)
- **GT-COA-FR-047:** The system shall enforce the LAT art. 53 regime guard
  as dated config: EVERY ISR taxpayer, regardless of regime (*Régimen
  Sobre las Utilidades* or *Régimen Opcional Simplificado Sobre Ingresos
  de Actividades Lucrativas*), "están obligados a llevar contabilidad de
  acuerdo con el Código de Comercio de Guatemala" plus the books,
  registers and financial-statements duties — no profile shall waive the
  CC-based contabilidad or the book registry for Opcional Simplificado
  enrollment by regime alone (the CC-side Q25,000 omission floor of
  GT-COA-FR-003 remains the only CC-books omission route, and it never
  waives special-law books). (LB-007; EVID-591; GT-COA-FR-003)
- **GT-COA-FR-048:** The system shall provide the ISR backing-statement
  surface: *Régimen Sobre las Utilidades* taxpayers back the annual
  *Declaración Jurada de Renta* with the registros of *balance general*,
  *estado de resultados*, *flujo de efectivo* and *estado de costo de
  producción* (when applicable) if obliged to full contabilidad;
  taxpayers not obliged to full contabilidad back it with detailed period
  information of income, costs and deductible expenses — modeled as
  statement-record kinds on the FS-cycle surface of GT-COA-FR-016/017
  (consumed by id), each declaration cycle linked to its backing
  statements. (LB-007; EVID-591; GT-COA-FR-016/017)
- **GT-COA-FR-049:** The system shall implement the six-field inventory
  detail per AG 213-2013 on the inventory register: (1) código del bien
  (if any), (2) nombre o denominación, (3) cantidad total, (4) unidad de
  medida, (5) precio de cada unidad, (6) valor total — the column set of
  the inventarios book's goods-for-sale detail.
  (LB-007; EVID-591)
- **GT-COA-FR-050:** The system shall implement the "para efectos
  fiscales" cap as a fiscal-scope row: for tax purposes only the books
  described — the CC four-book set plus the tax-law books of FR-036 — are
  the habilitación/autorización universe ("Para efectos fiscales solo
  están obligados a habilitar y autorizar los anteriormente descritos").
  The Q25,000 omission floor and Q20,000 contador floor restated by 60_
  are CONSUMED from `01_books-anchor.md` GT-COA-FR-003/GT-COA-FR-014 by
  exact id as 1970-nominal dated rows (never indexed — R67; GOQ-126 kin) —
  never re-derived here. (LB-005; EVID-589; GT-COA-FR-003/014; R67)

### 3.5 Tax-law bookkeeping specs (RLIVA arts. 38-39)

- **GT-COA-FR-051:** The system shall implement the *Libro de compras y
  servicios recibidos* field spec per RLIVA art. 38 as the purchases-journal
  column design: document serie + number + date (facturas, facturas de
  pequeño contribuyente, notas de crédito, declaración aduanera de
  importación, escrituras públicas, facturas especiales); seller's NIT +
  full name (DPI number consigned for facturas especiales when the seller
  has no NIT); precio neto (tax excluded) separated according to the sales
  activity classes; IVA crédito fiscal under the SAME separation; and a
  MONTHLY SUMMARY row set separating purchases/importations of goods and
  acquisition of services corresponding to local sales, export sales and
  exempt persons — the crédito split by output class is a column-group
  invariant of the book.
  (LB-006; EVID-590)
- **GT-COA-FR-052:** The system shall implement the *Libro de ventas y
  servicios prestados* field spec per RLIVA art. 39: document serie +
  number + date (factura, facturas de pequeño contribuyente, nota de
  débito, facturas especiales, escritura pública); buyer's NIT + full
  name; total value of exports and of exempt sales; precio neto (tax
  excluded); IVA débito fiscal (excepted for pequeño contribuyentes per
  the prior numeral); and the DAILY CONSOLIDATION idiom — when the
  taxpayer consolidates daily sales, one row per document type stating the
  serie and the first and last numbers issued.
  (LB-006; EVID-590)
- **GT-COA-FR-053:** The system shall implement the pequeño contribuyente
  net rule of the single combined book: "En el caso de pequeños
  contribuyentes, el precio neto es equivalente al monto total de la
  factura" — net = invoice total, no débito fiscal column for PC rows
  (RLIVA art. 38 penúltimo-párrafo relation as printed by 60_). The
  statutory hook is GT-TAX-FR-066 and the operational column/row engine is
  GT-FIN-FR-086/087/088 — all consumed by exact id; this FR owns only the
  matrix-level net=total rule inside the dual-track book set.
  (LB-006; EVID-590; GT-TAX-FR-066; GT-FIN-FR-086/087)

### 3.6 Electronic-books bridge (IVA art. 29-"A"; D-4-2019 art. 6)

- **GT-COA-FR-054:** The system shall model the electronic-books subsumption
  as the third legalization variant: taxpayers registered in the *Régimen
  de Factura Electrónica* must use "un sistema electrónico de registro de
  operaciones y de documentación de soporte" of all giro-normal operations,
  including, as applicable, the FIVE book categories — (1) Libro de
  Inventarios; (2) Libro de primera entrada o diario; (3) Libro mayor o
  centralizador; (4) Libros de Estados Financieros; (5) Libros de compras
  y ventas y otros auxiliares que determinen las leyes específicas —
  recorded as the `electronic_variant` flag on the matrix (FR-035).
  Provenance: IVA art. 29-"A" 2nd paragraph, added by D-4-2019 art. 6, "el
  cual entró en vigencia el 30 de octubre 2019" (version + effective date
  as D12/D16 rows); the statutory text is owned by e-invoicing
  (`../e-invoicing/04_mandate-onboarding.md` LB-003 — cited by pointer,
  never restated), and the post-2018 consolidated IVA text caveat rides it
  (GOQ-01 kin → OQ-005). FEL/DTE archive duties stay in the GT-EINV wave
  (outcome-only cross-ref). (LB-008; EVID-592; GOQ-01 kin)
- **GT-COA-FR-055:** The system shall record the duty-allocation row: "la
  Administración Tributaria pondrá [printed "po", sic] a disposición de
  los contribuyentes, todas las herramientas electrónicas
  correspondientes" — SAT's tool-provisioning duty is recorded exposure on
  the electronic-variant surface (the taxpayer duty is to OPERATE an
  electronic system when in the REF regime); the system never emulates
  SAT's tools. (LB-008; EVID-592)
- **GT-COA-FR-056:** The system shall record the resolución-vigencia rule
  verbatim with its defect: "La resolución que emita la Administración
  cobrará [sic — tomará/adquirirá] vigencia tres meses posteriores a su
  notificación" — effective three months after notification; and the
  regime-reglamento allocation: SAT develops and makes available the
  regulation governing incorporation, requirements and conditions to
  operate in the regime. The verb defect and the unclear antecedent (which
  resolución the 3-month clause binds) are recorded, not resolved — GOQ-130
  (OQ-003). (LB-008; EVID-592; GOQ-130)
- **GT-COA-FR-057:** The system shall pair the Agencia-Virtual *sistema de
  libros electrónicos* with the book registry on the SaaS side: a web tool
  inside Agencia Virtual easing electronic recording in the PC *Libro de
  Compras y Ventas* for VOLUNTARY compliance; pequeño contribuyentes
  enrolled in FEL get automatic loading of electronic tax documents (DTE)
  of sales/services rendered plus manually generated documents; non-FEL
  PCs can key monthly purchases and generate the monthly declaration. LET
  mechanics — eligibility gate and folio continuity — are owned by fin04
  and consumed by exact id, pointer-only: GT-FIN-FR-104 (active
  habilitación-precondition gate), GT-FIN-FR-118 (folio-continuity
  bridge). (LB-008; EVID-592; GT-FIN-FR-104/118)

### 3.7 Sanction gates and track separation (CT arts. 85/94.4 via taxation)

- **GT-COA-FR-058:** The system shall implement the legalization-gap
  PREDICATE (this file's only sanction surface — the machinery is taxation's,
  consumed by id): per book, a missing required track (CC books: missing RM
  autorización OR SAT habilitación; tax-law books: missing SAT habilitación)
  marks the legalization-gap state, which is the CT art. 85 infraction
  feeding *cierre temporal* — sanction machinery = GT-TAX-FR-216 (10-20
  continuous days, juez de paz penal, oral audiencia; the judicial
  procedure as 60_ prints it: memorial → resolution setting the oral
  hearing → judgment → execution once firme) and GT-TAX-FR-217
  (commutation), never re-derived here. The art. 85.4 garbled-text caveat
  ("autorizado y habilitado… y habilitado" [sic]) is consumed via
  GT-TAX-FR-231 — GOQ-56 kin (OQ-004). Exposure is recorded, never
  computed as a workflow. (LB-009; EVID-593; GT-TAX-FR-216/217/231;
  GOQ-56 kin)
- **GT-COA-FR-059:** The system shall implement the books-condition
  predicates that fire the Q5,000 formal-duty multas, each "cada vez que
  se fiscalice" (CT art. 94 num. 4): (i) books not kept *al día* — the
  currency metric and 2-month test are GT-TAX-FR-231, consumed by id; (ii)
  books kept "en forma distinta a la que obliga" the CCom and the specific
  tax laws (the form-conformity predicate over FR-038's medium and the
  §3.4/§3.5 content specs). The multa rows themselves are GT-TAX-FR-214
  rows 4 and 5 — consumed by exact id; this FR owns only the per-book
  predicates. (LB-009; EVID-593; GT-TAX-FR-214/231)
- **GT-COA-FR-060:** The system shall enforce the sanction-track separation
  guard (R62): the RM track's sanction (CCom art. 370 multa band Q100-Q1,000
  per case, imposed by the Registro Mercantil = GT-COA-FR-020, consumed by
  id) and the SAT/CT track's sanctions (cierre temporal + Q5,000 multas —
  FR-058/059) are SEPARATE registers with separate enforcers, exposed as
  distinct exposure rows; no surface shall merge, net or convert between
  them. (LB-003; EVID-521/587/593; GT-COA-FR-020; R62)

## 4. Data Model

Layer semantics: the dual-track status model, required-track matrix,
thresholds and RM fee rows are dated config shared across the architecture;
the wizard surfaces and bookkeeping book specs live in the Odoo client;
portal-resolución ingestion and the Agencia-Virtual DTE auto-load pairing
live on the SaaS side (with fin04). The system records compliance facts —
it never emulates the Registro Mercantil, SAT or the courts, and never
charges either authority's fees. No printed data table in this file
warrants a CSV sidecar (small config sets; the matrix and fee rows are
seed rows).

**Dual-track legalization status (extends l10n_gt_commerce.book, `01_books-anchor.md` §4):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.book | sat_habilitation_state | select + date + ref | pending · solicited · habilitado (resolución ref + date + hojas habilitadas) — SEPARATE dimension from rm_authorization_state (T1 FR-007), never merged | FR-034, FR-043 |
| l10n_gt_commerce.book | track_required | computed | both (CC four books) · sat_only (IVA books) · via_cc_books (ISR registros) | FR-035, FR-036, FR-037 |
| l10n_gt_commerce.book | electronic_variant | boolean + regime ref | subsumed in the REF electronic system (IVA art. 29-"A"; set for FEL taxpayers' five categories) | FR-035, FR-054 |
| l10n_gt_commerce.book | medium | select | manual · computerized (taxpayer's choice) | FR-038 |
| l10n_gt_commerce.book | bank_account_rows | one2many | account_no · institution · account_type · closing_amount · country_jurisdiction (foreign accounts included by law) — inventarios book only, at each ejercicio close | FR-045 |
| l10n_gt_commerce.book | investment_rows | one2many | amount · class · institution · national_foreign · country_if_foreign — inventarios book only | FR-046 |
| l10n_gt_commerce.book | isr_backing_kinds | tags on FS cycle | balance_general · estado_resultados · flujo_efectivo · estado_costo_produccion · detailed_period_info (non-full-contabilidad) | FR-048 |
| l10n_gt_commerce.book | inventory_detail_fields | const set | código · nombre/denominación · cantidad_total · unidad_medida · precio_unitario · valor_total (AG 213-2013) | FR-049 |

**Book-legalization map seed (EVID-605, as printed):**

| Book/registro | Who must have it | RM autorización | SAT habilitación | Electronic variant |
|---|---|---|---|---|
| Inventarios; Primera entrada o diario; Mayor o centralizador; Estados financieros | comerciantes with contabilidad completa (activo > Q25,000 dated row; NGOs per D-2-2003 art. 13) | YES (CC art. 372; Q0.20/hoja per 73_) | YES (any agency / SAT-7121) | subsumed in REF electronic system (IVA art. 29-"A") |
| Libro compras y servicios recibidos + Libro ventas y servicios prestados | IVA Régimen Normal/General (IVA art. 37) | no | YES only | same |
| Libro de Compras y Ventas de Pequeño Contribuyente | IVA Pequeño Contribuyente (IVA art. 49) | no | YES only | SAT web tool, DTE auto-load for FEL PCs |
| ISR backing registros (balance, resultados, flujo, costo producción) + inventory detail | ISR taxpayers (LAT arts. 40/42/53) | via CC books | via CC books | same |

**Dated config rows (l10n_gt_commerce.dated_value — D16: instrument + valid_from/valid_to + provenance + flags):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt_commerce.dated_value | rm_book_authorization_fee | monetary + flag | Q0.20/hoja + pago_variable=true; instrument = RM arancel 73_ (prints NO date — 2022-label as-of); re_verify flag R66; no valid_to asserted until re-verified | FR-041 |
| l10n_gt_commerce.dated_value | sat_habilitation_fee | NO ROW BY DESIGN | absence is the requirement — no SAT-side fee evidenced in any corpus document (guard comment in the seed; GT-FIN-FR-089 consumed) | FR-039 |
| l10n_gt_commerce.dated_value | cc_omission_floor · cc_contador_floor | consumed | T1 FR-003/FR-014 rows — consumed by id, never re-derived (1970-nominal, GOQ-126 kin) | FR-050 |
| l10n_gt_commerce.dated_value | fiscal_scope_cap | const | fiscal-side legalization universe = CC four books + tax-law books only ("para efectos fiscales") | FR-050 |
| l10n_gt_commerce.dated_value | art29a_regime | regime row | IVA art. 29-"A" 2nd ¶, added D-4-2019 art. 6; vigencia 30-oct-2019; 60_-banner provenance flag (≥ 2019-10-30, illustrative-only) | FR-044, FR-054 |

**IVA book column catalogs (RLIVA arts. 38-39; seed columns on the purchase/sales journal surfaces):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| compras journal (book spec) | columns | const set | doc_serie · doc_numero · doc_fecha (facturas/FPC/notas de crédito/declaración aduanera/escrituras públicas/facturas especiales) · NIT · nombre · precio_neto (by sales class) · iva_crédito (by sales class) | FR-051 |
| compras journal (book spec) | monthly_summary | computed row set | per period, separating local-sales / export / exempt-persons purchases+importations+services | FR-051 |
| ventas journal (book spec) | columns | const set | doc_serie · doc_numero · doc_fecha · NIT · nombre · total_exportaciones · total_ventas_exentas · precio_neto · iva_débito (PC rows: none) | FR-052 |
| ventas journal (book spec) | daily_consolidation | row idiom | one row per document type: serie + primer y último número emitido | FR-052 |
| PC combined book (book spec) | net_rule | const | precio neto = monto total de la factura; no débito column (engine = GT-FIN-FR-086/087 by id) | FR-053 |

**Sanction-predicate exposure rows (consumed by the taxation sanction evaluator; this file owns only the predicates):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| book legalization exposure | legalization_gap | computed boolean | any required track missing (CC books: either; tax books: SAT) → CT art. 85 row → GT-TAX-FR-216/217 by id | FR-058 |
| book legalization exposure | not_al_dia · wrong_form | computed booleans | currency test = GT-TAX-FR-231 by id; form conformity over medium + content specs → GT-TAX-FR-214 rows 4/5 by id | FR-059 |
| book legalization exposure | track_separation | const guard | RM multa band exposure (T1 FR-020) and CT-track exposure never merged/netted (R62) | FR-060 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture D2, wave defaults): `shared` =
the dual-track status model, required-track matrix, thresholds, fiscal-scope
cap and RM fee tables — dated config both sides must honor identically;
`odoo` = the habilitación/autorización wizard surfaces, book registry
fields and bookkeeping book specs in the LGPL client; `saas` =
portal-resolución ingestion from the Agencia Virtual flow and the
Agencia-Virtual DTE auto-load pairing (with fin04), plus the sanction
evaluator that consumes FR-058/059 predicates (D2 dual-validation). Model
names are stable across Odoo 17/18/19/20; no version-specific behavior is
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-034 | shared | l10n_gt_commerce.book | rm_authorization_state + sat_habilitation_state | Two independent dimensions; merge guard; vocabulary R62; T1 FR-007 consumed |
| FR-035 | shared | l10n_gt_commerce.book + map seed | track_required, electronic_variant | EVID-605 map as seed config; consumed by both sides |
| FR-036 | shared | l10n_gt_commerce.book seed | tax-law book rows keyed on IVA regime | GT-TAX-FR-066 + GT-FIN-FR-086 consumed by id |
| FR-037 | shared | registry guard | — | RM autorización offered only for the four CC books (art. 372 enumeration) |
| FR-038 | odoo | l10n_gt_commerce.book | medium | manual/computerized at taxpayer choice; legality basis = T1 FR-005 by id |
| FR-039 | shared | dated_value guard | sat_habilitation_fee = no row | No SAT-side fee evidenced (GT-FIN-FR-089 by id); never a single legalization fee — R62 |
| FR-040 | odoo | l10n_gt_commerce.book | RM-track facts + wizard | Computerized-books procedure open — GOQ-125 flag rides the surface (OQ-001) |
| FR-041 | shared | l10n_gt_commerce.dated_value | rm_book_authorization_fee | Q0.20/hoja + pago variable; 2022-label, re-verify R66; exposure only, never auto-charged; fee rail = C3 forward ref |
| FR-042 | odoo | habilitación wizard | channel + SAT-7121 facts | Any agencia/oficina or Agencia Virtual; registry echo = GT-FIN-FR-020 by id |
| FR-043 | saas | portal ingestion + book registry sync | resolución ref, hojas habilitadas | Agencia-Virtual flow ingestion; GT-FIN-FR-089 = printed pequeño instantiation; folio feed = GT-FIN-FR-118 pointer-only |
| FR-044 | shared | provenance flags on all 60_-derived rows | illustrative + ≥2019-10-30 bound | 60_ never law; SAT-7121 flow/URLs re-verified pre-build — GOQ-129 (OQ-002) |
| FR-045 | odoo | l10n_gt_commerce.book | bank_account_rows | All accounts incl. abroad; four mandated fields at ejercicio close |
| FR-046 | odoo | l10n_gt_commerce.book | investment_rows | Amount, class, institution, national/foreign + country |
| FR-047 | shared | regime-applicability config | lat53_guard | Opcional Simplificado owes CC-based contabilidad; only T1 FR-003's floor omits CC books |
| FR-048 | odoo | FS-cycle statement records | isr_backing_kinds | 4 statements (full contabilidad) / detailed period info (non-full); T1 FR-016/017 consumed |
| FR-049 | odoo | inventory register surface | 6-field column set | AG 213-2013 detail fields |
| FR-050 | shared | l10n_gt_commerce.dated_value | fiscal_scope_cap + consumed floors | "Para efectos fiscales" cap; Q25,000/Q20,000 = T1 FR-003/014 by id (1970-nominal, GOQ-126 kin) |
| FR-051 | odoo | purchases journal book spec | RLIVA-38 columns + monthly summary | Crédito split by local/export/exempt class |
| FR-052 | odoo | sales journal book spec | RLIVA-39 columns + daily consolidation | Export/exempt totals; serie + first/last number per doc type |
| FR-053 | odoo | PC combined book spec | net = invoice total | No débito column for PC rows; engine = GT-FIN-FR-086/087/088 by id |
| FR-054 | shared | electronic-variant config | art29a_regime row | Five categories subsumed; D-4-2019 art. 6, vigencia 30-oct-2019; statutory text = e-invoicing/04 LB-003 pointer; GOQ-01 kin |
| FR-055 | shared | exposure row | SAT tool-provisioning duty | Recorded exposure; system never emulates SAT's tools |
| FR-056 | shared | dated rule row | resolución vigencia = notification + 3 months | Verbatim with [sic "cobrará"]; GOQ-130 (OQ-003) |
| FR-057 | saas | Agencia-Virtual pairing | PC web tool + DTE auto-load | Voluntary compliance; LET mechanics = GT-FIN-FR-104/118 pointer-only |
| FR-058 | shared | legalization exposure | legalization_gap predicate | Feeds GT-TAX-FR-216/217 (cierre temporal + commutation) by id; GOQ-56 kin via GT-TAX-FR-231 |
| FR-059 | shared | legalization exposure | not_al_dia / wrong_form predicates | Currency test = GT-TAX-FR-231; multa rows = GT-TAX-FR-214 rows 4/5 — by id |
| FR-060 | shared | exposure guard | track separation | RM multa band (T1 FR-020) ≠ CT track; never merged — R62 |

Version-regime notes (D12/D15/D16): every 60_-derived row resolves as-of
the domain anchor date with the illustrative-banner provenance flag and the
≥ 2019-10-30 snapshot bound (FR-044); the art. 29-"A" regime row records
version (D-4-2019 art. 6) + effective date (30-oct-2019); the RM fee is a
dated-2022-label row with re-verify flag (R66) — snapshot-on-write, no
valid_to asserted until re-verified; the restated CC thresholds are
consumed from T1's 1970-nominal rows (R67, GOQ-126 kin). Sanction values
are recorded exposure only — never computed fines, never auto-triggered
closures.

## 6. Acceptance Criteria

- **AC-001:** Given any legal book of a GT company, when its legalization
  record is inspected, then it carries TWO independent status dimensions
  (RM autorización; SAT habilitación) with no merged field, and a book
  holding RM authorization alone still shows the SAT dimension as pending.
  (FR-034)
- **AC-002:** Given the registry of an IVA *Régimen Normal* taxpayer, when
  seeded, then it holds the two IVA books (compras y servicios recibidos;
  ventas y servicios prestados) with `track_required = sat_only` and NO RM
  authorization surface offered; and given a *pequeño contribuyente*, then
  exactly one combined book is seeded (GT-TAX-FR-066 hook, GT-FIN-FR-086
  surface — by id). (FR-035, FR-036, FR-037)
- **AC-003:** Given the RM fee configuration, when inspected, then the
  books-authorization row reads Q0.20/hoja + pago variable with the 2022
  label, the re-verify flag set and NO valid_to asserted; and no SAT-track
  fee row exists anywhere in the configuration.
  (FR-039, FR-041)
- **AC-004:** Given a book whose required tracks are not all in place,
  when the compliance exposure is evaluated, then the legalization-gap
  predicate fires and surfaces the CT art. 85 → cierre-temporal exposure
  consuming GT-TAX-FR-216/217 by id — with no closure workflow computed
  in this module. (FR-058)
- **AC-005:** Given a book whose entries lag more than the 2-month test
  (GT-TAX-FR-231 by id) or whose form deviates from the mandated specs,
  when exposure is evaluated, then the not-al-día / wrong-form predicates
  surface the Q5,000-per-fiscalización rows via GT-TAX-FR-214 rows 4/5 by
  id — and the RM multa band remains a separate, never-netted exposure
  row. (FR-059, FR-060)
- **AC-006:** Given a *Régimen de Factura Electrónica* taxpayer, when the
  book matrix renders, then the five book categories carry the
  electronic-variant flag with provenance "IVA art. 29-'A', added by
  D-4-2019 art. 6, in force 30-oct-2019", and the resolución-vigencia rule
  displays verbatim with the [sic "cobrará"] flag retained.
  (FR-054, FR-056)
- **AC-007:** Given a pequeño contribuyente enrolled in FEL, when the
  Agencia-Virtual pairing is active, then sales/services DTEs and manually
  generated documents auto-load into the electronic Libro de Compras y
  Ventas pairing surface, with LET eligibility/folio mechanics delegated
  to GT-FIN-FR-104/118 by id. (FR-057)
- **AC-008:** Given a GT company's ejercicio close, when the libro de
  inventarios is generated, then it carries the bank-accounts register
  (number, institution, type, closing amount — foreign accounts included)
  and the investments register (amount, class, institution,
  national/foreign + country). (FR-045, FR-046)
- **AC-009:** Given an ISR taxpayer enrolled in *Opcional Simplificado*,
  when the book-registry profile applies, then the CC-based contabilidad
  obligation stands (no regime-level waiver), while an individual merchant
  under the Q25,000 dated floor keeps the T1 FR-003 omission route with
  special-law books surviving. (FR-047; GT-COA-FR-003)
- **AC-010:** Given a *Régimen Sobre las Utilidades* declaration cycle,
  when backed, then full-contabilidad taxpayers link the four backing
  registros (balance general, estado de resultados, flujo de efectivo,
  estado de costo de producción when applicable) and non-full taxpayers
  the detailed period information; and the goods-for-sale inventory
  detail renders the six AG 213-2013 fields. (FR-048, FR-049)
- **AC-011:** Given any row derived from 60_, when inspected, then it
  carries the illustrative-only banner flag and the ≥ 2019-10-30 snapshot
  bound, and no row cites 60_ as legal force (force attributed only to the
  instruments it cites). (FR-044)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
this file owns GOQ-125/129/130 for the C2 rows, with GOQ-56 and GOQ-01 as
kin where the CT art. 85.4 garbled text and the art. 29-"A" current text
are touched, and GOQ-126 as threshold kin. GOQ-124 (retention/destruction
matrix) is the Task 7 deliverable that consumes this file's
legalization-status rows as matrix inputs — not an open question of this
file. GOQ-123 rides every 66_ citation family (owned by `01_books-anchor.md`).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-125 (owned): "RM autorización of computerized books: exact present-day procedure outside corpus (art. 333 lets RM books be replaced by 'sistemas más modernos')." FR-040 ships the RM-track facts surface with the re-verify flag; the computerized-books procedure (form, channel, per-hoja basis for electronic records) must be verified against current RM practice before the wizard automates anything. | no | GT synthesis wave S-GT5 (acquisition queue) | open |
| OQ-002 | GOQ-129 (owned): "60_ currency: undated (≥ 30-oct-2019); SAT-7121 flow/URLs may have changed — re-verify before building the habilitación wizard." FR-044 carries the banner + bound on every 60_-derived row; the portal URL and step sequence in FR-042/LB-001 are the ≥2019 print, not verified current. | no | GT synthesis wave S-GT5 → W6 partner ask | open |
| OQ-003 | GOQ-130 (owned): "60_ p.11 'La resolución … cobrará [sic] vigencia tres meses posteriores a su notificación' — verb defect + unclear antecedent (REF incorporation? art. 29 'A' resolutions?)." FR-056 records the rule verbatim with the [sic] flag and computes nothing from the 3-month window until the antecedent resolves (kin: e-invoicing/04 LB-003 carries the same "cobrará" string in the SAT-DSI-639-2020 quote — acquisition candidate). | no | GT synthesis wave S-GT5 (acquisition queue) | open |
| OQ-004 | GOQ-56 (kin): art. 85.4 prints the redundant "…autorizado y habilitado… y habilitado…" [sic] — the cierre-infraction text this file's legalization-gap predicate feeds is consumed via GT-TAX-FR-231 (sense pending the clean edition there); FR-058 quotes only 60_'s art. 85 paraphrase, never the garbled statute text. | no | TX6 owner (taxation/06 §7); this file kin-cites | open |
| OQ-005 | GOQ-01 (kin): the post-2018 consolidated Ley IVA text — art. 29-"A" body as currently consolidated — is not in this corpus; FR-054's regime row cites 60_'s rendition + e-invoicing/04 LB-003 provenance and rides the currency caveat until the consolidated print lands. | no | GT synthesis wave S-GT5 (acquisition queue; folds into GOQ-01) | open |
| OQ-006 | GOQ-126 (kin): the Q25,000 omission floor and Q20,000 contador floor restated by 60_ (FR-050) are consumed from T1's 1970-nominal dated rows — verify against modern instruments/RTU before configuration (R67); no value in this file is derived from them beyond the T1 rows. | no | GT synthesis wave S-GT5 (verify-before-config gate) | open |
