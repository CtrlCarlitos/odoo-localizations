# SV — Chart of accounts — COA structure: account taxonomy, ESF/ERI/equity-statement/CFS architecture and classification attributes

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the account taxonomy and statement architecture of the SV
chart of accounts under the *Norma de Contabilidad NIIF para las PYMES*
(Accounting Standard for SMEs, 32_): the *estado de situación financiera*
(statement of financial position, ESF) root taxonomy — the (a)-(r) line-item
set as parent account classes with report-line binding, deferred-tax
accounts ALWAYS non-current, the current/non-current split with its
liquidity-ordering exception and operating-cycle/12-month rules; the
sub-classification surfaces of 4.11 (PPE classes; the related-party
segmentation of *cuentas por cobrar* (receivables) and *cuentas por pagar*
(payables) that feeds the Sección 33 disclosures; the inventory three-way
split; the payables split; provision and equity classes including the
statutory reserves consumed from the commercial-legal wave by id); the
share-capital and reserve disclosures of 4.12-4.13; the income-statement
architecture of Sección 5 (minimum items, the nature-vs-function expense
policy with function ⇒ separate *costo de ventas* (cost of sales), the
closed four-type OCI list, no extraordinary items, the discontinued single
amount, non-controlling-interest attribution); the *estado de cambios en el
patrimonio* (statement of changes in equity) with its 6.4 combined variant
and the 6.6 proposed-dividend note; and the *estado de flujos de efectivo*
(statement of cash flows, CFS) architecture of Sección 7 (the per-account
operación/inversión/financiación classification attribute, indirect/direct
methods, FX-flow rates with the unrealized-effect line, the interest and
dividend classification choices as config, non-monetary transactions
disclosed-not-flowed, the financing-liability reconciliation, the supplier-
finance tagging and disclosure of 7.19B-C, and the restricted-cash note).

It does **not** cover: PYME eligibility, the complete-FS-set contract,
policy governance or notes architecture (`01_framework-policies.md` — its
eligibility/config chassis and policy-event model are consumed here by FR
id); financial instruments, fair value and FX mechanics
(`03_financial-instruments-fx.md`); non-financial assets and their class
models (`04_nonfinancial-assets.md`); liabilities, equity instrument
classification, provisions measurement and employee benefits
(`05_liabilities-equity-benefits.md`); revenue recognition
(`06_revenue.md`); consolidation, NCI measurement and the Sección 33
disclosure builder itself (`07_groups-related-parties.md` — this file
defines the account-level segmentation attribute that file consumes by
id); deferred tax measurement and edition versioning
(`08_deferred-tax-adoption.md`). Fiscal computations (ISR/IVA/payroll/
special regimes) are owned by their waves by FR id — this file owns the
ACCOUNTING book's statement architecture only; book-vs-fiscal differences
route through N8's deferred-tax FRs (32_ Sección 29) and are never
re-derived here.

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling
R29): the operative framework LB = **32_** — *Norma de Contabilidad NIIF
para las PYMES, TERCERA EDICIÓN (Febrero 2025)*, IFRS Foundation official
Spanish translation — cited by section/párrafo as printed; this file's
operative span is Secciones 4-7 (txt PAGE 54-72), with Sección 10
policy-change mechanics and the Sección 29 deferred-tax measurement
consumed from their owning files by FR id. **33_** (EY *Guía Práctica de
NIIF y Sostenibilidad 2024/2025*) is SECONDARY-ONLY authority per R29(a):
it can NEVER be the sole LB of an FR; this file carries no 33_ LB row —
no version/horizon fact or contrast is needed for the taxonomy and
statement-architecture rules encoded here.

**SOQ-46 instrument-gap note (rides every FR in this file and this
wave):** the Norma itself is jurisdiction-neutral on who applies it —
"Las decisiones sobre qué entidades están requeridas o autorizadas a
utilizar las Normas NIIF de Contabilidad completas o la Norma de
Contabilidad NIIF para las PYMES recaen en las autoridades legislativas y
regulatorias y en los emisores de normas de las distintas jurisdicciones"
(Prólogo P12; txt PAGE 22) — and the SV adopting instrument (Consejo de
Vigilancia criteria per CC Arts. 443-444, or successor legislation) is
NOT in the corpus (commercial-legal/03 OQ-002 tracks the same
acquisition). The statement architecture encoded here therefore ships as
the Norma's own printed rules with NO invented SV presentation overlays;
it attaches to whatever company runs the NIIF-PYMES engine per the
framework flag of `01_framework-policies.md` SV-COA-FR-001 (informational
config, SOQ-53), never as a compliance gate.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 4: 4.2 line items: "(a) efectivo y equivalentes al efectivo; (b) deudores comerciales y otras cuentas por cobrar; (c) activos financieros [excluyendo los importes mostrados en (a), (b), (j) y (k)]; (d) inventarios; (e) propiedades, planta y equipo (incluyendo las plantas productoras en el alcance de la Sección 17…); (ea) propiedades de inversión registradas al costo menos la depreciación y el deterioro del valor acumulados; (f) propiedades de inversión registradas al valor razonable con cambios en resultados; (g) activos intangibles; (h) activos biológicos… se contabilizan al costo menos la depreciación acumulada y el deterioro de valor; (i) activos biológicos… llevados al valor razonable con cambios en resultados; (j) inversiones en asociadas; (k) inversiones en entidades controladas de forma conjunta; (l) acreedores comerciales y otras cuentas por pagar; (m) pasivos financieros [excluyendo los importes mostrados en (l) y (p)]; (n) pasivos y activos por impuestos corrientes; (o) pasivos por impuestos diferidos y activos por impuestos diferidos (éstos siempre se clasificarán como no corrientes); (p) provisiones; (q) participaciones no controladoras, presentadas dentro del patrimonio de forma separada al patrimonio atribuible a los propietarios de la controladora; y (r) patrimonio atribuible a los propietarios de la controladora." 4.3: "partidas adicionales (incluso desagregando las partidas enumeradas en el párrafo 4.2), encabezamientos y subtotales… cuando dicha presentación sea relevante". 4.4: corrientes/no corrientes "como categorías separadas… excepto cuando una presentación basada en el grado de liquidez proporcione una información fiable que sea más relevante. Cuando se aplique tal excepción, todos los activos y pasivos se presentarán de acuerdo con su liquidez aproximada (ascendente o descendente)." 4.6 asset current when: "(a) espera realizarlo o tiene la intención de venderlo o consumirlo en su ciclo normal de operación; (b) mantiene el activo principalmente con fines de negociación; (c) espera realizar el activo dentro de los doce meses siguientes después de la fecha de presentación; o (d) el activo sea efectivo o un equivalente al efectivo, salvo que su utilización esté restringida… durante, al menos, los doce meses…" + "Cuando el ciclo normal de operación no sea claramente identificable, se supondrá que su duración es de doce meses." 4.7 liability current when: "(a) espera liquidarlo en el transcurso del ciclo normal de operación…; (b) mantiene el pasivo principalmente con fines de negociación; (c) el pasivo debe liquidarse dentro de los doce meses siguientes a la fecha de presentación; o (d) la entidad no tiene un derecho incondicional para aplazar la cancelación del pasivo durante, al menos, los doce meses siguientes…". 4.8-4.10: "Esta Norma no prescribe ni el orden ni el formato"; denominations/order may change per the entity's nature; additional-item assessment on (a) importes, naturaleza y liquidez de los activos; (b) la función de los activos; (c) los importes, la naturaleza y el plazo de los pasivos. 4.11 sub-classifications (ESF or notes): "(a) propiedades, planta y equipo en clasificaciones adecuadas a la entidad; (b) cuentas comerciales por cobrar y otras cuentas por cobrar que muestren por separado los importes por cobrar de partes relacionadas y por cobrar de otras partes; (c) inventarios… (i) poseídos para ser vendidos en el curso normal del negocio; (ii) en proceso de producción con vistas a esa venta; y (iii) en forma de materiales o suministros…; (d) cuentas por pagar comerciales y otras cuentas por pagar, mostrando de forma separada los importes por pagar a los proveedores comerciales, por pagar a partes relacionadas, ingresos diferidos y acumulados; (e) provisiones por beneficios a los empleados y otras provisiones; y (f) clases de patrimonio, tales como capital pagado, primas de emisión, ganancias acumuladas y partidas de ingreso y gasto que, como permitido o requerido por esta Norma, se reconocen en otro resultado integral y se presentan por separado en el patrimonio." 4.12: per share class "(i) el número de acciones autorizadas. (ii) el número de acciones emitidas y pagadas totalmente, así como las emitidas pero aún no pagadas en su totalidad. (iii) el valor nominal de las acciones, o el hecho de que no tengan valor nominal. (iv) una conciliación entre el número de acciones en circulación al principio y al final del periodo. No es necesario presentar esta conciliación para periodos anteriores. (v) los derechos, privilegios y restricciones… incluyendo… las restricciones que afecten a la distribución de dividendos y al reembolso del capital. (vi) las acciones de la entidad mantenidas por ella o por sus subsidiarias o asociadas. (vii) las acciones cuya emisión está reservada como consecuencia de la existencia de opciones o contratos para la venta de acciones, describiendo las condiciones e importes." + "(b) una descripción de cada reserva que figure en patrimonio." 4.13 no-share-capital entities (fórmula societaria o fiduciaria): "información equivalente a la requerida en el párrafo 4.12(a), mostrando los cambios producidos durante el periodo en cada una de las categorías que componen el patrimonio y los derechos, privilegios y restricciones asociados a cada una." 4.14 binding-sale-agreement disposal: description of assets/group, facts and circumstances, carrying amounts | The ESF shall present line items (a)-(r): cash and equivalents; trade and other receivables; financial assets [excluding (a),(b),(j),(k)]; inventories; PPE (incl. bearer plants); investment property at cost less depreciation and impairment; investment property at FV through profit or loss; intangibles; biological assets at cost model; biological assets at FV model; investments in associates; investments in jointly controlled entities; trade and other payables; financial liabilities [excluding (l),(p)]; current tax liabilities and assets; deferred tax liabilities and assets (ALWAYS classified non-current); provisions; non-controlling interests presented within equity separately from owners' equity; equity attributable to owners. Additional items/headings/subtotals when relevant. Current/non-current as separate categories EXCEPT where a liquidity-ordering presentation is reliable and more relevant — then ALL assets and liabilities in approximate liquidity order. Current asset tests: operating cycle / trading / 12 months / unrestricted cash; cycle presumed 12 months when not identifiable. Current liability tests mirror + no unconditional right to defer ≥12 months. Neither order nor format prescribed; renaming/reordering allowed; additional-item assessment on amounts/nature/liquidity, function, term. Sub-classifications (ESF or notes): PPE in adequate classes; receivables split related parties vs others; inventories 3-way (for sale / WIP / materials and supplies); payables split suppliers / related parties / deferred income / accruals; employee-benefit vs other provisions; equity classes (paid-in capital, share premium, retained earnings, OCI items presented separately in equity). Share-capital disclosures per class: authorized; issued+paid and issued-not-fully-paid; par or no-par; circulation reconciliation (current period only); rights/privileges/restrictions incl. dividend and capital-repayment restrictions; treasury holdings (entity/subsidiaries/associates); option/contract-reserved shares with conditions and amounts; each equity reserve described; no-share-capital entities disclose equivalent info | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 4, párrs. 4.2-4.14 (txt PAGE 54-58) (EVID-278) |
| LB-002 | Norma NIIF para las PYMES, Sección 5: 5.4(b) — "se reconocen cuatro tipos de otro resultado integral… fuera del resultado, cuando se producen: (i) algunas ganancias y pérdidas que surjan de la conversión de los estados financieros de un negocio en el extranjero…; (ii) algunas ganancias y pérdidas actuariales…; (iii) algunos cambios en los valores razonables de los instrumentos de cobertura…; y (iv) cambios en el superávit de revaluación para las propiedades, planta y equipo medidos de acuerdo con el modelo de revaluación." 5.5 minimum items: "(a) los ingresos de actividades ordinarias. (b) los costos financieros. (c) la participación en el resultado del periodo de las inversiones en asociadas… y entidades controladas de forma conjunta… contabilizadas utilizando el método de la participación. (d) el gasto por impuestos excluyendo los impuestos asignados a los apartados (e), (g) y (h)… (e) un importe único que comprenda el total de: (i) el resultado después de impuestos de las operaciones discontinuadas; y (ii) las ganancias o pérdidas después de impuestos atribuible al deterioro, o reversión de éste, de los activos en las operaciones discontinuadas… (f) el resultado (si una entidad no tiene partidas de otro resultado integral, no es necesario presentar esta línea). (g) cada partida de otro resultado integral… clasificada por naturaleza… agruparán en las que…: (i) no se reclasifiquen posteriormente en el resultado del periodo —es decir, las del párrafo 5.4(b)(i), (ii) y (iv); y (ii) se reclasifiquen posteriormente… —es decir, las del párrafo 5.4(b)(iii). (h) la participación en el otro resultado integral de asociadas… (i) el resultado integral total (si una entidad no tiene partidas de otro resultado integral, puede usar otro término para esta línea tal como resultado del período)." 5.6: "(a) El resultado del periodo atribuible a (i) participación no controladora; y (ii) propietarios de la controladora. (b) El resultado integral total del periodo atribuible a (i)… (ii)…". 5.7 two-statement split: ER presents (a)-(f) with result last; ERI begins with result then (g)-(i) + 5.6. 5.9 additional items/headings/subtotals when relevant. 5.11: "Una entidad no presentará ni describirá ninguna partida de ingreso o gasto como 'partidas extraordinarias' en el estado del resultado integral (o en el estado de resultados, si se presenta) o en las notas." 5.10-5.11(b) expense breakdown "utilizando una clasificación basada en la naturaleza o en la función de los gastos dentro de la entidad, lo que proporcione una información que sea fiable y más relevante"; naturaleza: groups (depreciación, compras de materiales, costos de transporte, beneficios a los empleados, costos de publicidad) "no los redistribuirá atendiendo a las diferentes funciones"; función: "Como mínimo una entidad revelará, según este método, su costo de ventas de forma separada de otros gastos." | Comprehensive-income statement: four OCI types only (foreign-operation translation; actuarial gains/losses; hedging-instrument FV changes — the recyclable type; PPE revaluation-surplus changes). Minimum period items: revenue; finance costs; equity-method share of associates/JCEs result; tax expense (excluding amounts allocated to discontinued, OCI and associate-OCI items); single amount for discontinued operations (after-tax result + after-tax impairment/reversals); result (line omittable with no OCI); each OCI item by nature grouped non-recyclable vs recyclable; equity-method share of associates' OCI; total comprehensive income (renameable "resultado del período" when no OCI). Result and total comprehensive income each attributed separately to NCI and owners. Two-statement variant: ER items (a)-(f) ending in result; ERI starts with result. No income/expense item ever presented or described as "extraordinary items" in the statements or notes. Expense breakdown by nature (no functional reallocation) or by function — function requires cost of sales separately from other expenses | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 5, párrs. 5.4-5.11 (txt PAGE 59-62) (EVID-279) |
| LB-003 | Norma NIIF para las PYMES, Sección 6: 6.2-6.3 equity statement includes: "(a) el resultado integral total del periodo, mostrando de forma separada los importes totales atribuibles a los propietarios de la controladora y los atribuibles a las participaciones no controladoras; (b) para cada componente de patrimonio, los efectos de la aplicación retroactiva o la reexpresión retroactiva reconocidos según la Sección 10…; y (c) para cada componente del patrimonio, una conciliación entre los importes en libros, al inicio y al final del periodo, revelando por separado los cambios resultantes de: (i) el resultado del periodo; (ii) otro resultado integral; y (iii) los importes de las inversiones hechas por los propietarios y de los dividendos y otras distribuciones hechas a éstos…, mostrando por separado las emisiones de acciones, las transacciones de acciones propias en cartera, los dividendos y otras distribuciones a los propietarios, y los cambios en las participaciones en la propiedad en subsidiarias que no den lugar a una pérdida de control." 6.4: combined statement allowed "si los únicos cambios en su patrimonio… surgen del resultado, pago de dividendos, correcciones de errores de los periodos anteriores y cambios de políticas contables". 6.5: "(a) ganancias acumuladas al comienzo del periodo…; (b) dividendos declarados durante el periodo, pagados o por pagar; (c) reexpresiones de ganancias acumuladas por correcciones de los errores de periodos anteriores; (d) reexpresiones… por cambios en políticas contables; y (e) ganancias acumuladas al final del periodo…". 6.6 notes: "(a) el importe de dividendos propuestos (o declarados) antes de que se autoricen los estados financieros para su emisión, pero no reconocidos como una distribución…, y el importe por acción; y (b) el importe de cualquier dividendo preferente de carácter acumulativo que no haya sido reconocido." | Statement of changes in equity: total comprehensive income split owners/NCI; per-component retroactive-application/re-expression effects (Section 10 events); per-component opening-to-closing reconciliation separately revealing result, OCI, and owner investments/distributions — separately showing share issues, treasury-share transactions, dividends and other distributions, and ownership-interest changes in subsidiaries without loss of control. Combined income-and-retained-earnings statement when the ONLY equity changes are result, dividend payments, prior-period error corrections and policy changes; its items: opening retained earnings; dividends declared (paid or payable); error re-expressions; policy-change re-expressions; closing retained earnings. Notes: proposed/declared-before-authorization dividends not recognized as a distribution, with per-share amount; unrecognized cumulative preference dividends | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 6, párrs. 6.2-6.6 (txt PAGE 63-64) (EVID-279) |
| LB-004 | Norma NIIF para las PYMES, Sección 7: 7.2 cash equivalents: "inversiones a corto plazo de gran liquidez… fácilmente convertibles en importes determinados de efectivo… riesgo poco significativo… vencimiento próximo, por ejemplo, tres meses o menos"; overdrafts "se consideran normalmente actividades de financiación similares a los préstamos… si son reembolsables a petición… y forman una parte integral de la gestión de efectivo… son componentes del efectivo". 7.3 flows "clasificados por actividades de operación, actividades de inversión y actividades de financiación". 7.4 operating = "las principales actividades productoras de ingresos de actividades ordinarias" (incl. income-tax payments "a menos que puedan clasificarse específicamente dentro de las actividades de inversión y financiación"). 7.5 investing = LT-asset acquisition/disposal; subsidiary acquisitions/sales "deberán presentarse por separado, y clasificarse como actividades de inversión"; hedging-contract flows classified "de la misma forma que los flujos de efectivo de la partida que está siendo cubierta". 7.6 financing = "cambios en el tamaño y composición de los capitales aportados y de los préstamos tomados" incl. "(e) pagos realizados por el arrendatario para reducir un pasivo pendiente procedente de un arrendamiento financiero". 7.7-7.10: indirect (adjust result for inventory/AR/AP deltas; non-cash items — "depreciación, provisiones, impuestos diferidos, ingresos (gastos) acumulados… no recibidos (pagados) todavía en efectivo, pérdidas y ganancias de cambio no realizadas y participación en ganancias no distribuidas de asociadas"; other investing/financing-related items) OR direct ("las principales categorías de cobros y pagos en términos brutos" — from the records or by adjusting sales/cost of sales). 7.12: FX flows "aplicando… la tasa de cambio entre ambas monedas en la fecha en que se produjo el flujo de efectivo"; 7.12A: "Las ganancias o pérdidas no realizadas… no son flujos de efectivo. Sin embargo… debe presentarse en el estado de flujos de efectivo el efecto de la variación en las tasas de cambio sobre el efectivo y los equivalentes al efectivo… volverá a medir… a las tasas de cambio del final del periodo. La entidad presentará por separado la ganancia o pérdida no realizada…" 7.14-7.16 interest/dividends: "presentará por separado… clasificará… de forma coherente, periodo a periodo"; interest paid + interest/dividends received MAY be operating, or financing/investing respectively; dividends paid MAY be financing or operating. 7.17 income tax: separate, operating "a menos que puedan ser específicamente identificados con actividades de inversión y de financiación"; if split, disclose total taxes paid. 7.18: "excluirá del estado de flujos de efectivo las transacciones de inversión y financiación que no requieran el uso de efectivo… revelará estas transacciones en cualquier parte de los estados financieros" (asset-acquisition-via-liability or finance lease; purchase via capital increase; debt-to-equity). 7.19A: financing-liability reconciliation (opening vs closing ESF balances) including "(a) cambios procedentes de los flujos de efectivo por financiación; (b) cambios que surgen de la obtención o pérdida del control de subsidiarias u otros negocios; (c) efectos de las variaciones en las tasas de cambio…; (d) cambios en el valor razonable; y (e) otros cambios." 7.19B supplier-finance: "uno o varios proveedores de financiación ofrecen pagar los importes que una entidad debe a sus proveedores y la entidad se compromete a pagar según los términos y condiciones… en la misma fecha… o en una fecha posterior"; "suelen denominarse financiación de 'la cadena de suministro', 'financiación de cuentas por pagar' o 'acuerdos de factoraje inverso'"; NOT supplier-finance: credit-enhancement-only (guarantees incl. letters of credit) and direct-settlement instruments (credit-card settlement with obligation to the issuing bank). 7.19C: aggregate disclosure of "(a) los términos y condiciones clave… (separately for differing key terms); (b) al principio y al final del periodo: (i) los importes en libros, y las partidas asociadas presentadas en el estado de situación financiera… de los pasivos financieros que forman parte de un acuerdo…; (ii)… para los que los proveedores ya han recibido el pago…, a menos que sea impracticable…; (iii) el rango de fechas de vencimiento de los pagos… tanto para los pasivos financieros revelados… como para las cuentas comerciales por pagar comparables que no formen parte…"; "(c) el tipo y el efecto de los cambios no monetarios…" (business combinations, FX differences, 7.18 transactions; settling enrolled payables may classify as a financing outflow with no financing inflow = non-cash change). 7.20: "revelará los componentes del efectivo y equivalentes de efectivo, y presentará una conciliación… con las partidas equivalentes presentadas en el estado de situación financiera" (not required if identical). 7.21: "revelará, junto con un comentario de la gerencia, el importe de los saldos de efectivo y equivalentes al efectivo significativos… que no están disponibles para ser utilizados por ésta… debido a, entre otras razones, controles de cambio de moneda extranjera o por restricciones legales." | Cash-flow statement: three activity classes (operating = main revenue-producing activities incl. income-tax payments unless specifically investing/financing; investing = LT assets, subsidiary acquisitions/sales aggregated separately; financing = capital and borrowings incl. finance-lease liability reductions; cash equivalents = short-term highly-liquid ≤~3-month investments; on-demand overdrafts integral to cash management are cash). Indirect or direct method. FX flows at flow-date rate; unrealized rate effect on held cash remeasured at closing rates presented as a SEPARATE line. Interest/dividends presented separately and classified consistently: interest paid operating-or-financing; interest+dividends received operating-or-investing; dividends paid financing-or-operating (free classification choices). Income-tax flows separate, operating unless specifically identifiable; total disclosed when split. Non-monetary investing/financing transactions excluded from CFS but disclosed (asset via liability/lease; purchase via capital increase; debt-to-equity). Financing-liability balance reconciliation (cash flows; control changes; FX; FV; other). Supplier-finance arrangements (supply-chain financing / payables financing / reverse factoring; NOT credit-enhancement-only or direct-settlement): payables tagging + aggregate disclosure of key terms, carrying amounts at both dates with associated line items, financier-paid amounts unless impracticable, maturity ranges vs comparable trade payables, and non-cash change types. Components-of-cash note + reconciliation (waivable when identical); restricted/unavailable significant cash balances with management commentary | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 7, párrs. 7.2-7.21 (txt PAGE 65-72) (EVID-280) |

## 3. Functional Requirements

### 3.1 ESF root taxonomy and classification rules (Sección 4)

- **SV-COA-FR-022:** The system shall implement the chart-of-accounts root
  taxonomy as parent account classes bound one-to-one to the 4.2 ESF
  line-item set, cited as printed: (a) *efectivo y equivalentes al
  efectivo* (cash and cash equivalents); (b) *deudores comerciales y otras
  cuentas por cobrar* (trade and other receivables); (c) *activos
  financieros* (financial assets) excluding the amounts shown in (a), (b),
  (j) and (k); (d) *inventarios* (inventories); (e) *propiedades, planta y
  equipo* (property, plant and equipment) including *plantas productoras*
  (bearer plants, Sección 17 scope); (ea) investment property carried at
  cost less accumulated depreciation and impairment; (f) investment
  property carried at fair value with changes in results; (g) *activos
  intangibles* (intangible assets); (h) biological assets at the cost
  model; (i) biological assets at the fair-value model; (j) *inversiones
  en asociadas* (investments in associates); (k) *inversiones en entidades
  controladas de forma conjunta* (investments in jointly controlled
  entities); (l) *acreedores comerciales y otras cuentas por pagar* (trade
  and other payables); (m) *pasivos financieros* (financial liabilities)
  excluding the amounts shown in (l) and (p); (n) current-tax liabilities
  and assets; (o) deferred-tax liabilities and assets; (p) *provisiones*
  (provisions); (q) *participaciones no controladoras* (non-controlling
  interests) presented within equity SEPARATELY from (r) equity
  attributable to the owners of the controladora — every account in the
  template carries exactly one parent class whose report line is the
  statement binding, and the ESF generator shall render these items as
  separate lines with additional items, headings and subtotals (including
  disaggregation of the 4.2 items) whenever presentation is relevant to
  understanding the entity's financial position (4.3; the per-item
  measurement engines are owned by files 03-08 by id — the split pairs
  (ea)/(f) and (h)/(i) exist precisely because the measurement model
  differs within them).
  (LB-001; EVID-278)
- **SV-COA-FR-023:** The system shall enforce 4.2(o) as a HARD
  classification invariant: deferred-tax asset and deferred-tax liability
  accounts are ALWAYS classified non-current — the current/non-current
  attribute of any account whose parent class is (o) shall be locked to
  non_current and no configuration, template edit or reclassification
  shall place a deferred-tax balance in a current class or current report
  section (the deferred-tax measurement engine and its offset rules are
  owned by `08_deferred-tax-adoption.md` by id; this FR owns presentation
  only).
  (LB-001; EVID-278)
- **SV-COA-FR-024:** The system shall implement the current/non-current
  split as separate ESF categories for assets and liabilities (per
  FR-025/FR-026) WITH the liquidity-ordering exception as a per-company
  presentation election: when a presentation based on the degree of
  liquidity provides information that is reliable and MORE relevant, ALL
  assets and liabilities are presented in approximate liquidity order
  (ascending or descending) — the exception is all-or-nothing per
  statement (never a mixed current/non-current + liquidity hybrid), is a
  presentation classification subject to the uniformity and comparative
  reclassification rules consumed from
  `01_framework-policies.md` SV-COA-FR-009 by id, and shall be recorded
  with its relevance basis (the election record feeding the 8.6 judgments
  note slot of SV-COA-FR-021 by id).
  (LB-001; EVID-278)
- **SV-COA-FR-025:** The system shall classify an asset as CURRENT when
  any of: (a) it is expected to be realized, or is intended for sale or
  consumption, in the entity's normal *ciclo de operación* (operating
  cycle); (b) it is held principally for trading (*fines de negociación*);
  (c) it is expected to be realized within twelve months after the
  presentation date; or (d) it is cash or a cash equivalent UNLESS its
  use is restricted from being exchanged or used to settle a liability
  for at least twelve months from the presentation date — all other
  assets are non-current; when the normal operating cycle is not clearly
  identifiable its duration is PRESUMED to be twelve months.
  (LB-001; EVID-278)
- **SV-COA-FR-026:** The system shall classify a liability as CURRENT
  when any of: (a) it is expected to be settled in the normal course of
  the operating cycle; (b) it is held principally for trading; (c) it
  must be settled within twelve months after the presentation date; or
  (d) the entity does NOT have an unconditional right to defer
  settlement for at least the twelve months following the reporting date
  — all other liabilities are non-current (the ≥12-month deferral RIGHT
  governs, not the lender's short-term intent).
  (LB-001; EVID-278)
- **SV-COA-FR-027:** The system shall implement the format-freedom
  contract of 4.8-4.10: the Norma prescribes neither the order nor the
  format of ESF items — 4.2 is a list of items sufficiently different in
  nature or function to justify separate presentation, and the account
  template may adapt denominations and ordering of items (or groups of
  similar items) to the nature of the entity and its transactions;
  presentation of ADDITIONAL items by separate line (beyond the 4.2 set
  and any 4.3 disaggregation) is assessed on (a) the amounts, nature and
  liquidity of the assets, (b) the function of the assets within the
  entity, and (c) the amounts, nature and term of the liabilities — the
  assessment recorded on the template/report configuration so the
  uniformity rules of SV-COA-FR-009 (by id) apply to it.
  (LB-001; EVID-278)

### 3.2 Sub-classifications and share-capital disclosures (4.11-4.14)

- **SV-COA-FR-028:** The system shall sub-classify *propiedades, planta y
  equipo* into classes adequate to the entity (in the ESF or the notes):
  the PPE parent class (e) decomposes into per-class accounts (land,
  buildings, machinery, vehicles, furniture, bearer plants among others
  as adequate), each class carrying its own measurement-policy binding —
  cost model or revaluation model per class, class-wide — consumed from
  `04_nonfinancial-assets.md` by id (17.15; the class model, component
  depreciation and the superávit-de-revaluación routing live there; this
  FR owns the ESF sub-classification surface only).
  (LB-001; EVID-278)
- **SV-COA-FR-029:** The system shall implement the related-party
  segmentation of receivables as an ACCOUNT-LEVEL attribute feeding both
  the 4.11(b) split and the Sección 33 disclosures: *cuentas comerciales
  por cobrar y otras cuentas por cobrar* (trade and other receivables)
  shall show SEPARATELY amounts receivable from *partes relacionadas*
  (related parties) and receivable from other parties — realized as a
  related-party flag on the receivable account families (or dedicated
  related-party AR accounts) plus the related-party marking of the
  counterparty on each line, so the ESF/notes 4.11(b) split and the
  Sección 33 transaction-and-balance disclosure builder of
  `07_groups-related-parties.md` consume the SAME segmentation by FR id
  (that file owns the related-party definition set and disclosure
  builder; this FR defines only the account-level segmentation
  attribute).
  (LB-001; EVID-278)
- **SV-COA-FR-030:** The system shall sub-classify inventories showing
  separately amounts: (i) held for sale in the ordinary course of
  business; (ii) *en proceso de producción* (work in process) with a view
  to such sale; and (iii) in the form of materials or supplies for
  consumption in the production process or in the rendering of services —
  a three-way valuation-category attribute on inventory accounts (the
  costing engines — FIFO/AVG per nature-and-use class, NRV — are owned
  by `04_nonfinancial-assets.md` by id).
  (LB-001; EVID-278)
- **SV-COA-FR-031:** The system shall sub-classify *cuentas por pagar
  comerciales y otras cuentas por pagar* (trade and other payables)
  showing separately amounts payable to: commercial suppliers
  (*proveedores comerciales*); related parties (the SAME segmentation
  attribute as FR-029 applied to payables, feeding Sección 33 by id via
  `07_groups-related-parties.md`); *ingresos diferidos* (deferred
  income); and *acumulados* (accruals) — a four-way payable-category
  attribute on payable accounts; the supplier-finance tagging of FR-053
  rides on the supplier category.
  (LB-001; EVID-278)
- **SV-COA-FR-032:** The system shall sub-classify provisions into
  *provisiones por beneficios a los empleados* (employee-benefit
  provisions) and OTHER provisions (4.11(e)) — the provision recognition
  gate, best-estimate/PV measurement and reimbursement-asset rules are
  owned by `05_liabilities-equity-benefits.md` by id; this FR owns the
  ESF sub-classification classes only.
  (LB-001; EVID-278)
- **SV-COA-FR-033:** The system shall sub-classify equity into *clases
  de patrimonio* (classes of equity) — such as *capital pagado*
  (paid-in capital), *primas de emisión* (share premium), *ganancias
  acumuladas* (retained earnings) and the income and expense items that,
  as permitted or required by the Norma, are recognized in *otro
  resultado integral* (other comprehensive income) and presented
  separately in equity (the closed four-type OCI component set of
  FR-039) — an open ("tales como") list whose SV template ships the
  statutory reserves as NAMED equity classes consumed from the
  commercial-legal wave by id: the Art. 39 *reserva legal* chassis
  (SV-CML-FR-054), its per-type rates and limits (SV-CML-FR-055:
  5%→one-sixth colectiva-family, 7%→one-fifth-floor SRL/S.A./EIRL) and
  its deployment constraints (SV-CML-FR-056) — this file creates the
  equity-class accounts and their 4.12(b) description slots; the reserve
  constitution/restoration mechanics are NEVER restated here (equity
  instrument classification, treasury-share contra-equity treatment and
  the CC 445 revaluation-reserve disambiguation vs the NIIF
  superávit de revaluación are owned by `05_liabilities-equity-benefits.md`
  and consumed from SV-CML-FR-041 by id).
  (LB-001; EVID-278)
- **SV-COA-FR-034:** For every entity with *capital en acciones* (share
  capital), the system shall disclose — in the ESF or the notes — for
  EACH class of share capital: (i) the number of authorized shares
  (*acciones autorizadas*); (ii) the number of shares issued and fully
  paid together with shares issued but not yet fully paid; (iii) the
  *valor nominal* (par value) of the shares or the fact that they have
  no par value; (iv) a reconciliation of the number of *acciones en
  circulación* (shares in circulation) between the beginning and end of
  the period — required for the current period only, not for prior
  periods; (v) the rights, privileges and restrictions attached to each
  class, including restrictions on dividend distribution and on the
  repayment of capital; (vi) shares of the entity held by itself or by
  its subsidiaries or associates (*acciones propias en cartera* —
  treasury holdings); and (vii) shares
  whose issuance is reserved by the existence of options or contracts
  for the sale of shares, describing the conditions and amounts —
  emitted from a share-class register whose rows carry the seven data
  points per class and a circulation-reconciliation movement table
  (issues, treasury movements, cancellations per class).
  (LB-001; EVID-278)
- **SV-COA-FR-035:** The system shall disclose a description of EACH
  *reserva* (reserve) presented in equity (4.12(b)) — each equity-class
  reserve account carrying its description text, the statutory reserves
  referencing their SV-CML-FR-054/055/056 provenance by id — and, for
  entities WITHOUT share capital (such as those responding to a
  *fórmula societaria o fiduciaria* (partnership or fiduciary formula)),
  the EQUIVALENT information to 4.12(a): the changes during the period
  in each equity category and the rights, privileges and restrictions
  associated with each (4.13).
  (LB-001; EVID-278)
- **SV-COA-FR-036:** When at the reporting date the entity has a binding
  sale agreement for a significant disposal of assets, or of a group of
  assets and liabilities, the system shall disclose: (a) a description
  of the assets (or group of assets and liabilities); (b) a description
  of the facts and circumstances of the sale; and (c) the carrying
  amount of the assets (or, for a group, the carrying amounts of those
  assets and liabilities).
  (LB-001; EVID-278)

### 3.3 Income-statement and equity-statement architecture (Secciones 5-6)

- **SV-COA-FR-037:** The system shall implement the ERI minimum-item
  architecture: the statement (single *estado del resultado integral* or
  the two-statement variant consumed from SV-COA-FR-006 by id) presents
  as a minimum the period amounts for: (a) *ingresos de actividades
  ordinarias* (revenue — recognition engine owned by
  `06_revenue.md` by id); (b) *costos financieros* (finance costs); (c)
  the equity-method share of the result of investments in associates and
  jointly controlled entities (measurement owned by
  `07_groups-related-parties.md` by id); (d) *gasto por impuestos* (tax
  expense) EXCLUDING the taxes allocated to items (e), (g) and (h) (the
  allocation and measurement per 29.35 owned by
  `08_deferred-tax-adoption.md` by id); (e) the discontinued-operations
  single amount (FR-041); (f) the result — this line is NOT necessary
  when the entity has no OCI items; (g) each OCI item classified by
  nature, grouped into those that are NOT subsequently reclassified to
  result (types (i), (ii), (iv) of FR-039) and those that ARE
  reclassified when specific conditions are met (type (iii)); (h) the
  share of the OCI of associates and jointly controlled entities
  accounted for under the equity method; and (i) *resultado integral
  total* (total comprehensive income) — which may carry another name
  such as "resultado del período" when the entity has no OCI items; in
  the two-statement variant the *estado de resultados* presents items
  (a)-(f) with the result as the last line and the ERI begins with the
  result followed by items (g)-(i) (5.7); additional items, headings and
  subtotals are presented when relevant to understanding financial
  performance (5.9), under the SV-COA-FR-009 uniformity rules by id.
  (LB-002; EVID-279)
- **SV-COA-FR-038:** The system shall attribute BOTH the result of the
  period AND the total comprehensive income of the period separately to
  (i) *participación no controladora* (non-controlling interests) and
  (ii) the *propietarios de la controladora* (owners of the parent) —
  the attribution lines render from the (q)/(r) equity split of FR-022
  and the consolidation engine that owns NCI measurement
  (`07_groups-related-parties.md` by id).
  (LB-002; EVID-279)
- **SV-COA-FR-039:** The system shall implement the OCI account set as
  a CLOSED four-type list — no OCI account class exists outside: (i)
  some gains and losses arising from the translation of the financial
  statements of a *negocio en el extranjero* (foreign operation —
  Sección 30 mechanics owned by `03_financial-instruments-fx.md` by
  id); (ii) some actuarial gains and losses (Sección 28 policy election
  owned by `05_liabilities-equity-benefits.md` by id); (iii) some
  changes in the fair values of *instrumentos de cobertura* (hedging
  instruments — Part II of Sección 11 owned by
  `03_financial-instruments-fx.md` by id) — the ONLY type grouped as
  subsequently reclassifiable to result; and (iv) changes in the
  *superávit de revaluación* (revaluation surplus) for PPE measured
  under the revaluation model (Sección 17 owned by
  `04_nonfinancial-assets.md` by id) — each type posting to its own
  equity component per FR-033, and the validator rejecting any account
  creation that routes other items into an OCI equity class.
  (LB-002; EVID-279)
- **SV-COA-FR-040:** The system shall NEVER present or describe any
  income or expense item as *partidas extraordinarias* (extraordinary
  items) — not in the ERI, not in a separate *estado de resultados*, not
  in the notes: the label is blocked on account names, report-line
  names and note titles of the statement generator.
  (LB-002; EVID-279)
- **SV-COA-FR-041:** The system shall present the results of
  *operaciones discontinuadas* (discontinued operations) as a SINGLE
  amount comprising the total of: (i) the after-tax result of
  discontinued operations; and (ii) the after-tax gains or losses
  attributable to the impairment, or reversal thereof, of the assets of
  those discontinued operations — at the moment of classification as a
  discontinued operation, subsequently, and on disposal of the net
  assets constituting it (the impairment measurement is Sección 27,
  owned by `04_nonfinancial-assets.md` by id).
  (LB-002; EVID-279)
- **SV-COA-FR-042:** The system shall implement the expense-breakdown
  policy as a company-level election between *naturaleza* (nature) and
  *función* (function) classification, selecting whichever provides
  reliable and more relevant information: under NATURE, expenses are
  aggregated per the expense-account set (depreciation, purchases of
  materials, transport costs, employee benefits, advertising costs
  among others) WITHOUT reallocation among functions; under FUNCTION,
  expenses aggregate as cost of sales and, for example, distribution or
  administration costs — and the FUNCTION election REQUIRES the
  *costo de ventas* (cost of sales) line to be revealed SEPARATELY from
  other expenses — the election is an accounting policy whose change
  follows SV-COA-FR-014 by id (recorded on the policy record with its
  reliable-and-more-relevant basis), and the P&L account template
  carries the dimension (nature groups vs functional lines) the
  election renders.
  (LB-002; EVID-279)
- **SV-COA-FR-043:** The system shall implement the *estado de cambios
  en el patrimonio* with, for each period: (a) the total comprehensive
  income showing SEPARATELY the total amounts attributable to the
  owners of the controladora and to non-controlling interests; (b) for
  EACH component of equity, the effects of retroactive application and
  retroactive re-expression recognized per Sección 10 — the policy-change
  and error-correction posting engines consumed from SV-COA-FR-016 and
  SV-COA-FR-018 by id; and (c) for EACH equity component, a
  reconciliation of the carrying amounts from the beginning to the end
  of the period revealing SEPARATELY the changes resulting from: (i) the
  result of the period; (ii) other comprehensive income; and (iii)
  investments by owners and dividends and other distributions to them
  in their capacity as owners — showing separately share issues,
  treasury-share transactions, dividends and other distributions to
  owners, and changes in ownership interests in subsidiaries that do
  NOT result in loss of control (the NCI-transaction = equity-transaction
  rule consumed from `07_groups-related-parties.md` by id; the
  distribution and dividend mechanics of `05_liabilities-equity-benefits.md`
  by id).
  (LB-003; EVID-279)
- **SV-COA-FR-044:** The system shall implement the combined *estado de
  resultados y ganancias acumuladas* (statement of income and retained
  earnings) variant of 6.4: available only when the ONLY changes in
  equity during the periods presented arise from the result, dividend
  payments, prior-period error corrections and accounting-policy
  changes (the availability gate consumed from SV-COA-FR-006 by id —
  any OCI, reserve constitution or capital movement closes it); when
  used, the statement presents — in addition to the Sección 5
  information — (a) retained earnings at the beginning of the period;
  (b) dividends declared during the period, paid or payable; (c)
  re-expressions of retained earnings for corrections of prior-period
  errors; (d) re-expressions for accounting-policy changes; and (e)
  retained earnings at the end of the period (the posting values from
  SV-COA-FR-016/018 by id).
  (LB-003; EVID-279)
- **SV-COA-FR-045:** The system shall emit the 6.6 notes: (a) the
  amount of dividends proposed (or declared) BEFORE the authorization
  of the FS for issue, not recognized as a distribution to owners for
  the period, together with the per-share amount; and (b) the amount of
  any *dividendo preferente de carácter acumulativo* (cumulative
  preference dividend) not recognized — kept boundary-clean from the
  post-period-end no-liability rule (32.11, owned by
  `07_groups-related-parties.md` by id) and from the CC Arts. 37-38
  distribution ceiling (SV-CML-FR-053 by id — capacity overlay, never
  auto-derived from NIIF equity).
  (LB-003; EVID-279)

### 3.4 Cash-flow-statement architecture (Sección 7)

- **SV-COA-FR-046:** The system shall classify cash flows among the
  three activity classes via a PER-ACCOUNT CFS classification attribute
  — *actividades de operación* (operating: the principal
  revenue-producing activities, generally the transactions entering the
  determination of the result, including receipts from sales of goods
  and services, royalties/fees/commissions, payments to suppliers,
  payments to and on behalf of employees, and income-tax payments
  UNLESS specifically classifiable within investing or financing);
  *actividades de inversión* (investing: acquisition and disposal of
  long-term assets and other investments not classified as cash
  equivalents — PPE/intangible/other LT-asset payments and receipts,
  instrument purchases/sales, advances and loans to third parties and
  their repayments, derivative-contract flows other than
  trading-/financing-classified ones, with acquisitions and sales of
  subsidiaries or other business units presented AGGREGATED and
  separately, as investing); *actividades de financiación* (financing:
  changes in the size and composition of contributed capital and
  borrowings — share-issue receipts, payments to owners to acquire or
  redeem shares, issue receipts and repayments of obligations, loans,
  notes, bonds and mortgages, and lessee payments reducing an
  outstanding finance-lease liability) — with the special rules:
  hedging-contract cash flows classify SAME AS the hedged item; cash
  equivalents are short-term highly-liquid investments readily
  convertible into known amounts with insignificant risk (maturity
  around three months or less from acquisition) held to meet short-term
  commitments; bank overdrafts generally financing-like, but components
  of cash and equivalents when repayable on demand and an integral part
  of cash management.
  (LB-004; EVID-280)
- **SV-COA-FR-047:** The system shall present operating cash flows
  under EITHER method: the *método indirecto* (indirect method) — the
  result adjusted for the effects of (a) period changes in inventories
  and operating receivables and payables; (b) non-cash items such as
  depreciation, provisions, deferred taxes, accrued income/expense not
  yet received or paid in cash, unrealized exchange gains and losses,
  and the share of undistributed profits of associates; and (c) any
  other items whose monetary effects are investing- or
  financing-related — OR the *método directo* (direct method) — the
  principal gross categories of receipts and payments, obtained from
  the accounting records or by adjusting sales, cost of sales and other
  statement items for the same classes of changes; the method is a
  presentation election under the SV-COA-FR-009 uniformity rules by id,
  and investing and financing flows are ALWAYS presented by separate
  principal gross categories under either method.
  (LB-004; EVID-280)
- **SV-COA-FR-048:** The system shall record cash flows arising from
  transactions in foreign currency in the functional currency applying
  to the foreign-currency amount the exchange rate between the two
  currencies ON THE DATE the cash flow occurred (approximation per
  30.19 — rates that approximate the actual — consumed from
  `03_financial-instruments-fx.md` by id), converting a foreign
  subsidiary's flows at the rate on each flow's date; unrealized
  gains and losses from exchange-rate changes are NOT cash flows, but
  to reconcile cash and equivalents at the beginning and end of the
  period the CFS shall present the effect of the exchange-rate
  variation on cash and equivalents held — remeasured at closing rates
  — as a SEPARATE line for the unrealized gain or loss resulting from
  operating, investing and financing flows.
  (LB-004; EVID-280)
- **SV-COA-FR-049:** The system shall implement the interest and
  dividend classification rules as per-company CONFIG with consistency
  enforcement: interest and dividends received and paid are each
  presented SEPARATELY, and each flow classifies consistently from
  period to period as operating, investing or financing — the choices:
  interest PAID, operating (because included in results) or financing
  (cost of obtaining financial resources); interest and dividends
  RECEIVED, operating or investing (returns on investments);
  dividends PAID, financing (cost of obtaining financial resources) or
  operating (paid from operating flows) — a flip of a choice is a
  policy-classification change under the SV-COA-FR-009 uniformity rules
  by id, reclassifying the CFS presentation of that flow line ONLY
  (never the P&L or ESF recognition).
  (LB-004; EVID-280)
- **SV-COA-FR-050:** The system shall present income-tax cash flows
  SEPARATELY and classify them as operating UNLESS they can be
  specifically identified with investing or financing activities; when
  tax flows are distributed among more than one activity class, the
  TOTAL amount of taxes paid is disclosed.
  (LB-004; EVID-280)
- **SV-COA-FR-051:** The system shall EXCLUDE investing and financing
  transactions that do not require the use of cash or cash equivalents
  from the CFS, and DISCLOSE them elsewhere in the FS so that they
  supply all relevant information about those activities — the
  enumerated non-monetary transaction classes: acquisition of assets
  by directly assuming the corresponding financing liabilities or
  through finance-lease operations; purchase of an entity through a
  capital increase; and conversion of debt to equity (posted through
  their asset/liability/equity accounts per files 03-05 by id; the
  disclosure rides the notes builder of SV-COA-FR-019 by id).
  (LB-004; EVID-280)
- **SV-COA-FR-052:** The system shall emit a reconciliation between
  opening and closing ESF balances for the liabilities arising from
  financing activities (liabilities whose cash flows have been or will
  be classified as financing in the CFS), including separately: (a)
  changes from financing cash flows; (b) changes arising from obtaining
  or losing control of subsidiaries or other businesses; (c) the
  effects of exchange-rate variations; (d) fair-value changes; and
  (e) other changes — built from the payable/financing-liability
  accounts tagged with the FR-046 financing attribute plus their
  non-cash movement classes.
  (LB-004; EVID-280)
- **SV-COA-FR-053:** The system shall implement *acuerdos de
  financiación de proveedores* (supplier finance arrangements — 7.19B,
  a THIRD-EDITION paragraph set; see version note §5): arrangements
  where one or more finance providers offer to pay the amounts an
  entity owes its suppliers, the entity undertaking to settle per the
  arrangement's terms on the same date the suppliers are paid or later
  — extended payment terms for the entity or early payment for the
  suppliers relative to the corresponding invoice due date — commonly
  termed *financiación de la cadena de suministro* (supply-chain
  financing), *financiación de cuentas por pagar* (payables financing)
  or *acuerdos de factoraje inverso* (reverse factoring); EXCLUDED:
  arrangements that are solely credit enhancements for the entity
  (financial guarantees, including letters of credit used as such) and
  instruments used to settle directly with a supplier the amounts owed
  (e.g. settling the supplier by credit card with an obligation to the
  issuing bank). The system shall implement: (i) a supplier-finance
  PROGRAM register (finance provider, key terms and conditions:
  interest-rate-related, fees charged, extended payment conditions,
  security or guarantees provided); (ii) per-payable ENROLLMENT
  tagging (which supplier-category payables of FR-031 form part of
  which program, with enrollment windows); and (iii) the AGGREGATE
  disclosure of 7.19C: (a) the key terms and conditions, with
  arrangements having DIFFERENT key terms disclosed separately; (b) at
  the beginning and end of the period, the carrying amounts of the
  financial liabilities forming part of an arrangement AND their
  associated ESF line items, including — unless impracticable, stating
  the fact when not possible — those for which the finance providers
  have already paid the suppliers; (c) the range of payment maturity
  dates for BOTH the arrangement payables and the COMPARABLE trade
  payables not part of an arrangement (comparable = e.g. the entity's
  trade payables in the same line of business or jurisdiction),
  splitting or explaining broad ranges; and the type and effect of
  NON-CASH changes in the disclosed carrying amounts (business
  combinations, exchange differences and other 7.18-type transactions)
  — including the classification effect that settling an enrolled
  payable may classify as a financing outflow with no reported
  financing inflow, surfacing as a non-cash change in
  financing-activity liabilities (feeding FR-052's reconciliation).
  (LB-004; EVID-280)
- **SV-COA-FR-054:** The system shall emit the cash-components and
  restriction notes: (a) the components of cash and cash equivalents
  together with a reconciliation of the CFS amounts to the equivalent
  items presented in the ESF — NOT required when the amount of cash and
  equivalents presented in the CFS is identical to the similarly
  described item in the ESF; and (b) together with management
  commentary, the amount of SIGNIFICANT cash and cash-equivalent
  balances not available for use by the entity — among other reasons,
  foreign-exchange controls or legal restrictions — as a restriction
  flag on cash/equivalent accounts and balances with the restriction's
  nature.
  (LB-004; EVID-280)

## 4. Data Model

Layer semantics: the COA structure is Odoo-native — the account template
(account.account/account.account.type), per-account classification
attributes, company-level presentation config and the report-line
bindings all live in the client (wave default `odoo`; see §5). The model
records the ENTITY's own architecture (classification attributes,
elections, programs); it does not emulate the IASB. No printed data table
in this file warrants a CSV sidecar — the (a)-(r) set and the
sub-classification categories are small config sets shipped as template
rows (default none per plan).

**Account template and classification attributes (account.template →
account.account):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.account | sv_coa_esf_class | select | a_cash · b_receivables · c_fin_assets · d_inventories · e_ppe · ea_inv_prop_cost · f_inv_prop_fv · g_intangibles · h_bio_cost · i_bio_fv · j_associates · k_jce · l_payables · m_fin_liabilities · n_tax_current · o_tax_deferred · p_provisions · q_nci · r_equity_owners | FR-022 |
| account.account | sv_coa_current | select | current · non_current · not_applicable | FR-024-026; o_tax_deferred locked non_current (FR-023) |
| account.account | sv_coa_cfs_class | select | operacion · inversion · financiacion · no_cash_flow (equity/internal) · cash_equivalents | FR-046 |
| account.account | sv_coa_related_party | boolean | related-party AR/AP segmentation flag (account families) | FR-029, FR-031 |
| account.account | sv_coa_inventory_category | select | venta · proceso · materiales (4.11(c)) | FR-030 |
| account.account | sv_coa_payable_category | select | proveedores · partes_relacionadas · ingresos_diferidos · acumulados (4.11(d)) | FR-031 |
| account.account | sv_coa_provision_class | select | beneficios_empleados · otras (4.11(e)) | FR-032 |
| account.account | sv_coa_equity_class | select | capital_pagado · primas_emision · ganancias_acumuladas · oci_conversion · oci_actuarial · oci_cobertura · oci_revaluacion · reserva_legal_statutory (C4 kin SV-CML-FR-054/055 by id) · otras_reservas · propias_en_cartera | FR-033, FR-039 |
| account.account | sv_coa_restricted_cash | boolean + nature | significant balances unavailable (FX controls, legal restrictions) | FR-054 |
| account.move.line | sv_coa_rp_party | related partner flag | counterparty marked related (Sec 33 definition set = 07 by id) feeds 4.11(b)/(d) splits | FR-029, FR-031 |
| account.move.line | sv_coa_supplier_finance_id | m2o l10n_sv_chart.supplier_finance_program | payable enrollment tagging (per-payment windows) | FR-053 |

**Company-level presentation config (res.company):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_coa_liquidity_order | boolean + basis | liquidity-ordering exception election (ALL items, ascending/descending) + relevance basis | FR-024 |
| res.company | sv_coa_operating_cycle_months | int + identifiable flag | cycle length; 12 presumed when not clearly identifiable | FR-025/026 |
| res.company | sv_coa_expense_analysis | select | naturaleza · funcion (function ⇒ separate costo de ventas) | FR-042 |
| res.company | sv_coa_cfs_method | select | indirecto · directo | FR-047 |
| res.company | sv_coa_cfs_interest_paid | select | operacion · financiacion | FR-049 |
| res.company | sv_coa_cfs_int_div_received | select | operacion · inversion | FR-049 |
| res.company | sv_coa_cfs_dividends_paid | select | financiacion · operacion | FR-049 |

**Share-class register and reserves (l10n_sv_chart.share_class /
reserve descriptions):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.share_class | authorized · issued_paid · issued_unpaid | int | per class (4.12(a)(i)/(ii)) | FR-034 |
| l10n_sv_chart.share_class | par_value / no_par | monetary · boolean | valor nominal or no-par fact (iii) | FR-034 |
| l10n_sv_chart.share_class | rights_privileges_restrictions | text | incl. dividend-distribution and capital-repayment restrictions (v) | FR-034 |
| l10n_sv_chart.share_class | treasury_holdings · option_reserved | int + text | entity/subsidiary/associate-held shares (vi); option/contract-reserved with conditions+amounts (vii) | FR-034 |
| l10n_sv_chart.share_reconciliation | clase · opening · movements (issues/treasury/cancellations) · closing | movement rows | acciones en circulación reconciliation — current period only | FR-034 |
| l10n_sv_chart.reserve | account · description · provenance | m2o · text · ref | each equity reserve described (4.12(b)); statutory reserves provenance = SV-CML-FR-054/055/056 by id | FR-035 |
| l10n_sv_chart.equity_category_change | category · change rows · rights | for 4.13 no-share-capital entities | equivalent information | FR-035 |

**Supplier-finance programs (l10n_sv_chart.supplier_finance_program):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.supplier_finance_program | financier · key_terms | m2o res.partner · text | rate-related terms, fees, extended payment conditions, security/guarantees; differing-terms split | FR-053 |
| l10n_sv_chart.supplier_finance_program | excluded_kind | boolean/select guard | credit_enhancement_only · direct_settlement = NOT a program (validation) | FR-053 |
| l10n_sv_chart.supplier_finance_program | disclosure_state | computed | carrying amounts + ESF items at both dates; financier-paid (unless impracticable → state fact); maturity ranges vs comparable payables; non-cash changes | FR-053 |

**Statement-builder surfaces:** ERI/ESF/CFS report-line bindings derive
from sv_coa_esf_class + sv_coa_current (or liquidity order); the
financing-liability reconciliation (FR-052) from the
financiacion-tagged liability accounts + non-cash movement classes; the
6.6 note rows from the dividend surfaces of `05` by id; the
discontinued-operations single amount from the discontinued flag owned
with Sec 27 by `04` by id.

## 5. Odoo Mapping

Layer semantics for this wave: the chart-of-accounts structure is
Odoo-native — account.account/account.account.type template,
account.move.line posting, res.company config and the report layouts —
every FR maps `odoo`; no SaaS rows are introduced because none of these
FRs touch DTE generation/transmission (the only architecture-split
surface per `shared/docs/saas-thin-client-architecture.md` D2). Model
names are stable across Odoo 17/18/19/20; report-line binding builds on
Odoo's financial report layouts (balance sheet / P&L / cash-flow
templates) with the SV template supplying the (a)-(r) line set — layout
gaps carried as OQ-2/OQ-3.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-022 | odoo | account.account + account.account.type + l10n_sv chart template | sv_coa_esf_class; parent classes | (a)-(r) as printed incl. (ea)/(f) and (h)/(i) measurement-split pairs; report-line binding via financial report templates; Odoo generic layouts need extension — OQ-2 |
| FR-023 | odoo | account.account (o_tax_deferred) | sv_coa_current locked | hard validation on write + template constraint; never current |
| FR-024 | odoo | res.company + report layout | sv_coa_liquidity_order + basis | all-or-nothing per statement; election feeds 8.6 judgment slot (SV-COA-FR-021 by id) |
| FR-025 | odoo | account.account + res.company | sv_coa_current; sv_coa_operating_cycle_months | four current-asset tests; 12-month cycle presumption |
| FR-026 | odoo | account.account | sv_coa_current (liabilities) | unconditional-deferral-right test governs |
| FR-027 | odoo | chart template + report config | denominations/order; additional-item assessment record | uniformity via SV-COA-FR-009 by id |
| FR-028 | odoo | account.account (PPE classes) | sv_coa_ppe_class rows | class model/measurement = 04 by id |
| FR-029 | odoo | account.account + account.move.line + res.partner | sv_coa_related_party; sv_coa_rp_party | feeds 4.11(b) split AND Sec 33 builder (07 consumes BY ID) |
| FR-030 | odoo | account.account (inventory) + product.category | sv_coa_inventory_category | costing engines = 04 by id |
| FR-031 | odoo | account.account (payables) | sv_coa_payable_category | four-way split; related-party leg same attribute as FR-029; supplier-finance rides proveedores |
| FR-032 | odoo | account.account (provisions) | sv_coa_provision_class | gate/measurement = 05 by id |
| FR-033 | odoo | account.account (equity) | sv_coa_equity_class | statutory reserves as named classes — SV-CML-FR-054/055/056 by id; OCI components closed set (FR-039) |
| FR-034 | odoo | l10n_sv_chart.share_class + share_reconciliation | seven data points per class + circulation table | current-period-only reconciliation; disclosure in ESF or notes (note_slot of SV-COA-FR-019 by id) |
| FR-035 | odoo | l10n_sv_chart.reserve | description + provenance | 4.13 equivalent-info builder for no-share-capital entities |
| FR-036 | odoo | l10n_sv_chart note/report rows | disposal-agreement disclosure | 4.14 |
| FR-037 | odoo | report layouts (P&L/ERI) | minimum-item lines (a)-(i) | two-statement variant per SV-COA-FR-006 by id; no-OCI renaming |
| FR-038 | odoo | report layouts | NCI/owners attribution lines | NCI measurement = 07 by id |
| FR-039 | odoo | account.account (OCI equity classes) | closed 4-value select | validator blocks other OCI classes; each type's engine = 03/04/05 by id |
| FR-040 | odoo | account.account name + report/note titles | "partidas extraordinarias" label block | hard block on create/write/rename |
| FR-041 | odoo | report layouts + discontinued flag (04 kin) | single-amount line | impairment measurement = 04 by id |
| FR-042 | odoo | res.company + account.account (P&L) + analytic/functional dimension | sv_coa_expense_analysis | function ⇒ mandatory separate costo de ventas line; change = policy change (SV-COA-FR-014 by id) |
| FR-043 | odoo | report layouts (equity statement) | per-component reconciliation columns | Sec 10 events via SV-COA-FR-016/018 by id; NCI transactions = 07 by id |
| FR-044 | odoo | report layouts | combined variant items (a)-(e) | availability gate = SV-COA-FR-006 by id |
| FR-045 | odoo | l10n_sv_chart note rows | proposed dividends + per-share; unrecognized cumulative preference | boundary: 32.11 (07) + SV-CML-FR-053 by id |
| FR-046 | odoo | account.account | sv_coa_cfs_class | three classes + special rules (overdrafts, hedging, subsidiary aggregations); CFS layout gaps — OQ-3 |
| FR-047 | odoo | res.company + CFS report | sv_coa_cfs_method | indirect reconciliators / direct gross categories; uniformity via SV-COA-FR-009 by id |
| FR-048 | odoo | account.move.line (cash journals) + CFS report | flow-date rate conversion; separate FX-effect line | 30.19 approximation + FX engines = 03 by id; 7.12A line needs layout support — OQ-3 |
| FR-049 | odoo | res.company + CFS report | sv_coa_cfs_interest_paid / int_div_received / dividends_paid | choices as config; flip reclassifies CFS line only |
| FR-050 | odoo | account.account (tax) + CFS report | separate income-tax flow lines | total-paid disclosure when split |
| FR-051 | odoo | account.move (non-monetary flag) + notes | excluded-but-disclosed transactions | posts via 03-05 engines by id; note slot SV-COA-FR-019 by id |
| FR-052 | odoo | CFS report builder | financing-liability reconciliation table | from financiacion-tagged accounts + non-cash classes; layout gap — OQ-3 |
| FR-053 | odoo | l10n_sv_chart.supplier_finance_program + account.move.line | program register + enrollment tagging + 7.19C block | NEW 3rd-ed. paragraph set — version note below; disclosure block needs layout support — OQ-3 |
| FR-054 | odoo | account.account (cash) + CFS report + notes | sv_coa_restricted_cash; components reconciliation | reconciliation waivable when identical |

Version-regime notes (D12/D15): the NIIF edition is a DATED regime row —
3rd edition (Feb-2025) applies to annual periods beginning 2027-01-01,
early adoption permitted (A1); the edition flag and Tabla A1 delta map
are owned by `08_deferred-tax-adoption.md` by id. Edition-sensitive
content in THIS file: **7.19B-C supplier finance is a THIRD-EDITION
addition (EVID-280 marks it NEW 3rd ed.)** — FR-053's disclosure block
applies to 3rd-edition reporters only; 2nd-edition (2015) regime rows
carry it switched off pending the Tabla A1 mapping. All other Sección
4-7 rules encoded here are edition-stable in the corpus (no 2nd-vs-3rd
divergence evidenced for them). D15 anchors: classification attributes
and presentation elections resolve as-of their election dates and
snapshot on the record (policy-class changes via SV-COA-FR-014 by id);
supplier-finance enrollments resolve per payment window. Mid-year
go-live (D18): migrating classification attributes ingest with the
accounts they describe (is_historical ingestion semantics owned by T8's
Sec 35 surface by id). No hard gates beyond FR-023 (deferred tax never
current) and FR-040 (no extraordinary items) — both D16 no-override
blocks, never disabled by configuration.

## 6. Acceptance Criteria

- **AC-001:** Given an account whose parent class is (o) deferred tax,
  when any user or template process attempts to set its
  current/non-current attribute to current, then the write is rejected
  by the FR-023 validator and the account renders in the non-current
  section of every ESF layout, under both the default and the
  liquidity-ordering presentation (FR-023).
- **AC-002:** Given a company with sv_coa_cfs_interest_paid =
  financiacion, when the config flips to operacion, then the interest-
  paid amount moves between CFS activity sections in the NEXT generated
  statement only — no P&L account, no ESF classification and no prior-
  period CFS is touched, and the flip records as a presentation-
  classification change under the uniformity rules (FR-049).
- **AC-003:** Given a supplier payable enrolled in a supplier-finance
  program (financier-paid, 60-day extended terms), when the period
  closes, then the 7.19C disclosure block surfaces: key terms,
  carrying amounts at both dates with their ESF line items, the
  financier-paid amounts, maturity ranges for program payables AND
  comparable non-program trade payables, and the non-cash change
  feeding the financing-liability reconciliation — and a
  credit-enhancement-only guarantee flagged as a program is rejected
  by the excluded_kind guard (FR-053, FR-052).
- **AC-004:** Given a bank-like entity electing the liquidity-ordering
  exception with a recorded reliable-and-more-relevant basis, when the
  ESF renders, then ALL assets and liabilities present in approximate
  liquidity order — no current/non-current headings survive — and the
  election appears in the 8.6 judgments note slot (FR-024).
- **AC-005:** Given receivables from a related-party counterparty and
  from ordinary customers posted to the segmented AR families, when the
  ESF/notes render, then the 4.11(b) split shows the two amounts
  separately from the SAME line-level segmentation that
  `07_groups-related-parties.md` consumes by id for its Sección 33
  disclosures — one attribute, two consumers, zero re-derivation
  (FR-029).
- **AC-006:** Given sv_coa_expense_analysis = funcion, when the P&L
  renders, then a separate *costo de ventas* line appears before other
  functional groupings; when the election is naturaleza, then expenses
  group by nature with no functional reallocation — and switching the
  election records as a policy change under SV-COA-FR-014 by id
  (FR-042).
- **AC-007:** Given a period with a PPE revaluation surplus (OCI type
  iv), an actuarial gain (type ii) and a translation difference (type
  i), when the equity statement renders, then EACH equity component
  reconciles opening-to-closing showing result, OCI and
  investments/distributions separately — the OCI movements landing only
  in the three closed-list components, never in a fifth class
  (FR-043, FR-039).
- **AC-008:** Given a machine acquired under a finance lease (a
  non-monetary investing/financing transaction), when the CFS renders,
  then no flow line appears for the acquisition, and the notes disclose
  the transaction — while the lease's subsequent principal payments
  render as financing outflows (FR-051, FR-046).
- **AC-009:** Given USD cash in a foreign account subject to an exchange
  control making part of the balance unavailable, when the CFS notes
  render, then the significant unavailable amount appears with
  management commentary and the FX-effect-on-cash line reconciles cash
  at closing rates separately from operating, investing and financing
  flows (FR-054, FR-048).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-46 carried: the SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is NOT in the corpus — the statement architecture of this file attaches to the informational framework flag of SV-COA-FR-001 (SOQ-53) with NO invented SV presentation overlays and no compliance gate; who must run the PYMES engine remains external dated law (32_ Prólogo P12 leaves it to jurisdictions). Acquisition candidate ≥75 (same instrument as commercial-legal/03 OQ-002). | no | Takumi S8 (sources watch) | open |
| OQ-2 | Odoo report-layout gap (balance sheet/P&L): whether Odoo's generic financial-report layouts can express the full (a)-(r) binding without custom sections — specifically the (ea)/(f) investment-property measurement-split pair, the (h)/(i) biological-assets pair, the (q) NCI vs (r) owners' equity attribution lines within the equity section, and the 5.5 discontinued single-amount line — needs an implementation-time layout inventory; current design assumes an l10n_sv report template extension over account.financial.html.report. | no | Takumi S8 (implementation design) | open |
| OQ-3 | Odoo report-layout gap (cash-flow statement + reconciliations): the CFS surfaces beyond per-account classification — the 7.12A separate unrealized-FX-effect-on-cash line, the 7.19A financing-liability opening-to-closing reconciliation table (five change types), the 7.19B-C supplier-finance disclosure block (third-edition rows) and the 7.20-7.21 components/restricted-cash notes — are not native Odoo cash-flow layout objects; implementation needs custom report sections fed by the sv_coa_cfs_class and supplier-finance tagging model of §4. | no | Takumi S8 (implementation design) | open |
