# GT — Fiscal reporting — Pequeño contribuyente regime chain & libro de compras y ventas

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | fiscal-reporting |
| Status  | draft |
| Authors | GT synthesis wave S-GT4 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for cluster F3: the Guatemala
**Régimen de Pequeño Contribuyente** (small-taxpayer regime) two-document
operational chain — the undated ~2013 SAT digest `55_` (still live at the
2024-05-13 Wayback capture) and the ≥ ~2018-11 LET-era procedure `61_` — and
the **libro de compras y ventas** (purchases-and-sales book) obligation they
describe: the single combined SAT-habilitated book (columns, no-tax column,
daily one-row ventas consolidation, anulada/C.F. row idioms, manual o
computarizado); the SAT-7121 + boleta SAT-2000 → resolución de habilitación
flow; the LET operational layer (FEL auto-load, cierre order, 20-line
folios); the obligation set printed surfaces (factura title + "No genera
derecho a crédito fiscal" legend, Q50 per-operation floor with "Clientes
Varios"/NIT "CF" daily consolidation, purchase-factura demand duty); the
monthly declaración lifecycle with its form-number drift ledger (2043/2047/
2049 → 2046 → 2046/2241), whole-calendar-month window (LIVA art. 48),
unconditional zero-activity filing, retención credit, marca de caja and
payment rails; the ISR/ISO relief bundle prints; and the R56/R57 fidelity
guards (never copy the Q.179.00 rounding; never cite LIVA paragraph ordinals
from a digest).

It is the OPERATIONAL half of a two-layer contract: every statutory pequeño
value — threshold Q150,000 (R20 provenance), 5% definitive tarifa, Q50
invoice floor, Q2,500 retention floor, exit rule LIVA art. 50, ISR relief,
legend/title reglamento art. 30, sanction amounts — is owned by
`gt/requirements/taxation/02_iva-pequeno.md` (GT-TAX-FR-046..068) and
consumed here by exact FR id, never re-derived; sanction VALUES (CT art. 94
numerals 3/4/7/18, art. 94 "A") are owned by
`gt/requirements/taxation/06_ct-procedures.md` (GT-TAX-FR-214/215/226/231) —
cross-referenced only. Form REGISTRY identities (2046/2241 current
generation; predecessor chain 2043/2047/2049) are owned by Task 1
(`01_form-inventory-channels.md`, GT-FIN-FR-006/014/015) — this file owns
the drift LEDGER keyed by era. The PC 5% retention-agent surface is Task 2's
(`02_retenciones-web.md` GT-FIN-FR-034/039/069) — cross-referenced where it
touches pequeño.

It does **not** cover: the statutory pequeño regime itself (taxation/02 —
all GT-TAX-FR ids); the F4 LET manuals 57_/58_/82_ and the Informe
Electrónico 59_ (Task 4, `04_let-electronic-books.md` — 61_ is the earlier
procedure for the same book obligation, paired there by FR id); the FEL
DTE emission stack and the FEL mandate calendar for pequeños (e-invoicing
wave; `55_` carries zero FEL content — EVID-444); the RetWeb agent-side
operating system (Task 2); the SAT-2390 devolución channel (Task 5); the
Criterios interpretive layer (Task 6); the Código de Comercio books model
and the habilitación dual-track (SAT-7121 RM authorization vs electronic)
owned by the future S-GT5 COA wave — this file records only the 55_/61_
printed flow with a cross-ref pointer; and sanctions/procedures generally
(taxation/06).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble — fiscal
reporting): **manuals are PRIMARY for MECHANICS, SECONDARY for statutory
parameters**. `55_` = as-of-~2013 digest still live at the 2024-05-13
capture — **EVERY number it prints is a dated as-of-~2013 value, never
current** (GOQ-100 banner discipline); `61_` = ≥ ~2018-11 LET-era procedure
(URL-anchor epoch inference; "v3" label unprinted — GOQ-101); current-
generation form identities come from the 48_ registry (Task 1). Statutory
pequeño values live in taxation/02 (GT-TAX-FR-046..068) — consumed by exact
id; CT sanction values live in taxation/06 — cross-ref only. Both documents
are SAT orientation digests carrying the disclaimer "Este material solo
puede ser utilizado con fines ilustrativos y no sustituye la consulta de
leyes y reglamentos correspondientes." Dated rows follow D15/D16 (cite
together): the 55_/61_ chain and the form-number drift are dated layers
with as-of qualifiers, never silently merged. All quotes verified verbatim
against `gt/.extractions/55_61_Pequeno_libro.evidence.md` (EVID-431..450)
and the 55_/61_ committed text layers.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | 55_ identity/vintage: "Unidad de Orientación Legal y Derechos del Contribuyente — Departamento de Consultas — Intendencia de Asuntos Jurídicos" / worked-example headers "COMPRAS MES: Mayo 2013" (p.8), "VENTAS MES: Mayo 2013" (p.9) / fn.6: "Artículo 30 del Acuerdo Gubernativo Número 5-2013, Reglamento del Impuesto al Valor Agregado." / no printed date or version in 20 pp; task Wayback capture 2024-05-13 | SAT legal-orientation digest, no date/version printed anywhere; May-2013 worked examples and AG 5-2013 cited as in force prove a ~2013 body; capture 2024-05-13 proves only that the ~2013 text was still published then — every value is an as-of-~2013 dated value (GOQ-100) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via `gt/.extractions/55_SAT_PequenoContribuyente_guia.pdf.txt`) | p.1 header block; pp.8-9 examples; p.6 fn.6 (EVID-431) |
| LB-002 | 61_ identity/provenance: "PROCEDIMIENTO DE AUTORIZACIÓN, OPERACIÓN Y USO DEL LIBRO DE COMPRAS Y VENTAS DEL PEQUEÑO CONTRIBUYENTE" / "Unidad de Orientación Legal y Derechos del Contribuyente — Departamento de Consultas Tributarias — Intendencia de Asuntos Jurídicos" / URLs incl. "https://portal.sat.gob.gt/portal/requisitos-de-personas-empresas/#1541621044169-4198d06d-693f" / "Libro Electrónico Tributario –LET-" (p.4) / "Si emite FEL, el sistema cargará automáticamente los datos de sus facturas en Ventas." (p.7) / "Generar Formulario SAT-2046" (p.12); no printed date; "v3" NOT printed | SAT procedure manual for authorizing/operating the pequeño book, same orientation unit (department renamed Consultas Tributarias); URL anchor epoch-ms ≈ 2018-11-07 = an inferred content floor (not a printed date); LET/Agencia Virtual/FEL auto-load/SAT-2046 era; task's "v3" label unprinted (GOQ-101) | `gt/sources/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf` (via `gt/.extractions/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf.txt`) | 61_ p.1 title + unit; p.3 URLs; p.4; p.7; p.12 (EVID-445) |
| LB-003 | 55_ p.2 + fn.1: "Con la vigencia del Decreto 04-2012 del Congreso de la República de Guatemala…, la cual inició el 25 de febrero de 2012, se configura el nuevo Régimen de Pequeño Contribuyente, derivado de lo cual, a partir del 1 de abril del 2012, los contribuyentes inscritos en las anteriores modalidades denominadas Régimen Simplificado 5% y Pequeño Contribuyente, Declaración Anual, fueron inscritos de oficio en el mencionado régimen por la SAT, siempre que sus ingresos no hayan superado la suma de Q150,000.00 durante el año 2011." / "Pueden inscribirse en el Régimen de Pequeño Contribuyente las personas individuales o jurídicas cuyo monto de ventas de bienes o prestación de servicios no exceda de ciento cincuenta mil Quetzales (Q150,000.00) durante un año calendario, conforme lo establecen los artículos 45 y 46 de la Ley del Impuesto al Valor Agregado" / fn.1: "Artículos 45 y 46 de la Ley del Impuesto al Valor Agregado, reformados por los artículos 12 y 13 del Decreto 4-2012 del Congreso de la República." | Threshold ≤ Q150,000.00 annual gross (goods + services, año calendario) per LIVA arts. 45-46 reformed by D-4-2012 arts. 12-13, in force 25-Feb-2012; SAT migrated the two old modalities de oficio on 1-Apr-2012 (2011-income test ≤ Q150,000) — the R20-resolved attribution; eligible persons: individuales (incl. liberal professionals) y jurídicas (all mercantile society forms) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ p.2 intro + fn.1 (EVID-432) |
| LB-004 | 61_ p.2: "De conformidad con el Artículo 45 y 46 de la Ley del Impuesto al Valor Agregado, pueden inscribirse en el Régimen de Pequeño Contribuyente y Régimen Electrónico de Pequeño Contribuyente, las personas individuales o jurídicas cuyo monto de ventas de bienes o prestación de servicios no exceda de ciento cincuenta mil Quetzales (Q150, 000.00) [sic] durante un año calendario." / "…el artículo 50 de la norma legal citada, establece que los contribuyentes pueden permanecer en este régimen siempre que sus ingresos no superen la suma de Q150,000.00 durante el año calendario anterior, al superar dicha suma deberá solicitar su inscripción al Régimen General, de lo contrario la Administración Tributaria lo podrá inscribir de oficio en el Régimen Normal o General, dándole aviso de las nuevas obligaciones… y el período mensual a partir del cual inicia en el nuevo régimen." / "…el artículo 49… establece en el último párrafo que los contribuyentes inscritos en este régimen quedan relevados del pago y la presentación de la declaración anual, trimestral o mensual del Impuesto Sobre la Renta o de cualquier otro tributo acreditable al mismo." | 61_ adds: (i) a second affiliation variant — Régimen Electrónico de Pequeño Contribuyente — under the same Q150,000 test; (ii) the stay/exit rule (LIVA art. 50): prior-calendar-year income > Q150,000 forces solicitud to Régimen General, failing which SAT inscribes de oficio with notice + start period; (iii) ISR relief phrased as relief from payment AND presentation of any ISR declaration — same threshold/5% as 55_, no drift | `gt/sources/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf` (via txt) | 61_ p.2 (EVID-446) |
| LB-005 | 55_ pp.3-4: "…deberá acudir a cualquier Oficina o Agencia tributaria de la república y debe manifestar ante la Superintendencia de Administración Tributaria que, conforme la disposición legal vigente y tomando en cuenta que sus ingresos no superan la suma anual de Q.150,000.00, desea que se le inscriba en el Régimen de Pequeño Contribuyente." / "Cualquier contribuyente, que actualmente se encuentre afiliada [sic] en el régimen general del IVA… se percata que sus ingresos actuales no superan la suma mencionada durante el año calendario, podrá solicitar su afiliación al Régimen de Pequeño Contribuyente, ante la SAT en cualquier fecha." (fn.4: art. 46 D-27-92) / "La Administración Tributaria lo inscribirá, entregando la hoja de obligaciones correspondiente y el período mensual a partir del cual inicia a cumplir sus obligaciones tributarias en este régimen." | Opt-in mechanics: manifestation at any SAT office; general-regime taxpayers may switch at any date; inactive-NIT holders update in person anytime; SAT performs the inscription, issues the hoja de obligaciones and fixes the starting monthly period — regime start is SAT-determined, not petition-determined | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.3-4 inscripción section (EVID-433) |
| LB-006 | 55_ pp.5-6, Obligaciones numerales 1, 2 y 4: "1. Notificar a la Administración Tributaria por cualquier cambio que ocurra en cuanto a datos que se proporcionaron al momento de la inscripción y afiliación a este régimen." (fn.5: art. 120 CT D-6-91; examples "Cambio de domicilio fiscal - Cambio de domicilio comercial, el cual conlleva la autorización de nuevas facturas.") / "2. Actualizar o ratificar sus datos de inscripción anualmente." / "4. Solicitar autorización para la impresión de las facturas a utilizar, las cuales debe identificar como “Factura de Pequeño Contribuyente” y agregar la frase en forma visible: “No genera derecho a crédito fiscal”." (fn.6: art. 30 AG 5-2013) | Formal obligations: data-change notice (CT art. 120; commercial-domicile change re-triggers factura authorization); ANNUAL ratification of registration data; the pequeño factura must be titled "Factura de Pequeño Contribuyente" and carry the visible legend "No genera derecho a crédito fiscal" (reglamento art. 30, anchored through this secondary print — dated-as-of) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.5-6 numerales 1, 2, 4 + fn.5-6 (EVID-434) |
| LB-007 | 55_ p.6 numeral 5 + fn.7: "5. Emitir y entregar facturas, por todas sus ventas o prestación de servicios mayores de Q50.00 (en el caso que sean menores a este monto, deberá consolidar el total de las mismas en una sola factura que debe emitir al final del día, conservando el original y la copia en su poder)." (fn.7: "Artículo 29 y 49 del Decreto Número 27-92…") | Invoice duty: one factura per operation > Q50.00; operations ≤ Q50.00 consolidate into a single end-of-day factura with original + copy retained by the issuer — the per-operation invoice floor (statutory framing owned by taxation/02) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ p.6 numeral 5 + fn.7 (EVID-435) |
| LB-008 | 55_ p.8 numeral 6 + fn.8: "6. Exigir las facturas correspondientes por la compra o adquisición de bienes y servicios, las cuales debe conservar por el plazo de prescripción. En caso que no exija o conserve estas facturas, incurre en infracción tributaria de carácter formal, la cual es sancionada con una multa de Q 100.00, cien quetzales por cada documento, sanción que no podrá exceder de Q 1,000.00, mil quetzales, de conformidad con lo regulado en el artículo 94 numeral 3) del Código Tributario, Decreto 6-91 del Congreso de la República." | Purchase-side duty: demand facturas for purchases/acquisitions and keep them for the prescription period; failure = formal infraction, Q100.00 per document capped Q1,000.00 (CT art. 94 num. 3 — sanction VALUE owned by taxation/06, cross-ref only) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ p.8 numeral 6 + fn.8 (EVID-436) |
| LB-009 | 55_ pp.8-10 numeral 7-8: "7. Llevar el libro de compras y ventas de Pequeño Contribuyente, habilitado por la Administración Tributaria, el cual se llevará únicamente para efectos tributarios…" / "…puede consolidarlas diariamente en un sólo renglón y podrá llevar esta parte del libro en forma física o electrónica…" / COMPRAS model columns "Día / (1) Número de Documento / (2) Serie / NIT / (3) Proveedor / Nombre / (4) Montos de Compras o Servicios (5)" (sample rows incl. DPI as supplier ID: "1 6 DPI 1010 1011 1012 Karla Aguilar Ruiz 20.00"); VENTAS model "Día / Número Factura de Pequeño Contribuyente / Serie / NIT del Comprador / Comprador / Monto" with row idioms "3 00008 “A” anulada anulada anulada" and "7 00010 “A” C.F. Clientes Varios 85.00" / p.9: "Las facturas emitidas por pequeños contribuyentes, se registrarán en el libro de compras sin consignar ningún valor en la columna correspondiente al impuesto… como lo establece el penúltimo párrafo del artículo 38 del Acuerdo Gubernativo No. 5-2013…" / "…el Libro de Compras y Ventas de Pequeño Contribuyente, antes de su utilización, debe ser previamente habilitado por la Administración Tributaria (artículo 49 del Decreto número 27-92…)" / p.10 numeral 8: "Llevar al día los libros mencionados…, pues de no hacerlo incurre en la infracción establecida en el artículo 94 numeral 4) del Código Tributario." | THE book spec: ONE single combined compras+ventas libro, tax purposes only, SAT-habilitated BEFORE use (LIVA art. 49); ventas consolidable daily into one row; ventas part physical or electronic; columns both sides = día/número/serie/NIT/nombre/monto with NO impuesto column (AG 5-2013 art. 38); row idioms: annulled factura = "anulada" across fields, unidentified customers = "C.F. / Clientes Varios", DPI accepted as natural-person supplier ID; books kept al día or CT art. 94.4 infraction | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.8-10 numeral 7 + models; p.9 reglamento cite; p.10 numeral 8 (EVID-437) |
| LB-010 | 61_ p.3 obligations: "…el contribuyente inscrito en este, para efectos trib utarios [sic], únicamente debe llevar el libro de compras y ventas habilitado por la Administración Tributaria, en el que debe registrar sus ventas y servicios prestados, las primeras de las cuales puede consolidar diaria mente [sic] en un sólo renglón, pudiendo llevarlo en forma manual o computarizada." / "…obligados a emitir siempre facturas en todas sus ventas o prestación de servicios mayores de cincuenta Quetzales (Q.50.00), cuando se trate de ventas o pre stación [sic] de servicios menores del referido valor, podrá consolidar el monto de éstas en una sola, que debe emitir al final del día, debiendo conservar el original y copia en su poder, de conformidad con el artículo 49 de la Ley del Impuesto al Valor Agregado. Asimismo, se encue ntran [sic] obligados a enterar el Impuesto mensualmente, a través del formulario que la Administración Tributaria ponga a disposición de los contribuyentes." | 61_ restates the operative core: the book is the ONLY accounting record for tax purposes ("únicamente debe llevar el libro"), kept manual or computarizado; Q50 floor + daily consolidation identical (citing LIVA art. 49); monthly payment through whatever form SAT provides (= SAT-2046 in this manual, LB-020) | `gt/sources/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf` (via txt) | 61_ p.3 obligations paragraph (EVID-447) |
| LB-011 | 55_ pp.10-11 numeral 9: "9. Requerir a los agentes de retención del IVA las constancias de retención respectivas, así como a los que lleven contabilidad completa y a quien designe SAT para que actúen como agentes de retención del Impuesto al Valor Agregado, cuando les vendan bienes o presten servicios de Pequeños Contribuyentes." | The pequeño's retention-side duty: demand and keep constancias de retención from IVA retention agents (full-accounting buyers and SAT-designated agents) on sales made to them — those constancias feed the declaration credit (LB-012) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.10-11 numeral 9 (EVID-438) |
| LB-012 | 55_ p.11 numeral 10: "10. Presentar la declaración respectiva a través de formulario “IVA-PEQUEÑO CONTRIBUYENTE, denominado, Declaración Jurada Simplificada y Recibo de Pago Mensual, Régimen de Pequeño Contribuyente”, disponible en papel mediante formulario SAT No. 2043 y en medio electrónico mediante formulario SAT No. 2047, en el plazo legalmente establecido, conforme lo regulado en el artículo 48 de la Ley del Impuesto al Valor Agregado, es decir, dentro del mes calendario siguiente al vencimiento de cada período mensual. Declaración que debe presentar independientemente que realice o no actividades afectas." / "De contar con constancias de retención del Impuesto al Valor Agregado, se deberá incluir en la declaración el valor de éstas, mismo que será restado del impuesto determinado y se verá reflejado en el monto a pagar…" | Monthly simplified declaration + payment receipt in one form; window = within the WHOLE calendar month following each monthly period (LIVA art. 48) — no fixed day-of-month or días-hábiles count stated (GOQ-103); mandatory even with zero taxable activity; retention constancias included and SUBTRACTED from the determined tax. Form numbers 2043/2047 = ~2013 prints (drift ledger, FR-093) | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ p.11 numeral 10 (+ p.13 form names) (EVID-439) |
| LB-013 | 55_ pp.13, 15, 16 Gestión de Pago: "Total de Ventas o Servicios del Período Q.3,575.00 — Multiplicado por la tarifa 5% — Impuesto a pagar Q.179.00 — Formulario a presentar 2043 en papel, 2047 electrónico" [sic — 3,575.00 × 5% = 178.75; printed 179.00 = R56 digest arithmetic defect, never copied] / "Al finalizar el llenado del formulario respectivo, se deberá dejar el formulario en estatus “congelado”, generar la boleta SAT-2000, imprimirla y presentarla en una agencia bancaria, para realizar el pago en efectivo sin importar el monto, para lo cual no requiere tener cuenta bancaria." / "El número de referencia de la boleta 2000, podrá utilizarlo para hacer el pago vía BANCASAT." / BANCASAT adhesion ending "…podrá descargar el formulario electrónico número SAT-2049." | Payment rails of the ~2013 era: form left in estatus congelado → boleta SAT-2000 generated and printed → paid in cash at a bank agency (no account needed) or via Bancasat after adhesion; a third pequeño form number SAT-2049 (Bancasat electronic) — all superseded channels recorded as dated historical rows (GOQ-100), and the 5% worked example whose printed result Q.179.00 (exact 178.75) is the R56 defect | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.13, 15, 16 (EVID-441) |
| LB-014 | 55_ pp.17-18 doctrine: "…el de pequeño contribuyente como el régimen en el que este paga con una tarifa del 5% sobre los ingresos brutos en forma mensual, sujeto a retención con carácter de pago definitivo, para los casos que establece la ley." / "El artículo 49 de la Ley del Impuesto al Valor Agregado, en su cuarto párrafo refiere que el valor que soporta la factura de pequeño contribuyente no genera derecho a crédito fiscal para compensación o devolución, para el comprador…, constituyendo dicho valor costo deducible para efectos del Impuesto Sobre la Renta." / "…la tarifa establecida en el artículo 47…, se considera una diferencia sustancial a la tarifa que establece el artículo 10 de la misma ley…" / "…el artículo 18 de la Ley…, que se refiere a la documentación para el reconocimiento del crédito fiscal, no se encuentra la Factura de Pequeño Contribuyente…" | Core doctrine (secondary, dated-as-of ~2013): 5% on monthly gross income, definitive character including via retention (art. 47 vs the general 12% of art. 10); the pequeño factura value gives the buyer NO crédito fiscal (art. 18 excludes it as credit documentation) but is an ISR-deductible cost. The "cuarto párrafo" ordinal here drifts vs "último párrafo" elsewhere — R57: cite by content against consolidated LIVA via taxation/02, never digest ordinals | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.17-18 (EVID-442) |
| LB-015 | 55_ p.12 CONSIDERACIONES IMPORTANTES a)-e) + fn.9-10: "a) No está obligado a llevar Contabilidad completa, toda vez tenga un activo total que no exceda de veinticinco mil quetzales (Q. 25,000.00)." (fn.9: art. 368 Código de Comercio D-2-70) / "b) No tiene obligación de presentar declaración de Impuesto Sobre la Renta." (fn.10: "Artículo 49 del Decreto número 27-92…, último párrafo.") / "c) No debe pagar Impuesto de Solidaridad." / "d) La ley no lo obliga a tener Contador para llevar sus operaciones o hacer sus trámites." / "e) Si derivado de lo establecido en el Código de Comercio, el pequeño contribuyente estuviere obligado a llevar contabilidad completa, deberá efectuar las retenciones del Impuesto Sobre la Renta, en la adquisición de bienes y servicios, en los casos que proceda y enterar dicho impuesto retenido…, conforme lo regulan los artículos 28 y 29 del Código Tributario." (+ sanctions exposure "artículo 94 numerales 7 y 18") | Relief bundle: no full accounting while total assets ≤ Q25,000.00 (CCom art. 368); no ISR declaration (LIVA art. 49 last ¶); no ISO; no mandatory contador; BUT if the Código de Comercio obliges full accounting, the pequeño becomes an ISR retention agent on acquisitions (CT arts. 28-29) with CT 94.7/94.18 sanction exposure — all dated-as-of-~2013 secondary prints (statutory layer GT-TAX-FR-067); ISO line is pre-2024-regime language | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ p.12 a)-e) + fn.9-10 (EVID-440) |
| LB-016 | 55_ pp.19-20 sanction table (CT art. 94 as digested ~2013), rows: "Omisión de dar aviso… de cualquier modificación o actualización de los datos de inscripción…" → "Multa de cincuenta Quetzales (Q.50.00) por cada día de atraso con una sanción máxima de mil quinientos Quetzales (Q.1,500.00)." / "No llevar al día los libros contables u otros registros obligatorios… Se entiende que están al día, si todas las operaciones se encuentran asentadas en los libros y registros debidamente autorizados y habilitados, dentro de los dos (2) meses calendario inmediatos siguientes de realizadas." → "Multa de cinco mil Quetzales (Q.5,000.00), cada vez que se le fiscalice." / 85% voluntary reduction: spontaneous confession + immediate payment rebaja 85% per "artículo 94 'A'" | The sanction spine for pequeño formal duties as the ~2013 digest prints it: late-aviso Q50/day cap Q1,500; books late Q5,000 per fiscalización with the al-día test = entries within 2 following calendar months; 85% voluntary-reduction rule — every VALUE is as-of-2013 and owned by taxation/06 (GT-TAX-FR-214/226) — cross-ref only, never re-derived here | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.19-20 (EVID-443) |
| LB-017 | 55_ NEGATIVE FINDING (entire document, pp.1-20 inventoried): exhaustive string inventory "FEL", "Factura Electrónica", "Documento Tributario Electrónico", "DTE", "Fel", "electrónica" (as invoicing modality) — 0 occurrences; the only "electrónico" usages are "formulario SAT No. 2047", "libro… en forma física o electrónica", "formulario electrónico número SAT-2049"; invoicing uniformly imprenta/paper ("Acreditar a la imprenta de su preferencia para la impresión de facturas") | 55_ contains NO electronic-invoicing content — its world is printed facturas from accredited imprentas; the FEL mandate for pequeños postdates it by ~a decade and must be sourced from 57_/48_ (e-invoicing wave + Task 1), never from 55_; modeling pequeño invoicing from 55_'s paper workflow would be a dated-instrument error | `gt/sources/55_SAT_PequenoContribuyente_guia.pdf` (via txt) | 55_ pp.1-20 full inventory (EVID-444) |
| LB-018 | 61_ p.4: "Libro Electrónico Tributario –LET- / Este libro, constituye una herramienta web que se encuentra dentro de s u [sic] Agencia Virtual, con la cual, los contribuyentes afiliados, podrán llevar el registro de las facturas emitidas y de los documentos de las compras efectuadas, dentro del libro de compras y ventas, facilitándose el cumplimiento de esta obligación tributaria." / "¿Cómo habilitar hojas del Libro de Compras y Ventas computarizadas? / Ingresar a Declaraguate por medio del Portal SAT… / Seleccione el formulario SAT-7121, genere la boleta SAT 2000, puede presentarla en ventanilla bancaria o banca en línea, luego ingrese nuevamente a Declaraguate en la opción buscar formulario ingrese el número de acceso y formulario e imprima la resolución de habilitación de libros" | Habilitación flow for computarizado sheets: formulario SAT-7121 (solicitud) → boleta SAT 2000 paid at bank teller or online banking → back in Declaraguate, print the resolución de habilitación de libros — SAT authorizes (statutory hook LIVA art. 49 per LB-009); LET = the web tool inside Agencia Virtual that records issued facturas + purchase documents AS the libro. NO fee amount is printed anywhere in the flow | `gt/sources/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf` (via txt) | 61_ p.4 LET section + habilitación Q&A (EVID-448) |
| LB-019 | 61_ pp.5-11 step sequence: "1. Ingrese a la Agencia Virtual, con su usuario y contraseña." / "2. Seleccione el menú Servicios /Sistema de Registro del Libro de Compras y Ventas para el Pequeño Contribuyente / Ingreso de Factura" / "Seleccione mes y año a generar, presione el botón “Aceptar” y luego “Ingresar”" / "Si emite FEL, el sistema cargará automáticamente los datos de sus facturas en Ventas." / "Luego de haber registrado todas tus Ventas y Servicios Prestados, cierra las Ventas" / "Luego de haber cerrado las Ventas, si recibiste FEL por Compras, el sistema cargará automáticamente los datos de sus facturas." / "Debe seleccionar las FEL que desee que se registren en la sección Compras y seleccionar el botón “Confirmar”." / "Luego de haber registrado todas sus Compras y Servicios Adquiridos, Cierre las Compras" / "Genere el Resumen de su Libro de Compras y Ventas" / "Indica el número de Folios utilizados hasta el momento en tu Libro de Compras y Ventas" / "En LET cada folio cuenta con 20 líneas para mostrar el detalle de los documentos. El sistema establecerá la cantidad de folios a requerir…, basándose en la cantidad de líneas a imprimir." | LET operational rules: period sessions keyed mes/año; FEL auto-feed on BOTH sides (issued FEL → Ventas automatically; received FEL → Compras by user selection + Confirmar); strict order: register/close Ventas FIRST, then Compras, then Resumen; folio mechanics: 20 document lines per folio, folio count system-derived from lines to print; folios-utilizados captured at resumen; non-FEL facturas typed in via Ingreso de Factura; FEL exists here as integration, no mandate stated | `gt/sources/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf` (via txt) | 61_ pp.5-11 step sequence (EVID-449) |
| LB-020 | 61_ pp.12-19 closing sequence: "Seleccione el botón “Generar Formulario SAT-2046”" / "Cuándo [sic] el impuesto a pagar es “0” Selecciona el botón “Presenta Formulario”" / "Genera un correo automático de constancia de que se ha generado declaración del IVA" / "Confirma la presentación del formulario SAT-2046" / "Ingrese la fecha de su nacimiento y selecciona el botón “Confirmar”" / "El sistema te mostrará un mensaje de confirmación de la presentación del formulario, el cual lleva implícito la marca de caja." / "Selecciona en el calendario, la fecha en la que pagarás el impuesto y selecciona el botón “Confirmar”" / "El sistema generará el número de formulario y número de acceso para pagarlo a través de tu banca virtual, o bien; al seleccionar el botón “Ir a Declaraguate” para buscar el formulario e imprimir la boleta SAT-2000" / "¿Cómo visualizar el libro de compras y ventas? … Seleccione el menú Consultas /Sistema de Registro del Libro de Compras y Ventas para el Pequeño Contribuyente / Reporte Libro de Compras y Ventas / Seleccione el período a generar, luego el botón “Generar Reporte”" / "…el formulario denominado: “IVA-PEQUEÑO CONTRIBUYENTE, Declaración Jurada Simplificada y Recibo de Pago Mensual, Régimen de Pequeño Contribuyente”, disponible en medio electrónico SAT No. 2046" / "La declaración mensual debe presentarse todos los meses, independi entemente [sic] de que realice o no actividades afectas o que le hubiesen retenido la totalidad del impuesto en la fuente durante el período correspondiente." | End-to-end declaration lifecycle (61_ era): the LET resumen generates the SAT-2046 directly (single electronic form; no paper variant mentioned); zero-tax presentation path exists; email constancia of generation; presentation confirmed with a birth-date check; the confirmation message carries the marca de caja; the taxpayer PICKS the payment date from a calendar (no fixed day printed — GOQ-103); payment via banca virtual or boleta SAT-2000; the libro is retrievable as a per-period report; the monthly duty is UNCONDITIONAL — no activity or full source retention does not excuse filing | `gt/sources/61_SAT_LibroComprasVentas_Pequeno_Proc.pdf` (via txt) | 61_ pp.12-19 closing sequence (EVID-450) |
## 3. Functional Requirements

### 3.1 The two-document regime chain (dated layers — GOQ-100/101)

- **GT-FIN-FR-075:** The system shall model `55_` as a DATED LAYER with the
  GOQ-100 banner discipline: an undated SAT digest whose body is provably
  ~2013 (Mayo-2013 worked examples; AG 5-2013 cited in force; pre-FEL
  imprenta/papel channels), still published at the 2024-05-13 Wayback
  capture — capture date ≠ authorship. EVERY quantitative value it prints
  (Q150,000; Q50; Q25,000; Q100/Q1,000; Q5,000; 5%; 85%; forms
  2043/2047/2049; sanction amounts; ISO line; Bancasat rails) is an
  as-of-~2013 dated value that shall never surface as current law without
  re-verification. (LB-001; EVID-431; GOQ-100 → OQ-001; D15/D16)
- **GT-FIN-FR-076:** The system shall model `61_` as the LET-era dated
  layer with a provenance row (GOQ-101): "PROCEDIMIENTO DE AUTORIZACIÓN,
  OPERACIÓN Y USO DEL LIBRO DE COMPRAS Y VENTAS DEL PEQUEÑO CONTRIBUYENTE",
  no printed date; the task's "v3" label is NOT printed; content floor ≈
  2018-11-07 inferred from the URL anchor epoch (an inference, never a
  printed date); LET/Agencia Virtual/FEL auto-load/SAT-2046 era — verify
  the live SAT page before citing any 61_ mechanic as the current
  procedure. (LB-002; EVID-445; GOQ-101 → OQ-002; D15/D16)
- **GT-FIN-FR-077:** NEGATIVE FR (R56-adjacent provenance guard): `55_`
  contains ZERO FEL content (exhaustive string inventory) — the system
  shall never model pequeño invoicing, payment or channel mechanics from
  55_'s imprenta/papel/congelado/Bancasat workflow as current state; the
  FEL mandate for pequeños (57_/48_ lineage) is sourced from the
  e-invoicing wave and Task 1 — cross-referenced, never from this corpus
  pair. (LB-017; EVID-444)
- **GT-FIN-FR-078:** The regime chain model shall record both affiliation
  variants — **Régimen de Pequeño Contribuyente** and **Régimen
  Electrónico de Pequeño Contribuyente** — under the single Q150,000.00
  eligibility, consuming every statutory value from taxation/02 by exact
  id: threshold + R20 provenance (GT-TAX-FR-046), entry/switch (FR-047),
  2012 cutover + de-oficio migration rows (FR-049, whose 55_ fn.1 print =
  LB-003). R20 (binding): the threshold = D-27-92 arts. 45/46/50 as
  reformed by D-4-2012 arts. 12/13/18 — never cite the LAT for pequeño
  thresholds (GT-TAX-FR-068 guard consumed). (LB-003; LB-004; EVID-432,
  EVID-446; R20; cross-ref GT-TAX-FR-046, GT-TAX-FR-047, GT-TAX-FR-049,
  GT-TAX-FR-068)
- **GT-FIN-FR-079:** The onboarding surface shall implement the RTU
  opt-in mechanics as printed: manifestation at any SAT office; a
  Régimen General taxpayer within the threshold may request the switch
  **at any date**; SAT performs the inscription, delivers the **hoja de
  obligaciones** and fixes the starting monthly period — the regime start
  is SAT-determined, never petition-determined (operational print of
  GT-TAX-FR-047). (LB-005; EVID-433; cross-ref GT-TAX-FR-047)
- **GT-FIN-FR-080:** The lifecycle surface shall consume the exit rule
  from GT-TAX-FR-048 by exact id (LIVA art. 50): prior-calendar-year
  gross > Q150,000.00 → solicitud to Régimen General, failing which SAT
  inscribes de oficio with notice + new start period. `61_` (LB-004) is
  the ONLY print of the rule in this corpus pair — `55_` carries opt-in
  mechanics but NO exit rule (documented asymmetry; model the lifecycle
  from 61_ + art. 50, never from 55_). (LB-004; EVID-446; cross-ref
  GT-TAX-FR-048)

### 3.2 Obligation set & printed invoice surfaces

- **GT-FIN-FR-081:** The obligation set shall include the registry-duty
  pair as printed: (i) data-change notice to SAT for any change to
  inscription/afiliación data (CT art. 120; a commercial-domicile change
  additionally re-triggers factura authorization), consuming the
  statutory 30-day clock from GT-TAX-FR-200; (ii) ANNUAL
  actualizar/ratificar of registration data, consuming GT-TAX-FR-201 —
  this FR owns only the pequeño-surface wiring; late-notice sanction
  exposure (Q50/day cap Q1,500 as-of-2013, LB-016) is taxation/06 data
  (GT-TAX-FR-214), cross-ref only. (LB-006; LB-016; EVID-434, EVID-443;
  cross-ref GT-TAX-FR-200, GT-TAX-FR-201, GT-TAX-FR-214)
- **GT-FIN-FR-082:** THIS FILE owns the printed-surface requirement: the
  pequeño factura shall be issued titled **"Factura de Pequeño
  Contribuyente"** carrying the visible legend **"No genera derecho a
  crédito fiscal"** — the statutory layer (reglamento AG 5-2013 art. 30,
  anchored through the 55_ secondary print, dated-as-of) is consumed from
  GT-TAX-FR-063 by exact id; FEL document-type mapping (FPEQ/FCAP) is the
  e-invoicing wave's — cross-ref only. (LB-006; EVID-434; cross-ref
  GT-TAX-FR-063)
- **GT-FIN-FR-083:** The invoicing surface shall enforce the Q50
  per-operation floor mechanics as printed: one factura per operation
  > Q50.00; operations ≤ Q50.00 consolidated into a **single end-of-day
  factura** with original + copy retained by the issuer — statutory
  framings (Ley art. 49 mandate + reglamento art. 55.1 on-request path +
  "Clientes Varios"/NIT "CF" idiom) consumed from GT-TAX-FR-061/062 by
  exact id; 61_'s identical print (LB-010) cites art. 49 and adds that
  the consolidated daily factura feeds the libro's daily one-row
  consolidation (FR-088). (LB-007; LB-010; EVID-435, EVID-447; cross-ref
  GT-TAX-FR-061, GT-TAX-FR-062)
- **GT-FIN-FR-084:** The purchase-side duty shall be recorded: demand
  facturas for every purchase/acquisition of goods and services and keep
  them for the prescription period; non-demand/non-retention = formal
  infraction under **CT art. 94 numeral 3** — the sanction VALUES
  (Q100.00 per document, cap Q1,000.00) are consumed from GT-TAX-FR-214
  (taxation/06 dated rows), NEVER re-derived from the 55_ print.
  (LB-008; EVID-436; cross-ref GT-TAX-FR-214)
- **GT-FIN-FR-085:** The retention-side duty surface shall record: the
  pequeño must REQUIRE the *constancias de retención* (retention
  certificates) from IVA retention agents, full-accounting buyers and
  SAT-designated agents when selling to them — collected constancias feed
  the declaration credit (FR-096); the agent-side universe/rate/floor
  (5% ≥ Q2,500.01 exclusive, GT-TAX-FR-054/055/057) and the RetWeb
  operational surfaces (GT-FIN-FR-034/039/069) are cross-referenced,
  never duplicated. (LB-011; EVID-438; cross-ref GT-TAX-FR-054,
  GT-TAX-FR-055, GT-TAX-FR-057, GT-FIN-FR-034, GT-FIN-FR-039,
  GT-FIN-FR-069)

### 3.3 The compras-y-ventas libro (single combined book)

- **GT-FIN-FR-086:** The libro model shall implement: **ONE single
  combined compras-y-ventas book**, kept "únicamente para efectos
  tributarios" (the ONLY accounting record for tax purposes per 61_),
  **habilitado by SAT BEFORE use** (statutory hook LIVA art. 49 =
  GT-TAX-FR-066 by exact id), kept **manual o computarizado** (61_) /
  ventas part "física o electrónica" (55_) — the statutory hook is
  taxation-owned; this FR owns the operational bookkeeping surface
  (odoo bookkeeping + folio management + daily consolidation).
  (LB-009; LB-010; EVID-437, EVID-447; cross-ref GT-TAX-FR-066)
- **GT-FIN-FR-087:** The libro column spec shall implement the printed
  models for BOTH sections — Día / Número de Documento (compras) or
  Número Factura de Pequeño Contribuyente (ventas) / Serie / NIT / Nombre
  (Proveedor or Comprador) / Monto, with per-section totals — and **NO
  impuesto column**: pequeño facturas carry no IVA ("sin consignar
  ningún valor en la columna correspondiente al impuesto", AG 5-2013
  art. 38 penúltimo párrafo per the 55_ print); buyer-side no-IVA-column
  registration is statutory (GT-TAX-FR-026/FR-041 via GT-TAX-FR-064) —
  cross-ref only. (LB-009; EVID-437; cross-ref GT-TAX-FR-064,
  GT-TAX-FR-026, GT-TAX-FR-041)
- **GT-FIN-FR-088:** The libro row engine shall implement the printed
  row idioms and consolidation rule: annulled facturas recorded as
  **"anulada"** across the counterparty fields; unidentified customers
  recorded as **"C.F." / "Clientes Varios"** (the daily-consolidated
  factura idiom, FR-083); **DPI accepted as supplier ID** for natural
  persons; and the **daily one-row consolidation of ventas** (statutory
  GT-TAX-FR-066 / reglamento art. 55.4, consumed). (LB-009; EVID-437;
  cross-ref GT-TAX-FR-066)
- **GT-FIN-FR-089:** The habilitación surface shall record the printed
  flow for computarizado sheets: **formulario SAT-7121** (solicitud in
  Declaraguate) → **boleta SAT 2000** paid at ventanilla bancaria or
  banca en línea → re-enter Declaraguate → **print the resolución de
  habilitación de libros** — SAT is the authorizing party (LIVA art. 49
  hook). NO fee amount is printed anywhere in the flow (the evidence
  file records that the task's "Q50 planilla fee" appears in NEITHER
  document — never asserted). The C2 dual-track habilitación model
  (SAT-7121 RM authorization vs electronic books) is owned by the future
  S-GT5 COA wave — cross-ref POINTER only, never modeled here.
  (LB-018; EVID-448; S-GT5 cross-ref pointer)
- **GT-FIN-FR-090:** The LET identity row shall record: **LET = Libro
  Electrónico Tributario, a web tool inside Agencia Virtual** with which
  affiliated taxpayers record issued facturas and purchase documents
  within the libro de compras y ventas — the SAME statutory book
  obligation in a later era. The F4-era LET mechanics (57_ manual:
  immutability, reports, folio bridge) are owned by Task 4
  (`04_let-electronic-books.md`) — cross-referenced by file, never
  duplicated; this FR records the 61_ definition only. (LB-018;
  EVID-448; Task 4 cross-ref)
- **GT-FIN-FR-091:** The LET session model shall implement the 61_
  operational discipline as the earlier-era print: sessions keyed per
  **mes y año** (menu Servicios → Sistema de Registro del Libro de
  Compras y Ventas para el Pequeño Contribuyente → Ingreso de Factura);
  **FEL auto-load on both sides** (issued FEL → Ventas automatically;
  received FEL → Compras auto-surfaced for user **selection +
  Confirmar**); non-FEL facturas typed in; strict cierre order —
  register/close **Ventas FIRST, then Compras**, then generate the
  **Resumen** with the folios-utilizados capture; **folio = 20 document
  lines**, folio count system-derived from the lines to print. Task 4
  owns the F4 pairing (57_) of these mechanics. (LB-019; EVID-449;
  Task 4 cross-ref)
- **GT-FIN-FR-092:** The books-currency surface shall record the al-día
  discipline as printed: all operations entered within **2 calendar
  months** of realization (CT art. 94.4 definition, LB-009/LB-016),
  failing which the books-late infraction applies — sanction VALUES
  (Q5,000 per fiscalización, as-of-2013 print) consumed from
  GT-TAX-FR-214/231, and the 85% voluntary-reduction rule (art. 94 "A")
  from GT-TAX-FR-226 — ALL cross-ref only, never re-derived here.
  (LB-009; LB-016; EVID-437, EVID-443; cross-ref GT-TAX-FR-214,
  GT-TAX-FR-226, GT-TAX-FR-231)

### 3.4 Declaration lifecycle (form-drift ledger + window + generation)

- **GT-FIN-FR-093:** The form-number drift shall be stored as DATED ROWS
  keyed by era (D16/D-GT10; never silently merged): **55_ era (~2013)**:
  SAT-2043 (papel) / SAT-2047 (electrónico) / SAT-2049 (Bancasat
  electronic download) → **61_ era (≥ ~2018-11)**: SAT-2046
  (LET-generated electronic) → **current generation (48_ registry)**:
  SAT-2046 (normal variant, valid ≥ 2013-09) + SAT-2241 (Régimen
  Electrónico variant). The registry identities and predecessor-chain
  selection are owned by Task 1 (GT-FIN-FR-006/014/015 — the terminus);
  this file owns the drift LEDGER; 55_ numbers shall never surface as
  current. (LB-012; LB-013; LB-020; EVID-439, EVID-441, EVID-450;
  cross-ref GT-FIN-FR-006, GT-FIN-FR-014, GT-FIN-FR-015; D15/D16)
- **GT-FIN-FR-094:** The declaration surface shall generate the form
  titled **"IVA-PEQUEÑO CONTRIBUYENTE, Declaración Jurada Simplificada y
  Recibo de Pago Mensual, Régimen de Pequeño Contribuyente"** with the
  window consumed from GT-TAX-FR-059 by exact id: **the whole calendar
  month following each monthly period** (LIVA art. 48). GOQ-103 (owned
  here): NEITHER 55_ nor 61_ prints a fixed day-of-month or días-hábiles
  count — only "dentro del mes calendario siguiente" + the
  taxpayer-selected payment date; the per-NIT-digit vencimiento calendar
  is EXTERNAL, consumed via Task 1's ingestion surface (GT-FIN-FR-024;
  GOQ-14 kin). (LB-012; LB-020; EVID-439, EVID-450; GOQ-103 → OQ-004;
  cross-ref GT-TAX-FR-059, GT-FIN-FR-024)
- **GT-FIN-FR-095:** The filing duty shall be UNCONDITIONAL: the monthly
  declaration is due **todos los meses** regardless of taxable activity
  OR full source retention ("independientemente que realice o no
  actividades afectas o que le hubiesen retenido la totalidad del
  impuesto en la fuente") — identical in both prints; consumed jointly
  with GT-TAX-FR-059's mandatory-at-zero row. (LB-012; LB-020; EVID-439,
  EVID-450; cross-ref GT-TAX-FR-059)
- **GT-FIN-FR-096:** The declaration content assembly shall carry: the
  month's gross operation sum (daily-consolidated rows included), the
  5% determination and the **constancia-backed retención credit
  subtracted** ("se deberá incluir en la declaración el valor de éstas,
  mismo que será restado del impuesto determinado"), payable floored at
  zero — computation consumed from GT-TAX-FR-051/052 by exact id. R56
  FIDELITY GUARD: the 55_ worked example prints "Q.179.00" for
  Q3,575.00 × 5% (exact **178.75**) — a digest arithmetic defect [sic]
  that shall NEVER be copied; SAT's official 5%-rounding rule is unknown
  (GOQ-102) and plain decimal arithmetic applies per GT-TAX-FR-053
  (consumed). (LB-012; LB-013; LB-014; EVID-439, EVID-441, EVID-442;
  R56; GOQ-102 → OQ-003; cross-ref GT-TAX-FR-051, GT-TAX-FR-052,
  GT-TAX-FR-053)
- **GT-FIN-FR-097:** The LET-to-declaration surface shall implement the
  61_ generation sequence: the libro resumen feeds **"Generar
  Formulario SAT-2046"**; when the determined tax is "0" the
  **"Presenta Formulario"** zero-tax path applies; SAT sends an
  automatic email constancia of the generated declaration;
  presentation is confirmed with a **birth-date check** ("Ingrese la
  fecha de su nacimiento… Confirmar"); the confirmation message carries
  the **marca de caja** implicitly. (LB-020; EVID-450)
- **GT-FIN-FR-098:** The payment surface shall implement: the taxpayer
  **selects the payment date from SAT's calendar** (within the legal
  window — no fixed day printed, GOQ-103); the system generates the
  número de formulario + número de acceso for **banca virtual** payment
  or the "Ir a Declaraguate" path to print the **boleta SAT-2000**. The
  55_-era rails — estado **congelado** → boleta SAT-2000 → cash at a
  bank agency (no account required) or **Bancasat** after adhesion,
  with the **SAT-2049** electronic download — shall be recorded as
  DATED HISTORICAL channel rows (as-of-~2013, GOQ-100), never routed as
  current. (LB-013; LB-020; EVID-441, EVID-450; GOQ-100 → OQ-001;
  D15/D16)
- **GT-FIN-FR-099:** The libro retrieval surface shall implement the
  per-period report: Consultas → Sistema de Registro del Libro de
  Compras y Ventas para el Pequeño Contribuyente → **Reporte Libro de
  Compras y Ventas** → select período → Generar Reporte → download
  and/or print. (LB-020; EVID-450)

### 3.5 Relief bundle prints & doctrine guards

- **GT-FIN-FR-100:** The relief surface shall consume the statutory ISR
  relief from GT-TAX-FR-067 by exact id (LIVA art. 49 final ¶:
  pequeños relieved of payment AND presentation of any ISR declaration —
  annual, quarterly or monthly — and of any tax creditable to ISR),
  recording the 61_ print ("relevados del pago y la presentación") as
  its operational echo. R57 GUARD: LIVA art. 49 paragraph ordinals
  DRIFT inside 55_ itself ("cuarto párrafo" p.17 vs "último párrafo"
  p.12 fn.10) — this file shall cite art. 49 BY CONTENT against the
  consolidated LIVA via taxation/02 and never reproduce a digest
  paragraph ordinal. (LB-004; LB-015; EVID-446, EVID-440; R57;
  cross-ref GT-TAX-FR-067)
- **GT-FIN-FR-101:** The ~2013 secondary relief details shall be seeded
  as DATED-AS-OF rows (GOQ-100), consuming GT-TAX-FR-067's layering: no
  full accounting while total **activo ≤ Q25,000.00** (CCom art. 368);
  **no ISO** (pre-2024-regime language flag — the ISO line is vintage
  evidence, never a current relief claim); no mandatory contador; AND
  the conditional duty — if the Código de Comercio nonetheless obliges
  full accounting, the pequeño acts as **ISR retention agent** on
  acquisitions (CT arts. 28-29) with CT 94.7/94.18 sanction exposure
  (VALUES = GT-TAX-FR-214 cross-ref only). (LB-015; EVID-440; GOQ-100 →
  OQ-001; cross-ref GT-TAX-FR-067, GT-TAX-FR-214)
- **GT-FIN-FR-102:** The doctrine echo row shall record the 55_
  secondary doctrine (dated-as-of, statutory layer consumed by exact
  id): the pequeño pays **5% on gross monthly income with definitive
  character including via retention** (art. 47, contrasted with the
  general 12% of art. 10 — GT-TAX-FR-051); the factura value gives the
  buyer **no crédito fiscal** and is an **ISR-deductible cost** (art. 18
  excludes the pequeño factura as credit documentation — GT-TAX-FR-064);
  cited by content under the R57 ordinal guard. (LB-014; EVID-442; R57;
  cross-ref GT-TAX-FR-051, GT-TAX-FR-064)
## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + provenance
+ as-of qualifier; snapshot-on-write. This file stores NO statutory
constants — thresholds, rates, floors, windows, sanction amounts are
taxation-owned (taxation/02 + /06) and consumed by FR id; what is stored
here is the two-document chain ledger, the libro/LET operational surfaces,
the form-drift ledger and the print-provenance rows.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.pequeno.docchain | layer / identity_es / vintage / as_of / anchor | selection 55_-61_ / char / char / char / char | 55_ = ~2013 body, live at capture 2024-05-13 (GOQ-100); 61_ = ≥ ~2018-11 URL-epoch floor, "v3" unprinted (GOQ-101); both = "Departamento de Consultas / Consultas Tributarias" orientation digests | FR-075, FR-076 |
| l10n_gt.pequeno.regime.print | variants / threshold_ref / exit_print | selection normal-electronico / char (GT-TAX-FR-046) / char | both variants under one Q150,000 test; exit rule printed only in 61_ (55_ asymmetry recorded) | FR-078, FR-080 |
| l10n_gt.pequeno.onboarding | gesture / switch_any_date / hoja_obligaciones / start_period_source | char / boolean / boolean / selection=sat | manifestation at any SAT office; SAT-issued hoja + start period | FR-079 |
| l10n_gt.pequeno.invoice.surface | title / legend / per_op_floor / daily_consolidation / keep_original_copy | char / char / char (→GT-TAX-FR-061) / boolean / boolean | "Factura de Pequeño Contribuyente"; "No genera derecho a crédito fiscal" (GT-TAX-FR-063); Q50.00 floor; end-of-day consolidated factura; original+copy retained | FR-082, FR-083 |
| l10n_gt.pequeno.purchase.duty | demand / retain_period / sanction_ref | boolean / char=prescription / char (GT-TAX-FR-214) | CT 94-3 exposure Q100/doc cap Q1,000 — values cross-ref only | FR-084 |
| l10n_gt.pequeno.constancia.demand | agents / feeds | char (IVA agents + full accounting + SAT-designated) / char=FR-096 | collected constancias = declaration credit input | FR-085 |
| l10n_gt.pequeno.libro | count / scope / habilitacion_previa / media / statutory_ref | integer=1 / char=tax-purposes-only / boolean / selection manual-computarizado-fisica-electronica / char (GT-TAX-FR-066) | single combined compras-y-ventas book, SAT-habilitated before use | FR-086 |
| l10n_gt.pequeno.libro.column | side / columns / tax_column | selection compras-ventas / char list día,número,serie,nit,nombre,monto / boolean=false | NO impuesto column (AG 5-2013 art. 38 via 55_ print) | FR-087 |
| l10n_gt.pequeno.libro.row | idiom / value | selection anulada-cf_varios-dpi-normal / char | "anulada" across fields; "C.F."/"Clientes Varios"; DPI as natural-person supplier ID; daily one-row ventas consolidation | FR-088 |
| l10n_gt.pequeno.habilitacion | form / boleta / output / fee_printed / sgt5_pointer | char=SAT-7121 / char=SAT 2000 / char=resolución de habilitación de libros / boolean=false / char | Declaraguate flow; no fee amount printed; S-GT5 C2 owns the dual-track model | FR-089 |
| l10n_gt.pequeno.let | definition / home / session_key / fel_autoload / cierre_order / folio_lines / folio_count | char / char=Agencia Virtual / char=mes y año / selection ventas-auto-compras-select+confirmar / char=ventas→compras→resumen / integer=20 / char=system-derived | 61_-era operational layer; Task 4 owns the 57_ pairing | FR-090, FR-091 |
| l10n_gt.pequeno.form.drift | era / forms / valid_from / provenance | selection 55_~2013 / 61_≥2018-11 / current-48_ / char list / char / char | 2043+2047+2049 → 2046 → 2046+2241; T1 registry = terminus; never silently merged | FR-093 |
| l10n_gt.pequeno.declaration | title_es / window_ref / unconditional / zero_tax_path / marca_caja / birth_date_confirm | char / char (GT-TAX-FR-059) / boolean / boolean / boolean / boolean | "IVA-PEQUEÑO CONTRIBUYENTE, Declaración Jurada Simplificada y Recibo de Pago Mensual…"; whole-month window; monthly at zero; "Presenta Formulario" path | FR-094, FR-095, FR-097 |
| l10n_gt.pequeno.declaration.content | gross_sum / rate_ref / retention_credit / rounding | decimal / char (GT-TAX-FR-051/052) / boolean / char=plain-decimal (GT-TAX-FR-053) | R56: never reproduce Q.179.00; GOQ-102 open | FR-096 |
| l10n_gt.pequeno.payment | date_selection / rails_current / rails_historical | selection=calendar-within-window / char list banca_virtual-boleta_2000 / char list congelado-bancasat-2049 (as-of-~2013) | payment date taxpayer-selected; historical rails never routed | FR-098 |
| l10n_gt.pequeno.libro.report | menu / period / output | char / char=período / selection download-print | Reporte Libro de Compras y Ventas | FR-099 |
| l10n_gt.pequeno.relief.print | isr_declaration / iso / contador / activo_cap / conditional_isr_agent / as_of | boolean=false (GT-TAX-FR-067) / boolean=false (vintage flag) / boolean=false / decimal=Q25,000.00 (CCom 368, dated) / boolean / char=~2013 | secondary prints layered over the statutory relief | FR-100, FR-101 |
| l10n_gt.pequeno.guard | key | char | 55_never_current (GOQ-100); v3_unprinted (GOQ-101); no_fel_from_55_ (EVID-444); r56_no_q179 (R56); r57_no_digest_ordinals (R57); goq103_no_fixed_day; sanctions_crossref_only; habilitacion_fee_unprinted | FR-075..FR-077, FR-096, FR-100, FR-102 |
## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = XML
emission, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Wave defaults
for this file (binding): libro bookkeeping + folio management + daily
consolidation = `odoo`; SAT-2046 generation data assembly = `odoo` with
`saas` transmission; regime-chain dated layers + form-drift ledger =
`shared`. Model names stable across Odoo 17/18/19/20; no version-specific
behavior required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-075 | shared | — (config data §4) | docchain 55_ layer row | GOQ-100 banner: as-of-~2013 qualifier on every 55_-sourced value; capture 2024-05-13 ≠ authorship |
| FR-076 | shared | — (config data §4) | docchain 61_ layer row | GOQ-101: ≥ ~2018-11 inferred floor; "v3" unprinted; live-page verification pending |
| FR-077 | shared | — (guard) | no_fel_from_55_ | 55_ = imprenta era; FEL mandate sourced from e-invoicing wave + T1 |
| FR-078 | shared | — (config data §4) | regime.print rows | Values consumed GT-TAX-FR-046/047/049/068 (R20); both variants recorded |
| FR-079 | odoo | res.partner (regime onboarding) | manifestation + hoja_obligaciones + SAT start period | SAT-set start period recorded, never inferred; GT-TAX-FR-047 consumption |
| FR-080 | odoo | res.partner (regime lifecycle surface) | exit-warning display | Evaluation = GT-TAX-FR-048 (saas monitoring); this surface displays + records 61_-only print |
| FR-081 | odoo | res.partner (pequeño duties surface) | change-notice + annual-ratification scheduling | Clocks GT-TAX-FR-200/201; sanctions GT-TAX-FR-214 cross-ref |
| FR-082 | odoo | account.journal / account.move (document layout) | title + visible legend | Printed-surface owner; statutory GT-TAX-FR-063; FPEQ/FCAP = e-invoicing wave |
| FR-083 | odoo | account.move (invoice emission + consolidation job) | Q50 floor routing + end-of-day consolidated factura | GT-TAX-FR-061/062 consumed; original+copy retention flag |
| FR-084 | odoo | account.move.line (supplier docs) / retention policy | demand + retain flags | CT 94-3 values GT-TAX-FR-214 — never local |
| FR-085 | odoo | account.move (constancia input records) | constancia de retención link | Feeds FR-096 credit; agent side GT-TAX-FR-054/055/057 + T2 GT-FIN-FR-039/069 |
| FR-086 | odoo | books surface (pequeño libro) | single combined book flag + habilitación state | Statutory hook GT-TAX-FR-066; manual o computarizado media row |
| FR-087 | odoo | libro line model | column set, no tax column | AG 5-2013 art. 38 via 55_ print; buyer-side statutory GT-TAX-FR-026/041/064 |
| FR-088 | odoo | libro line model (idioms + consolidation) | anulada / C.F.-Clientes Varios / DPI id / daily one-row | Folio management odoo-side; GT-TAX-FR-066 consumed |
| FR-089 | shared | — (provenance row + capture surface) | SAT-7121 + boleta SAT 2000 → resolución flow | No fee printed; S-GT5 C2 dual-track = pointer only |
| FR-090 | shared | — (config data §4) | LET identity row | Task 4 owns F4 LET mechanics; 61_ definition recorded |
| FR-091 | odoo | libro session model (LET pairing surface) | mes/año sessions; FEL auto-load pairing; cierre order; 20-line folios | Task 4 cross-ref for the 57_-era mechanics |
| FR-092 | odoo | books surface (al-día monitor) | 2-calendar-month entry lag | Sanction values GT-TAX-FR-214/226/231 cross-ref only |
| FR-093 | shared | — (config data §4) | form.drift dated rows | 2043/2047/2049 → 2046 → 2046/2241; T1 registry terminus (GT-FIN-FR-006/014/015) |
| FR-094 | odoo | account.move (declaration skeleton; SAT-2046 data assembly) | window + form selection | Generation assembly odoo with saas transmission; window GT-TAX-FR-059; calendar GT-FIN-FR-024 (GOQ-14 kin) |
| FR-095 | odoo | account.move (filing duty engine surface) | unconditional-monthly flag | Both prints; GT-TAX-FR-059 joint consumption |
| FR-096 | odoo | account.move (declaration content) | gross sum + 5% + retention credit − payable | GT-TAX-FR-051/052/053 consumed; R56 guard — Q.179.00 never reproduced; GOQ-102 |
| FR-097 | odoo | declaration generation flow + saas transmission | SAT-2046 generate / zero-tax path / birth-date confirm / marca de caja | 61_ sequence; email constancia surface |
| FR-098 | odoo | payment surface (declaration) | calendar date selection + boleta/banca virtual rails | Historical congelado/Bancasat/2049 rows = dated, never routed (GOQ-100) |
| FR-099 | odoo | libro report action | per-period Reporte Libro de Compras y Ventas | Download/print |
| FR-100 | shared | — (consumption row) | ISR relief echo | GT-TAX-FR-067 exact; R57 ordinal guard enforced on citation surface |
| FR-101 | shared | — (config data §4) | relief.print dated-as-of rows | Q25,000 activo / no-ISO vintage flag / conditional ISR-agent; GT-TAX-FR-067/214 cross-refs |
| FR-102 | shared | — (doctrine echo row) | 5%-gross-definitive + no-crédito-fiscal doctrine | GT-TAX-FR-051/064 consumed; R57 guard |
## 6. Acceptance Criteria

- **AC-001:** Given the docchain ledger, when any 55_-sourced value is
  surfaced, then it carries its as-of-~2013 qualifier and none of
  {2043, 2047, 2049, congelado, Bancasat, ISO relief} is presented as
  current (GOQ-100); the 61_ layer carries the ≥ ~2018-11 inferred floor
  with "v3" marked unprinted (GOQ-101). (FR-075, FR-076, FR-093, FR-098)
- **AC-002:** Given the regime configuration, then two affiliation
  variants exist under the single Q150,000 threshold whose provenance
  reads "D-27-92 arts. 45/46/50, reformados por D-4-2012 arts. 12/13/18"
  (R20) resolved from GT-TAX-FR-046 — no surface cites the LAT for
  pequeño thresholds — and the exit rule resolves from GT-TAX-FR-048
  with the 55_-has-no-exit-rule asymmetry recorded. (FR-078, FR-080)
- **AC-003:** Given a pequeño onboarding, then the start period is
  recorded as SAT-determined with the hoja de obligaciones issued, and a
  General-regime switch request is accepted with any effective date.
  (FR-079)
- **AC-004:** Given a pequeño invoice emission, then the document is
  titled "Factura de Pequeño Contribuyente" with the visible legend "No
  genera derecho a crédito fiscal" (GT-TAX-FR-063 consumed); given
  sub-Q50.00 sales across a day, then exactly one end-of-day
  consolidated factura is issued and its libro row is the daily single
  row. (FR-082, FR-083, FR-088)
- **AC-005:** Given the libro, then it is ONE combined book with columns
  Día/Número/Serie/NIT/Nombre/Monto and NO impuesto column; annulled
  facturas render "anulada" across counterparty fields; unidentified
  customers render "C.F."/"Clientes Varios"; DPI is accepted as a
  natural-person supplier identifier; and the habilitación state records
  the SAT-7121 + boleta SAT 2000 → resolución flow with NO fee amount
  asserted. (FR-086..FR-089)
- **AC-006:** Given a LET session for a month, then ventas register and
  close before compras; issued FEL auto-load into Ventas while received
  FEL enter Compras only by selection + Confirmar; the resumen captures
  folios utilized; and folio pagination derives from the 20-lines-per-
  folio rule. (FR-091)
- **AC-007:** Given the form-drift ledger, then the three eras resolve
  as distinct dated rows (2043/2047/2049 ~2013; 2046 ≥ 2018-11;
  2046/2241 current per T1) and a period-keyed read selects the correct
  generation via GT-FIN-FR-015 — never a silent merge. (FR-093)
- **AC-008:** Given a declaration month, then the window is the entire
  following calendar month with no fixed day or días-hábiles count
  invented (GOQ-103; calendar external via GT-FIN-FR-024), the duty
  stands at zero activity and at full source retention, and
  constancia-backed retentions are subtracted from the 5% determination
  floored at zero. (FR-094, FR-095, FR-096)
- **AC-009:** Given gross invoiced Q3,575.00 with no constancias, then
  the payable computes Q178.75 — the 55_ print "Q.179.00" (R56) is
  recorded as a defect and never reproduced; rounding stays plain
  decimal until GOQ-102 resolves. (FR-096)
- **AC-010:** Given a LET-closed month, then the SAT-2046 generation
  flow executes (zero-tax "Presenta Formulario" path when tax = 0),
  presentation is confirmed by birth-date check and the confirmation
  message carries the marca de caja; the payment date is chosen from
  the calendar within the window and the boleta SAT-2000 / banca
  virtual rails generate. (FR-097, FR-098)
- **AC-011:** Given the relief configuration, then ISR declarations are
  suppressed per GT-TAX-FR-067 (art. 49 final ¶) while the Q25,000
  activo cap, no-ISO and no-contador rows carry dated-as-of-~2013
  flags, and the conditional ISR-retention-agent duty fires only when
  full accounting is CCom-obliged — with sanction values resolved from
  taxation/06, never from this file. (FR-100, FR-101)
- **AC-012:** Given any art. 49 citation produced by these surfaces,
  then it cites by content against the consolidated LIVA via
  taxation/02 and contains no digest paragraph ordinal ("cuarto
  párrafo"/"último párrafo") — grep-able R57 guard. (FR-100, FR-102)
## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C.4);
question text verbatim from the register (abbreviated where noted). This
file OWNS GOQ-100/101/102/103 (F3 rows) and cites kin GOQ-06 (register
lists TX3, F2 rate catalog) and GOQ-14 (register lists F-cluster deadline
CRs). The S-GT2 taxation/02 §7 rows citing GOQ-102/103 as kin (statutory
half answered there) are consumed, never re-opened. Nothing outside this
register is treated as an open question; new gaps are flagged to the
controller as non-OQ notes (no invented ids).

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-100 (owned): "55_ = undated ~2013 body still live at 2024 capture: EVERY value (Q150,000; Q50; Q25,000; Q100/Q1,000; Q5,000; 5%; 85%; forms 2043/2047/2049; sanction amounts; ISO line; Bancasat rails) = as-of-2013 dated value." Affects FR-075 (banner), FR-093/FR-098 (historical form/channel rows), FR-101 (relief prints) and every 55_-sourced LB row: values re-verified against current instruments before any current-law use; sanction amounts especially (CT reformed since — taxation/06 owns the current table). | no | GT synthesis wave S-GT4 → acquisition queue (current instruments; sanction consolidation rides taxation/06) | open |
| OQ-002 | GOQ-101 (owned): "61_ provenance: 'v3' label unprinted, no date (URL epoch ≈2018-11; FEL/LET/SAT-2046 era) — verify live page before citing as current procedure." Affects FR-076 and every 61_-sourced mechanics row (FR-090/091/097/098/099): the LET flow may have evolved (Task 4's 57_ manual is the later-era pairing); live-page verification pending. | no | GT synthesis wave S-GT4 → acquisition queue (live SAT page) | open |
| OQ-003 | GOQ-102 (owned; register residue of EV04c OQ-7): "SAT official 5%-rounding rule unknown (55_ worked example prints Q.179.00 for 178.75 [sic]) — do not copy; verify rule." S-GT2 kin row (taxation/02 OQ-003) already ships the computation guard (GT-TAX-FR-053: plain decimal arithmetic, divergence recorded); this file consumes that guard on the declaration surface (FR-096) and owns the register row until the SAT rule is verified. | no | GT synthesis wave S-GT4 → W6 partner ask (SAT rule verification; shared with S-GT2) | open |
| OQ-004 | GOQ-103 (owned): "Pequeño deadline shape: neither 55_ nor 61_ prints a fixed day/hábiles count — only LIVA art. 48 'mes calendario siguiente' + taxpayer-selected payment date; a per-NIT-digit calendar source is external (GOQ-14)." Statutory half ANSWERED in taxation/02 (GT-TAX-FR-059: whole-month window, mandatory-at-zero); this file owns the mechanics half (FR-094/FR-098: no deadline object beyond the whole-month window; payment date = taxpayer-selected from SAT's calendar; per-NIT-digit ingestion via GT-FIN-FR-024). | no | GT synthesis wave S-GT4 (mechanics half; statutory half resolved S-GT2) | open |
| OQ-005 | GOQ-14 (kin; register lists F-cluster deadline CRs): "Accountant asks pending: calendario perpetuo vencimiento windows per NIT last-digit (JSF transcription, owner browser; atlas.com.gt cross-check only); consolidated IVA print (folds into GOQ-01); D-15-2026 reglamento status (folds into GOQ-12)." Affects FR-094/FR-098: with no ingested calendar vintage, no per-NIT deadline object is generated and the gap is flagged — never invented (consumes T1's GT-FIN-FR-024 ingestion surface). | no | GT synthesis wave S-GT4 → accountant track / owner-browser JSF transcription (W6; T1 owns the surface) | open |
| OQ-006 | GOQ-06 (kin; register lists TX3, F2 rate catalog): "5% IVA-retention additions (Pequeño suppliers ≥ Q2,500.01; Agropecuario on total factura) + 1.5% 'valor total' qualifier vs the D-20-2006/AG 425-2006 matrix — reconcile vs LIVA art. 54-bis text (GOQ-01 kin) before freezing the retention-rate catalog." Affects FR-085 (the pequeño's constancia-demand surface references the agent-side 5% ≥ Q2,500.01 rule): statutory floor consumed from GT-TAX-FR-057 ("mayor a" exclusive); the RetWeb render rows (GT-FIN-FR-039) and `iva_retention_rates.csv` secondary rows carry the pending status — never frozen here. | no | GT synthesis wave S-GT2 → acquisition queue (LIVA art. 54-bis text; this file consumes the kin rows only) | open |
