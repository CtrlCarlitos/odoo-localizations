# SV — Chart of accounts — Non-financial assets: inventories, PPE, intangibles, impairment, investment property, specialized activities

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file encodes the ACCOUNTING-book engine for the Norma's non-financial
asset clusters (wave cluster N4): *inventarios* (inventories, Sección 13)
with the lower-of-cost-and-NRV measurement, the cost build, the
FIFO|AVG-only cost formulas and the technique set; *propiedades, planta y
equipo* (property, plant and equipment, Sección 17) with component
accounting, the cost build, the per-class cost-OR-revaluation election
with *superávit de revaluación* (revaluation surplus) OCI routing, the
depreciation discipline and disposals; *activos intangibles distintos de
la plusvalía* (intangible assets other than goodwill, Sección 18) with
the recognition gate, the all-internally-generated-expensed rule,
finite-life-always amortization and the *plusvalía* (goodwill) ≤10-year
cap (19.34-19.35); the *deterioro del valor de los activos* (impairment
of assets) engine of Sección 27 — indicators, *importe recuperable*
(recoverable amount), *unidad generadora de efectivo* (cash-generating
unit, CGU) allocation and reversal caps — consumed by every other
cluster in this file; *propiedades de inversión* (investment property,
Sección 16); and the specialized activities of Sección 34 (agriculture
with *plantas productoras* (bearer plants), exploration and evaluation
of mineral resources, and service concessions).

It does **not** cover: the COA/ESF account architecture and the OCI
account set (`02_coa-structure.md`); financial instruments, the
fair-value engine and FX (`03_financial-instruments-fx.md` — its
Sección 12 engine SV-COA-FR-076..081 is consumed BY ID here); the
framework/policy chassis (`01_framework-policies.md` — its
disproportionate-cost registry FR-012, revaluation-switch FR-015 and
estimate-change FR-017 consumed BY ID); liabilities, equity and employee
benefits, including the Sección 21 provision mechanics and the Sección 25
borrowing-cost rule (`05_liabilities-equity-benefits.md`); revenue
(`06_revenue.md`); business combinations and consolidation
(`07_groups-related-parties.md` — the goodwill-recognition machinery
whose output this file amortizes and impairs); deferred tax and
first-time adoption (`08_deferred-tax-adoption.md`, the bridge target).

**Two-track invariant (binding, the wave's spine):** this file owns the
ACCOUNTING book only. The FISCAL book is the taxation wave's asset
register (`taxation/06_isr-assets.md` SV-TAX-FR-150..172 — Art. 30/30-A
rates and mirrors) and the Art. 29-A non-deductible catalog
(`taxation/02_isr-deductions.md` SV-TAX-FR-052 — incl. the 29-A.19
goodwill/marks head of the 29-A.19/22 set), consumed BY ID, never
re-derived and never overridden here; fiscal *castigo* (fiscal
write-off of deteriorated/expired goods) and *mermas* (shrinkage losses)
run on their own fiscal tracks (SV-TAX-FR-052 / SV-TAX-FR-038 by id);
every book-vs-fiscal difference routes through
`08_deferred-tax-adoption.md` (T8) by filename; and the ISR capital-gain
basis — *costo básico* = acquisition cost minus ADMITTED depreciation
(`taxation/03_isr-rates-gains.md` SV-TAX-FR-081 by id) — is NEVER
affected by book revaluation.

## 2. Legal Basis

Authority order (binding, per ruling R29): the operative framework LB =
**32_** — *Norma de Contabilidad NIIF para las PYMES, TERCERA EDICIÓN
(Febrero 2025)*, IFRS Foundation official Spanish translation — cited by
section/párrafo as printed (effective 2027-01-01 with early adoption
permitted, A1; txt PAGE 315). **33_** (EY guide) is SECONDARY-ONLY
authority (never sole LB; where 33_ and 32_ could diverge, 32_ governs
without exception); this file carries no 33_-anchored FR.

**SOQ-46 instrument-gap note (rides every FR in this file and this
wave):** the Norma itself is jurisdiction-neutral on who applies it —
"Las decisiones sobre qué entidades están requeridas o autorizadas a
utilizar las Normas NIIF de Contabilidad completas o la Norma de
Contabilidad NIIF para las PYMES recaen en las autoridades legislativas y
regulatorias y en los emisores de normas de las distintas jurisdicciones"
(Prólogo P12; txt PAGE 22) — and the SV adopting instrument (Consejo de
Vigilancia criteria per CC Arts. 443-444, or successor legislation) is
NOT in the corpus (commercial-legal/03 OQ-002 tracks the same
acquisition). Every hard encoding in this file is therefore the Norma's
own printed rule: NO SV-specific quantitative deviation, threshold or
override is invented — where the corpus is silent the surface stays
config-gap (SOQ-46/SOQ-53 discipline).

**Citation ruling (S8 controller, binding on this file):** the evidence
file's blocks for Sección 16 and the FULL Sección 27 engine are thin —
FRs anchored there cite `32_ + section/párrafo + txt PAGE anchor`
accompanied by the nearest governing EVID id (EVID-286/287/288/289/298);
everywhere else FRs cite the EVID id + section/párrafo normally. PAGE
anchors refer to `sv/.extractions/32_NIIF_PYMES_2025.pdf.txt`.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 13 (inventarios): 13.4 — medirá los inventarios "al importe menor entre el costo y el precio de venta estimado menos los costos de terminación y venta". 13.6-13.7 — costo de compra: precio + "aranceles de importación y otros impuestos (que no sean recuperables posteriormente…)" menos descuentos/rebajas; el elemento de financiación del aplazamiento → gasto por interés, NO costo del inventario. 13.8-13.9 — costo de transformación: costos directos + costos indirectos fijos sistemáticos "sobre la base de la capacidad normal" (capacidad ociosa → gasto; producción anormalmente alta reduce el costo unitario) + variables al uso real. 13.10 — coproductos/subproductos (valor de venta relativo; subproductos inmateriales al VNR deducidos). 13.13 — exclusiones: desperdicios anormales; almacenamiento (salvo proceso de producción necesario); generales administrativas que no llevan a condición/ubicación; costos de venta. 13.14 — productos agrícolas cosechados al valor razonable menos costos de venta en la cosecha = costo desde esa fecha. 13.16 — técnicas: costo estándar, método minorista, precio de compra más reciente. 13.17 — identificación específica para partidas no intercambiables/proyecto específico. 13.19 — "Una entidad medirá el costo… utilizando los métodos de primera entrada primera salida (FIFO) o costo promedio ponderado… El método última entrada primera salida (LIFO) no está permitido en esta Norma." — misma fórmula por clase de naturaleza y uso. 13.22 — revelaciones (política y fórmula; importe en libros; gasto reconocido; deterioros/reversiones; pignorados). Sección 27.2-27.4 — deterioro por partida (o grupo de partidas similares) y reversión limitada a la pérdida original, nuevo importe en libros = menor entre costo y precio de venta revisado | Inventory cost-model contract: lower of cost and NRV (estimated selling price less costs to complete and sell); purchase-cost build with non-recoverable duties/taxes net of discounts and the financing element routed to interest; normal-capacity overhead absorption; joint/sub-products; exclusions; approximation techniques; FIFO or weighted average ONLY — LIFO banned; same formula per nature-and-use class; ag-product harvest FV becomes cost; NRV write-down with capped reversal | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 13, párrs. 13.1-13.22 (txt PAGE 123-127); Sección 27, párrs. 27.2-27.4 (txt PAGE 239-240) (EVID-286) |
| LB-002 | Norma NIIF para las PYMES, Sección 27 Deterioro del Valor de los Activos (cited direct per ruling): 27.2-27.3 — evaluación por partida (o grupo de partidas similares; agrupación por línea/propósito/ubicación geográfica si impracticable por partida); 27.4 — reversión "se limita al importe original de pérdida por deterioro", nuevo importe = menor entre costo y precio revisado; 27.5-27.6 — reducción al importe recuperable, pérdida inmediata en resultados SALVO activo revaluado → decremento de la revaluación (17.15D); 27.7-27.10 — indicios evaluados en cada fecha; externos: (a) caída del valor de mercado significativamente mayor de lo esperable, (b) cambios adversos significativos en el entorno legal/económico/tecnológico/mercado, (c) incremento de tasas que afecte materialmente la tasa de descuento, (d) activos netos en libros > valor razonable estimado de la entidad en conjunto; internos: (e) obsolescencia o deterioro físico, (f) cambios adversos en alcance/manera de uso (activo ocioso, discontinuación/restructuración, disposición antes de lo previsto), (g) informes internos de rendimiento peor que el esperado; el indicio obliga a revisar vida útil/método/valor residual AUNQUE no se reconozca pérdida; 27.11 — importe recuperable = "el mayor entre su valor razonable menos los costos de venta y su valor en uso"; 27.12-27.14 — atajo de medida única + guía de FV de la Sección 12; 27.15-27.21 — VIU: valor presente de flujos de uso continuado + disposición; presupuestos/extrapolación con crecimiento nulo o decreciente; "no incluirán: (a) entradas o salidas de efectivo por actividades de financiación; o (b) cobros o pagos por el impuesto a las ganancias"; flujos al "estado actual" (sin reestructuración futura no comprometida ni mejoras); "la tasa (o tasas) de descuento… será la tasa (o tasas) antes de impuestos"; sin doble contabilización de riesgos; UGE = "el grupo identificable de activos más pequeño que incluye al activo y genera entradas de efectivo que son en gran medida independientes de las entradas procedentes de otros activos o grupos de activos"; pérdida de la UGE — "en primer lugar, se reducirá el importe en libros de cualquier plusvalía distribuida a la unidad" y después proporcional; nunca por debajo del "mayor de: (a) su valor razonable menos los costos de venta…; (b) su valor en uso…; y (c) cero", exceso redistribuido; 27.24-27.27 — la plusvalía no se vende ni genera flujos independientes; la plusvalía adquirida se distribuye desde la fecha de adquisición entre las UGE que se beneficiarán de las sinergias; ajuste a efectos prácticos por participaciones no controladoras; no asignable de forma no arbitraria → entidad adquirida en su totalidad (no integrada) o grupo excluyendo no integradas; 27.28 — "Una pérdida por deterioro del valor reconocida en la plusvalía no se revertirá en los periodos posteriores."; 27.29-27.31 — reversiones (indicios opuestos; tope = importe en libros que habría tenido neto de depreciación/amortización sin la pérdida anterior; P&L salvo activo revaluado → aumento por revaluación 17.15C; UGE: proporcional excepto plusvalía, tope = menor de importe recuperable y costo-no-deteriorado; depreciación futura ajustada); 27.32-27.33 — revelación por clase (inventarios; PPE incl. propiedades de inversión al costo; plusvalía; intangibles distintos de plusvalía; asociadas; ECE) | Impairment engine: assessment at each reporting date on indicators; recoverable amount = max(fair value less costs to sell, value in use); VIU excludes financing and income-tax flows, reflects the asset's current state, discounted at pre-tax rate(s); CGU = smallest identifiable asset group with largely independent cash inflows; CGU loss reduces goodwill first, then pro rata, floored at max(FV−costs to sell, VIU, zero); acquired goodwill allocated to synergy CGUs from acquisition date with NCI practical gross-up and whole-entity fallback; goodwill impairment NEVER reversed; other reversals capped at notional un-impaired carrying, P&L unless revalued (then 17.15C/17.15D); disclosures by asset class | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 27, párrs. 27.1-27.33 (txt PAGE 239-248); nearest governing EVIDs: EVID-286 (27.2-27.4), EVID-287 (17.15C/17.15D routing), EVID-288 (19.34-19.35 + 27.28), EVID-289 (goodwill CGU allocation 27.23-27.27) |
| LB-003 | Norma NIIF para las PYMES, Sección 17 (propiedades, planta y equipo): 17.5-17.7 — cada parte cuyo costo sea significativo respecto al total = componente separado; reposiciones capitalizadas (el componente reemplazado se da de baja — o, si sus libros no lo identifican, se usa el costo de sustitución como indicativo) y costos de inspecciones mayores capitalizados como componente; 17.9-17.14 — costo: precio de compra (honorarios legales/intermediación, aranceles/impuestos no recuperables, neto de descuentos) + costos directamente atribuibles de ubicación/condición + estimación inicial de los costos de desmantelamiento y retiro del elemento y la restauración del sitio; NO son costo: apertura de nuevas instalaciones, introducción de nuevos productos, apertura de nuevas ubicaciones/segmentos (incl. formación), generales administrativas, costos por préstamos (→ Sección 25, gasto); precio equivalente de contado (aplazamiento → valor presente); permuta de activos al valor razonable salvo sin sustancia comercial/FV no fiable en ambos → importe en libros del activo entregado; 17.15-17.15D — por CLASE: (A) costo − depreciación acumulada − deterioro; (B) modelo de revaluación — valor revaluado = FV en la fecha de revaluación − depreciación/deterioro posteriores, mantenido "con suficiente regularidad"; "Si se revalúa un elemento…, todos los elementos… de esa clase se revaluarán"; aumento → OCI superávit de revaluación (salvo reversión de disminución previa en resultados); disminución → resultados salvo saldo de superávit disponible; 17.16 — depreciación por componentes cuando los patrones de consumo difieran significativamente; 17.19-17.21 — depreciación desde disponibilidad para su uso hasta la baja (continúa en ocio salvo totalmente depreciado); vida: uso, desgaste, obsolescencia técnica/comercial (incl. caída futura de precios de venta de lo producido), límites legales/arrendamiento; terrenos sin vida limitada (salvo mineras/canteras/vertederos); valor residual/vida/método = cambios de estimación; 17.22 — métodos lineal, decreciente o basado en el uso; "No es apropiado un método de depreciación que se base en los ingresos de actividades ordinarias"; 17.27-17.29 — baja: ganancia/pérdida en resultados, NO ingresos; fecha de disposición = transferencia del control (23.57-23.61); 17.31-17.33 — revelaciones (bases de medición, métodos, vidas/tasas, bruto + acumulado, conciliación, restricciones/gravados, compromisos, revaluación) | PPE cost-model contract: component recognition with replaced-component derecognition (or substitution-cost proxy) and major-inspection components; cost build including the initial dismantling/removal/site-restoration estimate and the NOT-costs list; cash-equivalent price; asset-exchange measurement; per-CLASS cost OR revaluation model with sufficient-regularity revaluation, class-wide scope and superávit-de-revaluación OCI routing with reversal rules; depreciation from availability to derecognition (idle continues), land not depreciated, life/residual/method as estimate changes, revenue-based method banned; disposal gains/losses as non-revenue P&L; disclosure set | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 17, párrs. 17.1-17.33 (txt PAGE 142-149) (EVID-287) |
| LB-004 | Norma NIIF para las PYMES, Sección 18 (intangibles) + 19.34-19.35 (plusvalía): 18.4 — reconocimiento cuando (a) probabilidad de beneficios, (b) medición fiable del costo/valor, y "(c) el activo no es resultado del desembolso incurrido internamente"; 18.7/19.16 — intangible adquirido por separado (o en combinación de negocios) reconocido si su FV es medible sin costo o esfuerzo desproporcionado, al FV; 18.15-18.16 — "Una entidad reconocerá el desembolso incurrido internamente… como un gasto, incluyendo todos los desembolsos para actividades de investigación y desarrollo, como un gasto cuando incurra en él, a menos que forme parte del costo de otro activo…"; ejemplos gastados: marcas/logotipos generados internamente, listas de clientes, establecimiento/preapertura/lanzamiento, formación, publicidad, reubicación/reorganización, plusvalía generada internamente; anticipos (pagos anticipados) capitalizables; desembolsos de periodos anteriores NUNCA se recapitalizan; 18.19 — "todos los activos intangibles tienen una vida útil finita"; tope contractual/legal + renovaciones solo con evidencia de costo no significativo; 18.20 — "Si la vida útil… no puede establecerse de forma fiable… no superará los diez años."; 18.21-18.22A — amortización desde disponibilidad para su uso; método que refleje el patrón de consumo, lineal como alternativa; PRESUNCIÓN de inadecuación del método basado en ingresos, refutable solo si (a) los derechos se expresan como medida de los ingresos o (b) los ingresos están altamente correlacionados con el consumo; 18.23 — valor residual presumido nulo (compromiso de tercero o mercado activo); 18.24-18.26 — revisiones = cambios de estimación; revelaciones incl. total de R&D gastado; 19.34-19.35 — plusvalía amortizada según 18.19-18.24 con el tope de 10 años, deterioro según Sección 27, no reversible | Intangibles recognition gate (incl. the not-internally-generated condition); ALL internally generated expenditure expensed as incurred — including ALL research and development — unless part of another asset's cost, with capitalizable advances and no later re-capitalization; finite life always with the contractual/legal cap and the 10-year unreliability cap; zero-residual presumption; amortization from availability with linear fallback and the refutable revenue-based presumption; goodwill amortized ≤10 years with non-reversible impairment | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 18, párrs. 18.1-18.29 (txt PAGE 150-155); Sección 19, párrs. 19.34-19.35 (txt PAGE 156-170) (EVID-288) |
| LB-005 | Norma NIIF para las PYMES, Sección 19 (plusvalía — procedencia) + Sección 27.23-27.27 (asignación a UGE): 19.22 — plusvalía = contraprestación transferida (+ PNC + FV de la participación previa en adquisiciones por etapas) − activos netos identificables; 19.14 — PNC "por la parte proporcional… en los importes reconocidos de los activos netos identificables"; 27.23-27.27 — asignación de la plusvalía a las UGE para la comprobación del deterioro (mecánica en LB-002). La mecánica de combinación de negocios es de `07_groups-related-parties.md` por id — nunca reexpuesta aquí | Goodwill provenance (business-combination output, owned by file 07 by id) and its allocation to cash-generating units for impairment testing | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 19 (txt PAGE 156-170); Sección 27, párrs. 27.23-27.27 (txt PAGE 244-245) (EVID-289) |
| LB-006 | Norma NIIF para las PYMES, Sección 16 (propiedades de inversión, cited direct per ruling): 16.1 — "Solo las propiedades de inversión cuyo valor razonable se pueda medir con fiabilidad sin costo o esfuerzo desproporcionado, y en un contexto de negocio en marcha, se contabilizarán de acuerdo con esta sección por su valor razonable con cambios en resultados. Todas las demás propiedades de inversión se contabilizarán utilizando el modelo de costo-depreciación-deterioro del valor de la Sección 17"; 16.2 — definición: terrenos/edificios (o partes) mantenidos por el dueño o un arrendatario bajo arrendamiento financiero para obtener rentas, plusvalías o ambas, y NO para (a) producción/suministro/administración ni (b) venta en el curso ordinario; 16.3 — participación en propiedad mantenida bajo arrendamiento OPERATIVO clasificable como propiedad de inversión "si, y solo si" cumpliese la definición y el FV de la participación fuese medible sin costo o esfuerzo desproporcionado — elección por cada propiedad por separado; 16.3A — juicio activo-vs-combinación de negocios (mecánica 07 por id); 16.4 — uso mixto: separar; si el FV del componente de inversión no es medible sin costo o esfuerzo desproporcionado → todo como PPE (Sección 17); 16.5-16.6 — costo inicial: precio de compra + gastos directamente atribuibles (honorarios legales/intermediación, impuestos por transferencia, costos de transacción); aplazamiento más allá del crédito normal → valor presente; construcción propia según 17.10-17.14; participación arrendada clasificada → importe del párrafo 20.9 (menor entre FV de la propiedad y valor presente de los pagos mínimos) con pasivo equivalente; 16.7 — FV en cada fecha con cambios en resultados (la partida medida es la participación, no la propiedad subyacente; guía Sección 12); todas las demás → modelo del costo de la Sección 17; 16.8 — cuando el FV deje de ser medible sin costo o esfuerzo desproporcionado → Sección 17 (el importe en libros a esa fecha se convierte en costo; cambio de circunstancias, NO de política; revelación 16.10(c)(iii)); 16.9 — fuera de ese caso, transferencias hacia/desde la categoría SOLO por cambio de uso con evidencia; 16.10-16.11 — revelaciones para las de FV: (a) [eliminado, como impreso]; (b) extensión en que el FV se basa en tasación de tasador independiente cualificado con experiencia reciente en la zona/categoría (o revelar su ausencia); (c) restricciones; (d) obligaciones contractuales de adquisición/construcción/desarrollo o reparación/mantenimiento/mejora; (e) conciliación del importe en libros inicio→fin con (i) adiciones (separando combinaciones de negocios), (ii) ajustes netos al FV, (iii) transferencias hacia/desde el modelo del costo, (iv) traspasos hacia/desde inventarios y propiedades ocupadas por el propietario, (v) otros cambios — sin comparativos; más las revelaciones de arrendador/arrendatario de la Sección 20 | Investment property: fair-value model ONLY when reliably measurable without disproportionate cost in a going-concern context, else Sección 17 cost model; leasehold (operating-lease interest) per-property classification; mixed-use split with PPE fallback; initial cost build incl. the 20.9 leasehold amount; transfers on change of use only (plus the FV-unavailability fallback, a circumstance change not a policy change); disclosure set incl. appraiser extent and the carrying reconciliation | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 16, párrs. 16.1-16.11 (txt PAGE 138-141); nearest governing EVIDs: EVID-287 (Sección 17 fallback model), EVID-298 (disproportionate-cost kin) |
| LB-007 | Norma NIIF para las PYMES, Sección 34 (actividades especializadas): 34.1-34.2B — política contable por clase de activos biológicos: modelo del FV (34.4-34.7) cuando el FV sea "fácilmente determinable sin un costo o esfuerzo desproporcionado", modelo del costo (34.8-34.10) para los demás; NO aplica a las plantas productoras que "puedan medirse por separado de los productos de éstas sin costos o esfuerzos desproporcionados" (inicial y continuamente) → Sección 17 PPE; PERO la sección aplica a los productos de esas plantas; si no medibles por separado → la planta entera bajo esta sección; ejemplos de plantas que NO son productoras: cultivadas para cosecharse como productos agrícolas (madera/fruto-madera) y cosecha anual (maíz, trigo); 34.3 — reconocimiento (control por sucesos pasados + beneficios probables + FV o costo medible sin costo/esfuerzo desproporcionado); 34.4-34.7 — modelo FV: FV menos costos de venta en el reconocimiento y en cada fecha, cambios en resultados; "Los productos agrícolas cosechados o recolectados… se medirán a su valor razonable menos los costos de venta en el punto de cosecha o recolección. Esta medición será el costo a esa fecha"; guía Sección 12; revelaciones (descripción de clases; conciliación con cambios de FV, compras, cosecha, combinaciones, conversión de moneda, otros — sin comparativos); 34.8-34.10 — modelo del costo: costo − depreciación acumulada − deterioro acumulado; productos cosechados igualmente al FV−costos en la cosecha = costo; revelaciones (por qué el FV no es medible sin costo/esfuerzo desproporcionado, método de depreciación, vidas/tasas, bruto + acumulado + deterioro); 34.11-34.11G — exploración y evaluación: política que especifique qué desembolsos son activos de E&E "de acuerdo con el párrafo 10.4", exenta del 10.5; ejemplos (derechos de exploración, estudios topográficos/geológicos/geoquímicos/geofísicos, perforaciones exploratorias, zanjas/trincheras, muestras, factibilidad técnica/viabilidad comercial); el desarrollo NO es E&E; costo en el reconocimiento, luego Sección 17/18 según su naturaleza, desmantelamiento/restauración según 17 y 21; deterioro según Sección 27 SALVO que para estos activos los hechos/circunstancias del 34.11E reemplazan los indicios de 27.7-27.10: (a) derecho de exploración expirado o por expirar sin renovación esperada, (b) sin desembolsos significativos presupuestados/planificados de E&E posterior en el área, (c) sin descubrimiento de cantidades comercialmente viables y decisión de interrumpir, (d) desarrollo probable pero recuperación completa del importe en libros improbable; política de asignación a UGE o grupos de UGE (34.11F); clase separada de activos + revelaciones de 17/18 congruentes (34.11G); 34.12-34.16 — concesiones de servicios: definición (concedente controla/regula servicios, destinatarios, precios, participación residual); modelo activo financiero — derecho contractual incondicional a efectivo u otro activo financiero → reconocer al FV, luego Sección 11; modelo activo intangible — derecho de cobrar a los usuarios (condicionado al uso) → FV inicial, luego Sección 18; contrato mixto en la medida de la garantía incondicional; ingresos de los servicios según Sección 23 | Specialized activities: bearer plants out of agriculture into PPE when separately measurable without disproportionate cost; biological assets FV or cost model per class with the harvest-point FV becoming produce cost; E&E expenditure-recognition policy choice with its own impairment triggers and separate-asset class; service concessions as financial asset vs intangible by the unconditional-cash-right test | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 34, párrs. 34.1-34.16 (txt PAGE 301-306) (EVID-298) |

## 3. Functional Requirements

### 3.1 Inventories (Sección 13)

- **SV-COA-FR-093:** The system shall measure inventories at the LOWER OF
  cost and *precio de venta estimado menos los costos de terminación y
  venta* (estimated selling price less costs to complete and sell — net
  realizable value, NRV) at every reporting date, on a per-item basis (or
  group of similar items when item-level assessment serves), any
  write-down being an impairment loss recognized immediately in profit or
  loss per the Sección 27 NRV engine (FR-098).
  (LB-001; EVID-286)
- **SV-COA-FR-094:** The system shall build purchase cost as the purchase
  price plus import duties and other taxes that are NOT subsequently
  recoverable, NET of trade discounts and rebates — and shall route the
  financing element of deferred payment (the excess over the normal-credit
  cash price) to interest expense, NEVER into inventory cost (13.6-13.7;
  the Sección 30 FX clock on the same deferred balances is owned by
  `03_financial-instruments-fx.md` by id).
  (LB-001; EVID-286)
- **SV-COA-FR-095:** The system shall build transformation cost as direct
  costs plus the systematic allocation of fixed production overheads ON A
  NORMAL-CAPACITY basis — idle-capacity cost expensed as incurred,
  abnormally-high production periods reducing unit cost so that inventory
  is never carried above cost — plus variable overheads at actual use;
  shall allocate joint costs to joint products by relative sales value
  (immaterial by-products at NRV deducted from cost); and shall EXCLUDE
  from cost: abnormal waste, storage costs unless necessary in the
  production process, administrative overheads that do not bring inventory
  to its condition and location, and selling costs (13.8-13.10, 13.13).
  (LB-001; EVID-286)
- **SV-COA-FR-096:** The system shall offer ONLY the FIFO (*primera
  entrada primera salida*) and weighted-average (*costo promedio
  ponderado*) cost formulas — "El método última entrada primera salida
  (LIFO) no está permitido en esta Norma" (13.19): any LIFO-style
  configuration is REJECTED at validation; and shall enforce the SAME
  formula for all inventories of a class with similar nature and use (the
  class scope recorded on the inventory-class record), with specific
  identification reserved for non-interchangeable items or
  project-specific inventories (13.17).
  (LB-001; EVID-286)
- **SV-COA-FR-097:** The system shall support the cost-approximation
  techniques of 13.16 — standard cost, the retail method and the
  most-recent-purchase-price method — flagged as approximation techniques
  subject to the same lower-of-cost/NRV rule; and shall implement the
  agricultural bridge: agricultural produce harvested from biological
  assets is measured at fair value less costs to sell AT THE POINT OF
  HARVEST, and that measurement becomes its COST from that date (13.14;
  the harvest event is consumed from FR-132 by id).
  (LB-001; EVID-286)
- **SV-COA-FR-098:** The system shall implement the inventory NRV
  impairment-and-reversal engine (27.2-27.4): assessment at each
  reporting date by item or group of similar items (grouping by product
  line with similar purpose or end use produced and marketed in the same
  geographic area when item-level determination is impracticable);
  write-down recognized immediately in profit or loss; at each later date
  a fresh assessment, and when the circumstances that caused the
  impairment cease or clear evidence of an NRV increase exists, the loss
  is REVERSED limited to the original impairment amount, so the new
  carrying amount is the LOWER of cost and the revised NRV.
  (LB-001; EVID-286)
- **SV-COA-FR-099:** The system shall keep the book-vs-fiscal tracks of
  inventory losses separate (two-track invariant): the BOOK NRV engine of
  FR-093..098 computes the accounting write-down/reversal only; the
  FISCAL deductibility of deterioration/expired-goods losses (*castigo*)
  and *mermas* (shrinkage) — including the D.L. 345-2019 documentation
  gate — is owned by the taxation wave BY ID
  (`taxation/02_isr-deductions.md` SV-TAX-FR-052 and SV-TAX-FR-038),
  never re-derived here; where the book NRV and the fiscal
  castigo/merma amounts differ, the system records the difference and
  routes the bridge through `08_deferred-tax-adoption.md` (T8) by
  filename.
  (LB-001; EVID-286 — fiscal tracks by id: SV-TAX-FR-052/SV-TAX-FR-038)
- **SV-COA-FR-100:** The system shall emit the inventory disclosures of
  13.22: the accounting policies adopted for inventory measurement
  INCLUDING the cost formula used; total carrying amount classified as
  appropriate for the entity; the amount of inventories recognized as
  expense in the period; impairment losses recognized or reversed in
  profit or loss per Sección 27; and the total carrying amount of
  inventories pledged as collateral (*pignorados*).
  (LB-001; EVID-286)

### 3.2 Property, plant and equipment (Sección 17)

- **SV-COA-FR-101:** The system shall implement PPE component accounting:
  each part of an item whose cost is significant relative to the item's
  total cost is accounted for as a separate component and depreciated per
  its own consumption pattern (17.5, 17.16); the purchase or construction
  of a REPLACEMENT is recognized as the acquisition of an asset while the
  carrying amount of the component replaced is derecognized regardless of
  its age — or, where the replaced component cannot be identified in the
  books, the cost of the replacement is used as the indicative
  substitution-cost proxy for what the replaced part had cost; the cost
  of a MAJOR INSPECTION is capitalized as a component, with any remaining
  inspection-component carrying derecognized when it occurs (17.5-17.7).
  (LB-003; EVID-287)
- **SV-COA-FR-102:** The system shall build PPE cost at initial
  recognition as: the cash-equivalent purchase price plus directly
  attributable expenditure (legal and broker fees, non-recoverable
  tariffs and taxes, net of discounts) plus costs of bringing the asset
  to location and working condition, PLUS the initial estimate of
  dismantling, removal and site-restoration obligations (the Sección 21
  provision surface owned by `05_liabilities-equity-benefits.md` by id) —
  and shall EXCLUDE from cost: costs of opening a new facility,
  introducing a new product or service, commencing business in a new
  location or with a new class of customer (including staff training),
  administration and general overheads, and borrowing costs (expensed per
  Sección 25.2 — all borrowing costs expensed under this Norma; surface
  owned by file 05 by id); deferred payment beyond normal credit terms
  measures at present value (17.9-17.14).
  (LB-003; EVID-287)
- **SV-COA-FR-103:** The system shall measure asset exchanges (*permuta*)
  at the fair value of the assets received UNLESS the exchange lacks
  commercial substance or the fair value of neither the asset received
  nor the asset given is reliably measurable — then at the carrying
  amount of the asset given up; fair-value measurement per the Sección 12
  engine consumed from SV-COA-FR-076..081 by id (17.12-17.14).
  (LB-003; EVID-287)
- **SV-COA-FR-104:** The system shall implement the subsequent
  measurement of each PPE CLASS under exactly one of two models — (A) the
  cost model: cost less accumulated depreciation less accumulated
  impairment; or (B) the REVALUATION model: the *valor revaluado*
  (revalued amount) = fair value at the revaluation date less subsequent
  accumulated depreciation and impairment, revaluations kept sufficiently
  regular ("con suficiente regularidad") so the carrying amount does not
  differ materially from fair value — with CLASS-WIDE scope: when an item
  is revalued, ALL items of that class are revalued (17.15-17.15B); a
  revaluation INCREASE goes to OCI as *superávit de revaluación*
  (revaluation surplus) in equity — the equity class and OCI routing
  being accounts owned by `02_coa-structure.md` by id — EXCEPT to the
  extent it reverses a revaluation decrease of the same asset previously
  recognized in profit or loss; a revaluation DECREASE is charged to
  profit or loss EXCEPT to the extent a revaluation-surplus balance is
  available for that same asset/class (17.15C-17.15D); the first-time
  cost→revaluation switch for a class posts PROSPECTIVELY per 10.10A
  (consumed from SV-COA-FR-015 by id — never a retrospective
  restatement); the fiscal register is unaffected (FR-108).
  (LB-003; EVID-287)
- **SV-COA-FR-105:** The system shall depreciate each PPE component from
  the date it is available for use until the date it is derecognized —
  depreciation CONTINUES while an asset is idle or temporarily out of
  use (unless fully depreciated); LAND with unlimited life is not
  depreciated (except land treated as mines, quarries or landfill);
  useful life reflects expected usage, wear and tear, technical or
  commercial obsolescence (including the future selling-price decline of
  the items the asset produces) and legal or similar limits on use;
  residual value, useful life and the depreciation method are reviewed at
  each reporting date as ESTIMATE changes applied prospectively
  (consumed from SV-COA-FR-017 by id); the method catalog is linear,
  diminishing-balance or usage-based ONLY — "No es apropiado un método de
  depreciación que se base en los ingresos de actividades ordinarias"
  (17.22): a revenue-based depreciation method is REJECTED at validation
  (17.19-17.23).
  (LB-003; EVID-287)
- **SV-COA-FR-106:** The system shall derecognize a PPE item on disposal
  or when no future economic benefits are expected from its use or
  disposal, any gain or loss (net disposal proceeds minus carrying
  amount) being recognized in PROFIT OR LOSS as a NON-REVENUE item —
  never within *ingresos de actividades ordinarias* (revenue) — the
  disposal date being the date control transfers per 23.57-23.61
  (consumed from `06_revenue.md` by id) (17.27-17.29).
  (LB-003; EVID-287)
- **SV-COA-FR-107:** The system shall emit the PPE disclosures of
  17.31-17.33: the measurement bases used for each class; depreciation
  methods; useful lives or depreciation rates; gross carrying amount and
  accumulated depreciation (plus accumulated impairment, and revalued
  amounts where the revaluation model applies) at the beginning and end
  of the period; a reconciliation of carrying amount by class (additions,
  disposals, revaluations, depreciation, impairment losses and
  reversals); restrictions on title and items pledged as collateral; and
  contractual commitments for the acquisition of property, plant and
  equipment — plus, under the revaluation model, its disclosures
  (valuation date and whether an independent qualified appraiser was
  involved, carrying amounts at fair value vs the cost-model basis).
  (LB-003; EVID-287)
- **SV-COA-FR-108:** The system shall keep the PPE two-track invariant:
  the FISCAL book is the taxation wave's asset register
  (`taxation/06_isr-assets.md` SV-TAX-FR-150..172 by id — Art. 30 fixed
  percentages 5/20/25/50 and Art. 30-A software 25%, no fiscal
  revaluation, no catch-up of missed quotas, no percentage change without
  *Administración Tributaria* authorization); book depreciation computed
  under FR-101..107 NEVER overrides the fiscal quota and vice versa; the
  ISR capital-gain basis remains *costo básico* = acquisition cost minus
  ADMITTED depreciation (SV-TAX-FR-081 by id) — UNAFFECTED by any book
  revaluation surplus under FR-104; and all book-vs-fiscal differences
  (rates, revaluation, idle-time depreciation, component lives) route
  through `08_deferred-tax-adoption.md` (T8) by filename, never
  re-derived here.
  (LB-003; EVID-287 — fiscal tracks by id: SV-TAX-FR-150..172,
  SV-TAX-FR-081)

### 3.3 Intangible assets and goodwill (Sección 18 + 19.34-19.35)

- **SV-COA-FR-109:** The system shall implement the intangible
  recognition gate (18.4): an identifiable non-monetary asset without
  physical substance is recognized as an intangible ONLY when (a) future
  economic benefits are probable, (b) the cost or value is measured
  reliably, AND (c) the asset is NOT the result of internally incurred
  expenditure — condition (c) barring internally generated intangibles
  from the recognition gate entirely (their treatment is FR-110); a
  separately acquired intangible — including one acquired in a business
  combination — is recognized when its fair value is measurable without
  disproportionate cost, at fair value as its cost (18.7, 19.16; the
  combination mechanics are owned by `07_groups-related-parties.md` by
  id).
  (LB-004; EVID-288)
- **SV-COA-FR-110:** The system shall recognize internally incurred
  expenditure as an EXPENSE when incurred — "incluyendo todos los
  desembolsos para actividades de investigación y desarrollo" (ALL
  research and development outlays) — unless it forms part of the cost of
  another asset under this Norma (18.15-18.16); the expense guard blocks
  capitalization of the Norma's worked set: internally generated *marcas*
  (brands) and logotypes, customer lists, establishment/pre-opening and
  launch costs, staff training, advertising and promotion, relocation and
  reorganization costs, and internally generated goodwill; ADVANCES
  (prepayments) for goods or services not yet received ARE capitalizable
  as assets; and expenditure expensed as internally incurred in PRIOR
  periods shall NEVER be re-capitalized later as an intangible.
  (LB-004; EVID-288)
- **SV-COA-FR-111:** The system shall treat ALL intangibles as
  finite-lived (18.19): useful life defaults to the contractual or legal
  life cap, extended for renewal periods ONLY when there is evidence the
  entity can renew without significant cost; when the useful life cannot
  be established reliably it SHALL NOT EXCEED TEN YEARS (18.20); and the
  residual value is PRESUMED ZERO unless an active market exists for the
  asset or a third party is committed to buy it at the end of its life
  (18.23).
  (LB-004; EVID-288)
- **SV-COA-FR-112:** The system shall amortize intangibles from the date
  the asset is available for use, using a method reflecting the expected
  consumption pattern of the economic benefits — with the LINEAR method
  as the fallback — and shall carry the 18.22A PRESUMPTION that a
  revenue-based amortization method is inappropriate, refutable ONLY with
  a recorded justification that (a) the rights attached to the asset are
  expressed as a measure of revenue or (b) revenue is highly correlated
  with the total consumption of the economic benefits embedded in the
  asset; reviews of useful life, residual value and method are estimate
  changes applied prospectively (consumed from SV-COA-FR-017 by id;
  18.21-18.26).
  (LB-004; EVID-288)
- **SV-COA-FR-113:** The system shall carry goodwill ONLY as the output
  of a business combination (recognition mechanics owned by
  `07_groups-related-parties.md` by id) and amortize it per the Sección
  18 machinery of FR-111..112 SUBJECT TO the ≤10-year cap when its life
  is not reliably determinable (19.34-19.35), with impairment tested and
  measured per the Sección 27 engine (FR-116..124) — a goodwill
  impairment loss is NEVER reversed (27.28).
  (LB-004; LB-005; EVID-288/289)
- **SV-COA-FR-114:** The system shall emit the intangible disclosures:
  for each class of intangibles, the accounting policies, gross carrying
  amount and accumulated amortization at the beginning and end of the
  period, the reconciliation (additions, impairments and reversals,
  amortization, disposals), useful lives or amortization rates — and the
  AGGREGATE amount of research and development expenditure recognized as
  expense in the period.
  (LB-004; EVID-288)
- **SV-COA-FR-115:** The system shall keep the intangibles two-track
  invariant: the FISCAL treatment — goodwill (*derechos de llave*) and
  marks amortization NON-deductible per the Art. 29-A catalog
  (`taxation/02_isr-deductions.md` SV-TAX-FR-052 numeral 19, by id) and
  software amortized under the Art. 30-A 25% regime
  (`taxation/06_isr-assets.md` SV-TAX-FR-165/166 by id) — is consumed by
  id and never re-derived; the book engine (finite-always, ≤10-year cap,
  ALL R&D expensed) computes the accounting amortization only; every
  book-vs-fiscal difference (software book life ≠ 25%, blocked
  goodwill/marks, expensed R&D) is recorded as a temporary difference
  and routed through `08_deferred-tax-adoption.md` (T8) by filename.
  (LB-004; EVID-288 — fiscal tracks by id: SV-TAX-FR-052,
  SV-TAX-FR-165/166)

### 3.4 Impairment engine (Sección 27)

- **SV-COA-FR-116:** The system shall implement the Sección 27 impairment
  engine for ALL assets except those other sections govern: deferred-tax
  assets (Sección 29 — `08_deferred-tax-adoption.md` by filename),
  employee-benefit assets (Sección 28 — file 05 by id), financial assets
  within Sección 11 (`03_financial-instruments-fx.md` by id), investment
  property measured at fair value (FR-125..129), biological assets at
  fair value less costs to sell (FR-130..132), and contract assets and
  costs-to-fulfil under 23.70 (`06_revenue.md` by id); inventory
  impairment runs on its NRV variant (FR-098; 27.2-27.4) inside this
  same engine's disclosure surface.
  (LB-002: 32_ Sec 27, párr. 27.1, txt PAGE 239; EVID-286/287/288/289
  nearest)
- **SV-COA-FR-117:** The system shall assess, at each reporting date,
  whether ANY indicator of impairment exists for an asset — EXTERNAL
  sources: (a) the asset's market value declined significantly more than
  expected from the passage of time or normal use; (b) significant
  adverse changes occurred or are imminent in the legal, economic,
  technological or market environment of the entity or of the asset's
  market; (c) market interest or investment rates increased and will
  probably affect materially the discount rate used for value in use;
  (d) the entity's net carrying amount exceeds its estimated fair value
  as a whole; INTERNAL sources: (e) evidence of obsolescence or physical
  deterioration; (f) significant adverse changes in the extent or manner
  of the asset's use or expected use — including the asset becoming
  IDLE, plans to discontinue or restructure the operation it belongs to,
  and plans to dispose of it before the previously expected date; (g)
  internal reporting evidence that economic performance is or will be
  worse than expected; when an indicator exists the recoverable amount is
  estimated, and even where no impairment ends up recognized the
  indicator triggers a review of remaining useful life,
  depreciation/amortization method and residual value as estimate
  changes; with NO indicator, no recoverable estimate is required.
  (LB-002: 32_ Sec 27, párrs. 27.7-27.10, txt PAGE 240-241;
  EVID-287/288 nearest)
- **SV-COA-FR-118:** The system shall measure the *importe recuperable*
  (recoverable amount) of an asset as the HIGHER of its fair value less
  costs to sell and its value in use — fair-value measurement per the
  Sección 12 engine consumed from SV-COA-FR-076..081 by id, less
  disposal costs; where either amount exceeds the carrying amount the
  asset is not impaired and the other need not be estimated; where no
  reason exists to believe value in use significantly exceeds fair value
  less costs to sell, the latter is the recoverable amount (frequently
  the case for an asset held for disposal); when the individual asset's
  recoverable amount cannot be estimated, it is estimated for the
  cash-generating unit to which the asset belongs.
  (LB-002: 32_ Sec 27, párrs. 27.11-27.14, txt PAGE 241-242; EVID-286
  nearest)
- **SV-COA-FR-119:** The system shall compute value in use as the present
  value of the future cash flows the entity expects to obtain from the
  asset — continuing-use inflows and the directly attributable or
  reasonably-and-consistently allocated outflows needed to generate
  them, plus the net disposal flows at the end of useful life —
  reflecting expected flows, variability expectations, the time value of
  money, a price for the uncertainty inherent in the asset and other
  market factors such as illiquidity, based on recent budgets/forecasts
  with extrapolation at a ZERO-OR-DECREASING growth rate unless an
  increasing rate is justified; the flow projections shall EXCLUDE
  inflows/outflows from FINANCING activities and income-TAX
  collections/payments (27.19); shall reflect the asset's CURRENT state
  — excluding estimated flows from future restructurings to which the
  entity is not yet committed and from future enhancements or
  improvements of the asset's performance (27.20); and the discount
  rate(s) shall be PRE-TAX, reflecting current market assessments of the
  time value of money and of the asset-specific risks for which the flow
  estimates have not been adjusted, with no double counting of risks
  (27.21 area).
  (LB-002: 32_ Sec 27, párrs. 27.15-27.21, txt PAGE 242-243; EVID-287
  nearest)
- **SV-COA-FR-120:** The system shall recognize an impairment loss when,
  and only when, the recoverable amount is below the carrying amount —
  reducing the carrying amount to the recoverable amount immediately in
  profit or loss — EXCEPT that for an asset carried at a revalued amount
  under the Sección 17 revaluation model the loss is treated as a
  REVALUATION DECREASE per 17.15D (surplus-first routing through the
  *superávit de revaluación*, FR-104), never through profit or loss
  while a surplus balance is available (27.5-27.6).
  (LB-002: 32_ Sec 27, párrs. 27.5-27.6, txt PAGE 240; EVID-287 nearest)
- **SV-COA-FR-121:** The system shall implement the cash-generating unit
  machinery: a CGU is the smallest identifiable group of assets that
  includes the asset and generates cash inflows largely INDEPENDENT of
  the inflows from other assets or groups; a CGU impairment loss is
  recognized when, and only when, the unit's recoverable amount is below
  its carrying amount, and is allocated to reduce the carrying amounts of
  the unit's assets IN ORDER: (a) FIRST against any GOODWILL allocated
  to the unit, and (b) then pro rata on the carrying amount of each
  other asset — with per-asset FLOORS: no asset is reduced below the
  HIGHEST of its fair value less costs to sell (if determinable), its
  value in use (if determinable) and ZERO, any undistributable excess
  being redistributed pro rata among the unit's other assets
  (27.8, 27.21-27.23).
  (LB-002: 32_ Sec 27, párrs. 27.8 y 27.21-27.23, txt PAGE 240 y 244;
  EVID-289 nearest (27.23-27.27))
- **SV-COA-FR-122:** The system shall implement goodwill-CGU testing:
  goodwill (alone unsellable, its fair value only derivable from the
  CGUs it belongs to) acquired in a business combination is allocated
  FROM THE ACQUISITION DATE to each CGU expected to benefit from the
  combination's synergies, regardless of whether other assets or
  liabilities of the acquiree are assigned to those units; for a
  partly-owned unit, the unit's carrying amount is grossed up for
  practical purposes with the goodwill attributable to the
  *participaciones no controladoras* (non-controlling interests) before
  comparison with recoverable amount; and where goodwill cannot be
  allocated to individual CGUs (or groups) on a non-arbitrary basis, it
  is tested by determining the recoverable amount of the acquiree AS A
  WHOLE (when not integrated) or of the whole group of entities
  excluding any unintegrated ones (27.24-27.27; the combination-side
  allocation input is consumed from `07_groups-related-parties.md` by
  id).
  (LB-002: 32_ Sec 27, párrs. 27.24-27.27, txt PAGE 244-245; LB-005;
  EVID-289 (27.23-27.27))
- **SV-COA-FR-123:** The system shall implement impairment reversals: a
  loss recognized on GOODWILL is NEVER reversed in later periods
  (27.28); for every other asset, at each reporting date the system
  assesses whether indicators exist that a previously recognized loss
  has decreased or ceased (generally the opposites of the 27.9
  indicators) and, when they exist, increases the carrying amount to the
  recoverable amount CAPPED at the carrying amount that would have been
  determined (net of depreciation or amortization) had no impairment
  loss been recognized in prior years — the reversal recognized
  immediately in profit or loss, EXCEPT that for an asset carried at a
  revalued amount under 17.15B the reversal is treated as a REVALUATION
  INCREASE per 17.15C (OCI routing, FR-104); for CGU-based losses the
  reversal is allocated to the unit's assets PRO RATA — never to
  goodwill — capped per asset at the LOWER of its recoverable amount and
  its notional un-impaired carrying; after any reversal, future
  depreciation/amortization is adjusted to spread the revised carrying
  amount less residual value over the remaining useful life
  (27.29-27.31).
  (LB-002: 32_ Sec 27, párrs. 27.28-27.31, txt PAGE 245-247; EVID-288
  (27.28) / EVID-287 (17.15C/17.15D) nearest)
- **SV-COA-FR-124:** The system shall emit the impairment disclosures of
  27.32-27.33: for EACH class of assets, the amount of impairment losses
  recognized in profit or loss during the period AND the line item(s) of
  the comprehensive-income (and income) statement where they are
  included, and likewise the amounts of reversals — the classes being:
  inventories; property, plant and equipment (including investment
  property accounted for under the cost model); goodwill; intangibles
  other than goodwill; investments in associates; and investments in
  jointly controlled entities. Fiscal two-track note: book impairment
  and its reversal are ACCOUNTING events only — the fiscal castigo
  deductibility tracks run per SV-TAX-FR-052 by id, differences routed
  to T8.
  (LB-002: 32_ Sec 27, párrs. 27.32-27.33, txt PAGE 247-248; EVID-286
  nearest — fiscal track by id: SV-TAX-FR-052)

### 3.5 Investment property (Sección 16)

- **SV-COA-FR-125:** The system shall classify investment property —
  land or buildings (or parts of either) held by the owner or by a
  lessee under a finance lease to earn rentals or appreciation, and NOT
  for use in production or supply of goods or services, administrative
  purposes, or sale in the ordinary course of business — as its own
  asset category; an interest in a property held by a LESSEE under an
  OPERATING lease MAY be classified and accounted for as investment
  property if, and only if, the interest would otherwise meet the
  definition and its fair value could be measured without disproportionate
  cost or effort, the election being available property by property
  (16.2-16.3); mixed-use property is SPLIT between the investment
  component and owner-occupied PPE — and where the investment
  component's fair value cannot be measured reliably without
  disproportionate cost, the WHOLE property is accounted for as PPE
  under Sección 17 (16.4); the asset-vs-business determination for a
  property acquisition (16.3A) is consumed from
  `07_groups-related-parties.md` by id.
  (LB-006: 32_ Sec 16, párrs. 16.1-16.4, txt PAGE 138-139; EVID-287
  nearest)
- **SV-COA-FR-126:** The system shall measure investment property at
  COST on initial recognition: purchase price plus directly attributable
  transaction costs (legal and broker fees, property-transfer taxes and
  other transaction costs); where payment is deferred beyond normal
  credit terms, cost is the present value of all future payments
  (cash-equivalent price); self-constructed property per 17.10-17.14
  (FR-102); and a leased interest classified as investment property is
  recognized at the Sección 20 finance-lease amount — the LOWER of the
  property's fair value and the present value of the minimum lease
  payments — with an equivalent liability (16.5-16.6; the Sección 20
  lease engine is consumed by id, not restated here).
  (LB-006: 32_ Sec 16, párrs. 16.5-16.6, txt PAGE 139; EVID-287
  nearest)
- **SV-COA-FR-127:** The system shall measure at FAIR VALUE at every
  reporting date, with changes recognized in profit or loss, ONLY those
  investment properties whose fair value can be measured reliably
  WITHOUT disproportionate cost or effort, in a going-concern context —
  the measured item being the leasehold INTEREST where the holder is a
  lessee, not the underlying property; ALL other investment property is
  accounted for under the Sección 17 cost-depreciation-impairment model
  (16.1, 16.7); fair-value measurement per the Sección 12 engine
  consumed from SV-COA-FR-076..081 by id; and every fallback to the cost
  model on disproportionate-cost grounds feeds the
  disproportionate-cost relief registry consumed from SV-COA-FR-012 by
  id (the fact-and-reasons disclosure; the judgment remade at each
  subsequent measurement date).
  (LB-006: 32_ Sec 16, párrs. 16.1 y 16.7, txt PAGE 138-139; EVID-287
  nearest; 01-file SV-COA-FR-012 by id)
- **SV-COA-FR-128:** The system shall transfer a property into or out of
  the investment-property category ONLY on a CHANGE OF USE with evidence
  — the property starting or ceasing to meet the definition (owner
  occupancy, commencement of development for sale, end of owner
  occupancy or of development, commencement or end of occupation by a
  finance lessee) — PLUS the single measurement-driven fallback: when a
  reliable fair-value measure CEASES to be available without
  disproportionate cost for an item under the fair-value model, the item
  is accounted for prospectively under Sección 17, its carrying amount
  at that date becoming its DEEMED COST, until reliable fair-value
  measurement again becomes available; this fallback is a CHANGE OF
  CIRCUMSTANCES, not an accounting-policy change, and its disclosure
  rides FR-129's set (16.8-16.9).
  (LB-006: 32_ Sec 16, párrs. 16.8-16.9, txt PAGE 139-140; EVID-287
  nearest)
- **SV-COA-FR-129:** The system shall emit the investment-property
  disclosures (16.10-16.11) for fair-value-model properties: the extent
  to which fair value is based on a valuation by an INDEPENDENT
  professionally-qualified appraiser with recent experience in the
  location and category of the property — or, where no such valuation
  took place, disclosure of that fact; the existence and amounts of
  restrictions on realizability, on collection of rental income or of
  proceeds from disposal; contractual obligations to purchase,
  construct or develop investment property or for repairs, maintenance
  or enhancements; and a CARRYING-AMOUNT RECONCILIATION from the
  beginning to the end of the period showing separately (i) additions
  (with those from business combinations shown separately), (ii) net
  fair-value adjustment gains or losses, (iii) transfers to and from the
  cost model (16.8), (iv) transfers to and from inventories and
  owner-occupied property, and (v) other changes — comparative-period
  reconciliation NOT required; plus the Sección 20 lessor and lessee
  disclosures for the leases it participates in (16.11; lease surface
  consumed by id).
  (LB-006: 32_ Sec 16, párrs. 16.10-16.11, txt PAGE 140-141; EVID-287
  nearest)

### 3.6 Specialized activities (Sección 34)

- **SV-COA-FR-130:** The system shall classify *plantas productoras*
  (bearer plants) OUT of the agriculture engine and INTO PPE under
  Sección 17 (FR-101..108) when, at initial recognition, they can be
  measured SEPARATELY from the produce they contain, both initially and
  continuously, without disproportionate cost or effort; where they
  cannot be so measured, the agriculture engine applies to the plant as
  a whole; the PRODUCE of bearer plants always remains within the
  agriculture engine until harvest (34.1-34.2B); plants cultivated to be
  harvested as agricultural produce (e.g. trees grown for timber or for
  fruit-and-timber) and annual crops (e.g. maize, wheat) are NOT bearer
  plants and remain biological assets; every bearer-plant/carve-in
  judgment feeding the disproportionate-cost registry is consumed from
  SV-COA-FR-012 by id.
  (LB-007; EVID-298 — 32_ Sec 34, párrs. 34.1-34.2B, txt PAGE 301)
- **SV-COA-FR-131:** The system shall account for biological assets per
  class policy: recognition when the entity controls the asset from past
  events, future benefits are probable, and fair value or cost is
  reliably measurable without disproportionate cost (34.3); the FAIR
  VALUE model — fair value less costs to sell at initial recognition AND
  at each reporting date, changes recognized in profit or loss — for
  classes whose fair value is readily determinable without
  disproportionate cost; the COST model — cost less accumulated
  depreciation less accumulated impairment — for all others (34.4,
  34.8), each fallback feeding the disproportionate-cost registry
  (SV-COA-FR-012 by id); fair-value measurement per the Sección 12
  engine consumed from SV-COA-FR-076..081 by id; with the model-specific
  disclosures: class descriptions plus the change-in-carrying
  reconciliation (fair-value changes, purchases, harvest decreases,
  business-combination additions, currency conversion, other — no
  comparatives) under the FV model; and the why-not-FV explanation,
  depreciation method, lives/rates and gross-plus-accumulated detail
  under the cost model (34.6, 34.10).
  (LB-007; EVID-298 — 32_ Sec 34, párrs. 34.3-34.10, txt PAGE 301-303)
- **SV-COA-FR-132:** The system shall measure agricultural produce at
  harvest at its fair value less costs to sell AT THE POINT OF HARVEST
  or collection — and that measurement becomes the produce's COST from
  that date under Sección 13 (or other applicable section), feeding the
  inventory engine of FR-093..100 through FR-097's bridge, under BOTH
  the FV model and the cost model for the parent biological assets
  (34.5, 34.9).
  (LB-007; EVID-298 — 32_ Sec 34, párrs. 34.5 y 34.9, txt PAGE 302-303)
- **SV-COA-FR-133:** The system shall implement exploration-and-evaluation
  (E&E) assets: an expenditure-recognition POLICY developed under the
  10.4 criteria (exempt from 10.5), applied consistently, specifying
  which expenditures are recognized as E&E assets — the Norma's example
  set: acquisition of exploration rights; topographic, geological,
  geochemical and geophysical studies; exploratory drilling; trenching;
  sampling; and technical-feasibility/commercial-viability evaluation
  activities — while mineral-DEVELOPMENT expenditures are NEVER E&E
  assets (34.11-34.11A); E&E assets are measured at cost on recognition
  and thereafter follow Sección 17 or Sección 18 according to their
  nature (with dismantling and site-restoration obligations per 17 and
  Sección 21 — file 05 by id); impairment applies per the Sección 27
  engine EXCEPT that the E&E-specific facts-and-circumstances triggers
  REPLACE the 27.7-27.10 indicators, and ONLY for these assets:
  (a) the exploration right for the area expired during the period or
  expires in the near future with no renewal expected; (b) no
  significant further E&E expenditure is budgeted or planned for the
  area; (c) exploration in the area has not led to discovery of
  commercially viable quantities and the entity has decided to
  discontinue; (d) sufficient data indicate that, although development
  is probable, the carrying amount is unlikely to be recovered in full
  from successful development or sale (34.11B-34.11E); the entity keeps
  a policy for assigning E&E assets to CGUs or groups of CGUs for
  testing (34.11F); and E&E assets form a SEPARATE CLASS of assets with
  Sección 17/18-consistent disclosures (34.11G).
  (LB-007; EVID-298 — 32_ Sec 34, párrs. 34.11-34.11G, txt PAGE 303-305)
- **SV-COA-FR-134:** The system shall implement service concessions: a
  concession exists where a government or public-sector grantor engages
  a private operator to develop (or upgrade), operate and maintain the
  grantor's infrastructure assets, the grantor controlling or regulating
  what services the operator provides, to whom and at what price, with
  any significant residual interest at the end of the term (34.12); the
  operator recognizes a FINANCIAL ASSET to the extent it has an
  unconditional contractual right to receive a specific or determinable
  amount of cash (or other financial asset) — including grantor
  guarantees of shortfall versus user collections — measured at fair
  value, thereafter under Sección 11 (consumed from
  `03_financial-instruments-fx.md` by id); and an INTANGIBLE ASSET to
  the extent it receives a right to charge users of the public-service
  asset (amounts conditional on the degree of public use — NOT an
  unconditional right), measured at fair value initially, thereafter
  under Sección 18 (FR-109..115); a single contract containing both
  elements is split along the unconditional-guarantee measure
  (34.13-34.15); construction and upgrade services revenue follows
  Sección 23 (`06_revenue.md` by id) (34.16).
  (LB-007; EVID-298 — 32_ Sec 34, párrs. 34.12-34.16, txt PAGE 305-306)

## 4. Data Model

Layer semantics: all entities are Odoo-native config/posting surfaces
(wave default `odoo`; see §5). The model records the ENTITY's own
measurements, elections and tests — it does not emulate any regulator or
appraiser. No printed data table in this file warrants a CSV sidecar
(the indicator/trigger catalogs are small config sets; default none per
plan).

**Inventory surfaces (product.category + NRV engine):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| product.category (class) | sv_coa_inv_formula | select | fifo · avco (+ standard-cost technique flag for MRP) — same formula per nature-and-use class (13.19); no lifo value ships | FR-096 |
| product.category | sv_coa_inv_technique | select | none · standard_cost · retail · most_recent_purchase (13.16 approximation flag) | FR-097 |
| l10n_sv_chart.nrv_assessment | scope · item/group | select + m2o | item · group_similar (line/purpose/geography grouping basis recorded) | FR-093, FR-098 |
| l10n_sv_chart.nrv_assessment | nrv · loss · reversal | monetary | reversal capped at original loss; new carrying = lower(cost, revised NRV); D15 dated row per assessment date | FR-098 |
| product.template / stock moves | financing_element_split | config | deferred-payment excess → interest account (never inventory cost) | FR-094 |
| MRP costing config | normal_capacity_basis | config | fixed-overhead absorption on normal capacity; idle-capacity → expense; abnormal-production unit-cost dampener | FR-095 |
| l10n_sv_chart.inv_disclosure | pledged_amount flag | boolean | *pignorados* disclosure rows (13.22(e)) | FR-100 |

**PPE / intangible asset profile (account.asset + extensions):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset (class config) | sv_coa_ppe_model | select | cost · revaluation — PER CLASS (17.15); switch posts prospectively (10.10A via SV-COA-FR-015) | FR-104 |
| l10n_sv_chart.asset_component | parent_asset · kind | m2o · select | component split; kind: part · replacement · major_inspection; replaced-component derecognition or substitution_cost_proxy flag | FR-101 |
| account.asset | dismantling_provision_link | m2o | initial dismantling/removal/site-restoration estimate (Sec 21 surface, file 05 by id) | FR-102 |
| account.asset | acquisition_basis | select | purchase_cash_equivalent · self_constructed · exchange_fv · exchange_carrying · donation (D18 is_historical rows for migrated histories) | FR-102, FR-103 |
| l10n_sv_chart.asset_revaluation | fv_date · fv_amount · regularity | date · monetary · int | per-class revaluation rows kept "con suficiente regularidad"; OCI surplus account + reversal rules | FR-104 |
| account.asset | method | select | linear · declining · usage — revenue-based NOT in catalog (17.22 validation block) | FR-105 |
| account.asset | availability_date · idle_state | date · boolean | depreciation availability→derecognition; idle continues (no depreciation stop) | FR-105 |
| account.asset | land_flag | boolean | non-depreciable except mines/quarries/landfill | FR-105 |
| account.asset (intangible profile) | internally_generated | boolean | expense guard: blocks capitalization (18.4(c)/18.15-18.16); advances carve via advance flag | FR-109, FR-110 |
| account.asset (intangible profile) | life_basis · life_cap | select · int | contractual_legal (renewal evidence gate) · reliable_estimate; cap 10y when unreliable (18.20) | FR-111 |
| account.asset (intangible profile) | residual_presumed_zero | boolean + evidence | active-market/third-party-commitment evidence to rebut (18.23) | FR-111 |
| account.asset (intangible profile) | amort_method · revenue_based_refutation | select + justification | linear fallback; revenue-based presumption refutable only on recorded (a)/(b) evidence (18.22A) | FR-112 |
| account.asset (goodwill profile) | goodwill_profile | boolean | ≤10y cap (19.34-19.35); non-reversible impairment (27.28); provenance linked to 07's combination record by id | FR-113 |
| l10n_sv_chart.rnd_expense_tag | aggregate disclosure feed | account analytic tag | aggregate R&D expensed in period (18 disclosures) | FR-114 |

**Impairment engine (l10n_sv_chart.impairment_*):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.impairment_test | subject | m2o | asset · cgu · inventory_group (scope carves per 27.1 recorded) | FR-116 |
| l10n_sv_chart.impairment_test | indicators | m2m config | external (a)-(d) · internal (e)-(g) checklist; no-indicator → no estimate required; indicator triggers estimate review hook | FR-117 |
| l10n_sv_chart.impairment_test | recoverable | monetary + basis | max(fv_less_costs · viu); single-measure shortcut; held-for-disposal presumption; FV per SV-COA-FR-076..081 by id | FR-118 |
| l10n_sv_chart.impairment_test | viu_worksheet | json/one2many | flows excl. financing/tax; current-state flag (no uncommitted restructuring/enhancements); pre-tax discount rate(s); no-double-count check; zero-or-decreasing growth extrapolation | FR-119 |
| l10n_sv_chart.impairment_test | routing | select | p&l · revaluation_decrease_17_15D (revalued assets) | FR-120 |
| l10n_sv_chart.cgu | definition_basis · members | char · m2m | smallest identifiable group, largely independent inflows; member assets + allocated goodwill | FR-121 |
| l10n_sv_chart.cgu | nci_gross_up · fallback | monetary · select | practical NCI goodwill gross-up; none · acquiree_whole · group_ex_unintegrated (27.24-27.27) | FR-122 |
| l10n_sv_chart.impairment_allocation | floors | computed | per-asset floor = max(fv_less_costs, viu, zero); goodwill-first order; excess redistribution | FR-121 |
| l10n_sv_chart.impairment_reversal | cap · routing | computed · select | notional un-impaired carrying cap; p&l · revaluation_increase_17_15C; goodwill NEVER (hard block) | FR-123 |
| l10n_sv_chart.impairment_disclosure | class feed | select | 27.33 classes (incl. cost-model investment property) | FR-124 |

**Investment-property profile (account.asset extension):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset | sv_coa_ip_flag | boolean | definition test (16.2); leasehold election per property (16.3); mixed-use split with whole-as-PPE fallback (16.4) | FR-125 |
| account.asset | sv_coa_ip_model | select | fv_p&l · sec17_cost (disproportionate-cost fallback; deemed cost on switch; registry link SV-COA-FR-012) | FR-127, FR-128 |
| l10n_sv_chart.ip_transfer | kind · evidence | select · char | use_change (owner-occupancy · development_for_sale · occupation start/end) · fv_unavailability (16.8) | FR-128 |
| l10n_sv_chart.ip_disclosure | reconciliation rows | one2many | (i)-(v) reconciliation; appraiser-extent; restrictions; contractual obligations (16.10) | FR-129 |

**Specialized-activity profiles:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| account.asset | bearer_plant_profile | boolean + separability evidence | separately measurable initially+continuously → Sec 17 PPE; else biological (34.2A/34.2B) | FR-130 |
| account.asset (class) | biological_model | select | fv_less_costs · cost — per class; fallback registry link (34.1, 34.4, 34.8) | FR-131 |
| l10n_sv_chart.harvest_event | fv_less_costs_at_harvest | monetary | becomes produce cost (Sec 13 bridge, FR-097) | FR-132 |
| l10n_sv_chart.ee_policy + ee_asset class | policy record · triggers · cgu_assignment | config + checklist | 10.4-developed policy (10.5-exempt); E&E triggers (a)-(d) replacing 27.7-27.10; separate class flag (34.11-34.11G) | FR-133 |
| account.asset | concession_profile | select | financial_asset (Sec 11 by id) · intangible (Sec 18) · mixed split along unconditional guarantee (34.13-34.15) | FR-134 |

## 5. Odoo Mapping

Layer semantics for this wave: the chart-of-accounts engine is
Odoo-native (account.account/account.asset/account.move, stock costing,
res.company config) — every FR maps `odoo`; no SaaS rows are introduced
because none of these FRs touch DTE generation/transmission (the only
architecture-split surface per
`shared/docs/saas-thin-client-architecture.md` D2). Model names are
stable across Odoo 17/18/19/20; the revaluation/impairment/NRV engines
are `l10n_sv_chart` extensions over account.asset and account.move, and
the disclosure builders use Odoo's report layouts.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-093 | odoo | stock valuation + l10n_sv_chart.nrv_assessment | lower-of basis | per-item/group scope; loss → P&L via account.move |
| FR-094 | odoo | account.move + product cost config | financing split | duties net of discounts in cost; interest routing |
| FR-095 | odoo | MRP/BoM costing config | normal-capacity absorption | idle → expense; joint/sub-products; exclusions |
| FR-096 | odoo | product.category | costing method | Odoo ships FIFO/AVCO (+standard) — no LIFO: validation gate is a negative test; same formula per class |
| FR-097 | odoo | product.category + l10n_sv_chart | technique flags + harvest bridge | techniques as approximations; FV-at-harvest becomes cost |
| FR-098 | odoo | l10n_sv_chart.nrv_assessment | reversal engine | cap at original loss; dated rows (D15) |
| FR-099 | odoo | config + linkage records | two-track router | fiscal tracks by id (SV-TAX-FR-052/038); bridge = 08 by filename |
| FR-100 | odoo | report layer | 13.22 note set | formula, expense, impairment, pledged |
| FR-101 | odoo | account.asset (+components) | component mgmt | replaced-component derecognition or substitution-cost proxy; inspection components — mapping gap OQ-3 |
| FR-102 | odoo | account.asset | cost build | dismantling estimate (Sec 21 → 05 by id); NOT-costs list; Sec 25 borrowing costs expensed (05 by id) |
| FR-103 | odoo | account.asset | acquisition basis | exchange at FV / carrying fallback; FV via SV-COA-FR-076..081 |
| FR-104 | odoo | account.asset + l10n_sv_chart.asset_revaluation | per-class model | OCI superávit de revaluación accounts (02 by id); 10.10A prospective switch (SV-COA-FR-015); no native Odoo revaluation model — custom engine |
| FR-105 | odoo | account.asset | depreciation | availability→derecognition; idle continues; land flag; revenue-based blocked at validation (17.22); estimate reviews prospective (SV-COA-FR-017) |
| FR-106 | odoo | account.asset + account.move | disposal routing | gain/loss to non-revenue P&L account; control-transfer date per 06 by id |
| FR-107 | odoo | report layer | 17.31-17.33 set | bases, methods, lives/rates, gross+accumulated, reconciliation, restrictions, commitments, revaluation |
| FR-108 | odoo | config + linkage | two-track router | fiscal register SV-TAX-FR-150..172 by id; costo básico SV-TAX-FR-081 unaffected by revaluation; bridge = 08 by filename |
| FR-109 | odoo | account.asset profile | recognition gate | 18.4(a)(b)(c) checks; combination intangibles from 07 by id |
| FR-110 | odoo | account.asset + expense guard | internally generated | ALL R&D + worked set expensed; advances carve; no re-capitalization |
| FR-111 | odoo | account.asset profile | life/residual | finite-always; contractual/legal cap; 10y cap; residual zero presumption |
| FR-112 | odoo | account.asset profile | amortization | from availability; linear fallback; 18.22A refutation gate with recorded justification |
| FR-113 | odoo | account.asset goodwill profile | ≤10y + no reversal | provenance 07 by id; 27.28 hard block on reversal |
| FR-114 | odoo | report layer | 18 disclosures | class reconciliation + aggregate R&D expensed |
| FR-115 | odoo | config + linkage | two-track router | SV-TAX-FR-052 (29-A.19) / SV-TAX-FR-165/166 (30-A 25%) by id; bridge = 08 by filename |
| FR-116 | odoo | l10n_sv_chart.impairment_test | scope carves | exceptions routed by id/filename (29→08, 28→05, 11→03, 23.70→06) |
| FR-117 | odoo | l10n_sv_chart.impairment_test | indicator checklist | external (a)-(d)/internal (e)-(g); estimate-review hook |
| FR-118 | odoo | l10n_sv_chart.impairment_test | recoverable | max(FV−costs, VIU); FV per SV-COA-FR-076..081 by id |
| FR-119 | odoo | l10n_sv_chart.impairment_test | VIU worksheet | pre-tax rate; no financing/tax flows; current-state; no double counting |
| FR-120 | odoo | l10n_sv_chart.impairment_test | routing | P&L or 17.15D revaluation-decrease (surplus-first) |
| FR-121 | odoo | l10n_sv_chart.cgu | allocation + floors | goodwill-first; pro rata; max(FV−costs, VIU, 0) floors; excess redistribution |
| FR-122 | odoo | l10n_sv_chart.cgu | goodwill testing | acquisition-date allocation; NCI gross-up; whole-entity/group fallback |
| FR-123 | odoo | l10n_sv_chart.impairment_reversal | caps + routing | goodwill NEVER; notional-carrying cap; 17.15C OCI routing for revalued assets |
| FR-124 | odoo | report layer | 27.32-27.33 set | per-class losses/reversals + line items; fiscal note by id |
| FR-125 | odoo | account.asset | IP classification | definition; leasehold election per property; mixed-use split |
| FR-126 | odoo | account.asset | initial cost | transaction costs; PV deferred; 20.9 leasehold amount (lease engine by id) |
| FR-127 | odoo | account.asset + FV schedule | FV model | P&L changes; disproportionate-cost fallback → registry SV-COA-FR-012 by id |
| FR-128 | odoo | l10n_sv_chart.ip_transfer | transfers | use-change only with evidence; FV-unavailability fallback = deemed cost, not policy change |
| FR-129 | odoo | report layer | 16.10-16.11 set | appraiser extent; restrictions; obligations; (i)-(v) reconciliation |
| FR-130 | odoo | account.asset | bearer-plant profile | separability evidence initial+continuous; produce stays agricultural |
| FR-131 | odoo | account.asset class config | biological models | FV−costs w/ reconciliation vs cost model + why-not-FV disclosure |
| FR-132 | odoo | l10n_sv_chart.harvest_event | harvest bridge | FV−costs at harvest = produce cost (feeds FR-097) |
| FR-133 | odoo | l10n_sv_chart.ee_policy + class | E&E engine | 10.4 policy; E&E triggers replace 27.7-27.10; separate class; CGU assignment policy |
| FR-134 | odoo | account.asset concession profile | concession models | financial (Sec 11 by id) vs intangible (Sec 18); mixed split; revenue per 06 by id |

Version-regime notes (D12/D15): the NIIF edition is a DATED regime row —
3rd edition (Feb-2025) applies to annual periods beginning 2027-01-01,
early adoption permitted (A1); SV 2025-2027 books may run the 2nd
(2015) edition (SOQ-48 — the Tabla A1 delta map and company edition
flag are owned by `08_deferred-tax-adoption.md` by id). The lettered
párrafs cited here (16.3A, 17.15B-17.15D, 18.22A, 34.11A-34.11G) are
3rd-edition print positions; any 2nd-edition vintage mapping routes to
T8's Tabla A1 rows — no dual implementation in this file. D15 anchors:
estimate changes (life/residual/method reviews; NRV assessments;
impairment tests) resolve as-of their own dates and snapshot on dated
rows. Mid-year go-live (D18): migrated asset histories, revaluations and
impairment tests ingest as `is_historical` rows with original-period
depreciation semantics (tiered ingestion; no re-derivation; D19
sequence-init kin = T8's Sec 35 surface). Hard gates never overridden by
configuration: the LIFO ban (13.19), the revenue-based depreciation ban
(17.22), the goodwill non-reversal (27.28) and the 10-year cap (18.20).

## 6. Acceptance Criteria

- **AC-001:** Given an inventory class configured with a LIFO-style cost
  formula, when the configuration is saved, then validation REJECTS it
  with the 13.19 print — only FIFO and weighted average are offered, and
  the class-scope rule enforces one formula across all inventories of
  the same nature-and-use class (FR-096).
- **AC-002:** Given a building PPE class switched to the revaluation
  model, when the class-wide revaluation posts, then the surplus books to
  OCI *superávit de revaluación* (never revenue, never retained
  earnings), every item of the class is revalued, subsequent depreciation
  runs on the revalued amount, the switch posts prospectively (no
  comparative restatement), and the fiscal register and *costo básico*
  remain computed on the unrevalued admitted-depreciation basis
  (SV-TAX-FR-150..172 / SV-TAX-FR-081 by id) with the difference routed
  to T8 (FR-104, FR-108).
- **AC-003:** Given an internally developed customer list with documented
  acquisition costs internally incurred, when the expenditure posts, then
  it is EXPENSED as incurred (18.15-18.16), no intangible asset is
  created, and any later attempt to re-capitalize the prior-period
  expenditure is rejected (FR-110).
- **AC-004:** Given a CGU whose recoverable amount falls below carrying,
  when the impairment posts, then the loss reduces the unit's allocated
  GOODWILL first and the remainder pro rata over the other assets without
  breaching any per-asset floor (max of FV−costs to sell, VIU, zero);
  when the unit later recovers, then every asset reverses capped at its
  notional un-impaired carrying EXCEPT the goodwill, which never
  reverses (FR-121, FR-122, FR-123).
- **AC-005:** Given software amortized over 4 book years while the fiscal
  register runs the Art. 30-A 25% regime, when the period closes, then
  the book quota posts per the ≤10-year finite-life engine and the
  book-vs-fiscal difference is recorded as a temporary difference routed
  through `08_deferred-tax-adoption.md` (T8) FRs — never by re-deriving
  the fiscal quota here (FR-111, FR-112, FR-115).
- **AC-006:** Given a machine held temporarily idle (not fully
  depreciated), when the depreciation run executes, then depreciation
  CONTINUES for the idle period; given a land parcel, then no
  depreciation line is generated (FR-105).
- **AC-007:** Given an inventory item written down to NRV 80 against cost
  100, when NRV later recovers to 95, then the reversal posts 15 — never
  beyond the original 20 loss — and the new carrying amount is the lower
  of cost (100) and revised NRV (95) (FR-098).
- **AC-008:** Given a major engine replacement on an aircraft frame whose
  books do not separately identify the replaced engine, when the
  replacement capitalizes, then the substitution-cost proxy derecognizes
  the old component's carrying and the new component depreciates on its
  own life; given a major inspection, then its cost capitalizes as a
  component and any remaining inspection carrying derecognizes
  (FR-101).
- **AC-009:** Given an investment property whose appraisal would cost
  disproportionately, when the fallback applies, then the property runs
  under the Sección 17 cost model with its carrying at that date as
  deemed cost, a disproportionate-cost registry row records requirement,
  item, basis and date (SV-COA-FR-012 by id), the 16.10(c)(iii)-area
  disclosure emits, and the judgment is remade at the next measurement
  date — and when fair value becomes measurable again, the FV model
  resumes (FR-127, FR-128).
- **AC-010:** Given an E&E asset whose exploration right for the area
  expired without expected renewal, when the impairment assessment runs,
  then the E&E-specific trigger (34.11E(a)) — not the generic 27.7-27.10
  indicator screen — forces the recoverable-amount test, and the loss
  measures per the Sección 27 engine (FR-133, FR-118..121).
- **AC-011:** Given a coffee harvest from bearer plants measurable
  separately from their produce, when the harvest posts, then the beans
  enter inventory at fair value less costs to sell at the point of
  harvest as their COST (thereafter FIFO/AVG + NRV), while the plants
  themselves depreciate as PPE — and the produce of plants NOT so
  measurable runs the biological-asset engine instead (FR-130, FR-131,
  FR-132, FR-097).
- **AC-012:** Given a revalued PPE asset under the 17.15B model that
  impairs and later recovers, when the loss posts, then it routes as a
  revaluation DECREASE per 17.15D (surplus first), and when recovery
  comes, the reversal routes as a revaluation INCREASE per 17.15C —
  neither leg through profit or loss while surplus mechanics apply
  (FR-120, FR-123).
- **AC-013:** Given a revenue-based depreciation method (or a
  revenue-based amortization method without a recorded (a)/(b)
  refutation justification), when the method is saved, then validation
  REJECTS it per 17.22 / the 18.22A presumption (FR-105, FR-112).
- **AC-014:** Given a toll-road concession with a government guarantee
  covering only half the construction cost, when the asset is
  recognized, then the guaranteed half books as a financial asset at
  fair value (Sección 11, 03 by id) and the usage-conditioned half as an
  intangible (Sección 18), with construction services revenue per
  `06_revenue.md` by id (FR-134).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-46 carried: the SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is NOT in the corpus — the measurement hard encodings of this file are the Norma's own printed rules with NO invented SV thresholds/deviations, and any SV-specific override the future instrument might introduce (e.g. mandatory revaluation, fiscal-book alignment) is external dated law. Acquisition candidate ≥75 (same instrument as commercial-legal/03 OQ-002; 01-file OQ-1 kin). | no | Takumi S8 (sources watch) | open |
| OQ-2 | Disproportionate-cost usage disclosures: the Sec 16 FV-fallback (16.1/16.7-16.8), the bearer-plant separability carve (34.2A) and the biological-asset cost-model fallback (34.1) all consume the 01-file registry (SV-COA-FR-012 by id); whether the notes builder needs a DEDICATED per-usage disclosure section per Sección 2.30 wording ("ese hecho y las razones") beyond the generic registry emission — and the exact disclosure wording for the 16.10(c)(iii)-area transfer case — needs a design check at implementation. Carried per controller instruction. | no | Takumi S8 (notes design) | open |
| OQ-3 | Odoo component-asset mapping gaps: 17.5-17.7 requires per-component recognition with replaced-component derecognition or the substitution-cost proxy when the books do not identify the replaced part — Odoo's account.asset has no native component parent/child with independent lives and no substitution-cost derecognition pattern; the l10n_sv_chart.asset_component design (child assets vs component lines; inspection-component rotation) is an open mapping gap, as is the absence of a native revaluation model (FR-104 custom engine) and native impairment postings (FR-116..123 custom engine). Carried per controller instruction. | no | Takumi S8 (asset engine design) | open |
