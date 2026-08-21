# SV — Chart of accounts — Groups: consolidation, separate/combined FS, business combinations, associates & joint arrangements, related parties, post-period events

| Field   | Value |
|---------|-------|
| Country | sv |
| Topic   | chart-of-accounts |
| Status  | draft |
| Authors | Takumi synthesis wave 8 (S8 chart-of-accounts) |
| Updated | 2026-08-20 |

## 1. Purpose

This file defines the multi-entity layer of the ACCOUNTING book under the
*Norma de Contabilidad NIIF para las PYMES* (32_): the consolidation duty and
its exemptions (Sección 9 — the controladora-is-subsidiary exemption and the
held-for-sale subsidiary exclusion with its one-year clock and restatement
rule); the control model (the 9.4B triad, the majority-vote presumption,
potential voting rights and the agent/principal determination); consolidation
mechanics (line-by-line combining, intragroup eliminations with the
losses-then-impairment rule, *participaciones no controladoras* — 
non-controlling interests, NCI — presented separately, uniform reporting date
and policies); loss of control (derecognition, retained interest at fair
value, gain/loss to P&L, FX-translation OCI never recycled); NCI transactions
without loss of control as equity transactions; the 9.26 separate-FS policy
menu per investment category; the 9.25A separate-FS-only presentation;
combined FS; business combinations (Sección 19 + Apéndice 19A — the
acquisition method, fair value of identifiables, **NCI at the proportionate
amount only**, the goodwill formula including step-acquisition stakes, bargain
purchases, contingent consideration, the 12-month measurement period,
acquisition costs expensed, and the business-vs-asset tests); associates
(Sección 14 — significant influence with the 20% presumption and the 14.4
policy menu); joint arrangements (Sección 15 — operations/assets/entities
forms, the 15.9 menu and the routing of parties without joint control);
related parties (Sección 33 — the definition set, the controladora/ultimate
naming disclosures regardless of transactions, aggregate KMP remuneration,
category-split transaction/balance/commitment disclosures, the
no-arm's-length-assertion bar and the government-related-entity exemption
with its substitute disclosures); and post-period events (Sección 32 —
adjusting vs non-adjusting, the 32.11 dividends-not-a-liability rule, the
authorization-date disclosure).

It does **not** cover: the single-entity FS architecture (`02`), financial
instruments/FX (`03` — held-for-sale classification 11.8(d) mechanics and FV
measurement), non-financial assets (`04` — impairment testing of goodwill
CGUs per 27.23-27.27), liabilities/equity/benefits (`05` — Sección 22
instrument classification, the 22.5(d) puttable-in-subsidiary liability case
and the declaration-date distribution mechanics incl. the 32.11 kin field),
revenue (`06`), deferred tax/first-time adoption/edition versioning (`08`).
Those files' surfaces are consumed BY ID. Fiscal computations (ISR capital
gains on share disposals, dividend taxation) are owned by their waves; the
book-vs-fiscal bridge routes through N8's deferred-tax FRs (`08` by id) and
is never re-derived here.

## 2. Legal Basis

Authority order (binding, per master evidence index §S8-A and ruling R29,
identically to `01_framework-policies.md`): the operative framework LB =
**32_** — *Norma de Contabilidad NIIF para las PYMES, TERCERA EDICIÓN
(Febrero 2025)*, IFRS Foundation official Spanish translation, Sections 1-35
+ Apéndice A + Apéndice B; effective 2027-01-01 with early adoption
permitted (A1; txt PAGE 315), cited by section/párrafo as printed.
**33_** (EY *Guía Práctica*) is SECONDARY-ONLY per R29(a): never the sole LB
of an FR; here its only role is the documented full-NIIF-vs-PYMES contrast
for the 19.14 NCI measurement (full NIIF's IFRS 3 fair-value-at-acquisition
election that PYMES removes — LB-007); where 33_ and 32_ could diverge, 32_
governs without exception.

**SOQ-46 instrument-gap note (rides every FR in this file and this wave):**
the Norma is jurisdiction-neutral on who applies it — "Las decisiones sobre
qué entidades están requeridas o autorizadas a utilizar las Normas NIIF de
Contabilidad completas o la Norma de Contabilidad NIIF para las PYMES
recaen en las autoridades legislativas y regulatorias y en los emisores de
normas de las distintas jurisdicciones" (Prólogo P12; txt PAGE 22) — and the
SV adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444,
or successor legislation) is NOT in the corpus (commercial-legal/03 OQ-002
tracks the same acquisition). **Consolidation-applicability kin (SOQ-46):**
group structures exist regardless of which framework a company's books
target — the consolidation engine below therefore ships
framework-agnostically on the group/relationship model, and NO SV
consolidation threshold or exemption-eligibility rule is invented; the 9.3
statutory exemption conditions are encoded as printed, their SV-legal force
gated only by the missing instrument (OQ-1).

**Citation ruling applied (controller, binding):** where the scoped evidence
block is thin for a specific párrafo, the LB cites `32_ + section/párrafo +
txt PAGE anchor` accompanied by the nearest governing EVID id. This applies
to Sección 14 (LB-003) and Sección 15 (LB-004), whose governing wave evidence
is EVID-282 (the 9.26 menu and 19.29/15.x cross-references); Secciones 9,
19+19A, 32 and 33 cite their governing EVIDs (282/289/298) with
párrafo-accurate anchors verified against the txt.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | Norma NIIF para las PYMES, Sección 9: 9.2: "Excepto por lo permitido o requerido en por los párrafos 9.3 y 9.3C, una controladora presentará estados financieros consolidados. Los estados financieros consolidados incluirán todas las subsidiarias de la controladora, excepto las subsidiarias a las que se aplica el párrafo 9.3A." 9.3: exención — "Una controladora no necesita presentar estados financieros consolidados si se cumplen las dos condiciones siguientes: (a) la controladora es ella misma una subsidiaria; y (b) su última controladora (o alguna de las controladoras intermedias) elaboran estados financieros consolidados con propósito de información general que cumplan con las Normas NIIF de Contabilidad completas o con esta Norma." 9.3A: "Sujeto al párrafo 9.3B, una subsidiaria no se consolidará si se adquiere y mantiene con la intención de venderla o disponer de ella dentro de un año desde su fecha de adquisición… se contabilizará de acuerdo con… el párrafo 11.8(d), en lugar de acuerdo con esta sección." 9.3B: si no se dispone dentro del año — 9.3C: "Si una controladora no tiene subsidiarias distintas de aquellas que no se consolidan de acuerdo con los párrafos 9.3A y 9.3B, no presentará estados financieros consolidados" (+ revelación 9.23A). 9.4: "Una subsidiaria es una entidad… que está controlada por otra entidad… Un inversor, independientemente de la naturaleza de su participación en la participada, determinará si es una controladora evaluando si controla la participada" (re-evaluación ante cambios en los tres elementos). "(a) La controladora consolidará la subsidiaria desde la fecha de adquisición… si la fecha de adquisición fuera en un periodo anterior, se reexpresarán los periodos anteriores correspondientes"; "(b) Si el retraso es causado por sucesos o circunstancias fuera del control de la controladora y existe evidencia suficiente en la fecha de presentación de que la controladora mantiene su compromiso con el plan de vender o disponer de la subsidiaria, la controladora continuará contabilizando la subsidiaria de acuerdo con el párrafo 9.3A." 9.4B: control = "(a) poder sobre la participada; (b) exposición, o derechos, a rendimientos variables procedentes de su implicación en la participada; y (c) la capacidad de utilizar su poder para influir en los rendimientos". 9.5: "Se presume que existe control cuando el inversor la posea, directa o indirectamente…, una mayoría de los derechos de voto… la presunción puede refutarse si se puede demostrar claramente que el inversor no tiene uno o más de los elementos de control". 9.7B: poder sin mayoría — "(a) un acuerdo contractual entre el inversor y otros tenedores de voto; (b) derechos procedentes de otros acuerdos contractuales; (c) derechos de voto del inversor; (d) derechos de voto potenciales (véase el párrafo 9.8); o (e) una combinación de (a) a (d)." 9.8: "Los derechos de voto potenciales… se consideran solo si el titular del derecho tiene la capacidad práctica de ejercerlo… el derecho necesita ser ejercitable actualmente." 9.12 (agente/principal): "Cuando un inversor con derechos de toma de decisiones (quien toma decisiones) evalúa si controla una participada, determinará si es un principal o un agente… Un agente es una parte dedicada principalmente a actuar en nombre y a beneficio, de otra parte o partes (el principal o principales) y, por ello, no controla la participada cuando ejerce su autoridad para tomar decisiones." 9.13: "combinará los estados financieros de la controladora y sus subsidiarias línea por línea, agregando las partidas que representen activos, pasivos, patrimonio, ingresos y gastos de contenido similar" + eliminación de la inversión + NCI "por separado" en el resultado y los activos netos + eliminación íntegra de saldos/transacciones intragrupo, pérdidas intragrupo → comprobación de deterioro (9.16); misma fecha o ajuste por transacciones significativas (9.14); políticas uniformes (9.15). 9.18-9.18B: pérdida de control — baja de activos/pasivos/NCI/plusvalía; interés conservado a valor razonable; ganancia/pérdida en resultado; OCI acumulado reclasificado EXCEPTO diferencias de conversión de subsidiaria extranjera (nunca se reclasifican). 9.20A: transacción con NCI sin pérdida de control = transacción con propietarios en su calidad de propietarios, sin ganancia/pérdida, sin revaluación de activos. 9.25A: "Una controladora que está exenta de presentar estados financieros consolidados… puede presentar estados financieros separados como sus únicos estados financieros." 9.26 (menú en separados): "(a) al costo menos el deterioro del valor; (b) al valor razonable con los cambios en el valor razonable reconocidos en resultados; o (c) usando el método de la participación siguiendo los procedimientos del párrafo 14.8. La entidad aplicará la misma política contable a todas las inversiones de una categoría (subsidiarias, asociadas o entidades controladas de forma conjunta), pero puede elegir políticas diferentes para las distintas categorías." 9.28-9.30: estados financieros combinados — eliminaciones intragrupo, políticas uniformes, y revelación de (a) que son combinados; (b) la razón; (c) la base de inclusión de entidades; (d) la base de preparación; (e) la información de la Sección 33 | A controladora presents consolidated FS (9.2) except under 9.3 (the controladora is itself a subsidiary AND its ultimate/intermediate controladora produces complying consolidated GPFS) or 9.3A (subsidiary acquired and held for sale/disposal within one year from acquisition — accounted per 11.8(d) held-for-sale, not consolidated); 9.3C (no consolidated FS where the only subsidiaries are 9.3A/9.3B-excluded, 9.23A disclosures); 9.4 (control determined regardless of the nature of the investor's interest — de-facto control); 9.3B: not disposed of within the year → consolidate from acquisition date with restatement of prior periods, UNLESS the delay is outside the controladora's control and commitment persists at the presentation date (then 9.3A treatment continues). Control = power + exposure/entitlement to variable returns + ability to use power to affect returns (9.4B); majority voting rights presumed control, refutation by clearly demonstrating a missing element (9.5); power without majority via contractual agreements and potential voting rights, considered only when practically exercisable/currently exercisable (9.7B, 9.8); decision-makers assess principal vs agent — an agent acting primarily for another's benefit does not control (9.12). Mechanics: line-by-line combining of like items; eliminate investment against equity; NCI separately in profit and net assets; full intragroup elimination with losses followed by impairment check; uniform date (or adjust for significant intervening transactions) and policies (9.13-9.16). Loss of control: derecognize, retained interest at fair value, gain/loss to P&L, accumulated OCI reclassified except FX translation of a foreign subsidiary (never recycled) (9.18-9.18B). NCI transactions without loss of control = equity transactions, no gain/loss, no asset revaluation (9.20A). Exempt controladora may present separate FS as its ONLY FS (9.25A). Separate-FS menu per category — cost less impairment \| FV through P&L \| equity method — same policy within a category, different across categories (9.26). Combined FS with eliminations, uniform policies and the (a)-(e) disclosures (9.28-9.30) | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 9, párrs. 9.1–9.30 (txt PAGE 75-84; 9.2/9.3/9.3A/9.3B/9.3C/9.4 PAGE 75-76; 9.4B/9.5 PAGE 76-77; 9.7B/9.8/9.12/9.13 PAGE 78; 9.18-9.18B PAGE 80; 9.20A PAGE 81; 9.25A/9.26 PAGE 82-83; 9.28-9.30 PAGE 83-84) (EVID-282) |
| LB-002 | Norma NIIF para las PYMES, Sección 19 + Apéndice 19A: alcance — NO combinaciones entre entidades bajo control común. 19.6: método de adquisición — identificar adquirente, fecha de adquisición, reconocer/medir identificables a VR, reconocer plusvalía o ganancia. 19.12-19.13: identificables a valor razonable a la fecha de adquisición. **19.14: "por la parte proporcional de la participación no controladora en los importes reconocidos de los activos netos identificables"** (sin opción de VR, a diferencia de NIIF completas). 19.16: intangibles si criterios Sección 18 + VR medible (exención 19.16 por costo desproporcionado, revelaciones 19.38). 19.17-19.19: pasivos contingentes asumidos reconocidos si VR medible con fiabilidad (aunque no sea probable). 19.20: impuestos diferidos Sección 29. 19.21: beneficios a los empleados Sección 28. 19.22: plusvalía = exceso de (a) [(i) contraprestación transferida (19.25) + (ii) NCI (19.14) + (iii) VR de la participación previa en etapas (19.29-19.30)] sobre (b) el neto de identificables (19.13-19.21). 19.23-19.24: compra en términos muy ventajosos → reevaluar ("re-assess") y luego ganancia en resultados. 19.26: contraprestación contingente al VR "si el valor razonable… puede medirse de forma fiable sin costo ni esfuerzo desproporcionado"; 19.27: si no, "utilizando el importe más probable… Posteriormente, la entidad adquirente no volverá a evaluar" (sin remedición del fallback); 19.36-19.37: clasificación por la Sección 22; patrimonio no se remide; pasivo financiero se remide → resultados (Sección 11). 19.29: por etapas — "volverá a valorar su participación en el patrimonio previamente mantenida en la adquirida a su valor razonable en la fecha de adquisición y reconocerá la ganancia o pérdida resultante". 19.31: periodo de medición ≤12 meses (ajuste retrospectivo); después solo corrección de errores. 19.32: costos de adquisición como gasto (costos de emisión 11/22). Apéndice 19A: negocio = insumos + procesos sustanciales → productos; **prueba de concentración opcional** 19A.3 — "(a) se cumple, queda determinado que el conjunto… no es un negocio y no es necesaria ninguna evaluación adicional; o (b) no se cumple… la entidad realiza la evaluación establecida en los párrafos 19A.4 a 19A.10"; "sustancialmente todo el valor razonable de los activos brutos adquiridos se concentra en un único activo identificable o grupo de activos identificables similares"; árbol de procesos sustanciales (Figura 19.1) | Scope excludes common-control combinations. Acquisition method (identify acquirer/date; recognize identifiables at FV; goodwill or bargain). NCI at the PROPORTIONATE share of recognized net identifiables (19.14) — no FV election, unlike full NIIF. Intangibles if Sec 18 criteria + measurable FV. Assumed contingent liabilities recognized when reliably FV-measurable, even if not probable. Deferred taxes per Sec 29; employee benefits per Sec 28. Goodwill = [consideration + NCI (19.14) + previously-held stake at FV] − net identifiables. Bargain purchase: re-assess then P&L gain. Contingent consideration at acquisition-date FV if reliably measurable without disproportionate cost; else most-likely amount, NOT re-measured afterwards; Sec 22 classification (equity not remeasured; financial liability remeasured → P&L). Step acquisition: revalue previously-held stake to FV → P&L. Measurement period ≤12 months, retrospective; then only error corrections. Acquisition costs EXPENSED. 19A: business = inputs + substantive processes → outputs; optional concentration test (substantially all FV in one identifiable asset/group → NOT a business); else the substantive-process decision tree | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 19, párrs. 19.6–19.38 + Apéndice 19A (txt PAGE 156-170; 19.6 PAGE 157; 19.12-19.14/19.16-19.17 PAGE 158; 19.22 PAGE 159-160; 19.26-19.27/19.29/19.31 PAGE 160-161; 19.32 PAGE 162; 19.36-19.38 PAGE 163; 19A.2-19A.3 PAGE 166-167) (EVID-289) |
| LB-003 | Norma NIIF para las PYMES, Sección 14 (citation ruling: 32_ + párrafo + PAGE anchor; nearest governing EVID-282): 14.2: influencia significativa = "el poder de intervenir en las decisiones de política financiera y de operación de la asociada, sin llegar a tener el control ni el control conjunto"; "(a) si un inversor mantiene… el 20 por ciento o más del poder de voto…, se supone que tiene influencia significativa, a menos que pueda demostrarse claramente que tal influencia no existe; (b) a la inversa… menos del 20 por ciento… se supone que no tiene… (c) la existencia de otro inversor que posea una participación mayoritaria o sustancial no impide…". 14.4 (menú): "Un inversor contabilizará todas sus inversiones en asociadas utilizando una de las siguientes opciones: (a) el modelo de costo del párrafo 14.5; (b) el método de la participación del párrafo 14.8; o (c) el modelo del valor razonable del párrafo 14.9." 14.5: costo menos deterioro (Sección 27); 14.7: inversiones con precio de cotización publicado → modelo del valor razonable. 14.8 (método de la participación): (f) estados financieros de la asociada a la misma fecha salvo impracticabilidad + ajustes; (g) políticas uniformes salvo impracticabilidad; (h) pérdidas por encima de la inversión → dejar de reconocer, provisión solo por obligaciones incurridas/pagos; (i) discontinuación al perder influencia significativa, con revaluación a VR cuando pasa a subsidiaria/negocio conjunto, baja con (recibido + VR conservado) − importe en libros al disponer, y nueva base de costo si se pierde por otra vía. 14.9 (modelo VR): VR con cambios en resultados; costo para la que no pueda medirse "sin costos o esfuerzos desproporcionados". 14.10: clasificación como activos no corrientes; 14.12-14.14: revelaciones (política; importe en libros; VR si cotiza y usa participación) | An associate is an entity over which the investor has significant influence — the power to participate in financial and operating policy decisions without control or joint control; ≥20% of voting rights (directly/indirectly) PRESUMES significant influence unless clearly disproven; <20% presumes none unless clearly proven; another large holder does not preclude it. Entity-wide menu for ALL associate investments: (a) cost model (cost − impairment); (b) equity method (same-date FS or adjustments; uniform policies unless impracticable; losses beyond the investment suspend recognition with provisions only for incurred obligations; discontinuation on losing influence — remeasurement rules on becoming subsidiary/JV, disposal gain = (consideration + FV retained) − carrying amount, fresh cost basis otherwise); (c) FV model (FV through P&L; cost fallback where FV not reliably measurable without disproportionate cost). Quoted-price associates use the FV model. Non-current classification; policy/carrying-amount/FV disclosures | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 14, párrs. 14.2–14.14 (txt PAGE 128-131; 14.2/14.4 PAGE 128; 14.5/14.7 PAGE 128-129; 14.8 PAGE 129-131; 14.9-14.10 PAGE 131) (32_ citation ruling; EVID-282 nearest governing) |
| LB-004 | Norma NIIF para las PYMES, Sección 15 (citation ruling: 32_ + párrafo + PAGE anchor; nearest governing EVID-282): 15.2A: formas de acuerdos conjuntos — operaciones controladas de forma conjunta; activos controlados de forma conjunta; entidades controladas de forma conjunta. 15.4-15.5 (operaciones): la parte reconoce "(a) los activos que controla y los pasivos en los que incurre; y (b) los gastos en que incurre y su participación en los ingresos…". 15.7-15.8 (activos): participación en los activos controlados conjuntamente según su naturaleza; pasivos propios y parte de los conjuntos; ingresos/gastos según su porción. 15.6 (entidades): "acuerdo conjunto que implica la creación de una sociedad…, en la que cada parte adquiere una participación". **15.9 (menú): "contabilizará todas sus inversiones en entidades controladas conjuntamente utilizando una de las siguientes alternativas: (a) el modelo de costo del párrafo 15.10; (b) el método de la participación del párrafo 15.13; o (c) el modelo del valor razonable del párrafo 15.14."** 15.15: exención por costo/esfuerzo desproporcionado del VR (fallback al costo + revelación); 15.16: revelaciones — política; importe en libros (4.2(k)); VR si cotiza con método participación; importe agregado de compromisos incluidos los conjuntos. 15.18A (enrutamiento sin control conjunto): participación en una entidad controlada conjuntamente sin control conjunto → Sección 11, salvo influencia significativa → Sección 14; 15.18B: operación conjunta sin control conjunto → 15.5; activos conjuntos sin control conjunto → 15.7 | Joint arrangement forms: jointly controlled OPERATIONS (party recognizes the assets it controls, liabilities it incurs, its expenses and its share of revenue); jointly controlled ASSETS (share of the jointly controlled assets classified by nature, own and shared liabilities, share of revenue/expenses); jointly controlled ENTITIES (a separate vehicle each party holds a participation in). Entity-wide menu for ALL JCE investments: cost model (15.10) \| equity method (15.13) \| FV model (15.14), with the disproportionate-cost FV→cost fallback and its disclosure (15.15) and the 15.16 disclosures (policy; carrying amount; FV of quoted equity-method JCEs; aggregate commitments incl. jointly incurred). Parties WITHOUT joint control route: JCE participation → Section 11 unless significant influence (then Section 14); joint operation → 15.5; jointly controlled assets → 15.7 (15.18A-15.18B) | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 15, párrs. 15.2A–15.21 (txt PAGE 133-136; 15.2A/15.4-15.9 PAGE 133-134; 15.15-15.16 PAGE 135-136; 15.18A-15.18B PAGE 136) (32_ citation ruling; EVID-282 nearest governing) |
| LB-005 | Norma NIIF para las PYMES, Sección 32: 32.5: hechos que implican ajuste — condiciones existentes al final del periodo (ejemplos: resolución de litigio, evidencia de deterioro, determinación de costos/ingresos, fraude/errores); 32.10: hechos que no implican ajuste — caídas de mercado posteriores, ganancias por litigios salidos tras el cierre; "(a) la naturaleza del evento; y (b) una estimación de sus efectos financieros, o un pronunciamiento de que no se puede realizar esta estimación". **32.11: "Si una entidad acuerda distribuir dividendos a los tenedores de sus instrumentos de patrimonio después del final del periodo sobre el que se informa, no reconocerá esos dividendos como un pasivo al final del periodo sobre el que se informa. El importe del dividendo se puede presentar como un componente segregado de ganancias acumuladas al final del periodo sobre el que se informa."** 32.9-32.10 (fecha de autorización): "Una entidad revelará la fecha en que los estados financieros han sido autorizados para su emisión y quién ha concedido esa autorización. Si los propietarios de la entidad u otros tienen poder para modificar los estados financieros tras la publicación, la entidad revelará ese hecho." | Post-period events: ADJUSTING when they provide evidence of conditions existing at the period end (litigation resolution, impairment evidence, cost/income determination, fraud/errors) — amounts adjusted; NON-ADJUSTING when they concern conditions arising after (post-period market declines, litigation gains from post-period events) — disclose nature and estimated financial effects or a statement that estimation cannot be made. Dividends AGREED after the period end are NOT a liability at the period end; the amount may be presented as a segregated component of retained earnings (32.11). The FS disclose the authorization-for-issue date and who granted it, plus the fact when owners/others retain power to modify after publication | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 32, párrs. 32.4–32.11 (txt PAGE 292-295; 32.5 PAGE 292-294; 32.9-32.10 PAGE 294-295; 32.11 PAGE 294) (EVID-298) |
| LB-006 | Norma NIIF para las PYMES, Sección 33: 33.2 (definición): personas — "(i) es un miembro del personal clave de la gerencia de la entidad que informa o de una controladora…; (ii) ejerce control o control conjunto…; o (iii) ejerce influencia significativa…", con familiar cercano; entidades — (i) miembros del mismo grupo; (ii) asociada/negocio conjunto (incluso de un miembro del grupo); (iii) ambas entidades controladas conjuntamente por la misma tercera; (iv) negocio conjunto de una tercera y asociada de esa tercera; (v) plan de beneficios post-empleo; (vi) entidad controlada/controlada conjuntamente por persona de (a); (vii) la entidad o miembro del grupo "proporciona servicios del personal clave de la gerencia"; (viii) persona de (a)(ii) con influencia significativa o KMP. 33.3: sustancia sobre forma. **33.4 (NO relacionados):** "(a) dos entidades que simplemente tienen en común un administrador u otra persona clave de la gerencia; (b) dos partes por el mero hecho de compartir el control conjunto…; (c)… proveedores de financiación; sindicatos; entidades de servicios públicos; o departamentos y agencias gubernamentales [por sus relaciones normales]; (d) un cliente, proveedor, franquiciador… o agente en exclusiva… simplemente en virtud de la dependencia económica". 33.6: "Deberán revelarse las relaciones entre una controladora y sus subsidiarias con independencia de que haya habido transacciones… Una entidad revelará el nombre de su controladora y, si fuera diferente, el de la parte controladora última del grupo. Si ni la controladora… ni la parte controladora última… elaboran estados financieros disponibles para uso público, se revelará también el nombre de la controladora próxima más importante que lo hace (si la hay)." 33.3 (KMP): "personas que tienen autoridad y responsabilidad para planificar, dirigir y controlar las actividades de la entidad… incluyendo cualquier administrador (sea o no ejecutivo)"; 33.7: "La entidad revelará el total de la remuneración del personal clave de la gerencia"; carve-out gestión: KMP de una entidad de gestión — revelar los importes por los servicios, no la remuneración pagada por la gestora. 33.9-33.10: transacciones/saldos/compromisos — "(a) el importe de las transacciones; (b) el importe de los saldos pendiente, incluyendo compromisos y: (i) sus plazos y términos, incluyendo si están garantizados…; (ii) detalles de cualquier garantía…; (c) provisiones por cuentas por cobrar incobrables…; y (d) el gasto reconocido… con respecto a las deudas incobrables…", separado por categorías: "(a) entidades con control, control conjunto o influencia significativa sobre la entidad…; (b) entidades sobre las que la entidad ejerza…; (c) personal clave de la gerencia de la entidad o de su controladora (en total); y (d) otras partes relacionadas". 33.12: tipos (compras/ventas, inmuebles, servicios, arrendamientos, I+D, licencias, financiación, garantías colaterales y avales, (ha) compromisos condicionales, liquidación de pasivos, planes de beneficios definidos compartidos). 33.13: "Una entidad no señalará que las transacciones… fueron realizadas en términos equivalentes a los que prevalecen en… condiciones de independencia mutua, a menos que estas condiciones puedan ser justificadas o comprobadas." 33.14: agregación salvo necesidad de separado. **33.11 (exención estatal):** exenta del 33.9 para transacciones/saldos/compromisos con "(a) un gobierno que tiene control, control conjunto o influencia significativa sobre la entidad que informa; y (b) otra entidad… porque el mismo gobierno tiene control, o control conjunto o influencia significativa tanto sobre la entidad que informa como sobre la otra entidad." **33.15 (sustitutivas):** "(a) el nombre del gobierno y la naturaleza de su relación…; (b) la naturaleza y el importe de cada transacción individualmente significativa; (c) para transacciones que sean colectivamente, pero no individualmente, significativas, una indicación cualitativa o cuantitativa de su alcance" | Related-party definition set: persons (KMP members and close family; holders of control/joint control/significant influence) and entities (same-group members; associates/JCEs cross-holdings; two JCEs of the same third party; JCE+associate of the same third; post-employment plans; KMP-controlled or jointly-controlled entities; KMP-service providers; significant influencers who are also KMP), assessed on SUBSTANCE over legal form. NOT necessarily related: two entities merely sharing a director/KMP; parties merely sharing joint control of a JCE; financiers, unions, utilities, government departments/agencies by virtue of normal dealings; economically dependent customers/suppliers/franchisees/distributors/exclusive agents. Controladora-subsidiary relationships disclosed REGARDLESS of transactions — name of the controladora and, if different, the ULTIMATE controlling party (else the most important nearer parent publishing public FS, if any). KMP = persons with authority and responsibility for planning, directing and controlling activities, including any administrator (executive or not); TOTAL KMP remuneration disclosed in aggregate (management-entity carve-out: disclose amounts for the service, not the gestora's own pay). Transactions/balances/commitments disclosures — amounts; outstanding balances incl. commitments with terms/guarantees/nature of consideration; doubtful-debt provisions; bad-debt expense — split by the four categories. No arm's-length assertion unless justifiable/demonstrable. Similar items aggregable unless separate disclosure is necessary. Government-related-entity EXEMPTION from 33.9 for dealings with the controlling government and co-controlled entities, with the 33.15 substitute disclosures: government name + nature of relationship; nature and amount of each individually significant transaction; qualitative/quantitative scope indication for collectively-significant ones | `sv/sources/32_NIIF_PYMES_2025.pdf` | Sección 33, párrs. 33.1–33.15 (txt PAGE 296-300; 33.2/33.4 PAGE 296-297; 33.6-33.7 PAGE 297-298; 33.9-33.11 PAGE 298-299; 33.12-33.13 PAGE 299-300; 33.15 PAGE 300) (EVID-298) |
| LB-007 | Guía EY (SECONDARY-ONLY per R29(a); never sole LB; contrast role only): full-NIIF-vs-PYMES contrast — NIIF completas (IFRS 3) allow the acquirer to measure NCI at acquisition either at fair value (the "full goodwill" method) or at the proportionate share of the recognizable net identifiable assets; the NIIF-PYMES 19.14 removes that election (proportionate-only). Documented as a boundary/contrast note for full-NIIF group entities (the niif_plenas flag values of `01` FR-001) — never a dual implementation | (Secondary authority, R29(a)): the NCI fair-value election exists only under full NIIF; the PYMES engine encodes proportionate-only and flags the contrast for framework-routing purposes | `sv/sources/33_Guia_NIIF_Sostenibilidad_2024-2025.pdf` | NIIF full-vs-PYMES contrast set (EVID-299 kin; EV33 OQ-1) |

## 3. Functional Requirements

### 3.1 Consolidation duty, exemptions and control (Sección 9)

- **SV-COA-FR-224:** The system shall implement the consolidation duty with
  its statutory exemption: a *controladora* (controlling entity) presents
  *estados financieros consolidados* (consolidated financial statements)
  including ALL its subsidiaries, EXCEPT (i) where BOTH 9.3 conditions hold —
  the controladora is itself a subsidiary AND its ultimate (or an
  intermediate) controladora produces consolidated GPFS complying with full
  NIIF or this Norma —   the controladora needs not present consolidated FS;
  and (ii) subsidiaries within the 9.3A held-for-sale exclusion (FR-225);
  plus the 9.3C case — a controladora having NO subsidiaries other than
  those not consolidated under 9.3A/9.3B presents NO consolidated FS (with
  the 9.23A disclosures emitted);
  the exemption is recorded as a dated determination on the group-structure
  record with its two 9.3 conditions evidenced (D15 snapshot-on-write;
  re-assessment on group events). **Reporting-entity boundary (CC kin,
  binding):** the consolidation perimeter is the REPORTING-ENTITY boundary —
  a *entidad que informa* that may be a legal entity or a part of one
  (EVID-282 xref: Sec 2 reporting entity ≠ legal entity, 32_ párrs
  2.39-2.41) — which by design does NOT coincide with the Código de Comercio
  personality-at-inscription boundary (legal personality perfected and
  extinguished by Registro de Comercio inscription, CC Art. 25), consumed
  from `commercial-legal/04_society-types.md` SV-CML-FR-048 BY ID: an
  inscribed sociedad holds personality for commercial-law purposes while its
  consolidation perimeter is fixed solely by the control model below — the
  system shall never derive consolidation scope from registry-inscription
  state, and never assert personality/consolidation equivalence in either
  direction.
  (LB-001; SV-CML-FR-048 by id; EVID-282)
- **SV-COA-FR-225:** The system shall implement the held-for-sale
  subsidiary exclusion with its one-year clock and restatement rule: a
  subsidiary acquired and held with the intention of sale or disposal within
  ONE YEAR from its acquisition date is NOT consolidated — it is accounted
  for per Sección 11 as an 11.8(d) held-for-sale investment (classification
  mechanics owned by `03_financial-instruments-fx.md` by id) — with the
  9.23A disclosures; the clock runs from the acquisition date (D15
  snapshot); when the subsidiary is NOT disposed of within the year: (a)
  default — the controladora consolidates the subsidiary FROM THE
  ACQUISITION DATE and, the acquisition date being in a prior period, the
  corresponding PRIOR PERIODS ARE RESTATED (re-expression), while (b) the
  outside-control continuation — where the delay is caused by events or
  circumstances OUTSIDE the controladora's control AND sufficient evidence
  of the maintained sale commitment exists at the presentation date — keeps
  the 9.3A treatment (no consolidation, no restatement); the clock branch
  chosen is recorded with its evidence.
  (LB-001; EVID-282)
- **SV-COA-FR-226:** The system shall implement the control determination:
  an investor determines whether it is a controladora REGARDLESS OF THE
  NATURE OF ITS INTEREST in the investee (de-facto control — equity
  percentage alone never decides; 9.4), and an investor CONTROLS an
  investee when ALL three elements of the 9.4B triad
  hold — (a) *poder* (power) over the investee: existing rights giving the
  current ability to direct the *actividades relevantes* (relevant
  activities — those significantly affecting returns); (b) exposure, or
  rights, to VARIABLE RETURNS from involvement; and (c) the ability to USE
  its power to affect those returns; with (i) the MAJORITY PRESUMPTION —
  holding, directly or indirectly through subsidiaries, a majority of
  voting rights presumes control WITHOUT evaluating the triad, the
  presumption REFUTABLE by clearly demonstrating one or more missing
  elements (e.g. another entity's existing contractual rights give it the
  current ability to direct relevant activities); (ii) power WITHOUT
  majority — via contractual agreements with other vote holders, rights
  from other contractual agreements, own voting rights, or combinations;
  (iii) POTENTIAL VOTING RIGHTS (9.8 — convertible instruments, options,
  forward contracts, of the investor AND of other parties) considered only
  when the holder has the PRACTICAL ability to exercise them (generally:
  currently exercisable), and decision rights combined with potential votes
  assessed together for power; and (iv) the AGENT/PRINCIPAL determination
  (9.12) — a decision-maker assessing control determines whether it is a
  *principal* (controls) or an *agente* (agent: a party dedicated primarily
  to acting on behalf and for the benefit of another party, hence NOT
  controlling when exercising its decision authority; a decision-maker is
  not an agent merely because others benefit from its decisions), and
  whether ANOTHER decision-making entity is acting as the investor's agent
  (power held and exercised through the agent belongs to the principal); the
  determination is a dated assessment record with re-assessment triggers
  (changes in voting rights, potential votes, contractual arrangements,
  decision-maker arrangements).
  (LB-001; EVID-282)

### 3.2 Consolidation mechanics (Sección 9)

- **SV-COA-FR-227:** The system shall implement consolidation mechanics:
  the consolidated FS present the group as a SINGLE reporting entity by (a)
  combining controladora and subsidiaries LINE BY LINE, aggregating items of
  similar nature (assets, liabilities, equity, income, expenses); (b)
  eliminating the carrying amount of the investment in each subsidiary
  against the parent's share of equity, and eliminating in FULL intragroup
  balances, transactions, income and expenses; (c) presenting
  *participaciones no controladoras* (non-controlling interests) SEPARATELY
  — within equity, separately from the owners of the controladora, and
  separately in the statement (profit attributable to NCI and to the
  controladora's owners); (d) applying the intragroup-loss rule: intragroup
  losses are eliminated like any intragroup item, and the resulting
  carrying amount is checked for IMPAIRMENT per Sección 27 (`04` by id for
  the testing mechanics); (e) using SUBSIDIARY FS AT THE SAME DATE as the
  controladora's, or — where impracticable — adjusting for the effects of
  significant transactions or events between the dates; and (f) applying
  UNIFORM accounting policies for similar transactions (a subsidiary using
  different policies is adjusted to the group's when its FS are used for
  consolidation).
  (LB-001; EVID-282)

### 3.3 Loss of control and NCI transactions (Sección 9)

- **SV-COA-FR-228:** The system shall implement LOSS OF CONTROL: when a
  controladora loses control of a subsidiary, it (a) DERECOGNIZES the
  assets, liabilities, any NCI and the goodwill of the subsidiary
  previously recognized in the consolidated FS; (b) recognizes any RETAINED
  INTEREST at its FAIR VALUE at the date control is lost (that FV becoming
  the initial carrying amount for subsequent accounting under the
  applicable section); and (c) recognizes the resulting GAIN OR LOSS in
  profit or loss attributable to the controladora's owners; RECLASSIFICATION
  RULE: amounts of accumulated OCI previously recognized in respect of the
  subsidiary are accounted for as if the retained interest had been
  disposed of directly — reclassified to P&L or transferred within equity
  as the section requires — EXCEPT that FOREIGN-EXCHANGE TRANSLATION
  differences of a foreign subsidiary (Sec 30 cumulative translation) are
  NEVER recycled to profit or loss (they may transfer within equity, e.g.
  to a separate component, on final disposal); partial-loss and retained-
  interest transitions follow 9.18A-9.18B (retained interest subsequently
  per Sec 11/14 — FV/fair-value-less-costs or equity-method routing per
  FR-242's menus).
  (LB-001; EVID-282; FX-OCI kin `03` by id)
- **SV-COA-FR-229:** The system shall implement transactions with NCI
  WITHOUT loss of control as EQUITY TRANSACTIONS (9.20A): acquisitions and
  disposals of NCI interests that leave control intact are transactions
  with owners acting in their capacity as owners — the carrying amounts of
  the subsidiary's ASSETS (including goodwill) and LIABILITIES are NOT
  REMEASURED, NO gain or loss is recognized in profit or loss, and the
  difference between the consideration (or proceeds) and the carrying amount
  of the NCI transacted adjusts EQUITY (attributable to the owners of the
  controladora), with presentation/disclosure of the nature and amount of
  the movement.
  (LB-001; EVID-282)

### 3.4 Separate FS policy menu and combined FS (Sección 9)

- **SV-COA-FR-230:** The system shall implement the 9.26 separate-FS policy
  menu PER CATEGORY: in *estados financieros separados* (separate financial
  statements) prepared under this Norma, an entity measures its investments
  in subsidiaries, associates and jointly controlled entities under ONE of
  (a) COST LESS IMPAIRMENT; (b) FAIR VALUE with FV changes recognized in
  profit or loss; or (c) the EQUITY METHOD following the 14.8 procedures —
  applying the SAME policy to ALL investments within a category
  (subsidiaries; associates; jointly controlled entities) while DIFFERENT
  policies across categories are permitted; the election is recorded on the
  investment-policy record per category (D15: resolves as-of election date,
  snapshots; changes follow the policy-change rules of `01` FR-014 — an
  election change IS a policy change).
  (LB-001; EVID-282)
- **SV-COA-FR-231:** The system shall implement the 9.25A separate-FS-only
  presentation: a controladora EXEMPT from presenting consolidated FS under
  the 9.3 exemption (FR-224) may present SEPARATE financial statements as
  its ONLY financial statements — the FS-set generator supports this
  variant (the separate FS under the 9.26 menu being the complete set),
  flagged as the 9.25A presentation, with the 9.3-exemption determination
  on record as its precondition (kin to `01` FR-005's 1.7 own-status rule:
  a controladora may also present separate FS under this Norma even when it
  consolidates under full NIIF or another GAAP — consumed by id there).
  (LB-001; EVID-282; `01` FR-005 by id)
- **SV-COA-FR-232:** The system shall implement *estados financieros
  combinados* (combined financial statements): where a set of entities
  under common control (or a grouping otherwise permitted by the Norma's
  9.28 conditions) presents combined FS rather than consolidated FS of a
  controladora, the preparation applies intragroup eliminations and uniform
  accounting policies as in consolidation (FR-227 mechanics, mutatis
  mutandis, uniform reporting date included), and the generator emits the
  9.30 disclosures: (a) the FACT that the FS are combined FS; (b) the
  REASON they are prepared; (c) the BASIS for determining which entities
  are included; (d) the basis of preparation; and (e) the related-party
  disclosures of Sección 33 (FR-244..249 by id).
  (LB-001; EVID-282)

### 3.5 Business combinations (Sección 19 + Apéndice 19A)

- **SV-COA-FR-233:** The system shall implement the ACQUISITION METHOD for
  business combinations (combinations between entities NOT under common
  control — common-control combinations are outside Sec 19's scope and
  follow the developed-policy hierarchy of `01` FR-013): identify the
  acquirer; determine the acquisition date (the date control transfers per
  the FR-226 model — D15 anchor); recognize and measure the identifiable
  assets acquired and liabilities assumed at their ACQUISITION-DATE FAIR
  VALUE (19.12-19.13), including (i) intangibles meeting the Sección 18
  criteria with reliably measurable FV (19.16 — with its disproportionate-
  cost relief routed through `01` FR-012's registry and the 19.38
  disclosures emitted here by id); (ii) assumed CONTINGENT LIABILITIES
  recognized when their FV can be reliably measured, EVEN IF NOT PROBABLE
  that resources will be transferred (19.17-19.19 — the 21.4(b)/21.12
  probability gates do not apply to assumed contingent liabilities);
  (iii) deferred taxes per Sección 29 (`08` by id); and (iv) employee-
  benefit liabilities/assets per Sección 28 (`05` by id).
  (LB-002; EVID-289)
- **SV-COA-FR-234:** The system shall measure NCI in a business combination
  at the PROPORTIONATE AMOUNT ONLY: the *participación no controladora* is
  recognized "por la parte proporcional de la participación no controladora
  en los importes reconocidos de los activos netos identificables" (19.14) —
  the engine offers NO fair-value-of-NCI election, this being a hard PYMES
  encoding; the full-NIIF contrast (IFRS 3's FV-at-acquisition election) is
  recorded as a boundary note only (LB-007, secondary), surfaced on the
  framework-routing flag of `01` FR-001 for niif_plenas group entities —
  never implemented as an alternative measurement path in this wave.
  (LB-002; LB-007 secondary contrast; EVID-289/299)
- **SV-COA-FR-235:** The system shall compute GOODWILL at the acquisition
  date as the excess of the sum of (a) the consideration TRANSFERRED
  (measured per 19.25, including any consideration payable under a
  contingent-consideration agreement, at FR-238's initial measurement),
  plus (b) the NCI amount (FR-234's proportionate measurement), plus (c)
  the acquisition-date FAIR VALUE of the previously-held equity interest in
  STEP ACQUISITIONS (FR-236) — over (d) the NET of the acquisition-date
  amounts of the identifiable assets acquired and liabilities assumed
  (FR-233); where the sum (a)+(b)+(c) is BELOW (d), the BARGAIN-PURCHASE
  result of FR-237 applies instead; goodwill recognized routes to the
  goodwill account of the consolidated COA and is allocated to CGUs for
  impairment testing per 27.23-27.27 (`04` by id).
  (LB-002; EVID-289)
- **SV-COA-FR-236:** The system shall implement STEP ACQUISITIONS: when an
  acquirer obtains control of an acquiree in which it held an equity
  interest immediately before the acquisition date, the acquirer REVALUES
  its PREVIOUSLY-HELD interest to FAIR VALUE at the acquisition date and
  recognizes the resulting gain or loss in PROFIT OR LOSS (19.29) — the
  revalued amount entering the goodwill formula as FR-235(c); the same
  revalue-through-P&L discipline applies to stakes that become subsidiaries
  or jointly controlled entities from associate status (14.8(i)/15 kin —
  FR-242).
  (LB-002; LB-003; EVID-289)
- **SV-COA-FR-237:** The system shall implement BARGAIN PURCHASES: where
  the goodwill formula of FR-235 yields a NEGATIVE residual (net
  identifiables exceed consideration + NCI + revalued prior stake), the
  system FIRST requires a RE-ASSESSMENT pass — re-examining whether all
  identifiable assets acquired and liabilities assumed have been recognized
  and measured per 19.13-19.21 (and the measurement of the components) —
  and only after that re-assessment confirms the residual does a GAIN arise,
  recognized in PROFIT OR LOSS (19.23-19.24); the re-assessment pass and
  its conclusion are recorded on the business-combination record.
  (LB-002; EVID-289)
- **SV-COA-FR-238:** The system shall implement CONTINGENT CONSIDERATION
  with its fallback discipline: the obligation to pay contingent
  consideration is recognized at its acquisition-date FAIR VALUE as part of
  consideration transferred when that FV can be measured RELIABLY without
  disproportionate cost or effort; where it CANNOT, the initial measurement
  uses the MOST-LIKELY AMOUNT — and that fallback amount is NOT
  subsequently RE-MEASURED (19.26-19.27, hard encoding: no re-estimation of
  the fallback); classification of the instrument follows Sección 22
  (`05` by id): equity-classified contingent consideration is NOT
  remeasured; liability-classified consideration is subsequently measured at
  FV with changes in P&L (Sec 11/12 mechanics owned by `03` by id).
  (LB-002; EVID-289)
- **SV-COA-FR-239:** The system shall implement the MEASUREMENT PERIOD: the
  acquirer may adjust the provisional amounts recognized for a business
  combination within TWELVE MONTHS from the acquisition date, to reflect
  new information obtained about FACTS AND CIRCUMSTANCES THAT EXISTED AT
  the acquisition date (retrospective adjustment, goodwill-affecting per
  FR-235) — the window closes at acquisition date + 12 months (D15 clock),
  after which adjustments to acquisition accounting enter ONLY the
  prior-period error-correction track of `01` FR-018; the measurement-
  period status of each provisional amount is tracked on the combination
  record (open/locked, with lock date).
  (LB-002; EVID-289)
- **SV-COA-FR-240:** The system shall expense ACQUISITION-RELATED COSTS
  (professional, legal, valuation and similar advisory fees) as INCURRED in
  the acquirer's P&L (19.32) — they are never capitalized into the
  combination's cost; costs of issuing debt or equity incurred in the
  combination follow Sections 11/22 (`03`/`05` by id); the expense routing
  is a hard account-mapping rule of the acquisition-entry builder.
  (LB-002; EVID-289)
- **SV-COA-FR-241:** The system shall implement the BUSINESS-VS-ASSET
  determination (Apéndice 19A): an acquired set of activities and assets is
  a BUSINESS when it includes INPUTS plus SUBSTANTIVE PROCESSES
  significantly capable of contributing to the ability to create OUTPUTS
  (products — goods, services, investment or other ordinary income — being
  the result of inputs and processes applied to them); the engine offers
  the OPTIONAL CONCENTRATION TEST (19A.3): where SUBSTANTIALLY ALL the fair
  value of the gross assets acquired is concentrated in a single
  identifiable asset or group of similar identifiable assets, the set is
  NOT a business (assessment ends); where the test fails or is not elected,
  the SUBSTANTIVE-PROCESS evaluation applies (19A.4-19A.10, Figure 19.1
  decision tree: whether the acquired set includes an organized workforce
  with the necessary skills/knowledge to perform processes, or inputs that
  significantly contribute to outputs, per the tree's branches); an
  asset-acquisition result routes the consideration to the asset sections
  (Sec 11/13/17/18 etc.) and OUT of Sec 19's machinery — the determination
  (test elected? passed? tree branch) is recorded on the transaction with
  its evidence.
  (LB-002; EVID-289)

### 3.6 Associates and joint arrangements (Secciones 14-15)

- **SV-COA-FR-242:** The system shall implement associate accounting
  (Sección 14): *influencia significativa* (significant influence) — the
  power to intervene in the financial and operating policy decisions of an
  *asociada* (associate) without control or joint control — is assessed
  with the 20% PRESUMPTION both ways: ≥20% of voting rights (directly or
  indirectly) PRESUMES significant influence unless clearly disproven;
  <20% PRESUMES its absence unless clearly proven; another investor's
  majority or substantial holding does NOT preclude it; the accounting
  policy for ALL associate investments is ONE entity-wide menu choice
  (14.4): (a) COST MODEL — cost less accumulated impairment (Sec 27,
  `04` by id), quoted-price associates excluded; (b) EQUITY METHOD
  (14.8) — same-date associate FS or the most recent available with
  adjustments for significant intervening transactions where impracticable;
  uniform investor policies unless impracticable; recognition of the share
  of results and OCI changes; suspension of loss recognition once the share
  of losses equals or exceeds the carrying amount (including instruments
  forming part of the net investment), with subsequent losses provisioned
  ONLY for incurred legal/constructive obligations or payments made on the
  associate's behalf, and resumption of profit recognition only after
  unrecognized losses are absorbed; discontinuation on losing significant
  influence — revaluation of the previously-held stake to FV through P&L
  when it becomes a subsidiary or jointly controlled entity, derecognition
  at (consideration received + FV of retained interest) − carrying amount
  (incl. goodwill) on disposal, fresh cost basis when influence is lost
  otherwise; (c) FAIR VALUE MODEL (14.9) — FV with changes in P&L, the cost
  model applying to any associate whose FV cannot be measured reliably
  without disproportionate cost (relief registry `01` FR-012 by id); an
  associate with a PUBLISHED QUOTED PRICE is measured under the FV model
  (14.7); investments classify as NON-CURRENT assets; the 14.12-14.14
  disclosures (policy, carrying amounts, FV of quoted equity-method
  investments) are emitted.
  (LB-003; LB-001 for the 9.26-separate-FS interaction; EVID-282)
- **SV-COA-FR-243:** The system shall implement joint-arrangement
  accounting (Sección 15) by FORM first: (a) *operaciones controladas de
  forma conjunta* (jointly controlled operations) — the party recognizes
  the ASSETS it controls and the LIABILITIES it incurs, its expenses and
  its share of the revenue from the arrangement; (b) *activos controlados
  de forma conjunta* (jointly controlled assets) — the party recognizes its
  share of the jointly controlled assets classified BY NATURE, any
  liabilities it incurs, its share of jointly incurred liabilities, and its
  share of revenue/expenses; (c) *entidades controladas de forma conjunta*
  (jointly controlled entities, JCE) — arrangements embodied in a separate
  entity in which each party holds a participation; JCE INVESTMENTS are
  measured under ONE entity-wide menu (15.9): cost model (15.10, less
  impairment per Sec 27) \| EQUITY METHOD (15.13) \| FAIR VALUE model
  (15.14), with the disproportionate-cost FV→cost fallback (15.15, registry
  `01` FR-012 by id) and the 15.16 disclosures — policy, carrying amounts
  (4.2(k)), FV of quoted equity-method JCEs, and the AGGREGATE of
  commitments related to JCEs including jointly incurred commitments;
  NON-CONTROLLING-PARTY ROUTING (parties participating WITHOUT joint
  control): a participation in a JCE routes to Sección 11 (financial
  instruments) unless the party has SIGNIFICANT INFLUENCE, in which case
  Sección 14 (FR-242) applies (15.18A); a party in a joint OPERATION
  without joint control accounts per the 15.5 operations rules; a party in
  jointly controlled ASSETS without joint control accounts per the 15.7
  asset-share rules (15.18B).
  (LB-004; EVID-282)

### 3.7 Related parties (Sección 33)

- **SV-COA-FR-244:** The system shall implement the related-party
  determination as a dimension on partners/entities, assessed on SUBSTANCE
  over legal form: a *parte relacionada* (related party) is (a) a PERSON —
  a member of *personal clave de la gerencia* (key management personnel, of
  the entity or of a controladora) or a CLOSE FAMILY MEMBER of such person;
  a holder of CONTROL or JOINT CONTROL; a holder of significant influence;
  and (b) an ENTITY — same-GROUP members (each controladora, subsidiary and
  fellow subsidiary related to the others); an associate or JCE of the
  entity or of a group member; two JCEs of the same third party; a JCE of a
  third party and an associate of that same third; post-employment plans
  for the entity's or a related entity's workers (and sponsoring employers
  when the reporting entity IS a plan); an entity CONTROLLED or JOINTLY
  CONTROLLED by a person in (a); an entity or group member PROVIDING KMP
  SERVICES to the entity or its controladora; and a person with significant
  influence over, or KMP membership in, the entity (or its controladora);
  the NOT-NECESSARILY-RELATED list is encoded as negative rules — two
  entities merely SHARING a director or other KMP; two parties merely
  SHARING JOINT CONTROL of a JCE; financiers, unions, public utilities and
  government departments/agencies by virtue of their NORMAL dealings (even
  where they affect freedom of action or participate in decision-making);
  and economically DEPENDENT customers, suppliers, franchisors,
  distributors or exclusive agents (significant transaction volume alone
  does not create relatedness).
  (LB-006; EVID-298)
- **SV-COA-FR-245:** The system shall disclose the controladora
  relationships REGARDLESS of transactions: the relationships between a
  controladora and its subsidiaries are disclosed whether or not there have
  been transactions between them; the generator emits the NAME of the
  entity's controladora and, if different, the name of the *parte
  controladora última* (ultimate controlling party) of the group; where
  NEITHER produces FS available for public use, the name of the nearest
  more-important controladora that does (if any) is disclosed instead —
  the group-structure record feeds this identification (FR-226 control
  chain, upstream).
  (LB-006; EVID-298)
- **SV-COA-FR-246:** The system shall disclose KMP remuneration IN THE
  AGGREGATE: KMP are the persons with authority and responsibility for
  planning, directing and controlling the entity's activities, directly or
  indirectly, including ANY administrator (executive or not) or equivalent
  governance organ; *remuneraciones* (remuneration) comprise ALL employee
  benefits per Sección 28 (short-term, post-employment, termination,
  share-based payments included), paid, payable or provided by or on behalf
  of the entity (including by the controladora or a shareholder) in
  exchange for services, and consideration paid to the entity's controladora
  for goods/services provided; the disclosure is the TOTAL for KMP — the
  aggregate is never broken down per person by this rule; MANAGEMENT-ENTITY
  CARVE-OUT: where KMP services come from a management (*gestión*) entity,
  the amounts INCURRED by the entity for those services are disclosed
  instead of the gestora's own remuneration data; the compensation figures
  are consumed from the payroll wave's statutory engine BY ID (no payroll
  computation re-derived here — two-track invariant).
  (LB-006; EVID-298; payroll by id)
- **SV-COA-FR-247:** The system shall implement related-party
  transaction/balance/commitment disclosures BY CATEGORY: where transactions
  with related parties exist, the generator discloses the NATURE of each
  relationship and the information on transactions, outstanding balances
  (including COMMITMENTS) and provisions needed to understand the potential
  effects: (a) the AMOUNT of transactions; (b) outstanding BALANCES
  including commitments, with their terms and conditions (including whether
  guaranteed, and the nature of consideration settled); (c) PROVISIONS for
  doubtful related-party receivables; and (d) the EXPENSE recognized for
  bad and doubtful debts from related parties — split SEPARATELY for the
  four categories: (i) entities with control, joint control or significant
  influence OVER the entity; (ii) entities OVER WHICH the entity exercises
  control, joint control or significant influence; (iii) KMP of the entity
  or its controladora (in TOTAL); (iv) other related parties; the
  transaction-type catalogue (33.12: purchases/sales of finished and
  unfinished goods; real estate and other assets; services; leases; R&D
  transfers; license arrangements; financing arrangements including loans
  and equity contributions; collateral guarantees and avales; conditional
  commitments to do/not do; settlements of liabilities on either side;
  parent/subsidiary participation in a shared-risk defined-benefit plan)
  drives the tagging surface on moves/partners; similar items may be
  AGGREGATED unless separate disclosure is necessary for understanding.
  (LB-006; EVID-298)
- **SV-COA-FR-248:** The system shall BLOCK the arm's-length assertion: it
  shall not emit or permit the statement that related-party transactions
  were carried out on terms EQUIVALENT to those prevailing in
  arm's-length/mutually-independent transactions UNLESS those conditions
  can be JUSTIFIED or DEMONSTRATED — the assertion requires a substantiation
  record (evidence basis) attached before the disclosure can carry it.
  (LB-006; EVID-298)
- **SV-COA-FR-249:** The system shall implement the GOVERNMENT-RELATED-
  ENTITY exemption with its substitute disclosures: a reporting entity is
  EXEMPT from FR-247's transaction/balance/commitment disclosure
  requirements for dealings with (a) a GOVERNMENT having control, joint
  control or significant influence over the reporting entity, and (b)
  another entity that is related ONLY because the SAME government has
  control, joint control or significant influence over both — and, when the
  exemption is engaged, the generator emits the 33.15 SUBSTITUTE
  disclosures for those exempted transactions and balances: (i) the NAME of
  the government and the NATURE of its relationship with the entity
  (control, joint control or significant influence); (ii) the nature and
  amount of EACH individually significant transaction; and (iii) for
  transactions collectively but not individually significant, a
  qualitative or quantitative INDICATION of their SCOPE (types per 33.12).
  (LB-006; EVID-298)

### 3.8 Post-period events (Sección 32)

- **SV-COA-FR-250:** The system shall implement the post-period-events gate
  — *hechos ocurridos después del periodo sobre el que se informa* (events
  after the reporting period): events between the reporting-period end and
  the FS authorization date are classified as (a) ADJUSTING — providing
  evidence of conditions that EXISTED at the period end (worked examples:
  resolution of litigation confirming a present obligation; impairment
  evidence; determination of cost/income amounts; discovery of fraud or
  errors) → the RECOGNIZED AMOUNTS in the FS are ADJUSTED; vs
  (b) NON-ADJUSTING — arising from conditions created AFTER the period end
  (worked examples: post-period market-price or FX declines; gains from
  litigation arising exclusively from post-period events) → NO adjustment of
  recognized amounts, but disclosure of (i) the NATURE of the event and
  (ii) an ESTIMATE of its financial effects, or a statement that such an
  estimate cannot be made; each post-period event carries its
  classification, its condition-existing evidence, and its disclosure
  state (D15: classified as-of the authorization window).
  (LB-005; EVID-298)
- **SV-COA-FR-251:** The system shall implement the 32.11 DIVIDENDS rule:
  dividends AGREED (declared) to holders of equity instruments AFTER the
  reporting-period end are NOT recognized as a LIABILITY at the period end
  — no dividend payable arises from a post-period agreement in the
  reporting-date balance sheet — and the amount may be presented as a
  SEGREGATED COMPONENT OF RETAINED EARNINGS (*ganancias acumuladas*) at the
  period end; the liability recognition occurs at the declaration event per
  `05_liabilities-equity-benefits.md` FR-175 (consumed BY ID — declaration
  mechanics, the CC distribution-capacity overlay SOQ-49 and the dividend
  tax routing are that file's surfaces; this file owns the 32.11
  reporting-date no-liability boundary and the segregated presentation
  toggle).
  (LB-005; EVID-298; `05` FR-175 by id)
- **SV-COA-FR-252:** The system shall emit the AUTHORIZATION-DATE
  disclosure on every FS set: the DATE on which the FS were AUTHORIZED FOR
  ISSUE and WHO granted that authorization; where the entity's owners or
  others have the power to AMEND the FS after publication, that FACT is
  disclosed; the authorization date closes the post-period-review window of
  FR-250 (events after that date are outside the review scope).
  (LB-005; EVID-298)

## 4. Data Model

Layer semantics: all entities are Odoo-native config/dated records on the
multi-company chart-of-accounts engine (`l10n_sv_chart.*` + res.company /
res.partner surfaces) — the group model never emulates any external
regulator (the IASB/Consejo set the Norma; the company records its own
determinations). The CC registry-inscription state is commercial-legal's
surface (SV-CML-FR-048 by id) and is deliberately NOT a field of the
consolidation scope. No printed data table here warrants a CSV sidecar
(the control-assessment, menus and exemption branches are small config
sets; default none per plan).

**Group structure and control (res.company / l10n_sv_chart.control_assessment):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.company | parent_id (group chain) + sv_coa_consolidation_scope | m2o + select | consolidated · exempt_9_3 (both conditions evidenced) · held_for_sale_9_3A · not_subsidiary | FR-224, FR-225 |
| l10n_sv_chart.control_assessment | investee · date · conclusion | m2o · date · select | control · no_control (re-assessment triggers recorded; D15 snapshot-on-write) | FR-226 |
| l10n_sv_chart.control_assessment | triad_power · triad_returns · triad_link | boolean + evidence | 9.4B elements; power sources: majority (presumption refutable) · contractual · potential votes 9.8 · agent-held 9.12 | FR-226 |
| l10n_sv_chart.control_assessment | majority_presumption · refuted | boolean + evidence | 9.5 presumption refutation basis | FR-226 |
| l10n_sv_chart.control_assessment | agent_principal | select + evidence | principal · agent_of (m2o principal) · decision_maker_of_other | FR-226 |
| l10n_sv_chart.held_for_sale_clock | subsidiary · acquisition_date · deadline | m2o · date · computed | 1y clock (9.3A); branch: consolidate_restate_9_3B(a) · outside_control_continue_9_3B(b) (commitment evidence at presentation date) | FR-225 |

**Investment policy menus (l10n_sv_chart.investment_policy):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.investment_policy | scope | select | separate_fs_per_category (subsidiary · associate · jce) · associates_entity_wide_14_4 · jce_entity_wide_15_9 | FR-230, FR-242, FR-243 |
| l10n_sv_chart.investment_policy | method | select | cost_less_impairment · fv_through_pnl · equity_method | FR-230 (9.26), FR-242 (14.4), FR-243 (15.9) |
| l10n_sv_chart.investment_policy | quoted_price_override | boolean | 14.7: quoted associates/JCEs → fv_through_pnl; disproportionate-cost fallback rows → cost (registry `01` FR-012 by id) | FR-242, FR-243 |
| res.company | sv_coa_combined_fs | boolean + disclosures | combined-FS variant with the 9.30(a)-(e) disclosure set | FR-232; FR-231 separate-only variant flag |

**Business combinations (l10n_sv_chart.business_combination):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.business_combination | acquirer · acquiree · acquisition_date | m2o · m2o · date | D15 anchor for all measurements; control transfer per FR-226 | FR-233 |
| l10n_sv_chart.business_combination | identifiables | one2many | per-line FV at acquisition date: assets, liabilities, intangibles (19.16 relief flag), assumed contingent liabilities (19.17-19.19), DT (08 by id), benefits (05 by id) | FR-233 |
| l10n_sv_chart.business_combination | nci_measure | select (locked) | proportionate_19_14 ONLY — no fv option encoded | FR-234 |
| l10n_sv_chart.business_combination | goodwill_calc | computed + components | consideration 19.25 + nci + prior_stake_fv − net_identifiables; bargain residual with re_assessment pass + pass date | FR-235, FR-237 |
| l10n_sv_chart.business_combination | step_acquisition | boolean + prior_stake_fv + p&l entry | 19.29 revaluation through P&L | FR-236 |
| l10n_sv_chart.contingent_consideration | initial_basis · most_likely_locked | select · boolean | fv_reliable · most_likely_fallback (NO remeasurement of fallback); classification + subsequent FV per 03/05 by id | FR-238 |
| l10n_sv_chart.business_combination | measurement_period_lock | date | acquisition_date + 12m; after lock → error track only (`01` FR-018 by id) | FR-239 |
| l10n_sv_chart.business_combination | acquisition_costs_account | m2o account | expensed-as-incurred routing (19.32); issuance costs → 03/05 by id | FR-240 |
| l10n_sv_chart.business_combination | business_vs_asset | select + tree path | business · concentration_test_passed · concentration_failed_or_not_elected → tree branch (19A.4-19A.10); asset → route out of Sec 19 | FR-241 |

**Loss of control / NCI transactions (l10n_sv_chart.policy_event kinds):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.policy_event | kind extension | select | loss_of_control (derecognize + retained_at_fv + p&l; fx_oci_never_recycled flag on the reclass rows) · nci_equity_transaction_9_20A | FR-228, FR-229 |

**Related parties (res.partner / l10n_sv_chart.rp_disclosure):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| res.partner | sv_coa_related_party | boolean + kind | person_kmp · person_close_family · person_control_jsi_si · entity_group_member · entity_associate_jce · entity_two_jce_same_third · entity_jce_associate_third · entity_post_employment_plan · entity_kmp_controlled · entity_kmp_services · person_si_kmp | FR-244 |
| res.partner | sv_coa_rp_not_related_guard | boolean | negative rules: shared_kmp · shared_joint_control · financier_union_utility_government_normal · economic_dependence only | FR-244 |
| res.partner | sv_coa_rp_government_exempt | boolean + government m2o | 33.11 exemption engaged; substitute set 33.15 emitted instead of 33.9 | FR-249 |
| res.company | sv_coa_controladora_name / ultimate | related fields | 33.6 naming incl. nearest publishing parent | FR-245 |
| l10n_sv_chart.rp_disclosure | category | select | controlling_over_entity · controlled_by_entity · kmp_total · other_related (33.10 split) | FR-247 |
| l10n_sv_chart.rp_disclosure | kmp_remuneration_total | monetary + feed id | aggregate per 33.7; payroll engine by id; management-entity amounts recorded | FR-246 |
| l10n_sv_chart.rp_disclosure | arms_length_claim | boolean + substantiation | blocked unless justified/demonstrated | FR-248 |

**Post-period events (l10n_sv_chart.post_period_event / FS set):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_sv_chart.post_period_event | kind · condition_existed_evidence | select · text | adjusting_32_5 (amounts adjusted) · non_adjusting (nature + estimate or cannot-estimate statement) | FR-250 |
| l10n_sv_chart.post_period_event | dividend_post_period | boolean | 32.11: no liability at period end; segregated retained-earnings toggle (kin `05` FR-175 distribution row by id) | FR-251 |
| res.company / period close | sv_coa_fs_authorization | date + who + amendable | authorization-for-issue disclosure; closes FR-250 window | FR-252 |

## 5. Odoo Mapping

Layer semantics for this file: the multi-entity accounting layer is
Odoo-native — group structure rides res.company's multi-company hierarchy,
investments ride the account.account/account.move engines, related-party
tags ride res.partner, and the consolidation/combination/FS-disclosure
builders are client report logic. No FR here touches DTE generation or
transmission (an architecture-split surface per
`shared/docs/saas-thin-client-architecture.md`); although consolidation
spans companies, it spans them through Odoo's OWN multi-company engine,
not through a SaaS-side service — every row is therefore `odoo` (default
per plan; no `saas`/`shared` rows introduced).

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-224 | odoo | res.company + l10n_sv_chart | consolidation_scope | 9.2 duty + 9.3 two-condition exemption; reporting-entity boundary NEVER derived from CC inscription (SV-CML-FR-048 by id; 2.39-2.41 kin) |
| FR-225 | odoo | l10n_sv_chart.held_for_sale_clock | 1y clock + branch | 11.8(d) classification = 03 by id; 9.3B(a) restate vs 9.3B(b) outside-control continuation |
| FR-226 | odoo | l10n_sv_chart.control_assessment | triad + presumption + potential votes + agent/principal | D15 dated assessments with re-assessment triggers |
| FR-227 | odoo | account.move (consolidation entries) | line-by-line + eliminations | NCI separate equity/caption accounts; intragroup-loss impairment check → 04 by id; uniform date/policies |
| FR-228 | odoo | l10n_sv_chart.policy_event + account.move | loss_of_control | retained at FV; gain/loss P&L; fx_oci_never_recycled hard flag on reclass rows |
| FR-229 | odoo | account.move | equity-only NCI entries | 9.20A: no P&L, no asset remeasurement; equity attributable-to-owners adjustment |
| FR-230 | odoo | l10n_sv_chart.investment_policy | per-category menu | 9.26: cost−impairment \| fv-pnl \| equity (14.8 procedures); same-within-category rule enforced |
| FR-231 | odoo | res.company FS-set config | separate-only flag | 9.25A precondition = 9.3 exemption on record; kin 01/FR-005 |
| FR-232 | odoo | report layer | combined-FS variant | 9.30(a)-(e) disclosures; eliminations + uniform policies/date |
| FR-233 | odoo | l10n_sv_chart.business_combination | acquisition entry builder | FV identifiables incl. assumed contingent liabilities even if not probable; intangible relief → 01/FR-012 + 19.38; DT/benefits by id |
| FR-234 | odoo | l10n_sv_chart.business_combination | nci_measure locked | proportionate ONLY (19.14 print); full-NIIF FV election = boundary note (LB-007 secondary) |
| FR-235 | odoo | l10n_sv_chart.business_combination | goodwill formula | consideration + NCI + step-up FV − net identifiables; CGU allocation → 04 by id (27.23-27.27) |
| FR-236 | odoo | l10n_sv_chart.business_combination | step_acquisition | 19.29 revalue prior stake → P&L |
| FR-237 | odoo | l10n_sv_chart.business_combination | bargain re-assessment pass | then P&L gain (19.23-19.24) |
| FR-238 | odoo | l10n_sv_chart.contingent_consideration | fv or most-likely locked | fallback NOT remeasured; Sec 22 classification + subsequent FV = 03/05 by id |
| FR-239 | odoo | l10n_sv_chart.business_combination | measurement_period_lock | ≤12m; retrospective; after lock → error track (01/FR-018 by id) |
| FR-240 | odoo | account.account mapping | acquisition-cost expense | 19.32; issuance costs → 11/22 by id |
| FR-241 | odoo | l10n_sv_chart.business_combination | business_vs_asset | 19A optional concentration test + substantive-process tree (Fig 19.1); asset route exits Sec 19 |
| FR-242 | odoo | l10n_sv_chart.investment_policy | associates menu 14.4 | 20% presumption; cost \| equity (14.8 mechanics) \| FV; quoted→FV (14.7); disproportionate fallback → registry by id |
| FR-243 | odoo | l10n_sv_chart.investment_policy | JV forms + JCE menu 15.9 | operations 15.5 / assets 15.7-15.8 / entities; JCE cost \| equity \| FV; 15.18A/B routing |
| FR-244 | odoo | res.partner | related-party dimension | substance-over-form; NOT-related negative rules (33.4) |
| FR-245 | odoo | report layer | controladora/ultimate naming | regardless of transactions; nearest publishing parent fallback (33.6) |
| FR-246 | odoo | l10n_sv_chart.rp_disclosure | KMP aggregate | payroll feed by id (two-track invariant); management-entity carve-out |
| FR-247 | odoo | l10n_sv_chart.rp_disclosure | category-split (a)-(d) | amounts/balances+terms+guarantees/provisions/bad-debt expense; 33.12 catalogue tagging |
| FR-248 | odoo | l10n_sv_chart.rp_disclosure | arms_length_claim gate | blocked without substantiation record (33.13) |
| FR-249 | odoo | res.partner + report | government exemption | 33.11 exemption + 33.15 substitutes (name/nature-of-relationship; individually significant; scope indicator) |
| FR-250 | odoo | l10n_sv_chart.post_period_event | adjusting gate | 32.5 vs non-adjusting + nature/estimate disclosures; window closed by FR-252 |
| FR-251 | odoo | l10n_sv_chart.post_period_event | dividend flag | 32.11 no-liability at period end; segregated RE toggle; declaration = 05/FR-175 by id |
| FR-252 | odoo | res.company/period close | authorization date + who | post-publication amendability fact disclosed (32.9-32.10) |

Version-regime notes (D12/D15): the NIIF edition is a DATED regime row —
3rd edition (Feb-2025) applies to annual periods beginning 2027-01-01,
early adoption permitted (A1); SV 2025-2027 books may run under the 2nd
(2015) edition with the Tabla A1 delta as the vintage artifact (`08` by
id; 2nd-ed. full text not in corpus — SOQ-48). Edition-sensitive content
in THIS file (Tabla A1; txt PAGE 326-327): Sección 9 additions 9.3D,
9.4A-9.4C, 9.7A, 9.7B, 9.18A, 9.18B, **9.20A** (previously printed as
22.19 in the 2nd edition — NCI-equity-transaction behavior identical,
citation renumbered) and **9.25A**; Sección 15 additions **15.2A,
15.18A, 15.18B**; Sección 14 modifications 14.2/14.8/14.10/14.12-14.14
(the 20% presumption and menu substance unchanged); Secciones 19+19A, 32,
33 carry no Tabla A1 delta rows read — cited as 3rd-ed. print. D15
anchors: control assessments, exemption determinations, held-for-sale
clocks, acquisition-date measurements, the 12-month measurement window
and post-period-event classifications resolve as-of their own event dates
and snapshot on the record. Fiscal bridge: share-disposal carrying
amounts (incl. step-acquisition revaluations and loss-of-control FVs)
feed Ley ISR Art. 14 capital-gain computations ONLY through N8's
deferred-tax FRs (`08` by id — two-track invariant; OQ-2).

## 6. Acceptance Criteria

- **AC-001:** Given a step acquisition building from a 15% associate
  stake to 85% control, when the acquisition entry posts, then the
  previously-held 15% stake is revalued to fair value at the acquisition
  date with the gain in profit or loss, and the goodwill formula includes
  that revalued amount alongside consideration and the proportionate NCI
  (FR-236, FR-235).
- **AC-002:** Given an acquisition with a 30% non-controlling interest,
  when the acquisition entry builds, then the NCI line is measured ONLY
  at the proportionate share of the recognized net identifiable assets —
  the engine exposes no fair-value-of-NCI path (FR-234).
- **AC-003:** Given a puttable equity instrument of the parent held by a
  subsidiary (classified equity in the subsidiary's separate FS), when the
  parent's consolidated FS assemble, then that instrument presents as a
  financial LIABILITY at the parent level — the SV-COA-FR-167 case (d)
  routing consumed by id, with the consolidation perimeter from the
  control model, never from registry inscription (FR-224; SV-COA-FR-167
  by id).
- **AC-004:** Given a government-controlled entity, when its related-party
  disclosures run, then transactions with the controlling government and
  co-controlled entities are exempted from the category-split tables and
  the substitute set emits instead: government name + nature of the
  relationship, nature and amount of each individually significant
  transaction, and a qualitative/quantitative scope indication for the
  collectively-significant remainder (FR-249).
- **AC-005:** Given a held-for-sale subsidiary not disposed of within one
  year because the delay was within the controladora's control, when the
  clock expires, then the subsidiary is consolidated FROM the acquisition
  date and the corresponding prior periods are restated — while the same
  expiry with an outside-control delay and maintained commitment keeps
  the 11.8(d) treatment unconsolidated (FR-225).
- **AC-006:** Given a controladora electing its separate-FS policies, when
  the elections record, then subsidiaries are measured cost-less-
  impairment, associates under the equity method and JCEs at fair value —
  uniform WITHIN each category, different ACROSS categories permitted;
  a per-investment deviation inside one category is rejected (FR-230).
- **AC-007:** Given dividends agreed by the shareholders AFTER the
  reporting-period end, when the period closes, then NO dividend payable
  is recognized at the period end; the amount may show as a segregated
  component of retained earnings, and the liability arises only at the
  declaration event through `05`'s FR-175 mechanics (FR-251).
- **AC-008:** Given loss of control over a foreign subsidiary with an
  20% retained interest, when the loss-of-control entry posts, then the
  subsidiary's assets/liabilities/NCI/goodwill are derecognized, the
  retained interest opens at fair value, the gain/loss hits profit or
  loss — and the subsidiary's accumulated FX-translation OCI NEVER
  recycles to P&L (FR-228).
- **AC-009:** Given KMP remuneration disclosures, when the note emits,
  then the amounts appear as one aggregate total (never per-person),
  fed by id from the payroll engine, and where KMP services come from a
  gestión entity the disclosed figure is the cost of those services, not
  the gestora's internal pay data (FR-246).
- **AC-010:** Given an FS set being authorized, when the notes emit, then
  the authorization date and authorizer are disclosed on every set, and a
  post-period event after that date is rejected from the FR-250 review
  window (FR-252, FR-250).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-1 | SOQ-46 carried + consolidation-applicability kin: the SV NIIF-adopting instrument (Consejo de Vigilancia criteria per CC Arts. 443-444, or successor legislation) is NOT in the corpus — which SV groups must consolidate under NIIF-PYMES vs full NIIF (and whether the 9.3 exemption's "cumplan con las Normas NIIF de Contabilidad completas o con esta Norma" condition is satisfied by any SV filer) is external dated law (32_ Prólogo P12 leaves it to jurisdictions). Groups exist regardless of framework: FR-224..232 ship the engine framework-agnostically with NO invented SV thresholds; the framework-routing flag is `01` FR-001's informational config. Acquisition candidate ≥75 (same instrument as commercial-legal/03 OQ-002). | no | Takumi S8 (sources watch) | open |
| OQ-2 | Fiscal bridge watch (EVID-289 doubts/xref): Ley ISR Art. 14 fixes the capital-gain basis on share disposals against the fiscal cost of the shares — book carrying amounts here (9.26 cost, step-acquisition FV revaluations, loss-of-control retained-at-FV openings) will generally differ from that fiscal basis; the bridge is owned by N8's deferred-tax FRs (`08` by id) and is NEVER computed or overridden in this file. Confirm at implementation that the disposal event object exports both bases by id. | no | Takumi S8 (N8 interface) | open |
| OQ-3 | KMP remuneration feed design: FR-246's aggregate needs the payroll wave's statutory engine data by id (no payroll computation re-derived here — two-track invariant), including the share-based-payment component (Sec 26) and the management-entity carve-out amounts. Integration contract (which payroll identifiers, which period aggregation) to be fixed when the payroll requirements land. | no | Takumi S8 (payroll interface) | open |
