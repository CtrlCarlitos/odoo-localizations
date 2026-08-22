# HN — Payroll — IHSS cotizaciones: rate matrix, regime ceilings, contribution base & withholding mechanics

| Field   | Value |
|---------|-------|
| Country | hn |
| Topic   | payroll |
| Status  | draft |
| Authors | Takumi synthesis wave S-HN4 + controller |
| Updated | 2026-08-21 (W9 fold-ins: 145_/147_/146_ acquired — base composition RESOLVED to text) |

## 1. Purpose

This file defines the functional requirements for the Honduran Institute of
Social Security (*Instituto Hondureño de Seguridad Social*, IHSS) employee
and employer **contributions** (*cotizaciones*) layer of cluster P5. It owns:
the cotización matrix as DATED rows — IVM (*Invalidez, Vejez y Muerte*,
invalidity/old-age/death) employer 3.5% / worker 2.5% / State 0.5% (D. 48-2024,
from 28-may-2024, lex posterior over the superseded 2/1/0.5 statutory floor of
Ley del Seguro Social Art. 55-A ¶2, R-H49) and EM (*Enfermedad y Maternidad*,
sickness/maternity) employer 5% / worker 2.5% / State 0.5% (LI Art. 55-A ¶1,
in force, untouched by D.48) — yielding the combined worker withholding of
5.0% and employer charge of 8.5%; the TWO regime ceilings as separate
dated-row families (IVM L11,336.32→L11,903.13; EM L11,109.30→L11,903.13 for
2024/2025 — the 2025 equality is a coincidence, never merged, R-H50; post-2025
= Junta Directiva rows per actuarial study); the contribution-base semantics —
base = min(monthly remuneration, regime *techo* (ceiling)) per the LI Art. 55-B
"remuneración máxima" precedent (R-H51), with base COMPOSITION (13th/14th
month, overtime, bonuses) delegated to the unacquired Reglamento General (LI
Art. 100) and therefore held as a configuration flag, never hardcoded; the
withholding mechanics of LI Arts. 60-64 (withhold at salary payment date,
1-month cure window, employer-share deduction absolutely void, mora recargos,
State 15-day rhythm as informational); the affiliation scope and exclusions of
LI Arts. 1-7; the riesgos-profesionales branch frame (employer-only financing,
rate absent from corpus = config gap); the enforcement metadata (solvencia
gate, salarios-mínimos fine schedule, mora = employer assumes all benefits,
5-year/imprescriptible prescription); and the ISR/RAP consumption interfaces
(prestaciones non-gravable tagging; IVM techo export to file 05).

It does **not** own: incapacidad/subsidy mechanics — the RIT engine (3-day
employer wait, 66% subsidy, refrendo workflow, entitlement qualifiers,
episode keys) is owned by file 04 (`04_ihss-incapacidad.md`,
HN-PAYR-FR-141..170); this file cites the LI Arts. 34.b/39.b/42.2/45/90-92
frame that authorizes it, nothing more (CT Título V residual = file 09). It
does not own the SMM rows feeding the multa unit (file 01,
HN-PAYR-FR-001..040), 13th/14th-month mechanics (file 02,
HN-PAYR-FR-051..087), RAP/fondo/FOVIIF cotizaciones that CONSUME the IVM
techo (file 05, HN-PAYR-FR-181..215), jornada (06), vacaciones (07),
cesantía/preaviso (08), suspension/maternity CT residual (09), the salary
concept/records (10, cross-referenced for the LI Art. 106 definitional
recourse only), ISR deduction semantics (taxation/02, HN-TAX-FR-046..078,
consumed by id), the ISR plantilla engine including its IHSS-benefit
exclusion (taxation/04, HN-TAX-FR-121..153, esp. FR-130, consumed by id), or
any comprobante/retention-certificate surface (e-invoicing/03,
HN-EINV-FR-139/140 — IHSS issues no comprobante de retención for
cotizaciones in this corpus).

## 2. Legal Basis

Authority order (binding, per master evidence index): the CURRENT rate and
ceiling authority for IVM + both 2024/2025 ceilings = Decreto 48-2024 (`81_`,
G 36,545 28-may-2024; pp.2-3 OCR layer is AUTHORITATIVE over the
mojibake native layer — evidence quotes govern); the regime frame, EM rates,
superseded IVM floor, ceiling semantics, withholding mechanics, base
delegation and enforcement = Ley del Seguro Social (`87_`, D.140-1959
consolidated with D.80-2001 reforms, TSC judicial print; OCR-only reading;
edition defect per R-H65 — cite signature 1-jun-2001 + Gaceta 29,503
14-jun-2001, title-page dates are print noise). D-H1/D-H2/D-H3 bind
everything: every statutory value = dated rows resolved by the payslip
period (*hecho generador*), additive-only, never-guess.

| ID | Citation (Spanish) | English translation | Source file | Location |
|----|--------------------|---------------------|-------------|----------|
| LB-001 | D. 48-2024, Art. 1 (APORTE RÉGIMEN PREVISIONAL DEL IHSS): "Para el beneficio de Invalidez, Vejez y Muerte (IVM) «…» la tasa de cotización será el tres punto cinco por ciento (3.5%) para el empleador, de dos puntos cinco por ciento (2.5%) para el trabajador y de cero puntos cinco por ciento (0.5%) para el Estado. Para el cálculo del aporte del Estado «…» se hará en base del total de los afiliados activos en el [Instituto Hondureño] de Seguridad Social (IHSS). Estos porcentajes se aplicarán sobre los techos de cotización vigentes para este régimen." | IVM contribution rate: employer 3.5%, worker 2.5%, State 0.5%; the State share computed on the total of active affiliates; "these percentages apply over the contribution ceilings in force" (cap semantics resolved by R-H51: rates on salary capped at the techo, never a flat ceiling amount) | `hn/sources/81_Decreto_48-2024_IHSS_aportaciones.pdf` | D48-Art. 1 (p.3/4, = G p. A.11; OCR layer authoritative) (EV81:EVID-251) |
| LB-002 | D. 48-2024, Art. 2 (GRADUALIDAD): "Para los años 2024 y 2025 los techos de cotización serán los siguientes: Año 2024/2025 — Régimen [De] Invalidez, [Vejez] y muerte (IVM) L. 11,336.32 / L. 11,903.13 — Régimen [De] Enfermedad y Maternidad (EM) L. 11,109.30 / L. 11,903.13. Para los años subsiguientes la Junta Directiva del Instituto [Hondureño] de Seguridad Social (IHSS), con base a un estudio actuarial, deberá de fijar los techos de cotización para el Régimen de Invalidez, Vejez y Muerte (IVM) y el Régimen de Enfermedad y Maternidad (EM)." | Gradualness: 2024/2025 contribution ceilings IVM L11,336.32/L11,903.13, EM L11,109.30/L11,903.13 (TWO regime ceilings; 2025 equality = coincidence, R-H50); from 2026 the IHSS Board of Directors fixes both ceilings by actuarial study (dated rows from JD acts, never hardcoded) | `hn/sources/81_Decreto_48-2024_IHSS_aportaciones.pdf` | D48-Art. 2 (p.3/4, = G p. A.11; both text layers agree on the table) (EV81:EVID-252) |
| LB-003 | D. 48-2024, Art. 4 (VIGENCIA): "El presente Decreto entrará en vigencia el día de su publicación en el Diario Oficial 'La Gaceta'."; signatures: Congreso "a los treinta días del mes de abril de dos mil veinticuatro", Ejecutivo "Tegucigalpa, M.D.C., 8 de mayo de 2024" (G 36,545 Sección A, 28-may-2024). Art. 3 (fondo acumulado de la derogada Ley Marco → servicios de salud, comisión STLCC+SESAL) = treasury governance, no payroll consequence | Effective on the day of gazette publication = 28-may-2024 — the effective date for the 3.5/2.5/0.5 rates and both ceiling rows; Art. 3 legacy-fund destination is non-payroll | `hn/sources/81_Decreto_48-2024_IHSS_aportaciones.pdf` | D48-Arts. 3-4 (pp.3-4/4, = G pp. A.11-A.12) (EV81:EVID-253) |
| LB-004 | D. 48-2024, considerandos 3-6: "la Sala de lo Constitucional de la Corte Suprema de Justicia, declaró mediante Sentencia de inconstitucionalidad recaída en el Recurso No. SCO-858-2015, la derogatoria total del Decreto No.56-2015 del 21 de Mayo de 2015 «…»"; the ruling "dejó sin efecto el tres por ciento (3%) de incremento a la tasa para el Fondo de Invalidez, Vejez y Muerte y además, el acuerdo de gradualidad lo cual permitía mover el techo de cotización para los diferentes Regímenes"; JD lineage Res. SOJD-IHSS-053-2023 (2-mar-2023) | Legal-history hinge: SCO-858-2015 (published 27-oct-2022) voided D.56-2015 entirely — the 3-point IVM increase and the gradualidad ceiling mechanism lost their anchor; the statutory floor of LI Art. 55-A ¶2 revived until D.48-2024 re-legislated IVM rates and both ceilings | `hn/sources/81_Decreto_48-2024_IHSS_aportaciones.pdf` | D48 considerandos 3-6 (pp.1-2/4, = G pp. A.9-A.10) (EV81:EVID-250) |
| LB-005 | Ley del Seguro Social (D.140-1959, TSC print consolidated with D.80-2001), Art. 1: "El Instituto Hondureño de Seguridad Social (IHSS), constituye un servicio público que se aplicará con carácter obligatorio en los términos que establece esta Ley y sus reglamentos. La seguridad social se aplicará en forma gradual y progresiva tanto en lo referente a los riesgos a cubrir como en cuanto las zonas geográficas a incorporar, de conformidad a los estudios actuariales que se realicen al efecto."; Art. 2: cubrirá "a) Enfermedad, accidente no profesional y maternidad; b) Accidentes de trabajo y enfermedad profesional; c) Vejez e invalidez; d) Muerte; e) Subsidios de familia, viudez y orfandad; «…»" | IHSS is a public service of mandatory application where the regime applies; coverage itself is statutorily GRADUAL (risks + geographic zones, per actuarial studies); the contingency catalog — the payroll-relevant branches are EM (a) and IVM (c/d); riesgos profesionales (b) is employer-only financed (LB-014) | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 1-2 (p.1/19; OCR-only reading; R-H65 edition note) (EV81:EVID-254) |
| LB-006 | Ley del Seguro Social, Art. 3: "Son sujetos de aseguramiento al régimen obligatorio: a) Los trabajadores que devenguen un salario en dinero o en especie o de ambos géneros y que presten sus servicios a una persona natural ó jurídica, cualquiera que sea el tipo de relación laboral que los vincule y la forma de remuneración; b) Los funcionarios y empleados de las entidades descentralizadas «…»; c) Los funcionarios y empleados públicos; d) Los trabajadores que laboran en empresas Comerciales o Industriales «…»; e) Los Agentes Comisionistas «…»; f) Las personas que laboran para un patrono mediante un contrato de aprendizaje «…» Los reglamentos que emita la Junta Directiva fijarán las condiciones en que los grupos anteriores estarán sujetos al Régimen."; Art. 5 (not obligatory): cónyuge/padres/hijos <16 del patrono; Fuerzas Armadas; persons under other public special regimes; persons expressly excluded; "Los extranjeros contratados temporalmente «…» únicamente en lo que concerniente a los riegos de vejes [vejez], invalidez y muerte"; misiones diplomáticas (salvo reciprocidad); "g) Los Diputados al congreso nacional." | Mandatory-insurance subjects: ANY worker earning a salary in money, in kind or both, whatever the labor-relationship type and remuneration form — broader than the CT subordination test; in-kind salary counts; plus public-sector and listed categories, conditions fixed by JD reglamentos. Art. 5 exclusions incl. the temporary-foreigner IVM-only carve-out | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 3 y 5 (pp.1-2/19) (EV81:EVID-255) |
| LB-007 | Ley del Seguro Social, Art. 7: "El Empleador está obligado a inscribir en el Instituto Hondureño de Seguridad Social (IHSS), a todo trabajador que ingrese a su servicio; y también deberá comunicar, en su caso, la cesación del trabajador tan pronto como sea posible. A cada trabajador inscrito se le entregará un documento de identificación y un estado de cuenta de aportaciones. El reglamento determinará el plazo y la forma de inscripción de los empleadores y de sus trabajadores y el uso de documentos de afiliación." | The employer must register every new hire with IHSS, notify terminations as soon as possible, and receive per-worker an ID document and a contributions statement; concrete deadlines/forms are delegated to the (unacquired) Reglamento General | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Art. 7 (p.2/19) (EV81:EVID-256) |
| LB-008 | Ley del Seguro Social, Art. 54 ("Los recursos del Instituto estarán constituidos por: 1) Las cotizaciones pagadas por patronos y trabajadores «…»"); Art. 55: "Las cotizaciones y aportaciones «…» serán fijadas por mayoría de votos en la Junta Directiva, tal como lo establece el Artículo 17 de la presente Ley, tomando en cuenta para cada caso los estudios financiero-actuariales que efectúe el Instituto «…»"; Art. 17 ¶2: "Las resoluciones relativas a la modificación de techos, tasas, aportaciones y demás contribuciones al Instituto Hondureño de Seguridad Social (IHSS), deberán se[r] aprobados con el voto favorable de seis (6) miembros de la Junta Directiva." | Rate-setting jurisdiction: contributions are fixed by the IHSS Board of Directors on financial-actuarial studies; ceiling/rate/aportación modifications require 6 of 9 Board votes — the pipeline for post-2025 ceilings (D48 Art. 2 ¶2) and any rate change (JD resolution → La Gaceta per LB-013/LI Art. 102 ¶2) | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 54-55 (pp.10-11/19) y 17 ¶2 (p.4/19) (EV81:EVID-257) |
| LB-009 | Ley del Seguro Social, Art. 55-A (added by D.80-2001): "La tasa de cotización para el beneficio de enfermedad y maternidad (EM) será de cinco por ciento (5%) para el empleador, de 2.5% para el trabajador y de 0.5% para el Estado, quien contribuirá como tal de manera adicional a los aportes como empleador. Para el beneficio de Invalidez, Vejez y Muerte (I:V.M) la tasa de cotización será del dos por ciento (2%) para el empleador, del uno por ciento (1%) para el trabajador afiliado y de 0.5% para el Estado como aporte adicional a su contribución como empleador. El monto del salario sobre el cual se aplicarán las tasas a que se refieren los párrafos anteriores serán establecidos, revisados y modificados por la Junta Directiva del Instituto Hondureño de Seguridad Social (IHSS), tomando como base los estudios actuariales, todo lo cual sin perjuicio de lo establecido en el Artículo 55-B de esta Ley. Estas revisiones y modificaciones se efectuarán de manera periódica, pero en ningún caso el plazo será mayor de cinco (5) años." | THE EM rate row: employer 5% / worker 2.5% / State 0.5%, still in force (D.48-2024 did not touch EM); ¶2's IVM 2%/1%/0.5% is the pre-D.48 statutory floor — operative after the SCO-858-2015 void and superseded for IVM from 28-may-2024 (lex posterior, no express derogation — 81_ OQ-4); ¶3: the salary amount the rates ride is JD-set, without prejudice to Art. 55-B; reviews at most every 5 years | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Art. 55-A (pp.10-11/19; quote deinterleaved across the page boundary) (EV81:EVID-258) |
| LB-010 | Ley del Seguro Social, Art. 55-B: "No obstante, lo dispuesto en el Artículo anterior a partir del 1 de junio del 2001 las tasas de cotización para los beneficios de enfermedad y maternidad, así como del beneficio de invalidez, vejez y muerte, serán aplicados sobre una remuneración máxima de DOS MIL CUATROCIENTOS LEMPIRAS (Lps. 2,400.00) «…» dichas cotizaciones serán incrementadas automáticamente, elevándose los techos a TRES MIL SEISCIENTOS LEMPIRAS (Lps. 3,600.00) y CUATRO MIL OCHOCIENTOS LEMPIRAS (Lps. 4,800.00) respectivamente «…»"; Art. 104-A: "La cotización del Estado como tal, prevista en esta Ley, serán aplicables a partir del 1 de enero del 2002." | Ceiling-mechanics precedent: rates apply "over a MAXIMUM remuneration of L X" = the rates ride the salary up to a cap — base = min(salary, techo); this is the reading that resolves D48 Art. 1's "sobre los techos" (R-H51). 55-B's own L2,400/L3,600/L4,800 numbers are historical auto-escalators (actual ceilings later rose by JD acts → D48's 11k values); State-share effectiveness 1-jan-2002 (historical) | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Art. 55-B (p.11/19) y 104-A (p.18/19) (EV81:EVID-259) |
| LB-011 | Ley del Seguro Social, Art. 62: "El patrono deberá de deducir del salario del trabajador asegurado las aportaciones personales de éste, en la fecha de pago del mismo; sino lo hiciere, deberá verificarlo en los pagos subsiguientes, dentro del plazo de un mes a partir de dicha fecha. Transcurrido este plazo, este aporte personal quedará a cargo del patrono."; Art. 63: "Las cotizaciones de los patronos no podrán ser deducidas en forma alguna de los salarios de los asegurados, y será absolutamente nulo todo convenio en contra. El patrono que infringiere esta disposición será sancionado de acuerdo con lo dispuesto en el articulo 84 «…» numeral 3)"; Art. 61: employer-retained cotizaciones not paid in the terms of the Law/Reglamentos → mora recargos "en ningún momento serán menores que el promedio de las tasas máximas activas de interés vigente en el Sistema Financiero Nacional"; Art. 60 ¶3: "Las cotizaciones y las contribuciones del Estado, serán pagadas por mensualidades vencidas, dentro de los primeros quince (15) días del mes siguiente a que correspondan." | The payroll mechanics: the worker's personal shares are withheld ON the salary payment date, with a statutory 1-month cure window for missed deductions, after which the worker share becomes employer cost; employer shares may NEVER burden the worker (any contra agreement absolutely void + 3-SMM fine); late payment accrues mora surcharges floored at the financial-system benchmark; the State pays by monthly arrears within the first 15 days of the following month | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 60-64 (pp.11-13/19) (EV81:EVID-260) |
| LB-012 | Ley del Seguro Social, Art. 65 ¶2: "Todo empleador sujeto al Instituto «…» queda obligado a exhibir la constancia de encontrarse al día de sus cotizaciones o contribuciones al Instituto, para ejercer los actos siguientes: a) Cobrar al Instituto cualquier obligación; y, b) Participar en licitaciones que promuevan El Instituto, El Estado y sus Entidades Descentralizadas «…»"; Art. 84 (multas "en salarios mínimos mensuales en su categoría más alta"): "1) De un veinticinco (25%) de un salario mínimo por cada trabajador, si no se inscriben o se niegan a afiliar al trabajador «…»; 2) De un salario mínimo, por demora excesiva o persistente en la presentación y pagos de la planilla de cotización «…» por cada planilla atrasada «…»; 3) De tres (3) salarios mínimos, si deduce sus propias cotizaciones de los salarios de los asegurados «…»"; Art. 88 ¶2: "En caso de los empleadores morosos por cotizaciones obrero patronales, todas las prestaciones previstas en la Ley y su Reglamento, serán asumidas directamente por éllos [ellos], sin responsabilidad alguna para el Instituto."; Art. 99: patronal cotizaciones+recargos+multas "prescriben en el término de cinco (5) años"; "Son imprescriptibles las cotizaciones de los trabajadores retenidas por los patronos que no fuesen enteradas al Instituto." | Enforcement stack: solvencia (being up to date) is a gate for collecting from IHSS and for public tendering; the fine schedule is denominated in highest-category monthly minimum wages (ties the P1 SMM dated rows); employer mora shifts ALL benefit costs to the employer; employer contributions prescribe in 5 years while retained-but-unremitted worker shares never prescribe | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 65, 84, 88, 99 (pp.12-13, 15-16, 17/19) (EV81:EVID-261) |
| LB-013 | Ley del Seguro Social, Art. 100: "El Reglamento definirá lo que debe entenderse por salario para el efecto del Instituto Hondureño de Seguridad Social (IHSS); éste también establecerá categorías de salarios para la clasificación de los asegurados y fijará «para cada una de ellas un salario base para el cálculo de las cotizaciones y de las prestaciones en dinero. Determinar así mismo, la equivalencia en dinero para los casos en que los asegurados perciban una parte de su remuneración en alimentos o vivienda."; Art. 106: "Si la presente Ley o sus reglamentos no definieren expresamente ciertos términos «…», se aplicarán la definiciones admitidas en las leyes de trabajo, o, a falta de éstas, las del Derecho Común."; Art. 102 ¶2: reglamentos on inscription, rights/duties, and "la periodicidad y a las modalidades de recaudación de las cotizaciones «…» deberán ser aprobadas por la Junta Directiva conforme lo establece en el Artículo 17 «…», debiendo ser publicadas en el Diario Oficial La Gaceta." | THE base delegation: the Law itself does NOT define the cotización salary — it delegates "salario", salary categories, per-category base salaries and in-kind equivalences wholesale to the Reglamento General (NOT in corpus — 87_ OQ-1, top acquisition lead); whether 13th/14th month, overtime or bonuses enter the base is unsaid anywhere in the corpus → configuration flag, never guessed; absent express definitions, labor-law definitions apply subsidiarily; base rules arrive via JD-approved, Gaceta-published reglamentos | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 100, 106 y 102 ¶2 (pp.18-19/19) (EV81:EVID-262) |
| LB-014 | Ley del Seguro Social, Art. 45: "Las Prestaciones del Seguro por Riesgos Profesionales, se financiarán exclusivamente con cargo a las cotizaciones de los empleadores, según lo determinen los Reglamentos «…» Podrá establecer cuotas técnicas especiales a cargo del empleador, tomando en cuenta la peligrosidad de cada actividad y la región «…»"; Arts. 34.b/39.b: incapacidad/maternity cash subsidies "cuyo monto duración y demás condiciones para su pago, serán fijadas por los Reglamentos"; Art. 90: subsidies "son incompatibles [entre sí]"; Art. 91: subsidy claims prescribe at 1 year; Art. 92: prestaciones en dinero "no serán gravables por impuesto alguno." | Riesgos profesionales are financed EXCLUSIVELY by employer contributions, reglamento-determined, with actividad-peligrosidad-variable technical quotas (no rate in corpus — 87_ OQ-2); the subsidy money-terms live in reglamentos (the RIT, owned by file 04 — cited here as frame only); cash benefits are mutually incompatible per contingency, claim-prescription 1 year, and NOT taxable by any tax (ISR interface) | `hn/sources/87_Ley_IHSS_TSC.pdf` | LI-Arts. 34.b, 39.b, 42.2, 45, 90-92 (pp.7-9, 16/19) (EV81:EVID-263) |
| LB-015 | **Acuerdo No. 003-JD-2005 (Reglamento General de la Ley del IHSS), Art. 135** (Sección II "DEL SALARIO SUJETO A COTIZACION"; Dado 15-feb-2005; gazette original G 30,735 29-jun-2005 per `147_`; `145_` = institutional "última versión" retypeset): "Se entiende por salario para los efectos de la aplicación de la Ley del Seguro Social no solo la remuneración fija u ordinaria, sino todo lo que recibe el trabajador asegurado ya sea en dinero o en especie y que implique retribución de servicios, sea cualquiera la forma o denominación que se adopte, como las primas, sobresueldos, bonificaciones habituales, valor del trabajo suplementario o de las horas extras, valor del trabajo en días de descanso obligatorio, porcentajes sobre ventas, comisiones o participación de utilidades. No constituyen salario las sumas que ocasionalmente y por mera liberalidad reciban el trabajador del patrono, como las primas, bonificaciones y gratificaciones «…» El salario en especie que reciba el trabajador, no excederá del treinta por ciento (30%) del total de la remuneración." | **THE base-composition resolver** (LI Art. 100's delegate text, W9): the cotizable salary = fixed/ordinary remuneration + everything implying retribution — primas, sobresueldos, **bonificaciones HABITUALES**, **OT/horas extras**, **rest-day work value**, % on sales, commissions, profit participation; EXCLUDED = sums received occasionally and by mere liberality (primas/bonificaciones/gratificaciones); in-kind salary capped at 30% of total remuneration (feeds FR-116's equivalence hook). OT is EXPLICITLY IN the base | `hn/sources/145_Acuerdo_003-JD-2005_Regl_Gral_Ley_IHSS_ult_version.pdf` | RegGen003-Art. 135 + Art. 4 defs. 14-15 (pp.3-4, 37-38; text layer; EV145:EVID-545; gazette-original corroborated EV147) |
| LB-016 | Acuerdo 003-JD-2005, Art. 134: "Independientemente del monto del salario o ingreso que se anota en la planilla, la cotización mínima mensual se calculará sobre un ingreso de referencia mínimo equivalente al salario mínimo vigente en su categoría o conforme a la modalidad que se establezca en la Tabla del Salario autorizado por el Gobierno de la República."; Art. 136: "El Instituto puede fijar límites mínimo y máximo de los salarios por los cuales se cotizará para los regímenes de afiliación especiales."; Art. 147: "Será de cuenta del patrono la cotización del trabajador, correspondiente a la diferencia entre lo que gane un trabajador y el salario establecido para la cotización mínima." | The MINIMUM cotización base = the worker's category SMM (P1 SMM-table dependency made explicit); the Instituto's min/max-fixing power (the ceiling pipeline's reglamento seat, alongside LI Arts. 17/55-A ¶3/55-B); the BELOW-minimum difference is EMPLOYER cost (worker shares never burden the under-minimum earner) | `hn/sources/145_Acuerdo_003-JD-2005_Regl_Gral_Ley_IHSS_ult_version.pdf` | RegGen003-Arts. 134, 136, 147, 151 (pp.9, 37, 39, 40-41; EV145:EVID-546/547) |
| LB-017 | Acuerdo 003-JD-2005, Riesgos Profesionales chapter (Arts. 88-97, Tít. III Cap. III Secc. IV): "Las Empresas que ingresen por primera vez al Régimen de Riesgos Profesionales cotizará[n] por el valor inicial del 0.2%. Sobre el salario nominal en base al techo actual para todas las categorías." (Art. 89 final ¶); five risk classes (Art. 95); annual siniestralidad review with employer January filing (Arts. 90-93); rate stability ≥1 year (Art. 97); employer-only financing restated (Art. 88) | The RP-rate machinery's reglamento seat: NEW entrants to the RP regime cotize an initial **0.2% on nominal salary capped at the current techo**; five-class structure + annual experience-review (January employer filing) + ≥1-year rate stability; the class-value cuadros themselves remain absent → OQ-006 NARROWED, not closed (no default rate computed) | `hn/sources/145_Acuerdo_003-JD-2005_Regl_Gral_Ley_IHSS_ult_version.pdf` | RegGen003-Arts. 88-97 (Tít. III Cap. III Secc. IV, pp.25-27; EV145:EVID-549) |
| LB-018 | Acuerdo 003-JD-2005, Art. 144 (cotización payment rhythm): cotizaciones are due **"dentro de los primeros diez (10) días"** of the following month, with oficio facturación riding the last planilla; Art. 161 a)/b)/g): non-affiliation → resarcimiento + capitales constitutivos + **10% administrative surcharge**; reporting failures → multa mensual 10% of the monthly cotizado total, until the cause is resolved; Arts. 165-166: the delinquent patrono absorbs the full prestaciones | The EMPLOYER payment deadline (10 days, reglamento seat — sharpens the LI-Art.-60 ¶3 15-day State-rhythm note of FR-122; employers' operative calendar = 10 days from 29-jun-2005) + the 10%-monthly sanctions class and moroso-absorbs-everything consequence (enforcement metadata) | `hn/sources/145_Acuerdo_003-JD-2005_Regl_Gral_Ley_IHSS_ult_version.pdf` | RegGen003-Arts. 144, 161, 165-166 (pp.39, 42-44; EV145:EVID-551) |
| LB-019 | **THE IHSS REGLAMENTO ANCESTRY TRIPLE (W9)** — `147_` = the GAZETTE ORIGINAL of Acuerdo 003-JD-2005 (G 30,735, martes 29-jun-2005, masthead-confirmed; full Art. 1-194 two-column print; the JD roster ≡ 145_'s) — EV147:EVID-556..560; `146_` = the 1971 REGLAMENTO DE APLICACIÓN DE LA LEY DEL SEGURO SOCIAL (institutional print titled "Decreto No.193-1971"; campo-de-aplicación structure; ≡ Acuerdo 101-JD-71 by G05-Art. 194's derogation-target inference — OQ-3(146_); its own salary/base articles pre-figure Art. 135) — EV146:EVID-554/555; `148_` = the G 33,879 (10-nov-2015) Sección-A Seguridad-Social extract: the IHSS Comisión-Interventora resolutions incl. the CUARTO-clause RAP-patrimony-safeguard ley initiative + Ley-Marco kin (payroll/05 context rows) — EV148:EVID-561..565 | The Reglamento General's identity chain complete: 1971 ancestor → 2005 gazette original → institutional retypeset; payroll/03 consumes 145_ for text (LB-015..018) and these three for provenance/ancestry/context | `hn/sources/147_Regl_Gral_Ley_IHSS_transparencia_scan.pdf` + `hn/sources/146_Regl_Aplicacion_Ley_Seguro_Social_Decreto_193-1971.pdf` + `hn/sources/148_Gaceta_33879_10nov2015_IHSS_RAP.pdf` | EV147:EVID-556..560; EV146:EVID-554/555; EV148:EVID-561..565 |
| LB-020 | **Acuerdo 006-JD-2008 ACQUIRED W10** (`155_`, gazette G 31,681 sábado 9-ago-2008; JD session 24-jun-2008): the **REGLAMENTO DEL RÉGIMEN ESPECIAL Y DE AFILIACIÓN PROGRESIVA DE LOS (AS) TRABAJADORES (AS) DOMÉSTICOS (AS)** — gradual geographic application per IHSS capacity (Art. 2); subjects = CT-Art.-150 domésticos (Art. 3); annual inscription with prepaid cotización + renewal/30-day grace/30-day carencia (Arts. 8-9); substitute-inscription free until year-end (Art. 11); prestaciones = HEALTH-ONLY (ambulatory + maternity; hospital EXCEPT maternity, Art. 15; **incapacidad subsidies EXCLUDED, Art. 16**); cotización values DELEGATED to JD per actuarial studies (Art. 18); optional IVM bridge ("Si el/la Trabajador(a) Doméstico desea gozar del beneficio del Régimen IVM, el patrono deberá realizar una aportación según lo establece en la Ley del Seguro Social"); vigencia 9-ago-2008 (Art. 26) | FR-126's domésticos flag gains its regime statute: a separate lane OUTSIDE the standard IVM/EM matrix — segment config gate, rates = unacquired JD family (OQ-011); the payroll/04 incapacity engine excluded for REAP workers | `hn/sources/155_Acuerdo_006-JD-2008_Regl_trabajadores_domesticos_REAP.pdf` | EV155:EVID-612..621 |
| LB-021 | **THE IHSS AMNISTÍA FAMILY ACQUIRED W11** — `162_` = **D.L. 112-2016** statute-original (G 34,170 miércoles 26-oct-2016 pp. A.5-A.6, ENAG full issue; Dado 16-ago-2016, Ejecútese 12-sep-2016, vigencia = publication day): authorizes the IHSS "por esta única vez" to amnistiate **recargos, multas e intereses** on aportes patronales y de trabajadores "dejados de enterar" (public+private patronos — the CAPITAL always remains payable); beneficiary gate = pay in legal form OR document+guarantee within 12 months (Art. 2); **Art. 3 = health-access restoration duty** ("debe restablecer el acceso a servicios de salud y protección social de los afiliados cuyos patronos paguen o regularicen sus adeudos en mora" — the mora-sensitive coverage lever behind LI Art. 88 ¶2/LB-012); Art. 4 = Junta-Interventora depuración mandate. `161_` = its **Reglamento Especial** (Comisión Interventora print, 11-nov-2016; Arts. 1-23 complete): **window printed 26-oct-2016 → 25-oct-2017** (Art. 3.a); four beneficiary-direct classes incl. current-convenio holders in mora (Art. 3.b); **convenio economics = plazo + prima inicial + FIXED 12% interest** (Arts. 3.d/n) with the prima/plazo table ≤L200k→20%/12m · L200k-1M→20%/18m · >L1M→15%/24m (Art. 20, prima = FLOOR); **default = 1 cuota + 31-day mora → amnistía lost, multas/recargos/intereses REVERT via débitos** (Art. 19, Ley-Marco-Art.-36 pointer); **convenios never suspend current monthly aportes** (Art. 20 ¶2); PN lane = Afiliación Progresiva (REAP population cross-link, Art. 14); 3-month interest-free capital-contado option (Art. 16 ¶2) | **HISTORICAL/closed-window rows only** (expired 25-oct-2017 — **succeeded by the LIVE 2025-2026 chain acquired the SAME WAVE, LB-022**: D.L. 44-2025 Art. 2 → D.L. 78-2026 Art. 2 → Res. SOJD-IHSS-016-2026-XIII): no live payroll computation from the 2016 family; value = (a) the LB-012 enforcement stack's first documented regularization episode (migration-era IHSS account reconciliation context, D-H3); (b) the 161_-Art.-6 RTN-unification/número-único-patronal origin (IHSS employer master-data is RTN-keyed); (c) the amnistía-family completeness lane (kin of 06_/109_'s D. 5-2024). Reglamento's own gazette-publication unpinned (OQ-012) | `hn/sources/161_Reglamento_Especial_Amistia_IHSS_DL112-2016.pdf` + `hn/sources/162_Gaceta_34170_Decreto_112-2016_Amistia_IHSS.pdf` | EV161:EVID-645..650; EV162:EVID-644/650 |
| LB-022 | **THE LIVE IHSS AMNISTÍA CHAIN 2025-2026 ACQUIRED W11** — `163_` = **D.L. 44-2025** (G 36,861 mié 11-jun-2025; Dado 3-jun, Ejecútese 10-jun-2025; vigencia = publication day): the seven-amnistía package; its Art. 2 = the IHSS amnistía re-grant (scope "recargos y multas" as printed; **10-month window** 11-jun-2025→11-abr-2026, superseded mid-flight; health-restoration + widened depuración). `164_` = **D.L. 78-2026** (G 37,166 vie 12-jun-2026; Dado 13-may, Ejecútese 15-may-2026; vigencia 12-jun-2026) the AMPLIACIÓN: Art. 2 re-grants the IHSS amnistía — **scope restored to recargos/multas/INTERESES, window 4 months = 12-jun-2026 → 12-oct-2026**; its Art. 1 = the SAR general amnistía (taxation/07 lane) and its considerando DEROGATES D. 7-2026 Art. 7 (06_). `165_` = **Res. SOJD-IHSS-016-2026-XIII** (JD 25-jun-2026; Comité Acta CR-02-2026; certified G 37,189 jue 9-jul-2026 pp. A.31-64) = the REFORMED REGLAMENTO — the operative procedure: convenio gate **principal > L15,000**; **economics table: 0% interest ≤12-month convenios / 12% longer; prima mínima 10%/15%/25% sin-refinanciamiento (12m/13-96m/demand-process) and 20%/30%/35% con-refinanciamiento (12m/13-48m/demand)**; hardship exceptions up to **120 months (prima ≥5%) / 96 months (prima ≥10%)** with 2-year-financials/ISR evidence; **terminal 12-oct-2026 + 6-month processing tail (→~12-abr-2027, received-in-time only)**; Art. 24 continuity (monthly cuota + convenio never suspended; default → judicial recovery LI-Art.-65 + Ministerio Público referral); patrono-initiated + 3 oficio depuración lanes | **the CURRENT employer regularization lane** — dated config rows per D-H2.6 (access window 12-jun→12-oct-2026; processing tail to ~12-abr-2027); the 2016 economics (LB-021: flat 12%, 12/18/24m) are SUPERSEDED — never mix the two tables; scope chain: 44-2025 two-item print vs 78-2026 three-item = OQ-2(163_) flagged for any 2025-window historical reconstruction; publication-route datum: IHSS JD acts publish as Sección-A certificaciones (the future techo/rate-act watch route) | `hn/sources/163_Gaceta_36861_Decreto_44-2025_Amnistias.pdf` + `hn/sources/164_Gaceta_37166_Decreto_78-2026_Amnistia_ampliacion.pdf` + `hn/sources/165_Gaceta_37189_SOJD-IHSS-016-2026_Regl_Amnistia_reforma.pdf` | EV163:EVID-651..653; EV164:EVID-654..657; EV165:EVID-658..664 |

## 3. Functional Requirements

### 3.1 The cotización matrix as dated rows

- **HN-PAYR-FR-101:** The system shall load the IVM cotización rate as DATED
  legal data per R-H49: employer 3.5% / worker 2.5% / State 0.5%, row
  `valid_from` 2024-05-28 (D.48 publication day), current row open-ended —
  never overwritten (D-H2), resolved by the payslip period (*hecho
  generador*), never "today". (LB-001; LB-003; EV81:EVID-251/253; R-H49)
- **HN-PAYR-FR-102:** The system shall load the EM cotización rate as DATED
  legal data: employer 5% / worker 2.5% / State 0.5% (LI Art. 55-A ¶1, from
  the D.80-2001 regime — signature 1-jun-2001, G 29,503 14-jun-2001 per
  R-H65), in force and untouched by D.48-2024; the row carries its statute
  provenance and open-ended validity. (LB-009; EV81:EVID-258; R-H49; R-H65)
- **HN-PAYR-FR-103:** The system shall compute the COMBINED per-period
  matrix from the two regime rows — worker withholding 5.0% (2.5% IVM + 2.5%
  EM) and employer charge 8.5% (3.5% IVM + 5% EM) — as a per-payslip
  composition of the regime rows, NEVER stored or maintained as a single
  merged statutory rate (regime rows evolve independently through JD acts
  and statutes). (LB-001; LB-009; EV81:EVID-251/258; R-H49)
- **HN-PAYR-FR-104:** The system shall carry the SUPERSEDED IVM statutory
  floor row — employer 2% / worker 1% / State 0.5% (LI Art. 55-A ¶2),
  `valid_to` 2024-05-27 — with its supersession recorded as lex posterior
  (D.48 Art. 1 contains no express derogation clause; considerandos'
  restitutory intent — 81_ OQ-4), and an interregnum caveat: the operative
  ceiling trail for pre-28-may-2024 periods (and the 2022→05-2024 revival of
  the floor after SCO-858-2015, published 27-oct-2022) is unaudited in this
  corpus → pre-vigencia historical payslips resolve to a config gap, never
  to guessed rows (81_ OQ-2, 87_ OQ-4). (LB-004; LB-009;
  EV81:EVID-250/258)
- **HN-PAYR-FR-105:** The system shall treat the two State shares (IVM
  0.5%, EM 0.5%) as INFORMATIONAL metadata only — never payroll-withheld
  lines, never employer remittance components — and shall not model any
  Estado-side computation row until the State base is pinned (D48 Art. 1's
  "en base del total de los afiliados activos" is grammatically broken in
  the gazette original — 81_ OQ-3; State-share effectiveness 1-jan-2002 per
  LI Art. 104-A is historical metadata). (LB-001; LB-010;
  EV81:EVID-251/259)
- **HN-PAYR-FR-106:** The system shall encode the rate/ceiling change-source
  model: every rate or ceiling row records whether it is a STATUTE row (D.48
  2024) or a JD-RESOLUTION row (Junta Directiva act approved by 6 of 9 votes
  on financial-actuarial studies, per LI Arts. 55/17 ¶2, published in La
  Gaceta per LI Art. 102 ¶2), with gazette reference and effective date —
  the ingestion contract for post-2025 ceilings and any future rate change
  (additive dated rows only, D-H2). (LB-008; LB-013;
  EV81:EVID-257/262)
- **HN-PAYR-FR-107:** The system shall carry the chronology metadata for the
  rate-history table: D.56-2015 (IVM +3 pts + gradualidad ceilings) → voided
  in full by SCO-858-2015 published 27-oct-2022 → LI 55-A ¶2 statutory floor
  revival (ceiling trail unaudited) → D.48-2024 rates/ceilings from
  28-may-2024 — as provenance notes on the dated rows, not as computable
  derived values. (LB-003; LB-004; EV81:EVID-250/253)

### 3.2 The two regime ceilings as dated-row families

- **HN-PAYR-FR-108:** The system shall load the contribution ceilings
  (*techos de cotización*) as TWO SEPARATE dated-row families, one per
  regime, per R-H50: IVM 2024 L11,336.32 / IVM 2025 L11,903.13; EM 2024
  L11,109.30 / EM 2025 L11,903.13 — the 2025 numeric equality is a
  coincidence and shall NEVER be stored, merged or looked up as one shared
  ceiling row; each family is independently superseded by future JD acts.
  (LB-002; EV81:EVID-252; R-H50)
- **HN-PAYR-FR-109:** The system shall bound the 2024 ceiling rows by the
  mid-year vigencia of D.48: `valid_from` 2024-05-28, `valid_to`
  2024-12-31; payslip periods 2024-01-01→2024-05-27 have NO corpus-evidenced
  operative ceilings (interregnum unaudited) and shall be BLOCKED with an
  explicit missing-ceiling configuration flag — never computed with the
  D.48 values, never back-dated, never guessed (D-H2 never-guess; 81_ OQ-2).
  (LB-002; LB-003; EV81:EVID-252/253)
- **HN-PAYR-FR-110:** The system shall key ceiling rows by calendar year
  with per-regime lookup by (regime, payslip-period date): 2025 rows
  `valid_from` 2025-01-01 / `valid_to` 2025-12-31; every ceiling selection
  in a payslip resolves the row family by the period being computed, and the
  resolved values are snapshotted onto the payslip at write time (D15), with
  paid slips frozen and corrections recomputed with ORIGINAL-period rows
  (D-H2/D16). (LB-002; EV81:EVID-251/252)
- **HN-PAYR-FR-111:** The system shall treat post-2025 ceilings as EXTERNAL
  DATED DATA per D48 Art. 2 ¶2: the Junta Directiva fixes both ceilings by
  actuarial study (JD resolution in La Gaceta); when a payslip period has no
  loaded ceiling row for a regime (e.g. any 2026+ period before the JD act
  is ingested) the computation shall be BLOCKED with a missing-ceiling flag
  — never defaulted to the prior year, never indexed, never derived
  (never-guess rule; watch instrument = JD resoluciones in La Gaceta).
  (LB-002; LB-008; EV81:EVID-252/257)
- **HN-PAYR-FR-112:** The system shall expose the resolved IVM techo of the
  payslip period as a consumption interface for the RAP/fondo engine — file
  05 (`05_rap-fondo.md`, HN-PAYR-FR-181..215) consumes the IVM techo BY ID
  (dated-row lookup by period) with no re-derivation and no second ceiling
  family. (LB-002; EV81:EVID-252)

### 3.3 Contribution-base semantics

- **HN-PAYR-FR-113:** The system shall compute each regime's cotizable base
  as min(monthly remuneration, regime techo) per R-H51 — the coherent
  reading of D48 Art. 1's "porcentajes se aplicarán sobre los techos" in
  light of LI Art. 55-B's "aplicados sobre una remuneración máxima"
  precedent; the literal flat reading (rates applied TO the ceiling as a
  fixed per-affiliate amount) is REJECTED as default and shall never be
  implemented without an express IHSS worksheet/consult confirmation (81_
  OQ-1 guard). (LB-001; LB-010; EV81:EVID-251/259; R-H51)
- **HN-PAYR-FR-114:** The system shall cap INDEPENDENTLY per regime: the EM
  shares are computed on min(remuneration, techo EM) and the IVM shares on
  min(remuneration, techo IVM) — two separate caps inside the same payslip
  (they differ, e.g. Dec-2024: EM 11,109.30 vs IVM 11,336.32; they merely
  coincide in 2025). (LB-001; LB-002; LB-010; EV81:EVID-251/252/259)
- **HN-PAYR-FR-115:** The system shall compute the contribution-base
  COMPOSITION per the Reglamento General Art. 135 text (ACQUIRED W9 as
  `145_`, EV145:EVID-545 — the LI-Art.-100 delegate): the cotizable salary
  INCLUDES the fixed/ordinary remuneration plus primas, sobresueldos,
  *bonificaciones habituales*, **overtime/horas extras and trabajo
  suplementario**, **statutory rest-day work value**, percentages on sales,
  commissions and profit participation, in money or in kind; it EXCLUDES
  sums received *ocasionalmente y por mera liberalidad* (primas,
  bonificaciones, gratificaciones). Component-level encoding:
  (a) OT lines and rest-day work lines are IN the base by default;
  (b) HABITUAL bonuses are IN; occasional/gratuitous bonuses are OUT
  (habituality is a configurable per-component attribute, default=habitual
  for recurring wage components);
  (c) the 13th month (*aguinaldo*) is OUT — barred from cotizaciones by
  the D. 117-2021 Art. 2 authentic interpretation (`89_`, EVID-335, valid
  14-feb-2022), which overrides the reglamento's generic habituality
  clause for that component;
  (d) the 14th month (*décimo cuarto mes*) remains a CONFIG FLAG pending
  the SMM-average-variant adjudication (OQ-010 — never guessed either
  way). A payslip carrying a component not covered by (a)-(d) surfaces an
  explicit pending-base-composition flag rather than silently computing
  (never-guess rule). (LB-013; LB-015; EV81:EVID-262; EV145:EVID-545)
- **HN-PAYR-FR-116:** The system shall provide an in-kind remuneration
  equivalence hook: salary in kind (*en especie* — e.g. alimentos,
  vivienda) counts as affiliation-triggering remuneration (LI Art. 3.a), and
  its money equivalence — fixed by the Reglamento General per LI Art. 100 —
  is pending configuration until that instrument is acquired (config flag,
  never a guessed conversion). (LB-006; LB-013; EV81:EVID-255/262)
- **HN-PAYR-FR-117:** The system shall record LI Art. 106's definitional
  recourse as INTERPRETIVE METADATA only: absent express reglamento
  definitions, labor-law definitions apply subsidiarily — a pointer to file
  10's salary concept (`10_salario-concepts-records.md`,
  HN-PAYR-FR-371..405) by cross-reference, explicitly NOT a derivation
  license for base composition (which remains governed by FR-115's config
  flag). (LB-013; EV81:EVID-262)

### 3.4 Withholding mechanics (LI Arts. 60-64)

- **HN-PAYR-FR-118:** The system shall withhold the worker's personal
  shares (EM 2.5% + IVM 2.5% of the capped bases) ON the salary payment
  date — one deduction event stamped at the payrun payment, per LI Art. 62,
  not at accrual and not at period close. (LB-011; EV81:EVID-260)
- **HN-PAYR-FR-119:** The system shall implement the statutory 1-month cure
  window: a worker share missed at a payment date may be recovered in
  subsequent payments within one month from that date; once the window
  lapses, the missed *aporte personal* becomes EMPLOYER-BORNE — recorded as
  a real ledger rule (late-withholding recovery lines, then an
  employer-cost absorption line), never silently dropped.
  (LB-011; EV81:EVID-260)
- **HN-PAYR-FR-120:** The system shall enforce the employer-share
  non-deduction invariant: employer cotizaciones may NEVER be deducted in
  any form from insured workers' salaries, and any contrary agreement is
  absolutely void (*absolutamente nulo todo convenio en contra*, LI Art.
  63) — a hard validation guard blocks employer-share amounts from worker
  deduction lines, with the 3-SMM fine (FR-127) recorded as the sanction
  consequence. (LB-011; LB-012; EV81:EVID-260/261)
- **HN-PAYR-FR-121:** The system shall flag mora on retained-but-late
  cotizaciones with the statutory recargo floor: surcharges never lower than
  the average of the maximum ACTIVE interest rates in force in the National
  Financial System (LI Art. 61) — the rate itself is external financial
  data, recorded as a pending-source accrual metadata field, never guessed.
  (LB-011; EV81:EVID-260)
- **HN-PAYR-FR-122:** The system shall record the State's monthly rhythm —
  cotizaciones/contributions paid by monthly arrears within the first 15
  days of the following month (LI Art. 60 ¶3) — as an informational
  calendar note (the de facto planilla practice anchor), NEVER as a payroll
  line or an employer obligation of this file. (LB-011; EV81:EVID-260)
- **HN-PAYR-FR-123:** The system shall support the affiliation workflow
  hooks of LI Art. 7: every hire → IHSS inscription event, every
  termination → *cesación* notification "as soon as possible", with the
  per-worker IHSS affiliate ID and *estado de cuenta* (contributions
  statement) reference on the employee master; the concrete deadlines/forms
  are delegated to the Reglamento General (unacquired — pending config,
  87_ OQ-1) and the non-affiliation sanction is the FR-127 fine.
  (LB-007; LB-013; EV81:EVID-256/262)

### 3.5 Affiliation scope (LI Arts. 1-5)

- **HN-PAYR-FR-124:** The system shall mark affiliation as MANDATORY for
  every subject of the obligatory regime per LI Art. 3: any worker earning a
  salary in money, in kind or both, serving a natural or juridical person,
  WHATEVER the labor-relationship type and remuneration form (plus public
  entities and municipalities, commercial/industrial/agro-forestry
  enterprises, commission agents, apprentices), with the per-group
  conditions fixed by JD reglamentos (dated config when they arrive).
  (LB-005; LB-006; EV81:EVID-254/255)
- **HN-PAYR-FR-125:** The system shall carry the LI Art. 5 exclusion flags:
  (a) cónyuge/padres/hijos under 16 working for the patrono's account; (b)
  Fuerzas Armadas; (c) persons covered by other public special regimes; (d)
  persons expressly excluded by law or convention; (e) TEMPORARILY
  CONTRACTED FOREIGNERS — affiliated for IVM ONLY (vejez/invalidez/muerte),
  EM lines suppressed; (f) diplomatic missions absent reciprocity; (g)
  Diputados al Congreso Nacional. (LB-006; EV81:EVID-255)
- **HN-PAYR-FR-126:** The system shall carry the voluntary/progressive
  categories (LI Art. 4: domésticos, a domicilio, independientes,
  patronos-personas-físicas, ocasionales/de temporada, etc.) as OPTIONAL
  worker flags — affiliation subject to actuarial-study gradualidad, never
  a default — and the zonal/risk coverage gradualness of LI Art. 1 as a
  per-establishment coverage DATA flag rather than an assumed
  national-default (87_ OQ-5). **W10 REAP STATUTE ANCHOR (LB-020): the
  domésticos flag now has its own reglamento — Acuerdo 006-JD-2008
  (`155_`, G 31,681 9-ago-2008): the Régimen Especial y de Afiliación
  Progresiva = a SEPARATE health-only lane (annual prepaid cotización,
  JD-set rates per actuarial study — values NOT in the instrument, OQ-011;
  ambulatory + maternity ONLY, hospital excluded except maternity,
  incapacidad subsidies EXCLUDED — the payroll/04 engine does NOT run for
  REAP workers; optional IVM bridge = patrono aporta per the Ley when the
  worker elects; substitute-inscription free until year-end; 30-day grace
  + 30-day carencia on lapse). Encode as a worker-segment config gate:
  REAP workers never enter the standard IVM/EM matrix (FR-112..115) —
  segment flag, never rate rows (rates = JD acuerdo family, unacquired).**
  (LB-005; LB-020; EV81:EVID-254/255; EV155:EVID-612..621)

### 3.6 Riesgos profesionales branch

- **HN-PAYR-FR-127:** The system shall carry the riesgos profesionales
  (*occupational risks*) branch as employer-ONLY financing per LI Art. 45
  and the Reglamento General RP chapter (ACQUIRED W9, `145_`
  EV145:EVID-549): new regime entrants cotize an initial **0.2% on
  nominal salary capped at the current techo** (Art. 89), five risk
  classes (Art. 95), annual siniestralidad review with a January employer
  filing (Arts. 90-93) and ≥1-year rate stability (Art. 97). The
  class-value cuadros/JD rate tables remain ABSENT from the corpus: no
  class-specific RP rate shall be computed until they arrive (87_ OQ-2
  NARROWED — the 0.2% entry value is encodable as the new-entrant row
  valid_from 29-jun-2005, with class rates config-gapped); the CT Título V
  residual belongs to file 09 (`09_suspension-maternity-special.md`,
  HN-PAYR-FR-331..357). (LB-014; LB-017; EV81:EVID-263; EV145:EVID-549)
- **HN-PAYR-FR-136:** The system shall schedule the EMPLOYER cotización
  payment deadline at the FIRST 10 DAYS of the following month per
  Reglamento General Art. 144 (oficio facturación on the last planilla),
  distinct from the State's 15-day rhythm (FR-122) — dated row valid_from
  29-jun-2005 (reglamento publication; any later instrument supersedes by
  D-H2 additive rows). (LB-018; EV145:EVID-551)
- **HN-PAYR-FR-137:** The system shall record the Reglamento General's
  minimum-base rule: independently of the payroll-annotated salary, the
  monthly minimum cotización base = the worker's category SMM (Art. 134),
  with the BELOW-minimum worker-share difference borne by the EMPLOYER
  (Art. 147) — an SMM-table dependency (file 01) feeding the base floor
  computation; never a flat derived value. (LB-016; EV145:EVID-546)

### 3.7 Enforcement metadata

- **HN-PAYR-FR-128:** The system shall record the *solvencia* requirement:
  an employer subject to IHSS must exhibit the constancia of being up to
  date on cotizaciones to (a) collect any obligation from IHSS and (b)
  participate in tenders promoted by IHSS, the State and its decentralized
  entities — an up-to-date status field on the company record exposed as a
  procurement-integration hook (gate logic itself consumed by the
  commercial/procurement surfaces by cross-reference).
  (LB-012; EV81:EVID-261)
- **HN-PAYR-FR-129:** The system shall record the mora consequence: an
  employer in arrears on obrero-patronales cotizaciones assumes DIRECTLY all
  prestaciones under the Law and its Reglamento, without any IHSS
  responsibility — a mora flag that switches benefit-cost assumption to the
  employer (the subsidy-mechanics execution of that switch is owned by file
  04, HN-PAYR-FR-141..170, consumed by id). (LB-012; LB-014;
  EV81:EVID-261/263)
- **HN-PAYR-FR-130:** The system shall carry the prescription ledger rules:
  employer cotizaciones, recargos and multas prescribe in FIVE (5) years;
  worker cotizaciones RETAINED by the employer and not remitted are
  IMPRESCRIPTIBLE — retained-unremitted worker shares post as a
  non-prescribing liability on the IHSS payable account, distinct from the
  5-year-prescribing employer balance. (LB-012; EV81:EVID-261)
- **HN-PAYR-FR-131:** The system shall carry the LI Art. 84 fine schedule
  denominated in salarios-mínimos units — "en salarios mínimos mensuales en
  su categoría más alta": (1) 25% of one SMM per worker not inscribed or
  refused affiliation; (2) one SMM per late *planilla de cotización*
  (excessive/persistent delay); (3) three SMM for deducting the employer's
  own cotizaciones from insured salaries — with the multa UNIT resolved as
  dated data from the P1 SMM rows (file 01, HN-PAYR-FR-001..040) by
  period, never hardcoded. (LB-012; EV81:EVID-261)

### 3.8 Interfaces (consumed by id — no re-derivation)

- **HN-PAYR-FR-132:** The system shall tag IHSS cash *prestaciones*
  (benefits) and subsidies as non-taxable — LI Art. 92: prestaciones en
  dinero "no serán gravables por impuesto alguno" — as a line-level flag
  consumed BY ID by the ISR layer: exclusion semantics = taxation/02
  (HN-TAX-FR-046..078, Art. 10 exclusions) and the plantilla-side
  exclusion = taxation/04 HN-TAX-FR-130; this file owns only the tagging,
  never the ISR treatment. (LB-014; EV81:EVID-263)
- **HN-PAYR-FR-133:** The system shall CITE, never own, the subsidy frame:
  LI Arts. 34.b/39.b/42.2 (subsidy amount/duration delegated to
  reglamentos), Art. 90 (mutual incompatibility), Art. 91 (1-year claim
  prescription) and the RIT mechanics they authorize — all owned by file 04
  (`04_ihss-incapacidad.md`, HN-PAYR-FR-141..170), which consumes this
  file's ceilings and rates by id. (LB-014; EV81:EVID-263)
- **HN-PAYR-FR-134:** The system shall expose this file's dated-row lookups
  as the single source for: the IVM techo (consumed by file 05,
  HN-PAYR-FR-181..215 — RAP base split), the combined worker-share rates
  (consumed by the payslip engines of files 01/02 only through this file's
  rule objects), and the ceiling values consumed by file 04's
  techo-capped subsidy base — all by id and dated-row lookup, no sibling
  file re-declares rates or ceilings. (LB-001; LB-002;
  EV81:EVID-251/252)
- **HN-PAYR-FR-135:** The system shall record the ingestion-depth boundary
  for IHSS history (D-H3): where an IHSS-side accrual exists in this file
  (the cotización liability rows), historical ingestion uses MONTHLY
  AGGREGATES per contract — never payslip-level import — with regime
  cutovers (e.g. the 28-may-2024 D.48 row boundary) handled as dated config
  rows resolved by the original period, and filed periods write-protected.
  (LB-002; LB-003; EV81:EVID-252/253)

## 4. Data Model

No CSV sidecar is allocated to this file; the rate/ceiling seed rows below
ship as dated module data (additive-only, D-H2). Amounts exactly as printed
in the instruments.

**Cotización rates and ceilings (dated rows):**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| l10n_hn.ihss.rate (new) | branch, employer_pct, worker_pct, state_pct, valid_from, valid_to, source_kind, gazette_ref | select/float/date/char | branch: ivm · em; rows seeded: ivm 3.5/2.5/0.5 (valid_from 2024-05-28, statute d48_2024); em 5/2.5/0.5 (valid_from 2001-06-01, statute d80_2001, R-H65 citation); ivm 2/1/0.5 (valid_to 2024-05-27, superseded floor + interregnum caveat); state_pct informational only (FR-105) | FR-101..FR-107 |
| l10n_hn.ihss.ceiling (new) | regime, valid_from, valid_to, amount, source_kind, gazette_ref | select/date/monetary/char | TWO families, never merged (R-H50): ivm 2024-05-28→2024-12-31 = 11,336.32; ivm 2025 = 11,903.13; em 2024-05-28→2024-12-31 = 11,109.30; em 2025 = 11,903.13; post-2025 = jd_resolution rows (actuarial study); lookup by (regime, payslip period); missing rows = blocking config gap | FR-108..FR-112 |
| l10n_hn.ihss.base.config (new) | include_13th, include_14th, include_overtime, include_bonuses, in_kind_equivalence_rules, status | boolean/char | status: pending_source (Reglamento General unacquired, 87_ OQ-1 TOP lead) · configured; NEVER seeded with guessed defaults | FR-115, FR-116 |
| l10n_hn.ihss.multa (new) | concept, smm_factor | select/float | concept: non_affiliation (0.25) · late_planilla (1.0) · employer_share_deduction (3.0); unit = highest-category monthly SMM resolved by period from P1 rows (file 01) | FR-120, FR-131 |

**Worker and employer surfaces:**

| Entity | Field | Type | Catalog / values | Reference |
|--------|-------|------|------------------|-----------|
| hr.employee | ihss_affiliate_id, ihss_exclusion, ihss_voluntary_category | char/select | exclusion: none · family_minor_of_employer · armed_forces · other_public_regime · express_exclusion · foreign_temporary_ivm_only · diplomatic · diputado; voluntary categories per LI Art. 4 (optional flags) | FR-123..FR-126 |
| hr.contract | ihss_inscription_date, ihss_cesacion_notified | date/boolean | hire→inscription and termination→cesación workflow hooks (deadlines pending Reglamento General) | FR-123 |
| hr.payslip | ihss_ivm_base, ihss_em_base, ihss_worker_ivm, ihss_worker_em, ihss_employer_ivm, ihss_employer_em, ihss_resolved_ceiling_snapshot | monetary (computed+stored) | per-regime capped bases and shares; snapshot-on-write of resolved rates/ceilings (D15); frozen on paid slips, corrections use original-period rows (D16) | FR-103, FR-110, FR-113, FR-114, FR-118 |
| hr.salary.rule (IHSS categories) | worker share rules tied to rate rows; employer charge rules; missed-withholding recovery + employer-absorption rules | payroll rules | withholding at payment date; 1-month cure window; employer-share deduction guard (hard constraint) | FR-118..FR-120 |
| res.company | ihss_solvency_status, ihss_mora_flag | select/boolean | solvencia: al_dia · mora · unknown (procurement/collection gate hook); mora → benefits assumed by employer (execution in file 04 by id) | FR-128, FR-129 |
| account.move.line (IHSS payable ledger) | prescription_class, retained_unremitted_flag | select/boolean | worker_retained_imprescriptible (never prescribes) · employer_share_5y; mora recargo metadata field (rate source external) | FR-121, FR-130 |

## 5. Odoo Mapping

Layer semantics for this wave: `odoo` = computation/bookkeeping logic living
in the LGPL client (hr_payroll engine + dated config models). No SaaS rows
are introduced: none of these FRs touch the thin-client/SaaS architecture
split — IHSS cotizaciones are payroll-internal computations with no
electronic-filing surface in the corpus (no DJIMR/DTE-like channel exists for
planilla de cotización in the evidence; if IHSS publishes one it arrives as a
new wave). Model names stable across Odoo 17/18/19/20; version-specific
behavior recorded per row where a legal vintage exists.

| FR | Layer | Odoo model | Field(s) | Notes / version differences |
|----|-------|------------|----------|------------------------------|
| FR-101..FR-107 | odoo | l10n_hn.ihss.rate | dated rows + provenance | Version regime (D12): IVM row valid_from 2024-05-28 (D.48 publication day); EM row from the D.80-2001 regime (R-H65: cite signature 1-jun-2001 + G 29,503 14-jun-2001); superseded floor valid_to 2024-05-27 with lex-posterior supersession note (81_ OQ-4); D15/D16: snapshot-on-write, original-period recompute; chronology metadata per FR-107 |
| FR-108..FR-112 | odoo | l10n_hn.ihss.ceiling | two regime families | D12: 2024 rows bounded 2024-05-28→12-31 (mid-year vigencia); 2025 rows calendar-year; post-2025 = JD rows (external ingestion, watch La Gaceta); pre-28-may-2024 and missing-JD-year periods = blocking config gap (never-guess); R-H50: 2025 equality never merged; IVM-techo export consumed by file 05 by id |
| FR-113..FR-117 | odoo | hr.payslip compute + l10n_hn.ihss.base.config | capped bases + composition flag | R-H51: base = min(remuneration, techo) per regime, never flat-to-ceiling without IHSS confirmation (81_ OQ-1 guard); composition (13th/14th/OT/bonuses) = config flag pending Reglamento General (87_ OQ-1 TOP lead — never hardcoded); in-kind equivalence pending config; LI Art. 106 recourse = metadata pointer to file 10 |
| FR-118..FR-123 | odoo | hr.salary.rule (IHSS) + hr.payslip + hr.contract/hr.employee | withholding rules + cure window + affiliate data | Withholding stamped at payment date (LI Art. 62); 1-month cure then employer-borne absorption line; employer-share deduction = hard validation block (LI Art. 63 void rule); mora recargo floor = external rate, metadata only; inscription/cesación hooks with Reglamento-pending deadlines |
| FR-124..FR-126 | odoo | hr.employee flags | affiliation scope | Mandatory for any salaried worker money-or-kind any-relationship (LI Art. 3); exclusion catalog incl. foreign_temporary_ivm_only (EM lines suppressed); voluntary categories optional; zonal coverage = per-establishment data flag (87_ OQ-5) |
| FR-127 | odoo | l10n_hn.ihss.rate (branch rp — no row seeded) | config gap | RP employer-only per LI Art. 45; rate absent from corpus (87_ OQ-2): no RP line computed until JD/Reglamento rate arrives; CT Título V residual = file 09 |
| FR-128..FR-131 | odoo | res.company + l10n_hn.ihss.multa + account.move.line | enforcement metadata | Solvencia gate flag (procurement hook); mora → benefits-assumed-by-employer switch (execution in file 04 by id); prescription classes: employer 5y vs worker-retained imprescriptible; multa unit = P1 SMM rows by period (file 01 by range) |
| FR-132..FR-134 | odoo | line tagging + id-based lookups | interfaces | Prestaciones non-gravable tag consumed by taxation/02 (HN-TAX-FR-046..078) + taxation/04 (HN-TAX-FR-130); subsidy frame cited-not-owned (file 04 HN-PAYR-FR-141..170); rates/ceilings exported by id to files 02/04/05 — no sibling re-declaration |
| FR-135 | odoo | historical ingestion surface | monthly aggregates | D-H3: monthly aggregates per contract for IHSS liability rows, never payslip-level import; D16: filed-period write-protection; D18/D19: not applicable — no go-live GL/declaration surface owned here (config rows only) |

Version-regime notes (D12): FR-101/FR-108 record D.48-2024 with effectivity
2024-05-28 (publication day, no adaptation window in the instrument); FR-111
records the post-2025 JD dependency (annual actuarial cycle, no fixed date —
watch instrument). D15/D16 applicability: every rate/ceiling resolution is
anchor-dated by the payslip period, snapshotted on write, and corrections
recompute with original-period rows; paid slips frozen. D18/D19: no go-live
declaration or GL routing surfaces belong to this file (one-line reason in
the table).

## 6. Acceptance Criteria

- **AC-001:** Given a payslip period of June 2024, then the matrix resolves
  IVM 3.5/2.5 + EM 5/2.5 → worker withholding rate 5.0% and employer charge
  rate 8.5%, composed from the two regime rows (no single merged rate row
  exists in config) (FR-101..FR-103).
- **AC-002:** Given a December-2024 monthly remuneration of L20,000.00, then
  IVM base = min(20,000, 11,336.32) = L11,336.32 and EM base =
  min(20,000, 11,109.30) = L11,109.30; worker shares = 2.5% × 11,336.32 +
  2.5% × 11,109.30 = 283.41 + 277.73 = L561.14; employer charges = 3.5% ×
  11,336.32 + 5% × 11,109.30 = 396.77 + 555.47 = L952.24 (FR-108,
  FR-113, FR-114).
- **AC-003:** Given a 2025 monthly remuneration of L10,000.00 (below both
  ceilings), then both bases = L10,000.00, worker withholding = L500.00,
  employer charge = L850.00 (FR-113).
- **AC-004:** Given the 2025 configuration, then TWO ceiling rows exist at
  L11,903.13 — one `ivm_2025`, one `em_2025` — and deactivating/superseding
  one family never affects the other (R-H50 coincidence guard) (FR-108).
- **AC-005:** Given a payslip period of 15-mar-2024 (pre-vigencia), then the
  computation is BLOCKED with a missing-ceiling config flag — never the
  D.48 ceilings, never the 55-A ¶2 floor with a guessed techo (FR-104,
  FR-109).
- **AC-006:** Given a January-2026 run with no JD actuarial ceiling row
  loaded, then the computation is blocked with a missing-ceiling flag —
  never the 2025 values, never an indexed derivation (FR-111).
- **AC-007:** Given a December payslip carrying a 13th-month component with
  the base-composition flag unconfigured, then the cotización computation
  surfaces a pending-base-composition flag and produces no silently
  included/excluded base for that component (FR-115).
- **AC-008:** Given an attempt to book any employer-share amount (e.g.
  L952.24) as a worker deduction line, then the record is rejected by the
  validation guard (employer-share deduction absolutely void) (FR-120).
- **AC-009:** Given a worker share of L500.00 missed at the 30-apr payment,
  then recovery lines may attach to payments through 30-may (1-month cure
  window); given no recovery by then, a L500.00 employer-borne absorption
  line is generated and the worker is no longer debit-able for it
  (FR-119).
- **AC-010:** Given an unaffiliated worker discovered in a period whose P1
  highest-category SMM row resolves to X, then the non-affiliation multa =
  0.25 × X, the late-planilla multa = 1.0 × X per late planilla, and the
  employer-share-deduction multa = 3.0 × X — all resolved by period from
  the P1 feed, never hardcoded (FR-131).
- **AC-011:** Given the company's IHSS mora flag set, then the solvencia
  status reads mora, the benefits-assumed-by-employer flag is set (execution
  of the subsidy-side switch verifiable in file 04's ACs by id), and the
  procurement-solvency hook reports not-al-día (FR-128, FR-129).
- **AC-012:** Given a temporarily-contracted foreign worker (exclusion e),
  then the payslip carries IVM lines only (2.5% worker / 3.5% employer on
  the IVM base) and NO EM lines (FR-125).
- **AC-013:** Given a retained-but-unremitted worker share of L561.14, then
  the payable line carries prescription_class =
  worker_retained_imprescriptible, while the employer-share balance of the
  same period carries the 5-year prescription class (FR-130).
- **AC-014:** Given an IHSS subsidy line on a payslip, then it is tagged
  non-gravable and the ISR engines consume that tag by id (taxation/02
  HN-TAX-FR-046..078; taxation/04 HN-TAX-FR-130) without this file deriving
  any ISR treatment (FR-132).
- **AC-015:** Given the file-05 RAP engine requesting the IVM techo for a
  Dec-2024 payslip, then the lookup serves L11,336.32 by id from this
  file's `ivm_2024` row — and serves L11,903.13 for a 2025 period from the
  SEPARATE `ivm_2025` row (FR-112, FR-134).

## 7. Open Questions

| ID | Question | Blocking? | Owner | Status |
|----|----------|-----------|-------|--------|
| OQ-001 | `81_ OQ-1` cap semantics ("porcentajes se aplicarán sobre los techos") → RESOLVED by ruling R-H51: base = min(monthly remuneration, regime techo), per the LI Art. 55-B "remuneración máxima" precedent; encoded in FR-113 with the never-flat-without-IHSS-confirmation guard. | no | — | resolved (R-H51) |
| OQ-002 | `81_ OQ-2` pre-28-may-2024 interregnum: for payslip periods 2024-01-01→2024-05-27 (and the 2022→2024 revival window after SCO-858-2015) the operative ceilings are unaudited — LI 55-A ¶2 floor presumably revived but the JD ceiling trail 2003→2024 is not in the corpus. Acquisition lead: JD ceiling resolutions (La Gaceta) 2003-2024; until then historical/back-dated payslips stay config-blocked (FR-104/FR-109). | no | acquisition queue | open |
| OQ-003 | `81_ OQ-3` Estado 0.5% base ("en base del total de los afiliados activos") is grammatically broken in the gazette original; not employer-payroll-relevant (never withheld), but pin before modeling any Estado-side row (FR-105 keeps State shares informational). | no | acquisition queue | open |
| OQ-004 | `81_ OQ-4` supersession formality: D.48-2024 Art. 1 carries no express derogation of LI 55-A ¶2; supersession follows lex posterior + restitutory considerandos (R-H49 kin). Encoded in FR-104; a formal derogation analysis only matters for litigious edges. | no | — | open (note) |
| OQ-005 | `87_ OQ-1` → **RESOLVED W9 (145_ acquired)**: the Reglamento General = Acuerdo 003-JD-2005 (Dado 15-feb-2005, gazette G 30,735 29-jun-2005 per `147_`; `145_` = institutional "última versión"; `146_` = the 1971 Reglamento de Aplicación it replaced, Acuerdo 101-JD-71 inference). Art. 135 = the delegate base definition — OT/horas extras + rest-day value + commissions + habitual bonificaciones IN; occasional/mere-liberality primas/bonos/gratificaciones OUT (FR-115 rewritten; LB-015). RESIDUAL = the 14th-month leg → OQ-010. | no | — | resolved (W9/EV145:EVID-545) |
| OQ-006 | `87_ OQ-2` riesgos profesionales cotización: NARROWED W9 — the Reglamento General RP chapter (`145_` EV145:EVID-549) supplies the machinery (0.2% new-entrant entry rate on nominal salary at the techo, five classes, annual siniestralidad review + January employer filing, ≥1-year stability; FR-127/LB-017). RESIDUAL: the class-value cuadros / JD rate tables still unacquired — class rates stay config-gapped. Lead: JD cuadro de cuotas por clase. | no | acquisition queue (narrowed) | open |
| OQ-007 | `87_ OQ-4` ceiling trail 2003→2024 (JD acts raising L4,800 → ~L11k, incl. the voided D.56-2015 gradualidad): needed only for historical dated rows; same acquisition family as OQ-002. | no | acquisition queue | open |
| OQ-008 | `87_ OQ-5` gradual coverage per zone/category (LI Art. 1): whether every formal-sector employer is inside EM+IVM today is practice data; per-establishment affiliation coverage carried as a data flag (FR-126), never assumed national-by-default. | no | Takumi S-HN4 + controller | open |
| OQ-009 | `87_ OQ-3` → RESOLVED as R-H65: the TSC print's title-page dates are internally inconsistent (edition defect, not mislabel); LB citations use the signature date 1-jun-2001 + G 29,503 of 14-jun-2001. No further action. | no | — | resolved (R-H65) |
| OQ-010 | 14th-month (*décimo cuarto mes*) inclusion in the IHSS base: the Reglamento General Art. 135 includes "bonificaciones habituales" generically, but the 14th month is an SMM-average-variant statutory payment (payroll/02 FR-094..096) whose salary-nature for cotización purposes is not adjudicated by any corpus instrument (D. 117-2021's cotizaciones exemption names only the aguinaldo). FR-115(d) holds it as a config flag — never guessed either way. | no | S-HN5 / acquisition watch | open |
| OQ-011 | W10 REAP (from `155_` OQs): (a) the domésticos cotización VALUES live in a JD-acuerdo family instrument (006-JD-2008 Art. 18 delegates to JD majority per actuarial studies — same delegation class as LB-015's Art. 136 ceilings/OQ-006) — unacquired, config-gapped, never guessed; (b) the REAP regime's CURRENT operative status (post-2013 Ley RAP, post-2024 IHSS reforms) unverified — whether the annual-prepaid lane still governs domésticos or a later instrument moved them needs a status check (ihss.hn reglamentos family); the optional-IVM bridge's rates = the Ley's standard worker/employer split per the Ley IHSS Arts. (87_ family by id). | no | acquisition watch (JD acuerdo family + status check) | open (new W10) |
| OQ-012 | W11 amnistía family (from `161_`/`162_` OQs): (a) the Reglamento Especial's own gazette publication (its Art. 23 duty) is unpinned — the corpus copy is the IHSS institutional print (a G ~nov/dic-2016 print would be the record copy; ENAG route available; LOW priority, window closed, content not in doubt); (b) minor: D.L. 112-2016's 44-day Ejecútese-to-publication lag (12-sep→26-oct-2016) unexplained in the print — no legal effect turns on it (vigencia = publication day). | no | LOW watch | open (new W11) |
