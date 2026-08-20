# SV — Chart of accounts — Financial instruments & FX: classification, amortized cost/EIR, incurred-loss impairment, derecognition, disclosures, Part II FV + narrow hedging, fair-value engine, foreign-currency translation

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file owns cluster N3 — the financial-instrument and FX engine of the
*Norma de Contabilidad NIIF para las PYMES* (Accounting Standard for SMEs,
32_): Part I basic-instrument classification (the 11.8 basic set with the
11.9/11.9ZA debt conditions and the 11.11A no-reclassification rule,
surfaced as account-level classification flags); initial measurement
(transaction price; trade receivables per Sección 23; financing
transactions at present value at the market rate — the partner/shareholder
loan rule) and subsequent measurement (amortized cost + *interés efectivo*
(effective interest) engine with the Norma's worked-example schedule
pattern; equities at fair value if reliably measurable without
disproportionate cost, else cost − impairment); the INCURRED-loss
impairment model (objective evidence, individual vs grouped, PV at the
original effective rate, capped reversal — explicitly NOT expected credit
loss); derecognition (risks-and-rewards, retained asset + liability,
substantial modification = extinguish + new); the Sección 11 disclosure
set (category balances, receivable aging + liability maturity bands,
pledged collateral, defaults); Part II (fair-value-through-P&L default,
the unquoted-equity cost fallback with last-reliable-FV-becomes-cost, and
the narrow config-gated hedging of 11.60-11.71); the reusable
fair-value-measurement engine of Sección 12 (exit price, principal/most
advantageous market, highest and best use, three approaches, Level 1/2/3
hierarchy, disclosure set); and the FX discipline of Sección 30 +
Apéndice 30A (functional currency and its prospective change,
transaction-date spot with average-rate relief, prepaid consideration at
the prepayment-date rate, closing-rate monetary vs cost/FV-date
non-monetary, P&L routing with net-investment OCI, presentation-currency
translation with never-recycled OCI, convertibility framework) plus the
Sección 31 hyperinflation config-off guard for USD-functional SV entities.

It does **not** cover: the framework/eligibility chassis and policy-event
model (`01_framework-policies.md`, consumed by id — the
disproportionate-cost registry FR-012 is this file's relief feed); the
ESF/P&L report lines and account architecture (`02_coa-structure.md`);
non-financial assets (`04_nonfinancial-assets.md` — they CONSUME this
file's fair-value engine by id); liabilities, equity and employee
benefits (`05_liabilities-equity-benefits.md`); revenue and Sección 23
receivables (`06_revenue.md` — the 11.13A/23.38 interplay is consumed by
id); consolidation and foreign-operation translation application surfaces
(`07_groups-related-parties.md` — 30.21-30.23 consolidation mechanics are
owned there); deferred tax, first-time adoption and edition versioning
(`08_deferred-tax-adoption.md`). Fiscal computations (ISR/IVA/payroll/
special regimes) are owned by their waves by FR id — this wave owns the
ACCOUNTING book only. The two-clock invariant (binding): CT Art. 62
governs the TAX base conversion only and is never re-derived here;
book-vs-fiscal differences (FX clocks, partner-loan deemed dividends)
route through N8's deferred-tax FRs (`08_deferred-tax-adoption.md` by
filename — no FR ids exist yet) and are never conflated.

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling
R29): the operative framework LB = **32_** — *Norma de Contabilidad NIIF
para las PYMES, TERCERA EDICIÓN (Febrero 2025)*, IFRS Foundation official
Spanish translation, Sections 1-35 + Apéndice A + Apéndice B; effective
2027-01-01 with early adoption permitted (A1), cited by section/párrafo
as printed. In this file 32_ is cited at Secciones 11, 12, 30 + Apéndice
30A and Sección 31. **33_** (EY *Guía Práctica de NIIF y Sostenibilidad
2024/2025*) is SECONDARY-ONLY authority per R29(a): it can NEVER be the
sole LB of an FR; its LB role here is limited to documented
full-NIIF-vs-PYMES contrasts — chiefly the ECL contrast (full NIIF
expected-credit-loss impairment vs the PYMES incurred-loss model of
11.21-11.26) and the hedge-accounting divergence (IFRS 9's broad
hedge model vs the narrow swap/forward-only model of 11.60-11.71) —
cited as contrasts only, with every FR's LB staying 32_; where 33_ and
32_ could diverge, 32_ governs without exception.

**SOQ-46 instrument-gap note (rides every FR in this file and this
wave):** the Norma itself is jurisdiction-neutral on who applies it —
"Las decisiones sobre qué entidades están requeridas o autorizadas a
utilizar las Normas NIIF de Contabilidad completas o la Norma de
Contabilidad NIIF para las PYMES recaen en las autoridades legislativas y
regulatorias y en los emisores de normas de las distintas
jurisdicciones" (Prólogo P12) — and the SV adopting instrument (Consejo
de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is
NOT in the corpus (commercial-legal/03 OQ-002 tracks the same
acquisition). Nothing in this file invents SV thresholds or SV-specific
instruments, markets or rates: the classification, measurement, FV and FX
machinery encodes the Norma as printed, and every jurisdictional
parameter (functional currency, markets, rate feeds) is company config.

**Two-clock spine (this file's most-loaded invariant):** (i) FX — the
book engine of Sección 30 (transaction-date spot, closing-rate
remeasurement to P&L/OCI) NEVER computes the fiscal conversion: CT Art.
62 governs the TAX base only, consumed BY ID as SV-TAX-FR-020
(`sv/requirements/taxation/01_isr-framework.md`: foreign-currency tax
bases converted to USD at the exchange rate of the day the taxable
event (*hecho generador*) occurred; exchange differences between that
date and payment of the tax NEVER enter the tax base; installment-sale
FX differences between contract date and payment of the balance or
installments SHALL be added to the base) — with the fiscal clock's
operational rate feed tracked at `sv/requirements/taxation/00_index.md`
OQ-006; book-vs-fiscal FX differences route to
`08_deferred-tax-adoption.md` (T8) by filename.
(ii) Partner/shareholder loans — the 11.13B book rule (present value at
market rate + implicit interest) coexists with the fiscal deemed-dividend
regime (Ley ISR Arts. 25 and 74-A — `sv/requirements/taxation/
05_isr-distributions.md` LB-004/LB-007), consumed by id, never overridden
and never re-derived here.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 11 Parte I (clasificación): 11.8: instrumentos financieros básicos: "(a) efectivo; (b) un instrumento de deuda (como una cuenta, pagaré o préstamo por cobrar o pagar) que cumpla las condiciones del párrafo 11.9 o el párrafo 11.9ZA; (c) un compromiso de recibir un préstamo que: (i) no pueda liquidarse por el importe neto en efectivo; y (ii) cuando se ejecute el compromiso, se espera que cumpla las condiciones del párrafo 11.9. (d) una inversión en acciones preferentes no convertibles y acciones ordinarias o preferentes sin opción." 11.9 conditions (a)-(d): rendimientos "bien: (i) un importe fijo; (ii) una tasa fija de rendimiento…; (iii) un rendimiento variable que a lo largo de la vida del instrumento, se iguala a la aplicación de una referencia única cotizada o una tasa de interés observable…; o (iv) alguna combinación de dichas tasas fijas y variables siempre que tanto la tasa fija como la variable sean positivas"; (b) "No hay cláusulas contractuales que, por sus condiciones, pudieran dar lugar a que el tenedor… pierda el importe principal y cualquier interés atribuible…"; subordinación no es tal cláusula; "Una parte puede pagar o recibir una compensación razonable a la terminación anticipada…"; (c) cláusulas de pago anticipado/reembolso "no están supeditadas a sucesos futuros distintos de los de proteger" al tenedor (riesgo crediticio del emisor, cambio de control) "o… cambios legales o fiscales relevantes"; (d) "No existe un rendimiento condicional o una cláusula de reembolso excepto para el rendimiento de tasa variable descrito en (a) y para la cláusula de pago anticipado descrita en (c)." 11.9ZA fallback: deuda que no cumple 11.9(a)-(d) queda en Parte I si las condiciones contractuales "dan lugar, en fechas determinadas, a flujos de efectivo que son únicamente pagos de principal e intereses sobre el importe principal pendiente"; el "interés" incluye "una compensación razonable por el valor temporal del dinero, el riesgo de crédito y otros riesgos y costos básicos de los préstamos… congruentes con un acuerdo básico de préstamo"; instrumentos con exposición a riesgos no relacionados o a la volatilidad "es poco probable" que cumplan. 11.9A/11.9B ejemplos (préstamo fijo→variable, SONIA+200pb; cuentas de origen comercial; cuentas por pagar en moneda extranjera; préstamos a/de subsidiarias pagaderos a requerimiento; permutas/contratos a plazo/NO — quedan en Parte II). 11.10: no satisfacen (→ Parte II): inversiones en patrimonio distintas de 11.8(d), permutas financieras de tasas, contratos a plazo liquidables en efectivo, opciones y futuros. 11.11A: "Después del reconocimiento inicial, una entidad NO reclasificará los activos o pasivos financieros dentro o fuera de la Parte I de la Sección 11" (citado por EVID-284). | Basic financial instruments: cash; debt instruments (account, note, loan receivable/payable) meeting the 11.9 or 11.9ZA conditions; loan commitments not net-cash-settleable expected to meet 11.9 when exercised; non-convertible preference shares and ordinary or preference shares without put option. 11.9 conditions: returns fixed, fixed-rate, single observable-reference variable, or positive fixed+variable combination; no contractual clause that could cause holder loss of principal or accrued interest (subordination not such a clause; reasonable early-termination compensation permitted); prepayment/demand clauses conditioned only on protective events (credit-risk/control changes, relevant legal/fiscal changes); no contingent return or redemption beyond (a) variable rate and (c) prepayment. 11.9ZA: debt whose contractual cash flows on specified dates are solely principal and interest on outstanding principal is Part I anyway (interest includes compensation for time value, credit risk and other basic lending risks/costs); instruments exposing to unrelated risks or volatility unlikely to qualify. 11.10 examples route swaps, forwards, options, futures and non-11.8(d) equity to Part II. 11.11A: NO reclassification into or out of Part I after initial recognition | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 11 Parte I, párrs. 11.7A-11.11A esp. 11.8-11.10 (txt PAGE 91-96) (EVID-284) |
| LB-002 | Norma NIIF para las PYMES, Sección 11 Parte I (medición): 11.13: medición inicial al precio de transacción, "excepto si: (a) el activo financiero es una cuenta por cobrar (véase el párrafo 11.13A); o (b) el acuerdo constituye, en efecto, una transacción de financiación para la entidad (para un pasivo financiero) o la contraparte (para un activo financiero) del acuerdo (véase el párrafo 11.13B)". 11.13A: "Una cuenta por cobrar comercial se reconocerá inicialmente por el importe determinado por la aplicación de la Sección 23, a menos que el acuerdo constituya, en efecto, una transacción de financiación y la entidad no aplique la opción del párrafo 23.38." 11.13B: "Un acuerdo constituye una transacción de financiación si el pago se aplaza más allá de los términos comerciales normales… o se financia a una tasa de interés que no es una tasa de mercado, por ejemplo, un préstamo sin interés o a una tasa de interés por debajo del mercado… la entidad medirá el activo financiero o pasivo financiero al valor presente de los pagos futuros, descontados a una tasa de interés de mercado para un instrumento de deuda similar determinado en el reconocimiento inicial." 11.14 medición posterior (sin deducir costos de disposición): (a) deuda Parte I al costo amortizado con el método del interés efectivo; los clasificados como corrientes "se medirán al importe no descontado del efectivo u otra contraprestación que se espera pagar o recibir… neto del deterioro" salvo transacción de financiación; (b) compromisos de préstamo al costo (a veces cero) menos deterioro; (c) acciones sin opción: "(i) si las acciones cotizan en bolsa o su valor razonable se puede medir de otra forma con fiabilidad sin esfuerzo o costo desproporcionado… al valor razonable con cambios… en el resultado del periodo; y (ii) todas las demás… al costo menos el deterioro." Dividendos solo cuando "(a) se establezca el derecho…; (b) sea probable…; y (c) el importe… pueda ser medido de forma fiable." 11.15 costo amortizado = inicial "menos reembolsos del principal; más o menos la amortización acumulada utilizando el método del interés efectivo…; menos… cualquier reducción… por deterioro". 11.16-11.18 EIR: tasa que descuenta flujos estimados al importe en libros inicial; gasto/ingreso por intereses = importe en libros inicial del periodo × EIR; la EIR considera condiciones contractuales "y pérdidas crediticias conocidas en las que se haya incurrido, pero no tendrá en cuenta las posibles pérdidas crediticias esperadas futuras en las que no se haya incurrido todavía"; comisiones, cargas financieras ("puntos"), costos de transacción y primas/descuentos se amortizan a lo largo de la vida esperada (periodo más corto hasta la revisión si se ajustan a mercado); tasa variable → reestimación altera la EIR. 11.19-11.20 revisión de estimaciones → recomputar al valor presente con la EIR ORIGINAL, ajuste a resultados en la fecha de la revisión. Ejemplo impreso: bono 5 años adquirido por 900 u.m. + 50 costos = 950; cupón 40; rescate 1.100; EIR 6,9584%; tabla importe inicial → interés EIR → efectivo → importe final (950,00→66,11→(40,00)→976,11 → … → 1.100,00). | Initial measurement at transaction price except (a) receivables per 11.13A/Sección 23 and (b) financing transactions per 11.13B at PV of future payments discounted at the market rate for similar debt at initial recognition (interest-free/below-market loans — the partner/shareholder-loan kin). Subsequent: amortized cost + EIR for Part I debt (current-classified at undiscounted net of impairment unless financing); loan commitments at cost − impairment; non-put equities FV-through-P&L if reliably measurable without disproportionate cost else cost − impairment; dividends on right-established + probable + reliably measurable. Amortized cost build (initial − principal ± accumulated EIR amortization − impairment); EIR determined on initial carrying amount, considering contractual terms and INCURRED credit losses only (never not-yet-incurred expected losses); fees/points/transaction costs amortized over expected life (to next reset if market-aligned); variable-rate re-estimation. Estimate revisions recompute at the ORIGINAL EIR with P&L adjustment at revision date. Printed worked example: 5-year bond 950 net initial, 40 coupon, 1,100 redemption, EIR 6.9584%, roll-forward table to maturity | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 11 Parte I, párrs. 11.13-11.20 con ejemplo (txt PAGE 96-99) (EVID-284) |
| LB-003 | Norma NIIF para las PYMES, Sección 11 Parte I (deterioro + baja en cuentas): 11.21: al final de cada periodo evaluar evidencia objetiva de deterioro de activos medidos al costo o costo amortizado; con evidencia objetiva, "reconocerá inmediatamente una pérdida por deterioro del valor en resultados". 11.22 evidencia objetiva (sucesos observables que causan la pérdida): "(a) dificultades financieras significativas del emisor o del obligado; (b) infracciones del contrato, tales como incumplimientos o moras…; (c) el acreedor, por razones económicas o legales relacionadas con dificultades financieras del deudor, otorga… concesiones…; (d) pase a ser probable que el deudor entre en quiebra…; o (e) los datos observables que indican que ha habido una disminución medible en los flujos futuros de efectivo estimados de un grupo de activos financieros desde su reconocimiento inicial, aunque la disminución no pueda todavía identificarse con activos financieros individuales…"; otros factores (cambios adversos tecnológicos/mercado/económicos/legales). 11.23: patrimonio SIEMPRE individual; otros activos individualmente si significativos; resto individual o AGRUPADOS por características de riesgo crediticio similares. 11.24 medición: costo amortizado → pérdida = importe en libros − valor presente de flujos futuros estimados descontados a la EIR ORIGINAL (tasa variable → EIR actual según contrato); costo − deterioro → "la mejor estimación (que necesariamente tendrá que ser una aproximación) del importe… que la entidad recibiría por el activo si se vendiera en la fecha sobre la que se informa" (podría ser cero). 11.26 reversión: si la pérdida disminuye y "puede relacionarse objetivamente con un hecho ocurrido con posterioridad" (mejora calificación crediticia), revertir "ya sea directamente o mediante el ajuste de una cuenta correctora. La reversión no dará lugar a un importe en libros… que exceda al importe en libros que habría tenido si anteriormente no se hubiese reconocido la pérdida… reconocerá el importe de la reversión en los resultados inmediatamente." 11.33-11.35 baja de activos: solo cuando "(a) expiren o se liquiden los derechos contractuales…; (b) la entidad transfiera sustancialmente a terceros todos los riesgos y recompensas…; o (c)… a pesar de haber conservado algunos riesgos y ventajas… significativos, ha transferido el control… y éste tiene la capacidad práctica de vender el activo en su integridad… y… sin… restricciones adicionales" → baja + reconocimiento SEPARADO de derechos/obligaciones conservados o creados; distribución del importe en libros por valores razonables relativos; diferencia a resultados; transferencia fallida (riesgos significativos conservados) → "continuará reconociendo el activo transferido en su integridad, y reconocerá un pasivo financiero por la contraprestación recibida. El activo y pasivo no deberá compensarse"; garantías no monetarias (derecho de vender/repignorar → reclasificación separada; incumplimiento → baja/reconocimiento). 11.37 baja de pasivos: solo cuando extinguido — "pagada, cancelada o haya expirado"; intercambio de instrumentos "con condiciones sustancialmente diferentes" = cancelación del original + reconocimiento de uno nuevo; "una modificación sustancial de las condiciones de un pasivo financiero existente… (sea atribuible o no a las dificultades financieras del deudor)" = cancelación + nuevo. 11.38: diferencia entre importe en libros y contraprestación (incl. activos no monetarios/pasivos asumidos) → resultados. | Impairment (incurred-loss): period-end assessment for objective evidence only; immediate P&L loss when evidenced. Objective-evidence events: significant financial difficulty; contractual breach (default/mora on interest or principal); creditor concessions linked to difficulty; probable bankruptcy/reorganization; measurable decrease in a GROUP's estimated future cash flows since initial recognition (adverse national/local/sector conditions) though not yet identifiable with individual assets; other adverse environment changes. Equities always assessed individually; individually-significant others individually; remainder individually or grouped by similar credit-risk characteristics. Measurement: amortized-cost assets = carrying minus PV of estimated future cash flows at the ORIGINAL EIR (variable-rate: current contractual EIR); cost-measured assets = best estimate (necessarily approximate) of sale proceeds at reporting date (may be zero). Reversal only when objectively linked to a post-impairment event; via direct write-down or allowance; capped at the carrying amount that would have existed had no impairment been recognized; immediate to P&L. Derecognition: rights expire/settle; substantially all risks and rewards transferred; or control transferred with practical unrestricted sale ability → derecognize and separately recognize retained/created rights and obligations (relative-FV allocation, difference to P&L); failed transfer → keep the asset in full + financial liability for the consideration, no offsetting; non-cash collateral rules. Liability derecognition only on extinguishment; substantially-different exchange or substantial modification (whatever the cause) = extinguish original + recognize new; difference to P&L | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 11 Parte I, párrs. 11.21-11.26 y 11.33-11.38 con ejemplos (txt PAGE 98-103) (EVID-284) |
| LB-004 | Norma NIIF para las PYMES, Sección 11 (información a revelar + Parte II): 11.39-11.40 política de medición por 8.5; 11.41 categorías ESF: "(a) activos financieros medidos al valor razonable con cambios en resultados…; (b)… deuda medidos al costo amortizado; (c)… patrimonio medidos al costo menos deterioro…; (d) pasivos financieros medidos al valor razonable…; (e) pasivos financieros medidos al costo amortizado; y (f) compromisos de préstamo medidos al costo menos deterioro"; 11.42 plazos y condiciones (tasa, vencimiento, reembolso, restricciones). 11.43 análisis de antigüedad "por referencia a la fecha de vencimiento, de las cuentas por cobrar comerciales y otros activos financieros medidos al costo amortizado… mostrando por separado: (a) el costo amortizado… antes de ajustar cualquier reducción… por deterioro…; y (b) cualquier reducción… por deterioro"; 11.43A "análisis de vencimiento para los pasivos financieros por categoría… vencimientos contractuales restantes… flujos de efectivo contractuales no descontados"; 11.43B intervalos de ejemplo: "(a) hasta un mes; (b) más de un mes y no más de tres meses; (c) más de tres meses y no más de un año; (d) a más de un año y no más de cinco años; y (e) más de cinco años"; 11.44 FV no disponible sin costo desproporcionado → revelar hecho + importe + razones. 11.45 transferidos sin baja: naturaleza, riesgos conservados, importes; 11.46 garantía: "(a) el importe en libros de los activos financieros pignorados como garantía; y (b) los plazos y condiciones relacionados con su pignoración"; 11.47 incumplimientos: "(a) detalles…; (b) el importe en libros de los préstamos por pagar…; y (c) si… ha sido corregido o… renegociado… antes de la fecha de autorización"; 11.48 partidas de ingresos/gastos/ganancias/pérdidas incl. "ingresos por intereses totales y los gastos por intereses totales (calculados utilizando el método del interés efectivo)… y (c) el importe de las pérdidas por deterioro… para cada clase". Parte II: 11.52 reconocimiento al ser parte; 11.53 medición inicial al valor razonable "que es normalmente el precio de transacción"; 11.54 medición posterior: "medirá todos los instrumentos… al valor razonable y reconocerá los cambios… en el resultado del periodo, excepto…: (a) [coberturas → OCI per 11.69]; y (b) instrumentos de patrimonio sin cotización pública y cuyo valor razonable no pueda medirse… sin esfuerzo o costo desproporcionado…, los cuales deberán medirse al costo menos deterioros de valor"; 11.56: "su valor razonable en la última fecha en la que se midió el instrumento con fiabilidad… se tratará como el costo del instrumento… hasta que sea capaz de determinar una medida fiable…"; 11.57 Sección 12 aplica; 11.58 pasivo exigible a la vista ≥ importe pagadero a la vista descontado. Coberturas 11.60-11.71: 11.62 condiciones (designar y documentar; riesgo de 11.63; instrumento de 11.64; "altamente efectivo"); 11.63 riesgos: "(a) riesgo de tasa de interés de un instrumento de deuda medido a su costo amortizado; (b) riesgo de tasa de cambio en moneda extranjera o de tasa de interés en un compromiso firme o en una transacción prevista altamente probable; (c) riesgo de precio de una materia prima cotizada…; y (d) riesgo de tasa de cambio de la moneda extranjera en una inversión neta en un negocio en el extranjero"; 11.64 instrumento de cobertura: "(a) es una permuta de tasa de interés, una permuta financiera de diferencias de cambio, contrato de intercambio a término de moneda extranjera o un contrato a término de cambio de materia prima cotizada…; (b) involucra una parte externa…; (c) su importe nocional es igual al importe designado…; (d) tiene una fecha de vencimiento especificada no posterior a [vencimiento/liquidación/ocurrencia]; (e) no tiene pago anticipado, terminación anticipada o características ampliadas"; 11.65-11.66 cobertura FV (tasa fija/materia prima posesión): FV del instrumento a resultados + ajuste al importe en libros de la partida cubierta; liquidaciones netas a resultados al devengar; 11.67 interrupción (expira/vende/cesa condiciones/revocación); 11.68 ajustes residuales se amortizan al interés efectivo; 11.69 cobertura de flujos (tasa variable, moneda/materia prima en compromiso/prevista, inversión neta): "reconocer en otro resultado integral la parte del cambio… que fue eficaz… reconocerá en el resultado… cualquier exceso… (ineficacia de cobertura)… se reclasificará en resultados cuando la partida cubierta se reconozca en el resultado… el importe acumulado… relacionado con una cobertura de una inversión neta… no se reclasificará… en el momento de la disposición o disposición parcial". | Disclosures: measurement-basis policy (8.5); ESF category balances six ways (FV-P&L assets; amortized-cost debt assets; cost−impairment equity assets; FV-P&L liabilities; amortized-cost liabilities; cost−impairment loan commitments); debt terms and conditions. Receivable aging by due date for trade receivables and amortized-cost financial assets showing amortized cost before vs impairment reduction separately; liability maturity analysis by category with remaining contractual maturities on UNDISCOUNTED contractual cash flows; illustrative time bands ≤1m, >1m-3m, >3m-1y, >1y-5y, >5y; FV-unavailable/disproportionate-cost fact + carrying + reasons; transferred-not-derecognized nature/risks/amounts; pledged financial assets carrying + pledge terms; unsolved loan-payable breaches: details, carrying, cured/renegotiated status; income/expense/gains/losses incl. total interest income/expense at EIR and impairment losses per class. Part II: recognize when party to terms; initial at FV (normally transaction price); subsequent FV with changes in P&L for ALL except hedge-instrument OCI portions and unquoted equity not reliably measurable without disproportionate cost (cost − impairment); last reliable FV becomes the cost until reliable measurement returns; Sección 12 governs FV; on-demand liability FV floor. Hedging: documented designation; only the four 11.63 risks; only interest-rate swaps, FX swaps, exchange forwards, commodity forwards from external counterparties, notional match, specified maturity not later than the hedged item, no prepayment/early-termination/extension features, high expected effectiveness; FV hedges adjust carrying + P&L; CF-type hedges route effective portion to OCI with ineffectiveness to P&L and reclassification when the hedged item hits P&L — net-investment amounts never recycled | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 11, párrs. 11.39-11.48 y Parte II 11.49-11.71 (txt PAGE 103-114) (EVID-284) |
| LB-005 | Norma NIIF para las PYMES, Sección 12 (valor razonable): 12.2: FV = "el precio que se recibiría por vender un activo o que se pagaría por transferir un pasivo en una transacción ordenada entre participantes de mercado, en la fecha de la medición" (medición basada en el mercado, no específica de la entidad). 12.4-12.7 mercado principal (mayor volumen y nivel de actividad) o, en su defecto, mercado más ventajoso; la entidad debe tener acceso; "Un precio de transacción es el precio pagado para adquirir el activo o recibido para emitir el pasivo… y representa un precio de entrada"; los costos de transacción NO se deducen (no son parte del precio); los costos de transporte se ajustan si la ubicación es una característica. 12.8-12.12 máximo y mejor uso para activos no financieros: físicamente posible, legalmente permitido y financieramente factible; presunción del uso actual salvo evidencia contraria. 12.14-12.16 técnicas: enfoques de mercado, costo e ingreso (valor presente, modelos de opciones, superávit de ganancias multiperiodo); cambio de técnica = cambio de estimación. 12.22-12.27 jerarquía: Nivel 1 precios cotizados (mercados activos, partidas idénticas); Nivel 2 datos distintos de Nivel 1 observables (partidas similares cotizadas, cotizadas en mercados no activos, tasas/curvas, corroborados); Nivel 3 no observables (datos de la entidad ajustados a supuestos de participantes de mercado); "la medición completa se clasificará en el nivel más bajo de entre los datos significativos de la medición completa". 12.28-12.32 revelaciones por clase: importe en libros, nivel, técnica + datos; Nivel 3 recurrente: ubicación en resultados/OCI de ganancias/pérdidas, conciliación con las partidas del estado, forma tabular cuantitativa. | Fair value = exit price — the price received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date (market-based, not entity-specific). Principal market (greatest volume/activity) else most-advantageous; entity access required; transaction costs not deducted (entry vs exit price); transport costs adjust when location is a characteristic. Highest and best use for non-financial assets (physically possible, legally permissible, financially feasible; current use presumed). Market/cost/income approaches; technique change = estimate change. Hierarchy: L1 quoted-identical-active; L2 other-observable; L3 unobservable (entity data adjusted for market-participant assumptions); the WHOLE measurement classified at the lowest level among its significant inputs. Class-level disclosures: carrying, level, technique + inputs; recurring L3 P&L/OCI location and reconciliation, tabular quantitative form | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 12 completa (txt PAGE 116-122) (EVID-285) |
| LB-006 | Norma NIIF para las PYMES, Sección 30 + Apéndice 30A (moneda extranjera): 30.2-30.5 moneda funcional (indicadores: moneda que influye principalmente en precios de venta; costos; financiación; retención de fondos; y para negocios en el extranjero: autonomía, proporción de transacciones con la entidad que informa, impacto de flujos de efectivo, autosuficiencia). 30.7/30.8 reconocimiento inicial "aplicando al importe de la moneda funcional la tasa de cambio de contado… en la fecha de la transacción"; "Por razones de orden práctico… tasa media semanal o mensual para todas las transacciones… Sin embargo, cuando las tasas de cambio varían de forma significativa, resultará inadecuado el uso de la tasa promedio." 30.8A (3ª ed.): "Cuando una entidad paga o recibe una contraprestación por adelantado en una moneda extranjera, reconoce un activo no monetario o un pasivo no monetario. La tasa de cambio que debe utilizarse en el reconocimiento inicial del activo, gasto o ingreso correspondiente (o parte de él) es la tasa de cambio en la fecha en que la entidad reconoció inicialmente el activo no monetario o el pasivo no monetario derivado del pago o la recepción de una contraprestación anticipada. Si existen múltiples pagos o cobros anticipados… una fecha de la transacción para cada pago o cobro." 30.9: (a) partidas monetarias a la tasa de cierre; (b) no monetarias a costo histórico → tasa de la fecha de la transacción; (c) no monetarias a valor razonable → tasas en la fecha en que se determinó el FV. 30.10 diferencias a resultados, salvo 30.13; 30.11 ganancia/pérdida de partida no monetaria a OCI → componente de cambio a OCI; a resultados → a resultados. 30.12-30.13 inversión neta: partidas monetarias "cuya liquidación no está contemplada ni sea probable… en el futuro previsible" (no cuentas comerciales) = parte de la inversión neta; en estados que contengan al negocio y a la entidad, diferencias "inicialmente en otro resultado integral… como un componente del patrimonio. No se volverán a reconocer en resultados… en el momento de la disposición de la inversión neta." 30.14-30.16 cambio de moneda funcional: prospectivo, tasas a la fecha del cambio; "Los importes convertidos resultantes para partidas no monetarias se tratarán como sus costos históricos"; solo si cambian las transacciones/sucesos/condiciones subyacentes. 30.17-30.20 presentación ≠ funcional: activos/pasivos (incl. comparativos) a tasa de cierre de cada ESF; ingresos/gastos (incl. comparativos) a tasas de fecha de transacción (media permitida, inadecuada si variación significativa); "(c) todas las diferencias de cambio resultantes se reconocerán en otro resultado integral… No se reclasificarán posteriormente al resultado del periodo"; fuentes (30.19); NCI attribution (30.20). 30.26-30.29 revelaciones: importe de diferencias en resultados (salvo FV-P&L de Sección 11) y en componente separado del patrimonio; moneda de presentación y, si difiere, moneda funcional + razón; cambio de moneda funcional; tasas estimadas por inconvertibilidad (moneda, restricciones, transacciones, importes, tasas usadas, proceso) + negocios extranjeros no convertibles. Apéndice 30A marco de convertibilidad (retraso administrativo normal; mecanismo de mercado exigible; propósito específico; primera tasa posterior disponible). | Functional currency by indicators (sales-price currency; cost drivers; financing; funds retention; foreign-operation autonomy/transaction share/cash-flow impact/self-sufficiency). Initial recognition at the transaction-date spot; weekly/monthly averages practical UNLESS rates fluctuate significantly. Prepaid/advance consideration (3rd ed. 30.8A): non-monetary item; the asset/expense/income (or part) is recognized at the rate of the date the prepaid non-monetary item was first recognized; one transaction date per advance payment. Subsequently: monetary at closing rate; non-monetary at cost → transaction-date rate; at FV → FV-determination-date rate. Differences to P&L except net-investment routing; non-monetary revaluation OCI/P&L consistency. Net investment: non-settled-foreseeable monetary items (not trade) — in statements containing both, differences initially OCI as an equity component, never re-recognized in P&L on disposal. Functional-currency change prospective (translated amounts = new historical costs). Presentation ≠ functional: assets/liabilities (incl. comparatives) at closing; income/expenses at transaction dates (averages with the volatility caveat); ALL differences OCI as equity, never recycled; NCI attribution. FX disclosures: P&L amounts (Sección 11 FV-P&L excluded), separate-equity amounts, presentation/functional currencies + reason, functional changes, estimated-rate/convertibility disclosures. Appendix 30A convertibility framework (normal administrative delay; enforceable market mechanism; purpose-specific; first subsequent rate) | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 30 completa + Apéndice 30A (txt PAGE 277-287) (EVID-297) |
| LB-007 | Norma NIIF para las PYMES, Sección 31 (hiperinflación): indicadores (inflación acumulada 3 años ≈/≥100% etc.); reexpresión indexada de estados financieros; ganancia/pérdida de la posición monetaria neta; 31.14 cese de reexpresión. NOTA: "no aplicable a entidades SV funcionales en USD — nota histórica únicamente" (EVID-297 gloss) — USD no es moneda de economía hiperinflacionaria; el motor se entrega apagado para SV. | Hyperinflation indicators (e.g. cumulative 3-year inflation at/above 100%), indexed restatement mechanics, net monetary position gain/loss, cessation rules — a CONFIG-OFF surface for SV: USD-functional SV entities never trigger Section 31; the guard exists to block accidental application, not to encode any SV hyperinflation expectation | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 31 (txt PAGE 288-291) (EVID-297) |
| LB-008 | Guía EY (SECUNDARIA per R29(a); nunca LB única): contraste NIIF completas vs PYMES (EVID-299) — deterioro: NIIF completas usa pérdidas crediticias esperadas (expected credit loss, ECL) mientras la PYMES usa el modelo de pérdidas incurridas (11.21-11.26); coberturas: IFRS 9 permite un modelo amplio de contabilidad de coberturas frente al menú estrecho swap/contrato a plazo de 11.60-11.71. Contraste documentado como nota de frontera — NUNCA importado como motor para SV. | (Secondary authority, R29(a)): the guide documents that full NIIF applies expected-credit-loss impairment and a broad IFRS 9 hedge model, against the PYMES incurred-loss and narrow-hedging models — recorded as boundary contrasts showing which entities fall outside the PYMES engine; the SV engine stays 32_ without exception | `sv/sources/33_Guia_NIIF_Sostenibilidad_2024-2025.pdf` | Contrastes NIIF completas/PYMES (EVID-299; EV33 OQ-1) |

## 3. Functional Requirements

### 3.1 Part I scope and classification (Sección 11 Parte I)

- **SV-COA-FR-055:** The system shall classify financial instruments
  into Part I (basic instruments) vs Part II at initial recognition using
  the 11.8 basic set: (a) *efectivo* (cash); (b) a *instrumento de deuda*
  (debt instrument — account, note or loan receivable/payable) meeting
  the 11.9 conditions or the 11.9ZA fallback; (c) a commitment to receive
  a loan that cannot be settled net in cash and is expected to meet 11.9
  when exercised; (d) an investment in *acciones preferentes no
  convertibles* (non-convertible preference shares) and ordinary or
  preference shares *sin opción* (without put option) — with everything
  not qualifying routed to Part II per 11.10 (swaps, cash-settled
  forwards, options, futures, equity investments other than 11.8(d)),
  and the exclusion lists of 11.49 (Secciones 9/14/15 investments, 20
  leases, 22 own equity, 26 share-based payments, 28 employee benefits,
  21 reimbursements, 23-receivable carve-out) respected.
  (LB-001; LB-004; EVID-284)
- **SV-COA-FR-056:** The system shall implement the 11.9 debt-instrument
  conditions as a machine-checkable set: (a) returns to the holder in the
  instrument's denomination currency are a fixed amount, a fixed rate of
  return, a variable return matching a single quoted/observable reference
  (e.g. SONIA-type), or a combination of fixed and variable rates BOTH
  positive; (b) NO contractual clause could cause the holder to lose
  principal or attributable interest (subordination is NOT such a clause;
  reasonable early-termination compensation is permitted); (c) prepayment
  or demand clauses are conditioned only on protective events (holder
  protection against credit-risk/control changes of the issuer, or
  relevant legal/fiscal changes); (d) no contingent return or redemption
  clause beyond (a) variable-rate returns and (c) prepayment clauses; and
  the 11.9ZA fallback: a debt instrument failing 11.9(a)-(d) STILL falls
  in Part I when its contractual terms produce, on specified dates, cash
  flows that are SOLELY payments of principal and interest on the
  outstanding principal — "interest" including reasonable compensation
  for the time value of money, credit risk and other basic lending risks
  and costs consistent with a basic lending arrangement (instruments
  exposing to unrelated risks or volatility are unlikely to qualify), all
  anchored to the Norma's printed examples (fixed-then-variable bank
  loans, observable-rate + spread loans, trade accounts and notes, and
  foreign-currency payables — with the 30.10 FX note — as qualifying;
  swaps, forwards, options and futures as NOT qualifying).
  (LB-001; EVID-284)
- **SV-COA-FR-057:** The system shall enforce the 11.11A
  no-reclassification rule: after initial recognition, a financial asset
  or financial liability is NEVER reclassified into or out of Part I —
  the Part I/Part II determination is made once at initial recognition
  and any later change of view (e.g. a condition later judged differently)
  produces no reclassification entry.
  (LB-001; EVID-284)
- **SV-COA-FR-058:** The system shall carry the classification as
  account-level flags: every financial-instrument account carries exactly
  one classification — `basic_amortized` (Part I debt + basic set,
  amortized cost + EIR) | `fv_pnl` (fair value with changes in P&L:
  Part I quoted/measurable non-put equities and every Part II instrument
  except the fallback) | `cost_impairment` (cost − impairment: Part I
  non-measurable equities and loan commitments; Part II unquoted-equity
  fallback) — non-instrument accounts carry none; the flag drives which
  measurement, impairment and disclosure engines apply to the account's
  move lines, and is set at account creation from the FR-055/056
  determination (never flipped afterwards per FR-057).
  (LB-001; LB-002; LB-004; EVID-284)

### 3.2 Initial and subsequent measurement (Sección 11 Parte I)

- **SV-COA-FR-059:** The system shall measure Part I financial assets
  and liabilities initially at the transaction price, except where the
  11.13 carve-outs apply — (a) a receivable (FR-060) or (b) an agreement
  that is in effect a financing transaction (FR-061); recognition occurs
  when the entity becomes a party to the instrument's contractual terms.
  (LB-002; LB-004; EVID-284)
- **SV-COA-FR-060:** The system shall measure *cuentas por cobrar
  comerciales* (trade receivables) initially at the amount determined by
  applying Sección 23 (owned by `06_revenue.md` by id), unless the
  agreement is in effect a financing transaction AND the entity does not
  apply the 23.38 practical-expedient option — in which case measurement
  follows FR-061.
  (LB-002; EVID-284)
- **SV-COA-FR-061:** The system shall implement the 11.13B
  financing-transaction rule: when payment is deferred beyond normal
  commercial terms, or financing is at a non-market rate (an interest-free
  loan or a below-market loan — the printed example is an employee loan;
  the SV kin is the partner/shareholder loan), the financial asset or
  liability is measured at the *valor presente de los pagos futuros*
  (present value of future payments), discounted at a MARKET interest
  rate for a similar debt instrument determined at initial recognition —
  the system computes and stores the discount, the market-rate basis and
  the implicit interest schedule (FR-062) at recognition, and posts
  interest income/expense over the term. **Two-clock invariant:** the
  FISCAL treatment of partner/shareholder loans (deemed dividends under
  Ley ISR Arts. 25/74-A — `sv/requirements/taxation/05_isr-distributions.md`
  LB-004/LB-007, consumed by id) never overrides, nor is derived from,
  this book PV; book-vs-fiscal differences route to
  `08_deferred-tax-adoption.md` (T8) by filename.
  (LB-002; EVID-284)
- **SV-COA-FR-062:** The system shall implement the amortized-cost +
  *tasa de interés efectiva* (effective interest rate, EIR) engine of
  11.15-11.20: amortized cost at each reporting date = initial
  recognition amount − principal repayments ± accumulated amortization
  (at EIR) of any difference between initial amount and maturity amount −
  impairment reductions (direct or via *cuenta correctora* (contra
  account)); the EIR is the rate exactly discounting estimated cash flows
  over the expected life to the initial carrying amount, taking into
  account ALL contractual terms (prepayments, options) and INCURRED known
  credit losses but NOT not-yet-incurred expected future credit losses;
  fees, financial charges ("puntos" (points)), transaction costs and
  premiums/discounts amortize over the expected life (shorter — to the
  next reset date — when the variable tracks market rates before
  maturity); variable-rate instruments re-estimate periodically (EIR
  changes; normally no significant carrying effect when initially at
  principal); estimate revisions recompute the carrying amount as the PV
  of revised cash flows at the ORIGINAL EIR with the adjustment to P&L at
  the revision date; instruments without an interest rate, not part of a
  financing transaction and classified as current measure at the
  UNDISCOUNTED amount expected (net of impairment); and the engine
  produces the Norma's worked-example schedule pattern — opening carrying
  × EIR = interest income/expense − cash flow = closing carrying
  (reproducing the printed 5-year bond example: 950 net cost, 6.9584%
  EIR, annual 40 coupons, 1,100 redemption, rolling to exactly 1,100 at
  maturity).
  (LB-002; EVID-284)
- **SV-COA-FR-063:** The system shall measure Part I equities and loan
  commitments subsequently as: loan commitments at cost (sometimes zero)
  − impairment; investments in non-put ordinary/preference shares and
  non-convertible preference shares at (i) fair value with FV changes in
  P&L when the shares are exchange-quoted OR fair value is otherwise
  reliably measurable WITHOUT disproportionate cost or effort, else (ii)
  cost − impairment (measurability calls recorded with their evidence
  basis; disproportionate-cost relief uses registered via
  `01_framework-policies.md` FR-012 by id); and dividends are recognized
  in P&L ONLY when (a) the entity's right to payment is established, (b)
  receipt of the associated economic benefits is probable, and (c) the
  amount is reliably measurable.
  (LB-002; EVID-284)

### 3.3 Incurred-loss impairment (11.21-11.26)

- **SV-COA-FR-064:** The system shall implement the INCURRED-loss
  impairment model — explicitly NOT expected credit loss: at each
  reporting date, cost/cost-amortized financial assets are assessed for
  *evidencia objetiva* (objective evidence) of impairment, and a loss is
  recognized IMMEDIATELY in P&L only when objective evidence exists — the
  observable event list: (a) significant financial difficulty of the
  issuer/obligor; (b) contractual breach such as default or *mora*
  (arrears) on interest or principal; (c) creditor concessions granted
  for economic or legal reasons linked to the debtor's financial
  difficulty; (d) it becomes probable the debtor enters bankruptcy or
  other financial reorganization; (e) observable data indicating a
  measurable decrease in a GROUP's estimated future cash flows since
  initial recognition, though not yet identifiable with individual assets
  (adverse national/local economic or sector conditions); plus other
  adverse technological/market/economic/legal environment changes —
  forward-looking indicators alone NEVER trigger a loss; the full-NIIF
  ECL model is a documented contrast only (33_ secondary per R29(a),
  LB-008), never an engine option.
  (LB-003; LB-008 secondary contrast; EVID-284/299)
- **SV-COA-FR-065:** The system shall scope the impairment assessment:
  equity instruments are assessed ALWAYS individually; other financial
  assets are assessed individually when individually significant; the
  remainder individually or GROUPED on the basis of similar credit-risk
  characteristics (grouping basis recorded on the impairment record;
  regrouping is an estimate-change event per `01_framework-policies.md`
  FR-017 by id).
  (LB-003; EVID-284)
- **SV-COA-FR-066:** The system shall measure impairment losses and
  reversals: amortized-cost assets → loss = carrying amount − present
  value of estimated future cash flows discounted at the asset's ORIGINAL
  EIR (variable-rate assets → the CURRENT contractual EIR); cost-measured
  assets (equities, commitments, Part II fallback) → the best estimate —
  "necessarily an approximation" — of the amount the entity would receive
  for the asset if sold at the reporting date (which may be zero);
  reversals are recognized when the loss decreases AND the decrease is
  objectively related to an event occurring AFTER the impairment was
  recognized (e.g. an improved credit rating), directly or via allowance
  account, to P&L immediately, CAPPED at the carrying amount the asset
  would have had had the impairment never been recognized.
  (LB-003; EVID-284)

### 3.4 Derecognition (11.33-11.38)

- **SV-COA-FR-067:** The system shall derecognize a financial asset ONLY
  when (a) the contractual rights to its cash flows expire or are
  settled; (b) the entity transfers SUBSTANTIALLY all risks and rewards
  of ownership to third parties; or (c) despite retaining some
  significant inherent risks and rewards, the entity transfers CONTROL
  of the asset to a party with the practical ability to sell the asset in
  its entirety to an unrelated third party, unilaterally and without
  additional transfer restrictions — case (c) derecognizes the asset AND
  separately recognizes any retained and created rights and obligations;
  on any qualifying transfer the carrying amount is allocated between
  retained and transferred rights/obligations on their RELATIVE FAIR
  VALUES at transfer date (new rights at fair value; any difference
  between consideration and net derecognized amount to P&L in the period
  of transfer); on a FAILED transfer (significant risks/rewards retained
  — e.g. a 120-day-recourse receivable sale) the transferred asset stays
  recognized IN ITS ENTIRETY with a financial liability recognized for
  the consideration received, asset and liability NEVER offset, income
  and expense on each recognized separately; non-cash collateral is
  reclassified separately when the receiver may sell or repledge it
  (pledged/lent-asset presentation), derecognized on transferor default,
  and otherwise stays off the receiver's balance sheet.
  (LB-003; EVID-284)
- **SV-COA-FR-068:** The system shall derecognize a financial liability
  (or part) ONLY when extinguished — paid, cancelled or expired; an
  exchange of instruments with SUBSTANTIALLY DIFFERENT terms, and a
  SUBSTANTIAL MODIFICATION of an existing liability's terms (whether or
  not attributable to the debtor's financial difficulty), are both
  accounted for as EXTINGUISHMENT of the original liability +
  recognition of a NEW liability; any difference between the carrying
  amount of the extinguished/transferred liability and the consideration
  paid (including any non-cash assets transferred and liabilities
  assumed) is recognized in P&L.
  (LB-003; EVID-284)

### 3.5 Sección 11 disclosures (11.39-11.48)

- **SV-COA-FR-069:** The system shall emit the instrument-balance
  disclosure set: measurement-basis policy information (per 8.5,
  `01_framework-policies.md` FR-019/020 by id); carrying amounts by the
  six ESF categories at the reporting date — FV-P&L financial assets;
  amortized-cost debt assets; cost−impairment equity assets; FV-P&L
  financial liabilities; amortized-cost financial liabilities; cost−
  impairment loan commitments; significant-terms information for
  long-term debt (rate, maturity, repayment schedule, restrictions); the
  income/expense/gains/losses items — FV changes by FV-P&L assets and
  liabilities and by amortized-cost assets and liabilities, TOTAL
  interest income and expense computed at the EIR for non-FV instruments,
  and impairment losses per class of financial asset; and where a
  reliable FV is unavailable (or only with disproportionate cost —
  registry-linked per FR-063), the fact, the instruments' carrying
  amounts and, when the relief is used, the reasons.
  (LB-004; EVID-284)
- **SV-COA-FR-070:** The system shall auto-build from move lines: the
  *análisis de antigüedad* (aging analysis) of trade receivables and
  other amortized-cost financial assets by reference to due date, showing
  SEPARATELY the amortized cost before impairment reduction and the
  impairment reduction (11.43); and the *análisis de vencimiento*
  (maturity analysis) of financial liabilities by category based on
  remaining contractual maturities at UNDISCOUNTED contractual cash
  flows (11.43A); time bands default to the Norma's illustrative set —
  up to one month; more than one to three months; more than three months
  to one year; more than one to five years; more than five years — and
  are configurable per company (11.43B lets the entity use the most
  useful bands).
  (LB-004; EVID-284)
- **SV-COA-FR-071:** The system shall emit the collateral-and-default
  disclosure set: financial assets transferred in transactions failing
  derecognition — nature of the assets, nature of the retained
  risks-and-rewards exposure, carrying amounts of the assets and any
  associated continuing liabilities; financial assets *pignorados como
  garantía* (pledged as collateral) — the carrying amount of pledged
  assets and the related terms and conditions; and *préstamos por pagar*
  (loans payable) with an UNSOLVED breach or default of principal,
  interest, sinking-fund or repayment terms at the reporting date —
  details of the breach, the related carrying amount, and whether cured
  or renegotiated before FS authorization.
  (LB-004; EVID-284)

### 3.6 Part II: FV default, equity fallback, narrow hedging (11.49-11.75)

- **SV-COA-FR-072:** The system shall implement the Part II default:
  every financial instrument outside Part I and outside the 11.49
  exclusions is recognized when the entity becomes a party to the
  contractual terms, measured initially at fair value (normally the
  transaction price) and subsequently at FAIR VALUE with changes in FV
  recognized in P&L — except the two carve-outs: (a) the hedging OCI
  portion of designated hedge instruments (FR-074/075) and (b) the
  unquoted-equity fallback (FR-073); the fair value of an
  *exigible a la vista* (payable on demand) financial liability is not
  less than the amount payable on demand, discounted from the first date
  payment could be required; FV determination uses the Sección 12 engine
  (FR-076..081) per 11.57; impairment (FR-064..066) and derecognition
  (FR-067/068) guidance applies to Part II cost-measured assets.
  (LB-004; LB-005; EVID-284)
- **SV-COA-FR-073:** The system shall implement the unquoted-equity cost
  fallback: publicly unquoted equity instruments whose fair value cannot
  be otherwise reliably measured without disproportionate cost or effort
  (and contracts linked to them that, if exercised, deliver such
  instruments) are measured at COST − impairment; when a reliable FV
  WITHOUT disproportionate cost ceases to be available for an
  FV-measured equity, the LAST reliable fair value measured without such
  cost becomes the instrument's COST, and the instrument stays at that
  cost − impairment until a reliable FV again becomes measurable without
  disproportionate cost (relief applications registered via
  `01_framework-policies.md` FR-012 by id and disclosed per FR-069).
  (LB-004; EVID-284)
- **SV-COA-FR-074:** The system shall implement hedging as a
  CONFIG-GATED engine (default OFF for SV PYMES — OQ-1): when enabled, a
  hedge designation requires ALL of: documented designation identifying
  the hedged risk, the hedged item and the hedge instrument (the hedged
  risk being the risk the instrument hedges); the hedged risk being one
  of the FOUR 11.63 risks — (a) interest-rate risk of an amortized-cost
  debt instrument; (b) FX or interest-rate risk on a firm commitment or a
  highly probable forecast transaction; (c) quoted-commodity price risk
  of a held commodity, a firm commitment or a highly probable forecast
  transaction; (d) FX risk on a net investment in a foreign business;
  the hedge instrument meeting 11.64 — ONLY an interest-rate swap, an FX
  swap, a forward-exchange contract or a commodity forward contract,
  with an EXTERNAL counterparty (outside the reporting entity/group),
  notional EQUAL to the designated principal/notional of the hedged item,
  a specified maturity NOT LATER than the hedged instrument's maturity /
  the commitment's settlement / the forecast transaction's occurrence,
  and NO prepayment, early-termination or extension features; and the
  hedge expected to be HIGHLY effective in offsetting the designated
  risk.
  (LB-004; EVID-284)
- **SV-COA-FR-075:** The system shall implement hedge accounting
  mechanics: for fixed-rate-debt and held-commodity hedges
  (FV-hedge type) — hedge instrument recognized at FV with changes in
  P&L and the hedged item's carrying amount adjusted for the
  hedged-risk-attributable FV change (also P&L), periodic net cash
  settlements accrued to P&L; for variable-rate, firm-commitment/
  forecast FX/commodity and net-investment hedges (cash-flow-hedge type)
  — the EFFECTIVE portion of the hedge instrument's FV change to OCI,
  any excess (ineffectiveness) to P&L, the OCI amount reclassified to
  P&L when the hedged item affects P&L — EXCEPT net-investment-hedge FX
  amounts, which are NEVER reclassified on disposal or partial disposal;
  hedge accounting discontinued prospectively when the instrument
  expires/is sold/settled, the conditions cease to be met, or the
  designation is revoked, with carrying-amount adjustments on continuing
  amortized-cost items amortized to P&L at the EIR over the item's
  remaining life.
  (LB-004; EVID-284)

### 3.7 Fair-value engine (Sección 12)

- **SV-COA-FR-076:** The system shall keep ONE reusable
  fair-value-measurement record model consumed by every FV surface of
  this wave (Sección 11 Part I equities, Part II instruments, hedge
  instruments, FX non-monetary FV items) and consumable by the other
  files' FV surfaces by id (inventories NRV-adjacent, investment
  property, PPE revaluation, business-combination, non-cash
  consideration, grant-date, plan-asset kin): each record stores the
  measured item, the valuation date, the fair-value amount and currency,
  the measurement basis — *precio de salida* (exit price): the price
  that would be RECEIVED to sell an asset or PAID to transfer a liability
  in an orderly transaction between market participants at the
  measurement date, a market-based (not entity-specific) measurement —
  plus the hierarchy level (FR-080), technique (FR-079), inputs and
  market basis (FR-077).
  (LB-005; EVID-285)
- **SV-COA-FR-077:** The system shall anchor each FV measurement to a
  market: the PRINCIPAL market (greatest volume and activity level for
  the asset/liability) when one exists, else the MOST-ADVANTAGEOUS market
  (maximizing the amount received for the asset / minimizing the amount
  paid to transfer the liability, after transaction and transport
  costs) — the entity must have ACCESS to that market; transaction costs
  are NOT deducted from FV (they are not a characteristic of the
  asset/liability; a transaction price is an ENTRY price, FV an EXIT
  price); transport costs DO adjust the price when location is a
  characteristic of the item.
  (LB-005; EVID-285)
- **SV-COA-FR-078:** The system shall apply the *máximo y mejor uso*
  (highest and best use) basis when measuring the FV of NON-FINANCIAL
  assets: the use physically possible, legally permissible and
  financially feasible that maximizes the asset's value, with CURRENT USE
  presumed unless a demonstrably better alternative use exists (whether
  by market participants or the entity); the resulting use sets the
  valuation premise — in use vs in exchange (the consuming files'
  assets — inventories, PPE, investment property — cite this engine by
  id; this FR owns the engine, not their classification calls).
  (LB-005; EVID-285)
- **SV-COA-FR-079:** The system shall support the three valuation
  approaches — MARKET (prices and market-observable information),
  COST (replacement cost, i.e. current acquisition/construction cost less
  depreciation/obsolescence) and INCOME (present value techniques
  including discounting, option-pricing models and multi-period excess
  earnings) — with techniques and inputs used consistently and maximally
  exploiting observable inputs; a change in valuation TECHNIQUE or its
  application is an ESTIMATE change (prospective, per
  `01_framework-policies.md` FR-017 by id) unless it stems from an error,
  and the technique-change event is recorded on the FV-measurement
  record.
  (LB-005; EVID-285)
- **SV-COA-FR-080:** The system shall classify every FV measurement in
  the three-level hierarchy by the LOWEST level among the inputs
  significant to the ENTIRE measurement: Level 1 — quoted prices
  (unadjusted) in active markets for identical assets/liabilities the
  entity can access; Level 2 — inputs other than quoted prices within
  Level 1 that are observable for the item, directly or indirectly
  (quoted prices for SIMILAR items in active markets, identical/similar
  items in INACTIVE markets, observable rates and yields,
  market-corroborated inputs); Level 3 — UNOBSERVABLE inputs (entity data
  adjusted
  for reasonably available information about market-participant
  assumptions) used only to the extent observable inputs are unavailable.
  (LB-005; EVID-285)
- **SV-COA-FR-081:** The system shall emit the FV disclosure set per
  class of assets and liabilities measured at FV: carrying amounts and
  the hierarchy level; the valuation technique(s) and significant inputs;
  for RECURRING Level-3 measurements — where in P&L (the affected line)
  or OCI the gains/losses are recognized, the movements/reconciliation of
  Level-3 balances, and the information in tabular quantitative form;
  the FV-class judgment feed for the 8.6 judgments note slot
  (`01_framework-policies.md` FR-021 by id, the 12.30 kin).
  (LB-005; EVID-285)

### 3.8 Foreign currency (Sección 30 + Apéndice 30A + Sección 31 guard)

- **SV-COA-FR-082:** The system shall carry the *moneda funcional*
  (functional currency) determination on the company (and on each foreign
  operation): the currency of the PRIMARY economic environment —
  indicators: the currency that mainly influences SALES PRICES, COSTS and
  expenses, FINANCING, and funds RETENTION from operating activities;
  for foreign operations: autonomy of activities, share of transactions
  with the reporting entity, cash-flow impact on the reporting entity,
  and self-sufficiency (debt serviced by own cash flows) — the
  determination recorded with its evidence basis and date (D15
  snapshot-on-write; management judgment when indicators are mixed) and
  changeable ONLY when the underlying transactions, events and conditions
  change (never by periodic recompute).
  (LB-006; EVID-297)
- **SV-COA-FR-083:** The system shall recognize foreign-currency
  transactions initially by applying to the functional-currency amount
  the SPOT exchange rate between functional and foreign currency at the
  TRANSACTION DATE (the date the transaction first meets the Norma's
  recognition conditions); as a practical approximation a weekly or
  monthly AVERAGE rate may be used for all transactions in each foreign
  currency during the period — but average use is blocked/flagged as
  INADEQUATE when exchange rates fluctuate significantly (rate-source
  and rate-basis recorded per move line).
  (LB-006; EVID-297)
- **SV-COA-FR-084:** The system shall implement the 30.8A
  prepaid-consideration rule: when the entity pays or receives advance
  consideration in a foreign currency, it recognizes a NON-MONETARY
  asset/liability, and the exchange rate for initial recognition of the
  corresponding asset, expense or income (or part of it) is the rate at
  the date the entity FIRST recognized the non-monetary prepaid item —
  with MULTIPLE advance payments/collections taking ONE transaction date
  PER payment/collection; the prepayment's rate is carried to the
  expense/income/asset when the consideration is applied and is NEVER
  remeasured (non-monetary; the closing-rate engine of FR-085 skips it).
  (Version note: 30.8A is a 3rd-edition paragraph; per Apéndice A it may
  be applied prospectively to in-scope preexisting items.)
  (LB-006; EVID-297)
- **SV-COA-FR-085:** The system shall remeasure at each reporting date:
  MONETARY items (rights to receive/pay fixed/determinable currency
  amounts — cash, receivables, payables, loans; account-level monetary
  flag) at the CLOSING rate; NON-MONETARY items measured at historical
  cost at the TRANSACTION-date rate; NON-MONETARY items measured at fair
  value at the rate on the FV-DETERMINATION date (linked to the
  FR-076 record).
  (LB-006; EVID-297)
- **SV-COA-FR-086:** The system shall route exchange differences to P&L
  in the period they arise — differences produced on SETTLING monetary
  items and on remeasuring monetary items at rates different from those
  used at initial recognition or in prior periods — EXCEPT the
  net-investment routing (FR-087); for revalued non-monetary items, the
  routing follows the underlying gain/loss: a non-monetary gain/loss
  recognized in OCI (e.g. PPE revaluation surplus) carries its FX
  component in OCI, one recognized in P&L carries FX in P&L. **Two-clock
  invariant:** this book engine NEVER computes the fiscal conversion —
  CT Art. 62 governs the TAX base only, consumed BY ID as SV-TAX-FR-020
  (`sv/requirements/taxation/01_isr-framework.md`: hecho-generador-day
  USD conversion; payment-date FX differences never in the base;
  installment-sale FX differences added to the base); book-vs-fiscal FX
  differences route to `08_deferred-tax-adoption.md` (T8) by filename,
  never re-derived here.
  (LB-006; EVID-297)
- **SV-COA-FR-087:** The system shall implement net-investment routing:
  monetary items receivable from/payable to a foreign business whose
  settlement is neither planned nor probable in the foreseeable future
  are in substance part of the entity's NET INVESTMENT in that business
  (long-term loans/receivables included; trade receivables/payables
  NEVER) — such items carry a net-investment tag; in FS that contain
  BOTH the foreign business and the reporting entity (e.g.
  consolidated), the exchange differences on them are recognized
  INITIALLY IN OCI and presented as an equity component, and are NEVER
  re-recognized in P&L on disposal or PARTIAL disposal of the net
  investment; in separate/individual FS the differences stay in P&L.
  (LB-006; EVID-297)
- **SV-COA-FR-088:** The system shall implement functional-currency
  change PROSPECTIVELY: on a change, translation procedures for the new
  functional currency apply from the change date; ALL items are
  translated at the rate at the change date; the resulting translated
  amounts for non-monetary items become their NEW HISTORICAL COSTS (no
  restatement of comparatives); the change is disclosed with its reason
  (FR-090), and the event records on the FR-082 determination with its
  new evidence basis.
  (LB-006; EVID-297)
- **SV-COA-FR-089:** The system shall implement presentation-currency
  translation when the *moneda de presentación* (presentation currency)
  differs from functional (the company may present in ANY currency):
  assets and liabilities of EVERY statement of financial position
  presented — including comparatives — at the CLOSING rate of each
  ESF date; income and expenses of every statement — including
  comparatives — at TRANSACTION-date rates (period-average approximation
  allowed, inadequate under significant fluctuation); ALL resulting
  exchange differences recognized in OCI and presented as a component of
  equity, NEVER reclassified subsequently to P&L; difference sources:
  income/expense at transaction vs assets/liabilities at closing, and
  translation of the opening net assets at closing vs prior-closing
  rate; cumulative translation attributable to *participación no
  controladora* (non-controlling interests) allocated to NCI in
  consolidated statements; when the functional currency is that of a
  hyperinflationary economy, Sección 31 procedures apply instead
  (FR-092 guard); consolidation application surfaces (30.21-30.23:
  intragroup monetary items NOT eliminated — a commitment to convert;
  goodwill and FV adjustments treated as foreign-operation items at
  closing rate) are owned by `07_groups-related-parties.md` by id.
  (LB-006; EVID-297)
- **SV-COA-FR-090:** The system shall emit the FX disclosures: the
  amount of exchange differences recognized in P&L during the period —
  EXCEPT those from instruments measured at FV-with-changes-in-P&L under
  Sección 11 (already inside those FV changes); the amount of exchange
  differences arising in the period classified in a SEPARATE COMPONENT
  OF EQUITY at period end; the presentation currency of the FS and, when
  presentation differs from functional, that fact plus the functional
  currency and the REASON for using a different presentation currency;
  any change in functional currency of the entity or of a significant
  foreign business, with its reason.
  (LB-006; EVID-297)
- **SV-COA-FR-091:** The system shall implement the convertibility
  framework of Apéndice 30A: when a currency is NOT convertible into
  another (no legally enforceable mechanism to obtain the currency at
  the measurement-date rate through normal administrative delay), the
  spot rate is ESTIMATED (first subsequent rate at which conversion
  becomes possible at a normal administrative delay, among the
  appendix's estimation routes); estimated-rate use triggers the 30.28
  disclosures — the currency and the restrictions making it
  non-convertible, the affected transactions, the carrying amounts of
  affected assets/liabilities, the spot rates used and whether they are
  observable-without-adjustment or estimated by another technique, and
  the estimation process with qualitative/quantitative inputs and
  assumptions — plus, for foreign operations whose functional currency
  is not convertible into the presentation currency (or vice versa), the
  30.29 disclosures (name, entity type, principal place of business,
  summarized financial information, and the nature and conditions of
  arrangements that could require the entity to provide financial
  support); SV default: USD-functional entities do not trigger this FR
  (no SV restriction rows invented — config-only).
  (LB-006; EVID-297)
- **SV-COA-FR-092:** The system shall ship the Sección 31 hyperinflation
  engine as a CONFIG-OFF guard for SV: the restatement machinery
  (hyperinflation indicators — e.g. cumulative three-year inflation at
  or above 100% among the printed indicators — indexed restatement of
  the FS, net monetary position gain/loss, and the 31.14 cessation
  rules) exists behind an explicit per-company gate that is LOCKED OFF
  while the company's functional currency (FR-082) is USD — a
  non-hyperinflationary currency for SV — blocking accidental
  application and blocking the hyperinflationary variant of
  presentation translation (FR-089); no SV hyperinflation expectation is
  encoded anywhere.
  (LB-007; LB-006; EVID-297)

## 4. Data Model

Layer semantics: all entities are Odoo-native (account.account /
account.move engines + l10n_sv_chart config and register rows) — wave
default `odoo` (§5). The Norma's IASB authors are external authorities:
the model records the COMPANY's own classifications, measurements and
determinations. No printed data table here warrants a CSV sidecar (the
bands, risk types and level catalogs are small config sets; default none
per plan).

**Instrument classification (on account.account):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.account | sv_coa_instrument_class | select | none (default, non-instrument) · basic_amortized · fv_pnl · cost_impairment | FR-055..058 |
| account.account | sv_coa_monetary | boolean | monetary vs non-monetary flag for FX remeasurement (30.9); prepaid-consideration items false | FR-084, FR-085 |
| account.account | sv_coa_instrument_determination | config text | 11.8/11.9/11.9ZA condition-set result snapshot (D15) + date; never flipped post-initial (11.11A) | FR-055..057 |

**Financing instruments + EIR engine (l10n_sv_chart.loan / .eir_schedule):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.loan | instrument_class | select | basic_amortized · fv_pnl · cost_impairment (mirror of account flag) | FR-058 |
| l10n_sv_chart.loan | initial_basis | select | transaction_price · sec_23_receivable · pv_market_rate (11.13B financing flag; interest-free/below-market basis recorded) | FR-059..061 |
| l10n_sv_chart.loan | pv_market_rate + rate_basis | float + char | market rate for similar debt at initial recognition + provenance | FR-061 |
| l10n_sv_chart.loan | eir + eir_basis | float + char | original EIR at initial carrying; variable-rate → current contractual EIR snapshots | FR-062, FR-066 |
| l10n_sv_chart.eir_schedule | period · opening · interest_at_eir · cash · closing | date · monetary ×4 | the worked-example pattern rows (opening × EIR = interest − cash = closing) | FR-062 |
| l10n_sv_chart.loan | partner_loan_flag + fiscal_track_link | boolean + m2o by id | partner/shareholder loan → taxation/05 (Ley ISR 25/74-A, LB-004/LB-007 of that file) linked, never merged; DT bridge → 08 (T8) by filename | FR-061 |

**Impairment + derecognition (l10n_sv_chart.impairment / .derecognition):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.impairment | trigger | select | financial_difficulty · contract_breach_mora · creditor_concession · probable_bankruptcy · group_measurable_decrease · adverse_environment (objective-evidence set; incurred-loss ONLY — no ECL) | FR-064 |
| l10n_sv_chart.impairment | scope | select | individual (equities always; individually significant) · grouped (credit-risk characteristics basis recorded) | FR-065 |
| l10n_sv_chart.impairment | measurement | select | pv_original_eir (amortized-cost; discount-rate snapshot) · best_estimate_sale (cost-measured; may be zero) | FR-066 |
| l10n_sv_chart.impairment | reversal_cap | boolean/monetary | cap = carrying had no impairment been recognized; objectively-linked post-event only; immediate to P&L | FR-066 |
| l10n_sv_chart.derecognition | outcome | select | rights_expired_settled · risks_rewards_transferred · control_transferred_separate_retained · failed_transfer_full_asset_plus_liability | FR-067 |
| l10n_sv_chart.derecognition | relative_fv_allocation + pld_amount | monetary | carrying allocation retained vs transferred at relative FVs; difference to P&L | FR-067 |
| l10n_sv_chart.derecognition | substantial_modification | boolean | liability: extinguish + new on substantially-different exchange/modification; consideration incl. non-cash | FR-068 |

**Fair-value engine (l10n_sv_chart.fair_value_measurement):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.fair_value_measurement | subject + valuation_date | m2o polymorphic + date | the ONE reusable record model consumed across the wave and by other files by id | FR-076 |
| l10n_sv_chart.fair_value_measurement | amount + currency | monetary + m2o | exit price | FR-076 |
| l10n_sv_chart.fair_value_measurement | market_basis | select | principal_market · most_advantageous (access recorded; transport-cost characteristic flag) | FR-077 |
| l10n_sv_chart.fair_value_measurement | best_use_premise | select | current_use_presumed · alternative_use_documented (non-financial assets; in_use · in_exchange) | FR-078 |
| l10n_sv_chart.fair_value_measurement | technique | select | market · cost · income (+ named technique); technique-change event = estimate change (01 FR-017 by id) | FR-079 |
| l10n_sv_chart.fair_value_measurement | level | select | 1 · 2 · 3 — lowest significant input classifies the WHOLE measurement | FR-080 |
| l10n_sv_chart.fair_value_measurement | inputs | one2many | per input: value · observable (1/2) · unobservable-adjusted-for-market-participants (3) · significant flag | FR-080, FR-081 |

**Hedging (config-gated; l10n_sv_chart.hedge_relation):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_coa_hedging_enabled | boolean | DEFAULT FALSE (OQ-1) — SV PYMES rarely qualify | FR-074 |
| l10n_sv_chart.hedge_relation | hedged_risk | select | interest_rate_amortized_cost · fx_or_rate_firm_forecast · commodity_price · fx_net_investment (the four 11.63 risks only) | FR-074 |
| l10n_sv_chart.hedge_relation | instrument | select | swap_interest_rate · swap_fx · forward_fx · forward_commodity (11.64 whitelist — no options, no features) | FR-074 |
| l10n_sv_chart.hedge_relation | conditions_check | booleans | external_counterparty · notional_equal · maturity_not_later · no_prepayment_termination_extension · documented_designation · high_expected_effectiveness | FR-074 |
| l10n_sv_chart.hedge_relation | routing | select | fv_pnl_carrying_adjustment (11.65) · oci_effective_pl_ineffectivity (11.69; net-investment never recycled) + discontinuation rows (EIR amortization) | FR-075 |

**FX config + engines (res.company / account.move.line / l10n_sv_chart):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_coa_functional_currency | m2o res.currency | with indicators record + determination date (D15); change only on underlying change | FR-082 |
| res.company | sv_coa_functional_change_events | one2many | change date + prospective application + translated-amounts-as-new-cost note + reason | FR-088 |
| res.company | sv_coa_hyperinflation_guard | config | LOCKED OFF while functional = USD (Sec 31 guard) | FR-092 |
| account.move.line | sv_coa_rate_basis | select | spot · weekly_average · monthly_average · prepayment_date · closing · fv_date · change_date (each with rate-source provenance) | FR-083..086, FR-088 |
| account.move.line | sv_coa_prepayment_link | m2o | advance-consideration link: the related expense/income/asset inherits the prepayment-date rate; skipped by closing remeasurement | FR-084 |
| account.move.line | sv_coa_net_investment_tag | m2o/boolean | net-investment-in-foreign-business monetary item (long-term loans/receivables; trade never) → OCI routing, no recycling | FR-087 |
| res.company | sv_coa_translation_oci_account | m2o account.account | presentation-translation OCI equity component (never recycled) + net-investment OCI component | FR-087, FR-089 |

**Disclosure config (res.company / l10n_sv_chart):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | sv_coa_aging_maturity_bands | config | default Norma set: ≤1m · >1m-3m · >3m-1y · >1y-5y · >5y (configurable per 11.43B) | FR-070 |
| l10n_sv_chart.pledge | asset · terms | m2o + text | pledged-collateral register feeding FR-071 disclosures | FR-071 |
| l10n_sv_chart.loan_breach | details · carrying · status | text · monetary · select | unsolved breach/default register (cured/renegotiated before authorization) | FR-071 |

## 5. Odoo Mapping

Layer semantics: financial instruments, FV and FX are Odoo-native GL
surfaces (account.account/account.move.line multi-currency engine,
res.currency/res.currency.rate, dedicated l10n_sv_chart registers) — every
FR maps `odoo`; no SaaS rows (nothing here touches DTE
generation/transmission, the only architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Odoo's native
multi-currency (amount_currency/currency_id, daily res.currency.rate)
covers spot mechanics; prepayment-date rate anchoring, net-investment
OCI routing, FV registers and the EIR engine are l10n_sv_chart
extensions (OQ-2 records the loan-object mapping gap). Model names
stable across Odoo 17/18/19/20.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-055 | odoo | account.account + config | basic-set determination | 11.8 set + 11.10/11.49 routing; Part I vs Part II at initial recognition only |
| FR-056 | odoo | l10n_sv_chart config | 11.9/11.9ZA condition checks | a-d + cash-flows-only-principal-and-interest fallback; "interés" gloss encoded; printed examples anchored |
| FR-057 | odoo | account.account | immutable determination | 11.11A: no post-initial reclassification — UI + API block |
| FR-058 | odoo | account.account | sv_coa_instrument_class | basic_amortized \| fv_pnl \| cost_impairment; drives measurement/impairment/disclosure engines |
| FR-059 | odoo | account.move | initial measurement | transaction price at recognition (party-to-contractual-terms trigger) |
| FR-060 | odoo | account.move.line | receivable initial amount | Sección 23 amount (06_revenue by id); 23.38 option interplay gate |
| FR-061 | odoo | l10n_sv_chart.loan + account.move | pv_market_rate + schedule | 11.13B financing rule; partner loans flagged + taxation/05 LB-004/LB-007 linked by id; DT bridge 08 (T8) filename |
| FR-062 | odoo | l10n_sv_chart.eir_schedule | EIR roll-forward rows | worked-example pattern (950/6.9584%/40-coupon/1,100 anchor test); original-EIR revisions; current-undiscounted simplification |
| FR-063 | odoo | account.account + l10n_sv_chart | equity measurability + dividends | FV-if-measurable-without-disproportionate-cost else cost−impairment; 3-condition dividends; relief registry 01 FR-012 by id |
| FR-064 | odoo | l10n_sv_chart.impairment | trigger set | incurred-loss ONLY — objective evidence (a)-(e) + adverse environment; NOT ECL (33_ LB-008 contrast note only) |
| FR-065 | odoo | l10n_sv_chart.impairment | scope | equities always individual; significant individual; rest individual-or-grouped by credit-risk characteristics |
| FR-066 | odoo | l10n_sv_chart.impairment | measurement + reversal_cap | PV at ORIGINAL EIR (variable: current contractual); best-estimate-sale for cost items; cap = never-impaired carrying |
| FR-067 | odoo | account.move + l10n_sv_chart.derecognition | asset derecognition | risks-rewards / control-with-unrestricted-sale; retained+liability separation; failed transfer = full asset + liability, no offset |
| FR-068 | odoo | account.move + l10n_sv_chart.derecognition | liability extinguishment | substantial modification (any cause) = extinguish + new; difference incl. non-cash to P&L |
| FR-069 | odoo | report layer (l10n_sv_chart) | category balances + P&L items | six 11.41 categories; EIR interest totals; impairment per class; FV-unavailable facts |
| FR-070 | odoo | report layer + account.move.line | aging + maturity analyses | auto-built from move lines; gross vs impairment split (11.43); contractual UNDISCOUNTED bands (11.43A; default set 11.43B) |
| FR-071 | odoo | report layer + registers | transferred/pledged/default rows | 11.45/11.46/11.47 disclosure feeds from pledge + breach registers |
| FR-072 | odoo | account.move | Part II FV-P&L default | initial FV (normally transaction price); on-demand liability floor; 11.49 exclusions respected |
| FR-073 | odoo | account.account + l10n_sv_chart.fair_value_measurement | unquoted-equity fallback | cost−impairment; last-reliable-FV-becomes-cost; relief registry linked |
| FR-074 | odoo | l10n_sv_chart.hedge_relation + res.company | config gate default OFF | four 11.63 risks; 11.64 whitelist (swaps/forwards only, external, notional match, maturity, no features); documented designation |
| FR-075 | odoo | account.move + hedge_relation | hedge mechanics | FV-type (carrying adjustment) vs CF-type (OCI effective, P&L ineffectivity, reclassification; net-investment never recycled); discontinuation + EIR amortization |
| FR-076 | odoo | l10n_sv_chart.fair_value_measurement | the reusable FV record | exit-price basis; consumed wave-wide and by other files by id |
| FR-077 | odoo | l10n_sv_chart.fair_value_measurement | market_basis | principal else most-advantageous; access; transaction costs excluded; transport-cost characteristic |
| FR-078 | odoo | l10n_sv_chart.fair_value_measurement | best_use_premise | non-financial assets; current-use presumption; consuming files cite by id |
| FR-079 | odoo | l10n_sv_chart.fair_value_measurement | technique | market/cost/income; technique change = estimate change (01 FR-017 by id) |
| FR-080 | odoo | l10n_sv_chart.fair_value_measurement | level 1/2/3 | whole measurement at LOWEST significant input level |
| FR-081 | odoo | report layer | FV disclosures | per-class carrying/level/technique/inputs; recurring L3 reconciliation + tabular; 8.6 judgment feed (01 FR-021 by id) |
| FR-082 | odoo | res.company | functional currency + indicators | D15 snapshot; change only on underlying change (30.14-30.16 basis) |
| FR-083 | odoo | account.move.line + res.currency.rate | spot / average rate basis | transaction-date spot; weekly/monthly average relief; volatility block |
| FR-084 | odoo | account.move.line + payment surfaces | prepayment_date basis | 30.8A hard encoding; per-advance dates; non-monetary — no closing remeasurement; VERSION note: 3rd-ed paragraph (2nd ed: none) with A-option prospective application |
| FR-085 | odoo | account.move.line | closing vs historical/FV-date rates | monetary (sv_coa_monetary=true) at closing; non-monetary cost at transaction rate; FV at FV-date rate |
| FR-086 | odoo | account.move | FX to P&L (+ OCI consistency) | two-clock: CT Art. 62 TAX base only, by id SV-TAX-FR-020 (taxation/01; rate feed = taxation 00_index OQ-006); DT bridge 08 (T8) filename |
| FR-087 | odoo | account.move.line + tag | net-investment OCI | not-planned-not-probable monetary items; OCI in containing FS, never recycled on (partial) disposal; trade never |
| FR-088 | odoo | res.company + account.move | functional change events | prospective; change-date rate; translated non-monetary = new historical costs |
| FR-089 | odoo | report layer + account.move | presentation translation | closing-rate B/S (incl. comparatives); transaction-date P&L (average relief); OCI never recycled; NCI attribution; consolidation surfaces = 07 by id |
| FR-090 | odoo | report layer | FX disclosures | P&L amounts (ex Sección 11 FV instruments); separate-equity amounts; presentation/functional currencies + reason; functional changes |
| FR-091 | odoo | config + report layer | convertibility framework | estimated spot + 30.28/30.29 disclosures; SV default non-triggering (no SV rows invented) |
| FR-092 | odoo | res.company | hyperinflation guard LOCKED OFF | Sec 31 indicators/restatement/cessation behind USD-functional gate; no SV expectation encoded |

Version-regime notes (D12/D15): 3rd-edition paragraphs printed in this
file that are ADDITIONS vs the 2nd (2015) edition per Apéndice A Tabla
A1 — 11.7A, 11.9ZA, 11.11A, 11.13A/11.13B, 11.14A, 11.43A/11.43B,
30.5A, 30.8A, 30.28/30.29 (txt PAGE 325-329) — meaning SV 2025-2027
books still under the 2nd edition (SOQ-48) pre-date some hard encodings
here (notably 30.8A prepaid-consideration and the 11.43A/11.43B maturity
bands); the company-level edition flag and the Tabla A1 delta map are
owned by `08_deferred-tax-adoption.md` by id, and 30.8A carries the
Apéndice A option of prospective application to in-scope preexisting
prepayments. D15 anchors: instrument classification, functional-currency
determination, FV measurements and hedge designations resolve as-of
their own transaction/measurement/designation dates and snapshot on the
record. Mid-year go-live (D18): EIR schedules, impairment history and FV
records ingest as `is_historical` rows with original-period semantics —
tiered ingestion, no re-derivation. No hard gates beyond 11.11A
(no-reclassification) and the 11.64 hedge whitelist (D16 no-override:
never overridden by configuration).

## 6. Acceptance Criteria

- **AC-001:** Given a two-year interest-free loan to a *socio* (partner)
  recognized at inception, when the loan is posted, then it measures at
  the present value of future payments discounted at the market rate for
  a similar debt instrument, an EIR schedule auto-builds in the
  worked-example pattern (opening × EIR − cash = closing), implicit
  interest accrues per period — and any fiscal deemed-dividend retention
  (taxation/05, Ley ISR Art. 74-A) posts as its OWN track linked by id,
  never altering the book PV (FR-061, FR-062).
- **AC-002:** Given trade receivables with mixed due dates and an
  impairment allowance, when the 11.43 disclosure is generated, then the
  aging analysis auto-builds from move lines in the configured bands
  (defaulting to the Norma's five bands), showing gross amortized cost
  and impairment reduction SEPARATELY (FR-070).
- **AC-003:** Given a prepaid USD expense paid to a foreign supplier on
  1 March at the prepayment-date rate, when the expense is consumed on
  30 April, then the expense recognizes at the 1 March prepayment-date
  rate — not the 30 April rate — and the prepaid balance is
  non-monetary: no closing-rate remeasurement ever runs on it, even with
  multiple advances each keeping its own rate (FR-084, FR-085).
- **AC-004:** Given a fair-value measurement whose significant input is
  unobservable (entity data adjusted for market-participant assumptions)
  alongside observable corroborating inputs, when the measurement record
  is saved, then the WHOLE measurement classifies Level 3 — the lowest
  level among significant inputs governs — and recurring Level-3
  disclosures (P&L/OCI location, reconciliation, tabular form) queue
  (FR-080, FR-081).
- **AC-005:** Given an instrument first classified Part I basic at
  initial recognition, when a user later argues the cash flows embed a
  commodity-price exposure, then NO reclassification posts — 11.11A
  blocks any into/out-of-Part-I move after initial recognition; the
  determination record stays immutable (FR-057).
- **AC-006:** Given a receivable impaired in 20X1 whose debtor's credit
  rating improves in 20X2 (an objective post-impairment event), when the
  reversal is posted, then it is capped at the carrying amount that
  would have existed had the impairment never been recognized, posting
  immediately to P&L — and a forward-looking "expected deterioration"
  indicator alone NEVER creates a loss: the trigger set stays
  incurred-loss (FR-064, FR-066).
- **AC-007:** Given a bank loan whose terms are substantially modified
  (maturity extended and rate reset to market), when the modification is
  recorded, then the original liability is extinguished and a NEW
  liability recognized, any difference between old carrying and new
  consideration posting to P&L — never a prospective catch-up on the old
  instrument (FR-068).
- **AC-008:** Given a USD-functional company with USD presentation
  currency holding a EUR-denominated payable, when the period closes,
  then the payable remeasures at the closing rate with the difference to
  P&L — and no presentation-translation OCI arises (presentation =
  functional); the fiscal conversion (CT Art. 62) is computed nowhere in
  this engine (FR-085, FR-086, FR-089).
- **AC-009:** Given any SV company whose functional currency is USD,
  when the Sección 31 surface is probed, then the hyperinflation guard
  stays LOCKED OFF — no indexed restatement, no net-monetary-position
  computation and no hyperinflationary translation variant can run
  (FR-092).
- **AC-010:** Given hedging config at its shipped default (OFF) for an
  SV PYME, when a user attempts to designate an OPTION as a hedge
  instrument, then designation is refused even after enabling config —
  the 11.64 whitelist admits only interest-rate swaps, FX swaps, exchange
  forwards and commodity forwards with matching notional, bounded
  maturity, no prepayment/extension features and an external
  counterparty; once designated, a net-investment hedge's OCI is never
  recycled on partial disposal (FR-074, FR-075).
- **AC-011:** Given financial liabilities across maturities from 20 days
  to 6 years, when the 11.43A disclosure is generated, then the maturity
  analysis shows CONTRACTUAL UNDISCOUNTED cash flows in the remaining
  maturity bands by category — never discounted balances (FR-070).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | Hedging-applicability config note (mandated): Part II hedging (11.60-11.71) is narrow (four risk types; swap/forward-only instruments) and likely RARE for SV PYMES — the engine ships config-gated default OFF (res.company sv_coa_hedging_enabled). No SV instrument in the corpus mandates (or forbids) hedge accounting for PYMES; the 33_ contrast (full NIIF IFRS 9 broad hedge model, ECL — LB-008, EVID-299) is boundary documentation ONLY and is never imported. Implementation review: whether the gate should also require an OQ-signed policy election per company. | no | Takumi S8 (config design) | open |
| OQ-2 | Odoo loan-mapping gaps (mandated): Odoo core has no first-party loan object for partner/shareholder loans — 11.13B PV detection, the EIR schedule engine (FR-062) and interest auto-posting map onto account.move + a new l10n_sv_chart.loan; receivable aging (FR-070) builds on native followup/aging surfaces; prepayment-date rate anchoring (FR-084) extends native multi-currency rate resolution (res.currency.rate is daily — per-advance anchoring needs the sv_coa_prepayment_link). Design decisions at implementation: schedule generation timing, reconciliation with payment allocations, and whether long-term-account receivable auto-posting reuses native deferred-entry surfaces. | no | Takumi S8 (implementation design) | open |
| OQ-3 | SOQ-46 carried: the SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is NOT in the corpus — this file encodes the Norma's instrument/FV/FX machinery as printed with NO invented SV thresholds, markets or rate feeds; every jurisdictional parameter stays company config. Same acquisition as commercial-legal/03 OQ-002 (candidate ≥75). | no | Takumi S8 (sources watch) | open |
| OQ-4 | CT Art. 62 by-id citation RESOLVED (fix round 1): the fiscal FX rule is consumed BY ID as SV-TAX-FR-020 (`sv/requirements/taxation/01_isr-framework.md`: foreign-currency tax bases converted to USD at the hecho-generador-day rate; payment-date FX differences never in the tax base; installment-sale FX differences added to the base) — cited directly in §2 and FR-086; the prior round's premise ("no taxation FR id surfaced") was wrong. Remaining open: (a) the fiscal clock's operational rate-source/feed selection stays in the taxation wave (`00_index.md` OQ-006) and is never back-derived here; (b) book-vs-fiscal bridges route to `08_deferred-tax-adoption.md` (T8) by filename until its FR ids exist (refresh at T8 landing). Partner-loan dual-track ids located: taxation/05_isr-distributions LB-004 (Art. 74-A) / LB-007 (Art. 25). | no | Takumi S8 (cross-file ids) | open |
