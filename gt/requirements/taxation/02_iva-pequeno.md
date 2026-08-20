# GT — Taxation — IVA pequeño contribuyente regime

| Field   | Value |
|---------|-------|
| Country | gt |
| Topic   | taxation |
| Status  | draft |
| Authors | GT synthesis wave S-GT2 |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the functional requirements for the Guatemala *Impuesto al
Valor Agregado* (IVA, value-added tax) **Régimen de Pequeño Contribuyente**
(small-taxpayer regime): the Q150,000.00 annual-gross qualification threshold
with its exact R20 legal provenance (D-27-92 arts. 45/46/50 as reformed by
D-4-2012 arts. 12/13/18 — entry, switch and stay/exit, de-oficio migration
history); the definitive 5% *tarifa* (rate) on monthly gross income (Art. 47)
and the monthly liability computation *gross × 5% − retentions soportadas*
(suffered retentions); the retention-by-agents track (pago definitivo,
*constancia de retención* (retention certificate), first-15-days remittance,
Q2,500 exclusive per-operation floor, card-operator rules); the no-retention
self-pay fallback via *declaración jurada simplificada* (simplified sworn
return) within the whole following calendar month, mandatory even at zero
activity or full retention; the Q50 invoice floor with its two complementary
statutory framings (R28) and the daily consolidated "Clientes Varios"/NIT
"CF" invoice; the single *libro de compras y ventas* (purchases-and-sales
book) statutory hook; the buyer side (no *crédito fiscal* (input-tax credit)
on pequeño invoices, exempt-entity buyers pay in full); the ISR/ISO relief
bundle; and the LAT art. 155 guard (the LAT names only the document type —
never pequeño thresholds).

It does **not** cover: the general regime (régimen general rate, credits,
refunds — Task 1, `01_iva-core.md`, GT-TAX-FR-001..045, cross-referenced
here by FR id); the general-regime retention matrix D-20-2006 +
AG 425-2006 and seller-side netting (Task 3 file, cluster TX3 — the pequeño
5% retention row cross-references it); ISR regimes (Tasks 4–5); the Código
Tributario procedure/sanction layer (Task 6); the libro column spec, LET
operation and SAT-2046 declaration generation (F-wave, clusters F3/F4 —
cross-referenced, never duplicated); and FEL document-type mechanics for
FPEQ/FCAP and the FEL mandate calendar for pequeños (already in
`gt/requirements/e-invoicing/01_document-types.md` as GT-EINV-FR-011/012
and the GT-EINV mandate file).

## 2. Legal Basis

Authority order (binding, per master evidence index preamble): the IVA
statutory layer = **Decreto 27-92 consolidated through D-10-2012 ONLY —
never cited alone**; every current-law row carries the qualifier "D-27-92
(texto ≤ D-10-2012), Art. N, reformado totalmente por el Artículo M del
D-4-2012" (per-article mapping as printed in the law copy: arts. 45←12,
46←13, chapter title←14, 47←15, 48←16, 49←17, 50←18); the post-2018
consolidated text is missing (GOQ-01). The IVA reglamento = "AG 5-2013,
reformado por AG 222-2019". The 55_/61_ SAT manuals are **secondary
prints**: every value they print is dated-as-of (~2013 / ≥ late-2018
respectively) and restates the statutory instruments, which outrank them
(fiscal-reporting authority order); they confirm, never re-derive, the
statutory parameters, and their form numbers (2043/2047/2049) are
superseded prints — current form identities come from the 48_ registry
(F-wave; R46 family discipline: RetWeb/48_ own form numbers). Dated values
(threshold, rate, floors, windows) follow the dated-instrument regime
D15/D16 (cite together): valid_from/valid_to rows + instrument provenance +
as-of qualifier, snapshot-on-write; historical rows are non-transmittable
class.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Ley del IVA, D-27-92 (texto ≤ D-10-2012), Arts. 45 y 46, reformados totalmente por los Artículos 12 y 13 del Decreto Número 4-2012: Art. 45: "Las personas individuales o jurídicas cuyo monto de venta de bienes o prestación de servicios no exceda de ciento cincuenta mil Quetzales (Q.150,000.00) en un año calendario, podrán solicitar su inscripción al Régimen de Pequeño Contribuyente." / Art. 46: "El contribuyente inscrito en el Régimen General, cuyos ingresos no superen la suma de ciento cincuenta mil Quetzales (Q.150,000.00), durante un año calendario, podrán [sic — agreement slip as printed] solicitar su inscripción al Régimen de Pequeño Contribuyente. La Administración Tributaria lo inscribirá, dándole aviso de sus nuevas obligaciones por los medios que estime convenientes y el período mensual a partir del cual inicia en este régimen." | Arts. 45/46: entry threshold — natural or legal persons whose gross sales of goods plus services do not exceed Q150,000.00 in a calendar year may request pequeño inscription; a Régimen General taxpayer whose income does not exceed the same sum may request the switch; SAT inscribes, notices the new obligations and fixes the starting monthly period | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 32–33 Arts. 45 y 46 + reform footnotes (EVID-175) |
| LB-002 | D-27-92 (texto ≤ D-10-2012), Art. 50, reformado totalmente por el Artículo 18 del D-4-2012: "El contribuyente puede permanecer en este régimen siempre que sus ingresos no superen la suma de ciento cincuenta mil Quetzales (Q.150,000.00) durante el año calendario anterior; al superar dicha suma deberá solicitar su inscripción al Régimen General, de lo contrario la Administración Tributaria lo podrá inscribir de oficio en el Régimen Normal o General dándole aviso de las nuevas obligaciones… y el período mensual a partir del cual inicia en el nuevo Régimen Normal o General. / Debe entenderse como Régimen Normal o General del Impuesto al Valor Agregado, el régimen mensual en el que el contribuyente determina su obligación tributaria y paga el impuesto, tomando en cuenta la diferencia entre el total de débitos y el total de créditos fiscales generados en cada período impositivo." | Art. 50: stay allowed while prior-calendar-year income ≤ Q150,000.00; on excess the taxpayer must request inscription to the Régimen General, failing which SAT inscribes it de oficio (with notice + starting period); statutory definition of "Régimen Normal o General" = the monthly regime determining tax by total débitos minus total créditos fiscales | `gt/sources/23_Ley_IVA_27-92.pdf` | p. 34 Art. 50 + reform footnote (EVID-175) |
| LB-003 | D-27-92 (texto ≤ D-10-2012), Art. 47, reformado totalmente por el Artículo 15 del D-4-2012: "La tarifa aplicable en el Régimen de Pequeño Contribuyente será de cinco por ciento (5%) sobre los ingresos brutos totales por ventas o prestación de servicios que obtenga el Contribuyente inscrito en este régimen, en cada mes calendario." | Art. 47: the pequeño tarifa is 5% on total gross income from sales or services obtained in each calendar month | `gt/sources/23_Ley_IVA_27-92.pdf` | p. 33 Art. 47 + reform footnote (EVID-176) |
| LB-004 | D-27-92 (texto ≤ D-10-2012), Art. 48, reformado totalmente por el Artículo 16 del D-4-2012: "Las personas individuales o jurídicas, entes o patrimonios, que sean agentes de retención del Impuesto al Valor Agregado y los que lleven contabilidad completa y designe la Administración Tributaria, actuarán como agentes de retención del Impuesto al Valor Agregado para pequeños contribuyentes, cuando acrediten en cuenta o de cualquier manera pongan a disposición ingresos a los contribuyentes calificados en este Régimen. La retención tendrá el carácter de pago definitivo del impuesto, y se calculará aplicando al total de los ingresos consignados en la factura de pequeño contribuyente, la tarifa establecida en el artículo anterior, debiendo entregar la constancia de retención respectiva. El monto retenido deberá enterarlo a la Administración Tributaria por medio de declaración jurada dentro del plazo de quince días del mes inmediato siguiente a aquel en que se efectuó el pago o acreditamiento." / "De no efectuarse la retención… el contribuyente inscrito… debe pagar el impuesto dentro del mes calendario siguiente al vencimiento de cada período mensual, a través de declaración jurada simplificada… independientemente que realice o no actividades afectas o que le hubiesen retenido la totalidad del impuesto en la fuente…" | Art. 48: retention agents for pequeño suppliers = IVA retention agents plus full-accounting taxpayers designated by SAT, triggered when they credit to account or otherwise make income available; the retention is a definitive tax payment at the Art. 47 tarifa on the total invoiced income, with a constancia de retención delivered; retained amounts remitted by sworn return within fifteen days of the month following the payment/accreditation (no "hábiles" printed); with no retention, the pequeño self-pays within the following calendar month via simplified sworn return, regardless of activity or full source retention | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 33–34 Art. 48 + reform footnote (EVID-176) |
| LB-005 | D-27-92 (texto ≤ D-10-2012), Art. 49, reformado totalmente por el Artículo 17 del D-4-2012: "…únicamente debe llevar el libro de compras y ventas habilitado por la Administración Tributaria, en el que debe registrar sus ventas y servicios prestados, los cuales puede consolidar diariamente en un sólo renglón y podrá llevarlo en forma física o electrónica." / "Están obligados a emitir siempre facturas de pequeño contribuyente en todas sus ventas o prestación de servicios mayores de cincuenta Quetzales (Q.50.00), cuando se trate de ventas o prestación de servicios menores de cincuenta Quetzales (Q.50.00), podrá consolidar el monto de las mismas en una sola, que debe emitir al final del día, debiendo conservar el original y copia en su poder." / "El valor que soporta la factura de pequeño contribuyente no genera derecho a crédito fiscal para compensación o devolución para el comprador de los bienes o al adquiriente de los servicios, constituyendo dicho valor costo para efectos del Impuesto Sobre la Renta." / "Los contribuyentes inscritos en este régimen, quedan relevados del pago y la presentación de la declaración anual, trimestral o mensual del Impuesto Sobre la Renta o de cualquier otro tributo acreditable al mismo." | Art. 49 obligations: the only statutory book is the single SAT-habilitated purchases-and-sales book (ventas consolidable daily into one row; physical or electronic); facturas mandatory for sales/services over Q50.00, sub-Q50 operations consolidable into one end-of-day factura (original and copy kept); the invoice value gives the buyer NO crédito fiscal — it is a cost for ISR purposes; pequeños are relieved of ISR declarations (annual, quarterly or monthly) and of any tax creditable to ISR | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 33–34 Art. 49 + reform footnote (EVID-176) |
| LB-006 | D-27-92 (texto ≤ D-10-2012), transitorios del D-4-2012: Art. 72: "…los contribuyentes inscritos en los anteriores Regímenes de Pequeño Contribuyente…, serán inscritos de oficio… al Régimen de Pequeño Contribuyente establecido en la presente Ley." / Art. 75 derogatorias: "a. El artículo 51 del Decreto Número 27-92…" / Art. 77: "entrara [sic] en vigencia ocho (8) días después de su publicación en el Diario Oficial." | D-4-2012 transitorios: prior-regime pequeños migrated de oficio into the new regime; old Art. 51 derogated; D-4-2012 in force eight days after gazette publication (= 25-Feb-2012 per the 55_ fn.1 dated confirmation, LB-012) | `gt/sources/23_Ley_IVA_27-92.pdf` | pp. 42–51 transitorios tail (EVID-179) |
| LB-007 | Reglamento de la Ley del IVA (AG 5-2013, reformado por AG 222-2019), Art. 55 (Capítulo XI): "1) Emitir facturas por las ventas o servicios cuyo importe sea menor a cincuenta quetzales (Q 50.00), cuando sea requerido por el comprador o adquirente. / 2) Para el debido control de las ventas… por los cuales no haya emitido factura, emitirá diariamente una factura consolidando el monto total facturado… / 3) Cuando se emita una factura por las transacciones del día, se consignará como nombre 'Clientes Varios', y como NIT: las iniciales 'CF'. / 4) Llevar un libro para registrar diariamente sus compras y ventas. Este libro deberá ser previamente habilitado por la Administración Tributaria y contener como mínimo: [compras lado izquierdo: número y fecha del documento, NIT y nombre del vendedor, precio total; ventas lado derecho: número y fecha de la factura de Pequeño Contribuyente, NIT y nombre del comprador si lo tuviere, precio total]" + "La sumatoria de la operaciones [sic] del mes deberá multiplicarla por el tipo impositivo, al resultado obtenido le restará el monto de las retenciones soportadas conforme las constancias recibidas y el resultado será el impuesto a pagar en la declaración." / "5) Presentar Declaración Jurada Mensual, haya o no realizado actividades afectas o que le hubiesen retenido la totalidad del impuesto en la fuente." | Reglamento Art. 55: sub-Q50 facturas on buyer request; daily consolidated factura for un-invoiced sub-Q50 sales; the consolidated daily factura carries name "Clientes Varios" and NIT "CF"; one prior-habilitated book with the minimum column set (compras/ventas sides; document no.+date, NIT+name, total price); monthly tax = month's operation sum × tarifa − retentions suffered per constancias; monthly sworn return mandatory with or without activity or full retention | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | pp. 23–24 Art. 55 (EVID-186) |
| LB-008 | Reglamento (AG 5-2013, reformado por AG 222-2019), Arts. 13, 22 num. 5 y 38: Art. 13: exentas usan constancias "salvo cuando se trate de pagos a pequeños contribuyentes, en cuyo caso deberán pagar el monto total de la factura." / Art. 22 num. 5 (gastos que no generan crédito, "entre otros"): "5) Las adquisiciones realizadas a los contribuyentes inscritos en el régimen de pequeño contribuyente del impuesto." / Art. 38: facturas de pequeño "se registrarán en el libro de compras sin consignar ningún valor en la columna correspondiente al impuesto" | Reglamento buyer-side rules: exempt entities buying from pequeños pay the FULL invoice (no constancia relief); pequeño-supplier acquisitions are on the open no-credit list; pequeño invoices register in the purchases book with no value in the IVA column (Task-1 cross-refs GT-TAX-FR-026/FR-041) | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | p. 5 Art. 13; p. 8 Art. 22.5; p. 19 Art. 38 (EVID-186, EVID-183) |
| LB-009 | Reglamento (AG 5-2013, reformado por AG 222-2019), Arts. 44, 49, 50, 52 y 59: Art. 44: "La constancia de retención referida en el artículo 48 de la Ley, deberá emitirse y entregarse al contribuyente a quien se le efectuó la retención…" / Art. 49: "…los agentes de retención…, practicarán las retenciones a pequeños contribuyentes, únicamente cuando paguen bienes y servicios cuyo valor sea mayor a dos mil quinientos Quetzales (Q 2,500.00)." / Art. 50: "Los operadores de tarjeta de crédito emitirán una constancia de retención consolidada mensual, conteniendo el detalle de las liquidaciones efectuadas que fueron objeto de retención durante el mismo mes calendario." / Art. 52: card payments by retention agents → no direct retention ("estará a cargo de los Operadores de Tarjeta de Crédito o Débito") / Art. 59 (transitional): exonerates multas for pre-reglamento non-retention on purchases "cuyo valor sea igual o menor a dos mil quinientos Quetzales (Q 2,500.00)" | Reglamento retention layer: constancia per Ley Art. 48 emitted and delivered to the retained taxpayer; pequeño retention only when paying goods/services with value **greater than** Q2,500.00 (exclusive floor — Art. 59's "igual o menor a" amnesty confirms the ≤ side never triggers); card operators issue one monthly consolidated constancia; card-settled purchases by agents are retained by the operator, not the agent | `gt/sources/24_Reglamento_IVA_AG_5-2013.pdf` | pp. 20–22 Arts. 44 y 49–52; p. 25 Art. 59 (EVID-185, EVID-186) |
| LB-010 | Ley de Actualización Tributaria, D-10-2012 (consolidated through Dto. 46-2022), Libro IV, Art. 155 (IVA art. 29): "a) Facturas… b) Facturas de Pequeño Contribuyente, para el caso de los contribuyentes afiliados al Régimen de Pequeño Contribuyente establecido en esta Ley… c) Notas de débito… d) Notas de crédito… e) Otros documentos…" | LAT Libro IV art. 155 restructures IVA art. 29 and names the "Facturas de Pequeño Contribuyente" document type — the LAT does NOT (re)define any pequeño threshold; thresholds remain in D-27-92 proper (R20 guard) | `gt/sources/26_LAT_10-2012.pdf` | pp. 52–57 Libro IV arts. 150–158, art. 155 (EVID-233) |
| LB-011 | Reglamento del Libro I de la LAT, AG 213-2013 (reformado por AG 167-2014), Art. 34: agents do not retain ISR "…Cuando el contribuyente tenga la calidad de Pequeño Contribuyente y así lo haga constar en la factura respectiva, el agente de retención deberá proceder conforme lo establece el artículo 48 de la Ley del Impuesto al Valor Agregado." | ISR reglamento art. 34: when the counterparty is a Pequeño Contribuyente (so stated on the invoice), the retention agent follows IVA Art. 48 — the ISR-side rule defers to the IVA pequeño regime; it is never a threshold source (R20 guard) | `gt/sources/28_Reglamento_LAT_AG_213-2013.pdf` | p. 17 Art. 34 (EVID-238) |
| LB-012 | SAT digest "Régimen de Pequeño Contribuyente" (55_, secondary print, ~2013, live at 2024-05-13 capture), p. 2 + fn.1: "Con la vigencia del Decreto 04-2012…, la cual inició el 25 de febrero de 2012, se configura el nuevo Régimen de Pequeño Contribuyente, derivado de lo cual, a partir del 1 de abril del 2012, los contribuyentes inscritos en las anteriores modalidades denominadas Régimen Simplificado 5% y Pequeño Contribuyente, Declaración Anual, fueron inscritos de oficio en el mencionado régimen por la SAT, siempre que sus ingresos no hayan superado la suma de Q150,000.00 durante el año 2011." / fn.1: "Artículos 45 y 46 de la Ley del Impuesto al Valor Agregado, reformados por los artículos 12 y 13 del Decreto 4-2012 del Congreso de la República." | 55_ fn.1 confirms the R20 attribution: Q150,000 and the modern pequeño chapter come from D-4-2012 arts. 12–13 (with 18) reforming LIVA arts. 45–46 (and 50); D-4-2012 in force 25-Feb-2012; de-oficio migration of the two old modalities on 1-Apr-2012 with a 2011 income test. Dated-as-of-~2013 secondary confirmation, never the primary source | `gt/sources/55_Pequeno_Contribuyente.pdf` | p. 2 intro + fn.1 (EVID-432) |
| LB-013 | 55_ (secondary print, ~2013), pp. 17–18 doctrine: "…el de pequeño contribuyente como el régimen en el que este paga con una tarifa del 5% sobre los ingresos brutos en forma mensual, sujeto a retención con carácter de pago definitivo…" / "El artículo 49 de la Ley… refiere que el valor que soporta la factura de pequeño contribuyente no genera derecho a crédito fiscal…, constituyendo dicho valor costo deducible para efectos del Impuesto Sobre la Renta." / "…la tarifa establecida en el artículo 47… se considera una diferencia sustancial a la tarifa que establece el artículo 10…" / "…el artículo 18 de la Ley…, que se refiere a la documentación para el reconocimiento del crédito fiscal, no se encuentra la Factura de Pequeño Contribuyente…" | SAT doctrine (dated-as-of ~2013, confirms the statutory layer): 5% on monthly gross income, definitive character including via retention; the pequeño invoice value is never crédito fiscal but an ISR-deductible cost; art. 18 credit documentation excludes the pequeño factura. Cite art. 49 by content, never by the digest's drifting paragraph ordinals (R57: "cuarto párrafo" here vs "último párrafo" elsewhere) | `gt/sources/55_Pequeno_Contribuyente.pdf` | pp. 17–18 (EVID-442) |
| LB-014 | 55_ (secondary print, ~2013), p. 11 numeral 10: "…disponible en papel mediante formulario SAT No. 2043 y en medio electrónico mediante formulario SAT No. 2047, en el plazo legalmente establecido, conforme lo regulado en el artículo 48 de la Ley del Impuesto al Valor Agregado, es decir, dentro del mes calendario siguiente al vencimiento de cada período mensual. Declaración que debe presentar independientemente que realice o no actividades afectas." / "De contar con constancias de retención…, se deberá incluir en la declaración el valor de éstas, mismo que será restado del impuesto determinado…" | 55_ on the declaration: window = the entire calendar month following each monthly period (LIVA art. 48), mandatory regardless of activity; retention constancias included and subtracted from the determined tax. Form numbers 2043/2047 are ~2013 prints (drift: 61_ prints 2046; the 48_ registry expects 2046/2241) — current identities are F-wave property | `gt/sources/55_Pequeno_Contribuyente.pdf` | p. 11 numeral 10 (+ p. 13 form names) (EVID-439) |
| LB-015 | 55_ (secondary print, ~2013), p. 6 numeral 4 + fn.6: "Solicitar autorización para la impresión de las facturas a utilizar, las cuales debe identificar como 'Factura de Pequeño Contribuyente' y agregar la frase en forma visible: 'No genera derecho a crédito fiscal'." (fn.6: "Artículo 30 del Acuerdo Gubernativo Número 5-2013, Reglamento del Impuesto al Valor Agregado.") | The pequeño factura must be titled "Factura de Pequeño Contribuyente" and carry the visible legend "No genera derecho a crédito fiscal" (reglamento Art. 30, cited here through the ~2013 secondary print — the art. 30 text is not otherwise in the corpus) | `gt/sources/55_Pequeno_Contribuyente.pdf` | p. 6 numeral 4 + fn.6 (EVID-434) |

## 3. Functional Requirements

### 3.1 Regime qualification, entry & exit (R20 provenance)

- **GT-TAX-FR-046:** The pequeño qualification threshold shall be stored as
  a dated row: annual gross **Q150,000.00** (sale of goods plus provision of
  services) per *año calendario* (calendar year), with instrument provenance
  exactly "D-27-92 arts. 45 (entry) / 46 (switch) / 50 (stay-exit) (texto ≤
  D-10-2012), reformados por D-4-2012 arts. 12/13/18" — the only verbatim
  source (R20, resolved at index level: the research-era "LAT D-10-2012"
  attribution was the error; 55_ fn.1 and the law copy agree). Guards:
  never cite the LAT or its reglamento (28_) for pequeño thresholds; the
  Q150,000.00 figure is D-4-2012-era and its currency carries the GOQ-01
  qualifier. (LB-001; LB-002; EVID-175; GOQ-01 → OQ-001)
- **GT-TAX-FR-047:** Entry and switch mechanics shall implement: natural or
  legal persons (individuals including liberal professionals; all mercantile
  society forms per the 55_ confirmation, LB-012) whose gross ≤ Q150,000.00
  may request inscription (Art. 45); a Régimen General taxpayer within the
  threshold may request the switch (Art. 46); in both cases SAT performs the
  inscription, notifies the new obligations and fixes the starting monthly
  period — the regime start is SAT-determined, not petition-determined.
  (LB-001; EVID-175)
- **GT-TAX-FR-048:** Stay/exit evaluation shall apply the Art. 50 rule:
  permanence while prior-calendar-year income ≤ Q150,000.00; on excess the
  taxpayer must request inscription to the Régimen General, and failing that
  SAT inscribes it **de oficio** (with notice of the new obligations and the
  starting period). The evaluation is a saas-side monitoring function with
  odoo surfacing (cumulative gross tracking + exit warning), never a silent
  automatic regime flip. (LB-002; EVID-175)
- **GT-TAX-FR-049:** The 2012 regime cutover shall be recorded as dated
  history rows (non-transmittable class): D-4-2012 rewrote the pequeño
  chapter (arts. 12–18 by article; chapter title by art. 14; old Art. 51
  derogated by art. 75 lit. a); D-4-2012 in force eight days after
  publication = **25-Feb-2012**; the two prior modalities (Régimen
  Simplificado 5%; Pequeño Contribuyente Declaración Anual) were migrated
  **de oficio on 1-Apr-2012**, conditional on 2011 gross ≤ Q150,000.00.
  (LB-006; LB-012; EVID-179, EVID-432)
- **GT-TAX-FR-050:** The regime boundary semantic shall be carried
  verbatim: "Régimen Normal o General" = the monthly regime determining the
  obligation as total débitos minus total créditos fiscales per period —
  the registration fact the SAT-DSI 1240-2021 FEL mandate keys on
  (general-regime registration); the pequeño FEL mandate layer (incl. the
  pequeño cohort resolution) is owned by the GT-EINV mandate file —
  cross-referenced, never re-derived. (LB-002; EVID-175)

### 3.2 Tarifa 5% & monthly computation

- **GT-TAX-FR-051:** The pequeño tarifa shall be a dated row: **5% on total
  gross income** (ingresos brutos, sales plus services) per calendar month
  (Art. 47, reformado por D-4-2012 art. 15), with **definitive** character —
  not a creditable prepayment. It registers in the Task-1 rate-exception
  registry (GT-TAX-FR-009 — cross-referenced, not re-derived) alongside the
  vehicle fixed fees; no other pequeño-side ad-valorem rate exists.
  (LB-003; EVID-176)
- **GT-TAX-FR-052:** Monthly liability shall be computed per the reglamento
  Art. 55 arithmetic: (sum of the month's operations × 5%) − (retentions
  soportadas per constancias received) = tax payable in the declaration;
  full source retention floors the result at zero. The month's operation
  sum is the gross invoiced total (daily-consolidated rows included).
  (LB-007; EVID-186)
- **GT-TAX-FR-053:** No statutory rounding rule exists in the corpus for
  the 5% computation: the SAT official rounding rule is unknown (GOQ-102
  kin) and the 55_ worked example's printed result "Q.179.00" for
  Q3,575.00 × 5% (exact **178.75**) is a digest arithmetic defect [sic]
  (R56) that shall never be copied — until GOQ-102 resolves, the
  implementation applies plain decimal arithmetic and records the
  divergence from the digest print. (LB-013; EVID-442; R56 → EVID-441;
  GOQ-102 → OQ-003)

### 3.3 Retention track (agent side)

- **GT-TAX-FR-054:** Retention-agent determination for pequeño suppliers
  shall cover exactly the Art. 48 universe: IVA retention agents plus
  taxpayers keeping full accounting designated by SAT, acting when they
  credit to account or otherwise make income available to regime members.
  The general-regime agent classes and their D-20-2006 rate matrix are
  owned by the Task 3 file (cluster TX3) — cross-referenced; the pequeño
  5% row here is the Art. 48 track, not a %-of-IVA retention.
  (LB-004; EVID-176)
- **GT-TAX-FR-055:** The retention itself shall be: **pago definitivo**
  (definitive payment) at the Art. 47 tarifa (5%) applied to the total
  income consigned in the factura de pequeño contribuyente, with the
  *constancia de retención* emitted and delivered to the retained taxpayer
  (reglamento Art. 44; format/media/system SAT-defined); the pequeño's duty
  to demand and keep constancias feeds FR-052's subtraction. (LB-004;
  LB-009; EVID-176, EVID-185)
- **GT-TAX-FR-056:** Agent remittance: the retained amount shall be
  entered via declaración jurada **within fifteen days of the month
  immediately following** the payment or accreditation (Art. 48 prints
  "quince días", no "hábiles"). The operational deadline and form identity
  (RetWeb SAT-2340, which prints "primeros 15 días hábiles") are F-wave
  property (clusters F2/F3) — cross-referenced; this file owns only the
  statutory window row. (LB-004; EVID-176)
- **GT-TAX-FR-057:** The per-operation retention floor shall be a dated
  row: agents retain on pequeño purchases **only when the value of the
  goods/services paid exceeds Q2,500.00** ("mayor a" — exclusive; Art. 59's
  transitional "igual o menor a" amnesty confirms the ≤ Q2,500.00 side
  never triggers). The RetWeb print "≥ Q2,500.01" (F-wave) is the same
  exclusive boundary; the 5% retention-addition catalog reconciliation vs
  the LIVA art. 54-bis text is GOQ-06 kin (with GOQ-01). (LB-009; EVID-185,
  EVID-186; GOQ-06 → OQ-002)
- **GT-TAX-FR-058:** Card-settled operations shall route retention to the
  card operator: operators (credit-card) issue **one monthly consolidated
  constancia** detailing the retained settlements of the same calendar
  month (reglamento Art. 50); a retention agent paying by credit or debit
  card does NOT retain itself — the retention is the operator's charge
  (reglamento Art. 52). (LB-009; EVID-185)

### 3.4 Declaration & self-pay fallback

- **GT-TAX-FR-059:** The no-retention fallback shall be: the pequeño
  self-pays the monthly tax **within the whole calendar month following the
  end of each monthly period** via *declaración jurada simplificada*, and
  the filing duty is mandatory **regardless of taxable activity or full
  source retention** (Art. 48 ¶2). GOQ-103 statutory half is answered
  here: the statute prints no fixed day-of-month and no días-hábiles count
  — only the whole-month window; the per-NIT-digit payment calendar is
  external (GOQ-103 register text, GOQ-14 kin). (LB-004; LB-014; EVID-176,
  EVID-439; GOQ-103 → OQ-004)
- **GT-TAX-FR-060:** Declaration content shall carry the month's gross
  operation sum, the constancia-backed retention credit subtracted
  (FR-052), and the resulting payable; current form identity and
  generation (SAT-2046 per the 48_ registry lineage; 55_'s 2043/2047/2049
  and 61_'s 2046 are dated prints) are owned by the F-wave (cluster F3) —
  cross-referenced, never re-derived here. (LB-007; LB-014; EVID-186,
  EVID-439)

### 3.5 Invoicing rules

- **GT-TAX-FR-061:** The Q50 invoice floor shall record BOTH complementary
  statutory framings (R28, resolved as complementary drafting — not a
  conflict): Ley Art. 49 — facturas mandatory for every sale/service
  **over Q50.00**, sub-Q50 operations consolidable into a single
  end-of-day factura (original and copy kept by the issuer); Reglamento
  Art. 55.1 — sub-Q50 facturas also emittable **on buyer request**. The
  product enforces the >Q50 mandate and supports the on-request path.
  (LB-005; LB-007; EVID-176, EVID-186)
- **GT-TAX-FR-062:** The daily consolidated factura for sub-Q50
  operations shall carry name **"Clientes Varios"** and NIT **"CF"** as
  the reglamento Art. 55.3 idiom. FEL-side final-consumer rules (receptor
  CF exact-string and the Q2,500 CF Gran-Total cap whose type list includes
  FPEQ/FCAP) are owned by the GT-EINV validation file — cross-referenced.
  (LB-007; EVID-186)
- **GT-TAX-FR-063:** Pequeño invoices shall be titled *Factura de Pequeño
  Contribuyente* and carry the visible legend **"No genera derecho a
  crédito fiscal"** (reglamento Art. 30, anchored through the 55_
  secondary print — dated-as-of; the art. 30 text is not otherwise in the
  corpus). The FEL document types FPEQ/FCAP are owned by
  GT-EINV-FR-011/012 — cross-referenced, not duplicated. (LB-015; EVID-434)

### 3.6 Buyer side

- **GT-TAX-FR-064:** Buyer-side treatment of pequeño invoices: the
  invoiced value generates **no crédito fiscal** for compensation or refund
  — it is a pure cost, ISR-deductible for the buyer (Art. 49; reglamento
  Art. 22 num. 5 open no-credit list + Art. 38 no-IVA-column registration
  are owned by GT-TAX-FR-026/FR-041 — cross-referenced); art. 18 credit
  documentation excludes the pequeño factura. Cited by content, never by
  the digest's drifting art. 49 paragraph ordinals (R57). (LB-005;
  LB-008; LB-013; EVID-176, EVID-183, EVID-442)
- **GT-TAX-FR-065:** Exempt-entity buyers purchasing from pequeño
  suppliers shall pay the **full invoice amount** — the constancia de
  exención gives no relief against pequeño invoices (reglamento Art. 13;
  general-regime statement GT-TAX-FR-015 — cross-referenced).
  (LB-008; EVID-186)

### 3.7 Book (statutory hook)

- **GT-TAX-FR-066:** The statutory book hook shall be recorded: the
  pequeño keeps **one single compras-y-ventas book**, SAT-habilitated
  before use, ventas consolidable daily into one row, kept physical or
  electronic (Art. 49 ¶1; reglamento Art. 55.4 minimum columns). The
  column spec, habilitación flow (SAT-7121) and LET operation are owned by
  the F-wave (clusters F3/F4, incl. the Régimen Electrónico variant) —
  cross-referenced, never duplicated. (LB-005; LB-007; EVID-176, EVID-186)

### 3.8 Relief bundle & guards

- **GT-TAX-FR-067:** The relief bundle shall be seeded as regime data:
  pequeños are relieved of ISR declarations (annual, quarterly or monthly)
  and of any tax creditable to ISR (Art. 49 final ¶, statutory). Secondary
  ~2013 detail (dated-as-of, 55_): no ISO; no mandatory contador; no full
  accounting while total assets ≤ Q25,000.00 (CCom art. 368); BUT if the
  Código de Comercio nonetheless obliges full accounting, the pequeño acts
  as ISR retention agent on acquisitions (CT arts. 28–29 — Task 6 file
  owns sanctions). (LB-005; EVID-176, EVID-440)
- **GT-TAX-FR-068:** Guard rows shall encode the R20 boundary: **LAT art.
  155 names only the factura type** (IVA art. 29 lit. b restructure) — it
  is the FPEQ statutory anchor, never a threshold source; 28_ art. 34
  merely defers the pequeño case to IVA Art. 48; no ISR-side pequeño
  regime exists (LAT creates none — Task 4/5 files' guard). Any citation
  path sourcing pequeño thresholds or the 5% from the LAT/28_ shall fail
  validation. (LB-010; LB-011; EVID-233, EVID-238)

## 4. Data Model

Dated rows follow D15/D16 (cite together): valid_from/valid_to + instrument
provenance + as-of qualifier; snapshot-on-write; threshold/rate/floor rows
are decree-bound, never constants (GOQ-50 pattern); historical rows are
non-transmittable class.

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_gt.iva.pequeno.threshold | amount / basis / period / valid_from / provenance | decimal / char / char / date / char | Q150,000.00; venta de bienes + prestación de servicios; año calendario; 2012-02-25; "D-27-92 arts. 45/46/50 (texto ≤ D-10-2012), reformados por D-4-2012 arts. 12/13/18" (R20); GOQ-01 currency qualifier | FR-046 |
| l10n_gt.iva.pequeno.rate | amount / base / character / provenance | decimal / char / char / char | 0.05; monthly gross ingresos brutos; definitive; "D-27-92 Art. 47 (texto ≤ D-10-2012), reformado por D-4-2012 art. 15"; registers in the Task-1 rate-exception registry (GT-TAX-FR-009) | FR-051 |
| l10n_gt.iva.pequeno.computation | formula | char | (Σ month operations × 0.05) − retentions soportadas; floor 0; rounding = plain decimal, no statutory rule (GOQ-102; R56 defect never copied) | FR-052, FR-053 |
| l10n_gt.iva.pequeno.retention | rate / character / constancia / remit_window / floor | decimal / char / boolean / char / decimal | 0.05 of total invoiced; pago definitivo; constancia de retención per operation (operator: monthly consolidated); first 15 días of following month (no hábiles printed; RetWeb 15 días hábiles = F-wave); per-operation floor Q2,500.00 exclusive ("mayor a" / "≥ Q2,500.01") | FR-054..057 |
| l10n_gt.iva.pequeno.card.rule | operator_retains / agent_retains | boolean / boolean | true / false (reglamento Arts. 50/52) | FR-058 |
| l10n_gt.iva.pequeno.declaration | window / mandatory_zero / retention_credit | char / boolean / boolean | whole following calendar month (LIVA art. 48; GOQ-103 statutory half); true (zero activity or full retention); true (constancias subtracted); form identity = F-wave (48_ registry: 2046 lineage) | FR-059, FR-060 |
| l10n_gt.iva.pequeno.invoice | per_op_floor / dual_framing / daily_consolidation / consolidated_name / consolidated_nit / title / legend | decimal / char / boolean / char / char / char / char | Q50.00; Ley 49 ">Q50 mandatory" + Reg. 55.1 "sub-Q50 on request" (R28 both recorded); true; "Clientes Varios"; "CF"; "Factura de Pequeño Contribuyente"; "No genera derecho a crédito fiscal" (Reg. Art. 30 via 55_ secondary) | FR-061..063 |
| l10n_gt.iva.pequeno.buyer | credit_fiscal / isr_cost / exempt_pays_full | boolean / boolean / boolean | false (never); true (deductible cost); true (Reg. Art. 13) | FR-064, FR-065 |
| l10n_gt.iva.pequeno.book | count / habilitation / consolidation | integer / char / char | 1 single compras-y-ventas libro; SAT-habilitated before use; ventas daily one-row; mechanics = F-wave | FR-066 |
| l10n_gt.iva.pequeno.regime | entry / switch / exit_test / exit_mode | char / char / char / char | solicitud art. 45; General→pequeño solicitud + SAT-set start period art. 46; prior-calendar-year gross > Q150,000 (art. 50); solicitud to General else SAT de oficio | FR-047, FR-048 |
| l10n_gt.iva.pequeno.history | event / date / class | char / date / char | D-4-2012 in force 2012-02-25; de-oficio migration 2012-04-01 (2011-income test; old modalities Simplificado 5% / Declaración Anual); art. 51 derogated (D-4-2012 art. 75 a); non-transmittable historical class | FR-049 |
| l10n_gt.iva.pequeno.relief | isr_declaration / iso / contador / full_accounting_cap | boolean / boolean / boolean / decimal | false (art. 49 final ¶, statutory); false / false / Q25,000.00 activo (secondary ~2013, dated-as-of; conditional ISR-agent duty if CCom obliges) | FR-067 |
| l10n_gt.iva.pequeno.guard | key | char | lat_art155_document_type_only; never_lat_28_thresholds; no_isr_pequeno_regime; rounding_rule_absent (GOQ-102) | FR-053, FR-068 |

## 5. Odoo Mapping

Layer semantics (thin-client architecture): `odoo` = data-capture,
configuration and selection surface in the LGPL client; `saas` = XML
emission, transformation and authoritative validation in the Elixir core;
`shared` = contract items both sides must honor identically. Taxation
defaults per wave plan: regime dated data (threshold/rate/floor/relief
rows) = `shared`; regime flag on journal/partner + invoice legend =
`odoo`; threshold-monitoring/exit evaluation = `saas` with odoo surfaces.
Model names stable across Odoo 17/18/19/20; no version-specific behavior
required by this file.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-046 | shared | — (config data §4) | l10n_gt.iva.pequeno.threshold row | Both sides resolve the same dated Q150,000.00 row; R20 provenance exact; GOQ-01 qualifier |
| FR-047 | odoo | res.partner / account.journal (regime selection) | pequeño regime flag + SAT start period | Entry/switch selection surface; SAT-fixed start period recorded, not inferred |
| FR-048 | saas | threshold-monitoring / exit evaluation module | prior-year + YTD gross evaluation | Odoo surfaces cumulative-gross dashboards and the exit warning; no silent auto-flip |
| FR-049 | shared | — (config data §4) | l10n_gt.iva.pequeno.history rows | Non-transmittable historical class (D16); displayed as regime provenance only |
| FR-050 | shared | — | regime-boundary semantic row | Citation spine; consumed by GT-EINV mandate cross-refs (1240-2021 registration fact) |
| FR-051 | shared | — (config data §4) | l10n_gt.iva.pequeno.rate row | 5% definitive; Task-1 rate-exception registry (GT-TAX-FR-009) points here |
| FR-052 | odoo | account.move / account.tax computation | monthly (gross × 5%) − retentions | Period aggregation incl. daily-consolidated rows; zero floor |
| FR-053 | odoo | account.tax computation (rounding) | plain decimal arithmetic | Never reproduce 55_ "Q.179.00" (R56); GOQ-102 kin |
| FR-054 | odoo | res.partner (agent determination) | retention-agent flags | Full-accounting + SAT-designated + IVA-agent universe; TX3 cross-ref for classes |
| FR-055 | odoo | account.move (retention posting) + constancia link | 5% pago definitivo line | Constancia emission/print surface = F-wave RetWeb; odoo records the credit input for FR-052 |
| FR-056 | odoo | account.move (agent remittance) | 15-días window row | Statutory "quince días" (no hábiles); RetWeb SAT-2340 deadline = F-wave |
| FR-057 | shared | — (config data §4) | Q2,500 exclusive floor row | "mayor a" semantics; RetWeb "≥ Q2,500.01" same boundary; GOQ-06 kin |
| FR-058 | odoo | account.payment / payment method routing | card-operator retention routing | Operator retains; agent abstains; monthly consolidated constancia reference |
| FR-059 | odoo | account.move (pequeño declaration skeleton) | whole-month window + mandatory-zero flag | GOQ-103 statutory half; per-NIT calendar external (GOQ-14 via GOQ-103) |
| FR-060 | odoo | account.move (declaration content) | gross sum + retention credit + payable | Form generation (SAT-2046) = F-wave; 55_/61_ form prints superseded |
| FR-061 | odoo | account.move (invoice emission) | Q50 floor + daily consolidation | Both R28 framings configured; end-of-day consolidated factura |
| FR-062 | odoo | account.move (consolidated factura) | name "Clientes Varios" / NIT "CF" | CF-cap and receptor rules = GT-EINV validation file |
| FR-063 | odoo | account.journal / account.move (legend) | title + "No genera derecho a crédito fiscal" | Regime flag on journal/partner drives FPEQ/FCAP selection (GT-EINV-FR-011/012) |
| FR-064 | odoo | account.move (supplier libro side) | no-credit guard on pequeño invoices | Task-1 FR-026/FR-041 own the list and the no-IVA column; ISR-deductible cost path → Tasks 4–5 |
| FR-065 | odoo | res.partner (exempt flag) + account.move | full-payment rule | No constancia relief vs pequeño; Task-1 FR-015 cross-ref |
| FR-066 | odoo | books surface (statutory hook) | single libro flag | Column spec/habilitación/LET = F-wave (F3/F4); never duplicated |
| FR-067 | shared | — (config data §4) | l10n_gt.iva.pequeno.relief rows | Statutory ISR relief (art. 49 final ¶) + dated-as-of secondary detail |
| FR-068 | shared | — | guard rows | LAT-art-155-never-thresholds citation validation; no ISR-side pequeño regime |

## 6. Acceptance Criteria

- **AC-001:** Given the threshold registry, when read as-of any date, then
  it resolves one dated row Q150,000.00 / año calendario with provenance
  "D-27-92 arts. 45/46/50 (texto ≤ D-10-2012), reformados por D-4-2012
  arts. 12/13/18" — and no surface cites the LAT, 26_ or 28_ as threshold
  source (grep-able guard). (FR-046, FR-068)
- **AC-002:** Given a pequeño whose prior-calendar-year gross exceeds
  Q150,000.00, when exit evaluation runs, then an exit warning fires
  (solicitud to General due; SAT de-oficio fallback recorded) and the
  regime is never flipped silently. (FR-048)
- **AC-003:** Given the rate registry, when the pequeño row is read, then
  it is 0.05 on monthly gross with the definitive flag and instrument
  provenance Art. 47 / D-4-2012 art. 15, and the Task-1 rate-exception
  registry (GT-TAX-FR-009) resolves it by cross-reference without
  re-derivation. (FR-051)
- **AC-004:** Given a month with gross invoiced Q3,575.00 and no
  constancias, when liability is computed, then the result is Q178.75 —
  never the 55_ print "Q.179.00" (R56); given full retention, then the
  payable is Q0.00 and the filing duty persists. (FR-052, FR-053, FR-059)
- **AC-005:** Given a retention agent paying a pequeño invoice of
  Q2,500.00 exactly, when retention is attempted, then it is refused
  (exclusive floor); given one of Q2,500.01, then 5% of the invoiced total
  is retained as pago definitivo, a constancia is recorded, and the
  remittance window reads "first 15 días of the following month".
  (FR-055, FR-056, FR-057)
- **AC-006:** Given a retention agent paying a pequeño supplier by credit
  or debit card, when the payment posts, then no agent retention occurs
  and the operator's monthly consolidated constancia is referenced.
  (FR-058)
- **AC-007:** Given a month with zero operations (or 100% source
  retention), when the period closes, then the monthly declaración
  simplificada obligation still stands with window = the entire following
  calendar month (no fixed day / días hábiles printed — GOQ-103 statutory
  half). (FR-059)
- **AC-008:** Given sub-Q50.00 sales across a day, when invoicing runs,
  then exactly one end-of-day consolidated factura "Clientes Varios" /
  NIT "CF" is issued (original+copy kept); given a sale over Q50.00, then
  an individual factura is mandatory; both R28 framings are present in
  configuration. (FR-061, FR-062)
- **AC-009:** Given a pequeño invoice emission, then the document is the
  FPEQ/FCAP type per GT-EINV-FR-011/012 and carries the visible legend
  "No genera derecho a crédito fiscal" with title "Factura de Pequeño
  Contribuyente". (FR-063)
- **AC-010:** Given a general-regime buyer booking a pequeño supplier
  invoice, when crédito fiscal is attempted, then it is refused (no-IVA
  column registration, ISR-cost path); given an Art. 8 exempt-entity
  buyer, then the full invoice amount is payable with no constancia
  relief. (FR-064, FR-065)
- **AC-011:** Given the books configuration, then exactly one combined
  compras-y-ventas libro hook exists for the regime (SAT-habilitated,
  daily one-row ventas consolidation) and column/LET mechanics resolve to
  the F-wave cross-reference, never to a duplicate spec here. (FR-066)
- **AC-012:** Given the relief bundle, then ISR declarations are suppressed
  for pequeños per art. 49 final ¶ (statutory) while the ~2013 secondary
  details (no ISO, no contador, Q25,000 activo cap) carry dated-as-of
  flags; and the history rows show 2012-02-25 vigor / 2012-04-01
  de-oficio migration as non-transmittable class. (FR-049, FR-067)

## 7. Open Questions

Master-index GOQ ids (register `gt/.extractions/00_MASTER_INDEX.md` §C);
question text verbatim from the register (abbreviated where noted). All
rows Status open; GOQs are trace-pending, not blockers.

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | GOQ-01 (kin; register lists TX1/TX2/TX3 freeze): "Post-2018 consolidated Ley IVA 27-92 text: Art. 29-'A' body, Ley 25 bis adder (electronic 100% refund), art. 54 B/BIS nomenclature, post-2012 exemption families (peaje/turismo/canasta), Q150,000 currency." Affects FR-046 (Q150,000 is a D-4-2012-era figure — currency verification pending) and, via art. 54-bis, FR-057's retention-addition reconciliation. | no | GT synthesis wave S-GT2 → acquisition queue (DCA Edición Legal / accountant) | open |
| OQ-002 | GOQ-06 (kin; register lists TX3/F2): "5% IVA-retention additions (Pequeño suppliers ≥ Q2,500.01; Agropecuario on total factura) + 1.5% 'valor total' qualifier vs the D-20-2006/AG 425-2006 matrix — reconcile vs LIVA art. 54-bis text (GOQ-01 kin) before freezing the retention-rate catalog." Affects FR-057's floor framing (statutory "mayor a" vs RetWeb "≥ Q2,500.01" — same exclusive boundary; catalog freeze pending). | no | GT synthesis wave S-GT2 (TX3 file owns the catalog row; Task 3 cross-ref) | open |
| OQ-003 | GOQ-102 (kin; register lists F3): "SAT official 5%-rounding rule unknown (55_ worked example prints Q.179.00 for 178.75 [sic]) — do not copy; verify rule." Affects FR-053/FR-052: plain decimal arithmetic until resolved; the R56 defect is recorded, never reproduced. | no | GT synthesis wave S-GT2 → W6 partner ask (SAT rule verification) | open |
| OQ-004 | GOQ-103 (kin; register lists F3): "Pequeño deadline shape: neither 55_ nor 61_ prints a fixed day/hábiles count — only LIVA art. 48 'mes calendario siguiente' + taxpayer-selected payment date; a per-NIT-digit calendar source is external (GOQ-14)." Statutory half answered in FR-059 (whole-month window, mandatory-at-zero); calendar half remains external. | no | GT synthesis wave S-GT2 → W6 partner ask (accountant, GOQ-14 kin) | open |
